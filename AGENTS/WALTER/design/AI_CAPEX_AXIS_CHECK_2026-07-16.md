# AI_INFRA_CAPEX axis check + VULCAN filter adjudication — 2026-07-16

**Status:** COMPLETE. Verdict delivered, WALTER-verified. **✅ ALL 4 FIXES LANDED same-day** — see §5.
> **✅ CLOSED 2026-07-16 ~21:00Z.** **Fixes 1+2 (intake) landed by PROME** in RESEARCH-INTAKE `faddb1e` — *WALTER independently re-verified in the live lane, not taken on report:* **MU CIK `723125` in `fetch_edgar_8k.py` TARGETS ✓** · **`memory-cycle` (TrendForce/DRAM/NAND/HBM) + `ai-capex` queries in `newsweep_config.py`, both tagged `VULCAN` ✓** (VULCAN is now the **first agent added to the lane's coverage since April** — agent set 9 → 10) · **the `fred` retry patch is live ✓** (PROME mock-tested 504→retry→success + 403 fail-fast, then live-tested all 4 dropped series; **MORTGAGE30US 6.55 confirms the lost-alert case**). **Fixes 3+4 (WALTER's) landed in CLUSTER_TAXONOMY v0.6** — `cluster_secondary` **forward-only + grandfathered** (Will's call) and the **bidirectional revisit trigger**.
> **Registered testable checkpoints (both sides):** **MU FQ4 ~2026-08-04 must surface in the lane** · **the first TrendForce hit ends the 0-in-764 streak.** If either fails, the fix failed — flag PROME.
> **Still open (not WALTER's to close):** the **fleet-wide intake coverage sweep** (11 agents still uncovered — **PROME surfaced it to Will as a decision and recommends yes**; a lane-side "Tier-1 with no intake coverage" doctor check = the analog of WALTER's #21) · **VULCAN's 5-axis re-cut** (recorded, not adopted — needs Will + the live VULCAN) · **the obsolescence angle** (§8 — nobody in the fleet owns hyperscaler depreciation schedules).
**Provenance:** Will-directed. WALTER ran the axis check; **VULCAN adjudicated the filter question** (spawned read-only subagent booted into VULCAN's real state — *not* the live VULCAN session; the live VULCAN should ratify). Every load-bearing claim below was **independently re-verified by WALTER** against the repo — see §4.

---

## 1. The question WALTER asked

The axis check found `AI_INFRA_CAPEX` (23 signals) had **concentrated, not fragmented**: financing 13 (~57%), ROI ~5, **obsolescence 1 (stale since 5/11)**, **input-cost 1**, power 2, muni/fiscal 1. The 6/6 taxonomy lock's premise — *"4-angle agreement [financing + obsolescence + input-cost + ROI] is load-bearing"* — was therefore dead.

**WALTER asked VULCAN the self-incriminating version:** did those angles genuinely stop mattering **(a)**, or **has WALTER's filter been killing them (b)**, or were they never separate axes **(c)**?

## 2. VULCAN's verdict — WALTER asked the wrong layer

| Angle | Verdict | Confidence |
|---|---|---|
| **Input-cost** | **(b) — WALTER's fault, but NOT the filter. An INTAKE gap + a CLUSTERING miss.** The gates never saw the news. Emphatically not (a) — it is the hottest read in VULCAN's domain. | **HIGH** |
| **Obsolescence** | **(c) primary / (a) secondary** — never an independent axis; it is the depreciation input to ROI, with no standalone observable series. | **MODERATE — thin, and VULCAN says the thinness is its own** |

**🔑 The finding: the filter is CLEAN. The failure is real but sits one layer upstream.**

> **"Your cluster count is measuring your taxonomy, not my domain."** — VULCAN

### The gates: 6 relevant kills, 6 correct — zero filter failures

VULCAN swept all 270 `kill_log` rows for semi/memory/obsolescence/input-cost and found **no false-positive kills**. It explicitly refused to manufacture one. The only near-miss **exonerates the gates twice**: the 7/10 *"DDR5 **consumer** pricing rolling over"* item was (i) unquantified advocacy with no source figure → **Credibility kill is correct**, and (ii) **consumer spot ≠ server contract** — VULCAN's actual S2 trigger series is the *server contract* price, so the claim **could not have touched its trigger even if true** (the fleet's `[[finding_proxy_segment_masks_trigger_series]]` class).

### Mechanism 1 — INTAKE GAP (the big one)

VULCAN's live S2 (memory-cycle) read is built on primaries **WALTER does not ingest at all**:

| Source | Datum | In BOARD (494) | In kill_log (270) |
|---|---|---|---|
| **TrendForce** (3/31, 6/1, 6/22) | DRAM **+58-63%** / NAND **+70-75%** QoQ | **0** | **0** |
| **Micron FQ3 FY26** (6/24) | Rev **$41.46B** vs $32.75-34.25B guide; DRAM **+207% YoY**; can fill only **50-67%** of demand | **0 as a signal** | **0** |

**The largest single input-cost datum in the domain — a ~$7-9B guidance beat confirming a structural supply deficit — never entered WALTER.** It wasn't killed; **it was never seen. There is no filter verdict on a document the filter never received.**

**Root cause:** WALTER's intake = Will's Telegram drops + the RESEARCH-INTAKE lane (EIA / EDGAR-8K / Treasury / CFTC / FRED / newssweep). **Company earnings releases and trade-research price prints sit outside all six.**

### Mechanism 2 — CLUSTERING MISS

The memory signals **are** on the BOARD — filed by **geography, not mechanism**:

| Signal | Content | Filed |
|---|---|---|
| SIG-W-20260626-001 | KOSPI AI/semi crash, **Samsung/SK Hynix −9%**, circuit breakers | `ASIA_CHINA` |
| SIG-W-20260628-005 | KOSPI 5 halts; Goldman leveraged **Samsung/SK Hynix** ETF loop | `ASIA_CHINA` |
| SIG-W-20260702-007 | KOSPI new low; driver = **SK Hynix −11.5% / Samsung −8.5%** | `ASIA_CHINA` |
| SIG-W-20260627-002 | **SanDisk NAND** RSI 99.01 "most overbought ever" | `POSITIONING_VALUATION` (secondary **AI_INFRA_CAPEX** ✓) |

**Memory-cycle signals wearing an Asia costume.** The angle isn't dead — **it's shelved in the wrong aisle.**

### VULCAN's correction to WALTER's own count

**The "1 input-cost signal" (SIG-W-20260627-018, Apple/CXMT) is not a clean input-cost signal** — its own header reads `domain: ASIA_CONTAGION`, its payload is a Pentagon-blacklist export-control story, and its input-cost content is **one clause**. **The input-cost axis has effectively ZERO clean signals in the cluster, not one.** *(WALTER verified: header confirmed `ASIA_CONTAGION`.)*

## 3. WALTER's correction to VULCAN — `cluster_secondary` is NOT unused

**VULCAN's rec #3 says the field is "already shipped in FORMAT_SPEC v0.8 and unused here." That is wrong, and the correction cuts in a useful direction.**

**15 dispatched signals already carry `cluster_secondary: AI_INFRA_CAPEX`** — so the cluster's true footprint is **23 primary + 15 secondary = 38 touching signals**, not 23. The field is used and working; the KOSPI memory trio simply points its secondary at **`POSITIONING_VALUATION`** instead of `AI_INFRA_CAPEX`.

**Two consequences:**
1. **The clustering miss is narrower + more precise than VULCAN framed it** — not "the field is unused" but "the field is pointed at the wrong secondary for the memory class." Cheaper to fix, and it means the mechanism already works.
2. **It independently strengthens the KEEP + cap-40 call** — a real footprint of **38 against a cap of 40** makes the old cap of 15 even more clearly an artifact. *(Ratified separately: CLUSTER_TAXONOMY v0.5.)*

## 4. WALTER's verification of VULCAN (Critical Rule #3 — agent data can be hallucinated)

**Verified BEFORE acting, and deliberately harder because the verdict exonerates WALTER — a comfortable answer deserves more scrutiny, not less.**

| VULCAN claim | WALTER check | Result |
|---|---|---|
| TrendForce: 0 across BOARD/kill_log/route_log | grep all three | ✅ **0 / 0 / 0 — CONFIRMED** |
| Micron: 0 as a signal | grep BOARD | ✅ **CONFIRMED** — 4 files mention it, **none is a Micron signal** (2 passing mentions + INDEX + the Apple/CXMT signal) |
| SIG-627-018 header = `ASIA_CONTAGION` | read header | ✅ **CONFIRMED** |
| KOSPI trio filed `ASIA_CHINA` | read headers | ✅ **CONFIRMED** (secondary = `POSITIONING_VALUATION`) |
| 7/10 DDR5 kill = unquantified advocacy | read kill row | ✅ **CONFIRMED** verbatim |
| `cluster_secondary` unused here | grep BOARD | ❌ **REFUTED — 15 signals carry it** (see §3) |

## 5. Pending fixes — NONE APPLIED YET

| # | Fix | Layer | Owner | Testable by |
|---|---|---|---|---|
| **1** | Add **Micron (CIK 0000723125)** to RESEARCH-INTAKE `edgar_8k` watched companies | **Intake** | **PROME** (lane is READ-ONLY to WALTER) | **Micron FQ4 ~8/4/26** — if it doesn't surface, the fix failed |
| **2** | Add **TrendForce** to the `newssweep` query set (**0 hits across all 764 archive rows**) | **Intake** | **PROME** (same) | Next TrendForce monthly print |
| **3** | Point `cluster_secondary` at `AI_INFRA_CAPEX` for the memory class | **Clustering** | **WALTER** | Re-run the axis count with secondaries |
| **4** | **Rewrite the 6/6 revisit trigger** | **Governance** | **WALTER** (needs Will — structural) | Backtest vs the 23 |

**⚠️ Fix #3 collides with post-dispatch immutability** (FORMAT_SPEC: *"pre-dispatch flexibility, post-dispatch immutability"*). Retro-editing `cluster_secondary` on dispatched signals is **not** obviously sanctioned — only `status`/`status_ref` are retro-applicable. **Likely resolution: forward-only, with the existing rows grandfathered** (the `INFLATION_TRANSMISSION` v0.2 precedent). **Needs a decision before applying — do not silently retro-edit.**

**Fix #4 is VULCAN's sharpest catch and is WALTER's own spec bug.** The 6/6 trigger — *"revisit only if angles fragment beyond 4 distinct axes"* — **fires in one direction only. It cannot detect concentration, which is the failure mode that actually occurred.** That makes it unfalsifiable-in-practice. VULCAN's proposed replacement, per the bidirectional-flip discipline: *"revisit if angle count >5 **OR any original angle falls below 2 signals in 60d**."* **Under that rule WALTER would have fired on 6/27 — without Will having to ask.**

## 6. What VULCAN says WALTER must NOT change

**Do not touch the filter gates.** Zero false-positive kills in 270. **"Changing a gate on this evidence would be a regression."** Also: the §2 substance-vs-financing boundary (ROUTING_TABLE v0.18) is **right — don't soften it**; it matches VULCAN's AI-credit seam with LIQUID (VULCAN owns the capex/fundamentals mechanism, LIQUID the spread tells, reconcile to ONE figure).

## 7. The 4-angle frame — VULCAN says re-cut it, but not by deference

**"Different objects":** WALTER's frame answers *"does the buildout continue?"* (a **question** frame); VULCAN's is `event → mechanism → repricing` (a **transmission** frame). Forcing a merge breaks both. But the 6/6 angle-set is mis-cut on its own terms:

- **Financing** ✅ keep — the real one (57%), the mechanism by which capex actually gets cut
- **ROI** ✅ keep — the demand-side question
- **Obsolescence** ❌ **demote → sub-facet of ROI.** No independent observable series; **it IS the depreciation input to the ROI calc**, already folded into SIG-626-008 (FCF crater) + SIG-626-031 (Oracle −$23.7B). **A 2-month gap is expected behavior, not decay.**
- **Input-cost** ✅ **promote + rename → "memory / supply-cost cycle."** The one angle with a genuine independent price series and its own live trigger — **and the one WALTER is structurally blind to**
- **Power** ✅ formalize (already 2 signals; VULCAN's S3) · **Muni/fiscal** → spillover facet of financing

**Proposed 5 axes:** `financing · ROI (incl. obsolescence) · memory/input-cost · power · supply-chain-geopol`. **VULCAN's own caveat: "arrive there by the reasoning above, not by deference to my frame. Mine is a month newer; that doesn't make it correct."**

## 8. ⚠️ The obsolescence verdict is a HYPOTHESIS, not a finding — VULCAN's own words

**VULCAN disclosed a disqualifying gap in itself, unprompted, and it must not be smoothed:**

> *"I have **zero obsolescence coverage.** `grep -rin 'depreciat|useful.life|obsolescen'` across my whole directory returns **only your note**. No channel of mine owns depreciation schedules. **I was built 7/10 — I have no coverage of the 5/11→7/10 window you're asking about.** So I **cannot certify (a)** from evidence. What I gave you is a **structural** argument (no independent series → episodic by nature), not an empirical one. **If a hyperscaler extended server useful-life in a Q2 10-Q and you missed it, that's a real (b) I am not equipped to see.**"*

**So the obsolescence angle remains genuinely OPEN.** Hyperscaler depreciation-schedule extensions are a live, real controversy; **nobody in the fleet currently owns them.** Treat §2's (c)/(a) as unresolved until someone with coverage tests it.

**A finding that isn't about WALTER:** obsolescence/depreciation is squarely AI-capex-systemic — the earnings-quality leg of VULCAN's S1 FCF-compression read — **and no VULCAN channel owns it.** The **live VULCAN** should decide: S1 sub-read, or channel promotion. **VULCAN's to fix, not WALTER's.**

---

## Process note — "idle ≠ reported" fired again, same day

**VULCAN went idle without delivering. Its work was complete; only the delivery failed.** WALTER chased via `SendMessage` rather than assuming failure — and got a full deliverable back immediately, citing DEWEY's finding from **earlier the same day** (*two sub-agents idled without reporting; both delivered complete work on chase; neither had actually failed*). **Third instance in one day. `[[finding_workflow_scratch_crash_recovery]]` — a declared gap is not a real gap until you chase it.** Read-only guardrail held: **zero writes, zero commits.**
