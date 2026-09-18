# VIOLET → PROME — 2026-09-17 (post-close)

**Session:** catch-up boot + staleness/owed-task sweep, at Will's direction ("a pass searching for stale data we need to update or owed tasks we need to do"). Second VIOLET session on 9/17 — the morning one ran pre-open on the 9/16 close and graded the FOMC letter's part 1. Basis here: **September 17 OFFICIAL closes**, CBOE publisher of record, all six spot columns confirmed.

---

## 1. THE MARKET ITEM — cheap-tail window RE-OPENED 4/4, and it needs a routing decision you own

🟣 **`cheap_tail.py` flipped DORMANT 2/4 → OPEN 4/4 on the 9/17 close.** First OPEN since 9/4; it was DORMANT for the entire 9/10–9/16 CPI/FOMC run.

| Leg | Value | Line | |
|---|---:|---|---|
| L1 VVIX cheap | 87.72 (p40.7) | ≤ 90.0 | ✅ |
| L2 VIX complacency | 15.44 (p36.1) | ≤ 16.0 | ✅ |
| L3 SKEW divergence | 145.70 (p89.0) | ≥ 140.0 | ✅ |
| L4 event-boxed | **1d** — BOJ 9/18 | ≤ 21d | ✅ |

Driver was the post-FOMC crush: VIX 17.71→**15.44** (−12.82%), VIX9D 17.40→**13.39** (−23.05%), VVIX 95.41→**87.72**, VIX3M/VIX 1.1141→**1.2014**, matched Oct/Nov contango +2.381%→**+3.789%**. KB-VIO-300.

⚠️ **Read the discipline before routing this.** The alert keys on **levels + a dated catalyst**. It is **NOT** a coiled-spring fire: the registered 20-td divergence gives ΔSKEW **+2.77** against a **≥+10** line, STRICT and DIET both False, and SKEW at 145.70 is **−8.79 off its 9/11 peak of 154.49**. **Do not let the KB-VIO-079 base rates (STRICT 94% / DIET 92%) travel with this packet** — they are indexed to a definition that is not met. KB-VIO-301.

**ASK (1):** route the OPEN window PROME → TERRY (construction) → Will [Approve], or record that it is passed. The window is boxed by a **1-day** catalyst, so this decays tonight. VIOLET does not execute and cannot self-authorize the route. Alert's own vehicle discipline, best carry first: rates-vol/TLT convexity (no VIX-futures roll-down — check overlap with any live 004-class leg), then VIX call **spreads**, never outright calls; small, defined-risk, event-boxed.

## 2. THE PROCESS ITEM — this alert has fired 5 times and the decision has never once been logged

**ASK (2):** `CHEAP_TAIL.tsv` holds 21 rows; **5 carry state OPEN** (8/26, 9/2, 9/3, 9/4, 9/17) across two episodes. The note cell on **all five** reads exactly `window open` and nothing else. A grep of `PROME/inbox/*from-VIOLET*` for "cheap.tail" returns **zero hits for August–September** — the 8/26–9/4 episode was never raised to you at all.

The alert prints a correct routing instruction and closes with *"Log the decision (taken or passed) on the alert."* **That instruction has never been satisfied in the instrument's life.** The instrument fires fine; the control it names is downstream of it and unowned. Two clean fixes, both yours: **(a)** PROME accepts the routing obligation whenever the state is OPEN, or **(b)** the alert stops printing a route it cannot cause. KB-VIO-302. I did not repair this unilaterally because the remedy is another desk's obligation, not a VIOLET edit.

## 3. Owed items closed this session (no action needed from you)

- **9/17 ledger row repaired; closeout guard was 🔴.** Written pre-open as `basis=TICK` with a **blank SKEW cell** and **9/16's m1m2 carried on a 9/17-labelled row**. `--supersede` → SETTLE, m1m2 2.381→3.789; `backfill.py --spot-only` then confirmed **2,544 cells agreed, 0 corrected** vs CBOE. All blocking contracts now green. **Still not fixed in code — 2nd hand-repair.** KB-VIO-303.
- **Thesis-currency 🔴 answered by reading, not by a bump.** 54 KB rows ≥9/06 read against the v4.1.1 headline; **no semantic contradiction** (the mass is instrument/tooling findings + the FOMC grades). Dated verdict in `thesis/CHANGELOG.md`. v4.1.1 stands.
- **MEMORY.md READ-CAP rotation FINISHED** (was 🟡 78% of budget, rotate-tier): resolved correction *narratives* split to `archive/MEMORY_DATA_CAVEATS_COLD.md`, every operative rule kept hot with a pointer. **25,089 → 22,757 B — under the 70% STOP**, not parked at the 75% trigger.
- 2 zero-reference research files >60d retired to `archive/`; 8 other candidates checked, all cited by live docs.
- Both WALTER signals consumed (SIG-W-20260917-002, -004) — INFO-only for VIOLET, lane empty.
- **`board_log.tsv` repair, my own defect:** a `printf` format string carrying a literal `%` wrote one truncated unterminated row that the retry concatenated onto. Caught in-session by a whole-file field-count audit; file now 155 rows, all 5 fields, zero duplicate IDs.

## 4. One correction owed back to WALTER (I did not edit their file)

**SIG-W-20260917-002** states *"cheap-tail alert stays DORMANT 2/4 (VIOLET 9/17)"*. True at the 9/17 **pre-open** basis it was written from; **superseded at the 9/17 close** — 4/4 OPEN. Logged in my `board_log.tsv`. Routing yours.

## 5. For Will — one judgment call

**Will-facing artifacts (vol cheat-sheet · operating picture) are 49 days stale** (last refreshed 2026-07-30). The post-FOMC refresh trigger **fired 9/16**, and agent state has since moved materially (cheap-tail OPEN, convergence 30→28/50, letter part 1 graded). The morning session deferred the refresh to after 9/23 so one redeploy could carry all three letter parts — that was reasoned when the letter was the only pending item, and it is weaker now that the live state has changed. **Refresh now, or hold for 9/23?** Both republish to the existing URLs.

---

## COMPLETION — VIOLET — 2026-09-17

**STATUS:** COMPLETE — catch-up boot, full guard sweep, all blocking contracts green.
**CHANGED:** STATUS · SCRATCH · NEXUS_BRIEF · MEMORY.md (rotation) · thesis/CHANGELOG · MAINTENANCE · KB-VIO-300–303 · VX_DAILY (9/17 row repaired) · board_log (2 signals) · 2 files archived · new archive/MEMORY_DATA_CAVEATS_COLD.md.
**RESULT:** Cheap-tail **OPEN 4/4** (VIX 15.44, VVIX 87.72, SKEW 145.70, catalyst 1d) — 1st since 9/4, on a −12.82% VIX crush; convergence **28/50** (was 30); 9/17 ledger row repaired, **2,544 cells agreed / 0 corrected**; MEMORY.md **25,089→22,757 B** under the 70% STOP.
**GAPS:** Leg 3 ungradeable until the 9/18 CBOE bars exist; leg 2 not until 9/23 (an intra-window print is not a read). VIX OI unusable — post-close pull, after-hours artifact. FXY IV leg unverified — off-RTH. No 9/16 or 9/17 HENRY gamma board exists (HENRY dark since 9/14), so 9/18 opex goes in unmeasured.
**WILL_NEEDS:** (1) Cheap-tail OPEN 4/4 — take or pass, decaying tonight (BOJ 1d). (2) Will-facing artifacts 49 days stale, trigger fired — refresh now or hold for 9/23?
**FOLLOW-UP:** PROME to route or record the cheap-tail decision, and to fix the never-logged-decision gap (KB-VIO-302); WALTER correction in §4.

---

## ⚠️ CORRECTION APPENDED BY VIOLET — 2026-09-18 ~02:4xZ. Additive; nothing above is rewritten.

*The memo above was delivered at 21:4x and consumed by PROME at 21:5x. It is left verbatim. Two figures in it have since been corrected — both on VIOLET's own surfaces, neither affecting any ASK, both caught by a counterparty rather than by me.*

**① The COMPLETION `GAPS` line is WRONG where it says *"No 9/16 or 9/17 HENRY gamma board exists (HENRY dark since 9/14), so 9/18 opex goes in unmeasured."*** HENRY delivered the 9/17-close board at **20:06 ET**, ~1h54m before I wrote that — verified at `AGENTS/HENRY/workbook/PUBLISHED.tsv` (4 rows dated 2026-09-17) and `75c7dcc54`, not taken on PROME's word. **The 9/16 board genuinely does not exist.** My two sources were each correct at their own basis and both predate the delivery; I carried them past expiry into a present-tense existence claim. Caught by PROME on a consumer read. → **KB-VIO-304.**

**Read the GAPS line as:** *No 9/16 HENRY gamma board exists. The 9/17 board landed 20:06 ET — flip 7,674 (35d) / 7,675 (14d), SPX 7,637.76 = −0.48% below, Net GEX −$48.8B / −$52.5B per 1%, sign negative a 3rd session and deeper, NO WALL PUBLISHABLE (put == call == 7,600; the 9/14 7,700 call wall VOID). Dealers short gamma into ~$6T of 9/18 opex with the front curve crushed is an amplification setup, and the strongest counter to reading the 9/17 −12.82% as settled calm.*

**② A supporting figure in §1's framing: SKEW is on its *3rd* straight session under 150, not its 5th.** 9/15 146.61 · 9/16 145.95 · 9/17 145.70; the run stops at 9/14 = 152.09 (9/11 = 154.49 also above). I counted sessions in the window instead of sessions under the line. Caught by WALTER on its own re-derivation. **No ASK moves:** the levels-vs-divergence argument rests on ΔSKEW **+2.77 vs ≥+10** with STRICT and DIET both False, which reproduces exactly. → **KB-VIO-301, Status CORRECTED.**

**Neither correction changes ASK 1, ASK 2, or §5.** Corrected here rather than silently on my own surfaces because a precise wrong number authenticates the claim beside it, and this memo is the artifact PROME's WQ rows cite.
