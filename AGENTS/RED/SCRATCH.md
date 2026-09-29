# RED SCRATCH — canonical session handoff
**Written:** 2026-09-29 10:3x ET [`date` 10:28 EDT at the ledger write; session start 10:24] · **Session:** S48 (PROME prome-82 Tier-1 spawn, WQ-184 due-row driver; DOCKET L525 FT-01 ruling + whole-inbox L0 drain) · **Supersedes:** S47 (2026-09-25), which is in git history (`git log -p -- AGENTS/RED/SCRATCH.md`).

---

## CHANGES SINCE (what moved while RED was dark, 9/25 → 9/29)

- **HY OAS widened 29bp in three sessions:** 273 [9/23] → 280.0 [9/24] → 293 [9/25] → **302 [9/28]**. BB 159 → 183 · CCC 1,093 → 1,146 · IG 77 → 83. B was 300 [9/25] and had not posted for 9/28 at 10:24 ET. HY yield 8.03%.
- **WALTER SIG-W-20260925-011** (ACTION RED): 280.0 is at the line, so this was FT-01 exit day 1 of 3. **LIQUID corrected the arbiter state**: X1 is CLOSED and DON'T-SIZE is DECIDED (BROCK KB-BRK-219, 8/28), so a 280 touch returns that answer. LIQUID's watcher text fix is owed on their side.
- **SAM 9/29 (`0b5524b8d`):** there is no driver-attribution read before 12/30, so CH-012 closes NO-VERDICT at year-end under the pre-written rule. MOF 30Y was 4.122 on 9/28.
- **PROME 9/27:** the board_log gap packet for -011. **PROME 9/25:** WQ-295 asks for a cadence declaration and watch terms.

## WHAT I DID

1. **RED-FT-01 EXIT EXECUTED on the letter.** The exit rule is `>=280 s=3` on FRED observation dates, and the prints were 280.0/293/302, so the count is 3 of 3 at the 9/28 obs. The pre-registered **CONF +2 was taken: HOLD 68 → 70.** Net-bear stays at 58. The round trip is **CLOSED**. Per S36d, FT-01 fires now move nothing and the ±2 sits on FT-12. Registry `exit_source` / `action_magnitude` / `state`, FT-12 `state_detail`, the scan view regenerated, STATUS, CHANGELOG, OUTBOX -044, NEXUS_BRIEF vS48 · ML-RED-267.
2. **Disagreements recorded after applying the letter:** ① The tie atom: 9/24 = 280.0 counts under canon `>=`. WL-03 `>` and LIQUID `>280` read 2 of 3. ② Composition is broad-tier: BB+B = 82% of 9/23→9/25. The BB/CHTR single-sector question is UNKNOWN. IG lagged.
3. **ML-RED-268: WL-03 op drift.** The display mirror has `>` where canon has `>=`, so boot.py printed "sustain NOT yet met" for a completed exit. It is recorded but not conformed in-session.
4. **TRIGGER_OUTCOMES: two DUE FT-01 rows graded.** 6/15 is CORRECT (+2.8%), graded 20 days late, a miss RED owns. 7/02 is WRONG (−5.4%). Apparatus data only.
5. **FT-07 / FT-12 read, no state change:** CCC 1,146 keeps FT-07 FIRING-BANKED. FT-12 is 42bp away and moving away.
6. **Inbox 3 + 1 → 0 + 0**, with 4 `board_log` rows. Boot §⑤ is now OK. CADENCE is declared EVENT-DRIVEN (PROME/inbox packet).

## NEXT SESSION (dated, priority-ordered)

1. 🔴 **2026-09-30 (the 9/29 obs publishes): confirm the exit's robustness.** Any 9/29 HY obs >280 completes even the strict count, which retires the tie-atom caveat. A 9/29 obs <280 does NOT reverse the exit. A reversal needs a fresh FT-01 fire (<280 s=3), which by S36d now moves nothing.
2. 🔴 **2026-10-01: apply the CH-009 rule mechanically** on the MOF 9/30 30Y close. Any close ≥4.300 on 9/25–9/30 ⇒ NO-VERDICT. All closes <4.300 with no ≥20bp session ⇒ DISMISSED.
3. 🟠 **FT-02 (>320 s=3) is the nearest line, 18bp away, and HY is moving toward it.** Pre-read it before it prints: NET-BEAR +3 / CONF +2 on fire, and the outcome spec is committed. Count evidence types, not desks.
4. 🟠 **WL-03 op conformance (`>` → `>=`, display only), with a reader.** It is bear-direction-relevant on the display, so it is not self-certified. The same class sweep runs across all WATCHLINES rows that mirror a registry exit leg (ML-RED-268).
5. 🟠 **Build the pre-append size gate for `board_log.tsv`** (n=3, still unbuilt). It is at 26,475 B, **81% of the 32,550 B cap**.
6. 🟠 **L247 v0.6 recheck when PROME lands the edit** (acceptance conditions are pre-written in the 9/25 report §4).
7. 🟠 **The DUE-scan does not read TRIGGER_OUTCOMES `resolve_after`.** The 6/15 row sat 20 days. Wire it into `boot.py` §④ (boot 9d says to disposition these at W2, but nothing surfaces them).
8. 🟠 CARL revision ledger full adversarial read (135 events). The CRL-08 ruling goes to DAEDALUS.
9. 🟠 FT-03/04 evaluator: re-point from `BZ=F` to a dated contract (L429).
10. 🟠 Counter-signal re-pull + hypothesis-weight re-derivation (weights are S29 8/12; confidence is now 70 on a mechanical move over S41's 68). This needs its own session.
11. 🟡 FT-11 F2 cut (BOND's quartile question) at the next spec review, never in-window · FT-08 basis reconciliation with WALTER · 5 ACTIVE challenge rows (CHG-027 first) · VX-RED-009 → CARL · KB 18 past `Stale_By` · registry arithmetic-path scan.
12. 🟡 FT-01 8/05 outcome row resolves ~10/29.

## OPEN THREADS

- **A mirror that disagrees with canon only on the tie atom is invisible until a print lands on the line.** WL-03 carried `>` for 3½ months beside a canon `>=`, and it cost nothing until 9/24 printed 280.0 exactly. The same shape as FT-07's float tie (ML-RED-241). Sweep display rows against canon exit legs **at the atom**, not by eye.
- **The exit is not a confirm.** A reader who sees "FT-01 fired +2 on a 302 print" and FT-02 later firing at 320 must not bank the same widening twice. The +2 here repays the 8/7 −2; FT-02's +3/+2 is a new state.
- **The BB/CHTR question** (LIQUID) is the live composition unknown. If a single-sector BB move carried the 9/25 day, the tie-atom day plus a sector day make a thinner exit than 3 of 3 suggests. It does not change the count, but it is the first thing to test if FT-02 approaches.

## PENDING WILL-DECISIONS

**None.** The only move was the pre-registered FT-01 exit +2 (mechanical, CONF only). No threshold, spec or sustain count was changed; $0. Sizing and X1 are Will's/LIQUID's, and both are untouched.

## GIT STATE

Committed path-scoped inside `AGENTS/RED/`, plus the completion memo and the cadence packet in `PROME/inbox/`. **No pull:** the tree held other desks' uncommitted work at boot (CRUISE, PROME), so root "Before pulling" step 2 applies. Push via `scripts/safe-push.sh`; the receipt is in the memo/SendMessage.
