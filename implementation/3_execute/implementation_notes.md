# Implementation Notes

## Document Status

- Status: Draft
- Phase: 3. Execute (not approved)
- Scope: skill boundary and repository directory architecture only
- Working assumptions: the unanswered Phase 3 choices use the recommended baseline `1A / 2A / 3A / 4A`; these assumptions may be revised before approval.

## Architecture Decisions

1. Keep invariant Keeper policy in `OUTPUT_AGENTS.md`; skills orchestrate bounded workflows and must not become a hidden second policy document.
2. Keep deterministic calculation and validation in versioned scripts. A skill may invoke a script but must not reimplement its arithmetic in prose.
3. Keep rule authority in data records keyed by rules profile, ledger ID, source page, capability status, and optional `scenario_id`. Do not copy rulebook prose into a skill.
4. Store skill source in this repository under `skills/`. Activation into a Codex skill directory is a separate, auditable profile-switching step; development never edits a user's globally installed skill in place.
5. Separate reusable engine data from scenario workspaces. No scenario secret, character state, or session log belongs inside a skill folder.
6. Prefer a small number of workflow skills with progressively loaded references over one monolith or one skill per dice branch.

## Required Skills

### MVP workflow skills

| Skill | Trigger and responsibility | Reads | Writes/delegates | Hard stop |
| --- | --- | --- | --- | --- |
| `coc-prepare-scenario` | Import a Markdown/text scenario without spoiling it; establish manifest, source checksum, truth/clue indexes, actors, and readiness | immutable scenario source, templates, scenario schema | new scenario workspace; scenario validator | source cannot be classified, required opening data is absent, or a secret would enter public output |
| `coc-create-investigator` | Guide the selected, source-supported character-creation profile and report incomplete fields | rules profile, creation references, character schema | player sheet; character validator/calculator | requested creation option is outside the verified source capability |
| `coc-resolve-check` | Frame and resolve ordinary percentile, difficulty, modifier, opposed, push, and Luck checks with provenance | public/pre-state, rules profile, rule ledger subset | dice CLI and resolution engine; append-only resolution record | capability is unsupported/core-check-required, authority conflicts, or irreversible effect lacks a verified branch |
| `coc-run-scene` | Classify the three input modes, narrate, request checks, isolate NPC decision context, propagate observed knowledge, and detect scene boundaries | current/resume, public state, Keeper indexes, per-NPC context projection | check/combat/SAN skills; scene event stream; checkpoint skill | ambiguous input would cause irreversible change, NPC context projection fails, or output scan finds possible leakage |
| `coc-manage-session` | Commit an atomic checkpoint, rebuild current/resume/summary, pause, and recover from the last valid checkpoint | append-only events, pending deltas, previous checkpoint | checkpoint validator and state projector | partial/invalid transaction, stale state version, missing resolution reference, or public/secret boundary violation |

### Required domain skills

| Skill | Why it is separate | Initial scope |
| --- | --- | --- |
| `coc-resolve-sanity` | SAN changes and insanity branches are CoC-defining, stateful, and more leakage-sensitive than a normal check. Independent triggering prevents the general check skill from silently approximating incomplete SAN rules. | Only branches confirmed by the active source profile; missing complete-system behavior remains a source gate. |
| `coc-resolve-combat` | Combat has a distinct round/action pipeline, opposed/dodge/fight-back choices, damage and injury ordering, and a no-push rule. | Quick-Start-confirmed branches only; chase and unconfirmed full-rule exceptions are excluded. |

### Deferred skills

- `coc-run-chase`: add only after an authorized source defines the requested chase profile and dedicated acceptance fixtures exist.
- `coc-run-downtime`: add after short-session integrity is proven and improvement, recovery, finances, and campaign time have sourced rules.
- Do not create a generic `coc-rules` skill. It would trigger too broadly and duplicate `OUTPUT_AGENTS.md`, domain workflows, and the rule ledger.

## Skill Folder Contract

Each skill follows the standard progressive-disclosure layout. Only create optional directories when the skill actually uses them.

```text
skills/<skill-name>/
├── SKILL.md                 # concise imperative workflow and stop conditions
├── agents/
│   └── openai.yaml          # display name, short description, default prompt
├── references/              # optional; schema slices and workflow-specific indexes
├── scripts/                 # optional; thin launchers only when invocation is skill-specific
└── assets/                  # optional; copied templates, never live scenario data
```

`SKILL.md` owns the trigger, ordered workflow, required inputs, allowed outputs, redaction boundary, script calls, and failure behavior. Detailed rule/profile material stays in `rules/`; reusable schemas stay in `schemas/`; shared executable logic stays in `tools/`. A skill reference links to those repository resources rather than duplicating them.

## Proposed Repository Tree

```text
.
├── AGENTS.md                         # development-process profile until promotion
├── OUTPUT_AGENTS.md                  # invariant game/Keeper profile candidate
├── audit.md
├── skills/                           # version-controlled skill source
│   ├── coc-prepare-scenario/
│   ├── coc-create-investigator/
│   ├── coc-resolve-check/
│   ├── coc-run-scene/
│   ├── coc-manage-session/
│   ├── coc-resolve-sanity/
│   └── coc-resolve-combat/
├── rules/
│   ├── profiles/                     # enabled capabilities and source manifests
│   │   └── coc7e_quick_start_2016_ja.yaml
│   └── ledger/                       # executable summaries/provenance, no long prose
├── schemas/
│   ├── scenario.schema.json
│   ├── character.schema.json
│   ├── knowledge.schema.json
│   ├── event.schema.json
│   ├── resolution.schema.json
│   ├── checkpoint.schema.json
│   └── rules-profile.schema.json
├── templates/
│   └── scenario/                     # empty safe-to-copy workspace skeleton
├── tools/
│   ├── coc_dice.py                   # raw auditable dice components
│   ├── coc_resolve.py                # pure threshold/modifier/outcome calculations
│   ├── coc_validate.py               # schema and cross-reference validation CLI
│   ├── coc_checkpoint.py             # atomic projection/rebuild logic
│   └── coc_spoiler_scan.py           # heuristic gate; never the sole guarantee
├── tests/
│   ├── fixtures/
│   │   ├── minimal_original/         # authored, copyright-safe test scenario
│   │   ├── authority_conflict/
│   │   └── leakage_canary/
│   ├── unit/
│   ├── integration/
│   └── acceptance/
├── scenarios/                        # runtime data; one isolated workspace per scenario
│   └── <scenario_id>/
└── implementation/                   # AIDLC preparation records
```

Generated/runtime files should not be committed by default. A later `.gitignore` decision must distinguish authored fixtures from private scenarios instead of ignoring the entire `scenarios/` model blindly.

## Scenario Workspace

The approved Phase 2 model is retained and made transaction-oriented:

```text
scenarios/<scenario_id>/
├── scenario.yaml
├── source/                            # immutable originals and checksums
├── keeper/
│   ├── truth.md
│   ├── clue_index.yaml
│   ├── preparation.md
│   └── rulings.yaml
├── public/
│   ├── state.md
│   └── handouts/
├── characters/
│   ├── player/<character_id>/sheet.yaml
│   └── npc/<character_id>/
│       ├── sheet.yaml
│       ├── knowledge.yaml
│       └── decisions.md
├── scenes/<scene_id>/
│   ├── events.jsonl                  # append-only canonical scene events
│   ├── resolutions.jsonl             # append-only mechanical provenance
│   ├── checkpoint.yaml
│   └── summary.md                    # derived, rebuildable
└── session/
    ├── rules.yaml
    ├── current.yaml
    ├── pending.yaml                  # uncommitted transaction; never canonical
    └── resume.md
```

`events.jsonl` replaces the ambiguous writable `log.md` role as the machine-readable canonical event stream. Human-readable scene prose may be rendered into `summary.md`; it is never more authoritative than checkpoint plus append-only events/resolutions.

## Dependency Direction

```text
OUTPUT_AGENTS.md
      ↓ constrains
workflow skills ──→ schemas/rule profile ──→ deterministic tools
      ↓ orchestrate                              ↓ emit records
scenario workspace ←──────── append/checkpoint ─┘
```

- Skills may call tools and read rules/schemas/templates.
- Tools must not invoke skills or invent Keeper rulings.
- Scenario-local rules require `scenario_id` and source page; they never flow back into universal profiles.
- `coc-run-scene` may delegate a resolution but may not fabricate its result record.
- `coc-manage-session` may apply only deltas that reference accepted event/resolution IDs.

## Activation and Profile Separation

1. Treat `skills/` as source, not as automatically active configuration.
2. During development, keep the root `AGENTS.md` active and record selected skills as `none` unless a focused test explicitly activates them.
3. For a game-profile trial, stage only the required skill folders into an isolated Codex home or symlink set, use `OUTPUT_AGENTS.md` as the candidate instruction profile, and record profile/skill versions.
4. Restore the development profile after the trial and verify that no global skill or root instruction was overwritten.
5. Specify exact commands and rollback checks in `agent_profile_switching.md` before the first activation.

## Implementation Order

1. Create schemas for rules profile, resolution, event, knowledge, and checkpoint.
2. Implement pure dice/resolution and validators; verify AC-RUL-04 through AC-RUL-16 before prose-heavy orchestration.
3. Create the authored minimal fixture and leakage/authority-conflict fixtures.
4. Initialize each MVP skill with the skill-creator tooling, then replace all placeholders and validate every folder.
5. Implement `coc-resolve-check`, then combat/SAN, then scenario preparation, session management, and scene orchestration.
6. Complete `OUTPUT_AGENTS.md` and profile-switching instructions; test with skills disabled first, then enabled.

## Design Validation Gates

- Every skill has one primary workflow and explicit trigger language; no cyclic skill dependency exists.
- Every deterministic branch maps to FR-RUL, ledger ID, source/page, risk, and acceptance test.
- Every runtime mutation references an append-only event or resolution and is applied once at checkpoint.
- A projected NPC context contains only its sheet, own knowledge, perceived public facts, and current observations.
- Public output remains safe when Keeper-only file names, clue terms, and semantic leakage canaries are present.
- Removing all skills still leaves invariant Keeper behavior discoverable in `OUTPUT_AGENTS.md`.

## Open Confirmation

Before creating the folders and skill files, confirm or revise the working assumptions in `plan.md`: official-source strategy, responsibility-sized skill split, script/user-supplied dice policy, and use of an authored minimal fixture. The architecture above is a reversible draft and does not pass the Execute phase gate.
