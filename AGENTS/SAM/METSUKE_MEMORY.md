# METSUKE MEMORY

State file for the trade-doc staleness-flagger sub-agent. Spec is in [`METSUKE.md`](METSUKE.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** METSUKE writes this file directly at end-of-run — `## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write. **`## CALIBRATION` is SAM-owned** (METSUKE cannot self-grade its own approve/decline rate from inside a run). SAM may also pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** METSUKE reads `METSUKE.md` first (spec), then `METSUKE_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last flagged*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by METSUKE at run start: what's moved in STATUS / THESIS / PREDICTIONS / CHANGELOG / TIMELINE / docket since the previous run. Cleared at end-of-run.*

### Run 4 (Jun 4 2026 — AM) — Two passes since Run 3 watermark (Jun 3 evening v1.5.1 reconciliation)

State-of-truth movement since Run 3:

**Jun 3 evening — v1.5.1 propagation completion (commit 693f4e65):**
- Three-line propagation fix closing the v1.5.1 reconciliation gap: THESIS L318 HENRY cross-agent link updated to Aug-2024-as-conditional-upside-tail framing; STATUS L210 Channel 2 REFERENCE DATA updated to match; STATUS header version stamp v1.5 → v1.5.1.
- No structural change — just the prose reconciliation that should have happened in the Run 3 PM pass but slipped.

**Jun 4 AM — cabling-window news ingest + OS.1 closure + Sato corrections (commit 079e46ca):**
- STATUS STATE OF PLAY rewritten to Jun 4 framing (Bloomberg sources-leak + Ueda Kisaragi-kai speech + Takaichi-as-permission + Polymarket 96.9%).
- STATUS MARKET DATA table refreshed Jun 4 reads: USDJPY 159.92, FXY $57.34, JGB 30Y 3.85% (+3bp), Brent $96.97, Polymarket 96.9% (Tue 87.6 → Wed 94.8 → Thu 96.9 — 3rd sequential build).
- BOJ ASSESSMENT table: 4 new dated rows added (Jun 3 Ueda + Jun 3 Takaichi + Jun 4 Bloomberg + Jun 4 Polymarket build).
- SAM-21 mechanical-trigger status box updated: Polymarket leg met across 3 sequential reads AND Takaichi-pushback pre-condition AFFIRMATIVELY CLOSED. **SAM-21 HELD at 70% per discipline** — pre-blackout cabling is exactly what discipline was set to NOT chase.
- **OS.1 (fiscal-dominance counter-frame) CLOSED** largely-falsified for SAM-21 binary; live as post-June PATH/CEILING story.
- **Sato date correction Jun 16 → Jun 30** across 4 docs (THESIS L182 / L213, STATUS BOJ ASSESSMENT row, CALENDAR L28, CATALYSTS.tsv row 8). Framing also UPGRADED: Nakagawa was an Apr-28 active 1.00% dissenter, so the active hike-dissent bloc drops 3 → 2 (material dovish shift in marginal-vote count for post-June PATH, not just hawk→dove swap).
- CHANGELOG: full 2026-06-04 entry documents all three sub-changes with "what's NOT changing" enumerated. SAM-23 also marked HELD at 72% per Jun-4 mark-DOWN conjunction discipline (Brent direction-leg firing, cumulative not met).

**No movement this pass:** PREDICTIONS (SAM-21 70% / SAM-23 72% / SAM-24 85% / SAM-26 ~25% all unchanged), TIMELINE (no new RESOLVED narrative — STATE OF PLAY captures Jun 4 news instead), position (13 sh + Jun-18 $58C unchanged), stop spec ($55.05 post-event AND-trigger unchanged).

**Predicted Run-4 drift profile (highest-yield categories):**
- **STALE-MARK cluster — Polymarket 94.8% → 96.9% / market quote.** TRADE/STRATEGY carry "market ~94.8%" in 6 locations (the same cluster Run 2 caught at 88.5% → 94.8%; this is the recurring drift pattern in PREDICTIONS-trajectory style).
- **STALE-MARK — STRATEGY Stage 3 "9 trading days to Jun 16 BOJ"** countdown — today is Jun 4, STATUS lead reads 8 trd days.
- **CAL-DRIFT — TRADE Key Dates Sato row (L246): "Jun 16 | Sato joins BOJ board | Hawk→dove swap"** — date wrong AND framing understated per CALENDAR L28 / THESIS L213 / STATUS BOJ-ASSESSMENT row (Jun 30, dissent bloc 3→2, material dovish shift).
- **STALE-FRAMING (low priority) — TRADE header `Last Updated:` (line 3) still reads "2026-06-03 (Jun 3 PM — stop-spec harmonization..."** — body has Jun-4 cabling cross-references implicitly (via market quote ~94.8% reads NOW vs Jun 3); header didn't roll. Same pattern as Run-2 catch. Borderline because no inline Jun-4-specific Will-decided changes hit TRADE body — header roll is more about consistency than information loss.
- **STALE-FRAMING — TRADE Active Positions Thesis blurb (line 20) cites "market ~94.8% — Polymarket Jun 3, +7pp/24h on USDJPY 160 break"** — the market quote is stale AND the "+7pp/24h on USDJPY 160 break" narrative is now Jun-3 history with Jun-4 build adding +2.1pp to 96.9%.
- **Cluster B Aug-2024 demotion confirmation (the Will-flagged focus item):** all 5 sites from Run 3 are properly qualified (TRADE:67 Options "Why options" / TRADE:129 No-call-spreads / TRADE:254-262 Historical Context / TRADE:156-160 Intervention Paradox / STRATEGY:18 Stage 5 / STRATEGY:96 Jun-18 expiry-problem). Cluster B is CLEAN — no straggler.
- **SAM-21 posture cross-check (the Will-flagged focus item):** TRADE/STRATEGY all carry 70% / market ~94.8% framing. None imply "+5pp imminent" or "about to bump" — Run 3 Cluster C rewrite landed clean and the recent updates only need the market quote refreshed (the discipline language is intact).

### Run 3 (Jun 3 2026 — evening) — v1.5 → v1.5.1 narrative reconciliation since Run 2 watermark (Jun 3 PM stop-spec close)

State-of-truth movement since Run 2:

**Jun 3 evening — v1.5.1 narrative reconciliation (THESIS + CHANGELOG only; no STATUS/PREDICTIONS/TIMELINE/docket edits):**
- THESIS bumped v1.5 → **v1.5.1**; header banner extended with v1.5.1 reconciliation annotation.
- Conviction line decomposed from single "HIGH on direction; MEDIUM on near-term timing" → explicit two-line split:
  - **Direction / level: HIGH** (structural over-determination via rate-diff/J-ICS/hedge-ratio/positioning; $60-62 target grounded in structural math)
  - **Near-term timing: MEDIUM** (explicitly cites PREDICTIONS timing-failure cluster: SAM-08/SAM-20/SAM-15/SAM-22/SAM-19; "right but early" = modal failure mode)
- **NEW SECTION** between CORE THESIS and CARRY-UNWIND METHOD: `## STRUCTURAL PILLARS — why long even if Jun 16 disappoints`. Four pillars enumerated (rate-diff multi-decade extreme; J-ICS lifer long-end abandonment domestic; hedge ratio 14-yr low; CFTC at 63.7% cycle peak). Closes with explicit sizing logic: 13 shares = structural-pillar bet, Jun-18 $58C = catalyst-conditional bet.
- Channel 2 prose reconciled with CH-004 METHOD:
  - **Aug-2024-speed demoted from expectation → upside tail.** New explicit framing: *"speed of unwind scales with the catalyst's surprise component, not with the catalyst's existence."* Only hawkish-on-size/path subset triggers; fully-priced hike does NOT unwind.
  - **Intervention paradox softened — both legs empirically falsified.** MOF acts → ~0.20 unwind|fires per CH-003 (not implicit ~0.50). MOF doesn't act → Channel 1 deferred dissolves the "forced" leg.
- One-liner refreshed catalyst-first → structure-first framing; stale "Channel 3 dormant" line removed.
- CHANGELOG: full v1.5.1 entry with what-changed list + why-minor-not-major + what's-NOT-changing list. Explicitly flags: METSUKE Run 3 spawned on the edited surface per the 6/2 PM CALIBRATION lesson.

**No movement this pass:** STATUS / PREDICTIONS / TIMELINE / docket / CALENDAR (all unchanged since Run 2 watermark). Tape didn't move thesis-side; this is prose-coherence only.

**Predicted Run-3 drift profile (highest-yield categories):**
- TRADE/STRATEGY paragraphs still framing "either path → unwind" as one-liner conclusion (Intervention Paradox section) — STALE-FRAMING against the reconciled Channel 2.
- TRADE/STRATEGY Aug-2024 references that read as expectation rather than hawkish-tail outcome.
- Catalyst-first framing in thesis-recap blurbs that bury the structural pillars as footnotes.
- "Conviction HIGH" monolithic framing without the direction/timing decomposition.
- Any leftover `v1.5` version stamps in forward-looking framing context (vs v1.5.1).

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

### Run 3 — 2026-06-03 (evening — post v1.5 → v1.5.1 narrative reconciliation pass; THESIS + CHANGELOG only)

Context: First METSUKE run on a pure prose-coherence pass (no STATUS/PREDICTIONS/TIMELINE/docket movement). The reconciliation reframed Channel 2 (Aug-2024-speed → upside tail; intervention paradox → both legs softened) and promoted the structural pillars to thesis backbone. Drift bias falls heavily on the *framing* of three sections where the v1.4 narrative cargo lives in current voice: TRADE "Intervention Paradox" + Aug-2024-Precedent + thesis-recap blurb, and STRATEGY Conviction line + Aug-2024 stage-table-and-options-rationale references + leftover "Channel 3 dormant on Brent collapse" history-as-current-voice line.

- **STALE-MARK: 0 items** (no numeric drift this pass — STATUS / PREDICTIONS marks unchanged; SAM-21/23/24/26 all aligned; carry-unwind decomposed 14/37/49 already applied at Run 2; Polymarket 94.8% already applied at Run 2)
- **STALE-FRAMING: 7 items** (this is a prose-reconciliation pass — every flag this run is framing drift against the v1.5.1 reconciled THESIS / CHANGELOG; clustered by theme below)
- **DUP-LIVE-SPOT: 0 items**
- **TRIGGER-STATUS-DRIFT: 0 items** (BOJ row, MOF #3 row, JGB 30Y row, Bessent row, ESR row all in sync with current STATUS state-of-play)
- **CAL-DRIFT: 0 items** (TRADE Key Dates unchanged from Run 2; CALENDAR unchanged)
- **ARCHIVE-CANDIDATE: 0 items**
- **MONEY-FIELD-ESCALATION: 0 items** (cost basis $58.32, share count 13, call premium $0.40, stop spec $55.05 post-event AND-trigger all internally consistent and unchanged)
- **CHANGELOG-GAP: 0 items** (v1.5.1 reconciliation fully documented in CHANGELOG with explicit what-changed / why-minor / what-NOT-changing structure)
- **VERSION-STAMP-DRIFT (sub-category of STALE-FRAMING, batched): 2 locations** (TRADE:138 section header `(v1.5 — Jun 3 decomposed)`; STRATEGY:4 thesis line `v1.5 (single-path...)`) — minor cosmetic per spawn note, but worth catching
- Sections checked + clean: TRADE Carry Unwind table (matches STATUS + THESIS METHOD); TRADE Risk Factors all 5 rows (still in sync — mitigation columns reference structural setup intact, which the new pillars formalize but don't contradict); TRADE Hard-Trigger Status table (all 6 rows current); TRADE Position A Sep-$60 section (multi-channel-convergence framing still correct as the original-spec basis); TRADE Watchlist (EWJ/TLT/Japan Banks all v1.5 sync'd); STRATEGY Stop loss pre/post-Jun-16 table (already cites "structural pillars (rate-diff, J-ICS, hedge-ratio, positioning)" in post-event rationale — IN SYNC with new STRUCTURAL PILLARS section, no drift); STRATEGY VOL SIGNALS (live Jun-1 reads, table all 3-of-3 directional); STRATEGY Hard-triggers table (Jun-3 stop-spec stamp applied at Run 2, no further drift); STRATEGY Asymmetry table (lines 192-202 — scenario list works under both v1.5 and v1.5.1 framing).
- **SAM-applied:** [filled by SAM post-run]
- **SAM-declined:** [filled by SAM post-run]

### Run 4 — 2026-06-04 (AM — post Jun-3-evening v1.5.1 propagation completion + Jun-4 AM cabling-window news ingest + OS.1 closure + Sato corrections)

Context: First post-Run-3 sweep. Two material passes since Run 3 watermark — (a) Jun 3 evening 3-line propagation fix (THESIS L318 / STATUS L210 / STATUS header v1.5→v1.5.1); (b) Jun 4 AM major STATUS update with cabling-window news ingest, OS.1 closure, Sato date+framing corrections. Will-flagged focus items: Aug-2024-demotion completeness audit (Cluster B from Run 3) + SAM-21 "held at 70% despite Jun-4 news" posture cross-check + standard sweep.

- **STALE-MARK: 7 items** (6 in Polymarket "market ~94.8%" cluster across TRADE+STRATEGY = recurring drift pattern, batched per CALIBRATION repeated-phrase rule; 1 in STRATEGY Stage 3 "9 trading days" countdown — STATUS now reads 8 trd days)
- **STALE-FRAMING: 2 items** (TRADE header `Last Updated:` 2026-06-03 — body's market quote implicitly references Jun 3; STATUS Jun 4 news cascade didn't propagate; TRADE Active Positions Thesis blurb L20 "+7pp/24h on USDJPY 160 break" is now Jun-3 history, Jun-4 added +2.1pp to 96.9%)
- **DUP-LIVE-SPOT: 0 items** (Run 1 strip + Run 2 re-verify still holding; no regression spot-check across TRADE/STRATEGY forward tables)
- **TRIGGER-STATUS-DRIFT: 0 items** (BOJ row + MOF #3 row + JGB 30Y row + Bessent row + ESR row all in sync with current STATUS; SAM-21 mechanical-trigger status note pattern updated in STATUS but TRADE/STRATEGY hard-trigger tables don't carry the trigger status detail — they carry the parent SAM-21 mark which is just the market-quote cluster)
- **CAL-DRIFT: 1 item** (TRADE Key Dates L246 "Jun 16 | Sato joins BOJ board | Hawk→dove swap" — date drift Jun 16 → Jun 30 AND framing understated; CALENDAR L28 + THESIS L213 + STATUS BOJ-ASSESSMENT row are canonical with "dissent bloc 3→2, material dovish shift in marginal-vote count for post-June PATH/CEILING"; mechanism-relevance test FIRES because Sato date+framing materially affects post-Jun-16 path read which is exactly what TRADE Key Dates is for)
- **ARCHIVE-CANDIDATE: 0 items**
- **MONEY-FIELD-ESCALATION: 0 items** (cost basis $58.32, share count 13, call premium $0.40, stop spec $55.05 post-event AND-trigger all internally consistent and unchanged across passes)
- **CHANGELOG-GAP: 0 items** (Jun 3 evening propagation + Jun 4 cabling-window/OS.1/Sato all documented in CHANGELOG 2026-06-04 entry with explicit "files touched" + "not changing" enumeration)
- **Will-flagged focus item A (Aug-2024 demotion COMPLETENESS) — CLEAN.** Spot-checked all 5 sites from Run 3 Cluster B: TRADE:67 (Options "Why options" item (c) "upside-tail Aug-2024-speed unwind ... conditional on hawkish-of-pricing trigger + positioning amplification at-peak, NOT the base case" ✓); TRADE:129 (No-spreads "Aug-2024-redux conditional on hawkish-of-pricing trigger + at-peak positioning" ✓); TRADE:254-262 (Historical Context section title "speed scales with surprise, not catalyst existence" + v1.5.1 reconciliation paragraph ✓); TRADE:156-160 (Intervention Paradox v1.5.1 reconciliation — full paragraph rewrite landed ✓); STRATEGY:18 (Stage 5 "Aug-2024-speed (hours not days) is the upside-tail path, conditional on hawkish-of-pricing trigger + at-peak positioning ... Base-case speed for a delivered-as-priced 25bp hike is days-to-weeks, not Aug-2024-hours" ✓); STRATEGY:96 (Jun-18 exit-rule expiry-problem "required a hawkish-of-pricing trigger — per CH-004 METHOD, a fully-priced 25bp delivery is unlikely to fire that cascade at all" ✓). One incidental Aug-2024 reference at STRATEGY:76 — "Aug 2024 precedent: USDJPY tagged 161.95 pre-BOJ then reversed to 141 over weeks" — this is a *dated historical-pattern* invocation in the stop-spec rationale (event-cap mode A) supporting the "don't get knocked out pre-event" argument, NOT a base-case-expectation claim. Per CALIBRATION (dated point-in-time observations are legit historical references), LEAVE. One Aug-2024 reference at STRATEGY:129 — "NOT buying call spreads — caps the Aug 2024 tail which IS the asymmetric point" — this is the same TRADE:129 framing in compressed form; "tail" wording is the v1.5.1-correct framing (tail not modal). LEAVE.
- **Will-flagged focus item B (SAM-21 70% posture cross-check) — CLEAN on discipline framing, only the market quote needs the routine cluster refresh.** TRADE Active Positions Thesis blurb L20 ✓ ("SAM held at 70% per pre-registered Jun 9 mechanical trigger and Takaichi-ceiling earned discount" — discipline language intact). STRATEGY HOLD section L56-61 ✓ (no "+5pp imminent" framing; references Jun 9 re-check as forward decision window). STRATEGY hard-trigger table BOJ row L36 ✓ ("SAM-21 held at 70% per pre-registered Jun 9 mechanical trigger"). All 6 cluster sites cite "70% / market ~94.8%" framing — none imply the +5pp move is "about to fire." Only routine cluster refresh needed (market quote 94.8% → 85-95% range or 96.9% as appropriate). No new framing flag.
- Sections checked + clean: TRADE Carry Unwind Probability table (still matches STATUS Jun-3 CH-004 decomposition 14/37/49 unchanged); TRADE Risk Factors all 5 rows (mitigation columns still match THESIS v1.5.1 RISK FACTORS — Sato dovish-shift implication doesn't change Jun-16 binary so risk-row probabilities held); TRADE Hard-Trigger Status table (all 6 rows current); TRADE Position A Sep-$60 section (multi-channel-convergence basis still correct; Jun-1 partial-trigger note still applies; Jun-4 news doesn't add new re-activation evidence); TRADE Asymmetric Setup Independent Fed Path (Jun-1 reframe still correct — Fed-cut multi-month tail unchanged); TRADE Watchlist EWJ + Japan Banks entry triggers carry market ~94.8% (folded into the STALE-MARK cluster); STRATEGY Stop loss pre/post-Jun-16 table (fully synced — Will-decided Jun 3 stop spec stable through Jun 4); STRATEGY VOL SIGNALS table (Jun 1 reads carried as dated historical — IV proxy + RR proxy + P/C table; KB-183 IV proxy calibration warning sits in STATUS not STRATEGY, so STRATEGY's "live IV in STATUS" pointer captures it correctly without restating); STRATEGY Asymmetry table (scenario list works under v1.5.1 framing); STRATEGY § Decision Rules subheader "STATUS UPDATED 2026-06-03" (Jun 3 PM stop-spec stamp; Jun 4 cascade doesn't add to STRATEGY body so subheader holds — borderline could roll to "2026-06-04" for header-date hygiene but no STRATEGY-internal information loss).
- **SAM-applied:** [filled by SAM post-run]
- **SAM-declined:** [filled by SAM post-run]

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

### Pending from Run 3 (2026-06-03 evening)

*Flags surfaced this run. SAM to apply or decline. METSUKE does not remove these — SAM clears.*

**Cluster A — Intervention Paradox legacy framing (THESIS v1.5.1 explicitly softened both legs):**

1. **STALE-FRAMING — TRADE § The Asymmetric Setup > "Intervention Paradox" (lines 154-157):** The entire 4-line subsection is verbatim v1.4 cargo:
   > *"MOF intervenes → sells USD/buys yen → accelerates carry unwind → FXY up. MOF doesn't intervene → yen weakens on oil → forces more repatriation selling of UST → carry unwind anyway → FXY up (delayed). **Both paths lead to the same destination.** The only question is speed."*

   Superseded by THESIS v1.5.1 § Channel 2 "intervention paradox" reconciliation note (THESIS lines 157-160) + CHANGELOG 2026-06-03 v1.5.1 entry §3. Both legs explicitly falsified: MOF-acts → ~0.20 unwind|fires per CH-003 (not implicit ~0.50); MOF-doesn't-act → Channel 1 deferred (3-of-3 Big 3 benign) dissolves the "forced repat" leg. **The case for being long is not the paradox; it is the structural pillars + an asymmetric option on Jun 16** (THESIS L160 verbatim). Requires paragraph-level rewrite — this is exactly the v1.4 narrative cargo the SAM-provided spawn note flagged.

**Cluster B — Aug-2024-speed as expectation rather than upside-tail (THESIS v1.5.1 explicitly demoted):**

2. **STALE-FRAMING — TRADE § Historical Context (lines 249-258):** Section titled "Aug 5, 2024 Precedent" — concludes with *"This can happen again. Position sizing must account for gap risk."* Read in v1.5.1 voice: this frames Aug-2024 speed (3%, VIX 65, Nikkei -12%, hours not days) as the expected outcome, not the upside-tail conditional on hawkish-on-size/path. Superseded by THESIS Channel 2 (v1.5.1) L155: *"Speed of unwind scales with the catalyst's surprise component, not with the catalyst's existence."* Needs a one-line qualifier — e.g. *"This is the upside-tail outcome IF the hawkish-on-size/path subset fires AND positioning amplification is at-peak — current setup matches positioning but the hike is largely priced; not a base-case expectation."*

3. **STALE-FRAMING — TRADE § Options Layer "Why options" (line 67):** *"That's wrong if: (a) BOJ actually hikes (realized vol 2-3x current IV), (b) intervention #3 fires, (c) Aug 2024-style unwind (realized vol 50%+)."* Item (a) implicitly conflates "BOJ hike" with realized-vol expansion; per CH-004 METHOD + v1.5.1 reconciliation, a fully-priced hike (94.8% market) doesn't unwind. (a) should read as "BOJ hawkish-on-size/path surprise" not "BOJ actually hikes." (c) "Aug 2024-style unwind" framed as default-case rather than upside tail.

4. **STALE-FRAMING — TRADE § Options "No call spreads" line (129):** *"the asymmetric tail (Aug 2024 redux) IS the point; capping upside throws away the best scenario"* — Aug-2024-as-base-expectation framing again. Minor (the no-spread *decision* is still correct under v1.5.1, just the rationale wording reads as "Aug-2024 is the modal upside" vs the new "Aug-2024 is conditional on hawkish-tail trigger"). Lowest-priority of this cluster — can probably leave or one-word qualifier ("Aug 2024-style tail").

5. **STALE-FRAMING — STRATEGY § "WHERE WE ARE IN THE TRADE" Stage 5 (line 18):** *"Yen strengthens, carry unwind cascades (Aug 2024 speed precedent: hours not days)"* — Aug-2024-speed as expected post-trigger pattern. Same demotion target as TRADE Historical Context. Add a "(if hawkish-on-size/path)" qualifier or pull the parenthetical entirely; stage table can stay vague on speed.

6. **STALE-FRAMING — STRATEGY § Jun-18 $58 call exit rules (line 96):** *"Historical pattern (Aug 2024) is the BIG move plays out 3-15 days POST-event. The call expires before the cascade."* This is the exit-rules rationale built on Aug-2024 as expected pattern; under v1.5.1 the cascade itself is conditional on hawkish-tail. The exit-discipline behavioral conclusion (sell into pops, don't ride past expiry) is still sound — it's the wording that drifts. Acceptable to leave as-is given the conclusion is correct; flagging because the spawn note explicitly asked for Aug-2024 expectation-vs-tail. Borderline.

**Cluster C — Catalyst-first framing burying structural pillars:**

7. **STALE-FRAMING — TRADE § Active Positions "Thesis (v1.5 single-path)" blurb (line 20):** Reads catalyst-first: *"Structural yen appreciation over next 3-6 months driven by BOJ rate hike (Jun 16 at SAM 70% / market ~94.8%...) and carry unwind (CFTC short -114,667...). Channel 1 demoted... Channel 3 REACTIVATED Jun 1... Channel 2 (carry/BOJ) remains the dominant near-term catalyst, now market-confirmed base case."* No mention of the structural pillars (rate-diff/J-ICS/hedge-ratio/positioning) as the backbone; the entire framing reads as catalyst-dependent. Under v1.5.1 THESIS L17 (one-liner) + new STRUCTURAL PILLARS section, the correct framing leads with structural over-determination and treats Jun 16 as the dominant *catalyst* (not the load-bearing driver). Highest-signal STALE-FRAMING this run because this is the doc-prominent thesis recap that any reader (or returning SAM) hits first. **Suggested rewrite anchor:** *"v1.5.1 single-path catalyst, structural over-determination. Direction/level (HIGH) grounded in rate-diff/J-ICS/hedge-ratio/CFTC-positioning (see THESIS § STRUCTURAL PILLARS); near-term timing (MEDIUM) hinges on Channel 2 (June BOJ Jun 16 — SAM 70% / market ~94.8%). Position survives a Jun 16 disappointment via the structural pillars; Jun-18 $58C is the catalyst-conditional bet."*

**Cluster D — Conviction monolithic framing:**

8. **STALE-FRAMING — STRATEGY header line (line 4):** *"**Conviction:** HIGH on direction; MEDIUM on near-term timing"* — text is technically aligned with THESIS v1.5.1 (correct values) but the framing is monolithic single-line; THESIS v1.5.1 explicitly decomposes into two labeled lines with the **PREDICTIONS timing-failure cluster** cited as the basis for the MEDIUM near-term timing read. Per spawn note ("flag if prose treats HIGH as monolithic"). Suggested fix: split into two bullets matching THESIS conviction-decomposed format, citing the failure cluster (SAM-08/SAM-20/SAM-15/SAM-22/SAM-19) as the basis for MEDIUM. Cosmetic but doc-prominent (one-line header).

**Cluster E — Version-stamp drift (low priority — batched per Run-2 cluster-collapse rule):**

9. **STALE-FRAMING — Version stamp drift v1.5 → v1.5.1 (2 locations, batched):**
   - TRADE:138 section header *"## Carry Unwind Probability (v1.5 — Jun 3 decomposed)"* → should read v1.5.1 since the framing now reflects post-reconciliation hawkish-tail caveat (TRADE:148 *"A fully-priced BOJ hike does NOT unwind; only the hawkish-tail subset…"* — this IS v1.5.1-aligned prose, header version stamp lags).
   - STRATEGY:4 *"**Thesis:** v1.5 (single-path, market-confirmed June BOJ base case)"* → should read v1.5.1 (the qualifier "single-path, market-confirmed" still holds; just the version stamp lags).
   - Low priority; spawn note explicitly called this out as *"minor but worth catching."* Per CALIBRATION repeated-phrase-cluster rule, batched as 1 flag.

**Cluster F — Borderline: STRATEGY "Channel 3 dormant on Brent collapse" in current-voice historical context:**

10. **STALE-FRAMING (borderline) — STRATEGY § Position A "Resolution logged 2026-05-27" paragraph (line 110):** *"Post-Sumitomo (3-of-3 Big 3 ESR window resolved benign), Channel 1 is demoted to deferred structural backstop and **Channel 3 is dormant on Brent collapse**. Structure has narrowed to single-path (June BOJ)."* The sentence opens "**Resolution logged 2026-05-27**" framing it as historical, but speaks in present-tense ("is demoted... is dormant"). At Run 1, TRADE was rewritten with a Jun-1 partial-trigger annotation in line 121's parenthetical, but the May-27 framing paragraph itself wasn't touched. Three options for SAM: (a) leave as-is (paragraph IS historical-resolution capture); (b) change to past-tense ("was dormant"); (c) add a footnote ("Channel 3 has since reactivated Jun 1 — see TRADE.md Position A section for the partial-trigger analysis at line 121"). Spawn note didn't specifically flag this, but the v1.5.1 reconciliation made the entire "dormant" framing structurally archived — surfacing for completeness. Borderline because doc-internal carve-out exists at line 121.

*Total Run-3 flags: 8 distinct STALE-FRAMING items + 1 batched version-stamp cluster (2 locations) + 1 borderline = 10 items across 6 clusters.*

*(SAM clears these as flags get applied or declined.)*

### Pending from Run 4 (2026-06-04 AM)

*Flags surfaced this run. SAM to apply or decline. METSUKE does not remove these — SAM clears.*

**Cluster A — Polymarket market quote drift 94.8% (Jun 3) → 96.9% (Jun 4, 3rd sequential build). Same repeated-phrase cluster pattern Run 2 caught at 88.5%→94.8%; batched per CALIBRATION rule:**

1. **STALE-MARK — "market ~94.8%" parentheticals (6 instances across TRADE + STRATEGY):** Polymarket BOJ Jun 16 hike now **96.9% (Jun 4)** per STATUS lead; 3rd sequential build (Tue 87.6 → Wed 94.8 → Thu 96.9), swap ~86%, Kalshi ~80%. Per STATUS state-of-play, the load-bearing framing is now "**market ~85-95% depending on surface**" (Polymarket 96.9 / swap 86 / Kalshi 80; ~11pp Polymarket-vs-swap gap intact but all moving same direction). Locations:
   - TRADE line 20 (Active Positions Thesis blurb): "BOJ rate hike Jun 16 (SAM 70% / market ~94.8% — Polymarket Jun 3, +7pp/24h on USDJPY 160 break...)" — quote stale; narrative "+7pp/24h on USDJPY 160 break" is Jun-3-specific history (Jun 4 build was +2.1pp to 96.9%, different narrative driver)
   - TRADE line 46 (Hard-Trigger Status BOJ row): "PENDING (Jun 16; **SAM-21 70%; market ~94.8%** — Polymarket Jun 3, +7pp/24h vs Tue 87.6%; SAM-21 held at 70% per pre-registered Jun 9 mechanical trigger)"
   - TRADE line 191 (EWJ Watchlist): "BOJ hikes to 1.00% (Jun 16 base case — **SAM-21 70%; market ~94.8%** Jun 3 Polymarket)"
   - TRADE line 202 (EWJ Status): "WATCHING — BOJ hike Jun 16 is the trigger (SAM-21 70% / market ~94.8% Jun 3 Polymarket)"
   - TRADE line 229 (Japan Banks Watchlist): same pattern "(Jun 16 base case — SAM-21 70%; market ~94.8% Jun 3 Polymarket)"
   - TRADE line 245 (Key Dates Jun 16 row): "BOJ MPM — DOMINANT REMAINING CATALYST (SAM-21 70%; market ~94.8% Jun 3 Polymarket; SAM-24 25bp @85%)"
   - STRATEGY line 36 (hard-triggers BOJ row): "SAM-21 70% / market ~94.8% — Polymarket Jun 3, +7pp/24h on USDJPY 160 break"
   - STRATEGY line 184 (Key Check Dates Jun 16): "Polymarket ~94.8% Jun 3, +7pp/24h on USDJPY 160 break; SAM 70% held per pre-registered Jun 9 trigger"
   - SAM-21 itself **HELD 70%** per STATUS state-of-play (mechanical-trigger discipline: pre-blackout cabling is what the discipline was set to NOT chase; Will elected hold). The 30% / "earned-discount" / "Takaichi-ceiling" framing is unchanged. **Only the market quote needs the routine refresh** — and per the spawn note's Will-focus-item-B, the "held at 70%" posture is the correct framing and should be preserved. Suggested refresh anchor: "SAM 70% / market ~85-95% (Polymarket 96.9% Jun 4 — 3rd sequential build Tue 87.6 → Wed 94.8 → Thu 96.9; swap ~86%, Kalshi ~80%; SAM held at 70% per pre-registered Jun 9 discipline)" or a compressed version with STATUS pointer for the surface decomposition. Per CALIBRATION Run-2 pattern, batch as 1 STALE-MARK flag with 8 locations listed.
   - **Highest-signal flag this run.** Note this is the SAME cluster as Run 2 — every Polymarket re-print between runs surfaces this. Will-side, this is now a recurring 3rd-time-touched edit.

2. **STALE-MARK — STRATEGY Stage 3 row (line 16, end of cell):** "9 trading days to Jun 16 BOJ." Today is Jun 4 (Thu); STATUS lead reads "BOJ Jun 16 = **8 trd days**." 1-day countdown drift (same drift class as Run 2's "11 → 9 trd days" — recurring pattern, applies in real time as Jun 16 approaches).

**Cluster B — Sato date + framing correction (TRADE Key Dates row, the canonical-divergence flag):**

3. **CAL-DRIFT — TRADE Key Dates line 246:** Row reads "Jun 16 | Sato joins BOJ board | Hawk→dove swap; post-June political risk." Both date and framing are stale per the Jun-4 corrections:
   - **Date:** Jun 16 → **Jun 30** (Nakagawa term expires Jun 29; Sato Ayano takes seat Jun 30). Conflated with BOJ Jun-16 MPM.
   - **Framing:** "Hawk→dove swap; post-June political risk" → **"Active hike-dissent bloc drops 3 → 2 (Nakagawa was Apr-28 1.00% dissenter alongside Takata, Tamura). Material dovish shift in marginal-vote count for post-June PATH/CEILING — strengthens v1.5.1 path-MEDIUM conviction; doesn't change Jun-16 binary."**
   - **Canonical:** CALENDAR L28 ("Jun 30 — Sato Ayano takes Nakagawa's seat..."), THESIS L213 (Catalyst Sequence row), STATUS BOJ ASSESSMENT row (post-Jun-16 implication), CHANGELOG 2026-06-04 § (c).
   - Mechanism-relevance test (per Run 1 CAL-DRIFT calibration rule): FIRES — Sato's seat date and the active-dissent-bloc shift materially affects the post-June BOJ PATH read (v1.5.1 path-MEDIUM conviction basis), which is exactly what the Key Dates row should capture. Not a generic operational date.

**Cluster C — Header date / framing roll (low priority — recurring pattern per Run 2 calibration):**

4. **STALE-FRAMING — TRADE header `Last Updated:` (line 3):** Reads "2026-06-03 (Jun 3 PM — stop-spec harmonization..., Polymarket BOJ hike refreshed to 94.8%; Carry Unwind table refactored to CH-004 decomposition. METSUKE Run 2 sync applied.)" — TRADE body's Jun-4 implications are limited (no direct Will-decided changes hit TRADE this pass — the news landed in STATUS), but the Polymarket quote is now Jun-3-stamped while STATUS has rolled to Jun-4-96.9%. Header date hygiene per STANDING MONITOR #3 (THESIS banner vs TRADE/STRATEGY header dates) — borderline because no internal Jun-4 information loss in TRADE body itself, but downstream Polymarket cluster refresh ON THIS RUN will inject Jun-4 references so the header should track. Run-2 calibration: SAM treats header rollforward as STALE-FRAMING when body has a more-recent stamp inline. Low priority but worth a one-line refresh stamp ("2026-06-04 — METSUKE Run 4 sync: Polymarket cluster refreshed to Jun-4 96.9% 3rd sequential build, Sato Key Dates row corrected to Jun 30 + material-dovish-shift framing"). Same flag class as Run 2 caught.

5. **STALE-FRAMING — TRADE Active Positions Thesis blurb (line 20), narrative-tail context:** *"...market ~94.8% — Polymarket Jun 3, +7pp/24h on USDJPY 160 break"* — beyond the cluster refresh, the **"+7pp/24h on USDJPY 160 break"** narrative tail is now Jun-3 history. The Jun-4 read is "+2.1pp to 96.9% on multi-source corroboration (sources-leak + Ueda speech), USDJPY pulled back to 159.92 — third sequential build, not single-print spike." Recommended: roll the narrative tail to capture the Jun-4 multi-source cabling pattern rather than the Jun-3 single-day break. (Could also collapse to "+9pp / 48h" cumulative or just the 3rd-sequential-build framing per STATUS lead. SAM's call on phrasing.) Lower-priority than the cluster refresh because the discipline framing is intact ("SAM held at 70% per pre-registered Jun 9 mechanical trigger and Takaichi-ceiling earned discount") — only the narrative-tail dates need the cascade.

**Notes for SAM:**

- Per the spawn note: **Will-focus-item-A (Aug-2024 demotion completeness) is CLEAN.** All 5 Cluster B sites from Run 3 properly qualified; no straggler. The two incidental references (STRATEGY:76 stop-spec rationale "USDJPY tagged 161.95 pre-BOJ then reversed to 141 over weeks" + STRATEGY:129 no-spreads "Aug 2024 tail") read as legit historical / v1.5.1-correct-tail-framing per CALIBRATION (dated point-in-time observations / "tail" wording matches reconciliation). No flag.
- **Will-focus-item-B (SAM-21 held-at-70% posture) is CLEAN on discipline framing.** All 6+ cluster sites cite "held at 70% per pre-registered Jun 9 mechanical trigger" — none imply +5pp imminent. Only the market quote needs cluster refresh (which is flag #1).
- **Cluster A (market quote) is now the 3rd-time-touched recurring cluster** (Run 1 surfaced 88.5%, Run 2 refreshed to 94.8%, Run 4 needs 96.9% — and SAM-21 mechanical trigger Jun 9 will likely fire +5pp to 75% even if Polymarket holds, so Run 5 will likely hit it again). Per Run-2 CALIBRATION the apply-pass should preserve differentiated context per location (historical narrative kept verbatim; current quote added with date stamp).

*Total Run-4 flags: 5 items across 3 clusters (1 batched STALE-MARK cluster with 8 locations + 1 single STALE-MARK + 1 CAL-DRIFT + 2 STALE-FRAMING).*

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
- **NEW (post Run 3):** Conviction-decomposition consistency. THESIS v1.5.1 decomposed Conviction into explicit Direction/level (HIGH, structural) vs Near-term timing (MEDIUM, cites PREDICTIONS failure cluster). Watch TRADE/STRATEGY header / thesis-recap blurbs for monolithic "Conviction HIGH" or "HIGH on direction; MEDIUM on near-term timing" single-line framing without the structural-pillars-and-failure-cluster basis. Cosmetic but doc-prominent.
- **NEW (post Run 3):** Aug-2024-speed framing — expectation vs upside-tail. Any TRADE/STRATEGY reference to Aug 2024 (hours-not-days, VIX 65, 3% one-day, "BIG move plays out 3-15 days POST-event," etc.) framed as base-case expectation rather than upside-tail conditional on hawkish-on-size/path trigger is STALE per THESIS v1.5.1 Channel 2 reconciliation: *"speed of unwind scales with the catalyst's surprise component, not with the catalyst's existence."*
- **NEW (post Run 3):** Intervention-paradox "either path → unwind / both paths same destination" framing — explicitly falsified in THESIS v1.5.1; both legs softened (MOF acts → ~0.20 unwind|fires per CH-003; MOF doesn't act → Channel 1 deferred dissolves the forced-repat leg). Watch for the legacy one-liner conclusion *"Both paths lead to the same destination. The only question is speed."*
- **NEW (post Run 3):** Catalyst-first vs structure-first framing in thesis-recap blurbs. Any TRADE/STRATEGY top-of-section thesis recap that frames the position as "driven by BOJ rate hike + carry unwind" without naming the structural pillars (rate-diff / J-ICS / hedge-ratio / CFTC positioning) as the backbone is buried-pillars STALE-FRAMING per THESIS v1.5.1 STRUCTURAL PILLARS section. The new doc-native voice leads with structure and treats Jun 16 as the dominant *catalyst*, not the load-bearing driver.
- **NEW (post Run 4):** Polymarket market quote cluster — recurring cluster-refresh drift, now 3rd-time-touched (88.5% → 94.8% → 96.9%). Pre-blackout cabling drives near-daily print evolution; cluster will recur every run between now and BOJ Jun 16 unless SAM converts the cluster sites to "market ~85-95% depending on surface (live in STATUS)" framing that doesn't carry a specific Polymarket number inline. Strong candidate for **structural fix in Run 5** (convert 8 cluster sites to STATUS-pointer once, eliminate the recurring touch).
- **NEW (post Run 4):** Sato date / framing across docs. Spawn-note context confirms a Jun-4 correction cascade hit 4 docs (THESIS / STATUS / CALENDAR / CATALYSTS.tsv); TRADE Key Dates row was missed. **Future Sato references in TRADE/STRATEGY should track CALENDAR canonical row (Jun 30, dissent bloc 3 → 2 dovish shift) — flag any Jun-16-Sato or "hawk→dove swap" framing as STALE.** Monitor each run until both TRADE and STRATEGY are clean on Sato (STRATEGY doesn't currently reference Sato directly; TRADE Key Dates is the only known site).
- **NEW (post Run 4):** Trade-day countdown to Jun 16 — STRATEGY Stage 3 carries the explicit countdown number which decays daily. Was caught Run 2 (11 → 9), Run 4 (9 → 8), now Run 5 (8 → 5; +3-day drift this run because Jun 5-9 weekend + Mon-Tue both lapped). Recurring drift class. Could be eliminated by removing the explicit number ("8 trading days") in favor of "T-X to Jun 16 BOJ" with X live-pulled from STATUS — but that requires SAM's call on whether the number is load-bearing (a near-term framing anchor) vs cosmetic. At Run 5, only 5 trading days remain to Jun 16, so the cluster sunsets at Jun-16 binary resolve.
- **NEW (post Run 5; numbers corrected Jun 9 PM):** Brent direction-tense drift. Brent has flipped direction TWICE in 8 days (Jun 1 +4% MOU-break re-accelerate → Jun 4-9 choppy down-drift, −4.5% cum from Jun-3 baseline with a Mon Jun 8 UP session and a Tue intraday $89.59 tag that didn't hold — NOT a monotonic collapse; driver China demand + Trump-Iran walk-back rumors). TRADE Risk Factors oil-shock row + EWJ Watchlist anti-triggers both carry directional tense ("re-accelerating", "no longer active") that becomes load-bearing-stale on each flip. Watch on every run as long as Iran/Hormuz remains unresolved. **Corollary from the Jun-9 correction cycle: verify session-count/breach claims against settled OHLC before proposing refresh text — METSUKE's Run-5 Cluster B carried a midday breach mis-read into TRADE/STRATEGY that SAM had to re-correct same evening.**
- **NEW (post Run 5):** CFTC level + cycle-peak-percentage drift. Same surfaces as the Polymarket / SAM-21 cluster (TRADE thesis blurb + Options "Why options"). Weekly release every Sat; will recur at Run 6+ (Sat Jun 13 release is the last pre-blackout). Run-5 saw 63.7%/-114,667 → 72.0%/-129,567 over two prints. Cluster as STALE-MARK batched per CALIBRATION rule.
- **NEW (post Run 5):** Post-fire SAM-21 cluster recurrence. Cluster A (Run 5) caught the 70%→75% post-fire cascade across 10 surfaces. The remaining cascade window to Jun 16 is 5 trading days; SAM-21 won't move mechanically again pre-meeting unless something material reverses, so Cluster A is a one-touch refresh, not the recurring class. Jun 16 binary resolves the SAM-21 surface entirely.

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

### Forward hints for Run 4

- **Watermark for Run 4:** state-of-truth advances after Run 3 are anything in STATUS/THESIS/PREDICTIONS/CHANGELOG/TIMELINE/CALENDAR with a `Last Updated` or dated entry **after 2026-06-03 evening (Run 3 finish, post v1.5.1 reconciliation)**. Earlier was considered Run 1/2/3.
- **Pattern to watch for Run 4 (Aug-2024-framing cluster):** Run 3 surfaced 4 distinct Aug-2024-as-expectation references (TRADE Historical Context, TRADE Options "Why options" (c), TRADE Options "no spreads" rationale, STRATEGY Stage 5, STRATEGY Jun-18 exit rules rationale) — if SAM applies all by qualifier-insertion ("upside tail IF hawkish-on-size/path"), check Run 4 that no NEW references slipped in if a fresh Aug-2024 outbox to HENRY/LIQUID gets drafted. Standing monitor #9-11 added (Aug-2024 expectation-vs-tail; intervention-paradox legacy; catalyst-first burying pillars).
- **Spawn Run 4 *after* SAM applies Run 3 flags** — ideal timing: after the Jun 9 SAM-21 mechanical-trigger re-check (which will cascade marks even if Polymarket holds at 94.8%; SAM-21 mark move + structural language refresh likely), OR after US CPI Jun 10 binary (Fed-side gate — soft print opens Fed-cut multi-month tail framing edit), OR before BOJ Jun 16 pre-meeting blackout (~Jun 13 T-2). One-pass Run 4 covering all three is ideal if no major intra-week reframe fires.
- **Catalyst-conditional framing watch (NEW post Run 3):** If Run 3 cluster C (TRADE thesis-recap) gets applied with the structural-pillars-led rewrite, check Run 4 that the cascade goes downstream — STRATEGY's "When to HOLD" section (line 56-61) and "When to EXIT" section (line 63+) may have the same buried-pillars pattern. Run 3 didn't flag those because the spawn-note targeting was specifically thesis-recap-blurb-level, but if structural-pillars-first becomes the doc-native voice, the HOLD/EXIT prose may need the same refresh.
- **Version-stamp drift hygiene (NEW post Run 3):** v1.5.1 will likely be followed by v1.5.2, v1.5.3, etc. as POV-pivots accumulate. The 2 locations flagged this run (TRADE:138 header, STRATEGY:4 thesis line) plus the TRADE:3 / STRATEGY:3 `Last Updated:` headers are the standing version-stamp surface — once a version bumps, sweep all four locations as one batch. Add to STANDING MONITORS if pattern recurs at Run 4.
- **Conviction decomposition cascade:** If SAM applies Cluster D (STRATEGY:4 conviction line split), check Run 4 that any cross-references to "HIGH on direction; MEDIUM on near-term timing" elsewhere in STRATEGY/TRADE pick up the new decomposition basis. Likely candidates: TRADE Position card "Thesis" subsection, TRADE Risk Factors mitigation columns, STRATEGY "When to HOLD" rationale.
- **Pure-prose-pass pattern (NEW from Run 3 — calibration anchor):** Run 3 was the first METSUKE sweep on a prose-only pass (no STATUS / PREDICTIONS movement). Result: 0 STALE-MARK / 7 STALE-FRAMING / 0 anything-else. Confirms the read that **STALE-FRAMING is the dominant category when the reconciliation is narrative-coherence rather than data-refresh**. Future SAM should expect Run-N reports with this profile to be predominantly STATE-FRAMING when the trigger is a CHANGELOG entry without a STATUS-level cascade.

### Forward hints for Run 5

- **Watermark for Run 5:** state-of-truth advances after Run 4 are anything in STATUS/THESIS/PREDICTIONS/CHANGELOG/TIMELINE/CALENDAR with a `Last Updated` or dated entry **after 2026-06-04 AM (Run 4 finish)**. Earlier was considered Run 1/2/3/4.
- **Polymarket cluster — structural-fix candidate for Run 5:** The cluster has now been touched 3 times (88.5% → 94.8% → 96.9%). Pre-blackout cabling between Run 4 and Run 5 will likely produce another print (Sat Jun 6 CFTC alone could move the read; daily polymarket prints continue). **Strong candidate for one-time structural fix:** convert the 8 cluster sites to a STATUS-pointer ("market ~85-95% across surfaces — see STATUS for live Polymarket / swap / Kalshi") that no longer carries a specific number inline. Eliminates the recurring 1-2-flags-per-run touch from then through Jun 16. SAM's call — preserving the explicit number serves the "Polymarket-vs-swap gap" narrative and the +7pp/24h on USDJPY-160-break narrative anchor, both of which are real information. If SAM keeps the explicit number, Run 5 will hit the cluster again. If SAM converts to pointer, the cluster disappears.
- **SAM-21 mechanical trigger Jun 9 outcome:** Pre-registered re-check Tue Jun 9. Per Jun 4 STATUS, Polymarket leg is now met (96.9%) AND Takaichi-pushback leg affirmatively closed (Jun 3 verbal = intervention-permission). Default discipline path is +5pp to SAM-21 75% on Jun 9 unless something material reverses (Polymarket regression below 90% across 3 sequential reads, Takaichi cabinet pushback, JGB long-end disorderly move). If SAM-21 fires to 75%, the cascade will hit TRADE/STRATEGY in ~4-6 locations parallel to the market-quote cluster — Run 5 timing ideally lands AFTER the Jun 9 re-check and TRADE/STRATEGY apply pass.
- **US CPI Jun 10 binary:** Hot/soft will likely move the Fed-side mitigation framing in TRADE Asymmetric Setup Independent Fed Path paragraph + STRATEGY HOLD section Fed-cut tripwire reference. If soft surprise, Fed-cut multi-month-tail framing tightens; if hot, holds. Run 5 should check Fed-cut-tail framing post-Jun-10.
- **JGB 30Y auction Jun 10:** BTC <2.5x or wide tail = J-ICS mechanism re-lights SAM-26; auction result will cascade to STATUS first then TRADE/STRATEGY Risk Factors framings. Run 5 should check JGB 30Y row + SAM-26 references if auction prints weak.
- **Spawn Run 5 timing:** ideal — after Jun 9 SAM-21 re-check + TRADE/STRATEGY apply pass, OR after Jun 10 US CPI + JGB 30Y auction. Combine into one Run 5 if no intra-week reframe fires; split if SAM-21 fires mechanically Jun 9 + new framing edits cascade.
- **Sato Key Dates row** — flagged this run; once applied, monitor next run that no other TRADE/STRATEGY Sato references remain (none currently known; if a fresh Sato outbox or watchlist note gets drafted between runs, watch it).
- **Header rollforward** — Run-2 and Run-4 both caught TRADE header lag; this is a recurring drift. Future SAM may want to add an explicit "roll TRADE header on any STATUS-Jun-X update that downstream cluster-refreshes TRADE body" rule, or accept the once-per-run touch as friction.
- **No structural reframes expected pre-Jun-16** unless a hard catalyst surprises (BOJ leak revises path, MOF #3 fires, oil shock, Tehran formal withdrawal). Base case for Runs 5+: continued Polymarket cluster drift + countdown drift + occasional small marks; STATUS-level news ingest continues but THESIS v1.5.1 framing is stable until Jun 16 binary resolves.

### Forward hints for Run 6

- **Watermark for Run 6:** state-of-truth advances after Run 5 are anything in STATUS/THESIS/PREDICTIONS/CHANGELOG/TIMELINE/CALENDAR dated **after 2026-06-09 ~12:35 PM ET (Run 5 finish)**.
- **Spawn Run 6 timing:** ideal — after the Jun 10 US CPI + JGB 30Y auction TRADE/STRATEGY apply pass, OR after the Sat Jun 13 last-pre-blackout CFTC print + TRADE/STRATEGY apply, OR before Jun 16 BOJ (pre-meeting blackout starts ~Jun 13, T-2). One Run 6 covering all three reads pre-Jun-16 is ideal; otherwise split if a fresh framing edit cascades.
- **Cluster A (SAM-21) is one-touch this run** — won't recur pre-Jun-16 unless something material reverses (Polymarket regression below 90% across 3 sequential reads, Takaichi cabinet pushback, JGB long-end disorderly move). Post Jun-16 binary, SAM-21 either resolves CONFIRMED (hike delivered) or FAILED (no hike) — Cluster A sunsets either way.
- **Cluster B (Brent direction) likely to recur** — Iran/Hormuz status not formally resolved; Trump-Iran walk-back rumors not yet primary-source confirmed; Brent below $90 could reverse on a Tehran rhetorical re-escalation OR continue down on China demand confirmation. TRADE oil-shock Risk row + EWJ anti-trigger remain the recurring drift surfaces.
- **Cluster C (CFTC level) recurs Sat Jun 13** — last pre-blackout CFTC print. Watch for 85%/-153K danger-zone breach (METHOD amplifier escalates to +8-10pp); flag the TRADE thesis-blurb + Options "Why options" CFTC surfaces.
- **Trading-day countdown** — STRATEGY Stage 3 row "5 trd days" decays to 4 / 3 / 2 / 1 across Run 6+. Cluster sunsets at Jun 16.
- **Money-field discipline check:** Will-confirm only on TRADE L37 Live P/L — METSUKE proposes no value. If Will refreshes the position-card P/L by hand, Run 6 should confirm the row matches Will's ground truth at that mark; otherwise leave as-is per money-field carve-out.
- **Post-Jun-16 binary cascade (Run 7+ hint):** When BOJ Jun 16 resolves, the cascade will hit virtually every section — SAM-21 resolves CONFIRMED/FAILED in PREDICTIONS; THESIS v1.5.1 bumps to v1.6 (or v1.5.2 depending on path); STATUS state-of-play rewrites entirely; TRADE position card P/L resets; STRATEGY exit rules become primary decision driver; carry-unwind table refreshes on actual unwind speed. Run 7 will be the highest-volume sweep since inaugural Run 1. **Critical:** spawn Run 7 **after** SAM has done the v1.6 cascade in THESIS / CHANGELOG / STATUS / TIMELINE — METSUKE-before-cascade will catch nothing useful.
- **Aug-2024-demotion cleanliness** — sustained 3-run cleanliness on the Aug-2024-as-tail framing. Standing monitor #10 holds; flag any new references in fresh outbox / risk-row prose that slip in.
- **Conviction-decomposition consistency (post Run 3 standing monitor #9)** — STRATEGY L4 conviction line still in v1.5.1 split format. Will hold through Run 6 unless THESIS bumps the conviction split format.

---

## LAST RUN (continued)

### Run 5 — 2026-06-09 (Tue 12:35 PM ET — post SAM-21 mechanical trigger FIRE 70% → 75% + Brent $90 break + USDJPY 4th day above 160 + NFP-shock window carry-forward)

Context: First post-Run-4 sweep. State-of-truth movement since Run 4 watermark (Jun 4 AM): (a) Jun 5-6 NFP shock window — May NFP +172K vs 85K cons → DXY +0.66%, USDJPY tagged 160.20, CFTC Jun 2 print -129,567 (72% of cycle peak, 5th build week, METHOD residual-gate test resolved AGAINST cover); (b) Jun 9 SAM-21 mechanical trigger FIRED — Polymarket 98.2%, Takaichi/cabinet pushback NONE, Q1 GDP revised +1.8% composition hike-tolerant → SAM-21 70% → 75% per pre-registered spec; (c) Brent breached $90 line ($90.16 Tue, −4.34%, 4th consecutive down session, −7% cum from $96.78 Jun-3 baseline); (d) USDJPY 4th day above MOF #3 hard trigger. THESIS not bumped; CHANGELOG not updated (per session context). Cluster A is the SAM-21 mark-up cascade (7 surfaces); Cluster B is the Brent direction re-reversal anti-trigger drift in TRADE; Cluster C is the CFTC -114K/63.7% → -129K/72% lag in TRADE thesis blurb.

> **⚠️ SAM POST-RUN CORRECTION (Jun 9 PM, OHLC-verified — run-log preserved as written):** Two state-of-truth inputs this run ingested were corrected in SAM's evening pass (commit `cd9f23cd`): (1) **context item (c)** — Brent did NOT breach $90 / was NOT a 4th consecutive down session: intraday tag $89.59 (~12 PM ET) recovered to $92.40 by evening (no closing breach); Mon Jun 8 closed UP +1.2%; cum −4.5% not −7%. (2) **context item (d)** — USDJPY was NOT "4th day above 160": 2 distinct tags (Fri + Tue) with Mon dip between. The Cluster B refresh text METSUKE proposed (and SAM applied midday) carried the breach framing into TRADE/STRATEGY — SAM's evening pass re-corrected those surfaces. **Next METSUKE run: diff against the evening-pass language ("tagged $89.59 intraday, didn't hold; choppy not monotonic"), not the midday breach framing.**

- **STALE-MARK: 4 items** (1 batched SAM-21 mark cluster covering 7 surfaces in TRADE+STRATEGY = highest-signal flag this run; 1 STRATEGY Stage-3 trading-day countdown 8→5; 1 STRATEGY L101 vol-crush "market-confirmed at ~88%" lag; 1 batched CFTC level cluster covering 2 surfaces in TRADE thesis blurb + Options "Why options")
- **STALE-FRAMING: 4 items** (1 TRADE header `Last Updated:` 2026-06-04 — body has Jun-9-relevant SAM-21 mark inline upon refresh; 1 STRATEGY header 2026-06-03; 1 TRADE L177 oil-shock risk-row "Brent re-accelerating" — direction now RE-REVERSED to collapse; 1 TRADE L200 EWJ anti-trigger "Oil shock resolves (Brent sub-$95)" — anti-trigger condition is now ACTIVE again at Brent $90.16, the "NO LONGER ACTIVE" framing is itself stale)
- **DUP-LIVE-SPOT: 0 items** (Run 1-4 strips holding)
- **TRIGGER-STATUS-DRIFT: 0 items** (BOJ row will refresh inside Cluster A; MOF #3 row PENDING still correct (zone in-frame but no strike); Bessent row REACTIVATED still correct; JGB 30Y row still correct (12bp below breach); ESR row still correct; USDJPY-sub-155 row noted under STALE-FRAMING via Brent direction below)
- **CAL-DRIFT: 0 items** (TRADE Key Dates includes Jun 10 US CPI / Jun 10 JGB 30Y auction / Jun 16 BOJ / Jun 17 FOMC / Jun 30 Sato — all match CALENDAR; Jun 9 SAM-21 mechanical re-check row was a one-off pre-fire signal in CALENDAR, now resolved post-fire, not a Key Dates omission)
- **ARCHIVE-CANDIDATE: 0 items**
- **MONEY-FIELD-ESCALATION: 1 item** (TRADE L37 Live P/L line reads "−1.4% at FXY $57.51 (≈−$10.5)"; STATUS reads −1.9% at FXY $57.23 (≈−$14). Per Run-1 CALIBRATION carve-out, position-card tracking row is by-design current-mark — but the gap has grown to ~$0.28 FXY / ~$3.5 P/L material from a Jun-1 watermark. Surface as Will-confirm; per spec, NO proposed value, NO direct edit.)
- **CHANGELOG-GAP: 0 items** (Jun 9 SAM-21 mechanical fire is in STATUS/PREDICTIONS/TIMELINE/BOJ ASSESSMENT but no THESIS body edit happened, so no CHANGELOG entry required by spec — informational note only: session context confirms intentional "no version event" decision)
- Sections checked + clean: TRADE Carry Unwind Probability table (14/37/49 unchanged from Run 4; CFTC anchor state described in narrative under the table will refresh on Cluster C apply); TRADE Risk Factors all 5 rows (mitigation columns still THESIS-v1.5.1-aligned; row 4 BOJ-delays risk language still applies; oil-shock row 2 framing flagged under STALE-FRAMING); TRADE Position A Sep-$60 section (multi-channel-convergence basis intact; Jun 9 fire strengthens the "cuts AGAINST Sep OTM" argument but the qualitative conclusion holds — minor STRATEGY L121 incremental note candidate, not a flag); TRADE Hard-Trigger Status all 6 rows (mostly current — BOJ row updates inside Cluster A); STRATEGY Stop loss pre/post-Jun-16 table (event-cap mode A still in force; $55.05 post-event AND-trigger unchanged — Will-decided Jun 3 stop-spec stable through Jun 9); STRATEGY VOL SIGNALS table (Jun-1 reads carried as dated historical; live IV/RR pointer to STATUS captures Jun-9 update without restating); STRATEGY Asymmetry table (5 scenarios still hold under v1.5.1); STRATEGY Decision Rules subheader "STATUS UPDATED 2026-06-03" (Jun-3 stop-spec stamp; Jun 9 fire is a probability mark not a decision-rule change, so subheader holds — borderline but no behavioral drift); TRADE Watchlist Japan Banks entry triggers (will refresh inside Cluster A); TRADE Asymmetric Setup Independent Fed Path paragraph (Jun-1 "Fed-cut multi-month tail" framing strengthened by Jun-5 NFP shock; the conclusion holds but the NFP confirmation could be flagged — borderline, NOT flagging because the paragraph's directional conclusion still holds; surfacing under STANDING MONITORS for next run instead).
- **SAM-applied:** [filled by SAM post-run]
- **SAM-declined:** [filled by SAM post-run]

---

## PENDING from Run 5 (2026-06-09)

*Flags surfaced this run. SAM to apply or decline. METSUKE does not remove these — SAM clears.*

**Cluster A — SAM-21 mark cascade 70% → 75% (mechanical trigger FIRED Tue Jun 9 per pre-registered Jun-3 spec; PREDICTIONS / STATUS / TIMELINE all reflect 75%):**

1. **STALE-MARK — SAM-21 70% mark across TRADE + STRATEGY (7 surfaces, batched per CALIBRATION repeated-phrase rule):** Trigger FIRED per pre-registered spec (Polymarket 98.2%, Takaichi/cabinet pushback NONE, Q1 GDP revised +1.8% composition hike-tolerant). The "held at 70% per pre-registered Jun 9 mechanical trigger" framing is now post-fire stale across the doc. Per STATUS BOJ ASSESSMENT row + SAM-21 mechanical trigger paragraph + PREDICTIONS SAM-21 trajectory (`70%→75%`), the canonical refresh is: **SAM-21 75%** with framing **"SAM 75% per Jun 9 mechanical trigger fire (Polymarket 98.2% + no Takaichi pushback + Q1 GDP composition hike-tolerant); 23pp earned-discount to Polymarket 98.2% preserved for ~25% Takaichi-ceiling tail (failed-twice-too-hawkish discount, calibration not directional disagreement — see STATUS BOJ ASSESSMENT)"** or a compressed variant. Locations:
   - TRADE line 3 (header `Last Updated:`): "SAM-21 HELD 70% per pre-registered Jun 9 mechanical trigger" — header roll required (see Cluster C for header treatment)
   - TRADE line 20 (Active Positions Thesis blurb): "BOJ rate hike Jun 16 (SAM **70%** / market **~85-95%** across surfaces — see STATUS for live Polymarket / swap / Kalshi; SAM held at 70% per pre-registered Jun 9 mechanical trigger and Takaichi-ceiling earned discount)"
   - TRADE line 46 (Hard-Trigger Status BOJ row): "PENDING (Jun 16; **SAM-21 70%; market ~85-95%** across surfaces — see STATUS for live Polymarket/swap/Kalshi; SAM-21 held at 70% per pre-registered Jun 9 mechanical trigger). Dominant remaining catalyst, **market-confirmed base case**."
   - TRADE line 191 (EWJ Watchlist Entry Trigger): "BOJ hikes to 1.00% (Jun 16 base case — **SAM-21 70%; market ~85-95%** across surfaces — see STATUS)"
   - TRADE line 202 (EWJ Status): "WATCHING — BOJ hike Jun 16 is the trigger (SAM-21 70% / market ~85-95% across surfaces — see STATUS)"
   - TRADE line 229 (Japan Banks Entry Trigger): "BOJ hikes to 1.00% (Jun 16 base case — **SAM-21 70%; market ~85-95%** across surfaces — see STATUS)"
   - TRADE line 245 (Key Dates Jun 16 row): "BOJ MPM — DOMINANT REMAINING CATALYST (SAM-21 70%; market ~85-95% across surfaces — see STATUS; SAM-24 25bp @85%)"
   - STRATEGY line 36 (hard-triggers BOJ row): "SAM-21 70% / market ~85-95% across surfaces ... SAM-21 held at 70% per pre-registered Jun 9 mechanical trigger; dominant remaining trigger under v1.5 single-path, now market-confirmed base case"
   - STRATEGY line 184 (Key Check Dates Jun 16): "market ~85-95% across surfaces — see STATUS for live Polymarket/swap/Kalshi; SAM 70% held per pre-registered Jun 9 trigger"
   - STRATEGY line 61 (HOLD section narrative): "**May 31 market repriced June BOJ hike to ~88%** (Polymarket / swap), sustained 9-day move that held straight through both dovish CPI prints (April national, Tokyo May 1.6%) → SAM-21 marked ~50% → **70%**. Market siding with wage/activity mechanism (Apr IP +0.8% / retail +2.1%) + 3-dissent split + SoO 'quite possible from next meeting' over the CPI threshold. Remaining near-term reads that can move SAM-21: CFTC weekly (next release Sat Jun 6), US CPI Jun 10 (Fed-side gate — could move dots one week ahead), BOJ pre-cabling (Jun 13-15; pre-meeting blackout starts ~Jun 13, T-2)." — Jun-9 trigger is now in the PAST not the FORWARD set; CFTC Jun 6 already released; remaining near-term reads is now (US CPI Jun 10, JGB 30Y auction Jun 10, CFTC Sat Jun 13). Suggested refresh: roll the narrative arc forward to: "May 31 repricing → 70% → Jun 9 mechanical fire → 75%" with the forward-reads list updated to Jun 10 / 13 / 16. **Highest-signal narrative-level edit in this cluster** because the HOLD section's recent-events reasoning is what gets re-read at every position-decision boot.
   - STRATEGY line 121 (Position A reactivation #3 partial-trigger note): "the higher near-term hike probability cuts AGAINST Sep OTM optionality" — argument intact, but the SAM-21 reference inline ("HAS re-rated to 70% via May 31 market repricing") can be incrementally extended with the Jun-9 fire ("re-rated to 70% via May 31 → fired to 75% via Jun 9 mechanical trigger; both via market-mechanism not the Tokyo-CPI-rebound + dissent-split-widening leg this condition spec'd"). Lower priority — the qualitative conclusion (NOT WARRANTED) is strengthened, not weakened. Suggested incremental refresh, not a load-bearing flag.
   - **Highest-signal flag this run.** Per CALIBRATION Run-2 pattern (surgical-preservation per location), Will likely wants to preserve the discipline framing (failed-twice Takaichi-ceiling earned discount, calibration not disagreement) verbatim at each site, with the mark updated 70 → 75 and the trigger condition language rolled from "held at 70% per pre-registered Jun 9 mechanical trigger" to "marked to 75% per Jun 9 mechanical trigger fire (pre-registered Jun 3)" or similar. Also, per Run-4 NEXT RUN HINT #1, **structural-fix candidate**: convert the SAM-21 mark surfaces to STATUS-pointer ("see STATUS BOJ ASSESSMENT") and avoid the once-per-cycle touch — but this is now post-fire, the next cascade is Jun 16 itself (binary resolution), so the cluster-touch friction is naturally bounded; preserving inline mark for the next 5 trading days may be the lower-friction choice. SAM's call.

**Cluster B — Brent direction re-reversal (collapse not re-acceleration); spillover into anti-triggers and risk-row framing:**

2. **STALE-FRAMING — TRADE line 177 oil-shock Risk Factor row, mitigation column:** "Brent re-accelerating post Jun 1 MOU break (live Brent in STATUS) — well below Kharg, but **direction reversed**." Direction has RE-REVERSED — Brent now $90.16 (Tue Jun 9), −4.34% Tue, 4th consecutive down session, cumulative −7% from $96.78 Jun-3 baseline, broke the $90 "headwind resolved" line (STATUS Key Thresholds row + Jun 5-6 NFP-shock window narrative + Jun 9 Tue boot). Suggested refresh: "Brent collapsed Jun 5-9 to $90.16 (−7% cum from $96.78 Jun-3 baseline), 4th consecutive down session, broke $90 headwind-resolved line. Driver: China demand weakness + Trump-Iran walk-back rumors. Direction is now Phase-1-pressure-resolving, NOT re-accelerating. Live Brent in STATUS."

3. **STALE-FRAMING — TRADE line 200 EWJ Watchlist Anti-Trigger:** "Oil shock resolves (Brent sub-$95, MOU framework hardening) — **❌ NO LONGER ACTIVE; Iran MOU effectively broken Jun 1, Brent +4% re-accelerating to $94.78**." This anti-trigger condition (Brent sub-$95) is now MET again — Brent $90.16 is sub-$95 by a wide margin. The "NO LONGER ACTIVE" framing is itself stale post Jun-5-9 oil collapse. Suggested refresh: "Oil shock resolves (Brent sub-$95) — **🟡 PARTIALLY ACTIVE again; Brent collapsed to $90.16 (Jun 9, −7% cum from Jun-3 baseline) on China demand + Trump-Iran walk-back rumors. MOU framework hardening NOT yet — message suspension still active. Treat as Brent-side resolution only, not MOU-side; the EWJ-puts anti-trigger calls for BOTH legs.**" Mechanism-relevance test: FIRES — EWJ thesis routes through BOJ→mortgage→consumption AND yen-side via channel coherence; Brent collapse mid-cycle is precisely the kind of macro re-read that should flip the anti-trigger live state.

4. **STALE-MARK — STRATEGY line 16 Stage 3 row, trailing line:** "**8 trading days to Jun 16 BOJ**." Today is Tue Jun 9; STATUS lead reads "**Next catalyst: BOJ Jun 16 = 5 trd days**." 3-day countdown drift (recurring class per STANDING MONITOR #15 added Run 4). Per NEXT RUN HINT: this is a recurring drift class until Jun 16; could be eliminated by removing the explicit number, but SAM's call on whether the countdown anchor is load-bearing.

**Cluster C — Header roll + CFTC anchor refresh:**

5. **STALE-FRAMING — TRADE line 3 `Last Updated:` header:** "2026-06-04 (Jun 4 AM — METSUKE Run 4 sync: ... SAM-21 HELD 70% per pre-registered Jun 9 mechanical trigger.)" — body's Cluster A refresh injects 70% → 75% with the trigger now post-fire; header line still cites "HELD 70% per pre-registered Jun 9 mechanical trigger" framing. Same recurring drift class as Runs 2 and 4 caught (STANDING MONITOR #3). Suggested refresh stamp: "2026-06-09 (Tue Jun 9 ~12:35 PM ET — METSUKE Run 5 sync: SAM-21 mechanical trigger FIRED 70% → 75% per pre-registered Jun-3 spec (Polymarket 98.2% + no Takaichi pushback + Q1 GDP composition hike-tolerant); Brent breached $90 line ($90.16, −7% cum from $96.78 Jun-3 baseline); USDJPY 4th day above MOF #3 hard trigger no strike yet; CFTC -129,567 / 72% of cycle peak, 5th build week)."

6. **STALE-MARK — TRADE line 20 thesis blurb + line 67 Options "Why options" CFTC level cluster (batched, 2 surfaces):** Both surfaces cite "CFTC short at 63.7% of cycle peak (-114,667 May 26; 4th build week, +27K new shorts WoW; broke -102K recent-cycle peak)" / similar. STATUS Channel 2 + dashboard now reads **-129,567 (Jun 2 data; 5th build week; 72.0% of Jul-2024 cycle peak; net -14,900 WoW)**. Suggested refresh: "-129,567 Jun 2; 5th build week; 72.0% of cycle peak — METHOD amplifier +5pp ON, residual ON; approaching 85% danger zone where amplifier escalates to +8-10pp." Next print Sat Jun 13 (last pre-blackout). Per Run-2 pattern: batched as 1 STALE-MARK with location list, preserving differentiated context per location (the thesis-blurb summary frames the "4th build week" arc, which now needs the "5th build" continuation; the Options "Why options" item (b) intervention-paradox subset framing is the v1.5.1-correct intervention condition and only needs the level update).

7. **STALE-MARK — STRATEGY line 101 vol-crush rule rationale:** "**Vol-crush risk on a priced-in hike is now elevated** (hike is market-confirmed at **~88%**, so the surprise premium is small)." Market-confirmed level now Polymarket 98.2% (Tue Jun 9); the qualitative conclusion (vol-crush risk elevated) is unchanged, the level needs to roll. Suggested refresh: "(hike is market-confirmed at **~88-98% depending on surface — Polymarket 98.2% Jun 9, swap ~86%, Kalshi ~80%**, so the surprise premium is small)" or compressed via STATUS pointer.

**Cluster D — Header roll for STRATEGY (low priority; recurring per STANDING MONITOR #3):**

8. **STALE-FRAMING — STRATEGY line 3 `Last Updated:` header:** "2026-06-03 (cross-ref pointer added → THESIS § CARRY-UNWIND PROBABILITY METHOD; carry-unwind buckets restated as decomposed estimate ...)" — header reflects the Jun-3 work; body has Jun-9 implications cascading inline upon Cluster A + Cluster B + Cluster C apply. Recurring header-roll-on-body-change pattern. Suggested refresh stamp: "2026-06-09 (METSUKE Run 5 sync — SAM-21 mark cluster 70% → 75% post Jun 9 mechanical fire; vol-crush market level rolled to ~88-98% surface range; Brent direction re-reversed to collapse [$90.16, −7% cum]; trading-day countdown rolled 8 → 5)" or similar.

**Money-field escalation (Will-confirm only — NO proposed value):**

9. **MONEY-FIELD-ESCALATION — TRADE line 37 Live P/L line:** Reads "**−1.4%** at FXY $57.51 (≈−$10.5); breakeven $58.32, above spot". STATUS § FXY POSITIONING + dashboard row now reads "**−1.9% at FXY $57.23** (≈−$14 unrealized)". Per Run-1 CALIBRATION carve-out, position-card P/L lines are by-design current-mark — but the FXY mark has drifted $0.28 (Jun-4 watermark to Jun-9 mark) and the P/L delta is ~$3.5 absolute, ~0.5pp percent. Surface as **Will-confirm only, NO proposed value** per spec (per `[[feedback_position_cost_basis_not_authoritative]]` and METSUKE money-field discipline — state-file figures are NOT authoritative). SAM's call on whether to refresh the by-design tracking row at this mark gap, but METSUKE does not propose the corrected number. The breakeven $58.32 and avg cost remain unchanged (Will's ground truth) — only the unrealized P/L number is the candidate stale field.

*Total Run-5 flags: 9 items across 4 clusters + 1 money-field escalation (1 batched SAM-21 cluster with 10 locations + 1 batched CFTC cluster with 2 locations + 4 single STALE-FRAMING + 1 single STALE-MARK + 1 MONEY-FIELD-ESCALATION).*

**Notes for SAM:**

- **Cluster A (SAM-21 70% → 75% post-fire cascade) is the highest-yield flag this run** — 10 surfaces across TRADE + STRATEGY. Per Run-4 CALIBRATION, the apply pass should preserve the discipline framing (failed-twice Takaichi-ceiling earned discount, calibration not disagreement) verbatim at each site; only the numeric mark and trigger-tense change (held → fired). The most narrative-load-bearing surface is STRATEGY L61 (HOLD section), where the "remaining near-term reads that can move SAM-21" list needs the most rewrite (CFTC Jun 6 → released; Jun 9 trigger → fired; forward set now Jun 10 US CPI + Jun 10 JGB 30Y auction + Jun 13 CFTC + Jun 16 BOJ).
- **Cluster B (Brent direction re-reversal) is the genuinely new mechanism flag.** Brent direction has flipped TWICE between Run 3 baseline ($94.78 Jun 1) and Run 5 ($90.16 Jun 9) — once Jun 1 (collapse → +4% re-accelerate on MOU break) and once Jun 5-9 (re-acceleration → −7% cum collapse on China demand + Trump-Iran walk-back rumors). The TRADE oil-shock Risk Factor row + EWJ Watchlist anti-trigger are the two surfaces that carry the direction-tense; both are now Jun-5-direction stale.
- **CHANGELOG-GAP**: 0 items per spec (Jun 9 mechanical fire was a probability mark update, not a THESIS body edit; STATUS / PREDICTIONS / TIMELINE / BOJ ASSESSMENT carry the cascade; session-context confirms intentional no-version-event treatment). Informational only — no flag.
- **Aug-2024-demotion completeness (Will-flag from Run 4) remains CLEAN this run** — no new Aug-2024-as-expectation references slipped in; the 5 Cluster B sites from Run 3 + the 2 incidental references (STRATEGY:76 stop-spec rationale, STRATEGY:129 no-spreads "tail") all still v1.5.1-aligned.
- **Stop spec (Will-decided Jun 3 event-cap mode A) remains stable through Jun 9** — TRADE entry-card stop row + STRATEGY pre/post-Jun-16 table + THESIS POSITION VIEW vehicle line + Risk Factors oil-shock row "Pre-Jun-16: no stop fires" all in sync; no edits needed.
- Recurring drift classes from prior runs all firing on cue: SAM-21 mark cluster (Cluster A — now post-fire cascade), trading-day countdown (Cluster B item 3 — 3-day drift), header roll (Clusters C + D — recurring).

*(SAM clears these as flags get applied or declined.)*

### Run 6 — 2026-06-19 (Fri AM — post Jun-16 BOJ hike-as-priced RESOLVED + Jun-17 FOMC Warsh debut hawkish + Jun-17 Iran/US deal SIGNED + Jun-18 Step 1.5 stop re-arm)

Context: First post-Run-5 sweep, fired at a regime hinge. Three resolved-event cascades hit between Run 5 (Jun 9) and now: (a) Jun 16 BOJ hiked 25bp to 1.00% as-priced (CH-004 confirmed, no carry unwind, 7-1 Asada-dovish-dissent); (b) Jun 17 FOMC under new Chair WARSH (debut, on board since May 22) held but +40bp 2026 median dot (Pillar 1 directional vector INVERTED across Jun 16-17); (c) Jun 17 Iran/US deal SIGNED (initial agreement, signing-binary resolved, verification leg open). Also: Jun 18 Step 1.5 stop re-arm (Will-decided single-leg FXY ≤ $55.05; supersedes Jun-3 AND-spec post-event because BOJ-dovish leg is permanently false). SAM-21/23/24/26 all resolved; 0 OPEN predictions. v1.6 backbone DRAFT exists (not canonical until post Fri-Jun-19 CPI + RED pass). Drift focus: Step 1.5 completeness audit + v1.5.1-vs-v1.6 tension flags (don't propose v1.6 framing yet).

- **CRITICAL DRIFT: 3 items** (1 STALE-FRAMING risk-row Channel-1-reactivates @10% / Norinchukin-resolved-against; 1 STALE-MARK STRATEGY HOLD-section forward-reads list now fully stale post-fire / post-CPI / post-auction / post-CFTC; 1 STRATEGY-Stage-3 paragraph entirely pre-event)
- **MODERATE DRIFT: 5 items** (STRATEGY hard-trigger BOJ row still PENDING + ~88-98% range; STRATEGY Hard-triggers subheader still 2026-06-03 stamp; TRADE header 2026-06-14 Sun PM stamp + STRATEGY 2026-06-09 PM stamp lag the Jun 16-18 cascade; Sat Jun 13 CFTC reference in TRADE carry-table is pre-RESOLVED; TRADE Asymmetric Setup Independent Fed Path entire section still Jun-1-Fed-cut-soft framing — completely inverted by Warsh)
- **MINOR DRIFT: 4 items** (TRADE Tranche-2 Hard-Trigger Status header "UPDATED Jun 1" lag; STRATEGY § Position A "v1.5 single-path" framing borderline; STRATEGY Key Check Dates Jun 1 RESOLVED Iran framing pre-signing; TRADE Key Dates "🟠 ongoing Iran/Hormuz MOU substantively walking back (unsigned)" superseded by SIGNED)
- **v1.5.1-vs-v1.6 TENSION: 4 items** (THESIS v1.6-DRAFT explicit "compression delivers via Channel 2" → "carry-trade convexity tail"; v1.6 downgrades conviction Direction/level HIGH → MEDIUM; v1.6 considers vehicle question OPEN; v1.6 reframes structural pillars under hike-regime re-derive — TRADE/STRATEGY load-bearing pillar language WILL need rewrite at v1.6 finalize)
- **DUP-LIVE-SPOT: 0 items** (Run 1-5 strips holding)
- **TRIGGER-STATUS-DRIFT: 0 items separate from Cluster A above** (Channel 3 reactivation language → Step 1.5 reconcile already collapsed in TRADE L20 + Risk Factors row 1 via Jun-18 sweep; the standalone trigger-row updates fold into the MODERATE-DRIFT Stage-3 + hard-trigger BOJ-row rewrite)
- **CAL-DRIFT: 0 items** (TRADE Key Dates Jun 16 row ✅ updated, Jun 17 FOMC + Jun 30 Sato still in sync with CALENDAR)
- **ARCHIVE-CANDIDATE: 0 items** (mid-event; v1.6 finalize will trigger several archival decisions)
- **MONEY-FIELD-ESCALATION: 0 items** (TRADE L37 Live P/L "−1.8% at FXY $57.26" matches STATUS exactly — within position-card carve-out; cost basis $58.32 unchanged; stop spec $55.05 just refreshed Jun 18, internally consistent across 3 spots TRADE + 3 spots STRATEGY + 4 spots STATUS per spawn note)
- **CHANGELOG-GAP: 0 items** (all three Jun-18 facts in CHANGELOG 2026-06-18 entry per spawn note; Step 1.5 audit trail in commit `97701098`)
- **Step 1.5 stop completeness — CLEAN** (per spawn note: 3 spots TRADE + 3 spots STRATEGY all carry the single-leg FXY ≤ $55.05 spec with the "BOJ-dovish leg permanently false → AND collapsed" rationale and "interim, v1.6 may revise" caveat. No straggler old-AND-spec references remaining in TRADE/STRATEGY body. The Jun-3 historical row in STRATEGY § Stop loss is correctly preserved as `~~strikethrough~~` audit-trail, not live spec).
- **R:R math — CLEAN** (TRADE L36 reflects $55.05 stop / $62 target / FXY $56.86 Thu boot / CH-032 modal band caveat — all coherent).
- **PREDICTIONS scoreboard — CLEAN** (no SAM-21/23/24/26 cited as live anywhere in TRADE/STRATEGY; all references properly post-resolution).
- **SAM-applied:** [filled by SAM post-run]
- **SAM-declined:** [filled by SAM post-run]

---

## PENDING from Run 6 (2026-06-19 AM)

*Flags surfaced this run. SAM to apply or decline. METSUKE does not remove these — SAM clears.*

### CRITICAL DRIFT (load-bearing — must fix before next position decision)

1. **STALE-FRAMING — TRADE § Risk Factors L184, "Channel 1 reactivates" row 10% / mitigation column:** Row reads *"Probability **10%** | +3-5pp 60d prob upside (offsetting positive — would expand structure back to multi-channel) | Watch JGB long-end, M&A saturation at Big 3 mutuals"*. Mitigation column is silent on the **Norinchukin gate RESOLVED NOT REACTIVATED Jun 10** (CLO record ¥10.1T, +¥1.8T YoY, 4-of-4 institutions grew US credit) — THESIS L116 + L311 RISK FACTORS row explicit that "Norinchukin gate (last near-term reactivation candidate) resolved AGAINST." Probability 10% may also be stale — THESIS L311 explicitly says **"Post-BOJ agenda (Will-directed): re-examine this 10% row and whether Channel 1 'deferred' should become 'retired pending new mechanism.'"** This is the post-BOJ re-examination THESIS flagged; TRADE row hasn't tracked. **Direction:** sync mitigation column to "Norinchukin gate RESOLVED AGAINST Jun 10; next re-test H2 FY2026 / FY2026 ESR" + flag probability as candidate for v1.6 retire decision. Load-bearing because this is a Risk Factor mitigation column the doc relies on.

2. **STALE-MARK / STALE-FRAMING — STRATEGY § HOLD section L61 "Remaining near-term reads that can still move SAM-21":** The 4-item list `(1) Wed Jun 10 US CPI / (2) Wed Jun 10 JGB 30Y auction / (3) Sat Jun 13 CFTC / (4) BOJ pre-cabling Jun 13-15` is **entirely pre-Jun-16-resolved**. All 4 reads have fired:
   - (1) US CPI Wed Jun 10: HOT-AS-EXPECTED, no soft surprise → gate closed (CALENDAR § RECENTLY RESOLVED)
   - (2) JGB 30Y auction Jun 10: BTC 2.936x, tail 2.8bp — SOFTENING not stress, no SAM-26 re-light (CALENDAR § RECENTLY RESOLVED)
   - (3) Sat Jun 13 CFTC: −145,818, 81% peak (no cover; STATUS dashboard)
   - (4) BOJ Jun 16: RESOLVED hike-as-priced
   - **And SAM-21 itself is now CONFIRMED.** This entire HOLD-rationale paragraph is the most-stale prose block in either doc. Load-bearing because HOLD-section is read at every position-decision boot.
   - **Direction:** rewrite the HOLD-section narrative to post-event posture — what SAM-relevant near-term reads exist NOW (Fri Jun 19 National CPI; Sat Jun 20 CFTC = post-event positioning state, decision-grade observable per v1.6 DRAFT § convexity-tail EV table; July 31 BOJ; Aug Hormuz toll-free expires; verification-leg watch). Don't propose v1.6 framing yet — but the forward-reads list MUST update.

3. **STALE-FRAMING — STRATEGY § WHERE WE ARE IN THE TRADE Stage 3 row (L16):** Entire long paragraph is the Run-5 pre-event composition (countdown "5 trading days to Jun 16 BOJ" + SAM-21 70%/75% + "Brent drifting down choppily" + market ~98% + "WE ARE HERE — v1.5 single-path, market-confirmed base case ... June BOJ dominant remaining trigger (SAM 75% / market ~98%); Fed-cut backup multi-month tail"). All of this is now history: BOJ hiked (catalyst spent), Fed-cut backup REPLACED by Fed-HIKE regime under Warsh, the "WE ARE HERE" framing belongs to Stage 5 (post-trigger) or a new Stage 6 (post-resolution awaiting v1.6). **Load-bearing because Stage-3 row IS the doc's live-status anchor** and the stage-table is what gets read first at any decision boot. **Direction:** Stage 3 → mark RESOLVED; advance the "WE ARE HERE" marker to Stage 4/5 or a new "post-catalyst tail watch" row; preserve the Stage-3 narrative as historical (consistent with how STATUS preserves pre-event framing under the resolved-block convention). Don't propose v1.6 framing for the new live row.

### MODERATE DRIFT (factual but not load-bearing — fix in v1.6 finalize or interim)

4. **STALE-MARK — STRATEGY § Decision Rules hard-triggers table BOJ row L36:** Row reads *"**BOJ hikes at June meeting** | PENDING (Jun 16; SAM-21 75% / market ~88-98% ... 98.2% Tue Jun 9 ... SAM-21 marked 70% → 75% Tue Jun 9 per pre-registered mechanical trigger FIRE ... market-confirmed base case) | OPEN for share add OR options re-up"*. PENDING → ✅ FIRED; Add-authorization "OPEN" → USED (or N/A post-event). Same content as the corresponding TRADE row (L46) which IS updated. **Direction:** mirror TRADE L46 — mark ✅ FIRED Jun 16, no longer OPEN. Lower priority than Cluster #2/#3 because hard-trigger tables are reference, not decision-narrative.

5. **STALE-FRAMING — STRATEGY § Decision Rules subheader L29:** *"**Hard triggers — STATUS UPDATED 2026-06-03 (Jun 3 PM — stop-spec harmonization + METSUKE Run 2 sync; per Will-decided event-cap mode A):**"*. The "event-cap mode A" is superseded by Step 1.5 single-leg (this is one of the original Jun-3 stamp references, now 16 days stale, and the "event-cap mode A" descriptor no longer characterizes the spec). **Direction:** roll stamp to 2026-06-18 (Step 1.5 re-arm + BOJ resolved + FOMC Warsh-hawkish + Iran SIGNED). Recurring header-drift class per STANDING MONITOR #3.

6. **STALE-FRAMING — TRADE header L3 Last Updated + STRATEGY header L3 Last Updated:** TRADE = "2026-06-14 Sun PM (Tier-1 mark refresh — Brent + Ueda + 6-input re-mark integration; money fields untouched per discipline)" — pre-dates the Jun 16-17-18 cascade. STRATEGY = "2026-06-09 PM (evening correction: Brent $90 was an intraday tag-no-hold...)" — predates by 10 days. STRATEGY has had only minor edits since Jun 9 per the L275-278 CHANGELOG (Jun 10 evening + Sun Jun 14 + the implicit Step 1.5 Jun 18 stop-spec touch). **Direction:** roll both headers to 2026-06-19 (METSUKE Run 6 sync — post BOJ/FOMC/Iran/Step-1.5 cascade). Recurring header drift, Standing Monitor #3.

7. **STALE-MARK — TRADE § Carry Unwind Probability table L153 narrative under table:** *"... CFTC -129,567 = 72.0% of cycle peak (Jun 2 data, Sat Jun 6 release; 5th build week) → amplifier +5pp ON, residual ON ... See STATUS for live anchor state + next CFTC re-eval Sat Jun 13 (last pre-blackout)."* Three drift items: (a) CFTC is now −145,818 / 81% of cycle peak (Jun 9 data, rel Fri Jun 12, 6th build week) — STATUS dashboard; (b) "next CFTC re-eval Sat Jun 13" was the Run-5 pre-event read — Sat Jun 13 release is now in the past; the next pre-fire-state-of-cover observable is **Sat Jun 20** (Jun 16 data, post-catalyst cover state — explicitly decision-grade per v1.6 DRAFT § EV table per spawn-note context); (c) the table's snapshot values (~8/23/32 Sun Jun 14 re-mark) ARE current per STATUS § CARRY UNWIND PROBABILITY but the table cells in TRADE L149-151 still read "~8% / ~23% / ~32% (Was 14% Jun 3; Sun Jun 14 re-mark)" — CURRENT and matches STATUS, but the contributor notes inline reference SAM-23 etc.; **the snapshot values are clean, only the under-table narrative drifted**. **Direction:** refresh narrative (a/b/c above). The Sat Jun 20 CFTC reference IS the v1.6 decision-grade observable per spawn-note item 7 — flag for SAM's call on whether to inject the v1.6-DRAFT EV-table forward observable here or wait for v1.6 finalize.

8. **STALE-FRAMING — TRADE § Asymmetric Setup, Independent Fed Path L170-173:** Entire section is the Jun-1 reframe of Fed-cut path as "multi-month tail, not Jun-window" — internally consistent at that watermark. **But now empirically inverted post-Jun-17 Warsh hawkish FOMC.** STATUS § SECONDARY PATH L243-245 reads *"FED CUT → FED HIKE REGIME (Jun 17 FOMC: SEP confirmed the regime flip; 'secondary CUT path' is now operationally a FED-HIKE path)"*. THESIS § INDEPENDENT CATALYST L255 explicitly flags the section "operationally inverted; v1.6 will retitle/restructure." TRADE Asymmetric Setup section still reads pre-Warsh: "CME FedWatch shows Jun 17 FOMC **>97% no-change** ... <10% cut odds anywhere in 2026 ... PC-cascade path is retained as a multi-month tail (cascade → recession → cuts later in 2026), not a discrete Jun-window backup." The "no-change priced" detail held literally (Fed DID hold) but the dot-plot SEP inverted Pillar 1 directionally. **Direction:** mirror THESIS L255 framing — section is operationally inverted; SAM-side carry tripwire moves from "Fed-cut surprise" → "any walk-back of the Jun-17 dot revision"; multi-month tail still live theoretically but under Warsh-Fed-hawkish regime (not Powell-era cut-pricing dynamics). Flag the entire heading as candidate for v1.6 retitle/restructure (THESIS already flags this in v1.6 plan). High-signal because the Asymmetric Setup section is doc-prominent thesis recap.

### MINOR DRIFT (prose/cross-ref polish — defer)

9. **STALE-FRAMING — TRADE § Tranche 2 Hard-Trigger Status header L42:** *"### Tranche 2 Hard-Trigger Status — UPDATED Jun 1"*. Body has rows refreshed through Jun 16 (BOJ row ✅ FIRED Jun 16) and Jun 14 (MOF row SAM-23 re-derived) and Jun 18 (Step 1.5 stop). Header stamp 17 days stale. **Direction:** roll to "UPDATED 2026-06-19" or similar. Recurring sub-header drift, Standing Monitor #3.

10. **STALE-FRAMING — STRATEGY § Position A re-activation #3 parenthetical L122:** Tail of the long parenthetical reads *"**Jun 9 update: SAM-21 marked further 70% → 75% on mechanical trigger fire (Polymarket 98.2%); CFTC further built to -129,567 (72% peak); Brent drifting down ($92.40 Tue PM after an intraday $89.59 tag that didn't hold).** Conclusion (NOT WARRANTED) holds and is arguably strengthened further — even higher near-term hike probability + amplifier-residual ON regime continuing makes deferred Sep OTM optionality less, not more, attractive."* Updates are now stale (SAM-21 marked to ~90 then RESOLVED CONFIRMED; CFTC 81% / −145,818; Brent ~$80 post-deal-signed). Conclusion (NOT WARRANTED) still holds — strengthened further by Jun-16 resolution. **Direction:** trim or refresh the dated update; the conclusion-line and decision (NOT WARRANTED) are still correct. Lower priority because Position A is "NOT WARRANTED" under v1.5 and v1.6 considers vehicle question OPEN — full Position A re-examination is v1.6's job, not METSUKE's.

11. **STALE-FRAMING — STRATEGY § Key Check Dates L180 ✅ Jun 1 RESOLVED bullet:** *"Iran/Hormuz MOU effectively broken — Tehran suspended document exchange + Hormuz block threat; Brent +4% to $94.78; Channel 3 REACTIVATED, SAM-23 ~72%. Forward watch is now walk-back (Trump-Khamenei reset → resign path) vs further escalation (Brent $100+ / Hormuz close attempt)."* Resolved-Jun-1 framing is historical and correct as a dated point-in-time observation per CALIBRATION (legit historical reference). **But the forward-watch line at the end** is fully resolved: deal SIGNED Wed Jun 17 (verification leg OPEN, Hormuz reopening process begun Day 110). **Direction:** keep the Jun-1 RESOLVED capture verbatim; trim/refresh the trailing "Forward watch is now..." clause to the post-signing forward watch (verification leg + Oman fee admin after 60-day toll-free / HEU dilution / sanctions waivers). Lower priority — the forward-watch in the resolved-bullet is decorative not decision-driving.

12. **STALE-FRAMING — TRADE § Key Dates L246 "🟠 ongoing Iran/Hormuz MOU — substantively walking back (unsigned)":** Pre-signing framing — Jun 17 deal-signed RESOLVES the signing-binary; verification leg is the live forward question per THESIS/CALENDAR. **Direction:** mirror CALENDAR § INTERVENTION WATCH "Iran/US deal SIGNED Wed Jun 17" row + GEOPOLITICAL WATCH "✅ Wed Jun 17" row framing. The "Iran has NOT confirmed" caveat is itself stale — Pezeshkian electronic signature is the Iran-formal confirmation per Al Jazeera / Step 1.5 reconcile.

### v1.5.1-vs-v1.6 TENSION (lines that v1.6 finalize will need to update — do NOT propose v1.6 framing yet, but flag for awareness)

13. **TENSION — TRADE L20 thesis blurb "structurally bid even if Jun 16 disappoints; the call premium is the catalyst-conditional bet":** This is the v1.5.1 structural-pillar backbone framing. v1.6 DRAFT one-liner explicitly says *"the carry-trade direction-conditional case for being long yen is wrong (or at least directionally inverted) near-term — but the carry-trade CONVEXITY case is intact-to-stronger"* and DRAFT explicitly DOWNGRADES Direction/level HIGH → MEDIUM. The current TRADE blurb's "structurally bid" framing rests on Pillar 1 directional case (rate-differential compression) which v1.6 DRAFT calls inverted. **Tension. Do NOT propose v1.6 rewrite — v1.5.1 + Jun-18 fact strip in THESIS L25 already qualifies Pillar 1 as "RE-WIDENING, not compressing" with structural-LEVEL argument retained pending v1.6 re-derive. The TRADE L20 blurb is currently aligned with v1.5.1+strip if read carefully, but the literal "structurally bid even if Jun 16 disappoints" is now thin (Jun 16 didn't disappoint — it confirmed; the Fed disappointed structure). v1.6 finalize will need to update.

14. **TENSION — TRADE L33 stop-loss cell "Interim risk-control; v1.6 pillar-audit may revise":** Correctly flags v1.6 dependency. No drift — already pre-flagged. Listed here to confirm METSUKE saw it and read it as v1.6-aware.

15. **TENSION — STRATEGY L4 conviction line "Direction/level HIGH; near-term timing MEDIUM":** v1.6 DRAFT explicitly downgrades to "MEDIUM / LOW / MEDIUM-HIGH-CONDITIONAL-on-Sat-Jun-20-CFTC / OPEN-vehicle-fit". CH-032 caveat IS embedded in STRATEGY L4. v1.5.1+strip THESIS conviction lines still read HIGH/MEDIUM (canonical until v1.6 finalize). **Tension flagged.** Don't propose rewrite — v1.6 finalize will replace these.

16. **TENSION — STRATEGY L203 hold-row "backstop language amended per CH-032 — pillars under hike-regime re-derivation; full pass in v1.6":** Already correctly v1.6-aware (Jun-10 evening edit explicitly acknowledged the pillar re-derivation pending). Listed for completeness.

### STANDING MONITORS NEXT (post Run 6)

- **NEW (post Run 6):** v1.6 finalize is the next major restructure event. When THESIS_v1.6_DRAFT.md is approved and renamed THESIS.md, the cascade will hit virtually every section of TRADE and STRATEGY (conviction lines, structural-pillar references, "compression delivers via Channel 2" framing, position vehicle question, Sep $60 Position A retire-vs-defer decision, Stop spec sizing-grade revision, Risk Factors v1.6 rebuild). Run 7 should be spawned **after** SAM completes the v1.6 cascade in THESIS / CHANGELOG / STATUS / TIMELINE — METSUKE-before-cascade catches little useful. Critical: this is the highest-volume sweep since inaugural Run 1, as anticipated in Run-5 NEXT RUN HINTS § Post-Jun-16 binary cascade. **Pre-finalize Run 6 covers the Step 1.5 interim window; Run 7 covers the v1.6 finalize cascade.**
- **NEW (post Run 6):** Sat Jun 20 CFTC print is the v1.6-DRAFT decision-grade observable for the CONVEXITY-TAIL SURVIVAL row (post-catalyst cover state UNRESOLVED until Jun 20 print per v1.6 DRAFT L34-35). Watch whether SAM's reference to "Sat Jun 13 CFTC" in TRADE/STRATEGY refreshes to "Sat Jun 20 CFTC" — same drift class as the recurring countdown drift. May produce cluster-refresh in Run 7.
- **NEW (post Run 6):** Step 1.5 stop-spec completeness — confirmed CLEAN this run. Future risk: if SAM updates stop-spec again (tighten / loosen / replace with stop-band) at v1.6 finalize, sweep the same 6 spots (3 TRADE + 3 STRATEGY) verified this run for cluster-completeness. Maintain audit-trail row in STRATEGY § Stop loss (strikethrough preserved).
- **NEW (post Run 6):** HOLD-section forward-reads list (STRATEGY L61) — the highest-velocity narrative-drift surface in either doc. Past 6 runs: forward-reads list lapsed at each catalyst boundary (CFTC release / CPI print / auction / BOJ meeting). v1.6 finalize will reset to the new forward set; Run 7 should re-audit and Run 8+ should expect the same drift class to recur every catalyst boundary. Consider STATUS-pointer fix at v1.6 finalize.
- **NEW (post Run 6):** Channel-1-reactivates risk-row probability (currently 10% in TRADE Risk Factors). THESIS flagged Will-directed re-examination post-BOJ ("'deferred' should become 'retired pending new mechanism'"); Norinchukin gate resolved AGAINST. Watch whether v1.6 retires the row entirely or shifts the probability.
- **CARRY-OVER from prior runs:** Recurring drift classes (SAM-21/SAM-23 mark cluster, header roll, trading-day countdown, market-quote cluster, etc.) all naturally sunset at Jun 16 binary resolution. New recurring classes for the v1.6 era should emerge in Run 7+.

*Total Run-6 flags: 12 distinct items across 3 severity tiers + 4 v1.5.1-vs-v1.6 tensions (informational, not action-now). Two are batch-flags (Step 1.5 completeness audit + R:R math + PREDICTIONS scoreboard) explicitly cleared CLEAN per spawn-note ask.*

*(SAM clears these as flags get applied or declined.)*
