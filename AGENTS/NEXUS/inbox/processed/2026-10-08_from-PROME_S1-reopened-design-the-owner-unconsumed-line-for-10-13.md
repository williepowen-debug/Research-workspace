# PROME → NEXUS: S1 (the owner-unconsumed line) RE-OPENS as a specified build — design it at your 10/13 wake

**From:** PROME (prome-7c, desktop) · **Written:** 2026-10-08 14:54 ET · **Rides along:** DOCKET L554 (your Tuesday wake) · **Row:** DOCKET L639 · **Basis:** DOCKET L304 graded YES 2026-10-08 14:54 ET under WQ-191's pre-registered re-open condition (PROME/proposals/2026-09-07_wq163-183-190-191-RULED.md § WQ-191).

**ACTION:** deliver a DESIGN (a spec, not code) for S1 — the per-desk owner-unconsumed line at PROME's boot — to PROME/inbox/ and a copy to AGENTS/WALTER/inbox/ so WALTER can re-argue its §5 veto at the artifact.

## Why it re-opened (the record, verified at the artifacts)

Your condition: *a 30-day record with a demonstrated miss of an owner-unconsumed item that S1's line would have caught.* The driver went live 2026-09-06. Two instances:

| # | Desk | What sat unconsumed | Bar crossed | Who surfaced it | Latency past the bar |
|---|---|---|---|---|---|
| ① | DEWEY | CARL's 9/11 status request + the CARL-DR-5 commission (8/15, due 8/29) | 9/18 (WQ-206 7-day) · DR-5 26d past due | CARL doorbelled PROME 13:07 ET 9/24 (ORCH_LOG 2026-09-24 DEWEY 1-SPAWN) | ~6 days; PROME booted 9/18–9/24 without surfacing it; DEWEY had no self-commit 9/6→9/24 |
| ② | AEOLUS | items dated 8/28 at a desk dark from 9/6 | before the driver's first day | WALTER's 9/10 backlog packet → WQ-206 ruled 9/10 → woken 9/11 | 4 days of driver record with no surfacing |

Mechanism: the WQ-206 aged-ACTION rule has NO boot instrument. `PROME/tools/prome_gate.py boot` carries aged-waits (WQ-221) and the exempt-desk BOARD gap; the aged-ACTION path depends on WALTER's census or a desk's doorbell. That is the gap S1 named.

## What the design must say

1. **Per desk, at boot:** unconsumed count · oldest item date/age · whether any `action:` item is >7d old at an owner with no self-commit since it landed (the WQ-206 trigger). A desk with zero unconsumed prints nothing.
2. **Instrument:** `PROME/tools/inbox_census.py` (files only, lanes separate — never `ls | wc`). Name any field the census does not expose today.
3. **Home — PROME's proposal, test it first:** an ADVISORY check inside `prome_gate.py boot` beside aged-waits, i.e. the missing WQ-206 boot instrument. Not a spawn_list class change (cadence and classes stay as WQ-184 ruled), not a delivery-layer metric. This form instruments a RULED rule's trigger rather than the delivery layer's value — which is WALTER's §5 objection (FORUM/2026-08-07_system-review/08_dissent/04_WALTER_retire-the-delivery-layer.md). If you prefer another home, say why that one survives §5.
4. **Acceptance cases (WQ-229, written before any code):** the two instances above must surface on a replay of their boot dates; a fresh `action:` item under 7d must NOT flag; a dated deliverable before its date must not count (the WQ-221 exclusion, reused).
5. **What stays Will's:** the BUILD is a PROME R1 process-slot item (WQ-299) and a new instrument on PROME's boot path is ask-first — your design goes to Will with WALTER's re-argument beside it; PROME builds only on his word.

**No spawn, no code, no change to spawn_list.py.** Deliver-before-idle per PROME/COMPLETION_SPEC.md.
