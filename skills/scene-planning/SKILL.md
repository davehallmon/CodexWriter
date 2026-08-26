# CodexWriter — Scene Planning

> **Role:** Creative Core — Phase 3 (late) / Phase 4 (early)
> **Type:** Generator / Planner
> **Position:** Operational at the boundary of Phase 3 and Phase 4. After Gate 3 approval, scene planning takes the chapter outline and creates detailed scene outlines ready for drafting.

---

## Purpose

Scene planning takes a chapter from the architecture and breaks it into a detailed scene outline. The outline is the direct input to scene writing — it tells the writer what happens, beat by beat, with emotional targets, dread elements, symbolic elements, and continuity notes.

A good scene outline eliminates uncertainty for the scene writer. The writer should not have to decide what happens — they should execute what the outline defines, with room for prose-level choices.

---

## Inputs

- **Chapter outline:** From narrative architecture — which scenes belong in which chapters, POV assignments, chapter purpose.
- **Character dossiers:** For POV character psychology, voice rules, pressure system, current state.
- **Character state:** Current dynamic state for the POV character (from character-state.json) — what they know, feel, and carry into the scene.
- **Worldbuilding:** Location details, rules, cultural context for the scene's setting.
- **Story state:** Timeline, promises/payoffs, open questions, continuity risks.
- **Scene template:** `templates/scene-template.md`.

---

## Outputs

- `scenes/[scene_id]-outline.md` — detailed scene outline using a structured format.
- Updates to `scene-state.json` (or the scenes section of story-state.json):
  - Scene entry created with scene_id, chapter_id, scene_number_in_chapter, pov_character_id, outline_status, beats, etc.
  - `state_revision` incremented.

---

## Workflow

### Step 1: Load the Chapter Context

Read the chapter outline from narrative architecture. Identify:

- Which scene in the chapter is being planned
- POV character and their current state
- Setting and location
- Which beats from the architecture belong to this scene
- What the chapter's purpose is

### Step 2: Load Character State

Read the POV character's current state from `character-state.json`:

- What they know (and don't know)
- Their emotional state and pressure level
- Their physical state
- What pressure they are carrying

This is critical. The scene outline must respect the character's knowledge constraints — the POV character cannot react to things they don't know about.

### Step 3: Load World Context

Read the relevant worldbuilding artifacts:

- Location details for the scene's setting
- Any rules that constrain what can happen
- Cultural context that informs character behavior in this setting

### Step 4: Define the Scene Beats

Break the scene into beats. Each beat is a unit of dramatic action — a moment of change, revelation, tension, or decision.

Each beat includes:

- **Beat number:** Sequential within the scene.
- **Description:** What happens in this beat.
- **Emotional target:** What the reader should feel during this beat.
- **Dread element (if applicable):** What suspense or dread is deployed.
- **Symbolic element (if applicable):** What symbolic object or motif is used.
- **Thread pull (if applicable):** Does this beat trigger a past or future thread? What sensory artifact triggers it? What does it reveal?
- **Knowledge state before:** What does the POV character know coming into this beat?
- **Knowledge state after:** What does the POV character know going out of this beat?

The beats should form a coherent dramatic arc within the scene — tension builds, peaks, and resolves (or deliberately doesn't resolve).

### Step 5: Identify Dread and Symbolic Elements

For each beat, identify:

- **Dread elements:** What creates suspense or dread? (silence, sensory mismatch, anticipation, bodily reaction, moral tension, the mundane becoming eerie)
- **Symbolic elements:** What objects, motifs, or images carry symbolic weight? These should connect to the character's symbolic vocabulary and the story's broader motif registry.

Dread and symbolism should be specific and actionable — the scene writer needs to know what to deploy, not just that they should "make it tense."

### Step 6: Map Continuity Notes

Identify what changes during the scene:

- **Character state changes:** How does the POV character's emotional or physical state change?
- **Knowledge reveals:** What does the POV character learn? What does the reader learn?
- **Object state changes:** Do any objects change hands, get damaged, get discovered?
- **Relationship shifts:** Do any relationships change status?
- **Promise setups or payoffs:** Does this scene set up a future payoff or pay off an earlier setup?
- **Questions raised or answered:** Does this scene raise new open questions or answer existing ones?

These continuity notes become the input to the continuity skill after drafting.

### Step 7: Identify Thread Pulls

If the scene triggers Thread Pulls (non-linear time shifts), map them:

- **Trigger:** What sensory artifact triggers the thread pull?
- **Thread type:** Past (analepsis) or future (prolepsis)?
- **What it reveals:** The content of the time shift.
- **Felt by:** Which character experiences the thread pull?
- **Dramatic purpose:** Why this thread pull exists.

Thread Pulls should be designed deliberately, not accidental. Each one should have a clear purpose.

### Step 8: Assemble the Scene Outline

Compile everything into a scene outline document using the scene template structure:

- Scene identity (ID, chapter, number, title, POV, setting)
- Beat-by-beat breakdown
- Dread and symbolic elements
- Thread pulls
- Continuity notes
- Knowledge state changes

The outline should be detailed enough that the scene writer can draft without wondering what happens next.

### Step 9: Author Review

Present the scene outline to the author. Highlight:

- The beat structure and dramatic arc
- POV and knowledge constraints respected
- Dread and symbolic elements identified
- Continuity notes and promise/payoff connections
- Any planning decisions that need author input

The author approves, requests revisions, or rejects.

### Step 10: Gate 4 Preparation

On author approval:
- Set `outline_status` → `outline_approved` in scene state.
- The scene is now ready for drafting.
- Report completion to the orchestrator.

---

## Error Handling

| Error | Response |
|---|---|
| Character state missing | "The POV character's current state is not available. I need to know what they know, feel, and carry into this scene. Either load the character state from a previous chapter, or provide a description of their current condition." |
| Beat conflicts with character knowledge | "This beat has the POV character reacting to [X], but their current knowledge state shows they don't know about [X] yet. Options: 1) Change the beat so they learn about it in this scene, 2) Assign the scene to a different POV character who knows about it, 3) Have them learn about it indirectly." |
| Dread element contradicts tone axioms | "This dread element ([description]) may conflict with the story's tone axioms: [axiom]. The tone axioms say [constraint]. Do you want to adjust the dread element or reconsider the axiom?" |
| Outline too thin | "This scene outline has [N] beats, which may not be enough for a scene of this importance. The chapter purpose is [purpose]. Do you want to add more beats, or is this a short scene by design?" |
| Outline too detailed | "This scene outline is very detailed, which may constrain the scene writer too much. The beats are clear, but consider leaving some room for the writer's prose-level choices. Which beats are structural (must happen) vs. flexible (can be executed in different ways)?" |

---

## Portability

- All outputs are Markdown — universally readable.
- The scene outline structure is text-based and can be executed by any AI host.
- The outline is designed to be read by scene writing skills regardless of which host runs them.
- Beat-level structure with emotional targets, dread elements, and symbolic elements is a prompting pattern, not a software tool.

---

## Integration with Scene Writing

The scene outline is the direct input to scene writing:

- **Scene writing** takes the outline and drafts the actual prose.
- The writer should execute the outline's beats, emotional targets, dread elements, and symbolic elements.
- The writer has room for prose-level choices (word choice, sentence rhythm, dialogue texture) but should not deviate from the structural plan without reason.

If the writer discovers during drafting that the outline needs adjustment, they should flag it. The outline can be revised, but the revision should go through the scene planning skill, not be improvised during drafting.

---

## Dread Element Catalog

Scene planning should draw on a catalog of dread elements appropriate to the story's tone. Examples (adapt to the specific story):

- **Silence:** The absence of sound as tension. What isn't said, what isn't heard.
- **Sensory mismatch:** When the senses report something that doesn't match expectation. A smell that shouldn't be there. A sound that's slightly off.
- **Anticipation:** The dread of what's coming. The character waiting for something to happen.
- **Bodily reaction:** The body betraying what the character is suppressing. Dry mouth, quick pulse, muscle tension, nausea.
- **Moral tension:** The character facing a choice that has a cost. The dread of what they might do.
- **The mundane becoming eerie:** Ordinary objects or settings taking on ominous significance.
- **Compression:** The feeling of being trapped, watched, or closing in.
- **Time pressure:** The dread of time passing without result, or time running out.

The specific catalog should be defined in the story bible's tone axioms and expanded during worldbuilding or character development.

---

## Symbolic Element Catalog

Scene planning should draw on the character's symbolic vocabulary and the story's motif registry. Symbols should be:

- **Character-specific:** Objects, textures, colors, and images that belong to this character's symbolic vocabulary.
- **Story-coherent:** Connected to the broader motif registry, not random.
- **Actionable:** Specific enough that the scene writer knows what to deploy.
- **Bounded:** Within the character's allowed symbols — not using another character's reserved symbols.

Symbols should accumulate meaning across scenes, not be announced. The scene writer should use them, not explain them.

---

## File Outputs

- `scenes/[scene_id]-outline.md` — the scene outline document.
- Updated scene state in story-state.json or scene-state.json.

---

## Evaluation

A scene planning implementation is successful when:

1. The outline is detailed enough that a scene writer can draft without asking what happens next.
2. Beat-level structure respects the POV character's knowledge constraints.
3. Dread and symbolic elements are specific and actionable, not vague.
4. Continuity notes identify real changes that will need post-draft checking.
5. A different AI host could read the outline and draft the scene without contradicting the outline's plan.
