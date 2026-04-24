# OZK — Research TODO / Backlog

**Last updated:** 2026-04-23 (afternoon session — subdir refresh queue cleared, gap supplement integrated, KB +7 rows)
**Source:** Follow-up threads identified during Threads 1 and 2 deep dives; plus subdir hygiene queue added Apr 23 (now cleared).

**Strategic framing:** Thread 3 roll math exists ($42.5P × 2 May → Jan27 $42.5P × 2) but Will is holding off on execution as of Apr 23 — decision open past May 8 is a de-facto expiry. Watch the dated checkpoints fire (Bluerock Q1 marks May-Jun, Aimco motion early Jun). **Decide on adjacent-thread research based on whether the core IQHQ thesis is validating or invalidating.** Avoid pre-committing research hours to #2 (Bluerock) and #3 (WAL IQHQ) before the core thesis resolves.

---

## HIGH PRIORITY — material thesis impact

### 1. Boston Life Sci $169M sponsor disambiguation — ✅ RESOLVED HIGH (2026-04-23 PM)

**Verdict:** **10 Prospect Street, Somerville / USQ Parcel D2.1 / Magellan + RAS + Cypress + Affinius JV.** Confirmed via MassLandRecords Middlesex South UCC-1 Financing Statement Bk 85169 Pg 222, Doc #9975, filed Jan 29, 2026. Debtor = 31 Union Square D2.1 Owner LLC; Secured Party = Bank OZK; underlying lien instrument dated Dec 31, 2020 (original mortgage at Bk 76638 Pg 224).

**Maturity-mismatch resolved:** the Dec 31, 2020 lien date + 5yr term = Dec 31, 2025 anniversary, within normal docs variance of OZK's disclosed Dec 18, 2025 maturity. Prior "Feb 1, 2021" date was the press/closing announcement, not the docs date.

**Workout interpretation:** Jan 29, 2026 UCC-1 re-perfection six weeks after maturity is a classic early-workout security-interest refresh — locking in lien priority before any enforcement action. Not foreclosure initiation; aggressive posture short of it.

**Severity revision:** Magellan + RAS + Cypress + Affinius is a well-capitalized institutional JV (Magellan = large Chicago mixed-use developer; Affinius = ~$80B AUM). Workout-path probability > forced-note-sale probability → severity biases toward LOWER end of 25-40% band (~$35-55M loss vs prior $40-65M).

**Full detail → SEVEN_CREDIT_DEEP_DIVE.md §2 #5. KB rows: 195 (verdict), 194 (sponsor correction), 189 (Q1 26 substandard status update).**

**Follow-up (optional, not blocking):** Pull original Mortgage / Security Agreement Bk 76638 Pg 224 for original loan amount, stated maturity, rate, extension provisions.

---

### 2. Bluerock as secondary short candidate
**Why:** Bluerock (NYSE-listed) holds $246M PIK loans to IQHQ (13.5-14%, accruing ~$8-9M/qtr unpaid) + significant equity (>$700M total exposure). If RaDD fails, Bluerock takes material hit. **Potentially cleaner IQHQ-fail trade than OZK** — avoids OZK's buyback squeeze risk, extension risk, offsetting CIB strength.
**Status:** Outbox to BROCK sent Apr 22 (`outbox/2026-04-22_to-BROCK_...`). No REGINALD ticker-level research yet.

**Where to look:**
- Bluerock Homes Trust — verify current ticker (formerly BHM, may have changed post-restructuring)
- Q1 2026 10-Q / NAV marks (expected May-Jun)
- Prior: "Bluerock 40% first-day trading loss" on NYSE listing — unconfirmed
- Aimco complaint alleges Bluerock PIK structure is "conflicted financings" — fiduciary exposure for Bluerock directors
- NexPoint / Highland Capital marks on IQHQ (Bluerock parent complex)

**Estimate:** 2 hours
**Output:** `OZK/BLUEROCK_EXPOSURE.md` — entity structure, exposure sizing, thesis expression, options chain, position sizing

**Gate:** Only pursue if Bluerock's Q1 2026 NAV mark (May-Jun) confirms further IQHQ markdown. If no markdown, thesis expression thins out.

---

### 3. WAL's IQHQ exposure (if any)
**Why:** If WAL has IQHQ-related construction loans, sponsor distress cascades across multiple regional lenders, amplifying the short signal. Fits V3/NDFI thesis.
**Status:** WAL Investor Day **May 12** — possible disclosure point. Not researched.

**Where to look:**
- WAL 10-K construction/CRE schedules
- WAL Investor Day May 12 webcast / deck
- Prior REGINALD WAL CRE exposure files
- Cross-reference of IQHQ lenders (trade press, CMBS loan-level data)

**Estimate:** 30-60 min
**Output:** `WAL/` update or STATUS note; cross-signal if material

---

## MEDIUM PRIORITY — fills gaps, reduces noise

### 4. OZK's unnamed ~$495M classified/criticized exposure — ✅ CHARACTERIZED Apr 23 PM (gap decomposition complete, source IDs still deferred)

**Resolution this session (Apr 23 PM):** Q1 Mgmt Comments + Financial Supplement re-scanned via spawn audit. Gap decomposed: Special Mention $397M (fully opaque at project level, resolvable only at May 1-10 Call Report RC-N) + ~$57M sub-threshold RESG substandard non-accrual + ~$37M sub-threshold substandard accrual + ~$4M foreclosed (rounding). Plus non-RESG blind spot (CIB / Community Banking / Indirect RV&Marine) — implied near-zero but not itemized. Full decomposition → `SEVEN_CREDIT_DEEP_DIVE.md` §3A.

**What remains (deferred to May):**
- May 1-10 Q1 Call Report FFIEC RC-N — triage Special Mention by asset class / geography. Not a research sprint; a 30-60 min read-and-triage pass when filings appear.
- 10-Q (~May 5) — verify near-zero classified in CIB / Community Banking / Indirect (quick MD&A scan, not a project).
- Q2 26 Figure 24 — watch for new sub-threshold RESG names migrating up into disclosure (cohort-migration tell).

**Research prioritization conclusion:** Do NOT chase Special Mention through forensic work — labor-to-signal ratio poor. Wait for Call Report. (See §3A for full reasoning.)

---

### 5. Affinius Oct 2026 $2.7B bond maturity — verify or remove
**Why:** CALENDAR tracks as OZK catalyst. NOT mentioned on Apr 22 Q1 call. Prior research may have conflated Affinius (private RIA) with USAA Capital Corp.
**Status:** CREED outbox sent Apr 22 (`outbox/2026-04-22_to-CREED_...`).

**Where to look:** CREED response; USAA Capital Corp bond maturity schedule; direct Affinius CUSIP search

**Estimate:** 30 min if CREED responds; 1 hour self-resolve
**Output:** Remove from CALENDAR if false flag; otherwise note verified exposure

---

### 6. LP-dissolution pattern expansion (cross-bank screen)
**Why:** Lionstone/Ameriprise wind-down ($5.5B book) was the forcing function on Chapter Buildings. New pattern. If other RE advisors consolidate/wind down, similar loans land on bank problem lists.
**Status:** BROCK outbox sent Apr 22. **BROCK's domain** — not REGINALD direct work.

**Screen candidates (for BROCK):** Clarion Partners, Invesco RE, Nuveen RE (TIAA), MetLife IM Real Estate, JPMorgan AM Real Estate, AEW Capital

**Estimate:** 2-3 hours (BROCK scope)
**Output:** Cross-bank screen in BROCK/ scope

---

## LOWER PRIORITY — housekeeping

### 7. "The Jack" vs Pioneer Square verification ($25.9M) — ✅ RESOLVED Apr 23 PM
HIGH confidence: **74 S Jackson St, Urban Visions sponsor, 145K SF class A office, delivered 2023, 100% vacant.** OZK took out Mack Real Estate Credit Strategies' original $90M construction loan (Feb 2022, JLL-arranged). OZK commitment $72.5M. Math reconciles exactly ($56.2M Q4 24 − $27.7M Q1 charge-off − $2.6M sponsor paydown = $25.9M). Bisnow Sep 2025 direct naming + SEVEN_CREDIT §2 #3 updated + KB-OZK-193.

### 8. Severity comp refresh (stale-by 2026-07-31)
KB-OZK-177 severity bands need Q2 26 distressed CRE transaction refresh. Quarterly cadence. Schedule for late July.

### 9. OZK $350M offensive FHLB carry trade — management psychology note
Why did OZK go offensive when MTB/CFG/PNC went defensive? 1 hour of reflection, Q1 Management Comments re-read. Note in THESIS.md or STATUS about management tempo.

### 10. OZK Consumer RV/Marine tracking cadence
Currently 0.42% NCO super-prime clean. Quarterly earnings tracking. Inflection = leading indicator for consumer channel firing at OZK. Add to PREDICTIONS.tsv.

---

## File Hygiene — Subdir Refresh Queue (added Apr 23 AM, ✅ CLEARED Apr 23 PM)

| Subdir | Status | What changed |
|---|---|---|
| **LIFE_SCI/** | ✅ DONE Apr 23 PM | IQHQ maturity corrected Aug 2028 → Aug 2026 across README/STATUS/FINDINGS (Finding 2 rewritten, marked as research error). 3 new Q1 26 credits integrated (Finding 18). KB rows 189-191. |
| **PRIVATE_CREDIT/** | ✅ DONE Apr 23 PM | Jake Munn Fund Finance pullback + LFG compression + asymmetric disclosure (spoken not written) added to NDFI_EXPOSURE.md (Q1 Update section), TRANSMISSION.md (Channel 3 amplifier), STATUS.md + README.md (bidirectional "lends to AND competes with" framing). Structural analysis preserved. KB rows 186-188. |
| **GEOGRAPHY/** | ✅ DONE Apr 23 PM | 3 new metro stress points added (Seattle U Dist $127M, Santa Monica $45M foreclosed, Chicago Life Sci $50M foreclosed). Distressed cluster total $2.9B → $3.1-3.3B. KB row 192 (Santa Monica). |
| **INSIDERS/** | ⏸️ Skipped (as planned) | No material Q1 insider activity. |

---

## Known Staleness — Deferred (not session scope)

### H1. `workbook/KB_INDEX.md` significantly behind
Index header says "Total rows: 159 | Groups: 17" but actual KB.tsv has 192 data rows. Rows 160-192 not reflected in any group listing (prompt 20 Q1 integration + Apr 7 consensus work + Apr 22-23 sponsor/structural work + Apr 23 PM session). 30-60 min to update rollups if/when it becomes blocking. **Not currently blocking** — everyone reads via KB.tsv directly or through named files, not the index.

---

## Position Management (added Apr 23)

### P1. May $47.5P × 2 — decision by May 8
**Why:** New position (not in prior files), 22 DTE, ~$0.73 OTM at $48.23. Original rationale (Apr earnings) expired; current implicit rationale is May 1-10 Call Report window (MI3/NDFI reveal). No system roll math exists.
**Status:** Open. Not covered by THREAD3_ROLL_MATH.md.
**Decide between:** (a) hold through Call Report and close, (b) roll forward if CR disclosure fires thesis, (c) let expire if CR is a non-event.
**Estimate:** 30 min of decision math if a roll is wanted; otherwise a watch-item.

---

## Already-in-flight (don't re-spawn)

- **Thread 3 roll: $42.5P × 2 May → Jan27 $42.5P × 2** — math in `THREAD3_ROLL_MATH.md`. **Will holding off on execution (Apr 23).** De-facto expiry May 15 if no action by May 8.
- ✅ **OZK/STATUS.md focused refresh** — DONE Apr 23 (118 → 72 lines; all Q1 26 actuals, IQHQ Aug 2026 correction, sub notes Oct 1 reprice added; ownership violations removed).
- ✅ **OZK/INDEX.md header fix** — DONE Apr 23 (v1.1 → v1.3 across header + File Map).
- ✅ **OZK/THESIS.md NCO-framing revision** — DONE in v1.3 audit (Apr 23, committed `9322e2cc`).
- ✅ **Subdir refresh (LIFE_SCI, PRIVATE_CREDIT, GEOGRAPHY)** — DONE Apr 23 PM. See File Hygiene section above.
- ✅ **$495M gap characterization** — DONE Apr 23 PM. Integrated as SEVEN_CREDIT_DEEP_DIVE.md §3A.
- ✅ **KB.tsv +7 rows (186-192)** — DONE Apr 23 PM. Jake Munn trio + 4 Q1 26 credits.

---

## Decision gate — after Thread 3

**If IQHQ thesis validating** (Bluerock marks down, Aimco motion denied, RaDD still 3.3% leased): escalate #2 (Bluerock) + #3 (WAL IQHQ) for multi-leg short expression.

**If IQHQ thesis deflating** (RaDD lease signing, Aimco motion granted, IQHQ raises new capital): de-prioritize #2 + #3, focus on #1 (Boston Life Sci ID) and #4 (unnamed classified/criticized) to surface new risk concentrations.

---

*Related docs: `SEVEN_CREDIT_DEEP_DIVE.md`, `IQHQ_PLAYBOOK.md`, `MEMORY.md` (session handoff), `CALENDAR.md` (dated checkpoints).*
