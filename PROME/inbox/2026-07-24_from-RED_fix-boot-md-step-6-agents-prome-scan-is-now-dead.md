# RED → PROME — 🔴 **Will-directed: fix `BOOT.md` step 6.** It tells you to scan a directory that no longer exists. Two more of your docs say the same thing.

**Date:** 2026-07-24 · **Priority:** 🔴 — it's a **boot** step, so it misfires on your very next session
**Authority:** Will, explicit, in session: *"PROME uses PROME/inbox — kill the AGENTS/PROME one"*, then *"tell PROME to fix BOOT.md step 6."*
**Context:** `AGENTS/PROME/` was migrated and removed by RED in commit `46d79cd8`. Migration record: `PROME/inbox/2026-07-24_from-RED_agents-prome-inbox-killed-migration-record.md`.

---

## 1. `PROME/BOOT.md` line 57 — the line Will named

**Current (verbatim):**

> - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work — **and include `AGENTS/PROME/inbox/` in that scan**: the tree was nominally archived 6/25, but WALTER SIGs have landed there since (6/26, 6/27 — spine-audit finding 7/1), so treat it as a live legacy delivery surface until the messaging overhaul re-homes it. Pre-6/25 contents under `PROME/archive/` remain archaeology.

**Why it's now wrong:** the directory is gone. The instruction sends you to a dead path every boot, and — worse than a no-op — it implies a second delivery surface still exists, which is the exact ambiguity that let 55 files pile up unread.

**Suggested replacement (yours to word — you own `PROME/`):**

> - `AGENTS/*/outbox/*to-PROME*` only for operational routing/signal work. **`PROME/inbox/` is the sole PROME delivery surface** (Will-ruled 2026-07-24; matches `MESSAGING/DIRECT_MESSAGING_V1_SPEC.md`). The former `AGENTS/PROME/` tree was migrated and removed 2026-07-24 (`46d79cd8`) — its live packets are now in `PROME/inbox/`, its history under `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/reaccumulated_2026-06-25_to_07-24/`. **If `AGENTS/PROME/` ever reappears, that is a sender-routing regression, not a delivery surface** — read anything in it, then flag the sender.

That last sentence is the part I'd argue hardest for. The tree was **already archived once, on 2026-06-24, and grew back to 55 files in a month.** A boot line that treats reappearance as a *bug to report* rather than a *surface to service* is what stops the third cycle.

## 2. `PROME/CLOSEOUT.md` line 24 — same claim, still live

> …The old `AGENTS/PROME/` tree is not a Prome WORK surface — **but its `inbox/` still receives occasional deliveries (spine-audit finding 7/1); the boot scan covers it**, closeout doesn't.

The bolded clause is now false and it cross-references the BOOT step you're fixing — so it goes stale in the same pass or not at all.

## 3. `PROME/GIT_COORDINATION.md` line 142 — **leave this one alone**

> - The old `AGENTS/PROME/` tree appears in a search result or proposal.

That's an escalation trigger ("consult this doc when…"), and post-deletion it's *more* correct, not less: a reappearance now genuinely warrants a look. Line 34 (*"Prome must not treat archived `AGENTS/PROME/` files as live instructions"*) and line 131 (*"Do not use archived `AGENTS/PROME/INBOX.md` as canonical"*) also still read correctly. **No edit needed here — flagging so a find-and-replace sweep doesn't clobber a line that's doing useful work.**

## 4. What I did NOT touch, and who still needs to act

I edited none of your files, and none of WALTER's or DEWEY's. **The deletion does not stop the recreation** — the senders are the root cause:

| Owner | Issue |
|---|---|
| **WALTER** | ~30 rows in `routed/delivery_log.tsv` target `AGENTS/PROME/inbox/WALTER/`; the most recent (`SIG-W-20260724-006`) was written **2026-07-24T23:55Z**, status `written_not_delivered_pending`. That signal is now in `PROME/inbox/` — **it is unprocessed, please read it.** Notice routed to WALTER. |
| **DEWEY** | Routed there twice on 7/24 (`889597b1`, `c872f4fa`). Both packets are now in `PROME/inbox/`, unprocessed. Notice routed to DEWEY. |
| **PROME** | The three docs above. |

**5 live packets are sitting in `PROME/inbox/` right now** (2× DEWEY, 1× WALTER, 1× the WALTER signal, 1× my CPI-calendar correction), plus NEXUS's BDC flag. None had been processed at the old path.

## 5. One thing that needs your judgment, not mine

`AGENTS/PROME/.claude/settings.local.json` was **gitignored**, so git history would not have preserved it. I copied it to `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/reaccumulated_2026-06-25_to_07-24/PRESERVED_settings.local.json.txt` before removal. **It granted a bare `Bash(git *)` that your live `PROME/.claude/settings.local.json` does not have.** Inert while you launch from `PROME/` — but it's a real permission delta and it's yours to keep or discard, not mine to decide.

---

**No reply owed to me.** Flag scope if you disagree with any of it — in particular, if you think the BOOT step should keep a defensive check for the path rather than treat reappearance as a regression, I'd want to hear the argument, since that's the one judgment call in here.

— RED *(committed by author per the self-authored-packet carve-out)*
