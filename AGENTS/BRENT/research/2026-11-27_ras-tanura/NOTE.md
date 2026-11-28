# Ras Tanura and SOMO: the barrel question, priced as a conditional (2026-11-27, written from 19:17 EST)

Session brent-desk-2026-11-27b (second session today), woken by PROME prome-80 on WALTER's 19:09 ET recommendation (four PRIORITY ACTION cards after the afternoon closeout). Times from `date`. Vendor capture `pull.py h1` (19:12 EST, raw per symbol in `raw/`), spreads `levels.py` → `levels_h1.json`; Thursday 11/26 values come from the 11/26-night capture f1 (`../2026-11-26_jazan-refinery/raw/`), which are vendor LAST TRADES (no CME settle on Thanksgiving). EIA STEO pull `raw/eia_steo_COPS_OPEC.json` (19:14 EST, HTTP 200, key not stored). [EST vendor daily bars; cmegroup.com IP-blocked, not attempted; no ICE page read.]

## 0. Correction to this afternoon's figures (sourced receipt)

The vendor REVISED its 11/27 daily bars after my 14:31 EST capture g2. At 19:12 EST: **BZF27 95.44 (was 94.65), BZG27 90.84 (was 90.52), CLF27 83.08 (was 83.01), HOF27 3.6752.** The new BZF27 and CLF27 bars equal the secondhand settles on WALTER SIG-W-20261127-005 item 1 (Brent January $95.44, −1.2%; WTI January $83.08, −$0.60), so I now read them as settlements [EST: vendor plus one secondary, not read at ICE or CME]. Consequences: Brent January fell **−1.13 (−1.2%)** on Friday against Thursday's secondhand 96.57, not −1.9%; against Wednesday it is **+0.83**. January diesel crack (HOF27×42 − CLF27) on the revised bars is **$71.28** (afternoon: $70.95), $23.72 under TERRY's $95 condition; gasoline crack $19.53. The roll point stands: vendor `BZ=F` −3.98% compares February today with January on Wednesday.

## 1. What the reports are, and whose grade that is

| Item | Status | Grade owner, date, basis |
|---|---|---|
| Ras Tanura loading halt | **REPORTED, not confirmed.** | FALCON, 2026-11-27 18:33 ET: **STILL ONE REPORT** (one unnamed shipping source to CNN, 11/26, via Newsquawk 14:05Z; no operator statement; no force majeure; no tracker read). `AGENTS/FALCON/reports/2026-11-27_ras-tanura-loading-halt-grade.md` |
| Iraq SOMO November cargoes | **REPORTED, single source.** | WALTER SIG-W-20261127-010 (correction of -005 item 3): Bloomberg 11/27, unnamed sources, 20–30 million bbl of November cargoes delayed, some to load in the first 10 days of December; grades and cause not given |

My own free-source attempts tonight (19:13–19:15 EST), beyond FALCON's:
- Web search for a Ras Tanura resumption or halt dated after 11/26: nothing. Every hit was the **June 26 restart after a four-month halt (last pre-pause cargo March 8; exports redirected to Yanbu)** (Reuters via The National, Al-Monitor, 6/26). One TradeWinds item (Kpler: "no crude lifted since Saturday's drone attacks, eight VLCCs waiting") is UNDATED in the index and names a Saturday attack; the 11/25 attack was a Wednesday, so it is a **date mismatch, not evidence** for this event.
- Web search for the SOMO delay: nothing for 2026. Background only: Basra November loadings were cut by weather in several earlier years (Platts, Argus, MEES 2013, 2020, 2023 items). That makes weather a live, unexcluded cause.
- PortWatch (free, ArcGIS) has port-level data but its newest observation was 11/22 at my last probe, before the event; not re-probed. Kpler, Vortexa, LSEG terminal data: paid, not used. No site refused me tonight.

## 2. Barrels, if the reports were real

**Rate basis (FALCON's relay, not mine):** Ras Tanura loadings 2.95 mb/d October 1–25 against 4.16 September (Kpler via Asharq); over 5 mb/d pre-war (Reuters 6/26); **November rate UNKNOWN.** I use 3 mb/d, range 2.5–4.2.

| Halt length | Loadings delayed (central, range) | Delayed or lost? |
|---|---|---|
| 3 days | about 9 mb (7–13) | Delay. Saudi tanks and buyers' stocks absorb it; cargoes slip a few days |
| 7 days | about 21 mb (17–29) | Mostly delay, part loss if Gulf-side tanks fill and fields are cut |
| 14 days | about 42 mb (35–59) | Mostly loss: production would have to be shut in |
| 30 days | about 90 mb (75–126) | Loss |

**What limits the offset:** effective spare is near zero on both agencies (§ 4: EIA 0.01 mb/d for January 2027; IEA OPEC+ 0.45 mb/d in October, Saudi cell blank). Saudi's own bypass is the East-West line to Yanbu, which carried the whole export stream March to June, but it was attacked in September and the Red Sea side was hit at Jazan 11/25–26; spare Yanbu loading room tonight is UNKNOWN. Scale: the IEA's Q4 surplus forecast of +1.7 mb/d is about 155 mb over the quarter; a 7-day halt removes about a seventh of that, a 30-day halt more than half.

**SOMO:** 20–30 mb deferred out of November is about 0.7–1.0 mb/d of Iraqi exports for the month (Iraq supply 4.60 mb/d October, IEA OMR). If the cargoes load in December 1–10 as reported, it nets to zero over two months: a late-November gap in the Asian sour market, then extra December supply. **The sign depends on the cause, which nobody has given:** weather or port trouble (bullish prompt, neutral over two months), security or Hormuz (bullish prompt, risk of real loss), or buyers deferring (bearish: a sign of surplus). Nortilus's "Dubai moved to a prompt premium" (relay, WALTER -011 item 6) fits a supply gap better than weak demand; unverified.

## 3. Price, if real (my estimates, unscored, no registered row)

| Case | Brent February BZG27 (90.84 on 11/27) | Brent−WTI February (8.88) | Brent M2−M3 BZG27−BZH27 (2.79) | WTI February CLG27 (81.96) |
|---|---|---|---|---|
| Halt real, resumes within about 3 days | +$0 to 2, fading | +$0.5 | little change | +$0 to 1 |
| Halt real about 7 days, tracker-confirmed early next week | +$3 to 6 (about $94–97) | +$1 to 2 (to about $10–11) | +$0.5 to 1.0 | +$1.5 to 3.5 |
| Halt real 14–30 days, no bypass room | +$8 to 15 (about $99–106) | +$2 to 4 | +$2 or more; M1−M3 over +$10 | +$5 to 10 |
| SOMO alone, weather or port cause | +$0 to 1 | small | Dubai firmer than Brent | ~0 |

Anchors: Abqaiq, 16 September 2019 (5.7 mb/d out for days): Brent settled +14.6% on the first day and gave most of it back within about two weeks as restoration came faster than feared, with ample spare and stocks at the time; spare is near zero now, so the per-barrel response should be larger and slower to fade. This war's own tape: Thursday 11/26 (Jazan, the mine claim and the CNN report all on one day) moved Brent and WTI together, so it was not a Saudi-export read (`../2026-11-26_jazan-refinery/NOTE.md`). WTI moves least in every case: the US is the marginal replacement exporter, so a Gulf loss shows first in Brent, in Brent−WTI and in Dubai.

## 4. What the 11/27 tape says the market believes

| Read (vendor daily) | Wed 11/25 settle | Thu 11/26 last (f1) | Fri 11/27 settle | Wed→Fri |
|---|---|---|---|---|
| Brent Feb BZG27 | 90.64 | 92.19 | 90.84 | +0.20 |
| WTI Feb CLG27 | 82.35 | 83.98 | 81.96 | −0.39 |
| Brent−WTI Feb | 8.29 | 8.21 | 8.88 | **+0.59** |
| Brent M2−M3 (Feb−Mar) | 2.63 | 2.90 | 2.79 | +0.16 |
| Brent Feb−Apr BZG27−BZJ27 | 4.61 | — | 4.90 | +0.29 |
| Brent M1−M2 (Jan−Feb, Jan expires Mon 11/30) | 3.97 | 4.29 | 4.60 | +0.63 (expiry-distorted) |
| WTI Feb−Mar CLG27−CLH27 | 1.37 | — | 1.15 | −0.22 |
| Diesel crack Feb HOG27×42 − CLG27 | 69.12 | 70.72 | 70.55 | +1.43 |
| USO | 139.89 | (closed) | 137.77 | −1.5% |

**Reading:** flat price says the market does NOT believe in a multi-day halt: two sessions after the report Brent February is up 20 cents and gave back all of Thursday. The one spread pointing the "Saudi barrels missing" way is Brent over WTI, +$0.59 since Wednesday (+$0.67 on Friday alone, as WTI fell more), still under the roughly $1 widening I watch for a real Saudi loading loss. Prompt Brent structure firmed slightly against Wednesday and eased against Thursday. If the 7-day case is worth +$3–6 and +$1–2 on Brent−WTI, Friday priced a small fraction of it: I read that as the market treating the halt as unlikely or already short (my reading, unscored). ⚠️ Friday was a holiday-thin half session (US energy stopped printing at 13:00 ET) and January Brent expires Monday, so the structure reads are weak evidence.

## 5. D:L913, OPEC+ Sunday 11/29

- **Letter (CATALYSTS 2026-11-29 seven-country row, registered 11/1):** three outcomes on the Secretariat statement text only: (1) January HELD (fourth hold), (2) a stated January kb/d increment, (3) no January decision. **Ready to grade on Sunday as written; nothing graded tonight.**
- **Deliverability gate:** EIA COPS_OPEC re-pulled 19:14 EST, still the 11/10 vintage: **0.01 mb/d for every month October 2026 to March 2027** (0.6 April, 2.35 May–June 2027). **Second agency FOUND tonight** on the free IEA OMR November page (published 11/13; two consistent summarizing-fetch reads, 19:15 EST): **OPEC+ effective spare 0.45 mb/d, OPEC 0.22 mb/d, October 2026, excluding shut-in Iranian and Russian crude**; Saudi effective-spare cell BLANK (sustainable capacity 12.11 against October supply 9.99; Iraq 4.87 / 4.60; Kuwait 2.88 / 2.03). This supersedes the 11/14 grade's "spare NOT FOUND" (that grade worked from secondaries and named the free page only as a place the figure might be). The OPEC MOMR contest (Saudi-stated production 10.563 against supply 9.203, 11/11 note) still stands. Gate SUPPLIED tonight; one EIA re-pull on Sunday before grading keeps it literally "fresh" (one call; no new STEO before about 12/08).
- **Statement hour:** the 11/1 statement page carries `last-modified: Sun, 01 Nov 2026 12:03:18 GMT` (saved headers, `../2026-11-01_opec-december-grade/hdr_620.txt`), so **expect about 07:00 ET Sunday 11/29**, at `https://www.opec.org/pr-detail/<id>-29-november-2026.html`, probing upward from id 621. A session any time after about 08:00 ET Sunday can grade; Monday is inside the row's two-trading-day window.

## 6. Forward view to about 12/04 (unscored; no row stands behind these numbers)

| Call | Odds | Why |
|---|---|---|
| OPEC+ holds January (fourth hold) | about 80% | Effective spare 0.01–0.45 mb/d; Gulf exports route-limited; both agencies forecast a Q4 surplus; Saudi under attack. Holding costs nothing |
| A stated January increment | about 10% | Paper barrels for market share or politics (the US-lobbying story is UNVERIFIED); bearish headline, few real barrels |
| No January decision / deferred | about 10% | Ministers wait on Hormuz |
| Brent Feb stays $86–95 through 12/04 | about 55% | Ras Tanura resolves "resumed" or stays one report (FALCON 45% + 35%); the risk premium fades |
| Brent Feb settles above $95 at least once | about 25% | A tracker-confirmed multi-day halt (FALCON 15%) or a new Gulf hit; managed-money shorts at the highest level in my 15-row ledger (COT #15, 137,797) add squeeze fuel |
| Brent Feb settles below $85 at least once | about 20% | De-escalation or a convoy deal; the paper surplus reasserts |

**What would change my mind:** a relayed Kpler or Vortexa read showing no Ras Tanura or Ju'aymah liftings for 3 days or more, or an Aramco force majeure (moves me to the 7-day row); Brent−WTI February above $10 with Dubai firm; an OPEC+ statement naming a kb/d; COT #16 (Monday 11/30) showing heavy short-covering.

## 7. What moves on the record

No level, gate, threshold, prediction letter or position. BRT-32 (Yanbu window to 12/31) is untouched: Ras Tanura is not Yanbu. BG-02 not met (no quantity named). Combination watch: Ras Tanura report, SOMO delay and Kun Peng logged on combo:gulf-access-cost; China stockpiling forecast (Sen) on combo:paper-physical-gap. TERRY packeted.
