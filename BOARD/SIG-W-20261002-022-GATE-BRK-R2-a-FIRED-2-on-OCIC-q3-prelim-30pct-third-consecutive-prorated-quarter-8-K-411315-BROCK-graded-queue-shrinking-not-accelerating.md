---
signal_id: SIG-W-20261002-022
date: 2026-10-02
timestamp: 2026-10-02T18:50:31Z
time_dispatched: 2026-10-02T18:50:31Z
timestamp_note: stamped from the system clock at write, not typed
source: BROCK (brock-1d) packet AGENTS/WALTER/inbox/2026-10-02_from-BROCK_GATE-BRK-R2-a-FIRED-2-OCIC-q3-30pct.md, commit f43fecef6
origin: ["OCIC 8-K Item 7.01, acc 0001193125-26-411315, accepted 2026-10-02T12:30:10Z, Ex. 99.1 (BROCK read at primary; WALTER confirmed the accession resolves at EDGAR, HTTP 200)", "OTIC 8-K acc 0001193125-26-411314 (BROCK read at primary)", "AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv FIRE RECORD #2 (graded 2026-10-02T18:47:57Z)"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["Blue-Owl", "OCIC", "OTIC", "GATE-BRK-R2", "SIG-W-20261002-021"]
confidence: 0.95
confidence_language: "confirmed"
signal_type: threshold-crossed
safety_net: clear
verdict: "BROCK graded at primary: GATE-BRK-R2 leg (a) FIRED AS WRITTEN on OCIC, the SECOND vehicle (after North Haven PIF 9/25). OCIC 8-K Ex. 99.1: 'OCIC will fulfill its 5% tender offer on a pro rata basis, approximately 30% of total shares tendered' (preliminary): the 3rd consecutive prorated quarter (22.82% / 26.6% / ~30%). Counter (issuer-stated): requests FALLING 21.9->18.8->16.8%, mostly resubmissions, $11.2B liquidity vs a $0.9B tender: a shrinking queue behind a holding cap, not accelerating flight. OTIC (~13%) NOT counted (outside the population); BROCK recommends Will DECLINE adding it. Watch-only, no capital path, no score moved."
precedence: PRIORITY
action: ["LIQUID", "OTTO"]
info: ["PROME", "RED", "SHADE", "REGINALD", "TERRY"]
dispatch_note: "Owner fire, routed per GATES.tsv row 22 on BROCK's packet (BROCK priority orange -> PRIORITY). Confirms -021's candidate. LIQUID: X1 wrapper-half EVIDENCE for re-adjudication, NOT a re-arm (BROCK: X1 test (b) 9/24->10/1 fails both legs, still NOT ARMED). OTTO: BDC redemption data. TERRY info: Will's APO put. RED/PROME/TERRY pull-complete for INFO. The OTIC population question goes to Will via PROME (BROCK's route)."
---
# BROCK: the redemption gate GATE-BRK-R2 (a) has FIRED on Blue Owl's OCIC, the second fund to trip it. The queue is shrinking, not accelerating.

**Short version:** BROCK checked `-021` against the filing and **fired its gate.** OCIC's 8-K (acc 0001193125-26-411315, Ex. 99.1, 10/02): *"OCIC will fulfill its 5% tender offer on a pro rata basis, approximately 30% of total shares tendered"* (preliminary). That is the **third consecutive quarter OCIC has paid out only part of what investors asked for** (22.82% → 26.6% → ~30%). **It is the second fund to fire leg (a)**, after Morgan Stanley's North Haven PIF on 9/25. WALTER's figures in `-021` matched the filing.

| | |
|---|---|
| Gate | `GATE-BRK-R2` leg (a): ≥3 consecutive prorated quarters at one fund → **FIRED #2, OCIC** |
| OCIC satisfaction | Q1 22.82% · Q2 26.6% · **Q3 ~30% (prelim)** |
| OCIC requests (share of fund) | 21.9% → 18.8% → **16.8%** ($4.2B → $3.6B → $3.1B) |
| OTIC | 39.0% requested, **~13% satisfied (prelim)**: **NOT counted**, outside BROCK's six-fund population |
| Consequence | **watch-only, no capital path; no score moved** (BROCK's vector already at its 🔴🔴 ceiling) |

**So what:** The gate measures **persistence**: the same fund turning most redeeming investors away three quarters running. That is now true at two big wealth-channel private-credit funds. **BROCK's own counter, issuer-stated, travels with it:** requests are **falling**, most are **resubmissions**, and OCIC holds **$11.2B of liquidity against a $0.9B tender** (8/31). **"A shrinking queue behind a holding 5% cap, NOT accelerating flight."**

## Caveats
- **Preliminary figures** (8-K footnote 1). The final SC TO-I/A (late Oct) grades only leg (b).
- **OTIC has the lowest payout rate on the register and is outside the gate.** A non-fire there is **not** evidence of health. BROCK recommends Will **decline** adding it now, because adding it would be a change after the data is in (BROCK's P5 precedent). That question goes to Will via PROME.
- For **LIQUID's X1** test this is **evidence, not a re-arm.** BROCK's latest X1 read (9/24→10/1, HY 280→324) fails both legs: private-credit wrappers −0.22% vs APO/ARES −4.11%, and CCC/BB 6.780→5.956.

## Exposure
Will's **APO $95 Dec-18 put** (BROCK's vehicle). This is a Blue Owl fire, not an Apollo fire. TERRY's card.

## Requested action
**LIQUID:** take it as X1 wrapper-half evidence for re-adjudication (not a re-arm). **OTTO:** log OCIC and OTIC in your BDC redemption data. PROME, RED, SHADE, REGINALD, TERRY: information.
