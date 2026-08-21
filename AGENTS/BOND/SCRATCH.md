# BOND SCRATCH — 2026-08-21 (Fri, ~11:30 → ~12:xx ET). **Session 2: a peer correction I accepted in full, which then surfaced a bigger error of my own.**

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout.

> 🔵 **THIS WAS WRITTEN AS A HANDOFF WHILE THE SESSION IS STILL OPEN.** Will said *"boot up"*; I ran the write-back tail off a peer correction before being tasked. **Everything below is accurate and pushed — it is just not a handoff yet.** Anything Will tasks from here appends to this session and this file gets rewritten at the real close.

> ## ⏰ THE ONE THING WITH A CLOCK — UNCHANGED FROM SESSION 1: the ORACLE gap-marked Kalshi pin had to START **TODAY, 8/21**
> T6's repaired *"keeps falling"* qualifier grades *"below its value **5 trading sessions prior**."* Will's Option C sets last gradeable data at **Fri 8/28**. Counting back: **8/28 → 8/27 · 8/26 · 8/25 · 8/24 · 8/21** *(no holiday; Labor Day 9/7)*.
> ✅ **PROME filed a provisional day-1 capture** (`KXFED-26SEP-T3.75` last $0.35, yes 33/35, 11:14 EDT), **deliberately un-adjudicated** — the API's own `updated` field reads 8/12 and which field is pin-canonical is ORACLE's call. **BOND records the trigger as `UNMEASURED`, not as a measurement.**
> **Next session: check whether 8/22 onward is being gap-marked. If ORACLE declines, the locked fallback fires — Polymarket canonical, substitution recorded on the grade. Never blended.**

## CHANGES SINCE SESSION 1 (same day)

### ★ SESSION 3 — WILL-TASKED BOOT-DOCUMENT AUDIT, worked A→E in order. Full report + dispositions → `AUDIT.md`.

**0. The two findings that matter most, if you read nothing else:**
   - 🔴 **THE SEPTEMBER FOMC WAS NOT ON THIS DESK'S DOCKET** (now docketed, **9/15–16, decision + SEP on 9/16, verified at the Fed's own calendar** — the fleet's two variants were each half-right). **`docket_check` could never have caught it: it is AUCTION-ONLY**, so FOMC/ECB/CPI/MTS are outside its guarantee. Boot step 5's wording is corrected.
   - 🔴 **JACKSON HOLE 8/27–29 — WARSH'S FIRST KEYNOTE AS CHAIR (~8/28) — WAS ALSO ABSENT**, while sitting on `PROME/DOCKET.tsv` since 8/18 **with BOND named as a consumer**. *Transfer completes only when the RECEIVER encodes.* **8/28 is the day before T6's hard close, on a test whose trigger is September-hike probability.** ⚠️ **Dates are SECONDARY** — primary unfetched by three independent attempts (PROME 403; BOND WebFetch 403 + curl/browser-UA **host TIMEOUT**). `re-test:` before 8/27.

**1. Five surfaces were a print behind on FR2004** (8/12 landed; TRADE, STATUS ×2, the docket row and DEALER_CAPACITY's body-under-a-fresh-header all read 8/05). **Both boot and closeout had returned rc=0 that morning — correctly, because FR2004 is the NY Fed api and no check covered it.** Coverage was the gap, not diligence: `check_fr2004()` added, regression-tested against the exact pre-fix text, and it found the 5th surface my manual sweep missed.

**2. The STATUS catalyst twin had drifted from the docket in three ways** — it told readers *"do not grade anything off"* the QRA **16 days after the content was established at two primaries** (the Q3 QRA **froze coupon sizes**); it carried a discharged ECB action as still open; and it was missing the 8/26 2Y reopening — **the exact row `docket_check` was built to catch, which reached the docket and never got mirrored.** All 12 dated docket events now verified present in the twin.

**3. `assertion_check`'s EXPIRED rule could see 16% of the dates on the files it scans** (253 ISO vs 1,336 slash) — the catalyst twin is entirely slash-dated and was **invisible by construction**. Fixed, plus two latent bugs: `owed` matched inside *"showed"*, and `\bwill\b` matched **the operator's name** (10 false positives — this desk writes "Will-ruled" constantly).

**4. `closeout_check --selftest` tested half of what it claimed.** It was a one-line delegation to `assertion_check`; the numeric half had ZERO coverage while CLAUDE.md said "the CHECKERS". Drift predicate extracted to a pure function; **41 fixtures now, all passing, across three checks** (was 14, one checker).

**5. `monitors/kb_lint.py` BUILT — the root-cause fix for a rule that was never enforced.** Boot step 7 has always mandated validating against `SCHEMA.tsv` + `VOCABULARIES.tsv`; nothing enforced it, and 14 rows had a bad `Conf`, 13 a bad `Epistemic`, 11 an off-vocab `Group`, and PREDICTIONS carried **both `FAILED` and `FALSE` for one state** (silently breaking every count of resolved outcomes, calibration included). **The tell it was a missing guard and not carelessness: I wrote three off-vocab rows that same morning.**

**6. The 94-day outbox item is CLOSED, 6 days early.** 4 of 5 packets **verified delivered by CONTENT** at the recipient → `outbox/delivered/`. ⛔ **1 genuine orphan (HENRY 5/19)**, absent on seven keys — **not re-sent**, because the figures are 94 days superseded and re-sending stale marks is worse than the orphan.

**7. ⚠️ FOUR OF MY OWN AUDIT FINDINGS WERE WRONG OR OVERSTATED, all caught by TESTING rather than re-reading:** B2 counted co-occurrence as suppression (measured across radii, the tradeoff is not monotone — reverted to the quiet default, `--strict` added); a `Stale_By` advisory I wrote contradicted the schema it enforces; a `#` comment I added to `PREDICTIONS.tsv` became the CSV header and **made my own new lint report CLEAN off a wrong referent**; and a future-date discriminator killed a real fixture. **Each correction is in the code as a comment or a fixture, so the next pass inherits the correction and not just the conclusion.**

**8. DAEDALUS flag folded in** (`976b0b8e7`): `NEXUS_BRIEF:43` carried the retracted *"FRED series starts 2021-08"* verbatim for 3 days while §0 killed it upstream — **upstream kill present, in-place amendment absent.** Annotated in place.


1. ✅ **VULCAN'S CORRECTION ACCEPTED IN FULL, NO QUALIFICATION — `KB-BND-159`.** Session 1 recorded that VULCAN *"independently pulled HY OAS 275bp [8/20], matching this refresh exactly."* **Both pulls hit `FRED BAMLH0A0HYM2` — ONE source fetched twice.** What it genuinely validates is the **FETCH** on both sides (no transcription slip, stale cache or mis-keyed series), and that is worth recording because it is normally invisible; what it **cannot** do is corroborate the **VALUE**. **Agreement between two readers of one source is a property of the readers, not of the number.** Fixed on `RECEIPT` + `SCRATCH`; it never reached the 9/3 deliverable. **⇒ STANDING RULE ADOPTED: when a BOND surface reports agreement with another desk, NAME THE SERIES BOTH SIDES PULLED.** *(VULCAN has adopted the same rule at its desk.)*

2. 🔴 **AND THAT SENT ME BACK TO THE PRIMARY, WHERE I FOUND A BIGGER ERROR OF MY OWN — `KB-BND-162`, n=6.** The CCC line published in session 1 said *"16 prior obs ≥1035, **every one of them April-2025**."* **FALSE.** Enumerated by month (`BAMLH0A3HYC`, session closes, 2023-08-22→2026-08-20, n=787, cache-busted): **12 in Apr-2025 (4/4–4/22) · 2 in Oct-2023 (10/30–31) · 1 on 2023-11-01 · 1 on 2024-08-05 — FOUR episodes across three years, 12 of 16.**
   - **UNAFFECTED and still true:** fresh 2026 high · not a series high · max 1137 (2025-04-07) · count 16 · all four declared parameters.
   - ⚠️ **THE DIRECTION RUNS AGAINST ME.** *"All April-2025"* framed 1035 as a level touched in **one** prior episode (the tariff shock). Four episodes across three years is a **more ordinary** level ⇒ it **weakens** the escalation read. `VX-BND-11` holds at 3 either way — 1100 is the registered line and nothing fired.
   - **THE METHOD LESSON (the reusable half):** I declared all four parameters and **computed the count**, then attached an **uncomputed adjective describing that set's internal composition**. **Where the 16 observations SIT is a second computation wearing the first one's parameters.** A distribution claim is not a free rider on a count.
   - **PROPAGATION + FIX:** 8 live surfaces here + PROME's HEARTBEAT §3 tag + VULCAN's STATUS (adopted verbatim with attribution). **Fixed by PATTERN, not by the grep line list** — ⚠️ **and the first pattern had a hole**: bold markers between the count and the clause hid `STATUS.md:8`, caught only by the residual re-scan. **Run the residual scan; the pattern pass is not the check.** `KB-BND-155` marked **CORRECTED**, Fact left intact as the record (`KB-BND-139` precedent).

3. ★ **RECIPROCAL FINDING SENT AND ADOPTED — FAN-OUT IS NOT REPLICATION (`KB-BND-161`).** VULCAN proposed strengthening the AI-complex CDS record from *unreached-by-two* to *unreached-by-three*. **Verified at LIQUID's artifacts — the claim checks out, but it bundles two claims of different strength:** **① the ABSENCE is genuinely three-desk strong** (each desk's failure to reach is an **independent attempt against its own toolkit**); **② the LEVEL is not** — all three of us hold the 7/27 prints from **ONE WALTER dispatch** (`SIG-W-20260728-008` to BOND/LIQUID/VULCAN, `-002` additionally to LIQUID/VULCAN) citing one Investing.com piece and one terminal capture. **Three inboxes, one source.** VULCAN has split it into two permanent lines. **Kept OFF Will's HELD US-sovereign-CDS item — different reference entity, existence still unchecked here.**

4. **IG "flat in a 3bp band" was also wrong and is corrected.** `BAMLC0A0CM` ran **0.78 → 0.82 over 12 closes — a 4bp band drifting WIDER**, not flat. **Better contrast, same data, now on both desks' surfaces: the HY index is DEAD FLAT 2.75 → 2.75 across 8/05→8/20 while its own CCC tail ran +12bp to a fresh 2026 high** — same index family, same provider, no denominator mismatch. ⚠️ **Perimeter caveat carried (VULCAN's own, returned): `BAMLH0A3HYC` is the WHOLE US CCC tier, so it corroborates the SHAPE, NOT the attribution — zero of that 12bp is decomposed by issuer.**

5. **CRWV financing ladder filed RELAYED-PENDING-VERIFICATION — `KB-BND-160`.** VULCAN offered the **filing, not the figure**: CRWV Q2 10-Q, acc `0001769628-26-000366`, Note 16 Subsequent Events. **5.0 → 5.5 in three months, both recourse-guaranteed = +100bp like-for-like; DDTL 4.0 is NON-recourse so Mar→Aug is NOT quotable as +325bp.** **BOND has NOT pulled it and does not assert the 100bp.** **Perimeter: CRWV is a NEOCLOUD on private/bank-syndicated paper ⇒ enters NEITHER side of the hyperscaler long-dated public IG issuance share.** Sits beside the 7/23 GS/JPM basket (`KB-BND-093`) as a separate datum.

6. **Boot checks all clean and the tape is unchanged from session 1** — `docket_check` **rc=0** (4/4 upcoming auctions docketed, CUSIP-keyed), `boot_recompute` **rc=0** (no unguarded drift on the boot-unread surfaces). Levels re-confirmed: 30Y **5.19** / 10Y **4.65** / 2Y **4.19** / DFII10 **2.35** [all 8/19] · HY **275** / CCC **1035** / IG **82** [all 8/20]. **Add-gate 15bp. Run 32 consecutive sessions ≥5.00, 48 days in 2026.**

## NEXT SESSION (dated, future-verifiable)

1. ⏰ **8/22 — verify the ORACLE pin is being GAP-MARKED** (box above). If declined, the locked fallback fires: Polymarket canonical, substitution recorded on the grade. **Never blended.**
2. 🔴 **~8/24 — LIQUID's concur on the CONJUNCTIVE fresh-high reading**, then Will's word. **If LIQUID is silent past its 8/24 touch, escalate** — 8/28 is the last gradeable data date.
3. **🔴 8/25–27 — the 2Y/5Y/7Y cluster is the hard commitment: the Will-ruled MATRIX_V2 legs (§1 drop dealer-as-bearish + §3c indirect-sufficient-alone at the 15th per-tenor pctile) get adopted AT PRE-REGISTRATION.** Re-derive per-tenor trailing-12 at grade time — **do not reuse another tenor's numbers.** The 5Y is where the 7/27 cover marker (BTC 2.28) fired. ⚠️ **Register PRE-PRINT with a residual branch and per-leg margins.**
4. **🟡 8/24 (Mon) — Will's HELD US sovereign-CDS sub-item.** Establish existence + pullability **before** proposing any threshold. ⚠️ **n=3 on claimed-unavailability-is-really-a-path-artifact.** **Audit the path before reporting a wall.** ⚠️ **And do NOT fuse it with the AI-complex corporate CDS thread (item 3 above) — different reference entity, different instrument.**
5. **🟠 by Fri 9/4 — base-rate (a)/(b)/(c) + the VX-01 revert-rule**, ahead of the 9/9–10 cluster. Corpus current to 8/13, 390 rows. *"Don't build it" is a real answer.*
6. **🟠 9/3 — SAM's CH-016 cross-section AND the PROME-allocated hyperscaler long-dated IG issuance share.** ⚠️ **Perimeter, twice-warned by VULCAN and now settled: their figures are CAPEX and OBLIGATIONS, mine is ISSUANCE — different objects that do not sum.** A $260B off-BS lease commitment is not bond issuance; **CRWV private paper is not public IG issuance either.** **Size first, attribution second.** *(Do NOT carry: the NVDA→OpenAI ~$250B backstop is filed nowhere; the $1.65T off-BS figure is secondary.)* **Ask VULCAN for the CRWV Note 16 pull whenever — offer standing, no rush.**
7. ✅ **CLOSED 2026-08-21 — the 5 outbox packets are content-checked, 6 days early.** Verified at each recipient's own files, by CONTENT and on multiple keys, never by filename. **4 of 5 DELIVERED** → `outbox/delivered/`: LIQUID 5/19 (its CHANGELOG + KB), SAM 7/1 (NEXUS_BRIEF + board_log), TERRY 7/10 (TRADE_BOOK + FIRE_CARDS_LADDER + INDEX), TERRY/PROME 7/16 (TERRY STATUS + the FLOW-TRIGGER card + PROME GATES + ACTIVE_DECISIONS). ⛔ **1 GENUINE ORPHAN: HENRY 5/19, 94 days.** Absent on seven independent keys; HENRY's inbox holds BOND packets from 7/28 and nothing from May; HENRY's own credit-decoupling references trace to VIOLET and to its own HY-OAS work. **NOT re-sent — the figures are a 5/19 snapshot, 94 days superseded, and re-sending stale marks is worse than the orphan.** Bannered in place. **The finding is that a packet can sit in `outbox/` for 94 days indistinguishable from a sent one** — which is exactly why `delivered/` exists and why it must be moved into by CONTENT.
8. **🟡 DAEDALUS review #6–15 still QUEUED** — #7 first (three surfaces disagree on gate (b)'s own level: 4.50 vs 4.6).
9. **🟠 CARRIED FROM SESSION 1, still undecided:** the 9/20 VIOLET HYG-skew leg is **NOT FIREABLE AS WRITTEN** (VIOLET can produce a POINT but not the DIRECTION). **Decide next session: RETIRE the clause or re-spec it** — do not leave it unfireable a second time.
10. **🟡 Retirement candidate:** `BND11_REFUNDING_PREREG_2026-07.md` — check the 8/21 root Data-Hygiene amendment first (pending-event carve-out + index-refs-don't-count).

## OPEN THREADS / KNOWN GAPS

- **Two corrections each way with VULCAN in one afternoon, and in both directions the RECEIVING desk was wrong and said so without hedging.** Worth naming because it is the thing that made both corrections cheap. VULCAN's own note on their half: *"I adopted the flattering version without re-deriving it"* — the asymmetric-rigor failure pointing **inward**.
- **⚠️ THE FIX-BY-PATTERN PASS IS NOT THE CHECK.** My regex missed `STATUS.md:8` because bold markers sat between the count and the false clause. **Always run the residual scan after the pattern pass**, and grade the residuals by whether each is a LIVE claim or a LABELLED retraction.
- **The composition-adjective class is now written up in TWO places and PROME routed it correctly:** local `MEMORY.md` (BOND-specific, n=6 of the superlative class) and the fleet memory `finding_verified_figures_do_not_verify_the_shape_claim` (third form — the two existing forms are shape verdicts over a SERIES; this one sits inside a single computed SET). `finding_crosscheck_with_free_parameter_validates_nothing` extended with the same-primary case + the fan-out corollary.
- **Neither closeout checker can judge whether ANALYSIS is still true** — and neither would have caught today's error, which had a correct number and a false adjective beside it. **The re-pull caught it, and only because an unrelated peer correction forced one.**

## POSITION

**TLT puts HOLD, no add — UNCHANGED, and nothing this session touched the book.** Will's 7/16 NO-ADD stands; the 8/20 60-DTE review ran and **Will ruled let it run: no roll, no add.** Leg at **40 DTE** (Sep-30 expiry).

**Only live add-gate: DFII10 2.35 [8/19] = 15bp away**, a second session AWAY. ⚠️ **Do not read that forward — the 8/20 nominal close is UNPUBLISHED (partial H.15 split) and the long end backed UP live today.** `BND-15` (70%, no DFII10 close ≥2.50 through 8/29) is **materially safer than when frozen — and the confidence does NOT move up, for the same reason it didn't move down when it looked wrong on 8/18.**

**Composite 12/35 — unchanged. OPEN predictions: `BND-15` ONLY** (timeframe runs to 8/29; **not DUE**).
⛔ **Harvest, roll and sizing are TERRY's calls on TERRY's rules with Will's approval.**

## MAIL

**In:** 5 deferred from session 1, unchanged and still deferred (DAEDALUS 18-findings · LABOR T7 verbatim · REGINALD FHLB · VIOLET HYG-skew · PROME hyperscaler allocation ~9/3). **General-inbox processing remains a SEPARATE task.** WALTER lane empty.
**Out:** 1 packet written + committed + doorbelled → **VULCAN** (`496f2893d`), **confirmed applied by VULCAN in-session** (their KB-108).
**Cross-session:** VULCAN ×2 (correction in → accepted; reply out → applied both ways). PROME ×2 (ack in; CCC correction out → **HEARTBEAT §3 had the false clause, corrected `b2f5ecdd1`, exposure ~20 min, and PROME confirms nothing false reached Will**).

## CLOSEOUT

**Session 3 (audit):** `AUDIT.md` ✅ (107 findings-report + 20-row disposition table) · `monitors/kb_lint.py` ✅ NEW · `assertion_check` ✅ (EXPIRED rebuilt, `--strict`, +13 fixtures) · `boot_recompute` ✅ (`gate_row_drift` extracted + `check_fr2004` + 8 fixtures) · `closeout_check` ✅ (3 checks, both selftests wired) · `CLAUDE.md` ✅ (step 5 scope, step 16, 2 FILES rows, 4 fixture counts) · `STATUS` ✅ 250/250 (2 headers archived to make room) · `TRADE`/`NEXUS_BRIEF`/`DEALER_CAPACITY`/`CATALYSTS`/`KB`/`PREDICTIONS`/`MEMORY` ✅ · `outbox/delivered/` +4.
**Checks: `docket_check` rc=0 · `boot_recompute` rc=0 · `closeout_check` rc=0 across all three · `--selftest` 41/41.** TSVs field-count verified whole-file (KB 13 · VX 9 · FLOW 10 · CATALYSTS 8 · PREDICTIONS 11).


STATUS ✅ (**249 ln, at cap**; 2 corrections recorded inline, no lines added) · SCRATCH ✅ · RECEIPT ✅ · KB ✅ (+159/160/161/162, `-155` → CORRECTED) · VX ✅ (`VX-BND-11` text) · CATALYSTS ✅ · TRADE ✅ · NEXUS_BRIEF ✅ · CREDIT_PRIMARY_MARKET ✅ · MEMORY ✅ (2 durable learnings) · auto-memory ✅ (×2 extended, no new slugs — index unchanged). **THESIS/CHANGELOG: NOT bumped — no thesis-level change** (no new channel, no conviction shift, no threshold breach, no prediction resolution; both corrections moved a characterisation, not a score).
