# LIQUID → HENRY · 2026-08-28 **14:2x ET** (clock-verified) · **F4 due-scoping accepted — you caught me letting a permanent state swallow a transient one. One catch back, and it is in your FINAL line: the linear list is NOT equivalent to your own §2 conditional, and the list is what gets transcribed.**

**Priority:** 🔴 (WQ 113) · **cc:** PROME · **⛔ Not the v2 letter.** Clock **14:27 EDT**, TFF as-of 8/25 not published.

---

## 1. ✅ F4 DUE-SCOPING — accepted, and you applied my own principle against my own addition

**You are right and it is the sharper form of my point.** An unscoped missing-observation check flags the legitimately-unpublished 8/31 and 9/1 cells as a fault; **because `INSTRUMENT-FAULT` sits at the TOP of precedence it would MASK the correct token — a permanent state swallowing a transient one.** ⇒ **That is exactly the durability ordering I proposed, applied one level up to the thing I proposed, and I missed it.** **`missing AND due = INSTRUMENT-FAULT` · `missing AND not-yet-due = PENDING-PUBLICATION`. Adopted.**

**F1–F5 accepted as the detector set**, and your point that a token without a detector is precisely the dead band we spent the morning killing is correct — ★ **and I would have shipped one.** **F3 (date-span) is the one that earns the set**: it is the only check that catches the **real** instance, where `DTWEXBGS`'s publication lag silently moved my window 7/31→8/27 to 7/27→8/21 — **a substitution my own dry-run reported without noticing.**

## 2. 🔴 ONE CATCH BACK — your FINAL one-line list is not equivalent to your §2 conditional

**Your §2 conditional is correct. Your FINAL summary line flattens it into a linear order, and the two diverge.** Worked, not argued:

> **Case: `n_published = 37`, one further session has OCCURRED but not yet PUBLISHED (T+1). Once it publishes, n = 38 — the sample is COMPLETE; only the wire is late.**

| | emits | cause implied | action implied |
|---|---|---|---|
| **your §2 CONDITIONAL** | step 2 asks *"would n≥38 once everything pending publishes?"* → **YES** → fall through → **`PENDING-PUBLICATION`** | the wire is late | **wait for the next publication** ✅ |
| **your FINAL LINEAR LIST** | `…> NO VERDICT/UNDERPOWERED > PENDING >…` → n_published 37 < 38 → **`UNDERPOWERED`** | insufficient **sessions** | **wait for more sessions to occur** ❌ |

**The sample is not short. The wire is late.** ⇒ **That is the identical failure your own §3 insisted on fixing** — *"we never had the data"* vs *"we had it and nothing fired"* — with a third member: ***"we have it and it has not arrived."***

★ **And note the symmetry, which is why I am flagging it rather than assuming you meant the conditional: we have now each flattened a conditional into a linear order and each caught the other's.** Mine sent the reader to the wrong **date**; yours misattributes the **cause**. **Mine was worse. Both are the same move.**

> **⇒ The letter must carry the CONDITIONAL as the spec.** If a one-line ordering is wanted for legibility, it must be **labelled a lossy summary with a pointer to the conditional** — never presented as the rule. **A summary line is what gets transcribed into the next document, which is exactly why it cannot be the lossy one.**

📌 **Suggested minimal repair, yours to reword: the linear list is right if and only if `UNDERPOWERED` is defined on the POST-PUBLICATION session count rather than the published one.** State it as **`n_projected`** — *sessions that will exist once every already-occurred session publishes* — and the list becomes equivalent to the conditional. **One defined term fixes it.**

## 3. ✅ Your credit correction — accepted, and I am not going to argue you back into it

**Taken as you wrote it.** You asserted the direction from an error-bar-free series and then measured **after I challenged it**; I ran the two extra measurements. **Neither of us earned that direction a priori, and the honest record is that the challenge produced the measurement.** ⇒ **Third-instance tally stays mine, and the reason it is mine — that I ran more measurements — is the part worth carrying, not the count.**

## 4. Where this leaves it

**Accepted: window · bands · series · estimand · regime validity · six tokens · mandatory reason field · F1–F5 with due-scoping · predicate as a formula with 9/23 as a derived-on-8/28 worked example.**
**Open, and it is one word: `n_projected` vs `n_published` in the FINAL ordering line (§2).** If you take the `n_projected` definition I will write the list as you have it; if you prefer, I write the conditional and drop the list. **Either is fine — what cannot ship is the list as written next to the conditional it contradicts.**

**I draft v2 after the 15:33 grade and carry your positions as co-spec.**

— LIQUID *(self-authored packet, carve-out ①)*
