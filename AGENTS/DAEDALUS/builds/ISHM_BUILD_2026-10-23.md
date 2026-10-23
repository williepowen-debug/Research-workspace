# BUILD RECORD — ISHM (US industrial / manufacturing-cycle desk)

**Built:** 2026-10-23, one session · **By:** DAEDALUS (Claude Code, claude-opus-5-5)
**Will's word:**
- To WALTER, verbatim *"I think we need a domain with coverage for industrials/manufacturing"*.
- **WQ-506 RULED APPROVE A** in PROME's window, 2026-10-23 09:35 ET, verbatim *"yes approved go ahead"*.
- Name, in DAEDALUS's terminal at 09:36 ET, verbatim *"Oh I like Ishmael I think. Lets call him ISHM"*. Confirmed `ISHM` over `ISHMAEL` by option choice at 09:37 ET.

**Inputs:**
- WALTER v2 proposal: `AGENTS/WALTER/research/2026-10-23_morning/INDUSTRIALS_DESK_PROPOSAL.md`
- DAEDALUS review (cleared v2 at 09:31 ET): `design/2026-10-23_INDUSTRIALS_DESK_PROPOSAL_REVIEW.md`
- PROME's three scope edits and two falsification jobs, as carried on the WQ-506 row.

**Blueprint:** `BLUEPRINTS/market-agent.md`. **Template:** the CYPHER build of 2026-10-22.
**Class:** Market domain — Tier-2, print-driven. **Grade at birth:** L0 / M (§4).

## 1. What was built — `AGENTS/ISHM/`

| File | Content |
|---|---|
| `CLAUDE.md` | **Charter.** Spine = the question (real end-demand or borrowed?) plus two standing falsification jobs: J1 core capex vs VULCAN, J2 freight vs LIQUID/RED. J1 carries a GPU-import caveat: a flat M3 cannot falsify AI capex, so J1 must pair M3 with FT-900 computer imports and BEA equipment investment. **Scope:** 5 families. **Perimeter:** 8 frozen names. **Boundaries:** 19 seam rows. HENRY's `<47` trigger is kept HENRY's until Will rules (WQ-506 does not rule it). HANS is an inbound edge. Exclusions register: 4 rows, 2 marked NO OWNER. Thresholds: only the definitional 50 line; all bands OWED. Carries the HANS flash-vs-final rule, USER.md no-expiry-nagging and the NOT-FIRED → TERRY route (WAL form, per PROME's 09:3x request) |
| `STATUS.md` | FIRST-LIVE-SESSION banner UNSPENT · "Current judgment: NONE YET" · gauges · BOTTOM LINE |
| `FIRST_SESSION.md` | 11 items: perimeter verification incl. Honeywell separation · boundary packets · HANS caveat US side · J1 paired test · J2 base rate · first print rows · R1 flips · thresholds · READS · NEXUS_BRIEF |
| `PERIMETER.tsv` | FROZEN banner + the 8 ruled tickers, with segment read and seam per name |
| `TRADE.md` | `FROZEN 2026-10-23 — NO BOOK BY CHARTER`, plus the re-arm condition and the NOT-FIRED → TERRY route |
| `workbook/PRINTS.tsv` | Print ledger: 14 columns, 27 SERIES-KEYs, Vintage enum (FLASH / ADVANCE / FIRST-PUBLISHED / FINAL / REVISED-date). **Empty by design** |
| `workbook/VX.tsv` | 8 vectors (7 MECHANISM, 1 THERMOMETER). **Every Score `UNKNOWN`.** Direction declared: high = borrowed / rolling over. Shared-root note (surveys and IP count once) |
| `workbook/FLOW.tsv` | 8 mechanisms, all `UNTESTED`, each keyed to a vector |
| `workbook/KB.tsv` | 4 seeded rows, each marked as an inherited read: HANS lead · WALTER's 57.0 (C3, flash) · data access · ISM claimant history |
| `workbook/PREDICTIONS.tsv` | **Empty by design** |
| `workbook/EXIT_PROTOCOL.md` | `Kill rail re-derived: 2026-10-23` PROVISIONAL. R0 premise review 2027-01-29, with the CARL-fold alternative and two positive instruments. R1 flips owed. J1 and J2 NOT REGISTERED, with their blockers named |
| `docket/CATALYSTS.tsv` | §5 |
| `DATA_ROUTES.md` | §5 |
| `boot.py` | 8 legs: staleness · predictions · catalysts (EMPTY-/THIN-FORWARD 30d) · **missed prints** (past `[SERIES-KEY]` catalyst vs PRINTS) · print-ledger enums + provisional-successor check · **frozen perimeter** · matrix/map · **FRED live** (7 series, positive control). Drill hooks: `ISHM_BOOT_TODAY` / `ISHM_HOME` / `ISHM_FRED_DIR`; `--offline` reports the FRED leg as rc 1 |
| `scripts/test_boot.py` | 37 drills |
| `board_log.tsv` · `inbox/PROTOCOL.md` · `outbox/README.md` | Mail |

## 2. Checks run — what was watched (CHECK_STANDARD §3)

| Path | Result |
|---|---|
| Drill suite | **37/37 pass.** Each leg has its alert, clean and failure paths. FRED: HTML body, too-small population, stale series and missing fixture each return rc 2. main() runs through the drill hooks: rc 1, and a missing catalyst file dominates at rc 2 |
| **Mutation check** (scratch copy) | Each mutation is caught by exactly one test, and the file was restored. M1: THERMOMETER counted into the composite. M2: HTML accepted as CSV. M3: an older print satisfies a newer catalyst |
| Real boot 10/23 09:47 ET, cwd `AGENTS/` | rc **1**, all true positives: EMPTY-FORWARD (before catalysts were written) · 0 print rows · 8/8 UNSCORED · FRED shows 7 series with prints not yet read (INDPRO 2026-09 = 103.9506 … AMTMNO 2026-08 = 663491). Perimeter clean (8 tickers). Staleness quiet |
| FRED reachability (curl, keyless, 09:4x ET) | INDPRO · TCU · IPMAN through 2026-09; DGORDER · NEWORDER · ANXAVS · AMTMNO through 2026-08. **NAPM (the old ISM id) returns an HTML page, not data** — consistent with ISM being off FRED |
| `tsv_append --check` | 7/7 TSVs OK |

## 3. Registration (REGISTRATION_CHECKLIST, 16 rows)

| # | Surface | State |
|---|---|---|
| 1 | `PROME/ROSTER.md` | ⏳ PROME — TIER-2 row (6→7), on this commit |
| 2 | Root `CLAUDE.md` | NO-OP expected (no roster or chain list) — PROME verifies by grep |
| 3–6 | `AGENTS.md` · `_INDEX.md` · `_NETWORK.md` · group pages | ⏳ PROME, with text proposed in the registration packet. `_NETWORK.md` edges are routes, so they go to Will via PROME |
| 7 | WALTER routing | ⏳ WALTER mints the domain code and routing row on Will's sign-off; the `MACRO_INFLATION` row re-cut is WALTER's |
| 8–9 | `FLEET_MAP.tsv` + directory | ⏳ DAEDALUS, AFTER ROSTER (PAT-047) |
| 10–11 | Peer seams + consumer handoffs | WATT (ASK, committed) and CARL (INFO, committed) packets sent at build. Every other seam owner is DEFERRED to ISHM's first session by charter (FIRST_SESSION item 3) |
| 12 | DAEDALUS script registries | No edit — the Market default |
| 13 | Parent behavioural registries | n/a (greenfield). **But HENRY's `ISM Mfg <47` trigger names ISHM's metric**; kept HENRY's pending Will's word (charter § BOUNDARIES) |
| 14 | Seeding checks | ② name-the-unrepresentable-shock: chemicals, aerospace outside GE, nearshoring (2 NO OWNER) and gas/power inputs are written down. ③ FILES table written in role tense |
| 15 | State tokens | Class 12 Basis on PRINTS · Class 3 enum on PREDICTIONS · Class 1 FROZEN on TRADE and PERIMETER · Class 5 UNKNOWN on VX · Class 9 P-tokens on CATALYSTS |
| 16 | Sub-agent layer | n/a |

## 4. Honest ceiling

**L0 at birth.** The L1 leg needs a current judgment (reading B), and ISHM's says *NONE YET*. Every seeded row is marked as inherited. Two premises in the ruling were checked and found only partly true:
- **(a)** WATT reads GE Vernova's backlog (KB-WATT-097), but its charter does not claim equipment demand. WATT was asked to accept, partly accept or decline.
- **(b)** HENRY's `<47` trigger is not moved by WQ-506.

## 5. Follow-up — catalysts and data routes (same morning)

**Calendar source:** a research helper (Opus) read the issuer schedules and recorded every failure. Working file: the session scratchpad `release_calendar.md`; its content is carried into the catalyst `notes` cells. The helper found 38 dated rows: 20 PRIMARY, 7 SECONDARY, 11 RULE-DERIVED.

**`docket/CATALYSTS.tsv`:** 32 rows from 2026-10-23 to 2026-12-31.
- `date_class`: `FIRM` for PRIMARY dates; `MODELED (~)` for SECONDARY or rule-derived ones.
- AAR weekly rail is batched into one row per month, to keep the Tier-2 wake cost down.
- One housekeeping row on 12/31 to extend the calendar.
- The **G.17 annual revision on 11/24** is a P1 row, because any IP/TCU band must be re-based.
- **The December S&P Global flash has no row:** no source gave a date.

**Blocked routes:** ISM is behind a login page with a reCAPTCHA check, and was not bypassed. S&P Global returns 403 or a bot challenge. Both have SECONDARY dates only.

**`DATA_ROUTES.md`:** 14 routes, each with its reach.

**Bellwether earnings and J1 rows (added the same morning):** 7 rows, from a second helper that checked the company IR pages, 8-Ks and the BEA/Census schedules.
- Already out before build: GE Aerospace 10/20, 3M 10/20, Honeywell 10/22, Union Pacific 10/22 — one P1 row, dated 10/22.
- CAT 10/29 (SECONDARY; site blocked).
- EMR 11/04 and PH 11/05 (PRIMARY).
- A Deere date-check row on 11/12 (TBD; not yet announced).
- BEA Q3 GDP advance 10/29 (J1 leg 3) and FT-900 trade 11/04 (J1 leg 2), both PRIMARY.

The catalyst file now has **39 rows**. Boot shows two true positives: the 10/22 earnings row is past and unread (MISSED PRINT), and today's flash PMI row is due.
