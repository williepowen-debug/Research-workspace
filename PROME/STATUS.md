# PROME STATUS.md
**Updated:** 2026-09-21 — Phase 2 document-state cleanup; selected queue corrections only. Owner grades, market freshness, current broker book and full manifest completeness were not reverified by this maintenance pass.
**Last spine audit:** 2026-09-20 (fourteenth run). Re-run when >7d. Historical findings → `PROME/archive/STATUS_HISTORY.md`; remaining residue at DOCKET L358 and its named sources. The historical WQ-272/full-reconcile wording is superseded: WQ-274 owns transaction/current-book verification.
**Companion reads (this file does not restate them):** continuity → `PROME/HANDOFF.md` · next-session state → `PROME/SCRATCH.md` ★ NEXT · Will's items → `PROME/WILL_QUEUE.md` · catalysts + dates → `PROME/DOCKET.tsv` · fire-ledger → `PROME/GATES.tsv` · regime → `HEARTBEAT.md`.

---

## Current Work Queue — PROME's own actions

Current resume point → [SCRATCH](SCRATCH.md); continuity and unverified older tails → [HANDOFF](HANDOFF.md). Re-check byte flow at any append or on 2026-09-28, whichever first (`scripts/read_cap_check.py --agent PROME --require-manifest`).

**Scope.** This queue highlights **selected PROME operational priorities and follow-ups. It is not an exhaustive task inventory.** Read it alongside the other required boot sources; **DOCKET owns registered dates, GATES owns gate state, and the relevant source artifacts establish completion.** Other desks' work is in § Owner lanes. Written at closeout; every state below was checked at the named source at the observation time given in the column header.

| PROME action | Canonical record | State — each row states its own observation time |
|---|---|---|
| Boot coverage / continuity | `PROME/plans/2026-09-21_boot-coverage-implementation.md` · `PROME/plans/2026-09-21_prose-invalid-date-correction.md` · `PROME/plans/2026-09-21_boot-phase2-continuity.md` | Phase 1 delivered (`fbfe85e36`, `0d104a775`); Phase 2 acceptance lives in its record. Older READS attestation remains unrenewed. Shorter log reads and incremental boot stay deferred. |
| Confirms surviving rotation | DOCKET L438 | DAEDALUS ①② and WALTER RULE 8 confirms remain pending; requires confirms or explicit declines. WQ-250’s archived container does not close these tails. |
| Publication | `PROME/DOCKET.tsv` L393 | Helm/Deck sources + renders regenerated at BOTH 9/17 closeouts; **NOT published** either time — the Deck republish needs a ~100K-token read of the live artifact (L393) and Will's 9/17 cost instruction stands. Hosted versions are the 9/15 vintage. Decided at pre-closeout 16:0x, reported PARTIAL. |
| Completed PROME repairs | `PROME/reports/2026-09-14_L335-ledger-completion.md` · `PROME/reports/2026-09-14_contract-repair-completion.md` | L335 and L394 independently accepted and delivered. Retain the stated historical-data and calibration limits; do not reopen completed code work from older session narratives. |
| Prediction-rule encoding | `PROME/proposals/2026-09-10_wq161-prediction-canon-RULED.md` · DOCKET L395/L400 | Approved bullets encoded; L395 is RESOLVED by its owner record. Its separate residue remains at L400. No further L395 ruling is owed. |
| Spawn/consumer continuity | `PROME/state/ORCH_LOG.tsv` · DOCKET L411/L277/L380/L397 · HANDOFF | Earlier “not spawned” text is historical: L411/L277 are RESOLVED with deliveries, but older consumer-read tails remain unverified. Use fresh native preflight before any launch; old cap counts grant no authority. SHADE’s Tier-2 proximity request still needs Will’s word or a registered qualifying row. |
| 🔴 **WQ-244 hooks — WQ-263's QUESTION CHANGED: the rec on the row does NOT cover the live false positives** | `PROME/tools/hooks/commit_subject_guard.py` + `pipeline_rc_block.py` (`616c8aa7a`) · `PROME/WILL_QUEUE.md` WQ-263 · reader ledgers in the 9/18 session scratchpad, counts on ORCH_LOG | Five Opus reads, 46 ❌ in all, a FALSE POSITIVE in every round (false positives per round 4·5·4·2·5); v6 fixes 12 of the fifth's 13 (`\|&` = recogniser perimeter, DAEDALUS packeted). Rec on the row: pipeline wrapper ADVISORY; subject guard BLOCKING on the `-m` core only, `-F`/heredoc inference ADVISORY. Both stay BLOCKING at v6 until the word. Reach: root hooks do not fire for subdirectory launches (CC #10367). 🆕 **2026-09-18 18:3x — CATO (different model family) found THREE more false positives and PROME REPRODUCED all three on current code:** `command -v git commit -m …`, `env printf %s git commit -m …`, `timeout 1 echo git commit -m …` all BLOCK though none executes git. PROME's controls isolate the mechanism CATO did not state: the guard steps through transparent prefixes (`env`/`timeout`/`command`) to find the command word — correct for `timeout 5 git commit` — but does NOT re-apply the prose test afterwards, so `printf %s git commit -m` correctly ALLOWS while `env printf %s git commit -m` BLOCKS. ⛔ **DECISIVE FOR THE SITTING, and it breaks PROME's earlier recommendation: these are `-m` cases, so the standing rec (wrapper ADVISORY, subject guard BLOCKING on the `-m` core) would keep blocking them.** CATO's repair is right — uncertain command RECOGNITION must sit outside the blocking core too. Cost to state honestly: `env FOO=1 git commit` and `timeout 5 git commit` do run git and would become advisory. ⛔ **PROME's *"not one is a bypass"* is WITHDRAWN as too broad** — the guard's own docstring records four recogniser bypasses found by readers (newline-swallow, `eval`, backticks, ANSI-C). ⚠️ The 104-char subject that landed (`507495a6e`) is the guard's OWN installing commit and is NOT a bypass. R5 also reproduced: three consumers accept `2026-02-30`; the gate correctly records the check as DID NOT RUN / UNKNOWN (CATO conceded this), so the live defect is inconsistent date validation, and no live row is malformed. 18:3x ET. |
| HEARTBEAT maintenance | `HEARTBEAT.md` header · DOCKET L369/L430 | The nineteenth re-base shipped; the header owns its current vintage/chain. Re-check size at any append; no second re-base at the tail of an edit-heavy session. L430’s source/basis and registrar-reconciliation caveats remain at its row and HANDOFF; this cleanup does not grade them. |
| Earlier SCRATCH review-loop evidence | `PROME/state/ORCH_LOG.tsv` scratchrot3–7cold · `PROME/archive/SCRATCH_ROTATED_2026-09-17_prome-b0.md` · `PROME/archive/SCRATCH_ROTATED_2026-09-18_prome-2a.md` | Prior receipt reported an open WQ-165 loop after renderer repairs at `8130dae8d`; retain as unverified historical review debt until its evidence is reconciled. Phase 2’s reader tests the current surface and does not retroactively certify that earlier loop. |
| Interrupted-session recovery | `memory/2026-09-18.md` · `PROME/state/ORCH_LOG.tsv` | Older recovery narratives are in STATUS_HISTORY. At a recovery boot inspect git state and orchestration evidence; idle/committed/clean is not a closeout acknowledgement. Historical UNKNOWN rows remain UNKNOWN. |
| **CODEX orchestration review → L381 (state NOT RUN, dated 9/17)** | DOCKET L381 · `git show 4f361a45a` | WQ-249's genuine addition is narrower than PROME first claimed: not *ask the desks* but *idle + committed + clean cannot establish that you ASKED*. The playbook's wave-approval line goes first and changes NO authority; do not expand into a governance project. Full finding → STATUS_HISTORY 2026-09-18. 12:5x ET. |
| VLO mirror pass completed; transaction evidence still open | DOCKET L424 (RESOLVED) · `PROME/WILL_QUEUE.md` WQ-274 · `AGENTS/TERRY/` owner card | Receipt-mirror pass `2cb4009f3` and standing-snapshot correction `68c688a57` landed; parser sees VLO at `cfd9b9115`. Do not repeat “mirror owed.” Two shares remain STAGED at the owner card; VLO account/fill time and transaction/current-book verification remain unresolved at WQ-274. No new trading instruction. |
| Calibration | `PROME/DOCKET.tsv` L392 | PROME owns the registered observation/calibration follow-up. Completion of the code review does not calibrate its cutoff. |
| **L409 FORGE market-data vintage + fallback repair** | `PROME/DOCKET.tsv` L409 (2026-09-24) | fetch.py fred_fetch returns latest-revised while two gates declare as-first-published; market.py previousClose fallback. WQ-229 consequential class: acceptance conditions first, independent reader before 'fixed'. Not started. |
| **WQ-157 leg ② — carried to Will with BOND's disclosure** | `PROME/WILL_QUEUE.md` WQ-157 (9/19) · DOCKET L271 | Both halves of the pairing instrument measured; neither supports it; the stock-leg inversion (p=0.009) sits at ≈35–40% power for its own effect; the funding leg detected no support (MDE ≈16bp at α=0.01). PROME rec PARK; successor at the 9/19 sitting. PROME grades nothing. |
| Read-cap floor and declaration follow-up | DOCKET L380/L350/L421 · `PROME/registry/READS.tsv` | Existing floor/perimeter issues remain: BRENT/REGINALD permanent-content limits are separate measurements, never a general curve; TERRY append headroom needs its own trigger. BROCK’s newer L421 split receipt does not silently close its pending registrar row. Phase 2 changes PROME continuity only; no fleet remedy, budget change or global re-attestation is implied. |
| **L247 remaining specification/review work** | `PROME/DOCKET.tsv` L247 | F4 is closed. F3 source_masses/normalization and F8 carrier reconciliation remain PROME-owned; RED's F1 v0.3 recheck remains owed. **No code before the required review passes.** Read the docket row for current disposition. |

---

## Owner lanes — not PROME actions

Listed so they are not mistaken for PROME work, and so their standing instructions survive. Each desk owns its own state; PROME does not chase.

| Lane | Owner | Standing instruction |
|---|---|---|
| DEWEY queue drain | DEWEY | Current work = its DOCKET rows. ⛔ Do **not** spawn off the old batch-2 recipe. ZHAO's CXMT bits are the oldest unconsumed item in this lane. |
| Coverage + hygiene SIGs | LIQUID · HENRY · BOND | ★ **RE-SCOPED 2026-09-12 by PROME on LIQUID's recommendation — the PRIMARY funding-microstructure leg is NOT “un-worked”, it is `PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND`.** Grounds LIQUID supplied and PROME accepts: **Form PF's stress-period fields are delayed a FOURTH time to 2027-07-01**, so THESIS v2 leg 3 has **no official instrument before then**; with HY-Energy OAS, TRACE breadth and the ECB's **self-declared** blindness to undrawn commitments, that is **four identical negatives** ⇒ by fleet canon (`finding_declared_data_wall_needs_fleet_memory_check`, which sets the bar at THREE) **the finding is ACCESS, not data.** ⛔ **NOT CLOSED** — LIQUID declined to close it unilaterally and PROME agrees: a supervisor-blind leg with a dated horizon is a live finding about the system, not a discharged task. ⚠ The re-scope changes what the label CLAIMS, not what is known; nothing was measured today that was not measured before. Re-open on any reachable instrument or at 2027-07-01, whichever first. HENRY/BOND unverified since 7/11. **Resolve at each owner's next launch brief — don't chase.** ⚠️ *PROME writes launch briefs, so PROME's only action here is to include the open leg when it next briefs that desk; it does not chase between briefs and does not own the resolution.* |
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

**Standing readings carried from retired rows** (full text → `PROME/archive/STATUS_HISTORY.md` § 2026-09-18)
- **Never date a CLASS** — L386 (roll desync) · L401 (F2 sibling): a dated instance goes quiet exactly before the next occurrence.
- **The push receipt is not the check — verify MEMBERSHIP** (each commit an ancestor of `origin/master`) — DOCKET L378 ⑧; the four failure modes recorded 9/14.
- **HEN-F1 roll hazard:** quote *"one roll is comparable to the whole separation"*, never a two-sig-fig %; treat it as AT LEAST one step (−$4.56) and never as self-cancelling (HENRY's own retraction `4e5d3971c`) — WQ-252 · L386.
- **BOND's TIPS-R I′ line is NOT the spec** — decision at the 10/1 refresh, DOCKET L410 (possible Will ruling).

---

## Live Surfaces / Ownership

| Surface | Owner / role | Current note |
|---|---|---|
| `AGENTS/CREED/` | National CRE / CMBS + public REIT equity tape | REIT tape absorbed; explicit-permission roster. |
| `AGENTS/TERRY/` | Trade construction | Owns the former TRADES verification playbook and `AGENTS/TERRY/RISK_SCORING.md` (edge, capped Kelly, Brier calibration, execution-block checklist). |
| `AGENTS/ORACLE/PREDICTION_MARKET_METRICS.md` | Prediction-market diagnostics | Entropy, KL bits, entropy-collapse alerts, ORACLE→TERRY packet. |
| `HEARTBEAT.md` (hot) + `PROME/HEARTBEAT_COLD.md` (cold) | Regime read | Base date and amendment count live in HEARTBEAT's own header and are **not** mirrored here. Why that rule exists → `PROME/archive/STATUS_HISTORY.md` §ownership. |
| `PROME/tools/fleet_dashboard.py` → claude.ai artifact | Fleet-Ops dashboard, Will-facing | Generated from canon; points, never owns. Refresh is closeout-wired; URL in the script header. **2026-09-12 (L339): a FAILING build no longer leaves a passing gate** — `PROME/tools/dashboard_build.json` records every non-preview run's outcome (fail-closed before the build), and `prome_gate` refuses a snapshot that is not the latest build's product, on both gate paths, compared on content stamps never mtime. ✅ **The three severed BASE headlines are FIXED** — the 15th re-base verified all eight render WHOLE at the 60-character slice, in the built HTML rather than asserted. ⚠️ The `headline[:60]` truncation itself still exists and will sever any future headline over 60 chars silently; it is a live hazard, not a live defect. |

---

## Completion evidence that a companion surface does not yet reflect

*Narrow notes kept on the read path because they distinguish done work from pending work, and the surface that still lists them as owed cannot show that.*

- **`KERNEL/README.md` L5 was fixed at the 2026-09-11 12:1x session** (recorded in that session's tool-fix list, alongside the `consumer_check` fix and the CalculatedRisk sweep). `HEARTBEAT.md` §KERNEL still lists *"`KERNEL/README.md` L5"* in its **Owed** line — its base is 10:3x, so that entry is **stale, not contradictory**. The other three legs on that line (L247 v0.3 after RED's F1 · WQ-150 root-④ edit · the live-interface adversarial review) carry no owner and are **not** resolved by this note.

---

## History

Full pre-cleanup STATUS → [Phase 2 source snapshot — 2026-09-21](archive/STATUS_HISTORY.md#phase-2-source-snapshot--2026-09-21).

Session recaps, prior `Updated:` stamps, rotation inventories, spine-audit findings, and the provenance behind the ownership rules → `PROME/archive/STATUS_HISTORY.md`. **Retired at the 2026-09-13 stamp (all ✅ DONE and recorded elsewhere, dropped to keep this file under its flow-rule line): the COT-35B consumer read · the BG-02 re-grade consumer read · the `PROME/inbox/` backlog sweep** — all three are in the 2026-09-12 `HANDOFF.md` entry and on their own GATES/DOCKET rows; `git log -p -- PROME/STATUS.md` has the verbatim rows. **Not a boot read** — open it to reconstruct how a state was reached. **Rotated at the 2026-09-18 12:5x stamp (`prome-0e`): 13 rows (10 DONE/historical/superseded + 3 standing-reading rows now pointed from § Restrictions) + the prior Updated line → `PROME/archive/STATUS_HISTORY.md` § 2026-09-18 (crc32 in that section's header, verbatim; the recompute command is there).**
