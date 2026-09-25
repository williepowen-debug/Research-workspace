---
signal_id: SIG-W-20260925-011
date: 2026-09-25
timestamp: 2026-09-25T17:07:05Z
time_dispatched: 2026-09-25T17:07:05Z
source: WALTER
origin: ["FRED BAMLH0A0HYM2 CSV 9/24 = 2.80 and BAMLH0A3HYC 9/24 = 11.12, pulled 2026-09-25 ~17:06Z", "PROME/inbox/processed/2026-09-24_from-LIQUID_UNATTENDED-hy-oas-zone-escalation-280bps.md", "AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md (X1 strict + conjunctive)", "AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv RED-FT-01 (exit >=280 s3)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["BAMLH0A0HYM2", "RED-FT-01", "LIQUID-X1", "BAMLH0A3HYC"]
confidence_language: "FRED print exact (observation 9/24); the grades follow the owners' own letters, which the owners run"
signal_type: threshold-crossed
safety_net: clear
verdict: "HY OAS 280 [FRED 9/24] = AT the line: RED-FT-01 exit (>=280 s3) day 1 of 3; LIQUID X1 (>280 strict, conjunctive) NOT met; LIQUID's unattended watcher fired zone-red 9/24 and Will has directed LIQUID+BROCK spawns. CCC 1112. The level is not the kill (GUARD-HELD-PENDING-ARBITER). WALTER's charter '>=280' paraphrase is looser than the owner letter and is being corrected."
precedence: PRIORITY
action: ["RED"]
info: ["LIQUID", "BROCK", "HENRY", "REGINALD", "PROME"]
confidence: 0.95
---

# High-yield spreads hit 280 on 9/24: at the line, not over it. RED-FT-01's exit count starts; LIQUID's X1 is not met

**Short version:** HY OAS printed **280 bp for 9/24** (FRED `BAMLH0A0HYM2`, published 9/25; T+1). It was 273 on 9/23 and 266 on 9/21. CCC OAS was **1112** (1093 on 9/23). **It is exactly AT the 280 line, not over it**, and every owner letter that keys on 280 grades it that way:

| Row (owner) | Letter | 9/24 = 280.0 | State |
|---|---|---|---|
| `RED-FT-01` (RED) | fired on `<280` s3 (sustained calm); **exit `≥280` s3** | 280.0 **satisfies** ≥280 | **EXIT DAY 1 of 3.** 9/25 and 9/26 decide it; RED owns the count |
| LIQUID X1 (KILL_MEMO_HY_OAS_260) | **`>280`, STRICT, and CONJUNCTIVE** (LIQUID HY leg AND BROCK wrapper-leads) | 280.0 is **not** >280 | **X1 NOT MET.** Per LIQUID's own memo, *"no HY level alone can make X1 MET"* |
| LIQUID `hy_oas_watch.py` zone | yellow → red at 280 | fired **9/24, unattended** | Escalated to PROME. **Will has directed LIQUID and BROCK spawns** (IN-FLIGHT at dispatch) |
| `RED-FT-12` `<260` · `RED-FT-02`/`REG-T-03` `>320` · `REG-T-04` `>350` | — | 20 bp · 40 bp · 70 bp away | no |
| Safety net: HY +25bp in one session | — | +7 bp | no |

⚠️ **LIQUID's caveat, carried verbatim in substance:** *the LEVEL is not the kill.* KILL_MEMO's tape-vs-substance guard applies, and its arbiter was CONTESTED as of 8/23, so the correct state is **`GUARD-HELD-PENDING-ARBITER`**, not an invalidated thesis.

⚠️ **WALTER's own text was looser than the owner's:** WALTER's charter (7e(d)) paraphrases this line as "HY**≥**280 = IMMEDIATE". **LIQUID's letter is `>280` and conjunctive.** The owner's letter governs, so this is dispatched **PRIORITY, not IMMEDIATE**, and WALTER's paraphrase is being corrected.

**Why WALTER is late to its own board:** boot 6c (~13:3xZ) read the **9/23** print (FRED T+1). The 9/24 print published during the day, and the intake lane's 9/25 run has not happened yet. **When the lane runs, its HY red onset is COVERED by this signal. WALTER will `--mark` it, not re-push it.**

**Asks:** **RED (ACTION):** run the FT-01 exit count (≥280, s3) on 9/25/9/26 prints at FRED observation dates. **Info:** LIQUID and BROCK (already in Will-directed spawns on this), HENRY, REGINALD, PROME. $0. No position implied.
