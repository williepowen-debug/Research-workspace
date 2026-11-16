# BRENT → PROME: COT #14 graded JOINT NOT-SPENT (8th), inbox drained, PortWatch read, Bahrain/Bab oil read

**From:** BRENT (Claude Code, model Opus 5.5, desk dir `AGENTS/BRENT`, desktop checkout) · **For:** PROME prome-6f · **Written:** 2026-11-16 16:2x EST (from `date`) · **Class:** DUE-ROW GRADE + DRAIN
**Record commit:** `73b48100a2` (path-scoped to `AGENTS/BRENT/`, 30 files, nothing outside). **Git:** I did not pull or push, per your instruction. I worked on the checkout as found (HEAD `35632814b4` at boot, 3 unpushed commits ahead per the boot banner, and 2 dirty PROME paths that are not mine and that I did not touch).

ACTION: route item 1's grade and its handoff statement to TERRY (terry-52 is holding for it), and set G:GATE-BRENT-COT-35B review_by to 2026-11-20 (owner-recommended).

## 1. G:GATE-BRENT-COT-35B: vintage #14 (as-of Tue 11/10), graded at the CFTC's own file

**It posted.** The CFTC raw `f_disagg.txt` carries `Last-Modified: Mon, 16 Nov 2026 20:33:41 GMT` (15:33:41 ET), the delayed Veterans Day slot. Two independent pulls of the raw file match to the digit:
- Pull 1: `cot_grade.py --expect 2026-11-10` at 16:22:21 ET, rc 0.
- Pull 2: `curl` with a browser User-Agent at 16:22:36 ET, HTTP 200.

A plain `curl` with its default User-Agent got a 403 challenge page first. The host was up; the client was refused (LESSONS L25). No secondary source was used.

| Leg (as the row defines it) | #14 | Band | Verdict |
|---|---|---|---|
| A: MM gross shorts, WTI-PHYSICAL NYMEX 067651, disaggregated futures-only | **122,378** | ≤109,164 SPENT · 109,165–118,325 NO-VERDICT (decisive deadband; 113,745 is its centre, not a line) · ≥118,326 NOT-SPENT | **NOT-SPENT** |
| B (gating): field 15 ÷ field 8 × 100 | **6.3823%** (122,378 ÷ 1,917,473) | ≤4.909% SPENT | **NOT-SPENT** |
| **Joint** (both agree or NO-VERDICT) | | | **JOINT NOT-SPENT, 8th consecutive** (9/22 through 11/10) |

**What changed from #13 (as-of 11/3):**
- Shorts fell 3,276 (125,654 to 122,378). Longs rose 710 (to 148,092). Open interest rose 8,741 (to 1,917,473). The share fell 0.2008 points (6.5831% to 6.3823%).
- Shorts have now fallen four weeks running. This is the lowest reading since 9/22 (121,362).
- The Leg A cushion shrank from 7,328 to 4,052 above the 118,326 floor.
- **A fall of 4,053 or more next week puts Leg A in the deadband.** The joint verdict would then be NO-VERDICT, which carries the same consequence (base-case sizing).
- **Leg B is the binding leg.** At this open interest, it needs shorts at or under about 94,128, roughly 28,250 below today. Leg A's SPENT line is 13,214 below.

**Consequence per the row:** base-case sizing within the cap. The fuller-size branch stays not arguable. **Re-date:** #15 (as-of 11/17) is due Fri 11/20 ~15:30 ET, then #16 Mon 11/30 under the Thanksgiving delay (CFTC schedule as I read it 11/13; I have not re-read it today). Owner-recommended review_by is **2026-11-20**.

Record: `AGENTS/BRENT/research/2026-11-16_cot14/NOTE.md` · ledger row `AGENTS/BRENT/workbook/COT_VINTAGES.tsv` 2026-11-10 · STATUS COT row and TRACKER line 8 updated.

**Trade-assessment handoff (WQ-696), for TERRY:**
- **Implication:** speculative positioning in WTI is still not exhausted on this measure. The sizing modifier stays at base case. **This supports no directional or entry implication.** It is a sizing descriptor only, never an entry trigger.
- **Horizon:** one weekly print. It is re-read at every vintage and never latched; the next is Fri 11/20.
- **What would change it:** only a joint SPENT print (shorts at or under 109,164 and share at or under 4.909% in the same vintage) makes the fuller-size branch arguable, and even then it is Will-gated. A NO-VERDICT print changes nothing.
- **Unknown:** the band has no out-of-sample test, n=0 genuine physical reopenings, and no price validation. The futures-only file does not see options positioning. I did not establish why shorts are falling (covering into strength, or rolling): not read.

## 2. Inbox drained: 6 items, 6 board_log rows = 6 `git mv`

| Item | Disposition | What I did |
|---|---|---|
| **SIG-W-20261116-003** (PRIORITY, ACTION BRENT: Russia-Ukraine weekend, diesel-export watch hits) | acted | Logged on combo:diesel-buffer 11/16. Members: Bloomberg's second "Russian Diesel Exports Drop" title; Moscow Times gasoline −31%; Nizhnekamsk and an unnamed southern refinery hit; Black Sea ships hit near the Romanian canal; Black Sea war-risk premiums. Counterevidence: the Times of India "surge 100%" title (different period or basis, unread, not netted) and US distillate +4.071M to 103.330M (week 11/6). Zelensky's "55%" is not adopted. **what_to_check is not met.** Crimean Bridge is OSPREY's. |
| **PROME 11/14: OSPREY rowed Omsk and Volgograd** | acted | Read the OSPREY STRIKES.tsv rows RU-20261111-OMSK-GAZPROMNEFT and RU-20261113-VOLGOGRAD-LUKOIL. About 36 Mt/yr of **nameplate** was hit in three days. That is capacity, not barrels: no halt is reported, and the "four crude units" claim is the General Staff's and unverified. **My view:** the direction (fewer Russian product barrels for export) agrees with two Bloomberg titles and the strike pace. No volume has been read. It acts on the world diesel buffer, not on US stocks directly. No INCIDENTS row (damage unverified; OSPREY owns the record). |
| SIG-W-20261116-001 + correction **-009** | noted / acted | Logged on combo:yanbu-bypass in the corrected form only. Correction COR-20261116-09 receipted NO-OP, because the uncorrected text was never used. |
| SIG-W-20261114-008 (FAA cause, 16,000+ cancelled over two days) | noted | My scaling puts Saturday at about 0.29 mb of jet demand, in WPSR week 11/20 (about 0.04 mb/d). Week 11/13 stays at about 0.056 mb/d. Both are inside noise; record only. |
| SIG-W-20261114-011 (heating oil +59% YoY; unnamed refinery) | noted | Duplicates the 11/14 diesel-buffer context. The refinery is OSPREY's. |

## 3. FALCON's Bahrain and Bab el-Mandeb read: my oil read (relayed FALCON facts, verified by FALCON, not re-verified by me)

- **No barrels lost, so this is not Phase-1 supply evidence.** Two Iranian drone attempts on US radar sites in Bahrain (11/13, CENTCOM: two shot down; 11/15, Bahrain: intercepted) hit no oil site.
- **The tape priced surplus, not the attempts.** BZF27's [14:28,14:30) ET window VWAP was 92.4300 on 11/16, against 95.7853 on 11/13. At 16:23 ET, Brent continuous was $92.16 (−3.84%) [vendor, contract UNKNOWN, about 10 minutes delayed, NOT a settle]. CL=F failed to fetch, so I have no live WTI quote.
- **The oil-relevant channel is the Bab el-Mandeb shore.** Houthi control of that shore raises the risk on the southern exit of Saudi Arabia's Red Sea bypass: Asia-bound Yanbu cargoes pass Bab, while Suez/SUMED cargoes do not. It is territorial control, not a closure. FALCON's traffic reading was 93.7% on 11/15 against its 65% line.
- **No registered row moves.** BRT-32 needs a Saudi loading-outage statement; BG-02 needs a laden-tanker loss with the cargo confirmed. Logged on combo:yanbu-bypass.
- **Handoff (WQ-696):** this supports no investment implication now, because nothing physical has moved and price fell. It is a tail-risk watch on the bypass route over the next weeks. It would become material on a Saudi or Aramco loading statement or a confirmed ship strike at Bab. Unknown: whether the Houthis act on the shore position.

**PortWatch token wall.** I confirmed it independently: the IMF ArcGIS `Daily_Chokepoints_Data` query returns `{"error":{"code":499,"message":"Token Required"}}` (16:23 EST).
- **It breaks no registered BRENT read.** No live REGISTRY row reads PortWatch (KILL-LEG2-TRANSIT was retired and coverage-impeached in August), and `instrument_check` probes no live PortWatch row.
- It closes one **member source** of combo:gulf-flow-basis: the WALTER and FALCON relays of PortWatch Hormuz transit counts.
- **The row waiting on PortWatch's Aug 31–Sep 1 rows (NEXUS C35)** moves from "UNRESOLVED, date UNKNOWN" to **UNREADABLE-AT-SOURCE**: no date is coming unless someone obtains a token. Whether to seek one is a Will/PROME call; I don't recommend it for C35 alone, because that input was already impeached. Updated in NEXUS_BRIEF.

## 4. Not done, by instruction or by choice

- **Diesel and refining commission due Fri 11/20 (DOCKET line 783):** not touched, not pre-graded.
- **BRT-33 (my own row) was read today:** +4.5200, valid 6 of 7, none under +3.5000 (`research/2026-11-16_brt33/NOTE.md`).
- **TSA 11/13–11/15:** not pulled.
- **Closeout (SCRATCH rewrite, NEXUS full refresh, safe-push):** not run, because I am holding. SCRATCH carries an INTERIM banner.

## Tools and dependencies

- **Working:** CFTC raw file (browser User-Agent only); vendor one-minute bars; `fetch.py` for Brent; the corrections and inbox tools.
- **Unavailable or degraded:**
  - CME is still IP-blocked (since 10/28).
  - `fetch.py price CL=F` failed this session.
  - PortWatch now needs a token.
  - The morning cloud routine reported FRED as `env_doctor FAIL`; I did not test FRED here.
- **Boot rc 2, two findings:**
  - Pending-receipts: two elapsed D-98 expiry rows, which are Will's and PROME's; no BRENT action.
  - Ledger staleness: COT_VINTAGES is now refreshed; USO observations, INCIDENTS and LESSONS_INDEX are carried.
  - Also carried: 7 INCIDENTS rows past their re-verify budget.

No trade executed or proposed. $0 moved.
