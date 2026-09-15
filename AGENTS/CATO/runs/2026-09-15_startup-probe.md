# CATO startup probe — 2026-09-15

**Provenance:** a fresh Codex CLI session, launched by the foundation builder with `--model gpt-6-astra`, cwd `AGENTS/CATO`, `--sandbox read-only`, `--ask-for-approval never`, `--ephemeral`, and low reasoning effort for this bounded test. This is a startup test, not an ordinary CATO work session or a maturity grade. The parent saved the returned report here; the child was prohibited from writing.

**Observed result:** CLI exited 0; the event stream ended with `turn.completed`. All recorded tool commands were document reads and Git inspection. The five startup files remained byte-identical to the installed candidates. The probe recovered the role, current authorization, deferred transition and prior L393/L381 limits without the conversation history. It could not independently attest an exact resolved backend model ID; Astra was explicitly requested, with no fallback code in the launcher. The production interactive launch uses workspace-write/on-request; those permission modes were validated with a stub rather than by this read-only probe.

The first attempt was blocked by the parent sandbox’s read-only access to Codex runtime files. The approved retry initialized successfully, while retaining read-only permissions inside the child session.

## Returned report (verbatim)

## Read-only startup verification

**Role and accountability.** I am CATO, Will’s independent reviewer of agent work, reliability and completion, with PROME the first review focus. I answer directly to Will. The [charter](/home/willi/Research-workspace/AGENTS/CATO/CHARTER.md) permits evidence-based review and bounded repairs within assigned scope; this session authorizes inspection only.

**Concrete startup instructions found.**

- Read CHARTER and CONTINUITY, then root CLAUDE, USER and AGENTS; read owner instructions before edits.
- Establish repository root, branch, HEAD, working-tree changes and staged paths. Preserve concurrent work; quiet history does not prove an owner is idle.
- Verify the current request, prior approvals and unresolved conditions through focused task records.
- Give a brief orientation; do not start pending tasks or PROME operational boot/closeout.
- Normally save substantive findings and update continuity, but respect an explicitly read-only review.

I read those documents plus README, the foundation record and two relevant task records. Git showed `master` at `ce78ab9b8d40bee55e7fb6bf34a1e13978eee8cf`, substantial foreign changes, untracked CATO/foundation files, and no staged paths. No pull was appropriate.

**Approved build versus deferred work.** Will approved the first manual foundation: startup instructions, charter, continuity, README and Astra launcher. Fleet registration, automatic routing, registry/launcher integration and the RAV succession transition remain deferred. RAV is not retired; its maturity and old backlog do not transfer automatically.

**Two approvals/limitations to preserve.**

1. **L393:** Will already approved the Owed/reference split; do not request layout approval again. Its record reports implementation, testing and independent local/code review, **not publication**. Preserve the existing private Owed artifact and ruling store. Native hosted verification, private reference URL and WQ-253 coverage remain unresolved.
2. **L381:** Instruction reconciliation was authorized **without changing authority**. Its record reports implementation and independent source verification; two ordinary completed-session observations remain owed. No new scorecard, and L378 mechanization remains separate.

These are documentary receipts, not independently rerun implementation checks in this session.

**Model and context limits.** The documented launcher requests `gpt-6-astra`. Session instructions identify Codex based on GPT-6, but no exact active-model runtime identifier was exposed; Astra execution is therefore unverified. README describes workspace-write/on-request, whereas this session actually has read-only/never permissions. Root’s generic Claude Code wording also differs from CATO’s explicit Codex setup. The foundation record promises verification receipts “below,” but currently ends there.

**Next step.** With no further assignment, offer a bounded review of remaining CATO/RAV integration with Will, then await direction.

No files—including continuity—were edited; no commits, pushes, publication, external messages, scripts or agents were launched.
