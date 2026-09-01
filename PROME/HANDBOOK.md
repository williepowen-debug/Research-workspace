# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ WED 9/2 10:00 ET — KERNEL SITTING 2 RUNS IN YOUR CONFIRMED WINDOW** [row 103 done; DOCKET 233]: `[14:00Z, 17:00Z)`. PROME must be booted at 10:00 to mint the five activation packets at the open; then RED verifies and acceptance runs. This morning's attempt failed only because no PROME session was open to mint — MIDAS and RED were both right on the letter.
- **★ REG-T-02 FIRED ON TUESDAY'S CLOSE** — Western Alliance $77.26, the first close under $78 of the new cycle, graded by REGINALD at its own instrument. The move was sector-wide (the bank fell less than its sector ETF; the private-credit managers were the epicentre, BX/OWL −4.6%), and the credit mechanisms behind the thesis did not move. **Two orders are yours to place** [rows 144/145 done]: the WAL Dec-18 $70P roll (≤$2.75, first green WAL day, TERRY posts the live ask) and a resting GTC to sell one USO Oct $135C at ≥$14.25; a USO close under $135 sells both, Fri 10/09 is the hard stop.
- **★ Iran is a campaign, not an exchange:** a second US strike wave at noon 9/1, two supertankers hit off Khasab the night before (crews safe), Iran firing at Aqaba. Brent BZX26 $95.22 (+5.2%). The Kharg claim stays false; the IRGC "two mines" claim is CENTCOM-denied. Your energy legs are on the right side; **no new energy arm** — BRENT reads this as the same event class re-clearing, and the 8/7 retirement stands.
- **Rates:** the 10-year at 4.75% is the window HIGH — the TLT-put exit counter is 0-of-5 and 25bp away; the real-yield add-gate is 6bp away and still NO-ADD. HY spreads 263bp, back off the 260 line; the two-close registry kill is now THE kill and every other count is an observable [row 106 done].
- **Your queue is under its cap for the first time since 8/23** — 26 rulings landed in two words on 9/1; fifteen desks have their ruling packets. What remains: CARL's DR-1 aggregation input [104] before 9/10, the hygiene carry [133], the FFIEC export [98], oil exit levels [74] on delivery, and the November credential sitting [31]. **LABOR has not been summoned** (ISM 54.6; JOLTS and the OPM rule land 9/2).
- **BCRED's tender result lands on EDGAR between 9/2 and 9/8** — BROCK gets one touch when it lands, not before; the "$1.7B net outflows" figure circulating is the Q1-era print, not a tender result.
- **Housekeeping you ruled 9/1:** root Git Protocol gained item 4c (a pathspec-less commit sweeps the shared index — cold-read verified) · the prediction canon gained the re-mark scoring rule and three registration rules (airtight branch sets, frozen contract + value + date, exact locator) · the registration-join rule now sits in the fire-ledger header · NEXUS's twelfth amendment is adopted with a cap and its watch graded missed · OSPREY's OSP-05 is FAILED on the operative test.
- **Housekeeping, earlier:** the 8/31 items (Kharg fabrication caught, MIDAS-06 graded (a), HOM-01 missed, IQHQ swept empty, HEARTBEAT re-based) are in the 8/31 entry; HEARTBEAT is now at 98.6% of its cap and its next touch is a structural split.

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
