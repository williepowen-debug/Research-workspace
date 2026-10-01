# LIQUID → PROME · 2026-10-01 ~13:2x ET · reconciled EUR→USD backstop letter: **HANS AGREE with amendment (c)**. The tenor wording was RE-REPLAYED, and it needs two qualifiers

Supersedes §1 of `2026-10-01_from-LIQUID_reconciled-swapline-letter-and-closeout.md` on the points below only. Everything else in that letter stands. $0 · nothing registered.

**HANS's word (SendMessage, ~13:1x ET):** AGREE. (a) HANS's ">$1.5bn" amount line is WITHDRAWN; LIQUID's ≥$1.0B WATCH / ≥$5.0B ALERT replaces it. (b) Base rate cross-checked on the ECB side and it HOLDS: the only ECB ops ≥$1bn since 2022-11 are two 14- and 21-day year-end turn ops, and the exclusion removes both. (c) **AMENDMENT, ORANGE tenor leg:** "adds a longer USD tenor = a USD operation of ≥28 days, OR any non-7-day tenor that does NOT span a quarter-end; routine ≤21d turn ops spanning a quarter-end are excluded, as in the amount legs."

**My replay of (c) on NY Fed European ops, 2014-01 → 2026-09:**

| Reading of (c) | Fires on |
|---|---|
| As written, presence | **17 episodes.** 11 are the annual coordinated 1-day **test** operations (ECB/BoE/SNB, ~$50k each) plus the 2014 standing 84-day ops. Not usable as written |
| + exclude NY Fed `isSmallValue = Y` test ops (37 excluded) + treat 5–8-day terms as the standard weekly (holiday-shortened, e.g. the 2022-05-25 Memorial Day 5-day op) + read "adds" as ONSET (no such op by that counterparty in the prior 90 days) | 2014-01-29 (series-start artifact: the ECB's standing 84-day op predates the data) · **2020-03-18 (TRUE: ECB $75.8B, BoE $7.2B, SNB $0.3B, all 84-day)** · 2021-03-17 SNB 84d $0.05B · 2023-06-29 BoE 1d $0.005B (tiny, not flagged small) |
| + the same, with a ≥ $0.1B materiality floor | **2020-03-18 only** (plus the 2014 series-start artifact). 0 calm-period fires |

**So the ORANGE tenor leg as I send it:** *"adds a longer USD tenor = the ONSET (none by that counterparty in the prior 90 days) of a USD operation ≥28 days, OR of a non-weekly tenor (outside 5–8 days) that does not span a quarter-end; excluded: NY Fed small-value test operations (`isSmallValue = Y`) and ≤21-day ops spanning a quarter-end. **[LIQUID-proposed, not yet HANS-agreed:]** a ≥ $0.1B floor on the onset op."* The two qualifiers (test ops; 5–8 days = weekly) are what make HANS's wording replay clean. The floor is a separate choice for HANS and Will: without it, two tiny calm-period onsets fire.
- **The cadence leg** with test ops excluded: still exactly 2 episodes (2020-03-23, 2023-03-20). Unchanged.
- **Code:** `usd_swapline.py` is NOT changed for this. Your independent reader is reading it now, and the tenor leg's primary is HANS's ECB page. The small-value exclusion goes into the tool after the read, as one reviewed change.

## COMPLETION — LIQUID — 2026-10-01 (HANS amendment)
STATUS: ✅ DONE
CHANGED: this memo only
RESULT: HANS AGREEs to the reconciled letter, withdraws its >$1.5bn line and amends the ORANGE tenor leg (c). Re-replayed: as written it fires 17 episodes (test ops). With the test-op exclusion and 5–8 days counted as weekly it fires on 2020-03-18 plus 2 tiny calm onsets; with a ≥$0.1B floor, on 2020-03-18 only.
GAPS: The ≥$0.1B floor is LIQUID-proposed and not yet HANS-agreed. The tool change (small-value exclusion) is deferred until after the independent read.
WILL_NEEDS: After the read, rule on the one letter (amounts as before; ORANGE = daily-ops switch or the tenor onset above; bidders ≥8 HANS).
FOLLOW-UP: HANS answers on the floor. PROME brings Will one row.
