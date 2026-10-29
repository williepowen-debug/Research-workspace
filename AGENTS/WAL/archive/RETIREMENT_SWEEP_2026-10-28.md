# WAL retirement sweep — 2026-10-28 (housekeeping, Will: "do all housekeeping now")

**Rule (root CLAUDE.md §Data Hygiene):** a file >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to `archive/`. Index/inventory/nav references and dated records don't count. Candidates came from the 10/22 desk sweep (`research/2026-10-22_desk-sweep.md` S9). References checked repo-wide on 10/28.

| File | Content date / last add | Boot-read | Live references | Action |
|---|---|---|---|---|
| `MARKET/README.md` | 3/25 chart notes / 2026-07-25 | no | charter FILES row (nav — does not count, re-pointed); `research/audit_2026-09-28/A_dashboard.md` (dated record) | **RETIRED** → `archive/MARKET/` |
| `MARKET/WAL_5min_2026-03-25.png` | 3/25 / 2026-07-25 | no | only the README above (moved with it, relative links intact); `memory/2026-03-25.md` names the pre-promotion folder (dated record) | **RETIRED** → `archive/MARKET/` |
| `MARKET/WAL_15min_weekly_2026-03-25.png` | 3/17–3/25 / 2026-07-25 | no | as above | **RETIRED** → `archive/MARKET/` |
| `MARKET/TRADE_LOG.md` | bannered FROZEN / 2026-07-25 | no | **`POSITIONS.md:7`** (live; explains the phantom-strike banner) | **HELD** — moving it would break that pointer |
| `FRAUD/WAL-JEF-PointBonita-Analysis-20260326.docx` | 3/26 / 2026-07-25 | no | **`FRAUD/FIRST_BRANDS.md:158`** (live fraud home: "Full analysis doc") + `FRAUD/STATUS.md` | **HELD** |

Moved with `git mv` (history preserved). Content untouched.

**Outbox filing, same session:** 26 of 27 sent packets (8/07–10/14) moved to `outbox/delivered/` after each was matched to recipient evidence: 18 exact copies in the recipient's inbox, 4 under a different file name (PROME 8/20, DAEDALUS 9/02, OZK 9/02, PROME 9/02), 2 by PROME courier (REGINALD `inbox/processed/2026-08-07_from-PROME_delivery-two-WAL-packets…`), 1 by the REGINALD pair log (8/23, ACKed in `REGINALD_CHANNEL.md`; REGINALD's own archive records the sold-not-lapsed fact). **Held in `outbox/`:** `2026-08-23_to-PROME_wave-3-delivery-…` — no copy in PROME's inbox; PROME's 8/23 handoff shows only "WAL + OZK lapse write-backs IN FLIGHT at close". Delivery unverified, so it is not filed as delivered. Its trade fact (the $77.5P was sold 8/18) reached REGINALD by the pair log.
