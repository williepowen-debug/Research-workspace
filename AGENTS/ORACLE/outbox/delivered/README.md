# `outbox/delivered/` — RETIRED 2026-08-27

**Do not add files here. Do not "catch up" the backlog.**

This directory implemented a hand-maintained "the recipient has picked this up" marker.
It has had **no consumer since HERMES was retired in June 2026** — agents poll each
other's inboxes directly — and it **stopped being maintained on 2026-07-17**: at
retirement it held **5 files while `outbox/` held 22**, none moved in 41 days.

**Why retire rather than revive:** a half-maintained delivery marker is worse than
none. A packet sitting in `outbox/` meant *either* "not yet picked up" *or* "picked up
41 days ago and nobody moved the file", and nothing on the surface distinguished them —
a fake signal about delivery state. Delivery is now evidenced where it actually
happens: the recipient `git mv`s the packet into its own `inbox/processed/`, which is
checkable from outside (`git ls-tree` on their dir) and needs no bookkeeping from me.

**The 5 files already here are kept as history** — they are real 7/02–7/17 dispatches
and deleting them would destroy the record. They are historical, not a live queue.

*Found in the Will-directed file sweep, 2026-08-27. See MAINTENANCE.md.*
