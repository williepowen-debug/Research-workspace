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
