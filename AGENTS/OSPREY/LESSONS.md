# OSPREY LESSONS — Mistake Patterns to Avoid

*Read at boot (SPAWN PROTOCOL step 3). **Hot/cold split 2026-09-08** under the fleet READ-CAP rule: this file keeps each item's headline, one-line incident and its **Rule** (rules verbatim); the full narratives and the long corollaries are archived verbatim at `archive/LESSONS_ARCHIVE_2026-09-08.md` (crc32 in its banner). **Item numbers 1-8 are stable and cited fleet-wide** — the file is chronological except item 4, a cross-cutting note. Items 1-2 are inherited from HAWK's frozen `LESSONS.md`; 3-8 are OSPREY's own.*

---

## 1. [2026-07-12] A prediction's literal wording narrows your evidence sweep — search the MECHANISM, not just the named targets
**Founding calibration lesson (HAW-15).** HAWK re-checked a prediction by searching its named terminals, missed a week-long Ukrainian campaign against shadow-fleet **tankers** — a different channel of the same mechanism — and was wrong twice in one day; Will surfaced it.
**Rule:** when re-checking a prediction at boot, sweep the underlying **mechanism** broadly (here: "Ukraine attacking Russian oil" — refineries AND terminals AND tankers AND pipeline), not just the prediction's named literal targets. Then map what you find back to letter-vs-spirit. Write prediction labels that name the mechanism, not one channel of it.
**Corollary — own-ledger staleness:** don't trust your own ledger as the baseline without checking its swept-through mark + running a completeness pass first; when a first sweep says "nothing," escalate to a date-careful multi-angle sweep before banking a "no." **A first-pass "no results" is a search-coverage statement, not a fact.** (Root cause of the Tier-1 ledger fixes in CLAUDE.md.)

## 2. [2026-06-12] Live-war boot needs a day-by-day gap sweep, not topic searches
**HAWK, Jun 12 (Iran).** A topic-shaped boot missed a chokepoint-closure declaration and a second strike night because the kinetic timeline had stopped days earlier.
**Rule:** during an active conflict, boot must sweep day-by-day from last STATUS date through boot date (date-specific queries or an equivalent chronology source), and explicitly check each open watch item against the window before writing any re-mark.

## 3. [2026-07-12] A swept-complete DATE is not proof of swept-complete CONTENT
**OSPREY's first session.** A ledger mark dated *that day* still hid four material strikes, including Omsk — Russia's largest refinery, struck for the first time.
**Rule:** don't let a boot-time staleness check (comparing today's date to the mark) substitute for actually re-running the sweep when the theater is ACTIVE — the step-5b check catches OLD marks; it does NOT catch a fresh-dated-but-incomplete mark. When inheriting or reading someone else's "complete" ledger at the start of a live-war domain, always run one independent day-by-day gap sweep before trusting the mark, regardless of how recent it looks.

## 4. [2026-07-12] Cross-cutting: a channel-sequence narrative must be re-tested against the full ledger
**HAWK's Pattern ①** read the crude→products shift as a one-way switch; the corrected sweep showed the crude channel never went dormant (Novorossiysk 5/23, 6/8 missed).
**Rule:** don't assume a channel-sequence narrative holds without periodically re-testing it against the full ledger — "the campaign moved on" is a hypothesis, not a default state, and a clean narrative that never gets re-tested is exactly what produced the HAW-15 miss above.

## 5. [2026-07-31] ★ A REGISTERED GATE CAPTURES ATTENTION — the loud tracked event hides the quiet countable one
**OSP-01 FAILED.** While the desk ran a daily, named adjudication on the CPC gate (Kazakh crude, non-countable), **Sheskharis** — Russian, ~650 kb/d, one-fifth of seaborne crude — halted for five days and the desk wrote "no new terminal damage" the day Bloomberg reported it. Wrong for nine days, routed to two consumers in that state.
**Rule:** when a gate/tripwire is live on ONE instrument inside a channel, **every session must run a separate, explicit sweep of the channel's OTHER instruments and say so in writing** — the gate check does not discharge the channel check, and a channel score must never be re-affirmed from gate evidence alone. Concretely: a CPC adjudication may **never** be the basis for a Channel-2 mark. Generalized: **ask "what in this channel is NOT being watched by the thing I'm watching?"** *(Promoted to auto-memory.)*

## 6. [2026-08-20] ★ AN ENUMERATED-MECHANISM TEST IS A HIDDEN CLAIM THAT THE MECHANISM LIST IS COMPLETE
**OSP-05 graded 0-of-2** (destroyed capacity / sustained interdiction) in the week exports printed 3.58 M bpd, a fifth straight fall, strike-attributed. The barrels left by a third route — **deterrence of offtake** — that no leg named. Bloomberg's own wording carried the tell: *"actual and threatened."*
**Rule:** before registering any N-leg test, **base-rate the LIST, not just the legs** — ask *"name a way the claimed outcome could occur that fires none of these legs,"* and if you can name one in under a minute, the test is mis-specified. Prefer at least one **outcome-measuring** leg alongside the mechanism-measuring ones. When a test grades 0-of-N while the outcome visibly occurs, **the finding is the test, not the world.** Companion: the letter you publish is the letter you will be graded on, so it must match the thing it tests — no broader, no narrower (the 8/8 ladder's missing cargo qualifier).

## 7. [2026-08-20] ★ A NAMED-FACILITY LIST IS A CLOSED SET STANDING IN FOR AN OPEN ONE — and adding the missing name is the same error again
**Tamanneftegaz** (largest private oil transshipment facility in southern Russia, ≥10 tanks destroyed 7/30) sat inside a window the ledger header called a "full mechanism-level sweep" and surfaced 21 days late — the sweep was still anchored on the facilities the desk already knew.
**Rule: the fix is NOT "add Taman."** Anchor the sweep on MECHANISM + GEOGRAPHY — every Russian Black Sea / Azov / Baltic oil-handling port, named or not — and treat any facility-name list as a *starting* set that must be exceeded, never as the scope. At least one query per sweep must contain **no facility name at all.** (Item 6 recurring in evidence-gathering instead of test design. Applies equally to **source sets** — a canvass is an enumeration too: the 8/21 war-risk print sat in an outlet a two-canvass, 8-outlet set did not include.)
**Corollaries (full text in the archive):**
- **A — Declining to patch is a detector.** A patch that gets adopted is never asked what it fails to cover; a patch you refuse to extend must be. *Whenever you decline to patch, write down what the fix you already have does not reach.*
- **B — An EVENT-RELEASE absence is weaker evidence than a SERIES non-increase.** Held at B3, not load-bearing (shared training environment = common cause even when inputs are disjoint); promotion needs an instance from outside this fleet's habits. Before logging any absence, ask which kind it is.
- **C — A causal claim about another agent's reasoning is verifiable exactly to the extent the reasoning was recorded.** Record WHY, not just WHAT. Unverified guesses about motive land charitable; refuse the credit and book the accurate version.
- **D — A fix inherits the PARAMETERS of the limb it replaces.** List every constant you carried over and re-derive each against the new row's window, units and resolver; an unbound placeholder must never leave a draft. An argument's own direction tells you which number you have not checked.

## 8. [2026-09-02] ★ A NAME-SHAPED QUERY CAN ONLY RETURN EVENTS YOU ALREADY SUSPECT — for a clock that counts EVENTS, sweep a source indexed by TIME
**Four instances of one shape:** (1) HAW-15 named terminals; (2) 8/16 Skiros — a hull-class check would have declared a false channel kill; (3) 8/24 — a vessel-name/keyword check read 17/21 on the Channel-3 clock four days from expiry while two shadow-fleet hulls had been struck; (4) **8/1 Yanina, found 9/8** — an object-class anchor ("all refinery-class") missed a confirmed sinking for 38 days. Each time the fix was "narrow the name gap"; each time the list was not the problem.
**Rule — registered as an INSTRUMENT, not a resolution:**
- **Before any name-shaped query, sweep a dated-window source covering the whole gap** (for Channel 3: a weekly maritime security bulletin, Black Sea / Azov / Baltic). Name queries come **after**, to enrich rows the window sweep already found.
- **Never grade a channel kill on the absence of NAMED events.** Absence of names is a fact about your index, not about the sea.
- **When a clock is within one sweep-interval of expiring, that is the session to distrust your own quiet.**
- **Ask what UNIT your clock counts, then what your source is INDEXED BY.** If those differ, the search cannot see what the clock measures, and every check will pass clean.

---
*Not inherited to OSPREY (FALCON-only per build spec §2): wording-identity discipline (HAW-10) and dormant-secondary-vector re-sweep (HAW-03) — readable at `AGENTS/HAWK/LESSONS.md`.*
*Related fleet memories: `finding_scan_keyed_on_naming_reads_local_form_as_absence` · `finding_instrument_reports_clean_against_the_wrong_reference` · `finding_attribution_authenticates_a_figure_its_named_source_never_produced` (instance 3 is this desk's 9/8 Urals correction).*
