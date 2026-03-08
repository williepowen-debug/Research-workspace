# LESSONS.md — Mistake Patterns & Rules

*Review at session start. If you catch yourself breaking one, stop.*

---

## 🔴 Costly Mistakes (These Lost Money)

### Don't Override Conviction With Probabilistic Hedging
Recommended closing CVNA put before earnings. Stock dropped 20% — would have been near-max profit. Implied moves are consensus, not ceilings. When someone has conviction + timing, don't talk them out unless the THESIS is broken.

### Mechanical Before Creative
KRE roll was #1 priority. Got pulled into oil thesis → airlines → new positions. Never executed the roll or trimmed WAL at +133%. **Execute urgent trades (rolls, trims, expiries) BEFORE opening new research threads.**

### Deploy Agents Then Wait
Deployed 4 agents to inform AAL, entered the trade before any came back. If you deploy agents for a decision, WAIT for outputs. If urgent, don't deploy — just decide.

### Enter Puts on Green Days, Calls on Red Days
Entered AAL puts on a -4-7% day. Default: puts on green, calls on red. Note when breaking and why.

---

## 🟡 Verification Rules

1. **Agent data can be hallucinated.** Verify against SEC 10-K/10-Q before trading. (DARWIN "Sonnet 4.6" incident, PSEC PIK 35% → actual 8.6%)
2. **Earnings dates** → company IR page or SEC 8-K. (OZK was wrong twice)
3. **Real-time prices** → pull live, not from STATUS files.
4. **Direction on screenshots** → state explicitly, verify against context. (Called WAL -10.64% as +10.64%)
5. **Test thesis against data, not data against thesis.** Consumer finance showed improvement when thesis said stress. K-shape is real.
6. **Timing estimates** require reading ALL agent STATUS files, not just one.

---

## 🟡 Process Rules

1. **Read before editing. Always.** Never call Edit without reading the file same turn. After subagent completes, read their changes first. If you spawned an agent to update a file, don't also edit it yourself.
2. **Boot sequence is mandatory.** No shortcuts. 2 minutes prevents 10 minutes of bad output.
3. **Will's mid-session ideas → capture, don't execute.** Log to scratchpad, finish current priority first.
4. **Don't spiral on debugging.** If code works via curl but not browser → caching. Hard refresh. Max 2 attempts.
5. **Removing HTML elements → grep for their IDs in JS.** Bare getElementById on missing element kills entire function.
6. **`/clear` vs `/new` — context management.** `/clear` wipes conversation history but OpenClaw generates a compaction summary that rides along in the session. Multiple `/clear` cycles stack summaries-of-summaries — lossy and heavy (observed: 53% context at boot after 4 clears in one day, ~21% was compaction weight). `/new` creates a fresh session without compaction baggage — drops to ~32% (system overhead only). **Pattern:** `/clear` for mid-session pivots where you want some continuity. `/new` when accumulated compaction weight drags. Full file handoff required before `/new` (context won't survive), optional before `/clear` (summary carries forward). (Discovered Mar 5, 2026)
7. **During KB updates, flag research opportunities.** When cross-verifying data, if you spot a discrepancy worth resolving, a data gap worth filling, or a thread worth pulling — say so immediately. Don't just log the data silently. Will wants to be alerted to where deeper digging could yield edge. (Established Mar 9, 2026 — during LABOR staleness updates.)
8. **Major data releases → write synthesis .md in the relevant agent's domain folder.** NFP, ISM, Beige Book, FOMC minutes, bank earnings — every time. Extract the 5 things that matter for our positions, not the raw text. Agents wake up with no memory; curated context beats raw dumps. The file becomes a permanent reference library. (Established Mar 4, 2026 — Beige Book was the first one done right.)
