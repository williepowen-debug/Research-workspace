# Registration-checklist gap: thematic group pages missed by the 7/12 sweep (PAT-050 instance)

**From:** PROME · **Date:** 2026-07-12 · **Signal:** 🟡 mechanism fix owed — your lane, no urgency

**What happened:** A Will-directed cross-model QA pass (RAV, read-only mirror, post-`d69ffeb1`) found the 7/12 OSPREY/FALCON/HOMER registration sweep (`efd18c09`) updated `_INDEX.md` + `_NETWORK.md` but **missed the three thematic group navigation pages** — `AGENTS/_CREDIT.md`, `AGENTS/_ENERGY.md`, `AGENTS/_FUNDING_MACRO.md` (last touch: June C2 consolidation). Same gap covered WATT/VULCAN/MIDAS (`0fdde6bb`). PROME patched all three + 2 `_NETWORK` wording spots, Will-directed, same-day (`c0ae6846`); CARL STATUS l.232 companion fix `c8dde339`.

**Why it's yours:** this is a PAT-050 instance (registration plumbing asymmetric across surface classes — canonical surfaces wired, human-nav surfaces not). **Mechanism fix = add the grouped `AGENTS/_*.md` pages (at minimum _CREDIT/_ENERGY/_FUNDING_MACRO/_PRIVATE_CREDIT/_SYNTHESIS_OPS) to your registration/build checklist** so the next agent build/reclassification sweeps them in the same pass. The fix batch is done — only the checklist edit is owed.

**Source:** RAV QA report (Will-relayed in-session 7/12) + commits `c0ae6846`/`c8dde339`.
