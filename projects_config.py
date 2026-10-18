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
        "buttons": [("primary", "#key", "핵심 판단 보기"), ("", "https://github.com/dpcks9677/shotgun-and-run", "GitHub (공개용)")],
        "play": """<section class="section play">
  <div class="kicker">PLAY</div>
  <div class="play-grid">
    <figure>
      <video src="../../images/shotgun-and-run/combat.mp4" poster="../../images/shotgun-and-run/combat.webp" autoplay muted loop playsinline preload="metadata" aria-label="교전 중 샷건 사격 영상"></video>
      <figcaption>교전 · 샷건 사격으로 적 처치</figcaption>
    </figure>
    <figure>
      <img src="../../images/shotgun-and-run/indicator.webp" alt="사격 인디케이터 조준 호 표시" loading="lazy" decoding="async">
      <figcaption>사격 인디케이터 · 조준 호 표시</figcaption>
    </figure>
  </div>
</section>""",
        "cells": [
            ("프로젝트", "Unity 6 (6000.3.22f1) · 팀 &ldquo;4번타자&rdquo; · 약 4주. 핵심 루프는 출격 → 파밍·전투 → 탈출입니다. 마감 안에 루프를 완성하기 위해 보스는 10/10에 범위에서 제외했습니다 (판단 01)."),
            ("팀", "<b>김예찬</b> 기획 · PM · 서브 프로그래밍<br>김민석 플레이어 프로그래머<br>정성훈 전투 · 적 AI 프로그래머<br>김호준 UI · 쉘터 프로그래머"),
        ],
        "featured": [2, 3, 9, 11],
        "key_lead": "시간 제한, 추격 구조, 맵 구조, 업무 분배. 각 항목은 상황 → 결정 → 이유 → 한계 순서입니다.",
        "all_lead": "보스 제외, 이동 속도와 맵, 퀘스트 구조, 카메라, QA, 아머, BGM, 컷씬 저장, 매니저 분리. 개발 쪽 판단은 13, 14번입니다.",
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
        "featured": [1, 4, 5, 6],
        "key_lead": "카드 기획, 서버 권위 구조, 주사위 결과 동기화, 후보 풀 보정. 각 항목은 상황 → 결정 → 이유 → 한계 순서입니다.",
        "all_lead": "Unity 이식 이유, 메타데이터 분리, 어셈블리 구조.",
        "extra": {},
    },
]
