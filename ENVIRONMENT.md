<!-- GENERATED FILE. Edit project/control/*.json, then run scripts/generate_operational_views.py. -->

# CodexWriter Host Environment Configuration

- Document Version: `1.0.0`
- Owner: Dave Hallmon
- Ownership: Human-owned and version-controlled. Agents may propose changes only through a human-reviewed pull request.
- Last Verified: 2026-08-28

## 1. Operating Governance
- Operating Model: Asymmetric LLM-as-a-Judge generation-verification workflow
- Human Authority: The repository owner approves consequential architecture, merge, release, and environment changes.
- Drift Policy: Update the snapshot through a human-reviewed pull request when material host, toolchain, model, limit, or responsibility boundaries change.

## 2. Connected AI Agents
### Hermes — Worker
- Role: Execute bounded repository work and return evidence
- Repository Access: Local write access when explicitly authorized

### ChatGPT-5 Sol — Judge
- Role: Independently inspect evidence, assess architecture, and issue verdicts
- Repository Access: Connector capability does not authorize implementation unless the repository owner explicitly requests it

## 3. Hardware & OS Profile
- Hardware: Chromebook
- OS: ChromeOS Stable
- Linux Subsystem: Crostini / Debian GNU/Linux 13 (trixie)
- Architecture: x86_64
- Memory: Approximately 13 GiB visible to Linux; no guest swap
- Workspace: /home/davehallmon/CodexWriter
- Shell: Bash

## 4. Integrated Tooling Stack
- Version Control: Git and GitHub
- Python: 3.13.5
- Node: 26.7.0
- Git: 2.47.3
- Docker: not installed

## 5. Hermes Execution Limits
- Max Agent Steps: 100
- Subagent Turn Limit: 80
- Parallel Subagents: 3
- Subagent Timeout Seconds: 900
- Command Timeout Seconds: 600
- Context Window: automatic
- Compression Threshold: 0.75
- Compression Target: 0.45
- Keep Awake: True

## 6. Browser Baseline
- Memory Saver: Balanced
- Experimental Flags: No user overrides

## 7. Security and Data Handling
- Never commit credentials, tokens, private transcripts, or unrelated personal files.
- Treat technical access as capability, not authorization.
- Verify live repository and environment state before consequential work.
- Use placeholders for credentials in documentation.
