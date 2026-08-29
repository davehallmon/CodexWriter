# CodexWriter — Narrative Architecture

> **Role:** Creative Core — Phase 3
> **Type:** Generator / Architect
> **Position:** Phase 3 of the 5-phase pipeline. Operates after Gate 2 approval. Takes worldbuilding and character dossiers and designs the plot architecture.

---

## Purpose

Narrative architecture transforms the world and characters into a structured plot. It defines the major arcs, the beat-by-beat progression, the scene breakdown, and the chapter outline. It is the blueprint that scene planning and scene writing will execute.

The architecture must be detailed enough that a scene writer can pick up any chapter and know what happens, whose perspective it's from, what the emotional targets are, and what the story gains or loses in that chapter.

---

## Inputs

- **Approved story bible:** Concept, setting, characters, preliminary plot and timeline.
- **Worldbuilding artifacts:** Locations, rules, cultural context.
- **Character dossiers:** Full psychological profiles, pressure systems, voice rules, arcs.
- **Genre expectations:** Structural conventions of the genre.

---

## Outputs

- `plot/` directory containing:
  - `arc-summary.md` — overall plot summary
  - `arcs.md` or `arcs/` — individual arc definitions
  - `outline.md` — beat-by-beat plot outline
  - `scene-breakdown.md` — scene-by-scene breakdown
  - `chapter-outline.md` — chapter-by-chapter outline with POV assignments

- Updates to `story-state.json`:
  - `plot.arc_summary` populated
  - `plot.arcs[]` populated
  - `plot.beats[]` populated
  - `timeline[]` refined with chapter references
  - `state_revision` incremented

---

## Workflow

### Step 1: Audit the Inputs

Read the story bible, worldbuilding, and character dossiers. Identify:

- What story questions are already answered
- What character arcs need to play out
- What world locations and rules will shape the plot
- What tensions exist between characters
- What the dramatic question is and how it might be resolved

### Step 2: Define the Major Arcs

Identify and describe the major narrative arcs:

- **Main plot arc:** The central story from beginning to end.
- **Subplots:** Secondary storylines that support, contrast, or complicate the main arc.
- **Character arcs:** How each major character changes across the story. (These should align with the character dossiers' stated arcs.)
- **Thematic arcs:** How the story's themes develop and resolve.

Each arc gets:
- A title or identifier
- Type (main, subplot, character, thematic)
- Status (setup, developing, climax, resolved, paying_off)
- A brief description
- Which promises/payoffs it connects to

### Step 3: Build the Beat Outline

Create a beat-by-beat progression of the story. A beat is a unit of dramatic action — a scene's worth or a significant story event.

Each beat includes:
- Beat number (sequential)
- Description (what happens)
- Which arc(s) it serves
- Which chapter it belongs to ( provisional — can be adjusted in scene planning)
- Emotional target (what the reader should feel)
- Any setup/payoff connections

The beat outline should be 20-50 beats for a novella, more for a novel. It is the skeleton that scenes will flesh out.

### Step 4: Design the Scene Breakdown

Group beats into scenes. A scene is a unit of dramatized action in a single location with a single POV (or a defined POV shift).

Each scene entry includes:
- Scene ID (provisional)
- Which beats it covers
- POV character
- Setting/location
- What happens (summary)
- What changes (what is different at the end of the scene)
- Knowledge state change (what does the POV character learn or realize?)
- Continuity notes (character state changes, object state changes, relationship shifts, promise setups/payoffs)

The scene breakdown is the bridge between plot architecture and scene planning. It should be detailed enough that scene planning can turn each entry into a scene outline.

### Step 5: Design the Chapter Outline

Group scenes into chapters. A chapter is a unit of pacing and reader experience.

Each chapter entry includes:
- Chapter ID (e.g., 01, 02, 03)
- Chapter title (provisional)
- Which scenes it contains
- POV character(s)
- Estimated word count range
- Chapter purpose (what this chapter does for the story)
- Entry state (what the reader knows coming in)
- Exit state (what the reader knows going out)

The chapter outline is the final output of narrative architecture. It is the document that scene planning and scene writing will execute against.

### Step 6: Thread Pull Integration

If the story uses Thread Pulls (non-linear time shifts triggered by sensory artifacts), map them into the architecture:

- Which scenes trigger past threads (analepsis)?
- Which scenes trigger future threads (prolepsis)?
- What sensory artifact triggers each thread pull?
- What does each thread pull reveal?

Thread Pulls should be designed as part of the architecture, not added ad hoc during drafting. Each one should have a clear dramatic purpose.

### Step 7: Promise/Payoff Mapping

Identify the promise/payoff structure:

- What is set up in early chapters that pays off later?
- What foreshadowing needs to be planted?
- What payoffs need setup scenes?

Each promise/payoff entry includes:
- Promise ID
- What the promise is
- Type (explicit, implicit, foreshadowed, emotional, thematic)
- Setup chapter references
- Payoff status (pending, paying_off, paid_off, subverted)
- Payoff chapter reference (if applicable)

### Step 8: Update Story State

Update `story-state.json`:

- `plot.arc_summary` — populated
- `plot.arcs[]` — populated with arc definitions
- `plot.beats[]` — populated with beat entries
- `timeline[]` — refined with chapter references
- `state_revision` — incremented
- `updated_at` — set

### Step 9: Author Review

Present the narrative architecture to the author. Highlight:

- The arc structure and how the story moves from beginning to end
- The beat outline and scene breakdown
- The chapter outline with POV assignments
- Thread Pull design
- Promise/payoff structure
- Any open questions or planning decisions that need author input

The author approves, requests revisions, or rejects.

### Step 10: Gate 3 Approval

On author approval:
- Set `phase` → `drafting` in story-state.json
- Set `phase_gate` → `approved`
- Increment `state_revision`
- Set `updated_at`
- Report completion to the orchestrator

---

## Error Handling

| Error | Response |
|---|---|
| Story bible or worldbuilding not approved | "Narrative architecture requires Gate 2 approval. The concept and worldbuilding are not yet locked." |
| Character dossiers not complete | "I can build a provisional architecture, but without complete character dossiers, the character arcs and POV assignments will be provisional. Do you want to proceed with what exists, or complete character development first?" |
| Plot hole detected | "This beat creates a problem: [description]. The story sets up [X] but the current architecture has [Y] happening instead. Here are options: 1) Adjust the beat, 2) Add a bridging beat, 3) Flag for resolution in scene planning." |
| Pacing issue | "This section has [N] beats packed into [M] chapters, which may feel rushed. Alternatively, this section has very few beats across many chapters, which may feel slow. Here's a suggested redistribution: [proposal]." |
| POV conflict | "This scene is assigned to [character A] but the key event is something [character B] experiences and [character A] doesn't witness. Options: 1) Change POV to B, 2) Have A learn about it later, 3) Use a Thread Pull or other device." |

---

## Portability

- All outputs are Markdown — universally readable.
- The beat/scene/chapter structure is text-based and can be executed by any AI host.
- The architecture is designed to be read and followed by scene planning and scene writing skills regardless of which host runs them.
- Chapter IDs, scene IDs, and beat IDs use consistent naming conventions that make cross-referencing machine-readable.

---

## Integration with Scene Planning and Scene Writing

Narrative architecture is the direct input to scene planning and scene writing:

- **Scene planning** takes the scene breakdown and creates detailed scene outlines (using scene-template.md).
- **Scene writing** takes the scene outlines and drafts the actual prose (using scene-template.md).

The chapter outline is the authority for which scenes belong in which chapters. If scene planning or scene writing discovers that a scene needs to move, the architecture should be updated to reflect the change.

---

## Thread Pull Design

If the story uses Thread Pulls (non-linear time shifts triggered by sensory artifacts), the architecture should define:

- **Trigger artifacts:** What sensory elements trigger thread pulls? (blood on stone, texture of a spoil, Egyptian dust taste, rope fibers, ram's hide smell, kokhavim/whispering stars)
- **Thread types:** Past (analepsis) or future (prolepsis)
- **What each thread reveals:** The content of the time shift
- **Which character feels it:** Thread pulls are character-specific — the sensory ghost is felt by a particular character
- **Dramatic purpose:** Why this thread pull exists — what it adds to the story that linear time would not

Thread Pulls should be sparse and meaningful. Each one should be a deliberate architectural choice, not a random time jump.

---

## Sources and Provenance

This skill draws on patterns from:

- **Lensetek/Fiction-book-agent-skills:** `plot-narrative-architect` and `storyboard-scene-planner` — the concept of dedicated plot and scene planning specialists.
- **danjdewhurst/story-skills:** `plot-structure` as one of the 7 core skills, with plot arcs and timeline as durable artifacts.
- **JeroTan/novel-writer-english:** The planner command with full-novel, arc, batch, and light modes; the task ledger as a planning tool.

CodexWriter's approach is an independent synthesis: narrative architecture produces a hierarchical structure (arcs → beats → scenes → chapters) with consistent IDs, promise/payoff tracking, and Thread Pull design integrated into the architecture rather than added later.

---

## File Outputs

- `plot/arc-summary.md`
- `plot/arcs.md` or `plot/arcs/`
- `plot/outline.md` — beat-by-beat outline
- `plot/scene-breakdown.md`
- `plot/chapter-outline.md`
- Updated `story-state.json`

---

## Evaluation

A narrative architecture implementation is successful when:

1. The chapter outline is detailed enough that a scene writer can draft any chapter without asking what happens next.
2. POV assignments are clear and respect character knowledge constraints.
3. The beat outline connects to specific arcs and promises/payoffs.
4. Thread Pulls are designed into the architecture with clear triggers and purposes.
5. A different AI host could read the architecture and produce a scene planning document for any chapter.
