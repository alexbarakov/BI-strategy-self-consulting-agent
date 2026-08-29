#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пересборка уровня 1 голден-сета из ../faq-participants.md.

Уровень 1 генерируется, уровни 2 и 3 ведутся руками.
Запуск:  python3 build.py
"""
import re, sys, pathlib

SRC = pathlib.Path(__file__).parent / ".." / "faq-participants.md"
DST = pathlib.Path(__file__).parent / "goldenset-tier1.yaml"

HEAD = """# Голден-сет скилла bi-strategy — уровень 1: retrieval
#
# Что меряет: нашёл ли агент нужные атомы базы знаний. Проверяется детерминированно,
# без LLM-судьи: сравниваются множества атомов, на которые агент сослался.
#
# ПРАВИЛО ФИКСАЦИИ: набор фиксируется до изменений в KB и НЕ переформулируется под то,
# что агент нашёл. Переформулировка под поиск — это подгонка под тест.
#
# Генерируется из ../faq-participants.md скриптом build.py — руками не править.
# Правки вносятся в FAQ, затем пересборка.
#
# mark: ◆ реальный вопрос участника · ◇ вынесен автором на обсуждение · ○ достроен из KB
# status: needs_review до вычитки автором; в зачёт идут только confirmed

meta:
  tier: 1
  kind: retrieval
  generated_from: ../faq-participants.md
  scoring: "expected_atoms ⊆ cited_atoms → hit; метрика = recall по атомам и доля вопросов с полным попаданием"
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
        sys.exit("не удалось разобрать FAQ — проверь формат заголовков вопросов")
    empty = [i["question"] for i in items if not i["atoms"] and not i["files"]]
    DST.write_text(render(items), encoding="utf-8")
    print(f"собрано {len(items)} позиций → {DST.name}")
    if empty:
        print("БЕЗ ССЫЛОК НА АТОМЫ (такие вопросы не скорятся):")
        for q in empty:
            print("  -", q)


if __name__ == "__main__":
    main()
