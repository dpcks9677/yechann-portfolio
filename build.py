#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
정적 마크다운 블로그 빌더 (build.py)
- content/posts/*.md -> blog/index.html (2단 티스토리 레이아웃) & blog/posts/*.html
- 카테고리 기준 이전/다음 글 네비게이션
- 읽는 시간 제거, 태그 발행일 하단 배치, 제목 상단 카테고리 표시
"""

import os
import sys
import re
import markdown

# Windows PowerShell cp949 encoding safe setup
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(BASE_DIR, "content", "posts")
BLOG_DIR = os.path.join(BASE_DIR, "blog")
BLOG_POSTS_DIR = os.path.join(BLOG_DIR, "posts")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def parse_frontmatter(content):
    """YAML Frontmatter 추출 및 파싱"""
    frontmatter = {}
    body = content

    pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
    match = re.match(pattern, content, re.DOTALL)
    if match:
        fm_raw = match.group(1)
        body = match.group(2)

        for line in fm_raw.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip("\"'")

                # Parse boolean
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                # Parse list e.g. ["Unity", "C#"]
                elif val.startswith("[") and val.endswith("]"):
                    items = val[1:-1].split(",")
                    val = [item.strip().strip("\"'") for item in items if item.strip()]
                elif key == "tags" and "," in val:
                    val = [item.strip() for item in val.split(",") if item.strip()]
                
                frontmatter[key] = val

    if "tags" in frontmatter and isinstance(frontmatter["tags"], str):
        frontmatter["tags"] = [frontmatter["tags"]]
    elif "tags" not in frontmatter:
        frontmatter["tags"] = ["General"]

    if "category" not in frontmatter or not frontmatter["category"]:
        frontmatter["category"] = "일반"

    return frontmatter, body

def preprocess_markdown(text):
    """코드 블록 외부에서 일반 텍스트 바로 뒤에 리스트가 올 경우 빈 줄을 자동 삽입하여 CommonMark(marked.js)와 동일하게 <ul>로 파싱"""
    lines = text.splitlines()
    new_lines = []
    in_code = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code = not in_code
        if not in_code and i > 0:
            prev = lines[i - 1].strip()
            curr = line.strip()
            is_list = re.match(r"^([*+-]|\d+\.)\s+", curr)
            prev_is_list = re.match(r"^([*+-]|\d+\.)\s+", prev)
            if is_list and prev and not prev_is_list and not prev.startswith("#"):
                new_lines.append("")
        new_lines.append(line)
    return "\n".join(new_lines)

def load_posts():
    """모든 마크다운 포스트 로드 및 정렬 (하위 디렉토리 재귀 탐색)"""
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR, exist_ok=True)
        return []

    posts = []
    for root, dirs, files in os.walk(POSTS_DIR):
        for fname in files:
            if fname.endswith(".md"):
                slug = os.path.splitext(fname)[0]
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()

            fm, body = parse_frontmatter(content)
            title = fm.get("title", slug.replace("-", " ").title())
            date_str = fm.get("date", "2026-01-01")
            category = fm.get("category", "일반")
            desc = fm.get("description", "")
            tags = fm.get("tags", ["General"])

            # Markdown conversion
            cleaned_body = preprocess_markdown(body)
            md = markdown.Markdown(extensions=["fenced_code", "tables", "nl2br"])
            html_content = md.convert(cleaned_body)

            posts.append({
                "slug": slug,
                "title": title,
                "date": date_str,
                "category": category,
                "description": desc,
                "tags": tags,
                "body_html": html_content,
                "raw_date": date_str,
                "ctime": os.path.getctime(fpath),
                "mtime": os.path.getmtime(fpath),
            })

    # 전체 최신 날짜순 정렬 (날짜가 같을 경우 파일 생성시간/수정시간 최신순)
    posts.sort(key=lambda p: (p["raw_date"], p["ctime"], p["mtime"]), reverse=True)
    return posts

def group_posts_by_category(posts):
    """카테고리별로 포스트 그룹핑 (최신순 유지)"""
    grouped = {}
    for p in posts:
        cat = p["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(p)
    return grouped

def build_post_pages(posts, grouped_posts):
    """개별 포스트 상세 페이지 생성 (카테고리 기준 이전/다음 글)"""
    os.makedirs(BLOG_POSTS_DIR, exist_ok=True)
    valid_files = {f"{p['slug']}.html" for p in posts}
    for f in os.listdir(BLOG_POSTS_DIR):
        if f.endswith(".html") and f not in valid_files:
            try:
                os.remove(os.path.join(BLOG_POSTS_DIR, f))
            except Exception:
                pass

    template_path = os.path.join(TEMPLATES_DIR, "blog-post.html")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    for post in posts:
        cat = post["category"]
        cat_posts = grouped_posts[cat]
        # Find index within the same category
        idx = cat_posts.index(post)
        newer_post = cat_posts[idx - 1] if idx > 0 else None
        older_post = cat_posts[idx + 1] if idx < len(cat_posts) - 1 else None

        # Previous post in category
        if older_post:
            prev_html = f'''<a href="{older_post['slug']}.html" class="post-nav-btn">
  <span class="post-nav-category-badge">[{cat}] 이전 글</span>
  <span class="nav-title">{older_post['title']}</span>
</a>'''
        else:
            prev_html = f'''<div class="post-nav-btn" style="opacity:0.4;cursor:default">
  <span class="post-nav-category-badge">[{cat}]</span>
  <span class="nav-sub">카테고리의 첫 번째 글입니다</span>
</div>'''

        # Next post in category
        if newer_post:
            next_html = f'''<a href="{newer_post['slug']}.html" class="post-nav-btn" style="text-align:right">
  <span class="post-nav-category-badge">[{cat}] 다음 글</span>
  <span class="nav-title">{newer_post['title']}</span>
</a>'''
        else:
            next_html = f'''<div class="post-nav-btn" style="text-align:right;opacity:0.4;cursor:default">
  <span class="post-nav-category-badge">[{cat}]</span>
  <span class="nav-sub">카테고리의 최신 글입니다</span>
</div>'''

        tags_html = "".join([f'<span class="tag">{t}</span>' for t in post["tags"]])

        rendered = template
        rendered = rendered.replace("{{CATEGORY}}", post["category"])
        rendered = rendered.replace("{{TITLE}}", post["title"])
        rendered = rendered.replace("{{DESCRIPTION}}", post["description"])
        rendered = rendered.replace("{{DATE}}", post["date"])
        rendered = rendered.replace("{{TAGS}}", tags_html)
        rendered = rendered.replace("{{CONTENT}}", post["body_html"])
        rendered = rendered.replace("{{PREV_POST}}", prev_html)
        rendered = rendered.replace("{{NEXT_POST}}", next_html)

        out_path = os.path.join(BLOG_POSTS_DIR, f"{post['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"  [Post] -> blog/posts/{post['slug']}.html (Cat: {cat})")

def build_blog_index(posts, grouped_posts):
    """블로그 메인 페이지(2단 티스토리 레이아웃) 생성"""
    template_path = os.path.join(TEMPLATES_DIR, "blog-list.html")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Category list HTML for sidebar
    total_count = len(posts)
    cat_items = [
        f'<a href="#" class="category-item active" data-category="all"><span>분류 전체보기</span><span class="category-count">({total_count})</span></a>'
    ]
    for cat, p_list in sorted(grouped_posts.items()):
        cat_items.append(
            f'<a href="#" class="category-item" data-category="{cat}"><span>{cat}</span><span class="category-count">({len(p_list)})</span></a>'
        )
    category_list_html = "\n".join(cat_items)

    # Post cards HTML for main column
    cards_html = []
    for p in posts:
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in p["tags"]])
        card = f'''<article class="post-card-item" data-category="{p["category"]}">
  <a href="posts/{p["slug"]}.html">
    <span class="post-card-kicker">{p["category"]}</span>
    <h2 class="post-card-title">{p["title"]}</h2>
    <p class="post-card-desc">{p["description"]}</p>
  </a>
  <div class="post-card-meta">
    <span class="post-card-date">{p["date"]}</span>
    <div class="tags">{tags_html}</div>
  </div>
</article>'''
        cards_html.append(card)

    rendered = template
    rendered = rendered.replace("{{CATEGORY_LIST}}", category_list_html)
    rendered = rendered.replace("{{POST_CARDS}}", "\n".join(cards_html))

    out_path = os.path.join(BLOG_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"  [Index] -> blog/index.html ({total_count} posts across {len(grouped_posts)} categories)")

def main():
    print("[BUILD] Starting static blog build...")
    posts = load_posts()
    if not posts:
        print("[WARNING] No posts found in content/posts/.")
        return

    grouped_posts = group_posts_by_category(posts)
    build_post_pages(posts, grouped_posts)
    build_blog_index(posts, grouped_posts)
    print("[SUCCESS] Static blog build completed successfully!")

if __name__ == "__main__":
    main()
