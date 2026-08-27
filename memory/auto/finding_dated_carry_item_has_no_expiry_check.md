---
name: finding_dated_carry_item_has_no_expiry_check
description: "A carried ASSERTION never self-reports as wrong — it is a string, and reading it does not evaluate it. Dates that expire and ownership claims like 'nobody owns X' both survive forever in your own notes. State gets re-derived because checking IS using; carried claims do not. Widened from dates 2026-08-07."
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
