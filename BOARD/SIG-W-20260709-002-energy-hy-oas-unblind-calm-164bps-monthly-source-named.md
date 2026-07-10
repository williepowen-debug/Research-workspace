---
signal_id: SIG-W-20260709-002
dispatched: 2026-07-10T00:20:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260702-006 — Batch-2 prompt 10, energy-HY-OAS un-blind) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-09
source: DEWEY report `AGENTS/DEWEY/output/2026-07-09_energy-hy-oas-unblind.md` (Mode Thesis / Confidence Med-High on the pre-re-escalation level + decoupling / Low on the live post-7/7 read — structurally unverifiable from public data)
signal_type: research-output
domain: CREDIT_SPREADS
cluster: HYDROCARBON_INFRA
cluster_secondary: FED_FRAMEWORK
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [LIQUID, BOND, BRENT]
info: [HAWK, RED, REGINALD, PROME]
confidence: 0.75
verify_verdict: VERIFIED-PRIMARY on the last hard datapoint (ICE BofA US HY Energy OAS = 164bps as of 2026-05-31, tightest of all HY sectors — DEWEY document-confirmed by pulling the source PDF directly, upgrading the workflow's 2-1 read; below both the >300 trip and >400 stress line, and tighter than the ~285bps cited for Apr 28). UNVERIFIED (structurally, by design): any post-June-1 energy sub-index print — no public source publishes it. No WALTER verify-spawn (Phase 2.8b — primary-confirmed; the live-leg gap is honestly flagged, not an extraordinary claim).
verify_method: none — deliverable is DEWEY's direct PDF pull of the ICE BofA HY sector table + a FRED broad-HY anchor. WALTER routes + extracts per-recipient genuine delta (lean mandate). Caveats carried verbatim.
deep_research_ref: REQ-DEWEY-20260702-006 (Batch-2 prompt 10). Closes the DEEP_RESEARCH_FLAGGED_LOG row for REQ-DEWEY-20260702-006 (disposition RESOLVED / executor DEWEY). Un-blinds a trigger blind since Apr-28 (64d) across 3 dashboards + names a free monthly source. Re-prioritized #12→#2 on 7/8 (the de-escalation premise it was deprioritized on reversed with the 7/8 truce collapse).
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. Cluster-primary HYDROCARBON_INFRA (substance = the energy-SECTOR HY credit read + the oil-decoupling confirm — energy-domain home), secondary FED_FRAMEWORK (credit-conditions / convergence-matrix mechanism). signal_role cluster_mediating (the "energy-credit vector PRIMED, not fired; decoupling SUPPORTED" discriminator + the un-blinding of a paywalled trip) → RED auto-cc. ACTION = LIQUID (energy-OAS re-state + HY-path pre-registration, tasked 7/8) + BOND (the durable free monthly source for KB-063) + BRENT (energy-credit vector on the convergence matrix / the >400 line). Full DEWEY report durable in-repo at the `source:` path.
---

# Energy HY OAS un-blind — un-blinded to monthly resolution and reads CALM (164bps, tightest HY sector); decoupling SUPPORTED (DEWEY deep-research)

Routes DEWEY's prompt-10 deliverable: the blinded energy-HY-OAS cell (dark since Apr-28) un-blinded to a monthly resolution, plus a named FREE monthly source so the fleet can monitor it without paid ICE/BBG. **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.** Full report in-repo at `AGENTS/DEWEY/output/2026-07-09_energy-hy-oas-unblind.md`.

> ⚠️ **GRADE: VERIFIED-PRIMARY on the May-31 level (164bps). The live post-June-1 energy sub-index is UNVERIFIED BY DESIGN — no public source publishes it same-week; a >300 energy trip is NOT confirmable same-week.**

## Verdict (one line)
**The blinded energy-HY-OAS cell un-blinds to CALM.** Last hard datapoint: **ICE BofA US HY Energy OAS = 164bps as of May 31, 2026 — the *tightest* of all HY sectors**, below both the >300 trip and >400 stress line, and *tighter* than the ~285bps cited for Apr 28. **Neither threshold was crossed Apr 28 → end-May.** The live "is energy HY widening beneath the 7/7-8 re-arm?" question is UNVERIFIED at the sub-index level, but the surrounding evidence points to *no stress*: broad HY OAS **267–270bps, TIGHTENING through the 7/7-8 re-arm** (energy is a subset and its tightest sector — a >300 energy trip against a 270 parent would need an idiosyncratic blowout for which there's zero corroboration), and rising oil is *revenue-positive* for E&P issuers. **Energy-credit vector = PRIMED, not fired; both thresholds intact on all available data.**

---

## Per-recipient genuine delta (routing wrapper)

### → LIQUID (ACTION) — the energy-OAS re-state (tasked 7/8) + the same-week-blind caveat
- **The trip is not near:** 164 vs the >300 line = **136bps of headroom** at last read; broad HY tightening through the re-arm caps the plausible current energy level well under 300.
- Feeds your **7/8-tasked energy-OAS re-state + HY-path-under-oil-sustained-week pre-registration** — energy-credit stays PRIMED-not-fired.
- **⚠️ trip-logic caveat:** a **>300 energy trip is NOT confirmable same-week by design** (the only free source is monthly, ~5-6wk lag) — flag that in any trip logic; for same-week reads, proxy off broad HY (FRED live) + the "energy = tightest HY sector" prior.

### → BOND (ACTION) — the durable win (leg-4 deliverable): KB-063 now has a free monthly source
- No free source carries the ICE BofA energy sub-index daily (removed from free FRED — DEWEY re-verified the tickers HTTP 400).
- The one reproducible free artifact is **Fidelity Institutional's monthly HY PDF `931730.PDF`** — it republishes the full ICE BofA HY *sector* OAS table incl. Energy. Access: `pdf2text.py "<url>" --grep "ICE BofA"`. Cadence **monthly, ~5-6wk lag** (May-31 vintage was live 7/9). **This permanently un-blinds the cell to monthly resolution.**

### → BRENT (ACTION) — decoupling runs in the reassuring direction; the >400 line is remote
- An oil *price* re-arm is **not** a mechanical energy-credit-stress trigger; stress needs a *sustained* supply-loss / demand-destruction path (SSGA's 6-7% default scenario, "markets not pricing"). The **>400 line is remote absent that.**
- The decoupling thesis (KB-LIQ-058) is **SUPPORTED** — ECB finds oil-supply shocks widen credit only ~half what history implies then revert; energy stayed tightest-in-class through elevated Brent.

### → HAWK (INFO)
No energy-credit stress signature beneath the Brent decoupling through the kinetic window — energy HY stayed tightest-in-class.

### → RED (INFO, auto-cc cluster_mediating)
The discriminator: **energy-credit vector = PRIMED, not fired; both thresholds intact on all available data.** The Brent ~$71 decoupling is the *expected* base-rate signature (per prompt-06's 1987-88 Earnest Will finding), NOT evidence of stress — and NOT evidence of institutional reopening either.

### → REGINALD (INFO)
Energy-credit calm context for the Q2 convergence grid — no energy-sector widening feeding the bank-credit read.

### → PROME (INFO)
Un-blinds a trigger dark 64d (since Apr-28) across 3 dashboards; the named free monthly source is a durable fleet win.

## Open items (not blocking; future-flag candidates)
- **The one datapoint that would bracket the re-escalation:** does Fidelity's `931730.PDF` refresh to a **June-30 vintage** on its normal cadence (~mid-to-late July)? That June energy-sector OAS is the **first print spanning the truce collapse** — worth a monthly re-pull (the literature ID may rotate — DEWEY to re-confirm on the next energy run).
- **S&P DJI US HY Corporate Bond Energy Index** free-tier page as a *second* monthly proxy — tracking-vs-ICE validation not completed this run.
- Confirmed current **ICE energy sub-index ticker code** (H0EN-family not positively pinned against ICE's own docs).
