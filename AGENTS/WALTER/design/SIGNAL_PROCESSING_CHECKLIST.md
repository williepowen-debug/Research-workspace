# WALTER Signal Processing Checklist
**Version:** 0.36 | **Date:** August 22, 2026 (**Phase 2 step 7 gains the STATE RULE: a trigger with an exit condition is a state machine, not an event counter — grade close-by-close at the instrument against BOTH the trigger and its exit, never inherit state from a board summary. REGINALD's wording, PROME-endorsed, adopted after WALTER's live board carried `REG-T-02` as wrong in BOTH directions simultaneously.**) *(prior: 0.35 | August 20, 2026 (**The 8/08 forum-carry builds land, Will-directed — three dispatch-time conventions now machine-guarded.** ① **`entities:` MANDATORY at dispatch** [step 4.5]: a YAML list of specific greppable proper nouns on every signal dated 2026-08-20+, never retro-filled — canonical FORMAT_SPEC v0.18; doctor `entities_at_dispatch`. ② **TERRY token declaration** [Phase 3.5 gate]: every `action: TERRY` `delivery_log` row BEGINS its notes cell with `T-1`/`T-2`/`T-3`; absence of a valid leading token IS an override by definition [inverted-token, PROME-accepted]; `TERRY-OVERRIDE` stays as human-readable prefix, no longer load-bearing — canonical SPEC v0.19 §3.5.5; doctor `terry_override_ratio` incl. the 72h revert falsifier. ③ **consume-declaration on processed/ moves**: a `git mv` into processed/ is a consumption record only with `consume:<AGENT>` in the moving commit or a `.consumed.tsv` append — canonical SPEC v0.19 §5.1; doctor `filed_vs_consumed`. Doctor 27→30 checks.) | **v0.34:** August 20, 2026 (**SCOPE OF A `CONFIRMED` VERDICT clarified at Phase 1.5 — a CONFIRMED certifies the FIGURES and their FRAMING, NOT a SHAPE CLAIM built across them.** Before writing "peaked"/"rising"/"plateaued"/"not a wave starting": is the series a RATIO or a QUANTITY, and if a ratio, did the denominator move? Bought by `SIG-W-20260819-021`, where every share figure and date were correct and confirmed at primary by the trigger's owner, while the denominator moved 2.3× and the dollar series peaked two months later than the published shape verdict said. Not a sourcing failure — a share plotted over time looks exactly like a trend. Definition clarification, inline per RULE 8; no new verify-spawn trigger and no cost change.) | **v0.33:** August 7, 2026 (**TERRY override clause RATIFIED — denominator 30d → trailing 90d, activation n≥10 in the window, n=1 report to TERRY MANDATORY, breach ⇒ READ THE OVERRIDE LOG and never auto-widen T-1/T-2/T-3.** 90d because at ~3 dispatches/30d the n≥10 activation is unreachable by construction. ⚠️ The revert falsifier stays 30d/n=1/no-denominator — **two clocks on purpose, do not harmonise**: the falsifier is an event test. Canonical BOARD_CONSUMPTION_SPEC v0.16 §3.5.5 + ROUTING_TABLE v0.25.) | **v0.32:** August 7, 2026 (**THE TERRY GATE at Phase 3.5 — TERRY is NEVER on `info:`; `action: TERRY` only on T-1 named instrument / T-2 correction-or-retraction of a number any TERRY surface cites / T-3 closed-market event on a held-or-staged underlying.** Will CONFIRMED in-session on TERRY's own disposition (`FORUM/2026-08-07_system-review/06_proposals/07_TERRY_routing-disposition.md`, option (c)). Any non-qualifying send is an OVERRIDE, allowed, and logged as a `TERRY-OVERRIDE` prefix in that row's `delivery_log` notes cell so it counts against the >10%/30d return-to-forum trigger. Falsifier, non-renewable: if the S1 owner-unconsumed line ever names TERRY for an `action:` item unconsumed >72h, revert to the RED-class exemption and do NOT tune the tests. Desk-scoped — the fleet-wide ownership extension of the ACTION-LINE RULE remains unratified and must not be inferred. Canonical: BOARD_CONSUMPTION_SPEC v0.15 §3.5.5 + ROUTING_TABLE v0.24.) | **v0.31:** August 3, 2026 (**Correction pathway specified — `signal_type: correction` now REQUIRES a `corrects:` target.** Tag the type when a dispatch's *reason for existing* is to correct/retract/re-frame a prior WALTER claim, and declare the target in one of three forms: SIG-ID list · `SELF` (in-place) · `EXTERNAL: <what>` (packet / registry row / anchor stamp / third-party claim). ⚠️ **The field points FORWARD only — it does NOT discharge the obligation to write the BACKWARD pointer** (a `status:` tag + INDEX marker on the corrected signal), because readers arrive at the ORIGINAL. The 8/3 sweep found two signals untagged for 6 and 11 days behind a correction that already named them. Guarded by `walter_doctor` `correction_target_declared`, keyed on `signal_type` and deliberately NOT on `corrects:`. Canonical: FORMAT_SPEC v0.15, Will-approved 8/3.) | **v0.30:** August 2, 2026 (**Pre-decision-outcome contamination guard added to Phase 1.5** — SAM/VIOLET n=2 on the 7/31 BOJ MPM: search content asserting a scheduled event's outcome as completed fact, dated before the event, is kill-on-sight for grading and quarantine-and-log for provenance; fabricated-plausible not leaked [the "0.8% GDP" was the FY2027 figure garbled into FY2026]; distinct from stale-vintage recirculation. Source: SAM packet 2026-07-31, consumed 8/2.) | **v0.29:** July 27, 2026 (**PROME added to the §3.5 pull-complete exemption + THE ACTION-LINE RULE becomes a tagging precondition — Will-approved.** Phase 3.5 delivery skip now applies to **CARL + RED + PROME** (PROME: `board_scan.py` complete whole-INDEX every-boot scan + **0 action-line appearances in 605 signals all-time, scanner `exit 1`s if that changes**; DISPATCHES where PROME is info-only — notes still delivered per §3.5.1). **New precondition at Phase 2 step 4.5 + Phase 3.5: if a signal carries an ask directed at a named recipient, that recipient goes on the `action:` line, not `info:` with the ask buried in the body** — every exemption rests on "never the ACTION owner ⇒ zero ACTION-miss risk," which is a claim about **metadata accuracy**, so this is a safety precondition rather than tidiness. Bought by `SIG-W-20260727-016` (`action: [RED, LIQUID]` / `info: [..., PROME]` with a direct operational ask to PROME in §8), raised by PROME against its own proposal. Canonical: BOARD_CONSUMPTION_SPEC §3.5 + §3.5.4 v0.12.) | **v0.28:** July 25, 2026 (**THE ACTIONABILITY TEST gates Phase 3.5 — Will-directed.** Notes are NON-ACTIONABLE CONTEXT ONLY; anything that could change what a recipient DOES is a SIGNAL and gets the full dispatch treatment. Dispatch when unsure — an over-dispatched context item costs one BOARD row, an under-dispatched actionable item is invisible and untracked. Canonical: BOARD_CONSUMPTION_SPEC §3.5.3 v0.11. Evidence: 3 instances in 10 days, 2 raised by recipients [VULCAN ×2] + Will directing the third. Pointer only — the Phase 3/3.5 mechanics are unchanged; what changes is WHICH LANE content enters.) | **v0.27:** July 24, 2026 (**DEWEY process-v2 template changes, 2 items, PROME-endorsed with implementation authority granted + Will-endorsed in-session — WALTER-owned infrastructure, no Will gate**: (1) **`kill_condition:` now REQUIRED on every new Phase-2.8 `/deep-research` prompt** — freeform event/date/re-verify-at-intake condition; **DEWEY refuses to run if it is satisfied at intake** (self-enforced, no new WALTER machinery). Converts the silent "dead prompt still runs" failure into a loud one at ~zero authoring cost; 2nd-instance trigger met (PROMPT-15 7/24 ran with `deliver_by` 10d passed + gating catalyst already fired, caught by discipline not mechanism; prompt 12 parked 7/16). Optional on revisions — no retro-fill. (2) **`impact` column added to `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` (12→13-col)** — free text, populated at **consumption** by the consuming domain agent (PROME sweeps misses at closeout), NOT by WALTER and NOT at flag time; gives DEWEY the "which prompt kinds pay off" signal. Backfill-safe; `walter_doctor` reads by column name. Honest limit: covers the flagged-prompt lane only. Full spec: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md` §5b + §5e.) | **v0.26:** July 9, 2026 (**design-walkthrough batch, Will-approved 2026-07-09**: (1) **RED added to the §3.5 pull-complete exemption** → Phase 3.5 delivery skip now applies to **CARL + RED** (RED runs a complete whole-INDEX BOARD scan at boot step 1.5 AND is auto-cc'd INFO-only → zero ACTION-miss risk; was 24% of delivery volume); (2) **thin-liquidity prediction-market fold-convention [Phase 1b]** — a low-volume Polymarket/Kalshi datum that corroborates an existing thesis FOLDS into the related signal as a market-implied-timing layer, not a standalone dispatch. Pairs BOARD_CONSUMPTION_SPEC v0.8.) | **v0.25:** July 4, 2026 (**FILTER v3 codifications — image-batch dedup [Phase 1b] + distressed-CRE figure-class verify [Phase 1.5]**: (1) multi-image Will-Telegram drops dedup by Telegram file-id-stem → content-grep fallback *before* running gates [recurred 6/28 + 7/4]; (2) a headline `$` on a distressed / defaulted / deed-in-lieu credit is routinely the ORIGINATION, not the current UPB or the realized loss — verify WHICH before routing [OZK $196M-origination-vs-$126M-current, 7/4]. Pairs FILTER_SPEC v0.6 [3 named kill sub-classes + review-cadence recalibration]; Will greenlight 2026-07-04; canonical review doc `design/FILTER_V3_REVIEW.md`.) | **v0.24:** July 4, 2026 (**pull-complete recipient exemption — skip Phase 3.5 delivery for complete-pull agents**: per BOARD_CONSUMPTION_SPEC §3.5 [Will-approved 7/4, relayed via PROME], WALTER SKIPS the `inbox/WALTER/` handoff + `delivery_log` row for a recipient whose own boot scan is a *complete whole-INDEX* BOARD-diff — currently **CARL only** [verified 22/22 ACTION already dispositioned]; BOARD + `route_log` still written; REGINALD [tiered scan] + SAM [no scan] NOT exempt. See the Phase 3.5 note below.) | **v0.23:** July 3, 2026 (**`confidence_note` optional field — Filter v2 Segment D shipped**: Phase 2 guidance for reaching for the optional free-text observation-vs-interpretation asymmetry field per Will Option A [decided 2026-04-20 Telegram msg 856; implementation debt cleared 7/3]; pairs FORMAT_SPEC v0.13; ships FILTER_V2_PLAN v2 COMPLETE + unblocks the overdue FILTER v3 review.) | **v0.22:** June 27, 2026 (**investigation routing — verify-spawn vs assign-DEWEY discriminator + paywalled-pointer principle** [Phase 1.5]; Will-directed 2026-06-27 — a paywalled/headline posting is an investigation POINTER (sense → recognize topic → trigger investigation depth → recover content + pull data), NOT route-or-kill; and research execution **defaults to DEWEY** (keep WALTER's context for sensing+routing), with WALTER verify-spawn reserved for BLOCKING same-session framing-checks. Worked examples: flood SIG-030 [verify-spawn, borderline] / housing-distress DEWEY prompt #4 [assigned].) | **v0.21:** June 26, 2026 (**single-machine collapse** — Phase 3.5 platform-nuanced `delivered` → uniform committed+on-origin [OpenClaw-recipient line retired]; **Quick-WALTER RETIRED** per cutover 0d; canonical BOARD_CONSUMPTION_SPEC v0.6; Will-ratified 2026-06-26.) | **v0.20:** June 20, 2026 (**DEWEY-executor + inbox-consumption wiring (DEWEY revival Phase 2)** — Phase 2.8 executor moved "Will runs it" → "**DEWEY executes (Will triggers/approves)**"; Phase 2.8b deliverable now arrives via a **create-only DEWEY handoff in `AGENTS/WALTER/inbox/DEWEY/`**, consumed at boot [new spawn-protocol step 7d] + `git mv` to `processed/` after routing [**NEW→ROUTED→PROCESSED** lifecycle, prevents repeat-routing]; `DEEP_RESEARCH_FLAGGED_LOG` gains an `executor` column [11→12-col]. Will sign-off 2026-06-20.) | **v0.19:** June 19, 2026 (**Phase 2.8b RETURNING-DELIVERABLE HANDLING added** — how WALTER routes a `/deep-research` deliverable when it returns: **default to ONE `research-output` BOARD signal** [packet embedded verbatim + per-recipient genuine-delta wrapper; **no verify-spawn → VERIFIED-PRIMARY**; WALTER routes-not-analyzes per the lean mandate], close the originating `DEEP_RESEARCH_FLAGGED_LOG` row, and **carve a finding into its own child signal ONLY on the split test** [S1 different-actionable-owner / S2 registered-trigger-or-falsification-anchor / S3 different-lifecycle-clock / S4 standalone-discovery-unit]. First instance + worked example: SIG-W-20260619-008 (one signal was correct; the insurance commercial/condo finding was the lone borderline carve-out, kept in + elevated). Will sign-off 2026-06-19.) | **v0.18:** June 19, 2026 (**Phase 2.8 DEEP-RESEARCH CANDIDATE SCAN added** — a zero-research-execution-load triage flag: a dispatched signal that trips a tight trigger set [T1 new-coverage-channel / T2 new-cross-channel-interaction / T3 load-bearing-but-thin-evidence / T4 position-thesis-pivot / T5 verify-left-material-uncertainty] **AND** clears a mandatory materiality gate [name the question a cheap verify can't answer + the consequence; **no consequence → no flag**] → 🔬 line in the Telegram push + a ready-to-paste `/deep-research` prompt embedded in the BOARD body + a row in `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv`. **Will decides every time, WALTER never runs it.** Full-WALTER-only, max 3/batch, target ~1-2/wk. `walter_doctor` `deep_research_pending_overdue` check surfaces PENDING-past-deadline rows in the boot reply. Canonical: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md`. Will sign-off 2026-06-19.) | **v0.17:** June 18, 2026 (**Quick-WALTER registry-only routing boundary + UTC timestamp discipline: Quick routes only RED-FT / REG-T / safety-net triggers with fixed recipient_chain; delivery repair/backfill is non-routing maintenance; Will-supplied novel news still escalates Full WALTER. All `Z` timestamps must be true UTC.) | **v0.16:** June 18, 2026 (bright-line whitelist after ORC review; now tightened by v0.17.) | **v0.15:** June 18, 2026 (canonical-lane guardrail: Quick/Prome may not create parallel `FORGE/signals/` or generic recipient-inbox artifacts; if not using BOARD + `inbox/WALTER/` + logs, queue/escalate Full WALTER. Recipient minimization tightened.) | **v0.14:** June 17, 2026 (**Phase 3.5 DELIVERY step added** [section below] — per "WALTER Routing v2" packet, Will + PROME + ORC approved-in-principle: every dispatch now writes a per-recipient handoff file into `AGENTS/{RECIPIENT}/inbox/WALTER/` + appends a `delivery_log.tsv` row, in addition to the BOARD entry. Closes the "in BOARD ≠ received" gap (BRENT SIG-W-20260610-001 miss prototype). Platform-nuanced `delivered` (OpenClaw=shared-clone / Claude-Code=committed+pushed); FLASH/IMMEDIATE→CC scoped-push fallback; create-only collision-safe design. Canonical: BOARD_CONSUMPTION_SPEC v0.2. Also folds the Quick-vs-Full WALTER mode note into Phase 3.5.) | **v0.13:** June 10, 2026 (**Paired same-channel dispatch rule — new Phase 2.6** [inline cross-ref section below]: when 2+ same-session signals share one transmission channel, dispatch as an explicitly cross-referenced PAIR — mutual signal-ID cross-refs in both dispatch_notes + paired framing in both INDEX cells. The pairing carries the channel-level read neither signal carries alone. Promoted at 3rd instance per pre-registered trigger; Will sign-off 2026-06-10; promoted directly to CHECKLIST per promotion-path rules — dispatch discipline is CHECKLIST-owned, no MEMORY layover.) | **v0.12:** June 6, 2026 (5-decision walkthrough closeout — 5 process-discipline items batched. **(1) Passive at-boot threshold scan** added to WALTER CLAUDE.md spawn-protocol step 6b — cross-ref note added to Phase 2 step 7 below: triggers can now fire at boot, not only at-dispatch, closing the multi-day-gap detection hole surfaced 6/4 RED-FT-07 overdue (>930 since 5/29 but not eval'd until 6/4). **(2) Tier-1-forecaster public-forecast-missed pattern** added as 5th Phase 1.5 trigger pattern (verifier-confirms-forecast-wrong-on-print; substance can survive — De Haan distillate <100MMbbl 6/3 prototype). **(3) Composite-bifurcation batch-level tagging** added as new Phase 2.7: when a single session crystallizes N orthogonal bifurcation layers, dispatch closeout STATUS lead paragraph tags `composite_bifurcation:Nlayer` with explicit signal-ID cross-references (6/4 4-layer prototype: price + substance + plumbing + factor-cohort dispersion). **(4) Per-session-vs-day-aggregate `network_uncertainty_peak` threshold** — clarified rule: the ≥5 cluster_mediating threshold applies to BOTH per-session count AND day-aggregate sum; either triggers auto-flag. 6/4 fired on day-aggregate (15 dispatched / 14 cluster_mediating) while neither session crossed alone. **(5) 3-metric framework-agreement rule** — when 3+ independent positioning/credit/macro metrics simultaneously print at respective historical-analog peaks, surface in STATUS lead as regime-characterization not single-print noise. 6/4 prototype: GWIM 66% Oct'21 peak + FINRA margin/CinC 0.54 2000-peak + short-interest highest-since-2011. Will sign-off 2026-06-06 per 5-decision walkthrough closeout msg 2144.) | **v0.11:** May 8, 2026 (Phase 2 step 4.5 v0.8 routing-augmentation tagging added + Phase 2.5 event-window state check added per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a + §2d.5 + §2d.6; Will sign-off 2026-05-08. Step 4.5 covers signal_role / consumer_transmission / consumer_lens / cluster_secondary / event_window field tagging at dispatch time. Phase 2.5 reads EVENT_WINDOW_STATE.md once per session and overrides precedence to FLASH for Phase-2-cluster signals when state = OPEN, leaving cross-cluster signals at Phase 2 precedence; daily roll-up + close-of-window summary requirements; stale-check 7d. Step 5 updated to reference `signal_role: cluster_mediating` canonical form, retiring v0.7 prose-tag and `cluster_mediating: bool` interim discipline. Phase 3 header example refreshed) | **v0.10:** May 6, 2026 PM (Phase 2 routing-augmentation steps 5-7 added per RED ↔ WALTER LIAISON + JOINT_PROPOSAL_2026-05-06_red_walter §3) | **v0.9:** May 5, 2026 (Cluster assignment step added to Phase 2 per CLUSTER_TAXONOMY.md v0.1) | **v0.8:** April 20, 2026 (Filter v2 Segment C — Phase 1 step 2.5 verify-research trigger check added) | **v0.7:** April 20, 2026 (Filter v2 Segment B — Phase 1b same-theme combine step added) | **v0.6:** April 11, 2026 PM (canonical Domain Vocabulary referenced — Gap C resolved) | **v0.5:** April 11, 2026 PM (Phase 1 reconciled with FILTER_SPEC v0.2 unified filter model) | **v0.4:** April 11, 2026 (header schema reconciled, conflict_zone clarified) | **v0.3:** April 10, 2026 (confidence model reconciled) | **v0.2:** April 10, 2026 (worked example added) | **v0.1:** April 7, 2026

---

## v0.23 — `confidence_note` (Filter v2 Segment D)

**Phase 2 (Classify) — optional `confidence_note`:** when a signal's *observation* confidence and *interpretation* confidence diverge by ≥1 band (a physically-verified event with ambiguous meaning, or a soft datum with a clear read), set `confidence` to the routing-relevant value and add a free-text `confidence_note` capturing **both** — don't let the single score bury either the solid observation or the real interpretation doubt. Discretionary, not a gate; reach for it only on a material gap. Canonical field spec: FORMAT_SPEC v0.13 Confidence Model. (Prototype: SIG-022 EAM/E-6B — obs ~0.85 verifiable / interp ~0.40 ambiguous, previously buried under a single 0.40.)

## v0.12 Items — Inline Cross-References

**(1) Passive at-boot threshold scan** — canonical in WALTER CLAUDE.md spawn-protocol step 6b. Phase 2 step 7 (below) historically only ran at-dispatch; v0.12 acknowledges that the same eval logic now fires at boot too, even on dispatch-empty sessions. Closes multi-day-gap detection hole (6/4 RED-FT-07 overdue prototype).

**(2) Tier-1-forecaster public-forecast-missed pattern** — extends Phase 1.5 verify-research trigger patterns. The 5th pattern: when a tier-1-forecaster (institutional-credibility analyst) makes a PUBLIC forecast that misses on print, verify-spawn explicitly to preserve underlying substance while flagging the specific call as missed. Distinct from CORRECTED-FRAMING-on-data (verifier-corrects-author) — this is FORECAST-MISS-ON-RECENT-CALL (verifier-confirms-forecast-wrong-on-print, substance still real). Source-credibility profile: trust the substance, calibrate down dramatic-framing one step. Prototype: De Haan @GasBuddyGuy distillate <100MMbbl 6/3 (actual built +1.5MMbbl) — substance "Hormuz export record 1.9 MMbpd" survived; specific week-call missed.

**(3) Composite-bifurcation batch-level tagging (Phase 2.7)** — new phase-step run at session closeout BEFORE Phase 3 OUTPUT writes. When a single session's dispatched signals crystallize N orthogonal bifurcation layers (current observed N = 2/3/4: tape-vs-substance / price+substance+plumbing / price+substance+plumbing+factor-cohort-dispersion), surface in STATUS lead paragraph with explicit `composite_bifurcation:Nlayer` notation + signal-ID cross-references for each layer. Don't try to "net them out" — the bifurcation IS the frame. Prototype: 6/4 PM Batch 2 4-layer (SIG-001+002 [price] / SIG-005+010-014 [substance+plumbing] / SIG-009 [factor-cohort dispersion]).

**(4) Per-session-vs-day-aggregate `network_uncertainty_peak` threshold** — clarification of the ≥5 cluster_mediating per-day rule: rule applies to per-session count AND day-aggregate sum independently; either trips auto-flag. 6/4 fired on day-aggregate (15 dispatched / 14 cluster_mediating across 3 sessions) while no single session crossed alone. Distinct from 5/11 PM 21-in-day prototype which was single-session.

**(5) 3-metric framework-agreement rule** — when 3+ independent positioning/credit/macro metrics simultaneously print at their respective historical-analog peaks (different cycles), surface in closeout STATUS lead as regime-characterization input not single-print noise. Treat each metric as independent corroborator; require independence (e.g., GWIM ≠ FINRA margin ≠ short-interest measure different positioning vectors). Pattern: "N-metric framework agreement at historical-analog peaks simultaneously = regime characterization." Prototype: 6/4 PM Batch 2 (GWIM 66% Oct'21 peak + FINRA margin/CinC 0.54 2000-dotcom peak + short-interest highest-since-2011).

## v0.13 Item — Inline Cross-Reference

**Paired same-channel dispatch (Phase 2.6)** — applied at dispatch-batch shaping, after Phase 2.5 event-window check and before Phase 2.7 composite-bifurcation tagging. **Trigger:** two or more signals in the same session share one transmission channel — same mechanism the substance rides, not merely same cluster (de-dollarization axis; Phase-2 oil-thesis supply channel; a single conflict-escalation arc). **Action:** dispatch as an explicitly cross-referenced pair: (a) mutual signal-ID cross-reference in both dispatch_notes naming the shared channel; (b) paired framing in both INDEX cells ("pairs SIG-... same session"); (c) same-session timing so recipients encounter them together. **Why:** the pairing itself carries the channel-level read neither signal carries alone (e.g., CB-gold-rising + foreign-CB-UST-share-falling = composition-shift narrative only visible as a pair); recipients consume one structure instead of reassembling it from separate dispatches. **Distinct from Phase 1b same-theme combine:** 1b merges duplicate-origin tellings of ONE story into ONE signal; 2.6 keeps TWO distinct stories as separate signals but binds them. Distinct from Phase 2.7: 2.7 tags N orthogonal *layers* at batch level; 2.6 binds 2+ signals on ONE shared channel. **Promotion record:** pattern pre-registered at 2nd instance (6/06 PM-3 closeout), trigger set at 3rd; fired 6/10. Instances: 6/06 PM-2 de-dollarization (SIG-W-20260606-001 + -002), 6/06 PM-3 Phase-2 oil-thesis (SIG-W-20260606-003 + -004), 6/10 Iran multi-front (SIG-W-20260610-001 + -002). Will sign-off 2026-06-10.


## v0.15/v0.16 Items — Inline Cross-Reference

**v0.15 Quick-WALTER canonical-lane guardrail** — promoted from the 2026-06-18 Moscow MNPZ comparison between Prome/mini-WALTER and Full Claude Code WALTER. Mini-WALTER got the broad triage right but created a parallel `FORGE/signals/` + generic `AGENTS/{recipient}/inbox/signal_*.md` path and over-routed LIQUID on weak cross-asset relevance. Quick WALTER may write only canonical artifacts (`/BOARD/`, `/BOARD/INDEX.md`, `route_log.tsv`, per-recipient `inbox/WALTER/SIG-W-*.md`, `delivery_log.tsv`).

**v0.16/v0.17 Quick-WALTER bright-line whitelist** — ORC correctly identified the remaining gap: “obvious/mechanical” was self-judged, and the Moscow MNPZ miss was precisely a judgment miss. v0.17 final boundary: Quick WALTER routes only pre-registered RED-FT / REG-T / safety-net trigger fires where recipient_chain and precedence/action are fixed by the owning registry/spec. Delivery repair/backfill is allowed only for existing BOARD signals with already-named recipients and is not a routing decision. All novel news/screenshots, Will-supplied but unregistered news items, Visegrad/aggregator claims, extreme-language claims, source-lineage/RED decisions, confidence scoring, or discretionary recipient selection queue/escalate to Full WALTER. **Timestamp discipline:** every `timestamp`, `dispatched`, `delivered`, and `timestamp_routed` with `Z` must be true UTC; convert ET/local time before writing.

One-page operational reference for processing incoming signals. Derived from 10 research prompts across emergency medicine, military communications, ATC, pub/sub systems, intelligence dissemination, emergency dispatch, scientific alerts, open output systems, newsroom editorial, and trading desk operations.

> **Canonical source cross-references:**
> - `SIGNAL_FORMAT_SPEC.md` owns the signal file format, header fields, **and the Domain Vocabulary** (15 canonical codes per FORMAT_SPEC v0.4: LABOR, MACRO_INFLATION, TARIFF_TRADE, CONSUMER_CREDIT, BANK_CRE, FUNDING_LIQUIDITY, PRIVATE_CREDIT, INSURANCE_SHADOW, OIL_ENERGY, GEOPOL_ENERGY, GEOPOL_NON_ENERGY, JAPAN_BOJ, MARKET_VOL, ASIA_CONTAGION, UST_FOREIGN).
> - `FILTER_SPEC.md` owns Gate 1 filter logic (System-Critical bypass → Novelty → Relevance → Credibility).
> - `ROUTING_TABLE.md` owns domain → recipient routing rules, using the canonical Domain Vocabulary codes in every row.
>
> This CHECKLIST is the operational *process* — it describes how to execute those specs, not what they define. On any divergence, the owning spec wins and this CHECKLIST is updated to match.

---

## PHASE 1: INTAKE (Kill or Keep — under 10 seconds)

Per FILTER_SPEC v0.2 unified filter model. Pre-gate bypass first, then two hard kill gates, then soft credibility check.

```
0. SYSTEM-CRITICAL BYPASS  → If held position hit, safety net trigger,
                             falsification rule pierced, or Will FLASH:
                             SKIP all gates, route FLASH immediately.

1. NOVELTY (HARD KILL)     → Already in any agent's STATUS or routed <48h?
                             Yes: KILL, log to kill_log.tsv ("already known").

2. RELEVANCE (HARD KILL)   → Touches held position / active thesis /
                             watched metric / transmission chain / catalyst?
                             No: KILL, log to kill_log.tsv ("not thesis-relevant").

2.5 FRAMING AUDIT (SOFT)   → Any of the 4 verify-research trigger patterns
                             present (see Phase 1.5 below)? If yes, spawn
                             verify-research sub-agent before Gate 3.
                             Verdict adjusts Gate 3 inputs — confirms,
                             corrects framing, kills as false, or flags
                             indeterminate (lowers confidence).

3. CREDIBILITY (SOFT)      → Sets confidence tier (0.30-1.0 based on source
                             quality + specificity). Not a hard kill UNLESS
                             final confidence after adjustments < 0.30 floor.
                             Low-credibility-but-novel-and-relevant signals
                             pass to Phase 2 flagged, don't die outright.
```

Most signals die at Novelty or Relevance. That's correct. Target: 80-90% filtered.

**Key change from v0.1/v0.2/v0.3 of this file:** Novelty and Relevance are AND-gates (must pass BOTH), not pass-any-of-three. Credibility is a confidence modifier, not a hard gate. System-Critical is a pre-gate bypass that precedes all filtering. See FILTER_SPEC.md for full rationale.

---

## PHASE 1.5: VERIFY-RESEARCH TRIGGER (Framing Audit)

Runs between Gate 2 pass and Gate 3. Purpose: catch framing errors in shaky source language before credibility is scored. This month (Apr 2026) caught 4 framing issues that would have routed with bad framing otherwise — BOJ ¥330B misframing, WhaleInsider Hormuz "zero tankers / first in history", Blue Owl "co-founders / alt-collateral" overstatement, SIG-029 "first NATO state-response" inaccuracy.

**Trigger patterns** — any ONE fires a verify-research spawn:

| # | Pattern | Examples | NOT triggered by |
|---|---------|----------|------------------|
| (a) | Secondhand citing primary | Aggregator or X-repost of a primary source you haven't read yourself (WSJ-via-X-aggregator, Bloomberg-via-retweet, FT-summarized-by-newsletter) | Reading the primary directly |
| (b) | Summarizing plurals | "co-founders", "all three", "both", "every", "each of the", "the trio" | Named specifics ("Owl Rock's Doug Ostrover and Marc Lipschultz") |
| (c) | Mechanism-assertions not yet in primary coverage | "replaced with", "swapped for", "backed by", "triggered by", "in exchange for" — when the underlying filing/source doesn't yet carry that language | Mechanism claims that quote the primary source directly |
| (d) | Extreme-absolute extraordinary claims | "zero", "first in history", "largest ever", "never before", "unprecedented" | Falsifiable comparatives like "record high" / "biggest since 2021" / "5th largest" (these self-bound and are routinely checkable) |

**🆕 Pre-decision-outcome contamination guard (v0.30, SAM/VIOLET n=2 — 2026-07-31 BOJ MPM).** Any search result or summarized content **describing a SCHEDULED event's outcome as completed fact, dated (or content-dated) BEFORE the event's scheduled time**, is **KILL-ON-SIGHT for grading/framing purposes and quarantine-and-log for provenance.** Distinct from the stale-vintage-headline class: that is OLD content resurfacing; this is **pre-dated content asserting a FUTURE outcome**, which reads as authoritative precisely when it is most dangerous (pre-registration windows, pre-print sweeps). The graded instance proves the content is **fabricated-plausible, not a leak**: the circulating "BOJ holds at 1%, GDP upgraded to 0.8%" (techtimes 7/27, pre-decision) garbled the real print — the actual FY2026 median was +0.6%; 0.8% is the FY2027 figure. Two independent witnesses (SAM 7/29 + VIOLET 7/30, before cross-reading) suggest an index/syndication artifact; **techtimes is a repeat originator** (also the fabricated oil headlines, per the source-credibility map). Applies to ANY scheduled event: FOMC, CPI, auctions, earnings, BOJ. Evidence: `AGENTS/SAM/thesis/BOJ_2026-07-31_PREREGISTRATION.md` (§ headers preserved; extracted verbatim from STATUS 8/2 — SAM compression pass, redirect stub left) + SAM-38 contamination clause (CLEAN).

**Figure-class verification — distressed-CRE $ (v0.25, FILTER v3).** A headline `$` on a defaulted / foreclosed / deed-in-lieu / REO / troubled credit is routinely the **origination** amount, NOT the current unpaid balance or the realized loss — trade-press reposts conflate them. Before routing a distressed-CRE dollar figure, confirm WHICH it is (origination vs current UPB vs realized loss); routing the origination as "the default" overstates the loss (OZK Seattle 7/4: "$196M default" = the 2022 origination; current exposure ~$126M, a ~55% overstatement). Generalizes the "a number carries its threshold/unit/source" discipline to distressed credit. *(1 instance + systematic — this book has 4 CRE agents [REGINALD/CREED/CORAL/OZK]; re-check for a 2nd at v4.)*

**Spawn discipline** (per auto-memory Sub-agent Prompt Discipline):
- Lead the prompt with the routing decision that depends on the answer ("WALTER is about to route this to CARL as IMMEDIATE; need to know if the framing holds").
- Set a hard total word cap on the sub-agent's response (e.g., 200 words).
- Require a single-line VERDICT at the top of the response — everything else is optional.
- Ask for decision-usefulness, not comprehensiveness. Don't template — write the prompt each time.

**Verdict handling:**
| Verdict | What it means | WALTER action |
|---------|---------------|---------------|
| **CONFIRMED** | Framing holds; primary source supports the claim as written | Proceed to Gate 3 as normal. Cite verification in signal body. |
| **CORRECTED-framing** | Primary source exists but the summary overstated or misframed | Rewrite signal body with corrected framing before Gate 3. Lower confidence by one band. |
| **FALSE** | Primary source contradicts the claim, or no primary source exists to support it | KILL. Log to kill_log.tsv with reason "framing-false, verify-research verdict". |
| **INDETERMINATE** | Primary exists but is ambiguous, or verification inconclusive within time budget | Route with lowered confidence (move to `unconfirmed` tier) and add note to signal body flagging the unverified framing. |

🔴 **SCOPE OF A `CONFIRMED` VERDICT — ADDED v0.34, 2026-08-20. A `CONFIRMED` CERTIFIES THE FIGURES AND THEIR FRAMING. IT DOES NOT CERTIFY A *SHAPE CLAIM* BUILT ACROSS THEM.**

**A shape claim is any verdict about the SERIES rather than about a figure: "peaked", "rising", "plateaued", "not a wave starting", "the trend has turned", "decaying".** **Every input can be correctly sourced, correctly dated, and correctly framed, and the shape verdict laid over them can still be false — because no per-figure check ever looked at it.**

⇒ **BEFORE WRITING A SHAPE WORD, RUN TWO QUESTIONS:**
1. **Is the series a RATIO or a QUANTITY?** **If a ratio — NAME THE DENOMINATOR AND CHECK WHETHER IT MOVED.** A share can plateau while the thing it measures doubles.
2. **Does the same shape hold on the underlying QUANTITY?** **If you cannot answer, do not write the shape word** — report the levels and say the shape is ungraded.

🔑 **BOUGHT 2026-08-20, AND THE CIRCUMSTANCES ARE THE POINT — this was NOT a sourcing failure.** `SIG-W-20260819-021` published *"the metric PEAKED IN MAY — 70 → 65 → 66 — this is not a wave starting."* **Every share figure was correct, every date was correct, and CREED (the trigger's owner) re-read all four Trepp primaries and confirmed so.** **But the denominator moved 2.3×** ($2.62B → $6.00B of newly-delinquent balances), **so in DOLLARS the series peaked in JULY at $3.96B — +40% vs May and +131% vs June.** **The shape verdict was exactly backwards on the measure carrying the risk, and nothing in Phase 1.5 as written would ever have caught it.**

⚠️ **WHY IT IS INVISIBLE RATHER THAN CARELESS (CREED's diagnosis, adopted verbatim): *a share plotted over time looks exactly like a trend and invites a shape verdict.*** **The chart shape and the risk shape are different objects that render identically.** ⇒ **`[[finding_verification_zero_is_ambiguous]]`'s sibling: a check certifies its OBJECT, not the claim built on it.**

📌 **AND THE PROPAGATION ASYMMETRY MAKES IT WORSE: the shape word is the QUOTABLE part.** It led the entry-point handoff, it is in the BOARD filename, and it travelled further than any figure in the signal. **The most memorable sentence gets the least verification and the most distribution — invert that.**

**Discretion:** If you already have the primary source open in the current session and the claim matches, no spawn required — note the inline-verification in the signal body and proceed. The trigger applies when you are relying on the secondhand framing.

**Investigation routing — verify-spawn (here) vs assign-DEWEY (Phase 2.8) (Will-directed 2026-06-27):**

Two refinements govern WHO investigates and WHERE the research lives:

1. **A paywalled / headline-only posting is an investigation POINTER, not a signal to route-or-kill.** When Will (or a feed) surfaces a gated headline, the job is NOT to relay the bare headline NOR to kill it as "thin / stale / already-covered." WALTER is the system's eyes/ears: **sense it, recognize the topic, then trigger the right investigation depth to recover what the article is communicating + pull the underlying data.** The headline is a lead, not the signal.

2. **Default the research to DEWEY; keep WALTER's context for sensing + routing.** Research execution should not live in WALTER's context. Discriminator:
   - **→ WALTER verify-spawn (this Phase 1.5 — narrow fast-path):** ONLY when a routing decision is BLOCKED *this session* and a cheap framing-check unblocks it — a FLASH/IMMEDIATE item that must route today, or "is this viral/extraordinary claim even true before I route it." Time-sensitive + decision-blocking + a quick check suffices. (The trigger patterns above still gate WHETHER a check is needed; this gates WHO runs it.)
   - **→ Assign to DEWEY (default — Phase 2.8):** every "investigate the topic / build out the data" job — multi-thread topics, non-urgent single articles, paywalled-pointer recovery where the value is depth + citations. Write a scoped `/deep-research` prompt to `AGENTS/DEWEY/inbox/WALTER/` (the create-only request lane) + log a `DEEP_RESEARCH_FLAGGED_LOG` row; route the cited result on return (Phase 2.8b). DEWEY's cited output beats a quick verify, and WALTER's context stays clean.

   **Litmus:** "Do I need the answer THIS session to make a routing call?" Yes → verify-spawn. No (topic-investigation / data-building) → assign DEWEY. **Worked examples 2026-06-27:** the flood article (SIG-W-20260627-030) routed same-session via a WALTER verify-spawn — *borderline* (non-urgent structural channel → under this rule it could have been a DEWEY assignment); the housing-distress cluster (paywalled foreclosure headlines) was correctly **assigned as DEWEY prompt #4** rather than relayed-as-headlines or run in WALTER's context.

---

## PHASE 1b: SAME-THEME COMBINE CHECK (Before Phase 2)

Once 2+ items have survived Phase 1 filters (in the current drafting session — items not yet dispatched to route_log.tsv), ask: **do any of them point at the same underlying event or specific sub-theme within the same canonical domain?**

```
For each pair of surviving items (i, j):
  Same canonical domain (per FORMAT_SPEC Domain Vocabulary)?   [hard requirement]
  AND same underlying event OR same specific sub-theme?        [soft test — domain alone is too broad]
  AND each origin adds independent value (not identical dup)?  [identical dup → kill the extra, don't combine]
  → YES to all three: COMBINE into one signal with multi-origin header
                      (origin becomes array per FORMAT_SPEC Multi-Origin Signals)
  → NO: process each item independently
```

**Multi-image batch dedup (fast path — v0.25, FILTER v3).** On a multi-image Will-Telegram drop (now the dominant intake mode), *before* running Phase-1 gates per image: **(a)** compare each image's Telegram `file_id` stem against the prior batch — an identical stem = exact re-send → dedup-skip with one audit note, no re-OCR; **(b)** if stems differ, a re-send can still carry a *fresh* stem, so content-grep each image against BOARD INDEX + `kill_log` before processing. For a fully-duplicative batch, log ONE consolidated `re-send dedup` kill row (log_reconcile counts unique signal_ids, so the dedup row is free). *(Recurred 6/28 batch-4, 7/4 batches 2–3.)*

**Pre-dispatch only.** While drafting, items from any arrival path — same Telegram batch, different batch, separate Will message, WALTER-found article — may fold in. Once a signal has been appended to route_log.tsv, it is immutable; later items become dup-kill or follow-up signals that cite the prior SIG-ID. No retroactive merging.

**Thin-liquidity prediction-market fold-convention (v0.26, Will-approved 2026-07-09):** a **low-volume** Polymarket/Kalshi/ORACLE prediction-market datum that **corroborates an existing signal's thesis** FOLDS into that signal as a **market-implied-timing layer** (a `dispatch_note`/body line — e.g. "Polymarket <50% Hormuz-normal-by-7/31 = market-implied timing"), **NOT a standalone dispatch.** Rationale: thin-liquidity prints are noisy/manipulable and carry more signal *as a timing overlay on a thesis WALTER already routes* than as their own entry — matches the thin-liquidity-discipline (`[[finding_thin_liquidity_prediction_market_discipline]]`). A prediction-market datum that OPENS a *new* thesis (no existing signal) still routes normally to ORACLE/the owner; the fold applies only to corroboration of an already-live signal. (First use: 6/22 Polymarket-Hormuz fold.)

**Common cases the check catches:**
- Paired-chart posts by the same author (Bilello VIX + SPX 3-wk extremity — MARKET_VOL, extremity-counter)
- Cross-source same-event (disclosetv carrier build-up + BRICSinfo talks rejected — GEOPOL_ENERGY, Iran-escalation)
- Visual + analytical versions of the same physical event (Flightradar24 Doha overflight + Celestyal cruise Hormuz transit — GEOPOL_ENERGY, Hormuz operational state)
- Bundled macro prints on the same sub-theme (CPI + UMich prelim — MACRO_INFLATION, stagflation-pressure)

**What the check does NOT catch:**
- Different domains, same broad narrative ("recession fears" spanning LABOR + CONSUMER_CREDIT + BANK_CRE) — route separately; NEXUS owns cross-domain synthesis.
- Different events in same domain (Hormuz shipping + Iran nuclear talks, both GEOPOL_ENERGY but different events) — route separately.
- Second source arriving post-dispatch — dup-kill or follow-up, never retroactive merge.

See FORMAT_SPEC v0.6 Multi-Origin Signals section for full combine rule, origin array syntax, body conventions, and historical examples.

---

## PHASE 2: CLASSIFY (For signals that survive intake)

**Precedence** — how fast:
| Level | Criteria | Target |
|-------|----------|--------|
| FLASH | Portfolio damage imminent, system-threatening | Immediate |
| IMMEDIATE | Thesis-critical, threshold breach, confirmed catalyst | <30 min |
| PRIORITY | Meaningful new information, requires agent analysis | Next agent boot |
| ROUTINE | Background context, monitoring update | Archive only |

**Confidence** — how much to trust. TWO bound fields, both required:

| `confidence_language` | `confidence` band | Meaning |
|-----------------------|-------------------|---------|
| `confirmed` | **0.90–1.0** | Official data release (BLS, FRED, SEC, central bank) OR multiple independent authoritative sources verifying same fact |
| `reports` | **0.75–0.89** | Single credible named source with direct knowledge (Bloomberg, Reuters, SEC filing, named analyst) |
| `assessed` | **0.50–0.74** | Strong indicators, agent synthesis or inference, not direct evidence |
| `unconfirmed` | **0.30–0.49** | Single source, no corroboration — flag heavily, usually shouldn't route |
| (filtered) | **<0.30** | Below threshold — kill log, not the archive |

The numerical score lives in the YAML header for machine routing. The language tier is a SECOND header field bound to the score. They cannot disagree. See SIGNAL_FORMAT_SPEC.md "Confidence Model" section for full mapping rules and adjustment factors.

**Two-source rule:** Don't promote to IMMEDIATE+ unless corroborated. Exception: "golden source" with direct knowledge (single official release like a BLS print can stand alone at `confirmed`).

**Conflict zone** — relationship to thesis (analytical step, NOT a header field):
- 🟢 Confirms thesis (gas hits $4 as CARL predicted)
- 🟡 Tension — doesn't break thesis but doesn't confirm (HY OAS tightening)
- 🔴 Contradicts thesis or threatens position (major counter-signal)

> **Why this is not a header field:** A signal's conflict_zone is recipient-dependent — the same signal can be 🟢 for CARL (confirms consumer stress) and 🔴 for HENRY (contradicts Fed-trap resolution). Baking one conflict_zone label into the header would collapse that nuance. Instead: use this step to sharpen the **Relevance** body section so each recipient sees the signal through their own thesis lens. If you need a header-level marker for machine filtering, use `signal_type` (which IS in FORMAT_SPEC) — e.g. `counter-evidence` vs `thesis-confirmation`.

**Cluster assignment** (added v0.9, 2026-05-05): Every dispatched signal lands in exactly one primary cluster per `design/CLUSTER_TAXONOMY.md`. Decide before writing the signal file:

```
1. Which cluster does this fit? Pick from the 10 buckets in CLUSTER_TAXONOMY.md.
2. Does it fit two? Apply edge-case rules (substance > mechanism > action-recipient).
3. Doesn't fit any? → MISC. New cluster only with explicit Will sign-off (≥3 signals on a coherent new theme + expected forward-momentum).
```

The cluster is written to the signal YAML header (`cluster: <NAME>`) AND determines which section of `/BOARD/INDEX.md` the dispatch row lands in. CLUSTER_TAXONOMY.md is canonical-source for the bucket names — don't invent.

**Superevent check:** Do any signals from this session GROUP into a convergence event more significant than its parts?

**🔴 Step 4.4 — THE ACTION-LINE RULE (added v0.29, 2026-07-27, Will-approved; canonical BOARD_CONSUMPTION_SPEC §3.5.4).** Before filling any other field, split `action:` from `info:` by **what the signal asks**, not by whose domain it touches:

> **If the signal carries an ask directed at a named recipient, that recipient goes on the `action:` line — not `info:` with the ask buried in the body.**

**Ask literally: "does this signal ask anyone to DO something — pull a filing, re-mark, re-pull, adjudicate, fix a tool, answer a question? Then they are `action:`."** Domain-adjacency alone is `info:`; a *request* is `action:`.

**Why this is a safety precondition, not tidiness:** the §3.5 pull-complete exemptions (CARL, RED, PROME) all rest on *"this agent is never the ACTION owner ⇒ zero ACTION-miss risk."* **That is a claim about the accuracy of this metadata, not about the agents.** Bury an ask for an exempt agent inside an `info:`-only signal and it arrives as one line in a diff-scan they have been told they may skim. Exempt agents' scanners `exit 1` on action-line items, so correct tagging converts a hopeful skim into a hard stop. **Binds for EVERY recipient** (it is simply correct metadata); it is only a *hard stop* where the recipient's scanner enforces it.

**Same asymmetry as §3.5.3, applied one level in:** *actionable ⇒ dispatched* becomes *actionable **for a named recipient** ⇒ that recipient is **actioned***. Over-marking costs one extra handoff; under-marking hides an ask.

*(Bought by `SIG-W-20260727-016` — `action: [RED, LIQUID]` / `info: [..., PROME]` while its §8 carried a direct operational ask to PROME as RESEARCH-INTAKE lane owner. **Raised by PROME against its own exemption proposal**, i.e. the recipient argued for the rule that constrains the exemption it was requesting.)*

---

**Step 4.5 — v0.8 routing-augmentation field tagging** (added v0.11; applied AFTER cluster assignment + Superevent check + step 4.4, BEFORE the routing-augmentation steps 5-7 below). For each surviving signal, fill the v0.8 optional fields per FORMAT_SPEC v0.8 / JOINT_PROPOSAL §2a + §2d.5:

> **🆕 FIRST, the one MANDATORY field in this step (v0.35 / FORMAT_SPEC v0.18, 2026-08-20): `entities:`** — a YAML list of the signal's specific proper nouns (tickers, orgs, named instruments/series, places), hyphenating multi-word names (`Western-Alliance`), including both ticker and unambiguous name where a bare ticker collides with prose (`WAL` grepped at 78% noise). **Every signal dispatched 2026-08-20 or later carries it; older signals are NEVER retro-filled.** Doctor `entities_at_dispatch` flags omissions.

- **`cluster_secondary`** (comma-separated) — multi-cluster signals tag primary cluster (already set in step 4 above) plus optional secondaries in descending action-relevance order. Drives batch-folding at recipient boot. Tag whenever applicable. Skip if no cross-cluster relevance.

- **`signal_role`** (4-value enum: `primary_substance` / `cluster_mediating` / `counter_evidence` / `thesis_confirmation`) — tag the role within the cluster narrative. Authoritative-voice precedence on `cluster_mediating`: NEXUS > WALTER (tagger) > action-primary. Tag whenever the role is non-default-primary (i.e., always tag explicitly when it's `cluster_mediating` / `counter_evidence` / `thesis_confirmation`; `primary_substance` is the default and may be omitted).

- **`consumer_transmission`** (9-value enum) — tag ONLY when CARL is on the routing line (action OR info). Pick the mechanism through which the signal reaches CARL's consumer-stress thesis: `pump_pass_through` (oil/gas → retail pump → CPI energy → consumer-burden) / `wage_pressure` (labor data → wage growth / employment cost index) / `wealth_effect` (equity-portfolio-driven top 40% → discretionary spend) / `policy_pass_through` (tariff / regulatory / fiscal → consumer-cost / income) / `discretionary_demand` (observation-side demand-destruction) / `services_export` (international-inbound demand) / `lng_substitution` (LNG redirect → US/EU gas → heating-fuel substitution; BRENT-side outbound) / `counter_evidence` (within-cluster counter-thesis data) / `none` (info-only, no consumer-stress transmission). Skip when CARL not on routing line.

- **`consumer_lens`** (4-value enum: `tier_stratified` / `broad_collapse` / `mixed` / `counter`) — tag ONLY on consumer-cluster signals with CARL on routing line. Codifies K-shape framing: `tier_stratified` = mid-tier pullback with top-decile counter-channels intact / `broad_collapse` = multi-tier consumer demand destruction / `mixed` = multi-axis no clear K-shape / `counter` = counter-evidence to consumer-stress thesis. Energy-cluster signals don't carry.

- **`event_window`** (boolean: `open` / `closed`) — read current state from `AGENTS/WALTER/design/EVENT_WINDOW_STATE.md`. If state = OPEN: set `event_window: open` on Phase-2-cluster signals; cross-cluster signals stay `closed`. If state = CLOSED (default): omit field or set `closed`. State transitions are BRENT-declares-OPEN / WALTER-declares-CLOSE per JOINT_PROPOSAL §2d state machine.

**Worked example (today's SIG-W-20260508-006 NFP, retro):** primary cluster CONSUMER_STAGFLATION + cluster_secondary BANK_COLLATERAL (Financial -11K cross-cluster) + signal_role cluster_mediating (paper-vs-structural Goldilocks-tape vs stagflation-underbelly) + consumer_transmission wage_pressure (AHE 3.6% YoY accelerating + LFPR drop) + consumer_lens mixed (multi-axis labor cooling AND wages accelerating) + event_window closed (no Phase-2 declaration active 2026-05-08). The v0.7 `cluster_mediating: true` interim form on today's dispatches maps equivalently to v0.8 `signal_role: cluster_mediating` — forward dispatches use the v0.8 form.

**Routing augmentation (steps 5-7 added v0.10 — applied AFTER domain + signal_type + cluster + step 4.5 v0.8 tagging, BEFORE Phase 3 OUTPUT writes the signal):**

5. **Cluster-mediating auto-cc.** If signal carries `signal_role: cluster_mediating` (v0.8 canonical), ensure RED in info line. Skip if RED already in to/info. Per ROUTING_TABLE v0.7 By Tag/By Verdict. **Legacy compatibility:** v0.7-era signals with `cluster_mediating: true` boolean field map equivalently — read either form. Pre-v0.7 prose-tagged paper-vs-structural / tape-vs-substance / bifurcation / divergence dispatch_note language is fully retired as of v0.11; new signals use `signal_role` header field.

6. **CORRECTED-FRAMING auto-cc.** If verify-research returned CORRECTED-FRAMING verdict (Phase 1.5 output), ensure RED in info line. Skip if RED already in to/info. Composes with step 5 — apply both, but RED appears once. Per ROUTING_TABLE v0.7 By Tag/By Verdict.

7. **Falsification-trigger auto-fire scan.** Before final dispatch session-end, scan `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` for any thresholds that crossed during the current session per JOINT_PROPOSAL_2026-05-06_red_walter §2 eval logic (read-loop step 6b in WALTER spawn-protocol; sustain-window check, threshold evaluation, last-fired suppression via `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`). For each sustained cross: auto-generate falsification-derived signal with:
   - `signal_type: threshold-crossed`
   - `falsification_trigger: <RED-FT-NN>` body field
   - Action recipient = `trigger.recipient_chain.action`
   - Info recipients = `trigger.recipient_chain.info`
   - Precedence per `trigger.action` enum (IMMEDIATE-FALSIFY → IMMEDIATE / PATH-B-CONFIRM → PRIORITY / ADD-POSITION → IMMEDIATE / etc.)
   - dispatch_note carrying trigger_id ref + current vs threshold value + sustain confirmation count + falsification_thesis_ref pointer
   - Cluster per metric (HY-OAS → BANK_COLLATERAL, BRENT-PAPER → IRAN_HORMUZ or HYDROCARBON_INFRA per state, INITIAL-CLAIMS → CONSUMER_STAGFLATION, VIX → POSITIONING_VALUATION, CCC-OAS → BANK_COLLATERAL)

   > 🔴🔴 **STATE RULE — ADOPTED 2026-08-22 (REGINALD's wording, PROME-endorsed, WALTER's file and WALTER's call per the packet). A TRIGGER WITH AN EXIT CONDITION IS A STATE MACHINE, NOT AN EVENT COUNTER.**
   >
   > **> Trigger fire STATE is graded against the INSTRUMENT — close-by-close against the registered trigger AND its registered exit — never inherited from a board summary. Closes inside a fired state are RE-ENTRIES, not fires.**
   >
   > 🔑 **BOUGHT BY A BOARD THAT WAS WRONG IN BOTH DIRECTIONS AT ONCE.** On 8/20 WALTER's live board carried **"ZERO FIRES"** for `REG-T-02` **and** *"still between fire and exit."* **Both false, in opposite directions.** REGINALD's ruling of record graded it: **FIRED 2026-05-11 at 76.95** (WALTER's own 7/27 claim was correct) · **8 further sub-78 closes 5/12→6/03 were RE-ENTRIES INSIDE the fired state, not 8 fires** · **EXIT MET 6/30** (`WAL ≥81.90` on 3 consecutive closes: 6/26 82.05 · 6/29 82.88 · 6/30 82.20), satisfied twice more since as no-ops. **Ruled state token: `REG-T-02: UN-FIRED (exited 2026-06-30; prior cycle 2026-05-11 → 2026-06-30)`.**
   >
   > ⚠️ **NEITHER board statement was a reading of the tape.** Both were artifacts of a fire-ledger that recorded **neither the fire nor the exit** — and **a ledger that can be simultaneously wrong in both directions will do it again on a different trigger.** ⇒ **the fix is to grade at the instrument, not to correct the summary.**
   >
   > ✅ **OPERATIONAL CONSEQUENCE, LIVE NOW: a `WAL` close <78 from 8/21 onward is a FIRST FIRE OF A NEW CYCLE — fresh signal, full `V1V3-ACCELERATE` chain (REGINALD / WAL / Will), NO duplicate suppression.** Subsequent re-entries inside that new fired state ARE suppressed. **8/21 close: $79.67 — 2.1% above the line, un-fired.**
   >
   > 📌 **Generalises to every exit-carrying row on the board** (`RED-FT-01`/`-06`/`-07`/`-09`/`-10`, `REG-T-*`, `CREED-T-*`): **read the exit column before reporting a state, and report the STATE, not the last event.** `[[finding_record_of_an_action_is_not_the_action]]`

   Append fire row to `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` (5-col schema: trigger_id / fired_date / metric_value_at_fire / dispatched_signal_id / sustain_confirmation — per JOINT_PROPOSAL §2.4, preserves Critical Rule #2 by keeping fire-history out of RED's tree). Approaching-threshold (within 5% one-sided per `threshold_op`) flagged in WALTER closeout SESSION LOG as "near-trigger watch", not auto-dispatched. Stale-fire suppression: skip a trigger if it fired within prior `sustain_window` sessions per the ledger.

**Phase 1.5 verify-research note:** when CORRECTED-FRAMING verdict returns from a verify-research spawn, the Phase 2 step 6 auto-add-RED rule fires automatically downstream — no special handling needed in Phase 1.5 itself. Verdict logging stays in dispatch_note as prose; Phase 2 reads it.

---

## PHASE 2.5: EVENT-WINDOW STATE CHECK (Precedence override)

Added v0.11 per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2d.6. Runs once per session AFTER Phase 2 classification has assigned per-signal precedence, BEFORE Phase 3 OUTPUT writes. Reads `AGENTS/WALTER/design/EVENT_WINDOW_STATE.md` for current declared state.

```
Read EVENT_WINDOW_STATE.md → current state?

  CLOSED (default)         → no action; Phase 2 precedence assignments hold; proceed to Phase 3
  OPEN                     → for each signal, check cluster:
                             - Phase-2-cluster (IRAN_HORMUZ + HYDROCARBON_INFRA + OIL_ENERGY-domain transmits) →
                                 * override precedence to FLASH (regardless of Phase 2 default)
                                 * tag signal header `event_window: open` per FORMAT_SPEC v0.8
                                 * Will-Telegram pings thread under "BURST WINDOW OPEN — Phase 2 trigger" master
                                 * verify-research mandatory on extreme-claim items (heightened threshold)
                             - Cross-cluster (CONSUMER_STAGFLATION / BANK_COLLATERAL / POSITIONING_VALUATION /
                               FED_FRAMEWORK / etc.) →
                                 * Phase 2 precedence holds (no override)
                                 * tag `event_window: closed` (default) — don't bleed window context
  PENDING_VERIFICATION     → treat as OPEN; verify-research extra-mandatory; gate-status check first
```

**Daily roll-up requirement during OPEN:** WALTER posts a single 00:00 UTC roll-up message (signal count, key dispatches, verification-gate progress per gates a-d in EVENT_WINDOW_STATE.md). One message per UTC day until window closes.

**Close-of-window summary required at OPEN→CLOSED transition:** WALTER posts a window-summary to Will (window duration, dispatches fired, gate-confirmation status, any retroactive false-positive-tagging if early-close per LESSONS #18 disambiguation).

**Stale check:** if EVENT_WINDOW_STATE.md hasn't been updated in >7 days AND state shows OPEN, flag stale and revert to BALANCED posture pending freshness re-confirmation (don't sit in declared-OPEN forever on memory alone).

**Composes with Phase 2 routing-augmentation steps 5-7:** OPEN-window precedence override happens AFTER cluster_mediating + CORRECTED-FRAMING + falsification_trigger augmentation — it overrides the precedence floor but doesn't change recipient routing. RED auto-cc still applies; falsification triggers still fire as configured.

See FILTER_SPEC v0.5 "OPEN-window dispatch posture" sub-section for the full posture rules + cost-asymmetry justification + state-transition handling. EVENT_WINDOW_STATE.md is canonical for current state.

---

## PHASE 2.8: DEEP-RESEARCH CANDIDATE SCAN (Full WALTER only)

Added v0.18 (Will sign-off 2026-06-19). Runs at dispatch-batch shaping, AFTER Phase 2.7 composite-bifurcation tagging and BEFORE Phase 3 OUTPUT writes. A triage flag with **no research-execution load** — surfaces signals worth a deeper `/deep-research` pass; **Will decides every time, WALTER never runs it.** Canonical: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md`.

For each surviving signal, check the trigger set **AND** the gate (the gate is the noise-suppressant — without it the triggers describe the median signal here and the flag fires 3-5×/day):

**Triggers (any one):**
- **T1 new-coverage-channel** — opens a signal lane / sub-domain the network doesn't yet track (FL bankruptcy-filings → CORAL). Highest value — what the system structurally can't see on its own.
- **T2 new-cross-channel-interaction** — reveals an unmapped transmission path; must clear MORE than routine `cluster_secondary` tagging.
- **T3 load-bearing-but-thin-evidence** — could affect a position/thesis, routed SKIP-VERIFY/single-verify, but the *surrounding evidence base* is shallow (distinct from Phase 1.5 "is the framing true?" — T3 is "is the broader case under-researched?").
- **T4 position/thesis-pivot** — the answer could change position **sizing, timing, or core confidence.**
- **T5 verify-left-material-uncertainty** — CORRECTED-FRAMING / INDETERMINATE leaving a *substantive* open question (not a framing nit; about the residual question, not the correction).

**Gate (mandatory — applies to every trigger):** WALTER must state, one line each — **(a)** the question a *cheap verify can't* answer that deep-research would resolve, and **(b)** the consequence — the specific position size/timing, thesis weight, or coverage-channel decision that moves. **No consequence → no flag.** (Same discipline as the verify-spawn rule: decision-usefulness, not comprehensiveness.) A signal CONFIRMED by verify can still be a deep-research candidate — they're orthogonal.

**For any signal that passes:**
1. Add the 🔬 line to the Phase 3 push (template below).
2. Embed the ready-to-run `/deep-research` prompt in the BOARD signal body under a `## 🔬 Deep-research prompt (candidate)` section — persists in the permanent archive, not just Telegram.
3. Append a row to `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` (**13-col as of v0.27**): `disposition: PENDING`, `outcome: PENDING`, `executor: DEWEY` (default — Will opens a DEWEY session; set `Will` only if Will runs `/deep-research` directly), `prompt_ref` = the BOARD signal path, `deadline` = the date/named-event the research is decision-useful by (or `open` if not time-sensitive), **`impact` = LEAVE EMPTY at flag time** (free text, populated later at *consumption* — see below).
4. Tag the BOARD `dispatch_note`: `deep_research_candidate: <trigger-id> — <one-line decision question>`.

**Telegram push template** (appended under the normal push):
```
🔬 DEEP-RESEARCH CANDIDATE — SIG-W-YYYYMMDD-NNN
Why: <trigger + the stake, one line>
Question: <the specific decision question>
Would change: <the position / thesis / coverage that moves>
Run it: DEWEY session → /deep-research <self-contained prompt — pre-answer the skill's clarifiers>
```

**`/deep-research` prompt shape** (so Will can paste-and-go): `<Subject>: <the specific question>. Scope: <in/out of bounds>. Timeframe: <period>. Region/entities: <…>. This informs: <the decision it feeds>. `**`kill_condition: <moot if X has happened / after date Y; re-verify Z at intake>.`**` Prioritize primary sources; flag where evidence is thin or contested.`

**🆕 `kill_condition:` — REQUIRED on every new prompt (v0.27, 2026-07-24).** Closes a silent-failure mode: a prompt whose timing rationale has rotted still *runs*, at full cost, answering a question that no longer decides anything. Evidence: **PROMPT-15** (run 7/24) had `deliver_by` **10 days passed** with its gating catalyst already fired — caught by DEWEY's discipline, not by any mechanism; **prompt 12** (7/16) was parked after 2 of 3 decision-feeds resolved pre-run. Freeform, any mix of (a) event-based kill trigger, (b) date-based expiry, (c) re-verify-at-intake instruction. **Required on new prompts, optional on revisions** (no retro-fill). **Enforcement is DEWEY-side and self-enforced** — DEWEY's intake reads the field and **refuses to run if the condition is satisfied**, returning the prompt with the reason; **no new WALTER-side machinery.** Authoring bar: a kill_condition that can only be evaluated *by doing the research* isn't one — it must be checkable in seconds (a date, a calendar event, a published print).

**🆕 `impact` ledger column — populated at CONSUMPTION, not at flag time (v0.27, 2026-07-24).** One free-text line on what the consuming agent actually DID with the returned report (gate armed / killed / not-fired / calibrated / no-op-yet / thesis re-weighted). **The consuming DOMAIN AGENT writes it** when the report is load-bearing for a state change (closest to the event); **PROME sweeps the misses at its closeout.** **WALTER owns the ledger but is not the capture bottleneck** — do not block a dispatch on an empty `impact`. Rationale: DEWEY shipped 3 reports on 7/24 with zero structured path for impact to return, so it can't tell which prompt *kinds* pay off. Backfill-safe (existing rows empty; `walter_doctor` reads by column name). **Honest limit: this measures the flagged-prompt lane only** — Will-directed carve-outs and agent-originated slates (e.g. CARL's) never open a ledger row.

*Both items: DEWEY process-v2 memo 7/24 → PROME-endorsed with implementation authority granted (WALTER-owned template + ledger, no Will gate); Will-endorsed in-session 7/24. Full spec: `design/DEEP_RESEARCH_FLAG_PROPOSAL.md` §5b + §5e.*

**Constraints (hard):** **Full WALTER only** (Quick escalates — never raises this flag); **max 3 flags per batch**, target ~1-2/week; flag decision-useful unknowns, never "interesting"; **no auto-run, no sub-agent spawn, no research execution by WALTER** — deep-research is explicitly NOT in the autonomous-verify-spawn class. WALTER surfaces the prompt; **DEWEY executes it (Will triggers/approves)** — Will opens a DEWEY session (Tier-2, Claude Code), feeds it the prompt; DEWEY runs `/deep-research` under its citation/counter-evidence discipline, archives the cited report to `AGENTS/DEWEY/output/`, and hands it back to WALTER (Phase 2.8b). *(v0.20: executor moved "Will runs it" → DEWEY per the DEWEY revival; WALTER still never runs research itself.)*

**Calibration:** light review every closeout (glance at the week's fires + dispositions); formal review at **14 days OR 20 flags**, whichever first. Tighten if >2/wk sustained AND Will-`SKIPPED` rate >50%; loosen if <1/wk AND a retro "obvious miss" surfaces. `walter_doctor` `deep_research_pending_overdue` (check 10) surfaces PENDING-past-deadline rows (+ stale `open`>30d) in the boot reply. Data source: the ledger `disposition` + `outcome` columns; WALTER backfills `disposition`/`outcome` at next boot from Will's action.

**Honest load note:** the flag itself is zero research-execution load (one line at dispatch; WALTER never runs/spawns). The small *named* recurring costs: the ledger disposition/outcome backfill at boot + the `deep_research_pending_overdue` doctor check — both near-zero.

---

## PHASE 2.8b: RETURNING-DELIVERABLE HANDLING (route the `/deep-research` output)

Added v0.19 (Will sign-off 2026-06-19); **executor + consumption wiring v0.20 (2026-06-20).** Phase 2.8 *raises* the flag; this closes the loop when the `/deep-research` deliverable comes back. **Deliverable arrival (v0.20):** DEWEY drops a **create-only handoff in `AGENTS/WALTER/inbox/DEWEY/`** pointing at its `output/YYYY-MM-DD_topic.md` report + naming the originating flag ID (or Will pastes it live). **WALTER scans `inbox/DEWEY/` (non-`processed/`) at boot** (spawn-protocol step 7d) and consumes any NEW handoff. **WALTER routes the output — it does NOT re-analyze it** (lean mandate: the packet IS the analysis; `[[feedback]]` 2026-06-19 "WALTER stays lean").

**Default — ONE `research-output` BOARD signal:**
1. Archive the deliverable as a single signal (`signal_type: research-output`, next `SIG-W-YYYYMMDD-NNN`), **embed the packet verbatim** under a `## Full research packet (verbatim)` section — keeps BOARD the self-contained SoT and `walter_doctor board_reconcile` happy with one file.
2. Write a thin **routing wrapper** on top: a one-line **verdict** + a **per-recipient genuine-delta block** — what's NEW vs each recipient's current state (per `feedback_check_recipient_before_sharing`). Surface the ONE finding that MOVES a thesis, not a re-summary.
3. **No verify-spawn** — a deep-research deliverable is already primary-sourced → `verify_verdict: VERIFIED-PRIMARY`; a $0.05 routing-check is strictly dominated. (Carry through any caveat the deliverable itself flags; don't re-verify the whole thing.)
4. Route to the **domain owner (action) + genuine-delta info recipients**; run normal Phase 2 cluster/role tagging + Phase 3 + Phase 3.5 delivery.
5. **Close the ledger** — set the originating `DEEP_RESEARCH_FLAGGED_LOG` row `disposition: RESOLVED`, `outcome: DELIVERED as SIG-W-…`, and `executor:` = who actually ran it (DEWEY | Will). (`walter_doctor deep_research_pending_overdue` then drops it.)
6. **Mark the handoff PROCESSED (v0.20)** — if the deliverable arrived via a DEWEY handoff in `inbox/DEWEY/`, `git mv` it to `AGENTS/WALTER/inbox/DEWEY/processed/` once routed. Lifecycle: **NEW** (DEWEY created it in `inbox/DEWEY/`) → **ROUTED** (the `research-output` BOARD signal now exists) → **PROCESSED** (moved to `processed/`). The dir-move IS the state machine — it prevents the boot-scan from repeat-routing the same report. WALTER owns the move; DEWEY only ever creates in `inbox/DEWEY/`, never touches `processed/`. Use `git mv`, not bash mv (per `[[feedback_git_mv_for_inbox_processing]]`). (Mirrors the recipient-side `inbox/WALTER/` → `processed/` pattern from WALTER Routing v2 — here WALTER is the recipient of DEWEY's handoff.)

**Split test — carve a finding into its OWN signal only when it meets ANY one:**
- **S1 — different action-owner AND independently actionable:** owner ≠ the document's owner AND it stands alone as a decision, not just FYI context.
- **S2 — maps to a registered trigger / falsification anchor** (RED-FT / REG-T / ROUTING_TABLE Boundary): needs independent tracking + may auto-fire.
- **S3 — ages / falsifies on a different clock:** you want to lifecycle-tag it (SUPERSEDED / FALSIFIED / EVENT-PASSED) independently of the parent.
- **S4 — standalone discovery unit:** a finding someone would grep BOARD for on its own, in a different primary cluster.

**Precedence note (S4 vs the wrapper-delta):** a finding *elevated as THE wrapper-delta* — the one finding that moves a thesis, surfaced prominently in the parent verdict + its own per-recipient block — already satisfies the discovery need, so **S4 does not independently force a split for it.** Split on S4 only when the finding is a genuinely separate discovery unit you'd grep for independently AND it is *not* already the parent's headline. A finding that merely sits in a different `cluster_secondary` is **not** automatically S4 — the parent's `cluster_secondary` tag + delta wrapper already cover cross-cluster discovery.

If a finding passes, dispatch it as a **child signal that cross-refs the parent** (`deep_research_ref: <parent SIG-ID>`); the parent stays the archive/SoT. **Default remains one signal + delta wrapper — splitting is the exception, paid only when the test is met.** Asymmetry: over-splitting = recipient noise (one owner gets N handoffs for one doc) + scattered archive + messy ledger; under-splitting = a trigger-linked or differently-aging finding buried where it won't get tracked. So one-by-default, split-on-test.

**Worked example — SIG-W-20260619-008 (S-FL distress deep-research, the first instance):** routed as ONE signal → CORAL action / REGINALD,CARL,SHADE,MARCO,RED info, packet embedded verbatim + 6 per-recipient delta handoffs; closed the SIG-007 ledger row. Split test applied finding-by-finding — bankruptcy/per-capita, bank-transmission, consumer/energy-CPI, business-bankruptcy, macro-overlay all FAILED (same owner CORAL/REGINALD, interdependent legs of one 70/30 verdict, no trigger linkage, same ~Q2/Q3 clock) → kept unified. The **insurance commercial/condo finding** was the one borderline candidate (distinct INSURANCE cluster, SHADE-relevant, the only thesis-correcting item) but FAILED all four — S1 (still CORAL-action — it's CORAL's mechanism), S2 (no registered trigger), S3 (same ~Q2/Q3 clock as the rest), S4 (per the precedence note: it was **elevated as THE wrapper-delta + cc'd SHADE**, so the distinct INSURANCE `cluster_secondary` alone doesn't force a split) → kept in rather than fragmenting. Net: one signal was correct.

---

## PHASE 3: OUTPUT (Write the signal)

**Disposition** — exactly one of:
| Disposition | What happens | When |
|------------|-------------|------|
| **PUSHED** | BOARD archive + Phase 3.5 delivery handoffs + Telegram ping to Will | FLASH / IMMEDIATE |
| **ARCHIVED** | BOARD archive + Phase 3.5 delivery handoffs (recipient consumes from `inbox/WALTER/` at boot) | PRIORITY / ROUTINE |
| **FILTERED** | Kill log entry only | Below threshold, already known, not relevant |

*v0.14: both PUSHED and ARCHIVED now write Phase 3.5 delivery handoffs into each recipient's `inbox/WALTER/` (not the old BOARD-only "agents pull from INDEX" model). FLASH still additionally Telegram-pings Will. Delivery ≠ consumption — see BOARD_CONSUMPTION_SPEC §1.*

*v0.24 (2026-07-04) / v0.26 (2026-07-09) / v0.29 (2026-07-27): **pull-complete recipient exemption** — for a recipient on the BOARD_CONSUMPTION_SPEC §3.5 exemption list (**CARL + RED + PROME** as of v0.29 — each runs a complete whole-INDEX BOARD-diff/scan at boot, so its own scan is already a complete pull; **RED and PROME are additionally INFO-cc-only → zero ACTION-miss risk**), **SKIP the Phase 3.5 inbox handoff + the `delivery_log` delivery row.** Still write the BOARD entry + `route_log` row (published + audit-logged as normal); only the redundant push to that agent is skipped. **NOT exempt:** REGINALD (tiered/selective scan — can miss the cluster an ACTION lands in) + SAM (no `/BOARD/` scan) + everyone else. Verify empirically (the agent's ACTION handoffs already appear dispositioned in its ledger, zero un-dispositioned ACTION — or, like RED and PROME, it never receives ACTION) before adding an agent to the list. **PROME (v0.12/2026-07-27, Will-approved): `PROME/tools/board_scan.py` every-boot `--advance`, complete-not-tiered, plus 0 action-line appearances in 605 signals all-time with the scanner `exit 1`ing if that changes. Applies to DISPATCHES where PROME is info-only; notes are still delivered (§3.5.1).**

> **🔴 PRECONDITION — THE ACTION-LINE RULE (§3.5.4, v0.12). Check this BEFORE applying any skip above.**
> **If the signal carries an ask directed at a named recipient, that recipient goes on the `action:` line.** The exemption is only safe because exempt agents are never ACTION owners — **which is a claim about metadata accuracy, not about the agents.** Burying an ask for an exempt agent in the body of an `info:`-only signal defeats the whole exemption: the ask arrives as one line in a diff-scan the agent has been told it may skim. **Ask at tagging time: "does this signal ask anyone to DO something? then they are `action:`, not `info:`."** *(Bought by `SIG-W-20260727-016` — `action: [RED, LIQUID]` / `info: [..., PROME]` with a direct operational ask to PROME in §8; raised by PROME against its own exemption proposal.)*

*⚠️ **Scope limit — this skip is about DISPATCHES only** (BOARD_CONSUMPTION_SPEC **§3.5.1**, v0.9, 2026-07-16; pointer only — no CHECKLIST process change, since a note is not a dispatch and never enters Phase 3). The skip is sound **only because the recipient's whole-INDEX BOARD-diff is fed the same BOARD entry as the handoff**. A deliberately **non-BOARD note** (create-only `*-NOTE.md` — a mechanism/correction/cross-reference that fails the Novelty gate as a signal but whose value-add the owner lacks; no BOARD entry, no `route_log` row, no `delivery_log` row) **has no BOARD entry for a BOARD-diff to find → the inbox is its ONLY channel, and it IS delivered even to CARL/RED.** Do not read "CARL/RED are exempt" as "never write to their inbox." Canonical rule + the accepted no-telemetry caveat: BOARD_CONSUMPTION_SPEC §3.5.1.*

**Signal file structure** (three-layer tearline):

```yaml
# Layer 1 — Header (machine-scannable)
# Full schema per SIGNAL_FORMAT_SPEC.md. All fields required unless marked optional.
---
signal_id: SIG-W-YYYYMMDD-NNN
precedence: FLASH | IMMEDIATE | PRIORITY | ROUTINE
timestamp: 2026-MM-DDTHH:MM:SSZ
source: WALTER
origin: "Free text — where raw info came from (e.g. BLS, Reuters, agent inbox)"

to: AGENT (ACTION)
info: AGENT, AGENT                    # optional
group: AIG_NAME                       # optional; see FORMAT_SPEC AIGs

signal_type: threshold-crossed | pattern-match | catalyst | divergence | research | position-risk | context | manual-flag
confidence: 0.0–1.0                   # numerical score, bound to language tier
confidence_language: confirmed | reports | assessed | unconfirmed
resources: 0 | 1 | 2                  # processing resource estimate
safety_net: clear | triggered         # override fired?

word_count: NNN                       # FLASH/IMMEDIATE must be ≤200

cluster: <CLUSTER_NAME>               # required v0.7+; one of 10 buckets per CLUSTER_TAXONOMY.md

# v0.8 optional routing-augmentation fields (added 2026-05-08 per JOINT_PROPOSAL §2a + §2d.5)
cluster_secondary: <CLUSTER_NAME>[, <CLUSTER_NAME>]   # multi-cluster cross-tag, descending action-relevance
signal_role: primary_substance | cluster_mediating | counter_evidence | thesis_confirmation
consumer_transmission: pump_pass_through | wage_pressure | wealth_effect | policy_pass_through | discretionary_demand | services_export | lng_substitution | counter_evidence | none   # CARL-on-routing-line only
consumer_lens: tier_stratified | broad_collapse | mixed | counter   # consumer-cluster + CARL-on-routing-line only
event_window: open | closed           # default closed; set 'open' during BURST_WINDOW state per EVENT_WINDOW_STATE.md
---
```

**Optional/conditional fields** (WALTER adds these at dispatch time, not drafting):
```yaml
dispatched: 2026-MM-DDTHH:MM:SSZ      # added when dispatched to recipient inboxes
dispatch_note: "Free text reason for trim/re-route/downgrade"
```

```
# Layer 2 — Summary (human-scannable tearline, 2-3 sentences)
What happened. Why it matters. What the receiving agent should consider.
```

```
# Layer 3 — Body (full detail, read on demand)
Source material, data, cross-references, context, WALTER's analysis.
```

**Push notification format** (for FLASH/IMMEDIATE — 200 words max):
```
Signal: SIG-W-YYYYMMDD-NNN
Precedence: [LEVEL]
Pre-arrival context: [What happened + so what + what agent should do]
Full signal: /BOARD/SIG-W-YYYYMMDD-NNN.md
```

---

## PHASE 3.5: DELIVERY (write recipient handoffs)

> 🔴 **GATE THIS PHASE ON THE ACTIONABILITY TEST FIRST (BOARD_CONSUMPTION_SPEC §3.5.3, v0.11, Will-directed 2026-07-25).** Before choosing the note lane over the dispatch lane, ask: ***"if the recipient never opens this, could they later take a decision they would have taken differently?"*** **If yes — or if you are unsure — it is a SIGNAL: dispatch it and run this phase in full.** **NOTES ARE NON-ACTIONABLE CONTEXT ONLY** (enriching mechanism/precedent · explicitly-labelled unverified pointers · courtesy cross-refs · internal-inconsistency breadcrumbs) and never enter Phase 3 or 3.5. **Dispatch even when the item fails the Novelty gate as news:** a correction to a prior signal whose consequence changes an action · anything touching a registered threshold / falsification trigger / gate / pre-registered prediction (including exit-proximity) · anything switching a watch on or off, or re-pointing one · a dated catalyst the recipient does not already carry · a refutation of a figure the recipient is using. **The asymmetry is deliberate:** an over-dispatched context item costs one BOARD row and a little noise; an under-dispatched actionable item is invisible, untracked, and discovered only once the decision has gone the other way. *Worked example: the 7/24 "the FHA/VA KILL rests on sector averages" caveat went out as a NOTE, was decision-changing (REGINALD was re-pointing a live watch on four banks), and was re-issued as `SIG-W-20260724-007` at Will's direction. Under this gate it dispatches at the outset.*


Added v0.14 per "WALTER Routing v2" packet (Will + PROME + ORC, 2026-06-17). Canonical spec: `design/BOARD_CONSUMPTION_SPEC.md` v0.5 §3–§4. Runs AFTER the BOARD signal file + INDEX row + `route_log` append, for every dispatch (all precedence levels). **"In BOARD" ≠ "received"** — this step makes delivery real.

```
For each recipient on the routing line (action + each info):
  1. Create AGENTS/{RECIPIENT}/inbox/WALTER/  if missing.
  2. WRITE (never edit) AGENTS/{RECIPIENT}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md
     using the handoff template (BOARD_CONSUMPTION_SPEC §3.2):
       header (BOARD pointer / Priority / Role / From / Date) +
       Kernel / Why-you-got-this / Requested-action / Confidence-caveats / Cross-refs.
     One file per recipient. WALTER only CREATES here — recipient moves to
     processed/ on consume → collision-safe even if recipient is active.
  3. APPEND one row per recipient to AGENTS/WALTER/routed/delivery_log.tsv
     (one row per signal × recipient): timestamp_routed / signal_id / recipient /
     role / recipient_platform / precedence / handoff_path / written_state / notes.
     written_state = WRITTEN until committed, COMMITTED after. WALTER records up to
     COMMITTED only — on-origin/delivered state is git-derived by walter_doctor.
```

**Delivered — single-machine (BOARD_CONSUMPTION_SPEC §3.3, v0.6):**
- **Every recipient is a CC session** (OpenClaw cut 2026-06-26): delivered = handoff committed **AND** pushed/on-origin. Written-but-unpushed is NOT delivered.
- **FLASH/IMMEDIATE:** if sync is pending, the FLASH→Telegram/Will path is the never-invisible fallback; WALTER may run the §3.4 clean-tree scoped-push via the `safe-push.sh` ff-gate (0g). **PRIORITY/ROUTINE:** commit local, mark `written_not_delivered_pending_push`, surface in `walter_doctor` + closeout until a sync window (or push-train) pushes it.

> 🔴 **BEFORE WRITING THE RECIPIENT LIST — THE TERRY GATE (v0.32, 2026-08-07; canonical BOARD_CONSUMPTION_SPEC §3.5.5 / ROUTING_TABLE v0.24; Will-CONFIRMED in-session).** **TERRY is NEVER on `info:`. Delete it from any `info:` line you were about to write.** TERRY goes on `action:` **only** if one of three tests is met: **T-1** the signal names, or bears directly on the level of, a registered TERRY instrument (live/staged `setup_id`, its underlying ticker, a card gate / kill line / invalidation / harvest level, a numbered `RISK_RULES` rule, a load-bearing `SIGNALS.tsv` row) · **T-2** it corrects/retracts/retires **a number or level any TERRY surface cites**, named or not · **T-3** it is a non-price event landing **while the market is closed**, on an underlying TERRY holds or has staged. Apply §3.5.3's wording — **fires / falsifies / re-points, never "is relevant to."** Positioning colour, war-theater signals with no TERRY instrument attached, and "relevant to sizing" all fail. **🆕 TOKEN DECLARATION (v0.35 / SPEC v0.19 §3.5.5, 2026-08-20): a QUALIFYING `action: TERRY` row BEGINS its `delivery_log` `notes` cell with its test token — `T-1`, `T-2` or `T-3` — optionally followed by a reason. Absence of a valid leading token IS an override by definition** (inverted-token: typos over-report and the clause fires early, which is the safe direction). **Sending a non-qualifying item anyway is an OVERRIDE and is allowed** — prefix that row's `notes` cell with **`TERRY-OVERRIDE`** + a one-line reason (human-readable; no longer load-bearing — the machine reads the absent token), **and report it to TERRY — n=1 reporting is mandatory, not just logging.** Counted per the §3.5.5 clause TERRY ratified 8/7: **ratio ≤10%, denominator trailing 90d, activation n≥10 in the window; a breach means READ THE OVERRIDE LOG, never auto-widen T-1/T-2/T-3.** *(Do not generalise this to other recipients: it is a desk-scoped rule, not the fleet-wide ownership extension, which is unratified.)*

**Scope:** WALTER writes only `/BOARD/`, `AGENTS/WALTER/`, `AGENTS/{RECIPIENT}/inbox/WALTER/`. Never touches recipient STATUS/CLAUDE/MEMORY/board_log/processed. Pathspec commits only.

**Run mode:** Full WALTER only (Quick WALTER **RETIRED 2026-06-26**, cutover 0d). The Phase 2.8 deep-research flag stays a Full-WALTER discretionary call. Canonical mode definition in CLAUDE.md SPAWN PROTOCOL.

---

## QUALITY CHECKS (Before finalizing)

**ADViCE** (from trading desk morning calls):
- ☐ **Conclusion-oriented** — key fact in first sentence?
- ☐ **Differentiated** — what's NEW vs what we already knew?
- ☐ **Validated** — source cited, confidence language applied?
- ☐ **Easy to consume** — numbers with context (direction + threshold + comparison), no jargon?

**Editorial discipline** (from newsroom):
- ☐ Don't prescribe the fix — identify the conflict, let the agent decide
- ☐ Every number has context ("$977M — 5x prior record since 2010")
- ☐ Would this surprise someone who already knows the current network status? If no → don't route
- ☐ Immutable once written — supersede with new signal, never edit

**Breaking news sequence** (if story is developing):
1. Alert (now): minimum viable signal, flagged as unconfirmed
2. Update (when corroborated): upgrade confidence, expand detail
3. Writethru (when complete): supersedes all prior versions

---

## COP UPDATE DECISION

After processing all signals in a session:
- Did any FLASH/IMMEDIATE signals fire? → Update COP ⚡ section
- Did any convergence events emerge? → Update Convergence section
- Did any domain status change? → Mark with △, update domain entry
- Did any new counter-signals appear? → Update Counter-Signals section
- Did any catalysts resolve or appear? → Update Catalysts section
- Is any domain's data now >48h old? → Add [stale] flag

If nothing changed: update timestamp only. A COP with just a new timestamp honestly says "I checked and nothing moved."

---

## WHAT NOT TO DO

- Don't route signals just because they're interesting — route because they CHANGE something
- Don't write a 500-word signal when 50 words convey the same information
- Don't promote single-source claims to IMMEDIATE without corroboration
- Don't filter counter-signals harder than confirming signals (confirmation bias)
- Don't process COP updates last in a session — do it first, when judgment is freshest
- Don't edit published signals — write a new one that supersedes

---

## WORKED EXAMPLE: CPI March + UMich April Preliminary (2026-04-10)

This example walks the checklist top-to-bottom on a real input. It shows what each step LOOKS LIKE in practice and validates that the checklist produces a clean routing decision.

### Raw Input

- **Source:** Will Telegram message ("CIP and UM sentiment - can you pull that data up?") → fetched CPI from FRED via FORGE/tools/market-data, fetched UMich Apr preliminary via WebSearch
- **Time:** 2026-04-10 ~17:30 UTC
- **Content:** CPI March: headline +0.86% MoM / +3.28% YoY, core +0.21% MoM / +2.61% YoY. UMich April preliminary 47.6 (record low, below 50 Biden trough). 1Y inflation expectations 4.8% (from 3.8%), 5-10Y expectations 3.4% (from 3.2%). 98% of UMich interviews conducted before Iran ceasefire announcement.

### PHASE 1: Intake — Kill or Keep?

Walked per FILTER_SPEC v0.2 unified model (System-Critical bypass → Novelty → Relevance → Credibility).

| Check | Result | Reason |
|-------|--------|--------|
| **0. System-Critical bypass?** | NO | Not portfolio-damaging, no stop-loss adjacent, no safety net trigger, no falsification rule firing. Continue through normal gates. |
| **1. Novelty (hard kill)?** | PASS | Both prints released today, fresh information, not in any agent's STATUS as of this morning. |
| **2. Relevance (hard kill)?** | PASS | Touches LABOR_DOWNSTREAM (CARL), market structure (HENRY), credit (LIQUID), thesis (RED), Japan (SAM via Fed reaction). Multi-domain. |
| **3. Credibility (soft modifier)?** | HIGH → conf 0.95+ base | BLS official release (golden source) + University of Michigan official Surveys of Consumers (second golden source) = TWO independent authoritative sources. Maps to 0.90–1.0 band. |

**Outcome:** SURVIVED intake. Confidence 0.97 (after +0.05 corroboration adjustment, capped at 0.97 to reflect UMich pre-ceasefire interview caveat). Proceed to classify.

**Note on the new model vs the old one:** Under v0.1's "fail-all-three" logic this would have passed trivially (all three questions gated pass). Under v0.2's AND-logic it still passes because Novelty AND Relevance both pass cleanly. The difference would matter on edge cases like a Bloomberg restating of a CPI print we'd already routed (fails Novelty as duplicate → now dies; under v0.1 would have passed on Credibility alone) or an anonymous Twitter post about WAL capital-raise rumors (passes Novelty + Relevance + Low Credibility = routes at ~0.35 confidence instead of dying outright).

### PHASE 2: Classify

**Precedence:** IMMEDIATE
- Threshold breach (UMich record low)
- Confirmed catalyst (scheduled CPI release)
- Multiple thesis components affected
- Action window: now

**Confidence:** `confidence: 0.97` / `confidence_language: confirmed`
- BLS official release for CPI (golden source) → 0.95+ baseline
- University of Michigan official Surveys of Consumers for sentiment (second golden source) → +0.05 corroboration adjustment
- Two-source rule satisfied via two independent authoritative releases corroborating the stagflation reading
- Lands at 0.97 → snaps to "confirmed" tier per SIGNAL_FORMAT_SPEC mapping (0.90–1.0 range)
- The 0.03 short of 1.0 captures the UMich pre-ceasefire interview caveat

**Conflict zone:** 🟡 Yellow → 🔴 Red mixed
- 🟢 Confirms CARL's consumption stress quarter framework
- 🟢 Confirms HENRY's Fed-cuts-pushed-to-H2-2027 thesis
- 🔴 Strengthens RED's Stagflation Spiral hypothesis (currently 41% — likely needs upward revision)
- 🟡 Tension: ceasefire announcement post-survey may cause partial recovery in next print
- Net: 🔴 because the dominant story is stagflation lock-in, with the ceasefire caveat as secondary

**Superevent check:** YES — bundle.
- CPI and UMich are TWO independent inputs pointing at ONE underlying cause (stagflation pressures + Fed paralysis)
- Both released same day, same window
- Routing them as separate signals would fragment the story
- Decision: ONE signal as superevent, citing both data sources in body

### PHASE 3: Output

**Disposition:** PUSHED
- Precedence is IMMEDIATE → push to recipient inboxes + Telegram ping to Will

**Routing decision:**
- **Action recipient:** CARL (consumer/consumption stress is the first-order domain — UMich at record low + headline CPI hot is squarely his lane)
- **Info recipients:** HENRY (Fed reaction function), RED (stagflation hypothesis re-weight), LIQUID (HY OAS implications), SAM (USD/JPY via Fed locked)
- **Group:** THESIS_CORE (CARL is a member; HENRY/RED/LIQUID/SAM listed individually as info — this is normal when info recipients span multiple groups)

**Signal file:** SIG-W-20260410-001-cpi-umich-stagflation.md (drafted, currently in WALTER/outbox/ awaiting approval)

**Push notification format** (when dispatched):
```
Signal: SIG-W-20260410-001
Precedence: IMMEDIATE
Pre-arrival context: Stagflation signature locked in.
  CPI Mar headline +0.86% MoM (gas/food pass-through), core contained +0.21%.
  UMich Apr prelim 47.6 RECORD LOW. 1Y inflation exp jumped to 4.8%, long-run
  expectations un-anchoring at 3.4% (Fed red line).
  Caveat: 98% of UMich interviews preceded ceasefire — final print may show partial recovery.
  CARL: update consumption stress framework. Others: see relevance section.
Full signal: /BOARD/SIG-W-20260410-001-cpi-umich-stagflation.md
```

### Quality Checks (ADViCE)

- ☑ **Conclusion-oriented:** First sentence states the conclusion ("stagflation signature locked")
- ☑ **Differentiated:** Calls out what's NEW (UMich record low, expectations jumping) — not just what persists
- ☑ **Validated:** Sources cited (BLS, U Michigan SCA, Axios, Spectrum), confidence language used (Confirmed)
- ☑ **Easy to consume:** All numbers in table form with context (current vs prior, YoY comparison, threshold reference)

### Editorial Discipline

- ☑ Doesn't prescribe the fix — describes the data and lets agents decide
- ☑ Every number has context (vs prior month, vs year ago, vs threshold)
- ☑ Surprise check: would this surprise an agent who already knows current network status? YES — UMich record low + un-anchoring expectations are NEW data
- ☑ Will be immutable once dispatched

### Anti-patterns I Avoided

- Did NOT route as two separate signals (CPI vs UMich) — caught by superevent check
- Did NOT draft a 500-word essay — kept Signal+Data ≤200 words per spec
- Did NOT skip the safety net check — flagged convergence (2+ agents on stagflation theme already)
- Did NOT default to "everyone gets a copy" — selected recipients based on first-order domain impact

### Initial Mistake (Recovered)

I initially drafted a SECOND signal (SIG-W-20260410-002, CPI-only with HENRY action) thinking the spec required separate signals per data release. Will challenged the benefit. On re-read of SIGNAL_FORMAT_SPEC, I realized "one file per action recipient" means **one file per inbox during dispatch**, not "one signal per data release." The correct model is ONE master signal that becomes multiple files (one per recipient inbox) at dispatch time. SIG-002 was duplication and is being deleted.

**Lesson:** When two data points land same day on same theme → bundle as superevent. When the ROUTING produces multiple recipients → that's the dispatch step creating multiple files, not the drafting step creating multiple signals.

### Gaps This Example Exposed

1. **~~Header confidence field divergence~~** ✅ RESOLVED in v0.3. SIGNAL_FORMAT_SPEC.md defines TWO bound fields: `confidence` (numerical 0.0–1.0) AND `confidence_language` (confirmed/reports/assessed/unconfirmed), bound by a mapping table.

2. **~~No routing log~~** ✅ RESOLVED Apr 11. `AGENTS/WALTER/routed/route_log.tsv` created per FILTER_SPEC schema. Today's dispatches backfilled. Going forward every dispatch appends a row.

3. **No capability/load check:** I picked CARL as action recipient without verifying his current load. CARL was updated today (not stale), but if he had been overloaded I should have considered re-routing or downgrading. **Partially addressed Apr 11** via Backup column in ROUTING_TABLE v0.2 with promotion semantics (use backup when primary stale >5d, in MINIMIZE, or spawning sub-agents). Still open: automated load check at routing time. (Open.)

4. **~~No backup recipient defined~~** ✅ RESOLVED Apr 11. ROUTING_TABLE v0.2 added a Backup column across all rows with explicit promotion semantics. CARL backup is HENRY for most domains.

5. **~~Header schema divergence between FORMAT_SPEC and CHECKLIST~~** ✅ RESOLVED Apr 11 (this file, v0.4). CHECKLIST Phase 3 header example now shows the full FORMAT_SPEC schema. `conflict_zone` clarified as an analytical step (informs Relevance prose) not a header field, because it's recipient-dependent. Header-level machine filter for thesis-vs-counter uses `signal_type` (counter-evidence vs thesis-confirmation) which is already in FORMAT_SPEC. The canonical-source rule is documented at the top of this file.

6. **~~Filter model divergence~~** ✅ RESOLVED Apr 11 (Gap B). FILTER_SPEC v0.2 and this CHECKLIST v0.5 now share a single unified filter model: System-Critical pre-gate bypass → Novelty (hard kill) → Relevance (hard kill) → Credibility (soft, confidence modifier with 0.30 floor). AND-logic on the hard gates. Model is versioned v1 and **provisional** — scheduled review after 10+ signals pass through or 30 days from Apr 11, whichever first.

---

*Operational checklist — derived from 10 research prompts | v0.1: April 7, 2026 | v0.2: April 10, 2026 (worked example added) | v0.3: April 10, 2026 (confidence model reconciled) | v0.4: April 11, 2026 (header schema reconciled; conflict_zone clarified) | v0.5: April 11, 2026 (Phase 1 reconciled with FILTER_SPEC v0.2 unified filter model — Gap B resolved) | v0.6: April 11, 2026 PM (canonical Domain Vocabulary referenced — Gap C resolved) | v0.7: April 20, 2026 (Filter v2 Segment B — Phase 1b same-theme combine check added between intake and classify, references FORMAT_SPEC v0.6 Multi-Origin Signals) | v0.8: April 20, 2026 (Filter v2 Segment C — Phase 1.5 verify-research framing audit codified with 4 trigger patterns, spawn discipline, and 4-verdict handling) | v0.9: May 5, 2026 (Cluster assignment step added to Phase 2 per CLUSTER_TAXONOMY.md v0.1 — every dispatched signal lands in exactly one primary cluster, header gets `cluster:` field, INDEX section is determined by cluster) | v0.10: May 6, 2026 PM (Phase 2 routing-augmentation steps 5-7 added per RED ↔ WALTER LIAISON + JOINT_PROPOSAL_2026-05-06_red_walter §3 — step 5 cluster_mediating auto-cc to RED with interim prose-tag discipline pre-v0.8, step 6 CORRECTED-FRAMING auto-cc to RED, step 7 FALSIFICATION_TRIGGERS auto-fire scan with sustain-window suppression and parallel ledger at AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv preserving Critical Rule #2) | v0.11: May 8, 2026 (Phase 2 step 4.5 v0.8 routing-augmentation tagging added per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a + §2d.5 — fills cluster_secondary / signal_role / consumer_transmission / consumer_lens / event_window v0.8 optional fields at dispatch time; step 5 updated to reference `signal_role: cluster_mediating` canonical form retiring v0.7 prose-tag interim discipline; Phase 3 header example refreshed; Will sign-off 2026-05-08) | v0.12: June 6, 2026 (5-item batch: passive at-boot scan / forecaster-miss pattern / Phase 2.7 composite-bifurcation tagging / per-session-vs-day-aggregate threshold / 3-metric framework-agreement; Will sign-off 2026-06-06) | v0.13: June 10, 2026 (Phase 2.6 paired same-channel dispatch — promoted at pre-registered 3rd instance; Will sign-off 2026-06-10) | v0.14: June 17, 2026 (Phase 3.5 DELIVERY step — per-recipient `inbox/WALTER/` handoff files + `delivery_log.tsv` on every dispatch; platform-nuanced delivered; canonical BOARD_CONSUMPTION_SPEC v0.2; "WALTER Routing v2" packet, Will + PROME + ORC approved-in-principle 2026-06-17) | v0.18: June 19, 2026 (Phase 2.8 DEEP-RESEARCH CANDIDATE SCAN — T1–T5 triggers + mandatory materiality gate + ledger `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` + `walter_doctor` `deep_research_pending_overdue` check; zero research-execution load, Will-decides/WALTER-never-runs; Will sign-off 2026-06-19) | v0.19: June 19, 2026 (Phase 2.8b returning-deliverable handling — one `research-output` signal default [verbatim embed + per-recipient delta wrapper, no verify-spawn] + ledger close + split test S1–S4 for child-signal carve-out; first instance + worked example SIG-W-20260619-008; Will sign-off 2026-06-19) | v0.20: June 20, 2026 (DEWEY-executor + inbox/DEWEY consumption wiring [boot step 7d + processed/ git-mv NEW→ROUTED→PROCESSED lifecycle] + `executor` ledger column [11→12-col]; DEWEY revival Phase 2; Will sign-off 2026-06-20) | v0.21: June 26, 2026 (single-machine collapse — platform-nuanced `delivered` retired [uniform committed+on-origin] / Quick-WALTER retired) | v0.22: June 27, 2026 (Phase 1.5 investigation-routing discriminator + paywalled-pointer principle — a paywalled/headline posting is an investigation POINTER not route-or-kill; research defaults to DEWEY-assignment, WALTER verify-spawn only for blocking same-session framing-checks; Will-directed) | v0.23: July 3, 2026 (confidence_note Phase-2 guidance — Filter v2 Segment D shipped) | v0.24: July 4, 2026 (pull-complete recipient exemption — Phase 3.5 delivery skip for complete-pull agents, CARL only) | v0.25: July 4, 2026 (FILTER v3 codifications — image-batch file-id/content dedup [Phase 1b] + distressed-CRE figure-class verify [Phase 1.5]; Will greenlight)*
