# PROME STATUS.md
**Updated:** 2026-09-12 11:4x ET. Prior stamps → `PROME/archive/STATUS_HISTORY.md` §stamps.
**Last spine audit:** 2026-09-05 — re-run when >7d. Findings, residue and prior runs → `PROME/archive/STATUS_HISTORY.md` §spine.
**Companion reads (this file does not restate them):** continuity → `PROME/HANDOFF.md` · next-session state → `PROME/SCRATCH.md` ★ NEXT · Will's items → `PROME/WILL_QUEUE.md` · catalysts + dates → `PROME/DOCKET.tsv` · fire-ledger → `PROME/GATES.tsv` · regime → `HEARTBEAT.md`.

---

## Current Work Queue — PROME's own actions

**Scope.** This queue highlights **selected PROME operational priorities and follow-ups. It is not an exhaustive task inventory.** Read it alongside the other required boot sources; **DOCKET owns registered dates, GATES owns gate state, and the relevant source artifacts establish completion.** Other desks' work is in § Owner lanes. Written at closeout; every state below was checked at the named source at the observation time given in the column header.

| PROME action | Canonical record | State — each checked at the named source between 22:10 and 22:51 ET on 2026-09-11 |
|---|---|---|
| HEARTBEAT 15th re-base — **PROME acts** | No DOCKET or GATES row; also carried by `PROME/SCRATCH.md` ★ NEXT item 1 | Over the rotation line. **Trigger: ≥24,412 B (75% of the 32,550 B read cap). Done: re-based below 22,785 B (70%), history to a pre-re-base snapshot.** Current size from `PROME/tools/measure.py HEARTBEAT.md`; `PROME/tools/prome_gate.py` meters it at boot. A prior session ruled it the first act of the next boot. |
| Consumer read at BRENT's artifacts for **GATE-BRENT-COT-35B**, then flip or escalate | `PROME/GATES.tsv`, row `GATE-BRENT-COT-35B` | 🔴 **BLOCKING, and this is the session-exception Will authorised on 2026-09-12.** `review_by` 2026-09-11 has now PASSED; `last_checked` 2026-09-06 (BRENT vintage #4, as-of 9/1). Consumer read done at BRENT's artifacts 2026-09-11 23:0x: `AGENTS/BRENT/STATUS.md` still carries vintage #4, so **the as-of-9/8 grade has not landed**. ⛔ BRENT owns the grade. The date was NOT moved, no grade was invented, and the gate was NOT cleared. **Done: BRENT grades, or PROME escalates to Will. FIRST act of the next boot.** |
| **Reconcile the REQ-002 delivery/consumption discrepancy — PROME acts**, then consume or close | `PROME/DOCKET.tsv` L244 | ⚠️ **The sources disagree and this row does not pick a side.** L244: **DELIVERED 2026-09-10**, successors L322/L323 registered, and the row itself says *"PROME consumer read owed at the 9/11 boot"*; VULCAN's receiver-side encode confirmed 9/11 (`eea6d3948`). But `HEARTBEAT.md` §6 and the 9/10 HANDOFF entry both read *"REQ-002 **consumed** 9/10"* — which may refer to DEWEY's delivery being consumed, not PROME's read. **Done: establish at L244 and the DEWEY report which of the two is meant, then either record the consumer read or close the row.** ⛔ The previously carried *"9/15 PENDING"* is stale against L244 and is retired. |
| `CLOSEOUT.md` rotate-vs-hot/cold decision — **PROME decides** | `PROME/DOCKET.tsv` L338 (also `PROME/SCRATCH.md` item 3) | Over its read-cap line and **grew again tonight** (the WQ-233 amendment plus its correction); current figure from `python3 PROME/tools/measure.py PROME/CLOSEOUT.md` against the 24,412 B line. ⚠️ `read_cap_check.py` divides by the 54,250 B token ceiling, not the 32,550 B read cap — its `% of cap` reads ~40% low; use `prome_gate` or `measure.py`. **Trigger already met. Due: before the next amendment to that file — not calendar-dated, so any edit to `CLOSEOUT.md` is the deadline. Done: THE DECISION is recorded — rotate, or split hot/cold. ⚠️ L338 asks PROME to DECIDE, not to perform the reduction; carrying the decision out is separate work that follows it and is not this row's completion test.** | **2026-09-12: L339's procedural half (leg g) now lands on this row** — `CLOSEOUT.md:55` and `.claude/skills/closeout/SKILL.md:6` require the dashboard build to be RUN, never to SUCCEED. ⛔ Deferred, NOT blocked: this row needs the DECISION before an amendment, not the split; an earlier PROME wording overstated that. Row is COVERED by the next PROME boot and is NOT done. |
| `PROME/state/ORCH_LOG.tsv` repair (`zero_capital=OK`) — **PROME commissions the read and makes the edit** | `PROME/SCRATCH.md` owed item ⓑ | Two-correction stop **TRIPPED** on that file. **Blocked until an independent cold read of the proposed diff happens — PROME spawns the reader (`coldreader`); it is not waiting on anyone else. Done: the repair lands after that read.** |
| Consumer read of BRENT's **BG-02** re-grade, when it lands | `PROME/DOCKET.tsv` L329 + BRENT's VX row | BRENT has **not** re-graded since the 2026-09-11 Saudi MoE statement. A shutdown statement is not a throughput measurement; the ≥0.7 mb/d 7-day-MA resolver runs to 2026-09-25. PROME consumes, BRENT grades. |

---

## Owner lanes — not PROME actions

Listed so they are not mistaken for PROME work, and so their standing instructions survive. Each desk owns its own state; PROME does not chase.

| Lane | Owner | Standing instruction |
|---|---|---|
| DEWEY queue drain | DEWEY | Current work = its DOCKET rows. ⛔ Do **not** spawn off the old batch-2 recipe. ZHAO's CXMT bits are the oldest unconsumed item in this lane. |
| Coverage + hygiene SIGs | LIQUID · HENRY · BOND | LIQUID's PRIMARY funding-microstructure leg is the **#1 network gap** and is open. HENRY/BOND unverified since 7/11. **Resolve at each owner's next launch brief — don't chase.** ⚠️ *PROME writes launch briefs, so PROME's only action here is to include the open leg when it next briefs that desk; it does not chase between briefs and does not own the resolution.* |
| HY >280 X1 watch | intake lane (auto) · LIQUID · BROCK | The lane auto-watches the re-arm and re-kill lines between sessions. **The re-kill is `GATE-HY-REKILL` (`PROME/GATES.tsv`): HY OAS strictly below 260.0 bp on TWO CONSECUTIVE published observations — that row carries the full counting rule (first-published basis, non-publication days, reset condition) and is canonical.** Its live level is **not** kept here — read the dashboard or FRED. Standing restriction is in § Restrictions. |
| Optional / if-requested | — | Dormant-agent cleanup · CREED CMBS/REIT tracker design · TERRY dry run · ORACLE entropy script. Dormant; not obligations. |

---

## Restrictions — standing, binding this session

**Capital and trading**
- Deploy fresh capital **only on a fired trigger**, **$500 per card** (Will 2026-06-26).
- **No auto-trading and no trade execution.** ORACLE measures · TERRY evaluates · Will approves.
- **X1 sizing gate CLOSED — DON'T-SIZE.** The wrapper half is adjudicated NOT ARMED, so no fresh capital absent an X1 or wrapper fire.
- **Position truth is off-repo** (Will/broker direct). `FORGE/STATUS.md` is the mirror, never the truth.
- **Refresh the dashboard or FRED before citing any level.** No level in this file is current by construction.

**Scope and authority**
- **No agent domain edits** unless scoped by Will.
- **No REITS / TRADES / HERMES revival** without Will — revival is a history-restore plus approval, not a launch.
- **No CREED full migration** unless explicitly approved; CREED remains explicit-permission roster.
- **Do not move or delete legacy source archives** unless scoped.

**Process and git**
- **Pathspec commits only.** Never broad add / reset / stash / force-push.
- **Push is auto at closeout** via ff-gated `safe-push.sh`. A non-ff abort is routine; recovery and escalation live in root `CLAUDE.md` Git Protocol and are never restated here.
- **Do not mirror HEARTBEAT's base date or amendment count here** — read HEARTBEAT's own header.
- **Next Best Action is FROZEN** (2026-08-08, Will-ruled): pointer only. Re-enabling it as a live surface is a Will ruling.

---

## Live Surfaces / Ownership

| Surface | Owner / role | Current note |
|---|---|---|
| `AGENTS/CREED/` | National CRE / CMBS + public REIT equity tape | REIT tape absorbed; explicit-permission roster. |
| `AGENTS/TERRY/` | Trade construction | Owns the former TRADES verification playbook and `AGENTS/TERRY/RISK_SCORING.md` (edge, capped Kelly, Brier calibration, execution-block checklist). |
| `AGENTS/ORACLE/PREDICTION_MARKET_METRICS.md` | Prediction-market diagnostics | Entropy, KL bits, entropy-collapse alerts, ORACLE→TERRY packet. |
| `HEARTBEAT.md` (hot) + `PROME/HEARTBEAT_COLD.md` (cold) | Regime read | Base date and amendment count live in HEARTBEAT's own header and are **not** mirrored here. Why that rule exists → `PROME/archive/STATUS_HISTORY.md` §ownership. |
| `PROME/tools/fleet_dashboard.py` → claude.ai artifact | Fleet-Ops dashboard, Will-facing | Generated from canon; points, never owns. Refresh is closeout-wired; URL in the script header. **2026-09-12 (L339): a FAILING build no longer leaves a passing gate** — `PROME/tools/dashboard_build.json` records every non-preview run's outcome (fail-closed before the build), and `prome_gate` refuses a snapshot that is not the latest build's product, on both gate paths, compared on content stamps never mtime. ⚠️ `headline[:60]` at `fleet_dashboard.py:1103` silently severs longer headlines — **three BASE channel headlines are currently severed** (Equity-vol cuts a date mid-token); fold into the HEARTBEAT 15th re-base. |

---

## Completion evidence that a companion surface does not yet reflect

*Narrow notes kept on the read path because they distinguish done work from pending work, and the surface that still lists them as owed cannot show that.*

- **`KERNEL/README.md` L5 was fixed at the 2026-09-11 12:1x session** (recorded in that session's tool-fix list, alongside the `consumer_check` fix and the CalculatedRisk sweep). `HEARTBEAT.md` §KERNEL still lists *"`KERNEL/README.md` L5"* in its **Owed** line — its base is 10:3x, so that entry is **stale, not contradictory**. The other three legs on that line (L247 v0.3 after RED's F1 · WQ-150 root-④ edit · the live-interface adversarial review) carry no owner and are **not** resolved by this note.

---

## History

Session recaps, prior `Updated:` stamps, rotation inventories, spine-audit findings, and the provenance behind the ownership rules → `PROME/archive/STATUS_HISTORY.md`. **Not a boot read** — open it to reconstruct how a state was reached.
