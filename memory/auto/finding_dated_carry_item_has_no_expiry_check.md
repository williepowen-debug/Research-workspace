---
name: finding_dated_carry_item_has_no_expiry_check
description: "A carried ASSERTION never self-reports as wrong — it is a string, and reading it does not evaluate it. Dates that expire and ownership claims like 'nobody owns X' both survive forever in your own notes. State gets re-derived because checking IS using; carried claims do not. Widened from dates 2026-08-07."
symptoms: "the boot check runs green every session and the obligation is still late" | "nobody re-measured the number the thesis rests on" | "the beta/coefficient/ratio we assumed hasn't been checked in months" | "it's written down in three places and the scheduler reads none of them" | "a parameter nobody wrote down can't go stale"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0fed4cdb-2b75-4107-8c19-03bcb6b7439f
  modified: 2026-08-07T22:23:26.245Z
---

**A threshold that gets crossed produces an EVENT. A date that simply PASSES produces nothing** — no alert, no contradiction, no failed check. It just keeps sitting on the carry-forward list looking pending, and every boot re-reads it as live.

**WALTER, 2026-08-07.** Four dispatched signals said *"MU 8/4 is the resolver."* Micron's fiscal Q4 ends ~09/03 and prints late September; it was never going to report on 8/4. VULCAN sent the correction on **8/3**. It sat unread in the inbox while "MU Tuesday 8/4" stayed in the STATUS near-trigger block **and** in the `LAST_COMPLETION` FOLLOW-UP list — the file whose entire purpose is to survive handoff — **through 8/4, 8/5, 8/6 and into 8/7.** The date came and went and **nothing in the system noticed**, because nothing was watching for a date to become the past.

**Why the asymmetry is structural, not carelessness:**
- Every *state* item on a carry list gets re-derived at boot — live levels are re-pulled, thresholds re-evaluated, registries re-read, staleness computed. **They are checked because checking them is the same act as using them.**
- A *dated* item is a string. Reading it does not evaluate it. **"MU 8/4" reads identically on 8/1 and on 8/7**, and only a human comparing it to today's date can tell the difference — which is exactly the comparison nobody makes while scanning a list they wrote themselves.
- The failure is silent in the **worst direction**: the item stays on the list, so it reads as *tracked*. An item that vanished would at least be noticed.

**How to apply:**
- **When a dated item goes onto a carry list, write what happens when the date passes** — not just the date. "MU 8/4 → if 8/4 closes with no print, the date is wrong, re-derive it" is self-checking; "MU 8/4" is not.
- **At boot, diff every dated carry item against today** before working the list. It is one pass and it is the only thing that catches this class.
- **A date sourced from an agent's prose (yours or another's) is UNVERIFIED until checked against the issuer's own calendar.** This one originated in VULCAN's 7/12 STATUS and was restated four times without re-derivation, then propagated to WALTER, then into four dispatched signals. **Nobody re-derived it because everybody had seen it before.**
- **Prefer verification by ABSENCE where it is available** — it is the strongest form and usually the cheapest. EDGAR showed MU's most recent 8-K of *any* kind was 6/24, so no 8/4 earnings report exists. That is dispositive in a way "the fiscal calendar suggests late September" is not.

## ⚠️ SCOPE WIDENED SAME DAY — it is not about DATES, it is about every carried ASSERTION (WALTER, 2026-08-07, hours after writing the above)

**I wrote this memory about dates, committed it, and then repeated the identical failure on a non-date within the same session.** I had told Will three times across four sessions that **gold was "unowned by any agent."** Will corrected it: **MIDAS owns metals, gold included** — and MIDAS's row in **`AGENTS/WALTER/REGISTRY.tsv`, the file WALTER owns and refreshes at every boot**, reads verbatim *"monetary (**gold**/silver/GSR/CB buying)."* **The owner was named in my own routing surface the entire time.**

**⇒ The mechanism is identical and the date framing was too narrow.** A date is just the easiest example of the real class: **an assertion carried forward in your own notes is a STRING. Reading it does not evaluate it.** State items (levels, thresholds, registries) get re-derived at boot **because checking them is the same act as using them**; a carried *claim* — an ownership, a gap, a "nobody tracks X," a "this is blocked" — is re-read verbatim forever and **never re-tested by being read.**

**🔑 The cost is the REMEDY, not the filing.** *"Gold is unowned"* selects **find an owner / raise a governance question** — work that did not need doing, and which I escalated three times. *"Gold's owner is dormant through an 8.7% move in its core channel"* selects **route it and wake the owner** — one dispatch. **A wrong attribution does not merely misfile a datum; it picks the wrong fix, and the wrong fix is expensive precisely because it looks like diligence.**

**Added discipline:** any claim of the form **"X is unowned / nobody tracks X / there is no owner for X / X is blocked"** is a **QUERY against a surface you can actually run** — a registry grep, a file check — **not a recollection.** Run it before asserting it, and again before carrying it forward. The claim is cheapest to check at exactly the moment it feels most settled.

## ⚠️ THIRD INSTANCE, AND IT NAMES WHERE THE TOOLING GAP ACTUALLY IS (VIOLET, 2026-08-20)

**VIOLET carried "BIN-A re-base — delivered 8/4, awaiting Will. Unchanged." for 16 days.** Its own return-leg packet, written 8/04 ~22:00, **withdraws the proposal in its own title** — *"p=0.27 on 29.6 years. Do not ratify. There is nothing to register"* — and VIOLET banner-marked the superseded proposal itself the same night. PROME's DOCKET recorded it RESOLVED 8/05.

**Two things this instance adds to the mechanism above.**

**① The line survived REWRITES, not just re-reads.** VIOLET's `STATUS.md` is rebuilt from scratch most sessions, and the claim was **re-authored into a fresh file each time** — then shipped again on 8/20 in STATUS, SCRATCH **and an outbound packet to the very agent holding the contradicting record.** So "carried forward" understates it: **a false assertion can be actively re-typed by its own author indefinitely**, because the author is re-typing a *conclusion* and never re-opening the artifact underneath it. Re-authoring feels like verification and is not.

**② 🔑 It is structurally invisible to a numeric-staleness toolchain — and that is measurable, not rhetorical.** VIOLET runs six independent staleness mechanisms: `consumer_check`, `ledger_staleness`, `canary_staleness`, `validate_workbook`, `grading_note_check`, and a blocking `closeout_guard` aggregating them. **All six ran green through all 16 days.** They had to: every one keys on **a number, a date, a ledger vintage or a row id**, and *"awaiting Will"* contains none. **A staleness stack scales with instrumentation and gets NO better at this class as it matures** — the more numeric guards a desk adds, the more confidently it will close out past an untested claim, because everything it can check is green.

**③ How it actually got caught: reading ACROSS records, by someone else.** VIOLET's STATUS said PENDING; PROME's DOCKET said RESOLVED. **Both files were internally consistent and neither could detect the conflict alone.** PROME resolved it at *VIOLET's* artifact rather than asserting its own row — the correct direction (`[[finding_owner_of_record_means_authoritative_not_correct]]`). **No self-check on either side would ever have fired.**

**Added discipline:** when you carry a claim that some *other* desk would also have a record of — a pending ruling, an open ask, an unanswered packet, "awaiting X" — **the check is a query against THEIR surface, not a re-read of yours.** And treat "awaiting <person>" specifically as the highest-risk shape: it names no number, names no date, implies the delay is someone else's, and therefore **selects "wait" as the remedy every single time it is read.**

**
**EXTENSION 2026-08-21 (BOND) — the form with NO NUMBER IN IT: a carried GOVERNANCE state.**

A durable thesis doc recorded two spec legs as **"HELD — none has been base-rated."** They had been **RULED IMPLEMENT by the operator the day before** (verbatim *"Approved on both - implement per your rec"*). The doc was otherwise in excellent shape — it passed a mechanical no-live-values test with **zero** date-stamped numbers in the entire file.

**Why this is worse than a stale figure, and it is the whole point:** a reader will re-check a level — levels visibly decay, and every freshness tool on the desk is pointed at them. **Nobody re-checks whether a RULING landed.** A governance state has no vintage, no units and no series, so it is invisible to every numeric guard, and it reads as current forever.

- **The tell is a state word, not a value:** `HELD` · `PENDING` · `BLOCKED` · `DEFERRED` · `awaiting X` · `owner is Y` · `not yet approved`. **Each is a claim about the world that decays exactly like a price.**
- **Where it hides:** durable docs, precisely because they are *supposed* to be stable. The stability is what stops anyone re-reading them.
- ⚠️ **And the correction can carry its own contradiction.** The first fix here said only *"no longer HELD — ruled implement"* and left the surrounding original text still asserting the precondition the ruling had superseded (*"the measurement is owed before any of these ships"*). Re-reading the ruling showed it carried **TWO dated items, neither gating the other** — adopt on one date, deliver the base-rating on a later one — i.e. it **deliberately inverted the desk's own base-rate-first default. When a ruling overrides a standing rule, say so explicitly; a reader who knows the standing rule will otherwise assume the doc is simply wrong.**

**How to apply:** when a ruling lands, grep your durable docs for the state word it changes — not for the numbers. And at any audit, treat every `HELD`/`PENDING`/`BLOCKED` as a dated claim owed a re-test, the same as an unavailability claim.

Related:** [[finding_weekday_assumed_never_evaluated]] and [[finding_date_gate_beats_weekday_name]] cover dates that are wrong *when written*; this one covers dates that were merely **unexamined** and then **expired**. [[finding_canonical_surfaces_stale_inbox_carries_live_state]] is the delivery half — the correction existed and was sitting unprocessed. [[finding_expected_window_rederived_from_now_drifts]] is the mirror image: there the anchor moves when it should be pinned; here it is pinned and nobody checks whether the pin is still in the future.


---

## ⚠️ EXTENSION 2026-08-24 (LIQUID) — **why** the carried item never gets evaluated: writing it discharged the obligation

This memory says a carried assertion is a string and reading it never evaluates it. **This adds the mechanism, and the mechanism is what makes it defer for months rather than days.**

> **A caveat you write in your OWN file reads to its author as diligence already performed. Writing it down discharges the felt obligation.** A *banner* advertises debt **to a reader**; a *caveat in your own working file* advertises it to nobody — and **no other reader is positioned to tell the difference**, because to them it looks like you already handled it.

**Measured instance.** A pre-registered BDC grading card carried, in its own baseline table:
> *"FSK P/NAV 0.52 is SUSPECT (NAV 20.89 vs px 10.82, exactly ~½ — smells like a split/NAV-vintage mismatch). Do NOT load-bear on it."*

**The suspicion was exactly right. The cause was in the SAME TABLE** — a 12/31 value sitting under a column headed *"Q1 NAV/sh (3/31)"*. **It was carried as a caveat for 36 days. Resolving it took about five minutes.** Cost had it gone ungraded: that name's quarter would have graded **−12.4% instead of −2.81%, a 4× overstatement**, on the name the card itself calls *"first-to-mark-down historically."*

### ★ The tell, and it is mechanical rather than a judgement call

> **COST ASYMMETRY. A caveat whose RESOLUTION is cheap relative to its AGE is not a caveat — it is an unstarted task wearing one.** 36 days versus 5 minutes.

### Operational form — run it on yourself

**Grep your OWN surfaces for hedge words YOU wrote** — `SUSPECT` / `smells like` / `probably` / `needs checking` / `unverified` / `owed` / `re-pull` / `TODO` — **and sort the hits by AGE, not by severity.**

⚠️ **Severity sorting fails here BY CONSTRUCTION: a hedge word is precisely how a thing gets recorded as low-severity.** Sorting by severity buries exactly the items this finding is about.

**First run of that audit, same session, surfaced two that mattered in its top four** — the BDC card above (36d → produced a graded CONFIRM, a self-contradiction and the 4× error) and a demand-hole pre-registration (44d → its verdict was fine, but **two of its premises had since been invalidated and nobody had annotated it**). Both were written as low-severity hedges.

*(Mechanism half developed jointly with DAEDALUS as PAT-085 after this desk supplied the instance. Companion: `[[finding_plausible_stale_value_evades_review]]` — there the plausibility comes from the value; here it comes from **your own prior sentence about it**.)*

---

### n+1 — the sub-form where the normal fix is FORBIDDEN (LABOR, 2026-08-27)

**The hardest version of this is an expiring assertion written inside an artifact you have deliberately frozen** — a pre-registered grading card, a sealed spec, a signed-off baseline.

A frozen QCEW benchmark card carried, in a pre-print addendum written 5 days out:

> *"LAB-08 walks into this print with ZERO external input having arrived."*

**True on the day it was written. False 4 days later**, when a named analyst published a current-cycle read pointing straight at the card's worst band — and **nothing in the boot sequence re-evaluated the sentence**, because it is a string, and the artifact holding it is *supposed* to be immutable.

**Why this sub-form is worse than the ordinary one:**

| Ordinary carry | Frozen-artifact carry |
|---|---|
| Fix = edit the line | ⛔ **Editing is itself a defect** — it destroys the pre-registration's value |
| Staleness looks like neglect | **Staleness looks like discipline** — the file is frozen *on purpose* |
| Any sweep can repair it | Only an **external** record can |

> ★ **A freeze protects the artifact's CONTENT. It does not protect the artifact's CLAIMS ABOUT THE WORLD — and those keep aging at the normal rate.** Freezing a document freezes your ability to *correct* it, not its ability to *go wrong*.

**Operational form.** When you freeze anything, **separate the two kinds of sentence inside it**: *commitments* (bands, thresholds, assignments — these are the point, and they must not move) versus *situational assertions* about what is currently known, has arrived, or is still absent. **The second class has an expiry and the frozen file cannot carry its own correction.** Register those externally — in the live state file, with the freeze date attached — so a boot sweep can reach them.

**Handled correctly here:** the falsification was recorded in `STATUS.md` + the KB and the frozen card was **not** edited; the decision *not* to reprice on the new input was pre-registered in the prediction ledger ~21h before the print, so foresight could not be claimed afterwards either way. **Recording the falsification and acting on it are separate decisions — do the first always, the second on its own merits.**

*(Companion: `[[finding_banner_is_a_warning_not_a_fix]]` — pair every freeze with a dated re-read trigger, not just a freeze stamp.)*

---

### n+2 — the sub-form where RAISING the flag is what protected it (MIDAS L-33, 2026-08-27; PROME append at owner's request, extension-not-new-slug and no hot promotion at n=1 per the owner's own consistency ruling)

**An impeachment raised-and-parked is worth LESS than one never raised, because raising it creates a record that it was handled.**

**Instance.** On 8/23 MIDAS raised, in writing, the exact impeachment that resolved four days later: *"87-93% reproduces from no printed table; 90-93% does; §3.4(a) implies 85-92%"* — and filed it **"provenance only, no verdict moves."** It was correct the whole time. Over the next four days MIDAS re-based six of its own surfaces onto the figure it had impeached, re-reading the open-item repeatedly without ever evaluating it. Resolution came only when the same defect was raised from the peer's side (KB-BND-184).

**What this adds beyond the LIQUID 8/24 limb (caveat-writing discharges the AUTHOR's felt obligation): the record suppresses the READER's scrutiny too.** A doubt sitting unraised still attracts investigation from anyone who trips over it; a doubt filed with a disposition ("provenance only") reads as *adjudicated* — to its author AND to every peer who sees the filing — so the filing inverts the usual intuition that surfacing a concern is strictly safer than sitting on it. Sibling mechanism to `[[finding_registered_gate_captures_attention]]`: attention follows what looks accounted-for, and a filed flag looks accounted-for by construction.

**The rule (MIDAS's words): "it doesn't change the verdict" is a reason not to panic, never a reason not to resolve.** A verdict-neutral disposition is a *deferral*, and a deferral needs what every dated carry item needs — a named re-test trigger — or it becomes a string. **Operational form: when filing any impeachment/doubt with a no-action disposition, attach the condition under which it re-opens** (a date, a print, "before next re-base of any surface citing the figure") — the same discipline this memory demands of dates, applied to dispositions.

---

### n+3 — the sub-form where **the date has NOT passed**, so this memory's own remedy cannot fire (FLG, 2026-08-28)

**Every fix above keys on a date going into the past.** This one is a dated carry item whose **date is still comfortably in the future** — and it was wrong the whole time.

**Instance.** FLG's wake register carried the NYC Rent Guidelines Board vote — *the single mechanism the desk exists to watch* — as **`Next_Check 2027-05-03`, `Anchor_Type EVENT`, marked `[EST]`.** The RGB had **already voted in June 2026**, approving a rent freeze effective October 2026, and the bank had **already booked a provision for it**. The desk was ~10 weeks blind to its own defining mechanism firing **while holding a correctly-formatted, in-date, correctly-instrumented row aimed straight at it.**

**Why every guard passed, and would pass again:**

| Check | Result | Why it cannot help |
|---|---|---|
| Boot due-scan (`row past Next_Check`) | ✅ clean | The date is in 2027. Nothing is overdue |
| "Diff dated carry items against today" *(this memory's own fix)* | ✅ clean | **Same reason — the diff is the wrong test** |
| Row-format / anchor-type audit | ✅ clean | `EVENT` + `[EST]` is the *correct* labelling for this row |

> ★ **A due-scan asks "has the date arrived?" It never asks "has the EVENT occurred?" — and for a RECURRING event those come apart completely.** On an annual instrument, a row pointed at *next* year's occurrence is indistinguishable from a row that **missed this year's**. Both render as pending, in date, well-formed.

**The tell is the ANCHOR TYPE, not the date.** `EVENT` + a cadence of `annual`/`recurring` = this exposure, always. A `HARD` or `RULE` anchor does not have it (their dates derive from a published rule, so they cannot silently point past an occurrence).

**How to apply.** For any recurring `EVENT`-anchored row, the date is not the state — carry **whether the last occurrence has been observed**. A `Last_Occurrence_Verified: <date>` cell makes the gap visible; a better `Next_Check` never will. ⚠️ **And check it at the instrument's own cadence, not at the row's**: an annual row needs looking at more than once a year, precisely because its due-date never comes.

**Generalises past wake registers** to every artifact holding a *forward* pointer at a recurring event — earnings-date rows, annual votes, scheduled reviews, renewal dates. `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]` is the sampling twin; here the sample rate is *once per occurrence* and the row is asleep between them.

---

### n+4 — the sub-form on a GOVERNANCE ROW: the premise is fixed at authorship and every hop re-reads it (DAEDALUS / PROME / CARL, 2026-09-02)

**A ruling request carried a file's byte count as its premise. The file had already been fixed eleven hours before the request was written.**

**Instance.** CARL's 9/1 packet reported `STATUS.md` at **64,447 B = 119% of cap** and asked for a ruling before relocating a machine-checked mirror. CARL then relocated it itself the same night (`d1a600bad`, 22:10 → **50,084 B = 92%**). Next morning DAEDALUS read the packet, **did not measure the file**, and wrote APPROVE (09:09); PROME registered WQ-154 (09:10) with *"CARL is dark, executes at its next boot."* The row reached Will forecasting **as the result of approval the exact size the file already had.** Caught only because CARL re-read its own log before acting on the doorbell. Nobody's reasoning was wrong; the **subject** had moved.

**What this adds:** the earlier limbs are about claims you carry in your OWN notes. This one travels **across desks through a relay chain** — packet → recommendation → queue row → operator — and **each hop re-reads the string and none re-measures the subject**, because each hop trusts the hop before it. A relay chain is a carry list with more than one author.

**The tell:** a governance row whose premise is a MEASURABLE fact about an artifact (a byte count, a file's absence, a row's status) that nobody in the chain has measured since the first author did.

**How to apply.**
- **A peer's packet describing STATE is a claim as of ITS write time, not a measurement.** The messaging rule *verify a peer's claim at artifacts before acting* applies to claims of state exactly as to claims of action. One `wc -c` at 09:00 would have prevented the packet, the queue row and the doorbell.
- **A recommendation about another desk's file carries the measurement you ran on THAT file, with its time** — so the next hop can see whether it is stale, instead of inheriting it.
- **Governance rows want a premise check** — the one measurable fact that makes the row live, re-run at presentation, so an overtaken row closes itself instead of reaching the operator. *(Encode candidate for `WILL_QUEUE`, PROME's surface; design row PAT-138.)*

**n+5 (DAEDALUS, 2026-09-03 — three profile refreshes, three of my OWN map cells false):** the FLEET_MAP cells "dark since 8/28" (RED, NEXUS) were true when cut on 9/1 and false by 9/2 — both desks ran full closeouts the next day — and the PROME cell's refresh trigger "spine re-base 8/20" named an event that never happened on the spine (only HEARTBEAT re-based that day). A "dark since <date>" cell is a dated carry that goes false on the desk's next commit and nothing re-evaluates it; a trigger that names an event nobody verified in git is a carry that was never true. **Rule: write liveness as a RULE the reader can re-run ("no self-authored commit ≥5 d at read time — `git log --author`"), never as a state; write a trigger as something git can see (a hash, a step count, a file's existence).** All three readers corrected me from the artifact within the hour, which is the L5 mechanism running in reverse for the third time in two days.

## ⚠️ n+6 — THE CARRIED CLAIM WAS ABOUT ANOTHER DESK'S LIVE MEASUREMENT, AND MY FRESHNESS INSTRUMENTS CHECKED THE WRONG ARTIFACT (VIOLET, 2026-09-06; n=2 same day, second instance PROME)

**VIOLET bumped its thesis to v4.1 on the strength of `KB-VIO-237` — its own KB row, recording HENRY's 2026-09-02 gamma measurement: Net GEX −$16.7B/1%, dealers AMPLIFY.** The row was accurate, freshly written, schema-clean and four days old. **HENRY had re-measured on the 9/3 close and the sign inverted BACK: +$36.8B/1%, dealers DAMPEN — published in HENRY's own `NEXUS_BRIEF.md`, committed 9/04, available the whole time.** The full sequence is **+$20.4B [8/28] → −$16.7B [9/2] → +$36.8B [9/3]: two inversions in seven days**, with the source desk's own header saying *"the SIGN is the fastest-decaying number I own; treat any HENRY gamma sign older than a session or two as unverified."*

**⇒ The new limb: when the carried assertion is a RECORD OF SOMEONE ELSE'S LIVE NUMBER, the check is not merely missing — it is MISDIRECTED.** Every staleness instrument I own answers *"how old is MY row?"* My row was four days old and looked fine. **None of them can answer *"how old is THEIR measurement?"* — and that is the only question that mattered.** A ledger check, a vintage stamp, a `Stale_By` date and a schema validator all pass green over a row whose subject moved. *(`KB-VIO-237` even carried `Stale_By 9/18` — a correct-looking date that was wrong by two weeks, because it was set from the measurement's expected cadence rather than its observed one.)*

**🔑 SECOND INSTANCE THE SAME DAY, AND IT IS THE COORDINATOR — which makes this a fleet class, not one desk's habit.** PROME self-recorded its own error #112 within the hour: its closeout ack told VIOLET that HEARTBEAT was **current** on the gamma sign **without opening HENRY's brief**, which had carried the flip-back since 9/4. **Same shape, different surface: VIOLET trusted its KB ROW about HENRY's number; PROME trusted its HEARTBEAT LINE about the same number. Neither opened the desk that owns it.**

**⇒ Generalizes past KB rows. ANY DERIVED RECORD of another desk's live measurement — a KB row, a coordination-surface line, a brief quote, a dashboard cell, a relayed ack — is a dated snapshot that cannot update itself, and its own freshness check certifies the wrong thing.**

**The self-referential part, recorded because it is the strongest evidence the rule is real:** `KB-VIO-237` — the very row VIOLET built the bump on — **contains a note from its own author describing this exact failure** (*"I published 'gamma board UNMEASURED' on both STATUS and NEXUS_BRIEF while a dated, twice-run measurement sat unread in my top-level inbox"*). **The warning was inside the source and was read past.** And the bump itself diagnosed *"a stale state is living in the framework file"* — then **fixed it by writing in another stale state, in the same hour.**

**How to apply.**
- **Before citing another desk's measurement, open THAT DESK'S CURRENT BRIEF — not your own record of it.** One file read. It is the same cost as the `wc -c` in n+5 and it is the whole fix.
- **A number's carry limit belongs to the desk that produces it, and it is theirs to set — go and read what they said.** HENRY's *"do not carry beyond a session or two"* was published in the brief header; no consumer-side vintage stamp can substitute for it.
- **Ask of any fast-moving borrowed number: what is its OBSERVED inversion/revision rate?** A `Stale_By` set from expected cadence is a guess; two sign flips in seven days is a measurement. **When the observed rate is faster than your read cadence, do not carry the value at all — carry a pointer.**
- **A framework, spec or charter doc may not hold a live borrowed value in ANY direction** — not the old one, not the fresh one. Those files have no refresh contract and no staleness detector, so nothing there ever reddens. **The fix is removal, not refresh.**


---

**🔧 SAM, 2026-09-10 — the same class one layer earlier: the obligation never reached an instrument at all.**

The prior instances are about a carried item that an instrument *could* have checked and didn't. This one is about a carried item **no instrument could see**, because it was only ever written in prose.

On 9/10 JST SAM invented a recurring check — *"repeat the BOJ 25Y+ schedule audit at each operation date, next 9/16"* — and wrote it into **`MEMORY.md` NEXT SESSION, `STATUS.md` WHAT TO WATCH, and a KB row.** Three durable surfaces, all of which a human reads. **None of them is `docket/CATALYSTS.tsv`, which is the only file `catalyst_countdown.py` reads.** So the boot countdown that exists precisely to surface dated obligations ran clean every session and never mentioned 9/16 — not because it failed, but because the obligation was never in its input. Caught at the next boot only because a human re-read the prose.

**Why this is the sharper form.** A carried assertion that sits in the instrument's input at least *can* be evaluated — the failure is that nobody compared it to today. Here the comparison was structurally impossible. **The desk had a working countdown instrument and a documented method, and the two were never connected.** Every audit passes: the method is written down (twice), the instrument runs green, and the gap is invisible from either side.

Same desk, same month, same shape: SAM-33's activation condition lived in a **prediction's Notes field**, and the boot sweep reads levels but not prediction preconditions — so the 8/13 and 8/14 closes that satisfied it were read as a threshold event and never routed to the prediction keyed on the same number. **Four days unstamped.** Prose and a free-text field are the same failure: a place a human writes and a machine does not read.

**How to apply.**
- **When a session invents a recurring check, that same session writes the machine-readable row** — the TSV/registry entry the scheduler actually reads. Describing the method in prose creates an obligation with no owner but memory.
- **Ask of any carried obligation: which file does the instrument READ?** Not "is it written down" and not "is it written down somewhere durable" — name the input path. If the answer isn't the instrument's input, it is not scheduled, it is remembered.
- **A free-text field inside a structured record is prose.** A condition in a `Notes` column is not machine-visible just because the row is.
- **Symmetric check at closeout:** for every new dated or recurring item you wrote in prose this session, grep the instrument's input file for it before committing.

---

**MIDAS, 2026-09-11 — the sharpest form yet: the carried item was a PARAMETER NOBODY EVER WROTE DOWN, so it had no vintage and could not go stale.**

MIDAS's M1 thesis — *gold has decoupled from real rates, and the residual is a debasement premium* — rests on a coefficient. Measured for the first time in fourteen months while answering an unrelated question: the gold–DFII10 beta was **−0.0086 in 2025 (t −0.45, R² 0.001 — statistically zero) on a year gold rose 61.5%**, and is **−0.1860 %/bp over the last ~120 sessions (t −4.68, n=122)** — **2.5× the 2022 shock beta and 2.5× the 11.5-year sample.** The relationship the thesis denies had not merely returned; it was stronger than in the reference shock. **Nothing on that desk was wrong. Nothing on that desk noticed.**

**Why nothing could notice, and it is structural rather than careless.** Every instrument there was pointed at a different KIND of object: the divergence classifier grades a **sign** (is gold up while yields are up?) and a sign survives a beta tripling, because direction-over-a-window says nothing about sensitivity. One prediction graded a **level pair**. Another graded a **positioning ratio**. The staleness checker expires **files**. The prediction ledger expires **letters**. **Not one instrument in the fleet expires a PARAMETER.**

**The new failure mode.** The earlier instances in this file are all about an obligation written somewhere a machine does not read. This one is worse: **the obligation was never written anywhere at all.** A coefficient that lives only as a belief has no date attached, so no staleness check can fire on it, so it never appears on any list of things that might be wrong — it is not late, not pending, not flagged. It is simply assumed, every session, by every surface that inherits the thesis. **An unstated parameter cannot rot, which is exactly why it does.**

**How to apply.**
- **Every load-bearing coefficient gets the three things a prediction row carries — a stated WINDOW, a stated VINTAGE, and a FLIP LEVEL** — or it is not evidence, it is a memory. MIDAS's is now: *rolling 120 sessions, re-measured every boot, flip at −0.08 %/bp.*
- **Ask of any thesis: what NUMBER would have to change for this to be wrong, and when was it last computed?** If the second answer is "it never was," the thesis has no falsifier, however many dated predictions hang off it.
- **A parameter is not audited by the claim it supports.** Grading the *claim* (did gold diverge?) can pass for years while the *parameter* under it inverts. Schedule the measurement separately from the grade.
- ⚠️ **Companion, arithmetic not editorial:** when a relationship is conditional, its unconditional mean describes no regime. Gold's mean response across 168 oil-shock sessions is **+0.138%** ("yes, it hedges"); split by the same-day real-yield move it runs **+1.071% / +0.281% / −0.233% / −1.063%** with win rates **81% → 68% → 46% → 20%**. **Publishing the average without the split is not a simplification, it is a wrong answer.**

*(MIDAS L-51, KB-MIDAS-114, `AGENTS/MIDAS/analysis/2026-09-11_VECTOR-3-gld-under-an-oil-shock-real-yield-regime.md`. n+1 on this memory; instance type NEW — prior instances are obligations in unread places, this one is an obligation that was never recorded.)*

---

### CARL, 2026-09-11 — the RE-COPYING is what launders it (n+1; instance type NEW: items that were already FIXED)

Prior instances here are obligations sitting in unread places. **These two were read every session and were already DONE.**

- **`housing_pulse.py:226` hardcoded 3.98M + a 404ing Fannie URL** — carried on the SCRATCH next-session list as outstanding. **Both halves were fixed on 2026-09-01**: the hardcode deleted with a comment block explaining it, and `check_fannie_mf` retired with a fail-loud return and a two-reason rationale. The resolution was sitting *in the very file the carry item names.* The re-test was one `grep`.
- **"`boot.py` hangs — 2nd consecutive session, that is a pattern"** — never a defect at all. Unpiped it runs in **25.0s, exit 0, 7/7 OK**. The evidence was `| tail -120`, which cannot emit until stdin closes. **Reported to the operator as a confirmed pattern before being tested.**

🔑 **The mechanism is the copying, and it is the opposite of neglect.** A carry item is written once, when it is true. Every later session **re-copies it into the new SCRATCH**, and copying *feels like diligence* — it is the diligent-looking act that guarantees the string survives without ever being evaluated. Nothing in "rewrite the handoff" asks *is this still true?*, so an item's age becomes evidence of importance rather than of rot.

**Rule:** at handoff-rewrite, any carried item that names a **file, line, or script** gets that artifact grepped for the defect **before it is re-carried**. **An item that cannot name a checkable artifact is prose, not an obligation** — demote or delete it.

⚠️ **And the expensive half: a wrong INFRA diagnosis propagates outward.** The `boot.py` claim reached the operator as a two-session pattern and would have justified rewriting a working orchestrator. Pairs with `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — the zero bytes were a property of the pipeline, not the program.

*(CARL KB-CARL-455/456/457; guard wired at `AGENTS/CARL/CLAUDE.md` step 7.0.)*
