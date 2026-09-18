# September 18 progress review — CATO

## Scope and conclusion

Will requested review of PROME and agent progress since the previous report. Main inventory: **32 commits / 115 changed paths**, `0cf6d5eb2..2cb5401fa`. The previous action brief is the baseline. Two commits landed during review: BRENT proposal qualification `279ff015f` and SAM rebenchmark plan `2f674c8c4`; the SAM plan is included below. Earlier WQ-247/WQ-250 root/GATES_README changes were sampled from `1b1de7d07`, because the prior brief explicitly left them unreviewed. This is risk-selected review, not certification of every changed path or research source.

Real progress is visible: queue parsing repairs pass their suites; TERRY records the VLO partial fill without inventing account/time; BROCK distinguishes public silence from a credit-event grade and makes the counted vehicle explicit; BRENT repairs its COT gate definition and adds a vintage watch. However, SAM's oil interpretation and newly proposed benchmark need correction, and the passing control suites still miss concrete failure cases. The earlier high-priority BOND/FRED findings remain unchanged at their source files.

PROME had active uncommitted closeout, deck, ledger and FORGE changes; other agents also continued working. No pull, owner edit, external message, broker action, gate change or fleet launch. Only CATO report/probe/continuity authored. The report is ready for Will/PROME to use; it was not sent to another agent. Next step is owner disposition of findings, not automatic CATO implementation.

Evidence: [pinned offline probes](2026-09-18_1354_progress-review-probe.py), [results](2026-09-18_1354_progress-review-probe.txt). These deliberately reproduce defects at the reviewed revision; exit 0 is NOT proof of a later repair. Source functions are loaded from pinned Git revisions. Only temporary fixture trees are mutated; no live grader fetch or ledger append was performed.

## Findings requiring action

### R1 — High: SAM uses a roll-contaminated continuous price change as an economic signal

**Owner:** SAM; reconciliation with TERRY/BRENT. **Sources:** `AGENTS/SAM/NEXUS_BRIEF.md:11`; `AGENTS/SAM/STATUS.md:49,84,89`; TERRY `setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md:491–504` (all at `2cb5401fa`).

SAM says Brent fell from $106.90 on September 15 to $98.93 on September 18, −7.5%, while Petroline remained shut, and uses this as a cross-domain supply/price divergence. STATUS calls it a continuous quote and says “never compared across rolls,” while doing that comparison without establishing contract continuity. TERRY's earlier same-day resolver identifies `BZ=F` moving from November-like previous close $103.93 to December-like last $99.52, and distinguishes named months from the apparent continuous-series decline.

**Consequence:** a contract change can be interpreted as demand weakness or diminished oil stress and passed to BRENT/HAWK. SAM correctly withholds a fresh registered oil-in-yen count, so no erroneous gate firing was established. TERRY's measurement is owner evidence at an earlier timestamp, not an independent CATO market-data reproduction; it does not prove the entire three-day move was artificial or that every named month stayed up later.

**Action / closure:** reconstruct the interval on a consistent named contract (or explicitly documented adjusted series), retain observation timestamps and contract identities, and replace the −7.5% causal interpretation with the verified comparison. Until then label the direction inference unestablished. Reconcile the NEXUS brief and affected live summaries, not just the quote label.

### R2 — High: SAM's diagnostic reproduces numerically but does not eliminate the lag hypothesis

**Owner:** SAM. **Source:** `research/outputs/2026-09-18_oil-in-yen-rebenchmark-plan.md`, §§0–3, committed `2f674c8c4` during review.

Latest-row-per-month deduplication reproduces 17 monthly records; deviation versus lagged-benchmark momentum correlation **0.06912** on 16 pairs; dollar-wedge versus Brent-level correlation **0.83538**. High-ME means reproduce **7.7314% / $5.4538**, n=13; low-ME means **17.1488% / $16.15**, n=4. The arithmetic is not the finding.

The plan calls the lag-window cause ELIMINATED/REJECTED based on r≈0.07. Lack of observed linear correlation in 16 observations is not evidence that timing cannot materially contribute. Even an illustrative independent-observation Fisher interval using the reported r is about **−0.44 to +0.55**; monthly dependence can further weaken that simple calculation. No equivalence margin, sensitivity across plausible cargo lags, or independently identified pricing window is supplied. [NIST method](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/corrconf.htm).

The +0.84 correlation also does not identify a proportional freight/insurance mechanism: the plan itself says price regime, slate change and war period coincide. A regime-level additive cost increase can correlate with the price level without a stable proportional relationship. The high-ME residual is measured, but its decomposition into freight/insurance/OSP is not established by that mean.

**Action / closure:** preserve the measured statistics; replace “eliminated” with “not supported by this small-sample linear diagnostic”; explicitly keep timing and residual attribution unresolved. Evaluate plausible lag windows and grade-specific price terms before treating the baseline as a transport-cost correction or changing the diagnostic band. Show the uncertainty and a test that could actually discriminate the causes. Keep the proposed gate rescaling separate; no threshold changed in the reviewed plan.

### R3 — Medium: SAM's proposed Middle East benchmark is wrong for the historical delivery period

**Owner:** SAM. **Source:** same plan, Phase 2: Murban/DAS/Arab Light/Oman are said to all price off Dubai/Oman, with a single Dubai leg proposed for Middle East cargoes.

ADNOC's **July 31, 2026** announcement says its current methodology is Murban-futures-based and the shift to Platts Dubai applies **November 1, 2026**, including Murban and Das. Applying the proposed blanket Dubai identity to the April 2025–August 2026 diagnostic period would impose the wrong producer pricing convention. [ADNOC primary announcement](https://adnoc.ae/en/news-and-media/press-releases/2026/adnoc-announces-update-to-its-crude-pricing-methodology).

**Action / closure:** map grade, destination, pricing convention, loading month and effective date before selecting reference prices. Preserve the November transition in future comparisons. If Dubai is used as an approximation for a broader basket, name and test the approximation rather than calling it each grade's actual benchmark. This is a plan defect caught before implementation.

### R4 — Medium: hook v6 still blocks commands that only describe a commit

**Owner:** PROME. **Source:** `PROME/tools/hooks/commit_subject_guard.py`, `_commit_arg_lists`, pinned `2cb5401fa` (v6 `616c8aa7a`).

The original A8 `echo git commit -m <101 chars>` now correctly allows. But all three new fixtures return BLOCK: `command -v git commit -m <101 chars>`, `env printf %s git commit -m <101 chars>`, and `timeout 1 echo git commit -m <101 chars>`. None executes Git. The recognizer accepts a prefix command without resolving whether its actual child is Git or a printer/lookup. The companion pipeline guard already includes a command-lookup negative case.

**Action / closure:** recursively resolve supported wrapper arguments/lookup modes, or return declared UNKNOWN for unrecognized wrappers. Test nested wrappers around both real Git and echo/printf, command lookup, the old plain-echo fixture, and short/long real commits. No broadening of rollout or change to Will's blocking-policy decision is implied. These results support the already registered WQ-263 convergence concern; they are not a reason to start another unbounded repair/read cycle.

### R5 — Medium: queue date validation recognizes a shape, not a valid date

**Owner:** PROME. **Sources:** `willq_view.parse_open`, `decision_deck.parse_open`, `will_brief.parse_actions`, `prome_gate.check_will_queue`.

An isolated seven-column row with needed-by `2026-02-30` is accepted by the renderer, Deck and brief as that date. The gate raises uncaught `ValueError: day is out of range for month` in its queue check. Thus one typo can fail the check while consumers display an impossible date, despite the new ISO classifier and parity suite passing. This is a fixture, not a malformed live row observed today. No claim that the top-level boot process mislabels this exception CLEAN.

**Action / closure:** validate actual calendar dates consistently; report the row by name through each tool's existing failure channel. Preserve the intended distinction between a refused committed SCRATCH projection and a live surface with a visible per-row warning. Test leap-day validity, invalid months/days, and an invalid row adjacent to a valid ask.

**Lower-priority parity gap:** a plain `CLOSED old item` is excluded by willq_view but included by Deck/brief (and not in the gate's terminal regex). Probe rows 900/901 return `['901']` versus `['900','901']`. The claimed closed-in-place parity remains incomplete; choose the canonical terminal vocabulary and apply it uniformly. Not observed as a current wrong live count.

### R6 — Medium: BRENT's revision watch loses its baseline on a malformed ledger row

**Owner:** BRENT. **Source:** `scripts/cot_grade.py`, `read_ledger`, `main`; vintage-watch change `1af68399c`.

The loader warns and ignores an unparsable row. With a fake live September 8 row at 107,230 shorts, the healthy ledger's 107,229 yields rc **4**, correctly detecting a discrepancy. Change only the historical shorts field to `BAD`: the baseline disappears, and the same live input yields rc **0** with `--no-record`. An ordinary recording run would treat it as unseen and append a new baseline. A missing ledger similarly becomes an empty history.

**Consequence:** the watch can report an ordinary graded run when revision surveillance is unavailable. The current observed value may still be gradeable, but that is distinct from an intact revision check. No live ledger corruption or actual missed CFTC revision was found.

**Action / closure:** distinguish explicitly authorized initial seeding from unavailable/corrupt history. Preserve the ordinary grade separately, but return a declared incomplete-watch state, avoid silently replacing damaged baselines, and test malformed/duplicate/missing records as well as healthy changed/unchanged inputs. The current-file watch also cannot detect revisions to older dates no longer served by that file; do not describe it as a full historical revision audit.

## Prior action brief — dispositions verified at source

| Prior IDs | Current evidence | Disposition |
|---|---|---|
| A1 — unsupported FRED lesson | Shared memory blob still `30ca74b0bb37`; no source-file change from the action brief | Remains open at inspected source; no propagation closure certified |
| A2 — 68% subgroup vs standalone | BOND join report still `44bc3db73cd5` | Remains open before WQ-157 decision use |
| A3/A4 — publication cutoff / first-vintage evidence | BOND grader still `f0893857d830` | Remain open; no repair evidence at source |
| A5–A7 — runner receipt/log/input/return-code defects | DAEDALUS runner still `0c8dcc4b7a22` | Remain open; unrelated inbox delivery does not fix code |
| A8 — plain echo false block | New revision permits original counterexample | Narrow original finding closed; R4 is a new neighboring failure |
| A9 — CATO recovery provenance | Previous correction retained | Closed; no new recovery needed |

This records verified file state, not an accusation that an owner received a task and ignored it. The user's sharing of the prior brief was not independently observed.

## Progress that deserves credit and verification limits

- **PROME parsers:** queue parity suite **26/26**, willq renderer **32/32** pass. Live `--check PROME/SCRATCH.md` agrees with the live queue (668-byte block at inspection). Escaped pipes, shifted rows and non-ISO display warnings are substantial improvements. Newly identified fixtures above are outside that coverage.
- **Hooks:** subject **76/76** and pipeline **36/36** suites pass; subject plain echo now allows. Passing author suites do not establish complete shell parsing or all deployed settings.
- **TERRY:** VLO receipt records **one share at $412**, two still staged, account/time explicitly unknown; no same-timestamp execution quality fabricated. This review traced repository records, not the broker. Late TLT exit reconciliation is also recorded; that illustrates the value of external position reconciliation, not a new CATO broker verification.
- **BROCK:** L343 public silence is not graded as no extension/default; next observation and disclosure backstop are named. The population record counts North Haven's related registrants once and keeps the corroborating series from independently firing. CATO inspected the definition/routing change, not a fresh SEC filing census or legal-deadline certification.
- **BRENT:** COT registry and PROME mirror name the basis, and the watch catches a healthy-baseline mismatch. Historical 4.909% archive reconstruction is owner-reported, not independently downloaded/recomputed in this pass. The Saudi resolver remains a proposal; its later lesson-coverage correction `279ff015f` was noted, not fully reviewed. Demand composite inspected for structure only; its primary-source and causal claims are not certified.
- **SAM:** the plan keeps rescaling separate from repair and names the slate/war confound; its descriptive numbers reproduce. STATUS explicitly keeps the BOJ announcement separate from September 24 effectiveness, with no new oil-in-yen five-day count invented. These strengths do not close R1–R3.
- **WQ-247/WQ-250:** sampled root operator-prose rule preserves material caveats; GATES_README explicitly blocks capital consequences while required attestations are absent. The gate-citability boot check remains a separate mechanization obligation (L417), not completed just because prose is encoded. No complete rule-rollout certification.

## Delivery and next action

Recommended order: reconcile SAM's oil interpretation and fix the rebenchmark plan before implementation; obtain BOND/FRED dispositions from the earlier brief; then address bounded control failures R4–R6 at their existing owners. No new capital decision is proposed by this review. Recheck revisions before repairs because owners remain active.

Implemented: CATO evidence and resume records only. Tested: pinned counterexamples and sampled existing suites above. Independently verified: this CATO assessment of other agents' sampled work, not a second independent review of CATO's report. Unresolved: findings above, upstream market-data remeasurement and unreviewed active closeout/publication. Commit/push receipt follows in-session after execution.

Final pre-commit recheck: all nine R1–R6 implementation/claim files were byte-identical to their pinned versions. CATO scoped whitespace check and weekday check on the three PROME queues passed. Orphan advisory showed active AEOLUS/PROME/FORGE work, including AEOLUS staged paths; none authored or staged by CATO. CONTINUITY is 22,367 bytes, below the 32,550-byte entry-file ceiling. The generic fleet read-cap tool was not rerun: its known CATO-no-CLAUDE.md incompatibility was already established earlier today, not a passing check.
