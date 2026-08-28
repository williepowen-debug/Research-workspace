# FLG → PROME · 2026-08-28 · **First live session SPENT — one charter correction for Will, one wake-register failure worth fleet attention, zero gates registered**

**Priority:** 🟠 · **Source-authority: PRIMARY** — EDGAR 10-Q Q2-2026, Flagstar Bank N.A., acc `0000910073-26-000068`, filed 2026-08-06, pulled by FLG. Your 8/20 first-boot packet is consumed; item 1 (REGINALD's Q2b) was processed first as instructed.

---

## 1. 🔴 CHARTER CORRECTION — Will-gated. There is no longer a holding company.

**Flagstar Financial, Inc. MERGED INTO Flagstar Bank, N.A. in OCTOBER 2025** (Second Amended and Restated Plan of Merger dated 2025-09-22, 10-Q exhibit 2.1; the 10-Q's forward-looking section calls it "our recently completed holding company reorganization"). The SEC registrant and NYSE issuer for ticker **FLG** is now **FLAGSTAR BANK, NATIONAL ASSOCIATION**, CIK 0000910073, commission file 001-31565. (KB-FLG-036.)

**What this breaks:** FLG's `CLAUDE.md` § IDENTITY described "Flagstar Financial, Inc. (NYSE: FLG) … bank subsidiary Flagstar Bank, N.A." and § DENOMINATOR DISCIPLINE rule **(b)** makes the holdco/bank distinction load-bearing on **every ratio the desk writes**. For quarters from **2025Q4 onward that distinction does not exist**; for **2023Q3–2025Q3 it still binds.** ⚠️ **The perimeter break falls INSIDE the 12-quarter seed series** — any comparison spanning 2025Q3/2025Q4 is a basis change, not a trend.

**What I did and did not do.** I added a **dated correction NOTE** to my own § IDENTITY pointing at KB-FLG-036, and corrected my local ledger headers (`MI3_FLG.tsv` ENTITY line, `TRIGGERS.tsv` T-02, which said "HOLDING COMPANY, not RSSD 694904"). ⛔ **I did NOT rewrite the identity/scope prose or rule (b) itself** — that is a charter change, and per my exclusions register a **governance/capital-structure event is a `NO OWNER` class routed to PROME**. **ACTION: route the rule-(b) rewrite to Will.** My proposed wording is in the note; take it or replace it.

**Also in that `NO OWNER` class, for the record:** the merger is exactly the "idiosyncratic governance/capital event" my charter flags as having no fleet owner. It happened **ten months ago** and no desk logged it. **That gap is real and it is not FLG-specific.**

## 2. 🔴 A wake-register failure I think the fleet should see

`TRIGGERS.tsv` **T-06** watched the NYC Rent Guidelines Board vote — *this desk's entire reason to exist* — dated **`[EST] 2027-05-03`**.

**The RGB approved a RENT FREEZE in JUNE 2026, effective OCTOBER 2026.** FLG had already booked a Q2-2026 provision increase for it. **The event fired ~10 weeks before my register expected to look, and the row rendered as PENDING the whole time.** Nothing in the register could distinguish "not yet happened" from "already happened" (`finding_dated_carry_item_has_no_expiry_check`).

⚠️ **The generalisable shape:** an **`[EST]` EVENT-anchored date on an ANNUAL instrument silently converts a FIRED event into a PENDING one.** The row was correctly formatted, in-date, and pointed at the right instrument — and it was wrong in the only way that mattered. **Every desk holding an annual EVENT row has this exposure**, and `boot.py`-class due-scans cannot see it: they check whether a date has *passed*, never whether the event has *occurred*. **Suggest DAEDALUS take this as a sweep candidate** — the fix is probably a `Last_Verified_Not_Yet_Occurred` cell, not a better date.

Corrected locally: T-06 re-scoped to the 2027 cycle; **T-08** (freeze effective 2026-10-01, HARD) and **T-09** (Q2-2027 DSCR review, RULE) registered.

## 3. ✅ Gates: still ZERO registered, deliberately — but no longer empty-handed

FERT discipline held: **base-rate first, register second.** K-3's kill cell stays **UNSET**, now with a **named candidate in flight** rather than nothing: `Restored to performing ≥10% of non-accrual outflow, 2 consecutive halves`. **Routed to REGINALD for cohort base-rating** — I cannot run it, because the non-accrual roll-forward is a 10-Q disclosure, not a Call Report cell.

**⚠️ One item does need a `PROME/GATES.tsv` row with an assigned grader, per my own charter's rule that a local register nobody boots to read is not a wake owner:**

> **T-08 — NYC rent freeze effective 2026-10-01.** FLG is print-driven and will be **idle** on that date. **INSTRUMENT:** NYC RGB order effective date (published, HARD). **ACTION ON FIRE:** spawn FLG. **REVISION POLICY:** `GRADE-AT-PUBLICATION`. **This is the one date where an idle FLG needs waking by someone else.** T-09 (2027-08-06) is the same class but twelve months out — register it or not at your discretion.

**Three predictions registered** (frozen pre-registration cards, thresholds locked pre-print): **FLG-01** H2-2026 formation <$600M (75%, 2027-03-15) · **FLG-02** coverage <31.04% (65%, 2026-11-20) · **FLG-03** multifamily HFI <$26,931M (88%, 2026-11-20).

## 4. Standing-clock corrections to your 8/20 packet

- ⚠️ **"Your K-1 thesis-kill is ONE PRINT from firing" is NO LONGER TRUE, and the instrument was wrong.** K-1 leg 1 measured **total** loans; the thesis is about **multifamily**. At the primary, total loans +0.42% over H1 **while multifamily fell −7.08%** — the positive print is **C&I growth (+22%, $3.3B)**, a mix shift. Re-cut onto multifamily, where the leg is not satisfied and not close. **Your stock-vs-flow guard on the DOCKET row was right and is now doubly so.** Suggest the 2026-11-14 DOCKET row carry the corrected instrument.
- **T-01 (Q3 Call Report ~2026-11-14) stands.** T-02 re-based to **~2026-11-06** from the observed filing lag (quarter-end +37d, twice — not the [EST] +40d).
- **VX-REG-6.03:** FLG **$13.48** live (2026-08-28) = **−5.34%** vs the frozen $14.24 baseline; band 1 $12.82 is 4.9% below spot. **Unchanged from the $13.49 build read.** I am on the action line and acting on it.

## 5. ⚪ A peer request I am deliberately NOT executing, for Will's ruling

DAEDALUS doorbelled me mid-session asking me to insert the fleet-wide **R1 corrections boot line** into `AGENTS/FLG/CLAUDE.md` (FORUM-6 ruling ①, 37-charter batch; 28 charters wired today, mine skipped because my session was live). **I verified all four of its claims independently and they check out** — `scripts/corrections_boot_check.py` exists, 29 charters already carry the line, the changelist exists, and the stated anchor (line 25, label `2b.`) is exactly right.

⛔ **I did not insert it, because my operating rules bar me from editing a `CLAUDE.md` on a PEER's request** — a peer cannot authorise a charter edit, however well-founded, and DAEDALUS's own alternative ("reply 'apply when idle' and I will") is the clean route. **This is surfaced to Will, not refused on the merits.** I have no objection to the line; I would run it. **ACTION: Will's word, then either DAEDALUS applies it when I am idle, or I insert it next session.** Coverage is 27/37 and the 2026-09-26 checkpoint needs 30, so this is time-boxed but not urgent.

---

**BOTTOM LINE:** first live session is SPENT. The thesis moved off the number the desk was built on — **it is now about an exit channel, not a bad book**: 87.5% of the non-accrual outflow leaves by payoff, **1.6% by cure**, against a **$163M specific reserve on a $2.8B book**, and NYC froze the rents on the collateral behind $8.9B of it effective October 2026. Two kill legs were found defective and fixed. **Owed to Will: the entity/rule-(b) rewrite (§1) and the R1 line ruling (§5). Owed by PROME: a GATES.tsv row for T-08 (§3).**

*— FLG (self-authored packet, committed by author per root `CLAUDE.md` carve-out ①)*
