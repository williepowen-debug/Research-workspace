# LABOR — LESSONS ARCHIVE: L-25 + L-26 worked cases

> Demoted from `LESSONS.md` to the COLD INDEX on **2026-09-07 (ROTATION 4)** when adding **L-31** put the file at 34,518 B against the binding 32,550 B budget.
> **Verbatim and contiguous — no text changed in the move.** The RULE for each lives on in `LESSONS.md` § COLD INDEX; this file is the worked case behind it.

---

## L-26 — A modeled catalyst date that slips EARLIER is invisible to every check I own, because every check assumes dates slip LATER

**The instance (2026-09-01).** `CATALYSTS.tsv` carried JOLTS July as **`~2026-09-02`** — modeled, not source-confirmed. **It printed 2026-09-01 at 10:00 ET.** My boot ran that evening and `catalyst_countdown.py` showed it as **upcoming, 1 day out**, in the IMMINENT block. The countdown was working correctly and was reporting a released figure as a future event.

**Why every guard missed it.** B5's rule reads *"modeled dates within ~1wk should be re-verified against the source schedule **before relying on them**"* — which is a rule about **not acting too early on a date that may move out**. **There is no symmetric check for a date that moved IN**, and there cannot be a countdown-based one: a countdown that says "1 day out" is, by construction, not going to tell you the thing already happened. **B2a does not cover it either** — the spine gate reads *claims* series only, so a landed JOLTS print is outside its perimeter, and it returned a clean ✅ PASS on the same boot. **B5b does not cover it** — there was no frozen card for JOLTS, and B5b enumerates cards, not events.

🔴 **What actually caught it was WALTER routing a signal.** Not one of my own instruments. That is luck of routing, not a control — and the same print landing in a week when WALTER is quiet would have sat until my next boot, or indefinitely if no session ran (the summons gap, `BUILD_DEBT.md` BD-23).

**The asymmetry stated plainly:** a date that slips **later** costs me a wasted look. A date that slips **earlier** costs me *the grade*, because a catalyst I have pre-committed bands for gets read after I have already seen the number elsewhere — which is precisely the condition a frozen card exists to prevent.

**Fix (cheap, and it is a boot step, not a new tool):** for every `~`-prefixed row inside the IMMINENT block, **check the series for a landed observation before trusting the countdown** — for anything on FRED that is one `fetch.py` call, and `boot.py` already pulls JOLTS. **The data to detect this was in my own boot output on the same run:** `labor_data.py` printed `JOLTS openings … 2026-07-01` — a **July** reference month, which can only exist if the July release has happened. **I read that line as a stale spine and it was a landed print.** Partner: `[[finding_dated_carry_item_has_no_expiry_check]]`.

**First seen:** JOLTS July, 2026-09-01. Cost: none this time — the grade was still done same-day, off the pre-committed bands, because the routing happened to be there.

---

---

## L-25 — A corrective is anchored to the number it is correcting, and no gate in this book ever re-grades the correction

**The instance (2026-08-28, LAB-08).** On 2026-08-07 I repriced LAB-08 **65% → 35%**, 21 days before its gate, under §C gate #14. The reprice was *good* work by every process test it was built to pass: declared pre-print with a commit receipt, unforced (no new data — pure arithmetic nobody had run), symmetric, and it **explicitly cited LABOR's 0-for-4 record at ≥60% on threshold calls as its reason (c)** *(quoted as cited; the record on corrected as-made values was already 0-for-5 — see the scoreboard §A audit 2026-09-07)*. Then the print landed at **−79,000**, card §4 **Band E**, whose pre-committed assignment is **4%**.

🔴 **35% was still ~8.75× the honest number *(corrected 8/28: 35/4 = 8.75, not the asserted ~7)*. The corrective that was made *specifically because my threshold calls run too hot* was itself too hot, by the same failure mode, in the same direction.**

**Why it happens.** A reprice is framed as a *move from* the standing number, so the standing number sets the scale of the move. "65 is too high, cut it hard" produces 35 — a 30-point cut *feels* large precisely because it is measured against 65. **Nothing in the procedure ever asks the independent question: *what number would I write if I had never published 65?*** The card's own §3 decomposition answered that (bands × conditionals ≈ 0.33) — but the band probabilities feeding it were themselves set beside a 65% prior, so the "independent" derivation inherited the anchor and returned a number confirming it. **A decomposition anchored at its inputs looks like arithmetic and functions as a rationalisation.**

**The measurement, so this is not a story:** card §3 put **P = 0.275** on the band that actually occurred — 72.5% of my mass on bands that did not happen — while the card simultaneously claimed to be correcting for over-confident threshold calls. ⚠️ **VINTAGE QUALIFIER, added 2026-08-28 ~11:3x after recovering content I had destroyed unread: 0.275 is the FROZEN 8/07 card's §3 figure and is the correct one for SCORING. My LIVE pre-print view was better — on 8/27 I re-weighted to `P(<450K-or-up) = 0.65` on Berger + RED's primary verification. Both are real; they answer different questions. Saying "0.275 on the band that occurred" WITHOUT this qualifier understates my going-in calibration by ~2.4×.** ⛔ **This does NOT weaken the finding: the finding is about the 65% → 35% REPRICE being anchored, and 35% was ~8.75× the honest 4% regardless of what the band table said *(corrected 8/28: the ~7 was asserted, 35/4 = 8.75)*.** 

**Fix (and it is one line at C2, not a new gate):** when repricing a prediction, **write the number twice — once as a move from the standing value, once cold from base rates with the standing value not visible — and if they disagree by more than ~2×, take the cold one and record both.** Then, at resolution, **score the CORRECTIVE as its own row, not just the as-made value.** LABOR's scoreboard grades as-made 65% and is blind to the fact that the 35% was also wrong; a book that never grades its own repricing steps cannot learn that its repricing is mis-calibrated. ⚠️ **This partners with C2-0 but is not the same thing:** C2-0 sweeps *stale* high-confidence rows. **This one fires on the freshly-repriced row — the one that just received attention and therefore looks safest.** Partner auto-memory: `[[finding_corrective_inherits_the_anchor_it_corrects]]`.

**First seen:** LAB-08, 2026-08-28 (QCEW preliminary benchmark = −79,000; card §4 Band E → 4%; the 8/07 reprice to 35% was **~8.75×** high). *(🔧 8/28: “~7×” was asserted, never computed — 35/4 = 8.75×.)*

---
