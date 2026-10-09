# RED → PROME — FT-02 count, weight re-derivation, inbox drain (S51, prome-75)

**Written:** 2026-10-09 10:35 EDT (`date`). Tier-1 spawn on Will's word 10:24 ET. Runtime: Claude Code, model Opus 5.5 (claude-opus-5-5), cwd inherited from PROME; root CLAUDE.md, AGENTS.md, USER.md and `AGENTS/RED/CLAUDE.md` read explicitly. **No pull at boot**: the tree carried other desks' uncommitted work (DAEDALUS, BRENT, WALTER, then ORACLE/ZHAO/REGINALD/LIQUID, including ORACLE's staged renames in the shared index). Every RED commit is pathspec-only.

## 1. FT-02 (HY OAS >320, sustain 3): 0 of 3, NOT FIRED

**Basis:** the registry letter is FRED BAMLH0A0HYM2, percent ×100, with the **observation date** governing the count. It pins **no vintage**. RED's practice is the value as pulled, i.e. latest-revised. **For this grade the question is moot:** `fetch.py fred BAMLH0A0HYM2 --first-published` (output_type 4) returns the identical value on every cell 9/30–10/8, with `short=false` and `missing=[]`. Pinning a vintage would be a basis amendment, so it goes to the CHG-051 spec review on 10/31 and is not done here.

| Obs | 9/30 | **10/1** | 10/2 | 10/5 | 10/6 | 10/7 | **10/8** |
|---|---|---|---|---|---|---|---|
| bps (first-pub = latest) | 312 | **324** | 310 | 312 | 303 | 309 | **315** |
| run | 0 | **1** | reset 0 | 0 | 0 | 0 | **0** |

- **One cell printed above 320 (10/1, 324).** The sustain count reached 1 of 3 and 310 on 10/2 reset it. **The count today is 0 of 3, 5bp away.** This matches the HEARTBEAT sequence and WALTER's 1-of-3 on 10/1.
- Composition 9/30→10/8: BB 194→194 · B 316→315 · **CCC 1,179→1,252 (+73)** · IG 84→82. Since 9/30 the index has moved only on the CCC tail, not on breadth.
- REG-T-03 is not merged. RED grades and does not size. Recorded in the registry FT-02 `state` / `state_detail`, with ML-RED-278.

## 2. Weight re-derivation, owed by 10/09: DONE on today's tape

**Net-bear 58 → 60 (+2, all discretionary and labelled). Confidence 70 unchanged** (no registered CONF leg fired). New weights: **Managed 31 · Stag 32 · Acute 14 · War 14 · Soft 5 · Rescue 4.**

| Move | Evidence named |
|---|---|
| **Acute +1** | The real-rate leg, **counted once** across rates, banks and HY (one antecedent). DFII10 rose +51bp from 9/3 and **held 2.88–2.95 for 7 sessions** (2.92 [10/7]). KRE −7.6% · WAL −8.6% · OZK −11.2% since 9/3. This is **not** the credit leg: FT-02 keeps its own +3 and is not pre-empted. |
| **War +1** | Yanbu struck 10/1, a new Hormuz tanker hit 10/2 (WALTER SIG-W-20261002-014/-016/-018). **Dated Brent 135.51 [10/2], 125.44 [10/6]** vs paper ~$104. ⚠️ Both counter-witnesses are named: paper is flat and OVX fell 52 → 48, which is why this is +1 and not more. |
| **Soft −1** | The 10/2 NFP band, pre-committed on 10/01: its **bear branch was MET** (LFPR 61.6→61.8 *with* U-3 4.1→4.2). 3-mo +50.67K (FRED PAYEMS reproduces LABOR exactly); Jul+Aug revised −60K. ⚠️ The band set a direction but **no magnitude**, so −1 is discretionary (ML-RED-277). |
| **Stag held** | Wages decelerated (AHE 3-mo 2.36%) while physical oil spiked. Its registered test is 10/14 + 11/10, and it is not pre-empted. |

The symmetry test and the re-steelmanned bull case are in the derivation file. The bull keeps 5y5y 2.33, VIX 15.4, IG tightening and claims at 197K.

**10/14 CPI tree (S50c): CONFIRMED, STANDS.** CPILFESL Jun/Jul/Aug are unrevised, and the Cleveland nowcast is still core +0.20 (stamp 10/09; unchanged since 10/01, so it is not a fresh witness). Per the tree's own pre-registered line, a fire applies +3 to the re-derived weights → **net-bear 60 → 63** (the tree's "→61" was written on the 58 base).

## 3. Whole-inbox drain: 6 top-level + 2 WALTER/ (census 10:24), all dispositioned in `board_log.tsv` and moved to `processed/`

| Packet | Disposition |
|---|---|
| LABOR 10/2 NFP revisions | acted: verified at FRED; it fed the Soft move; VX-RED-001 re-measured (bull 50→45) |
| BOND F2 10/1 + 10/8 | acted: both OFF-THE-RUN (0.00%); FT-11 v1.1 off-the-run branch; FT-11 precondition Δ5(DGS30) = **+3.0bp** [10/7] = clear, not met |
| DAEDALUS L546 float tie | **done**: `base_rate_review.flag()` rounds before comparing; new `test_base_rate_flag.py` passes 9/9 and fails exactly the two tie cases on the pre-fix code (IMPLEMENTED + TESTED, not independently verified) |
| DAEDALUS prose-remedy | item 2 **done** (W1 names `wc -l` + `read_cap_check.py`); item 1 **deferred, dated** → CHG-051 review **10/31**; both answered in STATUS |
| DAEDALUS wiring-17 | **done**: VX-RED-002 Flip_If names AHETPI−CPIAUCSL; VX-RED-001 is declared OR (no current grade moves) |
| WALTER SIG-…1002-005 | acted: the FT-02 grade above |
| WALTER SIG-…1008-033 (WQ-399) | acted: the receipt line in the RED charter is updated (C4 own-charter edit) |

**Corrections:** 23 named rows had built up unreceipted, and all are now receipted in the WQ-399 form (22 NO-OP with scope · 1 APPLIED, COR-20260906-03 → ML-RED-225/186); `corrections_boot_check RED` rc 0. ⚠️ The 21 generic NO-OPs rest on a grep of RED's live surfaces for each correction's subject. **The 21 BOARD bodies were not read in full.**

**Commits:** `79adf41e3` (RED S51 work) plus the commit carrying this memo and a stamp fix (see the SendMessage for the sha and push receipt).

## COMPLETION — RED — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/RED/{STATUS,SCRATCH,CALENDAR,OUTBOX,NEXUS_BRIEF,MAINTENANCE,CLAUDE}.md, thesis/CHANGELOG.md, docket/CATALYSTS.tsv, registry/{FALSIFICATION_TRIGGERS,_SCAN,corrections_receipts}.tsv, workbook/{ML,VX,VX_HISTORY}.tsv, board_log.tsv, scripts/base_rate_review.py, scripts/test_base_rate_flag.py (new), reports/2026-10-09_S51_{weight_rederivation,status_header_folded}.md (new), 8 inbox→processed moves; this memo
RESULT: FT-02 is 0 of 3 at the 10/8 obs, not fired. One cell (324, 10/1) printed above 320 and 10/2 reset the run. First-published = latest-revised on every cell. Weights re-derived: net-bear 58→60 (Acute +1 real-rate once, War +1 Yanbu/Hormuz/Dated $135, Soft −1 NFP band), all discretionary; confidence 70. The 10/14 CPI tree stands, and a fire now → 63. Inbox 6+2 drained; 23 correction receipts filed.
GAPS: FT-02's registry letter pins no vintage (→ CHG-051 review 10/31). The 21 NO-OP correction receipts rest on a grep of RED's surfaces, not on reading each body. Boot 1.5 b3/b4 BOARD read not run. KB/VX/TIMELINE/FLOW review debt carried.
WILL_NEEDS: None
FOLLOW-UP: 10/14 08:30 CPI: RED grades FT-08 off the tree (needs a spawn at the print). FT-02 is a daily T+1 count, 5bp away.
