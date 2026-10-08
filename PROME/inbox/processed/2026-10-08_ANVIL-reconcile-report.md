# ANVIL → PROME: FORGE/STATUS.md reconcile to the 10/8 Fidelity IRA capture: awaiting commit authorization

**Written:** 2026-10-08 by ANVIL (Claude Opus 5.5), spawned by PROME prome-7c. **Scope touched:** `FORGE/STATUS.md` only. No archive file was needed, nothing is committed, and `FORGE/PORTFOLIO.md` was not touched (its FROZEN banner is intact).

## 1. Ground truth verified independently (rule 1)
- I recomputed everything from §① with Python's Decimal, without relying on PROME's §②. Σ 19 position values = **$21,945.52**. Cash is $11,421.19 and pending is **+$1,283.98** (= +835.32 + 605.32 − 156.66). The three sum to **$34,650.69**, which ties to the cent. Σ basis $19,858.21 · Σ G/L +$2,087.31 · Σ Today +$1,734.39. On all 19 rows, value − basis = G/L and last × qty × multiplier matches value within 1¢.
- I viewed both images myself (`…_fidelity-IRA-{positions,activity}.png`). They match §① cell for cell on every row I checked. The Activity image is **cut off after the third 10/2 row**.
- The Activity running balance holds on every one of its 11 rows. **New derived bridge:** the 10/1 post-close cash of $14,147.60 plus the 10/1 pending of +$1,377.10 = **$15,524.70**, which is exactly the balance just before the first visible 10/2 row (+$3.75). So the 10/1 pending settled in full, with no net unseen cash between 10/1 post-close and 10/2.

## 2. Headline deltas (vs `e8fd99acf`, the 10/7 intraday mirror)
| | 10/7 | 10/8 `[10/8 rcv]` | Δ |
|---|---|---|---|
| Account total | $31,898.27 | **$34,650.69** | +$2,752.42 (positions +$1,468.43 · cash −$1,572.63 · pending +$2,856.62). This is a change between snapshots, not P&L. |
| Cash | $12,993.82 | $11,421.19 (32.96%) | settled the three 10/7 buys at $1,572.63 |
| Pending | −$1,572.64 | +$1,283.98 | the three 10/8 fills |
| Realized 10/8 (derived) | — | **+$918.30** | 755P lot +$596.65 + 745P lot +$321.65 |

## 3. Row by row
| Line | Class | What changed in the mirror |
|---|---|---|
| QQQ $755P Oct-09 | **QTY 2→1** | Bought 10/6 −$477.33. 1 sold 10/8 @ $8.36, net +$835.32 ⇒ **realized +$596.65** (derived from the broker's lot basis: $477.33 − $238.66 = $238.67). The 2nd sell at $8.50 was Verified Canceled. Now $7.85 / $785.00 / +$546.34; basis $238.66. |
| **QQQ $750C Oct-09** | **NEW** | Bought to open 10/8 ×1 @ $1.56, −$156.66. Will-direct; **no TERRY card and no approval record found**; expires Fri 10/9. $1.79 / $179.00 / +$22.34. |
| USO $150C Oct-09 | MARK | $0.66 / $66.00 / −$233.66; still held (no sale row). Fri 15:00 stop retained (WQ-366). |
| QQQ $745P Oct-15 | **QTY 2→1** | Bought 10/7 −$567.33. 1 sold 10/8 @ $6.06, net +$605.32 ⇒ **realized +$321.65** (derived: $567.33 − $283.66 = $283.67). Now $5.73 / $573.00 / +$289.34. |
| QQQ $740P Oct-15 ×4 | MARK | $4.05 / $1,620.00 / −$502.65; entry 10/2 −$2,122.65. |
| TLT 82P · HBAN 16P · KRE 60P ×2 lots · KRE 65P · APO 95P · WAL 65P · OZK 40P | MARK | Marks/values/G/L/Today updated from §①. OZK basis is now **$322.65** (D-75); WAL/OZK entry dates (10/7) added. TLT's multiple was restated as 2.42× (a mark multiple, not a trigger). |
| AAPL · GLD · USO · VLO · APD · TBT | MARK | Marks updated from §①. |
| Robinhood | carried | NOT captured; the 9/29 vintage stands and is bannered. |

**Also corrected:** the 10/7 mirror said no card was registered on the 755P or the Oct-15 lines. TERRY's cards `MGMT-QQQ755P-OCT09` and `MGMT-QQQ745P-OCT15` / `MGMT-QQQ740P-OCT15` exist under `AGENTS/TERRY/setups/`. I now quote their text next to the numbers without adjudicating it. The Oct-15 times are, in the card's words, *"a PROPOSAL for Will"*.

## 4. Discrepancy list, urgency-ranked with expiring items first (full list in the file's § Reconcile discrepancies)
1. 🔴 **QQQ $755P Oct-09 ×1: ITM** ≈$7.84 at QQQ $747.16 (WALTER Yahoo screening quote at 15:26:49 ET, not from the broker). The card says *"Do not carry into Friday."* TERRY's assignment caveat now covers ONE contract (≈$75,500 notional). Owner: **Will** (order); TERRY (card).
2. 🔴 **D-60: how Fidelity handles an ITM option at expiry is still unobserved.** Liquidation observations rise to ×5 (Oct-02 740P) and expired-without-cash observations to ×4 (Oct-05 735P). Owner: **Will**.
3. 🔴 **QQQ $750C Oct-09 ×1: NEW, no card.** It is 1 DTE, so C5's two-session lead is impossible. Its relationship to the 755P is not declared, and I inferred none. Owner: **Will**; **TERRY** (PROME's 10/8 packet asks the card question).
4. 🔴 **USO $150C Oct-09 ×1: Fri 15:00 hard stop** (WQ-366). Owner: **Will**.
5. 🟠 **QQQ $745P ×1 + $740P ×4, both Oct-15** (7 DTE). Owner: **Will** / TERRY cards.
6. 🟠 **TLT $82P / HBAN $16P, both Oct-16:** Wed 10/14 management clock. Owner: **Will** / TERRY / BOND.
7. 🟡 **D-71 stays OPEN (narrowed). ⚠️ I disagree with the framing in the spawn prompt.** The +$3.75 liquidation closes the **Oct-02** 740P, which is D-72's line. It is not the Oct-01 ×4 exit that D-71 names. That exit happened on 10/1, which is **below the image's cut**. What the view adds is the bridge in §1: the 10/1 pending settled in full. Its composition is still not shown, so the ≈ −$747.91 remains PROME's inference. Owner: **Will** (the same Activity view scrolled down to 10/1).
8. 🟡 **D-75 (new): OZK 1¢.** The 10/7 view showed $322.66 in basis, G/L and Today, plus pending −$1,572.64. Those cells are mutually consistent and tie the 10/7 total to the cent. **So a 10/7 transcription misread is UNLIKELY, contrary to the "likely transcription rounding" hypothesis:** a single misread would have broken that tie. The 10/8 Activity, the basis, and the cash bridge all say $322.65. The mirror now carries $322.65. Conjecture (labeled as such): the broker's same-day provisional cost settled 1¢ lower. The 10/7 image is no longer at its cited path (`AGENTS/WALTER/inbox/WILL/Capture.JPG` was not found), so I could not re-view it. There is no cash effect. Owner: **PROME** (record only).
9. 🟡 D-70 (mapping re-review / cards; this edit changes the `source_sha256`) · D-74 (WAL/OZK ownership; entry dates now shown) · D-66 (narrowed: dates, net amounts and the 10/8 fill prices are now shown; times and per-contract buy prices still are not) · D-69 (its gap now sits in 9/30→10/1, below the cut). Owners: PROME / TERRY / Will.
10. 🟡 Carried and untouched by the view: D-62, D-63, D-64, D-65, D-61, D-59, D-45, D-55, D-28, D-54, D-18, D-20, D-37, D-17, D-1. Ruled/gated rows unchanged: D-47, WQ-386/VLO, WQ-200, APD.

**CLOSED this pass:**
- **D-72:** Oct-02 740P ×4 ⇒ −$886.90 (liquidation +$3.75 on basis $890.65). Oct-05 735P ×5 ⇒ −$1,302.97 (sold-to-close +$65.35 plus EXPIRED, on basis $1,368.32). Both are **derived line totals**, supported by the §1 bridge (no other net cash 10/1→10/2). Per-row contract counts are NOT shown. Conjecture only: +$65.35 fits ×1 @ $0.66 less a $0.65 fee.
- **D-73:** all five entries now have dates and amounts, and the running balance links $15,524.70 → $12,993.82 (= 10/7 cash) → $11,421.19 (= 10/8 cash).

## 5. Consumer verdict (rule 3): NO STRUCTURAL CHANGE; no consumer sweep owed
- **`positions_from_forge.py --selftest`: rc=0** (PASS; "live file parses (19 live / 3 withheld)", no parse defects). The live parse values sum to $21,945.52 across 19 rows, which ties.
- `will_brief.parse_money()` returns total 34,650.69 · cash% 32.96 · vintage 2026-10-08 · marks 2026-10-08 ✓.
- `desk_attention.holdings()` returns 22 rows (19 Fidelity + 3 RH) with 0 warnings; the 750C parses as `$750C` 2026-10-09 ×1 ✓.
- `position_management.tsv`: this byte change **withholds every mapping sourced to this file until PROME re-reviews** (D-70). There is also no mapping row for the 750C.
- `pending_receipts.py`: text-level only; I did not run it.
- Same sections, same header prefixes (`Mark 10/8 rcv`), same row conventions. Header and table structure are unchanged.

## 6. Diff stat and size
- `git diff --stat -- FORGE/` → `FORGE/STATUS.md | 123 ++++----  1 file changed, 62 insertions(+), 61 deletions(-)`. `git status --short -- FORGE/` → only ` M FORGE/STATUS.md`.
- `measure.py FORGE/STATUS.md` → **32,523 B** (wc -c), 183 lines, against the 32,550 B cap: **under by 27 B**. My first full write was 33,711 B. I got under by tightening only this pass's own new prose, so **nothing was moved to `FORGE/_archive/`**. ⚠️ The 27 B margin means the next edit of any size will breach the cap. The next pass should plan a rotation; the closed D-72/D-73 block and the carried Robinhood D-rows are the natural candidates.

## 7. Awaiting commit authorization
⛔ Not committed. When PROME gives the word, I will commit through `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md` (subject ≤100 chars, blank line, body) and report the hash.
