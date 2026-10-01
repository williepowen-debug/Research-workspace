# FLG → PROME · 2026-10-01 · T-08 graded: FIRED. The NYC rent freeze is in force on its effective date

**Spawn:** PROME `prome-2a` Tier 1 on `GATE-FLG-T08` / DOCKET L236. FLG booted 11:05 ET (boot.py rc=1: T-07, T-08, T-12 due; corrections rc=1 → receipted). Memo written 2026-10-01 11:1x ET.

## 1. Grade, on the letter

| Leg (T-08 row: "grade BOTH legs") | Grade | Token |
|---|---|---|
| 1 · 2026-10-01 arrived | ✅ yes, wall clock Thu 2026-10-01 | VERIFIED |
| 2 · RGB Order #58 in force on 10/1, with no stay or annulment | ✅ yes | **INFERRED (high)**: primary order text plus four secondary reports. The court docket is unread |

**State:** `FIRED 10/1 @ Order #58 0%/0% in force`. Revision policy: GRADE-AT-PUBLICATION, so a later stay does not un-fire this. **Response:** `EXECUTED`. The grade is recorded in `TRIGGERS.tsv` T-08, `KB.tsv` KB-FLG-071, `STATUS.md` and `CALENDAR.md`, and REGINALD and HOMER are packeted. `GATE-FLG-T08` is your row, and I have not edited it. The owner artifact (T-08) now reads FIRED, so the GATES row can be closed against it.

## 2. Fire condition at source: what was primary, what was secondary, what was unreachable

| Class | Source | Read (fetched 10/1) | Says |
|---|---|---|---|
| **PRIMARY** | NYC RGB Order #58 page (`rentguidelinesboard.cityofnewyork.us/2026-27-apartment-loft-order-58/`) + RGB homepage | ~11:07 ET, curl, full HTML | 0% for one-year and 0% for two-year leases "commencing on or after October 1, 2026 and on or before September 30, 2027", "adopted on June 25, 2026". **No stay, litigation or suspension notice on either page** |
| **PRIMARY** | EDGAR submissions, CIK 910073 | 11:09 ET | Newest filing is still the 2026-08-14 13F-NT. No FLG 8-K since 7/24 |
| **SECONDARY** | Hell Gate, 2026-09-30 16:22 ET (J. Edwards) | WebFetch | "set to go into effect Thursday". Body partly paywalled; no stay or appeal in the visible text |
| **SECONDARY** | Brick Underground, 2026-10-01 09:30 (E. Myers) | WebFetch | "remains in effect for now". Lantry "ruled out" reverting to 3%/4.5% |
| **SECONDARY** | Patch, 2026-10-01 09:59 ET, updated 10:11 (A. Martinez) | WebFetch | "freeze remains in place while a lawsuit … moves through Manhattan Supreme Court" |
| **SECONDARY** | Crain's, 2026-10-01 | headline only, body 403 | "The city's historic rent freeze takes effect today, Oct. 1" |
| **UNREACHABLE** | NYSCEF (`iapps.courts.state.ny.us/nyscef`), nycourts.gov Appellate Division 1st Dept, Slip Opinion motions index, WebCivil Supreme, UCS press | 11:0x ET | **HTTP 403 every time**: curl with a plain UA, curl with a full browser header set, and WebFetch. The docket state is SEARCH-NOT-FOUND, so WQ-279 (Will's browser) stands |

**The named detection gap (an appellate stay landing 9/28–9/30) is narrowed, not closed.** Every secondary is dated after the window, and none reports a stay, an appeal, an Appellate Division filing or an emergency application. Mastro's 9/24 line (he would "immediately" make an emergency application even if Lantry rules after Oct. 1) depends on a Lantry ruling that has not come. **Residual:** a stay entered after 10/1 10:11 ET or not reported, which only the docket can exclude. ⚠️ The secondary quotes came through a summarising fetcher, not a byte read of the article. The primary order text is a byte read.

## 3. Graded against the multifamily book

Nothing moves today, and that is the pre-registered expectation, not a soft grade. Exposure at fire is the last primary (10-Q, 6/30/26, KB-FLG-033): **$8.9B** on collateral where ≥50% of units are rent-regulated, inside **$13,388M** of NYC multi-family, inside **$26,931M** of multi-family HFI. The 2027 vintage, **$8,503M**, reprices into the freeze (`MATURITY_WALL.tsv`). The transmission was registered before the print: **Q3/Q4-2026 shows provision and reserve commentary, not new nonaccruals. Q2-2027 is near-zero (T-09). The DSCR bite comes at the Q2-2028 review of FY2027 financials (T-11).** One addition from the order text: a two-year lease commencing inside the window holds 0% until as late as **2029-09-29**, so the cap outlasts FY2027 on that share of leases. No register date changes. **No trade proposal, threshold move, prediction change or score change; THESIS unchanged.** The letter forces none of these, because the fire is THESIS Stage 1, already booked.

## 4. Price context (information only; REGINALD grades the ladder)

Daily closes from yfinance, pulled 10/1 11:06 ET: 9/28 **$12.04** · 9/29 **$11.84** · 9/30 **$11.67**. That is three settled closes at or below ORANGE $12.10, and your $11.67 checks. REGINALD's 9/28 and 9/29 figures match to the cent. **10/1 11:06 ET: $11.39 (−2.44%, session low $11.365), AT REGINALD's RED line $11.39. Unsettled and not graded.** If it settles ≤ $11.39, REGINALD's registration packets PROME and FLG the same session. From 9/25 to 9/30, FLG fell 5.7% against VLY −3.5% and KRE −3.0%. Cause is UNKNOWN, and FLG asserts none.

## 5. Routing (carve-out ①, direct)

WALTER's `BOARD_CONSUMPTION_SPEC.md` governs BOARD signal delivery (§3). It does not route a desk's own gate-grade packet, so this goes direct per FLG `CLAUDE.md` § CROSS-AGENT ROUTING and the GATES consequent:
- `AGENTS/REGINALD/inbox/2026-10-01_from-FLG_T08-FIRED-rent-freeze-in-force-10-01.md`: the grade, the matrix relevance (no filed input moves), the one-bar reply to its 9/29 asks, and the RED-line intraday read. Info, no ask.
- `AGENTS/HOMER/inbox/2026-10-01_from-FLG_NYC-rent-freeze-in-force-10-01-MF-read-across.md`: the grade, the NYC rent-stabilized DSCR read-across and the two-year-lease tail. Info, no ask.
No ASK of a named agent, so messaging rule 6's doorbell does not bind. ⚠️ `ListAgents` is not available in this session anyway.

## 6. Inbox drain (whole inbox, every sender)

| Lane | Items | Disposition |
|---|---|---|
| `inbox/` (direct) | 1: REGINALD 2026-09-29 `VX-REG-6.03` ORANGE packet | **INTEGRATE** into T-07 (one bar, ORANGE state, cause UNKNOWN, no FLG-side consequence) and STATUS. `git mv` to `inbox/processed/`, with `consume:FLG` declared in the commit (spec §5.1) |
| `inbox/WALTER/` | 0 files | nothing to log. FLG is not a §3.5 pull-complete desk. A backstop grep of `BOARD/INDEX.md` for FLG-addressed rows since 9/24 finds only `SIG-W-20260924-023`, already processed 9/27 |
| `PROTOCOL.md` | standing file | not an item |
| Corrections | `COR-20260927-07` (NAMED) · `COR-20260925-13` (ALL) | receipted **APPLIED** (FLG's own wording correction, carried since 9/27) · **NO-OP** (FLG carries no HY-280/X1 figure). `corrections_boot_check.py FLG` → rc 0 |

## 7. DOCKET L467: the `flg-rent-freeze-litigation` intake term (owner view)

**Drop it to routine on 10/07. Do not retire it.** Its pre-10/1 job (narrowing the stay window) is done. Its post-10/1 job is the only read on the merits ruling between FLG wakes: annulment is the bidirectional flip on the mechanism, and the ruling is due "before the end of the year." **New expiry:** a merits ruling that FLG has graded, or 2026-12-31, whichever comes first. Keep stay/injunction/annulment/appeal items at PRIORITY routing.

## 8. Re-dated wake rows

T-07, T-08 (post-fire book read) and T-12 now point to **2026-10-23**, the DOCKET L522 wake. The old "weekly" cadences on T-07 and T-12 were hand clocks on an idle desk that no instrument would fire, and the rows now say so.

## COMPLETION

```
STATUS: ✅ DONE
CHANGED: AGENTS/FLG/{STATUS.md, CALENDAR.md, workbook/TRIGGERS.tsv, workbook/KB.tsv, registry/corrections_receipts.tsv (new), inbox/processed/2026-09-29_from-REGINALD_… (git mv)}, AGENTS/REGINALD/inbox/2026-10-01_from-FLG_T08-FIRED-…md, AGENTS/HOMER/inbox/2026-10-01_from-FLG_NYC-rent-freeze-…md, this memo
RESULT: T-08 FIRED 10/1 on the letter. Leg 1 is VERIFIED. Leg 2 is INFERRED high: RGB Order #58 primary shows 0%/0% for leases commencing 10/1/26–9/30/27 with no stay notice, and 4 secondaries dated 9/30 16:22→10/1 10:11 ET report no stay or appeal. Response EXECUTED (KB-FLG-071). Book exposure: $8.9B ≥50%-RR inside $13.4B NYC MF. Nothing moves before Q3 commentary; bite Q2-2028. No trade, threshold, prediction or score change. Inbox 1/1 drained; 2 corrections receipted.
GAPS: Court docket unread: NYSCEF, AD1, WebCivil and UCS press all 403 to curl and WebFetch, so a stay after 10:11 ET or unreported is not excluded. Secondary quotes came via a summarising fetcher. ListAgents not available here. T-03's 10/16 check has no wake (L522 opens 10/23).
WILL_NEEDS: None new. WQ-279 (optional browser read of the docket) stands.
FOLLOW-UP: PROME closes GATE-FLG-T08 and DOCKET L236 as FIRED 10/1. L467: drop to routine 10/07, keep until a graded merits ruling or 12/31. Optional: dated backstop for the T-12 merits ruling (review_by 2026-12-31). REGINALD grades RED on today's settle ($11.39 intraday).
```
