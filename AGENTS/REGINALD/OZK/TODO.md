# OZK — Research TODO / Backlog

**Last updated:** 2026-04-23 (boot + STATUS refresh + subdir staleness audit)
**Source:** Follow-up threads identified during Threads 1 and 2 deep dives; plus subdir hygiene queue added Apr 23.

**Strategic framing:** Thread 3 roll math exists ($42.5P × 2 May → Jan27 $42.5P × 2) but Will is holding off on execution as of Apr 23 — decision open past May 8 is a de-facto expiry. Watch the dated checkpoints fire (Bluerock Q1 marks May-Jun, Aimco motion early Jun). **Decide on adjacent-thread research based on whether the core IQHQ thesis is validating or invalidating.** Avoid pre-committing research hours to #2 (Bluerock) and #3 (WAL IQHQ) before the core thesis resolves.

---

## HIGH PRIORITY — material thesis impact

### 1. Boston Life Sci $169M sponsor disambiguation
**Why:** Single largest unresolved Q1 26 OZK problem credit. One credit = 27% of OZK's total $628M ACL. Sponsor ID changes recovery math materially.
**Status:** Narrowed to 2 candidates in `SEVEN_CREDIT_DEEP_DIVE.md` §2 #5:
- **10 Prospect Street, Union Square Somerville** — sponsor US2 (Magellan + Cathartes + RAS Development), orig $119M Feb 2021, 194K SF spec lab
- **808 Windsor / Boynton Yards Somerville** — sponsor Leggat McCall + DLJ Real Estate + Deutsche Finance America, orig $246M Dec 2021, 370K SF 96% vacant

**Where to look:**
- Middlesex County ROD mortgage assignments filed post-Q4 2025 (MassLandRecords.com)
- OZK 10-Q (~May 5) — MD&A footnotes may disclose
- Q2 26 earnings call July — Citi/Piper/Stephens have pressed repeatedly

**Estimate:** 1 hour
**Output:** Update SEVEN_CREDIT_DEEP_DIVE.md #5 with confirmed sponsor; new KB row; signal to CREED

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

### 4. OZK's unnamed ~$500M classified/criticized exposure
**Why:** Q1 26 total classified+criticized = $1.215B. The 11 credits we tracked = $719M. **~$496M classified/criticized we haven't mapped by project.** Could be special-mention, small granular classified, or watchlist items not in Figure 24.

**Where to look:**
- Q1 26 Financial Supplement + Management Comments (`raw/`) — re-scan for special-mention detail beyond Figure 24
- OZK Call Report RC-N (noncurrent loans) filed May 1-10 — finer breakdown
- Q4 vs Q1 special-mention migration delta

**Estimate:** 1-2 hours
**Output:** Supplementary section in SEVEN_CREDIT_DEEP_DIVE.md on "the rest of the problem book"

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

### 7. "The Jack" vs Pioneer Square verification ($25.9M)
MEDIUM confidence ID in SEVEN_CREDIT_DEEP_DIVE.md #3. King County records check for OZK mortgage on Seattle Pioneer Sq office. 20-30 min. Low dollar impact.

### 8. Severity comp refresh (stale-by 2026-07-31)
KB-OZK-177 severity bands need Q2 26 distressed CRE transaction refresh. Quarterly cadence. Schedule for late July.

### 9. OZK $350M offensive FHLB carry trade — management psychology note
Why did OZK go offensive when MTB/CFG/PNC went defensive? 1 hour of reflection, Q1 Management Comments re-read. Note in THESIS.md or STATUS about management tempo.

### 10. OZK Consumer RV/Marine tracking cadence
Currently 0.42% NCO super-prime clean. Quarterly earnings tracking. Inflection = leading indicator for consumer channel firing at OZK. Add to PREDICTIONS.tsv.

---

## File Hygiene — Subdir Refresh Queue (added Apr 23)

Identified via boot-time staleness audit. All four subdirs had mtime Apr 23 (Phase 3 restructure touches) but content is pre-Q1. Cold-boot agents reading these get stale thesis input.

| Subdir | Content date | Severity | What Q1 adds |
|---|---|---|---|
| **LIFE_SCI/** | 2026-03-25 | 🔴 Biggest gap | 4 new life sci credits (Boston $169M, Seattle U Dist $50M, Chicago foreclosed $50M) + IQHQ Aug 2026 date correction |
| **PRIVATE_CREDIT/** | 2026-03-24 | 🔴 Thesis-contradicting | Jake Munn disclosed OZK **pulling back** from Fund Finance capital-call subs — contradicts the subdir's core "lends to the lenders" framing |
| **GEOGRAPHY/** | 2026-03-24 | 🟠 Additive | 3 new metro-specific stress points (Seattle U Dist, Santa Monica 15% leased, Chicago Life Sci foreclosed) |
| **INSIDERS/** | 2026-04-12 | 🟢 Skippable | No material Q1 insider activity per KB. Skip this session. |

**Estimate:** LIFE_SCI 45 min · PRIVATE_CREDIT 30-45 min · GEOGRAPHY 20-30 min · INSIDERS skip
**Recommended order:** LIFE_SCI → PRIVATE_CREDIT → GEOGRAPHY
**Output:** Each subdir STATUS.md updated with Q1 26 actuals, new credits, and (PRIVATE_CREDIT) reframed narrative to accommodate Jake Munn pullback.

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

---

## Decision gate — after Thread 3

**If IQHQ thesis validating** (Bluerock marks down, Aimco motion denied, RaDD still 3.3% leased): escalate #2 (Bluerock) + #3 (WAL IQHQ) for multi-leg short expression.

**If IQHQ thesis deflating** (RaDD lease signing, Aimco motion granted, IQHQ raises new capital): de-prioritize #2 + #3, focus on #1 (Boston Life Sci ID) and #4 (unnamed classified/criticized) to surface new risk concentrations.

---

*Related docs: `SEVEN_CREDIT_DEEP_DIVE.md`, `IQHQ_PLAYBOOK.md`, `../MEMORY.md` (session handoff), `../CALENDAR.md` (dated checkpoints).*
