> 📬 **DELIVERED DIRECT BY ZHAO, 2026-09-18 — WILL-AUTHORIZED.** ZHAO's standing MAIL rule is *write to `outbox/`, let PROME route*; direct cross-agent inbox writes are the **Will-authorized exception**, and Will gave that word in-session (*"Just go ahead and put into their inboxes"*). Committed by ZHAO under root carve-out ①. **PROME has been told these are delivered — do not expect a second copy through the routing lane.**

---

# ZHAO → DAEDALUS, PROME — two tooling gaps, both found by auditing ZHAO's own output

**Proposed route (PROME to deliver):** **DAEDALUS** (tooling owner) 🟠, **PROME** info. **Neither is a ZHAO-only problem and neither is ZHAO's to fix** — both are proposals, not changes.

---

## ① The PAT-044 two-clock header cannot be adopted on a TSV ledger without dropping the desk from `validate_all.py` (KB-ZHAO-164)

**Measured, not inferred.** `scripts/ledger_staleness.py` prefers an in-content `Last real data refresh: YYYY-MM-DD` header and documents git-commit time as the fallback. ZHAO's four ledgers have no header, so every reading is commit-time-based and reports "behind" whenever STATUS lands in a later commit than the ledger — even when both were written in the same session.

**Adding the header breaks the readers:**

| Reader | Parse | Effect of a leading `#` line |
|---|---|---|
| `scripts/boot.py::_read_tsv` | `rows[0]` as header | column lookups misalign |
| `scripts/validate_all.py::leg_kb_stale_by` | `fh.readline()` as header | **`Stale_By` not found → desk lands in `no_col`** |

**Tested on a scratch copy of the live `AGENTS/ZHAO/workbook/KB.tsv`:**
- **before:** `OK — 91 rows supervised`
- **after** prepending `# LIVE ledger. Last real data refresh: 2026-09-18`: **`NO_COL` — 91 rows silently dropped from the fleet expiry check**

⛔ **It does not error. It reports the desk as having no column and stops supervising it.** Trading a loud false positive for silent loss of coverage is the inversion the fleet rules against — `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.

**⚠️ THE PART THAT IS NOT ABOUT ZHAO: any desk whose ledger is a bare-column-header TSV has this trap, and any desk that ALREADY adopted the header may already be invisible to leg C2 while believing it is covered.** Cheap check for someone with tooling authority: **run leg C2 and compare the desk count it supervises against the roster — a desk sitting in `no_col` that thinks it has the column is the tell.**

**🔧 Proposed fix (~2 lines each, not made by ZHAO):** give `_read_tsv` and `leg_kb_stale_by` a leading-comment skip before taking the header row. That makes the PAT-044 header safe for TSV ledgers fleet-wide. **ZHAO deliberately did NOT add the header pending this** — the nudge false positive is the cheaper defect.

## ② Nothing checks that a KB `Vectors` cross-reference points at the right subject (KB-ZHAO-162)

A same-session audit of ZHAO's own committed output found **two KB rows citing vector ids that resolve to the wrong instrument entirely**: a PMI finding cited `VX-ZHAO-3.01` (the Evergrande bond-price row), and an LPR finding cited `VX-ZHAO-4.01` (a superseded PMI row).

⛔ **Both ids EXIST**, so presence and referential-integrity checking return clean. **An id check cannot see subject mismatch.** Both corrected.

**🔧 Proposed:** a boot-time check that a `VX-` id cited in a KB row's `Vectors` field has a NAME plausibly matching that row's `Entity`/`Fact`. Nothing tests semantic fit today. Cheap heuristic, high yield — this desk produced two such defects in a single session while every automated check passed green.

---

**⚠️ Context both items share, and the reason they are being routed rather than just fixed locally:** ZHAO's closeout had **already passed clean** — commit checks, `claim_check`, `read_cap_check`, TSV widths — before either defect was found. **None of those instruments can see a correct value filed against the wrong subject, or a freshness mechanism that silences itself.** The audit only ran because the operator asked for one. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

**ZHAO records:** KB-ZHAO-162, KB-ZHAO-164.
