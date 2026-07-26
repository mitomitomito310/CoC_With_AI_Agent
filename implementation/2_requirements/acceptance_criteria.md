# Acceptance Criteria

## Document Status

- Status: Approved (2026-07-25)
- Rule: 各項目はチャット記録とリポジトリ差分から合否を判定できること

## Scenario and Rules

- **AC-SCN-01 (FR-SCN-01..04):** テキスト/Markdownの短編fixtureを配置すると、原本を変更せず、開始前検証が対象版、参照元、開始地点、人物、秘匿区分、不足事項を報告する。
- **AC-SCN-02 (FR-SCN-05, QR-03, QR-09):** 結末、黒幕、未発見手掛かり、NPC秘密を含むfixtureを取り込んでも、開始前チャット、公開ファイル、公開通知へ内容または推測可能な言い換えが出ない。
- **AC-RUL-01 (FR-RUL-01):** 新規ユーザー探索者をフル手順で作成でき、途中の選択、計算結果、最終sheetを再確認できる。
- **AC-RUL-02 (FR-RUL-02..03):** 判定ログから技能・能力、難易度、修正、ダイス、結果、根拠または暫定裁定を追跡できる。
- **AC-RUL-03 (FR-RUL-04):** 補助skill/scriptを無効にしたレビューでも、Keeperの必須運営規則を`OUTPUT_AGENTS.md`だけから特定できる。

## Input Modes

- **AC-INP-01 (FR-INP-01..03):** 同じ文面を3モードで与えた試験で、Speechだけが発言として伝播し、Actionだけが実行・判定され、Player to Keeperは世界状態を変えない。
- **AC-INP-02 (FR-INP-02, QR-07):** 明確で低リスクな入力10件は不要な確認なしに処理され、曖昧・秘匿性あり・不可逆の各fixtureは状態変更前に確認される。

## Information and NPCs

- **AC-INF-01 (FR-INF-01..04, QR-03):** 未開示の真相、未発見手掛かり、NPC秘密を含むfixtureでも、公開応答、公開状態、更新通知に該当文字列または意味上の漏洩がない。
- **AC-INF-02 (FR-INF-03..04):** NPCへKeeperだけが知る正解を与えずに意思決定させ、取得経路のない情報を発言・行動理由に使用しない。
- **AC-NPC-01 (FR-NPC-01..04, QR-06):** NPCが単独行動、虚偽、離脱、裏切りの少なくとも1つを人物像に従って選べ、ユーザー利益を理由に差し替えられず、事後に当時の知識と理由を追跡できる。

## Persistence and Long-form Readiness

- **AC-STA-01 (FR-STA-01..03, QR-01..02):** 複数種類の変更を含むシーン終了で1つのcheckpointが作られ、各状態ファイルと更新通知が同じ差分を表す。
- **AC-STA-02 (QR-02):** checkpoint確定前に更新処理を中断した試験で、直前の確定状態から再開し、部分更新を現在状態として採用しない。
- **AC-STA-03 (FR-STA-04):** プロセスまたはチャットを終了後、`session/current.yaml`と`resume.md`を起点に、公開・Keeper・NPC知識の境界を変えず再開できる。
- **AC-STA-04 (FR-STA-05, QR-04):** 長編相当の多数シーンfixtureで、全原ログを通常コンテキストへ読み込まず、現在状態、要約、必要なシーンだけで次の場面を開始できる。
- **AC-STA-05 (QR-05):** セッション完走後も`source/`配下のchecksumまたはGit差分が開始前と一致する。
- **AC-STA-06 (FR-STA-06, QR-08):** Keeperがユーザー確認を挟まず複数シーンを自然に接続し、各境界で整合したcheckpointを作れる。明示的中止では中断checkpointを作り、曖昧な台詞では終了しない。

## Phase-2 Approval Gate

- `plan.md`のCurrent Questionsが回答済みである。
- 全FR/QRに設計上の実現箇所と受け入れ条件が対応している。
- 初回対象外は実装漏れではなくDeferred scopeとして明記されている。
- `risk_notes.md`のCritical/Highリスクに予防策と検証先がある。
- Execute担当がゲーム方針を新たに決めず、テンプレートと指示候補の実装へ着手できる。

## Verified Rule Fixtures (Quick-Start PDF)

All fixtures must persist a resolution record shaped by `design.md`, including the cited ledger IDs/pages.

| AC / links | Fixture | Expected |
| --- | --- | --- |
| **AC-RUL-04** (FR-RUL-02; RUL-RES-02; p.14) | Skill 60, rolls 60 / 30 / 12 at Regular / Hard / Extreme difficulty | Each equals its threshold and succeeds at the named difficulty; 31 fails Hard and 13 fails Extreme. |
| **AC-RUL-05** (FR-RUL-02; RUL-MOD-01; pp.14–15) | Ones 4, tens 20 and 40 | One bonus selects 24; one penalty selects 44. A bonus plus penalty cancels and consumes only the ordinary tens result. Raw dice and selection remain logged. |
| **AC-RUL-06** (FR-RUL-03; RUL-PSH-01..02; pp.14,16) | Failed STR door attempt followed by a materially changed leverage method; failed firearm attack offered the same option | Keeper may permit exactly one door reroll after recording the escalated consequence. Firearm/combat push is rejected. An unchanged “try again” is not automatically eligible and records Keeper decision. |
| **AC-RUL-07** (FR-RUL-02; RUL-OPP-01; p.14) | A: Hard with skill 50; B: Regular with 80. Then both Hard with skills 50/80. Then equal skills and D100 42/37 | A wins first by level; B wins second by higher skill; lower 37 wins final tie-break. |
| **AC-RUL-08** (FR-RUL-05; RUL-CMB-01..05; pp.16–19) | DEX 70/50/45; melee attack Hard vs dodge Hard and fight-back Hard; second melee attacker; readied firearm at DEX50 | Order 70, then readied firearm at effective 100 as applicable, then remaining DEX. Dodge wins equal level; attacker wins equal fight-back; later melee attacker gains one bonus die; no combat roll exposes push. |
| **AC-RUL-09** (FR-RUL-05..06; RUL-DMG-02, RUL-INJ-01; p.19) | max HP 12/current 12: single damage 6; separate case damage 13; major-wounded character reaches 0; non-major-wounded character reaches 0 | Damage 6 causes major wound (`>= half`) and CON check; 13 causes immediate death (`> max`); major+0 enters dying CON sequence; non-major+0 is unconscious, not dying. HP never negative. |
| **AC-RUL-10** (FR-RUL-06; RUL-HEAL-01..02; pp.11,19) | Major wound with weekly Regular/Extreme CON; First Aid within one hour; Medicine same day and after the injury day | Restore 1D3/2D3 respectively and remove major wound only by stated conditions. First Aid restores 1; Medicine restores 1D3, takes >=1 hour/tools, and after the day requires Hard. Dying case stabilizes with First Aid before Medicine. |
| **AC-RUL-11** (FR-RUL-07; RUL-SAN-01..02; p.16) | SAN 60 with loss `0/1D6`: rolls 60 and 61; failed roll loses 5, then INT 70 rolls 70 and 71 in separate cases | 60 takes 0; 61 rolls 1D6. Loss 5 triggers INT: 70 starts temporary insanity 1D10 hours; 71 does not. Loss/state order is logged. |
| **AC-RUL-12** (FR-RUL-07; RUL-INS-01..02, RUL-SCOPE-01; pp.16–17) | Temporary insanity with selected bout, phobia, Reality Check success/failure | Bout lasts 1D10 rounds; applicable phobia/mania gives one penalty die to all actions; successful check pierces delusion. Failed check is flagged for sourced Keeper handling rather than invented complete-SAN effects. |
| **AC-RUL-13** (FR-RUL-08; RUL-SCN-01..03; pp.21–43) | Import the included scenario index and blank sheets | Scenario mechanics remain `scenario_id` scoped/spoiler-protected; sheet fields do not create rules absent from pp.7–20. |
