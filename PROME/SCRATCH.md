# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-19 14:53 ET (OpenClaw Prome — SAM/HAWK audits + WALTER deep-research flag design closeout)

## What Just Happened

1. **Pulled and reviewed SAM + HAWK pushed changes.**
   - SAM added `AGENTS/SAM/thesis/THESIS_v1.6_DRAFT.md`; initial audit flagged the USDJPY direction bug, CFTC timing issue, Pillar 1/3/4 wording, vehicle-gate discipline, and FXY-vol proxy caveat.
   - SAM subsequently incorporated the fixes and added a convexity-tail EV table. Prome read: the table supports **holding the small FXY tail stub, not adding size**; next real gate remains Jun 20 CFTC.
   - HAWK incorporated audit fixes: Brent math corrected to ~-9.5% from Jun 12, stale ~$77 references purged, energy-strike memory contradiction corrected, BRENT handoff delivered, and product/crack → Brent flip triggers added.

2. **WALTER deep-research candidate flag design was reviewed and greenlit.**
   - Will wants WALTER to flag routed signals that may deserve external/deeper research, without WALTER running that research.
   - ORC drafted `AGENTS/WALTER/design/DEEP_RESEARCH_FLAG_PROPOSAL.md` on branch `claude/brave-gates-jl3699`; Prome reviewed the branch copy and the later v0.3 attachment.
   - Final Prome recommendation: route to WALTER for ratification; **do not land live specs directly from ORC**. WALTER owns CHECKLIST v0.18 + ledger + doctor changes.
   - Approved shape: Full-WALTER-only Phase 2.8 flag; mandatory materiality gate; dispatched signals only for v1; ledger with `prompt_ref` + `deadline`; no FORMAT_SPEC header field; narrow `walter_doctor` overdue-pending check included in v1.
   - Implementation nit carried forward: actual ledger file must be real TSV, and `deadline` should start with ISO date or `open` so `walter_doctor` can parse it.

3. **HERMES/Hermes-v2 discussion resolved at concept level.**
   - Prome recommendation: do **not** revive legacy HERMES. If pursued, revive only a courier/receipt service: no judgment, no routing authority, no analyst role; WALTER remains signal/news router.

4. **Heartbeat poll / dashboard check ran.**
   - Dashboard compact pull: HY OAS **263 [FRED 6/17]**, CCC **939 [6/17]**, 10Y **4.49 [6/17]**, Brent **$80.59**, USD/JPY **161.27**, FXY **$56.85**, KRE/WAL green, VIX **16.78**, BIZD still red.
   - Regime unchanged: broad cascade still not confirmed; HY <260 kill-line remains close; carry stress still live.

## Current Git State

- Local repo was clean/synced before closeout edits.
- This closeout is intended to be **committed locally only** and **not pushed** per Will: “Stop short of pushing.”

## Current Operating Picture

- **WALTER deep-research flag:** greenlit for WALTER to ratify/implement. Prome should verify after WALTER lands it: CHECKLIST v0.18, 11-col TSV ledger, prompt embed, dispatch_note convention, Quick/Full one-liners, `walter_doctor` check, STATE sync, version-drift check.
- **Quick-WALTER boundary still holds:** Prome/Quick-WALTER does not route fresh news or discretionary research flags.
- **Market state:** same unresolved divergence — HY 263 near <260 kill, VIX/banks benign, carry red.
- **Positions:** no position/expiry action without broker/Will truth.

## Next Reboot Entry Point

1. Pull/verify repo; note this closeout commit may be local-only until Will approves push.
2. If system lane: check whether WALTER ratified the deep-research flag; inspect the actual spec/ledger/doctor diff, not just the proposal.
3. If market lane: refresh dashboard/FRED HY; key question remains whether HY breaks <260 or banks/PC re-weaken enough to offset.
4. If SAM lane: check Jun 20 CFTC against SAM v1.6 EV/convexity survival gates.

## Cautions

- Do not push this closeout unless Will explicitly asks.
- Do not edit `AGENTS/WALTER/*` from Prome for the deep-research feature; WALTER owns ratification.
- Do not spawn Quick-WALTER for fresh news/screenshots/research-flag judgment.
- No trade execution or old option/expiry cleanup without broker/Will reconciliation.
