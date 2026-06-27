---
name: finding-gitignored-private-drop-boot-surfaced
description: "User-private data drops (broker/account exports) should be gitignored AND boot-surfaced — gitignore keeps them off the shared repo but also hides them from git status, so a boot-card line is the only discovery path. Privacy and discoverability are a matched pair; do one without the other and you either lose the data or leak it."
metadata:
  node_type: memory
  type: finding
  originSessionId: 03e2af53-35da-49ec-be1d-20ad4806a175
---

When an agent accepts **user-private data drops** into its tree (broker CSVs, account exports, screenshots), gitignore the raw files so they never push to the shared/GitHub repo — account numbers, balances, and full fills do not belong in synced version control. But gitignoring has a hidden cost: the files become **invisible to `git status`**, so a fresh drop can sit unnoticed indefinitely (the normal "what changed?" scan won't show it).

**The fix is a matched pair:** pair the gitignore with an **out-of-band surfacing** — a boot-card line that counts/lists the drop folder (e.g. `boot.py` reading `inbox/WILL/` and printing "N file(s) awaiting review"). Gitignore alone → the data is silently missed. Surfacing alone → the data leaks to origin. You need both.

**Concrete instance:** TERRY `inbox/WILL/` drop zone, 2026-06-27 (built at Will's request for dropping trading results). `.gitignore` ignores `inbox/WILL/*` except `README.md` + `.gitkeep`; `boot.py` surfaces the count. Verified by dropping a test CSV: `git check-ignore` confirmed it stays local, the boot card listed it. Consumed drops move to a local (also-gitignored) `processed/` so the active count returns to 0. First real drop (a 520-row Robinhood export) flowed through cleanly: parsed in-place, analysis committed, raw never tracked.

**Generalizes:** any gitignored-but-operationally-important path — if you gitignore something you still need to *act on*, give it a non-git discovery path (boot card, dashboard line, periodic check) or it goes dark. The same blind spot applies to runtime caches, generated reports, and `.cache/` dirs that occasionally hold something you need to notice.

Related: [[feedback-ocr-verify-input-first]] (verify screenshot/paste/export input before trusting it), [[finding-push-train-pattern]] (committed work syncs via others' pushes), [[feedback-agent-git-isolation]] (commit only your own files).
