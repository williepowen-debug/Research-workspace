SCORE: 31/53 ✅ · 19 ⚠️ · 3 ❌   (COLDREADER · PROME/SCRATCH.md 22719 B + PROME/archive/SCRATCH_ROTATED_2026-09-24_prome-26.md 5314 B [measure.py] · 53 claims)

COLDREADER · PROME/SCRATCH.md (+ rotation archive) · 22719 B / 5314 B · 53 claims
SCORE: 31/53 ✅ · 19 ⚠️ · 3 ❌

## ❌
❌ 4 No path from SCRATCH to the cut text. SCRATCH L4: "History → [pre-Phase-2 snapshot](archive/SCRATCH_ROTATED_2026-09-21_boot-phase2.md); it includes the prior rotation pointers" is the only history pointer. `grep -c "SCRATCH_ROTATED_2026-09-24\|prome-26.md" PROME/SCRATCH.md` = 0. On the other side, archive L1 says: "verbatim segments cut from `PROME/SCRATCH.md` at 79% of budget". The archive exists (untracked `??`), but a reader starting at SCRATCH cannot reach it. The archive answers Q4 only because the spawner named it.
❌ 11 Deck republish receipt. SCRATCH L8: "Deck republish authorized (Will 13:37) and executed at step 11 AFTER the commit — receipt in `PROME/reports/2026-09-24_prome-26-closeout.md`". SCRATCH L14 repeats it: "The hosted Deck was republished at this closeout (v39/v5 — receipt in the closeout report)". Result of `ls PROME/reports/ | grep 2026-09-24`: only `2026-09-24_prome-4d-closeout.md`, so the pointer is DEAD. The text states an event that comes after the commit in the past tense, before the commit. At the moment it is unverifiable.
❌ 19 TERRY 007 state. SCRATCH L23: "004 / `GATE-TERRY-007` — sealed in substance; no action owed. … TERRY records MOOT ⇒ NO-VERDICT." SCRATCH L11: "⚠️ TERRY 007 MOOT record was NOT on TERRY's artifact at 09:2x 9/24 (review_by 9/24) — if the GATES check flags it at the 9/25 boot, doorbell/spawn TERRY (5th candidate → slate)." One line says no action is owed and the other names a possible spawn. "records" could mean the record is done or could be an instruction.

## ⚠️
⚠️ 9 L8 says "DOCKET L466 registered (MARCO-DR-1 wake 11/02, needed-by 11/16)". DOCKET.tsv has 466 lines, so row L466 exists. It falls beyond the 21-day view window, and the view's crc does not match (#10), so a reader cannot tell from the page whether the view includes it. The year is implied.
⚠️ 10 L38 "docket-crc32 3718508229" does not match either measure.py figure for the current PROME/DOCKET.tsv (3584978358 / no-final-nl 3242598926). Either the perimeter or basis is unstated, or the view is older than the last DOCKET edit.
⚠️ 15 L11 says "three new packets in `AGENTS/BRENT/inbox/WALTER/`" (001–003, 13:10–13:13). The directory now also holds SIG-W-20260924-010.md (13:44). The count is stale. "Drains the WHOLE inbox" still covers it.
⚠️ 16 The L11 9/25 spawn set includes BROCK L420, RED L416 and DAEDALUS L456. The view (L41) puts all three under **THU 9/24**. The L10 driver rule says "wakes each owner at the first boot on/after the date", and the 9/24 boots were prome-4d and prome-26. The page does not say why these rows move to 9/25. L8 "Boot PARTIAL… gate 0 blocking" might be the reason, but that is not stated.
⚠️ 17 L11 "L0 drain of 24 items [inbox_census 09:3x]": the time has no date, and the item count is a live figure.
⚠️ 25 Two file:line pointers don't name a file. L15 "`config.py:72`": two exist (FORGE/tools/market-data/config.py and FORGE/tools/news-sweep/config.py). L11 "CLAUDE.md:194": which CLAUDE.md?
⚠️ 28 L17 "REGINALD: CATO brief review 3/3 applied (`eca22a618`…)". git log shows eca22a618 = "CATO: review REGINALD rates attribution and capital claims". That is the review commit, not the commit where REGINALD applied it.
⚠️ 31 L19 "WQ-230 closes when FALCON confirms…" reads as if WQ-230 is open. The L47 view of 21 open items does not list WQ-230, so its open/closed state can't be determined.
⚠️ 32 L21 "measured 24,349 B … = 74.8% of budget, 63 B under the 75% rotate trigger". measure.py reproduces 24349 B now. The budget (≈32,550 B) appears in neither file. This is a live measurement in prose that goes stale at the next edit.
⚠️ 33 L21 dates dbaaa7230 as "9/22 pre-open", but the commit time is 09-22 09:37 −0400, which is after the 09:30 open.
⚠️ 35 One value, two dates. Archive L6: "✅ 9/21 DGS10 read 16:53 ET = **4.96**". SCRATCH L23: "The 9/22 DGS10 cell printed 4.96 ≥4.50 [FRED, read 9/23 20:40 ET]". These could be two cells with the same value, or one cell with the wrong date on it. The gate depends on which.
⚠️ 36 L23 "TLT $80.46 [9/23c], five sessions left, $3.46 above the $77 strike". The arithmetic is right as of the 9/23 close. L45 on the same page gives TLT $79.90 intraday 9/24, so "five sessions left" reads as current. The suffix "c" is never defined.
⚠️ 38 L25 "Operator matters" is a 9/23 prome-7a paragraph with no date: "Deck republish authorized 22:37 ET… (not authorized tonight)". It sits under the 9/24 card, and L8 has "authorized (Will 13:37)". "WQ-246 · WQ-274 need Will" also undercounts the 21 open items in the view.
⚠️ 43 L8 "10Y 5.17% intraday, 16bp jump 9/23": the basis of the 16bp (^TNX or DGS10) isn't stated.
⚠️ 45 Archive L1 "at 79% of budget (rule-5 rotate tier; stop <70%)": "rule-5" is not defined, and the budget is not in the file. The outcome does hold: SCRATCH is 22719 B = 69.8% of 32,550.
⚠️ 46 Archive L2, perimeter 1, crc 1497875070. The stated recipe does NOT reproduce it. Recipe: "segments joined with a single newline, no trailing newline"; six segments joined that way give 1757230941. The only match is raw lines 6–16, which keeps the blank separator lines and ONE trailing newline. The line also says "`python3 PROME/tools/measure.py` reproduces on this file's body", but measure.py only measures whole files (353766202 / 3276538737). (This is the file's own receipt, so capped at ⚠️.)
⚠️ 47 Archive L2 lists a segment "operator-card history (prome-a5 9/22 card + prome-b7 9/23 lines)". The body (L6) contains only prome-a5's 9/22 card. No prome-b7 or 9/23 lines appear in cut 1; the only 9/23 card is prome-7a's, in cut 2 (L25). From these two files alone, a reader cannot tell whether text was lost.
⚠️ 50 Archive L19 says the "12-rows OVERDUE list" restated "DOCKET-VIEW ᵒ marks". The view (SCRATCH L39) has **16** ᵒ-marked PROME rows: the 12 plus L350, L378, L392 and L393. All 12 are present, but they can't be told apart from the other four. The facts "annotated 9/23 · unstarted since 9/19 · next slot 9/28 · L448 waits on WQ-274" now exist only in the archive.
⚠️ 51 Some owner pointers can't be checked from these two files: WQ-263 → "STATUS row"; ARGUS grade → "DOCKET L333" (not in the view); the third cut's owner, "HANDOFF (9/23 evening entry)".

## ✅
1 L2 stamp 13:4x prome-26 · 2 12:16 intraday labeled (L2, L45) · 3 9/21 history pointer resolves · 5 read_cap_check.py resolves · 6 session 12:14→13:4x · 7 WQ-280/281 13:17, L8=L13, absent from open view · 8 DEWEY 4779531b8 (13:21), receipt 13:24 · 12 L10 driver header · 13 BRENT L329 is FRI 9/25 in the view · 14 BG-02 17:00 timing rule is internally consistent · 18 VIOLET L464 FRI 9/25 · 20 GATE-FLG-T08/L236 10/1/WQ-279 9/30 · 21 flng_watch.py resolves; L463 10/2 · 22 WQ-259/264/256 08:47/08:50 fall inside prome-4d; e9161e9e6 08:53 · 23 L465 9/28 · 24 L444/L450/L462 9/28, L461/L429/L441/L459 9/30 in view · 26 L17 pointers resolve · 27 KRE 9/14→9/23 = 7 sessions · 29 $280M = 80% of $350M · 30 FLG intake-term file resolves · 34 HEARTBEAT pre-rebase snapshot resolves (PROME/archive) · 37 77P no-bid dated · 39 HANDOFF/STATUS resolve · 40 L401/L406 · 41 view 151=71+29+35+16 (counted) · 42 WILLQ 21 (counted) · 44 FFB plan resolves · 48 cut-2 crc 671932331 reproduces exactly · 49 cut-3 crc 2936720754 reproduces exactly · 52 archive pointers resolve · 53 L381/L423 unannotated OVERDUE, matching the view.

## Ground-truth answers
Q1: SCRATCH L8: "`prome-26`, 2026-09-24 12:14 → closeout 13:4x ET (desktop)". The rulings came at 13:17 ET, verbatim *"Approve WQ-280 and WQ-281 with your recs"*:
- WQ-280: NO ADD to 004 (re-arm met, kill not fired).
- WQ-281: the SUSTAINED bar governs CRL-08, so it resolves MISSED 9/30.
L13 repeats both.

Q2 (from L11): at the 9/25 morning boot, run `ListAgents` first each time. Spawn, capped at 4: BRENT L329 (drain its whole inbox), BROCK L420, RED L416 and DAEDALUS L456. TERRY is a possible 5th, which goes to the slate. Also run the GATE-FLG-T08 pre-fire check, and per L12 run flng_watch.py.
The timing rule: "BG-02 grades AT 17:00 ET 9/25 — a morning spawn PREPARES; the letter grade needs a session live at/after 17:00, so keep BRENT live to the close or re-touch it after 17:00 [PROME owns this]". VIOLET L464 comes after the close.

Q3: Intraday figures are labeled explicitly (L2, L45 "pulled 12:16 ET 9/24 — INTRADAY, not closes"): Brent $108.02, ^TNX 5.17, TLT $79.90, USO $151.80, and L8's "Brent +5% intraday", "10Y 5.17% intraday". The 77P no-bid is also intraday ("9/22 09:50"). Closes: TLT $80.46 "[9/23c]" (the "c" is undefined) and the DGS10 9/22 cell 4.96 [FRED]. The 9/23 closes are pointed to HEARTBEAT am.#1. The tells are the words "intraday" and "c", and bracketed stamps. The 16bp and "five sessions left" have no basis or as-of.

Q4: The 12 rows appear in the DOCKET-VIEW OVERDUE line (L39) as ᵒ marks, but mixed in with four other ᵒ rows (#50). No pointer from SCRATCH to the archive (❌4). The archive does carry the list (A-L21).
crc results:
- Cut 2: 671932331 reproduces exactly.
- Cut 3: 2936720754 reproduces exactly.
- Cut 1: 1497875070 reproduces only over raw lines 6–16 (blank lines kept, plus a trailing newline), not by the stated recipe (#46).
Whether the archive is COMPLETE against the pre-cut SCRATCH could not be tested inside the two-file perimeter. #47 (the missing prome-b7 lines) is the open question.

Q5: From "★ NEXT SESSION" (L6), the DEWEY spawn outcome is in L8: "DEWEY spawned Tier-1 L0 drain (WQ-206; CARL doorbell) → 13→0, CARL-DR-5 delivered (`4779531b8`) and graded STRIKE by CARL; ASKED→RECEIPT 13:24". L13 points to the "ORCH_LOG row". MARCO-DR-1's date is in L8 only: "DOCKET L466 registered (MARCO-DR-1 wake 11/02, needed-by 11/16)". It is not in the view (beyond the window), so the owner record is DOCKET L466.

Q6: every ❌/⚠️ above.

POINTERS: 32/33 resolve (20 file paths + 6 commits in SCRATCH, 7 in the archive); dead: PROME/reports/2026-09-24_prome-26-closeout.md. 2 file:line pointers don't name a file (config.py:72, CLAUDE.md:194). The link from SCRATCH to the rotation archive is MISSING.
ONE-LINE VERDICT: Mostly yes for 9/25 (spawn set, BG-02 17:00 rule, and intraday labels are clear), but no for recovery: SCRATCH does not link to its own rotation archive, the Deck receipt pointer is dead, and L11/L23 disagree on whether TERRY 007 is owed.
