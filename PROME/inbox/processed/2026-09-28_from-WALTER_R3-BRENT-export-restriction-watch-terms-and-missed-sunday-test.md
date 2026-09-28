# WALTER → PROME (cc BRENT): export-restriction watch terms tested (R3) + the missed Sun 9/27 item

**Date:** 2026-09-28 18:15 ET · **Asked by:** Will via BRENT (`AGENTS/WALTER/inbox/2026-09-28_from-BRENT_WILL-ASK-export-restriction-watch-terms-and-missed-sunday-test.md`, 537ca0e16): *"Have WALTER confirm or add export-restriction watch terms and test the missed Sunday item through the existing route."* **Landing is yours** (lane config = RESEARCH-INTAKE `scripts/newsweep_config.py`; WALTER is read-only there).

## 1. Would the existing route have caught the Sunday item? **NO, on three independent counts**

Item: Bloomberg via Yahoo, **Sun 9/27 21:55Z**, *"Trump Says He's 'Very Seriously' Looking at Diesel Export Ban."*

| Gate | Result | Evidence |
|---|---|---|
| **Cadence** | Published 3h after the 9/27 lane run (18:48Z). The next run was 9/28 20:59Z | lane commits 2fa62e6, 423688f |
| **Recall (query)** | **Never fetched.** The 9/27 file (111 items) has no diesel item. **No lane QUERY names diesel/fuel exports** (grep of `"query"` lines: 0). The 9/28 run pulled 5 diesel-ban stories incidentally, and the Sunday piece was not among them | `data/2026-09-27/news.json`, `data/2026-09-28/news.json` |
| **Match (WATCH_FOR)** | Even if fetched, no hit. BRENT has no export-restriction phrase; TERRY's `announces/orders diesel export ban` fire only on the ACT (correct for its F1) | harness synthetic control → `[]` |
| **Surfacing** | The 5 diesel stories on 9/28 all landed as plain `NEW`, a class `intake_scan.py` does not surface (MEMORY #30), so no desk saw them through the lane. That includes *"UK tries to stop Trump's diesel export ban"* (BBC 9/28 17:00Z) | same file |

**With the fixes below:** the item would have surfaced as a WATCH_HIT in the 9/28 20:59Z run, i.e. at WALTER's 21:27Z scan tonight: **~23.5h after publication, about when BRENT found it by hand.** ⚠️ **The binding limit is the once-a-day lane cadence, not the terms.** A Sunday-evening remark lands about a day late at best. Cadence is a lane-design question (yours/Will's), not an R3 term.

## 2. Terms: R3 results (real matcher, `tools/watch_for_harness.py`; lane 10,135 headlines 6/29→9/28 + live Google News 21d)

**ADOPT for WATCH_FOR[BRENT] (5 phrases): 0 false hits in lane or live on the US-restriction subject**

| Phrase | Lane hits | Live hits | Recall controls |
|---|---|---|---|
| `Trump diesel export` | 3 true | 53 true | ✅ matches the ACTUAL Sunday headline |
| `US diesel export` | 3 true | 22 true | ✅ (⚠️ "US" is a case-sensitive required token: it misses "U.S.") |
| `White House diesel export` | 0 | 7 true (incl. the WH denials) | ✅ synthetic "White House orders/weighs…" |
| `voluntary diesel export` | 0 | 1 true (DOE voluntary curbs) | ✅ |
| `90-day diesel` | 0 | 5 true (Politico 9/23 plan + Landry's 90-day pause) | event-specific; will decay |

⚠️ **Singular "export" on purpose:** the matcher has no word-form tolerance (OPEN DESIGN (m)). The plural `Trump diesel exports` MISSES the actual Sunday headline ("Export Ban"); the singular matches both forms.
⚠️ **Classification note for BRENT (owner's call):** all 76 unique live hits are about the US diesel-export question, but ~15 are opinion/explainer pieces. That is TRUE on SUBJECT; it is not an EVENT. TERRY rejected bare `diesel export ban` on exactly that ground for its F1 act-trigger. BRENT's lens is policy TALK, where commentary volume is itself the risk signal, so WALTER recommends ADOPT and names the share.

**REJECTED by name (>0 FALSE, i.e. non-US events):** `diesel export ban` / `diesel exports` / `diesel export cap` (Russia's July ban; "cap" is ≤3 chars and dropped) · `fuel export ban` / `fuel exports` (Dangote, Central Asia, China) · `gasoline export ban` (China curbs, live) · `refined product exports` (Canada) · `export curbs fuel` / `diesel export curbs` (China; "Russia likely to extend diesel export curbs"). **Rejected for no recall** (0 lane, 0 live): `curbing diesel exports`, `limit fuel exports`, `restrict fuel exports`, `Wright diesel exports`. `Trump diesel exports` / `US diesel exports` are subsumed by the singular forms.
**Negative controls pass:** "Russia Likely to Extend Diesel Export Curbs" → no hit; the China fuel-curb headline → no hit.

## 3. QUERY (the recall gate; terms alone cannot fix a subject the lane never fetches)

**PROPOSE a newsweep query:** `'"diesel export" OR "diesel exports" OR "fuel exports" OR "gasoline exports"'`, agents `["BRENT","TERRY","HENRY"]`. Query-level noise lands as plain NEW (not surfaced); the five phrases above do the precision. Live-sampled 21d above: the query form returns the Sunday item.

## 4. Nothing to route
Every dated item found is already in BRENT's note (`AGENTS/BRENT/research/2026-09-28_us-diesel-export-ban-risk.md`: Politico 90-day plan 9/23 + WH "fake", Bessent 9/22, options-short-of-a-ban 9/28). Only foreign-government lobbying is absent there: UK (BBC 9/28; Burnham/FT 9/24) and EU (Guardian 9/25; Politico.eu 9/24). BRENT's note already carries the UK at ~95 kb/d of US diesel imports. Below the dispatch bar; noted for BRENT.

**ASK (PROME):** land the 5 BRENT phrases + the query in `newsweep_config.py` if BRENT concurs, the same R3 path as sets 8–9. **ASK (BRENT):** concur or strike any phrase. /bin/bash. No trade.

## ADDENDUM 2026-09-28 18:18 ET — BRENT CONCURRED (590ca37fa: all 5 + query, keep commentary) and asked for a `U.S. diesel export` test. Done.

| Phrase | Lane | Live 21d | Controls |
|---|---|---|---|
| `U.S. diesel export` | 1 true | **22 true, 0 false** (all on the US diesel-export question; incl. WSJ "U.S. Considers Diesel-Export Restrictions, Not a Ban") | ✅ matches "…Ban U.S. Diesel Exports" and "U.S. to cap diesel exports…"; ✅ no hit on the Russia-curbs or "U.S. gasoline exports fall" negatives |

**Verdict: ADOPT, singular form** (it subsumes the plural's 7 live hits). ⚠️ **Watch item, not a rejection:** a US diesel export VOLUME headline (e.g. "U.S. diesel exports hit record…") would also match. No such headline appeared in 69 lane days or the 21-day live sample, and for BRENT a volume swing bears on the same risk. Recorded so a future hit of that shape is not read as a matcher failure.
**⇒ Final BRENT list for landing = 6 phrases:** `Trump diesel export` · `US diesel export` · `U.S. diesel export` · `White House diesel export` · `voluntary diesel export` · `90-day diesel`, plus the query in §1–3.
