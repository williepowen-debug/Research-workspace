# BRENT → PROME: 10/1 proxies · Thursday's oil move · COT-35B review · OPEC+ 10/4 · L0 drain

**From:** BRENT (prome-70 Tier-1 due-row spawn, WQ-184) · boot 08:30 ET 2026-10-02 by `date` · desk commit `aae01599b` · evidence: `AGENTS/BRENT/research/2026-10-02_proxies-oil-move-cot/NOTE.md`. **$0. Measurement only. WQ-192 STAND DOWN holds.**

## 1. 10/1 settle-window proxies (OWED, now published)
Source: yfinance 1-min VWAP 14:28–14:29 ET, rows dated 10/01, single vendor. **Proxies, NOT CME settles.**

| Contract | Proxy | Note |
|---|---|---|
| BZZ26 | **102.37** | |
| BZF27 | 98.47 | |
| BZG27 | no bar | |
| CLX26 | **92.94** | |
| CLZ26 | 90.91 | |
| HOX26 | **4.6438** | |
| HOZ26 | 4.4916 | |
| RBX26 | 3.4044 | |
| **Nov ULSD crack** | **$102.10** | |
| **Dec ULSD crack** | **$97.73** | |
| Nov gasoline crack | $50.05 | |
| Dec−Feb | not measurable at the window | +$6.93 on the daily rows |

- **Cross-checks:** the vendor's 10/01 daily rows agree with the proxies to within $0.08. **L462:** a separate 10/02 (evening-session) row exists, so the 10/01 row is the 10/1 day session.
- **Reported settles (Reuters via Yahoo, 15:34 ET 10/1):** Dec Brent **$102.31 (+$4.28, +4.37%)**, WTI **$92.87 (+2.71%)**. Both equal the vendor rows to the cent.
- No CME page was read, and ULSD/RBOB settles were not found.

## 2. Thursday's move
- **Measured 10/1 closes:** USO $150.02 (+3.0%) · VLO $408.46 (+5.4%) · XLE $62.70 (+1.95%).
- **Products split:** RBX26 +4.4%, HOX26 −1.0%. Gasoline led; diesel slipped.
- **Attribution, sourced to the wire:** Reuters names two drivers:
  1. China's product-export halt (Reuters, four sources).
  2. A WSJ report of a third carrier (Theodore Roosevelt + Makin Island ARG) and 9–10k more troops; Trump: *"sign a very fair deal, or they won't exist any longer."*
- **Timing:** the tape (BZZ26 1-min) shows two steps:
  - 02:30–03:15 ET: +$1.93. This fits the China story; Reuters' timestamp was not read.
  - 13:45–13:55 ET: +$1.86. This coincides to the minute with UKMTO 147-26's 13:50 ET report time. WSJ's publication minute was **not found**; the earliest relay I timed is 14:39 ET.
- **⇒ The cause is established at the wire level. The split between the drivers is NOT established.**
- **WALTER's signals:** `-008` (China) explains step 1 and the gasoline/diesel split. `-026` (diesel-reserve pressure) is bearish for diesel, not crude. `-033` (UKMTO 147-26) matches step 2's time.
- ⚠️ **Gap for WALTER/HAWK:** no WALTER signal carries the WSJ carrier/troops report. `-033` §3 has only an OSINT "relief, not addition" reading.
- **10/2 pre-open (vendor, 08:21 ET):** BZZ26 99.73 (−2.5%), WTI 89.65 (−3.5%). The EU energy taskforce meets **today** on diesel stocks (Reuters, two EU diplomats). I registered it as a CATALYSTS row for 10/02.

**Effect on my letters.** Nothing fires.

| Line | Reading | State |
|---|---|---|
| VLO-HELD-01 leg A | $102.10 vs the $90.16 line ($11.94 above); also above the $95 A-notice line. TERRY's source-② daily row for 10/1 now reads **$102.09** (it was $101.70 provisional), so ② and ③ agree to $0.01. **TERRY grades.** | **NOT FIRED** |
| VLO-HELD-01 leg B1 | Federal Register API, public inspection (99 docs) and whitehouse.gov checked 08:34 ET 10/2. `-026` is a conditional, targeted threat, not signed text. | **NOT FIRED** |
| BG-02 | Policy, deployment and a tanker hit are not destroyed capacity. | Nothing to grade |
| Cushing <20.0M re-arm | 24.301M (wk-9/25), 4.30M clear. Next print Wed 10/7. | Not near |
| F-a | +$6.93 | Not crossed |
| **GASREGW** | **$4.465 vs $4.50** (wk-9/28). Thursday's RBOB +4.4% leans toward a cross. Next print ~Mon 10/5. | **Nearest line** |

**Measurement for Will's book:** USO closed $150.02 on 10/1, exactly at the strike of his Oct-09 $150 call. His sell-or-roll window runs to 10/9; the order is his.

## 3. GATE-BRENT-COT-35B (review_by 10/02)
- **Not gradable before 15:30.** At 08:34 ET, `cot_grade.py --expect 2026-09-29` returned NOT FRESH (newest row 9/22). The re-issue watch is clean: the 9/22 row equals the ledger at 121,362 / 1,841,811.
- **Owed reproduction: DONE again at the CFTC archive, 08:33 ET.** I used `fut_disagg_txt_2024–2026.zip`, matched by name, code 067651.
  - 104 weekly OI-shares, 2024-08-13 → 2026-08-04 inclusive: median **4.9086% → 4.909%**.
  - Base (6/16–8/4, n=8): **122,904.5**.
  - ⚠️ **The row's "NOT re-reproduced since 8/13" was already stale.** BRENT also reproduced the figure on 9/18 (REGISTRY COT-FUEL-35B note). **Please drop that ⚠ from the condition cell.**
- **Armed state for the 15:30 print (pre-registered):**
  - **A joint SPENT is practically unreachable.** Leg B would need shorts ≤ ~90,400 at OI ~1.84M, a fall of ~31k in one week.
  - Live outcomes: **NO-VERDICT** if shorts ≤118,325; **NOT-SPENT** if shorts ≥118,326.
  - As-of 9/29, so Thursday's rally is not in this print.
- **Who grades:** the Friday routine fires ~14:00 ET, before the post (exit 3; the structural defect stands). ⇒ **Re-spawn BRENT at ≥15:35 ET today**, or have a live BRENT session grade it before Fri 10/9 so two prints never stack.
- **Proposed review_by:** keep **2026-10-02** for this print. After the grade, move to **2026-10-09** (as-of 10/6). **PROME edits GATES.tsv.**

## 4. OPEC+ Sun 10/4 (L297)
- **What the meeting decides:** a November number only. It is graded on the Secretariat text at opec.org (enter via the root page) within 2 trading days.
- **Pre-meeting sourcing (Bloomberg, two delegates):** a November hold, "no final decision". Most members are still producing below target.
- **My pre-registered read:** outcome (1), a second consecutive hold, is the base case. Only that outcome lets "pause" become a defensible word.
- **Deliverability:** quota is not binding while Gulf exports are disrupted, so even an increment would be mostly paper. Before grading, the spare-capacity figure must be re-pulled at a primary. The Oct STEO lands Tue 10/6.
- **Surprise watch:** an increment with a deliverability claim, or a statement on Gulf export restoration.
- **⇒ A BRENT session is needed Mon 10/5 or Tue 10/6** to grade it.

## 5. L0 drain
- **Census:** top-level 0. WALTER lane: 7 = 7 board_log rows = 7 `git mv`.
- **The two ACTION items:**
  - **`-026` acted.** I recorded the state change (conditional + targeted, still no order). It moves no registered line. The Russia extension was already graded EXTENDED on 10/1.
  - **`-034` acted.** The Paulsboro (165 kb/d) crude-unit turnaround is **not new**: it has been in PBF's plan since at least 7/31 ("late fall, 30–35 days"). No start date has been published. It is not an INCIDENTS row, because that table is damage only.
- **The rest:** `-027` and `-033` noted. `-021`, `-023` and `-031` info-only.
- **`-008` and `-019`** were already dispositioned `acted` on 10/1 at 13:28:05 and sit in `processed/`.

## COMPLETION — BRENT — 2026-10-02
STATUS: ✅ DONE
CHANGED: AGENTS/BRENT/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, demand_destruction/TRACKER.md, research/2026-10-02_proxies-oil-move-cot/NOTE.md, archive/STATUS_dated_2026-10-01_and_09-30.md, archive/STATUS_summary-for-will_2026-10-01_and_09-30.md}, 7 inbox git mv, this memo
RESULT: 10/1 proxies published (Nov ULSD crack $102.10, BZZ26 102.37; Reuters settle $102.31). Thursday's +$4.28 is wire-sourced to the China halt + WSJ carrier/troops report, split NOT established. VLO-HELD-01 A ($11.94 above) and B1 NOT FIRED; nothing fires. COT 4.9086% + base 122,904.5 re-reproduced; 9/29 print armed (SPENT practically unreachable). 7 inbox items drained.
GAPS: COT #8 not graded: it posts 15:30 ET and this session did not wait (per brief). WSJ publication minute and Reuters China-story timestamp not found, so the driver split stays INFERRED. No CME settle page read.
WILL_NEEDS: None (USO Oct-09 $150C sell-or-roll stays his existing call; USO closed at the strike 10/1).
FOLLOW-UP: Re-spawn BRENT ≥15:35 ET today for COT-35B #8; GATES row: drop the stale ⚠ and set review_by 10/09 after the grade; OPEC+ grade Mon 10/5–Tue 10/6; WALTER/HAWK lack the WSJ deployment report.
