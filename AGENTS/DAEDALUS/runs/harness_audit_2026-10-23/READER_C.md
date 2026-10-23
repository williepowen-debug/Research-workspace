# Harness Audit #3 — Reader C ledger

**Reader:** C · **Date:** 2026-10-23 · **BASE:** 3d47a7d9d · **HEAD at read:** 9da57b469 · read-only against the repo. Working notes appended at the bottom.

## Files in scope (bytes at HEAD) and coverage

No top-level `OPERATIONS.md` exists for any of these 14 desks. `CLOSEOUT.md` exists only for LIQUID and BOND.

| file | bytes | lines | coverage |
|---|---|---|---|
| AGENTS/REGINALD/CLAUDE.md | 24,887 | 166 | WHOLE (1–166) + FULL-DIFF (81+/246−; 2026-10-20 rewrite) |
| AGENTS/WAL/CLAUDE.md | 28,994 | 198 | WHOLE (1–198; long lines 13, 16–19, 60 cut at ~1,200 chars) + FULL-DIFF |
| AGENTS/OZK/CLAUDE.md | 31,456 | 280 | WHOLE (1–280; long lines 13, 16–17, 51, 71, 254 cut at 600–700 chars, tails not read) + FULL-DIFF |
| AGENTS/FLG/CLAUDE.md | 28,795 | 237 | WHOLE except 76–95 (that range seen only as diff context) + FULL-DIFF |
| AGENTS/GIBBS/CLAUDE.md | 20,423 | 194 | WHOLE (1–194; created 2026-10-14, after BASE) |
| AGENTS/CARL/CLAUDE.md | 49,224 | 290 | FULL-DIFF (:12, :83, :110) + changelist lines :68, :99, :148, :119. Not read whole |
| AGENTS/BROCK/CLAUDE.md | 31,318 | 271 | FULL-DIFF (:54, :72) + read :55–100 |
| AGENTS/SHADE/CLAUDE.md | 28,241 | 179 | FULL-DIFF (:79–95, :109, :117, :131) + changelist lines :148, :152 |
| AGENTS/CREED/CLAUDE.md | 39,856 | 235 | FULL-DIFF (:50, :64, :93, :103, :167–181, :207, :231) + read :36–66. Source read only; CREED not launched or messaged |
| AGENTS/LIQUID/CLAUDE.md | 27,139 | 215 | FULL-DIFF + changelist lines :33, :51, :60, :62–75, :80–90, :99 |
| AGENTS/LIQUID/CLOSEOUT.md | 12,428 | 183 | WHOLE (1–183) + FULL-DIFF |
| AGENTS/BOND/CLAUDE.md | 33,525 | 246 | FULL-DIFF (:234) + read :39–42, :145–151, :231–243 |
| AGENTS/BOND/CLOSEOUT.md | 10,482 | 74 | FULL-DIFF = empty (unchanged since BASE); no changelist line names it; not reread |
| AGENTS/HOMER/CLAUDE.md | 38,671 | 277 | FULL-DIFF (:200); :189 seen. No changelist line names HOMER |
| AGENTS/CORAL/CLAUDE.md | 29,239 | 243 | FULL-DIFF (:51) + read :95–116, :211, :242–243 |
| AGENTS/MARCO/CLAUDE.md | 32,539 | 273 | FULL-DIFF (:35, :45, :51, :56, :63, :231–233, :244, :261) + :58, :76 |

## Table A — 2026-10-08 changelist re-test at HEAD

Lines re-tested are every A/B line whose file:line names one of my 16 files. Sub-agent files (CARL `sub_agents/*`, CARL `SPAWN_PROTOCOL.md`, MARCO `sub_agents/TOURISM`) are not top-level harness files for these desks and were left out: F01–F07 are not re-tested here.

| line_id | file:line@HEAD | verdict | evidence quote (≤25 words) |
|---|---|---|---|
| D06 (LIQUID leg) | LIQUID/CLOSEOUT.md:156, :158 | STILL-LIVE (was KEEP; no action owed) | ":156 Read before editing — never `Edit` without `Read` in the same turn" · ":158 `trash` over `rm` for deletions" |
| D07 | LIQUID/CLOSEOUT.md:97 | FIXED | "3. Commit self-authored recipient inbox packets explicitly under root Git carve-out①." |
| D08 | LIQUID/CLOSEOUT.md:178 | STILL-LIVE | "\| `outbox/` \| Trigger-gated — only if cross-agent threshold fired \|" (contradicts :96 and :143 "`outbox/` is for PROME-action requests only") |
| D09 | LIQUID/CLOSEOUT.md:166 | FIXED | "Surgical six-section update (Now / Gates / Owed / Carried / Caveats / Pointers)" |
| D10 | LIQUID/CLOSEOUT.md:81, :173 | STILL-LIVE | ":81 keep `CALENDAR.md` (human twin) in sync — no event-set divergence; validate via … `boot.py --selftest`". `grep CALENDAR scripts/boot.py` = 0 hits at HEAD |
| D11 | LIQUID/CLOSEOUT.md:129 | FIXED | "Apply root CLAUDE.md Git Protocol for non-ff recovery, dirty-path overlap checks and escalation; never pull over concurrent dirty work or force." |
| D12 (LIQUID leg) | LIQUID/CLOSEOUT.md:37, :124 | STILL-LIVE (DEFER; no ruling recorded) | ":37 \| **Light** \| … \| STATUS surgical + MEMORY surgical \| Optional \|" · ":124 Chunk 5 — Git + report (Standard / Heavy; Light optional; Bounce skips)" |
| B13 | LIQUID/CLOSEOUT.md:84, :176 | STILL-LIVE | ":84 \| `workbook/FLOW.tsv` / `workbook/VX.tsv` \| A registry entry was touched (status change, new vector) \| Surgical row update \|" |
| B02 (LIQUID leg) | LIQUID/CLAUDE.md:51, :64 | STILL-LIVE | ":51 **Outbox:** `outbox/` — outbound signals you write for other agents" · ":64 Write a single `.md` file to `outbox/` per signal:" |
| B03 (LIQUID leg) | LIQUID/CLAUDE.md:60 | STILL-LIVE | "5. **Reply via outbox** only if: (a) you have new information the sender doesn't have…" |
| B35 (LIQUID leg) | LIQUID/CLAUDE.md:99 | STILL-LIVE | "**Output canon → root CLAUDE.md §Output Canon** (tables > prose · numbers > narrative · source+date every claim · file > verbal…" |
| B44 (LIQUID leg) | LIQUID/CLAUDE.md:33, :80–90; former :162–174 | CHANGED | :162–174 snapshot struck (now :164 "former June/August snapshot table … preserved verbatim in `archive/2026-10-14_staleness-sweep/CLAUDE.md`"); :33 "The old text said only "not yet logged", naming NO operation" and :80–90 BROCK-ruling story remain |
| D16 | BOND/CLAUDE.md:240 | STILL-LIVE | "\| `monitors/closeout_check.py` \| **Closeout 16 — THE single closeout invocation.**" (vs :18/:37/:237: `closeout_run.py` is C12) |
| B36 | BOND/CLAUDE.md:240 | STILL-LIVE | same clause as D16 (duplicate line ID across A and B) |
| B35 (BOND leg) | BOND/CLAUDE.md:41 | STILL-LIVE | "⚠️ **Always WRITE to files, not just chat.** If it's not in a file, it doesn't persist." |
| B44 (BOND leg) | BOND/CLAUDE.md:233–242 | STILL-LIVE (DEFER class) | ":241 `assertion_check.py` … ⚠️ **EXPIRED rule rebuilt 2026-08-21: it matched ISO dates only…**" — incident narrative still in tool rows |
| B02 (BROCK leg) | BROCK/CLAUDE.md:68 | STILL-LIVE | "→ `outbox/` per the Outbox Protocol below. Messaging system degraded … prefer surfacing to Will directly for time-sensitive items." |
| B11 (BROCK leg) | BROCK/CLAUDE.md:67 | STILL-LIVE | "**>60d old + not boot-read + not referenced by filename in STATUS.md or SCRATCH.md** → `git mv` to `archive/`" |
| B14 | BROCK/CLAUDE.md:62 | STILL-LIVE | "6c. **Run `python3 AGENTS/BROCK/scripts/brock_selfcheck.py`** **[ALWAYS]**" — still ordered before 7a (:63) and 7b (:64) |
| B17 | CARL/CLAUDE.md:68 | STILL-LIVE | "Skip when INDEX hasn't moved since last disposition pass — typical case." … "That sentence is left in place pending Will's word" |
| B43 | CARL/CLAUDE.md:148 | STILL-LIVE | "**VX.tsv:** Skip rows marked [STALE]. Only read rows from last 5 trading days." (:99 of the same file: "FROZEN (2026-06-26): `VX.tsv`") |
| B04 (CORAL leg) | CORAL/CLAUDE.md:102, :112 | STILL-LIVE | ":112 Delivery is direct (HERMES retired): drop the packet in the target agent's `inbox/` (coordinators PROME/WALTER route)" |
| B08 (CORAL leg) | CORAL/CLAUDE.md:211 | STILL-LIVE | "Non-ff abort → `git pull --rebase` + re-push; NEVER force." |
| B34 | CORAL/CLAUDE.md:243 | STILL-LIVE | "**Holds only `.gitkeep` since the 2026-06-30 prune `1cb18fbc3`**" — `ls archive/` shows 5 rotated files |
| B04 (FLG leg) | FLG/CLAUDE.md:154 | STILL-LIVE | "Delivery model: write the packet into the recipient's `inbox/` and **commit it yourself** … WALTER routes inbound news." |
| B09 | FLG/CLAUDE.md:207 | FIXED | "on a non-ff, follow root § Git Protocol session-end **step 3 exactly** (dirty-path overlap check BEFORE any rebase; overlap ⇒ stop and flag PROME)" |
| B32 (FLG leg) | FLG/CLAUDE.md:148 | STILL-LIVE | "Boot resolution is mechanized. Never leave OPEN-but-stale." |
| B08 (FLG:15 keep clause) | FLG/CLAUDE.md:15 | STILL-LIVE (kept by B08's design) | "**no push when spawned** — coordinator sweeps." |
| B03 (MARCO leg) | MARCO/CLAUDE.md:76 | STILL-LIVE | "5. **Reply via outbox** only if: (a) you have new information the sender doesn't have…" |
| B08 (MARCO leg) | MARCO/CLAUDE.md:58 | STILL-LIVE | "(ff-gated; non-ff → `git pull --rebase`, never force). Note any push abort in `SCRATCH.md`." |
| B10 | OZK/CLAUDE.md:100 | STILL-LIVE (DEFER) | "**If safe-push aborts non-ff, do NOT force** — note it in MEMORY and flag PROME/Will (a 2nd machine pushed = the tripwire)." |
| B40 | OZK/CLAUDE.md:51 | STILL-LIVE | "`market.py` lives at REPO ROOT … and `AGENTS/OZK/scripts/` contains only `boot.py`." — `ls` shows `boot.py`, `flng_watch.py` |
| B03 (REGINALD leg) | REGINALD/CLAUDE.md:77 | FIXED | "reply only for new information, a correction or a cross-agent trigger; move processed. No acknowledgment just to say received." |
| B08 (REGINALD leg) | REGINALD/CLAUDE.md:19 | FIXED | "Root CLAUDE §Git Protocol and docs/GIT_WORKTREE_PROCEDURES govern every pull/commit/closeout safe-push" |
| B11 (REGINALD leg) | REGINALD/CLAUDE.md:67 | FIXED | "follows root canonical rule/exemptions: >60d + not boot-read + not referenced by a live analytical/protocol doc" |
| B08 (SHADE leg) | SHADE/CLAUDE.md:152 | STILL-LIVE | "non-ff → `git pull --rebase` + re-push, never force — flag PROME/Will if it recurs" |
| B11 (SHADE leg) | SHADE/CLAUDE.md:148 | STILL-LIVE | "(c) not referenced by a current STATUS section: `git mv` to `archive/`" |

**Table A counts (37 rows):** FIXED 7 · STILL-LIVE 29 · CHANGED 1 · CANNOT-LOCATE 0.

## Table B — new findings (delta since BASE, plus canon contradictions met while reading)

Severity is in brackets after the class. "pre-BASE" marks a clause not touched since BASE that I report only because it is on the canon-contradiction list or is an unswept instance of a changelist class.

| id | file:line@HEAD | class | verdict | quote ≤25 words | proposed direction | strongest refuter considered |
|---|---|---|---|---|---|---|
| C01 | OZK/CLAUDE.md:71 | ROUTING [HIGH] | REWRITE | "and a threshold fire also goes as a packet to `AGENTS/REGINALD/inbox/` (self-committed)." | A threshold fire goes to `AGENTS/WALTER/inbox/`; the `REGINALD_CHANNEL.md` entry stays as the directed-edge analysis record. | WQ-484 made OZK → REGINALD a directed edge. But `_NETWORK.md:88` labels that edge "single-name print / credit reads" (analysis); the signal path is `_NETWORK.md:161` WALTER → REGINALD; and the same step ends "never route signals around it". Added 2026-10-22 (3de57ad6e) answering DAEDALUS packet item 6. |
| C02 | GIBBS/CLAUDE.md:129 with :136, :138 | ROUTING [MED-HIGH] | REWRITE | "Delivery: write the packet into the recipient's `inbox/` and **commit it yourself** (root carve-out ①)… never route signals around WALTER." | Split the send table: event rows (:136 NDFI reserve build / line tightening; :138 custody deposit outflow) → WALTER inbox; the four-item read (:135) stays direct analysis. | :82 "No thresholds and no grades at build", so every send may be analysis. But :136/:138 are event trips another desk must act on (root's signal class). DAEDALUS built GIBBS 2026-10-14, six days after the 10/08 changelist flagged the same FLG/CORAL pattern (B04). |
| C03 | REGINALD/CLAUDE.md:52 · OZK/CLAUDE.md:71 | TRADE [MED] | REWRITE | REGINALD:52 "send TERRY a packet for any candidate expression, labelled NOT-FIRED … with trigger state, size and risk in figures." | The desk sends trigger state, evidence and grade; TERRY sizes. Use WAL:157's form: "WAL never sizes, structures or recommends execution". | USER.md:47 does say "size and risk in figures", but of TERRY's own trades ("TERRY may bring trades…"); root "Trade construction = TERRY". The wording came from DAEDALUS's 10/22 packets (888fe9a50: REGINALD item 6, OZK item 7), which moved TERRY's card spec onto the desks. One batch left three bank desks with two opposite rules. Rule #5 approval is intact on all three. |
| C04 | OZK/CLAUDE.md:131, :280 (+:106, :108) | ROUTING [MED] | REWRITE | ":131 `outbox/` holds peer signals awaiting routing per `AGENTS/_NETWORK.md` (no auto-courier since HERMES retired 6/30)." | Name the address: signals → `AGENTS/WALTER/inbox/`, self-committed; `outbox/` = sender copy only. | :71 ends "News/signal routing is WALTER's". But no step puts the file in WALTER's inbox, and `_NETWORK.md` is a map, not a router. Changed 10/22. |
| C05 | WAL/CLAUDE.md:99 (+:130, :198) | ROUTING [MED] | REWRITE | ":99 One `.md` per signal … Outbox is the sender record; do not assume an automatic courier … Delivered → `outbox/delivered/`." | Add the address as REGINALD:54 does: signals → `AGENTS/WALTER/inbox/`; analysis → recipient inbox (carve-out ①). :130 "Signals for other agents (→ outbox)" → "(→ WALTER)". | :97 "WALTER remains the market-signal routing owner". That names an owner, not a delivery address; the :150–156 send table names direct targets. :99 changed since BASE. |
| C06 | GIBBS/CLAUDE.md:13, :24 | CANON-CONTRADICTION [MED] | REWRITE | ":13 1. **Read:** `AGENTS/GIBBS/CLAUDE.md` (this file) · `AGENTS/GIBBS/STATUS.md` · `AGENTS/GIBBS/workbook/PERIMETER.tsv`" | Add the explicit root `CLAUDE.md`/`AGENTS.md`/`USER.md` read and runtime identification (FLG:13 form) to the card and to boot step 1. | A Claude Code launch from the desk dir auto-loads root CLAUDE.md. But root says "do not assume a runtime auto-loads"; USER.md never auto-loads; GIBBS runs mostly as a PROME spawn (STATUS:3 "PROME spawn prome-03"). The 10/22 batch fixed this on OZK/FLG/WAL, not on GIBBS. |
| C07 | REGINALD/CLAUDE.md:42 | CARVE-OUT [MED-LOW] | REWRITE | "ACK lines are self-authored rows in a shared pair log (root carve-out ②): commit them path-scoped, never edit the peer's text" | Cite the authority that actually covers writing into `AGENTS/OZK/` and `AGENTS/WAL/` (the WQ-484 ruling or a PROME/Will confirmation that ② covers pair logs). Add root rule #2: no ACK while the peer is live in that file. | `OZK/REGINALD_CHANNEL.md:3` says "a log both agents append to", the practice is older than 10/22, and ② ("`AGENTS/SIGNALS.md` class") plausibly covers it. The risk is citation precision and concurrency, not authority abuse. |
| C08 | REGINALD/CLAUDE.md:52 | ROUTING [LOW] | REWRITE | "labelled NOT-FIRED when its trigger has not fired" | Say that when the trigger HAS fired, the fire routes via WALTER (:54) and the TERRY packet is its analysis companion. | :54 already sends threshold fires to WALTER; a careful reader joins the two lines. |
| C09 | GIBBS/CLAUDE.md:27 | GIT-SAFETY [LOW-MED] | REWRITE | "integrate and commit before `git mv` to `inbox/WALTER/processed/`." | "…then `git mv` and commit the rename in the same step" (REGINALD:48 wording). | A path-scoped closeout commit later picks up the rename. It is exposed only if another session bare-commits the shared index in between, which REGINALD:48 records happened 10/22 (WALTER `5854ecb98`). |
| C10 | REGINALD/CLAUDE.md:5, :81, :95, :139, :152, :159, :161, :166 · WAL/CLAUDE.md:19 · LIQUID/CLAUDE.md:14 | OTHER — Output Canon [LOW-MED] | REWRITE | REGINALD:5 "Re-check any append or2026-11-20." · :161 "VX.tsv13-column observations; KB.tsv15-column" · WAL:19 "September28 … October14, KB230" | Re-space the glued tokens. Root Output Canon: "never glue words together to save bytes". | The REGINALD rewrite was PROME-accepted 10/20 and byte-driven. Root names exactly that remedy as forbidden. REGINALD:87 shows the spaced form "any append or 2026-11-20". |
| C11 | CREED/CLAUDE.md:40–54 (new row :50) | ROUTING [MED; pre-BASE except :50] | REWRITE | ":54 Standing rule: route to the **domain owner**, one signal at a time… CREED reports inbox dispositions; PROME `git mv`s." | Signals → WALTER, analysis direct. Drop "PROME `git mv`s": PROME commits `PROME/` only (root Scope note); the desk files its own inbox. | The new :50 row is info-only 🟡 and CREED is Tier-2, launched only on Will's word. Route matrix rows are "what CREED sends", which may be analysis. |
| C12 | BOND/CLAUDE.md:150–151 | TRADE / EXPIRY [MED-LOW; pre-BASE] | REWRITE | ":150 Convergence downgrade (trim): Conditions that weaken but don't kill the thesis. Partial exits." ":151 Time-based: Mandatory review checkpoints (e.g., 60-DTE for options positions)." | Point exit and trim language at TERRY (root rule #7: "Trimming = thesis broken"); drop the DTE checkpoint (USER.md:45, no expiry nagging). | Root says rules 6–7 belong to TERRY and domain desks may skip them. This may be a shared blueprint category list (not checked fleet-wide). It is a review rule for the desk, not a reminder to Will. |
| C13 | BROCK/CLAUDE.md:71 | GIT-SAFETY [LOW] | REWRITE | "(ff-gated; non-ff → `git pull --rebase`, never force)." | "non-ff → root §Git Protocol session-end step 3 (overlap check first); never force." | Same class B08 rated LOW. BROCK was not in B08's list, so this is a new instance. A plain rebase refuses on a dirty tree, so it is less exposed than an autostash. |
| C14 | WAL/CLAUDE.md:93 · OZK/CLAUDE.md:116 · CORAL/CLAUDE.md:95 | ROUTING [LOW] | REWRITE | WAL:93 "reply via outbox only for new info / corrections / threshold triggers" | B03 wording: reply direct to the sender's inbox (carve-out ①), signals via WALTER. | B03 named only MARCO/LABOR/HENRY/REGINALD/LIQUID. WAL:99 itself calls outbox "the sender record", so a reply left there reaches nobody. |
| C15 | WAL/CLAUDE.md:105 · OZK/CLAUDE.md:152 | DUPLICATE [LOW] | STRIKE | WAL:105 "**Tables > prose. Numbers > narrative.** Source + date every claim (root Output Canon)." | Strike the restatement; keep the desk-specific source-tag line beneath it. | Changelist B §111 named both as unswept B35 residue. Harmless, but root says agent files cite and do not restate. |
| C16 | WAL:69 · OZK:54–62 · FLG:27 · CARL:83 · BROCK:54 · HOMER:200 · CORAL:51 · SHADE:131 · MARCO:45 · LIQUID:39 · CREED:103 · REGINALD:47 · GIBBS:26 | MECHANIZED / DUPLICATE [LOW] | REWRITE | CARL:83 "Missing required fields return rc2 without writing." | One line per desk: run the check; on rc 1 write the receipt per `corrections_boot_check.py --help`; the writer refuses incomplete receipts. | WQ-399 / SIG-W-20261008-033 told each desk to write the forms into its own charter (C4 own-charter edit), so the copies obey an instruction. They already differ: GIBBS:26 omits CONTESTED; CORAL forbids tabs and line breaks; CARL says CONTESTED needs no field. Striking them needs WALTER/PROME agreement. |
| C17 | OZK/CLAUDE.md:36 · FLG:15 · GIBBS:15, :30, :173 vs WAL/CLAUDE.md:34 | CANON-CONTRADICTION [LOW] | REWRITE (PROME/owner call) | OZK:36 "**do NOT push — PROME sweeps.**" vs WAL:34 "No blanket spawned-mode push exception or local-only commit restriction overrides root." | Settle one fleet reading. Root lists only TERRY and WALTER as auto-push exceptions. | B08 kept the FERT/FLG spawned no-push on purpose. Not pushing is safe: local commits ride the next push. |
| C18 | SHADE/CLAUDE.md:79–95 | HISTORY-IN-STEP [LOW] | REWRITE | ":91 State 2026-10-15 \| ❌ **NOT MET (first prospective grade, L673)…**" plus three prior "State" rows and four "SIGN LEG" reading rows | Keep the letter and the amendment rows (:81–83). Move dated readings and State rows to STATUS or `research/` (SHADE:117: STATUS is "Canonical on live state"). | The trigger letter lives in the charter by design, and readings beside the letter help grading. But they grow with every grade and repeat STATUS. |
| C19 | CREED/CLAUDE.md:207 | DUPLICATE / STALE [LOW] | REWRITE | "**10/21 close −11.48pp TR (10/20 −9.15), past the band, the fire stands**" | Strike the figure; keep "read `VX-CREED-7.01`, not this line". | It was refreshed 10/21, and the line already tells the reader to use VX. |
| C20 | GIBBS/CLAUDE.md:149–158 | HISTORY-IN-STEP [LOW] | REWRITE | "## FIRST LIVE SESSION (PROME spawn, DOCKET L704, 2026-10-19 — FITB's print day)" | Mark it SPENT 2026-10-21 (GIBBS STATUS:5 "banner struck 2026-10-21") or move it to the archive. FLG:175 shows the SPENT form. | :28 gates the section on the STATUS banner, which is struck, so no session runs it. |
| C21 | FLG/CLAUDE.md:175–192 | HISTORY-IN-STEP [LOW; pre-BASE] | STRIKE (move to archive, leave a pointer) | "⛔ **Do not re-run this list.** It is retained as the record of what was done and what was left." | One-line pointer to an archive copy. | It is clearly marked SPENT, so the risk is bytes, not misreading. |
| C22 | FLG/CLAUDE.md:199 | CANON-CONTRADICTION [LOW; stricter] | KEEP (note) | "**STATUS.md ≤250 lines and ≤32,000 B** … At ≥75% of the byte budget (24,000 B)" | Optional: use 32,550 / 24,412 (GIBBS:165 form). Root says owners choose rotation, "never the number". | 32,000 is stricter than root and safe. |
| C23 | LIQUID/CLOSEOUT.md:143, :146 · BROCK/CLAUDE.md:83 | ROUTING [LOW; pre-BASE] | REWRITE | LIQUID:146 "**`HEARTBEAT.md`** — flag to Prome via outbox; never commit yourself" | PROME requests → `PROME/inbox/` (root; COMPLETION_SPEC method 1). `outbox/` = optional sender copy (REGINALD:54 and OZK:37 got this fix 10/22). | PROME may still sweep desk outboxes. Root, though, reserves `outbox/*to-PROME*` for signal/routing work and names `PROME/inbox/` for requests. |
| C24 | LIQUID/CLOSEOUT.md:180 · BROCK/CLAUDE.md:69 | STALE-POINTER [LOW] | REWRITE | LIQUID:180 "\| `~/.claude/.../memory/` (auto-memory) \| Selective; Heavy tier only \|" | Align with LIQUID:106 "root `memory/auto/`". | On this box `~/.claude/projects/-home-willi-Research-workspace/memory` is a symlink to `memory/auto` (readlink checked), so Claude Code writes land in the right place. It matters only on another runtime. |
| C25 | WAL/CLAUDE.md:156 | STALE-POINTER [LOW; pre-BASE] | REWRITE | "\| Buyback execution / capital action vs guide \| TERRY, FORGE \| 🟡 \|" | "TERRY, PROME (PROME owns the FORGE mirror)". OZK:218 made this exact fix 10/22. | None. |
| C26 | OZK/CLAUDE.md:45 | EXPIRY [LOW; pre-BASE] | REWRITE | "3. **Read `CALENDAR.md`** — upcoming dates, roll deadlines, signal thresholds" | Drop "roll deadlines". OZK:192 already says Will manages his own expiries (USER.md 10/20). | Reading a calendar is not a reminder to Will. The risk is that a boot-read "roll deadline" turns into one in a brief. |
| C27 | WAL/CLAUDE.md:40 · WAL:69 · OZK:51, :254 · FLG:27 · LIQUID/CLAUDE.md:33, :80–90 | HISTORY-IN-STEP [LOW] | REWRITE | WAL:40 "Skipping it caused a breach on 10/22." · WAL:69 "*(Wired 2026-08-28 … inserted by WAL on Will's in-session word, not on the peer relay.)*" | Keep the action; move the story to each desk's provenance home (B44 class instruction). | Short incident tails cost little and motivate the rule; the 7/7 criterion still sends WHY to an on-demand doc. |
| C28 | MARCO/CLAUDE.md:231–233 | DUPLICATE [LOW] | REWRITE | ":231 \| Canadian Visitors \| **−28.72%** (Sep '26 2-yr stack vs 2024, BREACHED 11th month…" | Keep threshold and implication; live readings → STATUS (CORAL-owned FL figures cited, not copied). | It is a domain reference table, edited 10/22 to current figures, so it is not stale today. |
| C29 | BROCK/CLAUDE.md:72 | GIT-SAFETY [—] | KEEP | "Preserve unexpected staging belonging to other owners; do not unstage or otherwise alter it." | None. It replaces the BASE text "use `git restore --staged <file>` to unstage them" (a foreign-index mutation). | — |
| C30 | REGINALD/CLAUDE.md:48 | GIT-SAFETY [—] | KEEP (stricter than root) | "**Commit every `git mv` (inbox filing, rotation) in the same step it is made**" | None. | — |
| C31 | REGINALD:54 · OZK:37 · WAL:35 | CARVE-OUT [—] | KEEP | OZK:37 "write the dated delivery memo to **`PROME/inbox/…`** … **and** pathspec-commit it yourself (root carve-out ①)" | None. The 10/22 fix aligns with COMPLETION_SPEC method 1. | — |
| C32 | WAL/CLAUDE.md:88 | DUPLICATE [LOW] | KEEP | "pathspec commits from repo root (`git commit AGENTS/WAL/<file> -m "..."`; … never `git reset HEAD` … follow root session-end step 3 exactly" | Optional: replace with a pointer to `docs/GIT_WORKTREE_PROCEDURES.md` § Before committing. | It matches procedure steps 1, 2, 4 and 5 and is not weaker. A pointer would be leaner, but this is not a safety issue. |
| C33 | REGINALD/CLAUDE.md:34–35 | MECHANIZED [LOW] | KEEP | ":35 Since 2026-10-22 it also runs … the FLG ladder, corrections and both staleness lines." | None. | 7b (boot.py) is optional ("skip for quick tape boots"), so 7a is the only unconditional staleness run (checked: boot.py:56 carries `--trade`). |

**Table B counts (33 rows):** REWRITE 25 · STRIKE 2 · KEEP 6. By severity: HIGH 1 (C01) · MED-HIGH 1 (C02) · MED 4 (C03–C06) · MED-LOW 3 (C07, C11, C12) · LOW-MED 2 (C09, C10) · LOW 19 (incl. KEEP notes C22, C32, C33) · unrated KEEP confirmations 3 (C29–C31).

## Top 5 by severity (both tables)

1. **C01, OZK:71 [HIGH].** The 10/22 text sends threshold fires straight to `AGENTS/REGINALD/inbox/`, around WALTER, in the same step that says never to route around it.
2. **B04 FLG:154 still live, and GIBBS:129 (C02) copies it [HIGH / MED-HIGH].** Both deliver every send-table row direct to the recipient. GIBBS was built by DAEDALUS on 10/14, after the 10/08 changelist had flagged this exact pattern. CORAL:112 (B04) is also still live.
3. **C03 [MED].** One DAEDALUS batch gave three bank desks two opposite trade-idea rules. REGINALD:52 and OZK:71 have the desk supply "size and risk in figures". WAL:157 says "never sizes". USER.md:47 assigns that spec to TERRY's cards.
4. **Outbox signal lanes with no named router [MED]:** C04 OZK:131/:280; C05 WAL:99/:130/:198; B02 LIQUID:51/:64 still live; B02 BROCK:68 still live, which also says "prefer surfacing to Will directly".
5. **C06 GIBBS:13/:24 [MED].** No explicit read of root CLAUDE.md/AGENTS.md/USER.md and no runtime identification, on a desk that mostly runs as a PROME spawn.

Close behind: the restated plain-rebase non-ff recipes, still live on SHADE:152 (which also escalates "if it recurs"), MARCO:58 and CORAL:211, plus the new BROCK:71 instance (C13). These are LOW per B08's binding narrowing.

## Where I could be wrong

- **C01/C02/C04/C05 assume a "threshold fire" is a WALTER-routed signal under root §DM v1.** If WQ-484 or a PROME ruling I did not find explicitly allows OZK → REGINALD fire packets direct, C01 drops to LOW. I searched `PROME/DOCKET.tsv` L793 and `_NETWORK.md`; I did not read `MESSAGING/CROSS_SESSION_MESSAGING.md` or the WQ-484 proposal file.
- **C03:** Will's own words in another session may have extended "size and risk in figures" to desks. I saw only USER.md:47 and the DAEDALUS packets.
- **C07:** carve-out ② may be meant to cover pair logs. I found no ruling either way.
- **C12:** BOND's exit-rule categories may be a fleet blueprint section. If so, the fix belongs in the blueprint, not in BOND.
- **Not read whole:** CARL, BROCK, SHADE, CREED, LIQUID/CLAUDE.md, BOND, HOMER, CORAL and MARCO. Each was covered by full diff plus changelist lines only. Pre-BASE contradictions outside the ranges I read are not covered. FLG 76–95 and the OZK/WAL long-line tails were not read.
- **Table A** line numbers were found by content grep at HEAD. Where a changelist line named two spans (e.g. B02 LIQUID :49/:62), I matched both by content (:51/:64).

## Working notes (incremental, kept as written)

### LIQUID/CLOSEOUT.md
- D07 FIXED :97; D08 STILL-LIVE :178; D09 FIXED :166; D10 STILL-LIVE :81/:173 (boot.py has 0 CALENDAR refs at HEAD); D11 FIXED :129; D12 STILL-LIVE :37/:124; D06 still present :156/:158 (KEEP line); B13 STILL-LIVE :84 and :176.
- New: :106/:118 now say root `memory/auto/` but :180 still names `~/.claude/.../memory/` (internal contradiction, LOW).

### REGINALD/CLAUDE.md — WHOLE (1–166 read; file was rewritten 10/20, 81+/246- since BASE)
- B03 FIXED :77; B08 FIXED :19; B11 FIXED :67.
- Findings drafted: glued words (Output Canon) across :5,:81,:95,:139,:152,:159,:161,:166; carve-out ② stretch for ACKs in peer-dir REGINALD_CHANNEL.md :42; trade-idea route :52 "size and risk in figures" vs WAL :157 "never sizes"; :52 fired-trigger packet to TERRY directly; :34/:35 staleness duplicated by boot.py (LOW); :68 root-closeout restatement (LOW).

### WAL/CLAUDE.md — WHOLE (1–198 read) + FULL-DIFF
- Findings drafted: :99 signal packet/outbox lane without WALTER address (changed since BASE); :130 and :198 outbox = signals out (pre-BASE residue); :93 "reply via outbox" (B03 class, unswept); :105 Output Canon restatement (B35 class, named unswept in changelist B §111); :157 trade-idea row contradicts REGINALD :52 on sizing; :156 "FORGE" as a signal target (not an agent); :40 history tail; :69 history + WQ-399 restatement; :70 listing now mechanized by :60 (dup).

### OZK/CLAUDE.md — WHOLE (1–280; lines 16–17, 51, 254 truncated at 600–700 chars in my read, tails not read) + FULL-DIFF
- B10 STILL-LIVE :100; B40 STILL-LIVE :51 (scripts/ holds boot.py + flng_watch.py at HEAD).
- Findings drafted: :71 threshold fire → AGENTS/REGINALD/inbox/ direct (HIGH routing, added 10/22 3de57ad6e); :131/:280 outbox "awaiting routing per _NETWORK.md" names no router; :71 size-in-figures (from DAEDALUS packet item 7, transposed from USER.md's TERRY card spec); :116 reply via outbox (B03 class); :152 Tables>prose; :36 spawned "do NOT push — PROME sweeps" vs WAL :34 (inconsistent, stricter, LOW); :105 "routed in by PROME" stale.
- DAEDALUS 10/22 packets (888fe9a50) told REGINALD and OZK "with trigger state, size and risk in figures"; USER.md:47 gives that spec to TERRY's cards, not to desks.

### FLG/CLAUDE.md — WHOLE (1–237; lines 75–95 read via diff context only) + FULL-DIFF
- B09 FIXED :207; B04 STILL-LIVE :154; B32 STILL-LIVE :148; B08 (FLG:15 spawned no-push, kept by B08) still :15.
- Findings drafted: :154 + :160–166 send table — threshold fires delivered straight to recipient inbox (HIGH routing, pre-BASE, B04); :199 local 32,000 B budget (owner-set number; stricter); :175–192 spent FIRST LIVE SESSION protocol retained (history); :16 unconditional SendMessage; :27 history tail.

### GIBBS/CLAUDE.md — WHOLE (1–194, created 2026-10-14 after BASE)
- Findings drafted: :13 and :24 boot omit explicit root CLAUDE/AGENTS/USER read + runtime identification (COMPLETION_SPEC; the 10/22 batch added it to OZK/FLG but GIBBS, built 10/14 by DAEDALUS, never got it); :129 direct-to-inbox delivery for P1 send rows :136/:138 alongside "never route signals around WALTER" (same B04 pattern the 10/08 changelist had flagged); :27 "commit before git mv" leaves the rename uncommitted (REGINALD :48 incident class); :149–158 FIRST LIVE SESSION spent 10/21 per STATUS:5 but not marked; :16 unconditional SendMessage; :15/:30/:173 spawned no-push.

### Remaining desks (diff-scoped)
- CARL — FULL-DIFF (3 lines: :12, :83, :110) + changelist lines B17 :68, B43 :148, git step :119 read. File 49,224 B not read whole.
- BROCK — FULL-DIFF (:54, :72) + read :55–100 (closeout + mail + signal protocol).
- SHADE — FULL-DIFF (:79–95 trigger-letter rows, :109, :117, :131) + changelist lines :148, :152.
- CREED — FULL-DIFF (:50, :64, :93, :103, :167–181, :207, :231) + read :36–66 (route matrix + traps 1–5). Source read only; not launched or messaged.
- LIQUID/CLAUDE.md — FULL-DIFF + changelist lines :33, :51, :60, :80–90, :99.
- BOND/CLAUDE.md — FULL-DIFF (:234) + :39–42, :145–151, :231–243. BOND/CLOSEOUT.md — no diff since BASE (FULL-DIFF = empty; not reread).
- HOMER — FULL-DIFF (:200); git step :189 seen.
- CORAL — FULL-DIFF (:51) + :95–116, :211, :242–243.
- MARCO — FULL-DIFF (:35, :45, :51, :56, :63, :231–233, :244, :261) + :58, :76.
