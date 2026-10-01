# LIQUID → PROME · 2026-10-01 13:0x ET · touch 4: EUR/USD funding blind spot. The basis LEVEL is not reachable free; swap-line USAGE is. Built, lines PROPOSED, today quiet

**On Will's word 12:49 ET ("go for the six").** $0 · no trade · nothing registered · X1 CLOSED. Full write-up: `AGENTS/LIQUID/analysis/2026-10-01_eurusd-basis-instrument.md`. Tool: `AGENTS/LIQUID/scripts/usd_swapline.py` (`--baserate` reproduces every count below).

**In plain terms:** no free source gives the euro–dollar funding premium itself. What we can now see is whether European banks are drawing dollars from the Fed's emergency swap line (through the ECB, SNB or BoE). They draw only once the market premium has climbed to the backstop rate, so it is a late, binary-ish alarm, not a gauge. **It caught March 2020 ($75.8B in one ECB draw) and the Credit Suisse stress of October 2022 ($11.1B from the SNB). It missed March 2023** (largest draw $0.48B). **Today it shows nothing:** $0.197B [ECB, 9/23, a quarter-end turn op] and $72M total outstanding [9/23]. It cannot show 10/01's European widening until the 10/7 operation, posted 10/8.

| Candidate | Pulled | Verdict |
|---|---|---|
| NY Fed swap operations API (per op, by central bank) | ✅ 2014→9/23, 1,355 ops | **USABLE**; posted ~T+1 at settlement |
| FRED `SWPT` (H.4.1, weekly) | ✅ 2002→9/23 | **USABLE**; Thursday release |
| ECB USD allotments | — | the same transaction as row 1 from the ECB side |
| CME futures-implied basis (yfinance 6E=F vs spot, SOFR/€STR) | ✅ 1,624 days | **ACCESS YES, DATA NO**: noise SD ~513bp (daily-change 709bp) vs stress of tens of bp; non-synchronous closes |
| FRED search for a basis series | ✅ | SEARCH-NOT-FOUND |
| ECB MMSR public dataflow | ✅ 446 series | VERIFIED: no FX-swap segment |
| BIS SDMX catalog | ✅ 28 dataflows | SEARCH-NOT-FOUND (names) |

**PROPOSED, NOT registered (Will's word):**
- **WATCH:** one European central-bank op ≥ $1B, with short quarter-end turn ops excluded. Since 2021H2: 1 hit, in October 2022.
- **ALERT, routed via WALTER:** one op ≥ $5B, or SWPT ≥ $10B. Since 2021H2: 2 ops, both SNB in October 2022, so one episode.
- **Acceptance conditions** are in the analysis §4. **Still owed before any registration:** an independent reader (WQ-229, consequential instrument) and a `--selftest` set.

⚠️ **Two findings travel with it:**
- ① FRED's CSV endpoint *tarpitted* the script's own User-Agent (timeout) while curl returned in 0.4s. The first two live runs failed closed (`UNGRADEABLE`), and the SWPT pull now goes through `fetch.py`'s API path. A negative was about the request, not the data.
- ② Before turn ops were excluded, all three ≥$5B hits in 2014–19 were quarter-end turn ops. The exclusion is what makes ALERT mean stress.

**Ownership:** I proposed this split to HANS at 12:50 ET: LIQUID owns the usage instrument and its US-funding read; HANS owns any quoted basis level (HANS-T-12). My pulls went to HANS at 12:59. **No reply from HANS at writing.** PROME confirms or re-assigns.

## COMPLETION — LIQUID — 2026-10-01 (touch 4)
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/LIQUID/{scripts/usd_swapline.py (new), analysis/2026-10-01_eurusd-basis-instrument.md (new), STATUS.md §5}, this memo
RESULT: A quoted EUR/USD basis level is not reachable free: futures-implied is noise (SD ~513bp), FRED and BIS have none, ECB MMSR has no FX-swap segment. Fed swap-line USAGE is reachable and built (NY Fed per-op + SWPT). It caught 2020-03 and 2022-10 and missed 2023-03. Today quiet: ECB $0.197B [9/23, turn op], SWPT $72M [9/23]. It cannot see 10/01 until the 10/7 op (posted 10/8).
GAPS: Lines PROPOSED, not registered. The instrument has no independent reader and no --selftest yet (owed under WQ-229). HANS has not replied on ownership.
WILL_NEEDS: Rule on the proposed WATCH ≥$1B / ALERT ≥$5B or SWPT ≥$10B lines, after the independent read.
FOLLOW-UP: PROME confirms ownership (LIQUID usage / HANS level) and schedules the independent read. LIQUID reads the 9/30 op tonight and the 10/7 op on 10/8.
