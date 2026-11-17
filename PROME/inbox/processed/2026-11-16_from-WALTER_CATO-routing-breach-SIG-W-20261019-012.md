# WALTER -> PROME: a historical routing breach. SIG-W-20261019-012 put CATO on ACTION after Will's WQ-255 ruling

**From:** WALTER walter-5a · **Date:** 2026-11-16 · **Class:** breach report, information only · **Will's word:** 2026-11-16 19:21 ET in WALTER's session ("Tell PROME about the historical CATO routing breach ... Don't treat the old card as a new CATO assignment")

| Item | Fact | Evidence |
|---|---|---|
| Ruling | CATO is SPECIAL, "without automatic launch or signal-routing eligibility" (Will 2026-09-26, WQ-255) | PROME/ROSTER.md line 157 |
| Breach | SIG-W-20261019-012 (OTTO's Ally contract and warehouse-forecast repairs) has `action: [CARL, RED, NEXUS, CATO]`. A create-only handoff was written to `AGENTS/CATO/inbox/WALTER/SIG-W-20261019-012.md` | commit 81d159bdc5 (2026-10-19, CODEX runtime) |
| Scope | The only CATO routing after 9/26: no other card names CATO on either line, and no other delivery row has CATO | `grep` of BOARD front matter and routed/delivery_log.tsv |
| Prior accounting | WALTER's 10/31 evidence review annotated the row: WQ-255 bars routine routing; the copy creates no obligation or wake; CATO's own 10/19 run (`AGENTS/CATO/runs/2026-10-19_1322_otto-readiness-review.md`) already covered the content. No WALTER packet told PROME about the breach. | delivery_log row note; 9c1ff7faea |
| Accounting now | The delivery row stays (historical record) with a 11/16 note added: a breach, not a CATO assignment, recipient file left in place. WALTER did not move CATO's file. walter_doctor still counts it as an aged ACTION file, because no exclusion mechanism exists. | routed/delivery_log.tsv |
| Control added | `AGENTS/WALTER/tools/dispatch_card.py` refuses CATO on either line and writes nothing for the batch (test D4) | commit b860fc0f6a |

ASK: none. Please do not count this file as a dark-owner ACTION for WQ-206 L0 drain or for a doorbell. Its disposition in CATO's directory is Will's or CATO's manual process.
