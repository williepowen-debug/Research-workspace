# LIQUID Domain Sweep — 2026-07-11 (Sat, ~14:45 ET, markets closed)

**Type:** Triage-only sweep (report, no analytics executed, no live pulls). All levels below are vintage-stamped, not live. Weekend — nothing here is a fresh print.

---

## 1. KB-LIQ-071 / LIQ-05 — premise HALF-FAILED — 🟠 blocking item — re-scope proposal

### What the pre-registration said (verbatim structure, KB.tsv row 72 / `workbook/PREDICTIONS.tsv` LIQ-05, registered 2026-07-08)

A single conjunctive IF/THEN with a companion falsifier:

- **CONFIRM branch (both legs required, AND):** IF Brent **sustain-confirms** (">$75 through Fri 7/10 close, no round-trip <$74, ≥2/4 institutional legs **per BRENT**") **AND** 10Y holds **>4.50 through the week** → HY OAS **partially retraces toward 275-280** over 5-10 sessions, via risk-off/duration **BETA** (KB-LIQ-053 stagflation-mix), NOT energy-credit substance. Grading diagnostic: CCC should co-widen with BB.
- **FALSIFIER branch:** IF Brent **denies** ("round-trips <$74, sanctions/war-risk walk back <48h") → HY OAS **continues retreating**, plausibly re-testing **260**.
- Either path: a re-approach of 280 alone does **not** fire X1 (BROCK wrapper-leads half still LAGS, separate gate).

The Brent leg was explicitly deferred to BRENT's own test ("per BRENT") — i.e., LIQ-05's IF-leg is contractually bound to whatever `GATE-BRENT-SUSTAIN` resolves.

### What actually happened

`PROME/GATES.tsv` — **GATE-BRENT-SUSTAIN RESOLVED 7/10 DENY** (BRENT-Opus, commit `59a34faa`, PROME level-verified): **LEVEL PASSED** (~$76 settle both sessions, no <$74 round-trip) **but only 1 of ≥2 required fresh countable legs fired** (war-risk surge counted; transits + P&I/JWC had no fresh Fri print = non-countable; sanctions down-weighted per the ratified spec). Verdict: DENY → energy tail reverts to fragile-watch.

**This is the mismatch:** LIQ-05's own falsifier text defined "Brent denies" as *round-trip <$74 or legs walking back within 48h* — neither occurred. The level held; nothing walked back. The actual DENY mechanism was a **different, narrower failure**: BRENT's ratified spec requires ≥2 *fresh* corroborating legs and only 1 fired. LIQ-05 did not anticipate this third outcome (level-holds-but-insufficient-fresh-corroboration) when it bifurcated the world into confirm/deny.

**The surviving leg:** 10Y >4.50 — `GATE-TERRY-ARM2` shows **3-of-5 OFFICIAL** closes ≥4.50 (7/7 4.55 · 7/8 4.56 · 7/9 4.54, FRED DGS10) with a 4th provisional (7/10 ^TNX ~4.57, DGS10 unposted as of this writing). This leg is holding, not denied.

### Net state

- The CONFIRM branch **cannot complete** — it required Brent AND 10Y; Brent's leg is formally DENIED, so the upside (275-280 retrace via BETA) path is foreclosed as pre-registered.
- The FALSIFIER branch's **literal trigger text did not occur** (no round-trip, no walk-back) — grading the downside path ("continues retreating toward 260") at the letter would be citing a mechanism that didn't happen, even though the practical upshot (Brent leg fails) rhymes with it.
- Current HY OAS tape does **not** cleanly support either scripted path: last verified 270bps [7/8], up from 267 [7/7] — a small uptick, not a clean retreat toward 260, and nowhere near 275-280.

### Proposed re-scope options (for PROME/Will sign-off — NOT applied)

**Option A — NO-GRADE / VOID, re-register a cleaner successor.** Grade LIQ-05 as **VOID (premise-mismatch)**: the pre-registration's binary branch structure didn't anticipate BRENT's actual DENY mechanism (insufficient-fresh-legs, not round-trip/walkback). Void it explicitly rather than force a fit. Re-register a LIQ-06 with the world as it now stands: Brent formally DENIED (energy leg OFF), 10Y holding-to-completing (rates leg ON, live) → single-leg prediction: does HY OAS drift with the surviving duration leg alone (no oil co-driver) into CPI 7/14? This is the cleanest option — avoids retrofitting a result onto text that didn't anticipate this branch.

**Option B — Formal partial grade at the letter.** Grade the CONFIRM branch **NOT-MET** (Brent leg denied, conjunction fails by construction — mechanical, not a judgment call) and separately grade the FALSIFIER branch **NOT-MET-AT-THE-LETTER** (its specific triggering language didn't occur) but note the **practical direction converges** with the falsifier's spirit (Brent leg gone) even though the mechanism differs. Net grade: **MISS-BY-CONSTRUCTION** (neither scripted path completes), logged with the distinction preserved so it doesn't read as silent death. Closest to "formal partial grade."

**Option C — Reweight, don't grade yet.** Treat DENY as removing one leg's *support* without removing the possibility entirely (BRENT's own re-arm condition is "2nd independent fresh Iran leg alongside war-risk + level >$75" — still live, not closed permanently). Leave LIQ-05 **OPEN**, degrade confidence from 55%→lower given one leg is out, and grade formally only at the 7/21 window (original 5-10 session target) or on CPI 7/14, whichever comes first — with the CCC/BB co-widening diagnostic reweighted to depend on rates-only beta, not the oil+rates dual mechanism the diagnostic was built for.

**Recommendation (not a decision — flagging for Will):** Option A is cleanest — it names the premise mismatch honestly rather than stretching either branch to fit, and hands PROME a fresh, correctly-scoped prediction for the CPI week. Options B/C are defensible if Will prefers not to void a numbered KB/prediction row.

**Not done this sweep (per instruction):** KB-LIQ-071 thresholds/text were NOT rewritten. `workbook/PREDICTIONS.tsv` LIQ-05 status was NOT changed from OPEN.

---

## 2. Gate-row cross-check — PROME `GATES.tsv` vs LIQUID KB/STATUS

| Gate | GATES.tsv state (last_checked) | LIQUID KB/STATUS state | Match? |
|---|---|---|---|
| GATE-HY-REKILL (<260 ×2 closes) | LIVE, auto-watched (7/9) | STATUS: no fire, 270 vs <260, needs 2 fresh sub-265 closes | ✅ Match |
| GATE-LIQ-069 (AI-HY re-arm) | LIVE (monitored; **7/9: BB 157**, tightened, no signal) | STATUS 7/10: NOT-FIRED/MONITORED (**BB 160bps [7/8]**) | ⚠️ **Drift** — same 7/8 obs cited as 157 in one place, 160 in the other (3bp). Not sequencing (157→160 tick is documented elsewhere as a real move from 7/7→7/8), so this looks like GATES.tsv citing a stale/earlier pull of the same date's data rather than a fresh later tick. Flag to PROME to reconcile which figure is canonical for the 7/8 obs. |
| GATE-LIQ-072 (IG mispricing re-arm) | LIVE (monitored, registered off SpaceX verdict) | STATUS: WATCH, IG OAS 76bps / basis 194bps [7/8], flat | ✅ Match |

**Latest HY OAS per PROME's stated verification (task prompt):** 270 [7/8], path 283[6/26]→267[7/7]→270[7/8] — matches LIQUID's own STATUS/KB text exactly. No drift there.

---

## 3. Unconsumed inbox items

| Item | Source | Dated | Age | Disposition |
|---|---|---|---|---|
| `2026-07-10_from-PROME_ask8-first-class-boot-slot.md` | PROME (relaying DAEDALUS) | 7/10 | 1 day | **Unconsumed.** Owed build: re-home 5 orphaned EXPECTED_SIGNALS types (FHLB stress, sponsored-repo, MMF WAM, FTD spike, CCY-basis) into a live `workbook/` tracker on the LABOR/SAM template. Explicitly asked for a "first-class next-boot slot," already slipped once (PAT-041 pattern). **Not built this sweep** — this is a Medium build, analytic/canon-adjacent, correctly deferred to a dedicated boot slot per the triage-only scope of this task. Flag: this is now the 2nd session it's sat unconsumed since flagged 7/10; risk of a 2nd slip if not given the dedicated slot next boot. |
| `2026-07-11_from-DAEDALUS_midas-safehaven-seam.md` | DAEDALUS | 7/11 (today) | 0 days | **FYI only, no action required.** New MIDAS agent owns gold/silver safe-haven flow (GSR >95 = risk-off); seam is clean (MIDAS routes LIQUID a signal when its monetary channel fires). No integration work owed — noted. |
| `inbox/WALTER/SIG-W-20260710-004.md` (JGB ALM-buyer-not-forced-seller, DEWEY prompt 08) | WALTER | 7/10 | 1 day | **Unconsumed — not yet board-logged or moved to processed/.** Content: repatriation channel reframe (ALM-buyer base = demand floor, not repatriation trigger, under an orderly grind; reverse-carry re-arm needs the disorderly >4.5% J-GAAP-impairment path). This is consistent with SAM's own 7/9-7/10 consumed overlay (JGB floor ~4.0%, lifer non-re-entry resolved FALSE) already sitting in STATUS Open Monitors — likely a **duplicate/corroborating** signal of ground already integrated, but formally still sitting unprocessed in the WALTER lane. Per this task's TRIAGE-FIRST scope, board_log.tsv processing (disposition + `git mv`) was **not executed** — proposing "noted, corroborates already-integrated SAM 7/2 overlay" as the disposition for the next normal spawn to apply. |

---

## 4. Ungraded/overdue KB entries + ledger drift

- **LIQ-05** (KB-LIQ-071) — covered in §1, the blocking item.
- **LIQ-04** (BSL AAA >SOFR+150, H2 2026, 25% confidence, registered 7/1) — OPEN, no interim data pull since registration. Not overdue by its own timeframe (H2 2026), but flagging that no PitchBook LCD monthly-average check has been logged yet this session-run; next natural check-in is with July LCD wraps.
- **Mandate-extension SIG (6/27, PROME coverage-gap, Will-approved) — PARTIALLY built, contrary to LIQUID's own STATUS text calling it "integrated 7/1":**
  - **SECONDARY (IG OAS + HY-IG basis)** — fully wired, live in `scripts/boot.py` (automated FRED pull, thresholds in Triggers table). Done.
  - **TERTIARY (EU credit contagion vector)** — the SIG asked specifically for **peripheral sovereign spreads (Italy/Spain/Greece)**. What got built instead is a **Euro HY *corporate* OAS** proxy row in `boot.py` (line ~152-161) — a different instrument than requested, and the "reconcile with BOND to one shared view" instruction from the SIG has not visibly happened (no cross-reference to BOND in STATUS on this leg). Flag: scope substitution, not full compliance.
  - **PRIMARY (funding-market microstructure — the SIG's #1-ranked, "highest-value gap in the whole network" item)** — this is the least-built leg despite being ranked top priority. Only **one manual, one-time datum** exists: NY Fed PD dealer inventory (PDPOSCSBND-G5L10, "+$359mm 6/3 → −$825mm 6/17"), now **~24 days stale** with no repeat pull. Repo GC-vs-special, SOFR-dispersion-as-a-recurring-series (the 75th/99th pct rows exist but only get pulled ad hoc, not a standing trend), MMF flows, haircut indices, and PB funding-constraint signals were never wired. This matches LIQUID's own `MEMORY.md` NEXT SESSION carry-forward #4 ("Microstructure build stage-2... deferred from 7/1"), so it's a self-acknowledged gap, not a surprise — but it explains why `PROME/DOCKET.tsv` line 49 still marks LIQUID's mandate-extension SIG **"still pending"** while LIQUID's own STATUS.md claims "integrated." **Both are partially right: docs/scope integrated, PRIMARY-leg data build did not happen.** Propose PROME update DOCKET wording to "PARTIALLY integrated — SECONDARY live, TERTIARY substituted-proxy, PRIMARY (highest-priority) leg thin/stale" rather than a flat "pending," and LIQUID treat PRIMARY-leg wiring as a real backlog item, not closed.
- **`workbook/VX.tsv` and `workbook/FLOW.tsv` — severe silent-rot, root CLAUDE.md Data Hygiene violation.** Neither file has a FROZEN banner nor a boot-time staleness alert, and neither is read by `scripts/boot.py`. Sample: `VX-LIQUID-6.04` (IG issuance) dated 2026-03-04; `VX-LIQUID-6.08` (DIFC) dated 2026-03-12; `VX-LIQUID-7.01/7.02/7.06` (China/Japan/Belgium TIC) all stamped "Jan 2026 TIC" — three TIC releases old (Apr, likely May/Jun) with no update, despite STATUS.md discussing April TIC and the upcoming 7/16 June TIC release. `FLOW.tsv` rows are similarly Feb-Apr vintage (FLOW-LIQUID-6.01 through 6.05 stamped Mar 12, FLOW-LIQUID-7.02 stamped an "Apr 20-25" watch window now three months past). Per root CLAUDE.md's rule, these are candidates for **either FROZEN-with-banner or a live refresh** — right now they're the silent-rot middle the rule exists to prevent. Proposing: FREEZE both with a banner pointing to STATUS.md/boot.py as canonical, since neither appears to be an active workflow (KB.tsv has clearly superseded them as the durable-findings track — KB.tsv is current through KB-LIQ-074, 7/10).

---

## 5. Gaps — credit-side coverage that should be watched into CPI week (7/14) and monolines (7/15-22) but has no home yet

1. **No consumer-ABS / credit-card / auto-loan spread tracking.** The monolines window (SYF/ALLY/COF/AXP, REGINALD/CARL/NEXUS-owned, "un-maskable M-08 transmission test") is a consumer-credit fundamentals story, but LIQUID owns the market-based credit-spread confirmation layer (HY/IG/CLO) and currently has **no instrument for consumer ABS spreads** (credit-card ABS, auto ABS OAS) that would show whether monoline stress is pricing into the plumbing LIQUID watches. This is a gap between LIQUID's dashboard and the monolines catalyst it's tagged to in HEARTBEAT/DOCKET.
2. **EU peripheral sovereign spreads remain untracked** (see §4) — if the CPI-week rates move (10Y arm-#2 completing Monday) has any EU-contagion echo, LIQUID has no live row to see it; only a corporate-Euro-HY proxy exists.
3. **No CPI-day-specific credit playbook.** CPI 7/14 is repeatedly named as "the hinge" across PROME/HEARTBEAT and is LIQ-05's/its-successor's grading date, but there is no written LIQUID row for "what HY OAS should do on a hot vs. soft CPI print" (analogous to the existing NFP/FOMC decision-tree pattern LIQUID has used before, e.g. the now-retired FOMC_TIC_DECISIONTREE). Given the pre-registration discipline this fleet uses (grade before the fact, not after), a short CPI-day pre-reg would be in-pattern and is currently missing.
4. **Funding-microstructure PRIMARY leg stale entering CPI week** (see §4) — the original mandate SIG's own argument was that this leg validates or pre-empts the HY>280 trigger precisely in a stress scenario; heading into a hinge week with a 24-day-stale dealer-inventory datum and no repo-dispersion trend line is the least-defensible moment for that gap to persist.

---

## EXECUTION ADDENDUM (same day, ~15:30-16:15 ET — Will decided, PROME-relayed)

Items 1 (Option A: LIQ-05 VOID + LIQ-06 registered, KB-LIQ-075), 3 (ask-8 tracker built → `workbook/EXPECTED_SIGNALS_TRACKER.md`), 5 (VX/FLOW FROZEN), 6-partial (CPI-day pre-reg written → `workbook/CPI_20260714_CREDIT_PREREG.md`; consumer-ABS row NOT approved/built) executed; item 4's STATUS-side correction applied (mandate claim → PARTIAL). Item 2 (BB-OAS drift) + DOCKET wording = PROME's side. The list below is preserved as the original proposal record.

## Summary of proposed items (original sweep output — see addendum above for what was subsequently executed)

1. Re-scope/grade KB-LIQ-071 / LIQ-05 per one of Options A/B/C (§1).
2. Reconcile the GATE-LIQ-069 BB-OAS 157-vs-160 [7/8] figure drift between `GATES.tsv` and STATUS (§2).
3. Give ask-8 (5-orphan-signal tracker) its promised dedicated first-class boot slot next session — 2nd session sitting unconsumed (§3).
4. Update `PROME/DOCKET.tsv` line 49 wording on LIQUID's mandate-extension SIG from flat "pending" to "partially integrated" (§4), and treat the funding-microstructure PRIMARY-leg build as live backlog, not closed.
5. FREEZE `workbook/VX.tsv` and `workbook/FLOW.tsv` with a banner (or schedule a refresh) — currently silent-rot (§4).
6. Consider a consumer-ABS/credit-card spread row and a CPI-day credit pre-reg ahead of 7/14-7/22 (§5).
