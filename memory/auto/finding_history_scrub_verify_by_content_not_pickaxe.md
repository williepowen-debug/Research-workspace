---
name: finding_history_scrub_verify_by_content_not_pickaxe
description: history-scrub verify by reading edited content + blob-enumeration, not just known-target pickaxe; scrub the whole credential
metadata:
  type: feedback
---

When scrubbing secrets from git history (`git filter-repo --replace-text`), VERIFY by reading the rendered edited lines AND enumerating secret formats over all kept blobs — NOT just pickaxe-counting your known targets. A first pass that replaced a telegram bot-**ID** read 0 for the ID yet left the token's **secret half** exposed (`***REMOVED***:<secret>`); only content-sanity (reading the edited line) caught it. Will's instinct to "double-check everything" is what surfaced it.

**Why:** (1) `--replace-text` silently SKIPS binary blobs → a committed `.pyc` retained the token (remove compiled artifacts by PATH, same as `.venv`). (2) Replacing one part of a `<id>:<secret>` credential orphans the other half — scrub the WHOLE credential (both halves). (3) Known-target pickaxe can't find secrets you never catalogued; a `git cat-file --batch` sweep over kept blobs (excluding path-removed dirs) grepped for credential REGEXES (telegram `\d{8,10}:AA…`, `GOCSPX-`, `AKIA…`, `ghp_…`, PRIVATE KEY blocks) enumerates them. (4) A coincidental base64-image substring shared the secret's `AAEf` prefix — confirm distinct (length/ending) and prove the blob is byte-identical post-scrub before trusting it's untouched.

**How to apply:** after any history scrub run, in order: (a) read every edited line, not just match-counts; (b) blob-level format sweep over kept history; (c) full-credential (not half) replace rules; (d) path-remove binaries/compiled artifacts; (e) byte-identical blob check on any near-miss false positive; (f) final proof on a FRESH clone of the remote (what the public sees). Playbook + manifest: `PROME/public-prep/HISTORY_SCRUB_PLAN.md`. Related: [[project_public_prep_anthropic_fellows]] · [[finding_automem_hardlink_inplace_edit]].
