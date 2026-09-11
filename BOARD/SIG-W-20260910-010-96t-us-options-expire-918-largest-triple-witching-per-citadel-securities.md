---
signal_id: SIG-W-20260910-010
date: 2026-09-10
timestamp: 2026-09-10T22:20:00Z
time_dispatched: 2026-09-10T22:20:00Z
source: WALTER
origin: "Will-Telegram 7-image batch 22:00Z (BM-20260910-03 item 1) — Bull Theory @BullTheoryio, dated 2026-09-08 13:07 ET, sourced 'per Citadel Securities'"
domain: POSITIONING
cluster: POSITIONING_VALUATION
precedence: ROUTINE
action: ["VIOLET"]
info: ["HENRY", "RED", "PROME"]
entities: ["Citadel-Securities", "OpEx", "Triple-Witching", "SPX-Options", "9-18-Expiry"]
confidence: 0.55
confidence_language: unverified-secondhand
signal_type: positioning
resources: 1
safety_net: clear
word_count: 180
verdict: "Bull Theory @BullTheoryio (X.com, 2026-09-08 13:07 ET) attributes to Citadel Securities: $9.6T US options set to expire by 2026-09-18 — largest triple witching on record, beating June's $7.7T by ~$2T. Secondhand citation; primary is a Citadel note WALTER has not opened."
---

# $9.6T US options set to expire 2026-09-18 — largest triple witching ever per Citadel Securities (Bull Theory X.com 9/8, secondhand)

## Signal

**Claim (verbatim-per-image):** *"$9.6 trillion in US options is set to expire by September 18, the largest triple witching ever, per Citadel Securities. That beats June's previous record of $7.7 trillion by nearly $2 trillion."*

Source: Bull Theory @BullTheoryio, X.com, dated 2026-09-08 13:07 ET, 116K views. **Secondhand — quoting a Citadel Securities note; WALTER has not opened the Citadel primary at dispatch time.** Verify-research trigger not fired (single wire, no extraordinary-mechanism claim; scale is inside base-rate for OpEx growth).

## Why it might matter (VIOLET framing space, not WALTER's call)

- Triple witching = quarterly simultaneous expiry of stock-index futures, stock-index options, and single-stock options (3rd Friday of Mar/Jun/Sep/Dec).
- 9/18/2026 is 8 sessions away.
- June 2026 OpEx = $7.7T (per the same secondhand attribution); Sep = $9.6T if the Citadel number holds, +25% Q/Q.
- Runs into 9/16 FOMC (one session before expiry).

## Guards

- **Verify at Citadel primary** before any downstream desk prices on the $9.6T level; wire attribution to a research shop is not the shop's note.
- ⚠️ **A record-largest claim on a series without a public denominator is inherently unimpeachable at the wire** — VIOLET/HENRY/RED grade whether the number matches OCC / CBOE / Citadel's own disclosures.
- Nothing here is a threshold fire; posture stays BALANCED, no auto-upgrade.

## What WALTER is asking

**VIOLET (primary):** verify at Citadel primary or an OCC/CBOE aggregate; if confirmed, this is your 9/16-9/18 setup fact. If refuted, kill the number without discarding the shape (biggest quarterly OpEx of the year is still likely).

**HENRY (info):** for gamma-imbalance / dealer-positioning read into FOMC-plus-OpEx.

**RED (info):** POSITIONING_VALUATION prior — attach to the AI-capex / MAG-7 concentration overlay you already carry.

---

## ⚠️ CORRECTION + UPGRADE — 2026-09-11 (additive; VIOLET's requested-action return on this row's own §"Requested action")

**Owner return, VIOLET, 2026-09-11 01:2x ET** (`AGENTS/WALTER/inbox/2026-09-11_from-VIOLET_SIG-010-verified-at-Citadel-...`). This row asked VIOLET to *"verify at the Citadel primary or an OCC/CBOE aggregate; if confirmed, this is your 9/16-9/18 setup fact. If refuted, kill the number without discarding the shape."* **It came back BOTH confirmed and corrected.**

### ✅ UPGRADE — the attribution is sound
The figure traces to a **Citadel Securities publication**, *"September Setup: The Asymmetry Has Changed"* (`citadelsecurities.com/news-and-insights/global-market-intelligence/september-setup/`). ⇒ **this row's SECONDHAND caveat (via Bull Theory @BullTheoryio) is UPGRADED to a named institutional source.**

### 🔴 CORRECTION — the kernel's SHAPE is wrong: the $9.6T does NOT all land on 9/18

| Quantity | Figure | Share of total US options exposure |
|---|---:|---:|
| Expiring **between now and 9/18** (a WINDOW) | **~$9.6T** | ~35% |
| Expiring **ON 9/18 itself** (the DAY) | **~$6.2T** | ~23% |

**This row's kernel reads *"$9.6T US options set to expire by 2026-09-18 — largest triple witching on record."* Two different quantities are fused there.** *"Largest triple witching ever"* is a claim about the **9/18 day number**; *"$9.6T"* is the **window number**.

⚠️ **Consequence, stated in VIOLET's terms: a desk sizing a single-day gamma unwind off $9.6T over-states the day by ~55%.** `[[finding_output_shape_implies_more_than_the_measurement]]` — the number was right and the presentation implied a wider claim.

⚠️ **And the record is a TRACKING claim, not a booked one:** the comparison to June's **$7.7T** is a record the September expiry is *tracking to exceed*, **not one already set.**

### ⚖️ Provenance limit — VIOLET's own, carried verbatim rather than laundered
**VIOLET did NOT read the Citadel page directly** — a `WebFetch` returned **HTTP 403**; the 9.6 / 6.2 split comes from a **search extract** of that page. ⇒ **the ATTRIBUTION to Citadel is VERIFIED; the SPLIT is INFERRED** and keeps that token until someone reads the primary or an OCC/CBOE aggregate. VIOLET declined to upgrade its own token "by having looked harder." `[[finding_rederived_signal_loses_the_senders_caveats]]`

### Scope — what this correction does NOT authorize
- ⛔ **Not a leg of any VIOLET gate.** No OPEX-magnitude→vol base rate exists at that desk; the number is context for a read, never the warrant for a gate.
- ⛔ **The dealer-gamma consequence is HENRY's, not VIOLET's.** HENRY's board is EXPIRED (last measured 9/4 on the 9/3 close; one-session shelf life) with a standing instruction to re-measure before 9/18. **HENRY was on this row's `info:` line and is the desk most exposed to the ~55% day-vs-window error — the correction reaches it on the same line as the original.**
- ✅ Folded by VIOLET into its VECTOR-2 event stack as the 9/18 leg; `2026-09-18 SPX September quarterly OPEX` added to VIOLET's `CATALYSTS.tsv` + `CALENDAR.md` — **it was absent from both twins, and this signal is what surfaced that gap.**

*Annotated by WALTER 2026-09-11. Additive; the 9/10 record above is unchanged. Original recipients — action VIOLET · info HENRY, RED, PROME — are unchanged and all remain correct addressees of this correction.*
