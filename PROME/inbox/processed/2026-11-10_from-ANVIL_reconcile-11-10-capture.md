# ANVIL → PROME: FORGE reconcile to the 11/10 captures, awaiting commit authorization

**From:** ANVIL (Claude Code subagent, Opus 5.5), spawned by PROME prome-07 · **Written:** 2026-11-10 15:23 EST · **Not committed, not staged.**
**Inputs:** `PROME/data/2026-11-10_broker-capture-TRANSCRIPTION.md` (uncommitted, yours) and the three images 5.png (Robinhood), 6.png (Fidelity positions), 7.png (Fidelity activity). I re-read all three images; every figure below comes from the images and the ledger. Marks are INTRADAY 11/10 with no clock on the captures (posted 15:13 ET).

## Headline

- **The Fidelity IRA (•1326) ties to the cent at $44,607.15** = positions $13,789.35 + cash $31,871.13 + pending −$1,053.33. I re-derived all 21 rows independently: value = last × qty, and G/L = value − basis. Σ Today −$1,018.82 ties, Σ open G/L −$6,659.28 ties (−32.57% on basis $20,448.63), and 23/23 running-balance steps tie. One precision note: GLD 18 × $369.3522 = $6,648.34, but the broker shows $6,648.33. That is the D-79 class, and the total ties on the displayed values.
- **Compared with the 11/5 mirror (`6db8d1d6f`):** 2 NEW lines (QQQ Nov-13 668P ×2, bought 11/10 −$1,053.33 = the pending; QQQ Nov-10 670P ×2, bought 11/9 −$303.33), 0 QTY CHANGE, 0 GONE, 19 MARK ONLY (quantity and basis identical on all 19).
- **Change since 11/5: −$234.29** = positions +$1,119.76 + cash +$3,652.95 + pending −$5,007.00. That splits into realized −$1.01, unexplained cash +$3.62 and an open G/L change of −$236.90. The 11/5 pending of $3,953.67 settled exactly (AAPL $704.72 + 690P $2,882.28 + VLO $366.67).
- **Realized booked this pass (DERIVED): −$1.01.**
  - QQQ Nov-09 650P ×1: +$522.65 (−$739.66 buy, +$1,262.31 sale; pairing INFERRED by elimination, D-100).
  - QQQ Nov-09 655P ×1: −$523.66 (bought 11/6, EXPIRED as of 11/9).
- **The Robinhood card (11/10 intraday, options list only) shows $440.86, Today −$93.04.** That puts the prior close at $533.90 (DERIVED). 3 NEW (QQQ $675P and $669P, both 11/10; KRE $71.5P ×2, 11/13), 2 GONE (QQQ $640P and USO $148C, both Nov-06, sold or expired NOT SHOWN), 3 MARK ONLY, T UNKNOWN. Every cost and value is DERIVED from $ ÷ % and labelled so.

## Verdicts on the transcription's § ④ (PROME-derived lines)

| § ④ line | Verdict |
|---|---|
| 19 Fidelity rows MARK ONLY | VERIFIED: quantity and basis match the mirror on every row |
| QQQ 668P ×2 NEW; QQQ 670P ×2 NEW | VERIFIED: Activity rows; ×2 from fee cents (.33) |
| Cash/pending change; the 11/5 pending settled | VERIFIED: $28,218.18 + $3,953.67 = $32,171.85 = the post-settlement balance |
| **QQQ Nov-09 650P: "the purchase has NO closing sale … disposition NOT SHOWN; the sale's opening is not in view"** | **REFUSED.** Neither 650P row is in the 11/5 ~10:0x capture (positions or Activity), so both post after it. The running balance has no break from 11/2 to 11/9, so no unseen money row exists. The 11/10 positions view shows no 650P, and there is no EXPIRED row for it, although the same-expiry 655P's EXPIRED row did post 11/10. Fee cents read ×1 buy (.66) and ×1 sale (.31). The sale-below-buy order matches the same-day 680P round trips on 11/2. Conclusion: one same-day round trip, INFERRED by elimination, +$522.65 booked. The two-lot alternative is kept in D-100 at low weight. |
| QQQ Nov-09 655P expired, −$523.66 | VERIFIED and booked |
| **QQQ Nov-04 680P listed as a round trip "since the 11/5 capture"** | **REFUSED as new.** The 11/5 mirror already booked both legs (+$127.66 and −$464.66), and the EXPIRED row was in the 11/5 view. Not booked again. |
| RH MARK ONLY ×3 / NEW ×3 / GONE ×2 / T UNKNOWN | VERIFIED. The three carried lines reproduce their 11/5 costs ($40, $55, $53) exactly, which supports reading the per-line $ as total return (INFERRED). |

## Step 1: rotation (done first)

`FORGE/_archive/STATUS_ROTATION_2026-11-10.md` is new (26,587 B, crc32 2890525929). It holds seven chunks of HEAD's `FORGE/STATUS.md` (blob `bc8a42192`, last commit `6db8d1d6f`), cut on whole lines. Each chunk was checked with `measure.py --identical` against a fresh extract from HEAD: rc 0 on all seven.

| Chunk | HEAD lines | Content | Bytes | crc32 |
|---|---|---|---|---|
| A | 5–9 | 11/5 header block | 2610 | 1001604595 |
| B | 25–29 | 11/5 Longs rows + CLOSED stock line | 2077 | 29664793 |
| C | 43–50 | 11/5 off-thesis rows + terminal records (+$4,168.14, +$30.47) | 2515 | 2526541593 |
| D | 80 | QQQ Nov-20 690P history line | 327 | 1779125658 |
| E | 95–112 | 11/5 after-close Robinhood section | 2552 | 1925048316 |
| F | 120–156 | the whole 11/5 discrepancy section, every row | 13047 | 2613405661 |
| G | 160–167 | 11/5 Immediate Actions | 675 | 306415108 |

**Size: `FORGE/STATUS.md` went from 32,331 B to 29,749 B (crc32 3810517053; 91% of the 32,550 B cap, rotate tier).** That is under the cap, with 2,801 B of headroom, but **the ~70% target was not reached.** Everything left in the hot file is live: current rows, open D-rows, standing banners and the parser footer. No more dated or closed history was left to move. Getting to 70% would mean demoting live open items, or splitting the discrepancy section (11.9 KB) into its own cold surface. That is a structural choice, and it is yours. Expect another rotation at the next reconcile.

## Discrepancy list (urgency-ranked, dated contracts first; recorded in the file as records, with no prompts)

1. **D-100 NEW 🟠**: the QQQ Nov-09 650P pairing (above). +$522.65 is booked on an inference. Owner: Will (row detail, if wanted); PROME records.
2. **D-98 rebuilt 🟠**: Robinhood 11/5 → 11/10.
   - GONE: 640P and 148C, disposition NOT SHOWN.
   - NEW lines: fills NOT SHOWN.
   - DERIVED identity, if the $24.11 residual is cash: buying power fell $865.15 → $24.11 = −$841.04 = −$455.75 new costs + X (640P/148C proceeds, ≥ 0) + Y. So **at least $385.29 of outflow is unseen.**
   - The per-line sum (−$187.00) is not Today (−$93.04).
   - The 11/5 gaps ①–③ are unchanged (chunk F).
   - Owner: Will (RH history and cash); PROME records.
3. **D-102 NEW 🟡**: badges.
   - Fidelity "NE" is on QQQ Nov-10 670P, USO Nov-11 172C and QQQ Nov-13 668P, and on no Nov-20 or later row. The 172C carried it on 11/5 at 6 days.
   - APO's 11/5 "E" badge is gone.
   - RH "6 days left" would mean 11/16, and no RH line expires that day.
   - CONJECTURE: "NE" is a near-expiration flag, and the RH badge is an account countdown. Neither meaning is stated.
4. **D-101 NEW 🟡**: cash +$3.62 (screen $31,871.13 vs last settled $31,867.51). No row shows it. A money-market accrual is CONJECTURE only. Not booked.
5. **D-94 🟠, D-96, D-95, D-97, D-90 UNCHANGED.** This Activity view starts at Nov-02 (clipped APD row) and stops above the 10/30 rows they need. D-94's basis of $1,339.665 is still unbooked.
6. **D-89 UNCHANGED**: no Orders panel this time.
7. **D-60 NARROWED**: the 655P lapsed as an EXPIRED row posted the next business day with no amount (the third path, one more instance).
8. **D-74** cluster refreshed: 41 contracts / 14 lines, basis $6,644.24, value $1,110.00. **D-77** adds the two new QQQ lines and the 650P/655P. **D-70**: new lines unmapped. **D-79**: the GLD 1¢. **D-76** and **D-83** refreshed. **D-91** and **D-78** unchanged.
9. **Closed: D-99** (answered and recorded 11/5; its row is in chunk F). **Moved to a carried row, still OPEN, verbatim in chunk F:** D-88, D-87, D-86, D-85, D-84, D-81, D-80. The 18 carried rows from 10/08 are untouched.

## Step 5: consumer verdict (rule 3)

| Consumer | Result |
|---|---|
| `positions_from_forge.py --selftest` | **rc 0**: 21 live / 7 withheld (was 19 / 6), no parse defects |
| `will_brief.parse_money()` | total 44,607.15 · cash 71.45% · vintage 2026-11-10 · marks "2026-11-10 intraday", marks_known True |
| `desk_attention.holdings()` | 28 rows, 0 errors |
| BRENT `pending_receipts.py` | rc 0; lists D-98 as a closure CANDIDATE for its RH USO $148C row, with the outcome correctly still UNKNOWN |
| `position_management.tsv` `source_sha256` | the byte change withholds every mapping sourced to this file until PROME re-reviews |

**No structural change:** section headings, table headers (`Mark 11/10 intraday` is still prefix-bound), row conventions and the header money-line shape are all unchanged. The PARSED BY footer is byte-identical to HEAD (`measure.py --identical` rc 0). **No consumer sweep is owed.** Two items for PROME, though:
- **(a) Mapping re-review:** the byte change withholds every `position_management.tsv` mapping sourced to this file until you re-review it.
- **(b) BRENT's TRADE.md row:** its RH USO Nov-06 $148C row ("no capture after expiry") now has a capture after expiry, and the outcome is still NOT SHOWN. That is BRENT's to re-check; I touched nothing of BRENT's.

`claim_check --check weekday FORGE/STATUS.md`: clean.

## Step 6: tree

```
 FORGE/STATUS.md | 147 +++++++++++++++++++++++++-----------------------
 1 file changed, 71 insertions(+), 76 deletions(-)
?? FORGE/_archive/STATUS_ROTATION_2026-11-10.md   (new; untracked, so not in diff --stat)
```

Final sizes from measure.py: `FORGE/STATUS.md` 29,749 B (crc32 3810517053); rotation 26,587 B (crc32 2890525929). Nothing is staged. I touched no other desk's files. The mirror's footer points at `PROME/data/2026-11-10_broker-capture-TRANSCRIPTION.md`, which is still uncommitted (yours); it needs to land with or before the FORGE commit. The PORTFOLIO.md FROZEN banner is intact.

**Awaiting commit authorization.** On your word I commit via `commit_check.py commit -F <msgfile> -- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-11-10.md`, then report the hash.
