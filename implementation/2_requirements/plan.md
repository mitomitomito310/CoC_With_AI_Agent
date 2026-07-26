# Plan

## Status

- Phase: 2. Requirements/Design
- Status: Completed
- Approval: Approved (2026-07-25)
- Current question: なし
- Recommended option: なし
- User answer: シナリオの結末を知らないユーザーが原本を渡す前提でネタバレを防ぐ。秘匿保証はチャットと公開ファイルまで。シーン境界はKeeperが没入感を損なわず判断し、ユーザーの明示的中止がない限り進行を継続する。原ログは不変保持し、要約と現在状態を派生更新する。次はPhase 3の実装計画を作る
- Next action: 確定成果物をPhase 3へ引き渡す

## Deliverables

- `requirements.md`: スコープ、機能・品質・運用要件、実装フェーズへの引き渡し条件
- `design.md`: シナリオ構造、情報境界、状態遷移、3モード、NPC判断、ルール支援の設計
- `acceptance_criteria.md`: 要件IDに対応する検証可能な合格条件
- `risk_notes.md`: リスク、兆候、予防策、実装・テストへの申し送り

## Phase Exit Checklist

- [x] Ideationの確定事項を要件ID付きで整理した
- [x] 短編MVPと長編対応設計の境界を定義した
- [x] ディレクトリ構造と主要ファイルの責務を設計した
- [x] 情報参照境界、3モード、NPC判断、シーン更新を設計した
- [x] 要件ごとの受け入れ条件と主要リスクを文書化した
- [x] 下記4件の設計判断をユーザー回答で確定する
- [x] 回答後に全成果物間の整合性を確認する
- [x] Phase 3の実装計画作成指示をもってRequirements/Designの基準線を確定する

## Decisions

| Date | Question | Options | Recommended | Answer | Result |
| --- | --- | --- | --- | --- | --- |
| 2026-07-25 | Requirements/Designフェーズへ進むか | 開始 / Ideationの追加修正 | 開始 | 承認、次のステージへ進む | フェーズ2開始 |
| 2026-07-25 | 最初の5設計質問 | 1A〜C / 2A〜C / 3A〜C / 4A〜C / 5A〜C | 1A / 2A / 3A / 4A / 5A | 1A（長編対応可能）、2A、3A、4A、5A（キャラクター準拠で制約なし） | 要件・設計の前提へ反映 |
| 2026-07-25 | 承認前の成果物編集制約 | planのみ / 各成果物を草稿化 | 各成果物を草稿化 | 全ステージでplanだけに限定する制約を削除 | 4成果物を作成し、判断が必要な4点を抽出 |
| 2026-07-25 | 残る4設計判断 | 取込方式 / 秘匿保証 / シーン境界 / 長編ログ | ネタバレ防止 / 論理分離 / Keeper主導 / 原ログ保持 | 結末を知らないユーザーへネタバレしない、2A、Keeperが没入感を保って区切り明示中止まで継続、4A | 全成果物へ反映しPhase 2を確定 |

## Post-approval rule-source clarification (2026-07-26)

- User-directed clarification completed without changing the approved Phase 2 status: all 43 pages of `NewCoC-QS_200228.pdf` were classified into `rule_ledger.md`, and FR/AC/design/risk traceability was refined.
- Phase 3 questions about exact Quick-Start scope, missing complete SAN rules, rounding, combat tie exceptions, and scenario-local mechanics are returned here as resolved source constraints, not as a phase transition.
- Still unresolved and requiring the core rulebook before implementation: every `RUL-SCOPE-*` item, especially complete Sanity, Luck spending, chase, armor/automatic fire, full character creation/campaign economics, and other unlisted edge cases.
- Next action remains Phase 3 execution under the existing phase state; implementation must first consume ledger IDs and must not infer unresolved rules.
