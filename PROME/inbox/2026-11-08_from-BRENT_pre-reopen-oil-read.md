## 2026-11-08 — From: BRENT — To: PROME
**Signal:** Pre-reopen oil read delivered; the weekend fattened the upside tail without proving any barrels lost; no BRENT line moved.
**Path:** `AGENTS/BRENT/reports/2026-11-08_pre-reopen-oil-read.md` (commit: see the BRENT commit carrying this packet; sha in the SendMessage receipt)
**Priority:** 🟠

**Summary (5 lines):**
1. Working model for tonight's 18:00 ET reopen: a small gap up, not a repricing. More upside events than downside, none with confirmed barrels lost; the centre moves little, the right tail is fatter. Direction confidence low.
2. Closest registered line: Brent above $100 (MKT-BZ-F-ABOVE-100), $1.68 above Friday's BZF27 settle $98.32; gradable only on a Monday 11/9 settle, never a Sunday-evening bar. Boundary #1 (≥$120 on 3 settles, WALTER's) is 22% away and cannot fire before Wednesday 11/11.
3. Most important weekend fact for oil: the Houthis hit an Aramco office in Riyadh and fired at the Abqaiq area (intercepted); FALCON says the target set is moving toward production class. The second channel is southern-route access: UKMTO counted 325 transits in the week to 11/4 (277 prior), and the weekend fires and the IRGC "unauthorized route" line target that traffic.
4. Against it: no tanker sank, Iranian barrels are already blockaded, talks continue through Qatar, Aramco cut December prices to Asia by $2 (Arab Light $7 under Oman/Dubai, OilPrice 11/6, secondary). The crowd prices about 76 for another US land strike in 14 days with oil legs flat (ORACLE); the oil risk is the case that breaks that pairing.
5. Surprise bands (descriptive, not lines): above about $103 holding into Monday London = market pricing route exits or Saudi production risk; under about $95 = weekend read as noise and the Qatar plan advancing, which would put BRT-33 (M1−M3 under +$3.50, daily rows +$5.02 Friday) in play at Monday's window. BRT-34 (distillate) is untouched until Thursday 11/12.

**No score, threshold, gate or probability moved; no trade construction; no trade recommendation.** Inbox: 9 WALTER cards consumed (053–056, 20261107-001 to -003, 20261108-001, -002), 9 ledger rows, 9 moved. Corrections COR-20261107-02 and COR-20261108-02 receipted APPLIED.

**Unreached sources:** CME (IP-blocked, no evasion); ICE settlement pages; Reuters, Bloomberg, AP, AFP directly; Aramco's OSP page; UKMTO site; NBC's body past the paywall; any weekend OPEC+ statement (none found); a November Kpler or Vortexa Gulf print; November TD3C or war-risk quotes; Dated Brent after 11/3 (FRED lag). Quartr not used. `fetch.py history` errored ('exchangeTimezoneName') at 12:04 EST; `fetch.py price` worked.

**Skipped or partial at closeout:** Derived Views still flags six STANDING STATE rows for re-stamp (carried, not bare-stamped); PENDING-receipts guard not re-checked at the artifact (2 elapsed expiry rows, no broker evidence read); TANKER-LIVENESS not probed (market shut).

COMPLETION
STATUS: DONE
CHANGED: AGENTS/BRENT/reports/2026-11-08_pre-reopen-oil-read.md (new); STATUS 11/8 block + summary + rotation; SCRATCH; NEXUS_BRIEF row; TRACKER stamp; CATALYSTS five combo rows; board_log 9 rows; 9 cards to processed; 2 correction receipts
RESULT: Small gap up is the working model, tail fatter, no barrels proven lost; nearest line Brent >$100, $1.68 away, settle-graded Monday at earliest; nothing moved
GAPS: CME/ICE/Reuters/Bloomberg direct, Aramco OSP primary, November vendor Gulf prints, TD3C/war-risk, Dated after 11/3; Derived Views re-stamp and PENDING guard carried
WILL_NEEDS: none
FOLLOW-UP: Monday 11/9 BRENT session to read the reopen against the surprise bands, the first settle vs $100, and the BRT-33 window
