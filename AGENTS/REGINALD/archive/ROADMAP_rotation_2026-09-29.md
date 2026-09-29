# ROADMAP.md rotation — 2026-09-29 (READ_CAP rule 5; ROADMAP reached 76% of budget after the 9/29 write-back)

Each block is VERBATIM + contiguous; recompute the crc32 over the exact bytes between the START/END lines (exclusive) before trusting.

**BLOCK R2 — AWAITING DATA — 'Forward (from 6/2)' table (all fired or CALENDAR-owned).** 1970 B, crc32 `f623792c`.

<!--R2-START-->
**Forward (from 6/2):**

| Date | Item | Test / Implication |
|------|------|-------------------|
| **Weekly Thu** | Initial claims | >300K trigger (latest **208K** [FRED wk 7/11, pulled 7/17] — falling) |
| ~~**Jun 18**~~ ✅ | AOCI / bank capital-rules comment period CLOSED | Confirmed (SIG-W-20260618-006). ~5.2% Cat III/IV relief + AOCI-inclusion catch + Barr 6-1 dissent. **Next: final-rule publication** (forward catalyst, date TBD) — see Open Threads. |
| ~~**Jun 18**~~ ✅ | Options expiry cluster | CLEARED — Will confirm 6/19 all closed out/expired worthless. POSITIONS.md updated (canonical). |
| **TBD (post-comment)** | Bank capital-rules FINAL rule | AOCI-inclusion CET1 impact on WAL/OZK; affects Bear-medium capital-absorption leg |
| **Jul 21 AMC** ✅ RE-CONFIRMED 7/9 | WAL Q2 print (was "~Late Jul / ~Jul 30" — corrected 7/9 via company primary: BusinessWire/Yahoo Finance/MarketBeat, release 7/6/2026) | NCO ex-fraud test (REG-25, **72%**); Office classified migration (REG-24, **65%**); REG-26 surprise (33%) — re-graded 7/16. Leading-bucket trend; one Office migration or 2+? (v2.2 vs v2.5/v3). **SAME DAY as OZK's confirmed 7/21 AMC print — double-fire.** Jul-17 $65P lapsed 7/17; Sep $67.5P+$70P is the print-catching tenor. |
| **Jul 21-22** | CRE-DQ-by-tier Q2 watch (from 6/20 drill) — now dated concretely, was "~Late Jul" | BKU + SBCF 30-89 **both tested 6/20 PM → small CRE leading-ticks (+50% / +132%); Q2 confirms BUILD vs quarter-end/acquired-pool lumpiness**; OZK/EGBN named-loan creep→NCO conversion; OZK FFIEC RC-N formal past-due-by-category; SSB/AMTB criticized→NCO (SIG-008 bar). |
| **Aug 2026** | IQHQ loan maturity (OZK) | Sponsor support test (OZK primary) — life-science pattern pair with WAL $99M |
| **Oct 1 2026** | OZK $350M sub notes reprice (2.75%→SOFR+209) | Tier 2 capital -20% (OZK primary) |
| **Oct 2026** | Affinius Capital $2.7B bond maturity | OZK link — NOT mentioned on Q1 call |

<!--R2-END-->

**BLOCK R3 — OPEN QUESTIONS — two resolved rows.** 449 B, crc32 `5958e5ae`.

<!--R3-START-->
| ✅ **Exit-100% rule re-anchor** | RESOLVED 2026-06-19 — **Will confirmed: keep as REVIEW trigger** (HY<260 no longer auto-exit; real exit re-anchored to CRE channel). In force in STATUS EXIT RULES. |
| ✅ **SSB $90P provenance** | RESOLVED 2026-06-19 — Will: **real position, sold/closed** (date/path unrecorded). NOT a fabrication-phantom → unrecorded-exit propagation gap (same class as KRE $70P 5/8). Recorded CLOSED in POSITIONS.md. |
<!--R3-END-->

**BLOCK R4 — OPEN THREADS: 12-aged-threads row.** 886 B, crc32 `03552a2c` (exact bytes between the START/END lines, exclusive; recompute before trusting).

<!--R4-START-->
| *(12 aged threads, last touched 4/26 → 6/20)* | **CLOSED 2026-09-02 with per-row verdicts and evidence → `archive/ROADMAP_aged_threads_2026-09-02.md`** (crc32 `a277c281`, 5,979 B). **Nine closed because LATER WORK HAD ALREADY ANSWERED THEM** (EGBN creep → the 7/25 Q2 grade · ZION MI3 → the 8/13 cohort re-run · Q1 drill → the Q2 10-Q pass · life-sci #3 → OZK's IQHQ sweep) **and nobody went back to say so**; three were never mine (WAL ×3 post-7/25 cutover, APO → BROCK) or dead on the thesis retirement. | ⚠️ **The class, worth more than the sweep: a thread that resolves as a SIDE EFFECT of other work does not self-close.** It sits at 🟠 advertising finished work, and every boot pays a read plus a moment of *"should I be doing this?"*. **Closing is a write-back obligation of the session that did the answering, not a tidy-up for later.** | 2026-09-02 |
<!--R4-END-->

**BLOCK R5 — OPEN THREADS: closed-threads row.** 908 B, crc32 `101f4efa` (exact bytes between the START/END lines, exclusive; recompute before trusting).

<!--R5-START-->
| *(closed threads)* | **24 RESOLVED rows EXTRACTED VERBATIM 2026-09-02 → `archive/ROADMAP_rotation_2026-09-02.md` BLOCK C**, crc32 `1d242fd4`, 30,363 B. ⚠️ **Non-contiguous row-set, not a contiguous block** — resolved and live rows are interleaved by construction, so READ_CAP rule 4(a)'s contiguity clause could not be met; verbatim + recomputable-crc + nothing-deleted all hold, and the deviation is named here rather than hidden. ⚠️ **One of the 24 was NOT marked resolved: `🔴 WAL Q2 grading frame — resolves 7/21` sat under OPEN THREADS as a RED row for ~6 weeks after both stages were graded 7/21-7/22** (`reports/2026-07-21_WAL_Q2_grade.md`, `..._stage2_grade.md`). A closed thread in an open container reads as urgent work at every boot. | **Re-check size at any append, or on 2026-10-02, whichever is first** — `python3 scripts/read_cap_check.py --agent REGINALD`. | 2026-09-02 |
<!--R5-END-->
