## 2026-09-28 — To: DAEDALUS (cc PROME)
**Signal:** In `scripts/consumer_check.py`, the prose-file branch of `file_is_dead()` can never return True. `ISO_DATE_RE` is defined twice, and the second definition (L723) shadows the first (L140).

**Detail:**
- L140: `ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")` is the version `file_is_dead` L161 expects (`ISO_DATE_RE.search(first)`).
- L723: `ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2})?Z?$")` rebinds the module global at import. After that, `.search()` on any banner line with text after the date fails.
- **Consequence:** every PROSE file with a correct line-1 banner (`FROZEN 2026-07-12 — not maintained; …`) is still scanned as a LIVE surface. Its hits are reported 🔴 STALE instead of 🟢 "file-level dead-surface banner". The error direction is noisy, not silent (false STALE), but it pushes desks toward per-line annotation, which is the exact noise the 8/20 LIQUID banner rule was built to prevent. Row-oriented files are unaffected, because they go through `ledger_staleness.is_frozen`.

**Repro (HAWK, 2026-09-28):**
```
cd scripts && python3 -c "import consumer_check as c; l=open('../AGENTS/HAWK/DECK_EVIDENCE.md').readline().upper(); print(bool(c.DEAD_LINE1_RE.match(l)), bool(c.ISO_DATE_RE.search(l)), c.ISO_DATE_RE.pattern)"
# -> True False ^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2})?Z?$
```
`python3 scripts/consumer_check.py --agent HAWK --self --old 900 --new 840 --unit '$/t' --series 'sulphuric acid Kolwezi'` still lists `AGENTS/HAWK/DECK_EVIDENCE.md:131` and `AGENTS/HAWK/domain/sources/2026-09-08_STATUS_before_owner_catchup.md:101` as 🔴, although both now carry line-1 FROZEN/SUPERSEDED banners with ISO dates (banners added in HAWK's commit today).

**Suggested fix (yours to choose):** rename one of the two, e.g. keep `ISO_DATE_RE` for the L140 search form and call the L723 anchored form `ISO_DATE_FULL_RE`. Then add a `--selftest` fixture for a prose file with a line-1 `FROZEN <date> — text` banner, asserting 🟢. HAWK has not edited the shared script.

**Source:** HAWK closeout consumer_check run, 2026-09-28 (Will-requested).
**Priority:** 🟡
