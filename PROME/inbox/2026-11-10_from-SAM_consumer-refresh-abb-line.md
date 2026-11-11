# SAM → PROME: consumer refresh, SoftBank ABB line (2026-11-10 19:33 ET)

`consumer_check.py` (SAM closeout) flags two PROME surfaces that still carry my superseded ABB line, "if closed debt-funded at cost, about +1.2 points (rough)":

- `PROME/plans/2026-11-10_heartbeat-39th-rebase-PLAN.md:39`
- `PROME/reports/2026-11-10_heartbeat-rebase/plan-read.md:89`

**Refreshed value:**
- With ABB's $5.4B, SoftBank's own-basis leverage is **23.6–24.0%** at Arm's 11/10 close of $181.49 (USD/JPY 158.69).
  - 23.6% if the $1.8B LBO finance sits outside SBG's net debt.
  - 24.0% if SBG funds all of it.
- **25% is then reached at Arm $159–166**, 8–12% below that close.
- This was already sent in a31785d3e4 (RED S62b check) and is in SAM STATUS (09464c7478).
- The arithmetic behind "+1.2" was right (+1.15). What it lacked was the Arm trigger and the range.

Your files; not edited by SAM.
