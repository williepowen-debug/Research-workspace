# BRENT SCRATCH — Thu Aug 13, 2026 **~10:xx ET** *(live session, PROME-directed)* · **THE SESSION WHERE AN 11-DAY BLOCKER TURNED OUT TO BE A SERVER ERROR STRING LYING ABOUT ITS OWN GATE**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴 **`$0` MOVED. NO GATE FIRED (there is no live gate). NO THRESHOLD MOVED. NO POSITION CHANGED. NO PREDICTION RESOLVED.**
> **ALL FIVE PROME RIDERS LANDED, ahead of the Fri 8/14 deadline. BLOCKING INSTRUMENT ROWS `1 → 0`. INBOX `8 → 0` (8 moved == 8 ledger rows).**

---

## ★ THE SESSION IN FIVE LINES

**`EU-STORAGE` was 🔴 `NO_INSTRUMENT` for 11 days "pending Will's GIE API key." There was never a key. GIE denies by USER-AGENT and its error text says "Invalid or missing API key" either way** — I reproduced both legs myself before wiring anything. **The footnote that refutes the blocker was sitting in DEWEY's DR-4 the whole time.**
**The STEO write-back — the one item I declared NOT DONE on 8/12 — graded, and the answer is material: the no-absorber window LENGTHENED a full quarter (Q1-27 surplus `1.57 → 0.030`), and the recovery that closes it is now `100.0%` MIDDLE EAST.**
**Building tomorrow's COT card found a FREE PARAMETER in the successor Will already approved: the median-unit WINDOW was never declared FROZEN or TRACKED, and the bar moves 1,508 contracts across three defensible windows — almost exactly the incumbent's entire 1,512 margin.**
**DR-4 corrected my own direction call: "TTF at €59 FALLING" had the level right TO THE CENT and the adjective wrong (July +38.1%, YoY +83.3%). A correct number carrying a wrong direction — and the exact level is what stops anyone checking.**
**And the Cushing <20M trigger — a live auto-dispatch condition — had NO registry row in ANY agent. It does now, on mine, because mine is the only desk with a live read-path to the series.**

---

## ⏳ FIRST THING NEXT SESSION — **IT IS FRIDAY 8/14 AND IT IS SEQUENCED**

> ### 🔴 **THE CARD IS ALREADY BUILT. USE IT, DO NOT RE-DERIVE.**
> **→ [`setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md`](setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md)**
>
> **1️⃣ INCUMBENT FINAL GRADE — pre-computed to ONE boundary: 8/11 MM gross shorts ≤ `104,072` ⇒ SPENT HOLDS · ≥ `104,073` ⇒ SPENT UN-FIRES** (a WoW re-gross of just **+1,513**; P = 47.4% all-history / 50.0% last 52wk).
> **2️⃣ WRITE THE VERDICT DOWN EITHER WAY — INCLUDING "SPENT HOLDS."** ⛔ Under 35a REVERT the modifier is a STATE re-read every print, not a latch: **it switches off SILENTLY and TERRY may size off a stale `LIVE`. A re-affirmation is a grade; silence is not.**
> **3️⃣ ONLY THEN register the 35b successor** — base `122,904` · median unit `9,160` **FROZEN** · Leg-A bar `113,745` · deadband `109,165–118,325` · Leg-B OI-share ≤ `4.909%`. ⛔ **NEVER run incumbent and successor on the same vintage.**
> **Pull: raw `f_disagg.txt`, code `067651`, MM short = field 15, OI = field 8, `report_date` verified IN-ROW.** `cot_grade.py --expect 2026-08-11`; **exit 3 = WAIT.**

2. **🟠 Baker Hughes (~Fri 8/14-15).** Grades **BRT-26** vs the frozen **457**; inherited **454 = 3 to the line.** ⚠️ **TWO INDEPENDENT PULLS. The primary has been 403/timeout-blocked from this box for weeks — if BRT-26 breaches on agreeing AGGREGATORS alone, SAY SO ON THE GRADE.**
3. **🟠 ~8/17 — CPC / non-Russian-tanker falsifier.** Still SURVIVES: Novorossiysk/Sheskharis struck 8/11-12 but **CPC was NOT reported hit** — that distinction is the whole ballgame.
4. **🟡 INCIDENTS row for Novorossiysk/Sheskharis 8/11-12** — now named KNOWN-INCOMPLETE in the ledger's own `# COVERAGE:` header rather than left silent. **Check HAWK's cross-theater `STRIKES.tsv` FIRST — do not fork a parallel record.**
5. **🟡 ROW 27's SECOND DEFECT — MINE TO ADJUDICATE, still open.** Leg (b) is **WIDTH-BIASED**: bid/ask friction is roughly a fixed **~$0.38** and does not scale with spread width, so a **WIDE spread passes a test a NARROW one fails on identical liquidity.** ⛔ **A DIFFERENT failure from the one my adopted amendment fixes, and the amendment does not reach it. It wants its OWN dated re-spec, not a patch folded into this one.** *(The row-27 encode itself is also still owed — a `TRADE.md` edit on a RETIRED arm, `$0` at risk, deliberately ranked below the four dated riders.)*
6. **🟡 Shell Q2 deck PRIMARY** before the Pearl-GTL force-majeure datum touches GATE-1/FAL-01 wording. **WALTER states plainly it never reached the deck — every figure is read off a screenshot.** A named-operator force-majeure disclosure is exactly the class I must not bank off an unverified image.
7. **🟡 Still open, unchanged:** EIA imports-by-country primary (Saudi→US ~600 kb/d Apr → ~0 late-Jul — I have the EIA v2 API wired; pull it, don't propagate a Bloomberg chart rendering) · ORACLE's forward cumulative-transit ladder in-or-out of my instrument set · **NEXUS_BRIEF still over its 100-line cap** · 5 structurally unresolvable predictions (BRT-07/12/16/17/21) · the SPR "floor" ambiguity **252.4M vs 400.0** (147.6M under one word — read the rationale, do not find-and-replace).

---

## CHANGES SINCE LAST SESSION

- **✅✅ `EU-STORAGE` 🔴 CLEARED — blocking rows `1 → 0`, the first clean instrument check of the cycle.** The gate was the **User-Agent**, never a key. **Bare UA → `{"error":"access denied","message":"Invalid or missing API key"}`; full browser UA → full dataset, keyless.** Wired as probe grammar **`gie:`** (EXTENDS, supersedes none) with two fail-loud guards: **`total==0` is a FAILURE not data** (AGSI answers HTTP 200 with an empty payload on malformed queries AND on UA denial) and **freshness reads the newest `gasDayStart` IN THE PAYLOAD.** ★ **GUARD FALSIFIED, NOT MERELY RUN.** First live read: **59.32% fill, 670.4321 / 1130.2074 TWh, gas day 8/11.** ⛔ **NO level registered — deliberately.**
- **🕐 STEO GRADED: the no-absorber window LENGTHENED ONE QUARTER.** `COPS_OPEC` August vintage: 2026Q2 0.053 · Q3 0.020 · Q4 0.020 · **2027Q1 `0.030`** · Q2 2.380. **Q1-27 moved `1.57 → 0.030` (−1.54 mb/d, −98%)** ⇒ window closes **Q2-2027, not Q1-2027**. ★ **And the assumption HARDENED: the recovery step is +2.350 total, ME +2.350 = `100.0%` (was ~99.6%).** ⚠️ **A forecast is not a barrel — tenor tolerance rises, nothing resolved.**
- **⛔ EU storage is the LOWEST FOR THE DATE IN FIVE YEARS, below even 2022** (59.3 vs 73.6/88.6/87.7/72.3). **90% needs 1.49× the four-year BEST pace = out of reach; 80% needs 1.00× = a dead heat. Landing zone 77–80%, 80% is the CEILING.** ⚑ **The binding rule was wrong on my surface: 90% target over a FLEXIBLE `1 Oct – 1 Dec` window, NOT 1 Nov** ⇒ my `2026-11-01` catalyst row's date was an artifact; re-framed as a WINDOW, all three blockers cleared.
- **⛔ DR-4 CORRECTED MY DIRECTION CALL.** "TTF at €59 FALLING": level **€59.07, right to the cent**; direction **wrong** — July **+38.1%**, YoY **+83.3%**, five sessions off a 52wk high. `[[finding_exact_level_authenticates_a_wrong_direction]]` **inward.**
- **✅ AUDIT CONVENTION — FIRST APPLICATION ENCODED.** F-2 (basis + declared authority on both pairs, the **13-of-254 COUNT** recorded, never the bare rate) · F-3 (roll rule + measured roll ledger on all six `BZ=F` rows) · **INCIDENTS schema v2** (7 cols added, **ZERO removed, ZERO values changed**) · **I-2 budget extended into `instrument_check.py`** — no tenth script — **and it fires: 19 ACTIVE rows past 60d** · I-3 `# COVERAGE:` · I-7 repoint · F-4 relabel.
- **✅ `CUSHING-20M` REGISTERED** with direction/level and the full Boundary #3 state machine. **Was prose-only in `WALTER/ROUTING_TABLE.md:446`, in NO agent's registry.** **NO LEVEL MOVED — migrated, not re-levelled.**
- **📬 INBOX 8 → 0** (8 moved == 8 ledger rows). The 8/12 deliberate **13-rows/12-moves** exception is now **CLOSED** — RED's commit landed, so its packet archived cleanly.

## WHAT I DID

**① CLEARED THE LAST BLOCKING INSTRUMENT — and reproduced BOTH legs myself before touching the probe**, rather than wiring on PROME's report. The blocker was an error string misnaming its own discriminator.
**② FALSIFIED THE NEW GUARD RATHER THAN RUNNING IT CLEAN** (standing rule): a malformed query returns HTTP 200 and the `total==0` guard correctly fails it. **A guard whose clean output has never been falsified is not evidence of anything.**
**③ GRADED THE STEO AT THE PRIMARY** and the pre-registered read paid: the trough didn't move, the **RECOVERY** did — which is exactly why the pre-reg said to read the recovery columns.
**④ FOUND A FREE PARAMETER IN A SPEC WILL HAD ALREADY APPROVED.** The successor's median-unit window was undeclared; the bar moves **1,508** contracts across three defensible windows. **Registered FROZEN at the approved basis; re-basing named a NEW N1 BUILD.**
**⑤ ACCEPTED OWNERSHIP OF THE CUSHING TRIGGER WITH A REASON, NOT BY DEFAULT** — mine is the only desk with a live read-path to the series.
**⑥ RECORDED A CHECK THAT PASSED AS A PASS.** `cot_grade.py`'s market name is CORRECT across the 2022 `CRUDE OIL, LIGHT SWEET` → `WTI-PHYSICAL` rename — my earlier query was wrong, not the script. **Reporting it as a near-miss would have been a fabricated finding.**

## OPEN THREADS / WATCHES

- **⛔⛔ THE SESSION'S REAL FINDING, AND IT IS ABOUT ERROR MESSAGES AS EVIDENCE: an 11-day blocker on a registered instrument was created ENTIRELY by a server's error text misnaming its own gate.** *"Invalid or missing API key"* is a **claim by the counterparty about why it refused**, and I treated it as a diagnosis. ★ **The generalisable rule: an error message is a WITNESS STATEMENT, not a diagnosis — and a failing request has at least two independent variables (credential AND identity/headers) that its error text is under no obligation to distinguish.** The cheap discriminator was one `curl` with a different header, and nobody ran it for 11 days. `[[finding_audit_resolution_path_before_reattempt]]` — **blocked by the PATH, not by missing data.**
- **⚠️ AND THE UNCOMFORTABLE HALF: DEWEY'S DR-4 SAID SO IN A PARENTHETICAL** — *"(no API key required; browser UA advisable)"* — **and it sat unread in my inbox while the row stayed red.** The information was delivered; the reading was the failure. `[[finding_delivery_check_is_not_a_knowledge_check]]`
- **⚠️ THE NEW GREEN IS A STATEMENT ABOUT SPECS, NOT SOURCES.** Four FRED rows threw HTTP 500 / timeout on the first pass and probed clean on retry — **transient, self-healing, and therefore the WORST shape**, because a retry-free consumer sees a silent gap rather than an error. **n=3 of this class across `BZZ26` too. "Zero blocking" must never be read as "every source answered."**
- **⛔ 35b: THE FREE PARAMETER IS THE LIVE RISK.** median unit **9,160 (n=235, 2022-02-08→2026-08-04) = FROZEN**. If a future session re-measures on a different window the bar moves ~1,508 contracts **with no ruling and no record** — the exact disease the successor exists to cure. `[[finding_threshold_level_is_a_measurement_not_a_constant]]`
- **⛔ INCIDENTS: 19 ACTIVE rows past the 60d budget, worst RF-004 at 147d.** The boot flag now exists; **the re-verification is research and has NOT been done.** ⛔ **NO AGGREGATE OVER THAT FILE IS QUOTABLE — event record, not capacity measure. The unit columns make units VISIBLE; they do not make the file summable.**
- **⚠️ SEAM WITH DAEDALUS, DECLARED NOT HIDDEN:** `STATE_VOCABULARY.md` has no zero-vs-unknown-vs-NA class, so my tokens are **BRENT-LOCAL**. **The distinctions are the ruling; the spellings are not — this file renames to match if DAEDALUS's differ.**
- **⛔ EXPORT-SIGN WARNING still live** · **RUNS-DECLINE IS NOT CAPACITY-OFFLINE** (band stays 25-35%; the ~33% re-centre is a candidate with Will, NOT applied) · **still no freight/Worldscale feed anywhere in the kit** · **Black Sea war risk UNPRINTED 20+ days — report it to nobody as flat.**
- **⚠️ R1 (OVX close >68.97) remains a NAMED CANDIDATE, NOT a registered tripwire. Recorded, never graded.** Re-arming requires a FRESH Will ruling.
- **★ THE PROMPT PREMIUM stays the strongest free evidence I have** — it peaked at the price LOW (8/5, front futures $79.45, premium +$7.20). **Watch whether it stays positive through further deal headlines.** ⚠️ **Two regimes in n=50 ⇒ quote the REGIME, never the mean; and it has never observed a genuine reopening either, so it does NOT close the n=0 gap.**

## POSITION DECISIONS PENDING

- **NONE. `$0` at risk from any gate — there is no live gate.** Convex arm **RETIRED 8/7 by Will, UN-DEPLOYED, `$0` ever at risk.** ⛔ **Will's 8/4 fill decline is STANDING and untouched — two separate decisions.**
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares = the book's large linear oil leg, no defined risk.** Not a trim recommendation (root rule #7 — thesis intact) and equally not an add.
- **5 live oil expressions.** USO 35sh · USO Oct-16 135C ×2 · USO Sep-18 150/165 · XLE Sep-30 65C ×2. ⚠️ **Option MARKS are `[STALE 8/4 broker export]`.** ⛔ **STNG is a TRACKED TICKER, not a holding.**

## MAIL STATE

- **✅ INBOX 8 → 0 — 6 acted / 2 noted. RECONCILED: 8 files moved == 8 ledger rows** (board_log 182 → 190).
- **SENT (3):** → **DAEDALUS** (convention encode-confirm + the token seam) · → **PROME** (delivery packet, all five riders) · **outbox** delivery memo.
- **Owed TO me:** **Will — the war-risk-halves ruling · the WP3 call · the FORGE fill-price reconcile on the Sep-18 150/165 (open since 7/24, now 20 days).** ⚠️ **The GIE key is NO LONGER on this list as a blocker — row 37 is hardening-only now.**

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` · `STATUS.md` (**246 ln, inside the 250 cap — WATCH IT, it grew this session**) · `RULINGS.md` · `workbook/REGISTRY.tsv` (**40 rows, 21 cols uniform**) · **THESIS v5.5** · `docket/CATALYSTS.tsv` · `refinery_damage/INCIDENTS.tsv` (**schema v2, 53 rows × 22 cols, +1 owed for Novorossiysk**) · TRACKER · board_log (**190 rows, +8**) · SCRATCH.
- **Boot 20.0s, 6 checks.** Lesson-conflict **0** · prose/index drift **0** · predictions-due clean · **Instrument Check: 1 blocking at boot → 0 after the EU-STORAGE wire**, 2 warnings (`BRT-26-RIGS`, `COT-FUEL`, both clear Friday), **+ the new I-2 advisory (19 rows)**.
- **Data pulled this session, all own primaries:** GIE AGSI+ `agsi.gie.eu/api/data/eu` + ALSI+ · EIA STEO v2 `COPS_OPEC` / `COPS_OPEC_R05` / `COPR_OPEC` / `T3_STCHANGE_WORLD` · CFTC raw `f_disagg.txt` (code 067651) + Socrata `72hh-3qpy` (400 rows, 2018-12-11→2026-08-04) · EIA weekly via boot.
