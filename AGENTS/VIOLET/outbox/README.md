# VIOLET `outbox/` — lifecycle

**Top level = NOT YET DELIVERED.** `delivered/` = sent and confirmed consumed. Adopted 2026-07-30 (KB-VIO-166).

## Why this exists

`inbox/` has had a `processed/` lifecycle for months. `outbox/` had **none**, so a delivered packet and a pending one were byte-identical in every observable way — 14 files sat at the top level, the oldest since 2026-07-01, with no way to tell which were owed. **23 of the fleet's agents already had `outbox/delivered/`; VIOLET was one of the few without it.** This is not a new convention, it is VIOLET catching up to one.

Reconstructing the delivery state cost a directory-wide audit that should have been a `git mv` at send time.

## The rule

| State | Where | Meaning |
|---|---|---|
| Pending | `outbox/*.md` | Written, not yet confirmed consumed by the recipient. **If anything is here, it is owed.** |
| Delivered | `outbox/delivered/*.md` | Confirmed in the recipient's `inbox/processed/`, or (for PROME) consumed in place. |

**`git mv` to `delivered/` as soon as delivery is confirmed** — same discipline as the inbox consume-step, same reason (`feedback_git_mv_for_inbox_processing`).

⚠️ **DELIVERED ≠ ACTIONED, and this directory must never be read as if it were.** `2026-07-28_to-WALTER_registry-stale-numbers.md` sits in `delivered/` and is **confirmed in WALTER's `processed/`** — and the REGISTRY row it asked about is *still* stale as of 7/30 (3rd notice). **An open ask lives in `STATUS.md` / `NEXUS_BRIEF.md`, never in an undelivered-looking file.** Leaving a packet at the top level to "remember" it is owed conflates two different states and breaks the only signal this directory carries.

## Delivery evidence for the 2026-07-30 backfill

Two standards were used and they are **not** equally strong. Recorded separately rather than blended:

**① Confirmed by artifact** — a matching `from-VIOLET` packet found in the recipient's `inbox/processed/`:
`2026-07-28_to-HENRY_re-base-accepted…` · `2026-07-28b_to-HENRY_ask-did-reach-you…` · `2026-07-28_to-SAM_jpy-ivrv-correction` · `2026-07-28_to-TERRY_kb-vio-110-answer…` · `2026-07-28_to-WALTER_registry-stale-numbers` · `2026-07-28_to-PROME_portfolio-gap-docket…`

**② Confirmed by the recipient's own record, with NO artifact in their directory** — `2026-07-01_SIG-VIO-BINA_to-LIQUID_…`. There is **no** VIOLET-named file anywhere under `AGENTS/LIQUID/`, so a pure delivery check returns ❌. But LIQUID's `STATUS.md` reads *"VIOLET Bin-A Gate C answered (7/2 AM)"* and its `KB.tsv` cites the KB-VIO-090/098 tree. **The signal landed and was acted on the next day.** 🔑 *A delivery check answers "did the file arrive?"; it never answers "do they know?" — those came apart here, in the direction that would have manufactured a false orphan* (`finding_delivery_check_is_not_a_knowledge_check`).

**③ Presumed consumed in place — the weakest, and labelled as such.** The seven remaining `to-PROME` items (2026-07-01 → 07-27). Root `CLAUDE.md` makes `outbox/` itself PROME's read channel (*"Write to `AGENTS/<NAME>/outbox/` to request Prome action… Prome checks these and routes accordingly"*), so **for PROME there is no arrival artifact to verify against, ever** — the check that works for every other recipient is structurally unavailable. They are dated 3–29 days back with PROME active daily throughout. **Presumed consumed on age and channel, not proven.** If any turns out to be unactioned, it is a live ask and belongs in STATUS, not back in this directory.
