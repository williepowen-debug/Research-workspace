# CORAL SCRATCH — 2026-06-20 (WALTER inbox + thesis rails install)

**Purpose:** Canonical ephemeral session handoff — where CORAL is, what changed, and what the next session should do. Read at boot; rewrite at closeout. Durable findings live in `MEMORY.md` / workbook; live state lives in `STATUS.md`.

---

## CHANGES SINCE LAST SESSION

- Processed all three pending WALTER ACTION handoffs (`SIG-W-20260619-002`, `SIG-W-20260619-007`, `SIG-W-20260619-008`).
- Added **recent-vintage negative equity** as the upstream collateral canary: ~18-20% of 2024-vintage financed FL buyers underwater, SW-FL Gulf Coast concentrated.
- Resolved the **bankruptcy** thread: M.D. Fla #2 / S.D. Fla #6 by volume is true but population-inflated; +22.2% YoY consumer-led acceleration is the real signal.
- Corrected insurance framing from blanket easing to **split read**: personal/reinsurance easing, but Citizens commercial/condo-association layer still rising (+10.4% capped / +18.8% uncapped).
- Installed thesis rails v1.0 at `thesis/THESIS.md` + `thesis/CHANGELOG.md`; bank-upgrade rail now requires either synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroboration.

## WHAT I DID LAST SESSION

- Appended WALTER consumption rows to `board_log.tsv` and moved consumed files to `inbox/WALTER/processed/` with `git mv`.
- Updated `STATUS.md` dashboard/open questions for negative equity, bankruptcy, and split insurance.
- Added durable facts to `workbook/KB.tsv`; added `VX-CORAL-NEG-EQ-01`, `VX-CORAL-BKCY-01`, and `VX-CORAL-INS-03`; added upstream FLOW pathways.
- Updated `FL_BANK_WATCHLIST.md` for AMTB as the purest South Florida bank barometer and clarified insurance split for banks.
- Refreshed `NEXUS_BRIEF.md` cross-domain sends/waits and `MEMORY.md` durable findings.
- Installed `thesis/THESIS.md` and `thesis/CHANGELOG.md`; updated `CLAUDE.md`, `STATUS.md`, and `NEXUS_BRIEF.md` pointers so thesis rails are durable and live metrics stay in STATUS/workbooks.

## NEXT SESSION

1. **Per-metro convergence grid** — Miami / Tampa / Orlando / Jax / SW-FL, now include negative-equity overlap (Cape Coral/Punta Gorda/Fort Myers/Naples/North Port/Lakeland).
2. **Q2 FL bank earnings prep** — single diagnostic: synchronized criticized/classified → realized NCO + specific reserve build across >1 FL bank; AMTB/USCB are now key local canaries.
3. **Bankruptcy follow-up** — pull native AOUSC F-2 / district data next update; tripwire = Ch.7 per-capita in M.D./S.D. Fla >~230/100k.
4. **Commercial/condo insurance detail** — if possible, isolate Citizens commercial-residential / condo-master layer from blended Commercial Lines.
5. **Add pillar 7/8/9 VX vectors** — migration/tourism/property-tax still need full rails beyond KB/SWEEP.

## OPEN THREADS

- **Bank leg timing:** Does collateral/consumer stress migrate from upstream canaries into Q2 bank NCOs/reserves, or stay delayed?
- **Insurance split:** Personal/reinsurance easing is real; condo/commercial cost pressure is also real. Need finer condo-master-policy data.
- **MARCO boundary:** Shared FL migration/tourism/condo inventory values still need reconciliation to one copy.
- **Property-tax amendment:** Nov 3 2026 remains two-sided — household relief vs local fiscal hole.

## MAIL STATE

- `inbox/WALTER/`: **0 pending**; processed `SIG-W-20260619-002`, `SIG-W-20260619-007`, `SIG-W-20260619-008` into `inbox/WALTER/processed/`.
- Legacy `inbox/`: 1 stale REGINALD BayFirst SBA signal from 2026-03-04 (not processed; outside this task scope).
- `outbox/`: no new acute outbox needed; cross-agent implications captured in `NEXUS_BRIEF.md` CROSS-DOMAIN.
