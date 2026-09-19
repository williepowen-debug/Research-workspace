# HANS — post-commit audit, 2026-09-18 (rotated from STATUS.md for the read cap)

**Prompted by Will asking whether the session was properly documented.** I re-ran the checks on work I had committed an hour earlier and found three defects in it. All fixed in the same session; detail below, lessons at `ML-HANS-451`/`452`, rule at `CLAUDE.md` RULE #1c.

---

## 🔴 POST-COMMIT AUDIT (asked for by Will) — 3 DEFECTS FOUND IN MY OWN SESSION'S WORK, ALL FIXED

**I ran the checks again after committing, on work I had just written and therefore trusted. Three real defects.**
**① STATUS-TOKEN SEMANTICS — the serious one.** I superseded 7 KB rows as `SUPERSEDED-BY-KB-HANS-059`, fusing the canonical token with its successor pointer, and invented `EXPIRED-NOT-REFRESHED` for 3 rows — **without opening `STATE_VOCABULARY.md`, which root canon points at.** Two guards on this desk then disagreed about the same column: `boot.py` (exact membership) printed **"10 EXPIRED" when the truth was 3**, burying the real ones; **`doc_audit.py` C8 (`Status != 'ACTIVE' → skip`, an allowlist of ONE token) silently dropped 3 rows from the stale-value check — plus 2 `CORRECTED` + 2 `CONFIRMED` rows never checked at all.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** FIXED: one shared dead-PREFIX predicate in both guards · **unknown tokens resolve to LIVE on purpose** · boot now NAMES unrecognised tokens · KB data in canon form · **7 regression tests, mutation-verified (reintroducing the bug fails 3).** Boot §[7] now reads **3 expired**, which is true. → `ML-HANS-452`, `CLAUDE.md` RULE #1c
**② ML ID COLLISION, mine, same session:** I cited `ML-HANS-450` for the supplied-delta lesson — **already taken** by my 9/10 C4 lesson. Corrected to `451` here and **in the delivered DAEDALUS packet with a visible correction note**, not a silent swap.
**③ Doc counts drifted:** `CLAUDE.md` said 51 tests / 7 audit checks; actual 58 / 8. Corrected.
⚠️ **ALSO STANDING, UNFIXED:** the **ECB primary pull is INTERMITTENT** — consecutive boot runs gave a clean §[2] and then a triple failure (AAA 10Y + the DE base leg, so spreads were correctly not computed). **It fails LOUD and refuses to compute off a stale base, which is right** — but §[2] coverage is run-dependent, so *a blank §[2] is not evidence of a quiet board.*


---

## Closeout re-cut (2026-09-18 late) — defects ④ and ⑤ added

## 🔴 POST-COMMIT AUDIT (Will asked) — **3 DEFECTS IN MY OWN COMMITTED WORK, ALL FIXED.** Full detail → `workbook/2026-09-18_POST_COMMIT_AUDIT.md`

**① STATUS-TOKEN SEMANTICS (serious).** I minted `SUPERSEDED-BY-KB-HANS-059` / `EXPIRED-NOT-REFRESHED` **without opening `STATE_VOCABULARY.md`, which root canon points at.** Two guards then read one column differently: `boot.py` printed **"10 EXPIRED" when the truth was 3**; **`doc_audit.py` C8 — an allowlist of ONE token — silently dropped 3 rows from the stale-value check, plus 4 never checked at all.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** Fixed: one shared dead-PREFIX predicate · **unknown tokens resolve to LIVE on purpose** · boot NAMES unrecognised tokens · **7 regression tests, mutation-verified.** Boot §[7] now reads **3 expired** — true. → `ML-HANS-452`, RULE #1c
**② ML ID collision** (`450` taken) → `451`, corrected **in the delivered DAEDALUS packet with a visible note**. **③ Doc counts:** said 51/7; actual **58/8**. 🆕 **④ PUBLISHED metric-name SPLIT** — I appended `EU_STORAGE_FILL_PCT` / `OAT_BUND_SPREAD_BP` for series already named, orphaning them **and leaving 67.33 and 87.4 reading CURRENT**, which silently disabled stale-consumer detection for both. Repaired by **continuing the established names** (append-only ⇒ never rename). → `ML-HANS-455`. 🆕 **⑤ `/tmp/enum.py` shadowed the stdlib** — the script ran as an import, **printed success, then crashed**; writes verified clean, but that was luck about ordering → `ML-HANS-454`. ⚠️ **UNFIXED:** the **ECB pull is INTERMITTENT** — a blank §[2] is not a quiet board.



---

# ROTATED OUT OF STATUS.md 2026-09-18 (session 2, read-cap rotate-tier)
*Verbatim, so nothing is lost by the move. STATUS carries a pointer to here.*

## 🔴 POST-COMMIT AUDIT (Will asked) — **5 DEFECTS IN MY OWN SESSION'S WORK, ALL FIXED.** Detail → `workbook/2026-09-18_POST_COMMIT_AUDIT.md`

**① STATUS-TOKEN SEMANTICS.** Minted tokens **without opening `STATE_VOCABULARY.md`**. Two guards read one column differently: boot printed **"10 EXPIRED" when the truth was 3**; **`doc_audit` C8 — an allowlist of ONE token — silently dropped 3 rows, plus 4 never checked.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** Fixed: shared dead-PREFIX predicate · **unknown tokens = LIVE on purpose** · boot names unrecognised tokens · **7 tests, mutation-verified.** → `ML-HANS-452`, RULE #1c
**② ML ID collision** (`450` taken) → `451`, corrected **in the delivered packet with a visible note**. **③ Doc counts** 51/7 → **58/8**. **④ PUBLISHED metric-name SPLIT** — new names for existing series orphaned them **and left 67.33 / 87.4 reading CURRENT**, disabling stale-consumer detection; repaired by **continuing the established names** (append-only ⇒ never rename) → `ML-HANS-455`. **⑤ `/tmp/enum.py` shadowed the stdlib** — ran as an import, **printed success, then crashed**; writes verified clean, but that was **luck about ordering** → `ML-HANS-454`.
⚠️ **UNFIXED:** the **ECB pull is INTERMITTENT** — a blank §[2] is not a quiet board.


⚠️ **STANDING PRIOR, SIX sessions:** every defect here found **from outside or by a script**, never by re-reading (8/28 ×4, 9/5 ×3, 9/10 ×7, **9/18 ×5**). 🆕 **Tonight added a new route: two came from a PEER's flag, and chasing one of those found the roll exposure on my own open fire.** The near-defects I avoided were caught by rules written **in advance**; the ones I shipped, by running the tools again. **None by reading.**

