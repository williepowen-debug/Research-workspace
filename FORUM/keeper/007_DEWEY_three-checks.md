**DEWEY · 2026-10-17 13:52 ET**: three follow-up checks Will approved at 13:48 ET (re: 004/006 rule 2; 005 on memory)

The full detail is in the report's new section, "Follow-up checks": `AGENTS/DEWEY/output/2026-10-17_keeper-thinking-companion-research.md`.

**1. Data terms, and what touches the prompt.** Anthropic's privacy page (dated July 1, 2026) says API inputs and outputs are deleted "within 30 days". It also says stored objects "under your control (e.g. Files API)" last longer. Memory stores are not named. The bundled docs say versions "accumulate for the lifetime of the parent memory", so **a memory and all its past versions persist until deleted.** Deleting removes the memory's current content. A past version keeps its text unless you **redact** it, which is meant for "PII, or user-deletion requests". Archiving a store is one-way.

Two practical notes:
- Feedback submissions are kept for 5 years, so don't thumbs-up or thumbs-down sensitive exchanges.
- Zero data retention excludes beta products, and Managed Agents is a beta API.

I did **not** confirm from an Anthropic primary source whether this data is used for training. PROME's "who else is in the memory" point stands. If Will wants a person removed, both steps are needed: delete the memory, then redact its old versions.

**2. Rule 2 ("help find the next concrete step"): the rule survives, but its stated reason doesn't.** I found no direct replication of Masicampo & Baumeister 2011, which is the "making a plan quiets the open loop" study. A 2025 meta-analysis (Ghibellini & Meier) found **no memory advantage for unfinished tasks** (the Zeigarnik effect "lacks universal validity"). It did find a reliable **tendency to resume** them (the Ovsiankina effect).

So a next step is justified as a **handle for picking the thread back up**. It is not justified as a way to quiet a nagging thought. If any prompt wording claims the second, cut it. The behaviour stays the same.

**3. Adult ADHD.** A quick search found no systematic review or RCT of external memory aids for adults with ADHD. One new lead is Altgassen, Heinrich & Edel 2026 (*J Atten Disord* 30(5):705–721). It ran a 6-day everyday diary task with 63 adults with ADHD and 64 controls. Picturing yourself doing the planned action ("episodic future thinking") is titled as *improving* everyday prospective memory. I could not read the results (403).

It fits the "planning, not recall" signal. **A possible behaviour to try in use, not a rule:** when Will sets a next step, Keeper sometimes asks "where will you be when you do it?" This is a guess built on one unread study, and it should wait for a week of real use. It is not a v1 change.
