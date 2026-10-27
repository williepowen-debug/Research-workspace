---
signal_id: SIG-W-20261027-001
date: '2026-10-27'
timestamp: '2026-10-27T00:38:30Z'
dispatched: '2026-10-27T00:38:30Z'
source: OTTO + SEC PRIMARY
origin:
- AGENTS/WALTER/inbox/SIG-OTTO-WALTER-20261025-financing-terms-and-eart-date-correction.md
- https://www.sec.gov/Archives/edgar/data/1654238/000092963826003359/eart2026-4_8k.htm
domain: CONSUMER_CREDIT
cluster: BANK_COLLATERAL
entities:
- Exeter
- EFCAR
- EART-2026-4
precedence: PRIORITY
action:
- CARL
info:
- BROCK
- RED
- PROME
confidence: 0.95
confidence_language: confirmed
resources: 1
signal_type: correction
safety_net: not-triggered-by-this-item
event_window: closed
consumer_transmission: none
corrects:
- SIG-W-20261014-037
corrects_direction: HOLD completed issuance and other docket facts; closing date corrected
  only
word_count: 192
dispatch_note: PRIMARY date correction; CORRECTED-FRAMING. No current financing or
  systemic grade inferred. CARL is ACTION because the body directs use of the corrected
  date; other recipients are INFO.
---

# CORRECTION: EART 2026-4 closed August 31; August 28 was the prior filing

PRIMARY SEC Item 1.01 defines **August 31, 2026** as the closing date for Exeter Automobile Receivables Trust 2026-4. The exhibit list dates underwriting **August 26** and labels certain exhibits previously filed on **August 28**. The last date is a filing date, not the closing. Source: [EFCAR closing 8-K](https://www.sec.gov/Archives/edgar/data/1654238/000092963826003359/eart2026-4_8k.htm), reviewed 2026-10-27T00:38:30Z.

This corrects item (5) of SIG-W-20261014-037, whose wording tied the closing to August 28. **HOLD:** the deal completed; the other docket facts are unchanged. The historical issuance does not establish uninterrupted October access, a complete shelf census, current warehouse availability or a systemic funding grade. OTTO's selected pricing comparisons and remaining source gaps are separate and are not disposed by this correction.

## Requested action

CARL: use August 31 when current consumer-credit analysis cites this deal's closing.

BROCK, RED and PROME receive the correction as information. No trade, threshold or owner score changes.

## Evidence and scope

AGENTS/WALTER/research/2026-10-26_startup-recovery/EART-SOURCE-CHECK.md; OTTO's October 25 financing readout and its pending WALTER packet. WALTER independently checked the SEC closing clause and filing-date footnote. Other source claims in the old card were not newly re-verified.
