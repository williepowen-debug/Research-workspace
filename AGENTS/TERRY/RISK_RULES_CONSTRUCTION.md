# TERRY RISK RULES — CONSTRUCTION (rules 14–23, full text)

**Cold register of the `RISK_RULES.md` hot/cold split, 2026-09-03 (read-cap remedy, Will-approved).** ⛔ **NOT an archive and NOT frozen — every rule here is LIVE, numbered, and cited by number.** `RISK_RULES.md` carries the hot index; this file carries the full text and the worked cases that make each rule stick.

**Read this file WHOLE before producing any actionable trade card** (`CLAUDE.md` BOOT step 7), and on demand whenever one of the index's *binds-at* triggers fires. Split content: `21,602 B`, crc32 `29a92fa2` at the split.

⚠️ **RE-TRIGGER (READ_CAP rule 7 — a remedy names its own, and never makes a leanness claim): re-measure BOTH halves at any append to either, or on 2026-12-03, whichever comes first.** `scripts/read_cap_check.py --agent TERRY` is the instrument. This file is on the reading path at build time, so it is NOT exempt from the cap — it is simply not read at boot.

---

### Gates & grading cadence

14. **★ SEPARATE A STRUCTURE PROPERTY FROM A MOMENT PROPERTY, AND GRADE EACH ON ITS OWN CLOCK.**

    | | Examples | When to grade |
    |---|---|---|
    | **Structure property** — a fact about the trade | strike exists in the expiry · two-sided quotes / OI · quote sanity (no `LOCK`/`XSD`/`DEAD`/`NOBID`) · moneyness band · tenor in spec · max loss | **any time.** Stable. |
    | **Moment property** — a fact about *now* | net debit · debit as % of width · IV · spread% · mark · R:R at the current price | **ONCE, at fire.** |

    **On a multi-leg `AND` gate whose legs resolve at different times, the early leg is assessed for READINESS before fire, and its VALUE is graded once — at the moment the last leg resolves.** A moment-property grade published before the gate can fire has **no decision content** (nothing can be actioned either way) and **real cost** (it lands on N surfaces × M revisions and manufactures drift).

    🔴 **The incident, 2026-08-04.** `TRY-BRENT-USOARM` leg (b) — net debit ≤33.0% of width — was graded **five times in one morning by three agents** while leg (a) could not resolve until the ~~16:15~~ **16:00** close: **27.0 → 34.0 → 38.0 → 26.0 → 31.0**, i.e. **two FAILs and three PASSes on the same structure** *(against the ≤33.0 line: 27.0 PASS · 34.0 FAIL · 38.0 FAIL · 26.0 PASS · 31.0 PASS).* ⚠️ **CORRECTED 2026-08-07** — this read *"three FAILs and two PASSes"* from the day it was written until a **Will-directed review caught it 8/6** by doing the arithmetic nobody else had. **The values were always right; the tally was always wrong**, and it sat inside the rule about grading discipline. ★ **The rule's force is unchanged and arguably sharper: the sequence still flips verdict THREE times, and the point was never the ratio — it was that every grade was correct at its timestamp and not one was actionable.** *(BRENT's 8/5 paraphrase — "graded 5× with **four verdicts**" — inherited the same confusion and is impossible on its own terms: a PASS/FAIL test has exactly two verdicts. Correction routed to BRENT.)* ★ **Had anyone acted on PROME's 11:38 read of `38.0% FAIL and worsening`, the arm would have been stood down on a number that was `26.0%` forty-six minutes later.** Nothing was mis-measured — every grade was correct *at its timestamp*. **The defect was treating a moment property as though it were a property of the trade.**

    **Corollaries:**
    - **A moment-property number is never quoted without its timestamp.** "Leg (b) = 26.0%" is not a fact about the trade; "26.0% on the 12:24 chain" is.
    - **Do not chase it.** If the number moves after you have recorded it, that is the number behaving normally — **re-writing the card to the newest print is the very behaviour that caused the drift.**
    - **A gate spec that tests a moment property must name its measurement moment** (this one does: *"live chain **at fill**"*). If it does not, that is a spec defect to route to its owner, not to resolve by picking a moment.
    - **Empirical half-life at this desk: ~40 minutes.** Leg (b) moved **5.0pp in 37 minutes** on 8/4. Budget accordingly — and see 6b, because a stamp error of ~1h can exceed a figure's entire useful life.

15. **⚠️ A GATE THAT OPENS ON VOL/PRICE DECAY CARRIES *ZERO* THESIS INFORMATION — AND WILL FEEL LIKE CONFIRMATION.** When an entry gate's trigger variable is *"the market has priced less of our thesis"* (vol decayed from peak, premium cheapened), the gate opens **precisely as conviction drains**, by construction. That is a legitimate and deliberate fade-the-consensus design — **but "the gate fired" is then, mechanically, a measure of the market disagreeing with the thesis owner more than it did yesterday.** ⛔ **Never let a gate firing be read as evidence the thesis is working, and say so on the card before it fires** — the pull to read it that way arrives exactly when capital is about to move. *(8/4: USO leg (a)'s cushion widened 2.5% → 7.3% on the same morning BRENT cut his own dip confidence 88% → 85%. Those two move together by construction; one is not corroboration of the other.)*

16. **★ MATCH THE EXPIRY TO THE VIEW'S HORIZON. A STRUCTURAL VIEW IN A SAME-DAY INSTRUMENT IS A DIFFERENT TRADE, AND A FAR WORSE ONE.** In 0–1 DTE options **being early is being wrong** — the instrument makes *timing* the entire trade, so a thesis about the next three weeks cannot survive inside it no matter how right it eventually is. **Before choosing tenor, say out loud how long the view needs to work; if the expiry is shorter than that, the expression is wrong even when the view is right.**

    🔴 **The worked example, and it is this desk's most expensive lesson to date.** The same QQQ view existed in the book twice in July–August 2026:

    | Expression | Max loss | Outcome |
    |---|---|---|
    | `TRY-WILL-QQQ-VFADE` — **Aug-21** put spread, defined risk, kill line pre-registered at 712 | **$452** | **never fired — $0** |
    | 11 tickets at **0–1 DTE**, undefined frequency | uncapped by count | **≈ −$4,341** |

    **The swing card would ALSO have lost** — it died on its own 712 invalidation. **It would have lost $452 on a level named in advance. Same view, same wrongness, 9.6× the cost, entirely from tenor and frequency.** The correct expression was built and sitting unfired while the incorrect one ran eleven times. → `POSTMORTEMS.md` 2026-08-04.

    **Corollary — ⛔ A CONTROL THAT HAS NEVER FIRED NEEDS ITS *FORM* CHANGED, NOT ITS WORDING.** That cluster's hard stop was specified in **four consecutive reviews and executed zero times**, re-written each time instead of re-shaped. **Count the executions, not the specifications.** At zero, replace the manual act with something that executes itself — a resting order, or a structure whose max loss *is* the premium. *(This is the same failure as `NO_HARVEST_RULE` #9, pointed at the loss side: a management spec that only works if someone overrides conviction in the moment does not work.)*

17. **★ THE SIZE-INCREASING BRANCH CARRIES THE HIGHER EVIDENTIAL BURDEN — fleet rule N4, Will-ratified 2026-08-11, consumed 2026-08-13 (PROME forum-4 close packet).** In a claim class whose **sole consumer is a size decision**, the branch that INCREASES size must clear a higher bar than the branch that DECREASES it — **and the spec must show the asymmetry in its own numbers**, not assert it in prose. *(The worked instance is the reason the rule exists: BRENT's crude "FUEL SPENT" fuller-size branch rested on an OI-normalized margin of **477–483 contracts (~5% of a median week), not the 1,512 its label implied** — 68% of the clearance was a denominator artifact — at the **67th percentile** of short-crowding, base rates **1.9:1 against** the claim surviving. Consumption details incl. 35a non-latching revert + 35b band death after its final 8/14 grade → `SIGNALS.tsv` row `FORUM4-35AB-FUELSPENT`.)*

18. **★ A PRINT NEVER JUSTIFIES A DEEP-OTM STRIKE — MATCH THE STRIKE TO THE EVENT'S REALIZED ENVELOPE, OR TAKE THE TENOR PAST THE PRINT.** *(Promoted from `options/IV_CRUSH_PARTB_2026-08-13.md`, Will-approved 2026-08-13 — the `options/` pipeline's first promotion to a numbered rule.)* Measured, not asserted: regional-bank singles (WAL/OZK/HBAN/ZION), 32 prints Oct-24→Jul-26 — realized 1-day reaction-session moves run **median ~2–3%, max 9.7%, 0 of 32 ≥10%**, while the July book held **12.7–15.5% OTM** strikes through prints. **A single ordinary print cannot reach a >10%-OTM strike on these names.**

    - **(a)** A strike **>10% OTM may not cite an upcoming print as its catalyst** — the print cannot pay it. Its real catalyst is multi-quarter transmission, so its tenor must span quarters (#16's horizon test, now with the event's measured size).
    - **(b)** If the print IS the intended catalyst, the strike belongs **inside the realized envelope** (median 2–3%, p95 ≲9%) — and there the crush tax is real (Part A: the event premium concentrates **+10–16 vol pts in front-month deep-OTM strikes**), so prefer a **spread that SELLS the rich deep wing** rather than paying it.
    - **(c)** Size a print-spanning long option against its **post-print mark**, not its pre-print hope.
    - ⚠️ **Regime-conditional, and the rule says so:** the sample contains no crisis print — Mar-2023-class gaps (SVB/FRC; WAL ~−47% intraday 3/13/23) exceeded this envelope. Holding a deep strike through a print is a bet that **the regime break lands ON the scheduled date**; if that is genuinely the trade, write it on the card as that bet, in those words, and size it as a tail-timing lottery.
    - **Scope:** the numbers are name-class-specific (regional-bank singles). Before applying the 10% line to another sector, **re-measure the envelope** — the tool is re-runnable (`options/partb_realized_moves.py`).

    **First consumers:** `TRY-FIRE-002` and `TRY-FIRE-003` (PRINT-class, staged) at build time.

19. **★ A SERIES-DERIVED EXTREME, STREAK OR "HAS X EVER HAPPENED" CLAIM MUST STATE ITS BAR COUNT.** *(Will-approved 2026-08-18. Born from WALTER `SIG-W-20260813-002` + this desk's own reproduction the same day.)* **Coverage is a property of the PULL, not of the instrument, and it varies between two identical calls.**

    🔴 **The measurement, on this box:** two identical `price_history()` calls **seconds apart** returned `^TNX` with **18 bars, then 60** (`IEF`: 59, then 60) for the same 60-day request. ⚠️ **The short pull contains ZERO nulls — the bars are simply ABSENT — so a `close is None` test is blind to it BY CONSTRUCTION.** WALTER's original finding was the *nullity* variant; **absence is the same defect with the detector removed.**

    **Why it is a trading rule and not an infra note:** every stat downstream is an **extreme** or a **window mean**, and a hole corrupts both *silently* — `max`/`min` exclude the extreme, a range-location verdict inherits the wrong range, and an "N-day MA" spans more calendar days than its label. **Concretely: the full 60-bar 10Y series has min `4.37`; the truncated 18-bar window has min `4.60`. `TRY-FIRE-004`'s disarm is a 10Y close `<4.50`** — the short series answers *"has it been below 4.50?"* with a confident **NO**.

    - **(a)** Quote the bar count beside any extreme/streak/percentile: *"11th percentile **of a 120-day window**"*, never a bare percentile.
    - **(b)** ⭐ **THE BATCH IS ITS OWN CONTROL.** Comparing bar counts **across tickers in the same pull** needs **no holiday calendar and no per-symbol expectation** — it catches "one symbol came back short" directly. An absolute floor backstops single-ticker pulls.
    - **(c)** **A short/holed series gets its derived verdicts SUPPRESSED, never interpolated.** An unmarkable series is reported UNMARKED. *(Implemented: `snapshot.py` `coverage_flags()`; regression suite `scripts/test_snapshot_coverage.py`, 12 synthetic-defect assertions including the 18→60 reproduction and a false-positive guard.)*
    - **(d)** **Print coverage on EVERY run, not only on defect** — a check that speaks only on failure teaches the reader to read silence as health.
    - ⚠️ **Cross-window percentiles are NOT like-for-like.** Comparing your 120-day percentile to someone else's differently-windowed one is a basis error; state both windows or compare **levels** instead.

20. **★ THE ENTRY HALF OF A TRADE CARD IS UNRECOVERABLE AFTER THE FILL; THE MANAGEMENT HALF NEVER WAS. A RETROACTIVE WRITE-UP IS MANAGEMENT-ONLY, AND SAYS SO ON ITS FACE.** *(Will-approved 2026-08-18. Forced by `USO $135C Oct-16 ×2` — $1,421.33 basis, in the book on no rail, no card, no owner agent; fill date and price **unobtainable from a positions view**, `FORGE` D-19.)*

    | Card section | After the fill |
    |---|---|
    | preconditions · entry/trigger/do-not-chase · structure rationale | 🔴 **UNRECOVERABLE — do NOT reconstruct.** Writing them retroactively **fabricates a decision record for a decision nobody made.** |
    | risk · target/management · time stop · roll rule | ✅ **NOT retroactive at all — purely forward-looking, and usually ABSENT.** |

    - **(a)** **"Recorded, unowned" is NOT an acceptable terminal state for an option leg.** An option with live theta and no management rule is an **unmanaged decaying asset** — `RISK_RULES` #9 is violated on its face, and it is violated *quietly* while the leg is underwater, which is exactly when nobody looks.
    - **(b)** **Management does not need the entry price.** Max loss from here is the **remaining mark**, whatever was paid. ⚠️ **Do not let a missing fill price block writing the exit** — that is the trap this rule exists to break.
    - **(c)** **Leave the entry fields explicitly marked UNRECOVERABLE, not blank.** *Blank reads as "unrecorded" (someone should go find it); the truth is "unrecoverable" (nobody can).* Mark `[POSITION_STATE_INCOMPLETE]` with the reason.
    - **(d)** Sunk basis is **not** forward risk: state forward max loss as the **remaining mark**, never the original debit. *(8/18: the oil sleeve's three option legs carried `$2,176.68` of sunk basis but only `$1,489.00` of forward exposure.)*

21. **★ A TENOR BAND IS AN *ENTRY-ECONOMICS* TEST, SO IT GOVERNS NEW DEPLOYMENTS AND NOT ROLLS — AND "ROLL" MUST BE DEFINED NARROWLY OR THE BAND DIES BY RELABELLING.** *(Will-ruled 2026-08-21 ~16:3x ET on the `USO Oct-16 135C` pair; recorded by BRENT at `AGENTS/BRENT/TRADE.md § BINDING WILL RULINGS` and on his roll card. **Mirrored here 2026-08-23 at BRENT's explicit ask — the `RISK_RULES` mirror is TERRY's to write; BRENT correctly did not edit this file.** This is a **SCOPE ruling, not an exception** — it says what the band was always about, and it therefore applies to every tenor band on this desk, not just the USO one.)*

    **The ruling:** the **`60–90 DTE`** band governs **NEW STRUCTURAL DEPLOYMENTS.** It does **NOT** govern the **roll of an existing leg.**

    **Why scope and not exception:** the band exists so that a shorter-dated vertical cannot make **leg (b)** — the net-debit-as-%-of-width test — easier to satisfy. That is an **ENTRY-economics** test. **A roll is never leg-(b) gated**, so read for the purpose it was written for, the band was never about rolls at all. *(Precedent for scoping a tenor rule this way is this desk's own: #16's horizon test already distinguishes a structural horizon from an off-ramp one.)*

    ⛔⛔ **THE GUARD IS BINDING AND TRAVELS WITH THE RULE — a scope ruling is broader than an exception, so it needs a tighter definition, not a looser one:**
    > **"ROLL" = SAME underlying · SAME strike · LATER expiry. NOTHING ELSE.**
    > **ANY change of STRIKE or STRUCTURE is a NEW DEPLOYMENT and the tenor band BINDS IN FULL.**

    ⚠️ **Without that guard a genuine new deployment arrives wearing a roll's clothes and the only economic gate on the trade is gone by relabelling.** A "roll" that moves the strike is a **close plus an open**, and the open is gated.

    - **(a)** **Say which you are doing, in those words, before pricing it.** If the answer needs a paragraph, it is a new deployment.
    - **(b)** **The scope exemption is not a recommendation to roll.** A roll pays new capital to keep the same view for longer; it is still subject to **root rule #7** (roll duration, don't trim size) and to the horizon test in #16. *(8/21 worked case: the counter-argument for acting was theta — the leg was ~ATM, 100% extrinsic, decaying ~`$19.61`/day and accelerating. **That argues for CLOSING, never for rolling** — rolling would have paid `$750` to keep the same problem for longer, while the same session's SELL-ONE was a de-risk. **Two decisions pointing in opposite directions is itself the tell.**)*
    - **(c)** **A roll of a filled leg is still a Will-gated proposal.** Scope-exempt from the band ≠ pre-approved. `$0` moves without [Approve].

22. **★ A CONTINUOUS FRONT-MONTH TICKER (`XX=F`) IS SAFE FOR A LEVEL AND UNSAFE FOR A DELTA. NAME THE CONTRACT, OR STATE THE BASIS AND CHECK THE ROLL.** *(BRENT → TERRY 2026-08-20; adopted here 2026-08-23. **I am a first-party casualty: I quoted a `$99.14` diesel crack off exactly this method.** BRENT's own rule ID is `L23`; this is the TERRY mirror.)*

    **`=F` tickers ROLL.** When they do, the symbol silently stops meaning one contract and starts meaning the next — **so a difference taken across the roll measures the CALENDAR SPREAD, not the market.** ⛔ **The print is not wrong. It is an answer to a different question, and nothing in the output says so.**

    🔴 **The worked case, and the scale of it is the point.** On 2026-08-20 `CL`, `HO` and `RB` all rolled in the same session. The rolling-front method printed a **gasoline crack of −$10.71** — read across the fleet as a collapse in refining margin. **Nothing sold off:** `RBU26` closed **+1.4c**, `RBV26` **+3.5c**, `HOU26` **+3.2c**, `CLU26` **+$2.32** — every contract UP on the day. The Sep−Oct RBOB spread was **25.7c/gal = $10.79/bbl**, i.e. **within 8 cents of the entire reported "collapse."** It was the summer→winter RVP grade change.
    **And the same session's diesel read was wrong twice over:** on a consistent Sep-contract CLOSE basis the record is **8/18 at $101.96** (not Monday), and the give-back from the true peak is **−$1.77 over two sessions and DECELERATING** — not the *"−$5.08 and accelerating"* that reached this desk. That figure was **an intraday bar that did not hold to the close.**

    - **(a)** **For a LEVEL, `=F` is fine.** For a **DELTA, a spread, a crack, or any week-on-week / year-on-year comparison**, name the contract (`HOV26`, `CLU26`) or state the basis and verify no roll sits inside the window.
    - **(b)** **Danger dates are structural, not random:** every expiry, and especially **late Aug (RB Sep→Oct)** and **late Nov**. Verify a roll by **close-matching** the continuous series against the named contracts — don't assume the date.
    - **(c)** **A seasonal grade spread is not a signal in EITHER direction.** Sep gasoline $49.14 vs Oct $40.17 is ~$9/bbl of RVP spec, every year. **A comparison straddling that roll is meaningless bullishly and bearishly alike.**
    - **(d)** ⚠️ **Pairs with the intraday trap, because they compound.** BRENT logged the identical error four weeks earlier on the same instrument (a *"gasoline crack −$10.89 in one session"* that was an intraday read; the close was $58.25, not $49.90). **Same instrument, same trap, twice.** `[[finding_ohlc_verify_before_session_claims]]` · `[[finding_continuous_front_ticker_rolls_so_deltas_lie]]`
    - **(e)** **Nothing was retracted upstream and nothing should be:** the earlier signals were **correct on their own dates** — the roll had not happened yet. **This rule is forward-looking. A method finding is not a retraction.**


---


23. **★ NAME THE DRIVER BEFORE YOU ADD. PROFIT FROM A MECHANISM YOU DID NOT UNDERWRITE IS EVIDENCE *AGAINST* THE CARD, NOT FOR IT.** *(SAM → TERRY 2026-08-27, delivering the §6 branch owed since 8/7; the FXY thesis is the worked example, the rule is general. Recorded on `setups/FLOW-TRIGGER_carry-convexity-FXY-call-v2.md`.)*

    **This resolves a real ambiguity in ROOT RULE #7** (*"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."*). #7 assumes you know **which** mechanism moved the position. When the tape pays you and the card's own driver was **not** what paid, #7 gives no answer on its face — and the default reading is the flattering one.

    **The test, in one line:** *did the position move for the reason the card underwrote?*
    - **YES** ⇒ mechanism operating, timing wrong ⇒ **ROLL** (#7's "timeline uncertain" branch).
    - **NO** ⇒ **thesis-broken ON THAT AXIS ⇒ TRIM** — *even if the move was profitable, and especially then.*

    ⛔ **THE TRAP, AND IT IS THE WHOLE POINT: an un-underwritten driver that PAYS reads as vindication and invites adding.** It is the opposite. **Being paid by a mechanism you did not underwrite means your edge was not what you thought it was** — the P&L is evidence about the *tape*, not about the *card*. **A winner is the hardest position to audit and the one this rule exists for.** *(`[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` — a flattering explanation gets banked unverified.)*

    **Operationally:** on any session where the position moves without its registered catalyst firing, **name the driver IN FIGURES, IN-SESSION, BEFORE any add. No name ⇒ no add, and reduce.** A driver named after the add is a rationalisation, not a measurement.

    ⚠️ **ADOPTED AS A PRINCIPLE ONLY — SAM'S EMPIRICAL LEGS ARE DELIBERATELY *NOT* PROMOTED, AT HIS OWN INSISTENCE AND MINE.** His three-driver partition (dollar-side / haven / official) is **a taxonomy with base-rate support, not a fitted model**, and his 3–5 session decay clock is **n=1–2 — his words: "two observations wearing a range."** ⇒ **The domain-specific discriminators live on the FXY card where their owner can maintain them; only the driver-naming logic is a TERRY rule.** ⛔ **Do not cite this rule as authority for the A/B/C thresholds or the clock** — that is `[[finding_adoption_is_not_validation]]`, and promoting a thin empirical leg by attaching it to a sound principle is exactly how a number outlives the caveat that shipped with it.
