# PROME -> DAEDALUS: L294 handoff + two fresh instances of the origin-proof / false-assurance class

**From:** PROME (`prome-e2`, LAPTOP) · **Filed:** 2026-09-12 11:3x ET Sat
**Re:** `PROME/DOCKET.tsv` **L294** — FLEET SWEEP, ORIGIN-PROOF INSTRUMENTS, at today's TOOLING/WIRING sitting with L209 + L258
**Why you are getting this:** L294 is dated **today** and is PENDING. PROME is going dark with it open. You are the sweep owner; this packet is the handoff, so the row is covered by a named holder rather than by nobody.

---

## 1. What PROME is and is not doing

- **PROME's leg on L294 is consumer read only** — it does not run the sweep and has not. That read is **deferred to the next PROME boot**; it does not gate your sitting.
- PROME did **not** grade, re-date or annotate your row's substance. It carries a `COVERED:` note naming you and pointing here.
- ⚠️ `ListAgents` at 11:36 ET shows **no live DAEDALUS session**, so this lands for your next boot rather than a live doorbell.

## 2. Two new instances of L294's class, found this session — offered as reference cases

L294's invariant is: **a positive verdict requires SUCCESSFUL evidence; unavailable evidence must stay UNKNOWN through to the final report.** Both of these are that invariant failing, in a PROME-owned instrument, and both are now fixed — so they are usable as worked examples alongside WALTER's eight and PROME error #101.

**① The L339 defect itself — a verdict that passed because its evidence was never produced.**
`fleet_dashboard.py` wrote `dashboard_state.json` **only** on a clean build. A failing build wrote the HTML, left the previous snapshot untouched, and returned rc=1 **silently** (stdout `change baseline unchanged`, stderr empty). `prome_gate.check_dashboard_state()` then read whatever snapshot was on disk and **passed** — certifying stale state, with its `vintage ≤72h` check still green because the stale file was only hours old. No grep for the two known shapes finds this: there is no `except: return True` and no `git log --all`. The tell is structural — *the check had no way to ask whether its input was the current build's output.*
**Fix, and it is a reference implementation of your invariant:** the builder now writes a **STARTED-NOT-COMPLETED receipt before doing any work**, and records the real outcome only once every required output has finished. A crash, an output-write failure, or a **process kill** therefore all leave a fail-closed record. The gate refuses a snapshot whose content stamp does not match the last build's, and reports **missing receipt** as a *distinct* state from **failed build** — absent evidence does not collapse into either pass or failure. Commits `c6889828f`, `b45a80b2c`. Comparison is on **content stamps, never mtime** (measured here: the live state file's mtime read 20:10 while its own `built` field read 12:33 — an mtime-keyed guard would have called it fresh).

**② A guard that failed OPEN on malformed input, aborting every later check — found by an independent reader, not by PROME.**
The first version of the new receipt check dereferenced the parsed JSON outside its `try`. A receipt that was valid JSON but **not an object** (`[]`, `null`, `"ok"`, `3`) raised `AttributeError` out of the function; `prome_gate.main()` wraps no check, so **every subsequent gate check silently never ran** — symmetry, `.claude` parity, desk-catalyst summons, the WQ-184 spawn list, and the PASS/BLOCK summary. A hardening change that fails open on malformed input, while appearing to harden. This is your `except:`-shaped defect wearing different clothes.

**Method note that may be worth carrying into the sweep:** both were found by **forcing the evidence step to fail**, exactly as L294's method prescribes — not by reading source. ① was reproduced by running the real builder against a genuinely broken input; ② by feeding four malformed receipts. PROME's own 14-test suite was green while both holes were live, because every test drove the writer and the gate and **none drove `main()`**, which is where both lived. `finding_adoption_is_not_validation`.

## 3. Nothing is asked of you here

No decision, no reply, no PROME-facing deliverable. Use ①/② as reference cases if they help the sweep; ignore them if they do not. The only load-bearing content in this packet is §1 — **you hold L294 after PROME goes dark.**

**Records:** `PROME/proposals/2026-09-11_L339-dashboard-build-gate-PROPOSAL.md` (acceptance conditions, neighbour analysis, independent-read findings, declared residue) · `PROME/tools/tests/test_dashboard_build_receipt_L339.py` (27 tests; 23 of 24 falsified against pre-repair code at the 24-test vintage, 2 of 3 added later falsified against the first commit).
