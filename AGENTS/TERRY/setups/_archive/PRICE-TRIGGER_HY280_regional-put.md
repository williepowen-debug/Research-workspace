# FIRE CARD — KRE — Regional-bank puts (fresh deploy)
**Setup ID:** TRY-FIRE-001 · **Trigger class:** PRICE
**Thesis owner:** REGINALD (regional/CRE) + NEXUS (regime) · **Card pre-built:** 2026-06-26 · **Fired:** ____ (**never fired**)
**Terry verdict:** 🔴 **RETIRED (terminal) 2026-08-21 — Will-ruled on TERRY's own recommendation. Card DEAD; PREMISE PRESERVED UN-GRADED. `$0` at risk from build to retirement (57 days).** *(Encoded 2026-08-23. Ruling of record: `PROME/proposals/2026-08-21_retro-sweep-and-tryfire001-RULED.md` — Will's verbatim word: **"Rule the retroactive-sweep and TRY-FIRE-001 off your recs."** Delivered via `inbox/2026-08-21_from-PROME_TRY-FIRE-001-RULED-retire-preserve-premise-rebuild-respec-unblocked.md`.)*
> ⛔ **RETIREMENT IS INSTRUMENT-DEATH, NOT PREMISE-REFUTATION — and the distinction is the whole ruling.** The repricing this card was built to catch is **real and still unexplained**; REGINALD's measured NULL mechanism **strengthens** the preserve rather than closing it. **The premise is NOT graded, NOT scored as a miss, and NOT available to be cited as a refuted call.** The **not-credit-≠-nothing** caveat rides with every future cite: all of REGINALD's instruments measure **CREDIT**; the finding is *"not credit,"* never *"nothing."* **Rebuild gates stand as pre-registered — see § RETIREMENT below. Reviving this is a NEW card, never a resumed one (`RISK_RULES` #18).**
> ⛔ **NO POSITION ACTION IMPLIED OR AUTHORIZED.** The card held **`$0`** (the PB-0004 refusal stood). The book's KRE Sep/Dec puts and bank legs **predate this card and are untouched.** Any exit/roll/add is a **separate proposal → Will [Approve]**, on live marks, root rule #4.
>
> *Prior verdict, kept as the dated record:* 🔴 **NO FIRE** *(2026-07-30 — the entry trigger was **MET** and had been since 7/27; TERRY declined anyway. Header added by `scripts/ledger_sweep.py` check C, which caught that this line still read the unfilled template `CLEAN / CONDITIONAL / NO TRADE` while the card body already declared NO FIRE.)*
**Status:** STAGED / **unfired, $0 at risk** — PROPOSE-ONLY, Will [Approve] required (rule #5). Detection owned by LIQUID/SENTRY — ⚠️ ~~which did not deliver: the 7/27 cross never reached TERRY — found 7/30 by accident~~ **CORRECTED 2026-07-30 15:45: DETECTION FIRED CORRECTLY AND ON TIME; the failure is DELIVERY.** LIQUID's watcher logged `🚨 ESCALATION 🟡→🔴 HY OAS 281bps` at **2026-07-28 13:00** — FRED publishes T+1, so that is the **first possible opportunity**. It writes to a local log with **no routing leg to any consumer**. LIQUID owns the routing build. **TERRY does not re-own the ZONE-1 detection line.**

> **Why NO FIRE on a MET trigger** (full reasoning in the 7/30 section below, summary here so the header is not misread as a pending approval): HY path **268 [7/22] → 281 [7/27] → 284 → 287 [7/29]**, three consecutive obs ≥280. ~~quality-sorted CCC +32 > HY +19 > IG +3 = genuine-stress signature~~ **← WITHDRAWN 7/30, see §2 of the 7/30 section: that ordering is mechanically forced and inverts under normalization.** **The transmission this card is built on is not happening** — KRE **$76.15, 2.3% under its 6mo high**, flat-to-up across the exact sessions HY widened, so the setup's *"before the equity tape catches the spread move"* premise has the tape moving the **other way**; the card's KILL line sits **closer than its CONFIRM line**; and ~~the live credit story looks like **AI-capex vendor financing, not banks** (attribution routed to LIQUID + REGINALD, unresolved)~~ **→ ATTRIBUTION NOW RULED (LIQUID + REGINALD, 7/30): neither. Broad DM HY risk-premium beta 68–84%; AI cohort 15–30%; bank/CRE ~0%, confidence HIGH.** `finding_threshold_vs_mechanism` holds — the threshold fired on a mechanism this card was never built for — but the mechanism is **broad beta on a rate repricing**, not the AI-capex story TERRY had inferred. **Card stays STAGED, ZONE 2 deliberately empty.**

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** **HY OAS breaks ≥ 280 bps** (from ~276 baseline 6/24) AND sustains
  the level (not a single intraday print — thin-liquidity discipline). This is the credit-regime
  widening tell that pulls broad-regional transmission forward from the Q1–Q2 2027 base case.
- **One-line setup:** credit is repricing risk in real time — buy liquid regional-bank downside
  before the equity tape catches the spread move.
- **Structure:** **KRE puts**, **~3–6 month** expiry (capture the widening momentum, not the 2027 grind),
  **~8–12% OTM** strike ladder. KRE = most liquid regional expression; tight option spreads.
- **Why this expression:** HY-break is a *path/level* trigger, not a single-name event → ETF beta is
  the clean vehicle. Puts (not duration/TBT) because the channel is credit-spread, not rates.
- **Alternatives rejected:** single-name (WAL/OZK) puts = idiosyncratic, miss the broad move;
  equity short = unbounded + margin; long-dated 2027 puts = wrong tenor for a momentum break.
- **Max-loss budget:** $500 per card (set by Will 2026-06-26)
- **Invalidation (thesis/price/time):** HY round-trips back < 270 sustained → credit-stress false alarm.
- **Kill line:** HY back < 270 sustained, OR KRE reclaims prior range high → exit.
- **Confirm line:** HY sustains > 280 **and** KRE breaks key support **and** ~~CCC-HY ratio widening~~
  **CCC ÷ HY RATIO rising** (REGINALD/NEXUS corroboration) → hold / consider 2nd tranche on next red day.
  - ⚠️ **SPEC PINNED 2026-07-30 — this line was ambiguous and the two readings DISAGREED.** *"CCC-HY
    ratio widening"* was resolvable as a **difference** (CCC − HY) or a **ratio** (CCC ÷ HY). On the
    7/22→7/29 move the difference **widens** (713 → 726bp ✅) and the ratio **narrows** (3.660 → 3.530 ❌).
    **Pinned to the RATIO** on LIQUID's and REGINALD's independent concurring rulings.
  - **Why the ratio, and why this is not a convenience call:** ① **the difference is mechanically
    non-informative** — CCC sits ~3.5× the index level, so any *parallel* proportional widening is
    *guaranteed* to widen CCC−HY; it fires on exactly the case a corroboration leg exists to exclude.
    ② **The ratio is already the fleet definition** — REGINALD's `VX-REG-18.04` tripwire *is* a CCC/HY
    ratio on a 3.6× line, so adopting the difference here would have created a **second, disagreeing
    gauge of the same quantity**. ③ It asks the intended question ("is this quality-sorted?"), which is
    inherently proportional. *(`finding_ratio_gauge_denominator_branch`.)*
  - **Consequence as of 7/29: this leg does NOT fire** (3.530, and `VX-REG-18.04` is not armed).
    Under the withdrawn difference reading it would have fired **on a technicality, in the direction
    that fires** — which is why it was routed out rather than resolved alone.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY this at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** HY OAS ___ bps (≥280 & sustained?) [Y/N] · **CCC ÷ HY ratio** ___ (rising? [Y/N] — **ratio, NOT the difference; see ZONE-1 confirm line**) · `fetch.py fred BAMLH0A0HYM2`
- **Normalization check (added 7/30):** tier moves in **%**, not bp — ___ ; bp ordering is mechanically forced by level and proves nothing
- **Spot:** KRE $____ (as-of ____) · `fetch.py price KRE --json`
- **Green/red day check (rule #6):** KRE today ___% → puts on green ✓ / breaking & why: ____
- **Chain marks:** `chain_fetch.py KRE <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [spread/OI per chain flags — Y/N]
- **Broker position truth:** existing KRE puts in book (FORGE/STATUS shows KRE Dec/Sep/Aug ladder) — net new vs overlap? [check live]
- **Sizing:** `risk_calc.py --premium <mark> --max-loss <budget>` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] HY actually ≥280 & sustained (not near-miss) · [ ] Live marks < 15 min · [ ] Green/red OK
- [ ] Liquidity OK · [ ] Max loss ≤ budget · [ ] Position truth known (overlap with existing KRE ladder checked)

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---


## 🔴 2026-08-20 Thu ~09:4x ET — **THIS CARD'S KILL CLAUSE TRIPPED ON 8/14 AND NOBODY WAS READING. THE TAPE THEN TURNED IN THE CARD'S FAVOUR. BOTH ARE TRUE AND I AM NOT RESOLVING IT MYSELF.**

Found in a Will-directed opportunity sweep, not by detection — this card had been unread since 7/30.

### ① The KILL clause fired — on the letter, by one cent
**Kill, exact wording:** *"HY round-trips back <270 sustained **OR KRE reclaims prior range high**."*
The prior range high on 7/30 was **77.92 (7/16)**. **KRE closed 77.93 on 2026-08-14 — a new 6-month high, one cent through.** ⇒ **On the letter this card is DEAD as of 8/14.**
⚠️ **Note the asymmetry, because it is a specification defect and not a judgement call: the HY leg carries a "sustained" qualifier and the KRE leg does not.** A single close, by $0.01, kills it. **I am flagging that, NOT relaxing it** — `[[finding_confidence_priced_against_thesis_not_letter]]`: a card resolves on the letter you wrote, and a desk that waives its own kill clause because the tape later improved is doing exactly the threshold-shaving `ledger_sweep` forbids by name.

### ② And then the tape did precisely what this card always wanted — starting the next session
| date | KRE | vs 20d | vs 50d |
|---|---|---|---|
| 2026-08-14 | **77.93** ← new 6mo high, **kill trips** | +1.42 | +3.39 |
| 2026-08-17 | 77.39 | +0.84 | +2.65 |
| 2026-08-18 | 76.85 | +0.25 | +1.96 |
| 2026-08-19 | 75.00 | **−1.55** ← breaks 20d | +0.01 |
| **2026-08-20** (live ~09:4x) | **74.88** | **−1.63** | **−0.21** ← **breaks 50d** |

**−3.91% in four sessions; below BOTH moving averages for the first time in this window.**
🔑 **This matters because it is the EXACT leg whose absence was my stated reason for refusing the met trigger on 7/30.** That verdict read: *"The equity tape is not lagging — it is going the other way… above both 20d and 50d… flat-to-up while HY widened."* **That sentence is no longer true.**

### ③ Confirm line, scored honestly — 1 of 3, so this is NOT a fire either way
**Confirm = *"HY sustains >280 AND KRE breaks key support AND CCC÷HY ratio widening."***
| leg | state | met? |
|---|---|---|
| HY OAS ≥280 sustained | **275** [8/18 FRED] — widening 4 sessions (267 → 270 → 275) but **5bp short** | ❌ |
| KRE breaks key support | **74.88, below 20d AND 50d** | ✅ **NEW** |
| CCC ÷ HY ratio widening | **3.735** (1027/275) vs **3.79** [8/14] — **FALLING** | ❌ |

### ④ CREED-T-02 fired this morning and it does NOT rescue the premise — I checked, and it cuts the other way
`CREED-T-02` fired 2026-08-20 (matured-balloon share of newly-delinquent CMBS balances >50%, sustained: May 70% · Jun 65% · Jul 66%; routed CREED→REGINALD/LIQUID). **The tempting read — "CRE stress fires + HY widens ⇒ the bank/CRE leg is back" — is manufactured convergence and I am not making it.**
**CREED's fire is effective JUNE 2026 with a ~6-week detection lag.** That deterioration was **already in the data** when LIQUID and REGINALD independently attributed the 7/22–7/29 HY widening as **bank/regional/CRE ≈ 0%, HIGH confidence**. ⇒ **T-02 does not overturn that attribution; it sharpens the negative** — CRE was visibly deteriorating and broad credit still priced no bank leg. **That is evidence the transmission this card requires is NOT occurring.**
⚠️ **The one legitimate open question is REGINALD's**, not mine: does the owner re-read the bank leg given T-02? **REGINALD has been dark since 8/13, so that packet sits unread — the question is LIVE but UNOWNED.**

### ⛔ Disposition — WILL'S / PROME'S, not TERRY's
**No status token changed by this block. No gate moved, no threshold shaved, nothing proposed, `$0` moved.** Two clean readings exist and they conflict:
- **(a) DEAD on the letter** as of 8/14 — the defensible default, and my recommendation absent a ruling.
- **(b) The kill was a mis-specified tripwire** (unqualified 1-cent reclaim vs the HY leg's "sustained") that fired one session before the tape delivered the card's own confirm leg.
**I recommend (a) unless Will rules otherwise.** ⚠️ And note that (b) is not a free option: **`RISK_RULES` #18 binds at any rebuild — the pre-built "8–12% OTM, 3–6mo" structure does not survive a fresh build**, same finding as `TRY-FIRE-002`. **Reviving this is a NEW card, not a resumed one.**

---

## 🔴 RETIREMENT — RULED 2026-08-21 (Will), ENCODED 2026-08-23 (TERRY)

**Will's verbatim word:** *"Rule the retroactive-sweep and TRY-FIRE-001 off your recs."* → **recommendation (a) accepted in full.** Record: `PROME/proposals/2026-08-21_retro-sweep-and-tryfire001-RULED.md`.

**Terminal state:** built **2026-06-26** → retired **2026-08-21**. **57 days · NEVER ARMED · NEVER FIRED · `$0` at risk throughout.** The entry trigger was **MET** (HY OAS ≥280 sustained, 7/27–7/29) and TERRY **declined** — that refusal is the card's product and it is now graded by nothing, because nothing was risked.

### What retirement does and does not mean
| | |
|---|---|
| **Card / instrument** | 🔴 **DEAD, terminal.** Archived. Not a shelf, not a pause. |
| **Premise** | 🟢 **PRESERVED, explicitly UN-GRADED.** The repricing is real and still unexplained. **Not a refuted call; never to be scored as a miss.** |
| **Position** | **`$0` — nothing to unwind.** Book's KRE/bank legs predate the card and are untouched. |
| **Rebuild** | **Gates stand as pre-registered (below). A rebuild is a NEW card** — `RISK_RULES` #18 binds and the pre-built "8–12% OTM, 3–6mo" structure does **not** survive a fresh build. |

### ⭐ REBUILD CONDITION #1 — RE-SPECIFIED. **"REGIONAL" IS THE WRONG FRAME AND THE MEASUREMENT SAYS SO.**
**This re-spec was held deliberately and is now UNBLOCKED.** TERRY refused to rewrite a rebuild condition while the card's disposition sat with the approver — **order-of-operations, and PROME has put that refusal on the ruling record as correct.** The disposition has now been ruled, so the re-spec executes here.

**The measurement (TERRY, 2026-08-20, own numbers):** **KBE −4.05% ≈ KRE −4.19% — 14bp apart.** **C is 3rd-worst of 38.** **JPM and BAC are the STRONG-side outliers.** ⇒ **the selloff does not discriminate regional from money-center; if anything the large-cap tail is inside it.** A condition written against *"regional"* would therefore be satisfied or refuted by a distinction the tape does not draw.

| | old (retired wording) | **NEW — binds at any rebuild** |
|---|---|---|
| **Frame** | ~~"regional"~~ | **BANK-SECTOR** |
| **Reference vehicle for the frame test** | ~~KRE alone~~ | **KBE *and* KRE together** — a rebuild must show the move is **bank-sector-wide**, not a KRE-only artifact. If KBE and KRE diverge materially, the "regional" story is back in play and must be **re-argued, not assumed.** |
| **Disqualifier (new, from the same measurement)** | — | **JPM/BAC on the STRONG side while the sector sells off is evidence AGAINST a sector-credit mechanism**, not neutral. |

⛔ **The re-spec changes the FRAME ONLY. No level moved, no threshold shaved, no new trigger created, and it does not make a rebuild easier** — it makes the frame test *harder* by requiring two vehicles to agree where one was required before. **`$0` moved.**

### Rebuild gates — UNCHANGED, restated so they survive the archive
The falsifiable re-entry table above (§ *Restated re-entry conditions*, 2026-07-30) **stands verbatim as the rebuild spec**, now read under the BANK-SECTOR frame. In PROME's summary form: **a named mechanism + persistence (n≈7) + credit confirming — or the vehicle changes.** Plus the card's own explicit NON-datums, which survive retirement:
- ⛔ **KRE breaking support ALONE is not a re-open datum** (7/29 showed it can be purely rate-driven).
- ⛔ **Another leg of HY widening ALONE is not a re-open datum** — *the whole finding is that HY by itself carries no bank information.*

### ⚠️ ONE KNOWN SPEC DEFECT, CARRIED FORWARD DELIBERATELY AND **NOT** REPAIRED HERE
The **kill-tripped-with-qualifier-asymmetry** defect (`d98b9d8a8`): the kill clause's KRE-reclaim leg is **unqualified** while its HY leg says **"sustained"** — so the kill tripped on 8/14 on a **1-cent** reclaim, one session before the tape delivered the card's own confirm leg. ⛔ **This is flagged for the REBUILD SPEC and is deliberately NOT repaired on a retired card.** Repairing a spec on a dead instrument produces a corrected artifact nobody will ever run, and risks the rebuild inheriting a fix that was never tested against a live tape. **Whoever builds the successor must resolve the asymmetry explicitly — both legs qualified, or neither.**

### Open question that outlives this card (NOT TERRY's)
Does REGINALD re-read the bank leg given **`CREED-T-02`** (fired 8/20)? **That question is LIVE and belongs to REGINALD** — it did not die with the instrument. TERRY's read stands: T-02 **sharpens the negative** rather than rescuing the premise, because the deterioration it detects was *already in the data* when the bank/CRE ≈ 0% attribution was made.

**⛔ `$0` moved. No gate, no threshold, no verdict re-issued. Nothing proposed.**

---

## 🔴 2026-07-30 ~13:40 ET — **THE ENTRY TRIGGER IS MET. TERRY STILL SAYS DO NOT FIRE.** (surfaced from the WALTER backlog, not by detection)

### The trigger leg — MET

**ZONE-1 trigger, exact wording:** *"HY OAS breaks ≥280 bps AND sustains the level (not a single intraday print)."*

| Date | HY OAS (bps) | |
|---|---|---|
| 7/22 | 268 | |
| 7/23 | 277 | |
| 7/24 | 279 | |
| **7/27** | **281** | ✅ ≥280 |
| **7/28** | **284** | ✅ ≥280 |
| **7/29** | **287** | ✅ ≥280 |

**Three consecutive daily observations ≥280, monotonically widening, +19bp in five sessions.** That is *sustained*, not a single print. **The entry trigger as written is MET.** *(FRED `BAMLH0A0HYM2`, pulled 2026-07-30 ~13:30 ET.)*

~~**Quality-sorted, which is the genuine-stress signature, not a technical:** CCC **981 → 1013 (+32bp)** · HY **268 → 287 (+19bp)** · IG **78 → 81 (+3bp)**. Widening concentrates down the quality curve.~~

🔴 **WITHDRAWN 2026-07-30 15:45 — REGINALD, and the inference inverts under normalization.** *(Struck, not deleted: this was written into the card, `SETUPS.tsv` and `STATUS.md` as an affirmative stress signature.)* **My figures were all re-pulled and are correct ✅ — the inference from them was wrong.** Normalized:

| Index | 7/22 | 7/29 | Δ bp | **Δ %** |
|---|---|---|---|---|
| **BB** | 157 | 176 | +19 | **+12.1%** ← *largest* |
| HY | 268 | 287 | +19 | +7.1% |
| B | 285 | 303 | +18 | +6.3% |
| BBB | 96 | 100 | +4 | +4.2% |
| IG | 78 | 81 | +3 | +3.8% |
| **CCC** | 981 | 1013 | +32 | **+3.3%** ← *smallest* |

**CCC widened the LEAST of any HY tier; BB — the highest-quality, longest-duration, most bond-like tier — widened the MOST.** The absolute-bp ordering CCC > HY > IG is **mechanically forced by the level ordering** in *any* parallel repricing (CCC sits ~981bp, so it always prints the biggest bp move) and therefore **carries zero discriminating information.** There is **no flight-to-quality inside HY**; the move concentrates where **duration** lives. **That is a rate fingerprint, not a credit one.** *(`finding_normalization_choice_picks_opposite_winners` — the same datum, two normalizations, opposite verdicts.)*

⚠️ **This STRENGTHENS the NO FIRE while deleting one of my own stated grounds for it.** REGINALD flagged it explicitly rather than let the convenient half stand — logged that way here for the same reason. **The VIOLET KB-VIO cross-check I cited as corroboration inherits the same defect: it too was read in bp.**

### 🔴 TERRY VERDICT: **NO FIRE.** The trigger is met and the trade is still wrong.

**① The transmission this card is built on is DEMONSTRABLY NOT HAPPENING.** The one-line setup reads *"buy liquid regional-bank downside **before the equity tape catches the spread move**."* The equity tape is not lagging — **it is going the other way.**

| | |
|---|---|
| KRE | **$76.15** |
| 6-month high | **77.92 (7/16)** — KRE is **2.3% below its high** |
| 20d MA / 50d MA | 75.61 / 72.90 — **above both** |
| Last 8 closes | 75.89 · 75.98 · 75.60 · 75.15 · 75.73 · 75.52 · 76.79 · 76.18 — **flat-to-up while HY widened 19bp** |

**② ⚠️ THE CARD'S OWN KILL LINE IS CLOSER TO FIRING THAN ITS CONFIRM LINE.** Kill = *"HY back <270 sustained, **OR KRE reclaims prior range high**."* KRE at 76.15 vs a 6mo high of 77.92 is **within 2.3% of the kill clause.** Confirm = *"HY sustains >280 **and KRE breaks key support** and CCC-HY ratio widening"* — KRE breaking support is **not remotely true.** **When a card's entry trigger and its kill line converge, the premise is not transmitting.** That is the finding, not the trigger.

**③ ⚠️ MECHANISM MISMATCH — `finding_threshold_vs_mechanism`. ✅ ATTRIBUTION NOW RULED (LIQUID + REGINALD, 2026-07-30 ~15:35, independent parallel lanes).** The card assumes HY widening = **broad credit stress → regional-bank/CRE transmission**. ~~The live credit story in the tape is **AI-capex financing**~~ — **that inference was WRONG TOO.** Of the +19bp:

| Attribution | bp | share | confidence |
|---|---|---|---|
| **Broad DM HY risk-premium beta** (US + Europe) | 13–16 | **68–84%** | Mod-high |
| AI / data-center HY cohort | 3–6 | 15–30% | Moderate |
| **Bank / regional / CRE credit** | **~0** | **~0%** | **HIGH** |
| Energy | ~0 | ~0% | **Low** (LIQUID's own instrument is XLE alone; disclosed) |

**BOTH of my candidate mechanisms fail. The card's premise is not merely unconfirmed — the bank/CRE leg is specifically ABSENT**, and I had inferred that only from KRE's *equity* tape; it is now established in the *credit* data (IG shows no BBB-tier discrimination: BBB +4bp vs IG +3bp, flat — where bank/CRE stress would surface first).

- **Geography, the strongest single piece (LIQUID):** Euro HY widened **+16bp = 0.84× the US move** vs a **0.55 median** across 63 comparable episodes (70th pctile). European HY has **~zero AI-infra issuance**; US-idiosyncratic episodes in the same sample print **0.10–0.37**. A US-AI-specific credit event predicts a *low* ratio; we observe a high one.
- **Tier shape says flow, not quality recognition:** BB +12.1% vs CCC +3.3% (CCC at **0.27×** BB's rate) — the inverse of a tail/default repricing. **HYG unmoved (−0.04%) on ~2× volume** = repositioning, not distress.
- **The AI cohort is arithmetically too small to be the driver:** ~4–6% of index MV, so **it would have to widen +320 to +475bp** to produce +19bp alone. It did not.
- **Bank side, REGINALD, ★ the sharpest datum:** on **7/29** — FOMC day, SPY −1.54%, Dow's worst since Apr-2025 — **WAL equity −3.53% while WAL's own junior preferred (WAL-PA) was +0.10%.** Same issuer, same session. WALTER's own "do credit instruments keep widening while equities fall?" discriminator gets a **hard NO on bank paper, on the one day it could have said yes.** *(This pair is 7/29 close-to-close and was never intraday — untouched by the restamp below.)*
  - ⚠️ **FIGURES RESTAMPED TO 7/30 CLOSES (REGINALD, 16:29 sweep).** The set I first adopted was his **intraday** pull, taken while the market was open; he sent the closes unprompted *because* I had adopted his counter-evidence rather than dropping it. **Closes: preferred basket** ZIONP **+0.95%** · OZKAP **+0.79%** · WAL-PA **+0.23%** · PFF **+0.93%** (~~mean +0.34% intraday~~) · **BKLN −0.05%** (~~−0.00%~~, floating/rate-immune — dispositive either way) · IG OAS +3bp.
  - **Honest counter-evidence, also restamped and it got WORSE:** WAL ~~−2.06%~~ → **−2.24%**, EGBN ~~−2.36%~~ → **−3.34%** (nearly a full point worse); KRE across the widening ~~+0.66%~~ → **+0.22%** (smaller, same sign). **Net: the equity leg of the counter-evidence worsened while the credit leg firmed — both point the same way, so `BANK-ABSENT` is unchanged and slightly better supported.** *I am recording the less flattering set because it is the current one.*
  - **REGINALD self-corrected one disclosed limit, narrowing it against himself:** his "no bank CDS reachable" is more precisely a **data-source gap, not an instrument gap** — his own STATUS tracks `iTraxx Senior Financials` (~95bps, >100bps line) with **no recorded vintage**, so it is too stale to cite and nothing in the verdict changes. Carried at his corrected weight.
- **The cause is rates:** FOMC held **9–3 with three regional presidents dissenting FOR A HIKE**; `^TYX` 5.096 [7/28] → **5.208 [7/30 intra]**, 30Y highest since 2007.

⚠️ **Asymmetry I am keeping on the card because it cuts against a clean story:** AI credit **is** the most stressed cohort in this tape — leading in **magnitude** by ~8× (CoreWeave's $2.6B DDTL repriced S+425–450/OID 99 → **S+550/OID 97 ≈ +140–165bp all-in concession** the day before commitments closed; CRWV CDS +>50% MTD) — while contributing only 3–6bp in **level**. My instinct was **correct about the locus of stress and wrong about the driver of the index number.** Both are true; only the second decides this card.

**④ CCC-HY "ratio" is SPEC-AMBIGUOUS and I will not resolve it in the firing direction. ✅ RESOLVED 7/30 — PINNED TO THE RATIO** (LIQUID and REGINALD concurring independently; adoption was mine and is now made in ZONE-1):
- **Difference** (CCC − HY): 713 → **726bp** = **WIDENING** ✅
- **Ratio** (CCC ÷ HY): 3.66 → **3.53** = **NARROWING** ❌ ← **binding**

**The card never defined which; it now does.** The difference is **mechanically non-informative** (CCC's ~3.5× level guarantees it widens on any parallel move) and would have created a **second, disagreeing gauge** against REGINALD's existing `VX-REG-18.04` CCC/HY 3.6× tripwire — which is **not armed** at 3.530. **⇒ the corroboration leg does NOT fire.** *(`finding_ratio_gauge_denominator_branch` / `finding_number_carries_threshold_unit_source`.)*

### 🔴 ~~DETECTION FAILURE — this reached me by accident~~ → ✅ **DETECTION WORKED. DELIVERY FAILED.** *(corrected 2026-07-30 15:45)*

~~Detection on this card is owned by LIQUID/SENTRY (ZONE-1, line 4). The trigger crossed on 7/27 and no signal reached TERRY.~~ **LIQUID's watcher fired correctly and at the first possible opportunity** — `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log`: `2026-07-28 13:00 🚨 ESCALATION 🟡yellow→🔴red HY OAS 281bps (as-of 2026-07-27)`. **FRED publishes T+1, so the 7/27 observation only became available on 7/28 — the cross was caught the same day it was knowable.**

**What failed is the ROUTING LEG: the watcher writes a local log and a state file that nothing outside `AGENTS/LIQUID/` reads.** It fired silently on the prior 6/29 cross (283bps) too. **LIQUID owns the routing build (a routing build, not a threshold change); it is owed at their next session. TERRY does NOT re-own the ZONE-1 detection line — it is real, not fiction.**

⚠️ **My half of this stands unchanged and is the part I own:** `STATUS.md` carried **"HY OAS 269 [7/20] — moved AWAY from the 280 line"** for **nine days** — **stale in the dangerous direction**, advertising the card as receding while it was crossing. I found the cross on 7/30 by accident while draining a 13-deep WALTER backlog. **Correcting the label from "detection" to "delivery" moves blame off LIQUID; it does not move any off me.**

### Status

**Card stays STAGED, unfired, $0 at risk.** ZONE 2 deliberately left empty — no live marks pulled, because I am not proposing an entry.

~~**Revisit only on:** (a) LIQUID/REGINALD ruling the widening is bank/CRE-driven rather than AI-capex-driven, **AND** (b) KRE actually breaking support.~~ **(a) IS NOW RULED — and it ruled AGAINST the card: bank/CRE ≈ 0bp, confidence HIGH.** The NO FIRE is no longer *"attribution unresolved, so decline"*; it is **"attribution resolved, and the mechanism this card needs is measurably absent."** Restated re-entry conditions, taken from the owners' own stated flip-datums so they are falsifiable rather than vibes:

| Re-open requires | Owner | Currently |
|---|---|---|
| **Bank junior-sub/preferred basket −≥2% over any 3-session window WHILE HY OAS is still widening** | REGINALD | mean **+0.34%**, 9/10 flat-or-up ❌ |
| **IG BBB OAS decoupling upward from the IG index** (bank/CRE stress surfaces here first) | LIQUID | BBB +4 vs IG +3bp — **flat** ❌ |
| IG index ≥+10bp with financials leading, or an actual bank CDS print | REGINALD | IG +3bp ❌ |
| **AND** KRE actually breaking key support | TERRY | 76.23, above 50d/200d ❌ |

⚠️ **Explicitly NOT re-opening datums (REGINALD, and I am adopting this):** **KRE breaking support *alone*** (equity, and 7/29 showed it can be purely rate-driven) **or another leg of HY widening alone** — *the whole finding is that HY by itself carries no bank information.* **If KRE reclaims 77.92, the kill line fires and this card lapses.**

**Watch, but NOT on this card:** `^TYX` 5.096 [7/28] → **5.208 [7/30 intra]**, +11bp in two sessions, 30Y highest since 2007. LIQUID flags a **duration leg re-arming that was absent from the move adjudicated above** (rates *rallied* 7/22–7/29, DGS10/DGS30 −6bp each, so duration drove none of it). **That is a forward mechanism change, and it lands on `TRY-FIRE-004` (long rates-vol), not here.** It does not retroactively alter this attribution.
