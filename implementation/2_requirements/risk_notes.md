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
| R-15 | クイックスタートを完全版または不特定の「最新版」と誤表示する | Critical | PDFにないSAN等の処理を断定する | rules profileと完全性を台帳化し、未収載処理は`unsupported_by_active_source`にする | AC-RUL-04 |
| R-16 | ボーナス/ペナルティ、対抗、戦闘の役割別規則を成功/失敗へ過度に単純化する | High | 生ダイスや回避/応戦の区別が残らない | 生ダイス、役割、同値、武器種、修正理由をroll logへ保存する | AC-RUL-05 |
| R-17 | SAN・重傷・瀕死・治療・MP・成長の時間状態が再開時に失われる | Critical | current値だけで発生時刻・状態フラグがない | 可変trackと期限をcheckpoint化し、複合fixtureで再開検証する | AC-RUL-06 |
| R-18 | シナリオ構造化で読み上げ文、Keeper注意、手掛かり条件を混同する | Critical | 秘匿文の公開、または手掛かりの無条件開示 | 型付きscenario index、原本locator、秘匿区分、開示状態を必須にする | AC-SCN-02、AC-INF-01 |

## Residual Design Decisions

なし。実装中に新たな不足が判明した場合は、Phase 2の`plan.md`へ判断事項として戻す。
