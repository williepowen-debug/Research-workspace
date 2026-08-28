---
name: finding_mtime_is_corrupted_by_git_sync
description: mtime records when a file landed on this disk, not when its contents were refreshed from source — git pull restamps it, so mtime-based staleness detectors fail in the false-negative direction
metadata:
  type: project
---

**`mtime` measures when a file last landed on this disk, not when its contents
were last refreshed from source.** Under the serial multi-machine protocol
(desktop ⇄ laptop, one at a time, `PROME/MACHINE_LOCAL.md`) those two quantities
diverge routinely, because any file a `pull` / `rebase` / `checkout` rewrites
gets a **current** mtime regardless of how old its contents are.

**Found by deletion, which is why it is trustworthy (VIOLET, 2026-07-27).**
While fixing a FRED cache-staleness bug, VIOLET built a 30-minute refetch
throttle keyed on cache-file mtime — then **deleted it before shipping**, having
traced that `fred_cache/*.csv` are git-committed, so a pull on the other machine
would stamp a stale file with a current mtime, the throttle would suppress the
needed refetch, and **the original bug would return by a new route.**

**Why it matters beyond that one script:** root `CLAUDE.md` Data Hygiene makes
*"LIVE with a boot-time **mtime** staleness alert"* one of only two sanctioned
states for a live ledger, and DAEDALUS's recurring silent-rot sweep plus HENRY's
ledger-staleness leg key on the same proxy. The failure direction is the harmful
one:

- false **positive** (mtime old, content fresh) → spurious "stale Nd" → noise, self-correcting
- ⚠️ false **negative** (mtime fresh, content stale) → **the alert never fires** → silent rot, exactly what the rule exists to prevent

Git produces the false negative. On a freshly-pulled box, every file the pull
touched is in that state.

**How to apply:** do not use mtime as a freshness proxy for anything that is
**git-tracked**. Derive vintage from **content** — the max observation date in
the series, a `Last-Updated` header, the newest row. mtime remains fine for
untracked, locally-generated artifacts (caches that are gitignored, scratch
output) and as a *liveness* signal for a file being actively written by a running
session — I used it that way at boot the same day and did not notice I was using
a proxy. Routed to DAEDALUS 2026-07-27 as a canon question (amend the rule /
re-point at content-derived vintage / require a corroborating content check);
the ruling is DAEDALUS's, but the underlying fact holds regardless.
Related: [[finding_ledger_drift_behind_narrative]],
[[finding_completion_stamp_skip_reads_as_current]], [[finding_passive_surface_rot_push_not_dashboard]].

**EXTENSION 2026-08-28 (DAEDALUS wiring sweep ⑯, n+4 measured in one grep):** four desks' `boot.py` key ledger age on `st_mtime`/`getmtime` and NEVER invoke the content-vintage enforcer — CORAL `scripts/boot.py:60`, CREED `:47`, LABOR `:113`, OZK `:265` (grep: 0 `ledger_staleness` refs in boot.py or CLAUDE.md on all four). On the machine that pulled, every ledger reads FRESH after the sync — the root Data-Hygiene (b) alert exists on paper and is blind in practice. CARL/HENRY/MARCO also compute an mtime age but ALSO run `ledger_staleness` (a duplicate display, not a blind guard). Discriminator for any staleness leg: does the desk's boot call `scripts/ledger_staleness.py` (content-vintage → git-commit → mtime last-resort, basis PRINTED)? If not, the mtime leg is the only guard and it fails false-negative on exactly the box that just synced. Owner packets routed 8/28; `symptoms:` grep-bait: "ledgers all read fresh right after a pull", "staleness alert never fires on the laptop", "age_days from st_mtime".

