# OSPREY SCRATCH — 2026-10-18 (Sun) · 17:55 ET (from `date`) · osprey-1018 · PROME prome-65 Tier-1 spawn (WQ-184: GATE-OSPREY-001 review_by + DOCKET L661 read-1 fix + L0 inbox drain)

*Rewritten in full (template). The 10/16 SCRATCH is in git history (`git log -1 --format=%h -- AGENTS/OSPREY/SCRATCH.md` before this commit); every carried item is below or in the STATUS OWED register.*

## CURRENT MARKS (one line)
- Refineries/products **5** · crude-export terminals **⚪1 KILLED 10/9 (dormant-armed, last live 5)** · shadow-fleet tankers **3** · band ~30% [EST] · Brent → BRENT (not tracked here).

## CHANGES SINCE LAST SESSION (10/16 17:26 ET → 10/18)
- Reuters 10/13: CPC September throughput 6.0 Mt (1.59 M bpd) vs 6.28 Mt August; Kazakh exports via CPC 5.2 vs 5.7 Mt; Karachaganak maintenance. No SPM damage, no FM.
- Lukoil-Bulgaria executive (BNT, ~10/13): Black Sea tanker war-risk cover ~$200K → ~$2.5M per vessel — single interested source.
- Palaemon 12–18 Oct NOT posted as of 10/18 ~18:00 ET. No refinery row after Ryazan 10/15 found in one query (not a sweep).

## WHAT I DID THIS SESSION
- **GATE-OSPREY-001 graded at review_by:** LIVE; (a) NOT FIRED (absence-based; cpc.ru 404), (b) stays fired, (c) NOT FIRED. Next review_by **2026-11-18**. KB-204/205. No BRENT route (no upgrade).
- **DOCKET L661 read-1 fix:** acceptance AC22–AC26 committed alone (`31053d1f6`), then fix (`7299a2e39`): leftmost window wins (❌1, CX-A), reader pins (CX-F, span 15/14, reversed, 2025–2026), ⚠️1 declared + pinned (CX-E), ⚠️3 residue non-exhaustive (+CX-D2, CX-E), ⚠️4 "~7 days". 64 tests OK. **IMPLEMENTED + TESTED, not verified.** Unattended run UNAVAILABLE until read 2.
- **Inbox 2/2 drained** (board_log + `git mv`; census 0/0). KB-206 + WARRISK LEAD row (data clock NOT advanced; re-pull clock 10/18 = targeted check, not a canvass).
- STATUS ACTIVE 10/18 block + OWED rows + BOTTOM LINE; NEXUS_BRIEF refreshed; memo to PROME.

## NEXT SESSION (dated, future-verifiable)
1. **~10/19+:** read **Palaemon 12–18 Oct** (C3 10/12–10/18; Azov follow-up for L666). An ATTENDED `strike_feed.py` run is allowed; unattended is not until read 2.
2. **Mon 10/19:** DOCKET L666 (Azov C2 lead) — PROME's row; nothing new found 10/18.
3. **~10/20–21:** +5d re-reads — Ryazan 10/15 (units, halt) and Surgut ZSK 10/16.
4. **10/23:** L718 — graded on its date; leg A cannot be met before 10/29.
5. **Before 10/27:** C3 limb-2 dated canvass (10 outlets + TD6) for HAWK, carrying KB-206 as an input. **10/27** earliest C3 limb-1 kill.
6. **11/2:** C1 aggregate blackout 60 days → UNREACHABLE flag if nothing prints (11/7 if IIR 9/8 counts). **11/8:** §5 EXIT RULES re-read. **11/18:** GATE-OSPREY-001 next review.
7. L661 read 2 — PROME commissions; answer any reader ❌ inside the episode budget (3 reads max; after read 2, one remains).

## OPEN THREADS / WATCHES
- 🔴 Refinery tempo after the 10/15 resumption (each refinery row resets the C1 14-day leg).
- 🟠 L661 read 2. Azov 10/10 hulls (void-on-backfill for the C2 kill as of 10/10).
- 🟡 Carried, unchanged: OWED-30 write-up · 42/50 basis pair · 43 Moscow barrels · 44 Ust-Luga condensate · 45 feed dispositions git-ignored · 46 condensate plants and C1 · 48 AWRP · 51 midstream backfill.

## PREDICTIONS DUE / DECISIONS PENDING
- No live prediction (book empty). No Will-gated decision open. None forced by this session's evidence.

## MAIL STATE (one line per surface)
- Inbox: clear (0 top-level). WALTER lane: clear (0). Outbox: none this session.

## PENDING PUSH / GIT
- Path-scoped commits; push via `scripts/safe-push.sh` — receipt in the PROME SendMessage. Tree also carries PROME's uncommitted ORCH_LOG.tsv; not pulled, not touched.
