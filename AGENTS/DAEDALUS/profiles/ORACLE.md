# Agent Profile — ORACLE

**Built by:** DAEDALUS · **Body date:** 2026-09-05 (whole rewrite; prior body 2026-06-29) · **Method:** solo full-tree read + **the subject's own guards RUN** (UPGRADE_PROTOCOL ★ rule)
**Sources read:** `CLAUDE.md` · `STATUS.md` (139 ln / 18,395 B) · `SCRATCH.md` · `TRADE.md` · `PREDICTION_MARKET_METRICS.md` · `NEXUS_BRIEF.md` · `MAINTENANCE.md` · `MEMORY.md` · `SIGNAL_INTAKE.md` · `workbook/` (10 files) · `tools/` (4) · `scripts/` (3) · `outbox/` (24) · `BLUEPRINTS/utility-agent.md` §role-ceiling table
**Guards executed:** `tools/metrics.py verify` → **rc=0**, reproduces every `dH` exactly and marks the retracted σ `UNREACHABLE` at every window · `scripts/test_search_coverage.py` → **rc=1**, failing loud on absent Kalshi creds (this box is the LAPTOP; the signed lane is desktop-only and ORACLE records lane state per-box by rule)
**Staleness:** refresh when the calibration-loop status changes, the role rubric materially changes, or **>45d** → checkpoint **2026-10-20**

> ⚠️ **THE 2026-06-29 BODY PREDATES ~24 SESSIONS OF WORK.** It graded a desk with 19 KB rows, 174 ODDS_LOG rows, one Kalshi pull and a TRADE.md stale since 6/19. Today: **79 KB rows** with a live SUPERSEDED/CORRECTED lifecycle · **1,233** ODDS_LOG · **7,254** HISTORY rows / 42 markets · **272** Kalshi rows · four purpose-built tools · a TRADE.md rebuilt 8/27 under a Will-directed redesign with machine-generated provenance. Its §7 open questions are answered below — that is the substance of this refresh.

---

## 1. Identity
Prediction-market diagnostics — real-money crowd-implied odds from **two venues**: Polymarket (Gamma/CLOB, public) + Kalshi (CFTC exchange, RSA-PSS signed, read-only). **Class: Utility** — grade vs `BLUEPRINTS/utility-agent.md`, never the market blueprint. **Role:** sentiment gauge / contrarian signal — *where real money agrees with or diverges from the fleet thesis.* Cedes all substance to domain owners (spreads→LIQUID, fundamentals→REGINALD, oil→BRENT, whether-the-attack-happened→HAWK) and **owns only the crowd read**. Read-only: states probabilities, never sizes or executes — TERRY sizes. **Spawnable by:** PROME / Will.

## 2. File anatomy (where the richness lives)

| Cluster | Files | State |
|---|---|---|
| **Governing** | `CLAUDE.md` (269 ln) — symmetric BOOT↔CLOSEOUT write-back, CONTRACT block (:14), route matrix, 5-type signal taxonomy, EXIT RULES | LIVE; the boot↔closeout mirror is the fleet **sourcing exemplar** |
| **Role rubric** ⭐ | `PREDICTION_MARKET_METRICS.md` (272 ln) — entropy, KL-bits dislocation score, tradeable-gap discount stack, k-σ entropy-collapse alert, signal fusion, TERRY handoff packet, anti-patterns | exemplary; far above the utility floor |
| **Live state** | `STATUS.md` — Alerts-first, 3-tier ~55-market dashboard with per-figure platform/date/volume, Convergence Matrix, Maintenance flags | dense and current (9/4) |
| **Handoff** ⭐ | `SCRATCH.md` — CARRIED FRAMING / WHAT I DID / NEXT SESSION (dated, priority-flagged) / CARRY-FORWARD / OPEN HYPOTHESES | **the best handoff surface I have read on any desk.** See §4.1 |
| **Cross-agent** | `NEXUS_BRIEF.md` — mandatory every closeout, `As of:`/`STATUS commit:` stamped | conformant |
| **Routing** | `TRADE.md` — rebuilt 8/27 (Will-directed): every routed figure carries **its own trajectory**, machine-extracted by `tools/trade_marks.py` → `TRADE_MARKS.tsv` (190 rows), **no vintage hand-typed**, and the tool **refuses to difference across a slug change** (‖) | ⭐ see §4.2 — this is the fix-form for a rot that recurred twice |
| **Record** | `KB.tsv` 79 (63 ACTIVE / 8 CORRECTED / 5 SUPERSEDED / 2 STALE / 1 RESOLVED, DerivedFrom chains) · `ODDS_LOG.tsv` 1,233 · `HISTORY.tsv` **7,254 daily rows / 42 mkts** · `KALSHI_ODDS_LOG.tsv` 272 (separate schema — ⛔ never merge) · `VX.tsv` 10 · `DISRUPTION_SUPPLY_SPREAD.tsv` 19 · `T6_PIN.tsv` 8 (event-scoped, spent) | exemplary |
| **Tools** | `scripts/{polymarket,kalshi}.py` (fetchers) · `tools/metrics.py` (entropy/KL/collapse **+ `verify`**) · `trade_marks.py` · `disruption_supply_spread.py` · `t6_pin.py` · `scripts/test_search_coverage.py` | rich; two known limits named in §6 |

## 3. Per-dimension local representation (utility floor + per-role ceiling)

| Dimension | Where it lives | Form | Rich? |
|---|---|---|---|
| **CONTRACT** (produces/consumed-by/proof) | `CLAUDE.md:14` | formal 3-line block — **LANDED** since the old profile flagged it missing | conformant |
| **Role rubric** | `PREDICTION_MARKET_METRICS.md` | entropy / KL-bits / discount stack / fusion / handoff | ⭐ exemplary |
| **Structured record** | 8 accruing workbook ledgers, valid schemas | KB lifecycle + two machine time-series + daily trajectory spine | ⭐ exemplary |
| **Standing disciplines** | `CLAUDE.md` + overlay | no-naked-numbers · thin(<$5K)⚠️-never-marked-on-one-print · ≥3-day re-check · anchor-to-surprise-not-headline · `closed`-field authoritative for resolution · **cite MID on wide books** · **record lane state PER-BOX** | ⭐ exemplary |
| **Cross-agent routing** | route matrix + `SIGNAL_INTAKE.md` + `NEXUS_BRIEF` + 24-file outbox | condition→target→priority; **retractions routed as first-class packets** | ⭐ strong |
| **CALIBRATION LOOP** (the blueprint's per-role truth-loop) | registered as **"Brier scoreboard"**, `utility-agent.md:53` | **DOES NOT EXIST** — 0 hits for `brier` anywhere in the tree, and ORACLE never claims one | 🔴 **the gap — §7** |
| **Authority/safety** | `TRADE.md` + METRICS §0 | read-only boundary stated explicitly | conformant |

## 4. Deviations from standard — three that are better than the standard

**4.1 — The handoff surface carries its corrections ABOVE the text they correct.** `SCRATCH.md` opens with **CARRIED FRAMING — do not re-derive from older text**, and the first entry is ORACLE's own withdrawal of its headline finding of that same session, placed *above* the superseded framing it retracts. A re-reader hits the correction before the claim. This is the fix-form for `[[finding_summary_section_merges_what_the_body_separates]]` — the abstract is where a correction normally lands last, and ORACLE inverted it. **Portable to every desk that keeps a handoff file.**

**4.2 — `TRADE.md` answers rot with visibility rather than freshness.** The file rotted twice (I caught it at 21 days; a Will-directed sweep caught it again at 15). The 8/27 rebuild does not just refresh — every figure now carries its own trajectory, machine-extracted from the append-only logs, so **a stale row announces itself** without a reader checking a header. Its own words: *"A refresh alone only resets the clock on the next rot."* Plus a contract-identity guard that **segments on slug change and refuses to difference across the break** — which is precisely the slug-rot defense (three-slug bank-failure "fade" that is not a move; month-stamped WTI-$100 legs that are four separate contracts).

**4.3 — `metrics.py verify` is a two-direction guard, which is rare.** It re-derives every published `dH` (all reproduce ✓) **and** sweeps every rolling window to ask whether *any* choice could reproduce the published σ — printing `UNREACHABLE` where none can. It confirms what is right and refuses to re-derive what was wrong, in one run. Three published σ stand retracted on its output (`KB-ORC-064 → CORRECTED`) while the directional findings survive. **This is `CHECK_STANDARD` §3 satisfied by an agent that has never read it.**

**Vestigial-but-live (do NOT "fix"):** the Convergence Matrix and `TRADE.md` are market-template labels on genuinely utility content (which markets are firing; no-sizing routing). They are **EQUIVALENT, not DARWIN-dead** — never delete them as market-construct violations, and never grade ORACLE against the market blueprint for having them.

## 5. DO-NOT-TOUCH

1. **Two-venue EXECUTE contract** — every session pulls BOTH fetchers. Kalshi creds live OUTSIDE the repo (`~/.config/kalshi/`, chmod 600), **never committed**; `KALSHI_ODDS_LOG` has a separate schema (OI + cents) — ⛔ do not merge into `ODDS_LOG` (8 mis-shaped rows were appended then scrubbed 6/27).
2. **Lane state is PER-BOX, never a fleet fact.** Verified live: this laptop has no `~/.config/kalshi/`, so the signed lane is genuinely dead here while STATUS correctly records it LIVE on the desktop. The discipline is load-bearing, not bookkeeping.
3. **The 0-ships `⛔RESOLVED` flag is a known FALSE POSITIVE** — row annotated DO-NOT-REPLACE; it fires every session by design. ⛔ Do not "clean up" the warning.
4. **KB lifecycle:** mark SUPERSEDED/CORRECTED with a DerivedFrom pointer — **never delete** a superseded row.
5. **`polymarket.py history` writes two rows stamped today** (intraday bar + live point). ⛔ Do **not** one-line-dedupe: those duplicate rows are what made the 9/4 NFP pre/post reconstruction possible. ORACLE's call — *decide which consumer you serve first* — is correct and should be left standing.
6. **Symmetric boot↔closeout.** Breaking the mirror is what previously left SCRATCH/NEXUS_BRIEF broadcasting retracted claims (the 6/22 remediation).
7. **The three retracted σ stay retracted.** `metrics.py verify` is the receipt.

## 6. Findings (2026-09-05, all verified at the artifact)

**🟠 F-1 — The registered downgrade trigger has no instrument that can ever fire it.** `CLAUDE.md:201` carries a standing rule: *"If prediction markets consistently wrong (track accuracy over time), reduce signal weight."* Nothing in the tree tracks accuracy over time. This is the **untrippable-band class** — a threshold with no metric surface — and ORACLE is the desk that spent its entire 9/4 session catching that exact defect in *other* desks' instruments. It is the same finding as the missing calibration loop (§7), stated where it actually bites.

**🟡 F-2 — Two carried items are ORACLE-lane and have each slipped twice.** `T6_PIN.tsv` freeze-or-drop from `LEDGER_GLOB` (SCRATCH item 10, "was item 11 last session"; now unambiguous — T6 is graded) · the Sept Iran-shipping on-date re-search (item 4; the Hormuz weekly roll has "run late five consecutive times", which ORACLE itself has already converted into a hard literal-date gate). Not defects — correctly carried, dated and self-diagnosed. Recorded so the next refresh can check whether the hard-date gate worked.

**🟡 F-3 — `t6_pin.py` prints no leg summary after `WIN_END`** (PROME 8/30, reproduced by ORACLE 9/4). Correctly **not fixed** — the test is spent — with the design lesson carried forward instead. Right call.

### ⚠️ Where I was wrong — struck before this shipped
- **"`test_search_coverage.py` exits 0 on a crash"** — **FALSE, struck.** It exits **rc=1**. My first measurement read `$?` after a pipe into `tail`, so I was scoring `tail`'s status, not the script's. **I flagged a silent-failure defect using a silently-failing measurement**; caught on re-measure. `[[finding_test_the_guard_not_just_the_guarded]]` turned on my own instrument.
- **"The Brier gap is the same shape as the Meta-L5 roadmap leg I struck on 8/17"** — **FALSE, struck before ruling.** I had the precedent lined up and it does not apply: `utility-agent.md:53` registers the calibration loop **per role, in the blueprint itself**, so it is adjudicated per-agent by construction and the "never adjudicated at any grade in the class" argument is void. A correct-looking precedent nearly produced a wrong ruling. See §7.
- **Came back clean:** CONTRACT block present (:14) · TRADE.md live (8/27, not stale) · KB lifecycle exercised (8 CORRECTED / 5 SUPERSEDED) · both fetchers accruing · 9/4 commits confirmed on origin · `metrics.py verify` reproduces.

## 7. ⚖️ THE RULING I OWED — Brier scoreboard: gap or ceiling? *(open since 2026-06-29; 68 days)*

**The 2026-06-29 question was a false dichotomy.** It asked whether the Brier scoreboard is *"required at L5-utility or DAEDALUS-row-local."* It is **neither**: `BLUEPRINTS/utility-agent.md:53` registers a **per-agent "Calibration loop" column** — WALTER `delivered_but_unconsumed` · NEXUS brief-vs-peer-brief diff · RED steelman/odds hit-rate · TERRY realized-vs-constructed · YEYOU flag-accuracy · **ORACLE Brier scoreboard** — described in the blueprint's own words as *"the role's truth-loop — the utility analogue of a market predictions ledger."* The blueprint's THIN FLOOR + ROLE CEILING design had already answered it; nobody had gone and read the answer.

**VERDICT: GAP, not a PAT-028 structural ceiling.** The 6/29 tractability objection was Polymarket slug-rot — markets resolve and drop, so can resolution even be scored? That objection is substantially answered by artifacts built *since* it was raised: **`HISTORY.tsv` (7,254 daily rows / 42 markets)** is a spine that survives slug rot · the **`closed`-field-authoritative** resolution rule already exists as discipline · **`TRADE_MARKS.tsv` already segments on slug change and refuses to difference across a break** — that *is* the slug-rot defense, built for a different purpose · and ORACLE demonstrably reads settlement (all 30 August Iran on-date legs settled 0.0% except 8/31 at 97.0%).

**But the ask must be re-scoped, and this is the substantive half.** "Brier scoreboard" is ambiguous between scoring *the crowd* and scoring *ORACLE*, and ORACLE mostly does not publish its own forecasts — it reports the crowd's. The loop its own charter already requires is scoring **the crowd**: `CLAUDE.md:201`. So the ask is not *"build a Brier scoreboard"* but **"build the instrument that makes `CLAUDE.md:201` executable"** — one table: slug · resolution date · outcome · ORACLE's logged probability at N days prior · Brier contribution. Every input already exists in the tree.

⚠️ **A real ceiling NOTE survives, scoped to a SUB-PART, not to the instrument:** only markets that resolve inside the log window can score, so early output will be dominated by short-dated legs (CPI/U3/Fed rungs) and will say little about the long-dated geopolitical book — which is where ORACLE's most-routed reads live. **Declare that limit in the scoreboard's own header** rather than letting a thin early score read as a verdict on the desk.

### 🔴 …and the ruling surfaced a defect on MY surface, not ORACLE's
**The blueprint requires a calibration loop per role and then grades nothing on it.** The utility L-ladder legs are **L3** role rubric applied consistently · **L4** output consumed by others · **L5** clean closeouts, zero YEYOU flags, current. **None of them reads the Calibration-loop column.** So a utility agent can reach **L5 with its registered truth-loop unbuilt**, purely because no leg looks — while at market class the stated analogue (*"predictions resolving"*) is an **L3** leg. The same requirement is load-bearing at L3 in one class and unreachable by any leg in another.
**Consequence for ORACLE, stated plainly:** its L4 is honest and its L5 line has been keyed to a leg the ladder does not actually contain. **This is a blueprint change, not a map edit — it is Will's to approve, and I am proposing it, not executing it.** Registered as a DAEDALUS build item; ORACLE is not blocked on it and should build the instrument regardless, because `CLAUDE.md:201` requires it independent of any grade.

## 8. Grade — **L4 (H) HELD.** Per-leg verdicts (UPGRADE_PROTOCOL review-rule 2)

| Leg (Utility class) | Verdict | Basis |
|---|---|---|
| L1 STATUS + BOTTOM LINE | **PASS** | 139 ln, alerts-first, BOTTOM LINE present |
| L2 structured record, valid schema, accruing | **PASS** | 8 ledgers accruing; KB lifecycle exercised (8 CORRECTED / 5 SUPERSEDED) |
| L3 role rubric applied consistently | **PASS** | `PREDICTION_MARKET_METRICS.md` applied live — entropy/KL scored on the 9/4 NFP event study |
| L4 output consumed by others | **PASS** | NEXUS via brief; SAM *"your verdict applied in full"* (8aca398ce); PROME routed the 9/4 adjudication onward to HENRY/RED/WALTER + DOCKET L125/L272 |
| L5 clean closeouts | **PASS** | 9/4 closeout clean, 3 commits confirmed on origin, push receipt in SCRATCH |
| L5 zero YEYOU flags | **WAIVED** | no YEYOU feed exists fleet-wide (charter-standing waiver, not an ORACLE concession) |
| L5 current | **PASS** | last session 9/4 = yesterday |
| **Role ceiling — calibration loop (`utility-agent.md:53`)** | **FAIL** | Brier scoreboard does not exist; `CLAUDE.md:201` has no instrument (§7) |
| *(ladder-leg coverage of the above)* | **NOT-ADJUDICATED** | no utility L-leg reads the calibration column — the defect is mine, §7 |

**Conf H** — read the artifacts and ran the guards. **L4 held, and the hold is now honest rather than vague:** every generic L5 leg passes; what fails is the per-role calibration ceiling, which the ladder does not currently read. Resolve the blueprint question with Will and ORACLE's grade follows in one step either way.

**L5 next-upgrade line:** *build the instrument that makes `CLAUDE.md:201` executable — crowd-resolution scoring off `HISTORY.tsv` + the `closed` field, with the short-dated-bias limit declared in its own header. Blocked on nothing at ORACLE's end; the ladder-leg question is DAEDALUS's to put to Will.*

## 9. Owed BY DAEDALUS to ORACLE (from its SCRATCH, both agreed and unmoved)
1. **The three-window vocabulary** — *"a registered trigger should name (a) close-vs-intraday, (b) the eligibility window explicitly, (c) one-sided vs two-sided."* ORACLE's carry-forward says this *"stays with DAEDALUS as agreed."* It is earned from a live failure: T6's tool was built around the 8/21–8/28 pin window while the trigger stayed eligible from 8/10, and **the mismatch walked PROME into measuring the wrong window.** → `CHECK_STANDARD` / `STATE_VOCABULARY` candidate.
2. **ORACLE's "spec-has-implementation check" prototype** — Tier-2, agreed with Will, not started, to be sent to me. Its declared honest limit: *it cannot catch "code exists but computes it wrong."*

## 10. Cross-check candidate (NOT asserted — outside this batch)
`NEXUS/CONFIRMED.md` is described in NEXUS's own charter as a *"thesis scorecard (trophy case)"*. A scorecard of confirmations only cannot falsify (**PAT-060**, default-zero instrument). NEXUS is L5 Utility with its own registered calibration loop (brief-vs-peer-brief diff / mined-edges) and was refreshed 9/3, so **this is a question to ask at NEXUS's next touch, not a finding.** Flagged only because §7's ladder gap means a scorecard-shaped calibration loop would never have been graded either way.
