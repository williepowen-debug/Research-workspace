# CARL SCRATCH
**Last session:** 2026-07-31 (Fri) ~20:15–20:45 ET — EVENING BOOT PASS (same-day re-boot after the ~16:25–19:30 main session + rulings). Drained the 4 late inbox packets, dispositioned 6 new BOARD signals, shipped STUE's LEDGER_GLOB fix, checked the HHDC advisory (not posted). **No score change: 51/70 holds.** THESIS v2.6.3.

**PRIORITY-1:** **Monday 8/3 is verify-and-execute, not a re-ask: verify the close (FRED weekly w/e 8/2 + AAA daily still ≥$4.00) → EXECUTE V5 3→4 (51→52/70, touches 5 surfaces per Check B) per Will's 7/31 pre-auth. Retrace <$4.00 = sustain failed, hold 3, report it.** Same day: Fitch ATR refresh (BEFORE the HHDC; Mar 6.11% is anchored on the seasonal LOW per OTTO's panel) + first EIA diesel print of the 8/3-8/17 lag experiment. The Q2 HHDC prints INSIDE 8/4-8/11 (**advisory NOT YET POSTED as of 7/31 eve — check every boot**; modal Tue 8/4) and grades by the FROZEN CARD + its 7/31 addenda, with CRL-21's capital riding the cells per the standing 7/24 ruling. CRL-28 is REGISTERED (FROZEN-at-55/day threshold); CRL-14 RETIRED. **NOTHING awaiting Will until the HHDC prints or NFP fires a V16 trigger.**

---

## CHANGES SINCE LAST SESSION (main 7/31 session → this evening pass)
- **STUE's carve-out commit LANDED** — its packet, SV, and sub-agent files are all committed; nothing to sweep. Sweet packet moved to processed/ (content was integrated in the main session).
- **BOARD 643→649 while offline (~1hr):** 6 new signals, all 7/31-dated, dispositioned this pass (see below).
- **VIX closed 15.99** — RED FT-06 (`<16` sustain 5) clock at session 1 of 5, earliest completion ~Thu 8/6 (SIG-731-001, RED's call whether session 1 counts — margin is one cent).
- **30Y closed 5.28% = new cycle high** (+18bp over 3 sessions; duration leg arming — BOND/HOMER/REGINALD lane).

## WHAT HAPPENED (this session)
1. **4 late inbox packets drained → inbox now 0 unprocessed:**
   - **HOMER (KB-304 HPI):** figures refreshed — C-S +1.1% May (Apr revised +0.9), FHFA +2.2% record, FMHPI "Mar 0.7" trough **REVISED AWAY** (trough = Jan 0.9; acceleration flatter/longer, conclusion survives). Leading-edge caveat: C-S SA MoM negative ×3 consecutive. FHFA runs ~110bps hotter than C-S — never cite interchangeably. **Plus: Fannie MF "improvement" (0.60% Q2 10-Q) is a RECOGNITION ARTIFACT** (mod-of-forbearance per Fannie's own 10-Q, provision +49% QoQ, Freddie went the other way) → caveat on KB-302 + STATUS V3 row. Does NOT reopen CRL-03.
   - **MARCO (Channel-1):** immigration cost-push **UNSUPPORTED FULL STOP** (pre-registered floor-controlled test NULL under both controls; no 4th attempt — CES can't see the off-payroll population). **Sep-30 FL $15 statutory impulse UNAFFECTED and stands** (KB-368 note). PROME caution honored: the "FL diagnostic STRENGTHENED" sentence NOT adopted — **and MARCO's second packet (landed mid-pass) RETRACTED it: scored MISS** (pre-reg said FL DID ≈0 if floor-driven; observed +6.89pp, June an outlier driven by the control sector; AL/LA beat FL with no floor step). CARL carried nothing → nothing to remove. **~6pp rule RE-SCOPED: stratum-means only; single-state band ~11.5pp.** Both MARCO packets → processed/. The refusal-until-scored pattern paid off within 3 hours.
   - **STUE (ledger enforcement):** **Fix A TAKEN — `workbook/LEDGER_GLOB` created + verified** (37 sub-agent ledgers now inside `ledger_staleness` scanning; patterns on separate lines per STUE's arity warning). First run surfaced **DOC FLOW.tsv 53d stale** → TEAM DOC row noted, FROZEN-or-refresh at next DOC spawn. Fix B (consistency_check coverage for prediction-less sub-agents) → backlog row, option 2 (advisory-on-missing) leading.
   - **STUE (Sweet):** already integrated in the main session — moved to processed/.
2. **BOARD 6/6 dispositioned (651 rows, 0 backlog, 0 dupes):** 1 INTEGRATED — SIG-731-002 **Apple raised consumer device prices on memory cost-push** (LTA-capped hyperscalers shift the increase to non-LTA customers = consumers; "100-year flood on memory pricing," 14 products) → **KB-371**, V7 small-weight wrinkle, MU 8/4 resolves AI-vs-consumer split. 5 REFERRED (VIX/RED · Volgograd/OSPREY — channel read consistent with the diesel-lag experiment · yen/SAM · G10 liquidity/LIQUID · 30Y/BOND).
3. **HHDC advisory checked: NOT POSTED** (newyorkfed.org advisory page + search; nothing newer than the Q1 5/12 release). Modal Tue 8/4 unconfirmed.

## STATUS CHANGES
| Item | Change |
|------|--------|
| V3 matrix row | + 7/31 HOMER recognition-artifact caveat (do not carry "GSE MF improving" as clean) |
| KB-304 | HPI figures refreshed; trough corrected Mar-0.7→Jan-0.9; Stale_By 9/15 |
| KB-368 | Channel-1 UNSUPPORTED full stop; statutory impulse stands; PROME caution noted |
| KB-371 | NEW — Apple memory cost-push into consumer devices (V7, small weight) |
| TEAM DOC row | ⚠️ FLOW.tsv 53d stale — FROZEN-or-refresh at next DOC spawn |
| workbook/LEDGER_GLOB | NEW — sub-agent ledgers now staleness-enforced |

---

## NEXT SESSION SHOULD

### IMMEDIATE (Mon 8/3 — the window)
1. **Verify the close (FRED weekly w/e 8/2 + AAA daily ≥$4.00) → EXECUTE V5 3→4 per the pre-auth — NO ASK.** Retrace = hold 3, report. (8/3 is a MONDAY.)
2. **Fitch ATR refresh** (V2's instrument, Jan-vintage; Mar print = seasonal LOW — OTTO panel context in STATUS row) + **first EIA diesel print** of the 8/3-8/17 lag experiment (Volgograd/Perm strikes are product-bullish per OSPREY — tailwind context for the crack, noted in BOARD_LOG).
3. **Every boot: check the NY Fed HHDC media advisory** (newyorkfed.org/newsevents/mediaadvisory — 403s to fetch, use search) — pin the exact date in 8/4-8/11.
4. **Read DEWEY C2 (`AGENTS/DEWEY/output/2026-07-24_c2-score-cascade-cc-breach-attribution.md`) BEFORE the HHDC** — cautions pre-registered on the card (addendum #2) but the full report is unread.

### DATED
5. **STUE hand-downs at its next run (PROME audit items 5+6b):** (i) VASP confound in STUE STATUS:221/293 + CASCADE.tsv:11 is a CATEGORY ERROR (11.88% is FHA-only, VASP is VA; DEWEY :69) → remove the false blocker on STUE Q#11; candidate real confound = HUD ML 2025-06 partial-claim waterfall; data hook = HUD Neighborhood Watch geographic cut (coord w/ HOMER); (ii) STUE STATUS:182 "monotone score-drop law" contradicted by its own table — delete/reword.
6. **~8/5** Treasury Phase 1 verification (STUE) · **8/7 July NFP — V16 re-arm resolver** · **8/12 July CPI (pre-registered SOFT — do not grade pass-through)** · **~8/14 AFT v. MOHELA free docket watch** (CourtListener text via curl+browser-UA; method in the CATALYSTS row) · **~8/15 Russia-ban test** (ban EXTENDED per RED — grade the crack vs 5-yr seasonal norm) · **8/20-21** Affirm FQ4 + Iran waiver expiry (CRL-08 45% live tail) · **~early Sept: CRMT covenant-relief expiry** (REGINALD co-owns).

### BACKLOG
7. Fix B (consistency_check sub-agent coverage — option 2 leading) · CPI component-vol REBUILD from BLS (SIG-725-016 — cite nothing until rebuilt) · Part D lead verify (DOC/POLLY) · AMCAR Apr-vs-Jun cert pull + abs_monitor GMCAR label fix · Brier re-run at N≈20 · container-freight AEOLUS reconcile (KB-344).

---

## OUTBOX (0 new; 6 stale Apr-17 signals deferred per messaging-overhaul direction)
## INBOX (0 unprocessed — all 4 drained this pass, moved to processed/)

---

## WORKBOOK HEALTH
| File | Size | Note |
|---|---|---|
| STATUS.md | 248 | under cap |
| KB.tsv | 368 lines | +1 this session (KB-371); 304/302/368 refreshed in place |
| PREDICTIONS.tsv | 29 | 16 OPEN incl. CRL-28 · CRL-14 RETIRED |
| CATALYSTS.tsv | 20 | 0 past-due |
| BOARD_LOG.tsv | 651 | 0 backlog, 0 dupes (through SIG-731-006) |
| PAPER_SLEEVE.tsv | 11 | 7 legs OPEN, marked 7/31, net +$9.43 |
| MEMORY.md | 71 | under 100 cap |
| LEDGER_GLOB | NEW | 37 sub-agent ledgers scanned; 1 stale (DOC FLOW.tsv → DOC next spawn) |

---

## URGENT
- **Monday 8/3 = V5 verify-and-execute (pre-authorized — no ask). The HHDC can land as early as Tuesday 8/4.** Fitch ATR must be refreshed before it.
- **The frozen card + 7/31 addenda govern the HHDC grade — do not edit the card, only dated addenda.** RED's rationalization test is live on it.
- **"CRMT defaulted" is retired language — covenant waiver, ~Sept expiry.** Do not let it re-enter synthesis.
- **Do not carry "GSE MF improving" as a clean signal** — recognition artifact (HOMER 7/31, KB-302).
