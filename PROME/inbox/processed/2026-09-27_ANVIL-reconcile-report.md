# ANVIL → PROME: FORGE reconcile report, 2026-09-27 (Fri 9/25 CLOSE). Awaiting commit authorization

**Run:** spawned by PROME (`prome-9b`) on Will's word *"Lets finish the reconciliation efforts now"* (Sun 9/27 15:20 ET). Input: `PROME/data/2026-09-27_broker-capture-TRANSCRIPTION.md`. Written 2026-09-27 ~16:1x ET (the clock read 16:10 EDT at rotation). **NO COMMIT made.**

## 1. Arithmetic re-verification (ANVIL recomputed from the tables, not from PROME's §④ or §⑤)
| Check | Result |
|---|---|
| ① value = last × qty (×100 for options), 15 rows | 15/15 ✓ |
| ① G/L = value − basis, 15 rows | 15/15 ✓ |
| Σ positions + cash + pending | $19,559.68 + $17,512.69 + $1.97 = **$37,074.34** ✓ |
| Σ Today / Σ Total G/L | −$1,956.92 ✓ / −$114.86 ✓ |
| ③ running-balance chain | 0 breaks across all 25 transitions (23 amount rows, 3 expiry rows unchanged) ✓; opening before row 26 = $17,940.38 (derived) |
| ③ close ↔ ① | $17,514.66 = $17,512.69 + $1.97 ✓ |
| ② RH card | $203.00 + $1.00 + $15.21 + $8.94 = **$228.15** ✓ (line values DERIVED); WAL cost 17/0.0773 = $219.92 |
| % cells | 3 broker % cells differ by 0.01 from recomputation (VLO −6.03 vs −6.02 · USO +21.30 vs +21.31 · QQQ 730P −47.73 vs −47.72). This is broker rounding; the shown values are kept |
| Parsed live Σ value (positions_from_forge) | **$19,559.68**, matching the broker Σ positions to the cent ✓ |

**§⑤ checklist verdict:** every PROME delta was confirmed at the tables. There was one refinement. D-56's old "−$4.29 residual" is fully explained: the actual Σ nets are +$1,419.10, which equals the ledger cash change 9/11→9/15 exactly. The old figure used 9/16 marks and carried the 1¢ TLT error.

## 2. Headline deltas
| Figure | Was | Now | Source |
|---|---|---|---|
| Fidelity account total | $39,779.11 [9/16 capture] | **$37,074.34** [9/25c] (−$2,704.77) | ① total row |
| Fidelity cash | $22,192.87 [9/16] | **$17,512.69 (47.24%) + pending $1.97** | ① cash; bridge rows 1–11 to the cent |
| Robinhood | $454.33 / BP $129.37 [9/16] | **$228.15 / BP $8.94** [9/27] | ② |
| AAPL / TBT / GLD | qty undated | **9/15 SOLD +$1,653.14 / SOLD +$158.96 / BOUGHT −$393.00** (qty −5/−4/+1 INFERRED; realized ≈+$1,534.92 / ≈+$20.60 derived from basis deltas; GLD basis exact) | rows 14/13/12 + ① basis vs 9/10 transcription |
| Avg cost | AAPL $23.64 · GLD $373.59 · TBT $34.63 | $23.65 · $374.74 · $34.65 | ① |
| VLO ×1 | § Account UNATTRIBUTED | **§ Fidelity — Longs**, $387.18, −$24.82 / −6.03% | row 7 + ① |
| NEW QQQ $730P Sep-30 ×10 | — | $1,300.00, −$1,186.63 / −47.73% (bought 9/24 −$2,486.63) | row 2 + ① |
| NEW USO $159C Sep-30 ×2 | — | $130.00, −$791.33 / −85.89% (bought 9/18 −$921.33) | row 8 + ① |
| WAL $70P + $67.5P Sep-18 | live-shaped, unbooked | **EXPIRED as of 9/18; realized −$768.67 − $750.67 = −$1,519.34** | rows 4–5; basis = 9/10 transcription |
| XLE $65C line | FLAT, first contract undated | first contract sold **9/09 +$169.34** (−$58.33); line realized **−$135.66** | rows 22, 15 |
| USO $153C Sep-11 | entry unknown | entry **9/09 −$77.66** ⇒ **+$135.68** | rows 20, 16 |
| TLT 77P ×5 9/10 net | $28.44 | **$28.43** (−$29.39 realized) | row 18 |
| Day-trade tickets 9/04–9/25 | — | 6 with both legs visible: **−$521.58**; IWM 293P entry unseen | rotation § Ticket record |
| Marks, all rows | 9/10 CLOSE | 9/25 CLOSE (e.g. TLT 82P $1.96→$3.02, +80.11%; HBAN $0.25→$0.80; APO $0.85→$1.25) | ① |

**Classification of the two new lines:** off-thesis / day-trade class (Will-direct). A grep of TERRY setups, STATUS and TRADE_BOOK, ORACLE STATUS, and PROME DOCKET, GATES and WILL_QUEUE found no card for either. That is SEARCH-NOT-FOUND, not VERIFIED absent.

## 3. Discrepancy list, urgency-ranked (the full table is in `FORGE/STATUS.md` § Reconcile discrepancies)

### EXPIRING WED 9/30 (3 sessions)
| # | Item | Owner |
|---|---|---|
| — | QQQ $730P Sep-30 ×10: $1,300, no rule | **Will** (his hand) |
| — | USO $159C Sep-30 ×2: $130, no rule | **Will** |
| **D-60 🆕** | Fidelity "OPTION LIQUIDATION" rows fall on each contract's own expiry day (IWM 9/04, QQQ 9/08, 9/18, 9/25). QQQ 716P Sep-21 EXPIRED instead. The mechanism is UNKNOWN (hypothesis: the broker closes some expiring options itself) | **Will**: ask Fidelity with the WQ-302 question |
| D-31 | TLT 77P ×20 HOLD (WQ-168 ④). It is at 0.35× fees-in; the harvest line is ≥$0.3469. `GATE-TERRY-007` resolved MOOT ⇒ NO-VERDICT 9/24 | TERRY watches the harvest line → Will |
| WQ-168 ⑥ | KRE 60P Sep-30 ×2 LAPSE | rides to $0 |

### Will decides: facts owed
| # | Item | Resolving input |
|---|---|---|
| WQ-302 | TLT 82P + HBAN 16P Oct-16, ITM: choose by Wed 10/14. ×2 each is now confirmed on the 9/25 view (IRA identity still INFERRED) | Will + the TERRY cards |
| **D-59 🆕** | Robinhood buying power fell −$120.43 (9/16→9/27) with no line to show for it. An expiry cannot lower BP | RH history view |
| D-57 | RH Sep-16 QQQ 713C / USO 165C: disposition unknown (dead by date) | RH history |
| D-58 RH leg | RH USO $159C Sep-11: dead by date, UNBOOKED. TERRY's refiner card says "expired/closed 9/11 — GONE", which is a desk record, not a broker row | RH history |
| D-45 residual | **−$85.33** unattributed between the 9/3 ~15:07 capture and the first 9/04 row (−$105.02 of the old −$190.35 is now attributed). Candidate, labeled: the IWM 293P entry | Fidelity Activity scrolled to 9/03 |
| D-44 | QQQ 3 sh sale date/price | same scroll-back |
| D-55 residual | VLO fill TIME | order detail, low |
| D-28 · D-18 · D-54 · D-20 · D-37 | carried Robinhood items | RH history |
| D-17 · D-1 | STNG · AAPL pre-7/30 5 sh | one line / older window |
| (standing) | fill times + per-share prices on every ledger row, because the rows are collapsed | not re-asked per row |

### Owner decides (nothing owed by Will today)
D-47 ROLL70-EXIT (REGINALD grades, TERRY proposes; 0-of-3 through 9/23; ≈$203 derived) · VLO-SCALE, 2 staged shares (TERRY; F1 UNKNOWN pending Will's CME read) · WQ-200 USO 37 (Will's hand) · APD tag (PROME/Will).

### Resolved this pass
D-49 · D-53 · D-56 (dates and nets; qty INFERRED) · the D-55 account leg · the D-58 Fidelity leg / WQ-168 ①② · the TLT 77P 1¢ · D-45 partial · the 9/19 consumer sweep (Account UNATTRIBUTED), which TERRY closed in `cfd9b9115` and I re-verified by parser run.

## 4. Rule-3 consumer verdict: **consumer sweep NOT owed for parsers (all pass); ONE re-review owed by PROME (position_management.tsv)**
I found five consumers, four more than the old footer named. All five are now listed in the footer:
| Consumer | Receipt (run 9/27, post-edit) |
|---|---|
| `AGENTS/TERRY/scripts/positions_from_forge.py --selftest` | **rc=0, SELFTEST PASS** (15 live / 3 withheld, no parse defects) |
| `positions_from_forge.py --all` (normal run) | rc=0. The new QQQ 730P / USO 159C rows are parsed live; VLO is in Fidelity; live Σ value $19,559.68 = broker. At `--asof 2026-10-01`, all four Sep-30 rows are withheld (11 live) ✓ |
| `PROME/tools/will_brief.py parse_money()` | ⚠️ **It returned None on the PRE-edit file** (the 9/20 header dropped the `money market):**` / `account total:**` shapes). **Fixed:** it now returns `{total 37,074.34, cash_pct 47.24, vintage 2026-09-27, marks 2026-09-25}` |
| `PROME/tools/desk_attention.py holdings()` | 18 rows, 0 errors. The WAL Sep-18 / RH USO Sep-11 / XLE qty-0 rows are no longer emitted |
| `scripts/position_agreement_check.py --all --quiet` | **rc=0** |
| `FORGE/position_management.tsv` `source_sha256` | 🔴 **7 mappings are pinned to the pre-edit hash `9a848c16…`** (TLT 77P · KRE 60P Sep-30 · WAL 70P/67.5P Sep-18 · HBAN 16P · RH WAL 70P Dec · RH USO 150/165). The renderer will WITHHOLD them until PROME re-reviews them. The WAL Sep-18 pair are now terminal (they come off the action rows). There are no mappings for QQQ 730P, USO 159C or VLO. **This is PROME's file; I did not edit it.** |
| `AGENTS/BRENT/scripts/pending_receipts.py` | text-level; not run (it needs BRENT's TRADE.md perimeter) |

**Structural changes (each flagged):**
1. The header money line was restored to the will_brief shape.
2. Option expiries now carry the year (`Sep-30-2026`). A year-less "Sep-30" parses as 2027-09-30 from 10/1 in positions_from_forge and would have re-emitted the dead rows as live.
3. A new table sits under the existing § Fidelity — Off-thesis heading.
4. § Account UNATTRIBUTED is kept, but it now has no rows.
5. The WAL subsection is now a note with no table.
6. Discrepancy subsections were renamed ("EXPIRING WED 2026-09-30", "Will decides — facts owed", "Owner decides — ruled / gated", "RESOLVED this pass"). No parser keys on them. `decision_deck.py` only glosses "D-n".

No section `##` names changed. The Longs header changed `Mark 9/10` → `Mark 9/25`, which is prefix-bound.

## 5. Byte cap and rotation
- `FORGE/STATUS.md`: **22,324 B / 159 lines** (`measure.py`; `read_cap_check.py` ✅ 69% of 32,550).
- `FORGE/_archive/STATUS_ROTATION_2026-09-27.md` (NEW): 34,763 B.
  - It has three verbatim chunks. A = src lines 5–11, 2639 B, crc32 2720157. B = lines 27–34/42–46/54/66–73/84–99, 9755 B, crc32 2441139879. C = lines 103–168, 16865 B, crc32 107158792. I checked each by byte-containment against the archive: all True.
  - The commit-object receipt is `git show 1ff1e4088:FORGE/STATUS.md`.
  - It also holds a compiled § Ticket record (9/04–9/25), which is labeled NOT verbatim.
- `FORGE/PORTFOLIO.md`: untouched; the FROZEN banner is intact.
- `claim_check --check weekday` on both files: clean.

## 6. Tree
```
git diff --stat -- FORGE/
 FORGE/STATUS.md | 167 +++++++++++++++++++++++++++-----------------------------
 1 file changed, 79 insertions(+), 88 deletions(-)
git status --short
 M FORGE/STATUS.md                                   <- ANVIL
?? FORGE/_archive/STATUS_ROTATION_2026-09-27.md      <- ANVIL (new; needs explicit add)
 M PROME/state/ORCH_LOG.tsv                          <- PROME's live work, not ANVIL's
?? PROME/data/2026-09-27_broker-capture-TRANSCRIPTION.md   <- PROME's input (untracked)
?? PROME/inbox/2026-09-27_ANVIL-reconcile-report.md  <- this report (not to be committed by ANVIL)
```
If authorized, the commit set would be `FORGE/STATUS.md` + `FORGE/_archive/STATUS_ROTATION_2026-09-27.md`, made via `commit_check.py` (the new file needs an explicit add). The transcription stays PROME's to commit.

## 7. State
**AWAITING COMMIT AUTHORIZATION.** No commit, no push.
