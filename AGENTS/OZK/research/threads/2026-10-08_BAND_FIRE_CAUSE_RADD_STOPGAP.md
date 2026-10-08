# 2026-10-08 — <$45 band FIRED (10/6 close) · cause search · RaDD stopgap to 10/9

**Session:** PROME `prome-fc` wake (WQ-391 item 3, Will 08:30 ET), laptop. Runtime Claude Code (Agent SDK), model `claude-opus-5-5`; session id not exposed (UNKNOWN). Written 2026-10-08 ~08:45 ET (`date`). Sole OZK writer.
**Scope:** cause search, band grade, REGINALD reconcile, inbox drain, arm items. **$0. No grade, weight, threshold or conviction moved.** No card, no recommendation on Will's puts (TERRY's).

---

## 1. Tape (two independent routes agree to the cent)

Routes: FORGE `fetch.py price --history` (yfinance daily bars, pulled 08:35 ET 10/8) and Nasdaq historical API (`api.nasdaq.com/api/quote/OZK/historical`, pulled 08:38 ET 10/8).

| Date | OZK close | OZK chg | High / Low | Volume | KRE chg | WAL | FLG | CFG | ZION | VLY | SPY |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10/5 Mon | $46.59 | −0.26% (yf; −0.25% on Nasdaq $46.705) | 46.90 / 46.35 | 1.27M | −0.55% | −0.47% | −1.11% | −0.03% | +0.17% | −0.47% | +0.67% |
| **10/6 Tue** | **$44.58** | **−4.31%** | 46.90 / **44.19** | **4.39M** | **−0.45%** | **+0.09%** | **−0.09%** | **−0.34%** | **−0.68%** | **−0.71%** | **+0.55%** |
| **10/7 Wed** | **$43.56** | **−2.29%** | 44.46 / 43.30 | **3.65M** | −1.68% | −2.29% | −2.25% | −1.59% | −1.48% | −1.50% | −0.24% |

- **Volume, one basis:** 20-session average before 10/6 = **1.165M** (9/8–10/5). 10/6 = **3.8×**; 10/7 = **3.1×**. (WALTER's "~3.5×" sits between the two days; 5-session basis gives 3.7× / 3.1×.)
- **10/6 is idiosyncratic:** OZK −4.31% while every cohort name was between −0.71% and +0.09% and SPY rose. **10/7 is sector:** OZK −2.29% = WAL −2.29%, FLG −2.25%.
- Latest official close **$43.56 [10/7]**. 10/8 pre-market not read (a pre-market read is a vendor read, not a close).
- TBV $48.41 [Q2'26] ⇒ **P/TBV 0.90×** on $43.56.

## 2. Cause search — what was checked, and what it returned

| # | Source (primary first) | Checked | Result | Token |
|---|---|---|---|---|
| 1 | **FDIC FLNG cert 110** (`flng_watch.py`, OZK's 8-K/10-Q home — OZK does not file with the SEC) | 10/8 08:34 ET | rc 0: 182 filings, schema + coverage OK, none after id 11981 (the 8/5 10-Q) | VERIFIED — no new filing returned |
| 2 | **FDIC EFR insider forms** (`/api/instdiscl/cert/110`) | 10/8 08:35 ET | 471 forms; newest published **2026-08-14** (Wolfe, Hicks) | VERIFIED — no insider form since 8/14 |
| 3 | **SEC EDGAR full-text** `"Bank OZK"` 10/1–10/8 | 10/8 08:36 ET | 21 hits: 13F-HR holdings reports, N-CSR fund reports, one S-4/A exhibit (Air Industries Group); **no 13D, no 13G, nothing issued by OZK** | VERIFIED — no ownership filing |
| 4 | **OZK press releases** (GlobeNewswire syndication; ir.ozk.com 403s scripts) | 10/8 | Newest: 9/30 (Q3 date) and 10/1 (dividend $0.49, record **10/13**, payable 10/20). **Nothing dated 10/2–10/8.** | SEARCH-NOT-FOUND (syndication only) |
| 5 | **Sub-notes call-notice window** | 10/8 | A notice for the 1/1/2027 call cannot fall before **11/2** (10–60 days). FLNG quiet; press shows no redemption, new sub-debt or offering | SEARCH-NOT-FOUND; window not yet open |
| 6 | **Ratings agencies** (KBRA, Moody's, S&P, Fitch) | 10/8 | Newest found: **KBRA affirmed 10/24/2025** (A- deposits / BBB+ sub debt, Outlook **Negative**); Moody's affirmation 2024. **No 2026 action found.** KBRA's annual review has landed late October in 2023–25 (pattern, INFERRED) | SEARCH-NOT-FOUND |
| 7 | **Sell-side** | 10/8 | **Citi (Ben Gerlinger), Tue 10/6: note on the RaDD loan modification** (below). TD Cowen Mon 10/5: target $52→$50, Hold (MarketBeat 10/5 11:48 ET) — 10/5 close −0.26%. Wells Fargo 9/30: $56→$51, Equal Weight. Morgan Stanley 9/28: $56→$57, Underweight. No outright downgrade found | Citi = the only 10/6 OZK-specific item found |
| 8 | **Peer tape** | §1 | 10/6 cohort flat; 10/7 cohort −1.5 to −2.3% | VERIFIED (two routes) |
| 9 | **Bluerock BPRE webinar** (IQHQ's largest holder) | 10/8 | Held **10/6 at 4:00 PM ET — after the close**; replay posted 10/7 (video, not machine-readable). BPRE's 8/31 top holdings: IQHQ warrant equity **5.1%** + IQHQ equity **2.6%** of gross assets | Timing **rules it out** as the 10/6 cause; content UNKNOWN |
| 10 | **Affinius / Athene linkages** | 10/8 | Affinius: newest item found Feb 2026 (Veris take-private). Athene: nothing tied to OZK or IQHQ | SEARCH-NOT-FOUND |
| 11 | **Short interest** (Nasdaq API) | 10/8 08:38 ET | Newest settlement still **9/15**: 16.51M sh, DTC 17.6. The 9/30 settlement is not published yet | No update |
| 12 | **SD County Recorder** (the RaDD instrument itself) | 10/8 | `arcc-acclaim.sdcounty.ca.gov` returns **403** to curl and to WebFetch | **UNKNOWN — unreachable by script** |

### The cause found — the RaDD loan was on a ~6-week stopgap

**What Citi's 10/6 note reports**, per Seeking Alpha (10/6, via TradingView), GuruFocus (10/6, page stamp 19:55Z) and Bisnow (10/7 12:59 ET, Matt Wasielewski):
- Document: **"Fifth Modification of Construction Leasehold Deed of Trust"**, filed with San Diego County on **10/2/2026**.
- Borrower **IQHQ-RADD 1, LLC**; lender Bank OZK; loan **$915M** (= the commitment; funded $555M per OZK's own filings).
- Original maturity **2026-08-26**. New maturity **2026-10-09** (Friday, tomorrow). Effective as of **8/26**; signed by **OZK 9/30**, by **IQHQ 10/1**.
- Citi, quoted: *"this extremely short extension of approximately six weeks is not a long-term solution"* · *"underscores the severity of the project's financial distress"* · *"The project's fate likely hinges on the negotiations that will take place before the new October 9th deadline"* · *"OZK has done this before (short duration extensions) with other sponsors."*
- Citi's rating and target on 10/6: **Sell / $40** per a search summary of a Google Finance table. That page did not render for me, so this is **UNVERIFIED**. Citi has held Sell since the May-2024 double downgrade.

**What OZK said:** Michelle Rossow (Chief Communications Officer), emailed to Bisnow 10/7: *"In complex transactions, short-term extensions routinely occur as the parties finalize documentation for longer-term extensions."* That is the issuer confirming that a short extension exists and that it calls the extension a bridge. **It is not an OZK release or filing.**

**Evidence grade:**
- A short-term extension EXISTS: **CORROBORATED** by Citi's document read plus the issuer's own statement.
- The terms (10/9 maturity, 8/26 effective date, signature dates, recording date): **SINGLE-SOURCE.** They are Citi's reading of a recorded instrument I could not reach.
- **Attributing the 10/6 move to the note is INFERRED.** The note is the only OZK-specific item dated 10/6, and three outlets attribute the move to it. The selling ran into the close: reports put OZK at **$45.44 (−2.48%) in afternoon trade**, with an intraday low of $45.06 at that point. The close was $44.58 and the low $44.19.
- 10/7's −2.29% was sector-sized, and it came on the day Bisnow ran OZK's confirmation.

**The finding:** the 10/6 cause is identified at the secondary level, not at the primaries. The primary (the recorded instrument) was not reachable. Every primary I could reach — FDIC FLNG, FDIC EFR, EDGAR, OZK releases — was silent.

## 3. What this does and does not change in the thesis — no number moved

- **The fact is consistent with v1.5.** v1.5 expects the extension to be negotiated and recognition to be back-loaded. On 7/22 management said a "multi-year extension + recap" was in negotiation with "~92 days" to more disclosure. As of 10/1 the executed instrument was **a 6-week bridge, not the multi-year deal**. OZK calls it routine documentation timing; Citi calls it distress. Both readings fit the recorded fact. **The weights (A30/B45/C8/D17), OZK-09 at 45% and conviction are untouched.** The playbook's own rule is that executed terms at the Q3 call move the weights.
- **One correction to the record:** the August maturity did not pass "quietly extended." By Citi's reading the loan's stated maturity was **8/26**, and no signed modification existed until **9/30–10/1** (made retroactive to 8/26). The 8/31 sweep's SWEPT-AND-EMPTY result stands for what was public on 8/31; nothing was recorded until 10/2. The recorder leg (TODO C2) is the leg that would have seen it.
- ⚠️ **An ambiguity in the OZK-09 wording. I did not grade it.** Two clauses read "any executed extension with <$140M recognition = FALSE regardless of funding source" (playbook Scenario A) and "an executed A/C takeout with <$140M resolves FALSE immediately" (the PREDICTIONS invalidation clause). Read literally, a 6-week stopgap signed 9/30–10/1 with $0 recognition could be called "executed" and resolve OZK-09 FALSE as of 10/1. **The desk's reading: no.** Scenario A's mechanism is "extend 1-2 years with new reserve contribution, TI guarantee, or covenant restructure." A bridge that expires inside the window with no disclosed capital is not that. Intent never resolves (Z10), and the row stays **OPEN**. **This is a reading of a frozen letter, so it is Will's:** proposal **P-OZK-6, not applied.** Pre-registering the reading now, before the 10/9 and 10/21 outcomes are known, keeps either reading from being chosen self-servingly later (the Option-2 principle, 7/23). It matters only on the B/D path. If a multi-year extension is executed with <$140M recognition, FALSE follows on either reading.
- **New dated observable (forced by the evidence, not a new direction):** the stopgap matures **Fri 10/9**. Possible outcomes: (a) a sixth modification, multi-year or another bridge; (b) default or forbearance; (c) silence until the 10/21 call. Visible through OZK or Citi statements, press, the recorder (a browser pull) and the **Q3 call 10/21**. That call is the first disclosure test and was already armed (L520).

## 4. The <$45 band — graded on its own letter

- **Letter** (`AGENTS/OZK/CLAUDE.md` §CROSS-AGENT SIGNALS, "You send" table): `| OZK price <$45 | REGINALD, PROME | 🔴 |`. The registered consequent is a 🔴 signal to REGINALD and PROME, nothing else. The letter names no basis (close or intraday) and no persistence count.
- **Grade: FIRED on the 10/6 regular-session close $44.58** (first sub-$45 close; the intraday low was $44.19). It was still below on the 10/7 close of $43.56. Two closes are below, so the grade does not depend on basis or persistence.
- **Graded two sessions late:** the desk was dark 10/2→10/8. REGINALD saw the crossing first and routed it through WALTER (SIG-W-20261008-003). The consequent is discharged today: a 🔴 packet to REGINALD, this memo to PROME, an `AGENTS/SIGNALS.md` row, and a routing packet to WALTER for the cause.
- **What it arms:** (1) the next registered price line, **<$40 → REGINALD, PROME, FORGE 🔴**, now **$3.56 below the 10/7 close (8.2% of the close; 8.9% of $40 if measured from the strike)**. $40 is also the strike of Will's Nov-20 puts. (2) Nothing else by its letter. **The first registered evidence test is the Q3 print, Tue 10/20 after the close, with the call Wed 10/21 08:30 ET** (DOCKET L520: OREO sale prices vs carrying, Boston 10 Prospect, RaDD terms, special-mention migration, buyback). The RaDD stopgap maturity **10/9** now comes before it.
- **What it does not do:** it is a price-notification band. It is not a thesis grade. It moves no prediction, weight, kill criterion or conviction, and it is not a trade signal.

## 5. Will's Nov-20 $40 puts ×4 — the evidence they sit on (no card, no recommendation)

- **Position facts** (PROME packet, 10/7 Fidelity capture; holdings only, time unknown): OZK Nov-20 $40P ×4, broker basis $322.66, last $0.65, value $260. Acquisition date, price and management are unknown. TERRY carries `NOTE-OZK40P-NOV20` (no card unless Will asks), and the C5 card is owed by Wed 11/18.
- **Does today's read change the registered evidence?** **Yes, it adds to it.** The 10/6 drop is no longer cause-unknown. It has an identified RaDD-specific cause: OZK's largest single credit ($555M funded) was on a ~6-week stopgap to 10/9 (Citi's reading of the recorded modification; OZK confirms short extensions are in place). The RaDD resolution therefore now lands **inside the Nov-20 tenor**: 10/9, the 10/21 call, the 10-Q in early November.
- **It cuts both ways:** an executed multi-year extension at the call would be Scenario A, which the playbook prices as a 0 to +5% stock reaction. Short interest is ~16% of float [9/15].
- **For TERRY's arithmetic** (TERRY owns it): the record date is **Tue 10/13** and the dividend $0.49, payable 10/20 (OZK's 10/1 release, syndicated). The ex-date equals the record date under T+1 (convention, INFERRED).

## 6. REGINALD's read (b92113ed0) consumed — shared figures reconciled to one number each

| Figure | REGINALD (10/7 memo) | OZK desk | One number |
|---|---|---|---|
| OZK closes 10/6 · 10/7 | $44.58 · $43.56 | $44.58 · $43.56 (two routes) | ✅ agree |
| 10/6 relative move | −4.31% vs KRE −0.45% | same | ✅ agree |
| Volume | (WALTER: "~3.5×") | 3.8× [10/6] · 3.1× [10/7] on the 20-session avg 1.165M | **3.8× / 3.1×, 20-session basis** |
| Distance to $40 | "8.2% out of the money" (of price) | WALTER: "8.9% above" (of $40) | **$3.56 = 8.2% of the 10/7 close** (the desk's convention: % of price) |
| Foreclosed property | "$150M to $288.1M in Q2" | Call Report OREO `RCON2150` $149.6M → **$288.1M**; MC/10-Q bank-wide foreclosed **$292.7M** (RESG six ≈ $288.1M) | ✅ agree on the Call Report basis; label the basis |
| Reserve coverage "154% → 78%" | as stated | Reproduces on **ALLL `RCON3123` $461.5M**: ÷ nonaccrual $300.4M = **153.6%**; ÷ nonaccrual + OREO $588.6M = **78.4%** [Q2'26 Call Report]. On reported total **ACL $617.8M** (includes the unfunded-commitment reserve): **205.6% / 105.0%** | ✅ reproduces; **always state "ALLL basis"** — the ACL basis reads ~50pp higher |
| Foreclosures carried at "95–100% of appraisal" | as stated | Desk 9/27 workout check: true for the **three Q2 OREO transfers** (Seattle office, Seattle life sci, Atlanta); **LA land 8150 Sunset is at 86%** | Scope: "the three Q2 transfers" |
| "Its own Seattle office **sold** at 58% of appraisal" | as stated | Desk 9/27 thread, from REGINALD's own dossier: 760 Aloha **marked to an offer** at 58% of a Nov-24 appraisal, $6.4M, n=1, **"a mark to an offer rather than a completed sale"** | ⚠️ **Wording drift: "sold" vs "marked to an offer."** REGINALD to confirm whether it closed |
| Q3 Call Report | "due ~10/30" | "~Nov 1–10" pull; REGINALD's run 11/07 | No conflict: **filing due 10/30** (30 days after quarter end); public pull ~early Nov |
| Short interest | ~16% of float (desk's 9/15) | 16.51M sh, DTC 17.6 [9/15]; 9/30 not yet published | ✅ |
| Cause of 10/6 | "no found cause" | **Citi 10/6 note on the RaDD fifth modification** (§2) | ⚠️ **superseded** — packet to REGINALD |

## 7. Armed, not done

| When | Item | Owner of the row |
|---|---|---|
| **Fri 10/9** (stopgap maturity) → read on/after | RaDD sixth modification / default / silence: OZK or Citi statements, press, recorder (browser; 403 to scripts) | **NEW** — proposed to PROME as a dated row |
| **Tue 10/13** | Record date for the $0.49 dividend (ex-date by T+1 convention) | TERRY's arithmetic; on the OZK calendar for reference |
| **Wed 10/14** | **Campus at Horton leasing check (TODO C1, CHECK-BY)** — matters more now: the D-severity comp | OZK |
| **Tue 10/20 after the close · Wed 10/21 08:30 ET** | **Q3 print + call (DOCKET L520)** = the "~92-day" RaDD report-back. New leg added to the D3 card: **RaDD's 9/30 risk rating and past-due status** (its stated maturity of 8/26 passed with no signed extension until 9/30) | OZK |
| **Mon 2026-11-02 → Tue 2026-12-22** | Sub-notes 1/1/2027 par-call notice window | OZK |
| ~10/24 (pattern, INFERRED) | KBRA annual review (Outlook Negative since 10/2025) | watch only |

## Sources
- Bisnow, "Bank OZK Shares Drop After Citi Flags $915M Mortgage Concern," 10/7/2026 12:59 ET — https://www.bisnow.com/news/national/capital-markets/bank-ozk-shares-drop-after-citi-flags-915m-mortgage-concern
- Seeking Alpha via TradingView, "Bank OZK stock dips after Citi's cautious view on RaDD modification project," 10/6/2026 — https://www.tradingview.com/news/seekingalpha:016e8c9f1094b:0-bank-ozk-stock-dips-after-citi-s-cautious-view-on-radd-modification-project/
- GuruFocus, "Bank OZK (OZK) Shares Slip 2.48% Amid Citi Concerns Over RaDD Loan Extension," 10/6/2026 — https://www.gurufocus.com/news/9111955/
- MarketBeat, TD Cowen $52→$50, 10/5/2026 — https://www.marketbeat.com/instant-alerts/analyst-td-cowen-issues-pessimistic-forecast-for-bank-ozk-nasdaq-ozk-stock-price-2026-10-05/
- Bluerock BPRE fund page (top holdings 8/31/2026; Oct-2026 replay listed 10/7) — https://bluerock.com/bluerock-private-real-estate-fund/
- KBRA affirmation 10/24/2025 — https://www.kbra.com/publications/VBTpyGKR
- OZK 10/1 dividend release (syndicated) — https://finviz.com/news/397983/
