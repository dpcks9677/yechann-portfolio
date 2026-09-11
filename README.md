# 김예찬 포트폴리오 & 기술 블로그

정적 에디토리얼 스타일의 포트폴리오 및 마크다운 기반 자체 기술 블로그(Devlog)입니다.

## 로컬 확인 및 전용 글 작성 에디터 (CMS)

```bash
python server.py
```
* **메인 포트폴리오**: `http://localhost:8000`
* **기술 블로그**: `http://localhost:8000/blog/`
* **📝 글 작성/수정 에디터**: `http://localhost:8000/editor`
  * 브라우저에서 편리하게 실시간 미리보기를 보면서 글을 작성/수정하고 저장할 수 있습니다.
  * **[저장 및 사이트 반영]**을 누르면 마크다운 파일 저장과 블로그 빌드가 원클릭으로 자동 완료됩니다.
  * **보안 보장**: 에디터와 `server.py`는 `.gitignore`에 등록되어 GitHub에는 절대 올라가지 않으며, 내 로컬 컴퓨터에서만 안전하게 실행됩니다.

## 수동 마크다운 작성 및 빌드 (CLI)

에디터 대신 텍스트 편집기로 직접 작성할 수도 있습니다:
1. `content/posts/` 폴더에 `[파일명].md` 작성
2. `python build.py` 실행

## GitHub Pages 배포

1. 빌드 완료 후 저장소에 커밋 및 푸시합니다:
   ```bash
   git add .
   git commit -m "Add new blog post"
   git push origin main
   ```
2. `https://dpcks9677.github.io/yechann-portfolio/` 로 즉시 공개됩니다.

## 이미지

`images/`에 5장이 들어가 있습니다. 이미지는 항상 컬러로 보이고, 마우스를 올리면 1.06배로 부드럽게 확대됩니다(`prefers-reduced-motion`에서는 정지). 프레임 높이는 이전 대비 1.2배입니다.

| 위치 | 파일 | 프레임 높이 |
| --- | --- | --- |
| About | `images/profile.webp` | 317px (286 폭) |
| Project 01 Phase 1 | `images/augmented-dice.webp` | 300px |
| Project 01 Phase 2 | `images/tessera.webp` | 300px |
| Project 02 | `images/daily-arrow.webp` | 288px |
| Project 03 | `images/offense-game.webp` | 288px |
| Media × 4 | — 스켈레톤 | 180px |

아직 받지 못한 미디어 4컷은 `.skel` 회색 스켈레톤입니다. 교체할 때는

```html
<div class="skel"><span class="skel-label">브이로그 썸네일</span></div>
```

을

```html
<div class="shot"><img src="images/vlog.webp" alt="브이로그 썸네일" loading="lazy" decoding="async"></div>
```

로 바꾸면 됩니다. 권장 비율 16:9 — 파일만 넣고 경로를 맞추면 CSS 수정은 필요 없습니다.

## 남은 항목

- 미디어 4컷 이미지 (브이로그 · 카드뉴스 · 릴스 · 일러스트)
- Project 03 기획서 · GitHub 링크 URL 미정
- `profile.webp`가 4:3 가로 사진이라 세로 프레임에서 좌우가 잘립니다 — 세로 원본이 있으면 교체 권장
