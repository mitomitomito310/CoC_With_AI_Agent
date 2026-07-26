---
name: coc-manage-session
description: CoCセッションのpending変更を原子的checkpointへ確定し、current、resume、中断、復旧を管理する。シーン終了、保存、中断、再開、破損復旧で使用する。
---

# セッション状態管理

1. append-only events/resolutions、current、pendingのbase versionを読む。
2. 各changeのbeforeが現在値と一致し、visibility、event/resolution参照があることを検査する。
3. `python tools/coc_checkpoint.py ...`でcheckpointとcurrentを原子的に書く。部分更新を正にしない。
4. `python tools/coc_resume.py <current.json> <resume-dir>`でpublic、Keeper、NPCごとに別ファイルへ投影する。単一の公開resumeへ秘密を混在させず、再開に必要な最小文脈だけを書く。
5. シナリオstatusは `tools/coc_state.py` の許可遷移だけを使う。明示中止は`active -> paused`、再開は`paused -> active`とする。
6. 失敗時は最後のcommitted checkpointを正としてpendingを診断し、勝手に適用しない。
