# Agent Profile — ORACLE

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** day clock 64d > 45d (content legs not fired). Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-15**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md, TRADE.md, NEXUS_BRIEF.md, SCRATCH.md, MEMORY.md, MAINTENANCE.md, SIGNAL_INTAKE.md, PREDICTION_MARKET_METRICS.md, workbook/{SCHEMA,KB,VX,KALSHI_ODDS_LOG,ODDS_LOG(head)}.tsv, watchlist.tsv + kalshi_watchlist.tsv (heads), HISTORY.tsv (row-count only). **Staleness:** refresh when the calibration-loop status changes (Brier scoreboard added), the role rubric (`PREDICTION_MARKET_METRICS.md`) materially changes, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Prediction-market monitoring — real-money crowd-implied odds on thesis/macro/geopolitical events, from **two** sources: **Polymarket** (Gamma/CLOB API, public) + **Kalshi** (CFTC exchange, RSA-PSS signed, read-only). **Class:** Utility (grade vs `BLUEPRINTS/utility-agent.md`, NOT market). **Role:** sentiment gauge / contrarian signal — tracks *where real money agrees with or diverges from* the fleet thesis; the gap between crowd and reality is the edge. **Transmission:** sends to LIQUID/HENRY (Fed), HAWK/BRENT (Iran/oil), RED (divergence), REGINALD/CARL (bank cluster), VIOLET (complacency), PROME (triage), TERRY (tradeability handoff only); consumes WALTER-routed signals + RED/HENRY/HAWK/BROCK thesis inputs. Cedes substance to domain owners (spreads→LIQUID, fundamentals→REGINALD, oil→BRENT) — **owns only the prediction-market read.** **Spawnable by:** PROME / Will. **What it's for:** "What is the crowd pricing, where does it disagree with us, and what moved?"

## 2. File anatomy (where the richness lives) — HEAVY, two layers (docs + workbook)
| File | Holds | Richness? |
|---|---|---|
| CLAUDE.md (269 ln) | symmetric BOOT/EXECUTE/CLOSEOUT protocol (14-step write-back), domain scope, core-markets tiers, CROSS-AGENT SIGNALS route-matrix, KEY THRESHOLDS, 5-type SIGNAL TAXONOMY, DATA COLLECTION METHOD (both fetchers), **plus vestigial CONVERGENCE MATRIX + EXIT RULES sections** | governing doc; very rich |
| PREDICTION_MARKET_METRICS.md (272 ln) | **the role rubric** — entropy, KL-bits dislocation score, tradeable-gap discount stack, entropy-collapse anomaly alert (k-σ), signal-fusion, routing table, TERRY handoff packet, Python reference, anti-patterns | exemplary (the L3 rubric) |
| STATUS.md (122 ln) | live dashboard — Alerts-first, 34-market signal table (live ts), Trajectory table (Δ30/90d), 5-row Convergence Matrix, Maintenance flags, BOTTOM LINE | live state |
| NEXUS_BRIEF.md (56 ln) | cross-agent surface (NEXUS/peers read in place of raw STATUS) — VIEW/CALIBRATION/CROSS-DOMAIN send+wait tables/tensions/forward catalysts; mandatory every closeout, no marks/P&L | sync surface |
| SCRATCH.md (40 ln) | canonical session handoff — CHANGES SINCE / WHAT I DID (commit hashes) / NEXT SESSION (priority) / CARRY-FORWARD (push state) / OPEN HYPOTHESES | handoff |
| workbook/KB.tsv (19 entries, 13-col) | knowledge base — derived claims/divergences, Admiralty digraph conf + EMPIRICAL/ESTIMATE epistemic + ACTIVE/SUPERSEDED/CORRECTED lifecycle w/ DerivedFrom provenance chains | permanent record |
| workbook/ODDS_LOG.tsv (174 rows, 37 slugs) | Polymarket machine time series (one row/market/pull) | permanent record |
| workbook/HISTORY.tsv (4,796 rows, 33 mkts) | full **daily** CLOB trajectory backfill — the durable view that survives stale point-in-time baselines | permanent record (large; row-count only) |
| workbook/KALSHI_ODDS_LOG.tsv (8 rows, 1 pull) | Kalshi native schema (OI + cents); separate shape, do NOT merge into ODDS_LOG | permanent record (new 6/27, sparse) |
| workbook/VX.tsv (8 rows) | tracked thresholds + state changes (Watch/Alert/Critical + Next_Trigger) | threshold ledger |
| workbook/SCHEMA.tsv (13-col) | KB schema (network standard) | schema |
| TRADE.md (28 ln) | "crowd-odds → position implications" routing surface — explicitly NO sizing/execution | thin handoff (**stale 6/19** — see §4) |
| SIGNAL_INTAKE.md (63 ln) | WALTER subscription spec (priority tiers, keyword patterns, what-not-to-send, active thresholds) | routing spec |
| MAINTENANCE.md (60 ln) | structural-change log (revival, Kalshi wiring, movers cmd, push-policy) + watchlist-upkeep routine | structural memory |
| MEMORY.md (28 ln) | durable ORACLE-specific learning (revival audit) | learning |
| scripts/{polymarket,kalshi}.py | the two fetchers (search/market/event/pull/history/movers; status/series/pull) | tooling |
| watchlist.tsv (~40 mkts) / kalshi_watchlist.tsv (8) | pinned markets pulled every session | config |
| domain/sources/, outbox/delivered/ (3 archived 6/18 files) | history | SKIP |

## 3. Per-dimension local representation (utility-class floor + vestigial market shapes)
| Dimension (utility floor) | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| **CONTRACT** (produces/consumed-by/proof) | scattered: CLAUDE.md IDENTITY + CROSS-AGENT SIGNALS + NEXUS_BRIEF | NO formal 3-line CONTRACT block (predates blueprint) — content present but unstandardized | gap (cheap) |
| **Role rubric** | `PREDICTION_MARKET_METRICS.md` | entropy/KL-bits/tradeable-gap-discounts/entropy-collapse/fusion/routing/TERRY packet | exemplary |
| **Structured record (logging)** | workbook/{KB,ODDS_LOG,HISTORY,VX,KALSHI_ODDS_LOG} | 13-col KB w/ lifecycle + 2 machine time-series + daily trajectory + threshold ledger | exemplary |
| **Standing disciplines** | CLAUDE.md SPAWN PROTOCOL + discipline overlay | symmetric BOOT(read)↔CLOSEOUT(write-back) mirror map; no-naked-numbers; thin-liq ≥3-day re-check; anchor-to-surprise; `[STALE]`>carry-forward | exemplary (blueprint's named exemplar for boot↔closeout) |
| **Cross-agent routing** | CLAUDE.md route-matrix + SIGNAL_INTAKE + NEXUS_BRIEF | condition→target→priority; WALTER subscription; mandatory brief writeback; crisis-only outbox | conformant |
| **Calibration loop** (the utility truth-loop) | EXIT RULES (CLAUDE.md) promise "track accuracy over time" | **NO Brier/resolution scoreboard file exists** — the loop is named, not built | MISSING (the L5 gap) |
| **Authority/safety** | TRADE.md + METRICS §0 | read-only boundary stated explicitly ("does NOT size or execute; TERRY sizes") | conformant |
| *Vestigial: convergence "matrix"* | CLAUDE.md + STATUS.md | 5-row table — repurposed to track *which prediction markets are signaling*, NOT thesis-convergence; filled + live (6/27) | EQUIVALENT (see §4) |
| *Vestigial: TRADE.md* | TRADE.md | "live reads → position implications" + standing rule for downstream agents; explicitly no positions/sizing | EQUIVALENT but stale |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** boot↔closeout symmetry is the fleet **sourcing exemplar** (blueprint cites ORACLE for "boot↔closeout + calibration"); `PREDICTION_MARKET_METRICS.md` is a far richer role rubric than the floor requires; **two real-money sources** with cross-platform agreement=confidence / divergence=signal; the `history` daily-trajectory tool caught a real false-reversal (6/27 Fed −14/7d looked like a pivot until the trajectory showed the baseline sat near a ~66% peak → `finding_delta_vs_own_prior_local_extreme`); KB supersede-don't-delete lifecycle with DerivedFrom provenance chains.
- **The key nuance vs the grounding:** ORACLE *does* carry a **Convergence Matrix (CLAUDE.md + STATUS.md) and a TRADE.md** — market constructs the utility-blueprint DARWIN guard says utility agents do NOT get. They are **NOT DARWIN-dead files:** the "convergence matrix" is repurposed to track which prediction markets are firing (live, scored, 6/27), and TRADE.md is a no-sizing crowd-odds→implications routing surface. So they are **EQUIVALENT (filled, useful), vestigial market-template labels on utility content** — not debt, not gaps. *(Grade them as utility surfaces; do NOT grade ORACLE against the market blueprint for "having" them, and do NOT ding it for them being non-market-shaped.)*
- **False-negative the old mechanical scan made (per grounding):** a market-blueprint scan would either over-credit ORACLE for its convergence-matrix/TRADE.md or ding it for a "stale TRADE.md / no predictions ledger." Both wrong — ORACLE is utility; its real truth-loop is the **Brier scoreboard, which is the one genuinely-missing piece.** ORACLE is the agent that **surfaced the utility-blueprint gap** (blueprint built 6/28, day after ORACLE's heavy 6/27 session).
- **Debt (real):** (1) **TRADE.md stale since 6/19** — its "live reads" numbers (enrichment 66.5%, recession 12.5%, no-cuts 81.9%) are 6/19 vintage, superseded by STATUS 6/27 (1.4%, 11%, 79.5%); it is NOT on the closeout write-back loop (CLOSEOUT steps 8–13 omit it) → ledger-drift-behind-STATUS; refresh-or-freeze. (2) **No CONTRACT block** in the blueprint's standardized 3-line form (predates the 6/28 blueprint). (3) **No `POLY`/`KALSHI` SOURCE_TAG in VOCABULARIES.tsv** — KB uses free-text "Polymarket 6/27" (flagged in MEMORY, unresolved).
- **The L5 gap (headline):** no calibration/resolution **Brier scoreboard** despite EXIT RULES promising accuracy-tracking — the utility analogue of a predictions ledger, and the role's own designated calibration loop.

## 5. Load-bearing context / DO NOT TOUCH
- **The DARWIN-guard nuance:** do NOT "fix" the Convergence Matrix or TRADE.md by deleting them as market-construct violations — they are repurposed utility surfaces (live signal-tracking + no-sizing routing). Touch only to rename/clarify or to refresh TRADE.md's stale numbers.
- **Two-fetcher EXECUTE contract:** every session pulls BOTH `polymarket.py pull --log` AND `kalshi.py pull --log`. Kalshi creds live OUTSIDE the repo (`~/.config/kalshi/`, chmod 600) — **never committed**; KALSHI_ODDS_LOG has a *separate schema* (OI + cents) — do NOT merge into ODDS_LOG (8 mis-shaped rows were appended then scrubbed 6/27).
- **Symmetric boot↔closeout:** what's read at boot is written back at closeout — breaking the mirror is what previously left SCRATCH/NEXUS_BRIEF broadcasting retracted claims (the 6/22 remediation). NEXUS_BRIEF refresh is MANDATORY every session even on no-change (staleness self-corrects via the `As of:`/`STATUS commit:` stamps).
- **Discipline overlay (load-bearing analytical conventions):** thin (<$5K liq) markets ⚠️ flagged, never marked on one print (≥3-day re-check); a market price is an *expectation* → anchor predictions to surprise-vs-pricing, not headline outcomes; no naked numbers (platform/market/date/volume on every figure); `closed`-field (not stale `endDate`) is authoritative for resolution (⏮ flag).
- **Fetcher behaviors:** `history --write` regenerates HISTORY.tsv (the trajectory view that defeats stale baselines); `movers` is the standing discovery sweep (domain-filtered, sports/election-excluded, ⚙ near-resolve flag) — residual Trump-keyword noise is acceptable, do not over-filter.
- KB lifecycle: mark SUPERSEDED/CORRECTED with DerivedFrom pointer — **never delete** a superseded row.

## 6. Maturity snapshot
**L4 (conf H)** — UTILITY class, graded vs `utility-agent.md`. **L4 consumption gate satisfied:** NEXUS reads the brief; LIQUID picked up the July-hike figure-check (now in their `processed/`); TERRY handoff packet is a defined surface (designed handoff, qualitative per PAT-028). Floor L0–L2 met (skeleton → live STATUS+BOTTOM LINE → 5 accruing valid-schema logs). L3 met (role rubric `PREDICTION_MARKET_METRICS.md` applied consistently). **Below L5 on:** (a) no Brier calibration scoreboard [the role's truth-loop, named in EXIT RULES but unbuilt], (b) TRADE.md stale-since-6/19 (closeout-hygiene), (c) no formal CONTRACT block, (d) no zero-YEYOU clean bill. Work queue → `upgrades/ORACLE_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated). **No temporal drift:** ORACLE's last commit was 6/27 (`2b74152b`), *before* the 6/28 grading — current state equals the graded state.

## 7. Open questions / comprehension gaps
- Is the TERRY-handoff path ever *actually exercised* (a real ORACLE→TERRY tradeability packet sent), or is it purely a designed format never fired? (affects how firmly the L4 consumption gate holds on the TERRY leg specifically).
- Is TRADE.md meant to be live (refresh on the write-back loop) or should it be FROZEN with a banner? (decides whether the 6/19 staleness is debt or by-design) — resolve before any L5 claim.
- Kalshi log has a single pull (6/27, 8 rows) — is the second-source loop actually accruing each session, or did it stall after wiring? (the calibration value depends on it building).
- Will a Brier scoreboard even be tractable given Polymarket slug-rot (markets resolve and drop)? — i.e. is the missing calibration loop a *gap* or a *structural ceiling* (PAT-028)? Needs a design call before grading it as fix-it debt vs ceiling-NOTE.
