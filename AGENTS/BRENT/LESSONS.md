# BRENT LESSONS.md

Read at boot. Current rules below supersede the mixed current/history presentation under Will’s approved cleanup, 2026-09-08. Stable lesson IDs and machine assertions are retained. Review date means text/index reconciliation, never refreshed market evidence. Full original narratives, failed hypotheses and dated examples: [unaltered history](archive/2026-09-08_cleanup/LESSONS.md).

Update this prose and `workbook/LESSONS_INDEX.tsv` in the same commit. Run `scripts/lessons_check.py --prose` after either changes; run `--concept` before and `--spec` after gate work. Read the complete [trade decision path](TRADE.md#decision-read-paths) before any trade-relevant decision. Lessons are not substitute execution instructions.

1. **Agent data can be hallucinated — verify against primaries.** Verify data against primary sources before citing it, including claims supplied by other agents and your own prior work. Independent pulls of one series are still one measurement lineage. *(Reconciled 2026-09-08; L01.)*

2. **Source tags mandatory ([CONF]/[EST] + source + date).** Attach source, observation date and CONF/EST classification to every data point. A retrieval date does not replace an observation date. *(Reconciled 2026-09-08; L02.)*

3. **Don't maintain stale copies — one source of truth per metric.** Keep one owner per metric. Reference HAWK for military operations, HENRY for VIX and LIQUID for HY OAS; do not maintain stale copies. *(Reconciled 2026-09-08; L03.)*

4. **Write synthesis .md for major data releases.** For major releases, write a synthesis explaining the five consequential findings, with sources, rather than depositing raw data alone. *(Reconciled 2026-09-08; L04.)*

5. **Oil prices are 24/7 — STATUS prices go stale fast, and a vendor DAILY BAR is MUTABLE until the session closes.** Pull current prices before a price update. Stored STATUS prices are dated context. Name the contract and distinguish live print, vendor daily bar and authenticated settlement. **EXTENDED 2026-09-11 (supersedes: none):** those three classes are not merely different, the middle one is *unstable* — a daily bar read before the session closes is an IN-PROGRESS bar and the vendor restates it afterwards. Never grade a settle-specified threshold off a bar captured intraday, **including a bar you yourself labelled 'still forming' in the same breath** — that is the measured failure, not a hypothetical. Also never difference two legs of one composite across different capture times: mixing an 18:0x crude quote with 00:00 product quotes produces a number that is arithmetically invalid rather than merely stale. When margin is thinner than the spread between vendor vintages, the honest verdict is NOT MEASURABLE, not a grade. *(Reconciled 2026-09-08; extended 2026-09-11; L05.)*

6. **Crack spreads tell the real story; crude price alone is incomplete.** Read product cracks alongside crude to locate refinery-margin stress. Name each contract and align units and observation times before computing spreads. *(Reconciled 2026-09-08; L06.)*

7. **Two-phase thesis is the core.** Assess evidence against the two-phase framework: supply shock and its transmission, then demand destruction or premium unwind. The framework remains falsifiable; an observation does not establish a phase transition by itself. *(Reconciled 2026-09-08; L07.)*

8. **Storage data has reporting lag.** Label inventory reporting lag and distinguish EIA surveys from Gulf-storage estimates. Publication time is not the date barrels were measured. *(Reconciled 2026-09-08; L08.)*

9. **EIA 'product supplied' MISLEADS in weeks 1-4 of a shock (stockpiling mask).** Do not infer early demand destruction from EIA product supplied alone in shock weeks 1–4: wholesale stockpiling can mask final consumption. Check aviation cuts and ATA tonnage as leading evidence. *(Reconciled 2026-09-08; L09.)*

10. **OPEC+ paper quotas != physical production.** OPEC announcements change paper quotas, not automatically production. Verify actual output and deliverable spare capacity independently. Historical quota gaps are examples, not current readings. *(Reconciled 2026-09-08; L10.)*

11. **Announcement entry precedes physical delivery; approved conditions still govern.** Announcement repricing and physical delivery occur at different times. Off-ramp entry follows the approved signature and paired T/C rules, not a wait for barrels. The old “80%” statement is a dated analogue claim, not a guaranteed fraction of any future move. *(Reconciled 2026-09-08; L11.)*

12. **Demand destruction timeline in 2026 is LONGER than historical analogs (EVs).** EV penetration may lengthen demand adjustment by removing price-sensitive marginal drivers. The original 28–32+ week forecast is historical thesis evidence, not an evergreen clock; test it against current demand observations. *(Reconciled 2026-09-08; L12.)*

13. **Oil shock macro damage is SEQUENTIAL, not simultaneous.** Oil-shock transmission is sequential: consumer costs, jobs/output, demand, oil prices, producer credit and bank exposure need not turn together. Align evidence and any proposal with the observed stage. *(Reconciled 2026-09-08; L13.)*

14. **1986 = the canonical glut/bank-crisis analog (geographic concentration).** Use the 1986 comparison to investigate geographic concentration in banks, rather than infer a systemic crisis from energy exposure alone. Historical counts and costs remain in the dated evidence. *(Reconciled 2026-09-08; L14.)*

15. **Bear put SPREADS not naked puts at high IV; 60-90 DTE / 10-15% OTM / 3:1.** Use spreads rather than naked options for the high-IV structural premise. Scope tenor to the move: slow demand-collapse short 60–90 DTE; off-ramp 21–35 DTE with mandatory H1/H2/H3. H1 is day+9 from announcement for both tranches, superseding the old per-tranche rider. Read the complete entry and holding specs before proposing. *(Reconciled 2026-09-08; L15.)*

16. **Equity stocks LEAD physical rates — exit on announcement, not delivery.** Equity repricing can lead physical freight rates. Do not wait for delivery merely because it is easier to verify, or turn that timing lesson into automatic entry/exit authority. Approved position-specific rules and the off-ramp spec govern. *(Reconciled 2026-09-08; L16.)*

17. **The OPEC+ '5-6M bpd spare' narrative is wrong — pressure-test official figures.** Pressure-test cartel spare-capacity claims against independent production and export constraints. The original 4.35M bpd estimate and country breakdown are dated historical claims; do not quote them as newly verified capacity. *(Reconciled 2026-09-08; L17.)*

18. **Separate signature, paired tanker liveness and physical retention.** Distinguish rhetoric, signed agreement and physical reopening. Entry uses the sign-blind three-name tanker liveness composite paired with crude follow-through. T is graded once at/after 14:00 ET; the close-basis veto still governs tranche 2. Physical verification belongs to retention, but the named transit instrument was retired August 21: it cannot be executed as a live kill test. JWC delisting is prompt-only; unresolved persistence applicability is preserved in the holding spec. H1 clock is resolved, not open. *(Reconciled 2026-09-08; L18.)*

19. **A signed deal is not an operational one; reopening is NOT uniformly tanker-bearish.** Reopening need not make tanker equities fall: competing ton-mile and premium channels can move them either way. Discard sign in the approved liveness test; do not revive the superseded dispersion test. The old “rose on 2 of 2” and “blocked 2 of 2” tallies are unverified and must not be cited. The approved T/C definitions and n=0 genuine reopening caveat travel together. *(Reconciled 2026-09-08; L19.)*

20. **I hold counterparties to a standard I don't hold myself to (n=4, also points INWARD).** Apply the same primary-source and reproduction standard to your own claims as to counterparties. A correction can itself be wrong; verify the correction, not merely the original error. *(Reconciled 2026-09-08; L20.)*

21. **A threshold fails on its SPEC before it fails on the world; match each leg's window to its own response time.** Test whether a threshold can fire in its intended regime, each leg in its own response window, and the compound gate jointly conditional on the trigger state. Test the replacement before proposing it. Verify that the proxy fits the actual structure; do not inherit a vega gate for an instrument designed to offset vega. Any change in a capital gate needs its existing approval path, not quiet relaxation. *(Reconciled 2026-09-08; L21.)*

22. **A pre-registration must name an instrument that actually TRADES and a THRESHOLD THAT IS A NUMBER, and "I verified it" is itself a claim that needs running.** Pull the named instrument and confirm it prints in the decision window. Reproduce analogue baselines from dated, like-for-like observations. Verification claims require an actual run. Freeze numerical verdict boundaries and an explicit NO-VERDICT band before observing the result; adjectives are not boundaries. *(Reconciled 2026-09-08; L22.)*

23. **A continuous front-month ticker (=F) silently re-points at the contract roll — a LEVEL survives it, a DELTA or SPREAD across it is fabricated.** A continuous ticker can roll into another contract. Name the contract for every derived delta/spread; crossing a roll fabricates a same-contract move. A dated continuous level can be reported as such, but does not establish a comparable delta. *(Reconciled 2026-09-08; L23.)*

24. **A publication date is not an event date — a weekday that disagrees with its date means TWO dates are in play, and that mismatch is the detector.** Separate event date from publication date. Preserve a source weekday as a checksum when reading; omit an unchecked weekday when authoring an operative instruction. Resolve mismatches before assigning the event date. *(Reconciled 2026-09-08; L24.)*

25. **A source that HANGS is not a source that is DOWN — a WAF tarpitting your User-Agent yields TimeoutError, which reads as the publisher's outage and is actually yours.** Distinguish publisher outage from request failure. Vary user agent and inspect response identity before declaring a source unavailable. Baker Hughes follow-up September 6 found GET/HEAD and request-volume differences: GET the page, identify the dated content-disposition, fetch one workbook; HEAD can fail independently. Avoid year-stale archive decoys. A standing caveat is an untested hypothesis until re-run. *(Reconciled 2026-09-08; L25.)*

26. **A pathspec-scoped commit after git mv silently drops the half of the rename not in the pathspec - HEAD carries the file at both paths, disk looks fine.** Scope commits to your files, and include both source and destination of every rename. Inspect staged deletions after a path-scoped commit; disk looking right does not prove HEAD records the move. Never use broad git add to solve the rename problem. *(Reconciled 2026-09-08; L26.)*
