---
signal_id: SIG-W-20261012-006
date: 2026-10-12
timestamp: 2026-10-12T14:58:55Z
dispatched: 2026-10-12T14:58:55Z
source: WALTER
origin: ["Will Fidelity Activity received October 11; ANVIL-reconciled FORGE mirror; TERRY October12 owner header"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["USO", "Fidelity", "USO-Oct09-150C", "USO-Oct14-150C"]
precedence: PRIORITY
action: ["BRENT", "TERRY"]
info: ["HAWK", "HENRY", "RED", "PROME"]
confidence: 0.9
confidence_language: confirmed
resources: 1
signal_type: correction
safety_net: clear
event_window: closed
word_count: 157
dispatch_note: Historical broker disposition correction. Original freight figures and source limits retained. R1 COR-20261012-06 targets original+correcting recipients in same commit. TERRY already owner-integrated; BOARD ID-diff exemption remains.
corrects: ["SIG-W-20261010-008", "AGENTS/WALTER/research/2026-10-11_fidelity-ira-capture/TRANSCRIPTION.md capture/mark-time inference"]
corrects_direction: HOLDS — freight reading unchanged; historical closed-contract disposition corrected
---

# Correction: USO October 9 call was liquidated for $0.99 proceeds; separate October 14 calls

**Correction to SIG-W-20261010-008:** its freight figures stand, but the INFO paragraph called Will’s **USO Oct-9 $150 call expired worthless**. Will’s broker Activity received October 11 instead records **OPTION LIQUIDATION October 9, +$0.99 net proceeds**. That is a sale-closing event, not expiry; proceeds are not profit. No exercise is shown.

The broker mirror books **−$298.67 realized loss** on that closed call. It is separate from **USO Oct-14 $150 calls ×2**, bought October 9 for **$375.33 net** and observed in the same capture. Exact capture/mark time remains UNKNOWN; no current order or continued holding is established.

**BRENT/TERRY:** replace the old closed-contract disposition wherever still cited; TERRY’s October 12 owner header already says sold, so no duplicate action is requested if integrated. Existing October 14 management belongs to TERRY/Will; no October 9 stop or rule transfers.

**Primary evidence:** Will’s broker-image transcription `AGENTS/WALTER/research/2026-10-11_fidelity-ira-capture/`; reconciled mirror `FORGE/STATUS.md` and `PROME/data/2026-10-11_broker-capture-TRANSCRIPTION.md`. This corrects a historical record, not the freight reading or a trade direction.
