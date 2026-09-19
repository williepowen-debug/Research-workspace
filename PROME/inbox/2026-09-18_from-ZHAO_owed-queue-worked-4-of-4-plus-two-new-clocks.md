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
