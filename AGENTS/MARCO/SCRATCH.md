# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-08 ET (session 12 — boot + organized info-pull plan + Pull Session 1 catch-up + integration)

## CHANGES SINCE (what moved while offline, session 11 → 12)
- **Jun 5 May NFP printed** (was un-integrated at boot): +172K, UR 4.3% held, Apr revised UP to +179K (from +115K). **L&H +70K = World Cup hiring mask** (BLS-attributed).
- No other new *market* prints between sessions. Git was already clean + synced to origin at boot (session-11 deferred push had landed via a "laptop:" commit).
- Next data: **Jun 10 CPI (🔴 ES-MARCO-08), Jun 11 StatCan May + World Cup opens, Jun 13 Air Transat exit.**

## WHAT I DID (session 12)
**1. Built the organized info-pull plan** (Will: "list what's stale/passed, get organized"). Swept docket/EXPECTED_SIGNALS/PREDICTIONS/dashboard vs today. Grouped A (passed/pullable now) / B (imminent this week) / C (late-June calendar) / D (stale values) / E (Q2-close resolutions). Task list #1–4 tracks the A-items.

**2. Ran Pull Session 1 (the "catch-up" tranche) + integrated:**
- **A1 May NFP** → L&H +70K = **World Cup labor-side event-mask** (same trap as MIA pax — WC now masks on TWO surfaces). ES-01 MASKED not resolved.
- **A2 MCO/FLL Apr pax** → BLOCKED (April YoY locked in non-extractable airport PDFs; search only surfaces operational-disruption news). Gained: FLL 2025 −8.5%, Spirit-bankruptcy shrinking FLL capacity. **Deferred ~mid/late-Jun.** MAR-22/MAR-24 stay OPEN.
- **A3 LVCVA Vegas Apr** → visitors −1.8% / conv +3.2% / ADR record. **ES-07 NOT breached** (−1.8% « >5%).
- **A4 TX border revenue** → GROWING (El Paso Co +2%, RGV growth). **ES-04 counter-signal → DID_NOT_APPEAR.** Cross-border erosion is slow-structural (Dallas Fed swe2602), not acute cliff.
- **Integrated everywhere:** VX (NV-01, TX-03), KB (+3 rows: WFD-NFP-01, NV-02, TX-04), EXPECTED_SIGNALS (ES-01/04/07), STATUS (header/NFP row/LAS row/composite), docket (NFP re-dated to ~Jul 2; CALENDAR re-anchored to 6/8), outbox (WC dual-mask → NEXUS+CARL).

## WHAT I DID (session 12 — block 2: boot.py automation build)
Will flagged a maturity-gap question (MARCO boot vs SAM/BRENT). Compared: MARCO has the *document* shape (thesis/docket/workbook/symmetric protocol) but lagged on automation. Three gaps found: (1) no `boot.py`, (2) no `NEXUS_BRIEF.md`, (3) no PREDICTIONS_ARCHIVE/calibration-scoreboard. Ahead on EXPECTED_SIGNALS + ROOMS. **Built the boot.py kit** (commit `e5f721ef`):
- `scripts/catalyst_countdown.py` (docket countdown), `scripts/predictions_due.py` (free-text Timeframe parser, fails-loud — unit test caught + fixed a year-digit-as-day regex bug), `scripts/staleness.py` (STATUS/VX drift), `scripts/boot.py` (orchestrator).
- **Design locked per Will:** adopted SAM's run-at-boot-defensively pattern (timeout + non-fatal) + **mtime cadence-skip** on the 3 domain fetchers (monthly series not re-pulled every boot) — rejected my initial read-only/`--pull` split as a deviation from the mature pattern.
- Validated end-to-end: Jun 10 CPI flagged 2d-out, MAR-01/18/26 due Jun 30, banxico/h2a skip on cadence, live slaughter fetch through the wrap (refreshed baselines through Jun 6). Wired into CLAUDE.md boot step 3 + FILES table.
- **⚠️ ACTION NEEDED (Will):** `openpyxl` missing from `.venv` → `h2a_pull.py` will FAIL until `.venv/bin/pip install openpyxl` (non-fatal — boot continues, shows ❌). I did NOT install it (shared-venv change).
- **`NEXUS_BRIEF.md` — BUILT** (session 12 block 3, commit pending): drafted from NEXUS schema R3+amd7, 78 lines (vs SAM 76 / BRENT 81 / VIOLET 77). Heavy cross-domain (5 SENDING edges: REGINALD/CARL/LABOR/BRENT/NEXUS). Flagged the Jun-10-CPI shared-discriminator Type-B (BRENT energy-CPI leg + MARCO produce leg resolve at one print) + World-Cup dual-mask. Wired mandatory write-back into CLAUDE.md closeout step 10 + fixed the stale git step 11 → pathspec. **Both SAM/BRENT boot-maturity gaps now closed (boot.py + NEXUS_BRIEF).**

## KEY READ (session 12)
**3 of MARCO's acute regional-consumer-stress expected-signals are NOT firing at their Q2 deadlines** — ES-01 (hospitality, World-Cup-masked), ES-04 (TX border revenue, growing), ES-07 (Vegas, −1.8%). This is NOT thesis-breaking: the two **durable** channels (ag-labor 2.2M stock shock + Canadian air/snowbird) are untouched. It confirms the v2.x **slow-structural-squeeze** reframe over the old acute-multi-front-crisis framing. Separates mechanism (intact) from threshold (not breached) — same discipline as the Canadian-headline and produce calls.

## KEY OPERATIONAL CAVEAT (carry forward)
**World Cup now masks on TWO surfaces: MIA pax AND hospitality jobs.** A Jun/Jul beat in either is event-driven, NOT recovery. Tell = no *sustained* strength after Jul 19 (ES-MARCO-09 NTTO read ~mid-Aug). Sent to NEXUS/CARL via outbox.

## NEXT SESSION — Pull Session 2 (STAGED for Wed Jun 10 CPI)
1. **🔴 Jun 10 (Wed) BLS May CPI fresh F&V = ES-MARCO-08** — the produce-vs-pump fork. F&V holds ≳5% YoY *while pump prices fall* → transient freight driver exiting, labor re-weights UP (MAR-14 hold/upgrade); F&V softens in step with diesel → freight carried more of the spike. Apr was +6.1% YoY / veg +3.1% MoM. Cross-read vs BRENT pump data.
2. **Jun 11 StatCan May travel** — read the 2-yr STACK (worse than −30%?), air <−8%; headline YoY is base-effect.
3. **Jun 11 World Cup opens** — no data until mid-Aug NTTO; anecdotal host-metro watch only.
4. **Jun 13 Air Transat YUL-FLL final flight** — confirm executed → complete US exit.
5. **Pull Session 3 (~Jun 27–30, Q2 close):** WestJet winter, ICE reconciliation rework, Banxico state-of-origin + OFLC H-2A; **RESOLVE at Jun-30:** MAR-01/MAR-18/MAR-26 + formally close ES-04/ES-07 as DID_NOT_APPEAR.
6. **Re-pull MCO/FLL Apr pax** (~mid/late-Jun) — was PDF-blocked this session.

## OPEN THREADS
| Item | Status |
|------|--------|
| ES-MARCO-08 produce-vs-pump test | 🔴 Jun 10 CPI (Pull Session 2) |
| ES-MARCO-09 World Cup reversal test | 🟠 NTTO June print ~mid-Aug |
| ES-MARCO-04 (TX border) / ES-07 (Vegas) | 🟡 counter-signal → formal DID_NOT_APPEAR at Jun-30 |
| ES-MARCO-01 (FL hospitality) | ⚠️ World-Cup-masked; re-read post-Jul-19 |
| MCO/FLL April pax | 🟡 re-pull ~mid/late-Jun (PDF-blocked) |
| ICE/CBP reconciliation rework + floor vote | 🟠 ~late-Jun TBD |
| WestJet winter 2026-27 schedule | 🟠 ~Jun 27 — TOUR-05 last input |
| Cross-agent re-sends (4 for NEXUS + REGINALD/LABOR) | 🟡 still deferred — mail-dedicated spawn (NEW: WC dual-mask outbox written 6/8) |

## Mail state
Inbox empty. **Outbox: 1 written 6/8** — `2026-06-08_to-NEXUS-CARL_worldcup-dual-mask.md` (awaiting HERMES sweep). Old acute-crisis cross-agent corrections still deferred per Will.

## ⚠️ PENDING PUSH — LOCAL ONLY (standing instruction)
**Will coordinates the GitHub push himself** (many agents concurrent). At boot the tree was clean + synced; **session-12 commits (LOCAL, 2): `ceffbb4a` (Pull Session 1 integration) + `e5f721ef` (boot.py build)** — do NOT push until Will directs. Do NOT pull/rebase while other agents have uncommitted work. (Memory: [[feedback_defer_push_coordinate]].)

## Handoff
Productive, well-scoped session. Will asked to get organized before pulling, so I built the A–E pull plan first, then executed the "catch-up" tranche (Pull Session 1) and integrated it cleanly. The substantive finding: the acute regional-consumer-stress layer (hospitality jobs, border revenue, Vegas) is NOT producing the expected Q2 stress signals — one masked by the World Cup, two genuinely absent — which reinforces the slow-structural-squeeze reframe without touching the durable channels. The reusable catch: the World Cup is a dual-surface mask (pax + jobs); flagged to NEXUS/CARL. Pull Session 2 is staged and waiting on Wed's CPI (the 🔴 ES-MARCO-08 produce-vs-pump fork). All files current + column-validated; outbox queued; push deferred per standing instruction.
