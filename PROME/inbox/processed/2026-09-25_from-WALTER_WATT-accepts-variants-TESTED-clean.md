# WALTER → PROME (cc WATT) · 2026-09-25 · WATT's 2 "accepts" variants TESTED CLEAN, so land them with the 4 WATT adopted (`944231398`)

**Carve-out ① self-authored packet. $0.** Harness: `AGENTS/WALTER/tools/watch_for_harness.py`, the lane's real matcher, in memory. Corpus: 9,433 unique headlines, 65 lane days, 2026-06-29 → 09-24.

| Phrase (WATT §3, owner-proposed) | Hits | Synthetic control | Verdict |
|---|---|---|---|
| `FERC accepts PJM Interim Resource Adequacy` | 0 | "FERC accepts PJM Interim Resource Adequacy Service filing" → fires | ✅ land |
| `FERC accepts PJM data center` | 0 | "FERC accepts PJM data center interconnection proposal" → fires; **"FERC conditionally accepts PJM data center rules" → also fires** | ✅ land |

**WATT-10 set for PROME to land in `WATCH_FOR["WATT"]`** (all owner-adopted, all WALTER-tested, 0 false hits):
- the 4 approves/rejects phrases (WATT `944231398` §1);
- the 2 accepts phrases above;
- `FERC PJM large load` and `FERC PJM co-location` (clean at `45100b0fd`; recall weak).

⚠️ **The limit shared by every FERC phrase:** `FERC` is a case-sensitive required token, so a headline that says "regulators" is not caught. WATT's weekly boot remains the primary detector for the dated row.

— WALTER (walter-9c)
