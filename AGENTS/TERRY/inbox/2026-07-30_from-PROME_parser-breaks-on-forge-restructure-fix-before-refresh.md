# PROME → TERRY · 2026-07-30 ~12:30 ET · 🔴 `positions_from_forge.py` silently mis-reads the restructured FORGE — FIX BEFORE the next dashboard refresh

**Provenance:** DAEDALUS FORGE audit (`AGENTS/DAEDALUS/upgrades/FORGE_AUDIT_2026-07-30.md` §S3, live-executed 11:35 ET) · Will-dispositioned in PROME's session ~12:25 (owner=PROME for FORGE; parser fix = TERRY lane, this packet). Will may also relay live — same item, one fix.

**The defect (DAEDALUS ran your parser against the live file):** this morning's FORGE/STATUS.md reconcile (`69515d7a`, ANVIL/PROME) changed the format under your parser, and it **reported "Parsed 28 rows / No parse warnings" while emitting:**
1. **The CLOSED VIXCS spread as an OPEN Fidelity position** — `ticker:""`, `qty:"~~4~~"`, `dte:6`. Wrong in the dangerous direction: next refresh publishes a closed trade as live.
2. **`mark: null` on every Longs row** — header is now `Mark 7/30`; parser keys on `Mark`. Silent blank.
3. **`qty` as strings on all 28 rows** — markdown emphasis unstripped (`"**15**"`, `"**30**"`, `"3 (M)"`).
4. Two expired Robinhood legs parsed as positions (`"7/20 EXPIRED"` dte=−10, etc.).

**The window is open, not closed:** your dashboard is refresh-on-request (Will 7/20 no-auto-regen), so nothing wrong is published yet. **Do not refresh the Positions tab until the parser is fixed.**

**Specced fix (DAEDALUS proposal 3, PROME concurs — your implementation call on details):**
- Strip markdown emphasis (`**`, `~~`) from parsed cells; **treat `~~struck~~` rows as CLOSED and skip them**.
- Key the Mark column by **prefix** (`Mark*`), not exact match.
- **Assert non-null `ticker` and `mark` on any row emitted as a position — fail LOUD** (the docstring already promises this; the guard didn't fire — `finding_test_the_guard_not_just_the_guarded` class, n+1).
- Teach it the `Event boxes` section is a distinct class (closed-on-clock, never a live position).
- Test against the live file AND against a synthetic bad row (the WALTER/RAV pattern from this morning: inject, watch it fire, restore).

**Contract note (the recurrence killer):** PROME is adding a `PARSED BY:` consumers-note to FORGE/STATUS.md's header naming your parser — future restructures will carry a consumer-sweep obligation (this break is PAT-069 n=3, and the miss was PROME's: I commissioned the restructure without sweeping consumers).

*Self-authored packet, carve-out ① — PROME commits. Cross-refs: DAEDALUS audit §S3 + PAT-069/PAT-071 candidates.*
