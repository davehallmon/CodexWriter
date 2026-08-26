# CodexWriter — Character Development

> **Role:** Creative Core — Phase 2
> **Type:** Generator / Psychologist
> **Position:** Phase 2 of the 5-phase pipeline. Operates after Gate 1 approval. Takes character sketches from the story bible and develops them into full dossiers.

---

## Purpose

Character development transforms brief character sketches from the story bible into complete, psychologically distinct dossiers. Each dossier is the authoritative reference for how that character thinks, feels, speaks, acts, and changes across the story.

The dossier is the bridge between the abstract character (role label, dramatic function) and the living character (scene-level behavior, voice, pressure system).

---

## Inputs

- **Story bible:** Character list with role labels, dramatic functions, and brief summaries.
- **Worldbuilding:** For context on the world that shapes character pressures (can be parallel or prior).
- **Genre and tone axioms:** From the story bible.
- **Any existing character notes:** Research, inspiration, prior drafts.

---

## Outputs

- `characters/` directory containing:
  - `character_dossier_[character_id].md` for each main and significant supporting character
  - Using the `templates/character-dossier-template.md` structure

- Updates to `story-state.json`:
  - `characters[character_id]` entries populated with full references
  - `character.current_state_ref` pointing to the dossier
  - `character.voice_ref` pointing to voice/speech rules
  - `state_revision` incremented

---

## Workflow

### The V4 Dossier Pipeline

Character development follows a 4-phase, 15-step controlled research-and-synthesis pipeline. This pipeline was developed through extensive iteration (documented in the Gemini Development notebook) and is the recommended methodology for creating original, evidence-bound, psychologically distinct character dossiers.

The pipeline has six core axioms:

1. **Evidence before interpretation** — Extract what the source text actually says before inferring psychology.
2. **Pressure system before craft parallels** — Define the character's unique internal pressure before looking at external style references.
3. **Stephen King is a style/craft engine only** — Use King for dread mechanics, embodiment, moral corrosion, and voice-under-stress patterns. Never copy his plots, dialogue, scenes, or characters.
4. **Abram's dossier is a format reference only** — One character's psychology must never default onto another. Each character gets their own body, voice, wound, moral logic, pressure system, and relationship web.
5. **Extract then synthesize** — Gemini NotebookLM extracts craft evidence; the Deep-Research LLM synthesizes it into original characterization.
6. **Every section carries a source lineage note** — Distinguish textual evidence, historical context, creative extrapolation, and craft reference.

---

### Phase 1: Pre-Processing — Context and Intake

#### Step 1: Source and Context Manifest (00A)

Establish exactly which texts enter the pipeline and their trust hierarchy:

| Source Tier | Trust Level | Use For | Do Not Use For |
|---|---|---|---|
| Genesis anchor text | Highest | Actions, speech, consequences | Modern psychology or motives |
| Translation notes | High | Textual ambiguity, variant readings | Certainty where text is unclear |
| Historical-cultural scholarship | Medium-High | Plausibility (ANE norms, customs) | Directly proving biblical events |
| Prior character dossiers | Low-Medium | Continuity (family ties, chronology) | Inferring inner motives |
| Abram dossier (if prior) | Low | Format/structure reference only | Transferring psychology |
| King corpus | Medium | Style/craft pressure (dread, embodiment) | Copying plots, dialogue, prose |

Produces: **Governing Boundary Map** — protects the character from anachronistic modern psychology and defines strict anti-contamination rules.

#### Step 2: Character Intake Card (00B)

Establish the character's dramatic foundation before any research or comparison:

- Character Name
- Role Label
- Dramatic Function
- Biblical Anchors (key scenes)
- Key Relationships
- Key Scenes
- **Pressure System** — what internal pressure drives this character
- Cosmic Orientation (relationship to the divine/covenant if relevant)
- Primary Tension
- Interpretive Stance
- Historical-Social Assumptions
- Negative Archetype (what lazy version must be avoided)
- Anti-Archetype Choices (what unexpected direction to take)
- Clichés to Avoid
- Research Questions
- Continuity Risks

**Critical rule:** Identify the "lazy version" of the character early and define the choices that prevent it.

Produces: **Intake Profile** — the character's unique pressure system, defined before any research or King parallels.

---

### Phase 2: Deep Research — Evidence and Synthesis

#### Step 3: Biblical Evidence Extraction (DR1)

Filter the source text to extract only what is actually on the page:

- Direct actions
- Direct speech
- Silences and omissions (what the text withholds)
- Relationship pressures
- Social pressures
- Cosmic pressures (if relevant)
- Consequences
- Repeated patterns
- Textual limits (what the text does NOT say)

**Evaluation harness standard:**
- Textual claims separated from inference
- Evidence specific to this character
- No imported scenes, voice, or fears from other characters
- No King material yet
- Missing textual limits identified

Produces: **Evidence Spreadsheet** — direct textual data mapped against textual limits.

#### Step 4: Interpretive Synthesis (DR2)

Translate the DR1 evidence into core psychological and social tensions:

- What the character wants / secretly wants
- What they fear losing
- Their pressure system
- Their moral compromises
- Textual silences and what they might mean
- Three possible dramatic readings
- Risks of over-reading
- Textual boundaries
- Negative archetype test

Produces: **Interpretive Matrix** — the character's personal moral compromises and narrative boundaries.

#### Step 5: Contamination Audit (DR2 QA)

Submit the DR2 synthesis to a panel of 6 adversarial reviewer modes:

1. **Biblical Textual Critic** — catches over-reading, unjustified inference, textual distortion
2. **Bronze Age Social Historian** — catches anachronistic psychology, modern social assumptions
3. **Trauma/Psychology Reader** — catches over-psychologizing, clinical language, modern diagnosis creep
4. **Narrative Architect** — catches flattening, boring choices, lack of dramatic tension
5. **Originality Auditor** — catches cliché, lazy archetypes, derivative choices
6. **Continuity Editor** — catches contamination from other character dossiers

Produces: **Vulnerability Report** — exposing modern biases, over-psychologizing, and psychological bleed-through from other characters.

#### Step 6: Biblical Character Profile (DR3)

Consolidate the validated biblical and historical research into a unified, clean document:

- Strip out procedural scaffolding
- Apply strict Source Lineage Notes to every section
- Ensure the document is ready for ingestion into the style-matching engine

Produces: **Clean Source Packet** — the character's evidence base, ready for craft integration.

#### Step 7: Ingestion Audit (DR3 QA)

Final verification that the DR3 packet is completely free of contaminated context or speculative drift before it is used for style matching.

Produces: **Search-Ready Ingestion Certificate.**

---

### Phase 3: Stephen King Style and Craft Engine

In this phase, the King corpus is used as a **pressure engine** to extract physical tells, stress-voice patterns, and dread mechanics — while strictly forbidding the copying of King's literal plots, prose, or characters.

#### Step 8: Notebook Source Manifest (NBLM0)

Register and classify the external craft references, assigning trust levels and marking plagiarism risks.

Produces: **External Source Ledger** — establishing boundaries for stylistic integration.

#### Step 9: King Corpus Broad Scan (NBLM1)

Scan the King corpus specifically for abstract behaviors:
- Moral logic under pressure
- Fear response and coping mechanisms
- Nervous tells
- Voice under stress
- How the body physically betrays what the character is suppressing

Produces: **Behavioral Scavenger Log** — raw, abstract human reactions.

#### Step 10: Match Analysis and Top 5 King Parallels (NBLM2 & NBLM3)

Pair the character's unique pressure system (from Phase 1) with King characters:

- Prioritize abstract behavioral and psychological alignment over demographic or surface resemblance
- Rank the top 5 matches
- For each match: why it works, what abstract techniques to adapt, what NOT to copy

Produces: **Ranked Parallel Index.**

#### Step 11: Contamination Audit (NBLM3 QA)

Formally audit and approve/reject the proposed King parallels to eliminate:
- Plagiarism risks
- Inappropriate modern tropes (e.g., modern domestic abuse frames, split-personality tropes)
- King-specific borrowing that would distort the character

Produces: **Vetted Style Parallel List** — ready for deep extraction.

#### Steps 12-15: Mechanics Extraction (NBLM4 through NBLM7)

Extract highly specialized, abstract mechanics into four dedicated writing resource files:

**NBLM4 — Scene Parallels:** Abstract dread, domestic claustrophobia, escalation mechanics, sensory unease. Do not copy scenes.

**NBLM5 — Relationship Dynamics:** Power imbalances, fear, shame, moral corrosion, how characters distort each other.

**NBLM6 — Physical and Nervous Manifestations:** How the body physically betrays what the character is suppressing. Adapt to the historical world — avoid generic trembling/sweating. Find body-specific tells.

**NBLM7 — Speech and Voice Patterns:** Vocal compression, evasion, denial, confession, fragmentation rules. How the character's voice changes under stress.

Produces: **Four Sensory Craft Files** — actionable prompts and bodily rules for scene-level writing.

---

### Phase 4: Synthesis — Assembly and Final QA

#### Step 13: Dossier Assembly Draft (DR4)

Synthesize (rather than list) the research and craft parameters into an original character. The dossier has 14 sections:

1. **Character Summary** — one-paragraph essence
2. **Biblical Evidence Base** — what the text actually says, with epistemic verb discipline
3. **Character-Specific Pressure System** — the core internal pressure, uniquely this character's
4. **Psychological and Moral Profile** — moral logic, contradictions, how they decide
5. **Historical-Social Embodiment** — how they live in their world
6. **King Style-and-Craft Pressure Integration** — how abstract King-craft mechanics apply, with source lineage
7. **Relationships** — key dynamics and how they evolve
8. **Voice and Speech Rules** — how they speak, vocal patterns, compression rules
9. **Scene Applications** — specific scenes where they appear
10. **Character Arc** — how they change across the story
11. **Symbolic Vocabulary** — objects, textures, colors, body imagery unique to this character
12. **Negative Archetype Defense** — what cliché must be avoided and why
13. **Originality Guardrails** — specific things that must never happen with this character
14. **Writer's Quick-Use Sheet** — one-page summary for drafting

**Epistemic verb discipline:** Every claim must be labeled by evidence type:
- TEXTUAL EVIDENCE — directly stated or shown in the source
- OBSERVABLE PATTERN — repeated behavior or structural pattern
- REASONABLE INFERENCE — plausible reading, not certainty
- HISTORICAL-CULTURAL CONTEXT — background plausibility
- CREATIVE EXTRAPOLATION — adaptation choice for fiction
- KING-CRAFT REFERENCE — abstract craft parallel, not copied material
- KING-STYLE REFERENCE — style mechanics, not copied material

Produces: **14-Section Master Assembly Draft.**

#### Step 14: Final QA and Revision Notes (DR5)

Submit the completed DR4 draft to a final round of 6-mode adversarial auditing:

1. **Biblical Evidence Auditor** — evidence labeling, textual fidelity
2. **Historical-Cultural Auditor** — plausibility, anachronism check
3. **Psychological/Embodiment Auditor** — psychological coherence, body specificity
4. **Narrative Architect** — dramatic shape, tension, arc
5. **Originality/King-Borrowing Auditor** — plagiarism check, cliché check, King scaffolding burial
6. **Continuity/Contamination Editor** — cross-character contamination, story consistency

Produces: **DR5 Final Action Log** — required fixes and revisions.

#### Step 15: Final Dossier Complete (00C)

Execute all required fixes from DR5:
- Apply revisions
- Seal the character's custom symbolic vocabulary
- Certify the dossier with a final validation table
- Add a final Source Lineage Summary confirming exclusion of psychological transfer from other characters

Produces: **Finalized Character Blueprint** — the active, modular database used to draft original scenes.

---

## Cross-Character Contamination Prevention

The most important rule in character development: **one character's psychology must never default onto another.**

Specific contamination risks to watch for:

- **Abram → others:** Abram's covenant faith, his specific fears, his theological framework must not transfer to other characters unless textual evidence justifies it. His dossier is a format reference only.
- **Sarai → other women:** Sarai's specific pressure system (barrenness, household rank, public vulnerability) must not become the default for other female characters.
- **Lot → other survivors:** Lot's specific compromised-survivor psychology must not bleed into other characters who have different relationships to the cities they live in.
- **Shared traits:** Characters in the same family can share history, but they must not share psychology, voice, or pressure system.

Every dossier must pass a negative archetype test: does this character risk becoming the lazy version? If yes, define the anti-archetype choices that prevent it.

---

## Error Handling

| Error | Response |
|---|---|
| Character too thin in story bible | "This character has a role label and dramatic function but not enough to build a full dossier. I need at least: key scenes, key relationships, and a sense of their pressure system. Here are questions that would help: [list]." |
| Contamination detected | "This section shows psychological bleed-through from [other character]'s dossier. The [specific trait/pressure/voice] here belongs to [other character], not this one. I'm flagging it for revision." |
| King borrowing risk | "This craft extraction is too close to King's specific language/scene/dialogue. The rule is: extract the abstract mechanic, not the expression. Here's the abstract version: [reformulation]." |
| Evidence/inference confusion | "This claim is labeled as textual evidence but it's actually inference. TEXTUAL EVIDENCE means directly stated or shown in the source. This is REASONABLE INFERENCE — plausible from the evidence but not certain." |

---

## Portability

- All outputs are Markdown — universally readable.
- The V4 pipeline is methodology, not platform-specific tools. Any AI host can follow the 15-step process.
- The epistemic verb discipline and source lineage notes are written into the dossier content, making them visible to any downstream consumer.
- The 6-mode QA audit is described as a prompting pattern, not a software tool — it works across hosts.

---

## Integration with Worldbuilding

Character development and worldbuilding are both Phase 2. They must cross-reference:

- **Pressure systems arise from world position:** A character's status, kinship, gender, and cultural position shape their pressures. The dossier should reference the worldbuilding context that makes those pressures plausible.
- **Rules constrain character action:** Characters operate within world rules. Their choices and conflicts should be shaped by those constraints.
- **Voice reflects culture:** A character's speech patterns should reflect their place in the world's social and cultural hierarchy, not just their personality.

If worldbuilding runs first, it provides the stage. If character development runs first, it defines what the world needs to contain. Either order works — the orchestrator should ensure cross-referencing before Gate 2.

---

## Sources and Provenance

This skill draws on patterns from:

- **Haowjy/creative-writing-skills:** `character-sim` and `character-designer` agents — the concept of character psychology as a specialist role with pressure systems and voice rules.
- **JeroTan/novel-writer-english:** Character depth as a knowledge file discipline, separated from the lean specification.
- **Lensetek/Fiction-book-agent-skills:** `character-designer-psychologist` — the role taxonomy and the concept of character sheets with Want/Need/Lie/Ghost and planned arc states.

The V4 pipeline (DR1-DR5, NBLM0-NBLM7) is the recommended implementation methodology, developed through the Gemini Development notebook. It is an independent synthesis that combines biblical evidence extraction, historical-cultural plausibility, adversarial QA auditing, and Stephen King craft integration under strict anti-plagiarism guardrails.

---

## File Outputs

- `characters/character_dossier_[character_id].md` for each character
- Updated `story-state.json` with character references

---

## Evaluation

A character-development implementation is successful when:

1. Each dossier has a unique pressure system that does not default onto other characters.
2. Biblical evidence is distinguished from inference using epistemic verb discipline.
3. King craft integration is abstract and mechanical, not copied plots, dialogue, or scenes.
4. The 6-mode QA audit catches contamination, anachronism, and cliché.
5. A different AI host could read the dossier and write a scene featuring this character without contradicting the dossier's established psychology, voice, and pressure system.
6. The Writer's Quick-Use Sheet is actually useful for quick reference during drafting.
