# Plan

## Status

- Phase: 3. Execute
- Status: In progress
- Approval: Not approved
- Current question: なし
- Recommended option: 1A / 2A / 3A / 4A
- User answer: `1A、2A（責務に合わせて最適に細分化）、3A、4A`。公式公開資料を優先して不足箇所だけ所持ルールブックの参照情報で補い、責務別skill、記録可能なscriptと物理ダイス入力、自作の極小fixtureを採用する
- Next action: 初回実装を拡張し、未実装のSAN/戦闘branch、scenario import、resume投影、AC-RUL-06/08/10..16のfixtureを追加して全受け入れ条件を検証する

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

接続できなかった事実をルール調査完了とは扱わない。公式資料を確認できるまでは、以下を実装対象の責務一覧として使い、数式、閾値、例外、正式用語を確定しない。

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
2. **Schemas and fixtures:** Phase 2のrepository modelを具体的なschema、雛形、ネタバレfixtureへ変換する。
3. **Deterministic core:** validator、ダイス記録、checkpoint整合性など物語判断を含まない処理を実装する。
4. **Skill drafts:** MVP skillsの`SKILL.md`を作り、入力、参照境界、出力、失敗、ログを揃える。
5. **Game profile:** 3モード、Keeper進行、NPC自律、ネタバレ防止、scene transactionを`OUTPUT_AGENTS.md`へ反映する。
6. **Profile switching:** `agent_profile_switching.md`に開発用/ゲーム用プロファイルの切替、復元、使用skillの記録方法を書く。
7. **Small chat trial:** ネタバレなし取込、探索者作成、調査、NPC秘密、シーン遷移、中断・再開を短いfixtureで試し、不足は該当フェーズへ戻す。

## Deliverables

- `implementation_notes.md`: skill境界とディレクトリ構成を草稿化済み。今後、実装順、schema、作成物、公式参照台帳、暫定裁定、Deferred scopeを実績に合わせて更新する。
- `agent_profile_switching.md`: 安全な切替、復元、利用中プロファイル/skillの監査手順。
- `OUTPUT_AGENTS.md`: skillなしでも保持すべきゲーム固有のKeeper運営規則。
- シナリオ雛形と短編fixture。
- 必要最小限のskills、scripts、validators、および各検証結果。

## Phase Exit Checklist

- [ ] 公式参照台帳でMVP対象ルールの版、根拠、確定状態を追跡できる
- [x] 原本を変更せず、ユーザーへネタバレせずにscenario workspaceを準備できる
- [ ] 探索者作成とMVP対象判定を根拠ログ付きで処理できる
- [ ] NPC別知識、公開情報、Keeper情報を混ぜずに進行できる
- [ ] Keeper主導のscene checkpointと明示中止からの再開ができる
- [x] 原ログ、checkpoint/current、派生要約の優先順位を検証できる
- [x] 恒久ルールが`OUTPUT_AGENTS.md`だけから特定できる
- [x] 開発用プロファイルへ安全に戻せる
- [x] 実装結果とDeferred scopeを`implementation_notes.md`へ記録する
- [ ] ユーザーがExecute成果物を承認する

## Confirmed Implementation Choices

1. **ルール参照（1A）:** 公式公開資料を再調査し、不足箇所だけユーザー所持ルールブックの参照箇所・要約で補う。本文はリポジトリへ複製しない。
2. **skill分割（2A・最適化）:** 準備、探索者作成、基本判定、Keeper/scene、session stateを独立したワークフロー責務とする。戦闘と正気度は、固有の状態遷移と停止条件があるため独立させる。チェイスとdowntimeは検証済み資料とfixtureが揃うまでDeferredとし、単純な判定ごとの過剰な細分化はしない。
3. **ダイス（3A）:** リポジトリのscriptが生成・記録し、ユーザーが明示した物理ダイス結果も同じresolution recordへ記録して受け付ける。
4. **初回fixture（4A）:** 著作権上安全な自作の極小fixtureで、調査、1回の判定、NPC秘密、正気度、scene遷移、中断再開を検証する。

## Decisions

| Date | Question | Options | Recommended | Answer | Result |
| --- | --- | --- | --- | --- | --- |
| 2026-07-25 | Phase 3で最初に行うこと | 直接実装 / ルール調査後にskill整理 | ルール調査後にskill整理 | 公式Webを詳細に調べて必要skillsを整理し、実装計画を作る | 調査方針、責務表、skill候補、実装順をplanへ作成 |
| 2026-07-25 | 作業のまとめ方 | task-stubへ分割 / このセッションで資料へ反映 | このセッションで資料へ反映 | タスクは分けずにこのセッション内で修正 | Phase 2回答反映とPhase 3計画作成を一括実施 |
| 2026-07-25 | 公式Web調査の接続結果 | 調査完了 / 未完 | 未完なら明示して根拠を捏造しない | 検索APIはHTTP 401、Chaosium/KADOKAWAへの直接接続はHTTP 403 | 公式確認済みとはせず、再調査を最初の実装ゲートに設定 |
| 2026-07-26 | 必要skillsとディレクトリ構成 | 単一skill / 責務分割 / 判定別の細分化 | 責務分割 | 設計を依頼。未回答4項目は推奨案を作業仮定にする | 7つのMVP/domain skill、共有rules/schema/tools、隔離scenario workspaceを`implementation_notes.md`へ草稿化 |
| 2026-07-26 | Phase 3へ進むか | Phase 2承認後に開始 / Phase 2を再修正 | Phase 2承認後に開始 | ステージ2を承認して次のステージに進む | Phase 3の進行意思を再確認。実装前にCurrent Questions 4項目の回答を待つ |
| 2026-07-26 | Phase 3の実装選択 | 1A〜C / 2A〜C / 3A〜C / 4A〜C | 1A / 2A / 3A / 4A | 1A、2A（最適に細分化）、3A、4A | 公式優先の参照、責務別7 skill、記録可能なscript/物理ダイス、自作極小fixtureを確定 |
| 2026-07-26 | Phase 3フル実装を開始するか | 初回increment開始 / 設計を継続 | 初回increment開始 | 時間をかけてフル実装を開始 | schema、lifecycle、tools、fixture、7 skills、OUTPUT_AGENTS、profile切替、15 testを初回実装 |

## Rule-ledger responsibility transfer (2026-07-26)

| Destination | Responsibility transferred from `rule_ledger.md` | Must not own |
| --- | --- | --- |
| Character-creation skill | Guided sequence and source prompts for RUL-CHR/DRV/SKL; surface outside-scope flags | Hidden arithmetic variants or core-only creation rules |
| Core-resolution skill | Frame intent/difficulty, push dialogue, opposed context, cite ledger pages | Random generation, mutable state, or inferred missing rules |
| Combat/Sanity skills | Orchestrate only confirmed RUL-CMB/DMG/INJ/HEAL/SAN/INS branches and stop on scope flags | Full combat/SAN system not in the PDF |
| Deterministic scripts | Floor thresholds/derived values, D100 candidates, bonus/penalty choice, comparisons, damage/state deltas; emit raw audit data | Keeper discretion or prose consequence invention |
| Scenario data | RUL-SCN page-scoped local rules, spoiler-bearing indexes and fixture inputs | Universal rule definitions or public output |
| `OUTPUT_AGENTS.md` | Source hierarchy, no-inference stop rule, Keeper discretion boundary, combat push prohibition, citation/state-application order | Copied rulebook prose/tables or script implementation detail |

Phase 3 must implement the `design.md` resolution record first, validate AC-RUL-04..13, and map every encoded branch to FR-RUL + ledger ID + PDF page + risk ID. `RUL-SCOPE-*` remains a hard stop until a core-rule source is supplied; this refinement does not change either phase's approval status.
