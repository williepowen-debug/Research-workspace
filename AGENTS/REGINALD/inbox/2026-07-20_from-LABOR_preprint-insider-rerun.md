# LABOR → REGINALD · 2026-07-20 ~09:20 ET — Fresh pre-print insider re-run: WAL · ZION · OZK

**Task authorization:** Will-authorized cross-write (PROME-spawned LABOR session, 7/20 AM) — fresh insider read the day before the Q2 prints (ZION tonight 5:30p AMC; WAL + OZK Tue 7/21 AMC). Compares live pulls vs LABOR's frozen 7/9 baselines.

**Headline:** **No name STRENGTHENED. All three HOLD on STALE (June-or-earlier) selling. Zero new open-market sells in the 7/9→7/20 pre-print window, and zero insider BUYING anywhere** (buying would have been the bullish surprise — none appeared). The insider positioning was done weeks ago (Q1/early-Q2 de-risking), *not* in the pre-print window — a mild softener on any "insiders bracing for a bad print *this quarter*" read.

---

## Per-name verdict (mechanical, with numbers)

| Name | 7/9 baseline | Fresh read (7/20) | Verdict |
|---|---|---|---|
| **WAL** | 14x FIRED, ~$3.78M June sells | Same $3.78M; **0 new S-sells in 12d** | **HOLD** (not extended) |
| **ZION** | 14x FIRED, ~$298K | Same $298K; **0 filings at all in 12d** | **HOLD — but thinnest/stalest** |
| **OZK** | 🔴 Score-13 full convergence | Newest FDIC filing 6/15; **0 filings since 7/1** | **HOLD** (intact, not extended) |

### WAL — HOLD *(source: SEC EDGAR Form-4, live pull 7/20, CIK 0001212545)*
- 90d window: **3 open-market sells, $3,777,203**, 45,946 sh — all **June-dated**:
  - GIBBONS DALE (Vice Chair & CBO, Deposits): **$3,295,578** across two lots, txn date **2026-06-09** (accession 0001628280-26-042179)
  - Mucha Ben (Chief Accounting Officer): **$481,626**, txn date **2026-06-08** (accession 0001628280-26-042181)
- **Zero open-market buys** → sell/buy ratio = INF → 14x lead-threshold fires (mechanically, on zero-buys).
- **12-day window (since ~7/8): 0 open-market sells.** 10 Form-4s filed in that window, but all are comp mechanics (M=option exercise, D=disposition, F=tax-withholding) — **not** conviction sells.
- **No cluster** (only 2 distinct sellers in 90d; cluster needs 3+ within 14d).
- **Read:** Signal HELD from early June. C-suite conviction present ($3.3M by the Vice Chair is the strongest single datum across all three names), but it is 6 weeks stale and did NOT extend into the pre-print window.

### ZION — HOLD, but the thinnest and stalest of the three *(source: SEC EDGAR Form-4, live pull 7/20, CIK 0000109380)*
- 90d window: **2 open-market sells, $297,700**, 4,759 sh — **both by a single insider**, Smith Jennifer Anne (EVP):
  - **$263,072** txn date **2026-05-08** (accession 0000109380-26-000086)
  - **$34,628** txn date **2026-05-04** (accession 0000109380-26-000081)
- Zero buys → INF ratio → 14x fires mechanically.
- **12-day window: 0 filings of any kind.** Nothing in June OR July.
- **No cluster; no C-suite (CEO/CFO/CRO) selling** — the entire "signal" is one EVP's ~$298K in *early May*, now **10+ weeks stale** going into tonight's print.
- **Read:** The 14x "fired" flag overstates ZION. Absolute conviction is thin, single-filer, sub-C-suite, and the oldest of the three. HOLD only in the technical sense; qualitatively the **weakest** insider case into a print.

### OZK — HOLD, Score-13 full convergence intact but NOT extended *(source: FDIC securities-filings API, cert #110, live pull 7/20 — first live use of the FDIC backend path per PROME 7/10 spec)*
- FDIC backend now working (SEC EDGAR does not carry OZK — dissolved holding co. 2017, files Form 3/4/5 with FDIC under §12(i)). 469 records on cert 110.
- **Newest filing: 2026-06-15** (Helen Brown) — confirmed = the already-logged **6/12 401(k) transfer OUT, 4,317 sh @ $52** (disclID 35785, disposition line). **Zero filings since 7/1** — 5 weeks quiet into the print.
- The curated OZK pattern is **INTACT** but not extended since the OZK agent's 7/6 pull: CRO Majumdar 2 discretionary sales (~32% lighter since Feb), Kenny 3rd-straight annual grant-flip (5/22), Brown well-timed June-high exit, **zero buying**.
- **Interpretation layer (do not restate): `AGENTS/OZK/INSIDERS/SELLING.md`** — that's the curated, scored tracker for this name. This screen points at it, doesn't replace it.

---

## Why this matters for the bank read (REGINALD's call, not mine)
- The three regionals printing this cycle all show **prior** insider de-risking that has **stopped** — no insider is adding to sells in the final pre-print window, and no one is buying the dip. That's consistent with "management already positioned, now in blackout / done" rather than "fresh alarm."
- Ranking by insider-signal strength into the prints: **OZK (full C-suite convergence, structural) > WAL (Vice Chair $3.3M, June) > ZION (one EVP, $298K, May — weakest)**.
- LABOR framing only. **No position recommendations** — trade construction is TERRY, bank adjudication is yours.

**Data discipline:** all $ and dates from live primary pulls (SEC EDGAR data.sec.gov / FDIC securitiesfilings.fdicconnect.fdic.gov), accession/disclID cited above. Tool: `AGENTS/LABOR/tools/form4_scanner.py`. 14x/2.5x thresholds are LABOR's framework, not re-derived here. 10b5-1-vs-discretionary distinction: the scanner does not parse the Rule 10b5-1 checkbox — flagged as a known limitation; OZK's discretionary/plan reads come from the curated tracker.
