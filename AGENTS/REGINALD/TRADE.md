# REGINALD — TRADE SURFACE

> **LIVE — rebuilt 2026-09-29 ~20:1x ET on Will's word (*"Do it now"*), replacing the March-2026 document (FROZEN 7/09; archived verbatim → `archive/TRADE_frozen_2026-03-07_archived_2026-09-29.md`, crc32 `ab819e73`).** This file carries the trade THESIS, the triggers by name, the refuters and the anti-trades. It carries **no marks and restates no strike it does not own**: position truth is off-repo (Will/broker); the structured mirror is `FORGE/STATUS.md` (PROME/ANVIL, last reconcile **2026-09-29 intraday**); this desk's structural ledger is `POSITIONS.md`. **Trade construction = TERRY; approval = Will (root rule #5).** Re-check size at any append (READ_CAP budget 32,550 B).

## 1. What this desk's trades are a bet on (state 2026-09-29)

**Thesis (STATUS-canonical since 8/13):** regional-bank credit stress is **CONCENTRATED, not tier-wide** — 3 elevated names of 14 (FLG 6 · EGBN 5 · AMTB 5, matrix v2.0), the CRE cut narrows to FLG · EGBN · OZK, and the cross-bank Q2 filings showed CRE bad-loan rates FALLING (2.46% → 2.23%). The index expression (KRE) is therefore **tail insurance on a sector repricing**, not a directional call on cohort credit.

**What the tape is doing (attribution 9/29, `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`):** 8/14 → 9/14 was small-cap/market beta with **no** financials component; 9/15 → 9/29 was a **financials-sector move led by the LARGEST banks** (14-name size sort ρ −0.72), in which KRE beat its factor loading and my credit ranking sorted the WRONG way (+0.48). Credit instruments (preferreds, BDCs, HY ETFs) barely moved. ⇒ **A KRE put today is a bet that the large-bank financials repricing continues and drags regionals at ~0.85 beta. It is NOT yet a bet on regional credit.** The credit-shaped exceptions are FLG and VLY (NYC rent-regulated multifamily; worst in both legs; FLG ladder ORANGE 9/28).

**What would make it a credit bet:** B-tier OAS holding >300 into >330 · loans to non-bank financials STALLING in H.8 · a Q3 print cluster (~10/20–28) showing breadth at the mid-pack (DOCKET L180) · an 8-K at a thesis name. None has happened (H.8 through 9/16 and H.4.1 through 9/23 all 🟢).

## 2. Live legs — pointers, not restatements

| Leg | Owner of the record | State (per FORGE 9/29 reconcile) | Guard / rule |
|---|---|---|---|
| `KRE $60P Dec-18-2026 ×5` | `POSITIONS.md` · FORGE | LIVE, 80 DTE, deep OTM (KRE $69.83 [9/29]) | `REG-T-01` KRE <$60 UN-FIRED; tripwire close ≤$66 → TERRY |
| `KRE $60P Sep-30-2026 ×2` | `POSITIONS.md` · FORGE | **Expires Wed 9/30 — LAPSE ruled (WQ-168 ⑥)**, −14.1% OTM | Write back 10/1 from the broker export, never the tape |
| `WAL $70P Dec-18-2026 ×1` (RH) | `../WAL/` · FORGE | LIVE, the ROLL70 duration roll (filled 9/02 @ $2.20) | `GATE-TERRY-ROLL70-EXIT` = `REG-T-02` exit: WAL ≥ $81.90 ×3 closes — **0-of-3 after 20 graded closes** (`registry/REG_T02_EXIT_LOG.tsv`) |
| `HBAN $16P Oct-16-2026 ×2` | `POSITIONS.md` · FORGE | **ITM** (HBAN $15.27 [9/29]); the 7/18 "exit-thesis dust, rides to expiry" premise FAILED | Card `MGMT-HBAN16P-OCT16`; **Will rules by Wed 10/14 (WQ-302)** |
| `APO $95P Dec-18-2026 ×1` | `POSITIONS.md` · FORGE | LIVE, 80 DTE; BROCK thesis vehicle | Will ruled HOLD 8/13; vehicle-mismatch flag live (BROCK) |
| `KRE $25P Jan-15-2027 ×1` (RH) | FORGE only | Deep-OTM lottery, entry never recorded (D-54) | Not thesis-scope |

**Open card(s):** **KRE-put ADD — Will asked 9/29 (~18:2x, ~19:5x ET); two REGINALD packets in `AGENTS/TERRY/inbox/` (`f6a95855b`… `8a850dc9f`); TERRY constructs at its 9/30 wake (DOCKET L255). Loop closes here + `POSITIONS.md` when the card id and Will's decision land (root rule #10).**

## 3. Triggers this desk grades (levels live in `STATUS.md` §THRESHOLD STATUS — never here)

| Trigger | Letter | State 9/29 | Consequence |
|---|---|---|---|
| `REG-T-01` | KRE < $60 | UN-FIRED, 14.1% away | 🔴 to ALL; the KRE puts' thesis level |
| `REG-T-02` | WAL < $78 | **FIRED since 9/1 (cycle 2)**; exit ≥ $81.90 ×3, run 0-of-3 | Guards ROLL70; 2-of-3 → packet TERRY |
| `REG-T-03` / `-04` | HY OAS > 320 ×3 / > 350 | 302 [9/28] — 18bp / 48bp away | Credit transmission — **run the bank-credit cross-check first** (`reports/2026-07-30_bank-side-HY-attribution.md`) |
| `VX-REG-18.04` / `18.05` | CCC/HY > 3.6× ×3 · B-tier > 300 / 330 / 380 | HARD-FIRE (3.795×) · **B 309 = YELLOW, first >300 9/28** | Escalation SENT 9/26; watch, not re-escalate (Will 9/26) |
| `VX-REG-6.03` | FLG ladder −10 / −15 / −20% vs $14.24 | **ORANGE** ($12.04 [9/28]; RED $11.39) | RED → packet PROME + FLG same session |
| `REG-T-06` | FHLB advances > $700B ×3 qtrs | leg 2 of 3 ($810.7B [6/30]) | Q3 print (~Nov) fires it — a LEVEL, not a signal, without composition |
| Claims (LABOR) | > 300K | 197K [w/e 9/19] | all ORANGE banks → RED |

**Exit rules** (STATUS §EXIT RULES, unchanged): HY < 260 is a REVIEW trigger, not an auto-exit (Will 6/19); BTFP-2.0 = thesis broken (auto-exit); CRE-channel anchors (WAL NCO ex-fraud < 25bp AND no office migration; office CMBS-DQ flows reversing 2 prints + bank CRE-DQ tier-creep reversing).

## 4. Refuters for any bank put on this desk (write them on the card)

B-tier OAS back **< 300** (a 9/15-style reversal) · HY back **< 280** · KRE reclaims **$72.74** (the 9/16 gap-down close) · a clean Q3 print cluster (no mid-pack breadth, L180) · H.8 non-bank lending re-accelerating with small-bank deposits stable · LABOR's bull-side kill firing (Sep NFP ≥ +150K, 10/2) removes the labor leg entirely.

## 5. Anti-trades (tempting, and the evidence says no)

- **Single-name puts on my top-scored names as a "credit" expression.** EGBN and AMTB (matrix 5) were the two BEST performers of the selloff (−2.9% / −0.2% vs KRE −10%); the market is not pricing my ranking. A credit thesis needs a print, not a score.
- **Adding on a red day.** Root rule #6: puts on GREEN days. Breaking it needs the direct measurement written on the card before the fill (`AGENTS/TERRY/RISK_RULES.md`); "the window is closing" is a chase. 9/29 was red.
- **Treating the March document as live.** Its eight-channel frame, its April earnings plan and every leg in it are dead (archived with crc above). Cite `STATUS.md` for thesis state.
- **Reading a HY level as bank transmission.** The 7/27–29 sustain over 280 was BANK-ABSENT; HY sits downstream of bank credit in my chain. Cross-check first.
- **Trimming for size when the thesis is intact.** Root rule #7: roll duration, don't trim (trimming = thesis broken). Any roll rides on TERRY's card.
- **Chasing the deposit-flight narrative with a trade.** "Agentic bank run" (Slok 9/27) is a mechanism frame with no flow data; it is a WQ-318 question (deliver 10/9), not a card input.

## 6. History — what this desk's names have done to the book

Jun-18 / Jun-30 clusters cleared (FORGE 7/16) · Jul-17 legs lapsed OTM (WAL $65P, ZION $57.5P, FLG $13P ×3) · **Aug-21 `KRE $60P ×3` lapsed worthless — broker-confirmed on the FORGE 9/29 ledger (five Aug-21 rows, realized −$2,816.72 book-wide)** · WAL Sep-18 pair (`../WAL/`) expired 9/18, broker-confirmed 9/21, −$1,519.34 · SSB $90P and KRE $70P = the two unrecorded-exit phantoms that built the POSITIONS-first rule (`LESSONS.md`). **Lesson the book keeps teaching: deep-OTM index puts with sub-quarter tenor have lapsed four times in a row; the live expressions that have paid or held are the duration roll (WAL Dec-18) and the ITM HBAN leg nobody expected.**

---
*Owner REGINALD. Levels → `STATUS.md`; strikes/qty → `POSITIONS.md` + `FORGE/STATUS.md`; construction → TERRY; approval → Will. Rebuilt 2026-09-29; prior file archived verbatim (crc above).*
