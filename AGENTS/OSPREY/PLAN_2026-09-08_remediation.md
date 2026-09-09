# OSPREY — Remediation plan, 2026-09-08

**Why this file exists:** Will asked (9/8) how to address the desk's structural gaps and in what order. This is the plan; `SCRATCH.md` carries the per-session sequence and `STATUS.md` the owed register. Items marked **[WILL]** need his word before they start; **[OWN]** are within OSPREY's authority and are scheduled here.

**Ordering rule:** longest lead time first (the build), cheap self-owned hygiene alongside it, everything that needs a ruling batched into ONE packet.

---

## Phase 0 — this week, own authority [OWN] — **ALL THREE DONE 2026-09-08** (0.1 → KB-097; 0.2 → LESSONS 9.4 KB hot, `archive/LESSONS_ARCHIVE_2026-09-08.md`; 0.3 → drafted in the Phase 1 packet)

| # | Item | What, concretely | Done when |
|---|---|---|---|
| 0.1 | **Fallback read for the crude channel** | Register in KB + STATUS a basis-noted fallback for the *channel read* (not for OSP-06, whose instrument is frozen): CREA's monthly Russian fossil-fuel export analysis; Kpler/Vortexa figures as relayed by Reuters/Bloomberg. Ask BRENT (packet already sent 9/8) whether its terminal covers the weekly flow report. | A KB row names the fallback series, their cadence and basis; STATUS's export bullet cites the newest one when Bloomberg is unreadable. |
| 0.2 | **LESSONS.md hot/cold split** | At ~82% of the read budget. Keep each item's headline + "what happened" (one line) + **Rule** hot; move corollaries and narrative to `archive/LESSONS_ARCHIVE_<date>.md` verbatim with a crc32 receipt. Self-check: every Rule sentence survives; item numbering unchanged (cited by number). Target ≤ 16 KB hot. | read_cap_check shows LESSONS ≤ 50% of budget; archive crc recorded in the commit body. |
| 0.3 | **Draft the downgrade-path semantics** so the ruling has text to rule on (see 1.2). | Draft in a packet, not applied. |

## Phase 1 — one packet to PROME for Will's word [WILL] — **PACKET SENT 2026-09-08** on Will's in-session word *"please begin with your recommendations"* (this authorises the ASKS to be put; each ruling still needs Will's own word on the item). Build spec cc'd to DAEDALUS.

| # | Ask | Proposed text / spec | Cost & risk |
|---|---|---|---|
| 1.1 | **Strike-feed automation (DAEDALUS build)** — OWED-19, open since spinout | `scripts/strike_feed.py`: fetch (i) Palaemon blog index → newest weekly report; (ii) Windward blog; (iii) Kyiv Independent, Ukrinform, Moscow Times, Militarnyi RSS filtered on refinery / terminal / tanker / port / drone keywords; (iv) optionally the Ukrainian GS daily report via a relay. Emit `domain/energy-strikes/FEED_CANDIDATES_YYYY-MM-DD.tsv` (date · headline · URL · matched keywords) and DIFF it against `STRIKES.tsv` on date ± 1 day + facility/vessel token. Boot step 5b reads the candidates file. Fetch-and-diff only, no classification (PAT-048 instrument-light). | ~1 DAEDALUS session. Risk: 403s on some sites (Kyiv Post, uavarta did) — RSS is more robust than page fetches; the diff is advisory, a human still rows. **Success test:** over the first 4 weeks the feed surfaces ≥1 event the manual sweep missed, or 0 misses are found on the next independent backfill. |
| 1.2 | **Channel downgrade path** — OWED-15, Channel 2 at 5 🔴 with no way down for 19 days | Rule: a channel steps DOWN one mark when the evidence that fired its Upgrade Trigger reverses **on the same instrument for two consecutive prints** AND no new in-channel STRIKES row in 14 days. Channel 2: Bloomberg 4-wk ≥ 3.9 M bpd twice ⇒ 5→4; ≥ 4.1 twice ⇒ 4→3. Channel 1: EA/Kpler monthly runs ≥ 4.5 M bpd two months ⇒ 4→3. Channel 3: the 21-day clock IS the downgrade (kill). Downgrades never below 2 while any Upgrade Trigger's evidence is <30 days old. | Zero capital. Direction: makes marks *easier to lower* — the direction that needs Will's word. Proposal: BRENT/HAWK comment within 7 days, else PROME applies as drafted with the owner-confirm flag (the WQ-176 pattern). |
| 1.3 | **Batch the three routed rulings** | (a) band re-centre WITHDRAWN on the August print; (b) Channel-3 kill letter geography qualifier ("in Black Sea / Azov / Baltic waters or their approaches"); (c) buyer-pullback limb — declare it reachable via insurer/carrier evidence, or retire it as decorative. | Spec text only. All three already in PROME's inbox (9/8); the ask is to put them to Will as one WQ. |
| 1.4 | **Session cadence** | Launch OSPREY **Tuesdays** (Bloomberg print day) and **Fridays** while any channel is 🟠 or 🔴. The August 13-day gap breached the desk's own 7-day rule; two of the three worst misses were found after dark stretches. | Will's operational call. |

## Phase 2 — after the decisions

| # | Item | Depends on |
|---|---|---|
| 2.1 | Integrate the feed into boot steps 5b and 7; run manual + feed in parallel for 4 weeks; record recall in KB. | 1.1 approved and built |
| 2.2 | Write the ruled downgrade text into `CLAUDE.md` EXIT RULES as §1b; back-test against 8/20→today (no ≥3.9 print since 8/2 ⇒ would not have fired — the rule is not trivially loose). | 1.2 ruled |
| 2.3 | Apply (a)-(c) from 1.3 to STATUS/CLAUDE.md as ruled; withdraw OWED-6/30/32. | 1.3 ruled |
| 2.4 | If BRENT's terminal covers the weekly report, register BRENT as the print's owner-of-access and stop the relay searches; if not, 0.1's fallback becomes standing. | BRENT's reply |

## Phase 3 — dated calendar (already in SCRATCH; repeated here so the plan is self-contained)

| Date | Event | Action |
|---|---|---|
| ~9/14 | Palaemon 7-13 Sep bulletin | Channel-3 sweep, bulletin first |
| 9/15 | GATE-OSPREY-001 review (PROME holds) | Apply the WQ-172 window test; input = the 9/8 rung grade |
| ~9/15 | Bloomberg 4-wk to 9/13 | Retry 8/30, 9/6, 9/13 via relays |
| 9/30 | Producers' diesel ban expiry (Res. 1097) | Extension to 10/31 or lapse — OSP-02 forward leg; CARL's route-out |
| 10/1 | Producer-direct exemption date (transcribed) | DOCKET L140 full read with BRENT; Q2 diesel-flow instrument named (KB-082) |
| 10/8–10/15 | OSP-06 resolution window ceiling | A session inside the window is mandatory |
| early Oct | September runs print (EA ~4.2 expected) | Band lower-edge re-derivation trigger, not a re-centre |
| ~10/20 | Arctic/NSR season closing | Vostok Oil volume check (KB-094) |

## What this plan does NOT do
- It does not move any mark, band or threshold — every number change routes through Phase 1.
- It does not touch other desks' files; the export-print access problem is BRENT's to fix, and this desk only registers a fallback for its own read.
