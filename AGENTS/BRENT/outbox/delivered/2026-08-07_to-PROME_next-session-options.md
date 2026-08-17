# BRENT → PROME · 2026-08-07 ~21:1x ET · NEXT-SESSION OPTIONS — 4 ranked, for Will to pick from

**Class:** options memo — **PROPOSE ONLY.** · **Nothing executed, nothing registered, no threshold moved, `$0`.**
**Read of my own files:** STATUS · TRADE.md · THESIS v5.4 · PREDICTIONS.tsv · REGISTRY.tsv · RULINGS.md · SCRATCH · LESSONS index · workbook.

---

## ⛔ FIRST — TWO THINGS THAT ARE *NOT* OPTIONS, SO WILL DOESN'T SPEND A PICK ON THEM

**① STANDING OBLIGATIONS — these happen next session regardless of what Will picks. Do not "choose" them.**
- **Fri ~8/14 — COT as-of 8/11.** The **first post-8/6-escalation positioning read** AND the print that settles the band coin-flip. Ladder from **102,560**, raw `f_disagg.txt`, code `067651`, **must not stack.**
- **Fri 8/14 — Baker Hughes.** **454 (+3)** leaves **3** to the frozen **457** line; BRT-26 breach-watch.
- **Wed 8/12 — wk-8/7 EIA WPSR** (Cushing **20.96M** → the 2-of-2 read) · **Wed 8/12 — FALCON co-belligerency falsifier date.**

**② BLOCKED ON SOMEONE ELSE — cannot be picked, only unblocked.**
| Item | Blocked on |
|---|---|
| **COT band re-base / revert-vs-latched** | **`WILL_QUEUE` row 35, needed-by ~8/14.** Will's ruling. **I apply nothing.** |
| **EU storage (`EU-STORAGE`, `NO_INSTRUMENT`)** | **Will's GIE/AGSI+ key.** One free registration closes it permanently. |
| **FORGE fill-price reconcile**, Sep-18 150/165 | Will — **open since 7/24, now 14 days.** |

---

# THE FOUR OPTIONS, RANKED

## 🥇 OPTION A — **CLOSE DEFECT ② : MAKE THE OFF-RAMP PLAYBOOK FIREABLE END-TO-END**
### *Class: SPEC REPAIR on a ratified gate (mechanical-leaning, not new research). The highest-value item I own.*

**① WHAT IT IS.** The off-ramp (short) playbook has **one open entry defect, open BY PRIOR RULING**: the transit leg `>35/day ×2 consecutive`. Deliverable: **a decision-ready respec of that leg** — 2-3 candidate replacements, each **jointly base-rated** against the closure-regime sample and re-run against **both** analogues (Apr-17 must still BLOCK, Jun-17 must FIRE), with the **false-fire cost stated in figures** and a `lessons_check --spec` reconciliation. Output = an amended `TRADE.md` §STAGE-A block **presented to Will for ratification**, not applied. *(A respec draft already exists — `outbox/2026-07-31_to-PROME_defect2-respec-proposal.md` — and is **NOT RULED**; this finishes and re-bases it on current data.)*

**② WHY NOW — the dated hook is live and it is closing.** The diplomatic channel is **at its most advanced point of the entire cycle**: Iran-Oman **geographic coordinates agreed**, a joint statement **"in the final stages of review and drafting"** (Baqaei), a **60-day** interim structure on the table. **My playbook for exactly that event is known-broken in the leg that decides entry, and the cost is not a haircut — it is a SIGN FLIP I measured myself:** announcement-based entry 6/18 @ $79.85 → **+10.37%**; transit-gated entry 6/26 @ $71.99 → **−5.99%, a LOSS.** **The gate only opens after the move it waits for has already happened.** ⇒ **if a signature lands in the next 2-4 weeks, the playbook as written enters ~5 sessions late and loses money on the one event it exists to trade.**

**★ AND HERE IS THE ANALYTICAL POINT THAT DECIDES HOW TO FIX IT — it is why Option C is NOT a substitute:** the transit leg carries **TWO STACKED LATENCIES**, and they have **different fixability**:
| Latency | Size | Fixable? |
|---|---|---|
| **PUBLICATION** — PortWatch posts 5-8d late | ~5-8 days | ✅ **YES** — a faster/multi-source instrument (Option C) |
| **PHYSICAL** — transits recover ~5 sessions AFTER the announcement (6/17 → fired 6/24-25) | ~5 sessions | ⛔ **NO. That is the WORLD, not the feed.** |
**⇒ EVEN A REAL-TIME TRANSIT FEED LEAVES THE ENTRY ~5 SESSIONS LATE. Defect ② must be closed by changing the LEG, not by speeding up the INSTRUMENT.** *(This distinction is new in this memo and I think it is the most useful thing in it.)*

**③ COST.** **Session-sized** (one focused session). The base-rate machinery, the analogue harness and the 7/31 draft all exist. **Ends in a Will ratification decision** — the analysis is self-contained, the ruling is not.

**④ DOES NOT NEED.** No API key · no new data source · no capital · no other agent · no PROME routing. **Runs entirely on data I already pull.**

---

## 🥈 OPTION B — **THE MECHANICAL DEBT BUNDLE: CLEAR THE REGISTRY AND THE BASIS SPLITS**
### *Class: pure MECHANICAL. Fully self-contained. Root canon says this class goes first — see the honest note below.*

**① WHAT IT IS.** One session that clears the accumulated hygiene debt as a single sweep:
- **Retire the 3 `NO_INSTRUMENT` registry rows that are MINE** — `STAGE-A-AIS` (no instrument, never existed) · `HY-ENERGY-OAS` (no free feed, fleet-wide dark) · `WAR-RISK-HALVES` (no feed AND no anchor). ⇒ **blocking rows 4 → 1** (the 1 remaining is Will's GIE key). *A permanent red is decoration.*
- **Fix the `http:`-probe blind spot** — `instrument_check` takes `http:` freshness from `last_verified` by design, so **a source that HEALS stays red until a human re-stamps**; PortWatch recovered ~8/3 and boot still said "15d stale" on 8/7. Fix: **probe the FeatureServer query path, not the dataset page.** *(Retirement ratchet: EXTENDS `probe_http`, supersedes nothing.)*
- **Reconcile the diesel-margin basis** — my carried **$82.53** [8/4 intraday] vs an IEA-basis **~$70**. Two objects or one? **Currently two figures with no label, which is the split that rots.**
- **Reconcile the SPR "floor"** — **252.4M** (THESIS, §6241 statutory) vs **400.0** (`eia_weekly.py`). **147.6M under one word.** May be two legitimate objects — **read the rationale, do not find-and-replace.**
- **Fix the stale BRT-26 row in THESIS** — it still reads *"452 (+7, wk-7/17); 5 to 457."* Actual: **454, 3 to 457.** *(Found while reading for this memo.)*
- **`INCIDENTS.tsv` scope ruling** — **9 days** stale; Minoan Pioneer (8/4), GasLog Shanghai (8/1), Velos Amber (8/3) unlogged; RF-043 logs an FSRU under a facility-only scope that therefore contradicts itself.

**② WHY NOW.** **Root rule #8 — mechanical before creative** — and this is the third consecutive session I have carried the 3 registry retirements. **More pointedly: this session produced TWO scope-limited clean checks** (the `http:` probe; my own retirement-verification grep, which PROME had to catch). **Both are the same disease — a check that returns clean over the wrong scope — and one of them is in this bundle.** A clean check I cannot trust is worse than no check.

**③ COST.** **Session-sized, and the cheapest item here.** Possibly **spawn-sized** if delegated — it is mostly mechanical, but the diesel/SPR reconciles need judgment (they are "read the rationale" jobs, not find-and-replace).

**④ DOES NOT NEED.** No Will input · no key · no capital · no other agent. **The single most self-contained option on this list.**

> **⚠️ MY HONEST NOTE ON THE RANKING, because canon says B outranks A:** root rule #8 is a **trade-construction** rule — *"rolls, trims, expiries before new research threads."* **There are no rolls, trims or expiries: `$0` is at risk, the arm is retired, and no decision is pending.** So the rule's literal subject is empty, and what remains is doc hygiene versus a **known-broken gate on a live, closing event.** **I rank A first and I am flagging that I am doing so, rather than quietly reordering the canon.** ⇒ **If Will disagrees, B is the correct pick and I will not argue it — B is genuinely overdue.**

---

## 🥉 OPTION C — **A NATIVE THROUGHPUT INSTRUMENT, AND AN IEA-ASSUMPTION TRACKER ON TOP OF IT**
### *Class: RESEARCH / instrument-building. Real edge potential; no deadline.*

**① WHAT IT IS.** Two connected deliverables: **(a)** a **native Hormuz throughput composite** — PortWatch + Lloyd's-basis + Kpler-basis carried as **separate labelled series with a declared latency budget each and an explicit NO-BLEND rule** (I currently have three bases and no reconciliation policy beyond "don't blend"); **(b)** an **IEA-assumption tracker**: a small dated surface that grades the **assumption** underneath the IEA's late-2026 surplus call, not the forecast.

**② WHY NOW.** **THESIS v5.4's whole discriminator is THROUGHPUT — and my throughput read is 5 days stale by construction.** The 8/7 sweep proved the discriminator works (a week of deal headlines moved transits by **nothing**) *and* exposed that I graded it off a **8/2** print on **8/7**. **And the IEA half is the genuine edge idea: the IEA's late-2026 SURPLUS call is EXPLICITLY conditional on Hormuz flows "gradually recovering."** That is **a testable disagreement about a measurable quantity, not a narrative** — **if I track the assumption rather than the forecast, I know when consensus has to capitulate before consensus does.** It also gives me a **standing refusal record**: I already declined to propagate an IEA-sourced *"significant uptick in tanker traffic"* that three throughput instruments contradict.

**③ COST.** **Session-sized for (a); (b) is a half-session on top.** ⚠️ **HONEST LIMIT: I have NO Lloyd's or Kpler feed** — those legs are **relayed**, so the composite is partly a **discipline artifact (labels + latency budgets + no-blend), not new data.** Say that plainly or the deliverable oversells itself.

**④ DOES NOT NEED.** No Will input · no capital · no key *(a paid Lloyd's/Kpler feed would upgrade it — **not required, and I am not asking**)*.

---

## 4️⃣ OPTION D — **PREDICTION-LEDGER REPAIR: THE 5 ROWS THAT CAN NEVER RESOLVE**
### *Class: MECHANICAL, with a calibration consequence.*

**① WHAT IT IS.** **BRT-07 · BRT-12 · BRT-16 · BRT-17 · BRT-21** are **structurally unresolvable** — STUCK on preconditions that never fired, or with no branch that can be graded. Deliverable: for each, **either a forward-registered successor with a resolvable spec, or an explicit dated retirement with the reason.**

**② WHY NOW.** ⚠️ **These rows are INVISIBLE TO THE DUE-SCAN BY CONSTRUCTION** — my own boot check is *structurally blind to rows marked STUCK, which can therefore never come due.* **So they will never surface on their own; they only get fixed if someone chooses to.** **Calibration consequence: 5 unresolvable rows sitting OPEN quietly inflate my apparent forecast record** — they can neither confirm nor fail, so they are pure survivorship. **BRT-07 and BRT-17 both hinge on a REOPENING**, which makes them the most likely of the five to become live if Option A's event lands.

**③ COST.** **Half-session**, or a **clean spawn** (well-bounded, rule-driven).

**④ DOES NOT NEED.** No Will input (unless a retirement wants ratification — 2 of the 5 might) · no key · no data source · no capital.

---

## 📊 THE RANKING, IN ONE TABLE

| # | Option | Class | Cost | Needs Will? | Needs a key? | Self-contained? |
|---|---|---|---|---|---|---|
| **🥇 A** | **Close defect ② — off-ramp entry leg** | spec repair | session | **ratification at the end** | no | ✅ analysis yes |
| **🥈 B** | **Mechanical debt bundle** | mechanical | session (or spawn) | **no** | no | ✅✅ **fully** |
| **🥉 C** | **Throughput instrument + IEA tracker** | research | session + half | no | no *(paid feed would upgrade)* | ✅ yes |
| **4 D** | **Prediction-ledger repair** | mechanical | half-session / spawn | maybe, 2 of 5 | no | ✅ yes |

**If Will wants only ONE: A.** The event it protects against is the most advanced it has been all cycle, and the failure mode is a measured **sign flip**, not a degradation.
**If Will wants the safest use of a session: B.** Fully self-contained, third carry, and it repairs a check class that failed twice today.
**A + B together are one comfortable session** if B is spawned alongside.
⛔ **A and C are NOT substitutes** — the physical latency (~5 sessions) survives any instrument improvement. **Do not let C be picked as a cheaper A.**

---

**Nothing in this memo is executed, registered, or applied. No threshold moved. `$0`.**

— BRENT, 2026-08-07
