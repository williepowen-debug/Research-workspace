# DR-5 — LNG as a target class: the reaction function, and who actually absorbs the loss
**Date:** 2026-08-12 | **Mode:** Thesis | **Confidence:** High (price reaction functions and the ownership chain — all PRIMARY, reproducible) / **NOT ANSWERED** (global FSRU register; war-risk premia post-Damietta)
**Commission:** WALTER DR-5, `REQ-DEWEY-20260731-005` | **Consumers:** FALCON action; BRENT/HAWK/SHADE info
**Engine:** primary-pull only (Will-ruled for this session). Fan-out is re-gated to user-invoked, not removed.

> **⚠️ SCOPE, stated rather than left to drift.** DR-5's phrase *"exposure surface of LNG infrastructure to kinetic risk"* is read here as **financial** exposure: who owns the assets, who bears the loss, and how the market repriced. This run builds **no** vulnerability assessment, no defensive-gap analysis, and no facility-by-facility risk ranking — the deliverable is loss-absorption and reaction-function arithmetic off public commercial and regulatory data, following the discipline note WALTER attached to DR-3. The liquefaction-geography leg is **deliberately not built** for this reason; see §Gaps.

---

## Key Finding

**Kinetic LNG events do not move gas prices up. In this sample they move them down, and FALCON's unadjudicated "real but non-transmitting" hypothesis is CONFIRMED on both benchmarks independently.**

Across five dated LNG kinetic/force-majeure events, **10 of 10 event-windows produced a negative 5-day return** — TTF mean **−6.37%**, JKM mean **−1.84%**, against unconditional 5-day means of **+0.79%** and **+0.75%** respectively. And on the biggest event of all:

| | pre-strike 2026-03-23 | 2026-07-01 | today 2026-08-12 |
|---|---|---|---|
| **TTF** (EUR/MWh) | 56.68 | 42.78 (**−24.5%**) | 60.49 (**+6.7%**) |
| **JKM** (Asia) | 21.00 | 16.02 (**−23.7%**) | 21.18 (**+0.9%**) |

**A 17%-of-Qatari-capacity outage with a 3–5 year repair horizon was declared on 2026-03-24, and three months later both European and Asian gas were ~24% BELOW their pre-strike levels.** Five months on, the Asian benchmark — the one most directly exposed to Qatari supply — is **+0.9%**. FALCON's read was correct for the period it covered.

**And the loss-absorption answer is the opposite of the obvious one.** The FSRU struck at Damietta (**Energos Winter**, 2026-07-29) is owned by Apollo-managed funds — and **New Fortress Energy exited that specific vessel in November 2025**, early-terminating the charter and novating the sub-charter for $150.0M across four vessels [PRIMARY: NFE 10-Q, period 2026-06-30, filed 2026-08-06]. **The US-listed name has no charter and no balance-sheet exposure to the struck hull.** The loss sits with Energos/Apollo — **which is itself in a restructuring support agreement with NFE signed 2026-03-08.**

---

## Evidence

### (1) The reaction function — FALCON's instrument-design deliverable

**Event windows, TTF (EUR/MWh) and JKM (Asia benchmark)** [PRIMARY: `TTF=F` / `JKM=F`, daily closes]

| event | | TTF t0 | TTF t0→t+5 | TTF t0→t+10 | JKM t0→t+5 | JKM t0→t+10 |
|---|---|---|---|---|---|---|
| 2026-03-24 | Ras Laffan strike / QatarEnergy FM | 54.04 | **−6.1%** | −16.2% | **−1.9%** | −5.0% |
| 2026-07-22 | FM prep to extend into mid-Oct | 62.54 | **−3.4%** | −16.2% | **−2.6%** | −4.9% |
| 2026-07-28 | FM extended to Asian buyers | 57.74 | **−3.1%** | +1.7% | **−0.7%** | −0.7% |
| 2026-07-29 | **Damietta** — drone hits FSRU *Energos Winter* + LNGC *GasLog Salem* | 60.42 | **−13.3%** | +0.1% | **−2.4%** | — |
| 2026-08-01 | *GasLog Shanghai* struck in Hormuz | 59.07 | **−6.0%** | — | **−1.6%** | — |
| | **mean** | | **−6.37%** | | **−1.84%** | |
| | *unconditional 5d mean (2y)* | | *+0.79%* | | *+0.75%* | |

**10 of 10 negative.** The largest single reaction is Damietta at **−13.3%** on TTF — a drone striking a US-managed FSRU and an LNG carrier at a Mediterranean port, followed by European gas falling 13% in five sessions.

**Adversarial check — is this just mean reversion?** The events cluster near local highs (87.4–100.0% of their trailing 20-day high), so post-event weakness could be reversion rather than response. Matched control — **all days at ≥87.4% of their 20-day high** — gives a 5-day mean of **+0.41%** and is **negative only 49% of the time**, versus 100% for the event days. So clustering does *not* explain the result. **But n is small and the events are not independent** (four fall within ten days, and TTF/JKM are correlated), so effective n is closer to **two episodes × two correlated benchmarks** than to ten. Formally: event mean vs control differs by ~1.3 SE — **not significant at any usable level.**

> **What this therefore supports is the strong NEGATIVE claim, which is what FALCON needs for instrument design:** there is **no evidence** that LNG kinetic or FM events produce a positive gas-price reaction, and **an instrument keyed to "LNG strike ⇒ gas price spike" would have fired wrong 10 times out of 10.** It does **not** support trading the events short.

### (2) FALCON's registered open question, answered

`VX-FALCON-GASLNG-01` carries this explicitly: *"OPEN AND NOT ADJUDICATED BY ME: no verified JKM/TTF series. If Asian/European gas absorbed a 17% Qatari outage for four months WITHOUT repricing, the loss is REAL BUT NON-TRANSMITTING — which cuts the other way and is a finding in itself."*

**Adjudicated: the loss was real and did not transmit for ~3.5 months.** Both benchmarks fell ~24% from pre-strike into July. Net from 2026-03-23 to today: **TTF +6.7%, JKM +0.9%.**

**Transmission did eventually appear — but through STORAGE, not spot, and with a ~4-month lag.** TTF ran +41% from the 7/1 low (42.78 → 60.49). My same-day DR-4 work identifies what changed: EU storage is at **59.32% — the lowest for the date in five years**, with 90% now unreachable at any pace demonstrated in four years, and **LNG send-out −20.4% YoY at only 38.3% utilisation** (cargoes, not regas capacity). **The outage was absorbed by drawing down the refill, and repriced only once the refill deficit became arithmetically undeniable.** That is a mechanism finding, and it is the bridge between DR-4 and DR-5.

### (3) Who absorbs the loss — primary-verified, and the vintage check reversed the answer

**The ownership chain, from NFE's own filings** [PRIMARY: NFE 10-Q period 2026-06-30, filed **2026-08-06**, accession `0001749723-26-000106`, CIK 1749723]:

- **Aug 2022 — "Energos Formation Transaction":** NFE transferred **eleven vessels** to Energos (an Apollo Global Management affiliate) for **~$1.85bn cash + a 20% equity interest.** Ten remained subject to NFE charters, which **"prevent the recognition of the sale"** — treated as a **failed sale leaseback**, so those ten stayed on NFE's balance sheet as PP&E with the proceeds recognised as debt.
- **Feb 2024:** NFE **"sold substantially all of our stake in Energos"** — completed **2024-02-14**, proceeds **$136.365M**, loss **$7.222M**, plus a **$5.277M** OTTI recognised in FY2023. NFE retained a residual **$1.0M** interest and **"no longer has significant influence."**
- **⚠️ Nov 2025 — the decisive fact:** NFE **"early terminated the long-term charter agreements with Energos for Energos Eskimo, *Energos Winter*, Energos Igloo and Energos Freeze and novated associated sub-charter agreements … in exchange for cash consideration of $150.0 million. This transaction resulted in the sale of these vessels that were previously accounted for as a failed sale leaseback. The Company no longer recognizes charter revenues and vessel operating expenses associated with these vessels."**
- **Mar 2026:** NFE entered a **restructuring support agreement with Energos** (2026-03-08, amended 2026-03-17), cancelling its forward-starting charter for *Nusantara Regas Satu*; NFE expects to recognise a **~$40.0M non-cash loss** on derecognition.

**So at the 2026-07-29 strike: the Energos Winter was owned by Apollo-managed funds, with NFE holding no charter, no sub-charter and no balance-sheet recognition.** The loss falls to **Energos/Apollo and its insurers** — an owner that is itself party to a restructuring, which is materially relevant to loss-absorption capacity.

> **This is why the vintage check mattered.** NFE's **Q1-2024** 10-Q states NFE was sub-chartering *"the Winter"* and carried **$1.287bn** of Energos vessels as a failed sale leaseback. Reported from that vintage, DR-5 would have told FALCON and SHADE that a **US-listed company had direct balance-sheet exposure to the struck hull.** The November-2025 transaction reverses it. `[[finding_deep_research_stale_vintage_headline]]`

### (4) The two precedents, dated

- **Ras Laffan / Mesaieed — 2026-03-24.** Iranian missile strikes damaged two trains; QatarEnergy declared force majeure. **~12.8 Mtpa ≈ 17% of Qatar's LNG export capacity**, repairs estimated **3–5 years**, ~$20bn/yr revenue. Lengthening rather than healing: Edison cargoes cancelled through end-September, extension prepared into mid-October, **extended to Asian as well as European buyers 2026-07-28** — a fourth month. *[FALCON `VX-FALCON-GASLNG-01`, FALCON-verified at primaries; Bloomberg 7/22 + 7/28, CNBC 7/1, Al Jazeera 3/24]*
- **Damietta — 2026-07-29.** A drone struck the FSRU **Energos Winter** (US-managed, Apollo-owned), with fire spreading to the LNG carrier **GasLog Salem** alongside. Crews evacuated, **no fatalities**. Egyptian Cabinet attributed the blaze to a drone. **Attribution not formally established — no actor claimed responsibility**; Windward reports Iranian state television named Damietta as a retaliation target two days prior, which is suggestive but commercial-secondary and should not be carried as attribution. *[Al Jazeera 7/29; CNBC 7/30; Egypt Oil & Gas; Riviera; Windward]*
- **Third event, same cohort — 2026-08-01.** *GasLog Shanghai* (Qatari cargo) struck by projectile in Hormuz; engine room, blackout, not-under-command, no casualties. **Twice in four days on the same operator's hulls** (Salem 7/29, Shanghai 8/1) — FALCON's observation, confirmed here by vessel name.

---

## Counter-Evidence

1. **The reaction-function result is directionally unanimous but statistically weak.** n≈2 independent episodes; ~1.3 SE. Do not register a threshold on it without more events.
2. **Over-determination cuts both ways.** July's +41% TTF move coincides with the FM extension, the storage deficit, Damietta, Hormuz escalation and the Libya/Egypt channel impairments. I attribute it to storage on mechanism grounds (DR-4's arithmetic), **not** on an identified causal test.
3. **"Non-transmitting" may be a statement about the starting point, not the shock.** Gas entered March 2026 well supplied; a 17% Qatari loss into a *tight* market could transmit immediately. The finding is conditional on the 2026 supply state.
4. **`JKM=F` instrument identity is NOT verified.** Its Yahoo metadata returns `quoteType: ALTSYMBOL`, `currency: None`, `shortName: None` — unlike TTF, which confirmed cleanly as *"Dutch TTF Natural Gas Calendar,"* EUR. The level (~21) is consistent with JKM in USD/MMBtu, but **I have not verified it is the Platts JKM benchmark.** It is therefore used for **percentage changes only** (unit-invariant) and **no JKM level is quoted as a datum.** `[[finding_number_carries_threshold_unit_source]]`
5. **Loss absorption ≠ loss magnitude.** I establish *who* holds the Winter, not what the casualty cost or the insurance recovery is. No claim, no premium, no P&I response was located.
6. **Energos fleet composition (13 vessels: 9 FSRUs, 2 FSUs, 2 LNGCs) is COMPANY-SECONDARY** — from Energos' own site and trade press, not a filing. Apollo funds are private; there is no equivalent of NFE's 10-Q for Energos itself.

---

## Gaps — PARTIAL delivery, 2 of 5 legs unmet

| Asked | Status |
|---|---|
| **JKM/TTF reaction functions to both events** | ✅ **answered — and it is the headline** |
| **The two 2026 precedents end-to-end** | ✅ **answered**, third event added |
| **FSRU fleet register + ownership, VERIFY at primaries** | ⚠️ **PARTIAL** — the **Energos/Apollo chain is fully primary-verified** (the leg the prompt singled out); a **global FSRU register is NOT built** |
| **War-risk insurance state, premia post-Damietta** | ❌ **NOT FOUND — explicit negative.** No LNG-specific post-Damietta premium, P&I response or AWRP revision located. FALCON's `WARRISK.tsv` remains the newest primary (**Marsh, Hormuz hull 7.5–10% of hull value, as-of 2026-07-22**), and its own staleness field marks it stale by 2026-08-03. **⚠️ Do not fill this with the beinsure "12× + $20bn DFC backstop" figure — FALCON logged that as a vintage trap dated 16 March 2026.** This is the leg SHADE most needs and it is **open** |
| **Liquefaction geography vs conflict zones** | ⛔ **DELIBERATELY NOT BUILT** — see the scope note at the head of this report |

---

## Reproduction

```
TTF / JKM : yfinance TTF=F, JKM=F, daily Close, period 2y
            VERIFY currency at .info before quoting any LEVEL (TTF=EUR confirmed; JKM=F does NOT confirm)
            event study: t0 = last close <= event date; fwd 5d/10d; matched control = days at
            >= min(event % of trailing 20d high) of their own 20d high
NFE       : scripts/edgar_doc.py search '"Energos"' --cik 1749723 --startdt 2026-01-01
            scripts/edgar_doc.py doc --cik 1749723 --accession 0001749723-26-000106   (10-Q, period 2026-06-30)
            then grep LOCALLY filtering 'us-gaap:|xbrli:|iso4217'  (per scripts/BACKLOG.md 2026-08-02)
```
⚠️ **Always pull the CURRENT filing.** The Q1-2024 10-Q (`0001749723-24-000052`) supports the *opposite* conclusion on NFE's exposure to the Energos Winter.

---

## Process Report

**Searches run:** 3 WebSearch (Damietta; Energos ownership; post-Damietta war-risk — the last returned nothing usable). Primary pulls: TTF/JKM 2y + metadata, 2 EDGAR full-text searches, 2 NFE 10-Q document pulls.
**Data gaps:** war-risk premia post-Damietta (the SHADE leg — open); global FSRU register; casualty/insurance loss magnitude.
**Source frustrations:** `edgar_fetch.py` **threw an unhandled traceback** on a CIK list attempt (`urllib` HTTPError path) — `edgar_doc.py search` worked and was used instead; the same "a probe must never traceback" lesson already logged for `fetch_url.py` on 2026-08-02 applies to `edgar_fetch.py` and is now in BACKLOG. `JKM=F` returns data but will not confirm its own identity at metadata.
**Errors caught in-run (1, and it was the load-bearing one):** I had the NFE/Energos Winter link established from the **Q1-2024** 10-Q — NFE sub-chartering the Winter, $1.287bn of failed-sale-leaseback vessels on balance sheet — and it would have made a striking finding: *a US-listed company with direct exposure to the struck hull.* Pulling the **current** (Q2-2026) filing showed NFE **exited that vessel in November 2025.** The finding inverted. Nothing in the 2024 document was wrong; it was simply 2.5 years stale, and the strike is 2026.
**Confidence:** High on the reaction functions and the ownership chain (primary, reproducible). The "non-transmitting" adjudication is **High on the fact** (both benchmarks, ~24% down) and **Medium on the mechanism** (storage-mediated transmission is inferred from DR-4's arithmetic, not causally tested).
**If I had more time/tools:** the war-risk leg — it is the one SHADE actually needs, and it needs a source I do not have (Lloyd's/P&I circulars, broker notes).
**Suggestions:** `edgar_fetch.py` needs the same transport-error guard `fetch_url.py` got on 8/2 — logged. The event-study harness (matched-control-by-proximity-to-rolling-high) is reusable and currently dies with this session; a candidate for `scripts/` **if** a second commission needs it. Will-gated; not promoted.
