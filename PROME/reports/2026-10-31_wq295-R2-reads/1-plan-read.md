COLDREADER · /home/willi/Research-workspace/PROME/proposals/2026-10-31_wq295-R2-encode-RULED.md · 12190 B (wc -c via measure.py semantics; re-measured at write time) · 50 claims
SCORE: 26/50 ✅ · 21 ⚠️ · 3 ❌
Plan read 1 of the episode · written 2026-10-31 13:38 EDT · read-only: nothing in the repository was written; helper files are listed at the end and live in this scratchpad.

SCOPE NOTE. The working tree was NOT quiet during this read (see ⚠️ 47). Where I quote the in-progress tool it is labelled "draft tool" and is evidence on whether the plan is implementable, not part of the artifact. Claims about EXISTING behaviour were checked against `git show HEAD:PROME/tools/spawn_list.py`.

════════════════════════ ❌ (would make the encode wrong / a live instruction false), ranked ════════════════════════

❌ 15  Dropped ruled limits: the inserted texts are less than the rule § 1 itself calls binding.
   claim → § 3a, § 4, § 6 encode "the rule as ruled".
   Quote A (record L9, § 1): "A cadence wake never grades anything on the desk's behalf and never marks a BOARD item consumed."
   Quote B (record L23, § 3a, all the charter says the wake IS): "it is a Tier-1 `CADENCE-DUE` wake — L0 drain plus a cadence self-check, beside dated rows, never instead."
   checked → grep -n -i 'grade|consum' on the record: L9 (the limit) and L51 ("consumers", A11) only; L23, L28-30, L36 carry neither limit. DOCKET L581 "Done when": "the four surfaces carry the rule and riders in Will's ruled form". Proposal R2 letter (L12) is where the limit comes from; its DISPOSITION note (L3) says the 10/1 approval governs.
   saw → nothing PROME acts on (charter, AUTONOMY, DAEDALUS spec) tells a woken desk, or PROME's spawn prompt, that BOARD items stay unconsumed or that PROME grades nothing on the desk's behalf. No § 7 condition tests it.
   change → add the sentence verbatim to § 3a and § 6; § 7 gets a condition that the cadence assignment text carries it.

❌ 16  Rider ③'s destination dropped: ruled "surfaced in the boot report", encoded as "reported".
   Quote A (record L7): "③ an EVENT-DRIVEN desk with no dated row for ≥14 days is surfaced in the boot report as UNREACHED (not woken)."
   Quote B (record L23): "An EVENT-DRIVEN desk with no such row is reported UNREACHED"; (L30) "EVENT-DRIVEN desks with no such row are reported UNREACHED".
   checked → "boot report" occurs once in the record (L7). BOOT.md step 8 "Required operational accounting" (L74), CLOSEOUT.md and the boot SKILL contain no UNREACHED / CADENCE-DUE (grep count 0 / 0 / 0). The only delivery the plan names is the gate line (`summarize_spawn_list`, § 5), which BOOT.md never requires the report to relay. DOCKET L581: "Done when: ... the first boot report shows the UNREACHED list." A11 stops at the gate summary.
   saw → mitigation exists but outside the ruled surfaces: the draft tool's gate hint string says "name them in the boot report". The schedule's purpose clause for rider ③ ("so its owner registers a row or PROME asks") is also gone, so UNREACHED has no stated action.
   change → say "surfaced in the boot report" plus the purpose clause in § 3a and § 4b; add a § 7 condition that the boot report lists UNREACHED (L581 done-when).

❌ 17  "PENDING dated row" / "PENDING dated DOCKET/GATES row" names a state GATES rows never have.
   Quote A (record L12, § 2): "PENDING DOCKET rows and LIVE GATES rows due on or before as-of +14 days".
   Quote B (record L36, § 6): "with no PENDING dated DOCKET/GATES row naming it first owner"; (L23, § 3a) "with no PENDING dated row naming it first owner".
   checked → GATES.tsv state first-tokens: LIVE 24 · RESOLVED(TERMINAL) 2 · RETIRED(TERMINAL) 1, zero PENDING. The live neighbour (PROME/CLAUDE.md L49) writes "a PENDING DOCKET row ... or LIVE GATES row" and `collect()` takes both.
   saw → read as its neighbour reads, § 3a counts DOCKET rows only: a desk with a LIVE gate inside 14 days gets a cadence wake AND its gate wake (the "two wakes, not one" A3 forbids). § 6 would hand DAEDALUS a spec whose GATES leg is empty.
   change → "no open dated row (PENDING DOCKET or LIVE GATES) naming it first owner ..." in §§ 3a, 4b and 6.

════════════════════════ ⚠️ (fix or declare in § 9), ranked ════════════════════════

⚠️ 18  "launchable" (L23, L36): defined only in § 2 L16.
   claim → ROSTER class ACTIVE / TIER-2 / SPECIAL, `spawn_slate.LAUNCH`.
   checked → spawn_slate.py L52 LAUNCH; ROSTER L156-157, L126; draft-tool dry run 10/31.
   saw → a stranger reads it as "no live session" (silent skip instead of doorbell) or "technically spawnable" (wake a DORMANT desk). By class alone it admits desks the ROSTER bars: the dry run names CATO ("Never launched by PROME", ROSTER L157) and RAV (Will-driven, L156) as CANNOT-EVALUATE at every boot, forever; CREED's row (L126) says "launch only on Will's explicit permission"; OTTO (TIER-2, "spawned as needed", declared WEEKLY 9/28) would age-wake, though the 9/26 schedule Will approved had 36 desks and none TIER-2.
   change → define it in § 3a; a desk whose ROSTER row bars PROME launch is named, never woken; declare the TIER-2 inclusion as PROME's reading.

⚠️ 19  "naming it first owner" (L23, L36) is code, not charter language.
   claim → first owner governs; a second owner does not (A4).
   checked → spawn_list.owner_token = first desk token of the owner cell, role words ignored ("HANS (owner) / PROME (consumer read)" → HANS); spawn_slate L628 "spawn_list reads the FIRST owner only"; end-to-end run (E3).
   saw → a literal "no dated row" counts any naming, so the reading ADDS wakes; a human reading "HENRY (consumer read) / TERRY (owner)" says TERRY, the tool says HENRY. § 2 L12 calls this "exactly how the 9/26 schedule Will saw was computed", but the schedule's header says only "naming each desk ... (spawn_list.collect, horizon 14)" and its script `r2_schedule.py` ("session scratchpad") is in neither git nor /tmp (SEARCH-NOT-FOUND). That Will "saw" it is asserted; 9/26 SCRATCH shows PROME produced it at his 15:04 ask.
   change → one-clause gloss in § 3a; § 2 says "consistent with collect()'s first-owner reading", not "exactly".

⚠️ 20  "+14 days (overdue included)" (L23): 14 is not ruled for WEEKLY/MONTHLY.
   claim → governing window = as-of +14d.
   checked → schedule L60 "The 14-day window was chosen to show two full weeks of WEEKLY clocks"; HEAD collect() `if due > horizon` (day 14 in, day 15 out); rider ③ wording "for ≥14 days"; draft selftest.
   saw → the number is rider ③'s and the demonstration's window, promoted to a rule parameter. A past-clock desk with a row 14 days out is not woken (silence can run ~7+14 days). An overdue ACTIVE-class row (owner committed since the row date) governs without itself waking the desk (charter: consumer read first), so a stale one suppresses age wakes indefinitely. Rider ③'s own "≥14 days" puts a row at exactly day 14 on the other side from "on or before +14". § 7 has no +14/+15 pair (the draft selftest does).
   change → declare 14 as PROME's reading; add the +14/+15 pair to A3/A5.

⚠️ 21  "the base four" (L23): the charter has no such term.
   claim → cadence wakes take only slots under the base four.
   checked → CLAUDE.md L49 "Cap four due-row spawns per boot", L51 "cap four/boot", L53 C6 "stays at four"; spawn_list CAP_PER_BOOT (informational).
   saw → "Dated wakes fill the cap first": an aged-ACTION wake is not a dated wake, so a stranger cannot tell whether it, a C8 session, a C9 commission or a doorbelled live desk takes a slot ahead of a cadence wake. No order among CADENCE-DUE rows when slots < rows (draft: most-overdue first; §§ 3-7 silent).
   change → "base four = the per-boot cap shared by every wake kind; dated and aged wakes first, then CADENCE-DUE most-overdue first".

⚠️ 22  Rider wording lost in §§ 3a/6.
   claim → riders ① and ② are encoded.
   checked → row 295 vs L23 / L36.
   saw → ① "otherwise roll to the next boot with room" became "else rolls to the next boot" (one-shot reading); § 6 has no roll clause. ② "never from a PROME packet or a WALTER delivery into its directory" became "from its last SELF-commit", and "SELF-commit" is undefined in the charter: a reader who takes any commit touching AGENTS/<DESK>/ as the clock never wakes a desk its neighbours keep writing to.
   change → restore both phrases.

⚠️ 23  Charter consistency: no outright contradiction with the WQ-184 (L49), WQ-206 (L51) or C6 (L53) paragraphs; the C6 restatement is accurate. Frictions:
   (a) Dark-owner triage still says "③ neither → normal inbox" (L47) and § 3a never says "outcome ①" though the R2 letter does; (b) L49 "Cap four due-row spawns" stands while § 3a spends the same four on non-row wakes; (c) overflow differs by class (dated "excess → slate for Will"; cadence "rolls"), ruled but unmarked at L49; (d) the "Spawn default" header (L42) lists WQ-184/WQ-206/WQ-221, not WQ-295.
   change → three one-clause edits, or declare.

⚠️ 25  § 3b replacement `their`.
   checked → exactly one hit for the target (CLAUDE.md L51) ✅; prome_gate.py L1058 prints "(one wake mechanism)" for the same rule.
   saw → "their" has no clear antecedent (aged waits? Aged ACTION + aged waits? the desk?). The old sentence was local to aged waits, and Aged ACTION already wakes with no DOCKET row, so "the old universal becomes false" over-reads it. If "their" means both rules it is newly false for Aged ACTION.
   change → "(WQ-184 remains the one wake mechanism for aged waits)"; note the prome_gate string.

⚠️ 26  Live statements the rule falsifies that the record never lists (hand consumer scan).
   saw → cadence spec L3 "It does not create a second triage tool or change live spawn authority."; ROSTER L213 "not ratified constants" and L218 "review hint past seven calendar days" (now the wake clock); HEAD spawn_list.py L286 "ANNOTATION ONLY" comment and L475 printed footer "CADENCE IS AN ANNOTATION ONLY"; DAEDALUS AGENTS/DAEDALUS/design/2026-10-08_L459_SPAWN_LIST_CADENCE_ACCEPTANCE.md L8 "I1 Cadence is an annotation only" (its byte-identity clause still holds for dated rows).
   change → one pass marking each amended, packeted (DAEDALUS-owned) or declared.

⚠️ 29  § 4b label and pre-typed dates.
   saw → Direction "⬆️ Promotion (encode of a 10/1 grant)" vs the 10/23 row for the same kind of event, "➡️ Record (encode of a 10/4 grant) ... Receipt, not a widening" (AUTONOMY C8 row). "2026-10-31" is typed twice (row date; § 4a "change log 2026-10-31") before the edit lands.
   change → choose the label by the C8 precedent or justify; stamp at insertion.

⚠️ 33  § 6 header quotes a phrase the spec does not contain.
   Quote (record L36): `one exception to "annotation only"`. checked → grep -i 'annotation only' on the spec: none; the phrase is in spawn_list's comment and DAEDALUS's L459 I1.
   saw → the spec's own words are point 3 "a separate cadence annotation" and L3 "does not ... change live spawn authority"; the amendment leaves L3 standing and contradicts it.
   change → quote the spec's words and name the sentence superseded.

⚠️ 40  A7 bundles seven causes in one row and picks a direction the fleet does not use elsewhere.
   saw → "no qualifying self-commit ⇒ never a wake" vs classify(): "no self-commit found in history" ⇒ DARK, and attributed(): "Ambiguity fails toward DARK". Liveness scans `git log -n 40`, so the darkest desk can land in this bucket. Not biting today: all 38 table desks have a qualifying commit (E2).
   change → one fixture per cause; say why cadence fails the other way.

⚠️ 42  A9 is "(code read)": an assertion, not a test.
   saw → the record's gloss "subject AND touched paths" copies Liveness's docstring, but attributed() accepts the `DESK:` / `DESK ->` subject form on subject alone.
   change → temp-git fixture: a PROME packet into AGENTS/<D>/inbox 1 day ago + own commit 10 days ago ⇒ still CADENCE-DUE.

⚠️ 43  A10 "dated-row output ... byte-identical" has no perimeter.
   saw → the draft's render appends a sentence to the READ footer when the block is present, and the block prints under --tsv too; byte-identity holds only for the count line + rows.
   change → name the compared lines or compare with the block off.

⚠️ 44  A11 is the converse of § 5.
   Quote A (L51): "is not-ok only while CADENCE-DUE exists". Quote B (L33): "returns not-ok while any CADENCE-DUE row exists".
   saw → X ⇒ Y vs Y ⇒ X; a gate that is never not-ok passes A11 as worded.
   change → "not-ok iff".

⚠️ 46  § 7 has no condition for: rider ① (print of slots / roll / base four) · the "never grades / never marks BOARD consumed" limits · COVERED exclusion · LIVE GATES as a governing source · +14/+15 · boot-report surfacing (rider ③ / L581 done-when) · order among CADENCE-DUE · the CLI path main()→horizon 14 · closing L581 (root rule #10: nothing after the DAEDALUS packet records the loop).
   saw → the "LIVE" legs are vacuous for the wake today: 28 WEEKLY desks, newest-to-oldest self-commit age 0-3 days, no MONTHLY desk, CADENCE-DUE 0 (E1, E2).
   change → add the conditions. Cheap CLI condition, which I ran on the draft tool and which behaves as § 3a says (E3): `spawn_list.py --as-of 2026-10-20 --horizon 0 --docket <fixture> --gates <empty>`: first-owner rows at +5d (HANS) and +14d (HAWK) ⇒ "governed"; +15d (AEOLUS) and second-owner-only (YURI) ⇒ CADENCE-DUE.

⚠️ 47  Order: "one blind plan read here → the tool built and tested" (L4); "before any edit" (§ 8).
   checked → stat / git status during the read.
   saw → record mtime 13:14:38; spawn_list.py modified (mtime 13:17:48, +221 diff lines), prome_gate.py modified (13:19:34) while the read ran. The plan read is not "before any edit" for the tool leg.
   change → say so in § 9 and apply this read's tool-touching findings (18-22, 40, 42-44, 46) to the draft.

⚠️ 49  § 2 reading choices that change WHO wakes are absent from § 3a and § 7.
   saw → (a) COVERED-suppressed rows do not govern (L12): a literal "no dated row" would count them, so a desk PROME marked COVERED gets woken; (b) any class governs (see 20); (c) DAILY never wakes (ruling silent; "only a WEEKLY or MONTHLY desk", L23); (d) second owners (19); (e) TIER-2 / SPECIAL (18). Each is declared in § 2; none is in front of Will, and the R2 letter is what he approved.
   change → list them in § 9 as PROME readings, or put (a) and (c) to Will with the encode.

⚠️ 50  Point-of-use gaps in § 3a.
   saw → "L0 drain plus a cadence self-check": neither term is defined there ("what did my domain do since my last session?" lives only at § 1 L9; "L0" appears in the charter only as "L0 drain-only", L51, and is never defined); no instrument writes a cadence wake's assignment (spawn_slate is unchanged); § 3a omits the Desk-spawn preflight the WQ-184 paragraph ties to every wake ("after owner absence is established by the Desk-spawn preflight below"). A quiet 8-day desk is the likeliest idle-but-live session, so a reader on § 3a alone spawns a duplicate.
   change → one clause each, or point at § 1 and the preflight bullet.

⚠️ 3   Row 295's "riders, verbatim from the 9/26 schedule" is trimmed against that file ("take what is left" vs "take the remaining slots"; drops "(they are review hints, not events)", "so its owner registers a row or PROME asks", the "WAL-class gap:" label). The ambiguity is the RULE's (the row), not the record's: § 1 quotes row 295 exactly. No change.

⚠️ 6   "exactly how the 9/26 schedule Will saw was computed" (L12): see 19.

⚠️ 7   Rider ③ reading (L13) "no first-owner row within +14d": the forward reading matches the schedule's own WAL example ("no dated row inside 14 days"), but rider ③ says "≥14 days" and § 2 says "on or before +14": they differ at exactly 14. See 20.

POINTERS: 21/21 resolve; dead: none. Tested: archive row 295 (L27) · proposal § R2 · 9/26 schedule · cadence spec (points 4/5/6) · DOCKET L581 · DOCKET L899 · ROSTER § DESK CADENCE (an H3, L203) · CLAUDE.md L49 / L51 anchors and the unique replace target · AUTONOMY Tier-1 bullet (L24) and anchor, change-log table (last block, 4 columns) · spawn_list.py · prome_gate.py summarize_spawn_list · spawn_slate.LAUNCH / roster_classes · Liveness.last_self_commit · attributed() · cadence_note · collect() · session_presence.py · WQ-566 record · C6 clause · bare "L455" (a DOCKET key; resolves in attributed()'s docstring). Not a record pointer but relied on: the schedule's `r2_schedule.py` (SEARCH-NOT-FOUND).

ONE-LINE VERDICT: No, not off §§ 3a/4/6 alone. The machine rule matches the ruling on frozen inputs, but the prose PROME would live by drops two ruled limits and the boot-report destination, says "PENDING" for GATES rows, and leaves launchable / first owner / +14d / base four unglossed; fix the 3 ❌ before insertion and declare the rest.

════════════════════════ The five questions ════════════════════════

Q1 Faithfulness. § 1's block quote is row 295 verbatim (archive L27, "R2 as ruled" through "(not woken)."), and the ruling's word, time and Deck tap agree across the row, the proposal's DISPOSITION note (L3) and DOCKET L581. The proposed texts are less than ruled in three places (❌ 15-17) and lose two rider phrases (⚠️ 22). § 2 adds readings that change who wakes, not just how it is measured: first owner (19), the +14d window for WEEKLY/MONTHLY (20), COVERED exclusion, DAILY, ACTIVE-governs, TIER-2 launchable (18, 49). Measurement-only choices are fine: the clock boundary (cadence_note), last self-commit via Liveness, the forward reading of rider ③.

Q2 Consistency. No contradiction with WQ-184 / WQ-206 / C6; frictions in 23. § 3b: target unique, replacement ambiguous (25). Other sentences made false: 26, 33.

Q3 Misreadings (acting on § 3a alone):
   "first owner"  → role-aware reading, or "any naming governs" → fail to wake second-owner desks / govern the wrong desk.
   "+14 days"     → counted from the clock date, or day 14 excluded → double wake or missed wake; a stale ACTIVE row suppresses forever.
   "base four"    → counts only DOCKET/GATES wakes → exceeds the cap; or "rolls" read as one-shot → a wake abandoned.
   "launchable"   → "no live session" → silent skip, no doorbell; "has a directory" → wakes DORMANT / bar-listed desks.
   "PENDING"      → GATES rows ignored → double wake.
   "SELF-commit"  → any commit touching the desk's directory → packets reset the clock → no wake.

Q4 Acceptance. No condition at all: rider ① (cap / roll / base four), the grade / BOARD limits, COVERED, LIVE GATES as a source, the +14/+15 edge, boot-report surfacing, the CLI path (46). Could pass while the rule is broken: A11 (converse), A9 (code read), A10 (no perimeter), A7 (bundled, opposite direction to classify()); every LIVE leg sees zero past-clock desks today. The fixtures themselves are sound: A1-A6 and A8 all held end-to-end on the draft tool.

Q5 Pointers. All resolve (list above).

════════════════════════ ✅ list ════════════════════════
✅ 1 ruling word / time / Deck tap agree: archive L27 · proposal L3 · DOCKET L581.
✅ 2 § 1 quote is row 295 verbatim.
✅ 4 R2 letter restated accurately (proposal L12).
✅ 5 "No dated row" definition matches collect(): inclusive horizon, covered() skip, owner_token first token, PENDING DOCKET + LIVE GATES.
✅ 8 clock boundary matches cadence_note (age > 7; today > _month_later(last)).
✅ 9 DAILY outside R2; WALTER the only DAILY desk (table scan), "Will-launched" in ROSTER.
✅ 10 launchable = spawn_slate.LAUNCH (L52), imported; roster_classes exists.
✅ 11 "Cap with C6" restates C6 accurately; CAP_PER_BOOT is informational.
✅ 12 visibility lists and the ISHM motive: L899 "dark since its 10/26 23:41 closeout"; ISHM, CYPHER, GIBBS absent from the table (dry run lists them).
✅ 13 exit code 2 / 1 / 0 unchanged; gate severity ADVISE (prome_gate run_script(ADVISE, "spawn list — L0 due-row candidates (WQ-184)")).
✅ 14 § 3a insertion anchor exists (CLAUDE.md L49).
✅ 24 § 3b target unique (1 hit, L51).
✅ 27 § 4a anchor present (AUTONOMY L24) and the inserted clause parses.
✅ 28 § 4b: 4-column change-log table, last block of the file.
✅ 30 "held 30 days behind the process ceiling": 10/1 → 10/31, DOCKET L581 "queued behind", WQ-566.
✅ 31 § 5 implementable as described; spawn_slate / session_presence omit the new parameter or call collect() directly.
✅ 32 § 6 points 4 / 5 / 6 exist and are paraphrased correctly.
✅ 34 A1, 35 A2, 36 A3, 37 A4, 38 A5, 39 A6 (fixture logic sound; A1/A3/A4 re-run end-to-end, E3).
✅ 41 A8 (the CLI has --roster; HEAD main() has an unreadable-ROSTER path).
✅ 45 A12 (N/A names its operation: the instrument cannot see sessions; the preflight governs).
✅ 48 § 9 is an honest placeholder.

════════════════════════ Evidence log (all read-only) ════════════════════════
E0 Reads: the record; archive row 295; proposal; schedule; cadence spec; CLAUDE.md L40-53; AUTONOMY L24 + change log; ROSTER L126-157, L203-268; DOCKET L581, L899; WQ-566 record; BOOT.md L61-80; GATES.tsv; HEAD spawn_list.py (copy: /tmp/claude-1000/-home-willi-Research-workspace-PROME/9df9d657-c7ea-4d69-a836-9a7e7d21c3ee/scratchpad/spawn_list_HEAD.py).
E1 Draft-tool dry run, as-of 10/31, horizon 0: CADENCE-DUE 0 · UNREACHED 4 (CREED, FLG, RED, WAL) · governed 0 · CANNOT-EVALUATE 5 (CATO, CYPHER, GIBBS, ISHM, RAV). Output: /tmp/claude-1000/-home-willi-Research-workspace-PROME/9df9d657-c7ea-4d69-a836-9a7e7d21c3ee/scratchpad/dryrun_h0.txt
E2 Independent perimeter (subject-prefix `DESK:` / `DESK ->` only) vs committed Liveness, 38 table desks: both give 0 past-clock desks; ages 0-3 days; no desk without a qualifying commit; no MONTHLY desk. Script: /tmp/claude-1000/-home-willi-Research-workspace-PROME/9df9d657-c7ea-4d69-a836-9a7e7d21c3ee/scratchpad/crosscheck_clock.py
E3 End-to-end CLI on frozen inputs (fixture DOCKET /tmp/claude-1000/-home-willi-Research-workspace-PROME/9df9d657-c7ea-4d69-a836-9a7e7d21c3ee/scratchpad/docket_fixture.tsv, empty GATES, live ROSTER, --as-of 2026-10-20): HANS (+5d) and HAWK (+14d) governed; AEOLUS (+15d) and YURI (second owner) CADENCE-DUE. Output: /tmp/claude-1000/-home-willi-Research-workspace-PROME/9df9d657-c7ea-4d69-a836-9a7e7d21c3ee/scratchpad/e2e_asof1020.txt
E4 Not done: the draft tool's own --cadence-wake-selftest (the author's suite proves "implemented", not "verified"); no repository file was edited.
