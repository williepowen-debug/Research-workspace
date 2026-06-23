# SCOUT — Step-by-Step Build Spec

*Owner: WALTER (design) · Implementer: WALTER or DEWEY next session · Status: **PLAN — not built.** Saved 2026-06-22 PM at Will direction ("save the plan… write a step by step build"). Companion to `AGENTS/DEWEY/REVIVAL_PLAN.md` (Scout-track architecture). Grounded in a live read of the actual feed infra, not memory.*

---

## 0. GOAL (one sentence)

A GitHub Action on a cron runs the existing deterministic fetch scripts and **posts a digest to the WALTER+PROME Telegram group — and never commits to git.** Scout gathers raw candidates → WALTER triages + routes. No second router; no auto-commit-to-master friction. ("Git = shared brain, Telegram = cockpit.")

**Why this shape:** the old feeds died of *git friction*, not bad collection. Removing the git-write step entirely (post to Telegram instead) kills the failure class by construction. WALTER stays the single entry point — Scout only surfaces; it never routes or commits.

---

## 1. CURRENT STATE (verified 2026-06-22)

Three legacy collection systems exist; all are dark:

| System | Lives in | What it does | Why dark |
|--------|----------|--------------|----------|
| **news-sweep** | `FORGE/tools/news-sweep/` (`sweep.py` 23KB, `config.py` 22KB = 15 thesis RSS queries, `cron_sweep.sh`) | M-F 8:30am ET: fetch thesis-tagged Google-News RSS → `latest.md`/`latest.json` → optional `--route` to inboxes → curl Telegram summary | Ran on the **OpenClaw VPS cron** (`/home/moltbot/.openclaw/...`); VPS down since ~mid-May |
| **filing-watch** | `FORGE/tools/filing-watch/` (`poll_edgar.py` 8KB, `watchlist.yml`, `seen_filings.json`) | Polls SEC EDGAR submissions API for high-signal forms (10-K/Q, 8-K, NT, Form 4, SC 13D/G) on watched CIKs → `latest.md` | Same VPS, same outage |
| **SENTRY** | `.github/workflows/feeds.yml` → `scripts/fetch_feeds.py` → `SIGNALS/inbound.md` | GitHub Action, twice-daily RSS/Atom (EIA Today-in-Energy + EDGAR getcurrent) → **git add/commit/push to master** | **Deliberately disabled 2026-06-02** by Will/Prome — the auto-commit-to-master was the friction. `workflow_dispatch`-only now. |

**Decision (from REVIVAL_PLAN, Will 6/20):** revive **news-sweep + filing-watch**; leave **SENTRY dead** (its commit-push model is exactly what we're replacing). Scout = one new Action that runs the news-sweep + filing-watch scripts and posts — replacing both the dead VPS cron AND the disabled SENTRY workflow.

**🔴 Security finding (live read):** `FORGE/tools/news-sweep/cron_sweep.sh` contains a **plaintext bot token** `***REMOVED***:AAEf4...PuY8k` — it is committed, so it's in git history and must be treated as **compromised**. The old cron also posted to Will's **DM** (`chat_id 8463631023`), not the group.

---

## 2. PREREQUISITES — WILL'S STEPS (the actual blockers; do these first)

1. **Rotate the feeds bot token.** In BotFather, `/revoke` the old token for bot `***REMOVED***` (or create a fresh dedicated "Scout/feeds" bot). The old token is in git history → dead it. *(History scrub of the old token is optional/separate — rotation makes it harmless; a full `git filter-repo` history rewrite is a heavier, fleet-coordinated job, not required to ship Scout.)*
2. **Add the new token as a GitHub repo Secret** named `SCOUT_BOT_TOKEN` (Settings → Secrets and variables → Actions → New repository secret). Never in YAML.
3. **Add the Scout bot to the WALTER+PROME Telegram group** + capture the **group chat_id** (the 6/17 group; confirm the exact id via `getChat` or the access config — do NOT reuse the DM id, and do NOT trust an OCR'd value, per the 6/17 chat_id lesson). Store the chat_id as a second Secret `SCOUT_CHAT_ID` (or a non-secret repo Variable — chat_ids aren't secret, but a Secret keeps it out of the YAML).
4. **Authorize WALTER to touch `.github/workflows/` + `FORGE/tools/`** (shared infra, outside WALTER's normal commit scope — same per-instance auth as the 6/22 FORGE/Cushing edit). Or hand the build to PROME.

---

## 3. BUILD STEPS — WALTER (once §2 is done)

### 3a. Pin the scripts as the data-pull library
- **v1 (recommended, minimal):** run the scripts **in place** — `FORGE/tools/news-sweep/sweep.py` + `FORGE/tools/filing-watch/poll_edgar.py`. No move; fastest path to a working Scout.
- **v2 (later cleanup, per the DEWEY consolidation):** `git mv` the fetch scripts under `AGENTS/DEWEY/scripts/` so DEWEY is the single data-pull home (it already holds `edgar_fetch.py`/`fred_pull.py`/`edgar_doc.py`/`pdf2text.py`). Defer — it's a refactor touching FORGE + DEWEY, not needed to ship.

### 3b. Make the run "no-git, post-only"
- Run `python3 sweep.py --compact` **without `--route`** (—route writes to agent inboxes = file writes we don't want from CI). Capture stdout = the digest.
- Run `poll_edgar.py` similarly → capture its new-filings digest.
- **The Action does ONE outward action: `curl` the combined digest to the group via `sendMessage`.** No `git add/commit/push` anywhere. (This is the whole point — contrast feeds.yml's commit step.)

### 3c. Persist dedup across ephemeral runners
- The scripts dedup via `.cache/`/`seen_filings.json` on a persistent host; GitHub runners are ephemeral. Use **`actions/cache`** to restore+save the seen-sets (`news-sweep/.cache/`, `filing-watch/seen_filings.json`) keyed on a stable key (e.g. `scout-seen-v1`). Cache, **not** a repo commit (no `seen.json` churn). Accept that a cache miss = one day of possible re-surfacing (harmless; WALTER dedups again at triage via BOARD-grep).

### 3d. The Action YAML (`.github/workflows/scout.yml`) — skeleton
```yaml
name: Scout Feed Digest
on:
  schedule:
    - cron: '0 12 * * 1-5'   # 12:00 UTC = 8:00am EDT, M-F (revisit for EST→13:00)
  workflow_dispatch:          # manual test-fire / on-demand
permissions:
  contents: read              # READ ONLY — Scout never writes to the repo
jobs:
  digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Restore dedup cache
        uses: actions/cache@v4
        with:
          path: |
            FORGE/tools/news-sweep/.cache
            FORGE/tools/filing-watch/seen_filings.json
          key: scout-seen-v1-${{ github.run_id }}
          restore-keys: scout-seen-v1-
      - name: Install deps
        run: pip install feedparser pyyaml requests
      - name: Run news sweep
        id: news
        run: echo "out<<EOF" >> $GITHUB_OUTPUT; python3 FORGE/tools/news-sweep/sweep.py --compact >> $GITHUB_OUTPUT; echo "EOF" >> $GITHUB_OUTPUT
      - name: Run filing watch
        id: filings
        run: echo "out<<EOF" >> $GITHUB_OUTPUT; python3 FORGE/tools/filing-watch/poll_edgar.py >> $GITHUB_OUTPUT; echo "EOF" >> $GITHUB_OUTPUT
      - name: Post digest to Telegram group
        env:
          TOKEN: ${{ secrets.SCOUT_BOT_TOKEN }}
          CHAT:  ${{ secrets.SCOUT_CHAT_ID }}
        run: |
          MSG=$(printf '🔭 *Scout digest* %s\n\n*News*\n%s\n\n*Filings*\n%s' \
            "$(date -u +%Y-%m-%d)" "${{ steps.news.outputs.out }}" "${{ steps.filings.outputs.out }}" | head -c 4000)
          curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
            -d chat_id="${CHAT}" --data-urlencode "text=${MSG}" -d parse_mode=Markdown
```
*(Skeleton — harden in build: the `$GITHUB_OUTPUT` heredoc capture needs the real multi-line-safe form; large digests may need chunking >4096 chars; consider posting news + filings as separate messages.)*

### 3e. EIA / Cushing fold-in (natural, since the EIA fetcher now exists)
- The 6/22 EIA work (`FORGE/tools/market-data/fetch.py::eia_fetch`) means Scout can also post the **weekly WPSR Cushing print** on Wednesdays. Add a third step that pulls Cushing (via the dashboard or a thin script) and appends "🛢️ Cushing: XX.XM (zone)" to Wednesday digests. Optional v1.1 — needs `EIA_API_KEY` as a Secret too (mirror of the gitignored `.env`).

### 3f. Cadence + delivery to WALTER
- Once daily pre-market (~8am ET) + `workflow_dispatch`. Not twice-daily.
- Output posts to the group → **WALTER reads it at boot/step-7c as another intake source** (alongside DM, images) → triages + routes through the normal pipeline. Scout never writes BOARD/route_log — WALTER does, after triage. (Wire Scout's group post into WALTER step-7c the same way the cron `latest.md` files were consumed.)

---

## 4. SECURITY & FAILURE-MODE REVIEW (self-red-team)

- **Token exposure:** old token compromised (git history) → §2.1 rotation is mandatory before any wiring. New token only ever in a Secret; `permissions: contents: read` means even a compromised workflow can't push.
- **No-git guarantee:** the Action has zero `git` write steps and read-only `contents` permission — structurally cannot create the merge friction that killed the old systems.
- **Idempotency / spam:** `actions/cache` dedup + WALTER's BOARD-grep at triage = double dedup; a cache miss degrades gracefully (one day of possible repeats, not a failure).
- **Rate limits:** Google-News RSS + EDGAR are unauthenticated/lenient at once-daily; EDGAR needs the declared User-Agent (the `edgar_doc.py` UA lesson — `poll_edgar.py` already sets one; verify before relying).
- **Failure handling:** if a fetch step errors, still post what succeeded (don't fail silently); a fully-empty/failed run should post "Scout: no items / fetch error" so silence ≠ ambiguity. Add `continue-on-error` per fetch step.
- **Secret in logs:** never `echo` the token; pass via `env:` only (as in the skeleton).
- **Group vs DM:** must post to the group chat_id, not the old DM id — confirm the id (don't OCR it).

---

## 5. ACCEPTANCE CRITERIA (how we know it's done)

1. `workflow_dispatch` test-fire posts a well-formed digest to the WALTER+PROME group (news + filings sections).
2. Zero commits to the repo from the Action (verify `git log` shows nothing from GitHub Actions).
3. A second run within the same day surfaces no duplicate items (cache dedup working).
4. Old token revoked; no plaintext token anywhere in the working tree (the `cron_sweep.sh` token is rotated/dead).
5. WALTER step-7c updated to consume the group digest as an intake source.

---

## 6. OPEN DECISIONS (small, can default)

- **Scripts in place (v1) vs moved under DEWEY/scripts (v2)?** → default v1 (in place) to ship; v2 cleanup later.
- **Chat target Secret vs Variable for chat_id?** → default Secret (keeps YAML clean); chat_ids aren't truly secret.
- **EIA/Cushing in v1 or v1.1?** → default v1.1 (ship news+filings first).
- **Keep SENTRY `feeds.yml`?** → delete or leave inert; recommend leaving it `workflow_dispatch`-only and unused (don't spend effort killing it).

---

## 7. OWNERSHIP / COMMIT NOTES

- Touches `.github/workflows/` (new `scout.yml`) + `FORGE/tools/` (read scripts; maybe a small `requirements`) — **shared infra, needs explicit Will auth or PROME coordination** (same posture as the 6/22 FORGE/Cushing edit).
- The build itself commits the YAML once (a one-time infra commit) — that's a normal commit, NOT the recurring auto-commit that caused friction. The *recurring* Scout runs never commit.
- Coordinate the bot-to-group + Secret with whoever owns the Telegram plugin/group (Will). DEWEY may be the better implementer if the v2 script-consolidation is done at the same time.

---

*Resume cold from this file. The architecture is settled (REVIVAL_PLAN + this spec); the gating path is §2 (Will's token/Secret/bot/auth steps), then §3 (WALTER/DEWEY builds), then §5 acceptance.*
