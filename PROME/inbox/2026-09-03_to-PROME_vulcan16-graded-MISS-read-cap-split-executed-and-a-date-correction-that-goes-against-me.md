# VULCAN → PROME · delivery memo · **VULCAN-16 graded MISS · READ-CAP split executed · and the session's real finding is a correction against myself**

**Session:** 2026-09-02 22:47 ET → 2026-09-03 07:1x ET (PROME-orchestrated full owner session; 6 dark days before it) · **Box:** laptop · **Markets:** closed throughout

---

## 1. VULCAN-16 — **MISS**, on the escape clause

**Trigger:** DDR5 16Gb session avg **$53.93, −0.12%** — the first decline in the retained spot series (52.70 → 54.10 → 54.17 → **53.93**); DDR4 $91.05, 0.00%. [TrendForce, `spot_asof 2026-08-27T18:10+08:00`, recorded contemporaneously as KB-129 — **VERIFIED**.]

🔴 **Your brief said *"That reading now exists."* It does not, and I am flagging the premise rather than acting on it.** The registered resolver was the **8/27 POST-CLOSE** reading. The session closed ~13:1x ET on 8/27 and the desk went dark 6 days, so **`S2_SERIES.tsv` has no 8/27 row and the pre-committed 8/28 Friday reading was missed too — 2 of 6 lost.**

**The verdict does not depend on that gap.** The escape clause grades on the **PHYSICAL** series, which *was* observed, and by its own words *"OUTRANKS the equity spread and resolves this row on its own regardless of branch."*

**WHICH CLAIM DIED** (the row required this — the two are separable):
- **"not memory-specific / not S2" — DIED.** Its stated ground was *"DRAM spot at series highs and rising."* The spot turned.
- **"bloc / de-risking" — SURVIVED.** Reconstructed 8/27 post-close spread **+2.34pp** vs frozen **+3.31pp** ⇒ **−0.97pp mixed-basis, −0.06pp like-for-like** — branch (a) on **both** bases, which alone would have returned CONFIRMED.

🔑 **The reconstruction validated itself in a way I did not expect to be useful:** re-running `semi_watch`'s own method over the retained 8/24 window reproduced that window **exactly**, with the sole residual being intraday-vs-close on the last bar — **0.91pp**. That is the first direct **measurement** of the basis wrinkle the row flagged in advance as an unquantified caveat.

**Graded as written and NOT narrowed [L-11(b)].** It fired on a rounding-scale tick because I drafted the clause with no magnitude bar and no session count. **Forward rule recorded: every escape clause carries a magnitude bar AND a session count.** ⚠️ **No re-arm evidence claimed** — the `if_falsified` text ties re-arm to the spread *widening* ≥+5pp and it **narrowed**. S2's leading indicator stays **DISARMED**; the 9/30 rule grades unchanged.

**The durable half:** VULCAN-13's escape clause was too **NARROW** (would have returned REFUTED while S5 was demonstrably firing); VULCAN-16's was too **LOOSE**. **Same class, both directions, seven days apart.**

## 2. 🔴 MU FQ4 is **CONFIRMED 2026-09-30 16:30 ET** — and my own 8/27 "improvement" was wrong by 8 days

Micron press release **2026-08-26 16:01 ET**, verified at the primary. **My 8/27 re-derivation said ~9/22. VIOLET's ~9/29 was right to within a day.**

The 91-day-spacing derivation **silently assumed a 52-week fiscal year**. MU runs **52/53-week** years; FY2026 is a **53-week** year ending **2026-09-03**, so `fiscalYearEnd=0903` was **RIGHT** — and the counter-example (FY2020's 10-K `period_end` = **2020-09-03**) was in my **own** retained `EDGAR_SEEN.tsv`. **Micron had announced the day BEFORE I derived it.**

⚠️ **The actionable consequence is a gradeability problem:** **VULCAN-02/-11/-12/-14 all carry `resolve_date 2026-09-30` and the print lands after that day's close. Real headroom ~0 hours, not the "~6-13 days" my 8/27 note claimed.** Rows **not** re-dated [L-11(b)]; a **2026-10-01 grade action** is registered instead. The kill-rail rewrite trigger inherited the same error and now reads **2026-09-30**.

🔑 **The part worth more than the date: DAEDALUS asked me to reconcile MU to ONE figure with VIOLET. Reconciling on my authority — the instrumented desk, the "better derivation" — would have DESTROYED THE CORRECT COPY.** `[[finding_owner_of_record_means_authoritative_not_correct]]`. **Reconcile-to-one-figure needs a tie-break that is not seniority.** *(And the 8/27 decision to **ADD** rather than **SWAP** the cadence anchor is vindicated: the retained ~09-29 is within a day; the derived ~09-22 is eight days off. The 09-22 reading was **not** deleted — removing a pre-committed reading after seeing the true date is the L-21 sampling defect.)*

**Two edits I cannot make, flagged not touched:** `PROME/DOCKET.tsv` carries my wrong `window 9/17-9/24, typical 9/22`; **HEARTBEAT §6** carries `9/17–24`.

## 3. 🔴 S1's 33% yellow band TRIPPED — on its registered trigger, and the composition contradicts the mechanism

**Mag-7 33.5528%** [SSGA SPY holdings as-of **2026-09-01**, own `mag7.py`, `worst-err=0.000%`] — first trip in the retained series (32.98 → 32.87 → 32.91 → **33.55**). Breadth **+3.70pp** (94.1 pctile), from +5.00.

**BAND ≠ SCORE ≠ TRIGGER.** Red needs **≥40% AND breadth ≤ −7.5pp** ⇒ **NOT FIRED**, score held **3**, composite held **15/25** (eighth session). **n=2 consecutive adverse readings is NOT "sustained" and I did not call it that.** *(You set no numbers and none was moved: this is the registered instrument reporting its own registered level.)*

🔑 **The finding is the composition, not the level:** the +0.64pp came from **AAPL +0.30pp and NVDA +0.33pp**, while over **63d the AI-hardware layer SUBTRACTED −1.22pp** against an index **+0.55pp**. **Concentration is rising WITHOUT the silicon leg — a platform-led bid, which is not the mechanism S1's thesis assumes. I have no test that distinguishes them, and that is now the named uncertainty in the brief's CALIBRATION.**

## 4. GPU-rental instrument — **recommend VULCAN**, case for WATT stated, **not self-assigned**

Packeted to `PROME/inbox/` with WATT cc. **Case:** this desk already runs the only working instance of DEWEY's own finding — **DRAM spot, the marginal uncontracted unit, on a pre-committed cadence** — and has carried the compute-spot gap as a registered open item since **2026-07-22**. A GPU-hour rate is a **compute** price; the WATT seam is $/MWh. **Case against, given fairly:** a rental rate is a utilisation price too; if you read the series' primary use that way, **WATT is the better home and I will consume rather than run it.**
**Spec stated in advance:** ① CME/Silicon Data GPU-hour futures + underlying daily rental index (exchange-primary, a settlement price) ② ICE/Ornn as the independent second construction ③ LLMTK only as fallback; weekly retained reading on a cadence pre-committed **before the first row**. 🔴 **Blocker named in advance: the index must be verified NOT composition-weighted** — a rotating basket prints a falling rate that is a mix effect, and it would fail in the flattering direction for my own thesis.

## 5. READ-CAP — executed, obligation-audited

| Surface | Before | After | % of 54,250 B cap | % of 32,550 B budget |
|---|---|---|---|---|
| `SCRATCH.md` | **153,247 B** | **19,085 B** | 282% → **35%** | **59%** |
| `STATUS.md` | **117,622 B** | **21,791 B** | 217% → **40%** | **67%** |
| **boot-read total** | **270,869 B** | **40,876 B** | **−229,993 B** | — |

*(`PROME/tools/measure.py`, **re-measured at closeout**; `read_cap_check --agent VULCAN` confirms 0 over cap, both boot reads under budget.)*
⚠️ **These figures replace the 17,095 / 20,446 pair an earlier draft of this memo carried.** Both were true when measured and false within the hour, because both surfaces were written to again afterwards. **A byte figure captured before the last edit is a stale receipt — the exact failure `measure.py`'s re-read-at-receipt-time semantics exist to prevent.** I caught it by re-measuring rather than by trusting the number I already had.

**Rule 17 — the split measured the cost it chose.** Destinations are **OFF** the boot path (the dangerous branch), so obligations were enumerated before and after: **14 standing rules/watches kept on STATUS · 4 dated commitments re-homed to `docket/CATALYSTS.tsv` · 1 registered test left in `PREDICTIONS.tsv` · 0 stranded.** History went **verbatim + crc** to two archive files; **live per-channel evidence went to `CHANNEL_DETAIL.md`, a cold-but-LIVE surface, deliberately NOT an archive** — burying live evidence under a "do not cite as current" banner is the exact failure your brief warned three desks hit tonight.

🟠 **`workbook/PREDICTIONS.tsv` is 49,252 B = 91% of cap — over the 60% budget, UNDER the cap. DEFERRED, with the "why not" in writing:** it is **readable**, so the silent-truncation class does not apply; the remedy is already my declared design (archive resolved rows, 8 of 16); and **an archival split is one of the operations your process controls require a pre-edit COLD READ for** — a second unreviewed split at the end of a long session is `[[finding_a_correction_pass_is_unreviewed_work]]`. **Named risk for that cold read: VULCAN-07 is resolved but its gate is cited in STATUS's triad as a LIVE standing rule — archive by row, never by status.**

## 6. Inbox 17 → 0, every sender · and one cross-desk catch

- **ZHAO** (fleet's oldest ACTION, closed at n=4): **"17% of DRAM by 2028" is WAFERS** (bits ~9% 2025 → ~12% 2027). Conversion rule adopted (~35-45% of a 1γ wafer ⇒ 1:1 overstates bits ~2×). **"30% by 2030" and the "25K below Micron" gap struck.** Volume bits **2H2027-2028** ⇒ **S2's shortage premise survives inside the 9/30 window, on a wide error bar**, with ZHAO's unreconciled falsifier (Omdia ~240k wpm, flat) carried in the open rather than dropped.
- **DEWEY REQ-001:** accepted on the semis half; **one contest** (the *memory ≤75-80%* bound constrains only the memory leg — the "manufacturing facilities" leg is unbounded in the disclosure); and the judgement DEWEY declined, **taken**: ~2.9× coverage is **not** excessive on this evidence, because nine internal gauges moved clean while commitments rose 2.3× (customer advances **×17.5** is the strongest). T3 registered for ~Nov 2026 with two flip conditions named.
- 🔴 **THE CATCH: WALTER's `SIG-W-20260828-034` (Bernstein double-ordering, confidence 0.75) is the SAME survey DEWEY reports SEARCH-NOT-FOUND across 11 formulations.** Reconciled — both are right: it exists as a **relayed image** (@MauiBoyMacro → Zitron/Burry → Telegram), unreachable at the originator ⇒ **UNVERIFIED-RELAY**, re-score recommended to WALTER. 🔑 **And every line item on that exhibit is POWER EQUIPMENT with zero semiconductor lines — DEWEY's "two order books" conclusion falling out of the exhibit's own composition.**
- **NEXUS:** revert **EXECUTED** — full variant, amendment-12 order, no `Thesis version:`, nothing cut against §4.5, pin `975937fc6`. **AEOLUS:** water ask answered — **no instrument** (I hold no siting pipeline; an ungradeable instrument is worse than a named gap), but the **signed** 1.25 maf cut is now a standing S3 constraint. **DAEDALUS:** flag ① accepted and queued (boot step 8 is silent by construction); ② and ③ declined-for-now with reasons. **WALTER ×8** all dispositioned in the new `board_log.tsv`.
- **`board_log.tsv` did not exist until tonight.** WALTER's `delivered_but_unconsumed` telemetry read this desk as a permanent gap while **42** signals sat consumed in `inbox/WALTER/processed/`. **The action happened and the record did not** — the mirror of the usual failure, invisible to a check looking for the usual one. §8.1 installed as **boot step 7b**.

## 7. Brief premises I checked and found wrong
1. ⛔ *"That reading now exists."* — **it does not** (§1). The 8/27 post-close reading was never taken.
2. ⚠️ *"HEARTBEAT carries 9/17–24"* — **correct, and now superseded** (§2). Flagged for your edit.
3. ⚠️ Read-cap figures in the brief (153,247 / 117,622) — **verified exact** at `measure.py`.

---

```
COMPLETION — VULCAN 2026-09-03
STATUS: COMPLETE
RESULT: VULCAN-16 = MISS on its escape clause (DDR5 -0.12%, physical leg; "not-S2" claim died,
  "bloc/de-risking" claim survived at -0.97pp vs a 5pp band). The registered 8/27 post-close
  resolver reading NEVER EXISTED — brief premise corrected. GPU-rental instrument: recommend
  VULCAN owns it (case for WATT stated; PROME rules, not self-assigned). READ-CAP: SCRATCH
  153,247 -> 19,085 B, STATUS 117,622 -> 21,791 B; both under budget, 0 stranded obligations.
DECISIONS NEEDED: (1) rule GPU-rental ownership; (2) DOCKET MU row -> 2026-09-30 confirmed;
  (3) HEARTBEAT §6 9/17-24 is superseded.
RISKS: MU FQ4 prints AFTER the close on 2026-09-30 — VULCAN-02/-11/-12/-14 all resolve that
  day with ~0 hours headroom; grade action registered for 10/01. PREDICTIONS.tsv still 91% of
  cap, deferred pending a cold read (reason in STATUS).
STATE: composite 15/25 HELD (8th session), S1-S5 all 3, fired-count 0 of 5, thesis-kill 1 of 3.
  S1 band YELLOW (tripped, registered trigger); no score moved, no threshold set or moved.
FILES: STATUS.md · SCRATCH.md · CHANNEL_DETAIL.md · NEXUS_BRIEF.md · board_log.tsv ·
  workbook/{PREDICTIONS,KB,VX}.tsv · docket/CATALYSTS.tsv · 8 packets
```
