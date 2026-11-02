# OSPREY → PROME: D:L814 graded NOT MET; leg B UNREACHABLE (blackout day 60); refinery strikes resumed 10/30–11/1

**Written:** 2026-11-02 (Mon) ~08:57 ET (from `date`) · osprey-1102 · PROME prome-40 Tier-1 WQ-184 wake under C6 · $0, no trade proposal, no mark/band/threshold moved.

## Boot (pages read with `PROME/tools/boot_read.py`, each to `eof: true`)
| File | Pages |
|---|---|
| root `CLAUDE.md` | 5 |
| `AGENTS.md` | 1 |
| `USER.md` | 2 |
| `AGENTS/OSPREY/CLAUDE.md` | 9 |
No `git pull`: other desks' tracked files are dirty (FALCON state JSONs, HENRY PUBLISHED.tsv, PROME/state), so Git refuses a rebase pull. I fetched and worked on the checkout.

## D:L814 — C1 5→4 downgrade test: **NOT MET**
| Leg | Result | Anchor / prints |
|---|---|---|
| A (14 clear days from the newest refinery-class row) | **NOT MET, RESET** | Newest row **`RU-20261101-KSTOVO-NORSI` (11/1) ⇒ 1/14, earliest 11/15**. Also new: `RU-20261031-UFA-NOVOIL` (10/31, C3), `RU-20261030-NOVOKUIBYSHEVSK` (10/30, B2, Deputy PM Novak via TASS: "three refineries and one gas-chemical complex" attacked). NOT MET under every anchor (most conservative: 10/30 ⇒ 3/14, earliest 11/13). Ryazan 10/15 is superseded. |
| B (independent capacity-offline aggregate <40% on two prints) | **NOT MET → UNREACHABLE** | Prints found: S&P/CERA **9/3** (~half offline) and IIR **9/8** (3.805 M bpd), both ≥40%. None since (SEARCH-NOT-FOUND 11/2). Rejected look-alikes: bne IntelliNews tracker ~45% (not an admitted instrument, 403), UNITED24 "10% in 72h" (capacity targeted), Ukraine MoD 51% (belligerent). |

**⚠️ BLACKOUT FLAG (the §1b clause, fired today):** 11/2 is day 60/60 from S&P/CERA 9/3 with no independent aggregate ⇒ **the C1 5→4 test is UNREACHABLE on leg B.** C1 stays **5** because leg A fails on its own (fresh strikes), so this is not a 5 held on a dead instrument; but leg B cannot pass on any instrument the letter admits. (11/7 if IIR's 9/8 print counts; I chose the earlier date at registration.)
- **What the letter does not say:** what follows the flag. My recommendation is not a self-ruling. Register a successor re-grade at **11/15** (leg A earliest from Kstovo), with leg B carried UNREACHABLE. Whether C1's exit from 5 should take a substitute instrument (§1b's 4→3 limb already uses runs: EA Analytics/Kpler ≥4.5 M bpd for two months) is a **letter change, so it is Will's** if you choose to raise it. There is no ask to Will from this desk today.
- Record: `AGENTS/OSPREY/domain/energy-strikes/L814_GRADE_2026-11-02.md` · KB-OSPREY-244 (grade), -245/-246 (strikes), -248 (aggregate search).
- Caveats travel: CAPACITY, not barrels. Militarnyi says all CDUs are down at Novokuibyshevsk; that rests on belligerent-side OSINT and conflicts with Novak's "minor damage at one plant". No General Staff claim was found for any of the three. Kstovo's identity rests on OSINT plus a governor statement naming no plant. The Moscow read and the decree-starvation risk (KB-222) still stand.

## Other dated items
- **11/1 diesel ban: EXTENDED to 2027-01-31** (decree №1436, YURI's primary via WALTER SIG-W-20261031-001) ⇒ the C1 companion tell does not start (KB-247).
- **OSP-07** (≥1 refinery strike 10/30–11/15): the 10/30 event is in its window. It is not graded early; the row grades on or after 11/18.

## Inbox drain — 6/6, every sender, logged per BOARD_CONSUMPTION_SPEC §5 (`board_log.tsv` +6, files `git mv` → `processed/`)
| Item | Disposition |
|---|---|
| SIG-W-20261029-052 (diesel to year-end, rations eased) | acted → KB-247 (year-end superseded by №1436) |
| SIG-W-20261030-008 (Novokuibyshevsk claim-only) | acted → rowed, KB-245 |
| SIG-W-20261031-001 (decree №1436) | acted → KB-247 |
| SIG-W-20261031-003 (Novokuibyshevsk corroborated) | acted → rowed + Ufa/Kstovo/Samara, KB-245/246 |
| SIG-W-20261031-004 (Novak 2.15 Mt plan) | noted → KB-247 context |
| 2026-10-31_from-WALTER_aleshki (Oleshky humanitarian halt) | info-only, no channel effect |

## Skipped / not done (named)
- `swept-complete` mark **not advanced** (stays 10/25): Palaemon 26 Oct–1 Nov was not yet on its index at 11/2 ~08:5x ET, so vessel coverage after 10/25 is news-only.
- `strike_feed.py` 11/2 ran (43 rows, NONE 41, NOT_READ 0); its NONE rows were **not** individually dispositioned in the git-ignored candidate file (boot step 5b-iv). The refinery and pipeline rows are rowed or named in KB-246.
- Not run: full closeout steps 10–12 beyond KB/STRIKES (no VX/FLOW change; no ANALYSIS regeneration); +5d re-reads (due ~11/6); FIRMS (no tool on this host).

COMPLETION
STATUS: DONE (D:L814 graded NOT MET; blackout flag fired)
CHANGED: STRIKES.tsv +4 rows · KB-OSPREY-244…248 · L814_GRADE_2026-11-02.md · STATUS/SCRATCH/NEXUS_BRIEF · board_log +6, inbox 6→0
RESULT: C1 stays 5. Leg A reset (anchor Kstovo 11/1, 1/14, earliest 11/15). Leg B UNREACHABLE: no independent aggregate since S&P/CERA 9/3 and IIR 9/8 (day 60)
GAPS: mark stays 10/25 (Palaemon 26 Oct–1 Nov unpublished) · no General Staff claim for the 3 refineries · feed NONE rows not individually dispositioned
WILL_NEEDS: none today; whether C1's exit from 5 gets a substitute instrument is Will's only if PROME raises it
FOLLOW-UP: register an L814 successor at 11/15 (leg A) · +5d re-reads ~11/6 · OSP-07 grade ≥11/18
