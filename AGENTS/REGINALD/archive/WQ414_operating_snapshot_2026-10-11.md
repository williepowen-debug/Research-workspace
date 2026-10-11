# WQ-414 operating preservation snapshot — 2026-10-11

HISTORICAL / NOT CURRENT. Verbatim pre-encode surfaces at plan checkpoint; originals unchanged in Git. No figures below are a current quote or current alarm consequence. Each fenced block CRC applies to its exact UTF-8 contents, excluding fence syntax.

## registry/THRESHOLDS.tsv

crc32 04e29b67; bytes 3523

````text
trigger_id	metric	threshold_op	threshold_value	sustain_window	action	recipient_chain	threshold_thesis_ref	grading_instrument	value_unit	value_basis	sustain_unit	exit_condition
REG-T-01	KRE-PRICE	<	60	1	ALL-ALL-ACUTE	REGINALD action / ALL-AGENTS info / Will	STATUS.md#kre-acute-trigger	scripts/market.py -> Yahoo Finance ticker KRE	USD	regular-session close, unadjusted, per-share	consecutive daily closes	KRE >= 63.00 on 3 consecutive daily closes (entry level +5% hysteresis)
REG-T-02	WAL-PRICE	<	78	1	V1V3-ACCELERATE	REGINALD action / WAL action / Will	STATUS.md#wal-v1v3-thesis	scripts/market.py -> Yahoo Finance ticker WAL	USD	regular-session close, unadjusted, per-share	consecutive daily closes	WAL >= 81.90 on 3 consecutive daily closes (entry level +5% hysteresis)
REG-T-03	HY-OAS	>	320	3	CREDIT-CANARY-FIRED	REGINALD action / CARL info	STATUS.md#hy-oas-canary	FRED series BAMLH0A0HYM2 (ICE BofA US High Yield Index OAS)	bps	option-adjusted spread, daily close, ~1 business-day publication lag	consecutive daily closes	HY-OAS <= 300 on 5 consecutive daily closes
REG-T-04	HY-OAS	>	350	3	ISSUANCE-FREEZE	REGINALD action / LIQUID action / Will	STATUS.md#hy-oas-issuance-freeze	FRED series BAMLH0A0HYM2 (ICE BofA US High Yield Index OAS)	bps	option-adjusted spread, daily close, ~1 business-day publication lag	consecutive daily closes	HY-OAS <= 330 on 5 consecutive daily closes
REG-T-05	INITIAL-CLAIMS	>	300	1	ORANGE-TO-RED	REGINALD action / CARL LABOR info	STATUS.md#claims-trigger	FRED series ICSA (weekly initial claims, seasonally adjusted)	thousands of persons	weekly SA headline print, first release; revisions do NOT retro-fire	consecutive weekly prints	ICSA <= 275 on 3 consecutive weekly prints
REG-T-06	FHLB-ADVANCES	>	700	3	EARLY-CRISIS	REGINALD action / LIQUID info	STATUS.md#fhlb-early-crisis	FHLB Office of Finance Combined Financial Report, system advances line	USD billions	system-wide period-end advances balance, all 11 banks combined	consecutive quarterly prints	FHLB-ADVANCES <= 650 on 2 consecutive quarterly prints
REG-T-07	OFFICE-CMBS-DQ-TREPP	>	15	3	CRE-ACCELERATE	REGINALD action / CREED info / BROCK SHADE info	STATUS.md#cmbs-cre-transmission	Trepp monthly CMBS Delinquency Report, OFFICE sector (see registry/NOTES.md REG-T-07)	percent	30+ day delinquency RATE on office CMBS balance; NOT special-servicing rate; NOT Fitch overall || ⚠️ TWO REGISTERED BARS SIT ON THIS ONE SERIES (CREED ask, 2026-08-20): REG-T-07 >15 sustain-3 (bank-relevant recognition bar, REGINALD) and CREED-T-01a >12 sustain-2 (CRE-stress-confirmed bar, CREED). The levels DIVERGE DELIBERATELY and must NOT be reconciled to one number. Reading either alone is not the whole picture. July-2026 print = 11.91 (REG-T-07 3.09pp away; CREED-T-01a 0.09pp away). August-2026 print = 12.00 [Trepp, published 2026-09-01; CREED at publisher; via WALTER SIG-W-20260903-006, logged 2026-09-11] -> REG-T-07 is 3.00pp away, sustain 0; CREED-T-01a NOT FIRED (band is STRICT >12; 12.00 is not >12), sustain 0. CREED ask 8/20 (CREED as info + two-bars note): ALREADY ENCODED on this row -- recipient_chain carries CREED info; VERIFIED 2026-09-11.	consecutive monthly prints	OFFICE-CMBS-DQ-TREPP <= 13.5 on 3 consecutive monthly prints
REG-T-08	SOFR-IORB	>	15	3	LIQUID-FHLB-SPIKE	REGINALD action / LIQUID action / Will	STATUS.md#sofr-iorb-fhlb	FRED series SOFR minus FRED series IORB	bps	daily published SOFR less interest on reserve balances, same trade date	consecutive daily prints	SOFR-IORB <= 8 on 5 consecutive daily prints
````

## registry/NOTES.md

crc32 f4ce4fc1; bytes 48206

````text
# REGINALD registry — row notes

**Created:** 2026-07-30 · **Owner:** REGINALD
**Why this file exists:** `THRESHOLDS.tsv` is a strict 8-column TSV with no notes column, so a row cannot carry its own rationale without breaking the schema. Anything a reader needs *in order to evaluate a row correctly* lives here, keyed by `trigger_id`. **A row with an entry below cannot be read safely from the TSV alone.**

**Rule:** notes record *measurement basis, provenance, and deliberate divergences*. They never restate or modify a level, operator, window, or action — those live in the TSV and move only by an explicit ruling.

---

## `REG-T-07` — OFFICE-CMBS-DQ-TREPP > 15, sustain 3

**⚠️ Evaluation basis is load-bearing and was previously ambiguous. Two providers publish "office CMBS delinquency" and they sit ~8pp apart.**

| Evaluate against | June 2026 | Distance to the >15 fire |
|---|---|---|
| ✅ **Trepp office DQ** — THE basis for this trigger | **11.91%** [July 2026] | **3.09pp** |
| ❌ Fitch *overall* CMBS DQ (different universe **and** different scope) | 3.31% (May) | 11.7pp — reads "nowhere near" |

**History.** Until 2026-07-30 the metric field read the un-provisioned `OFFICE-CMBS-DQ`, while my STATUS dashboard row under the heading "Office CMBS DQ" carried the **Fitch overall** figure. Both numbers are correct for what they measure; the defect was **a wrong denominator under the right label**, which makes the gate look ~3.5× further from firing than it is. Found by **CREED 2026-07-27** (`inbox/processed/2026-07-27_from-CREED_REG-T-07-fires-on-my-series...`) in a Will-directed structure survey. Same provider-stacking class as `[[finding_blended_index_masks_bifurcation]]`.

**Edits made 2026-07-30 (PROME-ruled GO; disambiguation, not level moves — no level, operator, window or action changed):**
1. metric `OFFICE-CMBS-DQ` → **`OFFICE-CMBS-DQ-TREPP`**
2. recipient chain += **`CREED info`** → `REGINALD action / CREED info / BROCK SHADE info`

**★ The divergence from CREED's trigger on the same series is DELIBERATE — recorded here because nothing previously recorded that anyone had compared them.**

| | metric | op | level | sustain | purpose |
|---|---|---|---|---|---|
| **`REG-T-07`** (mine) | OFFICE-CMBS-DQ-TREPP | > | **15** | **3** | **bank-transmission ACCELERATE gate** — the point at which securitized office stress is severe and persistent enough to argue transmission into bank-held CRE |
| **`CREED-T-01a`** (CREED's) | OFFICE-CMBS-DQ-TREPP | > | **12** | **2** | **RECOGNITION gate** — earlier, faster, fires when the market is acknowledging the stress |

Different questions of the same series ⇒ different levels are correct, not a conflict. **Do not "reconcile" them to one number.** CREED owns the series; **CREED had me as `action` on its trigger while I had CREED on none of mine** — that asymmetry is what item 2 fixes.

⚠️ **Bank-HELD ≠ securitized.** This trigger reads a CMBS series and is an *input* to a bank-transmission argument, never direct evidence of bank-held CRE deterioration. The bank-held/CMBS gap is tracked separately (~7.5pp as of the STATUS row).

---

## `REG-T-02` — WAL-PRICE < 78, sustain 1

**Chain provenance.** Reads `REGINALD action / WAL action / Will` as of 2026-07-29. The `WAL action` leg was added post-WAL-promotion by **RAV Codex** (Will's outside continuity tool, commit `383bf581`), WALTER diff-verified 7/30 (`SIG-W-20260730-008`), and **re-verified at source by REGINALD 7/30** rather than accepted on the relay. No further edit is owed; WALTER's 7/25 packets asking for it are **superseded**.

### ⚖️ EXIT GRADE 2026-09-11 (owner, REGINALD — drain session, desk dark 9/3→9/10) — **FIVE closes graded, 9/3 → 9/10: ALL NOT QUALIFYING. State stays `FIRED`; exit run `0-of-3`.** Gate row: **`GATE-TERRY-ROLL70-EXIT`** (`PROME/GATES.tsv`, registered 9/3; PROME 9/3 read-path packet — gate_id named here per GATES REGISTRATION JOIN RULE ②, so the row is DELIVERED).

| Close | WAL | vs 81.90 | Day | Qualifying | Run |
|---|---:|---|---|---|---|
| Thu 9/3 | **$81.00** | $0.90 / 1.11% short — **closest approach of cycle 2** | +$1.88 / +2.38% | NO | 0-of-3 |
| Fri 9/4 | $80.95 | $0.95 / 1.17% short | −$0.05 / −0.06% | NO | 0-of-3 |
| Tue 9/8 | $79.94 | $1.96 / 2.45% short | −$1.01 / −1.25% | NO | 0-of-3 |
| Wed 9/9 | $79.66 | $2.24 / 2.81% short | −$0.28 / −0.35% | NO | 0-of-3 |
| Thu 9/10 | $79.28 | $2.62 / 3.30% short | −$0.38 / −0.48% | NO | 0-of-3 |

> **Instrument:** yfinance daily bar (`history()`, unadjusted), pulled **2026-09-11 11:22 ET**; **VERIFIED** against the consumer captures already on the board — PROME/TERRY Yahoo-mirror 9/3 $81.00 · 9/4 $80.95 · 9/8 $79.94 (TERRY 9/8 packet, `PROME/reports/2026-09-08_owed-market-checks_evidence.json`), WALTER `SIG-W-20260903-002` ($81.00) and `SIG-W-20260908-008` ($79.94), PROME's 9/11 spawn census 9/9 $79.66 · 9/10 $79.28. **Seven pulls, zero disagreements.** Mon 9/7 = Labor Day, no session. **Fri 9/11 is INTRADAY at grading time ($78.76 at 11:22, L $77.85) and is NOT graded** — `value_basis` is the settled regular-session close.
> **The run never started.** No close reached $81.90; the nearest was 9/3, and the tape has moved AWAY from the exit since (81.00 → 79.28, −2.12% over four sessions). Distances above are each re-derived from the named dated close (÷ close basis) — nothing carried.
> ⛔ **Two errors this grade exists to prevent, both live on today's tape:** ① every close 9/3→9/10 was ABOVE $78 — **none is an un-fire**; the state clears ONLY on `≥81.90 ×3`. ② 9/10's intraday low $77.89 and 9/11's $77.85 are sub-78 PRINTS, not closes; **even a sub-78 CLOSE would be a SUPPRESSED re-entry inside the fired state, not a second fire** — log it, do not route it.
> **Routing:** NONE owed at 0-of-3 (TERRY's 2-of-3 packet ask is unmet; the registered announcement fires at 3-of-3). TERRY's 9/8 ask for the 9/3 / 9/4 / 9/8 owner observations is ANSWERED by the table above + `REG_T02_EXIT_LOG.tsv`, delivered via the PROME memo `PROME/inbox/2026-09-11_from-REGINALD_*.md` (this session is boundary-scoped to `AGENTS/REGINALD/` + that one packet; no TERRY-inbox packet written).
> **`PROME/GATES.tsv` row `GATE-TERRY-ROLL70-EXIT`:** the `state` / `last_checked` cells were NOT edited by me — the grade text is delivered in the 9/11 memo for PROME to encode (PROME is live this sitting; a concurrent edit to a PROME-owned file is root rule #2's exact case). Consequence unchanged: the Dec-18 $70P ×1 (Robinhood) stays open under TERRY's card; time stop 2026-12-04; harvest ≥$4.40 is a MANUAL act (WQ-167).

### 📐 AS-MADE AUDIT RECEIPT — COMPLETION 2026-10-10 (all 20 rows; closes DAEDALUS H2 packet 9/7 + PR#6 ask 3)

**Why the 9/11 receipt was partial:** it searched `STATUS.md` history only, as the tool does. **This desk registered its predictions in `AGENTS/REGINALD/PREDICTIONS.md`** (born `1c0b3d0cb` 2026-02-16, +5 rows `73e3253a5` 2026-02-23, migrated to TSV and emptied `65e054448` 2026-03-05). The 12 NOT-FOUNDs are a search-perimeter gap, not missing registrations. Every row below was re-derived by prediction TEXT at those blobs (commands: `git show <blob>:AGENTS/REGINALD/PREDICTIONS.md`, and a per-commit trace of the Confidence column across both TSV paths).

| Row | First registration (by text) | As-made | Later dated pre-resolution mark | Scores (WQ-112(i)) | Status |
|---|---|---|---|---|---|
| REG-01 | STATUS `67d336e32` 2026-02-12 | 90% | — | 90% | OPEN (Kernel-pinned) |
| REG-02 (Phoenix) | STATUS 2026-02-12 | 65% | — | — | EXPIRED-UNGRADEABLE |
| REG-03 | PREDICTIONS.md `1c0b3d0cb` 2026-02-16 | 70% | — | 70% | OPEN |
| REG-04 (FHLB >$600B) | STATUS 2026-02-12 | 60% | — | — | RETIRED-UNINSTRUMENTED |
| REG-05 | PREDICTIONS.md 2026-02-16 | 40% | — | — | RETIRED-UNINSTRUMENTED |
| REG-06 | STATUS 2026-02-12 | 50% | **10% [2026-08-27]** (`3ae52ac59`, Notes) | 10% | OPEN (Kernel-pinned; cell not re-formed) |
| REG-07 | STATUS 2026-02-12 | 55% | **68% [2026-03-05]** (`35de73fe2`, ML-REG-110) | **68%** | OPEN, grades 10/21 |
| REG-08 | PREDICTIONS.md 2026-02-16 | 45% | — | 45% | FROZEN-FAILED |
| REG-09 | PREDICTIONS.md 2026-02-16 | 50% | — | 50% | RESOLVED (FAILED) |
| REG-10 | PREDICTIONS.md 2026-02-16 | 65% | — | 65% | FAILED ⚠️ see below |
| REG-11 | PREDICTIONS.md 2026-02-16 | 55% | — | 55% | CONFIRMED (FSK cut 2/25) |
| REG-12 | PREDICTIONS.md 2026-02-16 | 60% | — | — | EXPIRED-UNGRADEABLE |
| **REG-13** | PREDICTIONS.md 2026-02-16 | **55%** | **72% [2026-03-05]** (`35de73fe2`, ML-REG-111) | **72%** | CONFIRMED 2026-07-10 |
| REG-14 | PREDICTIONS.md 2026-02-16 | 50% | — | — | EXPIRED-UNGRADEABLE |
| REG-15 | PREDICTIONS.md `73e3253a5` 2026-02-23 | 60% | — | — | TRANSFERRED-TO-WAL |
| REG-17 | PREDICTIONS.md 2026-02-23 | 50% | — | — | RETIRED-PREDICATE-DISSOLVED |
| REG-18 | PREDICTIONS.md 2026-02-23 | 45% | — | 45% | FROZEN-FAILED |
| REG-19 | PREDICTIONS.md 2026-02-23 | 70% | — | — | EXPIRED-UNGRADEABLE |
| REG-20 / REG-26 | ledger-born (3/5, 7/10) | 82% / 33% | — | 82% / 33% | not flagged by the tool |

**Result: no confidence was walked silently.** Three rows carry a deliberate, dated, pre-resolution re-mark: REG-06, REG-07 and REG-13. **REG-13 was the one the 9/11 pass missed:** it was raised in the same 3/5 commit as REG-07. Its cell is now re-formed to `72% [2026-03-05] (was 55% [2026-02-16])`. CATO's census v4 (`AGENTS/CATO/runs/2026-09-30_2251_census-v4/comparison_v3_v4.tsv`) independently records earliest 0.55 and current 0.72.

**Scoring vintages: none changed, nothing re-scored.** Under WQ-112(i) (Will 2026-09-01, `FORGE/PREDICTION_DISCIPLINE.md` §Grading), the latest dated pre-resolution mark scores, and the as-made value is reported separately as first-call calibration. REG-13 therefore scores 72% (Brier 0.0784), with a first call of 55% (0.2025). ⚠️ **That direction favours this desk, and the canon decides it, not me.**

**Two corrections to my own 9/11 receipt** (cells below edited in place; the old text is quoted there):
1. **REG-07 "Brier on 55%" was wrong under WQ-112(i):** 68% scores. On the FALSE track the corrected vintage scores **worse** (0.4624 vs 0.3025). Its first-call date also moves 2026-02-23 → **2026-02-12**: 2026-02-23 is the 3/4 rollout's placeholder `Date_Made`. Its upgrade commit is `35de73fe2` (3/5); `e30e09d50` (3/7) only moved the file.
2. **REG-03, REG-09 and REG-17 are FOUND by text,** in PREDICTIONS.md and not in STATUS, at 70 / 50 / 50, the same as the ledger.

⚠️ **REG-10 was registered after its outcome was public.** PSEC maintained its dividend on 2026-02-09/10. The row was written on 2/16, when the file dated the PSEC decision "Feb 20"; it was corrected on 2/19 (`3387965e9`). No earlier PSEC 65% exists anywhere in the repo (`git log -G`). **It stays FAILED and scored.** Removing it would delete a miss from my own record, and that would be a mass-moving retrofit, which WQ-161 ② forbids. I flag it for the calibration owners only. *(REG-11's confirming event, the FSK cut on 2/25, post-dates its 2/16 registration. TCPC's timing was not checked at primary.)*

**`Date_Made` cells are NOT rewritten.** They are the historical record. The placeholder is documented in the ledger header, and the true dates are in this table.

### 📐 AS-MADE AUDIT RECEIPT 2026-09-11 (DAEDALUS H2 harvest packet 9/7) — re-derived by prediction TEXT, not by ID — ⚠️ PARTIAL; completed and corrected by the 2026-10-10 section above

| Row | Tool flag | Re-derivation (STATUS blob `67d336e32`, 2026-02-12; ledger seed `91c301279`, 2026-03-04) | Disposition |
|---|---|---|---|
| REG-02 / REG-04 | MISMATCH | The 3/6 STATUS table numbered FHLB>$600B as REG-02 and Phoenix as REG-04; the ledger carries them REG-04 / REG-02. By TEXT: FHLB 60% = 60%, Phoenix 65% = 65%. | **ID cross-map, not a walk. No change.** |
| REG-03 | MISMATCH (70 vs 50) | The "50%" is the capital-raise row under the crossed ID; "$936B maturity wall" never appears in STATUS with a %. | **As-made 70%.** *(10/10: FOUND by text in PREDICTIONS.md `1c0b3d0cb` 2026-02-16 at 70%; the 9/11 text said "NOT-FOUND by text".)* |
| REG-06 | NOT-FOUND | "At least one Tier 1 bank capital raise **50%**" 2/12→3/6; seeded 50%; deliberately re-marked **10%** 2026-08-27 (`3ae52ac59`) with the prior value documented in Notes. | **As-made 50%. Row is Kernel-pinned (byte-frozen, Gate C a6/a7) — NOT re-formed; consumers read the 8/27 Notes entry.** |
| REG-07 | NOT-FOUND | "SSB NPL migration >0.5% **55%**" 2/12; seeded 55%; upgraded 68% 2026-03-05 (`35de73fe2`; `e30e09d50` 3/7 only moved the file), documented in Notes but the cell carried only 68%. | **Re-formed: `68% [2026-03-05] (was 55% [2026-02-12])`. Scores 68% (WQ-112(i)); 55% = first call.** *(Corrected 10/10. The 9/11 text read "(was 55% [2026-02-23])" and "Brier on 55%".)* |
| REG-09 / REG-17 | MISMATCH (50 vs 20) | Tool limit (1): the "20%" is prose ("0 of 1") in the 8/13 blob. | **False positive; as-made 50%.** *(10/10: both FOUND by text in PREDICTIONS.md, at 2/16 and 2/23 respectively; the 9/11 text said "neither prediction text ever appears in STATUS with a %", which was true and beside the point.)* |

No RESOLVED row's scoring vintage changed ⇒ nothing re-scored. `python3 scripts/asmade_audit.py REGINALD` will still print the same flags — it reads by ID; this table is the owner verdict.

### ⚖️ EXIT GRADE 2026-09-02 (owner, REGINALD) — **NOT QUALIFYING. State stays `FIRED`; exit run `0-of-3`.**

> **WAL $79.12** settled regular-session close (+$1.86 / +2.41% vs $77.26 [9/1]); O 77.86 / H 80.55 / L 77.82 / C 79.12; vol 1,245,295. **Instruments agree:** `scripts/market.py`, the yfinance daily bar and `regularMarketPrice` all return **79.12** — no disagreement to adjudicate.
> **Exit condition is `WAL ≥ 81.90 on 3 CONSECUTIVE daily closes`. 9/2 closed $2.78 / +3.51% short of leg 1 ⇒ not a qualifying close; the run stays 0-of-3 (it was 0, so nothing reset).**
> ⛔ **THE ERROR THIS GRADE EXISTS TO PREVENT: WAL closed back ABOVE $78 and that is NOT an un-fire.** `REG-T-02` is a state machine, not an event counter — once `FIRED`, it clears **only** on the registered exit condition. A close above the $78 trigger line looks like a reversal and is not one; anyone reading "WAL $79.12 > $78, so the trigger is clear" has read the trigger, not the state. Sub-78 re-entries stay suppressed for the same reason.
> ⚠️ **Intraday is not gradeable, demonstrated by today's own tape:** the 14:23 print was **$79.51** and the settled close came in **LOWER at $79.12**. `value_basis` is *regular-session close* — same-day readable, so this grades at the close and never off a last-trade.
> **NEW ARTIFACT — `registry/REG_T02_EXIT_LOG.tsv` (append-only, one row per settled close).** The run count had been living in prose on `STATUS.md`, i.e. carried from session to session by memory — the same shape as the CCC/HY row that read *"NOT ARMED … FALLING"* on stale data for three weeks. **The count is now COUNTED from the log, not remembered.** `[[finding_mechanize_the_cap_not_the_ritual]]`
> **Routing: NONE OWED and none sent.** The registered announcement fires on the 3rd qualifying close; TERRY asked for a packet at 2-of-3. The count is 0. Per the standing rule: log the close, move on — do not re-alert a non-event.
> ⚠️ **Consequence note:** `GATE-TERRY-ROLL70` filled 9/2 14:21 ET, so this grade now guards a LIVE position (1× WAL Dec-18 $70P @ $2.20) rather than a staged card. A grading error costs money in both directions.

### ⚖️ STATE RULING 2026-09-01 (owner, REGINALD) — **`REG-T-02` is `FIRED`. Fired 2026-09-01 (cycle 2 start). Exit condition `WAL ≥ 81.90 ×3 consecutive daily closes` is now LIVE.**

**State token for cross-desk records: `FIRED (fired 2026-09-01 on the 9/1 regular-session close $77.26; cycle 2 open; prior cycle 2026-05-11 → 2026-06-30; exit ≥81.90 ×3 consecutive closes LIVE, run 0-of-3)`.**

> **Graded at the registered instrument, not inherited from PROME's consumer read** (`scripts/market.py` → Yahoo `WAL`, regular-session close, unadjusted; re-run Tue 2026-09-01 ~17:0x ET, `marketState: POST`). **Daily bar 9/1: Open 77.94 · High 78.93 · Low 77.05 · Close `$77.26` · Vol 1,044,298** (yfinance `history()`); `regularMarketPrice` 77.26 / `regularMarketPreviousClose` 78.13 — the two reads AGREE, and they agree with PROME's `fetch.py` read ($77.26, −1.11%). **Instrument disagreement: NONE.**
> **Graded against the registered spec:** `WAL-PRICE < 78`, sustain 1. **$77.26 IS < 78.00 ⇒ FIRE. First sub-$78 close since the 6/30 exit ⇒ FIRST FIRE OF A NEW CYCLE (cycle 2), exactly the forward clause the 8/20 ruling wrote and 8/23 / 8/28 re-anchored. No duplicate-suppression applies to THIS close; every subsequent sub-$78 close is a RE-ENTRY inside the fired state and IS suppressed.**
> **Distance, derived from the CLOSE and from nothing else: `$78.00 − $77.26 = $0.74` BELOW the line = `0.74 ÷ 78.00 = 0.95%` below the threshold (÷ threshold basis) / `0.74 ÷ 77.26 = 0.96%` (÷ close basis). Day: `$77.26 − $78.13 [8/31] = −$0.87 / −1.11%`.** ⚠️ Intraday low $77.05 is the deepest print of cycle-1-exit-to-now (beats 8/27's $77.13); recorded, not gradeable. Volume 1.03× 3-mo average (1,044,298 vs 1,016,884) — **no volume tell.**
> ⛔ **KILL-ON-SIGHT from this ruling forward: every buffer figure this desk published 8/21→8/28 (`2.10%` · `0.50%` · `0.91%` · `0.70%` · `$0.55 above`) is HISTORY. WAL is BELOW the line, not above it; there is no "buffer" to quote. The only live distances are the two above and the exit distance: `$81.90 − $77.26 = $4.64` = WAL must RISE `6.01%` (÷ close) to print ONE qualifying exit close, and needs THREE in a row.**
> **Consequence executed (registered action `V1V3-ACCELERATE` → `REGINALD action / WAL action / Will`):** ① REGINALD action = this ruling + `STATUS.md` state flip + attribution below; ② WAL action = packet `AGENTS/WAL/inbox/2026-09-01_from-REGINALD_REG-T-02-FIRED-WAL-77.26-V1V3-ACCELERATE-single-name-leg.md`; ③ Will = packet `PROME/inbox/2026-09-01_from-REGINALD_REG-T-02-FIRED-WAL-77.26-V1V3-ACCELERATE-will-leg-Sep-18-pair.md` (⚖️ line on the Sep-18 67.5/70P pair; any trade = Will [Approve] + TERRY construction + live broker book; nothing self-executes). `AGENTS/SIGNALS.md` row appended (carve-out ②). `PROME/GATES.tsv` is PROME's to sync from this ruling — not edited here.
> **⚠️ ATTRIBUTION — the fire is a LEVEL event on a SECTOR day; the V1/V3 MECHANISM is NOT in the tape (VERIFIED at the instrument, 9/1 closes vs 8/31):** WAL **−1.11%** vs KRE **−1.28%** · KBE −1.27% · IWM −1.14% · XLF −0.88% · SPY −0.69%. **WAL fell LESS than its own sector ETF** (beat KRE by 17bp). Inside my 26-bank NDFI cohort (`workbook/NDFI_COHORT.tsv`) the 9/1 move ran **mean −1.13% / median −1.15%, range −2.71% (SBCF) → +0.75% (WFC)**; **WAL −1.11% ranks 14th of 26 = the median.** Worst were SBCF −2.71 · CUBI −2.25 · RF −1.97 · VLY −1.91 · BKU −1.89 · FLG −1.88; money-centres were flat-to-up. **Spearman ρ(PC-NDFI % of loans, 9/1 move) = +0.253, n=26; ρ(total NDFI %) = +0.298** — the SIGN is wrong for a private-credit repricing (higher exposure fell LESS; it is a size effect), so **the 8/20 result (ρ −0.255) is REPRODUCED in kind: banks are not being repriced for NDFI exposure today either.** The day's epicentre was the ALT-MANAGER complex — BX −4.59% · OWL −4.58% · APO −3.58% · ARES −2.85% (ARCC only −0.80%) — with VIX +13% to 16.34, crude +5.7%, 10Y 4.80%. ⇒ **Sector-wide risk-off with a private-credit-manager epicentre that did NOT transmit to bank-level sorting. WAL-specific component ≈ 0.** ⛔ **Do not narrate this fire as "the hidden-CRE thesis accelerating" — the letter fires on the LEVEL and the routing is mechanical; the MECHANISM leg (`V1` MI3 disconfirmed 8/7 at <25% ×12 quarters; `V3` 11-for-11 no reserve build Q2; BROCK 8/28: WAL's $126.4M First Brands receivables charge-off is H1-2026, in the 7/31 10-Q, a collateral-perfection failure not a credit-selection one, and does NOT fire `BRK-31`) is UNCHANGED by a price crossing a fixed line on a day the whole cohort fell.** `[[finding_registered_trigger_can_fire_on_an_unnamed_mechanism]]` — metric hit, cause unnamed: the FIRE is real under the letter (no mechanism clause exists in this spec), the ACCELERATE is a routing obligation, and the attribution travels WITH it so nobody downstream reads the routing as evidence.
> **Base rate, closed:** TERRY's ~1-in-5 (from $79.15) was an upper bound from $79.67; the event realised on the 7th evaluable close of the near-band (8/21→9/1: 79.67 · 78.39 · 79.63 · 79.60 · 78.71 · 78.55 · 78.13 · **77.26**). Precedent from cycle 1 (9 sub-78 closes 5/11→6/03): expect re-entries; suppress them.
> **Instrument note (VERIFIED 9/1, not a defect in this grade):** the yfinance daily `history()` for WAL and KRE returned NO 2026-08-28 bar today (8/27 → 8/31); the 8/28 closes ($78.55 / $74.31) were graded live on 8/28 and stand. The 9/1 bar is present and agrees with the quote endpoint.
> **`REG-T-01` graded the same close: `UN-FIRED`.** KRE **$72.62** [9/1 close, −$0.94 / −1.28% vs $73.56 (8/31); O 73.36 / H 73.82 / L 72.42; vol 14.0M]. **$12.62 above $60.00 = 21.0% above the line (÷ threshold) / KRE must fall 17.4% (÷ close).** Nowhere near.

### ⚖️ STATE RULING 2026-08-20 (owner, REGINALD) — **`REG-T-02` is `UN-FIRED`. Exited 2026-06-30.**

**State token for cross-desk records: `UN-FIRED (exited 2026-06-30; prior cycle 2026-05-11 → 2026-06-30; state re-graded and CONFIRMED UN-FIRED at the 2026-08-21 close)`.**

> ⚖️ **GRADING ADDENDUM 2026-08-23 (owner, REGINALD) — re-graded at the instrument, not inherited from a summary.**
> **Fri 2026-08-21 close: WAL `$79.67` (+0.66%)** [`scripts/market.py` → Yahoo `WAL`, regular-session close, unadjusted — the registered grading instrument, re-run this session; markets closed 8/22-23, so this is final-for-week and no intervening close exists].
> **Graded against the registered spec:** `WAL-PRICE < 78`, sustain 1. **$79.67 is NOT < 78 ⇒ NO FIRE. State is `UN-FIRED` and unchanged.** Exit condition (`≥ 81.90 ×3 consecutive`) is irrelevant while un-fired — a no-op, as on 7/27-28 and 8/05.
> **Distance, derived from the CLOSE and from nothing else: `$79.67 − $78.00 = $1.67` above the line = `1.67 ÷ 79.67 = 2.10%`.**
> ⛔ **KILL-ON-SIGHT: "WAL is 2.00% from `REG-T-02`."** That figure is wrong and it is wrong in the DANGEROUS direction — it understates the buffer, so it makes the trigger look nearer than it is. **2.10% is the number; anything else must be re-derived from a named close before it is repeated.** ⚠️ Equally kill-on-sight: **any WAL-to-`REG-T-02` distance not re-derived from a specific dated CLOSE.** An intraday print, a percentage carried forward from a prior session, or a distance quoted without its close is not a grade of this trigger. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`
> **The 8/20 ruling's forward clause is UNCHANGED and now re-anchored one session later:** the 8/21 session came and went without a sub-78 close, so **a close <78 from Mon 2026-08-24 onward is still a FIRST FIRE OF A NEW CYCLE** — full `V1V3-ACCELERATE` to `REGINALD action / WAL action / Will`, **no duplicate-suppression**. Re-entries *after* such a fire are suppressed; the first one is not.
> ⚠️ **The base rate moved with the price and it moved the RIGHT way, slightly.** TERRY's measurement (49/248 sessions ≤ −1.45%) was taken from **$79.15**, needing −1.45% to reach $78. From **$79.67** the required one-day move is **−2.10%**, a strictly rarer event — so **~1-in-5 is now an UPPER bound, not the estimate.** ⛔ Do not re-cite the 1-in-5 figure as if it were computed at this price; it was not, and I have not re-run TERRY's distribution.
> **Nothing was registered, no band moved, no level changed.** This is a state annotation at my own surface. `PROME` owns the fleet ledger sync (`GATES.tsv` is not mine to edit and I did not touch it).

**Asked by PROME 8/20 with WAL at $79.15 (+$1.15 from the line) and a live fire procedure staged. Ruled on the TAPE, not on the record conflict — the exit condition is a number and the number is gradeable.**

**Full state history, graded close-by-close against the registered spec** (`WAL-PRICE < 78`, sustain 1 daily close; exit `WAL ≥ 81.90 on 3 consecutive daily closes`), instrument `market.py` → Yahoo `WAL`, regular-session close unadjusted:

| Date | Close | Event |
|---|---:|---|
| **2026-05-11** | **76.95** | 🔴 **FIRED** — first close <78. **WALTER's 7/27 claim that it fired 5/11 is CORRECT.** |
| 5/12 → 6/03 | 77.56 · 74.97 · 75.93 · 74.42 · 76.59 · 76.11 · 77.03 · 77.75 | **8 further sub-78 closes — these are RE-ENTRIES INSIDE the fired state, NOT 8 separate fires.** A trigger with an exit condition is a state machine, not an event counter. |
| 6/26 · 6/29 | 82.05 · 82.88 | exit run 1, 2 |
| **2026-06-30** | **82.20** | ✅ **EXITED — 3rd consecutive close ≥ 81.90.** State returns to `UN-FIRED`. |
| 7/27-28 · 8/05 | — | exit condition satisfied twice more — **no-ops, already un-fired.** |
| **2026-08-20** | **79.15** | `UN-FIRED`, **+$1.15 above the line.** |
| **2026-08-21** | **79.67** | `UN-FIRED` — **+$1.67 / 2.10% above the line.** Re-graded 8/23 at the registered instrument. Week's final close; **no fire, no state change.** |

⇒ **A close <78 from 2026-08-21 onward is a FIRST FIRE OF A NEW CYCLE — a fresh signal. Full `V1V3-ACCELERATE` alert to `REGINALD action / WAL action / Will`. NO duplicate-suppression applies.** (PROME's Reading A.)

**⚠️ I am adopting the reading TERRY declined *because it was convenient* — so the grounds matter, and they are not convenience:**
1. **It is what the tape says.** The exit is a registered number; it was met on 6/30 and twice since. This is a measurement, not a judgment.
2. **It is also the SAFER error.** Reading A produces MORE alerting (a fresh full-chain alert), Reading B produces LESS (suppressed as duplicate). On a trigger whose action is `V1V3-ACCELERATE` with Will on the chain, **the costly error is the missed signal, not the extra one.** Convenient and conservative point the same way here; that coincidence does not make it wrong.

**⚠️ Retroactivity, addressed rather than assumed.** The exit spec was written **2026-08-13**; the exit event was **2026-06-30**. I rule the spec applies retroactively, because it was written as a **definition of when this trigger's state resets**, not as a policy with an effective date — and the alternative is absurd: with no retroactive application the trigger would be **permanently fired from 5/11 with no reachable reset**, which was plainly not the intent of writing an exit at all. *(This is the `finding_threshold_level_is_a_measurement_not_a_constant` family — the level was FROZEN; the state derived from it is TRACKED.)*

**⚠️ Both halves of WALTER's live board are wrong, in opposite directions** — *"ZERO FIRES"* (it fired 5/11) and *"still between fire and exit"* (it exited 6/30). **Neither is a reading of the tape; both are artifacts of a fire-ledger that recorded neither the fire nor the exit.** ⇒ **`REG-T` fire-ledger state must be graded against the instrument, never inherited from a board summary** — flagged to PROME for WALTER, not fixed here (not my file).

⚠️ **Base rate, for whoever sizes the alert:** TERRY measured 49/248 sessions ≤ −1.45% ⇒ **~1-in-5 chance of firing on any given day from $79.15.** This is a near-trigger band, not a remote tail. **The 9 sub-78 closes in the 5/11→6/03 cycle are the precedent: when it fires it tends to STAY in the band, so expect re-entries and suppress them under this ruling, not fresh alerts.**

⚠️ **Sustain is 1 — if it fires, it fires SAME-DAY**, with REGINALD + WAL + Will all on `action`. WAL has been oscillating around the ~5% near-trigger band. **WAL-specific analysis belongs to `../WAL/`;** REGINALD keeps the matrix row and cohort context only.

---

## `REG-T-03` / `REG-T-04` — HY-OAS > 320 / > 350

**⚠️ Two standing interpretation caveats — the levels are UNCHANGED by both; carry them when citing either row:**
1. **Composition drift (SIG-723-002, 7/23):** the thresholds are NOMINAL and the HY index has improved since calibration (CCC weight ~10% vs 16%, secured ~37% vs 18%) — the same print now represents MORE stress than at calibration. Flagged as anchor-drift family, not moved.
2. **Blended-index tail-lag (SIG-717-003, WALTER 7/15; promoted from SCRATCH 8/10):** the blended HY index can sit at a benign percentile while the CCC constituent sits at a stressed one (measured 7/15: blended at the 8.3 pctile of its 3-yr range, CCC at 87.8) — so a tail-led credit break may fire late against these blended-level triggers. Companion instrument = the CCC/HY RATIO tripwire `VX-REG-18.04` (spec pinned to the ratio 7/30), which is the tail-sensitive leg; sub-index (BB/B) collection is a fleet gap flagged to PROME by WALTER.

**Downstream-of-bank caveat (7/30 attribution, standing):** HY sits DOWNSTREAM of bank credit in my chain — an HY move without a bank-credit leg is not my chain firing. Before treating any HY level as bank transmission, run the bank-credit cross-check (`reports/2026-07-30_bank-side-HY-attribution.md`).

---

# SCHEMA CHANGE 2026-08-13 — audit-convention encode (8 cols → 13, APPEND-ONLY)

**Authority:** `PROME/proposals/2026-08-12_audit-convention-RULED.md` (Will-approved 2026-08-12, FLEET SCOPE) — *"a stored value must carry its unit and basis; a threshold must name the instrument that grades it (a continuous series is not a contract); and 'zero' must be distinguishable from 'unknown' and from 'not applicable.'"* Encode requested of REGINALD via PROME's 2026-08-13 spawn brief off DAEDALUS's `THRESHOLDS.tsv` findings (**zero exit conditions · zero instrument/basis columns**).

**⚠️ FLAG-BEFORE-ENCODE — the tension I resolved, stated rather than assumed.** DAEDALUS's own REGINALD profile records **"THRESHOLDS 8-col contract"** as a HELD invariant and **"NOTES.md is a companion, never folds into the TSV."** The convention needs machine-readable per-row instrument/basis; NOTES is prose keyed by `trigger_id` and only two rows carry entries. **Resolution: APPEND-ONLY extension.** Columns 1-8 are **byte-identical to `de75ab659`** (verified by `cut -f1-8` diff), so the 8-col contract survives as an exact prefix and any positional reader is unaffected; the five new columns are appended at the end. **No level, operator, sustain window, action, recipient chain or thesis ref moved.** Grep for script consumers before the edit returned **zero** — this file is read by humans and packets only.

| New column | Carries |
|---|---|
| `grading_instrument` | The named series/tool that grades the row. *A continuous series is not a contract* — so the row names FRED `BAMLH0A0HYM2`, not "HY OAS." |
| `value_unit` | Unit of `threshold_value` (USD / bps / percent / thousands of persons / USD billions). |
| `value_basis` | What the number measures — close vs intraday, SA vs NSA, rate vs balance, first-release vs revised. |
| `sustain_unit` | **The defect this closes:** `sustain_window` was a bare integer meaning *daily closes* on REG-T-01/02/03/04/08, *weekly prints* on REG-T-05, *monthly prints* on REG-T-07 and *quarterly prints* on REG-T-06. One column, four different clocks, none written down. |
| `exit_condition` | What un-fires the row. Previously **every row was a one-way auto-fire with no recorded un-fire**, so a fired row could only ever be un-fired by undocumented judgment. |

**Exit conditions are NEW SPEC, pre-registered here, and are deliberately conservative.** Construction rule, applied uniformly: exit requires the metric back on the benign side **by a stated margin** (5% hysteresis on the two price rows; 20bp on HY; a proportionate step on the rest) sustained for a window **≥ the entry window**, graded on the **same instrument** as entry. This is asymmetric by design — harder to un-fire than to fire — because a fired row escalates other agents and an oscillating gate would thrash the whole chain. **These are not levels moved: no entry threshold changed, and before this edit the exit was not "something else," it was *nothing*.** They are gradeable and executable inside the window their instruments quote (`finding_executability_is_a_separate_audit_axis`). If any owner on a recipient chain thinks an exit is mis-set, argue it before it fires, not after.

**Not registered, deliberately.** MI3 / hidden-CRE has **no row in this registry** and I did not add one on the day I re-ran the screen. The cohort re-run (`reports/2026-08-13_MI3_cohort_rerun.md`) found the legacy `>20%` flag catches one name on the legacy basis and **zero on the uniform basis** — so a new MI3 trigger would need its base rate and separation established first, and *"don't build it"* is a real answer (`finding_base_rate_the_threshold_before_building_it`). Recorded as a candidate on ROADMAP, not as a gate.

---

# MI3 HIDDEN-CRE SCREEN — HARDENING + FLAG DISPOSITION (2026-08-13, PROME follow-up, Will-directed)

**Why this section is in the registry file:** the 8/13 re-run was correct partly because the operator hand-caught the traps *in flight*. That is not a control. This records what moved out of session memory and into the instrument, plus the two judgment calls that are mine and not the script's. **Instrument:** `scripts/mi3_cohort_screen.py` (runbook now lives in its header — cohort definition + rationale, quarters convention, credentials, cadence, and the five traps). **Falsifier:** `scripts/mi3_guard_selftest.py`.

## What is now enforced by the tool rather than remembered

| Guard | Catches | Behaviour |
|---|---|---|
| `coverage_guard` | a bank-quarter silently dropped from the run | **exit 2, nothing written** |
| `schema_guard` | a blank/None in a scored cell — the class that would render a 031-filer's unresolved `RCON1766` as an implied **zero**, i.e. *"six banks have no hidden CRE"* | **exit 2, nothing written** |
| `repro_guard` | **the 37.6% class** — a previously published bank-quarter that no longer reproduces against the prior **committed** vintage (read from `git show HEAD:`, never the working tree) | **exit 2**, unless the restatement is DECLARED via `--accept-restatement "<why + source>"`, which records it on the row and in the summary |

Real FFIEC amendments happen, so restatement is *allowed* — but it can never be *silent*. **The defect that poisoned the OZK cell for months was found by archaeology; it is now found by the machine on the next run.**

**Fail-loud, never fail-partial.** Output is written to `.tmp` + `os.replace` only after all three guards pass, so a tripped guard leaves the previous good vintage in place rather than a half-written one.

**State vocabulary (8/12 convention).** `status` ∈ {OK, OK-V1-ONLY | NOT-REPORTED, DENOM-MISSING, PULL-FAILED}; scored statuses must carry every required cell, unscored statuses must carry **none**. `mi3_zero_class` ∈ {REPORTED-ZERO, NONZERO, UNKNOWN} — SBCF and AMTB file a **reported 0**, which is data, not a gap. A YoY off a zero base is recorded `N-A-ZERO-BASE`: **a third state, not a missing number.**

**Standard output is dual-basis AND absolute dollars, by construction.** `MI3_COHORT.tsv` carries `v1_pct`, `v1a_pct`, `item9_share_of_base_pct`, `mi3_k` and `mi3_yoy_pct` on every row; the script also generates `workbook/MI3_COHORT_SUMMARY.md`, which ranks the cohort **three ways** (v1 · v1a · dollar level) and auto-emits a warning whenever the two bases disagree on the top name or the largest absolute book is not the top ratio. **The up-cap migration is visible in default output — an analyst cannot fail to compute it, because nobody computes it.**

> ## ★ BASIS-NAMING RULE (binding on every claim sourced from this screen)
> **No cross-bank statement without its basis named.** `v1a` (÷ item 4 + item 9) governs **all** cross-bank claims. `v1` (÷ item 4) is retained **only** for continuity against v1-vintage records and is **not cross-bank comparable**. And **never quote a ratio without its dollars.**

**Guards are falsified, not assumed.** `mi3_guard_selftest.py` asserts each guard trips on the exact defect it exists to catch (8 cases: 5 trip, 1 declared-restatement passes, 1 no-false-positive on the live output). **8/8 at 2026-08-13.** A guard nobody has watched fail is an assumption. Re-run it whenever the script changes.

## ★ RULING 1 (mine, owner-lane) — the legacy `>20%` v1 flag is **RETIRED as a cross-bank screen**

**Status: RETIRED 2026-08-13, not re-scoped and not silently kept.** Two independent reasons, either sufficient:

1. **Its basis is non-comparable.** The flag reads `v1`, and the item-9 share of the base ran **5.5% → 65.8%** across the cohort at 2026Q2. The flag therefore ranks banks partly by their funding/bucket mix. It is the defect, not a victim of it.
2. **It no longer discriminates.** At 2026Q2 it catches **one** name (WAL 21.20%, falling), and on the uniform basis it catches **none** (cohort max EGBN 10.77%).

**What "retired" means concretely:** no surface may cite a `>20%` MI3 hit as a signal; `v1_pct` stays in the TSV as a continuity column only. **No level was moved** — this flag was never in `THRESHOLDS.tsv`; it lived inside the screen's own recipe, which is why it outlived its own validity without a publisher (`finding_retired_threshold_has_no_publisher`). It is now retired **in writing, with a date and a reason**, where a reader travelling against the link will find it.

## ★ RULING 2 (mine) — **no successor threshold is registered. Spec + base rate only; the numbers go to Will, not the registry.**

Base rate over the 56 scored bank-quarters (2025Q2 · 2025Q4 · 2026Q1 · 2026Q2):

| `v1a` cut | Fires | Rate | Banks that ever clear it |
|---|---:|---:|---|
| >5% | 22/56 | 39.3% | CFG · CUBI · EGBN · MTB · OZK · VLY · WAL |
| >7.5% | 14/56 | 25.0% | EGBN · MTB · OZK · WAL |
| >10% | 9/56 | 16.1% | EGBN · MTB · OZK · WAL |
| >12% | 4/56 | 7.1% | EGBN · OZK |
| >15% | 4/56 | 7.1% | EGBN · OZK |
| >20% | 2/56 | 3.6% | EGBN · OZK |
| >25% | 0/56 | **0.0%** | — |

Distribution: min 0.00 · p25 1.70 · median 4.34 · p75 8.99 · p90 10.77 · max 23.46.

**⚠️ And the reason I am NOT proposing a level off that table — it is the more important finding:**

| Per-bank `v1a` spread across the 4 quarters | |
|---|---|
| **EGBN 10.77 → 23.46 = 12.69pp · OZK 5.46 → 21.83 = 16.37pp** | the two widest |
| Every other bank | **≤ 2.15pp** (WAL 1.31 · MTB 0.88 · CUBI 1.10 · VLY 0.62 · CFG 1.01 · FLG 1.65 · BKU 2.15 · HBAN 1.05 · ZION 0.84 · SSB 0.16 · SBCF/AMTB 0.00) |

**Any cross-sectional level between ~12% and ~20% fires on exactly two banks' own quarter-to-quarter volatility and on nothing else.** That is not a screen, it is a re-description of EGBN and OZK — and it would have been very easy to publish as one, because the base-rate table alone looks respectable at those cuts.

**`n=56` is also not 56 independent observations.** Twelve of fourteen banks move less than 2.2pp across a full year, so the series are strongly autocorrelated and the **effective n is nearer 14** — well short of what a level calibration needs (`finding_base_rate_the_instrument_before_its_event_table`, `finding_cohort_too_small_to_move_the_index`).

**Recommendation of record — "don't build it" is the answer, for now:**
- **Do NOT register a `v1a` level trigger.** ≥25% has fired 0/56 (jointly unsatisfiable on this record); 12–20% is two-bank noise; ≤10% fires a sixth of the time on names nobody calls stressed.
- **The promising successor is a WITHIN-BANK CHANGE instrument, not a level** — e.g. a sustained multi-quarter rise in a bank's own `v1a`, which is what the *original* discovery (classification migration) was actually about. **Data requirement before it can be spec'd: ≥12 quarters** so a change threshold can be base-rated against its own history. The pull is cheap and cached; the quarters are not yet there.
- **Any level, when it comes, goes to Will as a numbers proposal with its base rate and separation attached — never straight into `THRESHOLDS.tsv`.**

## ⚠️ OPEN QUESTION — carried, not solved: does the up-cap finding change the COHORT?

The cohort was selected under **ratio-era priors**: MTB, HBAN and VLY were admitted as *clean large-cap benchmarks*. The 2026Q2 run then found **MTB holding the largest absolute MI3 book in the cohort ($4.95B, ~2× WAL's) and HBAN's dollars up 100% YoY** — i.e. the names admitted as the control group are where the dollars went.

**If the screen's question is "which bank is most concentrated," the current cohort is fine. If it is "where is hidden CRE pooling," the selection rule is measuring the wrong population** and a size-ranked or dollar-ranked frame is the right one (`finding_ranked_head_sample_is_not_the_population` — a cohort chosen by the ranked head of one metric cannot answer a question about a different metric).

**Deliberately not closed this session**, because re-cutting the cohort mid-instrument would silently change what every prior figure means. **Read-path so it cannot rot:** carried on ROADMAP as a dated thread and named in the script header beside `COHORT` (*"do not silently grow the list"*), so the next runner meets the question at the point of temptation. **Decide it before the 2026Q3 run**, so any change lands on a quarter boundary with both cohorts reported once.

---

## 2026-08-27 — CLASS RULING CONSUMED: lagged-publication series grade-date (Will, option (i))

**Record:** `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md` — Will in-session ~14:0x ET, verbatim *"Approve option (i) as the class ruling - go ahead."* Arrived via PROME 8/27. **Consumed here, not re-derived.**

**The rule.** Where a registered row's criteria name a metric from a lagged-publication series *"on `<date>`"*:
1. **The observation DATED `<date>` governs.** No substitute observation — an earlier print merely *available on* that date does not instantiate the cell.
2. **The grade WAITS for that observation to publish.** The strike time slips to the publication moment; **the referent never moves.** A publication lag is a transport artifact, not a spec term.
3. Non-lagged legs of the same row read at their own time and are **held**, with the grade marked **PROVISIONAL on its face** until the lagged leg publishes.
4. **It is a READING RULE for existing frozen letters, not an edit to any of them.**

**Which REGINALD surfaces this governs — audited 8/27, not assumed:**

| Row / vector | Series | Lagged? | Effect |
|---|---|---|---|
| `REG-T-03` HY OAS >320 | FRED `BAMLH0A0HYM2` | ✅ **T+1** | governed |
| `VX-REG-18.04` CCC/HY >3.6× ×3 consec | FRED `BAMLH0A3HYC` ÷ `BAMLH0A0HYM2` | ✅ **T+1** | governed |
| Claims >300K | FRED `ICSA` | ✅ weekly + lag | governed |
| Funding plumbing SOFR−IORB | FRED | ✅ T+1 | governed |
| 30Y level reads | FRED `DGS30` | ✅ T+1 | governed |
| `REG-T-06` FHLB advances | FHLB OF combined report | ✅ **quarterly, ~30d** | governed — and this is the one with a live forward fire (leg 3, ~Nov) |
| **`REG-T-01` KRE <$60** | yfinance regular-session close | ❌ same-day | **NOT governed** |
| **`REG-T-02` WAL <$78** | yfinance regular-session close | ❌ same-day | **NOT governed** |

⚠️ **The distinction that matters at fire time:** `REG-T-02`'s `value_basis` is *regular-session close* — same-day readable, so it is graded **on the day, at the close, and never off an intraday print**. **The lagged-series rule does NOT license waiting on it, and does NOT license grading it early off a last-trade.** Two different disciplines, opposite directions, and conflating them would be the expensive error.

⚠️ **Practical effect on my consecutive-session counting** (`VX-REG-18.04`): a run counted *"through 8/26"* is legitimate only once the 8/26-dated observation has published — which for a T+1 series is 8/27. **Count dated observations, never "latest available."** *(My 8/27 recount satisfies this: 19 sessions through the 8/26 observation, published 8/27.)*

**Not ruled, and I am not assuming it:** MIDAS's ask ② (observation-date and read-date as two separate registered fields) stays OPEN. Until it lands, `THRESHOLDS.tsv` carries no read-date column and this note is the read-path.

## `REG-06` — INSTRUMENT (2026-10-10; DAEDALUS Falsification #4 negative-resolution ask, overdue since 9/30; Will "go ahead" 11:57 ET)

**Why it is recorded HERE, not in the row:** `workbook/PREDICTIONS.tsv` row `REG-06` is **Kernel-pinned, byte-frozen** (Gate C a6/a7). Editing the row would break the Kernel record, so the instrument lives in this file. The row's text, its 10% confidence and its 8/27 re-mark basis are UNCHANGED.

**Letter (as made):** "At least one Tier 1 bank (EGBN, WAL) capital raise", H2 2026, 10%. Invalidation: "Both avoid capital raise through 2026."

**What counts (specified 10/10, before any H2 raise was observed):**
- **Counts:** issuance of **common or preferred equity** by EGBN or WAL, in any amount, including stock issued as acquisition consideration. The 8/27 re-mark names an equity-funded acquisition as the 10% residual path.
- **Recorded, but not counted:** subordinated debt, senior debt, an S-8 (employee or inducement plans) and DRIP/ATM maintenance. ⚠️ Sub-debt is a reading choice. If either bank issues Tier 2 sub-debt, it is flagged to Will rather than graded silently.

**Instrument:**
1. **EDGAR submissions** (`data.sec.gov/submissions/CIK<padded>.json`, UA header). WAL CIK 1212545, EGBN CIK 1050441. Forms to read:
   - **424B1–424B5** (offering prospectuses)
   - **S-1, S-3** and shelf takedowns
   - **S-4** (stock-for-stock acquisition)
   - **8-K** items 1.01 / 3.02 / 8.01, read for any equity issuance
2. **Daily backstop:** `scripts/8k_monitor.py`, which since `8255c2d13` checks WAL and EGBN identity and has no false all-clear.
3. **Press releases:** WAL on Business Wire, EGBN on GlobeNewswire, read when an 8-K lands.

**Dated attempts:**
- **2026-10-10, window 7/1–10/9 = NONE.**
  - WAL: 10-Q, 8-Ks 7/21 (2.02) and 7/30 (8.01), Forms 4, 13G. No 424B, S-1/S-3/S-4 or 3.02.
  - EGBN: 10-Q, 8-Ks 7/06 (5.02) and 7/22 (2.02), 8-K/A 9/14 (5.02), **S-8 8/07 (CEO inducement plan — recorded, not a raise)**, Forms 3/4, 13G.
- **Next scans:** 2026-10-31 · 2026-11-30 · **2027-01-05 (final, covering through 12/31).**

**Resolution:** TRUE on the first counted issuance in H2 2026. FALSE if the 2027-01-05 scan returns none.

## `REG-T-02` — the `V1V3-ACCELERATE` action token is a LEGACY NAME, not an attribution (2026-10-10; DAEDALUS Falsification #4 flag)

- **The defect:** the token's name pre-attributes any WAL <$78 fire to the hidden-CRE (V1) and V3 thesis legs. A fire is a PRICE event, and its cause is attributed at the fire, never by the label.
- **Already re-labelled 10/10:** the human labels in `CLAUDE.md` §KEY THRESHOLDS and `scripts/thresholds.py`. Both now read "WAL price stress (`REG-T-02`); cause not pre-attributed". The `threshold_thesis_ref` anchor `STATUS.md#wal-v1v3-thesis` also points at a section that no longer exists.
- **DEFERRED, with the reason:** the TOKEN itself in `registry/THRESHOLDS.tsv` is NOT renamed today. It is a cross-desk interface, read by WALTER (`AGENTS/WALTER/design/CROSS_REFS/REGINALD.md`, `design/NEWS_SWEEP_TARGETS.md`, `routed/route_log.tsv`, the registry-header receipts). A unilateral rename would break WALTER's join. Rename only as a coordinated change with WALTER, at the next registry touch.
- **Until then:** read `V1V3-ACCELERATE` as **"REG-T-02 fired (price)"** and nothing more.
````

## CLAUDE.md

crc32 4d6e070c; bytes 44171

````text
# REGINALD — Agent Instructions

**Domain:** Regional banks — convergence point for systemic stress
**Role in Network:** Hub agent. Eight independent research streams terminate at regional banks. REGINALD synthesizes signals from sub-agent CREED and peer agents (BROCK, CORAL, OZK, CARL, LABOR, LIQUID, SAM) to identify banks with multiple paths to break.

---

## ⚡ SPAWNED-MODE BOOT CARD (a coordinator spawn prompt can point here in one line)

*When PROME/another coordinator spawns you, you inherit the spawner's cwd, so **this file does NOT auto-load** — read it explicitly first. This 5-line card is the minimum; the full Boot sequence below still governs.*

1. **Read first (cwd-inherited spawn):** `AGENTS/REGINALD/CLAUDE.md` (this file) → `STATUS.md` → scan `inbox/` **and** `inbox/WALTER/` (report, don't process unless tasked).
2. **Print-window mode check** (a bank print ≤ ~5 trading days — the default this cycle): run the fuller `boot.py` sweep (Boot step 7b: earnings countdown / short-interest / 8-K monitor); confirm each in-window name's **grading frame is FROZEN + dates & weekdays verified vs company IR**; confirm **POSITIONS.md is current to the latest broker export** before any fire read. Skip `boot.py` for a quick tape-check boot.
3. **Prices live only** via `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/market.py)` — NEVER from STATUS/POSITIONS files (rule #4).
4. **Git:** all ops from repo root (`cd "$(git rev-parse --show-toplevel)"`), **pathspec own-dir only** (`git commit AGENTS/REGINALD/<file>`), **never push** — the coordinator sweeps at closeout.
5. **Deliver-before-idle (contract):** your final action before going idle = `SendMessage` the result to the coordinator **AND** write it to your own dir (outbox note). Never idle holding — it forces the coordinator to chase you.

---

## IDENTITY

You are REGINALD. You are the convergence point — every other agent's stress eventually flows through regional banks. You don't just watch banks; you watch everything that flows INTO banks.

Primary thesis: **`STATUS.md` §THESIS is canonical; read it there.** The live claim (v2.0, 8/20) is that severity is CONCENTRATED, not tier-wide. *(Re-pointed 2026-10-10 per DAEDALUS Falsification #4. This line used to state the eight-channel "Convergence" thesis, retired as a thesis claim 2026-08-13; the eight channels remain a map of where stress could come from, not a claim that they are firing. History: `archive/thesis_THESIS_v1.4_2026-04-16.md`.)*

You coordinate sub-agent CREED (CRE market-level). BROCK (BDC/private credit), CORAL (Florida), and OZK (single-name) are now top-level peer agents you coordinate with via inbox/outbox + read-only cross-reads, not sub-agents.

**⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md. If it's not in the file, it doesn't persist.**

---

## SPAWN PROTOCOL

### Boot (read phase — this order matters)
0. **`git pull`** — sync from GitHub before reading anything. Follow pull protocol in root CLAUDE.md. GitHub is the source of truth.
1. **Read `STATUS.md`** — sub-agent dashboard, FHLB level, bank watchlist, matrix scores
2. **Read `LESSONS.md`** — mistake patterns to avoid
3. **Read `CALENDAR.md`** — upcoming dates, earnings, signal thresholds
4. **Read `MEMORY.md`** — ends on session handoff: CHANGES SINCE + NEXT SESSION action items
5. **Read `ROADMAP.md`** — persistent state across sessions: open threads, awaiting data, open questions, recently resolved (~2wk). Tells you what's alive across sessions. ⚠️ **The investigations backlog is NO LONGER here** — split 2026-09-02 to `ROADMAP_BACKLOG.md` (cold, on-demand, **NOT a boot read**) per READ_CAP rule 4(b); pull it deliberately when starting research, never at boot.
6. **(Optional) Skim `SCRATCH.md`** — loose intra-day notes. Read if continuing partial day's work, or if MEMORY/ROADMAP point at unresolved details.
7. **Price refresh** — run `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/market.py)` *(cwd-proof form, 2026-07-01 — no longer relies on remembering to cd)*. Compare against STATUS.md thresholds (KRE <$60, WAL <$78, HY OAS >320). Flag breaches or significant moves (>3%) in boot report. Note what changed since last session for CHANGES SINCE section. **Then run the ladder detector** `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/REGINALD/scripts/vx_ladder_check.py)` — exit 1 = a frozen-baseline band is broken; report it and update the VX row. *(Wired 2026-09-24: FLG band 1 broke 9/16 and sat unseen 8 days because no script implemented the ladder, and the price was on my own boot screen.)*
7a. **Ledger staleness check** — run `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" REGINALD --quiet`; surface any ⚠️ stale-ledger alert and freeze-or-refresh it at closeout (root CLAUDE.md Data Hygiene — workbook ledgers are FROZEN-bannered or live, never silent-rot). *(Wired 2026-06-27; 4 orphan feeds frozen, FLOW/KB still flagged → refresh. Invocation cwd-proofed 2026-07-01 — the bare root-relative form failed from an own-dir launch cwd.)*
7b. **(Optional) Fuller monitoring sweep** — `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py)` — covers dark-pool/short-vol, thresholds, KRE float, earnings countdown, short interest, insider activity (EDGAR), 8-K monitor, in addition to step 7's market.py. **WIRED 2026-07-09** (DAEDALUS S3 unwired-orchestrator finding, 7/8 ask) — complementary to step 7, not a replacement; run when a deeper sweep is warranted (pre-earnings-cluster sessions, e.g. the 7/21 WAL+OZK window), skip for a quick tape-check boot.
### WALTER signal intake (inbox/WALTER delivery lane) — complements the step 9b /BOARD/ scan
At boot, after STATUS/MEMORY — run the glob + `git mv` from repo root (cwd-proof: `cd "$(git rev-parse --show-toplevel)"` first):
1. List `AGENTS/REGINALD/inbox/WALTER/*.md` whose SIG-W id is not yet in `board/BOARD_LOG.tsv` (BOARD_ID column).
2. For each: read it, decide disposition, append a row to the existing 11-col `board/BOARD_LOG.tsv` (Channels_Touched=INBOX_WALTER), then `git mv` the file to `inbox/WALTER/processed/`.
3. Let acted items inform the session. **Installed 2026-07-09** (PROME 7/4 rollout ask) — first drain cleared a 31-file backlog (22 archived-with-note as pre-6/26-session-boundary stale, 9 dispositioned live).
8. **Scan inbox** — `ls inbox/` (exclude `processed/`). Report count + senders. Do NOT process — just awareness.
9. **Check peer/sub-agent STATUS files if relevant** — `../BROCK/STATUS.md`, `../CORAL/STATUS.md`, `../OZK/STATUS.md`, `../WAL/STATUS.md`, **`../CREED/STATUS.md`** (all top-level; CREED runs live at `AGENTS/CREED/`)
9b. **BOARD diff scan** (per WALTER LIAISON Turn 2 lock) — pull `/BOARD/INDEX.md` + `/BOARD/SIG-W-*.md` since last `board/BOARD_LOG.tsv` row. Three-tier scope:
    - **(a) Action-recipient unconditional** — `grep '^to:.*REGINALD' /BOARD/SIG-W-*.md` since last-session — read all hits.
    - **(b) cluster_mediating unconditional** — `grep 'cluster_mediating: true' /BOARD/SIG-W-*.md` since last-session — read all hits.
    - **(c) info-recipient cluster-filtered** — read info-cc only when cluster ∈ {BANK_COLLATERAL, PC_STRESS, FED_FRAMEWORK, CONSUMER_STAGFLATION} (primary, always); secondary {IRAN_HORMUZ, ASIA_CHINA, AI_INFRA_CAPEX} read only on bank-ticker hit per `BANK_EXPOSURE_MATRIX.md` watchlist; skip POSITIONING_VALUATION / HYDROCARBON_INFRA / MISC unless cluster_mediating.
    - **Append disposition row** to `board/BOARD_LOG.tsv` (11-col schema: BOARD_ID / Date / Cluster / Verdict / Disposition / Post_Hoc_Conf / Vector_Update / Cross_Links / Channels_Touched / Bank_Tickers / Notes) for each signal read. Disposition values: INTEGRATED / INFO_ONLY / REFERRED / WOULD-INTEGRATE / BACKFILL.
9c. **R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" REGINALD` — §9 rc 0/1/2; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` **plus the WQ-399 fields (Will 10/8; the writer refuses an incomplete receipt, rc 2): APPLIED `--artifact <path#key> --validation-ref <path#key|NONE>` · NO-OP `--scope <text>` · DEFERRED `--review YYYY-MM-DD`; no `;` in any value** — the check's own rc=1 line prints the exact form — and commit `registry/corrections_receipts.tsv`. *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session.)*
9d. **Commit hygiene at write-back — use EXPLICIT PATHS on the commit itself, not a bare commit after staging.** ⛔ `git commit -F msg.txt` after `git add X` *sweeps whatever else is in the shared index* — the exact class the pathspec rule exists for. Always: `git status -- AGENTS/REGINALD/` first (catches any peer session's staged renames or edits waiting on the shared index), THEN `git commit AGENTS/REGINALD/<file> [more paths] -F msg.txt`. *(Added 2026-08-28 after this desk swept HANS's staged inbox renames into commit `9c126923c` — same class as `finding_prome_inbox_is_repo_root_not_under_agents`: a HELD-HOT rule that lives one round-trip away from where it's applied fails at the surface the workflow actually sees.)*

### Execute
10. **Execute the task**

### Write-back
11. **Research detail → `domain/sources/`**
12. **Cross-agent delivery — two lanes (re-cut 2026-09-11 per DAEDALUS route-around census 9/2): SIGNALS (a registered threshold firing, a cross-agent trip, a market/news datum another desk must act on) → `AGENTS/WALTER/inbox/` for routing; WALTER owns the signal lane. ANALYSIS and PACKETS → direct to the recipient's `inbox/`, self-committed per carve-out ①.** (`outbox/` = PROME-action requests only.) ⛔ **PROME packets go to `PROME/inbox/` at REPO ROOT, NOT `AGENTS/PROME/inbox/`** — the latter tree was removed 2026-07-24 and *silently regrows* when a sender writes to it (PROME still services it, so delivery appears to work; the fleet auto-memory `finding_prome_inbox_is_repo_root_not_under_agents` tracks it, HELD-HOT, re-grew twice — mine on 2026-08-28 was n+1). Same for WALTER: `AGENTS/WALTER/inbox/` is the real address.
13. **Run session close checklist** (see below)

### Session Close Checklist

**Run at EVERY session end, not just end-of-day** (per auto-memory `[[feedback_intra_day_closeout_discipline]]`). Multi-session-day intermediate sessions must honor closeout to prevent next-boot archaeology. Closeout is the write-back tail of boot — what you read at boot, you write back here.

Before ending, complete in order:

- [ ] **★ Inbox RE-scan (post-boot landings)** — `ls inbox/` + `inbox/WALTER/` again (excl. `processed/`). A cross-agent note can arrive **mid-session, after your boot scan** — e.g. LABOR's pre-print insider re-run landed 9:23 AM on 7/20, after boot, and only a coordinator ping surfaced it. Process or explicitly defer any new item; never close with an unseen same-day delivery sitting in the inbox. *(Added 2026-07-20 — closes the post-boot-landing blind spot.)*
- [ ] **STATUS.md** — update prices, thresholds, signals that changed this session
- [ ] **★ Derived / secondary surfaces (silent-rot class — boot does NOT read these, so they rot invisibly):** `NEXUS_BRIEF.md` · `POSITIONS.md` marks/context · Convergence Matrix (STATUS) · `DECK_EVIDENCE.md`. **Write-back symmetry:** after any price / catalyst / gate-or-thesis-state change this session, refresh-or-consciously-skip **each** — don't assume the STATUS top-line covered them. The 7/20 seeded sweep found exactly this rot ($81.88/$87.67 stale marks + a de-listed HBAN catalyst) living here, caught only by an external sweep, never by closeout. On any gate/thesis-state flip, run the **state-token sweep** (`grep -rn "<old value>" AGENTS/REGINALD/` for old value gone + new value landed) across ALL surfaces, not just STATUS/SCRATCH. *(Added 2026-07-20 — [[finding_status_spine_staleness_under_appended_top]], [[finding_state_token_sweep_all_surfaces]], [[finding_seeded_selfsweep_secondary_surface_rot]].)*
- [ ] **CALENDAR.md** — mark resolved events ✅, add new dates discovered, prune past events
- [ ] **POSITIONS.md** — update if broker data was received this session (skip if not)
- [ ] **Bank STATUS files** — WAL and OZK are both top-level peer agents (`../WAL/` since 7/25, `../OZK/` since 7/22) — REGINALD owns NO per-bank STATUS files anymore; the local `WAL/` subtree was `git mv`'d out. Cross-flag peers via their inbox, never edit their files. *(Stale WAL/ maintenance instruction removed 8/10 per DAEDALUS profile flag.)*
- [ ] **Thesis drift-grep** (per Orchestrator audit 6/8; hardened to class-fix 6/8 PM): run on **any thesis-level change — a version bump (vX.Y/vX.Y.Z), a framing/claim retirement, or an EV/PT/probability change** (the trigger is NOT version-bump-only: the 6/8 PM cohort-Hyp-A resolution had no bump yet still left stale stragglers). **Recursively grep your own agent dir — not a hand-enumerated file list** (enumerating re-commits the instance-not-class error: the next sub-entity file — BROCK-style per-fund, a future spinout, a new workbook doc — slips identically until someone hand-adds it). Sweep three things: the **old value** (lingering anywhere), the **new value** (confirm it landed everywhere), and the **version label** (anything not bumped — this is how ../WAL/STATUS.md sat a full version behind, caught 6/8 PM):
  ```
  # ⚠️ EXAMPLE ONLY, and the example itself went stale — kept because the METHOD is the point, not these tokens.
  # Post-WAL-cutover (7/25) the WAL thesis version + EV are **../WAL/-owned**; a REGINALD session should NOT
  # be sweeping for them. Substitute whatever value YOUR session moved. (Corrected 2026-07-30 sweep.)
  grep -rn "<OLD VALUE>" AGENTS/REGINALD/   # old value still present?
  grep -rn "<NEW VALUE>" AGENTS/REGINALD/   # new value landed everywhere it should?
  grep -rn "<VERSION>"   AGENTS/REGINALD/   # stale version label anywhere?
  ```
  Eyeball every hit — the extra hits are intended-historical mentions (the "PRIOR 6/8 AM" notes), and consciously clearing each is the point, not noise to suppress (you demonstrated 6/8 PM you can tell stragglers from historical framing). Recursive = zero upkeep + catches files that don't exist yet. Catches denominator drift (14/15/19% overvaluation), probability drift (60/55→70/75 PREDICTIONS), framing-stragglers (cohort "AMBIGUOUS" rows post-Hyp-A — surface fixes miss ~30% per [[finding_verification_correction_downstream_propagation]]), and stale version labels. Two-three greps, one minute, durable.
- [ ] **thesis/CHANGELOG.md** — ⚠️ **BOTH thesis docs are now RETIRED (THESIS R1 2026-08-13, TIMELINE R2 2026-08-20); `thesis/` holds only this CHANGELOG + two pointer stubs.** So this step now means: **append if a THESIS-LEVEL claim moved this session — the claim now lives in `STATUS.md`, which is thesis-canonical.** Do NOT edit the stubs. (skip if no thesis-level change)
- [ ] **MEMORY.md** — rewrite Session Notes:
  - `⚠️ Open question:` line at top — the one thing unresolved when you shut down
  - `CHANGES SINCE`: leave blank (next boot populates via market.py)
  - `LAST SESSION`: what you did, decisions made, files updated (not STATUS recaps)
  - `NEXT SESSION`: numbered action items — specific, checkable
  - Add new Feedback or Findings entries if earned this session
  - Prune any stale entries
- [ ] **ROADMAP.md** — update persistent state: move resolved threads to "Recently Resolved"; refresh "Last Touched" dates on threads worked; add new threads/backlog items surfaced this session; update awaiting-data dates as events resolve
- [ ] **SCRATCH.md** — prune aggressively. Promote useful entries to KB / ROADMAP / MEMORY / STATUS. Delete what's done. Date sections older than ~2 weeks should be deleted unless they earned a promotion.
- [ ] **Research retirement** — flag any `research/` file where ALL three hold: (a) mtime >60 days (`find AGENTS/REGINALD/research/ -maxdepth 3 -mtime +60 -type f ! -name README.md`), (b) NOT in boot-read set (STATUS/MEMORY/CALENDAR/SCRATCH/ROADMAP/CLAUDE.md), (c) NOT referenced in a current STATUS or ROADMAP thread. Files meeting all three: `git mv AGENTS/REGINALD/research/<file> AGENTS/REGINALD/archive/research/<file>`. Rule: **>60d + not boot-read + not referenced → archive**.
- [ ] **★ NEXUS brief fold — the session's LAST write-back** (Amendment 10, Will-approved 2026-07-31, propagated 8/4): rebuild/refresh `NEXUS_BRIEF.md` **after the final STATUS write, immediately before git commit** — checkable form: the brief's commit timestamp ≥ the session's last STATUS commit. The 7/31 fleet audit found 5-of-5 content-stale briefs had *refreshed mid-session and then kept working* — only the ordering constraint closes it. Spec: `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1.
- [ ] **Git** — commit own files per root CLAUDE.md §Git Protocol (pathspec `AGENTS/REGINALD/`, run from repo root) + auto-push via `scripts/safe-push.sh` (ff-gated; non-ff → `git pull --rebase`, never force).

**Discipline overlay (applies throughout closeout — per Orchestrator audit 6/8):**
- **One source of truth per metric.** Don't write the same value in two docs. Own it in the owner doc (see Doc Ownership table above); reference from the other. If a value appears twice, one is canonical and the other should be a pointer. *Prevents:* denominator drift, probability drift, aggregator-cited claims hardening as "precise" without primary.
- **STALE-marked > carried-forward-as-current.** If you can't refresh a value this session, mark it `[STALE]` with the date — don't present it as live. Stale-with-date is honest; carried-forward-without-flag is data fiction. *Prevents:* the SCENARIOS EV-math drift caught 6/2 (was pinned to 5/21 spot for 12 days without staleness flag).
- **Verify-before-propagate** for any count / scope / absence / staleness claim across files/commits (per auto-memory `[[feedback_verify_counts_before_propagating]]`).

**Thesis management:** ⛔ **`thesis/THESIS.md` is RETIRED 2026-08-13 (Will-ruled, retirement R1) — `STATUS.md` is now CANONICAL for thesis state.** The path survives as a pointer stub so inbound links don't dangle; the v1.4 original is at `archive/thesis_THESIS_v1.4_2026-04-16.md`, history only. It was retired rather than refreshed because it *argued the opposite of the live view* (eight channels / 🔴🔴🔴 CRITICAL vs a narrowed 🟠 concentration-not-tier read). ⛔ **`thesis/TIMELINE.md` is ALSO RETIRED (R2, 2026-08-20) — forward calendar is `CALENDAR.md`, NOT a thesis doc.** Changes tracked in `thesis/CHANGELOG.md`, which is now the ONLY live file in `thesis/`. **Do not resurrect an eight-channel document** — a successor, if wanted, is a v2.0 written from STATUS's narrowed claims. Read thesis files for deep context — they are NOT read at every boot, only when the task requires thesis-level understanding. **Rule (RE-SCOPED 2026-08-20 — its two original targets are now stubs): any time a THESIS-LEVEL claim moves, you MUST append an entry to `thesis/CHANGELOG.md`** documenting what changed, why, and old view vs new view. ⚠️ **The claim now lives in `STATUS.md`, so the trigger is a STATUS thesis-state change, not an edit to a retired file — and NEVER edit the stubs to satisfy this rule.** **Versioning is retired with the documents:** THESIS's `vX.Y` line ended at v1.4 and TIMELINE was never numerically versioned, so **entries are DATED, not versioned.** *(If a v2.0 successor is ever written from STATUS's narrowed claims, versioning resumes with it.)*

**MAIL:** Do NOT process inbox on normal spawns. Inbox processing is a separate task — wait to be spawned specifically for it.

Mail is direct file drops (HERMES retired — no delivery daemon):
- **Inbox:** `inbox/` — inbound signals; senders write `.md` packets here directly (coordinators PROME/WALTER route). Move to `inbox/processed/` after integration.
- **Outbox:** `outbox/` — ONLY for requests needing PROME action.

### Inbox Processing Protocol (when spawned for it)
1. **Read each signal** in `inbox/` — who sent it, what's the data, what priority (🔴/🟠)?
2. **Cross-reference workbook** — check your workbook files (VX.tsv, KB.tsv, FLOW.tsv, PREDICTIONS.tsv) for related vectors, prior research, or transmission mechanics. Does this signal connect to something you already track?
3. **Assess thesis impact** — does this change any prediction, threshold, or position view?
4. **Update STATUS.md** if warranted (new data, changed levels, adjusted confidence)
5. **Reply via outbox** only if: (a) you have new information the sender doesn't have, (b) their signal contains an error you can correct, or (c) it triggers a cross-agent threshold. Do NOT reply just to acknowledge — silence means "received and integrated."
6. **Mark processed** — move signal file to `inbox/processed/`

### Outbox Protocol
**SIGNALS route via WALTER** (`AGENTS/WALTER/inbox/` — a threshold firing, a cross-agent trip, a datum another desk must act on; re-cut 2026-09-11, DAEDALUS census 9/2 rows :126/:303). **ANALYSIS / PACKETS** go direct: write a single `.md` packet per item to the target agent's `inbox/` (`outbox/` only for PROME-action requests):
- **Filename:** `YYYY-MM-DD_to-[target]_[short_description].md`
- **Format:**
```
## YYYY-MM-DD — To: [TARGET_AGENT]
**Signal:** [one-line headline]
**Detail:** [2-3 sentences — what changed, why it matters]
**Source:** [data release / own analysis]
**Priority:** 🔴/🟠/🟡
```
- **Write a signal when:** a threshold fires, a prediction resolves, or analysis produces an actionable insight
- **Do NOT write for:** routine STATUS updates or data that only affects your own vectors


### Stale Data Rules
- **VX.tsv:** Skip rows marked [STALE]. Only read rows from last 5 trading days. If >50% stale, note it and move on.
- **STATUS.md values >24h old:** Pull live data via web_search before citing. Bank prices, KRE levels, FHLB data go stale fast.
- **Call Report data:** Always note the quarter (e.g., "Q4 2025 Call Report"). Never present last quarter's ratios as current without stating the lag.

If a cross-agent threshold breaches during your work, append to `AGENTS/SIGNALS.md`:
```
| DATE | REGINALD | TARGET | 🔴/🟠 | Description |
```


---

## ⚠️ READ-CAP — this desk breached it; the remedy is STRUCTURAL (2026-09-02)

Boot 9/2 measured **3 boot-mandated reads over the 54,250 B cap** (ROADMAP 218% · STATUS 204% · MEMORY 115%) and `STATUS.md` **regrown +4,561 B** since the 8/28 partial rotation — the trim-again remedy was being outrun. Fixed structurally: two cold splits (`STATUS_DASHBOARD.md`, `ROADMAP_BACKLOG.md`), verbatim crc-stamped rotations (`archive/{STATUS,ROADMAP,MEMORY}_rotation_2026-09-02.md`), and three de-duplications that were correctness fixes in their own right. **Result: all three under the CAP, all three still over the 32,550 B BUDGET — and the residual is LIVE state.**

⛔ **Binding on the next session, not just that one:**
1. **Run `python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py" --agent REGINALD` at EVERY closeout.** A census ages in hours (READ_CAP rule 13).
2. **Never raise the budget** (rule 6). **Never write a leanness claim** (rule 7) — every pointer this desk writes carries *"re-check at any append, or on 2026-10-02, whichever is first."* A size remedy that runs once and boasts is worse than none: it disarms the next check.
3. **DE-DUPLICATE BEFORE YOU REFRESH.** Three defects this pass were one class — a level copied to a second surface drifts, then contradicts canon. §CROSS-AGENT TRIGGERS read `CCC/HY 3.530×, below line and FALLING` while §THRESHOLD STATUS read `3.861×, 🔴 HARD-FIRE, 19th session`: **two surfaces, one metric, opposite fire states.** A refresh buys five weeks; the de-dup ends the class. **Duplicating a level IS the drift vector — point at the owner, never restate.**
4. **A ruling governs the next write, not the existing state.** The 8/20 de-versioning rule ("a peer's version number is THEIRS") lived in the Doc Ownership table and had reached **nothing the table governs** — WAL's version + EV + PT were still restated in two places 13 days later. **Pair every ruling with a retroactive sweep.**
5. **A line cap does not bound a byte-growing surface.** `MEMORY.md`'s own 100-line cap read **167 lines**; its 8/27 flag said "compact next session" and it grew 27 more across three sessions. Measure BYTES (READ_CAP rule 9, PAT-086).
6. **Rotation is verbatim + contiguous + crc-stamped, never deletion** — and **verify by RECOMPUTING the crc, never by trusting the banner** (rule 11). That check earned its keep on 9/2: the first cut of the ROADMAP archive used `<!--A-->` as both delimiter and example text inside its own instructions, so the self-check split on the instructions and returned a 410 B fragment. **A delimiter and the snippet that reads it must never share a literal.**

---

## OUTPUT RULES

- **Output canon → root CLAUDE.md §Output Canon** (tables > prose · numbers > narrative · source+date every claim · file > verbal — single home, consolidated 2026-07-07).
- Update bank watchlist scores when new data arrives.
- STATUS.md stays under 250 lines.
- When multiple channels fire for the same bank, escalate.

### Doc Ownership (no duplication)

| Doc | Owns | Does NOT contain |
|-----|------|-----------------|
| **STATUS.md** | Current prices, threshold status, signal dashboard, convergence matrix scores, sub-agent summary. Snapshot — tables and levels, minimal prose. | Research detail (→ bank folders), catalyst dates (→ CALENDAR), session history (→ MEMORY), position detail (→ POSITIONS) |
| **POSITIONS.md** | Thesis-relevant positions — strikes, expiries, contracts. Updated from broker screenshots. | Price levels (→ STATUS), thesis rationale (→ bank THESIS files) |
| **CALENDAR.md** | Forward-looking dates + thresholds. Pure table. Pruned weekly. | Narrative or analysis. Just dates, what to check, signal thresholds, who cares. |
| ~~**thesis/THESIS.md**~~ ⛔ **RETIRED 2026-08-13 → pointer stub** | — | **`STATUS.md` owns thesis state now.** Archived original: `archive/thesis_THESIS_v1.4_2026-04-16.md`. |
| ~~**thesis/TIMELINE.md**~~ ⛔ **RETIRED 2026-08-20 (R2) → pointer stub** | — | **`CALENDAR.md` owns forward dates; `STATUS.md` owns thesis state; `reports/*_grading_frame.md` own per-event bull/bear forks.** Archived original: `archive/thesis_TIMELINE_v1.4_2026-04-02.md`. ⚠️ **Do NOT resurrect as a second forward calendar** — that is the 6/19 desync vector. |
| **thesis/CHANGELOG.md** | What changed in THESIS/TIMELINE, why, old vs new view. | Current state — this is history, not the snapshot. |
| **MEMORY.md** | Cross-session memory: feedback from Will, data source findings, session handoff (CHANGES SINCE / LAST SESSION / NEXT SESSION). | Recaps of STATUS data. If it's already in STATUS, don't repeat here. |
| **LESSONS.md** | Mistake patterns — verified errors that burned us. Structural rules. | Session notes or findings. Only confirmed mistakes with prevention rules. |
| **`../WAL/`** (peer agent since 2026-07-25) | WAL promoted to standalone agent — deep coverage, **its own thesis version (read it at `../WAL/STATUS.md`, do NOT pin a version number here)**, predictions WAL-01/02 all live there. ⚠️ **De-versioned 2026-08-20: this cell hardcoded "v2.3" and went stale the day WAL shipped v2.4. A peer's version number is THEIRS and must never be mirrored here** — `[[feedback_behavior_language_over_hash_pinning]]`. REGINALD keeps the matrix row + cohort context (pointer-only seam, no restated figures). | Anything WAL-deep (→ `../WAL/`) |
| **ROADMAP.md** | Persistent state across sessions: open threads (with last-touched dates), awaiting data (calendar of external prints), open questions, recently resolved (**~2wk audit trail — ENFORCE it; it had reached ~16 weeks by 9/2**). Updated at session end. | Live dashboard data (→ STATUS), session-bridge handoff (→ MEMORY Session Notes), thesis-level shifts (→ thesis/CHANGELOG), curated facts (→ MEMORY) |
| **SCRATCH.md** | Loose intra-day workspace: half-thoughts, format gotchas, one-liners cached, things noticed but not pursued, draft language. Promoted or deleted regularly. | Tasks (→ MEMORY NEXT SESSION). Curated facts (→ MEMORY). Thesis (→ THESIS). Backlog items (→ ROADMAP investigations). |

*OZK is a top-level peer agent — its doc ownership lives in `../OZK/CLAUDE.md`.*

**Rule:** If you catch yourself writing the same data in two docs, stop. Put it in the owner doc and reference from the other.

---

## DOMAIN SCOPE

**You own:**
- Bank-level analysis (watchlist, capital, provisions, earnings)
- FHLB advance monitoring (convergence indicator)
- Multi-channel exposure scoring ("The Matrix")
- Hidden CRE (Memo Item 3 / RCON2746 reclassification)
- Sub-agent coordination (CREED); peer-agent coordination (BROCK, CORAL, OZK)
- **BaaS / sponsor-bank credit perimeter** *(added 2026-09-17, WQ-228 RULED by Will via Decision Deck 2026-09-15T17:08:21Z; packet `AGENTS/REGINALD/inbox/processed/2026-09-17_from-PROME_wq228-baas-perimeter-RULED.md`).* **The measurable object is a BANK BALANCE SHEET on a sponsor charter** — partner concentration and credit loss to the sponsor bank when a fintech consumer-credit book reaches the market through ABS. **Feeders (scoped overlap, not silo):** CARL / PHAN feed the fintech consumer-credit-book leg; LIQUID feeds the ABS marks. **Instrument + cadence:** sponsor-bank 10-Q/10-K partner-concentration disclosures at each print + event-driven 8-K on partner exposure or credit loss; watchlist of listed sponsor charters — **CCB** (Coastal Financial, the 7/29→7/30 −43.5% trigger event on a single-partner credit loss, net loss −$42,105K / provision $92,157K per SEC XBRL 10-Q 2026Q2, CARL-verified), Pathward (CASH), Green Dot (GDOT), plus private/subsidiary charters carried by ticker where a listed parent exists (Cross River, Evolve, Lead Bank, Column N.A., Celtic, WebBank — no listed parent → 10-Q of sponsoring partner or SEC XBRL fintech filer only). ⚠️ **Not a new desk, not a new tier, not a new capital rail.** No trade, gate, threshold or capital consequence from the ruling alone. Precedent = root canon's intentional scoped overlaps (CORAL↔MARCO, AEOLUS↔CORAL): one owner, one reconciled figure.

**Sub-agent owns:**
- CREED: CRE market-level data (CMBS DQ, office stress, maturity wall)

**Peer agents you coordinate with (no longer sub-agents):**
- BROCK: BDC/private credit fundamentals (PIK %, dividend coverage, bankruptcies)
- CORAL: Florida-specific (condo crisis, HOA/SIRS, Citizens insurance, FL bank exposure) — `../CORAL/`
- OZK: single-name bank deep coverage — `../OZK/`

**You do NOT own:**
- Employment data → LABOR (but claims >300K is your trigger)
- Consumer credit → CARL (but delinquencies flow to your NCO estimates)
- Market structure → HENRY
- Funding plumbing → LIQUID (but FHLB is your indicator)

---

## CROSS-AGENT SIGNALS

**You send:**

| Condition | Target | Priority |
|-----------|--------|----------|
| FHLB advances >$700B | PROME, LIQUID | 🔴 |
| KRE <$60 | ALL | 🔴 |
| Tier 1 bank capital raise | PROME | 🔴 |
| Multiple Tier 1 banks miss earnings | PROME | 🔴 |

**You receive from:**
- LABOR: Claims >300K → all ORANGE banks escalate to RED
- CARL: Consumer DQ acceleration → NCO trajectory
- LIQUID: Funding stress, credit spreads, MFS contagion
- BROCK: BDC dividend cuts, PIK >40%, fund gates
- SAM: Japan → CLO → BDC → bank fund finance chain

---



---

## HIDDEN CRE METHODOLOGY (Original Discovery) — ✅ COHORT RE-RUN SHIPPED 2026-08-13

Banks hide CRE exposure in C&I via FFIEC Schedule RC-C Memo Item 3 (RCON2746). **Canonical numbers, method, and every caveat now live in `reports/2026-08-13_MI3_cohort_rerun.md` (14 banks × 4 quarters, 56/56 rows at the FFIEC primary, both bases) + `workbook/MI3_COHORT.tsv` (machine-readable) + `scripts/mi3_cohort_screen.py` (reproducible).** Do not restate per-bank ratios here — one source of truth per metric; this section keeps only what a reader must know *before* opening them:

1. **Two bases, always report both.** `v1` = Memo3 ÷ item 4 (legacy, kept for continuity against v1-vintage records). `v1a` = Memo3 ÷ (item 4 + item 9) = the numerator's OWN stated parent, and **the only basis valid for cross-bank claims** — item-9 share of the base runs 5.5%→65.8% across the cohort, so **the basis choice inverts the rank** (WAL is #1 on v1 and #3 on v1a; EGBN is #4 and #1).
2. **`37.6%` (OZK) is KILL-ON-SIGHT** — no reproducible provenance at any quarter. But 4 of the 5 legacy cells reproduce to 2 decimals at the 12/31/2025 vintage, so it is a **single-cell data defect**, *not* a screen-level one. The screen-level defect is item 1's denominator.
3. **"Item 4" and "item 9" are CONCEPTS, not MDRMs.** FFIEC 031 filers (foreign offices — CFG/MTB/HBAN/FLG/VLY/AMTB here) report **RCFD** series and do **not** print the item-4 or item-9b totals; a naive `RCON1766` screen returns `None` for them, which reads as "no hidden CRE." The script resolves by fallback chain and records the MDRM chain used per row. **Zero ≠ unknown ≠ not-applicable** — a reported `RCON2746 = 0` (SBCF, AMTB) is data; a missing part is never coerced to 0.
4. ⚠️ **Scope fence, V1a ≠ V1:** MI3 = CRE *not secured* by RE. Secured books (WAL office + the $99M life-science credit, OZK RESG) are a different object and untouched by any of it.
5. **Instrument:** FFIEC CDR **REST + JWT** (header is literally `Authentication:`; a 403 is a WAF/UA block — use `curl`, don't debug the token). Creds `FORGE/tools/market-data/.env`, **JWT expires 2026-11-05**.

Metropolitan Capital failed with 61% true CRE (labeled 10.7%). Three masking levels: extend-and-pretend, mark-to-model, **classification** (our discovery) — **the masking taxonomy and the bucket-migration mechanism STAND** (a mechanism finding outlives its discredited ratio); the old per-bank ratio table does not, and has been replaced by the re-run above.

---

## BANK WATCHLIST

⚠️ **SCORES REBUILT 2026-08-20 (v2.0) — the v1 numbers below are DEAD and the RANKING INVERTED.** v1 was not reproducible (its own method computes EGBN 12; STATUS carried 20; no derivation exists). **New scale 0-6 — compare ranks, not points.**

**Elevated (instrumented):** **FLG (6)** ⬅ *was LAST under v1* · **EGBN (5)** · **AMTB (5)** — all three on CRE concentration + credit quality, and **all three carry reserves below 100% of their own nonaccruals** (29% / 88% / 51%).
**Mid:** VLY (3) · OZK · WAL · SSB · BKU · SBCF (2) — ⚠️ **WAL and OZK are mid-pack on instruments; the desk's attention had them at the top.**
**Low on the SCORED channels:** ZION · MTB · CUBI (1) · CFG · HBAN (0). ⚠️ **A 0 is not a clean bill of health** — CFG carries the cohort's 2nd-largest private-credit NDFI book (10.66% of loans), reported and deliberately unscored.
*(v1, retired: EGBN 20 / WAL 20 / CFG 15 / OZK 13 / SSB 11 / ZION ~8-9 / FLG 8.)*
**Live scores = STATUS.md Convergence Matrix** (synced 7/17 audit — this list had drifted to pre-rescale values); full methodology → `BANK_EXPOSURE_MATRIX.md` (STALE-VINTAGE-bannered, re-score post-7/21)

---

## KEY THRESHOLDS

*Thresholds + implications only — **live "current" values are OWNED by `STATUS.md` §THRESHOLD STATUS** (the "Current (Mar 4)" column formerly here rotted 4.5 months as a false-current surface; converted to pointer 7/17 audit per one-source-of-truth).*

| Metric | Threshold | Implication |
|--------|-----------|-------------|
| FHLB Advances | >$700B | Early crisis |
| KRE | <$60 | Acute stress |
| WAL | <$78 | WAL price stress (`REG-T-02`); **cause NOT pre-attributed**, attribute at the fire *(re-labelled 2026-10-10; was "Hidden CRE thesis accelerating")* |
| Claims (from LABOR) | >300K | All ORANGE → RED |
| Office CMBS **DQ** (not SS — basis note in STATUS) | >15% | CRE transmission accelerating |
| HY OAS (from LIQUID) | >320bps | Credit transmission confirmed — ⚠️ **QUALIFIED 2026-07-30: a wide HY print is NOT self-evidently bank transmission.** The 7/27-29 HY move sustained 3-of-3 over 280 with **zero** bank participation (IG +3bp, bank preferreds +0.34%, BKLN 0.00%) — cause was the FOMC/rates leg. **HY sits DOWNSTREAM of bank credit in my chain; before treating any HY level as confirmation, run the bank-credit cross-check** (`reports/2026-07-30_bank-side-HY-attribution.md`). Level >320 UNCHANGED. |

---

## FILES

| File | Purpose |
|------|---------|
| `thesis/THESIS.md` | ⛔ **RETIRED 2026-08-13 — POINTER STUB ONLY; `STATUS.md` is thesis-canonical.** Archived original `archive/thesis_THESIS_v1.4_2026-04-16.md` *(was: master convergence thesis v1.4, 10 sections: channels/clusters, 3-layer architecture, loss quantification, what's priced in, validation scorecard. |
| `thesis/TIMELINE.md` | ⛔ **RETIRED 2026-08-20 (R2) — POINTER STUB ONLY.** Forward dates → `CALENDAR.md`; thesis state → `STATUS.md`. Archived: `archive/thesis_TIMELINE_v1.4_2026-04-02.md`. *(was: forward catalyst calendar, week-by-week events, branch points, position calendar — the position calendar was an active phantom source, see LESSONS.)* |
| `thesis/CHANGELOG.md` | Thesis evolution audit trail — what changed, why, old vs new view. |
| `STATUS.md` | Live state — sub-agent dashboard, FHLB, watchlist. **Primary snapshot.** ≤250 lines. |
| `CALENDAR.md` | Forward-looking dates, earnings, signal thresholds. Pure table. **Boot step 3.** Prune weekly. |
| `MEMORY.md` | Cross-session memory: feedback, findings, references, session handoff. **Boot step 4. Write before finishing.** |
| `ROADMAP.md` | Persistent state across sessions — open threads, awaiting data, open questions, recently resolved. **Boot step 5. Update before finishing.** |
| `ROADMAP_BACKLOG.md` | **COLD, on-demand — NOT a boot read** (split 2026-09-02, READ_CAP 4b). Research/deep-dive ideas not yet started; nothing dated or owed. Pull when starting a research session. |
| `STATUS_DASHBOARD.md` | **COLD, on-demand — NOT a boot read** (split 2026-09-02, READ_CAP 4b). The 42 channel rows formerly in `STATUS.md` §SIGNAL DASHBOARD — per-channel analysis and audit trail. ⛔ **Live levels are canonical in `STATUS.md` §THRESHOLD STATUS, not here.** |
| `STATUS_MATRIX.md` | **COLD, on-demand — NOT a boot read** (split 2026-09-24, READ_CAP 4b, verbatim crc `fd2d0508`). The CONVERGENCE MATRIX detail formerly in `STATUS.md`: method notes, reserve-runway / reserve-vs-nonaccrual legs, and per-bank narrative rows (ZION/SSB/CFG · FLG · EGBN · WAL · OZK · non-bank vehicles). **LIVE analysis, not an archive.** Read it when a task needs a bank's matrix narrative. ⛔ **The live score line and the FLG ladder flag stay in `STATUS.md` §CONVERGENCE MATRIX; full method and table → `BANK_EXPOSURE_MATRIX.md`.** |
| `SCRATCH.md` | Loose intra-day notes / observations / format gotchas / one-liners. **Boot step 6 (optional). Prune before finishing.** |
| `POSITIONS.md` | Thesis-relevant positions (bank puts, credit, convergence). Updated from broker screenshots. |
| `TRADE.md` | **LIVE trade surface (rebuilt 2026-09-29, Will: "Do it now")** — trade thesis, live legs as POINTERS (FORGE/POSITIONS own strikes), triggers by name (levels live in STATUS), refuters, anti-trades, open cards. Thin (~8 KB); re-check size at any append. The March-2026 document is archived verbatim → `archive/TRADE_frozen_2026-03-07_archived_2026-09-29.md` (crc `ab819e73`). **Refresh at every position/card event; it is the doc a TERRY card can cite.** |
| `LESSONS.md` | Mistake patterns — read at boot. Distinct from MEMORY (lessons = verified errors, memory = learnings + handoff). |
| `inbox/` | Inbound signals from other agents. Process when spawned for it. |
| `outbox/` | PROME-action requests only. SIGNALS → `AGENTS/WALTER/inbox/` (WALTER routes); analysis/packets → direct to the recipient's `inbox/` (carve-out ①). |
| `BANK_EXPOSURE_MATRIX.md` | Multi-channel scoring ("The Matrix") — 614 lines, reference doc |
| `workbook/PREDICTIONS.tsv` | **Canonical** — 10-column schema (Pred_ID/Date_Made/Prediction/Confidence/Timeframe/Status/Date_Resolved/Outcome/Invalidation/Notes). Falsifiable predictions with invalidation criteria. |
| `domain/sources/` | Primary source docs (Call Reports, FDIC, WAL research, Hidden CRE screens) |
| `research/README.md` | **Master research index** — all series, key findings, data gaps, next priorities. Read before spawning research. |
| `research/FHLB/` | **FHLB research hub (built 2026-10-10, Will-directed): start at its `README.md`.** Canonical FHLB reports + verification + key tables + sources; `copies/` are crc-stamped snapshots (never edit there). Live levels stay in `STATUS.md`; alarm rows stay in `registry/`. |
| `research/outputs/` | Completed research by series (RP-REG-3.x, RP-REG-4.x, RP-FL-x.x, RQ-ad-hoc) |
| `research/prompts/` | Research prompts for external LLM execution |
| `workbook/VX.tsv` | Indicator vectors — **13-column** schema (ID/Name/Category/Current_Value/Yellow/Orange/Red/Status/Confidence/Last_Updated/Source/Cross_Links/Notes; label corrected 7/17). 62 rows; ⚠️ **27 rows marked STALE 2026-10-10** (Last_Updated before 8/11, prior status kept in Notes); 5 RETIRED 10/10 (wiring ⑰). |
| `workbook/KB.tsv` | Knowledge base — **15-column** schema (ID/Date/Session/Entity/Category/Description/Analysis/Data_Quote/Source/Status/Confidence/Thesis_Impact/Vector_Links/Cross_Links/Notes; label corrected 7/17). 116+ entries, ID format ML-REG-xxx. STALE-VINTAGE two-clock header; malformed block ~099..116 **+ 139** (reconstruction post-7/21). |
| `workbook/FLOW.tsv` | ⛔ **FROZEN 2026-10-10** (not maintained; last data 9/11). Transmission mechanics — 10-column schema (ID/Name/Speed/Layer/Status/Trigger/Current_Position/Pathway/Key_Insight/Cross_Links/Last_Updated). 22 rows. |
| `workbook/THESIS_VALIDATION.md` | Thesis confirmation/invalidation criteria + dependency maps |
| `workbook/OTTO_INTEL.md` | Cross-agent intel from OTTO (307 lines) |
| ~~`workbook/VX_HISTORY.tsv`~~ | **RETIRED 2026-08-12 stale-sweep** → `archive/workbook/VX_HISTORY.tsv`. Header-only, never populated in 5+ months; concept was "archived slow-moving vectors" that never had a live consumer. Do not resurrect without a demand path. |
| `SUB_AGENTS.md` | Sub-agent + peer coordination directory. **All four local sub-agent trees (BELT, CREED, TEX, RENO) now archived** — BELT/CREED 8/13, TEX/RENO earlier. ⚠️ **BELT's revival gate — "revive only on a mortgage-DQ catalyst" — is still LIVE and lives there.** BROCK/CORAL/OZK/WAL are top-level peers. |
| `domain/FL_MIGRATION_REFERENCE.md` | FL migration -93% data + Hormuz cascade table (static reference) |
| `earnings_briefs/` | Earnings analysis files (VLY Q1 etc.) |
| `sources/` | External source docs (Trepp CMBS, Metropolitan Capital, Wright) |

### Sub-Agent Files (read on demand, not at boot)
| Path | Agent | Purpose |
|------|-------|---------|
| `AGENTS/BROCK/STATUS.md` | BROCK | BDC/private credit (top-level peer agent) |
| `AGENTS/CORAL/STATUS.md` | CORAL | Florida-specific state (top-level peer agent, promoted 2026-06-19) |
| `AGENTS/OZK/STATUS.md` | OZK | Single-name bank deep coverage (top-level peer agent) |
| `../CREED/STATUS.md` | CREED | CRE market-level state — LIVE at `AGENTS/CREED/`. Local copy archived 8/13 → `archive/sub-agents/CREED/`. |
| `archive/sub-agents/` | BELT · CREED · TEX · RENO | Archived local sub-agent trees — research/sources only, no live STATUS. **Read only if a revival gate fires** (`SUB_AGENTS.md`). |
````

## STATUS.md

crc32 e6996895; bytes 24027

````text
# REGINALD STATUS
**🟠 10/10 SAT EVE (Will-launched): FHLB DRAFT CHECKED + FHLB HUB BUILT; NO SCORE, THRESHOLD OR TRADE MOVED.**
- ★ **FHLB by borrower type, 6/30/26 (Office of Finance Q2 CFR Table 3, pub 8/13):** commercial banks **$458.6B / 56.4%** (+$121.4B in H1 of +$136.2B) · insurers **$202.8B / 24.9%** (record $, share ↓ from 27.0% [3/31]) · credit unions + savings institutions **−$13.7B**. Ties to my XBRL par total ($813.30B). ⇒ more evidence for WQ-414: the H1 rise was not regional stress. Will's external FHLB draft checked claim by claim: **a lead list, not a source** (fabricated Council quote; GAO and Delaware Life findings reversed). **Everything FHLB → `research/FHLB/` (README first).** Bank links: Citizens $450M revolver to Delaware Life (undrawn YE25, status unknown) · WAL = 13% of FHLB SF advances [YE25]. RED packeted on its stale "$480B" (`b9ca8d708`).
*Prior headline (10/10 SAT PM, Will-launched): CATCH-UP DONE; ONE NEW FUNDING TELL; NO SCORE, THRESHOLD OR TRADE MOVED. Its bullets follow.*
- ★ **FHLB Q3 nowcast (10/10 late PM, OF debt files through 9/30):** total FHLB debt **$1,330.8B [6/30] → $1,288.8B [9/30] (−$42.1B)**; Sep +$6.2B only. Fitted on 25 quarters (corr 0.98) ⇒ **Q3 advances ≈ $770B (±2 sd $728–813B), down ~5%**; ≤$700B needs a miss twice the worst seen. ⇒ **`REG-T-06` very likely FIRES as lettered in a quarter when FHLB lending SHRANK** (WQ-414, due 10/24). → `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`.
- **Funding tell (Fed H.8 weekly, through 9/30):** small-bank borrowings (FHLB + other) **+$32.9B / +11.7% in 3 weeks**, the largest rise in 160 weeks (⚠️ the window starts AFTER SVB: SVB's first week was **+$290B in ONE week**, ~9× this) and not a quarter-end pattern. Large banks +0.9%. **Barely visible in FHLB debt** (banks' borrowings +$54.5B in Sep vs FHLB debt +$6.2B; gap 3rd of 41 months) → repo/fed funds, FHLB liquidity drawdown, or large members paying down: not yet separable. Small-bank deposits flat; discount window above its 60-week p90 for two weeks ($9.97B [10/7]). Credit-side bars quiet. **Read (inference): banks lining up cash, not credit transmission.** WALTER signal → LIQUID (+ amendment 10/10 late PM). Next H.8 Fri 10/16.
- **FHLB (6/30):** about half of H1's +$136B is four very large banks (PNC · Citi · USB · WFC); mid/small filers flat; Atlanta +6.9%, SF −10.6%. ⚠️ **`REG-T-06` does not discriminate** (>$700B in 12 of 26 quarters since 2020) → re-letter question to Will via PROME, before the ~10/29 Q3 figure.
- *(10/10 PM as-made audit + July-threads bullet → BLOCK T26, `cf568883`)*
- **Open with Will:** REG-07 VOID before 10/21 (WQ-412) · `REG-T-06` re-letter (WQ-414, due 10/24; Q3 nowcast ≈ $770B) · HBAN puts by 10/14 (WQ-302) · large-bank desk · JWT by 11/05.
*Prior headlines (10/10 AM · 10/9 PM), the 10/9-AM-and-older pointer chain and the stamp chain → `archive/STATUS_rotation_2026-10-10.md` BLOCK T20, crc32 `084f8b0d` (recompute before trusting).*
**Last Updated:** **2026-10-10 Sat ~20:4x ET (Will: external FHLB draft check → FHLB hub → RED packet):** headline + FHLB row (borrower-type mix, hub pointer); report paths re-pointed to `research/FHLB/reports/`. **Prior ~15:3x ET (Will: failures list + core-file sweep):** + 2026 bank failures row (6, FDIC list 9/25). **Prior ~14:1x ET (Will-launched FHLB dig):** Q3 nowcast from OF debt · H.8 scale vs SVB · Sep H.8-vs-FHLB gap. **Prior ~13:5x ET (items ①–③ + write-back):** as-made audit · FHLB + `REG-T-06` · weekly funding bars · July threads · TRADE/CALENDAR refresh · rotations T20–T25 (prior stamps in T20).

> **Thesis state:** STATUS is thesis-canonical (THESIS retired 8/13). Older carry blocks → `archive/STATUS_rotation_2026-09-02.md` BLOCK N and `archive/STATUS_rotation_2026-09-24b.md`.

---

## THESIS: The Convergence

> *8/20 reconciliation note (the retired eight-channel framing sat here 7 days after THESIS was retired for it) → BLOCK T12, crc32 `ff770d7b`.*
> **LIVE CLAIM: severity is CONCENTRATED, not tier-wide** — of 14 primary-sourced filers, **3 elevated, 8 score ≤2** (`BANK_EXPOSURE_MATRIX.md` v2.0). Concordant with the FL card (4-of-4 REVERT, 8/10) and the Q1 cohort NCO decomposition (Hyp A, 6/8). ⚠️ **The concentration is at DIFFERENT NAMES than assumed — FLG/EGBN/AMTB on instruments; WAL and OZK mid-pack.** ★ **9/26 CRE-specific cut (Will-asked): the three most worth investigating for CRE are FLG · EGBN · OZK. AMTB's score is mostly NON-CRE credit (CRE = 30% of nonaccruals on the Call Report, 5.8% on its own basis), and OZK's $288M of foreclosed CRE is invisible to the matrix credit leg.** → `reports/2026-09-26_CRE_vulnerability_top3.md`. Matrix scores unchanged until the 11/07 re-score. ⚠️ **Only 2 of the 8 channels below are instrumented here; the rest are owner-held** (map → matrix §6).

**Eight channels terminate at regional banks — 2 instrumented here, 6 owner-held (see §6 of the matrix). Channel-level state below is CONSUMED from owners, not re-derived.**

| Channel | Mechanism | Status |
|---------|-----------|--------|
| CRE | 70% of CRE at regionals, 70-94% loss severity confirmed. **Apr 2026: dual-stress now — Office plateau 11.69% +141bps YoY + Multifamily +56bps to 7.71% (NEW vector); GSE MF (HOMER, issuer primary, refreshed 9/26): Freddie MF DQ **0.64% [Aug]**, fourth straight rise off a 0.42% Feb trough, above HOMER's >0.50% RED · Fannie MF SDQ **0.61% [Jul]**, rising off 0.58% [May] (its fall from 0.78% was a loan MODIFICATION, not a cure; pair GSE DQ with the filer's provision direction) · Trepp CMBS MF DQ **7.69% [Aug]**, flat. The GSE-improving/CMBS-deteriorating asymmetry is GONE; compare directions, not levels (0.6% vs 7.7%).** | 🔴 |
| Hidden CRE | Cohort MI3 re-run shipped 8/13 (56 primary bank-quarters) → `reports/2026-08-13_MI3_cohort_rerun.md` + `workbook/MI3_COHORT.tsv`. v1a basis ruled 4+9.a (8/28); **rank citations DO-NOT-CITE until the 11/07 Q3 re-run.** Full cell → `archive/STATUS_rotation_2026-09-24b.md`. | 🟠 |
| SSFA/NDFI · Private Credit · MFS/Fraud | **Owner-held** (BROCK · HANS · LIQUID); the April cells (🔴🔴 'Ares gated', '£2B') were stale → BLOCK T27 `2f496d31` | → owners |
| CMBS Maturity | $875B total CRE maturing 2026 (MBA *2025 CRE Survey of Loan Maturity Volumes*, released 2026-02-09 — PRIMARY-CITED by HOMER 9/2 at MBA's own text on the newslink.mba.org mirror; 2027 $652B; 2026 is −9% vs $957B in 2025; depositories $396B = the largest lender bucket). $76.6B hard maturity + $400B wall pushed to 2026. No extensions. | 🔴🔴 |
| Federal Layoffs | **Owner-held (LABOR)**; April cell → BLOCK T28 `2f7a5b42` | → LABOR |
| Stagflation Trap | Rate leg at a cycle-high LEVEL; energy leg high. **Live levels → §THRESHOLD STATUS 10Y / 30Y / Brent rows (one source of truth).** The 9/25 narrative read (hike, real-yield-led move, Brent named contracts, KRE drift) → BLOCK T18, crc32 `d372ca3b`. ⛔ HAWK/BRENT/FALCON own oil, BOND owns the curve. | 🔴 |

---

## SIGNAL DASHBOARD → **`STATUS_DASHBOARD.md`** (cold, on-demand — NOT a boot read)

*42 channel rows split out 9/02 (crc `1585e8e9`); live levels stay in §THRESHOLD STATUS. Note → BLOCK T13, crc32 `eb9e9c85`.* Re-check size at any append.

## RESEARCH — POSITION NAMES (pointers to canonical state)

⚠️ **OZK and WAL are PEER AGENTS: read `../OZK/STATUS.md` / `../WAL/STATUS.md`. Their version, EV and PT are never mirrored here.** Full note → `archive/STATUS_rotation_2026-09-24c.md`.
*(→ BLOCK T29, `72424e60`)*

---

## CONVERGENCE MATRIX — Targets & Positions

> **Matrix detail (method notes, runway/reserve legs, per-bank narrative rows) → `STATUS_MATRIX.md` — COLD, on-demand, NOT a boot read; split verbatim 2026-09-24, crc-stamped.** Scores below are the live line; ⚠️ a `0` means clean on the scored channels only, not a clean bill of health. Method + full table → `BANK_EXPOSURE_MATRIX.md`.
> **🔴 FLG 6** *(was LAST)* · **🟠 EGBN 5** · **🟠 AMTB 5** *(absent from v1 entirely)* · VLY 3 · **OZK/WAL/SSB/BKU/SBCF 2** *(WAL was 1st=)* · ZION/MTB/CUBI 1 · **CFG/HBAN 0** *(CFG was 3rd)*.
> 🔴 **FLG price ladder `VX-REG-6.03` RED since 10/7** (band 3 $11.39 broken at **$11.30 [10/7]**; −20.5% vs FROZEN $14.24 at $11.32 [10/9]). **3 settled closes below RED through 10/9**; ladder exhausted (no band beyond RED). Packets PROME + FLG sent 10/7 (`018af9846`). Detector `scripts/vx_ladder_check.py` (exit-code fix `b6544d45d`; today's and NaN bars excluded via `scripts/settled_bars.py`, `8255c2d13`). Matrix score unchanged (price is not an input). *Prior text → BLOCK T21, crc32 `fc6e141e`.*



*Cohort Signal (Hyp A, 6/8) + Life-Sci sector signal: graded and canonical elsewhere → `archive/STATUS_rotation_2026-09-14.md` BLOCKS P+Q; stub → BLOCK T11, crc32 `18724a40`.*

---

## KEY CATALYSTS

*Dates are OWNED by `CALENDAR.md` (earnings dates in its Q3-2026 BANK EARNINGS DATES table, which `scripts/earnings_countdown.py` reads; CUBI + FLG still NOT ANNOUNCED). Read plan → `reports/2026-10-09_Q3_earnings_read_plan.md`. Next: Nano P&A re-check Tue 10/13 · H.4.1 Thu 10/15 / H.8 Fri 10/16 · CFG Fri 10/16 · `REG-T-06` Q3 ~10/29 (est.) · JWT 11/05 · Call Report retrieval 11/07. The prior mirror list → BLOCK T25, crc32 `2288fccd`.*

---

## CROSS-AGENT TRIGGERS

> ⛔ **THIS TABLE CARRIES THE ROUTING, NEVER THE LEVEL — every level is canonical in §THRESHOLD STATUS above. Duplicating a level IS the drift vector; point at the owner, never restate.** *(9/02 de-dup rationale + worked example → BLOCK T6, crc32 `1b7dacdf`; the example is quoted live in `NEXUS_BRIEF.md`.)* `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`

| Condition | Level | Routing on fire |
|---|---|---|
| Claims >300K | → §THRESHOLD STATUS | LABOR → all ORANGE banks escalate to RED |
| HY OAS >320bps (`REG-T-03`) | → §THRESHOLD STATUS | CARL → credit transmission confirmed. ⚠️ **A wide HY print is NOT self-evidently bank transmission** — run the bank-credit cross-check first (`reports/2026-07-30_bank-side-HY-attribution.md`; the 7/27-29 sustain was `BANK-ABSENT`). |
| HY OAS >350 (`REG-T-04`) | → §THRESHOLD STATUS | LIQUID + Will → issuance freeze |
| ⚠️ HY OAS <260 | → §THRESHOLD STATUS | **REVIEW trigger, NOT auto-exit** (re-anchored 6/19, Will-confirmed). Anchor-drift: the thesis narrowed to WAL-idiosyncratic + CRE; broad HY does not print it. |
| **CCC/HY >3.6× (3 consec)** — `VX-REG-18.04`, **MINE** (PROME 8/28) | → §THRESHOLD STATUS | LIQUID/BROCK → tail-decoupling. ⛔ **The vector's own rule decides escalation, not the level: HY-tightening-led = denominator artifact = NO escalate; only a CCC-LED re-cross escalates.** Escalation STOOD DOWN 8/13 (Will). Full definition → `research/CCC_HY_TRIPWIRE_2026-06-25.md`. |
| CLO AAA >165bps · iTraxx Sr Fin >100bps | **[STALE — no vintage; do not cite]** | LIQUID → BDC transmission (LIQUID-owned, ask don't re-derive) · HANS → EU→US contagion (a DATA-SOURCE gap, not an instrument-identification one). Rows → BLOCK T10, crc32 `9867efbc`. |
| SOFR−IORB >+15bps (`REG-T-08`) | → §THRESHOLD STATUS | LIQUID → FHLB spike. See §THRESHOLD STATUS §Funding plumbing for the structural read (the repo-to-IORB cushion has been consumed; it changes the CONVERSION RATE, not any level). |

## FRAMEWORKS (detail in workbook/)

*Pointer-only, collapsed to one line 2026-08-23 to hold the 250-line cap — zero data lost, these were four file paths:* **Dual Failure Channels (A=CRE, B=PC/NDFI)** → `workbook/CHANNELS.md` · **CRE 3-Layer Architecture** → `workbook/CRE_ARCHITECTURE.md` · **8 Convergence Channels** → `workbook/CONVERGENCE.md` ⚠️ *(eight-channel framing is RETIRED as a thesis claim — see §THESIS; the file is history)* · **NDFI/Whalen Research** → `workbook/NDFI_RESEARCH.md`.

---

## SUB-AGENTS & PEER COORDINATION

*Peer snapshot table (CREED/BROCK/CORAL/BELT/RENO rows, Apr–Jul vintages) → BLOCK T7, crc32 `8e07393b`. **Read each peer's own `STATUS.md`** (`../CREED/`, `../BROCK/`, `../CORAL/`, `../OZK/`, `../WAL/`, `../FLG/`). Two fences travel with any CREED cite: ① the `$875B` 2026 maturity wall is MINE (MBA, ALL-CRE), not CREED's CMBS-only figure (~9× apart); ② CREED's DQ/SS are RATES, WALTER's 'distress −$3.49B' is a BALANCE.*

---

## PREDICTIONS

> **Single source of truth: `workbook/PREDICTIONS.tsv`** (20 rows, REG-01…REG-26; REG-16/21/22/23 → OZK 4/24; REG-24/25 → WAL 7/25 as WAL-01/02, OPEN to the Q3 10-Q; REG-26 RESOLVED-DISCONFIRMED 7/21). `REG-07` re-mark and `REG-03` re-spec are OWED at the Q3 print (MEMORY 6/6d). *Prior text → BLOCK T9, crc32 `eb89e2c3`.*

---

## EXIT RULES

> **Anchor-drift rule (Will-confirmed 6/19, in force):** HY <260 is a **REVIEW trigger, not an auto-exit**; the real exit is re-anchored to the CRE channel (CMBS-DQ, bank CRE-DQ, WAL NCO). Full note → `archive/STATUS_rotation_2026-09-24c.md`.

- **Exit 50%:** Claims <240K sustained + CBRE >-5%
- **~~Exit 100%: HY OAS <260bps~~ → REVIEW trigger** (broad-credit stand-down; re-examine WAL-specific + CRE channel before any exit — do NOT auto-exit on broad HY)
- **Exit 100% (still auto):** BTFP 2.0 announced (genuine systemic backstop = thesis broken)
- **NEW — CRE-channel exit anchors (the thesis's actual confirmation lane):** WAL Q2 NCO ex-fraud comes in <25bps AND no Office classified migration (REG-24/25 both fail) → bear thesis disconfirmed at source; OR Office CMBS-DQ flows reverse (new-delinquency MoM negative 2 prints running) + bank CRE-DQ tier-creep reverses.

---

## ⚠️ THRESHOLD STATUS (**10/10 refresh: WAL/KRE/FLG = SETTLED 10/9 closes (two routes); HY/CCC/B/BB FRED 10/8 (10/9 not yet posted, checked 10/10 ~13:5x ET); small-bank borrowings H.8 through 9/30. Claims w/e 10/3, DGS10/30 10/8, VIX/^TNX/Brent 10/9 vendor reads, as before.** Older notes → BLOCK T22, crc32 `7314d335`, and BLOCK T19. Rows not named keep their stated vintage.)

> *(→ BLOCK T30, `597017ec`)*

| Metric | Threshold | Current | Note |
|--------|-----------|---------|------|
| **FHLB advances** | **>$700B, sustain 3 qtrs** | **$810.7B** [6/30/26, FHLB Office of Finance] | 🟠 **`REG-T-06` LEG 2 OF 3, does not fire.** ★ **By borrower type 6/30 (OF Q2 CFR Table 3): commercial banks 56.4% · insurers 24.9% · credit unions 9.1% · savings institutions 8.2%** (YE25: 49.7 / 26.3 / 11.4 / 11.4). Hub → `research/FHLB/README.md`. Q4-25 $677B (reset) · Q1-26 $734B · Q2-26 $810.7B. **A Q3 print >700 FIRES (~late Oct/early Nov).** ★ **Q3 NOWCAST 10/10 (OF debt through 9/30, −$42.1B in Q3): ≈ $770B (±2 sd $728–813B) ⇒ fires as lettered while advances likely FELL ~5%** (`research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`; in-sample fit, preliminary OF data). ★ **Composition read 10/10 (`research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`):** H1 +$136.2B (par) = **~half four very large banks** (PNC +27.4, Citi +20.0, USB +14.0, WFC +6.0). The 106 mid-size and small SEC filers added +$2.3B (median 0%); Atlanta +6.9%, SF −10.6%. Purpose read for PNC only. ⚠️ **The system was >$700B in 12 of 26 quarters since 2020 (peak $1,044.6B [3/31/23]); as lettered, `REG-T-06` would have fired mid-2023 and never exited** → re-letter question to Will via PROME. Not a trip of BOND's ungradeable `VX-BND-18` leg. Full cell → `archive/STATUS_rotation_2026-09-24c.md`. |
| **WAL** | **<$78** | **$74.27** [**Fri 10/9 settled close**, two routes agree] | 🔴 **`REG-T-02` = `FIRED` (cycle 2, since 9/1). Exit run `0-of-3`, COUNTED from `registry/REG_T02_EXIT_LOG.tsv` (28 rows through 10/9), never from here.** Exit = `WAL ≥ 81.90 ×3 CONSECUTIVE closes`; 10/9 is $7.63 / 9.32% short. Sub-78 closes are SUPPRESSED RE-ENTRIES. **Q3 print Mon 10/19 AMC** (call Tue 10/20 12:00 ET). Guards the RH `Dec-18 $70P` (ROLL70) only, not the Fidelity `Dec-18 $65P ×4`. |
| KRE | <$60 | **$69.01** [**Fri 10/9 settled close**, two routes agree]; selloff closing low $68.89 [10/7] | 🟡 **`REG-T-01` = `UN-FIRED`**, $9.01 / 13.1% above the line; −6.9% from 74.11 [9/14]. Sep-30 $60P ×2 SOLD 9/30, rolled to Dec-31 $65P ×2 (Will). `TRY-COND-KREADD` (TERRY) NOT armed on my legs. *Prior WAL/KRE text → BLOCK T23, crc32 `77401802`.* |
| HY OAS | >320 (`REG-T-03`) · >350 (`REG-T-04`) | **315bps** [FRED BAMLH0A0HYM2, **10/8**; ALFRED vintage 10/9, own pull 10:28 ET] | 🟡 **`REG-T-03` GRADED 0-of-3 at the 10/8 cell** (my letter: >320 on 3 consecutive closes): **324 [10/1] = 1 of 3**, **310 [10/2] RESET**, 312 [10/5], 303 [10/6], **309 [10/7] 0**, **315 [10/8] 0** (both ≤320, no run). NOT FIRED. 5bp under 320 (1.6%); RED's FT-02 graded separately. Prior: 17bp under 320 at 10/6, 43bp above the <260 REVIEW line. LIQUID: one tagged print, funding not confirming (SRF $0, SOFR−IORB −3bp [10/1]); X1 CLOSED (LIQUID's). ⚠️ Anchor-drift caveat stands [SIG-723-002]; bank-credit cross-check before reading any HY level as transmission. |
| **CCC/HY ratio** | >3.6× (3 consec) | **3.975×** [CCC **1,252** / HY 315, **10/8**]; 3.977× [1,229/309, 10/7] | 🔴 **HARD-FIRE CONTINUES: above 3.6× on every FRED close since 7/31 (last at or below: 3.542 [7/30]).** 10/7–10/8: CCC +23bp to 1,252 = NEW FRED-window high, HY +6; both legs widening, no CCC-led re-cross ⇒ no escalation by the vector's rule (LIQUID/RED own the tail read). B 308 [10/7] · 315 [10/8]; BB 189 · 194; B held >300 since 9/28, never reached ORANGE 330 (peak 329 [10/1]). Re-entry is LIQUID's (Will 9/26). Full rows → `workbook/VX.tsv` `VX-REG-18.04`/`18.05`. *Prior text → BLOCK T24, crc32 `ec961eab`.* |
| Claims | >300K | **197K** [FRED ICSA w/e **10/3**, API pull 10/9 20:4x ET; next print Thu 10/15] | 🟢 **103K of buffer.** w/e 9/26 **revised 197 → 199K**. Prior chain 198 [9/12] · 198 [9/19, revised from 197] · 197 [9/26, first print]. Sept payrolls +29K, net revisions −60K, U-3 4.2% (WALTER -20261002-001; LABOR's kill did NOT fire). LABOR owns the read. |
| VIX | n/a | **14.84** [**10/9** vendor read]; 15.08 [10/7] | 🟡 Mid-teens through a cycle-high 10Y, HY over 320 for one print and an FLG RED: **not a fear event.** |
| Brent | n/a | **`BZ=F` $104.43** [10/9 vendor read; contract month not re-checked]; $101.46 [10/7] | 🟠 Not re-read on a named contract. HAWK/BRENT/FALCON own the level and the verdict (BRENT settle-window proxies, HEARTBEAT §1). |
| 10Y UST | n/a | **5.24%** [^TNX **10/9** vendor read]; FRED DGS10 **5.22 [10/8]**, 5.28 [10/7] | 🔴 **Cycle high zone, still.** Official 10Y 5.28 [10/2] rose ABOVE its pre-payrolls level after a +29K print; real-yield-led (BOND, HEARTBEAT 10/2). **This is the LEVEL input to my AOCI/NIM/capital channel.** ⛔ BOND owns the curve. |
| **30Y UST** | n/a | **5.60%** [FRED DGS30 **10/8**]; 5.67 [10/7], 5.64 [10/6] | 🔴 Above every September print (5.49 [9/25]); BOND: 30Y real 3.34 = cycle high [10/2 official]. ⛔ BOND owns the series and the high-water claim. |
| **Funding plumbing** | *(`REG-T-08` SOFR−IORB >+15 ×3)* | SOFR−IORB **−3bp** [3.87 − 3.90, **10/8**, WALTER] · RRP **$2.338B** [**10/7**] · **Discount window primary credit $9.965B [Wed 10/7] / $7.701B wk avg** (H.4.1 via WALTER -20261008-049; highest Wednesday since ≥Jan 2024; no registered line; borrowers not named) | 🟢 15bp under `REG-T-08`; quarter-end passed without pressure (−3bp [10/1]). LIQUID owns the structural read. |
| **Financial stress** | *(no registered line)* | **STLFSI4 −0.468** · **NFCI −0.494** [both **10/2**] | 🟡 **STLFSI4 tightened +0.34 in one week (−0.809 [9/25] → −0.468)**, the HY-over-320 week; still on the loose side of zero. NFCI barely moved (−0.510 → −0.494). **Not systemic stress; the direction changed.** |
| **Bank failures, 2026 (FDIC)** | *(no registered line)* | **6** [FDIC Failed Bank List, last updated **9/25**; pulled 10/10]: Metropolitan Capital 1/30 · CB&T West Georgia 5/1 · Kentland 7/10 · Small Business Bank 7/17 · Tioga-Franklin 8/21 · **Nano Banc 9/25** | 🟡 **Most since 2017 (8) by count; ≈ $1.45B assets in total, est. FDIC cost ≈ $243M; none in my 14 or on Will's book.** A count, not a channel: a cohort name failing would be the signal. Re-pull the CSV for the count, never this cell → `reports/2026-10-10_2026_bank_failures_FDIC_list.md`. |
| **Small-bank borrowings (H.8, FHLB + other)** | *(no registered line; 9/29 descriptive bar ≥+5%/month)* | **$314.5B [9/30]**, +$32.9B / **+11.7% in 3 weeks** (281.6 [9/09]); SA, FRED `H8B3094NSMA`, updated 10/9 | 🟠 **Largest 3-week rise in 160 weeks; not a quarter-end pattern (12 prior QEs −4.9% to +1.4%).** ⚠️ **Scale (added 10/10 late PM): the 160-wk window starts after SVB; since 12/2022 it ranks 4th, behind the three SVB weeks (+$290B in the week of 3/15/23 alone). Month-end to month-end Sep: +$17.1B / +5.9% NSA. Large banks +0.9% SA over the same 3 weeks. FHLB system debt +$6.2B in Sep** (nowcast report §4). Small-bank deposits FLAT (5,674 → 5,673); discount window ≤ +$2.9B of it (all banks). ~2/3 shows as cash on SA (+$21.2B), but NOT on NSA (+$5.6B) → precautionary-liquidity read is INFERENCE. Not FHLB-specific, no bank named. Next print Fri 10/16. → report addendum `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`. *(Replaces the 8/05 H.8 deposits row: large +1.28% / small +0.04%, 4wk; git history.)* |

*(→ BLOCK T31, `54808dfd`)*

---

## BOTTOM LINE

**2026-10-09 (Q3 read plan, Will-asked; `reports/2026-10-09_Q3_earnings_read_plan.md`):**
- **Still CONCENTRATED on 6/30 evidence:** named banks with named mechanisms. Total-CRE bad-loan rate down year on year (2.46 → 2.23%). No cheap-deposit flight at 6/30.
- **Multifamily** fell year on year but rose last quarter at FLG / EGBN / CFG. That is individual, not spread.
- **What would make it spread:** only L180 (≥3 of the five mid-pack banks on the original total-CRE basis) or the FL-rail aggregate. Each reads UNKNOWN where missing banks could flip it.
- **Most consequential open question:** that breadth test, which comes from the Call Reports. Retrieval is planned for 11/07, with completeness checked then; the JWT expires 11/05 (Will).
- **Post-6/30 signals pointing the other way** (small-bank borrowings +11.7% in 3 wks to 9/30 with deposits flat; discount window $9.97B [10/7]; size-led selloff; KRE redemptions) name no balance sheet.

*§BOTTOM LINE 2026-10-07 (WQ-318) and 2026-09-29 (attribution) paragraphs, plus the 9/24 rotation pointer → `archive/STATUS_rotation_2026-10-09.md` BLOCK T17, crc32 `6961a43c`. Reports canonical: `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` · `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`. Their live claims are carried in the 2026-10-09 entry above.*

**Standing bear ledger → `STATUS_BEAR_LEDGER.md` (COLD, not a boot read).** Prior BOTTOM LINE (9/11, incl. the 9/14 WHAT-CHANGED and watch-list) → `archive/STATUS_rotation_2026-09-24b.md`.

⚠️ **Standing caveat: every instrument this desk owns measures CREDIT or a CLOSED QUARTER.** A non-credit repricing is invisible to it.

## OPEN PROCESS ASKS — dated answers (DAEDALUS 10/8 packets; DONE-WHEN = fixed or answered here)

| Ask | Answer 10/9 | Review by |
|---|---|---|
| *(six DONE rows: Prose-Remedy #1 · F#4 minor · F#4 flags · F#4 neg-res · wiring ⑰ · PR#6 ask 3)* | → BLOCK T32, `2f23b1f6` | — |
| Registry TOKEN `V1V3-ACCELERATE` rename (from F#4 flags) | DEFERRED: coordinated change with WALTER, which reads it (`registry/NOTES.md`) | next registry touch |
| L546 float-tie: `kre_float.py:102`, `si_refresh.py:45` round before compare | DEFERRED to next touch of either file (DAEDALUS: no deadline, LATENT) | next touch |
| *(WALTER -033, DONE 10/9)* | → BLOCK T33, `a100038c` | — |
````

## CALENDAR.md

crc32 330c33c6; bytes 22629

````text
# REGINALD CALENDAR

**Last Updated:** **2026-10-10 (Sat ~20:4x ET):** FHLB report paths re-pointed to `research/FHLB/reports/` (hub built); no date or threshold changed. **Prior (Sat ~15:3x ET, core-file sweep):** `REG-T-06` row + Q3 nowcast ≈ $770B · 11/05 JWT row: token on BOTH machines (laptop verified 10/10). No date moved, no threshold changed. *Prior stamp chain (10/10 ~13:5x back to 9/24) → `archive/CALENDAR_rotation_2026-10-10.md` BLOCK C7, crc32 `aa6aa94c`.*
*Stamp chain 9/11 and earlier → `archive/CALENDAR_rotation_2026-09-24.md` (verbatim, crc-stamped).*

---

## RECURRING

| Frequency | Event | What to Check | Threshold / Signal |
|-----------|-------|---------------|-------------------|
| Weekly (Thu) | Initial claims | DOGE layoff acceleration | >300K = all ORANGE banks → RED. (Latest: **197K** [FRED ICSA w/e **2026-10-03**, API pull 10/9 20:4x ET]; **103K from trigger**; w/e 9/26 **revised 197 → 199K**; next print Thu 10/15. *Prior latest (10/7 pull):* **197K** [w/e 9/26]; chain 198 [9/12] · 198 [9/19, revised from 197] · 197 [9/26]. *Prior latest (9/26 pull):* 197K [w/e 9/19]; chain 207 [9/05] · 198 [9/12] · 197 [9/19]. *Older text below is the 9/14 read, kept as history:* (Prior latest: **206K** [w/e 2026-09-05, pull 9/14]; 94K from trigger.) ⚠️ **The w/e 8/29 print was REVISED UP 206→207K** — chain 207 [8/15] · 204 [8/22] · 207 [8/29 rev] · **206 [9/5]**. I pulled the LEVEL at the same FRED primary LABOR uses because my vintage was three weeks stale; **LABOR still owns the READ, the 4-wk MA and the band call — I did not re-derive those.** ⚠️ **THE 8/20 "DIRECTION TURNED" CALL IS RETIRED — the up-drift STALLED:** **198 → 200 → 212 → 207 → 203**, level −4K, the 212K high two weeks behind, and **w/e 8/15 revised UP 206→207K**. Owner's phrasing: ***"off the July low but no longer rising."*** 4-wk MA **205,500** — ⛔ **the +1,250 rise is 100% roll-off, ZERO information; do not cite it as deterioration** (LABOR pre-committed the pivot and reproduced the move exactly). Continuing claims 1,778K [w/e 8/15]. LABOR: low-fire side of a deepening freeze, NOT strength → bank deterioration is **not** employment-transmitted. ⚠️ NFP July −23K first negative of cycle + fin-activities −121K since May-25 — but firing layer unmoved [LABOR 8/7].) |

## ⛔ JULY 2026 — ALL ROWS FIRED AND GRADED; ROTATED 2026-09-02

*9,804 B, verbatim + contiguous, crc32 `213aa875` → `archive/CALENDAR_july_2026-09-02.md`.* CPI 7/14 · CFG 7/16 · ZION 7/20 · WAL 7/21-22 · OZK 7/21 · EGBN 7/22 · monoline · HBAN 7/23 · the 4-name FL small-tier watch-card · the ~Aug 10-Q legs. **Grades are canon in `reports/`, never here.**

⚠️ **This file's own header rule is *"events older than 1 week get marked ✅ and removed at next update"* — it was carrying six weeks of graded rows.** Same shape as `STATUS.md` §KEY CATALYSTS, rotated the same day from under a header reading *"Forward-looking only."* **A pruning rule nobody executes is indistinguishable from no rule.**

**Re-check size at any append, or on 2026-10-02, whichever is first.**

⚙️ **2026-09-24: the 9/2 retention decision is executed early, with a fresh reason (PROME round 2, READ_CAP rule-5 STOP <70%).** Seven passed/resolved rows (Aug 21 OPEX · Aug 24-29 QBP · Aug 31 Kernel · Aug 2026 IQHQ · MI3 RAN 8/7 · Sep 5-7 CMA/FITB cutover · Sep 7 CRMT standstill) and the 9/2 decision note rotated VERBATIM → `archive/CALENDAR_rotation_2026-09-24b.md`. **Two permanent facts survive:** CMA is no longer a standalone KRE constituent (re-point to FITB, merger closed 2026-02-01); the CRMT 9/7 and CMA cutover outcomes were never asserted.

---

## Q3-2026 BANK EARNINGS DATES — canonical date list (read by `scripts/earnings_countdown.py`)

*Added 2026-10-09 (Will's bounded repair pass: the countdown had a hand-typed April list). **A date moves HERE first.** The §LATER rows below record how each date was verified on 10/7 and are not re-edited. `CONFIRMED` = issuer-announced; `NOT-ANNOUNCED` = the date shown is an ESTIMATE and is printed as one. The script checks each Day against its Date and refuses the table (rc 2) on any malformed row. Question = Will's 10/9 priority: Q1 funding × nonbank draws · Q2 CRE recognition · Q3 AMTB non-CRE credit · FL = frozen FL-rail frame · ctx = context.*

<!-- reginald:earnings-dates:begin -->
| Ticker | Date | Day | Timing | Status | Question | Source |
|---|---|---|---|---|---|---|
| CFG | 2026-10-16 | Fri | pre-open (time inferred); call 09:00 ET | CONFIRMED | Q1 | CFG IR 9/10; BROCK at issuer 10/9 (SIG-W-20261009-010) |
| MTB | 2026-10-16 | Fri | pre-open | CONFIRMED | ctx | BROCK at issuer 10/9 (SIG-W-20261009-010) |
| WAL | 2026-10-19 | Mon | after close; call Tue 10/20 12:00 ET | CONFIRMED | Q1 Q2 | Business Wire 10/6 (issuer text) |
| OZK | 2026-10-20 | Tue | after close; call Wed 10/21 08:30 ET | CONFIRMED | Q1 Q2 | OZK release 9/30 |
| EGBN | 2026-10-21 | Wed | after close; call Thu 10/22 10:00 ET | CONFIRMED | Q1 Q2 | EagleBank IR 10/7 |
| BKU | 2026-10-21 | Wed | before open; call 09:00 ET | CONFIRMED | FL | Business Wire 9/22 (repost) |
| SSB | 2026-10-21 | Wed | after close; call Thu 10/22 09:00 ET | CONFIRMED | FL | 8-K 7.01 acc 0001193125-26-411326 |
| VLY | 2026-10-22 | Thu | before open; call 08:30 ET | CONFIRMED | ctx | GlobeNewswire 10/7 |
| AMTB | 2026-10-22 | Thu | after close; call Fri 10/23 09:00 ET | CONFIRMED | Q3 FL | AMTB IR 9/30 |
| CUBI | 2026-10-22 | Thu | after close (pattern) | NOT-ANNOUNCED | Q1 | ESTIMATE from the Q2 pattern (Thu after close, Fri webcast); no notice found 10/9 21:2x ET |
| FLG | 2026-10-23 | Fri | before open (pattern) | NOT-ANNOUNCED | Q2 | ESTIMATE from the Friday pattern; Earnings Whispers says Mon 10/26; no notice found 10/9 21:2x ET |
| SBCF | 2026-10-27 | Tue | after close; call Wed 10/28 10:00 ET | CONFIRMED | FL | SBCF IR 10/5 |
<!-- reginald:earnings-dates:end -->

## PREDICTION INSTRUMENT DATES (named 2026-10-10; canonical text → `workbook/PREDICTIONS.tsv` Notes + `registry/NOTES.md`)

| Date | Row | Read |
|---|---|---|
| **Wed 10/21 after close** | `REG-07` (SSB) | EX-99.1 'Nonperforming loans as a percentage of period end loans', graded on the CHANGE vs 0.62% [12/31/25]: >+0.50pp TRUE, <+0.30pp clean FALSE. ⚠️ **Will may VOID it as misspecified before the print** |
| **Sat 10/31 · Mon 11/30 · Tue 2027-01-05 (final)** | `REG-06` (WAL / EGBN capital raise) | EDGAR submissions scan: 424B, S-1/S-3/S-4, 8-K 3.02. Equity counts; sub-debt is flagged to Will. Scan 10/10 (7/1–10/9) = none |
| **~Wed 11/25 (Q3 QBP) · ~late Feb 2027 (Q4 QBP)** | `REG-03` (recognition wave) | FDIC QBP industry CRE NCO rate Q3 or Q4 ≥ 1.5× Q2, as printed; via CREED (L514). FALSE if not met by the Q4 QBP |

## LATER (forward catalysts — OZK-primary, REGINALD info)

*Six resolved / past rows (WAL Barclays chat 9/16 · FOMC 9/16 · KRE $60P Sep-30 sold-and-rolled · CRMT 9/9 · WAL Sep-18 expiry · WAL Q3 date announcement 10/6) → `archive/CALENDAR_rotation_2026-10-10.md` BLOCKS C1 `0b269ca9`, C2 `124e9854`, C3 `ee8298e4`, C4 `6a2c00cf`, C5 `f3dee7be`, C6 `57f797b9`.*

| Date | Event | What to Check | Threshold / Signal | Who Cares |
|------|-------|---------------|-------------------|-----------|
| **Thu 10/15 (H.4.1) · Fri 10/16 (H.8)**, then weekly | 🟠 **WEEKLY FUNDING READ — two 9/29 bars CROSSED (10/10)** | FRED `H8B3094NSMA` small-bank borrowings (FHLB + other), $314.5B [9/30], +11.7% in 3 wks = largest in 160 wks; `WLCFLPCL` primary credit $8.74B [9/30] · $9.97B [10/7] > p90 $7.83B. Credit-side bars quiet (non-bank lending growing, no line draws, deposits flat) | Does the step-up continue, hold or reverse? A deposit decline alongside it = the PNC pattern spreading. Descriptive bars, NOT registered. → `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` | REGINALD; LIQUID (routed via WALTER 10/10) |
| **~Thu 10/29 (ESTIMATE; Q2 was published 7/30) → FHLBank Q3 10-Qs ~early–mid Nov** | 🟠 **`REG-T-06` LEG 3 — FHLB Office of Finance Q3 combined advances** | System advances at 9/30; a print >$700B FIRES as lettered (EARLY-CRISIS). **NOWCAST 10/10 (OF debt through 9/30, −$42.1B in Q3): ≈ $770B, ±2 sd $728–813B** → `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`; grade the print against it | ⚖️ **Will's re-letter decision BEFORE the figure exists** (WQ-414, due 10/24; the figure is now estimable, so rule early) (PROME WQ ask 10/10: the letter was >$700B in 12 of 26 quarters since 2020). Grade with the composition read: named-borrower share (the FHLBank 10-Q borrower tables) + the borrower-side XBRL median | REGINALD action · LIQUID info · BOND (`VX-BND-18` candidate) |
| ~~**Oct 1, 2026**~~ ✅ **RESET SCHEDULED-UNCONTRADICTED (OZK 10/1, 10/2)** | **OZK $350M sub notes reprice** (2.75% → **CME 3M Term SOFR + 209bp**, Act/360) | Tier 2 capital −20% (≈$280M eligible, unchanged) | **≈+$12.3M/yr pre-tax (≈$0.09 EPS)** at Term SOFR 4.0958% [9/29, INFERRED T−2 fixing, single source] ⇒ coupon ≈6.19% — **figure OZK-owned, canonical in `../OZK/CALENDAR.md`** (corrected 10/7 per OZK packet: my old ≈+$11.2M used overnight SOFR 3.87% as a proxy; the benchmark is 3M Term SOFR). Coupon VERIFIED at the Q3 10-Q (~early Nov). Next par call 2027-01-01 (notice window 11/2–12/22) | OZK primary |
| **early 1Q 2027 (close, EST.) → +180 days (~1H27)** | 🟠 **VLY–Bluevine close → Bluevine's partner-bank deposit program TERMINATED; deposits move to Valley within 180 days** (VLY 8-K EX-99.2, acc 0001193125-26-403391) | How much of the $2.1B sits on **CCB**'s own balance sheet vs swept (CCB Q3 10-Q partner disclosure); VLY brokered paydown | BaaS perimeter (WQ-228): a partner-deposit exit at CCB. HSR approval only, no bank regulatory approval | REGINALD (BaaS); KB ML-REG-188/189 |
| **Oct 2026** | Affinius Capital $2.7B bond maturity | OZK link — NOT mentioned on Q1 call | — | OZK primary |
| 🔴 **Every close from Tue Sep 1** | **`REG-T-02` EXIT grading — `WAL ≥ 81.90 ×3 consecutive daily closes`** (FIRED 9/1 at $77.26; cycle 2; run 0-of-3) | `scripts/market.py` regular-session close, never intraday. **Graded 9/2: WAL $79.12, NOT qualifying — run stays `0-of-3`, needs +3.51% from here.** Count is COUNTED from `registry/REG_T02_EXIT_LOG.tsv`. ⛔ **A close back above $78 is NOT an un-fire** — only `≥81.90 ×3` clears the state. Sub-78 re-entries are SUPPRESSED (state machine, not event counter). | Exit = state → UN-FIRED; announce to WAL/PROME; any roll card carrying the exit as its guard closes. | REGINALD grades; WAL/PROME/Will consume |
| ~~Aug 19~~ ⚙️ **DATE FIRED — re-cast 2026-09-02 from a dated event into a STANDING GUARD, which is why it is not pruned.** The effective date is past and ungradeable by me; **what survives is permanent and is the reason the row exists** — any C&I line-utilization read spanning this date carries a tariff artifact in BOTH directions and must say so. ⚠️ **A dated row whose date has passed can still be live: the event expires, the interpretive caveat it created does not.** | **Section 338 Canada tariff effective** (+50% ad valorem; 301 forced-labor 10-12.5% already LIVE since 7/24) [HAWK 8/10] | **Utilization-data guard, both directions:** pre-8/19 C&I drawdown spike = importers racing goods in (tariff artifact, NOT demand); any line-utilization rise since late July may be 301 tariff funding, NOT demand. No clean pre-shock baseline in recent utilization data. ⚠️ Autos-in-Annex vs 232-carve-out UNRESOLVED per HAWK — verify at proclamation Annex before sizing anything auto. | REGINALD (borrower working-capital read); HAWK owns the vector |
| **H2-2026 / Q1-2027** (finalization) | 🟠 **AOCI reinclusion — Basel III endgame re-proposals (Fed/OCC/FDIC, released 3/19/26)** | **HARVESTED 8/20 from the retiring `thesis/TIMELINE.md`, and CORRECTED on two axes in the process.** Mandatory AOCI inclusion in CET1 for **Cat III/IV** ($100B-$700B assets) ends the opt-out that let regionals keep unrealized AFS losses out of regulatory capital. **$49.5B aggregate across 21 firms** [Risk.net / Risk Quantum — re-sourced 8/20; SECONDARY, not a primary read]. 🔴 **CORRECTION 1 — DIRECTION: TIMELINE called this *'the slow-burning bomb… a SEPARATE capital drain on top of credit losses.'* That is one-sided.** The AOCI hit is real but the package it sits inside is a **net capital REDUCTION** for Cat III/IV (~0% CET1 change at holdcos, **−4.7% at depository subsidiaries**) — other changes OFFSET it. **Net = relief, not tightening.** 🔴 **CORRECTION 2 — TIMING: 5-year phase-in running to 2032** (100% excluded in year 1 → 0% by 2032), so this is a **drip, not a 2026-27 event.** TIMELINE's compound-capital-drain thesis leaned on it landing alongside CRE charge-offs; on this schedule it does not. | **Watch: FINAL RULE publication** (not yet issued — comment closed 6/18/26; still proposals as of 8/20). Then: does the final keep the offsets, or strip them and leave the AOCI leg standing? **That reversal is the only path back to the original bear read.** ⚠️ Do not cite $49.5B as primary. | REGINALD; cc LIQUID, HENRY |
| ✅ **dates VERIFIED 10/7** → **Wed 10/21 – Tue 10/27 prints → ~early Nov 10-Qs** | 🟠 **FL BANK-RAIL Q3 RE-TEST (BKU/SSB/AMTB/SBCF) — FROZEN frame `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md`** (DOCKET L227, converges with CORAL's GSE leg) | ✅ **DONE 10/7 (deadline 10/9) — all four ANNOUNCED, issuer text, weekdays `date -d`: BKU Wed 10/21 before market (call 09:00; Business Wire 9/22 via repost) · SSB Wed 10/21 after close (call Thu 10/22 09:00; 8-K 7.01 acc 0001193125-26-411326) · AMTB Thu 10/22 after close (call Fri 10/23 09:00; IR 9/30) · SBCF Tue 10/27 after close (call Wed 10/28 10:00; IR 10/5).** SSB Q2 classified-$ ($2,227.1M) and AMTB baselines filled at primary 9/24 (frame Amendment A1). | 8-K legs grade at each print; 10-Q legs at each 10-Q; aggregate FINAL by ~11/14. ≥2 TRANSMITS → packet CORAL + PROME same session. | REGINALD; CORAL consumes |
| **Tue Oct 13 (P&A re-check; bid summary read 10/9) → ~late Dec 2026-early Jan 2027 (est.) → ~Mar 25 2027** | 🟠 **NANO BANC FAILURE (9/25) — three forward reads** (PROME DOCKET L516 · L513) | (1) FDIC posts the **Sunwest P&A agreement** — ⚠️ **NOT POSTED as of 2026-10-09 10:26 ET**; the **bid summary DID post (page Last Updated 10/8)** and §3 was re-run on it → `reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md` (retained-pool ≈32–42%, desk scenario). **Next P&A check Tue 10/13** (Mon 10/12 Columbus Day), then each Tuesday; no posting by **Tue 10/27** → ask DEWEY for a records route. The P&A sizes the pools (A/D retained), places the $97.1M HFS book and WAL's O1 DOTs. (2) **FIRREA claims bar date** (not published 9/27; ≥90 days after first notice; WALTER WATCH_FOR). (3) **Fed OIG Material Loss Review** → grade §2d (C&I→9.b transfers: correction vs relabel) and §3 (final DIF vs $114M est.). | Shared figure ≈ $120M ≈ 17% [9/22 base] moves only on (1) or (3). | REGINALD; CREED/WAL consume |
| **~Oct 20 → ~Nov 25 — ⚠️ ALL DATES ESTIMATES** | 🟠 **WQ-313 Q3 CHECKS (Will 9/27 21:16 ET) — canonical rows are PROME `DOCKET.tsv` L35 · L180 · L521 · L514 (cite by line; each carries source · question · what to record if disclosure is insufficient)** | **L35, EGBN Q3 (✅ CONFIRMED Wed 10/21 after close, call Thu 10/22 10:00 ET — EagleBank IR 10/7; RED re-dates L35):** HFS sales vs post-write-down marks; the Prince George's apartment loan ($56.0M, matured again 8/21) and the Fairfax office loan ($22.1M, matured 9/25): paid, extended, downgraded or nonaccrual. Insufficient → record 'outcome not disclosed in Q3 deck'; CPAN stays deferred. **L521, VLY Q3 (✅ CONFIRMED Thu 10/22 before market, call 08:30 ET — GlobeNewswire 10/7; 10-Q ~11/10):** does the Q2 multifamily 30–59 cohort cure or roll; CRE nonaccrual vs $256.1M; Q3 modifications and any re-default of the $108M payment-delay loans; direction of quantitative CRE reserves. **A CHECKPOINT, not a resolution** (deferrals run to ~Q1-27). **L180, breadth test at the 11/07 run:** ≥3 of WAL · VLY · SSB · BKU · SBCF with CRE bad loans up >50% QoQ or a new foreclosure build → BROADER. ~~Insufficient → name the unavailable banks and grade the rest (14 chosen banks, not the population).~~ **Re-stated per Will 2026-10-09 21:33 ET (pre-print), plan §2.0:** · **Basis:** graded on the ORIGINAL total-CRE bad-loan RATE, Call Report (nonaccrual + 90+ over construction + MF + NOO, cross-bank §A3/§E), plus `oreo_total_k`. · **Multifamily is a separate sub-read**, never counted. · **Missing banks:** *c* ≥ 3 → BROADER · *c* + *m* < 3 → NOT BROADER · else **UNKNOWN**, naming the missing banks. · **Individual-bank deterioration** at FLG / EGBN / OZK / AMTB is NOT a spread. · **11/07 = planned retrieval;** completeness is checked then. · **Q1→Q2 dry run:** *c* = 1 (WAL OREO +2.3%, literal limb). PROME packeted to annotate DOCKET L180. **L514, FDIC Q3 QBP (~11/25):** a second consecutive rise in regional ($10–250B) foreclosed CRE, and whether CREED-T-03 fires. Reconcile with CREED to one figure per series. | Reports: `reports/2026-09-27_cross-bank_CRE_transmission.md` §D + §F · `reports/2026-09-27_VLY_CRE_transmission.md` · `reports/2026-09-27_EGBN_fairfax_observability.md` | REGINALD; RED (L35 owner) · CREED (L514) |
| **~Sep 30 → ~early Nov — ⚠️ ALL DATES ESTIMATES** | 🟠 **CRE TOP-3 Q3 TESTS (FLG · EGBN · OZK)**, Will-asked 9/26 | OZK Q3 date announcement ~9/30; EGBN ~Wed 10/21 AMC; FLG ~10/23 (FLG desk carries ~10/27); Q3 10-Qs ~early Nov (EGBN MF criticized table and FLG risk grades are 10-Q-only). **Verify each date when announced; none is announced at 9/26.** | Grade each bank's 'weakens if' lines in `reports/2026-09-26_CRE_vulnerability_top3.md` §6 and re-run `scripts/cre_loss_bridge.py` with actual Q3 marks. Key tests: FLG MF special mention ≤ $2,757M and modifications < $556M; EGBN downgrades < $100M and the Aug–Dec criticized maturities; OZK any OREO sale price vs carrying, Boston 10 Prospect sale, RaDD report-back. | REGINALD; CREED/FLG/OZK consume |
| **Fri 10/16 → Wed 10/21 — ✅ CONFIRMED (four of six); FLG + CUBI NOT ANNOUNCED (10/7)** | 🟠 **WQ-318 SIX-BANK Q3 PRINTS + the pre-committed observation list** (`reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` Deliverable 2) | **CFG Fri 10/16** (call 09:00 ET; release pre-open INFERRED; CFG IR 9/10) · **WAL Mon 10/19 AMC** (call Tue 10/20 12:00) · **OZK Tue 10/20 AMC** (call Wed 10/21 08:30; OZK release 9/30) · **EGBN Wed 10/21 AMC** (call Thu 10/22 10:00; EagleBank IR 10/7) · FLG NOT ANNOUNCED (secondary calendars 10/23 or 10/26) · CUBI NOT ANNOUNCED (pattern Thu 10/22 AMC — ESTIMATE). ⛔ The 8/27 "WAL Tue → EGBN Wed → EGBN Thu" pattern row is RETIRED: WAL moved to a MONDAY. | Grade each bank's UP/DOWN/INCONCLUSIVE row within one session of its print, from the NAMED line only; confirm F1/F3/N at the 11/07 Call Report run. Also at these prints: the WAL Q2 ex-fraud NCO 37bps re-basing figure (`reports/2026-07-21_WAL_Q2_grade.md`). | REGINALD; PROME (L527 consumer); TERRY/WAL/OZK context |
| **~Sep 15** | Canadian winter 26-27 FL schedule filings (AC/WestJet/Porter) | MARCO's capacity tell for the $600M-1.2B FL-$ hole → my Q1-Q2 2027 FL bank/CRE stress window; MARCO 7/31: intent divergence says flatten-and-extend the shock profile, not raise/lower | MARCO primary; REGINALD info |

## PREDICTION CHECKPOINTS

> **Single source of truth: `workbook/PREDICTIONS.tsv`** (REG-01 through **REG-26**, **20 rows** — count fixed 7/25: REG-24/25 extracted to WAL at promotion).
> Display copy removed 2026-06-26 — read the TSV for confidence and resolve dates.
> Active Q2-Q3 2026: **WAL-01/02 (formerly REG-24/25) now graded at the WAL agent** → `../WAL/workbook/PREDICTIONS.tsv` (25%/50% post-Stage-2, OPEN to Q3 10-Q) | **REG-26** RESOLVED-DISCONFIRMED 7/21 (history, this ledger).

---

| **2026-11-07 (Sat)** | **PLANNED RETRIEVAL of the 14 Q3 Call Reports — completeness checked THEN** (which banks have a Q3 filing in CDR; any amendment). A bank absent at retrieval is *m* in the breadth rule → UNKNOWN wherever it could flip L180 (Will 10/9). Feeds L180, the WQ-318 F1/F3/N confirms and the matrix re-score (+OREO). **MI3 COHORT SCREEN — 2026Q3 RUN DUE** (registered cadence: quarterly, ~45d after quarter-end; Call Reports file ~30d after, CDR availability lags). Command: `.venv/bin/python3 AGENTS/REGINALD/scripts/mi3_cohort_screen.py` — roll `QUARTERS` + `YOY_PAIRS` **+ `NEXT_DUE`** forward first (all three sit together; `NEXT_DUE` is the ledger's quiet-until date and a stale one makes the staleness nudge fire every closeout), then `scripts/mi3_guard_selftest.py`. ✅ **Two-clock header shipped 2026-09-02 — emitted by the WRITER, so it survives this run; do NOT hand-add one.** ⚠️ **BLOCKED BY THE ROW BELOW: the JWT expires 11/05, two days before this run.** If the token lapsed, the failure surfaces at `creds()` — that is by design, not a bug. ⚠️ **Decide the cohort-selection open question BEFORE this run** (`registry/NOTES.md`: the names admitted as clean benchmarks are where the dollars went) — a mid-instrument re-cut silently changes what every prior figure means. **This row IS the read-path — a lapsed window is visible here rather than found by archaeology.** | REGINALD |
| **2026-11-05** | ⚠️ **FFIEC CDR JWT EXPIRES — Will action (PWS account login).** The MI3 cohort screen, the item-4→item-9.a migration series, and every Call-Report pull run on this token. On expiry the instrument goes dark with a 500/5003, and the failure mode looks like an auth bug rather than a calendar event. **Regenerate before, not after.** (90-day lifetime by design; registered with PROME 8/7. Token lives in `FORGE/tools/market-data/.env`, gitignored; present on BOTH machines (laptop `WilliePOwen` verified 10/10, 255-char token; the old 'desktop-only' remark was flagged stale in SCRATCH 10/7). Regeneration before 11/05 is still Will's.) | REGINALD / Will |

*Pruning rule: events older than 1 week get marked ✅ and removed at next update. Fired-but-unverified items (FFIEC PDD MI3 window, WALTER LIAISON calibration 5/25, FDIC QBP mid-May, APO Epstein 5/21, ROAD to Housing vote) live in ROADMAP — Awaiting Data / Open Threads, not here.*
````

## ROADMAP.md

crc32 19f36858; bytes 23479

````text
# REGINALD ROADMAP — "Where are we"
**Updated:** **2026-10-10 (Sat ~20:4x ET — Will: external FHLB draft checked · `research/FHLB/` hub built · RED packet).** Prior: ~15:3x ET (FHLB dig · 2026 failures list · core-file sweep; BaaS thread opened). Full stamp + the PM catch-up stamp → BLOCK R6, crc32 `5f0a1deb`.
*Stamps 10/10 AM (BLOCK R5, crc32 `3693ce98`) and 10/9 PM · 10/7 · 9/29 (BLOCK R3, crc32 `adb2708f`) rotated VERBATIM → `archive/ROADMAP_rotation_2026-10-10.md`.*
*Stamps 9/27 PM, 9/27 and 9/26 rotated VERBATIM → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R1, crc32 `ebe14531`.*
*Stamps 9/14 and 9/02 rotated VERBATIM → `archive/STATUS_rotation_2026-09-27.md` BLOCK R1, crc32 `cb6c187f`.*

Persistent state-of-REGINALD tracker across sessions. **SCRATCH** = loose notes, intra-day workspace. **MEMORY.md Session Notes** = session-bridge handoff (what just happened, what's next). **STATUS** = live dashboard. **ROADMAP** = what threads are open, what data we're waiting on, what questions are unresolved, what we want to investigate next, what just got done.

**Maintenance discipline:** Updated at session end before commit. If a thread is moved to RESOLVED, that's the audit trail of what each session shipped. Pruned aggressively — promote to thesis/KB/research or delete; do not just accumulate.

---

## OPEN THREADS
*Active work spanning multiple sessions. Each entry: what / status / next step / last-touched.*

| Thread | Status | Next Step | Last Touched |
|--------|--------|-----------|--------------|
| *(12 aged threads, 4/26 → 6/20)* | CLOSED 2026-09-02 with per-row verdicts → `archive/ROADMAP_aged_threads_2026-09-02.md` (crc32 `a277c281`). Nine had been answered by later work and nobody closed them. | **Rule: a thread that resolves as a side effect of other work does not self-close — closing is the answering session's write-back obligation.** Full row → BLOCK R4, crc32 `03552a2c`. | 2026-09-02 |
| 🟡 **NEW 2026-09-02 — Commercial Chapter-11 filings as a NON-CREDIT / FORWARD bank instrument** *(the one live part extracted from the dead 5/9 pinch-hitter row)* | ⛔ **The 5/9 figure (+42%) is 4 months stale and unusable — do NOT adopt it.** What survives is the INSTRUMENT question, and it is my standing open one: **every gauge this desk owns measures CREDIT and a CLOSED QUARTER**, which is precisely why the 9/1 fire and the 9/2 bounce both came back unsortable at name level. Commercial bankruptcy filings are forward-ish and not sourced from a bank's own closed-quarter print. | **Base-rate BEFORE building** — separation, lead time vs bank credit prints, and whether it moves independently of HY. ⛔ **"Don't build it" is a real answer** and is the likelier one; the failure mode to avoid is adopting a series because it is available rather than because it discriminates. Companion candidates already listed on the blind-spot thread (forward P/TBV dispersion · revision breadth · KRE creation/redemption · short interest · options skew) — ⚠️ **all of those are TTM- or trailing-window-averaged, so they inherit the one-regime defect; this one may not.** | 2026-09-02 |
| *(closed threads)* | 24 RESOLVED rows → `archive/ROADMAP_rotation_2026-09-02.md` BLOCK C (crc32 `1d242fd4`; non-contiguous row-set, named deviation). One had sat RED for ~6 weeks after grading (WAL Q2 frame). | Full row → BLOCK R5, crc32 `101f4efa`. Re-check size at any append. | 2026-09-02 |
| 🔴 **`REG-T-02` exit grading (FIRED 9/1, cycle 2)** | Count lives ONLY in `registry/REG_T02_EXIT_LOG.tsv` (27 rows through 10/8, run `0-of-3`; 10/8 close $75.50, two routes; **10/9 owed from settled bars via `scripts/settled_bars.py WAL`**). Guards the live Dec-18 $70P (ROLL70). TERRY's clause (d) (missing vendor bar = labelled substitute or UNKNOWN, never a holiday) CONCURRED 9/26. | Grade every settled close; 2-of-3 → packet TERRY; exit → UN-FIRED + announce WAL/PROME. | 2026-10-09 |
| 🔴 **CCC/HY escalation (re-arm MET 9/24, sent 9/26)** | Live tier state → STATUS §THRESHOLD STATUS CCC/HY row; re-entry is LIQUID's (Will 9/26). 9/29 row → BLOCK R7, `2ba7bf66` | Tier test each boot (MEMORY 0a-NEW); B ORANGE >330 watch; only a CCC-LED re-cross escalates | 2026-10-10 |
| 🔴 **NEW 2026-09-26 — CRE top-3 (FLG · EGBN · OZK), Will-asked** | Report `reports/2026-09-26_CRE_vulnerability_top3.md` + dossiers + `workbook/CRE_RCN_COHORT.tsv` + `scripts/cre_loss_scenarios.py`. AMTB dropped (non-CRE credit); WAL 4th (the only name accelerating every quarter); VLY 5th. | **FLG ladder `VX-REG-6.03` RED 10/7 ($11.30; packets PROME + FLG `018af9846`; ladder exhausted).** Grade each report §6 'weakens if' line at the Q3 prints (FLG ~10/23, EGBN ~10/21, OZK TBA ~9/30 — ALL ESTIMATES). $133M gap: FLG answered 9/27 — structural (50–73% every period since FY23), location NOT DETERMINABLE, leading reading = loss at exit; bridge §① narrowed, 17.5% 'fix' withdrawn (20.45% stands). Loss bridge → `reports/2026-09-26_CRE_top3_loss_bridge.md` (`scripts/cre_loss_bridge.py`). Metric changes M1–M5 are RECOMMENDATIONS pending Will's word; not applied. | 2026-09-26 |
| 🟠 **NEW 2026-09-27 — Nano Banc failure (9/25): forward reads on a DELIVERED report** | `reports/2026-09-27_nano-banc-failure-forensics.md` (d8010b97f), accepted by PROME. **Shared figure ≈ $120M ≈ 17% [9/22 base] is MINE; CREED/WAL/PROME cite it.** Leading markers at Nano (Memo-3 share 79% of C&I; ALLL/noncurrent 10%) are n=1, NOT adopted. | **10/9: P&A NOT posted; bid summary read → §3 re-run (`reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`). Next P&A check Tue 10/13, then Tuesdays (DOCKET L516).** Bar date (WALTER). Fed OIG MLR ~3/25/27 → grade §2d/§3. If a national MI3-share screen is ever built, base-rate it on the FFIEC bulk RC-C file first. | 2026-09-27 |
| 🟠 **NEW 2026-09-27 (written back 10/07) — VLY: NEITHER + one bank-specific early flag** | Q2: MF past-dues $9.4M → $101.5M, NOO nonaccrual +$20.8M, $108M CRE payment-delay mods, in the same quarter as a disclosed decline in quantitative CRE reserves (categories undisclosed). `KB ML-REG-171`; `reports/2026-09-27_VLY_CRE_transmission.md`. | **At VLY Q3 (est. Thu 10/22, NOT announced; DOCKET L521):** does the MF 30–59 cohort cure or roll; CRE nonaccrual vs $256.1M; re-defaults of the $108M; reserve direction. A CHECKPOINT — deferrals run to ~Q1-27. **+10/10: VLY agreed 9/27 to buy Bluevine for $340M (~$255M cash + ~6.3M shares; 8-K acc 0001193125-26-403391): $2.1B of small-business deposits, close early 2027, ~5% TBV dilution at close** → ask at the 10/22 call how and when the deposits move; see the BaaS thread. | 2026-10-10 |
| 🟡 **NEW 2026-09-27 (written back 10/07) — PFBC ~$60M litigation-dependent NPLs (Nano/Makhijani shared collateral)** | Mostly exited at par in Q2 ($68.4M note sales); ~$60M left, resolution contingent on legal proceedings (SECONDARY call summary). Mark-contagion channel, not solvency. `KB ML-REG-173`. PFBC is OUTSIDE my cohort. | Read PFBC Q3 (date not checked) for the ~$60M; an FDIC sale of Nano liens on shared properties would print a mark (Nano P&A check-by 10/9, DOCKET L516). No TERRY packet (not in Will's book). | 2026-10-07 |
| 🟠 **NEW 2026-09-24 — Cohort AOCI: the rate leg's first FILED test** | All 14 opt out of AOCI (reported CET1 unaffected). ZION is the outlier (AOCI 22% of CET1). Q3 scenario −$2.6B to −$4.3B after-tax (duration ASSUMED). WAL expects to cross $100B by end-Q1 2027. → `reports/2026-09-24_cohort_AOCI_exposure.md` | At the Oct Q3 prints: grade reported AOCI/TBV per bank against the scenario; does KRE's drift track the TBV hit or run ahead of it (MEMORY open question)? | 2026-09-24 |
| 🟠 **`CREED-T-03` level leg has no sourceable parent** (the 3.40% series is absent from the Q1-26 edition) | Unresolved; CREED owns the trigger. | Full reasoning → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-27 |
| 🟠 **Regional CRE OREO +26.4% in one quarter — the only Q2 tell pointing toward recognition, and it is mine** | **NEW 8/27**, routed by CREED out of a clean QBP because CRE OREO on regional balance sheets is my surface. **The Q2 improvement's COMPOSITION splits by bank size:** regionals ($10-250B) grew CRE OREO **$723.9M → $915.3M (+26.4%)** *while their PDNA fell* 1.39→1.22%; the >$250B class did the opposite — OREO **−8.9%** with CRE NCOs **0.14→~0.22% (+57%)**. ⇒ **regionals FORECLOSING, money-centres CHARGING OFF** — one headline, two mechanisms, and the regional one moves the problem ONTO the balance sheet. | ⚠️ **Fence carried verbatim and it is load-bearing: accounting-scale comparison, NOT attribution** — both are stocks, the QBP shows no flow between them, loans also exit PDNA by cure/charge-off/sale/modification. **"Of a size that COULD account for ~18%" — never "did."** ⚠️ **Does NOT move S3** (CREED held it at 2); a 26% move on a $915M stock is not bank transmission. **Next step: watch it into Q3 (~late Nov QBP), and decide whether regional CRE OREO earns a registered vector or stays an on-demand read — base-rate first, "don't build it" is a real answer.** | NEW 2026-08-27 |
| 🟢 **Gate C increment 2 — nothing owed by me** | Commands a1/a2/a6/a7 immutable; precondition ⑦ resolved-blessed 8/27. | Never re-author or edit; a defect is fixed only by a NEW command. Full row → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-27 |
| 🔴 **The blind-spot question — is a credit-only instrument set capable of answering "why are banks moving?"** | **NEW 8/20, and it is the session's real output.** Today's null is only informative if my instruments *could* have found something. Every one of them measures CREDIT (MI3, NDFI, CRE-DQ, NCO, coverage, criticized). A non-credit repricing would produce this exact result and I would never see it. | **9/29: first non-credit / pre-print set BUILT** — weekly H.8 (NDFI loans, small-bank deposits, large time deposits, borrowings, C&I) + H.4.1 primary credit + KRE float + PFF/BIZD legs, report §3; all 🟢 through 9/16–9/23 (NDFI lending +1.1%, no deposit flight, discount window ordinary). **10/10 re-read: 2 of 8 bars CROSSED, both funding-side** (small-bank borrowings +11.7% in 3 wks to 9/30, the 160-week max — ⚠️ a post-SVB window; SVB's first week was +$290B, ~9× this; FHLB debt +$6.2B in Sep; discount window >p90 two weeks, $9.97B [10/7]). Credit-side bars stay 🟢 → banks lining up cash, not credit transmission (FHLB report addendum; WALTER signal to LIQUID). Descriptive bars only — **base-rate before any registration**; wire into `boot.py` as a deliberate task. Still unbuilt: P/TBV dispersion · revision breadth · skew. | 2026-09-29 |
| *(closed thread)* | 8/14 → 9/14 de-rating ATTRIBUTED 9/29 (beta, no bank component) → BLOCK R2, crc32 `454040d4`; Recently Resolved 9/29 PM row carries it. | — | 2026-10-07 |
| 🟠 **`REG-T-06` FHLB at LEG 2 of 3 — dated forward fire** | Q1-26 $734B · Q2-26 $810.7B; **a Q3 print >700 FIRES** (FHLB Office of Finance, ~late Oct/early Nov; grade waits for publication). PNC headroom = candidate instrument for BOND's ungradeable `VX-BND-18` leg, NOT a trip. | ✅ **Composition read DONE 10/10** (`research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`, ML-REG-185): about half of H1 growth is four very large banks (PNC · Citi · USB · WFC); mid/small filers flat; Atlanta +6.9%, SF −10.6%. ⚠️ **Base rate: >$700B in 12 of 26 quarters since 2020; as lettered the alarm fires mid-2023 and never exits.** **Next:** Will's word on re-lettering (via PROME's queue) BEFORE the Q3 print; then grade the Q3 print with the composition attached. ★ **10/10 late PM nowcast** (`research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`): OF debt −$42.1B in Q3 ⇒ advances ≈ $770B (±2 sd $728–813B), so the letter fires in a SHRINKING quarter; Sep H.8 borrowing +$54.5B vs FHLB debt +$6.2B, not yet attributable. **Grade the Q3 print against the nowcast too; if it misses by >$40B, find out why (FHLB liquidity drawdown is the named way it breaks).** ★ **10/10 eve: by borrower type (OF Q2 CFR Table 3) commercial banks +$121.4B of the +$136.2B H1 rise (56.4% of advances at 6/30), insurers 24.9% (share ↓), credit unions + savings institutions −$13.7B → more WQ-414 evidence, NOT yet sent to PROME (offered to Will). Everything FHLB now in `research/FHLB/` (README first).** Prior row → `archive/ROADMAP_rotation_2026-09-24b.md`. | 2026-10-10 |
| 🟠 **NDFI instrument (8/20)** | `workbook/NDFI_COHORT.tsv`, 26 banks at FFIEC primary. LESSONS NDFI entry DONE 8/20. 8/20 row → BLOCK R8, `23401de8` | **Open:** registered vector or on-demand pull (base-rate first); ledger SCHEDULED 11/07 | 2026-10-10 |
| *(5 aged July threads)* | **CLOSED 2026-10-10 (Will-directed)** with per-row verdicts → `archive/ROADMAP_aged_threads_2026-10-10.md` (crc32 `fd8df983`): domain-sweep SUPERSEDED · TX/Sun-Belt MF ANSWERED · BKU warehouse/buyout ANSWERED + SUPERSEDED (NDFI cohort) · ZION muni CLOSED, trigger is AEOLUS's · CCC/HY counter NOT BUILT → `ROADMAP_BACKLOG.md`. | — | 2026-10-10 |
| 🟠 **NEW 2026-10-10 — BaaS / sponsor-bank perimeter (WQ-228, Will-ruled 9/15): OPENED because it had NO live row** | CLAUDE.md DOMAIN SCOPE carries the ruling (watchlist CCB · CASH · GDOT; cadence = each 10-Q/10-K partner-concentration disclosure + event 8-Ks), but no STATUS / ROADMAP / CALENDAR row existed, so nothing would have checked it. **First live lead (10/10):** Bluevine's accounts are FDIC-insured "through Coastal Community Bank" (bluevine.com, read 10/10) with a program-bank sweep behind it; VLY is buying Bluevine ($2.1B deposits, close early 2027). ⇒ **a partner-deposit exit at CCB: VLY's deck says the partner program is TERMINATED at closing (early 1Q27) and deposits move within 180 days (~1H27)**; the on-balance-sheet share at CCB vs swept is UNKNOWN. VLY's motive = funding (97% LDR, $5.3B brokered; `KB ML-REG-188/189`). | **CCB Q3 10-Q:** partner-concentration / Bluevine deposit balance, any disclosed transition · **VLY Q3 call Thu 10/22:** migration timing · **Q3 print dates for CCB / CASH / GDOT: NOT CHECKED** → add to CALENDAR when checked. No trade, gate or threshold (the ruling says so). | 2026-10-10 |
| 🟠 **AOCI final-rule watch** | The proposal is net capital RELIEF for Cat III/IV with a 5-yr phase-in to 2032 (CALENDAR H2-2026 row). | Watch for final-rule publication. Full row → `archive/ROADMAP_rotation_2026-09-24.md`. | 2026-08-20 |
| 🟡 **Life-science strategic-default pattern (N=2: WAL $99M + OZK IQHQ)** | #3 test ran 8/31: EMPTY. 9/02 row → BLOCK R9, `7ad64c53` | **Watch only; do NOT re-raise without a third instance**; a thesis-level move lands on STATUS + `thesis/CHANGELOG.md` | 2026-10-10 |
| 🟠 **Cohort-selection rule — does the up-cap finding change WHO is in the screen? — NEW 8/13, dated carry** | **Flagged, deliberately NOT solved.** The cohort was picked under ratio-era priors: MTB/HBAN/VLY were admitted as *clean large-cap benchmarks*, and the Q2 run then found **MTB holding the cohort's largest absolute MI3 book ($4.95B, ~2x WAL) and HBAN +100% YoY** — the control group is where the dollars went. If the question is "who is most concentrated", the cohort is fine; if it is **"where is hidden CRE pooling"**, the selection rule is measuring the wrong population (`finding_ranked_head_sample_is_not_the_population`). **+9/27 (written back 10/07): PFBC (CRE 357% + uninsured 50%, cert 33539) shares Nano/Makhijani collateral and sits OUTSIDE the 14 — a live example that the cohort cannot see a name the failure forensics found (`KB ML-REG-173`).** Not re-cut mid-instrument because that silently changes what every prior figure means. | **Decide before the 2026Q3 run (CALENDAR 11/07)**, so any change lands on a quarter boundary with BOTH cohorts reported once. Read-path is triple: this row, the CALENDAR 11/07 row, and a note beside `COHORT` in the script itself ("do not silently grow the list") so the next runner meets it at the point of temptation. | NEW 2026-08-13 |
| 🟠 **SUCCESSOR: per-bank item-4 → item-9.a migration series** | ⚠️ At OZK the premise changed: MI3 ≡ PV09 (9.a), and L181 adjudicated LEGITIMATE (9/24): the reported debt-on-debt balance fell; runoff is inferred and a relabel is NOT EXCLUDED. | Re-scope at the 11/07 cohort run: test WHERE each bank's MI3 resides (item 4 vs 9.a) before building a migration series. Full row → `archive/ROADMAP_rotation_2026-09-24b.md`. | 2026-09-24 |


---

## AWAITING DATA
*Known external prints with dates. Order = chronological.*

**Added 2026-07-30 (full inbox pass):**

| Date | Item | Why it's mine |
|------|------|---------------|
| **Q3 + Q4 2026 prints** | **`BRK-31` — BROCK's pre-registered falsifier, 45%, resolves 2027-01-31.** *"≥1 of the 11 mapped banks discloses a PC/NDFI-attributable reserve BUILD, or names a private-credit counterparty in a criticized/classified migration, in its Q3 or Q4 2026 print."* **Invalidation:** Q3 **and** Q4 both release-or-flat with no PC/NDFI attribution **and** CFG's combined book still growing at Q4 → BROCK downgrades bank-warehouse 🔴(4)→🟠(3) and **re-dates the whole transmission thesis.** | **I am the data source that resolves it** — it grades on the bank prints I read. Registered off my 7/25 11-name map, which moved BROCK's NDFI vector 🔴🔴(5)→🔴(4) (first score BROCK has moved since 6/20, and it was a downgrade). **Watch for it at the Q3 prints; don't let it get absorbed into "recognition lag."** |
| *(3 fired/resolved rows)* | ROTATED VERBATIM 2026-10-07 → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R3, crc32 `6cbd872a` | — |

*(**Fired during the 5/21–6/2 gap, all dispositioned at the 7/17 audit** — 6 rows, 1,317 B, ROTATED VERBATIM 2026-09-02 → `archive/ROADMAP_rotation_2026-09-02.md` BLOCK M, crc32 `eeb45db6`. All six are closed: MI3/FFIEC PDD RESOLVED 8/7 · FDIC QBP Q1 folded · APO Epstein → BROCK, no-material-event · WALTER LIAISON calibration moot under Routing v2 · ROAD-to-Housing → HOMER · FL reinsurance → CORAL, resolved benign.)*
**Forward (from 6/2) — table ROTATED 2026-09-29 → `archive/ROADMAP_rotation_2026-09-29.md` BLOCK R2, crc32 `f623792c`.** Every row was fired or is CALENDAR-owned (claims weekly · AOCI comment closed 6/18 · Jun-18 expiry cleared · capital-rules final rule TBD · WAL Q2 7/21 graded · CRE-DQ-by-tier Q2 graded · IQHQ Aug swept-empty · OZK sub-notes 10/1 · Affinius Oct). **Forward dates live in `CALENDAR.md` only.**

*Still-pending integrations (printed, not yet worked — see OPEN THREADS): OZK 10-Q; APO Q1 (Atlas SP / warehouse); BLS state jobs + NFP (LABOR/CARL primary, check claims).*

---

## OPEN QUESTIONS
*Flagged but not actively worked. Decide before next acting on them.*

| Question | Surfaced | Action Owed |
|----------|----------|-------------|
| ✅ *Two RESOLVED rows (Exit-100% re-anchor, Will 6/19 · SSB $90P provenance, Will 6/19)* | → BLOCK R3, crc32 `5958e5ae` | Both in force: HY <260 = REVIEW trigger (STATUS §EXIT RULES); SSB $90P = real, sold, unrecorded-exit class (LESSONS). |
| *(five low-priority questions, 4/5–5/1: KB.tsv rows 056/057 column drift · HERMES revival · BROCK in SUB_AGENTS.md · 'sector silence' heuristic · MEMORY vs SCRATCH naming)* | 2026-04/05 | Actions owed verbatim in BLOCK R10, `79a78362`; none dated. KB drift: next workbook hygiene pass |

---

## INVESTIGATIONS BACKLOG → **`ROADMAP_BACKLOG.md`** (cold, on-demand — NOT a boot read)

*6,229 B SPLIT OUT 2026-09-02 verbatim, crc32 `6d6ce8a5`, under READ_CAP rule 4(b).* Nothing in it is dated or owed — it is the pull-list for a research session with no urgent catalyst, so every boot was paying for it and almost no session acted on it. **Re-check size at any append, or on 2026-10-02, whichever is first.**

## RECENTLY RESOLVED
*Last ~2 weeks. Top of mind so the audit trail is visible without reading commits.*

| Date | What | Result |
|------|------|--------|
| *(9/11 row)* | REG-15 NO-OWNER thread closed 9/11 → `archive/ROADMAP_rotation_2026-10-07.md` BLOCK R4, crc32 `0ab0bf65` | — |
| **2026-10-10 eve** | **External FHLB draft checked + FHLB hub (Will)** | `research/FHLB/` (`8d498d5bd`): 2 reports moved (stubs at old paths), verification (3 ledgers: draft = lead list, not a source), key filing tables, sources (PDFs local-only), 25 crc-stamped copies · RED packet: KRE bull case "$480B" vs OF $676.7B / $810.7B (`b9ca8d708`) · WQ-412 SouthState name fixed by PROME (`3780a92d6`) |
| **2026-10-10 late PM** | **FHLB dig + failures list + sweep (Will)** | Q3 nowcast ≈ $770B from FHLB Office of Finance debt (`ce1245f28`) · six 2026 failures at the FDIC list; `DECK_EVIDENCE` Metropolitan cert 57120 → 57488 (`7cbab9f8e`) · sweep: SVB-scale caveat everywhere, stamps, KB ML-REG-186..188, VLY–Bluevine verified, BaaS thread opened |
| **2026-10-10 PM** | **Will's three catch-up items** | ① DAEDALUS as-made audit: all 20 rows, REG-13 re-formed, REG-07 scoring line corrected (`28c7dd7dd`) · ② FHLB composition: half of H1 growth = four very large banks; `REG-T-06` non-discriminating → WQ ask via PROME; weekly H.8: small-bank borrowings +$32.9B in 3 wks to 9/30 → WALTER signal (`e4916e89a`, `e1fc74154`) · ③ five July threads closed (archive crc `fd8df983`) |
| **2026-10-10** | **Overdue process items (Will go-ahead)** | REG-03/06/07 instruments (REG-07 level reading true at birth → graded on the change; VOID is Will's call) · F#4 wording + wiring ⑰ (V1V3 token rename deferred, WALTER reads it) · VX 27 STALE, FLOW frozen, AOCI/FUNDING FROZEN-VINTAGE, KB +3 · large-bank desk packet `32d24f8ff` |
| **2026-10-09 PM** | **Monitor repair + Q3 read plan (Will-directed)** | OZK 8-K/insider → FDIC (OZK desk route reused) · VLY CIK 74260 (= Old Republic) → 714310 · FLG/AMTB/CFG/CUBI covered · no all-clear on failure (network-blocked live test) · countdown ← CALENDAR table · settled bars only · read plan + §2.0 rules · FL frame A3 · baseline: total-CRE 2.23%, MF 3.58% (Q2 rise at FLG/EGBN/CFG = individual) · L180 dry run *c* = 1 |
| **2026-10-07** | **WQ-318 baseline + L527 catch-up (PROME-spawned, Opus)** | `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`: no cheap-deposit flight at 6/30 at any of six; CUBI the one overlap name; pre-committed Q3 list (CFG 10/16 · WAL 10/19 · OZK 10/20 · EGBN 10/21) · 0-WB done (KB +6) · REG-T-03 0-of-3 · FLG RED · WAL Q3 locked → TERRY · inbox 14+19 → 0 · R3 phrases declined (`Nano Banc` covers) |
| *(9/24 + 9/26 rows)* | Rotated VERBATIM 2026-10-10 → `archive/ROADMAP_rotation_2026-10-10.md` BLOCKS R1 `ae15fc12`, R2 `158cd65b` | — |
| *(9/27 PM · 9/29 PM · 9/29 · 9/27 rows)* | Rotated VERBATIM 2026-10-10 PM (2-week rule + read-cap) → `archive/ROADMAP_rotation_2026-10-10.md` BLOCK R4, crc32 `ac6efce7` | — |
| *(rows 2026-09-01 and older)* | **ROTATED VERBATIM** → `archive/ROADMAP_rotation_2026-09-24.md` (2-week rule) and, for 7/17 and older, `archive/ROADMAP_rotation_2026-09-02.md`. | |

---

*Companion files: `MEMORY.md` (curated cross-session memory + session-bridge handoff) | `SCRATCH.md` (loose intra-day notes) | `STATUS.md` (live dashboard) | `CALENDAR.md` (forward dates) | `LESSONS.md` (verified mistake patterns)*
````

## MEMORY.md

crc32 141f468f; bytes 23277

````text
# REGINALD MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate. For verified mistake patterns with prevention rules, see `LESSONS.md`.*

---

## Feedback
- [2026-04-02 ×5] Will: **boot transparency** (say what you read, in what order); **freedom over pre-set priorities** (context not directives; ONE open question, not a ranked top-3); think **long-term infrastructure** (scaling + durability); **position data lives in POSITIONS.md** too; **discrete tasks, approval between each.** Full entries → BLOCK M10, crc32 `2d7441a5`.
- [2026-04-16] Will wants REGINALD to read full source documents (PDFs, 10-Ks) before opining, not just spot-check sections. Caught that I only keyword-searched the earnings release initially. Thoroughness > speed for primary source analysis.
- [2026-04-22] **Iteration philosophy validated:** Write Round 1 with available data, then improve as more data arrives. Will explicitly said "begin with what we have and we will improve on it as we learn more" when public press releases were truncated and he was going to provide supplement PDFs. Don't wait for perfect data to start writing.
- [2026-04-22] **"What I NEED FROM YOU" lists work.** When analysis files end with an explicit gap list, Will reads it and delivers the exact files. Keep these lists concise and specific (filename + what's in it).
- [2026-04-22] **Thesis architecture: "synthesis + pointer" pattern.** THESIS.md carries the synthesized takeaway from sub-docs (2-3 sentences + headline number + pointer), not duplicated detail. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE) hold the deep analysis. Changelog tracks THESIS.md only. Filter: thesis-level shifts get changelog entries; evidence accumulation stays in sub-docs + KB rows. Scope guard: if writing a 4th sentence of sub-doc summary in THESIS.md, it belongs in the sub-doc.
- [2026-04-22] **Per-bank CHANGELOG** mirrors `thesis/CHANGELOG.md` format (vX.Y; first entry pins prior as v1.0) — now `../OZK/`, `../WAL/`-owned. → BLOCK M11, crc32 `05b22ac4`.
- [2026-06-02] **Scope-clean sessions:** Will will explicitly fence a session ("REGINALD files only, no messaging, no position decisions/analysis"). When fenced, refreshing facts (prices, dates, FRED data) and marking resolved events is in-scope hygiene; recomputing EV/overvaluation, sending outbox replies, and making roll calls are out. Flag stale-but-load-bearing values (e.g. SCENARIOS spot price) rather than recomputing — "flag don't re-rate."

## Findings + References → **`MEMORY_REFERENCE.md`** (COLD, on-demand — **NOT a boot read**)

*Split out 2026-09-14 verbatim, crc32 `5db54789`, 11241 B, under READ_CAP rule 4(b). Nothing deleted.* **Holds the HOW-TO and LOOKUP half:** SEC EDGAR curl pattern (WebFetch 403s on sec.gov) · FFIEC CDR REST/JWT · FRED via `fetch.py` + the T+1 convention · the `perl -0pe` table-extraction recipe (a naive `sed` collapses 8-K tables) · catastrophic-regex warning · two-route derived-figure check · FDIC BankFind as an independent cross-check · the paywall map · **OZK files NO SEC periodic reports** · the cert/RSSD/CIK table · the WALTER LIAISON record. **Pull it when you are about to fetch a filing or debug an instrument — not at boot.** ⚠️ **Mistake patterns are NOT here — they stay in `LESSONS.md`.**

## Session Notes

⚠️ **Open question (10/10 late PM):** does the late-September jump in smaller banks' borrowing (H.8 `H8B3094NSMA` +$32.9B / +11.7% in 3 weeks to 9/30; deposits flat) **continue, hold or reverse in the Fri 10/16 print (week of 10/7)**, and does any Q3 print show it **with deposits leaving** (the PNC pattern spreading)? **New 10/10:** FHLB system debt rose only +$6.2B in Sep, so most of that borrowing was likely NOT FHLB (or was funded from FHLB liquidity). The OF combined Q3 figure (~10/29) can only flag the FHLB-liquidity case (advances well above ~$770B); per-bank attribution waits for the 11/07 Call Reports.
- The L180 breadth test (11/07 Call Reports) stays the CRE question; it is in the read plan, not here.
*Prior open question + LAST SESSION 10/9 PM (incl. 10/10 AM) + PRIOR SESSION 10/9 AM → `archive/MEMORY_rotation_2026-10-10.md` BLOCK M1, crc32 `1548bf8c`.*

### LAST SESSION — 2026-10-10 Sat ~16:48 → ~20:4x ET (Will: boot → external FHLB draft → FHLB hub → RED packet → closeout, Opus 5.5)
**Boot:** full read set · market.py (10/9 settled) · ladder rc 1 (FLG RED, 3 closes) · staleness 0 · corrections 0 · inbox 0 · `boot.py` (print window): 8-K alert = CFG 10/6 redemption of its 4% Series G preferred (routine) · BOARD -004/-007 logged.
**Caught:** PROME's WQ-412 called SSB "State Street" → packet `8d31de2aa` → PROME fixed `3780a92d6` (verified at the commit).
**Will's external FHLB draft** (`research/FHLB/sources/`), checked at primary (me at EDGAR + two Opus helpers): **a lead list, not a source.** Fabricated Council quote · GAO "masking" finding reversed · Delaware Life sequence reversed (Feb-26 subpoenas came FIRST) · insurer-share trend reversed · SF's ≥10% borrower is WAL (13%), not JPMorgan.
- **New primaries:** OF Q2 CFR Table 3, commercial banks +$121.4B of +$136.2B H1 · Athene FHLB $27.7B [6/30] (↓ from $28.2B) · Delaware Life $4,963M = 12% of FHLB Indianapolis (#2) · insurer-failure protection = STATE law + collateral (FHFA AB 2013-09), not §10(e) · Citizens Bank N.A. $450M revolver to Delaware Life (undrawn YE25).
**Built (Will):** `research/FHLB/` hub (`8d498d5bd`): 2 reports moved (stubs at old paths), verification, key tables, sources (17 PDFs local-only), 25 crc-stamped copies + MANIFEST; live surfaces re-pointed. **RED packet** on its "$480B" (`b9ca8d708`; RED not live).
**Offered to Will, NOT yet approved:** WQ-414 evidence packet to PROME · SHADE (fabricated quote, state-law point, Citizens line) · BROCK (Apollo vehicle point) · CFG 10/16 read note. Skipped, with reason: POSITIONS (no broker data) · thesis/CHANGELOG (no thesis-level change) · SCRATCH (unused) · LESSONS (lesson 47 carried below, no burned mistake).
### PRIOR SESSION — 2026-10-10 Sat ~14:04 → ~16:4x ET (Will: FHLB dig → 2026 failures → core-file sweep → VLY motive → closeout, Opus 5.5)
**Boot:** full read set · market.py (10/9 settled, weekend) · ladder rc 1 (FLG RED, 3 closes) · staleness 0 · corrections 0 · inbox 0. No pull (PROME's dirty tree).
**Found (`reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`):**
- **Office of Finance monthly debt files run through 9/30** (`cdn.fhlb-of.com/files/Debt%20Statistics/fhlbanalystdata.xlsx`): FHLB debt **−$42.1B in Q3** ⇒ advances nowcast **≈ $770B (±2 sd $728–813B)**, fit corr 0.98 on 25 qtrs ⇒ `REG-T-06` fires as lettered in a SHRINKING quarter.
- **Sep H.8 borrowings +$54.5B vs FHLB debt +$6.2B** (gap 3rd of 41 months): not yet attributable.
- **Scale:** SVB's first week was +$290B in one week; the 9/30 move is ~1/9 of that; large banks +0.9%.
- **Dead ends:** FHLBank 8-K 2.03 (excludes DNs ≤1yr) · H.8 FHLB split (discontinued 2018) · OFR MMF agency (through 8/31 only).
- **Press:** American Banker 9/16 "replace deposits" has no bank-level evidence; filings say PNC only.
**Sent:** PROME WQ-414 addendum (rule early, `047ef11d4`) · WALTER amendment to the 10/10 signal (`b680ef50d`) → **routed with the original as `SIG-W-20261010-007`** (WALTER `40b424536`; LIQUID action, HENRY/BROCK info; card verified to carry all three qualifications + the nowcast). Both live desks doorbelled.
**Will asked (~15:0x):** "6 bank failures this year, REGINALD has that data?" Count CONFIRMED at the FDIC Failed Bank List CSV (6; most since 2017; ≈ $1.45B assets; none in my 14), but the desk had NO single list until `reports/2026-10-10_2026_bank_failures_FDIC_list.md` + a STATUS row. ⚠️ The BankFind failures API index is from 8/25 (returns 4). `DECK_EVIDENCE.md` carried Metropolitan's cert as 57120 (= Uniti Bank) → fixed to 57488; its 10.7%/61% figures were never checked at FFIEC.
**Sweep (Will, ~15:1x–15:3x):** SVB-scale caveat added wherever '160 weeks' was cited (TRADE, ROADMAP) · stamps (STATUS, CALENDAR, ROADMAP) · nowcast pointer on VX-REG-7.01, dashboard, matrix, TRADE · KB ML-REG-186..188 · CALENDAR JWT row (token on both machines) · **VLY–Bluevine VERIFIED and the BaaS perimeter (WQ-228) had NO live row → ROADMAP thread opened.** **Read-cap rotation (rule 5, all three ≥75%):** CALENDAR 24,484 → 21,978 B (C7) · STATUS 24,876 → 22,631 B (T26–T33; incl. the April-vintage owner-held channel cells, which were showing 🔴🔴 as live) · ROADMAP 25,136 → 22,460 B (R6–R10); every crc recomputed from the archive. **Will asked (~16:3x): did VLY buy Bluevine for the deposits?** Yes, by its own deck (funding listed first: $2.1B at 1.44% vs VLY 2.28%, replaces brokered, path to ~90% LDR); a structural gap, not a run (VLY 6/30: 97% LDR, $5.3B indirect/brokered per 10-Q, deposits +$3.4B YoY). Deck: partner program TERMINATED at close (early 1Q27), deposits move within 180 days → CCB exit ~1H27. `KB ML-REG-189`; CALENDAR row. Skipped, with reason: POSITIONS (no broker data), thesis/CHANGELOG (no thesis-level change), LESSONS (no new verified mistake class beyond lesson 46).
*PRIOR SESSION 10/10 Sat ~12:39 → ~13:5x ET (catch-up ①–③ + write-back) → `archive/MEMORY_rotation_2026-10-10.md` BLOCK M2, crc32 `fcf6e807`.*
### CHANGES SINCE LAST SESSION
(leave blank — next-boot market.py + drift-grep populates)
### NEXT SESSION
**★ NEXT BOOT (set 10/10 PM; Will's three catch-up items are DONE, see LAST SESSION):**
0. **(NEW 10/10 eve) Ask Will about the four offered sends** — first the **WQ-414 evidence packet to PROME (borrower-type mix, OF Q2 CFR Table 3), which must land before Will rules by 10/24**; then SHADE · BROCK · CFG read note. Hub: `research/FHLB/README.md`. **At CFG Fri 10/16 (context, NOT a frozen-frame grade):** any mention of the $450M Delaware Life revolver. RED replies on "$480B" only if it disputes. ⚠️ **`NEXUS_BRIEF.md` closed at 24,405 B, 7 B under the 75% read-cap trigger: the next fold must ROTATE first (verbatim + crc to `archive/NEXUS_BRIEF_snapshot_*`), down to <70%.**
1. **Weekly funding read: Thu 10/15 H.4.1 · Fri 10/16 H.8** (`H8B3094NSMA`, `WLCFLPCL`, small-bank deposits + cash, SA AND NSA). Continue / hold / reverse? A deposit decline alongside = the PNC pattern spreading → packet LIQUID + PROME the same session. Bars stay descriptive (base-rate before any registration).
2. **`REG-T-06` re-letter (WQ-414, due 10/24):** Will's word via PROME's WQ row, BEFORE the ~10/29 Q3 figure. On his word: update `registry/THRESHOLDS.tsv` + `registry/NOTES.md`, then ONE packet to LIQUID + BOND (held until then). Without a word, it grades as lettered with the composition read attached. **Grade the print against the 10/10 nowcast (≈ $770B); a miss >$40B ⇒ check FHLBank liquidity drawdown in the Q3 10-Qs. Re-pull the OF debt file each month-end (October ~early Nov).**
3. **REG-07 (WQ-412): Will's VOID-or-grade before SSB prints Wed 10/21 AMC;** without a word, it grades on the CHANGE (scores at 68%).
4. **HBAN puts (WQ-302):** Will sells or rolls by Wed 10/14; write the fill back to POSITIONS from the broker export.
5. **Large-bank desk:** DAEDALUS holds the packet (`32d24f8ff`). Citi / USB / WFC FHLB purpose is that desk's perimeter if built.
6. **BaaS perimeter (NEW thread 10/10):** look up CCB / CASH / GDOT Q3 print dates → CALENDAR; at CCB's Q3 10-Q read partner concentration for Bluevine ($2.1B moving to VLY, close early 2027); ask at VLY's 10/22 call.
*Full 9/29 list (every carried item's text) → `archive/MEMORY_rotation_2026-10-07.md` BLOCK M2, crc32 `401793b1`. Items marked (M2) keep their full text there.*
**🔴 0-Q3. RUN THE Q3 READ PLAN AT EACH PRINT — `reports/2026-10-09_Q3_earnings_read_plan.md` §5 schedule** (CFG **Fri 10/16** first). Grade only the frozen frames: WQ-318 list · CRE top-3 §6 · L35 / L521 · FL frame + A3 · §2.3 AMTB lines. Read the WAL / OZK / FLG desks' grades for their names; the cross-bank row is mine.
- **§2.0 rules govern:** individual ≠ spread · original total-CRE basis, multifamily separate · missing → UNKNOWN · release = provisional.
- **11/07 = planned Call Report retrieval; check completeness FIRST.**
- **Update the §0 judgment only on L180 BROADER or FL-rail TRANSMISSION.**
- **CUBI / FLG dates:** update the CALENDAR earnings table when announced. The countdown reads it, and FLG's T-03 looks 10/16.
**🔴 0a. WAL exit grading:** 10/9 GRADED 10/10 (row 28, 0-of-3). Grade **10/12 onward** from settled bars (`scripts/settled_bars.py WAL`: two routes, today's bar excluded). Count from `registry/REG_T02_EXIT_LOG.tsv` (28 rows through 10/9, 0-of-3). 2-of-3 → packet TERRY.
**🔴 0a-NEW. Tier test each boot:** FRED HY/CCC/B/BB. ⚠️ The cache-busted CSV route FAILED 10/9 (HTTP/2 error / timeout), so the API route (`fetch.py fred`) was used. If HY prints >320 again, START the REG-T-03 count and run the bank-credit cross-check.
**🟢 0-DAEDALUS. DONE 10/10 (Will go-ahead):** REG-03/06/07 instruments named (REG-07 grades on the CHANGE in SSB NPL/loans vs 0.62% base, since its level reading was true at birth; **flagged to Will before 10/21**) · F#4 wording fixes (registry token `V1V3-ACCELERATE` rename DEFERRED, WALTER reads it) · wiring ⑰ VX re-cut · stale tables (VX 27 STALE, FLOW frozen, AOCI/FUNDING FROZEN-VINTAGE, KB +3).
**🟡 0-LIMB. L180's "new foreclosure build" is unquantified.** Read literally (any QoQ rise), WAL met it at Q2 (+2.3%). Print the size beside every grade. A floor is Will's rule to make; don't add one.
**🟠 0-HBAN. `HBAN $16P Oct-16 ×2` ITM — Will rules by Wed 10/14 (WQ-302, card `MGMT-HBAN16P-OCT16`).** Supply the bank-side read if asked; write back the ruling. HBAN prints 10/22, after expiry.
**🟠 0-NEW-PUTS. Fidelity WAL Dec-18 $65P ×4 / OZK Nov-20 $40P ×4 (FORGE D-74):** fills/approval unrecorded; WAL/OZK desks own the position records; TERRY owns any card. My Q3 rows (WQ-318 + CRE top-3) are the thesis reads that bear on them.
**🟠 0a-NANO.** 10/9: P&A **still NOT posted**; FDIC **bid summary posted 10/8** → §3 re-run done (`reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`: retained-pool ≈32–42%). **Re-check P&A Tue 10/13**, then Tuesdays; none by 10/27 → DEWEY records route. On posting: size Pools A/D, place the $97.1M HFS book + WAL O1 DOTs, re-run §2 with pool sizes. Bar date not posted.
**🟠 0a-FL.** ✅ Dates done 10/7 (BKU 10/21 BMO · SSB 10/21 AMC · AMTB 10/22 AMC · SBCF 10/27 AMC; VLY 10/22 BMO). Grade the frozen frame `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md` at each print; ≥2 TRANSMITS → packet CORAL + PROME the same session.
**🟡 0a-0. FLG ladder is RED and EXHAUSTED** — no band beyond RED. Exit-code defect FIXED `b6544d45d`. **Intraday-bar defect FIXED 10/9 (`8255c2d13`).** Census other frozen-baseline bands into the script (M2) — NOT this cycle (Will: no further tooling expansion).
**🔴 0a-bis (M2).** **11/05 FFIEC JWT expiry (Will), two days before the 11/07 run.** *(As-made packet DONE 10/10 PM; the DAEDALUS VX re-cuts were DONE 10/10 as wiring ⑰, per STATUS §OPEN PROCESS ASKS.)*
**🔴 0a-ter (M2). Carry-premise audit** — the most valuable item on this list; unchanged.
**🟠 2 (M2). Pre-print observables into `boot.py`** — base-rate before building. WQ-318 adds the per-bank observables (NIB average, IB cost, FHLB) but they are quarterly.
**🟠 3 · 4 · 6 · 6d · 6f · 6g · 6h · 6i · 6j · 6k · 7 (M2)** — ~~FHLB Atlanta/SF 10-Qs~~ (DONE 10/10) · OREO vector base-rate; REG-07 re-mark + REG-03/07 re-specs at the Q3 print, deliberately; EGBN runway post-break re-audit; read-cap every closeout; `boot.py` SHORT_INTEREST writes; aged 9/2 items. Unchanged; full text in M2.
**🟢 Done 10/10 PM:** catch-up ①–③ + FHLB follow-ups + write-back pass (LAST SESSION). **🟢 Done 10/9 PM:** monitor repair (OZK FDIC route · VLY CIK · coverage · no false all-clear · countdown · settled bars) · Q3 read plan + Will's clarifications. **🟢 Done 10/7:** 0-CARD (TERRY `TRY-COND-KREADD`, conditional, not armed) · 0-EXP (KRE rolled) · 0-WB · 0-WQ318 · item 1 TRY-FIRE-002 dates · DAEDALUS header · R3 phrases.

**CARRIED LESSONS — behaviour, not record.** *Newest first. Aging rule (9/02): full entry → one-line rule AND the full text goes to `archive/` verbatim + crc in the same pass. ⛔ Never age a lesson by deletion (the 12-21 compressions archived nothing; git history only). Preamble → BLOCK M7, crc32 `8028ecb4`.*
47. **[10/10 eve] In a SendMessage to PROME I typed a commit reference ("ab9b-REGINALD") that no command had printed; I sent the real hash (`8d31de2aa`) one message later.** The same session I keyed two FHLBank CIKs from memory (1325878 = Topeka, 1316220 = CAPE Holding); the filer-name check caught both before use.
   - ⇒ **An identifier (hash, CIK, accession) goes into a message only from a command's output in the same turn; a CIK is used only after the response names the intended filer** (lesson 43; `finding_attribution_authenticates_a_figure_its_named_source_never_produced`).
46. **[10/10 late PM] I sent "largest 3-week rise in 160 weeks" to WALTER, STATUS and Will. The 160-week window began 9/13/2023, just AFTER SVB, whose first week alone was ~9× the move.** I had also measured from a 9/09 trough (+11.7% vs +5.9% month-end to month-end). Both were true, and both made it look bigger.
   - ⇒ **A base-rate window must include the episode that defines the scale (here 2023), or name what it leaves out. Quote the change from a neutral base (month-end), not from the trough.**
45. **[10/10 PM] I told Will "the regionals were flat, so this isn't regional stress" from a 6/30 quarterly print, and checked the weekly H.8 only when he asked whether newer data existed.** It showed small-bank borrowings +11.7% in the three weeks to 9/30, the 160-week max. Same day: my own 9/11 receipt had written "Brier on 55%" against WQ-112(i), ratified ten days before it.
   - ⇒ **Before a "this is not happening" read built on a quarterly print, pull the fastest proxy that could contradict it, and date both.**
   - ⇒ **Before writing a scoring rule into a receipt, read the ratified canon (`FORGE/PREDICTION_DISCIPLINE.md`), not the asking packet's framing.**
44. **[10/10] I turned "I can't see deterioration" into "I expect stabilisation," and called the earnings outlook "mixed" without an expectations baseline.** "Mixed" was the expected result of my own test lines, not results against consensus.
   - ⇒ **Not seeing deterioration is not a forecast.** A relief or decline call needs positive evidence plus the market's expectations baseline.
   - **Alarm levels are confirmations, not preconditions.**
   - **Don't swap one unsupported direction for the opposite one.**
43. **[10/9] My 8-K monitor checked VLY under SEC CIK 74260, which is OLD REPUBLIC INTERNATIONAL, and checked OZK at the SEC, where OZK has not filed since 2017.**
   - **Neither could ever look wrong:** a valid feed for the wrong company, and an empty feed for a non-filer, both read as "no 8-K".
   - **Found at the evening boot, not by any check.**
   - ⇒ **An instrument keyed by an identifier must verify the response NAMES the intended entity, and must treat "nothing ever filed here" as a broken route, not a quiet bank.** `finding_instrument_reports_clean_against_the_wrong_reference`.
41. **[10/7] I pre-registered an expiry as 'lapse worthless, decision-free — no roll' (KRE $60P Sep-30). Will sold and rolled it the next day.** His standing practice (USER.md, 9/30) is to sell or roll before expiry. ⇒ **An expiry pre-registration carries a sell-or-roll branch, never a lapse branch, and the write-back reads the broker record, not my forecast.**
42. **[10/7] A Call-Report deposit cost (interest ÷ RC-K average) reproduced the company figure at 3 of 6 banks and was off by 30–60bp at the other 3.** I had built it as the 'one comparable basis'. ⇒ **Check a derived cross-bank measure against each bank's own figure BEFORE using it as the comparable column; the basis that looks cleaner is not the one that is true.**
40. **[9/27] I adopted a peer's 'correction' (CREED's FLG 17.5%) without re-running it, and it was wrong: it added the charge-offs to a denominator that already contained them. My own evidence pack labelled $2,088M as pre-charge-off.** The FLG desk caught it a day later. ⇒ **A correction to my figure gets the same recompute as the figure itself, before I write 'Accepted'** (`finding_a_correction_pass_is_unreviewed_work`). Same session: I told Will PFBC was unchecked against its filings when my own morning report had its Call Report. **Grep my own reports before describing what I have.**
39. **[9/27] A KB fact sourced from an LLM research pass sat INVERTED for 7 months: `ML-REG-044` said 'Fed C&D March 4, 2025'. The date was the Issuu UPLOAD date of the Fed documents, and March 2025 was the order's TERMINATION.** Caught by a peer desk (WAL), not by me. ⇒ **A regulatory action is cited from the regulator's own record (Fed enforcement CSV / agency release), never from a host that re-posts it; a date on a re-host is the host's date until proven otherwise.** Full evidence → `reports/2026-09-27_nano-banc_legal-leg.md` §1.
38. [9/24] Before an inference about a peer's name leaves my desk, read the primary it rests on or label it `INFERENCE FROM SECONDARY`; a brief compresses — check each compressed claim against its own data before sending (three CATO catches in one brief). Full text → BLOCK M6, crc32 `037ca359`.
37. [9/11] A claim about a PEER's ledger stays SEARCH-NOT-FOUND until you open the owner-declared path; assert a peer's STATE from their FILE, never from packet memory.
36. [9/2] A path in my prompt is a claim about the filesystem: resolve symlinks, and `git ls-files --error-unmatch` before claiming an artifact exists. 36-37 full text → `archive/MEMORY_rotation_2026-09-24c.md`.
35. [9/2] A ruling must ship with its retroactive sweep in the SAME commit; sweep by the SHAPE of the thing (a regex), not the value being retired — a supersession marker hides the prior vintage from a token grep.
34. [9/2] A source name authenticates a figure like an exact level does; asked for a construction you never built, return the NEGATIVE WITH EVIDENCE (schema, columns, n=) — silence reads as latency.
33. [8/28] Self-audit before handoff is a fleet standard — measure whether YOU do it on findings you offer.
32. [8/28] Before proposing a threshold, check which DIRECTION it trips and that the level and sign agree — a kill can be sign-inverted as easily as a confirm.
*Lessons 12-31 are indexed in `archive/MEMORY_rotation_2026-09-24d.md` (which points on to their verbatim archives: `MEMORY_carried_lessons_27-31` crc `05486924`, `…22-26` crc `9148add8`; 12-21 in git history).*
*32-35 aged 2026-09-24 to one-line rules (above); full text + the 8/27 housekeeping flags → `archive/MEMORY_rotation_2026-09-24b.md`.*

(leave blank — next-boot market.py + drift-grep populates)
````

## STATUS_DASHBOARD.md

crc32 239b168e; bytes 32964

````text
# REGINALD — SIGNAL DASHBOARD (cold half of `STATUS.md`)

**SPLIT 2026-09-02** out of `STATUS.md` under `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 4(b) *(hot/cold split)*. Moved **verbatim**, contiguous, crc32 `1585e8e9`, 31,189 B — nothing edited in the move.

**This is an ON-DEMAND reference surface. It is NOT a boot read** — do not add it to a boot step, and do not read it whole unless a task needs a specific channel row. `STATUS.md` §THRESHOLD STATUS remains **canonical for every live level**; the rows here carry the ANALYSIS and the audit trail behind each channel.

⚠️ **Rule 7 — this file gets a dated re-trigger, never a leanness claim.** It was 31,189 B at the split and it will grow, because the rows here are where corrections and retractions land. **Re-check its size at any append, or on 2026-10-02, whichever is first**; if it is ever promoted back onto a boot step it re-enters the cap immediately. Instrument: `python3 scripts/read_cap_check.py --agent REGINALD`.

**Verify the split was verbatim (rule 11 — recompute, never trust this banner):**
```
python3 - <<'EOF'
import zlib
s=open('AGENTS/REGINALD/STATUS_DASHBOARD.md',encoding='utf-8').read()
m='<!--DASH-'+'BODY-->'
print(format(zlib.crc32(s.split(m,1)[1].split(m,1)[0].encode())&0xffffffff,'08x'), '== 1585e8e9')
EOF
```

---

<!--DASH-BODY-->## SIGNAL DASHBOARD

| Indicator | Value | Status |
|-----------|-------|--------|
| HY OAS | **267bps** [FRED BAMLH0A0HYM2, **8/26**, refreshed 8/27] | 🟢 **53bp under REG-T-03 (>320); 7bp above the <260 review trigger.** ⚠️ **TIGHTENED 6bp while I was dark** (273 [8/19] → 267) and is now at the **bottom of its 267-275 August range** — moving TOWARD the <260 review trigger, not away. Still no trend break; 267 was also touched 8/14. ⚠️ **Anchor-drift caveat stands [SIG-723-002]** — nominal threshold, composition improved (CCC 10% vs 16% at calibration), so the same print carries MORE stress than the level implies. ★ **8/20: banks fell −4.77% mean (n=26) while HYG/JNK/LQD/BKLN moved −0.18/−0.18/−0.07/+0.07% — credit priced ZERO incremental bank risk.** *(was 270bps [8/7] — refreshed 8/20)* |
| CCC OAS | **1031bps** [FRED BAMLH0A3HYC, **8/26**] → **CCC/HY 3.861×** [8/26] | 🔴 **HARD-FIRE — 19th CONSECUTIVE SESSION >3.6×, unbroken 7/31→8/26** (recounted at the series 8/27, not incremented from memory). ★ **NEW RUN HIGH 3.861 [8/26]**, past the prior 3.790 [8/14] peak. ⛔ **AND IT IS BENIGN — the driver decomposition says so and it is now UNAMBIGUOUS: across the ENTIRE 19-session run CCC went 1034 [7/31] → 1031 [8/26], i.e. −3bp, FLAT. The whole 3.628 → 3.861 rise is the DENOMINATOR** (HY 285 → 267, −18bp). **Numerator has not moved; the ratio is at a run high because HY tightened.** Per `VX-REG-18.04`'s own rule (HY-tightening-led = beta = **NO escalate**) this is a denominator artifact, exactly the shape adjudicated in the 7/13 fire. ⚠️ **Re-arm `CCC ≥1050 AND HY ≥272 ×2 consec` NOT met and now BOTH legs fail** — CCC peaked 1039, still 11bp short; HY below 272 for four straight sessions. ⚠️ **Superlative CORRECTED at the series: CCC 1039 [8/25] IS a 2026 high**, superseding the 1034 [7/31] this row recorded (verified over 172 2026 observations). Series max 1137 [2025-04-07] unchanged (BOND `KB-BND-152`, peer-owned, not re-derived) — 1039 is ~8.6% below it. ⚠️ **THIS ROW READ "NOT ARMED … FALLING" ON 7/29 DATA UNTIL 2026-08-20** — the dashboard contradicted `VX-REG-18.04`'s own HARD-FIRE state for three weeks (LESSON-15 spine staleness, caught on the 8/20 re-sweep). **Escalation STOOD DOWN 8/13 (Will-approved)**; re-arm `CCC ≥1050 AND HY ≥272 ×2 consec` **NOT met — HY leg met (275/273), CCC leg 20bp short.** Run peak 3.790 [8/14]; last 3 closes below it. ⚠️ **1030 is an AUGUST high only** — 2026 max 1034 [7/31], SERIES max 1137 [2025-04-07] (BOND `KB-BND-152`). |
| Initial Claims | **203K** [FRED ICSA w/e **8/22**, refreshed 8/27 off LABOR's spine packet + own FRED pull — ⚠️ **MY "DIRECTION TURNED" FRAMING IS RETIRED AS HALF-STALE: the up-drift STALLED.** Corrected trajectory **198 → 200 → 212 → 207 → 203**; the run's high (212K, w/e 8/8) is now **two weeks behind** and the level ticked **DOWN 4K**. Honest phrasing per the owner: ***"off the July low but no longer rising."*** ⚠️ **w/e 8/15 was REVISED UP 206 → 207K** — my 206 was right when pulled and is now wrong on *two* counts (superseded AND revised). **4-wk MA 205,500** (was 198,750) — ⛔ **the +1,250 MA rise is 100% ROLL-OFF and carries ZERO information** ((203−198)/4 = +1.25K; LABOR pre-committed both the pivot and the term in `CATALYSTS.tsv` *before* the print and reproduced the realised move exactly). **Do NOT cite the MA rise as deterioration.** Continuing claims **1,778K** [w/e 8/15] — LABOR 8/7: the MA's 6th straight decline is mechanical (a ~215K week rolling out), not information] | 🟢 Far from >300K. Prints: 189K [7/18, rev] → 198K [7/25, rev] → 199K [8/1]. LABOR read stands: **low-fire side of a deepening freeze, not strength → bank deterioration is not employment-transmitted.** ⚠️ **NEW context [LABOR 8/7, BLS USDL-26-1291]: NFP July −23K (first negative of cycle, May+Jun revised −103K) — but the firing layer did NOT move** (JOLTS layoffs 1.1% flat, claims sub-200K). **Financial activities −121K since May-2025 peak, credit intermediation −9K in July** — LABOR's inoculated read = big-bank efficiency programs, not stress; the concentrated-vs-programmatic discriminator is MINE at the Q3 prints but **LABOR owns the interpretation** — routed, not re-derived. |
| KRE | **→ §THRESHOLD STATUS (canonical)** — currently **$74.31** [8/28 close] | 🟡 Above $60 by **~23.9%**. **LEVEL DE-DUPLICATED 8/27 eve — this row carries analysis only** (the cell below diagnosed duplication as the drift vector and then drifted anyway: this row ended its path at `74.33`, §THRESHOLD STATUS said `74.36`, the tape says **74.35**. Three surfaces, three answers, one metric — so the level is now a POINTER, not a copy.) (structural fix 8/27: this cell and the threshold block are the SAME metric on two surfaces and have now drifted twice — a 7/30 close carried 24 days, then a 8/21 close carried into 8/27. **Duplicating the level IS the drift vector**; `[[finding_status_spine_staleness_under_appended_top]]`). ★ **Flat-to-down through the dark window** (74.86 → 74.76 → 74.33 → 74.58 → 74.35): the 8/14→8/20 de-rating did NOT extend, and it did NOT retrace either — the cohort is sitting where the selloff left it. **−4.6% off its 77.92 [7/16] 52-week high.** ⚠️ **Still no identified catalyst, now ~9 sessions old.** |
| Brent | **→ §THRESHOLD STATUS (canonical)** — currently **$88.64** [8/27 close] | 🟡 ⚠️ **THIS CELL READ `$88.10 [7/17 settle]` FOR 41 DAYS** and asserted *"oil leg FIRING, +$12.10 on the week"* — a firing call preserved in amber while the threshold block beside it showed $94.39. **Level de-duplicated to §THRESHOLD STATUS 8/27; this row keeps the READ only.** **Current read: the oil leg has GIVEN BACK the July spike** — $88.64 vs the $100.69 [7/23] cycle-high tag (−$12.05) and −$5.75 since the 8/21 close. **The energy path into a hot CPI is materially weaker than a week ago.** ⚠️ **The AOCI/rate transmission does NOT depend on it** (term-premium-driven), so the bank leg is unaffected. FALCON/BRENT own the oil adjudication — routed, not re-derived. |
| 10Y UST | **→ §THRESHOLD STATUS (canonical)** — currently **4.67%** [8/27 close] | 🟠 ⚠️ **This cell read `4.54% [^TNX 7/17]` for 41 days — de-duplicated 8/27, read only.** TERRY arm-#2 (rates fuse) **COMPLETED 7/13** (5 consecutive closes ≥4.50) and **the ≥4.50 streak is UNBROKEN since 7/7 — through the soft July CPI, through the August bank de-rating, and through Brent giving back $12.** ⇒ **the leg is term-premium/supply-driven, not inflation- or growth-driven, and that is what makes it durable.** This is the bank-relevant AOCI/capital-rules input and it has not wavered. |
| **30Y UST** | **→ §THRESHOLD STATUS (canonical)** — currently **5.17%** [FRED 8/25] | 🟠 **De-duplicated 8/27, read only.** **BND-11 (30Y reopen) term-premium "demand-hole" thesis RESOLVED NOT-FIRED 7/9** — indirect bid **77.74%** (needed <52 to fire), dealer 10.05, BTC 2.44 [TreasuryDirect, PROME-verified]; refuted at flow level 3× that week. **The LEVEL, not the demand-hole, is my AOCI-transmission input** — and it eased 11bp off BOND's 5.31 19-yr high while staying ≥5.00. ⚠️ **Carry BOND's two-sided guard: nominally unremarkable vs 1977-98, but `DFII10` 2.41 is ~96.7th pct of its own history / 99.7th post-2010 — extreme in REAL terms, and the real curve impairs a bank's asset side and its borrowers at once.** Open Q routed to SAM/ZHAO: safe-haven-transient vs Japan-duration-extension bid. |
| **CMBS DQ — ⚠️ TWO PROVIDERS, TWO SCOPES, ~8pp APART. `REG-T-07` (>15, sustain-3) EVALUATES AGAINST → **`OFFICE-CMBS-DQ-TREPP`** = **11.91% [July 2026, Trepp primary via WALTER SIG-...-019]** (was 11.57% June) (June) = 3.4pp from fire. NOT against the Fitch overall figure (3.31%), which is 11.7pp away and would read "nowhere near."** *(Row relabelled 7/30 on CREED's 7/27 reconciliation — CREED owns this series and found the two figures sitting under one "Office CMBS DQ" heading; both are correct for what they measure, but a wrong denominator under the right label is how a gate gets mis-read. **✅ REGISTRY EDITS DONE 7/30, PROME-ruled GO** — disambiguation, not a level move: metric field `OFFICE-CMBS-DQ` → **`OFFICE-CMBS-DQ-TREPP`**, and **CREED added to the recipient chain** (`REGINALD action / CREED info / BROCK SHADE info`) — CREED owns the series and was on none of my chains while I am `action` on its `CREED-T-01a`. **No level, window or action changed.** Level divergence >15/sustain-3 vs CREED's >12/sustain-2 is **DELIBERATE** — mine is a bank-transmission *accelerate* gate, CREED's a *recognition* gate — now recorded as deliberate in `registry/NOTES.md`, which nothing previously did.)* **Fitch overall 3.31%** May 2026 (+3bps MoM) — headline near-flat BUT **flows deteriorating: new 60+ delinq +29% MoM to $1.73B, resolutions −25% to $1.54B, 64% maturity-driven** (refi-wall, not term stress). Office *led* fresh inflows (33%) even as office rate ticked down (base/resolution artifact). [SIG-W-20260618-007] *(Trepp office-specific series was 11.69% Apr; Fitch overall-index basis differs — REG-T-07 >15% NOT fired.)* **June 2026 Trepp [verified 7/10, ConnectCRE/Trepp primary]: overall −20bps to 7.35% — but that's a LODGING cure (−79bps to 5.22%); office +4bps to 11.57%, retail +30bps to 6.91%, MF +28bps to 7.23% ALL ROSE.** The headline drop is a lodging composition artifact — **refutes the "~37% CRE-softening" secondary read** that surfaced in the 7/10 sweep; mildly CONFIRMS the office/MF dual-stress leg. [[finding_blended_index_masks_bifurcation]] **NEW 7/17 [SIG-W-20260717-005, ACTION]: the DQ↓/SS↑ divergence = extend-and-pretend printing** — June special servicing overall **11.2% (+34bps)** / office **17.11% (+36bps)** RISING while DQ falls — ⚠️ **UPDATED 8/23: office SS FELL 53bps to 16.58% in JULY** on *"resolutions, paydowns, and workout activity"* (CREED 8/20, primary). **Not a contradiction with `CREED-T-02` firing the same month: extend-and-pretend still works on the SEASONED book while NEW maturity defaults enter through a different door.** ⛔ **16.58% is SPECIAL SERVICING and CANNOT grade `REG-T-07`, which is a DQ bar** — the guard held; SS fires PRE-delinquency (maturity/covenant — a loan can be in SS while current; office SS runs ~5.5pp above office DQ); servicers state the mechanism (lenders unwilling to seize; resolutions via extension/forbearance/new equity). REG-T-07 (>15% office DQ) NOT fired — 17.11% is SS not DQ; office DQ 11.57%. DECK_EVIDENCE #8 mislabel (17.11% as overall/Feb) corrected 7/17. | 🔴 |
| **Multifamily CMBS DQ** | **7.71%** (Apr 2026, Trepp) — **+56bps vector** (office+MF dual-stress). Fitch May: MF = **20% of new CMBS delinquency ($339M)**. **NEW (6/19) supply side: MF housing starts −42% May** (486K→284K SAAR; April's +14.3% offset fully reversed) — construction-finance "deals don't pencil" [SIG-W-20260618-008]. Two-sided: bearish construction lending, but fewer new units props EXISTING-MF collateral/NOI over ~2yr. **June print IN [Trepp, verified 7/10]: MF CMBS DQ 7.23%, +28bps MoM — deterioration continued (June was an increase, not a cure).** ✅ **RECONCILE FLAG CLOSED 2026-08-23 (HOMER 8/22) — and the answer is that it was never two sub-series. It is ONE SERIES THAT ROUND-TRIPS.** Full path, HOMER now holds five points where it held two: **Mar 7.15 → Apr 7.71 → May 6.95 → Jun 7.23 → Jul 7.69.** ⛔ **July 7.69% is NOT a new high** (Apr 7.71% stands **2bps** above it) **and is NOT a wave-start** — it is a **re-test of the April high after a 76bps round trip.** ⛔ **And HOMER's own 8/12 line that July was "the largest single-month MF move in the series" is RETRACTED by its author** — that was true of a two-point series; **April's +56 is larger and May's −76 is larger still and points the OTHER WAY.** ★ **The mechanism the PATH exposes and a LEVEL cannot: THIS SERIES CURES.** A −76bps month is large loans curing at scale ⇒ **CMBS-MF is a lumpy, few-large-loans object and is NOT the same phase as the residential pipeline**, which converts on 563-day timelines with REO +33% and does not round-trip. **Do not cite the two as one phase.** `[[finding_new_pin_needs_trajectory_before_level_read]]` | 🔴 |
| **GSE Multifamily 90d SDQ** | 🔴 **BAND CROSSED — CONSUMED 2026-08-23 (HOMER packet 8/22): Freddie MF DQ 0.51% [Q2-2026, Freddie 2Q-26 Form 10-Q, EDGAR acc 0001026214-26-000046, filed 7/30 — PRIMARY] is THROUGH HOMER's registered >0.50% RED band.** ⚠️ **I have held the 0.51% LEVEL since HOMER's 7/31 packet and never the BAND** — the band lived in HOMER's `CLAUDE.md`, the level in the brief I read, and the two were never joined. *A level with no reference is not a signal* `[[finding_level_without_a_reference_has_two_failure_modes]]`. ⚠️ **THE BAND IS CROSSED AND THE BAND IS ALSO WEAK — carry all three riders: (i) NOT a post-GFC high on either series.** Q3-2025 also printed 0.51% (MBA Q3-2025 Commercial/Multifamily) and Sep-2025 also 0.51% (Freddie Table 6, primary). **Supportable wording is "ties Sep-2025, top of its trailing-13-month range" — NOTHING STRONGER.** A carried "0.39% monthly prior peak" is **UNVERIFIED, not refuted** — unusable in either direction. **(ii) These bands key on a metric a SINGLE loan modification can move 18bps, and the re-spec is OWED and NOT DONE** — Fannie MF SDQ fell 0.78%→0.60% attributed by the issuer to *"the modification of a loan portfolio previously in forbearance and foreclosure activity"* **while Fannie's MF credit provision ROSE 49% QoQ ($174M→$259M).** ⇒ **STANDING INSTRUCTION until HOMER re-specs: pair EVERY GSE MF DQ reading with the SAME FILING's provision direction.** That pairing, not the level, is what held the signal in Q2-26 — and it is my own 7/31 transferable test running in the opposite direction. **(iii) ⛔ MY OWN ROW CARRIED A READ HOMER RETRACTED THE SAME EVENING IT PUBLISHED IT.** This cell said the move was concentrated in the non-credit-enhanced leg (0.13%→0.58%, 4.5×). **DEAD.** non-CE is 8.3% of the book on a denominator that shrank 23.7%; **the corrected read is BROAD — Freddie's Subordination bucket, $311.8B = 62% of the book, moved +9bps vs the +7bps blend — and it is MORE bearish than the read withdrawn** `[[finding_inherited_defect_propagates_though_both_ends_act_correctly]]`. ⚠️ **BASIS FENCE: both GSE metrics are 60+ days on UPB; Trepp CMBS is 30+ days over a different universe. COMPARE DIRECTIONS, NEVER LEVELS.** *(Prior text, still standing on substance:)* **⚠️ "IMPROVING" RETRACTED by HOMER 7/31 (its own correction, Q2 10-Qs verified): Fannie 0.60% headline fall is MODIFICATION-SUPPRESSED** — Fannie's own 10-Q attributes it to a modified forborne portfolio + foreclosures ("loans left the numerator; nobody cured") and warns of "additional delinquencies"; **Fannie MF credit provision +49% QoQ ($174M→$259M) in the same quarter the rate fell. Freddie ROSE to 0.51%, non-credit-enhanced leg 0.13%→0.58% (4.5×), no offsetting modification.** Treat the GSE MF book as **deteriorating with a suppressed headline**. Source: HOMER (one-owner) — do not re-pull. **Companion observed marks [HOMER 7/31]: Banc of California realized ~19.5% haircut on a 94%-MF $827M LOCOM block (charge-offs $161.6M, provision 16× QoQ)** — first *observed* (not modeled) MF severity anchor; caveats: mixed-block average (constr worse / stabilized better), sale-decision discount embedded, n=1. **Arbor REO ~$545M crossed ABOVE delinquencies ~$525M = conversion-not-accumulation phase signature.** | 🔴 (restored — the 7/16 🟠 downgrade rested on the now-retracted improving read; transferable test adopted: **when a DQ headline improves, check the provision line in the same filing**) |
| Bank CRE DQ gap | 4.18% vs CMBS 11.69% = ~7.5pp masking | 🔴 |
| **Bank CRE-DQ divergence — ✅ CLOSED 8/10: the Q1 small-tier leading-creep was LUMPINESS, verdict FINAL on primary** | **The 6/20 question ("do the Q1 30-89 ticks BUILD or REVERT?") is answered at the Q2 10-Qs: 4-of-4 REVERT.** BKU CRE 30-89 **$23.4M → $0** [10-Q 8/6] · SBCF **$12.48M → $7.09M**, seasoned 60-89 **cleared** $7.8M → $1.02M, CRE nonaccrual $55.8M → $43.4M below the Q4 start [10-Q 8/4] · SSB no label→cash-flow conversion (commercial nonaccrual −$10.4M) · AMTB CRE-NOO nonaccrual −16% [7/25]. **The down-tier creep does NOT broaden — severity stays concentrated at OZK/EGBN; the CRE-channel bear is a concentration story, not a tier story (5th independent confirmation).** Megabank leg unchanged (resolving, 1.9%→1.5% Trepp). → `reports/2026-08-10_SBCF_Q2_grade_watchcard_completion.md`; history: `research/CRE_DQ_BY_TIER_2026-06-20.md` pipeline. WAL creep separately idiosyncratic-office (UNCHANGED). Conf ~0.6; **Q2 = do BKU/SBCF leading ticks build or revert (quarter-end/acquired-pool lumpiness)?** **6/22 DEWEY FL-bank-timing corroborates** (research-output grade — EDGAR 403'd them; my 6/20 drill pulled 10-Qs direct = higher grade): independently confirms the BKU-vs-AMTB attribution + adds **SBCF CRE-NOO 224% of RBC** (high single-category concentration; canonical supervisory trigger is total-CRE >300% / constr >100%) + AMTB NPA 1.38→1.93% **[⚠️ CORRECTED 7/18 primary pull: that's a YoY move — QoQ was FLAT 1.91→1.93 (+2bps); AMTB is a weaker CRE-creep signal than the relayed figure implied, see `reports/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md`]**; timing call leading-edge H2'26 / charge-offs 2027. ⚠️ bank-HELD ≠ securitized Fitch CMBS. **★ Q2 2026 VERDICT (7/25, off primary 8-Ks): LUMPINESS CONFIRMED (provisional) — the creep does NOT broaden.** Watch-card frozen 7/18 scored **3-of-3 landed names REVERT**: **BKU** CRE criticized −14.2% ($560.9→$481.3M), CRE substd-nonaccruing −51.4%, NCO 0.61%→0.11% · **AMTB** CRE-NOO nonaccrual −16.0% ($11.17→$9.39M, reversing Q1's +161%), classified −14.7%, SM −25.9% · **SSB** NCO **6bps**, nonaccrual −3.3% QoQ. Pre-committed rule ≥3-of-4 REVERT → **severity STAYS CONCENTRATED at OZK/EGBN; CRE-channel bear does NOT broaden tier-wide.** 4th independent confirmation of the idiosyncratic frame. **PROVISIONAL:** SBCF prints 7/28; and ⚠️ **the card's PRIMARY metric (CRE 30-89 accruing) is a 10-Q table and NO Q2 10-Q is filed by BKU/SSB/SBCF** — spec failure disclosed, lagging buckets NOT substituted, legs marked PENDING-10-Q (~Aug). ⚠️ Two composition traps caught: BKU's headline *"criticized increased $7M"* while CRE FELL $79.6M (the rise is ~$86.6M C&I); AMTB's SFR nonaccrual +320% YoY where the **RATE fell 1.72%→1.60%** as the book grew +29%/6mo by acquisition. | 🟡 (concentration-graded, breadth DISCONFIRMED Q2) |
| Regional-bank IPO/consolidation revival | **NEW (6/19) [SIG-W-20260618-005].** First Carolina (FCBM, ~$3.4B, Raleigh) IPO'd 6/18 NYSE $12.50; Central Bancompany (Nov'25) +20%, Avidbank (Aug'25). 2025-26 community/regional bank-IPO + M&A wave is real (Renaissance/Skadden). **WEAK counter-evidence to the short — supply-side appetite, NOT credit quality.** First regional IPO priced INTO the 6/17 hawkish flip → aftermarket is the test. Genuine REGINALD angle: consolidation wave = WAL/OZK as M&A targets/acquirers (capital-relief headroom feeds it). | 🟡 |
| FHLB Advances | ⚙️ **10/10: composition + base rate → `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` (~half of H1 growth = four very large banks; the >$700B letter does not discriminate; small-bank H.8 borrowings +11.7% in 3 wks to 9/30). **+ Q3 nowcast ≈ $770B (FHLB debt −$42.1B in Q3) → `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`.** Live level → STATUS.** **$810.7B [6/30/26, FHLB OF primary — REG-T-06 at LEG 2 OF 3 on a sustain-3-QUARTERS spec, does NOT fire; fires on the Q3 print if >700]** *(prior row: ~$480B est, issuance +31% YoY — 190 days stale, and the row named the WRONG instrument: FHLB advances are NOT a Fed H.8 series).* **Cohort 7/7 bifurcated:** Surge — MTB/CFG/PNC. Decline — FITB/RF/ZION/**VLY** (-$350M Q1). **Insurer segment [SHADE 6/21]: Athene (Apollo) ~$28B advances drawn / $38B pledged / 135% OC (3/31)** — single insurer ≈6% of system advances; non-bank FHLB draws feed REG-02 (>$600B system-wide). | 🟠 **Downgraded Apr 20** — bank-specific, not sectoral. 3/7 surge = idiosyncratic funding stress at MTB/CFG/PNC. |
| Bank Reserves | $2.8T — 4yr low, G-SIB concentrated | 🔴 |
| Private Credit Default | **6.0% TTM (Apr 2026, Fitch — primary verify pending; surfaced via Bloomberg Tax/Reuters citing Fitch)** — new cycle high; 99 defaults, 81 first-time; **>50% PIK/deferral-driven** (direct V1-thesis PIK-masking confirmation). Was 5.8% Jan. MS projects 8%. Bad PIK 6.4% (vs 2.5% in 2021). | 🔴🔴 Record |
| PC Mainstream | Economist + Bloomberg + NPR all Apr 1. "Signs of strain" / "redemption crisis." Narrative inflection. | 🔴🔴 |
| Blue Owl OBDC II | Permanent gating (Feb). $2.50/sh return-of-capital (~30% NAV) by Mar 31. Liquidation path. | 🔴🔴 |
| Blue Owl OCIC/OTIC | **Apr 2:** OCIC 21.9% redemption requests, OTIC 40.7%. Both capped at 5%. $988M honored / ~$3.2B trapped (OCIC). $179M honored / ~$1B trapped (OTIC). **Apr 29 Bloomberg reframe.** OWL Q1 Apr 30 AMC. | 🔴🔴🔴 |
| Blackstone BCRED | **Q2 2026: FIRST-EVER GATE** — ~$4.4B redemption requests (~10% NAV on $79B fund); Blackstone capped at 5%, excess TRAPPED (Blackstone SEC 8-K Jun 4 2026). Escalation from Q1 ("committed $400M own capital to avoid gate") → structural illiquidity now confirmed. **CARL independently confirmed same primary.** | 🔴🔴🔴 |
| **Partners Group SICAV** | **6/3 redemption cap fired** — €8.6B (~$9B) Global Value SICAV: Q2 demand 9.8-10% vs 5% gate. Sector contagion same day (EQT -6%, CVC/KKR/Bridgepoint down; Partners Group stock down 13-18% across sources — wide range, treat as approximate). Europe PC-wrapper gating event — 4th major PC vehicle to hit gate this cycle (Ares/Apollo/Blue Owl/PG). Verified Bloomberg/CNBC/swissinfo per director audit 6/8. | 🔴🔴 NEW |
| **CCLFX watch (bank-side lane) — PREMISE CORRECTED 7/17** | **De-rated 🔴→🟠 by BROCK 7/17 (no dispute).** Two corrections to the 7/16 spec: **(1) the "forced $1B secondary" fuses two events** — the gate (Q2 ~17% requests vs 5% cap, priced 5/29) and the $1B secondary (PitchBook 3/10, in-market months EARLIER, GP-led Evercore-advised sell-down at 2:1 buyer leverage, Cliffwater retains ~$9B same assets) — B pre-dates A by ~3mo, cannot be its response; no arms-length loan print exists or is scheduled (next CCLFX N-23C3A ~8/7). **(2) My NAV-facility/sub-line ask targeted a channel that DOESN'T EXIST** — Cliffwater has neither [CCLFX/CELFX N-CSRs 6/8/26]. Real channel: **PNC-agented $7.69B facility** (revolver $4.84B committed / $1.25B FY-end **but $3.15B peak intra-year — watch PEAK DRAW, not year-end, 2.5× understatement**) + $6.51B private-placement notes (purchasers undisclosed); syndicate undisclosed (perimeter limit); no financial-ratio covenant. **Only 2 thresholdable held-balance names: CFG** (capital-call $8,756M +2.1% QoQ + secured-PC $4,096M +3.4%) **and WAL** (business-credit intermediaries **$3,415M** = the PC-relevant line; the 25.2% NDFI headline is ~69% mortgage-warehouse — composition trap). ARRANGER ≠ HOLDER; Fed league table not exposure. Direct channel small (full drawdown ≈ 2bp GSIB CET1, Fed) — **if Stage-3 fires the mechanism is INDIRECT**, and the Fed's comfort data pre-dates the gating wave + is perpetual-BDC stats (CCLFX is an INTERVAL fund — category error to apply). **Monitoring spec, NOT a gate row** (no surviving base rate either direction). **Re-test = Q2 10-Qs; WAL prints 7/21 = my dated checkpoint.** BROCK primary. | 🟠 WATCH (corrected 7/17) |
| Leveraged Loan ICR | Share with ICR <1.0x doubled to 20% (from ~10% in 2019). Forced selling by gated BDCs next. | 🔴🔴 |
| FL Foreclosures | +35% YoY, 12th consecutive increase. FL labor 4.6% > US 4.4% (SIG-024-001). **H1-2026 [ATTOM 7/16, via HOMER 7/17]: FL = #1 state foreclosure rate nationally** (0.27%, 1-in-373, 27,494 filings); **5 of top-10 US metros are FL** (Punta Gorda 0.50% worst-in-US, Lakeland 0.48% #2, Cape Coral 0.35%, Jax 0.31%, Ocala 0.31%); timelines shortening (563d, −13% YoY, lowest since 2013) + FL REO conversion fastest-rising → collateral realizing sooner. Path-C residential leg compounding the FL CRE/MF cluster; 30Y PMMS **6.65% [FRED MORTGAGE30US, wk 8/20 — refreshed 8/23 off WALTER `SIG-W-20260822-004`; was 6.55%, and the direction is UP]** = no refi cure, and less of one than the stale row showed. Bank-exposure translation = mine (FL-heavy books: BKU/SSB/AMTB/SBCF watch at 7/22-28 prints [dates verified 7/18; frozen watch-card `reports/2026-07-18_smalltier_FL_CRE-DQ_Q2_watchcard.md`]); raw housing figure = HOMER-owned. | 🔴🔴 |
| "Help with mortgage" | Google Trends ATH (surpasses GFC). Lennar Q1 margin 15.2% — lowest since 2010. Path C activating. | 🔴🔴 |
| NDFI Exposure | $1.54T total (FFIEC Q4 2025) — 5.1x prior $300B model. MS base: $80B bank losses. | 🔴🔴 |
| PC Gating | Ares 5% cap (11.6% requests), Apollo 45¢/$1 (11.2% requests). Warehouse lines = next transmission. | 🔴🔴 |
| CMBS Chicago | $167M office foreclosure — 2026's largest. Loss severity benchmark established. | 🔴 |
| MTB Baltimore | SIG-W-20260426-009: -$1B (29%) reassessed CRE. Sun primary verification pending before trade-thesis weight. | 🟠 NEW |
| Construction Labor | ICE raids → 57 Concrete bankruptcy (TX). 1-in-3 workers foreign-born. Q2 start data at risk. | 🔴 |
| Bank capital-rules package (incl. AOCI) | **Comment period CLOSED 6/18** [SIG-W-20260618-006]. OCC/FRB/FDIC 3-rule package (proposed 3/19): ~4.8% CET1 relief GSIBs / **~5.2% Cat III/IV regionals (WAL/OZK/KRE tier)** / 7.8% community — primary-exact (Holland & Knight). **🔑 The catch:** mandatory **AOCI inclusion** for Cat III/IV (5-yr phase-in) — the **exact SVB-2023 mechanism** (unrealized securities losses → CET1), landing as the Fed flips to HIKE → partly claws back the headline relief through the most rate-sensitive channel. Also brings mortgage origination/servicing BACK in-perimeter (partial re-reg). **🔴 Barr formal dissent (FRB 6-1):** "most significant dereg since 2008," charges **>20 material downward deviations from Basel minimums**, warns thinner buffers into a deteriorating-credit cycle. **Cuts both ways:** near-term tailwind (buyback/M&A headroom) vs longer-term bear amplifier (less cushion against the CRE/NDFI cycle). Final-rule shape = forward catalyst. | 🔴 |
| **Fed DFAST 2026 stress test** | **6/24: $708bn projected losses but ALL 32 banks PASS** [SIG-W-20260624-007]. Aggregate CET1 −1.6pp (12.8→11.2 trough→12.7 rebound); SCBs frozen to 2027 (methodology rework) → buyback/dividend tailwind (Regions $3bn, Zions, Prosperity). **Bull-counter on the kill-list — compounds the capital-relief leg.** **🔑 LOAD-BEARING CAVEAT (does NOT refute the regional short):** DFAST tests only the **32 LARGE banks — the KRE/WAL/OZK small/mid tier driving the short is NOT in the test.** "Banks passed" de-risks GSIBs/big-regionals, not the cohort. The test's own **CRE −39% / $75bn-CRE-loss** scenario underscores the CRE channel tracked. verify CORRECTED-FRAMING 0.88. | 🟡 bull-counter (coverage-limited) |
| MS $85B Transfer | Fed approved MS moving $85B broker-dealer→insured bank (4-3 vote, first ever). Regulatory capture signal. | 🟠 |
| BXMT 1 South Wacker (cross-ref) | **6/9: $343M BXMT loan maturity-default**, Chicago Loop, 73% occ, ~$159M CMBS [SIG-W-20260624-004]. **NOT regional-bank-held** (Blackstone = LENDER via BXMT, not owner) — CMBS/mREIT loss, cross-ref only for the office-refi-wall backdrop behind the CRE-DQ read (office CMBS DQ 11.71%, Chi CBD ~27% vac). Maturity-default mode = refi failure at current rates/values. No bank-level tripwire. | 🟡 INFO |
| Non-bank Servicer Warehouse | **Apr 14 PM research CLOSED:** CARL direct-regional-exposure thesis NOT SUPPORTED. Counterparty data shows ZERO US regional banks as warehouse counterparties to 4 largest public non-bank servicers. Transmission landing point = APOLLO (Atlas SP $6.9B at PFSI alone = 78% concentration). MFS UK template applies — but to Apollo balance sheet, not WAL/FHN/TCBI. WAL still has ~$9.2B mortgage warehouse BOOK, just not to FHA-stressed servicers. See `domain/WAREHOUSE_EXPOSURE.md`. | 🟡 |
| Apollo Atlas SP | Dominant warehouse provider to stressed non-bank mortgage servicers. PFSI: $6.9B (78% of book). LDI Master Repurchase Nov 2024. Adds to existing APO stack (MFS/First Brands fraud, Epstein May 21, Athene). | 🟠 |
| Tricolor Ch 7 bank losses | JPM $170M + **FITB $178M ✅ PRIMARY-VERIFIED 6/8** (FITB Q3'25 10-Q acc. 0000035527-25-000212 — "impairment of an asset-backed finance commercial loan… charge-off of $178M and a specific allowance of $20M"; **C&I classification, taken Q3 2025 not Q1'26**; FITB never names "Tricolor") + Jefferies (First Brands) $40M ≈ ~$388M total. 100% loss severity. **NEW transmission mechanic (REPORTEDLY):** Wilmington Trust shutting non-mortgage ABS custodial business (7 Tricolor trusts $1.8B+ ABS) + $113M receivables FROZEN in ownership dispute. Plaintiff-sourced; corporate-side confirm pending (M&T parent earnings / Wilmington press / ABS trustee-substitution filings). | 🔴 |
| **mREIT distress cluster** | KREF Q1 **div CUT 60%** ($0.25→$0.10) + BV -9% ($13.04→$11.87) + $73.5M CECL surge + Boston life-sci REO $37M loss + **0.53× BV (47% disc)** — apex public mREIT move cycle. STWD $0.39 dist-earn miss + $347M foreclosure. Sternlicht-franchise + KKR-vehicle 3rd-instance (KREF/KREST/FSK). (SIG-W-20260511-025/012) | 🔴 NEW |
| **JPM bank-PE de-risking** | JPM SRT on **$4B NAV-loan portfolio** (12.5% loss slice transferred to outside investors) — NOT divestiture; bank wants downside protection on PE NAV-loan book. MUFG doing same on listed-PC-fund loans. **Bank-PC transmission crystallizes;** cross-confirms Bloomberg "2023 bank-run template for PC stress" framing same day. (SIG-W-20260522-006 + 004) | 🟠 NEW |
| TCW Red Lobster mark gap | TCW PC Fund: equity -98%, debt at par on PIK loan maturing 2029. Mark-to-model fiction. (Bloomberg 4-14) | 🔴 |
| DB Financials positioning | Multi-year low (-1.5 to -2 z) vs consensus earnings growth +20-40% — widest divergence since 2020. **Crowded-short unwind risk** if WAL/OZK/ZION beat. **WAL-specific refresh [recon 7/17]: SI 3.8→4.91% float (+27.75%, FINRA 6/30 report) — shorts BUILDING into 7/21; Street de-risked (zero PT raises, EPS cut −3.16%/30d to $2.33); NO Street NCO estimate exists → credit line = unanchored surprise. `../WAL/PREPRINT_RECON_2026-07-17.md`.** **INSIDER re-run [LABOR 7/20, live EDGAR/FDIC]: no name strengthened — all 3 regionals (WAL/ZION/OZK) HOLD on STALE selling, ZERO new sells + ZERO buys in the 7/9→7/20 pre-print window → mild softener on "insiders bracing for a bad print THIS quarter" (positioning was Q1/early-Q2, now blackout/done). Strength rank OZK (full C-suite convergence) > WAL (Vice Chair Gibbons $3.3M June) > ZION (one EVP $298K May — weakest). Carry into Tue grade.** | 🟠 |

---
<!--DASH-BODY-->
````

## BANK_EXPOSURE_MATRIX.md

crc32 750621ce; bytes 22829

````text
# Bank Exposure Matrix — **v2.0**, rebuilt 2026-08-20

> ## 🔴 THE SCORES CHANGED, AND THE RANKING INVERTED. Read this box before citing any number.
>
> **v1 scores are DEAD** (EGBN 20 · WAL 20 · CFG 15 · OZK 13 · SSB 11 · ZION ~8-9 · FLG 8). They were **not reproducible** — see §5. Do not carry them.
> **The new scale is 0-6, not 0-20+.** A v1 number and a v2 number are not comparable; **compare RANKS, never points.**
>
> | | v1 rank | **v2 rank** | |
> |---|---|---|---|
> | **FLG** | **7th (last)** | **🔴 1st** | ⬅ **the biggest inversion, and it is the finding** |
> | EGBN | 1st= | 2nd= | holds up |
> | **AMTB** | *unscored* | **2nd=** | was never in the v1 table at all |
> | **WAL** | **1st=** | **mid (5th=)** | its bear was always single-credit, never concentration |
> | **CFG** | **3rd** | **last** | clean on both scored channels — ⚠️ **read §4 before concluding "safe"** |
>
> **Why FLG inverted:** it holds the cohort's **highest CRE concentration (327.5%, above the SR 07-1 300% supervisory line)**, the **highest nonaccrual rate (4.88% — 5.5× the cohort median)**, and the **thinnest reserve coverage (ACL/nonaccrual 29%)**. ⚠️ **v1 already knew this** — its own FLG note read *"NYC MF rent-reg"* — **and still scored it last.** A score that contradicts its own notes is the signature of a score nobody could recompute.

> ⚠️ **SCOPE (clarified 2026-09-26, wording only, no score moved):** the credit-quality channel (§1 channel 2) is **BANK-WIDE**: nonaccrual on ALL loans ÷ total loans, and ACL ÷ all nonaccrual. It is **not a CRE-specific measure** and excludes foreclosed property (OREO). A high credit score can therefore come from non-CRE loans (AMTB, 9/26). For CRE vulnerability, read `reports/2026-09-26_CRE_top3_loss_bridge.md`.

**Owner:** REGINALD · **Vintage:** all figures **FFIEC Call Report 2026-06-30**, pulled at the primary 2026-08-20 · **Cohort:** the 14 named MI3-cohort filers (bank-level RSSDs)
**Reproduce:** `AGENTS/REGINALD/scripts/mi3_cohort_screen.py` machinery (FFIEC CDR REST/JWT, `RetrieveFacsimile`/SDF). ⚠️ **JWT expires 2026-11-05.**

---

## 1. THE METHOD — stated, so a reader can recompute the score

**A channel is scored ONLY if it has (a) a named instrument at a primary source and (b) a band anchored to something outside my own judgment.** Channels failing either test are **reported, not scored** (§4) or **pointed at their owner** (§6). *This is the v1 defect the rebuild exists to fix: v1 scored 8 channels, and **not one of them named an instrument**.*

### Scored channel 1 — CRE concentration (0-3)
- **Instrument:** SR 07-1 CRE concentration = **(construction `RCONF158+F159` + multifamily `RCON1460` + non-owner-occupied NFNR `RCONF161`) ÷ total risk-based capital `RCOA3792`**. Owner-occupied NFNR (`RCONF160`) is **excluded**, per the standard.
- **Band anchor — external, not invented:** the **300% supervisory line** in SR 07-1 itself.
- `≥300% = 3` · `200-299% = 2` · `100-199% = 1` · `<100% = 0`
- ✅ **VALIDATED against a company disclosure before use:** computed EGBN **258.2%** vs EGBN's own Q2-2026 disclosed **267.6%** → **−9.4pp (3.5% relative)**. ⚠️ **v1 carried EGBN at 497% AND 547% — both ~2× wrong**, from an ambiguous denominator (its section header cited SR 07-1's total-risk-based-capital while its column header read "CRE/Tier 1"; on Tier 1 the figure is 279.9%, still nowhere near 497%).

### Scored channel 2 — Credit quality (0-3)
- **Instrument:** nonaccrual loans `RCON1403` ÷ total loans `RCON2122`; reserve coverage = ACL `RCON3123` ÷ nonaccrual.
- **Band:** nonaccrual `≥2.0% = 2` · `1.0-1.99% = 1` · `<1.0% = 0`; **plus 1 if ACL/nonaccrual < 100%** (reserves do not cover the nonaccruals already recognised). Capped at 3.
- **Why this band is defensible:** the coverage leg is not a judgment call — **<100% means the reserve is arithmetically insufficient for loans already on nonaccrual**, independent of any view.

**TOTAL = channel 1 + channel 2. Maximum 6.**

---

## 2. THE SCORES — with the arithmetic shown

| Rank | Bank | CRE conc | pts | Nonaccrual % | ACL/NA % | pts | **SCORE** |
|---|---|---:|:--:|---:|---:|:--:|:--:|
| 🔴 1 | **FLG** | **327.5%** | 3 | **4.88%** | **29%** | 3 | **6** |
| 🟠 2= | **EGBN** | 258.2% | 2 | 2.05% | 88% | 3 | **5** |
| 🟠 2= | **AMTB** | 218.4% | 2 | 2.46% | 51% | 3 | **5** |
| 🟡 4 | VLY | 319.5% | 3 | 0.88% | 128% | 0 | **3** |
| 5= | OZK | 259.5% | 2 | 0.92% | 154% | 0 | **2** |
| 5= | WAL | 161.1% | 1 | 0.86% | 86% | 1 | **2** |
| 5= | SSB | 281.0% | 2 | 0.53% | 217% | 0 | **2** |
| 5= | BKU | 193.9% | 1 | 0.95% | 95% | 1 | **2** |
| 5= | SBCF | 229.6% | 2 | 0.66% | 210% | 0 | **2** |
| 10= | ZION | 151.7% | 1 | 0.47% | 226% | 0 | **1** |
| 10= | MTB | 103.9% | 1 | 0.84% | 180% | 0 | **1** |
| 10= | CUBI | 179.2% | 1 | 0.31% | 293% | 0 | **1** |
| 13= | CFG | 95.3% | 0 | 0.96% | 137% | 0 | **0** |
| 13= | HBAN | 83.4% | 0 | 0.84% | 204% | 0 | **0** |

**Three banks carry reserves that do not cover their own recognised nonaccruals: FLG 29% · AMTB 51% · EGBN 88%** (WAL 86% and BKU 95% are marginal). That is the single most decision-relevant column in this table.

---

## 3. WHAT THE RE-SCORE CONFIRMS — and it is consistent with everything else this desk found in 2026

**Severity is CONCENTRATED, not tier-wide** — the same verdict as the FL small-tier watch-card (4-of-4 REVERT, closed 8/10) and the Q1 cohort NCO decomposition (Hypothesis A, 6/8). **3 of 14 names carry a materially elevated score; 8 of 14 score ≤2.** The v1 framing — eight channels, six at 🔴+, a tier-wide detonation — is not what the instruments show.

⚠️ **But the concentration is at DIFFERENT NAMES than v1 believed.** The desk's attention has been on WAL and OZK; on instrumented CRE concentration and credit quality, **FLG, EGBN and AMTB** are the elevated names and **WAL and OZK are mid-pack**.

---

## 3b. ⚠️ FLG TRAJECTORY — added 2026-08-20 PM after a DAEDALUS challenge. **It qualifies the top score and I am not burying it.**

**DAEDALUS asked, against the standard set in §1:** *can the SR 07-1 ratio RISE on a SHRINKING denominator?* — i.e. is FLG's 327.5% an artifact of balance-sheet shrinkage rather than CRE risk? **The right question, and it is answerable at the primary. 11 contiguous quarters pulled:**

| | 2023Q3 | 2026Q2 | change |
|---|---:|---:|---|
| CRE numerator (constr + MF + non-OO) | $48.33B | **$32.76B** | **−32.2%** |
| Total risk-based capital (denominator) | $10.27B | $10.00B | **−2.6% — essentially FLAT** |
| **SR 07-1 ratio** | **470.5%** | **327.5%** | **−143pp, and it FELL IN ALL 11 QUARTERS** |

**⇒ HYPOTHESIS REFUTED, and not narrowly: the ratio is not rising — it has fallen 143pp — and the denominator is not shrinking (capital is flat), so a shrinkage artifact is arithmetically impossible here.** The fall is driven **entirely** by a numerator down a third.
✅ **But DAEDALUS's composition intuition was RIGHT:** multifamily *is* the stickiest leg — construction **−55.6%**, non-OO CRE **−40.8%**, multifamily only **−28.6%**. It just does not produce the artifact, because capital held.

### 🔴 What this DOES change — the level score stands, the story around it does not

**FLG's 3/3 on channel 1 is a LEVEL score and it is correct: 327.5% is above the 300% supervisory line today.** But **the direction is hard, monotonic de-risking, and at this rate it crosses below 300% in roughly two quarters.** Reading "cohort-worst CRE concentration" as *deterioration* is wrong. **This is the EGBN §5 discriminator again — de-risking through a shrinking book vs deterioration, same arithmetic, opposite conclusions** — and on channel 1 FLG is the EGBN case.

### ⚠️ The credit leg answers DIFFERENTLY, and this is where the real signal is

| | peak | 2026Q2 | read |
|---|---:|---:|---|
| Nonaccrual $ | $3.51B [25Q1] | $2.99B | **−15% off peak — improving** |
| Nonaccrual % | 5.49% [25Q3] | 4.88% | **past peak — improving** |
| **ACL $** | $1.27B [24Q2] | **$0.87B** | 🔴 **−31.5%, and it has fallen in EVERY ONE of the last 8 quarters** |
| **ACL / nonaccrual** | 87% [24Q1] | **29%** | 🔴 **monotonic deterioration** |

**⇒ The reserve is being drawn down ~1.7× faster than the problem book is resolving** (ACL −26% vs nonaccrual −15% from their respective peaks). **Nonaccruals improving while coverage deteriorates monotonically for 8 quarters is NOT the de-risking signature** — at EGBN the ACL was *consumed by disposition*; here the ACL is falling against a book that is still $3.0B of nonaccruals.

**⇒ NET, and it is a better read than the one shipped this morning: FLG's score of 6 SURVIVES, but its two legs point in opposite directions. Channel 1 is de-risking (level high, trajectory good). Channel 2 is the live concern, and the load-bearing figure is the 29% coverage — NOT the 4.88% nonaccrual rate, which is past its peak.** Anyone acting on FLG should act on the reserve line.

### 🔴 §3b-ii — ACL ROLL-FORWARD (added same evening, answering FLG-desk's promoted Q2b). **The drawdown is NEITHER disposition NOR release.**

Schedule RI-B Part II, FLG, 2026 H1 — **ties to the dollar**: begin $1,029,999K + recoveries $55,488K + **provision $15,923K** − **charge-offs $232,410K** = **$869,000K**.

**⇒ NOT "release"** — provision is POSITIVE every quarter; reserves were never reversed into income. **⇒ NOT clean "disposition"** either — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet; here the reserve is eaten by realized losses **and not replenished.**

| | provision | charge-offs | CO/prov |
|---|---:|---:|---:|
| FY2023 | $781.1M | $210.7M | **0.3× building** |
| FY2024 | $1,101.6M | $874.5M | 0.8× |
| FY2025 | $180.3M | $436.1M | **2.4× draining** |
| **2026 H1 ×2** | **$31.8M** | **$464.8M** | **🔴 14.6×** |

**Provisioning collapsed −97.1% from FY2024 to the 2026 annualised rate while charge-offs held near half a billion a year.**
🔴 **$869M reserve ÷ ~$465M annualised charge-offs ≈ 1.9 YEARS of runway** at the current pace, against a still-**$2,988M** nonaccrual book.
⚠️ **And it reframes the "improving" nonaccrual leg: a nonaccrual rate falling while $232M is charged off in six months is partly MECHANICAL. A rate falling by charge-off is not a rate falling by cure, and the roll-forward nets — it cannot separate them.** Composition is single-name depth ⇒ **FLG-desk's, not mine.**
⚠️ **Caveats carried: `RIAD` is YTD (the ×2 is my annualisation, not a company figure); 6 of 11 quarters do not tie by the identity (adjustments/M&A, gaps −$12.9M…+$64.8M) though BOTH 2026 quarters tie exactly; and there is no peer base rate on CO/provision yet — 14.6× is not yet established as unusual.**

⚠️ **This is exactly why §7 says "do not read direction from this table."** A level score cannot distinguish a bank getting worse from one working down a large legacy book — **only the series can, and the series had to be pulled to find that the two channels disagree.** `[[finding_verified_figures_do_not_verify_the_shape_claim]]`

---

## 3c. 🔴 RESERVE RUNWAY — a THIRD instrument, built 2026-08-20 eve. **It reorders the cohort and it needs a companion to be read at all.**

**Runway = ACL ÷ TTM charge-offs.** Data: `workbook/RUNWAY_COHORT.tsv` (168 rows, per-quarter charge-offs derived from YTD with the Q1 reset handled).

| | EGBN | WAL | AMTB | OZK | **FLG** | CFG | MTB | HBAN | ZION | VLY | SSB | SBCF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **runway (yr)** | **0.53** | 1.44 | 1.59 | 1.93 | **2.15** | 2.69 | 3.02 | 5.03 | 6.27 | 6.63 | 7.51 | 11.14 |

*Cohort p10 1.43 · p25 2.22 · **median 2.97** · p75 5.08 · p90 6.89.*

### ⛔ THE INSTRUMENT'S BIAS IS INVERTED — read this before using any number above

**Runway assumes the trailing charge-off rate PERSISTS. A bank taking DISPOSITION-driven charge-offs therefore prints a catastrophic runway *because it is cleaning up*.** ⇒ **the metric fires hardest on the healthiest subject.**

🔴 **EGBN at 0.53yr is exactly that case, and this desk has the evidence in its own file: the July grade was *"DE-RISKING THROUGH REALIZED LOSS, escalation NOT triggered"* — CRE concentration 295.1%→267.6%, below the supervisory line, ACL consumed by disposition of classified assets.** **0.53yr is an asset sale's arithmetic shadow, not a run rate.**
⇒ **Do NOT rank on runway without a disposition discriminator.** Unqualified, this column would put EGBN top and be wrong about why.

### And it CORRECTED this desk's own published figure

**FLG runway was published earlier the same evening as ~1.87yr (H1-2026 × 2). TTM is 2.15yr** — H2-2025 charge-offs were lower, so doubling H1 overstates by ~15%. ⚠️ **A convenient annualisation standing in for the actual series** — the same shape as a threshold typed from a rounded display value.
**And the series inverts the story: FLG's runway BOTTOMED at 1.29yr [2025Q1] and has LENGTHENED every quarter since** → 1.29 · 1.59 · 1.90 · 2.36 · 2.25 · **2.15**.

⇒ **THREE of the four instruments now point AWAY from the FLG bear case** (CRE concentration de-risking · nonaccruals past peak · runway lengthening). **Only the coverage RATIO still deteriorates — and it falls partly BECAUSE charge-offs consume the ACL, which is the same mechanism lengthening the runway.** ⚠️ **Those two are in tension and this desk does not resolve it.**

### ★ The generalisation, and it is the day's main methodological output

**Every instrument built today needed a SECOND instrument to tell two opposite stories apart** — de-risking vs deterioration (CRE concentration), cure vs charge-off (nonaccrual), disposition vs release (ACL), asset-sale vs run-rate (runway). **A level scores a state; only the series says which direction produced it.** This is why §7's "do not read direction from this table" is a structural limit of the matrix and not a disclaimer.

---

## 3d. ⚠️ TWO DEFECTS FOUND 2026-09-26 (CRE-vulnerability cut, `reports/2026-09-26_CRE_vulnerability_top3.md`). No score moved. **Remedies are RECOMMENDATIONS awaiting Will's decision (bridge report §5, M1/M2), NOT applied.**

1. **The credit leg cannot see foreclosed property.** It reads nonaccrual (`RCON1403`), and OREO (`RCON2150`) is not nonaccrual. **OZK: $288.1M OREO [6/30/26], up from $150M in one quarter**; counting it, OZK's reserve (ALLL basis, `RCON3123`; 105% on the reported ACL) covers 78% of nonaccrual + OREO, not 154% of nonaccrual. WAL's $126M OREO is also invisible. **Recommended (M1, not applied): score coverage on nonaccrual + OREO.** Data already in `workbook/CRE_RCN_COHORT.tsv`.
2. **The credit leg is not CRE-specific.** AMTB's 3 credit points come mostly from C&I, owner-occupied and residential nonaccruals (CRE = $50M of $169M on the Call Report). As a *bank-wide* credit score that is correct. **As a CRE-vulnerability ranking it misleads.** Recommended (M2, not applied): decide whether to add a CRE-specific credit leg (RC-N by property type is in the same ledger) or to keep the matrix bank-wide and say so in the header.

---

## 3e. NOTES FROM THE 9/27 CRE→BANK WORK (written back 2026-10-07). **No score moved.**

1. **VLY concentration is flattered UP by co-ops.** About **25pp of VLY's ~320% SR 07-1 ratio is co-op lending at a 12% LTV** ($1.8B ÷ implied capital ≈ $7.1B; DERIVED). Co-ops are regulated as CRE but are low-loss blanket mortgages. **Ex-co-ops the ratio is ~292%, under the 300% line.** VLY's channel-1 points are unchanged by rule (the matrix scores the regulatory ratio); a reader comparing VLY to FLG/EGBN should know the gap. Source: `reports/2026-09-27_VLY_CRE_transmission.md` §(2) [VLY Q2 deck s4/s29].
2. **PFBC (Preferred Bank, cert 33539) is OUTSIDE this cohort and would carry channel-1 points** (CRE 357% + uninsured 50%, FDIC API Call Report 6/30/26). It surfaced through the Nano Banc forensics (shared Makhijani collateral), not through this screen — **a blind-spot example of cohort selection** (§7 "cohort ≠ population"; ROADMAP cohort-selection thread; `KB ML-REG-173`). Not added: a mid-instrument re-cut silently changes what every prior figure means; decide at the 11/07 run.

---

## 4. 🔴 REPORTED, NOT SCORED — and a 0 here is NOT a clean bill of health

**These are measured at the primary and carried on every row, but they DO NOT enter the score, because no defensible band exists.** Scoring them would be inventing a threshold.

| Bank | MI3 v1a (hidden CRE) | PC-NDFI % of loans | NDFI nonaccrual |
|---|---:|---:|---:|
| EGBN | **10.77%** *(cohort max)* | 0.00% | $0 |
| MTB | 9.69% | 3.95% | $7.0M |
| WAL | 8.99% | 7.50% | **$122.5M** |
| CUBI | 5.96% | **19.96%** *(cohort max)* | $0 |
| OZK | 5.46% | 8.58% | $25.9M |
| **CFG** | 4.20% | **10.66%** | $0.1M |
| VLY / FLG / BKU / HBAN / ZION / SSB | 4.69 / 2.83 / 3.29 / 3.06 / 1.70 / 0.87 | 2.73 / 1.75 / 2.18 / 3.80 / 1.93 / 0.63 | — |

**Why unscored — the honest reason:** on 2026-08-13 this desk **base-rated** the MI3 ratio and retired its >20% flag **with no successor**, because any cut between 12-20% is a re-description of two banks' own volatility (EGBN's 4-quarter spread is 12.69pp, OZK's 16.37pp, every other bank ≤2.15pp; effective n≈14, not 56). **PC-NDFI has no base rate at all yet.** A threshold without a base rate is a number I would be picking to fit.

⚠️ **⇒ READ THIS BEFORE CONCLUDING ANYTHING ABOUT CFG.** CFG scores **0** on the two scored channels and carries the **2nd-largest private-credit NDFI exposure in the cohort (10.66% of loans, ~$15.9B funded + $22.5B unfunded ≈ $44.5B committed).** **A 0 means "clean on CRE concentration and credit quality," NOT "low risk."** Same caution for CUBI (score 1, PC-NDFI 19.96%) and MTB (score 1, the cohort's largest absolute MI3 book at $4.95B).

---

## 5. 📛 WHY v1 WAS REBUILT RATHER THAN REFRESHED — the reproducibility failure, recorded

**The v1 scores could not be derived from v1's own method.**
- v1's stated rule: **🔴=3 · 🟠=2 · 🟡=1** across **8 channels** (CRE, NDFI, DC, BDC, CONS, FHLB, GEO, MUNI) → max 24.
- v1's own convergence table computes **EGBN 12** and **WAL 12**.
- `STATUS.md` carried **EGBN 20** and **WAL 20** as canonical.
- **There is no derivation of 20 anywhere in the repository.** Git archaeology found no rescale commit, no scale note, no method document. ⇒ **anyone citing "EGBN 20" could not reproduce it** — `[[finding_loadbearing_number_must_be_reproducible]]`.

**Compounding defects, all now moot:** v1's tables disagreed with `STATUS` *and with each other* (EGBN 11 vs 12, CFG 8 vs 9, ZION 6 vs 9); **OZK was absent from the scoring table entirely** despite being a live watchlist name; EGBN's CRE concentration appeared **twice at two values** (497% / 547%), both ~2× the primary; and the Hidden-CRE Screen table ranked banks on the **defective ÷item-4 basis** whose rank the basis itself inverts.

**Archived v1:** `archive/BANK_EXPOSURE_MATRIX_v1_2026-02-23.md` — history only.

---

## 6. UNSCORED CHANNELS → THEIR OWNERS (pointer-only; this desk does not re-derive them)

v1 scored these without instruments. They are real channels; they are **not mine to measure**, and a matrix that scores them on my impression is worse than one that points.

| Channel | Owner | Live state (consumed, not re-derived) |
|---|---|---|
| CMBS maturity / CRE recognition | **CREED** | `CREED-T-02` **FIRED** 8/20 (matured-balloon share >50, effective the June print). ⚠️ CREED's own read: **pre-transmission** — mechanism speed `QUARTERS`, perimeter is securitised paper, not bank-held. `CREED-T-03` (FDIC non-owner CRE PDNA) is the bank-relevant one and has **NOT** fired; **FDIC Q2 QBP ~8/24-29**. |
| Private credit / BDC | **BROCK** | BDC non-accruals ~2.8%, decade high (chart-read, conf 0.65). Bank-side exposure is §4 above. |
| Federal layoffs / DC | **LABOR** | Claims **203K** [w/e 8/22, refreshed 8/27] — ⚠️ the "direction turned" framing is **retired**: the up-drift stalled (198→200→212→207→203, level −4K). LABOR's read is unchanged and is the operative one: **low-fire freeze, not employment transmission**. |
| Consumer credit | **CARL** | — |
| Geography (FL / TX) | **CORAL / MARCO** | FL small-tier card CLOSED 4-of-4 REVERT (8/10). |
| Funding / FHLB | **REGINALD + BOND** | System advances **$810.7B** [6/30]; `REG-T-06` at **leg 2 of 3** on a sustain-3-quarters spec — does **not** fire; fires on the Q3 print if >700 (**nowcast ≈ $770B**, 10/10, `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`). |
| Rates / AOCI | **BOND** | 30Y 5.28%; `DFII10` 2.41 = ~96.7th pct of its own history. AOCI reinclusion nets to **capital RELIEF** for Cat III/IV, phase-in to 2032 — see `CALENDAR.md`. |
| Muni | *unowned* | ⚠️ v1 scored this channel; **no live instrument exists on this desk.** Dropped rather than carried on a Feb-vintage impression. |

---

## 7. WHAT THIS MATRIX DOES NOT DO

- **It is not a short-ranking.** v1 ended in a "SINGLE-NAME SHORT CANDIDATES (FINAL RANKING)" section that mixed exposure with M&A floor and expression. **Trade construction is TERRY's**; this file ranks *measured exposure* only.
- **It is a point-in-time cross-section, not a trajectory.** One quarter. `RCON2746` was shown cohort-wide to be **step-prone** (17/154 = 11.0% of QoQ transitions), so single-quarter Call Report levels move for reporting reasons as well as economic ones. **Do not read direction from this table.**
- **It scores 2 channels, not 8** — and that narrowing *is* a finding, not a gap. Six of v1's eight channels had no instrument on this desk; §6 points them at owners rather than pretending to measure them.
- **Cohort ≠ population.** These are 14 named filers selected by earlier MI3-era priors. **Extending the sample can move a rank** — demonstrated 8/20 when a cross-sectional coefficient collapsed from −0.559 (n=14) to −0.255 (n=26). `[[finding_extend_the_sample_before_publishing_a_coefficient]]`

---

## 8. REFRESH

**Cadence: QUARTERLY, alongside the MI3 cohort screen — next due 2026-11-07 (2026Q3).** Same credential, same RSSDs, same JWT (⚠️ expires **2026-11-05**, two days prior). This is a scheduled pull, not event-driven: the clock advances when the Call Report publishes.
**If this file reads stale after ~2026-11-10 that is neglect, not design.**

*Supersedes v1 (2026-02-23). Rebuild authorised by Will in-session 2026-08-20 ("okay lets rewrite the matrix"). Score changes propagated to `STATUS.md` §Convergence Matrix and `CLAUDE.md` §Bank Watchlist the same session.*
````

## TRADE.md

crc32 9f4246e5; bytes 10763

````text
# REGINALD — TRADE SURFACE

> **LIVE — rebuilt 2026-09-29 ~19:3x ET (stamp corrected at closeout against `date`; first written as ~20:1x from narrative) on Will's word (*"Do it now"*), replacing the March-2026 document (FROZEN 7/09; archived verbatim → `archive/TRADE_frozen_2026-03-07_archived_2026-09-29.md`, crc32 `ab819e73`).** This file carries the trade THESIS, the triggers by name, the refuters and the anti-trades. It carries **no marks and restates no strike it does not own**: position truth is off-repo (Will/broker); the structured mirror is `FORGE/STATUS.md` (PROME/ANVIL, last reconcile **2026-10-07 intraday Fidelity capture**; Robinhood last 9/29); this desk's structural ledger is `POSITIONS.md`. **Trade construction = TERRY; approval = Will (root rule #5).** Re-check size at any append (READ_CAP budget 32,550 B).

## 1. What this desk's trades are a bet on (state 2026-09-29; §2–§3 refreshed 2026-10-07; §1 credit-bet line + §3 trigger states refreshed 2026-10-10 from STATUS, 10/8–10/9 settled)

**Thesis (STATUS-canonical since 8/13):** regional-bank credit stress is **CONCENTRATED, not tier-wide** — 3 elevated names of 14 (FLG 6 · EGBN 5 · AMTB 5, matrix v2.0), the CRE cut narrows to FLG · EGBN · OZK, and the cross-bank Q2 filings showed CRE bad-loan rates FALLING (2.46% → 2.23%). The index expression (KRE) is therefore **tail insurance on a sector repricing**, not a directional call on cohort credit.

**What the tape is doing (attribution 9/29, `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`):** 8/14 → 9/14 was small-cap/market beta with **no** financials component; 9/15 → 9/29 was a **financials-sector move led by the LARGEST banks** (14-name size sort ρ −0.72), in which KRE beat its factor loading and my credit ranking sorted the WRONG way (+0.48). Credit instruments (preferreds, BDCs, HY ETFs) barely moved. ⇒ **A KRE put today is a bet that the large-bank financials repricing continues and drags regionals at ~0.85 beta. It is NOT yet a bet on regional credit.** The credit-shaped exceptions are FLG and VLY (NYC rent-regulated multifamily; worst in both legs; FLG ladder ORANGE 9/28).

**What would make it a credit bet:** B-tier OAS holding >300 into >330 · loans to non-bank financials STALLING in H.8 · a Q3 print cluster (~10/20–28) showing breadth at the mid-pack (DOCKET L180) · an 8-K at a thesis name. None of the credit legs has happened. ⚠️ **10/10: two FUNDING bars from the 9/29 set crossed:** small-bank borrowings +11.7% in 3 weeks to 9/30 (largest in 160 weeks; ⚠️ that window starts after SVB, whose first week was +$290B, ~9× this; FHLB system debt rose only +$6.2B in Sep, so it was likely mostly NOT FHLB money, unless the FHLBanks funded it from their liquidity holdings; not yet separable), and discount-window primary credit above its 60-week p90 for two weeks ($8.74B [9/30], $9.97B [10/7]). Credit-side bars stay 🟢: non-bank lending still growing, no line draws, small-bank deposits flat. That reads as banks lining up cash, not credit reaching balance sheets (`research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`).

## 2. Live legs — pointers, not restatements

| Leg | Owner of the record | State (per FORGE 9/29 reconcile) | Guard / rule |
|---|---|---|---|
| `KRE $60P Dec-18-2026 ×5` | `POSITIONS.md` · FORGE | LIVE, 72 DTE, deep OTM (KRE $68.89 [10/7]) | `REG-T-01` KRE <$60 UN-FIRED; tripwire close ≤$66 → TERRY |
| `KRE $65P Dec-31-2026 ×2` | FORGE (`MGMT-KRE65P-DEC31`, `5ce609f80`) | **NEW 9/30 — Will's own roll:** the Sep-30 $60P ×2 was SOLD 9/30 @ $0.01 (−$451.48, leg 1) and these bought @ $1.68 (leg 2) | TERRY rail: hard stop Thu 12/31 15:00 ET (not a price gate) |
| `WAL $70P Dec-18-2026 ×1` (RH) | `../WAL/` · FORGE | LIVE, the ROLL70 duration roll (filled 9/02 @ $2.20); RH not re-captured since 9/29 | `GATE-TERRY-ROLL70-EXIT` = `REG-T-02` exit: WAL ≥ $81.90 ×3 closes — **0-of-3 after 26 graded closes through 10/7** (`registry/REG_T02_EXIT_LOG.tsv`) |
| `WAL $65P Dec-18-2026 ×4` (Fidelity) | FORGE D-74 | **NEW vs the 10/1 mirror** (fill/date/approval UNRECORDED); 12.6% OTM at $74.35 [10/7]; spans the 10/19 print + Q3 10-Q | No card. ROLL70's gate does NOT transfer to this line. Thesis read → memo `PROME/inbox/2026-10-07_from-REGINALD_WQ318-baseline-T03-and-ladder.md` |
| `OZK $40P Nov-20-2026 ×4` (Fidelity) | FORGE D-74 · `../OZK/` | **NEW vs the 10/1 mirror** (fill/date/approval UNRECORDED); 8.2% OTM at $43.56 [10/7]; spans the 10/20 print + FDIC 10-Q | No card. OZK desk thesis (RESERVOIR) + its own <$45 band; thesis read → same memo |
| `HBAN $16P Oct-16-2026 ×2` | `POSITIONS.md` · FORGE | ITM since 9/26 (mark $0.85 [10/7 rcv]); the 7/18 "rides to expiry" premise FAILED | Card `MGMT-HBAN16P-OCT16`; **Will rules by Wed 10/14 (WQ-302)**. HBAN prints 10/22, AFTER expiry (OZK desk calendar) |
| `APO $95P Dec-18-2026 ×1` | `POSITIONS.md` · FORGE | LIVE, 72 DTE; BROCK thesis vehicle | Will ruled HOLD 8/13; vehicle-mismatch flag live (BROCK) |
| `KRE $25P Jan-15-2027 ×1` (RH) | FORGE only | Deep-OTM lottery, entry never recorded (D-54) | Not thesis-scope |

**Open card(s):** **KRE-put ADD (Will asked 9/29) → TERRY built `TRY-COND-KREADD` 9/30 08:12 ET (`AGENTS/TERRY/setups/KRE_add-puts_conditional-card_2026-09-30.md`): CONDITIONAL, NO FILL.** Arms only on a REGINALD instrument (`REG-T-03` ×3 with the bank-credit cross-check, a FAILED L180 breadth test, or `REG-T-01`) **plus** X1 open or Will's Tier-3 word **plus** a green day. **State 10/7: NOT ARMED on my legs** — `REG-T-03` 0-of-3 (peak run 1, 10/1), `REG-T-01` UN-FIRED, L180 grades 11/07. No Will decision is owed until it arms (root rule #10 loop: proposal recorded; decision pending the arm). Separately, Will rolled the Sep-30 KRE leg himself (row above).

## 3. Triggers this desk grades (levels live in `STATUS.md` §THRESHOLD STATUS — never here)

| Trigger | Letter | State (vintage in each cell; live levels → `STATUS.md` §THRESHOLD STATUS) | Consequence |
|---|---|---|---|
| `REG-T-01` | KRE < $60 | UN-FIRED, 13.1% away (KRE $69.01 [10/9 settled]) | 🔴 to ALL; the KRE puts' thesis level |
| `REG-T-02` | WAL < $78 | **FIRED since 9/1 (cycle 2)**; exit ≥ $81.90 ×3, run 0-of-3 (28 rows through 10/9, $74.27) | Guards ROLL70; 2-of-3 → packet TERRY |
| `REG-T-03` / `-04` | HY OAS > 320 ×3 / > 350 | **0-of-3** at the 10/8 cell (315); 324 [10/1] was 1 of 3, reset by 310 [10/2] | Credit transmission — **run the bank-credit cross-check first** (`reports/2026-07-30_bank-side-HY-attribution.md`) |
| `VX-REG-18.04` / `18.05` | CCC/HY > 3.6× ×3 · B-tier > 300 / 330 / 380 | HARD-FIRE (3.975× [10/8]; CCC 1,252 = FRED-window high, both legs widening, no CCC-led re-cross) · B 315 [10/8] = YELLOW; peak 329 [10/1], 1bp under ORANGE | Escalation SENT 9/26; watch, not re-escalate (Will 9/26) |
| `VX-REG-6.03` | FLG ladder −10 / −15 / −20% vs $14.24 | **🔴 RED — broke on the 10/7 close $11.30** (−20.6%) | Packets PROME + FLG sent 10/7 (`018af9846`); no band beyond RED |
| `REG-T-06` | FHLB advances > $700B ×3 qtrs | leg 2 of 3 ($810.7B [6/30]); composition 10/10: ~half of H1 growth = four very large banks | Q3 print (~late Oct) fires it. ⚠️ **The letter does not discriminate** (>$700B in 12 of 26 quarters since 2020); re-letter question with Will via PROME (WQ-414, due 10/24). **Q3 nowcast 10/10 ≈ $770B** (FHLB debt −$42.1B in Q3; `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`) ⇒ fires as lettered while lending likely shrank |
| Claims (LABOR) | > 300K | → `STATUS.md` (LABOR owns) | all ORANGE banks → RED |

**Exit rules** (STATUS §EXIT RULES, unchanged): HY < 260 is a REVIEW trigger, not an auto-exit (Will 6/19); BTFP-2.0 = thesis broken (auto-exit); CRE-channel anchors (WAL NCO ex-fraud < 25bp AND no office migration; office CMBS-DQ flows reversing 2 prints + bank CRE-DQ tier-creep reversing).

## 4. Refuters for any bank put on this desk (write them on the card)

B-tier OAS back **< 300** (a 9/15-style reversal) · HY back **< 280** · KRE reclaims **$72.74** (the 9/16 gap-down close) · a clean Q3 print cluster (no mid-pack breadth, L180) · H.8 non-bank lending re-accelerating with small-bank deposits stable · ~~LABOR's bull-side kill (Sep NFP ≥ +150K, 10/2)~~ did NOT fire: payrolls +29K, net revisions −60K (WALTER -20261002-001) — the labor leg stands.

## 5. Anti-trades (tempting, and the evidence says no)

- **Single-name puts on my top-scored names as a "credit" expression.** EGBN and AMTB (matrix 5) were the two BEST performers of the selloff (−2.9% / −0.2% vs KRE −10%); the market is not pricing my ranking. A credit thesis needs a print, not a score.
- **Adding on a red day.** Root rule #6: puts on GREEN days. Breaking it needs the direct measurement written on the card before the fill (`AGENTS/TERRY/RISK_RULES.md`); "the window is closing" is a chase. 9/29 was red.
- **Treating the March document as live.** Its eight-channel frame, its April earnings plan and every leg in it are dead (archived with crc above). Cite `STATUS.md` for thesis state.
- **Reading a HY level as bank transmission.** The 7/27–29 sustain over 280 was BANK-ABSENT; HY sits downstream of bank credit in my chain. Cross-check first.
- **Trimming for size when the thesis is intact.** Root rule #7: roll duration, don't trim (trimming = thesis broken). Any roll rides on TERRY's card.
- **Chasing the deposit-flight narrative with a trade.** "Agentic bank run" (Slok 9/27) is a mechanism frame with no flow data; it was a WQ-318 question, answered 10/7: no NIB-share decline at any of the six banks through 6/30 (`reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`), so nothing to grade yet.

## 6. History — what this desk's names have done to the book

Jun-18 / Jun-30 clusters cleared (FORGE 7/16) · Jul-17 legs lapsed OTM (WAL $65P, ZION $57.5P, FLG $13P ×3) · **Aug-21 `KRE $60P ×3` lapsed worthless — broker-confirmed on the FORGE 9/29 ledger (five Aug-21 rows, realized −$2,816.72 book-wide)** · WAL Sep-18 pair (`../WAL/`) expired 9/18, broker-confirmed 9/21, −$1,519.34 · SSB $90P and KRE $70P = the two unrecorded-exit phantoms that built the POSITIONS-first rule (`LESSONS.md`). **Lesson the book keeps teaching: deep-OTM index puts with sub-quarter tenor have lapsed four times in a row; the live expressions that have paid or held are the duration roll (WAL Dec-18) and the ITM HBAN leg nobody expected.**

---
*Owner REGINALD. Levels → `STATUS.md`; strikes/qty → `POSITIONS.md` + `FORGE/STATUS.md`; construction → TERRY; approval → Will. Rebuilt 2026-09-29; prior file archived verbatim (crc above).*
````

## workbook/VX.tsv

crc32 21bb51e9; bytes 55102

````text
# Last real data refresh: 2026-10-09 — (TOUCHED 2026-10-10, no data moved: 27 rows with Last_Updated before 2026-08-11 marked STALE, their prior status kept in Notes, so the fresh header no longer certifies a stale body; also the DAEDALUS wiring ⑰ re-cut — VX-REG-5.01 / 8.01 / 14.01 RETIRED, 14.03 RETIRED + CANNOT-FIRE, 17.01 re-pointed to BROCK VX-BRK-003 as the one Medallia figure.) FOUR rows moved: `VX-REG-18.02` HY 315 [10/8] (REG-T-03 0-of-3 at the 10/8 cell), `18.04` 3.975x (CCC 1252 new window high, both legs widening, no re-cross, no escalate), `18.05` B 315 [10/8], `6.03` FLG $11.35 [10/8] (2nd close below RED; ladder exhausted). FRED via ALFRED vintage 10/9; closes yfinance + Nasdaq API. Prior header (10/7): 2026-10-07 — FOUR rows moved: `VX-REG-6.03` (★ RED band broke on the 10/7 close $11.30; packets PROME+FLG), `18.02` HY 303 [10/6] (REG-T-03 0-of-3; 324 [10/1] one print), `18.04` 4.007x (HY-tightening-led, no escalate), `18.05` B 302 [10/6] (peak 329, ORANGE not reached). Prior header (9/29): 2026-09-29 — TOUCHED 2026-09-29: THREE rows moved — `VX-REG-6.03` (★ ORANGE band 2 broke on the 9/28 close $12.04; packets PROME+FLG), `18.04` CCC/HY 3.795x (CCC 1146 / HY 302 [9/28]), `18.05` B tier 309 (★ first >300, YELLOW). Prior header (9/26) → git history.
ID	Name	Category	Current_Value	Yellow	Orange	Red	Status	Confidence	Last_Updated	Source	Cross_Links	Notes
VX-REG-1.01	KRE ETF Price	1-Bellwether	$77.35	-10%	-15%	-20%	GREEN	90%	2026-08-12	market.py live	ML-REG-001	LIVE. $77.35 (+0.70% 8/12) — ~29% above the $60 acute line. Cohort risk-on regime intact.
VX-REG-2.01	Regional CLO Holdings	2-Credit	Concentrated: RF $4.17B (13.5%)	Sector-wide	RF-specific	RF + others	STALE	85%	2026-01-26	10-Q/10-K	ML-REG-005	REFRESH-OWED (Q1/Q2 10-Ks). Structural claim (RF=HIGH, BANC=ELEVATED). Do not re-cite $ without a fresh 10-Q pull. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-01-26 (>60 days); status was GREEN. A GREEN read from 2026-01-26 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-2.02	CLO AAA Spreads	3-Systemic	~125bps (consensus est, Mar 27)	150bps	165bps	180bps	STALE	75%	2026-03-27	PitchBook/MS/Barclays	ML-REG-004, FLOW-REG-1.01	OWNER-DEFERRED (LIQUID). >165bps = BDC transmission trigger; ask LIQUID for a fresh mark before citing.
VX-REG-2.03	BDC NAV Discount	5-Shadow	-16% avg (-21% median)	>10%	>15%	>20%	STALE	70%	2026-01-26	CEF Connect	ML-REG-003, FLOW-REG-9.01	OWNER-DEFERRED (BROCK). CEF Connect data not web-fetchable — needs manual cefdata.com pull. Likely WORSE given Ares/Apollo gating since Jan.
VX-REG-3.01	CRE Loan 90+ DQ	2-Credit	4.06% PDNA non-owner-occ (Q4 2025, >$250B banks)	>3%	>5%	>7%	STALE	90%	2026-03-27	FDIC QBP Q4 2025	ML-REG-002, CREED	REFRESH-OWED (FDIC QBP Q1 2026 — the standing missed-print in ROADMAP §Awaiting Data). Q4 read: 🟠 ABOVE ORANGE (down from 4.99% peak Q3 2024, still 7× pre-pandemic 0.58%). ★ 2026-08-27: THIS ROW IS THE PARENT OF CREED's DISPUTED 3.40 — identified when CREED could not reproduce 3.40 at the source VX-CREED-4.01 names. The FDIC publishes TWO different CRE PDNA objects and the row had fused them: (i) NOO-SPECIFIC >$250B, which is THIS row's series, published in QBP Chart 11 NARRATIVE not a table cell — Q3-24 peak 4.99, Q4-25 4.06 as the 5th consecutive decline; (ii) COMBINED nonfarm-nonresidential, a standing table cell — Q3-25 3.20, Q4-25 3.23 (a RISE), Q1-26 2.73, Q2-26 2.48. CREED graded T-03 against (ii) while the level came from (i). My Cross_Links already named CREED and my Notes already carried the 4.99, so I am the likely propagation path. Answered to CREED 8/27. ⚠️ STRUCTURAL, carry it: series (i) lives in a CHART + narrative sentence, so a text-grep misses it and an edition can plot it WITHOUT restating the number — a level leg on (i) can become silently unquotable. ★★ 2026-08-27 SAME DAY, CREED READ THE Q1-2026 EDITION AT PRIMARY AND MY OWN DESIGN-RISK FLAG IS CONFIRMED, HARDER THAN I STATED IT. 3.40 is NOT in the Q1-2026 QBP in any shape: zero occurrences of 4.06 or 4.99, the only non-owner mention is qualitative and numberless, and DECISIVELY that edition has only EIGHT CHARTS — there is no Chart 11. A chart can hide a number from a text extractor; a chart that does not exist cannot. So this is NOT an extraction caveat — the SERIES IS ABSENT FROM THAT EDITION. ⇒ CORRECTION TO MY OWN WORDING ABOVE: I said an edition can plot the series without restating the number. The truth is stronger — AN EDITION CAN OMIT THE SERIES ENTIRELY. Series (i) is published EPISODICALLY, in whichever edition features that chart, and the chart NUMBER is edition-specific (Chart 11 is the Q4-2025 edition's numbering, not a stable address). ⇒ CONSEQUENCE for anyone re-pointing here: fix (a) is DEAD. Re-pointing a trigger at the Q1-2026 QBP would name a source that does not contain the value — which IS the original defect, recreated by its own obvious fix. CREED caught it only by executing the fix and looking at the result. ⇒ 3.40's PROVENANCE IS NOW UNKNOWN, not merely unread. The arithmetic still fits perfectly (4.06 [Q4-25] -> 3.40 [Q1-26] is the 6th consecutive decline, exactly what VX-CREED-4.01 claimed, so BOTH its claims succeed on this basis having failed together on the combined one) — but no document either desk has opened contains it. Do NOT cite 3.40 as read, and do NOT attribute it to the Q1-2026 QBP. ⇒ MY REFRESH-OWED ON THE Q1-2026 EDITION IS NOW POINTLESS FOR THIS SERIES and I am recording that rather than spending the pull: CREED read it, the number is not there. Refresh-owed stands only if I want the COMBINED cell (2.73 Q1-26 / 2.48 Q2-26), which CREED already supplies. ⚠️ STILL UNREAD BY ANYONE: series (i) for Q1-26 and Q2-26 — because it may not exist in those editions at all. CREED ref KB-CREED-026, commit 9c7d30030. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-4.01	Deposit Flight Rate	4-Funding	TBD	-2% QoQ	-4%	-6%	STALE	70%	2026-02-16	Call Reports	FL-REG-002, FL-REG-019	REFRESH-OWED (Call Reports Q1/Q2 2026). Never populated with actual figures. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-16 (>60 days); status was GAP. A GAP read from 2026-02-16 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-5.01	Japan Regional Bank Exposure	6-Cross-Border	¥9.7T CLO (Norinchukin)	Qualitative	Qualitative	Qualitative	RETIRED	75%	2026-02-16	BOJ FSR	ML-REG-006, SAM	OWNER-DEFERRED (SAM). Structural datum on Norinchukin. | RETIRED 2026-10-10 (DAEDALUS wiring ⑰): qualitative thresholds, no instrument, owner-deferred to SAM since 2/16; the Japan-contagion channel is owner-held (SAM) and no longer a REGINALD thesis claim. History kept; do not read as current.
VX-REG-6.01	RF (Regions Financial)	1-Bellwether	$31.66	-10%	-15%	-20%	GREEN	85%	2026-08-12	yfinance live	ML-REG-007	LIVE. +21.6% from $26.03 (3/27) → GREEN not YELLOW. Cohort risk-on rally consumed the -9% approach. CLO concentration bellwether.
VX-REG-6.02	VLY (Valley National)	1-Bellwether	$14.89	-10%	-15%	-20%	GREEN	80%	2026-08-12	market.py live	ML-REG-026	LIVE. +22.6% from $12.15 (3/27). Q4 BEAT held; CRE 58%+.
VX-REG-6.03	FLG (Flagstar/NYCB)	1-Bellwether	$11.35 [10/8 close] vs FROZEN baseline $14.24 [8/12] = **-20.3%**; RED ($11.39) broke 10/7 $11.30; 2nd settled close below RED 10/8 (yfinance + Nasdaq agree)	-10%	-15%	-20%	🔴 **RED — band 3 BROKEN 2026-10-07** (state machine: worst band breached; no band beyond RED). Packets PROME + FLG sent 10/7 (018af9846) per the 9/24 registration	85%	2026-10-09	yfinance daily bar + Nasdaq historical API (independent route) agree to the cent, pulled 2026-10-07 21:5x ET; `scripts/vx_ladder_check.py` rc=1	ML-REG-027, FLG-desk (dual-action 8/20), BANK_EXPOSURE_MATRIX v2.0	★ 2026-10-07: RED broke on the 10/7 close $11.30 (-2.25% on the day; KRE -1.68%, VLY -1.50%); path 9/30 11.67 · 10/1 11.69 · 10/2 11.70 · 10/5 11.57 · 10/6 11.56 · 10/7 11.30. FLG -3.4% vs KRE -1.5% since 9/30. Cause UNKNOWN; no FLG 8-K since 7/24. Matrix score 6 UNCHANGED (price is not an input). The registered ladder is exhausted at RED: no further price packet is registered | ★ 2026-09-29: ORANGE broke on the 9/28 close ($12.04, -2.67% on the day vs KRE -1.40%, VLY -2.29%); caught by vx_ladder_check.py at the first boot after the close (zero session lag; band 1 sat 8 days). No FLG 8-K since 7/24 (EDGAR 9/29). Matrix score 6 UNCHANGED (price is not an input). Registered next step: settled close <= $11.39 = RED -> packet PROME + FLG again same session | 2026-09-26: last close $12.37 [9/25] (9/24 12.39); YELLOW unchanged, 8 closes below band 1 since 9/16; ORANGE $12.10 is -2.2% away (vx_ladder_check.py). | ★ **2026-09-24 — BAND 1 BROKE 9/16 AND SAT UNSEEN 8 DAYS (FLG packet 3547db167, verified at my own two-route pull).** Cause of the miss: **no detector existed** (PROME 9/23 census) and this row was last refreshed 8/20, with its status cell reading GREEN-BUT-APPROACHING as live. ⚠️ **I also printed FLG $12.30 in `market.py` at 9/24 boot and did not check it against this ladder; the number was on my screen.** **Fixed MECHANICALLY: `scripts/vx_ladder_check.py` (exit 1 on any band breach), falsified by a negative control truncated at 9/15 (GREEN, rc 0), then live (YELLOW, rc 1). Wired into boot step 7.** **COHORT RULING (my half of the dual-action split):** ① **Matrix v2.0 score UNCHANGED (FLG 6).** The matrix scores filed instruments (CRE concentration, credit quality, reserves), and there has been no FLG filing since the 8/14 13F-NT; price is not an input. ② **The move is a SECTOR/NY-GROUP move plus rates, not an FLG break:** 8/28→9/23 per FLG desk: FLG −8.5% / VLY −6.8% / KRE −4.7% / EGBN +1.8%. The FLG residual vs VLY is ~−1.7pp, cause UNKNOWN (9/15 Barclays fireside unrecovered). **The market is NOT sorting on my matrix** (EGBN, scored 5, is UP), so this does not validate the matrix ranking. ③ **No escalation at YELLOW. ORANGE ($12.10 close) → packet PROME + FLG the same session** — at that point it is the top-scored matrix name and the bellwether 15% under a frozen reference. ④ Rent-freeze annulment suit (FLG KB-FLG-053/T-12) is FLG-owned and cuts FLG-BULLISH. **PRIOR NOTES:** ★ **RE-POINTED DUAL-ACTION 2026-08-20 (REGINALD ruling, DAEDALUS flag).** FLG became its own desk today; this vector's METRIC is FLG. **Chain is now REGINALD + FLG-desk, not REGINALD-only.** ⚠️ **This is the PAT-063 shape and we have a live receipt for it TONIGHT: `REG-T-02` (WAL-PRICE<78) stayed REGINALD-only through WAL's promotion and the ownership gap surfaced only AT FIRE TIME** — PROME needed a state adjudication with WAL $1.15 from the line. **Not repeating it on FLG.** **Split: FLG-desk owns the single-name read (why it moved, fundamentals); REGINALD owns the cohort/matrix consequence.** Neither re-derives the other; tie-break on any FLG figure is THE PRIMARY, not either ledger. ⚠️ **BASELINE IS FROZEN, NOT TRACKED** — $14.24 [2026-08-12] is a fixed reference, so the bands are absolute levels ($12.82 / $12.10 / $11.39), NOT a rolling window. Stated because an unlabelled baseline is exactly how a threshold quietly becomes a family `[[finding_threshold_level_is_a_measurement_not_a_constant]]`. ⚠️ **STATUS TOKEN SHARPENED: plain GREEN under-reported proximity.** At −5.3% it is **53% of the distance to band 1** — technically GREEN, practically approaching, and DAEDALUS was right that the token hid it. ★ **AND THE FUNDAMENTAL CONTEXT NOW EXISTS, which it did not on 8/12: FLG is the TOP-SCORED name in the rebuilt matrix (6/6)** — cohort-worst CRE concentration 327.5%, nonaccrual 4.88%, **ACL/nonaccrual 29%**. ⚠️ **But see matrix §3b: the two legs DISAGREE** — CRE concentration is de-risking hard (470.5%→327.5%, down all 11 quarters), while **reserve coverage deteriorates monotonically (87%→29% over 8 quarters)**. **The load-bearing figure is the 29%, not the 4.88%.**
VX-REG-6.04	WAL (Western Alliance)	1-Bellwether	$82.13	-10%	-15%	-20%	YELLOW	90%	2026-08-12	market.py live	WAL-01, WAL-02	LIVE. +0.30% from $81.88 (7/17), ~$4.13 ABOVE the $78 threshold; tape not confirming the bear. Q2 print graded 7/22 NOT-surprise-tier (WAL-01/02 → 25%/50%). ⚠️ REG-24/25 EXTRACTED to WAL-01/02 at cutover 7/25 — cross-link updated.
VX-REG-6.05	CFG (Citizens Financial)	1-Bellwether	$73.64	-10%	-15%	-20%	GREEN	85%	2026-08-12	market.py live	ML-REG-049, FLOW-REG-5.01	LIVE. +27.4% from $57.78 (3/27) → GREEN. Q2 clean-benchmark CONFIRMED 7/16 (NCO 37bps 6th straight ↓, coverage 152% ↑).
VX-REG-6.06	CMA (Comerica)	1-Bellwether	DELISTED (Feb 2 2026)	—	—	—	RESOLVED	100%	2026-03-27	SEC/NYSE	ML-REG-010	RESOLVED. Merger closed Feb 1 → FITB at 1.8663 shares. Cutover systems weekend Sep 5-7 2026 (CALENDAR).
VX-REG-6.07	KEY (KeyCorp)	1-Bellwether	$22.88	-10%	-15%	-20%	GREEN	80%	2026-08-12	yfinance live	ML-REG-010	LIVE. +14.7% from $19.94 (3/27). Office NPL + equipment fraud exposure standing.
VX-REG-6.08	ZION (Zions)	1-Bellwether	$71.68	-10%	-15%	-20%	GREEN	85%	2026-08-12	market.py live	ML-REG-042	LIVE. +29.4% from $55.40 (3/27) → GREEN. Q2 graded 7/20 (5-of-5 tells benign; AOCI IMPROVED +$68M QoQ = opposite of bear tell).
VX-REG-6.09	AUB (Atlantic Union)	1-Bellwether	$42.44	-10%	-15%	-20%	GREEN	85%	2026-08-12	yfinance live	ML-REG-033	LIVE. +22.0% from $34.79 (3/27). Federal metro; sold $2B CRE proactively.
VX-REG-6.10	EGBN (Eagle Bancorp)	1-Bellwether	$28.74	-10%	-15%	-20%	YELLOW	90%	2026-08-12	market.py live	ML-REG-034	LIVE. +17.3% from $24.51 (3/27) → YELLOW not RED. Q2 graded 7/25 = DE-RISKING through realized loss (CRE conc 295→268% below the 300% line, NPA 1.31→1.17%, CET1 +78bps). Prior "ALREADY IN CRISIS" framing SUPERSEDED.
VX-REG-7.01	FHLB System Advances	3-Systemic	$810.7B [6/30/2026, FHLB OF Q2 Combined Operating Highlights, pub 7/30]	$700B	$750B	$800B	🟠 LEG 2 of 3 (level breached, sustain NOT met) — DISCRIMINATOR RESOLVED 2026-08-23	85%	2026-10-10	FHLB Office of Finance, Q2-2026 Combined Operating Highlights PDF (cdn.fhlb-of.com) — via BOND 8/19	ML-REG-009, FLOW-REG-3.01, REG-T-06, BOND VX-BND-18/KB-BND-140	★ 2026-10-10 late PM Q3 NOWCAST (ML-REG-186, reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md): FHLB Office of Finance debt -42.1B in Q3 ($1,330.8B [6/30] -> $1,288.8B [9/30]) => Q3 advances ~$770B (+/-2sd $728-813B), so the Q3 print very likely FIRES REG-T-06 as lettered while lending shrank ~5%. Current_Value stays the 6/30 print until the OF Q3 figure. | ★ 2026-10-10 COMPOSITION READ (ML-REG-185, reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md): H1 +$136.2B par = ~half four very large banks (PNC +27.4, Citi +20.0, USB +14.0, WFC +6.0); 106 mid/small SEC filers +$2.3B, median 0%; Atlanta +6.9%, SF -10.6%. BASE RATE: system >$700B in 12 of 26 quarters since 2020, so the $700B line does not separate stress from the 2023-24 plateau; re-letter question to Will via PROME. | ★ **DISCRIMINATOR RESOLVED 2026-08-23 AT PRIMARY, AND IT POINTS AWAY FROM STRESS.** BOND handed me the WHY on 8/19; this row carried it UNRESOLVED with a 0.35-conf lean. Now ~0.85 on two independent primary paths that agree. **The FHLBank Pittsburgh +111% H1 spike is ONE MEMBER: PNC.** PNC Form 10-Q (EDGAR 0001628280-26-053170, filed 8/05): **FHLB advances $13.0B [12/31/25] → $40.4B [6/30/26], +$27.4B / +211%** — that single name is **~67% of FHLBank Pittsburgh's entire H1 increase** and **~20.5% of the WHOLE FHLB system's H1 advance growth** ($133.7B). Corroborated independently at the FHLBank's own 10-Q (EDGAR 0001330399-26-000089): borrowing **members FELL 128 → 126**; five largest borrowers **70.6% → 82.1%** (top five = $37.9B of the $40.9B increase = **93%**); PNC capital stock **$547.9M/23.8% → $1,587.7M/40.5%**, i.e. **64.5% of the entire member capital-stock build**. **WHY, from the borrower's own balance sheet:** loans **+$36.5B/+11.0%** and securities **+$11.3B/+8%** against total deposits **+$8.9B/+2%** — and the deposit line is **acquisition-inflated** (FirstBank Holding Co closed 1/5/26, $4.2B consideration, 95 CO/AZ branches, goodwill +$2.36B). The clean ORGANIC measure is the cash-flow financing line: **interest-bearing deposits −$11,862M in H1**. Fed cash drawn $32.0B → $22.2B. ⇒ **ASSET GROWTH + ACQUISITION FUNDING with a deposit-mix leg — NOT a distress draw.** Credit is clean (NPAs −$211M/−9%, delinquencies stable) and **brokered deposits were CUT $5.1B → $2.1B**, which a funding-stressed bank does not do. ⚠️ **THE OTHER SIDE IS REAL AND MUST TRAVEL WITH IT: PNC's UNUSED FHLB capacity fell $50.7B → $37.7B (−26%)** and total contingent liquidity $241.4B → $229.1B in six months. **Benign PURPOSE, real BUFFER CONSUMPTION** — and "advance-depletion narrative" is a REGISTERED escalation leg on BOND's `VX-BND-18`. ⚠️ **n=1: PNC explains PITTSBURGH, not the system.** The OF primary's "advances to large members" is CONSISTENT with the same mechanism system-wide; I have tested one FHLBank and one member and will not extend it. ⚠️ **Term structure does NOT discriminate on its own** — FHLB-Pgh variable-rate advances $15.6B → $54.6B vs fixed ~flat $21.2B → $23.2B, 64% due ≤1yr. Short-and-floating is what a matched-book growth funder takes AND what a precautionary borrower takes. **The purpose was established at the BORROWER's balance sheet, not the FHLBank's.** ⚠️ **VINTAGE FENCE UNCHANGED: 6/30 data, published 7/30. It cannot date any August tape move and must not be fused with one — honest pairing is two independent 🟡s.** **REG-T-06 leg 3 (Q3, ~late Oct/early Nov) is UNAFFECTED as a registered trigger — but its INTERPRETATION now requires the composition question at fire time, not the level alone.** → `ML-REG-160`. || 🟠 **LEVEL breaches the VX Red band ($800B) — but `REG-T-06` DOES NOT FIRE, and the reason is the sustain count, not the level.** REG-T-06 = `>700, sustain **3 consecutive QUARTERLY prints**`. Series: **Q4-25 $677B (BELOW → resets) · Q1-26 $734B (leg 1) · Q2-26 $810.7B (leg 2)**. ⇒ **RUN = 2 of 3. Fires on the 2026Q3 print if >700** (OF combined report ~late-Oct/early-Nov). **$110.7B above the level and still not fired** — the binding constraint is time. ★ This is a **dated, pre-registered, high-likelihood forward fire** and is the single most decision-relevant thing on this row. ⚠️ **This desk did not pull it; BOND did, 8/19.** $810.7B at 6/30/26 = **+20% vs YE25** ($677B), **+10.4% Q/Q** ($734B at 3/31). Driver per the OF primary verbatim: *'an increase in advances to **large members**'*; **FHLBank Pittsburgh $36.8B→$77.7B, +111% in six months** [med-conf: two wire copies of the bank's own 7/23 release, 10-Q primary UNREAD]. ⚠️ **VINTAGE IS THE WHOLE CAVEAT: 6/30 data, published 7/30, full CFR 8/13. A +20% figure is a SIX-MONTH change, not news — it cannot be read as a fresh event and cannot date any August tape move.** ⚠️ **BOND's own non-fires carried, not dropped:** its +15% Q/Q leg NOT met; both its escalation legs NOT met; $810.7B is **11% below** BOND's $900B line and ~19% below the SVB-era ~$1.0T peak. ⚠️ **DISCRIMINATOR UNRESOLVED and it is MINE per BOND's handoff:** precautionary liquidity vs deposit-outflow replacement vs asset growth. Advances are a *funding-mix* choice, and cheap FHLB funding against a steep curve is an ARBITRAGE as often as a distress tell — the level alone does not separate them. ⚠️ **INSTRUMENT CORRECTED 2026-08-20: prior Source cell read 'Fed H.8', which is WRONG — FHLB advances are NOT an H.8 series.** Publisher = FHLB Office of Finance Combined Financial Report (quarterly, ~30d lag). ★ **THE 190-DAY GAP HAS TWO DISTINCT CAUSES AND I CHECKED WHICH APPLIED WHEN (git, not memory): (a) 2/11→8/13, 183 days — the ONLY named instrument anywhere was this wrong one; `registry/THRESHOLDS.tsv` was still 8-col and carried NO `grading_instrument` at all, so 'refresh' had no executable path** `[[finding_registry_names_a_concept_tool_resolves_an_instrument]]`. **(b) 8/13→8/20, 7 days — the CORRECT instrument existed** (I encoded it myself in `653cec3d7`) **and the series still went unpulled** `[[finding_unfetched_is_not_unavailable]]`. ⚠️ **The two registries disagreed for 7 days and nothing flagged it** — THRESHOLDS said FHLB-OF while VX said Fed H.8. **A per-row instrument field is only a control if something diffs the registries** `[[finding_owner_of_record_means_authoritative_not_correct]]`. Peak $675B (SVB 2023).
VX-REG-7.02	FHLB Collateral Haircuts	3-Systemic	2025 tightening active	+5%	+10%	+15%	STALE	85%	2026-02-02	RQ-REG-C01	ML-REG-042	REFRESH-OWED. Structural, low tempo. Participations 58%, 2nd liens 49%. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-02 (>60 days); status was YELLOW. A YELLOW read from 2026-02-02 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-7.03	FHLB Pledging Status	4-Funding	Blanket Lien (best)	Listing	Delivery	Suspension	STALE	80%	2026-02-02	RQ-REG-C01	ML-REG-042	REFRESH-OWED. Fraud → Delivery Status. Forensic audit freezes liquidity. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-02 (>60 days); status was GREEN. A GREEN read from 2026-02-02 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-8.01	HOA Special Assessments	7-Regional	Active FL/NV	>$5K/door	>$10K/door	>$15K/door	RETIRED	85%	2026-01-26	County Records	ML-REG-012, FLOW-REG-6.01	OWNER-DEFERRED (CORAL). Super-lien priority. | RETIRED 2026-10-10 (DAEDALUS wiring ⑰): owner-deferred to CORAL since 1/26; FL HOA / SIRS special assessments are CORAL's surface (`../CORAL/STATUS.md`). Do not read as current.
VX-REG-9.01	CRE Modification Wave	8-Accounting	$27.7B (+66% YoY) — UPDATED	>$25B	>$35B	>$50B	STALE	99%	2026-03-04	FDIC/CIRCUIT_BREAKERS inbox Mar 3	ML-REG-016, FLOW-REG-7.01	REFRESH-OWED (next FDIC QBP). Q4 2025 read: $27.7B +66% YoY. WFC 10% charge-off on current mods. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-04 (>60 days); status was RED. A RED read from 2026-03-04 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-9.02	CRE Modification Exhaustion	8-Accounting	>50% re-default	2nd mod >30%	>40%	>50%	STALE	90%	2026-01-26	Trepp/Moody's	ML-REG-017	REFRESH-OWED (Trepp). FLG -142bps allowance cut = reverse indicator. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-01-26 (>60 days); status was ORANGE. A ORANGE read from 2026-01-26 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-9.03	Open-End Fund NAV Drift	5-Shadow	ODCE queues ~12% of NAV (down from 20% peak)	Queue >10%	>15%	>20%	STALE	85%	2026-03-27	PREA/NCREIF	ML-REG-018, FLOW-REG-8.01	REFRESH-OWED (PREA/NCREIF). Queues easing but still >10%. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-9.04	BDC PIK Interest Inflation	5-Shadow	Golub 173% spike	PIK >15%	>20%	>25%	STALE	85%	2026-01-26	BDC 10-Q	ML-REG-019, FLOW-REG-9.01	OWNER-DEFERRED (BROCK). Cash NII declining; dividend cuts follow. See PROME NAMED-ASK context: BROCK disambiguates its own "20% PIK" trigger on NII-vs-TII basis in-packet (my side clean; this row is a *concentration* vector, not the BDC-income ratio).
VX-REG-10.01	Deposit Composition Shift	4-Funding	Monitoring	Uninsured >40%	>50%	>60%	STALE	75%	2026-03-27	Call Reports	ML-REG-020	REFRESH-OWED (Call Reports). SVB pattern: uninsured flight. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was YELLOW. A YELLOW read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-10.02	NIM Compression	4-Funding	Monitoring (no cuts since Sep)	-5bps QoQ	-10bps	-15bps	STALE	80%	2026-03-27	10-Q	ML-REG-021	REFRESH-OWED (Q2 10-Qs). ⚠️ Framing note went stale: "SOFR 3.65%, Brent $112" — SOFR still 3.65 [8/11], but the whole rate-path premise (FOMC hawkish hold + higher-for-longer + 10Y 4.67%) supersedes the specific Mar-27 language. FOMC held 3.50-3.75% 9-3 on 7/29 with three dissents FOR A HIKE. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was YELLOW. A YELLOW read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-11.01	AUB Federal Metro Exposure	6-Cross-Border	HIGH	UCFE +200%	+400%	Credit loss	STALE	70%	2026-02-01	LABOR	ML-REG-032	OWNER-DEFERRED (LABOR). DOGE → federal job loss → DC bank credit. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-01 (>60 days); status was YELLOW. A YELLOW read from 2026-02-01 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-11.02	DC Metro Unemployment	6-Cross-Border	6.7% (DC Dec 2025) / 6.1% (DC metro Nov 2025)	>4.5%	>5.5%	>6.5%	STALE	90%	2026-03-27	BLS/DOES	ML-REG-037	REFRESH-OWED (BLS Q1/Q2 2026 releases). DC highest in nation at last read. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was RED. A RED read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-11.03	DC UCFE Claims YoY	6-Cross-Border	UCFE 584/wk (Mar 14); 7,400 continuing (Feb 15, +12% YoY)	+200%	+400%	+600%	STALE	80%	2026-03-27	DOL	ML-REG-037	OWNER-DEFERRED (LABOR — see LABOR 8/7 for the current NFP/EPOP-respec context; U-3 no longer keyed to my thresholds). | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-11.04	EGBN Deposit Trend	4-Funding	$9.1B total (-4% QoQ Q4 2025)	-2%	-4%	-6%	STALE	85%	2026-03-27	EGBN Q4 2025 earnings (Jan 21)	ML-REG-034	REFRESH-OWED (EGBN Q2 print filed — pull deposit lines from the 8-K/10-Q). | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-12.01	Endowment Forced Selling	5-Shadow	Yale ~$3B negotiating (<10% discount) + Harvard $1B	>$10B agg	>$20B	Gates	STALE	80%	2026-03-27	Bloomberg/Yahoo/TIFF	ML-REG-048, FLOW-REG-5.01	REFRESH-OWED (Bloomberg pass). Yale's FIRST-EVER PE sale; Trump endowment tax 1.4%→21% threat. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-13.01	CRE/Equity Concentration	2-Credit	1,788 banks >300%	>2,000	>2,200	Sector event	STALE	85%	2026-02-02	FAU Screener	ML-REG-052	REFRESH-OWED (FAU Screener Q1/Q2). Count INCREASING. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-02 (>60 days); status was ORANGE. A ORANGE read from 2026-02-02 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-13.02	Office CRE Loss Severity	2-Credit	70-97% actual	Gap >40pp	>50pp	Recognition	STALE	90%	2026-02-02	RQ-REG-I01	ML-REG-053	Structural gap vs 20-40% modeled. Held. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-02 (>60 days); status was RED. A RED read from 2026-02-02 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-14.01	Shunto 2026 Outcome	6-Cross-Border	¥18,000 = STRONG	<3.0% Weak	2.5-3.5% Mod	≥3.5% Strong	RETIRED	90%	2026-02-27	SAM/HEARTBEAT	SAM VX-SAM-8.05, FL-REG-023, ML-REG-080	RESOLVED Feb 19. Strong = 85% April BOJ hike. Path D window closed. | RETIRED 2026-10-10 (DAEDALUS wiring ⑰): event RESOLVED-STRONG 2/19 (Shunto); no live consequence on this desk. Was RESOLVED-STRONG.
VX-REG-14.02	20Y JGB Auction BTC	6-Cross-Border	3.08 (Feb 19) = PASSED	<3.0x Weak	<2.5x Stress	<2.0x FAIL	RESOLVED-PASS	90%	2026-02-27	MOF	SAM VX-SAM-3.03, FL-REG-024, ML-REG-080	RESOLVED Feb 19. BTC 3.08 = strong demand. Path D did NOT fire.
VX-REG-14.03	Japan Repatriation Rate	6-Cross-Border	$10-15B/mo ACTIVE	¥500B/mo	¥1T/mo	¥2T/mo	RETIRED	90%	2026-02-16	SAM Intel	SAM VX-SAM-9.02, FLOW-REG-13.01	OWNER-DEFERRED (SAM). Life insurers SELLING UST for JGB 30Y 3.6%+. | RETIRED 2026-10-10, CANNOT-FIRE (DAEDALUS wiring ⑰): deferred to `SAM VX-SAM-9.02`, a row that does not exist (SAM VX.tsv FROZEN 8/17, 0 matches). No live SAM surface carries it. Was STALE.
VX-REG-14.04	Wright Current→Delinquent	2-Credit	0.7% transition rate (Dec 2025, ICE)	>400K/mo	>500K/mo	>700K/mo	STALE	80%	2026-03-27	ICE/Liberty St Econ/MBA	CARL, FLOW-REG-14.01	OWNER-DEFERRED (CARL). See CARL 8/11 packet: CC 90+ DQ 13.12→12.92% (bureau moved WITH bank-side data). | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was YELLOW. A YELLOW read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-FAIL-01	Metropolitan Capital Failure	2-Credit	Failed Jan 31	—	—	—	STALE	95%	2026-02-12	FDIC	ML-REG-055	CONFIRMED historical. First 2026 failure. $261M Chicago. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-12 (>60 days); status was CONFIRMED. A CONFIRMED read from 2026-02-12 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-15.01	SOFR-IORB Spread	4-Funding	0bp (SOFR 3.64 [8/11] / IORB 3.65 [8/12])	+5bps	+10bps	+15bps	GREEN	90%	2026-08-12	FRED SOFR/IORB	FLOW-REG-3.01	LIVE. No funding stress signal. LIQUID trigger: >+15bps = FHLB spike.
VX-OTTO-1.01	Auto 60+ Day DQ	2-Credit	7.1% (Equifax Dec 2025)	>5.5%	>6.0%	>7.0%	STALE	90%	2026-02-27	OTTO	OTTO_INTEL.md	OWNER-DEFERRED (OTTO). 32-year high; leads bank auto NCOs by 1-2 quarters. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-27 (>60 days); status was RED. A RED read from 2026-02-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-OTTO-1.02	2022 Vintage CNL	2-Credit	22.42% at 31 months	>18%	>20%	>25%	STALE	85%	2026-02-16	OTTO	OTTO_INTEL.md	OWNER-DEFERRED (OTTO). Crisis-level cumulative net loss; 2022 vintage "broken."
VX-OTTO-1.03	Auto Recovery Ratio	2-Credit	30.58%	<40%	<35%	<30%	STALE	85%	2026-02-16	OTTO	OTTO_INTEL.md	OWNER-DEFERRED (OTTO). vs 41% benchmark; severe loss given default.
VX-OTTO-2.01	Carvana Stock	1-Bellwether	$71.54 [8/12] ⚠️ VERIFY vs old $302 basis — likely stock-split adjustment	-20%	-40%	-60%	CHECK	60%	2026-08-12	yfinance live	OTTO_INTEL.md	LIVE-with-CAVEAT. yfinance returned $71.54 [8/12] vs prior $302.04 [3/27]; a -76% move in 5mo is implausible without a corporate action — likely a reverse-split / split-adjusted-basis mismatch, NOT organic decline. Verify with OTTO / broker before citing. Do NOT trip threshold logic off this row until confirmed.
VX-OTTO-2.02	Ally Financial Stock	1-Bellwether	$43.97	-10%	-15%	-20%	GREEN	80%	2026-08-12	yfinance live	OTTO_INTEL.md	LIVE. $19B Carvana exposure (42% originations), NO RECOURSE. Q2 print landed 7/21 (CARL/OWNER context).
VX-OTTO-3.01	First Brands BDC Exposure	5-Shadow	$237M across 15 BDCs	BDC stress	Dividend cuts	NAV collapse	STALE	95%	2026-02-16	OTTO	OTTO_INTEL.md	OWNER-DEFERRED (OTTO/BROCK). $9.3B debt, $12M cash at bankruptcy. WALTER SIG-W-20260803-004: First Brands plan → cramdown branch operative on Class 7 general-unsecured rejection. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-16 (>60 days); status was ORANGE. A ORANGE read from 2026-02-16 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-16.01	Blue Owl Private Credit Gate	5-Shadow	11 FUNDS GATED (Apr 2)	First gate	Multiple gates	Sector contagion	STALE	95%	2026-04-03	Bloomberg/BROCK	ML-REG-070, ML-REG-134, FLOW-REG-17.01	OWNER-DEFERRED (BROCK). 🔴🔴 SECTOR-WIDE CONTAGION. 11 funds gated as of Apr; OWL vehicle state is BROCK-tracked, not from this file. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-04-03 (>60 days); status was RED. A RED read from 2026-04-03 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-16.02	WAL Hidden CRE Total (RETIRED)	2-Credit	RETIRED 2026-08-12	>$2.5B	>$3.0B	>$3.5B	RETIRED	—	2026-08-12	FFIEC CDR (recipe superseded)	ML-REG-071, ML-REG-072	RETIRED 2026-08-12: the Memo3+RCON6550 "$3.0B / +62% in 18mo / structural classification" formulation is CONTRADICTED at the FFIEC primary 2026-08-07 — WAL live MI3 21.20% Q2-26 (never ≥25% in 12 quarters, plateaued <24%). Successor = cohort re-run on a settled uniform basis (REGINALD-owed, Will-gated pending two rulings on WILL_QUEUE).
VX-REG-17.01	Medallia 1L Mark	5-Shadow	→ BROCK `VX-BRK-003` (CANONICAL): 49.5¢ [BCRED Q2 10-Q, 6/30/26, ON NON-ACCRUAL]	<90¢	<85¢	<80¢	RED	97%	2026-10-10	BXSL 10-K 2026-02-25	ML-REG-082	OWNER-DEFERRED (BROCK). 🔴 BELOW RED as of Feb read; cross-holder marks Apollo 77 / Blackstone 78 / Monroe 84 / Onex 81 / HPS 89. | 2026-10-10 (DAEDALUS wiring ⑰): ONE FIGURE, ONE LADDER = BROCK `VX-BRK-003`. The 78¢ [BXSL 10-K 2/25/26] in this row was a superseded Feb vintage; BROCK's row retains it as its comparison point. This row is a POINTER, not a second mark.
VX-REG-17.02	UBS Private Credit Default Scenario	5-Shadow	Base 5.8% / Stress 15%	>6%	>8%	>15%	STALE	75%	2026-02-27	UBS/BROCK 2026-02-27	ML-REG-084	OWNER-DEFERRED (BROCK). UBS bear case: 15% default if AI disrupts middle market. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-27 (>60 days); status was ORANGE. A ORANGE read from 2026-02-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-17.03	US Life Insurer Private Credit Concentration	5-Shadow	$2T total; Top-10=43%	>$500B concentrated	>$1T top-10	Systemic gate	STALE	90%	2026-02-27	BROCK 2026-02-27	ML-REG-085, ML-REG-091	OWNER-DEFERRED (BROCK). Security Benefit ~55%, Delaware Life ~45%, MassMutual ~35%, Athene/Apollo. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-27 (>60 days); status was ORANGE. A ORANGE read from 2026-02-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-17.04	BDC Credit Facility Collateral Quality	5-Shadow	Impaired (FSK/BXSL/OBDC NAVs overstated)	NAV discount >10%	>15%	>20% + gates	STALE	90%	2026-02-27	BROCK 2026-02-27	ML-REG-086	OWNER-DEFERRED (BROCK). KeyBanc/Truist/Synovus hold BDC fund finance; CFG $10-11B. 2-3 quarter transmission lag. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-02-27 (>60 days); status was ORANGE. A ORANGE read from 2026-02-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-18.01	BCRED Redemption Rate	5-Shadow	$6.7B gross Q1 (7.9% of NAV)	>5% NAV/quarter	>7% NAV	Hard gate	STALE	95%	2026-03-04	Reuters/CNBC Mar 3	ML-REG-096, VX-REG-16.01, FLOW-REG-17.01	OWNER-DEFERRED (BROCK). 🔴 NEAR-GATE at Feb read. BX lifted cap 5%→7%, injected $100M firm capital. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-04 (>60 days); status was RED. A RED read from 2026-03-04 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-18.02	HY OAS Spread	3-Systemic	315bps [FRED 10/8]; 309 [10/7]; 324 [10/1] = only print over 320 this leg	>300bps	>320bps	>400bps	🟡 YELLOW (>300) — `REG-T-03` (>320 ×3) **0-of-3** at the 10/8 cell (309 · 315 both ≤320); peak run 1 (10/1)	90%	2026-10-09	FRED BAMLH0A0HYM2 through 10/6 — own pull 2026-10-07 21:47 ET, cache-busted fredgraph CSV + ALFRED first-published (identical on every cell)	HENRY, LIQUID, FLOW-REG-17.01, VX-REG-18.04	2026-10-07: chain 302 [9/28] · 308 · 312 · **324 [10/1]** · 310 · 312 · 303 [10/6]. REG-T-03 GRADED on my letter: 10/1 = 1 of 3, reset 10/2, 0-of-3 through 10/6, NOT FIRED. 17bp under 320 at 10/6; 43bp above the <260 REVIEW line. LIQUID: one tagged print; funding not confirming (SRF $0, SOFR-IORB -3bp [10/1]). X1 CLOSED (LIQUID). Run the bank-credit cross-check before reading any level as bank transmission | 2026-09-26: 280 [9/24] (268 [9/22] · 273 [9/23]); 40bp under the >320 Orange line, 20bp above the <260 REVIEW trigger — moved AWAY from review for the first time this month. At LIQUID's X1 line (>280 strict), not over; X1 CLOSED 8/28 (LIQUID's). | LIVE. LIQUID-canonical series — reference, don't fork. Path since last refresh: 268 [9/7] -> 267 [9/8] -> 271 [9/9] -> 270 [9/10] -> 265 [9/11]. **55bps of buffer to the >320 Orange line; 5bps above the <260 REVIEW trigger — the closest approach of the cycle, moving TOWARD it.** ⚠️ DO NOT READ 265 AS CALM: the index tightened on the BB bucket (150, -5bp) while the CCC tail WIDENED (+6bp) — see VX-REG-18.04. Dispersion inside a tightening headline. ⚠️ RED's FT-12 (HY <260 STRICT, sustain 3, IMMEDIATE-FALSIFY) is 5bp away; RED ruled PRE-DATA that the letter stands and fires as written, composition disagreement pre-registered rather than the threshold re-cut. | PRIOR (8/20, superseded): LIVE. LIQUID-canonical series — reference, don't fork. Path since last refresh: 271 [8/12] → 271 [8/13] → 267 [8/14, the low] → 270 [8/17] → 275 [8/18] → 273 [8/19]. **47bps of buffer to the >320 Orange line; 13bps above the <260 review trigger.** Level unremarkable and RANGE-BOUND — no trend. ⚠️ **Anchor-drift caveat STANDS [SIG-723-002]: REG-T-03/04 are NOMINAL and HY composition has improved (CCC 10% vs 16% at calibration), so the same print carries MORE stress than the level implies.** Thresholds NOT moved. ⚠️ **And the 7/30 BANK-ABSENT attribution is the governing read: a wide HY print is not self-evidently bank transmission — run the bank-credit cross-check first** (`reports/2026-07-30_bank-side-HY-attribution.md`). **Confirmed again 8/20 in the INVERSE direction: banks fell −4.8% mean over 8/14→8/20 while HYG/JNK/LQD/BKLN moved −0.18/−0.18/−0.07/+0.07% — credit priced ZERO incremental bank risk.**
VX-REG-18.03	Unrealized HTM Losses	4-Funding	$306.1B (Q4 2025, -$31B QoQ)	>$350B	>$400B	>$500B	STALE	85%	2026-03-27	FDIC QBP Q4 2025	ML-REG-016	REFRESH-OWED (FDIC QBP Q1 2026). Q4 read: $306.1B, lowest since Q1 2022. BUT: 10Y now 4.67% (vs 4.10% in Mar) → Q1 will likely REVERSE the improvement. AOCI reinclusion makes this a capital event for Cat III/IV banks. | STALE 2026-10-10 (item 3, Will go-ahead): Last_Updated 2026-03-27 (>60 days); status was ORANGE. A ORANGE read from 2026-03-27 is NOT a current read. Refresh or retire at the next touch (charter Stale Data Rules: skip STALE rows).
VX-REG-15.04	Brent Crude Price	3-Systemic	$88.63 [8/12]	>$100	>$130	>$150	YELLOW	95%	2026-08-12	market.py live (BZ=F)	FL-REG-HOA, VX-REG-HOA	LIVE. $88.63 [8/12] — sits BELOW the >$100 yellow threshold; regime is "elevated but not stress" (was $87.67 [7/17], tagged $100.69 [7/23], now backed off). HAWK/BRENT own the oil verdict.
VX-REG-15.02	10Y UST Yield	3-Systemic	4.67% [FRED 8/10]	>4.25%	>4.50%	>4.75%	ORANGE	90%	2026-08-12	FRED DGS10 / market.py	VX-REG-9.01, VX-REG-6.04	LIVE. 4.67% [FRED 8/10] / 4.72% [8/10 close] — durable ABOVE the 4.50% orange threshold, approaching 4.75% RED. HTM losses widening; CRE refi wall cannot clear; term-premium-driven per 7/30 attribution memo.
VX-REG-15.03	FL Energy Cost Shock	7-Regional	ELEVATED — regime softening (Brent $88.63 [8/12], below the $100 line)	Qualitative	Qualitative	Qualitative	YELLOW	85%	2026-08-12	Reuters/CNBC derived	VX-REG-8.01, CORAL	LIVE. Downgraded ORANGE→YELLOW: Brent $88.63 [8/12] sits below the $100 yellow line; late-July $100.69 tag has unwound. FL pipeline/LNG structural exposure unchanged. CORAL/BRENT own detail.
VX-REG-19.01	iTraxx Senior Financial	3-Systemic	~95bps (Mar 4 2026)	>85bps	>100bps	>130bps	STALE	80%	2026-03-05	HANS via HERMES 2026-03-04	ML-REG-111	OWNER-DEFERRED (LIQUID/HANS). Named as the European bank-CDS index in the STATUS 7/30 gap-disclosure amendment. Ask LIQUID for a fresh mark.
VX-REG-19.02	FL UI Exhaustion Cliff Date	7-Regional	Mar 24 onset / Apr 26 peak	Mar 24 first cliff	Apr 26 peak	Sustained post-Apr	RESOLVED-UNVERIFIED	90%	2026-07-17	CARL via HERMES 2026-03-04; ML-CARL-LABOR-003	ML-REG-110	RESOLVED-UNVERIFIED. Cliff dates passed ~4mo ago with no bank-transmission event surfaced Mar-Aug.
VX-REG-18.04	CCC/HY Bifurcation Ratio	3-Systemic	3.975x [CCC 1252 / HY 315, FRED 10/8]; 3.977x [10/7]; CCC 1252 = new FRED-window high	>3.6x (1 close ARMED)	>3.6x (2 consec)	>3.6x (3 consec HARD FIRE)	🔴 HARD-FIRE (re-arm ESC MET 9/24, escalated 9/26; NOT re-escalated — the 10/2-10/6 rise is HY-tightening-led, NO escalate by this vector's own rule)	85%	2026-10-09	FRED BAMLH0A3HYC / BAMLH0A0HYM2 / BAMLH0A2HYB / BAMLH0A1HYBB through 10/6 — own pull 2026-10-07 (CSV + ALFRED agree)	VX-REG-18.02, RED-FT-07, LIQUID/BROCK	2026-10-07: ratio 3.795 [9/28] · 3.756 [9/29] · 3.779 [9/30] · 3.750 [10/1] · 3.877 [10/2] · 3.881 [10/5] · 4.007 [10/6]. CCC 1,146 -> 1,157 -> 1,179 -> **1,215 [10/1] = FRED-window high** -> 1,202 -> 1,211 -> 1,214. Every tier widened 9/28->10/1, then HY/B/BB retraced while CCC did not. BROCK 10/2: CCC/BB compressed 6.780->6.077 on its basis, tail not leading; no BROCK row moves. Escalation already sent 9/26; Will 9/26: re-entry is LIQUID's | 2026-09-29: CCC 1112 [9/24] -> 1128 [9/25] -> 1146 [9/28] = highest in FRED's public window (exceeds the 1137 [2025-04-07] I cited as series max); HY 280 -> 293 -> 302. Ratio 3.971 -> 3.849 -> 3.795. Escalation already SENT 9/26 on the re-arm; NOT re-escalated (Will 9/26: re-entry is LIQUID's). LIQUID grades the widening broad/BB-led (c637aa7a2); my tier test agrees (B 309, BB 183) | ★ 2026-09-26 — RE-ARM MET, ROUTED. The 8/13 re-arm `CCC >=1050 AND HY >=272 on 2 consecutive closes` is satisfied on 9/23 (CCC 1093 / HY 273) and 9/24 (1112 / 280). Per its own text the escalation packet goes out carrying both baselines and leading with the CCC LEVEL: CCC 970 [7/16] and 1034 [7/31 run start] -> 1112 [9/24] = +142bp / +78bp; 1112 = 2026 high, 25bp under the series max 1137 [2025-04-07]. HY 271 [7/16] / 285 [7/31] -> 280. TIER TEST CHANGED: 9/22->9/24 B 271->286 (+15), BB 156->164 (+8), CCC 1075->1112 (+37) — the first two-session widening in this run that reaches B; B still under its 2026 mean 305 and the VX-REG-18.05 >300 band => migration STARTED, not established. The ratio FELL 4.011->3.971 because the denominator widened — do not quote the ratio slope. Leg (b) HY>=272 BOUND this time (it filtered nothing in the 533-session base sample): the re-arm waited on HY, not CCC, for ~3 weeks. Base rate of the adopted re-arm 8/532 = 1.5%. Scope: this executes the re-arm registered INSIDE Will's 8/13 stand-down; it does not lift the stand-down, touch X1 DON'T-SIZE (LIQUID, decided 8/28), or reopen WQ-251 (withdrawn by Will 9/26: re-entry only through LIQUID's work). 9/25 not yet on FRED. | ★ 2026-09-14 (2nd pass, WILL-PROMPTED) — TIER DECOMPOSITION RUN, AND IT MODERATES THE ALARM I RAISED THIS MORNING. The question the inversion could not answer on its own: is CCC widening because a credit cycle is migrating DOWN the ratings stack, or because the distressed bucket alone is deteriorating? Pulled all three tiers 8/26->9/11: BB 156->150 (TIGHTENED 6bp) · B 282->273 (TIGHTENED 9bp) · CCC 1031->1076 (WIDENED 45bp). *** EVERYTHING ABOVE CCC IMPROVED. The widening is CONFINED TO THE BOTTOM TIER = tail-concentrated, NOT a migrating credit cycle. *** Consistent with named idiosyncratic blowups in hand this week (Loparex marked to 6.2c, First Brands Ch.7, Tricolor) rather than a cycle. B tier at 273bp is the 1st PERCENTILE OF 2026 and ~7th of the available series -- i.e. the middle of HY is at its CALMEST of the year while the tail widens. => FOR MY DESK THIS IS THE LEAST BANK-TRANSMISSIVE FORM OF CREDIT STRESS: banks do not hold CCC corporate paper in size; their exposure is LENDING TO THE HOLDERS (NDFI/fund finance), which is second-order and slow, and V3 read 11-for-11 NO reserve build in Q2. *** THE TELL TO WATCH IS THE B TIER, NOT CCC: B widening = distress MIGRATING rather than concentrating, and that is the form that reaches banks. Registered as VX-REG-18.05. *** REVISED RECOMMENDATION ON THE 8/13 STAND-DOWN: its STATED REASON is still dead (CCC is not flat), but the CONCLUSION it supported survives on a BETTER reason -- re-base the stand-down on the tier test rather than lift it. | ★ 2026-09-14 — THE ATTRIBUTION FLIPPED AND THIS ROW'S PRIOR READ IS NOW WRONG AS WRITTEN. Since 8/13 this row said: "CCC is FLAT across the whole run (1034->1031, -3bp); the entire ratio rise is HY tightening; denominator artifact => NO escalate" — and Will's 8/13 escalation stand-down rested on exactly that ground. CCC IS NO LONGER FLAT: 1,031 [8/26] -> 1,076 [9/11], +45bp, MONOTONICALLY RISING FIVE SESSIONS (1,055 · 1,056 · 1,064 · 1,070 · 1,076). DECOMPOSITION 8/26->9/11: total ratio move +0.199, of which CCC contributes +0.169 (~85%) and HY +0.030 (~15%). The denominator-artifact explanation INVERTS. PROME independently reproduced the decomposition to the digit (85.2%/14.8%) and registered it WQ-251. ⛔ NOT ESCALATED AND THE STAND-DOWN IS NOT SELF-LIFTED: the re-arm condition is `CCC >=1050 AND HY >=272 x2` — CCC leg MET (>=1050 since ~9/2), HY leg 7bp SHORT (265 vs 272). THE CONDITION GOVERNS THE FIRE; what changed is the GROUND of the stand-down, and that is a decision for Will, reported not acted on. Companion: CCC-BB 926bp [9/11], a fresh high (915 [9/10]) — on the 9/10->9/11 session the index TIGHTENED 5bp while the CCC tail WIDENED 6bp and BB tightened 5bp = dispersion inside a tightening headline. ⚠️ REFERENCE FRAME so 1,076 is not over-read: SERIES max 1,137 [2025-04-07]; 1,076 is a 2026 high, ~5% below the series high. Routed to LIQUID + BROCK (they own the tail). ★ THE GENERALISABLE LESSON: this row re-checked its LEVEL every session for a month and NEVER re-tested the PREMISE under its verdict. A carried interpretation has no expiry check. [[finding_dated_carry_item_has_no_expiry_check]] | PRIOR (8/27, superseded): ★ RE-COUNTED AT THE SERIES 2026-08-27 (not incremented from memory): **19 consecutive sessions >3.6x, 7/31 → 8/26, UNBROKEN**, and the run made a **NEW HIGH 3.861 [8/26]** past the prior 3.790 [8/14]. ⛔ **AND THE DECOMPOSITION SAYS BENIGN, now unambiguously: across the ENTIRE run CCC went 1034 [7/31] → 1031 [8/26] = −3bp, FLAT, while HY went 285 → 267 = −18bp. The whole 3.628 → 3.861 rise is the DENOMINATOR.** Per this vector's OWN escalation clause (HY-tightening-led = beta/benign = NO escalate; CCC-widening substance required) this is a denominator artifact — the same shape adjudicated at the 7/13 fire. ⚠️ **Re-arm `CCC >=1050 AND HY >=272 x2 consec` NOT MET and BOTH legs now fail** — CCC peaked 1039 [8/25], 11bp short; HY has been below 272 for four straight sessions. ⚠️ **2026-max superlative corrected: CCC 1039 [8/25] is the 2026 high** (verified over 172 2026 observations), superseding the 1034 [7/31] this desk carried — which BOND had ALREADY retracted on 8/21 (`KB-BND-155`, 1035 [8/20]); **I carried a peer's retracted figure for 6 days, same class as the HOMER retraction fixed the same session.** BOND is current and AHEAD of me (`KB-BND-176`, 8/27) — **verified before packeting, and no packet sent, because telling an owner its own figure is noise.** ⚠️ **Lagged-series class ruling (Will 8/27) applies to this row: count DATED observations, never 'latest available' — the 8/26 observation published 8/27, which is what licenses counting it today.** *(Prior: run re-counted at primary 2026-08-20 at 14 sessions, 7/31 → 8/19; was 8 at the 8/13 count.)* (Was 8 sessions at the 8/13 count; +6 since.) Ratio path 8/12→8/19: 3.764 / 3.779 / 3.790 [8/14, the run HIGH] / 3.770 / 3.735 / 3.773. ⚠️ **RE-ARM `VX-REG-18.04-ESC` NOT MET, and only ONE leg is why:** spec = **CCC ≥1050 AND HY ≥272 on 2 consecutive closes**. **HY leg IS met** (275 [8/18], 273 [8/19] — 2 consec ≥272). **CCC leg is NOT: max 1030 [8/19], 20bp short of 1050.** So the compound gate is holding on the leg that was disclosed at design time as the BINDING one — working as specified. ⚠️ **CORRECTION TO MY OWN 8/13 NOTE: CCC 1030 is NOT the widest of the window.** CCC printed **1034 on 7/31** — higher. The 8/13 row said '1023 widest of window'; that was wrong then on the same series and is wrong now. **CCC is NEAR its window high, not at it.** ★ **CONVERGENT CATCH, INDEPENDENTLY — BOND retracted the same label the same day** (`KB-BND-152`, 8/20: *'CCC 1030bp [8/19] is a fresh AUGUST high, NOT a series high and NOT a 2026 high'*), and PROME corrected HEARTBEAT in place (`3c0add453`). **BOND's reference frame, adopted: 2026 max 1034 [7/31] · SERIES max 1137 [2025-04-07].** ⇒ **1030 is ~9% below the series high and below the 2026 high — it is an AUGUST high and nothing more.** Carrying the reference so the level cannot be re-inflated by a future reader `[[finding_level_without_a_reference_has_two_failure_modes]]`. `[[finding_exact_level_authenticates_a_wrong_direction]]`. ⚠️ **The ratio is NOT making new highs: 3.790 [8/14] is the run peak and the last three closes are below it.** TERRY independently flagged the ratio as falling into the 8/14→8/20 bank selloff — **it fell then ticked back up; the direction claim needs the 8/19 print to be honest, and the substance survives: the junk tier is NOT deepening while banks sell off.** ★ **This is now a 4th independent leg of the same 8/20 finding: the bank move has no credit confirmation on ANY instrument** (HY level, CCC/HY ratio, HYG/JNK/LQD/BKLN tape). PRIOR NOTE PRESERVED: ⚠️ **3RD HARD-FIRE — DATES CORRECTED 2026-08-13** (superseded text preserved: *"3RD HARD-FIRE 2026-08-07..08-11: 3 consec closes >3.6x (8/7 3.752 / 8/10 3.756 / 8/11 3.761) … the boot.py counter would have caught this at 8/9 close, 3 days sooner"*). **CORRECT: run began 7/31 and is UNBROKEN — 7/31 3.628 / 8/03 3.698 / 8/04 3.733 / 8/05 3.720 / 8/06 3.753 / 8/07 3.752 / 8/10 3.756 / 8/11 3.761 = 8 sessions, all strictly >3.6. Hard-fire criterion (3 consec) MET 2026-08-04, NOT 8/7** — the old label reported the LAST three closes of the run instead of the FIRST three. Found by NEXUS 8/12 (packet), verified by REGINALD at FRED 8/13. **So the late-catch is 8 days, not 3** (criterion 8/04, caught 8/12; a boot counter would have caught 8/05). ⚠️ **DRIVER-DECOMP IS BASELINE-SENSITIVE — carry both:** on the 7/16 baseline (CCC 970 / HY 271 / 3.579) CCC +53bp (+5.5%) vs HY +1bp (+0.4%) → **CCC-wide ⛔ **DEFINITIONAL SOURCE — DO NOT ARCHIVE: `research/CCC_HY_TRIPWIRE_2026-06-25.md`** holds this vector's FULL definition (3-consec >3.6x fire rule, the CCC-led=substance / HY-led=beta driver-decomposition, band derivation). This row carries the BANDS and STATE; the file carries the RULE that decides escalate-vs-stand-down — the 8/13 and 8/27 stand-downs both turned on it. It came up retirement-eligible 8/27 (>60d, not boot-read, referenced only by the research INDEX, which does not count) and was archived and REVERSED the same pass. This pointer exists so a live doc names it and the >60d rule cannot reach it again. `[[finding_retired_threshold_has_no_publisher]]`
VX-REG-18.05	B-Tier OAS (HY migration tell)	3-Systemic	B 315bps [FRED 10/8]; 308 [10/7]; peak 329 [10/1]; ORANGE 330 not reached	>300bps	>330bps	>380bps	🟡 YELLOW (>300) — held >300 for 7 prints 9/28-10/6; ORANGE >330 NOT reached (329 [10/1] = 1bp short)	85%	2026-10-09	FRED BAMLH0A2HYB through 10/6 — own pull 2026-10-07	VX-REG-18.04, VX-REG-18.02, BROCK, LIQUID, SAM	★ 2026-10-07: 309 [9/28] · 316 · 316 · **329 [10/1]** · 312 · 314 · 302 [10/6]. The 9/29 question (hold >300 into >330, or reverse like 9/15?) answers: HELD >300 seven prints, touched 329, did NOT reach 330, and is back at 302 - the migrating form persisted but did not escalate. BB 185 [10/6] (peak 204 [10/1]). Watch, not a trigger (base rate still owed) | ★ 2026-09-29: FIRST >300 print (309 [9/28]). The 9/26 question (does B hold >=285 and reach >300, or reverse like 9/15?) answers REACHED. BB 183 [9/28] also widening (164 -> 176 -> 183). This is the migrating form, not the concentrating tail — the one that can reach my banks via fund-finance/NDFI — but bank credit instruments cannot see it before the Q3 prints. ORANGE >330 next. No routing from this row (watch); LIQUID owns the HY grade | 2026-09-26: 286 [9/24], up from 271 [9/22] and 273 [9/11]. First two-session widening WITH CCC since this row was registered 9/14; BB 164 also widened. Still under the 2026 mean 305 and the >300 band; 9/15 printed 285 and reversed, so one more print is needed before calling it migration. Watch, not a trigger (base rate still owed). | NEW 2026-09-14, Will-prompted. *** PURPOSE: this row exists because CCC alone cannot distinguish a MIGRATING credit cycle from a CONCENTRATING tail, and only the migrating form reaches my banks. *** B is the middle of HY. CCC widening with B TIGHTENING = idiosyncratic blowups in the distressed bucket (current state). CCC widening WITH B widening = distress moving UP the stack toward the paper that actually sits behind bank NDFI/fund-finance lending. Current: 273bp, the 1st percentile of 2026 (YTD range 272-377, mean 305) and ~7th of the series -- the calmest of the year, i.e. the migration signal is ABSENT, not merely weak. Bands are set off the 2026 distribution, deliberately coarse and NOT a trigger: >300 = above the 2026 mean; >330 = upper quartile; >380 = above the 2026 max. *** BASE-RATE BEFORE PROMOTING THIS TO A REGISTERED TRIGGER -- "do not build it" is a real answer and this row is a WATCH, not a tripwire. *** CAVEAT ON THE PERCENTILES: the series I can pull starts 2023-09-15, so the reference frame contains no 2020 and no 2008 -- percentiles are within a BENIGN-REGIME sample and understate how tight 273 really is historically. CAVEAT ON VINTAGE: FRED is T+1, so the freshest possible cell during a trading day is the prior close; 9/11 is Friday and 9/14 does not post until 9/15.
````

## research/FHLB/README.md

crc32 3c22885b; bytes 8306

````text
# FHLB research hub (REGINALD)

*Built 2026-10-10 (Sat ~20:3x ET) on Will's direction: "consolidate it all into one centralized area. Even if we just copy the data/files over there." Owner: REGINALD. **Re-check this map at any append, or on 2026-11-07 (the Q3 Call Report run), whichever is first.***

**Start here.** Everything the fleet has on the Federal Home Loan Banks (FHLBs) is either IN this folder or listed below with its path. Two kinds of file live here:

- **Canonical (edit here):** `reports/`, `verification/`, `data/KEY_PRIMARY_TABLES.md`, `sources/SOURCES.md`, this README.
- **Copies (never edit here):** `copies/` and `data/DESK_ROWS_SNAPSHOT_2026-10-10.md`. Each copy opens with a 2-line banner naming its source path, commit and crc32; `copies/MANIFEST.tsv` lists all 25. Their figures are as of each source's own date. To refresh a copy, re-copy the source; to fix a figure, fix the SOURCE.

## The questions

| # | Question | Where it stands (2026-10-10; re-check) | Read |
|---|---|---|---|
| Q1 | **Is FHLB borrowing a sign of regional-bank stress?** (`REG-T-06`: advances >$700B ×3 quarters = "EARLY-CRISIS") | **No, as currently measured.** The H1-2026 rise (+$136.2B) was commercial banks (+$121.4B), about half of it four very large banks; credit unions and savings institutions shrank (−$13.7B); 106 mid/small SEC filers +$2.3B. Q3 likely FELL (nowcast ≈ $770B). As lettered the alarm fires ~10/29 anyway → **WQ-414 (Will, due 10/24).** | `reports/…_Q2_composition…` · `reports/…_Q3_nowcast…` · `verification/…` §Key primary figure |
| Q2 | **What is inside the total?** | By borrower type at 6/30/26: commercial banks 56.4% · insurers 24.9% · credit unions 9.1% · savings institutions 8.2%. Insurer dollars are a record ($202.8B) but their share fell from 27.0% at Q1. | `verification/…` · `data/KEY_PRIMARY_TABLES.md` |
| Q3 | **The insurer channel (Athene, Delaware Life) and its bank links** | Real, owned by **SHADE** (insurers) / **BROCK** (private credit). Losses in an insurer failure land mainly on policyholders and guaranty funds; the FHLB's protection there rests on **state** law and holding the collateral, not the federal §10(e) lien. Bank links are small and named: Citizens $450M revolver to Delaware Life (status after YE2025 unknown) · Truist and Fifth Third paused Delaware Life sales · WAL = 13% of FHLB San Francisco's book (YE2025). | `verification/…` ledgers B and C · `data/KEY_PRIMARY_TABLES.md` |
| Q4 | **Is the 2023 lifeline tighter for a weak bank?** | **Unknown (inference only).** FHFA AB 2024-03 (active) tells FHLBanks to lend on the member's condition, not just collateral; the FHLBanks' own Council calls it "procyclical". **No public evidence** of an actual pullback; FHFA-OIG calls member credit risk "abated" for FY2026. | `verification/…` ledger C (R1–R3) |
| Q5 | **Where did September's small-bank borrowing come from?** | Small banks' borrowings +$32.9B in 3 weeks to 9/30 (H.8), but FHLB system debt rose only +$6.2B in September ⇒ mostly NOT FHLB, or FHLB-funded from its own liquidity. Open. | `reports/…_Q3_nowcast…` §4 · STATUS H.8 row |

## Folder map

| Path | What |
|---|---|
| `reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` | **Canonical.** Who borrowed in H1 (district XBRL, named members, borrower-side breadth), the 2020–26 base rate of the >$700B letter. *Moved here 2026-10-10; a forwarding stub sits at the old `AGENTS/REGINALD/reports/` path.* |
| `reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md` | **Canonical.** Q3 advances nowcast from Office of Finance debt (≈ $770B, ±2 sd $728–813B), H.8 vs FHLB gap. *Moved; stub at old path.* |
| `verification/2026-10-10_external_report_verification.md` | Claim-by-claim check of Will's external draft: bottom line + three ledgers (EDGAR, Delaware Life, regulatory/system). |
| `data/KEY_PRIMARY_TABLES.md` | District top-borrower tables (Des Moines, Indianapolis, San Francisco, Chicago), Athene and Delaware Life borrowing room. |
| `data/DESK_ROWS_SNAPSHOT_2026-10-10.md` | COPY: every FHLB row in THRESHOLDS · VX · KB · FLOW · PREDICTIONS · registry NOTES, verbatim, with re-extract commands. |
| `sources/SOURCES.md` | Every primary document: URL or SEC accession, date, local file. |
| `sources/*.pdf` | 17 PDFs (Office of Finance CFRs, GAO, FHFA, FHFA-OIG, Council letter, Iowa code). **Local-only (gitignored here)**; re-download on another machine from SOURCES.md. |
| `sources/FHLB_Risk_Research_Report_Reconciled.docx` (+ `_TEXT.md`) | Will's external draft. **A lead list, not a source** (see verification). |
| `copies/REGINALD/` | 14 copies of desk material: Feb-2026 haircut research and monitoring design, Feb readings, CFG Q1 "FHLB flipped", the frozen FHLB-dependency scoring proposal, the PNC/Pittsburgh attribution (8/23), the WQ-318 per-bank funding baseline + script, BOND's two FHLB packets, my WQ-414 packets to PROME, my 10/10 signal + amendment. |
| `copies/fleet/` | 11 copies from other desks: OTTO (WAL FHLB & liquidity) · OZK (pledged loans) · SHADE (Athene funding mix; BROCK→SHADE Delaware Life packet) · BROCK→HAWK (5/1) · BOND (rotated catalyst rows) · FORGE (PE-insurer cascade, frozen corpus; T-bill/repo) · RED (KRE bull case) · WAL (stale earnings prep) · CORAL (Seacoast funding). |
| `copies/MANIFEST.tsv` | Source path, commit, crc32, bytes and a one-line note per copy. |

## Live surfaces that stay where they are (tools and boot checks read them there)

| Surface | Holds |
|---|---|
| `STATUS.md` §THRESHOLD STATUS: FHLB row, small-bank borrowings row | **the live level** (one source of truth; never restate it here) |
| `registry/THRESHOLDS.tsv` `REG-T-06`, `REG-T-08` · `registry/NOTES.md` | the alarm letters |
| `workbook/VX.tsv` `VX-REG-7.01` (live) · `7.02` / `7.03` (**STALE since 2026-02**) | tracking vectors |
| `workbook/KB.tsv` (17 FHLB rows, ML-REG-009 … 186) | knowledge base |
| `CALENDAR.md` (~10/29 Q3 figure row; weekly funding row) · `ROADMAP.md` (`REG-T-06` thread) | dates and threads |

## Next dates

| Date | What |
|---|---|
| Thu 10/15 · Fri 10/16 | Fed H.4.1 (discount window) · H.8 (small-bank borrowings, week of 10/7): Q5 |
| **Sat 10/24** | **WQ-414 due: Will re-letters `REG-T-06` or not** |
| ~Thu 10/29 (estimate) | Office of Finance Q3 combined advances; grade against the ≈ $770B nowcast (a miss >$40B ⇒ check FHLBank liquidity drawdown) |
| early–mid Nov | FHLBank Q3 10-Qs (top-borrower tables); Athene Q3 10-Q; OF monthly debt file for October |
| 2026-11-05 · 11-07 | FFIEC token expiry (Will) · Q3 Call Report run (per-bank FHLB advances) |

## Known bad figures in older material (do not cite)

- **"FHLB at $480B" (Feb–Apr 2026)**, in `copies/fleet/RED__KRE_BULL_CASE.md` (Pillar 10) and this desk's April WALTER liaison notes. The Office of Finance shows **$694.0B at 3/31/25 and $676.7B at 12/31/25**. The $480B basis is unknown. RED owns its file.
- **The external draft's** San Francisco JPMorgan >10% claim (that was YE2024), "$14.7B credit unions" (matches MBS investments), the Council of FHLBanks quote (fabricated), "Indianapolis most insurer-heavy" (Des Moines is), insurer membership 7.7% (9.7–9.9%), commercial-bank share ~48% (56.4%). Detail → `verification/`.
- `VX-REG-7.02` haircuts and `7.03` pledging: STALE since 2026-02; haircut schedules are not public.

## Not copied: incidental mentions

On 2026-10-10, **138 files in this desk** and **340 elsewhere in the fleet** (excluding `AGENTS/_archive/`) mention the FHLB. Most are one-line references inside bank notes, status rotations or routing logs; they were indexed by command, not copied. List them with (from the repo root):

```
grep -rli 'FHLB\|Federal Home Loan' --include=*.md --include=*.tsv --include=*.py AGENTS PROME FORGE | grep -v 'AGENTS/REGINALD/research/FHLB/'
```

Copy any of them in on request; add a row to `copies/MANIFEST.tsv` with the same banner format.

## Who owns what next door

SHADE: insurer lenders (Athene, Delaware Life; `T-SHADE-01`) · BROCK: private credit and the APO Dec-18 $95P vehicle question · LIQUID: funding plumbing (SOFR−IORB, discount window) · BOND: the curve; its FHLB vectors were shelved 8/18 · WAL / OZK / FLG desks: each bank's own FHLB use.
````

## NEXUS_BRIEF.md

crc32 3bef4889; bytes 24405

````text
# REGINALD — NEXUS Brief

**Status:** 🔴 on the LEVEL and 🔴 on the MACRO INPUT, 🟠 on the MECHANISM. **`REG-T-02` FIRED since 2026-09-01 (cycle 2), still FIRED through the 10/9 close:** 28 closes graded, none qualifying, run **`0-of-3`**; latest **WAL $74.27 [10/9 settled, two routes]** (exit ≥81.90 ×3; count lives in `registry/REG_T02_EXIT_LOG.tsv`). **`REG-T-03` (HY >320 ×3) 0-of-3** at the 10/8 cell — 309 [10/7], 315 [10/8]; 324 [10/1] was one print. CCC 1,252 [10/8] = FRED-window high. **FLG ladder `VX-REG-6.03` RED** since the 10/7 close $11.30; 3 settled closes below RED through 10/9 ($11.32). Matrix unchanged. **Nano Banc (10/9):** FDIC bid summary posted 10/8 (P&A not yet) — Sunwest bought Pools B/C at 82.30%/80.17% of book, 0.85% deposit premium, no loss-share; shared figure ≈$120M ≈17% [9/22] unchanged, retained-pool allocation ≈32–42% (desk scenario) → `reports/2026-10-09_nano-banc-bid-summary-and-section3-rerun.md`.

**WAL quarantine (cutover 7/25):** WAL thesis/predictions/positions are **`../WAL/`-owned — no WAL figure is restated here**; read `../WAL/STATUS.md`. REGINALD keeps the matrix row + cohort context. New via WAL 8/7 (consume-with-fences): **the V1a MI3 falsifier finally RAN and came back PLATEAUED <24%**, and WAL's NDFI share made a new high — **both under WAL's explicit "weights UNCHANGED pending Will's rulings" fence; do not consume WAL's scores as settled.**

**Domain:** Regional banks (watchlist + KRE) — convergence terminus for CRE, NDFI, private-credit, labor, stagflation channels; peer coordination with CREED/BROCK/CORAL/OZK/WAL (all top-level).

> **★ TRANSFERABLE DISCRIMINATOR (EGBN grade — the one other desks should take):** **coverage thinning has TWO causes with OPPOSITE meanings** — ACL failing to keep pace with *incoming* problem credits (bear, under-provisioning) vs ACL *consumed by outgoing realized losses* (de-risking). Same arithmetic, opposite conclusion. Companion adopted 8/10 (HOMER's version for delinquency rates): **when a DQ headline improves, check the provision line in the same filing** — Fannie MF SDQ "improved" to 0.60% via modification while its MF provision rose +49% QoQ.

**As of:** **2026-10-10 (Sat ~20:4x ET closeout: external FHLB draft checked · FHLB hub · RED, Opus 5.5) · STATUS pin `4a2d5a0f0`.** **Everything FHLB → `research/FHLB/` (README first).** The external FHLB draft Will brought is a lead list, not a source (fabricated Council quote; GAO and Delaware Life findings reversed). Bank links found: Citizens $450M revolver to Delaware Life (undrawn YE25) · WAL = 13% of FHLB SF advances [YE25]. Earlier 10/10 (nowcast ≈ $770B, failures, BaaS): pre-fold brief. View unchanged: CONCENTRATED; CFG Fri 10/16 first. *Pre-fold brief → git `1ccd3353a`.*

## VIEW

- **★ FHLB + WEEKLY FUNDING (10/10 PM) — what other desks should take:**
  - (1) **The Q2 FHLB build is a big-bank story:** by borrower type (OF Q2 CFR Table 3) commercial banks +$121.4B, insurers +$25.0B (share 27.0 → 24.9%), credit unions + savings institutions −$13.7B; about half of H1's +$136.2B (par) is PNC +27.4 · Citi +20.0 · USB +14.0 · WFC +6.0; three districts (Pittsburgh, NY, Cincinnati) are 73.5%. 106 mid/small SEC-filing borrowers added +$2.3B in total (median 0%). Atlanta +6.9%; SF −10.6%. **Why:** Citi says growth funding in its own 10-Q; USB borrowed and held cash (INFERENCE); WFC is growth; **only PNC replaced deposits that left** (credit clean).
  - (2) **`REG-T-06` (>$700B ×3 quarters ⇒ EARLY-CRISIS) does not discriminate:** the system was >$700B in 12 of 26 quarters since 2020, and as lettered it fires mid-2023 and never exits. Re-letter question with Will (via PROME, WQ-414, due 10/24) before the ~10/29 Q3 figure. **Don't read a Q3 fire as crisis without the composition.** ★ **Q3 nowcast (10/10 late PM):** FHLB Office of Finance debt $1,330.8B [6/30] → $1,288.8B [9/30] (−$42.1B); quarterly fit on 25 quarters (corr 0.98) ⇒ **Q3 advances ≈ $770B (±2 sd $728–813B)**, so it very likely fires **while FHLB lending shrank ~5%**. In-sample fit, preliminary data; an FHLBank liquidity drawdown is the named way it breaks. → `research/FHLB/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`.
  - (3) **Weekly H.8 to 9/30:** smaller banks' borrowings (FHLB + other) **+$32.9B / +11.7% in 3 weeks, the largest rise in 160 weeks** (⚠️ that window starts AFTER SVB, whose first week was **+$290B in one week**, ~9× this; month-end Sep +5.9% NSA; large banks +0.9%), not a quarter-end pattern; **FHLB system debt rose only +$6.2B in Sep vs banks' H.8 borrowings +$54.5B** (repo/fed funds, FHLB liquidity drawdown, or large members paying down: not separable yet); deposits flat; discount window above its 60-week p90 for two weeks ($9.97B [10/7]). Credit-side bars quiet (non-bank lending growing, no line draws). **Read: banks lining up cash, not credit transmission (INFERENCE; no bank named; FHLB share unknown; the cash leg holds on SA but not NSA).** Next H.8 Fri 10/16. → `research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`.
- **★ Q3 READ PLAN (10/9) — what other desks should take:**
  - (1) **Individual ≠ spread.** Worse numbers at FLG/EGBN/OZK/AMTB are severity at named banks. A spread needs L180 (≥3 of 5 mid-pack, total-CRE bad-loan RATE on the Call Report basis: nonaccrual + 90+ over construction + MF + NOO, or a foreclosure build) or the FL-rail aggregate.
  - (2) **Keep total CRE and multifamily apart.** At 6/30 total CRE was 2.23% (2.46% a year earlier). Multifamily was 3.58%, down year on year but **up from 3.23% in Q2, all at FLG/EGBN/CFG**; mid-pack multifamily was flat or falling.
  - (3) **Release figures are provisional;** a bank missing at the 11/07 retrieval makes a breadth verdict UNKNOWN wherever it could flip it.
  - (4) **Dry run Q1→Q2:** *c* = 1, WAL on a literal foreclosure-build limb (+2.3%; that limb is unquantified).
- **★ WQ-318 FUNDING vs NON-BANK EXPOSURE (10/7) — what other desks should take:** (1) **at 6/30 no cheap-deposit flight at any of six banks** — NIB share flat (within 0.5pp) or up YoY; interest-bearing deposit cost −27 to −52bp over four quarters; uninsured share UP at 5 of 6 while brokered share FELL at 6 of 6 (run-prone share grew, market-funded share shrank). (2) **CUBI is the overlap name:** NDFI 34.1% of loans (PC slice 19.96%), IB deposit cost 3.54% (highest), FHLB +72% YoY, brokered 21%, uninsured 44%. (3) **Unfunded NDFI ≈ drawn at CFG ($22.5B) and OZK ($3.3B)** — draw capacity, not a forecast. (4) **Rate-sensitivity figures are INCOMPARABLE** (static vs dynamic, shock vs ramp, beta stated only by WAL); every bank's own model has NII up with rates, but **FLG's short-rate-only scenario has the opposite sign** — the 9/16 hike was a short-end move. (5) The six hold ~3% of system FHLB advances and ~6% of Q2's growth — **`REG-T-06`'s build is not in this set.** ⚠️ A Call-Report deposit cost does not reproduce company figures at CUBI/OZK/EGBN. → `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`.
- **★ CRE→BANK TRANSMISSION (9/27 PM) — what other desks should take:** (1) **At 6/30 the 14-bank cohort's CRE bad-loan rate FELL** (2.46% → 2.23%; H1 CRE NCO $528M → $452M), and deterioration sits at named banks (only OZK jumped). **Breadth is tested at the MID-PACK Q3 prints** (WAL/VLY/SSB/BKU/SBCF; DOCKET L180), not at the top three. (2) **Workout FUNDING is UNDISCLOSED for ~all exit dollars** (FLG, OZK, EGBN, VLY): 'par payoffs show the refi market is open' is an INFERENCE (CREED). (3) **Hardship-modification tables are NOT comparable across banks**: OZK booked $0 CRE against 37 RESG extensions. (4) **FLG's 47% past-due on 12-month MF modifications is a delinquency LEVEL in a changing population, NOT a cohort failure rate** (Will 20:49); the issuer's $29M/$286M 'subsequently defaulted' are UNRECONCILED. (5) **VLY Q2:** multifamily 30–89 $9.4M → $101.5M + $108M of 8-month CRE payment deferrals + a quantitative CRE reserve decline. Q3 (est. 10/22) is a CHECKPOINT; deferrals run to ~Q1-27. (6) **FLG NYC rent-regulated recognised loss = 20.45%** of original ((351+76)/2,088); the '17.5%' is withdrawn. Files: `reports/2026-09-27_cross-bank_CRE_transmission.md` · `reports/2026-09-27_VLY_CRE_transmission.md`.
- **★ NANO BANC (9/27) — what other desks should take:** (1) **its CAPITAL loss was litigation-DOMINANT alongside credit deterioration** (2025 legal expense $46.3M the largest charge in a −$75.3M loss; provision $16.7M; composition, not an exact bridge), **its DIF loss is CRE assets** — two different mechanisms; don't merge them. (2) **The early warnings were on the Call Report two years out:** Memo-3 CRE-finance-not-secured-by-RE = **79% of C&I [12/31/23]** (my cohort max ~24%), and ALLL/noncurrent fell 109% → 10% while noncurrent rose. **n=1 — not an adopted screen.** (3) **'Fed C&D 3/4/2025' (my Feb KB row) was INVERTED** — an Issuu upload date; the Fed C&D (1/18/2022) was TERMINATED 3/20/2025. If you carried it, correct it. (4) '$108M BANC+EFSC' is three lenders incl. Nano — not citable per bank.
- **★ MI3 IS A STEP-PRONE LINE — COHORT-WIDE. Read this before citing ANY MI3 trajectory, mine or your own.** The screen now runs **12 contiguous quarters × 14 banks = 168 bank-quarters** with a step detector (|QoQ MI3| >25% while loans move <5%). **It fires 17 times = 11.0% of all QoQ transitions, across 7 of 14 banks, 9 up / 8 down.** ⇒ **MI3 LEVEL comparisons are unreliable ACROSS TIME for every bank** — a second, independent defect alongside the cross-bank denominator problem, and a second reason the `>20%` flag retirement was right. ⚠️ **This DOWNGRADES my own 4th-pass alarm:** OZK's 2025Q3 step ranks **3rd** by dollars (behind **two WAL steps**, +$582M 2024Q1 and +$438M 2024Q4) and is **an ordinary instance of an instrument property, not evidence OZK did something unusual.** "OZK de-risking" stays **UNRESOLVED** — ordinary is not de-risking. `finding_base_rate_the_instrument_before_its_event_table`. **Re-run receipts: 56/56 previously published cells REPRODUCED, zero restatements (third independent confirmation); guard falsifier 8/8.** OZK question routed to its desk with the base-rate correction leading; WAL notified that the two largest steps are inside its own series (its PLATEAUED **level** verdict is unaffected; the **trajectory** claim is what this touches).
- **⚠️ ★ OZK MI3 — ADVERSARIALLY RE-VERIFIED 8/13. Read this before citing any OZK hidden-CRE figure I have published.** **✅ The data is sound:** 12/12 cells reproduce **to the dollar** on two paths that are not my script — the FFIEC **PDF** facsimile (hand-read) and the **FDIC BankFind API at a different agency and host** (`LNCOMRE` = `RCON2746` exactly). The **cohort TSV is NOT publication-blocked**, and `37.6%` is dead a **third** time (no 37.6% at any of 14 FDIC quarters). **✅ The denominator doubling is real** — a **13-quarter monotonic ramp** ($902M → $3,819M); a tool artifact makes a level shift, this is a ramp. **⚠️ But the −64% YoY must NOT be quoted as a smooth economic decline:** MI3 sat in a $980M–$1,480M band for **eleven quarters**, then fell **−36% in ONE quarter at 2025Q3**, in the same quarter C&I rose +$540M on a **flat** book. Charge-offs ($42.4M), repayment, reclassification-to-secured (the secured book is *shrinking*) and item-9 migration are **all refuted** — **the loans never moved; only the CRE-purpose memo designation did.** **★ So "OZK de-risking / genuine decline" is DOWNGRADED to UNRESOLVED** — a bank whose C&I doubles while its memo-3 disclosure falls 64% is **disclosing less about a larger book**. **No figure retracted; one interpretation is.** ⚠️ **And my own quarter grid skipped 2025Q3**, the quarter holding the entire step — two-thirds of the "−64%" is one quarter. **Still safe to cite: OZK ranks 5th of 14 on both bases; every other bank's cells; EGBN's de-risking grade (separate 7/25 primary read).**
- **★ SELLOFF ATTRIBUTION (9/29 evening) — what other desks should take:** the regional drawdown is TWO legs with different causes: **8/14→9/14 = market + small-cap beta, financials contributed +0.1%** (a 5-factor OLS, R² 0.63); **9/15→9/29 = the financials SECTOR (−5.0 of −5.9 log-%) led by the largest banks** — inside my 14-bank cohort return sorted on ASSET SIZE (ρ −0.72), not on AOCI (−0.30), NDFI (−0.2/−0.3) or my credit score (+0.48, wrong way). KBWB −7.4% / IAT −7.7% vs KRE −5.8%. **⇒ bank EQUITY repricing concentrated in incumbents' size, consistent with the rate/AOCI leg in DOLLARS or with NEXUS's candidate Root B; NOT a regional-credit event** (FLG/VLY excepted — credit-shaped, both legs). Pre-print set saw no transmission through 9/16–9/23. ⚠️ **Through 9/30 two FUNDING bars crossed** (first bullet); the credit bars are still quiet.
- **★ CCC/HY + TIER TEST — STATE AS OF 10/7 (9/29 bullet in the 10/7 snapshot):** every tier widened 9/28 → 10/1 (HY 302 → **324**, B 309 → **329**, BB 183 → 204, CCC 1,146 → **1,215 = FRED-window high**), then HY/B/BB retraced by 10/6 (303 / 302 / 185) while CCC held 1,214. **`REG-T-03` 0-of-3 (one tagged print); B never reached ORANGE 330.** The ratio's rise to **4.007×** is HY-tightening-led = denominator form ⇒ no re-escalation (9/26 escalation stands; Will 9/26: re-entry is LIQUID's). Funding did not confirm (SOFR−IORB −3 to 0bp; SRF $0). STLFSI4 tightened +0.34 to −0.468 [10/2]. ⚠️ HY sits downstream of bank credit in my chain — cross-check before calling transmission.
- **★ The hidden-CRE COHORT RE-RUN SHIPPED 8/13 — the fleet's cross-bank number now exists.** 14 banks × 4 quarters at the FFIEC primary, **56/56 rows sourced**, both bases reported → `reports/2026-08-13_MI3_cohort_rerun.md` · `workbook/MI3_COHORT.tsv`. **NEXUS's "no valid cross-bank hidden-CRE number fleet-wide" hold is RELEASED.** Headline: **the legacy `>20%` flag now catches ONE name (WAL 21.20%, falling) on the legacy basis and ZERO on the uniform basis** (cohort max EGBN 10.77%). **OZK MI3 dollars −64% YoY, EGBN −38% — while HBAN +100%, BKU +193%, MTB +16%; MTB carries the cohort's LARGEST absolute MI3 book at $4.95B while ranking as a "clean benchmark."** The ratio screen structurally cannot see that. ⚠️ **The basis picks a different winner** — WAL is #1 on the legacy basis and #3 on the uniform one; EGBN is #4 and #1. **37.6% stays kill-on-sight** (no reproducible provenance at any quarter), but the *other four* legacy cells reproduce to 2 decimals → it is a **single-cell defect, not a screen-level one**; the screen-level defect is the non-comparable denominator. Bucket-migration mechanism SURVIVES. **V1a ≠ V1 — secured office books untouched.**
- *Three 8/13 bullets (UP-CAP migration retired · THESIS doc retired, STATUS canonical · MI3 screen hardened) moved verbatim to `archive/NEXUS_BRIEF_snapshot_2026-10-07.md`; their facts are unchanged and still hold.*
- *GSE MF (8/27: "improving" RETRACTED, the book is deteriorating with a modification-suppressed headline) and Labor (8/27 claims read) bullets moved verbatim to `archive/NEXUS_BRIEF_snapshot_2026-10-10.md`. Live levels: GSE MF in STATUS §THESIS CRE row (HOMER-owned, 9/26); claims 197K [w/e 10/3] in STATUS (LABOR owns the read).*
- **Tariff guard on utilization data** (HAWK): 301 live since 7/24, 338 Canada since 8/19 — C&I line-utilization reads spanning these dates carry a tariff artifact in BOTH directions (CALENDAR standing guard).
- **UWM / non-bank servicer channel (HOMER 9/29):** Fitch cut UWM to B+ on 8/7 (found 53 days late; HOMER's Class A fired); Citi MSR line $1.875B drawn at 6/30 (not a regional). My bank-side read (warehouse lines at WAL/BKU) folds into WQ-318's NDFI/warehouse column, not a separate thread.
- **FL residential undertone:** SBCF residential nonaccrual +136%/6mo (small base, ~0.9% of book) — consistent with HOMER's REO-conversion phase signature and MARCO's re-timed FL-$ hole (flatten-and-extend into Q1-Q2 2027; capacity tell ~Sep 15 schedule filings).

## CALIBRATION

- **Conviction (decomposed):** direction-H on the *concentration* shape (5 independent confirmations; cross-bank Q2 CRE bad-loan rate FELL 2.46% → 2.23%; WQ-318 adds: funding not breaking at 6/30) · timing-M (resolvers: the 10/16–10/27 prints, then the 11/07 Call Report run) · level — my live level claims are threshold distances: **WAL $3.73 under $78 [10/9] (FIRED), HY 5bp under 320 [10/8] (0-of-3), B 15bp over 300 [10/8], claims 103K under 300K, KRE $9.01 over $60 [10/9], FLG through RED.**
- **Diverge from market by:** less than at any point this year, and honestly so — the narrowing was driven by my own grades, not the tape. Where I still diverge: the market reads benign GSE MF headlines and clean small-tier prints at face value; I carry both as composition-masked (modification suppression; definitional NPA exclusions at BKU).
- **Uncertain about:** (1) **whether the bank-equity leg is now running AHEAD of credit** (HY half-retraced while KRE/FLG/OZK kept falling) — a non-credit repricing my instruments cannot see, or credit about to re-widen into the prints; (2) whether CFG's +$3.85B Q2 FHLB draw is brokered substitution (INFERENCE) or funding pressure; (3) the cause of OZK's −4.31% on 10/6 (none found); (4) the MI3 cohort-selection rule, decide before 11/07; (5) **whether the small-bank borrowing step-up continues (10/16 H.8), how much of it is FHLB, and whether a Q3 print shows it with deposits leaving.**
- **Failure patterns to mind:** a detector that exists only as a TSV cell has no lag guarantee — the FLG band-1 break sat 8 days, the band-2 break was caught at the first boot (zero lag) once `vx_ladder_check.py` existed (census every other frozen-baseline band into it); a broker chart's last print at the bell is not the vendor close (WAL $75.21 vs $75.76 on 9/29 — grade the settled bar, label the other); a correction to my figure gets the same recompute as the figure (lesson 40).

## CROSS-DOMAIN

**SENDING:**

| To | Signal | Priority | Mechanism |
|----|--------|----------|-----------|
| PROME + FLG | `VX-REG-6.03` RED on the 10/7 close (sent `018af9846`); ladder exhausted | 🟠 | Registered routing; matrix unchanged |
| PROME | WQ-318 delivered (`a033c799c`) + memo; register CFG 10/16 / CUBI grading rows | 🟠 | Report + KB ML-REG-176..180 |
| TERRY | WAL Q3 LOCKED Mon 10/19 AMC (`fe37dd785`); `TRY-COND-KREADD` REGINALD arm NOT met (`db3565b15`) | 🟠 | Packets; cards are TERRY's |
| WALTER → OZK | OZK closed below the OZK desk's <$45 band 10/6 + 10/7 (signal lane, `db3565b15`) | 🟡 | OZK grades its own band |
| BROCK | BRK-31 grading input at Q3/Q4 prints — *I am the data source* | 🟠 | PC/NDFI-attributable reserve builds |
| PROME | `REG-T-06` re-letter WQ ask + FHLB composition (`e4916e89a`, doorbelled) | 🟠 | Will's word before the ~10/29 Q3 figure; LIQUID + BOND packets held until then |
| WALTER → LIQUID | Small-bank borrowings +11.7% in 3 wks to 9/30 (signal lane, `e1fc74154`) | 🟠 | Descriptive bar, not a registered trigger |
| PROME | WQ-414 addendum: Q3 FHLB nowcast ≈ $770B, rule before 10/24 (`047ef11d4`) | 🟠 | Evidence update only; rec (B) unchanged |
| WALTER → LIQUID | AMENDMENT to the signal: SVB scale (+$290B in one week) + FHLB debt +$6.2B in Sep (`b680ef50d`) | 🟠 | Routed WITH the original as `SIG-W-20261010-007` (WALTER `40b424536`; LIQUID action) |
| DAEDALUS | H2 as-made receipt complete, 20 rows (`28c7dd7dd`) | 🟡 | For its 10/12 sitting |
| PROME · RED | WQ-412 named SSB "State Street" (`8d31de2aa`; PROME fixed `3780a92d6`) · RED's KRE bull case cites FHLB "$480B" vs OF $676.7B/$810.7B (`b9ca8d708`) | 🟡 | Corrections; owners edit their own files |

**WAITING FOR:**

| From | Input | Expected | How it changes my view |
|------|-------|----------|------------------------|
| Will | FFIEC JWT renewal before **2026-11-05** | before Nov | The 11/07 Call Report run (MI3 + WQ-318 F1/F3/N confirm) dies without it |
| CFG · WAL · OZK · EGBN | Q3 releases 10/16 · 10/19 · 10/20 · 10/21 | Oct | Grades the WQ-318 rows on their named lines |
| FLG · CUBI | Q3 date announcements | Oct | Locks their WQ-318 grading dates |
| Will | `REG-T-06` re-letter (WQ via PROME) · REG-07 VOID-or-grade (WQ-412) | before ~10/29 · before 10/21 | Decides what a Q3 FHLB fire means; whether REG-07 grades |
| FDIC | Nano Banc Sunwest P&A posting (NOT posted 10/9) | re-check Tue 10/13 | Re-runs forensics §3 (L516) |
| Broker (PROME/ANVIL) | Activity view for the new Fidelity WAL $65P / OZK $40P (D-73/74) | — | Records entry dates; cards stay TERRY's |

## NEXT DECISION POINT

- **What:** **the Q3 read plan's frames, one per print, CFG first (Fri 10/16)**: WQ-318 rows (UP/DOWN/INCONCLUSIVE per bank), CRE §6 lines, L35/L521, FL frame + A3, AMTB non-CRE lines. **The §0 judgment moves only on L180 BROADER or FL-rail TRANSMISSION.** Plus `REG-T-02` exit grading every settled close (0-of-3, 28 rows through 10/9), the tier test on each FRED cell, and the weekly funding read (H.4.1 Thu 10/15, H.8 Fri 10/16).
- **When:** 10/16 · 10/19 · 10/20 · 10/21 (+ FLG/CUBI TBA); every close; FRED each morning ~10:15 ET.
- **Falsifier context:** the expected modal outcome is INCONCLUSIVE at most banks (declared deposit programs at WAL/EGBN, OZK's pre-announced cost inflection) — written in advance so it can be wrong. An UP row at CUBI or CFG is the result that would change the view.

## FORWARD CATALYSTS (next 2-6 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🔴 **Every close** | `REG-T-02` EXIT grading (WAL ≥81.90 ×3) | 0-of-3 (28 rows); 10/9 $74.27 is 9.3% short |
| 🟠 **Daily ~10:15 ET** | FRED HY/B/BB/CCC (cache-busted CSV) | HY >320 restarts `REG-T-03`'s count; B ORANGE >330 |
| 🟠 **Thu 10/15** | Claims (197K [w/e 10/3]) | >300K = ORANGE banks → RED (far) |
| 🟠 **Thu 10/15 · Fri 10/16** | H.4.1 discount window · H.8 small-bank borrowings/deposits | Step-up continues / reverses; a deposit decline alongside = the PNC pattern spreading |
| 🟠 **Tue 10/13** | Nano Banc P&A posted? (L516; bid summary read 10/9) | Size Pools A/D; re-run §2 |
| 🔴 **Fri 10/16** | **CFG Q3** — first WQ-318 grade | IB cost ≥2.18%, NIB ≤20%, FHLB >$7.32B, capital call + PC >$15.46B |
| 🔴 **Mon 10/19 AMC** | **WAL Q3** (call Tue 10/20 12:00) | WQ-318 WAL row; WAL desk frame (L170); AOCI vs scenario |
| 🔴 **Tue 10/20 AMC** | **OZK Q3** (call 10/21 08:30) | OREO sale prices vs 95–100% marks; COIBD ≥3.34%; L520 |
| 🟠 **Wed 10/21 → Tue 10/27** | EGBN · SSB (10/21 AMC) · BKU (10/21 BMO) · VLY (10/22 BMO) · AMTB (10/22 AMC) · SBCF (10/27 AMC) · FLG/CUBI TBA | L35 · L521 · FL rail frozen frame · L180 breadth at 11/07 |
| 🔴 **Nov 5 → Sat Nov 7** | FFIEC JWT expiry (Will) → **planned Q3 Call Report retrieval, completeness checked then** | L180 breadth (UNKNOWN rule) · cohort-selection rule decided BEFORE the run |
| 🟠 **~Thu 10/29 (est.) → Nov** | FHLB Q3 report → `REG-T-06` leg 3 (>700 fires as lettered; Will's re-letter word first; **nowcast ≈ $770B**) · FHLBank 10-Qs · FDIC Q3 QBP (~11/25) | Level, not a signal, without the composition read; a miss >$40B vs the nowcast ⇒ check FHLBank liquidity drawdown |

---

*Brief format follows NEXUS_BRIEF schema (R3 + amendments 7, 10). Created 2026-07-09; body rebuilt 2026-08-10 per Amendment 10; **folded 2026-10-10 eve** (FHLB draft check + hub; STATUS pin `4a2d5a0f0`; pre-fold = git `1ccd3353a`); **folded 2026-10-10 late PM** (FHLB nowcast, failures list, sweep; STATUS pin `9fef700b5`; pre-fold = git `5305cb2aa`); **folded 2026-10-10 PM** (pre-fold → `archive/NEXUS_BRIEF_snapshot_2026-10-10.md`; STATUS pin `4156a7882`); folded 2026-10-09 PM (As-of → `archive/NEXUS_BRIEF_snapshot_2026-10-09.md`; STATUS pin `ec21517c5`, re-pinned 10/10 closeout); folded 2026-10-07 with pre-fold snapshot → `archive/NEXUS_BRIEF_snapshot_2026-10-07.md` (prior fold 9/29 → `archive/NEXUS_BRIEF_snapshot_2026-09-29.md`) (fold = session's LAST write-back; 7/30 stale-vintage banner retired with all three annotated defects resolved into the body).*
````
