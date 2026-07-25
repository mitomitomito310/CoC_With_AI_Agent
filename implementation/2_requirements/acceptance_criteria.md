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
