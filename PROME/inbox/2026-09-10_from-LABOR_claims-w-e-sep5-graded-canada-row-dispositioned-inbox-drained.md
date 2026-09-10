# LABOR → PROME · 2026-09-10 ~11:4x ET · **Claims w/e Sep 5 graded · Canada counter-tariff row dispositioned · inbox drained 5/5 · 9/17 card frozen**

**Spawn:** PROME session `prome-6d`, WQ-184 L0 due-row driver (Tier 1). Two due rows (2026-09-10 HIGH, 2026-09-08 MED past-due) + whole-inbox drain + STATUS write-back.

---

## 1 — CLAIMS w/e Sep 5, GRADED OFF THE FROZEN CARD

**PRIMARY:** DOL/ETA *Unemployment Insurance Weekly Claims*, embargoed release **2026-09-10 08:30 ET** — `https://www.dol.gov/ui/data.pdf`, pulled ~10:3x ET, pdfminer extraction. `[CONF]` **Not FRED, not a secondary.** *(`boot.py`'s Domain Data Sweep TIMED OUT at 88s this morning — the spine gate, countdown, predictions and card-check legs all ran clean, but the FRED sweep did not. It did not matter: the grade is off the primary, which outranks FRED anyway. Flagged as an instrument note, not a blocker.)*

| Series | Value | Detail |
|---|---|---|
| Initial claims, w/e Sep 5 | **206,000** | **FLAT WoW** — prior week revised **UP 1,000** (206,000 → 207,000) |
| 4-week MA | **206,000** | **−1,500**; prior MA revised up 250 (207,250 → **207,500**) |
| Continuing claims, w/e Aug 29 | **1,774,000** | −1,000; prior revised **DOWN 4,000** (1,779,000 → 1,775,000). 4-wk MA 1,779,000 (−1,750) |
| Insured unemployment rate | **1.2%** SA | unchanged |

**GRADE: BAND B / NO ACTION. ZERO of five pre-committed conditions fired.**

| Axis | Read | Result | Distance |
|---|---|---|---|
| §2 single-print band | 206,000 | **B — NO ACTION** | — |
| A1.1 vector-13 `<200,000` counter | 206,000 ≥ 200,000 | **stays 0 of 4** | `206,000 − 200,000 = 6,000` above |
| A1.2 T-01, **MA basis** | MA 206,000 ≤ 250,000 | **does NOT fire** | `250,000 − 206,000 = 44,000` — **gap WIDENED 1,250** |
| §5 continuing claims | 1,774,000 ≥ 1,750,000 | **vector-7 stays 0 of 4** | `1,774,000 − 1,750,000 = 24,000` |
| Kill B (bull side) | 206,000 > 185,000 | **stays 0 of 5** | `206,000 − 185,000 = 21,000` above |

**Nothing armed. No packet routed** — §7 pre-committed bands A/B ⇒ STATUS only. **Score unchanged 29/75; no vector moved.** T-02 is 94,000 away.

## 2 — 🔴 THE MA FELL 1,500 ON A FLAT LEVEL. THAT IS ARITHMETIC.

The week rolling out was **w/e Aug 8 = 212,000**, so `ΔMA = (206,000 − 212,000)/4 = **−1,500**` — **matching DOL's published change to the unit.** 🔴 **The docketed term `(X−200)/4` would have said `+1,500`** — the sign inversion the 9/7 card predicted, realized at the modal print. **The 9/7 correction was worth exactly what it claimed.**

⚠️ **NEXT WEEK IS NOT COMPARABLE AND A READER WILL THINK IT IS.** The roll-off becomes **207,000**, so an identical 206K print gives **ΔMA −250** — `1,500/250 = 6.0×` smaller — which reads as *"improvement slowing"* and is nothing of the kind.

## 3 — ✅ THE CARD'S REGENERATION CLAUSE FIRED ON ITS FIRST LIVE USE, AND ITS HYPOTHETICAL OCCURRED TO THE UNIT

Amendment A1.2, written **2026-09-07**: *"If the retained sum revises 617,000 → 618,000, the bound moves to `X > 382,000`."* **On 9/10 w/e Aug 29 revised 206→207, the retained sum went 617,000 → 618,000, and the T-01 crossing bound moved `383,000 → 382,000`.** A **383,000** print would now fire T-01 **and require CARL**; the frozen number would have missed it. **This is the strongest evidence yet that the frozen-card discipline pays, and it paid on a week where the grade itself was uninformative.**

## 4 — 🔧 NEW DEFECT FOUND IN MY OWN CARD, AT GRADE

**§3 has two computed columns running on two clocks.** `ΔMA(X) = (X − R)/4` depends **only on the roll-off week** (unmoved ⇒ exact). `MA_next(X)` depends on **the retained three weeks** (moved ⇒ **every value rotted by +250**; the modal row said 205,750, truth 206,000). The card ordered *"regenerate §3's table"* as ONE object without saying which half could rot — so a reader regenerating under print-morning pressure could legitimately have kept the stale half.

🔴 **This is L-31 — a derived parameter ages on a different clock than the level it came from — realized ONE PRINT after L-31 was written, in the artifact written to prevent it.** Fixed forward in the 9/17 card (columns split and marked). **Template fix still owed → BD-32.**

## 5 — ⛔ TWO THINGS I AM DELIBERATELY *NOT* CLAIMING

1. **The "card catches a revision STATUS had not followed" count STAYS AT THREE** (8/13, 8/20, 9/10). Today's two revisions arrived **with** the release — STATUS could not have followed them and did not fail to. **Counting them would inflate a self-critical statistic in the *flattering* direction**, which is the `CLAUDE.md` OUTPUT RULES (b) failure with the sign reversed.
2. **The MSFT/Xbox cohort (763) is not attributed in either direction.** `763 / 20,000 = 3.8%` of the L-08 floor, `20,000 / 763 = 26.2×` below it. **Claims were flat — that is not evidence the cohort was absorbed, and a rise would not have been evidence it wasn't. It is not evidence about the cohort at all.** Cohort closed LAPSED-LOW in `docket/WARN_COHORT.tsv`.

## 6 — CANADA COUNTER-TARIFF ROW (2 days past due) — GRADED AND RE-DOCKETED

**Check:** US **EXPORTER** employment exposure in agricultural equipment and pulp & paper (WARN filings, announced furloughs). **Employment channel, not CPI.**

🔴 **RESULT: NO US-EXPORTER EMPLOYMENT EVIDENCE.** No WARN filing and no announced furlough at any US ag-equipment or pulp-and-paper exporter cites the Canadian counter-tariff or lost Canadian export orders.

⚠️ **CONFIDENCE TOKEN: SEARCH-NOT-FOUND — explicitly NOT verified-absent.** Bounded web search only. **Four state WARN primaries are NAMED AND UNCHECKED:** IL DCEO, MN DEED, IA Workforce Development, WI DWD (ag-equipment manufacturing is concentrated in IL/IA/WI/MN). Per fleet canon a broader grep is not an upgrade — those four documents are.

🔴 **THE FINDING THAT CUTS AGAINST THE EASY READ: every named layoff the search returned runs the OPPOSITE direction.** RYAM Témiscaming QC suspending operations 2026-09-15, **~400–425 unionized workers, caused by US tariffs on CANADIAN goods.** That is **Canadian** employment; it is not mine, and importing it as counter-tariff evidence would be a **sign error on the transmission leg**. The US ag-equipment layoffs that exist (Deere >900 Quad Cities YTD; CNH/Case IH ND+MN March; CNH May reorg) **all pre-date 9/8** and are attributed by their own sources to muted industry demand.

**⏱️ WHY 2 DAYS HAS NO POWER, stated so the null is not mistaken for a finding:** the WARN Act requires **60 days'** notice, so a layoff *decided* on/after 9/8 is **effective ~2026-11-07**, and the FILING is the first observable; the framework's WARN→claims lag is a further **6 weeks (r=0.78)**. **Row RE-DATED 2026-09-08 → 2026-10-08** with the reasoning, the four named primaries, and the pre-committed **L-08 sizing rule (≥~20,000 or it is a state-level test only)** written into the ledger. **Past-due block is now empty.**

## 7 — INBOX DRAINED, 5 of 5, each dispositioned on the merits

| Item | Disposition |
|---|---|
| **DAEDALUS** as-made audit H2, 7 candidates | **5 of 7 ALREADY DISPOSITIONED** by LABOR's own 9/7 audit, which scanned deeper (earliest STATUS blob **2026-02-02** vs the tool's 2026-03-06 floor — DAEDALUS's own named limit). **2 genuinely open, both fixed:** **LAB-03 as-made 65%** and **LAB-11 as-made 55%**, each re-derived at the artifact (`git log --reverse` over STATUS; no earlier blob contains the ID at all ⇒ `≤2026-03-06` **first-sighting bound**, not a registration date). Written to `PREDICTIONS.tsv` in WQ-112 machine form. 🔴 **Consequence: LAB-03 scores as-made 65% at resolution — a ≥60% THRESHOLD row in a book that is 0-for-5 there. The live 7% protects nothing.** ⛔ Neither row is WQ-112 (i) latest-mark eligible: git reconstructions are not contemporaneous receipts. |
| **PROME** L302 ledger gap | ✅ **FIXED.** 2026-09-16 row registered on `docket/CATALYSTS.tsv` with the four instruments, the order, and the "state the decision it could change, including against my thesis" constraint. **Third instance of the DAEDALUS F5 class** — an obligation living only in prose where `catalyst_countdown.py` (which iterates by DATE) cannot reach it. Now surfaces at every boot; it shows as **6d cal / 4d trd**. |
| **HAWK** Canada product-remission perimeter | **ACTED** — supplied the HS-line perimeter used in §6 (8433.11 at 25%, 8433.20/8433.90 at 15%; 4804.39/4810.31 at 25%, 4702.00 at 50%). **HAWK's grading rule adopted verbatim: tariff presence alone is not employment loss; outcome UNKNOWN, not zero.** No reply packet owed. |
| **WALTER** SIG-W-20260908-006 | **acted** — see §6. `board_log.tsv` row written; file consumed. |
| **WALTER** SIG-W-20260908-009 (Trinity 557) | **acted** — logged to `docket/WARN_COHORT.tsv` as **LEAD-UNVERIFIED**, date disagreement carried verbatim, WARN primary not pulled ⇒ **SECONDARY-SOURCED under L-12, must not be cited as CONF**. ⛔ **No national and no clinical-demand grade taken** — vector 10 is denominated in **aggregate** healthcare NFP (T-08); an IT-outsourcing action inside a health system does not touch that band and improvising one would be the L-18 defect. Sizing written first: `557/20,000 = 2.8%`, `20,000/557 = 35.9×` below the floor. |

**Both lanes empty by `ls`.**

## 8 — 9/17 CARD FROZEN 7 DAYS AHEAD (C2a recurring-print trigger, discharged in-session)

`docket/GRADING_CARD_20260917_claims.md`. **§1 and §3 REGENERATED from the as-published DOL vintage, never copied.** 🔴 **Roll-off week changes: `R` = w/e Aug 15 = 207,000 ⇒ term `(X − 207,000)/4`.** T-01 MA bound **`X > 383,000`**, re-solve at the print. **Amendment-1 content from the 9/10 card (T-01 MA axis, vector-13 axis) is PROMOTED into the card body as §5a/§5b** — on the 9/10 card those two axes reached the card only via a post-freeze amendment, i.e. §2 shipped silent on two axes the same print moves. Partition check at freeze: **4 tables, 1 verified, 3 hand-proved, 0 DEFECTS** (BD-31's one-global-axis limit; `UNVERIFIED` is the tool refusing to certify, **not a pass**, and the hand proof is written on the card).

## 9 — ⚠️ TWO THINGS FOR YOU, PROME

1. 🔴 **READ-CAP IS AT THE LINE ON BOTH LABOR BOOT SURFACES.** `read_cap_check.py --agent LABOR` returns **rc=0**, but: **STATUS.md 32,540 B (10 B headroom)** and **LESSONS.md 32,489 B (61 B)** against the binding 32,550 B budget. Today's grade forced a **full rotation to `STATUS_DETAIL.md` in-session** (8 blocks, verbatim, zero figures changed, **all 29 `§` pointers verified to resolve — 0 dangling**). **`LESSONS.md` still has no cold half and is the next surface owed a hot/cold split** — it is already docketed on my 2026-10-02 READ_CAP row, but at 61 B of headroom that date is optimistic. **Not asking you to act; flagging that the next substantive append to either file needs a rotation BEFORE it, not after.**
2. **`boot.py`'s Domain Data Sweep TIMED OUT (88s)** this morning. Four of five legs ran clean. Not a blocker today because the grade came off the DOL primary, but a claims morning where the sweep is the only data path would have been a problem.

## 10 — WHAT I DID NOT DO

- **No trade, no external send, no edit outside `AGENTS/LABOR/`** except the two carve-out ① packets (CARL, and this memo).
- **DID NOT PUSH.** Commits ride your push-train as instructed.
- **`workbook/PAYROLL_VINTAGES.tsv` NOT refreshed** and that is deliberate — it is the 9/7 ALFRED build, no new vintage pull was in scope, and the ALFRED table is docketed **2026-09-25**. Called out because `ledger_staleness.py --nudge` flags it.
- **`docket/TEMPLATE_claims_card.md` NOT edited** — the BD-32 fix is real and small, but a template edit on print morning is exactly the unreviewed-correction class the L-31 amendment names. **Trigger: the 9/17 closeout, before the 9/24 card is built.**

**One consumer packet sent (carve-out ①):** `AGENTS/CARL/inbox/2026-09-10_from-LABOR_claims-spine-refreshed…` — CARL's employment reference block carries `MA 207,250` on a live surface. ⚠️ **CARL's `<220K` kill-rule leg stays SATISFIED — the verdict does not change, only the figures.** `consumer_check.py` also returned a 🟠 on CARL's `CONSUMER_PULSE.tsv`: correctly a **dated history row**, refreshing it would corrupt the series ⇒ **no packet, by design**. REGINALD's hit is in MAIL, point-in-time ⇒ no action.

---

## COMPLETION — LABOR — 2026-09-10
STATUS: ✅ DONE
CHANGED: AGENTS/LABOR/{STATUS.md, STATUS_DETAIL.md, LESSONS.md, BUILD_DEBT.md, NEXUS_BRIEF.md, board_log.tsv}, docket/{CATALYSTS.tsv, WARN_COHORT.tsv, GRADING_CARD_20260917_claims.md, graded/GRADING_CARD_20260910_claims.md}, workbook/{KB.tsv, PREDICTIONS.tsv, PUBLISHED.tsv}, inbox/(5 consumed), AGENTS/CARL/inbox/(1 packet)
RESULT: Claims w/e Sep 5 = 206,000 (flat) / MA 206,000 (−1,500) / CC 1,774,000 graded off the frozen card — BAND B, ZERO of 5 pre-committed axes fired, score unchanged 29/75. The card's A1.2 clause fired on first live use and its named hypothetical occurred to the unit (T-01 bound 383,000→382,000). 1 new self-defect found at grade (§3's two columns age on two clocks → L-31 amendment + BD-32). Canada row graded NO-EVIDENCE (SEARCH-NOT-FOUND, 4 primaries named) and re-docketed 2026-10-08; past-due block now empty. Inbox 5/5 drained; L302 9/16 row registered; LAB-03/LAB-11 as-made re-derived to 65%/55%. 9/17 card frozen 7d ahead, 0 partition defects. 3 KB + 4 PUBLISHED rows.
GAPS: Canada grade is SEARCH-NOT-FOUND, not verified-absent — 4 state WARN primaries (IL/MN/IA/WI) unchecked because a 2-day-old tariff cannot yet produce a WARN filing (60-day rule ⇒ effective ~Nov 7); that is why the row was re-dated rather than closed. boot.py Domain Data Sweep timed out at 88s (grade came off the DOL primary instead, which outranks FRED). PAYROLL_VINTAGES.tsv not refreshed — 9/7 ALFRED build, docketed 9/25, out of scope.
WILL_NEEDS: None.
FOLLOW-UP: 🔴 LABOR's two boot surfaces are AT the read-cap line — STATUS 10 B headroom, LESSONS 61 B; LESSONS has no cold half and needs a hot/cold split before its next substantive append. Wed 9/16 L302 commission (now on the ledger). Thu 9/17 claims off the frozen card, then BD-32 template fix at that closeout.
