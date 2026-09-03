# ANVIL → PROME — reconcile report, 9/3 intraday Fidelity capture
**Run:** 2026-09-03 Thu 15:10–15:2x ET (`date` wall clock) · **Source of truth:** `PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md` · **Artifact:** `FORGE/STATUS.md` (edited on disk, NOT committed) · **Delivery:** this file + final text (no `SendMessage` tool in this harness).

## 0. Ground-truth verification (rule 1) — VERIFIED
Independent recompute of all 17 rows + cash: Σ values = **$38,259.44 = account total to the cent** ✅ · Σ open G/L **+$1,520.73** on **$18,713.00** open basis = 8.13% ✅ · Σ today **−$137.82** ✅ · every row value = last×qty(×100) and G/L = value − basis ✅ except **APD**: 304.6775×2 = 609.355, displayed $609.35 (broker half-cent rounding; the broker's own total uses 609.35 — not a transcription error). Cash share 47.11% ✅.
**One transcription label slip (§③ mirror column, capture cells unaffected):** "TLT $85P … 2, basis $506.00" — $506.00 was the 8/28 mirror's VALUE; the mirror's basis was **$503.35** (P&L +$2.65 on $506). Today's $251.67 = exactly half ⇒ consistent with ONE contract sold, not a re-basing. Recorded that way in STATUS.

## 1. Headline deltas (8/28 close → 9/3 ~15:07 ET intraday)
| Line | 8/28 | 9/3 15:07 | Δ |
|---|---|---|---|
| Fidelity account total | $36,457.14 | **$38,259.44** | **+$1,802.30** |
| Cash (money market) | $13,600.67 + $722.58 pending | **$18,025.71**, no pending line | +$4,425.04 (**+$3,702.46 net of the settled pending — D-45, hypothesis until the activity view**) |
| Positions MV | $22,133.89 | $20,233.73 | −$1,900.16 |
| Open basis | $21,819.58 | $18,713.00 | −$3,106.58 = QQQ $2,144.23 + one 135C $710.67 + one 85P $251.68 ✅ |
| Qty changes (BROKER-VERIFIED) | — | USO 135C 2→1 · TLT 85P 2→1 · QQQ 3 sh ABSENT | dates/prices NOT verified (no activity view) |
| Movers | — | GLD +$140.32 today (411.55); USO 141.63 (+15.82% open); 135C $11.95 (+68.15% on remaining basis); TLT 77P $0.03 (0.26× fees-in) | — |
| Robinhood | $414.81 (8/28) | **NOT CAPTURED** | WAL Dec-18 $70P ×1 @ $2.20 added as PROME-SUPPLIED unverified row |

## 2. What changed in `FORGE/STATUS.md`
- Header: reconcile vintage = this capture, **intraday basis stated**, cite tag `[Fidelity positions, 9/3 ~15:07 ET intraday]`; 8/29 vintage retained as history (commit `183068dd1`, archive record pointer). Account-scope banner = ONE account, positions only. The 9/2 "STALE FOR TWO TRANSACTIONS" banner is replaced by an **events-by-label box** (BROKER-VERIFIED / PROME-SUPPLIED / RULINGS WQ-168 / GATE-TERRY-ROLL70-EXIT).
- Every Fidelity row: mark/value/G-L/today re-marked; DTE from 9/3 (Sep-18 = 15, Sep-30 = 27, Oct-16 = 43, Dec-18 = 106).
- **QQQ 3 sh → GONE**: retained, struck (`~~`), note says BOTH "absence is not proof of closure" AND "cash bridge supports the sale"; struck deliberately so the parser carries no phantom 3-sh position (un-strike if the activity view disagrees).
- Rulings written onto rows: WAL 70P/67.5P LAPSE (70P re-opens only on a WAL close <$71 in the week of 9/14) · KRE 60P Sep-30 LAPSE · TLT 77P HOLD to expiry · TLT 85P SELL @ $2.60 STAGED · XLE 65C dated exit (9/8 close ≥$66.50 else sell at the 9/9 open, DOCKET L252/L253) · RH USO 150/165 HOLD.
- Gate text beside numbers (rule 7, nothing adjudicated): 135C Rule B/C · 77P harvest "half at ≥3×" + GATE-TERRY-007 0-of-5 (9/1 DGS10 4.79 = window HIGH) · ROLL70-EXIT "≥$81.90 ×3" 0-of-3 at 9/2 close 79.12.
- Two WQ-167 facts (135C sale price · $4.40 GTC status) written **UNKNOWN — permanent, never an ask**, in the banner, the rows, and the discrepancy header.
- Byte discipline: 8/29-vintage history compressed (day-trade ticket prose → pointer; stale "NOT new — D-34" caveats removed; superseded banners removed). No section/header renames beyond `Mark 8/28` → `Mark 9/3`.
- Also recorded: **VLO absent** from the view ⇒ TRY-BRENT-REFINER (3× approved 8/27) unfilled in the IRA as of 15:07.

## 3. Discrepancy list — urgency-ranked, expiring first
**Closed this pass by WQ-168:** D-32 (WAL Sep-18 pair LAPSE) · D-33 (all four Sep-30 legs ruled; XLE dated exit → D-46) · D-29 (QQQ residual → D-44).

### Will decides
| # | Item | Urgency | Ask |
|---|---|---|---|
| **D-43 ★** | TLT $85P Sep-30 — ONE of two SOLD (qty 2→1 verified; basis halved exactly); WQ-168 ⑤ was SELL 2 @ $2.60; last 2.72 at 15:07 | 🔴 **now** — a second contract may be a WORKING order · 27 DTE | Sale date + price; **is the other contract still working?** (a) partial fill of today's 2-lot · (b) 1-lot order · (c) earlier/separate sale — ANVIL picks none |
| **D-44** | QQQ 3 sh GONE from the view | 🟠 fact owed | Sale date/price (or the activity view) |
| **D-45** | Cash bridge +$3,702.46 unexplained by the settled pending | 🟠 | **Fidelity Activity view, past 30 days.** PROME's estimate (QQQ ≈$2,130–2,150 + 135C ≈$1,200–1,400 + 85P ≈$260–275 ≈ $3,590–3,825) carried as a LABELED hypothesis only |
| **D-46** | XLE 65C ×2 dated exit — 9/8 close ≥$66.50? else SELL BOTH at the 9/9 open | 🟡 3 sessions | None — fully specified; Will's hand 9/9 |

### Owner decides (nothing owed by Will today)
| # | Item | Owner |
|---|---|---|
| D-31 | TLT 77P ×25 HOLD to expiry; $0.03 = 0.26× fees-in; GATE-TERRY-007 0-of-5, 29bp from the line; registry's own "NO-VERDICT if expiry beats the count" | TERRY grades DGS10 daily |
| D-47 (new) | RH WAL Dec-18 $70P ×1 @ $2.20 — PROME-SUPPLIED, unverified; guard ROLL70-EXIT 0-of-3; $4.40 GTC status UNKNOWN (permanent) | REGINALD grades / TERRY proposes / next RH capture verifies |
| D-48 (new) | USO 135C ×1 — Rule B (close <$135 ⇒ sell next open; 9/2 close 141.15 not fired), Rule C 10/9; leg A un-gradeable (price permanently UNKNOWN) | TERRY |

### Carried (need a capture or one line)
D-28 RH QQQ 715P expired 8/31 — UNRECORDED, not an ask (TERRY ④) · D-17 STNG (absent again) · D-20 RH T share / event contracts · D-1 AAPL 5-sh sale · D-18 RH WAL 77.5P P&L · D-37 RH inflow/banner.

## 4. Consumer verdict (rule 3)
- `positions_from_forge.py --selftest`: **PASS, rc=0** before AND after (live-file assertion now reads 17 live / 24 withheld).
- Live parse `--all --asof 2026-09-03`: **17 live / 24 withheld (14 closed · 6 event_box · 4 unverified), no parse defects, rc=0.** Every live row = the capture's mark/qty; QQQ 3-sh withheld as CLOSED (no phantom); new RH WAL 70P = `unverified` (no Mark column there — by design).
- Structural changes: NONE to sections/headers/columns; `Mark 8/28` → `Mark 9/3` (prefix-bound, same class as every prior pass); 2 rows newly struck (QQQ 3 sh; RH QQQ 715P — already withheld by date); 1 new RH row. **Consumer sweep NOT owed** — the only listed consumer was re-run post-edit and is clean. Footer consumers-note updated with this pass's line.
- `measure.py`: **BEFORE 31,586 B / 168 lines / crc32 1531964514 → AFTER 28,946 B / 177 lines / crc32 3021722483.** Under the 32,550 B cap by 3,604 B (was 964 B of headroom). No split needed.
- `claim_check.py --check weekday FORGE/STATUS.md`: **clean** — after I corrected my own three "OPEC+ Sat 9/6" instances: **2026-09-06 is a SUNDAY.** ⚠️ **Flag to PROME (not edited by me):** the "Sat 9/6" label lives upstream in `PROME/DOCKET.tsv` L253 and `AGENTS/TERRY/STATUS.md` L29 (the sources I copied it from). Whether the OPEC+ referent is 9/6 (Sun) or Sat 9/5 is the owners' to confirm; STATUS now says "OPEC+ 9/6" with no weekday.

## 5. Git state
```
git diff --stat FORGE/
 FORGE/STATUS.md | 161 ++++++++++++++++++++++++++++++--------------------------
 1 file changed, 85 insertions(+), 76 deletions(-)
git status --short
 M FORGE/STATUS.md                                   ← ANVIL (this run)
 M PROME/tools/dashboard_state.json                  ← not mine, untouched
?? PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md   ← PROME's, untouched
?? PROME/inbox/2026-09-03_from-ANVIL_reconcile-report-9-3-intraday-capture.md  ← this report
```
`FORGE/PORTFOLIO.md` FROZEN banner verified intact, not touched. No other file modified by me.

## 6. Status
**AWAITING COMMIT AUTHORIZATION.** On the go: `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md` from repo root (message via `-F`, `$` figures inside), then the verify-line hash back to you. Not started, not staged.
