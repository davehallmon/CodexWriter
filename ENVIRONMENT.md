# ENVIRONMENT.md

**Status:** Active execution-environment reference  
**Last updated:** 2026-08-28  
**Primary local host:** User Chromebook / ChromeOS / Crostini  
**Primary worker:** Hermes Desktop  
**Primary judge:** ChatGPT-5 Sol  
**Operating model:** Asymmetric LLM-as-a-Judge generation-verification workflow

---

## 1. Purpose

This file documents the technical execution environment used for AI-assisted
development work.

It exists so that any LLM, agent, reviewer, or future development session can
understand:

- what hardware and software are available;
- where project files and commands execute;
- which capabilities belong to Hermes versus ChatGPT;
- how local and cloud model inference are divided;
- what resource constraints should influence agent behavior;
- how the Hermes/ChatGPT LLM-as-a-Judge workflow operates;
- what evidence must be produced before work is considered verified; and
- which environmental assumptions must never be treated as architectural facts.

This file describes the **execution environment and operating protocol**.

It does NOT independently define or modify:

- application architecture;
- schema authority;
- product requirements;
- project scope;
- implementation priorities;
- ratified design decisions; or
- authorization to modify, merge, release, or deploy project code.

---

# 2. Authority and Instruction Precedence

When instructions conflict, use the following precedence:

1. **Current explicit user instruction**
2. **Ratified project architecture and decision records**
3. **Current approved implementation or planning artifact**
4. **Current Judge instruction/task packet**
5. **This `ENVIRONMENT.md`**
6. **Worker defaults, model assumptions, or inferred conventions**

`ENVIRONMENT.md` provides environmental context. It must never be interpreted
as permission to perform work that has not otherwise been authorized.

Live repository and system state must also be verified before consequential
operations. A value documented here is a baseline, not a substitute for
checking the actual machine or repository.

---

# 3. AI Operating Architecture

The environment uses an asymmetric **LLM-as-a-Judge** workflow.

```text
                         USER
                          │
                  final human authority
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      CHATGPT-5 SOL                  HERMES
          JUDGE                      WORKER
             │                         │
             │ evaluate                │ execute
             │ challenge               │ inspect
             │ verify                  │ edit
             │ constrain               │ test
             │                         │ commit/push
             │                         │
             └──── evidence/result ────┘
                          │
                   correction loop
                          │
                          ▼
                        USER
````

The two systems have deliberately different responsibilities.

This separation is a feature, not duplication.

---

# 4. Role: Hermes — Worker

## 4.1 Primary responsibility

Hermes is the **execution worker**.

Its role is to perform bounded technical work against the local development
environment and return evidence to the Judge.

Typical responsibilities include:

* inspect files and repository state;
* read source material;
* execute shell commands;
* run Git operations;
* create or modify files when authorized;
* run validation and tests;
* create branches;
* produce commits;
* push authorized branches;
* inspect command/test failures;
* collect system evidence;
* delegate independent subtasks to bounded subagents; and
* return a structured delivery report.

Hermes must not treat its own successful execution as equivalent to independent
verification.

---

## 4.2 Hermes execution topology

Hermes Desktop runs on the user's Chromebook and uses:

```text
Hermes Desktop
    │
    ├── Local Hermes Gateway
    │
    └── Crostini / Linux
            │
            ├── local filesystem
            ├── project repository
            ├── shell
            ├── Git
            ├── Python
            ├── Node.js
            └── compiler/toolchain
```

The **agent runtime is local**, but the configured large-language-model
inference is primarily remote/provider-hosted.

Do not confuse:

> local agent execution

with:

> local LLM inference.

The Chromebook is primarily performing orchestration, filesystem work,
process execution, networking, browser/UI rendering, and context handling.

---

# 5. Hermes Model Configuration

## 5.1 Main model

Configured main provider/model:

```text
Provider: Nous Portal
Model: upstage/solar-pro4:free
Reasoning: Medium
```

The exact provider/model may change over time. Verify live settings when model
identity materially affects a task.

---

## 5.2 Mixture of Agents

Hermes has a Mixture-of-Agents configuration available.

Current baseline:

```text
Mixture of Agents: Enabled

Reference 1
  Provider: openai-codex
  Model: gpt-5.5

Reference 2
  Provider: openrouter
  Model: deepseek/deepseek-v4-pro

Aggregator
  Provider: openrouter
  Model: anthropic/claude-opus-4.8
```

These models are part of **Hermes' internal worker-side reasoning stack**.

They are NOT the same thing as the independent ChatGPT Judge.

A Hermes Mixture-of-Agents consensus therefore does not constitute independent
LLM-as-a-Judge verification.

---

## 5.3 Model context sizing

```text
Context Window: 0 / Automatic
```

`0` instructs Hermes to use the selected model's detected context capacity.

Do not manually inflate this value without a demonstrated need.

Larger nominal context windows can increase latency, provider cost, memory
pressure, context pollution, and retrieval failure without improving reasoning.

---

# 6. Hermes Context and Memory Configuration

Baseline optimized configuration:

```text
Persistent Memory:       ON
User Profile:            ON

Memory Budget:           2200
Profile Budget:          1375
Memory Provider:         Built-in only

Context Engine:          Compressor
Auto-Compression:        ON

Compression Threshold:   0.75
Compression Target:      0.45
```

Interpretation:

* Hermes should preserve full conversational context until approximately 75%
  of the usable context budget is reached.
* When compression occurs, the target retains substantially more working state
  than the previous aggressive configuration.
* Compression is intended to reduce old conversational bulk while preserving
  recent operational state and critical project facts.

For technical work, especially Git and architecture tasks, prefer explicit
artifacts over conversational memory for:

* commit SHAs;
* branch names;
* approved decisions;
* filenames;
* test expectations;
* exceptions;
* constraints; and
* authority boundaries.

Do not rely on compressed conversational memory as the sole record of an
important decision.

---

# 7. Hermes Agent and Execution Limits

Optimized worker configuration:

```text
Max Agent Steps:         100
Subagent Turn Limit:      80
Parallel Subagents:        3
Subagent Timeout:        900 seconds
Command Timeout:         600 seconds
API Retries:               3

Execution Backend:       Local
Code Execution Mode:     Project
Persistent Shell:        ON
Keep Computer Awake:     ON
Tool-Use Enforcement:    Auto
```

Additional unchanged limits:

```text
File Read Limit:         100000 characters/request
File Page Limit:         2000
Line Length Limit:       2000
Checkpoint Limit:        20
```

---

## 7.1 Parallelism rule

Three parallel subagents is the normal maximum.

This is a **ceiling, not a target**.

Use fewer workers when tasks are dependent.

Examples:

Good parallelism:

```text
Agent A -> inspect schema family
Agent B -> inspect tests
Agent C -> inspect documentation
```

Bad parallelism:

```text
Agent A -> modify state
Agent B -> modify state dependent on A
Agent C -> validate state before A/B finish
```

Dependent state-changing work should normally execute serially.

---

## 7.2 Loop control

The 100-step global limit, 80-turn subagent limit, and 900-second subagent
timeout exist to prevent:

* uncontrolled investigation;
* repeated file reads;
* retry loops;
* provider stalls;
* recursive delegation;
* redundant verification; and
* agents continuing long after useful evidence has been obtained.

A worker approaching a limit should report the blocker rather than silently
spawn another path around the constraint.

---

# 8. Hermes Workspace

Primary project workspace:

```text
/home/davehallmon/CodexWriter
```

Baseline configuration:

```text
Working Directory:
  /home/davehallmon/CodexWriter

Automatic Repository Discovery:
  ON

Repository Discovery Root:
  /home/davehallmon/CodexWriter

Code Execution Mode:
  Project

Persistent Shell:
  ON
```

Repository discovery is intentionally scoped.

Do not recursively scan the user's entire home directory unless a task
explicitly requires it.

Private logs, unrelated projects, personal files, caches, and historical
artifacts outside the project root should not be treated as project context.

---

# 9. Role: ChatGPT-5 Sol — Judge

## 9.1 Project designation

`ChatGPT-5 Sol` is the project designation for the independent Judge role.

The underlying ChatGPT model may be upgraded over time without changing the
governance model described here.

The **role is architectural; the exact model version is operational metadata**.

---

## 9.2 Primary responsibility

The Judge evaluates the worker's output rather than merely extending it.

Primary responsibilities include:

* inspect Hermes' claims;
* check architectural compliance;
* identify unsupported assumptions;
* detect scope drift;
* challenge weak reasoning;
* compare implementation against ratified decisions;
* evaluate Git discipline;
* evaluate test sufficiency;
* identify missing evidence;
* distinguish execution from assertion;
* assign a verdict;
* determine the next authorized action; and
* generate corrective task prompts for Hermes when required.

The Judge should behave as an independent verifier, not as Hermes' co-author.

---

## 9.3 Default Judge restrictions

Unless the user explicitly changes the operating mode, the Judge should NOT:

* silently take over Hermes' worker role;
* treat Hermes' narrative report as proof;
* assume unpushed local state exists remotely;
* infer command success from intent;
* infer file contents that were not inspected;
* ratify its own proposed architecture;
* merge merely because a worker says a branch is ready;
* broaden scope to "help" without authorization; or
* convert an evaluation task into an implementation task.

The Judge may independently inspect available evidence and, when available,
remote GitHub state.

Remote repository visibility does **not** provide visibility into:

* uncommitted local changes;
* untracked files;
* local process state;
* Crostini memory usage;
* unsaved editor buffers; or
* local branches that have not been pushed.

Those require Hermes/local evidence.

---

# 10. LLM-as-a-Judge Operating Protocol

The normal cycle is:

```text
1. AUTHORIZE
      User/Judge defines a bounded task.

2. EXECUTE
      Hermes performs the authorized work.

3. EVIDENCE
      Hermes returns execution evidence.

4. JUDGE
      ChatGPT evaluates both result and process.

5. VERDICT
      PASS / CONDITIONAL PASS / FAIL

6. CORRECT
      If required, Judge provides a bounded corrective prompt.

7. RE-EXECUTE
      Hermes performs only the corrective work.

8. RE-VERIFY
      Judge evaluates new evidence.

9. HUMAN GATE
      User authorizes major transition, merge, ratification, or next phase.
```

Neither AI independently replaces the human authority layer.

---

# 11. Required Hermes Evidence Packet

For repository-changing work, Hermes should return enough information for the
Judge to reproduce the reasoning about what happened.

Minimum delivery packet:

```markdown
## Delivery Evidence

### Task
- Objective:
- Authorized scope:

### Repository
- Repository:
- Working branch:
- Expected base SHA:
- Verified base SHA:
- Local HEAD:
- Remote HEAD:

### Changed Paths
- Added:
- Modified:
- Deleted:

### Execution
- Commands run:
- Exit statuses:
- Tools/scripts used:

### Verification
- Tests run:
- Test results:
- Linters/validators:
- `git diff --check`:
- Working-tree status:
- Local/remote HEAD match:

### Exceptions
- Known warnings:
- Inherited defects:
- Unresolved issues:
- Assumptions:

### Scope Confirmation
- Work outside authorized scope: NONE / describe
- Architecture changed: YES / NO
- User decision required: YES / NO
```

Exact requirements may be strengthened by the task-specific Judge prompt.

---

# 12. Judge Verdict Standard

The Judge should evaluate at least:

### Correctness

Did the worker produce the intended result?

### Evidence

Can the result be demonstrated rather than merely asserted?

### Scope discipline

Were only authorized paths and responsibilities touched?

### Architecture conformance

Does the result comply with ratified architecture and decision records?

### Repository discipline

Are ancestry, branch, commits, remote state, and changed paths correct?

### Verification quality

Were appropriate tests/checks actually executed?

### Failure honesty

Were warnings, inherited defects, and uncertainty accurately reported?

### Side effects

Did the worker create unrequested changes, files, branches, dependencies, or
configuration?

Recommended verdict vocabulary:

```text
PASS
PASS WITH CONDITIONS
FAIL — CORRECTION REQUIRED
BLOCKED — USER DECISION REQUIRED
```

A verbose delivery report is not evidence of correctness.

---

# 13. User Chromebook

## 13.1 Host platform

Baseline host:

```text
Platform:          Chromebook
Operating System:  ChromeOS
Channel:           Stable
ChromeOS Release:  16667.62.0
Chrome Milestone:  149
Chrome Version:    149.0.7827.238
Architecture:      x86_64
CPU:               Intel Core Ultra 5 115U
Logical CPUs:      10
```

Board/platform identifiers observed:

```text
ChromeOS board:    rex
Platform model:    screebo
```

These identifiers are useful when diagnosing ChromeOS/Crostini-specific
behavior but normally have no application-level architectural significance.

---

# 14. Crostini / Linux Environment

Baseline Linux guest:

```text
Environment:       ChromeOS Crostini
Distribution:      Debian GNU/Linux 13 (trixie)
Architecture:      x86_64
Kernel:            Linux 6.6.x
Virtualization:    crosvm
```

Observed Linux resource envelope:

```text
RAM visible to Linux:  ~13 GiB
Swap:                  0 B
Linux filesystem:      50 GB
Observed free space:   ~26 GB
```

The absence of guest swap and the finite Crostini memory envelope are important
when designing agent concurrency.

This environment should be treated as **memory-sensitive**.

---

# 15. Installed Local Development Tools

Baseline observed toolchain:

```text
Python:      3.13.5
Node.js:     v26.7.0
Git:         2.47.3
GCC:         14.2.0
G++:         14.2.0
Docker:      NOT INSTALLED
```

Do not assume Docker is available.

If a task requires an unlisted dependency, verify availability before designing
the workflow around it.

Do not install system-wide packages merely because they are convenient unless
the task authorizes environment modification.

---

# 16. Graphics and Browser Environment

The Chromebook's Intel integrated graphics stack is hardware accelerated.

Observed Chrome acceleration includes:

```text
Canvas:             Hardware accelerated
Compositing:        Hardware accelerated
Rasterization:      Hardware accelerated
Multiple raster:    Enabled
OpenGL:             Enabled
Vulkan:             Enabled
WebGL:              Hardware accelerated
WebGPU:             Hardware accelerated
Video Decode:       Hardware accelerated
Video Encode:       Hardware accelerated
```

Chrome uses the Intel graphics stack through ANGLE/Vulkan.

This does NOT mean Hermes' configured LLM inference executes on the local GPU.

The configured Hermes models are provider-hosted.

Therefore:

> Do not diagnose remote LLM token-generation latency as a local GPU problem
> without specific evidence.

---

# 17. Chrome Performance Baseline

Expected browser configuration:

```text
Chrome Memory Saver:   ON
Memory Saver Mode:     Balanced
Experimental flags:    DEFAULT / no user overrides
```

Do not enable experimental GPU, Vulkan, rasterization, Graphite, WebGPU,
scheduler, or networking flags as a generic performance optimization.

The existing hardware-accelerated browser path is functioning.

Experimental Chrome flags require a specific demonstrated problem and an
explicit reason.

---

# 18. Performance Characteristics

The environment is best understood as:

```text
CPU:          capable
GPU:          capable, but not performing configured cloud LLM inference
RAM:          primary local constraint
Disk:         adequate
Network:      important because model inference is remote
Context:      important because repository tasks are information-heavy
Concurrency: deliberately bounded
```

The common workload is not large local-model inference.

It is:

* filesystem inspection;
* Git operations;
* Markdown/JSON processing;
* source comparison;
* repository analysis;
* remote model calls;
* context assembly;
* subagent orchestration;
* test execution; and
* verification.

Optimize for **reliable throughput and context fidelity**, not maximum agent
count.

---

# 19. Context Discipline for Repository Work

Prefer:

```text
specific task
    ↓
specific files
    ↓
minimum sufficient context
    ↓
bounded worker/subagents
    ↓
artifact/result
```

Avoid:

```text
whole repository
+ entire conversation history
+ unrelated logs
+ every architecture document
+ maximum parallel agents
→ one giant prompt
```

For long-running projects:

* materialize important decisions in files;
* reference exact filenames;
* reference exact commit SHAs;
* use summaries as navigation, not authority;
* reload authoritative artifacts when accuracy matters;
* isolate unrelated tasks; and
* avoid forcing historical transcripts into every agent context.

---

# 20. Resource-Aware Agent Guidance

Because Crostini has a constrained memory envelope:

1. Do not exceed three parallel Hermes subagents by default.
2. Prefer one agent for state-changing work.
3. Parallelize independent inspection more readily than mutation.
4. Terminate agents that have completed their evidence-gathering responsibility.
5. Do not repeatedly load very large files unless necessary.
6. Avoid redundant repository-wide searches.
7. Reuse verified results when their underlying state has not changed.
8. Allow commands up to the configured 600-second timeout before treating them
   as failed.
9. Report a stalled provider or command rather than recursively retrying it.
10. Use remote model diversity selectively; more models are not automatically
    better verification.

---

# 21. Security and Data Handling

Default assumptions:

* Never expose API keys or access tokens in prompts, commits, reports, or logs.
* Never commit credentials.
* Hermes secret redaction should remain enabled.
* Treat private user files outside the repository as out of scope unless
  explicitly authorized.
* Do not copy private development transcripts into a public repository.
* Do not assume a local/private URL is safe to transmit to remote providers.
* Review generated files for accidental secrets before commit or push.
* Use placeholders for credentials in documentation.

The existence of technical access does not imply authorization to use it.

---

# 22. Repository-State Rule

No LLM should infer repository state solely from this file.

Before meaningful development work, verify live state.

Recommended minimum:

```bash
cd /home/davehallmon/CodexWriter

git status --short
git branch --show-current
git rev-parse HEAD
git remote -v
git fetch --prune origin
```

For a task with a required base:

```bash
git rev-parse HEAD
git rev-parse <expected-base>
git merge-base HEAD <expected-base>
```

Use task-specific requirements where they are stricter.

---

# 23. System Preflight

When performance or environment state matters, Hermes can collect:

```bash
echo "=== OS ==="
cat /etc/os-release

echo "=== KERNEL ==="
uname -a

echo "=== CPU ==="
lscpu | grep -E 'Architecture|CPU\(s\)|Model name'

echo "=== MEMORY ==="
free -h

echo "=== DISK ==="
df -h /

echo "=== TOOLCHAIN ==="
python3 --version
node --version
git --version
gcc --version | head -1
g++ --version | head -1
```

Do not run extensive diagnostics on every task.

Use them when:

* performance changes unexpectedly;
* the environment has restarted or changed;
* dependencies are relevant;
* resource exhaustion is suspected; or
* the Judge specifically requests environmental evidence.

---

# 24. Known Constraints

Current known environmental constraints include:

### Crostini memory

Linux has approximately 13 GiB available to the guest and no guest swap.

Large parallel contexts can therefore create memory pressure.

### Remote inference latency

Hermes' configured LLMs are remote.

Latency can be influenced by:

* provider load;
* network conditions;
* model availability;
* rate limits;
* large prompts;
* Mixture-of-Agents fan-out; and
* retries.

### Provider dependency

A provider outage can impair an otherwise healthy local Hermes installation.

### No Docker baseline

Docker is not installed and must not be assumed.

### Context compression

Long Hermes sessions may compress historical conversation.

Critical operational facts should therefore be preserved in durable project
artifacts.

### Judge/local visibility boundary

The Judge cannot infer unpushed or uncommitted local state without evidence
from Hermes.

---

# 25. Environment Drift

This file represents a known-good baseline, not immutable truth.

Update it when any of the following materially changes:

* Chromebook hardware;
* ChromeOS version;
* Crostini distribution;
* Crostini resource allocation;
* primary project path;
* Hermes execution backend;
* Hermes concurrency limits;
* Hermes context-management strategy;
* principal worker model/provider;
* Mixture-of-Agents configuration;
* local development toolchain;
* browser performance strategy; or
* LLM-as-a-Judge responsibility boundary.

Minor package updates do not require a documentation update unless they affect
project execution.

---

# 26. Core Operating Principle

The environment deliberately separates **generation from verification**.

Hermes should optimize for:

> execution, evidence, and disciplined scope.

ChatGPT-5 Sol should optimize for:

> independent criticism, architectural fidelity, and verification.

The Judge should not trust the Worker merely because the Worker is confident.

The Worker should not optimize its report to persuade the Judge.

Both should optimize for evidence that allows the user's intended project state
to be established with high confidence.

The USER remains the final authority for consequential project decisions.


