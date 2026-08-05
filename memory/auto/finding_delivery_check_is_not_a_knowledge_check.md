---
name: finding_delivery_check_is_not_a_knowledge_check
description: Checking a recipient's INBOX tells you about the packet, not about what they already know — for a "you may be missing X" packet the target artifact is the owner's KB
metadata:
  type: feedback
---

Before sending a 🔴 URGENT packet warning an owner they may hold only half of a
number, **verify the owner's KNOWLEDGE, not the packet's DELIVERY.** These are
different artifacts and only one answers the question you are actually asking.

**The instance (PROME → VIOLET, 2026-07-27).** A commit body claimed a VIX-COT
decay finding was *"routed to VIOLET."* No packet existed — caught correctly by
checking VIOLET's inbox rather than trusting my own commit body
([[finding_record_of_an_action_is_not_the_action]]). I then sent it URGENT, on
the premise that VIOLET might hold only WALTER's bullish framing of `+3,098`
(net-long = supportive) and not the bearish half (down ~70% from `+10,189`).

**VIOLET had held both halves since two days earlier.** `KB-VIO-125` already
graded the pair as *confirm-2 FAILED* (needed pct3y ≥95, got 92.9) **with the
fade line (<90) also unmet** — i.e. the correct two-sided read, registered
against a pre-locked branch tree, before I noticed the number existed. One grep
of the owner's KB would have shown it.

**Why:** the inbox answers *"did my thing arrive?"* An owner-gap claim asserts
*"they don't know X"* — a claim about their state, which only their own
canonical surfaces (KB / STATUS / workbook) can support or refute. I verified
the wrong artifact and got a true answer to a question I wasn't asking. Cost:
one redundant packet, and a **false owner-gap propagated into two live surfaces**
(HEARTBEAT and SCRATCH both asserted VIOLET "holds only the bullish framing"),
which reads to every future reader as an outstanding owner obligation that does
not exist. Manufacturing owner debt is its own kind of error — it sends the
fleet chasing a closed item.

**How to apply:** before writing any packet whose premise is *"you may be missing
X"* or *"you may be carrying X one-sided"* — grep the owner's KB/STATUS for the
figure or its trigger ID first. If they have it, the packet is unnecessary; if
they have it **framed differently**, that is a much sharper packet than the one
you were about to write. Corollary for state files: an owner-gap sentence is a
CLAIM ABOUT ANOTHER AGENT and deserves the same verification bar as a number —
`[[finding_never_received_is_not_doesnt_hold]]` is the sibling failure, and this
is its inverse. Related: [[finding_asymmetric_rigor_counterparty_claims]],
[[finding_canonical_surfaces_stale_inbox_carries_live_state]].

**n+1, 2026-08-05 — the SAME error at fleet scale, and it produced a number that was almost entirely noise.** Asked to sweep for orphans, PROME counted **189 packets sitting at top-level `AGENTS/*/inbox/`** across the fleet, 35 of them ≥7d old, and reported it as unprocessed work. The justification was that every one of those agents maintains an `inbox/processed/` directory with real volume in it — **necessary, but not sufficient**, because an agent can consume a packet and simply not file it.

**Sampling refuted it in three of three tries:** ZHAO's STATUS references the lane query it supposedly hadn't read · OZK's references the Zion-axis verdict · **DEWEY had shipped `AGENTS/DEWEY/output/2026-07-28_c4-phantom-debt-magnitude.md` while its C1/C3/C5 prompt packets sat unfiled**, plus three more outputs on 8/02. Worse, `ACTIVE_DECISIONS.md` *already recorded* the answer — LABOR marked *"pure bookkeeping residue … only its packet was never `git mv`'d to `processed/`."* And the leading fix PROME was about to recommend died on measurement too: **37 of 37 agents already have an inbox step in their boot protocol**, so the queued "boot-rule blessing" would have changed nothing.

**Two lessons, and the second is the sharper one:**
1. **Inbox POSITION is a filing fact, not a knowledge fact.** Same failure as the 2026-07-27 instance, one layer up: a *count* of unfiled packets is not a *measure* of unread work. Read a sample of owner surfaces before quantifying anyone's backlog — and note the mirror-image case from the same session: a top-level `MSG-*` file with **two ACCEPTED obligations and a live review date is open BY DESIGN**, so unfiled-and-correct exists too.
2. **When a metric cannot separate two states, do NOT build an alarm on it.** The real defect is that nobody can distinguish unread from unfiled, so **a genuine orphan hides inside ~189 items of noise** — and a depth alarm would fire on all of them, training the fleet to ignore it. That is `consumer_check`'s 9-of-9-FP class reproduced at fleet scale. Fix the *filing* discipline (a closeout `git mv` step) rather than instrumenting the ambiguous signal.
