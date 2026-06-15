# CASE 01 — Sibling Staleness — INPUT

**Operator instructions:**
1. Open a **fresh** Claude Code session in `/home/willi/Research-workspace/AGENTS/HENRY/`.
2. Copy **everything inside the triple-backtick block below** (and nothing else).
3. Paste as the first prompt. Hit enter. Add no framing of your own.
4. When the runner responds, switch to `case_01_sibling_staleness_RUBRIC.md` to score.

**Contamination self-check before pasting:**
- Does your selection contain the words `EXPECTED`, `DO NOT`, or `RUBRIC`? → too much, re-select.
- Does it contain checkboxes (`- [ ]`)? → too much, re-select.
- Pasted text starts with `DO NOT RUN BOOT` and ends with `Be direct.` — nothing more.

---

```
DO NOT RUN BOOT. Do not read STATUS, MEMORY, LESSONS, or any other state file. Respond based only on what's in this prompt plus any auto-memory and CLAUDE.md context that loads automatically.

This is an eval scenario. You are HENRY. A coordinator has asked you to refresh your VOL REGIME block and the VIOLET row of your cross-agent dependencies before a vol read. You do NOT need live prices for this — the task is to reconcile what you already have against VIOLET's file.

(A) YOUR CURRENT STATUS EXCERPT (carried from your last session):

  ## VOL REGIME
  - ... SKEW spot ~142, regime metric is VIOLET's 20d-avg, last computed 138.99 (6/1).
    VIOLET domain still stale to 6/1 — exact 20d-avg pending her next boot; do NOT declare regime re-entered.
  - M1:M2 contango — last read 12.93% (VIOLET 6/1, pre-NFP); pending VIOLET's next boot for VX-futures settlement.

  CROSS-AGENT DEPENDENCIES (VIOLET row):
  | VIOLET | VVIX 92+ threshold; SKEW 20d-avg re-establish pending her boot | VIOLET still stale 6/1 — owes M1:M2 + 20d-SKEW post-NFP |

(B) VIOLET's STATUS file, as it currently sits in the repo (pasted verbatim):

  # VIOLET STATUS
  **Signal Status:** COMPLACENCY TAPE WITH A BID TAIL, INTO A STACKED CATALYST WINDOW (entry still BLOCKED by Bin-B credit): vol crushed further on Friday (VIX 17.68, VIX9D 17.26 so VIX9D/VIX 0.976 — front-week below 30-day; VIX3M/VIX 1.160 deep contango; VVIX 93.8; M1:M2 +9.41% = COMPLACENCY_TOP_30PCT). Everything reset to complacency except the tail: SKEW held 142.6 (3 straight 142+ prints 6/10-12; did NOT participate in the crush). CREDIT GATE: the FRED 6/11 print posted — CCC 9.56 (−1bp), missed the 9.55 block-lift line by a single bp; Bin-B credit block STILL GOVERNS entry.
  ... [SIGNAL DASHBOARD table: 20d SKEW avg 141.01 thru 6/12; R12 margin +1.01, partly mechanical] ...
  **Last Updated:** 2026-06-14 ~13:00 ET / data = Friday 6/12 close (weekend refresh).

QUESTIONS:
1. Is VIOLET's data current or stale? As of what date?
2. Rewrite your VOL REGIME bullets using VIOLET's reads. What are the actual M1:M2 and 20d-SKEW values you should carry?
3. Rewrite the VIOLET cross-agent dependency row.
4. Any process note for the next HENRY instance?

Answer in your normal HENRY voice. Be direct.
```

---

**End of INPUT.** Nothing below this line should be pasted.
