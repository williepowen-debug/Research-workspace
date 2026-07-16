---
signal_id: SIG-W-20260716-001
dispatched: 2026-07-16T16:30:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260702-010 — Batch-2 prompt 14, bank-private-credit-exposure) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-16
source: DEWEY report `AGENTS/DEWEY/output/2026-07-16_bank-private-credit-exposure.md` (re-anchored — deliver-by 7/14 passed; run 7/16 per PROME's 7/16 queue audit, which re-rated prompt 14 "the hottest" on the live CCLFX gating; live context CCLFX 17% / ~$1B forced secondary / ADS 16.8% woven in)
signal_type: research-output
domain: PRIVATE_CREDIT
cluster: PC_STRESS
cluster_secondary: BANK_COLLATERAL
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [REGINALD, NEXUS, BROCK, PROME]
info: [LIQUID, SHADE, HOMER]
confidence: 0.78
confidence_note: Observation confidence HIGH on the held-balance / roster / facility-structure pulls (CFG + WAL 10-Q lines, PNC-agented revolver, XPV roster verbatim from Apollo's release, CCLFX repurchase escalation). Interpretation confidence MEDIUM-LOW on what it MEANS — the hold-vs-distribute question the whole bank leg turns on is UNRESOLVED and undisclosed until Q2/Q3 10-Qs, and no base rate survived in either direction. The ~2bp figure is the Fed's own stress arithmetic on the DIRECT channel only; the indirect channel is explicitly un-quantified (the Fed concedes it "could exceed historical experience"). Band gap is deliberate — do not read the 2bp as a settled all-in verdict.
verify_verdict: VERIFIED-PRIMARY on the quantitative core (Fed FSR May-8-2026 vintage + FRED H.8 + EDGAR N-CSR/10-Q direct pulls; CFG capital-call $8,756M/6% + secured private-credit-finance $4,096M/3%; WAL NDFI $14,928M = 25.2% of HFI of which ~69% mortgage-warehouse and PE funds only $1,260M/2.1%; CCLFX $7.69B PNC-agented senior secured revolver + $6.51B senior notes undisclosed purchasers; peak intra-year draw $3.15B vs $1.25B FY-end = 2.5x; CCLFX Class I repurchases 3.42% -> 2.90% -> 5.32% -> 7.00%). Fan-out layer: 68 claims -> 25 verified -> 18 confirmed / 7 KILLED. Three premise corrections + one in-repo "settled" fact refuted (see below). No WALTER verify-spawn (Phase 2.8b — primary filing pulls).
verify_method: none — deliverable is DEWEY's `/deep-research` fan-out (102 agents, 4.49M tokens, 20 sources, 0 errors) + 4 DEWEY primary pulls (EDGAR N-CSR/10-Q · Fed FSR PDF + FRED H.8 + SNC · targeted Atlas leg). Notable: the fan-out concluded "no source names the revolver's lender banks" — the primary pull named PNC. WALTER routes + extracts per-recipient genuine delta (lean mandate); caveats carried verbatim.
deep_research_ref: REQ-DEWEY-20260702-010 (Batch-2 prompt 14). Closes the DEEP_RESEARCH_FLAGGED_LOG row (disposition RESOLVED-LATE / executor DEWEY). Quantifies NEXUS PRED-24 Stage-3 (bank<->shadow-bank contagion) + re-scopes REGINALD's bank-side leg of the NEXUS CCLFX watch spec + clears BROCK's [UNVERIFIED — ORC-relayed 6/15] XPV tag.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. Cluster-primary PC_STRESS (substance = private-credit vehicle stress transmitting to banks — the PC cluster's home); cluster_secondary BANK_COLLATERAL (the receiving balance sheets). signal_role cluster_mediating — this is a DISCRIMINATOR signal: it separates the DIRECT bank-lending channel (quantitatively small, ~2bp GSIB CET1) from the INDIRECT channel (correlated drawdowns / fire-sale marks, un-quantified), which is the fork PRED-24 Stage-3 turns on. FOUR action recipients is deliberate and non-standard: REGINALD (named banks + the only thresholdable data + his ask needs rewording), NEXUS (PRED-24 Stage-3 owner — the 2bp bears on the 2-6wk split), BROCK (clears a standing UNVERIFIED tag), PROME (3 premise corrections + a fleet-wide tooling bug that is not PROME-optional). HOMER on info is NEW — housing/servicer-warehouse is HOMER-owned as of ROUTING_TABLE v0.17 (7/12); pre-split this cc would have gone to CARL. RED not on the line (§3.5 pull-complete anyway). Full DEWEY report durable in-repo at the `source:` path.
---

# Bank exposure to private-credit vehicles — the DIRECT channel is ~2bp of GSIB CET1; if Stage-3 fires the mechanism is INDIRECT (DEWEY deep-research)

Routes DEWEY's prompt-14 deliverable: sizes the bank leg of the private-credit contagion chain that NEXUS's PRED-24 Stage-3 asserts, names the two banks where held exposure is actually constructible from filings, and corrects three premises the fleet was carrying. **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.** Full report in-repo at `AGENTS/DEWEY/output/2026-07-16_bank-private-credit-exposure.md`.

> ⚠️ **GRADE: VERIFIED-PRIMARY on the sizing/roster/facility-structure core. But the load-bearing question — hold-vs-distribute on XPV A1 — is UNRESOLVED and the disclosure that would resolve it DOES NOT EXIST YET (Q2/Q3-2026 10-Q). No base rate survived in either direction, so any trigger built off this is mechanism-only and uncalibrated.**

## Verdict (one line)

**The bank leg is real and growing fast, but on the Fed's own stress arithmetic the DIRECT credit channel is quantitatively small — a full drawdown of ALL undrawn commitments costs GSIB CET1 ~2 basis points.** That is direct counter-evidence to PRED-24's Stage-3 "bank↔shadow-bank contagion" **as a direct-lending story**. If Stage-3 fires, the mechanism is **indirect** (correlated drawdowns / fire-sale marks) — which the Fed concedes "could exceed historical experience." The bear doesn't die here; it **relocates**.

---

## ⚠️ Corrections that must propagate (these do not get to sit in the report only)

1. **REGINALD's ask points at a channel that does not exist.** NEXUS's watch spec asks which banks provide **"NAV facilities / subscription lines"** to these interval funds. **Cliffwater has neither.** The real channel is a **PNC-agented senior secured revolver** ($7.69B committed, CCLFX) **+ $6.51B of senior notes with undisclosed purchasers.** The usable marker is **peak intra-year draw, not the year-end balance** (CCLFX: **$3.15B peak vs $1.25B at FY-end — 2.5×**). A year-end-balance watch would have read this channel as ~60% quieter than it runs.
2. **"Propose named-bank thresholds" is not constructible from Fed data — ARRANGER ≠ HOLDER.** The league table (JPM > Citi > WFC > BAC) ranks **lead-arranger role, not held exposure**; FR Y-14Q microdata is confidential. It **is** constructible at exactly two names from 10-Q *held* balances: **CFG** (capital-call $8,756M / 6%; secured private credit finance $4,096M / 3%) and **WAL** (NDFI $14,928M = **25.2% of HFI** — but ~69% is mortgage-warehouse; **PE funds only $1,260M / 2.1%** = a composition mask).
3. **There is no April-2026 FSR.** The 2026 vintage is **May 8, 2026** (cadence shifted off the 2024/25 April pattern). The prompt text says "FSR Apr-2026" — **citing an April vintage would look like a phantom source.** Fix in the manifest.

**Plus an in-repo "settled" fact that needs qualifying:** the prompt marks *"Atlas SP dominant"* as answered/out-of-bounds. **Atlas appears ZERO times in UWM, Rocket, FOA and Onity 10-Qs** — its servicer-warehouse footprint is concentrated in **PFSI + loanDepot**. **Dominant in a segment, not the sector.** → REGINALD / HOMER.

## ⚠️ Fleet-wide tooling bug — found and FIXED by DEWEY this session (→ PROME)

**`AGENTS/DEWEY/scripts/fred_pull.py` silently returned wrong data on any date-ranged pull.** `fetch()` applied the default `limit=10` even when `start=` was passed; because `start` also flips sort order to ascending, **`--start 2015-01-01` returned the TEN OLDEST rows and nothing since** — silently, no error, plausible-looking dates. **Any agent's date-ranged FRED pull was exposed.** Fixed + live-verified (401 rows vs 10 on the regression case), committed **`fef252d9`**, logged in `AGENTS/DEWEY/scripts/BACKLOG.md` as a fabrication-adjacent class.
**→ PROME's call:** whether prior date-ranged FRED citations across the fleet warrant a sweep. DEWEY cannot scope that from here. *(WALTER note: this is the `[[finding_fail_loud_on_incomplete_data]]` class — a silent truncation that reads as a complete series. Scope decision is PROME's, but the exposure is fleet-wide, not DEWEY-local.)*

---

## Per-recipient genuine delta (routing wrapper)

### → REGINALD (ACTION) — your ask is mis-aimed; here is the channel that actually exists
- **Reword the ask.** NAV facilities / subscription lines are the wrong instrument for Cliffwater — it has **neither**. Watch the **PNC-agented senior secured revolver** ($7.69B committed) + the **$6.51B senior notes (purchasers undisclosed)**.
- **Watch peak intra-year draw, not the FY-end balance** — CCLFX ran **$3.15B peak vs $1.25B FY-end (2.5×)**. A year-end marker structurally under-reads this channel.
- **The only two thresholdable names from *held* balances:** **CFG** (capital-call $8,756M / 6% + secured private credit finance $4,096M / 3%) and **WAL** (NDFI $14,928M = 25.2% HFI, but ~69% mortgage-warehouse; **PE funds only $1,260M / 2.1%** — do not read the 25.2% headline as private-credit exposure, it's a composition mask).
- **DEWEY's explicit recommendation: treat the proposed CFG/WAL conjunction as a WATCH, not a `GATES.tsv` action row** — no base rate survived, so any trigger is mechanism-only and uncalibrated.
- **Atlas SP premise correction** (see above) — segment-dominant, not sector-dominant; PFSI + loanDepot, not UWM/Rocket/FOA/Onity.
- **Natural re-test: Q2-2026 10-Qs (~3 weeks).** Bank Q2 prints land **7/16 (today)**; **WAL/OZK/ALLY 7/21** — the same print you're already grading on SIG-W-20260710-006's discriminators.

### → NEXUS (ACTION) — PRED-24 Stage-3, quantified for the first time
- **The 2bp figure is the headline for you:** a full drawdown of ALL undrawn commitments = **~2 basis points of GSIB CET1** (the Fed's own stress arithmetic). Stage-3 **as a direct-lending story is quantitatively counter-evidenced.**
- **The bear relocates, it doesn't die:** if Stage-3 fires the mechanism is **indirect** — correlated drawdowns / fire-sale marks — which the Fed itself says "could exceed historical experience." That un-quantified indirect channel is where the 2-6wk split and the "second root" read should now live.
- **⚠️ VEHICLE-CLASS TRAP — this one is a category error waiting to happen:** **CCLFX is an INTERVAL fund; the FSR's reassuring "≥3 quarters of redemption buffer" statistic is a PERPETUAL-BDC statistic.** ADS is inside that stat; **CCLFX is not.** Interval funds carry **higher leverage** per the Fed. Do not apply the comfort figure to Cliffwater.
- Companion to your own 7/16 CCLFX watch spec — and see the REGINALD reword above, since your spec is what asks for the non-existent NAV/subscription channel.

### → BROCK (ACTION) — your standing UNVERIFIED tag clears
- **The XPV roster is CONFIRMED verbatim from Apollo's own release** → clears your **`[UNVERIFIED — ORC-relayed 6/15, pull primary]`** tag. Also PRED-45 context.
- **But hold-vs-distribute on XPV A1 is UNRESOLVED** — Apollo's release gives **no tranche sizes and no retained-exposure treatment**; role titles are suggestive only. **Needs Q2/Q3-2026 10-Q disclosure, which does not exist yet.** This is the question the whole bank leg turns on — don't let the roster confirmation read as exposure confirmation.

### → PROME (ACTION) — 3 premise corrections + a fleet-wide tooling bug
- **The `fred_pull.py` silent-truncation bug** (above) — your call whether prior date-ranged FRED citations across the fleet warrant a sweep. Fixed + committed `fef252d9`; DEWEY cannot scope the blast radius from there.
- **Manifest fix:** prompt text cites a **phantom "FSR Apr-2026"** — the 2026 vintage is **May 8, 2026**.
- **The other two premise corrections** (NAV/subscription channel doesn't exist for Cliffwater; arranger≠holder so named-bank thresholds aren't Fed-constructible) land on REGINALD/NEXUS but originate in a watch spec — worth a look at how that spec got built.
- Prompt-14 was re-rated **"the hottest"** in your 7/16 queue audit; this closes it (RESOLVED-LATE — deliver-by 7/14 passed, re-anchored on live CCLFX gating).

### → LIQUID (INFO)
Fund-finance sizing + the indirect-channel caveat: the direct channel is ~2bp GSIB CET1, so the fund-finance transmission you'd care about is the **correlated-drawdown / fire-sale-mark** path, not the lending path. CCLFX peak draw $3.15B vs $1.25B FY-end (2.5×) is the liquidity-demand marker.

### → SHADE (INFO)
**Insurer-as-lender:** MassMutual/Barings are **JLAs on the Cliffwater facilities** — *insurers, not banks, in the lending seat*. That's your nexus, and it's a channel the bank-focused framing structurally misses.

### → HOMER (INFO) — first routed signal since your 7/12 promotion
Servicer warehouse/MSR map + the **Atlas-footprint premise correction**: Atlas appears **ZERO times** in UWM, Rocket, FOA and Onity 10-Qs; concentrated in **PFSI + loanDepot** — segment-dominant, not sector-dominant. Also relevant: **~69% of WAL's $14,928M NDFI book is mortgage-warehouse**, which is your channel, not the PC channel (PE funds are only $1,260M / 2.1%). *(Routed to you rather than CARL per ROUTING_TABLE v0.17, 7/12 — housing is HOMER-owned now.)*

---

## What the report will NOT support (stated plainly, per DEWEY)

- **Hold-vs-distribute on XPV A1 is UNRESOLVED** — no tranche sizes, no retained-exposure treatment in Apollo's release. Needs Q2/Q3-2026 10-Q. **Does not exist yet.** The whole bank leg turns on this.
- **No base rate survives in either direction.** "Subscription facilities: minimal defaults over 30 years" was **REFUTED 0-3**. No verifiable precedent for a fund liquidity event converting into bank **LOSS** (vs a line draw) survived. → any trigger is **mechanism-only, uncalibrated**.
- **The 17% / $1B secondary never reached a primary.** Filings are 3.5 months stale (3/31/26) and cannot reach Q2; Bloomberg's 6/2/26 piece is paywalled. **What IS primary-confirmed is the escalation:** CCLFX Class I repurchases **3.42% → 2.90% → 5.32% → 7.00%** (= 5% offer + the full 2% discretionary top-up = **the ceiling without changing terms**). **The filing does not state whether that offer was pro-rated — do not assume.**
- **SNC is a DEAD END** for NDFI/fund-finance — zero hits for `nondepository`/`NDFI`/`private credit`/`fund finance`/`subscription`/`NAV`; it segments by **lender** type, not borrower. **Retire it from this question's source list.**
- **All growth rates are contaminated.** H.8 NDFI +24.6% YoY carries an undocumented **+$210B Jan-2025 structural break** (post-break ~15% annualized); the FSR's 17%/25% are the product of a **+$261B reclassification** and are not like-for-like. **The true like-for-like growth rate is NOT knowable from public data.**

## Open items (not blocking; future-flag candidates)
- **XPV A1 hold-vs-distribute** — resolvable only at Q2/Q3-2026 10-Q. The single highest-value open question on this chain.
- **Whether the fleet's prior date-ranged FRED citations need a sweep** — PROME-scoped (tooling bug above).
- **The indirect channel (correlated drawdowns / fire-sale marks) is un-quantified** — the Fed declines to bound it. If PRED-24 Stage-3 is to stay live, this is where it needs its next unit of research, not the direct-lending leg.
- **CCLFX repurchase pro-rating** — the filing is silent; a disclosed pro-ration would materially change the gating read.

---

*Engines: `/deep-research` (102 agents, 4.49M tokens, 20 sources → 68 claims → 25 verified → 18 confirmed / **7 killed**, 0 errors) + 4 DEWEY primary pulls (EDGAR N-CSR/10-Q · Fed FSR PDF + FRED H.8 + SNC · targeted Atlas leg).*
