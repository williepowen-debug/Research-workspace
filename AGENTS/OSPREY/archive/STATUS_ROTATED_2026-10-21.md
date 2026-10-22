# OSPREY STATUS — ROTATED 2026-10-21 (verbatim, READ_CAP rotation)

*Rotated from `STATUS.md` on 2026-10-21 by osprey-1021 (owner boot). Block below is byte-identical to the live file at rotation; crc32 of the block = 2002224843. Not boot-read.*

## ACTIVE — 2026-10-16 (L661 strike_feed residue · inbox 5/5 · no mark, band or threshold moved)
1. **Ryazan refinery hit overnight 10/14–15 — the first refinery strike after the pause; NEW C1 anchor.** (KB-200, `RU-20261015-RYAZAN`)
   - Governor Malkov (via Moscow Times 10/15): a major Ukrainian drone attack set the refinery on fire; *"The material damage is now being assessed."* Halt not established; +5d re-read owed.
   - **Read at the ledger:** C1 kill clock **1/30**. The §1b 14-day leg cannot be met before **10/29** (was 10/23). **L718 (10/23) is not graded early**; its own letter says any refinery row resets leg A.
   - ⚠️ **The 10/15 session missed it** ("no post-resumption strike found to ~08:30 ET"), although Reuters carried it from ~03:47 ET. The WALTER handoff caught it. 10/12–10/15 was swept, not certified, so no certification is false; the miss is real.
2. **The 10/11 "energy ceasefire" is TERMINATED in practice and was never in force** (KB-201). Zelensky to the FT 10/15: *"The block is out. We're done."* Peskov 10/15: Kyiv never complied. §2: no ceasefire in force. The Energy Intelligence "diesel ban lifted" headline is superseded at primary (partial permission, KB-198).
3. **Surgut condensate plant 10/16, graded:** event confirmed (governor: fire at an industrial facility after drones); identity probable (OSINT and residents name the Surgut ZSK, Gazprom); attribution inferred; damage unknown. **Not refinery-class** (OWED-46 open). (KB-202)
4. **Sberbank Balakovo data centre 10/14** = a non-energy target class, out of every count. It is the data-centre element of the Saratov 10/14 row; the "energy facility" there is still unidentified. (KB-203)
5. **`strike_feed.py` — DOCKET L661 (READ-3 residue, new episode): IMPLEMENTED and TESTED, NOT independently verified.** Four new doubt tells: out-of-date-order links below the followed bulletin; a featured duplicate keeps its list position; a title/slug disagreement over 180 days; the two-year window form parses. The single-date note no longer claims a window END. 56 tests OK; 11 fail on the released code; 15 mutants caught. Three cases are still silent (declared in the acceptance file and the feed README). Live index 10/16: newest 5–11 Oct, 0 doubts. Acceptance `e5fe3a692`, fix `48342e63a`. PROME commissions the read.
6. **GATE-OSPREY-001 review was due Sun 10/18 — ✅ GRADED 10/18 (ACTIVE 2026-10-18 item 1).** Evidence held (10/15): no CPC halt reported; the RIO spill reached the CPC SPM area (a spill, not structural damage); no Tengiz force majeure seen. That is not a dated canvass, so it is not a grade.
7. **Inbox 5/5 drained** (census 0/0). `strike_feed.py` NOT run live (a bounded spawn, not a sweep); mark stays 10/11.



---

*Second rotation 2026-10-21 ~21:4x ET (osprey-1021, STATUS at 96% of the read cap): the 10/18 block below, byte-identical; crc32 = 3199308906.*

## ACTIVE — 2026-10-18 (GATE-OSPREY-001 graded · L661 read-1 fix · inbox 2/2 · no mark, band or threshold moved)
1. **GATE-OSPREY-001 GRADED at its review_by: LIVE, no leg newly fired, NO Channel-2 upgrade, no BRENT route.** (KB-204/205)
   - **(a) CPC SPM structural damage confirmed by assessment: NOT FIRED.** Window 9/18→10/18. No SPM-damage report located (EN+RU). Reuters 10/13 (via Baird Maritime): CPC throughput 6.0 Mt (1.59 M bpd) in September vs 6.28 Mt in August, the drop put on Karachaganak maintenance; no terminal or SPM damage reported. ⚠️ **Absence-based this time** — unlike 9/18 no assessment ran (none was called for); cpc.ru press pages 404, operator primary NOT read.
   - **(b) FIRED 7/24, stays fired.**
   - **(c) Tengiz force majeure: NOT FIRED.** TCO's own news index (10 items 8/19→10/16) mentions no FM, halt or suspension; Reuters 10/13 mentions none. SEARCH-NOT-FOUND, not VERIFIED-absent (index read to 100k of 305k chars).
   - **Next review_by 2026-11-18** (30 days), or at once on any CPC terminal strike or SPM incident. PROME transcribes; I do not edit GATES.
2. **`strike_feed.py` L661 read-1 ❌1 FIXED — IMPLEMENTED + TESTED, NOT independently verified.** Leftmost window wins: a later two-year date pair in the anchor text can no longer make a stale bulletin read fresh (CX-A now `BULLETIN_STALE`, NOT_READ 1). Acceptance first `31053d1f6`, fix `7299a2e39`. 64 tests OK (8 new); 3 F on the pre-fix code, 16 F on the released code; read-1 mutants MR2/MR4/MR5/MR7 caught. ⚠️1 declared (pinned), ⚠️2 pinned, ⚠️3 residue list now non-exhaustive (+CX-D2, CX-E), ⚠️4 "~7 days". **Unattended feed run UNAVAILABLE on either version until read 2** (PROME 10/16 as corrected); PROME commissions read 2.
3. **War-risk: Lukoil-Bulgaria executive says Black Sea tanker cover rose ~$200K → ~$2.5M per vessel** (BNT, reported ~10/13). **Admissible as a dated claim, NOT a rate print** — one interested source, no broker primary, a different metric (USD per vessel). WARRISK LEAD row; data clock stays 9/18. Input to the C3 limb-2 canvass before 10/27 (HAWK grades). The 10/6 and 10/13 Bulgarian-coast incidents it cites are rowed and Russia-attributed (C3-excluded). (KB-206)
4. **L666 / L718 — nothing new; not graded early.** Palaemon 12–18 Oct still NOT posted (index read 10/18 ~17:5x ET); Azov 10/10 hulls stay unidentified. One name-free refinery query found no refinery row after Ryazan 10/15 (not a sweep; mark stays 10/11). L718 (10/23): leg A still cannot be met before 10/29.
5. **Inbox 2/2 drained** (census 0/0): PROME L661 packet + SIG-W-20261016-032.

