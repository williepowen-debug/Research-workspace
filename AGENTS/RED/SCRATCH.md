# RED SCRATCH — canonical session handoff
**Written:** 2026-09-25 09:4x ET [`date` 09:13 EDT at the fixture run; session start 09:08] · **Session:** S47 (PROME prome-2e Tier-1 spawn, WQ-184 due-row driver; DOCKET L416 + whole-inbox L0 drain) · **Supersedes:** S46 (2026-09-18). The S46 handoff is in git history (`git log -p -- AGENTS/RED/SCRATCH.md`).

---

## CHANGES SINCE (what moved while RED was dark, 9/18 → 9/25)

- **L277 leg 3 GRADED by VIOLET (9/18 close): CONFIRM-B = MISS OF THE MAP.** The Fed hiked 12–0. B's two discriminating cells carried the confirm; MOVE never printed (it was the non-discriminating cell). RED's ruling was applied in both halves. VIOLET's letter scoreboard: 0 CONFIRM · 1 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.
- **PROME L429 (9/23):** FT-03/04 evaluate on generic `BZ=F`, a continuation that rolled around 9/18.
- **BOND:** two more F2 reads. The 9/24 20–30Y op is OFF-THE-RUN (recent 0.02%). F2 was re-ranked by issue date, giving a base rate of 1 of 53.
- **CARL** answered RED's 9/14 revision-denominator ask six days early: 13 self-made calls helped the record vs 6 that hurt. Will then approved five record actions. **RED's CRL-05 concession was wrong.**
- **ORACLE:** Kalshi `KXRECSSNBER-26` has **no NBER leg**. KB-RED-096 had inherited the label.
- **DAEDALUS:** the FROZEN token on `AGENTS/SAM/red/COUNTER_THESIS.md` is RED's edit (SAM declined, correctly).
- **WALTER:** fill-forward error confirmed at settle (9/18 SKEW 148.10, MOVE 80.64). Goepfert's 100-year breadth claim routed for adversarial review. **`SIG-W-20260917-011`'s mechanism was WITHDRAWN**: derived FRED breakevens publish on Treasury's schedule and are not provisional.

## WHAT I DID

1. **L416 — L247 F1 recheck on spec v0.5: FAIL, 1 blocking** (CHG-RED-053, ML-RED-263). v0.5 closes the v0.2 hole: Exhibit A refuses at (vi) α, the ruled entry renders 0.2325, and both honest-limit endpoints pass as stated. **New hole:** §4 (i) never ties `forecast_id` to `question_id`. Exhibit C (a foreign forecast with scalar 0.9) passes (i)–(viii) and renders **0.01** on MIDAS-06; C2 renders **0.81**. Both are outside the stated [0.226875, 0.3025]. The row binding is also unspecified: a forecast-keyed build falls through to BINARY 0.3025. **Honest severity:** ruling-gated in practice, because the masses ≠ the letter; the FAIL is on the spec's stated guarantee. Remedy R1 + R2 + an honest-limit sentence fix + 2 fixtures. ⚠️ W1 (α terminator, inert), W2 (branch-key grammar, Exhibit D2), W3 (Σ context-precision basis). **Both of PROME's departures were ACCEPTED; my 9/10 "(vii) kills the degenerate" was wrong.** Acceptance conditions for the v0.6 recheck are pre-written (report §4). Fixture: `challenges/2026-09-25_L247_F1_v05_fixture.py`.
2. **Inbox 8 top-level + 3 WALTER-lane → 0 + 0**, with 11 `board_log` rows. `board_log` is at 25,234 B (78% of cap). ⚠️ **The next ~15 rows breach it — build the pre-append gate (item 4).**
3. **KB-RED-096 corrected in place** (Kalshi = GDP rule only); the superseded wording is preserved verbatim (ML-RED-265).
4. **CARL's CRL-05 correction VERIFIED** at CARL `PREDICTIONS.tsv` (first call 75% [3/09], 20% undated; 0.75² = 0.5625) and accepted (ML-RED-264).
5. **L429 DECLARED, not fixed.** FT-03/04's operative basis already disqualifies `BZ=F` from completing a count. Live `BZ=F` **98.16** [9/25 fetch.py, contract UNKNOWN, −7.92% on the day] is 31.84 / 23.16 from the 130 / 75 rungs, far beyond any calendar spread. Re-pointing the evaluator to a dated contract is still owed.
6. **Packets:** BOND gets the F2 cut answer (no re-cut inside a live window; both reads OFF on every cut). DAEDALUS gets the FROZEN token (ownership accepted, blocked by the perimeter, routed to PROME).

## NEXT SESSION (dated, priority-ordered)

1. 🔴 **PR#6 SAM rail — OVERDUE since 2026-09-24. MINE.** CH-009/CH-012 adjudications on the 9/3 30Y (SAM holds "Sep-3 30Y SOFT"). CH-017 is FALSIFIED on its own terms but still reads OPEN (cite the dated observation, USD/JPY <155 on 9/14, not `STATUS.md:34`). Prepend the FROZEN line to `AGENTS/SAM/red/COUNTER_THESIS.md` (text in the DAEDALUS packet). **Needs a spawn whose perimeter includes `AGENTS/SAM/red/`**; asked of PROME in the 9/25 memo. DAEDALUS escalates at 9/30.
2. 🔴 **L247 v0.6 recheck when PROME lands the edit.** Run it as a diff read against the pre-written acceptance conditions (report §4) and re-run the fixture extended by the two new cases. Do not re-open §3/§5 or DAEDALUS's legs.
3. 🟠 **CARL's revision ledger: the full adversarial read** of 135 events (`AGENTS/CARL/thesis/REVISION_LEDGER.{md,tsv}`, `scripts/revision_ledger.py --classify`). CARL calls RED "the second attacker". The CRL-08 28% vs 7% ruling goes to DAEDALUS before the 9/30 grade.
4. 🟠 **BUILD THE PRE-APPEND SIZE GATE for `board_log.tsv` (n=3, still unbuilt).** It sits at 78% after this drain.
5. 🟠 **FT-03/04 evaluator: re-point `boot.py` BRENT-PAPER from `BZ=F` to a dated, exchange-suffixed contract**, with roll awareness (L429). WL-11 and `base_rate_review.py:72` are the same class.
6. 🟠 **Counter-signal re-pull + hypothesis-weight re-derivation.** Weights are S29 (8/12) and confidence is S41 (9/6); neither has been re-derived since. Run it as its own session.
7. 🟠 **FT-11 F2 cut:** carry BOND's "newest quartile by issue date >50%" question and the 5/06 counterexample to the next FT-11 spec review. **Not ruled inside the live window.**
8. 🟡 **Date alignment on derived series (what survives the withdrawn -011).** Align observation dates before comparing series on different publication schedules. The "provisional cell postdates its inputs" mechanism is STRUCK: the S46 item 6 premise is withdrawn and no registry cell ever adopted it (grep 9/25).
9. 🟡 FT-08 basis reconciliation with WALTER (2.04% vs 1.97084%, a vintage question).
10. 🟡 5 ACTIVE challenge rows carried (CHG-RED-027 · -044 · -045 · -049 · -051). Never OPEN-but-stale; CHG-027 is the self-falsifier, so look there first.
11. 🟡 VX-RED-009 → route to CARL. KB rows past `Stale_By`: 18. Terminal rows still cited by live surfaces: 13.
12. 🟡 Registry "different arithmetic paths" scan (12 rows).

## OPEN THREADS

- **Why the L247 hole survived two seats.** The honest limit was written as a bound, [0.226875, 0.3025], and every reader, me included on 9/10, attacked INSIDE the bound. The bound's own premise was that (ii) pins p_YES to the row. Nobody attacked that, and (ii)'s wording ("that version's scalar") never named WHICH forecast. **Attack the premise of a stated limit, not just the region it fences.**
- **RED was wrong twice in this inbox**, both by inheriting a peer's reading. CRL-05's direction came from CARL's own line. The Kalshi "NBER" label was ORACLE's ticker read. In both cases the peer found and sent the correction. Relaying is asserting.
- **Goepfert (SIG-008): no trigger, deliberately.** The claim is unfalsifiable as stated because the composite's construction IS the argument. If breadth is ever registered, it needs the construction and a base rate first, and it is a new direction (Will).
- ⚠️ **`BZ=F` −7.92% on 9/25 with contract UNKNOWN.** It may be a roll artifact (mode ii) or a real move. This is BRENT's domain; RED only notes it cannot reach an FT-03/04 rung either way.

## PENDING WILL-DECISIONS

**None from this session.** No weight, threshold, sustain count or score moved; $0. The perimeter question (PR#6 rail under `AGENTS/SAM/red/`) goes to PROME, not Will.

## GIT STATE

Committed path-scoped inside `AGENTS/RED/`, plus 2 carve-out ① packets (BOND, DAEDALUS inboxes) and the completion memo in `PROME/inbox/`. **No pull:** the tree held other desks' uncommitted work at boot (VULCAN, WATT, PROME), so root "Before pulling" step 2 applies. Push via `scripts/safe-push.sh`; the receipt is in the memo/SendMessage.
