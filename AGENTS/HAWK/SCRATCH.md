# HAWK SCRATCH — 2026-07-28 (Tue, 3-day pass: CPC resolution + full mail lane + both derived surfaces)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 14). Disposable. Persistent learnings → `MEMORY.md` / `LESSONS.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CHANGES SINCE LAST SESSION (7/25 → 7/28)

- **FAL-01 RESOLVED FAILED 7/27** on Jazan — FALCON's first failed row, marked clean rather than rescued. They adopted **my** class-vs-direction basis over WALTER's. Scenario re-marked **B 10 / C 40 / D 50**, convergence 42→40.
- **US–Iran campaign PAUSED 7/24** after 13 nights, holding 3+ — cause is a **munitions / exhausted-target-list constraint** (Adm. Cooper, Gen. Caine), *not* diplomacy. Durable short-horizon, silent on intent.
- **Brent round-tripped $100.50 → $87.73 (−9.35% on 7/27)** with Jazan still burning. My 7/25 reversibility caveat, tested on its first case.
- **CPC RESUMED 7/27** — SPMs intact, no repair, no FM, Tengizchevroil-chartered tankers back.
- **Libya opened 7/28** (Mellitah, El Feel stopped) · **Ras Laffan LNG FM extended into month 4, now Asian buyers too** · **Golden Leo sunk 7/26** · **Tyumen refinery hit 7/25, ~2,000 km deep**.
- **FALCON adopted my war-risk correction in full** and named a war-risk surface — closes my 🟠 PROME nudge.

## WHAT I DID THIS SESSION

1. **Resolved my registered CPC natural experiment** against external primaries (Astana Times 7/27 fetched directly). **Willingness-bounded, cleanly** — owner return, SPMs intact, no FM, resumption conditioned on *"ongoing assessments of the security situation."* The returning charterer was **Tengizchevroil**, i.e. the same Chevron whose refusal defined the willingness leg on 7/23.
2. **Derived the session's headline finding: MAGNITUDE NO LONGER DISCRIMINATES.** ~440 kbpd Kazakh offline for a week (−21% national; Tengiz −56%) with **zero capacity destroyed**, reversed on a decision. ⇒ the test is **"was capacity destroyed?"**, not barrel count. `KB-HAWK-236`, → BRENT.
3. **Generalised the thesis off Libya.** A **third** supply-removal instrument — non-kinetic *and* non-insurance, output removed by domestic political leverage. Same class as CPC: reversible, non-destructive. **⇒ "willingness" was slightly the wrong name for my own thesis** — it names an actor class for a property that is really about the asset. `KB-HAWK-240/241`.
4. **Graded HAW-18 leg-by-leg — all five UNFIRED** — and **found + declared a four-instance spec defect in my own row** (below).
5. **Corrected my own load-bearing phrase fleet-wide:** "zero confirmed barrels offline" → **"zero confirmed CRUDE barrels offline."** The war's one confirmed, FM-backed, four-month supply loss is **Ras Laffan LNG** (~12.8 Mtpa, ~17% of Qatar's exports, FM since 3/24, lengthening). `KB-HAWK-242`.
6. **Cleared the entire mail lane** — 14 items (10 WALTER 7/27 + 3 WALTER 7/28 that landed mid-session + 1 FALCON) dispositioned into `board_log.tsv` and `git mv`'d to `processed/`. **Both lanes CLEAR.**
7. **Refuted FALCON's legacy-scripts premise** (boot.py's own line 4 is a freeze banner; my boot never invokes it; they read the freeze-commit mtime as "so live") — **and accepted their option 3**, which found a real hole in my own scope.
8. **Regenerated both derived surfaces** (`CROSS_WAR_SUMMARY.md`, `CROSS_THEATER_WAR_RISK.md`) and refined `FLOW-HAWK-19`. 8 KB rows (235-242).
9. **Routed 3 packets:** OSPREY (CPC state superseded + 2 staleness flags) · BRENT (magnitude/destroyed-capacity test) · FALCON (premise refuted + option 3 accepted).

## ⚠️ SELF-CORRECTIONS BANKED THIS SESSION (3)

1. **HAW-18's spec is defective in four places, all one root cause: I wrote FALCON's legs OPERATIONALLY and everything else as EXEMPLARS.** (i) leg (b) "vessel sunk" is bracketed `[FALCON theater]` — a **crude tanker** sunk in the Black Sea would read no-fire while the thesis died; what saved it on Golden Leo was the **cargo class** (grain), not the bracket. (ii) The OSPREY legs are damage/FM proxies with **no direct output test**, so −440 kbpd is invisible. (iii) **Scope, not wording:** the row says "NEITHER theater" as if the world had two — **Libya is neither**, so a 500-900 kb/d Libyan loss cannot fire my flagship row at all, and I am the *cross-cutting* agent. (iv) **Molecule:** oil-only, so Ras Laffan sits outside it. **Not amended** (evidence in-window). **The non-obvious half:** naively adding an output test would have fired HAW-18 FAILED on CPC — killing the thesis on evidence that *confirms* it. The successor leg must be **output offline CONDITIONED ON DESTROYED CAPACITY**, theater-agnostic and molecule-explicit.
2. **"Zero confirmed barrels offline" was true-but-misleading and I'd been broadcasting it.** BRENT/HENRY/LIQUID/SAM/FALCON all consume that phrase. WALTER caught the molecule gap; I corrected the phrase at source rather than annotating it.
3. **My derived surface understated the same sibling twice running.** `CROSS_WAR_SUMMARY` reported FALCON at 29 rows / swept 7/12 and flagged "worth a nudge" — they had already advanced to 7/27. Second instance of the 7/25 lesson, sign flipped: **OSPREY is now the stale side.** Lesson extended with the corollary: never write a staleness judgement about a sibling as a *standing* claim — the sibling is fixing it while you type.

## NEXT SESSION (dated, future-verifiable)

1. **🔴 FIRST ITEM — the content-triggered FLOW re-sweep I deliberately did NOT do.** `FLOW-HAWK-13` (Hormuz → Taiwan LNG) and `FLOW-HAWK-16` (Ras Laffan → helium → semiconductor rationing) are **MUTED (dormant-armed)** on **[STALE Apr-20 figures]**, and both are premised on Ras Laffan being offline — **which it still is, with the FM lengthening into month four.** Premise alive and strengthening; downstream figures 3 months stale. **This is the exact LESSONS-#3 shape (clock says 8/4, content says now).** Needs a full external re-derivation of the helium-buffer and Taiwan-power chains — a session of its own. **Do not carry these rows again without doing it.**
2. **Libya escalation watch — the tell is NOC terminal-level force majeure** at Es Sider / Ras Lanuf / Zueitina / Brega / Hariga. That is the step that converts 85 kb/d into 500-900 kb/d and the step both prior episodes took. Check ~daily while live; base rate says days-to-weeks resolution.
3. **CPC re-halt risk** — the resumption is explicitly conditioned on *"ongoing assessments of the security situation."* Same willingness variable, not a repaired asset. A second strike reopens it instantly.
4. **MRPL clause adoption test → ~2026-08-24.** ≥2 further Indian refiners (IOC/BPCL/HPCL/Reliance) = durable re-contracting and willingness has gone structural; zero = one cautious buyer. **Currently 1, checked 7/27, explicit negative recorded.**
5. **Refresh `CROSS_THEATER_WAR_RISK.md` (step 13a)** — re-stamp even on a no-change pass. **OSPREY's Black Sea leg is 7/21; formal 10d bar breaches 7/31** and it is content-stale already (no post-CPC-resumption print). Nudge sent 7/28; escalate if unmoved.
6. **Sibling predictions:** OSP-02 → Jul 31 · OSP-01 → Aug 1 · OSP-03 → Aug 2 · FAL-03 → Aug 17. Watched, not mine to resolve.
7. **VX dormant-book 45-day clock → 2026-08-04** (TRADE-02, SULPHUR-01, FININFRA-01, IRAQ-01).
8. **Taiwan: corroborate the 7/22 helicopter median-line crossing** (single-source, Taipei Times). Corroboration or any median-line action touching Strait shipping flips the hold-dormant recommendation.

## OPEN THREADS / WATCHES

- 🔴 **HAW-18** → Sep 1 (55%), all five legs unfired. **⚠️ Consumers should treat a CONFIRMED as weaker evidence than 55% implies** — three of the four defects make it easier to confirm than the thesis deserves. Stated before resolution so it can't be claimed retroactively.
- 🔴 **FLOW-13/16 re-sweep** (item 1) — the one thing I knowingly left undone.
- 🟠 **Libya → export terminals** · 🟠 **CPC re-halt** · 🟠 **OSPREY 4 days dark**, canonical STATUS carrying a superseded CPC state
- 🟠 **West Coast Saudi 0.1%** — still the cheapest falsifier I own. If it rises materially, risk migrated transit → origin and the whole decomposition dies. ⚠️ MRPL barring the *bypass* as well as Hormuz is early evidence buyers are widening the geography of avoidance.
- 🟡 **Shadow-fleet ENFORCEMENT lane is unbuilt** — mine per domain scope, currently a dead instrument. Highest-value HAWK build candidate; FALCON would consume it. **Not started.**
- 🟡 **RED steelman** *("is 'willingness' just the premium channel relabelled?")* — **half answered** by MRPL (a price unwinds; a contract clause persists). Remaining half: does the clause survive premium normalisation?
- 🟡 **Nov 10 2026** — US-China truce expiry.
- ✅ Closed: FALCON war-risk surface nudge · Hormuz stale-carry catch #1 · CPC natural experiment · FAL-01/Mangaf class question (row resolved FAILED).

## PREDICTIONS DUE / DECISIONS PENDING

- **HAW-18 OPEN** → Sep 1. Nothing due at HAWK before then.
- **Nothing pending at Will.** No trade construction — HAWK holds no book.
- **Nothing pending at PROME** — the FALCON war-risk-surface nudge closed itself (FALCON built one).

## MAIL STATE (one line per surface)

- **Inbox (root): CLEAR** — 1 FALCON packet dispositioned + `git mv`'d.
- **WALTER lane: CLEAR** — 13 dispositioned + moved (10 from 7/27, **3 that landed mid-session on 7/28**). WALTER was live throughout; expect more on next boot.
- **Outbox:** unchanged (8 pre-split packets, PROME-scanned). This session's 3 packets were **direct-dropped** to OSPREY/BRENT/FALCON inboxes and committed per carve-out ①.

## PENDING PUSH / GIT

- See the closeout commit. **Not mine, flagged not touched:** WALTER was working live in this tree throughout the session (BOARD signal written 09:41, staged DEWEY inbox renames) — left alone.
