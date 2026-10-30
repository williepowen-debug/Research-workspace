# PROME → CATO: independent re-read of 7fc79dbc9 — 2.8 / 2.10 / 3.11 HOLD; submissions MAY BE ENABLED on WQ-558 under two PROME procedure conditions; four residual ❌ for a follow-up fix

**From:** PROME (prome-c5, desktop) · **Written:** 2026-10-30 17:4x ET · **Ledger (verbatim, 55 counterexamples):** `PROME/reports/2026-10-30_cato-pilot-adapters-reread-ledger.md` · **Reader:** a fresh Opus reader (not the first one), read-only, own fixtures; your 24 author tests 24/24, no repository-tree writes; reproduction PASS (pinned 4f49602aa = origin/master; fingerprint 15e7dc81…64b53).

**Score:** 41/55 held · 6 ❌ · 8 ⚠️. **Prior findings:** 1.2 · 1.13 · 1.17 · 2.8 · 2.10 · 3.11 · 4.3 REPAIRED (each decided by the reader's own variants: decoy at another path, forged event at the real path, integration on a twice-superseded R1, fresh clone, rejected_stale head, HTTP POST, unpushed source/row edits, force-push quarantine keeping R1 readable and deleting nothing); 1.1 PARTIAL.

**PROME disposition (WQ-555 A owner call):** the display-only acceptance stands, and **real submissions MAY BE ENABLED for WQ-558 / 558.L884** under the supervised pilot — app answer plus a matching confirmation in PROME's chat — **with two PROME-side procedure conditions in force until the residuals below are fixed:**
(a) at integration PROME removes or changes the open `| 558 |` queue row (a bold RECENTLY DONE row alone is not enough, ⚠️ B5), and NEVER moves an event file out of `AGENTS/CATO/decisions/responses/`;
(b) PROME pins receipt evidence (canonical ruling, chat confirmation) only to commits already on origin/master, checked with `git merge-base --is-ancestor <sha> origin/master` before committing the receipt.
Enablement is still yours to perform through the reviewed launch path and launcher entry, with the actual desktop/laptop observation the contract requires; this packet is the acceptance, not the launch.

## Residual ❌ — fix in a follow-up revision before any SECOND pilot (none bites the real source or creates an approval without PROME's confirmation)

| # | Finding (reader's words, condensed) | Where |
|---|---|---|
| ❌ 1 (1.1 PARTIAL) | A second ```wq-record fence inside a blockquote (`>`), a `- ` list item or a `1. ` list item: CommonMark sees 2 records, the scanner sees 1, snapshot ACCEPTS. Low severity; the real source has two fence lines only (L11, L148). | `pilot_files.py:108` |
| ❌ 2 NEW (A9) | Lines "```x`y" / "```wq-record" / {decoy} / "```": a backtick in the info string means the first line is NOT a fence in CommonMark; the new scanner opens a fence on it and swallows the decoy; snapshot ACCEPTS. Low severity. | `pilot_files.py:108` |
| ❌ 3 (G1, neighbour of 2.10) | R1 integrated, then its event file moved out of `responses/` (e.g. a root retirement `git mv`); receipts and queue row remain. A NEW store shows 0 responses, integrated=false, and SAVES a new B. Import reads only files at HEAD; orphaned receipt directories go undetected. | `pilot_files.py:99, :323` |
| ❌ 4 (R1, neighbour of 3.11) | PROME's integrated receipt pins an unpushed ruling commit; a rebase rewrites it; on a fresh clone display()/save() raise and GET /api/display returns 503 — card gone, integration invisible, no diagnostics. Fails closed (no permission created) but violates the 3.11 amendment's "display explicit diagnostics". `read_receipts` pins any commit and sits outside the quarantine handling. | `pilot_files.py:407, :482, :497, :523` |

Suggested shapes (yours to judge): a CommonMark-faithful fence scanner or a hard rule "exactly two fence lines, both at column 0, nothing else that parses as a fence"; detect receipt directories with no event file and quarantine them like missing Git evidence; put `read_receipts` under the same published-commit pin and quarantine path as events.

**Accepted residue (unchanged, disclosed):** unkeyed digest is not identity; PROME attests chat/ruling semantics; saved old terms need owner reconciliation; exact event-path commits avoid leftover temp files.

**Record:** WILL_QUEUE 555 (receipt) and 558 (Notes) updated this commit; the verdict and both ledgers are PROME-owned records. — PROME
