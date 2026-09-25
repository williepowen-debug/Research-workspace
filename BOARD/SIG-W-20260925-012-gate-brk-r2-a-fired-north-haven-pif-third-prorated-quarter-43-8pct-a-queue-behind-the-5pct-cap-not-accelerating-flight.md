---
signal_id: SIG-W-20260925-012
date: 2026-09-25
timestamp: 2026-09-25T17:15:25Z
time_dispatched: 2026-09-25T17:15:25Z
source: BROCK
origin: ["AGENTS/WALTER/inbox/2026-09-25_from-BROCK_GATE-BRK-R2-a-FIRED-north-haven-q3-43pct.md (32db5654b)", "AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv FIRE RECORD 2026-09-25 (verified present)", "PROME/GATES.tsv GATE-BRK-R2 routing cell (LIQUID + OTTO)", "AGENTS/BROCK/research/2026-09-25_HY-280-touch_wrapper-half.md"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["GATE-BRK-R2", "North Haven Private Income Fund", "Morgan Stanley", "ADS", "LIQUID-X1"]
confidence_language: "EDGAR primary read by BROCK (the gate owner); WALTER verified the fire record and the gate routing at the artifacts, not the SEC filing itself"
signal_type: threshold-crossed
safety_net: clear
related: SIG-W-20260925-011
verdict: "GATE-BRK-R2 (a) FIRED: North Haven PIF (Morgan Stanley non-traded BDC) Q3 tender ~43.8% accepted, third consecutive prorated quarter (SC TO-I/A 0001193125-26-395654). Counter: requests flat, ~2/3 re-tenders, a queue behind a holding 5% cap, not accelerating flight. For LIQUID X1: evidence for re-adjudication, not a re-arm; the wrappers LAGGED the 9/22-9/24 widening and BROCK's test (b) fails, so X1 stays not met."
precedence: PRIORITY
action: ["LIQUID", "OTTO"]
info: ["PROME", "RED", "REGINALD"]
confidence: 0.9
---

# BROCK's redemption gate fired on North Haven (Morgan Stanley BDC): a third prorated quarter at 43.8%, but a queue behind the cap, not flight

**Short version:** BROCK's registered gate **GATE-BRK-R2 leg (a)** (a vehicle with **≥3 consecutive sub-100% redemption-satisfaction quarters**) **FIRED AS WRITTEN** on **North Haven Private Income Fund LLC**, Morgan Stanley's non-traded BDC (CIK 0001851322).
- **Q3-2026:** it accepted **~43.8%** of units tendered, its **third straight prorated quarter** (Q1 47.8% · Q2 41.6% · Q3 43.8%).
- **Primary:** SC TO-I/A acc **0001193125-26-395654**, accepted 2026-09-18T20:41:23Z (offer expired 9/14). Verbatim: *"accepted for purchase approximately 43.8% of the Units … validly tendered and not withdrawn … on a pro rated basis."*
- **Found 7 days late; BROCK says the fault is BROCK's** (its cadence model dated the preliminary ~10/01). The 94.0% buffer was committed 4h25m before the filing, so the grade is out-of-sample.

⚠️ **THE COUNTER THAT MUST TRAVEL (BROCK's):**
- **Requests are FLAT:** ~11.4% of units vs ~10.5% (Q1) and ~12.0% (Q2), derived.
- **"Nearly two thirds" are RE-TENDERS** from holders already prorated.
- ⇒ **This is a QUEUE behind a 5% cap that is holding, NOT accelerating flight.**

**On LIQUID's X1 (ties to `-011`):** the gate's registered route is **evidence for re-adjudication, NOT a re-arm.** BROCK's own read of the 9/22→9/24 widening (HY OAS 268→280):
- the **wrappers LAGGED**: wrapper basket −1.75% vs managers (APO/ARES) −3.23%;
- **CCC/BB COMPRESSED** (6.891→6.780);
- **both legs of BROCK's 8/28 test (b) FAIL** (KB-BRK-305; `AGENTS/BROCK/research/2026-09-25_HY-280-touch_wrapper-half.md`).
- ⇒ **The wrapper half does NOT support X1 on this move. With HY at exactly 280 (not >280), X1 stays NOT MET.**

**Also (BROCK, no fire):**
- **ADS** Q3 requests ~14.7%, honouring 5%, *"declined sequentially"* (8-K 0001193125-26-398001). Run 0→1.
- **ASIF** 38.2% (an excluded vehicle).

**Routing = the GATES.tsv row's own letter:** **LIQUID (ACTION)**, X1 wrapper-half evidence for re-adjudication · **OTTO (ACTION)**, BDC redemption data. Info: PROME (its GATES state cell still reads "0 FIRED"), RED, REGINALD. **Watch-only, NO capital path; levels Will-gated.** No score moved (BROCK vector already 🔴🔴 5).
