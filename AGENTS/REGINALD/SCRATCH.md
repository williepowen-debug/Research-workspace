# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

*(7/25 section pruned 2026-08-13 — 19d, promote-or-delete per lesson-14: the **perl EDGAR-table recipe** and the **regex-backtracking gotcha** → MEMORY §Findings; **"a stated basis is falsifiable, an unstated one isn't"** and the **control-covers-the-anticipated-case shape** → MEMORY lessons (the shape got two fresh instances today); the **EGBN two-route ACL cross-check** → MEMORY §Findings; the **small-bank-CRE-bid half-thought** → ROADMAP backlog; CCC/HY fire-#2 arithmetic DELETED as superseded by the full FRED series pulled 8/13. 7/17 section pruned 2026-08-10 — >3wk, per the lesson-14 discipline this time (same-session promote-or-delete, no unpromoted control-notes left behind): **the one live note — WALTER's BB/B sub-index gap on REG-T-03/04 — was PROMOTED to `registry/NOTES.md` §REG-T-03/04** before deletion; the other three (tripwire decomp design lesson, CFG beta-vs-substance, Brent overtaken) were already canon in ROADMAP/brief/STATUS. 7/10 section pruned 7/30 — its "two-clock header silences its own nag" note became MEMORY lesson 14 after sitting unpromoted 20 days.)*

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*

---

*(Sections 2026-08-27 (×2), 09-01 and 09-02 pruned 2026-09-24 at closeout, all >2 weeks old: rotated VERBATIM → `archive/SCRATCH_rotation_2026-09-24.md` (crc-stamped). The durable recipes in them (EDGAR/FFIEC fetch, perl table extraction) already live in `MEMORY_REFERENCE.md`.)*

*September29 dated tape/research/card-request notes rotated verbatim → `archive/SCRATCH_session-closeout_2026-10-14.md`,crc32 `6c22bdc8`. Existing KRE card/decision trail remains TERRY/Will-owned;re-check at any append.*

## 2026-10-07 PM — L527 session (PROME-spawned, Opus): working notes

**Instrument notes (not yet promoted):**
- ✅ **PROMOTED 10/10 → CALENDAR 11/05 row fixed (token on both machines).** FFIEC CDR JWT WORKS on the laptop (token in `FORGE/tools/market-data/.env` since 9/22) — the CALENDAR 11/05 row's "desktop-only" remark is stale; regeneration before 11/05 is still Will's.
- `fetch.py fred` CDN-stale class: used the cache-busted `fredgraph.csv?...&nocache=` route + `fred_fetch_vintage(basis='first-published')`; identical on every HY/CCC/B/BB cell 9/25–10/6.
- Independent price route that works from this box: `api.nasdaq.com/api/quote/<T>/historical` (UA + Accept json). Stooq now serves a JS proof-of-work page — dead for curl.
- RC-K average IB deposits ÷ period-end IB: ~1.33× EGBN every quarter, ~1.1× OZK, 1.34× CUBI in 2025 → [CR] deposit cost INCOMPARABLE there (KB ML-REG-180; lesson 42). Cause not chased.
- `firetime_check.py` reads quarter labels like `[12/24]` as day dates (Nano report: 3 flags, all quarter labels → KEEP). A detector false positive class worth telling DAEDALUS if it recurs.

**Things I noticed but did not dig into:**
- OZK −4.31% on 10/6 vs KRE −0.45%, no news found (one search). OZK desk's own <$45 band closed below 10/6 ($44.58) and 10/7 ($43.56) — the OZK desk grades it; OZK desk last committed 10/2.
- CFG FHLB advances 0.01B [9/30/25] → 6.36B [6/30/26]; +3.85B in Q2 alone, while CFG cut ~$1.5B Treasury brokered (INFERENCE: substitution). It is in the WQ-318 F3 line.
- STLFSI4 +0.34 in the week to 10/2. One week; not a level signal.
- ✅ **VERIFIED 10/10 at the 8-K (acc 0001193125-26-403391): $340M, $2.1B deposits, close early 2027; Bluevine banks through Coastal Community Bank → KB ML-REG-188 + ROADMAP BaaS thread.** Sub-reader side finding (NOT verified by me): VLY 8-K dated 2026-09-28 announces a merger agreement to acquire Bluevine Inc. (small-business fintech). If true, it touches my BaaS/sponsor-bank perimeter (WQ-228). Read the 8-K before citing.

## 2026-10-09 PM — pruned at closeout (same session)

Every note was promoted: monitor defects → FIXED `8255c2d13` (MEMORY LAST SESSION + lesson 43); 10/9 tape + FRED + claims → STATUS §THRESHOLD; FRED cache-busted route failure → MEMORY 0a-NEW; HBAN moneyness → POSITIONS; PROME prome-1e obligations → discharged at closeout (memo + receipt). Nothing left here.
