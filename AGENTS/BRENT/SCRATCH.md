# BRENT SCRATCH — September 28, 2026 (Monday; brent-d2 PM leg, Will-directed 16:22 ET; closeout written 17:12 ET by `date`)

*Two sessions ran today. The earlier leg (14:34–15:54 ET) is recorded in STATUS § September 28 (live, 14:34) and in commits `ebc3fb7c7` … `2c13f086c`. Its still-open items are carried below.*

## CHANGES SINCE LAST SESSION (15:54 → 16:22 ET, plus what the earlier leg missed)
- **Trump on record Sun 9/27 17:55 EDT** (Fox, Presidents Cup; Bloomberg/Yahoo, read at the page): a US diesel export ban is under consideration, *"we're looking at it very seriously — we may do it."* The earlier leg didn't have this.
- **White House (anonymous official), Mon 9/28 15:53 (Yahoo):** "No policy decision has been made."
- **Wright (UN):** "avoid a blunt hammer"; voluntary curbs.
- **WALTER -008** (Marines injured 9/14; IRGC's 19-ship claim) and **-010** (SPR; Goldman's ban scenario) landed. WALTER withdrew -010 (A) itself at 20:09Z.

## WHAT I DID THIS SESSION
- **Boot** rc=2, the standing set: TRADE.md, INCIDENTS and COT_VINTAGES stamps stale; ledger nudge. Corrections rc=0.
- **Post-settle tape 16:12:**
  - BZX26 105.72 · HOX26 +1.5% · RBX26 −0.8% · NG −2.7%.
  - Matched cracks: Nov ULSD $97.33 / Dec $95.91 · Nov gasoline $39.93 · BZ Nov−Dec +$7.51.
  - EIA retail wk-9/28 was NOT published at 16:25.
- **Export-ban risk read:** [note](research/2026-09-28_us-diesel-export-ban-risk.md) plus [source file](research/2026-09-28_us-diesel-export-ban_source-research.md), written by an Opus subagent; I re-read the key quotes at the page.
  - Exports ≈ 30% of distillate output.
  - [EST] Gulf Coast storage full ~2–5 weeks after a ban.
  - Direction: a ban weakens US diesel against crude (F1 cushion $1.23) and later strengthens gasoline (#6).
  - **Breach timings WITHDRAWN ~17:3x after CATO MR19** (relayed by PROME): they came from ×42 on Goldman's retail scenario. They're recast as sensitivities in note §3. Corrections are appended to both packets.
- **Packets (committed):**
  - WALTER `6691e5661`: answer to -010 (B); doorbelled, since walter-f8 is live.
  - TERRY `4f92f6a15`: card input. TERRY is DARK and the packet carries no ASK, so rule 6b doesn't fire; TERRY reads it at next boot.
- **Rotations (verbatim, crc checked):**
  - STATUS 9/25 PM block → `archive/STATUS_dated_2026-09-25_PM.md` (1,927 B, `349f7392`).
  - NEXUS 11 rows → `archive/NEXUS_BRIEF_rows_2026-09-10_to_09-23.md` (4,196 B, `e785caa2`).
- **Inbox:** -008 noted, -010 acted; both are in board_log and `git mv`'d.
- **$0. No trade, band, grade or thesis change.**

## ⚠️ MY ERRORS / NEAR-MISSES
- **The earlier leg's 15:26 news sweep missed Trump's Sunday on-record remark.** Its SUMMARY said nothing about a ban. The ban was already in my own L477 note (9/25) as decoupling mechanism #2, so the sweep never re-searched it. A known risk named in a note is not a monitored risk.
- **I multiplied a RETAIL scenario by 42 and published breach timings for FUTURES cracks** (note §3, both packets, STATUS, NEXUS; CATO MR19 caught it). ×42 converts units, not instruments; retail carries crude, distribution and taxes. Same class as [[finding_instrument_measures_a_superset_of_the_thesis_subject]]: the named series is real but isn't the subject. Before deriving a date against a registered line, name the instrument the source's number is ON.

## NEXT SESSION (dated, future-verifiable)
1. **Tue 9/29:** last BZX26 GRADED settle (the REGISTRY rule grades Nov through the session before last trade; ICE Nov last trade is Wed 9/30). HENRY's blind BRT-12 verdict is due.
2. **Wed 9/30 ~10:30:**
   - Grade **BRT-29** (T ≤7,555 kb/d) and **BRT-12** (8/13 rule). PREP: `setups/2026-09-25_Q3-predictions-grade-PREP.md`.
   - **Also read distillate exports wk-9/25** against 1,331 kb/d (4-wk 1,559). A sharp drop is consistent with a voluntary curb but doesn't prove one: look for a multi-week pattern plus refiner statements. DOCKET L531 points here.
   - BZZ26 becomes the graded month.
   - Russia's producer diesel ban expires; read the decree.
3. **Any day:** an export-ban executive order. That is an IMMEDIATE read of F1, HEN-46 and boundary #6, with packets to TERRY, HENRY and WALTER.
4. **Read the EIA retail print wk-9/28** (it wasn't out at 16:25 9/28). Regular was $4.478 against the $4.50 line.
5. **Fri 10/2:** COT #8. **Sun 10/4:** OPEC+. **~Mon 10/5:** Aramco Nov OSP. **Tue 10/6:** L471 sitting. **Sat 10/24:** WQ-264 shadow run ends.
6. **Rotate:**
   - STATUS is still at **91%** (29,589 B). The rule-5 stop is <70%, so rotate the 9/28 14:34 block's detail once 9/30 supersedes it.
   - NEXUS is at 29,966 B (92%). Its VIEW section is 9/10 vintage and stale: rewrite it.
   - TRADE.md is at 81% and 12 days stale.

## OPEN THREADS / WATCHES
- 🔴 **US diesel export ban:** policy unset.
  - Refiners' response to voluntary curbs is the biggest unknown.
  - Legal route: IEEPA plus an executive order, per the researcher; not counsel-verified.
- 🔴 **Yanbu:** restart REPORTED (Bloomberg, anonymous; ~3.5 mb/d Petroline). No operator figure.
- 🟠 **INCIDENTS owed:** Novoshakhtinsk 9/25 (new row), Ilsky 9/26 (update RF-050), OSPREY's Kuibyshev/Ufa. 11 ACTIVE rows past 60 days.
- 🟠 **Energy credit leg:** HY OAS 293 (9/25) belongs to LIQUID.
- 🟠 **USO Sep-16 165C disposition:** Will's (WQ-169). TRADE.md rotation offer is unanswered.
- 🟡 **Data gaps:** CME settlements are blocked on this box. ICE gasoil is not in the kit, so the HO−gasoil spread can't be measured.
- 🟡 **COT-FUEL-35B `last_verified`:** hand stamp 9/06, left deliberately.

## POSITION DECISIONS PENDING
- **None new.** USO 37 sh (USO $150.01 at the 9/28 close, yfinance). VLO 1 held (fill $412.00; $389.57 on 9/28, −5.4%) + 2 staged (TERRY/Will). WQ-192 stand-down holds.
- The ban risk goes to TERRY as card input only.

## MAIL STATE
- **Inbox:** clear. 5 consumed today = 5 board_log rows. -003 remains deferred, with its row.
- **Sent:** WALTER (-010 B answer, doorbelled) · TERRY (card input). Outbox: no open packets.
