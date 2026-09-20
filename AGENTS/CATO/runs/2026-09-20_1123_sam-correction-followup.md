# SAM correction follow-up — improvement verified, residual claims remain

September 20, 2026, CATO review for Will. Initial HEAD `6b20ae3d7`; actual SAM implementation `a16c17f6b`. The quoted `c34e56511` is an intervening CATO/PROME review commit, not SAM's implementation; it can serve as a shared-branch push head without changing authorship. No owner edits, sends, trade/grade changes, proxy build or operational boot assigned. Concurrent CATO CRUISE report preserved. No pull over that work.

## What is verified closed

- The stored original Totan image was independently viewed on white (original PNG unchanged). All five rows, source date/time, reference terms, OIS levels and displayed cumulative counts match the review JSON and final five ledger rows. SHA256 `1105fdfc5e5d0229651e6043fccf1aa033f7eb78f527bac5576360c0ac4d71e0` matches. Offline execution of the existing validator at review time passes all five rows. The current publisher page points to the same image URL. These are reviewed indicative values as of September18 15:15, with JST assumed, not executable quotes.
- The two-year proxy proposal is explicitly withdrawn in SAM's response/commit. No proxy code was added in the inspected commit.
- Study code, per-event output and a limitations report exist. A fresh read-only Yahoo rerun through the same script, with captured inputs under /tmp, reproduces all eight reported rounded means. Thirty-year results match exactly; the largest per-event TLT difference is about0.0000273 percentage point, immaterial at reported precision. This is same-vendor reproduction, not an independent market-data certification. There are179 input sessions and176 valid three-session baseline windows, not176 raw sessions.
- The unconditional “channel too small” conclusion and the bank-shares description are withdrawn. These are meaningful corrections. [Prior review](2026-09-20_1056_sam-intervention-and-proxy-review.md) remains the original finding record.

## F1 — High: the new position list still includes disposed/past-date contracts

SAM now identifies puts, but lists WAL77.5P together with WAL70P/67.5P as the exposure that partially offsets duration shorts. In `FORGE/STATUS.md`, WAL77.5P August21 is struck through and explicitly SOLD (Will confirmed August18); Fidelity WAL70P/67.5P September18 rows are past their dates with outcomes not freshly reconciled. Robinhood December70P is a distinct row. Do not turn a historical instrument inventory into current exposure. The October TLT82P is still omitted from the “TBT and TLT77P” duration summary despite appearing in both the mirror and the September16 capture report.

Correct conditional statement: if the currently held instruments remain long bank puts and bearish Treasury positions, a simultaneous bank decline/Treasury rally has opposing first-order directional effects. It does not establish a present, material offset or guaranteed gains/losses. Actual position status, option sensitivity, volatility and time still matter. No broker truth recertified here.

## F2 — Medium: chart values are accurate; next-hike and horizon interpretation are not equivalent

The chart's December63% column refers to that meeting's incremental25bp equivalent under the publisher's policy-only model. It is not automatically a63% probability that December is the first/next hike. Even assuming only no-change/one25bp hike at each meeting, with October22% and December63%, the probability of first hiking in December is63% minus the probability of hiking in both meetings: between41% and63%. The joint path is not supplied. December can still be the modal next date under that simplified model; the attached63% is not its identified next-date probability. The local OIS README already limits probability interpretation to a binary no-change/one-step assumption.

The source really prints1.94 through April2027. That is a model-dependent cumulative equivalent, not a certain number of hikes and not a like-for-like replacement for a two-year horizon. Preserve the reference period, source assumptions and TONA-versus-policy basis; do not imply direct arithmetic from the1.25% administered setting alone. [Totan methodology and table](https://www.totan.com/archives/15647).

Two distinct sources agreeing on December does not establish statistical independence; the survey statistic, sample/date and event definition need comparison before treating them as two independent probability estimates. No survey re-audit performed here.

## F3 — Medium: restored pricing has not reached the peer brief

At the reviewed snapshot, `AGENTS/SAM/NEXUS_BRIEF.md:49` still says pricing is DARK, the script returns an unreviewed chart and the desk has no current pricing. STATUS line24 says RESTORED, while its opening line retains “BOJ OIS still DARK” attached to the earlier boot sweep. Label that opening explicitly as pre-restoration history and update the active peer obligation. This repeats the already observed summary-propagation failure.

The new STATUS row highlights October30 expiry but omits the feed's separate four-day quote-age ceiling. September18 15:15 reaches that age limit September22 15:15 JST; the decision expiry does not keep the September18 quote current until October30. The existing validator enforces both, but prose consumers also need the earlier freshness limit. No new checker is necessary for these wording repairs.

## F4 — High: November is a checkpoint, not guaranteed funding identification

The new REPORT says the November MOF/FRBNY primaries settle the funding question. The examined [MOF quarterly format](https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2026_2Qe.html) publishes operation dates, amounts and currencies; it does not supply a Treasury liquidation funding ledger. The [New York Fed quarterly series](https://www.newyorkfed.org/markets/quar_reports) concerns its U.S. monetary-authority FX operations. It may clarify U.S. participation; it is not a promised comprehensive account of Japan's funding transactions. Future narrative could add evidence, but no guarantee is established. SAM's own `MOF_INTERVENTION_PLAYBOOK.md` section S1-B already separates Japanese reserve funding from ESF/SOMA participation and warns that reserve-stock changes do not identify Treasury sales.

Likewise, the new49bn/day calculation is an average conditional on a two-day allocation, not measured daily Treasury liquidation. The report itself labels July30's8.45trn an estimate and July31's6.95trn a residual. Subtracting an estimate from a monthly total does not independently identify a date or execution amount. Keep that assumption attached rather than asserting essentially all the money was spent on those two days as an official fact.

## Study boundaries and reproducibility

The saved script measures adjusted TLT close-to-close returns and Yahoo30-year-index close changes starting at the operation-date close. It therefore omits that day's intraday/immediate movement and supports post-operation-close descriptions only. Overlapping observations occur in two date clusters; their effective independent sample size is not established. Dependence alone also does not mathematically prove the nominal SE must be too small without a covariance assumption. The cautious conclusion is that the reported SE is not justified for this design, not that two independent campaigns or a direction of SE bias has been demonstrated.

The code downloads fresh adjusted data rather than retaining its original inputs. The current rerun supports the table at displayed precision, not byte-stable historical reproducibility. Initial sandbox DNS failure produced empty data/NaNs but exit0; the escalated rerun succeeded. This is an observed study-script robustness limit, not evidence that the committed179-session run was empty. No code repair performed. [Follow-up evidence](2026-09-20_1123_sam-followup-evidence.json) preserves rerun inputs/output, original-artifact hashes, validation and comparison results.

## Disposition

Accept the completed chart review, proxy withdrawal and rounded study reproduction. Ask for one bounded owner pass over current-position status, next-hike wording, OIS consumers/freshness and November's actual evidentiary scope. Do not rebuild the proxy or add a new blanket gate. Only CATO report/evidence and its SAM continuity entry changed. Whitespace check passed; root weekday check passed on four files. Orphan advisory identified six concurrent CRUISE paths, preserved along with the other CATO session's untracked CRUISE report. Final Git receipt in-session. Next: orient and await Will; no further task assigned.
