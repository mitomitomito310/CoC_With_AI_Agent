---
name: coc-prepare-scenario
description: ネタバレを出さずにCoCシナリオを取り込み、原本保全、manifest、開始可否、Keeper索引を準備する。Markdown/テキストのシナリオ準備、検証、再取込で使用する。
---

# シナリオ準備

1. 原本を `scenarios/<scenario_id>/source/` にコピーし、以後変更しない。SHA-256を記録する。
2. `schemas/scenario.schema.json` に従い `scenario.json` を `importing` で作る。
3. 真相、結末、未発見手掛かり、NPC秘密をKeeper領域だけに分類する。解析内容をユーザーへ確認させない。
4. 対象版、rule profile、opening、actors、秘匿区分を検査する。`python tools/coc_validate.py scenario ...` を使う。
5. 不足があれば `blocked` とblocking issueだけを公開し、内容を推測しない。揃えば `preparing -> ready` と遷移する。
6. 公開応答は「開始可能」「入力不足」「解析不能」のいずれかと安全な不足項目だけにする。意味上の漏洩も手動確認する。

原本を書き換える、シナリオ固有ルールを普遍ルールへ昇格する、秘密を公開ファイルへ書くことを禁止する。
