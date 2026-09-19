# ZHAO → PROME · 2026-09-18 · Boot + the owed queue, worked 4 of 4

**Session:** Will said "boot up", then "work owed". No coordinator spawn; ZHAO self-directed against its own NEXT ACTIONS list.

## What was owed and what happened

| # | Owed item | Result |
|---|---|---|
| 1 | DAEDALUS PR6, two asks due 9/24 | ✅ **both discharged** — SOFR leg re-based; `CATALYSTS.tsv:8` graded and re-dated; all four `date_class=modeled` rows given explicit re-check dates |
| 2 | WQ-112 as-made ledger write | ✅ written across all 17 rows — **and three ordered re-scores REFUSED as contrary to ratified canon** |
| 3 | RatingDog Aug PMI (overdue) | ✅ **51.5**, pulled from the S&P Global primary |
| 4 | ZHA-18 letter before Aug TIC | ✅ **registered 28 days early at a base-rated 40%** |

## The four things PROME may need to act on

**① A ratified-canon conflict inside a ZHAO report, now corrected (KB-ZHAO-160).** `reports/2026-09-17_ASMADE_VERIFICATION.md` instructed a re-score of ZHA-03/04/15 on their as-made confidences, and STATUS carried it as a 🔴. **WQ-112(i) says the opposite** — *"the latest dated pre-resolution mark governs scoring."* Replaying every commit of the ledger shows all three marks dated and landed 48 / 36 / 18 days pre-resolution ⇒ valid, grades stand, nothing re-scored. ⚠️ **Worth PROME's attention as a fleet pattern, not just a ZHAO fix: the report was written 16 days AFTER WQ-112 was ratified and cites `PREDICTION_DISCIPLINE.md` in its own header as canon-read.** Reading the canon did not produce applying it. Mass-neutrality proof (WQ-161 ③) written at patch time: `reports/2026-09-18_WQ112_ASMADE_LEDGER_WRITE.md`.

**② A dated escalation clock nobody on the fleet had registered (KB-ZHAO-156).** **BIS 90 FR 50857:** the Affiliates Rule ("50% rule") stay is *"stayed until November 9, 2026"* and *"set to end November 9, 2026, absent a future extension."* **That is one day before the reciprocal-tariff truce lapses (11/10, 12:01 EST) — two independent lapse-by-default mechanisms on consecutive days.** On reactivation any entity ≥50% owned, **including in the aggregate**, by Entity List parents is automatically covered — the controlled perimeter widens with **zero new listings**. Registered on ZHAO's CATALYSTS as P1. ⛔ **It does not touch ZHA-16** (separate instrument, separate clock; letter not amended). ⚠️ Not a forecast — BIS extended once and may extend again.

**③ A ZHAO kill criterion that satisfies itself on arithmetic (KB-ZHAO-159).** The standing thesis-kill leg *"Belgium <10% YoY ×2"* will print in Aug and Sep **with Belgium perfectly flat**, because the 2025 base rose from $425.4B (Jul) to $481.0B (Nov). Avoiding it would take a **+$25.5B** monthly buy, larger than any in the 42-month flow series. Declared in the ZHA-18 letter §2 **before** the print: record as **SATISFIED-ON-BASE-EFFECT, not evidence.** The full kill still cannot fire (other leg needs China >$700B ×3; China is $618.0B). **Leg needs re-spec; deliberately not done inside the letter that grades it.**

**④ A defect I introduced and caught before commit.** An earlier edit in this session left an unexpanded regex backreference in `STATUS.md`, merging convergence-matrix rows 1 and 2 into one line and dropping a cell. Found on the next pass, repaired, all 12 rows verified at 5 cells. Flagging it because it would have shipped a silently wrong matrix, and because the tell was a *falling* row count, not an error.

## 🔔 THREE OUTBOX PACKETS AWAITING PROME ROUTING

ZHAO does not deliver into other agents' inboxes. Written, not delivered:

1. `outbox/2026-09-18_to-HANS-LIQUID_belgium-yoy-kill-leg-fires-on-a-base-effect.md` — 🟠 **check your own hub YoY thresholds for the same 2025 base steepening** (Luxembourg/Ireland too). Instrument question, not a China claim.
2. `outbox/2026-09-18_to-HENRY-MARCO-MIDAS_china-factory-gate-prices-cut-first-time-in-2026.md` — 🟠 HENRY. Chinese output prices cut for the first time in 2026 **while export orders ran fastest in six months**: margin compression at the factory gate, China exporting disinflation harder. ZHAO asserts no pass-through view.
3. `outbox/2026-09-18_to-VULCAN-HAWK_bis-affiliates-rule-stay-lapses-nov-9-one-day-before-the-truce.md` — 🔴 VULCAN/HAWK. Ask to VULCAN: **does your entity map resolve ≥50% AGGREGATE ownership, or only direct majority holdings?**

## Also this session (boot leg)

The **−164bp HIBOR-SOFR spread was retired as never a measurement** — its SOFR leg was an unsourced `~4.30% [EST]`; SOFR printed 3.85%, true spread **−98.1bp** (KB-154). **The NY Fed answered on the first try once the request carried a browser User-Agent** — August's block was a header problem misread as loss of access, so "no third source exists" had been sitting in NEXT ACTIONS as a fact. Five of six key-figure stale flags cleared (yuan 6.70; won 1,385.95, retraced 27 won weaker; HK AB HK$53,975M flat, no intervention; 1M HIBOR 2.869%). **September LPR re-dated 9/22 → Sun 9/20** — the 20th is a State Council make-up workday, so the fixing does not roll (KB-157). STATUS read-cap rotation #3 → `archive/STATUS_COLD_20260918.md`, §①–㉓.

---

**STATUS:** COMPLETE
**CHANGED:** `STATUS.md` · `NEXUS_BRIEF.md` · `workbook/KB.tsv` (KB-153..160) · `workbook/VX.tsv` (2.01/2.03/2.04/2.05) · `workbook/PREDICTIONS.tsv` (all 17 rows + ZHA-18) · `docket/CATALYSTS.tsv` · 2 reports · 3 outbox packets · `archive/STATUS_COLD_20260918.md`
**RESULT:** owed queue 4/4; 2 new dated clocks registered; 3 self-defects found and recorded (a canon conflict, a degenerate kill-leg, a corrupted matrix row)
**GAPS:** GACC Aug tables still TLS-blocked; SAFE Aug reserves/gold unpulled since 7/7; Belgium kill-leg re-spec open; ZHA-10 `Date_Made` defect flagged not fixed
**WILL_NEEDS:** nothing gated on Will. Next decision point is the 9/24 summit grade (ZHA-16, on the document only)
**FOLLOW-UP:** PROME to route the 3 outbox packets; `CLAUDE.md` L56/L246/L260 re-key still held for PROME's word

---

# ADDENDUM 2026-09-18 ~21:3x ET — a documentation audit, and a closeout-discipline miss of ZHAO's own

**Why this addendum exists:** the memo above was filed at 21:12 and the session did not stop there. Will asked (a) whether all new data was properly documented, then (b) whether closeout had actually been run. Both questions found something.

## ① Documentation audit — 6 defects in output committed hours earlier (KB-ZHAO-162)

**One shape, six times: the fact was written correctly into KB, and the surface a reader travels was left wrong.**

- **`KB-ZHAO-158` cited `VX-ZHAO-3.01` — the Evergrande bond-price row.** A PMI finding pointing at a property instrument.
- **`KB-ZHAO-157` (LPR) cited `VX-ZHAO-4.01` — a superseded PMI row.** Correct home is `VX-ZHAO-6.06`.
- ⛔ **These two are the ones worth PROME's attention as a fleet pattern: both ids EXIST, so presence and referential-integrity checks return clean while the pointer is semantically wrong.** An id check cannot see subject mismatch.
- `VX-ZHAO-6.11` still declared the state-vs-private divergence *"NOT ESTABLISHED / unresolved for August"* hours after ZHAO resolved it.
- `VX-ZHAO-6.06` still read *"HELD 14th mo"* — true at the July fixing, two months stale; August never logged.
- `VX-ZHAO-1.04` — the row a reader consults for the Belgium YoY threshold — carried **none** of the base-effect refutation and kept the backwards framing.
- ⛔ **`STATUS.md` NEXT ACTIONS #8 instructed creating `VX-ZHAO-8.01`, an id already held by a FROZEN "NPC GDP Target" row. Executed literally it destroys data.** A stale instruction is not merely useless.

**New records created by the audit:** `VX-ZHAO-6.14` (private PMI + state-private gap — structural, previously untracked; bands ZHAO-set on n=2 and flagged PROVISIONAL) · `FLOW-ZHAO-13` (China factory-gate deflation → US goods disinflation, one observation) · `FLOW-ZHAO-14` (export-control perimeter widening, ARMED to 11/09) · `KB-ZHAO-161` (the TIC base rate, logged separately so it outlives the ZHA-18 letter) · `KB-ZHAO-163` (Aramco INFO dispositioned, no score move). **Both FLOW rows exist because the ledger-staleness nudge fired and was correct.** Inbox drained, 3 items filed to `processed/`.

⚠️ **The audit ran only because Will asked.** ZHAO's closeout had already passed clean — commit, `claim_check`, `read_cap_check`, TSV widths. **None of those can see a correct value filed against the wrong subject.**

🔧 **FOR DAEDALUS, proposed not built (tooling is not ZHAO's to add):** a boot check that a `VX-` id cited in a KB row's `Vectors` field has a NAME plausibly matching that row's Entity/Fact. Nothing tests semantic fit today.

## ② ZHAO broke the NEXUS Amendment-10 ordering rule

Measured, not asserted: **`NEXUS_BRIEF.md` last committed 21:12:54; `STATUS.md` last committed 21:21:50.** The brief was **9 minutes older than the surface it summarises** and content-stale on every audit finding.

ZHAO ran a compliant closeout at 21:12 (brief + STATUS + memo in one commit) **and then kept working.** ⚠️ **This is the exact mechanism Amendment 10 names** — not a skipped refresh, but a refresh followed by a second work phase. **The rule is not "refresh at closeout"; it is "refresh AFTER the last STATUS write."** Caught only because Will asked whether closeout had been run.

**Remediated in the correct order this time:** final STATUS write completed and byte-verified first (22,772 B, rule-5 stop cleared), then the brief folded, then a single commit. Recorded in `NEXUS_BRIEF.md` itself as evidence about the rule — NEXUS owns the schema, so the instance is routed there rather than quietly re-committed.

---

**STATUS:** COMPLETE (supersedes the completion block above)
**CHANGED (addendum):** `workbook/KB.tsv` (KB-161/162/163 + 2 cross-ref repairs) · `workbook/VX.tsv` (6.06, 1.04, 6.11 + new 6.14) · `workbook/FLOW.tsv` (13, 14) · `STATUS.md` · `NEXUS_BRIEF.md` · inbox → `processed/` ×3
**RESULT:** 6 self-defects found and fixed; 5 new records; ordering-rule breach found, remediated and documented
**GAPS:** unchanged — GACC Aug tables, SAFE Aug reserves, Belgium kill-leg re-spec, ZHA-10 `Date_Made`. China Aug PPI (~9/10) unpulled and is the nearest confirming instrument for FLOW-13
**WILL_NEEDS:** nothing gated. Next decision point remains the 9/24 summit grade (ZHA-16, on the document only)
**FOLLOW-UP:** PROME to route the 3 outbox packets; the DAEDALUS cross-ref check above; `CLAUDE.md` L56/L246/L260 re-key still held for PROME's word

---

# ADDENDUM 2 — the ledger-nudge disposition, and why the canonical fix was REFUSED

**Origin:** the previous addendum admitted a small miss — the ledger-staleness nudge was dispositioned to Will verbally instead of in a commit message, as the rule requires. Will asked for it to be fixed. Investigating the proper fix turned up a fleet tooling defect.

## The disposition, recorded where the rule asks (this packet + the commit message)

**Nudge:** `PREDICTIONS.tsv`, `FLOW.tsv`, `KB.tsv`, `VX.tsv` reported "behind" STATUS. **Disposition: NOTHING OWED — refresh declined, and the reason is mechanical, not a judgement call.** All four ledgers were written earlier in this same session (KB/VX/FLOW at `503cb7c76`, PREDICTIONS at `4c27c1548`). The tool counts STATUS-writes since each ledger's last *commit*, so splitting one session across four commits manufactures the "behind" count. No ledger's DATA is stale: KB, VX, FLOW and PREDICTIONS all carry 2026-09-18 content.

## ⛔ Why the canonical fix was refused — measured, not argued (KB-ZHAO-164)

`scripts/ledger_staleness.py` prefers an in-content **`Last real data refresh: YYYY-MM-DD`** header (PAT-044) and documents git-commit time only as the FALLBACK. So the textbook fix is to add the header and stop the false positive permanently.

**It breaks the readers.** `scripts/boot.py::_read_tsv` and `scripts/validate_all.py::leg_kb_stale_by` both take the FIRST line as the column header.

**Tested on a scratch copy of the live `AGENTS/ZHAO/workbook/KB.tsv`:**

| | Result |
|---|---|
| before | `OK — 91 rows supervised` by the fleet `Stale_By` expiry check |
| after prepending `# LIVE ledger. Last real data refresh: 2026-09-18` | **`NO_COL` — 91 rows silently dropped** |

**It does not error.** It reports the desk as having no `Stale_By` column and stops supervising it. **Trading a loud false positive for silent loss of fleet coverage is the inversion the fleet explicitly rules against.** The header was therefore NOT added; ZHAO's ledger staleness stays commit-time-based **by necessity, not neglect**.

**⚠️ NOT A ZHAO-ONLY PROBLEM, and this is the part for PROME:** any desk whose ledger is a bare-column-header TSV has the same trap, and **any desk that already adopted the PAT-044 header on a TSV may be invisible to leg C2 right now while believing it is covered.** Cheap check for whoever owns the tooling: **run leg C2 and compare the supervised-desk count against the roster — a desk in `no_col` that thinks it has the column is the tell.**

**🔧 Proposed, not built (tooling is not ZHAO's to change):** a leading-comment skip in `_read_tsv` and `leg_kb_stale_by` before the header row — ~2 lines each — which makes the PAT-044 header safe for TSV ledgers fleet-wide.

## Routed

`outbox/2026-09-18_to-DAEDALUS-PROME_two-tooling-gaps-found-by-auditing-my-own-output.md` — carries this plus the `Vectors` cross-reference gap from KB-162. **Fourth packet awaiting PROME routing.**

---

**STATUS:** COMPLETE (supersedes both completion blocks above)
**CHANGED (addendum 2):** `workbook/KB.tsv` (KB-164) · `STATUS.md` (NEXT ACTIONS #10 now carries both tooling gaps; outbox count 3→4) · `NEXUS_BRIEF.md` · new outbox packet to DAEDALUS+PROME
**RESULT:** nudge dispositioned in-record as the rule requires; the canonical fix tested and REFUSED with evidence; a fleet-wide tooling trap identified and routed
**GAPS:** unchanged — GACC Aug, SAFE Aug reserves, Belgium kill-leg re-spec, ZHA-10 `Date_Made`, China Aug PPI
**WILL_NEEDS:** nothing gated. Next decision point is the 9/24 summit grade
**FOLLOW-UP:** PROME to route 4 outbox packets; DAEDALUS to rule on the two proposed checks — **and to run the leg-C2 coverage census, which is the item with fleet blast radius**

---

# ADDENDUM 3 — the last owed pull refuted a same-day pathway, and the packet was corrected before you routed it

**Origin:** Will asked "everything okay now?". Running the verification found four leftovers, three of them cheap. The fourth was the overdue **China August CPI/PPI** pull — and it broke a finding from earlier the same session.

## 🔴 The refutation (KB-ZHAO-165) — ACT ON THIS BEFORE ROUTING PACKET #2

**China August CPI/PPI, released 2026-09-09, pulled 9/18:** CPI **+0.8% YoY** (cons 0.8%, Jul 0.5%), MoM +0.4%, **core 1.0%**. **PPI +3.8% YoY** (cons 3.7%, **Jul +3.5%**), MoM +0.4%. **NBS cites rising energy prices.**

`FLOW-ZHAO-13` — created hours earlier on RatingDog's *"output prices cut for the first time in 2026"* — **named PPI as its own confirming series. PPI came in the opposite direction.**

⇒ **Pathway downgraded ACTIVE → CONTESTED the same day it was created.**
⇒ ⛔ **`outbox/2026-09-18_to-HENRY-MARCO-MIDAS_...` HAS BEEN CORRECTED IN PLACE.** Its headline claim — *"China is exporting disinflation harder"* — is **withdrawn**. The correction sits at the top; the original text is retained verbatim beneath it so the correction is auditable against what it corrects. **Route the corrected file; do not route the original claim.**

✅ **The reconciliation, which is the actual finding:** NBS PPI is an **upstream/energy-weighted aggregate**; RatingDog measures **downstream manufacturers' own selling prices** as a diffusion index. Rising inputs with falling own-prices is **margin compression** — exactly what RatingDog reported. Both are true. **What dies is the aggregate claim:** the producer-price level a foreign buyer faces is **+3.8%, not negative.**

⚠️ **Named as a gap, not substituted for:** the right instrument is an export price index or a PPI for *finished manufactured goods*. ZHAO has neither. **Aggregate PPI is now explicitly ruled insufficient for this row — it measures the wrong layer.**

⚠️ **Stale benchmark found by running the check:** the CATALYSTS row asked for *"PPI YoY vs −2.6%"* when July was already **+3.5%** — the reference was ~6 points and a **sign** out of date.

## ② Three hygiene leftovers, fixed

- ⛔ **A `date_class` value ZHAO INVENTED this session — `modeled-recheck` — reverted to `modeled`.** `date_class` is a fleet convention read by **ten desks' `catalyst_countdown` scripts**; a one-desk value is schema drift. ZHAO's own boot flagged it within the hour. **If the re-check distinction deserves an enum value, DAEDALUS owns that spec — propose, don't mint.**
- **WQ-161 catalyst graded DONE** — ruled 9/10, encoded 9/14, verified at the primary. ⚠️ **Swept 3 days late, and the 9/18 session had READ that ruling while checking something else without grading the row that asked for it.**
- **July TIC row priority P1 → DONE.** It resolved 9/17 and said so in its own threshold cell, but the PRIORITY stayed live, so every boot re-listed it under "SWEEP NOW". **A resolved row with a live priority is indistinguishable from unswept work.**

## Still genuinely open (not defects — dated or owned elsewhere)

GACC Aug tables (TLS-blocked) · SAFE Aug reserves/gold · Belgium kill-leg re-spec · ZHA-10 `Date_Made` · China Sep PMI (9/30) · two PROME DOCKET rows that are **PROME's to grade, not ZHAO's**.

---

**STATUS:** COMPLETE (supersedes all completion blocks above)
**CHANGED (addendum 3):** `workbook/KB.tsv` (KB-165) · `workbook/FLOW.tsv` (FLOW-13 → CONTESTED) · `docket/CATALYSTS.tsv` (3 rows graded, invented enum reverted, stale benchmark fixed) · `STATUS.md` · `NEXUS_BRIEF.md` · **HENRY packet corrected in place**
**RESULT:** a same-day pathway refuted by its own confirming instrument and the cross-desk packet corrected **before** routing; 3 hygiene leftovers closed; schema drift reverted
**WILL_NEEDS:** nothing gated
**FOLLOW-UP:** 🔴 **route the CORRECTED HENRY packet, not the original** · 4 packets total · DAEDALUS: two proposed checks + the leg-C2 coverage census

---

# ADDENDUM 4 — ⛔ ROUTING CANCELLED: all four packets DELIVERED DIRECT on Will's word

**Will, in-session 2026-09-18: *"Just go ahead and put into their inboxes."*** ZHAO's MAIL rule makes direct cross-agent inbox writes the **Will-authorized exception**, so they were delivered directly and committed by ZHAO under root carve-out ①.

⛔ **PROME: DO NOT ROUTE THESE. The earlier FOLLOW-UP lines asking you to route four packets are DISCHARGED.** Every copy carries a banner saying it was delivered direct and why, so no recipient mistakes it for a lane delivery.

**9 copies, 8 desks:**

| Packet | Delivered to | Priority |
|---|---|---|
| BIS Affiliates-Rule stay lapses **2026-11-09** | **VULCAN**, **HAWK**, HENRY (info) | 🔴 |
| **CORRECTED** — China factory-gate price claim **withdrawn**, PPI came in opposite | **HENRY**, MARCO, MIDAS | 🟠 |
| Belgium YoY kill-leg fires on a base effect — check your own thresholds | **HANS**, **LIQUID** | 🟠 |
| Two tooling gaps (cross-ref subject check; PAT-044 header vs `validate_all.py`) | **DAEDALUS** | 🟠 |

✅ **The HENRY/MARCO/MIDAS copies are the CORRECTED file** — verified at the delivered artifact, not assumed. Its filename leads with `CORRECTED-` and its first section withdraws the original headline, with the superseded text retained beneath it.

**Outbox originals `git mv`'d to `outbox/delivered/`.**

**The one genuine dependency, unchanged:** VULCAN's answer on whether its entity map resolves **≥50% AGGREGATE** ownership or only direct majority stakes. That is the difference between a supply-chain map being right or wrong on 11/09.

**Still yours, not discharged:** the DAEDALUS packet's second item asks for a **leg-C2 coverage census** — whether any desk that adopted the PAT-044 header on a TSV ledger is currently invisible to `validate_all.py`. That has fleet blast radius and no owner but tooling.

---

**STATUS:** COMPLETE (supersedes all completion blocks above)
**CHANGED (addendum 4):** 9 packet copies into VULCAN · HAWK · HENRY ×2 · MARCO · MIDAS · HANS · LIQUID · DAEDALUS inboxes; 4 originals filed to `outbox/delivered/`
**RESULT:** all four packets delivered direct under Will's word; PROME routing obligation discharged
**WILL_NEEDS:** nothing gated
**FOLLOW-UP:** VULCAN's aggregate-ownership answer · DAEDALUS's leg-C2 census
