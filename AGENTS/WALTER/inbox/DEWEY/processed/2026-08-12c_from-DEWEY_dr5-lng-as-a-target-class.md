# DEWEY → WALTER · handoff · DR-5 LNG as a target class

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-12
**Report (canonical):** `AGENTS/DEWEY/output/2026-08-12_dr5-lng-as-a-target-class.md`
**Flag:** `REQ-DEWEY-20260731-005` · **INDEX row:** appended (49 rows / 49 files, reconciles clean, 8-field)
**⚠️ THIRD handoff from me today** — `2026-08-12_..._c3-masking-duration-base-rates.md` (CARL C3) and `2026-08-12b_..._dr4-european-energy-baseline.md` (DR-4) precede it. Three separate reports, three separate rows.

**Stubs written by me at write-time (constrained-B):** FALCON *(action)* · SHADE, BRENT, HAWK *(info)* — `AGENTS/<X>/inbox/2026-08-12_from-DEWEY_dr5-lng-as-a-target-class.md`.

---

## One-paragraph summary for the `research-output` signal

**Kinetic LNG events do not move gas prices up — in this sample they move them down, and FALCON's registered "real but non-transmitting" hypothesis is CONFIRMED on both benchmarks independently.** Across five dated LNG kinetic/FM events, **10 of 10 event-windows produced a negative 5-day return** (TTF mean **−6.37%**, JKM mean **−1.84%**, vs unconditional means of +0.79% / +0.75%; largest single reaction **Damietta at −13.3%** on TTF). On the Ras Laffan FM itself — **~17% of Qatari capacity, 3–5 year repair, declared 2026-03-24** — both benchmarks were **~24% BELOW pre-strike three months later** (TTF 56.68 → 42.78; JKM 21.00 → 16.02), and five months on the **Asian** benchmark is **+0.9%**. **Transmission arrived ~4 months late and through STORAGE rather than spot**, which is the bridge to my same-day DR-4 (EU storage at a five-year low, 90% unreachable, LNG send-out −20.4% YoY at 38.3% utilisation — the outage was absorbed by drawing down the refill). **And the loss-absorption answer inverted on a vintage check:** the struck FSRU *Energos Winter* is Apollo-owned, and **NFE exited that vessel in November 2025** (charter early-terminated, sub-charter novated, $150.0M/four vessels), so the US-listed name has **no** exposure to the struck hull; the loss sits with Energos/Apollo, itself in a restructuring support agreement with NFE since 2026-03-08.

**Confidence:** High on the reaction functions and the ownership chain (all primary, reproducible). **Medium** on the storage-mediated transmission mechanism — inferred from DR-4's arithmetic, not causally tested.

## ⚠️ PARTIAL DELIVERY — 2 of 5 legs unmet; do not close the row as fully served

- **War-risk premia post-Damietta — NOT FOUND, explicit negative.** No LNG-specific premium, P&I response or AWRP revision located. **This is the leg SHADE most needed and it is open.** FALCON's `WARRISK.tsv` (Marsh, Hormuz hull 7.5–10%, as-of 2026-07-22, self-marked stale by 8/3) remains the newest primary and **predates Damietta entirely.** ⚠️ **Ledger warning: the beinsure "12× + $20bn DFC backstop" figure is dated 16 MARCH 2026** — FALCON logged it as a vintage trap and I re-hit it in my own search. It is live and it will catch the next person.
- **Global FSRU register — not built.** The **Energos/Apollo chain, the leg the prompt singled out, IS fully primary-verified.**
- **Liquefaction geography vs conflict zones — DELIBERATELY NOT BUILT.** DR-5's phrase *"exposure surface of LNG infrastructure to kinetic risk"* I scoped as **financial** exposure (ownership, loss-bearing, reaction functions), with no vulnerability or defensive-gap analysis, **following the discipline note you attached to DR-3**. Stated at the head of the report rather than left implicit. **If the fleet wants that leg it should be scoped explicitly with Will, not inherited from a phrase** — flagging so the ledger records a deliberate scope decision, not an omission.

## Process items for your ledger

1. **A statistical caution I have written into every DR-5 packet, because it is the kind of finding that gets over-read on relay:** 10-of-10 is directionally unanimous, and a matched control (days at ≥87.4% of trailing 20-day high) rules out simple mean reversion — negative 49% of the time vs 100% for events. **But the events are not independent** (four inside ten days; TTF/JKM correlated), so effective n ≈ two episodes × two correlated benchmarks, ~1.3 SE, **not significant.** It supports the **strong negative claim only** — *an instrument keyed to "LNG strike ⇒ price spike" fires wrong* — and explicitly **not** "short gas on LNG strikes." Please preserve that qualifier if you re-wrap this for the BOARD; `[[finding_rederived_signal_loses_the_senders_caveats]]`.
2. **The load-bearing error caught in-run was a vintage error, and it inverted the conclusion.** NFE's **Q1-2024** 10-Q shows NFE sub-chartering *"the Winter"* with **$1.287bn** of Energos vessels on balance sheet as a failed sale leaseback — from which DR-5 would have reported *"a US-listed company has direct exposure to the struck FSRU."* The **Q2-2026** filing shows the November-2025 exit. Nothing in the 2024 document was wrong; it was 2.5 years stale and the strike is 2026.
3. **`JKM=F` will not confirm its own identity** — Yahoo metadata returns `quoteType: ALTSYMBOL`, `currency: None`, `shortName: None`, unlike TTF which confirms cleanly as *"Dutch TTF Natural Gas Calendar,"* EUR. **Used for percentage changes only; no JKM level is quoted as a datum anywhere in the report or the stubs.**
4. **Tooling defect for BACKLOG:** `scripts/edgar_fetch.py` **throws an unhandled traceback** on a transport error rather than reporting it — the identical "a probe must never traceback" defect I found and fixed in `fetch_url.py` on 2026-08-02. `edgar_doc.py search` worked and was used instead. Logged.

— DEWEY
