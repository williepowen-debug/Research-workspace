---
signal_id: SIG-W-20261002-006
date: 2026-10-02
timestamp: 2026-10-02T14:38:16Z
time_dispatched: 2026-10-02T14:38:16Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Connect CRE 'Return to Lender: Week of Oct. 1, 2026' (published 2026-10-01), citing SF Business Times, Washington Business Journal, Denver Business Journal, St. Louis Business Journal, Baltimore Business Journal, Morningstar Credit; primaries NOT opened"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Bank-of-America-Plaza-StLouis", "GSMS-2015-GC30", "225-Bush-St", "Flynn-Properties", "450-Fifth-St-NW", "Criterion-Real-Estate-Capital", "Thorofare-Capital", "Morningstar-Credit"]
case: ["Bank of America Plaza, St. Louis MO [CASE-CREED-016]", "225 Bush St, San Francisco CA", "450 Fifth St NW, Washington DC", "580 Market St, San Francisco CA", "Symes Building, 820 16th St, Denver CO", "Hotel Indigo, 501 Olive St, St. Louis MO", "906/921/923/935 St. Paul St, Baltimore MD"]
confidence: 0.75
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "Connect CRE roundup (10/01): 7 named CRE distress cases not on the BOARD or in CREED's ledger except BofA Plaza St. Louis (CASE-CREED-016, mostly UNKNOWN): GSMS 2015-GC30 $42.8M loan liquidated with $39.1M loss (~91%) in Aug; 225 Bush SF $350M note sold for $221M then deed-in-lieu; 450 Fifth St NW DC foreclosure auction set 10/28 ($166.6M owed). Primaries not opened."
precedence: PRIORITY
action: ["CREED"]
info: ["REGINALD"]
dispatch_note: "Named-case feed (ROUTING_CARVEOUTS 'Named-case feed - CREED', FORMAT_SPEC v0.23 case:). National CRE -> CREED action; REGINALD info for bank collateral. Baltimore rowhouses are small mixed MF/office; HOMER not added (no MF loan figures)."
---

# Seven named CRE distress cases: Bank of America Plaza (St. Louis) liquidated at ~91% loss; 225 Bush note sold at ~63¢; 450 Fifth St NW auction 10/28

**Short version:** Connect CRE's weekly "Return to Lender" roundup (published 10/01) lists **seven named distress cases**. Neither the BOARD nor CREED's case ledger carried them, except Bank of America Plaza (St. Louis), which the ledger holds as **CASE-CREED-016** with most fields UNKNOWN. **This roundup fills that row.**

| Property | City | Type | Event (date) | Figures | Original source (per Connect CRE) |
|---|---|---|---|---|---|
| **Bank of America Plaza** [CASE-CREED-016] | St. Louis MO | Office, 760k sf CBD | **Liquidated, CMBS GSMS 2015-GC30** (Aug 2026) | loan **$42.8M**, loss **$39.1M** ⇒ **~91% loss severity** (WALTER's arithmetic) | Morningstar Credit |
| **225 Bush St** | San Francisco CA | Office | **Note sale + deed-in-lieu** (Aug 2026) | **$350M note bought for $221.0M** (Flynn Properties) ⇒ ~63 cents on the dollar | SF Business Times / Morningstar |
| **450 Fifth St NW** (Judiciary Plaza LLC) | Washington DC | Office, 539,478 sf, slated for residential conversion | **Foreclosure notice filed 9/29; auction scheduled 10/28** | note $177.5M, $166.6M owed; lender Criterion Real Estate Capital | Washington Business Journal |
| 580 Market St | San Francisco CA | Office, 35k sf | Lender took ownership (recent, date unspecified) | — | SF Business Times |
| Symes Building, 820 16th St | Denver CO | Office, 98,577 sf | Lender (Thorofare Capital) took it Feb 2026; sale **$2.7M**, closing ~Nov 2026 | — | Denver Business Journal |
| Hotel Indigo, 501 Olive St | St. Louis MO | Hotel, 88 keys | Receivership sale **$2.3M** (Jul 2026; approved recently) | PACE loan | St. Louis Business Journal |
| 906 / 921 / 923 / 935 St. Paul St (Mt. Vernon) | Baltimore MD | Multifamily/office rowhouses | Foreclosure auctions, week of 9/24 | $1.6M each (two sales) | Baltimore Business Journal |

## Caveats
- **All figures come via Connect CRE's roundup; none of the business-journal or Morningstar primaries was opened.** The ~91% and ~63-cent figures are WALTER's division on those relayed numbers.
- Most events are **August**: late for news, and the reason they belong in the ledger rather than on a dated watch. The one forward-dated item is the **450 Fifth St NW auction on 10/28**.
- Selection bias (Will's 9/29 ruling): a weekly roundup surfaces what business journals cover, which is mostly office in large metros.

## Requested action
**CREED:** enter or update these cases in `cases/` (CASE-CREED-016's UNKNOWN fields first), and flag whether a ~91% CMBS loss severity on a CBD office is a comp you want carried on any band (that call is yours). REGINALD: information (loss-severity and bank-collateral read).
