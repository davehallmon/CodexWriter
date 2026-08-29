# CodexWriter — Continuity

> **Role:** Evaluation / Revision — Phase 4 and Phase 5
> **Type:** Validator / Auditor
> **Position:** Operational in Phase 4 (after drafting) and Phase 5 (after revision). Can run in any phase — it is phase-agnostic. Checks the manuscript against the stored state for contradictions, knowledge violations, timeline errors, and promise/payoff issues.

---

## Purpose

Continuity is the system's memory. It checks whether the drafted manuscript is consistent with the stored state — character states, knowledge, timeline, promises, and world rules. It does not judge prose quality, emotional impact, or artistic merit. It checks mechanical consistency.

The continuity skill has two jobs:

1. **Validation:** Run checks against schemas, state, and the manuscript, producing a structured report of findings.
2. **State maintenance:** Update continuity-state.json with the results of each check, creating a check history log.

---

## Inputs

- **Story state:** `story-state.json` — canonical machine-readable state.
- **Character states:** `characters/[character_id]/current-state.json` — dynamic character state for each character.
- **Scene states:** `scenes/[scene_id]/scene-state.json` — scene-level state including beats, knowledge changes, continuity notes.
- **Manuscript:** The drafted scenes and chapters.
- **Schemas:** `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, `schemas/continuity.schema.json`.
- **World rules:** From worldbuilding — codified rules that should be checked.
- **Continuity schema:** `schemas/continuity.schema.json`.

---

## Outputs

- `continuity-state.json` — the continuity tracking state, updated after each check.
- **Continuity report:** A structured document (Markdown or JSON) presenting findings organized by category and severity.

---

## Workflow

### Step 1: Load All State

Load:
- `story-state.json`
- All `character-state.json` files
- All `scene-state.json` files
- The relevant manuscript scenes
- The schemas for validation

### Step 2: Run Schema Validation

Validate `story-state.json`, all character states, and all scene states against their schemas. Flag any violations:

- Missing required fields
- Type mismatches
- Pattern violations (e.g., character_id format)
- Enum violations
- Range violations

Schema violations are mechanical — they should be fixed before deeper continuity checks.

### Step 3: Run Character Consistency Checks

For each character, check:

- **Voice consistency:** Does the character's dialogue and interiority in the manuscript match their voice rules in the dossier?
- **Physical state consistency:** Does the character's physical state in the manuscript match their current state? (injured, tired, carrying objects)
- **Knowledge consistency:** Does the character know what their state says they know? Do they react to things they don't know about? Are things they should know by a certain point actually known?
- **Emotional continuity:** Does the character's emotional state progress reasonably? Are there abrupt shifts without cause?
- **Relationship consistency:** Are the character's relationships with other characters consistent with what's been established?
- **Pressure system consistency:** Does the character's behavior reflect their pressure system? Are there moments where they act against their pressure without cause?

### Step 4: Run Timeline Consistency Checks

Check the timeline:

- **Ordering:** Do events in the manuscript occur in the correct chronological order?
- **Gaps:** Are there unexplained gaps in the timeline?
- **Overlaps:** Do scenes overlap in time in ways that don't make sense?
- **Causal:** Are cause-and-effect relationships preserved? Does effect come after cause?

### Step 5: Run Knowledge Consistency Checks

This is the most critical check for POV integrity:

- **Knows before should:** Does a character know something before they should?
- **Doesn't know should:** Does a character fail to know something they should know by this point?
- **Revealed early:** Is information revealed to the reader (or a character) before it should be?
- **Hidden too long:** Is information withheld past the point where the character should know it?

Knowledge violations are particularly damaging because they break the reader's trust in the POV.

### Step 6: Run Promise Consistency Checks

Check the promise/payoff structure:

- **Setup without payoff:** Is a promise set up that never pays off?
- **Payoff without setup:** Does a payoff arrive without being set up?
- **Payoff too early:** Does a payoff arrive before the setup is complete?
- **Payoff too late:** Does a payoff arrive so late that the setup has been forgotten?
- **Payoff subverted intentionally:** Is a payoff deliberately subverted? (This is allowed if intentional and flagged.)

### Step 7: Compile Findings

Organize all findings by category and severity:

- **Character consistency findings**
- **Timeline consistency findings**
- **Knowledge consistency findings**
- **Promise consistency findings**
- **Schema validation findings**

Each finding includes:
- Check ID
- Character or element involved
- Check type
- Status (passed, flagged, contradiction)
- Finding description
- Severity (info, low, medium, high, critical)

### Step 8: Update Continuity State

Update `continuity-state.json`:

- `continuity_revision` → incremented
- `last_check_at` → set
- `last_check_by` → "continuity skill"
- `character_consistency[]` → populate with check results
- `timeline_consistency[]` → populate with check results
- `knowledge_consistency[]` → populate with check results
- `promise_consistency[]` → populate with check results
- `open_contradictions[]` → move any unresolved contradictions here
- `check_history[]` → add an entry for this check

### Step 9: Produce Continuity Report

Produce a continuity report for the author. The report should be:

- **Organized by severity:** Critical and high findings first.
- **Specific:** Each finding should say what the problem is, where it is, and what the state says should be true.
- **Actionable:** Each finding should suggest what needs to happen (revise the manuscript, revise the state, or accept as intentional).
- **Distinguishing mechanical from judgment:** Continuity reports mechanical consistency. It does not say "this scene is boring" or "this character's choice is unsatisfying." Those are prose-editing and reader-simulation concerns.

### Step 10: Report to Orchestrator

Report completion to the orchestrator with:

- Continuity revision number
- Findings count by severity
- Open contradictions count
- Whether the manuscript passed or failed continuity
- Any critical findings that block progression

---

## Severity Levels

| Severity | Meaning | Action |
|---|---|---|
| **Critical** | The manuscript contradicts established state in a way that breaks the story's internal logic or POV integrity. Cannot proceed without resolution. | Must be fixed before the manuscript advances. |
| **High** | A significant inconsistency that will be noticed by a careful reader and damages credibility. | Should be fixed before the manuscript advances. |
| **Medium** | A noticeable inconsistency that doesn't break the story but creates a small credibility gap. | Should be addressed, but may be acceptable if the author chooses to leave it. |
| **Low** | A minor inconsistency or a potential issue that may not matter in context. | Note for awareness; author can decide. |
| **Info** | An observation, not a problem. A note about something that's consistent or a potential future concern. | No action required. |

---

## Error Handling

| Error | Response |
|---|---|
| State files missing | "Continuity checking requires story-state.json and character/scene state files. Some state is missing. I can check what's available, but I cannot run a full continuity check without the state." |
| Manuscript not drafted | "There is no manuscript to check. Continuity requires drafted scenes. Run scene writing first." |
| Schema validation fails | "State files fail schema validation. These mechanical errors must be fixed before continuity checks can be meaningful. Here are the schema violations: [list]." |
| Ambiguous finding | "This finding is ambiguous — the state says [X] but the manuscript shows [Y]. It's not clear whether this is a contradiction, an intentional update, or a state error. I'm flagging it for author resolution." |
| No contradictions found | "The continuity check ran [N] checks and found [M] findings, all of which are [severity level] or below. No critical or high findings. The manuscript is consistent with the stored state." |

---

## Portability

- All inputs and outputs are JSON and Markdown — universally readable.
- The check categories (character, timeline, knowledge, promise) are described as patterns, not software tools.
- Any AI host can read the state files and manuscript and run the checks.
- The continuity report structure is defined by the continuity schema, making it machine-readable.

---

## Distinguishing Mechanical from Judgment

Continuity checks are mechanical. They check whether the manuscript matches the state. They do not judge:

- **Prose quality:** Is the writing good? (prose-editing's job)
- **Emotional impact:** Does the scene land? (reader-simulation's job)
- **Character motivation quality:** Is the character's choice interesting? (prose-editing and reader-simulation)
- **Pacing quality:** Is the scene too long or too short? (prose-editing)
- **Voice fidelity:** Does the prose sound like the character? (This is a gray area — voice consistency is a continuity concern, but voice quality is a prose concern.)

The continuity report should be clear about which findings are mechanical contradictions and which are observations that may warrant attention but are not mechanical failures.

---

## Integration with Other Skills

- **Scene writing** produces the draft and records continuity notes. Continuity uses those notes as input.
- **Prose editing** uses the continuity report as input for revision priorities.
- **Reader simulation** runs after continuity is clean — the reader should not be distracted by continuity errors.
- **The orchestrator** uses continuity results to decide whether the manuscript can advance to the next phase.

---

## File Outputs

- `continuity-state.json` — updated continuity tracking state.
- `continuity-report.md` or `continuity-report.json` — the findings report.

---

## Evaluation

A continuity implementation is successful when:

1. It catches mechanical contradictions between the manuscript and the state.
2. It distinguishes critical/high findings from low/info observations.
3. It produces a report that is specific and actionable.
4. It updates continuity-state.json correctly, creating a check history.
5. It can run in any phase and produce useful results.
6. A different AI host could read the state, manuscript, and schemas, and produce a comparable continuity report.
