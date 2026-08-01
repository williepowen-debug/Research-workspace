# STUE inbox — conventions

**Created 2026-07-31, Will-ruled.** STUE is the **first sub-agent in the fleet with an inbox** — all seven were previously write-only upward.

**Full path for senders:** `AGENTS/CARL/sub_agents/STUE/inbox/`

---

## Why it exists — two real instances, not a theory

1. **DEWEY's FHA/VA work (2026-07-24)** established the strongest student-loan transmission bridge in the book. It went to CARL and **had nowhere to land in STUE.** STUE carried `0/0/0` FHA mentions for a week while its transmission section was 100% credit-cards — the channel the *same* DEWEY packet had shown to be second-order. STUE got the demolition and not the replacement.
2. **PROME had a message for STUE and had to fold it into CARL's** (Will, 7/31). Same failure, caught prospectively.

## Format

Plain `.md` packets, same convention as CARL's inbox:

```
YYYY-MM-DD_from-<SENDER>_<short-kebab-subject>.md
```

⚠️ **NOT the Direct-Messaging v1 coded route.** DM v1's `MSG-*.md` semantics are allowlisted to **PROME → BRENT** and **PROME → SAM** only. **Do not send STUE a `MSG-*` packet expecting v1 processing** — it will be read as an ordinary packet.

## For senders

- **Send domain material directly.** STUE owns federal student loans (delinquency, default, SAVE→RAP, servicers, collections, borrower defense) plus — **since 7/31** — **student-loan ABS/SLABS** (collateral-transmission question only) and **higher-ed institutional stress**.
- **CARL remains the system of record** for CRL-04/05/13/14. Threshold/prediction changes still route through CARL; STUE proposes, CARL disposes.
- **Commit your packet** (root carve-out ①) — an uncommitted packet never arrives and nobody is told.
- ⚠️ **STUE boots infrequently — roughly 5× per quarter, and only when spawned or launched directly.** If something is time-critical, **send it to CARL as well** and say so in the packet. This is a real property of the channel, not a disclaimer.

## For STUE

- **Read at every boot — normal AND spawned-mode** (it is on the spawned-mode boot card, because a scoped spawn is exactly where an inbox scan gets skipped).
- Integrate, then `git mv` the packet to `inbox/processed/`. **`git mv`, never bash `mv`** — bash leaves a dangling deletion in the shared index.
- **Any packet found here is by definition unprocessed** — there is no "seen but deferred" state. If you cannot action it this session, write a dated PARKED note in `STATUS.md` rather than leaving it silently sitting.
- **⚠️ AGE IS A FINDING, NOT JUST A FACT.** Because STUE boots rarely, a packet can sit for weeks while looking delivered to the sender. **At boot, check the age of everything here.** A packet older than ~30 days means the sender has been operating on the assumption STUE knew something it did not — **tell them.** That correction is worth more than the packet's original content.

> **The design risk this file exists to name:** an inbox nobody reads on a cadence is a **worse** failure than no inbox, because it *presents* as a live channel while silently absorbing mail. STUE flagged that risk when it proposed the options; Will ruled for the inbox anyway, which is the right call — **but the age check above is the mitigation, and it is not optional.**
