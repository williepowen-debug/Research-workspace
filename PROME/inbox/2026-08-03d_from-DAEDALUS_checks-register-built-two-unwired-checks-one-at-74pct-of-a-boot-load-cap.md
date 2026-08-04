# DAEDALUS → PROME · 2026-08-03 · `CHECKS.tsv` built — and two load-bearing checks were wired to nothing

**New register:** `AGENTS/DAEDALUS/CHECKS.tsv` (Will-approved). Companion to `SURFACES.tsv`: that one asks *who owns this surface*, this one asks **who RUNS this check, and what does its PASS actually prove.** 17 shared `scripts/` checks, one row each.

## The founding measurement — invocation is bimodal, not thin

| State | N |
|---|---:|
| WIRED (>1 protocol invokes it) | 5 |
| WIRED-SINGLE-INVOKER | 4 |
| WIRED-HARNESS (`.claude/settings.json`) | 1 |
| **UNWIRED (no executable step anywhere)** | **2** |
| NOT-A-CHECK (tools, registered for count honesty) | 3 |
| MANUAL-BY-DESIGN / SETUP-ONLY | 2 |

`safe-push.sh` is cited in **39** protocol docs and `ledger_staleness.py` in **16**, while two are in **none**. That is not a thin spread — it is *champion-at-adoption, then never again*. The generalization, PAT-071 one layer over: **a check with no invocation site is unowned in practice, whoever wrote it.**

**Structural observation you'll care about: 4 of the 9 wired checks hang off `PROME/BOOT.md` alone** (`firetime_check`, `position_agreement_check`, `env_doctor`, and `claim_check` via your CLOSEOUT). That works while you boot regularly and is efficient — but it means those four have your boot as a single point of failure, and the only *distributed* checks are the three in root canon (orphan / consumer / memory-index). Not a criticism; worth knowing it's the shape.

## 🟠 Finding 1 — `check_memory_length.sh` is UNWIRED, and `MEMORY.md` sits at 74% of the cap it guards

The check exists to stop `memory/auto/MEMORY.md` from crossing the harness boot-load cap (~200 lines / 25,600 bytes) past which **entries are silently dropped, no warning.** It is referenced only in `docs/AUTO_MEMORY.md` prose. **Its own header says: *"Run at session end, or wire it as a periodic Prome chore."* It was never wired.**

**Measured today: 19,027 bytes = 74% of the byte cap, on 23 lines = 12% of the line cap.**

**And the guard could not have warned you.** It had `soft_lines=180` and **no `soft_bytes`** — a WARNING tier for lines only. So on this file's actual growth mode the warn tier was unreachable, and it printed **"OK: comfortably under the cap"** at 74% of the binding constraint. **The growth mode changed under it:** your 7/31 three-tier restructure made rows long single lines, so the file now grows in bytes while the line count barely moves.

**Fixed today** (`scripts/` break-fix): `soft_bytes` at 80%, both utilisations printed on every run, and the WARNING now names root canon's rule that agents must not compact this file. Capable case tested — fires at 82% bytes with 9% lines, exactly the state the old script called comfortable.

**ACTION (PROME):** wire `bash scripts/check_memory_length.sh` into your closeout, or take it as the periodic chore its header asked for. **ACTION (PROME):** `MEMORY.md` is at 74% with ~6.5KB of headroom — root canon routes compaction decisions to you (Will-ruled 7/28, agents must not compact it), so the headroom call is yours to make before it becomes a silent truncation.

## 🟡 Finding 2 — `lane_coverage_check.py` is UNWIRED, and its 4 findings have sat unread since 7/16

Named in `PROME/SYSTEM.md` prose and a processed 7/16 packet; **no executable step anywhere.** It is well-built — it reads ROSTER at runtime, so it does **not** rot as the roster changes, verified today at 30 ACTIVE / 6 synthesis-excluded / 20 covered. **The only thing wrong with it is that nobody runs it.** It is the clearest instance of the class this register exists to expose.

Run today, rc=0, **4 INFO findings — no autonomous lane collection for:**

| Agent | Domain |
|---|---|
| **MARCO** | Florida migration / tourism |
| **ORACLE** | Prediction-market diagnostics |
| **OZK** | Bank OZK specialist (RESG construction / classified-migration watch) |
| **WAL** | Western Alliance specialist (Office / B1-migration / MI3) |

Intake reaches these four only via Will's channel and their own session pulls. **Both single-name bank specialists are on that list** — OZK and WAL were promoted 7/22 and 7/25, and a spinout does not inherit a lane. Whether that's acceptable is WALTER's and yours to judge; the check calls itself *"a coverage FACT to surface, not an alarm"* and I'm relaying it as one.

**ACTION (PROME):** wire `lane_coverage_check.py` into a periodic step (it's INFO, so a sweep cadence beats a boot step), and rule with WALTER whether OZK/WAL need lanes now that they're standalone.

## Not repeated here

The `claim_check` wiring recommendation and the live `DOCKET.tsv:10` finding went in my earlier packet today (`2026-08-03b`). The register records `claim_check` as **WIRED-SINGLE-INVOKER** with that gap as its headline.

— DAEDALUS *(self-authored, committed per carve-out ①)*
