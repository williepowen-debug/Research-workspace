# BOND outbox delivery audit — 2026-09-28 13:30 ET (Will-directed housekeeping)

**Rule applied (BOND CLAUDE.md §MAIL):** a packet moves to `outbox/delivered/` only after its CONTENT is verified at the recipient. That means one of: a copy in their inbox under any filename (the fleet often renamed `to-X` to `from-BOND`), git history of such a copy, or the recipient's own record carrying the packet's substance. A missing filename was never read as non-delivery.

**Result: 47 packets → 33 DELIVERED (verified; 2 were byte-identical duplicates of copies already in `delivered/`, so the outbox copies went to trash) · 8 RETIRED unverified (>60 days, no live reference) · 6 KEPT in outbox (unverified, <60 days).** Method: three scans (name / KB-id / content per recipient tree; distinctive-phrase context; same-date from-BOND inbox files incl. git history), then targeted reads.

## Verified delivered — now in `outbox/delivered/`

| Packet | Evidence at recipient |
|---|---|
| `2026-05-20_to-PROME_20Y-post-auction.md` | PROME/archive/CC_HANDOFF_2026-05-pre-22.md cites "20Y post-auction" / "BOND 5/20" (knowledge) |
| `2026-07-09_to-PROME_bnd11-30y-reopen-grade.md` | filename cited in PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-07-10.md |
| `2026-07-28_to-HENRY-NEXUS-PROME_prereg-challenged-by-my-own-backtest-pre-print.md` | copies in HENRY, NEXUS and PROME inbox/processed as 2026-07-28_from-BOND_prereg-challenged-by-my-own-backtest-pre-print.md |
| `2026-07-28_to-LIQUID-PROME_fr2004-gap-was-self-inflicted-and-the-dealer-record-has-unwound.md` | LIQUID inbox/processed/2026-07-28_from-BOND_fr2004-gap-was-self-inflicted-...; PROME got the related same-day 2026-07-28_from-BOND_fr2004-gap-closed-escalation-can-be-closed.md (PROME leg PROBABLE) |
| `2026-08-20_to-SAM_RETRACTION-the-below-DM-median-read-I-sent-you-this-morning-is-a-one-week-artifact.md` | SAM inbox 2026-08-20_from-BOND_RETRACTION-...; an IDENTICAL copy was already in delivered/ — outbox duplicate trashed 9/28 |
| `2026-08-20_to-SAM_bar-DECLINED-with-two-named-blockers-plus-common-factor-answered.md` | SAM holds same-day 2026-08-20_from-BOND_BAR-RULED-both-sides-... and cites all 3 KB-BND ids the packet carried (knowledge; filename differs) |
| `2026-08-20_to-TERRY_60DTE-review-on-004-is-19-days-overdue-and-sb0607-covers-half-its-remaining-life.md` | TERRY inbox/processed/2026-08-20_from-BOND_60DTE-review-...; IDENTICAL copy already in delivered/ — outbox duplicate trashed 9/28 |
| `2026-08-23_to-MIDAS_8-19-attribution-re-derived-independently-reproduces-but-the-retractions-corollary-is-inverted.md` | MIDAS inbox/processed/2026-08-23_from-BOND_8-19-re-derivation_LATE-FILED-... |
| `2026-08-23_to-PROME_re-derivation-verdicts-plus-two-gated-items-RETURNED-not-actioned.md` | PROME/DOCKET.tsv L226 records "RETURNED by BOND 2026-08-23" (knowledge) |
| `2026-08-23_to-REGINALD_RULED-pnc-headroom-does-not-trip-the-depletion-leg-and-the-leg-is-a-family-not-a-threshold.md` | REGINALD STATUS: "Pittsburgh +111% = PNC alone ... not a trip of BOND's ungradeable VX-BND-18 leg" = the ruling's substance (knowledge) |
| `2026-08-27_to-HENRY_sb0607-classification-ANSWERED-the-butterfly-not-the-peak-tenor.md` | git history: AGENTS/HENRY/inbox/2026-08-27_to-HENRY_sb0607-... |
| `2026-08-27_to-LIQUID_CONCUR-on-your-grade-date-trap-plus-KB-BND-092-closed.md` | git history: AGENTS/LIQUID/inbox/2026-08-27_to-LIQUID_CONCUR-... |
| `2026-08-27_to-PROME_MATRIX-V2-ADOPTED-plus-one-WILL-GATED-question-I-did-not-answer-myself.md` | PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md ruled on "BOND's ask, restated in its 8/27 doorbell reply" (outcome) |
| `2026-08-27_to-SAM_FRED-reaches-my-box-and-CANNOT-give-you-the-3m-JPY-leg.md` | git history: AGENTS/SAM/inbox/2026-08-27_to-SAM_FRED-... |
| `2026-08-27_to-SAM_the-four-legs-are-each-fine-but-two-share-a-release-and-a-blind-spot-so-the-convergence-claim-overreaches.md` | SAM inbox/processed copy + cited in SAM research/outputs |
| `2026-09-02_to-MIDAS_BND-21-TRUE-the-9-1-real-impulse-was-ZERO-so-your-positioning-candidate-carries-gold.md` | MIDAS inbox copy (from-BOND name) |
| `2026-09-02_to-PROME_inbox-drained-matrix-v2-and-ft11-disposition.md` | PROME inbox/processed copy (from-BOND name) |
| `2026-09-02_to-RED_FT-11-v1.1-design-call-all-on-menu-minus-4bp-FLOW-alternative-second-precondition-path-ADOPTED.md` | RED inbox copy (from-BOND name) |
| `2026-09-02_to-SAM_your-correction-is-consumed-and-your-ask-is-done-the-horizon-now-travels-on-the-summary-line.md` | SAM inbox copy (from-BOND name) |
| `2026-09-04_to-LABOR_retraction-consumed-BOND-surfaces-clean-and-one-contradiction-in-the-Fed-path-numbers-you-should-know-about.md` | LABOR inbox copy |
| `2026-09-04_to-ORACLE_wrong-contract-accepted-and-corrected-by-pattern-plus-the-memory-should-be-yours.md` | git history: ORACLE inbox copy |
| `2026-09-04_to-PROME_FLAG-fleet-auto-memory-index-at-75pct-flow-rule-trip-line.md` | git history: PROME inbox copy |
| `2026-09-04_to-PROME_WQ-157-leg-1-rec-RETAIN-through-the-refunding-then-PAIR-plus-buyback-classification-confirmed-pre-registered.md` | PROME inbox/processed copy + cited in PROME/proposals |
| `2026-09-04_to-RED_FT-11-v1.1-acknowledged-same-letter-and-the-non-strict-reading-does-NOT-change-my-call.md` | RED inbox/processed copy |
| `2026-09-04_to-SAM_Norway-GPFG-proposes-a-phased-18B-JGB-bid-JPY-index-share-5-to-8pct.md` | SAM inbox/processed copy |
| `2026-09-04_to-ZHAO_alecta-nordic-pension-UST-divestment-is-a-JANUARY-story-and-it-lands-in-your-net-BUYING-bucket.md` | ZHAO inbox + processed copy |
| `2026-09-04b_to-ORACLE_settled-it-is-NEITHER-A-nor-B-my-relay-named-no-venue.md` | ORACLE inbox/processed copy |
| `2026-09-04b_to-ZHAO_CORRECTION-there-IS-a-live-item-Norway-GPFG-80B-out-of-USTs-and-the-dollar-does-not-leave.md` | ZHAO inbox/processed copy |
| `2026-09-09_to-PROME_L17-answered-refunding-legs-1-2-clean-BND-24-TRUE-buyback-date-corrected-docket-adds.md` | PROME inbox/processed copy (from-BOND name) |
| `2026-09-09_to-RED_F2-does-not-exist-yet-the-first-long-end-buyback-op-is-9-10-not-9-9.md` | RED inbox/processed copy (from-BOND name) |
| `2026-09-09_to-TERRY_buyback-attribution-starts-9-10-not-9-9-and-the-refunding-legs-1-2-are-clean.md` | TERRY inbox/processed copy (from-BOND name) |
| `2026-09-10_to-WALTER_10y-level-graded-corroborated-within-1-4bp-AND-your-buyback-premise-is-one-step-stale-the-op-already-ran.md` | WALTER inbox/processed copy |
| `2026-09-17_to-PROME_tips-preprint-sep-grade-f2-carrier.md` | PROME inbox copy (from-BOND name) |

## Retired to `archive/outbox_unverified/` — DELIVERY NOT VERIFIED

All are >60 days old, not boot-read, and no live BOND doc references them (root CLAUDE.md retirement rule). **Their presence in the archive is NOT a delivery claim.**

- `2026-05-19_to-HENRY_credit_duration_decoupling.md`
- `2026-06-05_to-PROME_longend-deescalation.md`
- `2026-07-18_to-PROME_fed-path-map-40Y-JGB-prereg.md`
- `2026-07-18_to-PROME_label-check-eu-reconcile-weld.md`
- `2026-07-23_to-PROME_nexus-brief-refresh-hardened-label.md`
- `2026-07-28_to-HENRY_falsifier-was-mine-and-misspecified-plus-you-over-retracted.md`
- `2026-07-28_to-NEXUS_727-grade-delivered-holding-with-a-marker.md`
- `2026-07-28_to-PROME_7y-grade.md`

## Kept in `outbox/` — unverified, under 60 days

| Packet | Note |
|---|---|
| `2026-08-23_to-SAM_mof-date-adopted-8-28-leading-leg-and-your-defect-class-is-going-in-my-KB.md` | SAM answered BOND's 8/18 MOF-date ask on 8/23; no trace SAM received BOND's 8/23 reply. Content likely superseded. |
| `2026-08-23_to-VIOLET_RULED-retiring-the-hyg-skew-clause-your-option-3-and-your-denominator-diagnosis-is-right.md` | no trace at VIOLET; the HYG-skew clause retirement is recorded on BOND surfaces only. |
| `2026-08-23_to-WALTER_your-since-2007-impeachment-is-inverted-your-own-number-proves-the-claim.md` | no trace of the since-2007 impeachment reply at WALTER. |
| `2026-08-27_to-LIQUID_your-B2-branch-FIRED-KB-BND-092-closes-REFUTED-AND-MOOT.md` | KB ids cited at LIQUID but no copy; LIQUID did receive the same-day CONCUR packet. |
| `2026-08-27_to-PROME-MIDAS-RED_doorbell-consumed-your-DFII10-path-caught-a-live-wrong-direction-on-my-surface.md` | no copy at any of the three recipients; KB ids partially cited. |
| `2026-08-27_to-PROME_kill-scope-ENCODED-plus-three-uses-the-ruling-does-not-reach.md` | 🔴 POSSIBLY STILL LIVE: flags three uses of "composition failure" the 8/27 ruling does not reach (incl. the TLT-put ADD re-arm and the LIQUID outbound routing trigger). No PROME record found; BOND still runs those on the OLD definition. Re-send, or Will decides. |

**Only the 8/27 kill-scope packet may still carry a live question; the rest are superseded replies or FYIs.** Re-sending is a separate decision and was not done here.
