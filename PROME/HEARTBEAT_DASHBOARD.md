# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Twentieth base 2026-09-22 — amendment #1 (2026-09-23 20:5x ET): projection below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "c41aa0076d561746f35d00377597d68420fb8f94ecd5d65b4264879dbd927269",
  "set": {
    "one": "September 23, post-close: the TLT-put exit gate is sealed in substance — the 9/22 ten-year cell printed 4.96, so no five-close streak below 4.50 can complete before the 9/30 expiry; TERRY records it. Brent's 9/22 settle was $99.25 (Nov, single vendor); the 9/23 settle is unpublishable because the vendor's evening bar overwrote it — a new fetch.py defect class. Cushing built 2.27M to 23.75M and refinery runs fell to 94.0% with no line crossed. WQ-234 is encoded: AIS trackers corroborate, never fire. STAND DOWN holds; $0 moved.",
    "channels": {
      "Energy": {
        "headline": "🔴 the 9/22 settle is published ($99.25 Nov); the 9/23 settle is not, and Cushing built hard",
        "body": "BZX26 Nov $99.25 · BZZ26 Dec $95.41 [9/22 settle, single vendor, BRENT-adjudicated]. 9/23 settle NOT PUBLISHABLE: after ~18:00 ET the vendor daily bar is the NEXT session's evening trade (new fetch.py class, DOCKET L462). WPSR wk-9/18: Cushing 23.748M (+2.266M), SPR 284.552M, utilization 94.0%. WQ-234 encoded on BG-02 (C1–C6); 9/25 grade modal outcome = lapse."
      },
      "Rates": {
        "headline": "🟠 the 004 exit gate is sealed in substance; TLT $80.46 with five sessions left",
        "body": "9/22 DGS10 4.96 [FRED] ≥4.50 ⇒ GATE-TERRY-007 cannot complete a five-close streak before 9/30; TERRY records MOOT ⇒ NO-VERDICT. TLT $80.46 [9/23c], $3.46 above the $77 strike. Add line 2.50 still THROUGH (DFII10 2.68 [9/18]) ⇒ NO ADD. Harvest gate + expiry stand; forward risk unchanged."
      }
    },
    "ticker": {
      "Brent": "Brent Nov $99.25 [9/22 settle, SINGLE-VENDOR, BRENT-adjudicated; contract BZX26] ⛔ 9/23 settle NOT PUBLISHABLE (evening-bar overwrite, L462)",
      "**HY OAS": "**HY OAS 268 [9/22]",
      "CCC": "CCC 1,075 [9/22]",
      "**DGS10": "**DGS10 4.96 [9/22]",
      "TLT": "TLT 80.46 [9/23c]",
      "WAL": "WAL 75.60 [9/23c]",
      "**VIX": "**VIX 15.18 [9/23c; yfinance, NOT settle-confirmed]",
      "MOVE": "MOVE 95.45 [9/23c; yfinance, NOT settle-confirmed]",
      "**Cushing": "**Cushing 23.748M [wk-9/18; next WPSR 9/30]",
      "SPR": "SPR 284.552M [wk-9/18; next WPSR 9/30]**"
    }
  }
}
```

*⛔ **PRIOR (SUPERSEDED 2026-09-19 13:2x by amendment #1 — see the paragraph above; this one's "nothing is projected" instruction is DEAD).** Nineteenth base 2026-09-19 (Sat, markets closed) at its writing: **chain 0 — no amendments.** The eighteenth base's Amendment #1 (BOJ +25bp 7–2 · first clean SOFR/IORB pair −5bp · 9/17 credit cells flat), Amendment #2 (SAM's L34 grade + the dovish-dissent CORRECTION to #1 · RED's FT-10 grade 0-of-4) and Amendment #3 (HENRY L411 post-opex board · VIOLET L277 leg 3 · the 9/17 H.15 cells · the 9/18 closes · the stale-bar guard) were FOLDED INTO THE BASE at the ~11:2x ET re-base and **their projections are REMOVED here per this file's own rule**; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A19 / §A20 / §A21 (entry-crc32 2358365206 · 712775133 · 3493617609). ⛔ **Found by the nineteenth base's blind RESULT read: this file still declared the eighteenth base and chain 3 after the re-base had been written, and `fleet_dashboard.py` was returning BUILD FAILED — 'each HEARTBEAT amendment needs one reviewed dashboard projection'. The derived view was DEAD, not stale, and nothing in the re-base itself would have surfaced it.** **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the nineteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*


*⛔ **SUPERSEDED 2026-09-22 ~09:4x ET AT THE TWENTIETH RE-BASE — its projection is REMOVED per this file's own rule.** The nineteenth base's Amendment #1 (the GLD/TBT counts DISPUTED by the untranscribed 2026-09-16 13:57 ET broker capture) was FOLDED INTO THE TWENTIETH BASE. ✅ **Its binding warning was RE-HOMED IN ITS CORRECTED FORM, not dropped — and the dispute it named is DEAD.** ⛔ The 16/14 DISPUTE was discharged 2026-09-20 by WQ-272 (ANVIL write-in under Will's authorization); `HEARTBEAT.md:39` now carries **`GLD 17 · TBT 10`** and `:40` declares the old strings dead. What survives on the position line is the NARROWER live caveat: the book is **not transaction-reconciled and not current-book-verified** (WQ-274), on a visual capture that is not an export — the consumer location, per CATO's H3 and the root anti-laundering clause. **Twentieth base = chain 0, so this file must carry ZERO projections**; the builder requires len(amendments) == len(projections) and a single surviving block fails the build exactly as a missing one does. ⚠️ **That is not hypothetical here — it is the recorded failure at the nineteenth re-base, logged at the foot of this file.** **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the twentieth base.***


*Prior: Eighteenth base 2026-09-17 (evening): chain 3 — two projections (Japan/carry and the SAM/RED owner grades), both folded at the nineteenth re-base.*
*Prior: Seventeenth base 2026-09-17 (morning): chain 3 — three Rates-channel projections, all folded at the eighteenth re-base.*

*Prior: Fifteenth base 2026-09-12: **chain 0 — no amendments.** The fourteenth base's Amendment #1 (closeout write-back 12:1x) and Amendment #2 (the Saudi MoE Petroline shutdown statement) were FOLDED INTO THE BASE at the 2026-09-12 re-base and their projections are REMOVED here per this file's own rule; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A14 / §A15 (entry-crc32 3012472809 · 1121796424). **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the fifteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*

*⛔ **ONE ORPHANED PROJECTION REMOVED 2026-09-19 at the nineteenth re-base: amendment #3 of the EIGHTEENTH base (Equity-vol · Rates · Credit) was still present in this file, sitting immediately below a PRIOR note that declared projections removed.** It was left behind by an earlier re-base and it is the reason `fleet_dashboard.py` returned BUILD FAILED: the builder requires len(amendments) == len(projections), and with the nineteenth base at chain 0 a single surviving block is a mismatch just as surely as a missing one. Its content is fully carried by the nineteenth base (§5 · §2 · §3) and the amendment block itself is verbatim at `PROME/HEARTBEAT_COLD.md` §A21, so nothing is lost. 🔑 **The lesson for this file's own rule: 'remove projections for amendments folded into the base' had no CHECK, so a miss was invisible until the builder failed — and the builder's failure message names the amendment side, not the orphan side.** `[[finding_guard_correctness_and_wiring_are_independent]]`*
