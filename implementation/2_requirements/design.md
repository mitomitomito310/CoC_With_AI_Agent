# Design

## Document Status

- Status: Approved (2026-07-25)
- Open decisions: なし

## Design Principles

1. 原本、現在状態、履歴を分離し、進行によって原本を書き換えない。
2. 情報は「誰がいつ知ったか」を記録し、ファイル名だけでなく参照規則で境界を守る。
3. NPCの自由を行動制限で守るのではなく、人物像と知識に基づく判断および事後追跡性で守る。
4. 短編で検証するが、長編では原ログを残したまま派生要約を使える構造にする。

## Repository Model

```text
scenarios/<scenario_id>/
├── scenario.yaml              # 識別子、タイトル、対象版、状態、原本一覧
├── source/                    # ユーザー提供原本（読み取り専用）
├── keeper/
│   ├── truth.md               # 真相と固定された主要因果
│   ├── clue_index.yaml        # 手掛かり、発見条件、開示状態への索引
│   └── preparation.md         # 開始前検証結果と不足事項
├── public/
│   ├── state.md               # 公開済みの現在状態
│   └── handouts/              # 公開済み配布物
├── characters/
│   ├── player/<character_id>/sheet.yaml
│   └── npc/<character_id>/
│       ├── sheet.yaml         # 能力、技能、状態、人物像、自律傾向
│       ├── knowledge.yaml     # 知識、誤解、秘密、取得経路
│       └── decisions.md       # 重要判断の秘匿追記ログ
├── scenes/
│   └── <scene_id>/
│       ├── log.md             # 原則追記型の出来事ログ
│       ├── checkpoint.yaml    # シーン確定時の変更集合
│       └── summary.md         # 再開・長編参照用の派生要約
└── session/
    ├── rules.yaml             # 対象版、利用可能な参照元、暫定裁定
    ├── current.yaml           # 現在シーン、時刻、場所、参加者、状態版
    └── resume.md              # 次回開始に必要な公開・Keeper別要約
```

YAMLは機械的な検証・更新が必要な状態、Markdownは人間が読む原文・説明・ログに使う。具体的なschemaとテンプレートはExecuteで作る。

## Information Access Matrix

| Actor/process | Public | Keeper Only | Own NPC Knowledge | Other NPC Knowledge | Character Sheet |
| --- | --- | --- | --- | --- | --- |
| User-facing response | Read | No direct output | Disclosed portions only | No | Public/owned portions |
| Keeper reasoning | Read | Read | Read | Read | Read |
| NPC decision | Perceived/received only | No | Read | No | Own sheet + observed public state |
| System update notice | Changed public facts only | No | No | No | Public changes only |
| Post-session audit | Read | Read when explicitly requested | Read | Read | Read |

「Keeper reasoningが読める」ことと「NPCの判断根拠として使える」ことを分ける。NPCを演じる際は、そのNPC用の入力コンテキストへKeeper Onlyや他NPCの知識を含めない。

## Scenario Preparation Flow

1. 新しい`scenario_id`を割り当て、原本を`source/`へ保存する。
2. 対象版、参照元、原本一覧をmanifestへ記録する。
3. 真相、結末、主要因果、手掛かり、登場人物、開始条件をユーザーへ表示せずKeeper用索引へ抽出する。
4. 原本との矛盾、欠落、曖昧な開始条件、必要なキャラクターを検査する。
5. Keeper専用の構造化内容は確認させず、「開始可能」「解析不能」「入力不足」の状態だけをネタバレなしでユーザーへ返す。
6. 重大な欠落で開始できない場合だけ、秘密や正解を含まない抽象度で追加入力を求める。軽微な曖昧さはKeeper専用の暫定解釈として記録する。

## Input Mode Processing

| Mode | Game-world effect | Roll | Knowledge propagation | Log |
| --- | --- | --- | --- | --- |
| Character Speech | その場で実際に発言 | 原則なし | 聞き取れる登場人物へ伝播 | 公開または場面限定ログ |
| Character Action | 実行意図として受理 | 必要時のみ | 観測者へ結果を伝播 | 行動、判定、結果 |
| Player to Keeper | メタ相談・ルール確認 | 実行しない | ゲーム内へ伝播しない | メタログまたは記録なし |

処理順は、明示指定の検出、文脈推定、確認条件評価、必要時確認、実行、知識伝播、ログ記録とする。確認前には不可逆な状態変更やNPC反応を起こさない。

## NPC Decision Pipeline

1. NPC自身のsheet、状態、knowledge、現在知覚できるPublic情報だけを集める。
2. 目的、恐怖、倫理観、関係性、秘密、誤解から選択肢を生成する。
3. キャラクターとして最も妥当な行動を選び、ユーザー支援やパーティー維持を暗黙の優先条件にしない。
4. 単独行動、虚偽、離脱、裏切りを含め、そのまま実行可能性をKeeperが世界状態とルールから裁定する。
5. 重要行動なら参照知識、人物内理由、表向きの説明を`decisions.md`へ記録する。
6. 観測可能な結果だけをPublicおよび他人物のknowledgeへ反映する。

## Scene Transaction

1. シーン中の出来事は`log.md`へ追記し、状態変更候補を作業集合として蓄積する。
2. Keeperが場所、時間、目的、参加者、緊張状態の変化から物語上のシーン境界を判断し、状態、手掛かり、所持品、ダメージ、NPC knowledge、重要判断、次の開始地点の差分を検査する。
3. 秘匿漏洩と矛盾がないことを確認して`checkpoint.yaml`へ一括確定する。
4. `public/state.md`、各キャラクター状態、`session/current.yaml`、`resume.md`をcheckpointから更新する。
5. 秘匿を除いた変更概要は没入を妨げない短いシステム表示にまとめ、確認を待たず次の場面へ接続する。
6. ユーザーが「中止」「今日はここまで」「保存して終了」など明確に指示した場合、進行中シーンの安全な中断checkpointと再開地点を作る。曖昧な発言は中止とみなさない。

途中失敗時はcheckpointを確定せず、直前の確定版を正とする。

## Long-form Strategy

- `log.md`は監査可能な原記録として保持する。
- `summary.md`は原ログから再生成可能な派生情報とする。
- `session/current.yaml`と`resume.md`は現在状態と直近文脈だけを提供する。
- 章単位の要約・アーカイブ境界を設け、通常の再開では全ログを読み込まない。

要約とcheckpointが競合する場合はcheckpointを正とし、原ログとcheckpointから要約を再生成する。

## Execute Deliverables

- 上記ツリーとschemaに対応するシナリオ雛形。
- 開始前validator、ダイス・計算支援、checkpoint整合性検査のscript/skill候補。
- 開発用`AGENTS.md`とゲーム用`OUTPUT_AGENTS.md`を切り替える手順。
- Keeper参照境界、NPC pipeline、3モード、scene transactionを記載した`OUTPUT_AGENTS.md`更新案。
- 短編サンプルまたはfixtureと、正常系・漏洩系・再開系の試験入力。

## Rule Resolution Record and Processing Pipeline

The rule ledger IDs are defined in [`rule_ledger.md`](rule_ledger.md). A resolution is append-only; later state changes reference it rather than rewriting it.

```yaml
resolution:
  id: roll-0001
  rules_profile: coc7e_quick_start_2016_ja
  capability_status: verified # verified | scenario_local | core_rule_check_required | keeper_ruling_required | unsupported
  scenario_id: null              # required for RUL-SCN-* mechanics
  actor_id: investigator-01
  intent: "observable goal agreed with Keeper"
  pre_state_refs: [character-state-v3]
  check:
    kind: skill                   # skill | characteristic | luck | sanity | combat
    name: Spot Hidden
    full_value: 55
    difficulty: hard
    thresholds: {regular: 55, hard: 27, extreme: 11}
  modifiers:
    bonus: 1
    penalty: 1
    net: 0
    reason: ["source facts"]
  dice:
    source: script               # script | user_supplied
    ones: 4
    tens: [20]
    candidates: [24]
    selected: 24
    selection: only
  outcome:
    success_level: hard          # failure | regular | hard | extreme
    meets_difficulty: true
    opposed: null                # participant results, values, tie-break when used
  push:
    eligible: true
    requested: false
    changed_approach: null
    failure_consequence: null
    reroll_resolution_id: null
  application:
    rule_effects: []
    state_delta_ids: []
    applied: false
  references:
    ledger_ids: [RUL-RES-02, RUL-MOD-01]
    source: NewCoC-QS_200228.pdf
    pages: [14, 15]
    core_rule_check_required: false
    keeper_ruling: null
  authority_conflict: null        # conflicting profiles/pages and resolution, if any
```

Processing order is fixed:

1. **Frame:** classify intent, agree goal, decide whether uncertainty warrants a roll, and select skill/characteristic and `scenario_id` (RUL-RES-01, RUL-KPR-01).
2. **Build thresholds:** floor half/fifth, select required difficulty, and preserve the full value used (RUL-CHR-02, RUL-RES-02).
3. **Normalize modifiers:** cancel bonus/penalty pairs; retain every reason and candidate-tens die (RUL-MOD-01).
4. **Roll/select:** record source and raw components; create D100 candidates including the `00/0 = 100` rule; choose lowest/highest as required (RUL-RES-03, RUL-MOD-01).
5. **Classify:** determine success level, then whether it meets difficulty. For opposed/melee, compare both records using the applicable tie rule before any effect (RUL-OPP-01, RUL-CMB-02).
6. **Offer push only after failure:** exclude combat, require a changed approach and Keeper approval, and record the escalated failure consequence before the reroll (RUL-PSH-01..02).
7. **Derive effect:** calculate combat damage, injury, healing, or SAN branches in domain order without mutating state yet (RUL-DMG-*, RUL-INJ-*, RUL-HEAL-*, RUL-SAN-*).
8. **Apply atomically:** append the resolution, then apply referenced state deltas once. Mark `applied`; never apply an unreferenced narrative result.
9. **Cite/stop:** attach ledger IDs and PDF pages. If a required branch is absent, set `core_rule_check_required: true` and stop before irreversible application (RUL-SCOPE-*; FR-RUL-03).

Before step 1, the session registers a source manifest and rules profile. Only `verified` or correctly scoped `scenario_local` capabilities enter the normal pipeline. `core_rule_check_required` and `unsupported` stop; `keeper_ruling_required` may proceed only as an explicit, local, reversible ruling. Universal ledger rules, worked examples, sheet fields/base values, scenario mechanics, and handout assets occupy different authority namespaces. A conflict is retained in `authority_conflict` and blocks irreversible state deltas until resolved.

The complete page-by-page source classification and acquisition backlog are maintained in [`source_review.md`](source_review.md); the design consumes that classification rather than parsing all PDF content into a universal rule store.
