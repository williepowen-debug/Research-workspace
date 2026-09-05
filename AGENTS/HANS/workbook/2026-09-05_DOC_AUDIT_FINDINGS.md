# HANS DOCUMENTATION AUDIT — 2026-09-05

Full findings narrative, rotated out of `STATUS.md` for the read-cap byte budget **by the very check it describes** (`scripts/doc_audit.py` C6 fired on the commit that added it — the guard's first catch was its own author).
Durable homes: mechanism → `scripts/doc_audit.py` + `CLAUDE.md` §RULE #1b · lessons → `workbook/ML.tsv` `ML-HANS-437`–`442` · figures → `workbook/PUBLISHED.tsv`.

---

## 🔧 DOCUMENTATION AUDIT (2026-09-05) — `scripts/doc_audit.py` NOW EXISTS AND THE DESK PASSES IT

**Asked to document this session correctly, I re-read my own surfaces and thought them fine. A script disagreed, 8 times, on its first run.**

| Found | Fix |
|---|---|
| `CLAUDE.md`'s band table still carried **"(live: 54.1 Aug flash)"** and **"51.0, services 48.5"** — **I deleted the stale value-mirror from STATUS this session and left its twin standing in the boot-read charter** | Mirror is **bands-only by rule**; levels live in the registry |
| **2 duplicate VX metric surfaces** (`10.02`≡`8.06` PMI, `11.02`≡`8.01` TTF). The 8/28 mitigation was the ritual *"update BOTH"* — **it failed on its very first outing: mine** | Both **RETIRED**. Boot excludes retired rows by design, so they cannot diverge. **Dedup, never sync** `[[finding_mechanize_the_cap_not_the_ritual]]` |
| 🔴 **`HANS-T-09`'s LEVEL leg had NO metric surface at all** — compound row, only the spread instrumented, so it could never fire on its own terms and a clean spread scan read "not met" either way | **`VX-HANS-3.09`** (Italy BTP LEVEL) created. **Every LEG now names a surface**, checked per-leg |
| 3 sovereign VX rows stale (`3.01`/`3.02`/`3.07`) — I'd fixed the registry and not the surfaces | Refreshed |
| This desk had **no `PUBLISHED.tsv`** — so `consumer_check --from-ledger` could never run, and a figure I retired *and forgot* was structurally un-checkable | **Created, 17 metrics, append-only.** It immediately found 3 live consumers on stale HANS figures |

**⚠️ The audit's own first version matched bare values and flagged UK CPI 2.9% against EA HICP 2.9%.** Fixed by declaring each metric's VX surface, not by suppressing the row — **a check that cannot name the series is guessing.** All 7 checks are **falsified by injection** in `test_hans.py` (44 tests, OK).

**🔴 THREE CORRECTIONS DISPATCHED THAT ONLY THE LEDGER SWEEP COULD FIND:**
- **WALTER** — `REGISTRY.tsv` row for me carries 4 superseded levels and reads *"5 fires OPEN"* (it is **4 OPEN of 5 logged**).
- **HAWK** — carries *"next Qatar decision ~END-SEPTEMBER"* as a dated catalyst. **Superseded: the force majeure was extended INTO NOVEMBER on 8/31.** Sent them the LNG/crude shuttle asymmetry, which upgrades their own barrels-not-shipped framing.
- **HENRY** — closed an **8/28 request I never answered**: they grepped for two figures and found nothing because **the pointer I sent them died in the same session I sent it** (I rotated its target hours later). Figures sourced, split by basis — the ~€40bn/mo runoff is ECB's own; the **>€500bn/2026 aggregate is secondary and I told them not to fold it.**

---



---

## STATUS summary block, rotated in at closeout 2026-09-05

## 🔧 DOCUMENTATION AUDIT (2026-09-05) — **`scripts/doc_audit.py` now exists; the desk passes it.** Findings → `workbook/2026-09-05_DOC_AUDIT_FINDINGS.md` · lessons → `ML-HANS-437`–`442`

**I re-read my own surfaces and thought them fine. A script disagreed 8 times on its first run**, incl.: `CLAUDE.md`'s band table still carried **"(live: 54.1 Aug flash)"** — I deleted that stale mirror from STATUS this session and **left its twin standing in the boot-read charter**; **two duplicate VX surfaces** whose 8/28 mitigation was the ritual *"update BOTH"*, which **failed on its very first outing (mine)** — both now RETIRED, because dedup beats sync `[[finding_mechanize_the_cap_not_the_ritual]]`; and 🔴 **`HANS-T-09`'s LEVEL leg had no metric surface at all**, so a compound row could never fire on its own terms (`VX-HANS-3.09` created; **every LEG now names a surface**). ⚠️ The audit's own v1 matched bare values and flagged UK CPI 2.9% against EA HICP 2.9% — fixed by **declaring each metric's surface**, not by suppressing the row. All 7 checks **falsified by injection**; 44 tests OK. **`workbook/PUBLISHED.tsv` created** — this desk had none, so `consumer_check --from-ledger` could never run and a figure I retired *and forgot* was structurally un-checkable.

**🔴 Three corrections dispatched that only the ledger sweep could find — WALTER** (my `REGISTRY.tsv` row: 4 superseded levels, and *"5 fires OPEN"* when it is **4 of 5 logged**) · **HAWK** (carries *"next Qatar decision ~end-September"* as a dated catalyst — **superseded, the FM ran to November**) · **HENRY** (closed an **8/28 request I never answered**: their grep failed because **the pointer I sent died in the same session I sent it**).

---

