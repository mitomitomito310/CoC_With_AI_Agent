---
name: coc-run-scene
description: 3入力モード、NPC別知識、Keeper秘密、シーン境界を管理しながら没入的なCoCシーンを進行する。ゲーム内の発話、行動、Keeper相談への応答で使用する。
---

# シーン進行

1. 入力を `speech`、`action`、`keeper` に分類する。不可逆で曖昧な場合だけ確認する。
2. NPCごとに本人のsheet、個別knowledge、知覚した公開情報、現在観測だけを投影する。他NPCやKeeper秘密を入れない。
3. 発話は聞こえる人物へ伝播し、行動は必要時だけ判定へ委譲し、Keeper相談は世界状態を変えない。
4. 場所、時刻、目的、参加者、緊張の変化でKeeperが境界を判断し、確認を挟まず自然に次へ進める。
5. eventをappendし、変更候補をpendingへ置く。確定は`coc-manage-session`へ委譲する。
6. 公開文を秘密語と意味の両方で確認する。明示的な中止だけをpauseとして扱う。
