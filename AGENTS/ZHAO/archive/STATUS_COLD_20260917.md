# ZHAO STATUS — COLD SPLIT #2, moved verbatim 2026-09-17

**What this is:** the second READ-CAP rotation of `STATUS.md` (first: `STATUS_COLD_20260902.md`). DAEDALUS 9/5 measured the hot surface back at **32,534 B = 99.95% of the 32,550 B boot-read budget** three days after the 9/2 split (PAT-055 regrowth, n=2 with OTTO). `scripts/read_cap_check.py --agent ZHAO` on 2026-09-17 read 100% of budget, rotate-tier, and named the rule-5 STOP (<70% = 22,785 B). Every block below was **moved verbatim** — no wording changed, no figure restated. `STATUS.md` carries a one-line pointer at each cut site.

**Reciprocal pointer:** hot surface = `AGENTS/ZHAO/STATUS.md`. Permanent record = `workbook/KB.tsv`. Earlier cold half = `archive/STATUS_COLD_20260902.md`.

**Which cost this split chose (per the 9/2 FOLLOW-UP, KB-ZHAO-140):** history-to-cold, not compression — the Sep-2 narrative blocks (August-PMI grade, Sep-2 bottom line, closed cross-agent rows) moved whole; live rules, the dashboard, the matrix, the calendar and open predictions stayed hot. Per-surface bytes before/after and the boot-read total are in the commit body of the commit that created this file (`git log -1 -- AGENTS/ZHAO/archive/STATUS_COLD_20260917.md`), not restated here (no live measurements in prose).

**⚠️ Vintage:** everything below is **2026-09-02 vintage**. History, not a current read — go to `STATUS.md` or `workbook/VX.tsv` for live values.

---

## ① MOVED VERBATIM — `## 📌 SEP 2 — AUGUST PMI` block (STATUS.md 2026-09-02 lines 10-28, 2654 B)

## 📌 SEP 2 — **AUGUST PMI: the discriminator resolved, and the headline is the wrong number to read it on**

| Series | Aug | Jul | Read |
|---|---:|---:|---|
| Manufacturing | **49.8** | 49.2 | 2nd month sub-50 but **beat cons. 49.7**; **production 50.4** + **new orders 50.6** back in expansion (from 48.5, lowest since 2023) |
| Non-mfg / Services | 49.0 / **49.3** | 49.0 / 49.3 | **both flat — not recovering** |
| 🔴 **Construction** | 🔴 **46.9** | 47.0 | 🔴 **NEW RECORD LOW** below the prior record low. Expectations flat 51.8 = belief without activity |
| Composite | **49.5** | 49.3 | **2nd consecutive sub-50**; the +0.2 is **entirely manufacturing** |
| High-tech mfg | 52.9 | ~52.9 | held in expansion — VULCAN's leg |

**Source:** NBS via `english.www.gov.cn` (State Council release) 2026-08-31, ZHAO direct pull 9/2 + WALTER `SIG-W-20260901-012` + MIDAS 9/2 packet. **NBS statistician Huo Lihui: construction slowed on extreme weather, heavy rains and typhoons — the SECOND consecutive month with that attribution.**

**⇒ SPLIT GRADE.** **(b) weather** 🟡 partly supported *on manufacturing* — production and new orders back above 50 is what an unwinding one-month distortion looks like. **(a) broadening** 🔴 **supported on the PROPERTY leg, and this is the finding** — construction did not unwind, it went **lower**, on the identical attribution a second month. **A distortion that recurs is a condition.** Services flat for a second month is the other non-weather leg. **Net: strip manufacturing and China's non-manufacturing economy did not move at all in August.** *(Full table + grade verbatim → `archive/STATUS_COLD_20260902.md` §⑧.)*

⚠️ **Registered against myself:** my 8/3 spec said *"a second sub-50 composite turns July's break into a thesis."* **On the letter that is satisfied — and I am declining the full upgrade it permits**, because the mechanism that satisfied it (construction) is not the one the spec was reasoning about (broad demand), and manufacturing went the other way. **Same defect class MIDAS self-reported on its own I1 branches the same day (non-MECE, no boundary owner).** [[finding_registered_trigger_can_fire_on_an_unnamed_mechanism]]

⚠️ **NOT established:** the **RatingDog (ex-Caixin) August private PMI** was unpublished at read time — the state-vs-private divergence (July: NBS 49.2 vs RatingDog **50.9**) is **unresolved for August** and is the single check that could flip the manufacturing read. **Owed pull, early September.**

**→ 8/21 JUNE TIC block verbatim → COLD §① · detail → `reports/2026-08-21_JUNE_TIC_SESSION.md` · KB-119..127.**

---

## ② MOVED VERBATIM — XI block — the `boot.py` placeholder-day instrument-defect paragraph (STATUS.md 2026-09-02 lines 36-36, 607 B)

⚠️ **A defect in my own instrument:** `docket/CATALYSTS.tsv` and PROME `DOCKET` 219 both carried `2026-09-01..2026-09-30 / DAY UNANNOUNCED`, so `boot.py` printed **"2026-09-01 · 1d ago · RECENTLY FIRED · SWEEP NOW"** this morning. **A placeholder day aged into a false fire.** The 8/21 reader was built to stop this class and it arrived through the other door — the reader carried the RANGE correctly, but **nothing re-checked whether the unknown was still unknown.** `[[finding_dated_carry_item_has_no_expiry_check]]`. **CATALYSTS re-dated `2026-09-24`/`external`; PROME packeted for DOCKET 219.**

---

## ③ MOVED VERBATIM — XI block — the HAWK-credit paragraph under ZHA-16 (STATUS.md 2026-09-02 lines 43-43, 1013 B)

**Credit:** HAWK's 8/22 US-§338 post-mortem — *a dated branch can be **MIS-SHAPED rather than incomplete**: one leg is the **self-executing default**, the others are **overrides**; completeness-testing cannot catch it, and the catching question is **"which branch happens if nobody acts?"*** `[[finding_no_action_ruling_does_not_disarm_an_automatic_mechanism]]`. HAWK left the 11/10 structure **explicitly blank** and warned against importing their base rate rather than their question — so ZHAO read the instrument. **Their operational bar adopted verbatim for branch A: *is there a published instrument with an effective date beyond 2026-11-10?* Everything else is commentary** — on 8/22 a deal was announced, USTR described its coverage, and the tariff went live three days later, because the announcement was never converted into an instrument. ⚠️ **Graded on the DOCUMENT, never the tape:** a 2% equity rally with no instrument is **branch B**. `[[finding_market_ignoring_is_not_market_refuting]]`

---

## ④ MOVED VERBATIM — Convergence-matrix `FLAT TOTAL` blockquote (STATUS.md 2026-09-02 lines 113-113, 377 B)

> ⚠️ **FLAT TOTAL, SECOND CONSECUTIVE HIDDEN ROTATION.** 8/21's +2 hid one; today's **0** hides another: **property 4→5, domestic-demand 4→3.** August did not make China better or worse in aggregate — **it moved the damage into the leg with the debt attached.** Sum the rows every closeout; never carry the total. `[[finding_loadbearing_number_must_be_reproducible]]`

---

## ⑤ MOVED VERBATIM — CROSS-AGENT rows LIQUID · HANS/NEXUS/SAM/BOND (closed 8/21–9/2) (STATUS.md 2026-09-02 lines 123-124, 947 B)

| **LIQUID** | June TIC / Belgium falsification consumed 8/23 — every Belgium inference stripped, two derived numbers retired, two more level-keyed triggers of its own caught. Its ASK back (can TIC attribute the private bid?) **answered 9/2** | 🟢 CLOSED both ways |
| **HANS · NEXUS · SAM · BOND** | **HANS** 8/28: carries **no** Belgium→China inference on any live surface; one dormant March threshold retired in place; France −$20.92B accepted. · **NEXUS** PRED-30 re-graded on **composition** 45%→55%, ZHAO's fences carried verbatim — ⚠️ **M-10 left at 32%** pending its own matrix sweep, June TIC a live counterweight, **queued not folded.** · **SAM** Japan −$26.86B (Jun) is **bills not duration** (ST −$23.11B / LT −$3.75B); LIQUID has qualified its >$20B trigger to an LT basis on it. · **BOND** China 10Y / CGB assigned to ZHAO 8/18 (Will's word); boundary accepted as written | 🟢 closed / 🟡 NEXUS open |

---

## ⑥ MOVED VERBATIM — NEXT ACTIONS `Done Sep 2` paragraph (STATUS.md 2026-09-02 lines 184-184, 592 B)

**Done Sep 2:** 37 inbox items drained, both lanes ✓ · **August PMI graded — construction sub-index pulled that nobody else had** ✓ · **CXMT bit ask answered to VULCAN after 40 days / n=4** ✓ · summit DATED 9/24 + the false-fire in my own catalyst reader diagnosed ✓ · **ZHA-16 + ZHA-17 pre-registered before their events, with declared residuals** ✓ · READ-CAP split executed, nothing deleted ✓ · CGB scope + NEXUS brief-fold ordering adopted into `CLAUDE.md` ✓ · KB-ZHAO-128..134 ✓. **Full 8/21 NEXT ACTIONS (11,618 B) → `archive/STATUS_COLD_20260902.md` §④.**

---

## ⑦ MOVED VERBATIM — `## BOTTOM LINE` (Sep 2) narrative (STATUS.md 2026-09-02 lines 203-211, 2502 B)

**SEP 2 — the discriminator I registered five weeks ago fired, and it fired on the leg I was not watching.**

August's PMI reads like a rebound and is not one. Manufacturing beat (49.8 vs 49.7), production and new orders climbed back above 50, the composite ticked up — **all consistent with July's typhoon distortion unwinding, exactly as the (b) branch predicted.** But the branch was registered on the *composite*, and the composite is the wrong place to look: underneath it **construction printed 46.9, a new record low below July's record low, and NBS blamed extreme weather for the second month running.** Services sat flat at 49.3. **Strip manufacturing and China's non-manufacturing economy did not move at all in August.**

**On the record: a weather attribution that has to be re-used is weaker evidence, not stronger.** One month of typhoons is a distortion; two consecutive record lows on the same attribution is either a very unlucky season or a condition wearing a season's clothes — and the construction *expectations* index flat at 51.8 through both says the industry believes in a recovery it is not having. **Property went to 5, broad domestic demand to 3, and the total did not move — the second consecutive session where a flat 28 concealed a rotation.** The damage relocated into the leg with the debt attached to it.

**On capital flows nothing has changed since 8/21 and the next test is 14 days out.** China is at $633.4B on −$122.3B TTM, the Belgium proxy is falsified in both directions, rotation is refuted, and **I still cannot tell you where the money went.** July TIC ~9/16 is the composition arbiter, now a graded letter (**ZHA-17**) with half-open intervals and a named boundary owner — because my last three registrations all carried spec defects at resolution time, and the fix is to write the boundary before the print.

**Two things this session bought that were not on its list.** VULCAN's CXMT ask closed after 40 days — and what matters here is that I had been carrying **"not checked" as if it were "not available," and those are different claims about the world. One is about China. The other is about me.** And a HAWK packet landed mid-session and **corrected my own summit letter before the event**: the 11/10 suspension **expires by its own terms**, so the do-nothing branch is the tariff branch, and the branch I had written as the quiet base case is the escalation-by-default one. **Both findings came out of the queue, not out of the plan.**

---

## ⑧ MOVED VERBATIM — THESIS one-line restatement + long-standing gaps (STATUS.md 2026-09-02 lines 215-217, 1173 B)

**🚩 THESIS (7/16 reframe, Will-approved KB-ZHAO-102; amended 8/21 Will-ruled).** Canon: `CLAUDE.md` §BELGIUM PROXY METHODOLOGY — **cite it, don't restate it.** In one line: the $650B line tracks SAFE's narrowly-defined, TIC-visible, Treasury-specific holdings — real, mechanical, market-moving — **but a breach is not a reliable signal of China's aggregate USD exposure.** Both named mechanisms are gone (Agency rotation **REFUTED**; off-SAFE entity-shifting **demoted to possibility**); **what holds the doctrine up is valuation, which is true on the stock, false on the flow, and reverses if markets stop rising.** ⚠️ **Perimeter, always say which: −$122.3B** all Treasuries incl. bills (Table 3) · **−$91.3B** coupons only (Table 1). ⚠️ No live magnitude is hardcoded in canon — VX-ZHAO-1.03 / 1.02 only. **Full 8/21 tail verbatim → `archive/STATUS_COLD_20260902.md` §⑤.**

**Long-standing gaps:** Guizhou/Zhengzhou bank-specific NPL 🧊 FROZEN, no primary · Korea official-vs-all-residents scope split (VX-ZHAO-2.07) · **SOFR leg of HIBOR-SOFR never verified** · CNH-CNY spread · **KB.tsv `Stale_By` has no reader, 30 rows past due.**

---

## ⑨ MOVED VERBATIM 2026-09-17 — closed Sep-2 items cut whole from the hot surface (read-cap banner · summit date-sourcing · MIDAS cross-agent row · Q2-GDP and Korea-CPI dashboard rows · Aug-31 calendar row)

> 🧊 **READ-CAP SPLIT EXECUTED 2026-09-02** (DAEDALUS P1, 8/28): **47,477 B → under the 32,550 B boot-read budget.** Every cut block moved **VERBATIM** to `archive/STATUS_COLD_20260902.md` §①-⑧ — the 8/21 JUNE TIC and P3 blocks, matrix commentary, **the whole 8/21 NEXT ACTIONS (11,618 B)**, the 8/21 BOTTOM LINE + thesis tail, the pre-rewrite dashboard/matrix/calendar/predictions, and this session's August-PMI detail table. Pointers at each cut site; the cold file points back. **Nothing was deleted.**

**Date:** Trump named **2026-09-24** — the UNGA window (Bloomberg 7/6), then flatly on **7/23** (US News / Fox / WION, all tracing to his own remarks; invitation issued at the May-2026 Beijing summit). **PRIMARY-adjacent, US side.** ⚠️ **No PRC-side (MFA / Xinhua) confirmation located — US-announced, not bilaterally confirmed**, which is why branch D is real. *(KB-ZHAO-130)*

| **MIDAS** | **Aug PMI: grade differs on evidence, not method — construction 46.9 is a NEW record low and MIDAS did not have that sub-index.** Copper firm *through a new record low* is a **harder** test passed than MIDAS stated ⇒ its structural/AI-grid attribution is **strengthened**; the correction runs in its favour. Construction→copper lag answered **UNESTABLISHED**, with what would establish it | 🟢 **SENT 9/2** |

| China Q2 GDP | **+4.3% YoY** (vs 4.5% cons.; Q1 5.0%) | <4.5% = miss | 🟠 [CONF] NBS 7/15 (KB-095). H1 real-estate inv. **−18% YoY**; FAI ex-property only **−2.7%**; June IP **+5.3%** — a property-leg miss with the industrial leg accelerating |

| Korea CPI (Jun) **3.2%** · China real property (BIS) **~86** vs 2021 peak ~113 | — | — | 🟠 BoK hiked +25bp to 2.75% 7/16 (KB-093) · 20yr property gains erased (WALTER SIG-W-20260706-017) |

| ✅ Mon Aug 31 | **China August PMI** — **DONE, graded 9/2** (above) | ✅ KB-128 |

---

## ⑩ ORIGINALS OF LINES SHORTENED IN PLACE 2026-09-17 (truce-clock paragraph · CGB dashboard row · matrix rows 3 / 5 / 5b · Korea exit-rule bullet) — the hot surface carries a shorter form of each; this is the 9/2 wording, verbatim

🔴 **THE TRUCE CLOCK — instrument read, not assumed** (White House presidential action 2025-11): *"…**shall continue to be suspended until 12:01 a.m. eastern standard time on November 10, 2026**."* **That is a TIME-LIMITED SUSPENSION expiring by its own terms, not a rate modification that persists until changed.** ⇒ **Nobody has to decide to re-impose the heightened reciprocal tariff; somebody has to decide NOT to.** Suspended-state reciprocal rate **10%**, fentanyl-linked tariff cut **20%→10%** under the same arrangement; ⚠️ **the RESUMED rate is NOT specified in the order and I am not filling it in.** **The summit sits 47 days ahead and is the only head-of-state venue before it.**

| China 10Y CGB | **1.710%** (−7.0bp) | — | 🟡 🧊 **[STALE 7/31]** — **newly ZHAO's** (WALTER routing v0.27, Will 8/18). ⚠️ **A low nominal CGB yield is NOT haven demand**: the market sits inside capital controls with policy banks as principal buyers, so deflation + weak credit demand is at least as consistent — and the two read opposite downstream. **Boundary: “what is Beijing doing” = ZHAO · “how is the CGB market clearing” = BOND** |

| 3 | Custodial Arbitrage | 🟡 2 | **Scored 2 = CANNOT BE MEASURED, not benign.** Belgium at a series-record $482.5B on +$17.56B bought, but rho = **+0.05, n=41**. The migration inference is unsupported month-to-month. **HANS confirmed 8/28 it carries no China inference; LIQUID confirmed it did and stripped it.** HANS owns the hub table | Belgium **Jun'26**, live 8/21 |

| 5 | Property Zombification | 🔴 **5 ↑** | ⬆️ **UPGRADED 9/2 on the August print.** Construction PMI **46.9 — a NEW record low, below July's record low** — and the weather attribution was **re-used a second month**. H1 real-estate investment −18% YoY; Vanke ¥9.4B maturing. **The July typhoon caveat did not unwind here; it deepened.** Expectations index flat at 51.8 = belief without activity | **Aug 31** |

| 5b | Domestic Demand / Broad Activity | 🟠 **3 ↓** | ⬇️ **DOWNGRADED 9/2, and only the manufacturing leg earns it.** Mfg 49.2→**49.8** (beat), **production 50.4** and **new orders 50.6** back in expansion from 48.5. **But services are FLAT at 49.3 for a second month and the composite is sub-50 twice.** Read as *shallowing, not recovering* | **Aug 31** |

- ✅ **Korea KRW <1,450 sustained: FIRED 2026-08-12**, graded 8/21, basis-independent (0 of 10 days printed a high ≥1450). **Falsifies ZHAO's Korea-as-UST-anchor leg.** ⚠️ **Not a full stand-down** — the two caveats (foreign KOSPI selling not reversed; SK hynix conversion share) are **unverified, not resolved**. Full text → `archive/STATUS_COLD_20260902.md` §⑦.

---

## ⑨-b MOVED VERBATIM 2026-09-17 (third pass) — Property/LGFV cluster and PBOC-gold dashboard rows · Dec-2026 / May-2027 calendar rows · Thesis-Kill bullets · NEXT ACTIONS items 11 and 13

| Property / LGFV / banking cluster | Land sales H1 **−6.5% to −27% YoY** · LGFV ~**60T RMB** (IMF 44-58T) · Guizhou/Zhengzhou NPL **11.6% / 9.55%** 🧊 FROZEN 7/16 · small banks **130+** by Jun 4 (run-rate ~310+, ZHA-06) | mixed | 🟠 [CONF] as dated. **Source of truth = `workbook/VX.tsv`** |

| PBOC gold streak | **20 months** (+14.93t Jun) | — | 🟢 [CONF] **not** the primary UST-reallocation channel — too small (KB-099/102) |

| ~May 2027 | Rare-earth control postponement expiry | 🟡 |

| Dec 2026 | SEC Cash Clearing mandate (LIQUID's) | 🟡 |

### Thesis Kill

- Belgium <10% YoY for 2 prints AND China >$700B for 3 prints *(neither close: Belgium +12.1% YoY, China $633.4B)*

- Massive fiscal stimulus >5% GDP with LGFV full backstop

11. 🟡 Re-register ZHA-03 for H2 on a rho-surviving mechanism · 12. 🟡 China 10Y/CGB one stale datum (1.710%, 7/31): refresh or freeze.

13. 🟠 **HK sold $9.33B of Treasuries in June while the peg stayed quiet** — self-assigned 8/21, recovered 9/2, **still not logged** (KB-ZHAO-140).

---
