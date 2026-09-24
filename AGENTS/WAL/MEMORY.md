## Session Notes

## ✅ RAISE WITH WILL AT BOOT — **nothing is Will-gated today.**

⏱ **ONE dated item, NOT actionable yet: the FFIEC PWS JWT expires 2026-11-05** (`PROME/WILL_QUEUE.md` row 31). It lands inside the Q3 10-Q window, so a lapse re-darks MI3 exactly when the Q3 re-test is due. **Raise from ~mid-October (with the print-date pin, ~10/13), not before.** Creds are on the **DESKTOP** (`DESKTOP-BC6EF81`) only; the laptop (`WilliePOwen`) cannot pull MI3.

*The full 9/2 MEMORY (session-#6 handoff + the 9/2 NEXT-SESSION ranking) was rotated VERBATIM to `MEMORY_ARCHIVE.md` 2026-09-24 — `sha256(first16) = df422725ae3056a4`. COLD, not frozen.*

---

**⚠️ Open question #1 — THE SHORT'S MARGIN OF SAFETY IS GONE, AND IT WENT ON PRICE.** Spot **$75.60 [Wed 9/23 close]** vs v2.4 EV **$75.96** ⇒ **0.47% BELOW EV**, first time this cycle. EV has not moved since 8/20; no score moved. The fall was **sector + rates** (Fed +25bp 9/16; 10Y 5.11% 9/23; 9/22 "Meta Muse" AI-deposit scare) — WAL **beat** KRE over 9/2→9/23 (−4.45% vs −5.20%) and 8/20→9/23 (−4.49% vs −5.80%), though it traded with the CRE-heavy names (ZION/OZK) over 9/21→9/23 (−3.88% vs KRE −2.24%). ⇒ **The bear is priced; what is left is a resolution trade on the Q3 print + $99M appraisal.** `REG-T-02` stays FIRED (cycle 2), exit `≥$81.90 ×3` 0-of-3 — REGINALD grades; sub-$78 closes (9/16, 9/22, 9/23) are suppressed re-entries.

**⚠️ Open question #2 — the CEO pre-guided Q3 credit BETTER, and the thesis's own retire rule can't tell which basis he meant.** Barclays 9/16 (B2, third-party transcript, model-extracted): NPLs **$567M → ~$500M**, NCO rate + dollars **< Q2**, ACL **"well over 100%"** vs 95%, **"six credits … four down, two to go."** **$567M/95% is our NONACCRUAL basis** ($562M/96%) — on full NPL ($781M) coverage was **69.1%**. The Thesis-RETIRE rule says "ACL/NPL >100%" with **no denominator** ⇒ **~~pin it in the Q3 frame before the print~~ ✅ PINNED 9/24 (Q3 print frame §7): (funded + unfunded ACL) ÷ total nonaccrual; full-NPL reported alongside, non-gating.** ⛔ Guidance, not data: no weight moved; it is the Q3 benchmark. **Silent on the $99M loan.**

**⚠️ Open question #3 — V3 (NDFI) now has evidence pointing both ways.** For a re-score up: Q2 10-Q NDFI 25.9% of HFI (record, A1), FFIEC 9a up 11 of 12 qtrs (A1), Crestline 8-K 9/18 — WAL joined a private-credit SPV facility as LENDER (A1, size undisclosed), Urban Standard $200M (B2/B3). For holding 1/5: KB-121 paraphrase + Vecchione 9/16 *"warehouse … won't be as active going forward"* (B2). **Plan vs measurement — the Q3 10-Q NDFI table decides. Proposal P1 still open.**

**⚠️ Open question #4 (carried) — PT convention strained.** PT = [Bear-fast low, EV] anchors the $52 floor on a 2% scenario. **And spot is now AT the top of the band.** Candidate: anchor on the probability-weighted bear. Needs its own dated edit.

---

**LAST SESSION (2026-09-24 — WAL session #7, Will-directed "update WAL files and metrics"; Thu 00:05–~01:xx ET, LAPTOP; desk dark 22 days 9/2→9/24):**

- **Re-based every live surface on named closes.** $75.60 [9/23]; the 9/22 daily bar is **missing at yfinance** though the market was open (SPY/KRE have one) — used REGINALD's graded $77.75 (previous-close field; my last 30-min bar ~$77.76). `KB-WAL-188/189`.
- ★ **STATUS rotated the honest way, and MEMORY with it.** STATUS was 32,547 B (3 B headroom); the whole 9/2 surface went VERBATIM to `STATUS_ARCHIVE.md` (`sha256(first16)=6ef10add72c95e2d`, = the committed file at `399944561`), then STATUS rewritten lean → **~14 KB** (under the 22,785 B rule-5 STOP). MEMORY same pattern (`df422725ae3056a4`).
- ★ **The two-session-slipped catalyst sweep RAN** (Opus subagent, record `research/CATALYST_SWEEP_2026-09-24.md`): EDGAR clean (no 8-K/144/13G, 9 RSU-only Form 4s @ $79.03 — KB-193); Barclays pre-guide (KB-194/196); Crestline lender role (KB-195); Q3 date NOT announced, analysts, sector drivers (KB-197). **Closes MEMORY N-2.**
- **Positions:** Sep-18 $67.5P + $70P **finished OTM 9/18** ($78.54) — tape read; **broker booking UNRECORDED** (FORGE D-58). Dec-18 $70P **broker-verified 9/10** (D-47). **Live book = 1 leg.** `KB-WAL-191`, POSITIONS.md rewritten.
- **KB expiry backlog 61 → 0** over three row-by-row passes (first pass 61 → 41: 10 SUPERSEDED with successor named, 10 extended with a reason). ⚠️ **Found: KB-WAL-048 "74% of loans pledged ($23.9B)" does not tie to any loan total ($23.9B/74% = $32.3B vs $58.7B HFI) — marked DO-NOT-CITE.**
- **Found: KB-WAL-180's "$79.89 close 8/20" is wrong — the settled close is $79.15** (likely an unsettled bar read as a close). Corrected by a new row, `KB-WAL-190`; 180 untouched; the 9/2 cohort math already used $79.15.
- **Corrections / inbox:** COR-20260915-02 receipted **NO-OP** (the bad "new cycle" instruction was never carried here) — **8 days late, desk dark**. WALTER ×2 rowed + `git mv`; DAEDALUS ×2 info-only; PROME L441 → answered (drift baseline re-measured + a re-check date the script now ENFORCES — `BASE_RECHECK_BY`, overdue branch tested).
- **yfinance short-interest fields are garbage** (2,659 shares short) — `KB-WAL-192`; never refresh KB-061 from that route.

- **LATER THE SAME DAY (PROME rounds 1-2 + Will-directed housekeeping, ~00:30–~15:00 ET):**
  - **Both Q3 frames pre-registered** — print (L170) and 10-Q (L171). ⚖️ Two self-ruled measurement pins, flagged to PROME: RETIRE coverage leg = (funded+unfunded ACL) ÷ nonaccrual; 10-Q classified cross-check = classified LOANS + OREO (Q2: 1,002 + 126 = deck 1,128). **PROME's L171 premise was stale** (P2/P3 were ruled 8/12, repaired 8/20) — disputed with evidence, not re-asked of Will.
  - **Housekeeping, all four items:** KB expiry 61 → 0 · 7 root files + 7 FRAUD files archived (`Q1_2026_ANALYSIS.md` held) · FRAUD/ re-based (live homes FIRST_BRANDS + STUPIN_CRE) · Q2 13F aggregate (84.7% → 90.0%, AQR-led).
  - ★ **Numbers that were wrong and are now fixed:** the "~$46M Cantor residual" had no source → **$72.4M gross / $3.5M allowance** (THESIS, WEAKNESSES, CLAUDE.md on Will's OK) · Cantor loss recognized = **26.5%** of exposure, NOT "89% ≈ ZION 83%" (I repeated that error myself in the morning; retracted) · Q2 share count **flat (−0.08%)**, not −1.7% ⇒ the H2 buyback is UNEVIDENCED · **8/20 KB rows 173-177 corrupted by an unquoted heredoc** (`$`+digit eaten; NDFI nonaccrual read $22.5M, is $122.5M) — restored from REGINALD's cohort file; fleet memory extended (`finding_printf_format_tsv_append_corruption`, n=3).
  - **REGINALD Cat-IV packet:** 4Q-average assets $95.3B vs $100B; corrected his "managing below the line" inference (CEO expects to cross by end-Q1 2027 ⇒ average clears ~Q3-2027, after every carrier).
  - **Boot card + live-surface sweep (Will: "do a sweep")**: CLAUDE.md re-based; 76 stale items applied across THESIS/SCENARIOS/INDEX/KB_INDEX/NEXUS (worst: INDEX said FFIEC creds were on the laptop). ⚠️ **`derived_drift_check.py` saw NONE of the 15 HIGH items** — it only matches version/EV/PT/KB-count tokens + RETIRED_CLAIMS patterns; stale POSITION and DATE claims are invisible to it. Candidate build: a position/date-token check.
  - **Q3 date re-checked 08:49 ET: still not announced.** PROME flagged on ROSTER:107 (stale WAL line, their file).
---

**NEXT SESSION — re-ranked 2026-09-24 closeout (session #7):**

**★N-1. ⏱ From ~Fri 10/2: check the WAL IR feed for the Q3 date EVERY business day; on announcement pin it in `Q3_PRINT_GRADING_FRAME_2026-09-24.md` §9 and re-pin WAL-01/02 `Resolve_By`.** (Checked 9/24 08:49 ET: not announced.) Then watch EDGAR from ~10/24 for the 10-Q and pin it in the 10-Q frame §8.
**★N-2. Before the print: re-verify the Barclays 9/16 quotes at the IR webcast replay** (still B2; the one IR pull 404'd). They are the print frame §6 benchmark.
**★N-3. Weekly EDGAR 8-K sweep for the $99M appraisal** (clean to 9/24 04:10 UTC). ⛔ Silence grades nothing (0-for-1 base rate). The $99M is NOT one of mgmt's six credits (KB-112).
**★N-4. ⏱ ~Mid-October: raise the FFIEC JWT (expires 11/5) with Will.**
**★N-5. DESKTOP session: NDFI trajectory ≥4 quarters (or REGINALD runs it) → re-score V3 or say why not (P1)**; also re-derive KB-048 (pledged loans, basis defect) + KB-049, and verify REGINALD's CET1-incl-AOCI (KB-198).
**★N-6. Consider building a position/date staleness check** — the drift check missed all 15 HIGH items of the 9/24 sweep. Wire it into CLAUDE.md the same session (PAT-041).
**★N-7. 41 ACTIVE KB rows have a BLANK `Stale_By`** — give them dates, or teach `kb_expiry_check.py` a third bucket. Add the two missing rows found 9/24: Q1 V2-inventory-clean result; a Q2 deposit BALANCE.
**★N-8. Book the Sep-18 expiry as a realized loss** when the broker capture lands (ANVIL/FORGE D-58); then check POSITIONS.md History against it.
**★N-9. FRAUD/ open primaries:** Jefferies 3/8 release (guarantee direction) · NYSCEF (WAL v. JEF motions) · LA Superior portal (25STCV24263) · PACER/SCAC (class action) · 2026 DEF 14A.
**★N-10. Two stale token classes to watch at the next thesis bump:** INDEX line 7 and NEXUS carry the KB count and price — re-derive, never carry.

**Carried / lower:** identify the $99M building (LEED × gateway-market press) · read the 2026 DEF 14A · Cantor ledger tie-out at the Q3 10-Q · the second $60M credit (Q3 deck roll-forward) · Form 4 + 144 monthly (always both) · SCENARIOS strike-by-strike rebuild (May-vintage; now only one leg to rebuild for) · `boot.py` (wire into CLAUDE.md the same session) · never examined: FR Y-9C, life-science lab vacancy as the appraisal base rate, AOCI Cat III/IV rule watch (**10Y at 5.11% makes the AFS mark worse**).

**Feedback:** *(none yet — no correction or explicit confirmation from Will to record. 9/24: "use this session to update our WAL files and metrics" = scope grant.)*

**References:** promotion review → `../DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md` · Q2 print grades → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md` + `…_stage2_grade.md` · Q2 10-Q read → `Q2_10Q_READ_2026-08-07.md` · MI3 → `MI3_FIRST_RUN_2026-08-07.md` · **catalyst sweep → `research/CATALYST_SWEEP_2026-09-24.md`** · REG-T-02 exit log → `../REGINALD/registry/REG_T02_EXIT_LOG.tsv` · Jefferies node → `FORGE/research/jefferies/`.
