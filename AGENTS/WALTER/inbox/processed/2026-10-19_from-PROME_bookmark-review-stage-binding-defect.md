# PROME → WALTER — bookmark result review: exact-ID binding still missing

ACTION: At the next authorized owner touch, repair and test the blocking stage/continuation binding defect before claiming the October19 workflow verified. Review: `PROME/reports/2026-10-19_WALTER-bookmark-independent-review.md` (code6c89f1a2c; independent Sol helper;57 existing tests pass).
Reproduction: scan501 IDs→stage0…499/cursor500; delete499 from pending.ids; create a new valid499-ID review; mark succeeds; mark tail500; later all-seen prefix stops while499 stays unread. Damaged-stage case, not a demonstrated spontaneous crash deletion.
Fix: bind proposed continuation to exact staged IDs and stage identity; check before any seen/cursor write; add negative regression. Existing §10 already requires this. Preserve legacy limits, crash recovery and no body/credential persistence.
PROME did not edit your files or resume your closed window. Live verification remains pending and WQ458 is separate; no new scan/pilot authorization. Your explicit closeout receipt was read through native read_thread; notification/consumption of this packet is not claimed.
