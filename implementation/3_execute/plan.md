# Plan

## Status

- Phase: 3. Execute
- Status: In progress
- Approval: Not approved
- Current question: ルール参照の運用、skill分割、ダイス処理、初回fixtureを確定する
- Recommended option: 1A / 2A / 3A / 4A
- User answer: Phase 2の回答を反映し、クトゥルフ神話TRPGのルールと進行を公式Web情報から詳しく調査したうえで、必要なskillsを整理して実装計画を作る。作業は細切れのtask-stubにせず、このセッション内で資料へ反映する
- Next action: Phase 2の`rule_ledger.md`を入力契約としてschema/fixtureを実装する。Quick-Start対象外はコアルール確認まで停止し、下記4問の回答なしに運用選択を確定しない

## Phase 2 Handoff

- ユーザーは結末を知らずにシナリオ原本を提供する。構造化した真相、結末、手掛かり、NPC秘密はKeeper専用とし、開始前の応答もネタバレさせない。
- 秘匿保証は通常チャット、公開ファイル、公開通知まで。同一リポジトリのKeeper/NPC専用ファイルをユーザーが直接閲覧する場合は保証外とする。
- シーン境界はKeeperが物語上の変化から判断し、確認操作で没入を切らずに次の場面へ進む。ユーザーの明確な中止指示だけが安全な中断を起動する。
- 原ログは不変で保持し、checkpoint/currentを現在状態の正、章・シーン要約を再生成可能な派生データとする。
- NPCはユーザー利益やパーティー維持ではなく、自身の人物像、状態、目的、恐怖、倫理観、関係、個別知識、誤解から行動する。

## Official Rule Research

### Research policy

1. 対象版は日本語版の現行版に対応するCall of Cthulhu 7th Editionとし、版や日本語用語を混同しない。
2. 一次資料を、Chaosium公式ルールブック、公式Quick-Start Rules、公式Starter Set、KADOKAWAの日本語版製品・公式サポートの順で確認する。
3. 公式Webだけで手順の細部を確定できない項目は、一般知識で補わず「ルールブック参照が必要」と記録する。ユーザー提供資料を使う場合も本文を派生ファイルへ大量転載しない。
4. 各項目に資料名、版、言語、公式URL、参照日、確認箇所、利用範囲、確定/暫定を付ける。英語版と日本語版で用語差があれば対応表を持つ。
5. ルールに書かれた決定的処理、Keeper裁量、シナリオ固有処理を分離する。skillはルールブックの代替物にしない。

### Source register

| Priority | Source | Purpose | Current result |
| --- | --- | --- | --- |
| 1 | Chaosium Call of Cthulhu 7th Edition Keeper Rulebook official product/support | 完全ルールの対象版、章構成、正式な参照先 | 公式URLへの接続が実行環境のHTTP 403で遮断。再調査必須 |
| 2 | Chaosium Call of Cthulhu Quick-Start Rules official page/PDF | 基本判定、探索者、正気度、戦闘、進行の公開範囲 | Web検索APIがHTTP 401、直接接続がHTTP 403。再調査必須 |
| 3 | Chaosium Call of Cthulhu Starter Set official page | 初心者向けの段階的進行と導入範囲 | 公式URLへの接続がHTTP 403。再調査必須 |
| 4 | KADOKAWA クトゥルフ神話TRPG公式製品・サポート | 日本語版の現行製品、用語、正誤・補足 | 公式URLへの接続がHTTP 403。再調査必須 |

ローカル提供PDF `NewCoC-QS_200228.pdf` 全43ページを `SRC-QS-JA-20200228` として確認し、`implementation/2_requirements/rule_ledger.md`へ採録した。これはQuick-Start範囲の確認を満たすが、同台帳で対象外/要コアルール確認とした項目の完全ルール調査を満たさない。

### Rule and play-flow coverage

| Domain | Must identify before implementation | Planned owner |
| --- | --- | --- |
| Session setup | 対象年代、導入、参加者、探索者準備、シナリオ開始条件 | `OUTPUT_AGENTS.md` + scenario preparation skill |
| Investigator creation | 能力値、派生値、職業・信用、技能、経歴、装備、最終確認の正式手順 | character creation skill + calculator |
| Core resolution | percentile roll、難易度、成功段階、ボーナス/ペナルティ、対抗、プッシュ、幸運、成長の条件と例外 | core rules skill + deterministic dice script |
| Investigation | 情報提示、手掛かり、知覚可能性、失敗時の進行、秘匿情報の扱い | `OUTPUT_AGENTS.md`; scenario-specific index |
| Combat and harm | 行動順、攻撃、防御、反撃、ダメージ、装甲、負傷、意識、死亡、回復 | combat skill + state calculator |
| Sanity | SAN判定、喪失、一時的/不定/長期的影響、狂気の発作、回復 | sanity skill + state calculator |
| Chase | 参加条件、移動、行動、障害、終了条件 | chase skill; MVP採否は質問で確定 |
| Downtime | 技能成長、治療、幕間、継続探索者 | campaign skillまたはDeferred |
| Keeper flow | 場面提示、発話/行動/相談の識別、判定要求、結果描写、NPC判断、シーン遷移、中断・再開 | `OUTPUT_AGENTS.md` + checkpoint skill |

### 台帳から実装成果物へ移す責務

| 移送先 | `rule_ledger.md`から移す責務 | 所有してはならない責務 |
| --- | --- | --- |
| `coc-investigator-creation` skill | `RUL-CHR-*`, `RUL-DER-*`, `RUL-SKL-*`の質問順、未完項目、出典表示 | 未確認の完全作成表、端数を含む純計算 |
| `coc-core-resolution` skill | 判定種別選択、難易度/修正理由、プッシュ可否判定、Keeper説明 | 乱数生成、閾値計算、シナリオ秘密 |
| 戦闘／正気度skills | `RUL-CMB-*`〜`RUL-INS-*`の処理オーケストレーションと停止境界 | 完全銃器/回復/狂気表の推測 |
| 決定的scripts | 切り捨て閾値、百分率候補選択、成功度、HP／SAN差分、schema検証 | Keeper裁量、物語結果、対象外ルールの既定動作 |
| fixture | `AC-RUL-04..15`の入力/期待値、ルール／ページ／リスクの追跡 | PDF本文・handoutの転載 |
| `OUTPUT_AGENTS.md` | 参照元固定、判定前宣言、プッシュ条件、原子的結果適用、対象外時停止、秘匿 | 長大なルール再録、skillだけに存在する恒久規則 |

移送時は台帳IDを安定IDとして保持する。script出力は`design.md`のresolution schemaを満たし、各fixtureからFR、RUL、QS PDFページ、AC、リスクを辿れることをvalidatorで検査する。

## Skill Architecture

skillsは手順と文脈のまとまり、scriptsは同じ入力に同じ結果を返す計算・検証、`OUTPUT_AGENTS.md`はskillなしでも守る恒久的な運営規則に限定する。

### MVP skills

1. **`coc-scenario-preparation`**
   - 入力: ユーザー提供Markdown/テキスト、対象版、任意の開始条件。
   - 出力: 原本保存、manifest、Keeper専用truth/clue index、ネタバレなしの開始可否。
   - 禁止: 真相や構造化結果をユーザー確認用に表示すること、原本を書き換えること。
2. **`coc-investigator-creation`**
   - 入力: 対象版、作成方式、ユーザー選択、公式参照元。
   - 出力: 完全な探索者sheet、計算根拠、未完項目。
   - 境界: 正式手順が未確認なら推測せず停止し、必要な参照箇所だけを求める。
3. **`coc-core-resolution`**
   - 入力: 技能/能力値、難易度、修正、ダイス、適用可能なルール選択。
   - 出力: ロール、成功段階、状態差分、根拠ログ。ダイス生成と純粋計算はscriptへ委譲する。
4. **`coc-scene-keeper`**
   - 入力: 公開状態、Keeper専用索引、現在シーン、参加者、各NPCへ分離した知識。
   - 出力: 没入的な応答、必要な判定要求、観測可能な知識伝播、Keeper主導のscene checkpoint。
   - 境界: NPC判断用コンテキストへKeeper Onlyや他NPC knowledgeを混ぜない。
5. **`coc-session-state`**
   - 入力: 追記ログとシーン中の変更集合。
   - 出力: 原子的checkpoint、current、resume、派生要約、公開用の短い更新通知。
   - 復旧: 部分更新を正とせず、最後の確定checkpointから再開する。

### Conditional skills

- **`coc-combat`**: 戦闘の正式処理を公式資料で確認後に追加する。初回fixtureに戦闘があればMVP必須。
- **`coc-sanity`**: CoC固有の中核であり原則MVP必須。詳細表や例外は公式資料を参照し、無断複製しない。
- **`coc-chase`**: 初回fixtureで必要なら実装し、不要なら設計契約だけ残して後続へ送る。
- **`coc-downtime`**: 長編対応のschemaは先に用意し、成長・治療・幕間の完全支援は短編検証後でもよい。

### Scripts and validators

- `roll`: 乱数源、ダイス結果、入力値、修正、結果を追跡可能にする。物語上の裁定は行わない。
- `character-validator`: 必須欄、値域、派生値、未完選択を対象版schemaで検査する。
- `scenario-validator`: manifest、原本、開始地点、秘匿区分、初期人物、参照元、原本checksumを検査する。
- `checkpoint-validator`: state version、参照ID、変更集合、public/secret境界、部分更新を検査する。
- `spoiler-scan`: 公開候補をKeeper索引の秘密語だけでなく意味上の漏洩も含めてレビュー対象にする。自動検査だけで安全を保証しない。

## Implementation Sequence

1. **Rule register:** 公式参照元を再調査し、上表の各処理を確定/暫定/要ルールブックに分類する。
2. **Schemaとfixture:** Phase 2のrepository modelを具体的なschema、雛形、ネタバレfixtureへ変換する。
3. **Deterministic core:** validator、ダイス記録、checkpoint整合性など物語判断を含まない処理を実装する。
4. **Skill drafts:** MVP skillsの`SKILL.md`を作り、入力、参照境界、出力、失敗、ログを揃える。
5. **Game profile:** 3モード、Keeper進行、NPC自律、ネタバレ防止、scene transactionを`OUTPUT_AGENTS.md`へ反映する。
6. **Profile switching:** `agent_profile_switching.md`に開発用/ゲーム用プロファイルの切替、復元、使用skillの記録方法を書く。
7. **Small chat trial:** ネタバレなし取込、探索者作成、調査、NPC秘密、シーン遷移、中断・再開を短いfixtureで試し、不足は該当フェーズへ戻す。

## Deliverables

- `implementation_notes.md`: 実装順、schema、作成物、公式参照台帳、暫定裁定、Deferred scope。
- `agent_profile_switching.md`: 安全な切替、復元、利用中プロファイル/skillの監査手順。
- `OUTPUT_AGENTS.md`: skillなしでも保持すべきゲーム固有のKeeper運営規則。
- シナリオ雛形と短編fixture。
- 必要最小限のskills、scripts、validators、および各検証結果。

## Phase Exit Checklist

- [ ] 公式参照台帳でMVP対象ルールの版、根拠、確定状態を追跡できる
- [ ] 原本を変更せず、ユーザーへネタバレせずにscenario workspaceを準備できる
- [ ] 探索者作成とMVP対象判定を根拠ログ付きで処理できる
- [ ] NPC別知識、公開情報、Keeper情報を混ぜずに進行できる
- [ ] Keeper主導のscene checkpointと明示中止からの再開ができる
- [ ] 原ログ、checkpoint/current、派生要約の優先順位を検証できる
- [ ] 恒久ルールが`OUTPUT_AGENTS.md`だけから特定できる
- [ ] 開発用プロファイルへ安全に戻せる
- [ ] 実装結果とDeferred scopeを`implementation_notes.md`へ記録する
- [ ] ユーザーがExecute成果物を承認する

## Current Questions

1. **公式ルール本文を確認する方法はどれにしますか？**
   - **A（推奨）:** 公式公開資料を再調査し、不足箇所だけユーザー所持ルールブックの参照箇所・要約で補う。本文はリポジトリへ複製しない。
   - B: 公式公開資料だけで確認できる範囲をMVPとし、それ以外はDeferredにする。
   - C: ユーザー提供のルール要約だけを今回の正とする。
2. **skillの分割単位はどれにしますか？**
   - **A（推奨）:** 準備、探索者作成、基本判定、Keeper/scene、session stateをMVPの責務単位とし、戦闘・正気度・チェイスを必要に応じて独立させる。
   - B: 全ルールとKeeper進行を1つのskillへまとめる。
   - C: 各判定・各状態ごとに細かなskillへ分ける。
3. **ダイスはどの運用を正としますか？**
   - **A（推奨）:** リポジトリのscriptが生成・記録し、ユーザーの物理ダイス結果も明示入力なら受け付ける。
   - B: 常にAI側scriptで振る。
   - C: 常にユーザーが結果を入力する。
4. **最初の実装fixtureはどれにしますか？**
   - **A（推奨）:** 著作権上安全な自作の極小fixtureで、調査、1回の判定、NPC秘密、正気度、scene遷移、中断再開を検証する。
   - B: ユーザー所持の既存シナリオを最初から使う。
   - C: 公式Quick-Start収録シナリオを使う（利用条件と本文の扱いを先に確認する）。

推奨案を一括採用する場合は、`1A、2A、3A、4A`と回答できる。

## Decisions

| Date | Question | Options | Recommended | Answer | Result |
| --- | --- | --- | --- | --- | --- |
| 2026-07-25 | Phase 3で最初に行うこと | 直接実装 / ルール調査後にskill整理 | ルール調査後にskill整理 | 公式Webを詳細に調べて必要skillsを整理し、実装計画を作る | 調査方針、責務表、skill候補、実装順をplanへ作成 |
| 2026-07-25 | 作業のまとめ方 | task-stubへ分割 / このセッションで資料へ反映 | このセッションで資料へ反映 | タスクは分けずにこのセッション内で修正 | Phase 2回答反映とPhase 3計画作成を一括実施 |
| 2026-07-25 | 公式Web調査の接続結果 | 調査完了 / 未完 | 未完なら明示して根拠を捏造しない | 検索APIはHTTP 401、Chaosium/KADOKAWAへの直接接続はHTTP 403 | 公式確認済みとはせず、再調査を最初の実装ゲートに設定 |
