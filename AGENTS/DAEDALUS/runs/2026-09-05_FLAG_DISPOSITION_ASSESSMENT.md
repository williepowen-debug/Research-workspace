# Flag-disposition assessment — does existing evidence already show whether follow-through is improving?

**2026-09-05 EVE · DAEDALUS · Codex-recommended (round 2), bounded, NO new instrument.** Method: revisit the five walk cases + the instrument flags this session; for each, establish (i) correct disposition? (ii) reached affected consumers? (iii) stayed corrected? — and **count justified no-ops / false alarms SEPARATELY from ignored valid warnings** (the separation my "instruments work, failure is downstream" slogan collapsed). All disposition facts verified at the artifact, not from memory.

## Population (13 instances) and disposition

| # | Flag / correction | (i) disposition correct? | (ii) reached consumers? | (iii) stayed corrected? | Category |
|---|---|---|---|---|---|
| 1 | CVNA L131 fabrication (unwind) | yes — 6 surfaces unwound same day | yes (CARL sole) | yes — 0 stale copies now | ✅ CORRECTLY-ACTIONED |
| 1b | CVNA sub-flag: claim_check "Wed 9/10 is a Thursday" | **NO — resolved BACKWARDS** (Wed→Thu; erased the true survivor) | n/a | re-corrected later | 🔴 INCORRECTLY-RESOLVED |
| 2 | ES-02 lag rule defect | yes — rule replaced, verdict re-derived to confirm survival | yes (STUE+CARL) | yes | ✅ CORRECTLY-ACTIONED |
| 3s | HANS Qatar — HANS's OWN surfaces | yes — 2 surfaces + KB superseded | n/a (self) | yes | ✅ CORRECTLY-ACTIONED |
| 3c | HANS Qatar — HAWK consumer side | correction valid | **NO — packet unread, HAWK dark** | **NO — 4 stale copies STILL live** (STATUS·SCRATCH·NEXUS_BRIEF·KB×2, re-verified) | 🟠 NOT-REACHED |
| 4 | HAWK/Brent $86.36 (COR-828-01) | yes — HAWK confirmed clean 9/2 | yes | yes (0 stale) — but **receipt still unwritten** (verified 0) | 🟡 RECORD-GAP |
| 5 | HOMER FHA break (COR-828-04) | yes — caveat integrated 8/31 | yes | yes — but **receipt still unwritten** (verified 0) | 🟡 RECORD-GAP |
| 6 | verify_push false-green | instrument was BROKEN (latent since 8/23) | — | fixed tonight | 🔵 BROKEN-INSTRUMENT (external catch) |
| 7 | scorecard efficiency ratio | instrument measured wrong thing | — | withdrawn tonight | 🔵 BROKEN-INSTRUMENT (external catch) |
| 8 | complete_check pairing flags (41b/76e) | yes — verified already late-paired (EVOLUTION r) | n/a | n/a | ⚪ JUSTIFIED-NO-OP |
| 9 | subject guard `len=104` (46e4f6399, AM) | **NO — guard fired, committed anyway** (verified: subject is 104) | n/a | n/a | 🔴 IGNORED-VALID-WARNING |
| 10 | subject guard — tonight's 10 commits | yes — measured every subject, ALL ≤100 (max 97) | n/a | n/a | ✅ CORRECTLY-ACTIONED |
| 11 | my MIDAS "invocation missing ×3" flag | over-broad — 2 of 3 graders correctly on-demand | corrected in profile | — | 🟡 FALSE-ALARM (partial) |
| 12 | my "coverage=improvement" + "build an instrument" (to Will) | **NO — repeated the over-prescription reflex ONE MESSAGE after Codex named it** | Codex caught it | re-pointed to this assessment | 🔴 IGNORED-VALID-WARNING (live recurrence) |
| 13 | intake (A4): 3 of 5 corrections never entered the register | PROME registering | **PARTIAL — CVNA in (7 rows); Qatar+ES-02 routed, not emitted** | pending | 🟠 NOT-REACHED |

## Tally
| Category | n | What it means |
|---|---|---|
| ✅ CORRECTLY-ACTIONED | 4 | valid flag, acted on right, reached, stayed |
| ⚪ JUSTIFIED-NO-OP | 1 | flag fired, correctly judged no action — a GOOD outcome |
| 🟡 RECORD-GAP | 2 (+1 false-alarm) | substance right, receipt/record not written |
| 🟠 NOT-REACHED | 2 | valid correction, dark consumer / partial propagation |
| 🔴 IGNORED-VALID-WARNING | 2 | **the actual follow-through failure** |
| 🔴 INCORRECTLY-RESOLVED | 1 | acted in the WRONG direction (launders the defect) |
| 🔵 BROKEN-INSTRUMENT | 2 | instrument-integrity, both caught EXTERNALLY not by self-audit |

## The read — and it answers the question without a new instrument

1. **"Follow-through is failing" was too coarse, and the disaggregation matters because the buckets need DIFFERENT remedies.** The one bucket my slogan actually pointed at — IGNORED-VALID-WARNING — is 2 instances (the AM `len=104` commit; the repeated over-prescription reflex tonight). And the paradigm case, the subject guard, was **followed on all 10 of tonight's commits** after being ignored once in the morning. So the discipline is not uniformly failing — it failed once and held once. n=2, inconsistent: **too small a sample to call a trend in either direction.** That is the honest answer to "is prevention improving": *unproven, and the evidence we have is a coin-flip, not a curve.*

2. **The larger, differently-remedied problems are NOT follow-through at all:**
   - 🔵 **Instrument integrity** (2): both broken instruments were caught by EXTERNAL review, not self-audit — a standing blind spot. Remedy: keep external review in the loop (already happening), not "act on the instrument."
   - 🟠 **Propagation / intake** (2): HANS→HAWK is unreached (4 stale copies still live on a dark desk) and intake is partial (Qatar/ES-02 not yet registered). Remedy: intake + consumer reconciliation (the A4 fix PROME is executing), not "act on the instrument."
   - 🟡 **Record gaps** (2): HAWK/HOMER substance done, receipts unwritten. Remedy: A6 (a receipt POINTS at existing evidence), a bookkeeping fix.

3. **The single most diagnostic instance is #12:** I repeated the over-prescription reflex — proposing to BUILD an instrument — one message after Codex named that exact tendency and I *accepted* it. An ignored valid warning against a warning I had just agreed with. That is the strongest single piece of evidence that prevention/follow-through is unproven, and no new instrument would have caught it — a peer did.

## Conclusion (what this bounded pass establishes, per Codex's test)
**The existing evidence WAS sufficient — a new "act-on-instrument" instrument is not warranted.** Disaggregated, the "follow-through" problem is really 3–4 distinct problems, and three of them (instrument integrity, propagation/intake, record gaps) are already being addressed by other means (external review, the A4 intake fix, A6 receipts). The residual true follow-through failure (ignored-valid-warning) is n=2 and inconsistent — not a trend, and not a size that justifies building a reporting obligation to measure it. **Re-checking these same cases at the next comparable session, with the same buckets, is the cheap way to see whether n moves — a repeatable read, not a new instrument.** Adopt Codex's verdict: improvement in correction *quality* is concrete; improvement in *prevention* is unproven and, on this evidence, unmeasured-because-too-small — not because we lack an instrument.
