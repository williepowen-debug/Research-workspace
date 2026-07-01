# ACTION-CARD — Verification Pass: front-half cluster load-bearing numbers
**Created:** 2026-06-25 (eve) by Claude Code Prome · **For:** next-session Prome / a DEWEY-style verification agent · **Status:** QUEUED

## Why
The 2026-06-25 front-half cluster produced 4 strong synthesis docs, but ~25 load-bearing **numbers are agent-generated and unverified** against primaries (repo rule #3 — agent data can be hallucinated). The adversarial round already caught 2 stale figures slipping through (continuing-claims velocity; a "triangulated" claim). Before any of this is **trade-load-bearing**, verify the figures the grading instrument + reconciliation hang on. Output upgrades the grading-instrument baselines from "verify before trade" to **VERIFIED / CORRECTED**.

**Targets to update on completion:** `PROME/synthesis/2026-06-25_Q2-bank-print-grading-instrument.md` (the Q1 baselines), `_front-back-reconciliation.md`, `_front-half-demask-cluster.md`. Grep each for a corrected figure and propagate (numbers carry across docs — [[finding_number_carries_threshold_unit_source]]).

## Execution
Spawn RESEARCH/DRAFT-ONLY (output to me / a proposals file, NOT canonical agent edits). A per-name pipeline Workflow fits (~25 items / 5 sources). Tooling:
- **EDGAR 10-Q:** declared User-Agent header (DEWEY `edgar_doc.py` / `pdf2text.py`; [[finding_edgar_403_user_agent_header]]).
- **FRED:** `FORGE/tools/market-data/fetch.py fred <series>` via `.venv` python (NOT system).
- **DOL ETA claims:** WebFetch 403s the PDF → use declared-UA or FRED `ICSA`/`CCSA`.
- **FDIC Call Report (OZK — no 10-Q):** FFIEC CDR.
- **BLS:** FRED series or BLS API.

## Discrepancy rule
Primary wins. If a fresh primary pull conflicts with the agent figure, the **agent figure is suspect** (here the agent number is the unverified side — note this is the inverse of [[feedback_suspect_fresh_pull_over_curated_record]], where the *curated record* was trusted; cross-check year/unit/threshold either way). Material discrepancy → flag + correct + propagate. Confirm the YEAR on every metric ([[finding_subagent_year_verification]]).

---

## TIER 1 — grading-instrument Q1 baselines (HIGHEST priority; BUILD/RELEASE thresholds depend on these)
| Name | Claimed (agent, Q1'26) | Pull |
|---|---|---|
| **SYF** | NCO 5.42%; ACL coverage **10.42%** (+36bps QoQ); FY26 guide <5.5% (was 6.0%) | SYF Q1'26 10-Q + release |
| **ALLY** | retail-auto NCO 1.97%; 30+ DQ 4.6%; ACL **release ~$224M**; S-tier 37%; nonprime 10.1% | ALLY Q1'26 10-Q |
| **COF** | card NCO 5.1%; ACL **build $230M** ($155M subprime-tied); auto orig +21% YoY | COF Q1'26 10-Q + supplement |
| **EGBN** | nonaccrual coverage **114%** (was 149%); NPA **1.31%** (was 1.04%); IPRE +23%; CRE 547%/DC 100% | EGBN Q1'26 10-Q |
| **WAL** | NCO **39bps**; classified **1.08%**; **$99M** life-sci credit | WAL Q1'26 10-Q (REG had primary — reconfirm) |
| **OZK** ⚠️ | past-due **$465M/1.41%**; NCO 0.57%; NPA $451M; RESG 88% | **FDIC Call Report — NO 10-Q** (landmine) |
| **ZION** | NCO **0.03%**; muni **$5.78B** AFS; Basel III +93bps | ZION Q1'26 10-Q |
| **CFG** | NCO **0.39%**; consumer 18.7% housing-secured; BDC fund-fin $12.5B | CFG Q1'26 10-Q |

## TIER 2 — labor (the U-3 + white-collar read)
| Figure | Claimed | Pull |
|---|---|---|
| Continuing claims | **1,821K (w/e Jun 13)**; velocity **+21K vs +50K DISPUTED** (resolve) | DOL ETA / FRED `CCSA` |
| Initial claims | 215K (Jun 20) / 226K (Jun 13) / 229K (Jun 6) | FRED `ICSA` |
| White-collar contraction | **31 consecutive months**; financial **−107K YoY**; prof-biz openings **<1M** (1st since Apr'20) | BLS CES + JOLTS (FRED) |
| LTU | **27.5%** aggregate; mgmt-occ **25.4%**; recent-grad UR 5.6-5.7% | BLS A-12 / NY Fed |
| FL UR ⚠️ | **4.8% (or 4.9?)** + **40.5K jobs** (LABOR flagged ambiguous) | BLS LAUS (landmine) |
| Headline | U-3 4.3%; NFP +172K May; +93K revisions | BLS (FRED `UNRATE`/`PAYEMS`) |
| Immigration | 2.2M removal (CBO); ~1.5-1.9M LF; breakeven ~0-50K/mo | CBO / KC Fed / Brookings (model, not a single pull — mark estimate) |

## TIER 3 — flagged-uncertain / research-grade (HIGHEST discrepancy risk — verify or re-mark)
- **OZK** — no 10-Q → FDIC Call Report (may lag the print).
- **AMTB ~45% ACL** — EDGAR 403'd last attempt; declared-UA. If still blocked, mark **unverifiable-by-construction** ([[finding_private_by_construction_unverifiable]]), don't leave as "unverified-pending."
- **FL UR** — LAUS 4.8 vs 4.9 ambiguity.
- **Continuing-claims velocity** — +21K vs +50K (base-week dependent; state the base).
- **Student-loan default ~9.16M** — Bloomberg-sourced (secondary); find the primary (ED/NY-Fed).

## TIER 4 — macro/regime (low-risk; confirm fresh + the 6/30 re-pull)
- HY OAS 276 / CCC 964 / CCC-HY 3.49× [6/24] → FRED `BAMLH0A0HYM2` / `BAMLH0A3HYC`.
- **10Y: re-pull at the 6/30 mark** (4.30 [3/31] → 4.41 [6/24]) → FRED `DGS10`. *(This also feeds AOCI path (b) — load-bearing for the Q2 grade.)*
- Bank prices [6/25] → `fetch.py price`.

## Migration (TIER 2-3, harder)
Canadian −28.7% 2-yr stack (StatCan); WestJet 41 routes/24 US (schedule); Air Transat US exit Jun 30; **FL-$ hole ~$850M = a MODEL estimate**, not a single pull — verify the *inputs* (capacity cuts, Canadian-spend base), mark the $850M as derived.

---

## Output spec
1. **Verified-vs-claimed table** per figure: `claimed | verified | source + as-of | match? (✓/✗/Δ) | action`.
2. **Discrepancy log** — every ✗/Δ: the correction + every doc/section it propagates to.
3. **Update the grading instrument** baselines: `[VERIFIED 06-26]` or `[CORRECTED: was X → Y, source]`. Demote any structurally-unavailable figure to `unverifiable-by-construction` with its recovery path.
4. **One-line verdict:** does the trade thesis ((b) AOCI + (c) WAL = the Q2 exception; (a) trimmed) survive verification, or does a corrected figure move a path's odds?
