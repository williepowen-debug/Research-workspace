# VULCAN — STATUS

**Last Updated:** 2026-07-12 (first real session post-build — S1 capex quantification + S2/S4 first pulls) · **Status:** 🟠 elevated (S1 quantified; capex still being RAISED not cut — NOT-FIRED; first hard gate 7/22)
**Class:** Market-agent (AI-capex/semi/memory → systemic risk) · **Spawnable by:** PROME or Will · **Maturity:** L2 (first live pulls landed; S1 baseline quantified pre-print per PROME's hard-clock ask)

> **2026-07-12 session:** delivered the S1 pre-print capex baseline (all 4 hyperscalers, Q1 CY26 actuals + FY26 guides, sourced+dated) ahead of the 7/22 GOOGL gate and the 7/29-31 hyperscaler cluster, per PROME's routing. Closed the S2 and S4 first-pull gaps (both were open since 7/10). S3 (compute→MW) remains the one open gap — deliberately deprioritized this session for the hard-clock S1 work; flagged as next session's top item. Full row-level sourcing → `workbook/KB.tsv` (KB-VULCAN-005 through 015); full baseline table → `THESIS.md` S1 section.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **S1** | AI-capex concentration | **3 🟠** | QUANTIFIED: Q1 CY26 agg capex $129.8B (+80%YoY); FY26 agg guide ≈$710-725B (+77%YoY); Mag-7 32.5% (below 33% yellow); universal FCF compression all 4 names same quarter | root of S3+S5 (capex disappoint drives all) | [KB-VULCAN-005..011, 4/29-7/12/26] MSFT capex $31.9B (miss)/$190B guide · GOOGL $35.67B/$180-190B · AMZN $43-44B/~$200B · META $19.8B/$125-145B | Mag-7 ≥40% + breadth collapse OR hyperscaler capex cut YoY → 5. **First gate: GOOGL 7/22/26 (VULCAN-03)** |
| **S2** | Memory cycle | **2 🟡** | LIVE READ ESTABLISHED: TrendForce 2Q26 DRAM +58-63%/NAND +70-75% QoQ, Micron beat + demand-deficit confirm — accelerating UP, no roll; feeds S1 as cost-push (new link) | independent (memory cycle), but now a confirmed *input* to S1 | [KB-VULCAN-012/013, 3/31-6/24/26] TrendForce 2Q26 forecast; Micron FQ3 FY26 $41.46B rev beat | contract price −25% QoQ (cycle roll) → 4. Next test: SK Hynix 7/23/26 (VULCAN-04) |
| **S3** | AI-capex → power demand | **2 🟡** *(gap persists)* | inherited link only — not addressed this session | shares AI-capex antecedent w/ S1 | ⚠️ links to WATT P3 (datacenter buildout live); **VULCAN owes the compute→MW sizing** — now has hard $ capex figures to seed it | datacenter capex → grid-load imbalance confirmed w/ WATT → 3 |
| **S4** | Supply-chain / geopolitics | **3 🟠** | live read established: TSMC May rev +30.1%YoY (no stress); genuine two-sided pull — US eased (H200-China) vs Taiwan tightened (7/1 first criminal AI-chip detention) | independent (Taiwan/policy) | [KB-VULCAN-014/015, 6/10-7/1/26] TSMC monthly rev filing; BIS press release; Taipei Times 7/1 detention report | equipment ban / fab cutoff OR Taiwan kinetic (HAWK) → 4/5. Next test: TSMC delayed print 7/13/26 (VULCAN-05) |

**Composite: 10/20** *(S1 3 + S2 2 + S3 2 + S4 3, up from 9/20 at build. S3 unchanged — the one persisting gap.)*

**Independence note:** an AI-capex ROI disappointment drives S1 (concentration), S3 (power demand rolls over), and S5 (financing stress) at once — count the shared root once in any composite-stress call. S2 (memory cycle) is no longer purely independent — this session found it's also a *direct cost-push input* to S1's capex-guide raises (MSFT quantifies ~$25B of its $190B guide as pricing effect). S4 (Taiwan/policy) remains the cleanest independent root.

---

## LIVE CHANNEL READS (sourced + dated)

- **S1 — AI-capex concentration** [KB-VULCAN-005..011, 2026-04-29 to 07-12]: **quantified.** Q1 CY26 aggregate hyperscaler capex ≈$129.8-130.6B (+80% YoY); FY26 aggregate guide ≈$710-725B (+77% YoY vs $410B 2025) — every one of MSFT/GOOGL/AMZN/META raised guidance at the Q1 print. Mag-7 ≈32.5% of S&P 500 (below the 33% yellow line). The load-bearing new fact: **FCF compression is now universal, same quarter, across all 4 names** — AMZN TTM FCF −95% YoY (near-zero against ~$200B guide), GOOGL FCF margin 21%→9.2%, MSFT FCF −22% YoY. VIOLET's Path-B (index concentration/leverage) remains 🔴, now with its fundamental driver attached. Market is already pricing it: NDX-SPX 3m IV dispersion hit 10.2 on 7/2/26 (2nd-highest ever) [VIOLET board_log SIG-W-20260702-017]. **NOT-FIRED** — capex is still being raised, not cut. First hard gate: **GOOGL 7/22/26** (VULCAN-03).
- **S2 — Memory cycle** [KB-VULCAN-012/013, 2026-03-31 to 06-24]: **live read established.** TrendForce 2Q26 forecast: DRAM +58-63% QoQ, NAND +70-75% QoQ — accelerating up, not rolling; structural shortage, no capacity relief before late 2027/2028. Micron FQ3 FY26 (6/24/26) beat guidance by ~$7-9B (rev $41.46B vs $32.75-34.25B guide), CEO says can fill only 50-67% of demand. **New link:** this directly feeds S1 — MSFT and META both cite component/memory-cost inflation as explicit capex-guide-raise drivers (MSFT: ~$25B of $190B guide = pricing). Next test: SK Hynix 7/23/26 (VULCAN-04).
- **S3 — AI-capex → power demand** ⚠️ GAP PERSISTS: inherited link only — datacenter buildout is live (WATT P3, HENRY HEN-36). **VULCAN owes** the compute→MW demand sizing that WATT then prices. Deliberately not addressed this session (S1 hard-clock took priority per PROME routing); now has hard $ capex figures (KB-005..009) available to seed the sizing next session.
- **S4 — Supply-chain / geopolitics** [KB-VULCAN-014/015, 2026-01-13 to 07-01]: **live read established.** TSMC May'26 revenue +30.1% YoY (record) — no chokepoint stress on the revenue line; June print delayed to 7/13/26 (VULCAN-05). The export-control picture is genuinely **two-sided**, not one-directional: US *eased* (BIS approved H200-to-China sales 1/13/26, ~10 buyers cleared by 5/14/26, paired with a 25% tariff) while Taiwan *tightened* (weighing a Foreign Trade Act amendment to criminalize unauthorized AI-chip exports to all of China; first concrete enforcement event 7/1/26 — Keelung court detained 3 Super Micro/Albatron execs, Taiwan's first criminal AI-chip-diversion probe). No fixed-date legislative resolver exists yet. Kinetic Taiwan risk = HAWK cross-flag; route-out pending (domain-sweep).

**Inherited cross-agent context (not VULCAN-pulled):** the 7/22–7/29 megacap earnings stack (HEN-36) is the near catalyst for S1; WATT (spun out same day) owns the power leg S3 feeds; VIOLET holds the vol expression.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| S1 | Mag-7 ≥40% weight AND breadth collapse, OR hyperscaler capex cut YoY | concentration 🔴 (VIOLET); Mag-7 32.5%; capex still growing (agg guide ≈$710-725B, all 4 names raised) | NOT-FIRED — quantified, armed for the 7/22-7/31 cluster |
| S2 | DRAM/NAND contract −25% QoQ sustained | opposite extreme: DRAM +58-63%/NAND +70-75% QoQ (2Q26 TrendForce) | NOT-FIRED — first pull done, no roll signal |
| S3 | datacenter compute→MW demand outstrips grid (w/ WATT) | needs first pull (gap persists) | NOT-SCORED |
| S4 | equipment ban / fab-level cutoff OR Taiwan kinetic | US eased (H200-China); Taiwan tightening (7/1 first criminal detention, legislation undated); TSMC rev +30.1%YoY no stress | NOT-FIRED — first pull done, two-sided read established |

**Fired-count: 0 of 4** (3 of 4 channels now have live first-pull reads; S3 the lone remaining gap). **Thesis-kill vs channel-kill:** a strong memory quarter kills S2's bearish read — NOT the concentration thesis, which migrates to S1/S3. Thesis dies only if AI-capex re-accelerates AND concentration unwinds cleanly AND memory stays healthy — multi-quarter, testable at each earnings stack. *(This session found the OPPOSITE of a memory-cycle kill: memory is the tightest it's been, and is itself now feeding S1's capex-guide raises via cost pass-through.)*

**Cleanest bidirectional flip (BRENT discipline):** the 7/22–7/29 megacap earnings — capex guides raised + FCF holding → concentration thesis intact/extends; capex cut + FCF pressure → S1/S5 fire (the systemic unwind VIOLET is positioned for). **Operationalized 2026-07-12:** GOOGL 7/22 is the first test (VULCAN-03: guide held ≥$180B + Q2 capex ≥$40B = confirms; guide cut below $180B = fires). Full cluster resolves 7/31 against the $710-725B baseline (VULCAN-01/04).

---

## OPEN ON VULCAN (next session)

1. **S3 sizing (the one persisting gap)** — compute→MW demand; hand WATT the demand driver. Now has hard $ capex figures (KB-005..009) to seed a first-pass model. Top domain-sweep item.
2. **Resolve VULCAN-03 at the GOOGL 7/22 print** — first hard test of the S1 baseline; update the matrix same day.
3. **Resolve VULCAN-04/01 at the 7/29-31 cluster** — MSFT/META 7/29, AMZN 7/30 — full aggregate vs. $710-725B baseline.
4. **Resolve VULCAN-04 (SK Hynix 7/23) and VULCAN-05 (TSMC delayed print 7/13)** — near-term S2/S4 tests.
5. **Route-outs to deliver** (see `reports/2026-07-12_domain-sweep.md`): LIQUID (FCF-compression datum for AI-credit re-arm triggers), ZHAO/HAWK (7/1 Taiwan detention event), WATT (capex $ figures for compute→MW seeding), VIOLET/HENRY (component-cost-inflation nuance inside the capex guides).
6. **Sharpen the Mag-7 weight source** — currently aggregator-cited (32.5%, ~July 2026 vintage), not a primary index-committee figure.

---

## BOTTOM LINE

**VULCAN delivered its first live quantification 2026-07-12**, ahead of the GOOGL 7/22 gate and the 7/29-31 hyperscaler cluster per PROME's hard-clock routing. **S1 is quantified, not fired:** aggregate hyperscaler capex is still being *raised* (FY26 guide ≈$710-725B, +77% YoY, every one of MSFT/GOOGL/AMZN/META raised guidance at their Q1 print), Mag-7 sits at 32.5% (below VULCAN's own 33% yellow line) — but FCF compression is now universal across all four names in the same quarter (AMZN TTM FCF −95% YoY is the standout), which is the load-bearing new fact VIOLET's Path-B and HENRY's HEN-36 didn't have before. S2 (memory) and S4 (supply-chain) both got their first live pulls this session: memory is in a structural shortage (accelerating price, not rolling) that turns out to directly feed S1's capex-guide raises via component-cost inflation — a genuine cross-channel mechanism this session surfaced. S4 revealed a two-sided export-control picture (US easing vs. Taiwan tightening, with a concrete 7/1 criminal-enforcement event) rather than simple one-way tightening. S3 (compute→power) is the one channel still an honest gap, deliberately deprioritized this session. Next: the GOOGL 7/22 print is the first real test of everything quantified here.
