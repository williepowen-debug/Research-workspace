# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-21 ~14:00 ET (post-auction; BOND TIPS read in flight)

## What Just Happened (chronological, 10:54 → 14:00 ET)

### Thread A — Boot from cleared context (10:54 → 11:05)

CC-Prome booted per BOOT.md. While booting, BROCK and REGINALD ran live closeouts in parallel and pushed.

### Thread B — BROCK live closeout absorbed (11:05 → 11:35)

5 commits f47b9a30 → 1310ed42 by ~11:00 ET. Resolved 4 pending-work rows:
- APO Dec hold (thesis vehicle), APO Jun + ARES Jun + HYG Jun let-expire
- FSK Strong Bear classified; no fresh FSK premium (KKR structurally long defense)
- No fresh BIZD/ARCC yet (entry triggers documented)
- WALTER NDFI REQ closed ($128B → $1.4T framework)
- Convergence re-scored 38/50 → 46/60 with 2 new vectors (sponsor-bifurcation + duration-channel)
- LESSONS #16 — execution rails as PROME design problem (flagged to me)

### Thread C — REGINALD live closeout absorbed (same window)

Commit `f91ee9fb` 14 files +775/-341. WAL V2.1 → V2.2:
- B1 fired ($99M life-sci office walk-away), V4 new (Curley resignation), V2 inventory clean
- Bear-medium 30% dominant (Bear-fast 12%); EV $67.98; REG-25 55→75%
- Next critical test: Q2 print late July
- V1 MI3 / FFIEC PDD V1-fast falsifier still owed

### Thread D — PROME state refresh + push (11:30 → 11:35)

Commit `e40e27e5` — SCRATCH full rewrite + STATUS surgical (4 resolved rows collapsed, agent notes refreshed) + HANDOFF appended.

### Thread E — HENRY + VIOLET teams-mode revival (11:35 → 12:55)

Will asked which agents needed reviving beyond SAM. Identified HENRY (34d stale, 3 unintegrated revival packets in inbox, NVDA 5/20 catalyst) and VIOLET (7d stale, NVDA vol read-through pending, R11 analog watch). Will approved spawning both in teams mode.

**Parallel-spawned via Agent tool with `name:` parameter** (HENRY UUID `abf1cd8d4ed725569`, VIOLET UUID `ad7350e8d26f70249`). Both returned strong first-pass verdicts CONVERGENT on Stage-2-late:
- HENRY: macro/structure tape supports thesis; NVDA absorbed cleanly; posture pivot catalyst-anticipation → drift-monitoring
- VIOLET: Stage 2 confirmed, Stage 3 not imminent; R12 SKEW>140 regime terminated; R11 analog clock running (window 5/28-6/02, prior 36%)

VIOLET's 7-trigger Stage 3 watch list canonized: *2 of {VVIX>105, VIX9D>VIX, SKEW>145} same week as 1 of {HY>2.90, CCC>10.00, 10Y>4.75%}*.

**HENRY-VIOLET LIAISON channel opened** (Will-approved). VIOLET sharpened HENRY's hypothesis (R12 termination ≠ R11 weakening; R11 ACTIVATES with lower prior 36%). HENRY integrated VIOLET's correction pre-commit autonomously — LIAISON loop closed without Prome brokering. New finding: ~90min in-session LIAISON resolves shared-canary questions vs cross-session boundary.

**Gap-fill batch sent in parallel** (Will-approved single SendMessage each):
- HENRY (commit `36a8219b`): USD/JPY 159.16 (0.84 from 160 SAM yellow), HEN-27 PCE CONFIRMED (Core 3.20% YoY, "Fed-can't-cut locked"), HEN-28 NOT firing headline (claims 209K), PREDICTIONS.tsv refreshed
- VIOLET (commit `60b2e49c`): KB rename complete (`final_5d_change` correction), STATUS dashboard split into 2 distinct rows, MEMORY METRIC SEMANTICS section. **FRED spot-check found BROCK morning numbers 2 days stale** — HY 286 cited vs FRED 5/20 actual 280 (matches 5/19 close).

### Thread F — WALTER bull-counter calibration signal filed (~12:00)

Will-authorized cross-agent inbox write. `AGENTS/WALTER/inbox/SIG-PROME-WALTER-2026-05-21_bull-counter-weighting-calibration.md`. Asks WALTER to tier-rank SIG-006 (small/mid-cap fwd P/E discount) + SIG-007 (retail-puts-at-SPY-ATH 10/10 analogs) against 4-agent convergence on Stage-2-late. Awaiting WALTER boot.

### Thread G — BOND pre-auction baseline (12:25 → 12:55)

Spawned via Agent tool with `name: "bond"` (UUID `ad32628b028661b70`). Pre-auction baseline at `AGENTS/BOND/PRE_AUCTION_BASELINE_2026-05-21.md` (untracked-by-design).

**Will surfaced sentiment-trajectory framing for grading lens.** 5/19 4.687 → 5/20 rally (TLT $83.91) → 5/21 modest give-back. Held-rally backdrop, not concession-building. Relayed to BOND; he integrated as §2a SENTIMENT-CONTEXT GRADING LENS with 4-cell verdict matrix and operational sizing consequence (weak print on held-rally would surface upsize-question rather than execute half-add silently).

### Thread H — FRED publication-lag fix Phases 1-3 (13:00 → 13:35)

Driven by VIOLET's spot-check finding. Will-approved plan; my defaults executed:

**Phase 1 (commit `ded870e0`):** Citation Convention section added to `FORGE/tools/market-data/README.md` (cite format, per-series cadence). PROME/BOOT.md pointer in Market Data tools description.

**Phase 2 (commit `ded870e0`):** `dashboard.py` patched. New helper `_date_stamp(entry)` returns [M/D] label for FRED entries, empty for yfinance. `print_table` got new "As-of" column (widths [18,20,8,12,10]). `print_compact` inlines [M/D] between value and agent tag. No `fetch.py` changes needed (date already captured on line 276). Verified live: HY OAS 280bps [5/20] matches VIOLET's finding; 10Y 4.67 [5/19] shows FRED is 2 days behind on DGS10 right now; yfinance rows (KRE/APO/Brent) correctly have no stamp.

**Phase 3 (untracked-by-design):** 4 SIG files filed in BROCK, LIQUID, REGINALD, HENRY inboxes notifying of convention. Per-instance Will-authorized cross-agent writes.

**Phase 4 (deferred):** HEARTBEAT propagation post-auction.
**Phase 5 (deferred):** Compliance audit next session.
**STALE auto-flag deferred to v2** — needs per-series frequency tags in config.py to avoid false-positives on weekly publishers.

### Thread I — 1pm auction print + TIPS-vs-nominal CORRECTION (13:00 → 13:50)

Background polled TreasuryDirect for the 1pm reopening PDF (`b1qfwywt9`). Print finally landed as PDF `R_20260521_4.pdf` ~13:36. Critical correction: **the 1pm auction was the 9-Year 8-Month TIPS reopening (CUSIP 91282CPU9, Series A-2036), NOT a nominal 10-Year note reopening.** Treasury's `term` field collapses TIPS and nominal notes under the same label. My pre-auction brief assumed nominal; matrix v1/v2 thresholds don't apply to TIPS demand statistics. Will: 1✅ no matrix-grade post-auction respawn; 2 send BOND TIPS read; 3 reschedule matrix Q4 to next nominal 10Y; 4 stand-down HEARTBEAT-with-matrix-verdict tonight.

**Print data:**
- High Yield 2.169% real; BTC 2.52
- Bidder split: PD 11.13% / Direct 27.51% / Indirect 61.36%
- Issue 5/29; matures 1/15/2036; coupon 1.875%

**Matrix Q4 rescheduled:** BOND determined next nominal 10Y reopening expected **Tuesday June 9 or Wednesday June 10** (Treasury announcement ~June 3-4). His pre-auction baseline + sentiment-context lens are NOT wasted — apply to the June test instead.

**Lesson saved to memory:** `feedback_verify_treasury_security_type.md` — verify securityType / CUSIP family before scheduling matrix tests; Treasury's term-field collapses TIPS and nominal notes; CUSIP family is the quick distinguishing tell (`91282CQ*` nominal vs `91282CP*` TIPS).

### Thread J — BOND TIPS read in flight (~13:40 → ongoing)

BOND mid-write of `AGENTS/BOND/research/TIPS_5_21_READ_2026-05-21.md`. Last transcript line: *"Now I have everything. Let me write the TIPS research note."* Asked for read on real-yield-2.169% context, BTC 2.52 vs TIPS cohort, bidder split interpretation, breakeven inflation read-through (implied ~2.43%), demand cohort signal.

## Current Git State

Local at `ded870e0` after PROME FRED-fix push. BROCK + REGINALD + HENRY + VIOLET all pushed. SAM has 8 uncommitted files (Will-active session). Tree untracked:
- `AGENTS/BOND/PRE_AUCTION_BASELINE_2026-05-21.md` (BOND owns; won't commit since matrix-Q4 deferred — may delete or rename for the June test)
- 4× Phase 3 FRED SIGs in BROCK/LIQUID/REGINALD/HENRY inboxes (recipients commit on next boot)
- WALTER bull-counter signal in WALTER/inbox (WALTER commits on his boot)
- `WILL/share/` (Will's)

## Resolved This Session (off Pending Work)

| Item | Mechanism |
|---|---|
| APO/ARES Jun premium review | BROCK closeout (Dec hold, Jun let-expire) |
| FSK fresh-premium discussion | BROCK closeout (no; KKR structurally long defense) |
| BDC/private-credit decision prompt | BROCK closeout (no fresh entry yet; triggers documented) |
| WAL Q1 10-Q integration | REGINALD V2.2 shipped |
| HENRY revival packet integration | HENRY booted, integrated 3 packets, 19 inbox renames |
| HENRY NVDA 5/20 read-through | HENRY commit `36a8219b` |
| VIOLET R11 / SKEW regime check | VIOLET commit `1608fac2` |
| HENRY-VIOLET LIAISON channel | Opened + auto-converged via VIOLET outbox file |
| HEN-27 March PCE scoring | CONFIRMED (Core 3.20% YoY) — 3wk overdue resolution closed |
| HEN-28 Labor cliff update | Headline NOT firing (claims 209K); shadow series firing via CARL |
| HENRY USD/JPY data hole | Filled (159.16, 0.84 from SAM yellow) |
| VIOLET KB methodology rename | `final_5d_change` correction propagated, MEMORY semantics section |
| FRED publication-lag fix Phases 1-3 | Convention + dashboard patch + 4 agent SIGs |
| BROCK trap-clinching canonization | Done at his close (now folded into HENRY + VIOLET) |
| Matrix Q4 conditional rule resolution | NOT resolvable today — TIPS auction, not nominal. Deferred to ~June 9-10. |

## Next Planned Work

**Now (BOND in flight):**
- BOND TIPS read note completes (~10-20 min from spawn)
- Optional: PROME state refresh after BOND returns (this file is current; STATUS + HANDOFF parallel)

**Live Will-decision carries (remaining):**
- **🔴 FORGE rehab (NEW, Will-flagged via SAM 5/21 ~12:35)** — `AGENTS/SAM/outbox/2026-05-21_to-PROME_sam-position-state-for-forge-rehab.md` documents: FORGE/STATUS Mar 25, PORTFOLIO Feb 19, JOURNAL Feb 27, per-trade folders Mar 17. FXY in FORGE shows wrong position (4 shares @ $59.77; actual is 13 shares + 1 Jun-18 $58C). 6 expired options listed as active (USO 3/27, OWL 4/2, APO 4/17, SOFI 5/1, OZK 5/15, TLT 5/15). Will plans to have PROME do the rehab. **Top next-session item.**
- **SAM Sep-18 $60C × 5-10 contracts** — pending post-CPI cheaper entry. (Tranche 2 ALREADY executed 5/21 at $57.66, 5 shares — was previously listed here as awaiting direction; that was wrong-from-boot; lesson reinforced.)
- **HEARTBEAT.md refresh** — ✅ done this session by CC-Prome (8f3fa922 Path B + 16:25 surgical fix). OpenClaw refresh cadence still owed as design question.
- **WALTER bull-counter calibration** — ✅ WALTER responded 5/21 (`SIG-WALTER-PROME-20260521-bull-counter-tier-rec.md`); both Tier-2 + forced steelman.
- **PROME execution-rails design note** — BROCK LESSONS #16; quiet maintenance window. Especially relevant to 6/18 Jun expiry cluster (WAL/KRE/HYG/APO/AAL/ARES/EGBN/CF).
- **TODAY.md Path B refresh** — drafted this session but not shipped; FORGE finding redirected priority. Catalysts from CALENDAR.md (6/16 FOMC, 6/18 expiry cluster, 5/25 Memorial Day) NOT yet folded.
- **CALENDAR.md** — 3/27 stale; needs own refresh after TODAY.md.
- **OZK STATUS hygiene refresh** — STATUS still pre-roll posture (hygiene, not execution risk).

**Pre-June 9-10 (next nominal 10Y reopening):**
- BOND can re-validate his matrix v2 deployment on the June test
- Will should re-up the matrix-Q4 conditional rule for that date
- WALTER bull-counter response should be integrated by then for honest weight

## Cautions for Next Session

- **🔴 FORGE rehab is the highest-leverage next thread.** Bigger than HEARTBEAT/MEMORY were. Touches multiple agents' position state; needs careful reconciliation against AGENTS/SAM/TRADE.md (just refreshed v1.4), BROCK position-decisions (5/21 closeout), RED's processed Fidelity CSV, and reality-check against the 6/18 expiry cluster which is 28 days out.
- **Workflow gap detected.** SAM's PROME-bound signal lived in `AGENTS/SAM/outbox/` not `AGENTS/PROME/inbox/`. File-based routing depends on sender placing in receiver's inbox; outbox-resident signals don't trigger PROME attention. Per `project_messaging_overhaul` memory the file system is being replaced, but in the interim: **boot procedure should scan agent outboxes for PROME-targeted signals**, not just PROME/inbox.
- **The Tranche 2 wrong-from-boot finding is exactly the methodology lesson we just saved to MEMORY** (`Stamp content as well as metadata` — verify against current state, don't propagate from inherited STATUS/SCRATCH narrative). Even with the lesson explicit, I propagated it again this same session. Reinforces the value of cross-agent verification at boot.
- **BOND's pre-auction baseline file** untracked — repurpose-or-delete decision for the June 9-10 test. BOND owns.
- **HEARTBEAT staleness compounding.** Now has 4 days of tape + BROCK 46/60 convergence + REGINALD V2.2 + HENRY/VIOLET Stage-2-late + FRED convention adoption owed. Best window for refresh is when Will has time to review the diff.
- **TIPS-vs-nominal lesson saved to memory** — apply before any future matrix-test scheduling around Treasury auctions.
- **SendMessage UUID-only post-first-turn.** Named-spawn `name:` handle drops; only the UUID stays addressable. Saved to `feedback_named_spawn_teams_mode.md` as new bullets 6-7.
- **Do not spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. BOND/HENRY/VIOLET all OK in teams mode (currently standing by).
- **OZK STATUS still pre-roll posture** (hygiene, not execution risk).

## Live Carry: Posterior Shifts Tracked This Session

| Item | Pre-session view | Current view |
|---|---|---|
| 4-agent thesis convergence | Implicit | **Explicitly aligned (BROCK + REGINALD + HENRY + VIOLET on Stage-2-late)** |
| HY OAS cushion from kill | 26bps (BROCK morning, FRED-stale 286) | **20bps (actual FRED 5/20 280)** — closer to invalidation |
| R11 trigger #4 (HY >290) distance | 4bps (morning) | **10bps actual** — farther from firing |
| R11 substance trigger #6 (10Y >4.75%) distance | 8bps (HENRY morning, FRED 5/19 close) | **15bps live (BOND pre-auction 4.599)** — farther; tape moved |
| Convergence on R11 imminence | "Trap intensifying, imminent" | "Stage 2-late confirmed; R11 clock running 5/28-6/02 but prior 36%; not imminent" |
| HEN-27 March PCE | OPEN (Apr 30 resolution overdue) | **CONFIRMED** — Core 3.20% YoY ("Fed-can't-cut locked") |
| Today's 1pm auction matrix-Q4 resolution | "Mechanically resolves Q4" | **TIPS not nominal — Q4 deferred to ~June 9-10** |
| FRED data-discipline | Implicit | **Convention canonized + dashboard auto-displays observation date** |
| Execution-rails as Prome design problem | Implicit | **Surfaced via BROCK LESSONS #16 — owed work** |
