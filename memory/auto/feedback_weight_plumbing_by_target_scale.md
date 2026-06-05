---
name: Weight Plumbing by Target Scale
description: When evaluating WALTER/agent infrastructure work, measure against the scaled pipeline being built toward, not single-session throughput
type: feedback
originSessionId: 2594b10d-cd56-4ad8-bf7c-a10ebc44e78b
---
Don't use "did this move a thesis signal today?" as the test for whether plumbing/infrastructure work on WALTER (or any agent) is real work. The test is "is this ready for the operational scale we're building toward?"

**Why:** Will explicitly said (2026-04-11) "we will scale. We are still working out the kinks" and reminded me he was never trained to build any of this — he's self-taught on multi-agent architecture and iterating his way through. He's treating WALTER as real operational infrastructure that will eventually handle 10-15+ signals/week across a 12-agent network. This came up after I had wobbled and framed a routing-table + audit-log session as "plumbing work with contingent value" that I wasn't sure was worth it. He pushed back and reset the frame.

**How to apply:** When evaluating a plumbing task (spec fixes, routing tables, log directories, boot protocols, audit trails, backup columns), ask "does this unblock the scaled version?" not "did this move a thesis signal in this session?" Being honest about what's load-bearing today vs what's preparatory is still OK — but don't frame contingent-but-likely value as spinning wheels. Don't make Will feel like he has to justify the approach to me. He's building novel infrastructure and learning as he goes; the right posture is collaborative build-out, not skeptical ROI audit. When I'm honestly uncertain about a trade-off, I can ask, but I shouldn't imply the work is overbuilt.
