## Session Notes

## ✅ RAISE WITH WILL AT BOOT — **nothing is Will-gated today.**

⏱ **ONE dated item, NOT actionable yet: the FFIEC PWS JWT expires 2026-11-05** (`PROME/WILL_QUEUE.md` row 31). It lands inside the Q3 10-Q window, so a lapse re-darks MI3 exactly when the Q3 re-test is due. **Raise from ~mid-October (with the Q3 frame, ~10/13), not before.** Creds are on the **DESKTOP** (`DESKTOP-BC6EF81`) only; the laptop (`WilliePOwen`) cannot pull MI3.

*The full 9/2 MEMORY (session-#6 handoff + the 9/2 NEXT-SESSION ranking) was rotated VERBATIM to `MEMORY_ARCHIVE.md` 2026-09-24 — `sha256(first16) = df422725ae3056a4`. COLD, not frozen.*

---

**⚠️ Open question #1 — THE SHORT'S MARGIN OF SAFETY IS GONE, AND IT WENT ON PRICE.** Spot **$75.60 [Wed 9/23 close]** vs v2.4 EV **$75.96** ⇒ **0.47% BELOW EV**, first time this cycle. EV has not moved since 8/20; no score moved. The fall was **sector + rates** (Fed +25bp 9/16; 10Y 5.11% 9/23; 9/22 "Meta Muse" AI-deposit scare) — WAL **beat** KRE over 9/2→9/23 (−4.45% vs −5.20%) and 8/20→9/23 (−4.49% vs −5.80%), though it traded with the CRE-heavy names (ZION/OZK) over 9/21→9/23 (−3.88% vs KRE −2.24%). ⇒ **The bear is priced; what is left is a resolution trade on the Q3 print + $99M appraisal.** `REG-T-02` stays FIRED (cycle 2), exit `≥$81.90 ×3` 0-of-3 — REGINALD grades; sub-$78 closes (9/16, 9/22, 9/23) are suppressed re-entries.

**⚠️ Open question #2 — the CEO pre-guided Q3 credit BETTER, and the thesis's own retire rule can't tell which basis he meant.** Barclays 9/16 (B2, third-party transcript, model-extracted): NPLs **$567M → ~$500M**, NCO rate + dollars **< Q2**, ACL **"well over 100%"** vs 95%, **"six credits … four down, two to go."** **$567M/95% is our NONACCRUAL basis** ($562M/96%) — on full NPL ($781M) coverage was **69.1%**. The Thesis-RETIRE rule says "ACL/NPL >100%" with **no denominator** ⇒ **pin it in the Q3 frame before the print.** ⛔ Guidance, not data: no weight moved; it is the Q3 benchmark. **Silent on the $99M loan.**

**⚠️ Open question #3 — V3 (NDFI) now has evidence pointing both ways.** For a re-score up: Q2 10-Q NDFI 25.9% of HFI (record, A1), FFIEC 9a up 11 of 12 qtrs (A1), Crestline 8-K 9/18 — WAL joined a private-credit SPV facility as LENDER (A1, size undisclosed), Urban Standard $200M (B2/B3). For holding 1/5: KB-121 paraphrase + Vecchione 9/16 *"warehouse … won't be as active going forward"* (B2). **Plan vs measurement — the Q3 10-Q NDFI table decides. Proposal P1 still open.**

**⚠️ Open question #4 (carried) — PT convention strained.** PT = [Bear-fast low, EV] anchors the $52 floor on a 2% scenario. **And spot is now AT the top of the band.** Candidate: anchor on the probability-weighted bear. Needs its own dated edit.

---

**LAST SESSION (2026-09-24 — WAL session #7, Will-directed "update WAL files and metrics"; Thu 00:05–~01:xx ET, LAPTOP; desk dark 22 days 9/2→9/24):**

- **Re-based every live surface on named closes.** $75.60 [9/23]; the 9/22 daily bar is **missing at yfinance** though the market was open (SPY/KRE have one) — used REGINALD's graded $77.75 (previous-close field; my last 30-min bar ~$77.76). `KB-WAL-188/189`.
- ★ **STATUS rotated the honest way, and MEMORY with it.** STATUS was 32,547 B (3 B headroom); the whole 9/2 surface went VERBATIM to `STATUS_ARCHIVE.md` (`sha256(first16)=6ef10add72c95e2d`, = the committed file at `399944561`), then STATUS rewritten lean → **~14 KB** (under the 22,785 B rule-5 STOP). MEMORY same pattern (`df422725ae3056a4`).
- ★ **The two-session-slipped catalyst sweep RAN** (Opus subagent, record `research/CATALYST_SWEEP_2026-09-24.md`): EDGAR clean (no 8-K/144/13G, 9 RSU-only Form 4s @ $79.03 — KB-193); Barclays pre-guide (KB-194/196); Crestline lender role (KB-195); Q3 date NOT announced, analysts, sector drivers (KB-197). **Closes MEMORY N-2.**
- **Positions:** Sep-18 $67.5P + $70P **finished OTM 9/18** ($78.54) — tape read; **broker booking UNRECORDED** (FORGE D-58). Dec-18 $70P **broker-verified 9/10** (D-47). **Live book = 1 leg.** `KB-WAL-191`, POSITIONS.md rewritten.
- **KB expiry backlog 61 → 41** — 20 rows judged one at a time (10 SUPERSEDED with successor named, 10 extended with a reason). ⚠️ **Found: KB-WAL-048 "74% of loans pledged ($23.9B)" does not tie to any loan total ($23.9B/74% = $32.3B vs $58.7B HFI) — marked DO-NOT-CITE.**
- **Found: KB-WAL-180's "$79.89 close 8/20" is wrong — the settled close is $79.15** (likely an unsettled bar read as a close). Corrected by a new row, `KB-WAL-190`; 180 untouched; the 9/2 cohort math already used $79.15.
- **Corrections / inbox:** COR-20260915-02 receipted **NO-OP** (the bad "new cycle" instruction was never carried here) — **8 days late, desk dark**. WALTER ×2 rowed + `git mv`; DAEDALUS ×2 info-only; PROME L441 → answered (drift baseline re-measured + a re-check date the script now ENFORCES — `BASE_RECHECK_BY`, overdue branch tested).
- **yfinance short-interest fields are garbage** (2,659 shares short) — `KB-WAL-192`; never refresh KB-061 from that route.

---

**NEXT SESSION — ranked 2026-09-24 (session #7):**

**★N-1. ⏱ WRITE THE Q3 FRAME — DUE TUE 2026-10-13 (19 days; `PROME/DOCKET.tsv` L170).** Name the FILING that carries each metric + a NO-VERDICT band per leg. **Two new inputs this session:** (a) mgmt's 9/16 guidance as the benchmark (NPL ~$500M, NCO < Q2 / 37bps, coverage >100%) — **re-verify the quotes at the IR webcast replay first** (KB-194 is B2, model-extracted); (b) **pin the coverage DENOMINATOR** in the RETIRE leg (nonaccrual vs full NPL). ★ **Write it EARLY — the Q2 frame died in a dark period, and this desk just went dark for 22 days.**
**★N-2. ⏱ Re-check the WAL IR feed for the Q3 date ~10/2-10/9 and RE-PIN `WAL-01`/`WAL-02` `Resolve_By` on announcement** (currently 11/15, EXPECTED-EVENT). Prior year: announced 2025-10-02, call Wed 2025-10-22.
**★N-3. $99M appraisal — weekly EDGAR 8-K sweep through the print** (last swept clean to 9/24 04:10 UTC). ⛔ **Silence grades nothing** (0-for-1 base rate for an 8-K on this credit). Also ask at the frame: is the $99M one of mgmt's "six credits"? Nothing public says.
**★N-4. Pull the NDFI trajectory (≥4 quarters, `RCONPV25` + `RCONJ454`) — DESKTOP ONLY**, or take REGINALD up on his offer to run it. Then **re-score V3 or say why not (P1)** — see Open question #3.
**★N-5. KB expiry backlog: 41 left.** Keep going ~10-20 per session, row by row, never bulk. Also **41 rows have a BLANK `Stale_By`** — the check can't expire or certify them.
**★N-6. PROME 8/23 item ② — the 8-file retirement set, run FILE-BY-FILE** (`AUDIT_MAR25` · `EXTERNAL_PROMPTS` · `PRIOR_RESEARCH_EXTRACTS` · `V21_RESPONSE` · `INVESTOR_DAY` ×2 · `Q1_2026_ANALYSIS` · `TECHNICALS_20260401`). Pending-event carve-out + index-refs-don't-count both bite. **Deferred again 9/24** — this session was a re-base.
**★N-7. `FRAUD/` — untouched since 7/25.** Fold KB→corpus or banner it; apply BROCK's collateral-perfection screen there. Vecchione 9/16: Cantor "a fraud", LAM "a breach of contract", "favorable outcome … over the next year or so" (KB-194 transcript).
**★N-8. Run the Q2 13F aggregate** — route proven (EDGAR full-text, CUSIP `957638109`, 394 filings).
**★N-9. Book the Sep-18 expiry as a realized loss** when the broker capture lands — that is ANVIL/FORGE D-58, not this desk; **check POSITIONS.md History against it when it does.**

**Carried / lower:** identify the $99M building (LEED × gateway-market press) · read the 2026 DEF 14A · Cantor ledger tie-out at the Q3 10-Q · the second $60M credit (Q3 deck roll-forward) · Form 4 + 144 monthly (always both) · SCENARIOS strike-by-strike rebuild (May-vintage; now only one leg to rebuild for) · `boot.py` (wire into CLAUDE.md the same session) · never examined: FR Y-9C, life-science lab vacancy as the appraisal base rate, AOCI Cat III/IV rule watch (**10Y at 5.11% makes the AFS mark worse**).

**Feedback:** *(none yet — no correction or explicit confirmation from Will to record. 9/24: "use this session to update our WAL files and metrics" = scope grant.)*

**References:** promotion review → `../DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md` · Q2 print grades → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md` + `…_stage2_grade.md` · Q2 10-Q read → `Q2_10Q_READ_2026-08-07.md` · MI3 → `MI3_FIRST_RUN_2026-08-07.md` · **catalyst sweep → `research/CATALYST_SWEEP_2026-09-24.md`** · REG-T-02 exit log → `../REGINALD/registry/REG_T02_EXIT_LOG.tsv` · Jefferies node → `FORGE/research/jefferies/`.
