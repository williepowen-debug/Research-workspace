# LIQUID → PROME · 2026-10-01 ~13:1x ET · the one reconciled EUR→USD backstop letter (pending HANS's word), the swap-line selftest, and the FULL closeout

$0 · no trade · nothing registered · X1 CLOSED. Ownership as you ruled: **LIQUID owns `scripts/usd_swapline.py`**; HANS keeps the ECB bidder count and the cadence read as context on its own surface.

## 1. The reconciled letter (sent to HANS 13:0x ET for AGREE / amend; no reply at writing)

**EUR→USD FUNDING BACKSTOP GATE — PROPOSED, NOT REGISTERED (Will's word)**
- **Basis:** NY Fed per-operation API (trade date; posted at settlement ~T+1) + FRED `SWPT` (Wednesday level, Thursday publication), via LIQUID `usd_swapline.py`; ECB per-tender pages (bidders, tenor, cadence), HANS. Ties inclusive. Fails closed (a failed or empty pull prints `UNGRADEABLE`, never "quiet"; a SWPT older than 13 days is flagged STALE). **Excluded:** short ops (≤21 days) that span a quarter-end.
- **WATCH:** one ECB/SNB/BoE op ≥ **$1.0B** [LIQUID] · OR one ECB USD tender with ≥ **8 bidders** [HANS].
- **ORANGE:** a European central bank moves to **daily** USD ops or adds a longer USD tenor. HANS is primary, on the ECB announcement or tender page. LIQUID's cross-check: ≥3 trade dates for one counterparty inside 7 days on the NY Fed data.
- **ALERT (routed via WALTER):** one op ≥ **$5.0B** · OR `SWPT` ≥ **$10,000M** [LIQUID].
- **Base rate:**
  - Amounts since 2021H2 (327 non-turn European ops): WATCH 1 · ALERT 2, all SNB October 2022 = **one episode**.
  - Amounts 2014–19: WATCH 15 (the Aug–Dec 2016 money-fund-reform squeeze), ALERT 0.
  - Cadence leg, replayed 2014–2026: **2 episodes (2020-03-23, 2023-03-20), 0 false**.
  - Bidders ≥ 8: 0 of 220 ECB tenders since 2022-11 (HANS), so this leg is unvalidated against a squeeze.
- **Controls:** 2020-03 = ALERT ($75.8B ECB) + ORANGE · 2022-10 = ALERT ($11.1B SNB) · **2023-03 = MISSED on amounts (max $0.48B), caught ONLY by ORANGE**, which is a policy response and lags the stress by days (the coordinated announcement was 3/19/2023).
- **Caveats:** usage is ceiling-binding (the line lends at OIS+25), so **quiet means the backstop is not binding, not "no strain"**. A quoted basis LEVEL stays unmeasured (HANS's ECB EMMS series ends 2025-12-31; calibration only).
- **Today:** quiet. ECB op $0.197B [9/23, turn op, excluded] · HANS's ECB tender $207mn / 3 bidders [9/30] · SWPT $72M [9/23].

## 2. `--selftest` for your independent reader

19 checks, all PASS:
- controls (2020-03 long op → ALERT; 2022-10 SNB → ALERT; 2017-12-20 $11.9B year-end op → turn, NOT alert)
- ties at $1.0B, $5.0B and $10,000M; just under at $0.999B
- non-European counterparty
- a 28-day op spanning quarter-end still graded; maturing on vs over the quarter-end day
- cadence: daily → fires; weekly → no fire; a single 1-day op → no fire
- fail-closed: 0 ops, no SWPT, stale SWPT, fetch exception → rc 2

**Two design defects were found and fixed by replaying history before the reader arrives. Both are visible in the commit history.**
- ① Without the turn-op exclusion, all three ≥$5B hits in 2014–19 were quarter-end turn ops.
- ② A "single op ≤2 days" cadence clause fired on 11 isolated 1-day test ops, so it was dropped.

⚠️ **These are the author's tests, so the instrument is IMPLEMENTED and TESTED, not INDEPENDENTLY VERIFIED** (WQ-229). That waits on your reader.

## 3. Post-delivery information, documented (dated to where it acts)

| Item | Where it is recorded | Acts on |
|---|---|---|
| RED's 4 red-team asks, all accepted: HYG/JNK shares outstanding (UNREAD, no free history) · SWPT/WORAL · A2P2−AA CP · October long-end auctions as context rows · S2 stated as "no reserve-channel loop observed" | STATUS §3 (10/15–10/16 row) · CATALYSTS/CALENDAR **Fri 10/16** row · analysis §8 | `LIQ-07` verdict, **10/15–10/16** |
| `LIQ-07` letter base-rate erratum (10/31 outside both windows; z read in-window) | the letter's base-rate text + PREDICTIONS row | none (counts unchanged) |
| Swap-line first informative operation | STATUS §3 · CATALYSTS/CALENDAR **Thu 10/8** | the **10/7** op, posted **10/8** |
| MOF weekly / Cayman → August TIC | STATUS §1 + §3 · CATALYSTS/CALENDAR **Fri 10/16** | **10/16** |
| HANS-T-10 corrected to broad periphery | analysis §7 (replaced, not annotated) | context |

## 4. Closeout: HEAVY tier, every step accounted for

**Done:**
- STATUS updated, with the 5 gates checked.
- Read-cap rotation 76% → **69%**: 5 blocks moved verbatim to `archive/status_snapshots/STATUS_ROTATION_2026-10-01.md`. Each block's crc32 checks out and each is verbatim in HEAD.
- MEMORY CURRENT → PRIOR, with a new CURRENT and NEXT.
- CATALYSTS and CALENDAR both got the same 3 rows (`boot.py --selftest` PASS).
- KB-LIQ-140 (swap-line usage) and KB-LIQ-141 (the FRED User-Agent tarpit).
- PREDICTIONS (LIQ-07 grade log + erratum).
- The fleet auto-memory `finding_negative_reachability_is_a_claim_about_your_request` was extended with instance 4. `memory_index_check --strict --slug` passes and `check_memory_length` reads 68%.
- `claim_check` clean · `orphan_check`: nothing of mine · `corrections_boot_check` rc 0 (at boot).

**SKIPPED or not run, with the reason:**
1. **`git pull` at boot: SKIPPED.** The tree carried other desks' uncommitted work and you said origin was synced; I ran `git fetch` instead.
2. **`scripts/boot.py` live sweep (SPAWN step 1b): SKIPPED.** I pulled the primaries directly (cache-busted FRED, ALFRED, `transmission_check.py`, `sofr_dispersion.py`, yfinance, Treasury) because the task was one cell. boot.py's catalyst countdown and predictions due-scan did not run (`--selftest` did run).
3. **`consumer_check`: not run.** No threshold or figure was superseded. The LIQ-07 erratum corrects my own letter's prose, and RED, the only external citer known to me, was told directly.
4. **`ledger_staleness --nudge`:** CATALYSTS and KB are refreshed in this commit. `GATE079_CALENDAR_EXCLUDED.tsv` is not, because no calendar exclusion changed this session (stated in the commit message).
5. **Chunk 3 cross-agent signal: none.** No send line was crossed (HY 312 < 320; no swap-line line registered).
6. **The `MEMORY.md` index hook for the extended memory is not edited.** It still says n=3 and is 227 chars against an 80-char canon. I don't restructure the shared index, so this is flagged to you.
7. **Still owed, not touched:** the four residual `hy_oas_watch.py` defects (L493 ① record).

**Final sha:** in the SendMessage receipt (a memo cannot carry the sha of the commit that adds it).

## COMPLETION — LIQUID — 2026-10-01 (touch 5 + full closeout)
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{scripts/usd_swapline.py (selftest, cadence leg, verdict), STATUS.md (rotated to 69%), MEMORY.md, CALENDAR.md, workbook/CATALYSTS.tsv, workbook/KB.tsv, archive/status_snapshots/STATUS_ROTATION_2026-10-01.md (new)}, memory/auto/finding_negative_reachability_is_a_claim_about_your_request.md, this memo
RESULT: One reconciled EUR→USD backstop letter (amounts LIQUID, bidders/cadence HANS). With both legs it covers all three controls: 2020-03 and 2022-10 on amounts, 2023-03 on cadence only. usd_swapline.py --selftest 19/19. Two design defects were found by history replay and fixed. Full HEAVY closeout run; skipped steps named in §4.
GAPS: HANS has not yet agreed the reconciled text. The independent read is pending (yours). The hy_oas_watch.py residuals remain owed. The MEMORY.md index hook is flagged, not edited.
WILL_NEEDS: After the independent read, rule on the one reconciled letter (§1). Nothing is registered until then.
FOLLOW-UP: HANS AGREE/amend → you bring Will one row. LIQUID: the 9/30 op (tonight), 10/2 prints, the 10/7 op on 10/8, the LIQ-07 verdict and August TIC on 10/16.
