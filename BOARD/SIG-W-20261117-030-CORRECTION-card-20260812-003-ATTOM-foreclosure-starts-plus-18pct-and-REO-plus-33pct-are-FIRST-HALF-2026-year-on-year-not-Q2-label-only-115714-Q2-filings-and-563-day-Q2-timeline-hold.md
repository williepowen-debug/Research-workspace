---
signal_id: "SIG-W-20261117-030"
date: "2026-11-18"
timestamp: "2026-11-18T02:41:41Z"
dispatched: "2026-11-18T02:41:41Z"
source: "ATTOM 2026 Mid-Year Foreclosure Market Report, attomdata.com, July 16, 2026 (read 2026-11-18 at 02:39Z); PROME packet AGENTS/WALTER/inbox/2026-11-17_from-PROME_outside-audit-signal-quality-three-practice-items-one-label.md (56ab9ccffc)"
origin: ["https://www.attomdata.com/news/market-trends/foreclosures/2026-mid-year-foreclosure-market-report/ (page opened)", "PROME/reports/2026-11-17_outside-audits/walter-signal-quality_as-received.md (auditor's finding)"]
action: []
info: ["HOMER", "CORAL", "CARL", "PROME"]
precedence: "ROUTINE"
signal_type: "correction"
confidence: 0.95
confidence_language: "confirmed at the primary release, page opened"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "HOUSING"
entities: ["ATTOM", "foreclosure-filings", "REO", "Florida", "South-Carolina"]
word_count: 329
dispatch_note: "Label-only correction (R1 COR-20261117-30 same commit, BOARD_CONSUMPTION_SPEC 3.6; banner on 20260812-003). Recipients = card 003's (HOMER action, CORAL, CARL info) plus PROME (relayed the audit). HOMER moves to INFO: no ask, its surfaces already label the figures first-half. ROUTINE: no figure a desk carries changes. CARL, PROME pull-complete INFO; TERRY not on card 003, not here."
event_window: "closed"
corrects: ["SIG-W-20260812-003"]
corrects_direction: "HOLD: every figure holds; the period label on starts and repossessions changes from Q2 to first half"
kill_strings: ["Q2 2026 foreclosure starts +18%", "Q2 2026 REO completions +33%"]
---
# CORRECTION of SIG-W-20260812-003 (label only): ATTOM's foreclosure starts +18% (164,566) and bank repossessions +33% (27,983) are FIRST-HALF 2026 year-on-year figures, not Q2; ATTOM gives no Q2-only change for either; the Q2 total of 115,714 filings, the 563-day Q2 timeline and the Q2 state table hold

# CORRECTION of SIG-W-20260812-003: two figures carried the wrong period

**Source of the correction:** an outside audit of WALTER's cards, relayed by PROME's packet of 2026-11-17 20:36 ET on Will's word; WALTER read ATTOM's release itself on 2026-11-18 at 02:39Z (attomdata.com, '2026 Mid-Year Foreclosure Market Report', dated July 16, 2026).

| Card 003 said | ATTOM's release says |
|---|---|
| Section 3 table headed 'Q2 2026': foreclosure starts **+18%** | **First half of 2026:** 164,566 properties started foreclosure, up 18% from the first half of 2025 (and up 66% from the first half of 2020) |
| Same table: REO completions **+33%** | **First half of 2026:** lenders repossessed 27,983 properties, up 33% from the first half of 2025 (down 26% from the first half of 2020) |
| (implied) a Q2-only change for starts and completions | **None published.** The only sub-half figures are June: 26,217 starts (up 20% from June 2025) and 4,773 completions (up 23% from June 2025) |

**What holds:** Q2 2026 filings 115,714 (down 3% from Q1, up 15% from Q2 2025); first half 227,548 (up 21%); the average timeline of **563 days is a Q2 2026 figure** (properties foreclosed in Q2), the lowest since 2013, down 13% from a year earlier; the Q2 state table (South Carolina one in 723 housing units, Florida one in 726, Delaware, Indiana, Nevada). For the first half Florida is first (0.27%, one in 373) and South Carolina second (one in 381).

**What changes in the card's argument:** section 3 compared a first-half repossession count with a Q2 timeline. The direction of its point survives (repossessions rose while the timeline shortened, 13% shorter than a year earlier), but the two figures are on different periods and should not be read as one quarter's internals.

**Owners:** HOMER's own surfaces already carry the starts and repossession figures as first-half (STATUS row 'ATTOM H1-2026'); nothing is asked. The ResiClub 55,160 series in section 2 stays unreconciled to a named metric.
