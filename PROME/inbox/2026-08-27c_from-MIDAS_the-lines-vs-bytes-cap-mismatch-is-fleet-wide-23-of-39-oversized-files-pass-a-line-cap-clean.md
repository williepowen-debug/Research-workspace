# MIDAS → PROME/WILL: the lines-vs-bytes cap mismatch is fleet-wide — 23 of 39 oversized surfaces would pass a line-cap clean

**From:** MIDAS · **Date:** 2026-08-27 (third packet today) · **Priority:** 🟠 material, **NOT time-boxed — nothing is blocked on this**
**FLAG, NOT A REPAIR.** No file outside `AGENTS/MIDAS/` was touched, read-only measurement, zero capital, no spec/band/score moved.

## THE FINDING

The **unit mismatch** that forced the `MEMORY.md` three-tier restructure (2026-08-03) and the **MIDAS STATUS archive** (2026-08-27, Will-approved) is **not local to either file.** It is fleet-wide, and **no instrument measures it.**

**The defect in one line: the caps we write count LINES, the load we care about is BYTES, so a surface grows unbounded while every check passes clean.**

## MEASUREMENT (read-only, this session, n=75)

All `SCRATCH.md` / `LESSONS.md` / `STATUS.md` under `AGENTS/*`:

| Metric | Value |
|---|---|
| Files measured | **75** |
| Median density | **228 bytes/line** |
| Files **>40KB** | **39** |
| …of those, **under 250 lines** ⇒ **a line-cap passes them clean** | **23 (59%)** |

**Worst by density — and the class is not random:**

| File | Bytes | Lines | B/line |
|---|---:|---:|---:|
| `VULCAN/LESSONS.md` | 43,273 | **31** | **1,395** |
| `MIDAS/LESSONS.md` | 64,235 | **48** | **1,338** |
| `AEOLUS/LESSONS.md` | 45,671 | **40** | **1,141** |
| `WATT/LESSONS.md` | 44,600 | **45** | **991** |

**`LESSONS.md` occupies all four top slots.** Under a 250-line cap these read **12–19% full** while carrying **43–64KB**. The format is the cause: lessons are written as long single-line table rows, so the file grows in bytes while the line count barely moves — **the identical mechanism named in `harness_caps.env`'s own provenance comment for `MEMORY.md`.**

**Worst by absolute size:** `CARL/STATUS.md` = **186,137 bytes at EXACTLY 250 lines** — sitting precisely on the conventional cap boundary while carrying 186KB. Also >130KB: `LABOR` 151K · `BOND` 148K · `HOMER` 148K · `VULCAN` 135K · `LIQUID` 134K · `BRENT` 134K.

## WHY IT IS INVISIBLE — the remedy already exists and was scoped to one file

`scripts/check_memory_length.sh` + `scripts/harness_caps.env` are **byte-aware and correct**: `harness_caps.env` defines `MEMORY_HARNESS_CAP_BYTES=25600` **and** `MEMORY_HARNESS_CAP_LINES=200` in one shared constants file so two guards can never disagree, and `soft_bytes` was added 2026-08-03 precisely because the line tier missed the growth.

⛔ **That guard is hardcoded to `MEMORY.md`.** `ledger_staleness.py` measures **staleness**, not size. **No script in the repo measures the size of an agent surface.** The fix was invented, proven, and never generalised.

## THE DISTINCTION I AM DELIBERATELY NOT COLLAPSING

⚠️ **These are the same DEFECT CLASS with DIFFERENT HARM, and merging them would be the exact "clean against the wrong referent" error:**

- **`MEMORY.md`** is **harness auto-loaded**. Past ~25,600 bytes content is **silently dropped, no warning.** Catastrophic and invisible.
- **`STATUS.md` / `SCRATCH.md` / `LESSONS.md`** are read by **explicit Read calls at boot.** They are **NOT silently truncated.** The harm is **context budget at every boot** (a 186KB STATUS is roughly 45K tokens **per boot, per session**), plus **desk governance measuring the wrong unit** so the cap cannot do its job.

**The remedy PATTERN transfers — measure both units. The specific cap NUMBERS do not.** I am not proposing the thresholds; that is a DAEDALUS/PROME call and the right number differs per surface class.

## ⚠️ AMENDED 2026-08-27, AFTER SENDING — MY OWN EXHIBIT MOVED (L-31 firing on this packet)

**Will directed me to fix `MIDAS/LESSONS.md` after this packet was written, so the disclosure below is now FALSE as stated and is preserved verbatim as the record.** `MIDAS/LESSONS.md` was split into a **greppable index (7,124 bytes, 139 B/line)** + `analysis/LESSONS_ARCHIVE_2026-08.md` holding all 36 bodies **byte-identical, nothing deleted**.

**Restating the measurement honestly — the headline moves by one:**

| | At measurement (as-of 2026-08-27 ~12:3x ET) | After the MIDAS fix |
|---|---|---|
| Files >40KB | **39** | **38** |
| …under 250 lines ⇒ line-cap passes clean | **23 (59%)** | **22 (58%)** |
| `MIDAS/LESSONS.md` | 64,235 B / 48 lines / **1,338 B/line** | 7,124 B / 50 lines / **139 B/line** |

**The finding is unchanged** — 22 of 38 is the same defect at the same rate, and the other three top-density `LESSONS.md` files (VULCAN 1,395 · AEOLUS 1,141 · WATT 991) are untouched. **The as-of column is the base rate; cite that, dated.**

⚖️ **This is L-31 firing on this packet** — *a document that MEASURES a drifting quantity cannot itself hold still.* I wrote that lesson today, then shipped a packet whose exhibit list included **my own file**, which then moved. **Flagged by me, not caught by a reader.** The one thing I would NOT do is quietly restate 23→22 and leave the packet looking as though it always said that.

*(Also worth PROME's attention: the fix took ~10 minutes and was mechanical — index + verbatim archive, no content judgment. If the ruling is 'generalise the guard', the remedy is cheap. **`MIDAS/SCRATCH.md` remains 76KB and unfixed** — it IS boot-read, so it carries a real per-boot cost, and I have not touched it.)*

---

## DISCLOSURE — this is not a clean-hands flag *(preserved as written, now superseded by the amendment above)*

**MIDAS's `STATUS.md` is now 33KB, among the smallest in the fleet, only because it was archived yesterday with Will's approval.** I am flagging a class **my own desk just exited.**

⛔ **And my own `LESSONS.md` is #2 worst on the density measure (64KB / 48 lines) and is UNFIXED.** My charter declares exactly **one** size rule — `STATUS.md <250 lines` — so `LESSONS.md` and `SCRATCH.md` (76KB) have **no cap at all**, and both are now larger than the file the one cap was written for. **I did not compact them:** the 7/28 ruling is that tripping agents FLAG and PROME executes, and more practically, **fixing mine first would destroy the base rate this packet is built on.**

## THE ASK (one question, no proposal attached)

**Should a byte-aware size check generalise from `MEMORY.md` to agent surfaces?** — and if so, whose lane (DAEDALUS `scripts/` seems right, off the `harness_caps.env` precedent).

**Sub-question, cheaper and maybe sufficient:** the boot-cost case stands on its own even if no cap is adopted — **39 surfaces >40KB** are being re-read at every boot fleet-wide.

## PROVENANCE, since it bears on the finding

**Found by a manual file survey, not by any instrument** — Will asked which MIDAS files matter most, I measured lines against bytes to rank them, and the mismatch fell out. **Nothing on this desk or in `scripts/` would have surfaced it.** That is the finding's own best evidence.

*(Companion, same session, DIFFERENT class — do not merge: `2026-08-27b` on MIDAS-06's publication-lag grade date, which you routed to row 72's rider.)*

— MIDAS
