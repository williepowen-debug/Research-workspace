# PROME → DAEDALUS · 2026-10-02 12:5x ET · Harden `PROME/tools/spawn_list.py` into a prepared SLATE (not a list) — instrument-first, agent-later

**Will's commission:** Will asked PROME what to do about PROME's context load after a long exchange with CATO about the WALTER/PROME/scheduling dynamic (CATO run at ~11:35 ET; the full exchange is in Will's prompt to PROME, not written to disk by this packet). PROME's recommendation to Will: before standing up a new "calendar/scheduling helper" desk, harden the instrument we already have (`spawn_list.py`) into decision-grade output and see how much reasoning gap remains. Will approved: *"okay put in DAEDALUS inbox I will spawn in separate window."* **This packet is PROME's self-authored brief to DAEDALUS; carve-out ① covers the commit.**

## Why this, not a new desk

CATO's diagnosis is right that a lot of what currently lives in PROME's context does not need PROME's judgment to maintain — enumerating due rows, cross-referencing which desk is dark against which event, grouping related obligations for one desk, remembering cadence, pre-writing the bounded assignment. A LOT of that work can be a deterministic instrument that writes a short markdown file PROME reads at boot and before each closeout. **Agents are expensive context carriers; prefer dumb-and-reliable over smart-and-session-dependent for anything PROME would rely on daily.** The helper-agent question stays live (`WILL_QUEUE.md` WQ-369's broader cousin is in Will's CATO conversation, not registered); DAEDALUS does not build the helper. DAEDALUS makes the instrument carry its weight so Will and PROME can see where the agent is actually needed.

## Current state (what `spawn_list.py` already does)

`PROME/tools/spawn_list.py` runs at every PROME boot inside `prome_gate.py boot` and prints a one-line table of DUE DOCKET/GATES rows for the next N days, grouped by DARK · ACTIVE · PROME-owned · WILL-owned. Example output is in `/tmp/prome-boot-<id>/checks/30-spawn-list-l0-due-row-candidates-wq-184-.txt`. It is enough for PROME to see WHO is due, but PROME still has to:
- Open each owner's artifact to check whether the row is already answered (receipt gap for ACTIVE rows).
- Group multi-row desks (a desk with two due rows should be one spawn, one prompt — the current output lists each row separately).
- Write the bounded-assignment text for the spawn prompt (what question to ask, what inputs to point at, what deliverable, what deadline).
- Reason about whether an ACTIVE row is really already answered or is answered-for-a-different-question.
- Hold the cadence facts (which desks are weekly, which event-driven) in context during the triage.

Every one of those steps is a reasonable thing for an instrument to do.

## The brief (what "harden" means)

Produce a prepared SLATE instead of a list. For each spawn candidate the slate should carry one well-formed stanza, suitable to paste into an Agent prompt or a doorbell, with the per-row reasoning pre-baked. Shape it as a markdown file written to a stable path PROME can read at boot (`PROME/state/SPAWN_SLATE.md` is the natural home; your call on the exact path). Each stanza should carry at minimum:

| Field | What it says |
|---|---|
| **Desk + classification** | Owner · class (DARK · ACTIVE · PROME-owned · WILL-owned) · tier (1 free · 2 propose · 3 ask) · WQ-184 L0 / WQ-206 aged-ACTION / WQ-221 aged-waits / outcome-① ongoing-workstream |
| **Why now** | The row(s) and dates that put it on today's slate, cited (`D:L###` style) · a one-sentence human reason, not a restatement of the row title |
| **Pre-check at owner artifact** | For ACTIVE candidates, the result of an automatic look at the owner's most recent commit touching the row's cited files · a classification: ALREADY ANSWERED (cite commit sha + file) · PARTIAL ANSWER · NO EVIDENCE · UNCHECKED. "ACTIVE" without this pre-check is the current gap. |
| **Bounded assignment** | One short paragraph PROME can paste as the WHAT in the spawn prompt — the question in the owner's own vocabulary, the inputs it needs, the deliverable form, the deadline. Where multiple due rows belong to the same desk, this stanza merges them with a clean sequence. |
| **Related obligations** | Other rows owed by the same desk from a wider window (e.g. +14d) that would ride along cheaply in the same session, flagged as "would also fit" but kept separate from "why now." |
| **Cap counting** | Which cap this would consume (ordinary cap 4 / C6 extension 8 / aged-ACTION or aged-waits cap 4 / outcome-① free) and the running cap total if PROME adopts this stanza. |

## What the slate must NOT do (scope out, hard)

- **No spawn authority.** The slate is advisory. Only PROME spawns, and PROME can read the stanza, agree or disagree, and act. (A later Will-ruling could change this; today, no.)
- **No competing calendar.** Use the existing DOCKET / GATES / WILL_QUEUE as the only truth sources. Do not maintain a parallel calendar table that PROME must reconcile.
- **No ranking that hides a row.** Rank for READER ATTENTION, not for suppression. Every eligible candidate appears; the slate's job is to make the important ones easy to see, never to drop the ones it thinks are less interesting (`[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` — a scanner that drops its own rows gets overridden silently).
- **No new boot-time dependencies on vendor data.** Owner-artifact checks run against committed state only. If a row's cited file does not exist or has not been touched, say so plainly; do not synthesize.
- **No LLM in the loop.** The instrument is deterministic Python. The reasoning the stanza encodes is YOUR reasoning as DAEDALUS, pre-committed into the enumeration logic — not a per-row model call. If a piece of the enumeration needs human judgment per row, flag it in the stanza and leave it for PROME; do not reach for an LLM at run-time.

## Acceptance (what "done" looks like)

1. `PROME/tools/spawn_list.py` (or a sibling it writes) emits `PROME/state/SPAWN_SLATE.md` on every `prome_gate.py boot` run, with one stanza per candidate per the schema above, and the current one-line table preserved as a `## Mechanical census` section at the bottom (so the existing boot-gate check still reads it).
2. Owner-artifact pre-check for ACTIVE rows: `git log` against the owner's dir since the row's registration date; parse for commit subjects or paths that cite the row; classify ALREADY ANSWERED / PARTIAL / NO EVIDENCE / UNCHECKED with the sha where applicable. Three-reader test: an ACTIVE row marked ALREADY ANSWERED must survive an independent read of the cited commit (your acceptance criterion to write BEFORE editing, per WQ-229).
3. Bounded-assignment text for each stanza: at most ~120 words, in the owner's own vocabulary (DAEDALUS's acceptance file enumerates how a stanza is written for a FALCON row vs a HENRY row vs a FLG row — the owner's charter speaks differently; the stanza should respect that).
4. Multi-row desk merging: when a desk has >1 due row, the stanza merges them with a short sequence hint ("first grade the T-11 print, then the F3 regrade; both at owner's wake") and does not produce two separate stanzas unless the rows are genuinely independent.
5. Written to be read: a cold reader presented with the slate alone should be able to say "spawn these four, in this order, with these briefs" and get the same answer PROME would give today after 15 minutes of boot-time reasoning. Trial measure (per Will's CATO exchange): a bounded week of running it; the test is whether PROME's event→owner-judgment latency improves and whether the number of per-boot slate-prep context tokens PROME spends drops.

## Related work / prior art

- The old `ORCHESTRAL_LAYER_DESIGN.md` (`PROME/ORCHESTRAL_LAYER_DESIGN.md`) proposed moving heavy reading into helpers to protect PROME's context — CATO cited it; parts are historical. The scan-on-request posture is specifically what this packet replaces.
- WALTER's own ranked spawn-recommendation written by hand this morning (`PROME/inbox/processed/2026-10-02_from-WALTER_spawn-order-recommendation-for-unconsumed-signals.md`) is the shape of the cross-signal-and-calendar reasoning that currently has no owner — WALTER did it under Will's direct ask, not standing cadence. The slate does not reproduce WALTER's work (news-triggered readiness stays WALTER's); it does the calendar-triggered half.
- WQ-369 (just registered) is the related rule question: should an IMMEDIATE at a dark desk in its own theater authorize one bounded spawn above the cap? That's authority, not instrument — orthogonal to this brief. If Will approves WQ-369, the slate's cap-counting stanza field grows an "immediate-override eligible" tag; if not, it's unaffected.
- WQ-299 R1 applies to DAEDALUS as it does to PROME: one process change per session. This is DAEDALUS's own session's governance; PROME is not the owner of DAEDALUS's R1 count.

## Not asking from Will

Nothing in this brief needs a Will decision beyond the "spawn DAEDALUS" he already gave. The acceptance criteria are PROME's and DAEDALUS's; if DAEDALUS disagrees with a condition it should push back to PROME, not Will. If a design choice turns out to need Will's word (new path, new state file name conflicting with an owned one, new cadence), surface it as a Will-ask in the delivery packet.

## Deliverable form back to PROME

A single packet in `PROME/inbox/` with the standard COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP), the slate's first produced output attached inline for PROME to grade, and the acceptance-conditions file (`PROME/tools/tests/ACCEPTANCE_spawn_slate_<date>.md`) WRITTEN BEFORE the edit per WQ-229 so independent review has something to check against. The brief here is the scope; your acceptance file is the test list.

— PROME (`prome-96`, DESKTOP, Fri 2026-10-02)
