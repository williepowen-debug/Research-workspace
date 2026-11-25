---
signal_id: "SIG-W-20261125-040"
date: "2026-11-25"
timestamp: "2026-11-25T23:16:30Z"
dispatched: "2026-11-25T23:16:30Z"
source: "AGENTS/WALTER/research/2026-11-25_reboot/CONNECTIONS.md; vendor daily closes CRWV, ORCL, ARM, SPY, SMH, 9984.T pulled 15:42 ET Nov 25"
origin: ["WALTER arithmetic 15:42 ET Nov 25, vendor daily closes", "AGENTS/WALTER/research/2026-11-25_reboot/CONNECTIONS.md (931f8892c3)"]
action: ["SAM", "VULCAN"]
info: ["BROCK", "LIQUID", "HENRY", "NEXUS", "RED", "PROME"]
precedence: "ROUTINE"
signal_type: "research"
confidence: 0.7
confidence_language: "reports: WALTER arithmetic on vendor closes; links from desk records"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["CoreWeave", "Oracle", "Arm", "SoftBank", "OpenAI"]
word_count: 315
dispatch_note: "Will's go 18:15 ET on WALTER's offer. A question to owners, not a finding; moves no score. RED, PROME by BOARD diff."
event_window: "open"
---
# Hand-off on Will's word: CoreWeave, Oracle and Arm daily returns moved together far more from Oct 12 to Nov 24 (CRWV-ORCL 0.88, CRWV-ARM 0.89) than Jul 1 to Oct 9 (0.63, 0.50); after removing SPY and SMH 0.65 and 0.55; SoftBank's next Tokyo session about 0.4; correlation, not cause

# Co-movement test, CoreWeave, Oracle, Arm, SoftBank

| Pair | Oct 12 to Nov 24 (32 sessions) | Jul 1 to Oct 9 | Same, after removing SPY and SMH |
|---|---|---|---|
| CRWV-ORCL | 0.88 | 0.63 | 0.65 (was 0.46) |
| CRWV-ARM | 0.89 | 0.50 | 0.55 (was -0.10) |
| ORCL-ARM | 0.83 | 0.51 | 0.36 (was 0.12) |
| SoftBank next Tokyo session vs ORCL, CRWV, ARM, SMH | 0.39, 0.38, 0.40, 0.38 | 0.33 to 0.45 | not computed |

Daily returns, vendor closes; WALTER arithmetic, not a desk grade. Arm stands in as a SoftBank-held US listing.

**Documented links (desk records, in CONNECTIONS.md):** SoftBank to OpenAI (about $64.6B; a $10B loan against OpenAI shares with a value-linked prepayment, threshold undisclosed; KB-SAM-261, KB-VULCAN-404); Oracle to OpenAI (S&P 7/9 'key credit risk'; share of backlog 45 to 54% is relay-grade; KB-VULCAN-401); CoreWeave to OpenAI listed as backlog exposure, not sized (KB-178). No SoftBank to Oracle credit tie (SAM 11/06).

**The question for the owners:** is the rise in co-movement an OpenAI-specific chain (weaker confidence in OpenAI's payments lowers its value, pressuring SoftBank's loan and Oracle's backlog) or one broad AI-financing selloff? WALTER's data cannot separate them. **Tells:** OpenAI-specific news hitting Oracle and SoftBank but not the rest of AI; or a prepayment, gate or pulled deal naming two of the names. **Against contagion:** CoreWeave's Meta-backed loan is drawing interest (card 035); BROCK's named private-credit exposures to AI cloud firms are each under 1% of their funds.

- **Limits:** 32 sessions is short; returns overlap one selloff; the residual removes only SPY and SMH; the SoftBank lag test uses Tokyo closes after the US session.
- **Ask:** SAM (SoftBank, OpenAI loan) and VULCAN (Oracle, CoreWeave, OpenAI backlog) say whether this is worth a desk test, and if so own it. A 'no' is a complete answer. TERRY by BOARD.
