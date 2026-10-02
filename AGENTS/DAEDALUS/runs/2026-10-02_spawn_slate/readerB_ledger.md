COLDREADER · SLATE_h0.md · 20538 B · 44 claims
SCORE: 18/44 ✅ · 24 ⚠️ · 2 ❌

(Spawner fence: read ONLY the slate; no other file opened, no pointer tested. Read at 13:44 EDT Fri 2026-10-02, 1 min after generation.)

❌ 8 "In flight today — do not spawn: none" — L8 `- **In flight today — do not spawn:** none` vs L122 `### CRUISE — NO SPAWN — … · IN-FLIGHT today (re-ping, never spawn)` / L132 `1-SPAWN cruise-1002 (cites D:L502) → IN-FLIGHT` and L138 `### MIDAS — … · IN-FLIGHT today (re-ping, never spawn)` / L147 `1-SPAWN midas-1002 (cites D:L582) → IN-FLIGHT`. The summary says zero desks in flight; two stanzas say two are.
❌ 41 Past-due rows named in stanzas are missing from the census — L119 (BRENT) `` `D:L173` (09-30), … `D:L384` (09-22) `` and L150 (MIDAS) `` `D:L173` (09-30) `` (both listed as "due or within the window") vs L162 `32 row(s)` + L16 `32 rows in … census rows 32 · OK`. Census lines L164–L195 contain no D:L173 and no D:L384, even though both dates are before the as-of date. So either the census leaves out due rows (and the conservation "OK" proves nothing), or those dates don't mean "due". The slate never says which.

⚠️ 2 "horizon +0d" (L1, L162), yet every stanza has "Would also fit (not why-now; +14d)". Two windows, one artifact. "Not yet due (horizon): none" (L13) can't be anything else at +0d.
⚠️ 5 "No dates are stored here" (L3), in a file that is mostly dates. Probably means "no state is persisted here", but it doesn't say so.
⚠️ 7 "VULCAN (slot 1 of 4)" (L7). The summary carries no timing caveat. The row itself says (L27) "a spawn before ~16:00 ET cannot take it", and the slate was generated at 13:43. "Slot 1 of 4" also suggests a free slot, but L15 admits the slate can't know how many of today's 13 spawns used up this boot's cap.
⚠️ 10 L10 lists CRUISE and MIDAS as "Owner returned — PROME's read + write-back owed" while both are IN-FLIGHT. Reading a return while the session is still running may mean reading half a return.
⚠️ 15 "Will-owned: 0 — no stanza; every one is in the census below" (L14). "Every one" could mean the 24 PROME rows or the 0 Will rows.
⚠️ 16 Cap: "slot 1 of 4" (L7, L20), "cap 4/boot" (L148, quoted inside MIDAS's row) and "C6 (eight) needs EVERY wake that boot to be a due catalyst/review row" (L15). C6 is never defined. Is the cap 4 or 8? Do re-pings count toward it? That is "unruled (DOCKET L444)". A "boot" is never defined either.
⚠️ 19 VULCAN's bounded assignment is ready to paste at 13:43, but its own text says a pre-16:00 spawn can't do the work. The slate hands that judgment to PROME (L29) instead of deciding it.
⚠️ 20 VULCAN "Inputs the rows name: AGENTS/VULCAN/docket/CATALYSTS.tsv · …MU-FQ4-grade.md" (L28). Neither path appears in the quoted row text, so the reader can't tell where they come from.
⚠️ 24 SHADE PARTIAL rests on the "hedge word 'owed'" (L42), found in "state lines, owed dates". That looks like a keyword match, not an actual hedge.
⚠️ 25 SHADE: the PROME annotation is cut off mid-sentence ("lump […]", L43) and covers one leg (BROCK) out of four.
⚠️ 26 D:L182: "4 legs (SHADE gated-US-routes + AARe Note-14 … · BROCK … · CREED …)" lists 3 items separated by "·". Whether "+" splits one leg into two is the ROW's ambiguity, and the withdrawal rule depends on it: "≥2 legs finding an existing surface ⇒ … WITHDRAWN".
⚠️ 27 SHADE is "NO SPAWN", yet a bounded assignment is printed. ORCH_LOG shows no SHADE session today, so "re-ping" can only mean a spawn or an inbox packet. The slate doesn't say which.
⚠️ 28 "the NEWEST strong return decides the class" (L58, L101, L115). "Strong" is undefined. The list order (newest first or last?) is undefined. Several returns are hidden as "+N more".
⚠️ 29 ORCH_LOG targets point to PROME/inbox/… (L60, L80, L102, L116), but the same packets are cited at PROME/inbox/processed/… (L57, L78, L99, L114). Stale paths from the working tree.
⚠️ 30 FERT row "rock re-plateaus at exactly $170.0, 72%". The 72% has no stated basis (probability? confidence?).
⚠️ 31 LIQUID PARTIAL hedge "unpublished" (L79) refers to a "10/1 credit cell". The row D:L493 is a repair/owed set (①hy_oas_watch… ②≥ vs >…). The hedge may come from a different task than the row.
⚠️ 32 The "last self-commit" hash in the census differs from the stanza's citing commit (LIQUID d62500207 vs d14cb1d49; HENRY 4c4986fa1 vs 8d9de915e/ec553941b; BRENT 14a1d22d1 vs c0f0f9b4e). That's plausible, but never explained.
⚠️ 33 HENRY ALREADY ANSWERED is matched on "cites id FORUM-7" (L98–100), not on key D:L475. It's an id match plus "+16 more". The row also names BOND and NEXUS (L155), and the reader can't tell whether their legs are part of the answer.
⚠️ 34 "row start" (L24, L166) is undefined. For HENRY it is 09-25 against a due date of 10-01, and for BRENT 08-14 against 10-02, so it is not the due date. DARK and ACTIVE are both computed from it.
⚠️ 37 MIDAS is ALREADY ANSWERED (L145), but its row's timing words say "after 15:30 ET so one wake covers both" (L148), and the returned packet is titled "…day31-reading-question". MIDAS may still owe a post-15:30 reading, plus a question PROME has to answer. "Both" is undefined.
⚠️ 38 "ACTIVE" means two things: "ROSTER ACTIVE" (roster status, L22 etc.) and "[ACTIVE]" (owner self-committed since row start, L39 etc.). Same token, different facts.
⚠️ 39 "lane WQ-184 L0 (the only lane computed here)" appears in every stanza. It implies other lanes exist that weren't computed, i.e. due work this slate doesn't show. WQ-184 L0 itself is undefined.
⚠️ 40 The second-desk list (L155) leaves out D:L182, whose row text names BROCK and CREED legs. L157 concedes: "this list cannot" tell co-grader from informed.
⚠️ 42 The census itself carries open defects in the generating instrument: D:L368 "`spawn_list.py` SUPPRESSED ALL THREE DOCKET ROWS DUE TODAY" and D:L455 "`spawn_list.py`'s DESK-COMMIT PATTERN MISSES THE FLEET'S MOST COMMON…". If the slate is built on spawn_list (L153, L162), its DARK/ACTIVE basis (self-commit detection) is suspect, and the slate says nothing about this.

✅ 1 generated 13:43 EDT, as-of Fri 2026-10-02 (wall clock Fri, 13:44) · 3 HEAD 2a4344d00 (matches session git snapshot) · 4 20,538 B = 63% of 32,550 (wc -c 20538) · 6 ALREADY ANSWERED = evidence class (definitional) · 9 Unknown: none · 11 hedge list = SHADE/FERT/LIQUID stanzas · 12 receipt gap none · 13 not-yet-due none · 14 PROME 24, oldest 15d (D:L381 Δd 15) · 17 conservation 8+24=32, census lines count 32 · 18 DARK defined at L25 · 21 inbox drains whole (clear) · 22 VULCAN L250 +3d · 23 SHADE 2d overdue = census Δd 2 · 35 BRENT ALREADY ANSWERED · 36 CRUISE stanza self-consistent · 43 class counts DARK1/ACTIVE7/PROME24/WILL0 = rows · 44 L444 "unruled" consistent L15/L188

POINTERS: 0/30 tested (spawner fence: no lookups). 12 file paths + 18 commit hashes; HEAD only cross-checked against session context. dead: untested
ONE-LINE VERDICT: no. A cold coordinator who reads "Read this first" spawns VULCAN at 13:43 into a slot the slate can't vouch for, to do a post-16:00 job it can't yet do. Also believes nothing is in flight while two desks are.

---
## Answers to the spawner's 1–7

### 1. Spawn now?
None now. VULCAN only, at or after ~16:00 ET, and only if a cap slot is confirmed.
Words that told me: L27 "A POST-CLOSE reading: a spawn before ~16:00 ET cannot take it."; L29 "PROME judges whether a wake now is early".
Assignment (verbatim, L27): "VULCAN: 1 registered row due. 1) D:L564 (due Fri 10/02): "VULCAN FRIDAY POST-CLOSE SLOT — `mag7.py` slot 4 + GPU reading 4 (the first `GPU_SERIES.tsv` row). A POST-CLOSE reading: a spawn before ~16:00 ET cannot take it. The S2 memory spot series died the same way (0 of 8 scheduled slots taken, the 9/29 slot recorded MISSED) — this row exists so the next series does not." Return: your own record updated + one packet to PROME/inbox/ citing each row key."
Caveat: the spawn also drains 6 inbox packets (L33). ListAgents in the same minute first (L3).

### 2. Read + write-back only (no desk session)
| row | first artifact |
|---|---|
| HENRY D:L475 | PROME/inbox/processed/2026-10-02_from-HENRY_FORUM-7-final-and-gamma.md (FINAL), but it's unclear whether 8d9de915e is newer |
| BRENT G:GATE-BRENT-COT-35B | PROME/inbox/processed/2026-10-02_from-BRENT_10-1-proxies-oil-move-COT-review.md |
| CRUISE D:L502 | commit 30cd09b1e (COMPLETION block on the delivery memo); the memo path isn't given. Wait until it's no longer in flight |
| MIDAS D:L582 | PROME/inbox/2026-10-02_from-MIDAS_WQ-352-ENCODED-and-day31-reading-question.md. Not clean: carries a question + a post-15:30 timing word |

### 3. Read, then re-ping vs wait
| row | open | looking for |
|---|---|---|
| SHADE D:L182 | commit ffd823d80, then the D:L182 PROME annotation + FORUM …/03_PROME_rulings-record.md | did SHADE's own leg land; CREED leg status; is it already ≥2 legs ⇒ WITHDRAWN; is "owed" a real hedge |
| FERT D:L288 | PROME/inbox/processed/2026-10-02_from-FERT_pink-sheet-october-T11.md | does "T11 armed" auto-wake FERT on publication (⇒ wait; resolve_by 10-09) or does it need a manual re-check later today |
| LIQUID D:L493 | PROME/inbox/processed/2026-10-02_from-LIQUID_10-1-credit-cells-and-packets.md | which owed items ①②… are done; is "PENDING"/"unpublished" about D:L493 at all |

### 4. Do NOT spawn
CRUISE and MIDAS (in flight: re-ping only). HENRY and BRENT (answered: read only). SHADE, FERT, LIQUID (NO SPAWN until the return is read). All 24 PROME-owned rows ("do it, never spawn"). VULCAN before ~16:00.

### 5. Slots
My plan: 1 spawn (VULCAN, post-16:00), plus 0–3 re-pings whose cap status is unruled (D:L444). Cap = 4/boot (L7, L148), or 8 under the undefined "C6". 13 1-SPAWN rows today; how many fall in this boot is "PROME's knowledge". The slate can't confirm even one free slot.

### 6. What I couldn't tell (ranked by risk of a wrong action)
1. VULCAN appears as a spawn candidate at 13:43 with a work item that needs ≥16:00 (#7/#19)
2. "In flight: none" vs CRUISE/MIDAS IN-FLIGHT (#8)
3. Cap: 4 vs 8, C6, what a boot is, are re-pings cap-bearing, is "slot 1 of 4" real (#16)
4. MIDAS "ALREADY ANSWERED" vs the "after 15:30 ET" wake and a reading-question packet (#37)
5. What "re-ping" means for a desk with no live session (SHADE) (#27)
6. Hedge detection is keyword-based ('owed' in "owed dates"; 'unpublished' about a different task) (#24/#31)
7. The instrument's own open defects in the census (D:L368, D:L455) and no warning about them (#42)
8. Past-due named rows D:L173/D:L384 absent from the census (#41)
9. ACTIVE ×2 meanings; "row start", "strong return", "WQ-184 L0", "lane", "DARK" vs roster (#34/#38/#39/#28)
10. HENRY answered via id FORUM-7, not the row key; BOND/NEXUS legs (#33)
11. D:L182 "4 legs" lists 3 (#26)
12. horizon +0d vs +14d; "No dates stored" (#2/#5)
13. Noise I'd skip: the "named, not first owner" lists, ORCH_LOG brace-truncated paths, the +14d sections, the 24-row PROME census (except due-today L210/L487/L503)

### 7. Load-bearing claims not verifiable from the slate
- every ALREADY ANSWERED / PARTIAL class (rests on commits/packets not shown)
- DARK for VULCAN (no self-commit since row start; depends on a commit-pattern match flagged defective in D:L455)
- 13 1-SPAWN rows today; IN-FLIGHT state of CRUISE/MIDAS
- cap 4 / C6 eight
- every "last self-commit" hash/date; "within cadence"
- the 6/4/2/4/2/1/2/1 inbox counts
- the ROSTER ACTIVE status of each desk
- conservation completeness (contradicted by #41)
- all 30 pointers (untested by fence)

### Time estimate
~15 minutes to answers 1–5. About 5 of those went on deciding whether VULCAN is "spawn now" or "wait", and on reconciling L8 against the CRUISE/MIDAS stanzas.
