# HANDBOOK.md — the hand-written half of **THE HELM** (Will's page; renamed from "Operator Handbook" on his word 8/21 — repo filename kept to avoid reference churn)

**Owner:** PROME. Rendered by `PROME/tools/will_handbook.py` (regenerated at Standard+ closeouts alongside the brief and dashboard). The live sections on the page — Waiting on you · The clock — are GENERATED from WILL_QUEUE/DOCKET via the brief's own parsers and are never written here. **This file is the manual + the curated priorities. Plain language; every claim dated; update when a convention changes, not per-session.**

## Top priorities
- **★ TWO FACTS ARE YOURS, still owed after five asks: the USO $135 call's sale price, and whether the $4.40 GTC sell on the December WAL put is resting in ROBINHOOD.** Both fills stand on the trade desk's cards on your word [9/2 14:21]; the broker mirror is stale for both until the next export.
- **★ 🔴 PJM IS IN A LIVE CAPACITY EMERGENCY, THIRD DAY [WATT 9/3 07:27]:** emergency alerts 9/1 · 9/2 · 9/3, demand reduction dispatched in five zones, a DOE §202(c) order through 9/8 authorising backup generation at LARGE LOADS, $1,869/MWh Tuesday evening. The power desk's band fired on every limb; the cascade has NOT tripped; no trade proposed. Any load shed or EEA-2/3 through 9/8 wakes the desk the same day.
- **★ TWO CARRIED FIGURES DIED AT PRIMARIES [9/2–9/3]:** the "$160B+ MF maturity wall, +50%" has no primary and the industry survey says total maturities are DOWN 9% with multifamily the least pressured type (HOMER) · the three-way Florida price conflict never existed — the index cited excludes condos by construction (CORAL). The Florida seller-index breadth broke 3-of-5; the stand-down needs a second reading ≥9/13.
- **★ THE MARKET LINE:** high-yield 265 [9/1], five off the kill and moving away · office CMBS delinquency 12.00 vs a "> 12" bar, NOT FIRED [CREED, Trepp Aug] · the 30-year JGB auction SOFT on a 2.1bp tail, Japan's letter NO-VERDICT as pre-registered [SAM] · USD/JPY 156.14 live, −2.5% in two sessions, no confirmed op [SAM 9/3].
- **★ Your rulings this morning are executed:** 159 (T-03 stands — it fires on a flat print Friday) · 163 item 1 (NEXUS's file is a whole boot read; one breach; cure = split plus re-homing) · 151 (the auto-credit "sustained" wording, persistence reading) · 164 (the cruise fuel ladder retired).
- **Your queue by date:** 157 leg ① (by 9/8) · 163 items 3/4/⑤ (by 9/10) · 161 (9/15) · 160 (9/29) · 158 (held on BROCK) · 133 · 98 · 74 · 31. **Owed by hand:** the two facts above + the expired Robinhood QQQ put's disposition.
- **Structural, mine not yours, dated:** WQ-150 root carve-out edit ~9/8 · the fire-ledger at 187% of cap (a design, not an edit) · the DOCKET backlog of ~30 covered-but-unresolved August rows · the cold memory-index shard · a trading-calendar gap check for the price feed. **Owed to the book:** a trade-desk expiry pass for the 9/18 pair and the 9/30 cluster — nothing is pre-registered.
- **Rules that came out of the desks tonight:** a spawn brief quotes the registered row, never the desk's own summary (eight of thirteen briefs restated a stale gloss) · a relayed level travels with its UNIT or it does not travel (a tail in yen would have inverted a grade) · a gate base-rated on a RATE is silently falsified when the rate goes to zero (FERT) · a ruling that edits a charter sweeps the desk's state files too.

## Spawn queue
*(Format contract for the renderer: `- **NAME** · when · why` — one desk per line, decay order.)*
- **LABOR** · Thu 9/3 after 08:30 and 10:00, again after NFP Fri · re-ping to grade claims, ISM services and payrolls off its frozen cards; PROME never grades for it
- **HOMER + CREED** · Fri 9/4 · the $160B maturity wall retires (HOMER publishes; CREED attaches the primary or it dies)
- **CARL** · by Tue 9/8 · two open OTTO asks against its ≤9/10 V2 sitting (seasoning basis · deceleration vs turn), plus LABOR's answer and the Canada packet; OTTO's column landed 137/137
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
