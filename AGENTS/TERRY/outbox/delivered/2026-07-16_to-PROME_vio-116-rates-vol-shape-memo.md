# SHAPE MEMO → PROME → Will [Approve] — GATE-VIO-116 rates-vol hedge (registered consequence)
**From:** TERRY · **Date:** 2026-07-16 (~09:45 ET) · **Gate:** GATE-VIO-116 = FIRED-UNEXECUTED (VIOLET, KB-VIO-116)
**Consequence owed:** fresh rates-vol hedge look → PROME → **TERRY shape memo (rates-vol lane, NOT VIX-calls per Will 7/9)** → Will [Approve].
**Bottom line up front:** **NO ATTRACTIVE STAND-ALONE SHAPE RIGHT NOW.** The rates-vol event already happened (MOVE spiked to **77.77 on Mon 7/13**, the sustain-completion day) and has **round-tripped to 68.48** — buying rates-vol convexity now = paying for vol that just deflated. The rates-short *view* is better (and already) expressed via the armed **TRY-FIRE-004** (same lane). A dedicated VIO-116 hedge would **double-count** that. Re-open only on a MOVE re-escalation.

---

## 1. Fire attribution — CONFIRMED F3 (my earlier F1 correction RETRACTED)
**RETRACTION:** an earlier draft of this memo claimed the gate fired via F1 (not F3) on the grounds that "MOVE was 69.55 on 7/13." **That was wrong** — it rested on a yfinance 1h-bar series that was **mislabeled one day late** (it carried 7/10's 69.55 onto 7/13). An authoritative daily source (investing.com, self-consistent + arithmetic-tied, see §2) shows **7/13 MOVE = 77.77 (+11.82%)**. So on **7/13**: 10Y 4.62 (>4.60) **AND** MOVE 77.77 (>70) → **F3 ("10Y through 4.60 WITH MOVE>70 before 7/14") FIRED CLEANLY.**

**GATES.tsv's "F3: 7/13" attribution is CORRECT — do NOT amend it.** (F1 also technically fired — MOVE >72.41 on 7/13–7/14 — but F3 is the correct primary/registered fire and PROME already has it right.) The consequence is genuinely owed either way; my no-stand-alone-shape conclusion below is unaffected.

## 2. The rates-vol tape (authoritative daily — the spike was 7/13, then a clean fade)
| Date | MOVE close | Δ | Source | Note |
|---|---:|---:|---|---|
| 7/8 | 72.41 | — | yf daily | prior cycle peak |
| 7/10 Fri | 69.55 | — | yf daily | base into the weekend |
| **7/13 Mon** | **77.77** | **+11.82%** | investing.com daily | **>72.41 peak AND >70 → F3 (+F1) fire; same day 10Y completed 5-of-5 at 4.62** |
| 7/14 Tue (CPI) | 75.03 | −3.52% | investing.com daily | already fading through the cool print |
| 7/15 Wed | 68.48 | −8.73% | investing.com daily | round-tripped below the 70 marker |
| 7/16 Thu | 68.48 | — | yf "live" (= 7/15 close; ICE T+1 lag) | near, not at, N1 stand-down (<66) |

*(All values web-verified 2026-07-16; investing.com daily is internally consistent — 69.55×1.1182=77.77, 77.77×0.9648=75.03, 75.03×0.9127=68.48 — and reconciles to the yf 7/10 anchor. Independent WebSearch corroborates 7/14=75.03 −3.5%. This supersedes the yf 1h-bar series, which lagged the labels by one day.)*

The vol spike was **real and sharp** (7/13, through the cycle peak) but **deflated fast** (already fading by CPI day, −8.7% on 7/15). VIX 16.17 (+3.2% today) still cycle-calm. Classic post-event vol crush: **the hedge is being requested after the move it was meant to hedge.**

## 3. Honest read on a SHORT-rates / rates-vol hedge shape
The VIO-116 lane per Will (7/9) is **rates-vol / duration-tail, NOT VIX-calls**. Candidate listed shapes and my verdict:

| Shape | What it is | Verdict now |
|---|---|---|
| **TLT put / put spread** | directional short-duration + convexity (listed) | **This IS TRY-FIRE-004 (armed today).** A separate VIO-116 version double-counts. |
| TLT straddle/strangle | pure long-rates-vol (pays on realized move either way) | **Poor now** — buying long vol *after* MOVE deflated 77→68; theta bleed into a calming tape. |
| Payer swaption / rates-vol convexity | the institutional duration-tail expression VIOLET references | **Out of venue** — not accessible on Will's listed-options broker; flag if that changes. |
| /ZB, /ZN futures-options | cleanest listed rates-vol proxy | **Venue-gated** — only if Will trades Treasury-futures options; otherwise N/A. |
| TBT / PST (inverse UST ETFs) | directional short duration, **no convexity**, decay | Not a vol hedge; rejected for this lane. |

**Conclusion:** the only clean, accessible, in-lane rates-vol shape is a **TLT put/put-spread — which is already the armed TRY-FIRE-004 card.** There is no *second, distinct* rates-vol hedge worth putting on right now:
1. **Vol has deflated** (77→68.48) — long-vol convexity is being bought late/expensive-relative-to-signal.
2. **It double-counts.** VIOLET's own KB §4 names "TERRY's live card from the 7/9 disposition" as the vehicle reference — VIO-116 and TRY-FIRE-004 are the **same duration-short/rates-vol lane.** Running both = doubling duration-short risk under one thesis.

## 4. Registered consequence — satisfied
The shape memo is the owed deliverable and it is delivered: **the rates-vol hedge collapses into TRY-FIRE-004** (armed, separate packet). No stand-alone VIO-116 packet is warranted at 7/16 marks. **This is a valid "no attractive shape right now" conclusion, not a punt** — the vol event round-tripped and the rates-short view is already expressed.

**Re-open a dedicated rates-vol hedge look IF:** MOVE re-escalates **>70 (VIOLET's escalation marker) or >72.41 (F1 re-fire)** with the 10Y sustaining ≥4.60 — i.e., the rates-vol channel re-accelerates rather than continuing to bleed toward N1 (<66). At that point a TLT put-spread or (if venue available) a payer/futures-option shape becomes live and non-redundant.

## Decision
[ ] ACKNOWLEDGE — fold VIO-116 into TRY-FIRE-004, no separate hedge now (Terry rec)
[ ] REQUEST a stand-alone shape anyway (I'll build a TLT put-spread variant sized to $500, flagging the double-count)

**APPROVAL REQUIRED for any packet — Will must approve/reject before execution. TERRY never executes.**
