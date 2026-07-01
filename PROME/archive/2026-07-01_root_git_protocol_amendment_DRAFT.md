# DRAFT — Root CLAUDE.md Git Protocol amendment (serial multi-machine + git-cwd canon)
**Author:** PROME 2026-07-01 · **Status:** LANDED 2026-07-01 (Will-approved) — all three edits live in root `CLAUDE.md` via `dc2a0242`; follow-on mirror sweep complete. Archived 2026-07-01 (applied draft; retained for before/after wording provenance). Task 2 of the 7/1 machine-protocol package.

**What this fixes:** (1) the protocol's "single-machine operation" premise is stale — Will runs desktop ⇄ laptop serially (one at a time, close-out-push before switching), so a non-ff abort is usually *routine*, not a tripwire; (2) the git recipes assume repo-root cwd, and from an agent's own-dir launch cwd the mandatory pre-commit guard `git status -- AGENTS/<NAME>/` **silently false-passes** (pathspecs are cwd-relative) — found by the 7/1 18-reader audit across ~12 agent docs that mirror root canon.

---

## Edit 1 — replace the single-machine premise (Git Protocol intro)

**Current:**
> **Push is automated at closeout via `scripts/safe-push.sh`** (fast-forward-gated, fails safe) — predicated on **single-machine operation** (no VPS/laptop/web pushing; OpenClaw/VPS was cut 2026-06-26). safe-push never force-pushes and **aborts cleanly if origin has commits we don't** (the cross-machine case), so one agent's closeout push safely sweeps everyone's local commits — the push-train, now automated rather than gated on a manual Will window.

**Proposed:**
> **Push is automated at closeout via `scripts/safe-push.sh`** (fast-forward-gated, fails safe) — predicated on **serial multi-machine operation**: Will runs ONE machine at a time (desktop ⇄ laptop), closing out + pushing all agents before switching, so origin is always the handoff point (OpenClaw/VPS was cut 2026-06-26; machine-local infra inventory + switching checklist → `PROME/MACHINE_LOCAL.md`). safe-push never force-pushes and **aborts cleanly if origin has commits we don't**, so one agent's closeout push safely sweeps everyone's local commits — the push-train, now automated rather than gated on a manual Will window.

## Edit 2 — replace the non-ff tripwire language (Session-end step 3)

**Current:**
> **If safe-push aborts (non-ff), do NOT force — note it and flag Will.** A non-ff abort means origin diverged (a 2nd machine pushed) — the tripwire to switch to per-agent branches.

**Proposed:**
> **If safe-push aborts (non-ff), do NOT force.** First response: `git pull --rebase`, then re-push — under serial multi-machine this is **routine** (the other machine pushed since this clone last pulled). **Escalate to Will (per-agent-branches tripwire) only if** the rebase hits conflicts outside your own dir, or non-ff recurs mid-session — either means two machines ran simultaneously, which the protocol forbids.

## Edit 3 — NEW line at the top of "Before committing" (the git-cwd canon)

**Proposed (insert as step 0):**
> 0. **Run ALL git operations (and `scripts/safe-push.sh`) from the repo root:** `cd "$(git rev-parse --show-toplevel)"` first. Git pathspecs resolve relative to cwd — from an agent's launch dir (`AGENTS/<NAME>/`), `git commit AGENTS/<NAME>/<file>` fails loudly, but **`git status -- AGENTS/<NAME>/` silently shows nothing** (a false-clean pre-commit check). Every `AGENTS/<NAME>/…` recipe below assumes root cwd.

## Follow-on mirror sweep (after root lands — separate pathspec commits)

- `PROME/CLAUDE.md` + `PROME/BOOT.md` + `PROME/GIT_COORDINATION.md`: non-ff language ("2nd machine → flag Will") → align to Edit 2's routine-rebase framing.
- Auto-memory `feedback_defer_push_coordinate` (hook: "non-ff abort=2nd-machine flag") → rewrite body, keep slug.
- The ~12 agent docs whose closeout/git sections mirror the old canon verbatim (audit inventory: BRENT/BROCK/HAWK/RED/CARL/ORACLE/CORAL/MARCO/LABOR/VIOLET/OZK/YEYOU) inherit by pointer — no per-file edits needed once root states the cwd canon; their `safe-push.sh` references become correct-by-context.
- `AGENTS/DAEDALUS` packet already documents this class as PENDING-WILL — flip to APPROVED on landing.
