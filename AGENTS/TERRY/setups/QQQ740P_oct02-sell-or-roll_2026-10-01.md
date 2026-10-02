# SELL-OR-ROLL CARD — QQQ $740P Oct-02-2026 ×4 (Fidelity IRA) — expires FRIDAY 10/02, payrolls day

**Date:** 2026-10-01 Thu, written from 16:23 ET (`date` 16:23:06; live reads 16:19:17–16:23:01 below). **Session:** TERRY interactive (Will in the window) on PROME `prome-2f`'s ask 1 (WQ-347 workstream).
**Id:** `MGMT-QQQ740P-OCT02` (management card on a line Will opened by his own hand; no SETUPS row — that ledger is at 97.8% of its read budget, rotation owed by Mon 10/05).
**Thesis owner:** Will (no agent thesis on file — off-thesis class, `FORGE/STATUS.md` § Off-thesis).
**Terry verdict:** 🔴 **SELL-OR-ROLL BY FRI 10/02 15:00 ET — desk lean SELL in the first hour after the 09:30 open.** Holding into Friday's close is BAD STRUCTURE: worthless above 740, and below 740 an exercise into a 400-share QQQ short ($296,000) that sits in the IRA over a **weekend**. If Will keeps the bet, the roll that fits root rule #7 and construction rule #21 is **740P Oct-09 ×4** (≈ $4.34/ct net on tonight's screening marks, ≈ $1,736) — never another one-day roll.
**Confidence in the read:** Medium (vendor option quotes are screening grade; the 740P read moved 2.43 → 2.29 between 16:19 and 16:22 with the spot print unchanged — §2).
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** A card is a recommendation; the order is Will's (root rule #5).

---

## 1. Position (broker truth = Will; source = PROME transcription `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md`, Will's 16:15 ET end-of-day screenshot, ties to the cent at $36,077.04; ANVIL's FORGE reconcile in progress, not yet committed)

| Field | Value | Source |
|---|---|---|
| Line | **QQQ $740P Oct-02-2026 ×4, long** | transcription ① row "QQQ 740 Put Oct-02-2026 [NE]" |
| Basis | **$890.65 ($2.23 avg)** — opened 10/1 (Today's gain = Total gain = +$37.35) | same |
| Fidelity last | $2.32 ⇒ $928.00 | same; capture clock NOT shown |
| How it came about | A **ROLL by Will's hand** of the Oct-01 740P ×4 (same strike, one day later — a construction rule #21 roll in form). The Oct-01 four left the account for net ≈ **+$22.75** — **PROME's INFERENCE from the pending-cash change, not a fill** (no Activity view). | transcription ③④ |
| Fill price, fill time, order form (one two-leg order or legged) | **UNKNOWN** — not shown | — |
| Companion line | QQQ $735P Oct-05 ×5, basis $1,368.32, last $2.27 — **nine QQQ puts across Fri 10/02 and Mon 10/05** | transcription ① |
| Cash | $14,147.60 money market + pending $1,377.10 (was $2,245.00 at 12:24; −$867.90 = the roll) | transcription ①③ |

Will's roll took the one-day form the 11:05 and 12:5x cards marked ⛔ *"not recommended — the costliest time per session, and it puts this same expiry question back on the card tomorrow (construction rule #16)."* **Recorded, not graded** — a sale or roll before expiry is his standing practice (`USER.md`, 9/30 19:03 ET). This card is the "back on the card tomorrow" that note predicted.

## 2. Live read — 2026-10-01 after the close (moment property, construction rule #14; re-read at Friday's open)

| Item | Value | Basis |
|---|---|---|
| QQQ | **$742.03 (+0.31%)** close print ⇒ the 740 strike is **$2.03 out of the money** | `fetch.py price QQQ`, 16:19:17 ET |
| Vendor 740P Oct-02 bid/ask | **2.43 / 2.44** at 16:19:34 → **2.29 / 2.31** at 16:22:20 (last option trade 16:07) | `chain_fetch.py --no-cache` — **SCREENING ONLY** |
| Put–call parity on the 742 strike (16:22) | C 3.96/3.99 − P 3.13/3.14 ≈ +$0.85 ⇒ the option market priced QQQ ≈ **$742.85**, ~$0.80 above the close print — after-hours drift, which explains the 740P's $0.14 drop with no spot change | arithmetic (INFERRED; the feed shows no after-hours spot) |
| Four at the screening bid | ≈ **$916** (2.29 × 400) ⇒ ≈ **+$25 vs $890.65** (INFERRED, not proceeds) | arithmetic |
| **All of it is time value** | the put is out of the money, so every cent of the ≈ $2.29 decays to $0 by Friday's close unless QQQ falls below 740 | — |
| Friday's implied move | 742 straddle ≈ 3.98 + 3.13 = **$7.11 ≈ ±0.96%** (includes payrolls) | screening mids, 16:22 |
| VXN (Nasdaq-100 vol) | 22.63 (+0.76%) | `fetch.py`, 16:22 |

⚠️ **The live bid is BROKER-ONLY.** The vendor feed carries no bid/ask timestamp and on 9/11 read a bid ~10% high on the side being sold (`RISK_RULES.md` durable finding 5b). Will reads Fidelity's own bid before any order.

## 3. Payrolls timing — the only catalyst between now and expiry

- **September Employment Situation (BLS), Fri 10/02 08:30 ET** — on BOND's and LABOR's catalyst files (`AGENTS/BOND/docket/CATALYSTS.tsv`; `AGENTS/LABOR/docket/GRADING_CARD_20261002_NFP.md`). TERRY did not read the BLS schedule itself; two desks carry it independently.
- **These puts cannot trade until 09:30 ET.** The print lands an hour before the option market opens. There is no "sell before the print" branch — the four ride the print whatever Will decides tonight.
- At the open the line is worth roughly its intrinsic value plus about 6½ hours of time value. **Time value is the whole line,** so every hour after the open costs it unless QQQ is falling.

## 4. Value at a set of Friday QQQ levels (intrinsic = what a late-session sale fetches, near enough; at expiry exactly)

| QQQ Friday | vs $742.03 | Four 740P worth (intrinsic ×400) | vs $890.65 basis |
|---|---|---|---|
| $750 | +1.07% | $0 | **−$890.65** |
| $745 | +0.40% | $0 | −$890.65 |
| $742.03 | flat | $0 | −$890.65 |
| $740 | −0.27% | $0 | −$890.65 |
| $738 | −0.54% | $800 | −$90.65 |
| **$737.77** | **−0.57%** | **$891** | **breakeven** |
| $735 | −0.95% (≈ one implied move) | $2,000 | **+$1,109** |
| $730 | −1.62% | $4,000 | +$3,109 |
| $725 | −2.29% | $6,000 | +$5,109 |

Earlier in the session the line is worth MORE than this column (time value left); the column is the floor a sale near 15:00 converges to. Read the bid, not the table.

## 5. In-the-money expiry arithmetic in this IRA — why "hold" is not on the menu

| QQQ at Friday's 16:00 close | Four 740P held | Dollars |
|---|---|---|
| Above $740.00 | Expire worthless | **−$890.65** |
| Below $740.00 (even by $0.01) | OCC exercise-by-exception: the IRA **sells 400 QQQ at $740 that it does not own** | **$296,000 short** in an IRA, which cannot carry a short |
| Below 740, then the short is covered | **Covered at MONDAY 10/05's price — a WEEKEND sits in between** | **−$400 per $1 QQQ gap up**; a 1% gap (~$7.40) ≈ **−$2,960**, 3.3× the line's basis |

⚠️ **Fidelity's handling of an in-the-money expiry in this IRA is UNOBSERVED (D-60).** Every observed expiry-day "OPTION LIQUIDATION" row was out of the money; the Oct-01 four did not observe it either (QQQ closed $742.03, out of the money). Whether Fidelity sells the line for you before the close, exercises it, or restricts the account is UNKNOWN. **The only branches with a known outcome are SELL or ROLL before 15:00 ET Friday.**

## 6. SELL leg (desk lean)

- **Action:** sell to close QQQ $740P Oct-02 ×4, **limit at Fidelity's live bid**, in the **first hour after the 09:30 open** — and **no later than 15:00 ET** (hard stop).
- **Why early:** the line is pure time value with one catalyst. Once the 08:30 print is known, there is nothing left to wait for. If QQQ falls on the print, the open is when the gain is largest relative to the decay; if it rises, every hour bleeds what remains.
- **Floor:** if QQQ is below 740 at Will's read, do not accept a bid far below intrinsic (740 − QQQ).
- **Root rule #6:** selling a put is best on a **red** QQQ day (puts are richer). Friday's colour is unknown until the print; a sale on a green day is not a rule break (the rule governs buys) — it is a lower price, and holding to wait for red is a bet on the print, not a rule.

## 7. ROLL leg (if Will keeps the bet — his practice permits it)

**Form (construction rule #21): same underlying · same strike 740 · later expiry · same four contracts.** Tonight's screening marks; Friday's will differ. Net debit = buy at the ask, sell the Oct-02 at the bid.

| Roll to | Vendor 740P bid/ask (16:22) | Net debit/ct vs 2.29 | For four | Cash at risk after | Desk view |
|---|---|---|---|---|---|
| Oct-05 (Mon) | 3.69 / 3.72 | $1.43 | $572 | $1,488 | ⚠️ Stacks all nine QQQ puts on one Monday 15:00 decision (with the 735P ×5) — and is another near-one-day roll |
| **Oct-09 (Fri)** | **6.56 / 6.63** | **$4.34** | **$1,736** | **$2,652** | ✅ The roll the desk would build if Will rolls: staggers the lines (Mon 10/05 735P · Fri 10/09 740P) |

- **Do not chase:** no net debit above **$4.75/ct** for the Oct-09 roll without a fresh read (~9% over tonight's $4.34; Friday's figure moves with the print — re-price at the order). One two-leg net-debit order, never legged.
- **Per-card cap ($500 max loss, `STATUS.md` § Standing rules):** forward max loss now = the remaining mark (construction rule #20) ≈ $916 ≈ **1.8× the cap**; after an Oct-09 roll ≈ $2,652 ≈ **5.3×**. A SALE takes it to $0.
- **Cash:** an Oct-09 roll draws ≈ $1.7k from ≈ $15.5k (cash + pending). That is the cash the USO 150C ×1's exercise path leans on — see `MGMT-USO150C-OCT09` addendum (10/01 16:2x).
- **Root rule #6 on the BUY leg:** a put bought on a red day is the wrong colour; no direct measurement refutes the proxy tonight ⇒ it would be a recorded wrong-colour buy, **not** a legitimate break. Re-read the colour at the order. Non-Negotiable #6: no roll is pre-registered; Will's order is the explicit re-approval.

## 8. Why not / counter-case

The case for holding into the print is Will's QQQ downside view, which this desk does not own: a soft payrolls number could take QQQ below $737.77 and the four pay. The structural case against holding past the first hour: ≈ $916 of pure time value against a ±0.96% implied move, with the downside path ending in an un-observed IRA exercise over a weekend. The desk has no thesis and no fired trigger behind the line (durable finding 1).

## Decision

> **WQ-347 (Will), Friday 10/02:** SELL the four at Fidelity's bid in the first hour after the 09:30 open (desk lean), hard stop 15:00 ET — or ROLL them to QQQ $740P Oct-09 ×4 as one net-debit order, no debit above $4.75/ct (≈ $2.7k at risk, ≈ 5.3× the $500 cap). Not hold.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-02 Fri 09:47–09:50 ET: re-marked at the open after payrolls (PROME `prome-70`, Tier 1). The 10/01 text stands as written

**Positions as of the 10/1 capture.** Quotes are **SCREENING**. yfinance through `chain_fetch.py --no-cache --legs 740` passed the leg gate, but both feeds showed nothing live until 09:47. The newest option trades are stamped 09:30–09:35, so they may be up to about 15 minutes old. **Fidelity's bid governs.**

| Item | 09:47 | 09:50 |
|---|---|---|
| QQQ | $752.46 (+1.41% vs $742.03) | $751.98 (+1.34%) |
| 740P Oct-02 bid / ask | 0.24 / 0.25 | **0.14 / 0.15** |
| Four at the bid, after $2.60 fees | ≈ $93.40 | **≈ $53.40** ⇒ ≈ −$837 against $890.65 |
| Roll to the 740P Oct-09 (ask − Oct-02 bid) | 3.62 − 0.24 = $3.38/ct ≈ $1,352 | **3.13 − 0.14 = $2.99/ct ≈ $1,196** (inside the $4.75 no-chase limit) |
| Roll to the 740P Oct-16 | 6.63 − 0.24 = $6.39/ct ≈ $2,556 | — |

**Payrolls came in soft (+29K, LABOR) and QQQ rallied about $10. The four are now 1.6% out of the money, and their remaining value is falling by the minute: 0.24 → 0.14 between pulls.** The fees ($2.60) are no reason to hold. The sale nets a positive amount down to a $0.01 bid.
**Lean: SELL at Fidelity's bid NOW. 15:00 ET is the hard stop, not the target.** The only path that pays from here is QQQ falling 1.6% intraday, and the downside of that path is an in-the-money exercise into a weekend short (D-60). **If Will keeps the bet:** roll to the 740P Oct-09 for ≈ $3.0–3.4 a contract net. That's inside Thursday's limit, and QQQ is green, the right colour for the buy leg under root rule #6. It leaves ≈ $1.25–1.45k at risk, ≈ 2.5–2.9× the $500 cap, with no agent thesis behind it. Not Monday.

**APPROVAL REQUIRED — Will must approve/reject before execution.** Memo: `PROME/inbox/2026-10-02_from-TERRY_open-remarks-WQ347-357-360.md`.
