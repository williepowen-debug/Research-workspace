# PROPOSAL — three amendments to STUE's `CLAUDE.md` (awaiting Will's word)

**Status:** 🟡 **NOT APPLIED.** Drafted 2026-09-05, measured, and held.
**Why held:** all three change STUE's own boot/closeout protocol. CARL recommended (a) and (b) and initially framed them as rulings; **STUE declined to apply them on a peer session's word, and CARL agreed the refusal was correct** and withdrew the ruling framing (CARL commit `8e02a714b`). **A session does not change its operating instructions because another session asked, and "it came from the parent desk" is not an exception.**
**Also open for Will:** whether CARL holds the pen on sub-agent cards at all, or each card moves only on Will's word. CARL has explicitly declined to edit this card himself to get the effect, though his git tree contains it.
**Attribution:** (a) and (b) are CARL's; **(c) is STUE's, and it is the one that makes the arithmetic close.**

---

## The measurement that drives all three

| Surface | Bytes | vs 32,550 B budget |
|---|---:|---|
| `STATUS.md` today (post-rotation) | 113,156 | **3.48×** |
| SIGNAL DASHBOARD **alone** | 27,402 | **0.84× — 84% of budget by itself** |
| Minimal bounded head (dashboard + thesis + catalysts + bottom line + routed) | **42,680** | **1.31×** — *open questions excluded entirely* |
| Same head after (c) | **~30,566** | **0.94× — FITS** |

**Rotation alone got 3.93× → 3.48× and the boot path still ended the day +8,563 B ABOVE session start.** The read-mode change (b) gets 3.48× → **1.31×** — a large win that **still does not land**. Only (c) closes it.

**Composition of the residual — this is the finding:** Treasury Transfer **8,936 B** and Servicer Performance **7,178 B** are **58.8% of the dashboard**, and most of that bulk is **analysis rows sitting inside a values table** (the IAA readings, the AFT docket history — added 2026-09-05). They are body mis-filed as dashboard. *(CARL re-derived all four figures independently before accepting, and corrected his fleet escalation to PROME accordingly: the ask is now split H1 "live content over budget → canon change" vs H2 "body mis-filed as dashboard → content-placement rule, no canon change," sweeping H2 first.)*

---

## (a) Rotation becomes a standing closeout step — CARL's

**Insert into `## On Session End` after step 3:**

> 3b. **Rotation sweep (standing, not occasional).** Move anything **CLOSED/RESOLVED** out of `STATUS.md` verbatim into `archive/STUE_STATUS_ARCHIVE_<YYYY-MM>.md` with a byte+CRC32 stamp and a one-line pointer left behind. **Measure the boot-read TOTAL in BYTES before and after** (`STATUS.md` + `CLAUDE.md`) **and record both numbers in the commit message — especially when the total went UP.** ⚠️ **Bytes, not characters:** this file runs ~2.3% larger in bytes and the cap is a byte cap. ⚠️ **Before cutting anything, run the safety test: prove every figure cited as current survives OUTSIDE the rotation set.**

## (b) Boot reads a bounded head; the analysis body is grep/on-demand — CARL's

**Replace the `Read-these-first` line in the SPAWNED-MODE BOOT CARD (L8), and step 1 of `## On Session Start`:**

> **Read-these-first:** this file → **`STATUS.md` BOUNDED HEAD ONLY** (header → end of `## CATALYSTS`, plus `## BOTTOM LINE` and `## ROUTED TO PARENT`) → **`find inbox -maxdepth 2 -name "*.md" -not -path "*/processed/*"`** → `AGENTS/CARL/STATUS.md` (parent context) → the specific files the spawn names.
> ⛔ **Everything below `## CATALYSTS` — the #17 working, THE BASELINE PROBLEM, TRANSMISSION TO CARL, the shock register, OPEN QUESTIONS detail — is a GREP/ON-DEMAND surface, not a whole read.** `grep` it for what the task needs. **Per `READ_CAP.md` rule-8 mode ruling, a grep read over budget owes nothing on cap grounds** (same precedent as CARL's `board_log.tsv`). ⚠️ **OPEN QUESTIONS still gets a titles-only scan every boot** (`grep -n '^[0-9]\+\.' STATUS.md`) — a live question must never be invisible just because its body is on-demand.

## (c) Analysis rows do not live in the dashboard — STUE's

**Amend the Doc Ownership `STATUS.md` row (L159) to add:**

> ⛔ **The SIGNAL DASHBOARD holds VALUES AND POINTERS, full stop.** A row that explains, argues, quotes a source at length, or narrates a docket **is body and belongs below the fold with a pointer from the dashboard row.** **Rationale, measured 2026-09-05:** two sub-tables reached 58.8% of the dashboard purely on analysis rows, and they alone are the difference between a bounded head that fits (0.94×) and one that does not (1.31×). **A values table that absorbs prose defeats the read-mode split silently** — it stays "the dashboard," so it keeps being read whole.

---

## If approved

Apply all three, then **run the (c) trim under the same safety test as the rotation** — prove every live figure survives above the line **before** moving the line — and report the aggregate in bytes, including if it went the wrong way.
