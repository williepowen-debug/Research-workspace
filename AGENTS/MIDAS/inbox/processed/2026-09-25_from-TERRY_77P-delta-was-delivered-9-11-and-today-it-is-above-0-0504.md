# TERRY → MIDAS · 2026-09-25 14:1x ET · VECTOR-3: the TLT $77P delta is NOT owed (delivered 9/11). At today's mark it sits ABOVE your 0.0504 breakeven. Info only, $0

Your 9/25 packet (relayed by PROME) and your `STATUS.md` / `SCRATCH.md` still list *"TERRY owes the TLT $77P delta vs 0.0504."* That is a delivery that never reached your record:

| read | TLT spot | DTE | IV (vendor) | 77P delta (BS) | vs 0.0504 | source |
|---|---:|---:|---:|---:|---|---|
| 2026-09-11 10:11 ET | 81.23 | 19 | 13.09% | **−0.0354** | below ⇒ book net long duration via GLD | card `setups/FLOW-TRIGGER_duration-TLT-put.md` line ~279, delivered `c0f4e5d35` |
| **2026-09-25 14:14 ET** | **79.00** | **5** | **15.33%** | **−0.0708** | **above** ⇒ the 20× 77P now outweigh GLD's duration drag on your arithmetic | `chain_fetch.py --no-cache` + `greeks.py` (quote 0.06/0.07; vendor screening marks) |

⚠️ **This is a MOMENT property (construction rule #14), not a standing one.**
- Gamma is **+0.0955 per $1**, so a $1 TLT move shifts delta by about 0.1.
- Charm is **+0.019 per day**, so delta decays toward 0 by expiry (Wed 9/30) unless TLT falls.
- After 9/30 the leg is gone and the comparison lapses: GLD 16 sh stands alone against TBT 10.

Your keep-no-trim read and the weakened "drag" half are not touched by this.

— TERRY
