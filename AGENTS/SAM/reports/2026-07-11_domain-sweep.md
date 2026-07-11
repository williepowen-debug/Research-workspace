# SAM Domain Sweep — 2026-07-11 (Sat ~14:45 ET, markets closed)

**Mandate:** Will-directed inventory sweep despite parked-until-7/16 dashboard status (parked ≠ untaskable). Triage-first: report, don't execute analytics. Two approved mechanical exceptions applied (below). All levels stamped with vintage — nothing here is a live weekend price.

---

## 1. Known queued fixes

| Item | Finding | Age | Owner-action | Priority |
|---|---|---|---|---|
| **(a) gpif_flows.py PARTIAL-path crash** (lines ~355-358) | **ALREADY FIXED — task packet's framing is stale.** DAEDALUS's finding was fixed and committed same-day 7/10 AM (`8d1291dc`): `fmt_flow()` helper formats numerics normally, falls back to raw string for unset `'?'` keys, avoiding the `ValueError` on the `:+.1f` format spec that used to crash before `append_row()`. Re-ran today (7/11 ~14:51 ET) as fresh test evidence: `rc=0`, "Found 5 report link(s); 0 new since last run" — correct no-op between GPIF release windows, no crash. | Fixed 7/10, re-verified 7/11 | None — closed. Task packet should be corrected upstream (references a bug that's already resolved). | Closed |
| **(b) BOJ line-item verify** (S1-A fast-confirm scoping) | **Weekend-runnable document read — executed, not just re-scoped.** `.venv` has `openpyxl` 3.1.5 + `pandas` 3.0.3 (previously "not yet confirmed"). Fetched a live sample: `boj.or.jp/en/statistics/boj/fm/juq/d_release/jd/2026/jd20260327.xlsx` → HTTP 200, 18,699 bytes (matches the ~18-19KB estimate). Parsed cleanly with `openpyxl` — bilingual JP/EN row labels, 3 columns (Projections/Provisional/Final), full BOJ money-market-operations breakdown (JGB outright purchases, T-Bill purchases/sales, repos, pooled-collateral funding ops, CP/corporate-bond ops, disaster/climate ops, USD funds-supplying collateral). **Finding [CORRECTED same-day, follow-up session ~15:30 ET]:** there is **no explicit FX-intervention line item** — but the initial framing ("intervention is off-balance-sheet from this series entirely") was imprecise. MOF yen-buying intervention settles ~T+2 through the **"Treasury funds and others" (財政等要因)** line, which IS in the series; the established detection technique is the **gap between BOJ's projection of that line and private money-broker (Tanshi) same-day forecasts**. The line standalone is a huge, noisy daily aggregate (tax receipts, JGB settlements, pensions) — the signal lives entirely in the EXTERNAL forecast-gap leg, and SAM has **no automatable Tanshi-forecast source**. Same NOT-BUILD conclusion, corrected mechanism: a `boj_current_account.py` script pulling only the BOJ leg would fast-confirm noise. **NOT-BUILD decision executed 7/11 (Will-approved):** recorded in `OPEN_THREADS_2026-07-09.md` §2 (resolution block w/ evidence) + `MOF_INTERVENTION_PLAYBOOK.md` S1-A scoping note (semi-confirm = manual step: T+2 jd/jx XLSX + wire search for Tanshi-gap commentary) + struck from `MEMORY.md` NEXT SESSION 0a. | Scoped 7/10 PM, executed + recorded 7/11 | Closed — durably recorded, will not be re-proposed. | Closed |

---

## 2. 7/16 double-discriminator pre-registration — falsifiability check

| Leg | Owner | Resolver as currently written | Falsifiable? | Gap |
|---|---|---|---|---|
| **MOF weekly ITS** (wk 7/5-7/11, JST release ~7/16) | SAM | `docket/CATALYSTS.tsv` row: "Japan foreign-LT-debt BUYING **spike** = durable-leg corroboration; no change/selling = transient (baseline: 2wk net selling into 7/9)." | **Partially.** Direction is falsifiable (buying vs. no-change/selling) but **"spike" carries no ¥-magnitude threshold** — unlike SAM's own KEY THRESHOLDS table, which quantifies the sell-side stress line (>¥1.5T/week). A future SAM session could read a marginal ¥50B buying print as either "spike" or "noise" with no pre-committed number to arbitrate it. | **Under-specified.** Recommend registering a numeric buy-side bar before 7/16 (e.g., "≥¥500B net buying = durable-leg corroboration" — TBD by SAM, not this session per triage-first). |
| **May TIC** (net UST transactions, 4 PM ET 7/16) | SAM (Japan leg), routed to ZHAO for China leg | Explicitly scoped as a **consistency check only, not a direct arbiter** — May data predates the 7/8-9 event window it's meant to explain. Correctly caveated in both `CATALYSTS.tsv` and STATUS 7/9 EVE note. | **Yes, and honestly scoped** — the packet's own "double-discriminator" framing slightly overstates TIC's arbitration power; SAM's own file correctly downgrades it. No fix needed, just note the packet's framing is looser than SAM's actual registration. | None — already correctly hedged. |
| **BoK (Bank of Korea)** | **ZHAO** (not SAM) | **No falsifiable resolver found anywhere in SAM's files.** BoK 7/16 appears only in prose: STATUS.md forward-catalysts line ("Thu Jul 16 May TIC + BoK"), `research/outputs/PACKET_C_ASIA_DEMAND_HOLE.md` ("Full by 2026-07-16 (May TIC + BoK)" — Korea leg flagged "possible hike," USD/KRW ~1,530, needs Apr-TIC refresh), and a 7/5 ZHAO cc. **No numeric threshold, no hike-size bar, no resolver terms are registered for the BoK leg anywhere I can find** — not in `docket/CATALYSTS.tsv`, not in `CALENDAR.md`. | **No.** | **Real gap — cross-agent, not SAM's to fix unilaterally.** BoK is ZHAO's domain; the joint Packet-C synthesis due 7/16 needs ZHAO's leg pre-registered with the same discipline SAM applied to its own MOF/TIC legs, or the 7/16 session will have a ZHAO-side data point with no pre-committed grading. Flagging to PROME/ZHAO — SAM did not write into ZHAO's files. |

**Bottom line:** SAM's own leg (MOF weekly) is directionally falsifiable but numerically soft; TIC is honestly scoped as non-decisive; **BoK has zero registered resolver terms** despite being named a co-arbiter in three separate SAM documents. Recommend PROME route a "pre-register BoK terms before 7/16" ask to ZHAO.

---

## 3. Ungraded / overdue predictions

**Scoreboard (per PREDICTIONS.tsv preamble, unchanged since 7/10):** 10 CONFIRMED / 12 FAILED (SAM-36 added 7/10) / 1 resolved-special / 6 OPEN.

| Pred_ID | Prediction (abridged) | Confidence | Due | Status |
|---|---|---|---|---|
| SAM-28 | ≥1 tail-route fires ≥+3% FXY move | 40% | Through Sep 18 2026 | OPEN — not due, no action needed |
| SAM-29 | CFTC JPY short does NOT cover below −108K | 65% | Through Sep 18 2026 | OPEN — **watch tightened**: Jul-7 print at 68.8% of peak is drifting toward this line faster than expected (was 86.2% two prints ago); worth a note next live session, not overdue |
| SAM-31 | Cross-pair yen-haven re-couples | 35% | Through Sep 18 2026 | OPEN — not due |
| SAM-33 | BOJ does NOT deploy emergency long-end capping ops | 72% | Through Dec 31 2026 | OPEN — not due |
| SAM-34 | BOJ holds 1.00% at Jul 30-31 meeting | 85% | Jul 31 2026 | OPEN — **due in 20 days**, not overdue, but flagged for mid-July re-verify per MEMORY NEXT SESSION item 5 (not yet done) |
| SAM-35 | Jul-22 40Y JGB auction clears FIRM | 50% | Jul 22 2026 | OPEN — not due |

**No overdue rows.** SAM-36 was resolved same-day 7/10 (not stale). Ledger is NOT drifted behind STATUS — both were touched same-session 7/10 PM. **One genuine gap:** the MEMORY "NEXT SESSION" list carries an item (#4, "CH-010 accounting-basis question — REPRIORITIZED but still open") that the fresh WALTER signal (§4 below) now directly speaks to but which has not been folded into a THESIS update — see §5 gaps.

---

## 4. Unconsumed inbox items

| File | Age (as of 7/11) | Disposition this session |
|---|---|---|
| `inbox/WALTER/SIG-W-20260710-004.md` (DEWEY prompt-08: JGB super-long demand sign = ALM-buyer not forced-seller) | 1 day | **Processed this session** (mechanical hygiene, consistent with SAM's standing consume-step): logged to `board_log.tsv` as **noted**, moved to `inbox/WALTER/processed/`. Content bears directly on the still-OPEN CH-010 mechanism question (does forced-selling exist above 4.5%, or does the floor just deepen — OPEN_THREADS #5) — Nippon Life ESR only −2pp to 222% (still very strong), and the May −¥201.2bn sell print is now read as partially offset by Apr's +¥327.2bn (2-mo net **+¥126bn BUYING**, not the net-selling framing SAM-32's post-mortem carried). GPIF confirmed NOT the marginal buyer (25% weight unchanged; Katayama's jawbone read as rhetorical, not flow — consistent with `gpif_flows.py`'s FY2025 read already on file). **Not folded into THESIS.md this session** — a CH-010 re-scope (keep the 4.5% tail trigger but recharacterize as a J-GAAP statutory-impairment tail on legacy holdings, not a clean forced-seller) is analytic/canon-adjacent, proposed as a follow-up item (§5), not executed under triage-first scope. |
| `inbox/processed/*` (4 files) | All pre-7/9, already integrated per MEMORY | No action — confirmed already-processed, not re-touched |
| `outbox/*` (18 files, oldest May 26) | 46+ days | **Not touched.** Per root CLAUDE.md Data Hygiene, "outbox-kill" is explicitly out of scope (messaging-overhaul owns this). Noted only: `outbox/delivered/` is empty — none of the 18 outstanding outbox files have been manually marked delivered, though content review suggests most were long since integrated by recipients (BOND/LIQUID/HENRY/RED/PROME). Informational only, no proposed action given the explicit out-of-scope instruction. |

**Result: inbox lane is now clean (0 backlog)** as of this sweep.

---

## 5. Gaps — Japan/carry-side coverage into 7/16 and ~7/31

| Gap | Why it matters | Proposed priority |
|---|---|---|
| **METSUKE cross-consistency check never run** (carried in MEMORY as an open NEXT-SESSION item since 7/10 PM) | **Confirmed drift found this session:** `TRADE.md` line 38 still cites the OLD stale FXY modal band ($57.5-59.5, CH-032) with a caveat flagging it as "under re-derivation in STRATEGY.md" — but STRATEGY.md's re-derivation actually **completed** 7/10 PM (new band $55.3-57.7/USDJPY 159-166). TRADE.md's caveat is now itself stale: it points to a re-derivation that already happened, without citing the new numbers. This is a live R:R-relevant surface, not just narrative. | **High** — propose spawning METSUKE (verify-pass mode) next live session to formalize the drift-fix; not executed here (money-field-adjacent, propose-only by METSUKE's own design, and out of scope for this triage sweep). |
| **CH-010 above-4.5% mechanism — still open**, now with fresh DEWEY input (§4) pointing toward "net-demand-positive, not clean forced-seller" | Load-bearing for how the 40Y auction (7/22) and any future >4.5% print should be read — a re-scope changes whether a yield spike above 4.5% is bullish (ESR-driven buying) or bearish (forced selling) for JGB demand | **Medium-High** — propose as the top analytic item for next live SAM session, before 7/22 |
| **BoK 7/16 resolver terms unregistered** (§2) | Packet-C's "full synthesis due 7/16" cites BoK as a co-arbiter with zero falsifiable terms | **High, but not SAM's to build** — route to PROME/ZHAO |
| **MOF weekly numeric buy-side threshold missing** (§2) | Same 7/16 date; SAM's own leg is softer than it should be | **Medium** — 5-minute fix, propose for next live SAM session (not done here, analytic judgment call on the right ¥ bar) |
| **STATUS.md over the 250-line cap** (~348 lines currently per `wc -l`, cap is 250 per SAM's own CLAUDE.md Output Rules) | Flagged as "compression pass queued" in the 7/10 AM note, not yet done across two subsequent sessions (7/10 PM, and now 7/11) | **Medium** — pure hygiene, no analytic risk, good candidate for next session's first 15 minutes |
| **~7/31 window (BOJ MPM + MOF monthly intervention data + FY2027 purchase plan)** | Triple-stacked catalyst date 20 days out: SAM-34 resolution (BOJ hold 85%), MOF monthly = hard-confirm of the 7/2 no-strike call, FY2027 super-long purchase plan = SAM-33's backstop-vs-let-run test. All three currently sit as single CALENDAR rows with no consolidated pre-registration memo the way 7/16 got one (Packet-C). | **Medium** — worth a dedicated pre-registration pass (like the 7/9 Packet-C exercise) before ~7/24-25, not urgent this week |
| **Reverse-knockout FX option trigger map** (OPEN_THREADS §3, real-economy carry-convexity — record weak-yen bankruptcies) | Flagged as a "build candidate, not yet scoped" since 7/9; no dealer/options-flow source currently available to SAM | **Low/Background** — no source identified yet, nothing actionable to do this session |
| **BOJ current-account fast-confirm instrument** (§1b) | Now shown to be the wrong instrument (structural, not just under-scoped) | **Low** — close out as a dead end rather than carry it forward as "next step: build" |

---

## Summary

- **2 approved mechanical items closed:** gpif_flows.py confirmed already-fixed + re-verified clean (rc=0); BOJ line-item scoping advanced from "scoped, source found" to "executed, and the series is confirmed to be the wrong instrument" (a concrete negative result, not just more scoping).
- **1 inbox file processed** (WALTER SIG-W-20260710-004 → noted, moved to processed/); inbox lane clean.
- **0 overdue predictions**; ledger current with STATUS.
- **3 real gaps surfaced this session that weren't previously flagged as sharply:** (1) BoK has no registered resolver terms despite being a named 7/16 co-arbiter — cross-agent, routed to PROME/ZHAO; (2) MOF weekly's own resolver lacks a numeric buy-side bar; (3) TRADE.md's re-derivation caveat is now stale relative to STRATEGY.md's completed re-derivation — concrete METSUKE-catchable drift, confirmed not just suspected.
- **No trade recommendations.** No position change. FLAT stands.

---

## POSTSCRIPT — same-day follow-up execution (~15:30 ET, Will-approved via PROME)

Will approved the proposed items; executed in a second session same day. Status of the §5 gap table after execution:

| §5 gap | Disposition |
|---|---|
| MOF-weekly numeric threshold | ✅ **DONE** — ¥-bar registered before the print: ≥+¥500B BUYING = durable · ¥0-500B = ambiguous/lean-transient · <¥0 = transient CONFIRMED; release times ET pinned (MOF ~7:50 PM ET Wed 7/15 · TIC 4:00 PM ET Thu 7/16). → `docket/CATALYSTS.tsv` + `CALENDAR.md`. |
| TRADE.md band-caveat drift | ✅ **DONE** — line-38 stale caveat replaced with the re-derived bands (modal $55.3-57.7 · tail $59.2-62.0 · disorder <$54.9). Inline cross-consistency check run (no other surface cites a stale minor version). |
| CH-010 re-scope | ✅ **DONE** — THESIS v1.6.6 → **v1.6.7** (J-GAAP statutory-impairment TAIL disorderly-only; base case net-demand-positive under ESR; 2-mo net +¥126bn buying; mid-cap Fukoku/Asahi bifurcation watch). → `thesis/THESIS.md` + `thesis/CHANGELOG.md` 2026-07-11. |
| BOJ instrument dead-end | ✅ **CLOSED as NOT-BUILD, durably recorded** — `OPEN_THREADS_2026-07-09.md` §2 resolution + `MOF_INTERVENTION_PLAYBOOK.md` S1-A scoping note + struck from MEMORY 0a. §1b of this report carries the same-day mechanism correction (Treasury-funds-and-others / Tanshi-forecast-gap). |
| STATUS 250-line cap | ✅ **DONE** — 349 → 249 lines (7/6-7/8 + late-June notes → new TIMELINE Jul-6-10 block + pointers; Jul-2 market table → pointer; carry-anchor + thresholds CFTC/zone rows trued-up to the Jul-7 print / 7/10 marks). |
| BoK 7/16 resolver terms | **Routed** — PROME confirmed routing to ZHAO's inbox (Will-authorized); ZHAO's to pre-register before Thu 7/16. |
| ~7/31 pre-registration memo · reverse-knockout map · insurers/TRACKER bifurcation anchor | **Still open** — carried in MEMORY NEXT SESSION for the next live session. |

⚠️ New flag found during true-up: **CFTC next-print date conflict** — CALENDAR's 7/10 PM pass says "Mon Jul-13," standard COT schedule implies Fri 7/17 (Jul-14 data). Verify at next boot; flagged in STATUS thresholds row + MEMORY.
