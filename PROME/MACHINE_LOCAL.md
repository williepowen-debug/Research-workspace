# MACHINE_LOCAL.md — What Does NOT Travel With The Repo
**Created:** 2026-07-01 (Prome; Will-approved) · **Owner:** PROME · **Update rule at bottom.**

**Why this exists:** Will runs **serial multi-machine** — one machine at a time (desktop ⇄ laptop), closing out + pushing all agents before switching. Git carries every repo file cleanly across that handoff. **Machine-local infrastructure does not travel**, and its absence masquerades as breakage: the 7/1 session burned real time discovering that "Kalshi broken" and "HY auto-watch dark" were location facts, not defects. This file makes that a 10-second diagnosis.

## Inventory
*Laptop column verified 2026-07-01 on hostname `WilliePOwen` (believed LAPTOP — Will to confirm/label). **Desktop column verified 2026-07-02 on hostname `DESKTOP-BC6EF81`** (first desktop session post-cutover).*

| Item | Path | This box (7/1) | Desktop | Consequence when absent |
|---|---|---|---|---|
| Repo venv | `.venv/` | ✅ | ✅ assumed | root-canon python tools fail (yfinance etc.); rebuild from `scripts/requirements.txt` + FORGE reqs |
| Telegram channel tokens | `~/.claude/channels/telegram*` | ✅ | ✅ assumed | WALTER/PROME Telegram delivery fails |
| Kalshi creds | `~/.config/kalshi/{key_id.txt,private_key.pem}` | ❌ | ✅ (worked 6/27; files verified 7/2) | ORACLE `kalshi.py` dies at import → Kalshi lane is desktop-only until creds copied (chmod 600, NEVER in repo) |
| `liquid-hy-watch` systemd timer | `~/.config/systemd/user/` | ❌ | ✅ verified 7/2 — ran daily through 7/1 on the pre-scrub hardcoded key; runs on the `.env` key from 7/2 (installed) | between-session HY auto-watch dark on the laptop. **Mitigated 7/1: RESEARCH-INTAKE lane is now the machine-independent PRIMARY** (intake `89b2e31`); timer = redundancy. WSL2 caveat: user timers don't fire with no WSL instance running — true on BOTH boxes |
| LIQUID alerts output | `AGENTS/LIQUID/alerts/` | ❌ (never fired here) | ✅ log through 7/1 — **the 6/29 🔴 283 X1-tag alert fired here UNSEEN while the laptop was in use (live instance of the cross-box invisibility risk; surfaced at 7/2 boot)** | timer alerts fired on one box are invisible from the other (local writes, gitignored) |
| RESEARCH-INTAKE local clone | `/home/willi/Research-Intake` | ✅ (cloned 7/1) | ✅ | only needed to EDIT feeds — the lane itself runs on GitHub Actions, machine-independent by design |
| Pre-scrub mirror backup | `~/Research-workspace-PRESCRUB-BACKUP-20260630.git` | ❌ | ✅ (created 6/30; verified 7/2) | the history-scrub rollback net lives on the DESKTOP — locate it there before deleting post-public-flip |
| `gh` CLI | `gh` | ❌ | 🟡 `/usr/bin/gh` installed but **UNAUTHENTICATED** (`gh auth login` needed; verified 7/2) | GitHub API/PR/secrets ops unavailable until authed; plain git works (credential store ✅ both boxes) |
| Git identity (fresh clones) | repo-local `user.name/email` | main repo ✅ · new clones ❌ until set | ✅ | commits in a NEW clone fail "empty ident" — set repo-local from the main repo (done for Research-Intake 7/1) |
| `trash` CLI (rule #11: trash > rm) | on PATH (`trash-cli` package → `trash`/`trash-put`) | ❌ — found missing 7/23 late-eve (command-not-found mid-session); **workaround live: `gio trash <file>`** (`/usr/bin/gio` present); install `trash-cli` at next convenience | ✅ assumed (in daily fleet use; verify at next desktop boot) | rule #11 deletions fail command-not-found; agents fall back to `gio trash` (NEVER `rm`). env_doctor warns (non-fatal) when absent |
| PJM API key (Data Miner 2) | **single home: `FORGE/tools/market-data/.env` (gitignored)**, `PJM_API_KEY` | ❌ — **STILL ABSENT, re-confirmed 7/23 late-eve boot (env_doctor ✗, the box's one REQUIRED-missing)** — add: apiportal.pjm.com → Profile → Subscriptions → Primary key | ✅ added + **live-verified 7/16** (HTTP 200 on metadata + real rows pulled: PJM-RTO RT hourly LMP 7/15 15:00 = $195.14/MWh — the intraday-spike class the EIA proxy misses). Sub = "Data Miner 2 Non-Member" (free, 6 calls/min), header `Ocp-Apim-Subscription-Key` | WATT official-LMP leg dark; `power_watch.py` falls back to the lagged EIA proxy (blind to intraday spikes — the 7/12 class). Wiring into power_watch = WATT's named next increment (verified-hourly feed posts next-day ~11 AM; intraday = the 5-min feeds, same key) |
| FRED API key | **single home: `FORGE/tools/market-data/.env` (gitignored).** bashrc copies retired 7/2 — systemd units never read `~/.bashrc`, every loader falls back to the `.env`, and two homes = rotation drift (env_doctor flags bashrc copies) | ✅ `.env` only — **NEW key (swapped + FRED-validated 7/4)**; bashrc export line deleted 7/4 → single-home. Both machines now on the new key — only the GH secret + fred.org old-key deletion remain | ✅ `.env` only — **NEW key (created 7/2)**, env-stripped-verified 7/2 | all FRED pulls fail loud when absent (hardcoded copies scrubbed from 10 files 7/1, public-prep). **Rotation COMPLETE (7/4) ✅ — history-exposed key dead everywhere.** Desktop + laptop both on the new key. History log: (1) laptop — new key in `.env` + FRED-validated; `~/.bashrc` export line deleted → single-home; (2) RESEARCH-INTAKE GitHub Actions secret `FRED_API_KEY` swapped to the new key (web UI); (3) old key `8ce3f08d` (Feb-2026, history-exposed) DELETED at fred.stlouisfed.org. **Verified end-to-end:** the 7/4 `collect` run pulled 16 fresh FRED series (HY OAS 275 [7/2]) AFTER the old-key deletion = definitive proof the secret carries the new key. Pre-flip rotation item CLOSED |

## Switching checklist (Will)
1. **Leaving a machine:** close out every agent session (closeout runs `safe-push.sh`) → confirm `git status -sb` = `## master...origin/master` (0/0, nothing stranded).
2. **Arriving:** first session boots with `git pull --rebase` (standard boot step 0) — origin is the handoff point.
3. **Never run agent sessions on both machines simultaneously.** Serial operation is what makes the git layer safe (see root `CLAUDE.md` Git Protocol).

## Session diagnosis one-liners
```bash
python3 "$(git rev-parse --show-toplevel)/scripts/env_doctor.py"   # one-shot: keys + machine-local extras (PROME boot gate runs it --quiet)
hostname                                                  # which box am I on?
systemctl --user list-timers --all | grep -i liquid       # HY timer here?
ls ~/.config/kalshi/ 2>&1                                 # kalshi creds here?
ls -d ~/Research-Intake 2>&1                              # intake clone here?
```

## Standing rule
Anything new that lives **outside the repo** — a credential, timer, cron, local clone, backup, CLI tool an agent depends on — **gets a row here at creation time.** That's the price of admission for machine-local infrastructure. Prefer machine-independent homes (the RESEARCH-INTAKE GitHub-Actions pattern) for anything load-bearing between sessions ([[finding_passive_surface_rot_push_not_dashboard]]). **`scripts/env_doctor.py` (PROME boot gate) encodes the machine-checkable subset of this inventory** — when adding a required key or a desktop-expected item here, add it to the script's manifest too.
