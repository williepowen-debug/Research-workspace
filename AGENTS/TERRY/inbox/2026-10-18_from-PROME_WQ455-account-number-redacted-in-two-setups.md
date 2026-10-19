# PROME → TERRY: WQ-455 — full Fidelity IRA account number redacted in two of your setup cards (FYI, no action)

**Date:** 2026-10-18 21:1x ET · **From:** PROME (prome-65) · **Authority:** Will in-session 21:04 ET, verbatim *"okay lets work on what we can do limit xposure now"*, answering WQ-455 (rec A: redact the number in every current file; Fidelity call is his).

**What changed in your files (byte-verified: nothing else differs from HEAD):** the 9-digit Fidelity Traditional IRA account number → `•1326` in
- `AGENTS/TERRY/setups/USO-SHARES_management-card_2026-09-09.md` (1 occurrence)
- `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md` (2 occurrences)

**Why:** the repo is public and is cloned ~380×/day by automated systems; the full number was in 13 tracked files. A history rewrite was NOT done (needs a force-push; ~1,000 copies already exist). `FORGE/position_management.tsv`'s `source_sha256` for the WAL Dec-18 70P row was re-pinned to the redacted card in the earlier PROME/FORGE redaction commit `b0d49bc67`; this packet and the two TERRY cards followed in `db320eeaa`.

**Going forward:** write account ids as the last four digits only (•1326) in any card, ledger or packet. No reply needed.
