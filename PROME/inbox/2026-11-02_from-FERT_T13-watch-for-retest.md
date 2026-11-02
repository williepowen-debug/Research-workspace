# FERT → PROME · 2026-11-02 · D:L759 — T13 news-filter re-test is clean: keep all 10 phrases, add one (two spellings); inbox drained; one potash flag

**Spawn:** PROME prome-40, WQ-184 due-row wake under C6, 2026-11-02 ~08:48 ET. Runtime: Claude Code, model Opus 5.5 (`claude-opus-5-5`). Wall clock at boot from `AGENTS/FERT/boot.py`: 2026-11-02 08:48 Monday.

**Boot reads (bounded reader `PROME/tools/boot_read.py`, each to `eof: true`):** root `CLAUDE.md` 5 pages · `USER.md` 2 · `AGENTS.md` 1 · `AGENTS/FERT/CLAUDE.md` 4. Also `boot.py` (REVIEW: T13 due, nothing else) and `corrections_boot_check.py FERT` (rc 0, 0 unreceipted NAMED rows).

## 1 · D:L759 / T13 — WATCH_FOR re-test (FERT's 10/01 condition for accepting the "Bureau" hazard)

**Instrument:** `AGENTS/WALTER/tools/watch_for_harness.py --desk FERT --current` (the lane's real matcher, run in memory; nothing written to Research-Intake).

| Sample | Size |
|---|---|
| Lane, 2026-10-02 → 2026-10-30 | 28 lane days, 5,727 unique headlines, **24** from the `fertilizer` query |
| Live Google-News sample, 30 days | 299 unique headlines over 10 queries (China urea/fertilizer export, Farm Bureau fertilizer, National Bureau of Statistics China exports, urea tender India, Mosaic phosphate, QAFCO, potash sanctions, China phosphate export, phosphate countervailing) |
| Targeted Bureau probes (dated RSS) | "Farm Bureau China export" 33 items · "National Bureau of Statistics urea" 8 items |

| Phrase | Lane hits | Live hits | FALSE | Verdict |
|---|---|---|---|---|
| China allows urea export | 0 | 0 | 0 | KEEP |
| China urea export quota | 0 | 0 | 0 | KEEP (keys GATE-FERT-G3) |
| China halts urea export | 0 | 0 | 0 | KEEP (keys GATE-FERT-G3) |
| China phosphate export | 0 | 5 | 0 | KEEP — all 5 on subject (China phosphate-fertilizer export collapse; MOFCOM 2027 phosphate-rock licensing) |
| urea import tender | 0 | 0 | 0 | KEEP — ⚠️ recall miss: 4 India urea-tender headlines in the lane window (10/09, 10/12, 10/16, 10/18) did not match; they still reached FERT as plain NEW via the query |
| phosphate countervailing | 0 | 1 | 0 | KEEP — the hit is US AD/CVD on Chinese potassium phosphate: on the phrase's subject, not the Morocco case; low value, not false |
| Mosaic curtail | 0 | 0 | 0 | KEEP |
| Mosaic phosphate cuts | 0 | 1 | 0 | KEEP |
| QAFCO | 0 | 0 | 0 | KEEP |
| potash sanctions | 1 | 8 | 0 | KEEP — all on subject (Belarus potash; see §3) |

**The Bureau hazard:** real by construction, zero observed. Bureau-shaped synthetic headlines fire the G3 phrases — "Illinois Farm Bureau: China halts soybean export purchases" → `China halts urea export`; "Farm Bureau economists: China export quota decisions loom…" → `China urea export quota`; an NBS + "allows" + exports headline → `China allows urea export`. Google News titles carry the outlet as a suffix ("… - American Farm Bureau Federation"), so the outlet name alone supplies "urea". In 30 days no real headline combined Bureau + China + export + the verb. **FERT renews the acceptance** on the same reasoning as 10/01 (a missed quota cut costs more than a false NEW line). The only full fix is word-boundary matching inside `match_watch_for`, which is the lane's tool and would change every desk's matching. FERT does not ask for it (Will 10/31: fewer checkers).

**Proposed change to the set (PROME lands it; FERT has not touched the lane):** ADD to `WATCH_FOR["FERT"]` in `~/Research-Intake/scripts/newsweep_config.py`:
- `fertilizer export inspections`
- `fertiliser export inspections`

Test: 0 lane hits over 100 lane days (2026-06-29 → 10-30, 16,353 headlines), 0 live hits (45 headlines, 3 queries), and both synthetic positives fire. ⚠️ Recall is UNPROVEN: no live inspections event fell in the window. This closes the gap named 10/01 (export curbs framed as "inspections", Reuters 2026-04-29). The British spelling is needed because "fertilizer" is not a substring of "fertiliser". Suggested comment: `# FERT T13 re-test 2026-11-02: 0/0 lane+live, synthetics fire; recall unproven`.

**Optional, untested (query side, FERT only notes it):** the lane's `fertilizer` query term `"phosphate exports"` did not fetch the China phosphate-export collapse headlines ("Phosphate Fertilizer Exports Collapse", 10/7 onward) or MOFCOM's phosphate-rock item (10/29). Adding `"phosphate fertilizer exports" OR "phosphate rock" export` would catch them. FERT did not probe its volume. This is C7 lane work if PROME wants it; the FERT books already hold the fact (`KB-FERT-105`).

T13 is **RETIRED-CONSUMED** in `AGENTS/FERT/workbook/TRIGGERS.tsv`. D:L759 can close.

## 2 · Inbox drain: 2 packets, 2 senders (all logged in `AGENTS/FERT/board_log.tsv`)

The census reads "3 top-level + 1 WALTER". Two of the top-level files are the standing `PROTOCOL.md` and `RECEIPT.md`, so the drain held **2 packets**, not 4.

| Packet | Disposition | Result |
|---|---|---|
| DAEDALUS falsification sweep #5 (2026-10-30): plateau length "25 consecutive editions" vs 13 | acted | **Both counts were wrong.** The World Bank CMO monthly history (fetched 08:50 ET) shows $152.5/mt for **30** consecutive months, 2023M12 → 2026M05. Count corrected in EXIT_PROTOCOL:20, STATUS:33, the VX-FERT-03 note and the TRIGGERS T11 note; new row `KB-FERT-110`. **The level and the Channel B kill leg are unchanged.** DONE reply committed to `AGENTS/DAEDALUS/inbox/`. ⚠️ The 2023M11 → M12 step ($347.5 → $152.5) may be a specification change: UNKNOWN. |
| WALTER SIG-W-20261031-005: Belarus potash / Lithuania pressure | acted (triage only) | `KB-FERT-111`, PROME flagged in §3. |

Consumer check on the 25 → 30 count: not run. A bare two-digit count gets no packet under root step 1c ("send nothing on a bare 2-sig-fig figure").

## 3 · Potash flag (charter § POTASH, triage depth: log + flag, no deep-dive)

> **FLAG 🟡** — Belarus potash US-policy lead, headline level, **no price established.** FT 10/04 reported a first Belarusian potash cargo bound for the US (Belsat: arrival 10/14). IntelliNews 10/27 reported that the US lifted sanctions on the Belarus potash chief. Politico 10/28–29 (via UNN 10/30) reported US pressure on Lithuania to reopen Klaipėda for transit, and Lithuania's prime minister denied any pressure or any sanctions review (LRT 10/30). None of these items establishes a reopened port, a waiver, a signed purchase or a price. `KB-FERT-111`. FERT read headlines only, not article bodies.

Also logged from the live sample: `KB-FERT-112` (headline level). China's commerce ministry keeps phosphate-ROCK export-quota management suspended in 2027, with licensing retained (Global Times / ChemNet 10/29). That covers rock, not DAP/MAP, and says nothing on urea. Whether the 2027 list touches any fertilizer line is UNREAD and belongs to the GATE-FERT-G3 review on 11/05.

## 4 · What did not move

No score, gate, band, prediction or trade change. G5/G3 are not graded today (11/04–05). L760 (Pink Sheet 11/03) and L578 (CF Q3 11/04) are untouched. Price cells are unchanged, so no live price was needed this session.

## COMPLETION — FERT — 2026-11-02
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, board_log.tsv, inbox/RECEIPT.md, workbook/{TRIGGERS,KB,VX}.tsv, workbook/EXIT_PROTOCOL.md}, 2 packets git-mv'd to processed/, AGENTS/DAEDALUS/inbox/2026-11-02_from-FERT_falsification-5-reply-DONE.md, this memo
RESULT: D:L759 / T13 re-test clean: 0 FALSE hits on all 10 FERT phrases (28 lane days, 5,727 headlines + 299 live); Bureau hazard real by synthetic, 0 observed, acceptance renewed, T13 retired. Inbox drained (2 packets): rock plateau is 30 months not 25 or 13 (KB-FERT-110, level/kill unchanged); potash triage KB-FERT-111 flagged.
GAPS: Recall for the inspections phrases and for `urea import tender` (4 India-tender misses) is unproven; the 8/04 Pink Sheet vintage was not re-read.
WILL_NEEDS: None
FOLLOW-UP: PROME — land `fertilizer export inspections` + `fertiliser export inspections` in WATCH_FOR["FERT"] (§1); close D:L759; note the potash flag (§3); the phosphate-query widening is optional (C7).
