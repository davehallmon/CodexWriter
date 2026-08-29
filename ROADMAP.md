<!-- GENERATED FILE. Edit project/control/*.json, then run scripts/generate_operational_views.py. -->

# CodexWriter Master Framework Roadmap

- Roadmap Version: `1.0.0`
- Status: `human-authorized`
- Approved By: Dave Hallmon
- Approved At: 2026-08-29
- Approval Basis: Repository owner instruction to implement the audited operational-control revisions
- Governing Source Commit: `d6384996c0bc47e38bfb139497a8a57f3c86d12c`
- Amendment Policy: Changes require a pull request, passing governance checks, and repository-owner approval.

## Core Architecture Milestones

### ARCH-01: Architecture and Source Alignment
- Status: `completed`
- Deliverable ARCH-01.1: Ratify the layered authority model and transaction boundaries.
- Deliverable ARCH-01.2: Complete and reconcile the seven source analyses.
- Deliverable ARCH-01.3: Record reusable-core and optional-profile boundaries.
- Exit Criteria: Ratified architecture, source synthesis, crosswalk, and decision records are present and internally aligned.

### CP1A: Deterministic Transaction Spine
- Status: `planned`
- Deliverable CP1A.1: Define a host-neutral transaction contract.
- Deliverable CP1A.2: Implement schema-level validation for governed canon state.
- Deliverable CP1A.3: Add append-only provenance and audit records.
- Deliverable CP1A.4: Rebuild derived views transactionally.
- Deliverable CP1A.5: Prove the spine with fixtures, tests, and continuous integration.
- Exit Criteria: A generic state transition is rejected on stale revision, validated before promotion, audited, and reproduced from fixtures in CI.

### CP1B: Context Assembly and Derived Views
- Status: `planned`
- Deliverable CP1B.1: Build provenance-aware context assembly.
- Deliverable CP1B.2: Separate narrative, structured state, author memory, and derived views.
- Deliverable CP1B.3: Verify deterministic invariants on a second host.
- Exit Criteria: Context packages identify their sources and can be rebuilt without introducing unique facts.

### CP2: Specialist Orchestration Vertical Slice
- Status: `planned`
- Deliverable CP2.1: Align specialist skill contracts with the ratified authority model.
- Deliverable CP2.2: Run a two-phase generic fiction workflow through the deterministic spine.
- Deliverable CP2.3: Demonstrate context-blind reader simulation and governed editorial approval.
- Exit Criteria: The vertical slice executes through two specialist phases with validated state, explicit human gates, and reproducible evidence.

### PROFILE-01: Optional Dust and Ash Profile
- Status: `deferred`
- Deliverable PROFILE-01.1: Extract project-specific Biblical, ANE, stylistic, and research material from the reusable core.
- Deliverable PROFILE-01.2: Declare profile activation and contamination-review rules.
- Exit Criteria: The reusable framework operates without the profile and profile activation introduces only declared extensions.
