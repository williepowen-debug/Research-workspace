# MACHINE_LOCAL.md — What Does NOT Travel With The Repo
**Created:** 2026-07-01 (Prome; Will-approved) · **Owner:** PROME · **Update rule at bottom.**

**Why this exists:** Will runs **serial multi-machine** — one machine at a time (desktop ⇄ laptop), closing out + pushing all agents before switching. Git carries every repo file cleanly across that handoff. **Machine-local infrastructure does not travel**, and its absence masquerades as breakage: the 7/1 session burned real time discovering that "Kalshi broken" and "HY auto-watch dark" were location facts, not defects. This file makes that a 10-second diagnosis.

## Inventory
*Verified 2026-07-01 on hostname `WilliePOwen` (believed LAPTOP — Will to confirm/label). "Other box" = desktop, presumed.*

| Item | Path | This box (7/1) | Desktop | Consequence when absent |
|---|---|---|---|---|
| Repo venv | `.venv/` | ✅ | ✅ assumed | root-canon python tools fail (yfinance etc.); rebuild from `scripts/requirements.txt` + FORGE reqs |
| Telegram channel tokens | `~/.claude/channels/telegram*` | ✅ | ✅ assumed | WALTER/PROME Telegram delivery fails |
| Kalshi creds | `~/.config/kalshi/{key_id.txt,private_key.pem}` | ❌ | ✅ (worked 6/27) | ORACLE `kalshi.py` dies at import → Kalshi lane is desktop-only until creds copied (chmod 600, NEVER in repo) |
| `liquid-hy-watch` systemd timer | `~/.config/systemd/user/` | ❌ | ❓ Will to verify (`systemctl --user list-timers \| grep liquid`) | between-session HY auto-watch dark on this box. **Mitigated 7/1: RESEARCH-INTAKE lane is now the machine-independent PRIMARY** (intake `89b2e31`); timer = redundancy. WSL2 caveat: user timers don't fire with no WSL instance running — true on BOTH boxes |
| LIQUID alerts output | `AGENTS/LIQUID/alerts/` | ❌ (never fired here) | ❓ | timer alerts fired on one box are invisible from the other (local writes) |
| RESEARCH-INTAKE local clone | `/home/willi/Research-Intake` | ✅ (cloned 7/1) | ✅ | only needed to EDIT feeds — the lane itself runs on GitHub Actions, machine-independent by design |
| Pre-scrub mirror backup | `~/Research-workspace-PRESCRUB-BACKUP-20260630.git` | ❌ | ✅ (created there 6/30) | the history-scrub rollback net lives on the DESKTOP — locate it there before deleting post-public-flip |
| `gh` CLI | `gh` | ❌ | ❓ | GitHub API/PR ops unavailable; plain git works (credential store ✅ both boxes) |
| Git identity (fresh clones) | repo-local `user.name/email` | main repo ✅ · new clones ❌ until set | ✅ | commits in a NEW clone fail "empty ident" — set repo-local from the main repo (done for Research-Intake 7/1) |
| FRED API key | `~/.bashrc` export + `FORGE/tools/market-data/.env` (gitignored) | ✅ both (wired 7/1) | ❌ **Will: append the same 2 lines** (see below) | all FRED pulls fail loud (hardcoded copies scrubbed from 10 files 7/1, public-prep). Desktop one-liners: `echo 'export FRED_API_KEY=<key>' >> ~/.bashrc` and `echo 'FRED_API_KEY=<key>' >> FORGE/tools/market-data/.env`. **Recommend rotating the key** (free, fred.stlouisfed.org) — the old literal remains in git HISTORY |

## Switching checklist (Will)
1. **Leaving a machine:** close out every agent session (closeout runs `safe-push.sh`) → confirm `git status -sb` = `## master...origin/master` (0/0, nothing stranded).
2. **Arriving:** first session boots with `git pull --rebase` (standard boot step 0) — origin is the handoff point.
3. **Never run agent sessions on both machines simultaneously.** Serial operation is what makes the git layer safe (see root `CLAUDE.md` Git Protocol).

## Session diagnosis one-liners
```bash
hostname                                                  # which box am I on?
systemctl --user list-timers --all | grep -i liquid       # HY timer here?
ls ~/.config/kalshi/ 2>&1                                 # kalshi creds here?
ls -d ~/Research-Intake 2>&1                              # intake clone here?
```

## Standing rule
Anything new that lives **outside the repo** — a credential, timer, cron, local clone, backup, CLI tool an agent depends on — **gets a row here at creation time.** That's the price of admission for machine-local infrastructure. Prefer machine-independent homes (the RESEARCH-INTAKE GitHub-Actions pattern) for anything load-bearing between sessions ([[finding_passive_surface_rot_push_not_dashboard]]).
