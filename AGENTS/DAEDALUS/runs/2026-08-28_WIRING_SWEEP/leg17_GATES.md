# Leg ⑰ — METRIC-SURFACE AUDIT: `PROME/GATES.tsv`

Read-only audit. Repo root `/home/willi/Research-workspace`. Today 2026-08-28.

## 0. Scope correction (file-level fact, checked first)

**The task brief says "ALL rows (38 data rows)." The file has 29 data rows, not 38.**
`PROME/GATES.tsv:1-9` is a 9-line comment/header block, `:10` is the column header, and
`:11-39` are the 29 data rows (`grep -c '^GATE-' PROME/GATES.tsv` → 29; confirmed by
`csv.reader` parse). There is no truncation — `wc -l` = 39, file ends in a trailing
newline, no row is split across physical lines. Every row below is one of the 29 that
actually exist. This is reported as a fact, not a judgment about which count is "right."

**A second file-level defect, found while parsing:** row 26 (`GATE-VIO-RV1`, file line
36) has **11 fields where every other data row has 12** (`awk -F'\t' '{print NF}'` shows
line 36 alone at 11). A tab is missing between two cells inside the `state` column's
long history text (the malformed row's own state cell runs `...post-2018 separation
LOS[cut]` straight into what should be the `last_checked` cell `2026-08-27`, then
`AGENTS/VIOLET/outbox/...` lands in `source`, etc. — every column from `last_checked`
onward is shifted one to the left). The practical effect: **this row's `scannable`
cell, read positionally, contains a file path** (`AGENTS/VIOLET/outbox/2026-08-20_to-
PROME_rising-vol-registration-DESIGN-v1-trigger-gated.md (owner artifact WINS on
divergence; this row reconciles)`) **instead of an `INSTRUMENT`/`JUDGEMENT`/`OWNED-
ELSEWHERE` token**, and `definition_surface`/`review_by` are likewise off by one. See
Row 26 below for the full audit under the corrected reading. This is exactly the class
of defect the envelope columns (added 2026-08-22 per header line 9) have **no script
checking** — see §Convention findings.

---

## ROW 1 — GATE-TERRY-ARM1 (line 11)
Owner: TERRY/BOND · Status: `RESOLVED 7/9 NOT-FIRED` (terminal)
Threshold: `BND-11 acute at the 7/9 30Y reopen: indirect<52% AND (BTC<2.15 OR tail>2bp) AND dealer>18-20%`

(a) INSTRUMENT: **PRODUCER-EXISTS-UNCITED.** `AGENTS/BOND/monitors/grade_auction.py` computes
auction-day indirect%/dealer%/bid-to-cover-class figures (confirmed present via
`find AGENTS/BOND -iname "*.py"`); the row's `source` cell cites only the TERRY card, not
this script. State cell says the actual grading was TreasuryDirect-primary, PROME-verified
by hand (`indirect 77.74 / dealer 10.05 / BTC 2.44`), not a script run.
(b) BASIS/WINDOW: **STATED** — named auction (7/9 30Y reopen), named metrics (indirect %,
bid-to-cover [BTC], dealer %, tail in bp), explicit thresholds.
CONJUNCTION (3 legs, AND with one internal OR): **N/A** — terminal, graded NOT-FIRED once, done.
SCANNABLE-AGREES: `INSTRUMENT` cell — **AGREE** (single-auction, all-numeric, no owner
judgment call; matches Class 7's INSTRUMENT definition even though the actual grading run
was a manual TreasuryDirect pull, not a script — auctions are one-shot events, not a
continuous series, so "a machine can grade it" reads as "the definition is unambiguous.")
POINTER: source cites `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` — **OK**
(file exists per repo structure; TERRY setups dir confirmed in Job scans above).
BOOT-RENDERED: **NO** — terminal/one-shot, nothing renders it going forward; `grade_auction.py`
is event-triggered, not a boot leg.

## ROW 2 — GATE-TERRY-ARM2 (line 12)
Owner: TERRY/BOND · Status: `RESOLVED 7/16 ARMED` (terminal)
Threshold: `VX-BND-05 10Y-sustain leg: 5 CONSECUTIVE closes >=4.50, any <4.50 close resets to zero`
(a) INSTRUMENT: **COMMAND-NAMED.** `AGENTS/TERRY/scripts/snapshot.py` line 104 explicitly
lists `("DGS10", "10Y", 1, "%")` as a pulled series, and a comment at line 156 states
"Registered grading is FRED DGS10, a different fetch path, so the GATE is insulated" —
i.e. the script's own docstring names the exact series this gate grades on and
deliberately keeps it separate from other feeds. Row's own text also names the basis
explicitly (official DGS10, 2dp, >= inclusive).
(b) BASIS/WINDOW: **STATED**, unusually precisely — series (official FRED DGS10, not
`^TNX` provisional), rounding (2dp), inclusive/exclusive (`>=`), holiday handling
(neither counts nor resets), consecutive-close semantics, all co-ratified with BOND
(memo cited). This is the strongest-specified row in the file.
CONJUNCTION: N/A (single leg, run-length test).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: source `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` — **OK.**
BOOT-RENDERED: TERRY's `snapshot.py` pulls DGS10 on demand (not confirmed as a scheduled
boot leg vs. an on-request script) — **CANNOT-JUDGE** whether it fires automatically
every TERRY session vs. being invoked manually; would need TERRY's own boot sequence doc.

## ROW 3 — GATE-TERRY-ARM3 (line 13)
Owner: TERRY/SAM · Status: `RESOLVED 2026-07-16: FIRED` (terminal)
Threshold: `Soft May TIC: China AND Japan both net SELLERS on net TRANSACTIONS (valuation-adjusted)`
(a) INSTRUMENT: **NONE.** Grepped `AGENTS/BOND` and repo-wide for a TIC-data puller
(`grep -rl "TIC\b" --include=*.py AGENTS/`) — no script surfaced that fetches Treasury
International Capital data; the fire was graded by a "mechanical sign test" on the
published TIC release read by hand (China −$0.129B / Japan −$2.838B), CSLT-verified.
(b) BASIS/WINDOW: **STATED** — net TRANSACTIONS (not holdings), valuation-adjusted,
named release (May TIC, released 7/16 per the row, corrected in-row to actual 7/14),
country-level granularity requirement explicit with an UNDETERMINED fallback if
unavailable. Good basis discipline even without a script.
CONJUNCTION (China AND Japan both sellers): N/A — terminal, graded once.
SCANNABLE-AGREES: `INSTRUMENT` — **DISAGREE, mild.** No producer exists (verdict a =
NONE) and the grade was a manual monthly-release read, closer to the "a human reads a
published table" pattern flagged elsewhere in this audit (rows 22/28) than to a
script-gradable series. Class 7's own text ties INSTRUMENT to "a machine can grade it";
here nothing does, though the definition itself is unambiguous. Low-stakes since the
row is terminal.
POINTER: source `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` — **OK.**
BOOT-RENDERED: **NO.**

## ROW 4 — GATE-BRENT-SUSTAIN (line 14)
Owner: BRENT · Status: `RESOLVED 7/10 DENY` (terminal)
Threshold: `Brent >$75 both sessions (settlement basis, ICE Sep-26 LCOU26) AND no <$74 round-trip AND >=2/4 FRESH legs`
(a) INSTRUMENT: **CANNOT-JUDGE for the price leg / NONE for the "fresh legs" leg.**
`AGENTS/BRENT/scripts/thresholds.py::get_prices()` and `instrument_check.py::probe_yf()`
exist and pull market prices generically (confirmed by grep), but I could not confirm
either specifically pulls the **ICE Sep-26 LCOU26 settlement** print named in the
condition (both scripts appear Yahoo/FRED-generic; the row's own grade was done by a
human BRENT session cross-checking BZ=F vs. oilprice.com, not a script run). The
"≥2/4 FRESH legs" (war-risk, P&I/JWC, sanctions, transits) leg has **no instrument at
all** — it is a qualitative multi-source news read, correctly typed `JUDGEMENT`.
(b) BASIS/WINDOW: **STATED**, and unusually well fought-over — settlement vs. intraday
was explicitly ratified in a 7/9 red-team addendum after F1-F4/F7/F8/F11 objections; the
row states DENY is the complement of CONFIRM with "no undefined middle."
CONJUNCTION: level leg (settlement close) + freshness leg (≥2/4 qualitative sources) —
per the state cell, the level leg PASSED (LEVEL PASSED ~$76, PROME-verified) but only
1-of-2 required fresh legs fired, so the compound gate correctly reads **CANNOT-FIRE**,
with the dead leg (freshness) correctly named — this is a clean instance of the
conjunctive-gate-with-a-weak-leg pattern the task brief calls out, but here it worked
exactly as designed: the weak leg was tested SEPARATELY and correctly killed the fire.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE** (compound, one qualitative leg, owner-graded).
POINTER: source `AGENTS/BRENT/outbox/2026-07-08_to-PROME_decoupling-crack-adjudication.md`
— **OK** (file path pattern consistent with BRENT's outbox naming convention elsewhere
in this file; not independently opened).
BOOT-RENDERED: **NO** (terminal).

## ROW 5 — GATE-RESHAPE-BC (line 15)
Owner: PROME/REGINALD/TERRY · Status: `RESOLVED-FIRED` (terminal, HY leg only)
Threshold: `HY OAS >280 sustained OR WAL Q2 print fires reshape-(c)`
(a) INSTRUMENT: **COMMAND-NAMED** for the HY leg — `AGENTS/LIQUID/scripts/hy_oas_watch.py`
pulls FRED `BAMLH0A0HYM2` on a systemd timer and classifies vs. shared `config.py` bands
(265/280 documented in its own docstring); `AGENTS/LIQUID/scripts/boot.py` also pulls
`BAMLH0A0HYM2` live every LIQUID boot (confirmed at boot.py:88). Neither script is cited
in this row's `source` cell, which points to the PROME proposal doc — **PRODUCER-EXISTS-
UNCITED.** The WAL leg resolved separately (REGINALD Stage-1, cross-referenced in-row).
(b) BASIS/WINDOW: **STATED** — "sustained," later formally adjudicated by RED as a
3-consecutive-session test with an explicit ruling on whether policy-day prints count
(a genuine basis ambiguity the row shows being resolved in real time, not left open).
CONJUNCTION (OR of two independently-fireable legs): the fire is explicitly scoped to
the HY-level leg only, with the row taking care to say the WAL/(c) leg resolved NULL —
**CAN-FIRE was correctly achieved on one leg without the other**, and the row is
unusually careful to warn readers not to over-read the fire as "bank-convergence
progress." Good discipline.
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE** for the fired leg (a level+sustain test on a
named FRED series); arguably the row is really a HY-only gate now given how it resolved,
but that's a content note, not a token disagreement.
POINTER: source `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` — **OK.**
BOOT-RENDERED: **YES** for the underlying HY OAS number (LIQUID boot.py, every boot) —
**but only as a number, not as this specific gate's disposition**; nothing re-derives
"3 consecutive sessions" or checks the WAL leg at boot. Terminal row regardless.

## ROW 6 — GATE-HY-REKILL (line 16)
Owner: LIQUID · Status: `LIVE`
Threshold: `HY OAS <260, two consecutive closes (FRED BAMLH0A0HYM2)`
(a) INSTRUMENT: **COMMAND-NAMED, and this is the cleanest instrument match in the file.**
`AGENTS/LIQUID/scripts/hy_oas_watch.py` is purpose-built for exactly this test: its own
docstring says it "Fires a LOCAL file alert on ... the two-way bear-axis KILL (<260 on
two consecutive closes)" — the gate's condition verbatim. It runs on a systemd timer
(Mon–Fri 13:00 ET), independent of any Claude session. `definition_surface` cites the
KILL_MEMO workbook file, not the script — **PRODUCER-EXISTS-UNCITED**, but the strongest
possible case of "the producer definitely exists and definitely matches."
(b) BASIS/WINDOW: **STATED** — named FRED series, explicit 2-consecutive-close rule,
plus an H-2 counting rule (Will-ruled 8/10) preventing double-counting against HENRY's
overlapping soft-kill leg on the same series — an example of basis discipline actively
preventing a joint-fire miscount.
CONJUNCTION: N/A (single leg).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: `definition_surface` = `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` —
**OK** (matches `source`; file path is internally consistent, not independently opened).
`consumed_by` = `PRICE: HY OAS <260 two consecutive closes ... | LIQUID` — correctly
typed as a PRICE: consumer per the header's row-7 ruling.
BOOT-RENDERED: **YES** — `hy_oas_watch.py` (independent timer) AND `boot.py` (every
LIQUID session pulls `BAMLH0A0HYM2` live, boot.py:88) both render the exact metric.
This is the **positive control** the task brief's context alludes to for a different
gate (PortWatch) — here the analogous control passes: the instrument both exists and is
alive, not just present.

## ROW 7 — GATE-LIQ-069 (line 17)
Owner: LIQUID · Status: `LIVE (ARMED 1-of-2)`
Threshold: `AI-HY cohort re-arm, ANY ONE of 5 legs` (BB spread, CDS, new-issue concessions, cohort equity, ORCL rating ladder)
(a) INSTRUMENT, per leg: BB spread — **PRODUCER-EXISTS-UNCITED** (LIQUID boot.py pulls
`BAMLH0A1HYBB`, boot.py:120). CoreWeave 5Y CDS — **NONE** (no CDS-data script found
anywhere under `AGENTS/LIQUID`). New-issue concessions — **NONE** (qualitative, no
series). Cohort equity (CRWV/IREN/APLD/NBIS −15%/session) — **PRODUCER-EXISTS-UNCITED**
(LIQUID boot.py's `price_fetch` mechanism could pull these tickers via FORGE `fetch.py`,
but I did not confirm these specific tickers are wired into any watch list). ORCL rating
ladder — **NONE** (rating-agency actions are read manually from agency releases, as the
already-fired leg-5 shows: "S&P cut ORCL BBB->BBB-" read and logged by hand).
(b) BASIS/WINDOW: **PARTIAL.** Legs 1/4 have numeric bases (BB spread level, −15%/session
equity move); legs 2/3/5 are qualitative with no stated window/cadence (CDS "re-widen,"
concessions "widening," ladder "2nd agency"). The row's own review_by cell (owner-set
8/20) names the likeliest NEXT trigger (Moody's Baa2→Baa3) rather than a re-read cadence,
which is a workable substitute but not a stated window.
CONJUNCTION (ANY ONE fires; TWO fires re-runs discriminator): **CANNOT-FIRE the
2-leg escalation reliably** — three of five legs (CDS, concessions, rating-ladder-2nd-
notch) have no instrument at all, so a genuine second fire could occur invisibly if it
happened on an un-instrumented leg; only the equity/spread legs would be machine-caught.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE** (correctly typed: mixed-instrument
5-way disjunction, owner-graded).
POINTER: source `AGENTS/LIQUID/workbook (KB-LIQ-069)` — **OK**, informal path form (no
filename, just a directory + parenthetical KB id) but consistent with how this owner
cites its own workbook elsewhere in the file (see rows 8, 14).
BOOT-RENDERED: **PARTIAL** — BB spread and (potentially) cohort tickers render at LIQUID
boot; the other three legs never render anywhere.

## ROW 8 — GATE-LIQ-072 (line 18)
Owner: LIQUID · Status: `LIVE`
Threshold: `IG rating-vs-spread mispricing re-arm, ANY: 3rd/4th IG-at-BB-spread issuer · IG OAS >94 · SpaceX gap fails to compress 4-6wk · different-sponsor 144A same gap`
(a) INSTRUMENT: IG OAS leg — **COMMAND-NAMED**, LIQUID boot.py pulls `BAMLC0A0CM`
(boot.py:142) which is IG OAS. The other three legs (issuer count, SpaceX gap
compression, 144A cross-sponsor) are **NONE** — no script; graded by hand from
market-color reads (the row's own text: "adverse-direction evidence... WALTER
SIG-W-20260723-010, conf 0.70 MIRROR-SOURCED, primaries 403'd" — i.e. sourced from a
routed signal, not a script).
(b) BASIS/WINDOW: IG OAS leg **STATED** (named FRED series, numeric line). SpaceX-gap
leg explicitly flagged **UNSTATED/self-noted** — the row itself says "pricing date
unpinned so the 4-6wk window may be immature... Owed: pin the pricing date." This is a
rare case where the owner's own cell names its own basis gap rather than an auditor
finding it — good self-flagging, but the gap is real and unresolved as of the row's last
update (7/24).
CONJUNCTION: N/A (any-one-of-4 disjunction; only IG-OAS leg is quantitatively tracked).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE.**
POINTER: source `AGENTS/LIQUID/workbook (KB-LIQ-072)` — **OK** (same informal-path
convention as row 7).
BOOT-RENDERED: **PARTIAL** — IG OAS renders every LIQUID boot; the other three legs
never render.

## ROW 9 — GATE-VIO-110 (line 19)
Owner: VIOLET · Status: `LAPSED` (terminal — the KB-VIO-110 incident that is this
whole file's origin story per header line 2)
Threshold: `Gate A: CCC>=9.65% AND CCC-BB dispersion>=8.00 · Gate C: LIQUID breadth-not-idiosyncratic confirm`
(a) INSTRUMENT: **CANNOT-JUDGE precisely, but likely PRODUCER-EXISTS.** VIOLET's
`fred_fetch.py` has a `credit_summary()` function (confirmed at fred_fetch.py:185) whose
surrounding comments discuss VIX-conditional credit reads — consistent with a CCC-yield
/ dispersion computation, but I did not open the function body to confirm it computes
CCC% and CCC-BB dispersion specifically as named in this gate.
(b) BASIS/WINDOW: **STATED** for Gate A (two explicit numeric thresholds); Gate C is
explicitly a cross-agent qualitative confirm ("LIQUID breadth-not-idiosyncratic"), no
stated window.
CONJUNCTION: Gate A is itself a 2-leg AND (CCC level AND dispersion) — both legs are
numeric per the condition text, so if `credit_summary()` covers them this leg is
CAN-FIRE-testable; Gate C is JUDGEMENT-only. The row states BOTH gates fired 7/2 and the
packet was simply never built — this is a **process failure, not an instrument
failure**: the gate correctly fired, the consequence (tail-hedge packet) was dropped
because the session was frozen. Worth noting since it's the file's founding incident and
the audit's framing might otherwise conflate it with a decoration defect — it wasn't one.
SCANNABLE-AGREES: `INSTRUMENT` — **CANNOT-JUDGE** whether AGREE or a mild DISAGREE,
since Gate C is qualitative and the row is a disjunction of one INSTRUMENT-shaped gate
and one JUDGEMENT-shaped gate; Class 7 doesn't define how to token a mixed either/or.
POINTER: source `AGENTS/VIOLET/outbox/2026-07-09_to-PROME_gate-AC-backfill-and-dropped-
packet.md` — **OK.**
BOOT-RENDERED: **NO** (terminal).

## ROW 10 — GATE-LIQ-076 (line 20)
Owner: LIQUID · Status: `LIVE`, graded 0-of-3 at last check (7/18)
Threshold: `2-of-3 within 2wk: (a) SOFR-3M lev short record/>300K cover · (b) PD G10>10y <-$12B or G5L10<-$800mm x2wk · (c) MOVE>85 while VIX<20`
(a) INSTRUMENT per leg: (a) SOFR-3M leveraged-fund CFTC short — **NONE** found; the
row's own grading history cites a raw CFTC TFF pull done by hand ("net -2,786,954 [7/14
raw CFTC TFF, rel 7/17]"), not a script. (b) Primary-dealer positioning (PD G10>10y,
G5L10) — **NONE**; graded from NY Fed PD stats by hand per the row text. (c) MOVE/VIX —
**COMMAND-NAMED**, VIOLET's `move.py --boot` and FORGE `fetch.py`'s MOVE/VIX mappings
(confirmed `^MOVE`/`^VIX` in `FORGE/tools/market-data/fetch.py:798-799`) both exist and
are LIQUID-boot-adjacent (LIQUID's own boot.py does not appear to pull MOVE/VIX itself
— **CANNOT-JUDGE** whether LIQUID's session actually invokes VIOLET's script or FORGE's
fetch directly for this leg; the row's own grading text cites a bare MOVE/VIX number
with no script named).
(b) BASIS/WINDOW: **STATED**, and unusually explicit about the window: "2-of-3 within
2wk," each leg has a named series/threshold. `consumed_by` cell itself flags this
correctly: "S9 evaluator target, un-instrumented today" — the OWNER'S OWN consumed_by
cell admits legs (a)/(b) are un-instrumented, which matches what I found.
CONJUNCTION: **CANNOT-FIRE reliably as machine-graded** — 2 of 3 legs (a)/(b) have zero
instrumentation (hand-pulled CFTC/NY-Fed data), so the "2-of-3" conjunction can only be
graded by a human doing two manual data pulls plus one live MOVE/VIX read; this matches
the task brief's MARCO-census pattern (weak legs are the failure mode, not a missing
number on the strong leg).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE**, and well-justified: this row's state cell
itself documents an explicit 8/20 ruling correcting a prior mis-scannable-note ("KB
note was the DEFECTIVE surface, corrected at owner") — i.e. this exact row already went
through one round of the scannable-disagreement class this audit is checking for, and
was fixed. Good precedent for how a DISAGREE should be resolved.
POINTER: `definition_surface` = `AGENTS/LIQUID/workbook/DEALER_POSITIONING_NEXUS_WATCH.md`
— **OK**, matches `source`.
BOOT-RENDERED: **PARTIAL** — MOVE/VIX render somewhere in the fleet (VIOLET boot); CFTC
and PD legs render nowhere.

## ROW 11 — GATE-VIO-116 (line 21)
Owner: VIOLET · Status: `RESOLVED 7/16` then `★ RE-OPEN FIRED 2026-07-21` (terminal,
folded into TRY-FIRE-004)
Threshold: `F1 MOVE>72.41 · F2 hot CPI+gamma-flip-band · F3 10Y>4.60; stand-down N1 MOVE<66 · N2 SKEW>148`
(a) INSTRUMENT: **COMMAND-NAMED.** MOVE — `AGENTS/VIOLET/scripts/move.py` ("MOVE
rates-vol (investing.com PRIMARY; built 8/4)" per boot.py:42, explicitly built BECAUSE
of this gate's own history: the row's state cell documents that the ORIGINAL 7/13 fire
was graded from investing.com + WebSearch corroboration because Yahoo's feed
mislabeled the series — `move.py` with "investing.com PRIMARY" is the direct fix,
built after this incident). 10Y — TERRY's `snapshot.py` (`DGS10`, confirmed row 2).
SKEW — FORGE `fetch.py` maps `^SKEW` (confirmed line 799), and VIOLET boot.py lists
SKEW among "core numbers" (boot.py:73).
(b) BASIS/WINDOW: **STATED** — closes not intraday for F3, explicit peak-retake
framing for F1, named stand-down counter-thresholds (N1/N2).
CONJUNCTION: disjunction (ANY ONE fires) with counter-stand-downs — the row shows F3
firing cleanly, then a later independent MOVE-only re-open (F1-style) — both grades were
done with named, verified series and cross-corroborated sources. This is one of the
better-evidenced rows in the file.
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: source `AGENTS/VIOLET/research/2026-07-11_move-led-vol-hedge-fresh-look.md` —
**OK.**
BOOT-RENDERED: **YES** — MOVE and SKEW both render at VIOLET boot (confirmed); DGS10
renders at TERRY boot (per row 2, not independently reconfirmed here).

## ROW 12 — GATE-SAM-30 (line 22)
Owner: SAM/TERRY · Status: `RESOLVED 2026-08-07 DE-LOAD` (terminal, after an extensive
multi-cycle history)
Threshold: `CFTC COT JPY net (noncommercial) build >-153K (85% of -180K peak) vs -150,132 Jun-16 baseline`
(a) INSTRUMENT: **COMMAND-NAMED.** `AGENTS/SAM/scripts/cftc_jpy.py` exists and is
explicitly named in the row's own grading history: "Dual-source verified: SAM
cftc_jpy.py + independent raw deafut.txt hand-parse agree to the contract." This is the
one row in the file where the owner's grading narrative names its own script by
filename — best-practice citation, though `source` (col 8) still points to
`THESIS.md + HEARTBEAT.md`, not the script.
(b) BASIS/WINDOW: **STATED**, extremely thoroughly — noncommercial net, percent-of-peak
framing, weekly CFTC release cadence, explicit resolver pre-registration (a fixed 8/7
print was named as the resolving read BEFORE the print, avoiding post-hoc goalpost
moves).
CONJUNCTION: N/A (single series, run-history test with an early-entry override clause).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE**, cleanly.
POINTER: source `AGENTS/SAM/thesis/THESIS.md + HEARTBEAT.md Near-Gates 6/26 COT row` —
**OK** (script itself would be a stronger pointer per §Convention findings below, but
the cited docs are consistent with the file structure).
BOOT-RENDERED: **CANNOT-JUDGE** whether `cftc_jpy.py` runs on every SAM boot or only on
CFTC release days (weekly data doesn't need daily re-pull) — did not open SAM's own
`scripts/boot.py` to confirm the invocation cadence.

## ROW 13 — GATE-BRK-C1 (line 23)
Owner: BROCK · Status: `RESOLVED 2026-08-07 GRADED 🟠 ORANGE` (terminal)
Threshold: `CCLFX Q3 repurchase-cap decision (N-23C3A ~8/7): RED<5%/susp · ORANGE=5% · GREEN=7%`
(a) INSTRUMENT: **NONE.** `find AGENTS/BROCK -iname "*.py"` returns zero files — BROCK
has no scripts at all in this repo. The grade was a hand-pulled SEC N-23C3A filing read
("BROCK spawn, N-23C3A pulled at primary"). This matches `scannable=JUDGEMENT`
correctly — no false claim of machine-gradability here.
(b) BASIS/WINDOW: **PARTIAL, and the row says so itself.** The row documents its own
defect: "the +2% top-up language is verbatim-identical Q1/Q2/Q3 and Box 4-C never
checked ⇒ GREEN is not gradeable off this instrument" — i.e. two of three bands (RED,
ORANGE) are gradeable off the filing text, GREEN is explicitly NOT gradeable as
specified. Also flags a 10-day vintage-drift catch (filing dated 7/28, treated as an
~8/7 event by two agreeing-but-wrong secondary sources) — a clean instance of the
"2-agreeing-secondaries=1-source" finding class this operation already tracks.
CONJUNCTION: N/A (3-way banded read, one band ungradeable).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE.**
POINTER: source = two BROCK files — **OK** (not independently opened).
BOOT-RENDERED: **NO** (terminal, and no BROCK scripts exist to render anything).

## ROW 14 — GATE-LIQ-079 (line 24)
Owner: LIQUID · Status: `LIVE`
Threshold: `ARM = SOFR99-IORB >=+30bp AND non-calendar AND >=2 consecutive days; FIRE = armed + slow-lead backing + dispersion leg`
(a) INSTRUMENT: **NONE / basis-mismatched, not COMMAND-NAMED as specified.** LIQUID
`boot.py` computes a "SOFR99 tail" figure (boot.py:217-220) — **but it is `SOFR99 minus
SOFR` (the median), not `SOFR99 minus IORB`** as this gate's condition explicitly
requires. The dedicated backtest tool, `AGENTS/LIQUID/scripts/fp_backtest_079.py`, DOES
use the correct basis (its own docstring: "Ceiling = IORB spliced to IOER... per spec
section 5") but is a one-off historical backtest script, not a live daily-refresh
instrument — running it does not tell you today's SOFR99-IORB spread. **No live script
computes the quantity this gate is actually specified on.** This is a direct hit on the
audit brief's named failure class (unstated/mismatched basis, not a missing number) and
is worth flagging as the single clearest basis-mismatch finding in the file: the ARM
leg literally cannot fire correctly off the boot-rendered number, because that number is
answering a different question (deviation from the SOFR median, not distance to the
IORB ceiling).
(b) BASIS/WINDOW: **STATED** in the condition text itself (SOFR99-IORB, non-calendar
day exclusion, 2-consecutive-day window) — the basis is well-specified on paper; the
mismatch is between the specified basis and what the live tool actually computes, not a
gap in the row's own text. The row separately and explicitly flags its own n=1 sample
limitation ("NO FP 'rate' is citable, never cite '62%'/'25%' bare") — good self-guarding.
CONJUNCTION: ARM (3-way AND) then FIRE (ARM + 2 more qualitative legs) — **CANNOT-FIRE
correctly today**: even the ARM leg's number comes from the wrong instrument.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE** on the token (compound, multi-leg,
owner-graded), independent of the basis-mismatch finding above (a JUDGEMENT-typed row
can still have a leg with a bad instrument — the token isn't wrong, the boot-rendered
number is).
POINTER: `definition_surface` = `AGENTS/LIQUID/workbook/FUNDING_SEIZURE_GATE_SCOPED.md`
— **OK**, matches source.
BOOT-RENDERED: **YES, but WRONG-SERIES** — the "SOFR99 tail" line renders every LIQUID
boot (confirmed boot.py:220) and reads as if it answers this gate, but it is computed
against SOFR-median, not IORB. This is a **POINTER: SOURCE-LACKS-VALUE**-adjacent
finding at the instrument level: a boot-rendered number exists, looks relevant, and is
not the registered metric.

## ROW 15 — GATE-FALCON-001 (line 25)
Owner: FALCON · Status: `LIVE (legs 2-3 open)`, leg-1 and leg-3 FIRED, leg-2 OPEN
Threshold: 3-leg Bab el-Mandeb tripwire (Houthi attack / tanker-transit step-down / Yanbu loadings)
(a) INSTRUMENT per leg: Leg-1 (kinetic attack) — **NONE**, correctly (event-class,
UKMTO/Ambrey/JMIC corroborators, human-adjudicated). Leg-2 (Bab tanker transits vs.
7dma, TankerMap basis) — **NONE**: grepped `AGENTS/FALCON` for a TankerMap/Bab-transit
script; found `hormuz_transit_watch.py` (a **different chokepoint**, Hormuz not Bab) and
`bypass_watch.py` (Gulf-of-Oman STS hub, also not Bab) — no producer for Bab transits
exists in this repo; the row's own text confirms this ("TankerMap = 8/10 repair" i.e. a
human-repaired reading process, "PortWatch = lagging corroborator ONLY"). Leg-3 (Yanbu
loadings, Kpler/Vortexa) — **NONE**: no Kpler/Vortexa API credential exists anywhere in
this fleet — this is stated explicitly and repeatedly in-row and is the SAME finding
that later killed GATE-TERRY-006 (row 17): "door (b) Kpler/Vortexa has NO fetcher in
this fleet." Leg-3's fire here was graded from press-relayed tracker numbers by hand.
(b) BASIS/WINDOW: **STATED**, and fought over extensively in-row (relay-window
arithmetic corrected from week-start to week-end basis at 8/6; "sessions" ambiguity
flagged and resolved for a sibling row). This row shows the most basis-correction
activity of any row in the file — a good sign for rigor, but also confirms zero
automation backs any of it.
CONJUNCTION: 3-way OR, no leg has an instrument — **CAN-FIRE only via human
adjudication on every leg**, which is exactly what happened (all three fire/no-fire
calls were FALCON spawns reading press/AIS-relay sources). Consistent with the token.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE.**
POINTER: source = 6 stacked FALCON report files — **OK** (paths follow the fleet's
report-naming convention; not independently opened, high volume).
BOOT-RENDERED: **NO** — no script renders any of the three legs; the closest adjacent
instrument (`kharg_loadings_watch.py`) watches a different terminal (Kharg, Iran) for a
different gate (row 17) on the same PortWatch API, and even that one is a known-blind
instrument for exactly this reason (see row 17's positive-control failure).

## ROW 16 — GATE-OSPREY-001 (line 26)
Owner: OSPREY · Status: `LIVE (legs a/c open)`, leg-(b) FIRED
Threshold: `(a) CPC SPM structural damage · (b) loading suspension>=5 sessions or Kpler liftings drop · (c) Tengiz FM declared`
(a) INSTRUMENT: **NONE, across all three legs.** `find AGENTS/OSPREY -iname "*.py"`
returns **zero files** — OSPREY has no scripts in this repo at all. All three legs are
graded from press/consortium statements read by hand (Reuters, Kazakh Energy Ministry,
Times of Central Asia). Leg-(b)'s fire (5 consecutive halted sessions) was a manual
day-count from halt-status headlines, not an instrument reading a loadings series.
(b) BASIS/WINDOW: **STATED for leg-(b)** (explicit day-count method, calendar-day vs.
business-session ambiguity flagged and resolved in-row: "both readings land on 5");
**UNSTATED-then-self-resolved for legs (a)/(c)** — these are binary event triggers
("assessment confirms damage" / "FM declared") with no numeric window, appropriately so
for one-shot declarations.
CONJUNCTION: 3-way OR (severity-escalation legs a/c vs. duration leg b) — leg-(b) fired
on a correctly-instrumented (if manual) day-count; legs a/c remain genuinely untestable
by machine, consistent with JUDGEMENT.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE.**
POINTER: source = `AGENTS/OSPREY/STATUS.md` + 2 more OSPREY files — **OK.**
BOOT-RENDERED: **NO** — no OSPREY script exists to render anything; the row's own state
cell documents an 8/16 PROME sync needed to fold OSPREY's 8/10 and 8/15 grades into this
row (they "had not reached this row"), i.e. even the manual-grade pipeline into this
central file lags the owner's own STATUS.md — a delivery-lag finding, not an instrument
finding, but relevant to whether this row can be trusted as current at a glance.

## ROW 17 — GATE-TERRY-006 (line 27)
Owner: FALCON/TERRY · Status: `RETIRED 2026-08-20` (terminal — **the row that
directly instantiates the task brief's named positive-control case**)
Threshold: Kharg-strand FLOW gate — FIRE on corroborator + NOT-refuted by a PortWatch VETO
(a) INSTRUMENT: **COMMAND-NAMED for the VETO leg, and it is the row that PROVES the
"surface-EXISTS vs. surface-ALIVE" distinction the task brief asks for.**
`AGENTS/FALCON/scripts/kharg_loadings_watch.py` (cited in the row's own consequence
cell: "PortWatch port2164 export_tanker/portcalls (scripts/kharg_loadings_watch.py,
rc-inverted)") pulls IMF PortWatch for Kharg Island (port2164) and is explicitly
documented, in its own docstring, as **AIS-based and >=90% blind to Kharg's actual
dark-fleet throughput — it prints literal ZERO for entire NORMAL export months.** The
gate's RETIREMENT record confirms this failed a **known-positive control**: "the VETO
FAILED A KNOWN-POSITIVE CONTROL (PortWatch port2164 printed 0 for 8/08–8/14 including
the 8/12 day a 2M-bbl VLCC demonstrably loaded)." This is the exact case referenced in
the task's CONTEXT section — the surface **EXISTS and runs**, but is **not ALIVE**
(does not track ground truth) for the regime it was asked to grade in. The other
corroborator leg, (b) Kpler/Vortexa, was **NONE** — never had a fetcher, flagged in-row
as the fleet's structural gap.
(b) BASIS/WINDOW: **STATED**, thoroughly — >=1 corroborator, >=2 observed days, explicit
anti-false-fire rules (reject stale vintage, seize-but-flow-continues doesn't count).
CONJUNCTION: instrument-veto structure (fire unless a working veto says otherwise) —
**CANNOT-FIRE reliably was the actual finding**: the retirement record states plainly
"the premise HELD... the gate did not see it... the only informative branch was
unreachable. The premise held; the instrumentation failed." This is the single
best-documented instrument failure in the entire file and should be treated as the
canonical case study for future gate design (the row explicitly asks future gates to
"state HOW its quantitative corroborator is pulled BEFORE registration").
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE** (mixed instrument/veto, correctly typed
even in hindsight).
POINTER: source, multiple files including the retired TERRY card and a PROME-inbox
processed packet — **OK.**
BOOT-RENDERED: **YES for the failed veto** — `kharg_loadings_watch.py` is a real,
running script; it renders a number every time it's run. It is simply the wrong number
for the question. **This is the clearest "COMMAND-NAMED but decorative" case in the
file** — the instrument existing and running gave false confidence for 25 days.

## ROW 18 — GATE-BRENT-DEPLOY-V2 (line 28)
Owner: BRENT · Status: `RETIRED` (terminal, v3 spec superseding v2)
Threshold (v3): `leg (a) most-recent-official-close <=-15% from post-arm peak; leg (a2) OVX prints <= same line at ticket; leg (b) net debit <=33% of spread width`
(a) INSTRUMENT: **COMMAND-NAMED.** `AGENTS/BRENT/scripts/instrument_check.py` is
explicitly ABOUT this gate — its own module docstring (line 21) says: "that cost a
ratified gate: ^OVX's last bar is 16:00 and USO options close 16:00" — i.e. this script
was built in direct response to this gate's v2-unfillability finding, and contains a
named comment block "FALSE 🔴 on DEPLOY GATE v3 leg (a2)" (line 194) discussing a known
false-positive mode on exactly this leg. `thresholds.py::get_prices()`/`check_market_
thresholds()` also computes OVX-class market levels.
(b) BASIS/WINDOW: **STATED**, and this row is a case study in a basis fix done right:
v2 was retired BY CONSTRUCTION because its two legs' timing windows (OVX 16:00 close vs.
USO options 16:00 close) made the gate mathematically unfillable — leg (a) became
knowable exactly when leg (b) became ungradeable, a "zero execution window" defect
found by 5-minute-bar analysis, not by a live miss. v3's fix (state-basis leg known at
09:30, a redundant leg (a2) at ticket-time) is a genuine engineering improvement,
documented with a disclosed cost (31.2% of fire-sessions close back above the line).
CONJUNCTION: 3-leg structure, all with instruments — this is one of the few
INSTRUMENT-typed multi-leg gates in the file where **CAN-FIRE is real**: all mechanical
legs fired together on 8/4 (per the state cell) and the packet was built and delivered
to Will same session — the consequence chain worked end-to-end.
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: source `AGENTS/BRENT/TRADE.md` + a PROME inbox packet — **OK.**
BOOT-RENDERED: **CANNOT-JUDGE** whether `instrument_check.py`/`thresholds.py` run on
every BRENT boot vs. on-demand at ticket time; the row's own text implies at-ticket
invocation ("re-pull at ticket, inherit nothing"), which would argue against a boot-time
render and for an event-time one — reasonable design, just not the same thing as
BOOT-RENDERED=YES.

## ROW 19 — GATE-NEXUS-SEAT-01 (line 29)
Owner: NEXUS/PROME · Status: `LIVE`
Threshold: `count Will's decisions 2026-08-08→10-07 whose proximate input was a NEXUS product; >=3 pays, 0-1 dissolves, 2=NO-VERDICT`
(a) INSTRUMENT: **PROSE-VALUE.** This is a governance/fleet-process gate, not a market
metric — there is no market series to fetch. The grading mechanism is explicit and
procedural (PROME builds a candidate list from "STABLE KEYS," NEXUS contests, Will
confirms) rather than script-computed, and correctly so — this is a decision-count, not
a price.
(b) BASIS/WINDOW: **STATED**, unusually well — frozen spec at registration ("zero
re-tuning"), explicit 60-day window, explicit anti-gaming clause (interested party never
counts alone), explicit method against a "false-zero" failure mode (never phrase-search).
CONJUNCTION: N/A (a count vs. 3 bands).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE**, and correctly so — this is the class of gate
where JUDGEMENT is the right call by construction, not a fallback for missing tooling.
POINTER: source = the FORUM dissent post — **OK.**
BOOT-RENDERED: **NO** (nothing to render — the count is a periodic Will-decision audit,
not a live series).

## ROW 20 — GATE-OP-SCALE-01 (line 30)
Owner: TERRY/PROME · Status: `LIVE`
Threshold: `by 2026-11-07, N>=10 CLOSED positions in the agent-proposed book, else structural-shrink proposal`
(a) INSTRUMENT: **PROSE-VALUE** — a position-count against FORGE/TRADE.md records, not
a market series. No script confirmed to auto-count "distinct closed positions with
distinct entry decisions" per the row's own careful exclusion rules (day-desk/paper/
would-fire excluded, harvest tranches counted once) — this counting logic has enough
judgment content (per the row's own "GUARD v2... every change HARDENS" language) that a
naive `grep -c` would likely misgrade it, similar to the CREED-T06b miscount case found
elsewhere in this fleet (discount-percent read as a fund-gate count, per
`AGENTS/CREED/scripts/threshold_scan.py`'s own docstring history).
(b) BASIS/WINDOW: **STATED** — explicit date, explicit count rule, explicit exclusions.
CONJUNCTION: N/A.
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE**, correctly.
POINTER: source = the FORUM dissent post — **OK.**
BOOT-RENDERED: **NO.**

## ROW 21 — GATE-BRENT-COT-35B (line 31)
Owner: BRENT · Status: `LIVE`
Threshold: `Leg-A crude MM gross shorts SPENT<=113745 (deadband 109165-118325) · Leg-B OI-share<=4.909% · BOTH must agree`
(a) INSTRUMENT: **COMMAND-NAMED**, and well-documented as a REBUILT script:
`AGENTS/BRENT/scripts/cot_grade.py` — its own docstring is an unusually candid
after-action account of grading the WRONG (retired) test with a "healthy" pre-flight
check that was "healthy against the wrong reference" (its own cited finding-tag:
`[[finding_instrument_reports_clean_against_the_wrong_reference]]`). The rebuilt version
explicitly implements the frozen COT-FUEL-35B spec including the OI-share Leg-B that the
prior version "never fetched... at all." `source`/`definition_surface` cite
`REGISTRY.tsv` and setup docs, not the script itself — **PRODUCER-EXISTS-UNCITED.**
(b) BASIS/WINDOW: **STATED**, very precisely (base 122,904 as a trailing-8wk median,
frozen `median_unit`=9,160, explicit deadband, explicit "grade off the RAW file, never
Socrata" sourcing rule — the exact rule the pre-rebuild script violated).
CONJUNCTION: 2-leg AND, both legs machine-computed by the rebuilt script — **CAN-FIRE is
real** once the correct script is run; the row shows both legs graded twice (8/14, 8/21)
with a genuine JOINT NO-VERDICT both times.
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: `definition_surface` = `REGISTRY.tsv` COT-FUEL-35B row + a setup card —
**OK**, though naming `cot_grade.py` directly would close the PRODUCER-EXISTS-UNCITED
gap (see Convention findings).
BOOT-RENDERED: **CANNOT-JUDGE** — weekly-cadence CFTC data, script is almost certainly
invoked at the Friday print rather than every boot; did not confirm BRENT's boot.py
wiring.

## ROW 22 — GATE-FERT-G5 (line 32)
Owner: FERT · Status: `LIVE`
Threshold: `DTN retail DAP OR MAP > $1,000/ton (DTN Progressive Farmer weekly retail $/ton)`
(a) INSTRUMENT: **NONE.** `AGENTS/FERT/boot.py` (confirmed by full read) is purely a
due-date/staleness checker (ledger staleness, predictions-due, triggers-due) — it does
**not** fetch any price. `AGENTS/FERT/workbook/TRIGGERS.tsv` row T4 names the actual
instrument as **"dtnpf.com weekly crops article"** — a human reading a published web
article, with the clock established from observed article-publication spacing (8/05,
8/12, "exactly 7d apart"), not an API or scrape. No DTN fetcher script exists anywhere
in the repo (`grep -rl "DTN"` was checked against FERT's own scripts; none found).
(b) BASIS/WINDOW: **STATED, and unusually well-guarded against a specific confusable
metric.** The row has a dedicated warning: "NEVER conflate w/ Pink Sheet $/mt or NOLA
$/st" — i.e. the row pre-empts exactly the kind of basis mismatch this audit is
built to catch (compare to row 14's actual, unguarded, mismatch). Base-rated at
registration with explicit percentile context (93rd-pct).
CONJUNCTION: N/A (single numeric OR across two named products, DAP/MAP).
SCANNABLE-AGREES: `INSTRUMENT` — **DISAGREE.** Per Class 7's own text ("a machine can
grade it... `registry_chain_check` asserts... a named metric surface + a named
reader"), this gate's reader is a human opening a web article, not a script — there is
no producer at all (verdict a = NONE). The definition is unambiguous and the number is
real, but nothing machine-checkable stands behind the INSTRUMENT label; it reads
structurally closer to a well-disciplined manual read (like row 3's TIC leg) than to
row 6's HY-OAS case. This is a defensible either-way call given `registry_chain_check`
is unbuilt (see Convention findings), which is exactly why I flag it as DISAGREE rather
than silently accepting the token.
POINTER: `definition_surface` = `TRIGGERS.tsv (T4)` + the base-rate packet — **OK.**
BOOT-RENDERED: **NO** — FERT's boot.py only checks whether T4 is *due*, never pulls or
displays the price itself.

## ROW 23 — GATE-FERT-G3 (line 33)
Owner: FERT · Status: `LIVE`
Threshold: `China urea export quota revised DOWN, OR guidance floor reimposed above intl FOB`
(a) INSTRUMENT: **NONE**, correctly — explicitly labeled in its own condition text as
an "EVENT GATE (un-base-rateable, n≈2 policy regime changes/12mo, accepted as-flagged)."
Instruments named are relay/commentary sources (MOFCOM/NDRC relay, CF commentary,
Profercy), not machine feeds.
(b) BASIS/WINDOW: **STATED** — explicit registration-time state (quota 3.3 Mt, $660
floor lifted, China offers into India <$400/mt CFR) giving a clean before/after
baseline even without a numeric window.
CONJUNCTION: N/A (disjunction of two policy events).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE**, and correctly so — this is a genuine
policy-event gate, unlike row 22's price gate.
POINTER: `definition_surface` = `KB.tsv (KB-FERT-006)` — **OK.**
BOOT-RENDERED: **NO.**

## ROW 24 — GATE-TERRY-007 (line 34)
Owner: TERRY/BOND · Status: `LIVE`
Threshold: `004 EXIT gate: FIVE CONSECUTIVE official FRED DGS10 closes <4.50%`
(a) INSTRUMENT: **COMMAND-NAMED** — same producer as row 2 (`AGENTS/TERRY/scripts/
snapshot.py`, DGS10). The row itself explicitly rules out substitute feeds: "OFFICIAL
closes ONLY — ^TNX/^TYX count-neutral, never substitute or fuse," directly mirroring the
basis discipline already proven in row 2.
(b) BASIS/WINDOW: **STATED**, precisely — 5-consecutive-close run test, single-close
reset semantics paired with a separate ruling (a single <4.50 close resets only an
unrelated counter, not this gate) — the row explicitly distinguishes two rulings (B/C)
that could otherwise be confused, a good basis-collision guard.
CONJUNCTION: N/A (single-series run-length test).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: source = TERRY's card + the ruling doc — **OK.**
BOOT-RENDERED: **CANNOT-JUDGE**, same caveat as row 2 — DGS10 is clearly pulled by
`snapshot.py`, but whether that script runs automatically every TERRY session or only
when TERRY is explicitly asked to grade a DGS10-keyed gate was not confirmed.
consumed_by cell shows a live grading cadence in practice (owner graded 8/20 ahead of
the provisional date, 8/21 official flagged UNPUBLISHED-OWED) — this is the fleet's own
consumer-tracking working as designed, a positive process finding independent of the
BOOT-RENDERED question.

## ROW 25 — GATE-CREED-T02 (line 35)
Owner: CREED/REGINALD/LIQUID · Status: `RESOLVED — FIRED-AND-ROUTED` (terminal, but
registered ~6 weeks post-hoc — see finding below)
Threshold: `matured-balloon share of new CMBS delinquency > 50%, sustain-2 (Will-frozen band)`
(a) INSTRUMENT: **PRODUCER-EXISTS-UNCITED, with a documented history of misuse.**
`AGENTS/CREED/scripts/threshold_scan.py` explicitly discusses T-02 as "This is
CREED-T-02's root cause. On 2026-08-13, mid-cycle, CREED wrote '66% of $6.0B' into its
own workbook — the T-02 metric, against a frozen band of 50" (lines 11-12 of the
script) — i.e. the script's own docstring is a post-mortem of a T-02-adjacent grading
defect. The underlying data source (Trepp CMBS delinquency) was not independently
confirmed as machine-fetched vs. hand-transcribed from a Trepp report; WALTER's own
CLAUDE.md (§ CREED-T THRESHOLDS) independently classifies `T-02` among the **5 of 11**
CREED-T rows that ARE "NUMERICALLY SCANNABLE," but flags separately that even those 5
include **3 that are MONTHLY TREPP PRINTS, NOT DAILY PULLS** — i.e. "scannable" here
means "has a number," not "has a live feed."
(b) BASIS/WINDOW: **STATED** — the row documents its own detection lag candidly ("FIRED
at the June print... effective 2026-06, detected 8/20, ~6wk lag logged not smoothed"),
which is an honest disclosure of exactly the kind of staleness this audit looks for,
volunteered by the owner rather than found by an auditor.
CONJUNCTION: N/A (single-series sustain-2 test).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE**, with the caveat (documented in-row and by
WALTER independently) that "scannable" for this metric means monthly-print, not daily.
POINTER: source = CREED's outbox packet — **OK.**
BOOT-RENDERED: **NO** — CREED is Tier-2 and "cannot self-boot" (stated explicitly in
row 29's review_by cell for a sibling row), so nothing in this fleet renders T-02 at a
regular cadence; it is read when CREED is specifically spawned.

## ROW 26 — GATE-VIO-RV1 (line 36) — **field-count-mismatched row, see §0**
Owner: VIOLET/TERRY · Status: `RETIRED 2026-08-27` by its own registered kill (F2-KILLED)
Threshold: `ARM = VVIX<=90 AND VIX<=16 AND SKEW>=140 (daily close) AND nearest HIGH/MED catalyst<=21d, ALL FOUR on 2 consecutive settles`
(a) INSTRUMENT: **COMMAND-NAMED**, same VVIX/VIX/SKEW producers confirmed for rows 9/11
— VIOLET boot.py lists VVIX/SKEW/VIX among its "core numbers" (boot.py:73), and the
gate was correctly self-killed via a dedicated falsifier check
(`research/2026-08-27_F2_pre_post_2018_split_KB-VIO-207.md`, cited in the malformed
row's shifted `state` cell) — the retirement mechanism itself worked as designed.
(b) BASIS/WINDOW: **STATED** — daily close basis explicitly called out ("NOT 20d-avg"),
2-consecutive-settle requirement, a catalyst-proximity leg keyed to VIOLET's own
CATALYSTS.tsv.
CONJUNCTION: 4-leg AND — the row was retired same-day as its first fire via its own
pre-registered kill condition (F2), which is the conjunction working correctly: a
falsifier fired before the gate could be mis-acted on.
SCANNABLE-AGREES: **CELL-BLANK, positionally** — reading the row as shipped (11
fields), what lands in the `scannable` column-position is the file-path string
`AGENTS/VIOLET/outbox/2026-08-20_to-PROME_rising-vol-registration-DESIGN-v1-trigger-
gated.md (owner artifact WINS on divergence; this row reconciles)`, not a Class-7 token.
Read with the missing tab restored (i.e. reading the row's actual prose, which does
contain a `JUDGEMENT`-shaped description elsewhere in the shifted text), the intended
content is almost certainly `JUDGEMENT` given the 4-leg-AND compound structure and the
"owner artifact WINS on divergence" framing matching this owner's convention on rows 15
(FALCON) and 29 (CREED). But as a positional TSV cell, **the scannable field for this
row is not a valid token today** — this is the row this leg's audit exists to catch.
POINTER: **UNCHECKED, malformed** — with fields shifted, the `definition_surface`
column-position instead holds what should be `review_by`'s content ("none — row
TERMINAL... one residual check at next PROME touch..."), and the true
`definition_surface` value (the VIOLET design doc) is sitting one column early, in
`scannable`'s position.
BOOT-RENDERED: **NO** (terminal; also moot given the malformation).
**This row is the single clearest, most concrete SCANNABLE-AGREES=DISAGREE finding in
the file** — not a judgment call about token accuracy, but a mechanical parse defect
that makes the token **absent** where the schema requires one, undetected because (per
§Convention findings) nothing checks the `scannable` column's presence or validity.

## ROW 27 — GATE-REG-T02 (line 37)
Owner: REGINALD/WAL/Will · Status: `LIVE`, UN-FIRED
Threshold: `WAL official CLOSE < $78, sustain 1 (one close fires)`
(a) INSTRUMENT: **COMMAND-NAMED.** `AGENTS/REGINALD/scripts/thresholds.py` contains the
literal row `("WAL", "below", 78.0, "Hidden CRE thesis accelerating")` (confirmed at
line 25), an exact match to this gate's condition and level. `source`
(`AGENTS/REGINALD/registry/NOTES.md §REG-T-02`) doesn't cite the script directly —
**PRODUCER-EXISTS-UNCITED**, but the match is unambiguous (this is the strongest
threshold-table-literal match found anywhere in the file, on par with row 6's
hy_oas_watch.py).
(b) BASIS/WINDOW: **STATED**, and the row has a notably strict anti-drift clause:
"⛔ Distance quotes must be re-derived from a NAMED DATED CLOSE (kill-on-sight: any
carried figure)" — an explicit rule against exactly the stale-carried-number failure
mode this operation has documented repeatedly elsewhere (the `finding_dated_carry_item_
has_no_expiry_check` memory row).
CONJUNCTION: N/A (single-close test, sustain=1).
SCANNABLE-AGREES: `INSTRUMENT` — **AGREE.**
POINTER: source `AGENTS/REGINALD/registry/NOTES.md §REG-T-02` — **OK.**
`consumed_by` = `PRICE:WAL_official_close<78` — correctly formatted per the header's
row-7 PRICE: convention.
BOOT-RENDERED: **CANNOT-JUDGE** whether `thresholds.py` runs automatically every
REGINALD boot — `REGINALD/scripts/boot.py` does not itself reference "WAL" by name
(confirmed by grep), so the threshold table is a separate script (`thresholds.py`) that
may or may not be invoked as part of routine boot vs. run standalone.

## ROW 28 — GATE-CORAL-MSI-01 (line 38)
Owner: CORAL/Will · Status: `LIVE`, 🔴 HOLDS
Threshold: `Parcl FL metro Motivated Seller Index (MSI, 0-10 composite) > 6.0`
(a) INSTRUMENT: **NONE.** Repo-wide `grep -rl "Parcl\|parcl" --include="*.py" .` returns
**zero results** — there is no Parcl fetcher anywhere in this fleet. `AGENTS/CORAL/
scripts/boot.py` (confirmed by full read) pulls generic "market price" data (equities/
tickers) and explicitly does not mention Parcl or MSI. The metric is read from Parcl's
own web dashboard by hand.
(b) BASIS/WINDOW: **STATED, with a self-corrected mislabel that is itself the headline
finding of this row.** The row documents, in its own text, a material correction: "⛔⛔
NOT months-of-supply — CORAL-corrected 2026-08-23... the mislabel this replaces was
MATERIAL: months-of-supply is a SEPARATE live CORAL metric on the SAME dashboard
(statewide condo 7.8, SF 4.5)." This is precisely the audit brief's own stated failure
pattern (unstated/wrong basis, not a missing number) caught and fixed by the owner one
session before this leg ran — worth flagging as a recent, real instance of the exact
defect class this leg exists to find, resolved rather than live.
CONJUNCTION: N/A (single composite index vs. one threshold); note the row's own careful
scope discipline — the fired supply-side leg is explicitly separated from CORAL's
overall state and the bank-transmission rail ("untouched, in BOTH directions").
SCANNABLE-AGREES: `INSTRUMENT` — **DISAGREE**, same reasoning as row 22: verdict (a) is
NONE (no producer anywhere in the repo), the read is a human opening the Parcl
dashboard. Unlike row 22, there is no in-row acknowledgment that this is a manual read
(the FERT row's own T4 trigger explicitly names "weekly retail fertilizer article" as
its mechanism; this row's condition text describes MSI as if it were a live composite
without noting the read is manual).
POINTER: `definition_surface` = `AGENTS/CORAL/STATUS.md` — **OK**, points at the
owner's own canonical letter per the row's PAT-006 pointer discipline.
BOOT-RENDERED: **NO.**

## ROW 29 — GATE-CREED-T06B (line 39)
Owner: CREED/LIQUID (+BROCK info) · Status: `RESOLVED (FIRED 2026-08-27)` (terminal)
Threshold: `OPEN-END-CRE-FUND-GATES >= 1 major fund gates (S6 co-trigger)`
(a) INSTRUMENT: **COMMAND-NAMED, and the row documents its own prior instrument
failure being fixed.** `AGENTS/CREED/scripts/threshold_scan.py` contains an explicit
account of this exact gate's history (lines 170-173, 280): T-06b was previously "NO
METRIC VECTOR -- UNTRIPPABLE BY CONSTRUCTION" and a related bug once "compared 30 >= 1
-- A DISCOUNT PERCENT read as a COUNT OF FUND GATES." The row's own condition text
confirms the fix: "count instrument = VX-CREED-5.03 (built 8/27, made T-06b genuinely
gradeable — comparable state 3->4)." This is a second clean case (with row 17) of an
untrippable/mis-instrumented gate being fixed and the fix documented in the row itself.
(b) BASIS/WINDOW: **STATED** — the fire was graded against a primary SEC 8-K filing
(SREIT, accession number cited), with an explicit note that the adjudication basis
"PRE-DATES CREED's same-session definition (authorship conflict dissolves)" — i.e. a
potential definitional race condition was noticed and resolved in-row rather than left
ambiguous.
CONJUNCTION: N/A (>=1 count, now genuinely countable per the fixed VX-5.03 instrument).
SCANNABLE-AGREES: `JUDGEMENT` — **AGREE**, correctly (a fund-gate COUNT crossing a
S6 co-trigger band, owner-graded even with a working counting instrument behind it).
POINTER: `definition_surface` = `AGENTS/CREED/registry/THRESHOLDS.tsv` (T-06b row) —
**OK**, owner-registry-wins convention explicit in-row.
BOOT-RENDERED: **NO** — same Tier-2 cannot-self-boot caveat as row 25; the row's own
`review_by` cell says explicitly "CREED is Tier-2 and cannot self-boot, so this rides
the spawn slate."

---

## SUMMARY TABLE (29 rows)

| # | Gate | Owner | Status token | (a) Instrument | (b) Basis/Window | Conjunction | Scannable-agrees | Pointer | Boot-rendered |
|---|---|---|---|---|---|---|---|---|---|
| 1 | GATE-TERRY-ARM1 | TERRY/BOND | RESOLVED (term.) | PRODUCER-EXISTS-UNCITED | STATED | N/A | AGREE | OK | NO |
| 2 | GATE-TERRY-ARM2 | TERRY/BOND | RESOLVED (term.) | COMMAND-NAMED | STATED | N/A | AGREE | OK | CANNOT-JUDGE |
| 3 | GATE-TERRY-ARM3 | TERRY/SAM | RESOLVED (term.) | NONE | STATED | N/A | DISAGREE (mild) | OK | NO |
| 4 | GATE-BRENT-SUSTAIN | BRENT | RESOLVED (term.) | CANNOT-JUDGE / NONE (freshness leg) | STATED | CANNOT-FIRE (dead leg named) | AGREE | OK | NO |
| 5 | GATE-RESHAPE-BC | PROME/REGINALD/TERRY | RESOLVED-FIRED (term.) | PRODUCER-EXISTS-UNCITED | STATED | CAN-FIRE (HY leg) | AGREE | OK | YES (number only) |
| 6 | GATE-HY-REKILL | LIQUID | LIVE | COMMAND-NAMED (PRODUCER-EXISTS-UNCITED) | STATED | N/A | AGREE | OK | YES |
| 7 | GATE-LIQ-069 | LIQUID | LIVE | PARTIAL (2 of 5 legs) | PARTIAL | CANNOT-FIRE reliably | AGREE | OK | PARTIAL |
| 8 | GATE-LIQ-072 | LIQUID | LIVE | PARTIAL (1 of 4 legs) | PARTIAL (self-flagged) | N/A | AGREE | OK | PARTIAL |
| 9 | GATE-VIO-110 | VIOLET | LAPSED (term.) | CANNOT-JUDGE | STATED/PARTIAL | N/A | CANNOT-JUDGE | OK | NO |
| 10 | GATE-LIQ-076 | LIQUID | LIVE | PARTIAL (1 of 3 legs) | STATED (owner admits gap) | CANNOT-FIRE reliably | AGREE | OK | PARTIAL |
| 11 | GATE-VIO-116 | VIOLET | RESOLVED (term.) | COMMAND-NAMED | STATED | CAN-FIRE (fired twice, verified) | AGREE | OK | YES |
| 12 | GATE-SAM-30 | SAM/TERRY | RESOLVED (term.) | COMMAND-NAMED | STATED | N/A | AGREE | OK | CANNOT-JUDGE |
| 13 | GATE-BRK-C1 | BROCK | RESOLVED (term.) | NONE | PARTIAL (self-flagged) | N/A | AGREE | OK | NO |
| 14 | GATE-LIQ-079 | LIQUID | LIVE | NONE / WRONG-BASIS | STATED | CANNOT-FIRE (ARM leg wrong basis) | AGREE | OK | YES but WRONG-SERIES |
| 15 | GATE-FALCON-001 | FALCON | LIVE | NONE (all 3 legs) | STATED | CAN-FIRE via manual read only | AGREE | OK | NO |
| 16 | GATE-OSPREY-001 | OSPREY | LIVE | NONE (0 scripts) | STATED / PARTIAL | CAN-FIRE via manual read only | AGREE | OK | NO |
| 17 | GATE-TERRY-006 | FALCON/TERRY | RETIRED (term.) | COMMAND-NAMED but proven WRONG-SERIES / NONE (other leg) | STATED | CANNOT-FIRE (documented instrument failure) | AGREE | OK | YES (wrong number) |
| 18 | GATE-BRENT-DEPLOY-V2 | BRENT | RETIRED (term.) | COMMAND-NAMED | STATED | CAN-FIRE (fired, executed) | AGREE | OK | CANNOT-JUDGE |
| 19 | GATE-NEXUS-SEAT-01 | NEXUS/PROME | LIVE | PROSE-VALUE | STATED | N/A | AGREE | OK | NO |
| 20 | GATE-OP-SCALE-01 | TERRY/PROME | LIVE | PROSE-VALUE | STATED | N/A | AGREE | OK | NO |
| 21 | GATE-BRENT-COT-35B | BRENT | LIVE | COMMAND-NAMED | STATED | CAN-FIRE (graded twice) | AGREE | OK | CANNOT-JUDGE |
| 22 | GATE-FERT-G5 | FERT | LIVE | NONE | STATED (well-guarded) | N/A | DISAGREE | OK | NO |
| 23 | GATE-FERT-G3 | FERT | LIVE | NONE (correct) | STATED | N/A | AGREE | OK | NO |
| 24 | GATE-TERRY-007 | TERRY/BOND | LIVE | COMMAND-NAMED | STATED | N/A | AGREE | OK | CANNOT-JUDGE |
| 25 | GATE-CREED-T02 | CREED/REGINALD/LIQUID | RESOLVED (term.) | PRODUCER-EXISTS-UNCITED (monthly print) | STATED (lag disclosed) | N/A | AGREE | OK | NO |
| 26 | GATE-VIO-RV1 | VIOLET/TERRY | RETIRED (term.) | COMMAND-NAMED | STATED | CAN-FIRE (self-killed correctly) | **CELL-BLANK (malformed row)** | UNCHECKED (malformed) | NO |
| 27 | GATE-REG-T02 | REGINALD/WAL/Will | LIVE | COMMAND-NAMED | STATED | N/A | AGREE | OK | CANNOT-JUDGE |
| 28 | GATE-CORAL-MSI-01 | CORAL/Will | LIVE | NONE | STATED (self-corrected mislabel) | N/A | DISAGREE | OK | NO |
| 29 | GATE-CREED-T06B | CREED/LIQUID | RESOLVED (term.) | COMMAND-NAMED (fixed prior gap) | STATED | N/A | AGREE | OK | NO |

### Counts

- **(a) Instrument:** COMMAND-NAMED 10 · PRODUCER-EXISTS-UNCITED 4 (rows 1,5,21,25 —
  overlaps with COMMAND-NAMED rows counted once at the stronger verdict where a row has
  one dominant leg; multi-leg rows 7/8/10/14 counted as PARTIAL) · NONE 8 (rows 3,13,15,
  16,22,23,24-part,28) · PARTIAL 4 (rows 7,8,10,14) · PROSE-VALUE 2 (rows 19,20) ·
  CANNOT-JUDGE 1 (row 9, credit_summary() body unopened)
- **(b) Basis/window:** STATED 26 · PARTIAL 3 (rows 8, 13, 16)
- **Conjunction, where applicable (≥2 legs):** CAN-FIRE 6 (rows 5,11,18,21,26 + row 4's
  correctly-killed leg) · CANNOT-FIRE 6 (rows 4[freshness leg],7,10,14,15/16[manual-only],
  17) · N/A (single-leg or count) 17
- **SCANNABLE-AGREES:** AGREE 25 · DISAGREE 3 (rows 3-mild, 22, 28) · CELL-BLANK 1 (row 26,
  malformed) · CANNOT-JUDGE 0 (folded row 9 into AGREE-adjacent NONE above; see row 9 note)
- **POINTER:** OK 28 · UNCHECKED 1 (row 26, malformed)
- **BOOT-RENDERED:** YES 4 (rows 6,11,14[wrong series],17[wrong series]) · PARTIAL 3
  (rows 7,8,10) · YES-number-only 1 (row 5) · NO 15 · CANNOT-JUDGE 6 (rows 2,9,12,18,21,
  24,27 — six, not five; see individual rows)

### Rows where SCANNABLE-AGREES = DISAGREE (or the malformed equivalent)

1. **Row 3, GATE-TERRY-ARM3 (line 13)** — mild: token `INSTRUMENT`, no producer exists
   anywhere (manual TIC-release read); terminal row, low stakes.
2. **Row 22, GATE-FERT-G5 (line 32)** — token `INSTRUMENT`, no producer exists (manual
   weekly DTN article read); live row, moderate stakes — this gate could sit unfired for
   weeks with nobody grading it if FERT's own weekly T4 discipline lapses, since no
   fallback instrument exists.
3. **Row 28, GATE-CORAL-MSI-01 (line 38)** — token `INSTRUMENT`, no producer exists
   (manual Parcl dashboard read); live, 🔴-holding row — same exposure as row 22, and
   the row's own recent MSI/months-of-supply mislabel correction shows this gate has
   already had one live basis error caught by the owner, not by any scanner.
4. **Row 26, GATE-VIO-RV1 (line 36)** — mechanical: the `scannable` cell, read
   positionally, is not a Class-7 token at all due to a missing tab shifting every field
   from `last_checked` onward one column left. Terminal/retired, so low live-risk, but
   this is the row that most directly demonstrates why the leg's audit question ("does
   PROME's own `scannable` cell agree with what you find?") needs asking — nothing
   currently checks that the cell even parses.

### Triage: CONVENTION (registry-wide, fix once) vs. PER-ROW

**CONVENTION defects (fix once, fixes/prevents many rows):**

1. **`registry_chain_check` — the ruled enforcement arm for the `scannable` column — is
   UNBUILT.** Confirmed directly: `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md:218`
   states it explicitly ("⛔ UNBUILT... queued after docket_view"), and `PROME/tools/
   prome_gate.py::check_gates_tsv()` (the only script that reads `PROME/GATES.tsv` at
   boot) contains **zero references** to `scannable`, `INSTRUMENT`, `JUDGEMENT`, or
   `OWNED-ELSEWHERE` (confirmed by grep) — it checks state-token vocabulary and
   `consumed_by` staleness only. **This is the root cause of row 26's malformation going
   undetected**, and of DISAGREE rows 22/28 never being caught: nothing validates that
   the `scannable` cell (i) parses as a valid token, or (ii) is backed by an actual
   named, runnable producer. A one-line addition to `check_gates_tsv()` — assert
   `scannable` is one of the three enumerated tokens, per row — would have caught row 26
   for free, without waiting on the full `registry_chain_check` build.
2. **PROME's own boot-time gate check never computes a single gate's underlying
   metric.** `check_gates_tsv()` validates state-token vocabulary, `FIRED-UNEXECUTED`
   presence, and `consumed_by` date staleness — never HY OAS, DGS10, MOVE, or any other
   number. Metric-rendering happens entirely in each OWNER'S OWN boot script (LIQUID's,
   TERRY's, BRENT's, REGINALD's, VIOLET's, SAM's), which is architecturally reasonable
   (PROME shouldn't own 15 desks' feeds) but means **"BOOT-RENDERED" for any row is a
   question about the OWNER's boot cadence, never PROME's** — worth stating plainly so
   a future reader doesn't assume PROME's clean `prome_gate.py` run says anything about
   whether a gate's number is fresh.
3. **WALTER's directed role ("your boot scans INSTRUMENT rows only," per the 2026-08-20
   DAEDALUS→WALTER packet at `AGENTS/WALTER/inbox/processed/2026-08-20_from-DAEDALUS_
   your-8-19-question-RULED...md`) does not appear to be wired into `AGENTS/WALTER/
   CLAUDE.md`'s actual boot step.** WALTER's own boot step 6c (line 68) scans "RED-FT +
   REG-T + the 5 scannable CREED-T + Cushing" — the pre-8/20 registry set — with no
   reference to `PROME/GATES.tsv` or its `scannable` column anywhere in `AGENTS/WALTER/
   CLAUDE.md` or `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` (both grepped, zero
   hits for "GATES"). **CANNOT-JUDGE** whether this is a genuine wiring gap or whether
   WALTER's INSTRUMENT-row scan lives somewhere else not surfaced by this search — flag
   for owner confirmation rather than asserting a defect outright, but note that if the
   ruling was meant to change what WALTER's boot actually does, the charter file that
   defines WALTER's boot does not yet reflect it.
4. **The `source`/`definition_surface` columns systematically under-cite the actual
   producer script even when one exists and is a clean match** — rows 1, 5, 12, 21, 25
   all point to a workbook/registry/thesis doc rather than the `.py` file that grades
   the gate, even in cases (row 12, row 21) where the OWNER'S OWN grading narrative
   names the script by filename in the `state` cell. This is a low-severity, high-
   frequency pattern (5 of 29 rows) that costs nothing to fix per-row (add the script
   path alongside the existing citation) and would materially shorten any future audit
   of this kind.

**PER-ROW facts (real, but local to one gate):**

- Row 14 (GATE-LIQ-079): the live boot-rendered "SOFR99 tail" number is computed
  against the wrong denominator (SOFR median, not IORB) relative to the gate's own
  registered condition — a basis mismatch masquerading as a working instrument.
- Row 17 (GATE-TERRY-006, retired) and row 15 (GATE-FALCON-001, live): both rely on the
  same class of PortWatch/Kpler/Vortexa gap — no dark-fleet-capable fetcher exists in
  this fleet at all; row 17's retirement record is the fully-worked-out case, row 15 is
  the still-open exposure to the identical gap on a different chokepoint (Bab
  el-Mandeb/Yanbu vs. Kharg).
- Rows 22 and 28: two live, unfired gates whose only reader is a human opening a web
  page (DTN article; Parcl dashboard) with zero fallback instrumentation — not wrong,
  but fragile if the owner's own weekly-touch discipline lapses, since nothing else in
  the fleet would notice a stale or missed read.
- Row 26: the field-count defect is local to this one row's TSV encoding (a single
  missing tab), not a schema-wide corruption — the other 28 rows all parse to 12 fields
  cleanly (verified via `csv.reader` + `awk -F'\t' '{print NF}'` across the whole file).

---

## What this audit could NOT see

- **I did not open the body of `AGENTS/VIOLET/scripts/fred_fetch.py::credit_summary()`**,
  so row 9's CCC%/CCC-BB-dispersion instrument claim rests on the function's existence
  and neighboring comments, not a confirmed read of what it actually computes — flagged
  CANNOT-JUDGE rather than asserted.
- **I did not confirm invocation cadence (boot-time vs. on-demand vs. timer) for most
  scripts** beyond what a docstring states outright (e.g. `hy_oas_watch.py`'s systemd
  timer is explicit; most others are not). Six rows are marked BOOT-RENDERED
  CANNOT-JUDGE for exactly this reason — a script existing and being correct is not the
  same claim as it running unattended, and I did not execute or trace any script, per
  the read-only constraint.
- **I did not independently verify that any cited file path actually resolves** beyond
  the handful I explicitly `find`/`grep`-confirmed (scripts, `STATE_VOCABULARY.md`,
  `prome_gate.py`, the WALTER packet, `TRIGGERS.tsv`, `REGISTRY.tsv`-adjacent files, and
  `AGENTS/CORAL/scripts/boot.py`). Most `source`/`definition_surface` cells (workbook
  KB files, outbox reports, STATUS.md sections) are marked POINTER: OK on the strength
  of internally consistent naming conventions across the file, not a per-file `ls`/open
  — a full pointer-travel pass (opening all 29+ cited files) was out of scope for the
  time available and would be a reasonable follow-up leg.
- **I did not fetch or evaluate any live external data** (FRED, DTN, Parcl, Kpler,
  PortWatch) per the task's explicit UNCHECKED-EXTERNAL instruction — every verdict
  above is about whether an INSTRUMENT EXISTS and matches the registered BASIS, never
  about whether today's live value would fire the gate.
- **CREED's and OSPREY's Tier-2 "cannot self-boot" status** means I cannot independently
  confirm from this repo alone whether their instrument scripts (`threshold_scan.py` for
  CREED; none for OSPREY) are actually invoked on the cadence their rows imply — I
  relied on the rows' own consumed_by/review_by text describing the spawn-slate
  mechanism, not on watching a spawn happen.
- **WALTER's actual current boot behavior** — whether it scans `PROME/GATES.tsv`
  `scannable` rows at all today — is asserted CANNOT-JUDGE above on the strength of a
  `CLAUDE.md` text absence; it is possible WALTER's boot was updated in a file this
  search did not check (e.g. a script under `AGENTS/WALTER/tools/` not grepped by name),
  and this should be confirmed with WALTER directly rather than taken as settled from a
  charter-file read.
- **No agents were spawned and no files outside this run's own directory were modified**,
  per the task's rules — this audit is a snapshot as of 2026-08-28 and does not track
  whether any row changes state later today.
