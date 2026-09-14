# TERRY STATUS — CAPABILITY INVENTORY, ROTATED 2026-09-14

> **FROZEN — not maintained; `AGENTS/TERRY/STATUS.md` is canonical. Do not cite rows here as current.**
>
> **Rotated 2026-09-14 by TERRY at closeout.** Cut = the `## Capability inventory` section **verbatim**, **4610 B**, **crc32 `9fd5b8e4`** (section text only, trailing newlines stripped).
>
> **This is a HOT/COLD SPLIT, not a plain rotation** — the read-cap canon allows either, owner's choice of HOW. **The section was self-declared historical in its own heading** (*"historical descriptions; current position state is above"*) and every tool's LIVE spec lives in `CLAUDE.md` § KEY FILES, which is the surface a session actually travels.
>
> 🔴 **TWO ITEMS WERE **NOT** ROTATED — they are LIVE CANON and `STATUS.md` is their ONLY home** (checked: `grep` finds `1R ≡ $250` in neither `RISK_SCORING.md` nor `RISK_RULES.md`). **They were promoted INTO the retained text before this cut:**
> 1. **Standing rules (Will 2026-06-26):** fresh capital deploys ONLY on a fired trigger (no mechanical reshape; dry powder) · **max loss `$500` per card.**
> 2. **Risk unit (Will-ratified 2026-08-04): DOLLARS — `1R ≡ $250`, hard cap `2R = $500` per idea.**
>
> ⛔ **Had those two been cut, this would have been rotating LIVE STATE to hit a number, which the size-cap rule forbids by name.**
>
> **Why now:** this session's closeout write took `STATUS.md` **3,021 B over** the 32,550 B fleet READ-CAP, and the 9/14 block is the only session block left — 9/11 and 9/10 were already rotated today. **A current-state block cannot be rotated, so the cut had to come from declared history.**

---

## Capability inventory — historical descriptions; current position state is above

**Standing rules (Will 2026-06-26):** fresh capital deploys ONLY on a fired trigger (no mechanical reshape; dry powder). **Max loss = $500 per card.**

| Capability | State | Note |
|---|---|---|
| Trigger→card toolchain | 🟢 BUILT & TESTED | the minutes-not-hours path is live end-to-end |
| `scripts/chain_fetch.py` | 🟢 built, selftest PASS, live-validated | live option-chain CLI; marks matched the bank-put proposal exactly |
| `scripts/grade_print.py` + `grade_config.json` | 🟢 built, selftest PASS | Q2 print grader; 3 mis-grade traps as hard guards; `--tally` rolls path (a)/(b)/(c) |
| Fire cards | 🟢 **2 FIRED LIVE — 1 still open (004), 1 CLOSED with realized P/L (VIXCS: +7/27 → −7/30, −$111.60 / −38.8%)** + 3 staged | `TRADE_CARD_TEMPLATE_FIRE.md` + 4 fire cards (HY≥280 / WAL-EGBN / monoline COF-SYF-ALLY / **duration-TLT = 004, FIRED 7/20 @ $0.11, $330**); $500 budget: **$330 committed / ~$170 dry** · side-by-side: `setups/FIRE_CARDS_LADDER.md`. **TRY-FIRE-005 (FXY) dead 7/10 on DENY** — not in the live ladder. 006 (Kharg, $200 fence) ARMABLE, unfired |
| Day-trading review loop | 🟢 live · **SIDE tool** | dry-powder feeder, **subordinate to the thesis system** (Will 6/27) — must not displace the core work. S3 6/24–26 **−$3,969** (wiped S2; cumulative −$1,017) = funding nothing; plug the leak, keep it small. `daytrading/` |
| `SIGNALS.tsv` context ledger | 🟢 NEW, live | trade-construction context (WALTER INFO / my chart obs / thesis-owner timing); decay-tracked, boot-surfaced. **NEXUS regime PIN = 🟢 FRESH (7/16 anchor, re-stamped 7/17).** WALTER rows still decaying (4 of 6 >21d) |
| `inbox/WILL/` drop zone | 🟢 NEW, live | Will's reserved trading-data drop; raw gitignored (stays local), boot-surfaced; feeds the day-trading review |
| Desk dashboard (artifact) | 🟢 **v2 built 7/20, refresh ON REQUEST only** | `https://claude.ai/code/artifact/88c56079-77bf-4e10-ac45-9efac4da7f4e` — **3 tabs** (Cards / Shadow Book / Positions) + NEEDS-WILL strip + desk lede + all-cards catalyst calendar + shared-falsifier map + 004 payoff-ladder/DTE/disarm-cushion + distance-to-trigger bars. **Positions FORGE-SOURCED** via `scripts/positions_from_forge.py` (parses `FORGE/STATUS.md`, no re-keying). **Will 7/20: refresh on request, NOT every session — do NOT auto-regen at closeout;** natural next refresh = post WAL 7/21 print + REGINALD confirm. Source `scratchpad/terry_desk_dashboard.html` (session-local); republish same file → same URL, from a new session pass `url=<above>`. Full detail → `[[reference_terry_desk_dashboard]]`. |
| `scripts/ledger_sweep.py` | 🟢 **NEW 2026-07-30, selftest PASS + regression-tested on real historical card text** | **Anti-drift guard.** **C** card-header-vs-own-body · **A** state agreement across card/`SETUPS.tsv`/`INDEX.md`/`TRADE_BOOK.md` · **B** superseded-value drift off the git diff. **Advisory at boot (inside `boot.py`), BLOCKING at closeout (exit 1)** — *detection was never the gap, invocation was.* Matches on the **KEY**, never a bare number. **Found 4 live defects on first run, 2 unknown to me.** ⚠️ Never silence a finding by widening `COMPATIBLE`. **Known gap:** check B sees struck *values*, so a fixed defect still *narrated* as unfixed is NOT caught — STATUS write-back is the only cover. |
| Older scripts | 🟢 selftested | boot.py (**TSV reader hardened 7/30 — it had been keying `SIGNALS.tsv` off the banner line, printing "active rows: 0 of 15" with no regime PIN all day; now 4 active, and a zero-parse is a loud error, never a quiet ledger**), snapshot.py, risk_calc.py, chain_parse.py, csv_pnl.py |
| Live thesis trade cards | 🟠 **1 open (004)** | **POSTMORTEMS now has 2 entries** — TRY-FIRE-005 (PROCESS: correct DENY, 7-day logging lag; no trade, no P&L) + **TRY-VIOLET-VIXCS (the FIRST with a realized P/L: −$111.60 / −38.8%, tagged `BAD_STRUCTURE` primary + `GOOD_LOSS_PROCESS_WORKED` secondary; outcome-dependent legs PENDING 8/5)** |
| Position truth | 🟡 from Will/FORGE only | existing book in FORGE/STATUS; pull live before any fire-card sizing |
| Risk unit for Will | 🟢 **RESOLVED 2026-08-04 (Will-ratified)** | **DOLLARS: `1R ≡ $250`, hard cap `2R = $500` per idea.** ONE canonical surface: `daytrading/PROFILE.md` § risk unit (line ~76) — this row and the MEMORY Standing-Decisions line point there and restate nothing else. *(Row read "🟡 open" for 29 days after the ratification — DAEDALUS PR#5 9/1 caught it; closed 9/2.)* |
