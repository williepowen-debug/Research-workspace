---
name: finding_cftc_cot_raw_file_beats_socrata_lag
description: "CFTC COT Socrata API lags the 3:30 ET website post 15-60min; grade off the raw f_disagg.txt instead, verifying report-date in-row and reconciling the anchor via the ΔMM change columns."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5bff1e6c-8c5e-4af4-aab5-30be5323a69f
---

On COT-release Fridays the CFTC **Socrata dataset (publicreporting.cftc.gov/resource/72hh-3qpy.json) lags the 3:30 PM ET website post by ~15-60+ min** — it can stay showing last week's report-date well past 3:45. A gate that keys on Socrata report-date (e.g. BRENT's `cot_grade.py`, which correctly exits 3 on a stale row) will refuse to grade for that whole window. Verified 2026-07-17: 40 poll attempts over 15:17-15:45 all still returned 7/7 while the 7/14 print was already live elsewhere.

**The live path: CFTC's raw text files are posted AT 3:30, before Socrata.** For the disaggregated futures-only report (Managed Money etc.), fetch `https://www.cftc.gov/dea/newcot/f_disagg.txt` (User-Agent header required, `[[finding_edgar_403_user_agent_header]]`). For legacy futures-only (SAM's JPY leg) use the deacot/deafut file. Parse by CSV field index:
- field 2 = report_date `YYYY-MM-DD` (**verify == expected in-row — keep the report-date discipline even on the manual path**)
- field 13 = M_Money_Positions_Long_All · field 14 = M_Money_Positions_Short_All · field 15 = spread
- field 61 = change_in_M_Money_Long_All · field 62 = change_in_M_Money_Short_All (WoW)

**Anchor-reconcile before trusting the mapping:** base(prior week) + ΔMM-change-column = current-week level. 2026-07-17 WTI-PHYSICAL: 129,072 short + (−9,885) = 119,187 ✓ / 193,113 long + (−11,952) = 181,161 ✓ — confirms fields 14/62 and 13/61 in one step. This is the same reconciliation SAM ran on the legacy file. Cross-agent: BRENT (disaggregated) + SAM (legacy) both did it the same day.

Don't wait out the API; grade off the raw file with report-date + anchor checks. Related: `[[finding_verify_live_api_schema_over_docs]]`, `[[finding_fail_loud_on_incomplete_data]]`.
