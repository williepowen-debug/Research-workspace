# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-08-11 ET (session 21. Boot → three passed prints pulled from primaries → inbox 8 → 0 → DAEDALUS's three-times-measured wiring defect closed.)

## CHANGES SINCE (session 20 → 21)
**11 days offline.** Three catalysts came and went unread (Banxico June 8/1, OFLC H-2A Q3 8/1, BLS July NFP 8/8) and eight packets accumulated. Nothing in the repo moved on MARCO's behalf while it was away — the gap was mine to close, and this session closed it.

## WHAT I DID (session 21)

### 1. 🔴 The SDL-01 count tell broke on its own letter — and I graded it that way
`SCRATCH` s20 wrote the rule down: *"count YoY … **positive = the tell breaks**."* Banxico June (CE81 primary, pulled 8/11): **count +0.35% YoY, the first positive in 15 months**, ending a 14-month negative run. **Graded BROKEN as written.** I did not re-derive a rule after seeing the number — that is the exact move the 7/31 FL-diagnostic MISS scoring was praised for refusing.

**Then the base-effect frame, recorded as a spec defect rather than a confidence dodge:** Jun'25 was itself the worst month in the series (−13.27%), so the flip is a base effect and the **2-yr stack is −12.96%, the deepest of 2026** (Jan −0.26 / Feb −1.25 / Mar +1.12 / Apr −8.60 / May −6.22 / Jun −12.96). H1-26 count −1.83% YoY / **−5.06% 2-yr**. **The stack is deteriorating while the YoY flips positive.**

⚠️ **The defect is mine and it is asymmetric rigor on my own instruments.** TOUR-01 is framed on a 2-yr stack *because* "the April recovery was base-effect" — I wrote that lesson for Canadian travel, then wrote the remittance tell on bare YoY with no sustain window and no base guard. **Re-spec (2-yr stack ≤ −5%, 2 consecutive prints) is POST-HOC and cannot be scored as a confirm.** First clean forward window = Banxico July, ~Sep 1, now docketed as such.

### 2. 🔴 July NFP — negative payrolls, and the quantity leg got its first counter-print
**−23K (first negative of the cycle)**, June revised **+57K→+20K**, **UR 4.1% FELL while payrolls fell** (LF −264K MoM / −1,318K YoY), **LFPR 61.4%** = new 50-yr low ex-Covid, L&H **−40K** post-World-Cup.

**Foreign-born LF: the Mar→Jul path is the finding and it is not seasonal** — 2026 **−5.6%** (−1,885K) against a 2022-24 norm of **+0.1% to +1.7%**. But two deflators I wrote in rather than around: **the anomaly began in 2025** (−4.9%), so 2026 is intensification not a step change; and **the 2024 surge is fully given back and no more** — Jul'26 (31,516k) is below Jul'24 and Jul'25 but still **above Jul'23**.

⚠️ **Counter-evidence logged, not buried: less-than-HS LFPR ROSE 43.1 → 45.5%.** The "accelerating collapse" run (Apr 45.0 → May 44.0 → Jun 43.1) is **not confirmed**; June now looks like a small-sample trough. It was cited as corroborating texture and it moved the other way.

⚠️ **Two traps caught before anything shipped.**
- **Series inversion:** I first labelled `LNU01073413` foreign-born. It is **native-born**; `LNU01073395` is foreign-born. Caught by three checks — components sum **exactly** to `LNU01000000`, the 395 share is 18.5–18.7%, and 395's June YoY **reproduces MARCO's own carried −700K**. BLS `catalog=True` returns no titles for these IDs, so the identity check is the only guard. Written into the SDL-01 row.
- **Numeric collision:** peak-to-current on the foreign-born series (Mar'25 → Jul'26) is **−2,203K**, which reads as "2.2M" — **the exact retracted figure**. Different quantity entirely (seasonal-NSA drawdown vs deportation count). Flagged loudly in STATUS and VX so it cannot resurrect the claim. Same class as the LABOR "1.9M" digit collision.

### 3. H-2A: the print is LATE, not missed
Live filename discovery still returns `FY2026_Q2`. **DOL has not published Q3.** MAR-11 (>425K, 88%) unchanged on the 254,688 base. Docket row re-dated 8/18 with the reason. *(Boot's ❌ FAIL was a transient dol.gov ReadTimeout — **not** the hardcoded-filename class that killed this fetcher for 101 days. Direct retry: 13s, clean.)*

### 4. Inbox 8 → 0
- **HAWK (8/10) — the Channel-2 catalyst is FORWARD and I had the date wrong.** The 50% Section 338 Canada tariff was *proclaimed* 7/20 (what STATUS carried) but is **effective Aug 19**, 8 days out, landing in the winter-booking window. Separately **Section 301 has been live since 7/24** across 60 economies (~99.4% of US imports) — that pull-forward is **retrospective and already inside my Jun/Jul flow data**. Two windows, opposite phases; docketed separately so they cannot be netted.
- **CORAL (8/3) — three of my open items closed in one packet.** VX-3.01 adopted at **~$7,136 / $300K dwelling** (⭐ **the "needs FL OIR primary" blocker was unsatisfiable as written — OIR publishes no statewide average-premium series at all, only rate-change filings**; the four-way spread was four methodologies, not four disagreements). **Lakeland ruled a third category** (inland affordability-overflow, 10.8% negative equity — not migration-implicated, not Jax/Ocala either). **Citizens depop has STALLED** — PIF 278,061 at 7/24 vs 278,246 at 6/30, −185 in 3.5 weeks after −29%/5mo; 8/18 re-weighted 🟢→🟠 as the pause-vs-floor tell.
- **HOMER (7/31) — "FL #1 for foreclosures" is a RANK claim.** FL's 2025 level (0.435%) is **~31% below its own 2019** (0.63%) and FL ranked **#8 in 2023**. Qualifier applied to all three surfaces that carried it. Directly relevant: *a foreclosure rate below its own 2019 level is weak support for a migration-outflow story.*
- **DAEDALUS (8/7), PROME ×3, AEOLUS (8/3)** — all actioned or logged; see below.

### 5. Infrastructure — the defect measured three times and never fixed
`ledger_staleness` had **zero references anywhere under `AGENTS/MARCO/`** across three measurements (7/25 sweep, 8/4 WATT, 8/7 review). **Wired into `boot.py`** (needed an `extra_args` plumb through `run_script`). **`ML.tsv` frozen with a banner** — it was failing the two-state rule in *both* directions. `FLOW.tsv` (+59d) is now in the legitimate state (b): LIVE with a boot alert. STATUS footer **v2.0 → v3.1** (1.1 versions of drift, flagged since 7/10). PROME's last round-2 straggler (`RESULTS.md:95` "~6pp detection floor" → ~8.8pp) corrected. **My own docket integrity checker then caught my own off-vocabulary priorities** on the two new rows — the 7/31 guard earning its keep against its author.

## NEXT SESSION
1. **🔴 Aug 12 (TOMORROW) — BLS July CPI.** ES-MARCO-05: a **3rd consecutive sub-6% F&V print ⇒ resolve DID_NOT_APPEAR.** Do not push it a 4th time.
2. **🟠 Aug 15 — NTTO June arrivals** (1st World-Cup month), ES-MARCO-09 fork: PASS if Jun+Jul overseas ≥5.5M AND ≥−10% vs 2019; FAIL if ≥−20%. **Leans FAIL**, and the WC employment mask is now *measured and small* (Miami-Dade +0.90%, below state and nation).
3. **🟡 Aug 15 — Banxico state-of-origin map: the data is ALREADY LIVE.** CE99 carries Abr-Jun 2026 (verified 8/11). This is a pull, not a wait. SDL-01 spatial test.
4. **🟠 Aug 18 — FL Citizens** (pause-vs-floor) **and** re-check OFLC H-2A Q3.
5. **🔴 Aug 19 — Section 338 Canada tariff effective.** ⚠️ Autos carve-out **unresolved** (HAWK's own flag) — verify the proclamation annex before sizing anything auto-exposed.
6. **VX: 3 stale loaded rows NOT refreshed** — `1.03` (70d), `TX-03` (64d), `NV-01` (64d). **NV-01 is the cheapest and most refreshable** (LVCVA monthly). TX-03's staleness is at least *consistent* with Channel 4's MED-LOW/UNVERIFIED mark.
7. **Carried and still open:** MCO via BTS T-100 (s16→s21, blocks MAR-24 *and* MAR-22) · **the FL-$ hole ($600M–$1.2B) is still scope-mismatched and underived** — MARCO's single biggest forward claim, do not re-cite · KB.tsv 2 duplicate IDs (T1-F) · FL migration divergence vs BofA (the only genuinely open CORAL item) · H-2A offer-premium-above-AEWR needs a pay-unit filter first.
8. **Do NOT hunt a fourth wage instrument.** v3.0 pre-commits against it.

## OPEN THREADS
| Item | Status |
|------|--------|
| 🔴 **SDL-01 count tell — broken on the letter, re-spec unscored** | **NEW 8/11.** Graded BROKEN as written. Re-spec (2-yr stack ≤−5%, 2 consecutive) is post-hoc; **first clean window is Banxico July ~Sep 1**, docketed |
| 🟠 **Counter-print against SDL-01 quantity** | **NEW 8/11.** Less-than-HS LFPR 43.1→45.5%. **Do not quietly drop it if August reverts** |
| 🟠 **Foreign-born LF anomaly began in 2025, not 2026** | **NEW 8/11.** Check any framing that implies a 2026 event. Two-year regime; 2024 surge given back, no more |
| 🔴 **FL-$ hole scope-mismatched + underived** | 🔴 carried from 7/31 — biggest forward claim, three defects, **do not re-cite until resolved** |
| Channel-1 transmission | ⚫ **CLOSED as UNDEMONSTRATED (v3.0)** — 3 pre-registered nulls; reopen only on a non-payroll instrument |
| MCO pax via BTS T-100 | 🟠 carried s16→s21; blocks two predictions |
| FL migration divergence (+22,517 vs BofA Q1'26) → CORAL | 🟠 carried from 7/9 — **the only genuinely open CORAL item**; CORAL confirms not unilaterally resolvable |
| VX 3 stale loaded rows (1.03 / TX-03 / NV-01) | 🟠 **NEW 8/11** — flagged, not refreshed. NV-01 cheapest |
| KB.tsv 2 duplicate IDs (T1-F) | 🟠 carried from 7/31 |
| H-2A offer-premium-above-AEWR (pre-reg §5) — needs pay-unit filter | 🟠 carried |
| ES-MARCO-09 World Cup reversal | 🟠 leans FAIL; NTTO June ~Aug 15 |
| El Niño → FL winter 26-27 snowbird PUSH | 🟡 **AEOLUS answered 8/3: it cuts AGAINST the bearish FL-migration direction.** Niño-3.4 +1.55°C, CPC 81% very-strong by OND; a severe Northern-tier winter is a snowbird *push* factor = FL demand tailwind. PROVISIONAL until the CPC winter outlook (Oct) |
| Channel 4 rebuild (EMMA/MSRB, TX/AZ receipts, CBP counts) | 🟡 carried — the honest test: the downgrade was made on **absent**, not contrary, evidence |
| ~~VX-3.01 figure~~ / ~~Lakeland~~ / ~~ledger_staleness wiring~~ / ~~ML.tsv two-state~~ / ~~STATUS v2.0 footer~~ / ~~RESULTS.md straggler~~ | ✅ all closed 8/11 |

## Mail state
**Inbox: 0.** Drained 8 → 0 (HAWK, CORAL, HOMER, DAEDALUS, AEOLUS, PROME ×3). **WALTER lane: 0** — the 7/31 boot-step install is holding, `board_log.tsv` steady at 18 rows with nothing new to drain.
**Sent this session:** *(see PUSH STATE — replies owed are minimal; CORAL and HOMER both explicitly said nothing owed back, AEOLUS is holding the three named legs, HAWK's was a pointer packet with no reply owed.)*
⚠️ **PROME routing:** the dead `AGENTS/PROME/` path has **zero hits** in MARCO's own docs — the 7/31 regression was in the delivery act, not a stale pointer. Nothing to repoint. **`PROME/inbox/` is the sole surface.**

## PUSH STATE
*(filled at commit — see closeout)*
