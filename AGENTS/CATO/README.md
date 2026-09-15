# CATO

Will’s independent reviewer of agent work, system reliability and completion. **First foundation: manual use.** Fleet registration and the RAV transition are still separate work.

## Start a session

From the repository root:

```bash
bash AGENTS/CATO/launch.sh
```

Or supply one quoted task:

```bash
bash AGENTS/CATO/launch.sh 'Review the current L333 trial evidence; report gaps before changing anything.'
```

The launcher requests **`gpt-6-astra`**, starts in this directory so Codex finds its AGENTS.md, and uses workspace-write with on-request approvals. Repository access permits authorized repairs; it is not permission to edit arbitrary files. It uses the machine’s existing Codex installation/authentication and does not change global configuration or fall back to another model.

Inspect the command without starting a model:

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
| `runs/` | Dated task findings; create a report when substantive work occurs |

Root operating instructions still apply. RAV’s reports retain their historical authorship; CATO does not inherit its maturity or unverified backlog.

References for launch design: [Codex AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Astra model ID](https://developers.openai.com/api/docs/models/gpt-6-astra). Flags were checked against the installed Codex CLI help.
