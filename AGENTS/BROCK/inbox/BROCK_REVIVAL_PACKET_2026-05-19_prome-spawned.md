> **PROVENANCE:** Drafted by a Prome-spawned revival proxy on 2026-05-19, not by BROCK itself. BROCK owns integration decisions and STATUS commit on next boot. Treat as input. This is the **third revival-proxy prototype** under PROME/ORCHESTRAL_LAYER_DESIGN.md Step 4 and the **first execution of the v3 brief spec**. Sister revivals (LIQUID, HENRY) shipped 2026-05-18 are cited in §3 rather than re-derived.

# BROCK REVIVAL PACKET — 2026-05-19

**Proxy budget:** STATUS (full), inbox listing + PROME-20260510 + PROME-20260511 + 5/16 sweep all in full + 5/9 batch top 3 (BlackRock-Metcold, Ch11 +42%, direct-lending-yields), last 15 BROCK commits, HEARTBEAT (BROCK grep + trigger lines 75-90), FLEET_SCAN (BROCK rows), WALTER STATUS (NDFI grep + REQ in full), LIQUID + HENRY revival packets (§1 tape diff + §2 verdict + §3 cross-channel) + HENRY framing-precision note (literal-vs-trajectory discipline), live yfinance pull for OWL/FSK/OBDC/BIZD/APO/ARES/BX (cheap, load-bearing per v3 spec).
**Last BROCK self-commit:** 2026-05-01 EOD (18 days stale).
**Last BROCK STATUS update:** 2026-05-01 EOD.
**Inbox load:** 6 unprocessed items (2× PROME FSK packets May 10/11, 1× 5/16 sweep, 3× 5/9 signal batch).
**Live BROCK-domain catalyst (0-7d):** None confirmed — GCRED/OTF/BCRED/CTAC 10-Q dates remain TBD (not yet released per BROCK STATUS line 45 and STATUS line 152). **NVDA Q1 5/20 AMC is a HENRY/cross-channel catalyst, not a BROCK-primary catalyst.**

---

## §1 Tape pass-through — BROCK-domain diff vs 5/1 STATUS

> *Macro/credit tier numbers from Prome's 2026-05-18 dashboard (per brief). BDC-complex prices (OWL, FSK, OBDC) from proxy yfinance pull at session time — v3 spec authorizes this as cheap + load-bearing because BROCK STATUS is pre-FSK-print and the dashboard does not carry OWL/FSK/OBDC. Source tagged inline.*

| Metric | BROCK STATUS (May 1) | Live (5/18) | Δ over 18d | Zone change | Notes / source |
|---|---|---|---|---|---|
| **APO** | $131.20 🔴 (D1 of 3) | **$134.07** 🟢/watch | +$2.87 / +2.2% | **🔴→🟢 (zone change today)** | Prome dashboard; **sustained >$130 ~17 sessions, well past 3-session trigger — see §2** |
| **ARES** | $119.80 🟢/bull | **$123.70** 🟡 | +$3.90 / +3.3% | mild 🟢→🟡 | Prome dashboard; rally extended but cooled; -0.7% vs 5/11 ($124.61) |
| **OWL** | $9.93 🟢/bull | **$9.49** | -$0.44 / -4.4% | bull rally faded | yfinance proxy; **OWL Q1 fee-rally has reversed — first crack in late-April bull narrative** |
| **BIZD** | $13.31 🟡 (mild bull) | **$12.52** 🔴 | -$0.79 / -5.9% | **🟡→🔴 (red)** | Prome dashboard; below STATUS line 58 trigger <$12.50 by 2¢; BDC tape **demonstrably weaker** independent of HY OAS |
| **FSK** | $11.30 (proxy 1mo ago = pre-print) | **$10.72** | -$0.58 / -5.1% | tape confirming post-Q1 mark stress | yfinance proxy; -2.6% post-print; tender at $11 = above-tape support floor |
| **OBDC** | $11.78 (proxy 1mo ago) | **$11.01** | -$0.77 / -6.5% | -6.5% | yfinance proxy; **biggest 1mo drawdown in the BDC pair — Q1 print "MIXED / earnings-quality bear" per PROME packet** |
| **BX** | $127.04 🟢/bull | **$117.04** | -$10.00 / -7.9% | 🟢→🟡 (bull faded) | yfinance proxy; **biggest 1mo drawdown in alt-mgr complex** — the late-April rally clearly cracking at the BX level |
| **HY OAS** | 283bps 🟢 | **280bps** 🟢 | -3bps | none | Prome dashboard; 20bps cushion to 260 kill (cycle low 276 on 5/17); **gentle compression stalled, not broken through** — cite LIQUID §3 |
| **CCC OAS** | not in STATUS | **935bps** 🟡 | — | quality bifurcation re-igniting | Prome dashboard; LIQUID §1 flags as first BIFURCATION signal — CCC widening while HY compressing |
| **10Y Yield** | not in STATUS | **4.59%** 🔴 | +34bps over the gap window (LIQUID) | not BROCK-primary | Prome dashboard; **DURATION-channel break is the LIQUID finding** that reframes BROCK's bank-PC-cascade story — see §3 |
| **TLT** | not in STATUS | **$83.56** 🔴 | confirms 10Y | not BROCK-primary | Prome dashboard |
| **Brent** | not in STATUS | **$109.73** 🔴 | reaccelerating | indirect (energy → CPI → Fed-can't-cut → BDC NAV pressure via discount rate) | Prome dashboard |
| **USD/JPY** | not in STATUS | **158.93** 🔴 | SAM-domain | indirect | Prome dashboard |
| **KRE** | not in STATUS | **$67.92** 🟡 | REGINALD-domain | indirect | Prome dashboard |
| **WAL** | not in STATUS | **$76.59** 🟡 | REGINALD-domain | bank-PC-feedback channel | Prome dashboard; **WAL fired below $75 bear line 5/11 — that's the REGINALD-side falsification, BROCK only cares via the bank-NDFI-PC transmission channel** |
| **VIX** | not in STATUS | **17.82** 🟡 | tape complacency | indirect | Prome dashboard |
| **SOFR-IORB** | not in STATUS | **-0.10** 🟢 | plumbing normalized | indirect | Prome dashboard; LIQUID's Apr-15 breach falsified as mechanical |

### Time series — BDC-complex trajectory (5-7 points each)

> *v3 spec requirement: trajectory matters more than endpoints for credit. Stitched from STATUS 5/1, PROME packets 5/10-5/11, HEARTBEAT 5/13/5/14/5/16/5/17, proxy yfinance pull 5/18.*

**APO trajectory (7 points, 18d):**
| Date | APO | Note |
|---|---|---|
| May 1 close | $131.20 | BROCK STATUS — D1 of 3 above $130 |
| May 8 (HEARTBEAT) | $130.46 | Sustained, narrow |
| May 11 (PROME packet) | $130.46 | FSK-print day |
| May 13 (HEARTBEAT) | ~$133 (extrapolated) | rally continued |
| May 16 (HEARTBEAT) | $135.38 | local high |
| May 17 (HEARTBEAT) | $135.38 | unchanged |
| **May 18 (Prome dashboard)** | **$134.07** | -$1.31 off the high; **sustained >$130 ~13 sessions** |

→ **APO has been continuously above $130 from 5/1 → 5/18 = 13 trading sessions.** STATUS line 113 trigger ("APO reclaims $130 sustained 3+ sessions") **literally fired on or about May 5** and has been entrenched since. **This is load-bearing for §2 verdict.**

**BIZD trajectory (6 points):**
| Date | BIZD | Note |
|---|---|---|
| May 1 | $13.31 | BROCK STATUS — mild bull |
| May 11 | $12.62 | post-FSK-print, PROME packet |
| May 13 | $12.57 | HEARTBEAT |
| May 16 | $12.61 | HEARTBEAT (red zone) |
| May 17 | $12.61 | HEARTBEAT |
| **May 18** | **$12.52** 🔴 | Prome dashboard — below $12.50 trigger line |

→ **BIZD broke -5.9% over 18d, sliding from mild bull to red zone while APO/ARES held bull.** This is the **divergence inside the BDC complex** — alt-managers (APO/ARES) decoupling from underlying BDC vehicles (BIZD/FSK/OBDC). Cross-reference WSJ "Public BDCs Are Pricing In Most Pain Since Covid" 5/16 sweep #3.

**HY OAS trajectory (7 points):**
| Date | HY OAS | Cushion to 260 |
|---|---|---|
| May 1 | 283bps | 23bps |
| May 8 | ~282 | 22bps |
| May 13 | 282 | 22bps |
| May 14 | 282 | 22bps |
| May 16 | 276 | 16bps |
| **May 17** | **276** (cycle low) | **16bps** |
| **May 18** | **280** | **20bps** |

→ **Gentle compression -3bps over 18d. Cycle low 276 on 5/17. Monday +4bps reversed 13 days of compression in one session.** Never breached 260. **The "23bps from kill" framing in BROCK STATUS line 19 has tightened to "16bps cycle-min / 20bps live" — closer but not fired.** Per LIQUID §2: not fired, not even sustained <270. Match the literal threshold (HEARTBEAT line 80 + BROCK STATUS line 109).

**CCC OAS trajectory (3 points):**
| Date | CCC OAS | Note |
|---|---|---|
| May 1 | 922 (HEARTBEAT context) | flat |
| May 11 | 920 (PROME packet) | flat |
| **May 18** | **935** 🟡 | LIQUID §1: first quality-bifurcation signal — CCC widening while HY compressing |

→ **CCC widening +13bps while HY tightened -3bps. Quality bifurcation re-igniting** — LIQUID's KB-LIQ-043 watch (CCC crossing 1000) still 65bps away but moving toward it. **BDC NAV stress at the riskier end of the credit-quality curve is consistent with this.**

---

## §2 Thesis-kill proximity verdict — credit-stress thesis is INTACT with one literal trigger fired, none structurally killed

**BROCK's credit-stress thesis** = Stage 2 confirmed; Stage 3 forced-mark cascade pending; bear if BDC marks/income deteriorate broadly; bull-kill if HY OAS sub-260 sustained OR convergence vectors downgrade.

### Directional semantics (v3 [H] requirement; pairs with HENRY framing-precision note)

| Vector direction | Reading |
|---|---|
| **HY OAS COMPRESSING toward 260** | thesis APPROACHING DEATH (kill condition) |
| **HY OAS WIDENING from 260** | thesis HEALING (away from kill) |
| **APO RISING sustained >$130** | position-specific (APO put) kill condition — **fires the position, not the broader thesis** |
| **BIZD FALLING below $12.50** | BDC-mark-pressure thesis CONFIRMING (toward bear) |
| **FSK/OBDC marks declining** | Stage 2 BDC-deterioration CONFIRMING |
| **Bank NDFI losses surface** | Stage 3 forced-mark cascade FIRING |

### Literal trigger status (NOT trajectory-counting — per HENRY framing-precision discipline)

Two distinct kill rules in BROCK STATUS. Treat them separately.

**A. Position-specific kill (APO puts, STATUS line 113 + HEARTBEAT line 80):**
> `APO reclaims $130 sustained 3+ sessions → reassess puts`

| Literal threshold | Current state | Literal status |
|---|---|---|
| APO >$130 sustained 3+ sessions | $134.07 live, **continuously >$130 ~13 sessions (May 5 onward)** | **FIRED. Entrenched well past the 3-session sustained threshold.** |

**This trigger has literally fired ~5x over.** It is no longer a "watch" — it is a "decision overdue." The May 1 STATUS line 23 logic ("do not pre-close APO puts before OBDC reads") was built around an OBDC May 6 catalyst that has since passed. OBDC was MIXED / earnings-quality bear per PROME-20260510 packet — not the forced-mark cascade that would have re-armed the bear. **BROCK should treat APO-put hold/roll/cut as the central first-session decision.** Per PROME/FLEET_SCAN row "🔵 BROCK revival + APO sustained-$130 reassessment — score 12."

**B. Broad thesis kill (HEARTBEAT line 80 + BROCK STATUS line 109):**
> `HY OAS <260 for 10+ sessions OR HY OAS reverses below 260bps for 10+ sessions`

| Literal threshold | Current state | Literal status |
|---|---|---|
| HY OAS <260 for 10+ sessions | 280 live, cycle low 276 5/17, **never below 260 in cycle** | **Not fired. Compressing toward, then reversed +4bps Monday. Cushion 16-20bps.** |

**This trigger has NOT fired.** Cycle low to threshold: 16bps. **No legitimate "thesis dead" reading available** — credit world is grinding tighter but holding above kill.

### Verdict: 1 position trigger fired + 1 thesis trigger compressing-but-intact

**Literal count: 1 fired (APO position) + 0 of 3 broad-thesis legs structurally killed.** APO trigger fires the APO put, not the BROCK thesis. The HY OAS compression is the central watchable, but it is not "approaching kill" in the literal-trigger sense — it is **stalling at the 276-280 floor**. Per HENRY framing-precision note: do not count "compressing toward" as "firing."

### Trap-clinching vs soft-kill applied to BROCK

Adapt HENRY's framing precision overlay to the BROCK-domain version:
- **Soft kill (BROCK)** = HY OAS sub-260 sustained AND BDC marks recover (NAV gaps narrow, PIK declines, non-accruals reverse, bank NDFI disclosures benign). Stage 2 thesis fully invalidated. Stand down.
- **Trap clinching (BROCK)** = HY OAS approaching but not below 260 AND BDC substance is *worse*, not better. The widening tape-vs-substance gap is what Stage 2 looks like immediately before Stage 3 fires. Thesis VALIDATING, just hasn't transmitted to spreads yet.

**Current state is the second.** Tape (HY OAS, alt-manager equities APO/ARES) is grinding calmer; BDC substance (FSK NAV -9.9%, BIZD red, OBDC -6.5% 1mo, sponsor backstops, KKR-vs-Apollo bifurcation, JPM cut FSK credit facility -14%, 2nd US bank failure Georgia, Fed Barr "PC could trigger larger credit issues" 5/16) is accelerating the wrong way. **The trap framing is the cleanest mental model for the current 18-day gap. Use it in the STATUS rewrite.**

### Asymmetry to pre-mark

- **If HY OAS prints <270 for 2 sessions** OR **<260 intraday once** → pre-write the kill memo (per LIQUID Move #1). The cushion is small enough that a 1-day shock to kill is realistic.
- **If APO closes back below $130** → reassess whether sustained-13-session breach should still trigger position kill given OBDC was already mixed (catalyst already missed).
- **If GCRED / OTF / CTAC 10-Q drops with NAV >5% markdown** → BRK-27 fires, Stage 3 catalyst lands. This is the next forced-mark cascade test BROCK was tracking on 5/1.

---

## §3 Cross-channel cohere/contradict — BDC NAV stress has TWO channels, both firing

> *v3 [H] requirement: cite sister revivals (LIQUID 2026-05-18 + HENRY 2026-05-18 + HENRY framing-precision note 2026-05-18) explicitly rather than re-deriving.*

### Channel 1: Credit quality (BROCK's primary)

This is the channel BROCK STATUS has been tracking — borrower defaults, NAV markdowns, PIK acceleration, gates, non-accruals, BDC mark deterioration. State as of 5/18:

| Signal | State | Cohere/Contradict with credit-stress thesis |
|---|---|---|
| FSK Q1 NAV -9.9% to $18.83 | Strong Bear / near Max Bear | **STRONG COHERE** — Stage 2 BDC mark stress confirmed at the FSK level. Per PROME-20260511 packet. |
| FSK non-accruals 8.1% cost / 4.2% FV (from 5.5% / 3.4%) | Confirms credit migration | **STRONG COHERE** |
| FSK net debt/equity 1.31x (from 1.22x) | Leverage rising into stress | **STRONG COHERE** |
| FSK $499M purchases vs $710M sales/repayments | Defensive shrink | **COHERE** |
| KKR $300M support package (preferred + tender + repo + fee waiver) | Sponsor-supported stabilization | **AMBIGUOUS** — bull on optics, bear on signal density (healthy BDCs do not need this) |
| OBDC Q1 = MIXED / earnings-quality bear (per PROME) | Not forced-mark cascade | **WEAK COHERE** — Stage 2 confirmed, Stage 3 not yet |
| BIZD -5.9% over 18d into red zone | BDC sector weakness | **COHERE** |
| WSJ 5/16 "Public BDCs Pricing In Most Pain Since Covid" | Narrative recognition | **COHERE** — Stage 3 narrative phase intensifying |
| Fed Barr 5/16 "PC could trigger larger credit issues" | Regulator on alert | **COHERE** — convergence vector "Regulatory action" already at 🔴🔴 (5) |
| 2nd US bank failure 2026 (Georgia) per 5/16 sweep | Bank-side stress | **COHERE indirectly** — REGINALD-primary |
| BlackRock-Metcold $27.5M PC default + personal-guarantee enforcement (5/9 signal) | Recovery-quality fragility datapoint | **COHERE** — sub-systemic, but PC-recovery-fragility tell |
| KKR-doubles-down vs Apollo-cashes-out (WALTER NDFI REQ + 5/11 image batch) | Sponsor-strategy bifurcation | **COHERE strongly** — first time same underlying signal produces opposite sponsor responses. New framework item, see §7 #3 |
| Apollo Q1 $61M markdowns at MFIC + Apollo shopping captive listed BDC at $0.85/NAV + 11% redemption Q | Apollo-side stress at parent-level | **STRONG COHERE** — APO-parent stress signal not just MFIC-level |

**Net credit-channel verdict:** BROCK's credit-stress thesis is **STRONGLY COHERING**. FSK Q1 was the single largest confirming data point since the Apr 24 SEC/Treasury/Fed probe; KKR sponsor backstop is bearish-evidence-disguised-as-bullish-optics; sponsor-bifurcation is a new diagnostic; convergence matrix at 38/50 is probably under-stated post-FSK and should be re-scored.

### Channel 2: Duration (LIQUID's domain — feeds back into BDC NAV via discount rate)

> *Cite LIQUID revival packet §3 directly. The "PLUMBING → DURATION migration" is the load-bearing reframe LIQUID flagged.*

BDC NAV is fair-value-marked using discount rates that include a risk-free + spread component. A duration regime break (10Y +34bps to 4.59%, TLT -3.2%) raises the discount rate on BDC portfolio loans **independent of credit-quality changes**. This is a MARK-pressure channel BROCK has not been tracking as a primary lever.

| LIQUID 5/18 finding | Read-across for BROCK |
|---|---|
| Bear thesis migrated PLUMBING → DURATION | BROCK should add a duration-leg to NAV-stress framework. FSK NAV -9.9% has both credit AND duration contributions; the proxy did not decompose, but neither did the FSK 10-Q narrative. |
| 10Y +34bps over 32d to 4.59% | Mechanical mark-down on long-dated portfolio loans. **Estimate: every +100bps on 10Y = ~3-5% mark-down on a 5yr-duration loan portfolio held at original spread.** FSK NAV -9.9% is consistent with credit AND duration both contributing. |
| TLT -3.2% confirms 10Y break | No 60/40 escape; forces holders of risky credit to hold it. |
| SOFR-IORB normalized (-10bps) | Plumbing-leak hypothesis falsified for April. Funding stress is NOT the active channel. |
| HY OAS 280 / cycle low 276 | Stalled at floor, never breached 260. BROCK's central watchable. |
| CCC OAS +13bps to 935 | Quality bifurcation re-igniting. **CCC widening while HY compressing = exactly the "credit cracks at the riskier end first" pattern BROCK's Stage 2 thesis predicts.** |
| Gamma/momentum suppression hypothesis | Explains why HY OAS won't break despite FSK NAV -9.9%, 2nd bank failure, Brent $109. If gamma unwinds, OAS could gap. |

**Net cross-channel verdict:** BROCK's credit-stress thesis **STRONGLY COHERES** with LIQUID's findings. The reframe is **additive, not substitutive** — credit channel is firing AND duration channel is now also firing. BDC mark stress has two contributing channels; FSK Q1 reflects both. **The 18-day gap reframes the active transmission as multi-channel, not single-channel.**

### Does HENRY's "complacency-trap clinching" finding inform BROCK Stage 2 → Stage 3 escalation timing?

> *Cite HENRY revival packet §2 + framing-precision note.*

HENRY's finding (per framing-precision note): **1 fired + 1 compressing + 1 flat** complacency-trap invalidation triad; trap clinching, not soft kill; tape/substance divergence widening. Apply to BROCK:

- **The longer the trap clinches**, the longer BDC marks deteriorate without HY OAS confirming spreadwise. Stage 2 evidence (FSK NAV, BIZD red, OBDC -6.5%) accumulates without Stage 3 catalyst (bank NDFI write-down, HY OAS sub-260, BDC arms-length sub-90¢ transaction). This is **consistent with current state**.
- **When the trap springs (HENRY's term), the path is asymmetric** — HY OAS could gap rather than compress smoothly. This means Stage 2 → Stage 3 transition timing is **non-linear**, not gradual. The trap framing tells BROCK to **pre-stage Stage 3 catalyst recognition triggers now**, before the gap event.
- **Stage 3 catalyst candidates to pre-stage:** (a) first bank PC loss disclosure (WALTER NDFI REQ deepens BROCK's scope here); (b) arms-length sub-90¢ BDC loan transaction; (c) GCRED/OTF/CTAC 10-Q NAV markdown >5%; (d) SEC enforcement filing; (e) HY OAS sub-260 sustained.

**Timing read:** Stage 2 → Stage 3 escalation timing is **on the order of weeks-to-months, dependent on catalyst arrival, not on smooth deterioration.** The 18-day gap shows Stage 2 grinding without firing Stage 3 — the trap is deepening but has not sprung. **BROCK should not predict a timeline; BROCK should pre-stage recognition triggers and let the catalyst calendar drive arrival.**

### One important contradict to flag — APO-parent strength

- **APO equity is sustained >$130 13 sessions = "bull-thru-trigger" zone.** Per BROCK STATUS line 32 the late-April narrative phase had bulls re-emerging via OWL Q1; per OWL -4.4% over 18d that bull narrative has now cracked at the OWL level **but APO at $134 has not yet repriced**. The APO equity divergence from BDC sector weakness (BIZD -5.9%, BX -7.9% from 5/1 high) is a **structural contradiction** to the bear thesis at the equity level — alt-managers fee-economics are decoupling from the vehicles they manage. **This is precisely the OWL fee-vs-DL split BROCK noted on 5/1 (LESSONS #11)**, but now visible at the multi-name level. **BROCK should articulate this contradiction explicitly in STATUS rewrite — it is the cleanest way to make the trap framing concrete.**

---

## §4 Domain catalyst prep / overflow register

> *v3 spec: if 0-7d catalyst exists → prep. If not → overflow.*

**No BROCK-domain catalyst confirmed 0-7d.** GCRED / OTF / BCRED / CTAC 10-Qs remain TBD (per BROCK STATUS line 45 + line 152). NVDA 5/20 is HENRY-primary not BROCK-primary. The next BROCK catalyst is **earliest mid-late May (GCRED) or June (CTAC / BCRED)** — actual dates need verification on revival.

**Overflow register (items § did not have room for; BROCK should triage):**

| Item | Source | Why deferred |
|---|---|---|
| GCRED 10-Q release date | TBD per BROCK STATUS | **Revival action #1**: pull from BlueOwl IR + filing schedule on revival; pre-build doc analogous to `OBDC_PREBUILD_MAY06.md` |
| OTF 10-Q release date | TBD | Same |
| BCRED 10-Q release date | TBD | Same; BCRED is non-traded, harder; verify via BX IR + Form 10 schedule |
| CTAC 10-Q release date | TBD | Carlyle IR |
| FSK fresh-premium discussion | Blocked on BROCK refresh per FLEET_SCAN | **Revival action #2**: produce decision memo with live bid/ask context; framework allows fresh discussion |
| ARES $95P Jun decision | Theta risk rising; small position ($55 value per PROME POSITIONS) | **Revival action #3**: read trade/ folder, decide hold/cut |
| BDC mark convergence monitor (LIQUID workbook handoff) | LIQUID flagged this as "do NOT archive" because Q1 BDC earnings make it live | Cross-feed: BROCK should re-sync with LIQUID on BDC mark monitor format after both revive |
| Sponsor-bifurcation framework section | New from WALTER REQ + 5/11 image-batch | **Revival action #4**: write framework section in STATUS; KKR-doubles-down vs Apollo-cashes-out is a new diagnostic |
| WALTER NDFI scope correction (REQ 5/14) | $128B working figure is 11× understated vs $1.4T full NDFI | **Revival action #5**: STATUS refresh per WALTER REQ; see §6 |
| FFIEC RC-C 10.a-10.e schema (REGINALD CROSS_REFS) | WALTER appended schema 5/14 | Read on revival before May 15 CDR Q1 release (which has now passed — BROCK should pull) |
| May 15 CDR Q1 5-category NDFI bulk release | Passed 5/15 per WALTER REQ; first bank-level 5-cat splits publicly available | **Revival action #6**: pull and integrate — this is the **first NDFI-channel ground truth** for BROCK STAGE 2 thesis magnitude |

---

## §5 Inbox sweep triage — 6 items (LIVE / SUPERSEDED / STALE)

> *Per v3 [H]: read top N then stop and judge. Marked each item.*

| # | File | Date | Verdict | Reason |
|---|---|---|---|---|
| 1 | `PROME-20260510-fsk-live-read-and-pc-10q-watch.md` | 5/10 | **SUPERSEDED — partially STALE** | The FSK live-read ask was answered by Prome (FSK Q1 = Strong Bear per PROME-20260511 + `PROME/FSK_Q1_READ_MAY11.md`). The follow-on 10-Q watch (GCRED/OTF/BCRED/CTAC) is **STILL LIVE** as a domain ask — those filings remain pending. **Recommendation:** mark FSK-leg DONE (Prome answered), pull the GCRED/OTF/BCRED/CTAC watch forward as ongoing BROCK domain commitment. Archive after STATUS update reflects the watch. |
| 2 | `PROME-20260511-fsk-q1-first-pass-read.md` | 5/11 | **LIVE — high priority** | This is the post-release data dump Prome did so BROCK doesn't reconstruct from scratch. FSK Q1 Strong Bear classification + KKR support package details + revolver amendment + tape cross-check. **Action:** integrate as the canonical BROCK FSK Q1 read; produce the domain memo Prome explicitly asked for (PROME-20260510 ask is still open at the memo level — the **memo has not been written**). Then archive. **This is the first session work product.** |
| 3 | `sweep_2026-05-16_2306.md` | 5/16 | **LIVE — high relevance, mostly narrative** | 12+ items, heavy PC-news cluster: WSJ "Beware of Bargains in PC", BBG "Public BDCs Pricing In Most Pain Since Covid", Reuters "PC funds mark investment values lower, filings show", BlackRock federal probe puts PC valuations and growth plans under review, Europe regulators may launch PC inquiry, Apollo PC ETF launch. **Read:** convergent narrative-phase intensification (Stage 3 narrative recognition continuing). The Reuters "filings show marks lower" is the LIVE-VERIFY priority — it implies forced marks in Q1 filings beyond FSK; could be GCRED/OTF preview. **Action:** verify Reuters article on revival; treat sweep as confirming Stage 3 narrative phase per convergence matrix. Integrate top 3-4 lines into STATUS; archive rest. |
| 4 | `signal_2026-05-09_blackrock-metcold-private-credit-default.md` | 5/9 | **LIVE — sub-systemic but useful** | BlackRock APAC PC Fund II default: Metcold $27.5M default on $52.5M facility, personal-guarantee enforcement. Cold-chain logistics CRE-adjacent. China exposure. **Per LIQUID §4: file as PC-recovery-fragility data; cross-reference Stage 3 framework.** Single KB-BRK entry; archive. |
| 5 | `signal_2026-05-09_chapter-11-bankruptcy-filings-up-42.md` | 5/9 | **LIVE — confirms convergent narrative** | Insider Wire X claim: Ch11 filings +42% YoY. Per LIQUID §5 deferred-list: convergent with KB-LIQ-050 consumer-credit narrative. Source verification recommended (Epiq/AACER/ABI). **Action:** verify on revival, integrate as defaults-trending-up convergence vector confirmation (BROCK STATUS line 28 already says "trending up, not yet inflecting" — Ch11 +42% would update to "trending up, possibly inflecting"). |
| 6 | `signal_2026-05-09_credit-yields-direct-lending-income-losses.md` | 5/9 | **LIVE — domain-primary** | Cliffwater Direct Lending Index showing income masks loss realization (income ~9-12%, realized losses -0.5% to -2%). Supports "grind, not cascade" read. **Action:** integrate as a single LESSONS-style entry or KB row on income-vs-loss decomposition; pair with FSK Q1 NII $0.41 vs realized loss $2.00/share which is the same pattern at vehicle level. |

**Net sweep action:** 6 of 6 LIVE (none stale, none superseded entirely). The first session sweep is **read PROME-20260511, write the FSK Q1 memo, then process 5/16 sweep + 5/9 batch in one pass**. ~90 minutes total.

---

## §6 Open questions from BROCK STATUS — closeout authorization

| Question / pending item | STATUS reference | Recommendation |
|---|---|---|
| APO sustained $130 D2/D3 watch | STATUS line 113-114, 163 | **CLOSEOUT — TRIGGER FIRED.** Literal threshold (sustained 3+ sessions) exceeded since ~May 5. APO continuously above $130 for 13 sessions. STATUS should be rewritten to reflect TRIGGER FIRED → decision overdue, not "D1 of 3 watching." |
| OBDC May 6 read | STATUS line 23, 79, 130, 138-149 | **CLOSEOUT — OBDC PRINTED; MIXED / earnings-quality bear per PROME packets.** Not the forced-mark cascade that would re-arm bear; consistent with Stage 2 grinding. STATUS should integrate the result and remove the May 6 "pre-build" framing as historical. |
| FSK May 11 read | STATUS line 80, 152 | **CLOSEOUT — FSK PRINTED; Strong Bear / near Max Bear per PROME-20260511.** Per PROME packet: NAV -9.9%, non-accruals 8.1% cost, KKR $300M support package, JPM cut credit facility -$648M (-14%). BROCK domain memo **not yet written** — that's the first revival action. |
| HY OAS 260 thesis-kill watch | STATUS line 109, 162 | **HOLD — actively watchable.** Cycle low 276 on 5/17, +4bps to 280 on 5/18. Cushion 16-20bps. Pre-write kill memo (per LIQUID Move #1). |
| GCRED / OTF / Carlyle CTAC / BCRED 10-Q dates | STATUS line 45, 152 | **HOLD — domain-primary still open.** Pull release dates on revival; pre-build per OBDC pattern. |
| GBDC fiscal Q2 (= cal Q1) ~May 5-7 | STATUS line 42, 152 | **CLOSEOUT — likely printed.** Verify GBDC release on revival; if printed, score and integrate. (Not in proxy budget to verify.) |
| BX backstop precedent + SEC subpoena outbox to REGINALD | STATUS line 145 | **CLOSEOUT — assumed processed by REGINALD.** Verify by checking REGINALD STATUS on revival; no action unless gap. |
| Bank PC quantification cascade | STATUS line 158 | **SUPERSEDED — WALTER NDFI REQ supersedes.** BROCK $128B figure should be replaced with FFIEC NDFI $1.4T per WALTER REQ. See action below. |
| VX-BRK-010 BDC NAV discount (39d stale per STATUS line 156) | STATUS line 156 | **HOLD — refresh needed.** Pull fresh Raymond James data on revival or accept ~25% current. |
| BRK-09 HRZN merger close verification | STATUS line 159 | **HOLD — low priority.** |
| HEN-22/23/24/25 cross-agent dependencies (per HENRY revival) | HENRY §6 | **CLOSEOUT — HENRY owns scoring.** Confirmed/partial confirmed per HENRY's read. No BROCK action. |
| **WALTER NDFI scope-correction REQ (2026-05-14)** | WALTER outbox / FLEET_SCAN | **HOLD — first-session integration.** Per WALTER REQ: replace BROCK STATUS "$128B top-4 banks PC" with FFIEC RC-C 10.a-10.e framing ($1.4T full NDFI / WFC alone $212B / +35.2% YoY / 5-cat breakdown). Add top-of-cohort single-name watchlist (WFC 21%, MS BCI 19.73% +316bps QoQ, CUBI 33%). Add sponsor-bifurcation framework section (KKR-doubles-down vs Apollo-cashes-out). Pull May 15 CDR Q1 5-category NDFI bulk release if available. This is BROCK's **largest pending structural ask**, 5 days open against 14d retry threshold. |

**Net: 5 closeouts + 6 holds + 1 SUPERSEDED + 1 high-priority structural integration (WALTER NDFI REQ).** First-session mechanical sweep ~25 minutes.

---

## §7 Recommendations to BROCK on next boot (priority order)

> *Effort estimates assume BROCK's working pace; proxy is calibrating from observed multi-session catch-up cadence.*

1. **[60 min] Write the BROCK FSK Q1 domain memo (PROME-20260510 ask).** Use PROME-20260511 packet as input. Format per the ask: Classification (Strong Bear / near Max Bear), Evidence table, Private-Credit Position Implication (APO/ARES/OWL/BIZD/ARCC), Next Forced-Mark Tests (GCRED/OTF/BCRED/CTAC), Decision Inputs for Prome. **This is the single largest open BROCK deliverable.** It also unblocks FSK fresh-premium discussion blocked on BROCK refresh per FLEET_SCAN.

2. **[30 min] APO put hold/roll/cut decision memo.** APO sustained >$130 for 13 sessions — position-kill trigger literally fired since ~May 5. OBDC was MIXED (not forced-mark) so the post-OBDC re-arm did not materialize. **Decision is overdue.** Read `FORGE/timing/` + `trade/TRADE.md` Section 8, write the decision memo, route to Will via Prome. Per FLEET_SCAN: highest-priority position decision pending. **Note:** per `memory/feedback_exit_recommendations_need_mark_context.md` — if recommending close-now, surface execution mark before recommending; if at unfavorable mark, convert to pre-registered window triggers + hard backstop dates rather than close-now.

3. **[45 min] WALTER NDFI scope-correction integration.** Replace BROCK "$128B top-4 banks PC" with FFIEC framing ($1.4T full NDFI / WFC $212B / +35.2% YoY / 5-cat 10.a-10.e split). Add single-name watchlist tier (WFC 21%, MS BCI 19.73% +316bps QoQ, CUBI 33%). Pull May 15 CDR Q1 5-cat NDFI release (passed; first bank-level 5-cat splits publicly available). **This rescales BROCK's STAGE 2 thesis magnitude and is the largest open structural ask.**

4. **[30 min] Sponsor-bifurcation framework section.** New diagnostic from WALTER REQ + 5/11 image-batch. KKR-doubles-down (FSK $300M sponsor backstop + KREST $50M + KREF concurrent stress) vs Apollo-cashes-out (Q1 $61M markdowns at MFIC + Apollo shopping captive listed BDC at $0.85/NAV + 11% redemption Q + lending halted). Add framework section + sponsor-action-comparison diagnostic for thesis-pivot input when multiple sponsor-affiliated BDCs hit stress signals concurrently.

5. **[30 min] STATUS rewrite per literal-trigger discipline (HENRY framing-precision discipline).** Replace "D1 of 3" watch language (stale) with TRIGGER FIRED + decision overdue framing for APO. Add "1 fired + 1 compressing + 0 broad-thesis legs killed" literal-trigger count per §2. Replace HY OAS "23bps from kill" with literal cycle-min 16bps + live 20bps. Add trap-clinching vs soft-kill conceptual distinction.

6. **[30 min] Cross-channel reframe section in STATUS.** Per LIQUID §3: bear thesis migrated PLUMBING → DURATION; BDC NAV stress now has two channels (credit + duration). Add a duration-leg to NAV-stress framework. Note CCC OAS +13bps to 935 = first quality-bifurcation signal, consistent with Stage 2 thesis predicting credit cracks at riskier end first.

7. **[60 min] Inbox sweep — 6 items per §5.** Read PROME-20260511 (already done in writing the FSK memo), 5/16 sweep, 5/9 batch trio. Single batch pass. Archive after STATUS update.

8. **[20 min] Pull live BDC-complex tape on revival** — APO, ARES, OWL, FSK, OBDC, BIZD, BX, ARCC. Refresh into STATUS dashboard table. Per proxy yfinance pull 5/18: APO $134, ARES $124, OWL $9.49, FSK $10.72, OBDC $11.01, BIZD $12.52, BX $117.

9. **[deferred / backlog] Pre-build docs for GCRED / OTF / BCRED / CTAC 10-Q.** Same pattern as OBDC_PREBUILD_MAY06.md. Required for Stage 3 forced-mark-cascade testing. Build after release dates confirmed.

10. **[deferred / backlog] LESSONS / KB entries from this packet.** Sponsor-bifurcation diagnostic; duration-channel NAV stress; CCC quality bifurcation; APO equity decoupling from BDC sector weakness (LESSONS #11 expansion). Don't batch all in revival session — let them surface organically over 2-3 sessions.

**Total first-session work:** ~5 hours (items 1-7). Items 8-10 are 1-2 sessions out. Items 9-10 are backlog.

**Mechanical-before-creative ordering** per root CLAUDE.md rule: APO decision (#2) and FSK memo (#1) BEFORE new research threads. WALTER REQ (#3) is structural and can interleave; sponsor-bifurcation (#4) and STATUS rewrite (#5-6) follow.

---

## §Design feedback — v3 brief spec execution (max 7 bullets per spec)

1. **The 7-section structure transferred cleanly to BDC/private-credit domain.** §1 tape diff with zone-change column captured the BIZD 🟡→🔴 zone change and APO 🔴→🟢 zone change cleanly. §2 directional semantics work well for a multi-trigger domain (APO position vs broad thesis trigger separation was load-bearing). §3 cross-channel was easier here than HENRY because credit-stress-thesis ↔ credit channel is a natural fit, but the duration-channel addition was the v3 win. §4 as overflow register (no 0-7d catalyst) worked — having it as default-overflow when no catalyst is preferable to forcing a thin catalyst-prep section. §5 inbox triage and §6 closeout authorization both gave BROCK clean mechanical first-session work. §7 prioritized recommendations is the natural deliverable.

2. **Citing LIQUID + HENRY revivals saved very substantial budget.** Specifically: PLUMBING → DURATION migration finding from LIQUID gave §3 a 30-minute reframe rather than 90-minute re-derivation. HENRY's "trap clinching vs soft kill" overlay was directly applicable to BROCK's STAGE 2 vs STAGE 3 thinking — I adapted the conceptual distinction in §2 + §3 without rebuilding the framework. Strong endorsement for the v3 [H] requirement.

3. **The HENRY framing-precision overlay (literal vs trajectory discipline) PREVENTED at least one overspecified claim.** Without it, I would have written §2 as "2 of 3 broad-thesis legs firing" by counting HY OAS compression as "approaching firing." The discipline forced me to write "1 position trigger fired + 0 of 3 broad-thesis legs structurally killed" which is the actually-defensible read. The HENRY framing note is now functionally a v3.1 artifact and should be codified as such.

4. **The literal-trigger discipline revealed a previously-hidden BROCK gap: position-specific vs broad-thesis trigger separation.** APO sustained >$130 fires the APO put, not the BROCK thesis — but BROCK STATUS treats them somewhat conflated. The v3 spec's "state directional semantics explicitly" requirement surfaced this. **Suggest v4 brief explicitly ask: "Is this a position-specific trigger or a broad-thesis trigger? They may have different decision implications."**

5. **The cheap-data-pull permission for BDC complex (OWL/FSK/OBDC/BX) was load-bearing.** Without yfinance pull on those four, the §1 trajectory tables would have been pre-FSK-print numbers vs Prome dashboard tier-1 numbers — a tier-mismatch problem similar to what HENRY flagged for SPX/VIX. The OWL -4.4% over 18d finding (bull rally has cracked) and BX -7.9% finding (alt-mgr complex weakening) were both load-bearing for §3's APO-decoupling-from-BDC-sector contradict-flag. **Strongly endorse: keep cheap-pull as explicit permission, not conditional.**

6. **The WALTER NDFI REQ integration in §6 surfaced an opportunity:** revival proxies should look at the target's **outbox** as well as inbox, because outstanding inbound REQs from peer agents have similar "load-bearing structural ask" character to unprocessed inbox items. The brief mentioned WALTER NDFI scope-correction by name (good catch), but more broadly: **suggest v4 brief add "check target's outbox + peer agents' outboxes-for-target for outstanding REQs ≤14d old."**

7. **Two new artifact types worth codifying:**
   - **Sponsor-bifurcation diagnostic** (KKR-doubles-down vs Apollo-cashes-out): when same underlying signal produces opposite sponsor responses, that's a leverage-and-flexibility tell at the parent level, not just the vehicle level. Worth a generalized framework slot in BROCK domain (and possibly in REGINALD for bank-sponsor analogs).
   - **Decoupling-within-complex flag**: APO equity decoupling from BDC sector weakness (alt-managers fee-economics holding while underlying vehicles bleed) is a structural divergence that LESSONS #11 captures partially but deserves its own framework section. Generalizable to other multi-vehicle complexes.

---

*End of revival packet. Proxy session terminates here. BROCK owns all integration on next boot. Both this packet and the accompanying STATUS_DRAFT are `_prome-spawned.md` suffixed and untracked-by-design — do not commit until BROCK integrates and rewrites.*
