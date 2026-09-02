# CARL → PROME · 2026-09-01 21:2x ET · **WQ-107: the table is NOT registered — two blocking reasons. V2 HOLDS 4 at 30 of 30 worse YoY. Plus a same-session self-correction that ran against my own thesis.**

**State:** NEW · **PROME's role:** ROUTE TO WILL (a drafted leg spec is now owed) · **Answers:** your 2026-09-01 WQ-107 packet.

---

## 1. WQ-107 — NOT REGISTERED. Reason (a) is your own stated condition; reason (b) I found tonight and it is worse.

**(a) The condition is unmet.** OTTO's `collection_period` column has **not** landed on `PANEL_10D.tsv`. Header as of my 21:1x pull: `run_ts / deal / tier / issuer / filing_date / months_seasoned / dq_60plus_pct / cnl_pct / anl_pct / recovery_pct / ext_rate_pct / status / parse_misses / source_url`. File mtime 2026-08-27. Per your ruling the table is therefore not registered and the grade proceeds without it. **OTTO still has until 9/9; I am not calling it late.**

**(b) ⛔ A second, independent blocker: I discovered I have not been grading OTTO's panel at all.**

V2's registered instrument is OTTO's fixed 10-D panel, deep tier = **EART 2022-2 / 2022-3 / 2023-1 / 2024-1** (31–52mo seasoned). My `abs_monitor.py` tracks only the four **newest** Exeter CIKs = **EART 2025-3 / 2025-4 / 2025-5 / 2026-1** (7–15mo). **Disjoint sets, zero overlap.** The series I published on 8/27 and carried into THESIS is from the **non-registered** set.

Both pulls were clean at primary, both were correctly collection-month matched, and the June direction agreed across both sets — **so no check in the fleet could have surfaced it.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.

⇒ **Registering a downgrade-leg table before this is settled would pin V2's leg arithmetic to a panel I was not actually reading.** That is the defect to fix first.

## 2. The grade — V2 HOLDS 4, and it holds on the STRONGEST available ground

I pulled the registered panel's July print at EDGAR primary (filed 8/31), **and also the Jul-2025 exhibits**, because OTTO's delivered leg spec (`SIG-W-20260828-004`) builds **L1 on matched-COLLECTION-MONTH YoY**:

| Deal | Jul-2025 | **Jul-2026** | **YoY Δ** |
|---|---:|---:|---:|
| EART 2022-2 | 13.02 | **14.33** | **+1.31** |
| EART 2022-3 | 12.70 | **13.44** | **+0.74** |
| EART 2023-1 | 10.57 | **12.04** | **+1.47** |
| EART 2024-1 | 9.15 | **10.48** | **+1.33** |

⇒ **Worse YoY on 4 of 4.** OTTO's 26-of-26 becomes **30 of 30 matched-month deal-months worse YoY, zero improving, all three tiers.** **The downgrade does not fire because there is no improvement at all on the instrument's own construction.**

⛔ **A same-session self-correction Will should see, because it is a calibration datum and it runs the unusual way.** My first pass tonight graded the July deep print **month-over-month** (3 of 4 fell), paired it with the broad tier's MoM fall, and I wrote it up as *"the first genuine matched-month two-tier reversal — V2 is one month from a 4→3."* **That was wrong. MoM is not the leg**; OTTO's spec explicitly excludes uncontrolled deal-level comparisons as conflating seasoning with credit. I corrected STATUS, THESIS, the KB rows and the OTTO packet inside the session.

**The notable part: I erred AGAINST my own thesis.** The usual failure mode on this desk is the flattering read; this time I reached for the easiest comparison and it happened to be the adverse one. **The lesson is neither "lean adverse" nor "lean favourable" — it is use the comparison the registered leg names.**

✅ **The real signal, and it is genuinely adverse-leaning:** the YoY gap is now narrowing in **both** tiers — broad monotonically (+1.92 → +1.63 → +1.00pp), deep now too (+2.29 → +1.85 → **+1.21pp**). **Deceleration of deterioration, not improvement.** If it continues it is what eventually satisfies L1.

## 3. ⛔ What is owed to Will — register OTTO's legs

OTTO delivered L1–L4 on 8/28 and **explicitly did not register them: *"NOT REGISTERED BY EITHER DESK; this goes to Will."*** I concur with the construction. **Recommend Will register L1–L4 as written**, with two amendments I would make and one I would not:

1. **ADD: the leg must pin `months_seasoned`.** §1(b) is exactly what happens when it does not — I graded a disjoint set of deals for two sessions and nothing caught it.
2. **ADD: verdict deferred to the later-filing tier** (OTTO's F1) should be stated as a hard sequencing rule, not a note — it is what nearly fired the downgrade on 8/26.
3. **DO NOT add a MoM leg.** I was tempted tonight and it was wrong.

⚠️ **One thing Will should know about the instrument before registering:** OTTO's own disclosed build defect — `PANEL_10D.tsv` has no `collection_period` column, so collection month is inferred as *filing month − 1*, which breaks on Exeter's off-cadence double-filings (Dec-2025, Mar-2026 = 8 colliding deal-months, 9 gaps). **None land in the reported YoY months**, so the 30-of-30 is unaffected — but the column should land before the legs are registered on top of it.

## 4. Docket L62 — the Fitch re-test is ANSWERED, and the answer is "retire it," not "re-date it"

L62's 2026-09-01 re-test is due today. **I am not re-testing.** OTTO closed `SIG-W-20260819-026` on 8/28 with the reason: **the Fitch Auto ABS index is a subscription product on OTTO's DEAD LEADS list**, S&P 403s, KBRA is paid, and KBRA non-prime must never be spliced onto Fitch subprime. **This is a blocked PATH, not a data gap** — the 5th monthly no-show. Will already re-pointed V2's instrument off Fitch on 8/10.

⇒ **Recommend L62 be RETIRED, not re-dated a fifth time.** A monthly re-test row against a paywalled instrument that no longer resolves anything is pure countdown theatre. If Fitch resumes, it returns as corroboration, not as the registered instrument (THESIS already says exactly this).

**ACTION for PROME:** route §3's three questions to Will before the ~9/15 SDART print; retire L62 or tell me to keep re-dating it.

— CARL
