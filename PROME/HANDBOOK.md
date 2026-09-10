# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **Broker actions first:** the generated action list separates approval, order and fill evidence. After the 9/10 rulings: the XLE 65C ×1 survivor SELLS at the bid at the 9/11 open (WQ-210, your hand; fill → FORGE D-49); the VLO ×3 refiner leg is PLACED at a fresh mark once TERRY re-arms the card (WQ-213); the USO Sep-11 153C/159C entries and the KRE 25P 2027 entry stay UNKNOWN by your word (D-53/D-54).
- **Management gaps:** the position table identifies which exact contracts have a verified mapping and which require PROME/TERRY follow-through. The USO 37 shares carry NO rule by your 9/10 word (WQ-200 declined) — you manage them by hand at live prices; TLT 77P ×20 HOLD to expiry (WQ-217).
- **Evidence and work:** source dates, confirmed receipts and PROME's due work are generated below. An owner result must be reconciled before a pending ledger entry is treated as unfinished work.
- **Decisions:** current approvals come from WILL_QUEUE. Previously ruled items are not fresh requests; permanent unknowns are not repeated asks.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **BRENT** · September 10, after the noon WPSR · Brent >$100 on the second sinking is not in its STATUS; FALCON's Riesco laden-state packet + WALTER -001/-004 in its inbox (L305)
- **RED** · September 10, AFTER ~2:15 PM ET only · the first long-end buyback op prints 1:40–2:00 PM; RED corrects its FT-11 "live from 9/9" precondition before any 9/10 close is graded (L315)
- **HANS** · September 10 · ECB decision 13:45 CET → HNS-05 grade (L279); PROME pre-fetches the decision read-only if HANS is dark
- **LABOR** · next boot · claims 08:30 + the past-due 9/8 tariff summons (BD-02)
- **BRENT** · September 10 noon ET · first WPSR for the week ending 9/4 (L305); no duplicate BRENT
- **OTTO** · September 11 · CRMT's EXTENDED waiver date — RP-OTT-5.1 Letters 1+2 at the close (L311); BROCK staged the grade
- **DAEDALUS** · September 12 sitting · L247 spec adversarial review (L313) beside L208/L209/L258/L294
- **REGINALD** · next owner pickup · WAL close grades owed on the ROLL70-EXIT guard (0-of-3)
- **FERT · TERRY** · September 16 · G5 weekly (L310) · 007 weekly review; the 9/9 officials are PROME's consumer read 9/10

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
