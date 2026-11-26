# VIOLET -> PROME: Will's evening ask (options 1 and 3), delivered

**Date:** 2026-11-25, 20:04 ET. Will typed it in the VIOLET session at 19:58 ET ("Yes go ahead"). This is direct operator work, not a DOCKET row.

- **Study 1 (sticky credit after a VIX fade):** covers 29 spikes since 1990. Sticky credit is the normal state after a peak (18 of 29) and does not predict a second leg (6/18 against 2/7); it predicts a slower fade. The peak-scaled prediction 2' held 5 of 10 in comparable sticky cases, so my unscored fail view moved from 88% to about 75%.
- **Study 3 (VIX options):** put open interest grew 4.6 times as much as call open interest over 11/23 and 11/24; put volume on 11/25 was 1.4 times calls (Dec) and 2.3 times (Jan). The flow leans to the fade; its direction is not established.
- **Corrected in place:** both Artifacts (cheat-sheet version 18, Operating Picture version 20) and the NEXUS_BRIEF line. TERRY received a short addendum.
- **Own-script defect:** an after-hours `vix_options.py` run wrote OI 0 over good OI. I restored it by hand; the fix is queued (STATUS queue 7).
- **Partial History check at 18:44 ET:** 11/25 VIX9D, VIX3M, VIX6M and VVIX are on Cboe History and match the print. VIX and SKEW are not posted yet.

## COMPLETION — VIOLET — 2026-11-25
STATUS: COMPLETE
CHANGED: research/2026-11-25_sticky-credit/, KB-VIO-410, STATUS, SCRATCH, NEXUS_BRIEF, VIX_OPTIONS (11/25 volumes), two Artifacts, TERRY addendum
RESULT: sticky credit, new peak within 20 sessions 3/18; peak-scaled 2' held 5/10; 2' fail view 88% to about 75%; put OI +260,435 vs calls +56,224
GAPS: no long free HY series (FRED truncated to 2023), so Baa-10Y stands in; options volume does not show buyer or seller
WILL_NEEDS: none
FOLLOW-UP: 11/27 Cboe confirmation; vix_options OI-zero fix; 12/10 test window
