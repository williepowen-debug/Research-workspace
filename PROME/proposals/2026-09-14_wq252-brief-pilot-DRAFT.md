# WQ-252 — worked example for the briefing pilot · **DRAFT, nothing published**

**Written:** 2026-09-14 18:5x ET · **Session:** `prome-54`, **DESKTOP-BC6EF81** · **Owner:** PROME
**Authority:** Will's relay of CODEX 2026-09-14 — *"Proceed with your narrower pilot: understandable reasoning, with review priority stated briefly; defer preference elicitation. Prepare one WQ-252 example using existing evidence during ordinary authorized work... Show me the draft before replacing or publishing the current presentation."*

⛔ **This file changes nothing.** `PROME/WILL_QUEUE.md` WQ-252 is untouched and remains canonical. No standing instruction was edited. No new surface was created — if this is adopted, the text below **replaces the existing WQ-252 row's cell 2**, in place, and this file becomes the provenance record.

⛔ **Success is NOT that Will's decision changes.** A rewrite that moves the decision is a failure mode here, not a result: the same shaving class the fleet polices everywhere else. The test is whether the reasoning is inspectable and challengeable.

---

## THE DRAFT — what a WQ-252 briefing would say

> ⚖️ **WQ-252 — `HEN-F1`'s two thresholds are closer together than one contract roll. A letter-design question; nothing is fired and nothing waits on you.**
>
> **What changed.** On 2026-09-14 three desks independently established that `HEN-F1`'s two thresholds sit **$4.84** apart — stand-down `<$95.00`, thesis-dead `<$90.16` — while **one month-step of the crack curve is $4.48–$4.57** (HENRY, five pulls, spread $0.09). One roll is **comparable to the entire separation.** ⛔ Do not quote a two-significant-figure percentage; HENRY retired its own "94%" as unsupportable across that spread.
>
> **Why it deserves your attention.** `F1` is one of three pre-registered conditions that return the **VLO card (WQ-213) to you as a fresh ask**. So a falsifier that can trip on the calendar sits on the path to a capital decision you are re-affirming by 9/18 — and it would trip **while every structural check passes**, because the legs are matched, the negative control is satisfied, and there is no desync. The defect is invisible to the guard the fleet built for this class today.
>
> **What the conclusion depends on.** Two premises, both required, both currently true:
> 1. **`F1` is graded on a series whose contract month advances.** If it were graded on a fixed delivery month, the defect does not exist.
> 2. **The crack curve is steeply backwardated,** so each month-step is ~$4.5 rather than ~$0. If the curve were flat, the defect does not exist.
>
> **The uncertainty, and it is the live half.** Whether roll steps **accumulate or cancel** is **NOT established.** HENRY first framed it as a sawtooth that cancels over a cycle, then **retracted that against its own headline** because the premise could not be established. What was measured points the other way: `HOX26 − HOV26` widened from −0.1294 [8/25] to −0.2113 [9/14] — backwardation **deepened** as the near leg approached expiry, the opposite of convergence, and it survives normalisation by the prompt price (−3.036% → −4.235%). ⚠️ **The limit cuts both inferences equally:** n=17 bars, **one** cycle, observed 16 days from expiry — possibly too early to show convergence at all. Multi-cycle reconstruction is **blocked**: `HOU26`/`HOQ26` are delisted. **Suggestive, not proven.** The adopted grading instruction is the conservative one: treat the hazard as **at least one step (−$4.56)** and do not assume self-cancellation.
>
> ✅ **What is not in dispute.** `F1` is **NOT fired on any basis** — continuous $98.56 · matched-Oct $107.45 · matched-Nov $102.90, against `<$95`; minimum observed buffer **$3.34**. HENRY's grade **stands**. **No letter has been re-specced by anyone.**
>
> **Your options, and why the owner would not pick one.** Four remedies exist. **Every one moves the effective line, and on 2026-09-14 every one moved it in HENRY's own favour** — which is why HENRY declined to choose while its letter was being read, and why PROME proposes none either (PROME registered WQ-213 against the same card and would inherit whichever line the fix produces).
>
> | | Remedy | What it costs |
> |---|---|---|
> | ① | Grade on a **fixed delivery month**, rolled by hand | Removes the defect at the source; the roll decision becomes a judgment call someone must own |
> | ② | **Roll-adjusted (back-adjusted)** series | Removes the step; re-bases the whole history, so `$90.16` and `$109.93` stop meaning what they meant |
> | ③ | **Widen the separation** between the two thresholds | Keeps the series; is a threshold change, in the window the threshold is being read |
> | ④ | **Change nothing; check matched basis at fire time** | ⬅ **already in force** — HENRY registered the hazard against its own PREDICTIONS row, so whoever next grades `F1` or `F3` reads it at the moment of grading |
>
> **The next useful step.** Nothing tonight. ④ is live and needs no ruling, so the honest framing is: **you are choosing whether to replace a working disclosure with a letter change, not whether to leave a hazard unguarded.** ⛔ Do not rule inside a grading window. The natural moment is **`HEN-46`'s resolution (Q3 airline prints, late Oct)** or a session convened for it. ⚠️ **One dated pressure:** the desync recurs **every** monthly cycle — product legs expire exactly 10 days after WTI, every cycle — and the next window lands **~mid-October**, inside `HEN-F3`'s own horizon (DOCKET L386, L385).
>
> **Authority.** HENRY owns the letter and has not changed it. TERRY constructs, never withdraws your approve. PROME registers and grades nothing here. **The letter changes only on your word.**
>
> 🔍 **Review priority — HIGH consequence, LOW urgency.** If this is wrong, a thesis stands down for a calendar reason with every check green. It is not time-critical: `F1` is $3.34 from firing on its worst basis and the remedy in force needs no decision.
>
> **Where to check me:** letter → `AGENTS/HENRY/workbook/PUBLISHED.tsv` (*"F1 falsifier: crack <95 = stand down, <90.16 = thesis dead"*) · grade + basis → `AGENTS/HENRY/STATUS.md` row 3 · retraction → `4e5d3971c` (HENRY), re-derived `f11ce2505` (TERRY), precision `d4a65e5c6` (HENRY) · class + expiry table → `PROME/DOCKET.tsv` **L386**.

---

## What this does differently, stated so you can judge it rather than take my word

| | Current WQ-252 cell 2 | This draft |
|---|---|---|
| Size | **4,280 B** in one unbroken cell | ~3,400 B, sectioned |
| Decisive premise | Present, but derivable only by reading the whole cell | **Named as two premises, each with its own falsifier** ("if X were true, the defect does not exist") |
| Uncertainty | Present and honest, interleaved with the retraction history | Separated: what is measured · what the measurement cannot settle · what the adopted instruction is |
| Alternatives | Named in one clause (*"fixed delivery month · roll-adjusted · wider separation · matched-basis"*) | **Enumerated with their costs**, and ④ marked as already in force — which changes what the question is |
| Authority | Stated | Stated, unchanged |
| Review priority | Not stated | **Stated in one line** (consequence high, urgency low) |
| Verification | Commit hashes scattered through the prose | One "where to check me" line |

### ⚠️ What I dropped, and where it still lives — so "preserve, don't persuade" is checkable

Everything below is **removed from the brief and retained in the record.** None of it is load-bearing on the decision; all of it is load-bearing on *how the finding was reached*, which is what the provenance surfaces are for.

1. **The superseded sawtooth text**, carried in the current row marked HISTORY → survives in `git log -p -- PROME/WILL_QUEUE.md` and in DOCKET **L386**.
2. **The three-clause grading rule's clause ③** (*the step is not constant; on the observed direction it grows — near step −3.61 → −4.48 over 17 bars, OLS −0.0233/bar*) → this is **direction only**, both desks explicitly declined to size it. Retained at **L386** and in HENRY's PREDICTIONS row. ⚠️ **Flag: this is the single judgment call in the whole rewrite.** It makes the hazard worse and I cut it for length. If you want it, it goes back in the uncertainty paragraph.
3. **The chain of provenance** (REGINALD's residual → TERRY generalised → HENRY verified and refused to remedy; three desks, none the raiser's own instrument) → reduced to one clause. Full version at **L386** cell 6.
4. **HENRY's own sentence** — *"a correction that replaces a wrong frame with an unverified one is not an improvement; it is the same error wearing the other coat"* → a process lesson, not a decision input. Lives in `PROME/HANDOFF.md`, `PROME/STATUS.md`, and HENRY's own `LESSONS.md`.
5. **The independent three-desk agreement to within cents** (Oct ~107.7 · Nov ~103.2 · Dec ~98.4 · Jan ~96.5) → the numbers that matter ($4.48–4.57 step) are in the brief; the corroboration is at L386 and in HENRY's `PUBLISHED.tsv`.

---

## Open, and NOT decided here

- Whether item 2 above (the growing-step clause) belongs in the brief. **My read: it belongs, and I cut it wrongly.** It is the difference between "one step" and "steps that compound," and that is a decision-relevant distinction even at direction-only confidence. **Recommend restoring it before adoption.**
- Whether this replaces the row or sits beside it. CODEX's instruction is *replace, do not add a second report* — so: replace cell 2, keep cells 4/6/7 (needed-by, PROME's rec, the not-blocked note) as they stand.
- An **optional** paraphrase from Will — *"what do you understand the decision and its main uncertainty to be?"* — is **feedback, not a test, and PROME is not the answer key.** A mismatch is as likely to mean the brief was ambiguous, or that Will named a better premise than PROME did, as that the brief failed.
