# BOND RECEIPT — 2026-09-25 (Fri) ~01:03 → ~03:4x ET · five Will-directed PROME asks

*(Prior: `git show ad8bfdb3c:AGENTS/BOND/RECEIPT.md`.)*

| Item | Disposition |
|---|---|
| **Item 2** (01:02) | FR2004 timing RESOLVED at the primary (`KB-BND-332`); rates-move columns for HENRY; packet → PROME (`fded178ee`…`ad8bfdb3c` range) |
| **FORUM-7** (02:22) | Co-author, path vs premium 9/22→9/24, frozen before ACM 9/24 was read. Standalone legs `69eb3d2ee` (crossed in transit) → §BOND co-sign in HENRY's letter `f7efb8f76`; letter final `bc540e071` (HENRY). `KB-BND-333/334`. A2 conceded KW/X to §3; A1 accepted as a reporting rule; D3 adopted |
| **WQ-290** (02:16 ruling) | `fr2004_join.py` window fixed (PRE < auction ≤ POST); selftest 14/14, mutant fails 4; leg ② re-run → `KB-BND-335`; `KB-BND-306` SUPERSEDED (verbatim); packet `PROME/inbox/2026-09-25_from-BOND_WQ-290-DONE-…` |
| **Self-correction** | My item-2 GAP (c) ("9/2 base-rating used the join pools") was FALSE: `matrix_v2_base_rate.py` uses no FR2004. Corrected in KB-332, the analysis file, SCRATCH and the WQ-290 packet |
| **Inbox** | 3 PROME packets → `inbox/processed/` |
| **Checks** | kb_lint clean · closeout_check rc=0 · join selftest 14/14 |
| **Position** | TLT 77P ×20 HOLD, `$0`, no trade |
| **WQ-157 ② PARK** (L476) | KB-BND-335 stamped INCONCLUSIVE (text; SCHEMA lacks the token — DAEDALUS question per PROME) · `I'` alone = MARKER on TRADE + STATUS · `fb9a9299a` |
| **L477 Q3/Q4** | §7 co-sign `fb9a9299a` · Q4 BOND side `8163ad57d` (`KB-BND-336`), folded into LIQUID's report as D6–D8 · WILL_NEEDS → **WQ-291** (bucket for the kill's dealer leg; D3a +$8.6B caveat relayed) |
