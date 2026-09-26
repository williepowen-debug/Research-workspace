# HAWK → PROME · 2026-09-26 (Sat, 15:1x ET) · HAW-22 registered (WQ-296 A) + Kpler/Vortexa inquiry text for Will's hands

**Spawn:** PROME `prome-1d`, Tier 1, on Will's WQ-296 word (15:04 ET, verbatim: *"Approve A as a disclosed-loss forecast, retaining the uncalibrated probability and the warning that undisclosed damage can produce a misleading confirmation. Authorize the prepared quote request to each of Kpler and Vortexa. This authorizes inquiries only, with no subscription, payment or binding commitment."*). Record: `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`; DOCKET L508. **$0. HAWK sent nothing external. No trade, threshold, other confidence or score moved.** Inbox at spawn: 0 top-level, 0 WALTER (nothing new since the 14:5x drain).

## 1. HAW-22: what is registered

| Field | Value |
|---|---|
| Registry | `AGENTS/HAWK/thesis/PREDICTIONS.tsv`, new row `HAW-22` (10 cols, verified) + a dated preamble tally line (3 OPEN: HAW-19, HAW-20, HAW-22) |
| Letter | R1 from `AGENTS/HAWK/research/2026-09-25_L321_HAW19-successor_NOT-REGISTERED.md`, transcribed verbatim. The only additions are the WQ-296 warning and the confidence token |
| Confidence | **`65% UNCALIBRATED`**. The token sits in the cell itself, so it travels with the number. It is the v2 subjective placeholder, carried unchanged. It is not raised |
| Warning | On the front of the Prediction cell **and** in a grade-carry rule in the resolution cell: *"undisclosed damage can produce a misleading CONFIRM — a CONFIRM on this letter is a claim about what was DISCLOSED, never about capacity"*. The rule says any grade that omits it is itself a defect |
| Windows | Event window 2026-10-01 00:00 → 10-31 23:59 UTC · observation cutoff 12-21 23:59 UTC · resolution **2026-12-22, IMMOVABLE**. Registered 9/26, before the window opens |
| Verdict bands | FAILED (any candidate meets damage + only-path + declared irreversibility) · CONFIRMED only on a dated search log (final search 12/15–12/21) · UNRESOLVED-CANDIDATE (no credit) |
| Record | KB-HAWK-414. STATUS carries a HAW-22 row with the 65% (STATUS is the registration surface for `scripts/asmade_audit.py`). CATALYSTS L321 row → `MET-2026-09-26`. The research file has an OVERTAKEN banner; its filename is kept |
| HAW-19 | **Not touched.** Its DEFECTIVE INSTRUMENT encode stays on its 9/30 row (L491). HAW-22 does not need it: the succession pointer is in HAW-22's Notes |
| Superseded line | The CATALYSTS 9/11 and 9/25 rows said *"never register the uncalibrated 65%"*. Will's word retains the number explicitly, so the ruling supersedes that line, not HAWK. Noted on the row and in KB-414 |

## 2. Inquiry text, one per vendor (for Will to submit; inquiries only)

Both are web forms. **HAWK submitted nothing.**

### Kpler

- **Form:** https://www.kpler.com/company/contact-us. VERIFIED 2026-09-26: WebFetch returned the form, and the page title reads *"Contact Us: Connect with Kpler, Reach Out Today"*. `kpler.com/contact` returns 404.
- **Fields seen:** First Name, Last Name, Email, Phone, Company, **Enquiry** (required free text, maxlength 5000), Platform (select **Kpler**, not MarineTraffic), Department (select **Sales**), a terms checkbox and a newsletter checkbox (optional).
- **Alternative:** `/demos/request-demo` is also linked from the homepage. The contact form fits an inquiry better.
- **Paste into Enquiry:**

```
Research-seat quote request: daily crude exports by terminal (API), with point-in-time history.

This is an information and pricing inquiry only. It is not an order, trial sign-up or commitment of any kind.

We are a small independent research team. Please quote the shortest term (and state whether any trial exists) for ONE named research user with API access to: crude-oil exports by installation/terminal at DAILY granularity, realized cargoes only (no forecast/predicted trades), for all crude-export terminals in Russia (Baltic, Black Sea incl. CPC, Arctic, Pacific) and the Persian Gulf/Red Sea (Saudi Arabia, Iran, Iraq, Kuwait, UAE), with history from 2025-10-31 and POINT-IN-TIME (as-of/snapshot) retrieval of historical values.

Please also state:
(1) how a cargo's volume is assigned to a calendar day;
(2) how estimated or dark-fleet-imputed volumes are flagged;
(3) units and conversion basis;
(4) usage and licensing terms for internal research.
```

### Vortexa

- **Form:** https://www.vortexa.com/contact-sales, page title *"Contact Sales | Vortexa"*.
  - VERIFIED 2026-09-26 by curl with a browser user-agent (HTTP 200). WebFetch gets **403** on vortexa.com, so the page was never rendered.
  - The form is script-rendered (form id 1562 in the page data), so **its field list is UNVERIFIED**, including whether it has a free-text box.
  - `/contact` (general, form id 1019) also exists.
- **If there is no free-text field:** submit the form with the details Will is comfortable giving, and send the text below on the reply.
- **Paste:** the same vendor-neutral text as the Kpler block, unchanged (repeated below so each block stands alone).

```
Research-seat quote request: daily crude exports by terminal (API), with point-in-time history.

This is an information and pricing inquiry only. It is not an order, trial sign-up or commitment of any kind.

We are a small independent research team. Please quote the shortest term (and state whether any trial exists) for ONE named research user with API access to: crude-oil exports by installation/terminal at DAILY granularity, realized cargoes only (no forecast/predicted trades), for all crude-export terminals in Russia (Baltic, Black Sea incl. CPC, Arctic, Pacific) and the Persian Gulf/Red Sea (Saudi Arabia, Iran, Iraq, Kuwait, UAE), with history from 2025-10-31 and POINT-IN-TIME (as-of/snapshot) retrieval of historical values.

Please also state:
(1) how a cargo's volume is assigned to a calendar day;
(2) how estimated or dark-fleet-imputed volumes are flagged;
(3) units and conversion basis;
(4) usage and licensing terms for internal research.
```

**Changes from the 9/26 §5 draft:**
- Added the *"information and pricing inquiry only … not an order, trial sign-up or commitment"* sentence, which puts Will's no-commitment limit on the page.
- *"any trial"* became *"state whether any trial exists"*, so the text asks about a trial without requesting one.
- Nothing else changed.

**How to judge a reply:** the §4 criteria in `PROME/inbox/processed/2026-09-26_from-HAWK_paid-data-line-2-and-WQ-296.md` apply. A quote that fails (i) daily realized per terminal, (iv) point-in-time retrieval or (vi) day-allocation and imputation flags buys data the letter cannot use.

## 3. Surfaces updated

STATUS (Last Updated, L321 row, new HAW-22 row) · NEXUS_BRIEF (As-of, next-decision, predictions line) · SCRATCH (addendum; next-session item 1 is now only the 9/30 HAW-19 encode; the pending-decision line is struck) · CATALYSTS · KB-HAWK-414. No other boot or closeout legs were run in this spawn, and those in the SCRATCH next-session list are still owed: war-risk aggregate, dormant re-sweep, fingerprints, BOARD info lane.

```
COMPLETION — HAWK · 2026-09-26 15:1x ET · spawn prome-1d (WQ-296 A, Tier 1)
STATUS: DONE
CHANGED: AGENTS/HAWK thesis/PREDICTIONS.tsv (HAW-22 row + preamble tally), KB-HAWK-414, STATUS, NEXUS_BRIEF, SCRATCH, CATALYSTS, L321 research banner; this memo
RESULT: HAW-22 REGISTERED (row HAW-22, commit bba2e26fd): R1 verbatim, 65% UNCALIBRATED, event 10/01-10/31, cutoff 12/21, resolves 12/22 IMMOVABLE; undisclosed-damage warning verbatim on row + grade-carry rule. Two paste-ready inquiry blocks in §2 (Kpler form VERIFIED, Vortexa URL VERIFIED/fields UNVERIFIED)
GAPS: Vortexa form fields unseen (JS-rendered; WebFetch 403); HAW-19 DEFECTIVE encode deliberately left for 9/30 (L491); no other boot/closeout legs run
WILL_NEEDS: submit the two inquiry forms (his hands; inquiries only)
FOLLOW-UP: HAWK 9/30 HAW-19 encode (L491); DOCKET L508 -> MET; any vendor reply routes to HAWK for §4 criteria check
```
