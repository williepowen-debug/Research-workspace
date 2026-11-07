# FLG THESIS — blocks rotated 2026-11-07

Verbatim blocks moved out of `THESIS.md` by FLG at the Q3 10-Q session to make room under the 32,550 B read budget. History, never current. crc32 of the text between the fences: `5e5ee75b`.

```
### Q1 body


CRE concentration = CRE / total risk-based capital. FLG's book contracted **−28.8% in loans and −21.1% in assets** over eleven quarters (KB-FLG-005). If the easier-to-exit assets ran off first and multifamily is the stickiest leg, **the ratio rises while absolute CRE risk falls.**

✅ **ANSWERED THE SAME EVENING, AT THE PRIMARY, AND THE ANSWER IS NO** (REGINALD `fb1f68659`, matrix §3b, verified at artifact): CRE numerator **−32.2%** ($48.33B → $32.76B), total risk-based capital **flat at −2.6%** ($10.27B → $10.00B), ratio **−143pp and falling in all 11 quarters** (~11pp merger basis at 2025Q4, KB-080). **The denominator held, so the artifact is arithmetically impossible on this name.** The composition intuition survived — multifamily *is* the stickiest leg (MF −28.6% vs construction −55.6%, non-OO −40.8%) — it simply does not produce the artifact.

🔴 **But the answer changed the read, and that is the durable result:** channel 1 is **level-high, trajectory-de-risking**, ~2 quarters from crossing below 300% at the current rate. **"Cohort-worst CRE concentration" must NOT be read as deterioration.** The concentration channel is not where this thesis lives.

⇒ *v1.0 named 29% coverage as load-bearing; superseded: coverage is 31.04% (10-Q basis) and the live signal is the specific reserve, $163M = 5.8% (Q2b, STATUS).*
- **Unblocked:** concentration thresholds may now be proposed — but base-rate them against a *falling* series, not a rising one.
- *(Hypothesis refuted, question worth asking. `finding_normalization_choice_picks_opposite_winners` still applies in reverse: the two normalizations AGREED, and the agreement is what redirected the desk.)*

### Q2 body


Total loans QoQ, eleven quarters: `−0.1, −2.9, −1.1, −10.9, −5.8, −3.0, −4.0, −1.9, −3.5, −0.6, **+0.9**`.

**Q2-2026 is the first positive quarter in the series**, and the prior four decelerate monotonically toward zero (KB-FLG-014, first-hand recomputation — all eleven cells reproduce against `total_loans_k`).

✅ **ANSWERED AT THE PRIMARY 2026-08-28 — AND THE ANSWER DISSOLVES THE ALARM.** The 10-Q splits the book (KB-FLG-040):

| Book | 2025-12-31 | 2026-06-30 | H1 change |
|---|---:|---:|---|
| **Multi-family** — *the thesis's actual subject* | $28,983M | **$26,931M** | 🔴 **−7.08%** |
| Commercial & industrial | $15,217M | $18,563M | **+21.99%** |
| CRE | $9,314M | $8,244M | −11.49% |
| **Total loans HFI** | $60,732M | $60,987M | **+0.42%** |

⇒ **Total loans turned positive because C&I grew $3.3B on $4.8B of new originations, while multifamily ran off −7.08%.** `loans_qoq_pct +0.9%` measures a **MIX SHIFT**, not the end of the run-off. **The deleveraging of the multifamily book has not bottomed and is not close.**

🔴 **This was a CONSTRUCT-VALIDITY DEFECT IN K-1, now fixed** (`EXIT_PROTOCOL.md` K-1, re-cut 2026-08-28). The old kill would have fired on total loans and declared a NYC-rent-regulated-multifamily thesis dead on the strength of **commercial-and-industrial growth**. Leg 1 is re-cut onto multifamily dollars. ⚠️ **Note the error's direction: it made the kill EASIER, biasing the rail toward retiring a live thesis** — the failure nobody complains about.

- **Now graded by:** prediction **FLG-03** (multifamily HFI < $26,931M at 2026-09-30, 88% EMPIRICAL, resolves 2026-11-20).
- **What survives from the build read:** the *observation* was correct and correctly flagged as the strongest counter-evidence. Only the instrument was wrong.

### Q2e method note

**Method note worth keeping (REGINALD's, and it corrects a misreading of PAT-119 before anyone makes it):** on this instrument the kill and the signal are **exact complements**, so there is no 99th/43rd asymmetry to find. **That asymmetry was a property of the CO/prov FORM, not a general one — so PAT-119 coming back clean here is INFORMATIVE, not a null result.** A clean pass means the form is sound, not that the check failed to run.

### Q2d rounding trap

⚠️ **ROUNDING TRAP — read before anyone ever registers a level here.** FLG-2026Q2 computes to **14.5959×**. The original count was taken with a **14.6** cut, and 14.6 was itself the *rounded display value of that same observation* — so the unrounded datum fell just the **wrong side of a threshold derived from its own printed form**. REGINALD self-corrected it (`8b5a65231`); nothing downstream moved (99.4th either way, the ≥10× tail unchanged, the falsifier flag unchanged). **The generalisable rule: a threshold typed from a printed value of the observation it is meant to describe will misclassify that observation.** Carry the unrounded figure, or set the cut from the distribution rather than from the datum.

### Q3 process failure

🔴 **A process failure worth more than the finding.** `TRIGGERS.tsv` T-06 carried the RGB vote as `[EST] 2027-05-03` — so **an event that had already happened rendered as PENDING**, and the register could not tell the two states apart. **This desk was ~10 weeks blind to its own defining mechanism firing, while holding a correctly-formatted, in-date wake row aimed at it.** Corrected; T-06 re-scoped to the 2027 cycle.
```
