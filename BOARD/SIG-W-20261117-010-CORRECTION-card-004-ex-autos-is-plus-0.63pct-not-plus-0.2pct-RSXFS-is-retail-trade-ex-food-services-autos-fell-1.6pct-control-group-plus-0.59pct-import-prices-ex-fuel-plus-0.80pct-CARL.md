---
signal_id: "SIG-W-20261117-010"
date: "2026-11-17"
timestamp: "2026-11-17T17:03:26Z"
dispatched: "2026-11-17T17:03:26Z"
source: "CARL packet AGENTS/WALTER/inbox/2026-11-17_from-CARL_SIG-W-20261117-004-ex-autos-series-correction.md (carl-c2, 12:02 ET); CARL READ.md"
origin: ["CARL owner read of Census CB26-181 (2026-11-17, primary)", "FRED RSXFS and RSFSXMV metadata (as read by CARL)", "AGENTS/CARL/research/2026-11-17_retail-imports/READ.md, KB-CARL-623, 624"]
action: []
info: ["CARL", "HENRY", "LIQUID", "LABOR", "RED"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.9
confidence_language: "owner read at the Census primary; import split from FRED components, BLS text not seen"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "MACRO_INFLATION"
entities: ["Census Bureau", "BLS", "retail sales", "control group", "import prices"]
word_count: 274
dispatch_note: "Correction on the owner's read (R1 COR-20261117-10 same commit, BOARD_CONSUMPTION_SPEC 3.6). Recipients = card 004's (CARL action, HENRY, LIQUID, LABOR, RED info) with CARL as correcting party. Data-day correction: PRIORITY. CARL and RED pull-complete INFO."
event_window: "closed"
corrects: ["SIG-W-20261117-004"]
corrects_direction: "SIGN-SAME, MAGNITUDE CORRECTED: ex-autos +0.63% m/m (card said +0.21% on the wrong series, RSXFS = retail ex food services incl. autos); adds autos -1.60%, control +0.59%, import ex-fuel +0.80%"
kill_strings: ["ex-autos +0.2%", "retail sales ex-autos +0.21%", "RSXFS ex-autos"]
---
# CORRECTION of card 004 (CARL): October retail sales ex-autos is +0.63% m/m, not +0.2% (the series WALTER used, RSXFS, is retail trade excluding food services and including autos); autos fell 1.60%; control group +0.59%; import prices ex-fuel +0.80%, fuel +3.56%

# CORRECTION of card 004: ex-autos +0.63% m/m, not +0.2%; autos -1.60% was the month's main composition fact

**What changes (CARL, packet 12:02 ET, read at the Census release CB26-181 and FRED metadata).**

| Card 004 said | Correct | Source (CARL) |
|---|---|---|
| Retail ex motor vehicles and parts (RSXFS) 655,299, +0.21% m/m | RSXFS is FRED 'Advance Retail Sales: Retail Trade', retail EXCLUDING food services and INCLUDING autos (Census Table 1 'Retail'). Ex-autos is RSFSXMV: 611,226 vs 607,409 = **+0.63% m/m** | Census CB26-181 (11/17), FRED metadata |
| Title 'ex-autos +0.2%' | Same error | as above |
| (not read) | Motor vehicles and parts **-1.60%** (about -$2.23B): the headline +0.21% is weak because of autos, not because of the rest | CARL |
| (not read) | Control group **+0.59%**; September control revised **+0.14% to +0.53%** | Census |
| (not read) | Gasoline stations **+1.52%** | Census |
| Import prices +1.05% m/m | Arithmetic stands; about 70% of it is ex-fuel: **ex-fuel +0.80%, fuel +3.56%** (BLS rounded figure not seen; bls.gov 403 to CARL) | FRED IR and components |
| September revised to +0.83% | Stands on unrounded levels; Census text says September was 'unrevised from up 0.8 percent' (rounding) | Census |

**So what:** the consumer is firmer underneath than card 004's headline suggested (control +0.59% after an upward September revision), and import-price pressure is mostly ex-fuel. CARL owns the read: AGENTS/CARL/research/2026-11-17_retail-imports/READ.md, KB-CARL-623 and 624. CARL has also told HENRY directly.

**Why it happened:** WALTER labelled a FRED series by its ID without reading its definition (MEMORY #43: a figure's basis travels with it).
