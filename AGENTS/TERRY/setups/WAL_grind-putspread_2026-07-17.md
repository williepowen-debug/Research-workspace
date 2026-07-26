# TRADE CARD — WAL — Long Put Spread (grind expression)
**Date:** 2026-07-17 · **Updated:** 2026-07-26 (**owner repointed to the WAL agent** — DAEDALUS 7/25, WP-W4) · *prior update 2026-07-21 (REGINALD confirm consumed; print gate staged)*

> ### 🔄 OWNER CHANGE — 2026-07-26 (ACK to DAEDALUS 7/25)
> **WAL was promoted out of REGINALD** (`AGENTS/REGINALD/WAL/` → `AGENTS/WAL/`, Will-approved 7/22, cutover 7/25 — review: `AGENTS/DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md`).
> - **Adjudication owner for this card is now the WAL agent** (`AGENTS/WAL/`). Grind-intact-vs-broken calls route there; its thesis **v2.3 (grind INTACT-but-NARROWED**, per the Q2 Stage-2 grade) is the adjudication basis.
> - **REGINALD remains the cohort/KRE context source — NOT the WAL-grind adjudicator.**
> - **Position canon moved:** `AGENTS/WAL/POSITIONS.md` is now canonical for WAL strikes/expiries (7/20-export-current: 77.5P Aug-21 ×1 + 67.5P/70P Sep-18 core). **Use it, not the §7 snapshot below, at fire-time** — with a fresh broker export (rules #4/#6).
> - Sep-18 core expiry sits on WAL's STATUS §EXPECTED SIGNALS; fire-time reshapes still run TERRY rules #4/#5/#6/#7.
> - **No economics change.** Everything below is unchanged; only the routing pointer moved. **REGINALD attributions in the historical blocks stay as-written** (delivered-record canon) — they are an accurate record of who ruled what, when.

**Thesis owner:** **WAL agent** (`AGENTS/WAL/`, thesis v2.3) — regional-bank credit transmission / Will — **NOT TERRY.** ✅ **Thesis CONFIRMED 2026-07-20 by REGINALD when it still owned the queue** (`AGENTS/REGINALD/outbox/2026-07-20_to-TERRY_wal-grind-thesis-confirm.md`, v2.2.1: bear-medium 25, EV $68.93, PT $50–68; REG-26 crash tell only 33% → **grind is the base case by construction**; Jan-2027 tenor ruled CORRECT, NOT the Dec-2027 LEAP — meaningful re-rating window is Q2-26→~Q1-27 ≈ 2–3 quarters). **That confirm carries forward; re-confirmation is not owed — but any FRESH adjudication goes to WAL.**
**Terry verdict:** **CONDITIONAL** (structure + thesis both confirmed; gated on the §2b PRINT GATE + first green WAL day + live marks)
**Confidence in trade STRUCTURE:** High · **Confidence in thesis:** consumed not re-underwritten (REGINALD's 7/20 grade, now carried by the WAL agent at v2.3)
**Status:** NOT armed, NOT fired. Entry decision node = the 7/21 AMC print (gate below).

## 1. One-line setup
Express a **slow** WAL bear/grind thesis (credit transmission re-rates the name 10–18% over 2–4 quarters) with a **reachable, properly-tenored put spread** instead of deep-OTM near-dated lottery puts — the structural error Part B diagnosed in the current book.

## 2. Preconditions
- ✅ **REGINALD confirmed the WAL bear/grind thesis 7/20** — slow credit-transmission re-rating (criticized/SM build → classified → NCOs lag), 10–18% over 2–4 quarters. The crash path (REG-26) is a **minority tail (33%)** and is already covered by the legacy deep Sep puts + RH 77.5P — this card deliberately does NOT express it.
- **Entry is AFTER the 7/21 AMC earnings print** — avoids the pre-print event premium (Part A: WAL front-month carries ~+4–5 vol pts that crush post-print). A grind expression does not need the catalyst.
- WAL still in roughly the **78–85 zone** (has NOT already broken down). If WAL is already <~77, the shallow-strike grind entry is gone — do not chase. *(Live 7/21 ~15:12 ET: WAL $79.93, −1.28% into the print — in-band.)*
- **Rule #6:** buy the puts on a **green day** for WAL (relative strength up), not into a red-day flush.
- What must NOT be happening: WAL breaking to new highs / thesis retracted / a fresh systemic crash already underway (different trade).

## 2b. ★ PRINT GATE — grade the 7/21 AMC print BEFORE any entry (REGINALD 7/20; necessary-but-not-sufficient upgrade to "first green day + 78–85")
**Read the print on the CREDIT lines, not NIM/AOCI** — REGINALD's ZION grade says the tier's non-credit axis is QUIET (AOCI improved, TBVPS up, NIM flat), so a WAL selloff is unlikely to be balance-sheet-driven; the grind thesis is validated or killed on criticized / NCO / the $99M life-sci credit. Run `grade_print.py WAL --nco-bps <adjusted> --basis adjusted --life-sci-chargeoff <yes|no> …` as the mechanical layer.

**→ LAPSE (do NOT enter) if ANY of:**
- [ ] Criticized/special-mention **falls materially** (the $947M classified + $403M SM roll DOWN) — REG-24 disconfirm
- [ ] The **$99M life-sci credit is CURED/upgraded** — REG-26 disconfirm
- [ ] **NCO <40bps with NIM expanding** + crowded-short-unwind relief rally

**→ ENTER (on the first GREEN WAL day, WAL 78–85, debit ≤ ~$3.75) if the print CONFIRMS the grind:**
- [ ] Criticized/SM **builds or holds**, AND
- [ ] The $99M is **disposed A/B** (charged off, or extended-not-cured), AND
- [ ] NCO **in-or-above the 40–55bps** priced band

**Execution flags at entry (REGINALD sizing-side, Will/TERRY gate):**
1. **Net the 77.5 strike** — the spread's long 77.5P Jan-27 stacks with the live RH WAL 77.5P Aug-21 (same thesis, two tenors: Aug = decaying event leg, Jan = structural grind leg). If consolidating to one vehicle, the Jan spread is the better grind expression.
2. **Confirm the Sep-18 67.5P is actually the leg being rolled** — closing long 67.5 (Sep) + opening short 67.5 (Jan) = clean net-short the strike. Leaving a long 67.5P un-rolled creates an unintended calendar (long AND short the same strike across expiries).
3. **Roll, don't stack** — this replaces the dying Sep 70P/67.5P; it is NOT additive WAL exposure.

## 3. Entry
- **Trigger:** thesis-owner confirmation + first green WAL day *after* the 7/21 print.
- **Preferred entry zone:** WAL ~80–85 (spot 82.3 as-of 14:34 ET 7/17).
- **Do NOT chase:** if WAL < ~77 before entry (already grinding), or if the net debit > ~$3.75 (event-vol not yet normalized).

## 4. Structure
- **Primary — PUT SPREAD:** **long WAL 77.5P / short WAL 67.5P, exp 2027-01-15 (~182 DTE).**
  - Indicative net debit **~$3.45** (long 77.5P ~$6.05 / short 67.5P ~$2.60), as-of 7/17 14:34 ET — **PULL LIVE AT ENTRY.**
  - Max value **$10.00** (WAL ≤ 67.5 at expiry) → **max profit ~$6.55 on ~$3.45 risk ≈ 1.9:1.**
  - **Rationale:** Part B proved the 67.5 strike is rarely reached (3y realized-reach ~7%), so **selling it forfeits almost nothing and halves the cost** of the reachable 77.5 strike. Textbook grind structure.
- **Alternative — OUTRIGHT 77.5P Jan-2027 (~$6.05):** uncapped downside, but **$605/contract BREACHES the $500 max-loss cap at even 1 lot** → not usable as-is unless entry is materially cheaper post-crush or strike is raised. The spread is the sizing-disciplined choice.
- **Tenor note:** ✅ **Jan-2027 CONFIRMED (REGINALD 7/20)** — resolution windows cluster Q2-26→~Q1-27 (REG-25 Q2-or-Q3 NCO, REG-24 office-classified by Q3, IQHQ/OZK Aug/Oct). The Dec-2027 LEAP is ruled OUT: "if it hasn't re-rated by early 2027 the grind thesis is itself substantially weaker."
- **Why this beats the held book:** 77.5P (5.8% OTM) reachability **P(ITM) 46% / emp 22.6%** vs the held 67.5P Sep-18 (18% OTM) **17% / 7.2%**. Real delta — gains on any grind toward strike, not just a terminal cross.

## 5. Risk
- **Max loss budget:** net debit **~$345 / spread (1 contract)** = full loss if WAL > 77.5 at expiry. **Within the $500/card cap.** Size = **1 contract** (leaves headroom; do not exceed $500).
- **Invalidation:** (a) **thesis** — REGINALD retracts the WAL bear thesis; (b) **price** — WAL sustained **> ~88–90** / new highs (grind thesis wrong); (c) **time** — see time stop.
- **Stop/exit rule:** mechanical — exit if invalidation (a) or (b) triggers; otherwise manage to targets/time stop.
- **Gap/event risk:** the 7/21 print is the main one and is **deliberately entered around** (post-print). Secondary: sector-wide bank repricing gaps (favorable) or a bank-relief rally (adverse).

## 6. Target / management
- **Target 1:** WAL → 77.5 (long strike) — spread starts building intrinsic; take **partial (⅓–½)** if the spread **doubles** (~$6.90+).
- **Target 2:** WAL → 67.5 (short strike) = max value ~$10; scale out into it.
- **Roll rule (pre-registered):** this is a **GRIND, not a tail** — workflow §3d/§3c: the TT-02 terminal-window "hold to expiry" logic does **NOT** apply. Ordinary management. If thesis intact but slow near expiry, **roll duration** (rule #7) to a further-dated spread; do NOT stack more deep-OTM lottery tickets.
- **Time stop:** if by **~mid-Nov 2026** (roughly half the tenor) WAL has not begun grinding lower AND the thesis has stalled → reassess/exit. Spread theta is slower than an outright, so this is forgiving by design.

## 7. Why not / counter-trade
1. **Concentration:** Will **already holds WAL 70P/67.5P Sep-18** (~$95 mkt as of the 7/24 refresh, −92/−95%) plus a broad regional-bank put basket. This card should be a **re-expression to roll the dying Sep deep puts INTO** — not additive WAL exposure stacked on top. Adding fresh WAL on top of the basket concentrates a single-name and the shared bank-de-stress falsifier. **⚠️ (PROME 7/20): Will also holds a day-trade RH WAL 77.5P Aug-21 — the SAME strike as this spread's long leg.** Sizing must net against that existing 77.5 line (don't double the strike). *(Thesis has since landed — REGINALD confirmed 7/20, adjudication now carried by the WAL agent at v2.3. **Position truth at fire-time comes from `AGENTS/WAL/POSITIONS.md` + a fresh broker export**, not from the figures in this line.)*

### ★ EFFECTIVE-N — independence audit
*Added 2026-07-26 for compliance with `RISK_SCORING.md` §2b (adopted today). This card predates the field; the concentration paragraph above was already an informal version of it.*

| Field | Entry |
|---|---|
| **N_claimed** | **4+** — WAL Sep 70P · WAL Sep 67.5P · RH WAL Aug-21 77.5P · this spread · (+ the wider KRE/OZK basket behind it) |
| **Shared antecedent** | 🔴 **Regional-bank credit failing to crack.** Every WAL line *and* the whole KRE/OZK basket die to the same fact. The 77.5 strike is additionally **duplicated** between this card's long leg and the existing RH Aug-21 line. |
| **EFFECTIVE N** | **N_eff = 1** — one thesis, one falsifier, expressed four-plus ways on one ticker inside a basket that already expresses it. |
| **Sizing reference** | **Confirms the card's existing ROLL-NOT-ADD ruling, and now with a number behind it.** This must be a *re-expression* of dying exposure, never an addition. Any version of this that raises net WAL exposure is sized to `N_claimed`, not `N_eff`. |

> **This card is the closest thing the desk has to a worked example of why the field exists.** The KRE/OZK/WAL basket is ≈**−$5,291** across three names sharing one falsifier (`RISK_SCORING.md` §2b) — WAL alone is ≈−$1,425 of it. The roll-not-add discipline was already the right call on structural grounds; `N_eff = 1` is why.
2. **Structure supplies no edge** (options ~fairly priced for single names, Part A/RESEARCH): 100% of EV must come from REGINALD's thesis being right on direction AND rough timing. If the thesis is only "banks feel weak," that is not enough.
3. **Slow thesis risk:** transmission could take longer than Jan-2027 — the reason to consider the LEAP, and the reason this is a spread (cheaper to roll) not an outright.
4. **Best reason to pass:** banks (WAL included) have been resilient; a shallow reachable strike still needs the grind to actually start, and it hasn't.

## Decision
This is a **CONDITIONAL** card: structure is clean and data-backed. Gate status as of 2026-07-21: (1) ✅ REGINALD confirmed the grind thesis 7/20; (2) ⏳ the 7/21 AMC print must pass **AND grade non-disconfirming per §2b**; (3) ✅ WAL in-band ($79.93 live 7/21); (4) ⏳ live marks must confirm ~$3.45 debit (≤$3.75 no-chase) on the first green WAL day post-print. **Preferred use = the roll target for the dying Sep WAL puts, not additive exposure — net the 77.5 strike against the RH Aug-21 77.5P (§2b flags).**

**APPROVAL REQUIRED — Will must approve/reject before execution.**
