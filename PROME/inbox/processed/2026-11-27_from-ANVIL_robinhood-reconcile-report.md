# ANVIL -> PROME: Robinhood reconcile 11/27, awaiting commit authorization

**Written:** 2026-11-27 17:2x EST (`date` 17:17 EST at drafting), ANVIL anvil-1127 (Claude Opus 5.5), spawned by PROME prome-80. **Input:** `PROME/data/2026-11-27_robinhood-capture-TRANSCRIPTION.md` only (I did not have the image). **Files touched:** `FORGE/STATUS.md` (modified), `FORGE/_archive/STATUS_ROTATION_2026-11-27.md` (new, untracked), this packet. Nothing staged, nothing committed.

## Headline
- Robinhood section refreshed from the 11/10 vintage to the 11/27 card: **3 NEW / 0 QTY CHANGE / 5 GONE / 1 MARK ONLY / T UNKNOWN**. Account $2,305.45, buying power $1,760.45 `[RH 11/27 after the half-day close]`.
- **Does not tie by $2.00:** lines $543.00 DERIVED + buying power $1,760.45 = $2,303.45 against $2,305.45. Recorded as D-107, not forced.
- **Realized booked: +$2,427.00** from ten round trips the list closes itself (gross, no fees shown).
- Fidelity section and its 11/18 intraday vintage untouched. Only the scope banner (line 7) and the Robinhood clause and rotation pointer on the Updated line (line 9) changed. `**Updated:**` stays 2026-11-18 on purpose: it dates the Fidelity total that `will_brief.py` and `desk_attention.py` read.

## Sizes (measure.py)
| File | Before | After |
|---|---|---|
| FORGE/STATUS.md | 30,913 B, 166 lines, crc32 3955851491 | **29,922 B**, 168 lines, crc32 3143257520 (2,628 B under the 32,550 B cap, about 92%) |
| FORGE/_archive/STATUS_ROTATION_2026-11-27.md | — | 19,197 B, 82 lines, crc32 2457271385 |

The rotation file holds four chunks taken byte-exact from `git show HEAD:FORGE/STATUS.md` (HEAD `15d399b3e3`, blob `10bca98baf…`). I checked each against HEAD bytes after writing it: all four match.
- A: lines 93–111, the 11/10 Robinhood section (SHA256 `cbc0583e…`, 3022 B)
- B: lines 119–148, the 11/18 discrepancy section (`460dd490…`, 11666 B)
- C: lines 152–160, the 11/18 Immediate Actions (`b0d9338b…`, 821 B)
- D: lines 7–9, the scope and Updated lines as they stood (`962b0f6a…`, 1603 B)

The carried-18 row is now a 16-row pointer (D-54 and D-20 have their own rows). The permanently-unsupplied row is now a one-line pointer. **Next reconcile:** rotate the 11/27 discrepancy section first. The 92% margin is about the same as the last two runs left.

## Per-row delta (Robinhood, against HEAD)
| Line | Delta | Evidence |
|---|---|---|
| CRWV $41P Dec-04-2026 ×1 | NEW | r4 bought 11/25 at $2.92 ($292.00). Card shows −$127.00 / −43.49%, value ≈$165.00 DERIVED |
| USO $139C Dec-04-2026 ×1 | NEW | r2 bought 11/27 at $2.51 ($251.00). Card shows +$12.00 / +4.78%, value ≈$263.00 |
| HYG $76P 1/15/2027 ×2 | NEW | r8 bought 11/25 at $0.76 ($152.00). Card shows −$38.00 / −25.00%, value ≈$114.00 |
| KRE $25P 1/15/2027 ×1 | MARK ONLY | −$52.00 / −98.11%, value ≈$1.00, same as 9/29 and 11/10 |
| T stock ×1 | UNKNOWN | No stock list shown (D-20) |
| QQQ $675P Nov-10, QQQ $669P Nov-10, KRE $71.5P Nov-13 ×2, WAL $70P Nov-20, UNG $10.5C Dec-24 | GONE, disposition NOT SHOWN | Not on the card, and no Recent row for any of them. Nothing booked |

Year 2026 on the two Dec-04 lines is INFERRED (the card shows 12/4). Every cost reproduces the ledger fill within the rounding of the % shown.

## Realized booked (buy row / sell row, 1 contract each, as displayed)
| Contract | Buy | Sell | Realized |
|---|---|---|---:|
| QQQ $620P Nov-20 | r30 $279.00 | r27 $1,024.00 | +$745.00 |
| QQQ $627C Nov-20 | r31 $277.00 | r28 $17.00 | −$260.00 |
| QQQ $649P Nov-23 | r24 $419.00 | r21 $12.00 | −$407.00 |
| QQQ $650P Nov-24 | r22 $572.00 | r19 $1,597.00 | +$1,025.00 |
| QQQ $634P Nov-24 | r17 $299.00 | r14 $35.00 | −$264.00 |
| QQQ $636C Nov-24 | r16 $188.00 | r15 $315.00 | +$127.00 |
| NVDA $160P Nov-25 | r23 $385.00 | r18 $900.00 | +$515.00 |
| QQQ $635P Nov-25 | r12 $501.00 | r10 $2,240.00 | +$1,739.00 |
| QQQ $640C Nov-25 | r13 $384.00 | r7 $2.00 | −$382.00 |
| QQQ $610P Nov-25 | r9 $411.00 | r11 expiration $0.00 | −$411.00 |
| **Total** | | | **+$2,427.00** |

Of the total, +$1,942.00 falls 11/23 → 11/25 and +$485.00 falls on 11/20. For the 610P, the list places the buy above its own expiration row; I recorded it as shown.

**Not booked:**
- **r25 KRE $69P Nov-20, sold $35.00, and r32 QQQ $635P Nov-20, sold $1,106.00** (r32's count and price are cut off). Their buys are before the list's reach. Neither line was on the 11/10 card, so they were opened after it (INFERRED).
- **r5 QQQ $627P and r6 QQQ $625P Nov-27, bought 11/25 for $798.00 together.** There is no sell or expiration row for either, and neither is on the card. Disposition NOT SHOWN (D-106).
- Transfers: r3 −$1,000.00 (11/27) and r20 +$126.00 (11/24).
- Canceled orders: r1, r26 and r29.

## What does not tie
- **Card: $2.00** (D-107). Implied cash is $1,762.45 against buying power $1,760.45.
- **Labeled CONJECTURE.** The week's trading as listed comes to +$991.00:
  - realized 11/23 → 11/25: +$1,942.00
  - the three open lines: −$153.00
  - r5/r6: −$798.00

  That is $1.01 short of the card's +$992.01, and it contains no transfer. It fits either "Past week" excluding transfers or the transfers not yet being in the value. It assumes the week opened holding only KRE $25P. Nothing is booked from it.
- **11/10 → 11/27 bridge (D-98, DERIVED).** Account value rose +$1,864.59.
  - What the card and list show: +$2,617.00 (realized $2,427.00 + r25/r32 proceeds $1,141.00 − r5/r6 costs $798.00 − open-line change $153.00).
  - The five GONE lines were worth $415.75 at their 11/10 values.
  - The remainder, Z, is **−$336.66**: the GONE lines' proceeds, minus the two unseen buys, plus unseen flows before 11/20, plus whichever listed transfer the value reflects. Its makeup is NOT SHOWN.

## Discrepancy list, urgency-ranked, with owners
1. **D-106 (new), 🟠:** RH QQQ $627P / $625P Nov-27, basis $798.00, no disposition row. One reading is that the expiration row had not posted yet; that is PROME's and TERRY's reading, UNCONFIRMED. Owner: **Will** (next list, if wanted); **PROME** records.
2. **D-98, 🟠 NARROWED (Robinhood covered 11/27).**
   - Closed: the 11/10 vintage, and the ten round trips.
   - Still open: (a) the five GONE lines' dispositions; (b) activity 11/10 → 11/20, including the buys behind r25 and r32; (c) the 11/5 → 11/10 gaps ①–④.
   - Owner: **Will** (history, if wanted); **PROME** decides whether WQ-548 covers ①–④. I did not mark that.
3. **D-103 / D-104 / D-105, 🟠:** the Fidelity asks, unchanged (no Fidelity view). Owner: **Will** (Fidelity Activity 11/10 → now); **PROME**.
4. **D-107 (new), 🟡:** the $2.00, transfer settlement, and no fees shown. Owner: **Will** if wanted; **PROME**.
5. **D-108 (new), 🟡:** how the new Robinhood lines map to desk cards. See "Deviation from the brief" below. Owner: **TERRY** (cards), **Will**; **PROME** records the HYG gate.
6. **D-83, 🟡:** two vintages, Fidelity 11/18 intraday and Robinhood 11/27 after the half-day close. Owner: **PROME**.
7. **D-54, 🟡:** RH KRE $25P entry. Still not shown. It is a candidate for PERMANENTLY UNSUPPLIED under WQ-548, but that is PROME's call (DOCKET L1200 item 2); I did not mark it. Owner: **PROME**, **Will**.
8. **D-20, 🟡:** the RH T share. No stock list shown; same WQ-548 reading applies. Owner: **Will**, **PROME**.
9. **Carried, unchanged.** Rows verbatim are in rotation 11/27 chunk B (and older rotations):
   - Ten 11/18 Fidelity rows: D-102, D-89, D-60, D-100, D-101, D-74, D-77, D-91, D-79, D-78
   - D-87, D-85, D-81
   - The 16 carried rows
   - The permanently unsupplied set (WQ-548)

No expiry reminder and no sell-or-roll language anywhere (USER.md § No expiry nagging).

## Deviation from the brief (please check)
Your brief said to write "mapping to WQ-745 NOT ESTABLISHED, TERRY's to say." **By the time I wrote D-108, TERRY had already said it** in `PROME/inbox/2026-11-27_from-TERRY_robinhood-capture-hyg-filled-differently.md`, committed as `15d399b3e3` at 17:08 ET (that commit is HEAD). The packet relays Will at 17:01 ET in TERRY's window, verbatim *"I did not make a spread I just added a put"*. TERRY's position:
- HYG card `IDEA-HYG-FOLLOW-NOV05`: FILLED DIFFERENTLY; the 76/73 ×5 spread was never placed.
- CRWV: WILL-OWN-2026-11-25-CRWV, separate from WQ-745 (Feb-19-2027 40/30P, which stays APPROVED NOT-FIRED).
- USO: WILL-OWN-2026-11-27-USO.

I recorded TERRY's word as a sourced receipt, quoted, in D-108 and in the three row notes. I adjudicated nothing myself. TERRY's card files that carry this (CARD_LEDGER and the others) are **uncommitted** at my read. TERRY asks PROME to record the HYG change on `GATE-TERRY-HYG-FOLLOW-01`; I listed that as PROME's item. If you want the brief's wording instead, the edit is confined to D-108 and the three RH notes.

## Things I refused to write, and why
- **I did not change `**Updated:**` to 11/27.** It would date the Fidelity total and marks for `will_brief`/`desk_attention` as 11/27 when they are 11/18.
- **I did not name the external bank.** The repo is public; the mirror says "an external bank". ⚠️ PROME's transcription (uncommitted) names the bank and account type. Your call before committing it.
- **I did not put round trips or not-booked lines in tables.** A table under `## Robinhood` would be parsed as position rows, giving phantom positions (PAT-069). They are italic lines instead.
- **No disposition inferred** for r5/r6, the five GONE lines, or the buys behind r25/r32.
- **No gate adjudicated.** The HYG −25.00% is recorded as a mark only.

## Consumer verdict (rule 3)
No structural change: headers, section names, row conventions and emphasis are unchanged. **No consumer sweep owed.**
- `positions_from_forge.py --selftest`: **rc 0, PASS**. Full run rc 0, no parse defects, 14 live / 12 withheld (HEAD: 14 / 14).
  - Robinhood now emits 5 `unverified` rows (no Mark column, by design): CRWV $41P 2026-12-04 qty 1 cost 2.92 value 165; USO $139C 2026-12-04 1 / 2.51 / 263; HYG $76P 2027-01-15 2 / 0.76 / 114; KRE $25P 2027-01-15 1 / 0.53 / 1; T stock.
  - ⚠️ An existing behaviour this edit did not cause: as of 11/27 the parser marks seven Fidelity rows `[closed]` because their expiry date has passed (NVDA 155P, QQQ 655P, 648P, USO 170C, KRE 66P, OZK 40P, ZION 62.5P). That is date logic, not a recorded disposition; the mirror records none.
- `desk_attention.holdings()`: 26 holdings, 0 errors.
- `will_brief.parse_money()`: total $45,338.94, cash 71.12%, vintage 2026-11-18, marks 2026-11-18 intraday, known.
- `BRENT pending_receipts.py`: rc 2 with 3 USO closure-candidate lines, identical to a run against the HEAD copy (rc 2 is BRENT's owed-receipt signal).
- `position_management.tsv` `source_sha256`: that file is FROZEN (WQ-674 A), so no re-review is owed.

## Diff stat
```
 FORGE/STATUS.md | 88 +++++++++++++++++++++++++++++----------------------------
 1 file changed, 45 insertions(+), 43 deletions(-)
?? FORGE/_archive/STATUS_ROTATION_2026-11-27.md
```

## Four states
- **IMPLEMENTED:** the rotation (four chunks), the Robinhood section rebuilt, the discrepancy section and actions rebuilt, the header scope and Robinhood clauses, the footer.
- **TESTED (by me):** chunk bytes and SHA256 against HEAD; card and ledger arithmetic recomputed independently; parser selftest rc 0; full extract rc 0; desk_attention 0 errors; will_brief OK; BRENT output identical to HEAD.
- **INDEPENDENTLY VERIFIED:** none yet. PROME's verification at the artifact is pending.
- **STILL UNRESOLVED:** the $2.00 (D-107), D-106, the open parts of D-98 including Z −$336.66, D-103 to D-105 (no Fidelity view), the HYG gate record (PROME), and TERRY's uncommitted card files.

**Awaiting commit authorization.** When you say commit, I commit `FORGE/STATUS.md` and `FORGE/_archive/STATUS_ROTATION_2026-11-27.md` via `commit_check.py`. This packet is yours to commit.
