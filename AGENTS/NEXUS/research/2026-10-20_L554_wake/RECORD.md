# NEXUS — DOCKET L554 weekly Tuesday wake, fire #3 — RECORD

**Session:** 2026-10-20 Tue, opened 09:15:19 EDT (`date`). PROME-spawned Tier 1 (WQ-343 / DOCKET L554). Runtime: Claude Code, `claude-opus-5-5`, launched from PROME's cwd. Root `CLAUDE.md`, `USER.md` and NEXUS `CLAUDE.md` (BOOT/CLOSEOUT) were read explicitly. **Scope = L554 letter:** boot, self-letter audit, read what moved since 10/19 13:40, grade the resolvers that are due, close. Not a full matrix review and not a re-sweep.

**Sources (live, pulled this session; raw copies in this folder):** FRED `fredgraph.csv` 09:16–09:20 ET (`DFII10_fred.csv`, `FRED_frontier.csv`) · Cboe `VIX_History.csv` 09:17 ET (`VIX_cboe_tail.csv`) · `fetch.py` FRED + `price ^VIX --json` 09:15–09:17 ET. ⚠️ It is a trading day: anything quoted for 10/20 is intraday, not a close.

---

## 1. GATE-NEXUS-T12S-DFII10 (L13): window 1 GRADED ⚪ C#1 NO-VERDICT, EARNED

Letter: `research/2026-09-24_t12_successor_DFII10_letter.md` §2 (frozen). L = 2.85 [9/24]. UP = 5 consecutive cells ≥ 2.95. DOWN = 5 consecutive cells ≤ 2.75. Window = 15 published cells after the anchor.

| Cell | Obs date | DFII10 (FRED) | ≥2.95? | ≤2.75? |
|---:|---|---:|:-:|:-:|
| 1 | 9/25 | 2.83 | · | · |
| 2 | 9/28 | 2.90 | · | · |
| 3 | 9/29 | 2.91 | · | · |
| 4 | 9/30 | 2.93 | · | · |
| 5 | 10/1 | 2.88 | · | · |
| 6 | 10/2 | 2.92 | · | · |
| 7 | 10/5 | 2.95 | ✔ (run 1) | · |
| 8 | 10/6 | 2.91 | · | · |
| 9 | 10/7 | 2.92 | · | · |
| 10 | 10/8 | 2.87 | · | · |
| 11 | 10/9 | 2.91 | · | · |
| — | 10/12 | (blank: Columbus Day, not a cell) | | |
| 12 | 10/13 | 2.88 | · | · |
| 13 | 10/14 | 2.84 | · | · |
| 14 | 10/15 | 2.78 | · | · |
| **15** | **10/16** | **2.74** | · | ✔ (run 1) |

- **Neither branch completed by cell 15.** Longest UP run = 1 (10/5). Longest DOWN run = 1 (cell 15 itself, 2.74 ≤ 2.75). ⇒ **C#1 NO-VERDICT: the split moves 0pp, recorded as EARNED.** Arithmetic is in integer hundredths: 274 ≤ 275, 295 ≥ 295.
- **Vintage:** cells 1–14 match the values NEXUS logged at first read (9/25–10/19). Cell 15 was first read this session, so today's pull is the first-published value NEXUS holds. It is INFERRED, not VERIFIED, that FRED has not revised the cell since it first published (no ALFRED pull).
- **Disc-A:** no fire, so no mechanism grade.
- **Split 20/47/33 HELD by the letter.**

### 1a. Re-anchored window 2 (the one renewal the letter allows; C#2 ⇒ EXHAUSTED, terminal)

The frozen §2 text: *"C #1 ⇒ exactly one re-anchored window (L₂ = the 15th cell of window 1; the next 15 published cells; same edges, same consequences)."*

| Item | Value |
|---|---|
| L₂ | **2.74 [DFII10, 10/16, FRED]** |
| UP | 5 consecutive published cells **≥ 2.84** ⇒ Break +6pp, taken from Grind-lasts |
| DOWN | 5 consecutive published cells **≤ 2.64** ⇒ Break −6pp, given to Grind-lasts |
| C#2 | neither by cell 15 ⇒ **EXHAUSTED, terminal**. The split line then reads "currently un-falsifiable" on real yields. No third DFII10 window without Will's word. |
| Expected calendar (cells counted, not dates) | cell 1 = obs Mon 10/19 (not yet at FRED at 09:20 ET 10/20) · cell 5 = obs Fri 10/23 (earliest fire; FRED read ~Mon 10/26) · cell 15 = obs Fri 11/6 (FRED read ~Mon 11/9, possibly Tue 11/10). No bond-market holiday falls inside: Veterans Day 11/11 is after cell 15. |
| Regime check | 2.74 is still ≥ 2.50, inside the regime the letter was admitted for. |
| Count-once with L16 | The HY letter's window (if it anchors on 10/19) runs at almost the same time. Same-direction fires ≤30 days apart ⇒ ONE ±6pp. Opposite directions ⇒ both apply, net 0. This rule lives in the L16 letter and is carried here unchanged. |

**Dated deferral discharged (DAEDALUS Gate-Basis #2, 10/8; PREDICTIONS L13):**
- **Published precision:** 0.01 percentage points. Compare in integer hundredths; never use float ×100.
- **Ties:** inclusive at both edges (≥ 2.84, ≤ 2.64), as the frozen letter's ≥ and ≤ say.
- **Grid-backtest tie handling: UNKNOWN.** The 9/24 grid script was kept in a session scratchpad and never committed (letter line 131). This affects how much weight the 21.5% / 22.3% / NV 56.2% base rate deserves. It does not affect this grade, which runs on the letter's own inclusive operators.
- **Actionable life:** 8 of the 15 cells (15 − 1 publication lag − 5-cell run − 1 trading day). The same formula gives L16 its 10. The consequence is a published probability with no capital path, so "actionable" means when the split could move.

**Five-case counterexamples for window 2 (BOOT 0b, worked against L₂ = 2.74):**

| Case | Cells | Grade |
|---|---|---|
| Lower boundary, inclusive | 2.64 ×5 | DOWN at cell 5 |
| One unit inside the lower edge | 2.65 ×5 | no DOWN (C if nothing else completes) |
| Upper boundary, inclusive | 2.84 ×5 | UP at cell 5 |
| Mixed | 2.84 ×4, 2.83, then 2.84 ×5 | UP at cell 10 (the first run was broken by a published cell) |
| n = 0 (no cell published by the expected end) | — | not graded. The letter counts cells, so the window stays open, with no backstop. ⚠️ This is a gap in the frozen letter: it has no backstop or VOID clause for an outage, unlike L16. Disclosed, not edited. |
| n = 1 | a single 2.62, then window ends | no fire ⇒ C#2 ⇒ EXHAUSTED |

---

## 2. GATE-NEXUS-WQ459-HY (L16): **still NOT ARMED. The anchor is unpublished and nothing has failed.**

- **Anchor rule (frozen):** L and C₀ = the HY and CCC cells for observation date 2026-10-19 (Will ruled Mon 10/19), or the next qualifying observation if 10/19 doesn't qualify.
- **Check at 09:16–09:20 ET 10/20 (FRED `fredgraph.csv`):** all five ICE series (`BAMLH0A0HYM2` · `BAMLH0A1HYBB` · `BAMLH0A2HYB` · `BAMLH0A3HYC` · `BAMLC0A0CM`) end at **10/16**: HY 331 · BB 203 · B 335 · CCC 1297 · IG 85. The 10/19 cell is **SEARCH-NOT-FOUND (dated)**: not yet published, so it is no observation. Those 10/16 values are pre-ruling and are never used as the anchor.
- **Logged:** a `PUBLICATION_CHECK` row in `analysis/WQ342_grading_log.tsv` (first-read discipline: nothing logged as an anchor read).
- **Why the receipt gap since 10/19:** nothing has published that would let me arm it. The 10/19 13:19 check found the same 10/16 frontier. This is publication lag, not a defect.
- **Calendar:** the provisional dates in `research/2026-10-19_WQ459_registration/CALENDAR.json` stand unchanged: cell 3 = obs 10/22 (read ~10/23, L751) · cell 15 = obs 11/9 (read ~11/10, L753), or 11/6 (read ~11/9, L752) if 10/31 qualifies · backstop 11/23 end ET (L754 on 11/24).
- ⚠️ **Proposal for PROME:** the anchor needs a NEXUS first read once the 10/19 cell publishes, expected later on 10/20. With no wake before L751 (Fri 10/23), the first read of the anchor would happen on the same day as the earliest possible cell-3 fire. The letter allows that: the anchor is a first-read cell, and the grade re-pulls both vintages. But it leaves no day of separation. **Recommend a one-line NEXUS wake on Wed 10/21 (Tier 1, approved workstream) to read and log the anchor and fix L, C₀ and the numeric edges.** If PROME declines, L751 on 10/23 does the anchor read and the cell-3 check together.

---

## 3. Other letters that touched today

### M-04 (VIXCLS, UP ≥ 18.41 ×2): **UP COMPLETES ON THE 10/19 CBOE OFFICIAL CLOSE. The formal grade waits for the FRED cell.**
- 10/16 = 19.99 [FRED VIXCLS]. **10/19 = 18.44 [Cboe `VIX_History.csv` official daily row, read 09:17 ET 10/20]**, 3 hundredths above the 18.41 edge (1844 ≥ 1841). `fetch.py` agrees: prev 18.44 [10/19]. VIOLET recorded 18.44 as a 16:15 ET quote on 10/19 when Cboe's daily row was still missing, and that row has now published.
- **The letter's instrument is "VIXCLS (FRED, CBOE close)", and "a cell not yet published is not an observation."** The FRED 10/19 cell was unpublished at 09:20 ET. **So M-04 stays 26% on this surface until FRED publishes. If VIXCLS 10/19 = 18.44, or anything ≥ 18.41, then M-04 UP fires: 26% → 30% (+4pp), with fire cell 10/19.** If FRED differs from Cboe, FRED governs and the difference goes on the grade (same rule as L13's early copy).
- ⚠️ **0b finding (iii/iv):** the M-04 letter doesn't say whether Cboe's own published close can stand in as an early copy of the FRED cell. L13 has that clause; M-04 does not. Resolved conservatively: wait for FRED. Recorded, letter not edited.
- **Disc-A (mechanism, graded separately at the fire):** HENRY's after-close 10/19 Cboe-chain proxy shows **NEGATIVE gamma at both horizons** (14d flip ~7,756, 35d ~7,762, SPX 7,690.73). Source: HENRY STATUS 10/19 17:44–17:46 ET, routed in SIG-W-20261019-020. That is the claimed mechanism, so **at a 10/19 fire the mechanism check reads TRUE-in-spirit, with proxy caveats** (free-tier chain, assumed dealer positioning, walls withheld, one proxy family). It also clears the ⚠️ "M-04 26% reads ~3pp high" flag: the 9/29 +3 was made on negative gamma, gamma flipped positive 10/8, and it is negative again now. Removing that caveat moves no number.

### M-08 (UP needs B ≥ 330 AND CCC ≥ 1200 on 2 same-date cells)
1 of 2 (335/1297 [10/16]). The 10/19 pair is unpublished. No grade.

### M-01 / M-03 / M-05 / M-07: no branch completed
- HY 331 vs the 350 UP edge. ICSA 199K [w/e 10/10] (FRED's w/e 10/3 now reads 198K vs the 197K first print: first-published governs, revision noted).
- DGS10 5.09 [10/16] vs the ≤ 5.07 DOWN edge: 2bp above it, no run started.
- KRE 69.26 [10/19 vendor close] inside 64.02–75.16.
- IG 85 vs 71/93.

### L11 / PRED-30 (August TIC, raw ⚪): owner recommendation; PROME to confirm
- Letter (COLD §P5 L11, 9/17): HIT ≤ −$12.0B · MISS ≥ −$3.0B · ⚪ strictly between, "available ONCE — a second one resolves the row ❌ MISS and closes it." August China LT/coupon = −$4.828B (ZHAO 10/16) ⇒ ⚪.
- **Recommendation: grade ⚪ NO-VERDICT, FINAL, and close PRED-30.** The July ⚪ came from the *previous* two-branch letter's construction defect, not from this letter's band, so it is not this letter's first NV. That means August is not a "second" NV and does not convert to ❌.
- The letter registered exactly one print (August) and no follow-on window. Renewing it would be a new letter, and that is not done without Will's word.
- ⇒ **M-10 holds 25%** (its letter rides L11; ⚪ ⇒ hold, EARNED once).
- ⚠️ **0b (iv) finding:** the clause "available ONCE" is not exhaustive for a single-print letter, because it names no second window. Disclosed.
- If PROME or Will instead count July as the first NV ⇒ ❌ MISS, M-10 −4pp (25 → 21). Recorded as the alternative, not applied.

### PRED-38 (resolves 11/10)
WAL Q3 (8-K 0001628280-26-066286, owner WAL 10/19): total NCO $45.8M for the quarter, with no ≥$100.0M attributed NBFI charge-off ⇒ **WAL does not qualify**. k = 0 qualifying so far. Coverage is still incomplete (OZK 10/20 AMC; other banks' 10-Qs). No early grade.

---

## 4. BOOT 0b self-letter audit (delta since the 10/19 full audit `research/2026-10-19_full_synthesis/SELF_LETTER_AUDIT.md`)

| Letter | (i) date | (ii) magnitude | (iii) resolver exists today | (iv) branches | Finding |
|---|---|---|---|---|---|
| L13 window 2 | ~11/6 cell 15 | ±6pp; ±0.10 | FRED DFII10 returned 10/16 | five cases written above | ⚠️ no outage backstop (disclosed) |
| L16 | provisional 11/9–11/23 | ±6pp; ±10bp | five ICE series returned 10/16 | letter table | unchanged; NOT ARMED |
| M-01/03/04/05/07 | 11/05 | ±4pp | HY/ICSA/DGS10/VIXCLS/IG at FRED; KRE vendor | 10/8 page | ⚠️ M-04 early-copy clause absent (resolved: FRED waits) |
| M-08 / M-09 | 10/30 | ±4pp | B/CCC/BB at FRED | unchanged | — |
| M-10 / L11 | L11 grade | ±4pp | ZHAO TIC read | ⚠️ single-print NV clause | recommendation above |
| M-11 / PRED-45 | 11/20 | ±4pp / HIT-MISS | EDGAR/court documents | unchanged | — |
| PRED-38 / 41 | 11/10 / HHDC | k-count / ±50bp | EDGAR / NY Fed | unchanged | — |
| M-06 | — | withdrawn | — | DEFECTIVE (10/14) | unchanged |
| GATE-NEXUS-SEAT-01 | terminal 10/14 | — | — | — | archive at PROME's next terminal pass |

No letter newly marked DEFECTIVE. The two ⚠️ clause gaps are disclosed in place. Neither changes today's grade.

## 5. Inbox and WALTER lane (BOARD_CONSUMPTION_SPEC; rows in `board_log.tsv`)

| Item | Disposition | Note |
|---|---|---|
| SIG-W-20261019-012 (ACTION: OTTO Ally / warehouse 55→25% / calibration 3/8) | acted | NEXUS never carried the superseded 55%, the Ally framing or 5/10. Grep clean ⇒ COR-20261019-12 receipted NO-OP. |
| SIG-W-…-015/016/017/018/019 (breadth, cruise, repeat-losers) | noted | Context for R7 and counterevidence. They are not independent break votes (WALTER says so as well). No row moved. |
| SIG-W-…-020 (HENRY negative gamma both horizons) | acted | M-04 Disc-A context above; the ~3pp-high caveat is cleared. |
| SIG-W-…-021 (WAL Q3 counterevidence) | acted | PRED-38: WAL k = 0. Chain CARL→REGINALD counterevidence noted. |
| OTTO 10/19 ×2 (closeout finish; forecast repairs) | noted | Same content as -012. Brief pin 7a690e796 noted. No NEXUS figure affected. |

Not done (scope): BOOT 6 digest readers and the full brief census. This was a scoped due-row wake, and the 10/19 full review stands. The 10/19 evening commits by HENRY, WAL, LIQUID, CRUISE, VIOLET and TERRY were read through WALTER's routed kernels, plus direct owner reads of HENRY STATUS (gamma), WAL STATUS (NCO) and VIOLET STATUS (VIX row).
