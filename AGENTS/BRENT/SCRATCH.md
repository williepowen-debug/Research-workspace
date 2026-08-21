# BRENT SCRATCH — Fri Aug 21, 2026 **~16:4x ET** *(live session #4 FINAL CLOSEOUT — the GRADES session, which then ran long: both grades taken, STATUS cut −44%, KILL-LEG2 ruled+encoded, three position rulings)*

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ✅✅✅ **BOTH GRADES ARE TAKEN. THE COT WAS GRADED AT 15:30 ET ON ITS OWN PRINT — ZERO LATENCY, NO STACKING.**
>
> **This banner previously said the COT grade was OWED and told the next session to take it. It is DONE.** The session did not end at 14:49 as planned — work continued into the STATUS cut, the release posted ~15:30, and the grade was taken on the print.
>
> | Series | Result |
> |---|---|
> | **Baker Hughes** (`BRT-26`) | ✅ **452 oil rigs, −3 WoW, NOT BREACHED**, distance 2 → 5. Graded at the PRIMARY, a first for this ladder. |
> | **CFTC COT as-of 8/18** (`COT-FUEL-35B`) | ✅ **JOINT `NO-VERDICT` ⇒ sizing DEFAULTS TO BASE CASE.** Leg A `108,059` ⇒ **SPENT** (first ever) · Leg B `5.7206%` ⇒ NOT-SPENT (GATING). |
>
> ★★ **THE COT'S REAL CONTENT IS THE LEG OPPOSITION, NOT THE VERDICT: vintage #1 had both legs broadly aligned; vintage #2 has Leg A SPENT AGAINST Leg B NOT-SPENT — first direct opposition.** That is defect ⑤ (leg suppression) being ANSWERED rather than hidden. **Why: shorts fell 2,579 but OPEN INTEREST fell 3,469 with them, so OI-share moved only −0.126pp — absolute de-grossing, intensity ~unchanged.**
> ⚠️ **RAZOR-THIN, AND IT MUST TRAVEL: Leg A cleared the deadband floor by 1,106 contracts = 0.12 median units. A ~1% move flips it back. DO NOT RELAY "SPENT" AS ROBUST.**
> ⛔ **Retired incumbent NOT re-graded; for spec context only it would have sat in IGNITING (−21,013 vs its ≤−25,000 bar), so the retirement is NOT what changed the answer.**
> ⏰ **NEXT: COT as-of 8/25 releases Fri 8/28 ~15:30 · Baker Hughes Fri 8/28 ~13:00. DO NOT LET EITHER STACK.**

---

## ✅ WHAT SESSION 4 DID *(41 commits, all pushed, 0/0 with origin)*

**⑨ ✅ BOTH GRADES TAKEN — the mandate.** `BRT-26` **452 oil rigs, −3, NOT BREACHED, 2 → 5** (first PRIMARY-sourced grade in this ladder's history). `COT-FUEL-35B` vintage #2 **JOINT `NO-VERDICT`, sizing base case**, graded 15:30 **on its own print, zero latency**. ★ **The COT's real content is the FIRST DIRECT LEG OPPOSITION** (A `SPENT` vs B `NOT-SPENT`) — defect ⑤ leg-suppression visibly answered. ⚠️ **Leg A cleared its floor by 1,106 contracts = 0.12 median units — NEVER relay "SPENT" as robust.**

**⑩ ✅ `KILL-LEG2-TRANSIT` RULED BY WILL AND ENCODED.** All three per my recs unmodified. Retired **on INSTRUMENT grounds with the premise-NOT-refuted guard riding the token**. Successor `KILL-LEG2-JWC-LISTING` registered as the **asymmetric standing negative**; delisting **PROMPT-ONLY**. ✅ **And it is now SELF-ALERTING** — built a `jwc:` probe-grammar extension that watches the CIRCULAR NUMBER, because **reachability is not change-detection**. Falsified 4 ways. §13 prior-art line: **NOT novel** — `finding_dated_carry_item_has_no_expiry_check` already said it.

**⑪ ✅ THREE POSITION RULINGS (Will, ~16:3x).** **HOLD the second `135C`, no roll** — *every live catalyst fires BEFORE Oct-16; the roll bought 63 days with ZERO live catalysts*. **TENOR = SCOPE ruling** (`60–90 DTE` governs NEW deployments, not rolls) **with a binding guard: "roll" = same underlying/strike, later expiry ONLY.** **Root-rule-#6 break DELIBERATELY NOT RULED — `OPEN-BY-DESIGN`**, because no fill is on the table. ⚠️ **TERRY owes the `RISK_RULES` mirror — asked, NOT edited by me.**

**⑫ ✅ STATUS CUT −44% (Will-approved), ZERO CONTENT LOST.** `220,659 → 123,609 B`. ★ **T3 was the important tier and it was NOT the biggest — nine "standing state" rows under a CURRENT heading, THREE of them factually FALSE** ("NO OPEN ACTION", "INBOX EMPTY 8/7", "NOTHING OWED TO WILL"). **Root cause was DUPLICATION, not staleness** — replaced with a pointer, never a fresher copy.

**⑬ ⛔ THE LIVE ENTRY GATE NAMED TWO CAPITAL-AUTHORISING LEGS IT DID NOT DEFINE.** `(T)` and `(C)` were defined ONLY inside `STAGE-A v4 — SUPERSEDED`. Relocated verbatim into the live v5 gate. **No live capital risk (the arm is retired, nothing can fire) — but it had to be fixed BEFORE a re-arm, not discovered at one.**

## ⛔ MY OWN ERRORS THIS SESSION — all caught by checks, not by care
- **Four hypotheses wrong before testing:** HTTP/2 as the BH blocker (both protocols 200 in <0.3s — I had changed two variables at once) · Satorp's 230,000 as a "mislabelled running rate" (it is half of 460,000 either way) · Russian rows as "structurally un-re-verifiable" (they are not) · an "81-second race" explanation for PROME that PROME correctly refuted.
- **Declined a claim that would have flattered me:** a search summary asserted Tuapse *"remains shutdown as of August 21"* — the summariser's synthesis, no citation. Taking it would have licensed a fresh stamp.
- **Corrupted `CATALYSTS.tsv`** with raw newlines in a TSV field; field-count check caught it, `git checkout` restored, redo asserts no newline before writing.
- **Stamped the clock ahead of itself 3×.** ★ **Mechanism identified: I compose the stamp and run `date` in the SAME tool call, so the clock arrives too late to inform it. `date` must be a PRIOR call.**
- **Backticks in a double-quoted commit message** executed as command substitution and ate one word (`8eadc8988`). Use single quotes.
- **Ran a falsification under `--quick`**, which skips probes and reports everything STALE ⇒ rc=2 on a clean ledger. Noticed the anomaly instead of accepting a convenient pass.

## NEXT SESSION (dated, future-verifiable)
1. ✅ ~~TAKE THE COT GRADE~~ **DONE 2026-08-21 15:30 ET, zero latency. Next COT vintage as-of 8/25, releases Fri 8/28 ~15:30 — do not let it stack.**
2. **🔴 MON 8/24 — BESSENT PRESS CONFERENCE.** Grade on **PUBLISHED MECHANISMS** (OFAC designations, named entities, effective dates), **never on the presser happening** (L18). Pre-registered read is in the catalyst row — **do not rewrite it after the fact.**
3. **⏸️ WILL-GATED:** ~~the boot-load cut~~ ✅ **APPROVED AND EXECUTED FOR STATUS; TRADE.md is partially done and paused (see #8).** · the second `USO Oct-16 135C` (blocked on the unsatisfiable 60–90 DTE band and the root-rule-#6 break) · the `KILL-LEG2-TRANSIT` 3 decisions.
4. **⏳ FORWARD CHECK ② runs ~8/24–31** — use the AMENDED spec, and record `NOT RUNNABLE` rather than converting a mismatched figure.
5. **🟠 `INCIDENTS`: 12 ACTIVE + 6 unbudgeted still stale.** Remaining un-attempted are the ZERO-BPD set only (RF-004, RF-016, RF-030 wrong-unit; RF-033 no-double-count). ⛔ **Six unlogged Russian strike events are NAMED across RF-013/RF-009/RF-017 and owed as rows** (relay-grade sourcing; LESSONS #1 wants a primary first).
6. **🟠 BRT-29's mechanism deadline is 8/31 — 10 days.** Its leg needs **≥3 NAMED carriers citing fuel/war economics**; the strongest evidence is arriving as **aggregate capacity** (ME −5.7% YoY). ⛔ **Do not substitute off-list evidence for the leg as written** — count carefully, and if it does not fill, the honest verdict is a SPLIT.
7. ✅ ~~STATUS at the cap~~ **RESOLVED — WILL APPROVED THE CUT AND IT IS DONE: `220,659 → 123,609 B`, −44%, boot load −~24k tokens, ZERO content lost** (6 archives, all verbatim + crc32; conservation proven mechanically). ⛔ **The anchor blocker turned out to be a non-issue and that is recorded: only 2 `STATUS:N` refs shifted, both DATED AUDIT RECORDS in `board_log` that must NOT be re-pointed (re-pointing would rewrite the ledger's historical account); `STATUS:89` already pointed at a blank line before the cut.**
8. **⏳ TRADE.md — PARTIALLY CUT, FIVE SECTIONS LEFT (~87 KB), AND STOPPING WAS DELIBERATE.** `167,585 → 162,156 B` so far. ⛔⛔ **DO NOT ROTATE BY HEADING — TWO NEAR-MISSES PROVED IT: the `60–90 DTE` tenor ruling was living inside a section headed `2026-08-03 PRE-FILL DISCLOSURE` (a dated, closed-looking container), and the LIVE `Leg T v6` formula lives inside `STAGE-A v4 — SUPERSEDED`.** ★ **THE METHOD IS: EXTRACT THE LIVE SPEC FIRST, THEN THE REMAINDER GENUINELY BECOMES DATED RECORD.** The tenor rulings and both leg definitions are now extracted, so their origins ARE rotatable. ⚠️ **And internal cleanliness is NOT dependency-freedom — the one section I did rotate scanned clean internally and only a CROSS-REPO search found TERRY citing it (from a DEAD setup, so it was safe).**

## OPEN THREADS / WATCHES
- **⛔ SHARPEST EXPOSURE (v5.7) — now with a proposed answer awaiting Will:** an official narrative able to declare Hormuz resolved, against a falsifier that may be unable to answer it.
- **⚠️ `JWLA-033`'s BODY IS UNREAD** — so whether `JWLA-034` FIRST-LISTED Saudi or amended an existing entry is **unresolved**. Saudi IS listed today; that is all that is asserted.
- **⚠️ War-risk INSURANCE RATE levels remain `[STALE]` July-vintage.** `JWLA-034` is a **LISTING** action, not a rate quote — **do not conflate them.**
- **⚠️ Russian capacity-offline estimates disagree ~2.5× — DO NOT AVERAGE.** Reuters 17% (conservative live) · S&P 7 offline end-July +4 in Aug (cleanest count) · Kyiv Post 42.7% = CUMULATIVE-EVER-STRUCK, belligerent-aligned.
- **⚠️ Dos Bocas ATTRIBUTION CONFOUND:** RF-003+RF-020 assert 150,000 bpd offline at a facility whose baseline underperformance is large and pre-existing. Second instance of the Jazan-reformer class.
- **⛔ EXPORT-SIGN WARNING live · RUNS-DECLINE IS NOT CAPACITY-OFFLINE · every 8/19–8/20 Russian strike item is "fire reported" or CLAIMED with ZERO operator statements — do not convert into barrels.**
- **⛔ Unresolved:** Petroline 5 vs 7 mb/d · SPR floor 252.4M vs 400.0 · Yanbu↔Sidi Kerir double-count seam · `TANECO` incrementality · Mina Al-Ahmadi capacity 346k (reporting) vs 466k (ledger).

## POSITION DECISIONS PENDING
- **💵 WILL RULED 8/21: SELL ONE of the `USO Oct-16 135C ×2`.** ⚠️ **NOTHING FILLED, NO ORDER STAGED — execution is Will's.** ★ **The leg IMPROVED after the ruling: +41.7% (09:51) → +45.6% (14:2x, mid $10.35).**
- ✅✅ **RESOLVED 2026-08-21 ~16:3x — WILL RULED: HOLD the second contract to Oct-16, DO NOT ROLL.** `$0` moved, nothing staged. **Lead reason: EVERY live catalyst fires BEFORE Oct-16; the roll bought 63 days with ZERO live catalysts.** Supporting: the same-day SELL-ONE was a de-risk and rolling would have added $750 to the same view. ⚠️ **The ATM theta bleed (~$19.61/day, accelerating) is REAL and unresolved — it argues for CLOSING, never for rolling. If it becomes binding, harvest the second contract; do not extend it.**
- ✅ **TENOR — RULED as a SCOPE ruling:** `60–90 DTE` governs NEW STRUCTURAL DEPLOYMENTS, not rolls. ⛔ **GUARD: 'roll' = same underlying, same strike, later expiry ONLY; any strike/structure change is a NEW deployment and the band binds.** ⚠️ **TERRY owes its `RISK_RULES` mirror — flagged, not edited by me.**
- ⏸️ **ROOT RULE #6 BREAK — DELIBERATELY NOT RULED, and that IS the decision.** The test was met, but no fill is on the table after the HOLD, so ruling it would spend an operator decision on a dissolved question. **OPEN-BY-DESIGN.** ⛔ **If a same-strike calendar roll is proposed again, RE-MEASURE the day-colour cost on that day's tape — the 8/21 figures (~$21 / 2.8%) are NOT a standing pass.**
- **🟠 `XLE Sep-30 $65C ×2`: `$300` vs `$455.35` cost (−34.1%, live chain 14:2x), 40 DTE.** Disposition `LAPSE` **NOT re-ruled**.
- **NONE PENDING ON THE SHARES — WILL RULED HOLD 8/18.** 35 sh, basis $121.88, **+11.3%**. ⚠️ **No live stop.**
- ★★ **RISK SHAPE MOVED WITHOUT ANYONE ACTING: undefended-linear share 74.70% → 65.2% — NOT from selling, but because the defined-risk 135C appreciated faster. IT REVERSES ON THE WAY DOWN. Read as a MARK, never as de-risking.** USO-linked concentration unchanged at 95.9%.
- **⛔ NO LIVE DEPLOY GATE EXISTS.**

## MAIL STATE
- **INBOX 1 OPEN (deliberate) · WALTER lane 0 · outbox 0.** board_log **240** rows.
  - **DAEDALUS boot-load review** — `acted`, kept as the ACTIVE WORKING REFERENCE for the Will-gated cut. Archive it when the cut lands.
- **SENT THIS SESSION (7):** PROME ×3 *(UA-tarpit fleet advisory · row-58 delivery · row-58 CORRECTION · `KILL-LEG2` spec)* · CARL *(its UAs are FINE — measured; but `housing_pulse.py:83` Fannie URL 404s)* · TERRY ×2 *(row-58 + CORRECTION)* · WALTER *(SPR/DOE)* · FALCON + HAWK *(`JWLA-034`)*.
- **Owed TO me:** **Will** — the 3 `KILL-LEG2` decisions, tenor scope, root-rule-#6, boot-load go/no-go. **DEWEY** — `gie_pull.py`. **HAWK** — the three 8/21 asks.
- ✅ **CLOSED:** PROME row 58 (delivered + corrected, archived).

## 📒 LEDGER-NUDGE DISPOSITION
| Ledger | Disposition |
|---|---|
| **`TRADE.md`** | ✅ **REFRESHED 14:2x** — all four legs re-marked off the live chain. |
| **`INCIDENTS.tsv`** | ✅ **REFRESHED** — 5 rows re-verified, 8 attempted, I-8/I-9 added. |
| **`REGISTRY.tsv`** | ✅ **REFRESHED** — BRT-26 probe repaired, L25 cited. |
| **`LESSONS_INDEX.tsv`** | ✅ **REFRESHED** — L25 added (prose + index, same commit, C2 clean). |
| **`board_log.tsv`** | ✅ **REFRESHED** — 239 → 240. |
