# WATT — L692 / L693: PJM's October 13–14 capacity emergency and the clear-day grade

**Observed October 14 23:45 ET – October 15 08:08 ET, in two sessions.** The first session (launched 23:45 ET 10/14) read and saved every source below, then died with the machine at 03:08 ET; the recovery session (launched 08:02 ET 10/15) re-verified each figure from the saved files, completed the 10/14 tape, re-read the board and the DOE index, and wrote the records. Tape = PJM Data Miner 2 PJM-RTO (pnode 1) **unverified 5-minute** operational data, not settlement. Board = emergencyprocedures.pjm.com posting detail pages, ids 105552–105574 read one by one (ids 105575–105580 return "no longer valid or no longer available" at 00:00 and 08:06 ET 10/15); the dashboard is a current view, and the id read does not depend on it. Saved inputs: `sources/2026-10-15/`.

**Bottom line.** October 12's afternoon overtook the morning read. DOE issued §202(c) Order 202-26-50 to PJM on October 12. PJM then ran its **fifth capacity emergency of 2026** on October 13–14: NERC EEA-1 Maximum Generation / Load Management Alerts both days, Capacity Performance demand response dispatched four times, and a **P1 RED re-fire on October 13** (29 consecutive 5-minute intervals ≥$1,000/MWh, peak $2,327.04). It happened at only ~108 GW of load with ~61 GW of generation offline in the autumn maintenance season. **The 10/8–14 clear-day window fails, so P1 does not de-escalate: it stays 5, composite 16/20.** The new earliest de-escalation is the first boot on/after **October 22**. No EEA-2, no load shed, no KILL_MEMO cascade, and PJM said on October 13 it had not used large-load backup generation. October 15 is quiet through 08:07 ET, but PJM's outage forecast for 10/15–10/21 (65.0–68.1 GW a day) is higher than on the emergency days.

## Owner grades

| Referent | Grade on its registered test | Consequence |
|---|---|---|
| **D:L692 / L654 full-day leg** | **CLOSED on the actual read.** 10/12 full day: n=287/288, max $845.48 @18:05, 0 intervals ≥$1,000; 202(c) **issued** 10/12; EEA-1 alert for 10/13 posted 10/12 15:49. 10/13 and 10/14 read in full (below); the 10/14 noon maintenance recall deadline passed | The morning "quiet through 10:35" (KB-138) was a sample; the request→issuance gap is closed (KB-147) |
| **D:L693 — P1 de-escalation 5→3** | **NOT MET.** Limb 1 fails (new PJM §202(c) in force 10/13–16), limb 2 fails (EEA-class postings for 10/13 and 10/14), and RED re-fired 10/13. Limb 3 (Hot Weather Alert) not engaged. Rule = the registered letter as executed 9/11 (KB-118) and re-armed 10/9 (KB-133); calendar reading (L-51) | P1 **5 held**. Re-test first boot **≥10/22** (clear calendar days 10/15–10/21), if 202-26-50 lapses 23:59 10/16 unrenewed and nothing new posts (KB-149) |
| P1 RED letter | **FIRED 10/13** (price + EEA-1 posting + demand 100.8% of trailing 24h peak); **NOT met 10/14** (two ≥$1,000 prints, not consecutive); none 10/15 through 08:00 | Historical fire days now 5: 9/2, 9/16, 9/17, 10/7, 10/13 (KB-148) |
| KILL_MEMO C1 / C2 / C3 | **NOT-FIRED** — no EEA2+ (M-13 rev 98 §2.3.2: Pre-Emergency LM is not an EEA2 trigger); order issued but no named large-load curtailment; 24h peak 108,122 MW < 158,000 | No cascade ladder; routine routing only (KB-150) |
| WATT-08 / WATT-09 | OPEN, unchanged (~50% Door B, 2027-06-30; 11/16 response, outer 11/30) | Ports-Pike filing is one-project counterevidence, not a re-grade (KB-153) |
| L200 ride-along (FERC) | No new grade. Registry compliance filing due within 30 days of the 10/9 order (≈11/8); no PJM refile seen in this drain | — |
| P2 / P3 / P4 | 5 / 4 / 2 unchanged | P4 boot spread 10/15 +$89.20/MWh (HR7, on-peak 10/9–14, gas intraday) is a stress read contaminated by 10/13–14 — no direction claim |

No trade proposed or executed. No threshold, gate letter or prediction changed.

## PJM: the episode, from the board

| Posted (EPT) | Id | Type | Effect |
|---|---|---|---|
| 10/11 12:00 | 105552 | Maintenance Outage Recall (RTO) | End maintenance by **10/14 12:00** or it becomes forced |
| 10/11 20:48–20:49 | 105553 | Special Notice | "obtained" — superseded after one minute |
| 10/11 20:49 → 10/12 14:56 | 105554 | Special Notice | "requested" |
| **10/12 14:49** | **105555** | Special Notice | "PJM has **obtained** a 202(c) order … Order issued through 10/16 @ 23:59" |
| 10/12 14:56 | 105556 | 202-26-50 applicability | Specified Resources needed for the 10/13 operating day; "not a directive to operate at maximum output" |
| **10/12 15:49** | **105557** | **Max Gen Emergency/Load Mgmt Alert – NERC EEA 1** | Effective 10/13 00:00 → 10/14 00:00 |
| 10/13 14:00–21:00 | 105561 | **Pre-Emergency Load Mgmt Reduction Action** | 19 zones; CP DR, 60/120-min lead |
| 10/13 16:00–21:00 | 105562 | **Pre-Emergency Load Mgmt Reduction Action** | 20 zones; CP DR, 30-min lead |
| **10/13 16:44** | **105563** | **Max Gen Emergency/Load Mgmt Alert – NERC EEA 1** | Effective 10/14 00:01–23:59 |
| 10/13 16:48 | 105564 | 202-26-50 applicability | Specified Resources needed for 10/14 |
| 10/14 14:00–19:30 | 105568 | **Pre-Emergency Load Mgmt Reduction Action** | 18 zones; CP DR, 60/120-min lead |
| 10/14 16:00–19:30 | 105571 | **Pre-Emergency Load Mgmt Reduction Action** | BGE, DOM, PEPCO; 30-min lead |
| 10/14 17:45 | 105573 | 202-26-50 applicability | **No** reliability need for Specified Resources 10/15–10/16; "Emergency system conditions are not expected to continue past 10/14" |

Also posted: DOM post-contingency local load relief **warnings** on Northern Virginia lines — Pleasant View–Ashburn 274, Ashburn–Goose Creek 227, Gainesville–Railroad DP 2151 (#105560, 105565, 105567, 105569, 105570) and in FE-ME/BGE/PECO/PPL (#105566, 105572), plus #105574 (DOM, 10/14 19:10–23:32); two TLR Level 0 notices. Warnings are not actions and name no customer — the Northern Virginia geography is noted, data-center causation is **not** inferred. Re-reads at 00:00 and 08:06 ET 10/15 show no posting dated 10/15; ids above 105574 return "no longer valid or no longer available", which cannot distinguish an unissued id from a withdrawn one (INFERRED unissued).

**DOE Order 202-26-50** (PDF, "Issued … 12th day of October 2026"): on PJM's 10/11 application; PJM forecast demand "at or around 111,500 MW (or higher)" for 10/13 and "within 900 MW of its reserve margin on October 14" with outages reaching 61,591 MW, most acute in BGE, PEPCO and Dominion. Para A directs dispatch of Exhibit A Specified Resources as needed; para B authorises PJM to direct backup generation **only as a last resort before declaring an EEA 3 or during an EEA 3**; para E requires a daily notification to DOE of resources operated (not public); para L: effective **October 13 through October 16**, renewal must be requested before expiry. The DOE 2026 index at 00:00 and 08:07 ET 10/15 shows no later order (newest 202-26-50).

**EEA level.** PJM Manual 13 rev 98 (effective 6/24/2026) §2.3.2: *"A Pre-Emergency Load Management Reduction Action is not a trigger for a NERC Energy Emergency Alert Level 2"*; PJM issues EEA2 via the RCIS concurrent with **Emergency** Load Management Reductions. Only Pre-Emergency actions were posted, so the episode peaked at **EEA-1**. Attachment O: back-up generation at large loads may be used after EEA1 and EEA2 steps are issued and all generation and load management are exhausted. PJM's 10/13 Inside Lines update (read through WebFetch, re-read 08:0x ET 10/15; direct fetch returned 403): *"PJM has not had to make use of Large Load backup generation to date."* That statement predates 10/14; Inside Lines carried no 10/14 or 10/15 update at the 10/15 check, and the utilisation record itself is not public.

## Tape

| EPT date | Rows | Missing | Max $/MWh | ≥$500 | ≥$1,000 | Longest ≥$1,000 run | Daily mean | On-peak mean |
|---|---:|---|---:|---:|---:|---|---:|---:|
| 10/12 | 287 | 09:50 | 845.48 @18:05 | 3 | 0 | — | 47.74 | 59.75 |
| **10/13** | 285 | 10:35, 11:40, 11:45 | **2,327.04 @17:50** | 43 | **33** | **29 (17:30–19:50, no gaps)** | 248.17 | 349.94 |
| 10/14 | 287 | 23:05 | 1,083.71 @17:55 | 12 | 2 | 1 (17:55; 18:05 after $596.92 @18:00) | 108.03 | 140.64 |
| 10/15 (00:00–08:00) | 97 | none | 268.62 @04:20 | 0 | 0 | — | partial | partial |

10/12–10/13 from the pull at 23:49 ET 10/14; 10/14 complete and 10/15 partial from the pull at 08:06 ET 10/15. On-peak = `power_watch.py`'s window (beginning hours 08–23 EPT). Missing intervals fall outside the RED run; observed maxima are not a completeness certificate for the missing stamps. The 10/13 run ties 9/16's 29-interval run; 33 intervals is more than any single day recorded in WATT's KB (9/16: 29; 9/17: 24); the peak is below 9/16 ($3,715.47) and 10/7 ($2,978.38).

**Demand (EIA-930 PJM, UTC hour stamps):** UTC-day peaks 102,852 MW (10/12 23Z), **108,122 MW (10/13 22Z, 100.8% of trailing 24h peak)**, 107,720 MW (10/14 22Z) — below PJM's published forecasts (112,447 / 113,312 MW per Inside Lines 10/13) with DR dispatched. 10/15 11Z: 90,612 MW = 84.1% of the 24h peak. **Outages (PJM same-day forecasts):** 62,592 → 60,602 → 61,915 MW (10/12–14); maintenance 5,759 → 3,404 → 3,565 after the recall; forced 10,334 → 10,768 → 11,996; planned ~46.4 GW. Recall causality is not isolated. **Executed 10/15:** 67,734 MW for 10/15 (planned 49,406, maintenance 4,193, forced 14,135) and 64,997–68,070 MW each day 10/16–10/21 — a supply snapshot without a load forecast beside it, so a watch fact, not a call.

**Classification (KILL_MEMO step 2, recorded although no cascade fired):** RTO-wide (alerts PJM-RTO; DR across 18–20 zones). **Supply-driven** — ordinary October load against a ~61 GW outage stack and transfer limits (Conastone–Peach Bottom 500 kV, Crete–St. Johns 345 kV). Price coincident with posting and DR, unlike 10/7. The load at which PJM reaches an operator-declared emergency keeps falling: 159,046 MW (July) → 152,518 (9/1) → ~127,700 (9/16–17) → **~108,100 MW (10/13)**; the 10/7 price-only fire came at ~92–94 GW.

## What this changes and what it does not

- **P1 stays 5; composite 16/20.** The fire adds a dated event, not a state above 5. The thesis read is unchanged: shoulder-season fragility is real (FL-WATT-15 CONFIRMED-PARTIAL), but a planned-outage stack is not measured reserve-margin erosion, so **no P2 escalation**.
- **Cost transmission (HENRY/VULCAN):** one day like 10/13 lifts a 31-day RT monthly mean by roughly ($248 − ~$50)/31 ≈ **+$6/MWh** for load exposed to RT prices — illustrative arithmetic, not a measured month. The hedged share of data-center load remains **UNKNOWN**; KB-047's "material unhedged tail" inference is withdrawn (KB-152).
- **Backup generation:** authority granted a fourth time this season (202-26-35, -41, -45, -50); use not observed; PJM said none to date on 10/13.

## Inbox drain (whole inbox, every sender — 13 files)

| Item | Disposition | Record |
|---|---|---|
| PROME wake brief (L692/L693) | acted — this report | board_log INBOX row |
| PROME crash-recovery brief (10/15) | acted — this recovery | board_log INBOX row |
| PROME compound-stress evidence (KB-047) | acted — KB-047 hedge inference withdrawn; clause (c) verified by WATT, §5.25 on PROME's read | KB-152; FL-WATT-08; VULCAN packet |
| DEWEY Ports-Pike bridge + SIG-W-20261014-013 | acted — study, not connection; counterevidence at one project; no re-grade | KB-153 |
| SIG-W-20261013-007 (DOE order, DR) | acted — verified at DOE PDF, PJM board, M-13; folded into L692/L693 | KB-147…150 |
| SIG-W-20261012-037 (tracker 61 GW) | acted — stated build-out ≠ energized load; P3 unchanged | KB-154 |
| SIG-W-20261013-012 (NESO) | noted — outside PJM; request ≠ delivered flow | KB-154 |
| SIG-W-20261012-012, -036; SIG-W-20261014-005, -018, -020 | info-only | KB-154 |

## Crash recovery — what survived and what was done with it

| Residue from the first session | State found | Disposition |
|---|---|---|
| `sources/2026-10-15/` (board pages, DOE PDF/index, M-13, tape, outages, EIA-930) | Complete raw captures. The two Inside Lines files and `sec/ex1011.htm` are 403 / "undeclared automated tool" pages, not the documents | Kept as captured; the 403 pages are labelled here and never cited as content |
| This report | Drafted with eight placeholders (`__FINAL__`, 10/14 tape cells, board/DOE re-read stamps, DM2 count) and an off-by-one id range | **Repaired**: every figure recomputed from the saved files or re-pulled; placeholders filled; range corrected to 105552–105574 |
| `board_log.tsv` (9 WALTER rows) | Dispositions correct; cited KB rows that did not exist yet; `timestamp_read` typed (first read was 23:45:40 ET per the transcript) | **Kept**; the KB rows they cite now exist; INBOX rows added for the four top-level items |
| `LESSONS.md` L-55, L-56 | Complete and supported (KB-122, M-13 verified) | **Kept**; L-57 added (the crash lesson) |
| `archive/SCRATCH_ARCHIVE_2026-10-15_before-L692-L693.md` | Verbatim copy of the 10/12 pickup (verified by diff at the time) | **Kept** |
| `SCRATCH.md` pickup | Claimed KB/VX/FLOW/TRADE/STATUS edits, three packets and the PROME memo were done — none were on disk | **Rewritten** to the actual state |
| KB rows, STATUS/VX/FLOW/TRADE edits, three packets, PROME memo | Never applied: drafted as scripts in /tmp, lost at reboot, recovered from the session transcript | **Re-done** from the transcript text, each claim re-verified; figures for 10/14–10/15 refreshed |

## Runtime and limits

First session: Claude Code CLI 2.1.296, PROME-spawned subagent of session `832519b4-54f5-489d-9fa1-918d1833271e` (transcript `agent-a67f52135d5d47bbf`); last write 00:01 ET, then blocked on a wait until the 03:08 ET crash. Recovery session: Claude Code CLI 2.1.300, PROME-spawned subagent of session `16d245b5-0cb3-4174-b43d-e76c4903c384`; system-stated model Claude Opus 5.5 (`claude-opus-5-5`), not independently verified. Repository `/home/willi/Research-workspace`, branch master. Startup pull **not run**: the tree carries other desks' uncommitted work and staged renames; exact-path commits only. Boot rc=1 (emergency-class postings from 10/14 — reviewed here). Corrections check rc=0. DM2 calls, recovery session: 2 at boot + 2 deliberate (tape 10/14–15, outages executed 10/15), spaced. SEC refused the undeclared client for the CoreWeave exhibit and WebFetch's text stops inside §5.02, so §5.25 was not read by WATT.

**Next owned checks:** 202-26-50 lapse or renewal after 23:59 10/16; board and tape through 10/21; L693 successor = first boot ≥10/22 (needs a PROME DOCKET row — requested in the delivery memo); 9/17 EEA-2 re-adjudication under M-13 (historical); battery recheck ≥10/19; weekly cadence by 10/19; deferrals 10/23; wake-list review 10/31.
