# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ THE REGISTRY PILOT IS FULLY STAGED AND WAITS ONLY ON YOUR START/END TIME — next session's first item, on your own word** ["we will work on this directly in the next reboot", 8/27]. The red team reviewed it [verdict: proceed], its two findings were fixed and re-probed the same day, every file is hash-pinned, and the door provably refuses to open until your exact times are in the activation document. The sitting is ~30-60 minutes, you attending, worst case two extra files in an append-only folder.
- **★ THE CRUDE MOVE IS CERTIFIED SMALLER: −6.9%, not −8.5%** [8/21→8/26, like-for-like on the named October contract; the overstatement was one vendor's closing price, now with the routing desk to reconcile — three values exist for Tuesday's close]. The premium-unwind read *survives and is cleaner* at the certified size, and **your ruling stands: holding both October oil calls, riding the thesis** ["this ride isn't over yet", 8/27] — down ~$930 from their August peak as marked, concentration warning standing.
- **★ FRIDAY 8/28 IS THE MONTH'S HEAVIEST DAY — nine items and your two bond-test words.** The QCEW employment revision [labor desk moved 35%→15% the night before on primary-verified evidence; ⛔ tomorrow prints the *preliminary* — "confirmed" is the day's most likely error; and the two desks pointing the same way are ONE evidence chain read twice] · the new Chair's 10 AM keynote · the gold test on its frozen letter [needs +8bp of real yield in two sessions or it fails] · the architecture sweep, now carrying **eight findings from five desks** · your bond-test words [the deadline word + the NEW joint ask: publication lag makes a Friday record invisible to a Saturday grader — rule it, don't assume it].
- **A September Bank of Japan hike is now ~87% priced** [8/27; was carried at ~73% on a stale read whose direction-caveat was backwards]. The risk flipped: the bigger yen move now comes from a surprise *hold*. Japan's weekly flow data also printed its third most negative week in 21 years — watched, real, and explicitly *not* the reopening event the rules require.
- **Nvidia's quarterly filing landed five days early and quantifies the AI-credit structure: $3.5B → $108.5B of customer-obligation guarantees in one quarter**, with the filing itself stating customers "lack the ability to secure investment-grade financing." No alarm tripped — and the desk's honest note is that its alarms watch market prices while this quarter's risk grew in contract terms. Goes to Friday's sweep.
- **⛔ THE CANADA TARIFF REMAINS LIVE** [since 8/22]. **Canada retaliates Tue 9/8 on ~$28B.** Carried, unchanged.
- **Nothing fired today**: credit parked 10bp from both lines [HY 270, 8/25] · Western Alliance $1.60 above the bank trigger · claims came in benign [203K, no band] · the banking-report desk graded its trigger NOT FIRED at the primary. The quiet is real but two of the most exposed reads [private credit, bank spiral] belong to desks dark two weeks.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **LIQUID** · next wave, before Fri PM · four items wait on it [a tripped Japan-flow bar, two peer packets, the credit-quality ratio flip it owns] and its gate review lands Friday
- **REGINALD** · next wave · six items deep [the bank-trigger near-miss annotation, two consumed reports, a peer refresh, and a real internal contradiction a peer caught in its own file]
- **BROCK** · soon · two-plus weeks dark holding the private-credit adjudication with credit 10bp from the re-arm line; important, edging toward urgent
- **HENRY** · by Sat 8/29 · a peer's answer to its own question sits in its inbox and rides to Saturday; its gamma re-measure is still the board's blind spot
- **WALTER** · any window · owes the three-way crude-close reconciliation the certified figure depends on
- **ORACLE** · before 9/1 · the deferred instrument-succession decision needs its options brief; the supply leg dies 9/1
- **FALCON** · with/behind the next oil touch · corridor gates, the permanent-route calendar row, tanker weekly
*(Ran today, no re-spawn needed: SAM · BRENT · VULCAN · MIDAS · RED · BOND · CREED · LABOR + TERRY — all delivered and closed out; VULCAN's post-close packet arrives on its own.)*

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
