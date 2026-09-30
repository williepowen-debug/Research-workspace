---
name: finding_prose_claims_escape_test_rigor
description: in one session an agent applies full primary-source rigor to claims shaped like a pre-registered TEST and free-rides on same-session claims embedded in PROSE — and a universal quantifier over your own metrics ("all my X are improving") is a ledger claim that must be answered from the ledger, counting stale rows as UNKNOWN not absent
metadata:
  node_type: memory
  type: finding
symptoms: "an advisory to the operator states a domain fact the desk itself said it could not source"; "a coordinator's synthesis carries a spread, rate or exposure claim with no citation while the desk's version carried the block"; "a reviewer corrects the coordinator's aside, not the desk's finding"
---

**Verification behavior is triggered by the SHAPE of a claim, not its load-bearingness.** A claim formally framed as a test — pre-registered threshold, named prediction ID, expected-signal row — reliably triggers primary-pull discipline. A claim of equal or greater consequence written as a *sentence in the summary* rides on vibes. Both can ship in the same message, so the demonstrated rigor on the first launders the second.

**Worked case (2026-07-25, MARCO boot sitrep — two claims, one session, two standards):**

- **Claim A, shaped like a test (handled correctly).** ES-MARCO-08, a pre-registered produce-CPI-vs-pump-price discriminator due at the June CPI print. MARCO refused the search-result snippet, pulled the BLS public API directly, computed YoY from the index levels, caught that its own carried "+6.1% fresh F&V" was actually the `SAF113` aggregate and not `SAF1131` fresh, and reported a result that **cut against its own thesis** (F&V softened *with* the pump collapse → freight carried more of the spike than labor).
- **Claim B, shaped like prose (wrong).** In the same summary: *"every FL metric I own is improving, while CORAL's read hot."* False. Three improved; migration level, voter-reg net, Canadian air stack, FL capacity, MIA pax, hospitality **wages**, and the FL insurance **cost** index were breached, negative, or unrefreshed. `VX.tsv` was never opened before the claim was written.

**Three mechanisms produced Claim B — each generalizable:**

1. **Generalizing from the inbox instead of the ledger.** Three of the four rows in the FL table came straight from one inbound packet. An inbox is a feed of *deltas*, skewed to whatever a neighbor happened to refresh; the ledger is the *state*. Quantifying over "what arrived this window" and reporting it as "what I own" is the error.
2. **Stale scored as benign rather than unknown.** The boot sweep had printed `VX.tsv — 42/57 vectors older than 60d` *before* the summary was written. It was filed under "housekeeping gaps" instead of being read as the direct refutation of the paragraph. 42 unrefreshed vectors are 42 **unknown** readings, not 42 absent ones — and the refreshed subset is exactly the biased sample.
3. **Substituting an adjacent metric with a fresh print for the one that drives the mechanism.** MARCO used the insurer-side figure (Citizens' exposure/PIF, improving) as a proxy for household insurance cost (`VX-3.01`, still breached at 4.5x national, +72% since 2019). Both were in its own files, moving in opposite directions. Migration responds to the household number; the insurer number simply had a fresh print attached.

**The reason it survived: the error was wearing the costume of rigor.** The sentence built on the false premise was *"that's a measurement-selection problem on my side, not a thesis win"* — self-criticism, which reads as already-audited. A confident wrong claim invites scrutiny; a **self-deprecating** wrong claim deflects it, from the reader and from the author. Humility in the framing is not evidence about the premise. Audit self-critical claims at the same standard as self-serving ones — they are the ones that reach the reader unchallenged.

**How to apply:**
- Any sentence with a **universal quantifier over your own metrics** — *every, all, none, uniformly, across the board* — is a claim about your ledger. Answer it **from the ledger** (one grep of the vector/workbook file), and count stale rows as `UNKNOWN`, never as silent negatives. Cheap check, catches the whole class.
- Before writing a synthesis paragraph, ask *"is the population I'm quantifying over my state, or this window's inbound?"*
- When two metrics in your own files could carry a claim, pick the one that drives the **mechanism**, not the one with the freshest print — then say which you used.
- Staleness alerts emitted at boot are **evidence about the claims you are about to make**, not a chore list. Read them before the synthesis, not after.

**Instance n+1 (2026-09-30, PROME advising Will on a CREED thread, corrected by CATO the same hour):** CREED's own text said it could NOT source CMBS refinancing spreads (its one data-access block). PROME's Will-facing synthesis then asserted two domain facts as prose: *"a 6.5% rate implies a spread thinner than any normal CMBS market, so the 13.2% figure understates the risk"* (no spread source; and Trepp defines 13.2% as balance below 1.0× coverage in a sensitivity, not a share unable to refinance) and *"the risk sits with CMBS bondholders, not banks"* (banks hold CMBS; the defensible words were "no relevant bank exposure identified"). Both rode inside advice whose SHAPE was commentary, so neither got the test-class check PROME applies to a number in a GATES cell. **Tell:** the coordinator's aside was more confident than the owning desk's finding. **Rule:** in a Will-facing synthesis, a domain claim PROME cannot source is either tagged INFERRED in the sentence, or handed back to the desk as a question — never stated flat because it "sounds right." A decision to stop researching needs no confident claim that the exposure is irrelevant; *"potentially useful, presently unconnected, lower priority"* is enough (CATO).

**Siblings:** [[finding_asymmetric_rigor_counterparty_claims]] — same asymmetry sorted by *target* (rigorous where you measure, sloppy where you infer about the other side); this one sorts by *claim shape* (test vs prose) and points at your own state. [[finding_same_datum_two_evidentiary_standards]] — one datum graded decisive in prose and partial in the trigger rail. [[feedback_pull_live_primary_not_dashboard]], [[finding_ledger_drift_behind_narrative]].
