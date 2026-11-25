COLDREADER · /home/willi/Research-workspace/AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md · focus: header, §4.1 (+4.1-R), §4.4, §4.6, amendment 11 (read whole, line numbers from the file)

HEADLINE: no ❌ found. The two exceptions are written in consistently where they were applied (L106, L107, L109, L133, L135). 12 ⚠️ remain, mostly where untouched wording still presumes a refresh, or where the exceptions leave a trigger undefined. Strongest: Q1-1 (As-of meaning), Q1-2 (who runs the pin check), Q1-4 (packets/rotation vs "only when"), Q1-7 (rollout can stall).

## Q1. Does the standard read consistently?

1. ⚠️ L30, L84, L106 · "**As of:** YYYY-MM-DD HH:MM ET | STATUS commit: `<hash>`" vs "A session that changes none of those leaves the brief untouched: no As-of or pin refresh"
   Why: As-of no longer says "I checked this on date X". It says "last date a figure/threshold/send/wait changed". Nothing in the template or §4.4 tells a consumer that. A reader will take an old As-of as a stale brief, or take a recent one as a currency attestation.
   Fix: one clause at L30 or §4.1: "As-of = date of last content change, not a freshness attestation."

2. ⚠️ L107 vs L109 vs L133 · L107: "when `scripts/brief_pin_check.py` reports a desk's brief pin as PIN-UNRESOLVED ... the desk corrects the pin at that closeout". L109: "it is never shipped as an added closeout step in any desk's instructions". L133: "NEXUS compares the pinned STATUS hash ... and reports".
   Why: (i) The file never says who runs the checker, or how the desk learns of PIN-UNRESOLVED before closeout. (ii) A desk-side "correct at closeout when reported" is a closeout duty, yet L109 says Amendment 11 is never an added closeout step. (iii) PIN-UNRESOLVED is defined only as "pinned hash is not a commit that touched that desk's STATUS". Its relation to "UNPINNED / pointer-valued / NONE (reason)" (L138) is not stated.
   Fix: name the reporter and delivery channel, and say the repair is report-triggered, not a standing closeout step.

3. ⚠️ L107 · "A pin that merely lags is still only reported (§4.4), never re-pinned."
   Why: "never re-pinned" is absolute. L109 and L114 require a re-pin at a §4.1 rewrite and say a rewrite conforms "at its NEXT re-pin". A literal reader may think a rewrite must leave a lagging pin alone.
   Fix: "never re-pinned on its own (a §4.1 rewrite still pins to STATUS HEAD)".

4. ⚠️ (leaning ❌ if a desk obeys literally) L106, L116, L143 · L106: "rewrites and commits its brief at closeout only when a figure, threshold, or cross-desk send or wait in it changed". L116: "NEXUS packets ONLY desks whose non-conformance is currently LOAD-BEARING: the byte offset of `## CROSS-DOMAIN` exceeds ... 54,250 B". L143: "A brief over budget is the owner's to rotate".
   Why: A reorder (A12) or a rotation is a brief commit with no figure/threshold/send/wait change. "Only when" has no exception for them. A desk receiving a NEXUS packet or a budget flag cannot tell whether it may or must commit.
   Fix: add "or an amendment-conformance reorder or budget rotation requested under §4.1-R / §4.5" to the permitted triggers.

5. ⚠️ L106 · trigger set is "figure, threshold, or cross-desk send or wait".
   Why: nothing says whether these change the brief: Status emoji/claim, "Recent thesis pivot" (REQUIRED line), a CALIBRATION conviction letter, a "Cross-agent tensions" change, VIEW wording, or NEXT DECISION POINT. A desk with a thesis pivot but no figure change could be "untouched", leaving the REQUIRED pivot line wrong. "Figure" is also undefined (any number in the brief? only STATUS-derived?).
   Also L133 says "committed only when its content changes" and L114 says "whenever brief content changes". "Content" is broader than the four-item trigger in L106.
   Fix: use one trigger phrase everywhere, or state whether "content" is meant to be broader than the four items.

6. ⚠️ L106 · "A STATUS change that moves any of those updates the brief the same session." vs "at closeout" (same sentence) and amendment 10 (L108: brief fold is the LAST write-back).
   Why: "same session" could be read as mid-session, which L108 calls the dominant staleness mechanism. A STATUS change made by another desk or a later session is not covered.
   Fix: "...at that session's closeout fold".

7. ⚠️ L113–L116 (§4.1-R) · "in force when every full-variant brief conforms" and TRIGGER "each desk conforms at its NEXT re-pin ... A desk is non-conformant only after its next re-pin."
   Why: under on-change commits, a desk with an unchanged brief never re-pins, so A12 may never reach "every brief conforms" and its protection stays ZERO indefinitely. "Re-pin" now covers two different acts (a rewrite, and the WQ-721 pin repair). The pin repair is "no other change", so it cannot deliver A12 conformance, but the text does not say so.
   Fix: say that only a §4.1 rewrite counts as the "next re-pin", and that escalation (L116) is the only path for unchanged briefs.

8. ⚠️ L137 vs L107 · L137: "grandfathered and must NOT be rewritten; any checker accepts all four until the owner next touches the header". L107: "the desk corrects the pin".
   Why: a pin repair edits the pin line. It is not stated whether it must preserve the legacy token form. "Until the owner next touches the header" may now never happen. L138 "owed at the owner's next fold" is also a dead-letter obligation for a desk with no trigger: an UNPINNED or NONE pin is not clearly covered by WQ-721 (which says "pinned hash is not a commit...").
   Fix: "repair changes the hash only, keeps the token form"; state whether UNPINNED briefs are covered by the L107 repair.

9. ⚠️ L152 vs L108/L114/L133/L135 · "WQ-719 A (12:10 ET): the brief-on-change edit to §4.1, amendment 11's wording and §4.4 (a)".
   Why: the same ruling's effects also appear in amendment 10 (L108 "in a session that writes the brief at all"), §4.1-R TRIGGER (L114), the §4.4 pin-lag paragraph (L133) and the carve-out supersession (L135). The scope list names only three places. "approves that change only" makes the boundary matter. Separately, L6 still describes the amendment-11 carve-out as "written in below, as ratified", while L135 now says it is superseded.
   Fix: list all touched places in L152, or say "and conforming edits".

10. ⚠️ L107 and L152 · authorising words and a live conditional.
   Why: L107 quotes the authority as "721 yes right?  No brainer?", which reads as a question. L152 says "the edit is reverted if he withdraws on that ground" and that the cap fact was not in the block he answered. A cold reader cannot tell whether the condition is still open or was resolved. "pointer-only pin repair" (L152) is also unclear against L107's "corrects the pin to its STATUS HEAD".
   Fix: add a state token (OPEN / not withdrawn as of <date>) and define "pointer-only" in one clause.

11. ⚠️ L5 vs L151 · L5: "No amendment is pending and none may be proposed — see §4.6." L151: "the first change that would have been amendment 13 re-opens the whole schema ... (R4)".
   Why: "may not be proposed" vs "a proposal triggers an R4 sitting". L1 and L152 record two exceptions but L5 (the Status line) does not mention them.
   Fix: "none may be proposed except via R4 (§4.6)".

12. ⚠️ L109, L106, L133 · "STATUS HEAD" is never defined.
   Why: a reader must infer it means the latest commit touching `AGENTS/<DESK>/STATUS.md` (L107 gives only an indirect hint). A different reading, repo HEAD or last commit by that desk, is possible.
   Fix: define once at L30.

## Q2. Instructions that still assume every-session rewrite / As-of bump / pin refresh

No hard instruction found. Checked every occurrence of closeout, write-back, fold, session, each pass, cycle, re-pin, As of and pin in L1–L158, including the template blocks (L23–L88). Residual wording that presumes a refresh:

- ⚠️ L96 · "'None active this cycle' forces the look each pass."
  Why: the rationale assumes a per-pass review of the brief. Under L106 the brief is untouched, and a tension change is not a rewrite trigger (see Q1-5). L56 repeats "this cycle".
  Fix: "forces the look when the brief is written".
- ⚠️ L3 · "ordering invariant (brief fold = the session's LAST write-back, amendment 10)".
  Why: stated unconditionally. L108 qualifies it with "in a session that writes the brief at all". A reader of the ownership paragraph alone would infer every session writes.
  Fix: add "when written".
- ⚠️ L71 and L99 · "FORWARD CATALYSTS (next 2-4 weeks)" and "2-4 weeks forward, 3-6 rows"; L40 "Expected by"; L65 "When".
  Why: these are rolling or dated fields that decay with the calendar, not with a figure change. A past date is not a trigger under L106, and L134 (a) flags only disagreement with STATUS. The 2–4 week window is silently violated on an untouched brief.
  Fix: state that dated rows may age until the next on-change write, or add "date passed" as a trigger.
- ⚠️ L114, L137, L138 · "NEXT re-pin", "until the owner next touches the header", "owed at the owner's next fold". These are conditional on a commit that may never occur (see Q1-7, Q1-8). They do not require every-session action; they are dead-letter obligations.

## Could not verify from this file alone
- `scripts/brief_pin_check.py`: whether it emits "PIN-UNRESOLVED" and "N commits behind", who runs it, and how it reports to desks (not opened).
- `PROME/WILL_QUEUE.md` rows 719 and 721, and whether WQ-720 A (quoted in L106's verbatim "719 A, 720 A approved") touches this file.
- Whether `NEXUS_BRIEF_TEMPLATE.md`, `AGENTS/NEXUS/BRIEFS_MAP.md` legend, NEXUS charter BOOT 6 and per-desk instructions still carry every-session wording (the schema says it wins on disagreement, L8 and L135).
- Whether Will has withdrawn WQ-721 A on the cap-fact ground (L152).
- That root Git Protocol makes the "subject's desk prefix" name the commit author (L109); the cold-archive §A13 content, decision rows, and the 54,250 B READ_CAP figure (L116) versus the 32,550 B figure (L143); the cap number/amendment-count claims.
- No pointers were tested with `ls` (the task was scoped to the single file).
