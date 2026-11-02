# nport_holders.py — README

**Status:** KEPT DEWEY TOOL (WQ-495.NPORT A — Will 2026-10-30 11:10 ET, verbatim *"495 - yes approved"*; record `PROME/proposals/2026-10-30_wq551-495nport-RULED.md`; DOCKET L880).
**Schedule:** NONE. No unattended or recurring run is granted by the ruling; it runs only when a DEWEY session runs it.
**Built:** 2026-10-22, from the REQ-DEWEY-20261022-007 v2 leg (report `AGENTS/DEWEY/output/2026-10-22_data-center-abs-cmbs-holders.md`). Stdlib only. $0: public SEC endpoints, no key.

## What it answers

*Which registered funds hold a named set of bonds or securitization deals, how much, and in which class?*

## What it reads

| Step | Source | Note |
|---|---|---|
| 1 | SEC EDGAR full-text search (EFTS, `efts.sec.gov/LATEST/search-index`), forms `NPORT-P`, your date window | one query per `--term` (an EFTS phrase) |
| 2 | each hit's holdings XML under `www.sec.gov/Archives/edgar/data/<cik>/<adsh>/` | falls back to `primary_doc.xml` when the indexed file name 404s (about 60% of the first real pass on 2026-10-22) |
| 3 | `<invstOrSec>` rows in the N-PORT namespace | kept when name + title matches `--match` (regex, case-insensitive) |

It sends a declared-contact User-Agent, as SEC requires; it never logs in and never pays.

## What it returns

- `--out` TSV: the **latest** position per (registrant, series, CUSIP), columns `adsh · file_date · rep_date · registrant · series · net_assets · name · title · cusip · balance · valUSD · pctVal · assetCat · restricted · url · class`, sorted by value.
- `class` = the class letter read from the title (else the name); when neither carries one, it is inferred from other funds' titles for the same CUSIP and **marked with `*`**.
- Optional `--raw` TSV: every matched row before the dedupe.
- stdout: positions, fund-series count, total value, fetch-error count and a by-class summary; stderr: progress and the first ten fetch errors.

```bash
python3 AGENTS/DEWEY/scripts/nport_holders.py \
  --term 'Vantage="Vantage Data Centers Issuer"' --term 'SWCH="SWCH Commercial Mortgage Trust"' \
  --match 'VANTAGE DATA|SWCH' --start 2026-07-15 --end 2026-10-22 --out holders.tsv
```

## Limits — state them in any report that uses the output

1. **Registered funds only.** Private funds, separate accounts and insurer general accounts are NOT in N-PORT (insurer-sponsored variable trusts are). An absence here is not an absence of holders.
2. **EFTS caps each query at 1,000 hits.** The script warns on saturation; split the date window and re-run.
3. **Class letter is not a rating.** Map class to rating from the deal's presale ladder.
4. **Mostly quarter-end positions.** N-PORT is filed monthly but made public quarterly, so the latest public position can be up to about three months old; `rep_date` is the as-of date, cite it.
5. **Inferred classes (`*`) are inferences**, from other funds' titles for the same CUSIP; they are not read from the row itself.
6. **Fetch errors are reported, never filled.** A filing that fails both the indexed name and `primary_doc.xml` is listed as an error and contributes nothing.
7. **Name matching is textual.** `--match` keeps any holding whose name or title matches; a loose regex admits unrelated issuers, a tight one misses re-named series. Read the `--raw` TSV before quoting totals.

## The selftest (the one the ruling names)

```bash
python3 AGENTS/DEWEY/scripts/test_nport_holders.py
```

Offline, no network. It feeds a **synthetic** N-PORT document (`scripts/fixtures/nport_synthetic_primary_doc.xml`, invented values, real namespace and element names) through the scanner's own `parse()` and `klass()` and checks: the non-matching holding is dropped, each output column lands in its named place, and the class letter is read from both title forms (`CLASS A2` and the bare trailing `E`). Falsified at build (2026-11-02): breaking the match filter or the class reader makes it fail.

**Not covered by the selftest:** the EFTS search and pagination, the network fetch and its fallback, the latest-position dedupe and the CUSIP class inference (those run inside `main()` and need the network). A real run's stdout summary and `--raw` file are the check on those.
