# HANS — post-commit audit, 2026-09-18 (rotated from STATUS.md for the read cap)

**Prompted by Will asking whether the session was properly documented.** I re-ran the checks on work I had committed an hour earlier and found three defects in it. All fixed in the same session; detail below, lessons at `ML-HANS-451`/`452`, rule at `CLAUDE.md` RULE #1c.

---

## 🔴 POST-COMMIT AUDIT (asked for by Will) — 3 DEFECTS FOUND IN MY OWN SESSION'S WORK, ALL FIXED

**I ran the checks again after committing, on work I had just written and therefore trusted. Three real defects.**
**① STATUS-TOKEN SEMANTICS — the serious one.** I superseded 7 KB rows as `SUPERSEDED-BY-KB-HANS-059`, fusing the canonical token with its successor pointer, and invented `EXPIRED-NOT-REFRESHED` for 3 rows — **without opening `STATE_VOCABULARY.md`, which root canon points at.** Two guards on this desk then disagreed about the same column: `boot.py` (exact membership) printed **"10 EXPIRED" when the truth was 3**, burying the real ones; **`doc_audit.py` C8 (`Status != 'ACTIVE' → skip`, an allowlist of ONE token) silently dropped 3 rows from the stale-value check — plus 2 `CORRECTED` + 2 `CONFIRMED` rows never checked at all.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** FIXED: one shared dead-PREFIX predicate in both guards · **unknown tokens resolve to LIVE on purpose** · boot now NAMES unrecognised tokens · KB data in canon form · **7 regression tests, mutation-verified (reintroducing the bug fails 3).** Boot §[7] now reads **3 expired**, which is true. → `ML-HANS-452`, `CLAUDE.md` RULE #1c
**② ML ID COLLISION, mine, same session:** I cited `ML-HANS-450` for the supplied-delta lesson — **already taken** by my 9/10 C4 lesson. Corrected to `451` here and **in the delivered DAEDALUS packet with a visible correction note**, not a silent swap.
**③ Doc counts drifted:** `CLAUDE.md` said 51 tests / 7 audit checks; actual 58 / 8. Corrected.
⚠️ **ALSO STANDING, UNFIXED:** the **ECB primary pull is INTERMITTENT** — consecutive boot runs gave a clean §[2] and then a triple failure (AAA 10Y + the DE base leg, so spreads were correctly not computed). **It fails LOUD and refuses to compute off a stale base, which is right** — but §[2] coverage is run-dependent, so *a blank §[2] is not evidence of a quiet board.*
