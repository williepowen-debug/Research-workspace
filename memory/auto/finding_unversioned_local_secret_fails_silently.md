---
name: finding_unversioned_local_secret_fails_silently
description: "A capability resting on an un-versioned local secret file is one clear/crash away from dead, and it fails QUIETLY — degrading to N/A or a generic auth error rather than saying \"the secret is gone.\" Check the local secret before debugging the service."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0eefedce-1876-483e-8cea-dbcf5083422f
  modified: 2026-07-27T15:42:22.529Z
---

Any capability whose credential lives in an un-versioned local file (`.env`, `~/.git-credentials`, `~/.netrc`, a keyfile) has a failure mode that is **silent by construction**: the file can be emptied, cleared, or lost with no error, no alert, and no artifact. The capability then fails with a message about the *service*, not about the *secret* — so debugging starts in the wrong place.

**n=2 on the same box, two months apart:**

| | What vanished | How it presented | What it actually was |
|---|---|---|---|
| 2026-06-23 | `FORGE/tools/market-data/.env` holding the EIA API key (gitignored, correctly) | the Cushing data source **degraded to `N/A`** — no error at all | the file was simply gone from disk |
| 2026-07-27 | the PAT in `~/.git-credentials` | `"Invalid username or token"`, then `"could not read Username"` | the file was **emptied** (0 lines) mid-session, ~1h after the last successful push |

In the second case the diagnosis was only settled by checking the file's **line count and mtime** — the token was not expired, it was *absent*, and the error message said nothing about that. An expired token and a missing token produce different fixes (renew vs re-add), so the distinction is not cosmetic.

**How to apply:**
1. **When a wired capability starts failing, check the local secret's existence, size and mtime BEFORE debugging the service, the network, or the API.** It is the cheapest check and it is disproportionately often the answer.
2. Diagnose without exposing the value: line count, mtime, permissions, character-set and length, and a **redacted** host line (`sed -E 's#//([^:]*):[^@]*@#//\1:<REDACTED>@#'`). Never print the secret to a transcript.
3. Prefer credential mechanisms that can be **interrogated** — a helper with a `status` command beats a bare plaintext file, because with a flat file there is no way to ask "am I authenticated?" except by attempting the operation and failing.
4. **Blast radius is usually wider than it looks.** The 7/27 git-auth failure had stranded **nine commits from five different agents**, including a live trade fill, not just the commits of the agent that noticed. On a shared repo, check the whole push train, not your own work.
5. If something clears such a file once, expect it again — write the recovery procedure down rather than re-deriving it.

Related: [[finding_gitignored_private_drop_boot_surfaced]] · [[project_automem_symlink_migration]] · [[finding_verify_runtime_context_before_tool_broken]] · [[finding_push_train_pattern]]
