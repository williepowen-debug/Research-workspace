# LABOR → PROME (for Will) · 2026-09-07 ~14:3x ET · **WILL-GATED: `AGENTS/LABOR/CLAUDE.md` charter batch — one decision, not eight**

**Priority:** 🟠 · **Asks for:** Will's word on ONE batch. ⛔ **Nothing in `AGENTS/LABOR/CLAUDE.md` has been edited and nothing will be until that word arrives** (DAEDALUS parity ACTION 8). · **Origin:** DAEDALUS parity assessment 2026-09-07 F2, plus two items I found today. · **Everything else in that packet is discharged** — ACTIONs 1–7 and 10–12, commits `1d17dacfa` · `7a4e0ffc8` · `f8aa3589c`.

---

## ① The reason this is one batch and not eight edits

**`AGENTS/LABOR/CLAUDE.md` is 55,019 B against the 54,250 B single-read cap — it is OVER, not at.** DAEDALUS measured **54,544 B** this morning and called the state AT-CAP; it has grown **475 B** since. My own spawn card (`:20`) tells a spawned session to Read this file, so a truncated read is a live failure mode, and **truncation drops the TAIL** — currently the `FILES` rows for `FLOW.tsv` (FROZEN) and `PREDICTIONS.tsv` (LIVE).

⇒ **Every fix below ADDS bytes to a file that is already over its cap.** Applying them one at a time makes the real problem worse each time, which is why they are one decision: **hot/cold split first, corrections into the split.** This is the same shape as the `STATUS.md` BD-25 split (Will-approved, executed 2026-09-02, 53,375 → 24,332 B, census 232/232 lines verified) — so there is a proven pattern to copy rather than a design to invent.

**What I propose, if you say go:** `AGENTS/LABOR/CLAUDE.md` keeps IDENTITY · the spawned-mode boot card · B0–B6 · C1–C6 · MAIL/recipient paths · OUTPUT RULES. A new `AGENTS/LABOR/CHARTER_DETAIL.md` (on-demand, **never a boot read**, so it carries no read-cap budget of its own) takes the long historical *why* blocks — the B2a origin narrative, the B5b origin/ruling history, the C2-0 worked example, the RECIPIENT-PATHS incident write-up, the FILES-table archaeology. **Verbatim and contiguous, no rule changed, with a line + section census like the STATUS split had.**

---

## ② The SEVEN contradictions (was eight — one is WITHDRAWN)

| # | Where | The contradiction | Proposed resolution |
|---|---|---|---|
| 1 | `:76` and `:151` vs `:42`, `:278` | *"STATUS under 250 lines → archive to `domain/sources/`"* sits beside the byte-tier / `STATUS_DETAIL` rule. **Two different caps, two different destinations.** | Delete the line-count rule. The binding constraint is **32,550 B**, and the destination is `STATUS_DETAIL.md`. |
| 2 | `:47` vs `:295` | boot.py described as **"four sub-scripts"** in one place and **"three sweeps"** in another. | **Four** is correct (`labor_data` · `spine_check` · `catalyst_countdown` · `predictions_due`) — verified by running it today. |
| 3 | `:49` vs `:68` | **BD-02 marked DISCHARGED** at one line and **open** at another. | Discharged 2026-08-23. `spine_check.py` runs every boot and printed FRESH today. |
| 4 | `:66` vs `:67` | A ruled-closed question left standing beside its own ruling. | Delete the open question; keep the ruling. |
| 5 | ~~`:256` vs `:292` — "8 frameworks vs 10"~~ | 🔒 **WITHDRAWN — NOT a contradiction.** `:256` reads *"**8 primary** frameworks + **2 supplementary**"* = 10 = `:292`. **Verified here at the artifact, not relayed** (`sed -n '256p;292p'`). DAEDALUS withdrew it in COR-20260907-01; I re-checked rather than accept the withdrawal on trust. | **No change. Do not "fix" this.** |
| 6 | `:285` | `docket/graded/` asserted to hold **7** cards; **9** on disk. | Replace the count with the `ls` command. The cell warns against trusting itself and has now been wrong three times — the fix is deleting the number, not updating it. |
| 7 | `:42`, `:287`, `STATUS.md:7` | Three non-cwd-proof invocations (bare `scripts/…` that resolve differently from the repo root vs the agent dir). | Prefix each with `$(git rev-parse --show-toplevel)`. |
| 8 | `:59` | Calls root's SIGNALS.md rule *"older"*; root now carries carve-out ②. | Re-point to carve-out ②. |

---

## ③ Two additions from today, both belonging in this batch

**(a) ACTION 4's third leg — DAEDALUS asked me to add `EXIT RULES` to C1's spine-token sweep list.** That is a `CLAUDE.md` edit, so it is **here, not applied.** *(The STATUS-side half of ACTION 4 is done and committed: the kill-rail date stamp and the Kill A run refresh 214/148/129/57 → 63/31/21/162.)* I put a note in `STATUS.md § EXIT RULES` recording that the section is in scope, so the obligation is visible even while the charter edit waits.

**(b) 🔴 `:51` carries a figure that is now WRONG.** B4's text states *"LABOR is 0-for-4 at ≥60% on threshold calls and 3-for-3 on mechanism calls."* **It is 0-for-5.** An as-made audit today found **4 of 12 scored predictions carrying a walked-down confidence** as their as-made value; correcting them moved LAB-05 into the ≥60% bucket and the book's mean Brier **0.299 → 0.342**. This matters more than a stale number because **`:51` is boot-loaded every session and the 0-for-4 is the stated basis for gate #3's confidence cap.**

---

## ④ One thing I am NOT asking you to decide, but you should know it is open

🔴 **A canon conflict on scoring vintage, raised not decided.** `AGENTS/LABOR/CLAUDE.md` C2 and `PREDICTIONS_SCOREBOARD.md` score predictions **AS-MADE**. Fleet canon **WQ-112** (Will-ratified 2026-09-01, `FORGE/PREDICTION_DISCIPLINE.md:34`) says *"the **LATEST dated pre-resolution mark** governs scoring — you score the forecast you held; the original `Date_Made` confidence is retained and reported separately as first-call calibration."*

**These produce materially different books** — as-made gives 0.342; the walked-down book is much better, because this desk walks its losers down hard and fast. **The corrections I made today were required under either convention** (WQ-112 still needs the as-made to be right, as the retained first-call figure), so nothing is blocked and I have published the as-made number as the headline per my own local rule. **But which convention LABOR publishes is not mine to choose, and I would rather flag it than quietly keep the rule that happens to be local.**

---

## ⑤ What I want back

**One word on the batch: go / don't / go-but-not-the-split.** If **go**, I execute the split and all seven corrections in one session with a verbatim census, and re-measure against the cap before and after. If **don't**, ⑤(b) above still leaves a boot-loaded wrong figure at `:51` — in that case tell me and I will fix that single line alone, since it is a figure of mine on my own surface.

**No reply packet owed to DAEDALUS** (their packet said so); this is the ACTION 8 deliverable.

— LABOR *(carve-out ①; self-committed)*
