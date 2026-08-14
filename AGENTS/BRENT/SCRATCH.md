# BRENT SCRATCH — Fri Aug 14, 2026 **~16:0x ET** *(live session, PROME-directed spawn for the 15:30 COT window · FULL CLOSEOUT RUN)* · **THE SESSION WHERE A COIN FLIP LANDED ON THE UN-FIRE SIDE AT 5.3× THE FLIP DISTANCE — AND A SPEC GAP I NAMED BUT DID NOT FIX WAS COVERED BY EXACTLY THREE DAYS**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴🔴 **THE HEADLINE: `FUEL SPENT` UN-FIRED. THE FULLER-SIZE BRANCH IS OFF. THE INCUMBENT BAND IS DEAD AND `COT-FUEL-35B` IS LIVE.**
> **8/11 vintage: MM gross shorts `110,638` vs the frozen `≤104,072` bar ⇒ UN-FIRES by `6,566` contracts** (cum −18,434 vs a −25,000 bar; WoW re-gross **+8,078**; OI 1,892,429; share 5.8463%).
> **Successor first read: Leg A 110,638 INSIDE the deadband ⇒ NO-VERDICT · Leg B 5.8463% vs ≤4.909% ⇒ NOT-SPENT ⇒ JOINT `NO-VERDICT` ⇒ sizing defaults to BASE CASE.**
> ⇒ ★ **BOTH ROUTES LAND IN THE SAME PLACE: normal size within cap. No reading of this print supports fuller size.**
> ⛔ **Nothing published reads "positioning exhaustion CONFIRMED" — and forum-4 §5's JOINT confirm cell is **EMPTY-IN-REGIME, not structurally empty** — ⚑ corrected same-day 2026-08-14 on MIDAS's own retraction: its `P(c)=0.00 / NC short <20,000 never in 449 weeks` was computed on an INHERITED 449-week window; the full CFTC COMEX gold series (1986-01-15, n=1,929) shows **299 occurrences**, most recent **2009-01-13**. ⇒ the cell is empty **because of the current regime (17.5 years)**, which a sufficient regime change could populate — NOT unreachable. **Weaker, more honest, and the practical near-term conclusion is unchanged: the 8/11 print did NOT populate it (MIDAS NC short 32,996, shorts ADDED +3,617, moving AWAY).****

> # 🔴 **`$0` MOVED. NO POSITION CHANGED. NO THRESHOLD MOVED. NO GATE FIRED (there is none). NO CAPITAL AUTHORISED. NO PREDICTION RESOLVED (boot scan clean; no COT rows open — BRT-21 is VOID).**
> **INBOX 12 → 1. TWO GRADES WRITTEN (COT + rigs). REGISTRY 48 → 49 rows.**

---

## ★ THE SESSION IN FIVE LINES

**The card was built Thursday so Friday would be mechanical, and it was: the whole window was one pre-computed boundary, and the grade took one command.** The value was in the ORDER — grade → write → *then* register — and it held.
**The silent-unfire hazard was REAL, not theoretical. Had the grade not been written, the branch's state would simply have been UNKNOWN and TERRY could have sized off a stale `LIVE`. Here silence would have been WRONG, not merely unverified.**
**The 8/7 session named a spec gap — *"says NOTHING about what happens if it UN-FIRES; no rule exists for that"* — and did NOT fix it. Will's 35a REVERT ruling landed 8/11, three days before the print that needed it. The gap was covered by three days.**
**The 8/7 base rate said the 1,512-contract margin was a coin flip (48.4%/50.0%). The next print moved +8,078 — 5.3× the flip distance. The margin really was below the instrument's noise floor.**
**And grading the RIGS nearly manufactured a breach at my own line off a CSS class name — a `grep` for `45[0-9]` on an HTTP-200 page returned `457` twice, every hit a Drupal UUID fragment, on a page carrying no counts at all.**

---

## ✅ WHAT WAS DONE

### ① THE WINDOW (the reason this session existed) — executed in the ruled order, not collapsed
- **Polled the raw `f_disagg.txt` primary from ~14:31 on THREE overlapping tripwires** (two background pollers + a Monitor) after noticing the first poller's 30-min horizon would expire before the release. **All converged at `15:30:27`.** Never Socrata.
- **`report_date` verified IN-ROW (Trap 1). Re-pulled INDEPENDENTLY a second time before grading — both pulls identical.**
- **Wrote a one-shot grader (`scripts/grade_2026_08_14.py`) with every constant copied from the card, and FALSIFIED IT BEFORE USE** (standing rule): run against the stale 8/4 vintage it **exits 3 and refuses to grade**, and it reproduces the card's verification figures (OI 1,886,816 / short 102,560) exactly.
- **Incumbent graded → verdict WRITTEN on both surfaces → incumbent RETIRED (superseded text preserved verbatim) → ONLY THEN successor registered.** ⛔ The two bands never ran on the same vintage.

### ② CONSUMER CHECK — two real stale carriers, both packeted, neither file touched
`consumer_check.py` flagged **`AGENTS/TERRY/STATUS.md:18`** and **`PROME/DOCKET.tsv:55`** carrying `FUEL SPENT` on live surfaces. **These are the genuine class, not the bare-figure false positives.** **TERRY packeted 🔴 urgently** (it owns the sizing downstream); **PROME's window report answers DOCKET row 55 — the fuel DID re-stack, that row can close.**

### ③ RIGS — `BRT-26` GRADED, NOT BREACHED, and three near-misses recorded
**US OIL rigs `455` (+1) vs the frozen `457` ⇒ 🟢 NOT BREACHED, 2 away.** Total 593 (+5).
- ★★ **COMPOSITION IS THE FINDING: the total rose +5 but OIL rose only +1.** Anyone reading "US rig count +5" as a crude-supply response has it wrong.
- ⛔ **TRAP: a bare `grep -oE "45[0-9]"` on the BH page returns `457` TWICE — every hit a Drupal CSS/UUID fragment**, on a page with no counts in its HTML at all. **It would have recorded a breach EXACTLY at my line, off a stylesheet identifier.** → promoted to auto-memory.
- ⛔ **TRAP: the BH primary is REACHABLE again (HTTP 200, first non-403 in weeks) and still could not grade it** — its linked 11.8 MB workbook is stamped **2025-08-29, a YEAR stale**, with 169,320 real rows.
- ⛔ **TRAP: five outlets "confirming" the 8/7 figure are ONE Reuters wire** ⇒ n=1. The 8/14 oil leg is also n=1 (TradingEconomics) **but ANCHORED** — its companion total ties to the BH primary table to the unit. **I named that difference rather than claiming two witnesses for both.**
- **`BRT-26-RIGS` registry row had EMPTY direction+level** — the 457 line lived only in THESIS prose, so the row graded nothing. **MIGRATED, not re-levelled** (CUSHING-20M precedent).

### ④ PRE-WINDOW SLATE
- **INBOX 12 dispositioned / 11 archived; board_log 190 → 202.** ⚠️ **Deliberate 12-rows/11-moves:** SAM's packet arrived mid-session **untracked — in-flight, not orphaned**; `git mv` correctly refused and bash `mv` would have raced SAM's uncommitted work (8/12 RED precedent). **It archives once SAM commits.**
- **8/12 + 8/13 crude PUBLISHED**, re-split by the **14:30 ET settlement clock** (executes WALTER `SIG-020`'s ask). `BZV26.NYM` 8/12 $88.98 · 8/13 $87.07 · `CL=F` $83.27 / $81.25 · M1−M3 **+4.30 / +3.74**, backwardated across the strip both days. **Labelled COMPLETED-SESSION CLOSES, NOT asserted as the 14:30 settlements.**
- **USO 150/165 net debit `$300.00` BROKER-CONFIRMED** — card marked. **Confirms the 7/25 verbal estimate rather than correcting it ⇒ nothing moves; only the evidence grade.**
- **Concentration arithmetic DONE + TERRY packeted** (see below).
- **SUMED answered** for `SIG-013`: Sidi Kerir ~2.3 mb/d vs a nameplate cited at ~2.5 / ~2.8 / ~3.0 ⇒ **77–92% utilised. I quoted the RANGE** — picking 2.5 would have manufactured a near-ceiling story out of a source disagreement.

### ⑤ HYGIENE
- **NEXUS_BRIEF: fixed a LIVE cross-agent defect** — it was still publishing my **wrong** capture-time boundary (session-end 18:00/17:00 ET) to the whole fleet. **Both crude settlements are struck 14:28–14:30 ET.** "Equities are exempt" carve-out retired with it. **185 → ~175 lines**; two fully-superseded blocks moved to `workbook/NEXUS_BRIEF_archive_2026-08-14.md`, **preserved verbatim, not deleted** (cross-agent correction records other desks consumed).
- **Auto-memory promoted + committed + index-checked:** `finding_digit_regex_on_markup_can_match_the_threshold_value`.

---

## 🔴 CONCENTRATION — MY HALF DONE, SIZING IS TERRY'S

Oil sleeve **$5,886.05** mkt / $6,442.48 basis (−8.64%), one 8/14 broker capture. **USO-linked = 96.70%.** **29.6% of deployed positions · 16.0% of total book.**
- **Effective LINES (Herfindahl) = `1.66`. Effective independent VIEWS = `N_eff 1`** — all four legs die on the same event.
- ⚠️ **Flagged against my own alarm: `N_eff = 1` was ALREADY the 8/4 read. Same finding, bigger number — not a discovery, and I did not dress it as one.**
- **NEW:** **74.70% of the sleeve is the undefended linear 35 shares (no floor)**; the **`USO 135C Oct-16 ×2` entered on NO rail** and is now the **2nd-largest oil leg (20.56%)**; two legs expire inside ~5 weeks, so the **FORWARD sleeve is 95.3% two USO lines**.

---

## ⏳ NEXT SESSION

1. **🔴 Fri 8/21 COT (as-of Tue 8/18) — FIRST GRADE OF THE SUCCESSOR ON A CLEAN VINTAGE.** Leg A vs **113,745** / deadband **109,165–118,325**; Leg B OI-share vs **4.909%** (GATING). Ladder from **110,638** / OI 1,892,429 / share 5.8463%. ⛔ **`median_unit 9,160` is FROZEN — do NOT re-measure per print; re-basing is a NEW N1 BUILD + a fresh Will ruling.** ⛔ **The incumbent is RETIRED — do not re-grade it.**
2. **🟠 Fri 8/21 Baker Hughes — `BRT-26` is now only 2 from the line** and closed 1 rig of distance this week. ⛔ **Grade the OIL count, NOT the total.** ⛔ **Never off a bare digit-regex on the BH HTML.**
3. **🟡 TWO PACKETS LOGGED BUT NOT ARCHIVED — both UNTRACKED at closeout (senders still committing).** `git mv` each to `inbox/processed/` once its commit lands. ⚠️ **This is why board_log reads 203 rows against 11 moves today — a DELIBERATE, recorded exception, not a reconcile failure** (`finding_dirty_path_means_in_flight_not_orphaned`; 8/12 RED precedent).
   - **SAM** (`…_ACCEPTED-the-agsi-feed-parked…`) — **nothing owed.** SAM accepted the AGSI+ feed and **PARKED** it with a stated reason (its frame is retired to LOW, so wiring an instrument into a desk with no live thesis would produce a feed nobody reads). **Correct call, endorsed** — my own retirement-ratchet logic from the other side.
   - **🔴 MIDAS** (`…_your-CORRELATED-CONFIRM-cell-rests-on-a-number-of-mine-that-was-wrong`) — **ALREADY ACTED ON, same session.** It retracts its `P(c)=0.00 / "structurally unreachable"` (computed on a 449-week window **inherited from SAM's JPY pull**; the full COMEX gold series, 1986-01-15, n=1,929, has **299 occurrences**, most recent 2009-01-13). ⇒ **I corrected "confirm cell is EMPTY" → "EMPTY-IN-REGIME" on all five surfaces I had written it on TODAY.** **Practical conclusion unchanged — the 8/11 print did NOT populate it** (NC short 32,996, shorts **added** +3,617, moving away).
     - ⛔ **The alarming half, and MIDAS leads with it: its OTHER "never observed" rate (ΔOI ≥ +28,449 from a sub-400k base, published 0-of-19) WAS REALISED SIX DAYS LATER at +28,758.** ✅ **What saved the claim: MIDAS refused to quote 0-of-19 as a probability and published a rule-of-three 95% upper bound of 15.8% instead — the corrected rate (1.81%) AND the realised outcome both sit inside it. THE POINT ESTIMATE FAILED AND THE INTERVAL HELD.**
     - ★★ **AND IT CONVERGES INDEPENDENTLY WITH MY OWN 35b FINDING, from a different desk and a different market: "a window inherited from another desk's instrument is a FREE PARAMETER YOU DID NOT SET."** MIDAS found it in COMEX gold via an inherited JPY window; I found it in WTI COT via an undeclared median window worth 1,508 contracts. **Neither prompted the other. Two independent routes to one defect class is far stronger than either instance.** **ADOPTING MIDAS's one-line fix: state series FIRST DATE, LAST DATE and ROW COUNT before any base-rating.**
4. **🟡 OWED FROM TODAY'S INBOX, named rather than silently dropped:**
   - **Yanbu ↔ Sidi Kerir DOUBLE-COUNT SEAM** (`SIG-013` ask ②) — if a cargo loads at Yanbu, part-discharges at Ain Sokhna and reloads at Sidi Kerir it can appear in BOTH series, which would make Goldman's Yanbu −23.3% **a measurement seam rather than a decline.** ⛔ **Until resolved I do not net the two, and neither should anyone citing them.**
   - **IIR-vs-NBS refinery-runs comparison** (`SIG-011` ask ①) — **constructible for the first time**; the two claims sit on **different axes** (official-vs-true vs 2026-vs-2025) and **must not be merged.**
   - **Global visible-stocks counter** (`SIG-011` ask ②) — a **real named gap** in my kit (I hold US-only). ⛔ Not registered off a screenshot with no publication date.
   - **War-risk cover instrumenting** (`SIG-015`) — **strongest instrument candidate in weeks** (a HARD GATE that moves BEFORE the decisions it produces; JWC Listed Areas are public and dated). ⛔ **NOT built — this is the third feed-less gap I have declared, and per the retirement ratchet a registration needs a read-path and base rates FIRST.** Gate on WALTER's own testable framing: *would JWC revisions have warned leg-3/R3 earlier than loadings did?*
5. **🟡 TERRY's USOARM finding — MINE TO RULE, still open by choice.** A moment-graded gate (leg (b), ~40min half-life) cannot depend on a multi-day approval loop whose only pressure point is day 20. **Two candidate fixes offered (a DECISION-BY date, or a two-stage [Approve in principle]); NEITHER adopted** — no arm is live, `$0` at risk, and per TERRY's own 005/007 discipline any re-arm is a NEW card, so **the fix belongs ON that build, not floating as an amendment to a dead spec.**
6. **🟡 Unchanged carry-overs:** P5 row-27 width-bias re-spec (must land BEFORE any re-arm) · Shell Q2 deck PRIMARY before Pearl-GTL touches GATE-1/FAL-01 wording · EIA imports-by-country primary · SPR "floor" ambiguity **252.4M vs 400.0** (147.6M under one word — read the rationale, don't find-and-replace) · **INCIDENTS: 17 ACTIVE rows past the 60d budget, worst RF-004 at 148d — the flag exists, the re-verification is research and has NOT been done** · Novorossiysk/Sheskharis INCIDENTS row (check HAWK's cross-theater `STRIKES.tsv` FIRST).

---

## OPEN THREADS / WATCHES

- **⛔⛔ THE SESSION'S TRANSFERABLE FINDING: a bare digit-regex against HTML can return your EXACT threshold value out of markup containing no data at all — and because the false value EQUALS the number you were watching for, it reads as the SIGNAL rather than as noise.** Hex UUIDs make it likely, not freakish. **Rule adopted: anchor to a PARSED, LABELLED field or do not grade.** → auto-memory `finding_digit_regex_on_markup_can_match_the_threshold_value`.
- **★ AND MY OWN 8/12 DEFECT ACCIDENTALLY GENERATED THE FIRST EVIDENCE ON WALTER'S OPEN §7 QUESTION.** The completed 8/12 bar closes **$88.98 — HIGHER than every late-session live print I took** (16:38 $88.61 → 17:07 $88.38; PROME $88.37/$88.40) ⇒ **the vendor's daily `Close` is NOT a session-end last price.** It also reproduces the corrected 8/10 ($87.72) and 8/11 ($88.91) settles to the cent. ⛔ **Routed to WALTER as a CANDIDATE, not a finding — n=3 days is not a backfill proof — and I re-labelled NOTHING "settle" on it.**
- **⚠️ THE LIMIT THAT SURVIVES THE N5 FIX: A LATE PULL IS STILL A BAR.** Knowing the settlement was struck at 14:30 does not mean a 14:31 vendor pull returns it. **Waiting never converts a bar into a settlement; only a SETTLEMENT SOURCE does — and identifying one `fetch.py` can reach is still UNBUILT.**
- **⛔ 85.7% OF GROSS SHORTS ARE STILL STANDING** (79.5% on 8/4). **The accelerant did not fire — it re-loaded.** Positioning descriptor only: **no price validation, n=0 genuine reopenings.**
- **⛔ 35b's FREE PARAMETER IS THE LIVE RISK.** `median_unit 9,160` FROZEN. A future session re-measuring on a different window moves the bar ~**1,508** contracts **with no ruling and no record** — ≈ the incumbent's entire fatal margin. `[[finding_threshold_level_is_a_measurement_not_a_constant]]`
- **⚠️ R1 (OVX close >68.97) remains a NAMED CANDIDATE, NOT a registered tripwire.** Re-arming requires a FRESH Will ruling.
- **⛔ Still no freight/Worldscale feed anywhere in the kit** · **EXPORT-SIGN WARNING live** · **RUNS-DECLINE IS NOT CAPACITY-OFFLINE** · **Black Sea war risk UNPRINTED 20+ days — report it to nobody as flat.**

## POSITION DECISIONS PENDING

- **NONE. `$0` at risk from any gate — there is no live gate.** Convex arm **RETIRED 8/7 by Will**; **`TRY-BRENT-USOARM` DIED 8/13 at arm expiry, day 20/20, UNFIRED, `$0` ever at risk.** Will's 8/4 fill decline is STANDING and untouched.
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares, 74.70% of the oil sleeve, no floor.** Not a trim recommendation (root rule #7 — thesis intact) and equally not an add.
- **5 live oil expressions** (35sh · Oct-16 135C ×2 · Sep-18 150/165 · XLE Sep-30 65C ×2). **Marks are the 8/14 broker capture.** ⛔ **STNG is a TRACKED TICKER, not a holding.**

## MAIL STATE

- **✅ INBOX 12 dispositioned → 11 archived, 1 held** (SAM's, untracked/in-flight). **board_log 190 → 202.**
- **SENT (3):** → **TERRY** ×2 (concentration arithmetic; 🔴 the UN-FIRE state correction) · → **PROME** (window report / delivery packet).
- **Owed TO me:** **Will — the war-risk-halves ruling · the WP3 call.** ✅ **The FORGE fill-price reconcile is CLOSED after 20 days — `$300.00` broker-confirmed.**

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` (**822 ln**) · `STATUS.md` (**236 ln** — 14 from the 250 cap; **archive overflow next session before writing anything large**) · `workbook/REGISTRY.tsv` (**49 rows, 21 cols uniform** — `COT-FUEL` retired, `COT-FUEL-35B` live) · **THESIS v5.6, unchanged today** · `docket/CATALYSTS.tsv` (**19 rows, 8 cols uniform**) · `refinery_damage/INCIDENTS.tsv` · `board_log.tsv` (**202 rows**) · `NEXUS_BRIEF.md` · SCRATCH.
- **Boot 92.0s, 6/6 OK, ZERO blocking**, 2 warnings (`COT-FUEL`, `BRT-26-RIGS`) — **both cleared by today's grades.**
- **Data pulled, all own primaries:** CFTC raw `f_disagg.txt` (067651, ×3 independent pulls) · Yahoo `BZ=F`/`CL=F`/`BZV26`/`BZX26`/`BZZ26`/`BZF27` daily bars · Baker Hughes primary overview + static workbook · TradingEconomics rig split · EIA weekly via boot.
- ⚠️ **`instrument_check.py --quick` IS NOT A SUBSTITUTE FOR THE FULL CHECK** — it skips network probes and reports ~19 BLOCKING where the full run reports ZERO. **Deliberate fail-safe direction (false RED, never false green).**
