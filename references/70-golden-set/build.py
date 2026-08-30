#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild tier 1 of the golden set from ../faq-participants.md.

Tier 1 is generated; tiers 2 and 3 are maintained by hand.
Run with:  python3 build.py
"""
import re, sys, pathlib

SRC = pathlib.Path(__file__).parent / ".." / "faq-participants.md"
DST = pathlib.Path(__file__).parent / "goldenset-tier1.yaml"

HEAD = """# The bi-strategy skill's golden set - tier 1: retrieval
#
# What it measures: did the agent find the right knowledge base atoms. Checked deterministically,
# with no LLM judge: the sets of atoms the agent cited are compared.
#
# THE FREEZE RULE: the set is frozen before any change to the KB and is NOT rephrased to match
# what the agent found. Rephrasing to suit retrieval is fitting to the test.
#
# Generated from ../faq-participants.md by build.py - do not edit by hand.
# Make the edits in the FAQ, then rebuild.
#
# mark: ◆ a real participant question · ◇ put up by the author for discussion · ○ constructed from the KB
# status: needs_review until the author has read it through; only confirmed counts

meta:
  tier: 1
  kind: retrieval
  generated_from: ../faq-participants.md
  scoring: "expected_atoms is a subset of cited_atoms -> hit; the metric is atom recall plus the share of questions hit in full"
  items: {n}

items:"""


def parse(text):
    items, sec = [], None
    for blk in re.split(r"\n## ", text):
        head = blk.split("\n", 1)[0].strip()
        m = re.match(r"^(\d+)\.\s+(.*)$", head)
        if m:
            sec = (int(m.group(1)), m.group(2))
        if not sec:
            continue
        for qm in re.finditer(
            r"^\*\*([◆◇○])\s*(.+?)\*\*\n(.+?)(?=\n\n|\Z)", blk, re.S | re.M
        ):
            mark, q, ans = qm.group(1), qm.group(2).strip(), qm.group(3).strip()
            items.append(
                dict(
                    section=sec[0],
                    section_title=sec[1],
                    mark=mark,
                    question=q,
                    atoms=sorted(set(re.findall(r"\[\[([^\]]+)\]\]", ans))),
                    files=sorted(set(re.findall(r"`([a-z\-]+\.md)`", ans))),
                )
            )
    return items


def render(items):
    out = [HEAD.format(n=len(items))]
    for n, i in enumerate(items, 1):
        q = i["question"].replace('"', '\\"')
        out += [
            f"  - id: gs1-{n:03d}",
            f"    section: {i['section']}   # {i['section_title']}",
            f'    mark: "{i["mark"]}"',
            f'    question: "{q}"',
            "    expected_atoms: [%s]" % ", ".join(i["atoms"]),
        ]
        if i["files"]:
            out.append("    expected_files: [%s]" % ", ".join(i["files"]))
        out.append("    status: needs_review")
    return "\n".join(out) + "\n"


def main():
    items = parse(SRC.read_text(encoding="utf-8"))
    if not items:
        sys.exit("could not parse the FAQ - check the question heading format")
    empty = [i["question"] for i in items if not i["atoms"] and not i["files"]]
    DST.write_text(render(items), encoding="utf-8")
    print(f"built {len(items)} items -> {DST.name}")
    if empty:
        print("NO ATOM REFERENCES (these questions cannot be scored):")
        for q in empty:
            print("  -", q)


if __name__ == "__main__":
    main()
