# Oil-market evidence — September 16

Retrieval: 18:28–18:31 UTC. Yahoo **MIRROR**, indicative delayed prices, not exchange-authenticated settlements or broker execution quotes. `quotes.json` preserves each quote epoch, named symbol and vendor daily bars; `aligned.json` preserves minute bars. Source: Yahoo Finance chart/history endpoints through yfinance. No continuous ticker is used to construct a spread. `expireDate` was absent from retrieved metadata, so no continuous-contract identity certification is claimed. Dated October/November/December legs return distinct prices; that rejects simple all-symbol aliasing but does not replace exchange contract metadata.

## Same-contract before/after

Figures below derive from the **same September 16 retrieval**, not different historical captures. September 14/15 are vendor daily closing bars, not authenticated exchange settlements. September 16 is the **common 14:19 EDT completed minute** present in every required leg. Do not interpret the close-to-intraday comparison as a close-basis threshold grade. Archived September 14 captures can differ from this vendor's restated daily bars.

| [CONF retrieved; calculated] USD/bbl | Sep 14 vendor daily | Sep 15 vendor daily | Sep 16 14:19 EDT minute |
|---|---:|---:|---:|
| Brent November, BZX26.NYM | 105.68 | 108.75 | 105.41 |
| Brent January, BZF27.NYM | 96.85 | 98.75 | 96.37 |
| November−January | +8.83 | +10.00 | **+9.04** |
| WTI November, CLX26.NYM | 97.14 | 100.75 | 97.22 |
| November WTI−Brent | −8.54 | −8.00 | −8.19 |
| November ULSD−WTI, 42×HOX26−CLX26 | 102.58 | 109.67 | **111.97** |
| November gasoline−WTI, 42×RBX26−CLX26 | 34.63 | 35.60 | **38.23** |

November product inputs at 14:19: HOX26 $4.9808/gal; RBX26 $3.2251/gal. The same-minute WTI 3:2:1 gross crack is $62.81/bbl; Brent basis is $54.62/bbl. These are modeled gross futures margins, not VLO's realized margins. The named November spread avoids the known front-month mismatch. A matched future month can still differ from the threshold's calibration month; HENRY's F1 remains HENRY's close-basis grade. WALTER Boundary #8's settlement persistence and basis issues remain unresolved here; no close count inferred from this intraday level.

The November–January spread remains backwardated, but is below the captured September 10 daily +$9.27 baseline and yesterday's +$10.00. September 15 therefore did extend prompt-price/curve strength; carrying September 14's “repriced once and stopped” into today would be wrong. Today's retracement does not prove supply repair, nor does backwardation quantify missing barrels. Research falsifier +$3.50 has not been reached on this indicative reading; no settle-based capital grade.

## Physical and equity/freight context

[CONF MIRROR] Boot's FRED observations: Dated Brent $130.80/bbl and WTI spot $107.02/bbl, **September 15**, not September 16 live spot. These are different locations/bases from futures; no same-time physical-paper premium calculated. Boot receipt `boot.txt`; FRED series DCOILBRENTEU/DCOILWTICO.

| Yahoo quote | Value | Versus Sep 15 vendor close | Quote epoch converted to UTC |
|---|---:|---:|---|
| USO | $156.69 | −3.194% | 18:28:18 |
| VLO | $406.77 | +2.451% | 18:28:45 |
| MPC | $418.56 | +1.879% | 18:28:45 |
| PSX | $266.695 | +0.666% | 18:28:00 |
| BWET | $775.18 | +6.777% | 18:26:58 |
| BDRY | $15.259 | −0.463% | 18:05:48 |
| Dollar index DX-Y.NYB | 99.996 | +0.347% | 18:18:51 |

Freight ETF rebound contrasts with declining oil, but **BWET is not a route-specific freight fixture or war-risk premium**. BDRY's timestamp is earlier; no synchronized relative-spread or causal estimate uses that pair. Current realized freight and current negotiated insurance premium remain UNKNOWN. FALCON/OSPREY stale insurance rows are not refreshed by ETF prices.

Macro confounding is material. [Fed PRIMARY statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm), September 16 14:00 EDT, raises the target by 25 bp to 3.75–4.00%; directly retrieved at 18:33 UTC. Stronger dollar and lower crude are consistent with a macro channel, but no event-study identification or counterfactual was performed. Pipeline restart expectations, alternative cargo availability and US balance evidence also coexist. **No percentage of today's oil move is assigned to the war or Fed.** The earlier API-build headline is not the EIA result; EIA's measured commercial crude draw is in `EIA.md`.

## Position implications, not orders

PROME's September 16 13:57 screenshot transcription establishes USO37 shares and Sep16 165C ×1 at that capture. A subsequent broker recheck is unavailable. USO37 remains linear crude exposure, not a direct refining-margin position. WQ-200's share-exit scaffold remains declined; no automatic harvest/stop revived.

`uso-option.json` verifies the exact Sep16 165C public contract and indicative $0.01/$0.02 bid/ask at 18:28:55 UTC, last trade 18:10:24; quote timestamp UNKNOWN. At the simultaneous underlying $156.69, the strike is $8.31 above spot. No sale, expiry outcome, remaining holding, exercise instruction or replacement inferred. Current broker position/order status is required before a management recommendation.

Refiner-margin support strengthens, but WQ-213 still requires Will's reaffirmation after condition 2 and TERRY's fresh entry check. This snapshot shows the opposite signs from the required red-refiner/green-USO tape. No approval withdrawn, relaxed, renewed or executed.
