# MIDAS — Domain Sweep (4-lens), 2026-07-12

**Scope:** MIDAS's whole corpus as of the first real session (CLAUDE.md, STATUS.md, THESIS.md, workbook/*, SCRATCH.md, LESSONS.md, TRADE.md, NEXUS_BRIEF.md, inbox). Per `PROME/packets/DOMAIN_SWEEP_LENSES.md` — small mechanical fixes done in-session; analytic/canon-adjacent items proposed below.

**Context:** this is MIDAS's *first real session* (7/11 was a DAEDALUS scaffold build). Most of the corpus is one session old, so this sweep doubles as a fresh-eyes audit of the build itself — the biggest find (M1's framing) is exactly the kind of thing a same-day sweep is built to catch.

---

## Prioritized table

| Item | Lens | Age | Evidence | Proposed action | H-M-L |
|---|---|---|---|---|---|
| M1's "gold structurally bid despite rising real yields" claim was asserted with no spot pull, and the first pull contradicts it | UNFINISHED WORK / contradiction | 1 session | STATUS.md 7/11 vs KB-MIDAS-005 (this session) | **DONE this session** — STATUS/THESIS/VX/FLOW all corrected, score M1 3→2 | H |
| MIDAS-01/02 predictions had no spot-price anchor (written before any spot pull existed) | UNFINISHED WORK | 1 session | PREDICTIONS.tsv original rows: "gold spot vs 7/11 level" with no number | **DONE this session** — retroactively anchored to $4,113.70 (gold) / $5.75 (copper, 4/9) | M |
| `metals_watch.py` flagged as owed, not built | UNFINISHED WORK | 1 session | SCRATCH.md 7/11 pickup #1 | **DONE this session** — built, tested, wired into boot.py leg 0 | H |
| LIQUID gold-leg-ownership handoff sat unconsumed in inbox | UNFINISHED WORK | 1 session | `inbox/PROME_ROUTING_2026-07-11.md` | **DONE this session** — processed, ack drafted as route-out (see below) | M |
| LME/COMEX inventory — I1's threshold table needs it, no live source | GAPS | 1 session (structural) | THESIS.md I1 stage 2 always said "needs first pull"; this session tried and failed to find a free API | Registered as an honest gap (KB-010); try westmetall.com scrape next session | M |
| CFTC COT is weekly-cadence but has no automated pull — this session's baseline was a one-off manual `urllib` call | GAPS | new (found this session) | metals_watch.py header explicitly scopes COT OUT | Candidate: a lightweight weekly-cadence COT leg (separate script or extend boot.py cadence-skip pattern) | M |
| CB gold-buying / WGC flow data (Tier-2 M1 structural leg) — never pulled, single-source dependency (WGC) not yet even attempted | GAPS | 1 session (never closed) | KB-MIDAS-004-adjacent note in original build; still absent from workbook | Register as a quarterly-cadence pull, not this session's scope (Tier-2 not Tier-1) | L |
| No pre-registered resolver existed for CPI (7/14) or China Q2 GDP (~7/16) before this session, despite both being ≤3-week catalysts M1/I1 directly test | GAPS | 1 session | PREDICTIONS.tsv had only 9/30 resolutions, nothing catalyst-dated | **DONE this session** — MIDAS-03 (CPI) and MIDAS-04 (China GDP) registered w/ mechanical sign-check criteria | H |
| I2's first read is WebSearch-summarized (PROVISIONAL), including two mutually-inconsistent tariff-rate figures (132.83% vs 828%) from different sources | GAPS / evidence quality | new | KB-MIDAS-008 | Flag PROVISIONAL explicitly (done); primary-source verify next session (Federal Register / Commerce Dept determination, WPIC quarterly) | M |
| ZHAO's STATUS.md independently carries China PMI 50.3 (expansion) + Q1 GDP +5.0% YoY, with ZHAO's own "growth stronger than stress narrative" note — this directly corroborates MIDAS's I1 copper-growth-confirming read via a completely different data source (official stats vs. price/technical) | MISSED CONNECTIONS | new (found this session) | AGENTS/ZHAO/STATUS.md L73-83; KB-MIDAS-011 | Route to ZHAO as a cross-reference to add on their side; use as MIDAS-04's implicit "what does a miss look like" anchor (Q1 was +5.0%) | H |
| WebSearch/WebFetch gave two different WRONG number sets for the same CFTC gold contract on first attempt this session | (process, logged as LESSON not a domain item) | new | LESSONS L-05 | Fixed in-session (raw Socrata API pull); durable lesson banked for future structured-data pulls fleet-wide, not just MIDAS | M |
| The M1 (gold down) / I1 (copper up) co-movement this session is neither of THESIS.md's two named coherent-divergence cases ("reflation" both-up, "risk-off" gold-up/copper-down) | FURTHER THREADS | new | KB-MIDAS-009, STATUS.md independence note | Name it as a third case ("growth without debasement premium") in THESIS.md if it persists past one session — not done yet, watching first | M |
| Gold COT positioning is heavily net-long (52.2% of OI) even as price fell 18.6% over 90d — the long hasn't capitulated | FURTHER THREADS | new | KB-MIDAS-006 | Worth a standing watch: does a COT capitulation (net-long unwind) precede or coincide with LIQUID's EndGame gold-leg firing (<$4k)? No one has looked at COT vs. that discriminator together yet. | M |

---

## TOP 3 most consequential

1. **M1's headline framing was wrong, and the fix changes MIDAS's most-read output.** The 7/11 build session characterized gold as "structurally bid despite rising real yields" — a live debasement-premium divergence — without ever pulling gold's spot price (STATUS.md said so explicitly: "MIDAS owes the gold-spot + divergence quantification"). This session's first pull shows the opposite: gold fell 18.6% over 90 days while real yields rose 36bp, verified across five monthly markers so it isn't a two-point artifact. This is exactly the failure mode LESSONS L-06 names: an honestly-flagged gap can start reading as established fact if the narrative around it (STATUS's "🟠 elevated," the BOTTOM LINE prose) doesn't get re-tested at the first opportunity. Every downstream consumer (BOND, LIQUID, PROME's NEXUS_BRIEF reads) was about to inherit the wrong framing. Fixed this session across STATUS/THESIS/VX/FLOW/KB — but it's the clearest argument for why a same-session domain sweep matters even for a 1-day-old agent.

2. **The COT-verification-method finding is a fleet-relevant process lesson, not just a MIDAS fact.** WebSearch and WebFetch both returned confident-sounding but wrong and mutually-contradictory CFTC positioning figures on the first attempt. A direct `urllib` pull against CFTC's public Socrata API, cross-checked against its own schema field list, gave the correct numbers (verified by internal consistency: the same query re-run twice, plus a sanity check that OI = long+short+spread roughly holds). This generalizes past MIDAS: any agent citing structured government/exchange data (CFTC, FRED, EDGAR, EIA) via a WebFetch/WebSearch summary rather than a raw API pull is at real risk of silently propagating hallucinated numbers that *look* plausible. Logged as LESSONS L-05; worth a DAEDALUS-level look at whether other agents have this exposure.

3. **The ZHAO/MIDAS independent-convergence finding (China growth) is a genuinely new, unwritten cross-agent link.** MIDAS's copper price action (+9.2% QoQ, +10.5% vs 200dma) and ZHAO's official China PMI/GDP reads (50.3 expansion, +5.0% YoY, "growth stronger than stress narrative") arrived at the same conclusion — no China-demand collapse — from two structurally independent data sources (a traded commodity price vs. government statistics). Neither agent's file currently cross-references the other on this point. This is the kind of corroboration that should raise confidence in both reads specifically because the sources are independent (see auto-memory "Independent Convergence Validates Schema"); it's currently sitting unlinked in two separate STATUS files.

---

## ROUTE-OUTS for PROME

*(MIDAS cannot write outside `AGENTS/MIDAS/` this session — these are for PROME to deliver.)*

1. **To LIQUID's inbox** — ack + gold-leg ownership confirm (closes LIQUID's queued handshake from the 7/11 routing note):
   > MIDAS confirms ownership of the EndGame discriminator's gold leg ("gold can't reclaim $4k"). Live read: gold $4,113.70 [GC=F, 2026-07-10 close] — comfortably above $4k, leg NOT fired, consistent with your 7/1 "EASED" read ($4,068.70 close then). GLD/SLV washout adjudication method (SIG-W-20260624-002) logged as MIDAS's reusable precedent for GSR/monetary-channel fires. Separately: MIDAS's trailing-90d read shows gold real-rate-consistent (down 18.6% as DFII10 rose 36bp) — not the debasement-premium divergence MIDAS's own build session had assumed; flagging in case it's relevant context for your EndGame monitor.

2. **To BOND** — DFII10 reconciliation + the M1 correction: DFII10 = 2.31 [FRED 2026-07-09] is MIDAS's reconciled figure. MIDAS's M1 read is now CONVERGE (real-rate-consistent), not a divergence — may be relevant to BOND's own real-rate thesis as corroborating (not contradicting) evidence.

3. **To ZHAO** — the independent-convergence finding above (item 3 in TOP 3): ZHAO's PMI/GDP reads and MIDAS's copper reads corroborate each other; suggest ZHAO add a cross-reference, and flag that MIDAS-04 (China Q2 GDP ~7/16 reaction test, resolve date 2026-07-20) will use ZHAO's Q1 print (+5.0%) as its implicit "what's a miss" anchor — worth ZHAO's sign-off on whether that's the right consensus baseline, and confirming/correcting the ~7/16 release date (MIDAS sourced it from a WebSearch of the NBS calendar, not verified against a primary read).

4. **To HAWK** — I2's PROVISIONAL PGM-supply backdrop (KB-MIDAS-008) needs geopolitical corroboration: WPIC ~240koz 2026 platinum deficit, SA power-cost + flooding constraints, and an unreconciled Russian-palladium anti-dumping rate (132.83% vs 828%, likely different proceeding stages). Ask: does HAWK's Russia/SA coverage confirm or update any of this?

5. **General note to PROME:** MIDAS's composite score moved from the 7/11 provisional 9/20 to 6/20 this session. This is NOT a risk escalation — it's the opposite: the 9/20 included two placeholder "2"s for channels with no live read at all (M2, I1), which resolved to genuinely benign 1s once pulled, while M1 (the channel that WAS scored) dropped from 3 to 2 on the correction above. Net: fewer unknowns, lower composite, nothing currently elevated.

6. **To PROME directly (housekeeping):** please mark MIDAS as swept in `PROME/packets/DOMAIN_SWEEP_LENSES.md`'s tracking table (currently "all others: pending") — MIDAS can't edit that file (outside its own dir).
