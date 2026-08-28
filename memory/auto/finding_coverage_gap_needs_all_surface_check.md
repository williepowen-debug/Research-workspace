---
name: finding-coverage-gap-needs-all-surface-check
description: Never declare a coverage/blindness gap from one surface — check every collection mechanism (queries AND feeds AND entities AND human channels); 5 same-day instances, all caught pre-ship; corollary — keep watch-query edits direction-neutral
metadata:
  type: feedback
---

On 2026-07-16, PROME and WALTER produced **five** wrong "X is uncovered/blind" claims in one day, every one from checking a single surface: WALTER×3 (agents "truly blind" — but Will's Telegram drops covered the domains 5-for-5; "11 uncovered" — tags ≠ collection; "VIOLET uncovered" — the cftc_cot FEED was its lane, only newsweep queries were checked) and PROME×2 ("BOND has no auction coverage" — the treasury_auctions feed existed; the VIX narrowing below). All five were caught by the other party before shipping.

**Why:** a collection system has multiple mechanisms (news queries, dedicated feeds, entity lists, human drop channels, the agent's own in-session pulls). Any one surface can show a zero while another covers the domain. A gap claim from one surface reads as rigorous (it cites a grep) and is still wrong.

**How to apply:** before asserting "no coverage / blind / missing," enumerate EVERY collection mechanism and check each (for RESEARCH-INTAKE: `GOOGLE_NEWS_QUERIES` + all `fetch_*.py` feeds + entity/keyword lists + Will's drop channel). Encode monitoring checks with the all-surfaces predicate (the 7/16 doctor checks: FEEDS+QUERIES vs canonical ROSTER). State the narrow true claim ("no autonomous lane collection") not the broad false one ("agent is blind"). **Corollary (the 5th instance):** when narrowing a watch query to cut flood, keep it DIRECTION-NEUTRAL and check registered triggers first — PROME's "VIX spike OR surge" would have blinded RED-FT-06 (VIX <16, live) because vol regimes fail in both directions. Related: [[finding_comprehensive_grep_over_sampling]], [[finding_declared_data_wall_needs_fleet_memory_check]].

## 🔴 2026-08-07 — THE AXIS THIS MISSED: right surfaces, WRONG LAYER. Two instances in one WALTER session, both one grep from correct.

The 7/16 cases were all *"you checked one collection surface instead of all of them."* Tonight's two were different and worse: **the surface sweep was exhaustive and the LAYER was wrong.**

**Instance 1 — the owner.** WALTER told Will three times across four sessions that **gold was "unowned by any agent."** `MIDAS`'s row in **`AGENTS/WALTER/REGISTRY.tsv` — the file WALTER owns, refreshes every boot, and calls the canonical agent directory** — reads *"monetary (**gold**/silver/GSR/CB buying)."*

**Instance 2 — the instrument.** Two hours after shipping an IMMEDIATE, WALTER claimed *"the Red Sea theater has NO REGISTERED GATE OF ITS OWN, so a confirmed sinking there is un-instrumented by construction."* **WALTER had grepped every agent `STATUS.md` and all 667 BOARD signals for the EVENTS** (`Mukha`, `maritime coalition`, `Najran`) and correctly got **zero** — a genuinely thorough sweep. **It never grepped `GATES.tsv` / `VX.tsv`.** `GATE-FALCON-001` **is** the Bab el-Mandeb tripwire, and `VX-FALCON-SUNK-01` — a tiered total-loss ledger — had been **Will-ruled the day before.** The owner had already logged and graded a sinking under it.

**🔑 THE DISTINCTION THAT MATTERS: "does the fleet have this NEWS?" and "does the fleet have MACHINERY for this class of event?" are different questions against different files, and a perfect answer to the first says NOTHING about the second.** The event layer is `STATUS` / `BOARD` / `KB`. The machinery layer is **`GATES.tsv` · `VX.tsv` · `PREDICTIONS.tsv` · `THRESHOLDS.tsv` · `REGISTRY.tsv`.** Thoroughness on one is not evidence about the other — and it *feels* like evidence, which is why this survives a careful sweep.

**⚠️ The aggravator, and it inverts the intuition: a NEWLY-RATIFIED instrument is exactly what a "nobody has an instrument for this" claim will be wrong about**, because ratification is recent by definition. The thing you are least likely to remember is the thing most likely to have just been decided. **Recency makes the registry MORE worth querying, not less.**

**How to apply:**
- **Any claim of the form "there is no owner / no gate / no instrument / nobody tracks X" is a QUERY against the REGISTRY LAYER — never the event layer, and never from recall.** Name the file you ran it against, in the artifact.
- **Say which surfaces you checked, so the gap in the sweep is visible.** WALTER wrote *"0 hits across BOARD + every agent STATUS"* — accurate, and it is precisely that accuracy which made the unchecked layer invisible to the reader **and to the author.**
- **Both instances landed in the INTERPRETIVE layer, not the factual one** — the *"🔑 the finding underneath"* framing, not the events, tallies or rulings, all of which held. **The sentence where you tell the reader what it MEANS is the one that most needs a source, and it is the one that usually gets none.**

*(Related: [[finding_scan_keyed_on_naming_reads_local_form_as_absence]] — same family, where the scan's own key is what manufactures the false absence. And [[finding_dated_carry_item_has_no_expiry_check]] — instance 1 was ALSO a carried assertion; instance 2 was freshly invented, so the two failures are independent and this one does not require a carry.)*

---

**★ EXTENSION 2026-08-28 (WALTER, caught by HANS) — THE SAME RULE FOR A *CLEAN* VERDICT, AND A SECOND AXIS THE ORIGINAL DOES NOT HAVE.**

This memory says never declare a **gap** from one surface. **The identical rule governs declaring a surface CLEAN** — and a clean verdict is the more dangerous direction, because nobody re-opens it.

**Incident.** WALTER dispatched `SIG-W-20260828-038` retiring a BRENT throughput-impairment claim, and ran a consumer sweep first — correctly recording the result as a pre-declared negative. **The sweep opened every desk's `STATUS.md`, `THESIS.md` and `NEXUS_BRIEF.md` and reported "clean."** HANS replied that its only live `impair` instance sits in **`workbook/FLOW.tsv`** — a **ledger class the sweep never opened.** ⇒ *"Right answer, insufficient instrument."* **A transmission-chain ledger is the natural home for a supply/throughput claim, not an edge case.**

🔑 **AND THE SECOND AXIS, which is why simply widening the keyword net would have made it WORSE.** HANS's row reads *"the barrels are still moving, it is the REFINING that is impaired"* — **Russian refining capacity, not Hormuz transit.** Same word, different referent, and independently the same regime the dispatch was naming. **A concept-widened sweep would have flagged HANS as a carrier and been wrong; the narrow sweep cleared HANS and was right for the wrong reason.**

⇒ **SCOPE (which files you opened) and REFERENT (which object the words point at) are INDEPENDENT failure modes, and both were live in one case.** Widening the keyword net fixes neither: it worsens referent error while leaving scope error untouched.

**How to apply.**
1. **Report the PERIMETER WITH THE VERDICT.** *"Clean across STATUS/THESIS/NEXUS_BRIEF"* is a stronger and more honest claim than *"clean."* A bare "clean" silently asserts a perimeter it never had. **A verified claim names the files it opened.**
2. **Include the ledger class (`workbook/*.tsv`) in any consumer/claim sweep** — desks park exactly this kind of assertion in transmission-chain and KB ledgers, where prose surfaces never show it.
3. **Check the REFERENT on every hit before counting it as a carrier.** A keyword match is a candidate, not a finding.
4. Re-run on the widened perimeter here **left the verdict unchanged** (no ledger row paired an impairment claim with a Hormuz-transit referent) — **which is exactly why it needed running: an unchanged verdict is only informative once the instrument could have changed it.**

Related: [[finding_scan_keyed_on_naming_reads_local_form_as_absence]] ("lacks X" is a claim about your pattern set) · [[finding_verification_zero_is_ambiguous]] · [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_backup_copy_must_carry_the_predeclared_negative]].
