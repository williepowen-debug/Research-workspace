# The silent-fire ledger — every trigger that fired without us knowing
**Author:** PROME · 2026-08-07 late (4th session) · Phase 1, thread 03

Will's sharpest complaint — "there have been triggers that have fired without the system or myself knowing" — is not a feeling. It has a documented history. Here is every instance I can cite from the repo record, with the cause class for each.

## The ledger

| # | Incident | Fired | Discovered | Blind time | Cause class |
|---|---|---|---|---|---|
| 1 | **GATE-VIO-110** — VIOLET's Gate A + C both fired; the same-session tail-hedge packet-build never ran | 7/2 | 7/9 (backfill audit) | **7 days** | Owner frozen mid-session; consequence orphaned |
| 2 | **TERRY ARM2** — DGS10 5-of-5 completed, card should have armed | Mon 7/13 | 7/16 boot | 3 days | Machine offline (7/13-7/15 gap); *caught by GATES.tsv — the fix from #1 working as designed* |
| 3 | **GATE-VIO-116 F3** — MOVE/DGS10 rates-vol re-look fired | 7/13 | 7/16 | 3 days | Same offline gap |
| 4 | **MIDAS kill-condition #3** — gold +9.68%/3wk through rising real yields; condition was live and completable through its window | window closed 8/6 | 8/7 (revival session) | up to **15 days dark** | Owner not running; AND the owner's own watch script said CONVERGE rc=0 — its 90d window was blind to its registered 3-wk trigger (instrument-spec defect, fixed 8/7) |
| 5 | **HAWK's unread falsifier** — a WALTER-delivered signal containing the exact correction to HAWK's own canonical thesis sat in its inbox | — | 9 days later | **9 days** | Owner not running; inbound lane not boot-mandatory (since made so) |
| 6 | **Orphaned packets, pre-detector** — ~12% of cross-agent packets never reached recipients (authored but uncommitted) | ongoing | 7/23 (HENRY memo) | weeks, silently | Delivery plumbing; birthed carve-out ① + orphan_check |
| 7 | **OSPREY's stuck carrier packet** — two Will-gated falsifier defects (decorative thesis-kill; fires-on-letter exit rule) drafted 7/31, packet never left its outbox | 7/31 | 8/7 (DAEDALUS batch) | **7 days** | Delivery plumbing (queue row 33 now) |
| 8 | **LABOR's stranded packets** — incl. a 6-session escalation, stranded in a dead tree that kept regrowing (regrow #6) | — | 8/7 | multi-session | Delivery plumbing (dead-path class, sender since re-pointed) |
| 9 | **WAL filing into the dark period** — the Q2 filing landed 7/31; the fleet's frame assumed it was still ahead; discovered at EDGAR only when a spawn was about to run on the false premise | 7/31 | 8/7 | 7 days | No filing-feed watcher; premise carried instead of checked |
| 10 | **BRENT's moved-but-unlogged files** — 6 older signals filed to processed/ without registry rows; a count-based check passes this state | — | 8/7 reconcile | unknown | Instrument blindness (check counted, didn't match) |
| 11 | **The 32-item inbox pileup** (~20 info-cc duplicates) — not itself a fire, but the flooding that makes fires invisible | July | 7/27 | — | Attention flooding; birthed board_scan |

Adjacent-but-distinct: the 8/2 fetch.py FX defect rendered USD/JPY −2.40% against a true −0.68% *adjacent to a Will-gated capital trigger* — a near-miss silent MIS-fire, same family, different sign.

## What the pattern actually says

Group by cause and the distribution is lopsided:

- **Owner-not-running (#1-5): the dominant and most dangerous class.** Every domain agent's gates, kill-conditions, and inbound falsifiers evaluate ONLY when that agent has a session, and sessions happen only when Will launches them. Latency to detection = Will's launch cadence. This is structural, not behavioral — no amount of discipline inside sessions fixes what happens when there is no session.
- **Delivery plumbing (#6-8):** largely addressed by carve-out ① + orphan_check + the dead-tree migrations — the orphan class demonstrably shrank. But #7 and #8 both post-date the fixes, so the class is reduced, not extinguished.
- **Instrument blindness (#4b, #10):** the check runs and returns green while the condition is true. The scope-limited-confident-answer disease (4 instances on 8/7 alone). No single mechanism covers this; it yields to spec review, not more checks.

## What already works, and the residual hole

GATES.tsv (born from #1) genuinely works for its scope — #2 was caught by exactly the boot-rule it created. But its scope is **registered action-gates read at PROME boots**. The residual hole is everything else: owner-ledger kill-conditions, prediction falsifiers, and any condition requiring a DATA PULL to evaluate. Those fire in the dark whenever the owner is dark. MIDAS #4 is the clean demonstration: the condition was machine-checkable the whole time — gold price and DFII10 are both free API pulls — and nothing in the system was pointed at it.

**The one change that closes the largest share of the class:** decouple *condition evaluation* from *agent sessions*. The RESEARCH-INTAKE lane already proves the pattern — the HY >280/<260 lines are watched machine-independently every weekday, and that watch has never gone dark. Extend it: a scheduled evaluator that walks a registry of machine-checkable registered conditions (GATES rows + owner kill-conditions that reduce to a series + threshold) and raises a flag file/alert when one crosses. Sessions then adjudicate; the machine only watches. Adjudication stays human/owner-gated — this moves DETECTION off the launch calendar, nothing else.

I'll hold the full proposal for 06_proposals per the charter. Self-inclusion note: PROME's boot-time GATES scan is itself launch-gated — on any day I don't boot, the coordination layer's own safety net is dark too. I am not outside this diagnosis.
