# CATO

Will’s independent adviser on system direction, productivity and reliability. CATO helps prioritize useful research, remove bottlenecks and reduce wasted effort, using evidence review and bounded repair to support better outcomes. The [charter](CHARTER.md) defines the direction, execution and return questions used to guide this work. **SPECIAL, manual use (WQ-255):** downstream registration completion and RAV succession remain separate work.

## Start a session

From the repository root:

```bash
bash AGENTS/CATO/launch.sh
```

Or supply one quoted task:

```bash
bash AGENTS/CATO/launch.sh 'Help me direct the current PROME session: recommend the most useful next step and what to finish, defer or stop.'
```

The launcher requests **`gpt-6-astra`**, starts in this directory so Codex finds its AGENTS.md, and uses workspace-write with on-request approvals. Repository access permits authorized repairs; it is not permission to edit arbitrary files. It uses the machine’s existing Codex installation/authentication and does not change global configuration or fall back to another model.

Inspect the command without starting a model or requiring Codex on PATH (the repository, Bash and Git must still be available):

```bash
bash AGENTS/CATO/launch.sh --check
```

Model availability still depends on the installed client/account. Verification evidence and limitations: [foundation record](../../PROME/plans/2026-09-15_CATO-foundation.md).

## Files

| File | Job |
|---|---|
| [AGENTS.md](AGENTS.md) | Startup and closeout entry point |
| [CHARTER.md](CHARTER.md) | Role, authority and report contract |
| [CONTINUITY.md](CONTINUITY.md) | Current assignment, approvals and resume links |
| [Latest continuity archive](CONTINUITY_2026-09-26_ARCHIVE.md) | Verbatim pre-trim September 26 snapshot; past task dispositions and approvals, read on demand |
| [Earlier continuity archive](CONTINUITY_2026-09-21_ARCHIVE.md) | September 21 history; neither archive is a startup read or current assignment |
| `runs/` | On-demand task evidence; one report per continuing task with current disposition and dated follow-ups |

Root operating instructions still apply. RAV’s reports retain their historical authorship; CATO does not inherit its maturity or unverified backlog.

References for launch design: [Codex AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Astra model ID](https://developers.openai.com/api/docs/models/gpt-6-astra). Flags were checked against the installed Codex CLI help.
