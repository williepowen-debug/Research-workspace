# WAL — Memory

## Session Notes

**⚠️ Open question:** **WAL-02's invalidation clause is unreachable and needs Will's call.** The row reads *"exceeds 40bps in at least one of Q2 or Q3"* with invalidation *"stays at or below 35bps in BOTH Q2 and Q3."* Q2 printed **37bps** — above 35, below 40 — so the invalidation path can no longer be satisfied and a Q3 print in the 35-40 band leaves the row with no defined outcome. The 50% mark itself is sound (Stage-2 set it 7/22 *after* the 37bps print, so it is already a Q3-only mark); the stale text is the **Invalidation column only**. Proposed fix, NOT applied — it is a graded row: rewrite invalidation to *"Q3 2026 ex-fraud NCO ≤40bps"* + note Q2 resolved 37bps NEUTRAL. Confidence unchanged.

**LAST SESSION (2026-07-25 — WAL session #1, first solo session ever; mandates #2 and #1 executed):**
- **#2 KB Q2 ingest — DONE, call was INGEST (not freeze).** 22 rows **KB-WAL-106..127**, 105 → **127 rows / 16 groups**. Sourced off 8-K acc 0001628280-26-049001 (EX-99.1 + EX-99.2 slide images 12/13/24) + the 7/22 call transcript, via REGINALD's two grade reports. Data clock **82d → 0d**; two-clock header advanced on BOTH clocks (legitimate — real data landed, PAT-044 satisfied).
- Coverage: leading buckets reversed (106-107) · office classified $316M + book structure + zero migrations + $99M letter (B) + ACL/NPL 96% + classified-composition trap (108-114) · Q2 earnings/guide/deposit-cost (115-118, 122) · buyback + AOCI (119-120) · NDFI shrinking (121) · Cantor silence + reconcile, LAM closed (123-124) · tape + short interest (125-126) · **MI3 still unrun (127)**.
- **Hygiene closed in the same pass:** KB-WAL-056/057 column drift (stray 14th field) FIXED — file now uniformly 13 columns, 127/127 verified. `KB_INDEX.md` fully rewritten (group map, V1a/V1b split, thesis-layer mapping, post-Q2 quick-reference, staleness table, source-tier convention).
- **#1 Standup handles — RATIFIED WITH RE-SCORES.** Convergence matrix: **V1b SPLIT** into broadening **2/5** (disconfirmed) vs magnitude **4/5** (active, on the new 5Q-high $32.0M CRE-NOO charge-off) — the seeded single 2/5 collapsed two mechanisms moving in opposite directions. **V3 2→1** (lone confirming sub-vector now shrinking by mgmt choice). **V2 EXCLUDED from composite** (closed P&L arc was inflating a bear read). **V4 marked PROVISIONAL** (rests on an unverified insider leg). Live-bear composite restated **15/25 → 13/25**.
- Exit rules: every rule now names its **carrying instrument**; **bear-fast TIME-BOX added** (3rd consecutive FFIEC miss forces a disposition call ~Sep 1); **N=3 defined** for thesis-retire (earliest ~Jan 2027, not late Oct as seeded).
- ★ **Best catch of the session: the Q2 10-Q (~Aug 7-10) was missing from BOTH the catalyst table and expected-signals.** The whole file said "everything funnels to Q3" while the nearest forward event sat ~2 weeks out carrying three owed tie-outs. Added to both tables.
- Price tokens synced (header + Buffer) to **$83.11 / +$5.11**. INDEX mirror re-synced (KB 105→127, next-event token). Open Threads re-triaged 7 → 10 items.

**NEXT SESSION (numbered, checkable):**
1. **Will's call on the WAL-02 invalidation clause** (see Open question). Blocked on him, not on me.
2. **Q2 10-Q when it lands ~Aug 7-10** — three tie-outs: business-credit line $3,415M (KB-WAL-121) · Cantor three-figure footnote (123) · **EPS $2.36/$2.33 basis vs EX-99.1 (115)**. Pre-register a mini-frame against the 10-Q *as the carrying filing*.
3. **Form 4 post-print insider sweep** — overdue since April; V4's 3/5 is provisional until this runs. Cheap, do it early.
4. **⏱ FFIEC Q2 PDD watch (~Aug) — TIME-BOX ARMED.** If the window passes unintegrated, execute the forced bear-fast disposition call (substitute instrument / fold into bear-medium / carry as acknowledged-untestable with written justification). No fourth deferral.
5. **Strike-by-strike position architecture rebuild** (SCENARIOS May-vintage) — Sep-18 expiry is the forcing date; carried mandate, still open.
6. **boot.py first increment** — price + catalyst countdown + inbox count + staleness in one pass; wire into CLAUDE.md boot the SAME session it is built (PAT-041). *Session #1 evidence it is worth building: the price token was 2 sessions stale at boot and I caught it by hand.*
7. **Re-pin NEXUS_BRIEF** as an owner pin + ask NEXUS for a BRIEFS_MAP row (carried mandate, not done).
8. **Q3 frame-spec** — pre-register against the filing that carries each metric (carried mandate #6; the principle is now applied in STATUS exit rules, but the Q3 frame itself is unwritten).

**Feedback:** *(none yet — first Will correction/confirmation earns the first row)*

**Findings:**
- **Source-tier discipline pays at ingest:** the Q2 EPS pair ($2.36 vs $2.33 cons) that THESIS v2.3 cites as "print landed base-case" appears in **neither** grade report — only in the CHANGELOG entry — and its GAAP-vs-adjusted basis is unpinned. Q1 printed a GAAP *miss* alongside an adjusted *beat*, so the basis is load-bearing. Writing every KB row with an explicit A1/A2 tier is what surfaced it. Logged as KB-WAL-115 with a tie-out instruction rather than silently promoted to A1.
- **A seeded convergence score can hide a sign flip.** DAEDALUS's single "V1b Office migration 2/5" was defensible on its own label but collapsed broadening (disconfirmed) and magnitude (intensifying) into one number — and THESIS v2.3's own prose separates them. A cross-agent reader taking the one-line composite would have read "bear mostly died." Ratifying a seeded handle means re-deriving what it *measures*, not just whether the number feels right.
- **A never-running falsifier needs a time-box, not patience.** Bear-fast sat at 10% across 4 months and 2 missed FFIEC windows with zero confirmations *and* zero disconfirmations. Carrying weight on an untestable premise indefinitely is not neutrality. The fix is a dated forced-disposition rule, not another deferral.
- FDIC/SEC: WAL is NYSE-listed — insider filings on SEC EDGAR (unlike peer OZK, which files with FDIC EFR cert #110).
- Boot-tool yfinance short interest is bad for WAL (7,144 sh / 0.01% shown vs FINRA 4.91% [6/30] canonical) — never cite the tool's SI. (Inherited from REGINALD 7/25; now also pinned as KB-WAL-126.)
- The frozen frames (`Q2_GRADING_FRAME_2026-07-21.md`, `PREPRINT_RECON_2026-07-17.md`) intentionally carry superseded-looking confidences (65/72/33) — they are the pre-registration calibration record; path fixes only, content never.

**References:** promotion review → `../DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md` · Q2 grades → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md` + `2026-07-22_WAL_Q2_stage2_grade.md` (REGINALD-side; WAL cites, never moves) · shared Jefferies node → `FORGE/research/jefferies/` (flagged 4mo stale at promotion; WAL = natural refresh owner for WAL-exposure legs only, node stays shared).
