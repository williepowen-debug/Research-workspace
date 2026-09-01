# TERRY → PROME · 2026-09-01 Tue ~17:5x ET · **WQ-143 (B) / WQ-94 / WQ-95 executed — `TRY-WAL-ROLL70` card built (STAGED, not filled) · `TRY-MGMT-USO135C` rule-#20 terms written · QQQFADE archive was already done 8/27, INDEX row moved · `GATE-TERRY-007` graded 8/26–8/31 (0 of 5) · inbox 11/11 drained**

**Priority:** 🔴 (two items return to Will) · **Spawn:** prome-98, full desk session · **`$0` moved, no order, no fill, no gate moved, no threshold shaved.** · **Push:** NOT pushed — you sweep, as instructed.

## 1. WQ-143 (B) — `TRY-WAL-ROLL70` · card `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md` · verdict **CONDITIONAL** · commit `ee62261c6`

**The fill instruction Will [Approve]s (in-principle ruled 9/1; final [Approve] on the fill-day ticket with live prices):**
| Field | Rule |
|---|---|
| Shape | **BUY 1 × WAL Dec-18-2026 $70 PUT**, Fidelity IRA (same account as the Sep-18 pair) |
| Max debit | **$2.75/contract = $275** — the cap IS the no-chase line; ask above it ⇒ no fill, back to Will (never substitute Nov-20 without a fresh word) |
| Green-day rule (root rule #6, on the instrument transacted) | **WAL last > prior regular-session official close at the moment of fill** (9/1 ref = $77.26; rolls daily). KRE is context, not the test. Green that turns red before the fill ⇒ stand down. **9/1 was RED (WAL −1.11%) ⇒ no fill today; no break offered — none exists** (REGINALD's cohort sort says sector beta = the proxy working) |
| Precondition | `REG-T-02` still FIRED on REGINALD's registry (exit count < 3 of 3); `chain_fetch --legs 70 --no-cache` clean; **live Fidelity book open at fill** (pair still ×1/×1; cash) — FORGE is 8/29 vintage |
| Guard / exit | **`REG-T-02` EXIT: WAL ≥ $81.90 on 3 consecutive official closes (REGINALD grades) ⇒ close the roll next session.** Thesis retraction by the WAL desk ⇒ close |
| Harvest (RISK_RULES #9) | resting GTC sell at **≥ 2.0× the debit paid** (≥ $5.50 on a $2.75 fill) |
| Time stop / roll-again | **Fri 12/04**: sell if OTM; Will decides if ITM. **NO further roll pre-registered** (Non-Negotiable #6) |
| Existing pair | **HELD to expiry** (Will) — ≈ **$30 at bid** (0.20 + 0.10); nothing sold |
| Size / concentration | ×1 = 55% of the $500/card cap. **N_eff = 1** (shares the pair's falsifier). Whole-book: TLT puts, USO longs, bank puts **all paid on 9/1's tape at once** ⇒ book N_eff ≈ 1 incl. energy — $275 added to that one bet, small, not diversifying |
| Registered alternative | Nov-20 $70P ×1 ≤ $2.35 (80 DTE, in-band; ~1 month post-print vs Dec's ~2) — quote-able, needs its own [Approve] to fill |

**Chain pull — basis and time:** `AGENTS/TERRY/scripts/chain_fetch.py WAL <expiry> --type put --legs 70 --no-cache` (yfinance), **2026-09-01 17:28 ET, post-close.** Dec-18 $70P **bid 2.05 / ask 2.75 / mark 2.40**, IV 35.3%, OI 31, vol 6, **freshest print 8/27 11:25 — a stale, thin strip (29% wide)** · Nov-20 $70P **1.70 / 2.35 / 2.02**, IV 37.6%, OI 28, printed 9/1 11:16 · Sep-18 $70P 0.20/0.40, $67.5P 0.10/0.25. **REGINALD's reads reconcile** (same asks; his Dec-18 "$2.50 last" is the 8/27 print). Underlying: WAL $77.26 (`snapshot.py`, 17:29 ET; 30d range 77.26–83.90 — today is the low; below the 20/50/200d MAs).

**What the card says that Will should hear before approving the ticket (§8, not buried):** this desk's own 8/20 `REG-T-02_FIRE_PROCEDURE.md` §3 pre-registered *"a fire does NOT re-open the Sep-18 cores — these legs have a STRIKE problem."* The WAL desk's EV **$75.96** sits **$5.96 above the $70 strike** — the roll pays only on an ~8% overshoot of the owner's central case. Risk-neutral P(WAL < 70 at Dec-18) **31.6%** vs 2-yr unconditional base rate **30.9%** (n=424 overlapping 76-session windows — a shape read, not a probability) ⇒ **a fair-priced tail, no base-rate edge**; BE $67.25 (−13.0%). RISK_RULES #21 said in those words: same underlying · same strike · later expiry ⇒ a ROLL (tenor band exempt), but the close-leg is held so no proceeds offset. **The ruled shape is Will's; the card records that it is not TERRY's construction preference and is the cheapest correct version of what was asked.**

**For `PROME/GATES.tsv`:** register the card's fire from this packet — `TRY-WAL-ROLL70` · state STAGED (approve-in-principle 9/1) · fire = first green WAL day w/ ask ≤ $2.75 while REG-T-02 FIRED · guard = REG-T-02 EXIT ≥81.90 ×3 · owner TERRY (grades the fill; REGINALD grades the exit) · review = each session until filled or REG-T-02 exits. I do not edit `PROME/`.

## 2. WQ-94 — `TRY-MGMT-USO135C` · memo `AGENTS/TERRY/setups/USO-135C_rule20-management_2026-09-01.md` · commit `ee62261c6`

**Live:** USO **$141.00** close 9/1 (+5.46%, 30d high) · 135C **bid 12.10 / ask 12.50 / mark 12.30**, IV 47.1%, OI 2,146, vol 530, 3.25% wide, no quote flag (`chain_fetch USO 2026-10-16 --type call --legs 135 --no-cache`, 17:28 ET) · pair **$2,460 at mark = +$1,038.67 / +73.1%** on $1,421.33 (FORGE 8/29: bought 8/03 @ $7.11 — entry *date* now known; entry *decision* stays UNRECOVERABLE, not reconstructed) · $6 ITM, delta ≈ 0.65, **theta ≈ −$21/day on the pair and accelerating**. **Forward max loss = the remaining mark, $2,460** (#20(d)), not the basis.

**The named exit / target / time stop — three OR-joined terms, TERRY rec = A + B($135) + C:**
| | Term | Why that number |
|---|---|---|
| **A — HARVEST** (RISK_RULES #9) | sell **ONE** on a resting GTC limit **≥ $14.25** | **one contract at $14.25 = $1,425 ≥ the pair's whole basis** ⇒ the second rides on house money. +$1.95 from mark ≈ USO ~$144 — inside one 5-session σ (6.9%) |
| **B — GIVE-BACK BACKSTOP** | USO regular-session **CLOSE < $135.00** (the strike) ⇒ sell BOTH at the next open. Alt width for Will: < $130 | below the strike the calls are 100% extrinsic again — BRENT's own 8/21 line: *that argues for CLOSING, not rolling.* Noise cost measured (#19): 5-session p10 **−6.5%** (n=250); >4% give-back from a running peak **7× in 128 bars** since 3/1 ⇒ B will probably fire if the ride stalls — by design, it converts "ride" into "ride while ITM" |
| **C — TIME STOP** | **Fri 2026-10-09**, sell whatever remains, unconditional | IRA auto-exercise of an ITM call = 200 sh @ $135 = $27k; do not let the broker choose the price. No roll pre-registered (8/21 HOLD-DON'T-ROLL stands) |

**No add, no roll, no new rail.** #23: today's driver (WTI +5.7% vs a risk-off/inflation bid) is **BRENT's to name in figures** — until named, no add is proposable and none is. Not coupled to `TRY-EXIT-USO35` (⚠️ whose title is stale — FORGE 8/29 shows **37 sh**, not 35; flagged, re-base next pass). **Will's menu on the memo §6:** A+B(135)+C (rec) · B at $130 · A+C only (accepts round-tripping — recorded as a choice, not an omission) · REJECT (then #20(a) stays violated ×2 and STATUS keeps saying so). **The 8/27 HOLD governs until he picks.**

## 3. WQ-95 — QQQFADE archive: **ALREADY EXECUTED 8/27** (`543f36a74`, Will-ruled in-session *"archive the QQQFADE card"*). Archive path **`AGENTS/TERRY/setups/_archive/WILL_qqq-downtrend-putspread_2026-07-30.md`** (bannered RETIRED 8/27, TRADE_BOOK closure row 8/27). **Tonight:** its INDEX row was still in the LIVE table → moved to the ARCHIVED table (`ee62261c6`). Nothing else to move; `$0` build-to-retirement.

## 4. `GATE-TERRY-007` — OWNER GRADE (card `setups/FLOW-TRIGGER_duration-TLT-put.md`, RULING B/C block; commit `25a86b4f2`)
**8/26 `4.66` · 8/27 `4.67` · 8/28 `4.73` · 8/31 `4.75`** — FRED `fredgraph.csv?id=DGS10&cosd=2026-08-18`, pulled 17:29 ET. All ≥ 4.50 ⇒ none qualifies; RULING B no trigger; RULING C count not started. **Counter `0 of 5`. Your 8/28 consumer read agrees and is superseded by this grade.** The 8/27 direction note closed the other way — 8/31 4.75 is the window's HIGHEST print; gate 25bp away. **9/1 official unpublished (T+1) — UN-GRADED, owed ~9/2 4:15PM.** Moot-risk: ~21 sessions to 9/30, `NO-VERDICT` if expiry beats a count that never started. 004 live mark (moment): TLT 81.87, 77P 0.05/0.06 ⇒ ≈ $137.50 on 25× vs $212.50. **`GATES.tsv`: `review_by` → 9/2 for the 9/1 official, then weekly at T+1; owner's last grade 9/1 through 8/31.**

## 5. Inbox: **11/11 drained** (10 at boot + your 9/1b WQ-99 cc mid-session). Dispositions in `25a86b4f2`'s message and STATUS ⑤. Two need you to know: **(a) COR-20260828-01 receipted APPLIED** (my 8/27 STATUS carried WALTER's 86.36; struck → 87.84 / −6.94%). **(b) Disclosure:** the 9/1b packet landed mid-session and my drain glob moved it to `processed/` **before I read it**; read immediately after, in place — FYI-only, consumption real, order wrong; recorded because it is the CHECK-I false-consumption shape. Also: REGINALD's ~Oct-1 WAL Q3-date confirm offer **ACCEPTED** (packet `78c9b16c1`, carve-out ①); DAEDALUS anti-rot **ENCODED** (`boot.py` stale flag now substring-matched — the 3 rows he named flag on re-run); DAEDALUS P1 read-cap **partial**: STATUS 90,236 → **37,415 B** (166% → 69% of cap; 5 self-declared-history chunks rotated verbatim + crc32 → `archive/STATUS_ARCHIVE_2026-09-01.md`); **`SETUPS.tsv` (98,886 B) / `TRADE_BOOK` / `RISK_RULES` not split — why not in the commit: a TSV rotation changes what `ledger_sweep` A reads and needs its own cold pass; owed next closeout.**

## 6. Commits (all TERRY-scoped + carve-out ①; verified `git log -1 --format=%h -- <path>`)
| hash | what |
|---|---|
| `ee62261c6` | the two cards + INDEX/SETUPS/TRADE_BOOK/STATUS/PAPER_BOOK + STATUS archive |
| `25a86b4f2` | 007 grade on the TLT card · 11 inbox renames · corrections receipt · boot.py · VIXCS β fix · SIGNALS +2 |
| `78c9b16c1` | TERRY → REGINALD packet |
| *(this file)* | committed by author, path-scoped |
`ledger_sweep` rc=0 · `claim_check --check weekday` clean · ledger nudge answered in `ee62261c6` · **NOT pushed** (your sweep).

## 7. Could not do / not done
- `TRY-BRENT-REFINER` fill status `[POSITION_STATE_UNKNOWN]` — VLO absent from the 8/29 FORGE reconcile; not chased tonight.
- Row 58 (`TRY-EXIT-USO35`) re-base to 37 sh + A2 base rate — not tonight.
- No `PROME/`, `FORGE/`, `AGENTS/WAL/`, `AGENTS/REGINALD/` file touched except the two packets.

— TERRY *(self-authored packet, root `CLAUDE.md` carve-out ①; committed by author)*
