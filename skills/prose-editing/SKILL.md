# CodexWriter — Prose Editing

> **Role:** Evaluation / Revision — Phase 5
> **Type:** Refiner / Editor
> **Position:** Phase 5 of the 5-phase pipeline. Operates after Gate 4 approval and after continuity is clean. Takes a drafted scene and revises it for prose quality, voice fidelity, pacing, and clarity.

---

## Purpose

Prose editing improves the quality of drafted scenes. It addresses:

- Voice fidelity — does the prose sound like the character?
- Pacing — is the scene too fast, too slow, or well-paced?
- Clarity — is the prose clear, or is it obscured by awkward phrasing, overwriting, or ambiguity?
- Emotional impact — does the scene land the way it should?
- Style consistency — does the prose respect the story's tone axioms and style profile?

Prose editing is distinct from continuity (which checks mechanical consistency) and reader simulation (which tests the reader's experience). Prose editing is the craft layer — the human or AI editor making the prose better.

---

## Inputs

- **Drafted scene:** The prose from scene writing.
- **Scene outline:** To understand what the scene is trying to accomplish.
- **Character dossier:** For voice rules, pressure system, symbolic vocabulary.
- **Character state (pre-draft):** What the character knew and felt coming in.
- **Character state (post-draft):** What the character knows and feels going out.
- **Continuity report:** To know what mechanical issues have been flagged.
- **Story bible:** For tone axioms, style profile, narrative principles.
- **Worldbuilding:** For location and cultural context.

---

## Workflow

### Step 1: Load the Scene and Context

Read the drafted scene, the outline, the character dossier, the continuity report, and the story bible.

Understand:
- What the scene is trying to accomplish (from the outline)
- Who the POV character is and how they speak (from the dossier)
- What mechanical issues have been flagged (from continuity)
- What tone and style constraints apply (from the story bible)

### Step 2: Assess Voice Fidelity

Check the prose against the character's voice rules:

- **Dialogue:** Does the character's dialogue follow their speech patterns? Compression, evasion, directness, vocabulary?
- **Interiority:** Does the POV character's thoughts sound like them? Or do they sound like the narrator or a generic voice?
- **Prose texture:** Does the overall prose style match the character's voice? A character who is terse and guarded should not have lush, introspective prose unless there's a reason.

Voice issues to flag:
- Dialogue that sounds like a different character
- Interiority that sounds generic or narrator-like
- Prose that drifts from the character's voice in tone, register, or texture
- Voice rules violated (e.g., a character who never swears does swear)

### Step 3: Assess Pacing

Check the scene's pacing:

- **Scene length vs. content:** Is the scene too long for what it accomplishes? Too short?
- **Beat pacing:** Are the beats from the outline paced well? Does each beat get the space it needs?
- **Tension arc:** Does tension build, peak, and resolve (or deliberately not resolve) across the scene?
- **Slow sections:** Are there sections that drag — too much detail, too little happening?
- **Fast sections:** Are there sections that rush through important moments?

Pacing issues to flag:
- Sections that could be trimmed without losing content
- Sections that need expansion — important moments getting short shrift
- Beat transitions that feel abrupt or sluggish

### Step 4: Assess Clarity

Check the prose for clarity issues:

- **Awkward phrasing:** Sentences that are hard to parse.
- **Overwriting:** Too many adjectives, adverbs, or flourish. Prose that's more interested in itself than in the scene.
- **Ambiguity:** Is it clear who is doing what, what is happening, what a character is feeling?
- **Unexplained references:** Is there something the reader needs to know but doesn't?
- **Mixed metaphors or clichés:** Prose that relies on tired phrases or confused imagery.

Clarity issues to flag:
- Sentences that need rewriting for clarity
- Passages where the reader might get lost
- Clichés that should be replaced with specific detail

### Step 5: Assess Emotional Impact

Check whether the scene lands emotionally:

- **Emotional targets from the outline:** Are the intended emotional targets hit? Does the reader feel what the outline intended?
- **Emotional buildup:** Does the emotion accumulate across the scene, or does it arrive all at once?
- **Emotional authenticity:** Does the character's emotional reaction feel true to their pressure system and psychological profile?
- **Withholding:** Is there enough restraint? Or does the prose explain too much, robbing the reader of discovery?

Emotional issues to flag:
- Emotional moments that don't land because they're rushed or over-explained
- Emotional reactions that feel false to the character
- Moments where the prose tells the reader what to feel instead of creating the feeling

### Step 6: Assess Style Consistency

Check the prose against the story's tone axioms and style profile:

- **Tone axioms:** Does the prose violate any tone axioms? (e.g., "no Western, list-making, literal perspective" or "strive for Eastern, poetic, evocative narrative sense")
- **Style profile:** Does the prose match the story's style profile? (e.g., Stephen King / Literary Horror — psychological realism, grounded settings, dread emerging from familiarity, moral tension)
- **Show, don't tell:** Is the scene dramatized, or is it summarized?

Style issues to flag:
- Tone axiom violations
- Prose that drifts from the story's style profile
- Exposition dumps or summary instead of dramatization

### Step 7: Prioritize Findings

Organize findings by priority:

- **Voice fidelity issues** — high priority. Voice drift damages the character across scenes.
- **Clarity issues** — high priority. The reader shouldn't struggle to understand what's happening.
- **Pacing issues** — medium priority. Pacing can often be fixed with trimming or expansion.
- **Emotional impact issues** — medium priority. Emotional landing is important but sometimes requires larger structural changes.
- **Style consistency issues** — medium priority. Tone axiom violations should be fixed, but minor style drift may be acceptable.

### Step 8: Apply Revisions

Revise the prose based on the findings. Prioritize:

1. **Voice fixes** — bring the prose back into the character's voice.
2. **Clarity fixes** — rewrite awkward phrasing, remove overwriting, clarify ambiguity.
3. **Pacing fixes** — trim slow sections, expand rushed moments, adjust beat transitions.
4. **Emotional fixes** — adjust emotional buildup, fix false reactions, add restraint where needed.
5. **Style fixes** — address tone axiom violations, align with style profile.

Revisions should be surgical, not wholesale. The goal is to improve the prose, not rewrite the scene from scratch.

### Step 9: Record Editing Notes

Record what was changed and why:

- **Editing notes** — a list of revisions made, with brief explanations.
- **Remaining issues** — anything that was flagged but not fixed (because it requires author input, structural change, or is a judgment call).

### Step 10: Update State and Report

Update the scene state:
- `draft_status` → `revised` (or `approved` if the author approves)
- `scene_revision` → incremented
- `evaluation_notes` → record the editing notes

Report completion to the orchestrator with:
- What was revised
- What remains as an open issue
- Whether the scene is ready for author review

---

## Error Handling

| Error | Response |
|---|---|
| Continuity not clean | "There are unresolved continuity issues in this scene. Prose editing should happen after continuity is clean, because fixing prose in a scene that has mechanical errors may introduce more errors. Here are the open continuity findings: [list]. Do you want to address those first, or proceed with prose editing anyway?" |
| Voice rules missing | "The POV character's voice rules are not available. I can edit for general prose quality, but I cannot check voice fidelity without the dossier. Do you want to proceed with general editing, or provide the dossier first?" |
| Outline missing | "The scene outline is not available. I can edit the prose as it stands, but I cannot assess whether the scene is accomplishing its intended purpose without the outline. Do you want to provide the outline, or edit without that context?" |
| Author wants a different direction | "The author wants to change [specific direction]. This is a creative decision that goes beyond prose editing. I can revise the prose to align with the new direction, but the change itself is an author decision, not an editing fix." |

---

## Portability

- All outputs are Markdown — universally readable.
- Prose editing is a prompting pattern — any AI host can edit prose against voice rules, pacing, clarity, and style.
- The editing notes format is text-based and can be read by any host.
- The distinction between mechanical fixes (clarity, voice rules) and judgment calls (emotional impact, pacing) is a prompting discipline, not a software tool.

---

## Integration with Other Skills

- **Continuity** should run before prose editing. Fixing prose in a scene with mechanical errors may introduce more errors.
- **Reader simulation** should run after prose editing. The reader should experience the revised prose, not the draft.
- **Scene writing** produced the draft. Prose editing improves it. The scene writer and prose editor can be the same AI host or different ones — separation can improve quality by bringing a fresh eye.

---

## Editing Principles

General principles that guide prose editing:

- **Preserve what works:** Not every passage needs revision. Good prose should be left alone.
- **Fix the biggest issues first:** Voice drift, clarity problems, and tone axiom violations are more important than minor word choice improvements.
- **Surgical, not wholesale:** Revise specific passages, not the entire scene. wholesale rewriting risks introducing new issues.
- **Explain the why:** Editing notes should explain why a change was made, so the author can understand the reasoning and disagree if they want.
- **Respect the author's voice:** The goal is to serve the story, not to impose a generic "good writing" standard. If the author's style is intentionally rough, raw, or unconventional, editing should respect that.

---

## File Outputs

- Updated scene draft (revised prose).
- Updated scene state with evaluation notes.
- (Optional) `editing-notes-[scene_id].md` — a separate document listing revisions and remaining issues.

---

## Evaluation

A prose editing implementation is successful when:

1. It catches voice fidelity issues and fixes them.
2. It identifies clarity problems and rewrites them.
3. It addresses pacing issues without over-trimming or over-expanding.
4. It respects the story's tone axioms and style profile.
5. It distinguishes mechanical fixes from judgment calls and doesn't pretend the latter are objectively resolved.
6. Editing notes explain the reasoning behind changes.
7. A different AI host could read the draft, the dossier, and the story bible, and produce a comparable revision.
