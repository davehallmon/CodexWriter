# Source Analysis: zenstory-ai/oh-story-claudecode

**Status:** Draft ready for review  
**Analysis date:** 2026-08-25  
**Repository:** [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)  
**Analyzed commit:** [`d1f88587c0b88abdb0a62b101b850300e0617d7b`](https://github.com/zenstory-ai/oh-story-claudecode/commit/d1f88587c0b88abdb0a62b101b850300e0617d7b)  
**Phase:** Phase 1 evidence gathering  
**Decision status:** Every CodexWriter disposition in this document is provisional. This analysis does not change `ARCHITECTURE.md` or `docs/crosswalk.md`.

## Evidence Labels

- **Observed** — directly supported by repository files, executable behavior, tests, or GitHub metadata at the analyzed commit.
- **Inference** — an architectural interpretation derived from observed evidence.
- **Uncertainty** — a question the inspected evidence does not settle, a runtime-dependent behavior, or a claim that still needs empirical validation.

---

## 1. Repository Snapshot

### Observed

| Field | Evidence |
|---|---|
| Repository | [`zenstory-ai/oh-story-claudecode`](https://github.com/zenstory-ai/oh-story-claudecode) |
| Analyzed revision | Commit [`d1f88587c0b88abdb0a62b101b850300e0617d7b`](https://github.com/zenstory-ai/oh-story-claudecode/commit/d1f88587c0b88abdb0a62b101b850300e0617d7b), the `main` head inspected on 2026-08-25 |
| Repository classification | Public, not marked as a fork |
| GitHub primary language | JavaScript |
| Implementation mix | Markdown skill/reference files plus JavaScript, Python, shell, JSON, and TOML adapters or tools |
| Repository version | `0.7.6` in the skill/plugin manifests inspected at the pinned commit |
| Specialist bundle version | `agents_version: 25` |
| Skills | 13 top-level story skills |
| Specialist agents | 7 templates: story architect, character designer, narrative writer, consistency checker, story researcher, story explorer, and chapter extractor |
| Supported environments claimed and configured | Claude Code, OpenCode, ZCode, Codex CLI, OpenClaw, Reasonix, and generic file-reading agent environments, with materially different capability levels |
| GitHub activity snapshot | 6,063 stars, 898 forks, and 9 open issues when inspected on 2026-08-25 |
| License | MIT |

The 13 skills visible in the pinned tree are:

1. `browser-cdp`
2. `story`
3. `story-cover`
4. `story-deslop`
5. `story-import`
6. `story-long-analyze`
7. `story-long-scan`
8. `story-long-write`
9. `story-review`
10. `story-setup`
11. `story-short-analyze`
12. `story-short-scan`
13. `story-short-write`

The repository presents a full Chinese web-fiction workflow rather than only a drafting prompt. Its documented path covers market scanning, source-text deconstruction, long- and short-form planning and writing, review, prose cleanup, import, cover generation, setup, and local project inspection. The [English README](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/README_EN.md), [skill router](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/SKILL.md), and [setup skill](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/SKILL.md) establish that scope.

### Inference

The project is relatively young but operationally ambitious. Its large regression suite, cross-platform matrices, explicit upgrade procedures, generated-adapter parity checks, and rapid release history indicate more engineering maturity than repository age alone would imply. Its activity level also means that any architectural conclusions are a point-in-time reading, not a stable description of a slow-moving system.

### Uncertainty

- GitHub popularity and CI breadth do not establish production correctness, long-form literary quality, or sustained use on completed novels.
- The analysis did not run a complete book workflow across every advertised runtime.
- Runtime compatibility is not uniform: some environments receive agents and hooks, while others receive skills and soft instructions only.

---

## 2. Licensing and Provenance

### Observed

- [`LICENSE`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/LICENSE) is present and contains the MIT License with a 2025–2026 copyright notice for `oh-story-claudecode`.
- `NOTICE` was not found in the pinned repository tree.
- `ATTRIBUTION.md` was not found in the pinned repository tree.
- GitHub does not classify the repository as a fork.
- The README acknowledgments name the LINUX DO community and identify `wen1701/FanqieRankTracker` as a reference for font-obfuscation decoding and `Sophomoresty/zhuque` as an external AIGC-detector self-test reference.
- No repository-wide provenance document beyond the license and README acknowledgments was found.

### Inference

The repository is usable as an architectural comparison source under MIT, but copying implementation or instruction text would still require preserving license obligations and checking the provenance of any relevant component. The acknowledgments show influence or test/reference relationships; they do not by themselves prove that particular source files were copied or derived.

### Uncertainty

- The inspected files do not establish the precise code lineage of every detector, platform scraper, reference card, or bundled prompt.
- This analysis does not determine whether the README acknowledgments are sufficient for every third-party-derived component.
- CodexWriter should treat direct implementation borrowing as a separate provenance review, even where the high-level architectural responsibility is independently reusable.

---

## 3. Architectural Thesis

### Observed

Zenstory frames long-form web-fiction production around four recurring ideas documented in the [README](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/README_EN.md):

1. reverse-engineer successful works;
2. modularize plot and emotional delivery;
3. maintain layered state for long-running stories; and
4. preserve human control over scope and progression.

Its central creative premise is that recognizable web-fiction patterns can be decomposed into reproducible emotional and structural modules. The system then combines:

- workflow skills that route user intent;
- specialist agents with constrained responsibilities;
- a large on-demand methodology/reference library;
- deterministic tracking and validation scripts;
- runtime hooks that enforce selected preconditions;
- human stop points before expensive or consequential transitions; and
- local files as the project interface.

The long-form project separates several authority domains:

| Domain | Primary artifact class |
|---|---|
| Manuscript truth | Chapter prose under the manuscript directory |
| Planned content | Book, volume, and chapter-outline files |
| Static world/character setup | Markdown files under settings directories |
| Current dynamic continuity state | `_tracking-state.json` |
| Bounded prompt-facing state | Deterministically derived Markdown views |
| Author preferences | Separate workspace-level author-memory JSON plus derived views |
| Benchmark/deconstruction knowledge | Structured Markdown artifacts with explicit local precedence rules |

### Inference

The primary organizing principle is not “one file is canon.” It is a **layered, domain-specific authority model with one machine authority inside each transactional subsystem**. The most distinctive design move is to keep the per-book structured tracking authority out of prose prompts and expose bounded, reproducible projections instead.

Zenstory also treats creative craft and operational correctness as different layers. Models make semantic and literary judgments; scripts enforce schemas, revisions, file derivations, byte budgets, path safety, and selected surface heuristics.

### Uncertainty

- The repository does not define a single universal precedence rule that mechanically resolves every disagreement among manuscript prose, static settings, outlines, and dynamic tracking state.
- The files examined specify many responsibilities, but instruction-following remains model- and runtime-dependent where no hook or script enforces the contract.
- The architecture is strongly tuned to Chinese commercial web fiction; its thesis may not transfer unchanged to other fiction forms.

---

## 4. Workflow and Orchestration

### Observed

#### 4.1 Entry points and routing

The [`story` router](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/SKILL.md) directs explicit or inferred intent to specialized skills. The bundle distinguishes scanning, analyzing, writing, importing, reviewing, prose cleanup, cover work, setup, and browser-assisted acquisition.

The [`story-long-write` skill](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/SKILL.md) recognizes materially different scenarios:

- opening a new book;
- writing a specified chapter or range;
- expanding outlines without drafting prose;
- daily continuation; and
- revising an earlier chapter.

A bare invocation diagnoses project state and presents routes. It does not authorize autonomous prose generation. Drafting requires an explicit chapter or range; the normal default is one chapter, the daily path may handle two or three, and a single turn is capped at three.

#### 4.2 Long-form setup and writing

Opening a book runs planning phases and stops after the initial detailed-outline tranche by default. It does not proceed into prose unless the user explicitly requests prose. The chapter workflow requires a matching detailed outline, assembles bounded context, recalls relevant craft references and author preferences, confirms intent where required, delegates prose to the narrative specialist when available, runs machine checks, writes metadata, commits tracking state, and validates before continuing.

The daily continuation path is serial. A chapter is drafted, checked, and committed before the next chapter begins. Parallel chapter drafting is explicitly disallowed because every chapter depends on the committed state produced by the previous one.

#### 4.3 Deconstruction pipeline

The [`story-long-analyze` skill](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-analyze/SKILL.md) defines one staged pipeline:

| Stage | Function | Key handoff |
|---:|---|---|
| 0 | Identify chapters and create a thin overview | A single chapter-boundary table becomes the downstream slicing authority |
| 1 | Deeply analyze the opening three chapters | Produce a quick-preview artifact and normally stop for user confirmation |
| 2 | Produce per-chapter summaries | May parallelize independent chapter extraction |
| 3 | Aggregate plot, rhythm, emotion, and reusable modules | Establishes explicit authority among analysis outputs |
| 4 | Build settings, characters, and relationships | Some setting work can overlap Stage 3; later character work waits for merged identities |
| 5 | Produce the complete deconstruction report | May offer a clearly marked hypothesis backfill to a topic-decision artifact |
| 6 | Produce a bounded style profile | Failure is recorded but does not invalidate the earlier analytical stages |

The normal stop after Stage 1 is a material human gate. A user who explicitly requests a complete uninterrupted analysis can waive that stop at the outset.

#### 4.4 Specialist role boundaries

| Agent | Observed boundary |
|---|---|
| `story-architect` | Macro structure, outlines, hooks, and emotional architecture; may write planning artifacts |
| `character-designer` | Character design, relationships, and dialogue guidance; may write character artifacts |
| `narrative-writer` | Chapter prose, formatting, and anti-pattern checks; does not own tracking-state commits |
| `consistency-checker` | Read-only continuity audit with severity-ranked findings; explicitly avoids literary judgment |
| `story-explorer` | Read-only bounded retrieval and state/context assembly; no creative or state-write authority |
| `story-researcher` | External factual research; writes new reference files, uses multiple sources, and does not edit existing story artifacts |
| `chapter-extractor` | Read-only per-chapter extraction for parallel deconstruction; no critique or story mutation |

The main session remains the coordinator and owns the state transaction after a narrative agent writes prose.

#### 4.5 Stop conditions and fallbacks

- Missing primary contracts fail fast rather than silently substituting approximate files.
- A failed or stale tracking transaction stops progression until the transaction is corrected and the tracking check passes.
- Unsupported or missing custom-agent capability falls back to solo/direct execution and should be reported.
- Full and lean review modes fall back to solo if required agents cannot be used; partial multi-agent output is not labeled as a complete full/lean run.
- Imports stop for ambiguity about source length, incomplete endings, or volume boundaries.
- Earlier-chapter revision stops for a user choice between full and targeted rewriting, then reports downstream impact for a further user decision.

### Inference

Zenstory has a clearer separation between orchestration, prose generation, read-only retrieval, read-only continuity review, and deterministic state mutation than either a monolithic writing prompt or a collection of uncoordinated skills. It also uses stop conditions as part of the architecture, not merely conversational etiquette.

The staged deconstruction pipeline is a useful example of dependency-aware orchestration: independent extraction can parallelize, but aggregation and identity reconciliation remain ordered.

### Uncertainty

- Agent boundaries are only as strong as the host runtime's tool and agent enforcement. Skills-only installations provide weaker isolation.
- The repository documents fallback behavior, but this analysis did not exercise every fallback on every supported CLI.
- It is not established whether the orchestration density improves results enough to justify its ongoing maintenance and prompt cost.

---

## 5. State Storage Model

### Observed

#### 5.1 The project is layered, not globally centralized

Static settings, outlines, and prose remain author-readable Markdown. Long-form dynamic continuity is stored separately. The [`state-tracking` reference](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/state-tracking.md) limits dynamic tracking to facts whose absence could materially cause the next chapter to be written incorrectly.

Within the tracking subsystem, `_tracking-state.json` is the sole structured authority. The hot context, foreshadowing view, timelines, chapter records, and per-character snapshots are generated views or bounded records. The system does not parse those Markdown views back into canonical state.

That statement has a defined scope: `_tracking-state.json` is not the only authority for the entire book. Prose, static settings, and outlines remain primary artifacts in their own domains.

#### 5.2 Per-book state schema

The pinned demo state and [`tracking_commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/scripts/tracking_commit.py) implement schema version 4 with these top-level categories:

- book title;
- current character snapshots;
- bounded context;
- foreshadowing entries;
- imported-through chapter;
- last committed chapter;
- schema version; and
- monotonically increasing state revision.

Character snapshots include identity, location, current goal and condition, abilities or resources, relationships, knowledge, and open threads. Foreshadowing records include identity, summary, planting/resolution locations, status, and importance. Timeline entries distinguish objective author truth from what the reader currently knows and record reveal state and chapter references. Context carries current position, active characters, long-term constraints, continuity risks, recent chapters, and next-chapter commitments.

The implementation validates known keys and reference integrity. The current schema has no dedicated first-class entity for an open story question or for a promise/payoff pair. Those concepts can be approximated through open threads, foreshadowing, context commitments, or outlines, but they do not receive Dewhurst-style typed records.

#### 5.3 Derived views and bounded records

The transaction code deterministically renders:

- `Context.md` as the hot prompt-facing state;
- `Foreshadowing.md`;
- an author-truth timeline;
- a reader-known timeline; and
- one dynamic snapshot per active character.

It also writes a per-chapter record. The explicit budgets are:

| Artifact | Target | Hard maximum |
|---|---:|---:|
| Hot context | 8,192 bytes | 12,288 bytes |
| Chapter record | 1,536 bytes | 3,072 bytes |
| Character snapshot | 4,096 bytes | 8,192 bytes |

The default hot-context selection also limits active characters to six, active foreshadowing items to eight, and recent chapters to three.

#### 5.4 Transaction protocol

The [`tracking transaction guide`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/tracking-transaction.md) and implementation require all tracking writes to pass through `tracking_commit.py`; direct hand editing is prohibited by the workflow.

For an append transaction, the tool:

1. reads and normalizes the current authority;
2. validates the expected revision and next chapter;
3. merges the submitted semantic changes in memory;
4. enforces schema, references, explicit retirements, and byte limits;
5. writes the chapter record;
6. writes all derived Markdown views and character snapshots;
7. removes orphaned character snapshots; and
8. atomically replaces `_tracking-state.json` last as the commit point.

Each file replacement uses a same-directory temporary file, flush and filesystem sync, and `os.replace`. The transaction as a whole is not a filesystem-wide atomic operation. A derived-view write can succeed before a later write fails. In that case the JSON authority remains at the old revision, the `check` command detects drift, and rerunning the same transaction can repair the projections.

The expected revision rejects a transaction prepared from stale state. It is explicitly a sequential stale-write guard, not a lock. The project requires one serial writer per book and does not support multiple agents or terminals committing story state concurrently.

#### 5.5 History and revision behavior

The state model stores the current snapshot plus bounded chapter records. It is not an event-sourced replay log.

The [`earlier-chapter revision workflow`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/workflow-revision.md) requires the agent to inspect the revised chapter and all affected material through the latest chapter, recalculate impacted character, foreshadowing, and timeline values, and submit their current values in one `mode=revision` transaction. The script validates and merges the supplied current values. It does not mechanically replay chapters after the revised chapter or derive new state directly from manuscript prose.

An old-chapter revision preserves the existing next-chapter commitments unless the latest chapter itself is revised. Current rows retain their later update chapter rather than moving that marker backward. After the state commit, the workflow scans later prose and reports potentially affected chapters; the user decides whether to revise them.

Imported works use an `imported_through_chapter` cutoff. The importer does not invent historical deltas for imported chapters. Older tracking layouts are archived verbatim and a current state is reinitialized; they are not semantically migrated into a replayable history.

#### 5.6 Authority and conflict behavior

| Conflict | Observed behavior |
|---|---|
| `_tracking-state.json` vs. a derived tracking Markdown view | JSON wins; `check` reports byte-level drift and the view must be regenerated through a valid transaction |
| Current state vs. a stale transaction | Transaction is rejected when `expected_state_revision` does not match |
| Current state vs. prose semantics | No universal deterministic resolver; the workflow and consistency review inspect prose, then a revision transaction corrects state if needed |
| Static profile vs. dynamic snapshot | Static profile remains under settings; dynamic snapshot represents current conditions. The workflow loads both for relevant characters |
| Outline vs. prose creation | Runtime guards can block creation of a new prose chapter without the required outline; outlines constrain content but do not prescribe paragraph shape |
| Benchmark analysis artifacts | Rhythm and emotion-module files have explicit authority over summary projections; a project-specific style file outranks benchmark style guidance |
| Author memory vs. current request/book contract | Author memory is subordinate to hard gates, the current request, and current book settings/style/outline |

The deterministic `check` establishes that views faithfully reflect JSON and that the tracking structure is internally valid. It does not prove that the JSON accurately describes the manuscript.

#### 5.7 Separate author-preference memory

The 0.7.6 head includes a second transactional subsystem for cross-session author preferences. The [`author-memory reference`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/references/author-memory.md) and [`author_memory_commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/scripts/author_memory_commit.py) store workspace-level preferences under `.story/作者记忆`.

This subsystem has its own JSON authority, revision counter, idempotent transaction identifiers, state-last writes, derived profile/pending/journal views, conflict states, and explicit remember/confirm/replace/forget operations. It does not log every message. Inferred or repeated preferences remain pending until promoted. Queries return only active relevant items under a 2,048-byte cap and create nothing when no memory exists.

The stated precedence is:

1. hard safety/workflow gates;
2. the current user request;
3. current book settings, style, and outline;
4. book-specific author memory;
5. genre, workflow, and global author memory; and
6. benchmark or generic defaults.

Author memory is explicitly separate from story facts and canon.

#### 5.8 Exploratory and non-canonical material

Benchmark texts, deconstruction output, market scans, references, and story prose/settings are stored in distinct directories. The deconstruction pipeline also defines authority among its own aggregated outputs.

However, the examined state contracts do not expose a first-class `canonical`, `candidate`, or `sandbox` status for speculative story facts. Promotion from exploration into book settings, outline, prose, or tracking is mainly a workflow responsibility.

### Inference

Zenstory answers Dewhurst's distributed-state ambiguity only **inside the dynamic tracking subsystem**. It offers a strong, testable rule—JSON authority and disposable projections—without trying to collapse the whole creative project into one database. This hybrid boundary is more precise than describing Zenstory as either purely centralized or purely file-distributed.

The state-last protocol is a pragmatic recoverability design. It keeps the canonical revision from advancing unless all preceding writes succeed, but it relies on `check` plus idempotent retry rather than rollback or a journaled multi-file transaction.

The separate author-memory authority is a valuable isolation boundary: user preference can persist without becoming fictional fact. Its precedence ladder is more explicit than the book-state precedence among prose, outlines, static settings, and dynamic state.

### Uncertainty

- Semantic transaction content is produced by an agent or user workflow. Structurally valid JSON can still encode a mistaken interpretation of the prose.
- The chapter records are not demonstrated to contain enough information to reconstruct every historical state mechanically.
- Revision propagation is workflow-guided recalculation, not deterministic replay; correctness depends on the agent's inspection of chapters from the revision point through the current endpoint.
- The expected revision protects sequential commits but does not solve true concurrent writers, filesystem races, or distributed synchronization.
- The transaction code intentionally allows temporary derived-view drift after a partial failure; recovery is tested, but automatic rollback is absent.
- The analysis did not establish a universal rule for deciding whether prose or tracking is correct when they disagree semantically.
- The new author-memory subsystem was introduced at the pinned head and has tests, but its long-term field behavior is not yet observable from the repository alone.

---

## 6. Context Management

### Observed

Zenstory's stated context principle is relevance under consequence: load an item when omitting it could cause the current chapter to be written incorrectly. The long-form workflow intentionally excludes the complete `_tracking-state.json` from the prose prompt. It loads bounded projections instead.

The hot context has a fixed seven-section shape and a 12 KiB hard cap. Per-character snapshots and chapter records have separate caps. The daily workflow uses a retrieval ladder:

1. hot context;
2. one directly relevant line or current character snapshot;
3. the read-only story explorer;
4. search across a bounded recent set of chapter records;
5. one selected historical record or prose chapter; and
6. broader inspection only through a deliberate analysis/revision path.

Routine continuation avoids scanning the complete manuscript. Fixed context does not grow linearly with chapter count. Far-field material is accessed through bounded records, entity snapshots, indexes, search, or a specialist query agent.

The writing workflow typically combines:

- the target detailed outline;
- adjacent outline/prose context where required;
- `Context.md`;
- relevant static and dynamic character files;
- applicable setting rules;
- selected genre/craft cards;
- benchmark rhythm, emotion, or style guidance under explicit precedence; and
- relevant author-memory items under a 2 KiB cap.

State/context revision mismatch is a stop condition. When prose and state may disagree, continuity inspection or revision workflow is required; the system does not silently treat a summary as proof against the manuscript.

Cross-agent handoff is role-specific. The narrative writer receives the outline, bounded context, applicable style/craft constraints, and explicit output contract. It does not receive state-write authority. The story explorer returns compact query results rather than mutating files. Review agents receive a common rubric and return normalized findings.

The release process includes a [`doc-budget`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/doc-budget.json) policy and CI check so expanding always-loaded instructions becomes an explicit review decision. The [0.7.6 changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/CHANGELOG.md) records further reductions in duplicated always-loaded workflow text.

### Inference

This is the strongest explicit long-context strategy among the first three sources. It combines bounded state projections, near/far retrieval, deterministic size enforcement, on-demand methodology, and a read-only query role. The design recognizes that context selection is an architectural concern rather than an instruction to “read the relevant files.”

Excluding canonical JSON from the prose prompt also reduces accidental model edits and prevents raw machine structure from consuming the full budget. Deterministically reproducible views make prompt context inspectable without turning those views into a competing authority.

### Uncertainty

- Byte caps control size, not relevance. An agent still decides which semantic facts survive into bounded state and which far-field items to retrieve.
- A 12 KiB hot context may omit low-salience facts that become important unexpectedly.
- The repository tests format and budget behavior more readily than whether the selected context was narratively sufficient.
- Performance and quality at extreme manuscript length were not independently benchmarked in this analysis.

---

## 7. Creative-Craft Model

### Observed

Zenstory contains a deep, opinionated Chinese web-fiction craft layer. Its methodology emphasizes:

- emotional payoff before abstract thematic completeness;
- patterns learned from successful comparable works;
- modular plot, conflict, hook, rhythm, and payoff design;
- detailed outlines as content contracts;
- freedom for prose to rearrange and interweave outline beats rather than transcribe their list shape;
- chapter-end hooks, escalation, expectation, release, and after-effect;
- commercial-platform conventions and genre-specific cards;
- measurable prose checks such as character count, title duplication, repeated patterns, and outline-copy overlap; and
- stylistic de-AI heuristics and punctuation/format normalization.

The deconstruction pipeline produces authoritative rhythm and emotion-module artifacts, character and setting analyses, a story-level report, and a bounded style profile. The long-writing workflow retrieves these artifacts on demand rather than loading the entire methodology library.

The narrative-writer agent owns prose realization. The current agent template can run machine word-count and sentence-length checks and is explicitly told that the outline controls required content, not paragraph-by-paragraph shape. A project-specific style file has higher authority than benchmark-derived style. The changelog documents regressions discovered when the prose agent lacked tools needed to execute its own quality contract, and the corresponding template/tool corrections.

The review and prose-cleanup paths distinguish evidence-producing detectors from editorial judgment. The outline-copy detector reports overlap but does not automatically rewrite legitimate fixed phrases or story-internal quoted material.

### Inference

Zenstory's strongest contribution beyond state engineering is its connection between market analysis, benchmark decomposition, planning modules, prose instructions, and post-draft checks. It is much more craft-prescriptive than Dewhurst and more operationally integrated than a responsibility taxonomy alone.

The architecture treats creative quality as a mixed system: some surface properties are measured, while emotional causality, scene effectiveness, voice, and narrative judgment remain model tasks.

### Uncertainty

- The craft model is optimized for Chinese commercial web-fiction platforms and may overfit pacing, hook density, tropes, prose texture, or chapter economics that do not suit literary fiction or other markets.
- Anti-AI heuristics can detect selected patterns but cannot establish naturalness, originality, or artistic quality.
- Benchmark imitation and platform optimization can create homogenization pressure if not subordinated to the author's intent.
- This analysis inspected rules and tests, not a blind evaluation of generated novels.

---

## 8. Evaluation and Continuity

### Observed

#### 8.1 Deterministic tracking checks

`tracking_commit.py check` validates:

- schema and reference integrity;
- chapter-record presence after the import cutoff;
- canonical record filenames;
- size limits;
- exact correspondence between JSON state and rendered views; and
- the exact set of character snapshot files.

The [`tracking transaction tests`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/test-tracking-commit.py) cover initialization, derived views, warning and rejection thresholds, stale revisions, partial-write recovery, old-chapter revisions, import cutoffs, edited views, orphan files, retired-layout archival, explicit retirement, zero-mutation failure cases, and path edge cases.

These checks validate a data contract. They do not infer fictional truth from prose.

#### 8.2 Runtime guards and prose detectors

The shared [`story_hook_core.js`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/references/templates/hooks/story_hook_core.js) and runtime adapters inspect attempted prose writes. Depending on host capability, they can block a new chapter when:

- its detailed outline is missing;
- tracking state is missing, malformed, or on the wrong schema;
- the hot context revision disagrees with state;
- the chapter sequence is invalid; or
- unresolved prior-chapter deterministic quality debt crosses a configured gate.

The write-path parser covers direct write/edit tools and several common shell redirection/copy/move forms. The changelog explicitly states that this is static recognition, not a shell sandbox.

After prose changes, detectors report issues such as truncation, leaked workflow language, duplicate titles, word-count shortfalls, deterministic AI-like patterns, degeneration patterns, and excessive outline copying. The Codex adapter lacks an equivalent post-tool event, so its stop hook performs an advisory rescan rather than a hard post-write block.

#### 8.3 Review model

The [`story-review` skill](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-review/SKILL.md) is a read-oriented coordinator whose purpose is to find problems rather than certify correctness. It offers:

- full mode: architect, character, narrative, and consistency reviewers;
- lean mode: architect and consistency reviewers; and
- solo fallback.

Reviewers use a common S1–S4 severity scheme and normalized finding structure. The report records requested mode, effective mode, fallback reason, rubric, and rubric source. Reviewer disagreement is preserved for the user rather than collapsed into an automatic compromise. Multi-batch review keeps a separate `.story-review/state.md` so unresolved findings carry forward.

Review does not directly rewrite prose. Automated prose cleanup is routed to `story-deslop`. Full/lean review may correct tracking only through the transaction tool and only when prose evidence shows the existing tracking record is wrong or incomplete; solo review does not mutate tracking.

#### 8.4 Continuity role

The consistency-checker is read-only and uses search-first inspection plus model reasoning. It classifies continuity findings without acting as a prose critic. Author-truth and reader-known timelines give it a useful epistemic distinction, but the system has no dedicated reader-simulation agent comparable to Lensetek's explicit reader-facing role.

### Inference

Zenstory draws an unusually clear line between:

- mechanical integrity;
- heuristic prose evidence;
- semantic continuity judgment; and
- repair authority.

That boundary reduces false claims that a script can prove narrative correctness. The combination of state checks, runtime gates, independent reviewers, and explicit audit/repair separation is stronger than relying on one final “review this chapter” prompt.

### Uncertainty

- Model reviewers can still miss contradictions or agree on a mistaken reading.
- Static write-path guards can be bypassed by unrecognized commands or unsupported runtimes.
- Heuristic detectors may generate false positives or false negatives and do not constitute a literary-quality metric.
- Review-state persistence is separate from story truth; the repository does not demonstrate a unified issue lifecycle from finding through verified repair.
- Platform rubrics approximate market-reader response but do not replace explicit reader simulation.

---

## 9. Human-in-the-Loop Model

### Observed

Zenstory includes human gates at meaningful scope transitions:

- setup asks which runtime and deployment target should be used and resolves multi-environment ambiguity;
- opening a book stops after planning by default and does not draft prose without explicit authorization;
- a bare writing invocation diagnoses options rather than continuing autonomously;
- requested prose scope is explicit and capped;
- long-form deconstruction normally stops after the first three chapters for a continue/stop decision;
- importing asks the user to resolve length/type, an incomplete final chapter, and ambiguous volume boundaries;
- revision asks whether to replace the full chapter or selected passages;
- downstream chapters affected by a revision are reported for user choice rather than rewritten automatically;
- conflicting review findings are surfaced for user judgment; and
- external topic-decision backfill requires confirmation when the target file is outside the current project or ambiguous.

Inside an authorized chapter task, the system may apply deterministic formatting normalization, tracking updates, and configured checks without seeking approval for every individual change. Current-state semantics are generally agent-produced and transaction-validated rather than individually human-approved after each chapter.

### Inference

The HITL model is strongest at **scope, canon-affecting revision, long-running work, and ambiguity boundaries**, not at every low-level artifact write. This is a practical balance for a serial workflow.

The earlier-chapter revision path properly separates “update current state” from “rewrite all affected later prose.” That preserves author control even though it also leaves more work to human/model review.

### Uncertainty

- Canon promotion from exploratory ideas is not represented by a dedicated machine state or universal confirmation protocol.
- Users may not understand which automated edits or tracking mutations occur inside a broadly authorized writing/review command.
- The strength of interactive gates varies by runtime and whether the host exposes the expected question/agent APIs.

---

## 10. Runtime and Maintenance

### Observed

#### 10.1 Setup and capability detection

The [`story-setup` skill](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/SKILL.md) validates its reference bundle before writing, detects the target environment, merges rather than wholesale-overwrites user configuration, and records deployment metadata in `.story-deployed`. It treats user story state as create-only while replacing managed bundle assets and merging marked configuration sections.

Setup checks canonical paths to avoid copying a bundle into itself or creating recursive nesting. It validates the resulting installation and refuses to deploy an older bundle over a project marked with a newer agent version. Upgrades require redeployment and, when agent templates change, a fresh session.

#### 10.2 Capability matrix

| Runtime | Observed deployment behavior |
|---|---|
| Claude Code | Skills, specialist agents, and hooks; strongest enforcement path |
| OpenCode | Skills, specialist agents, and generated hook/plugin adapter |
| Codex CLI | Skills through `.agents/skills`, TOML specialist agents, Python hook adapter, and launch/config assets; fresh-session/trust requirements apply |
| ZCode | Skills and limited hooks; documented runtime version does not execute project custom agents or all lifecycle hooks |
| OpenClaw | Skills-only fallback; no custom agent/hook enforcement |
| Reasonix | Skills and manifest; no custom-agent/hook enforcement in the examined path |
| Generic environment | Skills plus project instructions; contracts are soft and execution is solo/direct |

The system explicitly reports solo fallback when custom agents are missing or unavailable. Version mismatch is advisory if files exist; actual absence of an agent or registry triggers fallback.

#### 10.3 Runtime dependencies

- Node.js is used for hooks, detectors, the dashboard, and several acquisition/normalization tools.
- Python 3 is used for state and author-memory transactions plus selected checks.
- Shell scripts support installation and adapters on Unix-like environments; Windows-specific paths and launchers are also maintained.
- Browser/CDP capability is used for market scanning.
- The dashboard binds locally to `127.0.0.1`, edits project files, checks modification times before overwriting, and is documented as not uploading story content.

There is no single package manifest that completely describes every runtime dependency for the full skill suite. The host CLI plus available Node, Python, shell, browser, and filesystem capabilities determine the actual feature set.

#### 10.4 CI and maintenance controls

The repository includes:

- [cross-platform CI](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/cross-platform.yml) across Ubuntu, Windows, and macOS for critical state, memory, continuity, detector, hook, and deployment paths;
- [CLI compatibility CI](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/cli-compat.yml) that installs current supported CLIs and checks discovery/adapters;
- [dashboard CI](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/dashboard.yml) with API and browser tests;
- byte-parity checks for generated/shared copies listed in [`shared-assets.json`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/shared-assets.json);
- context-document budgets enforced in CI; and
- a detailed [changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/CHANGELOG.md) with upgrade effects and regression narratives.

The state implementation's tests include explicit failure injection and recovery behavior, not only happy-path snapshots.

### Inference

Zenstory treats prompt bundles, runtime adapters, state scripts, and deployment outputs as a versioned software product. Its maintenance practices are a strong counterexample to treating skills as static Markdown.

The shared-source/parity-check approach mitigates runtime duplication but does not eliminate it. Every supported host expands the regression surface, especially when lifecycle events differ.

### Uncertainty

- Compatibility can drift immediately when external CLIs change despite scheduled CI.
- Host trust settings, symlink behavior, Python executable discovery, Node availability, and shell semantics remain environment-specific failure points.
- Some documented hard gates degrade to advisory or soft instructions on runtimes without equivalent hooks.
- Rapid releases and an expanding adapter matrix may impose substantial maintainer cost.

---

## 11. Strengths

### Observed

1. **Scoped machine authority.** Dynamic tracking has one structured source of truth, while prompt-facing Markdown is deterministically derived and checked.
2. **Bounded context as an enforced contract.** Hot context, chapter records, character snapshots, active entities, and author-memory queries all have explicit limits.
3. **Sequential stale-write protection.** State revisions prevent a transaction prepared from silently outdated state from committing.
4. **Recoverable failure design.** The state-last commit point and retry tests handle partial derived-view writes without advancing canonical state.
5. **Author truth vs. reader knowledge.** Separate timelines model information asymmetry directly.
6. **Static vs. dynamic character separation.** Stable profiles and current snapshots are not conflated.
7. **Author memory isolation.** Preferences have a separate authority, lifecycle, budget, and precedence from story facts.
8. **Strong role boundaries.** Prose generation, state mutation, bounded retrieval, external research, and continuity review are distinct responsibilities.
9. **Audit/repair separation.** Review reports findings; another workflow applies prose changes. Tracking corrections still use the transaction boundary.
10. **Human stop points.** Planning, long analysis, import ambiguity, revision scope, and downstream impact have explicit gates.
11. **Deep craft pipeline.** Market scan, deconstruction, emotion/rhythm modules, outline design, prose realization, and quality checks form a connected system.
12. **Operational rigor.** Cross-platform tests, CLI compatibility checks, failure injection, shared-asset parity, and document budgets are unusually comprehensive for a skill repository.

### Inference

Zenstory is the strongest first-three-source example of a **control plane around creative work**: it bounds context, gates state mutation, detects stale writes, separates agents by authority, and continuously checks the deployment artifacts that make those contracts real.

### Uncertainty

The repository evidence shows disciplined mechanisms. It does not prove that every mechanism improves story outcomes or that their combined complexity is appropriate for CodexWriter.

---

## 12. Weaknesses / Gaps

### Observed

1. **No universal story authority.** `_tracking-state.json` governs dynamic tracking, not every setting, outline, and prose fact. Cross-domain conflicts still require interpretation.
2. **Semantic state remains model-authored.** Schema checks cannot determine whether extracted facts accurately represent prose.
3. **No automatic downstream replay.** Revising an older chapter requires agent-led recalculation through the latest chapter; the script does not replay later events.
4. **No true multi-writer support.** Expected revisions reject stale sequential updates but provide no lock or concurrency protocol.
5. **Not a whole-transaction atomic commit.** Individual replacements are atomic, but a mid-transaction failure can leave some derived files ahead of canonical state until repair.
6. **History is incomplete for reconstruction.** Current snapshots plus bounded chapter records are not presented as a sufficient event log.
7. **No first-class questions or promises/payoffs.** Foreshadowing and open threads cover related concerns but with less typed semantics than Dewhurst.
8. **Imported history is cut over, not reconstructed.** Old layouts are archived and imported chapters do not receive invented deltas.
9. **No first-class exploratory/canon promotion state.** Directory separation exists, but candidate facts are not uniformly modeled.
10. **No dedicated reader-simulation role.** Market rubrics and review approximate reader response without an explicit reader-agent contract.
11. **Runtime enforcement is uneven.** Some platforms receive hard guards and agents; others receive skills-only soft behavior.
12. **Domain specificity.** The craft system is strongly shaped by Chinese commercial web-fiction conventions and platforms.
13. **Instruction and adapter complexity.** Large prompt contracts, generated copies, host adapters, and many references create synchronization and regression risk, even with CI.
14. **Surface detectors have limited epistemic reach.** Word counts, pattern matches, and exact derived-view checks cannot certify causality, voice, or continuity truth.

### Inference

The largest architectural risk is not centralization itself but **false confidence at the boundary between validated structure and unvalidated semantics**. A successful transaction means the state is well-formed and internally synchronized, not that it is narratively correct.

The second risk is portability. Zenstory's strongest behavior depends on setup, trusted project configuration, available hooks, Python/Node, and disciplined serial execution. A skills-only copy retains much of the instruction text but loses important control-plane guarantees.

### Uncertainty

- It is unclear how often the bounded context omits a fact that later causes a continuity error.
- It is unclear how users recover from a semantically wrong but structurally valid canonical state at very large scale.
- Long-term maintenance cost across all supported CLIs cannot be inferred from the current test suite alone.

---

## 13. Relevance to CodexWriter

All items in this section are **provisional Phase 1 candidates**, not architecture decisions.

### Observed reusable responsibilities

| Source responsibility | CodexWriter relevance |
|---|---|
| Intent router with bounded workflow scopes | Supports an orchestrator that diagnoses, delegates, and stops at explicit boundaries |
| Dedicated narrative writer | Reinforces prose generation as distinct from planning, state mutation, and review |
| Read-only story explorer | Identifies bounded retrieval/context assembly as a first-class responsibility |
| Read-only consistency checker | Reinforces separation between continuity audit and prose repair |
| Transactional state writer | Identifies deterministic state mutation as a tool/control-plane responsibility rather than a prose-agent side effect |
| Static/dynamic character separation | Gives character/world responsibilities a clearer time-sensitive boundary |
| Author-truth and reader-known timelines | Supports narrative epistemology and POV-aware continuity |
| Separate author memory | Separates persistent user preference from story canon |
| Long-form analysis pipeline | Connects benchmark decomposition to planning without treating source imitation as prose generation |
| Runtime setup and capability detection | Identifies installation, migration, doctor, compatibility, and update behavior as operational responsibilities |
| Deterministic prose evidence tools | Supports narrow machine checks without overstating literary validation |
| Review coordinator with normalized findings | Supports auditable multi-perspective evaluation and explicit fallback metadata |

### Provisional candidate architectural borrowing

- **Adapt candidate:** one authoritative machine representation within a clearly bounded state subsystem, with deterministic human-readable projections.
- **Adapt candidate:** state revision numbers and expected-revision checks for stale sequential writes.
- **Adapt candidate:** bounded hot context plus entity snapshots and an escalation ladder for far-field retrieval.
- **Adapt candidate:** author truth and reader knowledge as separate timeline dimensions.
- **Adapt candidate:** author preference memory as an explicitly separate authority with a precedence ladder and query budget.
- **Adapt candidate:** narrative agents do not directly mutate canonical tracking state; a deterministic transaction tool owns that boundary.
- **Adapt candidate:** state-integrity checks are distinct from semantic continuity review.
- **Adapt candidate:** every multi-agent review records effective mode and fallback rather than implying unavailable reviewers ran.
- **Adapt candidate:** runtime capabilities and enforcement degradation are surfaced explicitly.
- **Adapt candidate:** context/instruction budgets are reviewed and enforced like other software budgets.

### Provisional implementation-level borrowing requiring license/provenance handling

- The transaction schema, merge rules, derived renderers, file-write sequence, recovery behavior, and tests.
- Author-memory transaction code and its idempotency/conflict lifecycle.
- Hook parsers and runtime-specific adapters.
- Prose detectors, normalizers, scrapers, dashboard code, or test fixtures.
- Skill/reference text, agent templates, and genre/platform methodology.

The MIT license permits broad reuse subject to its conditions, but any direct reuse should preserve licensing and receive file-level provenance review.

### Provisional patterns to avoid

- Avoid describing one subsystem's JSON authority as the universal story canon.
- Avoid treating a successful structural check as evidence that prose and state agree semantically.
- Avoid adopting state-last multi-file writes without documenting partial-view recovery and the absence of whole-transaction atomicity.
- Avoid calling a revision counter a concurrency solution.
- Avoid assuming later-state recalculation is deterministic when an agent performs the semantic reconstruction.
- Avoid coupling CodexWriter's general craft model to one commercial market or language.
- Avoid claiming cross-runtime parity where hooks or custom agents are unavailable.
- Avoid copying a large multi-runtime adapter surface before CodexWriter has evidence that each environment is in scope.

### Inference

Zenstory most strongly supports a provisional split between creative responsibilities and deterministic control-plane responsibilities. It does not by itself decide whether CodexWriter should store canon in JSON, Markdown/YAML, a database, or a hybrid. It does show which contracts a chosen storage model may need: authority scope, revision identity, bounded projections, explicit repair, semantic audit, and runtime-visible failure behavior.

### Uncertainty

- The correct CodexWriter storage representation remains open pending later sources and synthesis.
- Whether state mutation should be one tool, several domain-specific tools, or an orchestrator service remains open.
- Whether the story-explorer responsibility warrants a named skill or is an internal context-service concern remains open.

---

## 14. Detailed Evidence

### Observed: primary evidence index

All links in this table are pinned to the analyzed commit unless they point to repository metadata.

| Area | Evidence | What it establishes |
|---|---|---|
| Overview | [`README_EN.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/README_EN.md) | Product scope, workflow pillars, project layout, runtime claims, tracking/context overview, local dashboard claims |
| License | [`LICENSE`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/LICENSE) | MIT license text |
| Release history | [`CHANGELOG.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/CHANGELOG.md) | Recent regressions, upgrade behavior, agent bundle version, context reductions, detector and hook limitations |
| Top-level routing | [`skills/story/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/SKILL.md) | Intent routes, global workflow, author-memory integration |
| Long writing | [`skills/story-long-write/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/SKILL.md) | Scenario routing, stop rules, project artifacts, context limits, state authority, chapter scope |
| Daily continuation | [`workflow-daily.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/workflow-daily.md) | Serial chapter execution, bounded retrieval ladder, per-chapter transaction requirement |
| Chapter workflow | [`workflow-chapter.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/workflow-chapter.md) | Detailed prose pipeline and machine checks |
| Revision | [`workflow-revision.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/workflow-revision.md) | Old-chapter revision, recalculation, stale retry, downstream impact report |
| State design | [`state-tracking.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/state-tracking.md) | Static/dynamic split and relevance rule |
| State transaction contract | [`tracking-transaction.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/references/tracking-transaction.md) | Sole structured authority, derived views, serial writes, revision behavior, recovery instructions |
| State implementation | [`tracking_commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-write/scripts/tracking_commit.py) | Actual schema normalization, merge rules, byte limits, file ordering, atomic replacements, checks |
| State tests | [`test-tracking-commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/test-tracking-commit.py) | Tested stale-write, failure, recovery, revision, cutoff, and view-drift behavior |
| Demonstration state | [`_tracking-state.json`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/demo/%E9%95%BF%E7%AF%87/%E8%AE%A9%E4%BD%A0%E7%AE%A1%E8%B4%A6%E5%8F%B7%EF%BC%8C%E4%BD%A0%E9%AB%98%E7%87%83%E6%B7%B7%E5%89%AA%E7%82%B8%E5%85%A8%E7%BD%91/%E8%BF%BD%E8%B8%AA/_tracking-state.json) | Concrete schema-v4 state at chapter 20 |
| Author memory design | [`author-memory.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/references/author-memory.md) | Preference/canon separation, precedence, lifecycle, and query budget |
| Author memory implementation | [`author_memory_commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story/scripts/author_memory_commit.py) | Separate authority, revision, idempotency, conflict and derived-view behavior |
| Author memory tests | [`test-author-memory-commit.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/test-author-memory-commit.py) | Stale, conflict, replace, forget, rollback, and query-budget coverage |
| Long-form deconstruction | [`story-long-analyze/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-long-analyze/SKILL.md) | Staged dependency graph, stop gate, analysis artifact precedence, parallel extraction |
| Import | [`story-import/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-import/SKILL.md) | Existing-work reconstruction, user gates, import cutoff, old-layout migration behavior |
| Review | [`story-review/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-review/SKILL.md) | Review modes, normalized findings, fallbacks, disagreement handling, audit/repair split |
| Setup | [`story-setup/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/SKILL.md) | Capability detection, deployment, merge policy, validation, versioning, downgrade guard |
| Shared hook core | [`story_hook_core.js`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/references/templates/hooks/story_hook_core.js) | Actual pre-write and post-write path checks for hook-capable runtimes |
| Codex hook adapter | [`story_codex_hook.py`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/skills/story-setup/references/codex/hooks/story_codex_hook.py) | Codex-specific enforcement and lifecycle limitations |
| Shared asset map | [`shared-assets.json`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/scripts/shared-assets.json) | Canonical copies and byte-parity targets for duplicated scripts/references |
| Cross-platform CI | [`.github/workflows/cross-platform.yml`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/cross-platform.yml) | OS matrix and regression coverage |
| CLI compatibility CI | [`.github/workflows/cli-compat.yml`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/cli-compat.yml) | Live CLI installation and adapter/discovery checks |
| Dashboard CI | [`.github/workflows/dashboard.yml`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/.github/workflows/dashboard.yml) | API and browser-level dashboard tests |

### Observed: licensing/provenance paths checked

- [`LICENSE`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/LICENSE) — present, MIT.
- `NOTICE` — not found at the pinned commit.
- `ATTRIBUTION.md` — not found at the pinned commit.
- README acknowledgments — present in [`README_EN.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/d1f88587c0b88abdb0a62b101b850300e0617d7b/README_EN.md).

### Inference

The strongest claims in this analysis rely on contracts confirmed in implementation and tests, particularly for state revisions, derived views, byte caps, failure recovery, and setup/runtime differences. Claims about creative effectiveness rely mainly on documented workflows and should be weighted accordingly.

### Uncertainty

The evidence index is representative, not an assertion that every file in the 648-entry pinned tree was semantically audited. The analysis prioritized files that establish architecture, authority, workflow, enforcement, and maintenance behavior.

---

## 15. Provisional CodexWriter Disposition

Every disposition below is **provisional** and must remain a comparison input until later-source review and an explicit synthesis decision.

### Provisional retain / strongly investigate candidates

- A bounded context-management responsibility with explicit budgets and a near/far retrieval ladder.
- Separate static and current dynamic character state.
- Separate author truth and reader-known timelines.
- A read-only story-query/explorer responsibility.
- A deterministic state-mutation boundary separate from prose generation.
- Revision identity and stale sequential-write rejection.
- Deterministic projections from a scoped machine authority.
- A structural-integrity check separate from semantic continuity review.
- Separate author-preference memory with an explicit precedence ladder.
- Review reports that disclose effective mode, fallback, and reviewer disagreement.
- Explicit human gates at planning-to-prose, analysis-expansion, import ambiguity, and revision-impact boundaries.
- Runtime capability detection, deployment validation, doctor/update behavior, and parity-tested adapters.
- Context/instruction budgets enforced in CI.

### Provisional adapt candidates

- `_tracking-state.json` authority — adapt the scoped-authority principle, but do not decide the CodexWriter representation yet.
- State-last derived-view writes — retain the recoverability insight while evaluating whether CodexWriter needs a journal, database transaction, or simpler single-file commit.
- Serial chapter commits — retain dependency ordering while defining explicit behavior for parallel non-mutating work and future multi-writer cases.
- Current snapshots plus chapter records — compare against Dewhurst's human-editable registries and later sources before choosing a history model.
- Zenstory's state schema — retain useful dimensions but consider first-class questions, promises/payoffs, scene state, objects, and richer relationship history.
- Story explorer — decide later whether it is a public skill, an orchestrator subrole, or an internal context service.
- Hooks — preserve enforceable preconditions where the runtime supports them, with honest degradation metadata elsewhere.
- Creative methodology — separate broadly useful narrative responsibilities from China-specific platform tactics and stylistic prescriptions.

### Provisional merge/split candidates

- **Split candidate:** continuity audit from state mutation and prose repair.
- **Split candidate:** persistent author preference from all story-canon state.
- **Split candidate:** deterministic validators from model-based critics.
- **Merge candidate:** context assembly, entity lookup, and bounded history retrieval may form one state/context service even if exposed through multiple roles.
- **Merge candidate:** setup, migration, doctor, reindex, and update may belong to one maintenance/control-plane capability rather than several creative skills.

### Provisional extension candidates

- Chinese commercial web-fiction platform scanning and genre cards.
- Browser/CDP acquisition tools.
- Local dashboard and cover generation.
- Platform-specific prose and publishing rubrics.

These can remain optional even if the underlying responsibilities are retained.

### Provisional defer

- Final canonical storage format.
- Universal precedence among manuscript prose, outlines, static setting files, and current state.
- Event log versus snapshot-plus-delta history.
- Concurrency and distributed-lock strategy.
- Exact state/context byte budgets.
- Whether CodexWriter should support all runtimes targeted by Zenstory.
- Whether a dedicated reader-simulation responsibility is retained from Lensetek or replaced by another evaluation model.

### Provisional reject / avoid candidates

- Treating `_tracking-state.json` as a settled CodexWriter choice.
- Equating schema validity with narrative truth.
- Claiming revision replay when later state is actually recalculated by an agent.
- Calling expected revision a concurrency lock.
- Allowing derived human-readable state to become a second editable authority.
- Silently degrading from enforced agents/hooks to instruction-only behavior.
- Making one market's commercial craft assumptions the default for all fiction.

---

## 16. Three-Source Comparative Baseline

### Observed

| Dimension | Lensetek | Dewhurst | Zenstory | Provisional Phase 1 reading |
|---|---|---|---|---|
| Primary contribution | Broad fiction responsibility taxonomy | Executable Markdown/YAML story contract and CLI continuity tooling | Integrated commercial-writing workflow with bounded transactional state and multi-runtime control plane | The sources are complementary rather than interchangeable |
| Specialist breadth | Broad planning, writing, editing, continuity, reader, publishing, and extension roles | Seven workflow skills around structured project operations | Thirteen workflow skills plus seven specialist agents | Lensetek remains broadest as a role map; Zenstory is deepest operationally |
| Orchestration | Responsibility-oriented skill routing | CLI and skill workflows over shared files | Scenario router, staged pipelines, agents, hooks, transactions, and fallbacks | Zenstory offers the strongest orchestration evidence so far |
| Project representation | Mostly human-readable skill artifacts | Distributed Markdown/YAML source artifacts | Hybrid: prose/settings/outlines plus JSON tracking authority and derived Markdown | Final representation remains open |
| Dynamic state authority | Not strongly centralized | Distributed registries/current-state files with authority ambiguity | One per-book JSON authority inside tracking; separate authority domains elsewhere | Zenstory narrows ambiguity without creating one universal canon |
| State history | Limited evidence | Durable entity/scene records and current state; revision is workflow-driven | Current snapshot plus bounded chapter records; revision is workflow-guided recalculation | Neither Dewhurst nor Zenstory provides deterministic downstream replay |
| Stale-write protection | Not central | No comparable revision guard found | Expected state revision rejects stale sequential transactions | Strong provisional Zenstory candidate |
| Concurrency | Not central | Not materially specified | Explicitly unsupported for state writers | Still an open CodexWriter requirement |
| Human inspectability | High | High; Markdown/YAML is directly editable | High for derived views and project files, but canonical dynamic state is JSON and derived views are not editable | Inspectability and single authority must be balanced |
| Context strategy | Responsibility and handoff oriented | Explicit reloads but weaker long-context budgeting | Capped hot context, snapshots, bounded records, on-demand references, query agent, author-memory cap | Zenstory is strongest on long-context mechanics |
| Character state | Character responsibility | Typed character and current-state artifacts | Static profiles plus bounded current snapshots | Both Dewhurst and Zenstory provide reusable distinctions |
| Scene state | Explicit scene template and change records | First-class scene-level state/change | Present mainly through outline/prose/chapter records, not a comparably typed scene entity | Dewhurst remains stronger here |
| Questions | Reader-facing role and planning concepts | First-class durable open-question records | Generic open threads/foreshadowing/commitments | Dewhurst remains stronger here |
| Promises/payoffs | Present as narrative responsibility | First-class promise/payoff records | Foreshadowing and commitments, but no dedicated pair entity | Dewhurst remains stronger here |
| Reader knowledge | Reader/testing responsibility | Knowledge state can be represented | Explicit reader-known timeline distinct from author truth | Zenstory provides the clearest epistemic state split |
| Reader simulation | Explicit reader-facing role | No equally prominent simulator | No dedicated simulator; platform rubrics and review approximate it | Lensetek responsibility remains unresolved, not displaced |
| Deterministic validation | Limited implementation evidence | Actual CLI validation, links, continuity checks, migration, and tests | State transactions/checks, hooks, prose detectors, setup validation, and extensive cross-platform tests | Dewhurst and Zenstory both show useful but different deterministic layers |
| Semantic continuity | Agent responsibility | Mixed CLI data checks and workflow judgment | Read-only consistency agent plus model review; JSON check is structural only | None proves semantic truth deterministically |
| Revision propagation | Workflow responsibility | Updates affected structured artifacts; no replay engine found | Agent recalculates through latest chapter; script merges supplied current values | Automatic propagation remains unsolved |
| Audit vs. repair | Specialist separation in taxonomy | Revision/continuity combines some concerns | Review is read-oriented; prose cleanup and state transaction are separate | Zenstory gives the clearest enforced separation |
| Creative craft | Broad fiction guidance | Comparatively light prose layer | Deep Chinese web-fiction market, emotion, rhythm, outline, and prose methodology | Zenstory is strongest but most domain-specific |
| Author preference memory | Not central in baseline | Not a distinct transactional subsystem | Separate workspace authority, lifecycle, budget, and precedence | Strong provisional responsibility candidate |
| Maintenance/runtime | Extensions and publishing responsibilities | Import/migrate/reindex/doctor plus CI and GitHub workflows | Setup/deploy/upgrade, adapters, hooks, migration, dashboard, CI matrices, doc budgets | Operational capability deserves first-class CodexWriter treatment |

### Inference

After three sources, the main state-design tradeoff is no longer “JSON versus Markdown.” It is:

1. how narrowly authority domains are defined;
2. which artifacts humans may edit;
3. whether machine-facing views are derived or canonical;
4. how stale writes and partial failures are handled;
5. how historical revision is propagated; and
6. which semantic checks remain explicitly model- or human-judged.

A plausible hybrid is visible, but it is still only a provisional candidate: human-editable canonical story artifacts for appropriate domains, a revisioned machine state for time-sensitive continuity, deterministic projections for context, and explicit reconciliation when prose and structured state disagree.

### Uncertainty

- Three sources may or may not be enough to synthesize CodexWriter's final state architecture.
- Later sources may show stronger event histories, canon-promotion workflows, conflict resolution, or lighter-weight context approaches.
- The comparative table evaluates repository contracts and implementation evidence, not equivalent end-to-end quality benchmarks.

---

## 17. Answers to Questions Carried From Dewhurst

### Observed answers

| Carried question | Zenstory evidence-based answer |
|---|---|
| Does one authoritative state solve Dewhurst's ambiguity? | It solves authority ambiguity for dynamic tracking and its derived views. It does not centralize the entire manuscript, settings, outline, benchmark corpus, or author memory into one authority. |
| How are history and earlier-chapter revisions handled? | Current state is authoritative, bounded chapter records preserve limited deltas, and an agent recalculates affected current values from the revised chapter through the latest chapter. The tool validates and commits; it does not replay. |
| Are stale updates protected? | Yes for serial state transactions through exact `expected_state_revision` matching. No general multi-writer lock exists. |
| Is Dewhurst more human-inspectable? | Dewhurst's canonical Markdown/YAML is more directly editable. Zenstory keeps inspectable Markdown projections but forbids editing them and requires JSON transactions for dynamic state. |
| Which has the stronger long-context strategy? | Zenstory has stronger explicit budgets, projections, fixed near-field limits, far-field escalation, and a read-only query role. |
| What belongs in tooling versus skills? | Zenstory puts schema, revision, rendering, byte caps, and file integrity in tools; semantic extraction, relevance selection, continuity judgment, and prose quality remain agent/skill responsibilities. |
| Can author-editable artifacts coexist with transaction guarantees? | Zenstory demonstrates coexistence across authority domains, but not one artifact serving simultaneously as editable source and deterministic projection. It avoids dual authority by making tracking Markdown derived-only. |

### Inference

Zenstory strengthens the case for explicit authority boundaries and transaction guarantees while also demonstrating why “single source of truth” must be qualified by domain. It does not eliminate reconciliation between structured state and prose; it makes that unresolved semantic boundary easier to see.

### Uncertainty

CodexWriter still needs to decide whether the usability cost of non-editable derived views is acceptable and whether a richer transaction model can preserve author-editable structured artifacts without creating competing truths.

---

## 18. Questions to Carry Forward

### Observed basis

The first three analyses leave the following questions unresolved:

1. Should CodexWriter synthesize a provisional state architecture now, or inspect Haowjy before choosing among snapshot, distributed-document, and hybrid models?
2. What is the smallest set of authority domains CodexWriter can define without creating either one overloaded canon file or many ambiguous truths?
3. Should questions, promises/payoffs, scenes, objects, relationships, character knowledge, foreshadowing, and timelines be first-class typed entities?
4. What historical representation is sufficient to propagate an earlier-chapter revision: replayable events, snapshots plus reversible deltas, dependency edges, or guided semantic recalculation?
5. Does CodexWriter need multi-writer locking, or is a single canonical writer plus parallel read-only workers an acceptable initial constraint?
6. Can human-editable Markdown/YAML be canonical while still supporting deterministic projections and stale-write checks?
7. When prose and structured state disagree, what evidence and human gate determine which artifact is corrected?
8. Should context assembly be a named user-facing skill, a specialist read-only agent, or an internal orchestrator service?
9. How should canon candidates and exploratory material be represented and promoted?
10. Which creative-craft responsibilities generalize across fiction markets, and which should remain extensions?
11. Should explicit reader simulation remain a first-class CodexWriter responsibility even though Dewhurst and Zenstory do not implement it strongly?
12. Which runtime guarantees are mandatory, and how should CodexWriter disclose degraded enforcement when a host lacks hooks or custom agents?

### Inference

The next decision point should be explicit: either synthesize the state architecture from the first three sources or continue the provisional source order with Haowjy because the unresolved history, canon-promotion, and representation questions remain material.

### Uncertainty

No architecture choice or crosswalk change is made by this analysis. All answers and dispositions remain provisional until review and a separately authorized synthesis step.
