# Gate C Increment 3 — bounded unattended windows (proposal)

**Prepared:** 2026-08-27 late night, by PROME (custodian/builder — NOT this increment's reviewer). **State: DRAFT — INERT.** Nothing in this document grants, activates, or relaxes anything. **Authorizing word to draft:** Will in-session 2026-08-27 ~23:1x, verbatim *"yes draft increment 3,"* on PROME's presentation of the middle relaxation (his question: *"Can we just turn this thing on and just keep an eye on it?"*).
**Gating chain, in order — each gate is a hard predecessor:** ① sitting-2 runs and its closeout packet reviews CLEAN (the evidence gate — the boundary has never written a live record before it) → ② the §3 hardening set BUILT and tested → ③ independent adversarial review of the widened surface (§4 — the prior review's conclusions do NOT carry) → ④ Will's activation ruling. **A defect at any gate returns the chain to that gate, not to argument.**

## 0. What this increment is, in one paragraph

Today the Kernel accepts work only inside a short operator-ruled window with **Will present throughout** ("attended"). Increment 3 replaces that with a **bounded multi-day window Will rules in one message** (proposed cap: **≤7 calendar days**, exact bounds his words, canonical form), inside which **PROME as custodian runs sittings unattended** and **commits a report packet to Will after each sitting**. Will's time drops to: one window ruling, reading reports, and ruling any stop. **Any stop condition freezes the entire window** — not just the sitting — until his word. This is deliberately NOT "always-on": windows stay bounded, revocation stays affirmative, and the increment after this one (standing window, watch-only) is proposed only if the measured burden of bounded windows still argues for it.

## 1. What changes

| Surface | Increment 2 (current) | Increment 3 (proposed) |
|---|---|---|
| Window | single sitting, ~30-60 min, Will attending | **≤7-day bounded window, Will-ruled in one message, Will attends nothing** |
| Sittings | one, operator-present | custodian-run, any number inside the window, each per the unchanged runbook steps |
| Reporting | closeout packet at sitting end | **report packet committed after EVERY sitting** (events accepted, receipts, refusals, suite state, burden row) — report-after under standing authorization replaces report-before for these mechanical steps only |
| Stop conditions | stop on screen, Will rules live | **stop FREEZES THE WINDOW** — no further sittings, machine-enforced (§3.4), until Will's word; a frozen window that expires stays frozen-closed |
| Will's presence | required throughout | not required; required only to rule stops |

## 2. What does NOT change — the invariants (restated so the review can attack the list)

Fail-closed refusals before any write · additions-only on `KERNEL/shadow/events/` + `KERNEL/audit/commands/` · exact-pathspec custodian commits, never directories · affirmative revocation at window close (N3 — closure is an act) · C1: every desk authors and commits its OWN byte-frozen files · proposer ≠ verifier, `_protected_verification` including the PROME prohibition · custodian authors no research and processes no records outside an active window · **CI never becomes an acceptance writer** (root canon, not tunable) · substitute-custodian rules unchanged · carve-out ④ scoped to ruled window bounds + custodian pause-doorbell (runbook §, encoded 8/27) · S1/S2 substitution conditions · P1 tripwire (no cross-desk forecasting this increment; close-timing re-review fires before any increment that widens it) · Will may revoke any window at any time with one word.

## 3. New machinery — ALL required before gate ④, none optional

1. **Narrowed read capability (RED N4, the root-cause fix):** read-only modes (`--check-views`, `--audit-additions`) stop minting write-capable stores at all — a read capability type, not a write capability restrained by call path.
2. **Lock guard:** `FixtureAcceptanceLock` refuses an unenforced grant (closes the RED-verified LOW-severity gap; `.rw/`-scoped but unattended operation removes the "someone is watching" mitigation).
3. **Destination-keyed view guard (RED's stronger form):** `write_views` requires a grant whenever `output_dir` resolves under a granted root — no caller can route around it by omitting a parameter.
4. **Stop-state persistence (new, the unattended keystone):** a durable window-state record (`KERNEL/` custody path) that any stop writes BEFORE surfacing; every subsequent sitting's preflight reads it and **refuses while a stop stands undispositioned**. A frozen state survives session death, machine switch, and window expiry. Fail-closed: unreadable/absent state where one is expected = frozen.
5. **Per-sitting report packet:** transcript auto-committed + a report to Will's queue surface after each sitting (events, receipts, refusals, post-sitting suite run, burden measures per the C8 pre-named set). A sitting whose report fails to commit is treated as a stop.
6. **Pin-vs-nudge disposition landed** (the 8/27g sweep item): ledger-hygiene tooling must know about Kernel-pinned rows before the pinned population grows across unattended sittings — whatever shape DAEDALUS's sweep proposes.

## 4. Why the prior review does NOT carry — stated so nobody leans on it

RED judged Findings 1-2 non-blocking **explicitly because the use was one attended single-apply**, and wrote: *"before any unattended or extended use of this interface: implement Finding 1's `window_enforced` guard [done], or N4's narrowed read capability [item 1 above]."* Unattended multi-apply is therefore a NEW review object, not an extension of a cleared one. The §3 build re-cuts the store/lock/render acceptance surface — the exact re-cut RED said should happen post-pilot **with its own review**. The reviewer must re-price every prior finding against: no operator watching, multiple applies per grant, longer-lived grants, and the stop path exercised without a human present.

## 5. Decision inputs at gate ④ (so the ruling is evidence-shaped)

- **Burden:** the C8 pre-named burden measures from sittings 1-2 (attended cost per event accepted) vs the projected Increment-3 cost. This is the number that justifies — or kills — the relaxation.
- **Boundary record:** stops fired vs stops mishandled across all attended sittings (to date: every stop pre-write, zero events lost, zero undispositioned).
- **Reviewer seat:** RED or DAEDALUS. ⚠️ Whoever holds a PARTICIPANT role inside Increment-3 windows (RED is standing resolution verifier) should not also review the increment — same principle as the 8/27 amendment routing; name the seat at commissioning.

## 6. Rollback — pre-registered, so reverting is mechanical not argumentative

Any of: an integrity-check failure (`EXCEPTION`/`UNKNOWN`/additions-only violation) · a stop dispositioned by anyone but Will · a report packet materially wrong · a defect reaching Will unrepaired past one weekly spine audit ⇒ **current window revoked affirmatively, mode reverts to attended sittings, and re-widening requires a FRESH gate-③ review** — not a resumed one. The revert is one custodian commit and loses nothing: the ledger is additions-only either way.

## 7. Perimeter

Command families, grants, actors, desks: **unchanged from Increment 2 as amended** (incl. `question.close_own` scoped, P1 standing). New desks or families are separate proposals. This increment changes WHO WATCHES, not what the machine may do.

— PROME, drafter. Reviewer verdict and Will's ruling are the only words that make any of this live.
