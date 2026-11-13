---
signal_id: "SIG-W-20261113-003"
date: "2026-11-13"
timestamp: "2026-11-13T16:46:28Z"
dispatched: "2026-11-13T16:46:28Z"
source: "X bookmark (Will) -> primary report"
origin: ["X bookmark 2120992457630326841 (@willdepue, 2026-11-12T21:29:42Z, author's own post, table image opened)", "X bookmark 2120998208688292286 (@MTSlive relay, folded)", "primary read by WALTER 2026-11-13T16:45Z: https://unemploymentlabs.com/checkpoint-forensics (Will DePue, 'Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs', Nov 12, 2026)"]
action: ["VULCAN"]
info: ["HENRY", "ZHAO", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.6
confidence_language: "primary report read in full at its own page; single researcher, not independently replicated; the report itself says it does not establish chip location, access route or a violation"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["Nvidia", "Blackwell", "GB200", "GB300", "B200", "B300", "DeepSeek", "Moonshot AI", "MiniMax", "Ant Group", "US export controls", "Will DePue"]
word_count: 330
dispatch_note: "AI supply-chain/export-controls is VULCAN primary per ROUTING_TABLE AI_CAPEX; ZHAO INFO for the export-control policy channel. Rule 9 trigger (extreme claim) satisfied by reading the primary rather than the relays; no replication exists to check. Relay bookmark folded as DUP."
event_window: "open"
---
# Forensic report: six Chinese frontier models released since April 2026 (DeepSeek, Moonshot, MiniMax, Ant) carry Nvidia Blackwell fingerprints in their weights; it shows access to the chips, not where they were or a violation; VULCAN

| Lab | Model (release) | Fingerprint | Earlier model |
|---|---|---|---|
| DeepSeek | V4-Flash (Apr 2026) | Blackwell B200/B300 (confirmed bit-for-bit on a B300) | V3 (Dec 2024): Hopper |
| DeepSeek | V4-Pro (Apr 2026) | Blackwell GB200/GB300 | — |
| Moonshot | Kimi K3 (Jul 2026), K3.1-Pro (Nov 2026) | GB200/GB300 (K3 confirmed on a rented GB200) | K2.5 (Jan 2026): Hopper |
| MiniMax | M3 (Jun 2026) | B200/B300 | M2.7 (Apr 2026): Hopper |
| Ant Group | Ling-3.1-flash (Oct 2026) | GB200/GB300 | Ling-3.0-flash (Aug 2026): Hopper |

Method (per the report): the starting weights a model is initialized with depend on the GPU layout and seed. Traces survive training. The author searched more than six trillion layout-and-seed combinations against the open weights. The report says the method matched the developer's own disclosure for all 24 models where the hardware was public. Qwen, GLM, Tencent, Xiaomi and StepFun still read as Hopper.

⚠️ **Limits, in the report's own words:** it provides "technical evidence of access to advanced computing hardware, but do[es] not establish where the chips were located, how access was obtained, or whether export controls were violated." The fingerprint shows where the weights were created, and only "supports, without proving" that training also ran on Blackwell. Restricted AMD hardware is the only alternative the report names. It excludes AMD for V4-Flash and calls it very unlikely for the rest. This is a single-author piece, not peer-reviewed or replicated. The author is described by a relay as a former OpenAI researcher, which WALTER did not verify.

**So what (WALTER's read; VULCAN grades):** this is the first public technical evidence for what US officials and press had alleged without published proof. It lands on top of the Nvidia CEO exit (SIG-W-20261112-002) and the WSJ's vanished Singapore revenue line (SIG-W-20261112-010), with Q3 results on Nov 17. NVDA was $159.66 (−3.93%) on the vendor at 11:46 ET, a move WALTER does not attribute to this report.

**Ask:** VULCAN: grade whether this changes your export-control or Nvidia China-exposure read, and whether it belongs with the Singapore-disclosure item. ZHAO: note it for the export-control policy channel. No position action follows from this card; tradeability is TERRY's.

INFO: HENRY (NVDA tape), ZHAO, RED, TERRY (BOARD-only), PROME. $0.
