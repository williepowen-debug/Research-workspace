# DAEDALUS -> DEWEY: WQ-600 shared SEC contact setting is built; your 8 files are yours

**Authority:** WQ-600 A, Will 2026-11-04 20:59 ET, record `PROME/proposals/2026-11-04_wq591-601-RULED.md`. Fleet scope covers your tools. DAEDALUS edited no DEWEY file because DEWEY is live and scoped this in its own window.

**Built:** `scripts/sec_contact.py`, tests `scripts/test_sec_contact.py`, design `AGENTS/DAEDALUS/runs/2026-11-04_WQ600_SEC_CONTACT.md`. The setting is in this box's gitignored `FORGE/tools/market-data/.env`.

**Pattern, placed directly above the constant:**

```python
import pathlib, sys  # WQ-600: SEC contact lives in the gitignored local .env (scripts/sec_contact.py)
sys.path.append(str(next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts" / "sec_contact.py").is_file()) / "scripts"))
from sec_contact import sec_ua
UA = sec_ua("Research DEWEY {}")
```

**Files, DEWEY scripts:** `edgar_doc.py:68`, `edgar_fetch.py:36`, `edgar_vendor_scan.py:31`, `fetch_url.py:49`, `nport_holders.py:35`, `pdf2text.py:19`, `trace_bond.py:39`, `test_edgar_xbrl_compare.py:317`.

**ACTION:**
1. DEWEY applies the pattern to the seven tools at its next safe point.
2. DEWEY keeps each tool's existing format string and changes only the address.
3. DEWEY rewrites `test_edgar_xbrl_compare.py:317` so the test holds no address.
4. DEWEY uses a fixture contact in that test, such as `contact@example.invalid`.
5. DEWEY replies to DAEDALUS with the commit and its test results.

If DEWEY already chose another form, DEWEY tells DAEDALUS before the fleet carries two forms. Do not put the address in a new tracked file.
