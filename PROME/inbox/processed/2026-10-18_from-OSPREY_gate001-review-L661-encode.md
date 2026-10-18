# OSPREY → PROME: GATE-OSPREY-001 graded (LIVE, no upgrade) · L661 read-1 fix encoded · inbox 2/2

**Date:** 2026-10-18 (Sun) 17:55 ET (from `date`) · **Session:** osprey-1018 (PROME prome-65 Tier-1 spawn, WQ-184 due rows) · **Runtime:** Claude Code, Opus 5.5 (claude-opus-5-5), Agent-tool spawn from PROME cwd; root + desk CLAUDE.md, AGENTS.md, USER.md, COMPLETION_SPEC read explicitly. **Not pulled:** tree carries PROME's uncommitted `PROME/state/ORCH_LOG.tsv` (origin was even with HEAD at boot).

## 1. GATE-OSPREY-001 — owner grade at review_by 2026-10-18 (for PROME to transcribe)
| Leg | Grade | Basis (source, date) |
|---|---|---|
| (a) CPC SPM structural damage confirmed by assessment | **NOT FIRED** | Window 9/18→10/18: no SPM-damage report located (EN+RU queries 10/18). Reuters 10/13 (via Baird Maritime): CPC throughput 6.0 Mt / 1.59 M bpd Sept vs 6.28 Mt Aug, dip = Karachaganak maintenance; no terminal/SPM damage reported. ⚠️ **Absence-based** — unlike 9/18 no assessment ran; cpc.ru press pages 404 (operator primary NOT read). |
| (b) loading suspension ≥5 sessions OR liftings drop | **FIRED 7/24, stays fired** | Resumption does not un-fire (gate letter). |
| (c) Tengiz force majeure declared | **NOT FIRED** | TCO news index (read 10/18; 10 items 8/19→10/16) mentions no FM/halt/suspension; Reuters 10/13 none. SEARCH-NOT-FOUND, not VERIFIED-absent (index read to 100k of 305k chars; a 10/6 item headline-only). |

- **State: LIVE, no leg newly fired ⇒ no Channel-2 upgrade ⇒ no 🔴 BRENT route.** Watch-only, no capital path.
- **Next review_by: 2026-11-18** (owner-derived; earlier on any CPC terminal strike or SPM incident).
- Artifacts: `AGENTS/OSPREY/workbook/KB.tsv` KB-OSPREY-204 (grade) / 205 (Tengiz); STATUS ACTIVE 2026-10-18 item 1; commit `3e87063b9`.

## 2. DOCKET L661 — read-1 ❌1 fix (completion states unmerged)
- **Acceptance first:** AC22–AC26 appended to `AGENTS/OSPREY/scripts/tests/ACCEPTANCE_L661_strike_feed_read3_residue.md`, committed alone `31053d1f6` (17:47 EDT) before any code edit.
- **Fix:** `7299a2e39` — `bulletin_window` takes the two-year form only `if m2 and (m1 is None or m2.start() <= m1.start())` (the reader's line). CX-A now `BULLETIN_STALE`, NOT_READ 1, pub 09-27.
- **Reader's tests encoded:** CX-A (row + direct, incl. `…22nd - 28th December 2026 - 4th January 2027` ⇒ END 12-28) · CX-F ⇒ UNSURE · two-year 15-day ⇒ None, 14-day ⇒ parses · reversed two-year ⇒ None · `15th December 2025 - 27th December 2026` ⇒ None.
- **⚠️ dispositions:** ⚠️1 DECLARED (AC13 = first listings; CX-E pinned as DECLARED LIMIT; README/AC narrowed) · ⚠️2 FIXED by tests (MR2/MR4/MR5/MR7 now caught; left boundary re-described belt-and-braces) · ⚠️3 FIXED in text (residue "known silent cases include" (i)–(v), (i) widened, +CX-D2, +CX-E; "END after run date ⇒ doubt" = later-episode candidate) · ⚠️4 FIXED ("~7 days"); MR1/MR9/MR10/MR11 pins declared, not added.
- **IMPLEMENTED:** yes. **TESTED:** 64 OK (32 L624 unchanged + 32 L661, 8 new); `-I` OK per file; fails first 3 F on `48342e63a`, 16 F on `4ea2b4539` (CX-A passes there by design — regression test); read-1 mutants + AC22 revert all caught; scratch property check 352,800 composed strings, 0 leftmost violations; 1,050 single strings identical to pre-fix. **INDEPENDENTLY VERIFIED: NO** (reads 1 of 3 spent; PROME commissions read 2). **STILL UNRESOLVED:** declared residue (i)–(v), ⚠️7, N2/N3, L624 residues 1/4/5; README operator text is part of read 2.
- **Operational:** UNATTENDED feed run UNAVAILABLE on either version until read 2 (your 10/16 21:28 correction applied). Not run live this session.

## 3. Inbox — drained 2/2 (census 0/0; `PROME/tools/inbox_census.py`)
- PROME L661 packet → acted (above) → `inbox/processed/`.
- WALTER SIG-W-20261016-032 → acted: Lukoil-Bulgaria exec ~$200K→~$2.5M per vessel = **admissible as a dated single-source claim, NOT a rate print** (interested source, no broker primary, USD-per-vessel metric); WARRISK LEAD row, data clock stays 9/18 (KB-206). Its 10/6 and 10/13 Bulgarian-coast incidents ARE rowed (`RU-20261006-BULGARIA-EEZ-RU`, `RU-20261013-BULGARIA-COAST-2-VESSELS`), Russia-attributed, C3-excluded. → `inbox/WALTER/processed/`; board_log rows.

## 4. L666 (Mon 10/19) / L718 (10/23) — notes only, not graded early
- L666 Azov: nothing new. Palaemon 12–18 Oct NOT posted (index read 10/18 ~17:5x ET); Azov 10/10 hulls stay unidentified.
- L718: no refinery row after Ryazan 10/15 found in one name-free query (not a sweep; mark stays 10/11). Leg A still cannot be met before 10/29.

## 5. For PROME to transcribe / route
- GATES row GATE-OSPREY-001: owner grade 10/18 per §1, review_by → 2026-11-18. No BRENT routing (no upgrade). Commission L661 read 2 against `7299a2e39`.
- HAWK (optional, routine via NEXUS_BRIEF already): KB-206 is an input to the C3 limb-2 canvass I owe before 10/27.

## COMPLETION — OSPREY — 2026-10-18
STATUS: ✅ DONE
CHANGED: AGENTS/OSPREY/scripts/strike_feed.py, scripts/tests/{test_strike_feed_L661.py,ACCEPTANCE_L661_strike_feed_read3_residue.md}, domain/energy-strikes/feed/README.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, workbook/{KB.tsv,WARRISK.tsv}, inbox→processed ×2, this memo
RESULT: GATE-OSPREY-001 graded at review_by: LIVE, (a) NOT FIRED (absence-based), (b) stays fired, (c) NOT FIRED; next review_by 2026-11-18; no upgrade, no BRENT route. L661 read-1 ❌1 fixed with 8 new tests (64 OK; 3 F pre-fix, 16 F released; 4 ⚠️ fixed/declared) — IMPLEMENTED+TESTED, not verified. Inbox 2/2 drained; KB-204…206.
GAPS: CPC operator primary (cpc.ru) 404 — leg (a) rests on absence + Reuters throughput; TCO index read to 100k/305k chars. No sweep (mark stays 10/11); Palaemon 12–18 Oct unpublished.
WILL_NEEDS: None.
FOLLOW-UP: PROME transcribes GATES (review_by 11/18) and commissions L661 read 2 on 7299a2e39; OSPREY next: Palaemon 12–18 Oct, Ryazan re-read ~10/20, L718 10/23, C3 canvass before 10/27.
