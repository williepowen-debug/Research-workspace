---
name: finding-fetch-before-trusting-boot-sync
description: At boot, git ahead/behind reads the LOCAL remote-tracking ref and is stale until you `git fetch` — a `0/0` can hide a large gap (53 commits here), especially right after a serial-multi-machine switch; fetch before declaring "synced" or reading state.
metadata:
  node_type: memory
  type: finding
  originSessionId: 7fba96fe-eedd-439b-93bd-bdd521c2082b
---

**Incident 2026-07-04 (laptop boot).** PROME booted on the laptop and ran the boot repo-state gate — `git status --short` (clean) + `git rev-list --left-right --count HEAD...origin/master` → **`0  0`** → declared boot state ("synced 0/0") and read HANDOFF/SCRATCH/STATUS/HEARTBEAT. Will asked "did you pull all the latest from GitHub?" A `git fetch` then showed origin was **53 commits ahead** — the entire 7/3 + 7/4 desktop-session history, including two later PROME sessions. Everything the first boot declaration was built on was 53 commits stale (wrong OZK date, missing FRED-rotation progress, etc.).

**Why it happens:** `git rev-list HEAD...origin/master` compares against the *local remote-tracking ref* `origin/master`, which is only as fresh as the last `git fetch`. `git status --short` shows a clean *working tree* but says nothing about how far behind origin the clone is. So a clean tree + `0/0` reads as "fully synced" when it can mean "haven't looked at origin since the last machine had it." Under **serial multi-machine** (desktop ⇄ laptop, one box at a time), the machine you *just switched to* is almost always behind — its clone last pulled before the other box did a full day of work + closeout pushes.

**How to apply:** at boot, run `git fetch` (or `git pull --rebase` if the tree is clean/safe) **BEFORE** trusting ahead/behind, declaring "synced," or reading the state files — never trust a `0/0` that hasn't been preceded by a fetch this session. Highest-risk moment is the first boot after a machine switch. Cheap tell: if `git fetch` prints ref updates (`abc..def master -> origin/master`), your pre-fetch `0/0` was a lie and everything read so far needs a re-read. Relatedly `[[finding_two_machine_partition_clean_merge]]` (the merge is clean, but only *after* you've actually fetched the other box's work).
