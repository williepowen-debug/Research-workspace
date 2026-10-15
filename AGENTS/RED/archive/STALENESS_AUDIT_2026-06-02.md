# RED Data-Structure Staleness Audit — 2026-06-02 (Session 16)

**Trigger:** Will — "look for stale data/files within RED's data structure that we should update, prune, address."
**Scope:** Full RED directory + workbook TSVs + live files. Two tracks: (A) file hygiene, (B) stale *data* in live files.
**Method:** mtime survey (noted: most mtimes are git-checkout artifacts, not content age — triaged on *content* dates), checksum dedupe, field-level TSV review against current thesis state, live-anchor refresh via repaired market tool.

---

## 0. Infra fix (prerequisite)

**The `.venv` did not exist** — `.venv/bin/activate` absent; system python3 had no pip (`No module named pip`); `python3 -m venv` failed (ensurepip/`python3.12-venv` not installed, needs sudo). **Recreated without sudo:** `python3 -m venv .venv --without-pip` → bootstrapped pip via `get-pip.py` → `pip install yfinance requests` (pulled pandas/numpy/curl_cffi etc.). **Validated:** `fetch.py price` returns live data. This unblocks RED's live-anchor discipline (was relying on PROME dashboard reads).
> NOTE for future sessions: if the venv breaks again and apt isn't available, repeat the get-pip bootstrap. The repo `.venv/` is gitignored (not committed).

**Live anchors captured 6/2 (green/risk-on day):** VIX **15.80** (−1.56%, sub-16), WAL **$80.20** (+2.30%, back above $78), KRE $69.53, OZK $48.54, TLT $85.65, HYG $79.90, 10Y 4.45%.

---

## A. FILE HYGIENE — EXECUTED

| Action | Files | Disposition |
|---|---|---|
| **Dedupe** (md5-identical archive↔challenges) | SSB_CHALLENGE_SUMMARY, SSB_CHALLENGE, SAM_CHALLENGE_V2, SSB_CHALLENGE_V2, NETWORK_SWEEP_2026-02-12 | `git rm` the 5 **archive/** copies; kept canonical in **challenges/** + git history |
| **Relocate completed work** | VIOLET skew recheck bundle (10 files incl 1.78MB `skew_vix_vvix_full.csv` + 3 `.py` + result CSVs + 3 TIER_RECHECK.md) | `git mv research/ → archive/violet_skew_recheck_apr2026/`. CHG-RED-023 RESOLVED-CONVERGED; decluttered active research/ |
| **Relocate superseded schemas** | `CHALLENGES_old_6col.tsv`, `VX_old_7col.tsv`, `ML_old_7col.tsv` | `git mv workbook/ → archive/superseded_workbook/` |
| **File integrated signal** | `HAWK_ROUTING_2026-05-22.md` (was loose in inbox/) | `git mv → inbox/processed/`. Content (HAWK scenario stepdown C/Grind 55%) already integrated in RED War-Escalation 6% / Brent-weakest-leg read |

---

## B. STALE DATA — EXECUTED

### B1. CALENDAR.md
- **Fixed contradiction:** RED-19 scoring window said "ACTIVE-RIGHT (408 May 1; verify)" while the header said "RED-19 falsified." → corrected to **RESOLVED WRONG** (rigs 429).
- Refreshed FALSIFICATION WATCH spot values to live: VIX 17.61→**15.80**, Brent $107→**$94.78**, HY OAS 276→**272**, claims 211K→**~209K**.
- Brent <$95 sub-trigger (d): **price leg now at/below $95** (was "clear from <$95").
- Added **VIX<16 DIET guard** to the falsification row. Header bumped to S16.

### B2. workbook/VX.tsv (the highest-value find — vectors un-reviewed since mid-April)
8 status/weight changes + 12 Last_Reviewed refreshes, **all logged to VX_HISTORY.tsv** (20 rows):

| VX | Was | Now | Reason |
|---|---|---|---|
| VX-RED-002 Real Wage Growth | MODERATE 45/55 | **FLIPPED-BEAR 15/85** | Flip_If FIRED — real wages negative 3 consec months (CARL 5/26 K-shape, bottom tercile −2.3pp) |
| VX-RED-004 Japan Muddle | MODERATE 35/65 | **FLIPPED-BEAR 20/80** | Flip_If FIRED — 30Y JGB 3.859% > 2.5%; BOJ Jun hike 88% |
| VX-RED-011 Earnings vs CARL | STRONG | **RESOLVED-BEAR** | "Testable now" — WAL+OZK both missed Q1 |
| VX-RED-018 SOFR-IORB | MODERATE | **RESOLVED-MECHANICAL** | LIQUID 5/18 confirmed tax-day TGA, not structural |
| VX-RED-019 Oil Paper-Physical | STRONG | **RESOLVED** | Apr 22 binary passed; spread collapsed, Brent ~$95 |
| VX-RED-020 Bank Cohort Fade | MOD-STRONG | **RESOLVED-BEAR** | WAL+OZK both missed Apr 21 |
| VX-RED-023 WAL V2.0 | STRONG | **RESOLVED-CONVERGED** | REGINALD V2.2 absorbed CHG-RED-025/026 |
| VX-RED-016 AAPL Concentration | "45% of portfolio" | **20.08% (corrected)** | Verified vs 5/21 broker CSV — was stale; still largest equity holding but ~half the logged figure |

Remaining 12 active vectors (001/003/005/006/007/008/009/010/012/013/014/015/021) got Last_Reviewed bumped to 6/2; directions still valid (per-vector notes in VX_HISTORY).

### B3. workbook/KB.tsv (Stale_By backlog — ~30 entries overdue 5-8 weeks)
- **14 SUPERSEDED** (point-in-time April facts overtaken): KB-RED-015 (Russia sanctions), 019 (CDX/cash, RED-06 wrong), 021/022 (SSB closed), 024 (GDPNow→actual 1.6%), 025 (savings 4.5%→2.6% collapse), 027 (Brent $141 peak), 028/032 (matured into bifurcation), 029 (gold), 031 (Kharg), 036 (SOFR mechanical), 037 (Brent $88.87), 038 (Q1 cohort).
- **8 EXTENDED** (live themes, Stale_By→2026-08-31/09-30 with review notes): KB-RED-010 (unanimity), 011 (claims), 013 (retail), 016 (policy — noted Waller weakened it), 026 (employment), 033 (PC gating), 034 (energy HY — noted oil-$94 weakens premise), 039 (bifurcation — THE live theme).
- **Schema fix:** normalized 2 pre-existing ragged rows (KB-RED-002 was 12-col missing Vectors; KB-RED-042 was 14-col stray field) → all 42 rows now uniform 13-col.

---

## C. FLAGGED FOR WILL — touch RED's documented charter, not changed unilaterally

1. ~~**Two divergent PREDICTIONS files.**~~ **✅ RESOLVED S16 (Will-directed).** Investigation found `thesis/PREDICTIONS.tsv` was worse than stale — the unreconciled pre-ML-RED-068 fork with *contradictory IDs* (May predictions mis-numbered RED-11–14, conflicting with canonical RED-16–19; missing the Apr-18 batch + RED-15–19). Retired: archived verbatim → `archive/superseded_workbook/PREDICTIONS_thesis_unreconciled_PRE-ML-RED-068.tsv`; breadcrumb `thesis/PREDICTIONS_README.md`; CLAUDE.md updated (workbook sole canonical); WALTER pinged (RED-TO-WALTER-20260602-001) to fix CROSS_REFS cache. See MAINTENANCE.md.
2. **RED_SKELETON.md references.** MEMORY says it was DELETED Apr 5; a copy survives in `archive/RED_SKELETON.md` (fine). But CLAUDE.md still lists it as a live reference in 3 places (lines 146/190/271). **Recommend:** prune those CLAUDE.md references or relabel as "archived." (Not done — CLAUDE.md is RED's charter.)
3. **thesis/TIMELINE.md** (Apr 20) — likely stale (position/expiry mismatch analysis predates the Jun stack capitulation + channel migration). Worth a refresh pass when time permits.

---

## What this audit did NOT touch
- Active research/ docs (CATALYST_FRAMEWORK_APR2, MI3_5_15_DECISION_TREE, WAL_OZK_APR21_FRAMEWORK, WAL_V20_STRESSTEST, CEASEFIRE_FADE_PROTOCOL, POSITION_TIMELINE_STRESS, APO_ROLL_DECISION_*) — historical analysis records, kept as audit trail. Several are event-resolved (Apr 21/22) and could be archived in a future pass, but they're not *misleading* where they sit.
- Full content re-review of the 12 still-active VX vectors and 8 extended KB entries — refreshed dates + spot-noted; a deep per-vector re-derivation is the natural next hygiene pass.

*Audit complete. File hygiene + the two highest-value data systems (VX vectors with fired triggers, KB Stale_By backlog) are current. Three structural items flagged for Will.*
