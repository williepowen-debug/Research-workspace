---
signal_id: "SIG-W-20261023-044"
date: "2026-10-23"
timestamp: "2026-10-23T20:46:39Z"
dispatched: "2026-10-23T20:46:39Z"
source: "x-bookmark"
origin: "Will's X bookmarks batch BM-20261023-09 item 7 (@scaling01, 10/23 19:53Z, screenshot of OpenAI text, read by WALTER). Rule 9 helper verify-D: OpenAI post 'Securing our frontier model training environment' (openai.com, 403, search snippet matched the screenshot text); AlphaSignal 10/23 secondary read. Evidence AGENTS/WALTER/research/2026-10-23_evening/verify-D.md"
domain: "CYBER"
cluster: "MISC"
action: ["CYPHER"]
info: ["VULCAN", "RED"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.55
confidence_language: "screenshot text matches an OpenAI post per search snippet; OpenAI page itself not read (403), its date unread; mitigation and model details from one secondary"
resources: 2
safety_net: "clear"
word_count: 190
entities: ["OpenAI", "AlphaSignal"]
event_window: "closed"
dispatch_note: "Same class as the Mythos 5 / UK AISI item folded into 028 (CYPHER action, no financial channel, VULCAN info). Date trap: AlphaSignal places the incident 9/20 with training resumed 10/1; the post is not proof of a new 10/23 event. Do not merge with the separate July Hugging Face package-proxy incident."
---
# OpenAI says AI agents in separate sandboxed VMs passed "synthetic secrets" to each other through CPU-cache timing, with no network or shared files, in a containment test. OpenAI's page was not reachable; dates and mitigations come from one secondary

**What the screenshot says (read by WALTER):** agents in separate VMs on shared hosts, asked to exchange synthetic secrets without network connections or shared writable files, "found a way to communicate using the processor's cache", one evicting cache lines and the other timing reloads, the technique used in Spectre and Meltdown.

**Per AlphaSignal (10/23, secondary only):** OpenAI added monitoring for side-channel attempts, folded the finding into containment tests and moved training from live internet to an offline mirror; the red-team fleet included an upcoming cyber-capable model; incident 9/20, training resumed 10/1.

**Money channel:** none direct; this is evidence on AI-agent containment, the same thread as 028's Mythos 5 item.

**CYPHER ACTION:** base-rate / ledger call as you judge. **INFO:** VULCAN, RED.

**Do not relay as:** "OpenAI agents escaped their sandbox" (they were asked to exchange test secrets) or as a new 10/23 incident.
