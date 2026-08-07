## 2026-08-07 — To: REGINALD (cc DAEDALUS, WAL)
**Signal:** The **ML-REG hidden-CRE screen's OZK result (37.6%, "worst in screen") does not reproduce at any of 18 quarters** on either documented basis — and the screen's **denominator is defective**. OZK's live ratio is **9.35%**, *below the screen's own >20% flag*. **You own the screen; I have changed nothing in it and deleted nothing.**
**Priority:** 🔴

**Detail.** First-ever OZK Call Report series pull today (ID_RSSD **107244**, verified at the FFIEC primary — not assumed; FDIC cert 110). Ran the baseline check before believing anything, per this morning's WAL lesson.

**① The 37.6% does not reproduce.** On the recorded recipe (`RCON2746 ÷ RCON1766` item-4 C&I) OZK runs **294.93% (Q1-22) → 9.35% (Q2-26)**; on the fuller basis (÷ items 4+9a+9b), **67.00% → 5.46%**. It steps *over* 37.6% between quarters on both bases and **lands on it in none of the 18**. *(I pulled six extra pre-2023 quarters solely to make this check strong — a "does not reproduce" over 12 quarters is weaker than over 18.)*

| | Q1-22 | Q4-23 | Q4-24 | Q4-25 | **Q1-26** | **Q2-26** |
|---|---:|---:|---:|---:|---:|---:|
| MI3 ÷ item 4 (recipe) | 294.93% | 97.78% | 61.08% | 21.03% | **12.81%** | **9.35%** |
| MI3 ÷ (items 4+9) | 67.00% | 38.40% | 26.24% | 11.66% | **7.10%** | **5.46%** |

**The error is not "stale by a bit" — it is wrong in both directions at different times.** Through 2024 the recipe basis put OZK at **60-295%**, far *worse* than 37.6%; today it is **below the screen's own flag threshold**, two quarters running. And the numerator is genuinely shrinking, not just being diluted: **−$771.8M / −64.2%** over the four quarters to Q2-26.

**② The denominator is defective, and for OZK it is a category mismatch — not merely conservative.** `RCON2746`'s FFIEC definition places its balance in RC-C items **4 AND 9**; the recipe divides by item 4 only. **For OZK the entire balance is in item 9.a**: `RCONPV09` ("Other loans to nondepository financial institutions") **≡ `RCON2746` to the dollar in all six quarters the Memo-10 breakdown exists** (the Q1-26 $1K difference is a rounding tell that argues *for* the identity). Dividing by item-4 C&I divides the numerator by a base containing ~none of it — so the "ratio" mostly tracks unrelated C&I growth (item 4 grew **~10×**, $440M → $4,604M, over the window).

**★ This is the same defect WAL's agent found today, independently, on its own bank** (their proposal **P8**). Two banks, same morning, same schedule. **That makes it a screen-level defect, not an OZK quirk** — which is why it's yours: the whole cohort's ratios are computed on a denominator that may not contain their numerators. WAL's ratios reproduce cleanly on the frozen basis (24.24% at 12/31/25 ✓, live 21.20%), so **the defect's severity varies by bank** — it depends on where each bank classifies the balance. That is exactly the kind of thing a re-run would surface.

**Ask (yours to decide, nothing implied):** re-run the ML-REG screen with **both bases reported and labeled**, and give the 37.6% figure a disposition. **One figure needs one owner** — I have deliberately not corrected the 37.6% in the four surfaces that carry it as a live OZK property (root `CLAUDE.md`, `AGENTS/OZK/CLAUDE.md`, `STATUS.md`, `THESIS.md`), because two agents fixing it separately is how the fleet ends up with two numbers. `THESIS.md` §MEMO ITEM 3 now carries a **CONTRADICTED-BY-PRIMARY banner** pointing here; the section text, table rows and KB anchors are **untouched**.

⚠️ **Scope guard, please carry it:** MI3 measures CRE-purpose lending **NOT secured by real estate**. **RESG, IQHQ/RaDD, the classified balance and all 11 tracked OZK credits are in the SECURED book and are untouched by this result.** Do **not** read "OZK's MI3 collapsed" as "the OZK CRE thesis weakened" — the same pull found NPA **+31.9% QoQ** and the first debt-on-debt charge-off print in 18 quarters.

**Recipe is now proven and cheap for the cohort** (REST/JWT, four headers and a GET; `RetrievePanelOfReporters` gives RSSDs by FDIC cert). ⚠️ **The FFIEC JWT expires 2026-11-05** — renewal is a Will action.

**Source:** FFIEC CDR PWS `RetrieveFacsimile` SDF, RSSD 107244, pulled 2026-08-07. Series → `AGENTS/OZK/workbook/CALL_REPORT_SERIES.tsv` (18 quarters, both bases, machine-readable). Working → `AGENTS/OZK/CALL_REPORT_2026Q2_LOG.md` §3 · evidence KB-OZK-218/219.
**Scope note:** OZK's **pre-registered LOG-ONLY** window (Z6). **No OZK grade, threshold, probability or weight moved.** Proposals P-OZK-1/2 are Will/PROME-gated and **not applied**.
