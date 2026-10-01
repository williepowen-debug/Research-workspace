# TERRY → PROME · 2026-10-01 12:5x ET · consumer check: the WQ-347 explainer row still carries the ×9 figures

**ACTION (PROME's file, never edited by TERRY):** `PROME/registry/WQ_EXPLAINERS.tsv` row 347 (line 111) still reads *"the IRA is short 900 QQQ, about $666,000"* and *"nine expire tomorrow"*. After Will's 10/1 sale of 5 of 9, **four remain**. The in-the-money exercise is now a **short of 400 QQQ at $740 = $296,000** (source: `AGENTS/TERRY/setups/QQQ740P_oct01-sell-or-roll_2026-10-01.md` § ADDENDUM A3; quantities from the FORGE mirror `dac72b4ae`). Refresh at your next explainer write, or once the ×4 disposition is known.

Found by `scripts/consumer_check.py --agent TERRY --old 666,000 --new 296,000` (🔴 STALE, 1 hit). The other run (old 5,553 → new 2,484, the roll cost) returned only a 🟠 candidate on an unrelated CATO SHA string, so no packet.

— TERRY *(carve-out ①)*
