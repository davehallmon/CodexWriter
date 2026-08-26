# Source Analysis: wgwtest/novel-writing

> **Upstream pin:** `b6382cf7ff29caa83830646432d8010ca96120f5`  
> **Default branch:** `main`  
> **Latest-status check:** live comparison on 2026-08-26 found the pin identical to `main` (`ahead_by: 0`, `behind_by: 0`); no newer default-branch commit existed at analysis time  
> **Analysis date:** 2026-08-26  
> **Decision status:** evidence review only; every CodexWriter disposition is Inference and provisional

This document records the pinned source before any CodexWriter architecture or crosswalk decision. It does not modify `ARCHITECTURE.md`, `docs/crosswalk.md`, or a stable skill list.

## Evidence Labels

- **Observed** — directly supported by an immutable file-and-line link, an executable check, or a complete-tree inventory at the pinned commit.
- **Inference** — an interpretation of observed evidence, not a claim that the source implements the inferred CodexWriter design.
- **Uncertainty** — something the pinned artifacts or bounded verification did not establish.

Claim IDs `W01`–`W50` resolve to immutable links in Section 14. Every linked upstream file uses the pinned commit above; no evidence link uses `main`, `master`, a tag, or another mutable ref.

## 1. Repository Snapshot

### Observed

| Item | Pinned observation |
|---|---|
| Repository | `https://github.com/wgwtest/novel-writing` |
| Commit | `b6382cf7ff29caa83830646432d8010ca96120f5` |
| Default branch | `main` |
| Latest default-branch status | Live `main` resolved to the pin on 2026-08-26 |
| Primary implementation | One Codex fiction skill: Markdown method/router, ten Markdown references, one Python manuscript checker, and OpenAI agent display metadata [W07] [W43] |
| Pinned inventory | 27 blobs total; 13 files in the installable `novel-writing/` package, including ten references and one checker; three repository test files |
| Declared scope | Planning, drafting/continuation, rewriting, and concrete fiction review; not poetry-only, screenplay formatting, pure copyediting, or nonfiction [W01] [W07] |
| Runtime | Codex skill installed by copying or linking the package subdirectory; Python is needed for the optional manuscript checker [W02] [W13] |
| Persistent project state | Explicitly delegated to the separate `novel-project-strategy` responsibility; this package stays focused on narrative work and adjacent-prose continuity [W48] |
| Executable verification | `python -B -m unittest discover -s tests -p 'test_*.py'` passed 20 tests under Python `3.12.13` on 2026-08-26 [W50] |

The README positions the source as a long-form fiction craft skill that favors causal planning, embodied dialogue, concrete findings, style preservation, and realism/access checks. [W01]

### Inference

The source is best understood as a **single-skill narrative reasoning library with a deterministic manuscript-hygiene sidecar**. It is not a novel workspace, persistent story-state service, multi-agent system, or full editing transaction engine.

Its most distinctive evidence after the first five sources is the combination of:

1. an explicit separation among author truth, character knowledge, and reveal boundary;
2. a two-axis cognition model;
3. causal role separation among viewpoint, decision, expertise, and execution;
4. a level-of-detail context policy with a prose-over-summary conflict rule; and
5. behavior-focused dialogue guidance that rejects mechanical gesture insertion.

### Uncertainty

- The analysis did not run a full planning-drafting-review cycle on a real novel.
- Passing tests establish checker and prompt-contract fixtures, not prose quality or uniform model compliance.
- No claim about production maturity, adoption, or general project quality follows from repository age, release count, or the maintenance boundaries recorded later.
- The related project-governance repository was not analyzed here; this document records only how the pinned source delegates that responsibility.

## 2. Licensing and Provenance

### Observed

| Check | Evidence |
|---|---|
| License | Exact root `LICENSE`; MIT text; copyright 2026 wgwtest [W06] |
| License blob | `5b51aeda90ec682d8204d45201b08ff9b26ffd6b` |
| MIT notice condition | The root license says the copyright and permission notice must accompany copies or substantial portions [W06] |
| `NOTICE` | Not found in the complete pinned 27-blob tree |
| Repository-level `ATTRIBUTION.md` | Not found in the complete pinned tree |
| Declared skill lineage | No translation, fork, vendor, or derivative lineage is declared in the pinned skill, README, or contributor documents |
| Additional attribution | `CODE_OF_CONDUCT.md` identifies its Contributor Covenant 2.1 adaptation; this is collaboration-document provenance, not claimed skill lineage [W45] |
| Install boundary | README installation copies only the `novel-writing/` package subdirectory; the exact root `LICENSE` is outside that subdirectory [W46] |
| Package validation boundary | The required-file list validates skill, metadata, references, and checker but does not require a license file inside the installable package [W40] [W46] |

### Inference

Responsibility-level comparison is safe to continue. Copying prompt language, reference methods, Python code, tests, or packaging scripts into CodexWriter would require file-level provenance and preservation of the MIT notice.

The manual install and package-validation layout creates a **provisional redistribution concern**: an installed or separately redistributed package directory can be detached from the repository-root license. That is an engineering provenance risk, not a legal conclusion. CodexWriter should not copy this packaging boundary without a release-level license/notice check.

### Uncertainty

- This is engineering provenance review, not legal advice.
- A user who retains the full clone also retains the root license; the analysis did not inspect every downstream installation or release archive.
- Absence of a declared derivative lineage is not proof that every writing idea is original; no similarity or authorship analysis was performed.
- Contributor Covenant reuse may carry terms outside the skill’s MIT license; that public-document question was not independently reviewed because it does not establish skill behavior.

## 3. Architectural Thesis

### Observed

The skill selects one of three stages—planning, drafting/continuing, or reviewing—and routes the task to only the relevant reference files. [W08]

The installable package separates:

- one top-level behavioral contract in `SKILL.md`;
- ten focused method references;
- one deterministic manuscript checker; and
- one four-line OpenAI display/default-prompt descriptor. [W43] [W49]

The repository root is the human collaboration and maintenance layer, while `novel-writing/` is declared the only editable skill package and runtime copies are treated as derived mirrors. [W03] [W04] [W44] [W49]

Persistent chapter state, cross-session recovery, manuscript-layer synchronization, and parallel chapter ownership are expressly outside this skill’s boundary. [W48]

Project-local rules override the general skill. When structure cards conflict with prose, the skill says to trust prose and update cards later. [W09] [W13]

### Inference

The organizing principle is **progressive disclosure around narrative judgment**:

`identify stage → load minimum method/context → apply causal and epistemic rules → produce prose or concrete findings → optionally run narrow hygiene checks`.

This is a deliberately bounded architecture. Its value lies less in workflow automation than in giving one model a disciplined set of distinctions. The Python checker is adjacent infrastructure, not the source of story truth.

### Uncertainty

- `agents/openai.yaml` supplies presentation metadata and a default prompt; it does not demonstrate a separately scheduled or permissioned agent.
- The source does not specify an orchestrator API, event loop, tool protocol, story database, or handoff envelope.
- Prompt routing can be followed differently by different Codex versions; only selected text contracts and the Python checker are tested.

## 4. Workflow and Orchestration

### Observed

#### 4.1 Stage routing

Planning routes to scene/chapter planning, long-form causal outline, cognition, causality/agency, dialogue behavior, structure, and realism references as needed. Drafting loads introduction, cognition, causality, dialogue, structure, style, and realism guidance. Reviewing starts with the revision checklist, then loads problem-specific references. [W08]

The routing is conditional rather than all-inclusive: optional cognition, responsibility, chapter-interface, and dialogue maps are reserved for scenes where they materially affect the work. [W14]

#### 4.2 Planning sequence

Every scene/chapter planning pass defines a main task, secondary task, POV limit, required characters, required reader information, and forbidden mistakes. [W14]

The plan then names the chapter job, identifies a secondary job, locks POV, orders information, defines the chapter end state, and—when continuity matters—records the entry/exit interface passed between adjacent chapters. [W15]

For larger outlines, the method requires the causal story before system explanation: minimum pre-story state, actor entry, pursuit/escalation, climax, and resulting state. Every major transition should identify pressure/evidence, interpretation, goal, method, changed options, and visible consequence. [W16]

#### 4.3 Drafting and review

Drafting is governed by hard rules for reader anchoring, access, cognition, responsibility, embodied dialogue, functional scene movement, and style preservation. [W10] [W11] [W12]

Reviewing produces structured findings before summary and checks structural/causal failures before sentence polish. [W13] [W32] [W33]

When plain-text delivery and access permit it, the working pattern runs the Python checker and treats warnings as review prompts rather than automatic prose defects. [W13] [W36]

#### 4.4 Enforcement boundary

The skill is a behavioral contract. It does not implement a scheduler, automatic stage transition, task ledger, editor-approval state, or write transaction. The user’s requested task and project-local rules determine whether drafting, review, or revision occurs. [W07] [W13]

### Inference

The strongest orchestration contribution is **selective method loading**, not agent fan-out. It gives an orchestrator a plausible internal decision tree, but the source itself remains one skill invocation.

Planning and review are more operational than generic workshop advice because they demand named jobs, owners, information limits, state changes, and finding fields. They are still model-executed checks rather than mechanically enforced transitions.

### Uncertainty

- No end-to-end fixture proves that the model always loads the right subset of references.
- No stop condition prevents a model from rewriting before findings or applying unapproved edits.
- The source does not define resumable task state or recovery after an interrupted session.
- Nothing in the package establishes multi-writer concurrency, locks, or merge semantics.

## 5. State Storage Model

### Observed

#### 5.1 State vocabulary versus storage

| State question | Observed source behavior |
|---|---|
| Project/author constraints | Existing project rules, outline, timeline, setting, and issue files are loaded from the surrounding project; the skill does not create a dedicated author-memory artifact [W09] [W13] |
| Canon/current story | A standalone outline or canon document should state the current story positively and omit obsolete revision-log residue [W18] |
| Story facts | The outline model distinguishes events that actually occur from character knowledge and hidden author truth [W17] |
| Character knowledge | Cognition is classified by distribution/source and by epistemic status, relative to character, time, and audience [W19] |
| Reader/reveal boundary | The outline separately records what the audience may reasonably confirm by the end of an arc or volume [W17] |
| Narrator/POV access | POV limits perception and pressure; observation, inference, authority, and action are separately checked [W11] [W21] [W22] |
| Scene/chapter current state | Optional entry/exit contracts record positions, actions, injuries, objects, unresolved questions, knowledge, relationship state, and next responsibility [W15] [W23] |
| Objects/identities/counts | Long-form outline guidance audits ownership, transfer, capabilities, aliases, organizations, victims, injuries, money, and elapsed time [W18] |
| Persistent/project state | Delegated outside the package to `novel-project-strategy` [W48] |

These are document and reasoning contracts. The pinned package contains no story database, JSON schema, state files, migrations, or event log.

#### 5.2 Authority and precedence

Two precedence rules are explicit:

1. project-local rules override this general skill; and
2. when structure cards conflict with prose, prose wins and cards are updated later. [W09] [W13]

Author truth must not become character knowledge, later explanation must not leak into earlier decisions, and a synopsis must not solve a mystery the volume preserves. [W17]

#### 5.3 History and revision behavior

Final-form outlines deliberately omit drafting residue, discarded alternatives, and explanations of older versions. Genuine unresolved decisions remain open functional slots rather than false settled facts. [W18]

Earlier-chapter revision uses necessary adjacent prose, entry/exit state, and a patch-versus-rewrite decision. The source does not define global downstream replay, a dependency graph, or automatic recalculation across later chapters. [W23]

### Inference

Wgwtest contributes the strongest **epistemic vocabulary** in the sequence so far, but not a state store. Author truth, character knowledge, reveal boundary, observation, report, inference, intention, and misrecognition are useful candidate distinctions; they are not typed persisted entities in this repository.

The prose-over-card rule provides local conflict precedence. It does not settle authority among direct author edits, canon documents, current-state projections, task records, or derived summaries in a larger CodexWriter system.

Earlier-chapter propagation is best labeled **Inference: guided adjacent-interface repair**. No deterministic impact analysis, revision counter, stale-write check, or replay engine is observed.

### Uncertainty

- No narrator-knowledge store is defined separately from POV/author/character/reveal reasoning.
- Reveal boundary specifies what may be confirmed by an arc endpoint; it is not a time-indexed record of what each reader has actually encountered.
- Entry/exit state has no prescribed file format, stable ID, revision, or provenance field.
- Current canon is favored over revision-log voice, but the source does not say where historical decisions should be preserved elsewhere.
- No rule resolves manuscript-versus-author-intent conflict when prose itself is known to be stale.

## 6. Context Management

### Observed

The source defines five context levels:

- `L0 Task`: immediate job;
- `L1 Hard constraints`: outline, timeline, setting, issues, and project rules;
- `L2 Near-field full text`: current/adjacent chapters and linked manuscript layers;
- `L3 Far-field structure`: chapter cards, timeline slices, and outline slices; and
- `L4 Cold zone`: unrelated future chapters and distant full text, excluded by default. [W09]

Direct language/style revision requires the target full text. Dialogue rhythm, psychology, ambiguity, flirtation, and body-detail work also require relevant prose rather than summary alone. [W09]

If structured cards conflict with prose, prose wins. If structured context is insufficient, the skill expands by targeted full-text reads rather than loading the entire novel. Future-chapter prose stays excluded unless a confirmed continuity dependency requires it. [W09]

The working pattern loads project-local structured artifacts before extra prose, then pulls near-field full text for language, style, or chapter-continuity work. [W13]

### Inference

This is the clearest **human-readable context precedence and level-of-detail policy** among the first six sources. It supplies a useful context-selection contract without claiming that summaries replace prose.

It remains a policy executed through direct file reads. It does not implement retrieval, indexing, embeddings, provenance capture, token accounting, coverage scoring, deduplication, or cache invalidation.

### Uncertainty

- No numeric context/token budget is defined.
- “Confirmed continuity dependency” has no machine-readable representation or discovery algorithm.
- The source does not specify how cards are updated, reviewed, or versioned after prose wins a conflict.
- There is no typed context-bundle output or cross-role handoff manifest.
- The analysis did not test context behavior on a manuscript large enough to force L3/L4 decisions.

## 7. Creative-Craft Model

### Observed

#### 7.1 Causal planning

Long-form outlines must foreground a causal narrative rather than encyclopedic mechanics. Major turns connect pressure/evidence, interpretation, goals, methods, changed options, and consequences; chronology alone is explicitly insufficient. [W16]

Chapter planning names primary/secondary jobs, POV limits, reader information, forbidden mistakes, information order, end state, and adjacent interfaces. [W14] [W15]

#### 7.2 Epistemic and agency model

The outline separates story facts, character knowledge, author truth, and reveal boundary. [W17]

Cognition uses two axes:

- distribution/source: common/shared, specialized/local, private/undisclosed; and
- epistemic status: observation, reported fact, inference/judgment, intention, misrecognition/bias/self-deception. [W19]

For high-conflict or information-asymmetric scenes, an optional cognition table connects accessible information and source to stakes, available action, actual choice, and expression to the present audience. [W20]

Consequential scenes separately name the experiential center, problem owner, decision owner, domain actor, and execution owner. [W21]

The causal scaffold connects spatial/social state, perception or misinterpretation, narrowed options, decision, action, consequence, and reassessment without declaring that sequence a mandatory formula. [W21]

#### 7.3 Dialogue and behavior

Dialogue guidance distinguishes functional action from decorative and procedural movement. Functional behavior reveals agenda/status or changes the next beat; motion alone does not make a scene active. [W24]

The exchange chain links each speaker’s local objective and selective expression to a listener with a different objective/knowledge state, then requires the response to affect the next tactic. Action density is expressly not a quality target, and rapid dialogue may remain untagged. [W25]

Meeting, interview, consultation, interrogation, laboratory, and research guidance ties disclosure and technical procedure to trust, authority, evidence, and human pressure. [W26]

#### 7.4 Character, structure, style, and realism

Character introductions scale anchoring requirements by passing, functional, and core roles and repair weak entrances by clarifying role, relationship, first impression, and a specific marker. [W27]

Scene structure evaluates functional segments, progression, transitions, causal action, pacing, and a changed end condition. [W28]

Style fidelity treats dialogue, interiority, digression, observation, ambiguity, rhythm, and expressive messiness as presumptively style-bearing; deletion carries a stated burden of proof. [W29]

Realism separates observation rights from knowledge rights, then checks institutions, bodily capability, crowds, spectacle, and one-chance access. Unsure real-world facts must be identified for verification rather than asserted. [W30] [W31]

### Inference

The craft model’s strongest contribution is not a branded plot formula. It is a set of **causal and epistemic diagnostics** that protect human agency: who knows, how they know, who may decide, who can act, what changes, and what the reader may confirm.

The dialogue method is also unusually resistant to common automated-revision failure: it rejects both transcript-like exposition and the superficial cure of evenly distributed gestures.

### Uncertainty

- The rules are broadly prescriptive; no comparative study establishes that they improve every genre, narrator, or experimental form.
- “Important character” and “consequential scene” remain model judgments.
- The source does not include dedicated genre packs, market analysis, theme agents, or reader personas.
- Author voice is protected during revision but not stored as a portable preference/voice artifact.
- No safety policy distinguishes legitimate style preservation from close imitation of a living author.

## 8. Evaluation and Continuity

### Observed

Review findings require location, problem type, current behavior, why it fails, revision direction, and whether the issue should become a project rule. If no findings exist, the reviewer says so and records residual uncertainty. [W32]

The minimum review orders structural, causal, responsibility, and continuity failures before sentence polish, then checks reader anchoring, progression, dialogue embodiment, chapter interfaces, style, realism, and manuscript hygiene. [W33]

The deterministic checker reports path, line, severity, rule ID, and message. It scans supported text/Markdown files for replacement characters, trailing whitespace, selected prompt leakage, plain-text Markdown leakage, suspicious Latin fragments, Chinese quote imbalance, adjacent near-duplicate paragraphs, and optional chapter-title format. [W34] [W35] [W36]

Errors fail the checker. Warnings pass normally and fail only under `--strict`; input/encoding failures return a separate exit code. [W34] [W36]

The repository tests exercise checker outcomes, allowlists, directory handling, duplicate detection, optional titles, false-positive examples, Markdown handling, and invalid inputs. Separate contract tests assert that the skill routes to the dialogue and outline references and retains required terminology. All 20 tests passed locally. [W37] [W38] [W39] [W50]

The skill and revision checklist both state that heuristic warnings are review prompts, not automatic literary defects. [W13] [W33]

### Inference

The source provides a useful two-layer evaluation boundary:

1. deterministic contamination/manuscript-hygiene checks; and
2. model-judgment causal, epistemic, craft, and continuity findings.

Its review schema could seed a common finding envelope, but it is not yet a persisted workflow object: there is no finding ID, severity taxonomy for narrative issues, status, evidence span, reviewer identity, or apply transaction.

### Uncertainty

- The checker does not validate story truth, causality, POV correctness, character knowledge, dialogue quality, or cross-chapter state.
- Contract tests verify required text/routing terms, not model behavior or prose outcomes.
- No blind-reader, reader-persona, multi-reviewer, adjudication, or consensus process is present.
- No real long manuscript benchmark or false-positive/false-negative study is included.
- The package has no CI workflow in the pinned tree, so local test results cannot be compared with an upstream automated run.

## 9. Human-in-the-Loop Model

### Observed

The user selects the task and supplies surrounding project rules. Project-specific law overrides the skill’s general method. [W07] [W13]

Review produces structured findings before summary; it does not instruct automatic application of every recommendation. [W13] [W32]

Each finding asks whether it should become a project rule, but the package defines no automatic rule-promotion action or storage location. [W32]

When realism is uncertain, the skill requires disclosure of what needs verification and recommends the most conservative plausible draft if writing must continue. [W31]

When policy/tooling prevents retaining a detail, the style guide requires disclosing the loss instead of presenting it as ordinary improvement. [W29]

### Inference

The human role is strongest at task definition, project-rule authority, and judgment over findings. The source assumes collaboration but does not formalize approval states.

“Should this become a project rule?” is a promising escalation question, not an observed canon/rule promotion transaction.

### Uncertainty

- No explicit confirmation is required before a rewrite or local patch is applied.
- No exact-text compare, expected revision, rollback, or author disposition status exists.
- Direct author edits outside the skill have no reconciliation protocol beyond rereading the prose and project files.
- No permission boundary prevents the skill from touching unrelated files; scope control remains prompt-level.

## 10. Runtime and Maintenance

### Observed

#### 10.1 Installation and source boundary

README supports cloning then copying the `novel-writing/` subdirectory, or symlinking that subdirectory for local development; Codex should restart after installation/update. [W02]

The repository declares itself the only editable source, the package subdirectory the only editable skill package, and runtime copies/links or same-named directories elsewhere as derived mirrors. [W03] [W04] [W44] [W49]

The Windows development-link script resolves `CODEX_HOME` or `%USERPROFILE%\.codex`, backs up an existing target with a timestamp, and creates a directory junction to the source package. [W42]

#### 10.2 Package validation

The PowerShell package checker requires all package files, validates skill front matter and reference links, scans the package for absolute/local paths and named private-project residues, syntax-checks the Python checker, runs its help, and invokes the repository’s unittest suite. [W40] [W41]

The pinned environment did not have PowerShell (`pwsh`), so the wrapper was not executed. Its Python test command was run directly and passed all 20 tests; `git diff --check` also passed.

#### 10.3 Pinned maintenance boundaries

Every item below is an **Observed repository fact**, not a general quality judgment.

1. **License/package separation:** the exact MIT license exists only at repository root, while documented installation copies the license-free package subdirectory and package validation does not require an in-package license. [W46]
2. **Checker language orientation:** the public skill is described for fiction generally, but the checker’s prompt patterns and quote-balance rule are Chinese-specific and its Latin-fragment heuristic warns on ordinary multiword English prose. [W47]
3. **English fixture behavior:** a bounded local fixture containing an English chapter title and one English sentence produced two `latin-fragment` warnings; normal mode exited `0`, while `--strict` exited `1`, matching the documented warning policy. [W34] [W36] [W47]
4. **PowerShell wrapper boundary:** Unix-like README installation is documented, but the full package validation/release helper is PowerShell-only. [W02] [W05] [W41]
5. **No pinned CI workflow:** the complete tree includes issue/PR templates but no `.github/workflows/` file; verification is documented as a maintainer-local step. [W05] [W44]
6. **Contract-test depth:** dialogue and outline tests assert routing and required phrases, while executable behavioral tests concentrate on the manuscript checker. [W37] [W38] [W39]
7. **No package version manifest:** the installable package has no package manifest or version field; release/tag procedure is maintained at repository level. [W05] [W49]

### Inference

The source has a disciplined maintenance boundary for private-path leakage, required references, test execution, and source-of-truth ownership.

Likely consequences of the listed boundaries—lost license notice in detached distributions, noisy English checker output, reduced validation portability, or undetected main-branch failures—are hypotheses for release testing, not evidence that the project is generally low quality.

### Uncertainty

- Full package validation was not run because PowerShell was absent; static inspection and the direct Python tests do not prove every PowerShell branch succeeds.
- The checker’s intended primary manuscript language is not explicitly declared. Its behavior is Chinese-oriented, but ordinary English may be accepted with warnings in non-strict mode or customized through allowlists.
- The analysis did not inspect every release archive or third-party installer.
- No upstream CI status exists at the pin.
- No conclusion about overall maintainability follows solely from these boundaries.

## 11. Strengths

### Observed

1. Clear stage routing with selective reference loading. [W08]
2. An explicit L0–L4 context policy, targeted expansion, future-prose exclusion, and prose-over-card precedence. [W09]
3. Causal outline bridges require actors, pressures, goals, choices, changed options, and consequences. [W16]
4. Story facts, character knowledge, author truth, and reveal boundaries are separated. [W17]
5. Cognition is classified by both distribution/source and epistemic status, relative to character, time, and audience. [W19]
6. Viewpoint, problem ownership, decision authority, domain capability, and execution are distinct roles. [W21]
7. Dialogue guidance distinguishes meaningful behavior from decorative and merely procedural motion. [W24] [W25]
8. Character entry, scene progression, style preservation, and realism each have concrete diagnostic questions. [W27] [W28] [W29] [W30] [W31]
9. Review output requires localized, typed, actionable findings and residual uncertainty. [W32]
10. The checker has deterministic rule IDs, severities, line locations, explicit exit behavior, and executable tests. [W34] [W35] [W36] [W37]
11. Package validation checks front matter, required references, local-path leakage, private residue, checker syntax, and tests. [W40] [W41]
12. The root license is exact MIT text rather than a badge-only claim. [W06]

### Inference

Wgwtest is especially valuable for **epistemic causality**: keeping hidden truth, situated knowledge, viewpoint pressure, authority, and action connected without collapsing them into one omniscient plot summary.

Its context and dialogue rules also demonstrate useful restraint. More context and more action beats are not automatically treated as better.

### Uncertainty

- Strength of a written contract does not prove consistent model execution.
- Tests do not score story quality or compare revisions against human judgments.
- Several rules may need genre- or author-specific exceptions.

## 12. Weaknesses / Gaps

### Observed

1. The package deliberately omits persistent chapter/project state and delegates it elsewhere. [W48]
2. Epistemic layers and entry/exit state are guidance, not stored schemas or revisioned records. [W17] [W19] [W23]
3. No global state update, event history, stale-write protection, lock, or downstream replay is implemented.
4. Context LOD is prompt policy; there is no retrieval/index/context-bundle service. [W09]
5. Findings lack stable IDs, disposition status, narrative severity, reviewer identity, and an apply transaction. [W32]
6. No explicit author approval gate precedes patching or rewriting. [W23] [W32]
7. The deterministic checker validates contamination/hygiene, not semantic story correctness. [W34] [W35] [W36]
8. English prose predictably triggers the Latin-fragment warning heuristic. [W47]
9. Contract tests check text presence rather than model adherence or output quality. [W38] [W39]
10. The installed package can be separated from its root license. [W46]
11. Full validation depends on PowerShell, and no pinned CI workflow runs it automatically. [W05] [W41]
12. There is no reader-simulation role, persistent reader-known timeline, or separately modeled narrator knowledge.

### Inference

The largest architectural gap is intentionally out of scope: **operational story state**. The source sharply describes reasoning at a scene or outline boundary but does not preserve that reasoning as versioned project data.

The largest evaluation gap is the distance between rich semantic guidance and narrow executable checks. CodexWriter would need to keep deterministic hygiene honest about its scope while testing model-judgment findings separately.

### Uncertainty

- The complementary project-strategy repository may address some state/workspace gaps; it was not imported into this source’s observed capabilities.
- A surrounding Codex project may add approval, versioning, or retrieval contracts, but this package does not standardize them.
- The checker may intentionally target Chinese manuscripts despite the broader README; maintainer intent is not explicit.
- Absence of CI does not mean tests are not run before releases.

## 13. Relevance to CodexWriter

Every item below keeps observed source responsibilities separate from CodexWriter direction. All borrowing/disposition language is Inference and provisional; nothing changes an architecture or crosswalk decision.

### Observed source responsibilities

| Wgwtest responsibility | Observed source behavior—not CodexWriter direction |
|---|---|
| Stage selection | Routes planning, drafting, and review into focused methods [W08] |
| Context LOD | Separates task, constraints, near-field prose, far-field structure, and cold content [W09] |
| Causal outline | Connects pressure, interpretation, choice, and consequence [W16] |
| Epistemic separation | Distinguishes facts, character knowledge, author truth, and reveal boundary [W17] |
| Cognition classification | Tracks source/distribution and present epistemic status [W19] |
| Agency separation | Distinguishes experiential, problem, decision, domain, and execution roles [W21] |
| Chapter interface | Records entry/exit state and selects patch versus rewrite [W23] |
| Dialogue behavior | Connects objectives, selective expression, listener response, and next tactic [W24] [W25] |
| Style preservation | Protects voice-bearing texture and discloses unavoidable loss [W29] |
| Concrete review | Requires localized problem/reason/revision fields [W32] |
| Hygiene checking | Emits deterministic file/line/severity/rule findings [W34] [W35] [W36] |
| Package validation | Checks package completeness, public safety, syntax, and tests [W40] [W41] |

### Inference — Provisional architectural candidates

- **Strongly investigate:** author-truth, character-knowledge, reveal-boundary, and POV-access distinctions in the authority model.
- **Strongly investigate:** cognition facts with source, confidence/status, holder, time, and audience.
- **Strongly investigate:** context LOD with explicit prose-over-derived-card precedence.
- **Strongly investigate:** separate problem, decision, domain, and execution ownership in scene/task contracts.
- **Strongly investigate:** causal bridge and entry/exit interface checks as inputs to impact analysis.
- **Strongly investigate:** behavior-based dialogue review that avoids action-density metrics.
- **Investigate:** a common finding envelope that extends Wgwtest’s fields with identity, severity, evidence span, disposition, provenance, and revision.
- **Investigate:** deterministic manuscript hygiene as an explicitly narrow validator class.

### Inference — Provisional implementation borrowing requiring provenance

- Manuscript-checker rules, CLI behavior, and tests.
- Exact prompt and reference wording.
- Package validation and private-path hygiene patterns.
- Cognition tables, causal scaffolds, finding templates, and examples.

Any implementation-level reuse requires MIT notice preservation, wgwtest provenance, and a distribution manifest that keeps license material with the reused files.

### Inference — Provisional patterns to avoid

- Avoid treating epistemic guidance as persisted state when it has no schema or revision.
- Avoid treating prose-over-card precedence as a complete cross-domain authority model.
- Avoid turning causal scaffolds into mandatory plot formulas.
- Avoid equating action-beat density with dialogue quality.
- Avoid presenting contamination checks as semantic continuity validation.
- Avoid distributing an extracted package without its applicable license/notice.
- Avoid language-specific heuristics without declared scope, fixtures, or degraded-mode behavior.
- Avoid local-only release checks when CI/reproducible automation is feasible.

### Uncertainty

- No responsibility, schema, API, or file layout becomes stable through this analysis.
- Rhavekost and later synthesis may strengthen, merge, or overturn these candidates.
- Implementation reuse has not been authorized by this responsibility-level comparison.

## 14. Detailed Evidence

### Observed: claim-level traceability map

| Claim | Immutable evidence |
|---|---|
| W01 | [README purpose, features, fit, and delegated project strategy, lines 9–36](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L9-L36) |
| W02 | [manual/link installation and restart, lines 46–76](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L46-L76); [repository/package layout, lines 78–86](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L78-L86) |
| W03 | [maintainer source-of-truth and pre-commit validation note, lines 101–108](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L101-L108) |
| W04 | [maintainer source boundaries and read order, lines 3–22](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CODEX_START_HERE.md#L3-L22) |
| W05 | [development, public-safety, and release workflow, lines 24–59](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CODEX_START_HERE.md#L24-L59) |
| W06 | [exact root MIT license, lines 1–21](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/LICENSE#L1-L21) |
| W07 | [skill metadata, scope, and exclusions, lines 1–29](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L1-L29) |
| W08 | [planning/drafting/review stage routing, lines 30–70](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L30-L70) |
| W09 | [context LOD, precedence, targeted expansion, exclusion, and state delegation, lines 72–92](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L72-L92) |
| W10 | [reader-versus-author knowledge and character-entry rules, lines 94–123](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L94-L123) |
| W11 | [access, cognition, and scene-role rules, lines 124–147](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L124-L147) |
| W12 | [dialogue behavior, functional segments, and style preservation, lines 149–176](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L149-L176) |
| W13 | [specific review, project-rule priority, and working pattern, lines 178–203](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L178-L203) |
| W14 | [planning outputs and optional aids, lines 1–37](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/planning.md#L1-L37) |
| W15 | [planning sequence, end state, and chapter interface, lines 39–102](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/planning.md#L39-L102) |
| W16 | [story-first outline and causal bridges, lines 1–72](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/story-outline-and-causal-summary.md#L1-L72) |
| W17 | [story facts, character knowledge, author truth, and reveal boundary, lines 74–87](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/story-outline-and-causal-summary.md#L74-L87) |
| W18 | [object/identity audit and final-form canon rules, lines 104–142](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/story-outline-and-causal-summary.md#L104-L142); [failure modes and final check, lines 144–167](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/story-outline-and-causal-summary.md#L144-L167) |
| W19 | [cognition distribution/source, epistemic status, and decision chain, lines 1–42](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/cognition-layers-and-language.md#L1-L42) |
| W20 | [scene cognition table, dialogue rules, failures, and review questions, lines 44–78](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/cognition-layers-and-language.md#L44-L78) |
| W21 | [scene roles and causal spine, lines 12–37](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/scene-causality-and-agency.md#L12-L37) |
| W22 | [POV pressure, topology, dialogue adjacency, and reveal timing, lines 39–83](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/scene-causality-and-agency.md#L39-L83) |
| W23 | [chapter interface and patch-versus-rewrite rules, lines 84–124](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/scene-causality-and-agency.md#L84-L124) |
| W24 | [functional, decorative, and procedural action, lines 1–37](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/dialogue-and-behavior.md#L1-L37) |
| W25 | [behavior chain, action density, consequential beats, and selective POV, lines 38–100](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/dialogue-and-behavior.md#L38-L100) |
| W26 | [professional-scene guidance and dialogue planning, lines 102–140](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/dialogue-and-behavior.md#L102-L140); [revision pass and failed repairs, lines 142–161](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/dialogue-and-behavior.md#L142-L161) |
| W27 | [character entry levels, questions, and context, lines 1–69](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/character-introductions.md#L1-L69); [villain entry, failures, repair, and review, lines 71–114](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/character-introductions.md#L71-L114) |
| W28 | [scene function, progression, transition, pacing, and ending, lines 1–81](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/scene-and-structure.md#L1-L81); [failure modes and review questions, lines 83–99](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/scene-and-structure.md#L83-L99) |
| W29 | [style-bearing material, correction boundary, deletion burden, and rewrite strategy, lines 1–69](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/style-fidelity.md#L1-L69); [style review questions, lines 78–83](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/style-fidelity.md#L78-L83) |
| W30 | [realism access, knowledge, institution, and body checks, lines 1–74](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/realism-constraints.md#L1-L74) |
| W31 | [crowds, spectacle, one-chance access, uncertainty, and review, lines 75–122](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/realism-constraints.md#L75-L122) |
| W32 | [review finding schema and problem types, lines 1–33](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/revision-checklist.md#L1-L33) |
| W33 | [minimum review procedure and checker boundary, lines 34–100](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/revision-checklist.md#L34-L100); [false assumptions and example finding, lines 102–125](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/references/revision-checklist.md#L102-L125) |
| W34 | [checker scope, patterns, and CLI controls, lines 1–78](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L1-L78) |
| W35 | [allowlist, discovery, Latin warning, and per-line contamination checks, lines 81–202](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L81-L202) |
| W36 | [quote balance, duplicate/title checks, output, and exit codes, lines 204–282](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L204-L282) |
| W37 | [manuscript-checker CLI tests, lines 14–204](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_check_manuscript_text.py#L14-L204) |
| W38 | [dialogue routing and contract tests, lines 14–47](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_dialogue_behavior_contract.py#L14-L47) |
| W39 | [story-outline routing and contract tests, lines 13–39](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_story_outline_contract.py#L13-L39) |
| W40 | [package required files, front matter, and reference checks, lines 1–43](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/scripts/check-package.ps1#L1-L43) |
| W41 | [public-path/private-residue scans and executable validation, lines 45–116](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/scripts/check-package.ps1#L45-L116) |
| W42 | [Codex-root resolution, backup, and junction install, lines 1–56](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/scripts/install-local-dev-link.ps1#L1-L56) |
| W43 | [OpenAI interface metadata and default prompt, lines 1–4](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/agents/openai.yaml#L1-L4) |
| W44 | [contribution source, package, privacy, and validation rules, lines 13–29](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CONTRIBUTING.md#L13-L29) |
| W45 | [Code of Conduct’s Contributor Covenant attribution, lines 68–74](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CODE_OF_CONDUCT.md#L68-L74) |
| W46 | [manual installation copies the package subdirectory, lines 46–54](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L46-L54); [exact root notice condition, lines 1–13](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/LICENSE#L1-L13); [required package file list omits a license, lines 6–24](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/scripts/check-package.ps1#L6-L24) |
| W47 | [general fiction positioning, lines 9–35](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L9-L35); [Chinese prompt patterns and Latin patterns, lines 15–33](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L15-L33); [Latin-warning implementation, lines 130–169](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L130-L169); [Chinese quote-balance check, lines 204–218](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/scripts/check_manuscript_text.py#L204-L218) |
| W48 | [README delegation of project recovery/state/governance, lines 24–36](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L24-L36); [skill delegation of persistent/collaborative state, lines 90–92](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/novel-writing/SKILL.md#L90-L92) |
| W49 | [repository/package separation, lines 78–86](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/README.md#L78-L86); [maintainer source boundaries, lines 8–14](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CODEX_START_HERE.md#L8-L14); [contribution source/package boundary, lines 13–21](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/CONTRIBUTING.md#L13-L21) |
| W50 | [checker behavioral test suite, lines 14–204](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_check_manuscript_text.py#L14-L204); [dialogue contract suite, lines 14–47](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_dialogue_behavior_contract.py#L14-L47); [outline contract suite, lines 13–39](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/tests/test_story_outline_contract.py#L13-L39); [package validator test invocation, lines 100–116](https://github.com/wgwtest/novel-writing/blob/b6382cf7ff29caa83830646432d8010ca96120f5/scripts/check-package.ps1#L100-L116) |

### Observed: licensing/provenance paths checked

| Path | Result |
|---|---|
| Root `LICENSE` | Found; exact MIT text; blob `5b51aeda90ec682d8204d45201b08ff9b26ffd6b` [W06] |
| Root/package `NOTICE` | Not found in the complete pinned tree |
| Root/package `ATTRIBUTION.md` | Not found in the complete pinned tree |
| Declared skill upstream/derivative lineage | Not found in the pinned skill/README/contributor corpus |
| `CODE_OF_CONDUCT.md` attribution | Found; Contributor Covenant 2.1 adaptation [W45] |
| Installable-package license | Not found under `novel-writing/`; root license is outside the copied package [W46] |

### Observed: corpus and verification checks

- Checked the complete recursive tree at the pin: 36 entries (27 blobs and 9 directories), not truncated.
- Read all behavior-bearing files: root/maintainer/contributor docs, the skill, agent metadata, all ten references, checker, package/link scripts, and all three test files.
- Searched the pinned tree for `LICENSE`, `NOTICE`, attribution, workflows, state/history/revision/lock terms, and absolute-path/package boundaries.
- Ran the repository’s direct Python test command: 20 passed, 0 failed under Python `3.12.13`.
- Ran `git diff --check`: passed.
- Could not execute the PowerShell package wrapper because `pwsh` was unavailable; inspected every branch of the 116-line script and ran its Python test command directly.
- Ran one bounded English fixture through the checker in normal and strict modes; both produced two Latin-fragment warnings, with exits `0` and `1` respectively.

### Inference

The evidence establishes prompt contracts, package-maintenance rules, and deterministic checker behavior. It does not establish end-to-end story quality, semantic continuity accuracy, state safety, or uniform behavior across Codex versions.

### Uncertainty

- Negative inventory claims apply only to the pinned tree.
- Live release/branch metadata was checked for orientation but was not used as immutable behavior evidence.
- Related repositories linked from the README were not treated as capabilities of this pinned package.

## 15. Provisional CodexWriter Disposition

All dispositions in this section are **Inference** and provisional. They require comparative synthesis and separate architecture/crosswalk review.

### Inference — Provisional retain / strongly investigate candidates

- **Retain responsibility:** planning, drafting, reviewing, and style-preserving revision.
- **Strongly investigate:** explicit author-truth, character-knowledge, reveal-boundary, and POV-access distinctions.
- **Strongly investigate:** cognition classification by holder/source/status/time/audience.
- **Strongly investigate:** context LOD plus prose-over-derived-view precedence.
- **Strongly investigate:** causal role and chapter-interface contracts.
- **Strongly investigate:** dialogue behavior as tactic/response change rather than gesture density.
- **Strongly investigate:** structured findings before repair.
- **Retain responsibility:** narrow deterministic manuscript hygiene with honest scope disclosure.

### Inference — Provisional adapt candidates

- **Adapt:** epistemic distinctions into versioned, provenance-bearing state rather than unpersisted tables alone.
- **Adapt:** chapter entry/exit contracts into typed revision-impact inputs.
- **Adapt:** context LOD into a budgeted context-bundle service with provenance, coverage, and conflict metadata.
- **Adapt:** review fields into a shared finding envelope with stable identity, severity, status, evidence, and revision.
- **Adapt:** “should this become a project rule?” into an explicit proposed-rule/promotion workflow.
- **Adapt:** language-specific checker rules into declared profiles with per-language fixtures and degraded modes.
- **Adapt:** package validation into cross-platform CI and license/provenance checks.

### Inference — Provisional merge/split candidates

- **Merge candidate:** cognition source/status with reader/character/narrator access state.
- **Split candidate:** author truth, character belief, narrator availability, POV access, and reader-confirmed state.
- **Split candidate:** deterministic contamination checks from semantic story review.
- **Split candidate:** finding generation, human disposition, and edit application.
- **Split candidate:** current outline/canon view from decision/revision history.

### Inference — Provisional extension candidates

- Revisioned facts, expected-revision guards, and multi-artifact update transactions.
- Dependency/impact reports from causal bridges, objects, knowledge changes, and chapter interfaces.
- Reader simulation and blind-read evaluation.
- Persisted rule proposals with author disposition and provenance.
- Cross-language checker profiles and false-positive measurement.
- Release manifests that keep licenses, provenance, code, prompts, tests, and generated package contents aligned.

### Inference — Provisional defer

- Exact cognition and chapter-interface schemas.
- Exact L0–L4 naming and context thresholds.
- Exact craft rules as universal defaults.
- Multi-writer execution until authority, revision, and locking semantics are settled.
- Importing the complementary project-strategy repository before it receives its own authorized analysis.

### Inference — Provisional reject / avoid candidates

- Treating outline guidance as a transactional state system.
- Treating reveal boundary as a complete reader-known timeline.
- Treating prose-over-card precedence as a universal authority rule.
- Mechanical action-beat targets.
- Silent broad smoothing of style-bearing prose.
- Semantic claims based on contamination-checker output.
- Detached package redistribution without applicable license/notice material.
- Architecture or crosswalk changes in this source-analysis PR.

## 16. Six-Source Comparative Baseline

### Inference — Provisional comparison of observed source evidence

The source columns summarize evidence recorded in separate analyses. Every comparison and the `Provisional Phase 1 reading` column is Inference, not a new source observation or CodexWriter decision.

| Dimension | Lensetek | Dewhurst | Zenstory | Haowjy | JeroTan | Wgwtest | Provisional Phase 1 reading |
|---|---|---|---|---|---|---|---|
| Orchestration | Broad lifecycle routing | File/CLI workflows | Scenario stages, hooks, transactions | Muse plus cognitive-role staffing | File/status router and eight stages | One skill with three-stage reference routing | Wgwtest adds disciplined internal routing, not a new control plane |
| Author contract | Limited | Project/config conventions | Commercial/genre constraints and gates | Author direction authoritative | Dedicated constitution/clarification | Project-local rules override; no dedicated artifact | JeroTan remains strongest explicit artifact; Wgwtest reinforces local-authority priority |
| Static canon | Skills/references | Markdown artifacts | Canon Markdown plus projections | Human-editable KB/wiki | Lean spec plus rich knowledge | Final-form outline/canon guidance | Wgwtest sharpens current-canon presentation but supplies no store |
| Dynamic state | Limited | Character/scene/current artifacts | Bounded snapshots/projections | Evolving pages | Five JSON domains plus tasks | Optional entry/exit contracts only | Wgwtest adds interface vocabulary, not persistent state |
| Epistemic state | Reader role | Representable | Reader-known timeline | Explicit concept | Character knowledge field | Facts, character knowledge, author truth, reveal boundary; two cognition axes | Wgwtest supplies the richest reasoning taxonomy; persistence remains open |
| History | Limited | Mostly current artifacts | Deltas/events plus current state | Source anchors/current pages | Mixed snapshots/history/logs | Final-form docs omit revision residue | No source yet supplies one complete cross-domain revision history |
| Stale-write safety | Not central | None found | Previously inferred candidate sequential guard | Reread/conflict instructions | No guard | None | Still unresolved; no concurrent-write evidence |
| Context | Responsibility handoffs | Explicit reloads | Bounded projections/far-field query | Role-specific files/history | Shards, prose, tested lookup | L0–L4, targeted expansion, prose over cards | Wgwtest offers strongest explicit selection/precedence policy; JeroTan strongest implemented lookup slice |
| Agency/causality | Broad roles | Workflow-oriented | Operational stages | Cognitive roles | Plan/task/review stages | Experiential/problem/decision/domain/execution roles plus causal bridges | Wgwtest most clearly separates viewpoint from authority and capability |
| Reader simulation | Explicit responsibility | Limited | Review approximation | Dedicated experiential role | None | None | Haowjy remains strongest source evidence |
| Evaluation | Broad roles | CLI checks/review | Scripts/hooks/review | Critic/editor/reader/continuity | Format scripts + editor/reviewer | Structured findings + contamination checker | Wgwtest adds epistemic/causal finding shape but no apply state |
| Creative craft | Broad | Comparatively light | Commercial web-fiction method | General prose/reader method | Structured craft/genres | Causal, epistemic, agency, dialogue, style, realism method | Wgwtest is strongest on causal/epistemic reasoning and anti-mechanical dialogue repair |
| Runtime | Limited | CLI/package | Broad adapters/degradation | Mars/Claude + fallback | Four-host installer/MCP/tests | Codex package, Python checker/tests, PowerShell validation | Wgwtest is narrower but testable; license/portability boundaries need review |
| License/provenance | Exact source license | Exact source license | Exact source license | Exact source license | Exact derivative/original licenses and attribution | Exact root MIT; installable package omits license | Wgwtest strengthens the need for package-level provenance tests |

### Inference

After six sources, a provisional split is clearer:

- operational state and revision safety require explicit infrastructure;
- epistemic, causal, craft, and context-selection policy can remain human-readable but should emit typed evidence where machines depend on it;
- prose, derived views, and hidden author truth need distinct authority and access rules;
- deterministic validators must declare their narrow scope; and
- findings, promotion, and application need separate states.

Wgwtest strengthens the reasoning layer without settling the persistence layer.

### Uncertainty

- The table compares contracts and implementation evidence, not equivalent output quality.
- Evidence depth differs among sources and is not a ranking of overall quality.
- All comparative conclusions remain provisional until Rhavekost and a separately authorized synthesis.

## 17. Answers to Questions Carried From JeroTan

### Observed evidence with explicit inference boundaries

| Carried question | Wgwtest evidence-based answer |
|---|---|
| Can author, narrator/POV, character, and reader knowledge be separated? | Story facts, character knowledge, author truth, and reveal boundary are explicit; POV perception/pressure and cognition status are separate. No narrator store or time-indexed reader-known ledger exists. **Inference:** this is the strongest taxonomy so far, not a complete persisted model. |
| Is there one authoritative state model or clearer precedence? | Project rules override the skill, and prose overrides conflicting structure cards. Final-form canon omits revision residue. **Inference:** two local precedence rules are observed, but no total state authority model exists. |
| Is revisioned history, stale-write protection, or deterministic propagation implemented? | No. Adjacent entry/exit interfaces and causal bridges guide review only. **Inference:** they could seed impact analysis but are not replay or stale-write mechanisms. |
| Which JeroTan domains deserve typed entities? | Wgwtest adds strong conceptual evidence for cognition, decision ownership, object transfer, and chapter interfaces but supplies no persistent schema. Entity adoption remains provisional. |
| Should context become a service? | L0–L4 and prose-over-card precedence define policy, while retrieval remains direct model reading. **Inference:** selection policy and retrieval mechanics should be separable. |
| What must a context bundle expose? | Task, hard constraints, near-field prose, far-field structure, exclusions, and conflicts are explicit. Numeric budget, provenance manifest, coverage, and recency are absent. |
| How should canon extraction work? | Author truth must not leak into character knowledge, and unresolved slots must not be presented as settled. No proposed-fact promotion record exists. |
| Can findings share an envelope? | Review fields cover location/type/current behavior/reason/direction/rule proposal. **Inference:** extend rather than copy this shape; identity, severity, evidence span, disposition, provenance, and revision are missing. |
| Which checks can be deterministic? | Encoding/prompt/Markdown leakage, Latin fragments, Chinese quote balance, adjacent duplication, whitespace, and optional titles are executable. Semantic causality and continuity remain model judgment. |
| Should drafting updates be one transaction? | The source does not update persistent story state. It neither supports nor refutes a transactional model. |
| What is the smallest revision-dependency graph? | Causal bridges, object transfers, knowledge changes, decision ownership, and chapter entry/exit state identify candidate edges. **Inference:** no graph is implemented. |
| Does the source justify multi-writer locking? | No; it delegates parallel chapter ownership and persistent collaboration state to another responsibility. |
| How should author voice be stored? | Style-bearing material is protected, but no portable voice/preference memory exists. |
| What should release provenance verify? | The package checker validates files/references/privacy/tests but not in-package license presence and has no CI. **Inference:** license/material manifest and cross-platform automation are required candidates. |
| Does it add blind-reader evidence? | No. Reader anchoring and reveal boundary are craft checks, not a simulated first-time reader role. |

### Inference

Wgwtest answers “how should a model reason about knowledge, authority, and causal action?” more strongly than “where should those facts live?” It materially sharpens candidate internal semantics while leaving storage and transactions unresolved.

### Uncertainty

No answer above is an architecture decision. Rhavekost can still add stronger evaluation, repair, or workflow evidence.

## 18. Questions to Carry Forward

### Observed basis

1. Can Rhavekost provide a genuine blind-reader or developmental-reader role rather than reader anchoring rules alone?
2. Does it persist findings with identity, evidence, severity, status, and repair history?
3. Does it separate diagnosis, author disposition, repair planning, and edit application?
4. Can it preserve author truth, narrator/POV access, character belief, and reader-confirmed state without omniscience leakage?
5. Does it define a canonical state authority or revisioned history missing from Wgwtest?
6. Can any remaining evidence justify stale-write protection, locking, or deterministic earlier-chapter propagation?
7. Which causal bridge and chapter-interface fields are stable enough to become impact-graph inputs?
8. Can reader simulation test whether the intended reveal boundary matches what prose actually establishes?
9. Can evaluation distinguish a source defect, a derived-card defect, and a context-assembly defect?
10. What is the smallest shared finding envelope across editor, critic, continuity, reader, realism, and deterministic validators?
11. Should project-rule proposals and canon-fact proposals share a promotion workflow or remain separate?
12. How should prose-over-derived-view precedence handle known stale prose or an explicit later author correction?
13. Which context LOD guarantees must be executable rather than prompt-only?
14. What language-profile and false-positive tests should gate manuscript hygiene tools?
15. What release manifest guarantees license/attribution, immutable provenance, package contents, tests, and supported runtimes remain aligned?

### Inference

The provisional source order should continue with `rhavekost/author-toolkit` after this analysis is reviewed and merged, unless review explicitly changes the order or authorizes synthesis.

### Uncertainty

No architecture choice, crosswalk change, stable skill-list change, schema decision, or adoption recommendation becomes final in this analysis. Every comparison and disposition remains provisional until review and a separately authorized synthesis step.
