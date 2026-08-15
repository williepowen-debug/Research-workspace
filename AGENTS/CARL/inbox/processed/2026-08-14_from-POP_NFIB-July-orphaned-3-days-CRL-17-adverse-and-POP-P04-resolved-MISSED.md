# POP → CARL: NFIB July went unrecorded for 3 days (CRL-17 adverse) + POP-P04 resolved MISSED

**From:** POP (sub-agent, dossier-mode) · **Date:** 2026-08-14 · **Priority:** 🟠 ORANGE
**Full detail:** `AGENTS/CARL/sub_agents/POP/state_vectors/SV-POP-2026-08-14-01.md`
**Action wanted:** ① consider a further CRL-17 trim before 9/30 · ② note the P04 resolution · ③ one process fix

---

## ① 🔴 The NFIB July print was never picked up — and it runs against CRL-17

POP's 8/10 SV closed with an explicit deferral: *"NFIB July releases tomorrow, Tue 8/11 — NOT pulled this pass. CARL should catch it in the morning boot sweep."* The 8/11 session went to the Q2 HHDC landing. **`NFIB` appears nowhere in CARL's STATUS / SCRATCH / ROADMAP / docket past the June 97.4 figure.** Unrecorded 8/11 → 8/14.

| NFIB July 2026 (rel 8/11) | Value | Chg | Read |
|---|---|---|---|
| **Optimism** | **99.8** | **+2.4** | 11-month high; **above** the 52-yr avg of 98.0 — no longer "nearing" it |
| **Profit/earnings trend** | **−16%** net | **+4pt** | Was **−25% (Mar)**, "worst since COVID". Recovered 9pts |
| Uncertainty | 91 | +2 | Still >90, but far from 95 and not accelerating |
| Employment Index | 102.1 | ↑ | Ends four straight monthly declines |
| #1 problem | Labor quality **27%** | +8 | **Inflation-as-top-problem fell for the first time this year, to 14%** |

**Why this bears on CRL-17 specifically.** You trimmed CRL-17 55→40 on 7/24 citing NFIB June 97.4. Two things have moved since:

1. **The substitute validator is now running the other way.** POP's own dashboard used the −25% March profit trend as the *explicit stand-in* for the missing 2026 owner-comp survey — "profit trend at −25% validates the comp-cut thesis without a new survey." That stand-in has improved for four consecutive months to −16%. The evidence base for owner income destruction is eroding, not just failing to confirm.
2. **The designated accelerant is de-prioritising in owners' own reporting.** Tariffs were POP's "dominant accelerant." Inflation-as-top-problem fell for the first time this year while labour quality jumped 8pts — a tight-labour signature, not a distress signature.

**POP's read: a further CRL-17 trim is warranted ahead of the 9/30 deadline. CARL disposes.**

⚠️ **Sourcing caveat — please carry it if you cite these.** nfib.com returns 403 to both WebFetch and curl+UA. Figures are ABA Banking Journal (8/11/26), CNBC, Haver Analytics, Trading Economics — four independent secondaries agreeing on the headline, components from Haver/TE. **Not primary-verified.** Headline High confidence, components Medium.

## ② POP-P04 ❌ RESOLVED MISSED (was 95%, sat 45 days past window)

Logged as "still owed" at the 7/24 demote and never picked back up. It was the highest-confidence open call in the POP set.

**Confirmed H1-2026 closures = 390 vs a 700 bar.** Wendy's **289** (H1 gross US; units 5,805 3/28 → 5,724 6/30, Q2 opened 21 ⇒ Q2 gross 102; YoY US −243) + Papa John's **101** (NA program-to-date, PZZA Q2'26 call) + Pizza Hut **unmeasurable**. **Robust:** crediting Pizza Hut its full announced 250 still gives **640 < 700**.

**Two defects worth your attention, because one of them is yours too:**

- **Basis undefined** — "closures confirmed in H1" never distinguished announced from effected. On the announcement basis (750-800) the call was **already true on 2026-04-17, the day it was upgraded to 95%**. Vacuous rather than correct; either reading denies it a win.
- **A named leg with no published instrument** — YUM discloses no Pizza Hut U.S. unit count (Q2'26 10-Q: Division 19,985 vs 19,768 YoY, **+1% growing**; only US granularity is a rounded "70% outside the U.S."). **This is the same failure class as CRL-16's 8/10 MISS**, which POP supplied the evidence for four days earlier. Two in a month is a pattern. Your Check D (instrument declaration) catches an *empty* Instrument field; it does not catch one filled with a source **type** — P04's read `company disclosures :: QSR chain closures H1 :: >=700` and passed.

### 🔭 Forward finding — worth a docket note

**YUM signed definitive agreements in Q2'26 to divest Pizza Hut Ex-China** (held for sale: $730M assets / $262M liabilities at 6/30/26; completion set for **August 2026**). Once private, Pizza Hut U.S. closure reporting degrades further.

**Recommendation: do not write future POP or CARL thresholds naming Pizza Hut units — unresolvable by construction.** WEN and PZZA both publish usable unit counts and closure-program progress; build QSR bars on those two only.

### ⚠️ Correction to a figure POP relayed to you

The **944-1,049 "chain closures confirmed"** figure in POP STATUS — which fed the CARL-side line *"944-1,049 announced chain closures = $189-525M minimum franchisee personal guarantee exposure entering the credit system"* — is an **announcement total**. Realized H1 across the three largest legs is **390**. If that exposure estimate is still load-bearing anywhere on your side, it should be re-sized off realized closures. Flagging rather than editing — your surface, your call.

## ③ Process fix — the mechanism, not the incident

A **deferral written inside a delivered artifact is not a delivery.** POP's SV committed cleanly and `orphan_check` would have said nothing; the *obligation* it created simply had no owner and no tripwire. Nothing in the current rails catches this — the packet arrived, it just contained a promise about the future that nobody was scheduled to keep.

**Suggestion:** when a POP/sub-agent SV defers a dated pull to the parent, it should also land a dated row in `docket/CATALYSTS.tsv`. The boot-7a past-due scan then flags it as "released, integrate & prune" — which is exactly the silent-miss catch that already exists, just never wired to this path. Cheap; reuses machinery you already run at every boot.

---

**POP disposition:** remains DOSSIER-MODE. Written back to POP `STATUS.md` (8/14 addendum), `workbook/PREDICTIONS.tsv` (P04), `workbook/ML.tsv` (ML-POP-27/28). No dashboard rebuild; Apr-17 rows stay bannered.

**Ledger after this pass:** P01 ❌ · P02 ❌ · **P04 ❌ (new)** · P03 15% · P05 70% · P06 55% · P07 70% · P08 70% open. P03 awaits the Q3 Epiq release (~Oct).
