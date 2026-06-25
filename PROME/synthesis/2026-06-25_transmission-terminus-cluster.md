# Transmission-Terminus Cluster — Shared Orchestration Brief
**Created:** 2026-06-25 ~16:20 ET · **Owner/synthesis seat:** Prome (Claude Code)
**Members:** CARL (consumer-credit substance) · CORAL (FL regional-bank CRE/condo) · REGINALD (bank terminus / integration hub)
**Status:** Pass 1 — stand up the shared grid + refresh legs.

---

## The one question this cluster exists to answer

**Does consumer-credit + CRE/condo stress actually CONVERT to realized bank losses — NCO + specific reserve build — and which banks have multiple independent paths-to-break, resolving at the ~late-July Q2 prints?**

This is the **transmission TERMINUS**: `LABOR → CARL → REGINALD`, with **CORAL feeding the FL regional-bank CRE/condo leg into REGINALD**. REGINALD is the integration hub.

**We are DOWNSTREAM of the live X1 trigger, not a substitute for it.** The live tradeable edge (credit/CCC-BB bifurcation, HY>280 + wrapper-basket X1 decoupling) is owned by LIQUID/BROCK and is *where the next event fires*. This cluster is *where it lands*. Do **not** re-derive the X1 trigger here — consume the live credit marks and ask "does it land on bank balance sheets, when, and where."

Why build this now, ahead of the catalyst: the trigger agents are already sharp (0–2d fresh); this cluster has the real build gaps and a window before Q2 prints to build the bank-landing machinery properly rather than scrambling at print time.

---

## Leg map — who owns what

| Leg | Agent | Owns | Pass-1 build |
|---|---|---|---|
| **Consumer-credit substance** | **CARL** | CC/auto/student/mortgage DQ, K-shape, the "masking holds until vintage curves load" counter-read | Grade today/imminent resolvers; refresh the stale HY-OAS counter-signal row; emit the consumer leg of the grid |
| **FL regional-bank CRE/condo** | **CORAL** | FL condo/SF/CRE → FL-bank loss leg; AMTB/USCB/SBCF/BKU canaries; per-metro convergence | Ingest the queued DEWEY packet; emit the FL-bank leg of the grid with the loss-transmission TIMING read |
| **Bank terminus / hub** | **REGINALD** | 8-channel multi-path-to-break scoring; WAL/OZK/EGBN/ZION/CFG/SSB watchlist; CCC/HY bifurcation tripwire | Build the long-flagged CCC/HY tripwire; assemble the master grid; integrate the consumer + FL legs |

---

## The shared artifact — Q2-Print Bank-Transmission Convergence Grid

REGINALD owns the master grid; CARL and CORAL each fill the rows/leg-columns in their domain so the legs slot in without a round-trip. Schema:

| Bank | Q2 print date | Stress legs feeding it (consumer / CRE-office / CRE-condo / NDFI-PC) | Each leg's predicted Q2 signal (+ owning agent) | **Single diagnostic** | Falsifier | Current read | 
|---|---|---|---|---|---|---|

- **Single diagnostic (the bar for "it's landing"):** *synchronized* criticized/classified → realized NCO **+ specific reserve build across >1 bank* in the same quarter. One bank ticking = idiosyncratic; ≥2 synchronized = transmission.
- Bank set: REGINALD — WAL, OZK, EGBN, ZION, CFG, SSB. CORAL — FL canaries AMTB, USCB, SBCF, BKU (+ VLY).
- Each row names the **owning agent per leg** so integration is unambiguous.

---

## Reconciliation rules — work as ONE cluster, no double-count, no silos

1. **FL banks: one number, reconciled.** CORAL does the bank-LEVEL FL read + loss estimate; REGINALD integrates into the fleet-wide view. Do not maintain two divergent FL-bank reads — reconcile to one.
2. **CARL's HY-OAS row == LIQUID's series.** Refresh it to the live print and frame it as CARL's *counter-signal* (credit-substance check), NOT a new independent bear signal. Don't double-count with the X1 cluster.
3. **Consumer vs CRE vs condo are distinct legs** — a bank with three feeding legs has three paths-to-break; score them independently, then ask whether they're synchronized (the diagnostic).
4. **MARCO overlap (FL migration/tourism):** CORAL flags if a MARCO-owned number is load-bearing; reconcile to one figure rather than re-deriving.
5. **Substance-vs-beta tie-in:** CARL's consumer-credit deterioration is the *substance* read that either supports or undercuts the X1 cluster's "the widening is beta" call. State your read explicitly; it's an input to Prome's synthesis, not a re-derivation of X1.

---

## Live marks — ORIENTATION ONLY (re-pull via `.venv` + `FORGE/tools/market-data/dashboard.py` before citing as current)

Post-close 6/25 ~16:04 ET: **HY OAS 276 [FRED 6/24]** · CCC 964 [6/24] · **CCC-BB tail-gap ~798** · BB 166 · banks GREEN: KRE $74.73 / OZK $51.81 / WAL $81.46 · BIZD $12.25 · APO $121.51 / ARES $112.47 · VIX 19.22 · Brent $75.49 · USD/JPY 161.80.

REGINALD's CCC/HY ratio for the tripwire: live ≈ 964/276 = **3.49×** (vs the >3.6×-sustain tripwire and the 3.56× [6/19] last mark — verify with a fresh pull).

---

## Operating contract for this cluster

- **Build in your OWN domain files** (that's your job) + fill your leg of the grid. Do not edit another agent's files.
- **Report back to Prome** (`SendMessage` to `main`) with: (a) your leg's grid contribution, (b) refreshed live numbers + as-of dates, (c) key resolvers/falsifiers + dates, (d) what you need from the other two legs.
- **Commits:** local-only OK; **NO push** (Will-coordinated). `git add` only your own `AGENTS/<NAME>/` paths.
- **Pass 1 is bounded** — build your leg + refresh, report back, then we iterate. Don't boil the ocean.

---

## Pass-1 task per agent (full detail in the spawn brief)
- **REGINALD:** triage the 6/25 WALTER inbox backlog (load-bearing-for-cluster only); build the CCC/HY >3.6×-sustain tripwire (the tie to the live root); stand up the master grid skeleton + name the leg-inputs you need.
- **CARL:** grade May PCE (today) + flag Fannie MF ~6/26 (CRL-03 resolver); refresh the HY-OAS counter-signal row (272 [Jun 1] → live); emit the consumer leg + your substance-vs-beta read.
- **CORAL:** ingest the 3 queued WALTER signals — chiefly the DEWEY Phase-3 packet (SIG-W-20260622-001, FL-bank loss-transmission timing); emit the FL-bank leg with the timing read; mark DEWEY research-not-verified-primary.

*Prome holds the synthesis seat: integrates the three legs, routes the validated bank-transmission read to NEXUS (9d-stale) as the follow-on, and surfaces the Will-facing decision when the grid matures toward the Q2 prints.*

---

## FINALIZED RESULTS — Pass 1+2 COMPLETE (2026-06-25 ~16:50 ET)

**Bottom line:** Credit stress is **NOT landing on bank balance sheets yet** — mechanism intact, transmission *lagged by extend-and-pretend*. The current 6/24 HY widening is **BETA** (3-way independent confirm). Realized synchronized bank NCO = a **2027 event**; the Q2 prints (Jul 16–30) are the **first read, not the landing**; the single diagnostic is NOT-met and **predicted still-un-met at Q2**.

**Finalized grid** (`AGENTS/REGINALD/research/Q2_PRINT_CONVERGENCE_GRID_2026-06-25.md`) — legs: O=Office, N=NDFI/PC, C=consumer, Cd=condo/CRE, R=resi 1-4 family %loans:

| Bank | Q2 (~) | Legs | Current read |
|---|---|---|---|
| **CFG** | Jul16 | **O,N,C — 3 paths** (CRE / BDC fund-fin $12.5B / consumer 18.7%) | 🟡 **multi-path standout, lead name** |
| OZK | Jul16 | O(RESG 88%),Cd | 🟠 leading, NCO benign 0.57%; IQHQ Aug |
| ZION | Jul21 | O,muni,N | 🟢 control/bull — Hyp-A hold? |
| EGBN | Jul22 | O(DC/IPRE) | 🟠 nonaccrual creep (NPA 1.04→1.31) |
| SSB | Jul24 | Cd/O (FL+TX 42%) | 🟡 NCO=2027; FL-$ [PENDING] |
| WAL | Jul30 | O,N | 🟠 idiosyncratic, $78 watch |
| AMTB | — | R25.6%, Cd/O | 🟠 most FL-pure; thin ~45% ACL → Q2 reserve-build risk |
| SBCF | — | R25%, Cd/O | 🟠 cleanest leading edge (30-89d $17.2→28.2M) but fortress CET1 14.4% |
| USCB | — | R15.5%, condo $126M | 🟡 #1 condo canary = first-crack wire (pristine now) |
| BKU | — | R24.7%, O, Cd | 🟢→🟠 loss is C&I $36M not FL-RE = "is it the mechanism" test |
| VLY | — | R11.5%, Cd/O | 🟡 weakest FL read |

**Two forward tripwires (would pull the 2027 landing earlier):**
1. **Consumer-side (CARL):** monoline Q2 NCO breaking guide WITH ACL coverage FALLING (SYF/COF/ALLY ~mid-Jul) → roll/transition-rate accelerating = extend-and-pretend breaking. Then NY-Fed Q2 HHDC (~mid-Aug).
2. **FL-side (CORAL/REGINALD):** rising 30-89d FL resi/condo at **≥2 of {AMTB, SBCF, USCB} for 2 consecutive quarters.**

Until either turns, the timing axis pins at **Q1'27 crystallization**.

**3-way beta confirmation (independent instruments):** CCC/HY tripwire DORMANT 3.49× (HY-led, not CCC-tail-led = beta) · CARL: HY index is the wrong thermometer for consumer-credit substance · CORAL: FL stress real but not landed. Independent corroboration of the upstream LIQUID/BROCK "widening is beta" call.

**Two-channel FL transmission (verified Q1'26 10-Qs):** the ~12mo insurance cost-push hits BOTH the household behind the resi 1-4 family loan (~25% of loans, CARL's mortgage-DQ lens, net ONCE) AND the association behind the condo master policy (CRE/condo, CORAL-only). Pure-HELOC overlap negligible.

**Artifacts built:** CCC/HY >3.6×-sustain tripwire (`VX-REG-18.04`, driver-decomposed, DORMANT 3.49×) · finalized Q2 grid · verified FL housing-secured reconciliation (`AGENTS/CORAL/CLUSTER_FL_BANK_LEG.md`) · CARL consumer leg (`AGENTS/CARL/outbox/2026-06-25_cluster-consumer-leg.md`) · this brief.

**[PENDING] watch-cells:** mostly RESOLVED by CORAL's verified final fill (below). Genuinely still-pending: exact SSB FL carve-out (not separately disclosed), Q2 dates vs IR calendars, AMTB/BKU Q1'26 10-Q to fully confirm the BKU-not-AMTB attribution fix.

**✅ VERIFIED FINAL FILL — CORAL 10-Q XBRL (3-31-26), commit `ee8c195e`** (resolves the [PENDING] cells; REFINES the read *toward not-landing*):
- **The 30-89d leading edge is COOLING QoQ, not accelerating** — SBCF $28.2M but **−14% QoQ** (off Q4 $32.9M peak), +65% YoY (sharper signal = nonaccrual $72→95M QoQ); AMTB +389% QoQ is **LUMPY/SUSPECT** ($52M is commercial 30-59d quarter-end timing, not consumer-resi); USCB +243% QoQ on a tiny $2.2B base (resi only $3.4M); BKU headline $234M is **gov-insured-dominated**, ex-gov ~$123M benign. Cleanest ≥2-bank synchronized = USCB+SBCF on **YoY only** — not QoQ momentum, not realized NCO. **Diagnostic NOT-met, and the cooling QoQ strengthens "not landing."**
- **SSB FL loss ≈ $0** — the $2.5B classified is **rate-shock reclass** (56% LTV / 98% current, little/no loss content), NCO 9bps; no clean FL carve-out. CORAL carries NO divergent FL number for SSB or VLY → defer to REGINALD fleet figure.
- **Condo/SIRS = confirmed 2027** charge-off event, NOT a Q2 signal (assessment-default wave hasn't hit the leading bucket; master-loan→receivership→bulk-sale is multi-quarter; USCB pristine). Faint 30-89d flicker at most late-2026.
- *Three potential misreads corrected by verification (AMTB surge / SBCF $28M / SSB $2.5B classified all look like acceleration at a glance; the 10-Q detail shows the opposite).*
*(REGINALD grid file reconciled to these verified figures — supersedes the DEWEY-grade SBCF + [PENDING] placeholders.)*

**NEXUS-handoff package (the 9d-stale synthesizer is owed):** (a) validated downstream read = "terminus not landing, 2027 crystallization, Q2 first-read predicted un-met"; (b) the two forward tripwires; (c) the cross-leg beta confirmation; (d) the CCC/HY tripwire as a standing convergence vector. Gated on Will's NEXUS refresh-hold.

**Commits:** all local-only, no push (Will-coordinated). CARL `5cbee49b`/`47742824`/`722fcb14` · CORAL `1d371108`/`245cfc52` · REGINALD (grid + tripwire, local) · Prome cluster brief (this file, uncommitted).

---

## PRE-Q2 ADVERSARIAL STRESS-TEST — Wave 1 (self-steelman) + Wave 2 (blind-spot critics + judge) — 2026-06-25 ~17:30 ET

**Pivot (Will-approved):** stress-test the cluster's own benign verdict before the Q2 prints. **VERDICT: HOLDS-WITH-ADDITIONS** — the systemic-2027 spine (synchronized *realized* charge-offs stay 2027; pre-loss cascade migrating UP) survived all 6 independent attacks, but the cluster was tuned to watch the one axis it concluded won't fire in July.

**Wave 1 — three self-steelman hits (each leg red-teamed its own benign read):**
- **CARL — category error:** extend-and-pretend is a CRE mechanism; FFIEC mandates charge-off at 180 DPD card / 120 DPD auto = unsecured is UN-MASKABLE. Consumer timeline BIFURCATES — unsecured (cards/auto→monolines) crystallizes **H2-2026**; housing-secured+CRE holds Q1'27. (committed `93ad1bca`)
- **CORAL — wrong-signed "cooling":** led with SBCF 30-89d −14% but buried nonaccrual $72→95M (+32%) + CRE-non-OO 60-89 ~10×. Cascade migrating UP. Revised FL 70/30→60/40. (committed `69256fe3`)
- **REGINALD — diagnostic altitude-mismatch:** the ≥2-bank bar is blind to single-name breaks (the trade's actual exposure). WAL REG-25 ~70%. Independently caught the same buried-SBCF-nonaccrual error CORAL did. (`AGENTS/REGINALD/research/Q2_PREREG_ADVERSARIAL_2026-06-25.md`)

**Wave 2 — three SHARED blind spots (self-critique structurally couldn't catch):**
1. **NON-CREDIT BALANCE-SHEET CHANNEL UNWATCHED (sev 7):** zero thresholds on NIM/deposit-cost/AOCI/TBV/FHLB — yet by the cluster's own logic credit is the 2027 dog-that-won't-bark at the Q2 horizon. **ZION false-control risk** — designated "control/bull," pre-registered purely on credit, but it's a classic muni/AOCI-securities-mark name ($5.78B muni); a clean-NCO print would be mis-read as "Hyp-A holds, bear disconfirmed" even if TBV/NIM break. **10Y +11bp: 4.30 [3/31] → 4.41 [6/24] ⇒ AOCI channel LIVE but mild** (re-pull at the 6/30 mark date).
2. **MONOLINES (COF/SYF/ALLY) NOT SCORED (sev 7):** CARL's own revision made the unsecured leg the FIRST + un-maskable landing path, yet the monolines have no scored grid row and print BEFORE the regionals (~Jul 15-22 vs WAL Jul 30). COF out-profiles CFG on the cluster's own multi-path criterion (largest US card issuer post-Discover + auto + commercial CRE). Domain-seam blind spot (REGINALD=CRE, CORAL=FL, CARL routed them to "tell").
3. **ONE-DIRECTIONAL SELF-CRITIQUE → WAL OVERCORRECTION (sev 6):** every leg steelmanned the bear, so synthesis could only ratchet bearish (RED, the bull-steelman owner, wasn't in the cluster). WAL ">40bps near-locked surprise" is LOW-INFO continuation (~1-4bp above Q1's 39bps run-rate; mgmt guides NCO to DECLINE H2, classifieds resolving, classified/assets −9bp to 1.08%). **Grade WAL on MAGNITUDE** (40-45bps = priced continuation; >55bps + majority of the $99M life-sci credit charged off in-Q2 = bear-confirm).
   - **+ Synthesis-layer re-benign-ing:** "stays 2027" privileges the realized-NCO half of a CONJUNCTIVE diagnostic. **Disjunctive reading:** a synchronized forced *reserve build* at ≥2 banks IS Q2 balance-sheet transmission (P&L/ACL/capital) — only realized *charge-offs* stay 2027. EGBN+AMTB ~45-50% is MARGINAL per-name; the JOINT ≥2-same-quarter prob is ~25-35%.

**Single most important watch:** WAL Jul 30 (magnitude + $99M treatment) — but watch the **monolines FIRST (SYF ~Jul 15-18, COF ~Jul 22)** = the un-maskable leading edge, currently off-grid.

**Data-integrity (judge verifications against primaries):** (a) a critic's "LAM $26M-of-$126M deferral precedent" was MISATTRIBUTED — LAM was fully charged off; the partial-deferral example is **Cantor Group Five** (conclusion survives via Cantor, cited example inverted). (b) AMTB ~45% ACL / $7.8M prov = research-grade (EDGAR 403'd, prior crashed-session misattribution corrected, 10-Q pending). (c) 60% LGD + Q2-timing on the $99M = modeled assumptions (only existence 10-Q-verified; currently nonaccrual). (d) WAL $81.48 [6/25] (was $78.76 stale [6/22]).

**ADDITIONS — IMPLEMENTED** (REGINALD grid + pre-reg, CARL leg; committed local-only): (1) **ZION re-registered on a non-credit axis** (green-NCO + falling-TBV/AOCI or NIM-compression falsifier; P~25-30%) — no longer a clean credit-only bull-control; (2) **COF/SYF/ALLY promoted to scored LEAD rows** (print first ~Jul 15-22) + **monoline-only decision rule ratified** (Axis A unsecured-H2-26 vs Axis B regional-Q1-27; monoline-only break = "masking holds, base case," does NOT flip Axis B); **COF confirmed DUAL-PATH** (card=Axis A + commercial-CRE=Axis B; out-profiles CFG, which folds to Axis-B-only); (3) **synchronized JOINT prob fixed to ~25-35%** (not the marginal ~45-50%) + **disjunctive note** (a synchronized forced reserve-build at ≥2 banks IS Q2 transmission); (4) **non-credit/balance-sheet tripwire class added** (≥2 of {ZION,WAL,CFG,EGBN} non-credit selloff → "credit-only sufficient at Q2" falsified); (5) **WAL graded on magnitude** — REGINALD corrected its own over-claim: "WAL ~70% near-locked" was P(>40bps)~70% but PRICED; **true bear-confirm (>55bps + majority of $99M charged-off) ~30-35%.** Monolines all GREEN 6/25 (SYF +2.88%) — turn not yet showing.

**FINAL HONEST READ (post-implementation):** the systemic-2027 floor holds for *realized synchronized charge-offs* — but the cluster is now **less "nothing until 2027" and more "2027 for realized losses, with three live ~25-35% Q2-able paths the green tape isn't pricing":** (a) synchronized forced *reserve-build* at ≥2 banks (IS Q2 balance-sheet transmission); (b) non-credit / AOCI selloff at ≥2 names (10Y +11bp 3/31→6/24 = AOCI live-but-mild); (c) WAL single-name at >55bps + the $99M charged off (~30-35%, not 70%). Full consolidated playbook in the Wave-2 workflow output (`tasks/wp24l3wb3.output`).

**Cluster commits (all local-only, no push):** CARL `93ad1bca`/`3fc00c17` · CORAL `69256fe3` (+ earlier `1d371108`/`245cfc52`) · REGINALD grid+pre-reg+tripwire (local) · Prome cluster brief (this file, uncommitted).
