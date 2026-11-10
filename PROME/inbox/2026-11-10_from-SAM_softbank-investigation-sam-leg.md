# SAM → PROME: SoftBank investigation, SAM leg (SoftBank's own documents), 2026-11-10 17:2x ET

**Scope:** PROME prome-07 17:19 ET (Will's 17:18 ET word) and the 17:26 ET re-aim of question 6. $0. No threshold, gate letter, band, card or prediction moved. VULCAN's and LIQUID's legs are not duplicated; LIQUID's ecc68f6a82 is cited.

**Full record:** `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_LOSS_INVESTIGATION.md` (commits 4031b45c1e and be0a4875c3; every line carries its page). Pass 1 is 07c8ff11ce.

**Plain words for Will:**
- SoftBank lost ¥1.12T in the quarter. Most of it is paper: Intel marks, the Intel hedge, and writing off money already spent on power equipment it no longer plans to buy.
- The cash still owed from that write-off is ¥140B, worth about 0.2 point of leverage.
- Leverage on SoftBank's own measure is about 22.7% at Arm's 11/10 close, against its 25% normal-times ceiling. Arm would have to fall to about $145 to breach it.
- The 13.88% jump in Tokyo came before the results were public. The only reaction so far is the US ADR, −4%. Tokyo's verdict comes at 19:00 ET tonight.
- **Caveat that matters:** SoftBank does not name the equipment suppliers, the Intel-hedge bank or SB7's remaining purchase commitments, so the size of what is still to pay is not knowable from its documents.

## Answers (pages: fr = financial report PDF/printed; ds = data sheet; deck; acct = accounting deck)

| # | Answer |
|---|---|
| **1. Q2 bridge (Q2 alone, ¥B, ds p.2, segments p.3 and p.16)** | Gross profit +1,143.4 · SG&A −1,081.9 · investments −133.6 (holding cos −303.9 incl. **Intel −270.1**; SVF +245.6) · **finance cost −461.9** (mostly cash; bridge-fee write-off inside) · FX +220.3 · derivatives −41.7 (holding cos −314.1 incl. **Intel collar −321.9**; Other segment +274.7, consistent with the Energy Global warrant liability falling, SAM inference) · **other −669.9** (**SB7 power −597.2**, Lordstown factory impairment −72.5) → pre-tax −1,027.9 → **owners −1,115.3** (rows reconcile; SAM check). About ¥1.25T is non-cash marks; ¥140.2B is new cash from Q3 |
| **2. ¥597.2B** | **SB7 (Silver Bands 7)**: SBG and SVF2 subsidiary, "a separate entity from SB Energy" (deck p.16). It paid suppliers **¥1,500.9B ($9.48B)** through 9/30 for "power generation-related equipment" for US AI data-center projects (fr 7/5). The **$2.9B** written off is for equipment "no longer in the revised procurement plans"; the **$0.9B** is contract modifications and settlements, with cash from Q3 (acct p.8). **"The loss of $3.7B is completely unrelated to PORTS-Pike"** (acct p.8). **$6.6B of advances stays on the balance sheet** (deck p.18; fr 29: ¥1,065.1B line). Rebates of up to $2.1B are not recognised. **Suppliers: not named.** "Turbine" appears nowhere. Further commitments: not quantified. **No SBG guarantee of SB7 or SB Energy found** (fr 14/12: subsidiary financing "non-recourse to SBG"). **No further loss flagged.** Separately, Energy Global, LP carries a ¥541.8B warrant liability to OpenAI (fr 71/69) |
| **3. ¥321.9B Intel** | Collar prepaid forwards by **a wholly owned financing subsidiary**, August 2026, on **all 87.0M Intel shares**. They raised **$7.35B** (3.7× the $2B cost), with a cap and floor on the settlement price (fr 71/69 note 2; fr 9/7). At 9/30: liability ¥1,139.6B plus derivative liability ¥337.9B (fr 14/12). **Non-recourse to SBG.** The loss comes from Intel rising after the August execution. **Counterparty, strikes, dates, margining: not disclosed** |
| **4. Leverage, cash, ceiling** | **15.9% at 9/30 contains both losses.** The Intel collar has no separate LTV effect (deck p.82 items a and i). Power cash out by 9/30 (deck p.79: "Data center and power generation-related expenditures −¥0.4T" in Q2). **Roll at Arm $181.49 (11/10 close, USD/JPY 158.69 at 17:23 ET): 22.7%, 22.9% with the ¥140.2B settlement**; 25% at Arm about $145–149 (SAM arithmetic). Cash **¥5.0T vs ¥1.6T** of two-year redemptions (deck p.23). Bridge fully repaid; record $56.5B financing in Q2 (deck p.66). Policy unchanged: under 25% normally, 35% upper, at least 2 years of redemptions in cash (deck p.65). **No covenant language.** Ratings as of 11/10 (deck p.71): **JCR A Negative · S&P BB+ Stable (from Negative 7/16) · Fitch BB+ Stable (new 9/11)** |
| **5. Musk's claim** | "SoftBank is defaulting on its turbine orders" (X 11/6). **Corroborated in part:** orders were cut and suppliers settled. **Contradicted:** the documents describe negotiated settlements with cash paid and rebates won, not a default. **Narrowed:** not PORTS-Pike. **Not established:** that the equipment was turbines |
| **6. The 13.88%, re-aimed** | **(a) Release confirmed at the primary:** the TDnet 11/10 list shows `15:30 99840 ソフトバンクグループ ... 第２四半期（中間期）決算短信` at **15:30 JST, the TSE close**, so the 11/10 Tokyo session traded **before** the results. **(b) Driver:** **no source found** (two searches). Context only: 9984.T fell −28.6% from 10/29 (¥4,765) to 11/9 (¥3,400), including the 11/6 Musk post; CDS was 497 on 11/9, widest since August (LIQUID ecc68f6a82). **(c) Post-results Tokyo: known-unknown until 11/11** (opens 19:00 ET; closes 01:30 ET). What I will read then: the completed close and % against ¥3,872; the low against ¥3,400; volume against 64.8M; the roll at that day's dated Arm price; any new 9984 TDnet filing; whether SoftBank posts its transcript. After results so far: SFTBY −4.00%, ARM −2.58% (vendor, US 11/10 session) |
| **7. Corrected in SAM's records** | Grade line 55 **CORRECTED** (pass 1). SB Energy guarantee line **stands, narrowed**. Q2-alone loss added. STATUS line 7 corrected and the roll added. Kill-on-sight **added**: do not call this a "default" or an "Ohio write-off". **The CONFIRMED grade is not touched** (the reported 15.9% is unchanged) |

## Known-unknowns

1. SB7's suppliers and whether the equipment was turbines.
2. SB7's remaining purchase obligations and project-financing timing.
3. Who pays the ¥140.2B: the +0.2 point assumes SBG.
4. Whether SB7's equity is valued in the LTV's "Others (b)".
5. The Intel collar's counterparty, strikes, dates and margining.
6. The non-cash share of Q2 finance cost.
7. Energy Global vs SB Energy identity (SAM reading only).
8. What drove the 11/10 rally, and the 11/11 Tokyo reaction.
9. Gotō's words at the primary (the transcript is still 404).
10. Rating-agency reaction (LIQUID).

**Routing:** VULCAN may close #1–2 from the supplier side.

**Next for SAM:** none ordered. I hold the window. If PROME wants it, I can read the 11/11 Tokyo session at 01:30 ET.
