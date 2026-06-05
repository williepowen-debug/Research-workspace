---
name: feedback-consolidate-domain-pressure
description: "When multiple agents converge on the same near-term Will-decision, route SIGs async with default-pass deadlines and consolidate responses into ONE Will-facing approval packet — don't let N parallel conversations land on Will"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e6629907-4074-4b33-a33b-c3bcc04ed00e
---

When multiple domain agents need to weigh in on a near-term Will-decision (typically because they each own positions inside the same catalyst window), route via async SIGs to their inboxes with explicit default-pass deadlines, then consolidate responses into a single Will-facing approval packet. Don't make Will absorb N parallel agent conversations.

**Why:** Will surfaced this directly on 2026-05-22 during the 6/18 expiry-cluster work — "every agent seems to be focusing on these june puts. I am getting this pressure from all agents haha." The clock was real (28 days to expiry), but the *coordination friction* was Prome-manufactured: asking 3 agents synchronously for input means 3 parallel conversations land on Will. The reframe was: file SIGs async with 48h default-pass, PROME consolidates, single decision packet to Will.

**How to apply:**

1. **Detect the convergence early.** When you find yourself wanting to ask BROCK + REGINALD + HENRY (or any 3+) about the same decision in the same session, that's the trigger.

2. **Route SIGs async, parallel writes, scoped slices.** One inbox file per agent. Ask only for *their slice* of the decision — not the whole problem. Specify exactly what calibration you need (thresholds, roll targets, trigger language).

3. **Set an explicit default-pass deadline.** "Default-passes 2026-05-24 EOD; draft levels stand if no response. Will-approval is the adoption gate, not your response — but your response materially improves the levels."

4. **PROME owns consolidation.** When responses land (or deadline passes), build v0.2 (or whatever the next version is) combining all inputs. Present to Will as ONE packet with: (a) consolidated artifact, (b) clear summary of what each agent contributed or default-passed, (c) explicit Will-approval ask.

5. **Use Convention B (own-outbox routing).** Tell each agent to reply via their own outbox `REPLY-PROME-YYYY-MM-DD-{slug}.md` rather than writing back to PROME inbox. PROME scans agent outboxes at next boot per [[feedback-scan-agent-outboxes-at-boot]]. Lower friction for the agent + audit trail stays in the agent's directory.

**When NOT to apply:** if only 1-2 agents need input, just spawn them (or write to one inbox). The async-and-consolidate pattern is for 3+ parallel weighs-in. Also don't apply when the decision is time-critical enough that 48h default-pass blows the catalyst window — in that case, teams-mode spawns may be appropriate despite the synchronicity cost.

**Cross-refs:**
- [[feedback-route-to-domain-agent]] — Prome is coordinator not domain expert; the SIG pattern routes calibration to domain agents
- [[feedback-scan-agent-outboxes-at-boot]] — Convention B reply mechanism
- [[feedback-front-load-planning]] — same family: surface decisions before execution + batch Will-approve defaults; this pattern is the multi-agent analog
- [[feedback-named-spawn-teams-mode]] — alternative for time-critical cases where async won't work
- [[finding-push-train-pattern]] — adjacent: async coordination across multiple agents producing clean outcomes
