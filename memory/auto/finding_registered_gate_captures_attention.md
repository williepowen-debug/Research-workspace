---
name: finding_registered_gate_captures_attention
description: "A live gate on ONE instrument silently redefines its whole channel — the loud tracked event hides the quiet countable one; sweep the un-gated instruments separately and say so in writing. ⚠️ THE SAME ASYMMETRY RUNS ONE LEVEL UP, ON PROTOCOL: registered STEPS get audited and unregistered REASONING does not — the instrument has a checklist, the inference has none (n=2, CORAL + PROME, 2026-08-23)."
symptoms: "every check I ran came back clean and the error was somewhere else · I audited the instrument because auditing instruments is a boot step · nothing in my protocol says to audit the argument · the peer caught both and I caught neither · my checklist passed and my reasoning did not"
  ⚠️ THIRD LIMB (HENRY, 2026-08-23): AUTOMATING ONE LANE STARVES ITS MANUAL SIBLING — a lane worked diligently for six weeks went dark three days after its twin got a boot-time enumerator, and stayed dark 23 days while every freshness instrument read the desk as current."
symptoms_extra: "one queue is current and its twin is months behind · I am not dark, I commit constantly, every staleness check passes · the step is written down but nothing runs it · I automated the sibling and never noticed this one stop"
metadata:
  node_type: memory
  type: finding
---

**OSPREY, 2026-07-31.** From 7/20 the desk ran a daily, dated, named adjudication on the CPC loading halt — `GATE-OSPREY-001`, Will-approved, PROME-registered, day-count clock, leg-by-leg checks, packets to BRENT. CPC carries **Kazakh** crude and was **pre-registered as non-countable** to OSPREY's own predictions; the desk had correctly written that down.

Meanwhile, on 7/22, **Sheskharis** (Novorossiysk) — a **Russian** crude-export terminal moving **~650 kb/d, ~1/5 of Russia's seaborne crude exports** — halted loadings for five days. Bloomberg reported it **7/24**, the same day the desk ran the day-5 CPC gate check and wrote *"Channel 2 — no new terminal damage found, non-countable attribution HOLDS."* That read stayed wrong for **nine days**, was routed to two consuming agents in that state, and **failed the desk's own prediction** (OSP-01).

**Why:** this is not stale-ledger and not named-target-only search — the ledger had been swept two days earlier and the desk searched broadly and *found things*. It is **attention capture**. A registered gate creates a dated, named, recurring obligation, and nothing creates an equivalent obligation for the un-gated part of the same channel. The gate manufactured the *feeling* of coverage — daily checks, real evidence, real adjudication — while covering only the one instrument that could not move the desk's own predictions. **The most-instrumented object silently redefined the channel's scope.** The sharpest version: the gate's subject was registered as *non-countable*, so effort and decision-relevance were pointed in opposite directions **by construction**, and the more diligently the gate was worked the more complete the coverage felt.

This is the inverse of the usual staleness failure. Nothing was rotting; something was **crowded out**. A staleness check cannot catch it, because the gate file is the freshest artifact on the desk.

**How to apply:**
- When a gate/tripwire is live on ONE instrument inside a channel, **run a separate explicit sweep of that channel's OTHER instruments every session, and write down that you did** — a gate check does NOT discharge a channel check.
- **Never re-affirm a channel score from gate evidence alone.** If the only fresh evidence under a channel mark came from the gated instrument, the mark is UNVERIFIED, not held.
- Ask each session: **"what in this channel is not being watched by the thing I'm watching?"**
- ⚠️ **If a gate's subject is pre-registered as non-countable to your own predictions, treat that as a standing flag** that attention and decision-relevance have been decoupled — that is the highest-risk configuration, not a safe one.
- Applies to any agent running a registered gate, not just war theaters: the mechanism is the obligation asymmetry, not the domain.

Related: `[[finding_theater_check_before_gate_check]]` · `[[finding_standing_guard_is_a_false_negative_risk]]` · `[[finding_coverage_gap_needs_all_surface_check]]` · `[[finding_verification_zero_is_ambiguous]]` · `[[finding_count_measures_intake_not_domain]]`

---

**PROTOCOL-LEVEL LIMB, 2026-08-23 — n=2 across two desks in one day. Registered STEPS get audited; unregistered REASONING does not.**

**CORAL, self-reported at closeout:** it registered a 🔴 leg with a trigger and no falsifier, and separately built an argument resting on a test that could not fail. **Both defects are the same shape — a condition that cannot come back against you — and they occurred three hours apart.** It caught the one in the instrument and missed the one in itself. Its own diagnosis, which is the actionable half:

> *"I audited the leg because auditing legs is a registered step, and I didn't audit the argument because nothing in my protocol says to. The instrument had a checklist; the inference didn't."*

**PROME, same day, independently:** every checklisted item ran and passed — gate-vocabulary check (which caught a bad state token on the spot), orphan check, memory-index check, push-receipt verification by path. **All four of its real defects sat in un-checklisted reasoning:** resolving a rule's status between two derived artifacts instead of the canonical letter; an authorship filter matching one prefix form; asserting a packet delivery nobody verified at the recipient; a 31-day ledger gap nothing was required to route. **The mechanical surface was clean the entire time.**

⇒ **A checklist does not merely fail to cover inference — it supplies EVIDENCE OF DILIGENCE that makes the uncovered half feel covered.** "All checks green" is true and is a statement about the checked set only. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.

## How to apply

- 🔴 **Ask at every closeout: what did I CONCLUDE today that no step required me to verify?** The checklisted work is not where the defects are — it is where the defects are not, by construction.
- **Peers catch what protocol cannot.** Both CORAL instances were caught by HOMER; PROME's four were caught by BOND, WALTER, MIDAS and CORAL. ⇒ **route your reasoning to a peer specifically when no gate obliges you to** — that is exactly the case the protocol will not surface.
- ⚠️ **Do NOT respond by adding checklist steps for inference.** The failure is a category difference, not a coverage gap; a checklist item reading *"audit your argument"* is unfalsifiable and will be ticked. **The instrument is a second reader, not a second box.**

---

**THIRD LIMB — HENRY, 2026-08-23. The gate does not only capture attention from UN-gated instruments. It captures it from a SIBLING LANE DOING THE SAME JOB, and mechanising one half is what does it.**

HENRY has two inbox lanes with identical obligations: a top-level `inbox/` and a WALTER delivery lane at `inbox/WALTER/`. Both had a written boot step. Only one got automated.

    2026-07-28  boot (f) top-level inbox triage lands — HENRY's own commit
    2026-07-31  WALTER lane consumed for the last time
    2026-08-23  53 unconsumed, oldest 16d — top-level lane drained to zero the same day

Consumption by month: **June 37 · July 102 · August 6 (+53 unconsumed).** The lane was worked diligently for six weeks and **stopped three days after its sibling got a mechanical enumerator.** The cause was one character of scope: `inbox.glob("*.md")` is **non-recursive**, so `inbox/WALTER/` had never been visible to any instrument. Step 3a was prose the whole time.

**Why this limb is distinct from the two above:** OSPREY's gate crowded out *un-instrumented* parts of a channel; CORAL/PROME's checklists crowded out *reasoning*. Here **both halves were registered obligations in the same document** — one acquired a runner and the other did not, and the automated one absorbed the attention the manual one had been getting on habit alone. **Habit is a shared, depletable resource; a runner does not add coverage to one lane, it reallocates attention away from every lane that lacks one.**

**The reason it survived 23 days is the sharp part:** every freshness instrument read the desk as healthy. Zero days dark, commits daily, STATUS current, ledger checks passing — and a dark-owner doorbell could not help, because *darkness was not the failure*. A desk that boots and does not read is invisible to every instrument built to detect a desk that does not boot.

**How to apply:**
- 🔴 **When you automate one instance of a repeated obligation, enumerate every OTHER instance of that same obligation in the same edit** — and either wire them too or write down that you did not. The dangerous moment for lane B is the day lane A gets a runner.
- **Check the SCOPE of any enumerator you rely on, not just its output.** A non-recursive glob, a single-directory scan, a filter tuple missing a token: the read looks healthy because it *is* healthy about the subset it sees. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.
- **Measure a lane by CONSUMPTION RATE PER MONTH, not by whether it has ever been worked.** "145 items processed" and "0 processed in three weeks" are both true of a dead lane.
- ⚠️ **Framing selects the remedy.** Reported as "this desk doesn't drain its backlog," the fix is a nag and it recurs. Reported as *"one lane stopped, on this date, while its twin is current,"* the fix is a five-minute scope change. The peer who reported it (WALTER) corrected its own framing from the first to the second before sending, and that correction is what made it findable.

Related: `[[finding_mechanize_the_cap_not_the_ritual]]` — a deferrable step wants a boot check, not a remembered ritual; this limb is its failure mode when only *some* of the steps get one.
