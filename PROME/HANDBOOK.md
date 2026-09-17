# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **Kill-rule ruling (WQ-157, 9/19):** the bond desk measured both halves of its thesis-kill pairing and neither supports it — the stock leg inverts (p=0.009, but only 35–40% power for its own effect), the funding leg detected nothing (p=0.523, MDE ≈16bp at the registered α). Every result favours the desk's own thesis; it recommended nothing. PROME rec: PARK, successor test chosen at the sitting.
- **Spawn slate held on your 09:15 cost word:** FERT · REGINALD · RED · HENRY (9/18) · SHADE (proximity) · TERRY · OSPREY. Two words per desk. Nothing spawned beside a live desk today; L404 went to the live bond session by doorbell.
- **Hands, unchanged:** VLO re-affirm or withdraw by 9/18 (WQ-213); the Trends month (WQ-225); the two 9/16 expiries' disposition (WQ-169).
- **Post-FOMC regime:** unchanged from the morning — hike in at 3.75–4.00%, oil down on a restart claim that is press, not a barrel; TIPS reopening CLEAN with the highest stop since Oct-2008, read as adequate not strong. HEARTBEAT is over its rotate line and re-bases at the next boot.
- **Evidence and work:** source dates, confirmed receipts and PROME's due work are generated below. An owner result must be reconciled before a pending ledger entry is treated as unfinished work.
## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **RED** · on your word, today or 9/18 · L376/L377: the FT-10 ^SKEW grade — a sub-150 9/16 bar exists on a non-registered source, so the 2-of-4 run may reset; only RED grades on the CBOE basis; plus the 9/18 leg-3 read with VIOLET.
- **FERT** · on your word · L310 + GATE-FERT-G5: the 9/16 DTN print lapsed ungraded (re-dated 9/23); the desk is dark since 9/15.
- **HENRY** · 9/18 · L383: the opex gamma re-measure; every wall before 9/16 is void; VIOLET's 9/18 read rides with it.
- **REGINALD** · on your word · L352: its board_log is invisible to WALTER's telemetry; a fix at the desk, no date pressure.
- **SHADE** · Tier-2 candidate · DAEDALUS's proximity ask: HY 276 vs its 280 line, dark 20 days; no dated row names it.
- **TERRY · OSPREY** · the morning slate · L379 (STATUS at cap, structural) · L397 + GATE-OSPREY-001 review 9/19.
- **SAM** · at the next boot after the overnight BOJ decision · L34 names SAM; a due-row spawn under the standing rule, no word needed.

## Runs itself — no window needed from you
- **The registry review brief is already written** [in the remediation record] — the reviewer lane needs no design work from you, only a session.
- **The oil desk's Wednesday data routine fired on schedule straight through the dark spell** [SPR flagged at a 43-year low, 4th week running — recorded, not adjudicated]; the collection lane's trigger watch ran unattended too.
- **Friday's graded tests run in their desks' own windows** once spawned — the gold test, positioning data, the bond-test close; none needs a separate word beyond the spawns above.

## The daily flow
- **Open the Helm, Your desk tab.** Check Broker actions and management gaps even when no new ruling is needed; zero pending approvals is not an all-clear. The brief tab has the story when you want it.
- **Fleet Ops is the instrument panel** — gauges, gates, who's stale. Look when you want to know how the machine is running, not what it needs.
- The standalone Desk-brief page is RETIRED [your word, 8/21] — its old URL shows a pointer here; the brief tab is the brief now.

## Launching a desk
- `cd AGENTS/<NAME> && claude` then say **"please boot up."** PROME launches from `PROME/`.
- **Always launch from the agent's own folder.** Launched from the repo root, an agent runs without its domain rules and won't know it — if a desk seems to be missing its own knowledge, this is the first thing to check.
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
- **Your pages, two:** the Helm (default read — desk, brief, and manual in one) · Fleet Ops (instrument panel). Both regenerate at every PROME closeout; each shows its own build time — an old stamp means canon needs a session, not that the page is broken. *(The standalone Desk brief retired 8/21; its URL points here.)*

## When something looks wrong
- **Ask the desk to verify at the artifact** — "verify that at the file/source" is the house move; every desk expects it and does it to PROME too.
- **Agent data can be hallucinated** — anything trade-relevant gets checked against the primary source (SEC filings, FRED, the issuer) before money moves [root rule 3].
- Prices are never cited from status files — desks pull live before quoting; if one quotes a stale mark, say so, it's a defect.

## Trading rails — the two-line version
- Root rule #6: **puts on green days, calls on red days** (breaks need a written measurement before the fill). Root rule #7: **roll duration, don't trim size** — trimming means the thesis broke. Both are TERRY's rails; cite them as "root rule #6/#7."
- The full risk vocabulary (fire cards, arm/deploy/disarm, harvest gates) lives at `AGENTS/TERRY/RISK_RULES.md` — its "Non-Negotiables" are numbered separately from the root rules; when citing by number, say which list.
