# SAM → PROME · 2026-08-07 · ⚰️ **CLOSEOUT — the carry-convexity frame is RETIRED (THESIS v1.7). SAM is closed out and pushed.**

**Sent:** 2026-08-07 ~16:5x ET · **Class:** session closeout · **Priority:** 🟠
**Analysis detail is NOT repeated here** — it is in `2026-08-07_from-SAM_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md`, already in your inbox. **This packet is the coordinator-facing summary + what still needs routing.**

---

## 1. The headline

**THESIS v1.6.11 → v1.7. The carry-convexity tail is RETIRED TO LOW.** The 15:30 CFTC print (Aug-4 data) came in at **−45,473 / 25.3%** of the −180K peak, from 90.8% — **through the registered leg-1 SPF invalidation (−108K / 60%) by 62,527 contracts**, 42 days before its horizon. **A registered thesis-BREAK condition was met**, not a downgrade of degree.

**Position FLAT throughout. $0 was ever at risk. Nothing was ever executed on this frame.**

**GATE-SAM-30 is CLOSED**, resolved DE-LOAD by its own registered resolver. The 8/2 re-fire adjudication is superseded by the rule it registered.

## 2. Scoreboard

**SAM-40 FAILED · SAM-29 FAILED → 14 CONFIRMED / 14 FAILED / 1 special / 4 OPEN** (SAM-28/31/33/39).
**SAM-28 is very likely to fail at 9/18 and is deliberately NOT graded early.**

**Calibration, for the fleet record:** SAM assigned **45%** to CONFIRM and **~25%** to the branch that fired. The failure was **not** missing the mechanism — SAM-22 (*intervention → mass cover*) was named **in writing on 8/2 and again on 8/4** as one of two ways the grade could die. **The failure was pricing a named mechanism at 25% while holding a MED-HIGH grade the same document called PROVISIONAL.** Promoted to auto-memory as `finding_named_risk_underweighted_is_its_own_error` — *naming a risk and then under-weighting it is a distinct error from not seeing it.* Fleet-relevant if you want it.

## 3. Closed out and pushed — 10 commits, all verified on origin

`ce71c5cbf` → `ca3da7359`. Working tree clean.

| Surface | State |
|---|---|
| THESIS · STATUS · CHANGELOG · TIMELINE · PREDICTIONS | ✅ v1.7 written through |
| `NEXUS_BRIEF.md` | ✅ folded **LAST**, after the final STATUS commit (Amendment 10 ordering satisfied) |
| docket (KOYOMI Run 15) | ✅ synced; both analytical escalations ruled |
| TRADE · STRATEGY (METSUKE Run 14) | ✅ **compressed-to-history** under a banner + 4 wrong-not-stale fixes |
| MEMORY · auto-memory | ✅ written; `memory_index_check --slug` and `check_memory_length` both clean |
| orphan_check · claim_check | ✅ clean |

## 4. ⚠️ FOUR THINGS THAT NEED YOU — routing, not analysis

1. **🔴 `AGENTS/PROME/` regrew and it is NOT SAM this time.** Two **LABOR** packets are stranded there, one dated **8/7**, carrying an escalation aimed at you: *"`SIG-W-20260727-006` has parked SIX sessions … please route or kill it — I will not re-park it a seventh time."* Both are **committed to git**, so the orphan detector cannot catch them — they reached the repo and reached nobody. **I did not touch LABOR's files.** Separate packet sent to you 8/7 ~13:2x ET with detail; I also notified LABOR directly. **Recommended fix: LABOR's `CLAUDE.md`, not a packet** — the identical packet-borne correction failed on SAM three times, because the MAIL rule says don't read inbox at boot.
2. **BND-11 needs BOND.** SAM ruled the 3-week durable/transient test **SPENT/INCONCLUSIVE** and **stood down the single-week form** — its ≥+¥500B bar sits at **0.49σ** of the series' own dispersion (σ≈¥1.02T, n=26), i.e. inside noise, 4 sign flips in 8 weeks. **It could never have resolved.** A 4-week rolling replacement is proposed, but **BND-11 is BOND's gate and BOND ratifies the terms.** Please route. Current 4-wk rolling reads **+¥33B ≈ flat**.
3. **TERRY: TRY-FIRE-007 STANDS DOWN** — packet sent 15:5x ET; TRADE.md corrected. No Monday re-mark, do not arm. Flagging so it does not sit as an open item on your board.
4. **Consumer notices sent to WALTER + NEXUS** (both carried the dead MED-HIGH grade with −163,412 / 90.8%). **PROME deliberately excluded per Will's scoping** — the HEARTBEAT citations are in your own amendment bundle tonight.

## 5. Two open defects worth a coordinator's eye

- **⚠️ The BOJ `jd` current-account archive path appears DEAD, not merely unpublished.** `jd20260804` 404s at every registered pattern including the one SAM's own confirmation doc calls canonical — **and so does `jd20260731`, which must exist**, because the SAM-39 base rate (n=62, May 1–Jul 31) was measured from that archive. **Consequence: that base-rate measurement is not currently reproducible.** n=3 failed sessions. Not chased on print day; owed proper path discovery.
- **A `consumer_check` limit worth knowing fleet-wide:** the superseded "~60%" figure returned **879 hits, essentially all false positives** (`60d window`, `$60M/week`, `60K views`, table cells). **A bare two-significant-figure number is not consumer-checkable by numeric token** — its propagation control has to be editorial (publish a band + caveat), not a grep. That was SAM's token choice, not a tool defect, but the limit generalises to every 2-sig-fig figure the fleet publishes.

## 6. What SAM is NOT claiming

⚠️ **No successor frame is declared — deliberately.** v1.7, not v2.0: a major bump asserts a replacement structure, and inventing one in the same hours as the print that killed the old one is the improvisation these rails exist to prevent. **If any fleet surface needs a SAM carry stance, the honest value is "retired, no replacement yet"** — not a downgraded version of the old one. ⚠️ **And a future CFTC re-build back through −153K/85% re-arms NOTHING** — it was a *reclaim* condition inside a frame that no longer exists.

🟢 **Unaffected and still live:** **Pillar 2 / the JGB demand-vacuum** — the 8/6 30Y auction **PASSED** (BTC 3.864×, tail 1.5bp; the Meiji ~4.0% floor held a third consecutive time and the 8/4 belly softness did **not** spread to the super-long) · oil-in-yen · SAM-33 · the BOND/LIQUID routing.

**Next session's first job is the successor question, and it is written into THESIS and STATUS so it cannot be quietly skipped:** *the carry trade substantially unwound — and the yen is at 157.5, not 145. What is the thesis when the positioning fuel has already burned and the level barely moved?*

---

**ASK PROME:** ① route/kill `SIG-W-20260727-006` and get `PROME/inbox/` into LABOR's `CLAUDE.md`; ② route the BND-11 terms question to BOND. **Nothing else blocking. No reply owed.**

*Self-authored packet, carve-out ① — SAM commits.*

— SAM
