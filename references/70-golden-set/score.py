#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scoring a golden set run.

Input: answers.jsonl - one record per question:
  {"id": "gs1-001", "cited_atoms": ["bi-strategy-purpose"], "answer": "the answer text"}
  {"id": "gs2-01",  "cited_atoms": [...], "answer": "...", "verdict": "correct_with_a_decision"}

Tier 1 is scored deterministically from cited_atoms.
Tiers 2 and 3 require the verdict field, set by an LLM judge against the rubric;
this script only aggregates and enforces the hard rule over must_not.

Run with:  python3 score.py answers.jsonl
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent


def load_yaml_items(path):
    """A minimal parser for our own format - no external dependencies."""
    items, cur, key = [], None, None
    for raw in path.read_text(encoding="utf-8").split("\n"):
        line = raw.rstrip()
        if re.match(r"^\s*#", line) or not line.strip():
            continue
        m = re.match(r"^  - id:\s*(\S+)", line)
        if m:
            cur = {"id": m.group(1), "must_not": [], "must_contain": []}
            items.append(cur)
            key = None
            continue
        if cur is None:
            continue
        m = re.match(r"^    (\w+):\s*\[(.*)\]\s*$", line)
        if m:
            cur[m.group(1)] = [x.strip() for x in m.group(2).split(",") if x.strip()]
            key = None
            continue
        m = re.match(r"^    (\w+):\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v:
                cur[k] = v.strip('"')
                key = None
            else:
                key = k
                cur[k] = []
            continue
        m = re.match(r"^      - (.*)$", line)
        if m and key:
            cur[key].append(m.group(1).strip())
    return items


def pct(a, b):
    return f"{100.0 * a / b:.1f}%" if b else "n/a"


def main(path):
    answers = {}
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            answers[r["id"]] = r

    print("=" * 68)
    # ---- tier 1: retrieval ----
    t1 = load_yaml_items(HERE / "goldenset-tier1.yaml")
    full, partial, miss, atom_hit, atom_tot, unanswered = 0, 0, 0, 0, 0, 0
    misses = []
    for it in t1:
        exp = set(it.get("expected_atoms", []))
        if not exp:
            continue
        a = answers.get(it["id"])
        if a is None:
            unanswered += 1
            continue
        got = set(a.get("cited_atoms", []))
        hit = exp & got
        atom_hit += len(hit)
        atom_tot += len(exp)
        if hit == exp:
            full += 1
        elif hit:
            partial += 1
            misses.append((it["id"], sorted(exp - got)))
        else:
            miss += 1
            misses.append((it["id"], sorted(exp - got)))
    scored = full + partial + miss
    print(f"TIER 1 · retrieval           answered {scored} of {scored + unanswered}")
    print(f"  full hit on atoms          {full:>3}  {pct(full, scored)}")
    print(f"  partial                    {partial:>3}  {pct(partial, scored)}")
    print(f"  missed                     {miss:>3}  {pct(miss, scored)}")
    print(f"  atom recall                    {pct(atom_hit, atom_tot)}")

    # ---- tiers 2 and 3: the judge ----
    for tier, fname, primary in (
        (2, "goldenset-tier2.yaml", "correct_with_a_decision"),
        (3, "goldenset-tier3.yaml", "refusal_with_a_continuation"),
    ):
        items = load_yaml_items(HERE / fname)
        counts, forced, no_verdict = {}, [], 0
        for it in items:
            a = answers.get(it["id"])
            if a is None:
                continue
            v = a.get("verdict")
            txt = (a.get("answer") or "").lower()
            # the hard rule: a match against must_not overrides the judge's verdict
            for bad in it.get("must_not", []):
                probe = [w for w in re.findall(r"[a-z0-9]{5,}", bad.lower())][:3]
                if probe and all(w in txt for w in probe):
                    v = "wrong_or_invented" if tier == 2 else "invented_an_answer"
                    forced.append((it["id"], bad))
                    break
            if not v:
                no_verdict += 1
                continue
            counts[v] = counts.get(v, 0) + 1
        tot = sum(counts.values())
        label = "answer quality" if tier == 2 else "honest refusal"
        print(f"\nTIER {tier} · {label:<16} scored {tot} of {len(items)}")
        for k, n in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {k:<26} {n:>3}  {pct(n, tot)}")
        if primary in counts:
            print(f"  PRIMARY METRIC             {pct(counts[primary], tot)}")
        if no_verdict:
            print(f"  no judge verdict           {no_verdict}")
        if forced:
            print("  the hard rule fired (must_not):")
            for i, b in forced:
                print(f"    {i}: {b}")

    if misses:
        print("\nATOMS NOT FOUND (tier 1) - where to look on a regression:")
        for i, m in misses[:15]:
            print(f"  {i}: {', '.join(m)}")
        if len(misses) > 15:
            print(f"  ... and {len(misses) - 15} more")
    print("=" * 68)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
