# SIGNAL_PROCESSING_CHECKLIST — version history and amendment provenance

**Provenance home for `design/SIGNAL_PROCESSING_CHECKLIST.md`.** Created 2026-09-21 on the established pattern of [`ROUTING_TABLE_VERSION_HISTORY.md`](ROUTING_TABLE_VERSION_HISTORY.md). ⚠️ **No CHECKLIST provenance file existed before this**, so this is a new file on an existing convention rather than a new convention — the alternative was leaving incident narrative in the executable checklist, which is the defect CATO-S1 names.

⛔ **THIS FILE IS NOT A BOOT READ AND NOT ROUTING LAW.** The active rule always lives in the CHECKLIST itself. This is where the *reason* lives. `git log -p -- AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` is the other copy.

---

## v0.47 (2026-09-21) — `FALSE` no longer absorbs "no primary source found"

**Active rule:** in the CHECKLIST verdict table (`FALSE` / `INDETERMINATE` rows). **Status: LANDED, INDEPENDENT READ OUTSTANDING** — see the pinned revision below.

### 🔒 EXACT REVISION UNDER INDEPENDENT REVIEW — PINNED, DO NOT EDIT

🔴 **HAWK is reviewing a SPECIFIC WORDING under `SIG-W-20260921-020` (as narrowed by `-021`). That wording is pinned here verbatim so its acceptance has a fixed target.**

**Pinned revision:** commit **`8d2c9b8ef`** · file `design/SIGNAL_PROCESSING_CHECKLIST.md` **v0.47** · retrieve exactly with:

```sh
git show 8d2c9b8ef:AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md
```

⚠️ **IF A LATER PASS CHANGES THE VERDICT-TABLE WORDING, HAWK's ACCEPTANCE MUST COVER THE RESULTING VERSION — IT DOES NOT SILENTLY CARRY FORWARD TO DIFFERENT TEXT.** (CATO, 2026-09-21.) **Any such change obliges a fresh notice to HAWK naming the new revision.**

### The amendment narrative, moved VERBATIM from the checklist 2026-09-21

*(Relocated under CATO-S1 — incident narrative does not belong in an executable instruction file. Moved unaltered; the active rule and a pointer remain in the CHECKLIST.)*

> 🔴 **v0.47 (2026-09-21) — `FALSE` NO LONGER ABSORBS "NO PRIMARY FOUND". Amended after CATO independent review §S2 (rated HIGH), verified at this line by WALTER before the edit.**
>
> **WAS:** *"Primary source contradicts the claim, **or no primary source exists to support it**"* → KILL.
> ⛔ **THAT CONFLATED ABSENCE OF EVIDENCE WITH EVIDENCE OF ABSENCE, AND THE ACTION WAS A KILL** — a claim nobody has sourced *yet* may be true, unpublished, paywalled, or genuinely false, and the old letter recorded all four as disproved.
>
> 🔑 **THE VERDICT IS NOT THE DISPOSITION, AND THIS IS THE LOAD-BEARING HALF.** ⛔ **This amendment does NOT mean routing every rumour.** An unsupported claim may still be killed — on **Novelty**, **Relevance**, or **Credibility**, on its own merits, with that gate named. **What it may NOT do is exit as `framing-false`**, because that reason asserts something about the world. **Whether an unverified item deserves routing, investigation or the bin is a SEPARATE relevance/urgency decision taken after the verdict, never encoded in it.**
>
> ⚠️ **SCOPE OF THE AMENDMENT — STATED SO IT IS NOT OVER-READ.** This is a **letter-level** correction. **It does NOT establish that any historical kill was wrong.** One prior row is qualified at the artifact (`filtered/kill_log.tsv`, 2026-04-20 Kazakhstan crude-export claim): **that row records a `FALSE` verdict without demonstrated contradiction. Its other reasoning may support withholding dispatch, but review has NOT established the claim's truth, the verdict's calibration, or harm caused by the old rule.** **No other row is re-adjudicated and no re-audit of the 635-row log is implied.**
>
> ⚠️ **MEASUREMENT NOTE, because the next person to size this will hit the same wall:** the `kill_log.tsv` **`Failed_Gate`** vocabulary (Novelty · Relevance · Credibility · …) does **NOT** contain this table's reason strings. **A grep for `framing-false` over the log returns 0 and is a FALSE NEGATIVE** — that is exactly what happened on the first attempt to size this defect. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`
>
> ⛔ **NOT YET INDEPENDENTLY REVIEWED.** The amendment is landed under the 2026-09-21 approval; **the required independent read (own counterexamples, non-implementing) is OUTSTANDING and this clause is not "closed" until it completes.**
### Amendment provenance

- **Defect found by:** CATO independent review `AGENTS/CATO/runs/2026-09-21_1257_walter-structure-review.md` §S2 (rated HIGH). **Not found by WALTER's own boot, doctor or closeout checks, which passed clean over it.**
- **Verified by WALTER at the line before editing** (`SIGNAL_PROCESSING_CHECKLIST.md:124`).
- **Landed under:** Will's approval 2026-09-21 13:09 ET, relayed in `inbox/processed/2026-09-21_from-PROME_cato-second-review-...md`.
- **WALTER's own proposal** (`outbox/2026-09-21_verdict-letter-FALSE-vs-UNSUPPORTED-PROPOSAL-to-Will.md`) proposed a NEW `UNSUPPORTED` enum value; **CATO objected that this creates a third overlapping state and WALTER dropped it. That proposal's enum is SUPERSEDED by this amendment.**
- **Three WALTER errors corrected from outside during this thread**, recorded so a later reader can calibrate the amendment's author: a dropped enum proposal · a truncated `INDETERMINATE` quote that made the enum look sealed when the real defect is overlapping instructions · **a withdrawn assertion that an expected Brent move had been observed not to occur, when the record documents no price observation at all.**
- **Historical row qualified in place**, not re-adjudicated: `filtered/kill_log.tsv`, 2026-04-20 Kazakhstan crude-export claim.
- **Review request:** `SIG-W-20260921-020`, narrowed by `SIG-W-20260921-021`.
