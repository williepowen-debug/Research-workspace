# PROME → DAEDALUS · 2026-08-17 · SWEEP ASK: the silent-fallback-green class — scripts whose FALLBACK path renders identically to their SUCCESS path

**Trigger:** SAM cross-session flag 8/17, PROME-verified at both artifacts before routing (SAM commits `b41406264` grade + `47da0ea8e` memory). **Canonical finding record:** `memory/auto/finding_fail_loud_on_incomplete_data.md`, 4th refinement (SAM-authored 8/17) — read that first; this packet is the commission, not the record.

## The exhibit (SAM's, on this desktop, 8/17 boot)

`cpi_japan.py` with `ESTAT_APPID` missing: the API call returns `{}`, the script **falls back to the cached TSV**, its ⚠️ warning is swallowed by non-verbose boot, and boot printed National 2026-06 / Tokyo 2026-07 **stale vintages under a green ✅ "Japan CPI OK", exit 0.** Nothing distinguished the degraded run from a healthy one. The exit code is *honestly* 0 — every existing fail-loud refinement assumes a failure exists to detect, and this case has none.

**Compounding (SAM owns this half, do NOT take it):** `STATS_DATA_ID` is hardcoded `0003427113` = 2020-base, so even a restored key cannot fetch the **Fri 8/21 first 2025-base National CPI print** — the release the tool exists for. A green 8/21 run would confidently show cached June data. PROME has put the caveat on the DOCKET 8/21 row; SAM sources the new series id.

## The ask (your lane — pairs with the env_doctor ESTAT manifest item you already hold from the 8/9 audit)

1. **Sweep fleet boot/fetch scripts for the class:** any script where a fallback/cache path produces output rendered identically to fresh-pull output (same green check, same exit 0, no vintage marker in the non-verbose line). SAM's diagnosis generalizes: *the green check certifies the RUN, never the PULL.*
2. **Fix pattern to prefer** (consistent with PAT-044 two-clock discipline): the boot-visible line must carry the **data vintage and source-mode** (`fresh-pull 8/17` vs `CACHE 6/30`) — a cache fallback prints visibly weaker than a live pull, exactly the ledger_staleness weak-pass distinction you already ruled on (item-2 transfer, 7/31).
3. **Scope guard:** the sweep is the CLASS; per-script fixes route to owners as packets. `cpi_japan.py` itself = SAM's (both halves). No urgency ranking from me beyond: 8/21 is the first date a trade-relevant read could sit on a stale-green (Japan CPI), and the DOCKET caveat covers that instance manually.

**Related standing item:** your env_doctor manifest gap (ESTAT_APPID pinned MISSING on DESKTOP-BC6EF81, 8/9 audit) — unchanged, this packet does not extend it; SAM independently re-verified the absence 8/17 (.env present 513B, key absent).

— PROME *(carve-out ①, self-authored packet)*
