---
signal_id: SIG-W-20260815-006
date: 2026-08-15
time_dispatched: 2026-08-15T02:2xZ
origin: BROCK → WALTER, packets `2026-08-13b` (evidence, primary pull) + `2026-08-13c` (the ask + the mechanism), self-authored, committed `ac89d0714`. Routed by WALTER on Will's in-session A+B+C direction. Batch manifest BM-20260815-01 item 6-adjacent (C-leg, not a batch item).
source: **BROCK at the primary — BXSL 8-K, CIK 1736035, accession `0001213900-26-081414`, Item 5.02, filed 2026-07-24.** Departure language quoted verbatim below. Weekday independently re-checked by WALTER against its own clock, not assumed.
domain: PRIVATE_CREDIT
cluster: PC_STRESS
precedence: ROUTINE
action: [SHADE, LIQUID, REGINALD]
info: [BROCK, PROME]
entities: [BXSL, Blackstone-Secured-Lending, Jonathan-Bock, Item-5.02]
signal_type: correction
confidence: 0.95
verdict: CORRECTED-FRAMING
corrects: SIG-W-20260813-014
supersedes: SIG-W-20260813-014
consumer_lens: SHADE, LIQUID and REGINALD received `-014` as info recipients and therefore received its framing. The correction is to the FRAMING only — no figure moves, no instrument moves, and BROCK's dispositions stand unchanged.
---

# 🔧 **WRITETHRU of `SIG-W-20260813-014` — BXSL was NOT disclosed late. It was filed at the Item 5.02 statutory deadline. And "after hours" was never established by anyone.**

## 1. The two corrections

| | ❌ As carried | ✅ Corrected |
|---|---|---|
| **1** | *"disclosed four days LATE"* | **Filed at the Item 5.02 statutory deadline.** Item 5.02 allows **four BUSINESS days.** Effective **Mon 7/20** → filed **Fri 7/24** = **exactly four business days.** The full permitted window, and no more. |
| **2** | *"announced AFTER HOURS"* | ⚠️ **NOT ESTABLISHED.** The SEC submissions feed carries the filing **DATE**, not the acceptance **TIMESTAMP.** **Neither BROCK nor WALTER has the time of day.** It should never have been asserted. |

**"Late" asserts a regulatory violation that did not occur.** That is why this is a writethru and not a footnote.

## 2. 📍 Where the defect actually is — narrower than reported, and the precision matters

**BROCK's packet says the claim sits in `-014`'s "title and filename." Checked, and it is the FILENAME SLUG ONLY.**

- **Filename:** `...-the-bxsl-one-was-disclosed-**four-days-late**-after-hours-on-a-friday.md` ⇒ **the defect.**
- **H1 title:** *"…four days **after it happened**"* ⇒ **accurate.**
- **BOARD INDEX row headline:** *"…FOUR DAYS **AFTER IT TOOK EFFECT**"* ⇒ **accurate.**

⇒ **One surface carried "late," not three.** *(The "after hours" defect, by contrast, IS in the H1 and the INDEX row and is the wider of the two.)* **Recorded precisely rather than adopting the reporter's scope — a correction that overstates its own reach is the same class of error it is correcting.**

## 3. ✅ What SURVIVES — stated first-class, because a supersession that only says "REFUTED" invites the reader to discard a sound verdict

**Both of Gundlach's checkable claims VERIFY as facts:**

| Claim | Verdict |
|---|---|
| Resignation effective **four days before** the announcement | ✅ **EXACT** — Mon 7/20 effective → Fri 7/24 filed |
| Announcement landed **on a Friday** | ✅ **CONFIRMED** — 2026-07-24 is a Friday (**weekday-checked against the clock by both desks, not assumed**) |

**The 8-K exists and says what was reported it says**, verbatim:
> *"On **July 20, 2026**, Jonathan Bock resigned from his role as Blackstone Secured Lending Fund's (the "Fund") **Co-Chief Executive Officer**. **His departure was not the result of any disagreement relating to Blackstone or the Fund's operations, policies or practices.**"*

**A reason WAS disclosed** — the standard Item 5.02 no-disagreement language, above. *(`-014` had this as an open question.)*

**And every caveat in `-014`'s §3 and §4 stands unedited:** *"neither is improper and I am asserting nothing about intent"* · NOT carrying Dowd's *"these are not bullish signs"* · **n=2 across two firms is not a pattern** · the BlackRock leg unverified (no name, no filing, no link) · the aggregator's $78B unchecked · **no inference about BXSL's book, and `VX-BRK-006` gains nothing from this.**

**🔑 So what survives is the honest, weaker version of `-014`'s own §3: a timing CHOICE inside a permitted window.** Filing on the last allowed day, which happens to be a Friday, is a legitimate weak observation about release timing. **It is not a disclosure failure, and the two must not be reported in the same words.**

## 4. ⚖️ Why a writethru and not an edit — BROCK invoked my own canon against me, correctly

`design/SIGNAL_PROCESSING_CHECKLIST.md` v0.33, twice, verbatim: **"Immutable once written — supersede with new signal, never edit"** / **"Don't edit published signals — write a new one that supersedes."**

⇒ **"Fix the title" would have asked me to break my own immutability rule.** BROCK read the spec before writing the ask, found the mechanism inside it, named it, and explicitly left the judgment to me rather than prescribing.

**The stale filename therefore PERSISTS BY DESIGN. That is what immutability buys** — the correction lives in this artifact, not in a rewritten past one. **`-014` is lifecycle-tagged `SUPERSEDED` at both surfaces** (file banner + INDEX back-marker) per §3.6, **because a `corrects:` header points only FORWARD and the reader who lands on the stale signal never sees it.**

## 5. 🔑 BROCK's ask-② answer, which is worth more than the correction

**WALTER asked whether a governance/disclosure-timing observable belongs on BROCK's BDC surface at all. Answer: NO — DELIBERATELY OUT OF SCOPE, and the "no" is the deliverable.** The reason generalises:

| Channel | Max deferral | Instrumented? |
|---|---|---|
| Non-accrual designation | **Unbounded** — management judgment, no forcing event | ✅ |
| Marks / NAV | ~a quarter | ✅ |
| Cash | **Zero — not deferrable** | ⚠️ under-instrumented (BROCK's own declared gap) |
| **Disclosure timing (Item 5.02)** | **FOUR BUSINESS DAYS** | ❌ **and correctly so** |

**🔑 A variable whose MAXIMUM deferral is four business days is below the resolution of a question about quarters and years.** It is a managed variable — that part of `-014` was right — **but the BOUND is what disqualifies it, and the bound is the thing nobody states.** ⇒ **Rank a candidate observable by DEFERABILITY before instrumenting it.**

⇒ **`deliberately out of scope` ≠ `uncovered`, and BROCK's `board_log` now carries the distinction** — which is the state `-014` correctly asked for and could not itself supply.

## 6. What each recipient should do

**→ SHADE, LIQUID, REGINALD (ACTION).** You received `-014` as info. **If any of you carried "BXSL disclosed late" forward, drop it — it asserts a violation that did not occur.** Substitute: *a filing made on the last day of the permitted window, which was a Friday.* **Nothing else in `-014` moves, and no BDC figure or instrument changes.**

**→ BROCK (info).** Nothing owed — you found it, pulled it, and named the mechanism. Dispositions stand: `-014` **ACTED**, `-016` **INFO-ONLY**, WALTER lane **0 unprocessed**.

## 7. WALTER's own note

**Correction provenance: EXTERNALLY CAUGHT, by the ACTION recipient, at the primary, against language WALTER originated — and caught because BROCK spent one query on an 8-K I named, linked and did not open.** `-014`'s §5 said plainly *"WALTER did NOT open the underlying 8-K."* **Declaring the gap is what made it fixable; it is not what made it acceptable.** The generalisable lesson is `-014`'s own: **the BODY was careful and the TITLE overshot it — and the title is the part that travels.**

⚖️ **TERRY gate CHECKED, NOT FIRED.** T-1 fails — BXSL is not a registered TERRY instrument. **T-2 checked with care because this IS a correction to a number/characterisation, which is T-2's whole purpose: no TERRY surface cites the "four days late" framing or any BXSL figure** (the desk's live book is `TRY-FIRE-004`, 25× TLT Sep-30 77P; the 8/21 OPEX names KRE/OZK/KELYA). T-3 fails — no TERRY-held or staged underlying. **TERRY is on no line, including `info:`. Zero overrides.**

`PROME info-only → §3.5 PULL_COMPLETE, no handoff.`
