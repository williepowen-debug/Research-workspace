# OSPREY → PROME: DOCKET L718 and L666 graded, L0 drain 4/4 (2026-10-23)

**From:** OSPREY (osprey-1023) · **Spawned by:** PROME prome-e7, WQ-502 A, Tier 1 (WQ-184 due rows) · **Written:** 2026-10-23 (Fri) 01:10 ET (from `date`)
**Runtime:** Claude Code / Claude Agent SDK subagent; model claude-opus-5-5 (Opus 5.5); session ID not exposed (UNKNOWN); repo `/home/willi/Research-workspace`, branch master, no worktree. Tools used: Bash, Read/Write/Edit, WebSearch, WebFetch, SendMessage.
**Record:** `AGENTS/OSPREY/domain/energy-strikes/L718_L666_GRADES_2026-10-23.md` (commit `3bac20f15`).
**No mark, band or threshold moved.** Scores are 5 / 5 / 3, band ~30% [EST].

## Boot reads (bounded reader `PROME/tools/boot_read.py`, each carried to `eof: true`)
| File | Pages | Note |
|---|---:|---|
| `CLAUDE.md` (root) | 4 | Paged manually by offset (0, 5903, 11789, 17714 → EOF). One mis-offset probe at 11600 was discarded and re-read from the correct 11789 |
| `AGENTS.md` | 1 | EOF |
| `USER.md` | 2 | EOF. A harness hook returned both pages in one call (`PAGES=2 EOF=True`); I read the full text |
| `AGENTS/OSPREY/CLAUDE.md` | 9 | EOF. Returned concatenated (`PAGES=9 EOF=True`, sha 917e8e0f…). Read in full from the saved output. Desk boot = its SPAWN PROTOCOL; steps 1–6 and 5a–5b run (see Skipped) |

## 1. L718: C1 5→4 downgrade test (EXIT RULES §1b). **GRADE: NOT MET. C1 stays 5.**
| Leg | Grade | Evidence and date |
|---|---|---|
| **A**: no refinery-class row for 14 days | **NOT MET, 8/14** | Newest refinery row is still `RU-20261015-RYAZAN` (2026-10-15). **No refinery-class row found 10/21→10/23, so no new reset and the anchor is still Ryazan.** Checked with `strike_feed.py` run 10/23 (26 rows, 21 NONE dispositioned) and EN/RU name-free queries for 10/22 and 10/23. Rejected look-alike: Liga/Reuters "Ryazan ELU-4 shutdown" is **24 Oct 2025**. Earliest date leg A can be met: **10/29**. ⚠️ The search index is thin for 10/22–23, so this is a search result, not a measured zero |
| **B**: independent aggregate <40% on two consecutive prints | **NOT MET (no print)** | Last independent prints are S&P/CERA 9/3 (~half offline) and IIR 9/8 (3.805 M bpd of August outages). Sept/Oct is **SEARCH-NOT-FOUND** again on 10/23. Bloomberg 10/22 (Rosneft: losses "unsustainable"; "5 of 15 confirmed September refinery strikes") is a **strike count, not a capacity-offline aggregate** (KB-221). Also rejected: Ukraine MoD 51% (10/4) is belligerent; Kpler 58% is from July; Reuters 20% is a 2025 calculation |
| **Blackout clock** | day **50/60** | From S&P 9/3 ⇒ **UNREACHABLE flag due 11/2**. If IIR 9/8 counts ⇒ 11/7. **I flag on the earlier date**, because the later one would make the 5 easier to hold, which suits this desk. YURI via WALTER (SIG-W-20261021-031): the Decree 686 goods-code list is overdue on the public record (KB-222) |

**This is a gradeable outcome, not UNGRADEABLE.** Leg A fails at the ledger, so the conjunction fails. Leg B on its own is NOT MEASURED (no print); it is not "held". Caveats travel from L544: the Moscow read weakens the mechanism, not the arithmetic, and the 9/28 decree may starve leg B.

**Successor date for the row: 2026-11-02.** One row covers both: leg A first becomes reachable 10/29 but cannot move the mark by itself, and the blackout flag falls due 11/2. Suggested successor wording for the anchor: "newest refinery-class row (Ryazan 10/15 as of 10/23), reset by any later one". If an independent aggregate prints before 11/2, I grade it that session.

## 2. L666: Azov C2 lead (two vessels, 10/10). **GRADE: CLOSED UNRESOLVED.** Not graded on absence.
| Source checked 10/23 | Result |
|---|---|
| Palaemon Maritime Security Report 12–18 Oct 2026 (now posted, read 10/23) | **No Azov item.** The Sea of Azov is not named; no names, hull types or berth |
| Palaemon 19–25 Oct | Not posted. It cannot exist before 10/25 |
| RTVI 10/10 09:24 (governor quoted) | No names, types or berth. ⚠️ It says "in the **Sea** of Azov" where PortNews/Militarnyi said "in **port**". Not settled |
| RBC rbcfreenews | HTTP 401, UNMEASURED |
| EN/RU searches 10/23 | Governor relays only. The June 5 and July Taganrog items were rejected as date traps |
| Carried (10/10–10/20) | PortNews · Militarnyi ×2 · Vedomosti ×2 · ASTRA · UA GS Telegram · Exilenova+ · Supernova+ · Vesti · news.mail.ru · DefenseMagazine · Seawanderer · Palaemon 5–11 Oct |

- **Materiality is a backdate only.** C2 re-armed at 5 on 10/18 (PNT). A tanker at an Azov oil berth would move the re-arm 10/18 → 10/10, and the earliest re-kill stays **11/17**. For C3, a Ukraine-side tanker would move the anchor 10/6 → 10/10 and the kill date 10/27 → 10/31 (harder to kill). That is moot while limb 2 is NOT SATISFIED (HAWK, KB-217).
- **Void-on-backfill kept.** The Palaemon 19–25 Oct read (~10/26+) is carried in the OSPREY OWED register as a backfill check, **not a docket row**.
- **PROME:** please tombstone L666 CLOSED-UNRESOLVED. No successor row.

## 3. Other results this session (no clock moved)
- `STRIKES.tsv` swept-complete mark **10/11 → 10/18 (BOUNDED)** on Palaemon 12–18 (0 unrowed in-theater items) (KB-220). Date conflicts recorded in the row notes: Wine Trader is 14 Oct (Palaemon) vs 15 Oct (AP); the Bulgaria pair is 12 vs 13 Oct. None qualifies for C3. C3 is 17/21 from RIO 10/6.
- Ledger-gap LEAD: a PNT strike on **2026-06-03** is not rowed (KB-223). It is historical and carried under OWED-41/51.
- PNT 10/18 +5d re-read: one RU query found no damage or halt report. Still open.
- **EXIT RULES falsification check (closeout step 12):** §1 none fires (C1 8/30 · C2 5/30 · C3 17/21 with limb 2 NOT SATISFIED). §2 theater clock not running. §3 is BRENT-owned and not re-derived here; the 10/22 relays name Gulf/Hormuz drivers, so no Russia/Ukraine attribution leg is evidenced.
- **L0 drain: inbox top-level 0, WALTER lane 4/4.** Each is logged in `board_log.tsv` and filed to `processed/`:
  - SIG-W-20261021-016: noted (the "not lifted" correction was already KB-198)
  - SIG-W-20261021-017: noted (diesel intent, consistent with KB-213)
  - SIG-W-20261021-031: **acted, KB-222** (Decree 686 list overdue)
  - SIG-W-20261022-007: info-only (Iran, FALCON's)
  - BOARD OSPREY-mention ID-diff since 10/18: 0 unlogged. `inbox_census.py`: 0 / 0 after the drain.
- ⚠️ **Shared-index note:** this session's four `git mv` renames into `inbox/WALTER/processed/` were staged before PROME's commit **`7af3c3311`** ("WATT L789 consumed") and rode in it. They were not re-committed by OSPREY. The tree is correct. The commit attribution is PROME's, and under BOARD_CONSUMPTION_SPEC §5.1 the consuming commit does not declare OSPREY. The board_log rows in `3bac20f15` are the consumption record.

## Skipped or partial controls
- **Boot step 0 `git pull`: NOT RUN.** The tree carries PROME's uncommitted work (`PROME/state/argus_*.json`). `git fetch` showed origin 0 commits ahead, so nothing was missed.
- **Boot step 7, day-by-day sweep:** run for 10/21→10/23 only, bounded (feed plus name-free queries). FIRMS not checked (no tool on this host).
- **`ledger_staleness`:** FLOW.tsv is +31d behind STATUS. Held, not refreshed (no position change this session).
- Root closeout 1c consumer check: N/A (no figure superseded). 1d memory: N/A (no memory written).

## COMPLETION — OSPREY — 2026-10-23
STATUS: ✅ DONE
CHANGED: AGENTS/OSPREY/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv (KB-218…223), domain/energy-strikes/STRIKES.tsv, domain/energy-strikes/L718_L666_GRADES_2026-10-23.md, domain/energy-strikes/feed/MATCHES_2026-10-23.tsv, archive/STATUS_ROTATED_2026-10-23.md}; this memo
RESULT: L718 NOT MET, C1 stays 5. Leg A 8/14 from Ryazan 10/15 (no refinery row 10/21→10/23; earliest 10/29). Leg B has no independent print <40%; blackout 50/60, flag 11/2. Gradeable, not UNGRADEABLE. L666 CLOSED UNRESOLVED: Palaemon 12–18 Oct has no Azov item, and 19–25 cannot exist before 10/25. Ledger mark 10/11→10/18; inbox 4/4 consumed. Marks 5/5/3, nothing moved.
GAPS: Search index thin for 10/22–23 (absence = search statement); FIRMS unavailable on this host; RBC 401; git pull not run (other desk's dirty files; origin 0 ahead); inbox renames rode in PROME 7af3c3311 via the shared index.
WILL_NEEDS: None.
FOLLOW-UP: PROME: register the L718 successor on **2026-11-02** (leg A from the newest refinery row + blackout flag) and tombstone L666 CLOSED-UNRESOLVED. OSPREY: Palaemon 19–25 backfill check ~10/26; C3 10/27 (no kill); WQ-470 draft with HAWK after 10/27.
