# HENRY → PROME · 2026-07-31 ~11:55 ET · **Boot-document audit — 22 flags, AUDIT ONLY, no edits applied**

**Directive:** Will, via PROME — audit the boot-read document set for stale / wrong / superseded / contradictory / dead-pointered content. **No edits this round, including self-fixable ones.** `date` verified: **Fri Jul 31 11:40:34 EDT 2026**.
**Method:** opened every line cited below in the file itself — no check-tool output taken on faith (my 7/31 hard trigger, applied to myself here). Where a current fact is asserted I name the source. Anything I could not verify is labeled **UNVERIFIED**.

## Scope — what my boot protocol actually reads (enumerated, not assumed)

| Surface | Boot role | Verified how |
|---|---|---|
| `CLAUDE.md` | auto-loaded (launch-dir) | read in full |
| `STATUS.md` standing sections | boot step 1 | read in full |
| `LESSONS.md` · `MEMORY.md` | boot steps 2–3 | read in full |
| `workbook/PREDICTIONS.tsv` | **content-read** by `boot.py` (due-scan) | `boot.py:189` |
| `VX.tsv` · `KB.tsv` · `FLOW.tsv` · `MARKET_DATA.tsv` · `board_log.tsv` | **mtime-checked only**, not content-read | `boot.py:230-235` |
| `workbook/PUBLISHED.tsv` | consumer-check input | `boot.py:370` |
| `NEXUS_BRIEF.md` | **peer-facing** — read by NEXUS + domain agents at *their* boot | CLAUDE.md FILES |
| `domain/REFERENCE_TABLES.md` · `domain/ECON_CALENDAR.md` | referenced-as-authoritative by CLAUDE.md | CLAUDE.md:176,219 |

⚠️ **Distinction that matters for seed ③:** *content-read* vs *mtime-checked* vs *referenced-as-authoritative* are three different things, and the rot is concentrated in the third.

---

## A. STRUCTURAL — highest severity

### 🔴 A1 · `CLAUDE.md:176` — the boot doc's designated "dynamic" data pointer resolves to a dead ledger
**Says:** *"Specific CTA trigger levels + gamma flip + put wall are dynamic — pull from `workbook/VX.tsv` (VX-HEN-15.xx, VX-HEN-9.xx). **6/23 refresh** … gamma flip **~7,448** … put wall **~7,000-7,200** band, CTA sell-trigger ≈**7,200-7,365** (BofA)."*
**Wrong two ways.** (i) The hardcoded 6/23 numbers are 38 days old and the put wall is off by 200–400pts: current read **put wall 7,400 / call wall 7,550, flip ~7,458** [CBOE 14d, 3,210 contracts, `boot.py` 7/31 ~11:05 ET], and my own **published** 7/28 put-support band was **7,300–7,400**. (ii) The pointer target is itself stale — `VX-HEN-9.02` flip (6/23), `9.04` put wall (6/23), `15.06` CTA trigger (6/23), and **`VX-HEN-15.01`–`15.05` are literally marked `STALE` with `Last_Updated 2026-03-03` = 150 days.**
⇒ **A boot doc tells me to "pull the dynamic levels" from rows that are 38–150 days dead.** The genuinely live surface is `gamma_flip.py` + `workbook/PUBLISHED.tsv`, which the sentence doesn't mention.
**Class: (a)** for deleting the hardcoded 6/23 numbers · **(b)** for the real question — should the VX gamma rows be retired in favour of `gamma_flip.py`/`PUBLISHED.tsv` as canonical? That's an architecture call, not a mechanical fix.

### 🔴 A2 · `NEXUS_BRIEF.md` — 8 days stale, PEER-FACING, and wrong on four load-bearing items *(answers seed ⑤: yes)*
**`As of: 2026-07-23 ~21:00 ET`** — and other agents read this at *their* boot, so the staleness propagates outward.

| Line | Says | Current fact (source) |
|---|---|---|
| 3, 10 | HEN-36 "~55%→~80% … **Count 1 of 4**" | **RESOLVED-CONFIRMED 4-of-4** [7/31, SEC/IR primaries] |
| 3, 10 | equity-de-rate leg "**ARMED**" | **FALSIFIED as a class mechanism, 2-2** [7/31] |
| 11, 21 | HEN-42 as settled: "front-led bear flattener = **POLICY-PATH**"; **"Conviction: direction-HIGH (two legs confirmed on actuals/primaries)"** | **~55%, CONTESTED** — the FOMC-day curve fired both my DENY legs [FRED 7/28→7/29] |
| 13 | credit = "**the cleanest un-contradicted signal**"; "CCC 981 is 19bp from orange" | **DEMOTED 7/28** (the gap metric was blind to a parallel widening); **CCC 1,006, orange CROSSED** [FRED 7/30] |
| 16 | gamma flip **~7,496** · Net GEX −$45.2B · SPX 7,408.30 | flip ~7,458 · **−$3.6B** · SPX 7,444 [7/31]; **7,496 is retired** |
| 13, 20 | HY **268**; USD/JPY **163.93** "1.1 from my red" | HY **284** [FRED 7/30]; USD/JPY **159.25**, *below* yellow [7/31] |

**Seed ⑤ answered: YES — `NEXUS_BRIEF.md:11,21` states policy-path attribution as settled at "direction-HIGH," and it is the one boot surface other agents consume.** **Class: (a), and I'd rank it the single highest-priority fix in this list** — every other item misleads only me.

### 🔴 A3 · `FLOW.tsv` — the silent-rot class, confirmed *(answers seed ③)*
**Seed ③ answer, precisely: `FLOW.tsv` is *mtime-checked* by `boot.py` (LEDGERS, `boot.py:230-235`) but its contents are never read by any code — while `CLAUDE.md:182` ("Full cascade detail → `workbook/FLOW.tsv`") and the FILES table present it as authoritative.** That is exactly root §Data Hygiene's silent-rot shape: referenced-as-live, never actually consulted, quietly wrong.
**12 mechanism rows; 9 stamped `2026-03-04`/`03-09`/`03-12` (~140 days), 3 at 6/23 (38d).** Rows carrying `ARMED`/`ACTIVE` status on superseded or inverted data:

| Row | Carries | Current fact |
|---|---|---|
| `FLOW-HEN-027` **ARMED** | "HY OAS 265 [FRED 6/22] — **tightened AWAY from the 300 bracket**" | **284** [FRED 7/30] — moving **toward** it. The row is armed on an inverted read |
| `FLOW-HEN-020` **ARMED** | "HY OAS 265 [FRED 6/22]" | **284** |
| `FLOW-HEN-021` **WATCH** | "10Y 4.48 (6/23)" | **4.73** [^TNX 7/31] |
| `FLOW-HEN-019` **ACTIVE** | "Oil makes new high on second leg (**above $119**)" | Brent **$90.04** [7/31] |

**Class: (b)** — root §Data Hygiene gives exactly two legal states (FROZEN banner, or LIVE with a boot-time content-vintage alert). It is currently in the illegal middle. Ruling needed on which.

### 🟠 A4 · `boot.py:~260` — my staleness check uses the **deprecated mtime mechanism**, and fails in the silent direction
`ledger_staleness()` computes age from `os.path.getmtime(p)` and prints *"(e) LEDGER STALENESS · **mtime** vs …"*. Root `CLAUDE.md` §Data Hygiene: *"⚠️ **Never key a NEW freshness/throttle mechanism on mtime** — git sync restamps it, failing **FALSE-NEGATIVE**"* (`finding_mtime_is_corrupted_by_git_sync`, VIOLET 7/27, wording amended 7/28). `scripts/ledger_staleness.py` already prefers a content-derived `Last real data refresh:` header (PAT-044); my orchestrator doesn't call it.
⇒ **A `git pull` restamps every ledger to "fresh" and the 🔴 nag silently disappears with nothing refreshed.** Self-referential: this is the check that was supposed to catch A3.
**Class: (a)** mechanically (delegate to `ledger_staleness.py`) — flagging **(b)** only if PROME wants it fleet-consistent rather than HENRY-local.

---

## B. THRESHOLD-SPEC DEFECTS *(seeds ① and ②)*

### 🔴 B1 · `CLAUDE.md:161` — the USD/JPY orientation defect is in **two** boot docs, not one *(seed ①)*
**Says:** `| USD/JPY | >160 / >162 / >165 | Carry unwind (→ SAM) |` — identical orientation to the STATUS row I self-flagged this morning.
**Why wrong:** the rows fire on USD/JPY **rising** = yen *weakness* = the condition that **builds** a crowded carry position. **The unwind is a fast yen APPRECIATION** — which is what printed today: **163.48 [7/29] → 159.25 (−2.48%) [7/31 live]**, through all three levels **from above**, on the BOJ decision. Read literally, both docs now report "de-risked" on precisely the tape that would signal the unwind. The *label* ("Carry unwind") describes an event the *trigger* cannot detect.
**Class: (c) + (b).** SAM owns the carry call and consumes this threshold — **I should not unilaterally re-key it.** But the rows live in my boot docs and the mislabel is mine. Needs a joint SAM/PROME ruling on whether to add a downside/velocity leg or re-label the existing rows as "carry-BUILD."

### 🔴 B2 · Seed ② — **yes, and the worst instances are in the cascade table itself**
`CLAUDE.md:170-174` (mirrored in `domain/REFERENCE_TABLES.md` § CASCADE ORDER):
1. Vol-Control — VIX >23-24 → **$200-400B AUM** · 2. Short-Term CTAs — SPX < 50-DMA → **~$100B** · 3. Medium-Term CTAs — **~$80B** · 4. Long-Term CTAs — **$40-60B** · 5. Risk Parity — **~$1T AUM**
**Every trigger is a LEVEL (VIX/SPX); every dollar magnitude is decorative and has never been tested by anything** — the exact class as my "~$290-320B annualized" capex band that turned out ~2.3× low. **Worse here:** my own `NEXUS_BRIEF.md:24` records that **DEWEY confirmed the precise CTA/levered-ETF quanta are *not publicly sourceable*** and instructs *"do not cite the $464bn levered-ETF figure"* — yet the cascade table presents **five unsourced dollar figures as fact** in the doc I read every boot. **Class: (b)** — source them, or demote to explicitly-unsourced order-of-magnitude.

Two more of the same family:
- **`CLAUDE.md:180` — "With 65% of SPX volume in 0DTE"**: unsourced, undated, and contradicted by my own standing gap (see E1). **Class (b).**
- **`domain/ECON_CALENDAR.md:107` — `| ECI QoQ | >1.2% | Wage-price spiral risk |`**: per LABOR's BLS-primary work today, ECI q/q has sat in a **0.8–1.0% band for seven straight quarters** (this print 0.9%). A >1.2% trigger sits far outside the realized distribution and has never fired — **a threshold that cannot test the thing it names.** **Class: (d)** retire-or-rebase. ⚠️ **Also subject to LABOR's tripwire: from Dec-2026 data BLS re-weights ECI and removes workers' comp** — any ECI-denominated threshold must be re-checked before then; **next ECI 2026-10-30 is the last on the current basis.**

---

## C. DEAD POINTERS / SUPERSEDED ROUTING

- **🟠 C1 · `CLAUDE.md:4, :12, :119, :143` — HAWK named as my geopolitical counterparty, superseded 2026-07-12.** All four say variants of *"receives from … HAWK (geopolitical)"* / *"You do NOT own: Geopolitical risk → HAWK"* / *"You receive from … HAWK: War/geopolitical → VIX spike, risk-off."* Per `PROME/ROSTER.md:28,97` and root CLAUDE.md, **HAWK was reclassified to cross-war synthesis + dormant book on 7/12; the acute theaters split to OSPREY (Russia/Ukraine) and FALCON (Iran/Gulf)**, and acute theater signals route **direct to BRENT with HAWK cc'd**. My boot doc points me at a reclassified agent for acute war signal. **Class: (a)** mechanical, with a **(c)** confirm to BRENT/HAWK on who I should actually be reading.
- **🟡 C2 · `CLAUDE.md:222` — KB.tsv self-description drift.** Says *"108 entries (last ID ML-HEN-136)"*; actual **117 rows, last `ML-HEN-145`** (`awk` verified this session; I appended 143/144/145 today). **Class (a).**
- **🟡 C3 · `CLAUDE.md:219` — `ECON_CALENDAR.md` described as *"Release schedule **Mar-Jul** … (live docket = Jun-tail + Jul)."*** **Today is 7/31 — the live docket expires today**, and none of my tracked August+ catalysts (8/7 NFP, ~8/12 CPI, 8/29 HEN-42 resolution, 10/30 ECI) are in it. Dead-tomorrow pointer. **Class (a).**
- **🟡 C4 · `CLAUDE.md:227` — `scripts/` inventory omits `gamma_flip.py`.** It lists only `boot.py` and `credit_monitor.py`, yet `gamma_flip.py` is invoked by name at `CLAUDE.md:35` and is the most-cited tool in my last six sessions. **Class (a).**
- **🟡 C5 · `CLAUDE.md:220` — `domain/BEIGE_BOOK_MAR4_2026.md` "template for future releases."** ~5 months old, not used by any Beige Book synthesis since. Meets my own LESSONS archive test (>30d + not in the active read path). **Class (d).**
- **🟠 C6 · `CLAUDE.md:241` vs `CLAUDE.md:18` — a contradiction I introduced TODAY and want ruled, not guessed.** `:241` says `TRADE.md` is *"the domain's tradeable output — convergence threshold matrix, **position recommendations**, vol structure trades."* `:18` — the Phase-2 rule I embedded this morning — says *"HENRY focus is macro + market trends, **NOT trade-position management**."* **Two lines in the same file now point opposite ways.** This is precisely the collision an embed can create, and I'd rather surface it than pick a side. **Class (b).**

---

## D. Seed ④ — VIXCS residue on boot surfaces I did **not** touch in `1a43ce8d` · ✅ **CLEAN**

Swept `CLAUDE.md`, `NEXUS_BRIEF.md`, `LESSONS.md`, `MEMORY.md`, `VX.tsv`, `FLOW.tsv`, `REFERENCE_TABLES.md` for `VIXCS|7,496|7496|7,455|7455|7,491|7491`.
**No live-position residue.** Hits break down as: (i) `NEXUS_BRIEF.md:16` carries **~7,496 as a current gamma level** — stale as a *level*, but it is **not** a VIXCS/kill-line reference (the brief is 7/23, predating the 7/27 fill); folded into **A2**. (ii) `MEMORY.md:62,72` and `LESSONS.md:84,93` — the retraction record and the two lessons, which **should** contain those strings. **Nothing to retract.**

## E. Seed ⑥ — capabilities boot docs assert that do not exist

- **🔴 E1 · `CLAUDE.md:95` mandates a field that is known to be unobtainable — and `:180` states a hard number for it.** `:95` (OUTPUT RULES): *"**VOL REGIME:** Maintain a 5-line block … current VIX, term structure shape, vol-control threshold status, **0DTE share**, GEX regime. **Update every session.**"* But **0DTE share has been PENDING for months** (standing gap in STATUS), and `NEXUS_BRIEF.md:24` records **DEWEY's finding that the precise quanta are *not publicly sourceable*.** Meanwhile `:180` asserts **"65% of SPX volume in 0DTE"** as fact. **`:95` and `:180` cannot both be right, and `:95` mandates work that cannot be done.** **Class (b)** — source it, drop the field, or record it as structurally unavailable (the honest option; DEWEY already did the work).
- **🟠 E2 · `CLAUDE.md:35` advertises a wall read the tool cannot always deliver.** Boot step 3c describes `gamma_flip.py` as producing *"flip / net-GEX / **call+put walls**"* with a free-tier caveat covering only the **$B assumption**. It does **not** warn that wall output can disagree **across horizons** — on 7/29, 14d gave 7,500/7,300 while 35d gave a broken **7,000 = 7,000** tie on *both* walls, and I published no wall level that session. The existing near-tie guard checks only *within* a horizon. Logged in `MAINTENANCE.md` 7/29, still unfixed. **Class (a)** for the doc caveat now · **(b)** for whether to build the cross-horizon check.

## F. STATUS.md standing sections

- **🟡 F1 · THESIS section header still self-dates to 7/28** — *"…what is left is one macro driver and a credit signal I was mis-measuring (**re-framed 7/28**)"* — while Axis 2 beneath it was rewritten today and ACTIVE THRESHOLDS above it are 7/31. Axis 1 and Axis 3 bodies remain 7/28-vintage. **Class (a).**
- **🟠 F2 · Two boot instructions conflict on where data releases are logged.** `CLAUDE.md:190` (DATA RELEASE PROTOCOL): *"When a macro data release drops … **log immediately in STATUS.md**."* `CLAUDE.md:237`: *"**Data release entries go in KB**, not a separate log."* Practice has drifted to KB — I put ECI in `KB.tsv` today, consistent with `:237` and inconsistent with `:190`. Symptom: STATUS's `DATA RELEASE LOG` holds only May PCE (6/25) and June NFP (7/2) — **June CPI (7/14), the 7/29 FOMC and today's ECI are absent.** **Class (b)** — pick one home.
- **🟡 F3 · INVALIDATION TRIAD carries stale as-of stamps** — SPX leg *"FIRED, still untested"* against a **7/27** settle; VIX leg [7/27]; HY leg [7/24]. The standing rules are fine; the state stamps are 4–7 days behind the threshold table in the same file. **Class (a).**
- **🟡 F4 · `VX.tsv` header banner has no dated rewrite trigger.** It self-warns: *"Rows still flagged LIVE below (21.02/21.03/21.04/20.04/20.05) are Mar-war-regime relics pending a cleanup pass — **do NOT read their LIVE status as a current call**."* The cleanup has been "pending" since ~6/23 (**38 days**), and `VX-HEN-20.01` still reads *"HY OAS Corrected Level (Mar 4) — 297bps — **LIVE**"* (current 284, 150-day-old row). My own auto-memory `finding_banner_is_a_warning_not_a_fix` says pair every banner with a **dated** rewrite trigger. **Class (b)/(d).**

---

## Disposition summary

| Class | Count | Items |
|---|---|---|
| **(a)** self-fixable mechanical next session | 9 | A2 *(highest priority — peer-facing)*, A4, C1, C2, C3, C4, E2-doc, F1, F3 |
| **(b)** needs Will/PROME ruling | 9 | A1-architecture, A3, B1 *(with SAM)*, B2-cascade, B2-0DTE, C6, E1, E2-build, F2, F4 |
| **(c)** owner-owed by another agent | 2 | B1 (SAM — carry-unwind semantics), C1 (BRENT/HAWK — war routing) |
| **(d)** delete/retire candidate | 3 | B2-ECI-threshold, C5, F4 |

**The three I'd fix first if given one pass:** **A2** (peer-facing, actively misinforms other agents' boots, and it's the seed-⑤ hit), **A4** (a staleness check that fails silent is worse than none — it is why A3 rotted unnoticed), **A1** (my boot doc points at 150-day-old rows for "dynamic" levels).

**Pattern worth naming across A1/A3/A4/F4:** four independent instances of *a surface that advertises its own liveness while being dead* — a "dynamic — pull from here" pointer, an authoritative-by-reference ledger, an mtime check that self-heals on `git pull`, and a banner with no expiry. **Each was individually invisible; the class is what makes them findable.** Related to `finding_passive_surface_rot_push_not_dashboard` and `finding_banner_is_a_warning_not_a_fix`.

**UNVERIFIED / bounds on this audit:** I did not audit `archive/`, `research/`, `sources/`, or `evals/` (not boot-read). I read `REFERENCE_TABLES.md` for the cascade + GCVR blocks but did not line-audit its full contents. `MAINTENANCE.md` and `LAST_COMPLETION.md` are write-surfaces, not boot-reads, and were excluded. I did not verify DEWEY's "not publicly sourceable" finding at its own source — I am relying on my own `NEXUS_BRIEF.md:24` record of it.

**No edits applied. No thresholds moved. No files touched outside `AGENTS/HENRY/outbox/`.**

— HENRY
