# PROME → DAEDALUS: NISABA v3 — I edited your build file (FYI, no action owed)

**Date:** 2026-10-18 15:2x ET · **Authority:** Will, in PROME's window 15:13 ET ("cant you just edit it in DAEDLUS folder?") · **Class:** info

`agents/nisaba/agent.md` edited and `console-panel-nisaba.yaml` regenerated with your `render_console_panel.py` (round trip OK). Live agent updated to **v3** through the API (`agents.update`, pinned to version 2; verified system == file, tools and model unchanged). Before the edit, live v2 == file, so no Console-only change was overwritten.

Changes:
1. Rule 10 gains one sentence: the GitHub repo below is the one exception.
2. New rule 11: offered inferences and unanswered questions live in `pending.md`, never only in the picture (PROME's 10/17 audit; NISABA had followed it since).
3. Memory section: `pending.md` line; boot read now profile + picture + pending.
4. New section **GitHub repo**: NISABA's own draft verbatim (session output `nisaba-repo-rule-draft.md`, sesn_01FyuRR9…), plus one PROME line: if the repo isn't mounted, say so once and carry on.

Context: Will created private repo `williepowen-debug/nisaba-memory`; token scoped to it, Contents + Issues R/W, no Workflows/Admin. NISABA refused to push under rule 10 as written — correct.
