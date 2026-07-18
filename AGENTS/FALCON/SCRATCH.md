# FALCON SCRATCH — 2026-07-18 Sat-eve (Kharg-source freeze + gate merge + weekend reads)

**Purpose:** Ephemeral session handoff — read at boot (step 2), rewritten at closeout (step 13). Durable learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Scenario **B 5 / C 30 / D 65 (BASE)** — **UNCHANGED from 7/17** (markets closed, no new escalation tonight) · Convergence **40/50 🔴 all-time high** · Kinetic 🔴 · **Brent 7/17 SETTLE $88.10 [Yahoo BZ=F] = $85×3 session 1 of 3.**

## CHANGES SINCE LAST SESSION
- **GATE-TERRY-006 (Kharg-strand) UNBLOCKED.** Froze the loadings source and — the honest finding — **disqualified it as a numeric trigger.** IMF PortWatch `port2164 export_tanker` exists/pullable but is AIS-based → **~90%+ blind to Iran's dark fleet**, prints literal 0 for whole NORMAL months (Jan/May/Jul all 0). Gate re-anchored on a **corroborator menu**; PortWatch/Kpler = refuting veto only.
- **$85 clock advanced:** 7/17 SETTLED $88.10 (>$85) = **session 1 of 3** (was "zero settles" when I last wrote, because 7/17 was still intraday). Corrected across STATUS + NEXUS_BRIEF.
- **No new PortWatch transit print** — still 7/12 = 10/88 (11%), 6d old. "No print" is the finding.

## WHAT I DID THIS SESSION
- **Built the frozen source spec** `domain/KHARG_LOADINGS_SOURCE.md`: exact recipe (ArcGIS `Daily_Ports_Data` port2164 `export_tanker`), cadence (~5-8d lag), trailing baseline, and the semantic-gap analysis with monthly evidence + Ras Tanura positive control.
- **Built `scripts/kharg_loadings_watch.py`** (clone of transit watcher, INVERTED codes: rc1=nonzero=refutes strand, rc0=quiet=uninformative). Smoke-tested rc1 (late-June detections in trailing-14d).
- **Merged ONE condition** (my Kharg-seizure tripwire + TERRY's flow condition) → corroborator-anchored wording, routed to PROME (`outbox/2026-07-18_to-PROME_...`). Own-outbox note to TERRY confirming the one trigger inversion (`outbox/2026-07-18_to-TERRY_...`). **Did NOT edit GATES.tsv (PROME registers).**
- **Transit read:** ran `hormuz_transit_watch.py` rc0; graded published 7/6-7/12 series as **flat 7-14 "bypass-carries" band** (my registered most-likely); no 7/13+ print.
- **$85 clock:** verified 7/17 settle via BZ=F = $88.10 (session 1); flagged PROME's $87.71 discrepancy (both >$85).
- Logged **KB-FALCON-025/026**; refreshed **NEXUS_BRIEF**; targeted STATUS $85 + Kharg corrections (no re-mark).

### WAVE 2 (Will-selected proposals #1 + #2; #3 FAL-01 scaffold DEFERRED to Monday)
- **BUILT the bypass-integrity gauge** (`scripts/bypass_watch.py` + `domain/BYPASS_INTEGRITY_BASELINE.md`) — first quantitative measure of the shuttle-breakage tell. PortWatch `export_tanker` at Fujairah(port362)+Sohar(port988); trailing-14d **74,593 t/d vs 15,684 floor = HOLDING/HOT** (Fujairah ~2× base, Mar-Jul high). **Bypass ABSORBING, not breaking → premium-not-supply-loss now has a number.** Positive-control passed (hubs 18-26 nonzero days/mo). INVERTED alarm (rc1=collapse). Honest limits: STS-at-anchorage undercount, global-hub attribution → use via conjunction (collapse AND transits-collapsed).
- **RE-SOURCED the Iraq/PMF discriminator** (`domain/IRAQ_PMF_DISCRIMINATOR_REVIEW.md`) — embassy feed confirmed a dead false-quiet channel (34d silent, ordered-departure). New primary = **CTP/ISW Iran Update (daily) + Shafaq**. [as-of CTP 7/15]: **genuinely unfired** — no new kinetic attacks despite six strike nights; militias conditional/deterred amid a US-Iraq disarmament standoff; no Basra threat. Embassy `baghdad_watch.py` demoted to positive-alert backstop.
- Logged **KB-FALCON-027/028**; STATUS Next-Rung Tells #4/#6 + convergence bypass row + header updated; NEXUS_BRIEF refreshed (bypass = premium-vs-supply-loss discriminator for synthesis).

## NEXT SESSION (dated, future-verifiable)
1. **PortWatch 7/13-15 prints** — STILL not published as of Sat 7/18 18:00 ET; re-check Sun 7/19 / next boot. Grade on prints only (<10 deepening · 7-14 bypass-carries · >18 leaking).
2. **$85 clock:** check **Mon 7/20 + Tue 7/21 settles.** If both >$85 → 3-consecutive FIRES Tue 7/21 → oil vector 4→5, D-tell #3 fires. If either <$85 → clock resets. **Pin the canonical Brent settle source** (Yahoo $88.10 vs PROME $87.71).
3. **GATE-TERRY-006:** confirm PROME registered the corroborator-anchored condition (PROPOSED→armable). If Kharg corroborator appears (declaration / Kpler-Vortexa read / Kharg war-risk notice), that's the fire — run `kharg_loadings_watch.py` as the veto cross-check.
4. **FAL-01 window closes Jul 26** (8 days). Watch KHARG (the real tail) — power plants do NOT fire it (Trump forward-dated grid to 7/20-26). RE-DERIVE 70% at re-registration, don't inherit.
5. **[DONE wave 2] Baghdad watch re-sourced** → CTP/ISW + Shafaq. **Monday boot item:** re-point boot step 5b so the Iraq/PMF discriminator reads off CTP Iran Update, not the dead embassy feed (deferred tonight). Add `bypass_watch.py` to boot as step 5b-3 (RED posture, weekly min).
5b. **[DEFERRED to Monday, Will-directed] FAL-01 re-registration scaffold** (proposal #3) — pre-build the from-scratch 70% re-derivation ahead of the Jul 26 window-close. → `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md`.
6. **WSJ hull-count reconcile** (4→8 double-count risk) — resolve with BRENT.
7. **Bab el-Mandeb conditional** — US grid strike → Iran's Houthi request; neither half fired.

## OPEN THREADS / WATCHES
- 🟠→armable **GATE-TERRY-006 Kharg-strand** — corroborator-anchored, PROME to register; PortWatch is veto not trigger
- 🔴 **FAL-01** (Jul 26) — unfired, base strengthened; Kharg is the tail
- 🔴 **$85×3** — 1 of 3 banked (7/17); earliest fire Tue 7/21
- 🔴 PortWatch 7/13-15 prints — overdue, not published
- 🟠 Bab el-Mandeb conditional · WSJ hull double-count · **shuttle/STS bypass integrity — NOW QUANTIFIED (`bypass_watch.py`, HOLDING/HOT)** · **Iraq/PMF re-sourced (CTP+Shafaq, genuinely unfired)**

## PREDICTIONS DUE / DECISIONS PENDING
- **FAL-01 (Jul 26)** — only OPEN row; 70% frozen, re-derive at re-registration. Scoreboard **1C / 0F / 0P / 0V / 1 OPEN.**
- No Will-decision pending (FALCON holds no trade book). GATE-TERRY-006 arming is TERRY/Will's call once PROME registers.

## MAIL STATE (one line per surface)
- Inbox (root): 4 PROME items — Sat packet consumed (executed); 3 prior (denominator ruling, seizure tripwire ask, loadings addendum) all folded into tonight's deliverable. `git mv` to processed at next full inbox pass (not blocking).
- Outbox: **2 written wave-1** (to-PROME source-freeze, to-TERRY merged-condition) + **wave-2 memo** appended/added (bypass gauge + Iraq re-sourcing).
- WALTER lane / BOARD: none new this session.

## PENDING PUSH / GIT
- Committed pathspec `AGENTS/FALCON/` (domain spec, script + state, KB, STATUS, NEXUS_BRIEF, SCRATCH, outbox). Auto-push via `scripts/safe-push.sh`. GATES.tsv NOT touched (route-out to PROME). 4 agents + PROME writing concurrently tonight → strict own-dir pathspec, never `git add -A`.
