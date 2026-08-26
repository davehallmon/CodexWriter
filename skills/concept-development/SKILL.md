# CodexWriter — Concept Development

> **Role:** Creative Core — Phase 1
> **Type:** Generator / Planning
> **Position:** Phase 1 of the 5-phase pipeline. Creates the story bible and establishes the creative contract.

---

## Purpose

Concept development transforms a vague story idea into a structured, author-approved story bible. It is the foundation everything else builds on. The output is not prose — it is the creative contract that defines what the story is, who is in it, and what rules govern it.

---

## Inputs

- **Initial idea:** A title, logline, or rough concept from the author.
- **Existing notes:** Any pre-existing brainstorming, research, or inspiration material.
- **Genre conventions:** Understanding of the target genre's expectations and boundaries.

---

## Outputs

- `story-state.json` — initialized with project metadata, phase set to `concept`, state_revision = 1.
- `story-bible.md` — the canonical story bible using `templates/story-bible-template.md`.
- (Optional) Initial character list, setting catalog, and plot arc summaries.

---

## Workflow

### Step 1: Intake

The skill receives the author's concept and asks clarifying questions if the idea is too vague to proceed. Minimum viable input: a working title and a one-sentence description of what the story is about.

If the author provides more (genre, tone, inspiration, existing notes), incorporate it.

### Step 2: Concept Exploration

Using the author's input, develop:

- **Logline:** A one or two sentence summary that captures the story's core conflict.
- **Central dramatic question:** What is the story actually asking?
- **Theme:** What is the story about beneath the plot?
- **Tone axioms:** Rules that define the story's tone and must not be violated.
- **Style profile:** Authorial voice reference (e.g., Stephen King / Literary Horror, literary fiction, noir, etc.).

### Step 3: Setting Skeleton

Define:

- **World overview:** One paragraph describing the story's world.
- **Key locations:** List of important places with brief descriptions.
- **Rules and constraints:** Physical, social, cultural, and supernatural rules.
- **Cultural/historical context:** Relevant background.

Do not over-develop the world at this stage — capture what the story needs, not everything that could exist.

### Step 4: Character List

Identify the main characters and create a brief entry for each:

- Name
- Role label (e.g., protagonist, antagonist, mentor, foil)
- Dramatic function (what they do in the story)
- One-paragraph summary
- Key relationships

Characters at this stage are sketches, not full dossiers. Full dossiers come in Phase 2.

### Step 5: Plot Architecture (Preliminary)

Develop:

- **Arc summary:** One paragraph describing the overall plot.
- **Major arcs:** List of main plot arcs, subplots, character arcs, thematic arcs.
- **Key beats:** Major plot beats in order (10-20 beats maximum at this stage).

This is a rough architecture, not a scene-by-scene breakdown. That comes in Phase 3.

### Step 6: Timeline (Preliminary)

Create a chronological event list:

- Canonical events in order
- Textual status (direct, inferred, silence, contradicted)

Keep it high-level. Detailed timeline comes later.

### Step 7: Open Questions

Identify questions that need author decisions before the story bible can be finalized:

- Unclear character motivations
- Unresolved plot choices
- Setting details not yet decided
- Tone or style questions

Each question gets an ID, the question text, origin phase, and status (`open`).

### Step 8: Story Bible Assembly

Compile everything into `story-bible.md` using the template. Ensure:

- Every section is populated or marked as "to be developed."
- Source lineage is noted for any material drawn from research or inspiration.
- Open questions are listed clearly.
- Tone axioms are explicit and memorable.

### Step 9: Author Review

Present the story bible to the author. Highlight:

- What is solid.
- What is provisional.
- What open questions remain.
- What needs author decisions.

The author approves, requests revisions, or rejects.

### Step 10: Gate 1 Approval

On author approval:

- Set `phase` → `worldbuilding` in story-state.json.
- Set `phase_gate` → `approved`.
- Increment `state_revision`.
- Set `updated_at`.
- Report completion to the orchestrator.

---

## Error Handling

| Error | Response |
|---|---|
| Idea too vague | "I can work with this, but I need at least a working title and a sense of what the story is about. Here are some questions that would help: [list]." |
| Conflicting input | "I notice [conflict]. Here are two ways to resolve it: [option A] or [option B]. Which fits your vision better?" |
| Author rejects | "Understood. What would you like to change? I can revise specific sections or start over with different assumptions." |
| Author stalls on a question | "This question is blocking finalization. You can: 1) Make a provisional decision and revisit later, 2) Mark it as deferred and proceed, or 3) Sit with it and come back." |

---

## Portability

- All outputs are Markdown and JSON — universally readable.
- No platform-specific tools or commands.
- The skill can be executed by any AI host that can read the templates, follow the workflow, and write Markdown/JSON files.
- The story bible template is designed to be genre-agnostic — it works for literary fiction, genre fiction, historical fiction, speculative fiction, etc.

---

## File Outputs

- `story-state.json` — project state, initialized.
- `story-bible.md` — canonical story bible.
- Updates to `characters/` directory if any initial character sketches are written.

---

## Evaluation

A concept-development implementation is successful when:

1. It can take a one-sentence idea and produce a complete story bible.
2. It asks clarifying questions when the input is too vague, rather than guessing.
3. It produces a story bible that a different AI host could use as input for worldbuilding.
4. It identifies real open questions, not filler ones.
5. The author can read the story bible and understand what the story is without having to ask follow-up questions.
