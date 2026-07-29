# BRENT SCRATCH — Tue Jul 28, 2026 (night boot + full closeout: pause broken · both owed grades cleared · 36-packet inbox drain · 3 wrong-way boot guards fixed)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

---

## CHANGES SINCE LAST SESSION (Mon Jul 27 → Tue Jul 28 night)

- **🔴 THE PAUSE BROKE, AND IRAN BROKE IT.** IRGC ballistic missiles at a US base in **Jordan**, 7/28 ~5:45 PM ET, **all intercepted** per CENTCOM, no casualties/damage — first launch since the pause began ~7/24, landing during Netanyahu's first White House meeting of the war [WALTER SIG-013]. **Precision to keep: the 7/27 halt quote was the ARMY (Akraminia); tonight is the IRGC — two institutions.**
- **The pause's cause turned out to be MUNITIONS, not diplomacy** [SIG-015]: Adm. Cooper told Trump the target list was *"nearly exhausted"*; CJCS Caine warned on Patriot/Tomahawk stockpile strain. ⇒ **durable short-horizon but SILENT ON INTENT — and Iran answered the intent question by restarting.** Anyone reading the quiet as de-escalation was reading intent into a supply constraint. Cooper's framing also implies the next escalation is likelier a **STEP CHANGE** than a resumed nightly tempo.
- **Tape:** Brent **$100.69 (7/23) → $96.78 → $88.36 → 7/28 open $84.95 = the session LOW → close $87.57 → $87.74 two hours post-launch.** Peak-to-trough **−15.6%** (my 7/27 surface carried −10.5%, an intraday-basis understatement). **The bounce HELD rather than fading** — but still **−12.9% below the high.**
- **Abqaiq WAS struck 7/27 and did burn** — NASA FIRMS primary (Will-supplied): six hotspots at Abqaiq's exact coordinates, FRP to 299 MW, confidence 100 on five, **night pass** so not solar glint. **But 299 MW is FIRE (~70 MW) + EMERGENCY FLARING (100 MW+) BUNDLED**, and emergency flaring is a controlled shutdown response, not burning wreckage. No Aramco statement, no FM, no throughput figure ⇒ **real disruption at the highest-consequence node in world oil, NOT a supply event.**
- **CPC RESUMED 7/27** — ~440 kbpd off for a week, **nothing destroyed, nothing repaired**, restored by owners deciding to sail (the returning hulls were chartered by Tengizchevroil — *the same Chevron reported 7/23 as refusing to call*).
- **Ras Laffan LNG force majeure entered MONTH FOUR and extended 7/28 to ASIAN buyers** (~12.8 Mtpa ≈ 17% of Qatar's exports, FM since 3/24).

## WHAT I DID

- **★ BOTH OWED GRADES CLEARED — before Friday, when they would have stacked two prints per series.**
  - **COT as-of 7/21 = COILED — a REVERSAL of the 7/14 IGNITING read.** MM gross shorts 129,072 (7/7 base) → 119,187 (7/14) → **123,490 (7/21)**: cumulative **−5,582** (COILED band ≥−7,000) because **shorts REBUILT +4,303 WoW**. Longs rebuilt +6,308; **net −62 = FLAT.** ⇒ 7/14 de-grossing, 7/21 **re-grossing: positioning is CHURNING, not trending; the squeeze UN-ignited.** Graded off Socrata **AND** the raw `f_disagg.txt` primary (agreed this week; parse cross-checked on a control row).
  - **BRT-26 = THE BREACH DID NOT HAPPEN. Rigs 450 (−2 WoW).** First decline after 12 rises in 13 weeks; **7 to 457**, further than the 5 at wk-7/17. **My 7/21 "likely FAILS imminently" call was WRONG IN DIRECTION** — rigs lag price 4-8wk, so this reflects late-May/June $70s-80s decisions; I forecast off a pace I knew was lagged. Conf ~58%.
- **★ 36-PACKET INBOX DRAIN** (both lanes, backlog 7/22→7/28) — 26 acted / 9 noted / 1 near-miss. **Near-miss worth remembering: I nearly consumed PROME's fighting-shape review UNREAD**, caught only by reconciling moved files against ledger rows before committing.
- **★ THREE BOOT GUARDS FOUND POINTED THE WRONG WAY AND FIXED** [DAEDALUS audit; verified at source myself]. `thresholds.py` carried retired v4 rows: `<$75 = THESIS BREAK` (v5 retired sub-$75 as a break — it is decoupling, thesis-*confirming*) and `<$85 = squeeze weakening` (v5 grades $85×3 as *bullish* sustained premium), plus a **firing-every-boot** `Dated Brent <$100 = physical squeeze resolving` that infers physical tightness from flat price — **the exact inversion of this thesis's central finding.** **Not hypothetical: Brent opened at $84.95 today, below the $85 line.** Root cause: the script sourced `VX.tsv`, **FROZEN since 6/14**. Repointed to THESIS as canonical-wins.
- **★ A LIVE FALSEHOOD CORRECTED:** my 7/27 note **declared** the PENDING-fill contradiction fixed; I had fixed only the execution-log row. TRADE.md:3, TRADE.md:120 and **NEXUS_BRIEF.md:61** all still said *"pending fill"* against a position filled 7/24 — and **NEXUS reads that brief in place of my STATUS.** Corrected + **correction packet sent to NEXUS naming the exact window**, rather than letting it self-heal.
- **Derived-surface sweep** (the thing the 7/27 closeout skipped): convergence matrix **CPC row 3→2** on demonstrated reversibility + **Storage row** corrected (had contradicted my own dashboard 40 rows up for 5 days); **matrix TOTAL 63→62/75, first down-mark this cycle**; **NEXUS_BRIEF body fully re-stamped** (was 7/23-vintage under a 7/27 stamp); STATUS vestigial `"Last Updated: 2026-07-08"` stripped and **PAT-044 two-clock header adopted**; PREDICTIONS stamp corrected + the 7-vs-6 OPEN count reconciled (**TSV's 7 is right**; STATUS renders BRT-07/17 as one display row — a presentation artifact, noted not "fixed").
- **Protocol edits to my own CLAUDE.md** (the root causes, not the instances): **boot 6b** general-inbox triage *(defer freely; go silent never)* · **boot 6c** PENDING-row guard **mechanized** (was prose-only in the two surfaces that rotted) · **closeout 7a** `cot_grade.py` **wired** (it existed since 7/17 with zero references in the file) · **closeout 13a** one mail-archive sweep covering **both** inbox and `outbox/delivered/` · duplicate step-6 renumbered.
- **Outbox swept: all 11 top-level packets → `delivered/`** (loops demonstrably closed; `delivered/` had not been walked since 5/04).
- **Two auto-memory APPENDS** (not new slugs): `[[finding_record_of_an_action_is_not_the_action]]` n=4 — *"declared-fixed but partly-fixed is worse than open, because the declaration immunises the gap against discovery"*; `[[finding_test_the_guard_not_just_the_guarded]]` n=4 — *a guard that AGED into pointing the wrong way; fails silent in the worst available form, loud and confident and backwards.*

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **Wed Jul 29 10:30 ET — EIA WPSR wk-7/24, THE RESOLVER. Walk in EXPECTING the Cushing sign contradiction, not a clean print** (API relays split Geiger −273K vs First Squawk +273K; I carried neither). API showed crude **+3.296M vs −2.5M forecast** (~5.8M bearish surprise, 2nd straight build) + SPR −3.7M. **Boundary #3 unchanged either way** (both readings <20M).
2. 🔴 **Wed Jul 29 FOMC** — decides on a cool June CPI while the oil shock lands in July's print (~Aug 12). ⚠️ The shock is now **MUDDLED**: July carries the spike, August carries the crash.
3. 🔴 **Fri Jul 31 — CFTC COT as-of 7/28: the FIRST print capturing BOTH the $100.69 high and the −15.6% unwind** (7/21 predates both). Ladder from 123,490. **+ Baker Hughes: does the −2 extend or reverse?** Run the newly-wired closeout step 7a; do NOT let these stack again.
4. 🔴 **Does the resumption HOLD, and does the US answer?** Cooper's framing says a US return is likelier a **step change** than nightly tempo. Watch the antecedent, not the price.
5. 🟠 **TTF / European gas — SELF-OWED, and it is the deciding question on the LNG line I am now carrying to SAM and HAWK.** If Europe absorbed 17% of Qatari exports for four months **without** repricing, that is a finding in the *opposite* direction.
6. 🟠 **TERRY's 3 diesel structures were CONDITIONAL "not at Monday's price"** — tonight's re-widening moved the entries again. **Re-read at a live quote before anyone (including TERRY) cites them as actionable**; the XLE-65C rotate-don't-stack funding question rides with it.
7. 🟡 **Libya: watch for NOC TERMINAL-level force majeure** (Es Sider, Ras Lanuf, Zueitina, Brega, Hariga) — the step that converts 85 kb/d into 500-900 kb/d, and the step both prior episodes took.

## OPEN THREADS / WATCHES

- 🔴 **QUEUED FOR WILL, NOT YET DRAFTED — the LESSONS #21 re-spec** (see POSITION DECISIONS). **Do not treat the silence since 7/27 as a ruling** [PROME item 2].
- 🔴 **My Branch-2 ladder has NO RUNG FOR PARTIAL EXECUTION.** Yanbu loadings at **−30% (3.3 vs ~4.7 mb/d) sit BETWEEN "still loading" and "liftings stop."** Fix the ladder before it has to grade something. FALCON still owes the leg-3 adjudication itself.
- 🟠 **Adopted from HAWK, and I owe a one-line loop-closure reply:** *"was capacity destroyed?"* replaces barrel-count as the discriminator (my premium-vs-supply-loss test already **was** a reversibility test — this is a genuine sharpening of phrasing). **And the qualifier is now "zero confirmed CRUDE barrels offline"** — the war's one confirmed quantified loss is LNG.
- 🟠 **MRPL tender clause = RE-CONTRACTING, not re-routing** — first Indian refiner ever to bar Hormuz *and* the Red Sea in a spot tender; forward-dated, contractual, sticky. **The mechanism by which a premium becomes a structural route re-pricing — the transition I have been trying to date.** Falsifier: no second Indian adopter in 3-4 weeks ⇒ one cautious buyer.
- 🟠 **War-risk decomposes on TRANSIT, 75-100×** (0.1% no-chokepoint vs **7.5-10% Hormuz**) — the quantified backbone of the discriminator, and why the premium is reversible: transit risk unwinds on a **decision**, not a repair.
- 🟡 **Flows-vs-inventories reconciliation still open:** ~13-14 mb/d flows hit vs only −2.7 mb/d visible draw ⇒ **the gap is SHUT-INS, recoverable.** Cuts against my tightness read on the way up and for a sharper Phase 2 on the way down.

## POSITION DECISIONS PENDING

- **USO Sep-18 150/165 spread — HOLD, no action.** Filled 7/24 ~$300 (defined risk, already paid). Needs **+24.5%** to the 150 strike, **+27%** to BE ~$153, **52 DTE**. USO $120.49 is a 4 PM close that **predates the 5:45 PM launch — should gap up.** Do not add, do not cut into FOMC + the 10:30 print. **⚠️ FORGE reconcile STILL OWED — exact fill price from the broker book (Will).**
- **Convex MAIN arm = ARMED-and-HOT, no capital.** Gate unmet both legs, **6th session.** OVX 57.15 vs <44.2 (−29.3%, binding) · ratio 3.138 vs <2.89. ⚠️ **Tonight's vol reading is a 4:15 PM print and predates the 5:45 PM missiles — expect re-inflation.**
- **🔴 QUEUED FOR WILL — LESSONS #21 re-spec, pre-registered, NEW FROZEN numbers (never rolling percentiles).** **(a) The OVX <44.2 leg may be unfireable by construction** — oil vol does not return to the 40s while the strait is shut, and if it reopens the arm has nothing left to capture, so **the main arm's gate may never release capital while the thesis is alive.** Needs Will's written ruling on a drafted proposal. **(b) The off-ramp's "war-risk halves within 3 trading days" is a 2-4 WEEK indicator in a 3-day window** — mechanical, per-leg windows, approvable on sight. **Neither to be quietly relaxed to fit the tape.**
- **Off-ramp playbook ARMED-PASSIVE** — tanker sanity check fired correctly a **4th** straight session (STNG +0.88% / FRO +0.49% / DHT +1.64% on a day crude opened at its lows).
- **XLE $65C Sep-30 = LAPSE** (−56%) — TERRY proposes it as the diesel-leg funding source.

## MAIL STATE

- **Inbox: ZERO both lanes.** 36 packets consumed this session, every one with a `board_log.tsv` row (reconciled moved-files == ledger-rows).
- **Outbox: ZERO top-level** — all 11 swept to `delivered/`.
- **Sent this session:** NEXUS correction packet (filled-position window named).
- **Owed BY me:** HAWK one-line loop-closure · FALCON nothing (they owe me leg-3) · Will the #21 re-spec draft.

## WORKBOOK HEALTH

- **LIVE & current (7/28):** STATUS (two-clock header, 220 lines, under the 250 cap) · TRADE · NEXUS_BRIEF (body re-stamped) · PREDICTIONS.tsv · CLAUDE.md (4 protocol edits) · `scripts/thresholds.py` · SCRATCH (this) · board_log.tsv (94 rows).
- **FROZEN (bannered, correct):** KB.tsv, VX.tsv, FLOW.tsv, GROUP_MAP.tsv, TIMELINE.md. ⚠️ **`VX.tsv` being frozen is what silently rotted `thresholds.py` — a frozen source cannot signal that it stopped moving.**
- **STILL OWED from the DAEDALUS audit (none urgent, all logged in `board_log.tsv`):** the **structural** threshold fix (scripts READ the registry, never restate — I only corrected the instances tonight) · `domain/sources/` referenced but nonexistent · bare-relative MSG-v1 validate invocation · CLAUDE.md:124 hardcoded positions duplicating TRADE's canonical table · `workbook/SCHEMA.tsv` unbannered · `GROUP_MAP.tsv` banner self-declares a delete never executed · `scripts/BUILD_PLAN.md` 3mo stale · FASTOW dormant 51d with no dormancy note · PREDICTIONS_ARCHIVE ~6wks behind · archive candidates.
- **L5 condition (DAEDALUS):** fill-confirm leg PASSED; the zero-operator-caught-surface-errors leg did not. **New condition: one closeout cycle where derived surfaces agree with the banner layer + thresholds repointed (DONE) + W1-W3 landed (W1 DONE, W2 DONE, W3 DONE).** ⇒ **the remaining test is simply whether the NEXT closeout stays clean.**
- **GIT:** own-dir pathspec commits + NEXUS packet under carve-out ① + memory appends under carve-out ③ + safe-push.
