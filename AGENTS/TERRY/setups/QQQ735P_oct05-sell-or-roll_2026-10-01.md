# SELL-OR-ROLL CARD — QQQ $735P Oct-05-2026 ×5 (Fidelity IRA) — expires Mon 10/05

**Date:** 2026-10-01 Thu, written 11:10 ET (live read `date` 11:09:14). **Spawn:** PROME `prome-2a`, Tier 1, WQ-347 (Monday's half). **Id:** `MGMT-QQQ735P-OCT05` (management card; no SETUPS row).
**Thesis owner:** Will (no agent thesis on file — off-thesis class).
**Terry verdict:** 🟡 **SELL-OR-ROLL BY MON 10/05 15:00 ET — no action owed today.** Hold-to-expiry is not on the menu (worthless above 735; a 500-share short in the IRA below it). Today's figures are a moment read (construction rule #14); **re-read Monday morning** before Will acts.
**Confidence in the read:** Medium (vendor option quotes are screening grade; the live bid is Fidelity's).
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.**

---

## 1. Position (mirror `FORGE/STATUS.md`, ANVIL `33bc8c293`)

| Field | Value |
|---|---|
| Line | QQQ $735P Oct-05-2026 ×5, long — **BOUGHT 9/30 @ $2.73 limit, basis $1,368.32** (transcription row 13; a $2.52 limit was Verified Canceled, row 14) |
| Nature | **New size by Will's own hand** (root rule #5) — a single-leg buy, not a roll leg. Fourteen QQQ puts across two lines with the Oct-01 740P ×9 (`setups/QQQ740P_oct01-sell-or-roll_2026-10-01.md`) |
| 9/30 post-close mark | $3.52 / $1,760.00, +$391.68 |

## 2. Live read — 2026-10-01 11:09 ET (moment property, construction rule #14)

| Item | Value | Basis |
|---|---|---|
| QQQ | **$737.10 (−0.36%)** ⇒ the 735 strike is **$2.10 out of the money** | `fetch.py`, 11:09:14 |
| Vendor 735P Oct-05 bid/ask | $3.78 / $3.80 (last option trade 10:53) | `chain_fetch.py --no-cache` — **SCREENING ONLY** |
| Five at the screening bid | ≈ $1,890 ⇒ ≈ **+$522 vs the $1,368.32 basis** (INFERRED, not a fill) | arithmetic |
| VXN | 23.37 (+4.05%) | `fetch.py` |

## 3. The Monday rail (sell-or-roll, Will's standing practice — `USER.md`, 9/30 19:03 ET)

- **Hard stop: Mon 10/05 15:00 ET.** Sell at Fidelity's live bid, or roll as one net-debit order.
- **Exercise path if held:** a close below $735.00 ⇒ the IRA **sells 500 QQQ at $735 it does not own = $367,500 short**; each $1 gap up on Tue 10/06 = −$500. Fidelity's in-the-money handling in this IRA is **UNOBSERVED (D-60)** — the Oct-01 nine may observe it first if they are held today.
- **Roll form (construction rule #21):** same strike 735 · later expiry · same five. Indicative at today's screening marks (net = buy at the ask, sell the Oct-05 at the bid): **Oct-09 735P** 6.74 / 6.76 ⇒ **≈ $2.98/ct (≈ $1,490 for five)** · **Oct-16 735P** 9.61 / 9.67 ⇒ ≈ $5.89/ct (≈ $2,945). ⚠️ **Monday's net debit will be HIGHER than these**: the Oct-05 leg loses its time value by Monday while the far leg keeps most of its own. Re-price Monday.
- **Coordination with WQ-347:** if the Oct-01 nine are rolled to Oct-09 today, a Monday roll of these five to Oct-09 stacks fourteen puts on one Friday expiry. Desk preference in that case: Oct-16.
- **Root rule #6:** today is red for QQQ, the wrong colour to BUY a put leg and the right colour to SELL. Monday's colour is unknown — read it at the order, in figures.

## 4. Rules on this line, in figures

| Rule | State |
|---|---|
| Standing per-card cap ($500 max loss; `STATUS.md` § Standing rules) | Forward max loss = the remaining mark (construction rule #20) ≈ **$1,890 ≈ 3.8× the cap** — Will's own hand on 9/30, recorded |
| Durable finding 9 (every profit zone needs its own harvest rule) | ⚠️ **No P/L-keyed harvest exists on this line.** The line is ≈ +38% at the screening bid with nothing that fires on profit alone. If Will wants one, the desk's suggested form: **sell all five at any Fidelity bid ≥ $5.46 (2× the $2.73 fill) before Monday's stop** — a suggestion for Will to adopt or not, not a live rule |
| Durable finding 1 (deploy on a fired trigger) | The 9/30 buy had no fired trigger on file — recorded, not re-litigated |

## 5. Bottom line

Nothing is owed today. **Monday by 15:00 ET: SELL at Fidelity's bid (desk lean, for the same reasons as the Oct-01 card — no agent thesis, no trigger, every roll adds cash at risk) or ROLL to 735P Oct-16 as one net-debit order.** Hold is not on the menu.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-01 12:5x ET: re-read after Will's partial sale of the 740P (the 11:10 text stands as written)

**Trigger:** PROME `prome-0c` spawn, WQ-347 follow-up. This is a moment read (construction rule #14). **Re-read Monday morning before Will acts.**

| Item | Value | Basis |
|---|---|---|
| QQQ | **$738.78 (−0.13%)** at 12:51:01; $738.28 (−0.20%) at 12:52:30 | `fetch.py` |
| 735 strike | **$3.78 out of the money** at 12:51 (was $2.10 at 11:09) | arithmetic |
| Vendor 735P Oct-05 bid/ask | **$3.28 / $3.30** (12:50:53) | `chain_fetch.py --no-cache`, SCREENING ONLY |
| Five at the screening bid | ≈ **$1,640** ⇒ ≈ **+$272 vs $1,368.32** (INFERRED). Fidelity mark $3.80 / $1,900 `[≤12:24]` | arithmetic; FORGE |
| Indicative rolls (buy ask − sell $3.28 bid) | **Oct-09 735P** 5.99 / 6.03 ⇒ $2.75/ct ≈ **$1,375** · **Oct-16 735P** 9.00 / 9.01 ⇒ $5.73/ct ≈ **$2,865** | screening; Monday's debit will be higher (the Oct-05 leg loses its time value by Monday) |

**Does today's partial sale of the 740s change how the five are handled?** On structure, no. On context, three things move:
1. **If the 740P ×4 are SOLD today, these five are the IRA's only QQQ put line.** The 9/30 position was fourteen puts across two lines; it would become five on one line. The Monday decision then stands alone and is no longer stacked against a same-week roll. Desk lean is unchanged: **SELL at Fidelity's bid by Mon 10/05 15:00 ET**, for the same reasons (no agent thesis, no fired trigger, every roll adds cash). A sale at today's screening bid is ≈ +$272 on top of today's +$890.35.
2. **If the 740P ×4 are ROLLED to Oct-09 today,** the 11:10 coordination note stands: a Monday roll of the five should go to **Oct-16, not Oct-09**, so that nine puts do not share one Friday expiry.
3. **If the 740P ×4 are HELD into today's close in the money,** Fidelity's in-the-money expiry handling (D-60) gets its first observation on a 400-share line. Read that outcome before Monday: it decides what "held" means for a 500-share line ($367,500 short below 735).

**Unchanged:** the hard stop (Mon 10/05 15:00 ET) · the exercise arithmetic (500 sh, −$500 per $1 gap-up) · the per-card cap (forward max loss ≈ $1,640 at the screening bid ≈ 3.3× the $500 cap) · no harvest rule (durable finding 9; the suggested ≥ $5.46 form stands as a suggestion). Will's tranche-and-limit method today (three fills, one canceled limit) is his own order craft. The card does not prescribe it.

**APPROVAL REQUIRED. Will must approve or reject before execution.**

---

## ADDENDUM 2026-10-01 16:2x ET: refresh to Will's 16:15 ET end-of-day capture (moment read; re-read Monday morning)

**Source:** `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md` (Fidelity positions, after the close). Quantity and basis unchanged: ×5, $1,368.32.

| Item | Value | Basis |
|---|---|---|
| QQQ close | **$742.03 (+0.31%)** ⇒ the 735 strike is **$7.03 out of the money** (was $3.78 at 12:51) | `fetch.py`, 16:19 ET |
| Fidelity last | **$2.27 ⇒ $1,135.00; −$233.32 / −17.06% total; −$650.00 today** | broker view |
| Vendor 735P Oct-05 bid/ask | **2.19 / 2.24** (16:19:50) ⇒ ×5 at the bid ≈ **$1,095 ⇒ ≈ −$273 vs basis** | `chain_fetch.py --no-cache --legs 735`, SCREENING ONLY |

**What changed since 12:5x:**
1. **The 740P ×4 were rolled to Oct-02, not sold and not rolled to Oct-09.** So the IRA carries **nine QQQ puts on two dates two sessions apart**: ×4 740P Fri 10/02 (`MGMT-QQQ740P-OCT02`) and these ×5 735P Mon 10/05.
2. **Monday roll destination:** the 12:5x note said *"Oct-16 if the ×4 go to Oct-09."* That condition can now only arise Friday. **If the ×4 are rolled to Oct-09 on Friday, a Monday roll of these five goes to Oct-16; otherwise Oct-09 is open.** Re-price Monday.
3. **Payrolls (Fri 10/02 08:30 ET) is the main move between now and Monday's stop.** Both QQQ put lines ($2,258.97 of combined basis) ride the same print.
4. **Harvest suggestion (≥ $5.46, 2× fill)** is now far — the line is under basis. It remains a suggestion, not a rule (durable finding 9).

**Unchanged:** hard stop Mon 10/05 15:00 ET · exercise arithmetic (500 sh / $367,500 short below 735; −$500 per $1 gap) · D-60 UNOBSERVED (the Oct-01 four ended out of the money, so they observed nothing) · forward max loss ≈ $1,095 at the screening bid ≈ 2.2× the $500 cap · desk lean SELL by Monday 15:00 ET.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-02 Fri 09:47–09:50 ET: re-marked after payrolls (PROME `prome-70`). The text above stands as written

**Positions as of the 10/1 capture. Quotes are SCREENING** (yfinance, possibly up to about 15 minutes old; Fidelity's bid governs).

| Item | 09:47 | 09:50 |
|---|---|---|
| QQQ | $752.46 ⇒ the 735 strike is **$17.5 (2.3%) out of the money** | $751.98 |
| 735P Oct-05 bid / ask | 0.55 / 0.56 | **0.43 / 0.44** |
| Five at the bid, after $3.25 fees | ≈ $271.75 | **≈ $211.75** ⇒ ≈ −$1,157 against $1,368.32 |
| Roll to the 735P Oct-09 | 2.46 − 0.55 = $1.91/ct ≈ $955 | 2.20 − 0.43 = **$1.77/ct ≈ $885** |
| Roll to the 735P Oct-16 | 5.25 − 0.55 = $4.70/ct ≈ $2,350 | — |

**Lean: SELL. Today is better than Monday on the arithmetic.** Almost all of what's left is time value, and Monday's session holds about one day of it. Unless QQQ falls about 2.3% by Monday, most of it runs off over the weekend. Selling a put on a green QQQ day gets a lower price, but it's not a root rule #6 break, because the rule governs buys. The hard stop stays **Mon 10/05 15:00 ET**. If the 740P ×4 are rolled to Oct-09 today, any roll of these five goes to **Oct-16**.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-07 Wed 11:1x ET: DOCKET L592 — the expiry date has passed; the OUTCOME IS UNKNOWN to this desk (PROME wave-2 spawn, cloud session). The text above stands as written

| Item | Value | Basis |
|---|---|---|
| Expiry | **Mon 10/05** (the 15:00 ET stop on this card was the last sale point) | card § 3 |
| QQQ close 10/5 | **$756.20** ⇒ the 735 strike was **$21.20 (2.8%) out of the money** at the close | yfinance daily, `auto_adjust=False`, pulled 10/7 11:0x ET |
| What the tape says | Zero intrinsic value at the close. A contract still held at the close had no exercise path (out of the money). Whatever was realized depends on whether, when and at what bid Will sold before 15:00 | arithmetic |
| Broker record | **NONE.** No broker capture has reached this desk since the 10/1 end-of-day view. The 10/2–10/6 fills are unbooked on `FORGE/STATUS.md` | PROME spawn brief 10/7 |

⛔ **Not recorded as fact:** neither a sale nor an expiry. **State: outcome pending Will's Fidelity Activity view (WQ-347).** When it lands: book the fill or the expiry row here, on `setups/INDEX.md`, in `STATUS.md`, and in `POSTMORTEMS.md` (root rule #10). Basis for the P/L: $1,368.32 for five (§ 1).

`$0` MOVED · NO ORDER · no gate moved.
