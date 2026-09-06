# Codex — what to borrow from Anthropic's multi-agent research system (relayed by Will, Sun 2026-09-06 ~10:0x ET)

**Filed verbatim by PROME (session `prome-04`, LAPTOP) at 10:1x ET.** Provenance: Will relayed Codex's text in-session after the two of them reviewed Anthropic's engineering post *"How we built our multi-agent research system"* (anthropic.com/engineering/built-multi-agent-research-system). PROME's verification ledger and assessment follow the verbatim block. Routing: WQ-185 (the 9/5 Codex overall assessment — same initiative, per Codex's own instruction "use that existing proposal, not create another") · DOCKET L291 (spawn-driver review 9/19) · L294 (origin-proof sweep 9/12) · L282 (P4 sitting 9/17).

---

## Codex, verbatim

> The most useful thing to borrow is Anthropic's evaluation discipline—not its agent hierarchy. You already have much of the delegation, continuity, and artifact infrastructure.
>
> After checking the current repository, I would pursue four options, in this order.
>
> ## 1. Evaluate one complete research episode
>
> Problem addressed: We can demonstrate that the system operates and corrects mistakes, but not yet how much that machinery improves research or decisions.
>
> Anthropic recommends evaluating actual outcomes, groundedness, coverage, and source quality—not simply whether an agent followed its prescribed process. Evaluation guidance
>
> PROME has already proposed three historical episode reviews under WQ-185①. We should use that existing proposal, not create another initiative. It remains pending in the queue I inspected. WQ-185 (Research-workspace/PROME/WILL_QUEUE.md:24)
>
> I would sharpen its proposed question, "Did the machinery change the decision?" Changing a decision is not inherently good; correctly maintaining one can be valuable.
>
> Instead, ask:
>
> - What was known at the time, and what was merely assumed?
> - What useful information did the system add?
> - Did its interpretation warrant changing—or retaining—the decision?
> - Did corrections reach the relevant decision surfaces in time?
> - What coordination work and human intervention were required?
>
> Smallest implementation: Review one of the proposed episodes first, using existing records, and produce one short findings document.
>
> Stopping condition: Identify the principal contribution, principal failure, and uncertainties. Do not turn the exercise into desk grading or a permanent scorecard.
>
> This is my preferred starting point.
>
> ## 2. Make bounded assignments genuinely bounded
>
> Problem addressed: A narrow research question can accumulate broader operational obligations.
>
> You already have "one spawn, one objective," a bounded subagent mode, and a completion format. However, the same spawn template also requires a whole-inbox drain and full owner-session responsibilities. A seemingly small assignment can therefore include substantial unrelated work. Existing orchestration contract (Research-workspace/PROME/ORCHESTRATION_PLAYBOOK.md:214)
>
> Anthropic's useful principle is explicit task boundaries and an expected output, with additional agents justified by distinct work. Lead-agent prompt
>
> Smallest experiment: For one suitable investigation, distinguish:
>
> - Investigation: answer the bounded question and return evidence.
> - Owner application: separately determine whether canonical state needs updating.
>
> This must respect your existing authority rules; it is not permission to bypass required owner work.
>
> Keep it only if: It produces an equally useful answer with less elapsed time or intervention, without creating an unowned application task. Otherwise, the separation has merely moved the burden elsewhere.
>
> I would test this before changing the standing spawn contract.
>
> ## 3. Replace repeated factual summaries with owner pointers
>
> Problem addressed: Each independently maintained copy creates another place a correction must reach.
>
> Your current completion format already has CHANGED, RESULT, and GAPS. Those fields can carry precise artifact references without adding a schema. Completion specification (Research-workspace/PROME/COMPLETION_SPEC.md:12)
>
> PROME's proposed generated "Pending Will" block under WQ-185② is a concrete instance: replace two hand-maintained copies with projections from the existing queue.
>
> Smallest implementation: Complete that one bounded projection if approved. For research handoffs, prefer the existing owner record plus the actionable implication.
>
> Acceptance test: Change a fixture's canonical item and verify both projections update correctly. The old manual copies must actually disappear.
>
> The benefit is less reconciliation work, not a more attractive dashboard.
>
> ## 4. Use known failures as reusable behavioral tests
>
> Problem addressed: A repair can look convincing without protecting against recurrence.
>
> WALTER's rewritten tests are already moving in the right direction. This also belongs in the existing September 12 verification work—not a new monitoring layer.
>
> Use a few consequential cases:
>
> - Failed evidence retrieval must not produce a positive verification verdict.
> - Filing must not substitute for application.
> - A corrected premise must invalidate dependent conclusions where appropriate.
>
> Test the final result, including successful controls. Keep research-judgment cases separate from deterministic software checks.
>
> ## What I would defer
>
> I would not add a permanent citation agent, another reviewer desk, a universal quality score, or a new orchestration framework.
>
> A fleet-versus-generalist comparison is worthwhile later, but the first episode review should help us define what a fair comparison would measure.
>
> My suggested first move: design and conduct one WQ-185 episode review, then choose the smallest operational change its evidence supports. That gives us a reason to build something—or a reason not to.

---

## PROME verification ledger (five-field; confidence tokens per STATE_VOCABULARY Class 13)

| # | Claim | Artifact | Check | Observed | Disposition |
|---|---|---|---|---|---|
| 1 | WQ-185 ① proposes three historical episode reviews graded on "did the machinery change the decision?" and is pending | `PROME/WILL_QUEUE.md` row 185 (the OPEN table; Codex cited line 24) | `sed -n '20,30p'` at 10:0x | Row 185 rec ①: "(a) duration → 004 TLT put … (b) GATE-REG-T02 → ROLL70 → EXIT guard … (c) HY 280/260 rails + X1 … graded on ONE question: did the machinery change the decision?" — needed by 9/11, OPEN | **VERIFIED.** Codex's sharpening lands on the exact phrase. |
| 2 | The standing spawn template requires a whole-inbox drain and full owner-session responsibilities alongside the bounded task | `PROME/ORCHESTRATION_PLAYBOOK.md` § Spawn/re-ping template item 2 (Codex cited :214) | `sed -n '205,235p'` | Item 2: "Full owner session, never a read-only receiver (§3.5.2): integrate … COMMIT … Whole-inbox drain — every sender, not just the triggering item (rule-6b mandate)." Item 4: the last touch runs the desk's FULL closeout. | **VERIFIED.** Live instance the same morning: the 09:50 BRENT L0 spawn = one bounded grade (OPEC+ L123) + a 10-item drain + the COT-35B read + full closeout, one tasking. |
| 3 | COMPLETION_SPEC's block already carries CHANGED / RESULT / GAPS | `PROME/COMPLETION_SPEC.md` § Required (Codex cited :12) | read at boot 09:4x | Block fields: STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS · FOLLOW-UP | **VERIFIED.** |
| 4 | WQ-185 ② = a generated "Pending Will" block replacing two hand copies | `PROME/WILL_QUEUE.md` row 185 rec ② · `HEARTBEAT.md` § Forward calendar line | rows read at boot | Rec ②: generated from `will_brief.py`'s queue parser, replacing the copies in SCRATCH (operator card) and HEARTBEAT. HEARTBEAT's line *stopped carrying a copy 9/5* ("after the copy rotted") — ONE hand copy remains (SCRATCH). | **VERIFIED with one correction:** "two hand-maintained copies" was true at registration; one already died. The projection still replaces a live copy. |
| 5 | WALTER's rewritten tests are behavioural; the 9/12 verification work exists | `PROME/HANDOFF.md` 9/5 NIGHT-2 ② · DOCKET L294 | HANDOFF read at boot; `sed -n '294p' PROME/DOCKET.tsv` not re-run this pass | Suite v2 = 34 behavioural assertions (dbf8c765c · c1281504a); L294 = FLEET SWEEP — ORIGIN-PROOF INSTRUMENTS, DAEDALUS, 9/12, behavioural method | **VERIFIED** (HANDOFF + SCRATCH calendar; DOCKET row cited by the view). |
| 6 | Anthropic's post: end-state evaluation; rubric = factual accuracy · citation accuracy · completeness · source quality · tool efficiency; human eval finds edge cases; start with ~20 queries; subagents need objective · output format · tools · task boundaries; effort scaled to complexity; a CitationAgent | anthropic.com/engineering/built-multi-agent-research-system | WebFetch 10:0x (summary extraction) | All seven points present, quoted: "focus on end-state evaluation rather than turn-by-turn analysis" · the five-dimension rubric verbatim · "People testing agents find edge cases that evals miss" · "about 20 queries" · "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries" · the 1 / 2–4 / 10+ subagent scaling · the CitationAgent | **VERIFIED** (by a summarising fetch — not a line-by-line read of the post). |

## PROME assessment (10:1x ET) — one paragraph per option

**① Episode review — AGREE, and the re-cut question is the improvement.** The fleet's norm of "verify at the artifact" is Anthropic's *groundedness*; "source + date every claim" is *citation accuracy*; "graded at the primary" is *source quality*; the completion block's GAPS is *completeness*. The rubric dimension the fleet does NOT measure anywhere is **tool efficiency (cost per result)** — Codex's fifth question ("what coordination work and human intervention were required") is exactly that line, and the ORCH_LOG (spawns · drained · Will-word triggers) + the correction register are the existing instruments to read it from. Rec: rule WQ-185 ① with the five-question frame; **one episode first: (b) GATE-REG-T02 → ROLL70 → EXIT guard** — the smallest complete chain (registered → fired 9/1 → filled 9/2 → three rulings 9/3 → live guard), every record inside the current spine (nothing rotated), one owner desk plus TERRY plus Will's own hands (the Robinhood fill; the GTC price still UNKNOWN, WQ-167 — a real "human intervention required" datum). (c) HY rails + X1 second, as the *retained-decision* case the re-cut question was built for. Stopping condition as Codex states; no scorecard.

**② Bounded assignments — AGREE on "test before changing the contract", DISAGREE that it is cheap to test on a dark desk.** The whole-inbox drain exists because a DARK desk has no other consumption path (8/23: TERRY held 10 unconsumed items — the case that widened the rule); for a dark desk the "owner application" half is unowned by construction, which is Codex's own keep-criterion failing. The fleet already has the bounded-investigation mode for read-only work (BOARD_CONSUMPTION_SPEC §3.5.2 / triage outcome ②; `coldreader`). The open question is only for WRITE-class bounded spawns on desks with an imminent owner session. Rec: instrument, don't experiment yet — the 9/19 spawn-driver review (L291, M1/M2/M3 + kill criteria) is the home; feed it n≥3 L0 spawns' time-split (bounded task vs drain vs closeout, from commit timestamps + the memo's CHANGED list; the 09:50 BRENT spawn is #1). A new WQ-185 leg ⑤ carries the question so it is not a new initiative.

**③ Owner pointers — AGREE; the precedent exists.** `docket_view.py` already did this for the SCRATCH calendar (ADOPTED 9/3, gate-advisory drift check, 0 divergences). WQ-185 ② is the same flip for the Pending-Will list. Codex's acceptance test (change a fixture item → both projections update → the manual copy is deleted, not left beside) becomes the ② deliverable's test. Note the HEARTBEAT copy already died 9/5, so ② replaces one live copy, not two.

**④ Failures as behavioural tests — AGREE; dock, don't build.** Case (a) *failed evidence retrieval must not produce PASS* IS L294's method (WALTER's eight defects are its reference cases). Case (b) *filing ≠ application* is the P4 sitting's subject (L282, 9/17: correction-class validation; the receipt-gap instances L115/L239/HOMER). Case (c) *a corrected premise invalidates dependents* is the CVNA unwind (six CARL surfaces) and error #100 — `consumer_check.py` class, also L282. Rec: dock the three as NAMED test cases into L294 (a) and L282 (b)(c) notes; each must have a passing control. DOCKET edits, after this session's first DOCKET edit (the glob-pointer fix).

**Deferrals — AGREE.** No citation agent (coldreader is the bounded form and stays per-artifact), no new reviewer desk (RAV is sole QC since 9/5), no universal score, no framework. Fleet-vs-generalist later; the episode review defines the measure.

**What this filing changes:** WQ-185's rec cell carries a 9/6 amendment (five-question frame · (b) first · leg ⑤). Nothing else moves without Will's word.
