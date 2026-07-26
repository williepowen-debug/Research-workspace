# OTTO STATUS — archived boot-pointer blocks (line-cap pass 2026-07-25, session 016)

Archived from `STATUS.md` when the file hit the ~250-line cap. These are the **session 015 (Jul 4)** and **Jun 9 / Jun 8 / Jun 2** boot-pointer narratives. Resolved outcomes live in STATUS § CRITICAL TIMELINE; thesis pivots in `thesis/CHANGELOG.md`; structural history in `MAINTENANCE.md`.

---

> **📌 Session 015 (Jul 4, same-day follow-on — P2 primary-source pass):** (1) **2022-vintage 10-D pull `[CONF SEC 10-D]`** — the "2022 vintage" is bifurcated ~2.3x by tier: DEEP subprime (Exeter EART 2022-3 **27.58%** / 2022-2 26.34%) already >25% & grinding to ~28-29% terminal; BROAD subprime (Santander SDART 2022-6 **12.08%**) nowhere near. Fitch blended index (22.42%) is a composition average anchored DOWN by Santander's dominant $2B+ deals → **OTTO-04 68→62%**; deep-subprime magnitude leg CONFIRMED but the blended-index metric may falsify-on-technicality (→ CHANGELOG session-015 entry). (2) **Fitch "May print" = March data** (2mo lag) — confirms prior figures, no summer re-deterioration visible yet; 3 stale-vintage traps (2023/24/25) avoided. (3) **ML.tsv CRLF-corruption REPAIRED** (182 clean rows → MAINTENANCE). All committed local. — *Jul 4 catch-up pointer below.*
>
> **📌 New spawn (Jul 4 catch-up sweep — 25-day dark, Jun 9 → Jul 4):** A full catalyst cluster fired unswept while OTTO was dark. **Resolved this session (primary-sourced):**
> - **OTTO-05 FALSIFIED** — subprime BBB ABS spread did NOT hit 250bps; it **TIGHTENED to +140bps** (EART 2026-3 Class D, settled ~Jun 24 `[CONF SEC FWP/IFR]`) vs +190 in Mar. Deal upsized to $1.2bn; Exeter earned 1st-ever AAA. **The "systemic subprime-ABS funding freeze" sub-thread is disconfirmed** — primary market open + tightening. Fraud-case leg (Tricolor/FBG) is idiosyncratic, not a broad-market repricing.
> - **OTTO-28 FALSIFIED-on-window** — Ally Q2 prints Jul 21 (after Jun 30 resolve); Q1 had no Carvana break-out. And Ally credit is *improving* (retail NCO 1.97% −15bps YoY; 30+ DQ 4.60% −17bps YoY, 4th straight qtr) — prime/near-prime improving vs deep-subprime bleeding = Invisible-Exit-consistent bifurcation.
> - **OTTO-32 HOLDS 85%** — Jun 12: UST convert-to-Ch.7 motion NOT granted; reformulated plan pays admin claims in full; **DS conditionally approved**; **confirmation moved to JUL 28** (new operative resolver). Plan still routes 111/112 debtors → Ch.7 — majority-Ch.7 branch on track inside Sep 30.
> - **OTTO-04 nudged 75→68%** — spring tax-refund bounce softened the monthly Fitch series (recovery up to 37.48%); makes the ~24.3-24.5% Sep-30 projection less likely to cross 25%.
> - **Carvana quiet** — CVNA $68.60 (+7% off $64 Jun 5) despite CFO insider selling; no new short report (Gotham's was Jan 28). The "Jun 12 Discovery Production 2" catalyst was a **phantom** (never independently confirmed — WINTERKORN was right); retired from docket.
> - **Signal downgrade 🔴🔴 → 🔴/🟠 split:** fraud-pattern leg intact & grinding; systemic subprime-ABS-funding leg took two disconfirming hits. **⚠ Private-credit / BDC dashboard rows below are Feb–Apr stamped and were NOT refreshed this session — do not cite as current.** Docket swept + rebuilt; WINTERKORN weekly run due (Tue).
> - **Inbox processed (Jul 4):** PROME PAT-035 task-packet actioned — **TRADE.md FROZEN** (no active OTTO position; Feb-vintage ideas stale/disconfirmed) + `--trade` staleness boot-line wired into boot.py. 2 WALTER signals integrated (Hertz −41% used-car weakness + record 5.6% aggregate auto DQ) — both **corroborate the summer-re-deterioration watch** (OTTO-04); logged ML-180/-181, no threshold trip. — *Prior boot-pointer (Jun 9) below.*
>
> **Jun 9 session = thesis/ consolidation + WINTERKORN sub-agent (CLAUDE.md → v2.7):** new docket-steward sub-agent at `docket/WINTERKORN.md` + `docket/WINTERKORN_MEMORY.md` (FASTOW-pattern scoped owner of CATALYSTS.tsv; weekly Tue + T-3 pre-hearing cadence). Closes the Jun-17→Jun-12 date-keeping failure mode on cadence. **Jun 12 is the canonical first-spawn target** (First Brands UST hearing pre-fire verification). Earlier in same session — thesis/ consolidation (CLAUDE.md → v2.6): built `thesis/` subdir; new `thesis/THESIS.md` v1.0 (12-section canonical thesis — Primary Cockroach, Secondary Invisible Exit, Carvana sub-thesis carve-out, transmission chain, why-now timing claim, conviction decomposition, expanded risk matrix); moved `CHANGELOG.md` → `thesis/CHANGELOG.md` + `workbook/PREDICTIONS.tsv` → `thesis/PREDICTIONS.tsv` (scripts updated); new `thesis/PREDICTIONS_ARCHIVE.md` (5 resolved-row post-mortems + calibration scoreboard — knocks STALE_PUNCHLIST #4-5). STATUS § THESIS block now mirror-only (canonical → `thesis/THESIS.md`). **No domain-data refresh — dashboard metrics unchanged from Jun 8 sweep.** Prior context — **Jun 8 = boot+closeout infra maturation (v2.3):** boot kit added (`scripts/boot.py` + `docket/CATALYSTS.tsv` — boot steps 4-5 now script-driven, ~2s); closeout matured toward SAM/BRENT — STATUS line-cap+archive (this file 417→162 lines, Mar-May check-ins → `workbook/STATUS_archive_20260608.md`), new `CHANGELOG.md` thesis-pivot log, promotion-scan step, Git section fixed to pathspec. **No domain-data refresh this session — dashboard metrics still Feb-Apr stamped (stale; flagged for next session).** Prior context — **Jun 2 = protocol hardening (v2.1, Phases 1-3b):** new git-pull boot step 0 + past-due-catch calendar scan; closeout rewritten as write-back mirror of boot; new `## Evidence & Hygiene Conventions` (evidence-grade tags `[CONF]`/`[PRESS]`/`[ALLEG]`/`[EST]`, `[STALE]` marking, Doc Ownership table); live-state stripped from CLAUDE.md (STATUS is single source of truth). Cross-doc audit produced **`STALE_PUNCHLIST.md`** (9 items; TRADE.md is headline 3.5-mo rot — remediation DEFERRED). **First Brands sweep resolved the boot-flagged May 20/25/29 catalysts:** May 20 conditional-DS approval DENIED (admin-insolvency grounds, cuts toward thesis); 4 Evolution SPV debtors already Ch.7 (Apr 9); confirmation re-targeted **Jun 17**; OTTO-32 held 85%.


---

## Archived 2026-07-25 (2nd line-cap pass) — superseded Carvana 'thesis patience' block (Jul 4)

### Carvana — 🟡 thesis patience (Jul 4, superseded)
Q4 EBITDA miss, GPU -$255 QoQ. **Stock $68.60 (Jul 4) — +7% off the $64 Jun 5 low** despite continued CFO insider selling (Form 144 Jun 1: Jenkins ~$19.5M/3mo, zero buys); William Blair had *added* CVNA to June conviction list. **No new short-seller report through Jul 4** (Gotham's forensic report was Jan 28; Hindenburg/MW silent). GCR: DriveTime 20x-40x leverage, 73% adj EBITDA = related-party. **The "Jun 12 Discovery Production 2" catalyst was a phantom** — never independently confirmed from public sources (WINTERKORN correctly halted; catch-up searches found no such docket event). Separate DE Chancery Jun 16 dismissal was the *old 2020 direct-offering* case (SLC/Zapata), NOT the related-party/Bridgecrest thread `[PRESS, needs verify]`. Price strength + short-seller silence = re-entry NOT triggered; stay patient.



---

## Archived 2026-07-25 (3rd line-cap pass) — resolved CRITICAL TIMELINE rows, Mar-Jun 2026

| Date | Event | Status |
|---|---|---|
| **Mar 31** | Tricolor vehicle-sale deadline (ORIGINAL — operative) | ✅ Auctions ran; 5,857 sold / $39.5M net (data emerged ~May 14) |
| **Mar 31** | First Brands asset sales (Walbro $50M pending) | ✅ $25M 12-brand sale confirmed |
| **Apr 9** | First Brands: **4 Evolution SPV debtors converted to Ch.7** (Lopez order) — first concrete partial conversion | ✅ `[CONF]` (swept Jun 2) |
| **May 15/18** | First Brands: PMG single-debtor Ch.11 liquidating plan filed (May 15) + Disclosure Statement (May 18); Global Settlement → Litigation Trust; all other debtors → Ch.7 after effective date | ✅ `[CONF]` (operative DS; supersedes earlier "Apr 28 PMG" draft ref) |
| **May 13** | First Brands: US Trustee motion to dismiss-or-convert all FBG cases to Ch.7 | 🔴 PENDING — contested into Jun 17 hearing `[CONF]` |
| **May 20** | First Brands: Disclosure statement conditional-approval hearing | ✅ **DENIED** by Judge Lopez — creditor-rights + admin-insolvency grounds (UST argument landed); ordered parties to keep negotiating `[CONF]` (swept Jun 2) |
| **May 22/25/29** | First Brands: litigation-trust bid deadline / omnibus / debtor-requested combined confirmation hearing | ✅ Superseded — May 20 denial reset timeline; no confirmation occurred; re-targeted to Jun 17 `[CONF]` (swept Jun 2) |
| **Apr 24** | Trustee Rule 2004 motion vs Tricolor affiliates + Fifth Third supplemental motion (contents opaque) | 🟠 |
| **May 5** | CVNA stockholder vote: split PASSED (5-for-1, eff. May 7-8); chairman separation FAILED 96%; GT ratified | ✅ |
| **May 7** | PSEC declares $0.035 monthly div (down from $0.045) — Q3 FY26 earnings | ✅ |
| **May 12** | NY Fed Q1 2026 HDC published — auto $1.685T, transition 2.97% flat | ✅ |
| **May 14** | Trustee Rule 2004 motion vs ACV Capital LLC | 🟠 fraud surface expansion |
| **Jun 12** | Carvana discovery production 2 | ✅ **PHANTOM** — no such docket event independently confirmed (swept Jul 4); catalyst retired |
| **Jun 12** | First Brands: UST convert-or-dismiss hearing (Judge Lopez, §1112(b)) — was OTTO-32 resolver | ✅ **RESOLVED (swept Jul 4)**: UST conversion NOT granted; reformulated plan pays admin claims in full; **DS conditionally approved**; confirmation → **Jul 28**. Pre-registered "deny+reset → confirmation survives" branch fired `[CONF Bloomberg Law/TT/Octus]` |
| **Jun 17** | Tricolor §341 creditor meeting (continued) — trustee distribution-plan watch | ✅ **held + continued to Nov 11** (swept Jul 4); no distribution plan filed; $113M gridlock unresolved. OTTO-29 resolution-slip past Sep 30 confirmed |
| **Jun 17** | First Brands: plan-confirmation hearing (contingent) | ✅ **SUPERSEDED → Jul 28** (swept Jul 4) — Jun 12 DS approval reset the confirmation to Jul 28 |
| **Jun 30** | OTTO-05 + OTTO-28 prediction resolve | ✅ **BOTH FALSIFIED (swept Jul 4)** — OTTO-05: BBB spread tightened to +140bps (not >250); OTTO-28: Ally Q2 postdates resolve + no break-out |
