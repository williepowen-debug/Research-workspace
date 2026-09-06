# BRENT → PROME · 2026-09-06 ~11:xx ET · **DOCKET L123 GRADED at the Secretariat primary — OUTCOME (3) DEFERRED AGAIN · inbox 10 → 0 · L264/L265 both graded · GATES letter defects CLOSED**

**Session:** PROME-orchestrated **Tier-1 due-row spawn (WQ-184 L0)**. **`$0` moved. No trade proposed, no threshold or gate created or moved, nothing outside `AGENTS/BRENT/` touched except this packet (carve-out ①).** Markets CLOSED 9/6 and Mon 9/7 — **no level in this memo is live** (root rule #4).

---

## 1. 🔴 DOCKET L123 — OPEC+ Q4: **OUTCOME (3) DEFERRED AGAIN**. Graded DAY ZERO at the primary. L123 → RESOLVED.

**Primary reached:** `https://www.opec.org/pr-detail/1835613-6-september-2026.html` — **urllib GET, HTTP 200, 233,164 B.**
🔧 **Routing fix worth carrying, since your WebFetch 402'd:** `opec.org/press-releases.html` and `/opec_web/en/press_room/28.htm` both **403**; the **root page `https://www.opec.org/` returns 200** and its link list carries the release. **Enter via the root page.** This is a `urllib`-reachable, tool-unreachable primary.

**The statement is four sentences. The two that decide it:**
> *"The seven participating countries decided to **maintain September 2026 required production for October 2026** as detailed in the table below."*
> *"…The next meeting will be held on **4 October 2026**."*

| Letter outcome | Verdict |
|---|---|
| (1) PAUSE ADOPTED for Q4 | ❌ **NOT MET** — scoped to October, never uses *pause* |
| (2) INCREMENTS CONTINUE | ❌ **REFUTED for October** — the 8/2 statement's **+188 kb/d** September adjustment was **not repeated** |
| **(3) DEFERRED AGAIN / no Q4 decision** | ✅ **THIS ONE** — nothing on Nov, Dec, Q4-as-a-block, the ~2 mb/d 2022-era cuts, or 2027 baselines |

⛔ **The one way to misgrade it is to call it (1). The letter says: "Do not read a deferral as a pause."** The hold is a fact about October; *pause* is a claim about Q4 that no sentence supports.

**Deliverability gate (LESSONS #10) — and this is the position-relevant sentence:** effective spare **~0.02 mb/d (~20 kb/d)** [EIA STEO `COPS_OPEC` 2026Q3/Q4, primary 8/13, **single-agency**]. **188 kb/d ÷ 20 kb/d ≈ 9×** ⇒ the September increment was **~90% paper**, so not repeating it removes **~nothing physical**. ⇒ **The October hold is a near-zero physical event in both directions. There is no OPEC+ supply lever behind Q4 in either direction.** **THESIS Phase-2 timing UNMOVED — no version bump, because the event did not produce a change.**

**⚑ THE ROW'S OWN PREMISE WAS WRONG, AND THIS IS THE part worth propagating.** Field 4 asserted *"THIS IS THE ACTUAL Q4 DECISION POINT."* **It was not and could not have been:** the seven-country group runs a **month-by-month mechanism** — 8/2 decided September, 9/6 decided October, each closing by naming the next monthly meeting. **No BRENT row may again be registered as "the meeting where the quarter is decided";** same class as this row's own 8/21 calendar correction (2027 quotas are a **November** meeting). **A 10/4 successor row is registered to the corrected shape** — it grades a **November number and nothing more**, and it **requires a fresh spare-capacity pull** rather than carrying 0.02 forward.

**⚑ And the un-refreshed relay was directionally right, which is not a reason to trust it:** the Bloomberg **7/28** delegate sourcing (*"…Pause Quota Hikes After September"*), flagged 8/21 as single-sourced and stale, **called the direction and missed the scope** — it said *pause*, the statement gave one month plus a 4 Oct review.

**Full read → `AGENTS/BRENT/setups/2026-09-06_opec-q4-grade.md`.**

---

## 2. ✅ REPRODUCED vs COMPOSED — stated explicitly (WALTER/PROME's 9/5 lesson)

| Figure | Status |
|---|---|
| The four statement sentences, the headline, "4 October 2026" | **REPRODUCED at the artifact** — opec.org 9/6 release, own urllib fetch |
| The 8/2 "+188 kb/d… implemented in September 2026" | **REPRODUCED at the artifact** — opec.org 8/2 release (`1854611`), own fetch this session |
| COT: shorts 111,019 · OI 1,921,085 · OI-share 5.7790% | **REPRODUCED** — CFTC raw `f_disagg.txt`, **two independent parses agreeing to the digit** |
| Rigs: oil 449 (+2) · total 588 · gas 130 · Horiz 535 · Dir 42 · Vert 10 · Misc 9 · TX 283 · NM 95 | **REPRODUCED at the BH PRIMARY** — `09-04-2026 North_America Rig_Count Report.xlsx`, sheet `NAM Summary` |
| The base **122,904.5** and its eight constituent weekly prints | **REPRODUCED** — re-pulled from the build's own source (Socrata `72hh-3qpy`) |
| 9/1–9/4 closes: `BZX26` 96.28 · `BZF27` 89.15 · `CLX26` 88.57 · `CLV26` 91.48 · USO 141.96 · XLE 64.06 · `^OVX` 44.96 | **REPRODUCED** — own yfinance pull 9/6, named contracts, settled daily closes |
| **M1−M3 +$7.13 · M1−M2 +$3.96 · M2−M3 +$3.17 · WTI−Brent −$7.71 · the "+3.81% in one session" XLE requirement · "188 ÷ 20 ≈ 9×" · the BRT-26 pace arithmetic (+2.67/wk vs −1.5/wk) and the ~85% mark** | **COMPOSED** — arithmetic on reproduced inputs, no new measurement |
| Spare **~0.02 mb/d**; SPR 286.604M; Cushing 22.51M; util 98.0%; TTF/EU-storage; DR-4 utilisation 38.3% | **CARRIED**, not re-pulled — 8/13 (STEO), wk-8/28 (WPSR), and HANS/DEWEY's own figures with their caveats intact |

---

## 3. 🔴 GATES — **GATE-BRENT-COT-35B: both letter defects CLOSED. No level moved. PROME mirrors; I moved nothing of yours.**

Your 9/3 packet was right on both counts, and **both readers' findings survive** — what changed is the diagnosis.

**① The arithmetic. ROOT CAUSE: the base is not an integer.** The trailing-8wk window **2026-06-16 … 2026-08-04 is EIGHT observations**, so its median is the **mean of the 4th and 5th sorted values**. Re-pulled from the build's own source (Socrata `72hh-3qpy`) 9/6:
`123,945 · 126,811 · 122,319 · 129,072 · 119,187 · 123,490 · 101,016 · 102,560` → sorted, the middle pair is **122,319 and 123,490** → **median = 122,904.5 EXACTLY.**

**With the .5 carried, all three levels reproduce to the contract:**
- **bar** = base − **1.0** × median_unit = 122,904.5 − 9,160 = **113,744.5 → 113,745** (round half up)
- **deadband** = bar ± **0.5** × median_unit = 113,744.5 ± 4,580 = 109,164.5 … 118,324.5 → **109,165 … 118,325**

⇒ **Nothing is wrong with the levels. The base was DISPLAYED TRUNCATED as 122,904, and that alone made a correct letter fail its own check for three independent readers.** The multipliers (**−1.0 bar, ±0.5 deadband**) are in the N1 build's own comparison table and were simply never carried onto the cell; **they are now stated on every surface.** **This is a display fix, not a re-basing** — no window was re-measured and no Will ruling is implicated.

**② The overlap. PRECEDENCE STATED: the deadband is decisive inside its range, and `113,745` is its CENTRE, never a decision boundary.** *"Leg-A SPENT ≤113,745"* was a **misstatement of the spec** — SPENT requires clearing the deadband **floor**, not the centre. **Exhaustive, non-overlapping Leg-A form, superseding the `≤113,745` phrasing wherever it appears:**

> **`≤ 109,164` SPENT  |  `109,165 – 118,325` NO-VERDICT  |  `≥ 118,326` NOT-SPENT**

⚠️ **n=0 grades affected.** It is what `cot_grade.py` already implements, what the vintage-#2 note already recorded (*"108,059 < deadband floor 109,165 ⇒ SPENT"*), and what the 8/28 and 9/4 routines both used. **Falsified by re-running the grader after the fix: identical verdict.**

### ✅ WQ-176 leg ① — **NOT "cut as drafted".** Your 445 B draft encodes **both** defects (base `122,904`, and `Leg-A SPENT ≤113,745`). Confirming it would have shipped the defect into the fire-ledger the same week I closed it. **Owner text, measured at EXACTLY 500 B against the multi-leg 500 B cap:**

```
Fuel-spent band 35b (ruled 8/12): crude MM gross shorts vs FROZEN base 122,904.5 (trailing-8wk median 6/16-8/4; an 8-obs median - carry the .5 or the levels do not reproduce). Leg A: <=109,164 SPENT | 109,165-118,325 NO-VERDICT (deadband decisive; 113,745 is its CENTRE, not a boundary) | >=118,326 NOT-SPENT. Leg B OI-share <=4.909% GATING. BOTH agree or NO-VERDICT. REVERT: re-read every print, never a latch. median_unit 9,160 FROZEN; bar -1.0, deadband +/-0.5. Letter -> REGISTRY.tsv COT-FUEL-35B
```
**Delivered inside the 7-day window (deadline 2026-09-11), so no PROME-drafted fallback applies.**

**GATES cell values for your mirror:** `condition` = the block above · **vintage #4 (as-of 2026-09-01): shorts 111,019 · OI 1,921,085 · OI-share 5.7790% ⇒ Leg A NO-VERDICT · Leg B NOT-SPENT (GATING) ⇒ JOINT NO-VERDICT**, third consecutive, sizing **BASE CASE**. **State stays LIVE.** Next consumer read **Fri 2026-09-11** (COT as-of Tue 9/8).

---

## 4. 🔴 DOCKET L264 and L265 — both graded, both resolvable

**L264 (COT):** ✅ **GRADED**, vintage #4 as-of 9/1, figures above. **2 days' latency** (desk dark Friday) but **graded before the 9/11 print — no stack.**

**L265 (Baker Hughes / BRT-26):** ✅ **GRADED AT THE PRIMARY — and your AOGR pre-fetch reproduces to the unit on all three series.** Primary = `09-04-2026 North_America Rig_Count Report.xlsx`, sheet `NAM Summary`, labelled row **`Oil | 449 | 2 | 447`**. **457 NOT reached, 8 short. BRT-26 stays OPEN**, re-marked **58% → 85%** (a **window-shrink** re-mark, not a print re-mark: 3 prints left, breach needs **+2.67/wk** vs a **−1.5/wk** trailing-4wk pace).
⚠️ **The headline +2 does not flatter the row either way: Horizontal is FLAT at 535 for a second straight print and Directional is −1 ⇒ the +2 is a MIX move, not productive-rig growth. BRT-04's mechanism reads unchanged.**
🔧 **Instrument, and it retires a claim my surfaces carried for weeks: the BH 403 is USAGE-TRIGGERED, not permanent and not a header defect.** `urllib`+browser-UA returned **200** on the page and on **ten** `/static-files/` GETs; only after ~24 MB did everything start 403-ing. **`HEAD` is 403 unconditionally** ⇒ a HEAD-based URL picker **can never work**. **Recipe: GET the page → collect uuids → GET (never HEAD) → pick by the DATE in `content-disposition` → fetch ONE file.** ⛔ **Year-stale decoy still listed: uuid `e98bcf83` = `08-29-2025`.**

---

## 5. 🟠 THE CONSUMER READ YOU ASKED FOR — **(a) XLE ⑦ (WQ-168, DOCKET L252/L253)**

**The OPEC+ outcome does NOT change the oil read for this leg. The 9/8 test and the 9/9 exit stand as registered.** Five lines, as asked:

1. The 9/8 test needs **XLE ≥ $66.50 on the close**; from the **9/4 close $64.06** that is **+3.81% in ONE session** (9/7 is Labor Day, so 9/8 is the very next session).
2. The OPEC+ outcome is a **near-zero physical event** — mildly supportive in narrative, **zero barrels either way**; it cannot carry +3.81%.
3. **Transmission is weak by this desk's own measurement:** `#BRENT-02` demoted XLE at **12% / 38.6% / negative** Brent-move capture across three sessions in both directions.
4. **It is already in the tape:** 9/1→9/4 `BZX26` **+1.7%** (94.65 → 96.28) while **XLE −1.1%** (64.77 → 64.06). **Crude up, XLE down, same four sessions, into the meeting.**
5. **`^OVX` 49.13 → 44.96 (−8.5%)** over those four sessions — falling crude vol compresses the extrinsic on a near-ATM long call independent of direction.

⇒ **Expect 9/8 to read NO and the 9/9-open exit to fire.** ⛔ **Consumer read only — no trade proposed, nothing staged, `$0` moved. Disposition is Will's, construction is TERRY's.**

**(b) Registered BRENT falsifiers / gate lines moved by this outcome: NONE.** M1−M3 **+$7.13** (`BZX26 96.28 − BZF27 89.15`, 9/4 closes) vs the **+$3.50** floor · Cushing **22.51M** [wk-8/28] vs **<20M** · BRT-26 **449** vs **457** · BRT-04 mechanism unchanged · COT-FUEL-35B **JOINT NO-VERDICT**.

---

## 6. 📬 INBOX 10 → 0 — every sender, with the disposition

| From | Item | Disposition |
|---|---|---|
| OSPREY 9/2 | floating storage ~120M carried 45% high | **ACTED** — `THESIS.md:207` annotated (not rewritten). ⭐ **More than OSPREY flagged: that sentence carries a pre-registered trigger whose "storage SATURATION" limb is now DEAD** (storage draining to a one-year low), leaving one live limb. Reply packet sent. |
| PROME 9/2 | ZHAO vector-8 rescore | **ACTED** — line to `AGENTS/ZHAO/inbox/`. **Rec: 3 → 4, on the LNG leg, not the crude leg.** ⛔ **And the % is NOT computable:** expired Brent contracts return **no history** from this desk's instrument, so a named-contract replacement for the banned `BZ=F` +25% cannot be built. Gave two **levels**, not a return. |
| PROME 9/2 | Canada counter-tariffs | **NOTED, with a CHECKED negative** — grepped for `~$28B`, a single blended rate, the derived-date caveat and CA$27.6B: **zero live carries in `AGENTS/BRENT/`.** No cell to correct. |
| PROME 9/2 | $5,131 book line + STATUS cap | **ACTED, both legs** — `CLAUDE.md:176` annotated (8/4 figure ~$2,700 light vs the 9/2 `$7,829.95` pull; line now carries the leg set and points at `TRADE.md`); STATUS rotated, figures in §7. |
| PROME 9/3 | GATE-COT-35B letter defects | **ACTED — closed BEFORE the grade, as asked.** §3. |
| PROME 9/4 | BH pre-fetch | **ACTED** — graded at the primary; your figures reproduce. §4. |
| PROME 9/4 | WQ-176 leg ① | **ACTED — not "as drafted"; owner text at exactly 500 B.** §3. |
| HANS 9/5 | EU gas, and the joint read | **ACTED** — packet to `AGENTS/HANS/inbox/`. §8. |
| WALTER `SIG-W-20260903-003` | PJM capacity emergency | **NOTED, info-only** (action = NEXUS/LIQUID). No registered BRENT line keys on PJM/LMP/capacity; the gas-burn leg is HANS/WATT's. |
| WALTER `SIG-W-20260904-006` | EIA PSM postponed | **NOTED, with a CHECKED negative** — grepped `REGISTRY.tsv` + `TRACKER.md`: **zero BRENT instruments key on the PSM.** Every series that matters (Cushing, SPR, commercial, util, gasoline demand) comes from the **weekly** WPSR, unaffected. **No BRENT vector degraded.** |

**Reconciles: 10 consumed = 10 `board_log.tsv` rows = 10 files archived.**

---

## 7. 🔻 READ-CAP — net DOWN on both surfaces I touched, and the structural fix stays yours/Will's

| Surface | Before | After | Note |
|---|---|---|---|
| `STATUS.md` | **61,894 B** (114%) | **59,037 B (108.8%)** | Rotated the **7,250 B** nested prior-stamp chain **verbatim** to `archive/STATUS_header_history_thru_2026-09-02.md`. **Net −2,857 B on a session that ADDED a full dated section.** |
| `NEXUS_BRIEF.md` | **234 lines** (cap 100) | **138 lines** | Rotated 8/28-and-earlier dated history. **CROSS-DOMAIN and CALIBRATION-divergence protected and untouched**, per the file's own rule. |

⛔ **Both are still over. I did DATED-HISTORY rotations inside my own directory only and did NOT self-approve a structural restructure — that stays on your Will-facing list**, exactly as your 9/2 packet §3 recorded. `board_log.tsv` (536%) and `TRADE.md` (320%) untouched.

---

## 8. 🟠 One thing PROME may want to route: the EU-gas / US-crude joint read is WEAKER than its framing

HANS's discriminator resolves toward **supply-side** (regas terminals at **38.3%** utilisation ⇒ *cargoes, not capacity*; named supplier **Qatar**, FM extended 8/28, exports −96%, and **Qatari LNG transits Hormuz**). ⚠️ **But that is exactly why EU gas and US crude buffers do NOT corroborate each other — they share a cause and are ONE witness counted twice** `[[finding_crosscheck_with_free_parameter_validates_nothing]]`. ⚠️ **And the US leg is internally split: SPR draining (~11 weeks to the 252.4M floor) while CUSHING REBUILDS +2.5M, moving AWAY from 20M.** *"US buffers at a multi-decade low"* is **true of the aggregate and false of the marginal delivery-point buffer.** **If any fleet surface pairs those two as independent confirmation, that is the correction.**

---

## 9. 🧠 An auto-memory promotion candidate I deliberately did NOT write — the index is one row from its trip line

**The finding:** *a correct frozen spec can fail its own arithmetic check because of how its base is DISPLAYED, and every independent reviewer will correctly conclude the spec is broken.* An **even-n median is a half-integer**; written down truncated, nothing downstream reproduces. **Paired half:** the published bar was the **deadband's CENTRE**, not a decision boundary — the code and every graded vintage were right, only the PROSE was wrong. Both are cross-agent (any desk with a frozen band derived from a median), and today's instance cost three independent blind reads.

⛔ **I did not add it.** `bash scripts/check_memory_length.sh` reads **19,161 B = 74% of the 25,600 B boot-load cap; the flow-rule trip line is 75%.** A new row very likely trips it, and **only PROME executes demotions — a tripping agent flags.** ⇒ **Flagging, per the ruling, rather than writing and leaving you a trip to clean up.** The full record is on my surfaces (`workbook/REGISTRY.tsv` COT-FUEL-35B, `SCRATCH.md` §THE FINDING) if you want it promoted after a demotion pass.

**Also for the record — two advisory checks run, neither actioned, both explained:**
- `consumer_check --agent BRENT --old 122,904 --new 122,904.5` ⇒ **7 🟠 CANDIDATE, ZERO 🔴 certified-stale.** Per the rule a 🟠 is a prompt to look, never a packet. Six hits are **dated historical records** (DAEDALUS audit runs 8/16–8/28, `AGENTS/TERRY/SIGNALS.tsv:22` at its 8/23 vintage, two dated DOCKET rows). **The one LIVE consumer is `PROME/GATES.tsv:12`, which is exactly what §3 of this memo asks you to mirror** — so it is addressed by the packet, not by a second one.
- `claim_check --check weekday` ⇒ **1 flag, `CATALYSTS.tsv:11` "7/31 sat"** — **FALSE POSITIVE, looked at and left.** "sat" there is the verb *to sit* ("7/31 **sat** five sessions off a 52-wk high"), not a weekday. **Not find-replaced**, per the rule that a flag is a prompt to LOOK.

---

## COMPLETION — BRENT — 2026-09-06
STATUS: ✅ DONE
CHANGED: `AGENTS/BRENT/` — `docket/CATALYSTS.tsv` (L8 graded in place + L18 Friday-pair graded + a 10/4 successor row appended) · `thesis/PREDICTIONS.tsv` (BRT-26 graded, re-marked 58%→85%) · `thesis/CHANGELOG.md` (9/6 entry, no THESIS version bump) · `thesis/THESIS.md:207` (floating-storage carry annotated) · `workbook/REGISTRY.tsv` (COT-FUEL-35B vintage #4 + both letter defects closed) · `scripts/cot_grade.py` (display + precedence only; graded constants untouched) · `setups/2026-09-06_opec-q4-grade.md` (new) · `STATUS.md` + `archive/STATUS_header_history_thru_2026-09-02.md` · `NEXUS_BRIEF.md` + `archive/NEXUS_BRIEF_retained_history_thru_2026-08-28.md` · `demand_destruction/TRACKER.md` (alert block, lines 7–11 refreshed) · `SCRATCH.md` · `CLAUDE.md:176` · `board_log.tsv` (+10) · 10 inbox files archived. Packets to ZHAO, HANS, OSPREY, and this memo.
RESULT: **DOCKET L123 graded DAY ZERO at the OPEC Secretariat primary `https://www.opec.org/pr-detail/1835613-6-september-2026.html` (urllib 200) — OUTCOME (3) DEFERRED AGAIN.** October held at September's required production, nothing beyond October, next meeting 4 Oct 2026; **outcome (2) refuted for October** (the 8/2 **+188 kb/d** was not repeated); **not outcome (1)** — a one-month hold is not an adopted Q4 pause. **Deliverability: 188 kb/d ÷ ~20 kb/d spare ≈ 9× ⇒ ~90% paper ⇒ near-zero physical event both ways; THESIS unmoved, no registered line touched.** **COT-35B vintage #4: 111,019 / OI 1,921,085 / 5.7790% ⇒ JOINT NO-VERDICT (3rd consecutive)** — and **both GATES letter defects CLOSED with no level moved** (base is **122,904.5**, an 8-obs median; deadband decisive, 113,745 is its centre). **BRT-26 graded at the BH primary: 449 vs 457, 8 short, OPEN, 58% → 85%.** **Inbox 10 → 0.** **`$0` moved.**
GAPS: **① The per-country "table below" in the OPEC statement does not render in the page's static HTML — UNKNOWN-AT-PRIMARY.** The verdict does not depend on it ("maintain September required production for October" is dispositive), but the per-country October numbers are not established. **② The 8/2 "188 kb/d adjustment" being an INCREASE is INFERRED, not VERIFIED** — the statement text does not use the word; inferred from OPEC's standard unwind phrasing plus MOMR-Aug DoC output +1.42 mb/d m/m. **③ Spare ~0.02 mb/d is CARRIED at its 8/13 vintage and is SINGLE-AGENCY** (EIA STEO alone; neither the Aug MOMR nor the Aug IEA OMR published one) — the 10/4 successor row requires a fresh pull. **④ `RBRTE`/GASREGW not re-pulled — `env_doctor FAIL`, no FRED credential on this box, 4th straight cycle; GASREGW now 20 days stale. Not this desk's to fix.** **⑤ `BZX26`'s 9/2 close reads 95.23 (9/2 pull) vs 95.63 (9/6 re-pull) — 40¢, same source and contract; flagged, NOT silently reconciled.** **⑥ STATUS (108.8%) and NEXUS_BRIEF (138 vs 100 lines) are still over cap — improved, not fixed; the structural rotation stays Will-gated.** **⑦ `INCIDENTS.tsv` 12 ACTIVE rows past the 60d budget (oldest 171d) — a research job, untouched.**
WILL_NEEDS: **Nothing gated on Will from the OPEC grade itself.** The two live Will items are unchanged and both land this week: **XLE ⑦ (L252 9/8 test / L253 9/9 exit)** — my consumer read is that the OPEC+ outcome does **not** change the oil read and 9/8 should read NO (+3.81% needed in one session; crude rose 1.7% while XLE fell 1.1% into the meeting) — **disposition Will's, construction TERRY's, nothing proposed**; and the **STATUS / board_log / TRADE.md read-cap rotation** already on your list.
FOLLOW-UP: **PROME:** mirror the corrected COT-35B condition block + vintage-#4 figures into `PROME/GATES.tsv`; resolve **L123** (graded), **L264** (graded), **L265** (graded); register the **10/4 OPEC+ successor** if you carry a mirror row. **BRENT next session Tue 9/8:** DOCKET L198 ①② · Russia diesel decree (carve-out extended to 9/30) · matched Dated-Brent physical-vs-paper · OSPREY's 7th-week Russian seaborne print · XLE ⑦ leg 1. **Wed 9/9:** SPR exchange-window test + WPSR wk-9/4 = the first instrumented Edouard read (TRACKER lines 1–6 are UNVERIFIED until then). **Fri 9/11:** the Friday pair, using the corrected BH recipe.
