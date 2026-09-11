# SAM → PROME · 2026-09-11 01:0x ET · **VECTOR 5 — JAPAN UNDER $108 BRENT: the answer is NONE, and the arithmetic says why**

**Carve-out ① self-authored packet.** DOCKET L328, executed tonight on Will's 00:29 ET word. Report-before-execute: NO card, NO order, $0, book FLAT, no threshold or confidence moved except on my own registered letters.

## COMPLETION — SAM — 2026-09-11
STATUS: ✅ DONE
CHANGED: AGENTS/SAM/STATUS.md, MEMORY.md, NEXUS_BRIEF.md, thesis/PREDICTIONS.tsv, docket/CALENDAR.md, workbook/KB.tsv, workbook/BOJ_MEETING_OIS.tsv, workbook/boj_ois_reviews/2026-09-11T1115-JST.json, workbook/JGB_YIELDS.tsv, board_log.tsv, inbox/WALTER/processed/ (5), PROME/inbox/ (this), AGENTS/WALTER/inbox/ (1 stale-figure packet)
RESULT: VERDICT **NONE** — no tradeable Japan instrument in this stack. Oil cannot flip Japan's current account: July CA **+¥2,988.9B** against a **¥1,408.9B/month** crude bill means the oil-in-yen proxy must rise **212%** (Brent ≈ **$309** at ¥154) to zero the surplus; the $108 shock adds ~**¥120B/month** (+8.5% proxy), **4.0%** of one month's surplus. Sep BOJ is **98% priced** at my own re-pulled primary (Totan 9/11 11:15 JST) — the residual surprise is a HOLD, which is yen-NEGATIVE. Across two oil-shock sessions Sep stayed 98% while the FORWARD path was SHAVED (cumulative 2.63→**2.59**): the market reads oil as dovish-for-pace.
GAPS: Bloomberg 9/6 "Japan Likely Sold Treasuries" primary PAYWALLED (bloomberg.com + Japan Times mirror both HTTP 402) — body stays SEARCH-NOT-FOUND; figures recovered from the search abstract and cross-checked at my own MOF primaries. Japan August trade balance (the honest discriminator) does not print until 9/16 08:50 JST.
WILL_NEEDS: None.
COMMITS: `eb31d5946` (domain work — STATUS/MEMORY/CALENDAR/PREDICTIONS/KB/board_log/OIS review/inbox moves) · `a188c0a8e` (NEXUS brief fold, folded AFTER the STATUS commit per schema Amendment 10). NO PUSH — PROME-spawned session; PROME pushes at closeout.
FOLLOW-UP: 9/16 08:50 JST Japan August trade balance — read crude **VOLUME**, not value; it is leg (a) of the pre-registered re-open test below. 9/18 BOJ: read the VOTE SPLIT and whether the statement names oil, not the rate.

---

# THE ONE PAGE

## VERDICT FIRST: **NONE.** No instrument. Five reasons, in order of how hard they are to argue with.

**1. The arithmetic forbids the transmission.** [own computation from `workbook/TRADE_BALANCE.tsv` 2026-07 kakusoku + MOF `bp202607.pdf`; VERIFIED]

| Leg | Figure | Source / date |
|---|---|---|
| Japan crude imports, July | 12,106 kKL = **76.1 M bbl/mo ≈ 2.46 mb/d** | MOF customs, 2026-07 kakusoku |
| Crude import VALUE, July | **¥1,408.9B/month** | same |
| Oil-in-yen proxy, July average | **¥15,291/bbl** (Brent $94.1 × ¥162.5) | matched-basis proxy, THESIS §OIL-IN-YEN |
| Oil-in-yen proxy, NOW | **¥16,594/bbl** (BZ=F $107.52 × USDJPY=X 154.33) | fetch.py, 2026-09-11 05:0x UTC |
| Change | **+8.5%** = oil **+14.3%**, yen **−5.0%** | the yen leg has absorbed **~40%** of the oil move |
| Incremental crude bill | **+¥119.8B/month ≈ +¥1.44T/yr** | July bill re-priced on the proxy ratio |
| July current account | **+¥2,988.9B** (primary income +¥4,289.6B) | MOF `bp202607.pdf`, rel 9/8 |
| ⇒ the shock as a share of the CA surplus | **4.0% of ONE month** | — |
| ⇒ oil-in-yen needed to ZERO the CA surplus | **+212% → ¥47,700/bbl ≈ Brent $309** at ¥154 | (incl. LNG: ~$251) |

**Japan's current account is a primary-income surplus with a goods deficit bolted on.** The oil channel is too small to reach it by roughly an order of magnitude. This is the same arithmetic that killed **SAM-15 @80% (FAILED)** — "oil-in-yen forces repatriation independent of rate differential" — which died three ways: premise evaporated, **mechanism inverted** (supply destruction → trade SURPLUS, not deficit; KB-SAM-176), insurers *grew* foreign books. $108 does not revive it. ⚠️ Caveat held against my own case: the proxy excludes freight, and freight is spiking (WALTER SIG-018, BWET +6.04% 9/9) — so the landed bill is UNDERSTATED here, in the direction of my counterparty. It is not understated by 20×.

**2. The hike is 98% priced, and the residual surprise has the WRONG SIGN.** My TFX/OIS primary, **re-pulled tonight** (Totan ICAP indicative meeting-OIS median, image SHA `45825f9d…`, publisher stamp **2026-09-11 11:15 JST**, transcribed and ingested this session):

| Meeting | 9/10 11:15 JST | **9/11 11:15 JST** | Δ |
|---|---|---|---|
| **2026-09** | 98% | **98%** | **0** |
| 2026-10 | 28% | **25%** | −3pp |
| 2026-12 | 62% | **61%** | −1pp |
| 2027-01 | 35% | **36%** | +1pp |
| 2027-03 | 42% | **40%** | −2pp |
| **cumulative expected hikes** | 2.63 | **2.59** | **−0.04** |

Sep OIS 1.2213%, unchanged to 4dp. ⚠️ Indicative OTC medians, model-dependent, **not traded probability**; incremental 25bp equivalents ≠ cumulative hike counts. **Read the table, not the headline:** September did not move one basis point across a **+5.6%** Brent session (9/10) and a $107–108 hold (9/11) — while the FORWARD path was SHAVED. The market is pricing the oil shock as a **terms-of-trade TAX that is dovish for the PACE**, not as an inflation impulse that is hawkish. [INFERRED — n=2 sessions, small magnitude, no causal attribution claimed.] At 98%, a hike pays nothing and the only surprise left is a **HOLD**, which is **yen-NEGATIVE** — the opposite side from "oil shock hurts Japan." You cannot build a falsifiable edge against a 98% print.

**3. The last data the BOJ sees before 9/18 contains NONE of the oil shock — and shows terms of trade IMPROVING.** August CGPI, own primary, BOJ `cgpi2608.pdf`, released **2026-09-11 08:50 JST** [VERIFIED]:
- PPI **−0.2% m/m / +7.6% YoY**
- Import Price Index, **yen basis: −3.0% m/m / +24.8% YoY**; contract-currency basis **−1.0% m/m / +16.7% YoY**
- **Petroleum, coal and natural gas contributed −1.18pp** to the contract-currency monthly fall (crude petroleum, naphtha, LPG) — oil was the single largest DRAG
- FX rate column **−2.4% m/m** (negative = yen appreciation)

In August, Japan's import prices fell **in both currencies**, oil led them down, and the yen strengthened. The September shock reaches **zero** of the 9/11 CGPI, the 9/16 trade balance or the 9/18 National CPI. The BOJ decides on pre-shock data plus forward judgment — and Masu (9/10, primary) already keyed the PACE to oil.
🔧 **Vintage correction, mine, flagged against my own surface:** today's primary shows **July PPI +7.7% r** and **June +7.4%**. SAM's STATUS carried **7.2% [Jul] / 7.1% [Jun]** from the 8/13 release. The old pair is superseded at the primary — fixed in STATUS this session; do not cite it.

**4. There is no US-listed instrument whose P&L is Japan's oil import bill.** Every candidate is a rate proxy or a yen proxy wearing an oil costume. [all quotes fetch.py; ADR/ETF marks 9/10 close, FX/Brent 2026-09-11 05:0x UTC]

| Candidate | Mark | What is actually priced | Falsifier / why it fails |
|---|---|---|---|
| **FXY** $59.40 / **YCS** $51.57 | 9/10 | the 98% hike, in full | Retired as a vehicle; ETF-proxy ATM IV 14.38% is **not** underlying FX vol (KB-183: read sign, not level). No edge against 98%. |
| **MUFG** $23.29 **+0.65%** · **SMFG** $26.55 **+0.91%** · **MFG** $11.06 **+1.10%** | 9/10 | the rate path — cumulative **2.59** hikes to Mar-2027 | ⚠️ On the **+5.6% Brent day** the banks **ROSE** while EWJ fell −0.58%. They are already long the leg the market just **marked down** (2.63→2.59). Confounded by US rates (^TNX 4.92–4.94, 9/10). A rate trade, not an oil trade. |
| **JGB futures** | — | — | **SEARCH-NOT-FOUND:** no US-listed expression. OSE/SGX only. Structurally unavailable. |
| Japanese **importers / utilities** (the actual victims) | — | — | **No liquid US listing.** The US-listed Japan set is bank- and exporter-weighted. |
| **DXJ** $173.47 / **EWJ** $96.44 pair | 9/10 | the yen, again | DXJ is currency-**HEDGED** and exporter-tilted — long yen WEAKNESS, not long the oil bill. The pair is the same 98%-priced yen bet at worse cost and tracking drag. |

**5. Correlation, not instrument selection.** The energy sleeve is **already** one "Mideast stays hot" bet (~**$6,007** at the 9/10 close). A Japan-oil expression is a **second helping of the same bet** — it adds notional to the same underlying, not diversification. That argument stands even if reasons 1–4 were all wrong.

## Root rule #6
Nothing to place, so no day-colour test applies today. If this ever became a card it would be a **PUT-side** expression (short yen / short Japan equity) and root rule #6 would demand a **GREEN day at the actual instrument** — note 9/10 was RED for EWJ (−0.58%) and GREEN for the bank ADRs on the same tape, so "Japan was green/red" is not a usable reading. Construction is TERRY's (Non-Negotiable #1: TERRY owns the card); Will approves (root rule #5).

## What would change my mind — PRE-REGISTERED so this is not an open-ended maybe. ALL THREE, or the answer stays NONE.
| Leg | Test | State today |
|---|---|---|
| (a) | Japan **August trade balance, 9/16 08:50 JST**: crude **VOLUME** up YoY (July +5.5%) — Japan paying more **and lifting more**, i.e. supply destruction is NOT inverting Phase 1 | **UNKNOWN** — prints 9/16 |
| (b) | Oil-in-yen proxy **≥¥18,000/bbl on 5 consecutive completed sessions** (= Brent ~$117 at ¥154, or $108 at ¥167) — a LEVEL, not a spike | **FALSE** — ¥16,594 |
| (c) | USD/JPY **weakens through 158** on the yfinance `USDJPY=X` completed-session close basis **while Brent holds** — the terms-of-trade channel moving the currency, rather than the rate differential moving it | **FALSE** — 154.33 and strengthening |

Leg (c) is the one that matters and it is currently running the **wrong way**: the yen has gone 160.19 [9/1] → 154.33 [9/11] *through* the oil shock. A currency that strengthens into its own terms-of-trade shock is telling you the rate differential, not the oil bill, owns the price.

---

## L34 — BOJ MPM 9/17–18 PRE-READ (delivered on this touch, as scheduled)
- **Priced: 98% for +25bp to 1.25%** (own primary above). Officials aligned from every direction: Masu 9/10 (primary — rate "below the estimated range" 1.1–2.5%, "will continue to raise", pace keyed to **oil**, AI demand and FX), Ueda 9/2, Takata 9/2, Himino 8/26, Aida 9/7, Katayama 9/8; Reuters via FXStreet 9/11 "set to raise by 25bp next week."
- **The asymmetry, unchanged since 9/1: the SURPRISE is a HOLD, and it is yen-NEGATIVE.** ~2% probability, large move.
- **What to read on 9/18 — not the rate:** ① the **VOTE SPLIT** — a 2+ dissent *for a faster pace* is the only hawkish surprise left; ② whether the statement **names oil**, and HOW: framed as a downside risk to activity it is **dovish for the pace** (and confirms the 2.63→2.59 shaving); framed as a second-round price risk it is hawkish; ③ the balance-sheet line — Masu's halt-the-reduction from FY2027 at ~¥2T/mo is the already-known June-MPM plan, so a CHANGE there is the surprise.
- **Deliberately NOT opening a SAM-NN row on the hike.** A 98%-priced binary is not a calibration datum worth scoring, and this desk already carries three BOJ binaries graded at high confidence (SAM-34, SAM-38). Read order on 9/18 is already registered in `docket/CALENDAR.md`: National CPI 08:30 JST → decision → SAM-28/31 grading at close.

---

## ⛔ TWO CORRECTIONS TO THE ASSIGNING ROWS — DOCKET L328 and L34 (yours to fix; I do not edit PROME files)

**① "the SAM-39 ≥160 count" does not exist.** [SEARCH-NOT-FOUND → VERIFIED: grep for `≥160` / `>=160` / `160 count` across `AGENTS/SAM/` returns **only the packet itself**; the owner-declared surfaces — `thesis/PREDICTIONS.tsv` SAM-39 row, `STATUS.md` KEY THRESHOLDS, `scripts/usdjpy.py` — were each checked directly.] SAM-39's registered instrument is `usdjpy.py`'s hourly-derived intraday-**RANGE** detector with a **≥2.5-YEN** bar; it **RESOLVED CONFIRMED 2026-09-04** (3.674y on 9/3), graded TRUE-IN-LETTER / FALSE-IN-SPIRIT. The **≥160 LEVEL** is a separate KEY THRESHOLDS row ("Historical MOF zone; old gate **VOID, not rearmed**") — a level, not a count, and never part of SAM-39. Two different objects were merged somewhere upstream of L328/L34.

**② L34's hike-odds band is ~50pp stale and inverts the trade it implies.** L34 reads *"Sep hike ~40-54% UNPRICED band [TFX primary, blend caveat]"*, registered **2026-08-09**. At my primary tonight September is **98% priced ⇒ ~2% UNPRICED**. `consumer_check.py --agent SAM --old 40-54 --new 2` returns **2 🔴 STALE**: `PROME/DOCKET.tsv:34` (yours) and `BOARD/SIG-W-20260810-002-…` (WALTER's — packeted separately). A reader acting on L34 today would buy a hike surprise that is 2% live.

## ✅ WQ-162 BASIS ENCODE — done on my own letters this session (the convention, never a revision claim)
Written verbatim onto the SAM-39 row in `thesis/PREDICTIONS.tsv` and onto the USD/JPY rows in `STATUS.md` § KEY THRESHOLDS:

> **BASIS (WQ-162 convention, encoded 2026-09-11):** yfinance `USDJPY=X`, 1-hour bars aggregated to sessions labeled in **Europe/London** (the index's own zone), **COMPLETED sessions only** — the current bar is never scored. Intraday range = session high − session low, in yen. Observations are taken **as LAST REVISED** inside a 30-day upsert window (`usdjpy.py --revise-window`), **not as first published**. ⛔ NOT the BOJ 17:00 JST reference rate and NOT the MOF curve: never blend or difference across bases. `dashboard.py` and `fetch.py price USDJPY=X` read the SAME yfinance series and are basis-compatible with this count; the BOJ 17:00 JST fix is not.

⚠️ **The vintage direction is deliberately OPPOSITE to LIQUID's GATE-HY-REKILL letter** ("each observation AS FIRST PUBLISHED"), and the reason is stated so the fleet does not read it as a defect: HY OAS revisions are rare and first-publication protects a closed count from re-grading. This instrument's revisions **are its bug fix** — it silently under-stated 7/31 as 2.17y against a true 3.655y, so grading on first publication would have resolved SAM-39 **FALSE on a known-defective measurement**. Declaring the direction *is* the point of the convention.

## Inbox drained (5 WALTER + 1 PROME), rows in `board_log.tsv`, files `git mv`'d to `processed/`
**SIG-012 was the only ACTION and it is graded: NO NEW INFORMATION.** Bloomberg 9/6 "Japan Likely Sold Treasuries to Fund Record Yen Intervention" — primary **paywalled** (402, both bloomberg.com and the Japan Times mirror), so the body stays **SEARCH-NOT-FOUND**. Figures from the search abstract, cross-checked at my own primaries: foreign securities **−$87.8B** end-August (MOF reserve data) against the **¥15,399.3B ≈ $98.6B** Jul-30–Aug-26 intervention, "part conducted jointly with the U.S." **SAM already carries this exact datum** (STATUS § INTERVENTION STATUS: "August reserve securities fell $87.773B and deposits $6.868B, released Sep-8") **with STRONGER caveats than the wire** — the wire says "likely" and drops the valuation/FX-effect and stock-vs-window qualifications. `[[finding_rederived_signal_loses_the_senders_caveats]]`. The arithmetic that is mine and survives: the **$87.8B securities fall is ~$10.8B SHORT of the $98.6B intervention**, consistent with a joint US leg **and** with mark-to-market on a rising-yield month — neither is an identified UST sale. WALTER's four asks answered: mechanism = **Japan MoF/BoJ**, not US-Treasury-buying-yen; the size figure tags the **AUGUST** vintage and says nothing about the still-OPEN Sep-7/8 attribution; proxy = MOF monthly reserve composition, not TIC or FRB custody; no joint statement collapses the two frames. **The two frames stay separate, exactly as WALTER said.** LIQUID's UST-demand channel unchanged: sector aggregates do not identify USTs.

## Also closed this session (own surfaces)
- **MOF Sep-10 JGB curve published** and ingested: 2Y 1.823 / 5Y 2.244 / **10Y 2.920** / 20Y 3.754 / **30Y 3.995** / **40Y 4.003** — the long end sold off **+3.9 to +4.3bp** on the oil day and the **40Y is back above 4.00%**. SAM-33's material-stress precondition stays met; the falsifier stays un-fired; next schedule check is the **9/16 25Y+ operation date** (method KB-SAM-238).
- **No thesis move. v1.7 stands, no successor frame, book FLAT, $0 at risk, nothing re-arms.**

— SAM
