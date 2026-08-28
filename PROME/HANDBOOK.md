# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ MONDAY 8/31 AFTER 16:15 IS THE DECISION: the kernel sitting needs only your window** [row 103 — every other precondition closed 8/27; sequence: the 8/28 real-yield print decides MIDAS-06 (one number) → your word on the no-verdict band [row 66] → MIDAS authors activation 2 → you rule the window → MIDAS + RED spawn → grants promotion between activations D and E, by design].
- **★ THE MARKET BELIEVED WARSH — and credit ignored it.** Sept-hike odds 31%→50% [8/28 live], long end *rallied* (5s30s −6bp), gold −3.3%, NVDA −4.6%; HY 263bp [8/27] = 2026 low while CCC/HY = the three-year record. Nearest trigger on the board: RED's HY<260 ×3 at 3bp; 8/28's close publishes Monday.
- **★ Four counts sit on the HY 260 line and only one is a registered kill** [row 106 — LIQUID + HENRY concur on the relabel; one word]. LIQUID's silent dealer gate [row 88 — option A, unanimous].
- **HEN-42 = DENY (term premium led July; the policy channel is alive today)** — flips Saturday on its pre-written record; BOND owes the C-36 two-part label and is dark; the 9/9 collision's precondition is clear.
- **Oil's verdict: the peace framework unwound the paper premium, not the physical one** — Hormuz flows at two-thirds of pre-war (1.7× the old falsifier), "supply impaired" retired; rigs 447 (−5) is reclassification with horizontal rigs at a series high; crude positioning joint no-verdict; EU storage will NOT refill to 84% (~70–76%).
- **Gold: the positioning falsifier fired against its own desk** [COT net/OI 56.86%, chased spec flow]; MIDAS-06 provisional (d), Monday one number; palladium +8% / +4.5σ needs Monday's closed bars to confirm.
- **Banks/BDC:** WAL closed $0.55 above its trigger [78.55, un-fired, next close Monday]; First Brands is Chapter 7 (BROCK dark 15d — re-size owed); Tricolor's CEO sat on Origin Bancorp's board (not a Reg O violation on face, enforcement orange); the $160B multifamily wall was a misattributed sponsor quote — retires 9/4.
- **Europe (HANS revived):** Bund 3.29% = highest since 2011 (European term premium), UK 30Y 5.80% = highest since 1998, BoE 3.75% with three hike votes — three hawkish banks off ONE energy shock, count it once.
- **⛔ THE CANADA TARIFF REMAINS LIVE** [since 8/22]; **Canada retaliates Tue 9/8 on ~$28B.** Carried, unchanged.
- **Housekeeping you ruled today:** P1 read-cap budget is canon (root line committed; 7 desks rotated under it); row 89 declined; HANS spawned as Europe owner; FLG's charter rewritten; T3 re-specified by LIQUID+HENRY (no dissent; earliest verdict 9/23).

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **BOND** · before Mon 8/31 · owes the C-36 two-part label within a session of Saturday's HEN-42 flip; HANS's Bund/gilt packets + T6 words in its inbox
- **BROCK** · Mon 8/31 · First Brands → Chapter 7 (8/24) needs the BDC re-size; dark 15 days; WALTER's one doorbell recommendation
- **HOMER** · by Thu 9/3 · publishes the $160B maturity-wall retirement on 9/4 (kill-setter); five carriers to route
- **MIDAS + RED** · Mon 8/31 post-16:15 · the kernel sitting (MIDAS-06 final first)
- **OZK** · Mon 8/31 · IQHQ August maturity window closes; disclosure sweep unrun (your window)
- **HAWK** · Mon 8/31 · palladium I2 re-open "n=3" if Monday's closed bars confirm
- **SAM · VULCAN · DEWEY · CARL · FALCON · FERT · ORACLE** · next week · dated items per DOCKET (Friday quadruple · VULCAN-16 grade · DR-4 refuted · retail question + V2 9/10 · consumer dates 9/1-9/2 · T6 daily close)

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
