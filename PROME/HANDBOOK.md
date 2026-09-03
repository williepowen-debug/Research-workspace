# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ TWO FACTS ARE YOURS, still owed after four asks: the USO $135 call's sale price, and whether the $4.40 GTC sell on the December WAL put is resting in ROBINHOOD.** Both fills are recorded on the trade desk's cards on your word [14:21]; the broker mirror says it is stale for both until the next export.
- **★ TWELVE DARK DESKS RAN TONIGHT ON YOUR WORD [19:37], ALL DELIVERED.** TERRY · BOND · BROCK · DEWEY · LABOR · HAWK · ZHAO · VIOLET · HENRY · NEXUS · LIQUID · OTTO — 320+ inbox items drained, seven files split under the read cap, nine letters frozen before their events, every commit verified on origin, $0 moved. Seven queue rows came out of it (157–163) and two operator facts went in.
- **★ THE MARKET LINE:** high-yield spreads set their 2026 low on 28 August EXACTLY on the sub-260 kill line, strict less-than, so nothing fired, and have widened to 265 since — while the CCC tail set four straight three-year highs underneath: bifurcation at a low, not repair [LIQUID 9/2]. The options gamma board flipped NEGATIVE inside a twelve-day unmeasured window (flip band 7,689–7,699, spot below, dealers amplify) [HENRY 9/2]. Ten-year 4.79% on the 1 September print, a window high; real yields 2.44%, add-gate still 6bp, NO-ADD.
- **★ INSTRUMENTS, NOT MARKETS, WERE TONIGHT'S FINDINGS:** the bond desk's kill leg fires on a quarter of auctions with no price separation [WQ-157] · the BCRED tender results have never ridden the filing the docket watched [BROCK] · the AI order book is TWO books, semis clean and power equipment failing the clean-book tests, with two commissioning claims unfound in any primary [DEWEY] · a missing 28 August bar in the free SKEW feed moved a live threshold distance and flipped a graded forecast [VIOLET/HENRY] · four of five credit gates name a series but not a vintage, one decisive at 0bp [WQ-162].
- **★ FRIDAY 08:30 — row 159:** a labor trigger fires on an UNCHANGED employment-population print because its three-month reference rolls forward. Rec: let it stand; it routes to two desks, it moves no capital, and retuning a frozen letter because you can see it coming is the class the discipline exists to stop.
- **Your queue by date:** 159 (Fri 08:30) · 157 leg ① + 158 (held on BROCK's denominator) + 162 dated leg (by 9/8) · 163 (by 9/10) · 161 (by 9/15) · 160 (by 9/29) · 151 (by 9/14) · 133 · 98 · 74 · 31.
- **Structural, mine not yours, dated:** WQ-150 root carve-out edit ~9/8 · three-outcome scoring spec ~9/9 · the cold memory-index shard · the fire-ledger at 187% of cap · BROCK/BRENT STATUS splits · six queue roll-offs · a trading-calendar gap check for the price feed.
- **Rules that came out of the desks' own cross-checks tonight (canon asks on 161/162; blueprint asks with DAEDALUS):** a file split is audited by OBLIGATION, never by bytes (two splits silently deleted owed actions while every byte check passed) · a correction is done only when every surface a reader actually opens carries it · a threshold letter pins a vintage for EVERY published observation it reads · route the second question to a desk with no stake in the answer.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **LABOR** · Thu 9/3 after 08:30 and 10:00, again after NFP Fri · re-ping to grade claims, ISM services and payrolls off its frozen cards; PROME never grades for it
- **HOMER + CREED** · Fri 9/4 · the $160B maturity wall retires (HOMER publishes; CREED attaches the primary or it dies)
- **CARL** · by Mon 9/8 · two open OTTO asks against its ≤9/10 V2 sitting (seasoning basis · deceleration vs turn), plus LABOR's answer and the Canada packet; OTTO's column landed 137/137
- **BROCK** · 9/3 → 9/4 → 9/8 · the BCRED tender re-checks at EDGAR on the corrected filing; sends the WQ-158 denominator
- **VULCAN + WATT** · this week · DEWEY's phantom-demand stubs; the unowned leading instrument (spot GPU rental prices) needs an owner
- **WAL** · this week · REG-15 has been its since 8/12 and nobody scores it; Q3 frame-before-filing deadline 10/13
- **DAEDALUS** · 9/3–9/5 · renderer window; five PROME packets waiting (grade→block hop · reader-traversal pattern · read-cap caveat · three mechanisms · the vintage sweep by a non-owner)
- **CORAL · OSPREY · MARCO · FERT · CRUISE · WALTER · RED** · dated per DOCKET · MSI review ~9/5 · HAWK's basis audit blocks OSPREY's band · Canada + HAWK-301 · ladder retirement 9/5 · lane-query rewrite + RED's 6b switch · FT-11 9/9 route

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
