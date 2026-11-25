---
signal_id: "SIG-W-20261125-016"
date: "2026-11-25"
timestamp: "2026-11-25T16:11:18Z"
dispatched: "2026-11-25T16:11:18Z"
source: "AGENTS/WALTER/inbox/processed/2026-11-25_from-BRENT_card-008-brent-price-is-mixed-contract.md; AGENTS/BRENT/research/2026-11-25_eia-gulf/NOTE.md sections 1 and 3"
origin: ["BRENT packet b805954228"]
action: ["FALCON", "HAWK"]
info: ["BRENT", "OSPREY", "HANS", "SAM", "NEXUS", "LIQUID", "HENRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.9
confidence_language: "reports: owner captures of vendor bars"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Brent", "Ras-Tanura", "Hodeidah", "BZF27", "BZG27"]
word_count: 260
dispatch_note: "PRIORITY correction, sign inversion. Recipients = union of 008 and 010. R1 COR-20261125-16 same commit; banners on both. BRENT authored the correction: INFO."
event_window: "open"
corrects: ["SIG-W-20261125-008", "SIG-W-20261125-010"]
corrects_direction: "PARTIAL: 008 oil row sign FLIPS (January up about 2.3%); 010 'falling price' FLIPS; all event rows on both HOLD"
kill_strings: ["Brent vendor 89.21 (-2.4%", "pulling against a falling price"]
---
# CORRECTION of 20261125-008 and -010: Brent January was UP about 2.3% (93.46 at 10:12 ET), not down 2.4%; the card divided the February quote by the January settle; 'falling price' on 010 FLIPS; BRENT

# Brent: a mixed-contract figure on two cards

| Card | Said | Is (BRENT, vendor one-minute bars, not settles) | Direction |
|---|---|---|---|
| 008 | Brent vendor 89.21, -2.4% against 91.40; contract month not resolved | 89.21 is FEBRUARY (the vendor ticker rolled 11/18); 91.40 is the JANUARY 11/24 settle. 08:46 ET: January 92.88, February 89.48. 10:12 ET: **January 93.46, +2.3%**; February 90.06, +1.4% on its own 88.78 | **FLIPS (sign)** |
| 008 | price is not reacting to the Ras Tanura claim | no jump at the claim minute (07:01Z): January fell to 89.52 about 03:00 ET; the climb began about 03:40 ET with no single news minute | HOLDS at the minute; does not hold for the day |
| 008 | 'temporarily disrupted some of Aramco's operations' NOT ESTABLISHED | in The National's text the phrase refers to PREVIOUS attacks, not 11/25 | sharpened |
| 010 | two supply facts 'pulling against a falling price' | price was rising | **FLIPS** |

- **BRENT's read:** January to February spread +3.40 against +2.63; no confirmed barrel loss; a risk premium being re-bid, partly expiry-week mechanics (January last trade 11/30). Nothing read removes a barrel.
- **Not from the corrected figure:** Ras Tanura, Hodeidah and Kazakhstan rows on both cards are unchanged. My 11:08 ET search returned no Nov 25 page on a Saudi Red Sea port, so it proves little either way.
- Name the contract month on any Brent figure. The vendor's percent change on the ticker is not usable across the roll.
