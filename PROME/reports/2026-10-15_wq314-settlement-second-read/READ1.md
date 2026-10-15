COLDREADER · AGENTS/ORACLE/analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md · 11091 B (wc -c) · 44 claims
SCORE: 26/44 ✅ · 15 ⚠️ · 3 ❌
❌ 37 O8 vs R4, the fired state at the November roll — L33 "A reset event (§3) **never clears a fired state**" vs L42 (R4 is a row of the §3 reset table) "October's state ends with October's series". §5.2 L58 puts that end at the PIN (~10/25), not at the 10/31 close: "The October band series ends at the pin". So an October Alert/Critical ends at the pin without the 3 below-level reads that O8 requires. §5.4 resets only the RUN (L60, "starts disarmed at run 0") and says nothing about the fired VX-ORC-04 state. A stranger cannot tell whether a fired October state is held, cleared or carried into November.
❌ 23 November listing basis — L57 "The seven prior monthly WTI events (Mar–Oct 2026)" … "(INFERRED from n=7)". Mar–Oct inclusive is 8 months. Either one month is missing and the file doesn't say which, or n=8. This is the basis for the ~10/25 pin date. Low consequence, because the pin waits for an actual listing anyway.
❌ 43 Packet pointer — L3 "`inbox/2026-09-28_from-PROME_v5-thresholds-define-reads-and-resets-CATO.md`". `ls AGENTS/ORACLE/inbox/` has no such file. It resolves only at `AGENTS/ORACLE/inbox/processed/…`, where it was moved on consumption. Low consequence.
⚠️ 3 Resolution source "Pyth 1-minute candle High" (O2 L27) — **the settlement text is not quoted in this file.** Only the title is verbatim (L26). O2 is ORACLE's paraphrase mixed with ORACLE's own derivations (e.g. "The last October session is the one dated Fri 10/30"). A second reader cannot separate the market's words from the gloss. This file does not support the premise that the settlement text "is quoted inside the file". What a stranger needs: the verbatim rules text plus a fetch timestamp or hash.
⚠️ 4 "High **≥ $110.00**" (L27) — inclusive ≥ vs strictly >, and "$110.00", are paraphrase. The title only says "hit (HIGH) $110". The tie at exactly 110.00 can't be checked from the file.
⚠️ 5 "Active Month of ICE Futures Europe WTI (Pyth 'CLL')" (L27) — the file never states what Active Month means. That definition decides which contract resolves the market.
⚠️ 6 The switch rule (open of the 3rd-to-last session before LTD) can only be reverse-engineered from R3 L41: "Nov26's third-to-last session is the one dated Thu 10/15, which matches the market's own worked example". That worked example is never quoted. The arithmetic is consistent (10/15 Thu · 10/16 Fri · 10/19 Mon LTD; 11/17 Tue · 11/18 · 11/19 Thu LTD), but the rule itself is unsourced in the file.
⚠️ 7 Start boundary — "during an October 2026 trading session" plus "sessions open at 8:00 PM ET the evening before" means prints from 8 PM ET Wed 9/30 (= 10/01T00:00Z) count. The file states the last session (Fri 10/30) but not the first. A stranger can derive it, but it is not written.
⚠️ 9 Fallback "If Pyth is unavailable … ICE official daily high (`ice.com/report/10`)" — "unavailable" has no scope (a minute? a session? the month?). The external pointer wasn't tested (cannot reach). It is consistent with a switch at session open, because the session's daily high is then one contract's.
⚠️ 13 "Text re-read at Gamma on 2026-10-09T14:26Z, unchanged from 9/28" — not checkable: no verbatim text, no hash. L68 itself says "A second reader has **not** checked it".
⚠️ 19 Pyth CLL roll (L69) "assumed to follow the market text's rule … the text governs" — this leaves a state undefined: if Pyth's CLL feed rolls on a different minute from the text's Active Month, the file doesn't say whose 1-min candle resolves in that window, or whether the fallback applies.
⚠️ 21 YES timing — L46 "Critical fires on YES at once, with no sustain needed" vs L51 "Between the touch and the formal close, a price near 99 is counted as an ordinary read". So "at once" means at the Gamma close, not at the touch. A Pyth ≥$110 candle that ORACLE sees before the close has no state. "99" has no unit (99% / 99¢).
⚠️ 22 NO record — L52 "The record is the last qualified read before the close". L58 says post-pin October reads are "context", so the last read that COUNTS may be ~10/23, not the last read before close. Which one is "the record" is ambiguous.
⚠️ 25 L33 "the Active-Month switch lowers the odds mechanically" is stated unconditionally. That holds only while Dec26 trades below Nov26 (R3: $0.89, measured on a CME proxy, "Re-measure at the switch"). The fail-closed rule survives either way, but the stated reason does not.
⚠️ 31 O3 "US business day (ET date)" — no calendar is named. Mon 10/12 (Columbus Day: a federal/bond holiday while futures trade) is unclassified, and that decides "holiday pulls are context" and the R2 gap count.
⚠️ 34 O6 "Round to 0.1pp **before** testing" — no rounding mode is given. A 39.95 half-tie under binary-float round() can go either way, which moves the cited L546 float-tie class into the rounding step instead of curing it.
⚠️ 36 O8 "3 **consecutive** qualified reads below its level" — R1/R2 say only "Held" for a thin read or a gap. Undefined: ① whether a thin read or gap restarts the CLEARING count (R3 L41 implies the switch does: "first 3 qualified post-switch reads"); ② the outcome of a mixed re-grade (2 below, 1 above), and whether the window then slides or restarts; ③ the Critical→Alert path when 3 reads fall below 60 but stay ≥40.
⚠️ 39 R2 "More than **2 business days** between two consecutive reads" (L40) and L67 "gaps of no more than 2 business days" — neither says whether days strictly between are counted or the difference is. This is live now: 10/9 Fri → next read 10/14 (ET) Wed is 2 between (no gap) or 3 apart (gap), and 1 if 10/12 is a holiday. Moot this time only because the switch reset intervened.
✅ 1 O1 id/slug/YES, value = outcomePrices[YES] — slug and `yes_prob`/`liquidity` columns resolve in ODDS_LOG.
✅ 2 Title verbatim (the only quote).
✅ 8 Session opens 8 PM ET; Monday's at 6 PM Sunday — used consistently in R3 and §5.5.
✅ 10 Prices as published, no rounding (oil price; distinct from O6's odds rounding).
✅ 11 End 2026-11-01T03:59:59Z = 11:59 PM EDT Sat 10/31 (`date` verified).
✅ 12 Last session Fri 10/30 (10/31 is Sat).
✅ 14 Switch 8 PM EDT Wed 10/14 = 2026-10-15T00:00Z (`date` verified).
✅ 15 ICE LTDs Nov26 10/19 Mon · Dec26 11/19 Thu · Jan27 12/18 Fri (cited source, external).
✅ 16 Nov26 3rd-to-last session = Thu 10/15.
✅ 17 Only switch in October; Nov26 is Active at the start (CLX26 used as spot).
✅ 18 Sides classed by UTC. A live edge row exists: ODDS_LOG 2026-10-15T03:56Z (ET Wed 10/14, post-switch), which the rule handles.
✅ 20 YES recorded via Gamma closed / YES=1 / umaResolutionStatus.
✅ 24 Nov switch 8 PM EST Mon 11/16 = 2026-11-17T01:00Z (DST ends 11/1; INFERRED disclosed).
✅ 26 $110 = +20.5% over $91.27.
✅ 27 +73.0pp = 81.5 − 8.5.
✅ 28 31.5pp below Alert (40 − 8.5).
✅ 29 §1 figures match ODDS_LOG row 2026-10-09T14:26Z (0.085, vol 74,815, liq 41,006, d1 −0.025, d7 −0.01) and the 9/28 row (0.255, vol 224, liq 3,284, thin).
✅ 30 Alert ≥40 / Critical ≥60 or YES — L5 = L32.
✅ 32 O4 ≥$5,000 QUALIFIED, <$5K THIN — consistent with R1 and L14.
✅ 33 O5 only live reads count.
✅ 35 O7 run / ARMED / Alert / Critical.
✅ 38 R1 thin read → reset to 0 and disarm.
✅ 40 R3 reset to 0, no run straddles the switch.
✅ 41 §5.3 meaning check, §5.4 entry read, §5.6 pause with no re-strike.
✅ 42 L20 "qualified run = 1" (9/28 thin, and >2bd gap anyway).
✅ 44 Pointers: DOCKET L618 · L546 · `scripts/polymarket.py` · `workbook/ODDS_LOG.tsv` · `tools/disruption_supply_spread.py` (REGIME `v5-oct26-icewti110`, SUPPLY_PREFIX, "war premium" guard present) · KB-ORC-101 (KB.tsv) · VX-ORC-04 (VX.tsv) · MAINTENANCE.md §2026-09-28 · `FORGE/tools/market-data/fetch.py`.
UNDEFINED STATES (rules): Pyth-vs-text roll window (19) · touch seen before Gamma close (21) · clearing count across a thin read/gap (36①) · mixed re-grade (36②) · Critical→Alert downgrade (36③) · fired October state at the Nov pin (37) · holiday calendar (31) · half-tie rounding (34) · fallback scope (9).
POINTERS: 13/14 local+internal resolve (§2 O5, §3, §4, §5 included); dead: `inbox/2026-09-28_…CATO.md` (moved to inbox/processed/). External untested (unreachable): ice.com/report/10, ice.com/products/213 expiry, Gamma market 4936102.
ONE-LINE VERDICT: no — the calendar and arithmetic are right, but a cold reader cannot second-read the settlement text because the file never quotes it beyond the title (the Active-Month rule exists only as an unquoted "worked example"), and the fired-state rules contradict each other at the November pin and leave the clearing count undefined across thin reads and gaps.
