# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ THE FIRST CONFIRMED SINKING, RULED [9/7 14:42]:** the war-theater desk fired its hull-loss gate on the Kylo and moved its mark to 75; the oil desk read its own letter and found an empty hull in a blockaded trade destroys no capacity, then found its own status line had handed its capital trigger to the other desk's gate. **You ruled stand down, the letter governs, and "vessel SUNK" now carries a capacity floor** — applied by the oil desk on all three of its surfaces within the hour. $0 moved.
- **★ THE OIL INSTRUMENT ROLLED WITHOUT A WORD [ORACLE 9/7 → row 190, by 9/11]:** the question the docket carried since 8/11 was aimed at a death that never happened — the supply leg rolled to the September WTI-$100 market on 8/27 as maintenance. Ratify it, with the 9/18 contract switch disclosed. Its spread tripwire fired (45.5→36.0) and the desk did not raise the row; a full session re-check is owed.
- **★ THE LABOR DESK'S DAY [9/7]:** the revision bias you keep describing is now measured — first print to current averages −66K a month, 35 of 44 months revised down; its boot sweep had fired retired triggers for 31 days; its charter was over the read cap and was split on your word (row 193, delivered 17:09). Four rounds of outside review, every defect confirmed at the artifact. **Row 191 (by 9/11):** let the S1 build lapse as superseded by the spawn rule.
- **★ ONE PROCESS DEFECT WORTH A RULE [Codex 9/7]:** an amendment read for one correction did not update a second decision derived from the original packet — the coordinator registered a question the desk had already withdrawn. Amendments should name the queue items they affect; consumption should reconcile each. Saturday's spine audit carries it.
- **★ THE MARKET LINE [9/4 closes; 9/3 officials; Monday electronic prints as stamped]:** Brent ~$97.5 live Monday, five sessions up, curve lifting together, $100 not a threshold · SKEW 151.58 [9/4 CBOE], 2 of 4, Tuesday extends or resets, Wednesday's close is the earliest fire · HY 265 [9/3], 5 bp from the re-kill line, 15 from the re-arm; **the convergence desk's second read can lock Wednesday, two days before the CPI it is named after** · DGS10 4.77, the exit gate 27 bp away · WAL 80.95, the exit line 95 cents above.
- **Your queue by date:** 163 (9/10) · **190 · 191 · 179 · 183 (9/11)** · 187 · 133 (9/12) · 181 ② (9/14) · 161 (9/15) · 160 (9/29) · 182 (9/30) · 31 (11/1) · 98 · 74 · 169. **By hand:** the TLT 85P sell at the broker's count Tuesday · the three broker facts · the expired Robinhood put · the systemic-risk desk's charter word in its window.
- **Rules that came out of today:** two desks on one event, on different letters, produce a better question than either verdict — the disagreement locates the defect · a gate held under a counterparty's finding deserves less scrutiny than one relaxed · when you replace a state because a string is matchable, the provenance note must not contain the string · message timestamps are UTC; stamp from the clock, never the narrative.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **LABOR** · Fri 9/4 after 08:30 · grade payrolls off the frozen card (T-03 fires on a flat print → CARL + HENRY); idle in your window — reopen it or PROME re-pings
- **REGINALD** · Fri 9/4 after the close, only if WAL ≥ $81.90 · it owns the December put's exit grade (0 of 3) and has been dark since 9/1; also holds HOMER's wall retraction and WAL's REG-15 refutation
- **BRENT** · Fri 9/4 · the crude positioning print grades its COT gate; letter defects from three reads are in its inbox; OSPREY's diesel reconcile
- **OTTO** · Fri 9/4 → Mon 9/7 · CRMT's weekly liquidity test, the covenant waiver expiring Labor Day, CARL's L1 answer
- **DAEDALUS** · 9/4–9/5 · scorecard first render, renderer checkpoint; six PROME packets waiting (the claim-check blind spot, two ledger-staleness marker packets, tie-sets, WQ-163 cc)
- **HAWK** · this week · basis-pair audit 17 days overdue, blocking OSPREY's band; Canada 9/8 owner
- **CARL** · by Tue 9/8 · V2 sitting prep (≤9/10), WQ-151 first application ~9/15
- **NEXUS · LIQUID** · ≤9/11 · both closed out tonight; NEXUS owes two missed re-marks and the 9/11 grade, LIQUID encodes any-one-name and the retire-and-repoint
- **AEOLUS · VULCAN · CORAL · FERT · CRUISE · WAL · MARCO** · dated per DOCKET · MSI second reading 9/13 · FERT G5 9/9 · MU 9/30

## Runs itself — no window needed from you
- **The registry review brief is already written** [in the remediation record] — the reviewer lane needs no design work from you, only a session.
- **The oil desk's Wednesday data routine fired on schedule straight through the dark spell** [SPR flagged at a 43-year low, 4th week running — recorded, not adjudicated]; the collection lane's trigger watch ran unattended too.
- **Friday's graded tests run in their desks' own windows** once spawned — the gold test, positioning data, the bond-test close; none needs a separate word beyond the spawns above.

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

- **In chat:** decisions arrive as `⚖️ WQ-<row>` blocks at the top of PROME's message — **the number is the WILL_QUEUE row, registered before the block is shown; you rule by number (`WQ-118 = approved`), and RECENTLY DONE is the log** [your word, 8/29]; load-bearing facts as `ATTENTION` blocks whose circle is the item's true severity. **A message with neither block needs nothing from you.**

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
