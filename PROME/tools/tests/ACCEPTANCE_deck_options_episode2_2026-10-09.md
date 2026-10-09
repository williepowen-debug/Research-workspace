# ACCEPTANCE — Decision Deck Change A, EPISODE 2 (DOCKET L662) — written BEFORE the edit, 2026-10-09 13:38 ET, PROME prome-75

**Authority:** Will 2026-10-09 13:37 ET, verbatim *"okay do the code fix please"*, on PROME's statement that L662 is a second process change this session (WQ-299 R1 overrun, disclosed at closeout as Will-authorized). Episode 1 = `ACCEPTANCE_deck_options_2026-10-09.md` (three reads spent, STILL UNRESOLVED; its disposition stands: the buttons are WITHHELD until this episode is INDEPENDENTLY VERIFIED **and** TERRY re-cuts the TLT and exit cards, f80d472a0). `reads: 0`. `decision_deck.py` carries episode 1's two-correction stop: this pass is its third correction and is NOT called fixed until this episode's read says so.

**The defects in their own terms (read 3's ❌X3 + residue R1–R10, read 2's W-items):** a card that cannot be read at build brings back verbs with no stated meaning; PROME's annotation can hide inside the owner's text; a withdrawn (struck) card figure ships as live text; three sidecar mistakes resolve silently; a plain row's tap stores the verb, not the letter the rec maps it to; a legacy whole-row tap shows on the first unit; the parent-render test skips instead of failing; two rows can carry conflicting taps on one position; the HBAN If-nothing abridges the card; the live selftest reads ❌ while options are withheld.

## Acceptance conditions
- **E1 (❌X3, fail closed):** on a multi-decision row, a unit whose owner card is unreadable at build (missing source, file/section not found, no label-shaped rows) REFUSES THE BUILD naming the unit — never a bare-verb fallback. A single-decision row keeps episode 1's AC5 behaviour (today's plain card + warning).
- **E2 (R1):** a `[PROME: …]` bracket is accepted only at the END of a consequence (after the verbatim cells); a bracket anywhere else refuses the build naming the option.
- **E3 (R2):** struck text (`~~…~~`) is ABSENT for comparison on both sides (card cells and sidecar); a sidecar consequence that reproduces struck card text refuses the build; rendered option text/consequence carries no markdown markers (the sidecar holds plain text; `**`/`~~`/backticks in a sidecar option cell refuse the build).
- **E4 (R3):** PLAIN syntax errors raise, never resolve silently: a duplicate `APPROVE=`/`DECLINE=`; any `::` part after the reason that is not `APPROVE=`/`DECLINE=` (so a `::` inside a meaning raises); a meaning that is empty.
- **E5 (R5):** a single-decision row may be declared `PLAIN :: reason :: APPROVE=… :: DECLINE=…`; it then renders the plain card WITH the two meaning lines and a unit-class tap wrap (`id="tap-<wq>"`, `data-did="<wq>"`), and a tap stores `decision_id=<wq>`, `choice={label: verdict, text: meaning, consequence: ""}`, `options_shown=[]`; a row with an EMPTY options cell stays byte-identical to the pre-Change-A render (AC1 unchanged). WQ-357 is re-cut this way (Approve = A at the live clock · Decline = C), so its tap records the letter's meaning, not a bare verb.
- **E6 (R6):** on a multi-unit card a document with no `decision_id` renders in a card-level state line, never inside a unit; the card tint follows the LATEST document among the card's units/row by `ts`, not iteration order.
- **E7 (R7):** the AC1 parent-render test FAILS (not skips) when the parent generator cannot be obtained from git history.
- **E8 (R8, pickup rule):** BOOT 3b says that when two rows carry taps bearing on the SAME position (e.g. 357 and 302.TLT on the TLT 82P), PROME writes both verbatim and asks Will which governs before either is encoded.
- **E9 (R10):** the 302 If-nothing carries the HBAN card's own <$16 list verbatim (a Rep-Assisted close · an exercise and buy-in · an instruction not to exercise with the intrinsic lost).
- **E10 (selftest):** with a 10-column sidecar and NO options rows, the live selftest reports "options withheld" as ✅ with the count, never ❌; with ≥1 options row the AC8 coverage check runs as before.
- **E11 (R9/R4):** the episode-1 file's remaining typed clock is replaced by its commit name; AC7 there is amended to the BOOT forms (one sentence each: CHOICE · plain-unit APPROVE/DECLINE · unit LATER · whole-row document).
- **E12 (regression):** every episode-1 fixture test still passes; `--selftest` passes on the live sources with the options withheld; the rendered plain page is byte-identical to version 94's page apart from the build stamp and the 357/302 explainer edits named here.

## Neighbours (WQ-229 — considered)
ordinary → E12 · overlap → E8 (two rows, one position) and E6 (two document shapes, one card) · wrong owner → E1/E2/E3 (nothing not from the card ships as the card's) · missing information → E1 (unreadable card ⇒ refuse on a multi-decision row), E4 (malformed sidecar ⇒ raise) · concurrent activity → E6 (a legacy whole-row document from the pre-Change-A page beside unit documents); TERRY's re-cut landing mid-episode changes nothing here because every options cell is empty until the ship.

## Not in this episode
Re-populating the option cells (after TERRY's re-cut, with a build + the next closeout's read of the rendered page) · Change B · WALTER's backlog 12–15.

## States at commit (filled below at the end of the pass)
