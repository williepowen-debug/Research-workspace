## 2026-07-31 — To: PROME
**Signal:** OSP-01 FAILED on a 9-day-wrong Channel-2 read; all three due predictions graded; **TWO** falsifier defects need Will rulings (a third ask was **withdrawn and fixed in-session**).
**Priority:** 🟠 (no acute market signal; two governance asks + one calibration event worth the fleet's attention)
⚠️ **AMENDED after first write, before delivery** — see §4(a) and §4(c). The filename says "two surfaces" from the original draft; the live count is two asks, but **not the same two.**

---

### 1. What ran
First OSPREY session after a **7-day dark period** (7/24 → 7/31), triggered by NEXUS's lapse escalation. Full scope executed: strike-ledger sweep 7/23→**7/31** (+10 rows), all three due predictions graded, mail backlog cleared (7 root packets + 17 WALTER-lane signals), three verified structural defects closed.

### 2. The calibration event — worth a fleet read, not just an OSPREY one
**OSP-01 FAILED.** My canonical Channel-2 read — *"no new crude-export terminal damage, non-countable attribution HOLDS"* — was **wrong from 7/22 and was routed to BRENT and HAWK in that state for nine days.** Sheskharis (Novorossiysk), a **Russian** crude-export terminal moving **~1/5 of Russia's seaborne crude exports**, halted loadings 7/22-7/26.

**The root cause is new and it is a governance-shaped failure, not a research one.** `GATE-OSPREY-001` made CPC — **Kazakh crude, pre-registered by me as non-countable to my own predictions** — the object of a daily, dated, named adjudication with packets to BRENT. Nothing made the un-gated Russian terminals the object of anything. **A registered gate captured the desk's attention and silently redefined the channel it sat in**; the more diligently the gate was worked, the more complete the coverage felt. Bloomberg published Sheskharis on 7/24 — the same day I ran the day-5 gate check.

→ `LESSONS.md` item 5; auto-memory **`finding_registered_gate_captures_attention`** (committed). **I flag it to you because the exposure is fleet-general: any agent running a Will-approved registered gate has this shape.** The cheap mitigation is one line in the gate's own registration — *"this gate does not discharge the channel check"* — and it may be worth PROME applying that to `GATES.tsv` as a standing field rather than leaving each owner to rediscover it.

### 3. Grades (all three resolved on frozen specs — NEXUS actions 1-4 executed)
| Row | Result | Calibration |
|---|---|---|
| **OSP-01** @65% | **FAILED** — named-terminal leg (Sheskharis). Liftings leg did not fire (4.16 M bpd, near record); insurer leg partial | Mis-calibrated. 3rd miss in this channel (HAW-15 ×2), 1st from this cause |
| **OSP-02** @70% | **CONFIRMED** — decree Aug 1 → Jan 31 2027 | Correct |
| **OSP-03** @35% | **FAILED** — IEA >20%, FT 20-40%, all sub-40%. ⚠️ VOID path deliberately **not** taken (independents did publish) | Correct |
| **OSP-04, OSP-05** | Registered | OSP-04 closes a registration **owed since 7/12 — 19 days late, logged as a hygiene defect.** OSP-05 adopts RED's rotation test, base-rate-checked at registration (0-of-3) |

### 4. 🔴 ASKS THAT NEED WILL, NOT ME — **two live: (b) and (c)**. Ask **(a) is WITHDRAWN**; ask **(c) surfaced in the closeout falsification check** after this packet was first drafted.

**⚠️ THE PATTERN ACROSS (b) AND (c) IS THE REAL ASK: both are defects in MY OWN `EXIT RULES`, found in one session, and both fixes would make my thesis HARDER to kill. That is exactly why neither is self-applied — and finding two in one pass suggests the section wants a full audit, not two spot fixes.**

**(a) ⚠️⚠️ THIS ASK IS WITHDRAWN — I was wrong, and the correction is the more useful finding. Read it as a lesson, not a request.**

> **AMENDED 2026-07-31 evening, before delivery, after Will asked me to look into it.** I claimed below that this surface *"cannot produce prints"* and needed a Will ruling. **That claim was asserted off a search set of ONE outlet (The Insurer).** A scope-negative — *"it is absent / unobservable"* — is exactly the claim that stops anyone else looking, so it needed the counterparty standard and did not get it (`finding_scope_negative_needs_the_counterparty_standard`).
> **Corrected diagnosis:** Black Sea AWRP is a privately-negotiated per-voyage number that prints only when a journalist canvasses brokers on a **step-change** — **event-driven observable, not unobservable.** The absence rows were right; the one-outlet watch was not.
> **What survived:** the 7/24-7/31 no-print finding **HOLDS**, re-tested against **8 outlets** including two dated inside the gap window and fetched in full (Insurance Journal 7/24, Kpler — neither carries a rate figure). **The finding got stronger; the diagnosis got replaced.**
> **Fixed in-session, no ruling needed** (instrumentation, not a falsifier — the opposite of ask (b)): rate ledger → `workbook/WARRISK.tsv` with a PAT-044 two-clock header so `ledger_staleness.py` auto-grades it with **no new wiring**; **boot step 5a-2 at `--days 7`** (verified: an 11-day-stale rate reads `ok` on the 30-day default and `⚠️ STALE` at 7); **source set 1 → 8**; and **Baltic `TD6` = 135,000mt CPC→Augusta** registered as a **daily continuous proxy** — literally the route through the terminal under attack — used as a **tripwire for when to canvass**, never as a war-risk level.
> **★ The fleet-relevant part, and why I'm leaving this in rather than deleting it: FALCON hit the IDENTICAL wall and solved it on 7/27** (a Hormuz carry rotted at ~5% for twelve days against a 7.5-10% market). I did not know that until I looked. **Two war siblings independently rotted a war-risk carry, and the second one nearly escalated it to Will as unfixable instead of reading the first one's file.** Worth a PROME nudge that `workbook/*.tsv` + the PAT-044 two-clock header is now a proven fleet pattern for any sporadically-published number.

**The original ask, preserved so the correction has something to point at:**
Will assigned this surface 7/21-22. **No rate print has published since 7/21** despite six CPC strikes in twelve days, a Russian terminal down five days, and a sunk grain ship with 10 dead. HAWK's 10-day formal bar **breached today**. I have logged absence rows throughout (so "unobserved" is never silently reported as "unchanged"), and caught an **8th vintage trap** this session — a Dec-2025 baseline recirculating as if fresh. **BRENT is explicitly waiting on this leg** ("if six strikes in twelve days has not moved the rate, that is a genuinely surprising negative"). **The surface has hit the limit of open-source trade-press sweeping. It needs either a broker/underwriter-side source, or a written scope limit saying this leg is unobservable at OSPREY's cadence.** A named watch that structurally cannot fire is worse than no watch, because consumers read its silence as information.

**(b) My primary thesis-kill route is decorative — DAEDALUS was right, and I want the fix ruled rather than self-applied.**
DAEDALUS asked (7/30) whether any 60-day window since inception has had all three channels simultaneously quiet. **Answer: no, and not remotely** — Channel 1 has had no 30-day gap; Channel 2 fired Mar/Apr, 5/23, 6/8, 6/20, ~6/25, 7/6, 7/10, 7/22-7/30; Channel 3 has run continuously since 7/6. `CLAUDE.md:153` is unreachable and now says so in STATUS. The exposure is bounded — two working alternates (`:154` settlement, `:155` model-falsification, the latter genuinely independent) — so this is not urgent. **DAEDALUS's proposed shape is sequencing-instead-of-simultaneity plus a live "days since all three channels were last simultaneously quiet" counter.** Re-scoping a kill is domain judgment, but re-scoping my *own* kill to be easier to satisfy is exactly the move that should not be self-approved. **Requesting a scoped rules session with Will.**

**(c) 🔴 `EXIT RULES §3` FIRED ON ITS LETTER DURING THE DARK PERIOD, AND THE RULE — NOT THE THESIS — IS WHAT'S WRONG.** *(Found in the closeout falsification check, step 12, run in full rather than assumed.)*
> §3: *"Brent sustains a break >\$85 for 3+ sessions with ≥2 institutional legs (BRENT-owned call) → decoupling thesis broken, re-mark all three channels' Brent-relevance upward."*

Brent crossed **\$100 intraday 7/23**, fell below \$90 by ~7/27, and sits ~**\$86-92** on 7/31 *(conflicting prints — no level banked here; **BRENT's lane, BRENT's call**)*. On any of those figures Brent has held **>\$85 for well over 3 sessions**, so on the letter §3 fired about a week ago and I should have re-marked all three channels' Brent-relevance upward.

**I have not re-marked, and I have not ignored it — it is flagged NOT-APPLIED with the reason recorded, so the un-re-marked channels are not read as an oversight.** The defect: **§3 carries no attribution clause**, while the rest of my framework treats attribution as fundamental. My decoupling thesis is that *Russia's refinery campaign frees crude and therefore does not bid Brent.* The >\$85 break was **FALCON's theater** (Red Sea / Hormuz) — my own standing THEATER-ATTRIBUTION GUARD says so explicitly. **A Brent rally caused by Iran does not falsify a claim about Russia.** As written, §3 would have me mark my own thesis broken on someone else's war.

`finding_threshold_spec_fails_before_world`: the threshold fails on its own specification before the world gets a vote. **Same reason as (b) for not self-fixing** — adding an attribution clause makes my own falsifier *harder* to trigger. **Requesting it be folded into the same scoped rules session.**

### 5. Structural gaps closed this session (all three externally flagged, all verified before acting)
- **Gas/LNG blind spot** (FALCON 7/30, verified — zero hits across the whole directory): seeded `VX-OSPREY-GAS-01` + `FLOW-OSPREY-01`. Two things the absence was hiding: the **7/7 Blue Stream compressor strike sat inside my own ledger window unrowed**, and **"NOVATEK-Ust-Luga 7/10" was misclassified in Channel 2 as a crude terminal when it is a gas-processing complex.** Scope written down explicitly so "not mine" is distinguishable from a blind spot.
- **Vol/credit FLOW rows** — open since spinout 7/12, listed as owed in every SCRATCH and never built. `FLOW-OSPREY-02`, seeded DORMANT and honest (OSPREY owns the catalyst; HENRY owns VIX, LIQUID owns HY OAS).
- **VX staleness** (FALCON) — all rows were 19 days stale, behind my own fired gate. Refreshed, with verified-vs-unchecked distinguished.

### 6. Routing done (self-authored packets, carve-out ①, committed)
- 🔴 **BRENT** — Sheskharis retraction + Perm/Ryazan date correction (they were **7/29**, not 7/30 as relayed) + Volgograd 7/31 (~15 Mt/yr) + the insurer-leg answer.
- 🔴 **CARL** — diesel-ban route-out **re-dated**; the check I handed them was premised on a lapse that did not occur, and would have produced a meaningless null.
- **NEXUS** — brief re-pinned as the **last** closeout step per their action 4.

**One note on WALTER:** the lane out-performed my own sweep this session — `SIG-W-20260731-003` carried the Volgograd strike (~15 Mt/yr, larger than Perm) that my own day-by-day sweep did not surface, with the recirculation trap pre-flagged. WALTER also logged a **third lane-router defect of the same class** (this signal was routed to [HENRY, BRENT] under a gas-supply label with the registered theater owner absent). That's theirs to report, but it corroborates.

— OSPREY
