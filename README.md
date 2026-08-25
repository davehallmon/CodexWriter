# CodexWriter

**Status:** Early development — private repository.  
**License:** TBD (pending source license verification).  
**Branch:** `development`

CodexWriter is an AI-assisted fiction authoring framework. It is the result of a deep analysis of several open-source “fiction skill” repositories, most notably:

- [`lensetek/Fiction-book-agent-skills`](https://github.com/lensetek/Fiction-book-agent-skills) — specialist role architecture
- [`danjdewhurst/story-skills`](https://github.com/danjdewhurst/story-skills) — persistent story state & deterministic continuity
- [`haowjy/creative-writing-skills`](https://github.com/haowjy/creative-writing-skills) — writer/critic/editor separation, voice preservation
- [`JeroTan/novel-writer-english`](https://github.com/JeroTan/novel-writer-english) — constitution, pre-write context reload, document sharding
- [`wgwtest/novel-writing`](https://github.com/wgwtest/novel-writing) — narrative epistemology, POV boundaries, context LOD
- [`rhavekost/author-toolkit`](https://github.com/rhavekost/author-toolkit) — context-blind reader testing, separate editorial passes
- [`zenstory-ai`](https://github.com/zenstory-ai) — additional inspiration; to be analyzed and incorporated

Rather than simply translating or copying any single repository, CodexWriter aims to synthesize the best architectural ideas from each into a new, more robust system.

## CORE PRINCIPLES 

- **Specialist agents over monolithic prompts** — different cognitive tasks (planning, worldbuilding, drafting, critiquing, continuity) are handled by dedicated skills with clear boundaries.
- **Persistent, checkable story state** — characters, timelines, plot arcs, promises/payoffs, and world facts are stored as structured artifacts and updated after each writing session.
- **Deterministic continuity validation** — where possible, continuity is checked against schemas and scripts, not just free‑form reasoning.
- **Context management by design** — large projects are sharded, summarized, and selectively loaded using level‑of‑detail (LOD) strategies to avoid exhausting the model’s context window.
- **Human‑in‑the‑loop gates** — at key stages (concept approval, outline, draft, final review), a human author remains the final decision‑maker.
- **Modular and version‑controlled** — each skill lives in its own directory with a `SKILL.md`, supporting schemas, and tests. The entire system can evolve without breaking the whole.

## TBD PLANNED STRUCTURE
```text
codexwriter/
├── README.md
├── ATTRIBUTION.md          # credits for source inspirations
├── ARCHITECTURE.md         # design decisions and cross‑walk
├── docs/
│   ├── source-analysis/    # detailed notes on each reviewed repo
│   │   ├── lensetek.md
│   │   ├── danjdewhurst-story-skills.md
│   │   ├── haowjy-creative-writing-skills.md
│   │   ├── jero-tan-novel-writer-english.md
│   │   ├── wgwtest-novel-writing.md
│   │   ├── rhavekost-author-toolkit.md
│   │   └── zenstory-ai.md   # to be added
│   ├── crosswalk.md        # mapping of Lensetek roles to improvements
│   └── design-decisions.md
├── skills/
│   ├── fiction-orchestrator/
│   ├── concept-development/
│   ├── worldbuilding/
│   ├── character-development/
│   ├── narrative-architecture/
│   ├── scene-planning/
│   ├── scene-writing/
│   ├── continuity/
│   ├── prose-editing/
│   ├── reader-simulation/
│   └── ...                 # additional specialists as needed
├── schemas/
│   ├── story-state.schema.json
│   ├── character-state.schema.json
│   ├── scene-state.schema.json
│   └── continuity.schema.json
├── templates/
│   ├── story-bible-template.md
│   ├── scene-template.md
│   └── tracking-file-template.md
└── tests/
    ├── continuity/
    ├── skill-smoke-tests/
    └── evaluation-prompts/
```

## CURRENT PHASE

We are in **Phase 1: Architecture & Source Preservation**.  
No skills have been copied verbatim. We are:

1. Documenting the six source repositories in detail.
2. Building a cross‑walk table to decide what to keep, replace, or improve.
3. Resolving licensing status (Lensetek’s MIT license file is currently missing).
4. Drafting original skill specifications that incorporate the best ideas.

Until licensing is clarified, this repository will remain **private** and will not redistribute any derivative content from ambiguous sources.

## Next steps

- Set up the initial `development` branch and file structure.
- Populate `docs/source-analysis` with notes from the six repositories.
- Define the target architecture and cross‑walk.
- Begin drafting the first original skills (orchestrator, story‑state manager, continuity checker).

---

*CodexWriter is a working name and may change before public release.*
