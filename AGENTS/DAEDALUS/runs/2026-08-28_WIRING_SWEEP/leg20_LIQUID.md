# Leg ⑳ BOOT-SEQUENCE AUDIT — LIQUID
2026-08-28 · read-only · subject: `AGENTS/LIQUID/` (CLAUDE.md SPAWN PROTOCOL + `scripts/boot.py`, 620 lines)

## 1. Boot/spawn sequence extracted (CLAUDE.md:18-32)

| Step | Claim (verbatim, truncated) |
|---|---|
| 0 | "`git pull` — sync from GitHub before reading anything." |
| 1 | "Read `STATUS.md` — dashboards (credit, domestic, foreign), thresholds, transmission mechanisms. (On a cold boot, CALENDAR / MEMORY NEXT SESSION are touched here too.)" |
| 1b | "Live sweep — `scripts/boot.py` — ...one-command boot brief: live 3-dashboard pull (FRED+yfinance) + catalyst countdown (`CATALYSTS.tsv`) + predictions due-scan (`PREDICTIONS.tsv`). **This is the live-primary source**" |
| 2 | "WALTER signal intake (`inbox/WALTER/`)... List not-yet-logged files... append row to `board_log.tsv`... `git mv` to `processed/`." |
| 3 | "Execute the task — `acted` board items + live-primary pulls feed the work" |
| 4 | "Write results back to `STATUS.md`" |
| 5 | "Research detail → `domain/sources/`" |
| 6 | "Write-back tail → `CLOSEOUT.md`" |

## 2. Step-by-step: claim vs. delivered

| Step | Claim | Instrument | Verdict | Evidence |
|---|---|---|---|---|
| 0 | git pull sync | shell `git pull` | DELIVERS (mechanical, not independently gradeable) | CLAUDE.md:22 |
| **1** | "Read STATUS.md" whole, primary memory | harness Read tool | **SUBSTITUTED-risk / OVER-CAP** | `AGENTS/LIQUID/STATUS.md` = **119,776 B**, 218 lines. Harness Read cap ≈54,250 B. File is **2.21× over cap** despite satisfying LIQUID's own written rule "STATUS.md stays under 250 lines" (CLAUDE.md:80) — the line-cap passes clean while the byte-cap silently truncates. Avg 549 B/line (dense prose paragraphs, e.g. STATUS.md:1 alone ≈2,700 chars). A boot Read of this file is **not guaranteed to see step 4/6's own most-recent write-backs** if they land past the truncation point (file grows top-down by session, most recent = top; truncation risk is at the BOTTOM, i.e. history/KB, but that still fails the file's own "primary memory... Read" claim of wholeness). |
| 1 (cold-boot rider) | "CALENDAR / MEMORY NEXT SESSION are touched here too" | harness Read of `CALENDAR.md` / a `NEXT SESSION` section of `MEMORY.md` | CANNOT-JUDGE (scope ambiguous) | `CALENDAR.md` = 28,899 B (under near-cap floor, clean). `MEMORY.md` = 62,930 B / 296 lines — **OVER-CAP if read whole**, but the CLAUDE.md wording names "MEMORY NEXT SESSION," which is a labeled section (`MEMORY.md:273 "### NEXT SESSION"`), not necessarily the whole file. Cannot determine from static text alone whether agents Read the file whole or just that section — flagging the byte fact, not asserting the verdict. |
| 1b | "one-command boot brief: 3-dashboard live pull + catalyst countdown + predictions due-scan, alert-collapsed" | `scripts/boot.py` | **DELIVERS, with one systemic SILENT gap (see Finding #2)** | Executed live (§3 below): RC=0, 25 series, 0 fetch errors, all three sections rendered. |
| 2 | WALTER inbox drain → `board_log.tsv` append + `git mv` to `processed/` | manual protocol (not scripted) | DELIVERS (substrate intact) | `AGENTS/LIQUID/inbox/WALTER/` currently holds only `processed/` (no pending `.md` at top level) — inbox is drained. `board_log.tsv` header = `timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes` (183 lines, matches v0.2 spec) verified by `head -1`/`tail` read. |
| 3-6 | Execute / write-back / research / closeout | agent-judgment steps, not instruments | CANNOT-JUDGE (no script to trace; behavioral, not mechanical) | — |

## 3. Execution transcript

- Pre-check: `git -C .../Research-workspace status --short -- AGENTS/LIQUID/` → **empty, clean**. Proceeded to execute (rule 3 of task).
- Write-scan: `grep -nE "open\([^)]*['\"]w|write_text|to_csv|\.write\(|subprocess|shutil|git commit|git add" boot.py sofr_dispersion.py` → **no matches**. Script is write-free (stdout only). Cleared to run.
- Run 1 (repo-root cwd, full): `.venv/bin/python3 AGENTS/LIQUID/scripts/boot.py` → **RC=0**, 25 series, 0 fetch errors, 10.8s. HY OAS 263bps 🟢, CCC OAS 1031bps 🔴 (>1000 trip), CCC-BB 878bps 🟢, 10Y 4.66% 🟠, 30Y 5.18% 🟠, USD/JPY 159.85 🟢.
- Run 2 (repo-root cwd, `--verbose`): all 25 series render individually incl. all rows collapsed-hidden in Run 1 (SOFR, IORB, SOFR-IORB, SOFR75-IORB, SOFR99 tail, 2Y, Reserves, RRP, SRF, HYG, TLT, Brent, BB OAS, IG OAS, HY-IG basis, Euro HY OAS, VIX) — none showed `ERR`, `N/A`, or a fallback marker. SOFR75-IORB rendered via the new `sofr_dispersion.py` instrument (🟢, "z +0.0 ... regime tightening +7.1bp/yr") — dynamic import succeeded, no fallback path exercised.
- Run 3 (cwd = `AGENTS/LIQUID/`, `--quick`, invoking the venv python by absolute path): **RC=0**, 18 series (yfinance skipped as designed), same FRED values as Run 1/2 — **confirms cwd-proofness** (path resolution via `Path(__file__).resolve().parent` and `.parents[2]` works from both repo root and the agent's own dir).
- Post-check: `git -C .../Research-workspace status --short -- AGENTS/LIQUID/` → **empty again** — boot.py did not mutate its own tree (no PAT-054 class finding).
- `--selftest`: **PASS** — `✓ FORGE fetch.py import OK`, `✓ CATALYSTS.tsv OK (20 rows, 8 cols, dates parse)`, `✓ PREDICTIONS.tsv OK (all OPEN timeframes parse)`, `✓ KB.tsv OK (106 rows, 13 cols, IDs well-formed)`.
- Cross-check of the "Unattended Watcher" step (`AGENTS/LIQUID/alerts/HY_OAS_STATE`, read by `watcher_echo()`): confirmed the systemd timer is real and live — `systemctl --user status liquid-hy-watch.timer` shows `Active: active (waiting)`, next trigger `Fri 13:00:00 EDT`, prior run `Aug 27 09:53:09`. `watch.log` tail shows 5 consecutive daily runs, no gaps. This is a genuinely-live instrument, not a decorative one.
- Transcripts saved (this run's dir only): `leg20_boot_stdout.txt`, `leg20_boot_verbose.txt`, `leg20_boot_fromliquid.txt`, `leg20_boot_selftest.txt`.

## 4. Three most consequential findings

1. **STATUS.md is 119,776 B against a ≈54,250 B harness Read cap (2.21× over) while satisfying its own 250-line rule (218 lines) — the byte failure mode is invisible to the file's own governing metric.** SPAWN step 1 is the literal first instruction of every boot ("Read `STATUS.md`"), and the file's own header calls itself "**Primary memory**." A line-based self-check gives false confidence that the file is boot-safe. (`CLAUDE.md:80`, `AGENTS/LIQUID/STATUS.md` wc: 218 lines / 119,776 B.)

2. **`boot.py`'s two dashboard-builders apply inconsistent error-visibility rules — `build_credit()`'s core metrics report a per-row `ERR` marker on fetch failure, but `build_domestic()`'s SOFR, IORB, SOFR75/SOFR99, DGS2, DGS10, the headline DGS30, Reserves, and RRP do not.** Trace (`boot.py:179-255`): each of these blocks reads `if not err: ... add(...)` with **no `else` branch** — contrast with HY OAS (`boot.py:89-90`, explicit `if err: add(...ERR...)`), CCC OAS (`:116-117`), BB OAS (`:124-125`), IG OAS (`:149-150`), Euro HY (also silent, `:161-169`, no else), and SRF (`:266-268`, explicit partial-failure reporting). On a fetch failure for one of the silent series, `fred_series()` still increments the module-level `ERRORS` counter (`boot.py:57-61,69-70`), so the **only** surviving evidence is a decremented row-count / incremented fetch-error count in the final `BOOT SUMMARY` line (`boot.py:571-573`) — no row, no note, no reason on the dashboard itself. This is exactly the class the task brief calls SILENT ("prints nothing on today's state and cannot say why — no '0 found in N searched' line"), and it hits **DGS30**, a `headline=True` row (`boot.py:239`) that feeds the duration-regime read cited directly in STATUS.md's BOTTOM LINE. **Not observed live** — today's run had 0 fetch errors on all 25 series (§3), so this is a static-trace finding only, unconfirmed at runtime this session.

3. **Dashboard 3 (Foreign Official) delivers only 2 of the domain's named series (USD/JPY, Brent) — TIC, Belgium, and auction-indirect data are absent from `boot.py` entirely.** This is **by design and self-disclosed**: CLAUDE.md:24 itself instructs "Pull anything load-bearing that boot.py doesn't cover (TIC country tables, auction internals) from primary directly," and `PRICE_SPECS` (`boot.py:275-284`) confirms no TIC/Belgium ticker exists in the script. Recorded as DELIVERS-PARTIAL-BY-DESIGN, not a hidden gap — but it means the CLAUDE.md DOMAIN SCOPE line "Foreign official flows (TIC, Belgium **level** watch...)" and the mandate-extension PRIMARY lane (dealer PD stats, MMF flows) are **not** covered by the "This is the live-primary source" claim at step 1b for those specific series — a reader who trusts 1b's framing without reading its own caveat could believe the boot brief is complete for Foreign/microstructure when ~half that dashboard's named scope requires a manual pull every session.

## 5. Secondary / minor observations (not top-3, still worth recording)

- **CCC OAS threshold hand-copy, currently non-diverging.** `boot.py:112-114` uses an inline yellow floor of **960** ("elif ccc > 960"), while the SHARED `FORGE/tools/market-data/config.py` (the canonical SENTRY band the HY OAS comment explicitly claims to mirror, `boot.py:85-87`) sets CCC yellow at **(900, 1000)**. `boot.py` never imports `config.py` for CCC — the 960 line is an independent, hand-typed choice, not a claimed mirror (unlike HY OAS, which does claim "mirrors the live `hy_oas_watch.py`" and, checked against `config.py`'s live 265/280/260, currently matches exactly). Today's CCC print (1031bps) is red either way, so no divergence manifested. Risk: a future SENTRY retune of `config.py` propagates automatically into `hy_oas_watch.py` (which imports it live) but **not** into `boot.py` (which hardcodes copies) — a silent fork between the two instruments that display the "same" HY OAS zone language.
- **Watcher-echo vs. live-dashboard juxtaposition.** In the same boot output, the live HY OAS dashboard row reads 🟢 263bps (today's FRED pull) while the "Unattended Watcher" echo two sections below reads 🟡 "yellow 267bps" (obs 2026-08-26, checked 2026-08-27). Both are correctly dated and labeled — this is DELIVERS as designed (`watcher_echo()`'s job is exactly to surface the last unattended state, `boot.py:446-461`) — but a reader skimming for the "HY OAS number" could land on either value without reconciling them; no in-script note ties the two rows together.
- Corroborated the `sofr_dispersion.py` KB-LIQ-106 fallback path is genuinely fail-loud: on an import/analysis exception it prints marker `⚪` with explicit text "dispersion instrument UNAVAILABLE... NOT graded; do not read the absence of a marker as calm" (`boot.py:213-216`) — this is the one place in the file that actively defends against PAT-106-class silent substitution, and it worked correctly today (dynamic import succeeded, normal path taken).

## 6. Read-cap table (files the boot sequence names for a whole-file Read)

| File | Size | Mandated by | Verdict |
|---|---|---|---|
| `STATUS.md` | 119,776 B | Step 1, unconditional, explicit "Read" | **OVER-CAP** (2.21×) |
| `MEMORY.md` | 62,930 B (296 lines) | Step 1 rider, cold-boot only, names a sub-section ("NEXT SESSION," `MEMORY.md:273`) not the file | **OVER-CAP if read whole** — CANNOT-JUDGE whether whole-file read is actually mandated |
| `CALENDAR.md` | 28,899 B | Step 1 rider, cold-boot only | Under near-cap floor (32,550 B) — clean |
| `workbook/KB.tsv` | 192,836 B | Not a CLAUDE.md-mandated agent Read — consumed only programmatically inside `boot.py --selftest` (`Path.read_text().splitlines()`), never named as a boot-step Read target | Out of scope for this leg (script-internal read, not harness Read tool) |
| `thesis/THESIS.md` | 20,698 B | Listed in FILES table only, not in SPAWN steps 0-6 | Out of scope, under cap regardless |

## 7. R1 leg

`scripts/corrections_boot_check.py` — **NOT invoked** anywhere under `AGENTS/LIQUID/` (`grep -rn` empty) and LIQUID is not named inside the script itself (`grep -n LIQUID scripts/corrections_boot_check.py` empty). Absence matches expectation (R1 is a DAEDALUS-specific closeout step, not fleet-wide per root CLAUDE.md).

## 8. What this audit could NOT see

- Whether `MEMORY.md`'s "NEXT SESSION" rider is actually read as a whole-file Read or a scoped grep in practice — that's a live-agent-behavior question, not something static text or a script trace settles.
- Runtime behavior of the `build_domestic()` silent-ERR gap (Finding #2) — today's live run had 0 fetch errors, so the SILENT path was never actually exercised; the finding rests on static code trace only, not observed output.
- Steps 2-6 as *behavior* (only the WALTER-inbox *substrate* was checked — directory state and `board_log.tsv` format, not a live agent actually performing the drain-and-log sequence this session).
- Whether `hy_oas_watch.py` (the systemd-timer companion script that WRITES `HY_OAS_STATE`/`watch.log`/`HY_OAS_ALERTS.log`) itself has any SILENT/SUBSTITUTED defects — out of scope per the task brief (boot.py and files a boot step invokes); it was only cross-checked as a liveness fact for the watcher_echo() step.
- Whether `config.py`'s SENTRY bands have in fact been retuned since `boot.py`'s inline copies were last hand-synced — only a snapshot comparison at today's values (currently matching for HY OAS, diverging for CCC OAS) was possible.
