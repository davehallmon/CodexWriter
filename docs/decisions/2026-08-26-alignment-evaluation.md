# Alignment Evaluation — Decision Record

**Date:** August 26, 2026  
**Status:** Finalized — framework decisions approved; next phase sequenced  
**Branch:** `development`  
**Evaluation basis:** CodexWriter commit [`50dee18a`](https://github.com/davehallmon/CodexWriter/tree/50dee18a1a43c76f86786788a5d82be0379d4f48); six completed CodexWriter source analyses; independent inspection of Rhavekost at upstream commit [`b78287003edf52e5f0784ee2b4a004111173358f`](https://github.com/rhavekost/author-toolkit/commit/b78287003edf52e5f0784ee2b4a00411173358f)

---

## 1. Accepted Decisions

### F1 — State model: provisional implementation prototype

The existing JSON state model (`story-state.json`, `character-state.json`, `scene-state.json`, `continuity-state.json` with their schemas) is **preserved but not ratified**. It is classified as a **provisional implementation prototype** pending the seven-source synthesis. It may prove correct, partially correct, or in need of revision — that determination requires all seven sources analyzed.

The ARCHITECTURE.md guardrails required all seven source analyses before CodexWriter chose a canonical state design. That guardrail was violated: the orchestrator declared `story-state.json` canonical and the build proceeded before Rhavekost was analyzed. The violation is procedural; it does not establish that the JSON model is wrong. It establishes that the decision was premature.

### F2 — Framework scope: reusable core with optional project profiles

CodexWriter remains a **reusable fiction-authoring core with optional project profiles.** The Biblical/ANE/Stephen King/Gemini/Thread Pull requirements are **extracted into a *Dust & Ash* profile.** Their generalizable reasoning principles — evidence before inference, pressure systems, source lineage notes, and contamination review — remain in the core.

This directly addresses the over-reliance finding: the character-development skill's V4 pipeline and the generic character-dossier template both required Biblical evidence and Stephen King integration, making the core skill Dust & Ash-specific rather than a reusable framework component.

---

## 2. Evaluation Basis and Methodology

### Hermes Agent evaluation

Built against the build report at `docs/build-report-2026-08-26.md` plus the six completed CodexWriter source analyses in `docs/source-analysis/` and the actual skill files on the `development` branch.

### ChatGPT-5 Sol evaluation

Built against the full repository tree at commit `50dee18a` (37 tracked files). Six CodexWriter source analyses were available. Rhavekost was still marked "Not started" in CodexWriter; ChatGPT-5 Sol independently inspected its latest upstream commit at `b7828700` to test the claimed reader and editorial patterns. That independent inspection was sufficient for the evaluation. It was **not** a substitute for the agreed full CodexWriter Rhavekost analysis.

### Reconciliation process

The two evaluations were compared line by line. ChatGPT-5 Sol's tree-based findings control where the evaluations differed, because it read the actual files rather than the build report. The build report's inventory counts (schemas, file sizes) are not reliable and should not be treated as authoritative.

---

## 3. Summary of Findings

### Strongest elements

- **Specialist roles:** 11 dedicated skills plus a routing orchestrator, with clear boundaries between planning, drafting, reviewing, editing, continuity, and reader testing.
- **Phase routing:** Five-phase pipeline with phase gates. The structure is sound even though gates are not yet executed.
- **Story-state vocabulary:** POV assignments, knows/doesn't-know lists, promise/payoff tracking, Thread Pull design integrated into narrative architecture.
- **Voice guidance:** Scene-writing and prose-editing skills contain strong voice-preservation guidance, though no structured voice artifact exists yet.

### Key gaps

- **Deterministic continuity:** The continuity skill describes checks that the orchestrator calls "mechanical" but that require model judgment — voice consistency, "reasonable" emotional progression, pressure-system consistency, payoff timing. There is no executable validator, no test harness, and no schema validation implementation. This is the single largest operational gap.
- **Context management:** No context assembler, no LOD strategy, no context budget, no near/far policy, no index. Skills list inputs but do not define how much to load, how to narrow, or what to exclude. This is the largest scalability gap.
- **Reader simulation drift:** The reader-simulation skill loads the revised manuscript, scene outlines, character dossiers, story bible, continuity report, and narrative architecture. These are privileged author context. A genuine context-blind reader test requires a first pass with the manuscript only, an isolated context, and an optional informed diagnostic pass afterward. The current design contradicts the best practice found in Rhavekost.
- **Proof vs. claim:** Portability, determinism, and reusability are claimed but not demonstrated. No cross-host test, no executable validator, no tests.
- **Documentation drift:** README still says private, Phase 1, no skills. Build report miscounts schemas and files. ATTRIBUTION.md uses mutable `main` links. Only 3 of 11 skills have explicit provenance sections.

### Source representation

- **Lensetek:** Strongly reflected in the visible architecture — 11-skill taxonomy, five-phase routing.
- **Dewhurst:** Terminology and state-vocabulary adopted; operational rigor (executable continuity engine, tests, CLI, CI, migration) not yet reflected.
- **Haowjy:** Writer/critic/editor separation and voice preservation partially reflected; Muse coordination role, cognitive stance staffing, context discipline, and KB convention not yet built.
- **JeroTan:** Constitution concept, editor's exact-text gate, and sharding reflected in places; full context reload machinery not built.
- **wgwtest:** Epistemic vocabulary, context LOD policy, and deterministic checker not yet reflected in the built system. Its influence on the current schema design is real but partial.
- **Rhavekost:** Contradicted in key places — reader context is not blind, editorial stopping rules are not carried over. Independent inspection confirmed the patterns the CodexWriter analysis had not yet documented.
- **Zenstory:** Influenced the current layered schema design (state layers, revision counters, checks, reports). Transaction semantics, stale-revision protection, atomic commits, derived views, and separate author memory are absent.

---

## 4. Four Priority Adjustments

### 4.1 Tests and CI raised to High

A validator without fixtures and automated tests cannot substantiate "deterministic continuity." Schema hardening (A4), the schema validator (A5), the continuity validator (A6), and generic fixtures + smoke tests + CI (A17) form one **High-priority infrastructure workstream.** They should be built and tested together, not sequentially.

### 4.2 Portability reframed

An initial portability smoke test (one skill on a second host) is useful evidence, but it does not establish framework portability. Alpha should require a **representative workflow on at least two hosts, with differences and fallbacks documented.**

### 4.3 Framework approvals separated from story phase gates

Framework-development approvals (architectural decisions, releases, state model ratification) and author-facing story phase gates (concept approval, outline, draft, final review) are different things. Framework approvals belong in the Framework track. Dust & Ash story phase approvals belong exclusively in the **Dust & Ash project track.**

### 4.4 Source representation wording tempered

RHavekost is contradicted in key places (reader context, editorial stopping rules). wgwtest is partially operationalized. Zenstory influenced the layered schema design — it is not merely terminology. The word "terminology" alone understates the current state.

---

## 5. Public-Log Sensitivity Inventory

The following environment-specific session logs and operational details are currently tracked in the public `development` branch:

| File | Size | Contents | Sensitivity Assessment |
|---|---|---|---|


**No redaction, movement, or deletion was performed in this commit.** These files remain in place. The inventory is presented for approval before any action is taken.

**Post-cleanup note:** As of the documentation-hygiene commit, all three files were removed from the public `development` tree. Private copies are preserved outside the Git repository at `/home/davehallmon/.codexwriter-private/logs/`. The inventory above records what was found and why removal was recommended.

### Recommendations for approval

1. **Option A — Remove from public repo.** Move the three _LOG transcripts to a non-public location (private repo, local storage, or Google Drive) and remove them from `development`. This is the cleanest option for a public framework repository.
2. **Option B — Keep with a clear boundary.** Retain the files but add a top-level notice that they are environment-specific session logs, not framework material, and may be removed at any time.
3. **Option C — Redact and retain.** Strip session-specific operational details (API references, auth discussions, environment-specific paths) and retain the analytical content.

A decision on these recommendations is required before any action is taken. option A is the default recommendation for a public framework repository.

---

## 6. Framework Task List (Framework Track)

### High priority

- **A1 — Complete pinned Rhavekost analysis** (`b7828700`): fresh sub-agent model, reader-test stopping rules, prose-mechanics audit contract, diagnostic-to-repair approval flow.
- **A2 — Produce 7-source synthesis:** update ARCHITECTURE.md and crosswalk from all seven sources.
- **A4–A6 + A17 — Infrastructure workstream:** schema hardening with stable IDs, references, gate audit records, knowledge provenance, revision history, cross-file consistency checks; schema validator (Python, validates all 4 schemas against instances); minimum viable continuity validator (schema validation + character_id pattern checks + phase/phase_gate consistency + state_revision monotonicity); generic fixtures + smoke tests + CI. Build and test together.
- **A14 — Public-log sensitivity inventory and redaction/removal proposal:** see Section 5. Implementation pending decision.

### Medium priority

- **A3 — Extract V4 pipeline into Dust & Ash profile** (contingent on F2; retain generalizable principles in core).
- **A7 — Context assembly strategy:** wgwtest-inspired L0–L4, sharding boundaries, LOD, pre-write reload contracts, conflict precedence.
- **A8 — Redesign reader-simulation for context-blind model:** blind first pass (manuscript only), isolated context, optional informed diagnostic pass, stopping rules.
- **A9 — Shared findings/disposition schema:** audits stop for author review before repairs.
- **A11 — Update README:** public, Phase 2, 11 skills, all 7 sources analyzed or in progress.
- **A15 — Project initializer:** create story-state.json + project scaffold from title/logline.

### Low priority

- **A10 — Add provenance sections to all 8 remaining skills** (fiction-orchestrator, concept-development, scene-planning, scene-writing, continuity, prose-editing, reader-simulation, export).
- **A12 — Fix build report:** correct schema count to 4, file size to ~116 KB, confirm continuity schema exists.
- **A13 — Pin ATTRIBUTION.md links:** use pinned source revisions, not mutable `main`.
- **A16 — Portability smoke test:** initial signal; Alpha needs representative workflow on 2+ hosts with documented differences and fallbacks.
- **A18 — Executable export path:** DOCX/ePub/PDF — deferred.

---

## 7. Dust & Ash Project Track

The following are author-facing creative tasks for the Dust & Ash novel. They are **not** framework-development tasks and belong in a separate project track.

| Task | Description | Priority |
|---|---|---|
| **D1 — Finalize the Blueprint** | Gate 1 artifact. The creative contract for the story: concept, theme, tone, characters, setting, plot. | **CRITICAL** |
| **D2 — Consolidate Chapter 1 drafts** | Review all 5 variants, choose the authoritative draft, move to Drive. | **HIGH** |
| **D3 — Export Gemini notebooks** | All 8 Dust & Ash notebooks to `_Dust & Ash/NotebookExports/` on Drive. | **HIGH** |
| **D4 — Phase gate approvals** | Author approves each phase output (story bible, worldbuilding, architecture, drafts, final manuscript). | **CRITICAL (ongoing)** |
| **D5 — Avram end-to-end V4 pipeline test** | Run character-development skill against existing Gemini content for Avram. Validates the skill and produces a finalized dossier. | **MEDIUM** |

---

## 8. Six-Step Immediate Sequence

1. **Inspect public logs** — sensitivity inventory presented in Section 5; redaction/removal proposal pending approval. Non-destructive first.
2. **Complete the pinned Rhavekost analysis** — does not wait for F1 or F2. Evidence gathering only.
3. **Produce the 7-source synthesis** — update ARCHITECTURE.md and crosswalk from all seven sources.
4. **Ratify or revise the state architecture** — now that all sources are in. The JSON model is provisional until this step completes.
5. **Separate the reusable core from the Dust & Ash profile** — extract Biblical/ANE/Stephen King/Gemini/Thread Pull requirements; retain generalizable principles in core.
6. **Build and test one generic vertical slice** — representative workflow on 2+ hosts, with tests and CI.

---

## 9. Decision Record Notes

- The JSON model is **provisional pending the seven-source synthesis.** It is preserved but not ratified.
- The Rhavekost source analysis is **not complete.** Only an independent upstream inspection has been performed. The CodexWriter analysis is still pending.
- This document records framework-alignment decisions only. It does not make any other framework or implementation changes.
- Files changed in this commit: `docs/decisions/2026-08-26-alignment-evaluation.md` (new), plus the public-log sensitivity inventory findings above (no files removed, moved, or redacted).

---

*End of decision record.*

---

## Historical snapshot notice

**Date:** August 27, 2026

Sections **1 through 9** (accepted decisions, evaluation basis and methodology, summary of findings, four priority adjustments, public-log sensitivity inventory, framework task list, Dust & Ash project track, six-step immediate sequence, and decision record notes) are a **dated historical snapshot** from August 26, 2026. They record the state of the evaluation at that time, including the original task list, immediate sequence, and Rhavekost/synthesis status.

**Those operational statuses are superseded by the August 27 ratification note below.** The ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3` and the ratification note in this section are the current governing material.

**Do not execute the old "next steps," task list, or immediate sequence as current instructions.** Those sections are retained as historical evidence, not as current action items.

The original F1 and F2 reasoning and the evaluation basis are historical evidence and are preserved verbatim above. Only the current-status handling is corrected below.

---

## Ratification note

**Date:** August 27, 2026
**Status:** Ratified — hybrid architecture ratified; documentation alignment authorized; schema, skill, and implementation changes remain unauthorized
**Branch:** `architecture/ratified-alignment`
**Governing decision instrument:** CodexWriter ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`

### What this note establishes

- **F1's provisional-state review is complete at the architecture level.** The seven-source synthesis is complete, and the layered hybrid architecture is ratified. The existing JSON state model remains a **provisional implementation prototype** until separately reviewed by the authorized file-by-file schema and skill impact plan.
- **The hybrid architecture is ratified.** The ratified model establishes approved Markdown manuscript files as authoritative for exact narrative wording, approved structured state as authoritative for explicitly governed machine-checkable intended canon and workflow fields, and derived views as non-authoritative rebuildable projections. It establishes explicit author reconciliation when approved prose and approved structured canon conflict, validated transactions, stale-revision protection, provenance, audit history, and no silent overwrites as architectural requirements.
- **Existing schemas remain a provisional implementation prototype until separately reviewed.** Ratification does not authorize schema or skill-contract changes. Documentation alignment is now complete on the isolated branch `architecture/ratified-alignment` and pending review. The file-by-file schema and skill impact plan is the next **prospective** deliverable, subject to explicit authorization after documentation alignment is accepted. It is not presently authorized. Before any schema or skill-contract change begins, the impact plan must be produced and approved separately.

- **Documentation alignment is complete on the isolated branch** `architecture/ratified-alignment` **and pending review.** Ratification authorizes alignment updates only to `ARCHITECTURE.md`, `docs/crosswalk.md`, and the applicable decision/status documentation, on that branch created from commit `70861e660d7d7e5261482834397f5f6a97aa43d3`.
- **Schema, skill, and implementation changes remain unauthorized.** This ratification does not authorize merging the synthesis branch, changing schemas, templates, or skill contracts, or beginning validator, initializer, runtime, CI, portability, or vertical-slice implementation work. Reviewing the documentation-alignment changes does not automatically authorize implementation.
- **The ratification addendum at commit `70861e6` is the governing decision instrument.** Where this decision record and the addendum address the same subject, the addendum controls because it is the instrument the user ratified.

### What this note does not change

This note does not reopen F1 or F2. It records that their provisional-state-review and framework-scope decisions have reached ratification at the architecture level. It does not make any schema, skill, template, implementation, test, CI, or Dust & Ash file change.
