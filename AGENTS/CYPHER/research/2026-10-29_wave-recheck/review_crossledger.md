# CYPHER consistency review — 2026-10-29 12:14 EDT (read-only)

Commits reviewed: f1d07f46c, cf0d4b315, ca5098e24.
Clean: every TSV row has the same field count as its header; no CRLF; composite 2+3+3+3+3+4+3+1 = 22 raw / 16 adjusted agrees everywhere; FLOW counts 7/7/2/4 = 20 agree; 47 incidents and 35 chokepoints agree; 1 FIRED / 8 NOT-FIRED agrees; no new hand-typed "HH:Mx" placeholders in text written 10/29 (the only hits are older 10/23 text inside rows edited today); no exposed-bank list in NEXUS_BRIEF or the five packets.

## ❌ Wrong or contradictory
1. STATUS.md:81 says "Hanmi has hit twice", but KB.tsv KB-CYP-065 says "Third Hanmi boilerplate hit (10/23 too)". Only two Hanmi reads are on file: the 10/23 read of a 7/23 filing, and the 10/29 filing.
2. VX.tsv:2 says "Last re-pull ATTEMPTED: 2026-10-26", but line 1 says "Last real data refresh: 2026-10-29". The refresh cannot be later than the last attempt.
3. VX.tsv VX-CYP-02 Local_State still reads "Japan precautionary pauses only". The 10/29 note in the same row now rests the score of 3 on a US credit-union pause (CYB-INC-046).
4. INCIDENTS.tsv CYB-INC-007 still says "no malicious exploitation known against PAN products" in its 10/26 note, and its Last_Checked is still 2026-10-26. Palo Alto's 10/29 statement replaced this in CHK-32, KB-CYP-066 and row 1, but this wave-root row was not updated.
5. INCIDENTS.tsv:7 says "boot.py leg 6 checks each key against the CISA KEV catalog". In boot.py the KEV check is leg 7; leg 6 is matrix + map.

## ⚠️ Stale or ambiguous
6. These "Next:" lines are past or wrong:
   - VX.tsv:1 "re-score at the 2026-10-29 DEWEY rerun"
   - KB.tsv:1 "DEWEY REQ-008 rerun 2026-10-29"
   - The rerun is now dated 10/30 (CATALYSTS:3).
7. FLOW.tsv:1 "Last real data refresh: 2026-10-26", but FL-CYP-14 got a new data point today (As_Of 10/29).
8. INCIDENTS.tsv:3 says "rows 015-023 CYPHER's own". The ledger now runs to 047.
9. The Chrome catalyst was retired 10/29, but two rows still treat it as pending:
   - VX-CYP-05 Notes: "Chrome removal remains expected 10/27 … pending"
   - FL-CYP-17: "docket date 10/27 retained"
   - CYB-INC-009 was updated 10/29; these linked rows were not.
10. CHK-33 Last_Checked is 2026-10-26, but its linked CYB-INC-037 (Finzly) was re-checked 10/29.
11. CHK-13 is POSSIBLE with Last_Checked 10/23. The header says POSSIBLE rows are re-checked when the wave changes, and the wave changed today.
12. CATALYSTS:4 (Palo Alto): its threshold "Palo Alto reports exploitation against its products" was met 10/29, but the notes record no 10/29 consumption.
13. CATALYSTS:6 (Kiteworks) says "no exploitation statement as of its 10/22 12:30 PDT update". CHK-15 records a 10/27 update.
14. Two KB rows are superseded but still ACTIVE:
   - KB-CYP-029: ConnectWise restoration "by the end of this weekend"
   - KB-CYP-061: Park24 "no affected population/total cost", superseded by KB-CYP-070
15. Claim-pass scope does not line up:
   - STATUS:92 and NEXUS:58 list "036–040, 043"; CATALYSTS:18 also includes 045.
   - REPORTED rows 042 and 045 were not re-checked 10/29 (Last_Checked 10/26).
   - 042 has no next-check date at all.
16. The claim that the credit union is named in only one place is false. KB-CYP-068 says "Name in INCIDENTS only", and the REGINALD packet says "named only in CYPHER's research files". MSUFCU is also named in:
   - ESCALATION_WATCH rows 3 and 8
   - CATALYSTS:5, which PROME's summons reader takes in
   - This does not breach guardrail 2 (a precautionary pause is not an exposure list), but the containment claim is wrong.
17. Linked VX rows were not re-dated after today's re-check: VX-CYP-01 As_Of 10/26, VX-CYP-03 and VX-CYP-08 As_Of 10/23, and the VX.tsv:7 header still says "COMPOSITE 2026-10-26". Their watch rows (3/4/5, 6/7, 7) were all re-checked 10/29.
18. NEXUS_BRIEF.md:28 "The last of 11 outstanding" reads wrong. It should say 1 of 11 is outstanding (10 confirmed).
