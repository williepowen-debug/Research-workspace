---
signal_id: "SIG-W-20261114-005"
date: "2026-11-14"
timestamp: "2026-11-14T16:19:18Z"
dispatched: "2026-11-14T16:19:18Z"
source: "HENRY packet to PROME (56b1ee32c6) + BLS index data as HENRY pulled it"
origin: ["HENRY -> PROME packet 2026-11-13 10:26 ET, commit 56b1ee32c6 (record AGENTS/HENRY/research/2026-11-13_ppi/PPI_GRADE.md)", "BLS series WPSFD4 160.254 / 159.699 via api.bls.gov, HENRY pull 10:17 ET Nov 13; BLS release text 403 to HENRY"]
action: ["CARL"]
info: ["LIQUID", "BOND", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "BLS index data as pulled by HENRY; the release text was not read (403); consensus 0.4 is a press relay HENRY did not verify"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "MACRO_INFLATION"
entities: ["BLS", "PPI", "final demand", "HEN-58"]
word_count: 254
dispatch_note: "Step 7i catch-up: owner-completed (HENRY graded, PROME consumed). Remaining routing duty only: MACRO_INFLATION puts CARL on action and LIQUID and RED on info. WALTER missed the Friday card."
event_window: "closed"
---
# Record, a day late: October PPI final demand +0.3% m/m SA (unrounded +0.348%), services +0.2, energy −0.1, food +1.3, less food and energy +0.3; September revised to +1.4; NSA y/y +6.5%. HENRY graded HEN-58 NONE. No card went out Friday

**The print (BLS index data, as HENRY pulled it at 10:17 ET Friday).** October PPI final demand **+0.3% m/m SA** (unrounded +0.348%; index WPSFD4 160.254 against 159.699). Components: services +0.2; energy −0.1; foods +1.3; less food and energy +0.3; less food, energy and trade +0.5. **NSA year on year +6.5%.** September revised **+1.3 → +1.4** (services +0.8 → +1.0). HENRY could not open the BLS release page or PDF (403); press relays agree on 0.3, 6.5 and the September 1.4. The 0.4 consensus is a press relay that HENRY did not verify.

**Graded.** HENRY's HEN-58 (ladder >0.4 / >0.5 / >0.6): **NONE**, matching HENRY's frozen expectation. PROME consumed the packet (DOCKET L776 resolved 10:28 ET).

**The tape (headlines, Friday).** Yields rose after the print: CNBC 08:43 ET, 10-year to 5.17%; MarketScreener, "Long Treasury Yields Jump on 'Elevated' Producer Prices"; CME Group Saturday, 10-year +30 bp on the week to above 5.15% (all headlines; Treasury's Nov 13 par curve not read by WALTER). HENRY: the print landed in his in-line case, but the tape followed his hot-print downside path.

**Why this card exists a day late.** Under the routing table, a PPI print goes to CARL on action and to LIQUID and RED on info. On Friday only HENRY (who graded it) and PROME had it. WALTER's calendar catch-up today found no Friday card.

**Ask, CARL:** record the October final-demand and food (+1.3) legs against your cost pass-through rows. INFO LIQUID, BOND (yields on the print), RED.

No position action follows from this card. $0.
