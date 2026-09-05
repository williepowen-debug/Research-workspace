# ARCHIVED FROM STATUS.md — the 2026-08-28 §NEXT SESSION / infrastructure block

**Rotated out of `STATUS.md` on 2026-09-05** at the 250-line cap. Its live content is compressed into STATUS §NEXT SESSION; the operating rules it names (boot.py, fetch_eu.py, finding_check.py, test_hans.py, delivery-verification, fire counts) are canonical in `CLAUDE.md` §FILES and are NOT superseded by this rotation. Kept verbatim as history.

---

## NEXT SESSION — WHAT IS OWED (written 2026-08-28 so the next boot inherits it, not re-derives it)

**Desk state per DAEDALUS FLEET_MAP, ruled 2026-08-28 at the close of this session: L3 → L4, Conf H** *(their surface, their call — recorded here as a ruling received, not as a self-claim)*. Cited basis: signals flowing **and consumed** (HENRY has mine in `processed/`), record accruing, predictions resolving, falsification surface live, FLOW two-state clean. WALTER's liveness cell still reads "33d dark" and was **explicitly treated as a stale mirror its owner cannot write today** — do not re-litigate it here; it self-corrects when WALTER's write freeze lifts.

**The three L5 legs, in the order they come due:**
| # | Leg | Due | Notes |
|---|---|---|---|
| 1 | **First forward grade — `HNS-05` (ECB hikes 25bp to 2.50%)** | **2026-09-10** | The first prediction this desk resolves since the revival. ⚠️ Anchor is FIXED-CALENDAR-EVENT but grade on **the first rate decision on or before 9/10** — an emergency hike resolves it HIT early. Registry row `HANS-T-04` moves with it. |
| 2 | **Clean closeouts sustained TWO cycles** | next 2 sessions | The test is FLOW/PREDICTIONS/VX moving **with** STATUS, not after it. `ledger_staleness.py --nudge HANS` at every closeout. |
| 3 | **WALTER routing re-cut** | when WALTER's write freeze lifts | Owed on **their** side, not mine: `ROUTING_TABLE.md` L58 / L293 / L12 still say the UK is an open question with BOND as default — **that text is FALSE as of 8/28.** Line numbers recorded here so the debt survives if their session doesn't. **Do not edit their file.** |

⚠️ **STATUS is at 246 / 250 lines — ONE EDIT FROM BREACHING ITS OWN CAP.** Flagged here rather than left for the next session to hit mid-write `[[finding_mechanize_the_cap_not_the_ritual]]`. **First action next session: archive the §SECOND LIVE SWEEP block to `workbook/` once its corrections are absorbed into the tables** — it is a session narrative, and the tables carry the live values.

**Also live, no clock:** ECB Sept 10 · EA flash HICP Sept 1 · German flash PMI ~Sept 23 (`HNS-06`) · EU storage window Oct 1–Dec 1 (`HNS-07`, resolves 11/01) · next Qatar force-majeure decision ~end-Sept · `HNS-08` is **continuous-monitoring** — it resolves MISS the instant the Bund closes ≥4.00%, not at year-end.

**✅ INFRASTRUCTURE BUILT 2026-08-28 (Will approved the recs) — use it, don't rebuild it:**
- **`.venv/bin/python AGENTS/HANS/scripts/boot.py` is SPAWN PROTOCOL step 0.** 7 sections, ~10s.
- **`scripts/fetch_eu.py` — European PRIMARY pull, called by boot §[2].** ✅ **Bund proxy (euro-area AAA 10Y, daily) + DE/IT/FR/ES 10Y with derived spreads — ECB Data Portal, NO KEY.** ✅ **EU gas storage fill + gap-to-norm — GIE AGSI+ (key live in `FORGE/tools/market-data/.env`, installed 8/28).**
  ⚠️ **AGSI query form is `type=EU`, NOT `country=EU`** — the wrong form returns HTTP 200 with an empty array and reads as *"gas day not published yet."* Comment is in the source; don't re-derive it.
  ⚠️ **The storage GAP is a CROSS-SOURCE derivation** — AGSI fill minus a GEF norm. Script prints the caveat every run. **Follow-up: compute the norm from AGSI history.**
- ⚠️ **STILL MANUAL and named in boot §[2]: UK 10Y/30Y gilt** (no free daily source), plus the event-driven rows (ECB/BoE decisions, monthly PMI) which have no feed by nature. **A clean §[1]+§[2] is NOT a clear board.**
- **`workbook/KB.tsv`** — 34 facts on ZHAO's schema; **`Stale_By` is enforced by boot §[7]**. New facts go here, not into `ML.tsv`.
- **VX is now 40 live / 67 total.** 27 rows are FROZEN or RETIRED **on purpose**; boot excludes them by design. **Do not "helpfully" refresh a frozen row — read its named upgrade source first.**
- **`thesis/ECB_2026-09-10_PREREGISTRATION.md`** — grade **both** `HNS-05` **and** its §3b tactical-vs-regime read. Reporting only the binary is the failure that document exists to prevent.

- **`scripts/finding_check.py` — RUN `gate()` INSIDE any research script before shipping an empirical finding.** Two gates: INDEPENDENCE (does the robustness check vary something independent of what the claim is *about*?) and SUBSAMPLE STABILITY (auto re-run ex-crisis; fail on sign flip). ⚠️ **It catches 2 of the 3 failure modes that bit this desk on 8/28 — it does NOT catch construct validity** (*does my classifier measure what I claim?*). That one still needs a human question. Fleet adoption is DAEDALUS's to rule; HANS-local until then.

**⚙️ RUN AFTER TOUCHING ANY SCRIPT: `.venv/bin/python AGENTS/HANS/scripts/test_hans.py` — 36 offline tests, ~4s.** Regression-first: the falsy-zero staleness bug · the AGSI `trend`-as-string crash · the `country=EU` silent-empty trap · **every non-green band tier carrying its threshold id** (the severe tiers were the ones missing it) · and that boot **consumes** `fetch_eu`'s return rather than calling it for side effects.

**Standing hygiene bought this session — run these, don't rediscover them:**
- **Verify delivery at the RECIPIENT's tree**, never from `outbox/delivered/`: `find AGENTS/<RECIPIENT> -iname "*HANS*"`.
- **Fire counts come from `registry/HANS_T_FIRED_LOG.tsv`, not from prose.** *Did it fire?* and *how much does it tell us?* are two axes — never let a down-weighting caveat drop a row from the count.
- **Only 6 of 14 registry rows are daily-scannable** *(re-cut 2026-09-05; was 12/5 in four places)*. **A clean scan of the 6 does not clear the 14**; `T-12` is uninstrumented and cannot fire at all.

⚠️ **The session's own verdict on itself:** four separate defects surfaced on 2026-08-28 — no threshold registry at all, a miscounted fire, an `ACTIVE-STALE` third status, and a banner lost to a directory name. **All four were found from outside** (WALTER ×2, DAEDALUS ×2), **every one on a surface I had just written and therefore trusted.** The desk is current; the self-audit demonstrably is not. Treat that as the standing prior at next boot.

---

