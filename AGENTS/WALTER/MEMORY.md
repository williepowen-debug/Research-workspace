# WALTER MEMORY

*Curated cross-session memory. Read at boot, write before finishing. **This file is a TRIGGER INDEX, not an archive** — each rule below is one line that must fire at boot or at dispatch; the full narrative, the instance and the evidence live at the surface named beside it.*


> **Size/review trigger:** measure every Tier-2; READ_CAP.md budget, rotation trigger and stop bind. Next calendar check2026-10-22. Promote findings only after their actionable rule has an owning surface; preserve unique narratives verbatim in MEMORY_PROMOTED.md. No mechanical date-only rotation or physical-ceiling-as-pass. Earlier size incidents: MEMORY_PROMOTED.md, October16 instruction-cleanup section.

*Distinct from STATUS.md (operational state) and LAST_COMPLETION.md (latest session's deliverables). This file holds durable learnings that shape how WALTER works, not what WALTER did. Per-session "what happened" lives in SESSION_LOG.md + git history, not here.*

---
## Feedback

- [2026-10-14, Will direct] **Expiry management/reminders stay with Will and TERRY.** Will already tracks position expiries; WALTER must not participate in their management or repeat them in routine boot/news briefs. Keep WALTER focused on news, source verification and signal routing.

- [2026-05-21] **Read domain-agent STATUS at boot, not just at LIAISON setup.** Domain agents have continuous-monitoring inputs WALTER doesn't subscribe to (the Iran-anchor re-verify missed the Barakah 5/17 strike; BRENT's STATUS had it). Make "read the relevant domain-agent STATUS" a standard input for any anchor re-verify. *(2nd validation 6/10: domain reads contribute FRAMING, not just missed events. 3rd 6/20: ≥3 owners triangulating from multiple primaries can SUBSTITUTE for a redundant independent WebSearch — but only if they applied symmetric skepticism; a one-sided fleet read → spawn the sweep anyway per `[[feedback_verify_existence_external_primaries]]`.)*
## Findings — STANDING TRIGGERS (one line each; the owning surface is the second half of the line)

> 🔑 **READ THIS AS A FIRING INDEX.** Every line is a condition that must fire at boot or at dispatch. **The owning surface is where the rule is EXECUTED, and the trip to it is what keeps it alive** — `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`. Full narrative + the instance that bought each one: `MEMORY_PROMOTED.md` §Rotation 2026-08-31, matched by number.

**At INTAKE (CHECKLIST v0.39 PHASE 1 — travelled at every triage):**
1. **A sibling mechanism landing the SAME DAY is a commission trigger** — stronger than either item's own quality. → rule 1a
2. **"Is this ALREADY OURS?" runs BEFORE "is it true?"** on any curated batch — a grep disposes of a quarter of it in seconds; n=15 owner-already-has-it in one day. → rule 1b
3. **An all-dup batch IS a filter-health result — do not manufacture a dispatch to justify the time.** → rule 1c
4. **The RESEARCH-INTAKE lane counts OUTLETS, not SOURCES** — syndication inflation is structural to Google-News RSS, not occasional. → rule 1d
5. **The batch manifest is declared on CONTENT ITEMS, never images** — a clean close on the wrong denominator reads as coverage. → rule 1e

**At VERIFY (CHECKLIST v0.39 PHASE 1.5):**
6. 🔴 **DATE-CHECK BEFORE MECHANISM-CHECK on any long-running story — the desk's DOMINANT failure mode, and its base rate COMPOUNDS with story age.** The most dangerous input here is a REAL event, CORRECTLY reported, at the WRONG DATE. → rule 1.5a; named traps = `anchors/IRAN_WAR_GUARDS.md` **n+1 10/16:** `SIG-W-20261015-013` routed a KBRA 2023-08-01 bank-failure article as 2026's "4th failure" off a 10/13 lane row whose caveat said "primary not fetched" — one fetch shows the dateline (`-20261016-002`). **A lane row's batch date is not the article's date; fetch before counting.**
7. **GREP THE OWNERS BEFORE THE WEB (n=6)** — a domain agent's continuous collection beats a router's one-shot query, on FACTS as well as framing. → rule 1.5b
8. **Number right, sign wrong = the backwards-route tell** — and the natural recipient is the one whose thesis it will corrupt. → rule 1.5c

**At PRECEDENCE (CHECKLIST v0.39 PHASE 2):**
9. 🔴 **SORT BY DECAY RATE, NOT CONFIDENCE. A desk built to not-be-wrong will be RIGHT AND LATE — you cannot position on a refusal.** Route decaying items faster at lower confidence with the caveat WRITTEN IN; a stated uncertainty is a repair instruction. → PRECEDENCE DOCTRINE · `[[finding_route_by_decay_rate_not_by_confidence]]`

**At the CREDIBILITY gate (FILTER_SPEC v0.7):**
10. **The source-credibility map is PER-ACCOUNT-PER-TOPIC, never a blanket prior** (6 accounts; Amit Tal = sign-inversion on Fed-plumbing). → §Credibility (1)
11. **Sign-inversion is the most pernicious framing-error class** — on any registered-threshold metric, verify-research must EXPLICITLY confirm the sign convention. → §Credibility (2)
12. **The most kill-prone SHAPE can wrap an official primary** — verify the core against the primary the artifact implicitly cites, not against the wrapper. → §Credibility (3)
13. **On a quote-post the wrapper and the quoted post are TWO sources with TWO verdicts** — `kill_log` is the substrate of the credibility map, so a misattribution down-weights an account for something it never said. → §The Kill Log

**Cross-fleet (auto-memory) findings #14–23 — ROTATED 2026-10-03 to [`MEMORY_PROMOTED.md`](MEMORY_PROMOTED.md) (verbatim; they are `[[slug]]` duplicates of fleet auto-memory, which auto-loads for every desk — exactly what PROMOTED is for). Grep PROMOTED on demand; the slugs still auto-load fleet-wide.**

24. **A STATUS WORD THAT CARRIES A REGISTERED CONSEQUENCE IS THE ONE THAT GETS MANUFACTURED** — carry it ONLY off a primary that uses the word; "de facto <status>" is the tell that it was not declared (9/17: "de facto force majeure" → FAL-05 route (a), which has no duration bar). → `anchors/IRAN_WAR_GUARDS.md` ADD#25 (same class ADD#20 "ceasefire", ADD#24 SHUT≠HIT)
25. **A guard that reads only the token that was bumped cannot fail on the token that was not** — `spec_version()` took the first match and the H1 is line 1, so a field left at v0.37 under an H1 at v0.38 printed `ok`. Watch a guard FAIL on the instance before trusting the fix. → `tools/version_drift_check.py` docstring (DAEDALUS PR#6 ⑩)
26. **No WALTER session on a data day = a BOARD hole nobody announces** — the 9/16 FOMC hike reached four desks through their own reads and never the board; HENRY/RED (dark) never got it. At boot after any missed weekday, diff the catalyst calendar against the BOARD's last date BEFORE reading the lane. → `LAST_COMPLETION.md` OPEN DESIGN DECISIONS (a); raised to PROME 9/17

27. **A boundary whose FIRE-PRIMARY is another desk and that NO WALTER scan leg covers can fire UNSEEN for a week** — #8 (Brent 3:2:1) sat above its bar on matched November 9/15→9/24 while BRENT (primary) never fired and 6c scanned only the four registries + Cushing. "Fallback if the primary is stale" never triggers when the primary is fresh but silent. → `LAST_COMPLETION.md` OPEN DESIGN DECISIONS (j); boundary letter `design/ROUTING_OVERLAYS.md` §By Boundary Threshold

28. **Before calling a claim absent/unsupported, search specifically for it.** If the item relays a named wire, reach that wire (or a syndicator) before asserting an omission. For fast-moving theater negatives, query today’s date and the agency’s own wording. A fetched primary outranks a search summary. → `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`; four incidents preserved in MEMORY_PROMOTED.md.

29. **Every work leg after closeout reopens it:** rerun charter Tier1 on its outputs; refresh affected STATUS levels/counts, LAST_COMPLETION claims/receipt, then closeout_check.py. Resolve failures or explicitly carry them, never claim PASS from doctor alone. At boot compare STATUS BOARD count with INDEX to catch late dispatches. → CLAUDE.md §Closeout; eight recurrences preserved in MEMORY_PROMOTED.md.

30. **ROTATED 2026-10-08 (laptop Tier-2) verbatim → [`MEMORY_PROMOTED.md`](MEMORY_PROMOTED.md)**: owning surfaces are the RESEARCH-INTAKE config comment (`ff21407`) and the WATCH_FOR census.

31–32. **ROTATED 2026-10-08 (laptop Tier-2) verbatim → [`MEMORY_PROMOTED.md`](MEMORY_PROMOTED.md)**: both already have owning surfaces (#31 `tools/watch_for_harness.py --live`; #32 the `tools/intake_scan.py` fix `cc9c14017`).

33. **When a signal characterizes a SINGLE-NAME desk's exposure, read THAT desk's own record before stating the link, not the hub's KB row about it.** 9/27: `-004` framed WAL↔Nano Banc as "fraud exposure, NOT a loan to Nano, no new loss by itself" off REGINALD's secondhand Feb-2026 KB row; WAL's own verified complaint (on WAL's surfaces since 2025) showed Nano liens SENIOR to WAL on 5 of 10 pleaded loans. Two corrections in 40 minutes (`-005`, `-006`). Same class as #7 (grep the owners), one level finer: the RIGHT owner is the one whose exposure is being described. → `[[finding_verify_reader_before_source]]`
34. **Never type a dispatch time into a Write-tool signal.** 9/27: all 7 dispatches stamped +8 to +73 min AHEAD of their own commits; the doctor caught it at closeout, and only because some were still in the future. → `[[finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock]]` (n+1 appended 9/27; n+1 10/9: '~17:50 ET' typed into a consume declaration at 17:44, caught the same minute — the rule covers EVERY ledger cell, not only signals; n+1 10/16 evening: '~21:45Z'/'~21:50Z' typed into two `source:` lines of a batch stamped 21:39:26Z, caught pre-commit. The `source:` frontmatter line is a stamp too); n+1 10/18: "01:0xZ" typed into REGISTRY Focus cells at 00:57Z, caught pre-commit
36. **A date in your own carry list is a claim, not a fact. Re-open its source before you build a routing decision on it.** 9/29: `-004` told TERRY and PROME that the WQ-316 options card was due "15:00 ET today". My own LAST_COMPLETION listed it under **9/30**, and WQ-316 says "the two WEDNESDAY expiries". I misread the bucket, used it to pass the doorbell gate (L3a), and rang PROME for a deadline a day away. PROME caught it in minutes (`-009`, DOORBELL_LOG CORRECTED row). The real consequence was the reverse of what I routed: the one-session gamma read EXPIRES before the decision. **Before a doorbell or a precedence choice keyed on a date, open the owner row (WILL_QUEUE/DOCKET), not your summary of it.** → `[[finding_dated_carry_item_has_no_expiry_check]]`
37. **Two series on the same index are ONE witness, not two.** 9/29 `-003` called the CCC effective yield "a second series beside RED-FT-07's CCC OAS". LIQUID: it is the same ICE CCC index plus a rates leg (9/17→9/28: +95bp yield, of which OAS +70), so it adds the all-in refinancing cost, not corroboration. **Before writing "second witness/corroborates", name what each series measures and what they share.** → `[[finding_agreeing_secondaries_share_a_frame_so_they_omit_the_same_things]]`

35. **Before routing an ask at an owner's ROW, read that FILE's header for a FROZEN banner. A grep hit in a frozen ledger reads exactly like a live row.** 9/28: `-010` told BRENT its SPR basis was ~411M and 125M stale, citing KB-BRT-152/VX-BRT-13. Both files are bannered "FROZEN 2026-07-01, do NOT cite rows here as current", and BRENT's live 284.552M was already in TRACKER. BRENT caught it the same hour; the claim reached Will on Telegram and was corrected. Root CLAUDE.md § Data Hygiene already says ledgers can be FROZEN; the trip that was skipped is `head -2` on the file before quoting a row as the owner's current basis. → `[[finding_plausible_stale_value_evades_review]]`


38. **ROTATED 2026-10-08 (laptop Tier-2) verbatim → [`MEMORY_PROMOTED.md`](MEMORY_PROMOTED.md)**: owning surfaces are the sizing records `research/2026-10-01_R3/*-sizing.md`.

39. **A lane row's `date` is the date the ITEM was published or re-published, not the date of the EVENT, and a repost aggregator gives an old wire a fresh date.** 10/01: EnergyNow's "Oil Loadings Suspended at Saudi's Red Sea Port of Yanbu" sat in the 10/01 batch stamped 9/30. It was Reuters 9/15, and carrying it would have reversed the live "loadings resumed" state. Same day, a Petroline "restarts" item carried its true 9/22 date. **On any state-reversing item, search the exact headline before routing; the earliest dated copy is the event date.** Same class as #6, one level finer: the lane can supply the wrong date with nothing looking stale. → `[[finding_relayed_level_predates_the_event]]`

40. **An item already routed is not an item that has stopped moving.** 10/02: `-002` (09:32 ET) told BRENT "no agreement is reported" on Europe's diesel release, while Macron's "G7 DECIDED" headline had posted ~09:20 ET. The later gap sweep never re-searched the diesel story because it was "covered", and the decision reached the fleet only through Will's screenshot (`-009`). **Before any sweep, and before calling a sweep done, re-search each of the day's routed STATE-DEPENDENT stories once (talks, releases, deals, strikes) and ask "what changed since I sent it?".** Same family as #29 (work after a closeout re-opens it): a dispatch is a snapshot, not a watch. → `[[finding_dated_carry_item_has_no_expiry_check]]`
41. **Missing fleet visibility is UNKNOWN, not DARK.** When PROME has in-process spawns, require its current teammate evidence before a dark verdict; clean files and native ListAgents can miss them. Re-read ORCH_INFLIGHT immediately before EVERY doorbell/dark claim; rows can be written at spawn, and boot-time evidence expires. Apply charter9b and Rule13 before a qualifying doorbell to PROME. → CLAUDE.md; two incidents preserved in MEMORY_PROMOTED.md.
42. **A capacity add inside a disciplined oligopoly is material even with no capex guide.** 10/02: WALTER killed the TrendForce 'Toshiba doubles HDD capacity, $380M' lane row at 12:33 ET as a single-vendor capacity add; STX/WDC fell ~10% on it by 15:58 ET (`-024`, kill re-opened). **Before a materiality kill, ask: does the market leaders' story rest on SUPPLY RESTRAINT? If yes, any new unit is the story.** → kill_log re-open row 10/02
43. **A figure’s BASIS travels with it; its owner sets the basis.** Before relaying a number or scope word, name source, session and definition. When the owner is live, send it the figure for a basis check before it reaches Will. → `[[finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session]]` · `[[finding_rederived_signal_loses_the_senders_caveats]]`; three incidents preserved in MEMORY_PROMOTED.md.

45. **Run `claim_check --check weekday` on the day's BOARD cards BEFORE the first commit, not at closeout — a weekday typed into a handoff reaches desks within minutes.** 10/8: -009 said "Tue 10/14" (Wednesday); HENRY copied it and caught it with the checker 25 min after dispatch (-016). The checker also false-flags a correct date when another year sits in the same line (-013, "2028–2029"): look, never find-replace. → root closeout step 1e · `[[finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock]]`

46–47. **ROTATED 2026-10-10 PM (walter-66) verbatim → [`MEMORY_PROMOTED.md`](MEMORY_PROMOTED.md)**: both acquired owning surfaces this session — #46 `design/SIGNAL_PROCESSING_CHECKLIST.md` v0.51 rule 1b; #47 `design/X_BOOKMARKS_ACCEPTANCE.md` LIVE UPDATE 2026-10-10.

48. **One delivery_log row per (signal, recipient).** A second 'corrective' row for the same pair makes `closeout_check.py` return UNKNOWN; correct the original row's path in place and put the history in its notes. (10/14, -034 PROME path fix.)


**✅ RETIRED 2026-09-01 — the two-branch-test-sharing-a-premise finding (2026-08-03) is PLACED:** PROME landed it as the n=5 extension of `[[finding_enumerated_mechanism_test_hides_a_completeness_claim]]` (8/31 night, packet filed to WALTER 9/1) and the test now sits in bold in `FORGE/PREDICTION_DISCIPLINE.md` § Registration. *(Was: "owed, not placed — WALTER cannot file to a PROME-owned surface." The obligation discharged the way it was supposed to: a packet, then the owner's write.)*

## References

- **Root `CLAUDE.md`** — git protocol, agent lifecycle, cost model, status hierarchy.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup, RULES, closeout git steps 16a-16f.
- **`AGENTS/WALTER/design/`** — all specs. FORMAT_SPEC (schema), ROUTING_TABLE (routing), FILTER_SPEC (filter), CHECKLIST (process). STATE.md = design+infra completeness directory (on-demand). CROSS_REFS/{AGENT}.md = identifier cache (dispatch-time).
- **LIAISON path convention:** `AGENTS/{TARGET}/handoff_WALTER/LIAISON.md`; manifest in STATUS.md "Active LIAISON channels"; playbook `design/LIAISON_PLAYBOOK.md`. Outbox at `AGENTS/WALTER/outbox/REQ-{TARGET}-{YYYYMMDD}-{slug}.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py`.
- **Bright Data Web Unlocker (WQ-383 pilot, LIVE 2026-10-04):** `bdata scrape <url>` for a 403'd no-screenshot bookmark link; free tier 5k/mo HARD STOP, Web-Unlocker-only, key in gitignored `.env` (per-machine). Full method+limits+ledger: `design/X_BOOKMARKS_ACCEPTANCE.md` §9a.
## Session Notes

**2026-10-19T16:26:16Z resumed owner:** publishedHY0033/3;004HMI;005newJMICrisk/tug,existinglossconflict;006OTTO;007office-routecorrection,008OTTOpanel44/44+forecast8%OPEN. Interrupted8-itembatchclosed; ownerinbox4integrated. L599notrepeated/noextension. Authrepair onWill’s directrequest:401/refresh400→reauth→200;seenunchanged,0bookmarkfetch/mark. Evidence `research/2026-10-19_resume/`; currentdutiesandpublication/consumptionlimitsinLAST_COMPLETION.
