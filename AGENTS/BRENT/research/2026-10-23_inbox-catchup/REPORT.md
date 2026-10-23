# BRENT — October 23 inbox catch-up and owed work (live session, Will-launched 15:14 ET)

Stamps come from `date`. $0 moved. No trade, threshold, gate or authority change.

## 1. COT #11 (as-of 10/20): JOINT NOT-SPENT, fifth consecutive

| Series | Value | WoW |
|---|---|---|
| MM gross shorts, WTI-PHYSICAL NYMEX | 127,226 [CONF raw CFTC f_disagg.txt, graded 15:51 ET] | −4,173 |
| MM gross longs | 163,413 | −8,560 |
| Open interest | 1,835,144 | −65,035 |
| OI share | 6.9328% | +0.018 pp |

Leg A: 127,226 is 8,900 above the deadband top (118,326), so NOT-SPENT. Leg B: 6.93% against a 4.909% bar, so NOT-SPENT. A separate curl pull at 15:51 ET matches to the digit. Shorts fell, but the OI share edged up because open interest fell faster. The ledger row is in `workbook/COT_VINTAGES.tsv`, and the packet went to PROME/inbox (G:GATE-BRENT-COT-35B).

## 2. Price tape and the contract roll

Vendor quotes at 15:19 ET, not settles: Brent January BZF27 $111.84 (+2.93%); WTI December CLZ26 $103.49 (+4.04%); HOZ26 $4.80; RBZ26 $3.13. The BZZ26 symbol errored in BRENT's fetch. WALTER's 18:39Z read was BZZ26 $116.71 (+3.13%). The vendor's continuous `BZ=F` moved to January on 10/23, so its daily change splices two contracts (LESSONS #23). **Fleet basis:** BZZ26 through its last trade on 10/30, then BZF27 from 11/2 (the boundary #8 rule). WALTER was answered by packet.

Boundary #1 (Brent ≥ $120 for three settles) is about 3% away on an intraday December read. It is a watch, not a fire. FALCON graded the strike-timing tape FAL-07 NOT FIRED (relayed by PROME; BRENT does not re-grade the theater). The White House's written line (10/22) of no attack before the midterms stands.

## 3. Pre-stages

- **BRT-30 (resolves Mon 10/26):** IUA index at 15:54 ET, newest circular JWLA-035, none ≥036. The procedure is written into `thesis/prediction_notes/BRT-30.md`. Not a grade.
- **OPEC+ 11/01 deliverability gate:** EIA STEO API (October STEO vintage, the newest; read 15:56 ET) gives OPEC crude spare capacity `COPS_OPEC` of **0.02 mb/d for October–December 2026** and 0.03 for January–March 2027. Capacity `COPC_OPEC` is 20.78 mb/d in October and 21.25 in December. This is a single agency, and the November STEO (~11/10) comes after the meeting. A second agency is still owed before grading.

## 4. Owed work delivered

- **L526:** routine boot-preamble DRAFT `setups/2026-10-23_L526_routine-boot-preamble-DRAFT.md` plus a new `scripts/routine-requirements.txt`. Not installed; that is Will's word.
- **CYPHER boundary:** confirmed as written.
- **DEWEY Tanker War base rates:** corrections banner added to the archived precedents file.
- **WQ-508:** DAEDALUS applied BRENT's lines in f4149bf51. Diff read; no contest.
- **R1 corrections:** five receipts (COR-20261021-11 NO-OP, -16 APPLIED, -22 APPLIED, COR-20261022-04 NO-OP, COR-20261023-31 NO-OP). Check rc 0.

## 5. Supply policy and product items (WALTER -009, -022, -025)

Source: a read-only helper's lookups 15:51–15:59 ET (tiers P = primary, S = secondary, R = relay; "snip" = search snippet only). BRENT checked the arithmetic.

| Item | Finding | Tier | Read for BRENT |
|---|---|---|---|
| **-009 Great Lakes gasoline** | Cause: a unit shutdown at **ExxonMobil Joliet** (~275 kb/d) from 10/20. Exxon: "working to resolve an operational issue", no timeline (CNN, snip). Only an automated GuruFocus piece names the catalytic reformer; Bloomberg says "a key unit". Chicago conventional blendstock $3.67/gal (+$0.33), +$0.55 over futures (likely the 10/21 assessment). GasBuddy Michigan $4.59 → $4.74, Ohio $4.05 → $4.34 (10/21 → 10/22). EIA Chicago regular $4.705 (week of 10/19, snip). Kloza's "+45–50 c on 10/22" print was not found at any outlet | S (Bloomberg via Insurance Journal, read) / S-weak | **A regional product outage, not crude.** RBOB is national: RBZ26 was +1.3% on 10/23 against a +3% crude day. BRT-31's demand leg uses national four-week supplied and is unaffected. Its price leg uses national retail, which a Midwest spike lifts slightly, making it easier to meet. No INCIDENTS row: "an operational issue" is not confirmed damage at the P-tier this ledger requires. Joliet's 9/14–9/18 outage was a separate, earlier event |
| **-022 SPR exchanges** | **10/23: up to 400,000 bbl** from West Hackberry to Phillips 66 Lake Charles. The stated cause is only "a crude oil supply disruption". **10/10: up to 4 M bbl** (ExxonMobil 2 M, BP America 2 M) after Gulf hurricane disruptions, returned with premium barrels in 2027. SPR 282.683 M bbl, week 10/16 (−0.300 M) | **P** energy.gov (both read); P EIA | Loans to named refineries, not policy releases. 0.4 M bbl is ~1.5 days of Lake Charles runs. The −0.3 M weekly SPR draw is consistent with the 10/10 exchange starting to deliver (inference). Ledgered here beside the 10/10 exchange and the 10/6 40 M bbl exchange solicitation (CATALYSTS row 10/6, awards still UNKNOWN). A reported 17 M bbl solicitation on 10/16 (roic.ai) is UNVERIFIED and not adopted |
| **-025 DPA § 303 (10/22)** | Same findings, waiver (§303(a)(1)–(a)(6)) and scope as the **4/20** determination. No dollar figures or projects. **The one change: it is addressed to the Secretary of War**, where April's went to Energy | P whitehouse.gov (both read via a summarizing fetch; not a verbatim diff) | **No new supply.** The authority moves to defense-side funding; no barrels or capacity can be measured from it. Do not cite "no other change" until both texts are diffed verbatim |
| **-025 Germany EBV** | A **SALE** tender for diesel, heating oil and crude (Newsquawk headline, "according to a document"). Relay: it is Germany's first release under the IEA/G7 ~100 M bbl action. Germany pledged up to 15 M bbl, and the minimum stock floor was cut from 90 to 82 days. Volumes and timing NOT FOUND. ebv-oil.org tender page HTTP 404 | S headline / R relay | **Direction reversed:** July EBV tenders were refill BUYS. A European diesel release eases the crack (the L783 direction is toward $90.16). Relay figure, not adopted: ICE gasoil crack ~$95 in late September → ~$76 on 10/23. If confirmed, that is European diesel margin relief well ahead of US December HO. The physical product-scarcity fact (Gulf clean products ~50% below pre-war, Kpler 10/1) is unchanged; policy stock release is drawing inventory, not restoring refineries |
| **OSPREY ask (OSP-06)** | Bloomberg four weeks to 10/11 **~3.7 M b/d** (−110 kb/d), snip only (403). **Newer: four weeks to 10/18 3.59 M b/d** (−110 kb/d; weekly 3.13, lowest since March; Primorsk paused ~3 days), Bloomberg 10/20 snip plus a ua.news relay | S snip / R | 3.7 is confirmed only to the snippet level. The 10/18 print is **below** OSPREY's ≥3.9 flip line, so it does not flip OSP-06 on this evidence. OSPREY grades its own row. Packet to OSPREY |

## 6. Settlements Friday 10/23 [secondary, not exchange-read]

| Contract | Settle | Change | Source |
|---|---|---|---|
| Brent December **BZZ26** | **$116.72** | +3.55 (+3.14%) | Newsquawk "SETTLES" crude wrap 19:09Z (headline read). Arithmetic check: 116.72 − 3.55 = 113.17, matching CNBC's 10/22 close $113.17 (snip). CNBC: highest Brent settle since 4/29; +6.2% on the week |
| WTI December **CLZ26** | **$103.27** | +3.80 | same |
| ULSD December **HOZ26** | NOT FOUND | — | CME API HTTP 403. The December crack for 10/23 cannot be computed from settles here; TERRY grades leg A on its own basis |

Brent December rose from $108.82 (10/21) to $113.17 (10/22) to $116.72 (10/23) on three settles. **Boundary #1 (≥ $120 × 3 settles): 0 of 3; $3.28 (2.8%) below the line.** BZZ26 has five sessions left (last trade 10/30), so a three-settle count would have to land by 10/30 or span the BZF27 switch, which is about $5 lower on today's quotes. How a count that spans the switch is treated follows the boundary's own letter (WALTER/RED routing overlay), not re-read here.
