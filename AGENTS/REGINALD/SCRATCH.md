# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-06-25 — Transmission-Terminus Cluster, Pass 1 (hub seat) — tripwire + grid + leg-spec

**Did three bounded things (per Prome spawn brief):**
1. **CCC/HY >3.6×-sustain tripwire BUILT** (finally — flagged 6/8, 6/19, 6/22, never built). VX-REG-18.04 + `research/CCC_HY_TRIPWIRE_2026-06-25.md`. Live re-pull (`.venv` + fetch.py fred): **3.49× [6/24]** (CCC 964 / HY 276). **3.6× NEVER crossed in 12 sessions** (band 3.42-3.57x) → DORMANT. Sustain = **3 consecutive closes >3.6×** (derived: oscillation cycle ~1-2d, in-band elevated clusters up to 3d, threshold set above the band ceiling); reset on any ≤3.6×; ARMED at 1-2. Mandatory **driver-decomp**: CCC-led=substance/escalate LIQUID/BROCK; HY-led=beta/benign.
2. **Master Q2-Print Convergence Grid** skeleton stood up → `research/Q2_PRINT_CONVERGENCE_GRID_2026-06-25.md` (WAL/OZK/EGBN/ZION/CFG/SSB + CORAL FL-canary rows) + exact leg-input spec for CARL/CORAL.
3. **Inbox triage** (load-bearing-for-cluster only).

**Key analytic finding (substance-vs-beta):** 6/19→6/24 ratio **COMPRESSED** 3.560→3.493× — HY widened +3.8% vs CCC +1.8%, so the 6/24 bear leg is **HY/index-led, not CCC-tail-led = beta not substance.** Additive gap (CCC−HY) widened +7bp though → ratio and gap diverge when both legs move (ratio base grows). Handed to Prome/CARL as a corroborating input to the X1 "widening is beta" call; CARL's consumer-substance read is the independent test.

**WALTER inbox triage dispositions:**
- **PROCESSED (cluster-load-bearing):** SIG-W-20260624-007 (DFAST) → INTEGRATED, bull-counter+coverage-caveat row in STATUS + BOARD_LOG. SIG-W-20260624-004 (BXMT) → INFO_ONLY cross-ref (not bank-held), STATUS + BOARD_LOG.
- **DEFERRED, already-integrated:** 618-005/006/007/008/009 (ACTION cluster) — all live in STATUS rows (IPO / capital-rules / Office CMBS / MF starts / CRE-DQ-by-tier DRILLED 6/20). Not re-moved.
- **DEFERRED → other agents' legs:** 619-002/007/008 + 621-011/013 + 622-001 (DEWEY) → CORAL (FL CRE/condo). 622-008 (consumer card) → CARL. 621-009 (liquidity backdrop) → LIQUID. 622-002 (AI-software CLO) → BROCK/light. None cluster-Pass-1-critical; DEWEY (622-001) already partially reflected in my STATUS CRE-DQ row.

**Grid FINALIZED + VERIFIED-RECONCILED same session** — both legs folded then reconciled to CORAL's verified 10-Q XBRL fill (commit `ee8c195e`): CARL consumer (CFG = only separate consumer path → 3-path standout; rest housing-secured→CORAL) + CORAL FL (5 canaries, BKU/AMTB attribution fixed, two-channel resi+condo netting). **Verified 30-89d:** SBCF $28.2M (−14% QoQ off Q4 peak/+65% YoY; nonaccrual $72→95M sharper), USCB $10.1M (tiny base), AMTB $88.6M (lumpy-commercial), BKU $234M→$123M ex-gov benign. SSB FL-content ≈$0 (rate-shock reclass); VLY→fleet. **Cluster verdict: diagnostic NOT-met + predicted un-met Q2; realized synchronized NCO = 2027; condo/SIRS = 2027.** Key refinement: the only ≥2-bank synchronized = USCB+SBCF **YoY-ONLY**, NOT realized NCO, QoQ cooling. CCC/HY tripwire DORMANT (3.49×); 6/24 widening HY-led=beta. All three corroborate: nothing fires near-term, machinery pre-built for X1.

**Wave-2 + adversarial pass + COF/CFG axis-split wired same session** (`research/Q2_PREREG_ADVERSARIAL_2026-06-25.md` + grid): 3 tripwire classes (synchronized-credit / single-name-credit / **NON-CREDIT balance-sheet** ≥2 of ZION/WAL/CFG/EGBN). **TWO-AXIS consumer/CRE model (CARL-ratified):** Axis A = unsecured/un-maskable/H2-26 = monolines SYF/ALLY + COF-card (LEAD); Axis B = collateral-backed/deferrable/Q1'27 = regional CRE terminus (my positions sit here). **COF = dual-axis standout** (only name with both on one B/S post-Discover); **CFG reclassified** strong-3-path-regional-but-Axis-B-only (18.7% consumer is housing-secured, NOT unsecured). Monoline-only break confirms Axis A, does NOT flip Axis-B terminus. **monoline LEAD COF/SYF/ALLY** print FIRST ~Jul15-22 (all GREEN 6/25, Axis-A turn not showing); **ZION re-registered** onto AOCI/NIM axis (10Y 4.41 [6/24], +11bp QoQ — re-pull 6/30 mark); **WAL magnitude-graded** — 40-45bps PRICED, bear-confirm >55bps+$99M-charge-off ~30-35% (NOT my prior ~70% — over-claim corrected); EGBN+AMTB ~25-35% JOINT + disjunctive (reserve-build IS Q2 transmission, realized NCO 2027).

**Threads carried (ROADMAP):** CCC/HY tripwire daily monitor (un-fired, 3-consec >3.6× = fire); **monoline LEAD prints ~Jul15-22** (earliest consumer-turn read); **ZION 6/30 AOCI/TBVPS re-pull**; Q2-grid forward confirmer = rising 30-89d FL resi/condo at ≥2 of {AMTB,SBCF,USCB} 2 consec Q; WAL Q2 magnitude watch (>55bps+charge-off); SSB FL-# resolves Q2/10-Q.

**Open for next session:** Pass-2 = wire CCC/HY consecutive-count check into scripts/boot.py (deferred); refresh STATUS prices (WAL $81.48 6/25, stale 6/22 block); refresh grid [PENDING] cells + AMTB/BKU 10-Q attribution at the Q2 prints; re-pull 6/30 quarter-end AOCI mark for ZION.

---

## 2026-06-22 — Boot refresh + STATUS-to-6/22 + SHADE Athene + DEWEY FL-timing

**Noticed during the session:**
- **"Oil-leg re-fire" was really a stall, not a re-fire.** Brent +3.45% on the day but ~flat vs Thursday ($80.69→$80.59) — a sharp up-day off a Friday dip, NOT a move back toward the $94 war premium. Reading the day-% as a trend would overstate it; the honest read decomposes the move from the level. Same family as the 6/19 CCC/HY-oscillation caution — don't read a single 2-day print as a trend.
- **DEWEY FL-bank-timing independently corroborated my 6/20 drill** on the BKU-vs-AMTB attribution (two surfaces converging via different evidence — my direct 10-Q pull vs DEWEY's institutional-mirror; my drill the higher grade since EDGAR 403'd DEWEY). New datapoint it added: SBCF CRE-NOO 224% of RBC.
- **CCC/HY tripwire flag recurring (3rd boot).** 3.56x today, oscillating in the 3.44-3.57 band every refresh. The 6/19 note flagged building a >3.6x-sustain tripwire so it stops being a prose judgment call each boot. Still flagged, not built — promote to a VX vector if it recurs once more.
- **WAL diverged WEAKER than the cohort** (−1.44% vs KRE +0.96%) — the cleanest single-day idiosyncratic-WAL tape signal we've had; closed $0.76 from the $78 threshold.

**Threads carried (all in ROADMAP):** WAL $78 threshold watch (new-live), CRE-DQ-by-tier Q2 build/revert, capital-rules final rule, MI3/FFIEC, APO Q1, OZK Call Report, CARL handover, PROME ZION-scaffold.

---

## 2026-06-20 — Recovery of orphaned 6/19 BOARD rows + CRE-DQ-by-tier drill

**Noticed during the session:**
- The CRE-DQ-by-tier question resolved cleaner than expected: it's a CRE-**CONCENTRATION** sort, not asset-size. OZK + EGBN (the 2 highest-CRE names) creep; BKU/SBCF (diversified) don't. SIG-009's "$16-40B tier" was a proxy for concentration — a Trepp asset-bucket cut can mask a concentration story. Worth remembering for future tier-based signals.
- **Reservoir-lag is the load-bearing concept.** OZK's NCO (0.57%) looks benign but past-due doubled and 88% is 5 CRE loans; the loss line lags the leading bucket 1-2 quarters. Reading NCO alone (the 6/8 cut) missed this — the drill's value was *switching metrics* (DQ leading vs NCO lagging), exactly what the 6/19 open question flagged.
- **Accepted the adversary's BKU hole.** I pulled BKU's nonaccrual (lagging) and called it RESOLVING but never pulled its 30-89 past-due (leading) — the bucket that moved at OZK. With only the OZK number I might've over-claimed tier-creep; with only BKU-resolving, over-claimed idiosyncratic. Honest read needs the leading bucket on BOTH; Q2 gets it. Good case for why the adversarial stage earns its cost.
- **OZK files no SEC 10-Q** — cost the subagent ~3 verification passes. Promoted to MEMORY Findings so the next OZK drill doesn't repeat the hunt.

**Threads carried (all in ROADMAP):** BKU 30-89 past-due Q2 falsifier, EGBN CRE-creep watch, Iran oil-leg re-firm (Mon 6/22), capital-rules final rule, MI3/FFIEC, APO Q1, OZK Call Report recheck.

---

## 2026-06-19 — Boot + 11-day-gap catch-up + BOARD CRE-credit mini-cluster [pruned stale 6/02 section >2wk; its threads live in ROADMAP]

**Noticed during the catch-up:**
- The CCC/HY "narrowing" framing I shipped 6/8 (3.48→3.44x) has **re-widened to 3.57x** on the 6/17 FRED refresh — HY tightened to 263bps faster than CCC came in. The bifurcation read keeps oscillating on the 2-day window; the durable statement is "tail lags the index rally," not a clean trend either way. If I keep re-litigating this every boot, it's a candidate for a CCC/HY-ratio tripwire (e.g. >3.6x sustain) so it stops being a prose judgment call. Flagged, not built.
- **IORB sanity-check caught a framing trap:** WALTER's BOARD signals repeatedly say "Fed flipped cut→HIKE 6/17." IORB is flat at 3.65 → no actual hike happened. It was a hawkish *guidance/dots* flip. Transcribing the signal's shorthand as "hike" would have been wrong. (Echoes [[finding_circular_corroboration_via_state_file]] / verify-from-raw-series.)
- **HY OAS 263 is 3bps from my own Exit-100% rule (<260).** Risk-on tape is quietly walking me toward my own exit trigger from the credit side while the CRE-fundamental side deteriorates. The bear can be "right on fundamentals, stopped out on credit spreads" — hold both in view.
- The Trepp CRE-DQ-by-tier signal (009) *looks* like it contradicts my 6/8 cohort finding but is a different metric (DQ vs NCO). Logged the distinction explicitly in STATUS + BOARD_LOG so a future read doesn't false-flag a contradiction.

**Threads carried (all in ROADMAP):** CRE-DQ-by-tier drill (new, OZK-cleanest), capital-rules final-rule watch (new), WAL $85P disposition flag (new) + prior: Juris banking, Slide 113 stress test, Slide 89 NDFI chart, Q&A transcript, life-sci #3, MI3/FFIEC, APO Q1, OZK 10-Q.

---

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
