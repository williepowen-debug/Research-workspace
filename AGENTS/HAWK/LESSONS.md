# HAWK LESSONS — Mistake Patterns to Avoid

*Read at boot (SPAWN PROTOCOL step 3). One lesson per entry: what happened, why it bites, the rule.*

**Split history:** sibling-inherited lessons and the July12 scope split are recorded verbatim in `archive/LESSONS_ROTATED_2026-10-21.md`. Dormant-vector cadence remains HAWK-owned.

## [2026-06-12] Prediction text and promotion-threshold text must be written identically
**Rule:** when a prediction and a vector threshold describe the same event, write one canonical sentence and reference it from both; on conflict the registered PREDICTIONS.tsv text is canonical. *Full entry (what happened, why it bites, corollaries): `archive/LESSONS_ROTATED_2026-10-21.md` (rotated verbatim 2026-10-21).*

## [2026-06-12] Live-war boot needs a day-by-day gap sweep, not topic searches
**Rule:** during an active conflict, boot sweeps day-by-day from the last STATUS date to the boot date and checks each open Tier-1 watch item against the window before any re-mark. *Full entry (what happened, why it bites, corollaries): `archive/LESSONS_ROTATED_2026-10-21.md` (rotated verbatim 2026-10-21).*

## [2026-06-20] A deprioritized secondary vector can go stale for MONTHS — re-sweep dormant vectors, don't carry them forward
**What happened:** HAW-03 ("No US military intervention in Venezuela in 2026," 95%) and VX-HAWK-VEN-01 ("rhetoric only, no military action") were carried OPEN/unchanged from Feb–Apr through Jun 20 — but the US had actually run Operation Absolute Resolve on **Jan 3 2026**, capturing Maduro, with a naval blockade since Dec 17. The boot theater-sweep surfaced it (A1, multi-primary); the vector had been wrong for ~5.5 months because the Iran war "absorbed bandwidth" and the dormant vector was never re-verified.
**Why it bites:** a stale 95%-confidence prediction sitting OPEN reads as live calibration when it's actually a buried miss; and a "rhetoric only" vector understates a realized intervention with live oil-supply implications (US now controls Venezuelan export flows). Carry-forward without re-verification silently rots — and the staleness is invisible precisely because the vector is "quiet."
**Rule:** at boot, dormant/secondary vectors (Venezuela, Taiwan, trade war) get a periodic FULL re-sweep against external primaries — not a carry-forward of the last state. Treat "VX last-updated >30 days ago AND has an OPEN prediction" as a re-sweep trigger, not a skip. Extends the boot predictions-scan ([[finding_boot_predictions_scan]]) from predictions to the vectors behind them.

## [2026-07-12] A prediction's literal wording narrows your evidence sweep — search the MECHANISM, not just the named targets
**Rule:** re-check a prediction by sweeping its underlying MECHANISM (every channel), not its named targets. A first-pass 'nothing found' is a coverage statement, so escalate to a date-careful multi-angle sweep before banking a 'no', and never trust your own ledger as a baseline without a completeness pass. *Full entry (what happened, why it bites, corollaries): `archive/LESSONS_ROTATED_2026-10-21.md` (rotated … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-07-25] The unprocessed inbound lane contained the correction to my own canonical thesis
**Rule:** **if a signal lane can carry a falsifier for a thesis you own, it is boot-mandatory, not spawn-optional.** Concretely: at boot, scan inbound *headlines* for anything naming your own canonical thesis or its key metric even when you are not spawned for inbox processing — that scan is seconds, and full processing can still be deferred. Corollary: **a dark window is not neutral for a thesis-owning surface.** … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-07-25] "Derived" is not "self-updating" — a regenerated surface rots at the cadence of its regeneration
*Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-07-28] I wrote one theater's prediction legs OPERATIONALLY and the other's as EXEMPLARS — and the asymmetry is invisible until the wrong theater moves
**Rule:** **write every leg of a multi-theater prediction to the same standard — operational thresholds, not named exemplars — and state explicitly for each leg whether it is theater-scoped or cross-theater.** If a leg is genuinely cross-theater (a vessel sinking, a barrel count), do not let a `[theater]` bracket silently narrow it. **Corollary, and it is the non-obvious half:** the fix is *not* simply "add a direct … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-07-28] A promotion gate is only meaningful against the scale it is scored on — I attached a military test to a vector whose bands measure LNG inventory
**Rule:** **when you add or amend a gate on an existing row, re-read that row's BANDS in the same edit, and state which band the gate resolves into.** If the gate cannot be written as "this moves the row from band X to band Y," it does not belong on that row — it belongs on a row that measures the thing the gate tests. **Corollary — the diagnostic that would have caught it in seconds: ask "what, concretely, changes … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-08-20] I fixed HAW-18's *wording* asymmetry and shipped the *unit-of-analysis* one four times in a single row
**Rule:** **for every leg, name the unit of analysis on BOTH sides of the comparison before writing the threshold** — stock vs flow, component vs terminal, route-scoped vs theater-wide, instrument-perimeter vs claim-perimeter. If the two sides are not the same object, the leg is broken no matter how well-sourced the number is. **Corollary, and it is the non-obvious half: having just applied a principle is a RISK … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-08-20] A ruling does not travel to the instruments — three instances, three desks, one day
**Rule:** **when you rule an instrument out, grep for its IMPERATIVE wording and fix it at the point of use in the same commit** — sources tables, boot sequences, script docstrings, consumer packets — not just at the point of decision. A ruling that lives only where decisions are recorded governs nobody's next action. **Corollary for publishers:** when you correct a threshold you have published, assume a consumer … *Full entry: `archive/LESSONS_ROTATED_2026-11-09.md` (rotated verbatim 2026-11-09).*

## [2026-09-28] A re-sweep keyed on ONE band's trigger certifies a negative the adjacent band already contradicts
**What happened:** the 8/10 re-sweep of `VX-HAWK-IRAQ-01` searched for a force-majeure LIFT (the GREEN trigger), found none, and wrote "EXPLICIT DATED NEGATIVE: no lift, no restart". The 9/28 re-sweep found a Basra Oil Co full-output order of 7/3 and the minister's 2.75 mb/d of 8/9. Both predate the negative, and together they meet the YELLOW gate (>2M bpd). The mark sat RED for ~7 weeks under a gate its own ladder said had fired.
**Why it bites:** a negative written against the most salient headline ("FM lifted?") reads as a full review, and "dated, explicit" wording makes it look more rigorous than a carry. Same family as HAW-15: the search took its scope from one named trigger, not the ladder.
**Rule:** a dormant re-sweep tests **every band boundary adjacent to the current mark** (the one above AND the one below), each against its own instrument, and writes one line per boundary. "No X" is only ever a claim about the boundary you searched.

## [2026-10-29] A trigger's named example became its search scope — Croatia met EURMIL RED (b) six months before registration
**What happened:** RED (b) read "activation of compulsory military service or mobilisation by a European NATO state — for Germany specifically, …". Every sweep from registration (~Sept 18) to October 25 searched Germany only. Croatia's compulsory intake had begun on 2026-03-09, so the ORANGE text ("no activation") was false on the day it was written. It was found only by a residual check on October 29. Will then ruled B (a prospective clarification to mobilisation or crisis call-up).
**Rule:** when a trigger says "any X" and names one example, the sweep enumerates every X, and the example is only one row in it. At registration, test the bands against the world as it already is (has any member state already done this in the look-back window?) before writing a band's "unstepped" claim. Same family as the 2026-07-12 lesson (a letter's wording narrows the sweep).

## [2026-11-06] A proxy with no known-positive control certifies nothing, and I had called it a measured negative
**What happened:** on 10/29 I accepted TD6/TD19 as a stand-in and wrote "SATISFIED-BY-PROXY, a measured negative". OSPREY's 16-week backfill showed it fires only on CPC disruption and reads clear in 9 of 10 windows.
**Rule:** before a proxy may satisfy a test, show it has seen the object at least once. If it never has, it can only cue, never clear.

## [2026-11-09] Two lessons from the catch-up: a search miss is not a refutation, and a fingerprint record must cover every changed input
**What happened:** (1) I carried WALTER's "not found" search for the Rubio quote and the IRGC claim date as a refutation; FALCON had both at the primaries, and PROME's relay reversed it. (2) Twice in one session I recorded fingerprints with an owner input changed and unread: first FALCON's brief at 10:55 ET, then OSPREY STRIKES `e4bc891bb9`, committed 10:51:23 ET, in the same minute as my aggregate stamp. The aggregate said "unchanged" and the brief said "OSPREY has not rowed Kirishi" for about two hours.
**Rule:** (1) a search that finds nothing is a statement about the search, not the event; write UNVERIFIED, never "did not happen". (2) Before `--record`, list every REVIEW path that the capture printed and name the diff read for each; a stamp written in the same minute as an owner commit has to be re-checked against `git log`.
