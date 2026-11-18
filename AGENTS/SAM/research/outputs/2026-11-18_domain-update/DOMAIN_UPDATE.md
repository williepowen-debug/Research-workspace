# SAM domain update through the 11/17 close — 2026-11-18

**Author:** SAM · **Written:** 2026-11-18 10:37 ET onward (clock) · **Wake:** PROME prome-6e, DOCKET L1183, Will's word WQ-709 (11/17 18:16 ET). Claude Code, Opus 5.5, desktop. Research only, $0. No level, gate, band, letter or prediction term changed.

Basis rules: USD/JPY from own vendor hourly bars, completed London-labelled sessions (WQ-162; bar count checked). JGB levels MOF basis only. Auction grades on the frozen 9/11 ruling (`thesis/AUCTION_GRADING_RULING_2026-09-11.md`: SOFT = BTC < 3.5 or tail > 2.0bp; FIRM = BTC ≥ 4.0 and tail ≤ 1.0bp). Words are words: they do not move the intervention ladder.

## 1. What moved, by SAM's own rules

| Series | Through 11/17 (source, clock) | Rule outcome |
|---|---|---|
| USD/JPY completed sessions | 11/12 **159.858** (24 bars now; H 160.044) · 11/13 **159.686** (H **160.188** 06:16 UTC, 22 bars, Friday) · 11/16 159.526 (H 159.862) · 11/17 **159.520** (H 159.612 / L 158.860) · 11/18 live 159.27 (15:32 UTC, not a session) | **TOUCH 160 again on 11/13 (second in two sessions), NO CLOSE above 160 in any session (last close above: 9/1).** 11/12 Close revised 159.873 → 159.858 once the 22:00/23:00 bars filled; the 11/12 grade stands. Speed row not fired: largest range 0.752 (11/17); two-session spans 0.885 (11/12–13), 1.002 (11/16 H 159.862 → 11/17 L 158.860), all under ~2–3 yen. |
| 11/13 06:16 UTC high | 160.188 → 159.643 by 06:39 UTC (−0.545 yen over 23 minutes); EUR/JPY fell with it (177.126 → 176.593), EUR/USD flat | Yen-wide but **gradual**, no single-minute jump. Unlike 11/12 11:43 ET (−0.705 inside one minute). No official act found. |
| JGB curve, MOF | 11/17: 2Y 1.878 / 5Y 2.274 / 10Y **2.925** / 20Y 3.787 / 30Y **4.069** / 40Y 4.101 (11/11: 1.861 / 2.214 / 2.840 / 3.696 / 3.990 / 4.029) | 30Y back **above 4.0 since 11/13** (4.038), first since early October. Bear steepener: 2Y +1.7bp, 10Y +8.5bp, 30Y +7.9bp, 40Y +7.2bp (11/11 → 11/17). Largest one-day 30Y move +6.4bp (11/13): gradual, under SAM-33's ~20–40bp disorder bar. |
| JGB 20Y auction 11/18 (#198) | Bids ¥1,914.0B / accepted ¥525.8B = **3.640×**; lowest 3.782 / average 3.756% ⇒ **tail 2.6bp** (MOF eresul20261118) | **SOFT** on the tail leg (2.6 > 2.0bp; margin 0.6bp, not precision-limited). BTC leg passes (3.640 ≥ 3.5). Second SOFT long-end auction in eight days (30Y 11/10 SOFT). Not a failure (BTC ≫ 2.0, no signal). The script's "Orderly" label is a different alert, not this grade. |
| 10Y inflation-indexed 11/16 | BTC 2.696× | Descriptive only (FIRM unreachable at this tenor per the 9/11 ruling). |
| BOJ meeting OIS (Totan, SAM visual review, SHA `24fd7b38…`) | **11/18 15:15 JST: Dec 84% / OIS 1.4388; Jan 14; Mar 56; Apr 24; Jun 32; cumulative 0.98 by Jan, 2.10 by Jun** (11/10: Dec 76, cumulative Jun 1.85) | Arithmetic chain checked (OIS differences and cumulative counts reconcile to rounding); ingested 5 rows. Incremental 25bp equivalents, not probabilities. ⚠️ Charts 11/11–11/17 were never reviewed: the path between 76 and 84 is not observed. |
| CFTC JPY, 11/10 (rel 11/13) | **Net +123,113 LONG**, Δ **+20,792** (longs +22,561, shorts +1,769); OI 388,875 | **Outside the ±12,160 deadband**; new high on the ledger (prior +120,359, 9/15). Speculators added yen LONGS into the week the yen touched 160: no short-yen fuel for an August-2024-style squeeze. Window ends 11/10, before the 11/12–13 touches. |
| MOF weekly foreign LT debt | 11/1–7 **−¥537.6B** (selling); 4-week +¥537.1B; 12-week −¥4.33T | Inside the ¥1.5T one-week bar. Week 11/8–14 publishes 11/19. |
| US–JP gap (rate_differential.py, retried after a fetch timeout) | 11/17 5Y **2.626pp** / 10Y **2.175pp** (11/12 peak 2.741 / 2.259) | Widened to 11/12 then narrowed slightly. SAM-41 is resolved; descriptive only. |
| Japan Q3 GDP, 1st prelim (ESRI 11/16, primary PDF; components layout-parsed) | **−0.0% q/q, −0.1% annualised**; private consumption −0.3%; net exports −0.6pt contribution; business investment +1.6% (press, matches) | First activity read spanning the September hike and the oil shock: soft, consumption-led. Did not stop December pricing rising (76 → 84). |
| Japan October trade (Customs sokuho 11/18) | Balance **−¥476.5B**; crude volume 11,273 thousand kL (**−0.7% y/y**), value +60.5%; LNG −26.1%; ME crude volume 8,972 thousand kL | Value rise is price, not volume. ⚠️ Script's branch "(a) Phase 1 back online" and the "$114/bbl vs $95 (+20%)" are on the Brent proxy whose repair is owed: **not a cost finding**. 🆕 **Middle East share of crude volume (own arithmetic): Aug 62.6% · Sep 62.0% · Oct 79.6% (provisional).** |
| Brent (vendor) | BZ=F $89.51 (15:22 UTC 11/18, not a settle) | Roll inside the lookback (guard): no percentage across it. BRENT owns marks. |

## 2. Intervention: what is now ESTABLISHED

1. **The US leg of the summer operation was ¥79.4B, all ESF, against euros, on 7/31; the Federal Reserve (SOMA) did not intervene.** FRBNY Q3 FX report (released 11/12; PDF retrieved 11/18, sha256 `64dcfa7f…`), p.5: *"the New York Fed purchased 79.4 billion yen in the spot foreign exchange market against the sale of euros from the Exchange Stabilization Fund"*; *"The Federal Reserve did not intervene in foreign exchange markets over the period."* Treasury's ESF August statement (via WALTER 20261113-004) says the same ($500M). Against Japan's ¥15,399.3B the US leg was **0.5%**.
   - Consequence for SAM's own record: STATUS_REFERENCE's line that the $87.8B reserve-securities fall being ~$10.8B short of the ~$98.6B operation is "consistent with a joint US leg" is **dead for any material size**: the US leg was about $0.5B and was funded from US euro reserves, not Japan's. The gap is valuation and other flows, unexplained. The 8/10 research file's "direct evidence the Fed leg may not be participating at all" is **confirmed**.
   - Katayama at MOF, 11/13, asked about ¥79.4B vs Japan's "over ¥5 trillion": no problem; joint statements and Bessent's "strong yen reflecting fundamentals" stand (MOF transcript my20261113).
2. **Katayama 11/13 words upgraded REPORTED → ESTABLISHED** (MOF transcript `my20261113.html`, read 11/18): volunteered in her opening remarks, *「為替市場の動向につきましては、足元で一方的に急激な動きが見られます。米国財務省とも緊密な連携を続け、適切に対応をしてまいります。」* ("one-sided, rapid moves at present; continuing close coordination with the US Treasury; will respond appropriately"). No "decisive action".
3. **11/17 press conference: no currency question or remark at all** (zero occurrences of 為替/介入; MOF `my20261117.html`). Words did not escalate as USD/JPY held 159.5.
4. No MOF statement since 8/3 (statement index read 11/18). No rate check or intervention reported in November in the press searched (11/18). Mimura 11/12 remains REPORTED only.
5. Ladder unmoved (words only). Official confirmation of any operation 10/29–11/26 is MOF's monthly total, ~11/30.

## 3. The intervention-funding question (OPEN with SAM, BOND, LIQUID) — SAM's leg

- **Capacity (MOF reserves 10/31, unchanged):** securities $834.6B, deposits $150.7B (≈ ¥24T at 160, ~1.6× the summer's ¥15.4T).
- **Who funds it:** on the only measured precedent, Japan funded essentially all of it (US 0.5%, from US euros). A repeat should be read as a Japan-funded operation unless a US statement says otherwise.
- **How Japan funds it:** still a hypothesis. August: securities −$87.8B, deposits −$6.9B against a ~$98.6B operation, with valuation and window mismatch. That leans to securities, **not identified UST sales**.
- **What 11/19's H.4.1 can and cannot show:** custody (BOND) and foreign repo / FIMA (LIQUID) move for every official holder; with **no operation established** for 11/12–13 (no close above 160, no official act, a gradual 11/13 pullback), a custody fall on 11/19 has no Japan event to attribute to. SAM's yen call for that read: **no Japanese operation is established in the 11/11–11/18 window.**

## 4. SAM-33 (OPEN, 72%) — November audit at the record

BOJ daily operations files `ope20261104` … `ope20261118` (11 files, read 11/18): outright JGB purchases only on **11/4** (≤1Y ¥100.0B, 1–3Y ¥330.0B, 25Y+ ¥75.0B) and **11/11** (1–3Y ¥330.0B, 5–10Y ¥305.0B, 10–25Y ¥85.0B), each on its `mpr261030c` date and the Sep-30 plan size. Other days: securities lending, a ¥800B two-week pooled-collateral supply (11/10, floating 1.25%), a same-day fixed-rate funds supply 11/11 (¥6B taken), and US-dollar operations. **No fixed-rate or unscheduled JGB purchase while the 30Y rose through 4.0. Falsifier un-fired through 11/18.** Next scheduled: 11/19 (3–5Y, 5–10Y, 25Y+), 11/26; December dates 11/30 17:00 JST.

## 5. SoftBank (PROME 11/16, reader finding F1) — graded

**F1 accepted.** My "25% at Arm about $145" assumed no net-debt drift since 9/30. Re-run on my full-revaluation model (`ltv_fx_sensitivity.py` inputs, fD 0.62, USD/JPY 158.63): no drift **$143**; + interest carry ¥0.125T (reader's pro-rating of SoftBank's Q2 bridge line, an estimate) **$146**; + SB7 settlement ¥140.2B **$147**; both **$150**. Corrected line: **"25% at Arm about $146–150 with interest carry and the SB7 settlement; about $143–145 assumes no net-debt drift since 9/30."** The 22.5% roll at Arm $183.26 stands (this run 22.4%). Reader's eight non-blocking findings noted; the untested-holdings point (other listed shares and OpenAI held at 9/30 in the 11/9 pro forma) is right and stays a known-unknown.
- **New, title only (WALTER 20261116-005):** "SoftBank Seeks Over $11 Billion in Junk Bonds for OpenAI Bet" (Bloomberg). Size, tenor, use not read. If it is new money for new OpenAI investment: about **+2.3 points** (22.4% → 24.7% at Arm $183.26, own arithmetic, debt and holdings both +$11B = ¥1.75T at 159.27). If it refinances existing bridge debt: about zero. Not established; LIQUID owns the bond read.
- "Arm boss Rene Haas approached in Nvidia CEO search" (FT headline, WALTER 20261114-006): logged, no LTV route.

## 6. Trade-assessment handoff (WQ-696)

**USD/JPY at 160 and intervention.** The evidence implies a capped grind: two completed-session touches of 160 (11/12, 11/13) with no close above, verbal resistance that did not escalate (11/13 words, 11/17 silence), and speculators long yen rather than short. **Horizon:** to the MOF monthly total (~11/30) and the BOJ decision (12/18). **Invalidation:** a completed close above 160 with a range ≥1.5–2% a day, or a nonzero MOF total for 10/29–11/26. **Unknown:** whether a rate check happened (none reported), offshore FX-swap funding, and how much of December's 84% is already the yen's support. **Investment implication:** none new from SAM. A Japan-led carry unwind is not supported (no short fuel); the asymmetric event is a Japan-funded operation near 160, whose timing these data do not identify. No TERRY packet from this read.

**JGB long end.** 30Y above 4.0 with two SOFT long-end auctions in eight days implies thinner demand at these yields, not a failure. Horizon: next 30Y auction (December) and the 11/25 40Y (descriptive). Invalidation: a FIRM long-end print. Unknown: buyer identity. No investment implication beyond BOND's long-end read.

## 7. Inbox, 22 files

5 packets + 17 WALTER cards (one, 20261118-007, arrived after PROME's count of 18). Dispositions → `board_log.tsv` (17 rows) and §8 of the PROME packet. Four named corrections receipted NO-OP (`registry/corrections_receipts.tsv`).

## 8. Known gaps

- Totan 11/11–11/17 charts unreviewed (not recoverable as reviewed quotes).
- ESRI GDP components parsed from a PDF layout; headline matches the press.
- US Treasury par-yield fetch timed out once at boot, succeeded on retry.
- Ueda 10/30 press conference, Outlook full text, September minutes: still unread.
