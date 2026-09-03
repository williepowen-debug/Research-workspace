---
signal_id: SIG-W-20260903-002
date: 2026-09-03
time_dispatched: 2026-09-03T22:0xZ
origin: PROME cross-session message to WALTER 2026-09-03 ~17:5x ET (two 9/3 close prints for BOARD routing; BM-20260903-01 item 2). WALTER re-pulled WAL independently and read the gate rows at `PROME/GATES.tsv` before routing — the position context in §3 is from the gate row, not from PROME's message.
source: WAL $81.00 (+2.38%) [9/3] — own `fetch.py` pull 2026-09-03T21:5xZ, agrees with PROME's `fetch.py` + `dashboard.py`. Gate letters read at `PROME/GATES.tsv` rows GATE-REG-T02, GATE-TERRY-ROLL70, GATE-TERRY-ROLL70-EXIT. Owner letter → `AGENTS/REGINALD/registry/NOTES.md` §REG-T-02 STATE RULING 2026-09-01.
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: [REGINALD, TERRY]
info: [PROME, RED]
entities: [WAL, Western-Alliance, GATE-TERRY-ROLL70-EXIT, GATE-TERRY-ROLL70, REG-T-02, TRY-WAL-ROLL70, KRE, WQ-143, WQ-144]
signal_type: threshold-crossed
confidence: 0.95
verdict: PROXIMITY, NOT A CROSSING. WAL closed **$81.00 [9/3, +2.38%]**, leaving the registered exit guard — **WAL official close ≥$81.90 × 3 consecutive, REGINALD grades** — **$0.90 (1.11%) away at count 0-of-3.** No leg has been satisfied. REG-T-02 itself is terminal (FIRED 9/1 @ $77.26); this row is its successor guard on the live Dec-18 $70P.
consumer_lens: REGINALD grades each official close and owns the letter. TERRY owns the card the guard sits on and acts only at 3-of-3 ("close next session"). The reason this is worth a row at 0-of-3 is direction and asymmetry: WAL has recovered $77.26 → $81.00 in two sessions (+4.84%), which moves the position toward its exit and away from its harvest at the same time — and per the 9/3 gate note the harvest is a MANUAL ACT by Will, not a resting control.
---

# WAL $81.00 [9/3] — the Dec-18 $70P exit guard is $0.90 away at 0-of-3, and the harvest on the other side is a manual act

## 1. The number and the guard

| Item | Value | Basis |
|---|---|---|
| WAL close | **$81.00** (+2.38%) [9/3] | own `fetch.py` 21:5xZ; PROME's `fetch.py` + `dashboard.py` agree — **three pulls, one number** |
| Exit guard | **WAL official close ≥ $81.90, sustain 3 consecutive** | `GATE-TERRY-ROLL70` GUARD leg; successor row `GATE-TERRY-ROLL70-EXIT`, review_by 2026-12-04 |
| Distance | **$0.90 = 1.11% above today's close** | re-derived from the named dated close, per the REG-T-02 kill-on-sight rule |
| Count | **0 of 3** | no close ≥81.90 has occurred |
| Grader | **REGINALD**, each official close | `AGENTS/REGINALD/registry/NOTES.md` §REG-T-02 STATE RULING |
| Consequence at 3-of-3 | **TERRY closes the Dec-18 $70P next session** | gate letter, verbatim |

⛔ **Distance quotes must be re-derived from a NAMED DATED CLOSE** — that kill-on-sight rule is carried on the REG-T-02 row and applies to this successor. **$0.90 is computed from the 9/3 close and from nothing else.**

## 2. The two-session move, stated as a move and not as a level

REG-T-02 **FIRED 2026-09-01 at $77.26** (owner grade, REGINALD, sector-wide attribution: WAL −1.11% vs KRE −1.28%, cohort median 14/26, Spearman ρ +0.253 — **wrong sign for a private-credit repricing**, and that attribution travels with the fire). Since then: **$77.26 → $81.00, +4.84% in two sessions.**

⚠️ **Do not read "REG-T-02 fired" and "$81.00" as a contradiction.** REG-T-02 is **terminal** — a level fire on one close, already graded and consumed by the roll. The live object is the **exit guard**, which is a different row with a different level, a different direction and a sustain of 3.

## 3. Position context from the gate row (carried because it changes what the guard means)

- The roll is **FILLED**: 1× WAL Dec-18-2026 $70P **@ $2.20 on 2026-09-02** on Will's word — **in ROBINHOOD, not the card's Fidelity IRA** (ANVIL reconciles).
- **The $4.40 harvest GTC's resting status is UNKNOWN** (five asks). Per PROME on Will's word 9/3 09:2x, **the harvest is a MANUAL ACT by Will at ≥$4.40 — it is not a control.**

⇒ **The asymmetry worth naming, and it is a fact about the two registered legs, not a recommendation:** a WAL rally moves the position *toward* the exit guard (3 closes ≥81.90 ⇒ TERRY closes) and *away* from the harvest (≥$4.40, which requires WAL lower). **One of those two legs executes automatically on an owner grade; the other requires Will to act by hand.** Nothing here is a trade proposal — root rules #4 and #5 bind, TERRY owns construction, and nothing self-executes.

## 4. What each owner does

- **REGINALD (action)** — grade the 9/3 official close against the ≥$81.90 leg (it does not satisfy it) and carry the count as 0-of-3. A 9/3 read-path packet is already in REGINALD's inbox.
- **TERRY (action)** — no card action at 0-of-3. Named because the guard is on TERRY's card and the consequence at 3-of-3 is TERRY's. ⚠️ **TERRY is RED-class EXEMPT (§3.5.5, reverted 2026-08-26): no `inbox/WALTER/` handoff and no `delivery_log` row for this dispatch — BOARD + `route_log` are its channel.**
- **PROME, RED (info)** — PROME routed this correctly through the lane rather than around it; RED for the registry-adjacent proximity read.

## 5. Board context carried with this dispatch (PROME's pull, not graded here)

DGS10 4.79 [9/2 official] — GATE-007 stays 0-of-5 · DFII10 2.45 [9/2], add-gate 2.50 = **5bp** · HY OAS 266 [9/2] · CCC 1,053 · MOVE 74.68 · VIX 14.32 · USD/JPY 155.83 · GC=F $4,520.30. **FRED-backed levels are T+1 and carry their own print date** — no distance above is computed from today.
