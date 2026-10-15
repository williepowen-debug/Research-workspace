# HANDBOOK.md — the hand-written half of THE HELM

**Owner:** PROME. Stable operating guidance plus a short source-backed priorities index, rendered by `PROME/tools/will_handbook.py`. Queue and calendar are generated from WILL_QUEUE/DOCKET. Publication policy and delivery evidence are linked in the manual below.

<!-- Declared residue 2026-10-11, plan read1: the existing renderer omits Spawn queue prose when there are no recognized current rows; spawns REVIEW remains. No verified launch slate is claimed. See reports/2026-10-11_current-surfaces-cleanup.md; current source/preflight rules remain at their canonical records. -->

## Top priorities

**2026-10-15 12:58 ET — midday closeout, first desktop sitting; levels are intraday reads, owner reads as dated:**
- **Your orders, nothing placed by PROME:** one QQQ Oct-15 715P expires at today's close (the 740 puts and the USO calls were sold 10/14, confirmed by your 10:10 capture); HBAN Oct-16 16P ×1 rides with ONE LOOK Friday before 16:00 ET (WQ-302 R-B); TBT ×5 sale approved, the order yours (WQ-357); WAL 65P ×4 before Monday's print and OZK 40P ×4 before Tuesday's (WQ-429/428), no order at the capture. Owed from your screen: the OZK/WAL fills, the lower Activity rows, a Robinhood view.
- **What the day meant:** high-yield 325 [10/14] is the first print over the 320 line since 10/1 (RED 1 of 3; LIQUID grades Friday), CCC at a window high, CoreWeave repricing hard, funding orderly, bonds rallying through a hot PPI. Nothing fired on the fire-ledger. Details: the brief tab and `HEARTBEAT.md` (31st base + amendment #1).
- **Ruled today, all encoded:** twenty Deck taps (`proposals/2026-10-15_deck-batch-16-RULED.md` and the 12:00 set): WQ-365 declined (card lapses Friday), 403 OTIC gate registered, 314 (b) with ORACLE's daily pull, 412 REG-07 void, 410 COR1M retired, 435 CRUISE re-scope, 439/440 ORACLE rules, 411 spine audit #16 run; four carrier rows left at ruling.
- **Still your word:** WQ-441 Volta baseline (by 10/17) · WQ-442 CoreWeave card (by 10/23); hands on 302 · 357 · 422; the generated queue owns the full list.

## Spawn queue

Current owner obligations and dates come from `PROME/DOCKET.tsv`; eligibility and preflight remain in `PROME/ROSTER.md` and `PROME/CLAUDE.md`. A same-minute liveness check precedes every launch; a desk you launched yourself is doorbelled, never duplicated. Tomorrow's due-row wakes (WQ-184 class, up to eight when every row is a dated catalyst or review date):

- **LIQUID** · Fri 10/16 after 08:00 ET · LIQ-07 funding verdict on the 10/15 SOFR; the 10/14 HY cell for 069 L4; discount window; TIC (L721)
- **BROCK** · Fri 10/16 · CRMT Item 1.01 backstop #3 and the bridge-6 STD check (L586 · L651); dark since 10/14
- **ORACLE** · Fri 10/16 · first bounded daily pull of the October $110 oil leg (WQ-314 (b); L729, through 11/1)
- **REGINALD** · Fri 10/16 · CFG Q3 print (call 09:00 ET, L620) and the Nano Banc P&A document check (L516)
- **CRUISE** · Fri 10/16 if dark · the re-scoped charter's first read (L712; WQ-435) — slated past the cap of four
- **GIBBS** · Mon 10/19 · first live session: retrospective read of the already-printed large banks, then FITB after the close (L704)
- **HOMER** · Mon 10/19 · NAHB October HMI (A3 leg of GATE-HOMER-THESIS-KILL) and the 10/15 spread recompute (L725)

## Runs itself — no window needed from you

Collection and desk routines keep their existing owners and schedules. Their receipts establish what actually ran; an old dated report of a successful run is not current coverage. Next-launch obligations stay in DOCKET and the owner's records; no new unattended launch is authorized here.

## The daily flow
- **Open the Helm, Your desk tab.** Check Broker actions and management gaps even when no new ruling is needed; zero pending approvals is not an all-clear. The brief tab has the story when you want it.
- **Published Fleet Ops is retired (WQ-372).** Current publication rules and receipts: `PROME/CLOSEOUT.md` step 11, WQ-382’s ruled record in `PROME/WILL_QUEUE.md`, and the latest PUBLISH entry in `PROME/state/ORCH_LOG.tsv`.
- The standalone Desk-brief page is RETIRED [your word, 8/21] — its old URL shows a pointer here; the brief tab is the brief now.

## Launching a desk
- `cd AGENTS/<NAME> && claude` then say **"please boot up."** PROME launches from `PROME/`.
- **Verify root and desk instruction loading in the actual runtime** under `PROME/COMPLETION_SPEC.md` and `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics (WQ-385). Launch from the desk directory where supported; cwd alone does not establish what was loaded.
- One machine at a time (desktop ⇄ laptop). Before switching: have every open session close out — the push happens automatically at closeout. Switching checklist: `PROME/MACHINE_LOCAL.md`.
- `! <command>` in any prompt runs a shell command in that session — used for interactive logins the agent can't do itself.

## Saying the words — how rulings work
- **A decision only exists when you say it.** The phrasing that works: **"Rule row N off your recs"** · **"Approve X"** · **"ok approve 1 and 2"** · **"go ahead with Y."** Your exact words get committed to the record the same hour, and desks execute against the word, not a paraphrase.
- **Silence never approves.** Anything gated waits; a desk re-presents dated items and stays quiet on silent-scheduled ones.
- **Nothing trades without your explicit [Approve] at live prices.** PROME never sets thresholds, never moves capital, never executes. Fresh capital deploys only on a fired trigger, $500 per card [standing rule, 6/26].
- **Position truth is your broker, never a repo file.** `FORGE/STATUS.md` is a mirror that stales between your exports — the page and every desk will refuse to fill against it.
- You can **edit WILL_QUEUE.md directly** — strike things, add notes. PROME reconciles your marks at its next touch; that file is your ledger, not PROME's.

## The glyph legend — strict, one role each [declared 8/21; registered at STATE_VOCABULARY 8/22 — the delivery-ladder and verification-basis classes minted on your word the same day]
| Glyph | Means | Never means |
|---|---|---|
| 🟢 🟡 🟠 🔴 | **Severity only**: none · monitoring · elevated · active/critical | emphasis, priority, decoration |
| `P1 P2 P3` | Priority on state surfaces: this-session · by-the-date · next-touch | — |
| ⚖️ | **A decision only you can make** (chat blocks, top of message) | general importance |
| ⛔ | Prohibition / kill-on-sight — do not carry this claim | strong emphasis |
| ⚠️ | A caveat that must travel with the number beside it | generic warning |
| 🧊 | FROZEN surface — do not cite as current | cold/inactive vibes |
| ★ | Notable result | decoration |
| ✅ ❌ | Resolved true / resolved false | agreement/disagreement |

- **In chat:** decisions arrive as `⚖️ WQ-<row>` blocks at the top of PROME's message — **the number is the WILL_QUEUE row, registered before the block is shown; you rule by number (`WQ-118 = approved`), and RECENTLY DONE is the log** [your word, 8/29]; load-bearing facts as `ATTENTION` blocks whose circle is the item's true severity. **A message with neither block needs nothing from you.**

## Where things live
- **`PROME/WILL_QUEUE.md`** — your open-items ledger (the brief's top section renders it).
- **`PROME/DOCKET.tsv`** — every dated catalyst the fleet is watching.
- **`PROME/GATES.tsv`** — the fire-ledger: registered triggers and their state.
- **`HEARTBEAT.md`** — the market-regime memo. PROME maintains and commits it under a standing grant — **you freed it from your-word gating on 2026-08-23** (record: `PROME/AUTONOMY.md` change-log row 2026-08-23; the basis was latency, never a quality grant, and PROME says so whenever it cites its own authority on this file). Root-doc lines about HEARTBEAT stay your-word-gated; new trade decisions still require your approval.
- **Everything on your two pages is DERIVED** — command compression built from the canon files above; on any conflict the owner file wins [the same banner sits atop the market memo itself since 8/22].
- **Publication and page freshness:** `PROME/CLOSEOUT.md` step 11 plus WQ-382’s ruled record in `PROME/WILL_QUEUE.md` govern when each page publishes. The latest PUBLISH receipt in `PROME/state/ORCH_LOG.tsv` establishes hosted delivery; a local rebuild alone does not.

## When something looks wrong
- **Ask the desk to verify at the artifact** — "verify that at the file/source" is the house move; every desk expects it and does it to PROME too.
- **Agent data can be hallucinated** — anything trade-relevant gets checked against the primary source (SEC filings, FRED, the issuer) before money moves [root rule 3].
- Prices are never cited from status files — desks pull live before quoting; if one quotes a stale mark, say so, it's a defect.

## Trading rails — the two-line version
- Root rule #6: **puts on green days, calls on red days** (breaks need a written measurement before the fill). Root rule #7: **roll duration, don't trim size** — trimming means the thesis broke. Both are TERRY's rails; cite them as "root rule #6/#7."
- The full risk vocabulary (fire cards, arm/deploy/disarm, harvest gates) lives at `AGENTS/TERRY/RISK_RULES.md` — its "Non-Negotiables" are numbered separately from the root rules; when citing by number, say which list.

## History and unresolved carry

[Full pre-cleanup handbook](archive/CURRENT_SURFACES_2026-10-11/HANDBOOK.md) preserves every dated priority, old spawn slate and routine-run report. [HANDOFF](HANDOFF.md) retains recovery and unresolved historical tails; [cleanup acceptance](reports/2026-10-11_current-surfaces-cleanup.md) records this rotation. The older September18 “big task” had no recorded closure in the prior handbook: its scope remains UNKNOWN; clarify the brief rather than inventing a task. The old MARCO/CATO wording-fix pointer and registry-remediation review brief remain unverified carry at their original packet/record, not closed by archival.
