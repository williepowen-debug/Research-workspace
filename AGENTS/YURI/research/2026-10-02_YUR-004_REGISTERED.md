# YUR-004 — REGISTERED (WQ-293 three corrections applied; YUR-001 superseded unscored)

**Author:** YURI (third session; spawned by PROME prome-96, Tier 1, DOCKET L434) · **Written:** 2026-10-02 (Fri) 11:5x ET (`date` in-session).
**Ruling:** Will 2026-09-26 15:54 ET, verbatim: *"Approve the prospective public-declaration test with three corrections: start at registration; use dates rather than decree numbers to determine eligibility; and count an operative declaration in the act's text even if its title is generic. Unread relevant text remains unresolved. Supersede YUR-001 unscored, preserving its partial reading."* Record: `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md` § Second ruling.
**Carried in from:** `AGENTS/YURI/research/2026-09-26_WQ-293_YUR-004_declaration-test-PROPOSED.md` (`5bf10bb90`).
**Carried over to:** `AGENTS/YURI/workbook/INTENT_LEDGER.tsv` row **YUR-004**, this commit.

---

## 1. THE REGISTERED LETTER (with Will's three corrections applied verbatim)

> **YUR-004 — Does the Russian state PUBLICLY DECLARE a mobilisation between 2026-10-02 (registration, Moscow date) and 2026-10-31?**
>
> **What this tests.** Whether a public act declaring mobilisation appears at the two places a Russian mobilisation decree is published. It does **not** test whether a decision was taken in secret. A MISS means *"no public declaration was found at the declaration sources"*. It never means *"no mobilisation decision occurred"*.
>
> **1. Instrument.** A presidential decree (Указ), or an equivalent named legal act (a presidential order, or a federal law), carrying a number, a date and a title, that **declares or orders mobilisation (general or partial), either in its title or in an operative paragraph of its text**. 2022 model: Указ № 647 of 21.09.2022, «Об объявлении частичной мобилизации в Российской Федерации». Under Federal Law 31-FZ a presidential decree declares mobilisation, so the decree is the decision. **Correction #3 (Will, WQ-293) applied:** an act whose TEXT contains an operative mobilisation declaration COUNTS even under a generic title. A title-level read that cannot see the text leaves that act UNRESOLVED, never MISS.
>
> **2. Declaration sources.** The act must appear at one or both of these, which are where the 2022 decree appeared on the day it was signed:
> - **(a)** the presidential block of the official legal-information portal, `http://publication.pravo.gov.ru/documents/block/president`, read in number order;
> - **(b)** the Kremlin's presidential feed, `http://kremlin.ru/events/president/news`, with `http://kremlin.ru/acts/news` as a variant. **Operational note added 2026-10-02:** source (b) requires a `User-Agent: Mozilla/5.0` header on curl requests — without it, this box receives HTTP 000. The 9/26 intermittence was that artefact.
>
> Both are read with `curl` over plain `http://`. HTTPS times out from this box.
>
> **3. Window.** Acts dated **2026-10-02 through 2026-10-31**, Moscow dates. **Correction #1 (Will, WQ-293) applied — window starts at REGISTRATION, not the 9/26 baseline read.** **Baseline at window open:** the presidential block was read at 15:46 UTC on 02.10.2026. Its highest number was **№ 712 (02.10.2026)** and it held **0 mobilisation titles**. Acts carried over the number threshold are NOT the gating criterion (see §3-bis).
>
> **3-bis. Eligibility by DATE, not by NUMBER (Correction #2, Will, WQ-293).** Any act whose **publication date is inside the window 2026-10-02 → 2026-10-31** is eligible for this test, whatever its decree number. The '№ 680 / № 712 above baseline' rule from the PROPOSED version is **dropped.** The baseline reads (№ 680 on 2026-09-26, № 712 on 2026-10-02) are kept only as a record of what the number-ladder stood at on those dates.
>
> **4. Checkpoints and grading cadence.**
> - **Weekly reads on Fridays:** **10/09, 10/16, 10/23, 10/30**.
> - **Final grade Sat 2026-10-31**, the end of DOCKET L432. Re-reads are allowed through **Mon 2026-11-02**, but only to fill coverage for acts **dated inside the window**.
> - Any single read may produce a CONFIRM early. A MISS is written only at the final grade.
>
> **5. CONFIRM (the row resolves `HIT`, reading DECIDED).** An act that meets §1, is dated inside the window, and is found at declaration source (a) or (b). The row cites the act's number, date, title and URL — and, where correction #3 applies, the operative paragraph of the text. A late-published act dated inside the window and found by 11/02 still confirms, and its publication lag is recorded.
>
> **6. MISS (the row resolves `MISS`, reading NOT-DECIDED at the declaration sources).** At the final grade, both of these must hold:
> - **(a) is covered continuously by date.** Every publication date in the window **2026-10-02 → 2026-10-31** has every listed act's title read, or the act recorded as a named gap. (Correction #2: coverage is by DATE, not by number.)
> - **(b) is covered for every date in the window.** Coverage is the union of the date ranges read across all the grading reads. A hole can be back-filled by paging back through the listing, up to 11/02.
>
> The MISS also needs zero titles that meet §1 at either source **and** zero acts whose generic title covered an unread text that could carry an operative mobilisation declaration (correction #3). Any act in the latter class stays **UNRESOLVED** on the grade line — never MISS — until its body is read.
>
> **7. If a declaration source cannot be read.** If (a) or (b) still has uncovered window dates on 11/02 after at least three host or scheme variants were tried (and the UA-header fix for kremlin applied), the row resolves **`STUCK (UNDETERMINED — <source> unreachable, dates <from–to> uncovered)`**. It never resolves MISS on one source alone, and it never stays OPEN indefinitely.
>
> **8. What never confirms (kill-on-sight at TITLE; still goes to UNRESOLVED on text, per correction #3).**
> - The routine **autumn-conscription decree** («О призыве … граждан на военную службу»). Autumn call-up starts on 1 October, so this decree is **expected inside the window**. Title-level kill. If the body text contains an operative mobilisation declaration ⇒ UNRESOLVED, not MISS.
> - Titles about mobilisation **preparation** («мобилизационной подготовке»), reservist training calls («военные сборы»), establishment-strength decrees such as № 419 of 12.06.2026 and **№ 700 of 28.09.2026** (same class), and martial law («военное положение»). Logged and routed as PREPARATION or adjacent. Not a declaration. **If any body text contains an operative mobilisation declaration ⇒ UNRESOLVED, not MISS.**
> - A press-cycle report, a belligerent headcount (300k or 500k+, under any attribution), a Russian denial, or the "secret decree of 1 October" rumour.
>
> **9. Every grade line carries the unread paths by name.** Every read in this row, including a MISS, ends with this line, updated with the variants tried that day:
> *"mil.ru unread (mil.ru http/https · function.mil.ru · structure.mil.ru — HTTP 000) · restricted numbers <list of gaps above baseline> unread by design · decree bodies scanned, no OCR — title-level only · kremlin.ru/acts/news <read / unread>, kremlin.ru/events/president/news read with UA 200. Implementation leg (MoD orders, call-up notices): DECLARED GAP, not tested by this row. Unread relevant text (acts in §8 whose body could carry an operative declaration): <list by № or 'none this read'>."*
>
> The absence is closable at the declaration sources only when every eligible-by-date act's text has been seen or named. The implementation leg stays a declared gap and is never silently dropped.
>
> **10. Routing.** HIT: OSPREY (theatre manpower) and HAWK (Leningrad Military District refill, NATO posture; a 12–18 month fuse, not near-term armed-conflict risk). A `SIG-YURI-WALTER-*` file goes in the same commit. MISS or STUCK: HAWK is the named consumer, and PROME closes DOCKET L432 with the reading and the unread-paths line quoted, not paraphrased.

## 2. YUR-001 → VOID-superseded, UNSCORED, reading preserved verbatim (WQ-293 ruling applied)

`workbook/INTENT_LEDGER.tsv` YUR-001 is set this commit to:
- `status` = **`VOID (superseded prospectively by YUR-004 on Will's WQ-293 word 2026-09-26; reading preserved verbatim; not scored)`**
- `reading` cell **unchanged** — the "NOT-DECIDED · PERIMETER PARTIAL (YURI 2026-09-25 re-read, window 09-19→09-25, …)" string is preserved byte-for-byte.
- `outcome` = **"VOID-SUPERSEDED, UNSCORED. The partial-perimeter grade from 2026-09-25 (`research/2026-09-25_L432_YUR-001_GRADE.md`, `0abe3353c`) stands as the record of what the primaries this box can reach held in the 09-19 → 09-25 window; it is not and must never be read as certainty that no mobilisation decision occurred. YUR-004 is the forward-only, bounded, gradeable replacement."**
- `resolved` left empty (VOID, not scored).
- `kill_on_sight` unchanged.

VOID keeps YUR-001 out of Brier. The 2026-09-25 grade memo is unchanged on disk.

## 3. SESSION OPERATIONAL NOTES (added to this desk's playbook)

- **Primaries playbook:** `http://kremlin.ru/events/president/news` returns 200 with `-H 'User-Agent: Mozilla/5.0'` and 000 with curl's default UA. The 9/26 intermittence recorded in YUR-004 PROPOSED §3 was a UA artefact, not a server flake. Added to §2 above and to the operational playbook.
- **PDF bodies:** `pdfminer.six` on the three Decree-302 list-amendment PDFs (№ 661 · № 674 · № 689) and on № 700 returns 0–3 chars (form-feed only). Confirmed scanned-image class, no OCR on this box. The row's unread-paths line continues to name them.
- **The L434 grade memo is `AGENTS/YURI/research/2026-10-02_L434_YUR-003_GRADE.md`** (same commit).

## 4. REGISTRATION RECORD

- Row id: **YUR-004**
- `registered` cell: **2026-10-02** (Moscow date, same as the window start — Correction #1).
- `resolve_by`: **2026-10-31** (final grade; re-reads allowed through 2026-11-02).
- Status token: **`OPEN`**.
- Reading: **"NOT-DECIDED · PERIMETER OPEN (window 2026-10-02 → 2026-10-31; baseline at open: pravo pres block highest № 712, 0 mobilisation titles; kremlin.ru/events/president/news with UA 200, 0 relevant hits)."**
- Kill-on-sight: as §8 above.
- If_confirmed_route: HAWK (named consumer) + OSPREY (theatre manpower) + WALTER `SIG-YURI-WALTER-*` same-commit.
