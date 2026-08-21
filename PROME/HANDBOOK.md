# HANDBOOK.md — the hand-written half of Will's Operator Handbook page

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **Say the Batch A word** — two one-liners for the memory system, drafted verbatim, first agenda item of your next session [queued 8/21].
- **Monday 8/24 brings one more word:** the bond-test concurrence lands, then it needs one ruling from you before 8/28.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **AEOLUS** · before Sun 8/24 · its silence is destroying evidence — AEO-11's window passed unobserved and the retro-read decays daily; Sunday's audit grades it first
- **SAM** · soon · positioning data + Japan CPI grading touch owed since Friday
- **MIDAS** · soon · gold positioning touch + five ruling-encodes waiting in its inbox
- **CREED** · 8/24–29 window · the FDIC banking report is its first trade-relevant trigger and it only exists when spawned
- **LABOR** · any window · one wrong date (Jackson Hole) it keeps alarming on daily, plus the KELYA expiry log
- **ZHAO** · any window · inbox session — 27-item backlog its new boot triage can't clear alone

## Runs itself — no window needed from you
- **Sunday 8/23 sitting** (PROME): registry audit + the vocabulary block.
- **Monday 8/24:** hedging-map re-measure, test grades, prediction-market pin day 2 — all in desk windows you already run or PROME's.

## The daily flow
- **Open this page, Your desk tab.** The one-line summary under the title is the whole state — if it reads zero words and zero desks, you're done. The brief tab has the story when you want it.
- **Fleet Ops is the instrument panel** — gauges, gates, who's stale. Look when you want to know how the machine is running, not what it needs.
- The standalone Desk-brief page still exists and shows the same content as the brief tab; one word retires it if this page has replaced it for you.

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

## The glyph legend — strict, one role each [declared 8/21; fleet register lands at STATE_VOCABULARY Sunday]
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

- **In chat:** decisions arrive as `⚖️ YOUR DECISION` blocks at the top of PROME's message; load-bearing facts as `ATTENTION` blocks whose circle is the item's true severity. **A message with neither block needs nothing from you.**

## Where things live
- **`PROME/WILL_QUEUE.md`** — your open-items ledger (the brief's top section renders it).
- **`PROME/DOCKET.tsv`** — every dated catalyst the fleet is watching.
- **`PROME/GATES.tsv`** — the fire-ledger: registered triggers and their state.
- **`HEARTBEAT.md`** — the market-regime memo (PROME-written, your-word-gated).
- **Your pages:** this Handbook (default read — desk, brief, and manual in one) · Fleet Ops (instrument panel) · the standalone Desk brief (same content as the brief tab, kept until you retire it). All regenerate at every PROME closeout; each shows its own build time — an old stamp means canon needs a session, not that the page is broken.

## When something looks wrong
- **Ask the desk to verify at the artifact** — "verify that at the file/source" is the house move; every desk expects it and does it to PROME too.
- **Agent data can be hallucinated** — anything trade-relevant gets checked against the primary source (SEC filings, FRED, the issuer) before money moves [root rule 3].
- Prices are never cited from status files — desks pull live before quoting; if one quotes a stale mark, say so, it's a defect.

## Trading rails — the two-line version
- Root rule #6: **puts on green days, calls on red days** (breaks need a written measurement before the fill). Root rule #7: **roll duration, don't trim size** — trimming means the thesis broke. Both are TERRY's rails; cite them as "root rule #6/#7."
- The full risk vocabulary (fire cards, arm/deploy/disarm, harvest gates) lives at `AGENTS/TERRY/RISK_RULES.md` — its "Non-Negotiables" are numbered separately from the root rules; when citing by number, say which list.
