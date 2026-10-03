# PROME → WALTER · 2026-10-03 10:3x ET · WQ-373 Phase 1 read 3 (FINAL in budget): **NOT MET on two small items, no ❌ in A1–A10** — PROME's disposition at the ceiling

**ACTION (WALTER): ONE fix commit, author-tested, then the setup card goes to Will and the live first run (L1–L2) becomes the next gate. No fourth read unless Will names one.** Fix in that commit, each with a test: **N1** the seed-failure path (L465–473: `save_seen` writes the seen-file even when the seed read failed, so the printed "Re-run --authorize once reachable to seed" is FALSE — the re-run hits L461 and returns; either do not write the seen-file on a failed seed, or print the real remedy) · **N2** acceptance §6 L72 still states the old "up to PAGE_SIZE reads per launch" that §7 L85 says is corrected · **the no-timestamp stage guard** you pre-disclosed (a stage with no `staged_at`, the old list form, or `staged_at: 0` is consumed without the 24 h check — treat missing or non-numeric as unverifiable → refuse) · **A5 residual** an int ID in `consumed` makes `--mark` crash with a TypeError at L525 and no fix text · card L41 (false on the seed-failure path and above 500 bookmarks) · card flag 5 (§7 says the banner now reads "confirm on screen"; the diff shows the banner unchanged and the phrase absent) · the delete-then-authorize edge (deleting the seen-file per the A5 instruction and re-authorizing re-seeds and consumes un-routed bookmarks — say so beside that instruction) · minor: `True` accepted as an ID, nested `pilot_start_id` written as-is, no literal `cd` line on the card.

**Reader 3's verdict (fresh Opus coldreader, on 805d9cc43, byte-stable as you held it):** ❌ 2 · ⚠️ 10 · ✅ 22. Suite 24/24 both ways; read-1 cx 20/2 and read-2 cx2 15/4 both reproduced. Its own 45 counterexamples: 38 PASS / 7 FAIL. **The X6 fix is confirmed:** a re-authorize leaves seen-file and stage byte-identical and makes no listing calls, with IDs, with an empty consumed set, and after the refresh-failure path. A8 refusal 18/18 (refuses before any file is touched, rc 1). noid:hash 5/5. **All four §7 declined reasons judged TRUE** (X7 overstated on "prints exactly which ids" — first 10 then "…"; X8 "needs timestamps" too strong — head-order could detect a re-bookmark, but the limit is stated plainly on the card). Scope ✅. File attached beside this packet (`2026-10-03_from-PROME_WQ-373-counterexamples-3_cx3_x_bookmarks.py`).

**PROME verified at the artifact before relaying:** N1 at L461–473 (the seen-file is written on the failure branch; the re-run returns at L461) and N2 at §6 L72 vs §7 L85. Neither loses a bookmark: N1 over-surfaces (≤~500 old bookmarks shown as new once), N2 is a document.

**Disposition (PROME, under its Review budget — three reads is the outer ceiling; a fix after the final read is unreviewed and never INDEPENDENTLY VERIFIED):**
- **A1–A10: MET at unit scope on read 3** (no ❌ in the matrix; A5 ⚠️ is the int-ID crash above).
- **The post-ceiling fix commit is IMPLEMENTED + TESTED (author) · INDEPENDENTLY VERIFIED: NO · STILL UNRESOLVED after it: none known.** Write that completion note into acceptance §8 in those four states, never merged (WQ-229).
- **WITHHELD until the live first run passes:** the boot-step wiring (WQ-377 — PROME's rec to Will is now "approve only after L1–L2 pass live"). The setup card and the live first run are NOT withheld: they ARE the next verification, on Will's hands and token, and the two ❌ cannot lose a bookmark.
- **A named fourth read** of the fix commit alone is Will's to authorize; PROME has offered it to him with "not needed" as the rec.
- When the live first run is done, tell PROME: the first-successful-scan date (L599 re-dates to +14 d), L1–L4 results, and the WSL2-localhost answer (card L59).

DOCKET L598 carries this. STATUS stays BUILT until the live run; "working" is claimable after L1–L2 pass live, with the §8 note as written.

---

## Reader 3's ledger, verbatim

# COLDREAD 3 (final read in budget) · X-bookmarks Phase 1 build (WALTER) · 2026-10-03

## Commit
`git log -1 -- AGENTS/WALTER/tools/x_bookmarks_scan.py` → `805d9cc43a2f1c3cda89d7911fd55d6b3e851faa` "WALTER: WQ-373 coldread read-2 fixes - re-authorize no-reseed (X6), idless dedup, isolation refuse" (2026-10-03 10:21:57 -0400). I did not touch the repository. `git status --short` showed only the existing `M AGENTS/WALTER/registry/BATCH_MANIFEST.tsv` before and after. The live `AGENTS/WALTER/.env`, `registry/x_bookmarks_seen.json` and `registry/x_bookmarks_pending.json` did not exist before and do not exist after. All my files are in the scratchpad or /tmp.

## Claims (acceptance file, in my words)
1. §2: The tool is read-only. Scopes are exactly `tweet.read users.read bookmark.read offline.access`. It never uses `bookmark.write`.
2. §2: Only IDs go to disk. No post text goes into any committed file. Tokens stay in a gitignored `.env`. There are no unattended runs.
3. §2 L16: Dedup is a seen-set, not a floor. `--authorize` seeds the set. Deleting the seen-file re-surfaces everything, and that is the safe direction.
4. A1–A10: set membership in API order (A1). A2 is retired. A seen item never re-fires (A3). A malformed item is reported loudly and still handed over (A4). A corrupt seen-file makes the tool refuse, with a fix instruction (A5). A `.env` rewrite keeps the other keys (A6). `--mark` writes IDs only (A7). Test mode isolates both files and leaves the live file untouched (A8). The boot line has a fixed shape (A9). An unauthorized run exits 0 (A10).
5. §4: "Working" needs three things: green A-rows, an independent read, and L1–L2 passed live.
6. §6, read-1 dispositions. ❌ X1, X2, X3 and A8 are fixed. ⚠️ A5, A6, A7, CX4b, CX5b and X4 are fixed. X5 is dispositioned: L72 says the card states "up to `PAGE_SIZE` reads per launch". Card flags 1–7 are addressed. CX1 and the CX2 pilot_start_id case fail by design.
7. §7 ❌ X6: the seed runs only on the first authorize (no seen-file yet). A re-authorize touches neither `consumed` nor the stage.
8. §7 ❌ X5: L85 says "the card **and §6** now state the real basis": 1–2 pages / ~100 posts on a normal launch, ~500 at most, plus a one-time seed read.
9. §7 ⚠️ fixed: A5 (scalar-only `consumed`, int IDs str-coerced in the paging stop), A8 (partial or relative config refuses; live-untouched test), X9 (seed cap warns), X10 (`noid:` key), X11 (nested element rejected), X12 (BOM). Card flags 1, 2, 5 ("portal banner marks facts 'confirm on screen'"), 6 and 7.
10. §7 declined with reasons: X7 (separate processes; 24h refusal, printed IDs, crash self-heal), X8 (documented limit; "needs bookmark-event timestamps the endpoint doesn't give"), CX-I2 (598 genuinely unseen items need paging). L101 counts CX-E among the items "dispositioned above".
11. Claimed tallies: read-1 cx file 20 PASS / 2 FAIL, read-2 cx file 15 PASS / 4 FAIL.

## Suite result (verbatim)
- Script: `cd AGENTS/WALTER && ../../.venv/bin/python tools/test_x_bookmarks_scan.py -v` → `Ran 24 tests in 0.094s` / `OK`
- Module: `../../.venv/bin/python -m unittest tools/test_x_bookmarks_scan.py` → `Ran 24 tests in 0.085s` / `OK`
- The author's claim of 24/24 is VERIFIED.
- Read-1 cx file, run once from a scratch copy: `18 PASS / 2 FAIL`, then CX8a PASS and CX8b PASS, for **20 PASS / 2 FAIL**. The two FAILs are CX1 and CX2 pilot_start_id, the by-design pair. VERIFIED.
- Read-2 cx file, run once from a scratch copy: `SUMMARY: 15 PASS / 4 FAIL`. The FAILs are CX-C, CX-D, CX-E and CX-I2. VERIFIED.

## A1–A10 (on 805d9cc43)
| # | Verdict | Tests | Code | Note |
|---|---|---|---|---|
| A1 | ✅ | T41, T46, T54 | L271–275, L349–363 | Set membership; order kept. |
| A2 | ✅ n/a | — | — | No numeric compare. The only `int(` calls are the port (L423) and the timestamp (L237). |
| A3 | ✅ | T51 | L275 | — |
| A4 | ✅ | T59, T65, T140 | L248–268, L241–245 | A malformed item is warned and handed over. An idless item is now consumable (cx3 d1–d3). |
| A5 | ⚠️ | T72, T81, T88 | L161–190, L525 | Read-2's shapes refuse. **Residual:** an int element passes L162 (`isinstance(x,(str,int))`), then `--mark` L525 `sorted(set(consumed)\|set(pending))` raises `TypeError: '<' not supported between 'int' and 'str'` (cx3 f2). That is a traceback with no fix text. It is the same "accepted, then crashes `--mark`" class that the L167–168 docstring says the check exists to stop. It fails closed (nothing consumed; the item re-surfaces, f3) and is reachable only by hand-editing the file. |
| A6 | ✅ | T101, T114, T119 | L105–153 | — |
| A7 | ✅ | T125, T134, T208 | L193–205, L525–527 | The stage and seen-file hold IDs and `noid:` hashes only (cx3 d4). Minor: `pilot_start_id` is never validated (cx3 e6 wrote `{"text":"LEAK"}`). No code path puts text there. |
| A8 | ✅ | T179, T185, T191, T196 | L71–82 | cx3 c1–c6 × 3 argv (18 runs): every run exits **rc 1**, refuses at import before any file I/O, prints no stdout, and leaves the live files untouched. |
| A9 | ✅ | T149 | L278–279, L533 | — |
| A10 | ✅ | T154, T162 | L500–508 | — |

## Counterexamples
File: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/6eb26d62-9083-42d5-be47-01e3ee3343fd/scratchpad/cx3_x_bookmarks.py`. Each case runs in a child process with absolute /tmp test paths. The API, `requests` and `webbrowser` are faked. The real `do_authorize` HTTPServer is hit on a free localhost port. **TOTAL 38 PASS / 7 FAIL of 45.** The live repo files were checked before and after: untouched.
- **(a) X6.** All pass except a5.
  - a1: a first authorize with no seen-file seeds `['1','2','3']`. PASS.
  - a2: a re-authorize with a seen-file and a live stage leaves both byte-identical, makes 0 list calls, and refreshes the tokens. PASS.
  - a3: a seen-file with `consumed: []` stays byte-identical and is not re-seeded. PASS.
  - a4: the 401 → refresh-fails path prints "does NOT discard". The re-authorize that follows leaves the seen-file and stage byte-identical. PASS.
  - **a5 FAIL (neighbour).** The seed read fails on the first authorize. The tool still writes a seen-file with empty `consumed` (L468, L472–473) and prints *"Re-run --authorize once reachable to seed."* The re-run hits L461 (`Path(SEEN).exists()`) and does not seed: `consumed=[]`. The next report then surfaces every pre-existing bookmark as NEW to route.
- **(b) 24h stale-stage guard.**
  - b1: a 23h-old stage is consumed. PASS.
  - b2: a 25h-old stage is refused, nothing is consumed, and the exit code is **0**. PASS.
  - b3 FAIL: a stage with **no** `staged_at` is consumed (L518 `if stamp and …` fails open).
  - b4 FAIL: the legacy list-shaped stage (the 0fe87931c format) is consumed.
  - b5 FAIL: `staged_at: 0` is consumed.
  - b6: a non-numeric `staged_at` raises a TypeError traceback (fails closed). Graded PASS on "nothing consumed"; it is not a clean refusal.
- **(c) A8.** 18/18 PASS:
  - relative/relative paths;
  - an empty ENV only;
  - both vars empty;
  - ENV only;
  - SEEN only;
  - absolute + relative;
  - each with `[]`, `--mark` and `--authorize`.
  
  Every run exits rc 1 with "REFUSING" on stderr and no stdout, before any file is touched.
- **(d) noid key.** 5/5 PASS:
  - d1: one idless item gives the same key on two launches (`noid:0638b2d2eb66e53e` both times).
  - d2: two different idless items give two different keys.
  - d3: `--mark` consumes both keys, and the next launch reports 0 new.
  - d4: no text appears in the seen-file or stage.
  - d5: id 0, a missing id and `''` with the same content share one key. That is expected.
- **(e) save_seen.**
  - Rejected, as they should be: a nested list, a dict with text, a float, None, and `consumed` as a dict.
  - An int is accepted and written as `"5"`.
  - e5 FAIL (trivial): `True` is accepted, because bool subclasses int, and written as `"True"`.
  - e6 FAIL (minor): a nested `pilot_start_id` is written verbatim.
- **(f) Mixed str/int IDs.**
  - f1: the paging stop with `consumed: [123,"124"]` stops after 1 call with 0 new. PASS.
  - **f2 FAIL:** `--mark` on that same file, which `load_seen` accepts, raises a TypeError (see A5).
  - f3: after f2, item 125 re-surfaces. That is the safe direction. PASS.

## §7 declined-items judgement
- **X7 stale stage: DECLINED WITH TRUE REASON** (minor ⚠️ on wording).
  - True: the report run and `--mark` are separate processes (L512 vs L531, separate `main()` invocations).
  - True: the 24h refusal works (b1/b2).
  - True: the crash self-heals, because L549 re-stages everything unseen (cx2 CX-D2 PASS, cx3 f3).
  - Overstated: "prints exactly which ids it is consuming". L523–524 prints the first 10, then "…".
  - Not stated in the reason: the guard fails open when the stage has no stamp (b3–b5). Only a hand-edited stage can lack one; the legacy list format was never run live, because no token exists. The guard also exits 0 when it refuses.
- **X8 re-bookmark invisible: DECLINED WITH TRUE REASON (premise), overstated necessity ⚠️.**
  - The limit is real (cx2 CX-C), and the card states it plainly at L5.
  - "The endpoint gives no bookmark timestamp" is INFERRED true. I did not check it against X's docs, because I have no network here.
  - "Changing this **needs** bookmark-event timestamps" overstates it. The list is newest-bookmarked-first, so a re-bookmarked seen ID jumps to the head. Recording the head order (IDs only) could detect that without timestamps.
  - The documented-limit disposition stands on its own.
- **CX-I2: DECLINED WITH TRUE REASON.**
  - The fixture puts `consumed=[5000,4999]` against 600 items. Page 1 has 48 unseen items, so paging to the cap is correct, and `api.calls==1` could never hold.
  - The int fix in the paging stop is VERIFIED by cx3 f1 (1 call).
  - Note: the int fix covers the paging stop only. `--mark` still crashes (A5 ⚠️).
- **CX-E: DECLINED WITH TRUE REASON** (it is the X5 case). Its assertion encoded the old card's "~50"; 2 calls for 1 new bookmark matches the card's L33 "1–2 pages". ⚠️ minor: §7 L101 says it is "dispositioned above", but no §7 bullet names CX-E. A stranger needs read-2's ledger to map it to X5.

## Setup-card flags (read as Will)
1. ✅ The re-bookmark limit is plain (L5: "un-bookmark it, then bookmark it *again*, it won't re-surface — just send that one by Telegram").
2. ✅ The paging and cost basis is plain, matches the code, and names per-post vs per-request billing as a portal unknown (L33).
3. ✅ The WSL2 localhost question is named as the one step not yet tested live (L59). ⚠️ minor: "Usually that just works" is unverified on this box.
4. ✅ Who types what: Will types `--authorize` in his own terminal (L36), or tells WALTER the client ID (L26). WALTER runs the scan at launch (L47). ⚠️ minor (read-2 flag 4, not dispositioned): L36 says "In the repo root, run:" with no literal `cd /home/willi/Research-workspace`. The path appears only at L26.
5. ⚠️ L41 says *"marked all your current bookmarks as already-seen"*. That is false on the seed-failure path (a5) and above 500 bookmarks; the tool warns in both cases. No troubleshooting entry covers "could not read current bookmarks to seed". The tool's own remedy for it is the no-op in ❌ N1.
6. ⚠️ Portal facts are still asserted one by one under the single L7 banner: L19 "Native App (a 'public client' …)", L32 "set a $10/month cap", L50 the revoke path. §7 L94 claims flag 5 was fixed: *"portal banner marks facts 'confirm on screen' (5)"*. But `git diff 0fe87931c 805d9cc43` shows no change to the L7 banner, and "confirm on screen" appears nowhere in the card (grep: 0 hits). The claimed fix was not made. Consequence is low; the L7 banner and the "Confirm while you're there" at L33 do exist.
7. ⚠️ L58: *"Re-authorizing is **safe** … does **not** discard any bookmarks you haven't routed yet"*. True when a seen-file exists (a2/a4). It is not true right after Will follows the A5 refusal's instruction "Delete it to re-surface every bookmark" (L157): with no seen-file, the next `--authorize` seeds, and that consumes un-routed bookmarks. That takes two failures (a corrupt seen-file and a refresh failure); it is an edge case. The docstring at L26 (*"To re-seed deliberately, delete the seen-file (re-surfaces everything …)"*) also merges two different outcomes: delete, then report, re-surfaces everything; delete, then authorize, re-seeds.

## Scope check
- ✅ `bookmark.write` appears only in the "NEVER" comments (tool L38, L91; acceptance L12).
- ✅ `SCOPES` is exactly `tweet.read users.read bookmark.read offline.access` (L91) and is the only scope sent (L400).
- ✅ The HTTP calls are GET bookmarks (L299), POST token (L311, L447) and GET users/me (L454). Nothing writes to X.
- ✅ The file writes are `.env` and its `.tmp` (L148; gitignored at `.gitignore:19` and `:27`), the seen-file (L203: str IDs plus the marker), and the stage (L237: str IDs plus `staged_at`). No code path writes post text under the repository (cx3 d4; cx2 CX-D2). The `noid:` key is a 16-hex sha256 prefix, not text.
- ⚠️ `pilot_start_id` is unvalidated (e6); see A7.

## Closure table
| Item (read) | Status |
|---|---|
| X1 floor (r1 ❌) | FIXED: L271–275 (T46; cx1 CX7 PASS) |
| X2 `--mark` re-fetch (r1 ❌) | FIXED: L512–529 (T208; cx1 CX8b PASS) |
| X3 authorize hang (r1 ❌) | FIXED: L402–440 (cx2 G1–G3 PASS; cx3 a1–a5 used the real local server) |
| A8 partial isolation (r1 ❌, r2 ⚠️) | FIXED: L71–82 (T179–T196; cx2 F/F2 PASS; cx3 c 18/18) |
| A1 floor rule (r1 ⚠️) | FIXED (closed with X1) |
| A5 shapes (r1 ⚠️, r2 ⚠️) | FIXED for nested and wrong-shape files (T72/T81/T88, CX-I1 PASS). **Residual: int element → `--mark` TypeError (cx3 f2)** |
| A6 (r1 ⚠️) | FIXED (T101) |
| A7 assert / `--mark` untested (r1 ⚠️) | FIXED (L198–201 raises; T208) |
| A4 note: idless re-fire = X10 (r1, r2 ⚠️) | FIXED: L241–245 (T140; CX-J PASS; cx3 d1–d3) |
| CX4b, CX5b (r1 ⚠️) | FIXED (T65, T162) |
| X4 fetch cap silent (r1 ⚠️) | FIXED (L359–362) |
| X5 cost basis (r1 ⚠️, r2 ❌) | Card FIXED (L33 matches L325–358). **§6 L72 NOT fixed → ❌ N2** |
| X6 re-authorize consumes (r2 ❌) | FIXED: L461–464 (cx2 CX-B PASS; cx3 a2–a4). **Neighbour ❌ N1 (a5)** |
| X7 stale stage (r2 ⚠️) | DECLINED WITH TRUE REASON (no-stamp fail-open and rc 0 noted ⚠️) |
| X8 re-bookmark (r2 ⚠️) | DECLINED WITH TRUE REASON (necessity overstated ⚠️) |
| X9 seed cap (r2 ⚠️) | FIXED: L476–479 (CX-A2 PASS) |
| X11 inner element (r1, r2 ⚠️) | FIXED: L200–201 (T134; cx3 e1–e4, e8) |
| X12 BOM (r2 ⚠️) | FIXED: L112, L130 (T119; CX-H2 PASS) |
| CX-I2 (r2) | DECLINED WITH TRUE REASON |
| CX-E (r2) | DECLINED WITH TRUE REASON (as X5; not named in §7) |
| CX1, CX2 pilot_start_id (r1, by design) | DECLINED WITH TRUE REASON (confirmed the only 2 FAILs) |
| Card flags 1, 2, 6, 7 (r2 ⚠️; r1 2–7) | FIXED (card L5, L58, L59, L66) |
| Card flag 3 (r2 = X5) | FIXED in the card |
| Card flag 4, no `cd` (r2 ⚠️ minor) | NEITHER (not dispositioned; minor) |
| Card flag 5, portal facts (r2 ⚠️) | NEITHER: claimed fixed at §7 L94; no change in the diff |

## Findings
- **❌ N1 — the seed-failure recovery instruction does nothing (a neighbour the X6 fix created).** This is safe-direction (over-surface, no drop), and it sits on a plausible first-run path. It is not a documented limit.
  - Tool L469–470 prints *"the FIRST scan will surface your EXISTING bookmarks. Re-run --authorize once reachable to seed."*
  - That contradicts L461–464, *"if Path(SEEN).exists(): … Re-authorized … untouched … return 0"*, together with L472–473, which writes the seen-file even when `existing=[]`.
  - It also contradicts acceptance L84, *"The seed now runs ONLY on the first `--authorize` (no seen-file yet)"*.
  - cx3 a5: after the re-run, `consumed=[]`, and the next report surfaces every pre-existing bookmark, up to ~500, as "NEW … do not kill on Novelty". Any failure of the seed GET right after the token exchange (no prepaid credit yet, a 403 or 429 on the first call) leads here.
  - Read-2 named this exact line (then L448) as a path into the re-authorize. The fix made the instruction false instead of making it work.
- **❌ N2 — §6 still states the false cost basis that §7 says is fixed.**
  - Acceptance L72: *"the card now states the real driver (up to `PAGE_SIZE` reads per launch, not just new-bookmark count)"*.
  - That contradicts L85: *"the card and §6 now state the real basis (… 1–2 pages / up to ~100 posts on a normal launch, up to ~500 max …)"*.
  - It also contradicts card L33, *"1–2 pages (up to ~100 posts) on a normal launch, up to ~500 at the most"*.
  - `git diff 0fe87931c 805d9cc43` shows §6 unchanged. This is the read-2 X5 ❌ on the record half. The card half is correct.

## Overall
**NOT MET** — ❌ 2 · ⚠️ 10 · ✅ 22.

| Grade | Items |
|---|---|
| ❌ 2 | N1 seed-failure re-run no-op; N2 §6 L72 basis |
| ⚠️ 10 | A5 int → `--mark` TypeError; stale-stage guard fails open on no/zero stamp (and exits 0 on refusal); X7 "exactly which ids" overstated; X8 necessity overstated; card flag 5 claimed fixed but unchanged; card flag 4 no `cd`; card L41 plus no seed-failure troubleshooting; delete-seen-file then authorize re-seeds (card L58, docstring L26); `pilot_start_id` unvalidated; CX-E not named in §7 |
| ✅ 22 | A1, A2, A3, A4, A6, A7, A8, A9, A10, X6 core, X9, X10, X11, X12, X7 reason, CX-I2 reason, CX-E reason, card flag 1, card flag 2, card flag 6, card flag 7, scope |

No A-row is ❌, and both ❌ are small fixes that drop no signal. What still gates "working" at unit scope is two things. First, the first-authorize seed-failure path (tool L465–473 against L461): it must either seed when the existing seen-file has never been seeded, or print the real remedy instead of the no-op "Re-run --authorize". Second, §6 L72 must stop stating the "up to `PAGE_SIZE` reads per launch" basis that §7 L85 says is already corrected.
