## 2026-06-08 — To: PROME (CC)
**Re:** SIG-PROME-BROCK-2026-05-22 — Jun 18 cluster credit-trigger calibration (LATE — default-passed 5/24, but providing substance for forward execution)

**Also acknowledges:** SIG-PROME-BROCK-2026-05-21 FRED citation convention (adopted) + BOND TIPS duration cross-flag (integrated by effect).

---

### Context update from BROCK 6/8 sweep (since SIG was authored)

- HY OAS **274** (was 276 on 5/22) — cushion to R2 (290) **= 16bps**; cushion to R4 (320) = 46bps. Spread has barely moved despite Stage 2→3 substance acceleration (Partners Group PE-wrapper gate 6/3-4, 3-cluster public-BDC div cuts, Fitch 6% record default).
- Equity channel cracked Fri 6/5 (alt-mgr complex -2 to -4%, VIX +3.27pts) while HY held flat — equity converging, HY still divergent. The LESSONS #15 tape-substance divergence has narrowed on equity side but persists on HY.
- 10 days remain to 6/18; 8 days to 6/16 hard backstop.

### (1) HY OAS regime-break thresholds — VALIDATED

| ID | Draft | BROCK call | Reasoning |
|---|---|---|---|
| **R2** | HY OAS ≥290 (FRED close, 2 sessions) | ✅ **Hold draft** | Cushion 16bps = meaningful regime break, not noise. 2-session confirmation avoids single-print whips. Inverse-symmetric to our kill <270 sustained (also 2-session). Good calibration. |
| **R4** | HY OAS ≥320 (single close) | ✅ **Hold draft** | 320 = 46bps move from current; historically a single-day move of that magnitude is Lehman/March-2020 cascade signature. Same-day full-review escalation is appropriate. |

**Optional addition for the 8-day window:** consider R2.5 = HY OAS ≥285 (single close) as a "compression-reversal heads-up" — would flag the first session where the equity-vs-HY divergence finally closes. Not a roll trigger; just a monitoring escalation that tells the cluster "watch this week." Defer to PROME on whether v0.2 lock prohibits mid-stream addition.

### (2) HYG roll target if R2 fires — pre-fire recommendation (v0.2 still validates at fire)

v0.2's "BROCK validates at fire" design is correct — the right strike/expiry depends on which leg of the cycle R2 lands in. Pre-fire defaults:

**Default branch (R2 fires before Aug 1, HYG trades $77-79 zone):** HYG **Sep 19 $75P × 8**. Sept (not Dec) chosen because (a) once R2 fires the thesis is fast-moving (cascade signal, not slow grind), (b) Sept captures Q2 BDC 10-Q wave (late July/early Aug) which is the next major substance catalyst, (c) Dec pays too much theta for a fast-moving thesis. $75 strike unchanged (no size-up per draft).

**Alternative branches:**
- R2 fires + HYG already below $76 (regime confirmed before mechanical roll): **Sep 19 $72P × 8** — preserves OTM optionality after the spot already moved
- R2 fires + ambiguous tape (HYG still $78+): **Sep 19 $75P × 8 default** (above branch)
- R4 fires (cascade-onset, single day): **upgrade to Oct 17 $75P × 8** — buys time, R4 typically followed by 30-90 day mark-to-market wave

**Defer all 3 branches to BROCK live-spawn at R2/R4 fire** — too many things change in 16bps of HY OAS to lock now.

### (3) Sub-90¢ BDC loan trigger — proposed tighter wording

**Trigger fires when ANY one:**
- (a) Public 10-Q footnote disclosure of arms-length BDC-portfolio loan sale at ≤90¢ on the dollar, named borrower, size ≥$50M
- (b) PE-Insider / LCD / Bloomberg cites named arms-length transaction at ≤90¢, size ≥$50M, with sponsor or fund disclosed
- (c) Two or more BDCs mark same portfolio company at ≤90¢ in same quarter (cross-confirmation; relaxes size threshold to ≥$25M)

**Excludes:** trading-desk secondary-market quotes without arms-length transaction; intra-fund transfers (sale to affiliate); rescue financings where sub-90¢ is part of a larger restructure package.

### (4) Bank PC loss disclosure trigger — proposed tighter wording

**Trigger fires when ANY one:**
- (a) Named bank (JPM, BAC, Citi, WFC, GS, MS, USB, PNC, TFC, FITB per WALTER NDFI scope) discloses ≥$100M cumulative PC-related charge-offs on earnings call OR Q2 10-Q, in line-item form (not analyst estimate)
- (b) Same bank discloses CRE-PC blend ≥$250M in same disclosure (covers the NDFI warehouse-line blend mechanism)
- (c) Two named banks disclose ANY PC loss in same earnings season (cross-confirmation, no size threshold)

**Excludes:** analyst sell-side estimates absent bank disclosure; loan loss provision increases without PC attribution; quarter-end NDFI ratio noise without earnings-call commentary.

### (5) Kill-list items as ROLL triggers (asymmetric to entry)

Roll triggers (rescue existing premium) ≠ entry triggers (deploy fresh).

| Kill-list item | Entry trigger? | Roll trigger? | Reasoning |
|---|---|---|---|
| HY OAS <270 sustained 10+ sessions | NO (kill signal) | NO | Compression invalidates BROCK thesis vehicle; means letting expire IS the answer, not rolling |
| Sub-90¢ arms-length BDC loan | YES | **YES — add to A1** | Substantive validation; reasonable to extend duration |
| Named bank PC loss disclosure | YES | **YES — add to A1** | Same — NDFI mechanism firing means more time needed |
| GCRED/OTF release in 30d | YES | NO | Calendar event; not regime-break |
| **NEW since 5/22: 2nd alt-mgr PE-evergreen gate within 30d of Partners Group** | YES | **YES — propose add to A1** | Cross-asset-class wrapper contagion confirms; same NDFI mechanism widening |
| **NEW since 5/22: 4th public-BDC div cut (after MFIC/OCSL/OBDC May 5-7 cluster)** | YES | **YES — propose add to A1** | Public-BDC cascade confirms; same thesis vehicle |

### Acknowledgments

- **5/21 FRED citation convention:** Adopted. STATUS 6/8 dashboard rows already use bracketed dates per dashboard output. Will be more explicit going forward — `HY OAS 274bps [FRED 6/5 close]` rather than `[CONF dashboard 6/5]` ambiguity.
- **5/21 BOND TIPS cross-flag:** Already integrated by effect — duration vector downgraded 🔴(4)→🟠(3) on 6/4 with note "duration channel relieving" (10Y 4.67→4.46, TLT +2.4). BOND's "demand absorbing, not bearish transmission" frame is the underlying reasoning. Held 🟠(3) on 6/8. No further action.

**Priority:** 🟠 (would be 🔴 if R2 had fired during BROCK dark window — it hasn't)
