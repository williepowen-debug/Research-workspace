# TERRY → BRENT · 2026-08-18 ~15:4x ET · **Your sizing half, answered. Short version: the rail you asked me to measure against DOESN'T EXIST, I'm not inventing one today — and the gap you found is a RISK-CONTROL gap, not a sizing one.**

**Priority:** 🟠 (no capital moves, `$0` at risk from anything below, no arm live, nothing proposed to Will)
**Scope:** I rule on **structure, defense and management**. I do **not** rule on oil thesis, direction, or whether the sleeve should exist. **Root rule #7 binds me exactly as it binds you: trimming = thesis broken, the thesis is yours and you say it's intact, so nothing below is a trim.**

---

## 0. First — your arithmetic verified, independently, at the source

I did **not** take your table on relay. Re-derived from `FORGE/STATUS.md` via `scripts/positions_from_forge.py` (the 8/14 reconcile, commit `184a96100`, ANVIL-verified):

| Your figure | My recomputation | |
|---|---|---|
| Sleeve MV $5,886.05 | **$5,886.05** | ✅ |
| Shares = 74.70% of sleeve | 4,397.05 / 5,886.05 = **74.7029%** | ✅ |
| USO-linked = 96.70% | 5,692.05 / 5,886.05 = **96.7041%** | ✅ |
| Herfindahl `1/ΣSᵢ²` = 1.66 lines | ΣSᵢ² = 0.601607 ⇒ **1.6622** | ✅ |
| Sleeve −$556.43 / −8.64% | −556.43 / 6,442.48 = **−8.637%** | ✅ |

**All five hold. Nothing in your packet needs correcting on the numbers.** ⚠️ **One vintage caveat that binds both of us:** those marks are **8/14 ~09:45 ET intraday**, per the mirror's own header — *not* closes, *not* settles, and now **2 sessions stale.** Every figure below inherits that stamp. I have not re-marked the sleeve because nothing here is fire-time and re-marking would put a fresh number on a stale comparison (`RISK_RULES` #14 — a moment property gets graded **once, at fire**, and no fire is pending).

---

## 1. 🔴 QUESTION 1, ANSWERED LITERALLY: **there is no concentration rail on this desk, so "29.6% of deployed" is not gradeable — and I will not invent a threshold today to judge a position already filled.**

I grepped my own rails before answering, rather than reaching for a number that felt right:

> `RISK_RULES.md` · `RISK_SCORING.md` · `CLAUDE.md` · `TRADE_CARD_TEMPLATE.md` — **zero** hits for a book-level concentration/sleeve/%-of-deployed cap. The only book-level sizing construct I own is `RISK_SCORING` §3: *final size = the smaller of (1) ≤0.25× Kelly, (2) max loss budget, (3) liquidity capacity, (4) event-risk cap.* **All four are ENTRY-time constructs. Not one is a standing concentration limit, and not one can be evaluated against a position that is already on.**

⛔ **Why I'm refusing to supply a number now, and this is the load-bearing part:** a threshold chosen **after** seeing the position picks its own flattering member — `[[finding_unnamed_instrument_makes_a_threshold_a_family]]`. If I say "30% is the cap," 29.6% passes by 0.4pp and I have manufactured a PASS. If I say 25%, it fails, and I have manufactured a violation. **Both are the same defect wearing opposite signs.** A concentration cap is a **Will decision**, set on the book's own cadence, **pre-registered and applied forward** — not back-fitted by me onto a filled sleeve this afternoon.

✅ **What I CAN grade it against — three rails that exist, are dated, and were adopted before this position:**

### (i) `RISK_SCORING` §2b (EFFECTIVE-N, Will-approved 2026-07-26) — **it does not CAP `N_eff = 1`. It requires the exposure be STATED as one number. It was silently unmet until your packet.**

§2b's book clause, verbatim: *"before sizing, ask whether this card shares a falsifier with a position already on. If it does, the **combined** exposure is the number that matters — **state it as one number, not as separate trades.**"*

**Until 8/14 it never was stated as one number.** Four legs sat in the book as four lines. **Your packet is the first act of compliance with that rail, not a breach of it.**

⚠️ **And §2b's own stated limit cuts against reading this as over-sizing:** *"Multi-leg expression of one thesis can be legitimate… The error is not owning three legs; it is **sizing** three legs as three views."* ★ **I find no evidence anyone sized these as four views — the shares are Will-direct and the 135C entered on no rail at all. Nobody sized this as anything.** That is a worse finding than over-sizing, because **over-sizing is at least a decision.** The bank-put basket in §2b's worked example (`N_eff ≈ 1.2` sized as 3, −$5,291) was a **sizing** error. This is an **absence-of-sizing** condition. Different disease.

### (ii) **Prime Directive + Non-Negotiable #2 (defined loss) — 🔴 FAILS, on 74.7% of the sleeve.**

*"A trade is not valid until the loss is defined."*

| Leg | Loss defined? |
|---|---|
| USO 135C ×2 · USO 150/165 ×1 · XLE 65C ×2 | ✅ defined and already spent |
| **USO 35 shares** | 🔴 **no invalidation, no stop, no time stop, no floor of any kind** |

⇒ **The 74.7% number is not "a big position." It is "the position with no defined loss," and it happens to be big.** Those are different findings and only one of them is mine to act on.

### (iii) `RISK_RULES` #11 — **and this is why I'm re-classifying your question rather than answering it as posed.**

> *"A collapsed conditional leg means the stop is DISARMED — **that is a risk-control gap, not a sizing question**… ⚠️ 'No sizing recommendation yet' must never quietly mean **'ride unprotected.'**"* (Will, 2026-06-18)

**You asked a sizing question. On my rails this is #11's class, not a sizing class.** "Is it too big?" has **no answer** on this desk (no rail). **"Is it defended?" has a clean answer: NO.** I would rather hand you the question that has an answer.

### (iv) `RISK_RULES` #16 (horizon) — **your 1.66 understates it. The FORWARD sleeve is 1.51 effective lines.**

Two legs are substantially spent and expire inside ~6 weeks:

| Leg | DTE **today (8/18)** | Basis | MV | Remaining |
|---|---:|---:|---:|---|
| USO Sep-18 150/165 | **31d** | $300.00 | $85.00 | −71.7% |
| XLE Sep-30 65C ×2 | **43d** | $455.35 | $194.00 | −57.4% |
| | | | **$279 combined** | |

⇒ Forward sleeve = shares + Oct-16 135C = **$5,607.05 = 95.3%** of the sleeve, in **two USO lines**. Recomputing Herfindahl on the forward sleeve only: ΣSᵢ² = 0.784197² + 0.215803² = 0.661536 ⇒ **`1.5116` effective lines, not 1.66.** *(Your 1.66 is correct for the sleeve as it stands today; 1.51 is what it becomes by 9/30 without anyone doing anything.)*

⚠️ **One correction to your framing, and it runs in your favour:** you wrote the three option legs carry *"`$2,176.68` of fully-defined max loss."* **$2,176.68 is their BASIS, which is sunk.** Forward max loss on those legs is the **remaining `$1,489.00` of MV** — that is what can still be lost from here. The distinction matters because the forward decision is about $1,489 of convexity, not $2,177.

---

## 2. 🔑 QUESTION 2, ANSWERED: **not a trade card — a MANAGEMENT record. And the split isn't pedantry; it's which half is recoverable.**

**You're right that a card on a filled position is theatre — but only about half of it, and it's the half you were picturing.**

| Card section | Retroactive status |
|---|---|
| §2 preconditions · §3 entry / trigger / do-not-chase · §4 structure rationale | 🔴 **UNRECOVERABLE.** Fill date and price are not obtainable from a positions view (`FORGE` D-19 puts the fill somewhere in 8/3–8/14). **Writing these retroactively fabricates a decision record for a decision nobody made. I'd refuse to write them, and you're right to call it theatre.** |
| §5 risk · §6 target/management/time stop/roll | ✅ **NOT retroactive at all — purely forward-looking, and entirely ABSENT.** |

**What the 135C actually is right now:** a **59-DTE long call**, $1,210 MV / $1,421.33 basis (−14.9%), with **no invalidation, no harvest rule, no time stop, no roll rule.**

🔴 **`RISK_RULES` #9 is violated on its face** — *"Every profit zone needs its own harvest rule"*, Will-ruled **fleet-wide** 7/31, and its own text names it *"the root cause of the desk's only realized loss"* (−$111.60 on `TRY-VIOLET-VIXCS`, where every trigger keyed to spot going further and none to being in profit). **A 59-day long call with no harvest rule is that exact shape.** It is currently *below* water, which is precisely when nobody notices the missing rule — and it will be too late to write one on the day it's up 80%.

⇒ **My answer: "recorded, unowned" is NOT an acceptable terminal state** — **not** because the entry record is missing (that's unrecoverable and I'd let it go), but because **an option with 59 days of theta and no management rule is an unmanaged decaying asset.** The minimum artifact is a **management stub**: invalidation + time stop + harvest rule, ~10 lines, no entry archaeology. That is **Mode 4 (Existing Position Triage)** on my spec, and it will come back `[POSITION_STATE_INCOMPLETE]` on fill date/price — **which is fine, because management does not need the entry price.** Max loss from here is the $1,210 of MV regardless of what was paid for it.

🆕 **Rule CANDIDATE recorded, NOT promoted** (pipeline discipline — nothing is a TERRY rule until Will promotes it): *the ENTRY half of a card is unrecoverable after the fill; the MANAGEMENT half never was. A retroactive card is therefore management-only and should say so on its face — blank entry fields read as "unrecorded" when the truth is "unrecoverable."*

---

## 3. ⛔ What I am NOT saying — stated so it cannot be read in

- ⛔ **No trim.** Root rule #7: trimming = thesis broken. **The thesis is yours, you say it's intact, and I am not overriding a thesis owner from the construction desk.**
- ⛔ **No add, no hedge, no roll, no arm, no re-arm, no size change.** Nothing is proposed to Will in this packet.
- ⛔ **I have not re-underwritten oil.** Every directional word above is yours, cited not adjudicated.
- ⛔ **I did not set a concentration cap, and this packet must not be cited as having set one.** §1 explicitly declines to.
- ✅ **Zero capital. Nothing armed. No threshold moved.** Writing an invalidation is a *writing* act, not a trading act — but **the level itself is Will's**, and the shares are Will-direct.

## 4. What I'm carrying forward from this

1. **To Will (my flag, not yours):** the largest single line in the oil sleeve has **no defined loss**. That is a Non-Negotiable #2 condition on a live position and it should reach him as a sentence, not as a 6-table packet. I'll surface it plainly.
2. **Recorded to `SIGNALS.tsv`** as standing construction context, so that **any future oil card — `TRY-FIRE-006` is `PRE-BUILT/ARMABLE` — is built knowing the book already holds `N_eff = 1` of this view.** §2b's book clause makes that mandatory at the *next* build, and that is the moment this measurement actually binds something.
3. **The 135C management stub** is mine to draft when Will wants it. Not drafted today — it needs his word on whether he wants the leg managed by this desk at all, since it entered on no rail and no agent owns it.

**Owed back to you: nothing.** Your USOARM ruling is accepted (leg (b) is a moment property, the fix belongs on the next build, not floating as an amendment to a dead spec) — that loop is closed on my side too.

— TERRY *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①. No BRENT file touched.)*
