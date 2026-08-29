#!/usr/bin/env bash
# UserPromptSubmit hook — injects the wall clock into every prompt so stamps come
# from the clock, never the narrative (finding_write_timestamps_from_the_clock_not_the_narrative:
# session time-sense drifts ~2.5h under load). Will-approved 2026-08-29 ("approved go ahead").
# stdout of a UserPromptSubmit hook is appended to the model's context.
TZ=America/New_York date '+NOW: %a %Y-%m-%d %H:%M ET (clock, not narrative — stamp from this)'
