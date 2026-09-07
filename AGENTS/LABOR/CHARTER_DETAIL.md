# LABOR — CHARTER DETAIL (cold half of `CLAUDE.md`)

**Created 2026-09-07 under WQ-193** (Will verbatim *"Approve WQ-193 with your recs"*, 16:35 ET; contract `PROME/proposals/2026-09-07_wq193-RULED.md`).

⛔ **ON-DEMAND / grep ONLY — this file is NEVER a boot read, and it therefore carries no read-cap budget of its own.** If it ever becomes a boot read it acquires one.
🔒 **`CLAUDE.md` wins on any RULE.** This file holds the *why* — origins, worked examples, incident write-ups, rulings-as-history. **Blocks were moved verbatim and contiguous; no rule was changed and no obligation was deleted in the move.**
📋 **Census at the split → the WQ-193 delivery memo** (text census: line/byte/crc before and after; obligation census: every active duty located after the split).

---

<a id="b2a-origin"></a>
## § `b2a-origin` — B2a — spine-freshness gate: build history, falsification record, and the three misses that paid for it

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

✅ **AUTOMATED 2026-08-23 (BD-02 DISCHARGED) — `scripts/spine_check.py`, run by `boot.py` as step (a-bis) immediately after the data sweep.** It parses **ISO `obs YYYY-MM-DD` tokens ONLY** (prose dates like *"w/e Aug 15"* are deliberately NOT parsed — that fragility is what deferred this build three times; a prose-only STATUS reports **CANNOT-VERIFY**, never a false PASS), reduces with **max()** so dated-historical rows are inert **by construction** rather than by exclusion rules that rot, and prints **three states — STALE / FRESH / CANNOT-VERIFY — every run, never silent.** **A fetch failure is CANNOT-VERIFY, not a pass.** Exit 2 on stale-or-unverifiable. ⚠️ **You must still READ the line** — the gate reports, it does not refresh. **Falsified before adoption** (4 cases: fires on a stale spine; inert on an added historical row; loud on a missing ISO token; loud on an unreachable FRED). *Paid for by THREE misses: 7/16, 7/31, and 8/20 — the last found by DAEDALUS's external sweep three days before my own boot found it.* ⚠️ And note the limit even once built: **this gate only fires when a session runs.** Neither it nor anything else in my boot docs can catch a print that lands on a day nobody boots (the summons gap — an external CATALYSTS-driven alert is PROME's to build).

---

<a id="b5b-origin"></a>
## § `b5b-origin` — B5b — why the unconsumed-dated-artifact check exists (the 7/30 and 7/29 cards)

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

   > **Why this step exists.** B5 reconciles `CATALYSTS.tsv` *events*; nothing reconciled the *artifacts*. A frozen grading card is written days ahead precisely so the grade cannot be improvised after the fact — but until 2026-07-31 **no boot step ever looked for one.** On 7/30 `GRADING_CARD_20260730.md` sat unconsumed for its own print, and the 7/29 FOMC labor-language card went ungraded, both discovered only when a spawn happened to boot on 7/31. *(Audit item A2; boot-step half authorized by PROME 7/31. Whether an unconsumed card should also BLOCK closeout is a separate open question in Will's disposition batch — **do not** treat this step as a closeout gate yet.)*

---

<a id="b5b-ruled-no-gate"></a>
## § `b5b-ruled-no-gate` — B5b — the RULED-NO-GATE decision of 2026-07-31 and its stated basis

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

   > ✅ **RULED-NO-GATE (Will, 2026-07-31, via `inbox/2026-07-31_from-PROME_remaining-rulings-RULED-implement-next-boot.md`).** The open question above — *should an unconsumed card also BLOCK closeout?* — is **decided: keep B5b, add NO closeout gate.** One mechanism, boot-side. The ruling's stated basis is LABOR's own honest-limit reasoning: a closeout gate would fire on the session that is *already too late* to help, while the boot check catches the card at the next available moment either way. **Do not re-open this without a new failure.**

---

<a id="c2-0-worked-example"></a>
## § `c2-0-worked-example` — C2-0 — the LAB-06 worked example that bought the stale-high-confidence sweep

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

**Why this exists:** every gate in `PREDICTIONS_SCOREBOARD.md` §C runs at **registration** (boot B4, *"before writing any NEW prediction"*). LAB-06 was registered 2026-02-18 and sat at **80% for five months** — no gate ever looked at it again, and it reached scrutiny on 7/31 only because a session happened to ask *"what would I be embarrassed by on Monday?"*. **That is luck, not a control**, and it cost 0.64 of Brier and moved the book's mean from 0.256 to 0.293. **The exposure is the STALE high-confidence row, not the newly-written one** (`[[finding_registered_gate_captures_attention]]` — the gated instrument absorbs the attention; sweep the un-gated ones separately). ⚠️ **Do NOT read a hardcoded flag-list here — RUN the sweep.** This line used to name *"LAB-08 (65%) and LAB-10 (75%)"* as currently flagged; **by 2026-08-23 both had moved and the sentence was false on both counts** (LAB-10 **RESOLVED ❌ 2026-08-07**; LAB-08 **repriced 65% → 35% posted on 8/7**, so it no longer clears the ≥60% bar — its as-made 65% still governs SCORING). **A sweep whose worked example is a stale list teaches the reader the answer instead of the procedure**, and this is a boot-loaded file, so the stale list loaded every session. **Live result at the 2026-08-23 sweep: ZERO rows trip it** — the four OPEN rows are LAB-03 7%, LAB-12 30%, LAB-08 35%, LAB-11 50%, all under 60%. Re-derive it each time from `workbook/PREDICTIONS.tsv` (OPEN **and** ≥60% **and** confidence unmoved 60d+); if the answer is zero, say zero.

---

<a id="recipient-paths-incident"></a>
## § `recipient-paths-incident` — RECIPIENT PATHS — the 2026-08-07 stranded-packet incident and why the rule lives in the charter

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

> ⚠️ **Why this lives in `CLAUDE.md` and not in a note.** Writing to a non-existent path **does not fail** — `git add` creates it, the commit succeeds, and from the sender's side the packet looks delivered. **`orphan_check.sh` cannot catch it either**: the file is committed, so it is not an orphan. The only signal is that nobody ever replies. On 2026-08-07 SAM found **two LABOR packets stranded at `AGENTS/PROME/`**, one of which carried a **six-session escalation** (`SIG-W-20260727-006`) that PROME had therefore never seen. SAM had made the identical mistake three times, and **the correction only stuck once the path went into SAM's own `CLAUDE.md`** — because the flag itself arrived as an inbox packet, and the MAIL rule above says don't read inbox at normal boot. **A routing fix delivered by the broken channel cannot fix the channel.** *(Both stranded packets were migrated by PROME at `86aa38645` and are in `PROME/inbox/processed/`; verified 2026-08-12.)*

---

<a id="published-tsv-archaeology"></a>
## § `published-tsv-archaeology` — FILES — `workbook/PUBLISHED.tsv`: the three usage rules and the measured cost of the distinctive-form rule

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

⚠️ **Three usage rules bought the hard way:** (a) `asof` must be an **ISO timestamp, not a bare date**, whenever a metric can change twice in one day — a date-only tie makes the reader sort by value *alphabetically* and it will report the **retracted** value as current (hit live 7/31; → HENRY packet, BD-10); (b) the `value` column must hold the **distinctive form that actually appears in prose** (`3.4->3.1%`, `202,750`), never a bare percentage — bare `10%` returned **1,785 hits**. ⚠️ **KNOWN COST, measured 2026-08-23 — this rule trades one failure for another and you should know which you are buying:** a "distinctive form" contains punctuation, so `NUM_RE.fullmatch` fails and the needle is typed **TEXT** — and **a TEXT needle can never be demoted to 🟠 by `consumer_check`, by construction** (it hits the *"exact by construction"* branch before the context and sig-digit checks, and the collision pass only inspects numeric needles). **So this rule buys precision and pays in un-demotable 🔴s.** Live instance: `--old 32/75` returned **5 🔴 of which 1 was real**, the other four correctly-dated historical records. **Keep following the rule — the 1,785-hit alternative is worse — but treat a 🔴 on a text needle as UNGRADED, and check the path class yourself before packeting anyone.** Routed to HENRY (builder) 8/23; (c) `suppress_until` is **documentation only — the tool does not read it** (BD-10). |

---

<a id="grading-card-inventory-archaeology"></a>
## § `grading-card-inventory-archaeology` — FILES — grading-card rows: the repeatedly-restated inventory counts and why the cell is not to be trusted

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

⚠️ **Do not trust an inventory written here — `ls docket/*.md` is the answer** (this line said *"Currently live: none"* while `docket/graded/GRADING_CARD_20260828_QCEW.md` had been live since 8/7). ✅ **GRADED AND ARCHIVED 2026-08-28: `docket/graded/GRADING_CARD_20260828_QCEW.md`** — frozen 2026-08-07, **21 days early**, carried **LAB-08** and vector 8. **Graded same-morning off §4: the preliminary printed −79,000 ⇒ BAND E ⇒ vector 8 4 → 2, LAB-08 live 15% → 4%, and NO resolution row (the final lands Feb-2027 and scores as-made 65%).** 🔒 **The card did the thing cards are for: two pre-commitments written 21 days apart agreed and no judgment was exercised on the day.** **LIVE CARDS AT 2026-08-28: NONE** — `ls docket/GRADING_CARD_*.md` returns empty, which is the answer, not this cell. **Next card owed: ECI Q3, 2026-10-30** (quarterly-gauge rule, C2a). |

---

<a id="graded-dir-archaeology"></a>
## § `graded-dir-archaeology` — FILES — `docket/graded/`: the count that has now been restated three times

*(moved verbatim from `CLAUDE.md` 2026-09-07; not edited)*

**Contents are enumerated by `ls docket/graded/`, not by this cell** — it held 4 cards when this line was written and holds **7** as of 2026-08-28 (`GRADING_CARD_20260828_QCEW.md` added at today's grade; before that `GRADING_CARD_20260813_claims.md` + `FOMC_LABOR_LANGUAGE_20260819.md` at the 8/20 grade). ⚠️ **This count has now been restated three times and is exactly the class of cell the file warns about — trust the `ls`.** |

---
