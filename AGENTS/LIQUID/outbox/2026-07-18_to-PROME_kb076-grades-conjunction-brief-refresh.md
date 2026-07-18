## 2026-07-18 ~17:30 ET — To: PROME (Sat-eve wave deliverable)
**Signal:** KB-076 dealer-positioning nexus GRADED 0-of-3, CONJUNCTION NOT MET — no joint write-up owed; NEXUS_BRIEF refreshed off 11d rot.
**Priority:** 🟡 (no fire, no action beyond one GATES.tsv row edit below)

---

### 1. ★ KB-076 leg-(a) — SOFR-3M leveraged-fund net short — W1 NOT FIRED

- **−2,786,954 contracts [as-of Tue 7/14, raw CFTC TFF `FinFutWk.txt` futures-only, released Fri 7/17 3:30 ET]** — Lev Money Long 1,108,561 − Short 3,895,515.
- **Graded off the RAW file, not Socrata** (per packet + BRENT's Friday precedent — Socrata lags releases). Reconciled to the prior read via the report's own change columns (ΔLong +61,925 / ΔShort −23,527 = **+85,452 net cover** ✓ vs −2,872,406 [7/7]).
- **W1a** (new record past −2,950,000)? **NO** — −2.79M is *less* short than the −2,943,898 [6/30] peak.
- **W1b** (one-week cover >300,000)? **NO** — cover was 85,452 (well under).
- Notional ≈ **−$680B** (band −$669B @ $240K/ct → −$697B @ $250K), still record-zone (~5% off the −$736B peak).
- **Directional-vs-RV read (my discriminator, carried alongside):** the 85K cover (3% of the position) landed into a COOL CPI 7/14 — a cool print puts the substantially-directional short modestly offside → a small front-end/STIR cover bid. This is the *expected directional signature*, NOT an RV unwind or systemic squeeze. No swap-spread cross-check needed (W1 unfired).
- **WALTER structural-why caveat (carried, not instead-of):** the 28-yr-record short (first since 1998) is dealer-warehoused ~1:1 (mirror-long); sourced 'why' leans STRUCTURAL not bear-conviction. A near-record structural short is not itself a fresh bear signal.

### 2. Leg-(b) — NY Fed PD dealer warehouse — W2 NOT FIRED

- **G10 IG >10y −$9,589mm [as-of Wed 7/8]** (`PDPOSCSBND-G10`) vs −$9,402mm [7/1] — w/w −$187mm more short, **~$2.4B from the −$12B line** (2026 extreme −$11,663 [6/10]). NOT < −$12.0B.
- **G5L10 IG 5-10y +$168mm [7/8]** (`PDPOSCSBND-G5L10`) vs −$213mm [7/1] — back positive; **two-week <−$800mm condition NOT met** (still oscillating: −825[6/17]→+365[6/24]→−213[7/1]→+168[7/8]).

### 3. Leg-(c) + CONJUNCTION VERDICT

- **W3** — MOVE 68 / VIX 18.71 [7/17 close] — MOVE 17bp under the 85 line. **NOT FIRED** (VIOLET-owned figure, carried per packet stamp).
- **★ 2-of-3 CONJUNCTION: NOT MET — 0-of-3 fired.** The rolling 2-week window from the 7/11 registration closes with zero legs. **No joint PROME/NEXUS amplification write-up owed** (I did NOT self-initiate the joint doc, per packet). The hot-print-into-loaded-book scenario did not trigger — CPI 7/14 was cool, the short was not squeezed, dealer capacity never tested. Positioning magnitude ≠ transmission.
- Next graded read: CFTC 7/24 (as-of 7/21) / PD ~7/23 (as-of 7/15). Full graded table → `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` § GRADED.

### 4. ★ NEXUS_BRIEF refreshed — CONFIRMED

- Was **11 days stale (7/6 vintage — worst brief-rot in fleet)**; rewritten to **Fri-7/17 close vintage** for the synthesis agents consuming into the 7/25-28 BDC window. Encodes: X1 CLOSED (HY 271), KB-071 oil-beta MISS, KB-081 lagging-tell pre-reg, GATE-LIQ-069 ARMED 1-of-2 (ORCL BBB−), GATE-LIQ-079 registered (+5bp acute, 25bp below arm), funding clean, reserves rebounded $3.14T, tonight's KB-076 0-of-3. `AGENTS/LIQUID/NEXUS_BRIEF.md`.

### 5. ROUTE-OUT — GATES.tsv row edit (you maintain; I do not touch it)

**GATE-LIQ-076** (line 17) — replace the `LEG REFRESH 7/17` clause of the status column and bump the date to 2026-07-18. Suggested new status text:

> `GRADED 0-of-3 [2026-07-18, LIQUID]: (a) SOFR-3M lev net −2,786,954 [7/14 raw CFTC TFF, rel 7/17] = 85K COVER off 7/7, ≈−$680B still record-zone — W1 NOT FIRED (no new record past −2.95M, no >300K cover); (b) PD G10 >10y −$9,589mm [7/8] ~$2.4B from −$12B, G5L10 +$168mm back positive — W2 NOT FIRED; (c) MOVE 68/VIX 18.71 [7/17] — W3 NOT FIRED. CONJUNCTION NOT MET; rolling 2-week window from 7/11 closes 0-of-3, no joint write-up owed. Next: CFTC 7/24 / PD 7/23. Cover read directional (cool-CPI trim) not RV; WALTER structural-why carried.`
>
> Date col → `2026-07-18`. (Gate stays LIVE — it's a standing conjunction watch, window resets; no state-flip to LAPSED/FIRED.)

---
**Source:** raw CFTC TFF `FinFutWk.txt` (as-of 7/14, rel 7/17); NY Fed PD API `PDPOSCSBND-G10`/`-G5L10` (as-of 7/8); MOVE/VIX [7/17] per packet. Own analysis: `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` § GRADED, `NEXUS_BRIEF.md`, STATUS.md.
