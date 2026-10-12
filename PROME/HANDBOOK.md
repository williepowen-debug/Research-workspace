# HANDBOOK.md — the hand-written half of THE HELM

**Owner:** PROME. Stable operating guidance plus a short source-backed priorities index, rendered by `PROME/tools/will_handbook.py`. Queue and calendar are generated from WILL_QUEUE/DOCKET. Publication policy and delivery evidence are linked in the manual below.

<!-- Declared residue 2026-10-11, plan read1: the existing renderer omits Spawn queue prose when there are no recognized current rows; spawns REVIEW remains. No verified launch slate is claimed. See reports/2026-10-11_current-surfaces-cleanup.md; current source/preflight rules remain at their canonical records. -->

## Top priorities

**2026-10-12 — current source index:**
- **Position-facing work first:** [SCRATCH's next action](SCRATCH.md#-next-session--start-here) names the nearest expiries and existing owner; [FORGE](../FORGE/STATUS.md) carries the book. [Broker evidence](data/2026-10-11_broker-capture-TRANSCRIPTION.md) was received October11; exact capture/quote time and working orders remain UNKNOWN, Robinhood was not supplied, and D69's +$53.54 remains unexplained. Receipt date does not establish fresh quotes.
- **Computer-switch continuity:** [Closeout record](reports/2026-10-12_machine-switch-closeout.md) and [HANDOFF](HANDOFF.md) distinguish saved work from pending owner intake and hosted publication. Verify fresh owner identities before routing.
- **Already-approved work:** [WQ418/420 ruling and receipts](proposals/2026-10-11_wq418-420-RULED.md) distinguish the decision from owner encoding, independent acceptance, recipient consumption and new closeout. Prior commissioned work's closeout is not evidence that the continuation is finished; no repeat approval is owed.
- **What needs your word:** the generated queue below owns current asks. Owner work and clocks remain in [DOCKET](DOCKET.tsv); operating condition and remaining repairs are indexed in [STATUS](STATUS.md). No new trade ruling comes from this cleanup.

## Spawn queue

Current owner obligations and dates come from `PROME/DOCKET.tsv`; eligibility and preflight remain in `PROME/ROSTER.md` and `PROME/CLAUDE.md`. Use the generated clock and verified current ownership before any launch. Older dated spawn slates are history in the linked snapshot, not launch instructions.

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
