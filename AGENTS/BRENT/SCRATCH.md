# BRENT SCRATCH — Fri Aug 21, 2026 **~14:4x ET** *(live session #4 — the GRADES session; Will closed it at ~14:4x, BEFORE the COT print)*

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

## ✅ WHAT SESSION 4 DID *(all committed and pushed; origin verified by path AND hash)*

**① `BRT-26` GRADED — 452 oil rigs (−3), NOT BREACHED, 2 → 5 away.** Confidence **HELD ~58%**, not re-marked off one print (symmetric with holding through a +1 on 7/31).
⚠️ **The headline flatters the row and I did not take it:** the whole US −5 is **DIRECTIONAL** rigs (50→45); **HORIZONTAL flat at 533** ⇒ the productive-rig base did not retreat, **BRT-04's mechanism reads UNCHANGED**. Anyone relaying "US rigs −5" as a supply-response signal has it wrong.

**② The month-long "BH primary times out" caveat was FALSE — and it had hardened into a SPEC.** The host **tarpits a self-identifying User-Agent**: `TimeoutError` at 20s AND 45s vs **HTTP 200 in 0.1–0.4s** on a browser UA. The registry's probe literally read `manual:two independent aggregator pulls`. **First primary-sourced grade in this ladder's history.** → `LESSONS L25`; the fix already existed **one function away** in the same file.

**③ Row 58 DELIVERED, then SELF-REFUTED within the hour.** The B-1 base rate I had only *offered* to run, run: **38% of war days sit at/below a pre-war-normal bar, longest run 25 trading days (6/12–7/20), going negative, ending three days before the war's high.** An exit keyed to it sells the bottom. **B-1 demoted to context; B-2 explicitly NOT promoted (it is merely unmeasured).**
★ **The result that matters is the CONVERGENCE:** the lessons sweep (`L11`/`L16`) and the base rate reached the same wall independently ⇒ **the exit latency is a property of the expression, not a parameter TERRY can tune.** That is a Will/TERRY choice to make in daylight.

**④ `INCIDENTS` backlog 17 → 12 ACTIVE; every bpd-bearing row now attempted.** 5 re-verified, 8 attempted-and-recorded. ★ **All four resolved corrections REMOVED asserted outage** — the header's directional-bias warning realised 4 of 4. Two new checks: **I-8** (a row asserting more offline than the facility has, in a status nothing read) and **I-9** (correcting a row **silently removed it from supervision** — I tripped that myself; it revealed the flag was **understating** the backlog: true stale count **18**, not 12).

**⑤ `KILL-LEG2-TRANSIT` re-spec DELIVERED to Will — 3 decisions, nothing registered.** Keyed to the **JWC war-risk listing**: headline-immune, binary, published. **I asked "can it fire?" FIRST this time** — yes, `Deleted: Pakistan` after 20+ years. Weaknesses stated by me: it is a **confirmer** (~4.5-month latency) and a delisting **can be lobbied**, so it is proposed as an **asymmetric standing negative**.

**⑥ 🆕 `JWLA-034` — the London war-risk market put SAUDI ARABIA in the Listed Areas on 2026-07-29 and no surface of mine carried it.** Primary PDF pulled and quoted. ★ **7/29 PRE-DATES the w/c-8/3 Yanbu collapse** ⇒ a **candidate mechanism** that is correctly ordered in time, unlike the reallocation story. Routed FALCON + HAWK **as a candidate, not a conclusion.**

**⑦ SPR falsifier premise WEAKENED three weeks early.** DOE primary is **not** empty on 2026 (my surface said it was); premium is **per-solicitation and rose** (June 1.26× vs carried 1.18–1.24×); and **DOE deliberately does not publish the return schedule** ⇒ the ~9/9 branches hang on a window the issuer never published. WALTER packeted.

**⑧ Forward check ② re-spec'd 3 days before it runs.** As written it compares a **670 kbpd Asia-only, month-scoped** figure to a **2.17 mb/d total-weekly** bar ⇒ a **−69% phantom collapse, in my own favour.** ⚑ **FALCON caught this, not me.** Perimeter/cadence/basis/vintage conditions added + a `NOT RUNNABLE` branch.

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
3. **⏸️ WILL-GATED, UNTOUCHED, DO NOT ACT UNASKED:** the boot-load cut (staged, prepped, peer-reviewed — **a reviewer's concur is not Will's word**) · the second `USO Oct-16 135C` (blocked on the unsatisfiable 60–90 DTE band and the root-rule-#6 break) · the `KILL-LEG2-TRANSIT` 3 decisions.
4. **⏳ FORWARD CHECK ② runs ~8/24–31** — use the AMENDED spec, and record `NOT RUNNABLE` rather than converting a mismatched figure.
5. **🟠 `INCIDENTS`: 12 ACTIVE + 6 unbudgeted still stale.** Remaining un-attempted are the ZERO-BPD set only (RF-004, RF-016, RF-030 wrong-unit; RF-033 no-double-count). ⛔ **Six unlogged Russian strike events are NAMED across RF-013/RF-009/RF-017 and owed as rows** (relay-grade sourcing; LESSONS #1 wants a primary first).
6. **🟠 BRT-29's mechanism deadline is 8/31 — 10 days.** Its leg needs **≥3 NAMED carriers citing fuel/war economics**; the strongest evidence is arriving as **aggregate capacity** (ME −5.7% YoY). ⛔ **Do not substitute off-list evidence for the leg as written** — count carefully, and if it does not fill, the honest verdict is a SPLIT.
7. **🟠 STATUS is at 250 lines / ~210 KB — AT the cap.** Archiving is blocked on DAEDALUS-owned anchors and the byte cut is Will-gated. **Disclosed, not resolved.**

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
- **⏳ OPEN: the SECOND contract** — roll to `Dec-18 $135C` vs hold to Oct-16. **Blocked on the two unanswered rulings. NO FILL WITHOUT BOTH.**
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
