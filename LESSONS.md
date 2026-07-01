# LESSONS.md — Mistake Patterns & Rules

*If you catch yourself breaking one, stop.*

**Updated:** 2026-06-30

---

## 🔴 Costly Mistakes

1. **Don't override conviction with probabilistic hedging.** Recommended closing the CVNA put before earnings — the stock then dropped 20%. Implied moves are consensus, not ceilings. Don't talk Will out of a position unless the THESIS is broken.
2. **Mechanical before creative.** Rolls, trims, expiries BEFORE new research threads. (The KRE roll got bumped by the oil thesis → never executed.)
3. **Deploy fresh capital only on a fired trigger — not the calendar.** Standing rule (Will, 2026-06-26): new capital goes in ONLY on a *sustained/fired* trigger, $500/card max-loss. A date on the calendar is not a trigger. (Auto-memory: `deploy_on_trigger_not_calendar`.)
4. **Deploy agents then wait.** If you spawn agents for a decision, wait for their outputs. If it's too urgent to wait, don't deploy — just decide.
5. **Puts on green days, calls on red days.** Default. Note when breaking it and why.
6. **Roll duration, don't trim size.** Expiry too short → roll to a later expiry. Trimming size = thesis broken. Rolling = timeline uncertain. (Sold HYG at $0.51 when HY OAS was 1bp from the trigger.)
7. **Two expiry frameworks — don't mix them.** PC single-name puts (APO, ARES, ARCC): dateable catalysts → May/Jun/Jul expiry. Macro/index (HYG, KRE, IWM): Hamilton demand-destruction → Dec expiry. BRENT owns the Hamilton clock; BROCK owns the PC catalyst clock.
8. **One spawn, one objective.** Don't bundle two distinct goals into one agent spawn — agent context is finite. (REGINALD P-002 bundled inbox processing + an EARNINGS_PREP upgrade — the inbox got done, the prep didn't move. Split into two proposals.)

---

## 🟡 Analytical Discipline

1. **Steelman the counter-case on every position.** When discussing any trade, proactively articulate the honest case for being wrong — with a real probability, not a throwaway hedge. Conviction without doubt is stubbornness. A thesis being 90% right still means 10% wrong, and that 10% needs a plan. (Apr 1: WAL chart looked bullish; steelmanned it honestly at 15–20% chance the thesis is wrong. Didn't change the position, but sharpened the "what would falsify this" criteria.)
2. **Separate intellectual honesty from position management.** Being able to articulate why you're wrong doesn't mean you think you are. Rigor ≠ uncertainty. Flag the counter-case, assign it a probability, then trade your conviction — not your anxiety.

---

## 🟡 Verification

1. **Agent data can be hallucinated.** Verify against SEC filings before trading. (PSEC PIK 35% → actual 8.6%.)
2. **Earnings dates** → company IR / SEC 8-K. (OZK wrong twice.)
3. **Prices** → pull live, never cite from a STATUS file.
4. **Test thesis against data, not data against thesis.**
5. **Verify a scrub by content, not just pickaxe.** During the 2026-06-30 git-history secret scrub, a grep/pickaxe pass looked clean — but pass 1 had removed only *half* a credential (the bot-ID, leaving the 35-char secret). Caught by reading the actual edited content + a blob-level secret enumeration. Grep answers "does this exact string still appear"; it does not answer "is the whole secret gone." (Auto-memory: `history_scrub_verify_by_content_not_pickaxe`.)

---

## 🟡 Process

1. **Read before editing. Always.** Never Edit without reading the file the same turn. Don't edit a file a subagent is actively updating.
2. **Boot sequence mandatory.** No shortcuts.
3. **Will's mid-session ideas → capture, don't execute.** Log to scratchpad, finish the current priority.
4. **Flag research opportunities during KB updates.** Don't just log data — say when deeper digging could yield edge.
5. **Flag LLM-inaccessible data for Will.** Google Trends, real-time dashboards, paywalled portals — don't let him waste time on prompts that return garbage.
6. **Major data releases → write a synthesis .md in the agent's domain folder.** Extract the 5 things that matter for positions. Agents wake with no memory; curated context > raw dumps.
7. **Dry-run prompts before batch deployment.** Agents catch file-path errors (missing KB.tsv), date errors (TIC Mar 18 not Mar 15), and context gaps you won't see from the outside.
8. **Inject confirmed data, don't re-search it.** Each batch of agents should receive findings from prior batches as confirmed context. Saves tokens, prevents conflicting data.
9. **Close the proposal loop.** When the system generates a trade proposal and Will acts on it, Prome MUST record the resolution in the originating agent's STATUS.md immediately. (The system recommended selling STNG, Will sold it, but a week later the same system re-flagged the position because nobody closed the loop.) Proposal → decision → execution → recording. Prome owns the recording step.
10. **Scoped git commits, never `git add -A`.** Agents stage only their own `AGENTS/<NAME>/` dir. A `git add -A` sweeps up other agents' uncommitted work and can push half-finished files. Stage only what you changed. (Apr 3: found 4 sessions of `git add -A` that could have pushed agent WIP.)
11. **`git pull` at boot.** Claude Code agents push to GitHub independently. Without pulling first, Prome reads stale agent STATUS files all session. (Apr 3: Prome had never been auto-pulling — added as step 0 of the boot sequence.)
12. **Audit your auto-loaded files regularly.** The genuinely auto-injected context is the auto-memory `MEMORY.md` index + the `CLAUDE.md` files (root + `PROME/`) — the most expensive real estate in the system, and entries go stale silently. (`HEARTBEAT.md`, `AGENTS.md`, `USER.md`, `KERNELS.md` are explicit boot-reads, NOT injected — audit them too, but they don't cost every message.) (Apr 3: found 6 stale entries, 3 duplicates, 5 missing file paths → ~30% context reduction after an audit.)
