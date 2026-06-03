# METSUKE MEMORY

State file for the trade-doc staleness-flagger sub-agent. Spec is in [`METSUKE.md`](METSUKE.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** METSUKE writes this file directly at end-of-run — `## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write. **`## CALIBRATION` is SAM-owned** (METSUKE cannot self-grade its own approve/decline rate from inside a run). SAM may also pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** METSUKE reads `METSUKE.md` first (spec), then `METSUKE_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last flagged*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by METSUKE at run start: what's moved in STATUS / THESIS / PREDICTIONS / CHANGELOG / TIMELINE / docket since the previous run. Cleared at end-of-run.*

### Run 2 (Jun 3 2026) — Two material work passes since Run 1 watermark (2026-06-01 ~18:07 ET)

State-of-truth movement (per SAM-provided context + verified against canonical):

**AM Jun 3 — CH-004 close (MEASUREMENT CORRECTION, not POV pivot):**
- THESIS new section `## CARRY-UNWIND PROBABILITY METHOD` added (formula + 5-trigger anchor table + state-dependent residual + CFTC amplifier + overlap discount + calibration anchors)
- STATUS § CARRY UNWIND PROBABILITY refactored — decomposed buckets 14% / 37% / 49% (7d/30d/60d) replace prior 15% / 70% / 80%; framed as "decomposed estimate, not authoritative probability"
- CHANGELOG 2026-06-03 entry — yen-direction conviction HIGH unchanged; no version bump
- STRATEGY header note cross-references THESIS METHOD; STRATEGY body itself does not carry a probability table to update

**PM Jun 3 — 5-file stop-spec harmonization (Will-decided event-cap mode A):**
- STRATEGY Stop loss section restructured into pre/post-Jun-16 table + rationale (pre-event = no mechanical price stop, event-capped by sizing; post-event = exit if BOTH BOJ dovish AND USDJPY 167+/no MOF)
- STATUS lead line, state-of-play, Sep-call decision footer reflect new spec
- TRADE entry card stop row, R:R row, "oil shock dominates" risk-factor row updated
- THESIS POSITION VIEW vehicle line + 2 RISK FACTORS rows updated
- CHANGELOG 2026-06-03 entry documents

**Other state movement:**
- USDJPY 159.64 → 160.03 (first print above hard trigger this cycle, Wed Jun 3 15:29 ET)
- Polymarket BOJ Jun 16 hike: 88.5% → 94.8% (+7pp/24h)
- SAM-21 HELD at 70% with pre-registered mechanical trigger (Jun 9 re-check, mechanical +5pp to 75% if Polymarket ≥90% AND no Takaichi pushback) + honesty caveat (deliberate Takaichi-ceiling discount, NOT 30% hold-view)
- Brent $94.78 → $97.70 (+1.77% Wed, 4th straight up day)
- JGB 10Y 2.657% → 2.577% (-10bp publication-to-publication per STATUS); JGB 30Y 3.859% → 3.810% (-5bp)
- MOF intervention reference data corrected: authoritative MOF aggregate ¥11.73T (Apr 28–May 27) added to STATUS § INTERVENTION STATUS; ~¥10T Reuters/BofA two-op estimate retained as named-op back-out

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

### Run 2 — 2026-06-03 (post CH-004 decomposition + 5-file stop-spec harmonization + Jun 3 USDJPY 160 break)

Context: First post-Run-1 sweep. Two material work passes today touched TRADE/STRATEGY substantially. Run 1 cleared all 4 PENDING items. SAM-provided hypothesis: highest-yield drift on (a) carry unwind tables in TRADE/STRATEGY citing the OLD 15/70/80 marks, (b) "market ~88.5%" parentheticals now ~24h stale (94.8% Jun 3), (c) header date lag in TRADE (still 2026-06-01).

- **STALE-MARK: 6 items** (1 carry-unwind table in TRADE = single highest-signal flag; 4 "market ~88.5%" parentheticals across TRADE/STRATEGY that lag the Jun 3 Polymarket 94.8% print; 1 "11 trading days to Jun 16" countdown in STRATEGY Stage 3 row)
- **STALE-FRAMING: 2 items** (TRADE header `Last Updated: 2026-06-01` — body has Jun-3 Will-decided stop spec inline, header not rolled forward; STRATEGY § Decision Rules subheader "Hard triggers — STATUS UPDATED v1.5 (May 27)" — body has Jun-1 updates applied + Jun-3 stop-spec sync, subheader date drift)
- **DUP-LIVE-SPOT: 0 items** (TRADE/STRATEGY body redirected to STATUS for all live levels in Run 1 sweep; spot-check confirms no regression)
- **TRIGGER-STATUS-DRIFT: 0 items** (Bessent row + MOF #3 row + JGB 30Y row all carry Jun 1 status notes consistent with current STATUS)
- **CAL-DRIFT: 0 items** (TRADE Key Dates includes Jun 10 JGB 30Y auction + Jun 10 US CPI per Run 1 fix; CALENDAR Jun 8 GDP / Jun 19 National CPI / Jun 23/25/30 JGB auctions are not present but those are KOYOMI-tier operational dates and Key Dates is by-design a curated subset — no mechanism-relevance test fires per Run 1 carve-out)
- **ARCHIVE-CANDIDATE: 0 items**
- **MONEY-FIELD-ESCALATION: 0 items** (cost basis $58.32 unchanged from Will's 2026-05-28 ground truth; share count 13; call premium $0.40; stop spec $55.05 post-event AND-trigger all internally consistent)
- **CHANGELOG-GAP: 0 items** (both Jun 3 entries — CH-004 close + stop-spec harmonization — are documented in CHANGELOG with full edit lists)
- Sections checked + clean: TRADE Stop spec row (matches Will-decided Jun 3 event-cap mode A); TRADE Risk Factors all 5 rows (oil-shock + intervention-fails + BOJ-delays + Channel-1-reactivates + Takaichi all match THESIS Jun 3 surgical-sync); STRATEGY Stop loss section pre/post-Jun-16 table (fully synced); STRATEGY Position A re-activation #3 partial-trigger reframe (Run 1 applied, still current); STRATEGY VOL SIGNALS table (framed "Jun 1" historical, leave); TRADE Asymmetric Setup Independent Fed Path (Jun 1 reframe still current — Fed-cut multi-month tail).
- **SAM-applied: 8 of 8 flags (100% apply rate)**
    - STALE-MARK 6/6 (Carry Unwind table refactored to CH-004 decomposition with method pointer + ~10-anchor caveat; 4 "market ~88.5%" → "~94.8% Jun 3 Polymarket" w/ pre-registered trigger context preserved; "11 trading days" → "9 trd days")
    - STALE-FRAMING 2/2 (TRADE header rolled forward to 2026-06-03 with METSUKE Run 2 stamp + Jun 3 work cited; STRATEGY hard-triggers subheader rolled forward to 2026-06-03 with event-cap stop-spec stamp)
    - Pattern win: the 4+2 "market ~88.5%" cluster was indeed one find/replace conceptually but each instance needed bespoke context preservation ("repriced May 31" historical kept; "Polymarket Jun 3 +7pp/24h on USDJPY 160 break" current added). Batched as single STALE-MARK item in NEXT RUN HINTS per METSUKE's note.
- **SAM-declined: 0 of 8**

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

### Pending from Run 2 (2026-06-03)

*Flags surfaced this run. SAM to apply or decline. METSUKE does not remove these — SAM clears.*

1. **STALE-MARK — TRADE Carry Unwind Probability table (lines 138-146, "v1.5 — Jun 1"):** Three buckets cite the pre-CH-004 marks (7d **15%**, 30d **70%**, 60d **80%**) with the prior driver notes. STATUS Jun 3 decomposition: **14% / 37% / 49%** (decomposed estimate; method in THESIS § CARRY-UNWIND PROBABILITY METHOD). The 30d and 60d cells are −33pp / −31pp stale. The driver-note prose also needs the decomposed framing ("BOJ June hike single-driver" → "BOJ surprise = hawkish-tail subset only; decomposed across 5 triggers + state-dependent residual"). **Highest-signal flag this run.**
2. **STALE-MARK — "market ~88.5%" parentheticals (4 instances):** Polymarket BOJ Jun 16 hike now **94.8%** (Jun 3 per STATUS lead; +7pp/24h). Locations:
   - TRADE line 20 (Active Positions Thesis): "Jun 16 at **SAM 70% / market ~88.5%**, repriced May 31"
   - TRADE line 240 (Key Dates Jun 16 row): "SAM-21 70%; market ~88.5%; SAM-24 25bp @85%"
   - TRADE line 186 (EWJ Watchlist): "BOJ hikes to 1.00% (Jun 16 base case — **SAM-21 70%; market ~88.5%** repriced May 31)"
   - TRADE line 224 (Japan Banks Watchlist): same pattern
   - STRATEGY line 36 (Hard-triggers table BOJ row): "PENDING (Jun 16; **SAM-21 70% / market ~88.5%** — repriced May 31)"
   - STRATEGY line 184 (Key Check Dates Jun 16): "Polymarket ~88.5% / swap ~87.5%; SAM 70%"
   - SAM-21 itself is **HELD 70%** (per STATUS state-of-play and BOJ ASSESSMENT) — direction-of-conviction not stale, only the market quote. Per CALIBRATION ("keep flagging even small-magnitude marks"), surfacing as a batch.
3. **STALE-MARK — STRATEGY Stage 3 row top (line 16):** "11 trading days to Jun 16 BOJ" — today is Jun 3 (Wed); STATUS lead reads "BOJ Jun 16 = **9 trd days**." 2-day countdown drift.
4. **STALE-FRAMING — TRADE header `Last Updated:` (line 3):** Reads "2026-06-01 (Jun 1 sync...)" — but TRADE body has the Will-decided Jun-3 stop spec inline at line 33 + line 172 (Risk Factors oil-shock row). Header not rolled forward to capture the Jun-3 stop-spec harmonization. STATUS / STRATEGY / THESIS / CHANGELOG all carry Jun-3 stamps.
5. **STALE-FRAMING — STRATEGY § Decision Rules subheader (line 29):** "Hard triggers — STATUS UPDATED v1.5 (May 27):" — body has Jun-1 Bessent REACTIVATED + JGB 30Y retracement + Jun-3 stop-spec sync applied. Subheader date is 5 weeks stale. Cosmetic but worth a one-line refresh to "STATUS UPDATED v1.5 (Jun 3, post stop-spec harmonization)" or similar.

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

### After Run 2 (cumulative n=27; Run 1 + Run 2)

- **Run 2 apply rate: 100% (8/8).** No declines. Cumulative S/N: 26/27 = 96.3%. Maintains "precision-over-recall" discipline — METSUKE did not pad TRADE flags despite STRATEGY also being clean on framing.
- **Repeated-phrase cluster pattern (NEW from Run 2):** The "market ~88.5%" cluster fired 6 times across TRADE+STRATEGY for what is conceptually one stale fact. METSUKE batched in NEXT RUN HINTS as a future grouping rule. **Going forward: report repeated-phrase clusters as ONE STALE-MARK item with list of locations**, not N separate items. Keeps S/N numerator honest and reduces noise. Applied retroactively this run (counted as 1 multi-instance flag in METSUKE's own report).
- **Apply-pass surgical-preservation pattern (NEW):** When updating a cluster like "market ~88.5%", SAM preserved differentiated context per location: historical narrative ("May 31 repricing happened") kept verbatim; current quote ("Polymarket Jun 3 +7pp/24h on USDJPY 160 break") added with date stamp. Confirms METSUKE's batched-flag approach doesn't reduce SAM's editing precision — SAM still applies per-location nuance.
- **Two-pass-day pattern (NEW):** Run 2 was the first post-Run-1 case where TWO material work passes (AM CH-004 + PM stop-spec) hit the docs in a single day. Both produced drift — METSUKE caught both classes in one sweep. Confirms: spawn METSUKE *after the day's last edit pass*, not after each pass individually, for max-yield single-sweep coverage.
- **TRADE Carry Unwind table-refactor pattern:** The biggest single edit (3-row table contents + driver-note prose + framing line + method pointer) was a contained one-section refactor — METSUKE correctly flagged as STALE-MARK rather than escalation. SAM-applied as a single Edit. Pattern: when a table's contents are stale but its STRUCTURE is sound (same columns, same rows), STALE-MARK is correct even if the change is multi-cell.
- **Header `Last Updated:` rollforward as STALE-FRAMING:** Run 2 caught TRADE header lag (Jun-1 stamp; body had Jun-3 edits). Confirms STANDING MONITOR #3 (THESIS banner vs TRADE/STRATEGY header dates) is high-yield — METSUKE should auto-include this check at run open.

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

### Forward hints for Run 3

- **Watermark for Run 3:** state-of-truth advances after Run 2 are anything in STATUS/THESIS/PREDICTIONS/CHANGELOG/TIMELINE/CALENDAR with a `Last Updated` or dated entry **after 2026-06-03 (Run 2 finish)**. Anything earlier was considered in Run 1 or Run 2.
- **Pattern to watch for Run 3:** The "market ~88.5%" cluster (4 instances across TRADE + 2 in STRATEGY) is a single repeated phrase that drifts in lockstep with Polymarket re-prints. Likely candidate for a sed-style batch refresh by SAM. If SAM applies all 4 as one edit and Polymarket prints again before Run 3 (e.g., Jun 9 re-check at the mechanical trigger), expect the same cluster pattern to re-surface — METSUKE should batch it as one STALE-MARK item with a list of locations, not 4 separate items. *(Adjusts Run 2 reporting in hindsight: the 4 "market ~88.5%" items could have been consolidated to a single batch flag.)*
- **Spawn Run 3 *after* SAM applies Run 2 flags** — ideal timing: after the Jun 9 SAM-21 mechanical-trigger re-check (Polymarket re-print → likely SAM-21 mark move + cascade to TRADE/STRATEGY), OR after US CPI Jun 10 (Fed-side gate, could trigger framing edits), OR before the BOJ Jun 16 pre-cabling window closes (~Jun 13 blackout).
- **Standing high-watch for Run 3:** (a) the Carry Unwind Probability table refactor in TRADE — flagged this run; once applied, check that STATUS decomposition + THESIS METHOD pointer + TRADE table are all narratively consistent (no "double pointer" or framing drift between the three); (b) if Polymarket re-prints Jun 9 and SAM-21 fires the +5pp mechanical trigger to 75%, the cascade will touch many of the same locations flagged this run — expect a fresh STALE-MARK cluster; (c) US CPI Jun 10 hot/soft binary will likely move the Fed-cut tripwire framing — watch THESIS RISK FACTORS BOJ-delays row + TRADE Asymmetric Setup Independent Fed Path paragraph for cascade.
- **Carve-out reminder (per CALIBRATION):** position-card P/L lines in TRADE entry card (line 37) are by-design current-mark — do NOT flag as DUP-LIVE-SPOT. This is the one place where the no-same-data-in-two-docs rule has an exemption.
- **CAL-DRIFT calibration (n=1 baseline):** TRADE Key Dates is curated-subset, not parity. Only flag CAL-DRIFT if a missing CALENDAR row tests a SAM mechanism prediction or live trigger (per Run 1 Will rubric). Generic operational dates (Jun 8 GDP, Jun 19 National CPI, Jun 23/25/30 JGB auctions) failed that test this run — METSUKE correctly did not flag.
