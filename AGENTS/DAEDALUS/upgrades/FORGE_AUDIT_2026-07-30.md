# FORGE — Full Architecture Audit

> 🗄 **DATED AUDIT/WORK RECORD (last content 2026-07-30; bannered 2026-08-17, self-audit F5).** Findings were routed at write time; this doc is history, not a live queue. Closure state of individual findings lives with the owning agents.

**Date:** 2026-07-30 (Thu, ~11:40 AM ET) · **Auditor:** DAEDALUS (Will-directed) · **Method:** solo read (no fan-out per session rules) — full file inventory, repo-wide reference graph, live tool execution (PAT-070), parser run against the 2-hour-old restructure
**Scope:** `FORGE/` — 204 tracked files (696 on disk incl. gitignored cache), plus every live doc that references it
**Read-only.** Nothing in FORGE or any agent dir was modified. All fixes below are proposals.

---

## VERDICT

**FORGE is three different things wearing one directory, and none of them has an owner.**

| Layer | State | Files |
|---|---|---|
| **① Position mirror** (`STATUS.md`) | 🟢 **Live and well-made** — today's reconcile is the best one on record. But **machine-parsed, restructured 2h ago, and the parser mis-reads it while reporting clean** | 1 |
| **② Toolchain** (`tools/market-data/`) | 🟡 **Live and used constantly** — `dashboard.py` correct; `fetch.py price` returns a **plausible wrong number** for one symbol and errors on all index symbols | 10 |
| **③ Research corpus + dead tools** (`research/ timing/ signals/ education/ trigger-sets/ news-sweep/ filing-watch/ auction-data/`) | 🔴 **Silent-rot middle** — 160 files, 2–4 months cold, **no FROZEN banners**, and root `CLAUDE.md` advertises one of them as a live Key Directory | 160 |

The defect mass is **not sloppiness** — layer ① is exemplary work. It is **absence of an owner**: every other file class in this repo has an accountable agent; FORGE has "whoever passes through, with Will's OK." Findings S1–S2 are the disease; everything else is a symptom.

---

## STRUCTURAL

### S1 — FORGE has no owner 🔴

`FORGE/STATUS.md` is the **single most-referenced path in the repository (499 references)**. `fetch.py` is second (445). Root `CLAUDE.md` §Git Protocol tells every agent to *flag* shared files to PROME rather than commit them; PROME commits FORGE "with Will's OK first." So FORGE is **written by many, owned by none.**

Consequences observable today: no boot step reads it for hygiene, no closeout sweeps it, no agent's STATUS is graded on it, and no one walked its mirrors when it changed this morning (H2). The 7/20→7/30 gap between reconciles was 10 days with no mechanism that would have noticed an 11th.

### S2 — FORGE is outside every fleet enforcer, including mine 🔴

`scripts/ledger_staleness.py` is hard-scoped to `AGENTS/`:

```
:170   cand = os.path.join(REPO, "AGENTS", arg)
:257   for p in glob.glob(os.path.join(REPO, "AGENTS", "*", anchor))
```

`--trade --all` **structurally cannot reach `FORGE/STATUS.md`.** The enforcer was extended to trade surfaces in the first place (PAT-035a, 7/4) precisely because those are what get cited into a position — and the surface that gets cited into positions *more than any other file in the repo* is the one it cannot see.

Same blind spot on my side: FORGE has **no `FLEET_MAP` row, no maturity grade, and is in none of my 5 registered sweeps** — my map globs `AGENTS/*` too. This is PAT-050 turned inward again, the identical shape that left the coordinator structurally invisible until 7/28.

### S3 — The position mirror's parser silently mis-reads this morning's restructure 🔴

`AGENTS/TERRY/scripts/positions_from_forge.py` parses `FORGE/STATUS.md` into TERRY's desk-dashboard Positions tab. Its own docstring: *"fail LOUD, never fabricate… A row it cannot parse is reported in a WARNINGS block, not silently dropped."*

Run against the file as it stands right now, it prints:

> **`Parsed 28 rows.` / `No parse warnings — all position rows mapped.`**

while emitting:

| Defect | Evidence (verbatim from `--json`) | Why it matters |
|---|---|---|
| **Phantom live position for the CLOSED trade** | `{"group":"Fidelity","ticker":"","instrument":"Aug-05-2026","expiry_iso":"2026-08-05","dte":6,"qty":"~~4~~","cost":0.7,"mark":null,"value":null}` | The VIXCS spread **closed at 09:50 today**. It renders as an **open Fidelity position with a 6-day clock** and no ticker. Wrong in the dangerous direction |
| **`mark: null` on every Longs row** | AAPL · GLD · USO · APD · TBT · XLE all `mark=null` | The new table header is `Mark 7/30`; the parser keys on `Mark`. **Silent blank, not error** |
| **Two more ticker-less rows** | `"instrument":"7/20 EXPIRED"` dte=−10 · `"instrument":"7/22 — EXPIRED 8 DAYS AGO"` dte=−8 | Expired Robinhood legs parsed as positions |
| **`qty` is a string on all 28 rows** | `"**15**"`, `"**13**"`, `"**35**"`, `"**30**"`, `"~~4~~"`, `"3 (M)"`, `"~1"` | Markdown bold/strikethrough not stripped. Any downstream arithmetic breaks or coerces wrong |

This is **PAT-069 verbatim, eight days after the HEARTBEAT/`fleet_dashboard.py` instance**: a parsed document's format is an interface, a re-base is a breaking change, and the break is silent-blank rather than loud. The emphasis-markers are new — the 7/30 pass added `**bold**` to exactly the changed quantities, which is good prose and a format break.

**Not yet fired:** TERRY's dashboard is refresh-on-request (Will 7/20: do not auto-regen), so nothing wrong has been published. The window is open, not closed. The next refresh publishes a closed trade as live.

---

## HIGH

### H1 — `fetch.py price` answers with the wrong instrument for MOVE 🔴

Run live 2026-07-30 ~11:35 ET from `FORGE/tools/market-data/`:

| Command | Result | Truth |
|---|---|---|
| `fetch.py price MOVE` | **`$11.50 +6.44%`** | **MOVE index = 74.18** (`dashboard.py`, same minute) |
| `fetch.py price VIX` / `OVX` / `SPX` | `ERROR float() argument must be a str` | — |
| `fetch.py price SKEW` / `VIX3M` | `ERROR 'currentTradingPeriod'` | — |
| `fetch.py price ^MOVE` / `^VIX` / `^SKEW` | `74.18` / `18.84` / `139.55` ✅ | correct |
| `fetch.py price KRE` / `TLT` | `$75.95` / `$82.63` ✅ | correct |

`config.py:347` already maps MOVE → `^MOVE`, which is why `dashboard.py` is right. `cmd_price` passes its argument to yfinance **unmapped**, so bare `MOVE` resolves to an unrelated equity.

The index errors are **loud and therefore safe**. `MOVE` is the one that isn't: it returns a real-looking number for a different asset. `fetch.py` is referenced 445× and is named as *the* live-price CLI in both root `CLAUDE.md:63` and `PROME/BOOT.md:73`.

**Grade honestly — latent, not fired.** No live doc currently invokes the bare form for MOVE; every live invocation I found uses equities/ETFs (KRE, USO, WAL, FXY, OZK, MFIC). But it is a trap laid across today's work: **PROME/SCRATCH item 7 assigns VIOLET "MOVE 7/30 — re-cross >76 un-breaks confirm-3 → KB-VIO-144 re-grade."** A 76 threshold, and the fleet's default price tool answers 11.50 to that symbol name.

*Fix:* route `cmd_price` through `config.py`'s existing symbol map, or fail loud when a bare symbol resolves to a different asset class than the caller's series registry expects. Owner = whoever owns FORGE (S1).

### H2 — Two always-loaded docs carry the wrong reconcile date, as of this morning 🟠

| Surface | Says | Truth |
|---|---|---|
| root `CLAUDE.md:30` | "broker-export refreshed — **last reconcile 2026-07-20**" | 2026-07-30 ~09:40 |
| `PROME/SYSTEM.md:166` | "last reconciled **2026-07-20** (broker export; prior 7/16)" | 2026-07-30 ~09:40 |

Root `CLAUDE.md` loads into **every agent session in the fleet**. Right now every agent boots believing the position mirror is 10 days stale when it is 2 hours old.

**PAT-068, third instance in eight days** — a canon change that didn't walk its mirror map. The drift direction here is *conservative* (agents distrust a good surface rather than trust a bad one), which is the less dangerous half of PAT-062, but the mechanism is identical and the fix is one line each.

### ~~H3 — `dashboard.py`'s As-of column is blank on every row~~ ❌ **RETRACTED 2026-07-30 ~13:10 — WRONG AS WRITTEN**

**The claim was false and the error was mine.** PROME challenged it with evidence the same afternoon; I re-ran the tool over its *full* output and PROME is right.

Tier 1 stamps **every** FRED/EIA row:

```
HY OAS 287bps [7/29] · CCC OAS 1013bps [7/29] · Gas 4.10 [7/27] · Init Claims 197,000 [7/25]
Cont Claims 1,782,000 [7/18] · SOFR 3.65 [7/29] · 10Y 4.61 [7/28] · Cushing 18.60 [7/24]
```

Blanks appear only on **live-price rows** (Brent, USD/JPY, and all of Tier 2), which `_date_stamp()`'s docstring declares intentional — those are intraday-live, not dated series.

**Root cause of my error:** I ran `dashboard.py | tail -25`, which captured only the Tier-2 position-monitoring table — all price rows, all legitimately blank — and asserted a whole-file property from that slice. A sampling error, and precisely the discipline my own **PAT-038** exists to enforce (*trust missing-labeled-handle flags; RE-VERIFY, never propagate, missing-substance claims*) plus `[[finding_comprehensive_grep_over_sampling]]`. I had the tool in my hand and read a fraction of its output.

**Residual, real but cosmetic** (carried to the item-2 batch, PROME's framing adopted): a live-price row prints an *empty* As-of where it could print `live`. Blank reads as *unknown vintage*; `live` would say what it means. Small, and genuinely a nicety — not the finding I filed.

*Kept in place rather than deleted: a retracted finding is evidence about the auditor, and PAT-070 was banked off a similar own-miss two days earlier.*

---

## MEDIUM

| # | Finding | Detail |
|---|---|---|
| **M1** | **The position surface's own history pointer dangles** | `FORGE/STATUS.md:143` → `` `JOURNAL.md` `` — file is at `_archive/JOURNAL.md`. `PORTFOLIO.md:3` dangles identically. Two dead pointers inside the position surface |
| **M2** | **Asymmetric tombstoning of dead tools** | `news-sweep` is *exemplary*: WALTER `CLAUDE.md:67` strikes step 7c with dates, successor, and a doctor backstop; `PROME/SYSTEM.md:161` says "local cron is dead." But **`SYSTEM.md:162` presents `FORGE/tools/filing-watch/` as "Useful for Qs/10-Q catalysts and Call Reports"** with no caveat — its data is 2026-05-07 vintage (84d) and RESEARCH-INTAKE's `edgar_8k` feed superseded it. Same death, one tombstone, one live recommendation. **`FORGE/tools/auction-data/`** (2026-05-05) is referenced by **nothing at all** — pure orphan, superseded by the lane's Treasury feed |
| **M3** | **Three cron scripts, no crontab** | `crontab -l` → *"no crontab for willi"*. `cron_dashboard.sh`, `cron_sweep.sh`, `morning_briefing.sh` are VPS-era leftovers (OpenClaw cut 6/26). `cron_sweep.sh` additionally sources `FORGE/tools/news-sweep/.env`, **which does not exist** (only `.env.example`). PAT-040 wire-or-retire |
| **M4** | **160 files of research corpus in the silent-rot middle** | `research/` (last commit 04-06, 51f) · `signals/` (05-16, 30f) · `timing/` (07-01, 60f) · `education/` (04-05, 1f) · `trigger-sets/` (06-08, 1f) — **zero FROZEN banners**, and root `CLAUDE.md`'s Key Directories table advertises **`FORGE/timing/`** as a live resource. Root Data Hygiene's two-state rule is FROZEN-with-banner **or** LIVE-with-alert, never the middle. Most *are* cited by a live doc so the strict >60d retirement rule doesn't fire — which is exactly why they need **banners** rather than archival. `education/` (1 file, **zero** live referrers) is a clean retire |
| **M5** | **`PORTFOLIO.md`'s banner word is outside the enforcer's vocabulary** | It reads "**SUPERSEDED** 2026-05-21". The PAT-035b recognizer set is `FROZEN\|RETIRED\|NOT CURRENT\|DO NOT CITE\|NOT MAINTAINED\|ARCHIVED`. Moot while FORGE is unscanned — but it would **false-flag as live** the moment S2 is fixed. One word, fix it with S2 |

---

## CLEAN — verified, not assumed

- **Secret hygiene holds.** `FORGE/tools/market-data/.env` is **not tracked** (`git ls-files` → no match). `.cache/` (519 files), `__pycache__/`, `logs/market_data.log` (280KB) all correctly gitignored. The public-prep cleanup held.
- **Dangling references are otherwise confined to history.** `ACTIVE_TRADES.md`, `CF-trade-thesis.md`, `WATCHLIST.md`, `oil-shock-position-timing.md`, the `KRE/ OZK/ WAL/` per-trade folders — all archived, all cited **only from other archived docs** (`PROME/archive/`, `memory/`, BRENT's research corpus). Harmless.
- **`FORGE/PREDICTION_DISCIPLINE.md`** is a *forward* reference in `scripts/firetime_allowlist.tsv:41`, created by the approved 8/3 memory migration and allowlisted as "benign until then." Correct practice — the model for how a not-yet-existing path should be handled.
- **`dashboard.py` works and is honest** — rc=0, live values, zone-change deltas surfaced.
- **The 7/30 reconcile itself is the standard.** Arithmetic verified to the cent ($18,527.27 + $20,549.75 + $1,500.00 = $40,577.02). Single-account limitation bannered at line 5 *before* any table. Ten discrepancies ranked by decision urgency. Every unresolved item labeled **hypothesis**, none resolved by invention. D-9 verified benign rather than waved off. This is what the rest of FORGE should look like.

---

## PROPOSAL

**What.** Give FORGE an owner and split its three layers.

| | Proposal | Why |
|---|---|---|
| **1. Owner** | Name an accountable owner for FORGE. **Recommend PROME** — it already transcribes the export, already commits the directory, and S1's symptoms are all coordination-layer failures. TERRY is the alternative (owns trade construction and the only parser) but doesn't own the tools or the corpus | Every finding above traces to S1 |
| **2. Extend the enforcer** | Teach `ledger_staleness.py` a non-`AGENTS/` path mode; register `FORGE/STATUS.md` under `--trade`. Add "SUPERSEDED" to the banner vocabulary in the same patch (M5), and fleet-diff-validate before shipping (PAT-059's lesson) | S2 + M5. Shared script → gated |
| **3. Fix the parser contract** | TERRY-lane: strip markdown emphasis from parsed cells; assert non-null `mark`/`ticker` and **fail loud** when either is empty; teach it the `Event boxes` section is a distinct class and skip `~~struck~~` rows. Add a consumers-note to `FORGE/STATUS.md`'s header so the next re-base knows it has a parser (PAT-069 fix-form) | S3. Route as a packet — TERRY committed at 11:02 today |
| **4. Map the index symbols** | Route `fetch.py cmd_price` through `config.py`'s existing symbol map | H1 — the only wrong-number defect found |
| **5. One-line mirror sweep** | Root `CLAUDE.md:30` + `PROME/SYSTEM.md:166` reconcile date 7/20 → 7/30; `FORGE/STATUS.md:143` + `PORTFOLIO.md:3` JOURNAL pointer → `_archive/JOURNAL.md` | H2 + M1. Root doc = Will-gated |
| **6. Banner the corpus, retire the orphans** | FROZEN banners on `research/ signals/ timing/ trigger-sets/`; `git mv` `education/` + `auction-data/` to `_archive/`; tombstone `filing-watch/` in `SYSTEM.md:162` the way `news-sweep` already is; delete or tombstone the three cron scripts | M2 + M3 + M4 |

**Effort.** Items 4/5 ≈ 20 min. Item 3 ≈ 1 TERRY session. Items 2/6 ≈ one gated batch. Item 1 = a Will decision, and it is the only one that stops this recurring.

**Expected value.** Item 3 prevents publishing a closed trade as a live position on the next dashboard refresh. Item 2 puts the repo's most-cited surface inside the rule that exists for it. Item 1 is the difference between fixing this list and fixing it again in September.

**First step.** Will names the owner (item 1). Everything else routes from there.

---

## PATTERN CANDIDATES

- **PAT-071 (proposed):** *A shared directory with no owning agent accumulates every defect class the fleet has mechanisms for, because every mechanism is scoped to the ownership unit.* FORGE: 204 files, the #1 and #2 most-referenced paths in the repo, invisible to `ledger_staleness.py`, `FLEET_MAP`, all 5 DAEDALUS sweeps, and every closeout protocol — all of which glob `AGENTS/*`. Evidence: S1+S2, and the same shape found at the coordinator on 7/28 (PROME structurally unscannable for the same globbing reason). Fix-form: **the ownership unit and the enforcement unit must be the same unit** — when a surface can't have an owning agent, an owner must be *assigned* and the enforcers taught the path explicitly. Sibling of PAT-050 (inward blindness) at the *directory* rather than the agent layer.
- **PAT-069 extension, n=3:** emphasis markers (`**bold**`, `~~strike~~`) added to a machine-parsed table are a format break. Prose-quality edits are interface changes. Instances: HEARTBEAT re-base → 3 `fleet_dashboard.py` parsers (7/28) · BOARD schema migration → `board_scan.py` (7/28) · FORGE reconcile → `positions_from_forge.py` (7/30). **A fail-loud parser that reports "no warnings" while emitting null marks and phantom rows is the strongest form of the lesson yet** — the guard was designed for this and did not fire (`[[finding_test_the_guard_not_just_the_guarded]]`).

---

*Read-only audit. No FORGE or agent file modified. Fix routing pending Will's disposition.*
