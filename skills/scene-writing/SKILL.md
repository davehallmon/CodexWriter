# CodexWriter — Scene Writing

> **Role:** Creative Core — Phase 4
> **Type:** Generator / Drafter
> **Position:** Phase 4 of the 5-phase pipeline. Operates after Gate 3 approval and scene outline approval. Takes a scene outline and drafts the actual prose.

---

## Purpose

Scene writing transforms a detailed scene outline into drafted prose. The writer executes the outline's beats, emotional targets, dread elements, and symbolic elements, with room for prose-level choices (word choice, sentence rhythm, dialogue texture).

The scene writer is not deciding what happens — they are dramatizing what the outline defines. This separation of planning from execution is what allows the system to maintain continuity, voice, and dramatic structure across scenes and chapters.

---

## Inputs

- **Scene outline:** From scene planning — beat-by-beat breakdown, emotional targets, dread elements, symbolic elements, thread pulls, continuity notes.
- **Character dossier:** For POV character psychology, voice rules, pressure system, symbolic vocabulary.
- **Character state:** Current dynamic state for the POV character — knowledge, emotional state, physical state, carried pressure.
- **Worldbuilding:** Location details, rules, cultural context for the scene's setting.
- **Story state:** Timeline, promises/payoffs, open questions, continuity risks.
- **Previous scene draft (if applicable):** For continuity of voice and character state across adjacent scenes.
- **Scene template:** `templates/scene-template.md`.

---

## Outputs

- `chapters/[scene_id]-draft.md` or `chapters/[chapter_id]-[scene_number]-draft.md` — the drafted scene prose.
- Updates to scene state:
  - `draft_status` → `draft_complete`
  - `draft_ref` → path to the draft
  - `word_count` → actual count
  - `scene_revision` → incremented
  - Continuity notes recorded from the draft
  - `state_revision` incremented

---

## Workflow

### Step 1: Load the Scene Outline

Read the approved scene outline. Understand:

- The scene's purpose within the chapter
- The beat structure and what each beat must accomplish
- The emotional targets for each beat
- The dread and symbolic elements to deploy
- Any thread pulls and their triggers
- The continuity notes — what must change during the scene

### Step 2: Load Character Context

Read the POV character's dossier and current state:

- **Voice rules:** How does this character speak? What are their vocal patterns, compression rules, what they never say?
- **Pressure system:** What internal pressure is driving them?
- **Emotional state:** What are they feeling coming into this scene?
- **Physical state:** Are they injured, tired, carrying objects?
- **Knowledge:** What do they know? What don't they know? What are they uncertain about?
- **Symbolic vocabulary:** What objects, textures, colors, and images belong to this character?

### Step 3: Load World Context

Read the relevant worldbuilding:

- Location details for the scene's setting
- Rules that constrain what can happen
- Cultural context that informs character behavior

### Step 4: Load Adjacent Context (if applicable)

If this is not the first scene in the chapter, or if it follows an important previous scene:

- Read the previous scene's draft for voice continuity and character state carrying-over.
- Note what the character's state was at the end of the previous scene — that's their starting state for this one.

### Step 5: Draft the Scene

Write the scene prose, following the outline:

**Execute the beats:** Each beat in the outline should be dramatized. The writer decides how to render it in prose, but the beat's purpose should be accomplished.

**Hit the emotional targets:** Each beat has an emotional target. The prose should create that feeling for the reader — through pacing, detail, dialogue, interiority, or what is withheld.

**Deploy dread elements:** Use the dread elements identified in the outline. Dread should be specific and earned — not generic "something scary is happening" but the particular texture of dread this scene requires.

**Deploy symbolic elements:** Use the symbolic objects, motifs, and images from the outline. Symbols should accumulate meaning, not be explained.

**Respect voice rules:** The POV character's dialogue and interiority should follow their voice rules. If the character compresses, evades, or speaks in a particular pattern, the prose should reflect that.

**Respect knowledge constraints:** The POV character cannot react to things they don't know about. The prose should not reveal information the character doesn't have access to.

**Deploy thread pulls (if applicable):** If the scene triggers a Thread Pull, execute it as designed — the sensory artifact triggers the time shift, and the prose moves into the past or future with the same immediacy as the present.

**Show, don't tell:** Dramatize, don't summarize. The reader should experience the scene, not be told about it.

**Mind the tone axioms:** The scene should respect the story's tone axioms. If the tone axioms say "avoid Western, list-making, literal perspective" or "strive for Eastern, poetic, evocative narrative sense," the prose should reflect that.

### Step 6: Self-Review

After drafting, review the scene against the outline:

- Did each beat accomplish its purpose?
- Are the emotional targets hit?
- Are the dread elements deployed?
- Are the symbolic elements used?
- Is the voice consistent with the character's voice rules?
- Are there any knowledge violations (character reacting to things they don't know)?
- Are there any tone axiom violations?

Note any issues. Some can be fixed in revision; some may need to be flagged for the author.

### Step 7: Record Continuity Notes

From the draft, identify what changed:

- **Character state changes:** How did the POV character's emotional or physical state change?
- **Knowledge reveals:** What did the POV character learn? What did the reader learn?
- **Object state changes:** Did any objects change hands, get damaged, get discovered?
- **Relationship shifts:** Did any relationships change status?
- **Promise setups or payoffs:** Did this scene set up a future payoff or pay off an earlier setup?
- **Questions raised or answered:** Did this scene raise new open questions or answer existing ones?

Record these as continuity notes in the scene state. These become the input to the continuity skill.

### Step 8: Record Thread Pulls

If the scene triggered Thread Pulls, record them:

- Which sensory artifact triggered the pull?
- What type of thread (past/future)?
- What did it reveal?
- Which character felt it?

### Step 9: Update Scene State

Update the scene state:

- `draft_status` → `draft_complete`
- `draft_ref` → path to the draft file
- `word_count` → actual count
- `scene_revision` → incremented
- `dread_elements_used` → list the dread elements actually used
- `symbolic_elements_used` → list the symbolic elements actually used
- `thread_pulls_triggered` → list the thread pulls and their details
- `continuity_notes` → record the continuity notes from Step 7
- `updated_at` → set

Update `story-state.json`:
- `state_revision` → incremented
- `updated_at` → set

### Step 10: Report to Orchestrator

Report the completed draft to the orchestrator with:

- Scene ID
- Word count
- Draft path
- Continuity notes summary
- Any issues the writer couldn't resolve
- Whether the scene is ready for review or needs revision

---

## Voice Preservation

The scene writer must preserve the POV character's voice. This is the most common failure mode — the prose drifts into the writer's voice or a generic narrative voice.

Voice preservation techniques:

- **Read the character's voice rules before drafting:** Know how they speak, what they compress, what they never say.
- **Read a previous scene featuring this character:** Match the voice to what's been established.
- **Check dialogue against voice rules:** After drafting, review every line of dialogue. Does it follow the character's speech patterns? Does it violate any voice rules?
- **Check interiority:** The POV character's thoughts should sound like them, not like the narrator. If the character would never think a certain thought, it doesn't belong.

If voice drift is detected during self-review, revise before reporting completion.

---

## Error Handling

| Error | Response |
|---|---|
| Outline not approved | "This scene outline is not approved. Drafting requires an approved outline. The author needs to approve the outline before I can draft." |
| Character dossier missing | "The POV character's dossier is not available. I need their voice rules, pressure system, and symbolic vocabulary to draft with consistent voice. Either provide the dossier or specify which character this scene is from so I can locate it." |
| Knowledge violation detected | "I drafted this scene, but I notice the POV character reacts to [X] — something they don't know about yet. This is a knowledge violation. I can: 1) Revise the scene so they learn about it here, 2) Change the reaction so it's based on what they do know, or 3) Flag it for the author to decide." |
| Tone axiom violation | "This passage may violate the tone axiom: [axiom]. The passage reads as [description], which conflicts with [constraint]. Do you want me to revise, or is this an intentional exception?" |
| Voice drift detected | "I notice the prose in this scene drifts from the character's established voice in [specific way]. I can revise to bring it back into voice, or flag it for review." |
| Thread pull trigger missing | "The outline specifies a Thread Pull triggered by [sensory artifact], but I can't find a natural place to deploy that trigger in the prose. The trigger needs to be a sensory detail that's present in the scene. Do you want me to add the trigger detail, or adjust the Thread Pull?" |

---

## Portability

- All outputs are Markdown — universally readable.
- Scene writing is a prompting pattern — any AI host can draft prose from an outline.
- Voice rules, knowledge constraints, and tone axioms are written into the input documents, making them visible to any host.
- The self-review process is described as a prompting pattern, not a software tool.

---

## Integration with Scene Planning and Continuity

Scene writing is the execution layer that sits between planning and continuity:

- **Scene planning** provides the outline. The writer executes it.
- **Continuity** checks the draft against the state. The writer records what changed.

The writer should not skip the continuity note recording. Those notes are what allow the continuity skill to check the draft against the state without re-reading the entire manuscript.

---

## Prose Style Guidelines

The scene writer should follow the story's style profile and tone axioms. General principles that apply across most literary fiction:

- **Specific nouns and verbs over excessive adjectives:** Ground the scene in concrete detail.
- **Sentence rhythm matches mood:** Punchy in action; meandering in doubt; fragmented in shock.
- **Emotion through gesture, silence, and sensory mismatch:** Don't announce emotions — show them through what the character does, doesn't do, notices, or misses.
- **Naturalistic dialogue:** Dialogue should have character-specific rhythm, interruptions, hesitations, and what's left unsaid.
- **Sensory immersion:** Include smell, sound, texture, taste — not just sight.
- **Avoid exposition dumps:** Information should emerge through action, dialogue, and perception, not be delivered in blocks.
- **Show, don't tell:** Dramatize. The reader should experience the scene.

These are general principles. The specific style profile (e.g., Stephen King / Literary Horror) may add or modify these. The story bible's tone axioms are authoritative.

---

## File Outputs

- `chapters/[scene_id]-draft.md` — the drafted scene prose.
- Updated scene state in story-state.json or scene-state.json.

---

## Evaluation

A scene writing implementation is successful when:

1. The draft accomplishes each beat's purpose from the outline.
2. The emotional targets are hit — the reader feels what the outline intended.
3. The POV character's voice is consistent with their dossier and previous scenes.
4. No knowledge violations — the character doesn't react to things they don't know.
5. Dread and symbolic elements are deployed as planned.
6. Thread Pulls are executed as designed, with the sensory trigger present in the prose.
7. Continuity notes are recorded accurately — what changed in the scene.
8. The prose respects the story's tone axioms and style profile.
9. A different AI host could read the outline and produce a comparable draft.
