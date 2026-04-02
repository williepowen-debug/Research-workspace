# LESSONS.md — Mistake Patterns & Rules

*If you catch yourself breaking one, stop.*

---

## 🔴 Costly Mistakes

1. **NEVER stop/restart the gateway.** Running `openclaw gateway stop` or `systemctl stop openclaw-gateway` kills communication with Will. On Mar 18, a prior session stopped the gateway TWICE — Will lost contact for ~1 hour. The gateway is infrastructure, not something agents should touch. If there's a gateway issue, tell Will and let him handle it.
2. **Don't override conviction with probabilistic hedging.** Recommended closing CVNA put before earnings — stock dropped 20%. Implied moves are consensus, not ceilings. Don't talk Will out unless the THESIS is broken.
2. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads. (KRE roll got bumped by oil thesis → never executed.)
3. **Deploy agents then wait.** If you spawn agents for a decision, wait for outputs. If urgent, don't deploy — just decide.
4. **Puts on green days, calls on red days.** Default. Note when breaking and why.
5. **Roll duration, don't trim size.** Expiry too short → roll to later expiry. Trimming size = thesis broken. Rolling = timeline uncertain. (Sold HYG at $0.51 when HY OAS was 1bp from trigger.)
6. **Two expiry frameworks.** PC single-name puts (APO, ARES, ARCC): dateable catalysts → May/Jun/Jul expiry. Macro/index (HYG, KRE, IWM): Hamilton demand destruction → Dec expiry. Don't mix them. BRENT owns Hamilton clock. BROCK owns PC catalyst clock.

---

10. **One spawn, one objective.** Don't bundle two distinct goals into one agent spawn. Agent context is finite (~50K tokens, 3-8 min). REGINALD P-002 bundled inbox processing + EARNINGS_PREP upgrade — inbox got done, prep didn't move. Split into two proposals instead.
11. **Check subagent status before every response.** During active spawns, run `subagents list` before replying to Will. Report completions FIRST. Auto-announce is unreliable — system-level push notifications for subagent completion are inconsistent (race conditions when multiple finish near-simultaneously, possible delivery drops). Don't trust auto-announce alone. On Mar 26, BROCK and REGINALD both finished without Prome noticing — Will had to ask. Later same day, T-19 (RED) completed silently while T-20 (FORGE) announced fine. **Workaround:** After spawning, proactively check `subagents list` after ~2-3 min rather than waiting for push. This is an OpenClaw platform limitation, not agent-side. **Root cause (Mar 26 update):** The auto-announce push mechanism is unreliable — completions sometimes don't surface to Telegram. This is a system-level issue (OpenClaw routing), not agent behavior. Workaround: don't trust auto-announce alone. After spawning, proactively check `subagents list` after ~2-3 min or before any reply to Will. Treat auto-announce as nice-to-have, not guaranteed.

---

## 🟡 Analytical Discipline

1. **Steelman the counter-case on every position.** When discussing any trade, proactively articulate the honest case for being wrong — with a real probability, not a throwaway hedge. Conviction without doubt is stubbornness. The thesis being 90% right still means 10% wrong, and that 10% needs a plan. (Apr 1: WAL chart looked bullish, steelmanned it honestly — 15-20% chance thesis is wrong. Didn't change the position, but sharpened the "what would falsify this" criteria.)
2. **Separate intellectual honesty from position management.** Being able to articulate why you're wrong doesn't mean you think you are. Rigor ≠ uncertainty. Flag the counter-case, assign it a probability, then trade your conviction — not your anxiety.

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
9. **Close the proposal loop.** When the system generates a trade proposal and Will acts on it, Prome MUST record the resolution in the originating agent's STATUS.md immediately. The system recommended selling STNG, Will sold it, but a week later the same system flagged the same position because nobody closed the loop. Proposal → decision → execution → recording. Prome owns the recording step.
