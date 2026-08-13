# SHADE → PROME · private-credit grouping session, 2026-08-13

**Session:** real-SHADE, first since 7/27 (17-day gap; proxies 8/3–8/4). Markets open, ~12:40–13:40 ET.
**Discipline:** every figure below is primary-verified or explicitly marked otherwise. ⚠️ **This memo was amended after PROME caught a false claim in it — see §3.2.** **No band, threshold or confidence was moved.** Both grades ran on frozen letters. The one instrument-design change identified is **flagged here, not executed.**

---

## 1. Ranked-task results

| # | Task | Result |
|---|---|---|
| 1 | **M-11 leg-1 refresh** | ✅ **GRADED — STABLE.** The instrument published **today** (8-K `0001527469-26-000063`, Item 7.01). Peer penalty **+44.7 → +33.0bp like-for-like: NARROWED 11.7bp.** Also graded **Egan-Jones 8/12** (item ③): **RESOLVED, ladder NOT advanced.** |
| 2 | **M-11 leg-2 FINAL** | ✅ **GRADED — PARTIAL**, Δ **+$6,897M**, short of LANDED by **$103M**. 10-Q `0001527469-26-000056` (filed 8/10). **Packet delivered to CREED; the two desks reconciled to ONE figure.** |
| 3 | **Re-verify 3 carried figures** | ✅ **ALL THREE VERIFIED EXACT.** The 8/4 flag was a **search failure**, not a disclosure gap. |
| 4 | **HY OAS sign-leg re-read** | ✅ **COMPLETE. Level leg DEAD** (8 sessions <280bp) **AND sign leg re-read on closes: NOT MET** — 8/3→8/12 wrappers **+5.95%** vs managers **+4.91%**, both strongly UP. ⚠️ **My "no closes tooling" claim was FALSE and is struck** — see §3. |
| 5 | **Inbox drain** | ✅ **Both lanes CLEAN**, 4 processed. BROCK packet delivered (wrapper angle only; no disposition written). |

## 2. The two verdicts you asked to lead with

**LEG 1 — STABLE, decisively, and it is a clean NEGATIVE for SHADE's own kill-path-1.**
Athene **T+123 → T+110** (−13bp) vs like-for-like peers **−1.3bp** ⇒ ~11.7bp is **Athene-specific outperformance**, not FABN beta. Band ≤+48bp; the reading is +33.0 (like-for-like) / +30.0 (as published). ✅ The registered **+43–48bp** baseline **reproduces exactly**, confirming it as Athene's own arithmetic. **Kill-path-1 stays YELLOW** (RED bar >250bp — 140bp away). The withdrawn *"widening ~+15bp"* claim is now **actively contradicted**, not merely untested. ⚠️ **Athene added LNC to its own peer set** (widest peer) — flatters by 3.0bp; immaterial to the band, but it is the fifth instance of SHADE's **allocation-discretion** through-line. ⚠️ **The deck's RBC row is stale in both editions (fn.5 = 12/31/25) — 441% is not a 6/30/26 figure.**

**LEG 2 — PARTIAL by $103M, and the verdict turns on the card's own input error, not the print.**
The Q2 10-Q prices the deal for the first time: ***"we completed the purchase… including accrued interest, for $8.7 billion"* — not $9.0B** (that was the *commitment* amount). The frozen $7.0B floor was derived as *"78% of $9B"*. Against the actual size, **78% × $8.7B = $6.786B and Δ = 79.3%** ⇒ **the letter reads PARTIAL, the floor's stated intent reads LANDED.** **I graded the letter and did not move the band.** ⚠️ **"PARTIAL" must not propagate as "the assets didn't show up" — 79% of the book is in the registered line.**

## 3. 🚩 ONE ask for you — flagged, not executed *(the second is withdrawn; it was my error)*

1. **Kill-path-1 needs a supply-adjusted companion instrument.** The peer penalty tightened in the same six months FABN issuance collapsed ($2.0B → ~$1.2B) and the program shrank. **A secondary spread is a price on a float; withdrawing supply supports it.** SHADE's price-only canary **cannot separate "credit improved" from "the issuer stopped issuing."** This is an **instrument-design change** → report-before-execute. **Not taken.** Detail + three named discriminators: `research/ATHENE_FUNDING_MIX_ENCUMBRANCE_SHIFT_2026-08-13.md` §3.
2. ~~**Tooling: SHADE cannot grade its own sign leg.**~~ ❌ **WITHDRAWN — THE CLAIM WAS FALSE AND IT WAS MINE.** `fetch.py price <TICKER> --history N` was in the tool's own usage line all along. I invoked `fetch.py history <TICKER>` (wrong syntax), grepped subcommand dispatch, saw only `price`/`prices`/`fred`, and **declared the capability absent rather than reading the usage block.** `finding_unfetched_is_not_unavailable` — **un-invoked is not unavailable**, and a false *unavailable* claim propagates into other agents' plans. Caught by PROME within the hour. **Sign leg now graded (§1 task 4). No tooling ask stands.**

## 4. What Will should know
- **Two SHADE claims died today and both are recorded as losses**, not reframed: the FABN penalty **narrowed** when the thesis expects widening; and the HY OAS level leg that went live on 8/4 **had been dead since 8/3** — nine days carried un-re-read.
- **Nothing is closer to a trade.** Trigger back to **zero legs**, dig **holstered**, kill-path-1 **YELLOW**, kill-path-3 **not advanced**.
- 🟠 **One new lead worth a session:** Egan-Jones was reportedly **dropped from the Bermuda Monetary Authority's capital & solvency handbook for insurers** (media-only, unverified). **BMA recognition revocation is a registered SHADE domain item and bites the insurer capital channel directly** — unlike the ABS/government denial that actually happened on 8/12.

---

## COMPLETION

**STATUS:** COMPLETE — all 5 ranked tasks executed, task 4 now fully (sign leg graded on closes); 1 item flagged to PROME, not executed; 1 false claim of mine retracted across 5 surfaces.
**CHANGED:** `2026-08-04_athene-q2-m11-grade-card.md` (§7 FINAL grades) · `STATUS.md` (§0i, stamp, §0d retired) · `SCRATCH.md` · `board_log.tsv` (+7) · `NEXUS_BRIEF.md` · `research/ATHENE_FUNDING_MIX_ENCUMBRANCE_SHIFT_2026-08-13.md` (new) · packets to CREED, NEXUS, BROCK.
**RESULT:** Leg 1 **STABLE** — peer penalty **+44.7 → +33.0bp**, narrowed **11.7bp**; Athene **T+123 → T+110**. Leg 2 **PARTIAL** — Δ **+$6,897M**, **$103M** short of the $7.0B floor; deal repriced **$9.0B → $8.7B**. Egan-Jones **denied** (`34-106092`), **not revoked** — ladder stays 🟢. HY OAS **8 sessions <280bp** AND sign leg on closes **8/3→8/12 wrappers +5.95% vs managers +4.91%, both UP** ⇒ **both legs fail, trigger back to zero legs**; on both down-days the **managers** led down (3-for-3). Item ⑤ **3/3 verified exact**. Funding mix: secured **+$9.4B** vs unsecured **−$0.7B** in 6mo.
**GAPS:** Apollo Q2 10-Q RS cross-check not run · BMA de-recognition media-only · encumbrance not sized · STATUS at 420 lines vs the ~250 cap. *(Former gap "sign leg unread — no tooling" is RETRACTED: the tooling existed, I mis-invoked it; leg now graded NOT MET.)*
**WILL_NEEDS:** Nothing to decide. Two SHADE claims died today; nothing moved closer to a trade.
**FOLLOW-UP:** ① primary BMA pull ② Apollo RS segment ③ STATUS compression ④ PROME: supply-adjusted canary (held for Will's batch, do NOT build) ⑤ MBA Q2 ~mid-Sept for the joint 006/010 verdict.

---

# ADDENDUM — RULED BATCH EXECUTED, 2026-08-13 ~18:35 ET

**Authority:** `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` ③ + ④ — cited, not reconstructed. Both executed in the resident session. **No band, threshold, kill-line, vector or confidence moved.**

## ③ Supply-adjusted canary — BUILT, REGISTERED, NOT GRADED
`instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md`. All four ruled constraints honoured and **restated inside the spec** so they survive the file being read alone: companion-not-replacement (price canary **+33.0bp**, kill-path-1 **YELLOW** untouched) · **no band or kill-line moved in the build commit** · spec pre-registered **before** first graded reading · and I added one the ruling implied — **it cannot by itself move kill-path-1 to RED.**

**S1** issuance (10-Q MD&A only) · **S2** unsecured share of funding-agreement stock · **S3** public-syndication recency.
**Frozen baseline:** $2.0B → **~$1.2B** · 40.7% → 38.2% → **36.2%** · **~11 months**. All three one direction ⇒ Q2-26 sits in **(B) supply-withdrawn**, **ungraded**. **First graded reading Q3-2026**, incomplete until *both* the 10-Q and the FI deck land.

⚠️ **One design choice you should see, since it is a deviation from how SHADE usually ships an instrument: no numeric bands in v1.** Two quarters of S1/S2 cannot base-rate a threshold, and a band written now would be fitted to the only data in existence. Bands register after **≥4 quarters** as a dated re-spec, never after seeing the quarter they would grade. **Not a defect in the approved design — flagging it as a scope choice rather than encoding a number I would be inventing.**

## ④ BMA / Egan-Jones — 🔴 RE-SCOPED, and the re-scope is the result
`research/BMA_EGAN_JONES_RECOGNITION_2026-08-13.md`. **Not verified, not killed — the framing was wrong.**

✅ **Baseline VERIFIED AT PRIMARY** (three BMA handbooks pulled and extracted): Egan Jones IS a named rating agency in the 2024 **Long-Term** and the 2023/2024 General Business handbooks, ¶C2.3i(b)(i), with its own BSCR mapping column. 🔑 **The grid footnote reads *"As determined by the SEC"* — the causal link between the 8/12 SEC action and the BMA channel, which no media source draws.**

🔴 **But: Class 4/3B/3A are GENERAL BUSINESS — property & casualty. Athene Life Re and the ACRA sidecars are LONG-TERM (Class C/D/E), under a separate handbook that no source addresses.** So the lead that arrived as *"BMA revoked recognition — bites the insurer capital channel"* is really *"a P&C handbook dropped it; the life handbook is unexamined."* **Escalating on the media framing would have put a general-business regulatory change on SHADE's board as a life-insurer capital event.**

⚠️ Also: **n=2 independent sources, not 5** — Bloomberg Law is the same newsroom, Insurance Journal carries the Bloomberg story, and the SFA piece **names no document, no list and no date when actually fetched.** Only the Royal Gazette is original reporting, and it is the only one naming the instrument.
⚠️ **2025 handbooks: PUBLIC-AND-UNFETCHED, not unavailable** — BMA doc centre is JS-paginated, BMA site search returns a byte-identical page for different queries. Route recorded for the next attempt; **I am not calling it blocked.**

**Ladder 🟢 unchanged; the two channels are not conflated, per your rider.**

**Ask back (one grep, not a session):** the **2025 Long-Term** handbook, ¶C2.3i(b)(i). Absent → registered domain item, escalate; present → dead for SHADE. ⚠️ And the question no disclosure answers: **election is optional and elections are not public** — EJR says it has **no Bermuda-headquartered clients**, so **a recognition change with zero electors is a non-event.**

## COMPLETION (addendum)
**STATUS:** COMPLETE — ruled rows ③ and ④ both executed; ③ confirms as built, ④ returns a re-scope rather than a verify-or-kill binary.
**CHANGED:** `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` (new) · `research/BMA_EGAN_JONES_RECOGNITION_2026-08-13.md` (new) · `STATUS.md` §0j · `SCRATCH.md` · `board_log.tsv` (+2).
**RESULT:** Canary baseline **S1 $2.0B→~$1.2B · S2 40.7%→36.2% (−4.5pp) · S3 ~11mo**, first graded read **Q3-26**. BMA: Egan Jones primary-verified **present** in the 2024 Long-Term handbook; reported 2025 removal is **General Business only**; **n=2** independent sources.
**GAPS:** 2025 Long-Term handbook unfetched (public, route recorded) · Bermuda rating-agency *elections* not public · Apollo Q2 10-Q RS cross-check still not run · STATUS now ~500 lines vs the ~250 cap.
**WILL_NEEDS:** Nothing. Neither row moved anything; ④ removed a false escalation rather than adding a real one.
**FOLLOW-UP:** ① one grep of the 2025 Long-Term handbook ② Apollo RS segment ③ STATUS compression (now urgent) ④ canary Q3-26 read, both instruments ⑤ MBA Q2 ~mid-Sept.
