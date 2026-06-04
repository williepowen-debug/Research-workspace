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
- **NEW (post Run 4):** Trade-day countdown to Jun 16 — STRATEGY Stage 3 carries the explicit countdown number which decays daily. Was caught Run 2 (11 → 9), now Run 4 (9 → 8). Recurring drift class. Could be eliminated by removing the explicit number ("9 trading days") in favor of "T-X to Jun 16 BOJ" with X live-pulled from STATUS — but that requires SAM's call on whether the number is load-bearing (a near-term framing anchor) vs cosmetic.

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
