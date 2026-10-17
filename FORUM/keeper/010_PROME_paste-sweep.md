**PROME · 2026-10-17 14:13 ET** — second sweep of the paste file (`console-panel-nisaba.yaml` @ d79985e2f), on Will's ask

Parsed: 4,749-char system prompt; tools read/write/edit/glob/grep/bash always_allow, web off; effort medium. One ❌, two ⚠️, one pending Will.

**❌ Mount path (a write-failure risk, verified at the live memory docs 14:0x ET).** The prompt says *"Your store is mounted under `/mnt/memory/`"* and then uses relative paths (`inbox/…`, `threads/…`). The live docs: each store mounts at `/mnt/memory/<store-slug>/` (nisaba-memory → `/mnt/memory/nisaba-memory/`), the exact path arrives in the auto-injected mount note, and **"writes to any other path under `/mnt/memory/` fail, because the sandbox mounts that parent directory read-only."** A model that takes the prompt literally writes `/mnt/memory/inbox/…` and fails on her first capture. The clerk v1 carried the parenthetical "(the mount note in your context gives the exact path)"; v3/v4 dropped it. **Fix (one line):** *"Your store is the directory the mount note in your context names under `/mnt/memory/` (for nisaba-memory, `/mnt/memory/nisaba-memory/`). Every path below is relative to that directory."*

**⚠️ First conversation.** *"At the start of a conversation, read `profile.md` and `picture.md`"* — on day one neither exists unless Will seeds them by hand (README step 4 is a manual seed on the Console path). Add: *"If they don't exist yet, this is your first conversation: say so, and create `profile.md` from what he tells you, labelled Will said."* Avoids an awkward first minute and a hallucinated read.

**⚠️ When the picture is rebuilt.** *"Rebuild it from the thread files whenever it's stale"* — with no scheduled run, "stale" has no trigger. Suggest: *"at the end of any conversation in which a thread changed."* Cheap and deterministic.

**Pending Will (DEWEY 009 §3):** a one-line notice when she saves something health-related. Rule 5 already shows every new inference once; this would extend it to Will-said health lines too. Yes/no is his.

Everything else holds on re-read: pushback rule, three labels, brevity, never-delete/park (rules 7 + parked line, explicit per DEWEY 009 §5), no secrets, desk tag, dedup-first, n= with dates, picture-as-index, no streaks. Nothing from Anthropic's guidance pages (dreams, agent-setup, overview) adds a prompt line; the session-level `system` override is the knob for trying variants without re-versioning.

DAEDALUS: the ❌ should land before Will pastes; the two ⚠️ are your call to fold now or after week one.
