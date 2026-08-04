# 📋 DEPLOY PACKET — CONVEX ARM · **STAGED PRE-CLOSE 2026-08-04 ~12:55 PM ET**

> # ⛔ **SUPERSEDED 2026-08-04 14:0x ET — DO NOT ACT ON THIS FILE.**
> **Live packet → `2026-08-04_DEPLOY-PACKET-convex-arm-v3-GATE-LEGS-a-a2-MET.md`.**
> **Why:** §0 below poses the fillability question as OPEN and states *"I am deliberately not proposing the fix."* **It has since been answered and ratified.** The unverified 16:00-vs-16:15 question in §0/§24 is **RESOLVED: `^OVX`'s final bar is 16:00** (`^VIX` runs to 16:10; **OVX does not**) ⇒ **the v2 window was ZERO minutes, not 15**, and **DEPLOY GATE v3** was ratified by Will the same afternoon (`TRADE.md §DEPLOY GATE v3`).
> **RETAINED UNEDITED as the dated record** that the disclosure clause was staged ~3 hours before any fire, and that the fix was **declined at midday** rather than proposed on the afternoon it would have enabled a fill. **Its two blank verdict lines are left blank on purpose** — they were never graded under v2, and back-filling them now would manufacture a history that did not happen.

> # ⛔ **THIS IS NOT A FIRE, NOT A GRADE, AND NOT A REQUEST TO APPROVE ANYTHING YET.**
> **Leg (a) grades on the 16:00 CLOSE (Will-frozen 7/31, close basis). The close does not exist. Leg (b) grades on a re-pulled chain at fill.** Both verdict lines below are **deliberately blank.**
>
> **Why this is staged 3 hours early:** DEPLOY GATE v2's disclosure clause requires the three figures **IN FIGURES BEFORE THE FILL**, and *a pre-fill disclosure assembled AFTER a fire has already failed at the moment it exists to work.* On 8/3 the figures were staged five hours ahead and the clause worked on its first live test. **Same discipline here.**

**For:** Will [Approve] · **From:** BRENT · **Structure by:** TERRY (`TRY-BRENT-USOARM`) · **Independent check:** PROME
**Arm clock:** day **13 of 20** · 7 sessions after today · **expiry Thu 2026-08-13**

---

## 🔴 READ FIRST — A STRUCTURAL QUESTION THAT MAY DECIDE WHETHER THIS CAN FIRE AT ALL

**Leg (a) is only knowable at ~16:00. Leg (b) requires a live chain AT FILL. USO options stop trading at 16:00.** The gate fires on *"the FIRST session satisfying BOTH,"* and I have held that leg (a) must fire again on the session that actually fills.

**⇒ Those may not be jointly satisfiable on a same-session basis.** You cannot fill after knowing the close, and deferring to the next open doesn't fix it — leg (a) would then need N+1's close, which lands after N+1's fill window. **It is circular.**

⚠️ **On 8/3 this did not bite, and that is the part that concerns me: PROME's 3.5-hour routing delay meant there was no chain anyway, so a COORDINATION failure may have masked a STRUCTURAL one.** I recorded the routing delay as the cause and never asked whether the gate could have fired even with perfect coordination. If this is right it is the same class as the gate v2 *replaced* — `[[finding_compound_gate_jointly_unsatisfiable]]` — the old cooldown gate failed by **anti-correlation**; this one may fail by **timing**.

**⛔ I AM DELIBERATELY NOT PROPOSING THE FIX.** There is an obvious one — treat leg (a) as fired pre-close when it is through the line by a margin the final minutes cannot plausibly reverse, confirming on the official close. **Today would qualify trivially.** But **proposing a fillability fix on the afternoon it would enable a fill is exactly the trap TERRY refused this morning** (relaxing a guard to fit a preferred outcome), and making a gate fillable is **direction-relevant** — a loosening requiring your ratification and a paired tightening per #21(b), not my judgment at midday.

**There are 7 sessions after today. This can be ruled properly. If it cannot be resolved cleanly, the arm expiring un-deployed remains a CORRECT outcome.**
❓ **One fact I have NOT verified and will not assert:** whether USO options close at **16:00 or 16:15**. A 15:55 final OVX bar against a 16:15 options close leaves a real ~20-minute window and the problem partly dissolves. **Worth confirming before you rule.**

---

## 1. ⚖️ THE MANDATORY DISCLOSURE — three figures, staged before any fill

*(Item (i) extended today per THESIS v5.4 — the instrument/guidance binary is no longer sufficient. Direction-neutral: adds information, never permission.)*

### (i) STAGE-A LEG (i) — ⛔ **GUIDANCE ONLY. NO INSTRUMENT. And now CONTESTED FROM THREE DIRECTIONS.**

| Channel | Says |
|---|---|
| **Bessent** (Treasury Sec., CNBC, 8/4 AM) | *"We are in talks with the Iranians and I think there is a chance we may have a deal today or tomorrow to open the strait."* On tolls: *"freedom of movement."* |
| **Baqaei** (Iranian MFA, same morning) | *"To avoid any misunderstanding… We are not negotiating with the United States at this time. Our negotiations are with Oman."* |
| **Rubio** (same morning) | "progress" — but ***"no finality yet."*** |
| ★ **Reuters** (senior Iranian source in the talks) | Iran expects **CONTROL OF INBOUND SHIPPING**, visibility over outbound **with the ability to intervene**, exit clearance **through Oman after notifying Iran**, and **transit fees of $1–2M PER VESSEL**. Iran states the strait **cannot return to pre-war no-toll arrangements.** |

**⇒ Bessent is describing FREE PASSAGE. Iran is describing a TOLLED CORRIDOR IT CONTROLS.** Different objects — and the party with the anti-ship missiles is describing the second.

**⇒ NEW SUB-ITEMS (v5.4), answered:** **(a) Tolls?** reported **$1–2M/vessel vs a ~$250K pre-war war-risk cost = 4–8×.** **(b) Who clears inbound?** **Iran.** **(c) Who clears outbound?** **Oman, after notifying Iran.** **(d) War-risk / P&I restored?** **NO** — AWRP still 7.5–10% of hull, no P&I resumption notice. **(e) ⚠️ IS THE TRANSIT FEED LIVE? NO — see (ii). Recorded rather than skipped: an unmeasurable leg reported blank is indistinguishable from one that passed.**

**VERDICT: leg (i) UNMET on the strictest and the loosest reading. Textbook LESSONS #18 rhetorical, plus a substance gap that v5.4 says matters more than the signature question.**

### (ii) HORMUZ TRANSITS — ⛔ **NO RECOVERY, AND THE INSTRUMENT IS DOWN**

| Series | Latest | Baseline | % |
|---|---|---|---|
| PortWatch `n_total` | **10/day** (7/23) | 88/day | **11.4%** |
| `capacity_tanker` | **0 DWT** (7/23) | 2,330,676 DWT/d | **0.0%** |
| **Lloyd's List Intelligence** (wk 20–26 Jul) | **39 vs 82 = −52.4% WoW**; non-Iranian **−26.7%** | — | *"a near-term recovery in traffic is unlikely"* |

🔴 **THE FEED IS BROKEN: PortWatch `chokepoint6` has published nothing since 2026-07-23** while all 25 other chokepoints publish through 7/26 (clean `200`s ⇒ broken **partition**). **I own no transit instrument** — the script is FALCON's. **My spec's LEADING instrument is real-time AIS, which I have never had.** **Escalated to FALCON today as a blocking dependency.**
**⇒ Kill-test leg 2 — which v5.4 promotes to THE adjudicator — cannot presently be graded.** Stated plainly because it is the weakest point in tonight's case *in my own favour*.
🚢 **AND THE PHYSICAL LEG DETERIORATED AGAIN OVERNIGHT: MV MINOAN PIONEER struck ~20nm NE of Khasab — engine room, blackout, fire, ONE SEAFARER MISSING.** Third straight day of anti-ship fire in the same box. ⚠️ Counted conservatively per LESSONS #20: **at least two distinct hulls in three days, possibly three** (the 8/2-vs-Velos-Amber question is unresolved). **UKMTO primary not reached.**

### (iii) RESOLVING CRISIS, OR ORDINARY DIP? — ★ **ORDINARY DIP, ~85%** *(re-marked from 88% today)*

**Down 3pp** because the diplomatic channel genuinely strengthened — two cabinet officers, a dated timeline, the most advanced talks of the cycle. **Only 3pp** because the substance got clearer and worse for a reopening, and:

- 🔴 **THE CURVE STILL WILL NOT FLIP.** WTI M1−M3 **+$3.01**, Brent Oct−Dec **+$3.09** *(⚠️ INTRADAY)*. **−50.0% / −45.8% cumulative over two sessions and STILL BACKWARDATED. Jun-17 — the one genuine signature event of this regime — FLIPPED it into contango.** *A resolution flips the curve; a dip compresses it.*
- 🔴 **Institutional: zero movement.** War-risk 7.5–10% of hull; $3–10M/transit vs ~$250K pre-war; no P&I notice. ⚠️ **Weak evidence by construction** — underwriters need 2–4 weeks (#21(b)), so a genuine resolution would look identical today. **I discount this leg to near zero and weight the curve and transits instead.**
- ⚠️ **THE COUNTER I CANNOT ANSWER, in TERRY's words:** *is OVX at 53 the decay leg (a) was designed to buy, or the market correctly concluding the event is over?* **At n=0 genuine reopenings I cannot resolve that from evidence — which is exactly why the premise control is your [Approve] and not a threshold.**

---

## 2. GATE STATE — ⏳ **BOTH LINES OPEN**

| Leg | Test | State at ~12:55 ET | Verdict |
|---|---|---|---|
| **(a)** | OVX ≤ **58.6245** (−15% from the 68.97 post-arm peak, CLOSE basis) | **53.42** ⇒ **−22.55%** from peak. Needs a **+9.74% rally into the bell to AVOID firing.** ⚠️ **INTRADAY — NOT A GRADE.** | ⏳ **PENDING 16:00** |
| **(b)** | Net debit ≤ **33.0%** of width, live chain at fill | Graded 3× today and **NOT STABLE**: `125/135 ×1` 27.0 → 30.0 → 27.5% · `125/130 ×2` 30.0 → 34.0 → **38.0%** | ⏳ **PENDING RE-PULL** |

✅ **8/3's OVX close (57.20) is no longer single-source** — FRED `OVXCLS` published overnight at exactly 57.20, and the 68.97 peak re-derives from FRED's own series. **Instrument and value both have two witnesses.**

---

## 3. THE RECOMMENDATION — **~$300, USO Oct-16 `125C/130C ×2`, LIMIT $1.50**

| | `125/130 ×2` **← recommended** | `125/135 ×1` (alternative, built) |
|---|---|---|
| Limit | **$1.50** = **$300 exactly** | $2.38–3.00 |
| Leg (b) at limit | **30.0%** (3.0pp inside) | 23.8–30.0% |
| Max profit | **$700** | $730–762 |
| Breakeven | **126.50** (+8.6% from USO 116.45) | 127.38 (+9.4%) |
| Max value at | **USO 130 ≈ WTI ~85.1** | USO 135 ≈ WTI ~88.4 |

**Why the narrow:** the wide **never beats it by more than $92**; the narrow **beats the wide by up to $408** (at USO 130); crossover **USO ~134**. **USO 130 ≈ WTI ~85.1 — approximately a round-trip of this week's two-session gap** *(⚠️ corrected per PROME: a round-trip to exactly Friday's close pays **79% of max**, not max; max needs WTI ~85.1, modestly **above** the 7/31 close — the error fell in the DM-003 direction I registered myself, where the static USO/WTI conversion flatters USO)*. **Against a ~85% ordinary-dip read, the round-trip is the modal good outcome.** It also restores partial harvesting (sell one at 2×, hold one), closing the hole that cost `TRY-VIOLET-VIXCS` −$111.60.

**Why $1.50 and not TERRY's $1.65:** $1.65 × 2 × 100 = **$330, which breaches your ~$300 size ruling** — the limit had been anchored to the gate (33.0%) with nobody checking it against the size ruling. **Two constraints bind; both now applied.** If it will not fill at $1.50, that is **your** call (go to $330, or stand down), not something TERRY or I resolve by moving the limit.

### 🔴 THE ONE THING THAT IS YOURS TO ACCEPT OR REFUSE
**`125/130` puts the short leg at ~11.0% OTM against the ratified `~12–15%` band — ~1.3pp below it, and the departure WIDENS as USO climbs.** That band exists to preserve convexity. **It is outside a band you ratified, so it is not mine or TERRY's to override.** If you hold the band, **`125/135 ×1` stands as built.**

---

## 4. RISK — stated at full strength

- **Max loss = the debit, $300. Defined. No stop needed or used.** ~0.68% of the book.
- **★ N_eff = 1.** USO 35 shares (~$4,076 at $116.45), the Sep-18 150/165 spread, STNG, **and this**. All four die on one event. **Nobody should read a fourth leg as diversification.**
- **★ THE STANDING FLAG: the ~$4,076 of flat-price USO equity is the LARGE UNDEFENDED oil risk; this $300 arm is the small defined one.** The equity lost ~$440 over two sessions — **more than this entire trade costs.** **Not a trim recommendation** (root rule #7 — thesis intact), but if you want my judgment on where the real risk sits, it is there.
- **The Sep-18 150/165 is ~29% OTM at 45 DTE** — effectively a lapse. ⚠️ **FORGE fill-price reconcile owed, 5th session** — I still cannot state what it cost.
- **Root rule #6: SATISFIED, not broken.** Second consecutive ~5% down session; buying calls on a deeply red day is the textbook compliant entry. No break test invoked or needed.

---

## 5. ⛔ THE ARGUMENT I REFUSE TO MAKE

**"The arm expires 8/13, so take it."** That is the window-is-closing **CHASE** my own root-rule-#6 adjudication test calls illegitimate. **THE CLOCK IS NOT EVIDENCE.**
**If leg (a) does not fire, or leg (b) does not price at the limit, or the timing defect in §0 cannot be resolved cleanly — the arm expires un-deployed, and that is a CORRECT outcome, not a missed one.**

---

## 6. WHAT HAPPENS NEXT

1. **~15:55–16:00** — I grade leg (a) on the **official close**, verified against FRED `OVXCLS` when it publishes.
2. **TERRY re-pulls the chain.** The 3 readings above are not banked.
3. **If both legs clear → this packet goes to you completed, with the verdicts filled in.** Nothing fills without your [Approve].
4. **Separately and NOT tonight: rule on the §0 timing defect** and on the short-leg band departure.

**No capital has moved. No gate has fired. Nothing in this document authorises a fill.**

— BRENT
