# WQ-341 OBSERVED branch — VULCAN's bounded sub-read: do the AI-disrupted single-B incumbents explain the B-tier widening on 9/29 and 10/7?

**VULCAN · Fri 2026-10-09, written ~10:30 ET (`date`) · Will-launched session; the ask is NEXUS → PROME (`PROME/inbox/2026-10-09_from-NEXUS_wq341-observed-branch-attribution-asks.md`, `4994ec168`), pre-authorized by Will 10/3 (WQ-341).** Attribution only. It installs no root and no "non-root", and it contains no trade words. LIQUID's companion tier read: `AGENTS/LIQUID/analysis/2026-10-09_wq341-LIQ07-attribution.md`.

## ANSWER (one paragraph)
**On the letter, the mechanism leg FAILS: the named single-B incumbents were FLAT on both OBSERVED sessions ⇒ the OBSERVED result is IN-LETTER ONLY (Disc-A).** Four issuers have verified single-B US HY ratings and an AI or cord-cutting disruption story: Lumen, Cable One, Conduent, and McGraw Hill (a split rating). On **9/29** three of the four moved within |z| ≤ 0.2 of their own beta-adjusted noise; on **10/7** all four were within |z| ≤ 0.3. The one exception is Cable One on 9/29 (−13.0%, z −1.8), which follows S&P's 9/25 downgrade to B+ and is too small an issuer to move the index. There was **no dated AI-disruption event on 10/7**. On 9/29 OpenAI's DevDay launched always-on agents, and the incumbents did not react that day. Two further results point the same way, both outside the letter. **9/30:** Concentrix printed after the 9/29 close a $1.05B goodwill impairment explicitly blamed on clients' AI adoption, and on 9/30 B OAS was **flat (0bp)** while the named B incumbents were flat to up. **10/8:** the incumbents ROSE (median z +0.6) while AI enablers fell, which is the opposite sign to the mechanism, yet B widened +7. ⚠️ The test uses **equities as the instrument because bonds and CDS are unreachable from this box**, and it is a same-day test, so it cannot exclude credit catching up to the large equity damage of 9/15→9/28 (see §4).

## 1. Who the AI-disrupted single-B incumbents are (ratings verified by a fresh sourced search 10/9 — never from memory)
| Issuer (ticker) | Sector · why "disrupted" | Rating, agency, date | Single-B? |
|---|---|---|---|
| **Lumen (LUMN)** | legacy telecom/enterprise network; AI rewires enterprise traffic | Moody's B2 corp; S&P B- issuer, unsecured B (2026-02-23; 10-Q 8/4) | **Y** |
| **Cable One (CABO)** | cable broadband; cord-cutting + the Muse "agent negotiates your cable bill" demo (9/23) | S&P **B+ CreditWatch neg (2026-09-25)**; Moody's B1 (2025-12-22) | **Y** |
| **Conduent (CNDT)** | BPO / transaction processing — direct AI-substitution target | Moody's B2 neg (2025-09-16; a B3 cut 2026-04-21 is snippet-only); S&P B (2025-10-11, press) | **Y** |
| **McGraw Hill (MH)** | education publishing — AI-tutoring substitution | Moody's **B1** (upgraded 2026-07-27) / S&P **BB-** (upgraded 2026-09-18) | **SPLIT** |
| *Charter / CCO Holdings (CHTR)* | cable; LIQUID's withdrawn 9/29 attribution | corporate Ba2/BB+ (snippet); CCO unsecured notes **B1 / BB-** | *boundary — index bucket UNVERIFIED* |
| *Advantage Solutions (ADV)* | marketing services | S&P downgraded + CreditWatch neg 2026-02-13, **level not found** | UNVERIFIED |

**Excluded on the ratings, so not in the B index:** Getty, Optimum (ex-Altice), Rackspace and iHeart are **CCC**. Sirius XM, Ziff Davis and Concentrix are **BB or investment grade**. TTEC has no bonds. Clarivate's current rating was **not found** (last seen B1/B, 2021).
⚠️ **The B-tier universe is THIN:** most of the obvious AI-disruption names have already migrated to CCC, which is consistent with LIQUID's finding that CCC led on all three sessions. No 2026 source was found that calls a *named* US single-B HY issuer "AI-disrupted"; coverage (MSCI, UBS) is sector-level only.

## 2. Did they move against the B index? (daily total return; z = (return − β·SPY) ÷ σ, with β and σ fitted 2026-03-02 → 09-23, out of sample)
| Issuer | 9/29 (W) | 10/7 (W) | 9/30 (Concentrix day, out-of-letter) | 10/8 (OUT-OF-LETTER) |
|---|---|---|---|---|
| LUMN | +0.2% (z +0.2) | 0.0% (z +0.1) | +1.1% | −5.9% (z −1.3) |
| CABO | **−13.0% (z −1.8)** | +1.9% (z +0.3) | +0.8% | +16.4% (z +2.3) |
| CNDT | +0.6% (z +0.2) | −1.2% (z −0.2) | −1.3% | −1.9% (z −0.3) |
| MH | +0.6% (z +0.2) | +0.9% (z +0.3) | +4.2% | +2.1% (z +0.6) |
| *CHTR (boundary)* | −0.7% (z −0.2) | −1.5% (z −0.4) | +0.2% | +2.5% (z +0.7) |
| **B OAS (FRED)** | **+7bp** | **+6bp** | **0bp** | **+7bp** |
| SPY | −0.18% | −0.24% | −0.21% | −0.42% |

Data: yfinance closes via the repo `.venv` (auto-adjusted), pulled 2026-10-09 ~10:15 ET. B OAS is `BAMLH0A2HYB` per NEXUS's grading log, latest-revised.
- **Verdict on the letter (ask item 2):** *"Flat ⇒ the OBSERVED result is in-letter only (Disc-A) and the mechanism leg fails."* They are flat, so it fails.
- **Cable One 9/29** is the only large move, and it is issuer-specific: the S&P downgrade came 9/25 and the stock was −32.5% over 9/15→9/28. One issuer's few billion of bonds cannot carry a +7bp move in an index of several hundred issuers.

## 3. Dated AI-disruption news (ask item 3)
| Date | Event | In the window? |
|---|---|---|
| Tue 9/29 | OpenAI DevDay: "Dots" always-on agents inside Slack/Teams + an Agents API with computer use (CNBC live blog 9/29) | Yes — a genuine disruption-face event, but the named B incumbents did not move (§2) |
| Tue 9/29, **after the close** | Concentrix Q3: $910M operating loss incl. a **$1.05B goodwill impairment**, Q4 guided −3–5%, citing clients adopting AI faster (8-K Ex-99.1, SEC primary, acc 0001803599-26-000147) | Lands **9/30**, and B OAS was **0bp** on 9/30. Concentrix is investment grade (Baa3/BBB-/BBB), so its own bonds sit outside HY |
| Wed 10/7 | **None found.** AP attributed the tape to global yields; BofA called the Muse fears on Spotify overblown | — |
| Thu 10/8 | FT: OpenAI ~$50B revenue run-rate (a counting-basis gap) | OUT-OF-LETTER. It hits AI **enablers**, not incumbents |

The Muse scare itself (Meta launched it ~9/8–9/9) sold off on **9/22**: financials −2%, Goldman's "consumer inertia" basket −2.6%. The cable link is the 9/23 Connect demo. No source ties Charter or Comcast share moves to Muse. **All of it predates the graded window**, and 9/25 is excluded as in-sample.

## 4. What this does NOT establish (caveats that change the reading)
1. **Equities stand in for credit.** Bond prices (TRACE) and single-name CDS are not reachable from this box. Bonds can widen while the stock is flat, so a credit-instrument read could still overturn this result.
2. **Lag is not tested.** These names fell hard over **9/15→9/28** (CABO −32.5%, CHTR −21.1%, LUMN −19.0%, CMCSA −10.8%, CNXC −12.9%, GETY −63.8% vs SPY +1.3%). Credit catching up to that equity shock over the following sessions would satisfy the letter and leave the stocks flat on the day. A same-day test cannot exclude it. LIQUID's lagged-RATES model does not address this either; it is a lagged-EQUITY channel.
3. **Small and partly snippet-sourced.** n=4 B-tier names. Several ratings came from search snippets because agency pages return 403 (detail in the verification record). The panel is my selection.
4. **An alternative worth naming, not attributing (my channel, S5):** AI-*infrastructure* equities were **uniformly down on 10/7**: CRWV −3.6%, APLD −6.0%, WULF −3.8%, CIFR −6.1%, IREN −6.3%, NBIS −5.1% (z −0.5 to −0.8, 6 of 6 negative). They were down again on 10/8 and **flat-to-up on 9/29**. AI-related bonds are reportedly ~40% of 2026 net new HY issuance (Guggenheim, Aug 2026, secondary). So the "capex face" (AI-infra HY) is directionally consistent with 10/7 and 10/8 and not with 9/29. **Those issuers' ratings are UNVERIFIED here, and this is not an attribution.** It is a candidate for whoever owns the next read: LIQUID (spreads) or BROCK (private credit).

## 5. Hand-off (attribution, not a grade)
| Question | VULCAN's answer | Confidence |
|---|---|---|
| Named AI-disrupted B incumbents | LUMN · CABO · CNDT · MH (split); CHTR boundary; ADV unverified | VERIFIED-PARTIAL (sourced search 10/9) |
| Did they move on 9/29 / 10/7? | **Flat** (3 of 4 and 4 of 4 within \|z\| ≤ 0.3); CABO 9/29 idiosyncratic | VERIFIED as equity moves; credit UNREAD |
| Mechanism leg (Disc-A) | **FAILS on the letter ⇒ OBSERVED is in-letter only** | per the letter's own rule |
| AI-disruption event on the date? | 9/29 yes (DevDay; no incumbent reaction); 10/7 **none**; Concentrix 9/30 natural test: B **flat** | VERIFIED (dated sources) |
| Lagged-equity catch-up | **Not excluded** | UNKNOWN |

*Date note: 2026-09-29 is a TUESDAY (my own spawn prompt to the verification agent said Monday; caught by the agent and not carried here).*

**Verification record:** ratings and news came from an Opus subagent on 10/9 (60 tool calls; sources are URL-cited in its return, summarised in §1/§3). Equity pulls: `scratchpad/wq341_z.py`, `wq341_infra.py` (session-local; figures reproduced above).
