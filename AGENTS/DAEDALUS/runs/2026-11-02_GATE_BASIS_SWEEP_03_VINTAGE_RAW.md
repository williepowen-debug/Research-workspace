# Gate Basis Sweep #3 — vintage/basis reader raw report

**Reader:** `/root/gate_basis_vintage`, DAEDALUS read-only helper, not any gate owner. **As of:** 2026-11-02T15:08:32.816482+00:00. **Working-tree read, HEAD at report capture:** 1 ef 600 ebd 35f 5341 ba 6c 64759e 098d 8057 aa 4d 3a. Root `/home/willi/Research-workspace`. No owner file or code edited; only this raw report written. Parent owns synthesis, re-verification, routing and Git persistence. No market gate state, grade, trade or probability changed.

## Scope, authority and what this report proves

Read the whole 41-line `AGENTS/DAEDALUS/sweeps/GATE_BASIS_SWEEP.md`; `FORGE/PREDICTION_DISCIPLINE.md` complete Registration section (lines 4–34, in two bounded reads), and the entire 77-line `BLUEPRINTS/SPEC_LETTER_STANDARD.md`. Initial overlarge GATES/file reads truncated; recoveries used exact condition/source/definition fields, complete referenced definition sections and individual TSV rows. All 28 GATES rows were enumerated and classified. This is the vintage/basis leg only; it does not substitute for the separate stranger grade-read, a fresh grade from all current publishers, or owner consumption.

The 28 rows contain 3 terminal rows and 25 nonterminal rows. Of the nonterminal rows, 22 have operative published-observation paths and are inspected below. Three are not graded in this reader's published-series perimeter: OP-SCALE is operator-book outcome accounting; FERT-G3 is a policy-event letter; OSPREY-001's remaining unfired paths are SPM structural assessment / Tengiz force majeure (its numerical loading/suspension path already fired and is not re-armable). OSPREY's historical Kpler/suspension path is therefore not silently treated as nonexistent: it is an already-fired observation path with no fresh counting use. If the parent chooses to include it retrospectively, add a historical-only row rather than re-fire it.

S/U/V/O/C/R below mean **series**, **unit/conversion**, **resolving vintage**, **operator/precision/tie**, **consecutiveness/calendar**, **reset**. Y = named; D = WQ-162 as-first-published default is applicable (not proof that a publisher never revises); N = not named for the indicated live sub-leg; NA = this is a single/event observation with no run to reset. The observation counts count VALUES actually compared, including frozen endpoints; intermediate dates needed to establish a window are additional identity keys, not invented value observations. Variable counts are stated as formulas, never forced into one total. No aggregate six-element score is claimed for mixed numeric/event letters.

## Findings ranked for routing

### V1 — NEW, independently reproducible: inclusive −15% letter can fail in LIQUID's pipeline

**Gate:** GATE-LIQ-069 L4. **Definition:** `AGENTS/LIQUID/workbook/KB.tsv`, exact row KB-LIQ-069, PRECISION/TIE/RESET amendment: raw unadjusted two-decimal closes; compare unrounded ratio; **≤ −15% INCLUSIVE**, exact −15.00 meets. HY change **≥ +5 bp inclusive**; any one cohort name qualifies. **Code:** `AGENTS/LIQUID/scripts/gate069_legs.py::grade_l4`, lines 107–109 compute `(c[last] / c[ep] - 1) * 100` and later compare the float with −15.0.

Offline capable case: all four names 2.40 → 2.04 on consecutive NYSE sessions 2026-10-28 / 10-29, HY 300 → 305 bp. Decimal arithmetic is **exactly −15.00%**; code returns **NOT FIRED**, worst −14.999999999999991. In a sweep of **2,991 exact-boundary price pairs** (base = 20*k cents, close = 17*k cents, k=10…3000), **815** return false NOT FIRED. This is a pipeline defect despite a clear letter, not a letter rewrite. Counterexample that would refute this finding: the exact two-decimal input pair is not an admitted raw-close observation under the registered letter, or production normalizes it before grade_l 4 in a way absent from this direct function call. The exposed grading function itself admits the inputs. No claim that a live qualifying event was actually missed.

Reproduction (imports only the pure module; `if __name__ == '__main__'` guards its live path; no market pull or owner write):

```python
import importlib.util
from decimal import Decimal
spec = importlib.util.spec_from_file_location('gate069', 'AGENTS/LIQUID/scripts/gate069_legs.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
assert (Decimal('2.04') / Decimal('2.40') - 1) * 100 == Decimal('-15.00')
hy = {'2026-10-28': 300, '2026-10-29': 305}
def trial(new):
    eq = {t: {'2026-10-28': 2.40, '2026-10-29': new} for t in m.TICK}
    return m.grade_l4(hy, eq)
print(trial(2.04))  # observed NOT FIRED: false negative at the inclusive tie
print(trial(2.03))  # parent independently observed FIRED: capable control
print(trial(2.05))  # parent independently observed NOT FIRED: clean control
```

The two control outputs above are **parent's independent observation**, reported in its message; this reader independently watched the full boundary sweep and exact Decimal computation. Parent also reverified the 2.40→2.04 failure. Suggested owner ask: LIQUID preserves the ≤−15% letter and fixes the exact-decimal comparison with boundary-class fixtures. No generic tolerance/rounding or DAEDALUS direct edit is authorized by this finding.

### V2 — NEW registrar mirror drift: CORAL reading identity changed on a ruled owner letter

`GATE-CORAL-MSI-01.condition` still names a **page stamp** and one pull of five pages on one page stamp. Canonical `AGENTS/CORAL/STATUS.md` OQ **A2** explicitly encodes **WQ-475 A, Will 2026-10-21**: identity = **the data date of one Parcl build carrying all five metros**; governing series = **CURRENT**, prospectively from reading #11. The owner still preserves the September letter above A2 as history, with precedence made explicit. Numeric thresholds and persistence are unchanged. The October 27 current-series reading in state already follows A2, so the registry condition and current practice disagree in meaning.

Counterexample: an operator follows the summary literally and refuses all readings because the retired page stamp no longer exists, while the owner letter permits a correctly identified current build. **This is PROME summary drift, not a CORAL missing-basis defect.** Ask PROME to mirror its already-approved A2 identity and series, preserving the pointer/owner authority; no new numerical rule or re-grade.

### V3 — OPEN owner ambiguity now within a live December window: ORACLE business-day calendar

ORC-12's VX row names a qualified first read per **US business day**, alert on two qualified reads on **consecutive business days**. Its named observation/reset letter `analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md` O3 and §7.4 **⚠31** explicitly leave **“US business day = ? calendar” OPEN**, describing the issue as moot **through 10/30**. The December successor now extends to 12/09. The old moot-through date is not a definition of the later calendar. Weekday cron/routine counts are not themselves a ruled eligibility calendar.

The gap-count ambiguity and clearing ambiguity are **NOT reopened**: §§9.1/9.2 encode WQ-476 (strictly-between business days, sequential clearing). Counterexample: two plausible US calendars disagree about whether an intervening weekday is a holiday; the same two pulls may be consecutive under one and not the other. Ask ORACLE to identify the existing intended calendar or propose the missing convention; no calendar chosen by this reader. No present Alert/de-alert is graded.

### V4 — UNG summary omits a card guard; joint interpretation needs owner confirmation

`GATE-TERRY-UNG-01.condition` VOID text names **UNG ≥ $10.40 at entry**. Canonical card `AGENTS/TERRY/setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` **§2** additionally says **UNG closes ≥ $10.40 before entry** voids it. Parent correctly pointed out that **§4** also refuses UNG ≥ $10.40 at entry, and **§6** execution block requires UNG < $10.40. This reader then read both complete sections.

**Withdrawn:** the first provisional counterexample suggesting intraday ≥$10.40 could be allowed if the prior close was lower. §4 refutes that. **Surviving counterexample:** a prior settled close of $10.45 followed by an entry quote $10.30 fails §2's historical-close guard even though the summary's at-entry price test passes. Both card guards may be intended jointly; their coexistence is not proof of a contradiction. Ask TERRY to confirm the joint guard and PROME to carry both if so. No order, trade-state inference or new price limit.

### V5 — actionable-life residue, with an already-approved exception kept distinct

- **GATE-NEXUS-T12S-DFII10:** nominal W=15 published cells, run N=5, H.15/FRED lag ~1 and one later tradable session ⇒ **15 − 1 − 5 − 1 = 8 actionable cells, 8/15 = 53.3%** by this playbook's stipulated arithmetic. Earliest run ends at cell 5; a cell 15 fire publishes too late for action inside the nominal window. This is a next-letter/registrar disclosure, not authority to stop or revise this live owner-only letter. Exact trading-clock actionability still requires its horizon/implementation choice; no claim that the probability consequence becomes legally impossible after the nominal last cell.
- **GATE-NEXUS-WQ459-HY:** nominal 15/run 3/lag 1/later-session 1 ⇒ **10/15 = 66.7%**. This is **already explicit in the frozen owner letter AND accepted by Will's `PROME/proposals/2026-10-19_wq459-guarded-hy-RULED.md` Limitations**. Do not route a new re-registration demand as though it were undisclosed. Preserve accepted limitation, not a new blocker or automatic NO-VERDICT.
- **LIQUID-076 W2:** one of its 2-week conjunction legs uses NY Fed weekly Wednesday data published ~8 days later plus two-print persistence. A clean nominal-window fraction cannot be supplied without deciding whether the nominal 14-day observation window or a decision horizon is the denominator. No explicit finite expiry exists. Mark **CANNOT-CERTIFY actionable-life denominator**, not an invented short-window fire prohibition.
- **HOMER formal 11/20 grade:** owner §7 V5 already proves core kill count cannot reach 3 with only 2 post-registration monthly prints before that formal grade. Existing accepted staging, not new missing life. Counts update at releases; formal grades are not the eligibility window.

## Per-gate vintage/basis table — all 22 operative published-observation gates

| Gate | Observations needed (values, not polls) | S/U/V/O/C/R | Basis disposition and material limit |
|---|---|---|---|
| HY-REKILL | 2 consecutive HY prints | Y/Y/Y/Y/Y/Y | BASIS-NAMED. Canonical <260.0 strict, 0.01 percent × 100 to whole bp, missing/nonpublication bridge, ≥260 reset, terminal fire. T+1 pending is not a negative. ALFRED path control passed below; no new no-revision census. |
| LIQ-069 | L1 BB1 + CCC2 endpoints (6 CCC dates establish t−5); L2 latest quote plus two anchor prints, plus Dec peak for branch B; L3 deal price+guidance 2; L4 HY2 + 2 closes×4 names=10; L5 one rating action at a time | Y/Y/Y/Y/Y/Y for measured L1/L2/L4; L3 source N | BASIS-UNNAMED only for L3 unprovided primary/producer, already declared NO_INSTRUMENT (no new whole-gate no-fire claim). L5 secondary-source convention is explicitly registered, not falsely primary-verified. Pipeline V1 can fail L4's clear operator. Two sign readings are two model interpretations of the same input, not twice as many observed quotes. |
| LIQ-072 | Numeric live L2 IG1; HY−IG basis 2, reused IG ⇒ 2 distinct current series; L1/L4 issuer pricing/comparator values variable | Y/Y/Y/Y/NA/NA for numeric leg; N-source on event legs | BASIS-UNNAMED for live event L1/L4 unnamed producer-at-grade; neither is certified NOT FIRED. Historical SpaceX L3 is CANNOT-FIRE with elapsed window, not merely waiting for a date pin. Basis half was restored 10/1; do not re-raise its old omission. |
| LIQ-076 | W1 level 1 or delta 2; W2 G10=1 or G5L10=2; W3 MOVE+VIX2 per session; aggregate depends on 14-day calendar | Y/Y/Y/Y/Y/Y | BASIS-NAMED measurable letter after 9/29. Exact corporate PD ids, frozen −2,950,000, whole-contract ties, 14 calendar days, 10-business-day re-arm all named. Lag-denominator limitation above. |
| LIQ-079 | ARM2 dates×(SOFR99+IORB)=4; fire 3a EFFR/IORB at two endpoints 4; alt 3b percentile+IORB2; dispersion 2 or repo take-up 1; shared endpoints reuse | Y/Y/Y/Y/Y/Y | BASIS-NAMED ARM and newly banded FIRE numeric legs. WQ-535 (10/29) supersedes old unbanded FIRE deficiency. Calendar exclusions and rounding order explicit; generic “ties inclusive” does not repeal specifically strict EFFR75>IORB alternative. Archetype remains domain judgment. No new rate-calibration claim (n=1 true positive). |
| FALCON-001 | L2 two current 7d totals + frozen preceding 7d reference=3 aggregates, plus attribution evidence; historical L3 at least 2 tracker prints | Y/Y/Y/Y/Y/Y for live L2 | BASIS-NAMED live L2: current-vintage completed UTC days, integer 100×current≤65×reference, floor 21, missed-day readback, nonqualifying reset. Approximate historical L3 threshold no longer creates a fresh firing decision; no re-arm authorized. |
| BRENT-COT-35B | current shorts+OI2; frozen 8-print median and 104-week ratio distribution are additional construction inputs, not fetched per live grade | Y/Y/Y/Y/Y/Y | BASIS-NAMED. .5 median restored, exhaustive deadband and exact rational OI comparator; first-print resolving vintage plus same-report-date reissue alarm. Never run production cot_grade here: it can append owner ledger. |
| FERT-G5 | current weekly DTN DAP+MAP2; either strict>1000 suffices | Y/Y/D/Y/NA/NA | BASIS-NAMED current article/whole-dollar strict operator. Exact T4 canonical-home text and first-party wake method read. Pink Sheet monthly≥ context is explicitly NOT this gate's base rate; old operator mismatch closed, not re-raised. Full-history DTN access inference remains caveated, not proved absence. |
| CORAL-MSI-01 | five metros×two qualifying readings=10 values minimum; each intervening reading adds 5; current build data-date IDs | Y/Y/Y/Y/Y/Y owner letter | BASIS-NAMED canonical owner definition with WQ-475 A2; registry mirror drift V2. Same-metro stand-down<5.90 vs all-five strict>6.00 re-fire; ≥10-day first-clock rule named. |
| TERRY-ROLL70-EXIT | 3 settled WAL official raw closes; verification two tools/pulls per bar is not 6 different market observations | Y/Y/D/Y/Y/Y | BASIS-NAMED. ≥81.90 ties qualify, settled bar volume stable across tools, unadjusted per-share, regular sessions, missing cell UNKNOWN blocks completion, below resets. |
| BRK-R2 | per vehicle 3 issuer-stated quarterly proration/satisfaction observations for (a); final quarter ratio 1 or numerator/denominator 2 for (b); monthly inputs aggregate Σaccepted/Σsubmitted, never average rates | Y/Y/Y/Y/Y/Y | BASIS-NAMED. Population six with main North Haven registrant fixed; a prelim≤94 counts, >94 awaits final; b final only; as-filed precision; unmeasured breaks. P13 WQ-563 latch is now RULED/IN FORCE10/31 and owner-encoded 11/2; prior “post-fire missing” finding is closed. |
| NEXUS-T12S-DFII10 | 1 anchor + up to 15 window DFII10 cells; decisive run 5; mechanism adds DGS10 endpoints 2 or HY endpoints 2 | Y/Y/Y/Y/Y/Y operative series | BASIS-UNNAMED(actionable-life) by playbook arithmetic 8/15, V5. Basis/branch letter itself is otherwise explicit; no live re-grade. Stated precision comes from as-published source, no finer rounding introduced. |
| TERRY-VLO-HELD-01 | source 1/2 HO+CL2 per settle; source 3 two bars per contract=4 price/volume pairs, plus source 2 comparison when used; B event is separate | Y/Y/Y/Y/NA/Y | BASIS-NAMED current A. WQ-386 December amendment explicitly native precision, no pre-rounding, exact 2-bar [14:28,14:30), own-leg volume weights, inclusive≤0.15 acceptance and UNKNOWN zone; no new January roll. Prior run 2 rounding/window defects are cured in approved amendment. |
| HOMER-THESIS-KILL | C1 2 metrics×3 months=6; C2 Trepp 3 + Freddie 3 + Fannie 3 + quarterly provision pair 2 when invoked=11; reuse shared prints. Amplifiers are reported not kill-deciding | Y/Y/Y/Y/Y/Y core | BASIS-NAMED core letters after §7 V1–V5. First-published core releases, missing month PAUSES, Fannie serious DQ, pre-sale COUNT, provision QoQ paired values all named. Do not generalize core-vintage wording to every amplifier; those are outside this gate's core-kill decision. |
| BRK-OTIC | R first issuer-stated requests 1/quarter; S offer-size 1 or event; CLEARING2 first request quarters or satisfaction 1 | Y/Y/Y/Y/Y/Y | BASIS-NAMED numeric issuer observations, as-filed/first-vs-final rule, strict 45.0 and 5.0, population 1, graded Q4 onward, R quarter-fresh, S latches to resumed≥5.0. Missing issuer publication means UNMEASURED, not proxy-reconstructed. |
| NEXUS-WQ459-HY | five-series carry test current+prior up to 10 values; HY/CCC anchors 2; each qualifying window obs HY+CCC2; up to 15 window dates, mechanism IG/B endpoints | Y/Y/Y/Y/Y/Y operative series | BASIS-UNNAMED(actionable-life) by playbook 10/15, **already accepted by Will**, not new defect. First-read log plus latest-vintage double grade; disagree⇒C; integer bp inclusive; +35-day backstop and <3 VOID; count-once all named. |
| REG-27 | one issuer ratio per quarterly release; up to 4 releasesQ3-26…Q2-27 | Y/Y/D/Y/NA/NA | BASIS-NAMED. Exact issuer EX-99.1 table/row, >=0.70%, printed rate, any release; source release graded then 10-Q confirms. Base 0/5 was on same inclusive cutoff; no new raw-primary re-pull. |
| REG-28 | four loan identities from baseline plus four year-end held/exited/unknown observations; h/x counts, no missing=exited substitution | Y/Y/D/Y/NA/NA | BASIS-NAMED filing-state observations. EGBN deck table cutoffs and fallback 10-K, loan identities/maturities, h>=3/x>=2/else NO-VERDICT fixed; Mar 16 immovable backstop in notes. Binomial 74% base is disclosed as correlation-shaded, not a market series. |
| REG-29 | six Q4 rates + six frozen Q3 rates=12 | Y/Y/D/Y/NA/NA | BASIS-NAMED. Each issuer annualized NCO / average loans printed; equality not above; r+n failure branch and no-print NO-VERDICT. Base 50% transition rate implies binomial 34.375% for≥4/6, consistent with displayed 34%; no claim of independence calibration. |
| REG-30 | one Q4 total + frozen 9/30 comparison=2 | Y/Y/D/Y/NA/NA | BASIS-NAMED as printed $K; >=511390 inclusive. Definition change/absent table⇒NO-VERDICT; restated comparative noted. Do not decide an eventual line-definition conflict here. |
| ORC-12 | alert 2 probability reads +2 same-row liquidity values=4; de-alert similarly; watch 48h pair 2 probabilities, Critical FOMC event 1 | Y/Y/Y/Y/N/Y | BASIS-UNNAMED(calendar), V3. Exact PM meeting slug YES, Kalshi corroboration only, 0.1 pp inclusive 50, first own pull per date, >=$5K, 2 qualified reads; US calendar still explicit OPEN. Gap-count and clearing rules already ruled. |
| TERRY-UNG-01 | T1 observed analysis wind 1; red-session prior/current prices 2; prior settled-close history and entry quote are separate checks; spread debit 1 quote | Y/Y/D/Y/NA/NA T1 | BASIS-NAMED existential analysis threshold for T1 (ECMWF or NOAA GFS,10hPa 60N,< 0 m/s,observed not forecast). Source/current analysis timestamp matters. Card/summary guard question V4; no fired/non-fired state assessed. |

### Remaining 6 ledger rows, each accounted for

| Gate | Disposition | Reason |
|---|---|---|
| GATE-OSPREY-001 | NOT GRADED | Remaining live branches are event assessments; its already-FIRED(b) quantitative branch is latched, no fresh count. Read definition §7 in full, not retrospectively regraded. |
| GATE-OP-SCALE-01 | NOT GRADED | Distinct closed operator positions and refusals, not an external published series. No book or operator-hands assessment attempted. |
| GATE-FERT-G3 | NOT GRADED | Policy revision/floor event letter, not a periodic published-series count. Its comparison against prevailing international FOB remains the event owner's judgment; no numeric substitute supplied. |
| GATE-NEXUS-SEAT-01 | NOT GRADED | RESOLVED(TERMINAL), operator decision-attribution experiment. |
| GATE-TERRY-VLO-SCALE | NOT GRADED | RESOLVED(TERMINAL); not revived by held-share December amendment. |
| GATE-ORC-11 | NOT GRADED | RETIRED(TERMINAL), October meeting; December ORC-12 is the live successor inspected above. |

## Retrieval negative control — fresh execution, not inherited receipt

Used direct standard-library urllib HTTPS requests to **ALFRED/FRED official API `series/observations`**, same `PAYEMS` observation **2026-06-01**, two exact realtime dates and one deliberately malformed realtime date. Existing FRED_API_KEY loaded in memory from environment or existing market-data .env; never printed, saved, or embedded in the report URL. Did not import fetch.py, whose cache/write behavior was not needed. No owner data/cache files written.

| realtime_start = realtime_end | HTTP | extracted (date,value) | raw payload SHA256 |
|---|---:|---|---|
| 2026-07-10 | 200 | (2026-06-01,158984) | 37513c 198 ee 5 cf 9c 542b 1905a 2604 aa 0c 11a 9f 38a 6770445d 294 bb 4a 5 aaa 6177 |
| 2026-09-10 | 200 | (2026-06-01,158892) | f 2235a 1046 ddd 8a 5 cc 88 df 19b 977189016a 30822a 75d 534b 5470d 5 cf 4d 118b 90 |
| not-a-date | 400 | rejected | b 75744 ebf 73f 86b 3f 1 ab 9 cbaecb 4 bf 3 eadb 4d 1946673b 5 ebcc 3f 303136 bb 5323 |

**VINTAGE-PATH-VERIFIED**: extracted values differ by 92 thousand payroll jobs, and invalid date refused. Endpoint honors realtime controls. **This proves nothing about revision frequency of HY, SOFR, DFII10, CFTC, Parcl, model analyses or issuer filings.** No “unrevised” verdict for those series is shipped. No claim that ALFRED's date stamp proves wall-clock arrival time (LIQUID's known backdated-OAS realtime clock is retained). Payload hashes support identity, not the verdict.

## Pipeline perimeter and observed behavior

- `LIQUID/scripts/gate069_legs.py`: whole L1/L4 pure grading functions + calendar + main guard read. Boundary-class pure function probe performed; V1 reproduced. No live main.
- `LIQUID/scripts/hy_oas_watch.py`: `_first_published` whole function read. It requests output_type 4, excludes missing values, rejects duplicate dates before counting, converts bp as integer. Routing/file-write paths were read to prevent accidental main execution; not run. No new duplicate-date failure claim.
- `LIQUID/scripts/boot.py::grade_076`: function's window/per-leg missing logic inspected (through construction of MET/UNKNOWN/NOT); full live boot not executed because it has external pulls and owner writes. Data-calendar restrictions differ by W1/W2/W3 and no false clean claim is made beyond inspected code.
- `BRENT/scripts/cot_grade.py`: raw market-name identity, current-vs-expected date, read_ledger/reissue_check and leg_a/leg_b/joint functions read. LegB now uses Fraction exact rational compare (10/09 repair); do not re-raise former float tie. CLI defaults can append COT_VINTAGES, so not executed. Duplicate ledger keys are last-row-wins in inspected reader; no fabricated live duplicate or separate defect finding without a reproducer.
- NEXUS guarded-HY first-read log named by letter inspected through its current records for actual receipt fields; no numerical re-grade. Scripts directory does not exist under NEXUS; no invented local grader or execution claim.
- Manual issuer/filing grades, TankerMap retrieval, TERRY settlement source hierarchy and ORACLE run grader were inspected at their defining records only, not end-to-end executed. **The full fleet pipeline contract is not behaviorally certified.**

## Coverage ledger and not-read limits

Whole applicable definition sections were used, not arbitrary windows cutting a rule: HY canonical letter and grader conventions; exact KB-LIQ-069 / KB-LIQ-072 rows (069 recovered as characters 0…12499 and 12500…end); LIQ-076 Fire conditions including basis/window/reset; LIQ-079 scoped fire spec including ARM basis; FALCON FRESH_LEG_BASELINE entire canonical section 41…141 incl historical states/amendments (three bounded chunks); FERT T4 exact row and KB-FERT-006 exact row (superseded warning retained); CORAL complete OQ A/A2 letters through the next OWED TABLE; TERRY ROLL70 complete guard section; BROCK PC register entire header P1…P15; BROCK OTIC whole §§1–8; NEXUS DFII10 whole construction §1 and frozen §2; NEXUS guarded HY whole current file; HOMER complete frozen §§3–4 + complete defects §6 and clarifications §7; REGINALD exact REG-27 through REG-30 rows; ORACLE exact VX-ORC-12 row and complete entire observation/reset letter through §9.5; UNG complete §2/§4/§6 and management §7. No inference that a source's non-read unrelated section was covered.

Supporting references inspected: FALCON original proposal §5, full 8/10 leg 2 adjudication, leg 3 data/dating§§2–3 (historical no-regrade); OSPREY CPC §7 whole; BRENT COT card whole after initial bounded reads and registry exact row; FERT8/17 proposal whole + EXIT_PROTOCOL whole; CORAL8/23 source packet whole; HOMER9/29 registration packet whole and exact formal-grade catalyst row; BROCK9/3 out-of-sample record whole; NEXUS9/24 delivery whole, guarded-HY10/19 ruling whole, guarded first-read log targeted entries; REGINALD10/21 and 10/22 delivery packets whole and REG-T02 September 1 state ruling whole; ORACLE10/28 delivery and 527/528 ruling whole; BRENT STATUS exact COT row.

**Not read / remaining coverage:** all historical source packets/rulings in the 28 GATES source columns were not universally read whole. In particular the full FALCON7/23 leg 1 fire and 8/15 leg 3 fire reports, full OSPREY7/23 outbox and current STATUS, BRENT's full VLO observables source, TERRY full VLO held card outside declared sections and full UNG card outside declared sections, HENRY9/24F1 source, the three terminal letters/sources, and every WQ/docket row behind the provenance were not re-audited. The present canonical operative clauses/amendments above were inspected; parent should not label this a complete historical source audit. Whole massive TSV files were not read when exact registered rows/headers were the definition. No full all-series vintage census, fresh current trigger grades, historical base-rate primary recalculation, independent verification of every owner-reported source figure, or owner consumption receipt. The parent must retain these limits in the sweep synthesis; advance a whole-run clock only if its other reader/re-verification completes the required perimeter.

## What would refute the overall result

A later authoritative approved amendment not followed by this reader can cure a named omission or change which letter governs. The parent must check current owner files before routing V2–V4, particularly live concurrent desks. A source row containing the opposite operator in a historical comparison is not automatically an OPERATOR-MISMATCH in a current letter: FERT's Pink Sheet base was relabeled context and is not its gate's own base rate. No NEW base-rate operator mismatch was proved by this reader. Any threshold/actionable-life flag is a prospective registration/disclosure ask, never authority to rewrite a current letter or retroactively negate an owner grade.

## End-of-read fingerprint (working tree, not a freeze certificate)

| Path | SHA256 |
|---|---|
| PROME/GATES.tsv | b 071 cfd 75a 80e 6548939 cf 7a 0 cfd 39e 313b 88a 97b 422 eb 0e 1 dd 9 ad 3c 5b 188023 |
| AGENTS/LIQUID/scripts/gate 069_legs.py | 921a 5180b 699 dd 59423 abf 4787 adbacc 1594 da 2 dd 1d 884655069467824792 eb 6 |
| AGENTS/CORAL/STATUS.md | 018732f 6 bcdbe 5c 15 ba 1c 109b 77d 9b 131c 7325 feeb 5a 4508 fe 6 ade 0 cce 638692 |
| AGENTS/TERRY/setups/UNG_jan 15-10-12C_polar-vortex-break_2026-10-31.md | 9d 3 eb 1 aef 35 adb 5883f 534563 caad 04891e 1192a 0a 18 ed 8 ec 12d 10c 22597221c |
| AGENTS/ORACLE/analysis/2026-10-09_wq 314b-v 5-observation-and-reset-rules.md | 638d 7a 15455 ef 57 cc 2e 2335f 60c 06873a 2 eea 751729e 0 bea 51f 9125456f 47c 7b |
| AGENTS/NEXUS/research/2026-10-19_WQ459_guarded_HY_letter.md | 478005 fe 1018a 99928 fb 03 bc 160 fcf 52a 7253 fdcbd 3 bbbcebaa 188b 1c 5935843 |
