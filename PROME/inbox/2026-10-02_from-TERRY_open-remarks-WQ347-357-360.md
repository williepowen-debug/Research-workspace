# TERRY → PROME · 2026-10-02 Fri · open re-marks: WQ-347 (QQQ 740P Oct-02 ×4) · WQ-357 (duration exit) · WQ-360 (TLT Dec-18 card), plus the 735P Oct-05 and USO 150C Oct-09

**Written:** 09:49–10:0x ET (`date` 09:49:03). **Spawn:** PROME `prome-70`, Tier 1. **Positions: as of the 10/1 post-close capture.** If Will has traded this morning, this memo can't see it.
**`$0` MOVED · NO ORDER · NOTHING APPROVED BY THIS RE-MARK · NO GATE OR THRESHOLD MOVED.** Every card goes back to Will as before (root rule #5).

## ⚠️ Quote basis — read first

- **At the open, both option feeds were still showing Thursday's quotes.** yfinance showed every QQQ, TLT and USO strike as `0.00/0.00 DEAD` from 09:31 to 09:46. CBOE's delayed feed was still showing the 10/1 16:14 quotes at 09:47. PROME got a heads-up message at 09:37.
- **The first live option quotes came at 09:47:19–09:47:50 ET** (yfinance through `chain_fetch.py --no-cache --legs`; every leg-gate check passed). The newest option trades in those pulls are stamped **09:30–09:32**, and QQQ moved from about $749.3 at 09:31 to $752.4 at 09:47. So these bids may be up to about 15 minutes old and are **SCREENING ONLY**: on 9/11 this feed read the bid about 10% high on the side being sold (`RISK_RULES.md` durable finding 5b). **Fidelity's own bid governs every order.**
- **The TLT 82P quote is the weakest one here.** Its last trade was on 10/1, it is 7% wide, and it carries the `NONMONO,DIRINC` flags. Will should confirm it on his screen.
- **Stock prices** (`fetch.py`, 09:47:26): **QQQ $752.46 (+1.41% vs $742.03)** · **TLT $78.06 (+0.44% vs $77.71)** · **TBT $42.04 (−0.36% vs $42.19)** · **USO $144.38 (−3.76% vs $150.02)**. Day colour: **QQQ green · TLT green · TBT red · USO red.**

---

## 1. `MGMT-QQQ740P-OCT02` — WQ-347 — four QQQ $740 puts expiring TODAY (basis $890.65) — lean **SELL NOW**

| Item | Value (09:47) |
|---|---|
| Distance to strike | QQQ $752.4 ⇒ the puts are **$12.4 (1.65%) out of the money** |
| 740P Oct-02 bid / ask | **0.24 / 0.25** (09:47:43; it read 0.21/0.22 at 09:47:19). Volume 2,901, open interest 31,326 |
| Four sold at the bid | $96.00 gross − $2.60 fees ($0.65 a contract) ≈ **$93.40 net** ⇒ **≈ −$797 against the $890.65 basis** |
| Fee floor | The fees are 2.7% of the proceeds, so the sale is clearly worth doing. It stays positive down to a $0.01 bid ($4.00 gross − $2.60 = $1.40). **The fees are no reason to hold.** |
| ROLL to the 740P Oct-09 (construction rule #21: same strike, a week later) | ask **3.62**, so the net is 3.62 − 0.24 = **$3.38 a contract ≈ $1,352 for four** (+$5.20 fees). That is inside Thursday's no-chase limit of $4.75 and cheaper than Thursday night's $4.34, because QQQ rallied away from the strike. It would leave **≈ $1,448 at risk ≈ 2.9× the $500 per-card cap** |
| ROLL to the 740P Oct-16 | ask 6.63 ⇒ **$6.39 a contract ≈ $2,556 for four** |
| Day colour, root rule #6 | QQQ is **green**, so this is the **right** day to *buy* a put (the roll's buy leg). Selling a put on a green day gets a lower price, but it doesn't break the rule, because the rule governs buys |

**Lean: SELL all four at Fidelity's bid now, by the 15:00 ET stop at the latest.** That's unchanged from Thursday, and the case is stronger now. What's left is about $96 of time value, and it runs off every hour unless QQQ falls 1.65% before the close. Holding to expiry has a known outcome only if they expire worthless. If QQQ closed below $740, the puts would be exercised into a 400-share QQQ short held over the weekend, and how Fidelity handles that is unknown (FORGE D-60). **If Will wants to keep the bet,** the Oct-09 roll costs $1,352 net on today's screen. It's within Thursday's limit and bought on the right-colour day, but it puts ≈ $1.4k at risk with no agent thesis and no fired trigger behind it (durable finding 1). Never roll to Monday: that would stack all nine puts on one Monday decision.

## 3. `MGMT-DURSHORT-EXIT-WQ291` — WQ-357 — TLT $82P Oct-16 ×1 + TBT 10 shares — lean **A, sell both today**

| Leg | Live (09:47) | Proceeds | vs basis |
|---|---|---|---|
| TLT 82P Oct-16 ×1 | TLT $78.05 ⇒ **$3.95 intrinsic** (in the money). Bid / ask **3.95 / 4.25** ⚠️ (weak quote, see above) | $395 − $0.65 ≈ **$394.35** | +$226.68 on $167.67 |
| TBT ×10 | $42.04 | **$420.40** | +$73.94 on $346.46 |
| **Both lines** | — | **≈ $814.75** | **≈ +$300.62** on $514.13 |

- **Bonds rallied on the payrolls print, which is the adverse direction for both lines.** At Thursday's 16:19 marks the exit came to ≈ $841. Today's green tape has cost ≈ $26 of that so far.
- **The day-colour test, done in figures before any fill as the card's §6 requires:** time value in the put at the bid = 3.95 bid − 3.95 intrinsic = **≈ $0.00**. Nothing about selling convexity cheap is being given up, because the put has no convexity left to sell. ⇒ **Selling on today's green day is a legitimate break of root rule #6, on one condition: Fidelity's bid must sit within about $0.10 of intrinsic** (floor = 82 − TLT − 0.10, ≈ **$3.85** at TLT $78.05). The 10/16 deadline is not the reason, and the card doesn't offer it as one. No hard guard is relaxed.
- **What waiting costs, on the card's own terms:** there's no time value left to earn, so waiting is purely a directional bet. The two lines are short about $7.8k of TLT (the put's delta ≈ −0.89 on a Black–Scholes model estimate ≈ $7.0k, plus TBT at 2× $420 ≈ $0.84k). That's **about $78 lost for every 1% TLT rises, and about $78 gained for every 1% it falls.** That bet is exactly what BOND's MET kill says to stop holding (durable finding 12: once a kill-switch fires, it stands). The auctions on 10/6–10/8 are where HENRY says the long end can reverse on supply. That's the argument for holding, and it's a view against the kill, not a structural reason. Holding also brings back the 10/16 problem: an in-the-money expiry in an IRA, where the broker's handling is unknown (D-60).
- **Lean unchanged: A. Sell the 82P at Fidelity's bid (floor intrinsic − $0.10) and sell the TBT shares, now that the open has settled, by 15:00 ET today.** BOND's rider still applies. The kill fired on dealer positions in the 3–6-year bucket (the belly of the curve), and dealers' long-end positions *fell* on the same print. That bears on how much weight the exit deserves, not on whether the rule fired.

## 4. `TRY-COND-TLTPUT-WQ339` — WQ-360 — PENDING WILL, NOT APPROVED — does today qualify on the card's own letter?

| Leg | Test | Today, at 09:47 | Met? |
|---|---|---|---|
| E-1 | Will's [Approve] on this card | **None on file** | ❌ |
| E-2 | Window from Fri 10/02 09:45 ET | It is 09:47 | ✅ |
| E-3 | TLT green, adjusted for distributions (no ex-date today; the last one was 10/1), **and TBT red** | TLT $78.06 > $77.71 (+0.44%) · TBT $42.04 < $42.19 (−0.36%), so the two agree | ✅ |
| E-4 | No red tape at the moment of the fill | Green at this read. **It must still be green at the moment of any fill** | ✅ at 09:47 |
| E-5 | Official 10-year Treasury yield (DGS10) not below 4.50 | Official 10/1: 5.24. Today's official figure isn't published until tonight (PROME's vendor read this morning: 5.18) | ✅ |
| E-6 | TLT ≥ $74.50 | $78.06 | ✅ |
| E-7 | Strike = the whole-dollar strike **at or just below TLT**, ask ≤ $2.45, total ≤ $491.30 | **With TLT at $78.06 the letter picks the $78 strike, not $77.** The Dec-18 78P ask is **2.45, exactly the limit**: ×2 + $1.30 = **$491.30, exactly the cap**. If the ask goes above 2.45, the card steps down to the **77P: ask 1.98 ⇒ $397.30** | ✅ at the boundary |

**Plainly: by the card's own conditions, today's tape qualifies (E-2 through E-7 all pass at 09:47 screening marks). The one condition missing is Will's approval (E-1). Nothing fills, nothing is ordered, and the card goes back to Will exactly as before.** ⚠️ **One thing Will needs to see:** the card's headline says "$77P", but its own strike rule picks the **78P whenever TLT is at or above $78.00**, and today the 78P costs the full $491.30 cap. If he approves, he should say which strike he wants. At $491.30 the 78P is about −0.48 delta each (≈ $7.6k TLT-equivalent for the pair, model estimate). At $397.30 the 77P is about −0.42 each (≈ $6.6k).
- **Day colour, root rule #6:** TLT green means this is the **right** day to buy a put.
- **If it's paired with a WQ-357 exit, the order is sell first, then buy.** Selling brings in ≈ $815 and the buy costs at most ≈ $491, so cash goes up by ≈ $323. The short-duration exposure goes from ≈ $7.8k (82P + TBT) to ≈ $6.6–7.6k (the Dec pair), the expiry moves 10/16 → 12/18, and the money at risk falls from ≈ $815 to at most ≈ $491. That's a re-strike and re-date, **not a construction rule #21 roll**. PROME's recorded lean is to reject it as an add. Treating it as a roll paired with the WQ-357 exit is Will's call.
- **Does HENRY's FORUM-7 verdict (PREMIUM-ABSORPTION, BOND co-sign pending) change the desk's view? It doesn't change the verdict or the structure. It sharpens *when* the card's evidence arrives.** About two-thirds of the 9/22–24 rise in the 10-year was term premium, and the "absorption" tag rests only on the 3–6-year dealer build. Dealers' long-end positions fell. If the premium is about supply, the **10/6–10/8 3-year, 10-year and 30-year auctions are the direct test**, and they land four sessions from now. That makes the card's **Variant E2** (fill only after BOND grades a failed auction, then the first green session) the form that best fits the evidence now. Buying today means buying the day before that test, on a soft-payrolls rally that runs against the thesis (construction rule #15: a green day carries zero thesis information). **The desk's view: CONDITIONAL as before. If Will wants the exposure, E2 is the better-evidenced trigger than today's colour. Either way, no fill without his word.**

---

## 2. `MGMT-QQQ735P-OCT05` — five QQQ $735 puts, Monday 15:00 stop (basis $1,368.32) — lean **SELL, today preferred**

| Item | Value (09:47) |
|---|---|
| Distance to strike | **$17.4 (2.3%) out of the money** |
| 735P Oct-05 bid / ask | **0.55 / 0.56** (open interest 12,118) ⇒ five at the bid = $275 − $3.25 ≈ **$271.75 ⇒ ≈ −$1,097 against basis** |
| Roll to the 735P Oct-09 | ask 2.46 (⚠️ `DIRINC` flag, last trade 10/1) ⇒ **$1.91 a contract ≈ $955** |
| Roll to the 735P Oct-16 | ask 5.25 ⇒ **$4.70 a contract ≈ $2,350** |

**Lean: SELL. Today is better than Monday on the arithmetic.** Almost all of the $0.55 is time value, and Monday's session holds about a day of it. Unless QQQ falls about 2.3% by Monday, most of that $275 runs off over the weekend. Selling a put on a green day gets a lower price, but that's not a rule break. Hard stop stays **Mon 10/05 15:00 ET**. If the 740s are rolled to Oct-09 today, any roll of these five goes to **Oct-16**, not Oct-09.

## 5. `MGMT-USO150C-OCT09` — one USO $150 call (basis $299.66), Fri 10/09 stop — lean **no action today; wait for BRENT**

| Item | Value (09:47) |
|---|---|
| Distance to strike | USO $144.38 ⇒ **$5.62 (3.9%) out of the money** |
| 150C Oct-09 bid / ask | **1.45 / 1.59** (9% wide, open interest 1,458) ⇒ one at the bid ≈ **$144.35 net ⇒ ≈ −$155 against basis** |
| Roll to the 150C Oct-16 | ask 2.95 ⇒ **$1.50 net ≈ $150** |
| Exercise path | A close above $150 now needs +3.9%. The cash-headroom constraint from 10/1 (≈ $525 over $15,000) **eases a lot**. A QQQ roll today no longer threatens the funding of a likely exercise |

**Lean: no action owed today.** USO is red, which is the wrong day to *sell* a call (it's the right day to *buy* one, i.e. a roll's buy leg). BRENT is attributing this morning's oil drop now, and that attribution is the input that matters here. Sell or roll by **Fri 10/09 15:00 ET**. The harvest suggestion (≥ $5.98) is now out of reach.

---

## Inbox and records (after delivery, 09:50–09:53 ET)

- **HENRY packets:** pre-open (superseded) and post-open (09:48: SPX gamma POSITIVE above an unchanged flip ~7,696, meaning dealers dampen moves; QQQ gamma not measured). Both read in full, logged in `board_log.tsv`, filed to `processed/`. The post-open read **supports the SELL lean on the 740s and 735s**: the only path that pays them is a sharp fall, and dealer dampening makes that less likely (INFERRED). Note that QQQ $740 maps to roughly SPX 7,650, which is below the flip.
- **FORGE D-68:** the card, INDEX and STATUS were already corrected on 10/1 (`5ce609f80`). The last uncorrected piece of the `ee04fbb26` record was the notes cell on `PAPER_BOOK.tsv` row PB-0002b ("CLOSED AT EXPIRY … ≈ −$103.33"). It now reads SOLD TO CLOSE, ≈ −$84.53, with the old text struck through.
- **FORGE D-71:** on `MGMT-QQQ740P-OCT01` and INDEX, the exit of the four Oct-01 740 puts is now **UNKNOWN / UNBOOKED, pending Will's Activity view**. The +$22.75 figure stays visible as PROME's inference only, and the derived −$747.91 (on the four) and +$142.44 (whole nine-contract line) are withdrawn. TERRY's 10/1 STATUS block still carries them, and today's STATUS block supersedes it.
- **Checks:** ledger sweep CLEAN (A–H), inbox at zero, claim_check clean, orphan check clean, read-cap rc=0. No BOARD scan was run beyond `boot.py` (0 unlogged action-line signals).

## Update 09:53 ET: USO 150C with BRENT's attribution folded in (`f8edd625e`)

BRENT (`5ddb2dfea` + `1ffe243cf`) traces the drop to a Reuters story about an EU **proposal** to release 50M bbl of diesel plus 50M bbl of IEA crude. **No decision was taken.** It's one wire, and the Commission's own statement carries no volume. USO is $145.08 (−3.29%) at 09:53, and the 150C bid is 1.37 (≈ $136 net, against $299.66).
**Lean: no sale today.** It's a red day, and this is a low driven by a headline. The call is now a cheap five-session option on "no decision". **Sell, don't roll, by Fri 10/09 15:00.** Sell sooner on the first green USO session, or right away if an EU volume is adopted. No roll: BRENT is on STAND DOWN and no trigger has fired.

## COMPLETION — TERRY — 2026-10-02
STATUS: ✅ DONE
CHANGED: this memo (+09:53 USO update); AGENTS/TERRY/setups/{QQQ740P_oct02,QQQ735P_oct05,DURATION-SHORTS_exit,TLT_dec18-77P,USO150C-KRE65P,QQQ740P_oct01}*.md, setups/INDEX.md, PAPER_BOOK.tsv, STATUS.md, board_log.tsv, inbox→processed ×2
RESULT: As of 09:47–09:50 (screening quotes): 740P×4 bid 0.24→0.14, lean SELL NOW (Oct-09 roll ≈$3.0–3.4/ct). WQ-357: 82P time value $0.00–0.03 ⇒ the green-day exit is a measured root rule #6 break, ≈$815–824, lean A. WQ-360 meets E-2–E-7, but E-1 (Will) is not met, and the strike flips between 77 and 78 at TLT $78. 735P×5: SELL (today). USO 150C: no sale today, sell-not-roll by 10/9 (BRENT: EU release is a proposal). D-68 PB-0002b fixed; D-71 → UNKNOWN.
GAPS: Option quotes may be up to ~15 min old (both feeds were dark until 09:47); the 82P quote is weak. Fidelity's bid governs. Positions as of the 10/1 capture. KRE 65P not re-read.
WILL_NEEDS: WQ-347 sell/roll by 15:00 today · WQ-357 A/B/C · WQ-360 approve/reject (name 77P or 78P) · 735P by Mon 15:00 · his 10/1 Activity view (D-71).
FOLLOW-UP: Book Will's 10/2 fills into the cards once FORGE reconciles; Monday pre-open re-mark of the 735P (fresh gamma board from HENRY).
