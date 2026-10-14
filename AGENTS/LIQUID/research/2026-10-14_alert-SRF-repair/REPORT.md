# Alert output and SRF date alignment — October14 repair

**Session:** `01a13b8c-ebf0-74c0-a1c3-5ae79550bd06`, ongoing sole LIQUID writer confirmed by Will; Codex/OpenAI, GPT-6 family, exact variant UNKNOWN. Will authorized CATO's proposed repairs. Acceptance committed **701511870 before code edits**; pre-edit scripts/state and protected hashes retained. No additional agent, live test delivery, timer invocation, trade, spending or threshold change.

**State: IMPLEMENTED · TESTED. INDEPENDENTLY VERIFIED: pending.** WQ229 requires a reader-devised counterexample before a consequential repair is called fixed. No reader was launched. The source edits are present in the existing script paths; no independent certification or operational hold/release decision is invented. The swap-line instrument and letter remain WITHHELD and untouched.

## What changed

| Repair | Implementation | Evidence |
|---|---|---|
| **Alert content at actual consumers** | SIGNALS emits one full row per fresh event, preserving each event's date, target/priority and applicable guard. No240-character cutoff or first-event-only description. Local alert log carries the same full qualification. PROME mixed packet retains both sides | Temporary-file tests run the real watcher main/delivery functions for ordinary, late, escalation and simultaneous events, then inspect emitted packet, SIGNALS and alert log |
| **Historical event versus current quote** | Packet headline names recovered historical event/date separately from the current quote. SIGNALS row date is the original historical event date. Unknown/invalid historical dates remain UNKNOWN | Recovered July2 event with October14 290bp current quote appears separately on all consumers; neither is presented as a current sub260 reading |
| **First-publication value/date labels** | Ordinary kill alert reports its first-published observation value. Historical detection compares the recovered event date to the latest observation date, so a lagging first-publication frontier cannot stamp the event as today | Two additional author counterexamples: first-published258/latest290 and first-published frontierJuly3/latestJuly6. Existing code failed; revised output preserves original value/date |
| **SRF combined grade** | Existing Treasury/MBS display requires finite values and aligned valid observation dates. Mismatch, missing date or failed leg shows individually dated components and withholds combined grade. Aligned strict>$50B and existing routing unchanged | Synthetic30B legs on different dates no longer grade60B. Quiet mismatches, equal50, above50, missing dates/legs and nonfinite values tested; default collapsed output keeps ungradeable row visible |
| **Preventive HY precision** | Both latest zone input and as-first-published kill observations normalize to the existing integer-bp basis before comparisons |259 qualifies;260/261 and tiny floating representation perturbations do not. Invalid quote is parse failure without a grade. No observed live260bp misgrade claimed |
| **Verdict/context boundary** | STATUS, MEMORY and LIQ-07 preparation now state that missing ETF/discount-window/financing context cannot delay an otherwise complete registered verdict | Required inputs and both session lists remain necessary; frozen letter/prediction fields, calendar and registered funding calculations are byte-stable |

Delivery remains file-only to the same existing destinations. Existing delivered-key format is unchanged; old state keys are recognized. No unattended Git or external notification is added. Historical emitted alerts are not rewritten or retrospectively regraded.

## Tests and acceptance coverage

- **18 offline consumer/date tests PASS**, including ordinary, overlap, wrong-owner preservation, missing information and repeat/append activity. All output destinations are temporary directories. Full synthetic consumer snapshots are in `consumer-tests.txt` and clearly labeled, not market observations.
- **Five old-code negative controls fail as intended:** truncated qualification, conflated mixed headline, latest/first-published value confusion, delayed-frontier event misdating and cross-date SRF grade. These are author falsification probes, not independent review. Receipts: `baseline-probes.json`.
- **39 saved published observations August20–October13 replay unchanged** for zone/count/terminal state and event count against pre-edit code. Latest zone versus first-published kill bases remain separate. This is a bounded saved-data replay, not a fresh pull or full-history census.
- Existing watcher and boot selftests PASS; protected-content/diff, weekday and scoped read-budget checks accompany `validation.json`.

Reproduce from repository root:

```bash
.venv/bin/python3 AGENTS/LIQUID/scripts/test_alert_srf_repair.py
.venv/bin/python3 AGENTS/LIQUID/research/2026-10-14_alert-SRF-repair/baseline-probes.py
.venv/bin/python3 AGENTS/LIQUID/scripts/hy_oas_watch.py --selftest
.venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --selftest
```

## What remains unresolved

1. **Independent review:** consequential author-tested code is not yet VERIFIED. PROME receives exact source/tests/acceptance/results and must obtain an existing authorized reader's own counterexample before closure. No new reader/agent launch is authorized by this packet; CATO remains manual-only.
2. **Delivery-failure retry bookkeeping:** existing delivery marks attempted events in its state even after a destination failure; a pending-event/per-recipient retry redesign is outside this bounded content/date repair. Missing SIGNALS destination now produces a visible failure log, never a success receipt. This repair does not certify guaranteed delivery after an I/O failure.
3. **General stale-state-language proof and broader dashboard debt:** tests preserve the applicable conditional rules; they do not prove every novel wording harmless. Other ladder calculations, letter precision/curve questions and GATE079 FIRE calibration remain their existing obligations.
4. **Future verdict evidence:** October16 funding completion still requires its registered observations and both lists. Missing required data remains pending; unavailable supplementary context is reported beside a grade and never becomes an extra condition. Offshore basis/private collateral evidence remains unavailable; withholding unchanged.

No live market refresh was performed for this repair. STATUS market cells retain their observation dates throughOctober13. This does not certify current market conditions or recipients' consumption.

## State write-back and delivery

STATUS's repair rows now distinguish implementation/testing from independent closure. The normalization task is no longer described as unimplemented; the other DAEDALUS asks remain. The stale pending FORGE classification fix was removed after reading its processed October8 FYI and confirming current `config.classify` precision normalization. FORGE itself is untouched.

Pre-edit state/preparation documents are archived, and all five gate rows, prediction rows/Kernel-pinned LIQ-04, withheld files, gate letters, calendar twins and shared configuration remain unchanged. No new auto-memory/KB/catalyst entry: this is an existing-tool repair with no new criterion or date. Ledger-nudge warnings are acknowledged; there is no changed ledger fact to refresh.

PROME receives a self-authored dated packet under carve-out①. Shared WALTER/VIOLET work was left alone; no pull. Native cross-window notification/consumption and independent-reader disposition remain unverified. Final Git receipt proves persistence, not review or receipt by PROME.
