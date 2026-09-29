# VIOLET CANARY MAP — fleet early-warning layer (v1.3)

**Reviewed September 14, 2026.** This map owns instruments, threshold references and routing relationships. **Current values live in STATUS.md and the named ledgers**, not duplicated here. Pre-sweep evidence histories: `archive/sweep_2026-09-14/CANARY_MAP.md`.

SKEW here means the **Cboe S&P 500 SKEW index**, not SPX delta-specific put skew or rates swaption skew. A canary informs interpretation; it is not permission to trade.

## TIER 1 — OWNED, LIVE

| Canary | Leads / scope | Registered threshold | Source / cadence | Owner / current value |
|---|---|---|---|---|
| MOVE | Rates-vol transmission | F1 >72.41; confirm-3 75.50; N1 <66 (KB-VIO-116/123) | investing.com primary; daily via move.py | STATUS / MOVE.tsv; original GATE-VIO-116 resolved |
| CCC / CCC−BB | Credit-to-vol | BIN-A old level tree STUCK, no verdict; BIN-B block CCC ≥9.55 | FRED, observation-date lag | LIQUID owns substance; STATUS / fred_cache |
| VIX3M/VIX | Peak marker, not onset | <1.0 | Cboe same-date quotes + archive; daily/intraday | STATUS / VX_DAILY.tsv |
| VVIX | Vol-of-vol | >100 watch; >120 stress | Cboe; daily/intraday | STATUS / VX_DAILY.tsv |
| SKEW | Tail pricing | Legacy VIOLET prediction #6 >150 sustain-4 is distinct from RED-FT-10 ≥150 sustain-4; do not merge inequalities or grades | Cboe archive for grading; quote timestamp for provisional context; EOD | STATUS / VX_DAILY.tsv; RED owns FT-10 |
| COT leveraged money | Crowding | Historical band (−75,000,0); percentile ≥90 informal extreme; KB-VIO-123 requires ≥95 | CFTC actual release availability; report-date cadence + grace | COT_VIX.tsv; do not synthesize holiday release rules |
| JPY vol | Carry transmission | RV p90 WATCH / p95 FIRE, recomputed per run; IV/RV >2 event premium | JPY history + usable FXY IV; daily | JPY_VOL.tsv; SAM owns policy/causality |
| OVX/VIX | Oil-vol transmission | Ratio p90 WATCH / p95 FIRE plus OVX p75 floor | OVX/VIX history; daily | OVX.tsv; BRENT/HAWK substance; inspect numerator and denominator |
| Cheap-tail | Opportunity alert | VVIX ≤90 AND VIX ≤16 AND SKEW ≥140 AND catalyst ≤21d | One dated Cboe close + catalyst feed | CHEAP_TAIL.tsv; no partial reopen; GATE-VIO-RV1 remains retired |
| Implied correlation | Index-vs-constituent volatility | No new calibrated action threshold | Cboe quotes; daily accumulation | IMPLIED_CORR.tsv; derive daily change from distinct dated ledger rows |

## TIER 2 — OWNED, SCOPED / THRESHOLD TBD (honest holes)

| Canary | Leads | Threshold state | Pull source · cadence | Route on fire | Status / what closes the gap |
|---|---|---|---|---|---|
| **Single-stock vs index skew split (put/call)** | Positioning-complacency extreme / private-cushion depletion | **TBD** — 0.71 [7/10] is a record low (10-yr avg 12) but no registered line exists; what sets it: one percentile-calibration pass against the 10-yr series (source access via WALTER/YCharts to be established) | **No direct pull** — arrives via WALTER signal intake only (SIG-W-20260709-015 class) · ad hoc | → feeds VIOLET's own complacency verdicts (fresh-look 7/11 §3); no standalone gate | Fed the 7/11 NO-FIRE verdict as the "no private cushion under single names = amplification risk" leg. Needs: pullable source + calibrated line |
| **NDX−SPX 3m ATM IV dispersion** | Concentration/Path-B pricing (VULCAN mechanism seam; HENRY expression) | **TBD** — known anchors: ATH 10.80 [6/23], 2nd-highest 10.2 [7/2 signal], mean ~5.1 [SIG-W-20260702-017]; a registered line (e.g. fresh-ATH = Path-B pricing signal) should be set AFTER the VULCAN seam reconciliation | **No direct free pull found** — WALTER intake only · ad hoc | → VULCAN (mechanism) + HENRY (expression); route-out for the existing series already queued (threads-sweep RO-1) | 6/23 ATH aligned with the Path-B partial-fire (KB-VIO-105) — one demonstrated coincidence, not yet a calibrated lead |
| **Korea 2× leveraged-ETF amplifier (KOSPI)** | Offshore Path-B realization — concentration stress realizing where it isn't indexed away (Korean leveraged retail flow amplifying US AI/semi moves) | **No validated live VIOLET numeric trigger.** Historical KOSPI 8,200 anchor is unverified (DEWEY July 20); do not propagate it as an operative level. Watch actual concentration, leveraged-ETF rule changes and owner-confirmed flow. | **No direct pull** — WALTER intake + ad-hoc web check on US-semi stress days · ad hoc | → VULCAN (mechanism seam — SK-Hynix/HBM/KOSPI-as-semi-proxy leg is VULCAN S2's; reconcile-to-one-figure on KOSPI levels) + NEXUS_BRIEF cross-domain; Korea macro broadly = explicitly unowned | **FORMALIZED VIOLET-OWNED 7/25** (DAEDALUS 7/22 disposition packet, Will-approved 3-way split of the fleet KOSPI gap; was Tier-3 "no watcher"). **WORKED 6/23-7/2:** Korea realized the unwind (2 circuit-breakers, 30 sidecars YTD, record margin defaults) while US VIX absorbed — same stress visible offshore first |

## TIER 3 — REFERENCED (other-agent-owned; VIOLET consumes, does not pull)

| Canary | Leads | Threshold [owner] | Route | Note |
|---|---|---|---|---|
| **Net GEX / flip band** | Equity amplification context | HENRY owns measurement and validity; one-session shelf life | HENRY → VIOLET context | Live board in STATUS and HENRY NEXUS_BRIEF. Never copy a dated sign into this durable map; all pre-Sep-14 wall levels are void. |
*(KOSPI 2×-ETF amplifier row promoted to Tier-2 as VIOLET-owned, 7/25 — see above.)*

---

## Staleness audit contract

> ## ⚠️ **STANDING RULE — `^SKEW` VALUES MUST BE INTEGRITY-CHECKED AT THE MOMENT OF USE, NOT AT BOOT** *(added 2026-09-04, KB-VIO-241)*
>
> **Before quoting or grading any `^SKEW` value, run:** `.venv/bin/python3 AGENTS/VIOLET/scripts/skew_integrity.py --days 30` **and paste its one-line verdict beside the claim.**
> **Why not a boot check — this is the design, not an oversight.** The mirror's defect **heals** (KB-VIO-221: the 8/28 hole was present 9/2 and gone 9/4, in the same query), so a check that runs *before* the work does not bound the work — the gap can open between boot and use, and a later audit passes clean over a grade that was wrong when computed. **Wiring it into boot would manufacture exactly the false assurance it exists to refute.**
> **It compares VALUES, not bar counts.** ⚠️ **CORRECTED 2026-09-11 (COR-20260908-03, receipting RED's 9/6 full-history census). The rate this line carried was withdrawn by its own author on 9/6 and stood here live for 5 days.** There are **THREE** defect modes, not two: ① **OMISSION** — CBOE bar absent from the mirror (62 sessions, 0.67%) · ② **FORWARD-FILL** — mirror repeats its own prior value while CBOE moved (77, 0.84%) · ③ **DATE-SHIFT** — mirror value = CBOE's *previous* session (**316, 3.43%**). **397 unique defective sessions = 4.31% of the full 9,221-session history; the modes OVERLAP and must never be added as disjoint counts.** The old **2/253 = 0.79%** is **WITHDRAWN** — RED's own 253-session window reproduces **0.40%**; that window was a quiet sample published as the instrument's rate. **The 2025-12-24 cell (CBOE 161.30 vs mirror 160.53) is RECLASSIFIED to mode ③ DATE-SHIFT, not a value error** — the mirror carries the right number on the wrong day; which value was *first published* on 12/24 remains **UNKNOWN**, and a shift is consistent with either. 🔑 **Rank mirror defects by DETECTABILITY, not frequency.** A completeness check catches ① and is **blind to ② and ③ — 84% of all defective sessions** — and **neither a completeness check NOR a value-range check can catch ③**, because every value present is a real published SKEW value sitting on the wrong date; that needs a **paired-date comparison against the publisher.** **Mode ② is the one that bites a sustain counter, and FT-10 is a sustain-4 counter on exactly this series:** a frozen value **above** a line **holds alive** a run the publisher had already broken, **below** one it **kills** a run that was actually running, **and nothing looks wrong either way.** (RED KB-RED-093 / ML-RED-222; supersedes KB-VIO-236.)
> **rc:** 0 clean · 1 defect (grade from CBOE only) · **2 = endpoint unreachable, which FAILS CLOSED — an unreachable publisher is not agreement and must never be quoted as verification.**
>
---

A canary is **DARK** when its last pull exceeds 2× its stated cadence (EOD instruments: **>2 trading days**; ad-hoc WALTER rows exempt but must carry their signal date).

⚠️ **COT IS NOT GRADED ON CALENDAR AGE AND THE OLD `>9 days` LINE IS RETIRED.** A `>9d` rule false-DARKed a perfectly current ledger **every Friday morning**. Its replacements were wrong twice more — first assuming a fixed Tue→Fri+3d lag, then inventing a Monday-holiday Tue→Wed report-date shift that **does not exist** (my own ledger holds `2026-05-26`, a Tuesday straight after Memorial Day). **The live rule (v4) synthesizes no calendar at all:** observed cadence + a grace window, evaluated on the ledger's own dates — **0 = nothing owed · 1 cycle late = 🟡 PENDING** (a delayed release and a missed pull are indistinguishable from here) **· 2+ cycles = 🔴 DARK**, which no single delayed release explains. **There is no federal-holiday table and no release arithmetic.** → KB-VIO-243

> ## ✅ **2026-09-04 — FIXED IN CODE, AT THE THIRD ATTEMPT. The diagnosis below is kept verbatim; the two REMEDIES that followed it were both wrong and are recorded as such.**
>
> **The diagnosis (AM, below) was right: a `>9d` age rule false-DARKs a current ledger every Friday.** What followed:
> - **v2** — a fixed Tue-report / Fri+3d-release lag, certified *"zero free parameters, self-calibrating."* **WRONG:** federal holidays delay releases.
> - **v3** — added a holiday model asserting a **Monday** holiday slips the **report date** Tue→Wed. **WRONG, AND FABRICATED** — CFTC shows Tue 2024-09-03 and Tue 2023-09-05 straight after Labor Day, and **`COT_VIX.tsv` itself holds `2026-05-26`, a Tuesday directly after Memorial Day.** The falsifying evidence was in the ledger this guard reads.
> - **v4 (LIVE)** — **no calendar synthesis at all.** Observed cadence + grace, on the ledger's own dates: **0 = nothing owed · 1 late = 🟡 PENDING · 2+ = 🔴 DARK.** No holiday table, no release arithmetic.
>
> 🔑 **All three wrong versions passed their own selftests, because the tests were written from the same model as the code — a selftest cannot falsify the premise it was derived from.** The count went 14 → 24 while the premise got *more* wrong. **When a guard models an external schedule, test it against OBSERVED HISTORY first.** → **KB-VIO-243**
>
> ⚠️ **If precision is ever needed, ingest CFTC's published release calendar. Do NOT re-derive one — this desk has now tried twice.**
>
> ---
>
> ## 🔴 **2026-09-04 (AM) — DIAGNOSIS AS WRITTEN AT THE TIME: THE COT `>9 days` LINE IS MIS-SPECIFIED AND FIRES A FALSE DARK EVERY SINGLE WEEK.**
>
> `closeout_guard.py` blocked this session on *"COT VIX lev-money: COT_VIX.tsv last row 2026-08-25 = 10d old (contract: DARK >9d, weekly)."* **The measurement is correct. The threshold is wrong.**
>
> **Why it is structural, not incidental.** CFTC TFF report dates are **always Tuesdays**, released the **following Friday at 15:30 ET** — a fixed **+3-day publication lag**, verified against every report date in `COT_VIX.tsv` (`07-07 · 07-14 · 07-21 · 07-28 · 08-04 · 08-11 · 08-18 · 08-25`, all Tuesdays). The contract measures the age of the newest **report date**, so the age of a perfectly current ledger cycles:
>
> | When | Newest report date | Age | Contract verdict |
> |---|---|---|---|
> | Fri 15:30 → Sat | Tuesday, 3d prior | **3d** | 🟢 fresh |
> | Wed | Tuesday, 8d prior | **8d** | 🟢 fresh |
> | **Thu** | Tuesday, 9d prior | **9d** | 🟡 exactly on the line |
> | **Fri, before 15:30** | Tuesday, **10d** prior | **10d** | 🔴 **DARK — every Friday morning, forever** |
>
> ⇒ **A fully up-to-date COT ledger is guaranteed to breach this contract once a week.** Worked example (written Friday 2026-09-04): the 9/1-data report released that day at 15:30 ET. **Nothing is dark and nothing was missed.**
>
> 🔑 **WHY THIS MATTERS MORE THAN THE FALSE ALARM ITSELF: this is the fourth-plus RED on this file, and a guard that cries wolf on a fixed weekly schedule is training its reader to wave the red through** — which is precisely the *"boot printed it and the session did nothing"* failure `closeout_guard.py` was built to end. **A recurring false positive does not merely waste a look; it degrades the instrument's authority for the case where it is right.** `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]` cuts the other way here too: the remedy is **not** to relax the number until the noise stops, because that would silently raise the real-miss threshold as well.
>
> **THE CORRECT SPECIFICATION, DERIVED — ZERO FREE PARAMETERS, NOT A NUMBER I PICKED.** The contract's own intent is *"2× stated cadence."* For a series with a fixed publication lag the quantity to compare is **not** report-date age but **whether the most recent report date that has ALREADY BEEN RELEASED is present.** Expected newest report date = *the latest Tuesday whose following-Friday 15:30 release has passed.* DARK ⇔ the ledger's max date is **older than that**. This is self-calibrating, needs no constant, and never fires on schedule alone. *(A crude equivalent, if a scalar is wanted: `>17d` = 7d cadence + 3d lag + one fully missed cycle. Inferior — it hides the lag instead of modelling it.)*
>
> ✅ **FIXED 2026-09-04 PM (Will-directed) — the paragraph below was true when written and is kept as the record of the deferral.** ⛔ **NOT FIXED [AT THE TIME], AND DELIBERATELY SO.** Changing a live guard's threshold at the end of a session, on the strength of one session's diagnosis, is the ship-then-audit pattern this desk killed `GATE-VIO-RV1` for. **The diagnosis is written here where the next reader meets the red; the code change is queued.** ⚠️ **Until it is made, every Friday-morning boot and closeout will print this RED. That is expected. It is not permission to stop reading them** — the discriminator is the arithmetic in the table above: **age 9d or 10d against a Tuesday report date is the artifact; anything ≥17d, or a Friday-afternoon reading still showing the prior week, is real.** → **KB-VIO-226**

> 🔴 **THIS CONTRACT WAS UNENFORCED FROM v1.0 UNTIL 2026-07-28, AND THE FILE WAS BREACHING IT ON FIVE ROWS** — COT 21d, JPY 11d, OVX 11d, cheap-tail 6d, Tier-3 GEX **18d**. The sentence *"extend `ledger_staleness.py` coverage to this file's Tier-1/2 pull dates = a future small ask"* has sat here since v1.0 and **was never built**, so the only thing enforcing the contract was remembering to. **It wasn't remembered, and the instrument the map exists to protect — a canary going dark unnoticed — went dark inside the map's own text.** *(`finding_mechanize_the_cap_not_the_ritual`; the v1.0 cautionary tale was OVX dark through a war week, and the file then reproduced the failure in its own cells.)*
>
> **WHAT CLOSED IT — ✅ BUILT 2026-07-30, `scripts/canary_staleness.py`, boot-wired (this was the design, and it was right):** every Tier-1/2 row already states a pull source and cadence, and every Tier-1 instrument already writes a dated row to a workbook ledger (`VX_DAILY`, `JPY_VOL`, `COT_VIX`, `CHEAP_TAIL`). So the check is **not** a new data pull — it is comparing each row's asserted as-of date against the **max date in its own ledger**, which is a ~20-line addition to the existing boot staleness pass. **The data to enforce this has existed the whole time.**

**Dark rows remaining at v1.2:** **broad equity put/call** (WALTER-intake only, no direct pull) — queued, genuinely un-pullable rather than un-refreshed. *(OVX was the standing dark row at v1.0 — the "dark through the war week" cautionary tale — CLOSED 7/17: built, calibrated, boot-wired.)*

## Review cadence

- **Re-derive percentile thresholds** (JPY RV lines) at each calibration pass — they're window-anchored, not constants.
- **Row review:** at every thesis version bump + whenever a registered threshold shifts (same triggers as SIGNAL_INTAKE) + monthly staleness sweep.
- **Evidence column discipline:** append new worked/failed instances with KB row cites; a canary with two false fires gets demoted to Tier 2 pending recalibration.

*Registered sources cited per row: KB-VIO-034/081/090/096/098/102/105-108/110/112-116 · thesis predictions #2'/#6 · SIGNAL_INTAKE §ACTIVE THRESHOLDS · FLOW.tsv 7/1 COT band · scope memo `research/2026-07-11_jpy-vol-instrument-scope.md` · fresh-look memo `research/2026-07-11_move-led-vol-hedge-fresh-look.md` · `PROME/GATES.tsv` (canonical for action-gates). No threshold invented in this pass.*

---

*Reviewed September 14, 2026. Earlier refresh narratives are preserved in archive/sweep_2026-09-14/CANARY_MAP.md.*
