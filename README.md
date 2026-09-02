# 김예찬 포트폴리오

정적 원페이지 사이트. 빌드 도구·의존성 없음 — `index.html`과 `styles.css` 두 파일이 전부입니다.

## 로컬 확인

```bash
cd site
python3 -m http.server 8000   # → http://localhost:8000
```

## GitHub Pages 배포

1. 이 폴더의 파일을 `dpcks9677/yechann-portfolio` 저장소 루트에 올립니다.
2. Settings → Pages → Source를 `main` 브랜치 `/ (root)`로 지정합니다.
3. `https://dpcks9677.github.io/yechann-portfolio/` 로 공개됩니다.

## 이미지

`images/`에 5장이 들어가 있습니다. 이미지는 항상 컬러로 보이고, 마우스를 올리면 1.06배로 부드럽게 확대됩니다(`prefers-reduced-motion`에서는 정지). 프레임 높이는 이전 대비 1.2배입니다.

| 위치 | 파일 | 프레임 높이 |
| --- | --- | --- |
| About | `images/profile.webp` | 317px (220 폭) |
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
