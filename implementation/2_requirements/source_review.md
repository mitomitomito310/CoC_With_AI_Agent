# Quick-Start Source Review

## Review purpose and status

- Source: `NewCoC-QS_200228.pdf`
- Extent: 43/43 PDF pages reviewed
- Role: evidence map for the Phase 2 requirements; not a substitute for the source book
- Spoiler policy: scenario pages are classified by function only. Their people, locations, clues, statistics, handouts, revelations, and conclusions are not reproduced here.
- Rule authority: executable details belong in [`rule_ledger.md`](rule_ledger.md). If this review and the ledger differ, implementation stops and the PDF page is rechecked.

The review separates three questions that must not be conflated: what the PDF actually states, what this product needs, and what still requires another authorized source. This prevents a familiar rule, a character-sheet field, or a scenario example from silently becoming a universal rule.

## 43-page coverage evidence

| PDF page(s) | Classification | Repository-relevant extraction | Destination / handling |
| --- | --- | --- | --- |
| 1 | Cover | Identifies the Japanese Quick-Start document. | Source identity only; `rule_ledger.md` source boundary. |
| 2 | Credits / publication data | Establishes publication and translation provenance. | Source metadata; do not treat credits as rules. |
| 3 | Contents / edition context | Confirms document structure and 7th-edition Quick-Start context. | Navigation and version pinning. |
| 4 | Introduction | Defines the Keeper/player relationship and says the booklet is not the complete rules. | `RUL-KPR-01`, `RUL-SCOPE-01..04`; require scope gates. |
| 5 | Play overview | Establishes conversational play, Keeper description, player declarations, and dice-mediated uncertainty. | Keeper turn loop and input-intent design. |
| 6 | Dice / example material | Defines percentile dice reading, including the `00` edge case. | `RUL-RES-03`; deterministic dice fixture. |
| 7 | Creation step 1 | Fixed characteristic array and half/fifth calculations. | `RUL-CHR-01..02`; creation-state validation. |
| 8 | Creation step 2 | Derived HP, MOV, SAN, Luck, MP, and MP recovery/over-spend behavior. | `RUL-DRV-01..02`; derived-field calculator. |
| 9 | Creation steps 2–3 | Damage bonus/build bands, sample occupations, and occupation-skill allocation start. | `RUL-DRV-03`, `RUL-SKL-01`; table-bound range guard. |
| 10 | Creation steps 3–5 | Completes occupation/personal-interest allocation, backstory/equipment guidance, and skill improvement marking. | `RUL-SKL-01..04`; creation workflow and improvement ledger. |
| 11 | Skill digest A | Abbreviated skill purposes and special timing/difficulty for treatment. | `RUL-SKL-03`, `RUL-HEAL-02`; descriptions are not complete core rules. |
| 12 | Skill digest B | Additional abbreviated skills and permission for concealed Psychology resolution. | `RUL-SCOPE-04`, `RUL-KPR-02`; secret-roll output boundary. |
| 13 | Skill digest C | Psychoanalysis recovery/fumble specifics and further abbreviated skills. | `RUL-SAN-03`, `RUL-SCOPE-05`; do not generalize fumbles. |
| 14 | Resolution | Goal-first rolls, difficulty levels, opposed rolls, modifiers, and pushed-roll entry. | `RUL-RES-*`, `RUL-MOD-01`, `RUL-OPP-01`, `RUL-PSH-01`. |
| 15 | Resolution continuation | Bonus/penalty candidate selection, Luck rolls, group Luck, and Keeper discretion. | `RUL-MOD-01`, `RUL-LCK-01`; Luck spending remains absent. |
| 16 | Sanity / combat entry | SAN loss and temporary-insanity entry; combat order and no combat pushes; explicit incompleteness of SAN rules. | `RUL-SAN-01..02`, `RUL-CMB-01`, `RUL-PSH-02`, `RUL-SCOPE-01`. |
| 17 | Insanity / melee | Bout/delusion handling plus melee responses, tie behavior, damage, and Extreme damage. | `RUL-INS-01..02`, `RUL-CMB-02..03`, `RUL-DMG-01`. |
| 18 | Combat continuation | Firearm timing/range/shots/cover and maneuver procedure. | `RUL-CMB-01`, `RUL-CMB-04..05`; weapon-specific dispatcher. |
| 19 | Injury / healing | Outnumbering, HP and major-wound branches, dying, First Aid, Medicine, and natural healing. | `RUL-CMB-05`, `RUL-DMG-02`, `RUL-INJ-01`, `RUL-HEAL-01..02`. |
| 20 | Other injury / improvement | Other-damage guidance, suffocation/drowning, poison, and skill improvement completion. | `RUL-DMG-03`, `RUL-SKL-04`; contextual damage remains source-bound. |
| 21 | Scenario: opening | Spoiler-bearing Keeper setup and scenario-local setup. | `RUL-SCN-01..02`; Keeper-only scenario namespace. |
| 22 | Scenario: background/start | Spoiler-bearing background, hooks, and opening material. | Keeper-only; never include details in import reports. |
| 23 | Scenario: investigation A | Research material, local checks, and clue delivery. | Scenario-local resolution records with page and `scenario_id`. |
| 24 | Scenario: investigation B | Research continuation and handout references. | Keeper-only clue graph; public only after in-fiction discovery. |
| 25 | Scenario: investigation C | Further research branches, consequences, and handout references. | Keeper-only; pushed consequences remain local. |
| 26 | Scenario: investigation D | Research/location material and transition toward the principal site. | Keeper-only scene index and prerequisite tracking. |
| 27 | Scenario: principal site A | Site description, encounters/hazards, and local checks begin. | Keeper-only location graph; no universal-rule promotion. |
| 28 | Scenario: principal site B | Site continuation with local state and consequences. | Keeper-only scene state and local mechanics. |
| 29 | Scenario: principal site C | Site continuation, encounter information, and conditional effects. | Keeper-only actor/location data; source-tag all effects. |
| 30 | Scenario: principal site D | Site continuation and escalating local mechanics. | Keeper-only; preserve trigger/result provenance. |
| 31 | Scenario: climax material | Spoiler-bearing antagonist/tactical or climactic handling. | Keeper-only actor/tactic records; block from NPC knowledge unless learned. |
| 32 | Scenario: resolution | Spoiler-bearing conclusions, outcomes, or rewards. | Keeper-only terminal branches; publish only reached outcome. |
| 33 | Player handout 1 | Scenario handout asset. | Immutable source asset; release state tracked separately. |
| 34 | Player handout 2 | Scenario handout asset. | Same handling; asset contents are not generic rules. |
| 35 | Player handout 3 | Scenario handout asset. | Same handling; access only after release condition. |
| 36 | Player handout 4 | Scenario handout asset. | Same handling; record source page on release. |
| 37 | Player handout 5 | Scenario handout asset. | Same handling; public copy must not carry adjacent Keeper data. |
| 38 | Player handout 6 | Scenario handout asset. | Same handling; retain original unchanged. |
| 39 | Player handout 7 | Scenario handout asset. | Same handling; close scenario-source page range. |
| 40 | Investigator sheet | Blank sheet front/back material and printed fields/base values. | UI/schema evidence only; sheet presence does not define missing procedures. |
| 41 | Investigator sheet | Continuation/duplicate sheet material. | Same handling; validate field mapping without inventing rules. |
| 42 | Investigator sheet | Additional blank sheet copy. | Same handling; no independent rule authority. |
| 43 | Investigator sheet | Final blank sheet page. | Same handling; confirms full 43-page review boundary. |

## Information newly required by this repository

### 1. Source capability declaration

Every session must declare both a desired rules profile and the sources actually available. For this PDF alone, the supported profile is `coc7e_quick_start_2016_ja`, not “full current-edition character creation.” A requested capability is one of:

- `verified`: executable from a ledger ID and page;
- `scenario_local`: executable only with `scenario_id`, page, and spoiler-protected context;
- `core_rule_check_required`: blocked until an authorized source is supplied and indexed;
- `keeper_ruling_required`: reversible/local adjudication only, clearly recorded as a ruling;
- `unsupported`: outside the declared session profile.

### 2. Provenance-bearing resolution records

A mechanical resolution needs, at minimum: rules profile, ledger IDs, source page(s), scenario ID when local, pre-state, declared goal, roll candidates, selected roll, thresholds/modifiers, branch selected, state delta, and whether any field requires source confirmation. This is the minimum evidence needed to replay a calculation without exposing scenario text.

### 3. Separate namespaces for rules, examples, and scenario mechanics

The importer must not elevate a worked example, sheet label/base value, scenario stat block, local difficulty, spell, hazard, reward, or handout into the universal rules namespace. Scenario mechanics are usable only inside that scenario; handouts are immutable assets with a separate release record.

### 4. Explicit conflict and uncertainty policy

When a ledger entry, scenario instruction, character-sheet field, and Keeper ruling appear to disagree, do not silently choose. Record the conflict, prefer an explicit scenario-local instruction only within its scenario scope, and stop before an irreversible mechanical effect if authority remains uncertain. Familiarity with another edition or the full rulebook is not evidence.

## Remaining acquisition backlog

| Need | Why the Quick-Start is insufficient | Required action before support |
| --- | --- | --- |
| Complete 7th-edition investigator creation | Quick-Start uses a simplified fixed-array path and omits full age/occupation/economic procedures. | Obtain an authorized current Japanese core-rule source, index exact edition/pages, and add independent fixtures. |
| Complete Sanity/insanity lifecycle | The PDF expressly supplies only a subset. | Source triggers, phases, caps, recovery, and edge cases before enabling irreversible long-term effects. |
| Luck spending | Only Luck rolls/group Luck are present. | Keep spending disabled until sourced. |
| Chases, automatic fire, armor, expanded weapons/combat | Procedures are absent or incomplete. | Mark capability unsupported; add source-specific modules rather than infer. |
| Campaign improvement, downtime, finances, magic | Quick-Start is introductory and scenario-focused. | Defer or source each module independently. |
| General critical/fumble rules and unlisted skill specializations | Only narrow/abbreviated statements occur. | Never generalize the Psychoanalysis fumble statement; source full rules. |

## Completion check

- Every PDF page appears exactly once in the coverage table, either individually or within an explicit content group.
- Pages 21–39 are recognized without copying spoiler content into a public-facing derivative.
- Every executable universal mechanic is routed to a ledger family; every known omission is routed to `RUL-SCOPE-*` and the acquisition backlog.
- The review adds no claim that the Quick-Start provides the complete/current game rules.
