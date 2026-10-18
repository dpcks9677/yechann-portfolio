# -*- coding: utf-8 -*-
"""프로젝트 상세 페이지 설정. 새 프로젝트는 PROJECTS에 항목을 추가하고
content/projects/<slug>/judgments.md 를 작성한 뒤 `python build_projects.py` 를 실행한다."""

PRETENDARD = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css"

PROJECTS = [
    {
        "slug": "shotgun-and-run",
        "title": "Shotgun and Run",
        "kicker": "TEAM PROJECT · 2026.09.17 — 10.14",
        "desc": "2D 탑다운 익스트랙션 슈터 Shotgun and Run의 기획 판단 기록. PM·전체 기획·레벨 디자인을 맡았고, 판단마다 상황, 결정, 이유, 한계를 적었습니다.",
        "og": "PM · 전체 기획 · 레벨 디자인. 판단 14건과 그 한계를 기록했습니다.",
        "hero": "2D 탑다운 익스트랙션 슈터. 던전에 들어가 파밍하고, 주기적으로 몰려오는 습격을 쓸어버리며, 제한 시간 안에 탈출하는 게임입니다. 4인 팀에서 PM과 전체 기획을 맡았습니다.",
        "roles": ["PM", "전체 기획 (GDD)", "레벨 디자인", "컷씬 · 퀘스트", "BGM 기획 · 사운드 디렉팅", "서브 프로그래밍"],
        "buttons": [("primary", "https://www.youtube.com/watch?v=wpbb_FIQQbo", "트레일러 ▶"), ("", "#key", "핵심 판단 보기"), ("", "https://shotgunandrunreport.super.site/", "팀 보고서 ↗"), ("", "https://github.com/dpcks9677/shotgun-and-run", "GitHub (공개용)")],
        "play": """<section class="section play" id="trailer">
  <div class="kicker">TRAILER</div>
  <div class="play-trailer">
    <div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/wpbb_FIQQbo" title="샷건 앤 런 트레일러 | Shotgun and run Trailer" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p class="meta">플레이 트레일러 · 약 1분 · <a class="link" href="https://www.youtube.com/watch?v=wpbb_FIQQbo" target="_blank" rel="noopener">YouTube에서 보기 ↗</a></p>
  </div>
  <div class="kicker" style="margin-top:36px">GAME FEEL</div>
  <div class="play-grid">
    <figure>
      <video src="../../images/shotgun-and-run/feel-hit.mp4" poster="../../images/shotgun-and-run/feel-hit.webp" autoplay muted loop playsinline preload="metadata" aria-label="사격과 피격 연출 영상"></video>
      <figcaption>사격 · 피격 연출 · 총구 섬광, 탄 궤적, 피 이펙트</figcaption>
    </figure>
    <figure>
      <video src="../../images/shotgun-and-run/feel-vignette.mp4" poster="../../images/shotgun-and-run/feel-vignette.webp" autoplay muted loop playsinline preload="metadata" aria-label="저체력 비네팅과 폭탄 경고 연출 영상"></video>
      <figcaption>저체력 비네팅 · 폭탄 경고 연출</figcaption>
    </figure>
  </div>
</section>""",
        "hero_bg": "../../images/shotgun-and-run/hero-bg.webp",
        "cells": [
            ("프로젝트", "Unity 6 (6000.3.22f1) · 팀 &ldquo;4번타자&rdquo; · 약 4주. 핵심 루프는 출격 → 파밍·전투 → 탈출입니다. 마감 안에 루프를 완성하기 위해 보스는 10/10에 범위에서 제외했습니다 (판단 01)."),
            ("개발 환경", "Unity 6000.3.22f1 · C# · URP · New Input System · 2D Tilemap · uGUI &amp; TextMesh Pro<br>협업: GitHub, Notion, Discord, Slack · 배포: Windows Standalone (GitHub Releases)"),
        ],
        "after_cells": """<section class="section" id="team">
  <div class="kicker">TEAM · 4번타자</div>
  <h2 class="title-sm">팀원별 담당 역할과 주요 작업</h2>
  <div class="team-wrap"><table class="team-table">
    <thead><tr><th>이름</th><th>담당 역할</th><th>주요 작업</th></tr></thead>
    <tbody>
      <tr class="me"><td><b>김예찬</b></td><td>👑 PM<br>🎨 그래픽/사운드 디자인<br>💻 서브 프로그래머</td><td><ul><li>전체 게임 기획(GDD)</li><li>던전 대형 맵 레벨 디자인</li><li>컷씬 &amp; 퀘스트 시스템 구축</li><li>BGM 기획/사운드 디렉팅</li><li>전역/동적 Light2D 배치</li><li>오디오 믹서 구축</li></ul></td></tr>
      <tr><td><b>김민석</b></td><td>💻 플레이어 프로그래머</td><td><ul><li>플레이어 조작·이동·대시 기능</li><li>샷건 조준 및 사격과 탄환 오브젝트 풀링</li><li>조준·집탄률 인디케이터 기능</li><li>파츠 데이터 설계 및 업그레이드 기능</li><li>소모품 데이터 설계 및 사용 기능</li><li>전투 게임필 (카메라 쉐이킹, 히트 스탑, 사운드, VFX) 구현</li><li>QA 종합 및 피드백</li></ul></td></tr>
      <tr><td><b>정성훈</b></td><td>💻 전투 프로그래머</td><td><ul><li>Enemy 6종 구현</li><li>유한 상태 머신(FSM) 기반 Enemy 행동 관리 구현</li><li>A* 및 LOS(Line Of Sight: 직선 상 장애물 판별): 기반 길찾기 내비게이션</li><li>스포너(Standard, Raid, Destruction) 및 난이도 청크 시스템 구현</li></ul></td></tr>
      <tr><td><b>김호준</b></td><td>💻 프로그래머<br>🎨 UI 디자이너</td><td><ul><li>인게임 HUD(체력, 대시, 탄창, 타이머, 퀵슬롯) 구현</li><li>쉘터 시스템(창고, 무기 강화, 소모품 제작, 레벨업)</li><li>런 결과창 구현</li><li>실시간 미니맵 구현</li></ul></td></tr>
    </tbody>
  </table></div>
</section>""",
        "featured": [2, 3, 9],
        "key_lead": "시간 제한, 추격 구조, 맵 구조. 눌러서 펼쳐 보세요.",
        "all_lead": "",
        "extra": {
            9: [
                ("../../images/shotgun-and-run/map-draft-v21.webp", "도형 초안 v21 · 존(초록)과 홀(갈색), 커넥터(회색) 배치 · 10/14", "스테이지 1 도형 초안 v21"),
                ("../../images/shotgun-and-run/map-ingame.webp", "인게임 지도 · 플레이어가 보는 모습", "스테이지 1 인게임 지도"),
            ],
        },
    },
    {
        "slug": "augmented-dice",
        "title": "증강 요트 다이스",
        "kicker": "SOLO PROJECT · 2026.07 — 진행 중",
        "desc": "요트 다이스에 증강 55종을 얹은 실시간 멀티플레이 보드게임. 카드 기획부터 서버 권위 구조까지, 판단마다 상황, 결정, 이유, 한계를 적었습니다.",
        "og": "카드 기획 · 시스템 설계 · 개발. 판단 7건과 그 한계를 기록했습니다.",
        "hero": "클래식 요트 다이스의 족보 규칙 위에 증강 55종을 얹은 2인 대전 게임입니다. 웹 실시간 멀티플레이로 룰을 다듬었고, 지금은 같은 룰을 Unity 6 3D 테이블탑(Tessera)으로 옮기고 있습니다. 기획부터 구현까지 혼자 맡았습니다.",
        "roles": ["기획", "시스템 설계", "개발"],
        "buttons": [("primary", "#key", "핵심 판단 보기"), ("", "https://augmented-dice.web.app", "플레이 ↗"), ("", "https://github.com/dpcks9677/augmented-dice", "GitHub ↗"), ("", "https://github.com/dpcks9677/Tessera", "Tessera ↗")],
        "play": """<section class="section play">
  <div class="kicker">PHASE 1 · PHASE 2</div>
  <div class="play-grid">
    <figure>
      <img src="../../images/augmented-dice.webp" alt="Augmented Dice 플레이 화면" loading="lazy" decoding="async">
      <figcaption>Phase 1 · 웹 · 배포 중 (Vite · Vanilla JS · PartyKit · Cloudflare Workers · Firebase)</figcaption>
    </figure>
    <figure>
      <img src="../../images/tessera.webp" alt="Tessera 인게임 스크린샷" loading="lazy" decoding="async">
      <figcaption>Phase 2 · Tessera · Unity 6 URP · 개발 중</figcaption>
    </figure>
  </div>
</section>""",
        "cells": [
            ("프로젝트", "2026.07.01 첫 커밋 이후 커밋 110개. 1·6·9턴마다 증강 3택 1을 고르는 2인 대전이고, 클래식 4인전도 지원합니다. 6자리 PIN으로 방을 만들어 바로 붙는 실시간 멀티플레이입니다."),
            ("범위", "<b>김예찬</b> 기획 · 시스템 설계 · 개발 (1인)<br>증강 카드 55종, 서버 권위 구조, 주사위 연출 동기화, Unity 이식 구조"),
        ],
        "featured": [1, 4, 5],
        "key_lead": "카드 기획, 서버 권위 구조, 주사위 결과 동기화. 눌러서 펼쳐 보세요.",
        "all_lead": "",
        "extra": {},
    },
    {
        "slug": "daily-arrow",
        "title": "Daily Arrow",
        "kicker": "SOLO PROJECT · 2026.06 — 운영 중",
        "desc": "매일 같은 50키 시퀀스로 겨루는 반응속도 랭킹 웹 미니게임. 데일리 구조와 운영 중 고친 문제들을 상황, 결정, 이유, 한계로 적었습니다.",
        "og": "데일리 구조 기획 · 개발 · 운영. 판단 4건과 그 한계를 기록했습니다.",
        "hero": "자정마다 바뀌는 50개의 방향키를 가장 빠르게 입력해 겨루는 반응속도 웹 미니게임입니다. 데일리 퍼즐 형식을 반응속도 게임에 가져왔고, 기획부터 배포와 운영까지 혼자 맡았습니다.",
        "roles": ["기획", "개발", "운영"],
        "buttons": [("primary", "#key", "핵심 판단 보기"), ("", "https://daily-arrow.web.app", "플레이 ↗"), ("", "https://github.com/dpcks9677/daily-arrow-game", "GitHub ↗")],
        "play": """<section class="section play">
  <div class="kicker">PLAY</div>
  <div class="play-grid">
    <figure>
      <img src="../../images/daily-arrow.webp" alt="Daily Arrow 플레이 화면" loading="lazy" decoding="async">
      <figcaption>Daily Arrow · 웹 · 배포 중</figcaption>
    </figure>
  </div>
</section>""",
        "cells": [
            ("프로젝트", "2026.06.05 첫 배포 이후 커밋 80개. 리더보드, 데일리 스트릭, 도전과제, 통계, 실시간 멀티플레이(v1.0.0)를 차례로 붙였고, 9월에는 디스코드 액티비티로 옮겨 음성 채널에서 함께 할 수 있게 했습니다."),
            ("스택", "React 19 · Vite · Firebase (Hosting, Firestore, Auth) · Cloudflare Workers · Discord Embedded App SDK"),
        ],
        "featured": [1, 2, 3],
        "key_lead": "데일리 구조, 기록 기준, 변조 방지. 눌러서 펼쳐 보세요.",
        "all_lead": "",
        "extra": {},
    },
    {
        "slug": "line-offense",
        "title": "Godot 횡스크롤 라인 오펜스",
        "kicker": "GRADUATION PROJECT · 2023.11 — 2024.11",
        "desc": "에르엘워즈를 레퍼런스로 만든 Godot 횡스크롤 라인 오펜스 졸업 프로젝트. 컴포넌트, FSM, 라인 격리, 세이브 구조의 설계 판단을 적었습니다.",
        "og": "1인 개발 졸업 프로젝트. 설계 판단 5건과 그 한계를 기록했습니다.",
        "hero": "여러 라인에서 유닛이 진격하고 맞붙는 횡스크롤 라인 오펜스입니다. 게임빌의 에르엘워즈를 레퍼런스로 삼았고, 유닛을 컴포넌트와 상태 노드로 조립하는 구조를 직접 설계했습니다. 1인 개발 졸업 프로젝트입니다.",
        "roles": ["기획", "개발", "구조 설계"],
        "buttons": [("primary", "#key", "핵심 판단 보기"), ("", "https://github.com/dpcks9677/Project_YEC", "GitHub ↗")],
        "play": """<section class="section play">
  <div class="kicker">PLAY</div>
  <div class="play-grid">
    <figure>
      <img src="../../images/offense-game.webp" alt="횡스크롤 라인 오펜스 게임 플레이 화면" loading="lazy" decoding="async">
      <figcaption>Godot 4 · 스테이지 플레이 화면</figcaption>
    </figure>
  </div>
</section>""",
        "cells": [
            ("프로젝트", "수원대학교 졸업 프로젝트 · 1인 개발. 커밋 163개(2023.11 — 2024.07 공개 레포 기준). 아군 11종, 적 8종 유닛."),
            ("스택", "Godot 4 · GDScript · Path2D · Autoload 싱글톤 · JSON 세이브"),
        ],
        "featured": [2, 3, 4],
        "key_lead": "컴포넌트 조립, 라인 격리, FSM 전환. 눌러서 펼쳐 보세요.",
        "all_lead": "",
        "extra": {},
    },
]
