# Agent Profile Switching

## Status

- Phase: 3. Execute
- Development profile: root `AGENTS.md`
- Candidate game profile: `OUTPUT_AGENTS.md`
- Skill source: repository `skills/`

## Isolated trial

グローバル設定を直接変更せず、一時ディレクトリで候補を試す。

```bash
trial_home="$(mktemp -d)"
mkdir -p "$trial_home/skills" "$trial_home/profile"
cp -R skills/. "$trial_home/skills/"
cp OUTPUT_AGENTS.md "$trial_home/profile/AGENTS.md"
printf '%s\n' "$trial_home" > implementation/3_execute/.active_trial_home
```

試験記録には、Git commit、profile path、有効にしたskill名、scenario fixture、開始・終了時刻を残す。開発作業とゲーム試験を同じチャットで混在させない。

## Validation before activation

```bash
for skill in skills/*; do
  python /opt/codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
pytest
```

validatorが環境依存で起動できない場合は原因を記録し、frontmatter、名前、`agents/openai.yaml`を代替検査する。ゲーム試験の合格とは扱わない。

## Restore

```bash
trial_home="$(cat implementation/3_execute/.active_trial_home)"
rm -rf "$trial_home"
rm implementation/3_execute/.active_trial_home

test -f AGENTS.md
git diff --exit-code -- AGENTS.md
```

root `AGENTS.md`を`OUTPUT_AGENTS.md`で上書きしない。昇格はPhase 4の承認後だけ行う。
