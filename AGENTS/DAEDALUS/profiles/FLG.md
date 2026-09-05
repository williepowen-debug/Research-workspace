# Agent Profile — FLG

**Built by:** DAEDALUS · **Date:** 2026-09-05 (**FIRST BUILD**) · **The desk itself was built by DAEDALUS 2026-08-20 and first ran 2026-08-28**
**Method:** solo full-tree read + `boot.py` RUN (rc=1) + ledger row counts + the PR#5 claims re-measured
**Sources read:** `CLAUDE.md` (228 ln) · `STATUS.md` (182) · `THESIS.md` · `TRADE.md` · `CALENDAR.md` · `workbook/` (7 TSV + `EXIT_PROTOCOL.md`) · `boot.py` · `scripts/` · `archive/` · `inbox`/`outbox`
**Staleness:** refresh at the **first grade, 2026-11-06** or **>21d** → checkpoint **2026-09-26**

---

## 1. Identity
**Flagstar Financial specialist** (formerly NYCB) — Market class, ACTIVE, **L3 (M)**. The chain: **NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy.** A single-name depth desk in the REGINALD regional-bank family, sibling to OZK and WAL. **Spawnable by:** PROME / Will.

**Born 8/20, first live session 8/28** — this is a **young desk**, and its grade should be read as such: it has structure that a 9-week-old desk normally lacks and a track record it cannot yet have.

## 2. File anatomy
| File | Holds |
|---|---|
| `CLAUDE.md` (228 ln) | charter, boot sequence, the FLG↔REGINALD boundary |
| `STATUS.md` (182 ln) | live state — **+182 net-new lines from the first live session** |
| `THESIS.md` | the rent-regulated → reserve-adequacy chain |
| `workbook/EXIT_PROTOCOL.md` ⭐ | **the dated falsification surface** — `Kill rail re-derived: 2026-08-28`; K-3 promoted to a primary leg (:56-67); **K-4 comparator ≥6.0% base rate, 0-of-5 at the artifact** |
| `workbook/PREDICTIONS.tsv` (9) | 3 FLG-authored OPEN rows with `Resolve_By` |
| `workbook/KB.tsv` (56) · `TRIGGERS.tsv` (16) · `NONACCRUAL_FLOW.tsv` (33) · `MATURITY_WALL.tsv` (20) · `MI3_FLG.tsv` (19) · `RGB_GUIDELINES.tsv` (10) | the domain ledgers — **three are quarterly and correctly declared EXPECTED-STALE** |
| `boot.py` | quarter-ingest check + filing-window logic (`"no closed quarter is past its ~45d filing window"`) |
| `TRADE.md` · `CALENDAR.md` · `archive/` | routing surface · dated calendar · history |

## 3. Per-dimension
| Dimension | Where | Form |
|---|---|---|
| Thesis | `THESIS.md` | the four-link chain, each link with its own ledger |
| Convergence | `TRIGGERS.tsv` (16) + `MI3_FLG.tsv` | banded triggers; the MI3 screen is the REGINALD-family shared instrument |
| Exit / kill ⭐ | `workbook/EXIT_PROTOCOL.md` | dated in-content re-derivation stamp + **a comparator with a measured base rate (0-of-5)** |
| Predictions | `PREDICTIONS.tsv` | 3 OPEN FLG-authored rows with `Resolve_By`; **first grade dated 2026-11-06** |
| Routing | `TRADE.md` + outbox | ⚠️ no confirmed reader-side consumption yet — §5 F-2 |

### §3b. Invalidation-surface inventory
| Surface | Kills / flips | Stamp | Fired-state |
|---|---|---|---|
| `workbook/EXIT_PROTOCOL.md` | the CRE-concentration → reserve-adequacy thesis | **in-content**: `Kill rail re-derived: 2026-08-28` | per-leg K-1…K-n with a promoted primary (K-3) |
| `PREDICTIONS.tsv` | individual calls | `Resolve_By` per row | Status/Outcome; first grade 11/06 |
| `TRIGGERS.tsv` | banded domain triggers | per-row | fired/not |

## 4. Deviations — one that is genuinely notable for a 9-week-old desk

**⭐ A comparator with a measured base rate.** `EXIT_PROTOCOL` K-4 does not assert a threshold; it carries **"comparator ≥6.0% base rate, 0-of-5 at the artifact."** A kill leg that states how often its condition has historically occurred — and reports **zero of five** — is doing the base-rating that older desks routinely skip. **This is the thing to protect under any future compression.**

**Quarterly ledgers declared EXPECTED-STALE rather than left rotting.** Three of the seven are quarterly-cadence and say so; the declaration form was packeted to me 9/1. Correct two-state handling, not drift.

## 5. Findings

**⭐ F-1 — FLG retracted its own finding TWICE IN ONE SESSION, and the second retraction is the valuable one.** Commits `5f8d18eb1 → 7ef1410f9`: it filed a read-cap truncation finding against my perimeter, then **failed its own positive control**, then **retracted in full** on discovering `READ_CAP.md:23` had already ruled the question. Its own commit subject names the lesson: *"audited an instrument without reading the blueprint that defines its perimeter."* **On a desk eight days old.** I am the counterparty here and the retraction was correct — the perimeter is decided canon.

**🟡 F-2 — the L4 consumption leg is untested, not failed.** No confirmed reader-side pickup at REGINALD's or CREED's artifact yet. For a desk that has had **one** session, that is sequencing, not a defect (**PAT-028/PAT-034**). It should not be written as a gap until a second session has had the chance to route something.

**🟡 F-3 — 8 days dark since the first live session.** Not a defect at Tier-active cadence, but the desk's whole record is a single day, so a second session is what converts structure into evidence.

**🟠 F-4 — `maturity_scan` flags "exit rules lack session counts."** This is a **mechanical hint against a local form** and should not be actioned literally: FLG's exit rails are **event- and filing-window-keyed** (quarterly 10-Q cadence, `~45d filing window` in `boot.py`), which is the right clock for a single-name bank desk. **Session counts would be the wrong unit here** — the same call already ruled for OTTO's calendar-dated bounds. Recording the disposition so the hint is not re-raised each scan.

## 6. Conf M→H — the condition, and a warning about how I wrote it
The map row says **"Conf M→H on the first grade 11/06 landing as dated."** That is a legitimate condition (it tests the prediction loop actually closing) but it is **63 days out**, and I have just spent a session finding invented gates. **This one is real — "predictions resolving" is a genuine L3/market leg and FLG's is dated-but-unobserved** — so it stands. Flagging only that a two-month-out condition should not silently become the reason nothing else gets looked at.

## 7. DO NOT TOUCH
1. **The K-4 base-rate comparator (0-of-5)** — a measured base rate is the scarcest thing on a young desk. Never compress it to a bare threshold.
2. **`EXIT_PROTOCOL.md`'s in-content re-derivation stamp** — `ledger_staleness` and the falsification sweep read in-content stamps, never mtime.
3. **The three quarterly ledgers are EXPECTED-STALE by declaration**, not rot. Do not "refresh" them off-cadence.
4. **The FLG↔REGINALD boundary:** REGINALD owns the regional-bank sector view and the MI3 screen's definition; FLG owns the single name. Don't re-derive REGINALD's instrument here.
5. **The first-live-session banner was struck deliberately** on 8/28 when FLG began pulling its own EDGAR primaries — it is no longer a mirror desk. Don't reinstate mirror-grade language.

## 8. Open questions
- Does FLG need a TRADE surface of its own, or does it route through REGINALD? (L4 leg depends on the answer — and per the CORAL finding today, this should be **decided by the desk**, not left waiting on a ruling.)
- Is the stage-1 instrument (still open per PR#5) something FLG builds, or does it inherit REGINALD's?
