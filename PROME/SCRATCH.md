# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-25 03:20 UTC (Tue 11:20 PM ET)

---

## QUICKSTART
Scenario D **78%**. War Day **25**. Account ~$54K+.
**WAL KB SEEDING — Pass 1 (extraction) in progress.**

---

## WAL KB STAGING LIST

Schema reminder: `ID | Date | Group | Entity | Fact | Source | Conf | Epistemic | Status | Stale_By | DerivedFrom | Vectors | Notes`

### GROUP: HIDDEN_CRE (Vector 1 — MI3 Reclassification)

1. **MI3_Ratio** | MI3/C&I ratio is 24.2%, GROWING from 15.5%. Only bank with increasing hidden CRE ratio. | FFIEC Call Report RC-C | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V1 | Trend is the tell — not just level

2. **MI3_Amount** | Hidden CRE amount = $2.73B ("Loans to finance CRE not secured by RE") | FFIEC Call Report RC-C | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V1 |

3. **True_CRE** | True CRE exposure ~59% of loans (vs labeled ~35%). CRE/Tier 1 = 474% (breaches 300% SR 07-1 guideline). | FFIEC Call Report RC-C + RC-R | A1 | DERIVED | ACTIVE | 2026-04-30 | →V1 | Derived from adding MI3 back to labeled CRE

4. **Mgmt_Confirm** | Vecchione Q4 call: "reserves adjusting modestly as our mix shifts towards higher return C&I growth." Bruckner: "we curtailed our growth and pressed out...CRE loans as a percentage decreased." Reality: True CRE stable at ~$36.8B, labeled CRE fell — relabeled, not reduced. | WAL Q4 2025 earnings call | A1 | EMPIRICAL | ACTIVE | — | →V1 | Management confirmed the relabeling on tape

5. **H8_Confirm** | H.8 data confirms systemic: C&I +14.4% YoY while CRE +1.1% (down from +5.9%) industry-wide. | Fed H.8 | A2 | EMPIRICAL | ACTIVE | 2026-06-30 | →V1 | Industry-wide relabeling, WAL is worst case

6. **Equip_Finance** | Equipment Finance = $3.489B, -16.6% YoY (Q4 2025). If genuine C&I (equipment) is shrinking while total "C&I" grows, growth must be relabeled CRE. Independent confirmation of MI3 thesis. | WAL Q4 2025 10-K/Call Report | A2 | DERIVED | ACTIVE | 2026-04-30 | →V1 |

7. **CRE_Tier1** | CRE/Tier 1 Capital = 474% using true exposure. Breaches 300% regulatory red line (SR 07-1). | FFIEC RC-R + derived MI3 | A1 | DERIVED | ACTIVE | 2026-04-30 | →V1 | Key regulatory threshold

### GROUP: SSFA (Vector 3 — Capital Arbitrage)

8. **SSFA_Total** | Total securitization exposures under SSFA: $17.22B at ~20% risk weight. RWA = $3.49B. | FFIEC RC-R Part II Items 9-10 | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V3 |

9. **SSFA_Other_OBS** | "Other On-Balance Sheet Securitization Exposures" = $10.815B at exactly 20.0% RW. Likely NDFI warehouse lending structured through SPVs (mortgage warehouse, BDC exposure, PE fund lines). | FFIEC RC-R Part II Item 9d / MDRM RCONS490, RCONS493 | A1 | EMPIRICAL (amount) + INFERRED (composition) | ACTIVE | 2026-04-30 | →V3 | Composition is inferred — needs verification

10. **SSFA_Capital_Savings** | Capital savings from SSFA = $1.098B ($1,378M required at 100% RW minus $279M at 20% RW). WAL holding ~$1.1B LESS capital than without SSFA. | Derived from FFIEC RC-R | A1 | DERIVED | ACTIVE | 2026-04-30 | →V3 |

11. **SSFA_AFS** | AFS Securities in SSFA: $3.792B at 21.1% RW. | FFIEC RC-R Item 9b | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V3 |

12. **SSFA_OffBS** | Off-balance sheet SSFA: $2.446B at 20.0% RW. | FFIEC RC-R Item 10 | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V3 |

13. **SSFA_Reg_Risk** | Basel III Endgame proposed tightening SSFA treatment. If enacted or if stress forces re-evaluation, WAL would need to raise ~$1.1B in capital. CET1 of 11.0% assumes SSFA continues. | Regulatory analysis | B1 | ASSESSMENT | ACTIVE | — | →V3 | No current regulatory action — forward-looking risk

### GROUP: CANTOR_FRAUD (Cantor Group V / Under-Provisioning)

14. **Cantor_Exposure** | WAL Cantor Group V exposure: $98.6M. Reserve taken: $30M (Q3 2025). Recovery rate assumed: ~70%. | WAL 8-K Oct 16 2025, Q3 earnings | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V2 |

15. **ZION_Comp** | ZION same fraud ring: $60M exposure, $50M charge-off (83% loss rate). Collateral deemed "irretrievably lost." WAL at 30% recognition vs ZION 83% on identical scheme. | ZION 8-K Oct 15 2025, CNBC | A1 | EMPIRICAL | ACTIVE | — | →V2 | Same perpetrators (Stupin/Marcil/Shyam), same collateral subordination scheme

16. **Cantor_Under_Provision** | If WAL matches ZION's 83% loss rate: required charge-off = $81.8M, current reserve = $30M, shortfall = $52M (5.2% of Q4 net income). If 0% recovery: shortfall = $68M. | Derived from WAL + ZION disclosures | A2 | DERIVED | ACTIVE | 2026-04-30 | →V2 |

17. **Cantor_Fraud_Mechanics** | Fraud methods: forged title insurance policies, lien position misrepresentation (not first position), collateral manipulation. Total ring exposure ~$270M across WAL, ZION, BANC, Enterprise Bank. | CA Bank & Trust lawsuit, SEC filings | A1 | EMPIRICAL | ACTIVE | — | →V2 |

18. **Cantor_Silence_Q4** | No mention of Cantor Group V in Q4 2025 earnings release or call. Reserve appears unchanged at ~$30M. Management not addressing under-provision. | WAL Q4 2025 earnings, Quartr | A2 | EMPIRICAL | ACTIVE | 2026-04-30 | →V2 | Silence ≠ resolution

19. **Repossessed_Assets** | OREO/repossessed assets trajectory: $8M (mid-2024) → $218M (Q2 2025) → $130M (Q3 2025) → $137M (Q4 2025). +2,625% from mid-2024 baseline, +163% YoY. | WAL quarterly filings | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V2 | Broader credit stress beyond Cantor

20. **Provision_Trajectory** | Provision for credit losses: Q1 2025 $31.2M → Q2 $39.9M → Q3 $80M (incl $30M Cantor). Charge-offs: Q3 2024 $26.6M → Q3 2025 $31.1M (+17% YoY). | WAL quarterly filings | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V2 |

21. **Legal_Exposure** | Class action investigation by Rosen Law Firm + Shamis & Gentile. SEC comment letters being reviewed. Investigation period: Oct 2024 — Oct 2025. Portnoy Law also investigating. | Legal filings, press releases | A2 | EMPIRICAL | ACTIVE | — | →V2 |

22. **Note_Finance_Book** | Total Note Finance book: $2B. Cantor = $98M = ~5% of note finance. Post-fraud review: all loans >$10M reviewed, no additional irregularities found. | WAL disclosure | A2 | EMPIRICAL | ACTIVE | 2026-04-30 | →V2 | Cantor contained within defined portfolio — but pattern matters more than size

### GROUP: INSIDER

23. **CFO_Swap** | CFO Gibbons (22-year tenure) moved to "VP Deposit Initiatives and Innovation" — parking title. Replaced by Idnani from JPM FIG (bank advisory/restructuring). Gibbons was dual-hatted CEO+CFO during Dec 2024 medical leave when CRE reclassification accelerated. | WAL 8-K, proxy filings | A1 | EMPIRICAL | ACTIVE | — | →ALL | The tell. You don't hire JPM FIG for good times.

24. **CEO_Medical** | CEO Vecchione took medical leave Dec 2024. Gibbons dual-hatted during exact quarter hidden CRE ratio grew fastest. Governance gap during reclassification acceleration. | WAL proxy/8-K | A1 | EMPIRICAL | ACTIVE | — | →V1 |

25. **Board_Risk** | Two risk-specialist directors added Dec 2025, including Clarke Starnes III (former Truist CRO). Boards add risk specialists when expecting risk. | WAL proxy | A1 | EMPIRICAL | ACTIVE | — | →ALL |

26. **CAO_Exit** | CAO Ardrey retired. Two discretionary open-market sales at $64 and $76 before announcement. Replacement Mucha: 641 shares sold Feb 2026 (only open-market sale). | SEC Form 4 filings | A1 | EMPIRICAL | ACTIVE | — | |

27. **Zero_Buying** | Zero insider buying across all officers and directors. | SEC Form 4 filings | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →ALL | Monitor for any change — would challenge thesis

28. **Comp_Restructure** | Cash-settled RSUs + new Executive Stock and Bonus Deferral Plan (Dec 2025). Ambiguous signal — could be retention or preparation. | WAL proxy | B1 | EMPIRICAL | ACTIVE | — | | Ambiguous

29. **Insider_Cross_Bank** | OZK insiders sell crudely (open-market). WAL insiders restructure sophisticatedly (title changes, board additions, comp restructure). Different tactics, same message: preparation for difficult chapter. | Cross-bank analysis | B1 | ASSESSMENT | ACTIVE | — | →ALL | Pattern, not proof

### GROUP: GEOGRAPHIC (FDIC District / Fast-Transmission Evidence)

30. **SF_NCO_Highest** | SF district NCO rate 1.13% — HIGHEST of any FDIC district (national avg 0.62%). Losses being recognized, not deferred. | FDIC QBP Q4 2025 Table III-B | A1 | EMPIRICAL | ACTIVE | 2026-06-30 | →ALL | Core fast-transmission evidence

31. **SF_Pipeline_Lowest** | SF district 30-89 day pipeline 0.26% — LOWEST of any district (national avg 0.33%). Cleanest incoming delinquency. | FDIC QBP Q4 2025 Table V-A | A1 | EMPIRICAL | ACTIVE | 2026-06-30 | →ALL | Pipeline methodology breaks for WAL

32. **SF_PDNA_Gap** | SF PDNA/NCO gap = 0.54pts (tightest nationally). Dallas = 1.69pts (widest). National = 0.94pts. SF banks charge off aggressively without prolonged delinquency stage. | FDIC QBP Q4 2025 derived | A1 | DERIVED | ACTIVE | 2026-06-30 | →ALL |

33. **SF_CRE_Noncurrent** | SF district CRE noncurrent 0.90% (below national 1.30%). Surface reads bearish for short, but offset by highest NCO — losses go direct to P&L, not pipeline. | FDIC QBP Q4 2025 Table V-A | A1 | EMPIRICAL | ACTIVE | 2026-06-30 | →ALL |

34. **Fast_Transmission** | WAL losses bypass delinquency pipeline → direct to P&L. Standard leading indicator methodology (watch 30-89 → predict noncurrent) works for OZK but NOT for WAL. Cantor fraud = the pattern, not the exception. | FDIC geographic analysis | B1 | ASSESSMENT | ACTIVE | — | →ALL | Core thesis differentiator from OZK

35. **OZK_Complement** | OZK = reservoir (stress accumulates, maturity wall forces recognition). WAL = fast-transmission (episodic, sudden). Different mechanisms → complementary paired trade. Different put expiry logic. | Cross-bank analysis | B1 | ASSESSMENT | ACTIVE | — | →ALL |

### GROUP: JEFFERIES (Vector 2 — Double-Pledging / Intermediary Chain)

36. **Jeff_Chain** | Private credit fund stress → Jefferies/Barclays as intermediaries → WAL as lender to intermediaries. If Jefferies flags credit provisions, WAL contagion narrative reignites. | Bloomberg, thesis analysis | B1 | ASSESSMENT | ACTIVE | 2026-04-30 | →V2 | Chain logic — needs Jefferies Q1 data to confirm

37. **SMFG_Acquisition** | SMFG signaled intent to acquire up to 20% of Jefferies. Japan deepening US credit exposure at peak stress. SAM/ZHAO crossover. | Bloomberg via @kshaughnessy Mar 21 | A2 | EMPIRICAL | ACTIVE | 2026-06-30 | →V2,SAM |

38. **Convergence_Day** | WAL -10.64% on Feb 27, 2026 ("Convergence Day") on ZERO firm-specific news. Pure vulnerability premium. Market already pricing systemic risk. | Market data | A1 | EMPIRICAL | ACTIVE | — | →V2 |

39. **Madison_Bankruptcy** | Madison Small Cap Fund sold WAL explicitly citing "bankruptcy risk." | Madison fund commentary | A2 | EMPIRICAL | ACTIVE | — | →V2 | Institutional money naming the risk

40. **Jeff_Q1_Signal** | Jefferies Q1 (Mar 25 after close) = first Wall St look at troubled credit markets + ME war impact. Bloomberg framing as bellwether. | Bloomberg Mar 21 | A2 | EMPIRICAL | ACTIVE | 2026-03-26 | →V2 | STALE TOMORROW — need to pull results

### GROUP: NEVADA_GAMING

41. **NV_Exposure** | Nevada-originated loans estimated 18-22% of consolidated $58.7B loan portfolio. Heavily weighted toward gaming/hospitality. | Analyst estimates + historical geographic disclosures | B1 | ESTIMATED | ACTIVE | 2026-04-30 | | Estimate, not disclosed precisely

42. **Circa_Facility** | WAL = joint lead arranger, book runner, admin agent for Circa Resort $420M senior secured credit facilities. Flagship gaming exposure. | WAL press release / client story | A1 | EMPIRICAL | ACTIVE | — | |

43. **Gaming_Business_Line** | "Western Alliance Gaming" = national business line. Senior secured debt, treasury management, specialized depository for commercial casino + Native American gaming. | WAL annual report | A1 | EMPIRICAL | ACTIVE | — | |

44. **NV_Depression_Survival** | WAL survived 2008-2012 "Nevada Depression." Emerged as consolidator (acquired Western Liberty Bancorp/Service1st Bank, $199M assets, in 2012). Management has cycle experience. | Historical filings, NV Business Magazine | A2 | EMPIRICAL | ACTIVE | — | | Mitigant — experience ≠ current health

45. **Consumer_Crossover** | If consumer discretionary spending collapses (CARL thesis) → Nevada gaming revenues drop → WAL gaming credits under pressure. | Cross-agent analysis | B2 | ASSESSMENT | ACTIVE | — | →CARL | Transmission chain, not yet activated

### GROUP: CAPITAL

46. **CET1** | CET1 ratio 11.0% (late 2025). Above $50B-$100B peer median. But assumes SSFA treatment continues — without SSFA, capital adequacy drops materially. | FFIEC RC-R | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | →V3 |

47. **CLN_Coverage** | Credit-Linked Notes cover $8.1B in residential loans (first-loss risk transferred). Effective coverage: 131 bps (vs 74 bps without CLN). LIMITATION: CLNs cover residential, NOT hidden CRE in C&I (MI3). | WAL annual report | A2 | EMPIRICAL | ACTIVE | 2026-04-30 | | Partial mitigant only — doesn't touch the thesis

48. **Loans_Pledged** | 74% of loans pledged ($23.9B). Worst in SVB/FRC comparison set. | FFIEC Call Report | A2 | EMPIRICAL | ACTIVE | 2026-04-30 | | Depositor subordination risk

49. **Uninsured_Deposits** | Uninsured deposits $11.9B vs ~$10B unpledged assets. Tight coverage. | WAL Call Report | A2 | EMPIRICAL | ACTIVE | 2026-04-30 | |

### GROUP: EARNINGS

50. **Record_Q4** | Q4 2025: EPS $2.59 (+13.6% QoQ, +32.8% YoY). Net revenue $980.9M (+17% YoY, beat by $67M). FY net income $991M (+25.8% YoY). | WAL Q4 2025 press release | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | | Record earnings masking under-reserved fraud + hidden CRE

51. **NPL_Ratio** | NPL ratio 0.85% (Q4 2025), improved from 0.92%. Criticized loans $1.3B, -$73M YoY. Management says criticized peaked mid-2025. | WAL Q4 2025 | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | | Surface metrics improving — doesn't account for MI3 or fast-transmission

52. **NCO_Ratio** | NCO ratio 0.24% FY2025 (vs 0.18% FY2024). Peer avg ~0.32%. Still below peers but rising. | WAL annual filings | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | |

53. **Growth_Trajectory** | Total assets: $70.9B (2023) → $80.9B (2024) → ~$90B (2025). Deposits: $55.3B → $66.3B → $77.2B. TBV/share: $46.72 → $52.27 → $61.29. | WAL annual reports | A1 | EMPIRICAL | ACTIVE | 2026-04-30 | |

### GROUP: MARKET_SIGNAL

54. **Cantor_Reaction** | Oct 16, 2025: Cantor fraud disclosure → WAL stock -10.88%. Market reacts sharply to WAL credit surprises. | Market data | A1 | EMPIRICAL | ACTIVE | — | →V2 | Reaction precedent for episodic events

55. **Convergence_Day_Detail** | Feb 27, 2026: WAL -10.64% on zero firm-specific news. Largest single-day drop without company catalyst. Pure systemic/contagion pricing. | Market data | A1 | EMPIRICAL | ACTIVE | — | →ALL |

56. **Madison_Sale** | Madison Small Cap Fund explicitly sold WAL citing "bankruptcy risk." Institutional money naming existential scenario. | Madison fund letter | A2 | EMPIRICAL | ACTIVE | — | |

57. **Portnoy_Investigation** | Portnoy Law investigating WAL. | Legal press release | A2 | EMPIRICAL | ACTIVE | — | |

58. **May2025_Low** | May 2025 low = $57.08. Current ~$68. Prior cycle bottom. -16% downside to revisit. | Market data | A1 | EMPIRICAL | ACTIVE | — | |

59. **Price_Trajectory** | Parabolic rally $57 (May 2025) → $97 (Feb 2026) = +70%. Distribution at top with heavy volume. Now forming lower highs. | Chart analysis | A1 | EMPIRICAL | ACTIVE | — | | Textbook "selling into strength"

---

## ROW COUNT: 59 rows across 10 groups

## GROUP SUMMARY
| Group | Rows | Vector | Key Fact |
|-------|------|--------|----------|
| HIDDEN_CRE | 7 | V1 | MI3 24.2% GROWING, 474% CRE/Tier 1 |
| SSFA | 6 | V3 | $17.2B at 20% RW, $1.1B capital savings |
| CANTOR_FRAUD | 9 | V2 | $98M exposure, 30% reserved vs ZION 83% |
| INSIDER | 7 | ALL | CFO swap = JPM FIG crisis banker |
| GEOGRAPHIC | 6 | ALL | SF NCO highest + pipeline lowest = fast-transmission |
| JEFFERIES | 5 | V2 | Double-pledging chain, Convergence Day |
| NEVADA_GAMING | 5 | — | 18-22% NV, Circa $420M, consumer crossover |
| CAPITAL | 4 | V3 | CET1 11.0% assumes SSFA, CLN doesn't cover MI3 |
| EARNINGS | 4 | — | Record Q4 masking under-reserved fraud |
| MARKET_SIGNAL | 6 | ALL | -10.88% and -10.64% reaction precedents |

## NOTES FOR PASS 2
- All dates should be 2026-03-25 (extraction date)
- IDs: KB-WAL-001 through KB-WAL-059
- Stale_By: most Q4 data stales at Q1 earnings (~Apr 21)
- DerivedFrom: populate cross-references during TSV formatting
- Jeff Q1 results (row 40) will be stale by next session — pull and add rows
- Consider splitting CANTOR_FRAUD into CANTOR + PROVISIONING if it grows
- ZION comparison (row 15) could also live in a PEER group — keep in CANTOR for now
- Rows 34-35 are pure assessment/framework — flag as FRAMEWORK epistemic type?

---

## HANDOFF
**Last context:** WAL KB Pass 1 COMPLETE. 59 rows extracted across 10 groups. All source files consumed. Staging list in SCRATCH ready for Pass 2 (TSV formatting).
**Next session (Pass 2):**
1. Read this SCRATCH → convert staging list to KB.tsv (13-column TSV)
2. Write KB_INDEX.md (group navigator with vector mapping)
3. Update WAL/INDEX.md with row count + group count
4. Update WAL/STATUS.md "What's Changed"
5. THEN: pull Jefferies Q1 results (row 40 is stale)
