# MANAGEMENT PROPOSAL — VLO ×1 held share — a price rule vs a policy/event rule

**Date:** 2026-09-28 Mon, written 18:18 ET (`date` wall clock) · **Id:** `MGMT-VLO-SHARE` (management-only; no SETUPS row — that ledger is at 97% of its read budget with a rotation owed; registered in `setups/INDEX.md`)
**Commissioned by:** Will, ~18:10 ET 9/28 in BRENT's window, verbatim (WQ-329 item 2 · DOCKET L535): *"Ask PROME to commission one bounded TERRY management proposal for my held VLO share now. Compare a price-based rule with a policy/event-based response. State the evidence, observation timing, missing-data treatment and execution limitations. Keep it proportionate to one share. This authorizes preparing the proposal; I approve the resulting rule separately. Do not wait for the historical study."*
**Parent card:** `setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md` (`TRY-BRENT-REFINER`), § ⑦ fill record: *"no rule created for the held share — that needs its own line, Will's [Approve]"*. This file is that line, proposed.
**Thesis owners:** BRENT (distillate-strong leg) · HENRY (`F1` / `HEN-46`, the $95 and $90.16 lines). **Construction:** TERRY. **Approval:** Will (root rule #5).
**`$0` MOVED · NO ORDER · NO SIZE CHANGE · NO GATE OR THRESHOLD MOVED.** This proposes a *rule*; a rule's fire is a sell recommendation that Will executes by his own hand.

**Out of scope, stated once:** the **2 STAGED shares** (WQ-213 / WQ-282, `GATE-TERRY-VLO-SCALE`). Nothing here changes that gate, its letter or its $95 line.

---

## 0. The position and its scale

| item | value | source |
|---|---|---|
| holding | **VLO ×1 share**, bought 9/18 @ **$412.00** limit, Will's hand | card § ⑦ (Will's pasted receipt) |
| account | **Fidelity** (FORGE 9/27 reconcile, Activity row 7 ⇒ D-55 account leg CLOSED); account TYPE Traditional IRA = **INFERRED** | `FORGE/STATUS.md` § Fidelity — Longs |
| fill time | UNKNOWN (D-55 residual) — does not bear on this proposal | FORGE D-55 |
| last close | **$389.57** (+0.62%), 9/28 | `fetch.py price VLO`, pulled 18:14 ET |
| open P&L | **−$22.43 / −5.44%** vs $412.00 | arithmetic |
| size of a normal day | 1-year daily σ **2.33%** ⇒ **~$9** on one share (252 bars to 9/28); worst 1-y day −7.48% (2026-04-17) | own yfinance pull, `auto_adjust=False` |
| size of the last ban scare | 9/18 → 9/22: $413.28 → $377.14, **−8.7% ≈ −$36** | BRENT note §4, reproduced in own pull |
| worst case | the whole share, **$389.57** — **below the $500 per-card cap** (STATUS standing rule). The cap cannot bind. | arithmetic |
| rule today | **NONE** on the held share (card § ⑦, § ⑨, § ⑩; FORGE row: *"No exit rule exists on the held share"*) | — |

## 1. Proportionality — what one share is worth watching

**Worth doing (≈ zero marginal cost):**
- A rule that **rides reads already being made**: the crack is already graded for `GATE-TERRY-VLO-SCALE` through its 10/14 review; export-ban news already reaches Will, WALTER and BRENT.
- A rule **simple enough for Will to act on alone**, with no desk session needed.

**Not worth doing for ~$390 of exposure:** intraday monitoring · a new watcher, script or between-session tool · a TERRY spawn whose only job is to read a crack for this share · an option hedge (any VLO put costs a material fraction of the risk it covers) · re-litigating the $90.16/$95 basis for this share (the 10/06 sitting, L471, does it for the gate anyway) · a GATES row with its own review cadence after 10/14.

**"Neither" is a legitimate answer.** The share's full loss is under the card cap, and Will accepted the book's concentration in writing (WQ-297 A, 9/25 14:16 ET). The card's own § 7 says *"shares have NO defined loss without a rule"* — on one share, the defined loss is the share itself.

---

## 2. FORM A — PRICE-BASED: the Nov diesel crack against HENRY's existing lines

**Rule as proposed:**
- **A-exit:** the November-matched ULSD crack **settlement** (`HOX26 × 42 − CLX26`) closes **below $90.16** (HENRY's thesis-dead line, `F1` second tier / `HEN-46`) ⇒ TERRY writes a **SELL** recommendation for the held share; Will sells at the next regular session.
- **A-notice:** a settlement **below $95** (`F1`, the stand-down line for the staged shares) ⇒ **notice only** on the held share. TERRY states it in the gate grade line. **No action.**
- Both lines are existing referents. **Neither is moved.** This rule only reads them.

**Why the exit is $90.16 and not $95:**
1. $95 is the card's **add filter** (*"<$95 stand down, <$90.16 dead"*, card § RE-ARM #2 ②). "Don't add more" is not "the thesis is broken". With one share, an exit is the whole position, and root rule #7 reads that as a broken thesis.
2. **$95 is ~$1.20 away** (below), and the crack moved **−$7.04 (9/23)** and **−$7.09 (9/24)** in single sessions last week. A $95 exit would very likely fire on moves the thesis owner does not call thesis-death. $90.16 is ~$6 away: one bad session, but a session of the size that ends the thesis.

**Evidence it reads:**
| leg | series | source (in the gate's registered order) | basis |
|---|---|---|---|
| crack | `HOX26` (NYMEX ULSD, **New York Harbor**, Nov) × 42 − `CLX26` (WTI, Nov) | ① CME settlement (blocked to desk tools; Will can read cmegroup.com) · ② the yfinance daily row dated to the session, **accepted only if within $0.15 of ③** · ③ the **14:28–14:30 ET 1-min VWAP**, labelled **ESTIMATE** | November fixed **through 2026-10-14** (HENRY `90fa9a4c1`); after that, whatever Will rules at the **10/06 sitting (L471 / WQ-252)** |
| contract identity | `expireDate` on both legs, every pull | vendor | `HOX26` → 2026-10-30 · `CLX26` → 2026-10-20 (verified 9/28 pull) |

**Where it stands tonight (9/28, ESTIMATE, single vendor):** ③ = `HOX26` VWAP 4.49427 × 42 − `CLX26` VWAP 92.5616 = **$96.20** (3 bars per leg; volume 2,677 / 8,887; own pull 18:1x ET). BRENT's settle-proxy was $96.23. ⇒ **$1.20 above $95 · $6.04 above $90.16.** Not fired on either line. ⚠️ **The `F1` read for 9/25 is still UNKNOWN** ($95.0014, inside the ±$0.15 band; card § ⑩).

**Observation timing:**
- CME settles ~14:30 ET. ③ can be computed from ~14:31.
- ⚠️ **A futures daily bar read after 14:30 ET is the last trade, not the settlement** (`RISK_RULES` 6c). Never grade from it as a "close".
- The ② daily row is often **not final the same evening**: the rows dated 9/24 and 9/25 both still carry the prior session's volume (`HOX26` 100,465 on both; `CLX26` 410,015 on both; seen 9/28). So ② usually becomes usable the next day, if at all.
- **Action timing:** a fire on session T becomes a recommendation at TERRY's next touch, and a sale in the regular session after that. **Nothing reads this crack automatically.** The only reader is TERRY when spawned — today, through the `VLO-SCALE` grades. **Worst-case lag = the gap between TERRY sessions.**

**Missing data (UNKNOWN never defaults to a fire):**
| case | treatment |
|---|---|
| no 1-min bars / feed down | UNKNOWN for that session; held, re-read at the next session; **never back-filled** with a later number |
| ③ only, within **±$0.15 of $90.16** | UNKNOWN (same band the gate letter uses at $95) |
| ② row not final (duplicated volume, or carrying the post-settle last trade) | ② rejected; fall back to ③ |
| a leg's contract month is wrong (continuous `=F` ticker, or a rolled identity) | reading rejected (construction rule #22) |
| single vendor | ③ is single-vendor by construction and is labelled ESTIMATE. That is proportionate for one share, and it is the basis Will already approved for the gate. |
| **after 10/14 with no ruling from the 10/06 sitting** | **A is SUSPENDED (reads UNKNOWN).** It never carries November past 10/14 silently. |

**What Form A does badly:**
- **Wrong hub for the ban risk.** HO settles in New York Harbor; stranded export barrels would sit on the Gulf Coast, where VLO refines. Gulf margins could fall more than the graded crack shows (BRENT §3; direction only, magnitude unmeasured).
- It **ignores what the stock is actually trading on.** Since 9/23 VLO has moved with crude, not the crack (9/25 driver read; correlation with USO +0.51 over 120 sessions).
- It is **a management ride-along**, not a stop: its latency is TERRY's spawn cadence.

**A′ — VLO's own price. Considered, NOT recommended.**
- **Rule:** VLO official close below **$375.84** (the 9/23 close, the low of the ban-headline week) ⇒ sell.
- **Noise:** $375.84 is **3.5%** below Monday's close. Over the last year, **78 of 252** 10-session windows (**31%**) printed a close ≥3.5% below their start (origins 2025-09-12 → 2026-09-14, own pull). This line would fire on ordinary noise, often on a crude move the card never underwrote.
- **Its one merit:** it can rest at the broker as a stop order, with zero monitoring. But a resting stop triggers on an intraday print, not on the close (a different basis), and can fill through a gap. Whether this account offers the order type is **UNVERIFIED**.

---

## 3. FORM B — POLICY/EVENT-BASED: the US diesel export-restriction path

**Rule as proposed (three tiers; only the first acts):**
| tier | event | primary source required | action |
|---|---|---|---|
| **B1 — FIRE** | A **signed** presidential action with legal force that bans, caps or licenses **US distillate/diesel exports**: an executive order, a proclamation, an IEEPA national-emergency declaration with that operative text, or a Commerce/BIS licensing rule | the **text** at whitehouse.gov (Presidential Actions) or the Federal Register | **SELL the share at the next regular session.** Will can act on this without the desk. TERRY writes the rec at its next touch if Will has not acted. |
| **B2 — REVIEW** | **Valero itself** agrees to curb exports, on the record (press release, 8-K, or a named executive) | Valero IR / SEC EDGAR | TERRY re-reads the share at its next touch (crack, VLO close, driver). **No automatic action.** |
| **B3 — CONTEXT** | EIA weekly distillate exports (WPSR, **Wed 10:30 ET**, week ending the prior Friday; the first is **Wed 9/30**, week ending 9/25) | EIA | **Never a trigger by itself.** The last 8 weeks ran 1,331–1,935 kb/d, and one Sep-2025 week printed 851 (BRENT §5). A single week's drop is consistent with a voluntary curb but does not prove one. |

**These do NOT count as B1:**
- a headline or TV remark without signed text (Trump 9/22 and 9/27 were remarks);
- anonymous-official reports, and "no decision" statements;
- another refiner agreeing to curbs (notice only);
- voluntary arrangements (B2 at most);
- a federal diesel excise-tax suspension, state actions, the Jones Act waiver (in force to 11/15).

**Evidence and why:** BRENT's note §1–§2 (policy facts; EIA v2 primary). Exports are **~30% of US distillate output** (4-week basis). Gulf Coast storage headroom ≈ **2 weeks** of stranded barrels at the 2020 high; working range **2–5 weeks** to run cuts [EST, BRENT's, with its own caveats]. **No probability is attached** (BRENT: no base rate). **BRENT's withdrawn breach timings (MR19) are not used here.** No gate is graded from the §3 sensitivities.

**Observation timing:**
- An order can be signed at any hour, including weekends.
- The White House text usually appears the same day; the Federal Register lags by days. The headline will lead the text by minutes to hours.
- The action is always the next regular session (09:30–16:00 ET) after the primary text is read.

**Missing data:**
| case | treatment |
|---|---|
| headline, no text yet | **UNKNOWN — not fired.** Re-check the primary. ⚠️ This costs time on a real ban; the text normally follows within hours. |
| text signed but its distillate scope is ambiguous (e.g. "petroleum products") | Fires if diesel/distillate exports fall inside the operative scope. If genuinely unclear ⇒ UNKNOWN, and the call is Will's. |
| order enjoined or rescinded after signing | Does not un-fire. If sold, there is **no re-entry rule**; buying back is a new trade and needs a card. |
| EIA print missing or late | B3 is context only; nothing happens. |

**Execution limitations specific to B:** **B does not beat the gap.** On talk alone VLO fell 8.7% in 2 sessions, and on 9/23 HO fell ~4% in a day (BRENT §4). A signed order would be priced at the next open, before either of us can act. B buys an exit **before the second leg**: Gulf storage filling, then run cuts, which the NYH crack may understate. **Whether day one under-reacts is unmeasured.** B also stays silent on the **most likely path**: a voluntary curb or "tweak" (BRENT §1). Only A sees that path, and only if it shows up in the crack.

---

## 4. Side by side

| | **A (crack < $90.16)** | **B (signed ban, primary text)** |
|---|---|---|
| reads | the card's own thesis variable, at NYH | the policy event directly |
| catches | every path that kills the crack: ban, voluntary curb, demand, crude spike | only a formal restriction |
| misses | the Gulf-vs-NYH gap; crude-led moves in the stock | the voluntary path; anything non-policy |
| data risk | single vendor, settlement proxy, ±$0.15 band, basis unsettled after 10/14 | headline-before-text; scope wording |
| latency | TERRY's spawn cadence (T+1 at best) | next session after the text; Will can act alone |
| monitoring cost | ≈0 through 10/14 (rides VLO-SCALE grades); after that, a real cost or SUSPENDED | ≈0 (news Will already sees) |
| false-fire risk | low at $90.16 (high at $95; A′ at 31% noise) | low (signed text only) |

**They are complements, not rivals:** B covers the discrete formal ban; A covers every other way the thesis dies.

## 5. Execution limitations (both forms)

- **One share, Fidelity, Will's hand.** A long sale raises no short-sale or margin question. The commission on a stock sale is **not in the repo — UNVERIFIED.** A market or limit order is Will's choice; on one liquid share the spread is pennies.
- **Neither A nor B can rest at the broker.** Both need a human to read something. (Only A′ could rest, and it is not recommended.)
- **Root rule #6** has no object on a share sale (no convexity is bought), as recorded at the fill. **TERRY's construction rule for this exit:** sell at the next regular session **whatever the day's colour**. Waiting for a green day to sell a thesis-broken long is waiting for a bounce. That is a construction preference, **not a bar on Will's order.**
- **Root rule #7:** with one share, any exit is the whole position; there is no trim.
- **Gap risk:** both forms act at the next session. An after-hours or weekend event gaps.
- **Earnings:** VLO Q3 reports "late Oct" per the card. The date is **UNVERIFIED** here (company IR governs). Not a trigger under either form.
- **Staged shares (out of scope, one flag):** a **B1 fire would not stand down the 2 staged shares** under `GATE-TERRY-VLO-SCALE`'s current letter, which keys only on A/B/F1. If Will adopts B, whether the same event should also stand them down is a separate question.

## 6. Desk read (not a ruling)

**BOTH: A at $90.16 (with $95 as notice only) plus B1.** Together they cost ≈ nothing extra. Each covers what the other misses, and neither fires on noise. A is suspended at 10/14 unless the 10/06 sitting sets its month. **"Neither" is the honest alternative:** the share's whole value is below the card cap and the book's concentration is accepted. If Will takes only one, **take B**: it needs no desk session, it covers the scenario BRENT flags as the largest single risk, and Will can execute it alone.

---

## ⚖️ ASK — Will

**Choose one for the held VLO share:** **A** (crack settlement < $90.16 ⇒ sell rec; < $95 notice only) · **B** (signed export-restriction text at primary ⇒ sell next session; B2 review; B3 context) · **both** (desk read) · **neither**.
Optional if A: the exit line is **$90.16 (desk read)** or **$95**. Choosing $95 means exiting on the add filter, which is ~$1.20 away tonight.
On approval, PROME registers the rule; TERRY grades it at its touches. **A fire is a sell recommendation you execute, never an order placed for you.** The staged 2 shares and `GATE-TERRY-VLO-SCALE` are unchanged either way.

**APPROVAL REQUIRED — Will must approve/reject before execution.** — TERRY
