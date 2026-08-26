# Source Analysis: haowjy/creative-writing-skills

**Status:** Draft ready for review  
**Analysis date:** 2026-08-26  
**Repository:** `haowjy/creative-writing-skills`  
**Analyzed commit:** `fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3`  
**Upstream package version:** `0.5.9`  
**Phase:** Phase 1 evidence gathering  
**Decision status:** Every CodexWriter disposition in this document is provisional. This analysis does not change `ARCHITECTURE.md` or `docs/crosswalk.md`.

## Evidence Labels

- **Observed** — directly supported by repository files, executable code, or pinned repository metadata at the analyzed commit. Claim identifiers such as `[H14]` resolve to exact immutable file-and-line evidence in Section 14.
- **Inference** — an architectural interpretation derived from observed evidence.
- **Uncertainty** — a question the inspected evidence does not settle, a dependency- or runtime-dependent behavior, or a claim that still needs empirical validation.

All upstream source links in this document are immutable blob links pinned to `fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3`.

---

## 1. Repository Snapshot

### Observed

| Field | Pinned finding |
|---|---|
| Analyzed revision | `fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3`, verified as the upstream `main` head inspected on 2026-08-25 |
| Package version | `0.5.9` in `mars.toml`; the changelog dates that release to 2026-08-08. [H01] |
| Product scope | A creative-writing package for novels, short stories, and serial fiction, organized around specialized agents, shared craft skills, and a durable story knowledge base. [H02] |
| GitHub primary language | Python in the repository metadata snapshot inspected on 2026-08-25 |
| Canonical Mars source | 11 repository-owned skills under `skills/` and 11 agent definitions under `agents/`. [H03] |
| Flattened `cw/` distribution | 24 skills: 16 generated and 8 manual; plus 11 generated agents. Six generated skills and several manual adaptations originate in the `meridian-base` dependency rather than this package's canonical `skills/` directory. [H03] |
| External knowledge role | `kb-lead` is intentionally not bundled; Muse uses the dependency's agent when available or applies `story-memory` directly. [H04] |
| Implementation mix | Markdown agent/skill/reference files, Python packaging and prose-analysis scripts, shell hooks, JSON manifests, GitHub Actions workflows, and TOML package/runtime configuration. [H05] |
| Documented runtimes | Mars/Meridian, Claude Code, Cowork, and Claude.ai. `mars.toml` also targets `.codex`, although Codex is absent from the README compatibility table. [H06] |
| Release/maintenance evidence | The changelog records active consolidation through version `0.5.9`; CI validates package/plugin structure and builds skill archives. [H01] [H07] |
| License | Apache License 2.0 in the exact pinned root `LICENSE` file. [H08] |

The 11 canonical source skills are:

1. `character-sim`
2. `creative-research`
3. `creative-writing-craft`
4. `creative-writing-modes`
5. `creative-writing-muse`
6. `reader-sim`
7. `story-memory`
8. `story-planning`
9. `story-review`
10. `writing-principles`
11. `writing-staffing`

The 11 bundled agent definitions are:

1. `muse`
2. `writer`
3. `critic`
4. `editor`
5. `reader-sim`
6. `character-sim`
7. `continuity-checker`
8. `brainstormer`
9. `outliner`
10. `style-creator`
11. `web-researcher`

The README's tables are not complete inventories: its agent table omits `web-researcher`, and its skill table mixes repository-owned, dependency-provided, and `cw`-only components while omitting `creative-research`. [H03] [H09]

### Inference

Haowjy is best understood as a **creative operating model and craft library with multiple delivery formats**, not as a transactional story database. Its strongest contribution is the deliberate separation of creative stances—direction, drafting, focused critique, holistic editing, experiential reading, continuity checking, research, and memory capture—over shared human-readable artifacts.

The repository shows active design iteration and meaningful packaging discipline, but its version is still pre-1.0 and the pinned tree contains several contract/distribution inconsistencies. “Mature enough to study” should not be read as “behaviorally proven for completed long-form projects.”

### Uncertainty

- The analysis did not run an end-to-end novel project in every advertised runtime.
- Repository structure and CI do not establish literary quality, long-project reliability, or user adoption.
- Some effective Mars behavior comes from the moving `meridian-base` dependency, so the pinned application commit alone does not identify every runtime component actually resolved in a fresh installation.
- The README inventory drift makes component counts discoverable from source but less clear to users.

---

## 2. Licensing and Provenance

### Observed

- The exact pinned file [`LICENSE`, lines 1–5](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/LICENSE#L1-L5) identifies the Apache License, Version 2.0. The same file contains the standard terms and appendix through [`LICENSE`, lines 176–201](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/LICENSE#L176-L201). Its pinned blob SHA is `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`. [H08]
- `NOTICE`, `NOTICE.md`, `ATTRIBUTION`, and `ATTRIBUTION.md` each returned `404 Not Found` when checked at the pinned commit.
- The package declares a remote `meridian-base` dependency with version range `>=0.10.0` and a local `meridian-prompter` dependency. [H10]
- The committed `cw/` plugin intentionally bundles dependency-provided skills: six are copied through generated Mars output, while at least three additional dependency skills are maintained as de-Meridianized manual adaptations. [H11]
- `mars.lock` is ignored, so the repository does not commit the exact dependency resolution used to generate the pinned `cw/` copies. [H12]
- The repository's research-facing writing principles carry a source list that distinguishes research claims, contested replication, craft tradition, and community-derived claims rather than presenting every prompt rule as independently established fact. [H13]

### Inference

The Apache-2.0 license is direct evidence for the repository itself. It is sufficient for architectural comparison, but any implementation-level copying into CodexWriter would require a separate Apache compliance and provenance review.

The flattened distribution deserves extra care. The pinned tree proves that committed files are generated or adapted from a dependency, but the unbounded dependency range and absent lock file do not prove which exact `meridian-base` commit supplied each copied component. CodexWriter should not treat “present in this Apache-licensed repository” as a complete lineage record for dependency-derived text.

### Uncertainty

- This analysis does not make a legal determination about whether the root license alone satisfies every obligation for the dependency-derived `cw/` files.
- No pinned repository file maps each bundled dependency artifact to an exact upstream commit or source license.
- The absence of a `NOTICE` or attribution file is an inspection result, not proof that no third-party notice obligation exists.
- Substantial prompt, script, or adapter borrowing should remain blocked on file-level provenance review; responsibility-level comparison does not require copying source expression.

---

## 3. Architectural Thesis

### Observed

The package explicitly favors a strong author-facing Muse, a compact worker set, durable story context, and rich shared methodology over many near-duplicate writing agents. [H14]

Its primary separations are:

| Separation | Observed implementation |
|---|---|
| Coordination vs. execution | `muse` interprets intent, staffs work, synthesizes outputs, and owns the author-facing verdict; workers perform focused tasks. [H15] |
| Planning vs. prose vs. review | `story-planning`, `creative-writing-modes`, and `story-review` define distinct modes with explicit boundaries. [H16] |
| Production vs. diagnosis | `writer` owns prose; `critic`, `editor`, `reader-sim`, and `continuity-checker` are read-only in their Mars agent profiles. [H17] |
| Method vs. process | Agent bodies are thin role contracts; skills and resources carry craft, review, context, and memory methodology. [H14] [H18] |
| Durable knowledge vs. working material | `kb/` holds durable knowledge; `work/` holds outlines, drafts, critique reports, and brainstorm material. [H19] |
| Multi-agent vs. solo operation | Named workers receive separate contexts when available; `creative-writing-muse` switches stances in one conversation when subagents are unavailable. [H20] |

The core draft loop is Muse → Writer → one or more diagnostic roles → Writer. One writer owns all production modes to reduce adjacent-scene voice drift, while diagnostic stances stay separate to protect independence. [H14] [H21]

### Inference

The package's organizing principle is **cognitive-role separation plus progressive methodology loading**. It treats contamination between creative modes as a context problem: drafting should not begin in a critic's mental frame, and memory extraction should not inherit unexamined invention from drafting.

This is a different answer from Zenstory's state-first control plane. Haowjy uses process discipline, scoped files, and agent isolation to reduce errors; it does not make a revisioned state transaction the central architectural boundary.

### Uncertainty

- Separate process contexts may improve independence, but the repository contains no controlled evaluation demonstrating the benefit.
- One production writer may improve voice continuity, but that claim is a design rationale rather than a measured result.
- The extent to which the thin-agent/rich-skill split transfers across runtimes depends on each host's skill loading, subagent, and tool-isolation semantics.

---

## 4. Workflow and Orchestration

### Observed

#### 4.1 Entry point and phase flow

Muse is the primary author-facing entry point. The documented workflow moves among Explore/Plan, Draft/Revise, and Knowledge work rather than enforcing a single irreversible pipeline. Exploration uses brainstormers, character simulation, and outlining; prose work uses one writer plus specialized review; knowledge work captures settled facts and style. [H02] [H15]

Muse must preserve reader effect, emotional target, constraints, taste, uncertainty, and failure boundaries. It reads drafts and reports itself, resolves disagreement, chooses the next move, and does not simply forward raw specialist output. [H15]

#### 4.2 Specialist boundaries

| Role | Observed boundary and output |
|---|---|
| `brainstormer` | Produces scoped options, tradeoffs, and open questions in `work/brainstorm`; leaves convergence to the author. [H22] |
| `outliner` | Converts chosen direction into saga/arc/chapter/scene/beat blueprints that identify state change, reader information, emotion, and setup/payoff links. [H23] |
| `writer` | Produces fresh drafts, revisions, bridges, alternate takes, or line polish from briefs, style, critique, adjacent prose, and canon. [H24] |
| `critic` | Performs one deep adversarial focus-area review with passage anchors, reader cost, direction, and severity. [H25] |
| `editor` | Produces a holistic, large-to-small editorial memo; its profile denies file writes. [H26] |
| `reader-sim` | Reports a persona-bound first reading rather than an analytical diagnosis. [H27] |
| `continuity-checker` | Searches broadly across canon and reports evidence-backed contradictions without proposing fixes. [H28] |
| `style-creator` | Derives project-specific style reference files from samples and separates specified traits from inferred ones. [H29] |
| `web-researcher` | Produces sourced creative research with confidence, conflicts, contradictions, and gaps; story-fit remains a writer decision. [H30] |
| `kb-lead` or Muse | Extracts durable facts only after a triggering event settles; `kb-lead` comes from `meridian-base`, with direct Muse fallback. [H04] [H31] |

#### 4.3 Staffing, fan-out, and ordering

The staffing skill distinguishes same-prompt, cross-model **fan-out** from different-prompt **parallel lanes**. It recommends one writer per scene, focus-area critic lanes scaled to stakes, a reader simulation after the write/critique loop converges, and knowledge maintenance after a chapter, brainstorm, or author decision settles. [H21] [H31]

Model aliases are selected by cognitive role: creative judgment, structured synthesis, and mechanical gathering receive different defaults. The runtime is instructed to resolve aliases at dispatch time rather than assume a concrete model. [H32]

#### 4.4 Stop conditions and handoffs

- Production begins after the author confirms direction; the handoff includes approved outline, style files, and relevant context. [H33]
- Brainstorm contradictions and competing options coexist until the author chooses. [H34]
- Reader simulation waits until drafting/critique converges. [H31]
- Memory capture waits until facts or decisions settle; provisional brainstorms must not become canon. [H15] [H31]
- Project setup drafts the project contract, shows it to the author, iterates until approval, and only then creates files. [H35]
- Muse asks when the answer changes the work; otherwise it states its interpretation and proceeds. [H15]

#### 4.5 Solo fallback

When subagents are unavailable, `creative-writing-muse` deliberately switches among direction, drafting, critique, research, voice/terms, and memory stances. It self-prompts before each pass and updates memory only for settled facts and decisions. [H20]

### Inference

Haowjy offers the clearest evidence so far for **staffing by cognitive stance rather than by artifact name**. The same prose agent can draft, bridge, revise, and polish because those modes share voice ownership; critique, editing, reader experience, and continuity stay separate because they require different incentives or context.

The workflow is flexible and author-centered, but much of its ordering is instructional rather than transactional. A compliant Muse should respect convergence and canon-promotion boundaries; no central workflow engine proves that those stages occurred.

### Uncertainty

- It is not clear how a host without strong agent/tool enforcement prevents a worker from crossing its prompt-defined role.
- No explicit retry, cancellation, partial-result, or specialist-failure protocol is defined for creative work.
- The package does not define a durable workflow-status artifact that records which stage is complete.
- Same-prompt model diversity is a plausible evaluation technique, but no repository benchmark measures when it improves decisions enough to justify cost.

---

## 5. State Storage Model

### Observed

#### 5.1 Actual storage model

The repository defines a **Markdown-first, convention-driven project memory**. Durable knowledge lives under `kb/`; current work lives under `work/`; author manuscript space is separately described during setup. The package provides schemas as prose conventions, not a canonical JSON/YAML state engine. [H19] [H35] [H36]

| Required state question | Observed Haowjy behavior |
|---|---|
| Static/canonical facts | `kb/canon/`, `kb/world/`, reference pages, timeline pages, vocabulary, and character pages. Published/finalized chapter facts are defined as canon. [H36] |
| Dynamic/current state | Existing character, timeline, relationship, knowledge, and reference pages are updated as the story changes; there is no separate revisioned “current state” database. [H37] |
| Machine-readable authority | None specified for story state. Markdown files are the durable representation. [H19] [H36] |
| Human-readable authority | Files on disk; read the current versions before acting. The author's direct edits are always authoritative. [H19] |
| Authority among KB files | One source of truth per concept is the convention; related pages cross-link rather than duplicate. [H36] |
| Story-history representation | Current pages accumulate sourced facts; timeline/canon pages provide chapter or period organization; resolved issue files remain with resolution notes. No append-only event log or replayable delta ledger is specified. [H37] [H38] |
| Post-draft update | Extract the chapter's factual state diff, update existing entries, cross-link affected pages, and record chapter anchors. [H37] |
| Earlier-chapter revision | Record the ordering change and ask what else it affects; do not auto-adjust downstream material. Conflicts with existing KB truth remain unresolved until the author or orchestrator decides. [H39] |
| Stale/conflicting writes | Read current disk state and surface conflicting edits rather than overwrite. No revision number, compare-and-swap guard, lock, or transactional commit protocol is specified. [H19] |
| Exploratory material | Brainstorms stay under `work/`, AI suggestions use `<AI>`, secrets use `<hidden>`, rejected options use `<rejected>`, and only settled knowledge is promoted. [H40] |
| Author voice/preferences | Project conventions and `kb/styles/` are separate artifacts from `kb/canon/`; style files derive from samples and are selected per writing task. There is no separate cross-project author-preference store. [H29] [H35] [H36] |

#### 5.2 Fact model

Fact extraction asks for a chapter-level state diff covering character physical/emotional/location/knowledge state, timeline events, world canon, relationships, reader-versus-character reveals, terminology, and any other load-bearing fact. Entries should be compressed, sourced, factual, and updated rather than duplicated. [H37]

The package intentionally keeps the taxonomy open-ended. This preserves creative flexibility, but it means state categories are headings and prose conventions rather than validated types. [H37]

| Candidate CodexWriter entity | Haowjy representation |
|---|---|
| Character current state | Explicitly requested in character pages and extraction guidance, but untyped Markdown. [H37] |
| Character knowledge | Explicit category and handoff input. [H37] [H41] |
| Reader knowledge | Explicitly distinguished from character knowledge during fact extraction and reader simulation, but not stored in a dedicated reader-known timeline. [H27] [H37] |
| Relationships | Updated in both relevant character entries and linked timeline entries. [H37] |
| Timeline | Markdown chronology pages and continuity review; no executable event schema. [H36] [H39] |
| Objects/possessions | Can appear inside character state or generic canon; no first-class object record is defined. [H37] [H52] |
| Questions | Open questions appear in brainstorms and reviews; no durable typed question entity is defined. [H22] [H40] |
| Promises/payoffs | Outlines track setup/payoff connections; no paired durable promise/payoff schema is defined. [H23] |
| Issues | One persistent Markdown file per cross-chapter issue, with evidence, scope, severity, deduplication, and retained resolution history. [H38] |

#### 5.3 Conflict behavior

When a chapter conflicts with existing canon or vocabulary, fact extraction says to flag the conflict and preserve the existing record until the author or orchestrator resolves whether the cause is error, retcon, or terminology change. [H37]

The shared-workspace convention says every worker must reread current files, treat disk rather than memory as authoritative, surface edit collisions, and always defer to direct author edits. [H19]

### Inference

Haowjy demonstrates that human-editable story memory can support disciplined collaboration without a central state file. Its source anchors, one-concept pages, cross-links, explicit current-state rereads, and author authority are useful contracts.

It does **not** demonstrate stale-write safety or deterministic revision propagation. The earlier-revision guidance is explicitly human/agent-guided: record the change, expose affected questions, and wait for an author decision. That is a valuable honesty boundary, not an automated replay mechanism.

The model is closer to an evolving wiki plus workflow rules than to Dewhurst's typed project contract or Zenstory's transactional snapshot. That makes it inspectable and adaptable, but it leaves duplicate truth, merge conflicts, and incomplete propagation to model and human judgment.

### Uncertainty

- The exact `meridian-base` KB and knowledge-graph behavior resolved at installation is not pinned by this repository.
- No conflict test shows whether two simultaneous state writers reliably notice and surface an intervening edit.
- No repository evidence defines a universal precedence rule for contradictions among manuscript prose, an approved decision, an outline, a character page, a timeline page, and a canon summary.
- “Finalized” and “settled” are meaningful human terms, but the package does not encode a machine-checkable promotion status.
- The source does not show how a large earlier-chapter rewrite is exhaustively propagated across every affected page.

---

## 6. Context Management

### Observed

The `story-context` resource offers three handoff mechanisms: attach stable files; pass conversation history when unwritten reasoning matters; or materialize critical decisions before delegation when contradiction would be costly. [H42]

It gives role-specific scopes:

- writers receive the brief, selected style files, relevant character/vocabulary state, the immediately preceding scene, and only the chapters that establish referenced facts—typically two to four continuity files rather than the whole manuscript;
- critics receive the draft, brief, style, relevant earlier chapters, author intent, known issues, and vocabulary;
- brainstormers receive the question, constraints, rejected directions, and vocabulary, but not so much history that exploration collapses into conservative recombination;
- knowledge work receives source chapters plus existing affected KB files for deduplication, while full KB restructuring may read the entire KB. [H43]

Cross-phase handoffs combine conversation reasoning with materialized artifacts. Terminology settled in a session should be written before spawning a worker that could choose the wrong name. [H44]

Style references are sharded by the dimensions callers may need independently. Each file boundary is explicitly treated as a future context-selection decision. [H45]

Muse gives each subagent a separate context window and asks staffing to attach only the extra skills and files needed for that task. The continuity checker can use the Markdown link graph to locate related canon instead of reading everything. [H15] [H21] [H28]

There is no numeric token or byte budget for story context. The explicit quantitative guidance is qualitative/local: two to four continuity files for writers, self-contained style files, and an approximately 200-line split threshold in the `cw` KB-management adaptation. [H36] [H43] [H45]

### Inference

Haowjy provides a strong **smallest-sufficient-context judgment framework** but not a deterministic context compiler. Its near field is full prose and current state chosen by the orchestrator; its far field is linked Markdown and selectively attached reference material.

Materializing critical decisions before handoff is a useful bridge between conversational intent and durable project state. It reduces dependence on chat history without requiring every thought to become canon.

### Uncertainty

- No algorithm ranks or caps candidate context beyond the stated file-count and page-size heuristics.
- Link-graph proximity does not prove semantic relevance, and the continuity checker still relies on model judgment after retrieval.
- The package does not specify what happens when a compact KB summary conflicts with the exact manuscript passage beyond surfacing the conflict and deferring to author/orchestrator resolution.
- The analysis did not measure context use or retrieval recall on a manuscript large enough to stress the conventions.

---

## 7. Creative-Craft Model

### Observed

#### 7.1 Author-led planning

Creative direction starts from the intended reader experience and existing constraints, explores alternatives, recommends with evidence, and leaves the final choice to the author. Direction must be recorded before production handoff. [H33]

Brainstorm capture preserves ambiguity, tags provenance, permits contradictory options, and avoids filling gaps the author intentionally left open. Outlines remain hypotheses rather than contracts and can change when drafting reveals a better structure. [H40] [H46]

#### 7.2 Production modes

One writer supports five explicit modes: fresh draft, revision, bridge/connective tissue, alternate take, and line polish. Each mode has a different input set and stopping discipline; line polish is delayed until structure, causality, and voice are settled. [H47]

Revision starts from synthesized critique rather than every raw finding. It identifies the failed reader effect and changes the smallest surface likely to repair it while preserving voice, useful ambiguity, imagery, and working structure. [H47]

#### 7.3 Prose and scene craft

The craft library covers psychic distance, free indirect discourse, sentence rhythm, sensory grounding, interiority, POV discipline, scene entry, subtext, voice differentiation, pacing, and transitions. [H48]

The planning layer emphasizes nested story scales, causation over sequence, escalation, setup/payoff, and tension/release without mandating one named structure. [H46]

#### 7.4 Reader reward and AI failure modes

`writing-principles` treats the reader as an active collaborator and organizes diagnosis around transportation, aesthetic pleasure, social simulation, flow, and curiosity/prediction. It distinguishes intentional ambiguity or omission from accidental under-explanation. [H49]

Its failure-mode catalog targets LLM-specific tendencies such as over-expanding scope, flattening voice, info-dumping, labeling emotions, resolving tension early, homogenizing character voices, collapsing ambiguity, and over-intensifying language. [H50]

#### 7.5 Style, genre, and research

Style analysis discovers project-specific dimensions from samples, splits references where callers need independent context, includes representative chapter-cited examples, and separates reproducible patterns from unwanted tics. [H45]

The craft skill exposes genre-specific resources alongside general prose and scene technique. Creative research prioritizes current sources, primary/practitioner detail, conflicting evidence, citations, and explicit gaps while leaving story-fit judgment to the writer. [H30] [H51]

### Inference

Haowjy supplies the strongest general-purpose prose-and-reader methodology among the first four sources. It is less market-specific than Zenstory and more operationally detailed about voice, reader cognition, and review stance than Lensetek or Dewhurst.

The most reusable craft idea is not a single prose rule. It is the stack: author intent → reader reward target → project style → mode-specific execution → independent reader/critic evidence → smallest effective revision.

### Uncertainty

- The source list supports parts of the reader-reward framing, but many craft prescriptions remain synthesized expert guidance rather than experimentally validated prompt interventions.
- The repository does not include before/after literary benchmarks for its style files or failure-mode prompts.
- Asking for published works as style inspiration is documented during setup, but the inspected source does not define safeguards against overly close imitation of a living author's style.
- Genre resources cover a useful subset, not an exhaustive fiction taxonomy.

---

## 8. Evaluation and Continuity

### Observed

#### 8.1 Distinct judgment roles

- A critic is adversarial and focus-area specific. Findings identify the passage, reader cost, possible direction, and severity; parallel critics go deep on separate dimensions. [H25]
- An editor reads the full draft, diagnoses large before small, protects author voice, queries changes to meaning/voice/canon, and returns a priority-ordered memo. [H26]
- Reader simulation is experiential evidence tied to a named persona and knowledge boundary. It reports where attention, curiosity, transportation, aesthetic pleasure, social modeling, and flow changed rather than prescribing fixes. [H27]
- Continuity review checks timeline, geography, character state and knowledge, established rules, decisions, and vocabulary. Each reported contradiction includes both claims, source locations, and severity. [H28] [H52]

Reader-sim signal and craft critique are explicitly non-equivalent: the former supplies what a reader felt and where, while the latter diagnoses why and what to change. Convergence increases confidence; disagreement triggers investigation rather than automatic override. [H53]

#### 8.2 Deterministic/mechanical support

The bundled `analyze.py` computes sentence-length statistics, opener categories, dialogue-line ratio, repeated words within a paragraph window, and pronoun distribution. It emits measurements only; it does not prove narrative quality, POV correctness, or continuity. [H54]

`meridian kg graph` is used to navigate Markdown connections, and `meridian mermaid check` validates diagrams. Semantic contradiction detection remains the continuity checker's model judgment. [H23] [H28]

#### 8.3 Audit and repair

Critic, editor, reader-sim, character-sim, and continuity-checker profiles deny write/edit tools; the writer owns prose changes and Muse owns synthesis/routing. [H17]

There is one internal contract mismatch: the editor body says not to edit unless explicitly asked for a rewrite, but its agent profile denies write and edit tools unconditionally. In that profile, an explicit rewrite request still cannot be applied directly. [H26]

#### 8.4 Repository validation

CI checks package structure, plugin manifests, minimal frontmatter presence, `cw` lint, and skill-archive construction. It does not run the creative workflow, semantic continuity fixtures, prose analyzer tests, or story-quality evaluations. [H07]

### Inference

The repository offers a strong separation between **felt response**, **focused diagnosis**, **holistic prioritization**, **continuity audit**, and **repair**. CodexWriter can reuse these responsibilities without assuming each must be a permanently separate skill.

The mechanical analyzer is correctly scoped as signal. Its metrics are suitable for baselines and anomaly detection, not for declaring prose good or bad.

### Uncertainty

- No inter-rater calibration or ground-truth continuity corpus is included.
- The source does not specify a single structured finding schema shared by critic, editor, reader-sim, and continuity roles.
- The model can miss canon that was not attached or linked; the checker is required to report partial coverage, but no recall metric exists.
- CI validation demonstrates package integrity more than behavioral correctness.

---

## 9. Human-in-the-Loop Model

### Observed

| Event | Human role |
|---|---|
| Creative direction | Author has final say; production follows confirmed direction. [H33] |
| Project setup | Proposed conventions and KB layout are shown and iterated until the author approves them. [H35] |
| Brainstorm convergence | AI alternatives remain tagged and non-canonical; the author chooses or leaves them unresolved. [H22] [H40] |
| Timeline contradiction | Both versions remain visible; the author chooses canon. [H34] |
| Potential retcon/conflict | Existing KB truth is preserved until the author or orchestrator resolves the conflict. [H37] |
| Direct file edit | The author's current disk edit is authoritative. [H19] |
| Review-to-repair | Read-only reviewers report; Muse synthesizes; Writer performs the selected prose pass. [H15] [H17] |
| Canon promotion | Memory updates wait for settled decisions or finalized chapters; provisional brainstorms must not be promoted. [H15] [H31] |

The system does not require a human question before every operation. Muse asks only when the answer would change the work and otherwise states its interpretation so the author can correct it. Writer and most workers have `ask_user` denied and rely on Muse or the prompt for clarified intent. [H15] [H17]

### Inference

Haowjy's HITL model is **event- and ambiguity-based**, not a rigid approval checklist. It reserves explicit author authority for direction, contradiction resolution, setup, and canon promotion while allowing the coordinator to keep low-risk work moving.

This is compatible with CodexWriter's goal of meaningful creative gates, but the source does not provide a machine-enforced ledger proving approval occurred.

### Uncertainty

- “Settled,” “confirmed,” and “finalized” are not represented by a typed status field.
- The author may correct Muse after it proceeds, but the repository does not define rollback semantics for work already written from a mistaken interpretation.
- No permission rule differentiates low-risk draft creation from high-impact edits to existing author prose beyond project convention and prompt scope.

---

## 10. Runtime and Maintenance

### Observed

#### 10.1 Source package and flattened distribution

`skills/` and `agents/` are the Mars source. `cw/` is a Claude/plugin distribution composed of generated lowered copies plus manually adapted or `cw`-only skills. Claude.ai receives zipped skills but not multi-agent execution; the solo Muse skill is its fallback. [H06] [H11] [H55]

The package depends on `meridian-base >=0.10.0`, does not commit `mars.lock`, and builds generated `cw` content through a temporary Mars consumer. A fresh regeneration can therefore resolve dependency output different from the one used for the pinned commit. [H10] [H12] [H56]

#### 10.2 Hooks and runtime enforcement

- A Claude pre-tool hook blocks generic `Agent` spawns and redirects users toward named Meridian agents. [H57]
- A conditional Claude stop/session-end hook runs configured Meridian `git-autosync` hooks, suppresses failures, and does nothing when Meridian or the configured hook is absent. [H58]
- A Codex shell guard blocks commands likely to wait for interactive PostgreSQL, sudo, SSH, rsync, or Git credentials unless fail-fast conditions are present. [H59]
- The committed `.codex/hooks.json` contains two developer-specific absolute paths—one Linux and one macOS—to the same hook script. Those paths are not portable to a normal checkout. [H60]

#### 10.3 CI and release checks

CI runs on `main` pushes and pull requests. It installs unversioned `meridian-cli` and Claude Code CLIs, checks Mars structure and Claude plugin manifests, performs a first-line frontmatter test, runs `sync_cw_skills.py --lint`, and builds skill zips. [H07]

The full sync command rebuilds Mars output and compares generated content, but `--lint` intentionally skips that build/drift comparison because dependency resolution may differ. CI and pre-commit both use `--lint`. [H56] [H61]

The pre-commit hook is opt-in per clone, can be bypassed with `--no-verify`, and skips plugin validation when the Claude CLI is missing. [H62]

#### 10.4 Pinned maintenance discrepancies

1. `mars.toml` and the changelog identify version `0.5.9`, while both plugin manifests remain `0.5.8`. The lint implementation rewrites and stages those versions rather than recording a validation failure, so CI can finish successfully after mutating its ephemeral checkout. [H01] [H63]
2. Both canonical and `cw` `story-planning/SKILL.md` files point all three progressive-loading bullets to nonexistent `resources/story-planning.md`; the actual resources have different names. [H64]
3. Repository guidance says CI fails on generated drift, but the executed `--lint` path skips Mars rebuild and generated drift comparison. [H61]
4. The README tables omit the bundled `web-researcher` agent and canonical `creative-research` skill. [H09]

### Inference

The multi-format packaging and solo fallback are valuable, but source-of-truth duplication creates real maintenance load. The pinned discrepancies show that schema validation and component classification are not enough; reference existence, clean-worktree checks, reproducible dependency resolution, and immutable generated provenance also matter.

The role-based model aliases are a useful abstraction. CodexWriter should borrow the capability idea, not the pinned alias names or provider-specific frontmatter.

### Uncertainty

- The analysis did not execute Mars generation, plugin validation, or the host hooks.
- It is unclear whether a current Mars install rewrites the committed `.codex/hooks.json` before use or whether consumers can encounter its absolute paths directly.
- Moving dependencies and unversioned CI installers can change fresh-build behavior after the analyzed commit without any source change.
- The package does not expose a user-facing doctor/migration tool comparable to Dewhurst or Zenstory.

---

## 11. Strengths

### Observed

1. **Clean creative-role boundaries.** One prose owner is surrounded by distinct focused critique, holistic editing, reader simulation, continuity, planning, research, and memory responsibilities. [H14] [H17]
2. **Strong author-intent contract.** Muse carries reader effect, taste, ambiguity, and failure boundaries through staffing and synthesis rather than treating a brief as only plot requirements. [H15]
3. **Practical context discipline.** The repository distinguishes attached artifacts, conversational reasoning, and pre-handoff materialization, then specifies what each role needs. [H42] [H43]
4. **Source-aware human-readable memory.** Fact diffs, chapter anchors, one-concept pages, vocab discipline, cross-links, and explicit conflict surfacing make the KB inspectable. [H36] [H37]
5. **Excellent non-canonical hygiene.** AI, hidden, rejected, uncertain, and settled material receive different treatment, and brainstorms stay outside the durable KB until promotion. [H40]
6. **Reader-centered craft stack.** Planning, prose, style, failure-mode diagnosis, reader simulation, and review all connect back to intended reader experience. [H27] [H49] [H50]
7. **Audit/repair separation.** Review roles are read-only while Muse chooses and Writer applies changes. [H17]
8. **Honest deterministic boundary.** Mechanical metrics are described as signals, while semantic continuity remains a sourced model judgment. [H28] [H54]
9. **Graceful conceptual fallback.** The solo Muse skill preserves explicit stance changes when subagents are unavailable. [H20]
10. **Thoughtful packaging model.** The repository distinguishes canonical Mars sources, generated lowered copies, and manual adaptations rather than pretending one prompt format is native everywhere. [H11] [H55]

### Inference

Haowjy is particularly valuable to CodexWriter for the **behavioral contracts around creative collaboration**: how to keep exploration open, hand work to a focused writer, collect several kinds of evidence, protect author voice, and promote only settled knowledge.

### Uncertainty

These strengths are design and implementation observations, not evidence that the package produces better fiction than alternatives in controlled tests.

---

## 12. Weaknesses / Gaps

### Observed

1. **No revisioned state transaction.** Story state is mutable Markdown with advisory reread/conflict rules; no stale-write guard or lock is defined. [H19] [H37]
2. **No deterministic earlier-revision propagation.** Timeline guidance explicitly says not to auto-adjust downstream material. [H39]
3. **No typed story-state schema.** Questions, promises/payoffs, objects, scenes, and reader knowledge are conventions or prose, not validated entities. [H23] [H37]
4. **No universal authority rule.** Author edits win, existing KB truth is preserved on conflict, and pages should avoid duplicate truth, but manuscript/outline/decision/KB precedence is not fully specified. [H19] [H36] [H37]
5. **Context selection is judgment-driven.** Useful scoping guidance exists, but no deterministic projection, budget enforcement, or retrieval-quality test does. [H42] [H43]
6. **Behavioral tests are absent from CI.** The workflow validates packaging, not end-to-end writing, continuity, or review behavior. [H07]
7. **Dependency resolution is not reproducible from the pinned commit alone.** The remote range is open-ended and `mars.lock` is ignored. [H10] [H12]
8. **Generated-distribution drift is not actually checked in CI.** The CI-selected lint mode skips the build/diff path. [H56] [H61]
9. **Pinned version drift.** Package metadata says `0.5.9`; both plugin manifests say `0.5.8`; lint mutates rather than fails. [H63]
10. **Broken progressive-loading references.** `story-planning` routes three tasks to a missing resource path. [H64]
11. **Non-portable committed Codex hook configuration.** Absolute developer paths are embedded in `.codex/hooks.json`. [H60]
12. **Inventory documentation drift.** Public tables omit an agent and a canonical skill. [H09]
13. **Editor contract mismatch.** The body conditionally allows a requested rewrite, while the profile always denies edit/write tools. [H26]

### Inference

The largest design risk is that strong prose and workflow methodology can create confidence without equally strong state correctness. In a long project, source-aware Markdown helps people investigate a contradiction; it does not guarantee that every dependent artifact was found or updated.

The largest maintenance risk is duplicated, partly generated distribution state without a locked dependency graph or CI rebuild comparison.

### Uncertainty

- Meridian may provide additional conflict, graph, or autosync guarantees outside this repository; the moving dependency prevents attributing them to the pinned application snapshot.
- Some identified defects may be corrected immediately after the pinned commit.
- A lightweight Markdown model may be an intentional product choice rather than a deficiency for smaller projects; the scaling boundary is not benchmarked.

---

## 13. Relevance to CodexWriter

Every disposition below is provisional.

### Observed reusable responsibilities

| Haowjy responsibility | CodexWriter relevance |
|---|---|
| Author-facing Muse | Strong analogue for `fiction-orchestrator`: preserve intent, staff specialists, synthesize, and own the verdict. [H15] |
| Brainstorm provenance and sandbox | Strong evidence for non-canonical exploration inside concept, world, character, and planning work. [H40] |
| One production writer with modes | Strong evidence for keeping `scene-writing` cohesive while exposing draft/revise/bridge/alternate/polish modes. [H24] [H47] |
| Focused critic + holistic editor | Supports distinct developmental review and prose-editing modes without forcing both into one undifferentiated reviewer. [H25] [H26] |
| Persona-bound reader simulation | Direct evidence for retaining `reader-simulation` as a first-class responsibility. [H27] [H53] |
| Story-memory/context contracts | Evidence for cross-cutting context assembly and post-work fact extraction. [H37] [H42] |
| Style references | Supports an optional/cross-cutting voice-profile responsibility feeding writers and reviewers. [H29] [H45] |
| Continuity checker | Supports one Phase 1 `continuity` responsibility with evidence-backed, read-only audit behavior. [H28] |
| Creative research | Supports a research extension that supplies sourced detail but cannot decide story fit. [H30] |

### Provisional candidate architectural borrowing

- **Adapt:** separate author-facing coordination from focused worker contexts; keep final synthesis with the orchestrator.
- **Adapt:** use the smallest sufficient context and materialize decisions before handoff when contradiction would be costly.
- **Adapt:** treat critique, editor judgment, reader experience, and continuity as different evidence channels.
- **Adapt:** preserve one prose owner while exposing explicit production modes.
- **Adapt:** keep durable knowledge separate from drafts/brainstorms and require explicit promotion of settled facts.
- **Adapt:** distinguish current disk evidence, source anchors, author decisions, AI proposals, rejected options, and hidden information.
- **Adapt:** make style references task-selectable rather than one monolithic voice prompt.
- **Adapt:** keep deterministic measurements explicitly subordinate to literary and semantic judgment.
- **Investigate:** select models by capability/cognitive role at runtime, without adopting Haowjy's provider-specific aliases.

### Provisional implementation-level borrowing requiring license/provenance handling

- Any direct reuse of agent bodies, skill prose, style-analysis templates, source-tag syntax, review checklists, hooks, sync scripts, or prose-analysis code.
- Any reuse of `cw/` dependency-derived skills requires identifying their exact `meridian-base` sources and licenses first.
- The optional mechanical analyzer is small and legible, but direct copying would still require Apache-2.0 compliance, testing, and a decision about its English-centric tokenization and quotation assumptions.

### Provisional patterns to avoid

- Avoid treating advisory “read before write” instructions as stale-write protection.
- Avoid promoting current-state Markdown conventions into a claim of deterministic revision propagation.
- Avoid open-ended build dependencies when committing generated artifacts.
- Avoid validation commands that silently rewrite/stage version files while reporting success.
- Avoid saying CI checks generated drift when the invoked mode skips the build/diff.
- Avoid resource links that packaging validation does not confirm exist.
- Avoid committed runtime configuration containing developer-specific absolute paths.
- Avoid public inventory tables assembled independently from the shipped component manifest.

### Inference

Haowjy materially strengthens the case for retaining CodexWriter's current orchestrator, scene writer, continuity, prose editing, and reader-simulation responsibilities. It also strengthens—but does not settle—the candidates for story review, context assembly, story memory, and voice profiling.

### Uncertainty

- The eventual skill boundaries should wait for all seven source analyses.
- CodexWriter still needs to choose whether context and state maintenance are user-facing skills, internal services, or orchestrator contracts.
- The source does not answer whether Markdown alone can meet CodexWriter's long-form state guarantees.

---

## 14. Detailed Evidence

### Observed: claim-level traceability map

| Claim | Exact pinned evidence |
|---|---|
| H01 | [`mars.toml`, lines 1–7](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/mars.toml#L1-L7); [`CHANGELOG.md`, lines 1–10](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/CHANGELOG.md#L1-L10) |
| H02 | [`README.md`, lines 6–13](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L6-L13); [`README.md`, lines 73–115](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L73-L115) |
| H03 | [`sync_cw_skills.py`, lines 42–104](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L42-L104); [`sync_cw_skills.py`, lines 409–414](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L409-L414) |
| H04 | [`README.md`, lines 110–131](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L110-L131); [`agents/muse.md`, lines 81–87](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/muse.md#L81-L87) |
| H05 | [`.github/workflows/ci.yml`, lines 9–57](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.github/workflows/ci.yml#L9-L57); [`analyze.py`, lines 1–21](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/prose-critique/analyze.py#L1-L21); [`.claude/hooks/context-autosync/run.sh`, lines 1–26](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude/hooks/context-autosync/run.sh#L1-L26); [`.claude-plugin/marketplace.json`, lines 1–17](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude-plugin/marketplace.json#L1-L17); [`mars.toml`, lines 1–18](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/mars.toml#L1-L18) |
| H06 | [`README.md`, lines 22–71](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L22-L71); [`README.md`, lines 171–180](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L171-L180); [`mars.toml`, lines 12–18](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/mars.toml#L12-L18) |
| H07 | [`.github/workflows/ci.yml`, lines 1–57](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.github/workflows/ci.yml#L1-L57) |
| H08 | [`LICENSE`, lines 1–5](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/LICENSE#L1-L5); [`LICENSE`, lines 176–201](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/LICENSE#L176-L201) |
| H09 | [`README.md`, lines 116–149](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/README.md#L116-L149); [`sync_cw_skills.py`, lines 45–104](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L45-L104) |
| H10 | [`mars.toml`, lines 5–10](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/mars.toml#L5-L10) |
| H11 | [`AGENTS.md`, lines 43–61](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/AGENTS.md#L43-L61); [`sync_cw_skills.py`, lines 42–80](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L42-L80) |
| H12 | [`.gitignore`, lines 8–18](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.gitignore#L8-L18) |
| H13 | [`citations.md`, lines 1–46](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-principles/resources/citations.md#L1-L46) |
| H14 | [`docs/architecture.md`, lines 1–6](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/docs/architecture.md#L1-L6); [`docs/architecture.md`, lines 55–96](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/docs/architecture.md#L55-L96) |
| H15 | [`agents/muse.md`, lines 45–87](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/muse.md#L45-L87) |
| H16 | [`creative-writing-modes/SKILL.md`, lines 9–33](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-modes/SKILL.md#L9-L33); [`story-review/SKILL.md`, lines 9–38](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/SKILL.md#L9-L38) |
| H17 | [`agents/writer.md`, lines 24–60](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/writer.md#L24-L60); [`agents/critic.md`, lines 25–51](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/critic.md#L25-L51); [`agents/editor.md`, lines 25–40](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/editor.md#L25-L40); [`agents/reader-sim.md`, lines 24–34](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/reader-sim.md#L24-L34); [`agents/continuity-checker.md`, lines 21–37](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/continuity-checker.md#L21-L37) |
| H18 | [`AGENTS.md`, lines 9–13](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/AGENTS.md#L9-L13); [`creative-writing-craft/SKILL.md`, lines 9–21](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/SKILL.md#L9-L21) |
| H19 | [`writing-artifacts.md`, lines 8–44](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/writing-artifacts.md#L8-L44) |
| H20 | [`creative-writing-muse/SKILL.md`, lines 10–55](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-muse/SKILL.md#L10-L55) |
| H21 | [`writing-staffing/SKILL.md`, lines 27–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-staffing/SKILL.md#L27-L35); [`writing-staffing/SKILL.md`, lines 39–83](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-staffing/SKILL.md#L39-L83) |
| H22 | [`agents/brainstormer.md`, lines 39–63](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/brainstormer.md#L39-L63) |
| H23 | [`agents/outliner.md`, lines 35–56](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/outliner.md#L35-L56) |
| H24 | [`agents/writer.md`, lines 39–60](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/writer.md#L39-L60) |
| H25 | [`agents/critic.md`, lines 41–54](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/critic.md#L41-L54); [`prose-critique.md`, lines 27–79](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/prose-critique.md#L27-L79) |
| H26 | [`agents/editor.md`, lines 43–93](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/editor.md#L43-L93); [`editorial-review.md`, lines 42–88](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/editorial-review.md#L42-L88) |
| H27 | [`reader-sim/SKILL.md`, lines 9–53](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/reader-sim/SKILL.md#L9-L53) |
| H28 | [`agents/continuity-checker.md`, lines 40–72](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/continuity-checker.md#L40-L72) |
| H29 | [`agents/style-creator.md`, lines 45–52](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/agents/style-creator.md#L45-L52); [`style-analysis.md`, lines 14–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/resources/style-analysis.md#L14-L35) |
| H30 | [`creative-research/SKILL.md`, lines 12–77](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-research/SKILL.md#L12-L77) |
| H31 | [`writing-staffing/SKILL.md`, lines 53–67](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-staffing/SKILL.md#L53-L67); [`writing-staffing/SKILL.md`, lines 103–137](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-staffing/SKILL.md#L103-L137) |
| H32 | [`writing-staffing/SKILL.md`, lines 16–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-staffing/SKILL.md#L16-L35) |
| H33 | [`creative-direction.md`, lines 11–31](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/creative-direction.md#L11-L31) |
| H34 | [`continuity-timeline.md`, lines 1–18](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/brainstorming/continuity-timeline.md#L1-L18) |
| H35 | [`BOOTSTRAP.md`, lines 25–55](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/bootstrap/project-setup/BOOTSTRAP.md#L25-L55) |
| H36 | [`kb-management/SKILL.md`, lines 15–33](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/cw/skills/kb-management/SKILL.md#L15-L33); [`kb-management/SKILL.md`, lines 48–75](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/cw/skills/kb-management/SKILL.md#L48-L75); [`kb-management/SKILL.md`, lines 104–124](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/cw/skills/kb-management/SKILL.md#L104-L124) |
| H37 | [`fact-extraction.md`, lines 9–45](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/fact-extraction.md#L9-L45) |
| H38 | [`writing-issues.md`, lines 9–48](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/writing-issues.md#L9-L48) |
| H39 | [`continuity-timeline.md`, lines 20–61](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/brainstorming/continuity-timeline.md#L20-L61); [`fact-extraction.md`, lines 29–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/fact-extraction.md#L29-L35) |
| H40 | [`brainstorming.md`, lines 37–74](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/brainstorming.md#L37-L74); [`brainstorming.md`, lines 87–95](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/brainstorming.md#L87-L95) |
| H41 | [`story-context.md`, lines 35–57](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/story-context.md#L35-L57) |
| H42 | [`story-context.md`, lines 8–31](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/story-context.md#L8-L31) |
| H43 | [`story-context.md`, lines 33–75](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/story-context.md#L33-L75) |
| H44 | [`story-context.md`, lines 77–96](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-memory/resources/story-context.md#L77-L96) |
| H45 | [`style-analysis.md`, lines 14–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/resources/style-analysis.md#L14-L35); [`style-analysis.md`, lines 57–89](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/resources/style-analysis.md#L57-L89) |
| H46 | [`story-architecture.md`, lines 9–62](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/story-architecture.md#L9-L62); [`chapter-and-scene.md`, lines 34–47](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/resources/story-architecture/chapter-and-scene.md#L34-L47) |
| H47 | [`prose-modes.md`, lines 1–78](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-modes/resources/prose-modes.md#L1-L78) |
| H48 | [`prose-writing.md`, lines 9–99](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/resources/prose-writing.md#L9-L99); [`scene-construction.md`, lines 9–67](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/resources/scene-construction.md#L9-L67) |
| H49 | [`writing-principles/SKILL.md`, lines 13–76](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-principles/SKILL.md#L13-L76) |
| H50 | [`failure-modes.md`, lines 13–60](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-principles/resources/failure-modes.md#L13-L60); [`failure-modes.md`, lines 64–150](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/writing-principles/resources/failure-modes.md#L64-L150) |
| H51 | [`creative-writing-craft/SKILL.md`, lines 16–21](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/creative-writing-craft/SKILL.md#L16-L21) |
| H52 | [`continuity.md`, lines 1–64](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/prose-critique/continuity.md#L1-L64) |
| H53 | [`reader-sim-signal.md`, lines 1–56](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/reader-sim-signal.md#L1-L56) |
| H54 | [`analyze.py`, lines 137–218](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/prose-critique/analyze.py#L137-L218); [`analyze.py`, lines 222–300](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-review/resources/prose-critique/analyze.py#L222-L300) |
| H55 | [`AGENTS.md`, lines 43–61](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/AGENTS.md#L43-L61); [`create_skill_zips.py`, lines 1–11](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/create_skill_zips.py#L1-L11); [`create_skill_zips.py`, lines 81–107](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/create_skill_zips.py#L81-L107) |
| H56 | [`sync_cw_skills.py`, lines 1–20](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L1-L20); [`sync_cw_skills.py`, lines 253–305](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L253-L305) |
| H57 | [`.claude/hooks/deny-generic-agent/run.sh`, lines 1–19](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude/hooks/deny-generic-agent/run.sh#L1-L19); [`.claude/hooks/deny-generic-agent/run.sh`, lines 25–71](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude/hooks/deny-generic-agent/run.sh#L25-L71) |
| H58 | [`.claude/hooks/context-autosync/run.sh`, lines 1–26](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude/hooks/context-autosync/run.sh#L1-L26); [`.claude/hooks/context-autosync/claude.json`, lines 1–16](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude/hooks/context-autosync/claude.json#L1-L16) |
| H59 | [`.codex/hooks/deny-interactive-prompts/run.py`, lines 257–304](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.codex/hooks/deny-interactive-prompts/run.py#L257-L304) |
| H60 | [`.codex/hooks.json`, lines 1–23](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.codex/hooks.json#L1-L23) |
| H61 | [`AGENTS.md`, lines 50–57](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/AGENTS.md#L50-L57); [`sync_cw_skills.py`, lines 257–305](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L257-L305); [`.github/workflows/ci.yml`, lines 53–57](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.github/workflows/ci.yml#L53-L57) |
| H62 | [`.githooks/pre-commit`, lines 1–35](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.githooks/pre-commit#L1-L35); [`AGENTS.md`, lines 90–96](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/AGENTS.md#L90-L96) |
| H63 | [`mars.toml`, lines 1–3](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/mars.toml#L1-L3); [`.claude-plugin/marketplace.json`, lines 1–15](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/.claude-plugin/marketplace.json#L1-L15); [`cw/.claude-plugin/plugin.json`, lines 1–9](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/cw/.claude-plugin/plugin.json#L1-L9); [`sync_cw_skills.py`, lines 360–415](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/scripts/sync_cw_skills.py#L360-L415) |
| H64 | [`skills/story-planning/SKILL.md`, lines 9–17](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/skills/story-planning/SKILL.md#L9-L17); [`cw/skills/story-planning/SKILL.md`, lines 7–15](https://github.com/haowjy/creative-writing-skills/blob/fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3/cw/skills/story-planning/SKILL.md#L7-L15) |

### Observed: licensing/provenance paths checked

| Pinned path | Result |
|---|---|
| `LICENSE` | Present; Apache License 2.0; blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` |
| `NOTICE` | Not found |
| `NOTICE.md` | Not found |
| `ATTRIBUTION` | Not found |
| `ATTRIBUTION.md` | Not found |

### Observed: reference-integrity paths checked

| Pinned path | Result |
|---|---|
| `skills/story-planning/resources/story-planning.md` | Not found; referenced three times by the canonical `story-planning/SKILL.md` |
| `cw/skills/story-planning/resources/story-planning.md` | Not found; referenced three times by the flattened `cw` copy |

### Inference

The evidence map establishes source behavior and repository defects at one commit. It does not convert provisional CodexWriter candidates into adopted design.

### Uncertainty

- “Not found” records the exact pinned-tree inspection result; it cannot establish facts about uncommitted, release-only, or external dependency files.
- Dependency-derived `cw` files need an upstream lineage map before direct reuse.

---

## 15. Provisional CodexWriter Disposition

All entries are provisional and require later comparative synthesis.

### Provisional retain / strongly investigate candidates

| Responsibility | Provisional disposition | Reason |
|---|---|---|
| Author-facing orchestration | **Retain responsibility** | Muse preserves intent, staffs work, synthesizes evidence, and owns the verdict. |
| Concept/world/character exploration | **Retain responsibility** | Tagged alternatives and ambiguity preservation protect creative agency. |
| Narrative/scene planning | **Retain responsibility** | Nested structure, state-change beats, and setup/payoff links are reusable. |
| Scene writing | **Retain responsibility** | One prose owner with explicit production modes supports voice continuity. |
| Continuity | **Retain as one Phase 1 responsibility** | Read-only evidence-backed audit is strong; state-write boundaries remain undecided. |
| Prose editing | **Retain responsibility** | Large-to-small editing and voice protection complement focused critique. |
| Reader simulation | **Retain responsibility** | Persona and knowledge boundaries create an experiential evidence channel. |
| Story memory | **Strongly investigate cross-cutting responsibility** | Post-work fact diffs and source anchors are useful, but storage design remains open. |
| Context assembly | **Strongly investigate cross-cutting responsibility** | File/history/materialization choices operationalize smallest-sufficient context. |

### Provisional adapt candidates

- **Adapt** Muse's intent packet: reader effect, emotional target, constraints, taste, ambiguity, and wrong-success boundary.
- **Adapt** brainstorm source tags, but choose a CodexWriter-native representation only after state synthesis.
- **Adapt** focused critic lanes, holistic editorial priority, and persona reader signal into a shared finding contract.
- **Adapt** style references as independent, selectively loaded artifacts separated from canon.
- **Adapt** “state diff after prose” while adding explicit authority, revision, conflict, and propagation semantics.
- **Adapt** one-concept/source-aware KB conventions without assuming Markdown must be the sole implementation.
- **Adapt** runtime capability degradation and solo stance switching.

### Provisional merge/split candidates

- **Merge candidate:** keep fresh draft, bridge, alternate take, and prose revision as modes of `scene-writing`, not separate agent identities.
- **Merge candidate:** keep creative direction and divergent brainstorming inside existing concept/world/character/planning responsibilities unless later sources justify a separate public skill.
- **Split candidate:** keep holistic developmental/story review distinguishable from line/copy/proof editing, but defer the final public module boundary.
- **Split candidate:** keep story-memory update and continuity audit conceptually separate while preserving one Phase 1 `continuity` skill until synthesis authorizes a change.

### Provisional extension candidates

- **Extension candidate:** creative web/domain research with source confidence and contradiction reporting.
- **Extension candidate:** style/voice profile generation when an author supplies samples.
- **Extension candidate:** multi-model duplicate review for pivotal/disputed judgments.

### Provisional defer

- **Defer** Markdown-only canonical state.
- **Defer** exact KB directory taxonomy.
- **Defer** dedicated `story-memory`, `story-review`, `context-manager`, or `style-profiler` public skill names.
- **Defer** role-to-model aliases until runtime capability design.
- **Defer** dependency-derived implementation reuse until exact provenance is established.

### Provisional reject / avoid candidates

- **Reject as evidence of safety:** advisory reread-before-write as a substitute for stale-write protection.
- **Reject:** automatic canon promotion from brainstorm or model inference.
- **Reject:** calling Markdown link traversal deterministic semantic continuity.
- **Reject:** mutable dependency resolution for committed generated artifacts.
- **Reject:** validation that repairs derived metadata without failing or checking the resulting diff.
- **Reject:** developer-specific absolute runtime paths.
- **Reject:** public component inventories maintained separately from the actual package manifest.

---

## 16. Four-Source Comparative Baseline

### Observed source evidence and provisional comparative inference

The source columns summarize the four completed source analyses. Comparative rankings and the final column are **Inference**.

| Dimension | Lensetek | Dewhurst | Zenstory | Haowjy | Provisional Phase 1 reading |
|---|---|---|---|---|---|
| Primary contribution | Broad responsibility taxonomy | Executable Markdown/YAML contract and continuity CLI | Transactional long-form state and runtime control plane | Creative staffing, craft, reader evidence, and Markdown story memory | The four remain complementary |
| Orchestration | Broad lifecycle routing | File/CLI workflows | Scenario router, stages, hooks, transactions | Author-facing Muse plus cognitive-role staffing | Zenstory is strongest operationally; Haowjy is strongest on creative stance separation |
| State authority | Shallow/unclear | Distributed typed files with ambiguity | Revisioned JSON authority inside tracking | Current Markdown files; author edits win; one concept per page | No final CodexWriter authority model yet |
| Dynamic state | Limited | Character/scene/current-state artifacts | Bounded current snapshots and projections | Evolving character/timeline/wiki pages | Haowjy improves human process, not machine transactionality |
| History/revision | Limited | Workflow-updated records | Snapshot plus chapter records; guided recalculation | Sourced current pages; note earlier changes; do not auto-propagate | Deterministic downstream replay remains unsolved |
| Stale-write safety | Not central | None found | Sequential revision guard, not concurrency lock | Reread/surface-conflict instructions only | Zenstory remains the only concrete stale sequential write mechanism so far |
| Human inspectability | High | High | High projections, JSON dynamic authority | High, editable Markdown | Inspectability alone does not settle authority or propagation |
| Context | Responsibility handoffs | Explicit reloads | Bounded projections and far-field query | Role-specific files/history/materialization; no hard budget | Haowjy adds the best qualitative staffing/context rubric |
| Character knowledge | Responsibility | Representable | Explicit snapshots and reader-truth split | Explicit extraction/handoff category | First-class representation still open |
| Reader knowledge | Reader role | Representable | Dedicated reader-known timeline | Explicit concept, no dedicated persistent store | Zenstory remains structurally strongest |
| Questions/promises | Planning responsibility | Typed records | Generic threads/foreshadowing | Brainstorm questions and outline links, untyped | Dewhurst remains strongest structurally |
| Reader simulation | Explicit responsibility | Limited | Review approximation | Dedicated persona-bound experiential role | Haowjy supplies the strongest implementation evidence so far |
| Evaluation | Broad roles | CLI checks plus review | Scripts/hooks plus multi-agent review | Critic/editor/reader/continuity separation plus mechanical metrics | Haowjy clarifies evidence types; no source proves semantic truth mechanically |
| Creative craft | Broad | Comparatively light | Deep commercial Chinese web-fiction method | Deep general prose, style, reader-reward, and failure-mode method | Haowjy is the strongest general craft source so far |
| Non-canonical work | Workflow concept | Working artifacts | Staged work and author gates | Explicit AI/hidden/rejected tags plus work→KB promotion | Haowjy gives the clearest lightweight provenance convention |
| Runtime fallback | Limited | CLI/package behavior | Broad adapters and capability degradation | Mars/Claude distribution plus solo stance-switching | Haowjy's fallback is simpler; Zenstory's control plane is broader |
| Maintenance | Limited | Doctor/migration/reindex/CI | Extensive cross-runtime scripts/tests | Generation/lint/zips/hooks, but reproducibility and drift defects | Packaging method is useful; execution details should not be copied unchanged |

### Inference

After four sources, the main synthesis axis is not “structured state or creative craft.” CodexWriter likely needs both: explicit authority and update semantics for machine-sensitive continuity, plus Haowjy-style author intent, craft, context judgment, and evidence-channel separation.

Haowjy argues against over-centralizing creative uncertainty. Brainstorm options, style evidence, and reader response do not naturally belong in the same authority mechanism as current character location or a resolved timeline fact.

### Uncertainty

- Four sources still do not establish the right minimum state schema or historical representation.
- Later sources may provide stronger constitution, context-LOD, narrative epistemology, or blind-reader mechanisms.
- The comparison evaluates contracts and implementation evidence, not equivalent end-to-end story outputs.

---

## 17. Answers to Questions Carried From Zenstory

### Observed evidence and inference boundaries

| Carried question | Haowjy evidence-based answer |
|---|---|
| Synthesize state now or inspect Haowjy first? | Haowjy adds materially different evidence: human-editable wiki state, explicit promotion rules, author authority, and advisory shared-workspace conflict handling. **Inference:** inspecting it before synthesis was justified, but it does not close the core state questions. |
| Smallest useful authority domains? | Haowjy separates author manuscript space, work artifacts, canon/wiki/timeline/character/style/vocab/issues, and direct author edits. It favors one truth per concept but does not define universal cross-domain precedence. |
| Which concepts are first-class typed entities? | None are typed by a validated story-state schema. Character state, knowledge, relationships, timeline, canon, vocab, style, and issues receive explicit Markdown conventions; questions, objects, and promise/payoff pairs remain weaker. |
| Historical representation for earlier revisions? | Timeline guidance records the change and downstream questions but explicitly does not auto-adjust later material. **Inference:** this is guided semantic recalculation, not replay. |
| Multi-writer locking? | Shared workers are told to reread disk and surface collisions; no lock or revision guard exists. **Inference:** Haowjy supports a single prose owner plus parallel read-only reviewers better than concurrent canonical writers. |
| Can human-editable Markdown be canonical? | Yes as a convention: current files and author edits are authoritative. No evidence shows deterministic projections or stale-write checks over those files. |
| What wins when prose and state disagree? | Existing KB truth is preserved while conflict is surfaced; author/orchestrator decides whether prose, KB, or terminology changes. No universal automated precedence rule exists. |
| Context assembly boundary? | Haowjy places the methodology in `story-memory`, with Muse making the actual file/history/materialization decision for each spawn. **Inference:** this supports a cross-cutting contract, whether or not it becomes a public skill. |
| Canon candidates and exploration? | Work artifacts remain non-canonical; AI, hidden, rejected, vague, and author-stated material are distinguished; only settled knowledge is promoted. |
| Generalizable craft? | Reader rewards, author-intent preservation, prose modes, style sharding, and review separation generalize more readily than any provider/model alias. |
| Reader simulation? | Haowjy supplies a dedicated persona- and knowledge-bound experiential method, strengthening the case that this remains first-class. |
| Runtime guarantees/degradation? | Mars/Claude agents provide separated contexts and tool profiles; the solo Muse fallback switches stances in one context. The source does not provide a formal capability report, and enforcement varies by host. |

### Inference

Haowjy shifts the comparison from “how should state be stored?” toward “which knowledge should become state at all?” Its promotion discipline and ambiguity preservation are as important as its folder layout.

### Uncertainty

The four-source evidence still does not authorize a final state architecture or a change to CodexWriter's stable Phase 1 skill list.

---

## 18. Questions to Carry Forward

### Observed basis

1. Can JeroTan's constitution/clarification model provide the missing explicit status for “settled” direction and canon promotion?
2. Can wgwtest provide a stronger machine-usable distinction among author truth, narrator/POV access, character knowledge, and reader knowledge?
3. Can Rhavekost's blind-reader/editing passes strengthen Haowjy's persona boundary and stopping points?
4. What minimum typed entities are justified after comparing all sources: character state, relationships, timeline events, scenes, objects, questions, promises/payoffs, foreshadowing, and issues?
5. Should canonical human-editable files carry embedded revisions, or should CodexWriter pair them with a revisioned index/transaction layer?
6. What exact gate promotes `<AI>` or other candidate material into canon, and how is that decision recorded?
7. Can earlier-chapter revision propagation be partly deterministic through dependency edges while leaving semantic recalculation to agents and humans?
8. Should the initial system enforce one canonical writer and parallel read-only reviewers, or design multi-writer locking immediately?
9. Should context assembly remain an orchestrator contract or become a testable internal service with budgets, provenance, and coverage reporting?
10. Can a shared structured finding schema preserve the distinct semantics of critic, editor, reader-sim, and continuity reports?
11. How should author voice/preferences remain separate from story canon and portable across projects without creating unsafe imitation behavior?
12. Which runtime guarantees are required for a “supported” host, and how should degraded role isolation be disclosed?
13. What reproducible packaging/provenance policy should govern generated or dependency-derived skill distributions?
14. What behavioral fixtures should CI run for state updates, context assembly, continuity, canon promotion, and audit/repair separation?

### Inference

The next source should continue the provisional order with JeroTan unless review directs otherwise. A separate, explicitly authorized synthesis can begin after enough evidence exists to answer authority, promotion, history, and context questions without treating any one source as the default implementation.

### Uncertainty

No architecture choice, crosswalk change, or stable skill-list change is made by this analysis. All answers, comparisons, and dispositions remain provisional until review and a separately authorized synthesis step.
