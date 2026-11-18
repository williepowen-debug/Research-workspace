# Usage re-run, DESKTOP leg (WQ-714) — RED S67, 2026-11-18 10:20 EST

**Machine:** DESKTOP-BC6EF81 (desktop). **Laptop leg (WilliePOwen): NOT RUN** — owed at RED's next laptop session.
**Authority:** PROME packet `2026-11-17_from-PROME_WQ-714-one-usage-rerun-both-machines.md` (Will 2026-11-17 20:44 ET, "yes to the re-run"). One run per machine; not a recurring duty.
**Scripts:** `usage_by_desk_split.py` and `tier_rollup.py` are copies of `../2026-11-05_op-scale_usage/` with ONE change each: the split prints input / cache-write / output / cache-read separately; the rollup takes its input path as an argument. Counting logic unchanged (`diff` against the originals shows only those lines).

## Totals (tokens; "fresh+out" = input + cache-write + output, the 11/5 measure)

| Window (UTC dates, inclusive) | Claude fresh+out | Codex fresh+out | Combined | PROME | WALTER | DAEDALUS | RED |
|---|---:|---:|---:|---:|---:|---:|---:|
| 11/5 original run, 10/06–11/05 | 172,658,836 | 126,851,423 | 299,510,259 | 23.1% | 16.7% | 10.1% | 1.4% |
| **Re-run today, same window 10/06–11/05** | 131,846,728 | 127,038,420 | 258,885,148 | 18.3% | 17.5% | 8.7% | 0.9% |
| **Re-run today, trailing 10/19–11/18** (11/18 partial) | 275,614,785 | 75,393,439 | 351,008,224 | 20.0% | 12.6% | 6.7% | 1.7% |

⚠️ **The same-window re-run is 40.6M (13.6%) lower than the 11/5 run, and the whole gap is on the Claude side** (Codex 127,038,420 vs 126,851,423). Claude transcripts are being deleted after about 30 days (Claude Code removes old session files by default), so **a re-run cannot reproduce a window older than about 30 days; the 11/5 run stays the better record for 10/06–11/05.** Not verified against the setting itself (INFERRED from the pattern: the Codex side is intact, the Claude side shrank).

## The input / output split (the audit's open question)

| Window | Claude input | Claude cache-write | Claude output | Claude cache-read | Codex uncached input | Codex output | Codex cached |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10/06–11/05 | 93,004 | 104,894,966 | 26,858,758 | 6,204,898,998 | 113,422,580 | 13,615,840 | 3,849,286,784 |
| 10/19–11/18 | 146,294 | 221,862,865 | 53,605,626 | 11,934,735,841 | 66,663,637 | 8,729,802 | 2,598,720,128 |

**Answer: the 11/5 scripts could NOT split input from output (they summed them); these copies can.** On Claude, "fresh" is almost entirely cache-writes; plain input is under 0.1%. Output is about 20% of Claude fresh+out and about 11% of Codex fresh+out. Cache-reads are 43–47× the fresh tokens on Claude, so any dollar estimate turns mostly on the cache-read and cache-write prices, not on output. Pricing is not RED's call and is not applied here.

## Files
- `usage_output_DESKTOP-BC6EF81_2026-10-06_to_2026-11-05.txt` · `usage_output_DESKTOP-BC6EF81_2026-10-19_to_2026-11-18.txt` (per-desk rows; `SPLIT` lines per desk)
- `tier_rollup_DESKTOP-BC6EF81_*.txt` (tier shares, both tier maps as on 11/5)
