# CodexWriter — Reader Simulation

> **Role:** Evaluation — Phase 5
> **Type:** Simulator / Tester
> **Position:** Phase 5 of the 5-phase pipeline. Operates after Gate 4 approval and after prose editing. Simulates a reader's experience of the manuscript and reports on what works, what doesn't, and what the reader might miss or misunderstand.

---

## Purpose

Reader simulation tests the manuscript from the reader's perspective. It does not judge prose quality (that's prose editing's job) or check mechanical consistency (that's continuity's job). It answers:

- What does the reader experience?
- Where does the reader feel engaged, confused, bored, or moved?
- What does the reader understand, and what might they misunderstand?
- Does the story land emotionally?
- Are there gaps in the reader's understanding that should be filled or preserved?

Reader simulation is a judgment-based evaluation. It produces observations, not mechanical findings. The author decides which observations to act on.

---

## Inputs

- **Revised manuscript:** The prose after prose editing.
- **Scene outlines:** To understand what each scene is trying to accomplish.
- **Character dossiers:** For understanding character psychology and voice.
- **Story bible:** For understanding the story's concept, themes, tone, and structure.
- **Continuity report:** To know that mechanical consistency is clean (the reader shouldn't be distracted by continuity errors).
- **Narrative architecture:** For understanding the arc structure, beat outline, and promise/payoff design.

---

## Workflow

### Step 1: Load the Manuscript and Context

Read the revised manuscript, scene outlines, character dossiers, story bible, continuity report, and narrative architecture.

Understand:
- What the story is trying to do (from the story bible)
- How it's structured (from narrative architecture)
- What each scene is trying to accomplish (from scene outlines)
- Who the characters are (from dossiers)
- That mechanical continuity is clean (from continuity report)

### Step 2: Define the Reader Persona

Decide what kind of reader to simulate. The default is a general attentive reader — someone who reads carefully, pays attention to detail, and experiences the story as a normal reader would.

If the story has a specific target audience (e.g., fans of literary horror, historical fiction readers, biblical fiction readers), the reader persona can be adjusted to reflect that audience's expectations and knowledge.

The reader persona should be defined explicitly:
- **Knowledge level:** What does this reader know about the world, the genre, the source material?
- **Expectations:** What does this reader expect from this kind of story?
- **Attention:** This reader reads carefully and notices detail.

### Step 3: Simulate the Reading

Read through the manuscript as the reader persona. Take notes on:

- **Engagement:** Where does the reader feel engaged? Where does their attention drift?
- **Confusion:** Where is the reader confused? What don't they understand? Is the confusion temporary (resolved later) or persistent?
- **Emotional response:** Where does the reader feel something — tension, dread, sadness, joy, awe, amusement? Where does the reader feel nothing?
- **Understanding:** What does the reader understand about the story, the characters, the themes? What might they misunderstand?
- **Pacing:** Where does the story feel too fast, too slow, or just right?
- **Character impression:** What is the reader's impression of each major character? Do they feel real, distinct, and compelling?
- **Theme perception:** Does the reader pick up on the story's themes? Or do the themes feel heavy-handed or invisible?
- **Ending impression:** How does the reader feel at the end? Satisfied, unsatisfied, confused, moved, bored?

### Step 4: Organize Observations

Organize the reading notes by category:

- **Engagement and attention**
- **Confusion and clarity**
- **Emotional response**
- **Character impression**
- **Theme and meaning**
- **Pacing**
- **Ending and overall impression**

Each observation should be specific:
- Where it occurs (chapter, scene, or beat)
- What the reader experiences
- Why the reader might experience it that way
- Whether it's likely intentional or accidental

### Step 5: Distinguish Observation from Recommendation

Reader simulation produces observations, not directives. The report should:

- **State what the reader experiences:** "The reader feels confused here because..."
- **Not prescribe what to do:** "You should fix this by..."

The author decides what to do with the observations. Some observations will point to real problems. Some will be matters of taste. Some will be intentional effects that the reader experiences differently than the author hoped.

### Step 6: Flag Critical Issues

Some observations are critical — they indicate problems that will undermine the story for most readers:

- **Persistent confusion:** The reader is confused about something fundamental and it's never resolved.
- **Character inconsistency:** The reader perceives a character as inconsistent in a way that breaks their understanding of the character.
- **Emotional disconnect:** The reader doesn't feel what the story is trying to make them feel, and the disconnect is caused by a fixable issue.
- **Pacing collapse:** The reader loses interest because the story drags or rushes in a way that doesn't serve the story.
- **Theme failure:** The story's themes are invisible to the reader, or so heavy-handed that they feel preachy.

Critical issues should be flagged prominently. They don't have to be fixed — the author may have reasons for them — but they should be visible.

### Step 7: Produce Reader Report

Produce a reader simulation report. The report should:

- **Be organized by the categories from Step 4.**
- **Be specific:** Reference chapters, scenes, beats, characters.
- **Distinguish observation from recommendation.**
- **Flag critical issues.**
- **Include a summary:** The reader's overall experience in a few paragraphs.

The report should be honest. If the reader was bored, say so. If the reader was moved, say so. If the reader didn't understand something important, say so. The author needs real feedback, not polite fictions.

### Step 8: Report to Orchestrator

Report completion to the orchestrator with:

- Reader persona used
- Summary of the reader's experience
- Critical issues flagged
- Overall assessment

---

## Error Handling

| Error | Response |
|---|---|
| Continuity not clean | "Reader simulation should happen after continuity is clean. If the reader is distracted by continuity errors, the simulation results will reflect those errors rather than the story's actual effects. Here are the open continuity findings: [list]. Do you want to resolve those first?" |
| Manuscript not revised | "Reader simulation is most useful after prose editing. The draft has [known issues] that the reader will encounter. Do you want to simulate the draft anyway, or wait for prose editing to complete?" |
| Reader persona unclear | "I need to know what kind of reader to simulate. The default is a general attentive reader. If this story has a specific target audience, tell me what they know and expect, and I'll adjust the persona." |

---

## Portability

- Reader simulation is a prompting pattern — any AI host can read a manuscript and produce observations about the reader's experience.
- The reader persona is defined as text, making it visible to any host.
- The report structure is text-based and can be read by any host.
- Observations are text — they don't require software tools to generate or read.

---

## Integration with Other Skills

- **Continuity** should run first. A reader distracted by continuity errors is not experiencing the story.
- **Prose editing** should run before reader simulation. The reader should experience the revised prose.
- **Prose editing** can use reader simulation feedback to target revisions.
- **The orchestrator** uses reader simulation results to decide whether the manuscript is ready for Gate 5 (export approval).

---

## Reader Persona Examples

**General Attentive Reader:**
- Reads carefully, notices detail.
- No special knowledge of the source material, genre conventions, or historical context.
- Experiences the story as it's presented.
- Default persona for most fiction.

** Genre-Savvy Reader:**
- Familiar with the genre's conventions and expectations.
- May have stronger reactions to genre tropes (expected, subverted, absent).
- Useful for genre fiction where genre expectations matter.

**Source- Familiar Reader:**
- Knows the source material (e.g., the biblical text, the historical period).
- May have stronger reactions to adaptations, departures, or interpretations.
- Useful when the story is based on known material.

**Critical Reader:**
- Reads with a critical eye, looking for flaws, inconsistencies, and weaknesses.
- More likely to notice problems, less likely to be swept away by the story.
- Useful for late-stage evaluation when the story needs stress-testing.

The reader persona should be chosen based on what the author wants to know. Different personas will produce different observations.

---

## File Outputs

- `reader-report.md` or `reader-report.json` — the reader simulation report.

---

## Evaluation

A reader simulation implementation is successful when:

1. It produces specific, honest observations about the reader's experience.
2. It distinguishes observation from recommendation.
3. It flags critical issues without exaggerating them.
4. It captures emotional response, not just mechanical analysis.
5. Different reader personas produce different, appropriate observations.
6. A different AI host could read the same manuscript and produce a comparable report (though not identical — reader simulation is judgment-based, and different hosts may notice different things).
