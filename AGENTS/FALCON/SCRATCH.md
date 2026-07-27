# FALCON SCRATCH — 2026-07-27 Mon **session 2** (post-crash re-boot; FAL-03 REGISTERED)

**Purpose:** Ephemeral session handoff — read at boot (step 2), rewritten at closeout (step 13). Durable learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Scenario **B 10 / C 40 / D 50** · Convergence **40/50** · Kinetic **US-Iran PAUSED (3rd night)** / **Saudi-Houthi 🔴 ESCALATING** · **FAL-03 OPEN @ 58% (Jul 27 – Aug 17)** · Scoreboard **1C / 1F / 1 OPEN**. **Marks UNCHANGED from session 1 — nothing in the theater moved.**

## CHANGES SINCE LAST SESSION (7/27 s1 → 7/27 s2, ~90 min)
- **✅ CRASH COST NOTHING.** Session 1 completed its full closeout and committed at `184e4e21` (15:07-15:08 ET), then pushed. `git fetch` confirms local ≡ origin **in both directions**. Working tree clean for `AGENTS/FALCON/`. Nothing lost, nothing to replay.
- **🎯 FAL-03 REGISTERED** — the FAL-01 successor, closing the empty-ledger gap that was s1's top standing obligation. **58%**, Jul 27 – Aug 17. All three owed conditions discharged; derivation in the new `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md`.
- **📊 NEW LOAD-BEARING BASE RATE (KB-FALCON-050), and it is reproducible.** Classifying `STRIKES.tsv`'s Status column splits the war cleanly: **ACUTE Feb 28–Apr 9 = 10 operational-class events in ~41d**; **PREMIUM Apr 10–Jul 27 = ZERO in 109 days** *despite five logged strikes (VTTI 5/4, KOC 7/12, Mangaf 7/18, Jazan 7/25, Abqaiq 7/27)*. **This is the premium-vs-supply-loss thesis in quantified form** — the war has reached the asset class routinely for 15 weeks without taking barrels off the market.
- **🚨 NINTH FALSE-FIRE CAUGHT (KB-FALCON-051): "Bapco declares FM as Iran sets Bahrain's only refinery ablaze" = 9 MARCH 2026**, not current. Caught *while searching for a current Jazan FM* — precisely where a stale FM reads as fresh, and **with FAL-03 live it would false-fire route (a).**
- **Two live re-checks, both negative (i.e. state confirmed unchanged):** Jazan damage assessment **still absent at 3 days**; US-Iran pause **confirmed holding a third night**, Oman channel only (Iran MFA still denies bilateral talks).
- **HAW-10 reconciliation done:** STATUS's D-tell #1 and the Gulf-production/bypass-infra vector threshold now **REFERENCE** FAL-03's registered text instead of loosely restating it. A restatement in either place would have recreated the exact HAW-10 wedge.
- **Boot scripts all rc 0, all unchanged:** bypass **HOLDING** (69,793 vs 16,224 floor, thru 7/17) · Hormuz newest **7/19 = 15/88**, no new prints · kharg 0 = **UNINFORMATIVE** (correctly not read as a strand) · baghdad quiet · ledger-staleness clean · STRIKES swept-complete through 7/27.

## WHAT I DID THIS SESSION
- Full boot; verified crash recovery at the git layer before touching anything.
- **Derived** FAL-03's 58% rather than asserting it — regime-split base rate + two-leg decomposition (leg A Jazan retro-converts 25%; leg B new qualifying event 22% → P(fire) 41.5%).
- **Disclosed the hindsight-fitting risk head-on** and verified the defense at the primary: HAWK's operational-threshold rec is dated **7/25**, two days *before* FAL-01 resolved, and explicitly scoped *"for FAL-01's successor, not FAL-01 itself."* Pre-registered, not retro-fitted.
- Wrote the resolvability guard so **operator silence cannot auto-confirm** the row.
- Wrote scaffold + 3 KB rows (049-051); updated STATUS, NEXUS_BRIEF, PREDICTIONS header; ran the state-token sweep.

## NEXT SESSION (dated, future-verifiable)
1. **🔴 JAZAN DAMAGE ASSESSMENT — now a scored FAL-03 leg, not just a watch item.** Any Aramco/Saudi statement, bpd figure, or FM. **Note the guard:** if it is *still* unknown at 8/17 AND no independent route resolved it, FAL-03 caps at **PARTIALLY** — I do **not** get a CONFIRMED from silence. Chase an *affirmative* all-clear as hard as a positive disclosure.
2. **GATE-FALCON-001 leg-2** — **TANKER-SPECIFIC** Bab transits, ≥2 print-days sub-~8/day. PortWatch surfaces post-strike aggregates **~7/29-8/1** — that is this week. Total-vessel data (34→15, −56%) is in hand but is NOT my registered metric.
3. **GATE-FALCON-001 leg-3** — post-7/25 **Yanbu loadings** (baseline ~4.7M bpd). Did not exist as of 7/27; resolves leg-3 either way.
4. **Does the pause hold a 4th+ night?** B's flip-up needs **framework + a DATE** (only the halt leg is met). Strikes resuming → D back toward 65.
5. **P/R split implementation** — publish P and R scalars alongside the composite; send PROME the implementation note so NEXUS's route-count line + BRENT's grading wire consistently. **Still open.**
6. **Named war-risk surface owed** — a KB row has no staleness affordance (why ~5% went 12 days unchecked). HAWK's structural point, conceded. **Still open.**
7. **Yanbu second-salvo watch** — the test the 7/25 intercept predicts is a *larger* attempt; its defence is consumable.
8. **Outbox memo to PROME on FAL-03** — not written this session. s1's memo already flagged the successor as owed; a short follow-up closing it out is the clean loop.

## OPEN THREADS / WATCHES
- 🔴 **Jazan damage assessment absent 3 days** — now FAL-03's leg A; premium-vs-supply-loss hinges on it
- 🔴 **Two counter-moving wars in one file** — composite convergence masks the rotation until P/R ships
- 🟠 **Pause is munitions-constrained, not intent** (Cooper/Caine) — step-change risk rather than resumed tempo
- 🟠 **Yanbu** = 92% of Saudi seaborne crude, fired on once, saved by a consumable interceptor
- 🟠 **Iraq/PMF discriminator firing on the ACTOR axis** (Abqaiq 7/27) — watch for a *damaging* follow-on; it is now FAL-03's axis (d)
- 🟠 **WC Saudi war-risk 0.1%** — the transit→origin falsifier; cheapest early warning of P→R conversion
- 🟠 bypass HOLDING (69.8k t/d vs 16.2k floor, thru 7/17) · Hormuz 15/88 thru 7/19 · WSJ hull double-count STILL unresolved
- ✅ **FAL-01 CLOSED (FAILED)** · ✅ **FAL-03 OPEN** · ✅ **$85×3 closed 7/21** · ✅ **GATE-TERRY-006** live 7/18, kharg veto shows flow continuing

## PREDICTIONS DUE / DECISIONS PENDING
- **FAL-03 OPEN, window closes 2026-08-17.** Nothing due before then, but **leg A can resolve it at any moment** — a Jazan disclosure is the live trigger. Re-read the resolvability guard before resolving; **silence is not a CONFIRMED.**
- **Will decision PENDING (soft, carried from s1):** the re-mark **B 10 / C 40 / D 50 + convergence 40/50** is applied as my own call. Nothing downstream committed on it; cleanly revertible if Will prefers marks gated as on 7/23.
- **FAL-03 itself was registered on my own authority** (standing prediction-registration lane, not a Will gate). Confidence is mine and auditable in the scaffold — challengeable on the derivation, not just the number.

## MAIL STATE (one line per surface)
- **Inbox (root): EMPTY.** **WALTER lane: EMPTY.** Both drained in s1 and nothing new arrived.
- **Outbox:** s1's `2026-07-27_to-PROME_fal01-FAILED-jazan-and-remark-b10-c40-d50.md` (🔴, cc HAWK/BRENT/RED) — **left as a delivered snapshot**, correctly still reading "0 OPEN" as of its writing. FAL-03 follow-up memo owed (NEXT item 8).

## PENDING PUSH / GIT
- Committing pathspec `AGENTS/FALCON/` only (STATUS, SCRATCH, NEXUS_BRIEF, PREDICTIONS.tsv, KB.tsv, thesis/FAL-01_REREGISTRATION_SCAFFOLD.md). Foreign dirty paths present (WALTER/BOARD/memory/auto, PROME batch-3 dispatches) — normal concurrent-agent state, **not mine**; strict own-dir pathspec, never `git add -A`.
