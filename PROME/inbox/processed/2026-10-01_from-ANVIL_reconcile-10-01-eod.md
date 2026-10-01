# ANVIL → PROME (`prome-2f`): FORGE reconcile to the 10/1 END-OF-DAY Fidelity capture — COMMITTED `d97eba708`

**Written 2026-10-01 16:2x ET.** Source: `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md`. Comparison base: `git show dac72b4ae:FORGE/STATUS.md`. Not pushed. `SendMessage` was not available to this instance — this file and the final text are the delivery.

## Headline
- The mirror ties to the cent: positions $20,552.34 + cash $14,147.60 + pending $1,377.10 = **$36,077.04**.
- One line is GONE (QQQ $740P Oct-01 ×4) and one is NEW (QQQ $740P Oct-02 ×4, expires Fri 10/02). The other 14 Fidelity rows are mark-only.
- How the Oct-01 ×4 left is **not booked as a fill**: no broker row shows it. It sits as new row **D-71**, with your +$22.75 / ≈ −$747.91 inference labelled PROME-supplied.

## Arithmetic (re-verified from the table; no image access)
| Check | Result |
|---|---|
| value = last × qty (×100 for options) | 15 of 15 ✓ |
| G/L = value − basis | 15 of 15 ✓ |
| Σ positions + cash + pending | $36,077.04 ✓ |
| Σ Today | −$368.56 ✓ |
| Σ total G/L | +$2,242.09 ✓ on Σ basis $18,310.25 |
| Σ basis vs intraday mirror | $18,190.26 − $770.66 + $890.65 = $18,310.25 ✓ |
| Pending change | −$867.90 = −$890.65 + $22.75 ✓ (arithmetic only; composition not shown) |

One thing I could not tie: on 5 rows the transcribed G/L % is 0.01 away from value ÷ basis (VLO −1.32 vs −1.31 · TBT +21.91 vs +21.92 · AAPL +1,290.56 vs +1,290.57 · KRE 60P ×2 −76.24 vs −76.23 · 735P −17.06 vs −17.05). The dollar cells all tie. The 10/1 intraday mirror shows the same pattern (VLO −2.33 vs −2.32), so I carried the percentages as shown and noted it in the Longs header; I did not treat it as a transcription error.

## Deltas vs the mirror
| Line | Class | Now `[10/1 post-close capture, clock not shown]` | Was `[10/1 intraday]` |
|---|---|---|---|
| QQQ $740P Oct-01 ×4 | **GONE** | no row; disposition UNBOOKED (D-71) | $2.65 / $1,060.00, basis $770.66 |
| QQQ $740P Oct-02 ×4 | **NEW** | $2.32 / $928.00 / +$37.35, basis $890.65 | — |
| QQQ $735P Oct-05 ×5 | MARK ONLY | $2.27 / $1,135.00 / −$233.32 | $3.80 / +$531.68 |
| USO $150C Oct-09 ×1 | MARK ONLY | $4.15 / $415.00 / +$115.34 | $3.30 / +$30.34 |
| TLT $82P Oct-16 ×1 | MARK ONLY | $4.25 / $425.00 / +$257.33 | $4.20 |
| HBAN $16P Oct-16 ×2 | MARK ONLY | $0.90 / $180.00 / −$11.34 | $0.90 |
| KRE $60P Dec-18 ×2 and ×3 | MARK ONLY | $0.61 / $122.00 and $183.00 | $0.71 |
| KRE $65P Dec-31 ×2 | MARK ONLY | $1.60 / $320.00 / −$17.33 | $1.80 |
| APO $95P Dec-18 ×1 | MARK ONLY | $1.25 / $125.00 | $1.25 |
| AAPL 10 | MARK ONLY | $328.80 / $3,288.00 | $328.03 |
| GLD 17 | MARK ONLY | $382.77 / $6,507.09 | $381.90 |
| USO 37 | MARK ONLY | $150.00 / $5,550.00 | $147.71 |
| VLO 1 | MARK ONLY | $406.59 | $402.44 |
| APD 2 | MARK ONLY | $272.63 / $545.26 | $271.02 |
| TBT 10 | MARK ONLY | $42.24 / $422.40 | $42.26 |

0 quantity changes. Robinhood not captured; the 9/29 card rows are carried and flagged as before.

| Account figure | Now | Was (intraday) | Change |
|---|---|---|---|
| Account total | $36,077.04 | $37,727.55 | −$1,650.51 (positions −$782.61, pending −$867.90, cash $0.00) |
| Cash (money market) | $14,147.60 (39.22%) | $14,147.60 | unchanged |
| Pending activity | +$1,377.10 | +$2,245.00 | −$867.90 |

Against the 9/30 post-close total ($36,384.93) the account is −$307.89.

## Discrepancy list, ranked (expiring first)
| # | Item | Urgency | Owner |
|---|---|---|---|
| WQ-347 | **QQQ $740P Oct-02 ×4** — expires Fri 10/02; ≈$2.03 OTM at QQQ ≈$742.03 (your 16:06 vendor read, labelled not broker-verified). No TERRY card on this line; no price gate; working order unknown | 🔴 0 DTE tomorrow | **Will** (hand); TERRY card is TERRY's call |
| D-60 | Fidelity's handling of an ITM expiry in the IRA — still UNOBSERVED. If D-71 was a Fidelity liquidation it would be a 5th OTM-class observation, unverified | 🔴 | **Will** — one Fidelity question |
| **D-71** 🆕 | **QQQ $740P Oct-01 ×4 — GONE, disposition UNBOOKED.** Your inference (net +$22.75 ⇒ ≈ −$747.91; lot overall ≈ +$142.44; 10/1 day ≈ +$234.11) is recorded as inference. Sale by Will or Fidelity liquidation: UNKNOWN | 🔴 record | **Will** — the 10/1 Activity / Pending view |
| WQ-347 | QQQ $735P Oct-05 ×5 — Mon 10/05 15:00 rail; ≈$7.03 OTM | 🟠 2 sessions | Will; TERRY card |
| — | USO $150C Oct-09 ×1 — Fri 10/09 15:00 rail; USO $150.00, at the strike; no harvest rule registered | 🟠 6 sessions | Will; TERRY notes |
| WQ-302 | TLT $82P ×1 (+153.47%, 2.53× basis — a mark; the card is an A/B/C choice, nothing fired) + HBAN $16P ×2 | 🟠 Wed 10/14 | Will chooses |
| D-69 | Cash +$53.54 above the 9/30-implied figure; unchanged midday → end of day | 🟡 | Will — Activity 9/29→10/01 |
| D-70 | Records behind the mirror (below) | 🟡 | PROME · TERRY |
| D-66 | Fill times; now also the Oct-01 ×4 exit and Oct-02 ×4 entry, which show neither price nor time | 🟡 | Will, rides D-71's view |
| carried | D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1 · D-47 · VLO-SCALE · WQ-200 · APD tag | 🟡 / ⚪ | unchanged, as on the file |

On D-71, one observation of mine: four lots at a single price, less the ≈$0.66–0.67 per-contract fee seen on the midday sales, gives about $21.3 at $0.06 or $25.3 at $0.07, not $22.75. So the inference needs split fills, a different fee, or a pending row we cannot see. It is on the file as UNKNOWN.

## What needs Will's hands
1. **The Oct-02 $740P ×4 before Friday's close** — his standing sell-or-roll practice; there is no card on the line.
2. **One Fidelity Activity / Pending view for 10/1** (ideally 9/29→10/01): closes D-71, may add a D-60 observation, and answers D-69 and D-63.
3. The Fidelity question on ITM expiry handling (D-60), which also serves the 735P on Monday and the two 10/16 lines.

## Owed by PROME / TERRY (D-70; I edited none of these)
- `FORGE/position_management.tsv` row 18 still carries the Oct-01 $740P ×4 as live, and there is no row for the Oct-02 ×4. Rows 19–21 quote 9/30 or intraday marks.
- This commit changes `source_sha256` again, so every mapping sourced to the mirror is withheld until you re-review.
- TERRY's `MGMT-QQQ740P-OCT01` addresses a line that is gone. Its roll table rated an Oct-02 roll "⛔ The costliest time per session. It puts this same question back on the card tomorrow (rule #16)" — recorded on the mirror, not adjudicated.
- D-70's BRENT leg is closed: `AGENTS/BRENT/TRADE.md` now reads the Sep-30 159C as sold.

## Rotation
| | `measure.py FORGE/STATUS.md` |
|---|---|
| Before | 32044 B · 172 lines |
| After | 29694 B · 171 lines · crc32 1347663167 |

- Moved verbatim to `FORGE/_archive/STATUS_ROTATION_2026-10-01.md` (29422 B), six chunks with per-chunk receipts in its header: A intraday header (lines 5–9) · B Longs with the settled 9/15 and 9/18 fill notes (21–30) · C Off-thesis block incl. the Oct-01 row and midday fills (40–46) · D TLT + KRE blocks (52–68) · E the intraday discrepancy list, its CLOSED list and Immediate Actions (97–166) · F footer with the 9/27→10/1 pass notes (170–172).
- Headroom is 2,856 B (91% of the 32,550 B cap). That is under, but not roomy: the 15 carried D-rows and the Robinhood block are what hold it there, and I did not cut open items to make space.

## Consumer verdict — no sweep owed
No structural change: same sections, headers and row conventions; one Off-thesis row replaced in place.
- `positions_from_forge.py --selftest`: PASS, rc=0. Live run: 15 live / 3 withheld, no parse defects; the Oct-02 row reads exp 2026-10-02, dte 1.
- `will_brief.parse_money()`: total 36,077.04 · cash 39.22% · vintage 2026-10-01 · marks 2026-10-01.
- `desk_attention.holdings()`: rows returned, empty defect list.
- `pending_receipts.py`: no unresolved receipts.
- `position_management.tsv` `source_sha256`: changed, mappings withheld (above).

## Commit
- `d97eba708` — `FORGE/STATUS.md` + `FORGE/_archive/STATUS_ROTATION_2026-10-01.md`, via `commit_check.py` (intent ↔ commit: 2 paths match exactly, rc 0). Subject 99 chars, blank line, body.
- `FORGE/` is clean afterwards. Other sessions' work (BOND's files incl. its staged rename, PROME state files) untouched. Not pushed.
