# CodexWriter — Worldbuilding

> **Role:** Creative Core — Phase 2
> **Type:** Generator / Architect
> **Position:** Phase 2 of the 5-phase pipeline. Operates after Gate 1 approval. Extends the world skeleton from the story bible into full worldbuilding artifacts.

---

## Purpose

Worldbuilding transforms the skeletal setting description from the story bible into a rich, internally consistent world that supports the story. It defines locations, rules, cultural context, factions, and artifacts — the stable background against which characters act and scenes unfold.

The goal is not exhaustive world creation. It is creating enough stable world truth that scenes can be written without contradicting established facts.

---

## Inputs

- **Story bible:** The approved concept document, especially the setting skeleton, rules, and cultural context sections.
- **Genre expectations:** Understanding of what the genre requires from its world.
- **Story needs:** Which locations, rules, and cultural details the plot and characters will actually encounter.

---

## Outputs

- `worldbuilding/` directory (or `world/` in the project structure) containing:
  - `overview.md` — expanded world overview
  - `locations.md` or `locations/` — detailed location entries
  - `rules.md` — codified world rules (physical, social, cultural, supernatural, theological)
  - `cultural-context.md` — detailed cultural and historical background
  - (Optional) `factions.md`, `artifacts.md` if the story needs them

- Updates to `story-state.json`:
  - `world.settings[]` populated with location entries
  - `world.rules[]` populated with codified rules
  - `world.cultural_context` expanded
  - `state_revision` incremented

---

## Workflow

### Step 1: Audit the Story Bible

Read the approved story bible. Extract everything already defined about the world:

- Setting overview
- Key locations listed
- Rules and constraints
- Cultural/historical context
- Genre and tone axioms

Identify gaps where the story will need more detail. The audit produces a worldbuilding task list.

### Step 2: Expand the World Overview

Write a richer `overview.md` that captures:

- The feel and atmosphere of the world
- The scope (geographic, temporal, social)
- What makes this world distinctive for this story
- What is ordinary vs. extraordinary in this world

The overview should be vivid but not膨胀 — it is reference material for scene writing, not a travel brochure.

### Step 3: Develop Locations

For each location the story will use, create a detailed entry. At minimum:

- **Name and type** (protagonist_home, foreign_court, wilderness, city, sacred_site, other)
- **Physical description:** What it looks, smells, sounds like
- **Social function:** Who lives there, who rules it, what happens there
- **Relationship to characters:** Who has been there, who will go there
- **Story significance:** Why this location matters to the plot
- **Sensory anchors:** Specific sensory details writers can use

Locations that are only mentioned in passing do not need full entries. Locations where scenes will be written do.

### Step 4: Codify Rules

Define the rules that govern the world. Categorize them:

- **Physical rules:** What is physically possible? What are the constraints of the environment?
- **Social rules:** 계급, kinship, marriage, hospitality, law, honor, taboo
- **Cultural rules:** Customs, rituals, art, religion, language, food, dress
- **Supernatural rules:** If the story has supernatural elements, what can and cannot happen? What are the costs? What are the limits?
- **Theological rules:** If the story has a divine presence, how does it operate? What is known vs. unknown?

Each rule should have:
- A clear statement
- A source or rationale (textual, historical, cultural, or creative choice)
- Whether it is fixed or flexible

Rules are the world's version of continuity. Characters and scenes must operate within them.

### Step 5: Cultural and Historical Context

Flesh out the cultural background that informs character behavior:

- Social structures (family, kinship, hierarchy)
- Economic life (trade, wealth, poverty, survival)
- Religious and spiritual life
- Gender, age, and status dynamics
- Historical events that still resonate
- What characters take for granted vs. what they question

This context should explain *why* characters behave as they do, not just describe their world.

### Step 6: Flesh Out Factions and Artifacts (if needed)

If the story has factions (families, tribes, institutions, rival groups), define:

- Name and nature
- Goals and interests
- Relationships to main characters
- Key conflicts

If the story has significant artifacts (objects, texts, relics), define:

- What they are
- What they do or represent
- Who possesses them
- Their story significance

Skip this step if the story doesn't need factions or artifacts.

### Step 7: Cross-Reference with Characters

Ensure the worldbuilding is consistent with the character dossiers (or character sketches, if character development runs in parallel):

- Do the world's rules allow the characters' actions?
- Do the cultural norms explain the characters' pressures?
- Are the locations characters will visit actually defined?
- Are there world facts characters should know but don't?

If character development hasn't happened yet, note where worldbuilding depends on character decisions and leave placeholders.

### Step 8: Update Story State

Update `story-state.json`:

- Populate `world.settings[]` with location entries (location_id, name, type, status)
- Populate `world.rules[]` with codified rules (rule_id, category, statement, source)
- Expand `world.cultural_context`
- Increment `state_revision`
- Set `updated_at`

### Step 9: Author Review

Present the worldbuilding to the author. Highlight:

- What was expanded from the story bible
- What new rules and locations were created
- Any places where worldbuilding depends on character or plot decisions
- Any open questions about the world

The author approves, requests revisions, or rejects.

---

## Error Handling

| Error | Response |
|---|---|
| Story bible not approved | "Worldbuilding requires Gate 1 approval of the story bible. The concept is not yet locked." |
| Inconsistent with character dossiers | "This world detail conflicts with [character]'s dossier: [specific conflict]. Either the world detail or the character detail needs revision. Which do you want to adjust?" |
| Rule contradicts story need | "The story needs [X] to happen, but rule [Y] would prevent it. Options: 1) Revise the rule, 2) Find a way within the rule, 3) Flag this as a creative tension to resolve in narrative architecture." |
| Overdevelopment | "This location/rules/cultural detail is rich, but the story doesn't yet need it. I'm marking it as optional. We can develop it later if the story requires it." |

---

## Portability

- All outputs are Markdown — universally readable.
- No platform-specific tools.
- The worldbuilding artifacts are designed to be referenced by later phases (narrative architecture, scene writing) regardless of which AI host runs those phases.
- Rules are codified in a structured way that makes them machine-checkable by the continuity skill.

---

## Integration with Character Development

Worldbuilding and character development are both Phase 2 and can run in parallel or sequence. The key integration points:

- **Pressure systems:** A character's pressure system often arises from their position in the world (status, kinship, gender, culture). Worldbuilding should provide the context that makes character pressures plausible.
- **Rules as constraints:** Characters operate within world rules. Their choices, conflicts, and dilemmas should be shaped by the world's social and physical constraints.
- **Locations as scene settings:** Every location a character visits should be defined before scene writing begins.

If worldbuilding runs first, it provides the stage for character development. If character development runs first, it defines what the world needs to contain. Either order works — the orchestrator should ensure they cross-reference before Gate 2.

---

## Sources and Provenance

This skill draws on patterns from:

- **Lensetek/Fiction-book-agent-skills:** `worldbuilding-architect` — the concept of a dedicated worldbuilding specialist that produces a worldbuilding codex.
- **danjdewhurst/story-skills:** Worldbuilding as one of the 7 core skills, with location/system/faction/artifact sharding.
- **JeroTan/novel-writer-english:** Knowledge files for detailed world/character/location information, separated from the lean specification.

CodexWriter's approach is an independent synthesis: worldbuilding is a Phase 2 skill that produces structured Markdown artifacts and updates machine-readable state, with rules codified for continuity checking.

---

## File Outputs

- `worldbuilding/overview.md` — expanded world overview
- `worldbuilding/locations.md` or `worldbuilding/locations/` — location entries
- `worldbuilding/rules.md` — codified world rules
- `worldbuilding/cultural-context.md` — detailed cultural background
- (Optional) `worldbuilding/factions.md`, `worldbuilding/artifacts.md`
- Updated `story-state.json`

---

## Evaluation

A worldbuilding implementation is successful when:

1. It produces location entries for every place where scenes will be written.
2. Rules are specific enough that continuity checking can verify them.
3. Cultural context explains character behavior without dictating it.
4. The worldbuilding does not膨胀 beyond what the story needs.
5. A different AI host could read the worldbuilding artifacts and write a scene set in this world without contradicting established facts.
