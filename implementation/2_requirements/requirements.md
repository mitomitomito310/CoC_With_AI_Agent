# Requirements

## Document Status

- Status: Approved (2026-07-25)
- Phase baseline: Ideation approved on 2026-07-24
- Purpose: Executeフェーズが追加のゲーム方針推測をせず、テンプレート、補助機能、最終`OUTPUT_AGENTS.md`候補を実装できる要件基準を定める

## Product Goal

リポジトリを外部記憶として使うAI Keeperが、テキストまたはMarkdownの既存CoCシナリオを進行する。ユーザー探索者と自律NPC探索者による本格的なセッションで、ルールの正確さ、秘匿情報の分離、キャラクターに基づく予測不能な判断、途中再開可能な記録を両立する。

## Scope

### First implementation increment

- 提供された短編シナリオ1本を準備し、新規ユーザー探索者と1人以上のNPC探索者で最後まで進行できる。
- CoC現行最新版を主軸とし、対象版とユーザーが利用可能な参照元をセッションごとに明示する。
- データ構造はシーン数や中断回数に短編固有の上限を持たず、長編シナリオでも同じ更新・再開方式を使える。

### Deferred scope

- 自由生成シナリオ、継続探索者、複数シナリオをまたぐキャンペーン状態、GUI、音声、外部VTT連携。
- ただし自由生成の将来実装は、開始前に真相と主要因果を固定する原則を守る。

## Functional Requirements

### Scenario preparation

- **FR-SCN-01:** シナリオ原本はUTF-8のMarkdownまたはプレーンテキストとして、シナリオ単位のワークスペースへ配置できる。
- **FR-SCN-02:** 原本は進行中に変更せず、Keeper用索引、公開状態、進行記録は派生ファイルへ保存する。
- **FR-SCN-03:** 開始前検証は対象版、ルール参照元、シナリオ識別子、原本、開始地点、登場人物、既知の秘匿区分、必要な初期キャラクターを確認する。
- **FR-SCN-04:** 不足や矛盾を検出した場合、Keeperは補完内容を事実として捏造せず、開始前にユーザーへ示す。
- **FR-SCN-05:** ユーザーは結末や真相を知らずに原本を提供するものとする。構造化結果、検査報告、確認質問は未開示の真相、結末、犯人、手掛かり、NPC秘密を明かさず、開始可否と入力上の不足だけを伝える。

### Character creation and rules

- **FR-RUL-01:** 最終目標ではユーザー探索者を対象版のフル手順で作成し、質問分割、候補提示、自動計算で操作を支援する。ただし利用可能な参照元がQuick-Startのみの間は簡易作成プロファイルに限定し、フル手順対応を表示・推測しない。
- **FR-RUL-02:** ダイス結果、適用した技能・能力、難易度、ボーナス/ペナルティ、結果区分、参照根拠を追跡できる。
- **FR-RUL-03:** ルール参照元で確認できた裁定とKeeperの暫定裁定を区別する。根拠不足が不可逆な結果へ影響するときは確定前に確認する。
- **FR-RUL-04:** skills/scriptsは計算と手順案内を補助するが、恒久的な運営規則は`OUTPUT_AGENTS.md`に再現可能でなければならない。

### Input intent

- **FR-INP-01:** 入力を`Character Speech`、`Character Action`、`Player to Keeper`のいずれかとして処理する。
- **FR-INP-02:** 明示指定がなければ文脈から推定し、曖昧、秘匿性あり、危険、不可逆、意図しない公開発言になり得る場合だけ確認する。
- **FR-INP-03:** Speechはその場で聞ける人物の知識と反応へ、Actionは必要な判定と状態変化へ接続し、Player to Keeperはゲーム内人物の知識へ伝播させない。

### Information boundaries

- **FR-INF-01:** `Public`、`Keeper Only`、NPCごとの`NPC Knowledge`、`Character Sheet`を論理的に分離する。
- **FR-INF-02:** Keeperの公開応答は公開済み情報と今まさに開示する情報だけを含み、未開示の真相、手掛かり、NPCの秘密・理由を漏らさない。
- **FR-INF-03:** NPC判断は、そのNPCの人物像、状態、目的、恐怖、倫理観、個別知識、誤解だけを根拠とし、Keeperだけが知る情報を使わない。
- **FR-INF-04:** 同じ場にいない、知覚できない、伝達されていない情報はNPC Knowledgeへ自動追加しない。

### Autonomous NPCs

- **FR-NPC-01:** 自律傾向はキャラクターシートから推定し、必要なら明示的な微調整を記録できる。
- **FR-NPC-02:** NPCをユーザーに都合のよい安全な補助役へ制約しない。人物像と所持情報に沿うなら、提案、拒否、離脱、秘匿、虚偽、単独行動、裏切りを選択できる。
- **FR-NPC-03:** 重要行動は、判断時点、参照した個別知識、人物内の理由、表向きの説明、結果をKeeper専用記録へ残す。
- **FR-NPC-04:** 行動理由の記録は行動の許可判定ではなく、知識越境とご都合主義を事後検証するために使う。

### Scene lifecycle and persistence

- **FR-STA-01:** シーンは開始、進行中、終了処理、確定済みの状態を持つ。
- **FR-STA-02:** シーン終了時に公開状態、キャラクター状態、NPC個別知識、手掛かり状態、重要判断、次の開始地点を一貫したcheckpointとして更新する。
- **FR-STA-03:** ユーザーには変更対象と公開済み内容だけをシステムメッセージ形式で通知する。
- **FR-STA-04:** 中断後は、原ログを再解釈せず、最後の確定済みcheckpointから情報境界を維持して再開できる。
- **FR-STA-05:** 長編向けに原ログ、派生要約、現在状態を分け、全履歴を毎回読み直さずに再開できる。
- **FR-STA-06:** シーン境界はKeeperが場所、時間、目的、参加者、緊張状態の変化から内部的に決め、通常は確認操作を要求せず次の場面へ自然に接続する。ユーザーの明確な中止指示がある場合だけ安全な中断checkpointを作る。

## Quality and Operational Requirements

- **QR-01 Traceability:** 重要な状態変更は発生シーン、根拠、変更前後を追跡できる。
- **QR-02 Consistency:** checkpointは途中状態を残さず、失敗時に直前の確定状態へ戻せる設計とする。
- **QR-03 Spoiler safety:** 通常のチャット応答と公開用ファイルにKeeper/NPC秘匿情報を混入させない。
- **QR-04 Long-form readiness:** シーン数、中断回数、ログ総量が増えても、現在状態と必要な直近文脈を限定して読み込める。
- **QR-05 Source integrity:** シナリオ原本を進行状態の更新先にしない。
- **QR-06 Explainability:** NPCの意外な重要行動を、セッション終了後に当時の知識と人物像から説明できる。
- **QR-07 Pace:** 明確で低リスクな入力ではモード確認を挟まず進行できる。
- **QR-08 Immersion:** 内部の索引生成、シーン境界、checkpoint更新を必要以上に会話へ露出せず、物語の連続性を優先する。
- **QR-09 Secrecy boundary:** 秘匿保証は通常チャット、公開ファイル、公開通知を対象とする。同一リポジトリのKeeper/NPC専用ファイルをユーザーが直接開く場合は対象外とする。

## Execute Handoff Readiness

Requirements/Designを承認する前に、次を満たす必要がある。

1. 全FR/QRが`design.md`の構造または処理へ対応している。
2. 全FR/QRに`acceptance_criteria.md`の検証項目があるか、初回対象外の理由がある。
3. 未決事項が実装者のゲーム方針判断を必要としない状態になっている。
4. フォルダ・ファイル責務、読取境界、更新順序、失敗時の扱いが定義されている。
5. Executeで作るテンプレート、script/skill候補、`OUTPUT_AGENTS.md`規則が列挙されている。

## Verified Quick-Start Rules Baseline (2026-07-26 addendum)

The detailed source of truth is [`rule_ledger.md`](rule_ledger.md). This addendum narrows and details the existing FR-RUL baseline without changing Phase 2 approval state.

- **FR-RUL-01 (RUL-CHR-01..02, RUL-DRV-01..03, RUL-SKL-01..04):** Support the verified five-step Quick-Start creation path only: fixed characteristic array, floored half/fifth values, derived-value formulas/table, fixed occupation allocations, four personal-interest increases, concise backstory and final fields. Mark campaign finances and unlisted creation options as outside Quick-Start.
- **FR-RUL-02 (RUL-RES-01..03, RUL-MOD-01, RUL-OPP-01, RUL-LCK-01):** Record raw D100 components/candidates, selected result, threshold values, success level, difficulty, modifier cancellation/selection, opposed participant values/tie-break, and source page. Equality at a threshold succeeds.
- **FR-RUL-03 (RUL-PSH-01..02, RUL-SCOPE-01..05):** A push requires an initial failure, a justified changed approach, Keeper permission, one reroll, and a declared/recorded escalated consequence. Combat cannot be pushed. Missing rules set `core_rule_check_required`; no inferred completion is permitted.
- **FR-RUL-04 (all ledger IDs):** Skills/scripts may encode only ledger-confirmed deterministic operations. `OUTPUT_AGENTS.md` owns invariant Keeper behavior and the no-inference/source-record rule; scenario-local mechanics remain scenario data.
- **FR-RUL-05 (RUL-CMB-01..05, RUL-DMG-01..03):** Resolve Quick-Start combat in DEX order, preserve the distinct fight-back/dodge tie rules, apply firearm/maneuver/outnumbered modifiers, and calculate damage/Extreme damage only for confirmed weapon categories.
- **FR-RUL-06 (RUL-INJ-01, RUL-HEAL-01..02):** Apply HP floor, major-wound threshold, immediate-death strict comparison, consciousness/dying branches, stabilization, and natural/First Aid/Medicine healing in the recorded order.
- **FR-RUL-07 (RUL-SAN-01..03, RUL-INS-01..02):** Apply SAN success/failure loss, single-roll 5+ loss INT branch, temporary-insanity duration/bout/state changes, Reality Check, and only the recovery rules explicitly present. Flag the complete SAN system as requiring core rules.
- **FR-RUL-08 (RUL-KPR-01..02, RUL-SCN-01..03):** Separate universal Quick-Start procedures from Keeper discretion and `scenario_id`-scoped mechanics; never expose or promote pp.21–39 spoiler data as a generic rule.
- **FR-RUL-09 (source capability gate):** Declare the requested rules profile and available source set before play. Classify each requested mechanic as `verified`, `scenario_local`, `core_rule_check_required`, `keeper_ruling_required`, or `unsupported`; do not label the Quick-Start creation path as full current-edition creation.
- **FR-RUL-10 (provenance record):** A mechanical result retains profile, ledger/page references, scenario scope where applicable, declared goal, pre-state, roll candidates/selection, thresholds/modifiers, selected branch, state delta, and unresolved-source flag. The public rendering may redact spoiler-bearing provenance but must retain it in Keeper-only state.
- **FR-RUL-11 (authority namespaces):** Universal rules, examples, character-sheet labels, and scenario-local mechanics/assets use separate namespaces. Import never promotes an example, sheet field, scenario statistic, local difficulty, hazard, reward, or handout into a universal rule.
- **FR-RUL-12 (conflict stop):** Conflicting or ambiguous authorities are recorded rather than silently merged. A scenario instruction may override a generic assumption only within its scenario; unresolved authority blocks irreversible effects and requests a source or explicit reversible Keeper ruling.
