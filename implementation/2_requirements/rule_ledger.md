# Quick-Start Rule Ledger

## Source identity and use boundary

| Field | Verified value | PDF pages |
| --- | --- | --- |
| Source | `NewCoC-QS_200228.pdf`, **新クトゥルフ神話TRPG クイックスタート・ルール** | 1–3 |
| Edition | Call of Cthulhu **7th Edition** Quick-Start; the copyright line identifies Chaosium publication 23131 and ©2016 | 2–3 |
| Japanese edition | Japanese translation credited to Yukihiro Terada / Arkham Members (with Masayuki Sakamoto); the text directs readers to KADOKAWA's *新クトゥルフ神話TRPG ルールブック* for complete rules | 2, 4 |
| File extent checked | All 43 PDF pages: cover (1), credits/contents/introduction (2–6), investigator creation and rules (7–20), Keeper scenario **The Haunting / 悪霊の家** (21–39), investigator sheets (40–43) | 1–43 |
| Intended scope | Enough information to create a Quick-Start investigator and play the included introductory scenario; it is explicitly not the complete rules | 4, 16 |

This ledger is a procedural index, not a replacement for the book. It deliberately avoids reproducing prose, tables, scenario handouts, or the insanity table in full.

## Explicitly absent or incomplete

| Ledger ID | Finding | Status | PDF pages |
| --- | --- | --- | --- |
| RUL-SCOPE-01 | Complete Sanity rules are expressly not included. Longer-term consequences and complete recovery therefore require the core rulebook. | **Core-rule confirmation required** | 16 |
| RUL-SCOPE-02 | Income/assets are left unused by Quick-Start creation and described as campaign material. | **Outside Quick-Start** | 10 |
| RUL-SCOPE-03 | The PDF does not provide complete chase, automatic-fire, armor, spending Luck, age, occupation point formulas, credit-rating ranges by occupation, development phase, magic, downtime, or campaign rules. | **Outside Quick-Start / core-rule confirmation required** | 4, 7–20 |
| RUL-SCOPE-04 | The skill descriptions are abbreviated. Unstated specializations, edge cases, and full skill rules must not be inferred. | **Core-rule confirmation required** | 11–14 |
| RUL-SCOPE-05 | Fumble thresholds are stated for Psychoanalysis (96–100 below 50%; 100 at 50%+) but a general fumble/critical rule is not presented as a complete core-resolution rule. | **Do not generalize without core rules** | 13 |

## Investigator creation, characteristics, derived values, and skills

| Ledger ID | Procedure / formula / branch | PDF pages |
| --- | --- | --- |
| RUL-CHR-01 | Assign `40, 50, 50, 50, 60, 60, 70, 80` once each among STR, CON, SIZ, DEX, APP, INT, POW, EDU. | 7 |
| RUL-CHR-02 | For every characteristic and recorded skill: `half = floor(full / 2)`; `fifth = floor(full / 5)`. | 7, 10 |
| RUL-DRV-01 | `max_hp = floor((CON + SIZ) / 10)`; human MOV is 8; initial SAN equals POW; MP equals `floor(POW / 5)` and normally recovers 1/hour. Spending beyond zero MP reduces HP. | 8 |
| RUL-DRV-02 | Luck is `5 × 3D6`. A Luck roll succeeds on `D100 <= current Luck`. | 8, 15 |
| RUL-DRV-03 | Damage bonus/build from STR+SIZ: 2–64 → −2/−2; 65–84 → −1/−1; 85–124 → +0/0; 125–164 → +1D4/1; 165–204 → +1D6/2. Values beyond this Quick-Start table require core-rule confirmation. | 9 |
| RUL-SKL-01 | Choose a listed occupation or agree a custom occupation with the Keeper and select eight fitting occupation skills. Allocate fixed final values across those eight plus Credit Rating: one 70, two 60, three 50, and three 40; ignore printed bases for these allocations. Cthulhu Mythos cannot receive creation points. | 9–10 |
| RUL-SKL-02 | Choose four skills outside the occupation skills and add 20 percentage points to each printed base. Then record a concise backstory (2–3 entries suffice), identity, age/sex, and plausible occupational equipment. | 10 |
| RUL-SKL-03 | The PDF supplies sample occupations and abbreviated skill meanings/bases on the sheet. Medicine after the injury day requires Hard success; First Aid must be within one hour and restores 1 HP; Medicine takes at least one hour and restores 1D3, subject to dying-character sequencing. | 9, 11–14, 19 |
| RUL-SKL-04 | A successful dramatic skill roll marks that skill once. At scenario/session end, roll D100 per marked skill; only `roll > current skill` increases it by 1D10, then clear the mark. | 10, 19–20 |

## Core resolution

| Ledger ID | Procedure / branch | PDF pages |
| --- | --- | --- |
| RUL-RES-01 | Roll only when an outcome is dramatic/uncertain and agree the player's goal first. Use the most appropriate characteristic as a percentage value when no listed skill fits. | 10, 14 |
| RUL-RES-02 | Regular succeeds when `D100 <= full`; Hard when `D100 <= floor(full/2)`; Extreme when `D100 <= floor(full/5)`. Threshold equality succeeds. | 7, 14 |
| RUL-RES-03 | D100 uses ones plus tens; `00 + 0 = 100`, while `00 + nonzero ones = 1–9`. | 6 |
| RUL-MOD-01 | One bonus and one penalty die cancel. Each added tens die creates another candidate with the same ones die; bonus chooses the lowest candidate, penalty the highest. Difficulty and modifier dice may be used as alternatives or together, at Keeper discretion. | 14–15 |
| RUL-PSH-01 | After failure, a player may propose a materially justified changed/reinforced approach. If Keeper permits, reroll once; a second failure causes a serious adverse consequence. Keeper may disclose that consequence before commitment. | 14 |
| RUL-PSH-02 | Combat rolls cannot be pushed. The PDF does not enumerate every other prohibited push; scenario-specific impossibility/failure consequences control, otherwise core-rule confirmation is required. | 16, 21–39 |
| RUL-OPP-01 | Both sides roll and compare success level: Extreme > Hard > Regular > failure. If tied, higher underlying skill wins; if skills also tie, both roll D100 and the lower result wins. | 14 |
| RUL-LCK-01 | Use Luck for external chance/fate only when a skill/characteristic is not more suitable. Group Luck uses the present investigator with the lowest Luck. No Luck-spending rule appears. | 15 |

## Combat and damage

| Ledger ID | Procedure / branch | PDF pages |
| --- | --- | --- |
| RUL-CMB-01 | Order participants by descending DEX. A round is long enough for each participant to take one meaningful action; Keeper manages narrative timing. A readied firearm acts at `DEX + 50` for ordering. Tie handling is not stated. | 16, 18 |
| RUL-CMB-02 | Melee attack versus fight back: attacker wins ties; defender must obtain a strictly better success level to fight back and deal normal damage. Attack versus dodge: defender wins ties; attacker must obtain a strictly better level to deal damage. | 17–18 |
| RUL-CMB-03 | Extreme damage by the initiating attacker: blunt = maximum weapon damage + maximum DB; impaling = maximum weapon damage + maximum DB + one normal weapon-damage roll. Fight-back damage remains regular even on Extreme. | 17–18 |
| RUL-CMB-04 | Firearms use Firearms skill. Two or three handgun shots in a round apply one penalty die to every shot. Point blank (`<= DEX × 0.06` metres) gives one bonus die. A target cannot fight back or dodge a bullet, but may dive for cover: successful Dodge imposes one penalty die on shooter and the diver forfeits the next attack whether the dive succeeds or fails. | 18 |
| RUL-CMB-05 | Maneuvers resolve like Fighting (Brawl), with dodge/fight-back. If attacker build is smaller, apply one penalty die per build difference, maximum two; if defender is 3+ build larger, maneuver has no effect. After a character has dodged/fought back once in a round, later melee attackers against that character gain one bonus die; firearms are excluded. | 18–19 |
| RUL-DMG-01 | On a damaging hit, roll the stated weapon formula and add DB only where stated. The Quick-Start list covers unarmed, small knife, machete, small club, bat, handgun, shotgun at two ranges, and rifle; weapons/armor not listed require a source. | 17 |
| RUL-DMG-02 | Subtract damage from HP, minimum 0. One hit `>= max_hp / 2` causes a major wound and a CON roll; failure causes unconsciousness. One hit `> max_hp` causes immediate death. Note the distinct inclusive/exclusive comparisons. | 19 |
| RUL-INJ-01 | At 0 HP without a major wound: unconscious but not dying. At 0 HP with a major wound: dying; make CON at end of next and every later round, and any failure means death. Successful First Aid alone stabilizes dying. | 19 |
| RUL-HEAL-01 | No major wound: natural healing 1 HP/day. Major wound: weekly CON; success restores 1D3, Extreme restores 2D3. Remove major wound on an Extreme healing roll or when current HP reaches at least half maximum. | 19 |
| RUL-HEAL-02 | First Aid restores 1 HP and can awaken unconscious; on dying it only extends life until Medicine. Medicine needs at least one hour/tools, restores 1D3, and after use on a dying patient permits a healing roll one week later. The page-11 timing/difficulty rule also applies. | 11, 19 |
| RUL-DMG-03 | The other-damage table supplies severity bands from 1D3 through 8D10 plus contextual examples. Suffocation/drowning uses CON each round; after first failure damage repeats until breathing/death, and 0 HP kills while ignoring major-wound rules. Extreme CON halves poison damage. | 19–20 |

## Sanity and insanity

| Ledger ID | Procedure / branch | PDF pages |
| --- | --- | --- |
| RUL-SAN-01 | Roll D100 against current SAN. Apply the loss before `/` on success (`roll <= SAN`) and after `/` on failure (`roll > SAN`), rolling any loss dice. On failure, Keeper may briefly control the next involuntary reaction. | 16 |
| RUL-SAN-02 | If a single SAN roll loses 5+, make an INT roll. `D100 <= INT` means the investigator understands and enters temporary insanity for 1D10 hours. The Quick-Start does not state a result beyond “no temporary insanity” for INT failure; do not infer more. | 16 |
| RUL-INS-01 | During temporary insanity, Keeper selects or rolls a bout from the ten-entry table; a bout lasts 1D10 rounds. Keeper may add a phobia/mania or alter one backstory entry. Phobia/mania bouts impose one penalty die on all actions for their duration. | 16–17 |
| RUL-INS-02 | Keeper may present delusions during temporary insanity. Investigator may voluntarily request a Reality Check using SAN: success pierces the hallucination; failure deepens insanity, with the exact added effect requiring the complete rules/Keeper source. After 1D10 hours delusions cease but acquired backstory/phobia/mania remains. | 16 |
| RUL-SAN-03 | Psychoanalysis can restore 1D3 SAN once per in-game month on success; its stated fumble loses 1D6 SAN and ends treatment by that analyst. Indefinite insanity needs 1D6 months in an institution/equivalent and is explicitly not accelerated by Psychoanalysis. Complete SAN recovery/caps and indefinite-insanity triggers are outside this PDF. | 13, 16 |

## Keeper operation and scenario-specific information

| Ledger ID | Classification | PDF pages |
| --- | --- | --- |
| RUL-KPR-01 | Keeper presents situations, plays NPCs/monsters, decides possibility and when/which roll is needed, sets difficulty/modifiers, resolves consequences, and then asks what players do. The game is cooperative; Keeper-controlled opposition should be fair. | 4–6, 10, 14–16 |
| RUL-KPR-02 | Rolls should serve uncertainty rather than routine actions. Consequences and pushed-roll stakes should preserve meaningful choice. Hidden Psychology rolls are expressly permitted, with only resulting information reported. | 10, 12, 14 |
| RUL-SCN-01 | **Spoiler-bearing Keeper material:** “The Haunting / 悪霊の家” occupies pp.21–39. Pages 21–22 cover Keeper setup/background/opening; 23–26 research locations and handouts; 27–32 the primary location, hazards, antagonist statistics/tactics and conclusions/rewards; 33–39 player handouts. Treat all as scenario data, not universal rules. | 21–39 |
| RUL-SCN-02 | Scenario text gives local skill difficulties, automatic clue delivery, pushed-roll consequences, SAN losses, attacks/spells, and rewards. These override generic assumptions only inside this scenario and must carry page + scenario ID in a resolution record. | 21–32 |
| RUL-SCN-03 | Blank investigator sheet front/back and duplicates occupy pp.40–43. They evidence fields/base skills but add no prose rule beyond the creation chapter. | 40–43 |

## Traceability convention

Every implementation rule reference uses one or more IDs above plus PDF page(s), for example `rules: [RUL-RES-02]`, `source: NewCoC-QS_200228.pdf#page=14`. “Not stated” must map to `RUL-SCOPE-*` or an explicit `core_rule_check_required` flag; it must never be silently completed from memory.

## Implementation trace matrix

| Rule families | Requirements | Acceptance fixtures | Risks | Source pages |
| --- | --- | --- | --- | --- |
| RUL-CHR / RUL-DRV / RUL-SKL | FR-RUL-01 | AC-RUL-04, AC-RUL-10, AC-RUL-13 | R-15, R-16, R-17, R-20 | 7–14, 19–20, 40–43 |
| RUL-RES / RUL-MOD / RUL-OPP / RUL-LCK | FR-RUL-02 | AC-RUL-04, AC-RUL-05, AC-RUL-07 | R-15, R-17, R-18 | 6, 14–15 |
| RUL-PSH / RUL-SCOPE | FR-RUL-03 | AC-RUL-06, AC-RUL-12 | R-16, R-20 | 4, 13–16 |
| All ledger families / source invariant | FR-RUL-04 | AC-RUL-04..13 | R-15, R-16, R-20 | 1–43 |
| RUL-CMB / RUL-DMG | FR-RUL-05 | AC-RUL-08, AC-RUL-09 | R-17, R-18 | 16–20 |
| RUL-INJ / RUL-HEAL | FR-RUL-06 | AC-RUL-09, AC-RUL-10 | R-17, R-18 | 11, 19 |
| RUL-SAN / RUL-INS | FR-RUL-07 | AC-RUL-11, AC-RUL-12 | R-16, R-18, R-20 | 13, 16–17 |
| RUL-KPR / RUL-SCN | FR-RUL-08 | AC-RUL-13 | R-19, R-20 | 4–6, 10, 12, 14–16, 21–43 |

Legacy acceptance links remain valid: AC-RUL-01 exercises FR-RUL-01 with RUL-CHR/DRV/SKL (pp.7–10); AC-RUL-02 exercises FR-RUL-02..03 with the complete ledger/source record (pp.6–20); AC-RUL-03 exercises FR-RUL-04's `OUTPUT_AGENTS.md` reproducibility constraint (pp.1–43 source boundary). Their primary risks are R-04, R-11, R-15, R-16, and R-20.
