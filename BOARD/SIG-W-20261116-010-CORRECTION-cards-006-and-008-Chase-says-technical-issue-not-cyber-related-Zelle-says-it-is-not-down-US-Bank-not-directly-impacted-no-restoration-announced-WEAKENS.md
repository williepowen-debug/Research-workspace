---
signal_id: "SIG-W-20261116-010"
date: "2026-11-16"
timestamp: "2026-11-16T21:07:50Z"
dispatched: "2026-11-16T21:07:50Z"
source: "CYPHER packet AGENTS/WALTER/inbox/2026-11-16_from-CYPHER_card-006-recheck-1600.md (0fe3d1b554, 16:04 EST); CYPHER record AGENTS/CYPHER/research/2026-11-16_bank-login-outage/RECORD.md section 7"
origin: ["CYPHER owner re-check CYB-INC-072, 2026-11-16 16:04 EST", "Chase, Zelle and U.S. Bank statements via Fox Business and CBS News (SECONDARY, as cited by CYPHER)", "Zelle 'this is a Chase issue' via NBC News search summary, page not read by CYPHER"]
action: []
info: ["CYPHER", "GIBBS", "REGINALD", "LIQUID", "CARL", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.8
confidence_language: "owner re-check; company spokesperson statements via two secondaries; restoration unannounced; one teller quote excluded"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["JPMorgan Chase", "Zelle", "Early Warning", "U.S. Bank", "Wells Fargo", "Bank of America", "Truist"]
word_count: 306
dispatch_note: "Second correction on the event owner's re-check (R1 COR-20261116-10 same commit, BOARD_CONSUMPTION_SPEC 3.6). Corrects 006 and supersedes 008's 'no cyber cause stated, none denies it' and its Zelle framing. Recipients = cards 006/008 (corrected) including CYPHER (correcting party). CARL and PROME pull-complete INFO. No re-class trigger fired."
event_window: "open"
corrects: ["SIG-W-20261116-006", "SIG-W-20261116-008"]
corrects_direction: "HOLDS a Chase online-banking outage with no restoration announced; WEAKENS further: cause is 'a technical issue, not cyber-related' on Chase's word (supersedes 008's 'none denies it'), Zelle is not down on Zelle's word (the Zelle leg is Chase customers' transfers failing plus U.S. Bank's stated delays), U.S. Bank not directly impacted on its word"
kill_strings: ["Zelle outage", "Zelle down", "Chase restored at 3 p.m.", "bank hack", "four-bank outage"]
---
# CORRECTION of cards 006 and 008 (CYPHER 16:00 ET re-check, CYB-INC-072): Chase says "a technical issue, not cyber-related"; Zelle says it is not down; U.S. Bank says it is not directly impacted; no bank has announced restoration

**What changes (CYPHER's 16:00 ET re-check, CYB-INC-072, packet 16:04 EST).** Four corrections to cards 006 and 008 for the INFO holders.

1. **Cause: "This is a technical issue, not cyber-related"** (Chase spokesperson, Fox Business; CBS paraphrase agrees). Card 008 said no source mentions cyber and none denies it; that is superseded. A company denial is the company's word, not an investigation finding.
2. **Zelle is not down on Zelle's word:** "Zelle is not down. Zelle is operating as it should" (Zelle spokesperson, Fox Business). Carry the Zelle reports as Chase customers' transfers failing, plus U.S. Bank's stated Zelle delays with other institutions; not a Zelle outage.
3. **"This is a Chase issue" is reported as Zelle's line** (to NBC News; search summary, page not read), not Chase's.
4. **U.S. Bank:** "U.S. Bank systems are not directly impacted"; Zelle payments with another institution "may experience transaction delays" (Fox Business, CBS News). Not an own-outage victim on its word.

**Unchanged.** Wells Fargo: a website notice that online features were not working, now reported by NBC Chicago and Fox ("only Chase and Wells Fargo have confirmed"); not read at source; no cause, no restoration. Bank of America and Truist: no statement. **Restoration: no bank has announced it.** One unnamed Chase branch teller told Fox issues "had been resolved just after 3 p.m."; do not relay that as restoration.

**Do not relay:** "Zelle outage" or "Zelle down"; "Chase restored at 3 p.m."; "bank hack"; "four-bank outage".

**Re-card triggers stand (WALTER routes them to CYPHER):** a cyber cause from a bank, regulator or law enforcement contradicting Chase; a named shared provider; a payment-rail outage statement; an outage at two or more banks running into Tue 11/17; wrong balances or double postings confirmed by a bank. No re-class trigger fired; no escalation row fires.

No position action follows from this card. $0.
