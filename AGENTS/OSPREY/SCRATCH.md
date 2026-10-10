# OSPREY SCRATCH — 2026-10-10 (Sat) · osprey-1010 · PARTIAL (closed at PROME's WQ-249 ask ~11:47 ET)

## 10/10 — WHAT LANDED / WHAT IS OWED
- DONE: items 1-4 of the spawn read and recorded (STATUS ACTIVE 2026-10-10; KB-183…191; STRIKES +4; inbox 2/2 drained). Marks unchanged: 5 / ⚪1 KILLED / 3.
- ⛔ **OPEN C2 LEAD — Azov port, two vessels 10/10, types unknown (KB-184).** If a tanker at an oil berth: C2 re-arms at 5 as of 10/10. First check: Palaemon 5-11 Oct; portnews.ru; Slyusar's later posts.
- NOT DONE (next session): packets to BRENT / YURI / DEWEY (WALTER's -003 card already routed the facts; my adds = KB-187 price-cap/mainstream-tonnage INFERENCE → HAWK, KB-190 ban-lift confound → YURI, KB-183/189 answers to DEWEY claims 3-4) · NEXUS_BRIEF refresh · closeout claim/orphan checks · the 10/7 STATUS rotation if the next block breaks the cap (31,701 B now).
- 10/15 L544: pre-fetch in KB-191 — do NOT grade early.

# (prior) OSPREY SCRATCH — 2026-10-09 (Fri)

## CURRENT MARKS
C1 / C2 / C3 = **5 / ⚪1 KILLED (dormant-armed; last live mark 5) / 3**. Band **~30%, 25–35% EST**, unchanged. Prices come from BRENT. This was a PROME Tier-1 due-row wake (DOCKET L623, prome-75). Full state: STATUS; verdict record: `domain/energy-strikes/C2_KILL_EVAL_2026-10-09.md`.

## 10/9 PM: L624 FIX PASS 2 (PROME spawn prome-75, ~12:55–13:05 ET; this task only)
- READ 2 found STILL UNRESOLVED (1 ❌8). Acceptance was committed first (`88d715d03`), then the fix (`4ea2b4539`). Any link that could be newer than the followed bulletin is now named and fails closed (`BULLETIN_NEWEST_UNSURE`).
- Tests: 32 OK on the fixed code, 14 F on `04d8f06be`. The residue block is in `scripts/tests/ACCEPTANCE_L624_strike_feed_follow_newest.md`.
- ⛔ **Two-correction stop TRIPPED on `strike_feed.py`.** No third pass of my own; any change goes through PROME's READ 3. The feed is **WITHHELD** until READ 3 is clean, and the C2 feed leg stays UNVERIFIED.
- BRENT 10/9: 3.76 is not confirmed at text, and there is a 2025 3.74 date trap. It stays B3; no cell moved (KB-182, C2 record §2 receipt).
- Inbox: 3 packets consumed (PROME read-1, PROME read-2, BRENT) and moved to `processed/`.

## CHANGES SINCE LAST SESSION (10/8)
- ⚪ **C2 KILLED on its letter.** Limb 1 is 30/30 (Novorossiysk 9/9). Limb 2: the Bloomberg 4-wk was ≥ 3.5 throughout (3.76 to 10/4), and there is no shut-in signal (the 9/20 halt was offtake deterrence and reversed).
- 🔄 **C3: AFRAMAX RIO QUALIFIES.** Zelensky's 10/7 "response in the Black Sea" post carries the tanker's video. **3/21; the earliest kill is 10/27.**
- Volgograd halt VERIFIED (Reuters factbox, 10/2). Omsk 10/8. **Ukhta 10/9 = C1 anchor (0/30).** Volodarskaya products LPDS 10/6.
- Swept-complete mark **9/20 → 10/07 (BOUNDED)**.

## WHAT I DID
- Ran `strike_feed.py` (33 rows, 26 NONE, all dispositioned in the feed file) and a mechanism-level sweep (EN+RU, name-free plus nine ports, Reuters factbox).
- STRIKES: +6 rows, 2 updated in place. KB-177…181. VX refreshed (UKR-01, SHADOW-01).
- **Feed residue decision:** `MATCHES_2026-09-15/16/29.tsv` are the designed audit trail, not residue, so they are **COMMITTED**, not trashed. They are 6/6 precise (KB-181).
- Inbox drained 7/7 (DAEDALUS items 1 and 2 DONE; WALTER R3 adopt/decline sent to PROME; WQ-399 receipt line fixed in CLAUDE.md).
- Packets: HAWK (C3 limb-2 grade ask) and BRENT (confirm the 3.76 print). Memo to PROME.

## ⛔ THE THING NEXT SESSION MUST NOT FORGET
**The C2 kill is void-on-backfill.** If any in-geography crude-terminal, pipeline or oil-port strike dated **after 9/9** surfaces, C2 re-arms at 5 as of that date. First checks:
- the **Palaemon 5–11 Oct** bulletin (unpublished on 10/9);
- a **port-level Novorossiysk** figure for late September and October, since the restart is only inferred.

## NEXT SESSION
1. **10/8–10/15, OSP-06:** Bloomberg 4-wk to 10/11 (~10/13). 3.76 to 10/4 does not fail it; ≥ 3.9 would.
2. **10/15, L544 C1 5→4 first evaluation:** the 14-day leg is unmet (Ukhta 10/9). Check the aggregate leg, the blackout count from 9/3, and the **data-decree goods list (SEARCH-NOT-FOUND 10/9)**.
3. **10/27:** the earliest C3 limb-1 kill date (RIO anchor). HAWK owes the limb-2 grade.
4. **Unidentified:** Zelensky's 10/6–7 "oil facilities in Samara, Astrakhan, Perm" (inland or Caspian, so they cannot move C2).
5. **Carried:** OWED-30 write-up · 42/50 basis pair · 43 Moscow barrels · 44 Ust-Luga condensate · 45 FEED_CANDIDATES dispositions still git-ignored · 48 AWRP · 51 midstream backfill (now live in October: Samara, Volodarskaya).

## PREDICTIONS / DECISIONS
OSP-06 is OPEN at 45%, deadline 10/15. **No Will-gated decision is open.** The C2 kill is a letter-fired channel kill (§1), executed by the owner: no threshold moved and no capital path.

## MAIL STATE
- Inbox 7/7 consumed; the re-census reads 0 / 0.
- Sent 10/9: HAWK, BRENT, and the PROME memo `PROME/inbox/2026-10-09_from-OSPREY_c2-kill-eval-c3-rio-attribution.md`.

## PENDING PUSH / GIT
Committed path-scoped. Push via safe-push; the receipt is in the PROME memo or the SendMessage.
