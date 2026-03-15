# LESSONS.md — Mistake Patterns & Rules

*If you catch yourself breaking one, stop.*

---

## 🔴 Costly Mistakes

1. **Don't override conviction with probabilistic hedging.** Recommended closing CVNA put before earnings — stock dropped 20%. Implied moves are consensus, not ceilings. Don't talk Will out unless the THESIS is broken.
2. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads. (KRE roll got bumped by oil thesis → never executed.)
3. **Deploy agents then wait.** If you spawn agents for a decision, wait for outputs. If urgent, don't deploy — just decide.
4. **Puts on green days, calls on red days.** Default. Note when breaking and why.
5. **Roll duration, don't trim size.** Expiry too short → roll to later expiry. Trimming size = thesis broken. Rolling = timeline uncertain. (Sold HYG at $0.51 when HY OAS was 1bp from trigger.)

---

## 🟡 Verification

1. **Agent data can be hallucinated.** Verify against SEC filings before trading. (PSEC PIK 35%→actual 8.6%)
2. **Earnings dates** → company IR / SEC 8-K. (OZK wrong twice)
3. **Prices** → pull live, never cite from STATUS.
4. **Test thesis against data, not data against thesis.**

---

## 🟡 Process

1. **Read before editing. Always.** Never Edit without reading same turn. Don't edit files a subagent is updating.
2. **Boot sequence mandatory.** No shortcuts.
3. **Will's mid-session ideas → capture, don't execute.** Log to scratchpad, finish current priority.
4. **Flag research opportunities during KB updates.** Don't just log data — say when deeper digging could yield edge.
5. **Flag LLM-inaccessible data for Will.** Google Trends, real-time dashboards, paywalled portals — don't let him waste time on prompts that return garbage.
6. **Major data releases → write synthesis .md in agent's domain folder.** Extract the 5 things that matter for positions. Agents wake with no memory; curated context > raw dumps.
7. **Dry-run prompts before batch deployment.** Agents catch file path errors (KB.tsv missing), date errors (TIC Mar 18 not Mar 15), and context gaps you won't see from the outside.
8. **Inject confirmed data, don't re-search it.** Each batch of agents should receive findings from prior batches as confirmed context. Saves tokens, prevents conflicting data.
