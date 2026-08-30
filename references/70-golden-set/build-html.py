#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the strategy wiki into one portable HTML file.

No dependencies and no build step: markdown to HTML through our own converter, every page
in one document, navigation by anchors. Opens from disk, from email and on a phone.

  python3 build-html.py <wiki-folder> [output.html]
"""
import html, os, re, sys

def discover(src):
    """Page order: index first, then numbered pages, appendix last.
    Independent of the language the filenames are written in."""
    root = sorted(f[:-3] for f in os.listdir(src) if f.endswith(".md"))
    apx = []
    ap = os.path.join(src, "appendix")
    if os.path.isdir(ap):
        apx = sorted("appendix/" + f[:-3] for f in os.listdir(ap) if f.endswith(".md"))
    idx = [p for p in root if p == "index"]
    return idx + [p for p in root if p != "index"] + apx


def slug(name):
    return re.sub(r"[^a-zA-Zа-яА-Я0-9]+", "-", name).strip("-").lower()


CUR_PAGE = {"slug": ""}


def head_id(page_slug, heading):
    return f"{page_slug}--{slug(heading)}"


def inline(t):
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    # [[link|label]] and [[link]] -> an internal anchor
    def wiki(m):
        tgt = m.group(1).replace("../", "")
        anchor = (m.group(2) or "").strip()
        lab = m.group(3)[1:] if m.group(3) else (anchor or tgt)
        href = head_id(slug(tgt), anchor) if anchor else slug(tgt)
        return f'<a href="#{href}">{lab}</a>'
    t = re.sub(r"\[\[([^\]|#]+)(?:#([^\]|]+))?(\|[^\]]+)?\]\]", wiki, t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def convert(md):
    out, rows, in_tbl, in_quote = [], [], False, False
    def flush_tbl():
        nonlocal rows, in_tbl
        if not rows: return
        head, body = rows[0], rows[2:] if len(rows) > 2 else []
        out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>")
        for r in body:
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        out.append("</tbody></table>")
        rows, in_tbl = [], False
    def flush_quote():
        nonlocal in_quote
        if in_quote: out.append("</blockquote>"); in_quote = False

    for raw in md.split("\n"):
        line = raw.rstrip()
        if line.startswith("|") and line.endswith("|"):
            in_tbl = True
            rows.append([c.strip() for c in line.strip("|").split("|")])
            continue
        if in_tbl: flush_tbl()
        if line.startswith(">"):
            if not in_quote: out.append("<blockquote>"); in_quote = True
            out.append(f"<p>{inline(line.lstrip('> '))}</p>")
            continue
        flush_quote()
        if not line.strip():
            continue
        if line.startswith("---"):
            out.append("<hr>"); continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            hid = head_id(CUR_PAGE["slug"], txt)
            out.append(f'<h{lvl} id="{hid}">{inline(txt)}</h{lvl}>'); continue
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            out.append(f"<li>{inline(m.group(2))}</li>"); continue
        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            out.append(f"<li>{inline(m.group(3))}</li>"); continue
        out.append(f"<p>{inline(line)}</p>")
    flush_tbl(); flush_quote()
    # wrap consecutive li elements in a ul
    txt = "\n".join(out)
    txt = re.sub(r"(?:<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", txt, flags=re.S)
    return txt


CSS = """
:root{--bg:#fbfbfa;--fg:#1f2328;--mut:#5b6570;--line:#e4e6e8;--acc:#2fb9ca;--card:#fff;--code:#f3f4f6}
@media(prefers-color-scheme:dark){:root{--bg:#14171a;--fg:#e6e8ea;--mut:#9aa4ad;--line:#282d33;--acc:#43cadb;--card:#1b1f23;--code:#22272c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:250px 1fr;gap:40px}
nav{position:sticky;top:0;align-self:start;max-height:100vh;overflow:auto;padding:28px 0;font-size:14px}
nav a{display:block;padding:7px 10px;color:var(--mut);text-decoration:none;border-radius:6px;border-left:2px solid transparent}
nav a:hover{background:var(--card);color:var(--fg)}
nav a.on{color:var(--acc);border-left-color:var(--acc);background:var(--card)}
nav .grp{margin:16px 0 6px;padding-left:10px;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);opacity:.7}
main{padding:28px 0 96px;min-width:0}
section{margin-bottom:56px;scroll-margin-top:20px}
h1{font-size:30px;margin:.2em 0 .5em;line-height:1.25}
h2,h3{scroll-margin-top:16px}
h2{font-size:21px;margin:1.7em 0 .6em;padding-bottom:.3em;border-bottom:1px solid var(--line)}
h3{font-size:17px;margin:1.4em 0 .4em}
h4{font-size:15px;margin:1.2em 0 .3em;color:var(--mut)}
p{margin:.6em 0}
ul{margin:.5em 0;padding-left:22px}li{margin:.3em 0}
code{background:var(--code);padding:.13em .4em;border-radius:4px;font-size:.87em;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
blockquote{margin:1em 0;padding:.7em 1em;background:var(--card);border-left:3px solid var(--acc);border-radius:0 8px 8px 0}
blockquote p{margin:.3em 0}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:14px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:9px 11px;text-align:left;vertical-align:top}
th{background:var(--card);font-weight:600;white-space:nowrap}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
a{color:var(--acc)}
.hdr{padding:26px 0 6px;border-bottom:1px solid var(--line);margin-bottom:8px}
.hdr .t{font-size:13px;color:var(--mut)}
@media(max-width:900px){.wrap{grid-template-columns:1fr;gap:0}nav{position:static;max-height:none;border-bottom:1px solid var(--line)}nav a{display:inline-block}}
"""

JS = """
const secs=[...document.querySelectorAll('section')],links=[...document.querySelectorAll('nav a')];
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){
 links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+e.target.id));}})},{rootMargin:'-10% 0px -80% 0px'});
secs.forEach(s=>io.observe(s));
"""


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(src, "strategy.html")
    pages = []
    for name in discover(src):
        p = os.path.join(src, name + ".md")
        if not os.path.exists(p): continue
        md = open(p, encoding="utf-8").read()
        md = re.sub(r"^\[\[.*?\]\].*?\n", "", md, count=1)  # the breadcrumb is not needed
        title = re.search(r"^#\s+(.*)$", md, re.M)
        CUR_PAGE["slug"] = slug(name)
        pages.append((slug(name), name, title.group(1) if title else name, convert(md)))

    nav = []
    for sid, name, title, _ in pages:
        if name.startswith("appendix/") and "appendix" not in "".join(nav).lower():
            nav.append('<div class="grp">Appendix</div>')
        nav.append(f'<a href="#{sid}">{html.escape(title)}</a>')

    # a link to a sibling page inside a subfolder is written without the prefix - resolve it against the known anchors
    known = {sid for sid, _, _, _ in pages}
    body = "\n".join(f'<section id="{sid}">{h}</section>' for sid, _, _, h in pages)

    def fix(m):
        target = m.group(1)
        if target in known or target.split("--")[0] in known:
            return m.group(0)
        for k in known:
            if k.endswith("-" + target.split("--")[0]):
                return m.group(0).replace(target, k + target[len(target.split("--")[0]):])
        return m.group(0)
    body = re.sub(r'href="#([^"]+)"', fix, body)
    doc = f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(pages[0][2])}</title><style>{CSS}</style></head><body>
<div class="wrap"><nav><div class="hdr"><div class="t">BI+AI strategy</div></div>
{''.join(nav)}</nav><main>{body}</main></div><script>{JS}</script></body></html>"""
    open(dst, "w", encoding="utf-8").write(doc)
    print(f"built {len(pages)} pages -> {dst}  ({os.path.getsize(dst)//1024} KB)")


if __name__ == "__main__":
    main()
