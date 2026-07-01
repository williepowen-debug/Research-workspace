# Bank-Put Book — Reshape / Duration-Roll Proposal
**Date:** 2026-06-26 ~10:55 ET · **Author:** Claude Code Prome · **Status:** PROPOSE-ONLY — needs Will [Approve] (rule #5). No execution. *Refreshed 2026-07-01: WAL Q2 date corrected Jul-30→**Jul-16** throughout (per the 6/26 correction in ACTIVE_DECISIONS); dead pointers repointed. Still SHELVED_PENDING_TRIGGER (HY>280 sustained / WAL Jul-16 print).*
**Mandate:** Will 6/26 — "reshape within budget; build the full roll proposal." Reshape = recycle decaying premium, **no new net risk**.
**Inputs:** current book (Will's broker snapshot, 10:33 ET 6/26 — position truth is off-repo, Will/broker direct; re-pull the live book at fire-time, rule #4) × live prices + live 2027 option chains (yfinance, ~10:50 ET 6/26).
**Thesis base:** the 2026-06-26 verification pass (Tiers 1–3) — thesis SURVIVES; realized transmission window = **Q1–Q2 2027**; the two live Q2-able exceptions = **(b) AOCI/rates + (c) WAL single-name**; path (a) consumer/broad-regional TRIMMED to ~15–22%.

---

## The core insight — the duration mismatch is PATH-SPECIFIC, not uniform

The book is positioned for a 2026 event; the thesis defers realized transmission to 2027. But the fix differs by path because the **catalysts** sit at different dates:

| Path | Catalyst | Correct duration | Current book | Action |
|---|---|---|---|---|
| **(c) WAL single-name** | **WAL Q2 print Jul-16-26** *(corrected from Jul-30, 6/26)* | Sep-2026 puts CAPTURE it | WAL 75 P Sep-18-26 (fresh), 70 P Sep, 67.5 P Oct | **KEEP** — already correctly dated |
| **(b) AOCI / rates** | slow rate grind, no single date | needs 2027 duration | TLT 85 P Sep-26 / 82 P Oct-26 (too short) | **ROLL → TLT 2027 puts** |
| **(a) broad regional** | Q2 prints Jul 16–22 | n/a — path TRIMMED | KRE/OZK/ZION/HBAN short-dated, deep-OTM, −65→−99% | **HARVEST** (recycle into b) |

**One line:** keep (c) — it's correctly dated; roll (b) to 2027 where the AOCI grind actually lands; harvest the trimmed (a) regional premium and recycle it into (b). That IS the duration roll (rule #7 — timeline uncertain, thesis intact), not a trim.

---

## Live reference (≈10:50 ET 6/26 — re-confirm at execution, rule #4)
KRE **$74.93** · WAL **$81.81** · OZK **$51.80** · ZION **$69.07** · HBAN **$17.81** · TLT **$87.21** · TBT **$34.28** · APO **$120.32**
Banks GREEN today (KRE +0.17%, WAL +0.52%) → buying put legs on green ✓ (rule #6).

---

## A. HARVEST — close for residual value (path-a regional, decaying)
These have real premium left but expire before the 2027 window and re-fund a TRIMMED path. Close and recycle.

| Position | Exp | ~Value (img) | Note |
|---|---|---|---|
| KRE 60 P | Sep-18-26 | $184 | recycle |
| OZK 45 P (×4) | Sep-18-26 | $140 | recycle |
| WAL... | — | — | (KEEP — see C) |
| KRE 60 P (×2) | Sep-30-26 | $66 | recycle |
| HBAN 16 P | Oct-16-26 | $30 | recycle (small) |
| TLT 85 P (×2) | Sep-18-26 | $176 | recycle → into 2027 TLT (path b roll) |
| TLT 82 P (×2) | Oct-16-26 | $80 | recycle → into 2027 TLT |

**Est. recoverable ≈ $675** (confirm against live broker marks; image values are a 10:33 snapshot, not authoritative — rule #3).

## A2. LET EXPIRE — don't pay commission (sub-$30 dead remnants)
KRE 65 P Jun-30 ($16) · KRE 63 P Jun-30 ($2) · KRE 60 P Jul-17 ($27) · OZK 42.5 P Jul-17 ($20) · ZION 57.5 P Jul-17 ($10) · WAL 65 P Jul-17 ($5). Commission ≈ value; let them die.

## B. HOLD (separate decisions, not part of reshape)
- **KRE 60 P Dec-18-26 ($276, ×3)** — closest existing to the window; HOLD or roll to KRE Mar-31-27 (optional, see variant).
- **KRE 25 P Jan-15-27 ($52)** — lottery, leave it.
- **APO 95 P Dec-18-26 ($245)** — PC-manager path, separate axis; not part of (b)/(c) reshape.
- **TBT (long, 14 sh)** — open-ended rate-up equity expression for (b); HOLD (no theta).

## C. KEEP — path (c) WAL is already correctly dated
- **WAL 75 P Sep-18-26** (fresh add, ~8% OTM) + WAL 70 P Sep-18-26 ($160) + WAL 67.5 P Oct-16-26 ($115). All capture the **Jul-16-26** print. No roll needed now. Re-evaluate after Jul-16: if the print delivers → harvest; if thesis intact but unrealized → THEN roll to WAL Jan-15-27.

---

## D. REDEPLOY — recycled premium → path (b) 2027 (live marks)

**Path (b) AOCI via TLT puts — cheap, liquid, IV ~10–11%** (rate selloff / TLT down = bank AOCI losses widen; 10Y 4.39, tracking 4.30→4.41):

| Strike | Exp | Mark (bid/ask) | OI | Moneyness | Note |
|---|---|---|---|---|---|
| TLT 85 P | **Mar-19-27** | 2.12 / 2.17 | 502 | ~2.5% OTM | near-money anchor |
| TLT 82 P | Mar-19-27 | 1.17 / 1.22 | 6,237 | ~6% OTM | more convexity/contract |
| TLT 80 P | Mar-19-27 | 0.78 / 0.82 | **38,245** | ~8% OTM | cheapest, most liquid |
| TLT 85 P | **Jun-17-27** | 2.55 / 2.66 | 30,740 | ~2.5% OTM | more time |
| TLT 80 P | Jun-17-27 | 1.01 / 1.08 | 93,270 | ~8% OTM | most time + liquid |

**Optional path-(c) 2027 roll (only if Will wants WAL duration NOW vs waiting for Jul-16):** WAL Jan-15-27 — but **expensive + illiquid**: 75 P 6.20/7.80 (20% spread), IV 47%, OI 25; 80 P 7.3/8.6, OI 263. Recommend NOT forcing this — the Sep WAL puts already capture Jul-16. Flagged for completeness.

---

## E. Allocation variants (within ≈$675 recovered, no new risk)

**V1 — (b)-roll, recommended.** Recycle all harvested premium into TLT 2027. E.g. 2× TLT 85 P Jun-17-27 (~$530) + 1× TLT 82 P Mar-19-27 (~$122) ≈ $650. Rationale: TLT is the cheapest convexity in the book (IV 10% vs WAL 45%), liquid, and (c) is already covered by the Sep WAL puts. Cleanest, most cost-efficient.

**V2 — balanced (b)+regional tail.** Split: ~$450 into TLT 2027 + roll the KRE Dec-26 ($276) → KRE Mar-31-27 67–70 P to keep a small regional tail alive through the Jul GATE. Rationale: retains optional path-(a) exposure for the Jul 16–21 prints the grading instrument watches.

**V3 — (b) + force (c) 2027.** TLT 2027 + 1× WAL 75 P Jan-15-27 (~$700 mid). NOT recommended — doubles WAL when Sep already covers Jul-16, and pays a punishing spread/IV.

---

## F. Kill / confirm lines
- **(b) TLT:** confirm = 10Y sustains >4.40 / breaks higher → AOCI widens (10Y/HY tracked weekday-daily by the RESEARCH-INTAKE lane; the old 6/30 scheduled re-pull has passed — 10Y was 4.44 [7/1]). Kill = 10Y rallies back <4.20 sustained (TLT up = thesis-(b) off).
- **(c) WAL:** catalyst = **Jul-16-26 print** *(corrected from Jul-30, 6/26)*. GATE = monoline beat Jul-21 → fade (a)/(c) before WAL; break → re-arm. **⚠ Sequencing note (7/1):** the gate was designed when WAL printed Jul-30 — with WAL now Jul-16, the monoline window (7/15-22) no longer strictly precedes it; re-read the fade-before-WAL sequencing at fire-time. (Grading instrument: `PROME/archive/synthesis/2026-06-25_Q2-bank-print-grading-instrument.md`.)

## G. Discipline notes
- Rule #5 PROPOSE-only — needs [Approve] before any execution.
- Rule #4 marks live ~10:50 ET 6/26; re-confirm fills at execution.
- Rule #3 image values are a snapshot, not authoritative — confirm recoverable premium against the live broker book.
- Rule #6 banks green today → put adds on green ✓.
- Rule #7 this IS the duration roll, not a trim (thesis intact, timeline uncertain).
- Reshape = no new net risk: redeploy ≈ recovered premium.
