# L496 — Unattended-instrument register · BLUEPRINT v1 (register shape)

**Author:** DAEDALUS · **Written:** 2026-10-20 09:1x ET (`date` 09:17; first stamp ran ahead of the clock and was corrected — PAT-188) · **Row:** `PROME/DOCKET.tsv` L496 (Will 9/25 "proceed in order", system item 2) · **State:** BLUEPRINT DELIVERED — v1, plan-read by one independent reader (see L495 spec §9–§10, same read); seed rows drafted from a live host inventory; **register not created** — its home is PROME's (§2), and it is populated by PROME (lane + PROME rows) and each desk (own rows). Promotion of this text into `BLUEPRINTS/` waits for PROME's consumer read.

## 1. Why the register exists

An unattended instrument (timer · cron · cloud routine · GitHub Action · long-running service) writes fleet surfaces on its own clock, so no session watches it run. Two 9/25 failures were invisible for that reason: LIQUID's `hy_oas_watch.py` runs at 13:00 ET while FRED publishes ~16:15 ET, so unattended it is always a day late; and its state text carried "CONTESTED 8/23 ⇒ GUARD-HELD-PENDING-ARBITER" 28 days after the arbiter answered. Neither is a code crash; both are a **clock** and a **last-human-read** fact that nobody recorded. The register records them, once, per instrument.

## 2. Home and format

- **Proposed home:** `PROME/registry/UNATTENDED.tsv` (PROME creates it; beside `READS.tsv`, which it mirrors in spirit — one row per fact, owner-attested). TSV, LF line endings (`finding_crlf_textmode_tsv_flip`), header row exactly as §3.
- **Machine-local items** (systemd units, local services) also keep their `PROME/MACHINE_LOCAL.md` row; the register row points at it (`machine_local_row`) and never restates the machine status.
- **One row per instrument**, not per output file. An instrument with several outputs lists them `;`-separated in `writes`.

## 3. Columns (16)

| # | Column | Content | Rule |
|---|---|---|---|
| 1 | `instrument_id` | short stable id, e.g. `liquid-hy-watch` | unique |
| 2 | `owner` | desk that owns the code | one desk; PROME for the lane and PROME's own |
| 3 | `kind` | `systemd-timer` · `systemd-service` · `cron` · `gh-action` · `cloud-routine` · `console-agent` · `other` | |
| 4 | `host` | `desktop` · `laptop` · `both` · `github` · `anthropic-cloud` | WSL caveat: a user timer fires only while a WSL instance runs — `host` alone never implies it ran |
| 5 | `schedule` | the trigger as written in its unit/cron/YAML, with the timezone **the scheduler uses** (GitHub cron is UTC and ignores DST) | copy from source, never paraphrase |
| 6 | `schedule_source` | path to the unit / workflow / routine definition | must resolve |
| 7 | `inputs` | data the run consumes (`FRED BAMLH0A0HYM2`, `newsweep feeds`) | |
| 8 | `input_publish_time` | when each input is published, ET, with source of that fact; `UNKNOWN` allowed | |
| 9 | `lag_verdict` | `SAME-DAY` · `NEXT-DAY` · `INPUT-NOT-PUBLISHED-AT-RUN` · `UNKNOWN` — derived from 5 vs 8 | the hy_oas 13:00-vs-16:15 class shows here |
| 10 | `writes` | repo-relative paths (or external surfaces) it writes | `;`-separated |
| 11 | `commits` | `self-commits` · `reader-commits` · `gitignored` · `external` | `gitignored` = invisible to the other box and to every git-based check |
| 12 | `will_facing` | `yes` / `no` — does any output reach Will without a desk reading it first | |
| 13 | `carried_state` | any judgment text the instrument repeats run to run (a gate state, an arbiter verdict) and the file it is read from; `none` if pure data | the stale-arbiter class lives here |
| 14 | `last_human_read` | `YYYY-MM-DD` + reader + artifact where a human-or-desk session last READ THE OUTPUT TEXT (not the code) and confirmed it current | never inferred from a commit; `UNRECORDED` allowed and reported |
| 15 | `canary_path_id` | the L495 path id covering it, or `none` | `will_facing=yes` + `none` = open gap |
| 16 | `machine_local_row` | anchor in `PROME/MACHINE_LOCAL.md`, or `n/a` | |

## 4. Freshness rules (what a future check enforces — not built here)

| Rule | Condition | Verdict |
|---|---|---|
| R1 | `last_human_read` older than 30 days on a row with `carried_state ≠ none` | DUE (owner re-reads output text) |
| R2 | `will_facing = yes` and `canary_path_id = none` | gap, reported at the owner's boot |
| R3 | `lag_verdict = INPUT-NOT-PUBLISHED-AT-RUN` | the same cell also names the compensating session — `INPUT-NOT-PUBLISHED-AT-RUN; compensating=<desk session or none>` (who reads the input on publish day) |
| R4 | `schedule_source` does not resolve | UNKNOWN |
| R5 | an instrument found in a host inventory (`systemctl --user list-timers --all`, `crontab -l`, `.github/workflows/*.yml` with `schedule:`, cloud-routine list) with no row | gap; the inventory command and date are recorded |

The 30-day number in R1 is a **proposal** for PROME/Will, not a ruled threshold.

## 5. Who populates

PROME: the RESEARCH-INTAKE lane row(s), PROME's own instruments, and R5's inventory pass. Each desk: its own rows, at its next session after PROME creates the file. DAEDALUS: the shape; a reader of the first populated version on request.

## 6. Seed inventory (DAEDALUS, 2026-10-20 09:1x ET, this desktop only)

Read-only inventory: `systemctl --user list-timers --all` (2 timers) · `ls ~/.config/systemd/user/` · `crontab -l` (none) · `Research-Intake/.github/workflows/` (1 workflow with `schedule:`) · grep of desk charters for routines. Draft rows for PROME and owners to correct, not attestations: `design/2026-10-20_L496_SEED_ROWS.tsv`. Plan-read findings and their dispositions: L495 spec §10 (one read covered both docs).

Found and **not** yet attributed (UNKNOWN, owner to say): `clawdbot-gateway.service` (node gateway on port 18789; `~/.config/systemd/user/`) — whether it writes any fleet surface is not established here. The NISABA console agent's 06:00 schedule is PARKED for v1 (`STATUS.md` 10/17), so it gets no row until it runs. Laptop inventory not taken (one machine at a time).
