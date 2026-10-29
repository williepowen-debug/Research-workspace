# DOCKET L40 — amendment-12 watch: the format-vs-recogniser discriminator graded

**Graded:** 2026-10-28 21:2x ET (DAEDALUS; clock from the session stamp). **Row:** `PROME/DOCKET.tsv` L40 (registered 2026-08-07; re-dated to 2026-10-12; slated to Will). **Co-owner input:** NEXUS packet `inbox/2026-10-24_from-NEXUS_L40-amendment-count-since-am11-format-vs-nonformat.md` (86cb450f7). **Letter graded against:** `FORUM/2026-08-07_system-review/06_proposals/04_DAEDALUS_amendments.md` §5 — *"If amendment 11 ships and a twelfth amendment appears that is not itself a format rule, the discriminator is weaker than I have argued it is, and every proposal in my set that rests on it should be re-priced."*

## Method

NEXUS's count was NOT taken on faith (PAT-189). Every commit touching `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` since amendment 11 (`d22d6531b`, 2026-08-07) was enumerated with `git log` and its diff to that file read:

| Commit | Date | What it did to the schema | Numbered amendment? | Format rule? |
|---|---|---|---|---|
| `de28799f7` | 2026-08-28 | PROPOSED amendment 12 (CROSS-DOMAIN first in the FULL variant), escalated to Will; struck the "ordering resolved by practice" closure; ruled the 100-line ceiling unenforced; marked the watch RESOLVED EARLY | no (proposal) | the proposal is order-only |
| `895290f47` | 2026-08-28 | hot/cold split — §6–7 decision log and review history moved to archive (storage) | no | no |
| `f74f656fb` | 2026-08-28 | §4.4 companion ruling: canonical pin token `STATUS commit: \`<hash>\``; a pointer is not a pin (form of an existing field, self-ruled as not fleet-facing) | no | no (field form, not section form) |
| `58eca316c` | 2026-09-02 | **Amendment 12 ENCODED** (ratified 2026-09-01, Will via PROME WQ-105): section ORDER only, zero text; §4.6 CAP adopted in the same word — schema closed at 12 of 12 | **yes — #12** | **yes (order)** |
| `1c32d974c` | 2026-09-07 | §4.1-R rollout rule (trigger · owner · escalation for amendment 12) | no (process) | no |
| `a1f8d3366` | 2026-10-19 | §4.2 pilot cap text labelled HISTORICAL; §5 labelled historical proposal | no | no |
| `86cb450f7` | 2026-10-24 | Stage-2 repair: ratified texts of amendments 1–3, 9's COMPACT form and the §4.4 ruling written into the hot schema; history to archive §A13 | no (restoration; uncapped under §4.6 "already ratified") | no |
| `f6e88eb2a` | 2026-10-24 | one-line WQ-519 (i) header note (restoring ratified text is not an amendment) | no | no |

NEXUS's packet named five of these (895290f47 · f74f656fb · 1c32d974c · a1f8d3366 · the stage-2 repair). It omitted `de28799f7` (the 8/28 proposal commit) and `f6e88eb2a` (the 10/24 one-liner). Neither omission changes the count: **numbered amendments since #11 = ONE (#12), and it is a format rule.** Non-amendment edits = SEVEN, none a format change.

## Verdict on the letter

**The discriminator SURVIVES its registered test.** No twelfth NON-format amendment appeared between 2026-08-07 and 2026-10-28. The only amendment was #12, an order-only format repair. Recognition rules (amendments 1–10's class) generated zero amendments in the window. **Slate proposals resting on the discriminator do NOT re-price on this evidence.**

Two caveats travel with the grade:

1. **NEXUS's stronger paraphrase was falsified, and NEXUS already graded it.** NEXUS restated the discriminator as *"11 will end its class"* (no further format amendments). Amendment 12 is a second format rule, so that paraphrase MISSED; NEXUS recorded it as such on 2026-08-28 (`de28799f7`) and on 2026-09-02 (`58eca316c`, "the watch-prediction … was GRADED MISSED on its own letter"). My letter and NEXUS's paraphrase are different claims; the L40 row text ("a twelfth NON-format schema amendment") carries mine. Both grades stand side by side.
2. **The test went blind on 2026-09-01.** The §4.6 cap forbids any amendment 13, so after that date the schema cannot produce the falsifying event by rule. The live window was 25 days (8/7–9/1) of the 82 graded; it showed 1 format and 0 non-format amendments. The evidence is consistent with the discriminator and thin. Re-testing requires a different registry; none is proposed here.

## Disposition

- Grade: **DISCRIMINATOR HOLDS (letter) · NEXUS paraphrase MISSED (already graded by NEXUS) · test now UNTESTABLE on this schema (cap).** No slate re-pricing.
- NEXUS's co-owner half is DONE (its count verified correct in substance; two non-amendment commits omitted, immaterial).
- PROME writes back L40 and presents the row to Will (it is slated to him). Nothing is owed by NEXUS.
- Inbox packet filed to `inbox/processed/` with this record.

REVIEW: not-required — a grade of a registered letter at named commits; every diff cited is reproducible with `git show <sha> -- AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md`.
