# finding_expected_window_rederived_from_now_drifts

**Origin:** FALCON, 2026-08-06 commissioned session (Will-directed 8/6 commit-review R2 caught it). Leg-3 Yanbu w/c-7/27 tracker-print "expected relay window" was projected three times across three sessions — 8/2: "8/4-5" · 8/4: "~8/5-8/7" · 8/5: "~8/6-8/10" — each shift unflagged. The written rule ("prints relay 4-8 days after week-end") also contradicted its own evidence: the 4-8 figure had been computed from the week's START and mislabeled; counted from the week's END the observed relays would precede the week's own end.

**The failure shape:** an expected-publication (or expected-event) window that each session re-derives from *now* ("it hasn't landed, so it must be coming — call it tomorrow through tomorrow+N") instead of from a pinned anchor. Locally every restatement looks reasonable; globally it is a ratchet that can never rule an absence OVERDUE — which defeats the window's entire purpose, since the window exists to convert absence into information at a pre-committed point. Same family as goalpost drift on thresholds, but on the TIME axis, and invisible from inside any single session because each session sees only its own projection.

**The fix:**
1. Derive the window ONCE from a PINNED anchor, and name the anchor explicitly (period-start vs period-end vs publication event). For periodic data, the period-END is the only well-formed anchor — a full-period print cannot precede its period's end (that impossibility is also the fastest audit: if the observed lags would put relays before the anchor, the anchor is mislabeled).
2. Write the window down with its observation count (n) and thereafter only CONSUME it — an empty look inside the window is waiting; an empty look past it is OVERDUE, a finding about the channel (news-cycle displacement, mild-print bias — dramatic prints get relayed, "unchanged" doesn't — or source-quality collapse), never silently "not yet."
3. If the window must move, the move is itself a flagged event with a stated cause — never a silent restatement in the next session's report.

**Transfer:** applies to any agent grading an instrument on third-party publication cadence (tracker weeklies, agency releases, insurer re-rates, earnings): pin the anchor, log the observed lags, pre-commit the overdue line.
