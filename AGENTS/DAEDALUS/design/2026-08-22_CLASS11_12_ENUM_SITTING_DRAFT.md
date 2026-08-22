# STATE_VOCABULARY Classes 11 + 12 + surface-role enum — census-first draft for the 8/23 sitting

**Date:** 2026-08-22 morning · **Author:** DAEDALUS · **Status:** ~~DRAFT~~ **MINTED 2026-08-22** — Will verbatim "ok both approved" 14:34 EDT (sitting pulled forward to Sat 8/22; ruling record `PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §MINTED; four open picks ruled: UNPROCESSED not-minted w/ `delivered_unread` metric · OWNER-ASSERTED minted · DERIVED minted, GENERATED = banner subtype · exemption law single-homed at Class 11). **ENCODED same day → `BLUEPRINTS/STATE_VOCABULARY.md` Classes 11/12 + Class-1 extension; this doc is now HISTORICAL — cite the registry, not this draft.**
**Provenance:** Will verbatim "ok go ahead" 8/21 23:30 on the merged RAV package (`PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §RULED, `74139856e`). Source items: RAV 3 (Class 11) · RAV 2+8 merged (Class 12) · RAV 1 labels (enum). Review: `upgrades/RAV_FEEDBACK_REVIEW_2026-08-21.md`.
**Census method (§12 discipline — measured, not assumed):** token-shaped occurrences, `*.md`+`*.tsv` across AGENTS/PROME/FORGE(/MESSAGING), archives excluded, run 2026-08-22 09:3x EDT. Counts are usage-frequency evidence for which distinctions the fleet ALREADY makes; they are not row-level audits.

---

## Class 11 — Consumption-state ladder (packet/finding delivery lifecycle)

**Census:** CONSUMED 281 · unconsumed 295 · ROUTED 265 · DELIVERED 255 · UNPROCESSED 32 · CLOSED-VERIFIED 22 · ENCODE-CONFIRM(ED) 17 · landed-unread 7 · owner-encoded 4 (mostly the RAV artifact itself) · CREATED-as-token 0 · READ-as-token ~0 · ANSWERED-as-token ~0.

**Proposed token set (5 states + 1 exemption), mined from the measured ladder:**

| Token | Meaning | Census basis |
|---|---|---|
| `ROUTED` | written + committed toward the recipient; nothing known about arrival-side | 265 |
| `DELIVERED` | at the recipient's surface (inbox/board); not yet read. Compound display form `LANDED-UNREAD` stays legal as `DELIVERED` + an age | 255 (+7) |
| `CONSUMED` | recipient read/processed it (their filing or explicit ack) — says nothing about their surfaces changing | 281 |
| `ENCODE-CONFIRMED` | the change landed on the owner's own surface, owner-attested | 17 |
| `CLOSED-VERIFIED` | sender verified the encode at the artifact — the chain's terminal state | 22 |
| `EXEMPT-PULL` | declared exemption: pull-complete recipient — for this route DELIVERED **is** complete (`finding_deferral_rule_hides_its_own_cost`; Class-8 EXEMPT twin lesson) | WALTER exemption class |

**DON'T-MINT (near-zero-instance, per the ruling):** `CREATED` (0 — a state nobody records), `READ` (collapses into CONSUMED), `ANSWERED` (prose verb, not a state — an answer is itself a packet that gets its own ladder), `OWNER-ENCODED` (RAV's spelling; the fleet's is ENCODE-CONFIRMED, 17 vs 4 — one spelling survives).
**Sitting question (one):** does `UNPROCESSED` (32) survive as the standing negative of CONSUMED (inbox-count vocabulary), or is it DELIVERED + age? My lean: alias of DELIVERED-with-age, don't mint — but AEOLUS's unfiled-vs-unprocessed caveat (fleet_triage design input) says the *filing* sense needs a word; decide with the triage metric label in the same breath.
**Rule that travels with the class:** a packet may not be described as resolved below ENCODE-CONFIRMED; a sender may not describe it CLOSED-VERIFIED without the artifact check (RAV item 3's operative sentence, kept verbatim in spirit).

## Class 12 — Verification-basis (what kind of checking stands behind a claim)

**Census:** primary-verified 333 · artifact-verified/verified-at-artifact 146 · secondary-source 162 · "not independently verified" 60 · EDGAR-verified 36 · UNANCHORED 20 · owner-asserted 2 · unverified 1,591 (generic).

**Proposed token set (5), mined:**

| Token | Meaning | Census basis |
|---|---|---|
| `PRIMARY-VERIFIED` | checked against the primary/external source itself (EDGAR-verified = domain-specific subtype, stays legal prose) | 333 (+36) |
| `ARTIFACT-VERIFIED` | checked against a repo artifact — internal consistency, NOT external truth (the repo-vs-world line RAV item 8 wants) | 146 |
| `SECONDARY-SOURCE` | rests on a secondary report only | 162 |
| `OWNER-ASSERTED` | counterparty's claim, not independently checked (absorbs "not independently verified" — one spelling; 60 vs 2, sitting picks) | 62 |
| `UNANCHORED` | no anchor exists — the visible-absence token, the class's real payoff (`finding_silent_blank_evades_review`) | 20 |

**DON'T-MINT:** `UNVERIFIED` as a token (1,591 uses, but generic — it fails to discriminate OWNER-ASSERTED from UNANCHORED, which is the distinction the class exists to make; stays a prose word). `MARKET-DATA-CURRENT-AS-OF` (RAV's) — that's a timestamp practice already governed by PAT-044/root pricing rules, not a state token.
**Scope guard (in the class text):** load-bearing/decision claims only — labeling every sentence is the VULCAN 4-of-7 over-reporting class.

## Surface-role enum (RAV item 1's labels)

**Census:** HISTORICAL 221 · DERIVED 185 · CANONICAL 139 · GENERATED 38 · FROZEN 1,518 (Class 1) · SCRATCH = de-facto file names (SCRATCH.md fleet-wide).

**Recommendation: EXTEND Class 1's family, do not fork a new class.** FROZEN/archive banners already live in Class 1; the enum adds role labels to the same field-family: `CANONICAL` · `DERIVED` (with `GENERATED` as the machine-written subtype — one of the two survives as the token, sitting picks; my lean GENERATED⊂DERIVED, mint DERIVED, let "GENERATED — do not hand-edit" stay the established banner form) · `SCRATCH` · `HISTORICAL`. RAV's `archive` = already Class 1 territory, don't re-mint.
**Form guard (part of the ruling, restated):** the authority MAP is a generated join over these surface-local labels (render_directory model). Labels canonical at surfaces; map derived. A hand-maintained map is pre-declined.

---

**One-cloth note:** Class 11's EXEMPT-PULL, Class 8's SCHEDULED/EXEMPT-BY-CHARTER, and the cadence enum's designed-quiet all express the same law — *declared exemption must be expressible or the guard trains its reader to ignore it*. Rule the three token families in one breath (the standing prep note, now n=3).
