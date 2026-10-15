> ## ⚖️ DECISION 2026-07-25 — REPURPOSED, not retired (STALE_PUNCHLIST said "retire or hand to REGINALD")
>
> **Ruling: neither.** The *bank-watchlist* half is REGINALD's lane and is frozen below. The *method* half is now OTTO's
> single most important instrument and is promoted to the top of this file.
>
> **Why the reversal.** The punchlist wrote this doc off in March as a stale watchlist with heavy REGINALD overlap. That was
> right about the watchlist and wrong about the method. On 2026-07-25 an EDGAR full-text scan found **Triumph Financial's
> $60.5M Tricolor floorplan exposure** — a 7th named bank that ten months of press monitoring had missed — and, in the same
> query, established that **zero new US bank names** appeared in the whole OTTO-30 window. Press-sampling had previously
> missed Origin Bancorp for seven months the same way. **Retiring this file would have retired the one method that works.**
>
> **Live users of the recipe below (refreshed 2026-10-14):** **OTTO-33** (resolve Dec 31; EDGAR FTS q="Tricolor" is its instrument (1)), `scripts/shelf_halt_monitor.py` (OTTO-07's instrument since 7/25), and `research/TIER2_FORENSIC_SCREEN_SPEC.md`. *(OTTO-30 resolved FALSIFIED 2026-08-14 on this recipe's complete scan.)*

---

## 🔧 THE INSTRUMENT — EDGAR full-text search recipe (canonical; cite this, don't re-derive it)

**Endpoint:** `https://efts.sec.gov/LATEST/search-index?` + urlencoded params. **A compliant `User-Agent` header is mandatory**
or you get a 403 (`[[finding_edgar_403_user_agent_header]]`). `WebFetch` 403s here — use `urllib`/`curl`.

**Params:** `q` (quoted phrase), `forms` (e.g. `10-Q`), `startdt` / `enddt` (`YYYY-MM-DD`), `ciks` (zero-padded, for
single-filer history).

```python
import json, urllib.request, urllib.parse
UA = {"User-Agent": "OTTO Research <contact-email>"}
p   = {"q": '"Tricolor"', "forms": "10-Q", "startdt": "2026-04-15", "enddt": "2026-07-25"}
url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode(p)
r   = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))
r["hits"]["total"]["value"]   # count
[(h["_source"]["file_date"], h["_source"]["display_names"]) for h in r["hits"]["hits"]]
```

**Four rules, each learned by getting it wrong:**
1. **Filter by form type.** An unfiltered `"Tricolor"` query returned **676 hits**, overwhelmingly `NPORT-P` fund holdings —
   a fund *holding* a similarly-named security is not an exposure. Classify by doc-type **and direction**
   (`[[finding_edgar_entity_hit_direction_and_doctype]]`). Operating-company forms only: `10-Q`, `10-K`, `8-K`.
2. **Check each name's FIRST disclosure, not the filing you found it in.** TFIN's Q2 10-Q was in-window; TFIN's *first*
   Tricolor disclosure was a **2025-09-11 8-K**. Re-query with `ciks=` to get the filer's full history. Skipping this step
   is how a known-unknown gets mistaken for a forward discovery — twice now (`[[feedback_forward_discovery_prediction_spirit]]`).
3. **Positive-control every zero before banking it.** WINTERKORN confirmed "0 EART 2026-4 filings" only after checking
   2026-2 (98 hits) and 2026-3 (35 hits) returned normally. A zero from an untested query is not evidence
   (`[[finding_discovery_tool_wrong_slice_false_zero]]`).
4. **The filing date beats trade press.** Twice on 2026-07-25 primary sources settled in one query what trade press had
   wrong or a full news cycle stale.

---

> ### ❄️ The frozen bank-watchlist half moved to [`archive/EDGAR_8K_MONITOR_bank-watchlist_2026-03_to_2026-08.md`](archive/EDGAR_8K_MONITOR_bank-watchlist_2026-03_to_2026-08.md) (verbatim, 2026-10-14, s029).
> Bank 8-Ks are REGINALD's lane. The **FLG 8-K cc duty** OTTO wrote for itself on 8/27 ("first check OWED") was never run and is **retired**: FLG has its own print-driven desk that reads its own filings. **One method lesson kept from that half:** resolve a filer by EDGAR's `company_tickers.json` ticker map or by CIK, never by company-name search (FLG's filer renamed twice; a name search returns the wrong entity).
