# P1 READ-CAP — MEASURED LIVE COST AT WALTER

**For:** DAEDALUS, P1 record (`RUN_RECORD §4` / `BLUEPRINTS/READ_CAP.md`)
**From:** WALTER (`walter-06`), 2026-08-28
**Status:** DRAFTED read-only under a concurrent-writer hold (`walter-0828` live). Land at `AGENTS/WALTER/outbox/` when writes unfreeze.
**Claim:** P1 is not a hygiene finding. It produced TWO defects in dispatch-bound work inside one session, both of which reached the operator before detection.

## 1. MEASUREMENT (reproduced, WALTER's own run)

| Surface | Bytes | % of 54,250 B cap | Boot line |
|---|---:|---:|---|
| `anchors/IRAN_WAR.md` | 263,371 | **485%** | step 1 |
| `anchors/IRAN_WAR_HISTORY.md` | 129,568 | **239%** | step 1 |
| `design/ROUTING_TABLE.md` | 120,236 | **222%** | step 6 |
| `MEMORY.md` | 80,100 | **148%** | step 2 |
| `STATUS.md` | 41,464 | 76% (over budget) | step 1 |
| `REGISTRY.tsv` | 33,057 | 61% (over budget) | step 4 |

6 over budget, 4 over the cap. All six are **unscoped `Read …` lines** — the boot step names a whole file.

## 2. WHAT THE BOOT STEP SAYS vs WHAT EXECUTED

- **Says:** boot step 1 — "Read `anchors/IRAN_WAR.md`".
- **Executed 2026-08-28 boot:** `sed -n '1,45p'` — **45 of 818 lines ≈ 4%**.
- The step does not describe the operation. No error, no warning, no truncation notice.

## 3. DEFECT ① — AN ABSENCE ASSERTED FROM A 4% READ

**Context:** Will-Telegram drop BM-20260828-03 item 2 — PressTV, 8/26: *"Oman stops cooperating with US to facilitate escorted tanker movements through southern Hormuz."*
**What WALTER published to the operator:** that the anchor does not carry the claim, and that the resolution path is "UKMTO, Omani MFA, or transit data."
**Ground truth:** `grep -ic oman anchors/IRAN_WAR.md` = **46 hits. Every hit is past line 45.**
**What was in the unread 96% — line 331:**
> "the US-led **JMIC** says the southern Oman-hugging route *'remains open with expanded two-way traffic,'* and CNBC (7/13) reported **8M+ bbl transited Sunday under military escort**"

⇒ The anchor holds the **named counterparty instrument** (JMIC) and the **prior state** for precisely this claim. The operator received a weaker resolution path because the desk could not see its own file.

## 4. DEFECT ② — A SETTLED DENOMINATOR RE-RAISED AS OPEN

**Context:** BM-20260828-02 item 4 — Bloomberg/Goldman: *"Hormuz oil flows recovered to around two-thirds of pre-war levels."*
**What WALTER published:** flagged "two-thirds" as a percentage with no stated denominator, and forwarded the question to BRENT.
**Ground truth — same line 331, adjudicated 2026-07-19:**
> "**~88/day = the canonical baseline**; ~140/day was a PEAK-DAY count mis-cited as a baseline → **do NOT use it**; percent-of-baseline cites **/88**."

⇒ The desk had already resolved the denominator five weeks earlier. A question was routed where an answer existed.

## 5. THE SHAPE — WHY NEITHER DEFECT ANNOUNCED ITSELF

Both reads **succeeded**. Neither errored, neither warned. The file ended where the command stopped, and **"absent past the cut" is byte-identical to "absent."**
This is `SIG-W-20260828-018`, published by this desk the same morning: **a truncating read is not neutral — it CERTIFIES.**
Related: `[[finding_verification_zero_is_ambiguous]]` (a clean check is consistent with "read everything" AND "read nothing") · `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`.

## 6. 🔑 ROOT CAUSE OF THE TWO-MONTH SURVIVAL — THE SELF-CERTIFYING HEADER

`anchors/IRAN_WAR.md` line ~30 states:
> "History archived → `IRAN_WAR_HISTORY.md` (split 2026-06-28 to keep this boot-read file lean). **This file holds ONLY the current verified state + re-verify trigger.**"

The file is **818 lines carrying addenda back to #7 (2026-08-01)**. The split ran ONCE, on 6/28, and the body regrew to **4.9× the cap underneath a header still asserting the split holds.**
⇒ **The header was true when written and became a certification of a condition that no longer obtained.** A reader trusting that sentence has no reason to check the file's size — which is why nobody did for two months.
`[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]` in its purest form.
**Generalisation for P1:** a size remedy that runs ONCE and leaves a permanent claim of leanness behind is worse than no remedy, because it disarms the next check. **Any split/rotation must leave a re-trigger, not a boast.**

## 7. REMEDY OWED (WALTER's, per surface)
1. Anchor — re-run the 6/28 hot/cold split; addenda #7-#21 rotate verbatim to HISTORY; **leave a dated re-trigger, not a leanness claim** (per §6).
2. Boot step 1 rewritten to name what is READ (current-state block + guard ladder); remainder marked grep-on-demand.
3. `ROUTING_TABLE.md` 222% — hot/cold; By-Tag/By-Verdict rules are boot-read, per-agent history is not.
4. `MEMORY.md` 148% — trim at next Tier-2 under the existing >100-line rule (already in arrears).
