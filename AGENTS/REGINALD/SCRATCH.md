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

## 2026-07-17 — Boot + CFG print read + tripwire fire-fade + 3-packet integration

**Noticed during the session:**
- **The tripwire's pre-registered driver-decomp rule earned its keep.** VX-REG-18.04 technically hard-fired 7/13 (3 consec >3.6×: 3.607/3.606/3.613 — all within 0.013 of the line) then reset 7/14. Without the 6/25-built decomp rule ("HY-tightening=beta=no escalate") I'd have faced a judgment call on escalating a marginal, already-faded fire; the rule pre-decided it. The design lesson: the escalation clause keying on the DRIVER (CCC-led vs HY-led), not just the level, is what kept a denominator artifact from becoming a false 🔴 to LIQUID/BROCK.
- **CFG −3.27% the day AFTER a clean beat** — on a broad risk-off tape (SPY −1%, KRE −2.1%, VIX +9.8%). Post-beat profit-taking + beta. Watch that Monday: a WAL/OZK sell-off into/after the print needs the same beta-vs-substance decomposition before reading it as thesis-confirming.
- **Brent +$11.67/wk and the 7/10 "sustain verdict" framing is overtaken** — the question was whether $76 sustains; the tape answered with $87.67. HAWK/BRENT own the verdict; my STATUS rows now carry the escalation read (oil leg FIRING).
- **WALTER's BB/B sub-index gap flag (SIG-717-003) is worth remembering when citing REG-T-03/04:** blended HY at 8.3 pctile while CCC at 87.8 pctile — the blended >320/>350 triggers may lag a tail-led break. Not actionable now; lane fix is PROME's.

**Threads carried (ROADMAP):** 7/21 double-print grading (frames done, ALLY pin added); POSITIONS broker refresh gate; BROCK bank→BDC map fill (CFG data now in hand); post-7/21 rewrite buckets.

---

## 2026-07-10 — Core-files staleness sweep + triaged remediation

**Noticed during the session:**
- **PAT-043 in the wild.** The audit's headline — live thesis in STATUS, thesis-of-record fossilized — is exactly decay-from-the-durable-end. The tell: refresh loops touch STATUS because it's convenient mid-session; THESIS/TIMELINE/INDEX/MATRIX only move on a deliberate rewrite that never gets scheduled. Banner-guard is the cheap interim; the real fix is *scheduling* the rewrite (post-7/21).
- **The two-clock header silences its own nag.** Adding a STALE-VINTAGE header to KB/FLOW resets the git-commit-time the staleness script keys on → boot-7a stops flagging them. Caught it before committing; moved the refresh-debt to a ROADMAP thread so it's not lost. The human-readable "Last real data refresh" date is the honest artifact, but you MUST re-home the auto-nag or it vanishes (PAT-044 laundering).
- **CCC/HY quietly walked back to the tripwire line.** 3.49× [6/24] → 3.61× [7/9], AT the 3.6× line, ARMED 1-of-3. But the driver is HY compression (270 vs 276 6/24), not a CCC blowout — a denominator-shrink move, beta-ish, not tail-substance. Don't over-read the single close. *(RESOLVED 7/17: it went on to complete the 3-consec fire 7/13 then reset 7/14 — graded beta/benign per the decomp rule, no escalation. See 7/17 section + VX.tsv.)*

**Threads carried (ROADMAP):** post-Jul-21 thesis-of-record rewrite (bucket 2) + KB reconstruction (bucket 3); VX-REG-18.04 X1-root reframe; inbox (2 PROME + 5 WALTER) not processed.

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

*(6/22 section pruned 2026-07-17; 6/20 + 6/19 pruned 2026-07-10 — >2wk, substance in ROADMAP Recently Resolved / MEMORY Findings.)*

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
