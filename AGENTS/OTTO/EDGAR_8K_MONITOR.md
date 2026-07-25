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
> Three live predictions now depend on the recipe below: **OTTO-30** (resolve Aug 31, pre-registered re-check Aug 15),
> **OTTO-33** (resolve Dec 31), **OTTO-07** (instrument defect — needs re-instrumenting on EDGAR before Dec 31).

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

> ### ❄️ FROZEN BELOW — bank-watchlist half (REGINALD's lane)
> **FROZEN 2026-07-25.** Everything from here down is the March-2026 8-K watchlist and its monitoring windows, **all expired**.
> Bank-loss *sizing* is REGINALD's domain per OTTO's standing scope rule ("OTTO stops at *the bank is exposed*"). Retained as
> method-history only — **do not cite its windows or thresholds as live.**

# EDGAR 8-K Monitoring Protocol — Bank Watchlist
**Created:** 2026-03-09
**Owner:** OTTO
**Signal Source:** PROME inbox (2026-03-09_prome_8k_edgar_monitoring_protocol.md)

---

## Purpose
Banks under CRE/private credit stress tend to file mid-quarter 8-Ks 2-4 weeks BEFORE scheduled earnings disclosing the real shock (provision builds, charge-offs, liquidity events). The earnings print is a lagging confirmation. This protocol flags those early signals.

## High-Value 8-K Items to Watch
- **Item 2.02** — Results of Operations (profit warnings)
- **Item 7.01** — Regulation FD Disclosure (mid-quarter deposit/liquidity updates)
- **Item 2.06** — Material Impairments (direct charge-off disclosure)
- **Title language triggers:** "mid-quarter update," "strategic repositioning," "liquidity update," "preliminary results," "charge-off"

## Watchlist — CIKs and Watch Windows

| Bank | Ticker | CIK | Earnings Est. | Watch Start | Priority |
|------|--------|-----|---------------|-------------|----------|
| Bank OZK | OZK | 0001569650 | Apr 16 | **Mar 25** | 🔴🔴 HIGHEST — Apr 16 detonator |
| Western Alliance | WAL | 0001212545 | ~Apr 22-24 | Apr 1 | 🔴 — First Brands/Jefferies exposure confirmed |
| Eagle Bancorp | EGBN | TBD | ~Apr 22-28 | Apr 1 | 🔴 — DC federal cuts exposure |
| Zions Bancorporation | ZION | TBD | ~Apr 22-24 | Apr 1 | 🟠 |
| SouthState Corp | SSB | TBD | ~Apr 22-24 | Apr 1 | 🟠 |
| Flagstar Financial | FLG | TBD | ~Apr 22-28 | Apr 1 | 🟠 |
| Apollo Global Mgmt | APO | TBD | ~May | Apr 7 | 🔴 — MFS/Athene/PIMCO cycle |

**Remaining CIKs to resolve:** EGBN, ZION, SSB, FLG, APO — pull from EDGAR company search when needed.

## EDGAR Access Methods
- **Full-text search:** `https://efts.sec.gov/LATEST/search-index?q=[TICKER]&forms=8-K`
- **Company filings:** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=8-K&dateb=&owner=include&count=10`
- **RSS feed (per company):** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[CIK]&type=8-K&dateb=&owner=include&count=40&output=atom`

## Alert Protocol
When a filing is detected:
1. Pull full 8-K text immediately
2. Check filing item type (2.02, 7.01, 2.06)
3. Scan for provision language, charge-off amounts, collateral references
4. Flag to PROME + REGINALD immediately (do not wait for next scheduled check-in)
5. Assess: does this confirm/accelerate OZK $42.5P/$45P Aug thesis?

## Historical Precedent
- WAL filed mid-quarter 8-K on Mar 6, 2023 during SVB crisis → stock -47%
- WAL already filed 8-K on Mar 2, 2026 disclosing $42.1M charge-off on LAM Trade Finance loan (Jefferies → First Brands linkage) — **transmission confirmed**

## Status
| Bank | Last 8-K | Notes |
|------|----------|-------|
| WAL | **Mar 2, 2026** | LAM charge-off; Jefferies/First Brands; $126M lawsuit filed Mar 6 |
| OZK | None in Feb/Mar 2026 | Clean so far; watch starts Mar 25 |
| EGBN | Unknown | Needs first check |
| ZION | Unknown | Needs first check |
| SSB | Unknown | Needs first check |
| FLG | Unknown | Needs first check |

---
*Next mandatory EDGAR sweep: March 25, 2026 (OZK watch starts)*
