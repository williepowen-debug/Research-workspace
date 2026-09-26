# YUR-004 — PROSPECTIVE PUBLIC-DECLARATION TEST for a Russian mobilisation (WQ-293) — PROPOSED, NOT REGISTERED

**Author:** YURI · **Written:** 2026-09-26 (Sat) 15:1x ET (`date` in-session) · spawned by PROME `prome-1d`, Tier 1, DOCKET L510.
**Will's word this answers (2026-09-26 15:04 ET, verbatim, record `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`):** *"I support a prospective, clearly defined public-declaration test. Preserve the earlier partial grade; don't turn it retrospectively into certainty that no mobilisation decision occurred. Keep the unread-source limitation visible."*
**State:** PROPOSED. The row id `YUR-004` is reserved here and is NOT in `workbook/INTENT_LEDGER.tsv`. It is registered only after Will approves the letter in §1 through PROME (WQ-293). ($0 · no trade · no threshold · convergence Score unchanged at 2.)

---

## 1. THE LETTER (for Will to approve word for word)

> **YUR-004 — Does the Russian state PUBLICLY DECLARE a mobilisation between 26 September and 31 October 2026?**
>
> **What this tests.** Whether a public act declaring mobilisation appears at the two places a Russian mobilisation decree is published. It does **not** test whether a decision was taken in secret. A MISS means *"no public declaration was found at the declaration sources"*. It never means *"no mobilisation decision occurred"*.
>
> **1. Instrument.** A presidential decree (Указ), or an equivalent named legal act (a presidential order, or a federal law), carrying a number, a date and a title, whose **title** declares or orders mobilisation, general or partial. 2022 model: Указ № 647 of 21.09.2022, «Об объявлении частичной мобилизации в Российской Федерации». Under Federal Law 31-FZ a presidential decree declares mobilisation, so the decree is the decision.
>
> **2. Declaration sources.** The act must appear at one or both of these, which are where the 2022 decree appeared on the day it was signed:
> - **(a)** the presidential block of the official legal-information portal, `http://publication.pravo.gov.ru/documents/block/president`, read in number order;
> - **(b)** the Kremlin's presidential feed, `http://kremlin.ru/events/president/news`, with `http://kremlin.ru/acts/news` as a variant.
>
> Both are read with `curl` over plain `http://`. HTTPS times out from this box.
>
> **3. Window.** Acts dated **2026-09-26 through 2026-10-31**, Moscow dates. **Baseline at window open:** the pravo presidential block was read at 19:09 UTC on 26.09. Its highest number was **№ 680 (25.09.2026)** and it held **0 mobilisation titles**. So any act numbered above № 680 is inside the window.
>
> **4. Checkpoints and grading cadence.**
> - **Wed 2026-09-30:** the new Duma's first sitting (Указ № 680). This is the first date a law can pass.
> - **Weekly reads on Fridays:** **10/02** (shared with the YUR-003 grade), **10/09, 10/16, 10/23, 10/30**.
> - **Final grade Sat 2026-10-31**, the end of DOCKET L432. Re-reads are allowed through **Mon 2026-11-02**, but only to fill coverage for acts **dated inside the window**.
> - Any single read may produce a CONFIRM early. A MISS is written only at the final grade.
>
> **5. CONFIRM (the row resolves `HIT`, reading DECIDED).** An act that meets §1, is dated inside the window, and is found at declaration source (a) or (b). The row cites the act's number, date, title and URL. A late-published act that is dated inside the window and found by 11/02 still confirms, and its publication lag is recorded.
>
> **6. MISS (the row resolves `MISS`, reading NOT-DECIDED at the declaration sources).** At the final grade, both of these must hold:
> - **(a) is covered continuously.** Every number from № 681 to the highest listed number either has a title that has been read, or is recorded as a named gap.
> - **(b) is covered for every date in the window.** Coverage is the union of the date ranges read across all the grading reads. A hole can be back-filled by paging back through the listing, up to 11/02.
>
> The MISS also needs zero titles that meet §1 at either source.
>
> **7. If a declaration source cannot be read.** If (a) or (b) still has uncovered window dates on 11/02 after at least three host or scheme variants were tried, the row resolves **`STUCK (UNDETERMINED — <source> unreachable, dates <from–to> uncovered)`**. It never resolves MISS on one source alone, and it never stays OPEN indefinitely.
>
> **8. What never confirms (kill-on-sight).**
> - The routine **autumn-conscription decree** («О призыве … граждан на военную службу»). Autumn call-up starts on 1 October, so this decree is **expected inside the window**. This is INFERRED from the call-up calendar and has not been read at a primary.
> - Titles about mobilisation **preparation** («мобилизационной подготовке»), reservist training calls («военные сборы»), establishment-strength decrees such as № 419 of 12.06.2026, and martial law («военное положение»). These are logged and routed as PREPARATION or adjacent. They are not a declaration.
> - A press-cycle report, a belligerent headcount (300k or 500k+, under any attribution), a Russian denial, or the "secret decree of 1 October" rumour.
>
> **9. Every grade line carries the unread paths by name.** Every read in this row, including a MISS, ends with this line, updated with the variants tried that day:
> *"mil.ru unread (mil.ru http/https · function.mil.ru · structure.mil.ru — HTTP 000) · restricted numbers <list of gaps above № 680> unread by design · decree bodies scanned, no OCR — title-level only · kremlin.ru/acts/news <read / unread>. Implementation leg (MoD orders, call-up notices): DECLARED GAP, not tested by this row."*
>
> The absence is closable at the declaration sources. The implementation leg stays a declared gap and is never silently dropped.
>
> **10. Routing.** HIT: OSPREY (theatre manpower) and HAWK (Leningrad Military District refill, NATO posture; a 12–18 month fuse, not near-term armed-conflict risk). A `SIG-YURI-WALTER-*` file goes in the same commit. MISS or STUCK: HAWK is the named consumer, and PROME closes DOCKET L432 with the reading and the unread-paths line quoted, not paraphrased.

## 2. THE EARLIER PARTIAL GRADE — PRESERVED EXACTLY, NOT RE-GRADED

YUR-001's reading stays as recorded (`workbook/INTENT_LEDGER.tsv`, `research/2026-09-25_L432_YUR-001_GRADE.md`, `0abe3353c`):

> **NOT-DECIDED · PERIMETER PARTIAL (window 09-19→09-25)**

**What it does NOT establish:** it records that no mobilisation instrument appeared at the five primaries this box could reach from 19 to 25 September. It is not evidence, and must never be read as certainty, that no mobilisation decision was taken in that window, because mil.ru was unread, five decree numbers (№ 671/673/675/676/677) are unpublished and scanned bodies went unread.

YUR-004 is **prospective only**: its window opens on 2026-09-26 above № 680, so no date that YUR-001 read is ever re-graded by this test. **Proposed disposition of YUR-001 at approval (PROME/Will's call, not applied here):** set status to `VOID (superseded prospectively by YUR-004 on Will's WQ-293 word 2026-09-26; reading preserved verbatim)`, with the reading cell unchanged. VOID keeps it out of Brier, so the partial grade can never be converted into a MISS. The alternative is to leave it OPEN as recorded.

## 3. EVIDENCE BEHIND THE LETTER (read by YURI 2026-09-26, 19:09–19:14 UTC)

| Probe | Result |
|---|---|
| `http://publication.pravo.gov.ru/documents/block/president` | 200 · 100,652 B. Numbers listed near the top: 660, 661, 665, 666, 667, 670, 672, 674, 678, 679, **680 (25.09)**. **0** `мобилиз/призыв/резервист` titles. **Baseline = № 680.** |
| `http://kremlin.ru/events/president/news` · `https://…` · `http://kremlin.ru/` · `http://www.kremlin.ru/…` · `http://en.kremlin.ru/…` · `http://kremlin.ru/acts/news` | **000 on all six today.** On 2026-09-25 the http listing returned 200 (63,098 B). ⚠️ **Source (b) is intermittent, and that is why §7 exists:** without a terminal rule, one flaky source would reproduce YUR-001's "OPEN forever". |
| `http://mil.ru/` | 000 (and on 4 variants 9/25) |
| `http://pravo.gov.ru/` | 200 |
| `rg.ru/documents` (Rossiyskaya Gazeta, another official publication) | 301 → 404. **Not proposed as a source.** Named here as an unchecked candidate substitute for (b), if Will wants one. |

**Why §7 fails loud rather than quiet:** YURI's 9/25 re-scope proposal loosened a check (`finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction`). This test keeps the loosening Will approved, dropping mil.ru from the MISS perimeter, and puts a guard on it: the §9 line is mandatory, and an uncovered declaration source gives STUCK, never MISS.
