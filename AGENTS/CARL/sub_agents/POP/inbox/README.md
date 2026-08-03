# POP inbox — conventions

**Created 2026-08-03, Will-ruled 2026-08-02** — every CARL sub-agent gets an inbox (DOC, GIG, PHAN, POLLY, POP, META joining STUE, which was first on 7/31). The layer was previously **write-only upward**: sub-agents could report to CARL but nothing could reach them except through CARL as letterbox.

**Full path for senders:** `AGENTS/CARL/sub_agents/POP/inbox/`

**POP's domain:** Small-business consumer-side stress — Subchapter V filings, NFIB survey internals, owner-income destruction.

**Current mode:** **DOSSIER-MODE** — DEMOTED 2026-07-24 after its final refresh at the Sub-V-sunset gate. `STATUS.md` is bannered and its rows are **Apr-17 vintage — do not cite as current.**

---

## Format

Plain `.md` packets, same convention as CARL's inbox:

```
YYYY-MM-DD_from-<SENDER>_<short-kebab-subject>.md
```

⚠️ **NOT the Direct-Messaging v1 coded route.** DM v1's `MSG-*.md` semantics are allowlisted to **PROME → BRENT** and **PROME → SAM** only. A `MSG-*` file dropped here is read as an **ordinary packet** — it gets no v1 processing.

## For senders

- **Send domain material directly** — you no longer have to route it through CARL and hope it gets relayed.
- **CARL remains the system of record** for parent-owned thresholds and CRL-* predictions. POP covers the small-business rows behind V11, but **POP proposes, CARL disposes** — threshold and prediction changes still route through CARL.
- **Commit your packet** (root `CLAUDE.md` carve-out ①) — an uncommitted packet never arrives and nobody is told.
- ⚠️ **Boot-cadence honesty: POP is **dossier-mode and does not boot on a schedule.** It was deliberately demoted; expect no session unless something re-opens the domain.** If your material is time-critical, **send it to CARL as well and say so in the packet.** This is a real property of the channel, not a disclaimer.

⚠️ **Its final refresh resolved two predictions as MISSES** (P01 Ch-11 H1 +28% vs a >40% bar; P02 also missed) and fixed a **parent-sub monotonicity bug** (POP-P06 SBA default >5% at 50% sat under CRL-15 >6.5% at 65% — impossible in the pair). If you send material implying POP should be re-promoted, address those misses directly — the demotion was evidence-based, not neglect.

## For POP

- **Read at every boot — normal AND spawned-mode.** This goes on the spawned-mode boot card too, because a scoped spawn is exactly where an inbox scan gets skipped.
- **Anything present here is unprocessed by definition.** There is no read-cursor and no "seen but deferred" state — nothing to rot. If you cannot action a packet this session, write a dated PARKED note in your `STATUS.md` rather than leaving it silently sitting.
- Integrate, then `git mv` the packet to `inbox/processed/`. **`git mv`, never bash `mv`** — bash leaves a dangling deletion in the shared index.
- **⚠️ AGE IS A FINDING, NOT JUST A FACT.** Because this agent boots infrequently, a packet can sit for weeks while *looking* delivered to the sender. **At boot, check the age of everything here.** Anything older than ~30 days means the sender has been operating on a false assumption about what you know — **telling the sender outranks actioning the packet.**

> **The design risk this file exists to name:** an inbox nobody reads on a cadence is a **worse** failure than no inbox, because it *presents* as a live channel while silently absorbing mail. STUE flagged that risk when it proposed the options on 7/31; Will ruled for the inbox layer anyway, which is the right call — **but the age check above is the mitigation, and it is not optional.**
