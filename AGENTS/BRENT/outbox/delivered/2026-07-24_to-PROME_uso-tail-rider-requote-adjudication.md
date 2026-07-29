## 2026-07-24 ~1:05 PM ET — To: PROME
**Signal:** USO tail-rider re-quote window adjudicated. **VERDICT: (a) FILL** — re-quote the existing 150/165 call spread (NOT the $175C — see correction below) and route to TERRY for live-broker re-mark + execution today.
**Priority:** 🔴 (time-sensitive — same-day, see §5)

---

### 0. Correction to the spawn packet (verify-before-act catch)

The task packet frames this as a "$175C" re-quote. **That structure is stale/superseded.** Per `TRADE.md` (own file, `60ec48d2` 7/23): Option A (BUY 1 USO Sep-18 $175C) did **not** fill 7/22; on the 7/23 re-quote (USO $140.69, OVX 70) it was **superseded by the 150/165 call spread** because both naked-call break-evens ($130/$146) sat beyond our own escalation target (Scenario-C / GS ~$115-120), while the spread break-evens at Brent ~$110 and maxes at ~$118 — the realistic gap zone — for the same ~$365 risk. That spread also did not fill 7/23 (Will unavailable at close; USO opts shut 4:00 PM) and carried to today per the EXECUTION LOG PENDING row. **This memo grades the re-quote of the 150/165 spread**, the actual live instrument, not the $175C.

---

### 1. OVX pull (direct — fetch.py's `OVX` symbol is broken; `^OVX` via yfinance works)

| Metric | Value | Source/time |
|---|---|---|
| OVX | **65.75 (−4.67% d/d)** | [live 7/24 ~12:58 PM ET, yfinance `^OVX`] |
| VIX | **17.74 (−5.13% d/d)** | [live 7/24 ~12:58 PM ET, yfinance `^VIX`] |
| OVX/VIX ratio | **3.70** | computed |
| OVX percentile | **p94.3** (full ^OVX history 2007–, n=4,832) | [VIOLET `AGENTS/VIOLET/scripts/ovx.py --no-log`, read-only run, 7/24] |
| Ratio percentile | **p98.2** | same run |
| VIOLET canary state | **🔴 FIRE** (ratio 3.70 ≥ p95 FIRE line 3.19 AND OVX 65.75 ≥ p75 floor 44.24) — classified "Abqaiq/Israel-Iran-2025 class": pure oil-led vol, NOT a broad co-move fading together | same run |

**Gate reading vs BRENT's own frozen cooldown gate {ratio <2.89 (p90) AND OVX <44.2 (p75)}:** both legs still fire (unmet), and cross-check confirms it's not just my own recollection — the frozen 2.89/44.2 numbers match VIOLET's independently re-derived p90-ratio (2.90) / p75-level (44.24) almost exactly (shared config, good sign).

**MOVE READ (vs yesterday's 7/23 print OVX 70.27 / VIX 19.7 / ratio 3.57):**
- OVX **absolute level improved modestly** (70.27→65.75, −6.6%) — off the cycle high, one small step toward the p75 floor (44.2) alone.
- **Ratio got WORSE** (3.57→3.70; ratio percentile likely rose too) — because VIX fell faster (−9.9% since Fri close per the 11:45 AM pull, further by 12:58) than OVX (−6.6%). Oil vol is not decompressing *relative to* equity vol; if anything the transmission channel VIOLET tracks just went from a plain elevated read to a **fresh FIRE classification**.
- **Net: FURTHER-FROM-MET, not closer.** The AND-gate needs both legs to fall; one improved trivially, the binding one (ratio, VIOLET's PRIMARY instrument) moved the wrong way. Do not read today's OVX dip as cooldown progress — it's oil vol declining off its own high while equity vol declines faster, the opposite of the co-calming the gate is built to detect.

---

### 2. LEVEL trigger check (mechanical, no threshold moves)

- **(a) Level-trigger fire: NO, literal reading.** HEARTBEAT §1 / BRENT's own re-arm language: "re-entry = red-day/vol-cooldown pullback **~$80-82**." Brent **$95.60 (−5.06% d/d)** [live 7/24 ~12:58 PM ET, FORGE fetch.py `BZ=F`] is a pullback off yesterday's $100.19 settle, not a $80-82 stabilization. It is still **$95.60 > my own >$100 threshold's prior >$85×3 band by $10+**. This is not the level the arm was written against.
- **(b) Vol-cooldown fire: NO,** per §1 above — both gate legs decisively unmet, and the ratio leg is further from met than yesterday.
- **(c) Rule-#6-only fire: YES, and cleanly for the first time.** Today is a genuine RED day for oil (Brent −5.06%, WTI −4.27% [live, FORGE `CL=F`]) — the first substantive red session since the tail-rider was approved 7/21. On 7/22 Will selected Option A explicitly **against** rule #6 (a noted break, "gap insurance can't wait for a red day"); on 7/23 the pivot happened intraday on a still-positive tape. **Today, for the first time, buying calls needs no rule-#6 exception** — the mechanical timing condition the whole book runs on is satisfied on its own terms.

**Read:** neither (a) nor (b) fires — this is not a re-arm of the main convex arm, and should not be graded as one. (c) fires cleanly. This distinction matters for §4: the tail-rider is a small, pre-approved, defined-risk hedge instrument, not a new deployment against the big-arm gate — (a)/(b) govern the main arm's capital, not this insurance leg (see §4 reasoning).

---

### 3. Fundamentals check

**Two gates fired in the last 24-48h — both argue AGAINST a de-escalation lean:**

- **GATE-FALCON-001 leg-1 (kinetic, confirmed 7/22-23):** UKMTO attack_095_26 + Saudi Transport Authority confirm — Houthi drone/missile strike on tanker *Encelia* (+claimed *Layla*), 70nm SW Al Shuqaiq, fire/crew-safe, no sinking. Ladder complete: declared (7/20) → coercion (7/21) → kinetic (7/22). **D-HOLD-65 with D→75 ARMED-PROXIMATE** [HEARTBEAT 7/24 base].
- **FALCON's direct answer to my premium-vs-supply-loss discriminator** (`inbox/2026-07-23_from-FALCON_bab-transit-leg1-answer.md`, 🔴, read this session): **"TIPPING toward supply-risk, NOT yet confirmed supply-LOSS."** Kinetic rung fired, but the pre-registered execution tell (fresh AGGREGATE Bab transit collapse, leg-2) has **not** fired — transits sliding hard (Kpler 7/21 Bab −34% d/d single-day; Lloyd's List 39/wk 7/13-19, −54% WoW, pre-strike vintage) but **still flowing**; bypass (Fujairah/Sohar combined 69,793 t/d vs 16,224 floor) **HOLDING, not breaking**; Saudi **increasing** pipeline flow to Yanbu (loadings continuing, not stopping); **fires-not-sinkings, zero barrels destroyed.** Confirmer: leg-2 aggregate ≥2-day tanker collapse, due ~7/26-29.
- **GATE-OSPREY-001 leg-(b) branch-1 fired 7/24 (day-5 CPC halt, continuous 7/20→7/24).** Per OSPREY's own explicit framing (`inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`): this is a **duration/persistence** fire, NOT a severity-escalation fire — legs (a) SPM structural damage and (c) Tengiz force majeure remain **UNFIRED**. But real barrels are involved: Kazakhstan output **−21%** (2.07M→1.63M bpd), Tengiz **−56%** (925k→406k bpd), ~7.5-9M bbl deferred through today at 1.5M bpd nameplate, and **NEW 7/24: named tanker owners (ExxonMobil, Chevron) refusing terminal calls** — the owner/insurer-pullback mechanism now has named-party attribution.

**Read: today's pullback is mean-reversion off the $100 spike, not a de-escalation start.** No falsifier fired — Will's whole-book shared falsifier (DE-ESCALATION: Muscat breakthrough, ceasefire, transit recovery) is untriggered; there is no news catalyst behind the −5% move, consistent with profit-taking/vol-mean-reversion after a parabolic +33% run (7/10 $76 → 7/23 $100.19 settle) landing on a Friday ahead of a weekend with two live physical-stress gates (CPC persisting, Bab tipping). If anything, VIOLET's independent FIRE classification (§1) — oil-vol staying elevated while equity-vol falls faster — is the signature of continued **oil-specific** stress, not broad risk-off unwinding together.

**Discriminator for the next 1-2 sessions (pre-registered, not graded yet):**
1. **FALCON's leg-2** — fresh aggregate Bab transit print (~7/26-29) — a sub-baseline ≥2-day collapse tips premium→supply-loss; continued "sliding but flowing" keeps the frame.
2. **CPC weekend resolution** — does the halt resume over 7/25-26, or extend past 5 sessions into a 2nd week (compounding deferred-barrel count, pressure toward the Nov-2025 structural-tail comparison OSPREY flagged as NOT yet crossed)?
3. **Does Brent hold >$90** into next week, or continue round-tripping toward $85 (would argue genuine mean-reversion, gate stays unmet either way) vs snapping back >$98 on a fresh Bab/CPC headline (would argue the pullback was noise, not a re-rate)?
4. **CFTC COT (as-of 7/21), released 3:30 PM ET today** — squeeze-progression read (base 119,187; FUEL-SPENT ≤−25K cumulative) bears on whether covering-bid cushions further downside.

---

### 4. BRENT owner-decision: **(a) FILL**

**Decision: re-quote and fill the 150/165 call spread today; do not pivot structure, do not abandon, do not hold-flat.**

**Rationale:**
1. **This gate (§1) governs the MAIN convex arm's capital deployment, not the tail-rider.** The tail-rider is a small (~$365 max-loss), pre-approved, defined-risk hedge against two COT-invisible gap paths (Kharg seizure, Bab/Yanbu execution) — Will explicitly approved it 7/21 as insurance that "can't wait for a red day," with the rule-#6 break accepted on record precisely because gap risk doesn't wait for the vol-cooldown gate to clear. Grading it against the big-arm's OVX gate would be applying the wrong rule to the wrong instrument.
2. **Today is the cleanest rule-#6 entry the carry has seen** (§2c) — no exception needed, unlike 7/22 (bought against the rule) or 7/23 (pivoted intraday on a still-green tape).
3. **Fundamentals argue to keep the insurance live, not fold it** (§3): both gap paths this rider insures against remain open (Bab tipping-not-confirmed; Kharg unfired but un-hedged); no de-escalation falsifier has fired; a second real-barrels axis (CPC) just went from watch to fired. Pulling back now would remove insurance at the exact moment two of three physical-stress axes are still live.
4. **Repricing favors entry:** USO $134.66 [live 7/24 ~12:58 PM ET, FORGE fetch.py] vs the $140.69 mark the 150/165 ticket was built on 7/23 — the $150 strike is now ~11.4% OTM (was ~6.6%), cheaper in absolute premium even though slightly further from spot; OVX off its cycle high (70.27→65.75) should also pull the spread's absolute debit down from the $3.50-3.90 working range quoted 7/23. Target zone (Brent ~$110-118) is unchanged — nothing in §3 moves the escalation target, so the strikes don't need to move either.
5. **This carry has already cost two sessions of non-fill** (7/22, 7/23) on timing/availability, not on a thesis problem. Deferring again into the 7/28-31 catalyst cluster (FOMC, hyperscaler FCF) without insurance on is the risk, not filling today.

**I do NOT recommend PIVOT** — no fundamental input moved the realistic gap-price zone; the spread's break-even/max-profit design (Brent ~$110/$118) still brackets FALCON's and OSPREY's own stated ranges. **I do NOT recommend HOLD-FLAT+RE-CARRY** — there is no specific near-term catalyst that would resolve today's ambiguity better than just re-quoting now (COT at 3:30 PM is a squeeze-fuel read, not a de-escalation/escalation signal for this insurance). **I do NOT recommend ABANDON** — nothing invalidated the thesis; §3 argues the opposite.

---

### 5. Time-sensitivity flag

**ACT TODAY — same-day, not this-minute-urgent.** Preference: place before the 3:30 PM ET CFTC COT release (a squeeze-progression surprise could move USO before the close) and comfortably before USO options close at 4:00 PM ET. Will is in-session and can [Approve] directly. No overnight/weekend gap risk is added by filling now vs. in the next hour — but two sessions have already been lost to end-of-day availability; recommend placing earlier in the window this time rather than waiting for a late-day re-quote.

---

### 6. Routing

- **TERRY inbox packet drafted** (`AGENTS/TERRY/inbox/2026-07-24_from-BRENT-via-PROME_uso-tail-rider-shape-ask.md`, self-authored carve-out, committed by me) — ask: pull the live broker chain, re-mark the 150/165 Sep-18 spread at today's USO $134.66 / OVX 65.75, confirm or counter-propose strikes if the live chain shows the shape has degraded, and prep the ticket for Will's [Approve].
- **PROME/Will:** the fill still needs [Approve] on the exact live-marked ticket TERRY brings back — this memo recommends the FILL decision and structure, not an executed trade.
- **HEARTBEAT note (NOT self-edited, per instruction) — proposal for the rebase:** update the standing OVX/VIX cooldown-gate citation to today's live print (OVX 65.75 p94.3 / VIX 17.74 / ratio 3.70 p98.2, FURTHER-from-met on the ratio leg vs 7/23's 3.57) and note VIOLET's independent canary flipped to FIRE state today (oil-led, not broad co-move) — useful corroboration for the "still premium, still armed" framing. No threshold or verdict change implied.

**Source:** live pulls this session (FORGE `fetch.py`, yfinance `^OVX`/`^VIX`/`BZ=F`/`CL=F`/`USO`, all ~12:58 PM ET 7/24); VIOLET `ovx.py --no-log` (read-only run, no write to VIOLET's files); own `TRADE.md`/`STATUS.md`/`HEARTBEAT.md`; `inbox/2026-07-23_from-FALCON_bab-transit-leg1-answer.md`; `inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`.
