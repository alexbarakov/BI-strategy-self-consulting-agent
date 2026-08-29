# -*- coding: utf-8 -*-
"""Генератор SVG-визуализации зрелости по темам (как в Data & Analytics Maturity Tool).
Горизонтальный бар-чарт 0–4 с зонами Beginning / Learning / Developing / Mastering.
Использование: заполни SCORES само-оценкой участника (0–4) и OUT — путь к svg в вики (assets/maturity.svg).
Вставляй в 00-Диагностика.md как ![Профиль зрелости по темам](assets/maturity.svg)."""

# (тема, оценка 0–4) — 9 категорий Health Check + AI-readiness оверлей
SCORES = [
    ("Связь с бизнесом", 3.0),
    ("Adoption и удовлетворённость", 2.0),
    ("Управление контентом", 2.0),
    ("Self-Service delivery", 2.0),
    ("Guided delivery / поддержка", 1.0),
    ("Платформа: semantic / каталог", 1.0),
    ("Data Quality", 2.0),
    ("Безопасность и комплаенс", 2.0),
    ("Управление BI-проектом", 3.0),
    ("AI-readiness (оверлей)", 1.4),
]
OUT = "assets/maturity.svg"

def color(v):
    return "#E5534B" if v < 1 else "#E0A82E" if v < 2 else "#4CAF6E" if v < 3 else "#1F8A46"

def build(scores):
    bands = [(0,"#E5534B","Beginning"),(1,"#E0A82E","Learning"),(2,"#4CAF6E","Developing"),(3,"#1F8A46","Mastering")]
    tint = {"#E5534B":"#FBECEA","#E0A82E":"#FBF3DD","#4CAF6E":"#E9F6EE","#1F8A46":"#E1F1E7"}
    W, L, R = 780, 250, 760
    unit = (R - L) / 4.0
    rowh, top = 34, 84
    H = top + len(scores) * rowh + 34
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         '<text x="20" y="34" font-size="18" font-weight="700" fill="#171A26">Профиль зрелости по темам (0–4)</text>',
         '<text x="20" y="54" font-size="12" fill="#7A8299">Само-оценка · зоны: Beginning · Learning · Developing · Mastering</text>']
    for lo, c, name in bands:
        x = L + lo * unit
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{unit:.1f}" height="{len(scores)*rowh}" fill="{tint[c]}"/>')
        s.append(f'<text x="{x+unit/2:.1f}" y="{top-8}" font-size="10.5" fill="{c}" text-anchor="middle" font-weight="700">{name}</text>')
    for t in range(5):
        x = L + t * unit
        s.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+len(scores)*rowh}" stroke="#D9DFEA" stroke-width="1"/>')
        s.append(f'<text x="{x:.1f}" y="{top+len(scores)*rowh+18}" font-size="11" fill="#7A8299" text-anchor="middle">{t}</text>')
    for i, (name, v) in enumerate(scores):
        y = top + i * rowh + 6; bh = rowh - 12; c = color(v)
        s.append(f'<text x="{L-12}" y="{y+bh/2+4:.1f}" font-size="12.5" fill="#171A26" text-anchor="end">{name}</text>')
        s.append(f'<rect x="{L}" y="{y:.1f}" width="{max(2,v*unit):.1f}" height="{bh}" rx="3" fill="{c}"/>')
        s.append(f'<text x="{L+v*unit+8:.1f}" y="{y+bh/2+4:.1f}" font-size="12" font-weight="700" fill="{c}">{v:g}</text>')
    s.append('</svg>')
    return "\n".join(s)

if __name__ == "__main__":
    import os
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(build(SCORES))
    print("saved", OUT)
