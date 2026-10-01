# BRT-31 — Path-B successor: ADJUSTED DRAFT v2 for Will (after CARL's blind read)

> ✅ **REGISTERED 2026-10-01 as `BRT-31` (WQ-346 RULED, Will 9/30 19:32 ET blanket word via PROME `be8b72644`) — v2 AS WRITTEN. §2 below is the governing letter; the "NOT REGISTERED" status line that follows is the 9/30 draft-time record, kept verbatim.** Row: `thesis/PREDICTIONS.tsv`; note: `thesis/prediction_notes/BRT-31.md`.

**Status: DRAFT v2. NOT REGISTERED.** Written 2026-09-30 12:1x ET by BRENT. **Why not registered:** Will ruled WQ-345 at 11:55 ET, verbatim *"OK APPROVED"*: second reader first, then register **as written** unless the read forces a change to the bar, window, precondition, contamination clause or confidence (PROME packet `5fb52ac67`). CARL's blind read (`AGENTS/BRENT/inbox/2026-09-30_from-CARL_blind-second-read_BRT-31-draft.md`, `13aa2cd46`) found **two findings that force changes (❌1 base rate/confidence, ❌2 outcome precedence)**. ⇒ **This goes back to Will as a new decision.** v1 stays as the record: [`2026-09-30_BRT-31-path-B-successor-DRAFT.md`](2026-09-30_BRT-31-path-B-successor-DRAFT.md). $0.

## 1 · What changed from v1 (each tied to CARL's finding)

| # | v1 | **v2** | CARL | Forces Will's word? |
|---|---|---|---|---|
| a | No outcome precedence; the policy-cut result state had no name | **First terminal event in data-week order wins; a same-week tie goes to NOT-FIRED** (refusal wins ties). Contamination result named **NO-VERDICT-CONTAMINATED** | ❌2 | **Yes** |
| b | Base rate ignored the letter's own in-window precondition; confidence 30% vs a 36% base | Base rate **graded by the letter itself** (§3). Confidence **40%** vs a 46% base | ❌1 | **Yes** |
| c | Window: data weeks ending 10/2 → 11/20 | **Data weeks ending 10/9 → 11/27, fixed at the ruling, never moved.** The 10/2 print's 4-week average contains Labor Day week on the 2026 side only (Labor Day 2026 falls in w/e 9/11; its base week w/e 9/12/2025 has none) ⇒ a one-sided ~−0.4 pp push toward MET. From w/e 10/9 no window print contains it. **Thanksgiving is aligned** in w/e 11/27/2026 vs w/e 11/28/2025 | ⚠️6 (and ❌3 made moot) | **Yes** (window) |
| d | "Other policy action that lowers pump prices" (open class) | **Closed list** (§2) | ⚠️8 | Yes (part of a) |
| e | Rounding/vintage unnamed | **Unrounded computed value from the first-published psw01 print governs** | ⚠️9 | No (basis) |
| f | Price-check mapping unnamed | **GASREGW on the Monday after each data week vs the observation 364 days earlier**; fallback EIA's weekly retail series (the same survey) | L13 | No (basis) |
| g | Labels | **MET = "weakening measured", never "destruction confirmed". NOT MET = "volume resilient", never "consumer resilient"** (CARL's consumer-desk read: pump buyers can hold miles while stress rises) | Q5 | No (label) |
| h | — | **Recorded post-grade checks, NOT legs:** EIA monthly `MGFUPUS2` for Oct–Nov (weekly runs ~2.3 pp sd from monthly); any US Gulf named-storm/refinery outage in the window is named beside a MET | ⚠️10, ⚠️11 | No (record) |
| i | "Today +23.2%" | "12-week minimum +23.2%; **latest +43.2%** ($4.465 on 9/28 vs $3.118 a year earlier)" | ⚠️7 | No (wording) |
| j | "Ordinary" column = all starts | Truly ordinary (12-wk minimum price YoY < +20%), n=970 | ⚠️12 | No (label) |

## 2 · The letter (v2)

| Field | Text |
|---|---|
| **Claim** | US gasoline demand weakens measurably under the sustained price shock: **EIA gasoline product supplied (`WGFUPUS2`), 4-wk average vs the same 4 weeks 52 weeks earlier, ≤ −1.5% on two consecutive data weeks** in the window. |
| **Series / basis** | EIA WPSR psw01.xls "Data 2" `WGFUPUS2`; unrounded computed value; the **first-published** print governs (later revisions are recorded, never re-grade). Method reproduces EIA: wk-9/11 −1.0119%, wk-9/18 −0.7798%, wk-9/25 +0.2587%. |
| **Window** | **Data weeks ending 10/9, 10/16, 10/23, 10/30, 11/6, 11/13, 11/20, 11/27** (releases Thu 10/15 12:00, Wed 10/21, 10/28, 11/4, Thu 11/12 12:00, Wed 11/18, 11/25, ~12/2). Fixed at the ruling, never moved. "Consecutive" = consecutive data weeks; a data week EIA never publishes breaks consecutiveness and is not replaced. |
| **Evaluation order** | Data-week order. At each week: **(1)** price check: if this is the **3rd** window week with GASREGW YoY < +20% ⇒ **NOT-FIRED-PRECONDITION** (terminal; excluded from calibration; recorded for Path A). **(2)** If this week and the previous one are both ≤ −1.5% ⇒ **MET** (terminal). **Same-week tie ⇒ NOT-FIRED.** |
| **At window end** (no terminal event) | **NOT MET** if every print > −1.0%. Otherwise **NO-VERDICT** (a real answer). |
| **Contamination (closed list; can only refuse NOT MET)** | Takes effect **inside** the window, dated by the instrument's own effective date: **(i)** a suspension or cut of the federal gasoline excise tax; **(ii)** state gasoline-tax suspensions/cuts in states totalling ≥ 10% of US gasoline consumption (EIA SEDS shares). **Not on the list:** SPR releases, RVP/E15 waivers, export restrictions (supply actions, not pump-price policy). If one takes effect and no MET has been declared, NOT MET is unavailable and the end state is **NO-VERDICT-CONTAMINATED** (excluded from calibration). MET still grades. |
| **Excluded weeks** | None. |
| **Confidence** | **40%**, meaning P(MET \| not NOT-FIRED), consistent with BRT-29's convention that NOT-FIRED is excluded from calibration. |

## 3 · Base rate v2: graded by the letter [CONF EIA `WGFUPUS2` + FRED `GASREGW`; `research/2026-09-30_path-b-successor/baserate_v2.py`]

Same sample as v1 (1993–2025, excluding 2020-03 → 2021-12 observation weeks and all of 2026). High-price = GASREGW YoY ≥ +20% in each prior 12 weeks; start ≥ −0.5%.

| −1.5% bar | Windows | NOT-FIRED | **If fired: MET · NOT MET · NV** | Equal weight per episode (10 clusters) |
|---|---|---|---|---|
| **High-price (the letter)** | 88 | 22% | **46 · 32 · 22** | MET 43 · NOT MET 30 |
| High-price ex-2022 (COVID-era base, CARL ⚠️5) | 75 | 25% | 45 · 30 · 25 | MET 40 · NOT MET 29 |
| **Truly ordinary** (no precondition applied) | 970 | — | **15 · 66 · 19** | — |
| *(−2.0% bar, for comparison: high-price 30 · 34 · 36; ordinary 11 · 66 · 23)* | | | | |

- **Separation holds under every cut:** MET ~3× likelier in a shock than in ordinary times (46 vs 15); NOT MET about half as likely (32 vs 66).
- ⚠️ **About 8 price episodes, and 1999–2000 alone is 34 of 88 starts** (CARL ⚠️4). The equal-weight row is the honest centre: **MET ~43%**. Keep ±10–15 pts on every figure.
- ⚠️ **Noise floor:** 15% of ordinary windows hit MET too, and some of those were hurricane or weekly-estimate artefacts (CARL: 2005-09, 2012-09→11, 2016-12, 2023-09, 2024-02). Hence two consecutive weeks, the recorded monthly cross-check, and the "weakening measured" label.
- ⚠️⚠️ **Why v2's equal-weight MET (43%) is far above CARL's v1 figure (26%), and both are right:** I reproduce CARL's **26 / 31** exactly under v1 rules (no in-window precondition). Under v2 the precondition **cancels the short episodes where the shock faded**: 2000-11, 2004-07, 2004-12 and 2006 entirely, and 6 of 8 starts in 2010. Those were the NOT MET/NV episodes. **⇒ v2's 43% means "MET, given the price shock persisted", resting on only 6 surviving episodes:** 1999–2000 (14/34 MET), 2003 (6/10), 2007–08 (0/5), 2010 (0/2), 2011 (5/5), 2022 (7/13). It is a legitimate conditional (the letter only grades if the shock persists) and a **thin one: two episodes are all-or-nothing.**
- **CARL's 27% NOT-FIRED / 42% MET** comes from a different tie rule (precondition over the whole window); **both reproduce for their own rule.** v2 fixes the rule so there is one answer.

## 4 · Confidence 40% (base 46%, equal-weight 43%)

**Down from the base:** L12 (longer EV-era adjustment); the current trend is rising (4-wk YoY −1.61% on 8/28 → +0.26% on 9/25; the single week of 9/25 is +2.0% vs a year ago). **Up:** the shock is larger than the +20% floor (latest +43%), and diesel retail is $6.38 (9/28, FRED GASDESW). Same −6 pt adjustment as v1, now from the correct base. ⚠️ **The base rests on 6 episodes** (§3), so 40% carries at least ±15 pts. If Will prefers the unconditional equal-weight view (CARL's 26% under v1 rules), a mark near 25–30% is defensible, and the choice is his.

## 5 · Lessons (`lessons_check.py --spec` run on this file before sending)

L06, L08, L09, L12, L21, L22, L23, L25: dispositions unchanged from v1 §5 (volume test, data-week anchor, no futures, a failed retrieval never grades). **L27: satisfied.** CARL's blind read caught the base-rate/letter mismatch and the precedence gap, and both were my own support errors.

## 6 · What Will decides

1. **Approve v2 as written.** Registration then follows on his word, with the window fixed at data weeks 10/9 → 11/27; the first print is Thu 10/15.
2. **Or keep v1's 10/2 start** and accept the small Labor Day push toward MET. Changes (a) and (b) are needed either way.
3. **Or adjust** the bar or confidence (§3 gives the cost).
