# FLEET_SCAN — 2026-05-18 (v2)

**Scanner:** fleet-scanner v2 (subagent of Prome)
**Coverage:** 25 agents with STATUS.md — ATHENA, BOND, BRENT, BROCK, CARL, CRUISE, FERT, HANS, HAWK, HENRY, LABOR, LIQUID, MARCO, NEXUS, ORACLE, OTTO, OZK, RED, REGINALD, SAM, SENTRY, SHADE, VIOLET, WALTER, ZHAO
**Dormant scaffolds (no STATUS, last commit >30d):** BARON (Feb 12), BUFFER (Mar 5), CREED (Feb 24), DOC (Mar 23), EARNINGS (Mar 5), FOREX (Mar 5), HERMES (Mar 26), REITS (Mar 5), RESEARCHER (Mar 2), TRADES (Feb 17) — excluded from health table.
**Read budget:** first 30 lines per STATUS; last 5 commits per agent dir; inbox file counts; HEARTBEAT (full); POSITIONS head; SCRATCH. **Heavy reads delegated; this file is Prome's working surface.**

**Live price as-of caveat:** all numeric tape below is from `FORGE/tools/market-data/dashboard.py --compact` re-run **2026-05-17 10:38 ET** per PROME/SCRATCH.md + HEARTBEAT, unchanged from May 16 evening. **Sunday/weekend news has shifted the underlying** (BRENT 5/18 update: Iran drone strike on UAE Barakah May 17 + sanctions-waiver report drove Brent $111→$102 intraday). **Recommend Prome run dashboard for live Monday tape before any decision.**

## 1. Health Table (active agents only)

> *STATUS header age = days since the date at top of STATUS.md. Self-commit age = days since most recent commit that's about that agent's own work (route-only commits like "PROME: route May 16 news sweep" and "HERMES PM Delivery" excluded). For persistent agents (CARL/REGINALD/RED/SAM/BRENT/OZK on CC), self-commit age is the truer staleness signal — header may lag.*

| Agent | STATUS header age (d) | Self-commit age (d) | Inbox unproc | Position relevance | Catalyst proximity (d) |
|---|---:|---:|---:|---|---:|
| **BRENT** | 12 | **0** | 2 | 🔴 high (oil → CRE/banks/transports) | 0 (Barakah strike, NSC mtg 5/19) |
| **REGINALD** | 1 | **1** | 7 | 🔴 high (KRE/WAL/SSB/ZION puts) | 0-7 (WAL 10-Q integrate, MI3 check) |
| **WALTER** | 1 | **1** | 1 | 🟡 indirect (routing infra) | 0 (Iran-anchor reverify, TIC) |
| **BOND** | 5 | **2** | 2 | 🟡 indirect (HYG/TLT puts tiny) | 7-14 (refunding watch) |
| **VIOLET** | 5 | **4** | 1 | 🟠 med (vol-credit transmission) | 7 (cycle-1 calibration trigger) |
| **RED** | 5 | **5** | 6 | 🔴 high (adversarial overlay) | 7-14 (MI3 4-bin decision tree) |
| **SAM** | 6 | **5** | 7 | 🟠 med (FXY small / USD/JPY thesis) | 0 (TIC March), 0-2 (Bessent fallout) |
| **SENTRY** | 9 | 9 | 0 | 🟡 indirect (pipeline infra) | none acute |
| **CARL** | 13 | 13 | 5 | 🟠 med (consumer/BDC indirect) | 7+ (Sweet auto-relief Jun 15) |
| **LABOR** | 14 | 14 | 9 | 🟠 med (NFP transmission) | NFP next print |
| **BROCK** | 17 | 17 | 6 | 🔴 high (APO/ARES/OWL/BIZD) | 0-7 (GCRED/OTF/BCRED 10-Qs TBD) |
| **HANS** | 18 | 18 | 2 | 🟡 indirect (EU/China context) | none acute |
| **MARCO** | 25 | 18 | 0 | 🟡 indirect (FL/border/tourism) | DHS/TSA monitoring |
| **OZK** | 24 | 24 | 1 | 🔴 high (own put line; rolled — STATUS stale) | IQHQ Aug, see Section 5 hygiene |
| **HAWK** | 28 | 28 | 3 | 🟠 med (kinetic → Brent) | 0 (Iran-war anchor reverify) |
| **HENRY** | 31 | 31 | 15 | 🟠 med (market-structure/macro) | NVDA 5/20 |
| **LIQUID** | 32 | 32 | 19 | 🔴 high (HY OAS thesis-kill watch) | daily (HY OAS vs 260) |
| **OTTO** | 33 | 33 | 2 | 🟡 indirect (Tricolor/auto-ABS) | 7-14 (Tricolor Apr 30 follow-on) |
| **NEXUS** | 44 | 44 | 1 | 🟠 med (synthesis) | none until scenario shift |
| **ZHAO** | 46 | 46 | 8 | 🟡 indirect (China/HK macro) | TIC Apr captured, next mid-Jun |
| **ORACLE** | 47 | 46 | 0 | 🟢 low (prediction markets) | none |
| **SHADE** | 53 | 53 | 8 | 🟠 med (PE-insurer/AG-55) | Q1 statutory filings landing |
| **CRUISE** | 59 | 59 | 1 | 🟡 indirect (CCL/RCL/NCLH) | bunker-fuel / Brent linkage |
| **FERT** | 59 | 59 | 1 | 🟡 indirect (CF/fertilizer chain) | $800 urea trigger watch |
| **ATHENA** | 65 | 65 | — | 🟢 none (reading agent) | n/a |

## 2. Stale Agents — Decision Needed

> *Stale = self-commit age > 7d. Ordered by Position relevance × Catalyst proximity. One-line "why now" only.*

| Agent | Self-commit age (d) | Why it matters now | Recommendation |
|---|---:|---|---|
| **LIQUID** | 32 | HY OAS **276bps (as-of 2026-05-17 dashboard)** is 16bps from 260 thesis-kill — the level whose breach reframes the whole short book. Daily watch since Apr 16 has been unmanaged. | **Revive Monday.** Live dashboard pull + write HY OAS / CCC / SOFR-IORB read. |
| **HENRY** | 31 | Apr 17 STATUS showed VIX 17.76 / Brent $90.67 — both stale by ~$18 on Brent and worth a vol-regime re-read alongside VIOLET's 5/13 slope-flip. NVDA 5/20 is HENRY territory. | **Revive in next 1-2 sessions.** Lower urgency than LIQUID (VIOLET covers vol). |
| **BROCK** | 17 | APO closed **$135.38 (as-of 2026-05-17 dashboard)**, sustained above $130 watch for ~17 days; OBDC + FSK Q1 reads already integrated by HEARTBEAT/PROME but BROCK's own STATUS is pre-FSK-print. | **Revive this week.** Especially before any APO put hold/roll decision. |
| **HAWK** | 28 | Iran-war anchor reverify boundary **today (T-1d 2026-05-18)** per WALTER. Sun Barakah strike + NSC mtg 5/19 are HAWK-domain. | **Revive Monday alongside BRENT pull.** HAWK is the kinetic narrative anchor. |
| **OZK** | 24 | Position state in STATUS shows May 15 $42.5P × 2 + $47.5P × 2 as open — Will confirmed rolled (see Section 5 hygiene). STATUS doesn't reflect post-roll posture. | **Hygiene refresh only**, not domain re-research. |
| **NEXUS** | 44 | Convergence Score 50/50 ceiling Apr 4. Scenario weights have moved since (RED bear 52%, stagflation tape printing). Worth a re-run when an actionable scenario re-rank could shift decision. | **Defer until next decision-grade convergence change** (e.g., HY OAS through 260 or 320, or BDC Stage 3 confirm). |
| **SHADE** | 53 | AG 55 Q1 statutory filings landing, NAIC Spring PBR guardrails. Domain remains active. | **Spawn refresh** if APO/PE-captive thread re-opens; otherwise defer. |
| **ZHAO** | 46 | TIC Apr 15 print captured Apr 2; next Belgium/China print mid-Jun. Quarter-end HIBOR seasonal resolved. | **Defer** until TIC May or LGFV signal. |
| **ORACLE / SENTRY** | 47 / 9 | Prediction-market signals quiet; SENTRY pipeline live. | Defer. |
| **CARL / LABOR / MARCO / HANS / OTTO / CRUISE / FERT / ATHENA** | 13-65 | None at the front of the queue this week per HEARTBEAT priority. | Defer unless catalyst fires. |

## 3. Upcoming Catalysts (next 14 days)

| Date | Catalyst | Owning agent | Readiness |
|---|---|---|---|
| **Mon 5/18** | Iran-war anchor re-verify (T-1d) | WALTER → HAWK | ⚠️ partial — WALTER has callback queued; HAWK STATUS 28d stale |
| **Mon 5/18** | TIC March release (Japan UST flows) | SAM | ✅ ready — SAM 5d fresh, Bessent context integrated |
| **Mon 5/19** | NSC meeting on potential Iran military action | BRENT / HAWK | ✅ BRENT data pulled 5/18; HAWK partial |
| **Tue 5/20** | NVDA Q1 earnings | HENRY (read-through) | ❌ HENRY 31d stale |
| **Tue 5/20 – Mon 5/27** | CARL / BRENT / RED / REGINALD calibration cycle 1 trigger window | WALTER coordination | ⚠️ partial — clock ticking; threshold N=15 forward dispositions OR 14d calendar |
| **This week** | WAL 10-Q integration (filed 5/11; not yet integrated) | REGINALD | ⚠️ partial — flagged but not done |
| **This week** | MI3 / FFIEC PDD bulk update status check (window 5/14-16 passed) | REGINALD | ⚠️ partial — flagged but not run |
| **TBD this week** | SSB $95P expiry outcome confirmation | REGINALD + Will | ⚠️ ladder shipped; Will-confirm pending |
| **Daily** | HY OAS vs 260 thesis-kill (currently 276, 16bps gap) | LIQUID / BROCK | ❌ LIQUID 32d stale |
| **Daily** | APO sustained reclaim of $130 (currently $135.38, well above) | BROCK / REGINALD | ⚠️ HEARTBEAT tracks; BROCK 17d stale |
| **TBD** | GCRED / OTF / BCRED / CTAC 10-Qs (Stage 3 forced-mark test) | BROCK | ❌ not started |

## 4. Cross-Agent Contradictions / Red Flags

**Tape-vs-substance bifurcation (4th consecutive observation per RED Session 12):**
- **Substance is hot:** Apr CPI 3.8% YoY / Core 2.8% / Energy +17.9% YoY; Apr PPI 6.0% YoY (largest MoM since Dec 2022); NY Fed Q1 HHDC student-loan defaults 1M→2.6M vertical step-up; FSK Q1 NAV -9.9% QoQ; WAL 4+ consecutive sub-$78 closes; Brent **$109.26 (as-of 2026-05-17 dashboard)** above $100 red threshold; BIZD **$12.61** below $12.50 red; USD/JPY **158.73** above 158 red.
- **Tape is calm:** HY OAS **276bps (as-of 2026-05-17)** below 300 green; VIX **18.43** below 20 green; SPY at ATH per RED 5/13 ($742).
- **Convergence reading:** RED has bear at 52% (Full Stagflation 38% + Acute Dislocation 9% + War Escalation 5%) vs managed/rescue 47%. Bull steelman strengthening alongside bear-confirming substance prints. **No red flag from contradiction itself — but the resolution vector is the dominant decision input.**

**BRENT vs HEARTBEAT energy tape (as-of dates differ):**
- HEARTBEAT cites Brent **$109.26 (5/17 dashboard re-run)**. BRENT 5/18 Monday pull notes sanctions-waiver report drove Brent **$111→$102 intraday** Friday. If BRENT's intraday $102 is the Sunday-close print, HEARTBEAT's $109.26 is itself stale by ~$7. **Recommend Prome run dashboard before quoting energy tape Monday.**

**No within-budget contradiction observed in:** BDC stress reads (FSK/OBDC/BROCK aligned), regional-bank thesis (REGINALD/RED aligned post CHG-RED-025 converge), Japan thesis (SAM intervention confirmation aligned with BRENT-driven USD/JPY).

## 5. Hygiene Items (low-priority but worth Prome noting)

- **OZK STATUS-data desync:** STATUS dated 2026-04-24 still shows May 15 $42.5P × 2 + $47.5P × 2 marked "ROLL PENDING (hard deadline ~May 8)". **Will confirmed roll executed (~Sept).** OZK STATUS needs a refresh to reflect post-roll posture. **Hygiene, not execution risk.**
- **BOND STATUS dated 2026-05-13 by PROME** but self-commit on 5/16 (refresh market-structure monitors). Small STATUS-data desync — BOND has fresher data than header suggests.
- **MARCO STATUS dated 2026-04-23** but self-commit 2026-04-30 (HANS/MARCO logs). 7-day desync.
- **HENRY inbox 15 unprocessed**, **LIQUID inbox 19 unprocessed**, **SHADE inbox 8** — most likely WALTER/PROME signal-route accumulation during the stale window. Worth a sweep when each agent revives.
- **LIQUID STATUS line 7 flags "Apr 15 SOFR breached IORB +7bps"** — this was 33 days ago and the brief did not allow reading past line 30; **recommend Prome confirm whether the breach was mechanical (tax-day TGA build) or structural** when LIQUID revives. Not done within read budget.
- **VIOLET STATUS line 17-25 flags "20d-SKEW-slope sign-flipped negative for first time in 19-yr regime"** — analog R11 went VIX 17.76 → 52.33 in 8 trading days. **Recommend Prome deep-read VIOLET KB-VIO-044/058** if vol thesis becomes Section 6 candidate.

## 6. Top 5 Moves (ranked by HUNTING rubric, with score)

> *Scoring: Pos Prox ×2 / Press ×1.5 / Blind ×1 / Conv ×1 / Decay ×1 / Fresh ×1. Max 22.5. 🔴 ≥14 / 🔵 7-13 / 🟢 <7. Anti-pattern checks (busywork, loudness, completionism, recency) applied; "refresh stale agent" only included where domain is actively load-bearing on positions.*

1. 🔴 **Live Monday dashboard pull + tape read before any decision** — score **18.5** (Prox 3·2=6, Press 3·1.5=4.5, Blind 2, Conv 2, Decay 3, Fresh 1)
   *Prome (CC) — All cited tape is 24+ hours old; BRENT 5/18 update reports Brent $111→$102 intraday Friday on sanctions-waiver news, which if confirmed contradicts HEARTBEAT's $109.26. HY OAS, VIX, KRE, WAL, USD/JPY, BIZD all gate active decisions. — ~10 min.*

2. 🔴 **LIQUID revival: HY OAS / CCC / SOFR-IORB refresh + thesis-kill proximity read** — score **16** (Prox 2·2=4, Press 2·1.5=3, Blind 3, Conv 3, Decay 2, Fresh 1)
   *LIQUID — Agent owns the 260bps thesis-kill watch; STATUS 32d stale; HY OAS 276 is 16bps from kill per HEARTBEAT (verified: 276 − 260 = 16); refresh validates whether the short-book remains in regime. — ~20-30 min spawn.*

3. 🔴 **WAL Q1 10-Q integration (filed 5/11; Schedule O / Table 16 cross-credit inventory)** — score **15** (Prox 3·2=6, Press 2·1.5=3, Blind 2, Conv 2, Decay 1, Fresh 1)
   *REGINALD — Largest bank-short driver. REGINALD STATUS flags 10-Q filed but not yet integrated; Bucket A/C re-score could escalate WAL verdict to V2.2. Direct sizing/exit input on WAL Jun/Sep puts. — ~45-60 min.*

4. 🔴 **TIC March release read + SAM Tranche 2 (FXY $58 band) decision** — score **14.5** (Prox 2·2=4, Press 3·1.5=4.5, Blind 1, Conv 2, Decay 2, Fresh 1)
   *SAM + Will — TIC releases today; SAM 5/12 STATUS flags Tranche 2 add-window technically forfeited (FXY breached $58.00-58.25 upward during intervention dip, back at $58.26). Decision is "Will to direct" per SAM STATUS line 15. — ~30 min SAM, plus Will sign-off.*

5. 🔴 **MI3 / FFIEC PDD bulk-update status check (window 5/14-16 passed)** — score **14** (Prox 3·2=6, Press 2·1.5=3, Blind 2, Conv 1, Decay 1, Fresh 1)
   *REGINALD — Past-due reveal window has closed; status check pending. Direct input to WAL/OZK/SSB/ZION put theses (Hidden CRE / Office-migration). Pairs with #3. — ~30 min combined with #3.*

**Bench (scored but not top-5):**
- 🔵 BROCK revival + APO sustained-$130 reassessment — score 12 (Prox 2·2=4, Press 2·1.5=3, Blind 1, Conv 2, Decay 2, Fresh 0)
- 🔵 BRENT Path B Trigger #3 log entry + Phase 2 watch design — score 12
- 🔵 HENRY revival (NVDA 5/20 read-through) — score 10.5
- 🟢 OZK STATUS hygiene refresh — score 6 (busywork-bias; demoted per Section 5)
- 🟢 SHADE / NEXUS / ZHAO revivals — score <7 (completionism risk)

## 7. Open Loops & Pending Decisions (merged: proposals awaiting Will + in-flight tracking)

| Item | Agent | Status | Next action | Days waiting |
|---|---|---|---|---:|
| APO puts (Jun $100P, Dec $95P) — hold/roll/cut | BROCK / Will | Awaiting Will; OBDC says hold/roll, no add; APO **$135.38 (as-of 2026-05-17)** sustained above $130 watch | Will decision; reassess if APO 3 sessions >$130 confirmed OR HY OAS <260 sustained | ~10+ |
| FSK fresh-premium discussion (BDC/PC downside re-open) | BROCK / Will | Q1 classified Strong Bear / near Max Bear; framework allows fresh discussion | Will decision; needs live bid/ask + approval before any trade | ~7 |
| ARES $95P Jun — hold through BDC wave? | BROCK / Will | Theta risk rising into Jun; small position ($55 value) | Will decision; hold only if FSK/GCRED/OTF mark pressure confirms | ~7 |
| SSB $95P May 15 expiry outcome confirmation | REGINALD / Will | Ladder shipped (Phase 1-5 execution doc); SSB **$91.21 (5/15 intraday per REGINALD)** ITM ~$3.79 intrinsic | Will to confirm execution outcome | 3 |
| KRE / WAL / OZK / ZION / SSB bank-short book Monday prompt | REGINALD / Will | Triage card complete; WAL 10-Q + MI3 checks pending | Run #3 + #5 above, then Prome drafts Monday prompt | 7+ |
| SAM Tranche 2 (FXY $58.00-58.25) — decision pending | SAM / Will | $58 band technically forfeited per no-chase rule; FXY $58.26 currently | Will direction — re-enter / wait / skip | 5 |
| BRENT JOINT_PROPOSAL Will-surface (post-WALTER stitch) | BRENT / WALTER / Will | BRENT §1/§3 + WALTER §2/§4 shipped to repo; Will stitch pending | Will review of stitched proposal | ~13 |
| Calibration cycle 1 review (5/20-27 window OR N=15 forward dispositions) | WALTER + CARL + BRENT + RED + REGINALD | Clock ticking, paired across 5 LIAISONs | WALTER triggers when threshold hit | 0-9 |
| WALTER cron filing-watch leg (dry-run since 5/7) | WALTER | News-sweep leg restored 5/16 via PROME; filing-watch still dry | WALTER owns; not on Prome's plate | 11 |
| CARL CRL-22/23 thesis additions (K-shape Selection / Tariff Transmission) | CARL | Logged in v2.5.1 May 3; downstream impact tracking | Surface only if NFP / consumer print confirms | ~15 |
| HAWK 5/18 Iran-war anchor re-verify (T-1d boundary) | WALTER + HAWK | Boundary hit today | Spawn HAWK refresh tied to Move #1 | 0 |
