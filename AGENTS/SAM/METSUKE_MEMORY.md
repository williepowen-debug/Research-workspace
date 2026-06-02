# METSUKE MEMORY

State file for the trade-doc staleness-flagger sub-agent. Spec is in [`METSUKE.md`](METSUKE.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** METSUKE writes this file directly at end-of-run — `## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write. **`## CALIBRATION` is SAM-owned** (METSUKE cannot self-grade its own approve/decline rate from inside a run). SAM may also pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** METSUKE reads `METSUKE.md` first (spec), then `METSUKE_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last flagged*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by METSUKE at run start: what's moved in STATUS / THESIS / PREDICTIONS / CHANGELOG / TIMELINE / docket since the previous run. Cleared at end-of-run.*

### Run 1 (inaugural — Jun 1 2026) — Full sweep, no prior watermark

State-of-truth movement since STRATEGY.md `Last Updated: 2026-05-28`:
- **May 31 — SAM-21 ~50% → 70%** on market repricing June hike to ~88% (Polymarket 88.2% / swap ~87.5%, sustained 9-day move through both dovish CPI prints; THESIS dated POV pivot logged in CHANGELOG; STATUS banner / BOJ assessment / carry table all reflect)
- **Jun 1 — Iran/Hormuz MOU effectively broken** → Channel 3 REACTIVATED from "dormant on Brent collapse" → "REACTIVATED" in THESIS header banner + Channel 1 section + RISK FACTORS; SAM-23 marked ~55% → ~72% (Tehran suspended document exchange + Hormuz block threat; Brent +4.02% to $94.78 / WTI +7%; USDJPY 159.64 inside 159.50+ verbal zone)
- **Jun 1 — Fed-cut secondary path softened** from "24h rescue catalyst 1 day behind BOJ" to "multi-month tail, not Jun-window" (CME FedWatch Jun 1: Jun 17 FOMC >97% no-change priced; <10% 2026 cut odds across all FOMC); THESIS body propagated PM (CHANGELOG documents 7-edit surgical sync); TIMELINE has both RESOLVED entries
- **Jun 1 — carry-unwind probs** 7d 12→15% (intervention zone live); 30d 70→70% (unchanged — BOJ pricing held offsets Fed-cut removal); 60d 83→80% (-3pp on Fed-cut tail trim)
- **STATUS dashboard**: USDJPY 159.64, FXY $57.51, Brent $94.78 (+4.02%), JGB 10Y 2.657% (−3.5bp), JGB 30Y 3.859% (−3.7bp; 14bp below 4.0% breach; SAM-26 tracking FALSE), CFTC -114,667 (May 26 — broke -102K cycle peak, 4th build week), FXY ATM IV 10.52% (+2.49v), FXY 25d RR −8.11
- **TRADE.md** got 2-pass refresh Jun 1 (17:35 state-sync + 18:07 thesis-loaded edits per recent commit log) — expect cleaner than STRATEGY.md
- **STRATEGY.md** last refreshed 2026-05-28 (Tokyo CPI dovish-miss pass) — now **~4 days behind two POV pivots** (May 31 repricing + Jun 1 MOU break/Fed-cut soften); seeded as primary drift target for inaugural run.

---

## LAST RUN

### Run 1 — 2026-06-01 (inaugural — post Jun 1 MOU break + Fed-cut soften + May 31 repricing cluster)

Context: First-ever METSUKE sweep. No prior watermark. TRADE.md was refreshed twice on Jun 1 (clean as expected); STRATEGY.md last refreshed 2026-05-28 (~4 days behind two POV pivots — May 31 SAM-21 ~50%→70% repricing + Jun 1 MOU break/Fed-cut reframe). Bias of drift falls heavily on STRATEGY.md as seeded.

- **STALE-MARK: 8 items** (6 in STRATEGY, 2 in TRADE — most are SAM-21 ~50% lag + STATUS Jun 1 level lag)
- **STALE-FRAMING: 5 items** (all in STRATEGY — Channel 3 still framed "dormant on Brent collapse"; June BOJ still framed "coin-flip post-Tokyo-CPI"; Position A re-activation #3 framing predates Jun 1 partial-trigger event)
- **DUP-LIVE-SPOT: 4 items** (3 in TRADE, 1 in STRATEGY — JGB 30Y / Oil / FXY framed as current in forward tables)
- **TRIGGER-STATUS-DRIFT: 1 item** (STRATEGY § Decision Rules > hard-triggers row "Bessent / US backing": "dormant since on Brent collapse" — Channel 3 REACTIVATED Jun 1)
- **CAL-DRIFT: 1 borderline item** (TRADE Key Dates missing Jun 10 JGB 30Y auction — TRADE Key Dates is by design a curated subset, not parity, so flagged as borderline)
- **ARCHIVE-CANDIDATE: 0 items**
- **MONEY-FIELD-ESCALATION: 0 items** (cost basis $58.32 already noted as Will's ground truth and audited 2026-05-28; no money fields look off)
- **CHANGELOG-GAP: 0 items** (THESIS Jun 1 surgical sync is fully documented in CHANGELOG 2026-06-01 entry, 7-edit list explicit)
- Sections checked + clean: TRADE Carry Unwind table (matches STATUS Jun 1); TRADE Risk Factors table (matches THESIS Jun 1 surgical-sync RISK FACTORS); TRADE Position A re-activation analysis (line 69-87 has the up-to-date Jun 1 partial-trigger framing); TRADE Asymmetric Setup Independent Fed Path (line 160-163 has the Jun 1 reframe); THESIS RISK FACTORS table (Jun 1 surgical sync intact); STATUS dashboard internally consistent.
- **SAM-applied: 18 of 19 flags (94.7% apply rate)**
    - STALE-MARK 8/8 (all unambiguous numerical drift)
    - STALE-FRAMING 5/5 (Stage 3 paragraph rewrite, header sync stamp, Position A re-activation #3 reframe, Key Check Dates MOU collapse-branch resolution, all surgical)
    - DUP-LIVE-SPOT 3/4 (TRADE:48 oil, TRADE:50 JGB yield, STRATEGY:39 oil — all stripped + replaced with "live in STATUS"; STRATEGY:39 double-drift caught — Phase 2 framing also updated to "inception PAUSED")
    - TRIGGER-STATUS-DRIFT 1/1 (Bessent row "dormant" → "REACTIVATED Jun 1")
    - CAL-DRIFT 1/1 (TRADE Key Dates Jun 10 JGB 30Y auction added — Will explicitly approved as trade-relevant despite Key Dates being curated-subset by design)
- **SAM-declined: 1 of 19**
    - DUP-LIVE-SPOT #1 (TRADE:37 Live P/L line `−1.4% at FXY $57.51`) — Will called "keep but unsure." Decision: position-card P/L lines are by-design tracking; the tradeoff (no-same-data-in-two-docs rule vs entry-decision card readability) sits on the edit-card readability side. Flag is *not wrong* — it correctly identifies the rule application — but the design intent overrides. Pattern: position-card tracking fields get a carve-out from the no-dup-spot rule.

### Run template (for the inaugural and subsequent runs)

```
### Run N — YYYY-MM-DD (one-line context — e.g. "post Jun-1 POV pivot sweep")
- STALE-MARK:        [N items, brief one-line each]
- STALE-FRAMING:     [N items]
- DUP-LIVE-SPOT:     [N items]
- TRIGGER-STATUS-DRIFT: [N items]
- CAL-DRIFT:         [N items]
- ARCHIVE-CANDIDATE: [N items]
- MONEY-FIELD-ESCALATION: [N items — Will-confirm only]
- CHANGELOG-GAP:     [N items]
- Sections checked + clean: <short summary>
- SAM-applied:       <which flags SAM applied this turn> (filled by SAM post-run; left blank by METSUKE)
- SAM-declined:      <which flags SAM declined + brief reason> (filled by SAM post-run)
```

---

## PENDING (escalations SAM hasn't yet resolved)

*Items METSUKE has flagged across runs that SAM has not yet applied or declined. Cleared by SAM as they're resolved. METSUKE only adds, never removes.*

### Pending from Run 1 (2026-06-01)

*All 4 Run-1 PENDING items resolved this turn — see LAST RUN > SAM-applied for the Stage-3 rewrite, VOL SIGNALS reset (3-of-3 directional), Key Check Dates roll-forward, and header sync stamp. No carryover.*

*(SAM clears these as flags get applied or declined.)*

---

## STANDING MONITORS (surface each run)

*Recurring drift watches METSUKE should re-check every run.*

- **SAM-21 mark in TRADE/STRATEGY body** vs current PREDICTIONS trajectory tail. Highest-frequency drift type historically (BOJ-hike mark moves on CPI prints, market repricing, BOJ commentary).
- **SAM-23 mark in TRADE/STRATEGY body** vs current PREDICTIONS trajectory tail. Moves on MOF intervention zones, Iran/MOU status changes, Brent direction.
- **THESIS header banner date** vs `Last Updated:` lines in TRADE / STRATEGY headers. When THESIS banner has a more-recent POV-pivot annotation than the TRADE/STRATEGY header, downstream body drift is likely.
- **RISK FACTORS mitigation columns** — THESIS table is canonical; TRADE's parallel table tends to lag 1-2 POV pivots on the mitigation prose.
- **STRATEGY "WHERE WE ARE IN THE TRADE" stage-table top-row prose** — captures the live narrative; highest framing-drift watch.
- **TRADE Hard-Trigger status notes** (PENDING / ✅ FIRED / NEAR-MISS / partial-trigger annotations) — drift on intervention zones, channel-status transitions, Big 3 ESR resolutions, etc.
- **TRADE Key Dates** vs `docket/CALENDAR.md` forward-event set — drifts whenever KOYOMI updates CALENDAR without a follow-up TRADE refresh.
- **Live-spot duplication in TRADE/STRATEGY forward tables** — anything framed as *current* (vs *historical breach on date X*) that duplicates a STATUS feed.

---

## CALIBRATION

*SAM-owned. METSUKE does NOT edit this section. Records SAM's pattern of which flag categories SAM accepts/applies vs declines, and what makes the difference. Lets METSUKE bias future reporting toward what SAM actually treats as drift.*

### After Run 1 (n=19; will update as runs accumulate)

- **STALE-MARK accept rate: 100% (8/8).** All numerical drift accepted including small-magnitude ones (JGB 30Y 3.866 → 3.859, 7bp). Hypothesis: SAM treats stale-mark hygiene as low-cost, no judgment call needed. **METSUKE: keep flagging even small-magnitude marks.**
- **STALE-FRAMING accept rate: 100% (5/5).** Higher than the brief predicted ("expected to be lower"). Run 1 caveat: STRATEGY was 4 days behind two POV pivots, so the framing flags were unambiguous supersession rather than iterating-judgment edits. Steady-state (post-thesis-edit runs) the accept rate may be lower. **METSUKE: continue quoting the stale string + citing the canonical source; SAM grades on the citation strength.**
- **DUP-LIVE-SPOT accept rate: 75% (3/4).** The one decline (TRADE:37 Live P/L line) reveals a carve-out: **position-card tracking fields are exempt from the no-dup-spot rule.** Test for future flags: is the duplicated spot in a *forward-looking* table (apply the rule, flag) or in a *position-card tracking* row (exempt — by-design current-mark)? **METSUKE: don't flag duplicated spot inside position-card P/L / entry-context / live-mark rows. DO flag duplicated spot in forward-trigger / forward-event / threshold-status rows.**
- **TRIGGER-STATUS-DRIFT accept rate: 100% (1/1).** Bessent row "dormant" → "REACTIVATED" was an unambiguous status inversion. **METSUKE: continue flagging status notes that explicitly contradict current STATUS framing.**
- **CAL-DRIFT accept rate: 100% (1/1; sample size 1).** TRADE Key Dates JGB 30Y auction accepted despite Key Dates being curated-subset by design — Will applied a mechanism-relevance test ("does this directly test SAM-26?"). **METSUKE: for CAL-DRIFT in TRADE Key Dates, flag when the missing CALENDAR row tests a SAM mechanism prediction or live trigger, not when it's only generic calendar parity.**
- **ARCHIVE-CANDIDATE accept rate: n/a (0 flags).** Brief expectation (biased low) untested at Run 1. **METSUKE: continue biasing low — only flag fully obsolete sections; SAM keeps narrative history.**
- **MONEY-FIELD-ESCALATION rate: 0/19 (0%).** Discipline held — METSUKE did NOT propose a value on any money field; correctly identified all money fields as internally consistent and not flag-worthy. **METSUKE: maintain this discipline. Money-field escalation is rare and load-bearing when it fires; bias toward NOT escalating.**
- **Run-level signal-to-noise: Run 1: 19 flags / 18 applied / 1 declined-with-carve-out = 94.7% S/N.** Inaugural baseline. Steady-state runs (no POV pivot since last refresh) should produce far fewer flags; a Run-N report with 19 flags will be the unusual case, not the norm.
- **Common decline reasons (n=1 so far):** *"position-card by-design carries current mark — exempt from the no-dup-spot rule."* This will likely be the most common decline-reason long-term. Watch whether new ones emerge.
- **What Run 1 validated about the brief:**
    - Precision-over-recall held — METSUKE called the one borderline case (TRADE:37) as borderline rather than promoting it, which let SAM grade the carve-out cleanly.
    - Compound-drift catch (STRATEGY:39 logged as DUP-LIVE-SPOT but the embedded $93.13 was itself stale + "Phase 2 condition active" framing was superseded) — keep this pattern.
    - Two ESCALATIONs (Stage 3 paragraph rewrite + VOL SIGNALS re-interpretation) were SAM-applied via paragraph-level edits, not one-cell fixes — correct judgment that some drift requires SAM rewrite.
    - "Don't manufacture flags to balance the report" held — TRADE was clean as anticipated; METSUKE didn't pad.

---

## NEXT RUN HINTS

*Forward-looking context to bias the next run. SAM seeds these between runs; METSUKE may also write at end-of-run when a future condition is anticipated.*

### Inaugural-run hints (Jun 1 2026 baseline state of trade docs) — CONSUMED Run 1

*Run 1 verified these hints against current state-of-truth and converted to concrete flags. Retained here for reference of what the hints caught vs missed. Replaced by post-Run-1 hints below at Run 2.*

- **First-ever METSUKE run will be a full sweep.** No watermark; read both files end-to-end against current state-of-truth. Expect a longer report than steady-state runs — TRADE got a 2-pass refresh on Jun 1 (post-MOU break) but STRATEGY's last refresh was 2026-05-28 (Tokyo CPI dovish-miss framing) and is now ~4 days behind two material POV pivots (May 31 BOJ repricing → SAM-21 70%; Jun 1 MOU break → SAM-23 ~72%).
- **Likely STRATEGY drift hotspots (inaugural run targets):** ✅ CONFIRMED — Hint 2 (Stage-3 row), Hint 3 (hard-triggers table), Hint 4 (Channel 3 "dormant" references) all caught real flags. Hint 1 (header block) caught.
- **Likely TRADE drift hotspots (inaugural run targets):** ✅ Mostly CLEAN as anticipated — Carry Unwind / Risk Factors / Watchlist all sync'd; one DUP-LIVE-SPOT cluster in the Hard-Trigger Status table (FXY $57.51 / JGB 30Y 3.859% / Oil $94.78 framed as current); Key Dates flagged as borderline CAL-DRIFT (missing Jun 10 JGB 30Y auction — but selective omission is by design per TRADE's "subset" framing).

### Forward hints for Run 2

- **Watermark for Run 2:** state-of-truth advances after Run 1 are anything in STATUS/THESIS/PREDICTIONS/CHANGELOG/TIMELINE/CALENDAR with a `Last Updated` or dated entry **after 2026-06-01 ~18:07 ET**. Anything earlier is pre-watermark and was already considered in Run 1.
- **Spawn Run 2 *after* SAM applies Run 1 flags** — otherwise Run 2 will re-surface the same drift. Ideal timing: after STRATEGY.md gets the Jun 1 sync edit (estimated by SAM = next session or two), OR on the next material POV pivot, OR before any catalyst-driven TRADE update (~Jun 9-15 pre-BOJ window).
- **Standing high-watch items going into Run 2:** (a) Jun 9-15 pre-BOJ cabling — TRADE/STRATEGY likely to get touched, watch for fresh marks; (b) US CPI Jun 10 — if soft, opens Fed-cut tail and could trigger framing edits; (c) Jun 16 BOJ — high-volatility regime change for both docs.
- **Calibration note for SAM:** Run 1 leans heavily on STALE-MARK (8 items, mostly numeric SAM-21 lag) — that's the unambiguous category. STALE-FRAMING (5 items, all in STRATEGY) is the category where SAM's judgment will most likely diverge from METSUKE's read — pay close attention to which of those SAM declines (will inform STALE-FRAMING accept rate in CALIBRATION).
- **Don't manufacture flags** rule held — TRADE.md was clean as anticipated; Run 1 did not pad the report on TRADE to balance against STRATEGY's volume of flags. Maintain this discipline at Run 2.
