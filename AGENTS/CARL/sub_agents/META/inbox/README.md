# META inbox — conventions

**Created 2026-08-03, Will-ruled 2026-08-02** — every CARL sub-agent gets an inbox (DOC, GIG, PHAN, POLLY, POP, META joining STUE, which was first on 7/31). The layer was previously **write-only upward**: sub-agents could report to CARL but nothing could reach them except through CARL as letterbox.

**Full path for senders:** `AGENTS/CARL/sub_agents/META/inbox/`

**META's domain:** Methodology — the sub-agent build pattern, research-digest harvesting, cross-sub-agent process rules.

**Current mode:** **FROZEN 2026-07-10** (WP-2). `RESEARCH_DIGEST` was harvested to `AGENTS/DAEDALUS/reference/`. **Do not spawn.**

---

## Format

Plain `.md` packets, same convention as CARL's inbox:

```
YYYY-MM-DD_from-<SENDER>_<short-kebab-subject>.md
```

⚠️ **NOT the Direct-Messaging v1 coded route.** DM v1's `MSG-*.md` semantics are allowlisted to **PROME → BRENT** and **PROME → SAM** only. A `MSG-*` file dropped here is read as an **ordinary packet** — it gets no v1 processing.

## For senders

- **Send domain material directly** — you no longer have to route it through CARL and hope it gets relayed.
- **CARL remains the system of record** for parent-owned thresholds and CRL-* predictions. META covers no data rows; META owns process, not evidence, but **META proposes, CARL disposes** — threshold and prediction changes still route through CARL.
- **Commit your packet** (root `CLAUDE.md` carve-out ①) — an uncommitted packet never arrives and nobody is told.
- ⚠️ **Boot-cadence honesty: META is **FROZEN and is not spawned at all.**** If your material is time-critical, **send it to CARL as well and say so in the packet.** This is a real property of the channel, not a disclaimer.

🔴 **Read the warning below before sending anything here.** META is frozen with an explicit do-not-spawn instruction, so a packet placed in this inbox has **no scheduled reader whatsoever**. It exists because Will ruled the whole layer symmetric. If your material is methodology that needs to reach someone, **send it to DAEDALUS** (which inherited META's digest) **or to CARL** — not here. Use this inbox only for material that is genuinely fine to sit indefinitely until META is someday unfrozen.

## For META

- **Read at every boot — normal AND spawned-mode.** This goes on the spawned-mode boot card too, because a scoped spawn is exactly where an inbox scan gets skipped.
- **Anything present here is unprocessed by definition.** There is no read-cursor and no "seen but deferred" state — nothing to rot. If you cannot action a packet this session, write a dated PARKED note in your `STATUS.md` rather than leaving it silently sitting.
- Integrate, then `git mv` the packet to `inbox/processed/`. **`git mv`, never bash `mv`** — bash leaves a dangling deletion in the shared index.
- **⚠️ AGE IS A FINDING, NOT JUST A FACT.** Because this agent boots infrequently, a packet can sit for weeks while *looking* delivered to the sender. **At boot, check the age of everything here.** Anything older than ~30 days means the sender has been operating on a false assumption about what you know — **telling the sender outranks actioning the packet.**

> **The design risk this file exists to name:** an inbox nobody reads on a cadence is a **worse** failure than no inbox, because it *presents* as a live channel while silently absorbing mail. STUE flagged that risk when it proposed the options on 7/31; Will ruled for the inbox layer anyway, which is the right call — **but the age check above is the mitigation, and it is not optional.**
