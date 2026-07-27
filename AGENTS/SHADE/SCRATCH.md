# SHADE SCRATCH.md — Ephemeral Session State
**Rewritten:** 2026-07-27 ~14:15 ET (Will catch-up boot, Monday — 7-day gap: 15-item mail drain [both lanes CLEAN] + Delaware Life restatement pulled to PRIMARY + vector #1 moved to FIRING + live tape refreshed + one negative result that keeps the Athene wall standing)
**Amended:** 2026-07-27 ~19:45 ET — **post-crash re-boot. NOTHING WAS LOST.**
**CLOSED OUT:** 2026-07-27 ~22:45 ET — Will-directed (final; a first closeout at ~22:10 was reopened for the FABN canary rebuild). Session 2 delivered **Weld 2** (built, corrected, closed), the **ARCC pre-registration**, the **accrued-interest test**, and a **live tape refresh**. **Both mail lanes CLEAN; 6 packets processed; 5 outbound.**

## 🔴 SESSION-2 HEADLINE — FIVE of my own claims were retired by evidence, and one framing I adopted from CREED was retired too

**This session's most useful output was self-correction, and the handoff should say so plainly.**
1. **The accrued-interest anomaly** (my 7/27 flag) — **explained** by disclosed deferred-interest trust notes; **not** PIK, which fell 55.9%. Retired.
2. **"$775B = insurer CRE exposure"** — ⚠️ **wrong, and I had MBA's methodology passage in my own extraction and did not act on it.** It is **whole loans only, a FLOOR**; insurer-held CMBS prints in the ~$637B CMBS bucket. My "probably mostly distinct" is withdrawn; **the prior should be OVERLAP.**
3. **"The sink absorbs at PAR"** — withdrawn. **n=1 on performing paper, where par is the null hypothesis**, and CREED had logged 99.7% as a *counter*-datum.
4. **My own fix to CREED's falsifier was ALSO wrong** — my ~+$20B bar anchored to H2 quarters when Q2 is an H1 quarter; it would have resolved FALSE even on a full $9B landing. **Final agreed bar ≥+$10.0B.**
5. **"The FABN canary can't be refreshed until 8/4"** — ⚠️ **an untested path assumption, and wrong.** Rebuilt it independently from NPORT-P holder marks: **peer penalty ≈+40bp, bracketing the deck's +43–48bp.** *(It is corroboration, not a refresh — but the claim that it was impossible was mine and it was false.)*
6. **"The penalty is widening ~+15bp"** — withdrawn to **unestablished**; my own independent data fails to confirm it.

**What survived all of it: the through-line — ALLOCATION DISCRETION. The categories are set by the entities being measured.** Four instances now: the filer sets the SSAP-25 related-party test · the buyer sets the landing entity (§2.8, private notice) · the filer defines the deferred-interest population (undisclosed denominator) · **and the measurement system splits insurer CRE risk by the instrument's legal form** (CREED's, the cleanest — no entity chose anything).

---

## 🔧 CRASH RECOVERY NOTE (2026-07-27 ~19:45, read this first)

The 14:00 session ended in an unclean shutdown right after commit `771f4094` (14:26). **Verified state at re-boot: working tree CLEAN, `origin/master` in sync 0/0, and all three outbound packets delivered AND committed** — BROCK (`c88796b5`, since **consumed** into `AGENTS/BROCK/inbox/processed/`), PROME (`PROME/inbox/2026-07-27_from-SHADE_vector1-FIRING-delaware-life-primary.md`), CREED (`771f4094`). No re-send needed, no orphaned packets.

**The only real gap:** **two inbox packets landed AFTER the mail drain** (BROCK 14:21, CREED ADDENDUM 14:24) and were never logged. **Both drained on the re-boot** — `board_log.tsv` rows + `git mv` to `processed/`. Both lanes CLEAN again.

⚠️ **Correction to the 14:15 mail-state line below:** it lists two 7/27 files as sitting in `outbox/`. **They were never in `outbox/`** — they were written **directly into the recipients' `inbox/` dirs** under root-CLAUDE.md carve-out ①, which is the correct route. `outbox/` still holds only 7/09 and 7/20 files. Corrected in MAIL STATE at the bottom.

## TOP VERDICT (7/27) — a SHADE vector is FIRING for the first time, and it is NOT the flagged one

**Delaware Life Insurance Co.** (Group 1001, **Mark Walter**-controlled; $64.7B admitted) restated related-party investments to **$17.24B = 37.6% of general-account assets** — **$16.37B "predominantly contingent on the performance of affiliates"**, **$12.62B of it in the BOND line (+85.5% YoY)**. Driven by **Feb-2026 federal grand jury subpoenas (USAO SDNY) + a parallel SEC probe**; consequence **S&P outlook → NEGATIVE (A- affirmed)** + a **remediation plan to cut affiliated exposure**.

**SHADE's contribution beyond the routing:** WALTER delivered this media-sourced. **SHADE found the KPMG-audited statutory financials themselves on EDGAR** — Form **N-VPFS, filed 2026-06-29**, accession `0001193125-26-286687`. Everything above is now **primary**.

**The mechanism is the real finding:** **SSAP No. 25** classification where the filer **self-defines "predominantly contingent" as >50%**. The $16B was not offshore and not in a captive — it sat in the **general account bond line** on the wrong side of a **self-graded test**. That generalizes to every SSAP-25 filer.

**Vector #1 (insurer asset-transfer / affiliated exposure): 4 → 5 FIRING. Composite 19 → 20/30.**

## PRIOR VERDICT (7/20)
Wrapper thesis went CONCRETE but PRE-MORTEM (UBS/Nationwide wrapped-PC bond); trigger set unchanged.

## CHANGES SINCE LAST SHADE SESSION (7/20 → 7/27)
- **Delaware Life / Clear Spring (SIG-727-004)** — above. **The single highest-value SHADE event since inception**, because it converts the core hypothesis from pattern to named instance.
- **Double-jeopardy CORRECTED (DEWEY, EDGAR-primary; landed 7/20 21:57, *after* my closeout):** lender leg **REFUTED at named-entity level** for all 5 gated funds — every filed facility bank-led, zero insurer names (ADS Bald Eagle SPV agreement read in full: BofA admin / Citi collateral). **Athene↔ADS lender leg REFUTED**, holder leg not publicly confirmable. Also kills the fund-facility reading of the MassMutual/Barings datum I folded 7/20.
- **FHLBank Chicago Q2 (SIG-723-017, primary):** advances **+16% in six months to $71.1B**, release **naming insurance-company members** as a co-driver. ⚠️ 1 of 11 districts — do NOT stack against REG-T-06.
- **Granato & Drall paper (SIG-725-004):** guaranty-fund assessments → **creditable against state premium taxes** → loss lands on **state tax revenue**. Registered as a **tail-severity modifier**, NOT an arming trigger.
- **Tape (7-day gap closed):** **HY OAS 279 [FRED 7/24]**, 1bp under the level leg after a +11bp two-session move. **APO $124.07, ARES $126.88, ARCC $18.89, FSK $10.82, OBDC $10.94, BIZD $12.48** (all 7/27 intraday).

## WHAT I DID (2026-07-27)
1. **Full boot** — STATUS/SCRATCH/MEMORY; confirmed origin current (nothing to pull).
2. **Drained 15 mail items** — 10 WALTER + 5 root — all logged to `board_log.tsv` with reasoned dispositions and `git mv`'d to `processed/`. **Both lanes now CLEAN** (WALTER lane had been accumulating since 7/21).
3. **Pulled SIG-727-004 to primary** — EDGAR crawl (UA header via bash), located and parsed the DLIC statutory financials; reconciled the media figures, **found and flagged a divergence the media framing hides** (see below); wrote `research/DELAWARE_LIFE_RELATED_PARTY_RESTATEMENT_2026-07-27.md`.
4. **Adjudicated WALTER's explicit ask** — answered **NO** on moving `SIG-720-001` off pre-mortem, with the mechanism table showing why.
5. **Ran the cohort screen and recorded it as a NEGATIVE result** — the route does not reach Athene.
6. **STATUS write-back** — new §0d, vector #1 → firing, new classification-integrity dashboard row, double-jeopardy row corrected, ratings row corrected, new §5 watchlist row (Group 1001), 2 new §6 calendar rows, 4 new §8 questions, new BOTTOM LINE.

## ⚠️ NUMBERS DISCIPLINE — carry these exactly
- ✅ **Primary:** FY2024 Correction-of-Errors restatement **$2.26B → $11.56B = 5.1×**. FY2025 related-party total **$17.24B / 37.6% of $45.90B GA assets**.
- ⚠️ **Media-sourced, UNRECONCILED:** the circulating **"$1.4B (3%) → $17B (39%), ~12×"**. **The $1.4B is not in the filing.** Do not propagate 12× as primary.
- ⚠️ **NOT a credit event:** disclosure correction only — **no write-down taken, surplus not restated.** Impaired-vs-mis-labelled is **OPEN**.
- ⚠️ **NOT an audit red flag:** statutory opinion **UNMODIFIED** + Emphasis of Matter. The **"Adverse Opinion on U.S. GAAP" is boilerplate in every statutory-basis audit** — never report it as a finding.
- ⚠️ **NO CHARGES FILED.**
- ⚠️ **NAMING HAZARD:** the subject is **Mark Walter, a person** — always qualify, never bare "WALTER" (the signal router shares the name).

## NEXT SESSION
0a. 🔴 **HARD DATE — MONDAY 2026-08-04: Apollo/Athene Q2 earnings + FI deck.** This is the **real** FABN canary refresh (7/27's independent build was corroboration, not a refresh). Pull the **5Y FABN secondary + the peer table**, compare to the independent **≈+40bp**, and **re-test the withdrawn "widening" claim**. Also the first Athene surface that could show where the **ARI $9B** landed (mortgage-loan line, `PRED-CREED-010`).
0. ⭐ **FIRST ACTION WEDNESDAY 7/29: grade the ARCC pre-registration.** The print lands **pre-market 7/29**. Open `research/ARCC_Q2_2026_PREREGISTRATION_2026-07-27.md`, compare against the locked baselines, and **write the verdict to `board_log.tsv` even if nothing moved** — an unfired pre-registration that never gets graded is worthless. Watch the **beta trap**: HY through 280 on a risk-off does **not** arm the trigger.
1. **Boot:** STATUS → SCRATCH → MEMORY; check `inbox/WALTER/` + `board_log.tsv`; **pull HY/wrapper basket live before citing.**
2. **Delaware Life follow-through (top of queue):** remediation-plan size/timetable; **impaired vs mis-labelled**; the **Barbco "former affiliate"** de-affiliation + new **Nautilus (Barbados)** modco cession. **[Clear Spring statutory financials ATTEMPTED 7/27 — NOT publicly obtainable; see below. Do not re-attempt via EDGAR.]**
2b. ✅ **DONE 7/27 — accrued-interest anomaly TESTED, and my own flag was partly retired.** Real vs four controls, but explained by disclosed deferred-interest trust notes; **not** PIK. **Forward tests that remain:** (i) **what is the TOTAL trust-note book** (not just the $326M related-party subset) — needs annual-statement Schedule D / NAIC InsData, **not** in the N-VPFS; (ii) does FY2026 show deferred interest growing **faster than NII** (6.5% is the baseline to beat); (iii) CUSIP-level detail on what DLIC bought from CSLAC — **not obtainable**, CSLAC has no EDGAR route.
3. **Cohort read-across:** is the SSAP-25 self-set threshold understating related-party lines cohort-wide? **No EDGAR screen exists** — needs FY2026 enhanced statutory disclosure / NAIC InsData / state-DOI.
4. ✅ **PROME Weld 2 — BUILT AND CLOSED 7/27.** *(Superseded; kept for the shape of what was asked.)* ~~build the combined insurer-sink **triple-decker**~~ — the same balance-sheet class simultaneously absorbing **repackaged PC** + **fund-finance lending** + **shed CRE credit**, against the Moody's **$807B / 20%-illiquid** baseline. CRE leg is primary-stamped and on the shelf (MBA Q1-26: life insurers **+$3.3B** → $775B stock of a $5.02T market, vs CMBS/CDO/ABS **−$9.6B**). Extend `research/INSURER_LENDER_DOUBLE_JEOPARDY_2026-06-26.md`. ⚠️ Carry the **fast-vs-slow recognition** framing (securitized sheds, insurance absorbs) and the **anti-fusion discriminator** — absorption is not by itself the finding; **unmeasured** absorption is.
5. **Granato & Drall:** read the paper; test the premium-tax-credit claim against an actual state guaranty statute.
6. **Trigger watch:** unchanged — **HY >280 SUSTAINED (5+ sessions) AND wrapper-basket leads managers DOWN.** Level leg is 1bp away; **sign leg currently inverted.** Issuance ≠ arming; a beta-driven re-approach to 280 does NOT satisfy the sign leg.
7. **DO NOT** re-run the NPORT crawl unless kill-path-1 nears a trade. **DO NOT** cite $155B/$2.88B/1.44% as FY2025.

## OPEN THREADS
| Item | Status |
|---|---|
| Delaware Life / Clear Spring related-party restatement | 🔴 **FIRING** — primary-verified; DOJ+SEC live, no charges; S&P negative outlook; impaired-vs-mislabelled OPEN |
| **Vector-#1 scoring rule (NEW, post-crash drain)** | ✅ **ADOPTED** — the discriminator is **disclosure quality + price discovery, NOT affiliation**. Affiliation is normal in this structure; *unmeasured* affiliation is the problem. **ARI→Athene is the BENCHMARK, not corroboration** — a well-governed affiliated transfer does NOT add to the firing vector. Score named transfers on 4 axes (mechanism / size / disclosure / price discovery); the **divergence** from the benchmark is the finding. |
| **ARI→Athene $9B, Athene-side** | 🟠 **SHADE-OWNED residual** — capital treatment, RBC, L3, concentration, and the **ALM question** (floating 7.0% CRE first mortgages vs fixed annuity liabilities; no hedging disclosure pulled). ⚠️ **Not in any current Athene figure** — close 4/24/26 postdates the 3/31/26 balance-sheet date. Q2-26 filings = first observable. Falsifier: **MBA Q2 CM/MF print ~mid-Sept.** |
| Related-party classification integrity (SSAP-25 self-set test) | 🟠 **NEW, SHADE-OWNED** — measurement-integrity finding; degrades SHADE Key Ratios #1/#3 |
| **Accrued-interest anomaly** | ✅ **TESTED + PARTLY RETIRED 7/27.** Real outlier (9.77% vs **four** controls at 0.43–1.86%) but **EXPLAINED** by disclosed "trust notes that allow for deferred interest." **NOT PIK** — PIK fell 55.9%. **Replaced by:** deferred interest $159,580 ÷ trust notes $326,225 = **48.9%, impossible as a yield → denominator undisclosed**; and **96% of the $16.37B has no structural description.** `research/DELAWARE_LIFE_ACCRUED_INTEREST_TEST_2026-07-27.md` |
| **Impaired vs mis-labelled** | 🟡 **OPEN but moved** — **not impaired on any evidence in the filing, not demonstrably sound either.** ~6.5% of NII is non-cash by contract, from instruments "predominantly contingent on the performance of affiliates," population undisclosed. ⚠️ **Never cite the $225K non-admitted figure as evidence the book performs — deferred interest is never "past due" by construction.** |
| Cohort read-across (is Delaware Life idiosyncratic?) | ⚠️ **NO SCREEN AVAILABLE** — EDGAR proven to be the wrong slice |
| Clear Spring Life statutory financials | ❌ **NOT PUBLICLY OBTAINABLE** — no EDGAR registration, no N-VPFS (fixed/FIA only, so no variable-product filing to bundle into). Delaware DOI publishes exams, not annual statements. **Gated paths only: NAIC InsData / state-DOI request / AM Best–S&P CapIQ statutory data.** |
| Supervision as forcing function | ⚠️ **WEAKENED (NEW 7/27)** — DE DOI multi-state exam adopted 6/23/25 found "no significant findings, no recommendations"; AM Best went POSITIVE 10/10/25; the restatement came from a **Feb-2026 grand jury**, not from either. Bears on kill-path #2. |
| Athene statutory / Schedule-BA wall | ❌ **STANDS** — N-VPFS route does not reach Athene (tested + refuted this session) |
| Wrapper-decoupling trigger | ⚠️ **NOT ARMED — both legs fail** (7/27 close). HY **279** [FRED 7/24], 1bp under and **not sustained**; sign leg **INVERTED** — wrappers avg **+1.26%** vs managers **+1.16%**, i.e. wrappers led UP. |
| **ARCC Q2 print — PRE-REGISTERED** | 🟢 **DONE 7/27, before the print.** ⚠️ **Date corrected: 7/29 pre-market, NOT 7/28** (carried wrong since 6/28). Baselines locked from the Q1-26 10-Q: NAV **$19.59** (−1.76% QoQ from $19.94), marks **−$0.42/sh**, NII coverage **1.15×**. Movers, non-movers and the HY-280 beta trap all written down in advance. **`research/ARCC_Q2_2026_PREREGISTRATION_2026-07-27.md` — GRADE IT WEDNESDAY EITHER WAY, including if nothing moved.** |
| Wrapped-PC (UBS/Nationwide) tripwires | 🟠 PRE-MORTEM — 0 of 4 firing; unchanged |
| Insurer-lender double-jeopardy | 🟡 **DOWNGRADED to not-publicly-confirmable** — lender leg refuted; mechanism retained |
| Combined insurer-sink (Weld 2) | ✅ **BUILT + CLOSED 7/27** — `research/COMBINED_INSURER_SINK_WELD2_2026-07-27.md`; delivered to PROME. **Not a triple-decker; sink cannot be sized.** Deck 2 refuted, Deck 1 small/unstressed, Deck 3 the only measured one. **Residual live piece: same-entity convergence** (unverifiable — Schedule-BA wall + §2.8 gap). |
| **§2.8 landing-entity gap (NEW, SHADE-OWNED)** | 🟠 **The finding of the build.** ARI Purchase Agreement §2.8 lets Athene designate *"Affiliates, Managed Accounts or Portfolio Companies"* to take *"all or any portion"* of the $9B by **private notice**, ACRA entities named as subsidiaries — **the split was never disclosed.** Makes the ARI benchmark **four-of-five**, not five-of-five. Resolves (or doesn't) on **Athene Q2-26 filings, ~Aug.** ⚠️ No conduct allegation — routine structuring. |
| **CREED `PRED-006` re-spec** | 🔴 **ROUTED 7/27, awaiting CREED** — his baseline (+$3.3B) is a **seasonal trough**; a +$11B print resolves TRUE while being normal. Proposed threshold **~+$20B**, tested against the prior 4 quarters. **Want his final wording back** so my §7 falsifier table matches his ledger. |
| **Athene Q2-26 mortgage-loan line** | 🟡 **PRE-REGISTERED as CREED `PRED-CREED-010` (70%)**, resolving on Athene Holding 10-Q Q2-26 (~Aug), cross-checked vs Apollo 10-Q RS segment. **All 3 branches pre-committed** (both move / only Athene moves = bad instrument / neither moves = re-derive). ⚠️ **SHADE-relevant caveat:** the risk is **classification, not the transaction** — ACRA co-invest vehicles mean the book can land in a sidecar, a securitization, or "investment funds" instead of "mortgage loans", so a flat line is **ambiguous, not refuting.** Same Schedule-BA/ACRA opacity SHADE already owns. |
| **ARI post-sale size** | ✅ **RECONCILED to one number** — **$2.2B total assets / BVPS $12.05** (at-close, 4/24 press release). ⚠️ **Do NOT cite ~$1.3B as post-sale cash** — it was a Q1 (3/31/26) **pre-close cash component**, mislabelled; CREED took the error and corrected 4 surfaces. |
| Granato/Drall guaranty-fund → premium-tax | 🟡 registered as tail-severity modifier; paper unread |
| FABN peer-relative canary | 🟠 YELLOW — **✅ INDEPENDENTLY CORROBORATED 7/27 (session 2).** Rebuilt from NPORT-P holder marks with a SHADE-chosen FABN peer set, matched-fund design: **peer penalty ≈ +40bp** (within-fund paired, n=15 funds, 11/15 positive, IQR −1 to +52) — **brackets the deck's +43–48bp; the self-reported number does not flatter itself.** ⚠️ **Corroboration, NOT a refresh** (3/31–5/31 straddles the deck's 5/14). ⚠️ **"Widening ~+15bp" WITHDRAWN → unestablished.** ⚠️ Do not cite the 6–11y bucket (one CUSIP). **Rerunnable: `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`, ~4 min.** |
| **CREED `PRED-006` branch 2** | ✅ **CLOSED — CREED filed it.** Reads *"wholly or largely outside the Fed life sector"* in PREDICTIONS.tsv, scoreboard and SCRATCH; **level deliberately held at +$10.0B** (correctly — tuning a bar to an unobservable split fits the test to a quantity nobody can see), with the residual recorded and an explicit instruction that a half-landing must not be written up as a clean instrument failure. **Nothing owed either way.** |
| Egan-Jones Aug 12 | 🟢 calendar binary, unchanged (16 days out) |
| Apollo XPV A1 hold-vs-distribute | 🟡 UNRESOLVED — needs Q2/Q3-26 10-Q |

## MAIL STATE *(final, 22:10 closeout)*
- **`inbox/` root: CLEAN · `inbox/WALTER/`: CLEAN.** **6 packets processed this session** — 3 late arrivals from the crash window (BROCK, CREED ADDENDUM, CREED Weld-2 unblock) + 3 that landed mid-session (CREED $775B correction, CREED `PRED-006` counter-correction, WALTER `SIG-W-20260727-021`). All logged to `board_log.tsv` and `git mv`'d to `processed/`.
- **5 outbound packets, all self-authored under carve-out ①:** CREED ×3 (ARI primary verification · `PRED-006` re-spec · $10B accepted + corrections adopted) · PROME ×2 (Weld-2 delivery · **correction notice**, since PROME holds the uncorrected version) · WALTER ×1 (`SIG-021` both questions answered).
- ⚠️ **Open ask, the only thing owed to me:** CREED yes/no on phrasing `PRED-006` branch 2 as *"wholly or largely outside the Fed life sector"* rather than *"outside"* — so a **partial** §2.8 landing isn't recorded as a clean instrument failure.
- **Retirement scan:** `research/tmp_aaia_extract/` → `archive/`. No other file is >60d **and** unreferenced.

## MAIL STATE *(as corrected at the 19:45 re-boot — superseded by the block above)*
- `inbox/WALTER/`: **CLEAN** — 10 items drained → `processed/`, all logged.
- `inbox/` root: **CLEAN** — 7 items drained → `processed/`, all logged *(5 in the 14:15 drain + BROCK and the CREED ADDENDUM, which landed after it and were drained post-crash)*.
- `outbox/`: **unchanged since 7/20** — holds only the 7/09 and 7/20 files. The 7/27 packets did **not** go here.
- **Outbound 7/27, all DELIVERED + COMMITTED + verified on disk** (carve-out ①, written straight to recipient inboxes):
  | To | File | Commit | State |
  |---|---|---|---|
  | BROCK | `AGENTS/BROCK/inbox/…_from-SHADE_delaware-life-related-party-PRIMARY-verified.md` | `c88796b5` | ✅ **consumed** (in BROCK's `processed/`) |
  | PROME | `PROME/inbox/2026-07-27_from-SHADE_vector1-FIRING-delaware-life-primary.md` | `c88796b5` | ✅ delivered |
  | CREED | `AGENTS/CREED/inbox/…_from-SHADE_ARI-athene-verified-to-primary-affiliated-transfer-leg.md` | `771f4094` | ✅ delivered |
- No writes outside `AGENTS/SHADE/` except those three self-authored inbox packets (root CLAUDE.md carve-out ①).
