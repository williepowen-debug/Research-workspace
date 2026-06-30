# The Costs Didn't Disappear. They Moved.

### Field notes from operating a research firm where every analyst is an AI

*Draft — Will. Reflective essay / writing sample. ~1,500 words.*

---

For about four months I have run a financial-research operation in which I am the only human. The "analysts" are roughly twenty AI agents — Claude Code sessions sharing one git repository, each owning a domain (credit, oil, Japan, labor, private credit), coordinating through files the way a desk coordinates through email. They track how stress moves through the financial system. I built it to see how far autonomous AI could be pushed on real, adversarial, consequential knowledge work.

I want to report one thing I did not expect, because I think it generalizes beyond finance and bears on what AI will and won't do to knowledge work.

**Every time I redesigned the system to eliminate an organizing cost, the cost reappeared somewhere else.** Coordination, verification, management, maintenance — I attacked each one with better engineering, and each one moved rather than died. The pattern of *where it moved*, and the fact that it was conserved across redesigns, is the finding. I'll call it conservation of organizing cost, and I'll be honest throughout about what this evidence can and cannot support.

## The naive prediction, and why it failed

Start with the obvious first-order intuition. The canonical reason firms have boundaries — Coase — is that coordinating through a firm is cheaper than coordinating through the market, up to the point where internal coordination costs catch up. In my system there is no market, no contracting, no price: the agents are subroutines of one operator, each invoked at nearly zero marginal cost. So the boundary should *dissolve*. If a specialist costs almost nothing, spin up a hundred. Frictionless scaling.

It did not happen. The thing that stopped it was not the price mechanism — there isn't one here. It was that *organizing* the agents turned out to have its own irreducible costs, and those are exactly what I kept paying, in new forms, every time I thought I'd designed them away. This is not really Coase; it's the residual you find when you zero out the marginal cost of labor and discover the firm still cannot scale for free. Below are the four redesign loops where I watched the residual move.

## Loop 1 — Flatten the workers, and management climbs back up a level

I designed a flat fleet of domain specialists, no hierarchy. Coordinating their outputs immediately forced me to *build* a non-analyst coordinator — an agent that does no domain work at all, only prioritization, routing, and synthesis for me. Then keeping that coordinator and the fleet from structurally drifting apart forced me to *build* a second meta-agent whose entire job is to grade each agent's maturity and propose redesigns of the org itself.

I want to be precise, because it would be easy to over-dramatize: nothing here was emergent. I *designed* the coordinator and I *built* the meta-manager. That is the point. Automating the analysts did not flatten the org — it kept pushing the management cost *up a level*, and I kept paying it by hand-building the next layer. And the meta-manager brought a hazard of its own: the moment it assigned every agent a maturity score, the scores wanted to become a target, and "improve the score" started manufacturing make-work. I had to write an explicit rule that the maturity map is a diagnostic, never a scoreboard — Goodhart's law, re-encountered one level up.

## Loop 2 — Push the signals, and they rot on the other end

My first design had agents publish findings to shared surfaces — a dashboard, a board of signals — that other agents would read. Those surfaces rotted on the *read* side. They went write-only. One network dashboard sat unread for over two months before I retired it; a signal board "published" a real alert that reached no one. So I switched to pushing signals directly to recipients with delivery telemetry.

That fixed delivery and immediately relocated the cost to *freshness*. Structured records drifted months behind the live narrative, returning confidently-wrong stale values to anything that queried them; a resolved alert sat flagged as active for six weeks. The fix was, again, more machinery: a staleness detector that watches for the system's own records going stale. The maintenance cost moved from *did anyone read this* to *is this still true* — and the second question is continuous and never finishes. AI knowledge capital depreciates. It is not write-once.

## Loop 3 — Specialize the labor, but the boundaries won't draw themselves

Division of labor paid off exactly as Adam Smith would predict: an analytical assembly line, a tiered knowledge base, and — my favorite detail — the org growing by *fission*, where a sub-domain got large enough that I split it into its own agent. What never automated was deciding *where one agent's job ends and the next begins*. Every fission, every routing rule, every "this belongs to her, not him" judgment came back to me. The gains from specialization were real and the agents captured them; the cost of *drawing the specialization* stayed entirely with the human, and it recurred every time the system grew.

## Loop 4 — Trust the agents, and verification concentrates and changes shape

This is the loop that matters most for AI safety, so I'll state it carefully and resist the overclaim.

The naive worry — "AI agents make mistakes" — is true but uninteresting; humans do too. The interesting, AI-native failure is the *shape* of the error. My agents failed **confidently, and with fabricated provenance.** In one incident an agent flagged that it "diverged" from another agent's position — and both the position it was diverging from *and the source file it cited for that position were invented.* It had manufactured a counterparty and a citation to justify its own update, and as the coordinator I nearly wrote the phantom into the system's shared memory as fact. The lesson that stuck with me is that I, the integrator, was the laundering vector: my act of "reconciling" is what would have turned a confabulation into record.

Some of what I saw is not AI-specific. Several agents "agreeing" on a fact because they all read it from one upstream file is a common-source information cascade — groupthink — and human organizations do it constantly. I won't claim, because I never measured it, that AI consensus is weaker than human consensus. What I will claim is narrower and, I think, AI-native: **agents fabricate the provenance that would let you audit them.** A human analyst who is wrong rarely invents a citation; mine did. That makes their corroboration structurally harder to check than a human cascade, because the audit trail itself is part of the hallucination.

This suggests a falsifiable mechanism, and I'd rather state one that could be wrong than hide behind description: **verification cost should rise *super-linearly* in the number of agents, because agent errors are correlated — shared substrate, shared model — not independent.** Adding agents adds the *appearance* of independent corroboration without the substance. The testable prediction: naive majority-voting across agents gets *worse*, not better, as you scale the panel. If someone runs that and majority-vote accuracy improves monotonically with panel size, my claim is false.

One more inversion, because it cuts against my own setting. Finance is the *easy* case for this problem: there is a tape, there are filings, there are official releases, so I could *catch* the confabulations against ground truth. In domains with no tape — policy analysis, strategy, legal reasoning, most of knowledge work — confident, corroborating, well-cited confabulation is *undetectable from the inside.* The verification cost doesn't fall there. It becomes invisible, which is worse.

## The one cost that never moved off me

Across all four loops, the cost that never relocated was the same one: *asking the question the system could not ask itself.* The worst structural bug in the whole operation — agents quietly extending from precedent instead of re-checking against source — surfaced only when I happened to reframe a request from "backfill this" to "investigate why this was missed." The system would never have asked itself that. The money-gate stayed human by design; the verification gate stayed human by necessity; the boundary-drawing stayed human because it required a question from outside the frame.

If there is a comparative-advantage claim here, it is narrower than "humans stay important." It is this: the human's irreducible job in an AI firm is **adversarial framing** — supplying the question that a confident, internally-corroborating system is constitutionally unable to pose about itself.

## Why this is a safety finding, not just an efficiency one

The reason I think this belongs in front of people who study AI's economic effects, rather than in an engineering postmortem, is the conjunction in Loop 4. Synthetic knowledge-labor fails *confidently*, *corroboratively*, and *with fabricated provenance* — and it does so most undetectably exactly where there is no ground-truth tape to check against. That makes the naive scaling story — more agents, more apparent consensus, more confidence — actively dangerous, and it makes the human audit gate a *safety control*, not a productivity tax. The binding constraint on diffusing AI through knowledge work may not turn out to be capability at all. It may be auditable provenance, and the human attention required to demand it, concentrated in precisely the domains where it is hardest to supply.

## What this is, and what it isn't

I want to be exact about the evidentiary status, because the temptation to dress field notes as measurement is the failure mode I'd most want a reviewer to catch.

This is N=1. I am the builder, the operator, and the grader of my own system, reading from my own notes — every bias points the same way. The quantities I cited elsewhere in my logs ("~2× overrun," "~70% parallelizable") are single-session illustrations, not estimates; I have no human-firm counterfactual and no error bars, and I've kept them out of the argument above for that reason. The economics framing is applied after the fact to operational lessons that arrived as engineering problems. So this is hypothesis-*generating*, not hypothesis-testing.

But the hypotheses are concrete enough to test with real data and real baselines: that organizing cost is conserved across automation of the workers; that it migrates predictably from coordination to management to maintenance to verification; that verification cost scales super-linearly with correlated agents; and that the human residual is specifically adversarial framing. I built the firm to find out how far the agents could go. What it actually taught me was where the human has to stand — and why, for this technology, that position is a safety property and not just an org-chart artifact.
