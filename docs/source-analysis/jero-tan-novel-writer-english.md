# Source Analysis: JeroTan/novel-writer-english

> **Upstream pin:** `6d836f23281e240eed36d50529424e086c8ff42d`  
> **Default branch:** `main`  
> **Latest-status check:** a final live comparison on 2026-08-26 found the pin identical to `main` (`ahead_by: 0`, `behind_by: 0`); no newer default-branch commits existed at analysis time  
> **Lineage reference pin:** `wordflowlab/novel-writer-skills@5bc9b373ff609e8910e0e8d179e4a697bf2b1268`  
> **Analysis date:** 2026-08-26  
> **Decision status:** evidence review only; every CodexWriter disposition is provisional

This document records JeroTan behavior before making CodexWriter architecture or crosswalk decisions. It does not modify `ARCHITECTURE.md`, `docs/crosswalk.md`, or any stable skill list.

## Evidence Labels

- **Observed** — directly supported by a file, line range, executable test, or complete-tree inventory at the pinned commit.
- **Inference** — an interpretation of observed evidence, not a claim that the source implements the inferred CodexWriter design.
- **Uncertainty** — something the pinned artifacts or bounded verification did not establish.

Claim IDs `J01`–`J64` resolve to immutable file-and-line links in Section 14. JeroTan evidence links use the JeroTan pin above. The two independently checked lineage links use the separate wordflowlab pin above. No evidence link uses `main`, `master`, or another mutable ref.

## 1. Repository Snapshot

### Observed

| Item | Pinned observation |
|---|---|
| Repository | `https://github.com/JeroTan/novel-writer-english` |
| Commit | `6d836f23281e240eed36d50529424e086c8ff42d` |
| Default branch | `main` |
| Latest default-branch status | Live `main` resolved to the pinned commit on 2026-08-26 |
| Primary implementation language | JavaScript / Node.js, with Markdown command and skill definitions plus JSON templates |
| Package | `novel-writer-english@1.5.1`; Node `>=18.0.0`; `node --test` test script [J02] |
| Active pinned inventory | 86 non-`.old/` blobs: 71 under `src/`, including 29 command prompts, 26 `SKILL.md` files, and 13 templates; plus installer, MCP server, package, docs, attribution, license, and one test file [J03] |
| Archived inventory | 94 blobs under `.old/v1/`; the installer reads active material from `src/`, not the archive [J04] |
| Core workflow | Constitution → Specify → Clarify → Plan → Tasks → Write → Edit → Review [J11] |
| Runtime targets | Claude Code, Gemini CLI, OpenCode, Codex CLI, and manual copy/paste; installed MCP support is configured for the four CLI hosts [J01] [J04] |
| Executable verification | `npm test` passed all 11 tests on 2026-08-26 under Node `v24.19.0`; the tests cover story lookup, chapter inventory, format errors, MCP registration, configuration merging, project-root binding, Windows argument encoding, and bounded cache reset [J53] [J54] |

The README describes a structured eight-step writing assistant, a 13-item draft preflight, tracking files, a read-only lookup MCP, six genre packs, long-document splitting, and multi-platform delivery. [J01]

### Inference

The active source is best understood as a **file-oriented novel workflow with a deterministic read-only retrieval sidecar**. Most creative operations remain prompt contracts executed by the selected assistant; JavaScript supplies installation, format parsing, chapter discovery, search, and MCP transport rather than an autonomous multi-agent story engine.

Its most distinctive contribution after the first four sources is the combination of:

1. explicit author-facing constitution and clarification stages;
2. anti-god-file sharding contracts;
3. a tightly gated chapter editor;
4. typed-but-partly prompt-maintained tracking files; and
5. tested, source-locating, read-only access to a subset of story data.

### Uncertainty

- The analysis did not run an end-to-end novel project through every command on every supported host.
- Test success establishes the exercised JavaScript behavior, not semantic story correctness or prompt compliance by every model/host.
- Repository activity is recent [J05], but no claim about production maturity, user adoption, or broad project quality follows from age, stars, commit count, or the maintenance discrepancies recorded later.
- The archived `.old/v1/` tree is provenance and maintenance evidence; it is not treated as the installed active workflow.

## 2. Licensing and Provenance

### Observed

| Check | Evidence |
|---|---|
| JeroTan license | Exact root `LICENSE`; MIT text; copyright lines for the 2025 Novel Writer Team and 2026 JeroTan translation/re-architecture [J06] |
| JeroTan license blob | `cde9a1380b1b52717635a251a991df489fca9663` |
| `NOTICE` | Not found in the complete pinned 180-blob tree |
| `ATTRIBUTION.md` | Exact root file found; declares an English translation and re-architecture of `wordflowlab/novel-writer-skills`, names wordflowlab/wutongci, says the original license is MIT, and distinguishes original methodology from JeroTan additions [J07] |
| README lineage | Independently repeats that the source adapts the original methodology and later calls itself a translation and re-architecture [J08] |
| Declared adaptation scope | Platform-agnostic delivery, an editor pass, and additional Western-market genre knowledge [J07] |
| Original license check | Exact `wordflowlab/novel-writer-skills` root `LICENSE` at independently pinned commit `5bc9b373ff609e8910e0e8d179e4a697bf2b1268`; MIT text and 2025 Novel Writer Team copyright [J09] |
| Package metadata | JeroTan package declares MIT and publishes `bin/` and `src/` [J02] |
| Package contents caveat | `.npmignore` explicitly excludes `ATTRIBUTION.md`, the root `SKILL.md`, changelog, metadata, tests, archive, and version history; a local `npm pack --dry-run` confirmed that `LICENSE` and `README.md` remain included while `ATTRIBUTION.md` does not [J10] [J62] |

### Inference

The repository provides substantially better derivative-lineage evidence than a badge-only claim: both the derivative and declared original license files were checked at immutable commits, the derivative root license preserves the earlier copyright line, and the declared methodology lineage was compared against the independently pinned original README. [J64]

Responsibility-level comparison is safe to continue. Any copying of prompt text, templates, parser code, installer code, or test fixtures into CodexWriter would still require file-level provenance tracking, MIT notice preservation, and a deliberate decision about how the separately maintained `ATTRIBUTION.md` information is carried into distributed artifacts.

### Uncertainty

- This is engineering provenance review, not legal advice.
- The analysis did not compute a file-by-file similarity or authorship diff between the two repositories.
- The original repository was checked at its current default-branch pin for license and high-level lineage only; that pin is not asserted to be the exact revision JeroTan translated.
- The npm package includes the derivative README’s attribution paragraph and the root license, but the consequences of excluding the dedicated attribution file require separate legal/release review.

## 3. Architectural Thesis

### Observed

The root methodology assigns each stage an artifact: creative principles, a lean specification, clarified facts, a chapter plan, a task ledger, manuscript chapters, chapter-local edits, and a broad review report. [J11]

The project topology separates:

- author memory in `memory/`;
- story-level specification, plan, tasks, metadata, and manuscript;
- detailed Markdown knowledge;
- machine-readable tracking JSON;
- optional exploratory drafts;
- optional comics and sheet outputs; and
- reusable templates and skills. [J12]

`utility-guide-me` is a state-sensitive router. It checks file existence and task markers, then recommends the next command; it does not itself execute a hidden workflow graph. [J13]

The MCP layer is deliberately read-only. Its server annotations mark tools read-only, non-destructive, idempotent, and closed-world; the guide says command prompts retain ownership of every file update. [J14]

The specification is intentionally lean, while detailed character, voice, location, world, glossary, and strategic-reversal canon lives in dedicated knowledge files. [J15]

### Inference

JeroTan’s organizing principle is **progressive formalization through shared project artifacts**:

`author intent → bounded specification → resolved ambiguities → executable chapter plan → task state → prose → gated local edits → broad QA`.

The architecture is hybrid rather than purely prompt-only:

- prompts define creative and mutation behavior;
- Markdown keeps most author-visible truth;
- JSON gives selected dynamic domains stable shapes; and
- the MCP service provides deterministic retrieval and structural validation without write authority.

This remains materially different from Zenstory’s state-first transactional control plane. JeroTan supplies stronger artifact contracts and lookup code than Lensetek, Dewhurst, or Haowjy, but no global transaction or revision boundary unifies its files.

### Uncertainty

- “Canonical” is explicit for the knowledge files and implicit for several other core documents; no total precedence order is defined among constitution, specification, plan, knowledge, tracking, and manuscript.
- The active distribution contains no multi-agent definitions. Specialist names are workflow modes/commands, not independently scheduled workers.
- A prompt contract may be followed differently across supported assistants; the repository tests the JavaScript layer, not host-level prompt fidelity.

## 4. Workflow and Orchestration

### Observed

#### 4.1 Entry point and required sequence

`utility-guide-me` detects which core artifacts and task states exist, then routes the user into the eight core steps or the optional comics workflow. [J13]

The concise installed guide presents the core order as:

1. `/constitution`
2. `/specify`
3. `/clarify`
4. `/planner`
5. `/task-manager`
6. `/writer`
7. `/editor`
8. `/reviewer` [J11]

The root reference also permits a minimum `Constitution → Specify → Write` path, so planning, tasking, editing, and review are recommended rather than universally enforced by code. [J11]

#### 4.2 Planning and ambiguity gates

`/clarify` reads the constitution, relevant specification shards, and present knowledge files; it asks exactly one to five targeted questions, waits, then updates the affected specification and knowledge artifacts. [J16]

When an existing plan or task ledger is found, the user chooses update, replace, increment, bounded continuation, or split conversion. [J17]

The planner offers full-novel, arc, batch, and light modes. It also asks how to proceed around existing chapters. [J17]

Draft conflicts stop planning or task generation until the user resolves them. Content beyond the drafted range requires explicit approval. [J18]

#### 4.3 Drafting loop

Before drafting, the writer asks whether to work one chapter at a time, in a bounded batch, or through all remaining chapters. One-by-one mode waits for approval between chapters. [J19]

The writer then reloads the constitution, relevant specification/plan shards, focused knowledge and current-state entries, previous chapter, chapter goals, emotional target, pacing tag, and internal-reaction plan. [J20]

After writing, it saves the chapter, changes the chapter task from `[ ]` to `[FOR_REVIEW]`, and hands off to `/editor`; only broad review may mark it `[DONE]`. [J21]

#### 4.4 Editor and reviewer boundaries

The editor:

- edits one target chapter;
- lets the user select references;
- treats other chapters as read-only evidence;
- emits exact line-specific current/replacement text;
- keeps every item in `approve`, `skip`, or `for_discussion`;
- waits until every item is resolved; and
- applies approved changes only after a final confirmation, stopping if exact target text no longer matches. [J22] [J23]

The reviewer chooses framework, content, or final analysis; broad content analysis reads the complete project corpus and checks cross-chapter continuity, tracking accuracy, knowledge gaps, task state, and readiness. [J24]

The reviewer updates knowledge incrementally from `[FOR_REVIEW]` chapters, emits a structured report, avoids line rewriting, and changes a task to `[DONE]` only after broad review passes and required knowledge/tracking work can be completed. [J25]

#### 4.5 Optional and fallback routes

Utilities cover exploratory drafting, focused scene drafting, metadata, quick checklists, expert stances, tracking, timeline, relationships, voice refinement, authenticity audit, and output-format cross-checking. A comics branch begins only after prose chapters exist. [J13]

The installer converts the same command prompts into host-specific forms; Codex receives command-as-skill wrappers. Manual copy/paste remains the generic fallback. [J04]

### Inference

The workflow’s strongest orchestration contract is not concurrency; it is **visible artifact state plus explicit transition gates**. The task marker sequence and editor approval loop make handoffs inspectable even when one assistant performs every role.

JeroTan also sharpens a useful distinction:

- clarification is an author decision stage;
- editing is a local repair proposal/application stage; and
- reviewing is a broad evidence and readiness stage.

That separation is more precise than a single “review” role, though the active system does not isolate those stances into separately permissioned agents.

### Uncertainty

- No scheduler enforces that users actually run all recommended stages.
- `[P]` and `[Dep:X]` are task annotations; no execution engine, lock, or dependency validator was identified.
- Batch and all-at-once writing rely on the selected assistant continuing to follow the prompt contract over long runs.
- Reviewer knowledge updates occur before its report-and-wait instruction; the prompt does not define a separate author confirmation for every promoted fact.

## 5. State Storage Model

### Observed

#### 5.1 Actual storage model

| Required state question | Observed JeroTan behavior |
|---|---|
| Static author constraints | `memory/constitution.md` stores principles, standards, style, reader contract, pacing, and revision notes [J45] [J46] |
| Core story direction | Lean `specification.md` or split specification shards store premise, purpose, promise, cast/world snapshots, requirements, and open clarifications [J15] |
| Detailed canon | Markdown knowledge files store characters, voices, locations, world rules, glossary entries, and strategic-reversal systems [J15] [J27] |
| Dynamic/current character state | `tracking/character-state.json` stores schema version, chapter, condition, location, possessions, skills, knowledge, development, and supporting-character state [J28] |
| Plot and promises/payoffs | `plot-tracker.json` stores main/subplots, completed/upcoming nodes, foreshadowing plant/hints/reveal/status, conflicts, checkpoints, and issue notes [J29] |
| Relationships | `relationships.json` stores typed relationship buckets, dynamic trajectories, key events, factions, conflict classes, per-chapter history, and predictions [J30] |
| Timeline | `timeline.json` stores story time, chapter events, parallel events, history, travel constraints, and anomalies [J31] |
| Validation policy | `validation-rules.json` is a template for character/address/world checks and proposed auto-fix confidence settings; it is not itself an executable semantic validator [J32] |
| Work state | `tasks.md` or shards use `[ ] → [FOR_REVIEW] → [DONE]` and append editor/reviewer log entries [J33] |
| Manuscript | Markdown chapter files under recursively grouped `content/`, each ending in a short present-tense mini summary [J21] |
| Exploratory material | `draft/` material is explicitly editable, discardable, draft-only, and non-canonical until moved through planning/writing [J34] |
| Author voice memory | Constitution is actively loaded; a separate optional `memory/personal-voice.md` template exists but is not referenced by the active core commands [J45] [J59] |

#### 5.2 Authority and conflict behavior

The workflow gives drafts lower priority than specification, plan, knowledge, and tracking. Conflicting draft facts require user resolution or alignment to the core documents. [J18] [J35]

`/clarify` propagates a user answer into the relevant specification shard and matching knowledge file. [J16]

`/specify` calls the knowledge folder the detailed canon store, but no document defines a complete cross-core precedence rule when manuscript, specification, plan, knowledge, and tracking disagree with one another. [J15]

#### 5.3 Update and history behavior

The planner initializes five tracking JSON files. The explicit `/utility-track` command mutates or queries those files, preserves canonical keys, and updates `lastUpdated` for character state. [J26] [J36]

After drafting, the writer explicitly updates task status, not the tracking JSON. The reviewer checks all tracking files and updates Markdown knowledge, but its enumerated update step does not enumerate corresponding JSON mutations. This differs from the planner/README promise that tracking files will be updated as chapters are written. [J21] [J25] [J60]

History is mixed:

- current character and plot objects are rewritten snapshots;
- relationships include a per-chapter change history;
- the constitution carries a version-history appendix;
- task shards carry dated editor/reviewer logs; and
- there is no single ordered event log spanning all authority domains. [J30] [J33] [J46]

The writer can update, replace, or increment an existing chapter, and the editor applies local exact-text replacements to one chapter. The inspected commands do not specify deterministic recomputation of later plan, tracking, knowledge, or chapters after an earlier chapter changes. [J17] [J23]

### Inference

JeroTan provides a more useful domain decomposition than a monolithic state blob:

- author contract;
- story direction;
- rich canon;
- current character state;
- plot/foreshadowing;
- relationships;
- timeline;
- task/review state; and
- manuscript.

However, it is still an **agent-maintained collection of current files**, not a transactionally updated story database. The JSON shapes improve consistency and machine lookup, but only `character-state.json` receives executable schema checks in the MCP layer; other dynamic domains rely primarily on prompts and later review.

Earlier-chapter propagation is therefore best labeled **Inference: agent- and author-guided reconciliation**, not an Observed deterministic feature. The source exposes dependencies and continuity notes that could guide recalculation, but it does not implement a replay engine or stale-write guard.

### Uncertainty

- No revision counter, compare-and-swap field, lock protocol, or atomic multi-file commit contract was identified.
- `lastUpdated` records time, not write lineage or expected prior revision.
- Character `knowledge` is represented, but narrator knowledge, POV access, and reader knowledge are not separate typed domains.
- Objects appear in possessions, glossary, plot notes, and prose rather than one authoritative object ledger.
- There is no explicit total order for direct author edits versus later automated extraction.
- The exact user action required to “promote” exploratory material is a workflow transition, not a recorded canon-promotion event.

## 6. Context Management

### Observed

The source defines three complementary context strategies:

1. **Sharding:** specification, plan, and tasks switch to index + `_main.md` + focused shards around 500 lines; tasks read `_main.md` and only the relevant shard. [J38] [J39] [J40]
2. **Focused lookup:** MCP search normalizes names/text, scores exact/prefix/substring/token matches, caps results at 50, and returns source paths and line numbers for Markdown entries. [J41] [J42]
3. **Near-field prose reload:** the writer reads the immediately previous chapter, the earlier part of numbered pacing sequences, or the final chapter of the prior arc when relevant. [J20]

The writer’s target bundle includes the constitution, relevant specification and plan shards, selected character/location/current-state entries, world rules, glossary, optional strategic-reversal notes, chapter goals, emotional goals, pacing, and interiority. It explicitly excludes unrelated character and location entries. [J20]

Exploratory draft utilities use a deliberately lighter context set, while broad content review reads every project artifact and all chapters. [J24] [J34]

The MCP chapter inventory recursively discovers flat, saga/arc, and arbitrary nested chapter files, reports gaps and duplicates, supports pagination/order, and supplies hierarchy metadata. [J43]

### Inference

JeroTan offers the strongest **implemented context-retrieval slice** among the first five sources. It does not compile complete task packets, but it demonstrates that:

- deterministic story lookup can be read-only;
- results can retain provenance;
- chapter inventory can be independent from story selection;
- malformed canonical files can fail with actionable format errors; and
- an orchestrator can combine bounded structured lookup with exact prose/shard reads.

Its context model is still hybrid: the MCP service covers characters, locations, glossary, character state, and chapter inventory, while the model directly reads plans, tasks, world files, relationship/timeline JSON, and manuscript prose.

### Uncertainty

- The 500-line threshold is a file-maintainability heuristic, not a token budget.
- No explicit context budget, provenance manifest, coverage score, recency policy, or deduplication algorithm exists for assembled prompt context.
- The system does not define what to do when a retrieved summary/state value conflicts with manuscript prose beyond surfacing conflicts through model judgment.
- Cross-role context is persisted in files and chat, not an explicit typed handoff envelope.
- No embedding, index rebuild, cache invalidation, or far-field summarization service is present.

## 7. Creative-Craft Model

### Observed

#### 7.1 Author contract and planning

The constitution template covers core values, quality standards, creative style, content norms, reader promises, revision procedure, and pacing strategy. [J46]

The specification collects logline, premise, character psychology, themes, audience, success criteria, and unresolved questions while moving rich details to knowledge files. [J15]

The planner supports full, arc, batch, and light planning; it records structural approach, pacing/tension, foreshadowing, character arcs, chapter summaries/flow/continuity notes, and optional strategic-reversal design. [J17] [J47]

#### 7.2 Scene and prose rules

The writer uses planner flow as its main brief, requires emotional targets and interior reactions, varies sentence rhythm, discourages report-style action, shows emotion physically, and conditionally loads dialogue, banter, naming, punctuation, and strategic-reversal skills. [J20] [J48]

The skill library supplies:

- scene/sequel structure;
- character wound, motivation, contradiction, defenses, and vulnerabilities;
- subtext, voice asymmetry, action beats, status turns, and exposition-through-conflict;
- emotional interiority;
- pacing archetypes and tags;
- strategic reversal fairness/cost; and
- name research/fit/recording guidance. [J49]

#### 7.3 Genre and voice

Six active genre skills cover fantasy, romance, thriller, horror, mystery, and science fiction. The packs are compact convention/check lists rather than full research corpora. [J50]

Voice is represented in constitution style rules, character-specific voice fields, dialogue guidance, authenticity audit/refinement utilities, and an optional personal-voice template. [J27] [J45] [J49]

### Inference

The craft model is strongest when it turns qualitative advice into repeated fields or stage-specific checks: pacing tags, chapter flow, continuity notes, character voice roles, fairness seeds, exact edit findings, and preflight questions.

Compared with Haowjy, JeroTan is more prescriptive and artifact-shaped but less explicit about distinct critic, reader-experience, and story-memory personas. Compared with Zenstory, it is less market-specific and less transactional.

### Uncertainty

- No persistent narrator/POV/reader epistemology model was identified.
- “Show, don’t tell,” fragment thresholds, emotional interiority, and named structure patterns are prescriptive defaults; the repository does not establish that they improve every genre or author voice.
- The active style-detector/reference pack advertised by root docs is not present under active `src/`; that maintenance discrepancy is recorded in Section 10.
- No blind-reader simulation or persona-bound reader testing method is implemented.
- The source’s “authentic voice” heuristics are generic anti-pattern rules; they are not a validated authorship or AI-detection method.

## 8. Evaluation and Continuity

### Observed

The editor and reviewer are separated by scope and mutation behavior:

- editor: one chapter, exact line-level replacement proposals, explicit per-item decisions, confirmed repair;
- reviewer: project-wide framework/content/readiness findings, knowledge updates, task approval, no prose replacement. [J23] [J24] [J25] [J51]

The consistency skill checks character, world, timeline, foreshadowing, fragments, report-style narration, and emotional flatness, and tells the model to report rather than rewrite unless asked. [J52]

Deterministic JavaScript checks cover:

- exact headings and required fields for character/location/glossary entries;
- duplicate entries;
- `character-state.json` JSON and required structure;
- recursive chapter inventory, numbering, ranges, gaps, duplicates, and pagination;
- bounded search; and
- explicit `FORMAT_ERROR`, `NOT_FOUND`, `INPUT_ERROR`, and `TOOL_ERROR` paths. [J41] [J43] [J44]

`validate_story_files` checks only character profiles, locations, glossary, and character state; the server explicitly says it does not inspect manuscript chapters. [J44]

The pinned test suite exercises those lookup/format/config contracts. All 11 tests passed in the recorded local run. [J53] [J54]

### Inference

JeroTan supplies a useful three-layer evaluation model:

1. deterministic structural validation and retrieval;
2. model-judgment continuity/craft review; and
3. human-gated exact repair.

The exact editor item format is especially relevant because it separates finding identity, evidence, proposed change, reason, disposition, and application.

### Uncertainty

- The JSON `validation-rules` template describes semantic checks and auto-fix thresholds, but no JavaScript path was found that executes those story-semantic rules. `/utility-track --check` is a model prompt, not a deterministic validator.
- Plot, relationship, timeline, and validation-rules JSON are not included in the MCP format validator.
- The tests do not evaluate prose quality, state-update correctness after drafting/revision, canon promotion, or semantic continuity.
- No critic/editor/reader-simulation fan-out, consensus algorithm, severity schema, or machine-readable finding store is implemented.
- There is no demonstrated audit of a real long manuscript at the pinned revision.

## 9. Human-in-the-Loop Model

### Observed

Mandatory or explicit user gates include:

- whether to update an existing constitution; [J37]
- one to five clarification answers before specification/knowledge updates; [J16]
- update/replace/increment/split choices for existing plan/tasks; [J17]
- conflict resolution and permission before extending beyond user drafts; [J18]
- one-by-one, batch, or all-at-once writing mode; [J19]
- update/replace/increment choice for an existing chapter; [J17]
- approval before locking major names; [J48]
- editor reference selection, item approve/skip/discussion, and final confirmation before applying edits; [J22] [J23]
- explicit choice before overwriting or promoting exploratory draft changes; and [J34]
- an explicit request before stale project files are restructured by the cross-check utility. [J55]

Stop conditions include missing target/context, unresolved draft contradictions, unresolved editor items, exact-text mismatch during edit application, and unresolved continuity/repair work before `[DONE]`. [J18] [J23] [J25]

The reviewer does not rewrite prose, but it does instruct the assistant to update knowledge from chapters before presenting its report. [J25]

### Inference

JeroTan has the clearest **edit-application gate** among the first five sources. It also offers explicit planning-scope and conflict gates.

Its canon-promotion boundary is less complete: drafts are clearly non-canon, but reviewer extraction into knowledge is not modeled as a separately confirmed, revisioned promotion event.

### Uncertainty

- No permission manifest mechanically restricts prompt commands to their stated files.
- “Wait for user direction” is a behavioral instruction, not an enforced transaction state.
- Direct user edits outside the workflow have no reconciliation protocol beyond reread, cross-check, and model judgment.
- No role-specific credentials or file permissions isolate writer, editor, reviewer, and tracking mutations.

## 10. Runtime and Maintenance

### Observed

#### 10.1 Setup and platform adaptation

The installer:

- asks for Claude, Gemini, OpenCode, and/or Codex;
- copies or converts commands;
- copies skill directories and templates;
- converts commands into Codex `SKILL.md` wrappers;
- writes project-local MCP configuration; and
- installs a concise workflow guide. [J04]

Existing command/skill conflicts support overwrite, skip, overwrite-all, or skip-all choices. Template copying itself uses overwrite mode. [J04]

The MCP configuration layer:

- encodes the absolute project root in a base64url argument;
- uses a project-derived cache path under the OS temp directory;
- rejects invalid/non-absolute decoded roots;
- bounds cache deletion to its namespace;
- pins the invoked npm package to the installed package version;
- merges managed configuration into host files; and
- preserves unrelated settings in tested cases. [J54]

The MCP server is stdio-based and network-independent once the package is available, but generated commands use `npx --prefer-online` and a rebuilt project-bound npm cache. [J54]

#### 10.2 Recovery and migration

`NOVEL_WORKFLOW.md` provides host-specific MCP connection checks and recovery actions for format, lookup, and tool failures. [J14]

`/utility-command-cross-check` compares existing project artifacts against the active command/template format, reports `current`, `revise`, or `missing`, preserves story facts and IDs, and refuses automatic overwrite without an explicit user request. [J55]

#### 10.3 Tests

`package.json` exposes only `node --test`; the complete pinned tree contains one 490-line test file and no active `.github/workflows/` file. The local run passed 11/11 tests under Node 24. [J02] [J53]

#### 10.4 Pinned maintenance discrepancies

All items in this subsection are **Observed repository facts**, not a general quality verdict.

1. **Version documentation drift:** `package.json` and lockfile say `1.5.1`, while `CHANGELOG.md` stops at `1.5.0`; `version_history.md` also contains an earlier `v2.0.0`/ `v3.0.0` sequence followed later by `v1.3.x`–`v1.5.0`. [J02] [J56]
2. **User-facing command-name drift:** the root README names `/guide-me`, `/meta`, `/checklist`, `/expert`, `/track`, `/timeline`, `/relations`, and unprefixed voice utilities, while active filenames and the installed guide use `/utility-...` names. The installer derives installed names from active filenames. [J04] [J57]
3. **Archived-only style references:** root `SKILL.md` advertises `skills/quality-assurance/style-detector/SKILL.md`, and the writer points to `./knowledge-base/styles/`; the matching files are only under `.old/v1/`, while the installer reads active commands/skills/templates from `src/`. [J04] [J58]
4. **Personal-voice creation drift:** README topology places `personal-voice.md` in the constitution-created memory folder, but the constitution command creates only `constitution.md`; no active core command references the personal-voice file. [J45] [J59]
5. **Tracking-update contract gap:** planner/README text says tracking JSON will be updated as chapters are written, but the writer’s explicit post-write mutation is task status; reviewer explicitly updates knowledge and checks tracking, while JSON mutation is delegated to `/utility-track`. [J21] [J25] [J36] [J60]
6. **Declared engine-floor mismatch:** the package declares Node `>=18`, while the lockfile’s `@hono/node-server@2.1.0` entry declares Node `>=20`. [J61]
7. **Distribution provenance split:** the npm package manifest includes `bin/` and `src/`, while `.npmignore` excludes the dedicated attribution file, root methodology file, changelog, version history, and tests; README and LICENSE remain packaged. [J10] [J62]
8. **Local tests but no pinned CI workflow:** the source has executable tests and they passed locally, but the complete active tree contains no CI workflow definition. [J53] [J63]

### Inference

The executable retrieval/configuration layer is comparatively disciplined: bounded deletion, project-root binding, structured errors, source locations, and tests reduce several runtime risks.

The maintenance discrepancies instead concentrate at the boundary between root documentation, archived v1 assets, active `src/`, and the npm payload. Likely consequences—wrong command invocation, missing optional style behavior, incomplete automatic tracking expectations, or Node 18 install friction—are hypotheses to verify on supported hosts, not evidence of broad project quality.

### Uncertainty

- Tests were run under Node 24, not every declared/supported Node version.
- No install smoke test was performed against live Claude, Gemini, OpenCode, or Codex clients.
- Network/offline/proxy behavior of generated `npx --prefer-online` commands was not validated.
- No CI status exists to compare with the local run.
- No migration fixture exercises a real pre-1.5 project through the cross-check utility.
- The analysis did not inspect the published npm registry tarball; `npm pack --dry-run` evaluated the pinned checkout’s package rules.

## 11. Strengths

### Observed

1. Clear eight-stage artifacts and visible task transitions. [J11] [J33]
2. Constitution and bounded clarification make author intent and unresolved questions first-class. [J16] [J46]
3. Drafts are explicitly non-canonical and conflict-sensitive. [J18] [J34]
4. Specification/plan/task sharding defines maps, read order, focused updates, and a concrete size threshold. [J38] [J39] [J40]
5. The pre-write context contract combines exact plan intent, focused canonical lookup, previous prose, emotional goals, pacing, and interiority. [J20]
6. Editor findings are line-specific, persistent, individually dispositioned, and applied only after final confirmation. [J23]
7. Reviewer scope is distinct from chapter-local editing and blocks `[DONE]` on unresolved continuity or state work. [J24] [J25]
8. The read-only MCP boundary is explicit and technically annotated. [J14]
9. Story lookup preserves source paths/lines and fails deterministically on malformed canonical files. [J41] [J44]
10. Recursive chapter inventory accounts for nested layouts, ranges, gaps, duplicates, pagination, and latest-first ordering. [J43] [J53]
11. MCP configuration binds lookup to the intended project root and preserves unrelated host settings in tests. [J54]
12. The source records derivative lineage and exact MIT license text rather than relying on a badge. [J06] [J07] [J09]

### Inference

JeroTan is particularly valuable for **operational contracts around long-project files**: when to split, how to locate current work, how to retrieve bounded canonical context, how to propose exact edits, and how to migrate old artifact formats without silently rewriting story content.

### Uncertainty

- Strength of a contract does not prove every host/model follows it.
- Test coverage is meaningful but limited to the JavaScript retrieval/configuration slice.
- No comparative output-quality evaluation establishes that the craft rules outperform alternatives.

## 12. Weaknesses / Gaps

### Observed

1. Dynamic state is distributed across five JSON files, Markdown knowledge, tasks, and manuscript without one atomic update boundary. [J26] [J28] [J29] [J30] [J31]
2. Only character state among the tracking JSON files receives executable structural validation. [J44]
3. The writer does not explicitly update tracking JSON after drafting; reviewer mutation is explicit for knowledge, not each tracking domain. [J21] [J25] [J60]
4. No total authority order is defined among core files when they disagree; only drafts have an explicit lower priority. [J15] [J35]
5. Earlier-chapter edit commands do not specify deterministic downstream replay or dependency recalculation. [J17] [J23]
6. The active architecture has no separately scheduled writer, editor, reviewer, or reader-simulation agents. [J04] [J13]
7. `[P]` and `[Dep:X]` are represented in Markdown but not enforced by code. [J33]
8. The semantic `validation-rules` and auto-fix settings are templates; the deterministic validator checks formats, not those narrative rules. [J32] [J44]
9. Reader knowledge, narrator knowledge, and POV access are not separate state domains. [J28] [J29]
10. Reviewer knowledge extraction lacks a distinct recorded canon-promotion approval event. [J25]
11. Active documentation/distribution discrepancies can point users at archived or differently named capabilities. [J57] [J58] [J59]
12. The package’s declared Node floor and one locked dependency’s floor differ. [J61]

### Inference

The largest architectural gap is **state mutation semantics**, not state vocabulary. JeroTan names many useful domains but does not define stale-write protection, multi-file atomicity, provenance per state fact, or deterministic earlier-revision propagation.

The largest evaluation gap is **semantic automation**. Format checks are real and tested; story truth, continuity, and craft remain model judgments with human review.

### Uncertainty

- Some hosts may supply their own file locking, diff review, or skill isolation; the source does not standardize those guarantees.
- A user may manually keep JSON state accurate after every chapter, but that practice is not a tested repository behavior.
- Archived v1 assets may remain intentionally available for reference; their presence does not establish active support.
- No conclusion about overall maintainability follows solely from the listed drift.

## 13. Relevance to CodexWriter

Every disposition below is provisional. Observed source responsibilities are separated from CodexWriter adoption candidates. Nothing in this section changes an architecture or crosswalk decision.

### Observed reusable responsibilities

| JeroTan responsibility | Observed source behavior (not CodexWriter direction) |
|---|---|
| Author constitution | Makes project-level creative constraints and reader promises inspectable [J46] |
| Bounded clarification | Converts ambiguity into explicit author answers before planning [J16] |
| Lean spec + detailed knowledge | Separates direction from rich canonical reference [J15] |
| Sharded long documents | Gives large author-editable artifacts indexes, read order, and focused update rules [J38] [J39] [J40] |
| Pre-write context reload | Defines a concrete chapter context checklist [J20] |
| Read-only story lookup | Demonstrates deterministic, provenance-bearing retrieval without mutation authority [J14] [J41] |
| Chapter inventory | Gives layout-independent manuscript discovery and anomaly reporting [J43] |
| Typed tracking domains | Supplies candidate vocabulary for current character, plot, relationship, and timeline state [J28] [J29] [J30] [J31] |
| Exact editor gate | Separates findings, decisions, confirmation, and application [J23] |
| Broad reviewer | Separates project readiness from line repair [J24] [J25] |
| Draft/non-canon area | Preserves exploratory material without silently locking canon [J34] |
| Format cross-check | Provides an author-preserving migration/doctor responsibility [J55] |

### Provisional candidate architectural borrowing

- **Strongly investigate:** an author constitution/preferences artifact that is separate from story canon.
- **Strongly investigate:** a read-only internal story-query boundary with source provenance and explicit format errors.
- **Strongly investigate:** index + `_main` + focused shard contracts for large human-editable artifacts.
- **Strongly investigate:** editor findings with stable IDs/statuses, exact evidence, proposed replacement, and a separate apply transaction.
- **Investigate:** dedicated state domains for character current state, plot/foreshadowing, relationships, and timeline—without adopting JeroTan’s exact JSON layouts by default.
- **Investigate:** chapter-inventory validation as deterministic infrastructure.
- **Investigate:** an artifact-format doctor/migrator that preserves user prose and identifiers.
- **Investigate:** explicit non-canonical draft storage and author-confirmed promotion.
- **Investigate:** reviewer/readiness state distinct from local edit state.

### Provisional implementation-level borrowing requiring license/provenance handling

- Parser and chapter-discovery algorithms.
- MCP tool schemas, structured errors, and project-root binding patterns.
- JSON/Markdown templates and exact format contracts.
- Installer adapters and Codex command-to-skill conversion.
- Editor/reviewer prompt wording and craft-skill expression.
- Test fixtures.

Any such borrowing would require MIT notice preservation, JeroTan and declared upstream provenance tracking, and file-level review. Architectural comparison alone does not authorize copying.

### Provisional patterns to avoid

- Avoid presenting prompt-maintained JSON as transactionally safe state.
- Avoid a global “core documents win” rule without cross-domain precedence and conflict records.
- Avoid treating `lastUpdated` as a revision guard.
- Avoid automatic canon extraction without a recorded promotion decision.
- Avoid claiming semantic validation when only file shape is checked.
- Avoid exposing parallel/dependency markers without execution semantics.
- Avoid active references to archived-only assets or mismatched installed command names.
- Avoid separating attribution details from the distributed implementation without an explicit release policy.

### Inference

JeroTan materially strengthens the case for retaining CodexWriter responsibilities around author intent, clarification, planning, context assembly, deterministic lookup, continuity, prose editing, story review, and migration. It also strengthens—but does not settle—the candidates for typed story state and read-only internal services.

It does not resolve whether CodexWriter should store canonical state in Markdown, JSON, a revisioned database, or a hybrid. Its evidence instead clarifies what a hybrid must specify: authority, provenance, update transactions, conflict handling, and revision propagation.

### Uncertainty

- No candidate above changes `ARCHITECTURE.md` or `docs/crosswalk.md`.
- No responsibility name, API, schema, or file layout becomes stable through this analysis.
- The remaining sources may supply stronger epistemic, reader-testing, edit-pipeline, or state-history evidence.

## 14. Detailed Evidence

### Observed: claim-level traceability map

| Claim | Immutable evidence |
|---|---|
| J01 | [README purpose, features, runtime targets, lines 1–31](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L1-L31) |
| J02 | [package version, scripts, dependencies, license, files, engine, lines 1–50](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/package.json#L1-L50) |
| J03 | [root methodology’s skill inventory, lines 135–197](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L135-L197) |
| J04 | [installer platform map, lines 16–49](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/install.js#L16-L49); [copy/convert/install loop, lines 394–443](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/install.js#L394-L443) |
| J05 | [changelog dated activity and feature scope, lines 8–56](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/CHANGELOG.md#L8-L56) |
| J06 | [exact JeroTan MIT license, lines 1–22](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/LICENSE#L1-L22) |
| J07 | [exact JeroTan attribution and declared adaptation scope, lines 1–11](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/ATTRIBUTION.md#L1-L11) |
| J08 | [README lineage, lines 10–16](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L10-L16); [README attribution, lines 372–378](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L372-L378) |
| J09 | [exact original wordflowlab MIT license at independently pinned commit, lines 1–22](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/LICENSE#L1-L22) |
| J10 | [npm file exclusions, lines 1–25](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/.npmignore#L1-L25); [published file allowlist, lines 44–47](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/package.json#L44-L47) |
| J11 | [eight stages and outputs, lines 10–21](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L10-L21); [minimum workflow, lines 215–229](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L215-L229) |
| J12 | [project artifact topology, lines 23–69](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L23-L69) |
| J13 | [state-sensitive routing and stage transitions, lines 12–45](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-guide-me.md#L12-L45); [utilities and draft handoffs, lines 60–87](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-guide-me.md#L60-L87) |
| J14 | [guide read-only/update boundary, lines 12–16](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-guide-me.md#L12-L16); [MCP read-only annotations, lines 46–68](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/mcp-server.js#L46-L68) |
| J15 | [lean specification and knowledge-domain split, lines 14–66](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/specify.md#L14-L66); [detailed canon initialization, lines 176–200](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/specify.md#L176-L200) |
| J16 | [clarification context, questions, wait, and updates, lines 18–49](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/clarify.md#L18-L49) |
| J17 | [plan update choices and planning modes, lines 18–29 and 58–76](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L18-L29); [existing chapters and four plan modes, lines 58–76](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L58-L76); [existing-chapter write choices, lines 18–25](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L18-L25) |
| J18 | [planner draft conflict and scope gates, lines 39–56](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L39-L56); [task-manager draft gates, lines 41–58](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/task-manager.md#L41-L58) |
| J19 | [writer mode selection, lines 49–61](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L49-L61) |
| J20 | [writer 13-item context checklist, lines 75–97](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L75-L97) |
| J21 | [chapter output and task/editor handoff, lines 116–137](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L116-L137) |
| J22 | [editor selected references and editable boundary, lines 32–99](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/editor.md#L32-L99) |
| J23 | [editor exact finding/status contract, lines 124–169](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/editor.md#L124-L169); [confirmed exact-text application, lines 204–217](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/editor.md#L204-L217) |
| J24 | [review modes and complete content-review context, lines 18–62](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/reviewer.md#L18-L62) |
| J25 | [reviewer knowledge updates and report boundary, lines 64–88](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/reviewer.md#L64-L88); [review log, done gate, and stop conditions, lines 90–110](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/reviewer.md#L90-L110) |
| J26 | [planner initializes five tracking files, lines 344–358](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L344-L358) |
| J27 | [character and voice templates, character lines 1–26](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/knowledge/character-profiles.md#L1-L26); [voice lines 1–15](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/knowledge/character-voices.md#L1-L15); [world template, lines 1–28](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/knowledge/world-setting.md#L1-L28); [glossary template, lines 1–65](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/knowledge/glossary.md#L1-L65) |
| J28 | [character-state schema, lines 1–79](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/character-state.json#L1-L79) |
| J29 | [plot/foreshadowing/conflict state, lines 1–61](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/plot-tracker.json#L1-L61) |
| J30 | [relationship, faction, history, and prediction state, lines 1–69](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/relationships.json#L1-L69) |
| J31 | [timeline events, concurrency, constraints, and anomalies, lines 1–48](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/timeline.json#L1-L48) |
| J32 | [validation rule and auto-fix template, lines 1–92](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/validation-rules.json#L1-L92); [declared usage levels, lines 103–125](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/tracking/validation-rules.json#L103-L125) |
| J33 | [task markers, statuses, and review log, lines 79–156](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/task-manager.md#L79-L156) |
| J34 | [exploratory draft status and minimal context, lines 12–53](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-drafter.md#L12-L53); [non-canon generation/save gates, lines 96–130](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-drafter.md#L96-L130) |
| J35 | [core-document priority over drafts, lines 63–73](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L63-L73); [guide priority statement, lines 109–112](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-guide-me.md#L109-L112) |
| J36 | [tracking update/query/validation prompt contract, lines 18–40](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-track.md#L18-L40) |
| J37 | [constitution existing-file gate and save path, lines 18–39](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/constitution.md#L18-L39) |
| J38 | [specification split-mode contract, lines 123–178](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/specify.md#L123-L178) |
| J39 | [plan split-mode contract, lines 265–329](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L265-L329) |
| J40 | [task split-mode contract, lines 158–210](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/task-manager.md#L158-L210) |
| J41 | [Markdown parsers and source lines, lines 41–131](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L41-L131); [glossary parser/source lines, lines 134–214](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L134-L214) |
| J42 | [bounded search scoring and limits, lines 304–332](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L304-L332); [search result ordering, lines 554–565](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L554-L565) |
| J43 | [recursive chapter discovery and hierarchy, lines 335–476](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L335-L476); [inventory summary, lines 479–551](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L479-L551); [pagination, lines 619–648](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L619-L648) |
| J44 | [character-state executable validation, lines 217–267](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L217-L267); [four-file validator scope, lines 740–758](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/mcp/story-library.js#L740-L758); [server scope declaration, lines 131–135](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/mcp-server.js#L131-L135) |
| J45 | [optional personal-voice topology, lines 62–69](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L62-L69); [personal-voice template, lines 1–38](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/memory/personal-voice.md#L1-L38) |
| J46 | [constitution template, lines 1–67](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/memory/constitution.md#L1-L67); [pacing and version history, lines 68–91](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/templates/memory/constitution.md#L68-L91) |
| J47 | [plan structure and chapter fields, lines 82–151](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L82-L151); [foreshadowing, arcs, flow, and continuity, lines 176–227](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L176-L227) |
| J48 | [writer prose and conditional skill rules, lines 99–114](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L99-L114) |
| J49 | [scene/sequel skill, lines 6–23](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/writing-techniques/scene-structure/SKILL.md#L6-L23); [character depth, lines 6–15](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/writing-techniques/character-depth/SKILL.md#L6-L15); [dialogue, lines 6–28](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/writing-techniques/dialogue-techniques/SKILL.md#L6-L28); [strategic reversal, lines 6–53](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/writing-techniques/strategic-reversal/SKILL.md#L6-L53) |
| J50 | [six genre skill inventory, lines 173–182](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L173-L182); [fantasy skill depth, lines 6–16](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/genre-knowledge/fantasy/SKILL.md#L6-L16); [mystery skill depth, lines 6–17](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/genre-knowledge/mystery/SKILL.md#L6-L17) |
| J51 | [editor objective and scope, lines 12–16](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/editor.md#L12-L16); [reviewer objective and scope, lines 12–15](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/reviewer.md#L12-L15) |
| J52 | [continuity/model-review checks and no-rewrite boundary, lines 6–24](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/quality-assurance/consistency-checker/SKILL.md#L6-L24); [forgotten-thread method, lines 6–17](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/skills/quality-assurance/forgotten-elements/SKILL.md#L6-L17) |
| J53 | [lookup and nested chapter tests, lines 114–188](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/test/mcp-story-library.test.js#L114-L188); [range/error tests, lines 190–301](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/test/mcp-story-library.test.js#L190-L301); [MCP registration/execution tests, lines 432–490](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/test/mcp-story-library.test.js#L432-L490) |
| J54 | [project-root encoding, bounded cache, and package command, lines 13–75](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/installer/mcp-config.js#L13-L75); [host config updates, lines 120–200](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/installer/mcp-config.js#L120-L200); [config/cache tests, lines 303–430](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/test/mcp-story-library.test.js#L303-L430) |
| J55 | [cross-check objective/source-of-truth/target map, lines 12–77](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-command-cross-check.md#L12-L77); [report and no-overwrite preservation rules, lines 186–220](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-command-cross-check.md#L186-L220) |
| J56 | [changelog latest documented version, lines 8–10](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/CHANGELOG.md#L8-L10); [non-monotonic version-history headings around v2/v3, lines 77–83](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/version_history.md#L77-L83); [later v1.3 sequence, lines 263–287](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/version_history.md#L263-L287); [v1.5 entry, lines 430–439](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/version_history.md#L430-L439) |
| J57 | [README unprefixed utility command names, lines 157–172](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L157-L172); [active installed utility names, lines 60–76](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/utility-guide-me.md#L60-L76); [installer filename-derived command handling, lines 146–192](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/install.js#L146-L192) |
| J58 | [active root reference to style-detector, lines 160–171](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/SKILL.md#L160-L171); [writer’s knowledge-base style path, lines 79–86](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L79-L86); [archived style-detector path, lines 1–18](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/.old/v1/skills/quality-assurance/style-detector/SKILL.md#L1-L18); [installer active `src/skills` source, lines 201–244](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/bin/install.js#L201-L244) |
| J59 | [README memory files, lines 224–233](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L224-L233); [generated memory topology, lines 278–283](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L278-L283); [constitution creates only constitution.md, lines 18–39](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/constitution.md#L18-L39) |
| J60 | [README tracking update promise, lines 224–256](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L224-L256); [planner tracking promise, lines 344–358](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/planner.md#L344-L358); [writer’s explicit post-write mutation, lines 131–137](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/src/commands/writer.md#L131-L137) |
| J61 | [declared Node floor, lines 48–50](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/package.json#L48-L50); [locked transitive Node floor, lines 28–35](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/package-lock.json#L28-L35) |
| J62 | [package excludes attribution and root skill, lines 7–14](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/.npmignore#L7-L14); [README packaged attribution, lines 372–378](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/README.md#L372-L378) |
| J63 | [only declared test script, lines 10–14](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/package.json#L10-L14); [test file executable imports and fixture setup, lines 1–25](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/test/mcp-story-library.test.js#L1-L25) |
| J64 | [JeroTan’s declared original methodology and additions, lines 3–9](https://github.com/JeroTan/novel-writer-english/blob/6d836f23281e240eed36d50529424e086c8ff42d/ATTRIBUTION.md#L3-L9); [original repository’s pinned README workflow description, lines 1–39](https://github.com/wordflowlab/novel-writer-skills/blob/5bc9b373ff609e8910e0e8d179e4a697bf2b1268/README.md#L1-L39) |

### Observed: licensing/provenance paths checked

| Path | Result |
|---|---|
| JeroTan `LICENSE` | Found; exact MIT text; blob `cde9a1380b1b52717635a251a991df489fca9663` [J06] |
| JeroTan `NOTICE` | Not found in pinned recursive tree |
| JeroTan `ATTRIBUTION.md` | Found; derivative lineage and adaptation scope [J07] |
| JeroTan README attribution | Found [J08] |
| wordflowlab `LICENSE` at `5bc9b...` | Found; exact MIT text [J09] |
| Package distribution rules | Root license/README retained; dedicated attribution excluded by package rules [J10] [J62] |

### Observed: corpus and verification checks

- Fetched/checked the complete recursive tree at the JeroTan pin: 265 entries, 180 blobs, not truncated.
- Distinguished 86 active blobs from 94 `.old/v1/` archival blobs.
- Inspected every active command/skill/template path by inventory; deep-read the orchestration, state, context, craft, evaluation, installer, MCP, test, license, attribution, and maintenance paths cited above.
- Ran `npm ci --ignore-scripts` with a task-local cache and `npm test`; 11 passed, 0 failed under Node `v24.19.0`.
- Ran `npm pack --dry-run --json`; observed 76 package entries, including root README/LICENSE and excluding dedicated attribution/root skill/tests as the package rules indicate.
- Searched the pinned active tree for `NOTICE`, CI workflows, style-detector, knowledge-base styles, personal-voice use, revision/lock guards, and stale-write fields.

### Inference

The evidence establishes file contracts and tested retrieval/configuration behavior. It does not establish end-to-end creative quality, semantic correctness, transactional state safety, or uniform host behavior.

### Uncertainty

- Line ranges are pinned and were checked against the local detached checkout.
- Negative inventory claims apply only to the pinned tree.
- External naming/reference sites inside JeroTan skills were not treated as evidence for repository behavior.

## 15. Provisional CodexWriter Disposition

All dispositions in this section are **Inference** and provisional. They require comparative synthesis plus separate architecture/crosswalk review.

### Inference — Provisional retain / strongly investigate candidates

- **Retain responsibility:** author constitution and preference capture.
- **Retain responsibility:** bounded clarification before planning.
- **Retain responsibility:** story specification and detailed canonical knowledge.
- **Retain responsibility:** chapter planning, drafting, editing, broad review, and continuity.
- **Strongly investigate:** read-only, provenance-bearing story retrieval.
- **Strongly investigate:** deterministic chapter inventory and artifact validation.
- **Strongly investigate:** exact editor finding/approval/application contract.
- **Strongly investigate:** sharded human-editable documents with explicit maps and read order.
- **Strongly investigate:** exploratory non-canon draft space.

### Inference — Provisional adapt candidates

- **Adapt:** constitution into a portable author/project contract separated from story canon.
- **Adapt:** clarification into recorded decisions with provenance and revision.
- **Adapt:** JeroTan state domains into a versioned authority model rather than copying its JSON.
- **Adapt:** MCP lookup into an internal context service with budgets, coverage, and broader domain support.
- **Adapt:** `[FOR_REVIEW]`/`[DONE]` into typed workflow states with explicit transitions.
- **Adapt:** command cross-check into schema migration plus dry-run/diff/rollback.
- **Adapt:** reviewer knowledge extraction into proposed fact promotions requiring explicit disposition.

### Inference — Provisional merge/split candidates

- **Merge candidate:** constitution, author voice, and reusable preferences under one author-intent subsystem with project/global scopes.
- **Split candidate:** deterministic artifact validation from model-judgment story review.
- **Split candidate:** finding generation, human disposition, and edit application.
- **Split candidate:** context selection policy from read-only retrieval mechanics.
- **Split candidate:** current state snapshots from state-change history.

### Inference — Provisional extension candidates

- Revisioned state transactions and expected-revision guards.
- Earlier-chapter dependency impact reports and replay/recalculation workflows.
- Reader/narrator/POV/character epistemic layers.
- Machine-readable finding and canon-promotion records.
- Additional deterministic validators for plot, relationships, timeline, task state, and cross-file references.
- Host capability detection and explicit degraded-mode disclosure.

### Inference — Provisional defer

- Exact JSON and Markdown schemas.
- Exact 500-line split threshold.
- Comics, illustration, cover, and uploader feature integration.
- Exact genre/craft rule set.
- Multi-writer execution before authority and locking semantics are settled.

### Inference — Provisional reject / avoid candidates

- Treating prompt-maintained state as transactionally safe.
- Treating `lastUpdated` as a stale-write guard.
- Silent canonical knowledge promotion.
- Prompt-only “auto-fix” claims without executable scope disclosure.
- Active docs that route into archive-only files.
- A package floor that is not tested against the locked dependency floor.
- Architecture or crosswalk changes in this source-analysis PR.

## 16. Five-Source Comparative Baseline

### Inference — Provisional comparison of observed source evidence

The source columns summarize evidence recorded in the five separate analyses; the comparisons and the `Provisional Phase 1 reading` column are Inference, not new source observations or CodexWriter decisions.

| Dimension | Lensetek | Dewhurst | Zenstory | Haowjy | JeroTan | Provisional Phase 1 reading |
|---|---|---|---|---|---|---|
| Orchestration | Broad lifecycle routing | File/CLI workflows | Scenario router, stages, hooks, transactions | Author-facing Muse plus cognitive-role staffing | File/status router plus eight visible stages | JeroTan adds the clearest artifact transition loop; Zenstory remains strongest operational control plane |
| Author contract | Limited | Project/config conventions | Commercial/genre constraints and gates | Author direction is authoritative | Dedicated constitution plus clarification | JeroTan supplies the strongest explicit author-constraint artifact so far |
| Static canon | Skills/references | Markdown project artifacts | Canon Markdown plus structured projections | Human-editable KB/wiki pages | Lean spec plus rich Markdown knowledge | JeroTan clarifies direction-vs-detail separation but not total authority |
| Dynamic state | Limited | Character/scene/current-state artifacts | Bounded current snapshots and projections | Evolving character/timeline/wiki pages | Five typed JSON domains plus task state | JeroTan expands domain vocabulary; Zenstory remains stronger on update boundaries |
| History | Limited | Mostly current artifacts | Deltas/events plus bounded current state | Source anchors and current pages | Mixed current snapshots, relationship history, logs | No source yet supplies one complete cross-domain event history |
| Stale-write safety | Not central | None found | Previously inferred as a sequential revision guard, not a concurrency lock | Reread/surface-conflict instructions only | No revision guard identified; `lastUpdated` only | Zenstory remains the only candidate sequential stale-write mechanism so far |
| Context | Responsibility handoffs | Explicit reloads | Bounded projections and far-field query | Role-specific files/history/materialization | Shards + previous prose + tested bounded lookup | JeroTan offers the strongest implemented read-only lookup slice; no source has a full context compiler |
| Reader knowledge | Reader role | Representable | Dedicated reader-known timeline | Explicit concept, no dedicated store | Character `knowledge` only; no reader/narrator split | Zenstory remains structurally strongest |
| Reader simulation | Explicit responsibility | Limited | Review approximation | Dedicated persona-bound experiential role | No dedicated reader simulation | Haowjy remains strongest implementation evidence |
| Evaluation | Broad roles | CLI checks plus review | Scripts/hooks plus multi-agent review | Critic/editor/reader/continuity separation plus metrics | Format scripts + local editor + broad reviewer | JeroTan adds the best exact repair gate and tested format checks |
| Creative craft | Broad | Comparatively light | Deep commercial Chinese web-fiction method | Deep general prose/reader method | Structured general craft, genre packs, planning fields | Haowjy remains broadest general method; JeroTan operationalizes more fields |
| Non-canonical work | Workflow concept | Working artifacts | Staged work and author gates | Explicit AI/hidden/rejected tags | Explicit draft-only folders and approval gates | Haowjy tracks lightweight provenance; JeroTan supplies stronger file and promotion boundaries but no promotion record |
| Runtime | Limited | CLI/package behavior | Broad adapters and degradation | Mars/Claude distribution plus solo fallback | Four-host installer + read-only MCP + tests | JeroTan has the strongest tested distribution/retrieval slice after Zenstory’s broader control plane |
| Licensing lineage | Source license | Source license | Exact source license | Exact source license | Exact derivative and original MIT licenses plus attribution | JeroTan makes derivative provenance first-class, though distribution policy still needs review |

### Inference

After five sources, a plausible—but still provisional—shape is emerging:

- creative uncertainty and author intent should stay human-readable;
- machine-sensitive current state needs typed, revision-aware update semantics;
- context selection benefits from a read-only provenance-bearing service;
- local editing and broad review should remain distinct;
- deterministic validation should be explicit about its narrow scope; and
- canon promotion needs its own recorded decision boundary.

JeroTan strengthens the case for a hybrid system, but it does not choose the storage authority or transaction model for CodexWriter.

### Uncertainty

- The table compares contracts and implementation evidence, not equivalent end-to-end story outputs.
- Earlier source readings remain provisional until the source-analysis sequence and later synthesis are reviewed.
- JeroTan’s recent MCP layer received deeper executable inspection than some prompt-only sources; that difference in evidence depth is not a quality score.

## 17. Answers to Questions Carried From Haowjy

### Observed evidence and inference boundaries

| Carried question | JeroTan evidence-based answer |
|---|---|
| Can constitution/clarification provide explicit “settled” direction and canon promotion? | Constitution makes project principles/version notes explicit, and clarification removes resolved markers after user answers. Detailed knowledge is called canon. **Inference:** this improves direction status, but there is no universal `settled` state or recorded canon-promotion transaction. |
| Can later sources distinguish author truth, narrator/POV access, character knowledge, and reader knowledge? | JeroTan adds a character `knowledge` array but no separate narrator, POV-access, or reader-known store. The question remains open for wgwtest. |
| Can blind-reader/editing passes strengthen reader boundaries? | JeroTan strengthens editing but has no blind-reader role. The Rhavekost question remains open. |
| Which typed entities are justified? | Character current state, plot/foreshadowing/conflicts, relationships/history, timeline/anomalies, and task/review state now have concrete source evidence. **Inference:** they are candidates, not adopted schemas; objects, issues, questions, reader knowledge, and promises still need synthesis. |
| Embedded revisions or revisioned transaction layer? | Constitution version history, relationship history, and task logs coexist with rewritten current snapshots. No stale-write guard exists. **Inference:** embedded human history alone is insufficient evidence against a revisioned index/transaction layer. |
| What promotes candidate material into canon? | Drafts are explicitly non-canon; planner/writer conflicts require author resolution. Reviewer then updates knowledge from review candidates without a separately recorded approval per fact. **Inference:** JeroTan defines the boundary but not a complete promotion record. |
| Can earlier-chapter propagation be partly deterministic? | Task dependencies, continuity notes, typed tracking, and chapter inventory provide inputs, but no impact graph or replay exists. **Inference:** the source supports an impact-analysis candidate, not observed propagation. |
| Single writer or multi-writer locking? | The active workflow is sequential role switching and has no lock/revision protocol. **Inference:** it supports a conservative single canonical writer plus reviewers before multi-writer work. |
| Orchestrator-only context or testable internal service? | JeroTan implements a tested read-only MCP lookup slice with source paths and bounded search; prompts still select the rest. **Inference:** this is the strongest evidence so far for a testable internal context service beneath an orchestrator contract. |
| Shared finding schema? | Editor findings have exact evidence/replacement/reason/status, while reviewer output has broader project sections. **Inference:** a shared envelope with role-specific payloads looks viable, but JeroTan does not persist it. |
| Keep author voice separate from canon? | Constitution and optional personal voice live outside per-story knowledge/tracking. The personal-voice template is not wired into core commands. **Inference:** separation is supported; portability and safe-imitation policy remain open. |
| Supported-host guarantees? | Installer/config tests establish project-root binding and four config formats; generic copy/paste is fallback. No capability matrix or degraded-mode attestation exists. |
| Reproducible packaging/provenance? | Exact licenses and attribution exist, but npm rules exclude the dedicated attribution/root skill/tests and invoke a package through `npx`. **Inference:** CodexWriter needs a stronger distribution manifest and provenance test. |
| CI behavioral fixtures? | JeroTan supplies 11 retrieval/config tests but no CI workflow and no semantic state/context/promotion/repair fixtures. The broader fixture question remains open. |

### Inference

JeroTan answers “should context and format validation have executable support?” more strongly than it answers “what is authoritative state?” It also demonstrates that an excellent approval loop can coexist with incomplete canon-promotion and state-update semantics.

### Uncertainty

No carried answer is an architecture decision. The remaining sources can overturn or refine every candidate.

## 18. Questions to Carry Forward

### Observed basis

1. Can wgwtest provide explicit author/narrator/POV/character/reader knowledge layers absent from JeroTan?
2. Does wgwtest define one authoritative state model or clearer precedence among manuscript, canon, plan, and current state?
3. Can any remaining source demonstrate revisioned history, stale-write protection, or deterministic earlier-chapter impact propagation?
4. Which JeroTan JSON domains deserve typed CodexWriter entities, and which should remain human-readable views?
5. Should a context service cover plan/tasks/world/relationships/timeline as well as JeroTan’s implemented lookup subset?
6. What budget, provenance, coverage, recency, and conflict metadata must a context bundle expose?
7. Can canon extraction be represented as proposed facts with source spans, confidence, author disposition, and revision?
8. Can a unified finding envelope preserve editor exact-replacement semantics, Haowjy reader experience, and continuity evidence?
9. Which semantic checks can become deterministic without pretending to judge story truth mechanically?
10. Should state updates after drafting be one transaction spanning current state, plot, relationships, timeline, task status, and knowledge proposals?
11. What is the smallest viable earlier-revision dependency graph: chapters, scenes, facts, promises/payoffs, timelines, relationships, objects, and knowledge?
12. Does any source justify multi-writer locking, or should the initial design enforce one canonical writer and parallel read-only analysis?
13. How should portable author voice/preferences be created, updated, and safety-bounded separately from story canon?
14. What release test must verify license/attribution, immutable source provenance, generated artifacts, documented commands, engine floors, and package contents?
15. Can Rhavekost add blind-reader, developmental-edit, or repair-pipeline evidence that JeroTan lacks?

### Inference

The provisional source order should continue with `wgwtest/novel-writing` after this analysis is reviewed and merged, unless review explicitly changes the order or authorizes synthesis.

### Uncertainty

No architecture choice, crosswalk change, stable skill-list change, schema decision, or adoption recommendation becomes final in this analysis. All comparisons and dispositions remain provisional until review and a separately authorized synthesis step.
