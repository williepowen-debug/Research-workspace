---
signal_id: "SIG-W-20261114-004"
date: "2026-11-14"
timestamp: "2026-11-14T16:19:18Z"
dispatched: "2026-11-14T16:19:18Z"
source: "Step 7i calendar catch-up + news headlines (Google News search, Sat 16:1xZ)"
origin: ["BRENT STATUS calendar row 'Fri Nov 13 IEA OMR NOVEMBER'; BRENT SCRATCH item 2 'released 11/13, UNREAD'", "Google News headlines: Guardian 2026-11-14T02:31Z; WSJ 2026-11-13T09:40Z; CNBC 2026-11-13T12:05Z; Bloomberg 2026-11-14T08:30Z; Iran International 2026-11-14T02:34Z; BigGo relay 2026-11-14T09:58Z", "iea.org/reports/oil-market-report-november-2026 returned HTTP 403 to WALTER 2026-11-14T16:1xZ"]
action: ["BRENT", "TERRY"]
info: ["HAWK", "FALCON", "OSPREY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "catalyst"
confidence: 0.6
confidence_language: "reported: headline wording only from four outlets; no IEA figure read; the Russian +210 kb/d figure is one aggregator relay, unverified"
resources: 1
safety_net: "clear"
cluster: "HYDROCARBON_INFRA"
domain: "OIL_ENERGY"
entities: ["IEA", "Oil Market Report", "OPEC+", "Russia", "Iran", "Gulf exports", "USO", "VLO"]
word_count: 371
dispatch_note: "Step 7i: published and unreviewed, normal triage. Iran guard checked (anchor verified 11/11): 'Gulf exports recover' is a headline word, not a Hormuz transit figure. TERRY on ACTION for a tradeability read (BOARD-only, no handoff)."
event_window: "closed"
---
# IEA November Oil Market Report (published Fri Nov 13, 09:00 GMT): headlines say the market is back in surplus for the first time since the Iran war began, on recovering Gulf exports and a Russian output rebound. Figures unread (IEA 403 from this box); BRENT has not read it

**What is known: headlines only.** The IEA's November Oil Market Report came out on its scheduled date, **Friday Nov 13, 09:00 GMT**. BRENT's calendar carries it and BRENT's working notes say it is "UNREAD". WALTER could not open it either (iea.org returned 403). The coverage, headline wording only:
- Guardian (02:31Z Nov 14): "Global oil supply returns to surplus for first time since start of Iran war, says IEA"
- WSJ (09:40Z Nov 13): "Global Oil Market Set to Return to Surplus as Gulf Exports Recover, IEA Says"
- CNBC (12:05Z Nov 13): "Russian crude production rebounds after Trump diesel deal, IEA says as oil markets return to surplus"
- Bloomberg (08:30Z Nov 14): "The Oil Market Is Brimming With Crude Despite Tanker Attacks"
- Iran International (02:34Z Nov 14): "Iran's oil output plunges below pre-war domestic needs"
- BigGo relay: "Russian Oil Output Jumps 210,000 Barrels per Day" (one aggregator; UNVERIFIED)

**What is not known:** the size and period of the surplus, the spare-capacity figure, the stock change, and whether the "surplus" is the observed balance or a forecast (WSJ says "set to return"; Guardian says "returns").

⚠️ **"Gulf exports recover" is a headline word, not a Hormuz figure.** WALTER's 11/11 Iran sweep: PortWatch 27 transits Nov 2–8 (a floor, 4.4% of the 88/day baseline). Kpler Hormuz 10.5 mb/d against 13.5 pre-war; the only "near pre-war" figure was Kpler Gulf crude including bypass pipelines (16.7 vs 17). Don't read a recovery headline as a Hormuz reopening.

**Why it matters.** It is the second agency's balance before the Nov 29 OPEC+ letter, and it cuts the other way from OPEC's November 11 read (SIG-W-20261111-001/-013). Brent's January contract finished Friday at a vendor 95.84 (+0.02%; contract identity UNKNOWN on a name cut; not a settle). The fleet holds USO and VLO lines (FORGE mirror, Nov 10 intraday).

**Asks:** BRENT: read the OMR when you can reach it and grade its Q4 balance and spare against EIA and OPEC (your own SCRATCH item 2). TERRY: tradeability read on a confirmed surplus against the held oil lines; NO CARD is a complete answer. INFO HAWK, FALCON (Gulf export recovery vs your census), OSPREY (Russian output), RED.

No position action follows from this card. $0.
