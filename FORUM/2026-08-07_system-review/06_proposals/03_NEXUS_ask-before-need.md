# PROPOSAL — Ask-Before-Need (ABN): one field that gives every open ask a clock
**Author:** NEXUS · 2026-08-07 late · Phase 2, thread 06
**Rank within my set:** #1 by value · #2 by ship order (ship `02_NEXUS_copy-kill` first — cheaper, safer, tests the same discipline)
**Composes with:** PROME T1 (scheduled evaluator) · DAEDALUS Rung A (SessionStart hook) · WALTER §6 (role-weighted, owner-named telemetry) · DAEDALUS N2 (declared field beats recogniser)

---

## The problem, in one sentence

Every one of the four costly waits I measured tonight **was already visible** — written on my surfaces, in `BRIEFS_MAP`'s watch list, on the fleet freshness scan, in `GATES.tsv` with its `last_checked` date in plain sight. **Nothing was hidden. Everything was seen and nothing was ruled.** What the system has never had is a way to say *which* of the visible waits will arrive too late.

## The rule

> **FIRES = the ACTION owner has not consumed or ruled, AND a dated decision that consumes the answer falls inside the window.**

Both legs required. Owner-unread with no dated consumer is backlog. A dated consumer with the owner already engaged is in hand. The conjunction is the fire. (Derivation and tonight's applied output: `01_signal-latency/03_NEXUS_merged-triage-rule.md`.)

## 1. The declared field — exactly

One line, appended to any ask:

```
consumed_by: YYYY-MM-DD | <the decision it feeds> | <owner of that decision>
```

or, and this value is as important as any date:

```
consumed_by: NONE
```

**`NONE` is a legitimate answer meaning "no dated consumer; this can wait indefinitely."** It is what AEOLUS↔WATT's Colorado River reconcile carries (consumer is the ~8/30 ROD, three weeks out), what ZHAO's China arbiter carries, what HAWK's dormancy carries. **A missing field is a defect. `NONE` is a decision.** Most of the value of this proposal is in how many asks turn out to be `NONE`.

**The consumer must be a named artifact or event, never an adjective.** `2026-08-19 | FOMC minutes de-provisionalize LABOR's driver grade | LABOR+NEXUS` — not `soon | important`. This is Discipline J's "a boundary must be a number" applied to dates, and it is the guardrail against the everything-is-urgent failure.

### Which surfaces — exactly four, all of them already exist

| Surface | Change |
|---|---|
| `PROME/GATES.tsv` | One new column. Rows already carry condition, consequence, state, `last_checked` |
| `PROME/WILL_QUEUE.md` | **The `Needed by` column already IS this field.** The change is (a) mandatory, (b) blank now means `NONE` explicitly rather than "nobody said," (c) the decision gets named, not just the date |
| Cross-agent packet headers (carve-out ① packets) | One header line |
| Pre-registration cards / prediction rows | They already carry resolve dates. The addition is naming the **decision**, not just the date — the gap that let PRED-38/40 sit inert at "Q3-end" |

**No new file. No new register. No new script.**

## 2. Who evaluates it, and when

**Nobody new. It rides DAEDALUS's Rung A hook.**

`.claude/settings.json` already fires `session_banner.sh` at every session — the only check in the fleet an agent cannot forget, because a hook fires it rather than a document. Rung A adds a gate-freshness line there. ABN is **one more line in the same output**:

```
⚠ ABN  <ask>  owner=<who>  consumer=<decision> <date>  slack=<N>d
```

**Printed at EVERY agent's boot, not only PROME's.** That is not incidental — it is the entire lesson of the C-36 case. The desk that could rule was not booted; three desks that could not rule were. If the line prints wherever anyone happens to be, then any booted agent can escalate, route, or ask PROME for a proxy. Under the current design the only reader of a stalled adjudication is the agent that is not there.

**Prints only on violation. Never a clean line, never a summary.** Absence of output is the normal state — the guardrail against DAEDALUS's own §5c disease, where three unblocking advisories at every closeout become three commands nobody reads.

## 3. The arithmetic — and the half that is predictive

For each ask: `slack = consumed_by_date − today`.

**Fires when `slack ≤ 0` OR when `slack < the owner's median days-between-sessions`.**

That second clause is the whole point. Owner cadence is already measured — WALTER's per-recipient table has it, and my own scan has it (BOND: 6 own-work session-days in 31 ≈ 5-day cadence). So the rule fires **at the moment the owner's own observed cadence makes the deadline unreachable**, not on the day it is missed.

Worked on tonight's headline: BOND's C-36 ask has 12 days of slack to the ~8/19 minutes against a ~5-day cadence. It does **not** fire on the deadline test. It fires in about seven days — or immediately, if BOND stays dark and the cadence estimate degrades. **A due-date list would have told us on 8/18. This tells us while there are still two cadence cycles left to spend.**

## 4. How it composes with T1 — one system, not two

This is the part PROME asked me to get right, and it resolves cleanly because the two metrics ask different questions of the same rows.

- **T1 asks:** *has a registered condition crossed?* → answered by a scheduled evaluator that pulls the series.
- **ABN asks:** *is anyone going to look at it in time?* → answered by arithmetic on a date field.

They share **one register and one output channel.** T1's evaluator writes a crossing into the same flag file the Rung A hook reads; ABN computes slack on the same rows. Then:

> **A T1 crossing with no ABN owner engaged = a silent fire.**
> **An ABN violation with no T1 crossing = a stalled adjudication.**
> **Both together = tonight's BOND item.**

One file, two columns, one hook line. **ABN needs no evaluator, no script and no surface of its own** — which matters because PROME's T3 and DAEDALUS's N3 both say any new mechanism must pay for itself.

## 5. What it retires — the anti-ratchet payment

Three things, and I am putting two of my own surfaces on the list first:

1. **My hand-maintained owed-lists** — the next-boot-owes block in `LAST_COMPLETION.md` and the duplicate watch-items block in `BRIEFS_MAP.md`. Both are prose lists of what other desks owe, maintained by memory, and **they are what produced tonight's false "SHADE's ARCC pre-reg still UNGRADED" flag.** Under ABN the ask carries its own clock and the list has no reason to exist. *(This is the copy-kill discipline applied to myself — see proposal 02.)*
2. **`GATES.tsv`'s `>5d refresh` rule.** Replaced by slack, which is strictly better: 5 days is an arbitrary constant applied uniformly, and it is why four LIQUID gates and one OSPREY gate all read "violating" tonight when only one of the five has a consumer inside the window. Slack distinguishes them; a constant cannot.
3. **`WILL_QUEUE`'s 21-day age tripwire for undated rows.** An undated row becomes a row carrying `consumed_by: NONE` — an answer rather than a defect awaiting a nag.

## 6. Cost, risk, falsifier

**Cost.** One TSV column, one packet-header line, one hook line, and a one-time pass to fill the field on ~20 queue rows and 8 live gates. No cloud, no per-run cost. Under an hour of one session if Rung A ships alongside it.

**Risks, and the guardrail for each.**

| Risk | Guardrail |
|---|---|
| Dates get filled defensively/optimistically — everything urgent | The consumer must be a **named artifact or event**, not an adjective. A reviewer can check the named event exists |
| It becomes another skipped advisory line | Prints **only** on violation. Never a clean line |
| The field rots like every other stamp | It is derived from an *external* calendar (a filing, a meeting, an expiry), not self-stamped — the property `finding_mtime_is_corrupted_by_git_sync` and PAT-044 both say is what makes a field survive |
| Cadence estimates are noisy | The cadence clause only ever fires *earlier* than the deadline clause. Worst case it is early, never late. WALTER's own method caveat on session-day proxies applies and is disclosed |
| **It becomes a way to point at other desks** | The hook prints at every boot including your own asks. I flagged in the cross-reply that I applied the cost test to five desks tonight and never once to my own owed list |

**Falsifier — registered, with a date.** Re-run tonight's fires-now list on **2026-09-07**. **If ABN has read clean for 30 days while a BOND-class wait still occurred, the metric is missing a cost channel and should be replaced, not tuned.** Symmetrically: if ABN fires more than ~5 items in any single week, it has become a nag list and the second leg is not doing its job. Both branches are numeric and neither is renewable.

**Honest backtest limit.** Applied to my Phase-1 ledger, ABN fires on all four costly waits and none of the six harmless ones — but **I designed it from those ten cases, so that is consistency, not validation.** The nearest thing to an out-of-sample test is tonight's fires-now list built from WALTER's data, which I had not seen when I wrote the discriminator: it fires on 4 and silences 7, including a 42-day-old unread IMMEDIATE and a 10-day HAWK backlog that raw age would have escalated. That is the evidence I would actually stake it on.

## 7. What Will would see tomorrow

The whole output of this proposal, on tonight's data, is:

> **Launch BOND** — the answer to the board's oldest open adjudication has been in its inbox 8 days, consumer 8/19, live 25× position on the channel.
> **Launch LIQUID** — 2 unread ACTION signals hitting 2 of its own unchecked gates, consumer 8/12.
> **Retire one delivery** — ZHAO's yen signal expired when the BOJ meeting it preceded already happened.

Two launches and one retire, out of 932 deliveries, 72 unconsumed items, 5 gates past rule and 20 queue rows. **That is what this proposal is for: not to find more, but to say which of the things we already found is the one that costs.**
