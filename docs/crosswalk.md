# Crosswalk: Lensetek Roles → Improvement Sources

> This table is a Phase 1 mapping/planning tool, not a final architecture decision.  
> Lensetek supplies the initial responsibility taxonomy; the seven source analyses will determine what CodexWriter should retain, adapt, merge, split, or omit.  
> Keep architectural rationale, design arguments, and final module definitions in `ARCHITECTURE.md` or `docs/architecture-audit.md`; this file should remain a compact evidence-backed cross-reference.

## Working Crosswalk

| Lensetek Skill | Candidate Layer | Best Current Analogue / Evidence Source | Phase 1 Disposition | Candidate Improvements to Investigate |
|---|---|---|---|---|
| `fiction-book-orchestrator` | Control / coordination | Haowjy muse; JeroTan workflow; Zenstory router | Retain responsibility | Routing, stopping points, runtime fallback, explicit scope transitions |
| `story-concept-intake` | Creative core | JeroTan Specify/Clarify | Retain; naming/boundary undecided | Constitution, clarification markers, non-canonical exploration |
| `fiction-market-trend-analyst` | Optional research extension | Zenstory scan/analyze | Keep as optional extension candidate | Separate trend research from creative canon; provenance for research inputs |
| `worldbuilding-architect` | Creative core | Dewhurst worldbuilding; JeroTan knowledge | Retain | Static canon vs. dynamic world state, reusable system/faction artifacts |
| `character-designer-psychologist` | Creative core | Haowjy character-sim; JeroTan character-depth | Retain | Voice references, knowledge state, relationships, current-state snapshots |
| `plot-narrative-architect` | Creative core | JeroTan Plan; Dewhurst plot-structure | Retain | Promises/payoffs, dependency planning, reveal boundaries, causal spine |
| `storyboard-scene-planner` | Creative core | Dewhurst chapter-writing outline; wgwtest planning | Retain | Entry/exit state, causal beats, scene knowledge/access constraints |
| `novel-scene-writer` | Creative core | Haowjy writer; wgwtest drafting | Retain | Context LOD, style fidelity, pre-write reload, smallest-sufficient context |
| `comic-webtoon-scriptwriter` | Optional adaptation extension | JeroTan comics workflow | Extension candidate | Shared canon with form-specific output adapter |
| `children-story-creator` | Optional audience/form extension | No strong equivalent yet | Extension candidate | Age/audience calibration; avoid forcing into novel core |
| `braille-accessibility-formatter` | Optional accessibility extension | No strong equivalent yet | Extension candidate | Treat accessibility as output/adaptation layer; verify technical standards independently |
| `plot-hole-continuity-checker` | Evaluation / state | Dewhurst revision-continuity + CLI; Zenstory tracking/check; wgwtest review | Keep as one `continuity` skill for Phase 1 | Compare audit vs. state-update ownership before considering any future split |
| `prose-dialogue-polisher` | Evaluation / revision | Haowjy editor; Rhavekost line editor; wgwtest revision | Retain as `prose-editing` | Preserve style-bearing material; separate line-level polish from developmental review |
| `beta-reader-critique-simulator` | Evaluation | Rhavekost fresh reader; Haowjy reader-sim | Retain as `reader-simulation` | Context isolation, experiential reading, explicit stop after report |
| `fiction-layout-exporter` | Optional publishing extension | Dewhurst build/export | Extension candidate | Separate canonical manuscript from disposable build artifacts |
| `fiction-agent-update-manager` | Infrastructure / maintenance | Dewhurst maintenance; Zenstory setup/version/runtime checks | Replace conceptually with broader maintenance capability candidate | Project setup, migration, doctor, capability detection, safe upgrades |

## Candidate Capabilities Not Represented by a Lensetek Role

These are recurring patterns in other repositories and should be evaluated during source analysis without automatically becoming new skills.

| Candidate Capability | Evidence Sources | Question for CodexWriter |
|---|---|---|
| Story constitution / creative contract | JeroTan | Separate artifact/step or part of concept development? |
| Clarification gate | JeroTan | Separate workflow stage or behavior inside concept/planning? |
| Story memory / fact extraction | Haowjy | Distinct cross-cutting skill or responsibility of orchestrator/state layer? |
| Non-canonical work sandbox | Haowjy, JeroTan | How are brainstorms/alternate takes prevented from silently becoming canon? |
| Developmental/story review | Haowjy, Rhavekost, JeroTan | Distinct `story-review` skill or mode inside editing? |
| Context assembly / LOD manager | wgwtest, Zenstory, JeroTan | Distinct capability or shared contract every skill follows? |
| Runtime setup/capability fallback | Zenstory | Infrastructure skill, installer behavior, or orchestrator responsibility? |
| Project maintenance / import / migration / doctor | Dewhurst, Zenstory | One infrastructure skill or CLI/tool layer outside creative skills? |
| Author preference memory | Zenstory, Haowjy style references | How should author preferences remain separate from story canon? |
| Structured finding schema | Rhavekost | Shared contract for critique, continuity, and review outputs? |

## State Architecture Questions

Do **not** choose a canonical storage model from this crosswalk. Each source analysis must first document:

- canonical/static story facts;
- dynamic/current story state;
- authority rules when artifacts disagree;
- update/commit behavior after writing or revision;
- history representation (snapshots, deltas, logs, rewritten state);
- stale/conflicting update behavior;
- treatment of reader knowledge vs. author truth vs. character knowledge;
- author preference/voice memory;
- handling of non-canonical working material.

Zenstory's `_tracking-state.json` + deterministic derived views is one candidate pattern to compare, not the current CodexWriter decision.

## Initial Recommended Source Analysis Order

This is an initial planning sequence only and may be adjusted as earlier source analyses reveal better comparison paths.

1. Lensetek — baseline responsibility taxonomy and workflow gates
2. Dewhurst — persistent state and deterministic continuity comparison
3. Zenstory — transactional state, context filtering, runtime fallback, author memory
4. Haowjy — staffing, story memory, voice, critique/editor separation
5. JeroTan — constitution, clarify, tasks, sharding, review workflow
6. wgwtest — narrative epistemology, context LOD, style fidelity
7. Rhavekost — focused editorial personas, stopping points, fresh-reader isolation

## Usage

- Keep this file concise: map responsibilities, evidence sources, provisional dispositions, and open questions only.
- Update rows only when source-analysis evidence supports the change.
- Prefer `Retain`, `Adapt`, `Merge candidate`, `Extension candidate`, or `Defer` over premature keep/replace binaries.
- Put detailed architectural reasoning in `ARCHITECTURE.md` or `docs/architecture-audit.md`, not here.
- Record implementation-specific borrowing and licensing provenance in the relevant source analysis and `ATTRIBUTION.md` before copying any substantial source material.
