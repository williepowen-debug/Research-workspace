# Usage re-run, LAPTOP leg (WQ-714): RED S68, 2026-11-19 10:5x EST

**Machine:** WilliePOwen (laptop; `hostname` read at run time). **Desktop leg:** `../2026-11-18_usage-rerun_desktop/` (DESKTOP-BC6EF81, 11/18). This completes WQ-714: one run per machine. It is not a recurring duty.
**Authority:** PROME packet `2026-11-17_from-PROME_WQ-714-one-usage-rerun-both-machines.md` (Will 2026-11-17 20:44 ET, "yes to the re-run"); PROME prome-36 asked for this leg 11/19 10:53 ET.
**Scripts:** `usage_by_desk_split.py` and `tier_rollup.py` are byte-identical to the desktop leg's copies (`diff`: none). The desktop README lists their one change each from the 11/5 originals. `combine_machines.py` is new: it adds per-desk fresh+output across the two machines' outputs for the same window, using tier_rollup's own regexes. Run: `python3 usage_by_desk_split.py <since> <until> <claude.json>`.

## Laptop totals (tokens; "fresh+out" = input + cache-write + output, the 11/5 measure)

| Window (UTC dates, inclusive) | Claude fresh+out | Codex fresh+out | Laptop combined | PROME | WALTER | RED |
|---|---:|---:|---:|---:|---:|---:|
| 10/06–11/05 | 115,625,431 | 58,960,548 | 174,585,979 | 29.5% | 10.8% | 0.5% |
| 10/19–11/18 | 165,320,345 | 37,652,777 | 202,973,122 | 32.1% | 10.0% | 0.7% |

| Window | Claude input | Claude cache-write | Claude output | Claude cache-read | Codex uncached input | Codex output | Codex cached |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10/06–11/05 | 86,215 | 91,763,383 | 23,775,833 | 5,144,992,327 | 51,846,291 | 7,114,257 | 1,807,066,752 |
| 10/19–11/18 | 105,213 | 133,675,218 | 31,539,914 | 6,539,121,087 | 32,720,872 | 4,931,905 | 1,393,399,040 |

## Both machines, same window (laptop + desktop; transcripts are local to each box, so the two add)

| Window | Desktop | Laptop | **Both** | PROME | WALTER | DAEDALUS | RED |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10/06–11/05 | 258,885,148 | 174,585,979 | **433,471,127** | 22.8% | 14.8% | 5.9% | 0.8% |
| 10/19–11/18 | 351,008,224 | 202,973,122 | **553,981,346** | 24.5% | 11.7% | 5.4% | 1.3% |

⚠️ **The laptop adds about 58–67% to the desktop-only count,** so the 11/5 desktop-only figure (299.5M for 10/06–11/05) understated fleet use. ⚠️ **The 10/06–11/05 window is still undercounted on both machines.** Claude transcripts older than about 30 days are being deleted (INFERRED on 11/18 from the desktop pattern, not verified against the setting), so the both-machine 433.5M is a floor. The trailing 10/19–11/18 window is the better measure. ⚠️ Both machines were read about one day apart (desktop 11/18 10:2x ET, laptop 11/19 10:5x ET); the 11/18 bar is partial on the desktop.

Pricing is not RED's call and is not applied here.

## Files
`usage_output_WilliePOwen_<window>.txt` (per-desk rows plus SPLIT lines) · `tier_rollup_WilliePOwen_<window>.txt` · `claude_WilliePOwen_<window>.json` (raw per-desk counters) · `combined_both_machines_<window>.txt`
