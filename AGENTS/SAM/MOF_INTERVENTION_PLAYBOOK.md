# SAM — MOF INTERVENTION PLAYBOOK + CARRY/PC SHARED-ANTECEDENT READ

**Created:** 2026-06-25 (Desktop Claude Code session; OpenClaw degraded, Prome coordinating)
**Owner:** SAM
**Type:** Durable reference (reusable across cycles). Live marks live in STATUS.md; this is the *method*.
**Companion:** § INTERVENTION STATUS in STATUS.md (live SAM-23 mark), thesis/THESIS.md (Channel 3 MOF), CHANGELOG CH-003/CH-011.

---

## S1 — MOF INTERVENTION PLAYBOOK

### 1. Escalation ladder — verbal tiers × USD/JPY zone

The MOF/FX-diplomat verbal sequence is a graduated ladder; each tier raises the conditional probability of a physical strike. As of 2026-06-25 we sit **pre-T1** (MOF silent 9+ days at 161+).

| Tier | Language | Typical USD/JPY zone | Read |
|---|---|---|---|
| **T0** | "watching FX with a sense of urgency" | any level | Noise / routine. No information. |
| **T1** | **RATE CHECKS** — MOF/BOJ phone banks for live USD/JPY quotes | ~161–162 | **Single strongest pre-action tell.** Historically precedes a strike by hours to ~1 day. |
| **T2** | "one-sided / excessive moves," "won't rule out any option" | ~162 | Escalation; strike plausible on further velocity. |
| **T3** | "decisive action," "ready to act 24 hours," "stand ready" | ~162–163 | Imminent. |

**Strike history (this cycle):**
| Date | Size (est.) | USD/JPY | Outcome |
|---|---|---|---|
| Apr 30 | ~¥5.48T ($35B) | 160.70 → 155.55 | Same-day reclaim (~5 yen) |
| May 6 (Golden Week) | ~¥4.3T ($28B) | 157.89 → 155.05 | Same-day reclaim (~3 yen) |
| **MOF official aggregate (Apr 28–May 27)** | **¥11,734.9B (~$73B)** | — | Largest round since 2022. No #3 strike since. |

Record weakest 161.96 (pre-1986 comparison). → A **3rd strike most likely lands in the 162–163 zone.** USD/JPY 165 reached *without* a strike = either near-certain imminent action OR MOF capitulation (stepped aside).

### 2. Speed/disorder trigger — the real mechanism (CH-011)

**MOF intervenes on DISORDER, not level.** Empirically confirmed this cycle: 6+ orderly sessions at 160+ (and now 9+ days silent) drew no strike. The discriminator is **velocity**:
- **Triggers:** ~2–3 yen run in 1–2 sessions, or a vertical break of **>1.5–2% / day** through 162/163.
- **Tolerated:** slow grind of ~0.2–0.4 yen/day (exactly the 2026-06-25 tape — 161.65, MOF silent).

Level alone ≠ trigger; *speed through the level* is. A re-derive of SAM-23 (intervention probability) must weight rate-of-change, not just proximity to 162.

### 3. FXY-stub behavior by zone

| Scenario | USD/JPY | FXY behavior | P&L read |
|---|---|---|---|
| **Slow grind up** | → 162 (FXY ~$56.4) | bleeds lower with the grind | Loss path; the USD/JPY-162.5 stop leg fires HERE |
| **Disorderly spike → MOF strike** | spike 162–163 then snap | **FXY pops ~2–3% intraday** on the ~3–5 yen reclaim | The convexity payoff — this is what the stub is positioned for |
| **165 no-strike (capitulation)** | runaway | FXY craters | Worst case; thesis tail breaks |

**Cleanest single tell intervention is imminent:** *reported rate checks* (Nikkei/Reuters "MOF conducting rate checks") + a T3 "decisive action / ready to act" line from the FinMin or FX diplomat.

> **⚠️ S1-A — AMBUSH-TACTICS AMENDMENT (2026-07-02, Reuters exclusive):** MOF has shifted to **unsignalled "ambush" intervention** — sources say it is deliberately abandoning telegraphed warnings, naming no line-in-the-sand, and targeting yen shorts by surprise; Mimura's verbal-warning stand-down since the Apr-May campaign is *intentional*, and Katayama has deliberately not escalated. **This inverts the ladder's evidentiary value:** escalation UP the ladder (a fresh rate-check report, a new T3 line) still raises P(strike) — but **ABSENCE of T1/T3 no longer lowers it.** Silence is loaded, not passive. Consequences: (1) the strike, when it comes, is a **gap event with zero lead-in** — the FXY-stub "pop" scenario arrives unhedged-able; entries must catch the follow-through, not front-run the gap (deploy-on-trigger unchanged); (2) wire silence on a spike day is weaker evidence against an op than before → **lean on the fast semi-confirm: BOJ current-account projections vs money-broker forecasts, ~2 business days post-candidate; hard confirm = MOF monthly (~month-end, 5 PM JST last business day)**; (3) the speed/disorder trigger (§2, CH-011) is UNCHANGED — ambush changes the *signaling*, not the *reaction function*.
>
> **⚠️ S1-A semi-confirm SCOPING NOTE (2026-07-11 verify — NOT-BUILD decision):** the "BOJ current-account projections vs money-broker forecasts" fast semi-confirm is a **manual/desk-sourced read, not scriptable by SAM.** Verified against a live sample of the daily series (`boj.or.jp/en/statistics/boj/fm/juq/d_release/jd/2026/jd20260327.xlsx`, pulled+parsed 7/11): the release carries **no explicit FX-intervention line item** — intervention settles ~T+2 through **"Treasury funds and others" (財政等要因)**, a large, noisy daily line (tax receipts, JGB settlements, pensions) that is uninformative *standalone*. The technique's entire signal is the **gap vs private money-broker (Tanshi) same-day forecasts** of that line — and SAM has **no automatable Tanshi-forecast source**. A `boj_current_account.py` script pulling the BOJ leg alone would fast-confirm noise. **Decision: do NOT build; retired from the script queue** (evidence + full scoping → `OPEN_THREADS_2026-07-09.md` §2). If a candidate strike fires, this semi-confirm runs as a *manual* step: pull the jd/jx XLSX for the T+2 settlement date and search the wires for the Tanshi-forecast-gap commentary (Reuters/Nikkei routinely carry it after real ops).

### 4. ⚠️ Stop-vs-payoff whipsaw (load-bearing risk-control insight)

Near the 162–163 intervention zone, a **hard auto-stop at USD/JPY 162.5 risks getting tagged at the worst tick — the disorderly spike — just *before* MOF reverses it 3–5 yen.** That is the exact move the long-FXY stub is *betting on*, so a resting order converts the convexity payoff into a realized loss at the spike high.

**Implication:** in the intervention zone the stop wants to be **discretionary/mental, not a resting working order.** Outside the zone (slow grind, no MOF chatter) a working stop is fine. This must be reconciled with how the broker stop is actually implemented (see STATUS broker-reconciliation Q3).

---

## X1 — CARRY-UNWIND vs PC MULTIPLE-COMPRESSION: SHARED-ANTECEDENT READ

*(Carry-side vantage. Answered independently of BROCK's PC-side read; reconcile separately.)*

**Verdict: CORRELATED-NOT-IDENTICAL.** Shared latent root only in the *disorderly-unwind tail*; independent — and often **opposite-signed** — in the base case.

**(a) Shared vs independent:** Not the same trade. They share a latent antecedent (global higher-for-longer / USD-funding & liquidity withdrawal) *only* in a violent deleveraging tail.

**(b) Shared mechanism (tail only):** a *disorderly* yen-carry unwind = repatriation + global risk-off + USD-funding/vol spike → cross-asset deleveraging that force-sells the same leveraged/illiquid alts complex (APO/ARES/BX) via funding-cost spike + redemption/mark pressure. **Aug-5-2024 template** (yen unwind → everything-down). In that path, carry-signal and PC-signal convergence collapses to ONE root.

**(c) Decoupling tests (the discriminators):**
- **Carry fires WITHOUT PC stress:** *orderly* yen appreciation — a successful MOF strike or a hawkish-of-priced BOJ — FXY +2–3%, carry shorts cover, but it's a contained FX move with no vol spike; US rates/credit unchanged → PC multiples untouched. **This is SAM's MODAL convexity path.**
- **PC compresses WITHOUT carry unwind:** a US-centric credit/rate event (Warsh-Fed higher-for-longer) compresses APO/ARES/BX multiples while **yen stays WEAK** — a wider rate differential keeps carry ON, yen weaker not stronger. **Opposite sign.** (This is the live 2026 regime.)

**Regime-conditional reconciliation rule:**
- Carry + PC signals firing in an **orderly** regime = **2 genuine confirmations.**
- Firing together amid a **vol-spike / risk-off** = **suspect 1 root** — don't double-count convergence.

The base-case opposite-sign relationship (higher-for-longer = carry MORE on, but PC compresses) is itself strong evidence they are not the same underlying trade.

---

## LIVE PLACEMENT LOG (most-recent first)

### 2026-07-02 — CANDIDATE STRIKE ADJUDICATED: **NO STRIKE** (first live use of the playbook); AMBUSH regime logged (S1-A)

PROME flagged a candidate 7/2 strike (USDJPY 162.5 → 161.3 Tokyo → 160.7 on the 8:30 NFP bar; "speed-not-level signature from inside the 162-163 zone"). SAM decomposition:
- **Leg 1 — 15:45 JST Tokyo spike:** 162.2 → 161.10 in ~15 min, **yen-specific** (simultaneous −0.5-0.7% vs USD *and* EUR *and* GBP), CME 6J **30.3K contracts = 11× day-average volume** (2nd-biggest bar of the day), then **~60% retraced within 30 min.** Attribution: **repricing on the Reuters ambush-tactics exclusive** (published 11:36 PM ET Jul-1 = midday Tokyo Jul-2). Against a real op: ~1.1y magnitude is **~¼ strike scale** (Apr-30 ~5y, May-6 ~3y), instant retrace (real ops press and hold), no follow-through.
- **Leg 2 — 8:30 ET NFP bar:** 161.5 → 160.62, **USD-specific** — EURJPY/GBPJPY closed **UP** on the same bar → the dollar fell vs everything = data reaction; **rules out a Jul-11-2024-style piggyback** (a piggyback op hits the crosses too).
- **Verified negatives:** no op reported, no rate checks (⚠️ the circulating Mimura rate-check quote is **Feb-12-2026 vintage** — do not re-date it). Jawboning standing-tier only (Katayama "respond appropriately at any time" 7/1; Kihara; Mimura "prior op effective, some US officials supportive").
- **Disposition:** NO STRIKE (news-attribution + cross-pair + futures-volume + magnitude/retrace all concur). Hard confirm on the docket: **MOF monthly ~7/31**; the ambush regime (S1-A above) is the durable takeaway. MOF #3 anchor **held ~15-20%/30d** — ambush-intent story raises strike-tail intent, spot backing off 162.6 → 161.0 lowers proximity; offsetting.

### 2026-06-25 — S1 ladder: **T2-verbal but PRE-T1 operationally**
Scan since ~6/19 (WebSearch):
- **Jawboning elevated:** yen slid past 161, near a 40-yr low ("reviving intervention bets," CNBC 6/19). FinMin **Katayama (G7): Japan "prepared to take decisive action on speculative moves"** — T3 *vocabulary*, but the **standing recurring line → tape-not-signal**, not a fresh disorder-triggered escalation.
- **T1 RATE CHECKS = ABSENT** (the cleanest pre-strike tell). Experts call prior intervention "largely ineffective" vs structural US-yield drivers.
- Tape = **slow grind** (161.65, +0.03% on 6/25) → speed/disorder trigger NOT met.
- **Net: elevated jawboning, intervention NOT imminent. Step-change to watch = a *rate-check* headline.**

**BOJ SoO 6/24 (hawkish-of-priced, mild tail support):** broad hike support; oil-passthrough spreading beyond petroleum; **~90% see another hike by Dec, >⅓ October**; one member cited neutral-rate ~2% urging faster (~every few months); taper-reduction halt confirmed from Apr-2027 (one fiscal-financing-optics dissent). JGB 10Y ~2.67%. Himino: keep hiking, watch >2% underlying. → mildly supports *holding* the FXY convexity stub (hawkish-of-priced BOJ is one tail route).

### CFTC COT — read framework (set 2026-06-25)
- **Date discipline:** the **Jun-16-data COT printed Mon 6/22** (Juneteenth-delayed) → **−150,132 / 83.4% of the −180K cycle peak** (the v1.6 EV-gate). **Fri 6/26 release = data as of Tue 6/23** — first *post-BOJ-hike + post-FOMC* read; do not re-label it Jun-16. COT is Tue-data, ~3-day lagged (misses Wed-Fri).
- **Read vs the −150,132 baseline:**
  - **Build past −153K (>85% of peak):** amplifier escalates +5pp → +8-10pp; carry-convexity tail **STRENGTHENS** (shorts re-engaging into weakness = near-term bearish-yen confirm, tail-bullish).
  - **Within-band −145K to −152K:** benign continuation, no re-mark; amplifier stays +5pp ON.
  - **Cover toward <−140K and falling:** unwind fuel **de-loads** → tail **WEAKENS**.
  - **Cover <−108K:** pre-registered **retire-to-LOW** gate.
- **On print: verify vs CFTC primary (deafut.txt), not an aggregator headline** (provenance-asymmetry discipline).

**FXY:** recommendation unchanged — still pending Will's broker truth (trim fill Y/N, fill price, stop implementation); slow grind = stop not under acute threat today.

*Sources: CNBC 6/19 (yen past 161); CNBC 5/7 + Japan Times 5/9 (Katayama/intervention); investingLive 6/23-24 + Bloomberg 6/24 + FXStreet (BOJ SoO).*

---

*Method doc — not a live mark. Live intervention probability (SAM-23) and USD/JPY levels are in STATUS.md.*
