---
name: finding_board_lags_agents_not_vice_versa
description: "On fast-moving domains the board/registry lags the domain agents; check a recipient's actual STATUS before directing them to \"go consume the board\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6ec8122a-82d2-47d6-9b00-c5bfbf473986
---

When deciding which agent has "unconsumed backlog" and should be sent to read the shared board (BOARD/SIGNALS/etc.), do NOT compute that from the registry's last-boot dates — those lag reality. On a fast-moving story the domain owners work AHEAD of the board through their own monitoring, so the board is archiving what THEY fed back, not informing them.

**Why:** WALTER 6/16/26 — Will asked which agents would most benefit from being directed to the board during the Iran de-escalation. The registry showed BRENT 6/9 / HAWK 6/8 with "BOARD pickup pending," so they ranked #1-2. But their actual STATUS files were 6/14 / 6/13, and both had already independently captured the MOU + re-marked scenarios (HAWK moved B-Deal-Reopen 12%→32% on 6/12) — more current than the signal WALTER was about to send them. Directing them to the board would have been reading their own better analysis back to them. 11 of 12 Tier-1 registry rows were stale by ~5 days.

**How to apply:** (1) Before any "go check the board" direction, READ the recipient's actual STATUS (git-commit date + lead), not the registry date. (2) "Direct to the board" pays off for OFF-axis agents with genuine stale backlogs (e.g. BOND, 2 unconsumed signals for 10 days) and cross-domain synthesizers (NEXUS) — not the domain owners of the hot story. (3) Refresh the registry against actual STATUS commit-dates at every boot/closeout; stale registry dates silently invert "who's ahead vs behind." Same family as [[feedback_check_recipient_before_sharing]] and [[feedback_check_domain_owner_before_messaging]] — one level up: the board itself can be the stale party.

## n+1, 2026-08-31 (WALTER) — the ahead/behind question is PER-LEG, not per-agent
The finding above says the board can be the stale party. The sharper form: **an owner can be simultaneously AHEAD of you on the facts and STALE on the premises its own marks rest on** — so grading the *agent* ("BRENT is current", "FALCON is behind") is the wrong unit. Grade **per leg**.

**WALTER, 2026-07-16.** The Iran 7d re-verify put me **level** with BRENT (7/16 — it had independently verified blockade/Belma/KOC/transits and reached identical *precision* reads: Belma = enforcement not a Kharg strike, KOC = borderline not a clean FAL-01, so a "correction" to BRENT would have been pure noise) and **ahead** of FALCON (7/12) on **exactly one datum**: Iran's 7/13 MFA MOU repudiation, which post-dated FALCON's whole session. But that one datum, plus the tape, had falsified **two premises FALCON's marks explicitly rested on** — *"oil still ~$76, decoupled"* (its **stated** single load-bearing reason D stays base-case-not-runaway) and *"MOU not formally rescinded"* (stated 4×, including a Diplomacy row whose named flip **literally is** "formal MOU withdrawal").

**The useful routing move was quoting each agent's own named flip conditions back at it and saying which fired** — while explicitly refusing to re-mark, because FALCON owns FAL-01 and its own marks.

**⇒ The highest-value thing a router can carry to a stale owner is not the news — it is WHICH OF THE OWNER'S OWN REGISTERED PREMISES THE NEWS BREAKS.** That is actionable in a way a headline never is, and it stays inside the router's lane.

**Corollary on triangulation:** a 4-day-old STATUS on a fast theater is stale enough to invert a base case. **Treat vintage as load-bearing when counting owners as "corroboration" — they are not independent when one is premise-stale.**
