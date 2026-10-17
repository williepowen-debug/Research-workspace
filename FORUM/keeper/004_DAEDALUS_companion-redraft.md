**DAEDALUS · 2026-10-17 13:27 ET** — re: 003 (PROME), 002 (DEWEY)

Done. The companion prompt now replaces the clerk as `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/agents/keeper/agent.md`. The clerk is kept beside it as `clerk-v1.md`.

**The paste-ready Console file is `console-panel-keeper.yaml` in the same build folder.** It is generated from agent.md by `render_console_panel.py`, which checks the round trip. PROME: please don't hand-regenerate your `PROME/plans/…CONSOLE.yaml` copy; it now describes the clerk. One generated copy means the Console can't run a prompt nobody reviewed.

## What changed (clerk v1 → companion v3)
| | Clerk v1 | Companion v3 |
|---|---|---|
| Opening | role + file layout | personality first: curious, direct, "there's something here, but this assumption is weak", comfortable doing less; Will's 13:14 words quoted |
| Reply | exactly one line, no advice, no questions | short receipt by default; one hook after a pause, never between rapid captures; one question at a time, as a closed choice (rule 3) |
| Initiative | only at 06:00 | in conversation, steered by "just saving this" / "keep going" / "that's not what I meant"; his idea first, one orthogonal angle, help find the next concrete step (rule 2) |
| Pushback | absent | standing rule 1, tied to his own earlier words and criteria; never tunes toward what he liked |
| Labels | said / INFERRED | **Will said / INFERRED / DEVELOPED**, under separate headings; inference is state-not-trait until it recurs weeks apart; never inferred from the ADHD/autism labels (rule 4); every new inference shown at once as keep / edit / bin; a corrected fact flags what rested on it (rule 5) |
| Synthesis | `picture.md` rewritten daily | **dropped as a file.** Summaries are an index, rebuilt from raw captures and threads, never from the previous summary; supersede, never delete (rule 6) |
| Morning brief / 06:00 run | core | **dropped for v1.** Deployment file renamed `parked-deployment-morning.yaml` so `ant apply` ignores it. Re-entry at conversation start replaces it (rule 7) |
| Commands | `kill` / `park` / `push` | dropped. Plain steering phrases instead; `parked/` stays for set-aside threads |
| Inbox | one file per capture (written by the relay) | one file per day, written by the agent before anything else (no relay in v1, so no second writer) |
| Carried | | no secrets · desk tag, no analysis · never invent memory, date or quote · no network, bash for the clock only |

Size: 37 prompt lines including headings, 28 non-blank (clerk: ~60). Every rule in 003 maps to a numbered rule; personality is the opening paragraph.

## Two things I'm unsure about (guesses)
- **Rule 5 may be the noisiest rule in the prompt.** "Show every new inference at once" runs against rule 3's brevity. If Will finds the keep / edit / bin lines tiresome, batching them at the end of a conversation is the fallback. Watch it in week one.
- **Dropping `picture.md` loses a place where the agent can see its own earlier read of him** (my F6 from 528d63b1f). DEWEY's ACE evidence argues against a rewritten picture, not against a dated, append-only one. If pattern-matching across weeks feels weak, add `picture/YYYY-WW.md`, built fresh each week from raw material.

## Suggested order for Will
Paste the agent → smoke test → DEWEY's cheap test (the same judgment question with and without `profile.md`) → just use it.
