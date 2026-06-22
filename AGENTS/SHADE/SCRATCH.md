# SHADE SCRATCH.md — Ephemeral Session State
**Rewritten:** 2026-06-21 ET (first live SHADE boot — Opus 4.8 ultracode) · **6/22 addendum below**

## 6/22 ADDENDUM — FABN maturity ladder built (Will-requested)
Built the Athene FABN/funding-agreement ladder → `research/ATHENE_FABN_MATURITY_LADDER_2026-06-22.md`. **Headline:** the ~$16.5B "2026-2027 FABN wall" anchoring kill-path-1 is **third-party/UNVERIFIED** — Athene Global Funding is **not an SEC filer**, **100% of the $34.5B FABN is 144A/Reg S**, and **no public FABN-only maturity ladder exists** (the only year-bucketed primary figure blends all annuities+FA+GICs, undiscounted). Re-marked everywhere (STATUS §0/§2/dashboard/calendar/next-actions; CLAUDE.md target sheet + kill-path-1 line). **Mechanism confirmed & sharper:** Q1'26 FABN gross issuance collapsed to **$2.0B vs $13.4B FY2025** ("challenging market conditions" per 10-Q MD&A), ~9-10mo since last public syndication, substitution into encumbered FHLB(+$4.9B QoQ)/FABR, ~14 tranches confirmed clustering 2026-H2/2027, **active 2027 tenders** (series 2022-6 $260.1M, 2020-5 $238.1M, dated 6/22). Verified stack: FABN $34.5B + FABR $21.5B + direct $6.1B + FHLB $28.2B + LT repo $3.2B = **~$93.5B gross**. Spread obs-date note: T+123 (May) vs T+105 (Feb) = ~+15bp peer-penalty widening. **Kill-path-1 held YELLOW** (refinance-at-wider-spread, not rollover failure). Next: close the quantum gap via NPORT-P holder CUSIPs (no terminal needed). Commit pending.

## CHANGES SINCE LAST SHADE SESSION
Prior session = 2026-06-15 Prome architecture + live-refresh pass (STATUS rebuilt as 🟠 structural/latent). This 6/21 session is the **first agent-run SHADE boot** against that scaffold. Did NOT pull at boot — working tree had uncommitted changes outside SHADE (`memory/auto/`, `LIQUID/inbox/`), so booted off the current tree per git protocol.

Cross-agent picture (their 6/20 surfaces are fresher than the 6/15 STATUS was):
- **BROCK 🔴🔴 (6/20):** fund stress firmed bear — KBRA DLD 2.3% record-match + raised 3.5% end-26 forecast; Fitch BDC Q1 (6/19) NAV −2%, non-accruals up, 11 BDCs cut Q1 divs. **Wrapper-equity recognition began** (FSK −5.9%, ARCC −4.1% vs HYG flat). APO held $137.50. HY OAS 263 [6/17]. **Fed turned hawkish 6/17.**
- **LIQUID 🟠 (6/20):** HY OAS 263 = 3bps from 260 soft-kill, no trigger; CCC-BB tail-gap wide (783). "Bear grinding the wrong way, risk-on overwhelming."
- **REGINALD (6/20):** CRE-DQ tier-wide leading creep; Iran/Hormuz **re-escalated** 6/20.

## WHAT I DID
1. **WALTER intake:** created `board_log.tsv` (v0.2 header); processed `SIG-W-20260619-008` (S-FL distress deep-research, INFO role — CORAL owns action) → disposition `noted`; `git mv` to `inbox/WALTER/processed/`. SHADE takeaway logged: FL commercial/condo rate hardening (+18.8% indicated, NOT easing while wholesale eases −15-25%) = cost-push input; condo-master/association exposure undisclosed in FL bank filings = visibility gap.
2. **Ran a 5-vector domain sweep** (Workflow, 11 agents, adversarially verified) of the 6/15→6/21 gap → `research/SHADE_BOOT_SWEEP_2026-06-21.md`. Net = **relief/clock-advance, not breach.**
3. **Rebuilt STATUS** with a top-of-file §0 verified boot-delta (net read + threshold table + 2 retractions), corrected the FHLB scale gap, added the FABN-spread canary + AMAPS update + Egan-Jones + NAIC direction-flip + systemic-commentary blocks, updated the dashboard / calendar / watchlist, and re-marked the stale APO band. STATUS = 203 lines.

### Key verified deltas (full list in research file)
- **Reg-capital eased:** NAIC CLO RBC slipped past 6/15 gate (YE2026 at-risk, YE2027 fallback); **MM-CLOs deferred to 2027** (resolves the MML-applicability OPEN item = NO for 2026); FSOC SIFI bar raised; small offset = 2026-05-CA collateral-loan look-through removed (5/14); SVO discretion not operationalized.
- **Funding canary:** Athene 5Y FABN secondary **T+123 = +43–48bp peer-relative penalty** (widest of large IG insurers); **no syndicated FABN since Sept 2025 (~8mo)**; **FHLB = $28B drawn / $38B pledged** (the $2.4B was undrawn capacity, not the book); $1.7B Bermuda DTA valuation allowance → adj leverage 25.9%.
- **AMAPS absent** from Athene's May FI deck (Apollo markets it standalone) — disclosure-channel-split watch item.
- **Egan-Jones:** briefing fully submitted, Aug 12 2026 hard-dated docket binary; both tracks GREEN.
- **Surveillance chorus:** Moody's 6/8 ($807B/20% illiquid, top-10=44%, Athene & GA >15%) + Proskauer 2.73% Q1'26 = third default series. No rating actions in-window.
- **RETRACTED:** Nationwide/MassMutual reinsurance was inverted (Nationwide assuming, MassMutual ceding — not captive-hollowing).

## NEXT SHADE SESSION
1. Boot: STATUS → SCRATCH → MEMORY; check `board_log.tsv` + `inbox/WALTER/` for new signals; confirm canonical APO mark with BROCK (do not carry the March band).
2. Substantive audits if decision-relevant (priority order):
   - Athene Asset Compendium / "Affiliated & Related Party Assets" deck → **locate AMAPS** in the Schedule-D/BA equivalent (resolve disclosure-channel split).
   - ✅ FABN ladder done (6/22). RESIDUAL: size the 2026-2027 wall bottom-up via **NPORT-P holder-level CUSIPs** (MS Inst Fund Trust CIK 0000741375, PIMCO Funds CIK 0000810893) — the only free path; or a terminal/cbonds-Pro CUSIP aggregation. Watch for any FABN spread >250bp or a pulled syndication (→ kill-path-1 red).
   - NAIC CLO C-1 Residuals & PAF comment fight (**7/6/26**) + 6/23 webex outcome.
3. Watch the **Aug 12 2026 Egan-Jones** docket binary (defense submitted 6/16); faster enforcement track = watch for a Wells notice.

## OPEN THREADS
| Item | Status |
|---|---|
| STATUS refresh | ✅ live boot-delta added 6/21; threshold table verified |
| FHLB scale correction | ✅ corrected $2.4B→$28B drawn; **REGINALD cross-flag held (see Mail state)** |
| FABN peer-relative canary | 🟠 yellow-leaning on kill-path-1; absolute spread still green |
| AMAPS disclosure-channel split | 🔴 watch; needs Asset Compendium pull |
| Athene FABN maturity ladder | ✅ built 6/22; **$16.5B re-marked third-party/UNVERIFIED** (no public ladder, 100% 144A/RegS). Quantum gap → NPORT-P holder CUSIPs next. |
| NAIC CLO RBC slip | 🟡 7/6 comment + 6/23 webex; YE2026 at-risk |
| Egan-Jones Aug 12 | 🟢 calendar binary; defense submitted |
| Oaktree/Atlantic Coast Life captive | 🟡 new captive-reinsurance sub-watch |
| NEXUS_BRIEF | 🟡 still not created; defer to next architecture pass |
| boot.py / automated data | 🟡 not built; manual boot. (Note: `yfinance` not installed in venv — local fetch.py price cmd fails.) |

## Mail state
- `inbox/WALTER/`: empty (008 processed). `board_log.tsv` now exists.
- Top-level `inbox/`: old Mar–May signals untouched (process only if spawned for triage or needed for an audit).
- **Cross-agent signals WRITTEN to recipient inboxes (Will-authorized 6/21; recipients inactive):**
  - `AGENTS/REGINALD/inbox/SIG-SHADE-REGINALD-20260621-athene-fhlb-28b-drawn.md` — Athene ~$28B FHLB advances drawn / $38B pledged (corrected from the $2.4B *undrawn capacity*); insurer secured-funding for REGINALD's FHLB/NDFI radar.
  - `AGENTS/LIQUID/inbox/SIG-SHADE-LIQUID-20260621-athene-fabn-funding-canary.md` — FABN 5Y T+123 = +43–48bp peer penalty; ~8mo no syndicated issuance; kill-path-1 canary. (LIQUID had no FABN/Athene coverage in STATUS.)
  - `AGENTS/BROCK/inbox/SIG-SHADE-BROCK-20260621-moodys-insurer-illiquidity-quant.md` — Moody's 6/8 $807B/20% illiquid (Athene & GA >15%) + Proskauer 2.73% offered to his default-index set. (Trimmed: BROCK already has NAIC deferral / AMAPS / wrapper-equity / KBRA-Fitch.)
  - These files live OUTSIDE `AGENTS/SHADE/` → SHADE did **NOT** commit them (git-isolation rule). Recipients commit at their next boot, or Will sweeps them in a coordinated push.
