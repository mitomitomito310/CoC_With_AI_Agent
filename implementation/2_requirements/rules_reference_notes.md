# Quick-Start Rules Review

## Review Status

- Source: `NewCoC-QS_200228.pdf`
- Reviewed: 2026-07-25
- Coverage: 43 / 43 PDF pages
- Use: requirements evidence and implementation reference index; this file is not a replacement for the rulebook
- Copyright handling: rules are summarized as behaviors and data needs. Scenario prose, handouts, maps, tables, and character sheets are not reproduced.

## Source Boundary

The PDF identifies itself as an introductory quick-start for the Japanese seventh-edition game. It is sufficient to specify the first playable rules slice, but it explicitly omits parts of the complete rules (the sanity section says that the complete sanity rules are not included). Therefore:

1. `quick_start_7e` is a distinct rules profile, not an alias for `full_7e` or for an unspecified "latest" profile.
2. A mechanic is executable only when its source profile and page/range have been recorded.
3. Missing full-rule details must be reported as `unsupported_by_active_source`; they must not be completed from memory.
4. The supplied PDF may be read locally for this project, but derivative repository files should contain compact rules facts and locators rather than copied prose.

## Page-by-Page Coverage Ledger

| PDF pages | Reviewed content | Repository consequence |
| --- | --- | --- |
| 1 | Cover | No mechanical data. |
| 2 | Credits and publication information | Preserve the local source identity; do not infer edition from filename alone. |
| 3 | Introduction and contents | Establishes the quick-start scope and page map. |
| 4–6 | Roles, play loop, cooperation, scenario/campaign framing, dice notation and percentile dice | Keeper controls presentation and adjudication; store dice expressions and raw percentile components. |
| 7 | Character creation: eight characteristics, fixed quick-start array, half/fifth values | Character schema needs full, half, and fifth thresholds with floor rounding and a creation-profile field. |
| 8 | Derived attributes: damage bonus/build, HP, MOV, SAN, MP, Luck | Derived values need formulas, current/max separation, and provenance. MP recovery is time based. |
| 9 | Occupations, occupation skills, Credit Rating, damage bonus/build table | Occupation selection and Keeper approval precede skill allocation; Cthulhu Mythos is normally unavailable at creation. |
| 10 | Skill allocation, personal-interest skills, backstory, finishing details | Creation is staged and resumable; backstory and possessions are first-class character data. |
| 11–13 | Skill meanings, base chances, specializations, opposed skills, time/tool constraints | Skill definitions need specialization, base value, duration, prerequisites, opposing skill, and permissible consequence metadata. Hidden Keeper rolls are required for some information checks. |
| 14 | characteristic rolls, regular/hard/extreme difficulty, pushed rolls, opposed rolls, bonus/penalty dice | Roll records need thresholds, success level, push eligibility/attempt, announced stakes, opponent, and modifier sources. |
| 15 | bonus/penalty percentile procedure and Luck/group Luck | Preserve every tens die and the selected result. Group Luck uses the eligible participant with the lowest Luck. |
| 16 | SAN loss notation, temporary insanity trigger, combat order and combat-roll restrictions | SAN check and loss are separate operations. Combat is DEX ordered and combat rolls cannot be pushed. |
| 17 | bout-of-madness outcomes, melee response and common damage | Keeper may select or roll an episode; melee defense must distinguish dodge from fight back. |
| 18 | tie behavior, extreme damage, firearms, diving for cover, combat maneuvers | Resolution depends on attacker/defender role, weapon category, readiness, range, action forfeiture, and build difference. |
| 19 | outnumbered, HP/major wound/dying/death, first aid, medicine, healing, other damage | Persist per-hit damage, major-wound flag, consciousness, dying/stable state, treatment timing, and recovery schedule. |
| 20 | development checks and environmental damage continuation | Mark successful skill use, resolve improvement at session/scenario end, then clear the mark; some hazards repeat per round. |
| 21 | Scenario instructions and presentation conventions | Scenario ingestion must classify read-aloud/public text separately from Keeper advice and mechanical triggers. |
| 22–25 | Investigation flow, optional scene order, research, handouts, failed/pushed information rolls, social reactions | Scene graph must allow non-linear traversal; clue delivery records prerequisites, roll outcome, time, and public handout state. Failure must not silently dead-end play. |
| 26–35 | Location exploration, hazards, opposed checks, spells, antagonist tactics/statistics, ending guidance | Scenario index needs locations, sensory text, hidden facts, triggers, hazards, actors, tactics, spells, rewards, and end conditions without publishing them. |
| 36–39 | Extended example of play | Confirms the conversational loop: describe, declare, decide whether to roll, expose observable result, and continue; examples are guidance, not canonical state. |
| 40–41 | Blank investigator sheet, front/back | Character schema must cover characteristics, derived/current tracks, skills, combat, personal history, contacts, possessions, finances, injuries, phobias/manias, tomes/spells, and encounters. |
| 42–43 | Duplicate blank investigator sheet, front/back | No additional mechanics; confirms a two-sided reusable sheet layout. |

## Minimum Rules Facts to Structure

### Roll record

Every adjudicated roll should be able to retain: rules profile, source locator, roll kind, actor, target skill/characteristic/current track, full/half/fifth thresholds, difficulty, raw dice, selected D100 result, bonus/penalty count and reason, success level, opposed party and tie rule, push eligibility, push stakes, result, and resulting state delta.

### Character state

Separate stable facts from changing tracks. Stable facts include characteristics, skill values and specializations, occupation, backstory, damage bonus, build, and maximum HP. Mutable facts include HP, SAN, MP, Luck, major wound, consciousness, dying/stable state, conditions, phobias/manias, possessions, development marks, and time-based recovery.

### Scenario index

The included scenario demonstrates that a flat clue list is insufficient. The Keeper index needs typed entries for scenes/locations, public description, read-aloud text, Keeper-only truth, clue, handout, prerequisite, roll, failure/push consequence, elapsed time, actor reaction, hazard, combat/spell, transition, and ending/reward. Each entry must retain a source locator and disclosure state.

## Gaps Requiring Another Authorized Source

- The quick-start does not contain the complete sanity system.
- It provides a streamlined creation method, not evidence that every full-rule character-creation option is covered.
- It cannot establish every chase, magic, downtime, equipment, credit, combat, or campaign rule needed by arbitrary imported scenarios.
- Rules absent from this PDF require another user-available, authorized source before `full_7e` can be claimed.

These gaps do not block a quick-start fixture. They do block the current broad promise of a fully sourced, arbitrary "latest/full" session unless an additional source is registered.
