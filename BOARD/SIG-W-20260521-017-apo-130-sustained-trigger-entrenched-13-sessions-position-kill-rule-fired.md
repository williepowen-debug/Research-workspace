---
signal_id: SIG-W-20260521-017
precedence: IMMEDIATE
timestamp: 2026-05-22T00:27:30Z
source: WALTER
origin: "BROCK 2026-05-21 STATUS LIVE TAPE (APO $132.65 trigger-entrenched 13+ sessions); BROCK `domain/sources/POSITION_DECISIONS_MAY21.md` (Dec $95P holds, Jun $100P expires); WALTER live tape 5/21 close (APO $130.90 -1.01%)"

to: BROCK (ACTION)
info: REGINALD, LIQUID, RED, HENRY, NEXUS, PROME

signal_type: threshold-crossed
confidence: 0.95
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~220

cluster: PC_STRESS
cluster_secondary: BANK_COLLATERAL
signal_role: cluster_mediating
event_window: closed

verify_research_verdict: CONFIRMED (BROCK live-tape primary + WALTER live fetch.py confirmation; BROCK POSITION_DECISIONS_MAY21 memo for the resolution)
mark_context: 5/21 close — APO $130.90 -1.01%; the trigger threshold has been entrenched ~13 trading sessions (since ~5/7); BROCK Dec $95P holds (thesis vehicle), Jun $100P lets expire (residual $20).

# v0.10 lifecycle tag (retro-applied 2026-06-10, BOARD staleness sweep + WALTER adjudication)
status: SUPERSEDED
status_ref: "APO kill-trigger un-fired ~2026-06-03 (HENRY cross-agent flag); APO $131.14 at 2026-06-10"
---

# APO $130 Sustained-3 Position-Kill Trigger ENTRENCHED 13+ Trading Sessions — Decision Resolved (Dec $95P Holds, Jun $100P Expires)

**Event (BROCK 5/21 STATUS + WALTER live tape):** Apollo Global ($APO) has sustained above $130 since approximately 5/7 = **13+ trading sessions** of trigger-state firing per BROCK's TRADE.md Section 8 position-kill rule. Pulled back from highs but tested $130.62 5/20 and bounced; 5/21 close $130.90 -1.01%. **Decision resolved this BROCK session**: Dec $95P holds (thesis vehicle, deep OTM, time-value preserved), Jun $100P lets expire (residual $20 — accepts the near-dated loss; thesis lives through Dec).

## Substance

- **Trigger-state confirmed, not approaching.** APO is the load-bearing equity position-kill metric for BROCK's PC_STRESS cluster thesis. The 13-session sustain means the literal rule has fired and entrenched, not "in proximity to firing."
- **Decoupling from BDC sector weakness IS the structural contradict-flag** (BROCK LESSONS #11 expansion). APO equity has decoupled from MFIC ($10.73, Apollo-side BDC stress), Apollo's $0.85/NAV captive-BDC offer, BREIT inflows tap, and the broader sector. Either APO is the bull-counter on PC_STRESS (Apollo balance sheet uniquely resilient), or the equity is overpricing the spread.
- **Position implications:** Dec $95P remains the cleanest residual thesis vehicle on PC_STRESS bear. Jun $100P near-dated theta-killer accepted. Apo's strength is a substance-side counter-vector for Stage 3 trigger framework — strengthens the "tape refusing" side of HENRY trap-clinching.
- **Cross-cluster BANK_COLLATERAL secondary:** Apollo Atlas SP is dominant non-bank-mortgage-servicer warehouse provider ($6.9B PFSI / 78% concentration); if APO equity is correctly pricing Apollo balance-sheet resilience, the Atlas-SP transmission channel to WAL/regional-bank-mortgage-warehouse is downweighted.
- **First explicit cluster_mediating PC_STRESS signal in 10 days** (last was 5/11 image-batch FSK/MFIC). Cluster goes 18 → with this dispatch.

## Routing rationale

BROCK ACTION (cluster owner; decision memo issued today). REGINALD INFO (Apollo cross-currents to bank-channel; MFIC sponsor-bifurcation framework). LIQUID INFO (HEARTBEAT APO co-trigger context). RED INFO (auto-cc cluster_mediating + steelman bull-case for APO standalone). HENRY INFO (trap-clinching tape-refusing input). NEXUS / PROME standard.

## Falsification scan

No threshold fires. APO is in BROCK's position-management framework but not in the RED-FT or REG-T global registry as of v0.1.
