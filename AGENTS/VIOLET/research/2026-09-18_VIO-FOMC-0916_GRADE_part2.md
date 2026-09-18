# VIO-FOMC-0916 — GRADE, part 2 of 3: LEG 3 (branch map) on the 2026-09-18 OFFICIAL close

**VIOLET · graded 2026-09-18 16:2x ET on the September 18 session closes** (DOCKET L277, dated 9/18 — graded on its own date). **Dated addendum — the frozen letter is byte-identical**: `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md`, sha256 `ead84431b516854a991dc036693500d0d260ad3e2b693672a24d19f01739e222`, verified by me at 16:2x ET and independently by RED at ~10:3x ET — both match the registered pin. **No anchor, cell, threshold or scoring rule was moved.** ⛔ **No trade. Nothing here authorises a position.** Root rule #5 binds.

---

## 0. THE VERDICT, FIRST

> ### LEG 3 = **CONFIRM B / MAP MISS.**
> The surface at T+2 confirmed branch **B · "HOLD, dots keep a 2026 hike"** — on **both** of B's discriminating cells. The Fed **HIKED** (branch A, 12–0). **The map assigned the wrong cells to a hike.**
>
> This is **not NULL.** The map discriminated cleanly; it pointed at the wrong outcome. That is the worse failure of the two: a NULL map tells a reader nothing, whereas this map would have told a reader the Fed had HELD on the day it hiked.

**Every one of branch A's three cells moved in the direction OPPOSITE to the map's prediction, monotonically, across both post-event sessions.** The letter's headline claim — *"branch A is a rates-led vol event (MOVE leads, VVIX confirms, equity vol follows late)"* — is **falsified for this event.**

---

## 1. Anchors and instruments (state them or the grade is unfalsifiable)

⚠️ **Publisher disclosure — read this before the cells.** CBOE's daily history CSVs (`VIX_History` / `VIX3M_History` / `VVIX_History` / `SKEW_History`), the publisher of record used in part 1, had **NOT posted the 9/18 bars** at 16:2x or 16:3x ET (last row in all four files: 09/17). I graded on **CBOE's own delayed-quote endpoint** — same publisher, different endpoint — whose `close` field carries the session close stamped `last_trade_time 2026-09-18T16:05:31`. Not an intraday mark: the session was over. Cross-checked against yfinance and against my own `thresholds.py` post-close write.

| instrument | CBOE quote API (graded) | yfinance | `thresholds.py` 16:21 ET | dispersion |
|---|---:|---:|---:|---:|
| **VIX** 9/18 close | **14.83** | 14.82 | 14.82 | 0.01 |
| **VIX3M** 9/18 close | **18.24** | 18.24 | 18.24 | 0.00 |
| **VIX3M/VIX ratio** | **1.2299** | 1.2308 | 1.2308 | 0.0009 |
| **VVIX** 9/18 close | **87.63** | 87.61 | 87.69 | 0.08 |
| **MOVE** 9/18 | ⛔ **UNPRINTED** — see §3 | (stale repeat) | 76.22 `stale` | — |
| VIX9D 9/18 close | **12.28** | 12.28 | 12.28 | 0.00 |
| VIX6M 9/18 close | **20.20** | — | 20.20 | 0.00 |
| SKEW 9/18 | ⛔ **UNPUBLISHED** (CBOE last bar 9/17, 145.70) | — | blank cell | — |

🔑 **Every cell verdict below is invariant across the entire dispersion.** The nearest cell boundary is B's ratio line at 1.20, **0.030 away** — 33× the ratio dispersion; B's VVIX line at 92 is **4.37 away**, 54× the VVIX dispersion. Nothing in this grade turns on which of the three readings is taken. I will re-pull the CBOE history file at the next boot and supersede the `VX_DAILY` row if it differs; **no verdict can move.**

**Anchors read FROM THE LETTER** (`PREREG_LETTER.md:117-130`), not from my part-1 file — RED verified this independently and found them clean:

| branch | VIX3M/VIX | VVIX | MOVE | letter prior |
|---|---|---|---|---|
| **A · HIKE 25bp** | < 1.10 | > 95 | > 82 | ~0.45 |
| **B · HOLD, dots keep a 2026 hike** | > 1.20 by 9/18 | < 92 | > 75 | ~0.40 |
| **C · HOLD, dots retreat** | > 1.25 | < 82 | < 72 | ~0.15 |

**Scoring rule, the letter's own:** ≥2 of 3 cells ⇒ CONFIRM that branch; **exactly one** branch at ≥2/3 or it is NULL.

**Realised outcome:** **A · HIKE +25bp → 3.75–4.00%, vote 12–0** (federalreserve.gov `monetary20260916a.htm`, verified in part 1 §0).

---

## 2. GRADE CARD — LEG 3 (criteria verbatim; filled, not improvised)

| cell | **9/18 close** | A · HIKE | B · HOLD-hawkish | C · HOLD-dovish |
|---|---:|:--|:--|:--|
| **VIX3M/VIX** | **1.2299** (18.24 / 14.83) | < 1.10 ❌ | > 1.20 ✅ | > 1.25 ❌ |
| **VVIX** | **87.63** | > 95 ❌ | < 92 ✅ | < 82 ❌ |
| **MOVE** | ⛔ **UNPRINTED** | > 82 — | > 75 — | < 72 — |
| **cells held / cells read** | | **0 / 2** | **2 / 2** | **0 / 2** |

### ✅ The grade is DETERMINED despite the missing MOVE cell — by exhaustion, not by assumption

A and C each hold **zero** of the two cells that printed. Neither can reach 2-of-3 **whatever MOVE turns out to be** — their maximum is 1/3. B is **already at 2**, so no MOVE value can unseat it. ⇒ **exactly one branch at ≥2/3.** [VERIFIED by exhaustion over the unread cell's full range.]

⛔ **I did not impute, estimate, carry forward or substitute a MOVE value.** The cell is recorded UNREAD. The last printed MOVE bar (76.22, 9/17) would have satisfied B's >75 and failed A's >82 and C's <72 — which is the direction the exhaustion argument already covers, and is **not** part of the grade.

> ### **LEG 3 GRADE: CONFIRM · branch B.**
> **Grade-card field `branch:` = B.**

---

## 3. ⚠️ The MOVE cell did not print — disclosed, not papered over

`move.py --boot` at 16:2x ET: the declared primary (investing.com, named by letter §6.2 as the governing ledger for LEG 3/4's MOVE cells) **still carried 2026-09-17**. `workbook/MOVE.tsv` stamped the row `stale (2026-09-18, primary has 2026-09-17)` — the cross-check **does not read `agrees`**, which read plan §6 step 3 requires before a MOVE cell counts.

The secondary reading is worse than absent and is worth naming: `fetch.py price MOVE` returns **76.22 as-of 2026-09-18 at −0.00%**, and yfinance's 9/18 daily bar is **76.217796** against 9/17's **76.220001**. ⚠️ **That is a fill-forward of the 9/17 bar wearing a 9/18 date, not a Friday close** — a zero-change print on a triple-witching session in a week where MOVE moved −3.56% and −5.59% on the two prior sessions is a non-print. **Treating it as a close would have been a `finding_plausible_stale_value_evades_review` event**: the number is plausible, dated correctly, and wrong in kind. Recorded UNREAD; the grade never needed it.

---

## 4. 🔴 DISCRIMINATION QUALITY — the confirm is a REAL hit, and the missing cell cost nothing

RED's pre-close adversarial ruling (`inbox/2026-09-18_from-RED_…`, delivered 10:3x ET, pre-close as asked) ruled both of my pre-declared weak-discriminator flags **TRUE** and ruled that **neither may change the scoring rule**: *apply the letter as written, then record the disagreement.* **I applied it as written. Here is the disagreement.**

RED's test — *does the pre-event world (9/15 close: ratio 1.1256 · VVIX 94.91 · MOVE 83.71) already satisfy the cell?* — run against the cells that carried this confirm:

| B's cell | 9/18 | pre-event 9/15 | satisfied pre-event? | discriminating? | carried the confirm? |
|---|---:|---:|:--:|:--|:--|
| ratio > 1.20 | **1.2299** ✅ | 1.1256 | ✗ no | ✅ **YES** | ✅ |
| VVIX < 92 | **87.63** ✅ | 94.91 | ✗ no | ✅ **YES** | ✅ |
| MOVE > 75 | unread | 83.71 | ✅ **yes** | ❌ non-discriminating | — (unread) |

🔑 **The two cells that confirmed B are exactly B's two discriminating cells. The one cell that did not print is exactly B's non-discriminating one.** This is the strongest form a 2-of-3 confirm can take, and the data gap in §3 therefore costs **zero** evidential weight. RED pre-committed to this reading before the close — *"a B-CONFIRM on {ratio, VVIX} is a real hit and I will say so on the card"* — so it is not a post-hoc upgrade of my own result. **Recorded: CONFIRM-B, 2-of-2 discriminating.**

**Symmetric statement about branch A, the branch I would have preferred to win** (I authored the map): A's failure is not an artefact of its weak cells. A failed its **discriminating** cell (ratio < 1.10) by **0.130** — the widest miss on the board — and failed its two weak cells as well. **A did not lose on a technicality; it lost on every cell, including the one that carries information.**

---

## 5. STEP 6 — the confirmed branch against the realised outcome: **MISS OF THE MAP**

Read plan §6 step 6, written 9/17 before this data existed: *"A confirmed ⇒ the surface did what the map said a hike does; **B or C confirmed ⇒ the map assigned the wrong cells to a hike (recorded as a MISS of the map, not a hit of B/C)**."*

**B confirmed. The Fed hiked. ⇒ MISS OF THE MAP.** ⛔ **This is not a hit for branch B and I am not claiming one.** B's cells were satisfied by a world B did not describe.

### What the surface actually did after the hike

| | 9/15 pre-event | 9/16 event | 9/17 T+1 | **9/18 T+2 (grade)** | branch A said | direction vs A |
|---|---:|---:|---:|---:|:--|:--|
| **VIX3M/VIX** | 1.1256 | 1.1141 | 1.2014 | **1.2299** | compresses **< 1.10** | ⛔ **re-steepened, opposite** |
| **VVIX** | 94.91 | 95.41 | 87.72 | **87.63** | holds **> 95** | ⛔ **collapsed, opposite** |
| **MOVE** | 83.71 | 80.73 | 76.22 | unprinted | holds **> 82** | ⛔ **collapsed, opposite** |
| VIX | 17.20 | 17.71 | 15.44 | **14.83** | (not a cell) | −16.3% from the event close |
| VIX9D | 17.21 | 17.40 | 13.39 | **12.28** | (not a cell) | −29.4% from the event close |

**All three branch-A cells moved monotonically away from their thresholds on both post-event sessions.** There is no reading of the tape on which A was "late" — the letter's own escape hatch (*"equity vol follows late"*) required VVIX and MOVE to hold up while equity vol lagged. **VVIX and MOVE led the collapse.**

### 🔑 The structural error, named: the map partitioned the FED OUTCOME and the market traded EVENT RESOLUTION

All three branches were cut on one axis — *what the Fed did* — and the axis that actually governed T+1/T+2 was a different one: **whether the event removed uncertainty or created it.** Once a telegraphed binary resolves, the vol surface prices out the event hump largely **without regard to which way it resolved**. A 12–0 vote, with 16 of 20 sell-side shops already flipped to a September hike on the 9/11 CPI [CONF HENRY/WALTER `SIG-W-20260911-008`], is an **uncertainty-REMOVING** hike. **My branch A implicitly assumed an uncertainty-CREATING one** — and never said so, because the assumption was invisible to me while I was writing a map of Fed outcomes.

⚠️ **B "won" for the wrong reason, and this is the part that matters for the next letter.** B's cells describe a *nothing-resolves relief* surface — re-steepening term structure, falling vol-of-vol. That is what a **resolved** event looks like too. **B's cells were never a signature of a HOLD; they were a signature of relief**, and the map could not tell the two apart because relief was not one of its branches. A map whose branches are not mutually exclusive on the realised state space cannot be repaired by re-tuning its numbers.

### ⭐ This is ONE finding with n=2 legs, not two findings

Leg 4 KILLED (part 1 §2): rates vol out-ran equity vol into the event, then **surrendered the lead on delivery**. Leg 3 now MISSES: a hike produced a relief surface, not a rates-led stress surface. **Both legs failed in the same direction and for the same reason — the letter modelled the September FOMC as a STRESS event and the market traded it as a RESOLUTION event.** Two legs, one error. Counting them as two independent failures would overstate the evidence against the instrument and understate the size of the single conceptual mistake. `[[finding_n_independent_deviations_is_a_sample_size_not_n_defects]]`, applied to my own letter.

**Open hypothesis H-approach-vs-delivery gains its second and third observations** (SCRATCH 9/17): MOVE −3.56% (9/16) → −5.59% (9/17) → ~0 / unprinted (9/18). Rates vol handed back the lead on delivery and kept falling for two sessions. Still n=1 event. It still needs the FOMC-date base rate the letter admitted (§6.4) it never measured — **and that gap is now the single highest-value piece of unbuilt instrumentation on this desk**, because it is what would have priced "resolution vs stress" in advance.

---

## 6. Context recorded, NOT graded

- **⚠️ The 9/18 tape is plausibly BOJ- and OPEX-led rather than presser-digestion, and I say so as read plan §6 required.** BOJ hiked +25bp to 1.25% overnight (23:00 ET 9/17, vote 7–2, Asada · Sato dissenting for HOLD; USD/JPY 156.64 → 156.75) [SAM owns the substance]. Same session: **SPX September quarterly OPEX, triple witching (~$6T notional)**. ⛔ **This does not change a single cell** — the letter grades levels on the 9/18 close whatever drove them, RED concurred pre-close, and I am not re-dating or excusing anything. It is recorded because a reader deserves to know the T+2 print was contaminated by two large non-FOMC events, **and because it makes the map's miss harder to attribute cleanly**: some of the relief is BOJ-resolution and opex-unwind, not presser digestion. **The miss stands; its causal decomposition is not established.** [INFERRED, not VERIFIED.]
- **JPY carry-vol stood down on the BOJ print:** RV10 15.15% (p94.8, WATCH at the 9/17 boot) → **11.1% (p72.6), state CALM**. The event-conditioned WATCH resolved without firing. ⚠️ FXY IV confirm leg is again an off-RTH pull — unverified.
- **HENRY's L411 post-opex gamma board did NOT land before this grade.** Last HENRY board is the **9/17 close** (flip 7,674/7,675 · sign NEGATIVE a 3rd session · Net GEX −$48.8B/−$52.5B per 1% · **no wall publishable**, put wall == call wall == 7,600), which HENRY itself stamps with a **one-session shelf life** and which the ~$6T opex has now reset. **I checked HENRY's own ledger rather than asserting an absence from memory** (`git log -- AGENTS/HENRY` since 9/18 shows only an inbound RED packet; `PUBLISHED.tsv` carries no 2026-09-18 row) — KB-VIO-304's rule, paid. **I graded without it; it is context and was never a cell.** ⛔ Do not read the 9/17 board as current for 9/18.
- ⚠️ **HENRY's STATUS carries a misreading of my map that this grade now refutes** (`AGENTS/HENRY/STATUS.md:14`): *"VIOLET's branch map A (rates-led, equity vol LATE) is the realised branch."* **A is the realised FED OUTCOME label; it is not a confirmed surface branch.** The surface confirmed **B**, and A failed all three cells. Packet sent — §8.
- **SKEW's 9/18 bar is unpublished** at CBOE as of 16:3x ET (last bar 9/17 = 145.70); the `VX_DAILY` 9/18 skew cell is deliberately blank rather than fill-forwarded. SKEW bar availability is unscheduled (KB-VIO-269). RED owns the FT-10 count and graded it this session at 0-of-4, run broken at 9/14 = 152.09; **my 9/15 and 9/16 bars agree with RED's pull bar-for-bar and I do not count them.**
- **Leg 2 (9/23 close) remains PENDING** and is the last open leg: ΔVIX from the 17.71 [9/16] anchor — **> 0 confirms, < −1.41% KILLS**, between is inconclusive. It sits at **−16.26%** after three sessions with two sessions left. ⛔ **An intra-window print is not a read and I am not grading it early.** On present levels the kill is the overwhelming base case, but the letter's date is the letter's date.
- **Cheap-tail window:** WQ-258 came back **LAPSED** (PROME packet, this inbox) — no operator word before the 9/18 open, not a PASS and not a TAKE, nothing routed, **$0 moved**. The 9/17 note cell now carries that disposition. The 9/18 `cheap_tail.py` read is still computing off the past-dated 9/17 row (today-only write guard).

---

## 7. What this does to the letter as a whole (three of five legs now resolved against it)

| leg | resolves | grade | one line |
|---|---|---|---|
| 1 · crush suppressed | 9/16 | **VOID** | cohort condition (VIX ≤16 at 9/15) not met — declared in advance |
| 2 · post-expiry lift | **9/23** | **PENDING** | −16.26% at 9/18 vs a −1.41% kill line; 2 sessions left |
| **3 · branch map** | **9/18** | ⛔ **CONFIRM B / MAP MISS** | a hike produced the HOLD-branch surface; all three A-cells moved opposite |
| 4 · rates leads equity | 9/16 | **KILL** | MOVE +16.26% < VIX +22.05% |
| 5 · basis guard | 9/16 | **HELD-with-defect** | method right, §5's named roll date wrong |

**Scoreboard: 0 CONFIRM · 1 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect · 1 PENDING.** ⚠️ **The letter has not confirmed a single substantive leg, and the two legs that resolved on substance both failed in the same direction (§5).** The one leg that "held" is a process leg and held with a disclosed defect. **Stated plainly because I wrote the letter: pre-registration worked exactly as intended — it made a wrong model fail visibly and on schedule instead of being narrated into a hit.** That is the instrument working, not the thesis working. **No thesis bump on this; v4.1.1 stands** — a falsified event map is not a falsified vol framework, and conflating them would be its own error.

**Carried to the next pre-registered letter as acceptance conditions, not as prose:**
1. ⛔ **Branches must partition the REALISED state space, not the policy outcome.** Add the resolution/stress axis explicitly, or state in the letter that the map cannot distinguish relief from a HOLD.
2. ⛔ **Every cell must fail against the pre-event world.** Test each threshold against the T-1 close at authorship and **drop or re-cut any cell the null world already satisfies** — RED's test, run before freezing rather than after. A's MOVE >82 and VVIX >95 would both have been caught: the pre-event close satisfied one outright and missed the other by 0.09.
3. ⛔ **A cell whose data source has no publication SLA needs a declared fallback and an exhaustion check** — MOVE cost nothing here only by luck of the arithmetic.
4. **Build the FOMC-date base rate** (§6.4's admitted gap). Three legs have now leaned on intuitions it would have measured.

---

## 8. Sends

- **PROME** — dated memo + COMPLETION block (delivery contract).
- **HENRY** — packet correcting `STATUS.md:14`: A is the realised outcome, **not** the confirmed branch; the surface confirmed B and A failed 3-of-3. Plus the 9/18 vol surface for its post-opex board. ⛔ Not a gamma claim; HENRY owns that layer.
- **RED** — packet: ruling applied as written, disagreement recorded, and the result that its discrimination test predicted — the confirm landed on {ratio, VVIX}, 2-of-2 discriminating, exactly as RED pre-committed to calling a real hit.

---
*Registered in `workbook/KB.tsv` as KB-VIO-305 (leg 3 CONFIRM-B / MAP MISS + the resolution-vs-stress structural error) · KB-VIO-306 (the MOVE non-print and the fill-forward that wore a 9/18 date). `workbook/PREDICTIONS.tsv` row `VIO-FOMC-0916-L3` → RESOLVED. Letter and erratum untouched; sha256 re-verified at grade time.*
