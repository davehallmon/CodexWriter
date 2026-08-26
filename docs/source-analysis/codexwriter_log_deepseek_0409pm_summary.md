# Project Handoff Briefing

## 1. Project Overview

- **Purpose:** CodexWriter is an AI-assisted fiction authoring framework. It synthesizes ideas from seven open-source fiction-writing skill repositories into a modular, version-controlled system of skills, schemas, and workflows for long-form narrative projects.  
- **Repository URL:** `https://github.com/davehallmon/CodexWriter`  
- **Branch:** `development` is the main integration branch. `main` exists but is not used for active work.  
  - PR #2 (Lensetek analysis) has been merged into `development`.  
  - PR #3 (Dewhurst analysis) is **open and awaiting review/merge**.  
  - The next planned branch `source-analysis/zenstory` has **not** been created yet (blocked by a GitHub connector outage).  
- **Current status:** Phase 1 – Architecture & Source Preservation. The repository contains scaffolding, initial architecture documentation, and two completed source-analysis drafts (Lensetek and Dewhurst). No executable skills have been written yet.

**One-sentence description:**  
CodexWriter will be a structured system that turns general-purpose AI assistants into capable fiction-writing collaborators by combining persistent story state, specialist editorial agents, deterministic continuity checks, and human-in-the-loop control.

---

## 2. Repository State

### Files created / modified during this conversation

| File | Purpose | Dependencies | Notes |
|------|---------|--------------|-------|
| `.gitignore` | Standard ignore rules for OS, editors, Python, Node, logs, temp files | None | Created manually via GitHub web UI |
| `README.md` | Project overview, principles, planned structure, source list, phase status | None | Later edited to correct source count from six to seven and to add direct URLs; full latest not in conversation after later edits |
| `ARCHITECTURE.md` | High-level design document; skeleton initially created, later expanded by PR #1 audit | None | Latest full content not provided after PR #1; initial skeleton is included below |
| `ATTRIBUTION.md` | Licensing and provenance table for the seven source repositories | None | Later updated in PR #1 with verified licenses; full latest not provided |
| `templates/SKILL_TEMPLATE.md` | Standard template for all future skill modules | None | Full content provided |
| `docs/crosswalk.md` | Cross-walk table mapping Lensetek roles to improvement sources | None | Later expanded in PR #1; full latest not provided |
| `docs/source-analysis/README.md` | Instructions and status for source analysis documents | None | Later strengthened in PR #1 and updated after each source analysis; latest not fully provided |
| `test.md` | Test file used to verify ChatGPT write access | None | Content was updated by ChatGPT to include write-access verification line |
| `docs/architecture-audit.md` | New file created in PR #1 containing the seven-repository high-level audit | None | Full content not provided |
| `docs/source-analysis/lensetek.md` | New file from PR #2; evidence-based analysis of Lensetek repository | None | Full content not provided |
| `docs/source-analysis/danjdewhurst-story-skills.md` | New file from PR #3; evidence-based analysis of Dewhurst repository | None | Full content not provided; PR #3 currently open |

### Deleted files  
None.

---

## 3. Code Artifacts

### Important files with full code available from the conversation

#### `.gitignore`

```gitignore
# OS generated files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/

# Environment files
.env
.env.local

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
pip-log.txt
pip-delete-this-directory.txt

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Logs
*.log

# Temporary files
*.tmp
*.swp
*.swo
*~
```

#### `ARCHITECTURE.md` (initial skeleton, before PR #1 modifications)

```markdown
# CodexWriter — Architecture

> This document describes the high-level design of CodexWriter.  
> It is a working draft and will evolve as we analyze source repositories and implement skills.

## 1. Goals

- Provide a modular, version-controlled suite of AI fiction-writing skills.
- Preserve persistent story state and deterministic continuity checks.
- Support specialist agent roles (planner, writer, editor, critic, reader simulator, etc.).
- Manage long-context projects through sharding, summaries, and level‑of‑detail loading.
- Keep a human author in the loop at key decision points.

## 2. Source Repositories Under Review

| Repository | Primary Strength | License Status |
|------------|------------------|----------------|
| lensetek/Fiction-book-agent-skills | Specialist role taxonomy | MIT badge, missing file |
| danjdewhurst/story-skills | Persistent story state, deterministic continuity | MIT |
| haowjy/creative-writing-skills | Writer/critic/editor separation, voice preservation | Apache 2.0 |
| JeroTan/novel-writer-english | Constitution, context reload, document sharding | MIT (translation) |
| wgwtest/novel-writing | Narrative epistemology, POV boundaries, context LOD | MIT |
| rhavekost/author-toolkit | Context-blind reader testing, separate editorial passes | To be confirmed |
| zenstory-ai | Additional inspiration | To be reviewed |

## 3. Proposed Skill Modules

The system will be organized into modular skills. The current tentative list includes:

- `fiction-orchestrator` — central coordinator
- `concept-development` — story idea intake and refinement
- `worldbuilding` — setting, rules, history
- `character-development` — psychology, voice, arcs
- `narrative-architecture` — plot and structure
- `scene-planning` — beat-by-beat outlines
- `scene-writing` — prose drafting
- `continuity` — canon tracking and validation
- `prose-editing` — line editing and polishing
- `reader-simulation` — context-blind beta reading

Additional skills may be added or split as the design matures.

## 4. Persistent Story State

CodexWriter will maintain structured artifacts for the story, including:

- Story Bible / Constitution
- Character state (including knowledge, voice, arcs)
- World facts and rules
- Timeline
- Plot arcs and promises/payoffs
- Scene state
- Continuity records

These will be stored as Markdown and/or structured JSON (schemas to be defined).

## 5. Context Management Strategy

Long projects will be handled through:

- Document sharding (splitting large files)
- Level-of-detail (LOD) loading: full prose near the current scene, summaries for distant material
- Pre-write context reload: only necessary state is loaded before each writing session
- Post-write state updates: ensure the persistent state reflects new developments

## 6. Workflow / Branch Strategy

- `main` — stable, reviewed releases
- `development` — ongoing integration branch
- Feature branches — per task or skill (created from `development`, merged via PR)

## 7. Next Steps

- Complete source analysis documents in `docs/source-analysis/`
- Build the cross-walk table in `docs/crosswalk.md`
- Define skill templates and schemas
- Implement first prototype skills (orchestrator + state manager)

---

*This document will be updated as decisions are made.*
```

#### `ATTRIBUTION.md` (initial template, before PR #1 modifications)

```markdown
# Attribution

CodexWriter draws inspiration from the following open-source fiction‑writing skill repositories.  
No code or skill text has been copied verbatim unless explicitly noted.

| Repository | License | Contribution to CodexWriter |
|------------|---------|------------------------------|
| [lensetek/Fiction-book-agent-skills](https://github.com/lensetek/Fiction-book-agent-skills) | MIT (missing license file) | Specialist role architecture |
| [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills) | MIT | Persistent story state, deterministic continuity |
| [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills) | Apache 2.0 | Writer/critic/editor separation, voice preservation |
| [JeroTan/novel-writer-english](https://github.com/JeroTan/novel-writer-english) | MIT (translation of wordflowlab) | Constitution, context reload, sharding |
| [wgwtest/novel-writing](https://github.com/wgwtest/novel-writing) | MIT | Narrative epistemology, POV boundaries, context LOD |
| [rhavekost/author-toolkit](https://github.com/rhavekost/author-toolkit) | MIT (?) | Context-blind reader testing, separate editorial passes |
| [zenstory-ai](https://github.com/zenstory-ai) | To be reviewed | Additional inspiration |

*License details to be confirmed as source analysis progresses.*
```

#### `templates/SKILL_TEMPLATE.md`

```markdown
# Skill Name

> Replace this line with a short summary of what the skill does and when it should be used.

## Purpose

Describe the specific role or outcome this skill produces.  
Example: “Generates a detailed world bible from a high‑level concept.”

## Inputs

- What context, files, or state does this skill require?
- Example: `story-concept.md`, `worldbuilding.md`, current story state

## Outputs

- What files or artifacts does this skill create or update?
- Example: new chapter draft, updated character state, continuity report

## Dependencies

- Which other skills or schemas does this skill rely on?
- Example: `worldbuilding`, `character-development`, `schema/story-state.schema.json`

## State Updates

- What persistent story state is updated by this skill?
- Example: updates `timeline.md`, adds new scene to `scene-index.md`

## Instructions

Provide clear, step‑by‑step instructions for the agent.  
Use numbered steps, include quality checks, and define any constraints.

1. Load required context and state.
2. Perform the primary task (e.g., draft a scene).
3. Self‑review against the skill’s quality checklist.
4. Update persistent story state.
5. Save outputs to the specified locations.

## Quality Checklist

- [ ] Does the output align with the story bible and current canon?
- [ ] Are all required files created/updated?
- [ ] Are continuity risks flagged or resolved?
- [ ] Is the output formatted according to project conventions?

## Notes

Any additional guidance, edge cases, or examples.
```

#### `docs/crosswalk.md` (initial template, before PR #1 modifications)

```markdown
# Crosswalk: Lensetek Roles → Improvement Sources

> This table is a working planning tool.  
> It maps each Lensetek specialist role to the repository or skill that offers the strongest improvement, and records what to keep, replace, or borrow.

| Lensetek Skill | Best English Analogue | Keep? | Replace? | Borrow Improvements From |
|----------------|------------------------|-------|----------|--------------------------|
| fiction-book-orchestrator | Haowjy Muse / JeroTan methodology | ✓ |  | Haowjy + JeroTan |
| story-concept-intake | JeroTan Specify/Clarify |  | ✓ | JeroTan |
| worldbuilding-architect | danjdewhurst worldbuilding |  |  | danjdewhurst |
| character-designer-psychologist | Haowjy character-sim + JeroTan character-depth |  |  | Haowjy + JeroTan |
| plot-narrative-architect | JeroTan Plan + danjdewhurst plot-structure |  |  | JeroTan + danjdewhurst |
| storyboard-scene-planner | danjdewhurst + wgwtest |  |  | danjdewhurst + wgwtest |
| novel-scene-writer | Haowjy Writer + wgwtest |  | ✓ | Haowjy + wgwtest |
| prose-dialogue-polisher | Haowjy Editor / rhavekost Line Editor |  |  | Haowjy + rhavekost |
| plot-hole-continuity-checker | danjdewhurst revision-continuity + wgwtest |  | ✓ | danjdewhurst + wgwtest |
| beta-reader-critique-simulator | rhavekost fresh reader test |  | ✓ | rhavekost |
| (other Lensetek roles) | … |  |  |  |

## Usage

- Fill in the remaining Lensetek roles after reviewing the source repositories.
- Use this table to guide which parts of each source to adapt, replace, or keep as-is.
- Update the table as design decisions are made.

## Notes

- Lensetek's specialist taxonomy is broad; not all roles may be needed in the initial CodexWriter release.
- Some improvements may come from multiple sources; prioritize the strongest single source for each role.
```

#### `docs/source-analysis/README.md` (initial version, before PR #1 modifications and status updates)

```markdown
# Source Analysis

This folder contains detailed analysis documents for each source repository reviewed during the development of CodexWriter.

## Purpose

Each source repository (Lensetek, story-skills, creative-writing-skills, etc.) will be examined for its architecture, strengths, weaknesses, and licensing status. The analysis will inform the design decisions documented in `ARCHITECTURE.md` and the cross‑walk table in `docs/crosswalk.md`.

## File Format

Each source should have its own Markdown file named after the repository, e.g.:

- `lensetek.md`
- `danjdewhurst-story-skills.md`
- `haowjy-creative-writing-skills.md`
- `jero-tan-novel-writer-english.md`
- `wgwtest-novel-writing.md`
- `rhavekost-author-toolkit.md`
- `zenstory-ai.md`

Each file should include:

- **Repository URL**
- **License** (and any discrepancies, e.g., badge vs. actual file)
- **Overview** (high-level description)
- **Architecture** (key components, agent roles, file structure)
- **Strengths** (what it does well)
- **Weaknesses / Gaps** (what it lacks or does poorly)
- **Relevance to CodexWriter** (what we might adopt or adapt)
- **Detailed Notes** (quotes, specific observations, links to relevant files)

## Status

| Source | Status |
|--------|--------|
| lensetek/Fiction-book-agent-skills | Not started |
| danjdewhurst/story-skills | Not started |
| haowjy/creative-writing-skills | Not started |
| JeroTan/novel-writer-english | Not started |
| wgwtest/novel-writing | Not started |
| rhavekost/author-toolkit | Not started |
| zenstory-ai | Not started |

## Next Steps

- Populate each source analysis file with the details listed above.
- Use the cross‑walk table to map improvements to CodexWriter's planned skills.
- Update `ARCHITECTURE.md` as decisions are made.
```

---

### Files without final code in conversation

- `README.md` – Initial content was provided early, but later edited (source count change, URL links). No complete latest version in conversation.
- `ARCHITECTURE.md`, `ATTRIBUTION.md`, `docs/crosswalk.md`, `docs/source-analysis/README.md` – Were modified in PR #1. The full updated contents are not included in the conversation; only summaries and descriptions are available.
- `docs/architecture-audit.md` – New file from PR #1; full content not provided.
- `docs/source-analysis/lensetek.md` – New file from PR #2; full content not provided.
- `docs/source-analysis/danjdewhurst-story-skills.md` – New file from PR #3; full content not provided.
- `test.md` – Contains write-access verification line; exact final content not fully specified beyond a brief note.

---

## 4. Decisions Made

| Decision | Rationale | Alternatives Considered |
|----------|-----------|--------------------------|
| Use `development` as the active integration branch; keep `main` protected | Enables PR-based review and agent safety | Direct commits to `main` |
| Start with a source-analysis phase before writing skills | Need to understand best practices and licensing before implementation | Immediate translation of Lensetek |
| Treat Lensetek as the baseline taxonomy, not an implementation model | Its 16-role division is strong, but individual skill depth is shallow | Use another repo as baseline (e.g., Haowjy) |
| Keep `continuity` as one skill during Phase 1 | Avoid over-engineering before evidence | Split into `story-state-manager` + `continuity-validator` now |
| Defer the state architecture decision (single JSON vs. distributed Markdown/YAML) | Both Zenstory and Dewhurst offer credible but different models; need comparative analysis first | Adopt Zenstory’s centralized state immediately |
| Use Observed / Inference / Uncertainty labels in all source analyses | Maintain evidentiary rigor and prevent fabrication | Unstructured narrative notes |
| Keep all CodexWriter skill dispositions provisional | Avoid premature commitment | Mark some as final during analysis |
| Initial recommended source order: Lensetek → Dewhurst → Zenstory → Haowjy → JeroTan → wgwtest → Rhavekost | Logical progression from taxonomy → state/continuity → state engine → workflow → craft → editorial | Original order had Zenstory second; changed after evidence review |
| Do not modify `ARCHITECTURE.md` or `docs/crosswalk.md` within source-analysis PRs | Keep source analysis separate from architecture decisions until all sources are reviewed | Modify architecture incrementally with each PR |
| Use feature branches per analysis / architecture change, then PR into `development` | Enable human review and quality control | Direct commits to `development` |

---

## 5. Commands & Environment

### Terminal commands run  
**None** in this conversation. All repository actions were performed via the GitHub web UI or ChatGPT’s GitHub integration. No local terminal commands were executed by the user.

### Environment variables / secrets  
- **GitHub personal access token** – Not created or used.  
- **ChatGPT GitHub app** – Installed and granted access to `davehallmon/CodexWriter`. It has read/write permissions.  
- **Hermes Agent** – Not yet configured or connected. Planned later via GitHub CLI or MCP with a fine-grained token.

### Tool versions  
- ChatGPT (GitHub app) – exact version unknown  
- GitHub – standard web interface  
- No code runtime or dependencies installed

---

## 6. Errors & Fixes

| Error / Issue | Root Cause | Solution / Workaround |
|---------------|------------|------------------------|
| ChatGPT claimed write access but user did not see update to `test.md` | Initially ChatGPT was not actually connected; the assistant (DeepSeek) falsely assumed it had written | Clarified roles: DeepSeek cannot write to GitHub. User then granted ChatGPT proper access, and ChatGPT successfully wrote to `test.md` with commit SHA `97e0a1dcffe50c78637f6b7e7d599edd55f6f3d3` |
| GitHub connector became unavailable during attempts to create `source-analysis/zenstory` | Tool-side issue with ChatGPT’s GitHub integration | ChatGPT stopped without making any writes; user will resume when connector returns |
| Lensetek license file missing | Repository README displays MIT badge, but root `LICENSE` returns 404 | Treat Lensetek as unresolved; do not redistribute derivative content until license confirmed |
| Initial README said “six source repositories” though seven were listed | Oversight during early documentation | Fixed in commit `f4332e04245b6144640be5a1fd729448c5c844e7` |

---

## 7. Open Issues & Risks

- **PR #3 (Dewhurst analysis) is open and unmerged.** Review and merge before proceeding.  
- **GitHub connector for ChatGPT is intermittent.** May need retries or manual verification.  
- **Lensetek license ambiguity.** Cannot safely publish derivative work until resolved.  
- **State architecture undecided.** Must analyze Zenstory and possibly others before choosing between centralized JSON vs. distributed Markdown/YAML.  
- **Continuity skill scope unresolved.** Whether to split into state management vs. validation remains deferred.  
- **Hermes Agent not yet set up.** Second agent integration planned but not started.  
- **Source analyses incomplete.** Remaining repositories: Zenstory, Haowjy, JeroTan, wgwtest, Rhavekost.  
- **Crosswalk / architecture may need further updates** after all sources are analyzed.  
- **Risk of premature architecture commitment** if source analyses are not kept evidence-based and provisional.

---

## 8. Action Items

| Priority | Action | Status | Next Step |
|----------|--------|--------|-----------|
| 1 | Review and merge PR #3 (Dewhurst analysis) | Open | User reviews diff; merge if acceptable |
| 2 | Wait for GitHub connector to be available | Blocked | Retry connection; verify `development` head |
| 3 | Create `source-analysis/zenstory` branch from `development` | Not started | ChatGPT creates branch and analysis doc |
| 4 | Complete Zenstory source analysis (`docs/source-analysis/zenstory-ai.md`) | Not started | Use same evidence labels, focus on state authority, precedence, revision propagation |
| 5 | Continue remaining source analyses in recommended order | Not started | Haowjy, JeroTan, wgwtest, Rhavekost |
| 6 | Synthesize findings to update `ARCHITECTURE.md` and `docs/crosswalk.md` | Not started | After all analyses or when enough evidence gathered |
| 7 | Set up Hermes Agent with local repo access | Not started | Use GitHub CLI or MCP with fine-grained token |
| 8 | Begin drafting first prototype skills (orchestrator, state manager) | Not started | Only after architecture decisions are made |
| 9 | Resolve Lensetek license (contact author or wait for file) | Not started | Needed before public release or derivative reuse |

---

## 9. How to Run / Test

**No runnable code exists yet.** The repository currently contains only documentation and analysis files. There is no build, test, or execution step.

To verify repository integrity and access:

1. Ensure you are on branch `development`:  
   `git checkout development`
2. Pull latest changes:  
   `git pull origin development`
3. List files:  
   `ls -la`
4. Check PR status via GitHub web UI or `gh pr list` (if GitHub CLI is installed).

Expected outcome: All documentation files listed in Section 2 are present. PR #3 may still be open if not merged.

---

## 10. Additional Context

- **Guardrails for all future work:**  
  - Use Observed / Inference / Uncertainty labels.  
  - All CodexWriter dispositions must be provisional.  
  - Do not modify `ARCHITECTURE.md` or `docs/crosswalk.md` within source-analysis PRs.  
  - Keep source order flexible; “Initial Recommended Phase 1 Source Order” is not absolute.  
  - No state architecture decision (single JSON or distributed Markdown/YAML) has been made.  
- **Recommended source order:** Lensetek → Dewhurst → Zenstory → Haowjy → JeroTan → wgwtest → Rhavekost.  
- **Key unresolved questions for Zenstory analysis:**  
  1. Centralized vs. distributed state authority – what does Zenstory actually implement, and what problem does it solve or introduce relative to Dewhurst?  
  2. Authority/precedence rules – how does Zenstory resolve conflicts between artifacts, and does it have a universal precedence rule?  
  3. Revision propagation / stale-write protection – does Zenstory implement transactional updates, revision counters, or replay mechanisms, and what are the observed effects?  
- **Licensing summary:**  
  - Lensetek: MIT claimed, license file missing.  
  - Dewhurst: MIT confirmed.  
  - Haowjy: Apache 2.0.  
  - JeroTan: MIT, with upstream attribution to `wordflowlab/novel-writer-skills`.  
  - wgwtest: MIT.  
  - Rhavekost: MIT.  
  - Zenstory (`oh-story-claudecode`): MIT.  
- The repository is private. Do not expose or redistribute content until licensing is fully resolved, especially for Lensetek.