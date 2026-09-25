# BOND RECEIPT — 2026-09-25 (Fri) ~01:03 → ~01:5x ET · PROME item 2 (Will-directed 01:01 ET)

*(9/24 sessions: `git show fded178ee:AGENTS/BOND/RECEIPT.md` · earlier: `8308eff78`, `d93987642`.)*

| Item | Disposition |
|---|---|
| **Tasked** | PROME packet `inbox/2026-09-25_from-PROME_bounded-follow-up-…` (`40915c8c0`, verified at the artifact): (1) resolve the FR2004 settlement timing FIRST · (2) ACM/KW/composition columns for HENRY's matched-date table · (3) preferred reading + strongest counter · (4) keep DFII10 9/24 + 004 expiry visible |
| **(1) FR2004** | ✅ **RESOLVED at the primary**: FR 2004 Instructions eff. Jan 2022, GEN-6 §II.C + A-1 (trade-date; award counted on the award date) + Appendix A (WI ⊂ A). 9/16 print admissible. `KB-BND-332`; `KB-BND-327` → CORRECTED |
| **Side finding** | 🔴 `fr2004_join.py` PRE ≤ auction mis-windows Wednesday auctions (75/228) → WQ-157 "p=0.009" becomes −4.5bp p=0.248 on the trade-date window. Scripts saved in `analysis/`. Instrument NOT changed (PROME/Will call). 5Y dealer POST = 9/23 as-of ~10/1 (not 10/8) — corrected by pattern |
| **(2)(3)(4)** | `analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md` §2–§4 |
| **Peer** | HENRY messaged path + answer; cites, not re-derives |
| **Checks** | kb_lint clean · closeout_check rc=0 after moving NEXUS_BRIEF's LIVE-REGION-ENDS sentinel above the superseded 9/17→7/28 blocks (the class fix for an aged EXPIRED-PENDING flag) |
| **Outbox** | `PROME/inbox/2026-09-25_from-BOND_item2-…` (carve-out ①) + SendMessage prome-fa |
| **Position** | TLT 77P ×20 HOLD, `$0`, no trade |
