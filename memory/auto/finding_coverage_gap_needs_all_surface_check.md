---
name: finding-coverage-gap-needs-all-surface-check
description: Never declare a coverage/blindness gap from one surface — check every collection mechanism (queries AND feeds AND entities AND human channels); 5 same-day instances, all caught pre-ship; corollary — keep watch-query edits direction-neutral
metadata:
  type: feedback
---

On 2026-07-16, PROME and WALTER produced **five** wrong "X is uncovered/blind" claims in one day, every one from checking a single surface: WALTER×3 (agents "truly blind" — but Will's Telegram drops covered the domains 5-for-5; "11 uncovered" — tags ≠ collection; "VIOLET uncovered" — the cftc_cot FEED was its lane, only newsweep queries were checked) and PROME×2 ("BOND has no auction coverage" — the treasury_auctions feed existed; the VIX narrowing below). All five were caught by the other party before shipping.

**Why:** a collection system has multiple mechanisms (news queries, dedicated feeds, entity lists, human drop channels, the agent's own in-session pulls). Any one surface can show a zero while another covers the domain. A gap claim from one surface reads as rigorous (it cites a grep) and is still wrong.

**How to apply:** before asserting "no coverage / blind / missing," enumerate EVERY collection mechanism and check each (for RESEARCH-INTAKE: `GOOGLE_NEWS_QUERIES` + all `fetch_*.py` feeds + entity/keyword lists + Will's drop channel). Encode monitoring checks with the all-surfaces predicate (the 7/16 doctor checks: FEEDS+QUERIES vs canonical ROSTER). State the narrow true claim ("no autonomous lane collection") not the broad false one ("agent is blind"). **Corollary (the 5th instance):** when narrowing a watch query to cut flood, keep it DIRECTION-NEUTRAL and check registered triggers first — PROME's "VIX spike OR surge" would have blinded RED-FT-06 (VIX <16, live) because vol regimes fail in both directions. Related: [[finding_comprehensive_grep_over_sampling]], [[finding_declared_data_wall_needs_fleet_memory_check]].
