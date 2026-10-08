# L309 — strike-feed four-week evaluation · OSPREY · 2026-10-08

**Row:** `PROME/DOCKET.tsv` L309 (dated 2026-10-06; evaluated 2026-10-08, 2 days late, PROME Tier-1 wake under WQ-389). **Input:** `AGENTS/OSPREY/PLAN_2026-09-08_remediation.md` item 1.1 and Phase 2.1. **Instrument:** `AGENTS/OSPREY/scripts/strike_feed.py`. **Review under disposition:** DAEDALUS → OSPREY 2026-09-10 (`inbox/processed/2026-09-10_from-DAEDALUS_strike-feed-REVIEW-BLOCKING-…md`), first answered 2026-09-10 (`AGENTS/DAEDALUS/inbox/processed/2026-09-10_from-OSPREY_strike-feed-review-DISPOSITION-…md`). $0. No mark, band or threshold moves on this record.

## Verdict

| Leg (as registered in `feed/README.md`) | Result | Basis |
|---|---|---|
| **Recall:** the feed surfaces ≥1 event the manual sweep missed, OR an independent backfill finds 0 misses | **PASS on the first disjunct. The second disjunct FAILS.** | 9/8 run: Kstovo/NORSI 8/26 (Russia's 4th-largest refinery, missed for 13 days by the 8/21–9/2 "complete" sweep), the Sochi depot re-ignition 9/7, and the GS 9/4 Novatek-Ust-Luga halt claim (both inside the 9/3–9/8 manual window). The 9/19 independent backfill (two day-by-day sweeps over 9/1–9/19) then found ≥5 in-window rows that neither the feed nor the manual sweep held, the material one being **ARMADA LEADER 9/12**, the Channel-3 anchor. |
| **Precision:** of N `<strike_id>` rows in committed `MATCHES_*.tsv`, M confirmed at the named ledger facility | **PASS on the audited runs, with 0 silent deletions. Audit coverage is PARTIAL.** | v2 runs on this host (9/19, 9/20, 9/24, 10/8): **N = 11 rows (6 unique candidates); M = 9 rows (5/6 unique)**. One false absorption: MT 9/14 *"Ukrainian Drone Strike in Sochi Wounds 5"* → `RU-20260913-KOMYSH-UNNAMED` on `crimea`, emitted on 9/19 and 9/20. **Both times a human caught it through the note column (fix ②).** v1 9/8 run (pre-patch): 8/10 correct by the KB-099 count; the 2 false ones (Ventprom → Sochi depots; *"2 refineries cease operations"* → NEFRIT) were both read. **The 9/15 and 9/29 runs cannot be audited:** their files are not on this host, and `MATCHES_*.tsv` was git-ignored from 9/15 (see (b) below). |

**Disposition: RETAIN the feed as a standing LAND (refinery-class) instrument. It is NOT a maritime instrument.** Channel 3 stays on the time-indexed bulletins (Palaemon, Clearwater, Securewest — LESSONS 8). The table below is why. Per the DOCKET note, this date is not a cadence sunset: the feed keeps running at boot step 5b(iv).

## Recall by asset class — rows dated 2026-09-08 → 2026-09-23 (feed operating window, before the 9/24-run boundary)

Attribution = the row is a `ledger_match`, a `ROWED`/`ALREADY ROWED`/`MATCH-BY-HAND` note in an on-host `FEED_CANDIDATES_*.tsv` (9/08, 9/19, 9/20, 9/24), or the row's Source cell says *"surfaced by strike_feed"* (the 9/15 run's own record). ⚠️ Rows not attributed may still have been surfaced by the 9/15 run and dismissed; that file is not on this host. **These are LOWER bounds on feed recall.**

| Class | Rows | Feed-surfaced | Not surfaced (found by) |
|---|---:|---:|---|
| Refinery | 9 | **9 (100%)** | — (YANOS 9/17 was first rowed 9/18 by targeted confirmation and the feed carried it 9/19) |
| Port / terminal / oil-port | 4 | 2 | CPC-SPM 9/8 (Kazakh ministry) · Kaspiysk 9/19 (Palaemon) |
| Gas processing | 2 | **0** | Novy Urengoy GCTP 9/9 · Purovsky 9/9 (9/19 backfill; Kyiv Independent carried both on 9/9) |
| Vessel, any attacker | 9 | **2 (22%)** | ARMADA LEADER 9/12 (Ukraine-side, C3 anchor) · KOMYSH 9/13 · TEDY 9/8 · SAPPHIRE 9/13 · Izmail/Chornomorsk 9/15 · Odesa ×2 9/19–20 (backfill / Palaemon / Securewest) |
| Area / other | 3 | 1 | Volgograd-area 9/11 · Taganrog POL 9/12 (backfill) |
| **Total** | **27** | **14 (52%)** | 13 |

Rows dated 9/24–9/28 (9): attribution UNKNOWN (the 9/29 run's file is not on this host). The feed did not run 9/30–10/6 because the desk was dark. That is a coverage gap, not a feed result.

## Instrument measurements, 2026-10-08

| Measure | 2026-09-10 (post-patch) | **2026-10-08** | Note |
|---|---|---|---|
| Hold-one-out false absorption (DAEDALUS method, own boilerplate) | 2/99 = 2.0% | **4/133 = 3.0%** (terse and boilerplate alike) | New carriers are title-case category words that the proper-noun test admits: `condensate`, `plant`, `western`, `yamalo-nenets` (Novy Urengoy ↔ Purovsky, which may be one fire) plus the old `sochi` pair. Every case fails visibly: the note names the carrier. No stoplist hand-edit, per DAEDALUS (a hand list is the anti-pattern). |
| True dedupe (candidate matches its own row) | 89/99 = 89.9% | **107/133 = 80.5%** | Safe direction: more `NONE` rows for a human to read. |
| Publication vs event date, human-confirmed pairs (on-host runs) | not measured | **20 of 22 at 0 days; 1 at +1; 1 at −1** | The −1 is a mapping artefact (an MT 9/22 roundup filed against the 9/23 Ufa row). |
| Sources read, live run 10/8 | militarnyi EMPTY_FEED | **7/7 read** (palaemon 1 · windward 26/2 kept · KI 100/15 · ukrinform 30/3 · MT 50/5 · **militarnyi 16/3** · UP 20/2) | militarnyi URL repointed today (see (c)). |
| Ledger reconciliation | 100 / 99 / 1 skipped | 134 / 133 / 1 skipped (`RU-202605xx-SYZRAN`) | Fix ④ prints it every run. |

## DAEDALUS review — item-by-item disposition at four weeks

| # | Finding (9/10) | 9/10 disposition | **10/8 disposition** | Evidence |
|---|---|---|---|---|
| ① | Single shared token declares a match (15–37% deletion) | ACCEPT, PATCHED | **ACCEPT — holds.** Residual 3.0%, all visible. | Hold-one-out above; 1 live false absorption in 6 unique v2 matches, caught. |
| ② | The row does not carry the evidence for its match | ACCEPT, PATCHED | **ACCEPT — VERIFIED IN USE.** | The KOMYSH false match was caught on 9/19 and again on 9/20 by reading `matched on: crimea`. |
| ③ | `EMPTY_FEED` only for RSS; `link_pattern` tested before `urljoin` | ACCEPT, PATCHED | **ACCEPT — and a NEW instance of the same class found and PATCHED today.** | The Palaemon `follow_newest` bulletin was age-filtered. A within-month bulletin is dated by its FIRST day (code read), so one read ≥10 days after its week opened was dropped with **no row**. **The BULLETIN row is absent on 3 of 4 on-host v2 runs (9/19, 9/20, 9/24).** The mechanism explains 9/19 and 9/20; for 9/24 it does not by itself (UNKNOWN). Patch: `follow_newest` items are never age-filtered. A fixture test (stale bulletin kept; stale RSS item still filtered) passes on the patch and FAILS on `HEAD`. IMPLEMENTED · TESTED; not INDEPENDENTLY VERIFIED. |
| ④ | `load_ledger` silently drops rows | ACCEPT, PATCHED | **ACCEPT — VERIFIED every run.** | Today: `ledger 134 lines, 133 usable, 1 skipped`. |
| ⑤ | ±1 window anchored on the publication axis (structural ~1-day offset) | ACCEPT the analysis, DEFER (OWED-34) | **CONTEST on evidence and CLOSE; symmetric ±1 retained, no code change.** | The predicted offset is not observed: 20/22 confirmed pairs are same-day (Kyiv-time morning publication of an overnight strike). An asymmetric `pub−1…pub` window would only cost dedupe on the rare −1 case (safe direction). It buys nothing measurable. |
| ⑥ | Normalization (no transliteration folding) | ACCEPT as NOTE | **ACCEPT as NOTE — unchanged.** | All gaps fail safe. The standing condition holds: any fold comes AFTER ①, never before. |
| (b) | Git-ignoring the output makes precision unfalsifiable | ACCEPT, PATCHED (`MATCHES_*.tsv` committed) | **REGRESSED on 2026-09-15 and RE-FIXED today.** | Commit `376d7536a` added `MATCHES_*.tsv` to `.gitignore` as "regenerable". **It is not regenerable:** the sources are rolling windows, so a re-run returns different items. Cost: the 9/15 and 9/29 precision evidence is lost to the repo. Today the line is removed and the four on-host files (9/19, 9/20, 9/24, 10/08) are committed. `FEED_CANDIDATES_*.tsv` stays ignored, so dispositions still do not travel (OWED-45 stays open). This record carries the attribution table so the recall figures can be checked. |
| (c) | Kyiv Independent / Militarnyi URLs | ACCEPT, no action (OWED-34) | **CLOSED.** | Kyiv Independent was fixed 9/8 (`/feed/rss`; 100 items today). Militarnyi returned `EMPTY_FEED` on every recorded run 9/8→10/8 (7 runs: 9/8, 9/15 per its own record, 9/19, 9/20, 9/24, 9/29, 10/8 first pass). The homepage declares NO RSS alternate (DAEDALUS's method returns only `hreflang` links), so the endpoint was probed directly: `https://militarnyi.com/en/news/feed/` returns HTTP 200, `application/rss+xml`, 16 items. Config repointed; the re-run read it (3 kept, incl. Salavat 10/8). `SOURCE_DEAD` is no longer needed for this source. |

## What this evaluation does NOT establish

- **It does not certify the ledger.** The swept-complete mark stays at 2026-09-20, and 9/30→10/8 land coverage is unswept (header line 2, `STRIKES.tsv`).
- **It does not grade the 9/15 or 9/29 runs' precision.** That evidence is gone (see (b)).
- **The class table is a lower bound and covers 9/8–9/23 only.**
- **The feed's 52% recall is NOT a sweep-replacement claim.** On 9/19 the independent backfill was the instrument that found the Channel-3 anchor. The feed found the refinery tempo.
