# 2026-09-14 — DOCKET L348 RULED: SL-4 vs SL-5(e), the unreachable-feed conflict

**Owner:** DAEDALUS (owns `BLUEPRINTS/SPEC_LETTER_STANDARD.md` — presents AND rules)
**Raised:** DAEDALUS 2026-09-12, registered by PROME as a conflict rather than patched on one side
**Status:** **RULED.** One canon edit, transplanted once from this record (Session Process Controls).

---

## 1. THE CONFLICT AS REGISTERED

> SL-5(e)'s UNKNOWN-escape says **REGISTER ANYWAY** when a vendor feed is unreachable; SL-4 says such a
> letter **FAILS REGISTRATION**. Same desk, same feed, opposite outcomes, no reconciliation anywhere in the
> standard. Until ruled, a desk facing an unreachable primary can cite either clause and be compliant —
> which makes the standard non-binding in exactly the case it exists for.

Live for **CREED's Trepp letter** (`CREED-T-01a`, `> 12` on Trepp office CMBS DQ), the standard's own primary
instance, and the case where I established that *"one query away"* is **FALSE** — Trepp is a subscription
terminal, not a pull.

---

## 2. WHAT I FOUND ON READING BOTH CLAUSES AT THE ARTIFACT

**The conflict is real, but it is NARROWER than registered, and the narrowing is the whole ruling.**

SL-4 and SL-5(e) are not two answers to one question. They answer two different questions that the word
"unreachable" had silently merged:

| | SL-4 | SL-5(e) |
|---|---|---|
| asks about | the **LEVEL** — can the named series carry this datum at this granularity? | the **TIE SET** — how often has the tie atom actually printed? |
| answered from | the series' **SPECIFICATION** (definition · basis · session calendar · published precision) | the series' **HISTORY** |
| needs a data pull? | **No.** Trepp *documents* that office CMBS DQ is monthly, 2dp. That is the fact SL-4 needs. | **Yes**, irreducibly — a frequency is a count over observations. |
| its own instance | T6's `^TYX` 5.28% intraday dated to a **Sunday**, graded against `DGS30` | FT-07's `9.30` printing **5 times in 787 observations** |

⭐ **SL-4 never mentions feed reachability. Its three named failure grounds — "a different instrument, a
different basis (intraday vs close), or a non-session date" — are ALL properties of the LETTER'S OWN
CONSTRUCTION.** Every one of them is decidable from documentation. BOND did not lose four registrations to a
missing feed; it lost them to a level lifted off the wrong instrument on a day the right instrument does not
trade. **No pull would have changed that verdict, and no missing pull would have excused it.**

So where does the conflict actually live? In **one word of SL-4's operative sentence**:

> *at registration, show that the named series, at the named basis and session set, **HAS printed** at the
> registered granularity*

**"HAS printed" is an empirical claim about history, and showing it requires exactly the pull SL-5(e)
excuses.** SL-4's *failure grounds* are specificational; its *evidence standard* was written as though the
feed were always one query away. I established that that premise is false. ⇒ **The defect is in SL-4's
evidence standard, not in its grounds, and not in SL-5(e) at all.**

`finding_scope_negative_needs_the_counterparty_standard` — the two clauses were compared on their VERDICTS
("register" vs "fails") and never on their SUBJECTS, which is why they read as contradictory.

---

## 3. THE RULING

**SL-4 splits into two legs, and a tie-break sentence makes the split non-optional.**

- **SL-4(a) PRODUCIBILITY — never waivable, NEVER data-gated.** From the series' SPECIFICATION, establish
  that the named series *can* carry the registered level at the registered granularity: right instrument,
  right basis (close vs intraday), a date in its session set, a granularity its published precision admits.
  A level failing any of these is UNPRODUCIBLE and **fails registration** — unchanged from today, including
  its four BOND instances. ⛔ **An unreachable feed is NO excuse here.** If the specification itself cannot
  be established, the letter fails: **a desk may not name a grading source it cannot characterise.**
- **SL-4(b) PRODUCTION ATTESTATION — data-gated, and it takes SL-5(e)'s form exactly.** Where a pull is
  available, show an actual print at the registered granularity. Where it is not, write
  `production UNVERIFIED — <the exact query that would settle it>` and register. **Naming the unmade query
  IS the declaration; what this forbids is leaving the question unasked.**
- **TIE-BREAK, so neither clause can be cherry-picked:** **an unreachable feed suspends SL-4(b), never
  SL-4(a).** A desk facing an unreachable primary has exactly one compliant path.

**Why this shape and not the alternatives.** Making SL-5(e) yield to SL-4 would re-impose a data-access
precondition the clause was written to remove, and would fail CREED's letter for a reason that has nothing to
do with its quality. Making SL-4 yield to SL-5(e) would waive the producibility check that cost BOND four
registrations — the standard's single most load-bearing rail. **Neither clause should yield, because each is
right about its own subject.** The merge was the error.

★ **This is the same repair I made in `read_cap_check` this session, one layer up:** a single verdict channel
was carrying two findings of different kinds, so consumers had to guess which one fired. There the fix was to
type the finding; here it is to split the leg. `finding_status_token_membership_test_desupervises_improved_
rows` — separate the fact from the label.

---

## 4. DOES THIS CHANGE WHAT MAY BE REGISTERED AGAINST A CAPITAL GATE?

The row instructs me to escalate to Will **only** if it does, and to say explicitly either way. Two parts:

**(i) TODAY — NO. VERIFIED, not inferred.** Scanned `PROME/GATES.tsv`: **zero CREED rows**, and no gate cites
a letter carrying an UNVERIFIED production attestation. `CREED-T-01a` lives in CREED's own registry and its
August print was graded **NOT FIRED at exactly `12.00`** — a grading that held on a pre-registration frozen
2026-08-27, not on anything this ruling touches. **No live capital gate moves.**

**(ii) PROSPECTIVELY — YES, ONE STEP, AND I AM NOT RULING IT.** Against a *strict* reading of SL-4, CREED's
Trepp letter would have failed registration; under SL-4(b) it registers with `production UNVERIFIED`. That is
a real widening relative to the strict reading. **The question SL-4 never addressed — and which I decline to
settle unilaterally — is whether an UNVERIFIED-production letter may then be CITED against a capital gate.**

⛔ I am deliberately not ruling it, for a reason, not out of caution: SL-5(e) already permits registration
with `realisation UNKNOWN` and places **no** gate restriction on the result. Adding one to SL-4(b) alone
would make the two clauses asymmetric in a way a desk would read as arbitrary — and I would be legislating a
gate-eligibility concept that exists nowhere in this standard today.

**→ WILL / PROME, the one question:** should a spec letter carrying `production UNVERIFIED` (or
`realisation UNKNOWN`) be **registrable but not gate-citable** until its attestation lands?
**My recommendation: YES, and applied to BOTH clauses symmetrically, as a separate amendment.** A letter may
be recorded and reviewed on a named-but-unmade query; a capital action should not rest on one. ⚠️ But that is
a *capital* rule, not an authoring rule, and this standard governs authoring — so it is Will's call, not
mine, and it should probably live wherever gate eligibility is owned rather than here.

---

## 5. CARRIED WITH THE ROW, AND NOT FIXED TODAY — SL-5 IS 39% OF ITS FILE

L348 carries a second item, same owner, same date: **SL-5 is now 39% of `SPEC_LETTER_STANDARD.md` and 1.6× SL-1
through SL-4 combined**, in my own words *"every honest caveat I added made the rule less likely to be read."*
**A standard nobody finishes is not a standard.**

⛔ **NOT FIXED TODAY, AND SAYING SO RATHER THAN TOUCHING IT.** Two reasons, both binding:

1. **This ruling ADDS text to the file** (the SL-4 split). Compressing SL-5 in the same pass would put an
   expansion and a contraction in one diff, and PAT-161's measured lesson is that a tightening pass over
   settled prose **reliably adds bytes** (+242 B, +451 B, +584 B on three real attempts). The remedy for SL-5
   is **MOVING text out** — its instance narratives belong in a record, leaving the rule — and that is a
   restructure, which under WQ-178 earns its own plan read.
2. **The two-correction stop.** This file takes one edit today. A second, in the same session, on the same
   file, would need an independent cold read first — and a byte count does not earn one.

**Owed, dated: the SL-5 instance-narrative rotation at the 9/18 WQ-171 ③ sitting**, where a
receipt-lifecycle blueprint is already on the board and the rule/record split is the same move.

---

## 6. THE ONE CANON EDIT (transplanted once, verbatim, into SL-4)

See `AGENTS/DAEDALUS/BLUEPRINTS/SPEC_LETTER_STANDARD.md` SL-4 — *The rule:* paragraph, this commit.
