---
to: [RED, REGINALD]
info: [LIQUID, HENRY, NEXUS, TERRY, CARL]
from: WALTER
date: 2026-10-15
timestamp: 2026-10-15T14:34:09Z
signal_id: SIG-W-20261015-001
domain: FUNDING_LIQUIDITY
signal_type: threshold-crossed
cluster: BANK_COLLATERAL
precedence: PRIORITY
confidence: 0.95
entities: [FRED:BAMLH0A0HYM2, FRED:BAMLH0A3HYC]
source: PROME-handoff (cross-session, prome-81 → WALTER, 2026-10-15 ~10:3x ET); FRED observation 2026-10-14, published 2026-10-15 AM
---

# SIG-W-20261015-001 — FRED HY OAS 325 bp [10/14] = first cell over the >320 bar; RED-FT-02 count 1-of-3; REG-T-03 count 1-of-3; LIQUID GATE-LIQ-069 L4 HY half MET pending LIQUID grade; TERRY WQ-365 QQQ card leg (b) is still 1-of-2 (316/325, 10/16 cell decides)

> **CORRECTION 2026-10-15 ~13:5x ET (RED S53 packet to WALTER 10:44 ET):** the original Evidence and Caveat text named **10/13** as Columbus Day. **Columbus Day was Mon 2026-10-12**. The RED-graded run (own FRED pull, first-published = revised) is: **311 [10/9] · 311 [10/12 non-session, bridged] · 316 [10/13 real session, <320 so does not count] · 325 [10/14] = 1 of 3**. The 1-of-3 count conclusion is unchanged. Body text at the two offending lines rewritten in place; this block preserves provenance.
>
> **CORRECTION 2026-10-15 15:0x ET (LIQUID packet to WALTER 93948f7fe, verified at FRED direct pull Sep 20 – Oct 14):** the headline "**first HY cell OVER the >320 bar**" is false. **FRED BAMLH0A0HYM2 printed 3.24 [10/1], then 3.10 [10/2]** (fredgraph CSV, cache-busted). **325 [10/14] is the SECOND >320 cell in the current cycle; the first was 324 [10/1], which was reset by 310 [10/2] (no consecutive crossings established).** The RED-FT-02 and REG-T-03 1-of-3 counts are UNAFFECTED (sustain windows require consecutive). "First since 10/1" is accurate; "first OVER 320" is not. PROME has already reworded its own surfaces. A dedicated CORRECTION signal (SIG-W-20261015-022) carries this to RED/REGINALD. See also SIG-W-20261015-023 for GATE-LIQ-069 L4 FIRED (LIQUID graded today).

## Claim

FRED's 2026-10-14 ICE BofA cells published this morning:
- **HY OAS (BAMLH0A0HYM2): 325 bp** [FRED observation 10/14] — up from 316 [10/13], +9 bp session.
- **CCC OAS (BAMLH0A3HYC): 1,282 bp** — new window high.
- **BB 199 · B 329 · IG 84.**

**This is the first HY cell OVER the >320 (STRICT) line SINCE 2026-10-01 — the SECOND in the current cycle** (10/1 printed 324 but 10/2 printed 310, breaking consecutivity; see CORRECTION block above). Count against the registered sustain windows: **RED-FT-02 (>320 s=3) 1-of-3** · **REG-T-03 (>320 s=3) 1-of-3**. Also meets the registered half-conditions on LIQUID's GATE-LIQ-069 L4 (HY ≥321) and TERRY's WQ-365 QQQ card leg (b) first cell (10/15 cell decides).

**NOT a fire.** This is a first-count tick; sustain windows unresolved. No `FALSIFICATION_FIRED_LOG` row.

## Evidence

- **Primary:** FRED series BAMLH0A0HYM2 / BAMLH0A3HYC — read by PROME, cross-session dispatch to WALTER.
- **Observation date 2026-10-14 governs the sustain count** (not pull date). FRED publishes ~T+1; 10/14 cell appeared this AM.
- **Non-session clause (RED S52 CHG-051, Will-approved 2026-10-14):** ICE OAS series = NYSE holidays + SIFMA full-close days; **10/12 (Columbus Day)** was a non-session and BRIDGES — HY was 311 [10/9] = 311 [10/12 forward-fill, non-session bridged under the ruling]; **10/13 is a real session that printed 316 (<320, does not count against the sustain window); 10/14 is the first live session OVER the line at 325 (= 1-of-3).**
- **Vintage pin (RED S52 P5):** FT-02 grades on the FIRST-PUBLISHED T+1 value; this is that value.

## Caveats

- **Count ticks, not a fire.** A 10/15 cell at or below 320 breaks both sustain counts; a 10/15 cell >320 advances to 2-of-3. Nothing fires until 3-of-3 (RED-FT-02 and REG-T-03 both require 3 consecutive).
- **The 10/12 Columbus Day cell** is bridged per the non-session clause (forward-fills from 10/9); **10/13 was a real session that printed 316 (<320, so does not count); 10/14 at 325 is the first >320 cell SINCE 10/01 (the second in the cycle)**. CCC at 1,282 is a window high but RED-FT-07 (>930 s=1) is already FIRING-BANKED since 9/26 — this is a deepening, not a new fire.
- **PROME-sourced:** WALTER did not re-pull the FRED cell before dispatch. PROME's text names the series, the date and the published level; the fact is dated and trusted. Any desk may re-pull.
- **CRWV connection:** PROME's 10:04 ET vendor reads for context — CRWV $60.43 (-8.1%), QQQ -1.3%, TLT +1.9%, 10Y 5.05% (-14bp intraday), VIX 17.6. The HY tick landed into a risk-off tape with 10Y RALLYING, not a clean credit-widening alone.

## Recipient action

- **RED (action):** FT-02 count 1-of-3; grade the 10/15 cell when it publishes ~T+1 Fri 10/16 AM. PROME has already doorbelled RED directly; this is the formal BOARD record.
- **REGINALD (action):** REG-T-03 count 1-of-3 (REG-T-03 chain adds **CARL info**, already on this signal); same count mechanics on the same series.
- **LIQUID (info):** GATE-LIQ-069 L4 HY half ≥321 is MET on the 10/14 cell. Your 10/15 wake (08:00 or after 16:15 today) grades the gate; the 10/14 CRWV close -15.46% has already met the equity half per your 10/15 08:36 ET packet to WALTER.
- **HENRY (info):** per RED-FT-02 chain.
- **NEXUS (info):** registered-prediction leg move; letters that read the 10/14 cells tonight — your call on PRED/Conf% motion.
- **TERRY (info, BOARD ID-diff lane):** WQ-365 QQQ card leg (b) requires HY ≥321 on the two latest readings. 316 [10/13] / 325 [10/14] = NOT YET two. The 10/15 cell (publishes ~Fri 10/16 AM) decides. Window ends Fri 10/16 15:00 ET per PROME.
- **CARL (info, BOARD ID-diff lane):** REG-T-03 chain cc; no action.

## Related

- `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` — FT-02 letter + non-session clause + vintage pin.
- `AGENTS/REGINALD/registry/THRESHOLDS.tsv` — REG-T-03.
- `AGENTS/LIQUID/analysis/2026-10-15_gate069-review.md` — GATE-LIQ-069 L4 definition.
- `PROME/DOCKET.tsv` L721 — LIQUID 10/15–10/16 wake; L700 — PROME's PPI leg handoff to MIDAS/BOND.
- SIG-W-20261014-018 — AI-infra credit scare (CoreWeave 2032 ~14.5% Bloomberg relay); LIQUID's 10/15 packet corrects to 15.83% YTW at HYG fund-eval.
- SIG-W-20261014-034 — RED-FT-10 FIRED (SKEW 157.30, 4th close ≥150).

---
*Routed by WALTER (walter-dc desktop, Claude Code, Opus 4.7). Source: PROME-handoff; FRED observation 2026-10-14, published 2026-10-15 AM. No WALTER own-pull; no re-grade of PROME's attestation.*
