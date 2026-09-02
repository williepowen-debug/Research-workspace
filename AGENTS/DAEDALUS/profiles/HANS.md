# HANS — DAEDALUS Comprehension Profile

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** FLOW reconcile landed 8/28 · 51d > 45d · body 7/12. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-15**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*
**Built:** 2026-07-10 (firming read, single full-core reader) · **Grade at build:** L3 Conf-M-high (was L2 Conf-L — under-rate, PAT-024 #8) · **Class:** Market, tier-2 spawn-as-needed · **Staleness:** refresh on FLOW reconcile-or-freeze changelist landing or >45d

## Identity in one line — ⚠️ THE LABEL IS WRONG FLEET-WIDE
HANS is **European macro through the US-market lens** (German PMI→ISM ~2mo lead = declared #1 signal, ECB/Fed divergence, EU custody of USTs, EU sovereign spreads/LDI, EU bank USD-funding, EU energy *demand-side* TTF/storage) — per its own charter `CLAUDE.md:3,10`, with military/geopolitics **explicitly ceded to HAWK** (`:92`). The "Geopolitics (energy-geo)" label in `PROME/ROSTER.md:46` (+ formerly this map + `HENRY/STATUS.md:119`) is drift — it mis-rubrics graders and mis-routes signals (PAT-042). ROSTER fix flagged to PROME 7/10.

## Boundary / retirement verdict: DISTINCT LANE — DO NOT RETIRE
Boundaries documented on both sides (HAWK CLAUDE:209 "Europe macro → HANS"; HANS cedes military; BRENT owns barrels, BRENT:127-133). EU-energy three-way split is clean: HANS=TTF/storage/demand · BRENT=crude/supply · HAWK=military catalyst. Retiring HANS orphans Europe entirely — no other agent covers the PMI→ISM lead, ECB/Fed divergence, or EU UST custody.

## File anatomy
| Cluster | Files | State |
|---|---|---|
| Core | `CLAUDE.md` (155 ln, patched 7/8 S1) · `STATUS.md` (154 ln, **honest as-of stamp 2026-06-22** — cleanly parked, frame-flip table :11-22 = load-bearing anti-contamination history) | LIVE, parked |
| Revival | `REVIVAL_PLAN_2026-06-22.md` (8-phase, all ✅ — **one ✅ is FALSE**: "reclassify stale flow rows" never landed in FLOW.tsv) | done-artifact w/ false checkbox |
| Workbook | `ML.tsv` (405 rows → ML-HANS-402 next, sourced+verified) · `VX.tsv` (**56 banded vectors**, 11 groups — ~20 rows refreshed 6/22, rest Feb-vintage mixed) · `PREDICTIONS.tsv` (1 row: HNS-01 **RESOLVED MISS 6/22 w/ calibration note** — loop works, forward-EMPTY) · `FLOW.tsv` (**ROT +111d**: FLOW-8/10 still ACTIVE on "Hormuz closed" reversed war frame) · `VX_HISTORY.tsv` (installed-unexercised) | mixed |
| Legacy | `research/` (6/22 revival modules) · `sources/` RP-HANS-1..10 (Feb-Mar) · `domain/sources/` (Mar war artifacts) · STATUS archives (correctly cited) | frozen |
| Mail | inbox: PROME triage note 6/26 unacknowledged · outbox: **6/22 to-HAWK Qatar packet UNDELIVERED** (delivered/ empty; no from-HANS file anywhere in HAWK's dir) · HENRY flag held pending Will (STATUS:108 — don't auto-deliver) | loose ends |

## Per-dimension vs blueprint (scan negatives: ALL 3 false/mostly-false — PAT-038)
- **§2** — "no conv-matrix" FALSE: VX.tsv is one of the denser matrices in the tier; missing only 5-pt/Independence/composite handles.
- **§4** — "no exit-rules" MOSTLY FALSE: bidirectional per-metric thresholds (":121 <48 re-arms / >50.5 complicates") + wrong-sign discipline actively EXERCISED at revival (ECB threshold re-marked "wrong sign now"); missing N-session counts + kill formalism only.
- **§5** — "predictions unresolved" FALSE: HNS-01 resolved MISS honestly at boot w/ post-mortem. Real gap is the inverse: zero OPEN forward predictions (installed-but-unexercised).
- **§3 caveat** — durable/live split exists but CLAUDE.md embeds a stale live value (":135 PMI 50.7 Feb") + WAR CONTEXT §137-145 still frames the Feb war live.
- **§8** — "Bottom line" + TWO-SENTENCE SUMMARY present (local form, meets).

## Not-L4 because
Routing consumption undemonstrated — the one outbound signal never delivered; HAWK's TRADE:49 cites "HANS: ceasefire back-channel" as design-level consumption only. The L3→L4 path is mostly HANS's own next spawn: deliver-or-kill both parked signals + re-arm 2-3 forward predictions (Q4 storage tripwire, Aug-ISM 49-50.5 band — both already implicit in STATUS) + resolve the expired Jul-4 tariff docket row.

## DO-NOT-TOUCH
1. ML-HANS numbering (next 402) + VX vector IDs (cited in STATUS/research). 2. Frame-flip table + revival note (STATUS:5-22). 3. The Will-held HENRY outbox decision (STATUS:108) — never auto-deliver. 4. `REVIVAL_PLAN` — PROME co-owned. 5. CLAUDE.md:14 revival warning paragraph (fix only the dangling path inside it).

## Owner-lane drift register (next spawn's changelist)
FLOW.tsv reconcile-or-freeze (FLOW-8/10 ACTIVE on reversed frame; the false ✅) · dangling `archive/STATUS_PRE_REVIVAL` ref (CLAUDE:14 + plan; real archive = `workbook/STATUS_archive_20260430.md`) · CLAUDE stale WAR CONTEXT + Feb PMI embed · undelivered outbox + unacknowledged triage note · expired docket (Jun 23-25 talks, **Jul-4 tariff cliff** = first item next spawn) · VX mixed-vintage rows (UST-custody group still TIC Nov-2025) w/o systematic STALE marks · no `ledger_staleness.py` boot lines.
