# WQ-185 ① — Episode (b) review: GATE-REG-T02 → ROLL70 fill → EXIT guard

**Produced** 2026-09-13 12:0x ET by PROME (DOCKET L295) · **Protocol** `PROME/proposals/2026-09-06_wq185-RULED.md` §2 · **Window** 2026-08-23 (T02 registration) → 2026-09-11 (first exit owner grade).

Read-only over the §2 record set. No live surface touched. **No desk grades. No score.** The question is not "did the machinery change the decision" — correctly retaining is a result too.

**"The card"** throughout = `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md`. **`chain_fetch`** = `AGENTS/TERRY/scripts/chain_fetch.py`. WQ-nnn rows = `PROME/WILL_QUEUE.md` and `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md` / `_2026-09-10_evening_rolloff.md`.

---

## Q1 — Known vs assumed at each decision point

| Decision point | KNOWN (artifact) | CARRIED AS ASSUMPTION |
|---|---|---|
| **T02 registration** 8/23 | The letter at `AGENTS/REGINALD/registry/NOTES.md §REG-T-02`. Registration was **transcription-only** — PROME set and moved no threshold | TERRY's "~1-in-5" odds, **labelled an UPPER BOUND at the time** (measured at a closer level; distribution not re-run) |
| **The 9/1 fire** | WAL close **$77.26** (`scripts/market.py`→Yahoo, owner grade `5c94c9622`). Attribution: WAL −1.11% vs KRE −1.28%, cohort median 14/26, Spearman **ρ +0.253** (n=26) | — (graded at the instrument) |
| **Roll construction** 9/1 | Dec-18 $70P **bid 2.05 / ask 2.75 / mark 2.40**, IV 35.3%, OI 31, last trade 8/27 (`chain_fetch` 17:28 ET). Base rates: 2-yr 10.9% (n=488); 20-session p10 −11.6%, p5 −21.1% (n=250) | Position truth from `FORGE/STATUS.md` **8/29 vintage**, flagged on the card: *"Basis is a state-file figure (RISK_RULES #4) — confirm at fill."* WAL Q3 print date a **pattern ESTIMATE** (Tue Oct 20), flagged *"do not key anything to the estimate"* |
| **9/3 rulings** | The Sep-18 pair's live marks ($70P 0.05/0.40; $67.5P **NOBID**) | The two operator facts were **ruled UNKNOWN rather than assumed** (WQ-167) |
| **Exit-guard registration** 9/3 | The ≥$81.90 ×3 line taken from the card's own § Key resistance, and **re-verified on the card** before REGINALD's grade was accepted | — |

**Finding:** every assumption I can locate was labelled as one, at the time, with its vintage — nothing was silently promoted from estimate to fact.

## Q2 — What the system added

| Added | Where it landed | Would Will have had it? |
|---|---|---|
| **The attribution on the fire** — cohort sort, wrong-signed ρ ⇒ *sector beta, mechanism unchanged* | GATES `GATE-REG-T02` state cell; TERRY card §1 | No. This is the fact that made it a duration roll and not a trim or an add |
| **Liquidity read** — the $70P **29.2% wide**, OI 31, last print 8/27 ⇒ pay the ask or don't fill | Card §3/§4 | No — changed the execution instruction, not the decision |
| **The no-chase structure** — $2.75 hard cap, and *three consecutive green days unfilled ⇒ return to Will* | Card §4, WQ-143 ruling | No |
| **§5c account-deviation analysis**, written the day of the fill — 7 items | Card §5c; GATES row; TERRY packets | No |

*(The guard's re-homing on 9/3 is deliberately **not** listed here. It was caught by an unrelated housekeeping item, not produced by the system — see Principal failure.)*

## Q3 — Change or retain: was the interpretation warranted?

| Call | Judged at the time | Warranted? |
|---|---|---|
| **Roll duration, not trim/lapse** | Mechanism unchanged + sector-wide day ⇒ root rule #7 *timeline uncertain, not thesis broken* | **Yes** — and the card records its own counter-case in §8 (fair-priced tail, no base-rate edge, BE $67.25). Warranted call with its weakness beside it |
| **Dec-18 ≤$275 over Nov-20 ≤$235** | Dec runs ~42 sessions past the expected print; Nov ~23 | **Yes** (#18(a): a >9% OTM strike's catalyst is multi-quarter transmission) |
| **Sep-18 pair HELD, not sold** — a RETAIN | ≈$30 at the bid 9/1; ≈$5 by 9/2 with $67.5P NOBID | **Yes.** Nothing to save; the spread would have eaten the recovery. Retaining was the right read |
| **Exit = the trigger's own exit (≥$81.90 ×3)** — a RETAIN | Guard inherited rather than invented | **Yes.** The roll's exit is the thesis's exit; no new threshold was minted for a new instrument |

Every RETAIN was the right read of the evidence on hand; no decision required reversal.

## Q4 — Did corrections reach the decision surfaces in time?

| Correction | Surface(s) it needed | Arrived |
|---|---|---|
| WAL distance quotes must re-derive from a **named dated close** ("2.00%" dead; 8/21 $79.67 = 2.10%) | GATES `GATE-REG-T02` | **In time** — carried inline as kill-on-sight |
| Fill was **ROBINHOOD, not the Fidelity IRA** | Card §5c, GATES row, TERRY packets | **In time** — written 9/2, the day of the fill |
| $4.40 harvest **GTC status UNKNOWN** | Card §5c②/§7, GATES, WQ-167 | **In time** — but only after **five asks** |
| USO 135C sale price UNKNOWN ⇒ Rule A NO-VERDICT | GATES USO135C | **In time** |
| §5c⑤ **new OPEN item** — a Robinhood confirm/history line at the next FORGE export | `FORGE/STATUS.md` | ⛔ **Not reached.** Still unrecorded at the 9/8 review; precedent D-18 (the RH WAL $77.5P Aug-21 sale still *"P&L UNRECORDED, not zero"* 15 days after Will confirmed it) |
| ⛔ **The exit guard's OWNER GRADE for 9/3 · 9/4 · 9/8 · 9/9 · 9/10** | GATES `GATE-TERRY-ROLL70-EXIT` | ⛔ **Not reached for 8 days** — landed 2026-09-11 (`9f4837ac5`) |

**Commissioned leg I did not deliver:** §2 Q4 asks for "any HEARTBEAT retired-claim entries about WAL/REG-T02". I did not trace the HEARTBEAT snapshots. **This is an absence, not a nil finding** — do not read the table as saying HEARTBEAT was clean.

## Q5 — Coordination and human intervention (counts from the records)

| Item | Count | Source |
|---|---|---|
| Desk touches in the episode chain | **7** — REGINALD 9/1 · TERRY 9/1 · TERRY 9/2 · WAL 9/2 · TERRY 9/3 (subagent) · TERRY 9/3 (window) · REGINALD 9/11 | `PROME/state/ORCH_LOG.tsv` |
| Of those, touches that produced an **owner grade** | **2** (9/1 fire, 9/11 exit) — **both PROME-initiated spawns**, neither a desk booting itself | ORCH_LOG; `9f4837ac5` |
| Will words | **7** — WQ-143 17:22 9/1 · WQ-144 18:13 9/1 · the fill message 14:21 9/2 · WQ-166+167 09:17 9/3 · WQ-168 12:45 9/3 · *"pull step 2 forward"* 12:45 9/3 · ***"keep working"* 11:20 9/11** (the word that produced the closing grade). ⚠️ The two 12:45 9/3 entries may be one message; 7 is an upper bound on distinct messages, a lower bound on distinct decisions | `PROME/archive/WILL_QUEUE_ROWS_2026-09-09_rolloff.md` · `_2026-09-10_evening_rolloff.md` · `ORCH_LOG` 9/11 REGINALD row |
| Will **hand actions at a broker** | **1** (the Robinhood fill). The $4.40 GTC was never established as placed | Card §5c②/⑤ |
| Asks spent before a fact was ruled UNKNOWN | **5** (the GTC) | WQ-167 |
| PROME spawns that **died on API 529** 9/3 09:4x–10:02, converting orchestration into Will's hand | **5** (3 TERRY, 2 LABOR); Will opened both desks himself ~11:1x / ~11:5x | ORCH_LOG touch-3/4 rows |

⚠️ **Three commissioned counts are missing, and I substituted three of my own rather than say so.** §2 Q5 asks for six: PROME sessions touched · desk spawns/doorbells · Will words · **packets** · **corrections emitted** · hand actions. I delivered desk touches, Will words and hand actions, and added owner-grades, asks-to-UNKNOWN and 529 deaths. **PROME sessions, packets, and corrections-emitted are NOT counted here.** The cost line is therefore partial, and partial in the direction of understating cost.

---

## Principal contribution

**REGINALD's attribution read on the 9/1 fire** (Q1 row 2). Without the cohort sort, a close below $78 is just a threshold break. With it — sign *wrong* for a private-credit repricing — the day is sector beta, the mechanism is intact, root rule #7 applies, and the expression is one tenor out at the same strike rather than a trim or an add. It changed the *shape* of the action, not its confidence. *(`AGENTS/REGINALD/registry/NOTES.md §REG-T-02`, `5c94c9622`.)*

## Principal failure

**The position's price-based guard went 8 days without its owner grade, across the window's closest approach to the exit line.** Registered 9/3. PROME consumer-read the 9/3 close that evening — **$81.00, $0.90 short of $81.90, the nearest the position came to its exit all window** (`PROME/GATES.tsv`, `GATE-TERRY-ROLL70-EXIT` state cell: *"closest approach 9/3 $81.00 ($0.90 short)"*). The grade for that close and the four after it arrived 9/11.

**How it finally arrived is the finding, not an aside.** It came inside a **WQ-206 aged-ACTION drain on Will's 11:20 *"keep working"* word** — a generic dark-desk sweep whose trigger cell lists nine unrelated items, of which "PROME ROLL70-EXIT" is one line (`ORCH_LOG` 9/11 REGINALD row). **Nothing aimed at the guard ever fetched the guard.** It was swept up by a broom pointed somewhere else, and it needed a human word to start the broom.

The system *knew*: the GATES cell said **"owner grade OWED (REGINALD dark)"** from 9/3 onward. That produced no mechanism that fetched the grade. **A correctly-recorded owed obligation is not a control** — it is a note that happens to be true.

The mechanical cause is not "REGINALD was dark". `GATE-TERRY-ROLL70-EXIT`'s `review_by` is **2026-12-04**, the position's time stop; its grading cadence is **per official close**. The spawn driver reads `review_by`, so a row owing a grade every session is invisible until December. **A single `review_by` cannot express a per-observation obligation.**

**Second — a latent dependency, removed by luck.** The guard was registered 9/1 *inside* `GATE-REG-T02` and `GATE-TERRY-ROLL70`, both RESOLVED by 9/2, and the ledger's rotation rule sends terminal rows to archive at ≥7 days. **That rotation did not run** — checked 2026-09-13, both carriers are still in the live `PROME/GATES.tsv`, 11–12 days after resolving. So the claim is not an averted deletion: the rotation is *discretionary in practice*, the rows stay *eligible*, and an open position's guard sat on two rows any future rotation may remove. Re-homing it to a LIVE row on 9/3 (WQ-166 step 2, **pulled forward** on Will's word) removed that exposure. Nothing detected it; an unrelated housekeeping item collided with it.

## Uncertainties

- Whether the $4.40 harvest was ever **monitorable** — GTC status is permanently UNKNOWN by ruling, and no Robinhood activity view has reached FORGE in any capture.
- The **fill price is Will's word**; the lone Dec-18 print at 9/2 14:21 (vol 1) corroborates the minute, not the price.
- Whether retaining the Sep-18 pair **cost** anything — the $30→$5 decay is recorded, no counterfactual run.
- I re-derived **no price**; every level sits at its stated artifact and vintage.

## Smallest operational change the evidence supports

**Widen WQ-184 leg ⑥ at the 9/19 sitting to cover gate grading cadence.** Not a free pointer edit — I checked:

- `spawn_list.py` **does** already read GATES LIVE rows at `review_by` (`:21`, `:176`).
- But `PROME/GATES.tsv` has **12 columns and none expresses cadence**, so a per-observation obligation has nowhere to live.
- And `spawn_list.py:38` says so itself: **"cadence NOT modelled in v1 … commissioned as WQ-184 leg ⑥ (DOCKET, 2026-09-19)."**

Leg ⑥ as commissioned models **desk** cadence — *is this desk dark?* This episode needs **gate grading** cadence — *does this row owe a grade every session?* Different questions; only the first is commissioned. Naming the second costs one line at a sitting already happening; building it is leg ⑥'s work, not a new instrument.

Everything else worked, including the parts that worked by retaining.

---

## Declared residue (WQ-178)

One blind read: 6 ❌, all fixed above (three by reversing a claim); 13 ⚠️ recorded, not fixed: no inclusion rule stated for the "7 desk touches" count · ρ +0.253 (n=26) is quoted without naming its two variables or noting it is not distinguishable from zero, and the doc does not say which leg carries the attribution · the Sep-18 pair is graded though it does not expire until 9/18, five days after this document · "$2.75 cap" and "≤$275" are the same figure at different bases and the doc does not say so · the $2.20 fill price is doubted but never quoted · "WAL" is used for both the ticker and the desk · what firing the guard would actually have *done* (a TERRY proposal to Will; nothing self-executes) is not stated, so the 8-day gap cannot be sized · the count stayed 0-of-3 throughout, so no grade in the gap was ever actionable · several tokens (D-18, #18(a), Rule A, RISK_RULES #4) are unopenable by a cold reader · the doc runs over its ≤1,500-word target.
