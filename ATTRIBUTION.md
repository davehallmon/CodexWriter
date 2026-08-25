# Attribution

CodexWriter draws architectural inspiration from the following open-source fiction-writing skill repositories.  
No code or skill text has been copied verbatim unless explicitly noted in a future source analysis or provenance record.

| Repository | License / Provenance | Current Contribution Under Study |
|------------|----------------------|----------------------------------|
| [lensetek/Fiction-book-agent-skills](https://github.com/lensetek/Fiction-book-agent-skills) | README advertises MIT and links to a root `LICENSE`, but that file currently returns 404 | Specialist role taxonomy, HITL workflow breadth, publishing/adaptation responsibilities |
| [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills) | [MIT LICENSE](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE) | Persistent story state, deterministic continuity, project maintenance/CI |
| [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills) | [Apache 2.0 LICENSE](https://github.com/haowjy/creative-writing-skills/blob/main/LICENSE); no root NOTICE found in Phase 1 audit | Writer/critic/editor separation, voice preservation, story memory, knowledge/work separation |
| [JeroTan/novel-writer-english](https://github.com/JeroTan/novel-writer-english) | [MIT LICENSE](https://github.com/JeroTan/novel-writer-english/blob/main/LICENSE); [ATTRIBUTION.md](https://github.com/JeroTan/novel-writer-english/blob/main/ATTRIBUTION.md) identifies upstream `wordflowlab/novel-writer-skills` | Constitution, clarification, pre-write context reload, sharding, QA workflow |
| [wgwtest/novel-writing](https://github.com/wgwtest/novel-writing) | [MIT LICENSE](https://github.com/wgwtest/novel-writing/blob/main/LICENSE) | Narrative epistemology, POV/agency boundaries, context LOD, style fidelity |
| [rhavekost/author-toolkit](https://github.com/rhavekost/author-toolkit) | [MIT LICENSE](https://github.com/rhavekost/author-toolkit/blob/main/LICENSE); [ATTRIBUTION.md](https://github.com/rhavekost/author-toolkit/blob/main/ATTRIBUTION.md) tracks separately licensed vendored material | Context-blind reader testing, focused editorial passes, explicit stopping points |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | [MIT LICENSE](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/LICENSE); no root NOTICE or ATTRIBUTION file found in Phase 1 audit | Layered state candidate, transaction semantics, context filtering, runtime fallback, author memory |

## Provenance Policy for Phase 1

- Architectural ideas may be compared and independently reimplemented, but implementation-level copying must be recorded explicitly.
- Each source analysis must link the repository's LICENSE and any NOTICE/ATTRIBUTION files and identify upstream lineage.
- JeroTan must be treated as a derivative lineage: attribution should preserve both the English re-architecture and its identified upstream source when borrowing implementation-level material.
- Rhavekost vendors third-party material; any borrowing from a vendored component must follow that component's own license and provenance rather than assuming the repository's root MIT license is sufficient.
- Haowjy is Apache 2.0 and therefore requires separate redistribution/modification review if substantial source material is reused.
- Lensetek remains unresolved for public derivative redistribution until its advertised license is actually available or permission is otherwise clarified.

See `docs/architecture-audit.md` and the individual source analyses for detailed evidence.

*License status must be rechecked before any public release. This file is a research/provenance record, not legal advice.*
