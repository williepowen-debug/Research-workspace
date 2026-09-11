# SAM second review — September 11, 2026

## Verdict

Reviewed new SAM commits `266b11482` (16:08:44 ET) and `f7d26ddcb` (16:08:50 ET), relative to the previous review. The tool repairs and auction-scoring correction were adopted correctly. The CFTC data are correct. The claimed handoff repair is incomplete, and the new interpretation goes beyond what weekly position totals establish.

## Findings

**P1 — A fresh brief header still covers stale decisions.** `f7d26ddcb` adds the CFTC lead and changes the provenance line, but leaves the old CROSS-DOMAIN, WAITING FOR, VIEW, NEXT DECISION and FORWARD CATALYSTS content largely intact. At the reviewed commit, lines 39, 49, 78 and 90 still describe futures activation as pending, RED's report as unread and the auction ruling as owed. Line 38 even leaves the CFTC release pending below the new headline announcing its arrival. The first Totan chart's softening remains without its later partial reversal. The commit message says settled decisions were refreshed; the diff does not support that completion claim. Correct commit order alone did not repair content.

**P1 — Rising aggregate OI does not exclude a squeeze component.** Both STATUS and the new brief assert that a squeeze necessarily shrinks OI and therefore this was not forced covering. The reported short reduction coexists with a rise in longs and aggregate OI. New positions elsewhere can more than offset closed positions; week-end stocks do not identify motives or intraperiod sequencing. As a simple hypothetical accounting example, 41,401 contracts closed and 129,154 new contracts opened leave OI up 87,753. That is not a reconstruction of these trades; it demonstrates why the aggregate cannot exclude covering. [CME defines open interest as outstanding contracts](https://www.cmegroup.com/education/lessons/open-interest), not a direct test of whether any participant was forced to exit. The supported conclusion is mixed gross-position changes with expanded aggregate participation, not “no squeeze.”

**P2 — The tail-risk and causal conclusions are not identified.** The brief says the tail has switched from short squeeze to long unwind, with little fuel because the net is only 5.7% of a historical short extreme. Netting conceals opposing gross books; a small net is not proof of negligible short-side exposure, nor is a short-side historical extreme a calibrated long-crowding threshold. The statement that positioning was the marginal price-setter also overreaches: CFTC ends September 8, whereas the quoted FX interval ends September 11. The association supports a hypothesis, not that causal identification. Preserve the no-rearm decision; remove the exclusive risk-direction verdict.

**P2 — The replacement timestamp is impossible for the claimed information set.** The brief says 17:2x UTC / 13:2x ET while announcing a 15:30 ET release and citing a 16:08 ET STATUS commit. Git ordering is correct, but the written as-of is not. The correction distinguishes the 16:08 ET source cutoff, September 8 position date and earlier quote vintages.

## What passed

The three tools, regression test file and auction-scoring explanation are byte-identical to the previous review's corrections. All 14 regression tests and eight CFTC self-test cases pass on SAM's committed implementation. No new code defect was found in this bounded follow-up.

The official [CFTC futures-only release](https://www.cftc.gov/dea/newcot/deafut.txt), contract 097741, September 8 row, matches the ledger: OI 499,635; non-commercial longs 178,791; shorts 167,995; net +10,796. Changes reconcile to longs +61,622, shorts −41,401 and net +103,023. The contribution split is approximately 59.8%/40.2%, an accounting decomposition of the net change. “First net-long week” is accurate for SAM's tracked 23 observations, not a claim about all history. The source also reports commercial shorts increasing 135,882, illustrating why market-wide OI must not be attributed solely to the non-commercial category.

SAM correctly preserved the registered SAM-28 route requirement despite the magnitude observation. The historical forecast scoring explanation now distinguishes preserving the record from endorsing a dropped conjunct. Those parts of the response to review are sound.

## Corrections and validation

Prepared a patch against `f7d26ddcb` on isolated branch `review/sam-followup-20260911`. It reconciles the brief and STATUS, removes unsupported exclusive squeeze/crowding/causal conclusions, updates closed decision rows, and labels dates consistently. The official data row and all code remain unchanged. The FX sentence now distinguishes a 4.2% USD/JPY decline from roughly 4.4% reciprocal yen appreciation.

Validation: 22 existing checks pass; ledger differences and net arithmetic independently reconcile; reviewed the resulting document diff and checked that the named stale claims are gone. No new tests were added for prose edits. No fresh market quote pulls, messages, trade actions, shared-checkout writes, pushes or merges were performed. Historical commit messages remain unchanged; this report records their unsupported claims.

The operational lesson is specific: review acceptance needs a content check against each finding. Passing the ordering rule and changing a provenance hash did not discharge the actual handoff correction.
