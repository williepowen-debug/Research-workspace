# HANS → PROME · 2026-10-08 (hans-1008, WQ-391) · T-13/T-06 ARMED on the close · T-10 MET-OPEN · Budget date fixed · THRESHOLDS rotated — ⚠️ PARTIAL (stopped on PROME's WQ-249 ask, 11:55 ET)

Boot: `boot.py` rc1 (attention) · R1 corrections rc1 (COR-20260921-16 unreceipted — see GAPS) · read `CLAUDE.md`, `AGENTS.md`, `USER.md`, HANS `CLAUDE.md`, brief + COMMON. Runtime: Claude Code, Opus 5.5, Agent-tool spawn.

## 1. Grades (registered letters; proxies labelled — no fire graded on a proxy)

| Row | Letter | Reading (source, clock) | Grade |
|---|---|---|---|
| **HANS-T-13** UK 30Y | benchmark daily CLOSE >6.00 | TE 5.9910 [read 15:43Z] · CNBC 5.9943 [15:43Z] / 5.9931 [15:51Z] / 5.9979 [15:54Z]; CNBC 5-min at the 16:30 BST close 5.9914 [15:30Z] → 6.0015 [15:35Z]. Intraday high **6.0473** (~11:00Z); above 6.00 most of the London morning | **ARMED — NOT graded final.** All proxies 0.2–0.9bp UNDER, inside the vendor gap. **Armed rule (written before the close is final): FIRED (orange) dated 10/08 iff TE's 10/8 daily close > 6.000; CNBC 10/8 close cross-checks; a straddle grades on TE with the gap stated.** No fire ⇒ no consequent to quote |
| **HANS-T-06** UK 10Y | benchmark daily CLOSE >5.50 | TE 5.4791 [15:43Z] · CNBC 5.483–5.4863 [15:43–15:54Z]; intraday high 5.5267 | **ARMED — NOT graded final.** 1.4–2.1bp under. Same armed rule at >5.50 |
| **HANS-T-10** OAT–Bund | spread >100 AND OAT >4.50 (i-i governs) | **139.8bp / 4.90** (Bund 3.50) [ideal-investisseur 10/08, page 17h09 CEST]; CNBC ~140.6, TE ~139.3 | **MET-OPEN, unchanged.** Exit clock **0 of 5** — every i-i row 10/02–10/08 (146.9 · 143.4 · 127.4 · 134.4 · 139.8) is over both fire lines, which resets it; it cannot have started. Bund referee: i-i 10/07 3.49 vs ECB AAA 3.538 = 4.8bp (inside 5bp, barely) |

- **Official close NOT reachable at 11:55 ET:** the TE daily close (the rows' registered basis since 8/28) is not final at the post-close read; UK DMO reference prices sit behind a bot wall (perfdrive/ShieldSquare redirect); BoE IADB has **no 30Y** and `IUDMNPY` is a **par-yield cross-check at ~D+2, not the T-06 basis**. ⚠️ The brief's "IUDMNPY is primary for the UK leg" is not my registration — it is a cross-check (CLAUDE.md, boot §[2]).
- **Dark-days check 10/05–10/07:** no missed fire on either row (CNBC daily closes 30Y 5.9435 / 5.9058 / 5.9806; 10Y ≤5.4345). Three 30Y intraday touches without a close through: 10/01 6.0289 · 10/07 6.0357 · 10/08 6.0473.
- **Who closes the arming:** a reader of TE's 10/8 close (TE page/history on 10/9, or CNBC previous-close on 10/9). PROME re-spawn or a WALTER read is needed; HANS is not waiting hours for it.

## 2. Budget date — WALTER is RIGHT, verified at primary
**UK Budget = Wed 2026-10-28.** Primary: gov.uk *"Chancellor letter to the Treasury Select Committee (TSC) – Budget 2026 date"*, published 31 Jul 2026 (page: *"The Budget will be held on 28 October 2026"*); letter PDF (Healey to Dame Meg Hillier, dated 31 July 2026): OBR forecast *"for publication on 28 October 2026. This will be accompanied by the Budget."* 26 Nov was the 2025 date. **What it changes:** the T-13 LDI catalyst is **20 days out, not ~49**, and lands the day **before** ECB GovC 10/29 (T-04 one hike away). Fixed in STATUS docket + T-13 state. ⚠️ Still carrying 11/26 (not yet fixed): `workbook/FLOW.tsv` FLOW-HANS-5 notes, `workbook/KB.tsv` KB-HANS-045/064, `LAST_COMPLETION.md` (dated records in SESSION_LOG/DISPATCH_LOG/workbook blocks left as history).

## 3. READ_CAP — THRESHOLDS.tsv rotated (DONE, verified)
`registry/THRESHOLDS.tsv` **33,544 B (103%) → 22,120 B (68%)** of the 32,550 B budget (`measure.py`), under the rule-5 stop. 21 cells moved **verbatim** to the new cold `registry/THRESHOLDS_HISTORY.tsv` (crc32 per row; basis `51d95040f`); an independent check against `git show HEAD` rebuilt every changed cell exactly (0 defects). **Write mode adopted (rule 19):** the `state` cell carries the CURRENT grade only; superseded text goes to the cold file the same day. No band, sustain or fire changed; T-08/T-14/T-15 notes compacted with their operative rules kept hot (T-08 fail-closed exit clauses + baseline-sensitivity caveat; T-14 Will's 8/28 scope ruling; T-15 sizing/scope/withdrawn -5.8%). ⚠️ Headroom to the 75% re-rotation trigger is ~2.3 KB. WALTER needs no repoint (same path). **READS.tsv declaration packet NOT sent (GAP).**

## 4. Not done (stopped on the closeout ask)
LIQUID 10/1 floor/turn-bound answer · whole-inbox drain (3 top-level + 17 WALTER-lane, incl. new `SIG-W-20261008-019` Isaias; **none moved, none logged**) · COR-20260921-16 receipt (already APPLIED in T-15's 9/25 notes; the receipt command was not run) · STATUS rotation to <70% (STATUS 72%+, test `test_the_split_actually_moved_the_bytes` fails) · closeout_check/orphan/consumer/claim checks.
Pre-existing defects, named not fixed: `test_C2_is_SERIES_QUALIFIED` fails (two metric names, `OAT_BUND_SPREAD_BP` and `FRANCE_GERMANY_10Y_SPREAD_BP`, both declare VX-HANS-3.02 and both retire 96.8) · doc_audit C2 flags VX-HANS-3.07 = 4.90 because 4.90 was also a retired 10/01 value (a recurring value, not a stale one) · DISPATCH_LOG C7 pointers to PROME packets since moved to `processed/`.

## COMPLETION
STATUS: ⚠️ PARTIAL — T-13/T-06 ARMED (official close not reachable 11:55 ET), T-10 graded, Budget date verified, THRESHOLDS rotated; stopped on PROME's WQ-249 ask
CHANGED: AGENTS/HANS/registry/THRESHOLDS.tsv · registry/THRESHOLDS_HISTORY.tsv (new) · workbook/VX.tsv · workbook/PUBLISHED.tsv · STATUS.md · this memo
RESULT: T-13 ARMED (proxies 5.991–5.998, 0.2–0.9bp under 6.00; fires iff TE 10/8 close >6.000) · T-06 ARMED (5.479–5.486, ~2bp under) · T-10 MET-OPEN 139.8bp/4.90, exit 0/5 · UK Budget = 2026-10-28 (gov.uk primary) · THRESHOLDS 103%→68%
GAPS: TE 10/8 close unread · LIQUID packet · inbox drain 0/20 logged · READS packet · COR-20260921-16 receipt · STATUS still >70% · FLOW/KB/LAST_COMPLETION still say 11/26 · closeout checks not run
WILL_NEEDS: none (no fire, no trade, no threshold move)
FOLLOW-UP: on 10/9 read TE's 10/8 UK 30Y/10Y closes and apply the armed rule (fire T-13 iff >6.000); re-spawn HANS for the drain + LIQUID answer + READS packet before the 10/28 Budget
