---
name: coc-create-investigator
description: 有効なCoCルールプロファイルに従って探索者作成を案内し、出典、選択、計算、未完項目を記録する。新規探索者やキャラクターシート検証で使用する。
---

# 探索者作成

1. sessionのrules profileとsource capabilityを読む。
2. Quick-Startのみなら簡易作成と明示し、完全作成を名乗らない。`full_creation=core_rule_check_required`なら停止して必要資料を求める。
3. 選択を一段ずつ提示し、ユーザーの人物像を優先する。未確認の数式や選択肢を補完しない。
4. `schemas/character.schema.json`へ能力、技能、HP、SAN、条件と出典を保存する。途中選択と計算根拠を監査記録へ残す。
5. 必須欄、値域、派生値、未完選択を検査し、完了前にシートを再確認する。
