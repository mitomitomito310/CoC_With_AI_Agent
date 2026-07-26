---
name: coc-resolve-sanity
description: 検証済み資料の範囲だけでSAN判定、喪失、一時的狂気、現実検証と状態差分を処理する。恐怖遭遇やSAN状態変更で使用する。
---

# 正気度処理

1. active profileでSAN branchのcapabilityとledger/pageを確認する。完全SANをQuick-Startから推測しない。
2. SAN判定を基本判定へ委譲し、成功/失敗の損失式をシナリオscopeとともに記録する。
3. 損失を決定してから状態分岐を評価し、順序をresolutionへ残す。単一ロール5以上なら確認済みINT分岐だけを処理する。
4. 一時的狂気、bout、phobia/mania、Reality Checkは確認済み範囲だけ適用する。不明な失敗効果はsource gateで停止する。
5. SAN/condition deltaはcheckpointまで適用済みにしない。公開描写へ秘密の原因や表を露出しない。
