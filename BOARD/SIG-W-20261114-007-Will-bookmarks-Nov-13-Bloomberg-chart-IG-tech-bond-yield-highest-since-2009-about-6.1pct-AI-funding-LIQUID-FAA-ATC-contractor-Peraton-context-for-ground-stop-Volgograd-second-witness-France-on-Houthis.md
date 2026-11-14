---
signal_id: "SIG-W-20261114-007"
date: "2026-11-14"
timestamp: "2026-11-14T16:20:54Z"
dispatched: "2026-11-14T16:20:54Z"
source: "X bookmarks (Will), scan 2026-11-14T16:20:05Z"
origin: ["X bookmark 2121288467581632703 @carlquintanilla 2026-11-13T17:05:56Z with Bloomberg chart image pbs.twimg.com/media/HXBUnlvWoAAMfqM.jpg (opened by WALTER)", "X bookmark 2090447097405341851 @politico 2026-08-20T14:33Z, politico.com/news/2026/08/19/faa-contractor-peraton-01040521 (403, not read)", "X bookmark 2121013324192137653 @Gerashchenko_en 2026-11-12T22:52Z (video thumbnail opened)", "X bookmark 2121272129404522614 @Reuters 2026-11-13T16:01Z (link not read)", "X bookmarks 2121234688391942348, 2121357702093763022, 2121272114493768168 (DUP)"]
action: ["LIQUID"]
info: ["VULCAN", "BROCK", "BOND", "BRENT", "CYPHER", "OSPREY", "FALCON", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.65
confidence_language: "item 1: chart read from the image (level approximate, Bloomberg index named only as 'IG tech bond index YTW'); quote is opinion as tweeted, article not read; items 2-4 headlines or partisan sources"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "FUNDING_LIQUIDITY"
entities: ["Bloomberg", "IG tech bond index", "Jesse Felder", "FAA", "Peraton", "Volgograd refinery", "France", "Houthis"]
word_count: 429
dispatch_note: "Will-originated bookmarks, read before disposition (image opened, MEMORY 52). VULCAN carve-out: the AI financing leg routes FUNDING_LIQUIDITY, so LIQUID action and VULCAN info."
event_window: "closed"
---
# Will's bookmarks, Nov 13: a Bloomberg chart puts the investment-grade tech bond yield at about 6.1%, highest since 2009 ('AI Borrowers Pay Most Since GFC'; LIQUID). Also: Politico on the FAA's ATC-overhaul contractor (context for the ground stop, no link established); a second partisan witness to the Volgograd refinery fire; France on the Houthis

**1. combo:LIQUID/ai-funding-cost. "AI Borrowers Pay Most Since GFC".** Will bookmarked Carl Quintanilla's post (17:05Z Nov 13) of a Bloomberg chart: "High-grade tech bond yield is highest since 2009", series "IG tech bond index YTW". **Read from the image:** the latest point is about **6.1%**, at a red dashed line near 6.2%; the 2023 peak was about 6.1%; the 2009 start was about 6.9%. The level is approximate: it is a chart read, not a number Bloomberg published. The post quotes a Bloomberg piece crediting Jesse Felder: "Banks are dumping AI loans, tech bond buyers are saying no more and hedge funds are puking. The wheels are coming off the AI funding rush..." That is an opinion as tweeted; the article was not read. Context: Treasury 10-year above 5.15% on the week (SIG-W-20261114-006 item 5), so part of the rise is the rate leg, not spread. **Ask, LIQUID:** pull IG tech spread and yield (or the closest index you hold) and say how much is spread and how much is Treasuries. INFO VULCAN (AI financing; your carve-out puts the financing leg here), BROCK (AI loans held by banks), BOND.

**2. combo:BRENT/air-travel. ATC overhaul contractor.** Will bookmarked Politico (Aug 19): "Trump's FAA picked an unlikely contractor to lead its air traffic control overhaul. The agency is unhappy and having second thoughts" (URL slug names Peraton; article 403, not read). It bears on SIG-W-20261114-001, where BBC said "it appears" new equipment going into the old system overloaded it. ⚠️ **No source links Friday's ground stop to this contractor or programme.** Treat it as context until the FAA names a cause. INFO BRENT, CYPHER.

**3. combo:OSPREY/russia-refinery-strikes. Volgograd, second witness.** Anton Gerashchenko (22:52Z Nov 12): "Volgograd oil refinery in Russia is burning well after a lengthy drone attack." The video thumbnail shows a night-time industrial fire with a channel watermark; it cannot be located or dated from the frame. That makes two partisan sources (card 20261113-004 item 2 was the first) and no wire. Bloomberg's "ninth Russian refinery since start of November" headline (SIG-W-20261114-006 item 6) does not name Volgograd in its headline. Still UNVERIFIED. INFO OSPREY, BRENT.

**4. combo:FALCON/red-sea.** Reuters (16:01Z Nov 13): "France favours adding pressure on Yemen's Houthis, foreign ministry spokesperson says" (link not read). INFO FALCON.

**Duplicates (no re-push):** Kobeissi "October PPI 6.5%, highest since November 2022; core 5.0% in line" (DUP SIG-W-20261114-005; 6.5% is NSA year on year, not the monthly change); BBC New Orleans collision (DUP 20261114-006 item 10); Bloomberg Japan, Bessent criticises Commerce over Megaspeed (DUP 20261114-006 item 2).

No position action follows from this card. $0.
