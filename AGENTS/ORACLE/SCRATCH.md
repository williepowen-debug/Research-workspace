# ORACLE — SCRATCH (canonical session handoff)

**Session arc:** 2026-09-04 (Fri), catch-up boot after **8 dark days (8/28–9/03)** — run **against a live event**: the 08:30 NFP print landed 3 minutes before the first `pull --log`. PROME doorbelled mid-session with a Tier-1 ask that became the main deliverable.
**Last updated:** 2026-09-04 ~09:1x ET · **Box:** **desktop** (DESKTOP-BC6EF81). Kalshi **signed** lane LIVE (`status` rc=0).

## ⚠️ CARRIED FRAMING — do not re-derive from older text

- **🔴 THREE DIFFERENT FED NUMBERS EXIST AND THE FLEET HAS ALREADY CONFUSED THEM TWICE.** Sept-**meeting** hike 52.5% PM / 57.0% Kalshi · by-**Oct** cumulative 62.5% · **2026 aggregate** 74.5%. **A cumulative contract read as meeting-specific ALWAYS reads too hawkish** (it prices "a hike *by* then", not "a hike *at* that meeting"). BOND's 65–68% was one; NEXUS's 71.5% (ruled 8/18, corrected 8/28) was the other. **Twice in three weeks = a pattern.** Always name the contract.
- **⚠️ KALSHI `KXFED-26SEP` IS A CUMULATIVE "Above X%" LADDER, NOT OUTCOME LEGS.** It must be **differenced** to become a distribution. `Above 3.50%` 99.0 / `Above 3.75%` 59.0 / `Above 4.00%` 2.0 ⇒ cut ~1.0 · hold 40.0 · hike-to-4.00 **57.0**. Quoting `59.0` as "P(hike)" is wrong by 2pp and quoting it as a Polymarket-comparable leg is a category error.
- **⚠️ CME FEDWATCH IS NOT FETCHABLE.** `WebFetch` times out at 60s — JS app shell, serves no numbers. **Do not promise a CME cross-check.** The 9/3 "CME ~74.5% 50bp cut" relay was falsified against Polymarket + Kalshi **only**; re-verification at CME is **WALTER's**, and I explicitly did not assert what CNBC published.
- **⚠️ `polymarket.py history` STAMPS TWO ROWS WITH TODAY'S DATE** (an intraday bar + the live point; 52 duplicated `(slug,date)` keys). Fine for trajectory, **wrong if you read the tail as today's close.** Found via an 11.5pp `history`-vs-`pull` disagreement where **both were right**.
- **⚠️ THE SEPT HORMUZ LADDER RE-BANDED 20-wide → 5-wide.** Never difference or chart it against August. **No guard can see this** — PINNED-BUT-NOT-FOUND and ⛔RESOLVED both pass clean on a re-banding.
- **⚠️ THE IRAN DAILY-TEMPO GAUGE LAGS BY UP TO 4 DAYS.** The 8/31 leg moved **+53.4pp on 9/04**. A low reading on a recent date means "not yet priced" at least as often as "nothing happened." **Cite the date the PRICE MOVED.**
- **⚠️ `tools/metrics.py collapse` SCORES ENTROPY DROPS ONLY.** Today's biggest move raised entropy and is unscored; the scan's top hits were two thin markets. **"Collapse scan clean" ≠ "nothing moved."**
- **The 0-ships `⛔RESOLVED` dashboard flag is STILL a FALSE POSITIVE — do not retire that market.** Row annotated DO-NOT-REPLACE; it will keep firing every session.
- **⛔ THREE PUBLISHED σ REMAIN RETRACTED** (KB-ORC-064 → `CORRECTED`). Every dH and entropy LEVEL reproduces; every σ was inflated, three of five unreachable at any window. **Directional findings stand.** Reproduce: `python3 tools/metrics.py verify`.
- **`kalshi.py` reports the LAST trade; cite the MID on wide books** (KB-ORC-069). Live hits today: Sept-U3 `>4.2%` (9¢ book, last 49.0 / **mid 41.5**) and corporate-bankruptcies (7¢, last 83.0 / **mid 86.5**). Display-only — **the logged series keeps its last-trade basis on purpose.**

## WHAT I DID

*(Commit hashes filled at closeout — see `git log --oneline -- AGENTS/ORACLE/` for this session's set.)*

1. **Adjudicated PROME's Tier-1 ask at the instrument** — the two contradictory relayed September-Fed numbers. **Both wrong, differently:** BOND's 65–68% is a cumulative/aggregate contract mislabeled as meeting-specific (`KL 0.061 bits`); the WALTER-relayed "50bp CUT ~74.5%" is **sign-inverted and ~74pp off both venues** (`KL 6.619 bits` — ~108× further). Full working with every timestamp and basis: `domain/sources/2026-09-04_sept-fomc-instrument-adjudication.md`.
2. **Dated the September FOMC crossover** from daily closes: no-change led through 8/28 (68.5 vs 30.5) → 8/29 **TIE at 49.5/49.5, +19pp in one day** → 8/31 **hike takes the lead** → held 5 straight sessions. Kalshi OI +80% since 8/21 = new money.
3. **NFP event study** — the measurement no other desk could take. `pull` landed 3 min after the print and caught it mid-move; pre/post reconstructed from CLOB hourly bars. **28pp of mass moved, `dH` only +0.008, `KL(post‖pre) = 0.0587 bits`.** Found that my own collapse detector is blind to that shape by construction.
4. **13 watchlist rolls** — the largest single session in this file's history; every dead row carried since 8/27 cleared, **both** PINNED-BUT-NOT-FOUND rows resolved.
5. **T6 ledger written** at PROME's ask (`t6_pin.py --write`) — 8 rows, **zero gaps**, reproducing PROME's independently-run table exactly. VX-ORC-10 **closed**.
6. **Answered my own 8/27 open hypothesis** on unresolved Iran-shipping legs — they all settled 0.0%, and the answer **demotes an instrument I have been routing since ~7/17.**
7. **All 10 VX rows re-pinned**; 4 KB rows (075–078); STATUS, NEXUS_BRIEF, MAINTENANCE rewritten.

## NEXT SESSION (dated, priority-flagged)

1. **🔴 ~2026-09-11 (Fri) — AUGUST CPI PRINTS.** **Kalshi is the instrument** (`KXCPIYOY-26AUG-T3.3` **60.0%**, 87.3K ct) — the Polymarket modal market is ⚠️thin at $1.8K. **This is the CPI that arms the FOMC five days later.** Take a pre/post read exactly as done for NFP today; the method is proven and the file shows it.
2. **🔴 2026-09-15/16 (Tue–Wed) — FOMC.** The whole Sept complex resolves. Hike is currently modal on both venues. **Pre-meeting pin the day before; post-decision read same-day.**
3. **🟠 2026-09-06 (Sun) — Hormuz weekly resolves.** Re-pin wk-of-9/7 **only once it has depth** ($40 total today — do not pin a $40 book). *(Literal-date gate; this roll has now run late five consecutive times, so treat the date as hard.)*
4. **🟠 Re-search a SEPTEMBER Iran-shipping on-date event** — none exists yet (3 query forms tried). The August pin is retained only because its 8/31 leg is the live signal.
5. **🟠 PROME's 8/17 PortWatch war-regime ask — NOW OWED A SIXTH SESSION.** Sweep KB rows for war-regime PortWatch counts used as evidence; tag `PORTWATCH-WAR-REGIME-SUSPECT` or clear. **The ~88/day pre-crisis denominator clears; war-regime counts do not.** *(Carried since 8/17. It is no longer "deferred", it is overdue — do this one before new research.)*
6. **🟠 TIER 2, agreed with Will, not started: prototype the spec-has-implementation check** and send to DAEDALUS. **Honest limit unchanged: it cannot catch "code exists but computes it wrong."**
7. **🟠 THE RE-OPENABLE CLASS (carried since 8/18, still untriaged):** conclusions resting on a pre-fix `kalshi.py search` zero, *only where load-bearing*. Named candidate: **"no standalone VIX market on Kalshi."**
8. **🟡 Decide the `polymarket.py history` dedupe** — the right fix is a **separate intraday accessor**, not a one-line dedupe, because the duplicate rows are what made today's pre/post reconstruction possible. Decide which consumer you are serving before touching it.
9. **🟡 NEXUS + RED owe the 71.5%→aggregate relabel** — NEXUS applied it 8/28; **RED's side is still open.** Given BOND repeated the same error class this week, this is worth one line to RED rather than pure tracking.
10. **⚪ `T6_PIN.tsv` is event-scoped and T6 is now GRADED** — **freeze it or drop it from `LEDGER_GLOB` next session.** Instruction is in the glob file. *(This was item 11 last session and did not get done; it is now unambiguous because the test is closed.)*
11. **⚪ Archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`** — mutual-reference pair, never ages into retirement eligibility.

## CARRY-FORWARD

- **Push state:** see closeout commit + `safe-push.sh` receipt line. Other agents (BOND, SAM, VIOLET) had **uncommitted changes outside my dir at boot**, so per root protocol I did **NOT pull**; `git log HEAD..origin/master` was empty, so nothing was missed.
- **Coverage sweep run 9/04 → next due ~2026-09-11.** 10 hits, **1 nomination pinned** (Fed no-change, $22.0M — the leg that *lost* the lead, which is exactly the blind spot `coverage` exists for: `movers` ranks by move size and would never have surfaced it).
- **Kalshi lane LIVE + SIGNED on the desktop. Record lane state PER-BOX, never as a fleet fact.**
- **`ledger_staleness` still counts HISTORY.tsv in "8 scanned" and prints no row for it** — PROME's tool; documented in the glob file, reported not patched.
- **Successor-spec note for DAEDALUS/BOND/LIQUID (from T6, do not lose):** a registered trigger should name **(a) close-vs-intraday**, **(b) the eligibility window explicitly** (T6's tool was built around the 8/21–8/28 *pin* window while the trigger stayed eligible from 8/10 — that mismatch walked PROME into measuring the wrong window), and **(c) one-sided vs two-sided**. T6 hard-closed on the single largest UP-day of its series (+17pp, intraday high 0.65) with a 42pp intraday range inside its own window; a one-sided `<25%` level test on that series carried little directional information. **This does not disturb the NO-VERDICT.**

## OPEN HYPOTHESES

- **Is "the Fed hikes and nothing breaks" a coherent crowd view or an unpriced contradiction?** Sept-hike 52.5%, no-cuts-2026 92.3%, **recession 7.0% on both venues and UNMOVED through a 28pp FOMC repricing.** ORACLE can measure the crowd's internal consistency but not adjudicate it — **RED owes the counter-number, stale 83 days.** This is now the sharpest standing divergence on the board.
- **Was the 8/27 complacency decoupling a regime change or a one-week dislocation?** — **now leans DISLOCATION but is NOT closed.** The best-asset S&P leg recovered +4.0pp (53.5 → 57.5), roughly a quarter of the 15pp break. VX-ORC-09 lowered 🔴→🟠 on that retrace. **The registered tell (gold retaking the lead) still has NOT fired.**
- **~~Why do past-dated Iran-shipping legs sit unresolved 10+ days?~~ ANSWERED 9/04 and it demotes the gauge.** All three flagged legs settled 0.0%; the ladder prices events **up to 4 days late**. Consequence: any war-tempo read taken off my forward curve since ~7/17 should be re-read with that lag.
- **Does the Sept ladder's ~84%-below-10-transits/day survive contact with physical throughput?** ORACLE owns the crowd read only — and the PortWatch war-regime impeachment (item 5) is exactly the check that would answer it.
- **Was the 9/1→9/3 dovish wobble (Kalshi 0.62 → 0.45) news or positioning?** NFP reversed it (+8 to 0.53) but the two-day −17pp move has no identified driver in my data.
