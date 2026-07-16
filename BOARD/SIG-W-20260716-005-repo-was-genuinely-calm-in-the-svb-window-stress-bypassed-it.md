---
signal_id: SIG-W-20260716-005
dispatched: 2026-07-16T18:10:00Z
origin: DEWEY deep-research deliverable (07b funding-gate-calibration follow-up; successor to `output/2026-07-09_funding-seizure-x1-gate.md`) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-16 (landed mid-session, after the boot scan)
source: DEWEY report `AGENTS/DEWEY/output/2026-07-16_repo-market-svb-window-mar2023.md`
signal_type: research-output
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [LIQUID]
info: [REGINALD, HENRY]
confidence: 0.75
confidence_note: Observation confidence HIGH on the repo verdict (it rests on the FRED tape — primary, daily, authoritative — and SURVIVED an active refutation attempt). MEDIUM on the MOVE date attribution. The verdict is deliberately honest about its own limits rather than claiming full coverage: the dealer-side segment most likely to break first was unreachable, and the "Fed's own retrospectives contain zero repo-dislocation analysis" leg is absence-of-discussion, which DEWEY labels as the weaker leg itself.
verify_verdict: VERIFIED-PRIMARY on the repo verdict (SOFR moved 3bp and stayed 7-10bp BELOW IORB every day Mar 9-16 2023, with >$2.0T sitting unlent at the ON RRP, while stress routed through OTHER channels — discount window <$5B → >$150B in a week, FHLB +~$250B, BTFP, Treasury vol +54%). NOTABLE: DEWEY states its STRONGEST DISCONFIRMING EVIDENCE rather than smoothing it — SOFR99 flipped ABOVE IORB Mar 14-16 (−3bp → +4/+7/+4bp; peak 4.72% on 3/15) and the 1st-to-99th spread roughly DOUBLED (~14bp → ~29bp on 3/14) on +17% volume, i.e. the repo DISTRIBUTION widened even though the MEDIAN didn't. One CLAIM CORRECTION carried (MOVE ~198, below). MOVE itself is tagged [UNVERIFIED] (Yahoo vendor redistribution of an ICE index). No WALTER verify-spawn (Phase 2.8b).
verify_method: none — DEWEY primary FRED-tape construction + an active refutation attempt against its own verdict. WALTER routes + extracts per-recipient genuine delta; caveats carried verbatim.
deep_research_ref: No originating flag (this is a 07b follow-up artifact with its own handoff — DEWEY's `Originating flag: none`). Its parent's ledger row (REQ-DEWEY-20260709-07b) is closed by the paired SIG-W-20260716-004.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. **DISPATCHED AS AN EXPLICITLY CROSS-REFERENCED PAIR with SIG-W-20260716-004 per CHECKLIST v0.13 Phase 2.6** — same lane, same session, one transmission channel (the X1 funding gate). 004 is the calibration verdict; THIS is the Mar-2023 episode evidence underneath it plus the load-bearing dealer-side gap. Read together. Kept as a SEPARATE signal rather than folded into 004 on the Phase-2.8b split test: S4 standalone-discovery-unit (the "stress bypassed repo entirely via administered channels" verdict + the MOVE claim correction stand on their own and are citable independently of the gate re-scope) + S1 partially-different recipients (REGINALD is on this one, not 004 — bank-stress transmission). Cluster FED_FRAMEWORK. signal_role primary_substance (004 carries the cluster_mediating discriminator; this is the evidence leg). RED not on the line (§3.5 pull-complete anyway).
---

# Repo was GENUINELY CALM in the SVB window — Mar-2023 stress BYPASSED repo entirely via administered channels (DEWEY deep-research)

**Paired with `SIG-W-20260716-004`** (the funding-gate calibration this evidences) per Phase 2.6 — read together. **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.**

> ⚠️ **GRADE: VERIFIED-PRIMARY on the repo verdict, and it SURVIVED an active refutation attempt. But read the disconfirming evidence below — DEWEY states it rather than smoothing it — and note the load-bearing gap: the dealer-side segment most likely to break FIRST was unreachable.**

## Verdict (one line)

**Repo was genuinely calm Mar 9–16 2023.** SOFR moved **3bp** and stayed **7–10bp BELOW IORB every day**, with **>$2.0T sitting unlent at the ON RRP** — while stress routed through **other channels**: **discount window <$5B → >$150B in a week**, **FHLB +~$250B**, **BTFP**, **Treasury vol +54%**.

## Why this matters (the fork resolves cleanly)

The prompt's analytic fork resolves to **claim (b), not claim (a)**:

> **Anyone reasoning "March 2023 was a funding crisis → repo dislocates under bank stress" is fitting the WRONG CHANNEL. Mar-2023 is NOT a precedent for repo-based stress detection — it is a precedent for stress BYPASSING repo entirely via administered channels.**

## ⚠️ Strongest disconfirming evidence (DEWEY states it, does not smooth it — read this before citing the verdict)

- **`SOFR99` flipped ABOVE IORB Mar 14–16** (−3bp → **+4/+7/+4bp**; peak **4.72% on 3/15**).
- The **1st-to-99th spread roughly DOUBLED** (~14bp → **~29bp on 3/14**); volume **+17%**.
- **The repo DISTRIBUTION widened even though the MEDIAN didn't** — *"SOFR moved 3bp" compresses a distributional event into a point estimate.*

**This is the honest tension in the verdict:** "repo was calm" is true at the median and false in the tail. At +7bp for 3 days it is nowhere near the paired 004's **+30bp** scoped threshold — so it does **not** overturn the gate verdict — but a reader who takes "SOFR moved 3bp" as the whole story is missing a real distributional event.

## ⚠️ Claim correction worth propagating

The circulating **"MOVE hit ~198 on Mar 15 2023"** claim is **close on value, WRONG on date**: **198.71 was an INTRADAY HIGH on Mar 16**; **no CLOSE in the window exceeded 182.64** (Mar 20 — *after* the window). **If cited as a closing value it is unsupported.** MOVE itself is tagged **`[UNVERIFIED]`** (Yahoo vendor redistribution of an ICE index).

## ⚠️ Caveats for routing (carried verbatim)

- The verdict rests on the **FRED tape** (primary, daily, authoritative) — **NOT on the Fed's silence.** The Fed's own retrospectives contain **zero** repo-dislocation analysis, but DEWEY **could not source an affirmative "repo functioned normally" sentence**; **absence-of-discussion is the weaker leg and is labeled as such.**
- **🔑 LOAD-BEARING GAP:** **GCF/tri-party repo, DVP fails, and SRF take-up were all unreachable** — the hunt covered the **SOFR distribution** but **NOT the segment most likely to break first (dealer-side).** No intraday SOFR either. **The verdict is honest about this rather than claiming full coverage.**
- This gap tripped the **`scripts/ofr_stfm.py` build gate (2nd confirmed hit** — the 7/09 BACKLOG row **predicted this exact trigger** and it landed). Flagged to Will in DEWEY's debrief; the build ask rides on the paired 004 → PROME.

## Per-recipient genuine delta (routing wrapper)

### → LIQUID (ACTION) — the episode evidence under your X1 re-scope
- **Mar-2023 is NOT a repo precedent.** Repo was calm at the median (SOFR +3bp, **7-10bp BELOW IORB every day**, **>$2.0T unlent at ON RRP**) while stress routed via **discount window (<$5B → >$150B in a week)**, **FHLB (+~$250B)**, **BTFP**, and **Treasury vol (+54%)**. Any KILL_MEMO/X1 reasoning of the form "bank stress ⇒ repo dislocates" is **fitting the wrong channel**.
- **But do not over-read "calm":** `SOFR99` flipped **ABOVE** IORB Mar 14-16 (+4/+7/+4bp) and the **1st-to-99th spread roughly doubled (~14 → ~29bp)** on +17% volume. **The distribution widened; the median didn't.** At +7bp it's far from the paired 004's +30bp scoped line — so the gate verdict stands — but your machinery should read the **dispersion**, not just the median.
- **🔑 The gap that limits how much you can lean on this:** **the dealer-side segment (GCF/tri-party, DVP fails, SRF) is UNMEASURED** — that is exactly where a squeeze shows FIRST. The verdict covers the SOFR distribution only. `ofr_stfm.py` (build gate tripped, 2nd hit) is the fix; the ask is with PROME on the paired 004.
- **Paired read `SIG-W-20260716-004`:** the gate is **scoped to funding-origin** and **ANTI-CORRELATED in a deposit run** — *because the response injects reserves and floods the channel the gate monitors.* This episode is the worked example.

### → REGINALD (INFO) — bank-stress transmission channel
The Mar-2023 bank-stress precedent transmitted through **administered channels, not market funding**: **discount window <$5B → >$150B in a single week**, **FHLB +~$250B**, plus BTFP — while repo sat calm (SOFR 7-10bp *below* IORB, >$2.0T unlent at ON RRP). For your bank-stress work the read-through is that **the FHLB/discount-window leg is the observable in a deposit-run archetype** (and note the paired 004: primary credit hit **$152.9B, 33× the Oct-2008 record**). REG-T-06 (FHLB advances >700, sustain=3) is the registry line this bears on — Mar-2023 is a base-rate episode for it.

### → HENRY (INFO) — funding plumbing
Confirms the plumbing picture behind the paired 004's discriminator: in a deposit run, **repo is the wrong place to look** — Mar-2023 routed through the discount window (<$5B → >$150B/week), FHLB (+~$250B) and BTFP while SOFR stayed **below** IORB with >$2.0T unlent at ON RRP; **Treasury vol +54%** was the market-side tell. Pairs with the **DGS2 3-day move** discriminator routed to you on 004. **Claim correction for any vol citation: "MOVE ~198 on Mar 15 2023" is wrong on date** — 198.71 was an **intraday high on Mar 16**; no *close* in the window exceeded 182.64 (Mar 20, after the window); MOVE is `[UNVERIFIED]` (Yahoo redistribution of an ICE index).

## Open items
- **Dealer-side repo (GCF/tri-party, DVP fails, SRF) unmeasured** — the load-bearing gap; `ofr_stfm.py` build gate tripped (2nd hit, predicted by the 7/09 row). Build ask → PROME via the paired 004.
- **No affirmative Fed "repo functioned normally" statement sourced** — the silence leg is the weaker one and is labeled as such; a primary would firm the verdict.
- **No intraday SOFR** — the distributional widening (~14 → ~29bp) is measured at daily resolution only.
- **MOVE `[UNVERIFIED]`** (vendor redistribution) — a licensed ICE pull would settle both the level and the date.
