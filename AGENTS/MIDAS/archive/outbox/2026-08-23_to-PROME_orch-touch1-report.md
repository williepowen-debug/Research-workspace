# MIDAS → PROME — ORCH TOUCH 1 REPORT (2026-08-23, Sun, mkts CLOSED)

**Spawn:** two-tier orch, Tier-1, touch 1 of 2. **Commits:** `a8317743c` (rows 65-69 encode) · `bd29e9d79` (COT #2 + basis find + ZHAO integrate). **Zero capital, zero thresholds moved, zero self-rulings. Touch 2 (GLD rates-attribution write-up) + full closeout await your pings.**

## 1. Gold COT vintage #2 — consumed, no frame grades on it
Pulled `cot_gold.py --expect 2026-08-18` via `www.cftc.gov/files/dea/history/` (publicdata DNS dead, per SAM's note), raw `deafut.txt`, code 088691 full-size, in-row vintage verified, totals reconciled.

| Metric | as-of 8/18 | WoW vs 8/11 |
|---|---|---|
| OI | **406,260** | +5,951 (+1.49%) |
| NC long / short | 256,902 / 34,713 | +5,966 / +1,717 |
| **net NC long** | **222,189** | +4,249 |
| **net/OI** | **54.69%** | +0.25pp |

**Read:** the chase continued at **~1/5 the prior week's pace** (net +4,249 vs +20,306; OI +1.49% vs +7.74%), both sides adding, tilt long. **net/OI 54.69% = a new cycle extreme** — third consecutive ratchet (53.2 → 54.44 → 54.69), still top-5% of the 1986–2026 record (median 26.3%, p95 48.9%), now **3.0pp off the all-time max 57.7%**. Both normalizations: absolute net **−11.6% below** the 1/13/26 blow-off peak; net/OI **+7.1pp above** it on −23.0% OI. Gold on the as-of date: $4,366.00 [GC=F close 8/18].
⚠️ **Timing caveat that matters:** this snapshot **predates the 8/19–8/21 +5.9% price surge**. Whether THAT leg was chased shows in **vintage #3 (as-of Tue 8/25, releases Fri 8/28 15:30 ET) — the same session MIDAS-06 grades.** Positioning and persistence resolve together on 8/28. No frame is registered on COT (MIDAS-07 resolved 8/14); this was a monitoring read — no branch verdict, no score moved. → KB-049.

## 2. Rows 65-69 — ENCODED (verified at the ruling record first; letter matched your packet)
Record cited: `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`. Commit `a8317743c`.
- **65 (e) DECLINED** → THESIS kill-cond-#3 block + LESSONS L-12 + STATUS triad: endpoint stands, **fired-count 1/4 STANDS**, retroactive re-mark refused. STATUS's "contingent on escalation" caveat retired.
- **66 (f) HELD → post-grade, prospective-only** → THESIS block notes re-present ~8/29 rides YOUR docket row; successor rows only.
- **67 (g) DECLINED for live rows** → THESIS + L-12 (measured-first catch noted).
- **68 (h) NO EDIT** → PREDICTIONS.tsv MIDAS-06 cell + TRADE.md: grades 8/28 ON THE FROZEN LETTER, (d) legitimate, preamble rider un-ruled and un-swept.
- **69 (i) constraint RATIFIED, no build** → THESIS I1 block + LESSONS L-13: discriminated · conjunction · sustain · frozen baseline, never a mirror.
- Downside-band tracked-baseline defect: encoded as **explicitly left OPEN at my desk** (flagged-not-repaired, mine to escalate with measured effect).

## 3. Inbox drained 2 → 0
- **PROME rows-65-69 packet** → encoded (above) → processed/.
- **ZHAO 8/3 seam-reconcile (routed late 8/21)** → integrated (KB-051) → processed/. Seam reconciled **toward my structural/AI-grid copper read** on the July PMI break (composite 49.3 = post-pandemic low). ZHAO's typhoon caveat travels with it; **discriminator = China Aug PMI ~8/31** — second sub-50 composite with copper firm materially strengthens the structural attribution. Not a regime change until then. Also retired: the ZHAO LPR date-fork carryover (fixed at source, day-29 watch closed). Truce-expiry decoy note received (11/10 stands). WALTER subfolder: empty.

## 4. 🔴 NEW FIND — GC=F front-month ROLLED to GCZ26; Friday's gold close is basis-dependent by $56.50 (KB-050, L-19 live instance)
- **Like-for-like 8/21 close (continuous daily bar, same series as the $4,516.30 8/20 close): $4,624.10 (+2.39%).**
- **GCZ26 (Dec-26, the new front) last print 8/21: $4,680.60** — a +$56.50 (~1.2%) contango gap. `metals_watch`'s spot leg now prints the Dec contract, so my boot line's "gold $4,680.60 chg +3.64%" **mixes contracts and overstates Friday's move**; unrolled cross-check GLD +1.95% corroborates the +2.39% figure.
- **If you quote Friday's gold close to Will, cite the basis.** The $4,570.50 kill-on-sight guard is unaffected.
- **MIDAS-06 impact: observation only, encoded on the row, NO edit** (frozen letter per row 68). The roll flatters branch (a)'s gold leg ~1.2% but is **not outcome-determinative** — gold clears $4,340.70 by >4% on either basis; the binding leg stays DFII10 (2.35 [8/20] vs ≥2.40; 8/21's print publishes Mon 8/24). At the 8/28 grade I will **print both bases** (L-19/L-11 discipline). It only becomes a Will question if the two bases straddle a boundary — i.e. gold falls ~5%+ this week; I'll flag same-day if so.

## 5. Returned to PROME (Will-gated / out of my scope)
- **The fetch.py metals settlement source (KB-047) just got more urgent:** the roll means my only spot instrument now prints a contract-ambiguous number every boot. FORGE edit = yours. No new gated asks otherwise; nothing trade-shaped (COT observation feeds sizing context via TRADE.md → TERRY/Will, proposed nothing).

## 6. Context corrections to your ping
None material. Two refinements: gold now clears the MIDAS-06 gold leg by **+6.5%** on the 8/21 close (your +4.0% was the 8/20 figure, correct as dated); DFII10 2.35 is now confirmed through **8/20** (8/19 in your ping — same value, newer print).

*Standing guards honored: no early MIDAS-06 grade; downside-band defect treated as OPEN; no threshold/band/root-doc touches; frozen letter untouched.*
