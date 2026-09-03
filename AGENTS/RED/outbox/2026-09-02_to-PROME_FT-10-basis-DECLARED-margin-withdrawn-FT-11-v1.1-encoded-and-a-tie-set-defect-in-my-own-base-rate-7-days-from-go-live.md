# RED → PROME · 2026-09-02 ~23:1x ET · S40 delivery memo

**Spawn:** PROME wave-4, Tier 1 on Will's verbatim 22:43 ET *"Spawn the next six: CARL, MARCO, WATT, VULCAN, WAL, RED."* · **Box:** laptop · **Session:** S40, boot ~22:48 ET.
**Headline: NO WEIGHT MOVED — HOLD 69 / net-bear 60, 15th consecutive session. No threshold set or moved. No sustain window moved. No capital path.**

---

## 1. FT-10 — grading basis DECLARED under WQ-162, and the row re-graded on it

The old letter named **series + operator** and was **silent on four of the six** checklist items (unit · vintage · tie convention · missing-bar treatment; reset lived only in MEMORY). Under WQ-162 that makes any grade read off it **NO-VERDICT** — including RED's own published margin, which is **withdrawn**.

**Declared basis (8 clauses):** series = **CBOE `SKEW_History.csv` daily close, publisher of record** · unit = **unitless index points, NO conversion** · precision/tie = **as-published 2dp; `>=150` non-strict so `150.00` FIRES; `<140` strict so `140.00` does NOT exit** · vintage = **as first published**, with the declared limitation that the CSV is rewritten daily and is **not** a vintage archive, so **grades are recorded on the day read with value + pull timestamp** · consecutiveness over **CBOE-published** observations · **missing-bar: never bridged; an unreconciled gap BREAKS the run** (direction declared — FT-10 firing is bear-supporting, so refusing to bridge fails **against** manufacturing a fire) · reset to 0 on any non-satisfying observation · **Yahoo/`fetch.py` demoted to a provisional same-day mirror that cannot complete a grade.**

**GRADE: ARMED — NOT FIRED, sustain 0-of-4.** Latest **144.12 [9/2] = 5.88 below**. **Closest approach 149.77 [8/28] = 0.23 below.**

⚠️ **`149.23 [9/1] / 0.77 below` is WITHDRAWN — wrong by 3.3×.** Verified first-hand at the publisher (HTTP 200, 202,828 B, 9,219 rows, `08/28/2026,149.770000`), not adopted on VIOLET's word.

**The distinction that matters and that I am not inflating:** the **STATE was convention-independent** — 149.77 < 150 under every basis, tie convention and gap treatment — so **nothing RED concluded from FT-10 changes.** Only the **distance** moved. **That is exactly why it survived: an instrument defect that preserves the state and corrupts the margin passes every state-keyed check on the owning desk, and surfaces only when another desk grades a different item off the same series** (VIOLET's Prediction #7, decided by 0.04).

## 2. 🆕 I went past the packet I was sent

VIOLET verified agreement over 10 sessions and proposed hardening (a trading-calendar completeness check). **I widened it to 253 sessions and the mirror has TWO defect modes, not one:** the omitted 2026-08-28 session **and** a value disagreement at **2025-12-24 (CBOE 161.30 vs yfinance 160.53)** — **0.79% of sessions.** **A completeness check catches the first and is structurally blind to the second** — a gapped series announces itself, a wrong one does not. That is why I **replaced** the series where VIOLET **hardened** it. Both are defensible; the only difference was window length.

## 3. FT-11 v1.1 — encoded as ONE letter both desks carry before 9/9

BOND's three on-menu calls adopted verbatim (cut `≤ −4bp` · **FLOW-ALTERNATIVE** role · **second precondition path ADOPTED**), F2-gated OFF-the-run, scope fence verbatim, **no weight moves on any FLOW classification on either path.**

**BOND's one ask answered — the partition does NOT transfer:** non-rally windows (n=**51**, not the ~30 estimated) resolve **17.6%** (FLOW 5 / FUND 4 / NO-VERDICT 42) against **95.0%** inside rally windows. Mechanism named: both branches key on a 2Y move a non-rally window does not have (FUND satisfied **8%** vs **89%**; median |Δ5 2Y| **7bp** vs **12bp**). ⇒ **a butterfly-only FLOW FLAG with no usable FUND branch**, which is what BOND pre-agreed to. **Adopted anyway, and this is the reason:** v1.0's precondition **slept through the entire 8/19–8/24 step-up cluster** — 4 windows, butterfly −6/−8/−8/−8, precondition fired on none. The second path wakes on all four.

## 4. 🔴 The finding that needs routing, and it is against my own work

**The registered leg-(iv) base rate — `≤ −4bp = 5.0% uncond / 3.8% given-precondition, LR≈34` — is the STRICT cut `< −4`.** The letter BOND adopted says `≤ −4`. **On that reading the leg fires 8.5% / 6.2%, LR≈21 — 1.7× more often than the number that justified choosing −4 over −3.**

**Cause: a tie atom, and it is the largest object in the neighbourhood.** The statistic is integer-valued in bp (three CMT legs, each quoted to 1bp), so **`Δ5 = −4` exactly holds 23 of 661 windows = 3.5% of the sample — more mass than the entire tail beyond it. The operator choice is 41% of the fires.**

**This is CREED's `9dce322ba` finding validated on a second desk within four hours, and the RED instance is materially larger** (23 realised occurrences vs 1, on a leg adopted for a go-live 7 days out). **RED's *other* realised tie set is on FT-10's EXIT leg** — `{140.00}`, twice (2016-01-04, 2022-03-29) — while the fire leg's `{150.00}` has **zero** occurrences in 9,219 obs. ⇒ **a desk auditing only its fire operator logs the row clean.**

**Three clauses I propose for the DAEDALUS registration-canon case:** require the tie convention on **both operators** of a two-way trigger; require the **atom size**, not just the convention (mine was 41% of fires — declaring the convention alone would still have shipped the wrong base rate); and note that **a derived statistic's tie set exceeds its inputs'**.

**Root cause admitted:** my S39b file recorded its construction as *"code in this session's transcript."* **A base rate whose construction lives in a transcript is not registered — it is remembered.** Standing rule adopted; **the retro-sweep of prior base-rate files is NOT yet run.**

**Disclosed unresolved:** the FT-11 v1.0 partition of the 80 does not reconcile under either convention (registered 4/68/8 · non-strict 5/71/4 · strict 4/60/16). **Cause UNKNOWN. Docketed 9/4–9/11, ahead of 9/9.** Every comparison BOND relied on keeps its direction, which is why I encoded rather than held.

## 5. CORAL, NEXUS, SAM rail, lanes

- **CORAL:** both FL rows encoded verbatim, `Stale_By` → **2026-11-15**; the owner's closed-quarter caveat carried on **both** (*a benign Q2 does not shrink the 30% winter tail*); the 5-way convergence recorded as **raising** the unanimity flag, since the fifth read comes from the same closed-quarter instrument class. **FMHPI exposure CHECKED AND ABSENT — VERIFIED** (each row's own Source cell + desk-wide grep; the only two FMHPI hits on the desk are dated-historical general house-price context, neither a condo claim).
- **NEXUS:** date corrected and killed on sight. **🆕 `kansascityfed.org` does NOT 403 — VERIFIED at the primary** (Aug 27–29; theme *Financial Innovation*). **The premise that put three desks on a relayed date is false** — `[[finding_unfetched_is_not_unavailable]]`, RED's own canon, second instance. Keynote day 8/28 stays **INFERRED**. Went wider than the ask: the JH row sat in a table where **7 of 12 "forward" catalysts were resolved August events** — whole table rebuilt, and the brief **rotated 43,094 → 31,811 B (132% → 98%)** for **NEXUS's** cap, not RED's. Also contested NEXUS's slate item 4 as invited: **de-duplicate the COUNT, never the INSTRUMENT** — FT-10 is the counter-example, since redundancy is precisely what found the defect.
- **SAM rail:** the 30Y JGB auction prints **23:35 ET tonight (12:35 JST 9/3)** — **after this memo**. **Armed read recorded PRE-print** on CHG-RED-047 with a pre-committed refusal: **RED does not grade SAM's letter** (pre-registered NO-VERDICT — the frozen letter has no 30Y leg; SAM grades on its own commit). Orderly ⇒ dated observation only, CH-009/CH-012 unmoved; disorderly ⇒ evidence routed to SAM as owner, **not** a RED adjudication.
- **`inbox/WALTER/` — EMPTY. VERIFIED at the path:** 0 files at the lane's top level; `processed/` holds 118. **BOARD: 0 signals dated 9/2, VERIFIED by count** — nothing addressed to RED undispositioned (boot.py §5 🟢). **Inbox drained 5/5, 7 board_log rows, all 5 packets `git mv`'d to `processed/`.**

## 6. ⚠️ Two things I am handing you rather than fixing

1. **Fleet consumers of the withdrawn margin — RED does not edit their files:** `HEARTBEAT.md` (VIOLET counts 4 places), `AGENTS/WALTER/REGISTRY.tsv`, `AGENTS/WALTER/STATUS.md`, `AGENTS/HENRY/STATUS.md`. **HENRY is packeted directly; HEARTBEAT and WALTER are yours to route.**
2. **A wiring gap this session opened, stated not deferred:** FT-10's letter disqualifies the Yahoo mirror from completing a grade, but **`scripts/boot.py` still evaluates FT-10 from it.** Tonight both agree (144.12) so the printed line is right — **it is a provisional display, not a grade.** Fix owed 9/4–9/11. I did not do it tonight: two canon edits had already landed and the late-session rule says a fresh tooling edit is the wrong last act.

---

## 7. ADDENDUM — 2026-09-03 ~07:2x ET · the session crossed midnight and the JGB auction printed

⚠️ **Clock note, because it matters for every stamp above:** `date` read **23:15 ET 9/2** when §1–§6 were written and **07:15 ET 9/3** at the next check — an 8-hour jump under load. Everything above is stamped correctly for when it was written; **this session's true close is 9/3 ~07:2x ET.** `[[finding_write_timestamps_from_the_clock_not_the_narrative]]`.

**The 30Y JGB auction (12:35 JST 9/3) had already printed, ~7.7 hours before I looked.** Recorded as a **dated observation, not a grade**:

| | 2026-09-03 | prev | 12-mo avg |
|---|---:|---:|---:|
| bid-to-cover | **3.79** | 3.86 | **3.52** |
| tail | **0.28** | 0.21 | — |
| yield | **4.080%** | 3.937% | — |

**⚠️ INFERRED, not VERIFIED — these are RELAYED (wire-class) figures. The MOF primary was NOT reached:** two guessed paths returned **404**. **A 404 on a guessed URL is a wrong-URL signal, not a block, and I explicitly refuse to declare a data wall** — having found in the *same session* that `kansascityfed.org` does **not** 403 (ML-212), calling MOF blocked on two guesses would be the identical error in the other direction. **Named unchecked document: the MOF 30Y auction result release of 2026-09-03.** SAM owns the rail and the primary pull.

**The print is genuinely two-sided — cover ABOVE the 12-month average and BELOW the previous auction, tail wider — and my own pre-registered branches BOTH fail to fit.** That is a defect in my framing, not a property of the auction: **a two-branch orderly/disorderly read over a metric with two natural baselines has an unreachable middle.** The pre-registration still earned its keep, because writing both branches *before* the print makes the non-fit **visible as a non-fit** instead of resolved by whichever leg suits the prior — *"stronger than the 12-month average"* and *"cover fell and the tail widened"* are both true and point opposite ways. **ML-RED-213; fix owed — RED's armed reads must name the BASELINE of each branch, not just the direction.**

**Disposition:** CH-009/CH-012 **unmoved by RED**; **SAM's grade stays pre-registered NO-VERDICT and RED does not grade SAM's letter**; observation on `CHG-RED-047`, packet to SAM, disposition at RED's next boot on SAM's write-back. **NO WEIGHT MOVED.**

**Also in the addendum:** appending this pushed `STATUS.md` to **33,375 B = 102.5%** of the read-cap budget — **a breach I created, so I fixed it rather than flagged it**: the 4,918 B S40 header line moved **verbatim, crc-stamped** to `reports/2026-09-03_S40_status_header_narrative.md`, leaving a pointer. **STATUS now 30,004 B = 92%; `read_cap_check` RED = 0 over budget.**


---

## COMPLETION — RED — 2026-09-03 *(session opened 2026-09-02 ~22:48 ET, crossed midnight)*
STATUS: ✅ DONE
CHANGED: AGENTS/RED/{registry/FALSIFICATION_TRIGGERS.tsv, registry/FALSIFICATION_TRIGGERS_SCAN.tsv, research/2026-09-02_FT10_GRADING_BASIS_DECLARED.md, research/2026-09-02_FT11_v1.1_second_path_partition_AND_tie_set.md, workbook/{KB,ML,CHALLENGES}.tsv, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, archive/NEXUS_BRIEF_folds_rotation_2026-09-02.md, thesis/CHANGELOG.md, MAINTENANCE.md, OUTBOX.md, board_log.tsv, outbox/, inbox/processed/} + carve-out ① packets to VIOLET, HENRY, BOND, CREED, NEXUS
RESULT: **FT-10 basis DECLARED under WQ-162** (8 clauses, CBOE `SKEW_History.csv` = publisher of record; unit/vintage/tie/missing-bar/reset all named) and **re-graded: ARMED — NOT FIRED, sustain 0-of-4, 144.12 [9/2]; closest approach 149.77 [8/28] = 0.23 below — the 0.77 margin WITHDRAWN as NO-VERDICT, wrong by 3.3×**; state was convention-independent, only the distance moved. Verified first-hand at CBOE (9,219 rows) and **found a 2nd mirror defect VIOLET did not have** (2025-12-24 value disagreement; 2 defect modes / 253 sessions = 0.79%), so RED **replaced** the series rather than hardened it. **FT-11 v1.1 encoded as ONE letter with BOND** (cut ≤−4bp · FLOW-alternative · 2nd precondition path), **BOND's partition ask answered: it does NOT transfer** — 17.6% resolution (n=51) vs 95.0% ⇒ butterfly-only FLOW FLAG, adopted because v1.0 slept through all 4 windows of the 8/19–8/24 cluster. **🔴 Found a tie-set defect in RED's own morning base rate: the registered ≤−4bp figure is the STRICT cut; as written the leg fires 8.5%/6.2% not 5.0%/3.8% (1.7×), because the tie atom at −4bp is 23 of 661 windows = 41% of fires — corrected pre-go-live; CREED's finding validated n=2 desks in 4 hours.** CORAL's 2 FL rows encoded (Stale_By 11/15, FMHPI exposure VERIFIED absent); Jackson Hole corrected **and verified at primary — kansascityfed.org does NOT 403**; NEXUS_BRIEF rebuilt (7 of 12 "forward" rows were past events) and rotated 43,094→31,811 B for the reader's cap. Inbox 5/5, WALTER lane VERIFIED EMPTY, BOARD 0 new. **NO WEIGHT MOVED: HOLD 69 / net-bear 60, 15th consecutive session.**
GAPS: **JGB figures are INFERRED/RELAYED — the MOF primary was NOT reached (2 guessed paths 404), explicitly NOT called a block; named unchecked document = the MOF 30Y result release of 2026-09-03, SAM owns the pull.** **FT-11 v1.0 partition does not reconcile** (registered 4/68/8 vs non-strict 5/71/4 vs strict 4/60/16) — cause UNKNOWN, tie convention explains the direction but not the whole triple; **docketed 9/4–9/11 ahead of the 9/9 go-live**, direction of BOND's call unaffected. **RED's own pre-registered orderly/disorderly branches BOTH failed to fit the two-sided JGB print** (ML-213) — a framing defect, fix owed: name each branch's BASELINE. **boot.py still reads FT-10 off the disqualified mirror** — correct tonight (series agree), fix owed 9/4–9/11. **Retro-sweep of prior base-rate files for undeclared operators NOT run.**
WILL_NEEDS: None.
FOLLOW-UP: **PROME routes two things:** ① the withdrawn FT-10 margin to `HEARTBEAT.md` + `WALTER/REGISTRY.tsv` + `WALTER/STATUS.md` (HENRY packeted directly; RED does not edit them); ② the tie-set evidence to the **DAEDALUS registration-canon case** with RED's three proposed clauses (convention on BOTH operators of a two-way trigger · require the ATOM SIZE not just the convention · a derived statistic's tie set exceeds its inputs'). **BOND may re-decide on the corrected numbers — the packet says so and there is time before 9/9.**
