# HEARTBEAT NINETEENTH RE-BASE — cold-read accounting and declared residue

**Owner:** PROME `prome-73` · **Written:** 2026-09-19 11:17 ET · Sat 2026-09-19, markets CLOSED
**Rule:** `PROME/CLAUDE.md` § Session Process Controls, WQ-178 read budget — ONE blind read on the PLAN, ONE on the RESULT; fix ❌ only; every un-fixed ⚠️ is declared here.
**$0 moved by PROME · no gate graded BY PROME · no threshold set, moved, re-specced or fired · no trade proposed.**

---

## The re-base's stated reason was WRONG and that is the first thing in this record

PROME had been telling itself, across SCRATCH, STATUS and HANDOFF, that *"the chain is at 3 and amendment #4 is BARRED."* **No canon says that.** `PROME/HEARTBEAT_COLD.md` §C reads **"Re-base rule: chain >~5 amendments or ~2 weeks"**, and `PROME/tools/prome_gate.py` `check_heartbeat_chain` is **ADVISE-only**, tripping at n≥4 with the text *"re-base rule trips at ~5: plan it into the next substantive session."*

PROME hardened its own advisory into a prohibition and then cited it back to itself on three surfaces. The plan cold read caught it, **after** the wrong citation had already been written into an archived snapshot header, where it is now corrected.

**The work was still right, for a different and real reason:** the file stood at 98% of its 32,550 B read-cap budget (rotate trigger ≥75%) and `READ_CAP.md` rule 7 required a re-check at any append. **It was not blocking.** This was reported to Will as blocking and corrected to him in-session.

⚠️ Class: `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` run in REVERSE — the usual failure is an advisory being ignored; here an advisory was over-obeyed and became an invented rule. Both are failures to read the grant.

---

## Scores

| Read | Claims | ✅ | ⚠️ | ❌ | All ❌ fixed? |
|---|---|---|---|---|---|
| PLAN (blind, Opus) | 57 | 27 | 19 | **11** | yes — before any edit to the base |
| RESULT (blind, Opus) | 46 | 21 | 15 | **10** | yes — this session |

**No third read was taken.** WQ-178 allows one only when a ❌ fix on the result changed a RULE's meaning; none did — the ten result fixes were a wrong gate state, three wrong pointers, two wrong counts, a missing source, a self-contradiction, a sourcing upgrade and a dead cross-reference.

---

## What the PLAN read caught, before anything reached the live file

The plan read is the reason two false claims never shipped:

1. ⛔ **"FOUR irreconcilable Brent November readings."** The fourth, $98.77, is **HANS's `BZZ26.NYM` DECEMBER contract**, labelled as such in its own packet, with the −5.8% move built on it **already withdrawn by its author**. PROME had read HANS's narrative supplement and not its named-contract table. **Three readings, not four.**
2. ⛔ **A vendor-remapping hypothesis built entirely on (1)** — that a continuation ticker's HISTORY may not be stable, and therefore "the L429 repair is larger than written." It rested on the misread and was dropped.

Also caught and fixed pre-edit: citing "two uncoordinated desks agree" as corroboration when DOCKET L430 **explicitly forbids that phrasing**; three "current"/"today" tokens attached to levels inside a plan whose own invariant bars them; labelling $103.87 both "Established" and "does not reconcile" nine lines apart; calling the 9/17 leg "settled" when L430's named settling test (BRENT at a SECOND VENDOR) has not been run; calling a vendor's own adjustment factor "corroboration" of that same vendor's dividend row; retiring a kill-on-sight entry as spent when its own reason said 2 of 3 shares are STAGED and the card is RE-ARMED; and killing *"SPY fell while SPX rose"* as though it were false, when it is TRUE on raw prices and only the tracking INFERENCE dies.

---

## What the RESULT read caught — all ten fixed

| # | Finding | Fix |
|---|---|---|
| ❌1 | One-liner said the real 10Y was **18bp** through the add line while the body said **11bp** — a retired 2.68-vintage distance welded to the new 2.61 level | distance corrected, and the provenance of the 18bp named |
| ❌2 | 🔴 **`GATE-REG-T02` listed as "the tightest line on the book" under *Closest LIVE lines*. It is RESOLVED — FIRED 2026-09-01, terminal, consumed by ROLL70.** A Monday close below $78 would have been read as a fresh fire | replaced with an explicit ⛔ that it is not live, that a sub-78 close is a SUPPRESSED RE-ENTRY, and that the live successor is `GATE-TERRY-ROLL70-EXIT` |
| ❌3 | `GATE-TERRY-007` written "0-of-6" against the gate's own "0-of-5" — the run of failures used as the denominator instead of the requirement | corrected, with the convention stated in the cell |
| ❌4 | This report was cited by the base and did not exist | written |
| ❌5 | Cold **§19.2 · §19.3 · §19.8** cited and absent — Rates, Credit and Metals pointed at nothing | re-pointed to §18.2 / §18.3 / §18.8, each saying plainly that no new long-form was written this base |
| ❌6 | 🔴 **`fleet_dashboard.py` was returning BUILD FAILED and the derived view was DEAD, not stale** | root cause found and fixed — see below |
| ❌7 | The $1.8890 distribution had no source and no date token in the file, and its predecessor had called it UNVERIFIED | basis, ex-date, read-date and strength (INFERRED-STRONG, not verified at issuer) all written into the cell |
| ❌8 | The kill cell published **−5.09%**, which back-solves a 9/18 Brent November level the same file kills | no replacement percentage published; the reader is sent to HANS's own memo |
| ❌9 | ⛔ **"at the Estonian/Latvian/Lithuanian defence ministries."** OSPREY's provenance is **mil.ee plus ERR, LSM and LRT — one defence ministry and three national PUBLIC BROADCASTERS** | corrected in the file, and the old phrasing declared dead. **This had also been said to Will and was corrected to him in-session.** Class: sourcing upgraded on a verbatim-correct finding — the exact class §KOS.3 exists to kill |
| ❌10 | "WQ-150 root-④" cited while the file directs readers to `WILL_QUEUE.md`, where WQ-150 does not appear | re-pointed to its real home in `SCRATCH.md` § Continuity, with the absence stated |

### ❌6 in full, because the root cause was not the one the error message named

`PROME/HEARTBEAT_DASHBOARD.md` still declared the eighteenth base and chain 3 after the re-base was written. Resetting it to chain 0 did **not** fix the build. The real cause: **one orphaned `dashboard-amendment` block — amendment #3 of the EIGHTEENTH base — was still in the file, sitting immediately below a PRIOR note that declared projections removed.** The builder requires `len(amendments) == len(projections)`, so with the new base at chain 0 a single surviving block is a mismatch exactly as a missing one is.

🔑 **The generalisable part: this file's own rule — "at a HEARTBEAT re-base, remove projections for amendments folded into the base" — has NO CHECK.** A miss is invisible until the builder fails, and the builder's message names the **amendment** side (*"each HEARTBEAT amendment needs one reviewed dashboard projection"*), which points a reader at HEARTBEAT.md rather than at the orphan. `[[finding_guard_correctness_and_wiring_are_independent]]`. Nothing is lost: the content is carried by the nineteenth base (§5 · §2 · §3) and the block itself is verbatim at cold §A21.

---

## Structural work done at this re-base

- **Pre-re-base snapshot**, verbatim, body **byte-identical** to the source (round-trip asserted in-session): `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-19.md`, body crc32 **1749551517** over **32,182 B**, git receipt `git show 496fbf9d26ccf701ed1c77f70e8329cb20074f34`.
- **Amendments #1–#3 rotated verbatim** to cold **§A19 · §A20 · §A21**, each with a crc32 and byte count in its header; all three round-trip-verified byte-identical against the hot blocks before the hot file was rewritten.
- **Long-forms written** to cold **§19 · §19.1 · §19.2R · §19.5 · §19.7**; six theatre/sourcing kill entries moved with their reasons to **§KOS.3** (moved for space, none retired).
- **A new control built and run against this very rotation:** `PROME/tools/rotation_integrity.py`, which asserts that the hot∪cold section-header multiset never LOSES a member. It is ZHAO's finding, generalised — its own read-cap rotation silently deleted a nine-row subsection while every existing guard passed green, because **a rotation's success metric and its failure signature are the same observation: bytes went down.** Acceptance conditions were written before the implementation and are executable as `--selftest` (7/7 pass). **Falsified against ZHAO's real defect: run across the actual commit, it names `### Domestic Stress` as LOST.** Run on this re-base it reports 0 genuine losses — the only two flagged are intentional heading-text changes, which it correctly refuses to guess about (a rename reads as loss + addition by design).
- **Dashboard tile parity checked before and after:** 9 tiles → 9 tiles, none lost. ⚠️ This check is **not** the rotation-integrity check and caught something it cannot see: an earlier draft silently dropped the MOVE and OZK levels, which live *inside* one header's content. Two complementary instruments.

---

## DECLARED RESIDUE — un-fixed ⚠️, carried not hidden

**From the RESULT read (15):**

1. **Two different "79c" figures are live** — max−min of the 9/18 triple ($103.87 − $103.08) and the 9/17 delta ($104.82 − $104.03). Same number, different subjects.
2. **"~577 kb/d ≈ 4–5% of European runs" carries no date token**, violating the file's own rule. Cold §19.1 dates it June 2026.
3. **"Bund 10Y 3.50 [9/18, HANS]"** — `[9/18, HANS]` is not a form the date convention defines (close? intraday?). HANS's own row carries two values from two sources.
4. Several levels carry a source-and-date token the convention does not formally define (`[Baker Hughes 9/18]`, `[as-of 9/15]`, `[9/18, HANS]`).
5. **The one-liner's own levels carry no tokens** — SPX, VIX and DFII10 are dated only by the surrounding prose.
6. **"Bessent–He Lifeng met this weekend"** is indexical in a file written on a Saturday.
7. **VIOLET leg 2's "2 sessions left"** was correct when written 9/18; from Monday it is fewer.
8. **"35d only −12.5%"** is a CONTRACT-COUNT figure sitting immediately beside magnitude percentages — HENRY's artifact separates them.
9. The 4.909% discharge matches BRENT's artifact but is PROME's transcription of an owner claim, not an independent reproduction.
10. **"Fire-ledger: ZERO fired-unexecuted" is an undefined term** beside three gates whose legs ARE fired — a stranger cannot tell what it excludes.
11. **The "Unmoved:" list reads as complete and omits 8 of 20 GATES rows.**
12. **`HANS-T-13` sits in "Closest live lines" with no level and no distance** — the only entry a reader cannot rank.
13. WQ-192's scope as summarised is narrower in the queue than the file implies.
14. "WQ-169 fact 4" — the queue row enumerates its facts differently.
15. **Cold §A21 carries a kill the hot file now contradicts** (MOVE/^SKEW dated 9/18). §A21's header declares it history, which covers it, but the contradiction is real and a reader arriving at §A21 first sees the superseded rule.

**From the PLAN read (19), the ones that survive into the base:** the `Brent` parser anchor is real but under-specified (two anchors, one positional — verified working this session, 42 tokens parsed, 9 tiles mapped); the 13-for-13 equity re-pull is a TRANSCRIPTION check at the same vendor and is labelled as such in the file; VVIX 87.38 is one leg of a declared two-vendor spread and its reproducing settles only that leg; the `BZZ26`-distinguishes-months observation and the $1.8890 dividend row both rest on in-session vendor pulls that no file holds; "BRENT is dark" was asserted from commit recency, not a `ListAgents` receipt.

**Size:** ⛔ **this base lands above its own rotate line and did not shrink to pass.** Read the figure from `PROME/tools/measure.py`. The long-forms are already in cold and six kill entries are at §KOS.3, so the remaining weight is not prose that can be tightened: **the stress-dashboard level line and the kill-on-sight cell are each multiples of a channel's budget, both are monotonically GROWING LISTS, and neither has a budget or a rotation rule of its own** — the same structural shape as SCRATCH's generated DOCKET-VIEW block (L380 class). **PROME did not shrink either list, because every entry in both is load-bearing and a dropped kill entry is worse than an over-budget file.** That is a stated choice, not an oversight, and it is the third consecutive session PROME has recorded declining a size fix rather than taking one quietly.

---

## ⛔ ADDENDUM 2026-09-19 13:3x — THE RULE-7 RE-CHECK THIS BASE ORDERED, AND ITS RESULT (ARGUS ❌2)

This base's own header says **"re-check at ANY append or on 2026-09-26, whichever is first."** Amendment #1 was appended at this closeout, so the clock **fired**, and ARGUS found no re-check recorded anywhere in scope. Run now, `read_cap_check --agent PROME`, rc read bare:

| point | bytes | % of the 32,550 B budget |
|---|---|---|
| before the re-base (`git show 19efc0cbf:HEARTBEAT.md`) | 32,182 | 98.9% |
| after the re-base | 30,583 | 94.0% |
| **after amendment #1 (now)** | **32,253** | **99.1% — 🟡 ROTATE-TIER** |

⛔ **`over_budget=1, over_cap=0` — it is over the flow-rule budget and NOT over the harness read cap, so nothing truncates.** ⚠️ **The re-base bought 4.9 points and amendment #1 gave back 5.1.** That is not a defect of the amendment — the amendment carries a live position dispute Will needs — but it does mean **a re-base that lands at 94% is one ordinary append from where it started**, which is the L380 shape and is the honest read of this base's durability. **Recorded, NOT rotated:** a second re-base on the same day as the first, at the tail of a long closeout, is exactly L369's lesson. The next append re-fires the clock.
