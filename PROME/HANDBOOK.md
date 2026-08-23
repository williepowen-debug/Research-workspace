# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **⛔ THE CANADA TARIFF IS LIVE** [+50% duties took effect 12:01 a.m. ET Sat 8/22 — verified at the Federal Register by three desks independently]. **It went live by DEFAULT: a deal and an extension each needed a signature, and going live needed nothing.** The document is titled "Temporary Suspension" and reads like a pause — that reading is backwards; the suspension was a three-day date move that has expired. **Canada suspended talks 8/21 and retaliates Tue 9/8 on ~$28B.**
- **TWO words are now owed by you before Fri 8/28** [registered 8/22 evening as a ledger repair — they were live earlier and had been carried on a pointer view, not the live list]: the bond-test conjunctive clause [after the funding desk concurs ~Monday] and the bond desk's frozen-text repairs [one clause its own owner still marks 🔴 open]. Present together, one sitting.
- **Two NEW things need your word, both from Saturday night's session** [neither is urgent, both are first-ask]: **① the root instruction file's copy of the messaging rule is now incomplete** — the fleet adopted a new branch for what happens when a signal's owner is asleep, and the root file still only describes the awake case. It's a file only you can approve changes to. **② one part of the world has a signal, a filing code, and no live analyst** — the Europe desk has been dark 34+ days and the new mechanism cannot wake a desk that doesn't exist. That's a roster call, not a plumbing one.
- **A new rule went live Saturday night: when a signal's owner is asleep and something real is on the clock, the router now rings me instead of the inbox, and I decide whether to wake that desk.** If I do wake one, that session clears the desk's *whole* backlog rather than the one item that triggered it — because desks here run about three days a month, so a session is a scarce thing to spend. It is deliberately hard to trigger and will fire rarely. Nothing about it can move money.
- **Honest note on Saturday night: I got four things wrong and every one was the same mistake** — reading a number off a convenient screen without checking what that number actually counts. Three you caught by asking. The fourth was caught by the trade desk I woke, which refused my correction and turned out to be right. All four are fixed on the record and written into the fleet's memory; nothing reached a position and no money moved.
- **Monday 8/24 is the loaded day — seven independent reads land**, the FDIC banking-report window opens [its desk needs spawning], and the labor desk has two overdue items — including a wrong Jackson Hole date it keeps alarming on, and Jackson Hole is **this week** [8/27-29].

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **HAWK / MARCO** · Monday · tariff outcome RESOLVED 8/22 [both verified at primaries independently]; the open work is aftermath + the 9/8 retaliation, and line-level scope is established by nobody
- **SAM** · soon · positioning data + Japan CPI grading touch owed since Friday
- **MIDAS** · soon · gold positioning touch + five ruling-encodes waiting in its inbox
- **CREED** · 8/24–29 window · the FDIC banking report is its first trade-relevant trigger and it only exists when spawned
- **LABOR** · any window · one wrong date (Jackson Hole) it keeps alarming on daily, plus the KELYA expiry log
- **ZHAO** · any window · inbox session — 27-item backlog its new boot triage can't clear alone

## Runs itself — no window needed from you
- **The heavy sitting already ran Saturday** [audit #10 · vocabulary mint · promotion pass · registry envelope — all executed 8/22]; Sunday's residue is optional and PROME's.
- **Monday 8/24, seven reads in desk windows you already run or PROME's:** hedging-map re-measure [the old figure is dead data] · bond-test concurrence · the oil desk's $85 tourism-cost trigger grades · funding-desk Test B · the VLY exercise outcome · prediction-market pin day 2 · Saturday's tariff aftermath.

## The daily flow
- **Open the Helm, Your desk tab.** The one-line summary under the title is the whole state — if it reads zero words and zero desks, you're done. The brief tab has the story when you want it.
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

- **In chat:** decisions arrive as `⚖️ YOUR DECISION` blocks at the top of PROME's message; load-bearing facts as `ATTENTION` blocks whose circle is the item's true severity. **A message with neither block needs nothing from you.**

## Where things live
- **`PROME/WILL_QUEUE.md`** — your open-items ledger (the brief's top section renders it).
- **`PROME/DOCKET.tsv`** — every dated catalyst the fleet is watching.
- **`PROME/GATES.tsv`** — the fire-ledger: registered triggers and their state.
- **`HEARTBEAT.md`** — the market-regime memo (PROME-written, your-word-gated).
- **Everything on your two pages is DERIVED** — command compression built from the canon files above; on any conflict the owner file wins [the same banner sits atop the market memo itself since 8/22].
- **Your pages, two:** the Helm (default read — desk, brief, and manual in one) · Fleet Ops (instrument panel). Both regenerate at every PROME closeout; each shows its own build time — an old stamp means canon needs a session, not that the page is broken. *(The standalone Desk brief retired 8/21; its URL points here.)*

## When something looks wrong
- **Ask the desk to verify at the artifact** — "verify that at the file/source" is the house move; every desk expects it and does it to PROME too.
- **Agent data can be hallucinated** — anything trade-relevant gets checked against the primary source (SEC filings, FRED, the issuer) before money moves [root rule 3].
- Prices are never cited from status files — desks pull live before quoting; if one quotes a stale mark, say so, it's a defect.

## Trading rails — the two-line version
- Root rule #6: **puts on green days, calls on red days** (breaks need a written measurement before the fill). Root rule #7: **roll duration, don't trim size** — trimming means the thesis broke. Both are TERRY's rails; cite them as "root rule #6/#7."
- The full risk vocabulary (fire cards, arm/deploy/disarm, harvest gates) lives at `AGENTS/TERRY/RISK_RULES.md` — its "Non-Negotiables" are numbered separately from the root rules; when citing by number, say which list.
