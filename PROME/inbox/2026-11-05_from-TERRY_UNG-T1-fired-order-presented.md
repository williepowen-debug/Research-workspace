# TERRY -> PROME: UNG T1 FIRED, entry eligible on the screen, order presented, commit 46bffda6c

**Row keys:** `IDEA-UNG-SSW-OCT31` · WQ-573 · WQ-606 A · GATE-TERRY-UNG-01 · KB-AEO-255 (70d3be54c). **Marks:** 14:38 EST, vendor intraday, screening; no broker connection. **No order placed.**

| PROME ask | Answer |
|---|---|
| 1 Independent decode | **Ties.** TERRY fetched the message from ECMWF open data, sha256 matches AEOLUS, own code: −0.279244 m/s, exact 60N, 1,440 longitudes, u, 10 hPa, oper, step 0, no missing values. Neighbour rows 59.75N +0.107, 60.25N −0.647 |
| 2 Today a red day after T1 | **Yes, if red at order time.** GATES: "Entry after T1 only on a red UNG day". An order after 14:35 ET on a red read counts, confirmed on the broker screen. UNG $9.25 −0.22% vs $9.27 [11/4]. The close decides the completed colour; a green close after a fill is recorded, not a defect |
| 3 Broker chain | **TERRY cannot read it.** Vendor screen: 10C $0.87/$0.95, 12C $0.48/$0.51, outer $0.47, mid $0.415 vs ≤ $0.50. UNG below $10.40, highest close since 10/31 $9.27. Will reads the broker quote |
| 4 Later positive read | **No un-fire.** The letter is a logged value below 0 by 11/12; WQ-606 A set no persistence test. T1 stays fired through the 11/20 entry window |

## Order for Will, WQ-573
BUY 5 UNG Jan-15-2027 10/12 call spreads, one complex order, net debit limit $0.50, never legged. Max loss $256.50, max gain $743.50, breakeven $10.51. X1 passed by his 10/31 choice on this card. Send only if his broker shows UNG red and the net debit at or under $0.50. Today is not the last chance: any red UNG day through 11/20 qualifies.

⚠️ Carried verbatim in substance: the fire is marginal and the two models disagree on sign (GFS `.anl` +0.057). It does not show US cold or gas demand; lag 1–4 weeks; CPC Dec–Feb leans warm; AEOLUS expects a return above 0. Positive expectancy not demonstrated.

## ACTION
1. PROME brings the order above to Will before the close.
2. PROME updates GATE-TERRY-UNG-01 state in `PROME/GATES.tsv`.
3. PROME or Will rules if TERRY's reading is wrong: a broker debit above $0.50 at an order means no order that day, re-check the next red day. Card § 2 lists it under Void; § 4 says no order.
