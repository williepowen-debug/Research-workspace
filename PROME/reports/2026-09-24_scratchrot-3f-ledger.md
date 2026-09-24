COLDREADER · PROME/SCRATCH.md · 22,419 B (wc -c) · 33 claims (7 question items + 26 other ★NEXT claims)
SCORE: 11/33 ✅ · 19 ⚠️ · 3 ❌

## The six questions
Q1 ⚠️ Writer: `prome-3f`, desktop, session start 2026-09-24 14:28 ET, closeout still pending (L8). The last write is stamped "15:1x ET mid-session write-back" (L2), but the archive header says it was "Rotated 2026-09-24 15:24 ET", so SCRATCH was edited after its own stamp (self-stamp, one ⚠️ at most). The file never names a single most important item. The only item it flags is L11, "BG-02 grade on the letter at 17:00 ET … — THE clock": the BRENT L329 grade needs a BRENT session live at or after 17:00 ET on 9/25, and PROME owns that. A stranger also cannot tell whether the prome-3f closeout ever ran (see E9/E10).
Q2 ⚠️ The 9/25 spawn set (L11) is BRENT L329 · BROCK L420 · RED L416 · DAEDALUS L456. The constraint is "cap 4, `ListAgents` first each", and the WQ-184 driver wakes each desk at the first boot on or after its date. BOND may still be live, which means a doorbell instead of a spawn. The set is already at the cap, yet the file also asks for: VIOLET L464 "POST-CLOSE 9/25", which DOCKET dates FRI 9/25; a second BRENT touch after 17:00; and it says nothing about other 9/25 rows that name a desk (HAWK L321/L433, FALCON L229, HANS L431/L442). It gives no guidance on overflow or a slate.
Q3a ✅ CUT 1 recomputed with the header's exact pipeline: crc32 974285586, 1441 B. That matches the header (crc32 974285586, 1441 B). CUT 2 also matches: 650084905, 1391 B.
Q3b ⚠️ CUT 1 (archive L7) says: "`PROME/ROSTER.md:107` stale (v2.3/MI3 bear → thesis-of-record is v2.4, MI3 disconfirmed 8/7; status "new" → ACTIVE) — ⛔ HELD: a third ROSTER edit needs a cold read first (with ROSTER:204)." SCRATCH L17 keeps the HELD instruction and the cold-read precondition. It drops what the line currently says (v2.3), writing "stale (v2.4 thesis, …)", so a stranger could think line 107 already reads v2.4. ROSTER:107 really does say "thesis-of-record v2.3 … new". ROSTER:204 resolves to a cadence-table rule, and nothing explains why it goes with line 107.
Q4 ✅ Encoded. L19: "FLG intake-term encode — ✅ DONE 2026-09-24 14:4x ET … live in RESEARCH-INTAKE `82c4d4e` … expiry 10/07 or merits ruling = DOCKET L467". This agrees with L8 and with the DOCKET view (10/7 L467). Note: 82c4d4e is in another repo and I could not check it here.
Q5 ✅ The record `PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md` resolves (tracked). Its WQ-282 row reads "REGISTER `GATE-TERRY-VLO-SCALE` … letter VERBATIM from TERRY's packet … (`5fae05da9`)". That agrees with L8, "`GATE-TERRY-VLO-SCALE` REGISTERED (TERRY letter 5fae05da9 verbatim)". GATES.tsv has the row (1 hit). But see ❌ E1: another SCRATCH line contradicts this.
Q6 ❌ SCRATCH contradicts itself on whether this is done.
  L11: "✅ TERRY 007 MOOT record is on card 004 (04c5c7aad, 14:2x 9/24)" (DONE)
  L25: "no POSITION action owed (TERRY's one-line MOOT record on its artifact is still owed — the OWED NEXT line above)" (OWED)
  git: 04c5c7aad = 2026-09-24 14:27 "TERRY: 9/24 owed work - 007 closed moot…". L11 is correct and L25 is stale, and L25 points to L11 as its own authority.

## Other load-bearing ★NEXT claims
❌ E1 L19 "WQ-282 registered (VLO watcher row, TERRY letter `5fae05da9`, Will's word owed)" vs L8 "Will's word 14:59 ET, verbatim *"Approve WQ-282, …"*" and L13 "WQ-282 · 254 · 261 · 260 · 276 RULED 9/24 14:59". L19 was written before the ruling and never updated.
❌ E2 L19 "LABOR spawned Tier-1 on its due claims row (ORCH_LOG row; delivery pending)" vs L8 "LABOR … + OTTO … both ASKED→RECEIPT" and L11 "LABOR ✅ done 9/24".
⚠️ E3 L19 "today's set was LABOR only" vs L8, which also lists OTTO (WQ-206 drain) plus NEXUS and ORACLE spawns. Probably means only "due-row" spawns, but the file never says so.
⚠️ E4 T-12. L8 "NEXUS real-rate T-12 successor BLESSED" vs L36 caution "Carried and still live: ⛔ *"T-12 has a successor"*". Blessed is not the same as encoded (NEXUS encode is in flight), but a stranger cannot tell whether the caution was overtaken by the 14:59 ruling.
⚠️ E5 L8 "NEXUS + ORACLE … IN FLIGHT at 15:0x". No terminal state is recorded (receipt, still working, or went dark), so the next boot cannot tell whether they delivered.
⚠️ E6 L8 "Deck republish OWED at this closeout on Will's word — not yet given", with the header saying "closeout pending". A stranger cannot tell whether the closeout or republish happened. L27 "Deck republish = the prome-26 line above" points to L14, which says prome-26's republish is "confirmed only by its own report".
⚠️ E7 L4 History lists only the boot-phase2 and prome-26 archives, not the prome-3f one, which appears only inline at L17/L19. `git status`: `?? PROME/archive/SCRATCH_ROTATED_2026-09-24_prome-3f.md` is UNTRACKED, so the pointer resolves only on this box until someone commits it.
⚠️ E8 L11 says "three new packets in `AGENTS/BRENT/inbox/WALTER/`", but ls shows seven SIG-W-20260924-* files (001, 002, 003, 010, 011, 015, 016). The whole-inbox drain covers them, but the count is wrong for a stranger.
⚠️ E9 L11 "BG-02 grades AT 17:00 ET 9/25". The hour is not in the DOCKET view (L329 is only "RESOLVER WINDOW CLOSES"). I could not verify it without the row.
⚠️ E10 L11 "`GATE-FLG-T08` pre-fire check 9/25 (PROME)". DOCKET L236 dates the event 10/1, and the file does not say why the check is on 9/25 or cite a GATES row.
⚠️ E11 L15 "HANS TTF ladder rolls 9/29, NG 9/28". No DOCKET row and no pointer.
⚠️ E12 L21 "the next T3 window (~11/09–10) is UNREGISTERED". T3 is never defined, and nothing links it to L238.
⚠️ E13 L17 bare "ROSTER:107" / "ROSTER:204". Line-number pointers drift when the file changes, and why 204 goes with 107 is unstated.
⚠️ E14 L25 "9/22 DGS10 cell printed 4.96" sits next to L19 "10Y 5.11" (9/23 official) and L47 "^TNX 5.17" (9/24 intraday). That is a +15bp one-day move with no cited source. Also, two market-data vintages coexist: L2 "14:31 ET" and L47 "12:16 ET".
⚠️ E15 L8/L19 cite RESEARCH-INTAKE `82c4d4e`, which is in another repo and could not be checked from here.
⚠️ E16 WQ-283 (dated 9/24) is pending Will in the WILLQ view (L49) but appears nowhere in ★NEXT or Operator matters (L27 names only WQ-246 · WQ-274).
⚠️ E17 L8 "CARL asks: L346 RESOLVED on a6bc2ddc8". The sha resolves, but to a 9/17 CARL→OTTO commit, so it is unclear whether the resolving act happened on 9/24 or 9/17.
⚠️ E18 L17 is labelled "verbatim → … CUT 1", but the SCRATCH line itself is a paraphrase (see Q3b). Only the archive copy is verbatim.

✅ list (checked): L23 HEARTBEAT 24,349 B = 74.8% of 32,550, 63 B under 75% (math holds) · L25 TLT 80.46 − 77 = 3.46, 5 sessions to 9/30 · L15 9/28 rows L444/L450/L462 and L465 match the DOCKET view · L15 L461 9/30 matches · L12 `AGENTS/OZK/scripts/flng_watch.py` exists · L21 two WALTER packets in PROME/inbox (9/19, 9/21) · L13 packet/owner split matches the record's table · L11 "no pre-date spawn 9/24", L329 dated FRI 9/25 in view.

POINTERS: 22/23 resolve. Files: archive boot-phase2 · prome-26 · prome-3f (untracked) · RULED record · HANDOFF · STATUS · HEARTBEAT snapshot · prome-4d report · FFB plan · flng_watch.py · BRENT inbox/WALTER · ROSTER:107/204 · GATES row. Shas (8/8): 04c5c7aad 5fae05da9 f39972f32 a6bc2ddc8 dacacc61e dbaaa7230 e9161e9e6 730cc663f. Dead: none. Untested: RESEARCH-INTAKE 82c4d4e (other repo).
ONE-LINE VERDICT: no. The dated 9/25 spawn list and BG-02 timing are usable, but three prome-3f lines were never updated after later events (TERRY MOOT, WQ-282 word, LABOR delivery), NEXUS/ORACLE have no end state, and the list is already at the cap of 4 while also asking for VIOLET and a second BRENT touch, so a stranger would repeat finished work or misread what is owed.
