---
name: coc-resolve-check
description: CoC 7版の百分率判定を、ルール能力ゲート、ダイス由来、閾値、分岐、状態差分まで追跡可能に処理する。技能判定、対抗判定、ボーナス・ペナルティ、プッシュ判断で使用する。
---

# 基本判定

1. 目的、技能/能力、難易度、修正、profile、ledger ID、page、pre-stateを先に確定する。
2. capabilityが`verified`または正しくscopeされた`scenario_local`でなければ停止する。権威競合中は不可逆差分を適用しない。
3. script生成または明示された物理ダイスを `tools/coc_resolve.py` へ渡す。結果を都合よく変更しない。
4. `schemas/resolution.schema.json`に従いraw candidates、選択値、閾値、分岐、未適用のdeltaをappend-onlyで保存する。
5. Keeper裁量を計算結果と分離する。プッシュは方法変更と失敗時結果を記録し、戦闘では許可しない。
6. checkpointがresolution IDを参照したときだけdeltaを一度適用する。
