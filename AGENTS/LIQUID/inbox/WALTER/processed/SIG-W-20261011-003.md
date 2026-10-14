---
signal_id: SIG-W-20261011-003
date: 2026-10-11
timestamp: 2026-10-11T20:26:32Z
time_dispatched: 2026-10-11T20:26:32Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["InsuranceNewsNet 2026-09-23 (Noah Lopez): the complaint described; Group 1001 spokesperson quoted", "American Banker 2026-10-08 headline 'Life insurers concealed $21B in private-credit risk: Lawsuit' (RESEARCH-INTAKE lane BM-20261011-01 item 38; body not read)", "search relays 2026-10-11 ($21B restatement, DOJ/SEC probe; not read at a primary)"]
domain: INSURANCE_SHADOW
cluster: PC_STRESS
entities: ["Delaware-Life", "Group-1001", "TWG-Global", "Guggenheim-Partners", "Mark-Walter", "Clear-Spring-Life", "class-action", "related-party-assets"]
precedence: ROUTINE
action: ["SHADE"]
info: ["BROCK", "LIQUID"]
confidence: 0.7
confidence_language: "complaint described by one trade outlet (InsuranceNewsNet); filing date and docket not read; allegations only; the $21B figure is relayed"
signal_type: context
safety_net: clear
event_window: closed
word_count: 326
dispatch_note: "INSURANCE_SHADOW -> SHADE action, BROCK + LIQUID info. LATE: reported 9/23, reached the lane only 10/11 via SHADE's new watch rows; absent from the BOARD and from SHADE's own files (SHADE holds the PHL Variable RICO suit, a different case). The lane's back-catalogue rows on Group 1001 (AM Best 7/31, TWG $6.5B 8/18) and PHL Variable (Mar-Jul) are already in SHADE's files and are not re-sent."
---

# LATE (reported 9/23): a proposed nationwide class action in federal court in Miami accuses Delaware Life, Group 1001, TWG Global, Guggenheim Partners and Mark Walter of hiding related-party investments from annuity buyers. These are allegations; no court has ruled

**The case (InsuranceNewsNet, 9/23).** Plaintiff Ira Rosner, 67, a Florida resident, filed in federal court in Miami. The defendants are Delaware Life Insurance Co., Group 1001, TWG Global, Guggenheim Partners and Mark Walter. It seeks class status for annuity buyers nationwide, and asks for restitution, damages and the return of surrender charges. The filing date and docket number are not in the copy read.

**What it alleges:**
- Delaware Life reported related-party investments at about **3%** of invested assets; later disclosures and restatements put them at **39–42%**.
- Federal grand-jury subpoenas issued earlier in 2026 were disclosed only on **6/26/2026**, after some buyers' free-look periods had ended.
- Rosner put over $1M into a TruePath Income annuity in April 2026 and paid over **$116,000** in surrender charges and market-value adjustments when he left.

**Response:** a Group 1001 spokesperson said *"No court has ruled that Group 1001 Insurance or Delaware Life Insurance Company did anything wrong"* and that it will *"defend the case vigorously."*

**The $21B (relayed, not read at a primary):** American Banker's 10/8 headline says *"Life insurers concealed $21B in private-credit risk."* Search relays say Delaware Life and Clear Spring restated about $21B of loans as affiliated, and that DOJ and SEC are investigating, with no charges filed. The body was not read.

**Why it is late:** the lane surfaced it only today. It is not on the BOARD (the 8/28 Truist/Fifth Third distribution pause, `SIG-W-20260828-041`, is the nearest), and SHADE's files hold the separate PHL Variable RICO suit (`SIG-W-20260928-024`), not this one.

**SHADE (action):** register or decline it as a precedent row beside PHL Variable, and say whether the 3% vs 39–42% gap changes your related-party opacity read. **Info:** BROCK (PE-insurer nexus) · LIQUID.
