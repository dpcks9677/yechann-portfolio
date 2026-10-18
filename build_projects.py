#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로젝트 상세 페이지 빌더
- content/projects/shotgun-and-run/judgments.md  ->  projects/shotgun-and-run/index.html
- 판단 기록(마크다운)을 파싱해 접고 펼 수 있는 항목으로 렌더링한다.
- 실행: python build_projects.py   (블로그 빌드는 build.py 별도)
"""
import os
import re
import sys
import html
import markdown

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from projects_config import PROJECTS, PRETENDARD  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))


def tags(items):
    return "".join(f'<span class="tag tag-role">{t}</span>' for t in items)


md = lambda t: markdown.Markdown(extensions=["tables"]).convert(t)


def parse(path):
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"^## ", text, flags=re.M)
    how = ""
    items = []
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        head = head.strip()
        if head == "작성 방식":
            how = body.strip()
        elif head.startswith("판단"):
            m = re.match(r"판단\s*(\d+)\.\s*(.*)", head)
            no, title = int(m.group(1)), m.group(2).strip()
            fields = []
            for line in body.splitlines():
                fm = re.match(r"-\s+\*\*(.+?)\*\*\s*[:：]\s*(.*)", line)
                if fm:
                    fields.append([fm.group(1).strip(), fm.group(2).strip()])
                elif line.strip() and fields:
                    fields[-1][1] += " " + line.strip()
            items.append({"no": no, "title": title, "fields": fields})
    return how, items


def inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def render_item(it, extra, open_=False):
    rows = []
    for k, v in it["fields"]:
        cls = " limit" if k == "한계" else ""
        rows.append(
            f'<div class="jd-row{cls}"><dt>{html.escape(k)}</dt><dd>{inline(v)}</dd></div>'
        )
    o = " open" if open_ else ""
    figs = ""
    if it["no"] in extra:
        figs = '<div class="jd-figs">' + "".join(
            f'<figure><img src="{src}" alt="{html.escape(alt)}" loading="lazy" decoding="async">'
            f'<figcaption>{html.escape(cap)}</figcaption></figure>'
            for src, cap, alt in extra[it["no"]]) + '</div>'
    return (
        f'<details class="jd"{o} id="j{it["no"]}">'
        f'<summary><span class="jd-no">{it["no"]:02d}</span>'
        f'<span class="jd-title">{html.escape(it["title"])}</span>'
        f'</summary>'
        f'<dl>{"".join(rows)}</dl>{figs}</details>'
    )


def build(P):
    src = os.path.join(BASE, "content", "projects", P["slug"], "judgments.md")
    out_dir = os.path.join(BASE, "projects", P["slug"])
    how, items = parse(src)
    by_no = {i["no"]: i for i in items}
    feats = P["featured"]
    featured = "\n".join(render_item(by_no[n], P["extra"]) for n in feats)
    rest = "\n".join(render_item(i, P["extra"]) for i in items if i["no"] not in feats)
    everything = "\n".join(render_item(i, P["extra"]) for i in items)
    btns = "".join(
        f'<a class="btn{" btn-primary" if k == "primary" else ""}" href="{h}"'
        + ("" if h.startswith("#") else ' target="_blank" rel="noopener"') + f">{t}</a>"
        for k, h, t in P["buttons"]
    )
    cells = "".join(f'<div class="cell"><h3 class="sub">{h}</h3><p>{p}</p></div>' for h, p in P["cells"])
    page = TEMPLATE
    for k, v in {
        "{{TITLE}}": P["title"], "{{KICKER}}": P["kicker"], "{{DESC}}": P["desc"], "{{OG}}": P["og"],
        "{{HERO}}": P["hero"], "{{ROLES}}": tags(P["roles"]), "{{BUTTONS}}": btns, "{{PLAY}}": P["play"],
        "{{CELLS}}": cells,
        "{{AFTER_CELLS}}": P.get("after_cells", ""),
        "{{HERO_CLASS}}": " has-bg" if P.get("hero_bg") else "",
        "{{HERO_STYLE}}": f' style="background-image:url({P["hero_bg"]})"' if P.get("hero_bg") else "",
        "{{FEATURED_N}}": f"{len(feats)}건", "{{KEY_LEAD}}": P["key_lead"],
        "{{FEATURED}}": featured, "{{TOTAL}}": str(len(items)),
        "{{PRETENDARD}}": PRETENDARD,
    }.items():
        page = page.replace(k, v)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    dp = DECISIONS.replace("{{TITLE}}", P["title"]).replace("{{TOTAL}}", str(len(items))) \
        .replace("{{ALL_LEAD}}", P["all_lead"]).replace("{{ALL}}", everything).replace("{{PRETENDARD}}", PRETENDARD)
    with open(os.path.join(out_dir, "decisions.html"), "w", encoding="utf-8") as f:
        f.write(dp)
    print(f"[OK] projects/{P['slug']}/index.html + decisions.html ({len(items)} judgments)")


TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} — 김예찬</title>
<meta name="description" content="{{DESC}}">
<meta property="og:title" content="{{TITLE}} — 김예찬">
<meta property="og:description" content="{{OG}}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="{{PRETENDARD}}">
<link rel="stylesheet" href="../../styles.css">
</head>
<body>
<div class="shell" id="top">

<header class="nav">
  <a href="../../index.html" class="nav-brand">김예찬 <span>/ Project</span></a>
  <nav class="nav-links"><a href="../../index.html#work">← Work</a><a href="#key">핵심 판단</a><a href="decisions.html">전체 판단 기록</a></nav>
</header>

<section class="hero proj-hero{{HERO_CLASS}}"{{HERO_STYLE}}>
  <div class="kicker">{{KICKER}}</div>
  <h1>{{TITLE}}</h1>
  <p>{{HERO}}</p>
  <div class="tags role-tags">{{ROLES}}</div>
  <div class="btn-row">{{BUTTONS}}</div>
</section>

{{PLAY}}

<section class="section">
  <div class="split2">
    {{CELLS}}
  </div>
</section>

{{AFTER_CELLS}}

<section class="section" id="key">
  <div class="kicker">KEY DECISIONS</div>
  <h2 class="title-sm">핵심 판단 {{FEATURED_N}}</h2>
  <p class="lead" style="margin-top:14px;max-width:760px">{{KEY_LEAD}}</p>
  <div class="jd-list">
{{FEATURED}}
  </div>
</section>

<section class="section">
  <a class="btn" href="decisions.html">전체 판단 기록 {{TOTAL}}건 보기 →</a>
</section>

<section class="contact">
  <h2>더 궁금한 점이 있다면<br>연락 주세요</h2>
  <div class="contact-row">
    <div><div class="contact-lbl">EMAIL</div><a class="contact-val" href="mailto:yechann.dev@gmail.com">yechann.dev@gmail.com</a></div>
    <div><div class="contact-lbl">BACK</div><a class="contact-val" href="../../index.html#work">포트폴리오 홈</a></div>
  </div>
  <div class="copyright">© 2026 Kim Yechan</div>
</section>

</div>
</body>
</html>
"""

DECISIONS = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} 판단 기록 — 김예찬</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="{{PRETENDARD}}">
<link rel="stylesheet" href="../../styles.css">
</head>
<body>
<div class="shell" id="top">
<header class="nav">
  <a href="../../index.html" class="nav-brand">김예찬 <span>/ Project</span></a>
  <nav class="nav-links"><a href="index.html">← {{TITLE}}</a><a href="../../index.html#work">Work</a></nav>
</header>
<section class="section">
  <div class="kicker">ALL DECISIONS</div>
  <h2 class="title-sm">{{TITLE}} 판단 기록 {{TOTAL}}건</h2>
  <p class="lead" style="margin-top:14px;max-width:760px">{{ALL_LEAD}}각 항목은 상황 → 결정 → 이유 → 한계 순서입니다.</p>
  <div class="jd-list">
{{ALL}}
  </div>
</section>
<section class="contact">
  <div class="contact-row">
    <div><div class="contact-lbl">BACK</div><a class="contact-val" href="index.html">{{TITLE}} 소개로</a></div>
  </div>
  <div class="copyright">© 2026 Kim Yechan</div>
</section>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    for p in PROJECTS:
        build(p)
