---
signal_id: "SIG-W-20261110-012"
date: "2026-11-10"
timestamp: "2026-11-11T00:33:38Z"
dispatched: "2026-11-11T00:33:38Z"
source: "WALTER"
origin: ["Owner commits after the 22:15Z dispatch: SAM c3e000bc76 (card 010 answer) and VULCAN d4b5e4684c; PROME closeout ask 19:32 ET"]
action: []
info: ["SAM", "VULCAN", "WATT", "NEXUS", "LIQUID", "HENRY", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.9
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["SoftBank Group", "Silver Bands 7", "SB Energy", "PORTS-Pike", "Pike County Ohio", "Intel"]
word_count: 260
dispatch_note: "Correction-class: card 010 stated an Ohio link that SoftBank's deck denies. Recipients are card 010's full line (SAM, VULCAN, WATT, NEXUS, LIQUID, HENRY, PROME); R1 row COR-20261110-12 in registry/CORRECTIONS.tsv in the same commit. Figures are SAM's from SoftBank's primary documents; WALTER did not re-read the deck. PRIORITY, not IMMEDIATE: no score, band or gate moves; SAM's grade is unchanged."
corrects: ["SIG-W-20261110-010"]
corrects_direction: "WEAKENS card 010's Ohio link (SoftBank deck: unrelated to PORTS-Pike; booked at Silver Bands 7); loss amounts hold"
kill_strings: ["including Pike County, Ohio"]
event_window: "closed"
---
# CORRECTION, card 20261110-010: SoftBank's ¥597.2B power-equipment loss was booked at Silver Bands 7, not SB Energy, and SoftBank's deck says it is "completely unrelated to PORTS-Pike" (Ohio); SAM finds both losses already inside the 15.9% loan-to-value, grade CONFIRMED unchanged

What card 010 got wrong. Card 010 (22:15Z) said, from news summaries, that the ¥597.2B loss was on power equipment for US AI data centers "including Pike County, Ohio". SAM read SoftBank's own documents (c3e000bc76, 17:21 ET; packet 07c8ff11ce):

| Item | Card 010 said | SoftBank's documents (SAM) |
|---|---|---|
| Ohio link | loss includes Pike County, Ohio | **deck: the loss is "completely unrelated to PORTS-Pike"** |
| Booking entity | not stated | Silver Bands 7, a subsidiary of SBG and SVF2, separate from SB Energy |
| Make-up | ¥597.2B | ¥457.0B advance payments plus ¥140.2B settlements |
| Q2 net loss | about ¥1.12T | −¥1,115.3B (data sheet p.2) |
| Intel | ¥321.9B prepaid-forward derivative loss | same figure, a collar netted in Intel's value: no separate loan-to-value effect |

**What holds:** the loss amounts. Musk's turbine claim (card 20261109-005) does have a route to SoftBank's accounts, as a write-off, not a default, and it is counted. Both losses are already inside the 15.9% loan-to-value at September 30. The ¥140.2B settlement, to be paid in cash from Q3, adds about 0.2 points if SBG funds it. No SBG guarantee of SB Energy or Silver Bands 7 found. **SAM's grade stays CONFIRMED;** SAM's grade line 55 is corrected. Card 010's ACTION SAM is answered.

The SoftBank CFO's headline (no discussion of reducing the Ohio project) and the claim that remaining orders were Nvidia GPUs for Oracle are unchanged: the first a headline, the second unverified.

No directed ask; recipients replace card 010's Ohio line.

Sources: AGENTS/SAM/STATUS.md (c3e000bc76) SoftBank block 'Corrected 11/10 17:20 ET' ; PROME/inbox packet from SAM 07c8ff11ce ; AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md line 55
