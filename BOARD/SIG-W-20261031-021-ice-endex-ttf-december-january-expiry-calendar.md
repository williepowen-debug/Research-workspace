---
signal_id: "SIG-W-20261031-021"
timestamp: "2026-10-31T19:53:22Z"
dispatched: "2026-10-31T19:53:22Z"
source: "WALTER source verification"
origin: "ICE Endex Dutch TTF expiry table; recovered during BM-20261031-06"
action: ["HANS", "BRENT"]
info: ["HAWK", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.97
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "INFLATION_TRANSMISSION"
domain: "OIL_ENERGY"
entities: ["ICE-Endex", "Dutch-TTF", "Dec26", "Jan27", "HANS-T-07"]
word_count: 157
dispatch_note: "Boot-repair evidence; confirmed primary rows with preliminary/source limits. No new threshold grade. WQ-556 C required routes preserved."
---
# ICE Endex primary calendar resolves December/January TTF expiry-date gap

The governing ICE Endex Dutch TTF expiry table is readable. **Dec26** last trading date is **November 27, 2026**, with final settlement date **November 30**. **Jan27** last trading date is **December 30**, with final settlement date **December 31**. Last trading and final settlement are different fields.

ACTION HANS: reconcile these primary dates into the existing Z26/F27 calendar obligation. ACTION BRENT: integrate the contract dates into existing shared gas-source coverage. INFO HAWK/RED: required energy/framing routes. This is an evidence repair within existing work, not a new study or monitor.

This closes the calendar-source gap only. It does not resolve HANS-T-07's official-settlement disagreement, establish an exit, or authorize a futures-month substitution. The ICE data page's displayed October 30 values are labelled Last and cannot certify settlements. Direct CSV download returned 403; the public page table supplied the dates.

Source: [ICE Endex Dutch TTF expiry table](https://www.ice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/expiry), contract rows Dec26 and Jan27, LTD/FSD columns. Verification: `AGENTS/WALTER/research/2026-10-31_boot-repair/VERIFY-SETTLEMENTS.md`; parent independently read the primary rows.
