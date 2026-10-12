# WATT — handoff before approved protocol implementation

Payload: entire previous SCRATCH.md, UTF-8 bytes including final LF; 4379 B, crc32 57118be6. Preserved verbatim below.

# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**


---

## CURRENT PICKUP — 2026-10-12 12:31 ET; window closed on Will's instruction

**Source boundary:** records/procedure closeout only. No new PJM/FERC pull; power evidence remains **October 12 10:35 EPT**. P1/P2/P3/P4 **5/5/4/2**, composite16/20. WATT-10 MISS is final; WATT-08 (~50% DoorB) and WATT-09 remain OPEN. No trade or threshold change.

**Completed:** L654 morning primary checks and four-item inbox drain; FERC order grade; owner-consumer packets; native Codex queue verification. **PROME consumed** report/state427c1280f and deliveryd9127ded0 at `PROME/reports/2026-10-12_WATT-L654-L200-consumption.md` (30770e3bb). Prior research/status/queue/limitation commits published, verified against fresh origin657703deb. Historical automatic-review rejections are retained; **no approval or retry owed for that published work**. Other consumer acknowledgments remain unknown.

**Requested comparison:** `reports/2026-10-12_closeout-procedure-comparison.md`; draft `proposals/2026-10-12_CLOSEOUT_PROPOSED.md`. Recommend BOND's finish discipline + BRENT's source/write-back reconciliation + WALTER's receipt reconciliation. **Proposal only:** CLAUDE.md unchanged, no runner installed. User asked for recommendations; no new implementation commissioned.

## NEXT OWNER TOUCH — registered event work, not automatic monitoring

1. **L692, October 13–14:** complete October 12 tape/board/DOE read; inspect October 13–14 advisories and **October 14 noon EPT** maintenance recall. New backup authority is REQUESTED at the last read, issuance/use unverified. No full-day all-clear.
2. **L693, first boot>=October 15:** grade all seven clear calendar days October 8–14 and the new DOE-request disposition before P1 de-escalation. Preserve missing-interval limits. No early5→3.
3. **FERC:** original IRAS resolver L200 closed/WATT-10MISS; definition/registry compliance within30 days of October 9 and any revised filing remain follow-ups. EL26-67 response **November 16**, answers **December 16**, qualifying205 filing suspension respondent-specific; WATT-09 outerNovember 30 unchanged.
4. **Other registered clocks:** battery recheck>=October 19; existing instrument/interchange/metered-vs-DR deferrals October 23; wake-list review October 31. Weekly cadence next boot<=October 19; earlier L692/L693 take priority.

**Unresolved owner carry:** hedged/floating exposure owed to VULCAN; 6.5 GW gap; Appalachian basis/NG=F settlement clock; ERCOT Cal-27 discriminator. Details remain at STATUS OPEN and prediction rows; do not restate as newly measured.

**Operational continuity:** WATT session UUID 01a1308e-b0ab-7f00-883d-408ac1b2bd07 observed in this window; PROME queue target 01a1307b-f614-76b3-8caf-49b226027079 verified. A new window must discover its own identity/capabilities, not reuse this UUID. Startup pull deferred for foreign dirty work; exact owned-path commits only. Closing delivery and new-commit publication receipt are reported separately. Prior SCRATCH preserved at `archive/SCRATCH_ARCHIVE_2026-10-12_pre-final-closeout.md`.
