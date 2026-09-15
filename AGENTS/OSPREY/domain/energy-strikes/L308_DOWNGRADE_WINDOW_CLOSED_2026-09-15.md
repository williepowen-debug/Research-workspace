# DOCKET L308 — Channel-downgrade-rule objection window: **CLOSED 2026-09-15. RULE REMAINS IN FORCE.**

**Owner:** OSPREY · **Written:** 2026-09-15 · **Session:** PROME-spawned, WQ-184 L0 spawn driver (L308 dated today, names OSPREY)
**Rule at issue:** `AGENTS/OSPREY/CLAUDE.md` § EXIT RULES **§1b — Channel DOWNGRADE path**, RULED 2026-09-08 by Will (verbatim ***"all approved go ahead"***), which closed OWED-15.
**Window as published:** *"BRENT and HAWK have 7 days (to 2026-09-15) to object, as consumers of the marks; an objection re-opens the text via PROME, it does not suspend the rule."*

---

## 1 · VERDICT

> **NO OBJECTION WAS FILED BY EITHER NAMED CONSUMER. The §1b downgrade path stands in force, unamended, as ruled on 2026-09-08. The window is closed and is not reopened.**

**No mark moved. No band moved. No threshold moved. $0. No trade language.**

---

## 2 · The two consumers — disposition, and where each is EVIDENCED

⚠️ **Neither finding rests on an absence.** Both consumers positively recorded a disposition at **their own artifacts**, which is a stronger result than the SEARCH-NOT-FOUND the task anticipated. I read each at its source rather than inferring from my empty inbox — `finding_record_of_an_action_is_not_the_action`, applied in the useful direction: check the TARGET artifact.

| Consumer | Disposition | Confidence | Evidence, at the artifact |
|---|---|---|---|
| **HAWK** | **NO OBJECTION** — filed early, 2026-09-10 | **VERIFIED** | Packet delivered into my own inbox and consumed 9/10: `inbox/processed/2026-09-10_from-HAWK_downgrade-path-NO-OBJECTION-plus-two-consumer-flags.md`. Its closing line: *"The objection window is closed from HAWK's side: NO OBJECTION."* |
| **BRENT** | **NO OBJECTION** — recorded 2026-09-10 12:06:59-04:00 | **VERIFIED** | `AGENTS/BRENT/board_log.tsv`, verbatim: *"Consumed at the 9/10 drain (deferred 9/9). **No objection lodged to the channel downgrade path by the 9/15 window:** BRENT consumes OSPREY marks and holds no Bloomberg 8/30 or 9/6 print to offer."* Independently mirrored in `AGENTS/BRENT/NEXUS_BRIEF.md`: *"No objection to the channel downgrade path by the 9/15 window."* |

### What I checked, in order — the declared path first, then the documented fallbacks

1. **Declared path — my own inbox.** `AGENTS/OSPREY/inbox/` top level: **no BRENT file, no HAWK file.** Only three unconsumed WALTER-lane items (dispositioned this session, §5). `inbox/processed/` holds HAWK's 9/10 no-objection. **SEARCH-NOT-FOUND for a BRENT packet — and it stays SEARCH-NOT-FOUND, because BRENT never sent one.**
2. **Documented fallback — `git log` over my whole directory since the window opened (9/8).** Every commit touching `AGENTS/OSPREY/` from 2026-09-08 to today enumerated. The only inbound files are three WALTER signals (9/14) and the PROME/HAWK WQ-216 traffic (9/10-9/11). **No BRENT-authored file ever entered my tree.**
3. **Documented fallback — BRENT's own outbox.** `AGENTS/BRENT/outbox/` and `outbox/delivered/`: the only 9/10 delivered item is `2026-09-10_to-FALCON_riesco-wq189-grade-does-not-turn-on-laden-leg.md`. **Nothing addressed to OSPREY.**
4. **The upgrade from SEARCH-NOT-FOUND to VERIFIED — at BRENT's artifact, not by a broader grep.** My packet is in `AGENTS/BRENT/inbox/processed/`, i.e. **BRENT received and consumed it**. Its disposition is recorded in BRENT's `board_log.tsv` and `NEXUS_BRIEF.md` as quoted above. **The absence of a reply packet is explained, not merely observed:** BRENT considered it and chose not to object.

### ⚠️ One stale surface at BRENT, flagged — not edited, and it changes nothing

`AGENTS/BRENT/RULINGS.md` § `R-2026-09-08-OSPREY-owner-rules` still reads: *"The packet remains in inbox pending that source review and sender commit; no acknowledgement, objection or external send issued."* That is the **9/9 deferred state**, superseded by BRENT's own 9/10 consumption. It is a **vintage artifact, not a contradiction** — `board_log` and `NEXUS_BRIEF` both carry the later disposition, and RULINGS was simply not restamped. **A reader who travels RULINGS alone concludes the window is still open.** Routed to BRENT via PROME; **I do not edit another desk's file.** `finding_summary_section_merges_what_the_body_separates` / `finding_header_edit_is_the_edit_most_mistaken_for_maintenance`.

---

## 3 · Would the rule have fired in its own window? **No — and the reason matters**

§1b requires a **conjunction**: the Upgrade Trigger's evidence reverses on the **same instrument for two consecutive prints** **AND** no new in-channel `STRIKES.tsv` row for **14 days**.

| Channel | Instrument leg | Strike-drought leg (14d) | Fires? |
|---|---|---|---|
| **1** (refineries/products) | EA/Kpler monthly runs ≥ 4.5 M bpd × 2 months — **not met** (August ~3.8) | **Emphatically not met** — 5 new in-channel rows this week alone | **NO** |
| **2** (crude-export terminals) | Bloomberg 4-wk ≥ 3.9 M bpd × 2 prints — **cannot be evaluated; instrument unreadable since 8/23**, newest held print 3.46 | Not met — clock anchored 9/9 (Novorossiysk) | **NO** |
| **3** (shadow-fleet tankers) | the §1 21-day kill clock **is** the downgrade | **11/21** as of today (anchor: Nefrit USV 9/3-4) | **NO** |

✅ **HAWK's structural point holds up under this week's evidence and is worth restating:** in the DOWN direction the conjunction **fails safe** — an unreadable Bloomberg print *blocks* a downgrade outright, so no mark falls on missing data.

⚠️ **And the other face, which HAWK flagged and this session confirms is still live:** Channel 2 can be neither upgraded nor downgraded while the instrument is unreadable, so it **freezes at 5 🔴** — and a frozen mark is indistinguishable, on a dashboard, from one actively held on evidence. **The `FROZEN — INSTRUMENT UNREADABLE SINCE 8/23` vs `HELD-ON-EVIDENCE` labelling HAWK suggested is carried in STATUS and SCRATCH and stays.** This is the two-clock problem applied to a mark instead of a ledger.

### 🔑 A robustness note on the Channel-3 clock, because the letter is ambiguous and today it costs nothing to say so

The feed surfaced a **9/12 Black Sea event: a Ukrainian naval drone destroyed a Russian unmanned boat** ("first-ever battle" of its kind). Is that a *"vessel-strike incident"* under §1's Channel-3 letter?

- **On the channel's SUBJECT (shadow-fleet tankers):** no — a military USV-vs-USV engagement is not a shadow-fleet hull. Clock stays anchored 9/4 ⇒ **11/21**.
- **On the letter's bare WORDS ("no vessel-strike incident in Black Sea..."):** yes ⇒ **3/21**.

**Either way no kill and no downgrade, so nothing turns on it today — which is exactly why it should be settled now rather than at the sitting where it decides a channel's fate.** Not self-ruled; registered and routed. Same family as OWED-32, and as OWED-39 opened this session.

---

## 4 · Related registered date, confirmed on my own calendar

**DOCKET L309 — 2026-10-06 — strike-feed four-week evaluation.** ✅ **Confirmed present and dated in my own surfaces** (`SCRATCH.md` NEXT SESSION item 6; `CLAUDE.md` § FILES, `scripts/strike_feed.py` row: *"Acceptance test running 9/8 → 10/6"*). **Not performed today, correctly — it is three weeks out.** Both legs are registered: **recall** (feed surfaces ≥1 event the manual sweep missed) and **precision**.

⭐ **Interim datum for that evaluation, generated today and worth recording while it is fresh:** the 9/15 feed run surfaced **five material energy events this desk did not hold** (Saratov 9/11, Slavyansk ECO 9/13, TANECO 9/13, Makhachkala 9/10, Syzran 9/15). **The recall leg's pass criterion has now been met on two separate runs** (first run 9/8: Kstovo/NORSI 8/26 + Novorossiysk 9/8-9). The precision leg is untested and is the one that can still fail.

---

## 5 · Whole-inbox drain (PROME L0 rule: every sender, not just the triggering item)

| Item | Disposition |
|---|---|
| `SIG-W-20260914-023` — BOARD/INDEX.md read is unbounded | **CONSUMED, ACTED.** Claim **VERIFIED at the artifact**: `measure.py` reads **501,175 B / 1,071 lines** (WALTER said 498,513 B — the file has since grown; directionally confirmed). My `CLAUDE.md` boot step 6b **repaired**: bounded `## Cluster overview` ToC read + drill to `HYDROCARBON_INFRA` (62 signals) or grep, with the truncation-is-topical-and-silent warning stated. WALTER's own fix adopted verbatim in shape — and it matches what the generated file's own preamble already instructs. |
| `SIG-W-20260914-025` — is there a live scaled Russian refinery-outage campaign? | **CONSUMED, ANSWERED — see §6.** |
| `SIG-W-20260914-025-CORRECTION-NOTE` — the ULSD "collapse" was ~93% a contract roll | **CONSUMED, ACCEPTED, and it is load-bearing for me.** Read BEFORE acting on -025, as instructed. HENRY owns the series so HENRY's matched figure governs (108.24 → 107.45, −$0.79 / −0.73%). **Carried into §6's routing caveat: any grade of an outage scale into the products complex must be computed on MATCHED CONTRACT MONTHS, and must not be keyed to a date** — the roll follows volume migration, and the product legs left ~16 days early. |

---

## 6 · WALTER's ASK, answered from this desk's own evidence

> *"Is there a live, scaled Russian refinery-outage campaign right now, and what capacity is actually offline?"*

### ① Is the campaign live and scaled? **YES — unambiguously, and this was its densest week on this ledger.**

Five new energy rows for 9/9–9/15, every one verified at named dated sources:

| Date | Facility | Nameplate | What is established |
|---|---|---|---|
| 9/11 | **Saratov** (Rosneft) | 4.8 Mt/yr | Fire; **re-strike 3 days after 9/8**, inside its own repair window; 3rd row on this plant |
| 9/13 | **Slavyansk ECO** (independent) | ~5.2 Mt/yr | Fire; **new facility**, a non-integrated independent refiner |
| 9/13 | **TANECO** (Tatneft) | >16 Mt/yr | **One storage tank** alight — ⛔ not a processing unit |
| 9/15 | **Syzran** (Rosneft) | ~8.5 Mt/yr | Fires at multiple points; **40+ drones** at Samara Oblast; GS **and** Zelensky |
| 9/10 | **Makhachkala port** | n/a | Oil infrastructure, fire — **first Caspian row**, basin classification routed (OWED-39) |

Add the already-held 9/6 Ryazan consequence (**CDU-6 + CDU-4 shut, ~240 kb/d primary distillation, repairs "up to several weeks"**) and the picture is a sustained multi-basin campaign, not a spike.

### ② What capacity is actually offline? **The only honest answer is the band — and it did not move today.**

> **~30% of Russian refining capacity, range 25–35% [EST], `KB-OSPREY-029`, runs-anchored (July 3.6 / August 3.8 M bpd).**

⚠️ **Three caveats that must travel with that number, per my own rail:**
- **It is a PROXY, not a measurement.** Runs can fall for feedstock, demand or maintenance reasons, and capacity can be offline while surviving units run harder. It is a reasoned convergence.
- **Not one of this week's five events carries an independent capacity-offline figure.** Fires and GS confirmations, no aggregates.
- ⛔ **I REJECTED the two figures a casual search offers.** A summary surfaced *"38% of primary refining capacity idle as of September 28"* and *"42.7% disabled"*. The first is **2025-vintage** (September 28 has not occurred in 2026); the second is **Ukrainian-GS claim-class**, and OSP-03's letter is explicit that a GS claim **FAILS regardless of how many outlets relay it** — relay is not independent verification. **Neither is carried, and nobody downstream should carry them either.**
- 🟠 **One genuinely open thread (OWED-37):** a snippet attributes to *S&P Global Energy* that strikes *"have already reduced its actual capacity by more than 30%"* — the referent of *"its"* is **ambiguous** (the Saratov plant, or Russia nationally) and I did not open the primary. **Not logged as a figure.**

### ③ The part of WALTER's framing that this desk must correct — and it cuts against the intuitive read

✅ **WALTER is right that a live foreign supply channel under-specifies every US-only attribution on that board.** It is live and it is large.

⛔ **But the sign is not the obvious one, and BRENT's standing EXPORT-SIGN WARNING is the reason: "burn a refinery, free the crude."** A refinery outage **suppresses crude-export declines while supporting product cracks**. So this week's evidence is **crude-BEARISH / product-BULLISH at the margin** — the same lever as the Gulf and the **opposite sign**. Reading a dense refinery-strike week as undifferentiated "supply stress" gets the sign wrong twice.

**And one more, from this session's own finding:** the 9/9 Novorossiysk event — routed to BRENT as a crude-export-terminal event — is now **named as the FUEL OIL (products) terminal, not Sheskharis**. That pushes it further onto the products side of the ledger. **No number is retracted, because no bpd figure ever existed for it.**

---

## 7 · What I did NOT do, stated plainly

- **No mark, band, threshold, confidence or channel-score moved.** Upgrades remain Will-gated; the §1b downgrade conjunction is not met on any channel.
- **No Channel-2 or Channel-3 classification self-ruled** — OWED-39 (Caspian basin) and the Channel-3 vessel-scope ambiguity are **routed to PROME**, both deliberately raised while nothing turns on them.
- **No BRENT or HAWK file edited** — the stale `BRENT/RULINGS.md` line is flagged, not fixed.
- **No price quoted.** Brent levels are BRENT's; this desk holds none.
- **Sweep residue declared** in the `STRIKES.tsv` header: `militarnyi` returned EMPTY_FEED and was **NOT read**; day-by-day facility-name-free port queries were not run for every date. The pass was **instrument-complete, not query-exhaustive**.

---

## 8 · New obligations opened this session

| ID | Obligation |
|---|---|
| **OWED-37** | Open the S&P Global primary behind *"reduced its actual capacity by more than 30%"* and resolve the referent — or drop it. |
| **OWED-38** | Syzran 9/15 consequence leg: re-check for a halt/repair/restart statement (row written same-day, so its consequence is necessarily absent). |
| **OWED-39** | **Routed to PROME:** does the §1 **Channel-2** kill letter need a geography qualifier, as Channel 3 got on 9/8? A Caspian oil port currently resets a clock for a **Black Sea/Baltic seaborne-export** channel. Free to rule today; expensive to rule at a kill. |
| — | **Channel-3 vessel-scope ambiguity** (§3 above) folded into the same routing. |

---

*OSPREY, 2026-09-15. DOCKET L308 discharged. Rule in force. No capital moved.*
