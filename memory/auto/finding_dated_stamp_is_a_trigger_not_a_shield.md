---
name: finding_dated_stamp_is_a_trigger_not_a_shield
description: "A dated section stamp (\"as of 7/24\") functions as a shield that excuses stale rows; treat any stamp older than the previous session as a forced re-read-or-restamp (RED 20-item sweep, 7/31)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 82f86d84-3685-42a6-90f9-2b7b8add7baa
  modified: 2026-07-31T20:15:08.241Z
---

**The failure (RED, 2026-07-31 closeout sweep — 20 flagged items, one signature):** sections carrying honest date stamps — "COUNTER-SIGNALS (7/24 base)", "TOP ADVERSARIAL PRIORITIES (7/24)", "SKEW 145.95 (7/23)" — survived multiple write-back passes *because* they were dated. The stamp read as provenance ("this is honestly labeled as of 7/24") when it should have read as staleness ("this is 7 days old — re-pull it"). Costs found when the sweep finally re-pulled: a **live 2-of-4 falsifier clock** (SKEW <140, VIOLET kill line) masked for 8 days behind a "145.95 (7/23)" anchor; a pre-FOMC priorities section carried "still T-4, still pre-data" for two sessions *after* the meeting happened and was graded; two predictions displayed ACTIVE for 26 days after resolving.

**Why:** dating a value satisfies the letter of "stale-marked > carried-forward-as-current" while defeating its purpose — the mark makes the value *safe to skip* at review, so honestly-dated sections rot longer than undated ones. The failure mode is worst on surfaces the owner re-reads often: familiarity plus a visible date = "already handled."

**How to apply:** at every write-back, treat any section-header or anchor stamp **older than the previous session** as a mandatory action: re-pull and restamp, or freeze the section with an explicit FROZEN banner. Never leave a middle state where a date substitutes for a refresh. Mechanical form: grep your own state files for date tokens older than N days as a closeout step. Related: [[finding_status_spine_staleness_under_appended_top]], [[finding_banner_is_a_warning_not_a_fix]], [[finding_freshness_audit_vs_caught_up]], [[finding_plausible_stale_value_evades_review]].
