---
name: coc-resolve-combat
description: 検証済みQuick-Start範囲でCoC戦闘順、近接対抗、ダメージ、重傷、瀕死を追跡可能に処理する。戦闘開始、攻撃、防御、負傷更新で使用する。
---

# 戦闘処理

1. 参加者、DEX、構えた銃器、行動済み、数的不利、pre-stateを確定する。
2. active profileで対象branchを確認する。chase、装甲、自動火器など未確認要素を推測しない。
3. 攻撃とdodge/fight-backを基本判定へ委譲し、同成功段階の勝者規則を防御種別ごとに適用する。戦闘ロールのpushを拒否する。
4. damageを `tools/coc_resolve.py` の純粋計算で導出し、HPを負にしない。重傷、即死、瀕死、気絶を順序通り記録する。
5. damage/condition deltaを未適用resolutionとしてappendし、checkpointで一度だけ適用する。
6. Keeper描写は計算記録を変更せず、未確認例外があれば不可逆効果の前に停止する。
