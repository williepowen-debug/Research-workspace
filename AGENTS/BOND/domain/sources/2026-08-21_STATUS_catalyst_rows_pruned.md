# BOND STATUS — catalyst twin rows pruned at the 2026-08-21 audit

**Pruned per closeout step 12 (~1-week retention for FIRED rows).** Both were resolved with their outcomes recorded, and both are ALSO pruned from `docket/CATALYSTS.tsv` in the same commit — **the twin must not diverge from the docket in event SET, so a one-sided prune would have re-broken the parity fixed earlier the same day.**

⚠️ **Pruned by explicit ROW, not by date-key.** LABOR silently deleted rows in August by keying a prune on a date; the two rows below were read, verified fired-with-outcome, and are reproduced verbatim before removal.

**Substance is not lost:** the refunding grade is `KB-BND-136` and the archived pre-registration block; the QRA content (Q3 froze coupon sizes, signal did NOT fire) is carried on the live Exit/Falsification and in the docket's successor 11/4 row.

---

## 8/05 Q3 QRA (16 days past)

| ~~Wed 8/5~~ ✅ **CONTENT ESTABLISHED** | **Q3 QRA — the registered signal did NOT fire** | ✅ **RECONCILED WITH THE DOCKET 2026-08-21.** **The Q3 QRA FROZE coupon auction sizes** (marginal financing dollar → bills), per the TBAC presentation primary (`TreasuryPresentationToTBACQ32026.pdf`, consumed at the 8/19 WAM grade). The registered signal — **coupon UPSIZING = term-premium supply shock — did NOT fire.** Next QRA **11/4**, Treasury-stated in `sb0607` (F1/F3 checkpoint). ⚠️ **What survives is the PROCESS defect, not a data gap:** the 8/5 *date* was pattern-inferred and never primary-verified before the window — n=2 of the unverified-date class. 🔴 **This cell read "still UNVERIFIED … do not grade anything off it until it is" for 16 days AFTER the content was established at two primaries** — the twin was telling readers to discard a load-bearing supply fact the docket already held. |

## 8/11–8/13 August Quarterly Refunding (10 days past)

| ~~Tue 8/11 · Wed 8/12 · Thu 8/13~~ | **AUGUST QUARTERLY REFUNDING $125B** | ✅ **GRADED 8/18, FIVE DAYS LATE — NO COMPOSITION FAILURE AT ANY TENOR.** 3Y BTC 2.71 / ind 64.24% / dlr 11.74% · 10Y BTC 2.53 / **ind 76.73% (+8.41pp vs median, 2nd-strongest of its trailing-12)** / dlr 8.60% · 30Y BTC 2.39 / ind 66.85% / dlr 11.51%, clearing **5.216%** — ⚠️ *"highest 30Y auction yield since 2001" is **wire-level and NOT verified at my primary**: my TreasuryDirect corpus reaches 2023, so the 2001 window is outside what I can compute. Cite it as a wire claim, never as a BOND figure.* The 30Y clears its own failure bar by **7.33pp**. **12th straight benign resolution.** ⚠️ **This event was never docketed — the quarter's largest supply event ran ungraded while the desk was dark.** Full grade → the AUGUST REFUNDING section above. |

---

## The matching `docket/CATALYSTS.tsv` rows, pruned in the same commit

*(TSV, verbatim — restore by re-appending if either event is ever re-opened.)*

```
2026-08-05	Quarterly Refunding Announcement — ✅ **CONTENT NOW ESTABLISHED AT PRIMARIES (2026-08-19), 14 days late:** the Q3 QRA **froze coupon auction sizes** (marginal financing dollar → bills), per the TBAC presentation primary (`TreasuryPresentationToTBACQ32026.pdf`, consumed via the 8/19 WAM grade) — the registered signal (coupon UPSIZING = term-premium supply shock) did NOT fire	Coupon-size guidance change	NOT FIRED — coupon sizes frozen, no upsizing. sb0607 (8/19, separate action) also confirms: *next* Quarterly Refunding is **11/4** (stated in the release), which becomes the standing QRA date row (F1/F3 checkpoint, see rows 8/8b).	🟠	BOND,LIQUID	Process record retained: the 8/5 date was pattern-inferred, never primary-verified before the window, and the miss stands as n=2 of the unverified-date class — the discharge here is of the CONTENT (via two primaries consumed 8/19), not of the process defect. 11/4 QRA date is Treasury-stated in sb0607 = verified at primary at docketing, breaking the class for the successor row.	confirmed

2026-08-11	**AUGUST QUARTERLY REFUNDING 8/11-8/13 ($125B) — GRADED 2026-08-18, FIVE DAYS LATE**	3Y 91282CRG8 $58B / 10Y 91282CRF0 $42B / 30Y 912810UW6 $25B, composition vs each tenor's own trailing-12	RESOLVED — NO COMPOSITION FAILURE AT ANY TENOR	🔴	BOND,LIQUID,ZHAO,HENRY	**THIS ROW DID NOT EXIST UNTIL 8/18 — the largest supply event of the quarter was never docketed and ran ungraded while the desk was dark.** Graded off TreasuryDirect primaries (all pct of COMPETITIVE ACCEPTED): 3Y BTC 2.71 / ind 64.24 (+1.28pp vs med) / dlr 11.74 (below med) · 10Y BTC 2.53 / ind 76.73 (+8.41pp vs med, 2nd-strongest of its trailing-12) / dlr 8.60 · 30Y BTC 2.39 / ind 66.85 (+1.92pp) / dlr 11.51, clearing HY 5.2160pct = HIGHEST 30Y AUCTION YIELD SINCE 2001. The 30Y clears its own composition-failure bar by 7.33pp on indirect. 12th straight benign resolution; 'expensive not broken' passed the hardest supply test of the quarter. ALSO converts the FR2004 -9.3B week-to-8/05 drawdown from assumption to finding: dealers cleared balance sheet AHEAD of this supply, which then cleared into firm end-user demand => BENIGN DISTRIBUTION. Two honest limits: it is a 5-day-late reconstruction, and the trailing-12 windows span a repricing regime so the BTC comparisons (clearing by 0.01-0.07) carry no weight on their own; only the composition margins do.	confirmed
```
