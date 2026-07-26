# Risk Notes

## Document Status

- Status: Approved (2026-07-25)

| ID | Risk | Severity | Early signal | Mitigation | Verification / owner |
| --- | --- | --- | --- | --- | --- |
| R-01 | Keeper/NPC秘匿が公開応答や更新通知へ漏れる | Critical | 公開ファイルに未開示固有語が現れる | アクセス行列、公開前検査、秘匿fixtureを用意する | AC-INF-01 / Execute・Testing |
| R-02 | NPCがKeeperの真相を使い、キャラクターらしい自律性が崩れる | Critical | 取得経路のない正解へ直行する | NPC用コンテキストを分離し、knowledgeに取得経路を持たせる | AC-INF-02、AC-NPC-01 |
| R-03 | 「安全」の名目でNPCの対立行動が抑止される | High | NPCが常に同意・同行・情報共有する | ユーザー利益を暗黙目標にせず、人物内理由から選ぶpipelineを固定する | AC-NPC-01 / OUTPUT_AGENTS |
| R-04 | ルールを誤適用、または版を混同する | High | 根拠や対象版のない裁定 | session rulesに版・参照元・暫定裁定を記録する | AC-RUL-01..02 |
| R-05 | 原本の曖昧さをAIが捏造で補う | High | 原本にない真相や条件が確定情報になる | 開始前検証で不足と補完案を分け、確認後に固定する | AC-SCN-01 |
| R-06 | シーン更新の途中失敗で状態が食い違う | High | currentとcharacter/clue状態の版が異なる | checkpointを変更集合の正とし、確定前の部分更新を採用しない | AC-STA-01..02 |
| R-07 | 長編でログが肥大化し、重要情報を取り違える | High | 毎回全ログを読む、resumeが古い | 原ログ、派生要約、現在状態を分離し、要約再生成経路を持つ | AC-STA-03..04 |
| R-08 | 3モードの誤認で相談が発言・行動になる | High | メタ質問にNPCが反応する | 推定後にリスク条件を評価し、確定前確認を行う | AC-INP-01..02 |
| R-09 | 確認過多でセッションのテンポが落ちる | Medium | 低リスク入力でも毎回選択を求める | 確認条件を限定し、推定モードをログへ残す | AC-INP-02 |
| R-10 | 同じリポジトリをユーザーが直接読めばネタバレする | High | keeper/やNPC secretをユーザーが開く | 通常チャットと公開ファイルまでを保証範囲と明示し、専用ファイルの直接閲覧は対象外とする | AC-SCN-02 / OUTPUT_AGENTS |
| R-11 | 著作物の原本やルール本文を不必要に複製する | High | 派生資料に原文が大量転載される | ユーザー提供原本はsourceに保持し、派生資料は索引・参照・状態中心にする | Executeレビュー |
| R-12 | 要約が原ログと乖離し、誤った状態で再開する | High | summaryとcheckpointの事実が競合する | checkpoint/currentを正、summaryを再生成可能な派生物とする | AC-STA-03..04 |
| R-13 | 準備時の確認や構造化報告が結末を漏らす | Critical | 開始前応答に黒幕、結末、未発見手掛かりが現れる | 構造化はKeeper専用とし、ユーザーには開始可否と入力不足だけを返す | AC-SCN-02 |
| R-14 | シーン区切りや保存確認が物語を頻繁に中断する | High | 場面転換ごとに確認待ちになる | Keeperが内部的に境界を決め、短い通知後に自動継続する | AC-STA-06 |

## Residual Design Decisions

なし。実装中に新たな不足が判明した場合は、Phase 2の`plan.md`へ判断事項として戻す。

## Verified-rule risk addendum (2026-07-26)

| ID | Risk | Severity | Early signal | Mitigation | Verification / owner |
| --- | --- | --- | --- | --- | --- |
| R-15 | 7th-edition Quick-Start, another edition, English terminology, and Japanese core rules are mixed | High | Formula has no ledger ID/page or contradicts `rule_ledger.md` | Pin source/edition per resolution; implement only ledger-confirmed scope | AC-RUL-04..13 / FR-RUL-02..08 |
| R-16 | Quick-Start omissions are silently filled from memory | Critical | Luck spending, full insanity, chase, armor, or unlisted creation procedure appears without source | Use `RUL-SCOPE-*` and `core_rule_check_required`; stop irreversible effects | AC-RUL-06, AC-RUL-12 |
| R-17 | Half/fifth or HP boundary rounding/comparison is wrong | High | Rounded rather than floored threshold; `>` and `>=` conflated | Central deterministic floor helper; retain full and thresholds; boundary fixtures | AC-RUL-04, AC-RUL-09 |
| R-18 | Generic opposed tie logic is incorrectly used for dodge/fight-back or special damage | High | Equal dodge lets attack hit; fight-back wins tie; all Extremes use one formula | Dispatch to explicit ledger rule before generic comparison/damage | AC-RUL-07..09 |
| R-19 | Scenario-local exception becomes a universal rule or leaks spoilers | Critical | pp.21–39 condition lacks `scenario_id` or appears publicly | Store scenario mechanics separately with page/scope; spoiler scan outputs | AC-RUL-13 / FR-RUL-08 |
| R-20 | Ledger reproduces excessive copyrighted prose, tables, handouts, or scenario text | High | Long passages/table rows copied rather than procedural summaries | Retain formulas/branches/IDs/page pointers only; review diffs against source | Documentation review / Execute |
| R-21 | “Current/full rules” is claimed while only the Quick-Start source is available | Critical | Full creation, Luck spending, or long-term SAN is offered under the Quick-Start profile | Require a session capability declaration and reject unsupported profile claims | FR-RUL-09 / source review |
| R-22 | Sheet fields, examples, or scenario mechanics are promoted to universal rules | Critical | A rule record has no universal ledger ID or a scenario rule lacks `scenario_id` | Separate authority namespaces and validate imports against their source class | FR-RUL-11 / AC-RUL-15 |
| R-23 | A correct calculation cannot be reconstructed after state changes | High | Result stores only a total or prose outcome | Persist provenance-bearing resolution record and pre-state/state delta | FR-RUL-10 / AC-RUL-14 |
| R-24 | Conflicting sources are silently combined | High | Resolution cites incompatible profiles/pages without a conflict record | Stop irreversible resolution, record conflict, and request source or reversible ruling | FR-RUL-12 / AC-RUL-16 |
