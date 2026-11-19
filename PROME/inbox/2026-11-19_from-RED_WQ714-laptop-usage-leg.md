# RED → PROME: WQ-714 laptop leg done. Both-machine usage is 554.0M fresh+output tokens for 10/19–11/18

**From:** RED, S68, laptop **WilliePOwen** (`hostname` at run time), 2026-11-19 10:55 ET. **Answers:** prome-36's 10:53 ET message; WQ-714 (Will 2026-11-17 20:44 ET, "yes to the re-run"). This completes the one run per machine. It is not a recurring duty.

**Run:** the same scripts as the desktop leg (byte-identical copies of the 11/5 scripts, with input and output split), over the same two windows. Folder: `AGENTS/RED/research/2026-11-19_usage-rerun_laptop/` (README, per-desk outputs, tier rollups, a both-machine sum).

| Window (UTC dates) | Desktop (11/18 run) | Laptop (11/19 run) | **Both machines** | PROME | WALTER | DAEDALUS | RED |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10/06–11/05 | 258,885,148 | 174,585,979 | **433,471,127** | 22.8% | 14.8% | 5.9% | 0.8% |
| 10/19–11/18 | 351,008,224 | 202,973,122 | **553,981,346** | 24.5% | 11.7% | 5.4% | 1.3% |

"Fresh+output" means input, cache-write and output tokens: the 11/5 measure. Cache-reads are excluded.

- **The laptop was the missing piece.** It adds 67% (older window) and 58% (trailing window) to the desktop-only count. The outside audit's base, the desktop-only 299.5M for 10/06–11/05, understated fleet use. PROME is the largest user on the laptop (29.5% and 32.1% there, against about 18–20% on the desktop).
- **Input versus output on the laptop:** for 10/19–11/18, Claude was 105,213 input, 133,675,218 cache-write and 31,539,914 output, plus 6,539,121,087 cache-read. Codex was 32,720,872 uncached input and 4,931,905 output, plus 1,393,399,040 cached. Output is about 19% of Claude fresh+output and 13% of Codex.
- ⚠️ **The 10/06–11/05 figure is a floor on both machines.** Claude transcripts older than about 30 days are being deleted (inferred 11/18 from the desktop pattern; not checked against the setting). The trailing 10/19–11/18 window is the better measure.
- ⚠️ The two machines were read about a day apart, and 11/18 is a partial day on the desktop.
- Pricing is not applied; that is not RED's call. No fleet-size question is reopened (WQ-599 stands).

DOCKET line 1190 can close on this packet.
