# Claude Code Commands Reference

**Updated:** 2026-06-21

> Canonical agent folders remain flat at `~/Research-workspace/AGENTS/<NAME>/`. The new `_CREDIT.md`, `_NETWORK.md`, etc. files are indexes, not folders to cd into.

## Basic Agent Map

### Path model

Agents live in flat canonical folders:

```bash
~/Research-workspace/AGENTS/<NAME>/
```

Grouped files such as `AGENTS/_CREDIT.md`, `AGENTS/_ENERGY.md`, and `AGENTS/_NETWORK.md` are maps/indexes only. Do not `cd` into grouped subfolders; the active folders were not moved.

### Domain groups

**System / orchestration**
- PROME — chief-of-staff / orchestration / final synthesis
- WALTER — signal/news routing desk
- NEXUS — cross-agent synthesis
- RED — adversarial review
- DEWEY — deep research executor
- HERMES — signal carrier / inbox-outbox utility

**Credit / consumer / banks / CRE**
- LABOR — employment / claims
- CARL — consumer credit / housing
- REGINALD — regional banks
- OZK — OZK-specific bank work
- CORAL — Florida convergence
- CREED — national CRE / CMBS
- OTTO — auto / consumer delinquency
- REITS / DOC — background credit/CRE surfaces

**Private credit / insurance**
- BROCK — BDCs / private credit
- SHADE — PE-insurance-captive plumbing

**Funding / macro / market structure**
- HENRY — market structure / econ data
- LIQUID — funding / Treasury plumbing
- BOND — bond market structure / auctions / credit spreads
- SAM — Japan / BOJ / JGB / carry
- ZHAO — China / capital flows
- HANS — Europe / UST demand
- FOREX — FX background
- VIOLET — vol / VIX / credit-to-vol lag

**Energy / geopolitics / commodities**
- HAWK — geopolitics / military
- BRENT — oil / energy markets
- MARCO — migration / labor flows
- FERT — fertilizer / food security
- CRUISE — cruise / tourism canary
- BARON — Trump network / policy

**Research / trading / ops**
- ATHENA — reading / knowledge
- ORACLE — prediction markets
- TERRY — trade construction desk; proposes only
- BUFFER / EARNINGS / SENTRY / TRADES — ops, event, and trade-support surfaces

### Main transmission chains

```text
LABOR → CARL → REGINALD → repricing
CREED → REGINALD + CORAL + LIQUID + CARL
BROCK → SHADE → LIQUID
HAWK → BRENT → HENRY / LIQUID / CARL
SAM → LIQUID
BOND → LIQUID / HENRY / REGINALD
VIOLET watches credit-to-vol lag → HENRY / LIQUID / RED
NEXUS synthesizes cross-agent convergence and contradictions
```

### Launch caution

This reference is a menu, not a startup script. Launch agents one at a time when possible. Too many Claude Code agents can freeze the machine or cause plugin/resource contention.

## SYSTEM / ORCHESTRATION

### PROME

_Repo-native Prome surface. Not a siloed market-domain agent._

```bash
tmux new -s prome -d 'cd ~/Research-workspace/PROME && claude --dangerously-skip-permissions'
tmux attach -t prome
```

### WALTER

_Only Claude Code agent here using Telegram plugin._

```bash
tmux new -s walter -d 'cd ~/Research-workspace/AGENTS/WALTER && claude --channels plugin:telegram@claude-plugins-official --dangerously-skip-permissions'
tmux attach -t walter
```

### NEXUS

_Cross-agent synthesis._

```bash
tmux new -s nexus -d 'cd ~/Research-workspace/AGENTS/NEXUS && claude --dangerously-skip-permissions'
tmux attach -t nexus
```

### RED

_Adversarial analysis._

```bash
tmux new -s red -d 'cd ~/Research-workspace/AGENTS/RED && claude --dangerously-skip-permissions'
tmux attach -t red
```

### DEWEY

_Deep research executor / formerly RESEARCHER._

```bash
tmux new -s dewey -d 'cd ~/Research-workspace/AGENTS/DEWEY && claude --dangerously-skip-permissions'
tmux attach -t dewey
```

### HERMES

_Signal carrier / utility._

```bash
tmux new -s hermes -d 'cd ~/Research-workspace/AGENTS/HERMES && claude --dangerously-skip-permissions'
tmux attach -t hermes
```

## CREDIT / CONSUMER / BANKS / CRE

### LABOR

_Employment / claims._

```bash
tmux new -s labor -d 'cd ~/Research-workspace/AGENTS/LABOR && claude --dangerously-skip-permissions'
tmux attach -t labor
```

### CARL

_Consumer credit; Claude Code independent/siloed._

```bash
tmux new -s carl -d 'cd ~/Research-workspace/AGENTS/CARL && claude --dangerously-skip-permissions'
tmux attach -t carl
```

### REGINALD

_Regional banks; Claude Code independent/siloed._

```bash
tmux new -s reginald -d 'cd ~/Research-workspace/AGENTS/REGINALD && claude --dangerously-skip-permissions'
tmux attach -t reginald
```

### OZK

_OZK-specific bank agent; Claude Code roster._

```bash
tmux new -s ozk -d 'cd ~/Research-workspace/AGENTS/OZK && claude --dangerously-skip-permissions'
tmux attach -t ozk
```

### CORAL

_Florida comprehensive; Claude Code independent/siloed._

```bash
tmux new -s coral -d 'cd ~/Research-workspace/AGENTS/CORAL && claude --dangerously-skip-permissions'
tmux attach -t coral
```

### CREED

_National CRE / CMBS; Claude Code roster; explicit permission only._

```bash
tmux new -s creed -d 'cd ~/Research-workspace/AGENTS/CREED && claude --dangerously-skip-permissions'
tmux attach -t creed
```

### OTTO

_Auto / consumer DQ._

```bash
tmux new -s otto -d 'cd ~/Research-workspace/AGENTS/OTTO && claude --dangerously-skip-permissions'
tmux attach -t otto
```

### REITS

_REIT/CRE background._

```bash
tmux new -s reits -d 'cd ~/Research-workspace/AGENTS/REITS && claude --dangerously-skip-permissions'
tmux attach -t reits
```

### DOC

_Credit subdomain / background._

```bash
tmux new -s doc -d 'cd ~/Research-workspace/AGENTS/DOC && claude --dangerously-skip-permissions'
tmux attach -t doc
```

## PRIVATE CREDIT / INSURANCE

### BROCK

_BDC / private credit._

```bash
tmux new -s brock -d 'cd ~/Research-workspace/AGENTS/BROCK && claude --dangerously-skip-permissions'
tmux attach -t brock
```

### SHADE

_PE-insurance-captive._

```bash
tmux new -s shade -d 'cd ~/Research-workspace/AGENTS/SHADE && claude --dangerously-skip-permissions'
tmux attach -t shade
```

## FUNDING / MACRO / MARKET STRUCTURE

### HENRY

_Market structure + econ data._

```bash
tmux new -s henry -d 'cd ~/Research-workspace/AGENTS/HENRY && claude --dangerously-skip-permissions'
tmux attach -t henry
```

### LIQUID

_Funding / Treasury._

```bash
tmux new -s liquid -d 'cd ~/Research-workspace/AGENTS/LIQUID && claude --dangerously-skip-permissions'
tmux attach -t liquid
```

### BOND

_US bond market structure._

```bash
tmux new -s bond -d 'cd ~/Research-workspace/AGENTS/BOND && claude --dangerously-skip-permissions'
tmux attach -t bond
```

### SAM

_Japan / BOJ / JGB; Claude Code independent/siloed._

```bash
tmux new -s sam -d 'cd ~/Research-workspace/AGENTS/SAM && claude --dangerously-skip-permissions'
tmux attach -t sam
```

### ZHAO

_China / capital flows._

```bash
tmux new -s zhao -d 'cd ~/Research-workspace/AGENTS/ZHAO && claude --dangerously-skip-permissions'
tmux attach -t zhao
```

### HANS

_Europe / UST demand._

```bash
tmux new -s hans -d 'cd ~/Research-workspace/AGENTS/HANS && claude --dangerously-skip-permissions'
tmux attach -t hans
```

### FOREX

_FX background._

```bash
tmux new -s forex -d 'cd ~/Research-workspace/AGENTS/FOREX && claude --dangerously-skip-permissions'
tmux attach -t forex
```

### VIOLET

_Vol / VIX / credit-to-vol lag._

```bash
tmux new -s violet -d 'cd ~/Research-workspace/AGENTS/VIOLET && claude --dangerously-skip-permissions'
tmux attach -t violet
```

## ENERGY / GEOPOLITICS / COMMODITIES

### HAWK

_Geopolitical / military._

```bash
tmux new -s hawk -d 'cd ~/Research-workspace/AGENTS/HAWK && claude --dangerously-skip-permissions'
tmux attach -t hawk
```

### BRENT

_Oil / energy markets._

```bash
tmux new -s brent -d 'cd ~/Research-workspace/AGENTS/BRENT && claude --dangerously-skip-permissions'
tmux attach -t brent
```

### MARCO

_Migration / labor flows._

```bash
tmux new -s marco -d 'cd ~/Research-workspace/AGENTS/MARCO && claude --dangerously-skip-permissions'
tmux attach -t marco
```

### FERT

_Fertilizer / food security._

```bash
tmux new -s fert -d 'cd ~/Research-workspace/AGENTS/FERT && claude --dangerously-skip-permissions'
tmux attach -t fert
```

### CRUISE

_Cruise / tourism canary._

```bash
tmux new -s cruise -d 'cd ~/Research-workspace/AGENTS/CRUISE && claude --dangerously-skip-permissions'
tmux attach -t cruise
```

### BARON

_Trump network / policy._

```bash
tmux new -s baron -d 'cd ~/Research-workspace/AGENTS/BARON && claude --dangerously-skip-permissions'
tmux attach -t baron
```

## RESEARCH / LEARNING / OPS / TRADING

### ATHENA

_Reading / knowledge._

```bash
tmux new -s athena -d 'cd ~/Research-workspace/AGENTS/ATHENA && claude --dangerously-skip-permissions'
tmux attach -t athena
```

### ORACLE

_Prediction markets._

```bash
tmux new -s oracle -d 'cd ~/Research-workspace/AGENTS/ORACLE && claude --dangerously-skip-permissions'
tmux attach -t oracle
```

### TERRY

_Trade construction desk; proposes only._

```bash
tmux new -s terry -d 'cd ~/Research-workspace/AGENTS/TERRY && claude --dangerously-skip-permissions'
tmux attach -t terry
```

### BUFFER

_Ops/background._

```bash
tmux new -s buffer -d 'cd ~/Research-workspace/AGENTS/BUFFER && claude --dangerously-skip-permissions'
tmux attach -t buffer
```

### EARNINGS

_Event-driven earnings._

```bash
tmux new -s earnings -d 'cd ~/Research-workspace/AGENTS/EARNINGS && claude --dangerously-skip-permissions'
tmux attach -t earnings
```

### SENTRY

_Ops/sentry._

```bash
tmux new -s sentry -d 'cd ~/Research-workspace/AGENTS/SENTRY && claude --dangerously-skip-permissions'
tmux attach -t sentry
```

### TRADES

_Trade artifacts surface._

```bash
tmux new -s trades -d 'cd ~/Research-workspace/AGENTS/TRADES && claude --dangerously-skip-permissions'
tmux attach -t trades
```

## TMUX BASICS

Detach without killing the session:
Ctrl+B  then  D

List all tmux sessions:
tmux ls

Attach to a session:
tmux attach -t <name>

Kill one agent:
tmux kill-session -t <name>

Kill all tmux sessions at once (nuclear option):
tmux kill-server

Kill zombie Telegram processes from uncleanly-shutdown agents (do NOT run while agents are active):
pkill -f "bun.*server.ts"

Check for zombie bun processes before running that:
ps aux | grep "bun.*server.ts"

## PATH NOTES

Canonical agent paths remain flat even though grouped index files now exist:
~/Research-workspace/AGENTS/<NAME>/

Grouped files such as AGENTS/_CREDIT.md and AGENTS/_NETWORK.md are navigation/index files only. Do not cd into grouped subfolders; active agent folders were not moved.

REGINALD/CARL/CORAL/CREED/SAM/RED/OZK are Claude Code roster/independent surfaces. Prome should not casually spawn REGINALD, CARL, or CREED; CREED requires explicit Will permission before any spawn-like work.

WALTER should remain the only Claude Code agent launched with the Telegram plugin in this reference.

## DNS (Now Locked)

DNS is permanently locked to 8.8.8.8 via chattr +i. You no longer need to run the old echo-nameserver command after reboots. If something goes wrong:

Check current DNS:
cat /etc/resolv.conf
# Should show: nameserver 8.8.8.8

Unlock and reset (only if DNS is broken):
sudo chattr -i /etc/resolv.conf
sudo sh -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo chattr +i /etc/resolv.conf

## VPS / Prome Quick Reference

ssh moltbot@100.86.70.6
systemctl --user restart openclaw-gateway
systemctl --user status openclaw-gateway
openclaw gateway status
tail -50 /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log
openclaw cron list

## Troubleshooting Cheat Sheet

Agent won't boot: probably resource contention. Wait, then try one at a time.
"Unable to connect to API": check DNS with cat /etc/resolv.conf.
Agent frozen / can't scroll: Ctrl+B then [ to scroll, q to exit. Or mouse scroll.
tmux session stuck: tmux kill-session -t <name> and relaunch.
Zombie bun processes: pkill -f "bun.*server.ts" only when no agents are running.
Computer freezing: too many agents. Kill idle ones with tmux kill-session -t <name>.
Telegram plugin dropping messages: known bug. WALTER should be the only Claude Code agent using Telegram.

## File Locations

Agent working dirs: ~/Research-workspace/AGENTS/<NAME>/
Telegram bot tokens: ~/.claude/channels/telegram-<name>/.env
Tmux config: ~/.tmux.conf
Start script (not currently used): ~/start-agents.sh
Claude Code global settings: ~/.claude/settings.json

## Career Launch Cheat Sheet

Start:
cd ~/career-launch
git pull
claude
Tell Claude: "Read HANDOFF.md — continuing the career project."

Check:
git status
git log --oneline -5
ls -la

Save:
git add .
git commit -m "short description of what changed"
git push

Gotchas:
- Run git commands from inside ~/career-launch.
- Run commands one at a time if terminal is flaky.
- Never commit/publish the _private/ folder.

Repo:
GitHub: https://github.com/williepowen-debug/career-launch
Local: ~/career-launch
