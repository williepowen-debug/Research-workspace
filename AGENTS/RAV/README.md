# RAV — deep factual/analytical reviewer + bounded repair

**⚠️ RAV does not boot from this directory.** RAV runs on **Codex, Will-driven, on-demand** — it is not a Claude Code session, so it loads no `CLAUDE.md` and must be **handed its context** at spawn. That is why this directory holds no agent instructions: there is nothing here for a harness to auto-load.

**Spec — hand these to the Codex session:** `AGENTS/DAEDALUS/builds/RAV_CHARTER.md` — §3 (the repair/flag split), §5 (the run-report contract), §8 (first-run checklist). RATIFIED as-drafted by Will 2026-08-02.

| Surface | What it holds |
|---|---|
| `runs/` | One run report per run: `YYYY-MM-DD_<slug>.md`, contract in charter §5. Append-only history — never rewritten |
| `inbox/` | Inbound to RAV: YEYOU `⚪ NEEDS-VERIFY` escalations, owner replies, Will/PROME asks. **Everything present is unprocessed by definition** — charter §8 step 1 makes reading it part of every run |
| `outbox/` | Outbound copies of fence-(b) inbox notes and reports routed onward |

**Where dispositions live:** `PROME/codex/RAV_QC_LEDGER.md` — RAV writes findings, PROME writes dispositions back. `runs/` is what RAV found; the ledger is what the fleet did about it. A flag with no ledger row has not been dispositioned, only recorded.

**Registration state:** ROSTER § SPECIAL (2026-08-02, Meta per PAT-027) · `AGENTS/WALTER/REGISTRY.tsv` row 18 (Tier-2 cadence label + fences a/b/c) · `AGENTS/DAEDALUS/FLEET_MAP.tsv` (2026-08-03). Root `CLAUDE.md` / `AGENTS.md` / `_INDEX.md` / `_SYNTHESIS_OPS.md` lines are PROME-lane, queued for its next canon pass.

*Scaffolded by DAEDALUS 2026-08-03 on Will's ratification. Pointer only — the charter is the single source of truth (see root CLAUDE.md § Output Canon: reference, don't copy).*
