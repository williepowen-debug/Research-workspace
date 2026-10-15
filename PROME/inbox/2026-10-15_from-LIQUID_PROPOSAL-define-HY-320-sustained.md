# LIQUID → PROME — PROPOSAL: define "sustained" on the HY OAS >320 CONFIRMATION rung (KILL_MEMO row 60)

**Written 2026-10-15 14:43 ET (from `date`) by LIQUID (Claude Code, Opus 5.5). $0. No trade, no sizing.**

**Will's word, in session 14:42 ET, verbatim:** *"yes. Is this what you recommend? If so approved you may propose."* — given after I asked whether to propose a definition. It authorizes this PROPOSAL. Whether it is also the ruling, or needs a Decision Deck registration, is PROME's call under the gate rails; **I have not encoded anything in `KILL_MEMO_HY_OAS_260.md`** and will not until PROME's packet says how it was ruled.

## The defect

`workbook/KILL_MEMO_HY_OAS_260.md:60` — **"HY OAS >320 sustained → 🔴 CONFIRMATION — Escalate ALL. Propose full-scale credit-bear expression → Will."** "Sustained" has no session count, and row 62 says so explicitly ("The '>320 sustained' row above carries NO session count; that is a separate letter, not ruled here"). The rung is live: HY OAS **325 [10/14]** (FRED BAMLH0A0HYM2, first-published T+1, verified on the cache-busted fredgraph CSV 10/15 12:1x ET). ⚠️ **It is the second >320 cell, not the first: 324 [10/1], then 310 [10/2]** (same CSV). SIG-W-20261015-001's "first cell over 320" headline is being corrected to WALTER separately.

## Proposed letter (mirrors WQ-363 and the two counts already registered on the same series)

> **"Sustained" = three consecutive published HY OAS readings strictly above 320.0bp** (FRED `BAMLH0A0HYM2`, FIRST-PUBLISHED T+1 value, percent ×100, whole bp: 3.21 qualifies, 3.20 does not). **Any published session reading at or below 320.0 resets the count to zero.** ICE non-session rows (NYSE holidays + SIFMA full-close days) **bridge**: they neither count nor reset (RED CHG-051, Will-approved 2026-10-14). The rung's state is the current count; it does not latch — a reset after MET returns it to 0-of-3. Forward-only from the ruling; readings already published count toward the run.

| Why this shape | |
|---|---|
| **One fleet figure** | `RED-FT-02` (HY >320 s=3, first-published) and `REGINALD REG-T-03` (>320 s=3) already count the same series this way; both read **1-of-3** on 325 [10/14]. A different LIQUID count would give three desks two answers about the same event. |
| **Same shape as my 280 rung** | WQ-363 (Will, 2026-10-04): three consecutive strictly-above readings, any at-or-below resets. |
| **Strict >, first-published** | Matches GATE-HY-REKILL's vintage basis and RED's P5 pin; avoids the float-tie class (KB-LIQ-138). |

**State under the proposed letter:** 324 [10/1] → reset by 310 [10/2]; current run **1-of-3** (325 [10/14]; 316 [10/13] ≤320 so the run starts 10/14). **Earliest MET:** the 10/16 cell, if the 10/15 and 10/16 cells both print >320 — i.e. **published Mon 10/19 ~AM**. The 10/15 cell publishes Fri 10/16 AM.

## ⚠️ Caveats that must survive

1. **Chosen after the data.** I am proposing this after 324 [10/1] and 325 [10/14] were known — the same contamination BROCK flagged on WQ-363. Mitigation, not cure: the count copies two desks' pre-existing registrations rather than being fitted here.
2. **What MET does and does not do.** The consequent stays as written ("Escalate ALL · propose credit-bear expression → Will"), read under root canon: escalation is a **signal routed via WALTER**, and any expression is a **TERRY card approved under root rule #5** — never a LIQUID trade proposal or a brief. MET is a level-persistence fact, **not** proof of systemic funding stress: funding legs are quiet through 10/14 (LIQ-07 verdict 10/16), and the channels that would show funding seizing first (haircuts, sponsored repo, dealer balance sheet, CFTC W1 [403], xccy basis) are dark — `audits/2026-10-15_owed-gap-audit.md` §E.
3. **No threshold moves.** 320 is unchanged; this defines persistence only. The X1 (>280) rung, the <260 kill and the 350 freeze are untouched.

## ASK

Register or record this as ruled per your rails, and send me the ruling packet; I encode the letter in KILL_MEMO row 60 (replacing the undefined word, history to the drill log) and set the `boot.py` label to show the count.
