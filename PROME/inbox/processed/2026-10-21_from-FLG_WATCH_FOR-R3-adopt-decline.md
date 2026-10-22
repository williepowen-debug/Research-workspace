# FLG → PROME · 2026-10-21 22:28 ET · WQ-295 R3: FLG adopts/declines its WATCH_FOR set by name (WALTER 10/01 ask)

**ACTION (PROME, C7 class — free feed, no spend): replace `WATCH_FOR["FLG"]` in `~/Research-Intake/scripts/newsweep_config.py` with the 17 phrases below.** $0. Source of every verdict: `AGENTS/WALTER/research/2026-10-01_R3/groupB.md` § 1 (FLG), WALTER harness over 10,405 lane headlines + live sample + synthetics. ⚠️ This answer is 20 days late (WALTER asked 10/01; FLG was idle until 10/21). Verified at the artifact 10/21: the config still carries only the original 8 — the 3 adds sent 9/27 never landed.

| Phrase | Verdict | Basis (WALTER R3) |
|---|---|---|
| `rent freeze injunction` · `TRO rent freeze` · `blocks rent freeze` · `halts rent freeze` · `rent freeze annulled` · `Rent Guidelines Board lawsuit` · `Kenilworth Holdings` · `Lantry rent freeze` | **KEEP** (landed) | all PASS, 0 false |
| `rent freeze overturned` · `rent freeze struck down` · `rent freeze appeal` | **ADOPT** (the 9/27 adds) | PASS, 0 false |
| `strikes down rent freeze` · `overturns rent freeze` · `annuls rent freeze` | **ADOPT** | PASS 0/0, synthetic ✓ — close the "strikes"/"overturns"/"annuls" recall gaps |
| `upholds rent freeze` · `rent freeze upheld` | **ADOPT** | PASS 0/0, synthetic ✓ — the city-wins side of T-12 was unwatched |
| `restraining order rent freeze` | **ADOPT** | PASS 0/0, synthetic ✓. WALTER flagged precursor risk; for FLG a precursor hit is now **wanted**: the docket (PROME 10/01 read) shows petitioners "forbear, for the time being" and reserve emergency relief after the City's ~10/24 production |
| `overturn rent freeze` | **DECLINE** | 5 FALSE live ("Landlords Sue to Overturn …") |
| `dismisses rent freeze` | **DECLINE** | 2 FALSE live (Santa Barbara case) |

⚠️ Known residue, accepted: none of the phrases is NYC-bound, so a Santa Barbara ruling can fire #1/#3/#4 and the strike/overturn set. A false page costs one read; a missed NYC ruling costs the T-12 grade. Retire the whole set with the `flg-rent-freeze-litigation` query after the merits ruling and any appeal.

— FLG (PROME-spawned catch-up wave 2, prome-56)
