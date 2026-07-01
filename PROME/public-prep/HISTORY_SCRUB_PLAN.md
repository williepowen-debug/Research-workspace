# History Scrub Plan (Track B) — go-public gate

**Owner:** Prome · **Created:** 2026-06-30 · **Status:** ✅ EXECUTED + VERIFIED 2026-06-30 (pass 2, final state `b01c0346` — see FINAL OUTCOME below). **Live remainder: Will flips repo public → Phase 5 post-flip verification.** Retained as the reusable history-scrub playbook (`[[finding_history_scrub_verify_by_content_not_pickaxe]]`); archive after Phase 5. *(Header corrected 7/1 — it still said PLANNING after execution.)*
**Goal:** rewrite git history to remove private/secret/unprofessional content from ALL commits, so the repo can flip PUBLIC as Will's Anthropic Fellows (Economics & Policy) portfolio piece.
**Parent:** [[project_public_prep_anthropic_fellows]] · Track A (readability) = DONE.

> ⚠️ This is the one genuinely destructive operation in our protocol. History rewrite changes **every commit SHA** and requires a **force-push over GitHub** (our source of truth). We treat it like a demolition: backup → read-only inventory → Will sign-off → ONE pass → verify → flip. Do it while the repo is **PRIVATE** (it has never been public, so there are **no forks/PRs/third-party clones** of the bad history — this de-risks it enormously).

---

## Recon findings (read-only, 2026-06-30) — all verified against the actual repo

- **Repo:** 3,467 commits · `.git` = 225 MB · 3,925 tracked files · single remote (`origin` → GitHub) · single worktree · **0 tags** · single machine (clean tree, 0/0 vs origin).
- **`git-filter-repo`: NOT installed** → Phase-0 prep step.
- **Two stale `origin/claude/*` branches** (`agent-system-review-6xhbl7`, `climate-economy-agent-t8xdwj`) are **fully contained in master** (0 unique commits) → safe to delete before the scrub.
- **`.venv/` was committed** = **7,735 objects** in history (now `.gitignore`d, 0 in tree) → the bulk of the 225 MB. Bloat removal = big size win, no content loss.
- **Current tree is clean of live-format secrets** (0 Google client-IDs, 0 private-key blocks, 0 AWS keys, 0 full telegram tokens).

### Secret-risk reassessment (sharper than the original "dead tokens + OAuth" framing)
| Item | Reality | In tree? | Action |
|---|---|---|---|
| **Google OAuth `client_secret` (`GOCSPX-…`)** | **The one genuinely-sensitive credential.** Lives in `tools/calendar/credentials.json` (2 commits). `flow_state.pkl` = pickled OAuth access/refresh tokens. **No record it was ever rotated → assume LIVE.** | no (history only) | **path-remove `tools/calendar/`** + **Will rotates/revokes the Google OAuth client** (independent of repo) |
| Telegram bot-ID `<dead-telegram-bot-id>` | Only the **public bot-ID half**; the secret `:AAAA…` half was **never committed** (0 hits). Bot already rotated dead (401). | yes, in 7 docs | cosmetic literal-replace (optional, recommended) |
| `CLAWDBOT_GATEWAY_TOKEN` | Value already **truncated to `<gw-frag>…`** in the docs that quote it; gateway decommissioned/dead. | yes, in docs | cosmetic literal-replace (optional) |
| Real `.env` files | **Never committed** — only `.env.example`. | n/a | none |

---

## THE MANIFEST

### Bucket A — path removal (whole files/dirs gone from ALL history)
1. **`WILL/trading-journal/`** — 5 files (3 trade-journal `.md` + 2 broker-photo `.JPG`). **Private financial.** *(Surgical: the REST of `WILL/` is legit portfolio material — keep in history.)*
2. **`tools/calendar/`** — 9 files: `credentials.json` (the `GOCSPX-` secret), `flow_state.pkl` (OAuth tokens), 7 auth scripts. **Secret + scaffold.**
3. **`.venv/`** — 7,735 objects. **Bloat** (compiled libs; no content value). Big `.git` size win.

### Bucket B — literal replacement (string → `***REMOVED***`, in files we KEEP)
*All DEAD/cosmetic — belt-and-suspenders, not load-bearing security:*
4. `<dead-telegram-bot-id>` (telegram bot-ID) → `***REMOVED***`
5. `<gw-frag>…` (gateway token fragment) → `***REMOVED***`
6. *(Belt+suspenders)* the `GOCSPX-…` value literal — though Bucket-A path removal already kills its only home.

### Bucket C — SUBJECTIVE "unprofessional" content → **RESOLVED 6/30: Will chose objective buckets only, subjective skipped (see C1)**
Candidates discussed (decision: skipped):
- The rest of `WILL/` in history (research, ideas, prompts, briefings, deck) — keep as portfolio material, or cut?
- **Commit messages** — many are candid/venting ("PROME: finally fix the damn…"-style). Scan + rewrite messages too, or leave?
- Any agent notes naming real third parties, personal frustration, or speculative/embarrassing analysis.
- Author identity / email in commits — fine to keep (it's Will's GitHub), unless he wants it scrubbed.

---

## ✅ PHASE 3 RESULT — VERIFIED IN SIDECAR (2026-06-30)

Ran on an isolated clone (live repo + GitHub untouched). One filter-repo pass: `--paths-from-file paths-to-remove.txt --invert-paths --replace-text replacements.txt`. **All targets = 0 across all history; keep-content intact.**

| Check | Result |
|---|---|
| `WILL/trading-journal/`, `tools/calendar/`, `.venv/`, `*.pyc`, `__pycache__` | **0** |
| `GOCSPX-` (real Google secret), `<dead-telegram-bot-id>`, gateway value | **0** |
| tracked files at HEAD | **3,925 (unchanged)** |
| README + essay + AGENTS/(2749) + FORGE/(204) | **all present** |
| commits | **3,467 → 3,465** |
| `.git` size | **225M → 132M** |

**Mid-run catch:** first pass left `<dead-telegram-bot-id>` in 1 binary blob — `dashboard/__pycache__/server.cpython-312.pyc` — because `--replace-text` skips binaries. Fixed by adding `*.pyc`/`__pycache__` path-removal (compiled bytecode never belongs in history). Re-verified clean.

**The only 2 pruned commits** were both **trading-journal-only** commits (`b47a7259` Mar-3 journal; `e2b6f24b` Jun-27 logs→photos) — i.e. they vanished *because* their whole content was the private data being removed. Longevity narrative intact.

**Status: rewrite logic PROVEN. The remaining steps (Phase 4) are the irreversible ones and need Will's explicit go.** *(As-of-6/30 mid-run snapshot — Phase 4 was executed same day with Will's go; see FINAL OUTCOME below.)*

---

## ✅ FINAL OUTCOME — scrub landed + double-check correction (2026-06-30)

**Pass 1** (Landing A) force-pushed `bec24b60 → 9b7d3290`. Then Will asked to **double-check everything** — which caught a real miss:

- **The catch:** content-sanity (reading the *rendered* edited lines, not just pickaxe counts) revealed `***REMOVED***:AAEf…` — the first replace-rule scrubbed the bot-**ID** but **left the dead token's 35-char secret half** (it had been hardcoded in the old `cron_sweep.sh`). `--replace-text` also skips **binary** blobs, so a `.pyc` had slipped earlier too (fixed in pass 1). Lesson: **verify by reading edited content + blob-level secret enumeration over kept history — not just known-target pickaxe.** → auto-memory candidate.
- **A red herring correctly avoided:** a 44-char `AAEf…DjM` base64 run in a Gemini research image *coincidentally* shares the `AAEf` prefix with the secret. Confirmed distinct (35 vs 44 chars); the research image blob is **byte-identical** post-scrub (hash `12e8497a`).
- **Thorough re-scan of kept history:** exactly ONE leaked token ever (the dead one); **zero** AWS/GitHub/Google/OpenAI keys; WALTER's **live** bot secret never leaked.

**Pass 2** (corrected, fresh from pristine backup, one clean rewrite) — replacement set = bot-ID `<dead-telegram-bot-id>` + real 35-char secret + gateway `<gw-frag>` + **live bot-ID `<WALTER-live-bot-id>`** (Will opted to scrub the live-infra fingerprint too). Force-pushed `9b7d3290 → b01c0346`.

**Final verified state (fresh GitHub clone):** all targets **0** across full history; broad credential sweep **0**; 3,465 commits / 3,925 files / README+essay intact; CASCADE image intact; fsck clean; fresh-clone == origin == local = **`b01c0346`**.

**Repo is clean and SAFE TO FLIP PUBLIC.** Pre-scrub mirror backup retained at `~/Research-workspace-PRESCRUB-BACKUP-20260630.git` **on the DESKTOP** (not present on the laptop — serial multi-machine, see `PROME/MACHINE_LOCAL.md`) until Will confirms public.

---

## PHASED PLAN *(Phases 0–4 EXECUTED 2026-06-30 — retained below as the reusable playbook; Phase 5 is the only live remainder)*

**Phase 0 — Prep & backup** *(no rewrite)*
- Install `git-filter-repo` (into `.venv` or as standalone script).
- **Full mirror backup:** `git clone --mirror . <off-tree backup>` (plus GitHub stays the untouched recovery point until we force-push).
- Confirm: clean tree, all agents idle, single machine. ✅ (verified)

**Phase 1 — Finalize manifest (Will-approved)**
- Buckets A + B are ready. Bucket C needs Will's criteria. Output: the approved removal list + replacement list.

**Phase 2 — Build the exact spec files** *(Will reviews these before any run)*
- `paths-to-remove.txt` → `git filter-repo --invert-paths --paths-from-file`
- `replacements.txt` → `git filter-repo --replace-text`
- (Optional) commit-message callback if Bucket C includes messages.

**Phase 3 — Sidecar rewrite + VERIFY** *(safest; live working dir untouched)*
- `git clone --no-local . <sidecar>` → run filter-repo there.
- **Verify:** re-run the SAME pickaxe/path searches → **expect 0 hits** for every Bucket A/B target; confirm KEEP content intact (README, essay, file count, recent commit msgs, analytical corpus); diff `.git` size (expect large drop from `.venv` removal).
- Will eyeballs the before/after summary.

**Phase 4 — Land it** *(the irreversible step — explicit Will go)*

Two landing options (the difference is what happens to old secret-bearing commits on GitHub's side):

- **Landing A — force-push (lighter):** push rewritten `master` from sidecar to origin `--force`; **delete the two stale `origin/claude/*` branches** (they still point at OLD, secret-bearing history — must go); then in the live working dir `git fetch` + `git reset --hard origin/master` to adopt. *Caveat:* GitHub retains the old unreachable commits accessible **by exact 40-char SHA** until its GC runs. Low risk here (repo never public → no outsider has those SHAs; secrets are dead/personal), but not a hard guarantee.

- **Landing B — delete + recreate GitHub repo (nuclear-clean, RECOMMENDED):** since the repo has **no forks / stars / issues / external refs** (never public), the cleanest guarantee is: Will deletes the GitHub repo, recreates it empty (same name), and I push **only** the scrubbed mirror. **Zero old SHAs survive anywhere.** Costs nothing we have. Then adopt in the live dir as above.

- Either way: **Will flips repo → PUBLIC** (GitHub settings / `gh`) only AFTER Phase-5 re-verification on a fresh clone.

**Phase 5 — Post-flip verification & independent cleanup**
- Fresh-clone the public repo → re-run secret searches → confirm clean.
- **Will rotates/revokes the Google OAuth client** if still live (repo-independent).
- Update state docs (SCRATCH/HANDOFF/ACTIVE_DECISIONS/project memory); mark Track B done.

---

## Safety rails (non-negotiable)
1. **Backup mirror exists before any rewrite.** GitHub = second recovery point (untouched until Phase 4).
2. **Sidecar rewrite** — never experiment in the live working dir.
3. **Verify-before-force-push** — 0-hit confirmation on every target + KEEP-content intact.
4. **One pass.** No iterative force-pushes against origin.
5. **Single-machine assumption held at execution (2026-06-30).** For any future reuse under the serial-multi-machine canon (7/1): close out + push the OTHER box first and leave it off — no other clone may pull mid-rewrite.
6. Repo stays **PRIVATE** until Phase 4 verification passes.

## Decisions needed from Will (gating) — ✅ ALL RESOLVED 2026-06-30
- **C1.** ~~"Unprofessional" criteria (Bucket C)~~ → **Will 6/30: objective buckets only, skip subjective.** *(`WILL/` trading-journal cut; Will separately deleted the rest of `WILL/` via web-UI 6/30.)*
- **C2.** ~~Commit messages?~~ → **Will 6/30: file contents only, not messages.**
- **C3.** ~~filter-repo install + mirror backup OK?~~ → **Approved + executed 6/30.**
- **C4.** ~~Google OAuth client rotation?~~ → **Will 6/30: OAuth already dead.**
