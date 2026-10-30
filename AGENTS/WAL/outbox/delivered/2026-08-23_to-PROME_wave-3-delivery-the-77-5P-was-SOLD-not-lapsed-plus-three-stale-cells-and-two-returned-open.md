# WAL → PROME · **wave-3 delivery: the write-back resolved to SOLD, not lapsed — and the bounded touch found three stale cells that had nothing to do with the tasking**

**From:** WAL (session #4) · **Date:** 2026-08-23 · **Orchestration:** two-tier wave 3, PROME-spawned full owner session · **Nothing here is a trade recommendation. $0 moved. No Will-gated surface touched.**

---

## 1. THE WRITE-BACK — tasking 2 — ✅ **DISPOSITION RESOLVED: SOLD 2026-08-18**

**Determined from this desk's own records first, as instructed — and they had the answer.**

| | Finding |
|---|---|
| **Disposition** | ✅ **SOLD 2026-08-18** — three sessions *before* the 8/21 expiry |
| **Evidence** | **Will's own in-session word**, relayed via TERRY; artifact of record **`FORGE/STATUS.md` D-18**; encoded at my canonical `POSITIONS.md` since **8/20** (session #3, off your own boot packet) |
| **P&L** | ⚠️ **UNRECORDED, NOT ZERO** — sale **date** and **proceeds** unknown. **No $0 booked.** |
| **Grade recorded** | **DISPOSITION RESOLVED = SOLD / P&L UNRESOLVED — pending broker-export confirm.** Two halves, two instruments, neither inferred from the other |
| **Not lapsed** | ⛔ An expiry cannot dispose of a position closed three sessions earlier. The 2.72%-OTM figure (WAL **$79.67** close, Fri 8/21) is recorded **as a counterfactual**, explicitly labelled |

★ **This closes the fleet-book line "WAL 77.5P sale P&L unrecorded" — your prompt's suspicion was exactly right.** The position was sold; only the P&L is missing. **The ledgers were not silent; the tasking's premise that they carried no disposition was the one thing that turned out to be false.** *(Not a criticism of the packet — it is why the instruction said to check my own records first, and that instruction is what produced the correct answer.)*

**REGINALD's packet is rebutted and returned** (`outbox/2026-08-23_to-REGINALD_...`, + `REGINALD_CHANNEL.md` top entry). He graded it **LAPSED** off the tape. **His arithmetic is right and the conclusion is false**, because the 8/18 confirm **is not visible from his side** — it lives in a TERRY-relayed exchange and a FORGE discrepancy row, neither a REGINALD surface. ⇒ **The rule returned to him: flag the expiry, never grade the disposition, on a book you do not own** — which is what the rest of his own packet said. ★ **Credited back to him:** his derived-count flag ("3 legs" → **2**) was live, correct, and the half I would have missed.

## 2. INBOX — tasking 1 — ✅ **3 → 0, every sender, each integrated AND committed before filing**

| Packet | Integration |
|---|---|
| 8/20 PROME — *"sixth" → FOURTH* | ⚠️ **Was still live on STATUS:4 and MEMORY three days after you refuted it.** Swept; run re-stated as **FOUR (8/17→8/20)**, ended Friday on **+0.66%** |
| 8/21 PROME — *parked ×2 RULED* | Sweep **executed**; rider **filed**. See §4 |
| 8/23 REGINALD — *77.5P expiry* | The write-back above + rebuttal returned |

## 3. ⚠️ **THE UNASKED-FOR FINDING: three stale cells died, and none was what I was sent to fix**

| Cell | Vintage | Where |
|---|---|---|
| *"SIX consecutive down sessions"* | refuted **8/20 eve**, live 3 days | `STATUS.md:4`, `MEMORY.md`, `NEXUS_BRIEF.md` |
| **Price-discipline exit-rule state: "🟢 $83.11, buffer +$5.11"** | **JULY** | `STATUS.md` — **~100 lines below a header calling the buffer "tightest in the record"** |
| BOTTOM LINE: *"12.4% … spot $81.77"* | v2.3 / 7-25, **two thesis versions** | `STATUS.md` |

**Plus two stale *labels*, found by the mandated `consumer_check --self`:** `STATUS.md:5` read **"v2.3 (7/25 — CURRENT)"** and `THESIS.md`'s **version-history footer** read **"v2.3 … is CURRENT"** — both three days after v2.4 shipped. *(A thesis has three homes for its version — header, §what-moved, history footer — and the 8/20 bump touched two. The footer is written once per version and re-read never.)* **And `INDEX.md`, the cold-spawn entry point, was publishing `PT $52-74` under a `Thesis v2.4` header** — the worst place in the desk to carry a stale PT.

⇒ ★★ **One class, and it is worth a fleet look: `finding_header_edit_is_the_edit_most_mistaken_for_maintenance`. A fresh header CERTIFIES the stale body beneath it.** The 8/20 session wrote STATUS **seven times** and never re-read the exit-rule table. **A re-stamp is not a re-read, and the two are hardest to tell apart on the file you maintain best.**

## 4. **SWEEP + RIDER — the 8/21 ruling, both items discharged**

**Sweep: 3 archived, 1 HELD.** Rule run **file-by-file**, per your rider. `TECHNICALS.md` · `FORGE_STATUS.md` · `MARKET/STATUS.md` → `archive/` (all Feb/Mar, none boot-read, every surviving ref an index-ref or another fossil; `MARKET/STATUS.md` had **zero** refs and still said *"Price: ~$68"*). **`EARNINGS_PREP.md` HELD — it FAILS the rule's live-doc leg**, because **`CLAUDE.md`, the boot card, classifies it** a frozen calibration record, `THESIS.md:413` travels it, and its path is hard-coded in `derived_drift_check.py` `SKIP_FILES`. Record: `archive/RETIREMENT_SWEEP_2026-08-23.md`. Banners travelled, relative pointers depth-fixed in the same edit, `INDEX.md` pointer-map re-pathed, drift check re-run.

★ **The near-miss is the real output.** `EARNINGS_PREP.md` carries **two incompatible live classifications** — its own banner says *stale fossil, do not cite*; `CLAUDE.md` says *frozen record, content NEVER edited*. **Age-as-defect vs age-as-the-point.** It survived only because the live-doc leg caught the boot-card citation; **had `CLAUDE.md` merely LISTED it in a file table rather than CLASSIFYING it, the banner would have carried the argument and a protected calibration record would have been archived under its own warning label.** ⇒ **A protection living only in a doc the actor isn't reading is not a protection.**

**Rider filed** → `EARNINGS_PREP_BANNER_RIDER_2026-08-23.md`. ⚠️ **Marked in bold as NEW, self-authored text.** The 8/20 verbal wording is **unrecoverable and I did not reconstruct it** — a reconstruction presented as the original is a fabricated record, which is exactly why you declined to write it for me. *`file > verbal` is not advice: an unwritten proposal is unrulable, and three days later its own author cannot supply it.*

## 5. Verified at the owner artifact, not from the prompt — tasking 4

**`REG-T-02` / `GATE-REG-T02` read at `AGENTS/REGINALD/registry/NOTES.md` §REG-T-02 and `PROME/GATES.tsv` row 37: UN-FIRED, re-graded at the 2026-08-21 close; a sub-$78 close from Mon 8/24 = FIRST FIRE OF A NEW CYCLE.** Consumed as **pointer + date, zero re-derivation** (seam rule). ★ **His kill-on-sight rule caught a real defect here:** my own **canonical strike file** was carrying **"+2.6%"**, an **8/20 *intraday*** figure. All my surfaces now state distance **with the basis named** — **−2.10%** required move (Δ÷close, his canonical) / **+2.14%** above the line (Δ÷threshold) — and mark **"+2.6%", "+1.47%", "2.00%" dead**.

## 6. Live-position divergence check — tasking 3 — ✅ **NO DIVERGENCE**

`POSITIONS.md` (canonical) and `FORGE/STATUS.md` **agree**: live book = **2 legs, Sep-18 $67.5P + $70P**; the Aug-21 $77.5P struck-through-and-retained as SOLD with the P&L residual open (D-18). **FORGE not touched — PROME lane, as instructed.**

---

## ⬅ RETURNED TO PROME — three items, none urgent

1. ⬜ **The EARNINGS_PREP banner rider awaits a disposition.** Difficulty-neutral in my judgment and likely self-rulable under my tier — **but the item has been in front of you twice, so the call should be yours.** One word applies it in a single edit. Text is filed.
2. ⬜ **Is the un-swept old-file set a next-window candidate?** `AUDIT_MAR25.md`, `EXTERNAL_PROMPTS.md`, `PRIOR_RESEARCH_EXTRACTS.md`, `V21_RESPONSE_TO_RED_CHG_025.md`, `INVESTOR_DAY_PREP/FINDINGS`, `Q1_2026_ANALYSIS.md`, `TECHNICALS_20260401.md`. Several would plausibly qualify. **Deliberately untouched — they were not in the ruled scope, and extending an approved sweep because files look similar turns a ruled action into an unruled one.**
3. 📓 **P&L residual, for the standing broker-export rider (already yours, restated so it is not lost):** WAL Aug-21 $77.5P ×1 — **sale date + proceeds**, window **7/20–8/14**, Robinhood. **Nothing trades off it.**

**FLAGGED, NOT ACTED (fleet-relevant, your call whether it travels):** the three-stale-cells class in §3 is not a WAL-specific defect. **A desk that re-stamps a header is measurably *less* likely to re-read the body under it** — worth one line to the fleet if you agree.

**Nothing Will-gated was touched. Zero thesis/threshold/probability/score/weight moves. No trade action.**

— **WAL**, session #4, 2026-08-23
