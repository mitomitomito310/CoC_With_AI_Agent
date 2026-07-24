# エージェント指示

このリポジトリは、ゲームプロジェクト用の最終 `AGENTS.md` を作るための、軽量なAIDLC風の準備ワークスペースです。

## ディレクトリの流れ

`implementation/` ワークスペースは、次の順番で使います。

1. `implementation/1_ideation/` - ゲームのアイディアを出し、方向性を絞り込みます。
2. `implementation/2_requirements/` - 採用したアイディアから具体的な要件と設計を定義します。
3. `implementation/3_execute/` - 合意したゲーム固有の内容を実装し、開発環境で最終 `AGENTS.md` 候補を試します。
4. `implementation/4_testing/` - テスト計画、確認結果、検証メモを記録します。

## フェーズゲート

- 各フェーズは、ユーザーが明示的に承認するまで次のフェーズへ進みません。
- フェーズ開始時、エージェントはまず質問を提示します。できる限り選択肢と推奨案を含めます。質問は1回あたり3〜5個に絞ります。
- Ideationフェーズでは、質問提示の前に、エージェントの現時点での感想をかなりポジティブに伝えます。他フェーズでは現実的かつ建設的なトーンで進めます。
- ユーザーの回答は、そのフェーズの `plan.md` に短く記録します。
- Ideationフェーズでは、承認前でも発散した議論・感想・追加質問を `implementation/1_ideation/discussion_notes.md` に記録できます。`plan.md` は人間向けサマリ、`discussion_notes.md` はアイディア出しの作業メモとして使います。
- そのフェーズの `plan.md` と許可された作業メモ以外の成果物は、ユーザーが承認するまで作成・更新しません。
- 承認後にだけ、そのフェーズの成果物を作成・更新します。
- ユーザーが承認コメントを出した場合、その承認済みフェーズの成果物作成と `audit.md` 更新までは行いますが、次フェーズの作業は開始しません。作業後に「次のステージに進みますか？」「続きの実行などの指示をください」と促します。
- 承認が曖昧な場合は、作業を進めず、承認済みか確認します。

## フェーズごとの成果物

| フェーズ | 常に更新する計画 | 承認後に作る成果物 | 目的 |
| --- | --- | --- | --- |
| 1. Ideation | `implementation/1_ideation/plan.md` | `idea_candidates.md`, `selected_direction.md` | 複数案を比較し、採用するゲーム方向性を1つに絞ります。 |
| 2. Requirements/Design | `implementation/2_requirements/plan.md` | `requirements.md`, `acceptance_criteria.md`, `risk_notes.md` | 採用案を、実装可能な要件・設計・受け入れ条件・リスクに分解します。 |
| 3. Execute | `implementation/3_execute/plan.md` | `implementation_notes.md`, `agent_profile_switching.md`, `OUTPUT_AGENTS.md` 更新案 | 合意内容を最終エージェント指示へ反映し、開発環境で試せる状態にします。 |
| 4. Testing | `implementation/4_testing/plan.md` | `test_plan.md`, `test_results.md`, `final_review.md` | 最終指示がチャット上の実作業に耐えるか検証し、昇格可否を判断します。 |

## Executeフェーズでのチャットテスト方法

- 推奨方式は、最終成果物の `AGENTS.md` 候補を直接置き換える前に、プロファイル切り替え手順として `implementation/3_execute/agent_profile_switching.md` に記録して試すことです。
- 開発環境用プロファイルは、この初段 `AGENTS.md` と `audit.md` を使い、フェーズゲートと作業ログを守ります。
- 最終成果物用プロファイルは、`OUTPUT_AGENTS.md` を一時的な `AGENTS.md` 候補として読み替え、ゲーム制作タスクのチャットを小さく試します。
- skillsを使う場合は、開発環境用skillと最終成果物用skillを分け、どちらを有効にしているかを `plan.md` と `audit.md` に記録します。
- skillsは便利ですが、最終 `AGENTS.md` だけで再現できない暗黙ルールを増やさないようにします。恒久ルールは必ず `OUTPUT_AGENTS.md` に反映します。
- テスト中に見つかった迷い、危険な仮定、足りない制約は、`implementation/4_testing/test_results.md` ではなく、まず該当フェーズの `plan.md` に確認事項として戻します。

## 作業ルール

- ファイル名とディレクトリ名は英語のままにします。
- この初段の `AGENTS.md` は、最終的なゲームルールではなく、開発プロセスの要点に絞ります。
- 最終的なゲーム専用のエージェント指示は `OUTPUT_AGENTS.md` に作ります。
- `OUTPUT_AGENTS.md` は汎用的な内容にせず、提供された情報をもとに対象ゲームへ特化させます。
- 最終指示が完成したら、この初段の `AGENTS.md` を退避し、`OUTPUT_AGENTS.md` を `AGENTS.md` に昇格します。
- 進めながら改善できるように、小さく反復的に更新します。

## 作業ログルール

- 作業ログは `audit.md` に記載します。
- `audit.md` は別チャットへ移動しても引き継げる圧縮ログとして運用します。`Current` はフェーズ、固定方針、次アクションを中心にし、詳細な最新決定は1行履歴テーブルへ集約します。
- エージェントから質問し、ユーザーが回答したときは、質問と回答を1行で簡潔に記録します。
- 次のフェーズへ進んだときは、フェーズ変更、理由、次の作業を1行で記録します。承認指示がない限り、次アクションは質問継続を基本にします。
- 詳細な議論は成果物側に反映し、`audit.md` には決定と理由だけ残します。
- 古い履歴が増えたら、複数行を1行の要約に統合します。
