# BRENT SCRATCH — Tue Sep 8, 2026 ~12:2x ET

**Purpose:** ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> ⛔⛔ **TODAY'S DOCKET IS UNWORKED AND STILL OWED. THIS SESSION DID ARCHITECTURE, NOT MARKET WORK.** It ran from 9/7 through **9/8 ~12:2x ET** — i.e. straight through the 9/8 open — and **touched none of the dated items below.** `$0` moved, no tape pulled since the 9/7 12:2x crude read, **no equity/option marks refreshed since the 9/2 post-close chain pull.** ⚠️ **`DOCKET L198 ①②` was due at 0d and is now LATE. `L252/WQ-168 ⑦ leg 1` grades on TODAY'S XLE CLOSE (16:00) — if you are reading this before the close it is still catchable; after it, grade from the settled close and say the read was late.** **Do the docket FIRST next session — mechanical before creative (root rule #8).**
>
> ⚑ **WRITE MODE (rule 19, and this file is the test):** this handoff carries STATE and NEXT ACTIONS only. Every "why" from the 9/7 session is in the commit bodies (`git log 3bbf6a1db..55669cd02`), `archive/STATUS_DETAIL_2026-09.md` § REPAIRS, and `RULINGS.md`. **Do not re-tell it here.** Previous SCRATCH was 19,693 B and read like a session transcript.

---

## ⛔ READ FIRST — THREE THINGS THAT CHANGE HOW YOU WORK TODAY

**① `BRT-29` IS ARMED. Its premise graded MET 6/6 on 9/7** (GASREGW ≥$4.00 in ≥4 of 6 prints 7/27–8/31; all six cleared). Legs **(M)** and **(T)** are LIVE and resolve **2026-09-30**. ⚠️ **(T) needs the EIA gasoline 4-wk YoY to reach ≤ −3.0% by the wk-ending-9/25 print — start watching it at the 9/9 WPSR, not at the end.**

**② THE FRED BLOCKER WAS FALSE AND I CARRIED IT FOR FIVE CYCLES.** `.env` exists on Will's box with a live `FRED_API_KEY`; the keyed probe works. `.env` is **gitignored**, so only the CLOUD routines lack it — their honest `env_doctor FAIL` was copied onto this desk as a fact about "this box". **Never re-flag it.** `RBRTE` was a second bug inside the first: it is an **EIA** series id, not a FRED one — FRED's Brent series is `DCOILBRENTEU`. ⇒ **"My access path failed" ≠ "the evidence is unavailable"**, and a failure inherited from ANOTHER environment is not a report about yours.

**③ BOOT NOW EXITS rc=2 ON BLOCKING FINDINGS AND IT IS NOT A CLEAN BOOT TODAY.** Ledger Staleness + Ledger Nudge are 🔴 on real state (`INCIDENTS.tsv` +16d, `LESSONS_INDEX.tsv` +11d). rc contract: **0 clean · 2 ran-fine-with-findings · 1 a script broke.**

---

## ✅ WHAT THIS SESSION DID — 5 commits, all pushed (`a6c4145dd` → `55669cd02`)

**Housekeeping + architecture. `$0` moved, no trade proposed, no claim/confidence/threshold/level changed.**

| # | landed |
|---|---|
| `a6c4145dd` | Ledger staleness `--days 7` on a MEASURED base rate (n=178; `--days 30` flagged 0/178 — provably inert) · `TRADE.md` two-clock stamp · Baker Hughes probe rewired (`bhrigs:`, runtime uuid, decoy guard) |
| `b7fea3678` | False FRED blocker withdrawn · keyless FRED fallback · GASREGW → `$4.071` (8/31) · BRT-29 premise MET · STATUS v5.7→v5.8 |
| `df83fa757` | 4 CODEX defects: Cushing trigger unbound from `util` · prediction scanner (4 of 5 OPEN rows were unscanned) · boot rc contract · STNG container label |
| `3bbf6a1db` | **Rule 19 first application:** STATUS 75,158 → 22,338 B · calendar GENERATED from `CATALYSTS.tsv` |
| `55669cd02` | P3 completed 9/9 · reconciliation guard's two false greens fixed · repair stories moved to the cold record |
| `ccac63155`…`3c3f44ded` | 3 more charter contradictions · 2 more guard false greens (unbolded row · first-match grade date) · charter headroom 19 → 1,129 B · **P2 inventory started, `workbook/TRADE_OBLIGATIONS.md`, 16 rows** · tranche-2 rotation BLOCKED |

**Read cap:** ⛔ **no byte figures are copied here — run `python3 scripts/read_cap_check.py --agent BRENT`.** A copied measurement is stale the moment the file it measures is edited: this line carried its own size as `8,995 B` and was wrong inside the same commit that wrote it. **State: `TRADE.md` is OVER THE CAP (the P2 target) and `LESSONS.md` is over budget (ACTION 16); everything else is under.**

---

## ⏳ NEXT SESSION — FIRST TASK IS ASSIGNED

**🔴 P2 — the TRADE.md obligation inventory** → `workbook/TRADE_OBLIGATIONS.md` (tranches 1–2 in progress, 16 rows). ⛔⛔ **DO NOT ROTATE THE "HISTORICAL" SECTIONS — 6 LIVE OBLIGATIONS SIT INSIDE THEM** (the Will-directed survive-every-edit caveat at L595 · HALF/HALF sizing + both tranche conditions at L599–604 · the UNRESOLVED two-clock interaction at L604 · unresolved §0a at L597 · STAGE B persistence + the KILL TEST at L668+ · the 35a `REVERSE` modifier at L743). **A superseded section HEADING does not make the clauses inside it superseded** — 33 marker lines measured. ⚠️ **THOSE ARE RECONCILIATION CANDIDATES, NOT VERIFIED SURVIVORS** — reconciling just two of them found two errors (the 35a modifier is `REVERT` not `REVERSE`, and its incumbent band is RETIRED with `COT-FUEL-35B` as successor per `TRADE.md:738`; `WAR-RISK-HALVES` retired **8/07**, not 7/31 — that was a Worldscale conflation). **A marker scan is a DISCOVERY LIST, not a verdict.** Each row needs its own identity, trigger, destination and VERIFIED reader; anything called retired needs superseding evidence attached; split grouped rows whose condition, authority or reader differ. **No byte moves until then.** ✅ **THE FULL 6-STEP EXECUTION PLAN IS WRITTEN — `workbook/TRADE_OBLIGATIONS.md` § P2 EXECUTION PLAN** (inventory the whole file with stable IDs → establish what governs now with evidence → assign destination AND the moment it is read → move rules and readers TOGETHER → archive only after every obligation has a disposition → run the acceptance checks incl. proposal / mid-session-escalation / position-review scenarios). ⛔ **DONE = rules accounted for, readers work, TRADE small enough — NOT a longer inventory.** ⚠️ **`setups/SPECS_*.md` does not exist yet — it is a proposed destination, not a place.** **LESSONS (ACTION 16) and INCIDENTS are SEPARATE workstreams with their own completion criteria — do not let them ride on P2.** ⛔ **And do NOT offer `instrument_check` or `Derived Views` as replacement readers** — they check instrument health and stamp timing, never that the deciding agent read and applied a clause. One row per binding clause: `clause · from (section) · to (file § section) · reached by (which boot/closeout/decision step reads it)`. **A clause archived without a reader is lost operationally.**
> ⛔⛔ **VERIFY EACH READER PATH — DO NOT JUST FILL THE `reached-by` COLUMN.** A pointer in that column records **intended** access; it is not evidence of access. For every row, OPEN the named step and confirm it actually travels to the clause — the step exists, it is not conditional on something that never fires, and the path resolves after the move. ⚠️ **A filled column passes every presence audit while the obligation is unreachable** `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`, and this desk has already shipped that exact failure THREE times in two days: the calendar check registered at a path boot could not resolve · the standing guard that counted stamps instead of rows · `board_log.tsv` scored as a boot read because it was NAMED on a read line. **The inventory is only worth building if each row is a checked claim.** `[[finding_record_of_an_action_is_not_the_action]]` Then the binding-letter moves to `setups/SPECS_*.md` and the dated rotation to `archive/TRADE_*.md`. ASK-2 (self vs one RAV slot) needs no answer — DAEDALUS marks it optional.

| when | what |
|---|---|
| **TODAY Tue 9/8** | 🔴 **DOCKET L198 ①② — DUE NOW (0d).** ② is the live one: grade the PortWatch 8/31 print on *Sidr*/*Senegal Prosperity* (`≥~500k dwt` = series sees VLCCs; `<250k` = coverage defect). · 🔴 **L140 Russia diesel producer-direct carve-out — FIRST REAL READ, read the DECREE TEXT** (403×2 so far; extended to 9/30). · 🟠 **DOCKET L252 / WQ-168 ⑦ leg 1 — did XLE close ≥$66.50?** From `$64.06` (9/4) that is +3.81% in one session; expect NO ⇒ **L253 fires the 9/9 open. TERRY/Will's call.** · OSPREY's Russian seaborne 7th-week print. · matched Dated-Brent physical-vs-paper (owed since 9/2). |
| **Wed 9/9** | 🔴 **WPSR wk-9/4 — first instrumented read of Edouard** (pre-registered: `>~1pp` utilization fall ⇒ under-disclosed; flat-to-`−1pp` ⇒ the narrow read was right). **TRACKER lines 1–6 UNVERIFIED until this print.** · **START THE BRT-29 (T) WATCH: gasoline 4-wk YoY vs the −3.0% bar.** · SPR exchange-window test. |
| **Fri 9/11** | 🔴 **THE FRIDAY PAIR.** Baker Hughes ~13:00 — **the `bhrigs:` probe now grades it; run boot and read the number** · COT as-of Tue 9/8 ~15:30. ⛔ **DO NOT LET GRADES STACK.** ⚠️ **This is the cycle that closes the DAEDALUS demote trigger** — any derived-pointer disagreement (version fields · calendar event set · BOTTOM-LINE stub) ⇒ **L4 at PR#6 (9/15)**. |
| **Fri 9/18** | 🔴 **USO Sep-18 150/165 spread EXPIRY.** |
| **Wed 9/30** | XLE 65C expiry · **`BRT-12` · `BRT-26` · `BRT-29` all resolve** · BRT-26's window closes (last print inside it 9/25). |
| **Sun 10/4** | 🟠 OPEC+ — the NOVEMBER decision. ⚠️ **RE-PULL spare capacity at the primary; do not carry `0.02` forward.** |
| **Mon 10/26** | 🔴 **`BRT-30` RESOLVES** (JWC listing; baseline `JWLA-034`). Standing negative — nothing makes anyone re-read it. |

---

## 🔓 OPEN THREADS

- ⚠️ **THE `Derived Views` GUARD'S KNOWN LIMITS — recorded because a guard's blind spots must travel with it, not be rediscovered.** It went through FIVE rounds of CODEX fixtures on 9/7–9/8; each round found a real false green. **What it NOW catches** (all falsified): missing stamp on any row · stamps moved outside the STANDING STATE section · a row reconciled before a catalyst's grade date · a row that lost its **bold** · a LATER re-grade appended after an earlier one · calendar drift from `CATALYSTS.tsv`. ⛔ **What it still does NOT do:** it never checks whether a standing VALUE is correct — only whether the row was *reconciled after the newest grade*. **A row stamped today with a wrong number passes.** It also reads grade dates only from `CATALYSTS.tsv` prose, so a grade that never becomes a catalyst row is invisible to it. ⇒ **The stamp certifies that someone LOOKED, never that they were right.**

- 🔴 **`TRADE.md` 182,606 B = 337% of cap** — P2, above. **`LESSONS.md` 90%** — ACTION 16 (split by KIND, never by age; `lessons_check --prose` moves in the SAME commit, C2).
- 🟠 **`INCIDENTS.tsv`: 12 ACTIVE rows past the 60d re-verify budget** (oldest RF-004 at 172d) + 6 present-tense rows outside it. **⛔ DO NOT relabel them to a new status token** — a new token drops the row from BOTH I-2 (`status == ACTIVE`) and I-9 (hardcoded tuple), verified. Fix = an `evidence_state`/`verify_due` column the checks read. **Will's call: scoped batch re-verify, or explicit stated-boundary acceptance.**
- 🟠 **Acceptance test ④ IS BEING MEASURED RIGHT NOW and is not yet claimable:** does the closeout AFTER P1 keep the files small, or rebuild the narrative pile? The write pattern — not the byte counts — is the live risk; it recurred **four times** on 9/7, each time while fixing something else.
- 🟠 **`NEXUS_BRIEF.md` 44,502 B / 145 lines** — DAEDALUS ACTION 20 (re-order to amendment 12) at the next re-pin.
- 🟠 **DAEDALUS ACTIONs 17–19 not started:** INCIDENTS column · charter step 8 on the 12 `PREDICTIONS` rows over 2 KB (ARCHIVE unwritten since 6/20) · one retirement `git mv` pass + the FASTOW dormancy note.
- ⚠️ **`BRT-07` carries `OUTER BOUND 2027-03-06` in its STATUS cell, which the scanner does not read.** Event-conditional by design; check by hand.
- ⚠️ **TERRY:** decoupling-vs-XLE falsifier slot **NAMED BUT EMPTY on a filled position.** 9/8–9/9 is when it matters.
- **Energy HY OAS: unmeasured here** (LIQUID owns systemic). **No GCC-transit war-risk series and no Iranian-export series on this desk** — both figures are RELAYED.

---

## 💼 POSITIONS

**NONE PROPOSED. `$0` moved.** **USO 35 sh · USO Oct-16 135C ×2 · USO Sep-18 150/165 ×1 · XLE Sep-30 65C ×2.** `TRADE.md` canonical for marks and money; **position truth is off-repo (Will/broker direct).** ⛔ **Marks NOT refreshed since the 9/2 post-close chain pull** — no decision point arose (`RISK_RULES` #5 pulls the chain AT a decision point, not on a schedule). **Two legs die inside four weeks.** ⛔ **NO LIVE DEPLOY GATE EXISTS** — re-arming needs a fresh Will ruling. Frame-breaker carve-out, Stage-A and the OFF-RAMP playbook all SURVIVE; the carve-out's `vessel SUNK` limb now requires confirmed cargo/throughput loss (WQ-189, prospective from 9/7 14:42).

## 📬 MAIL

**Inbox 0** (1 consumed — DAEDALUS architecture review; logged to `board_log.tsv`, `git mv`'d to `inbox/processed/`; moved == logged == 1). **Outbox clear.** **ASK-1 answered in the `3bbf6a1db` and `55669cd02` commit bodies** (which of P1/P5 landed); the artifact is the receipt, no reply packet owed.
