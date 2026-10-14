---
signal_id: SIG-W-20261011-005
date: 2026-10-11
timestamp: 2026-10-11T20:32:06Z
time_dispatched: 2026-10-11T20:32:06Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Bloomberg 2026-10-10 (Will X-bookmark @business; body not read): Jefferies-run fund, Radiant World / Sapphire Minmetals", "CNBC, Reuters via US News, Notes from Poland, 2026-10-11: Poland security-services meeting", "Barchart 2026-10-10 chart (Will X-bookmark): TLT call volume, rolling one-month total", "Barchart chart, close Fri 2026-10-09 (Will X-bookmark): UWMC monthly", "Barclays desk note via @carlquintanilla 2026-10-11 (Will X-bookmark image)", "Will X-bookmarks BM-20261011-02 items 1, 20, 21, 24, 27"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["Jefferies", "Radiant-World", "Sapphire-Minmetals", "Poland", "Tusk", "Kosiniak-Kamysz", "TLT", "UWMC", "Barclays", "AI-capex"]
precedence: ROUTINE
action: ["BROCK", "HAWK"]
info: ["HANS", "BOND", "HENRY", "HOMER", "VULCAN", "TERRY", "PROME"]
confidence: 0.75
confidence_language: "Radiant from a Bloomberg headline and tweet (body not read); Poland at three outlets; the TLT, UWMC and Barclays items read from images Will bookmarked (charts and a note excerpt, not primaries)"
signal_type: context
safety_net: clear
event_window: closed
word_count: 324
dispatch_note: "Will X-bookmark residue. BROCK action (update to SIG-W-20260930-007); HAWK action (Poland, European security); HANS info (Europe lens); BOND/HENRY info (TLT options flow); HOMER info (UWMC); VULCAN info (Barclays); TERRY/PROME via ID-diff (Will holds a TLT Oct-16 put; no trade proposed)."
---

# Residue 10/11: a Jefferies-run fund now puts the allegedly fraudulent Radiant deals at ~$900M face. Poland treats a threat to PM Tusk and the defence minister as "deadly serious", with no attempt confirmed. TLT call volume is at a record. UWMC closed at a record low. A Barclays desk asks where AI's maintenance capex money comes from

**1. Radiant World (BROCK action; update to `SIG-W-20260930-007`).** Bloomberg 10/10: a Jefferies-run fund said in court proceedings that it has evidence of alleged fraud by Radiant World and Sapphire Minmetals in receivables-financing deals with a face value of **almost $900M**. `-0930-007` carried Jefferies-managed LAM Trade Finance's London suit for **>$500M**. The body was not read, so whether this is the same claim enlarged or a new one is UNKNOWN. These are allegations.

**2. Poland (HAWK action; HANS info).** Security services met Sunday at the Internal Security Agency's counter-terrorism centre after information about a possible attack on PM Donald Tusk and Defence Minister Władysław Kosiniak-Kamysz. A special-services spokesman called it *"deadly serious"* with *"a high probability"* of being carried out. The nature and source are undisclosed, and **no attempt is confirmed**. The bookmark's "possible assassination attempts" overstates it: this is a threat.

**3. TLT calls (BOND, HENRY info).** Barchart chart (10/10): TLT call-option volume on a rolling one-month basis is about **15M contracts**, the highest in the series shown (from 2006). That is flow, not a yield forecast. Will holds a TLT Oct-16 $82 put (WQ-302/357, TERRY's card).

**4. UWMC (HOMER info).** UWM Holdings closed **$1.08** on Fri 10/9, its lowest close, with a 9th straight red month on Barchart's chart. Its credit-overlay change is in `SIG-W-20261008-026`.

**5. Barclays desk (VULCAN info).** Note excerpt (date not shown): combined disclosed AI-lab revenue is about **$150bn** and total AI revenue about **$250bn**, against an ecosystem that "needs well in excess of $1trn" to run even maintenance capex. It is a view, not data, and the same question as `SIG-W-20261010-009`.
