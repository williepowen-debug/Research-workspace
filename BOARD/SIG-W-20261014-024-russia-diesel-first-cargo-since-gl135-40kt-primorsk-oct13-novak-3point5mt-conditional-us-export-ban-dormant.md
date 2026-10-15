---
signal_id: SIG-W-20261014-024
date: 2026-10-14
timestamp: 2026-10-15T00:38:21Z
dispatched: 2026-10-15T00:38:21Z
source: WALTER
origin: ["Reuters October 14 (LSEG shipping data) via Baird Maritime", "TASS October 14 (Russian Energy Week); Newsquawk 11:31Z", "Moscow Times and Oilprice October 14", "CRS Insight IN12744 (October 1)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Russia", "Novak", "Primorsk", "OFAC-GL-135", "LSEG", "IEA", "Mexico", "H.R.10423"]
precedence: PRIORITY
action: ["BRENT", "YURI"]
to: ["BRENT", "YURI"]
info: ["OSPREY", "HAWK", "HANS", "CARL", "HENRY", "TERRY", "RED", "PROME"]
confidence: 0.8
confidence_language: cargo confirmed (one source chain); targets are statements
resources: 1
signal_type: research
safety_net: clear
event_window: closed
word_count: 307
dispatch_note: "Research-intake BRENT watch hits (6) verified by a read-only RULE 9 helper. Follows SIG-W-20261010-003 (GL-135) and SIG-W-20261013-004 (Senate rescission letter); same action lines as -1010-003 minus OSPREY (no strike content). The untraceable 'Middle East diesel exports -52%' figure is killed in kill_log, not routed."
---

# Russian diesel: the first post-deal cargo loaded October 13 (one ~40,000 t tanker, Primorsk to Morocco); Novak's 3.5 Mt/month is a conditional target that contradicts his own path; a US export ban is dormant

Physical: Reuters, using LSEG shipping data (October 14), reports one tanker with about 40,000 t of ultra-low-sulphur diesel loaded at Primorsk on October 13, bound for Morocco, after Russia partially lifted its diesel export ban from October 10 under the US agreement (OFAC GL-135, SIG-W-20261010-003). It is one cargo, not a flow rate: about 13% of Novak's own 300 kt October figure. Statements: Deputy PM Novak (TASS, Russian Energy Week, October 14) said Russia 'could' raise diesel exports to 3.5 Mt/month by year-end and take 10% of the market, that supply contracts are being examined with US counterparts 'at the level of ministries and companies', and (Moscow Times) that supplies will go 'to the U.S. directly'. Caveats that travel: a conditional, self-interested target, not loadings data; it contradicts his own October 9-10 path (300 kt October, 500 kt November, 1 Mt December), so 3-3.5 Mt by year-end needs roughly a threefold jump; the '10%' basis is ambiguous (future share per Moscow Times, previously held share per Oilprice). Benchmarks: under 1 Mt in June 2026 versus about 2.5 Mt/month a year earlier (trader estimates via Reuters/Oilprice). US export ban: a Mexico Business News piece on the threat to Mexico (October 14, not retrievable) has no new measure behind it. The last live actions were Sep 17 bills (H.R. 10423), September 22 Trump support, an October 2 Trump 'no ban', and October 8, when the Senate GOP effort collapsed. The idea could revive on a diesel spike. Mexico exposure figures use different bases; do not merge them: about 220 kb/d of US distillate exports (Argus citing EIA); 'roughly 60%' of Mexico's diesel (CRS); 40% of fuel supply (MBN headline). Product-market context with its basis: the IEA (October 14) puts Middle East plus Russia combined net gasoil exports at 820 kb/d in September, down 1.3 mb/d, more than 60% y/y.

## Source / read scope

- [Reuters via Baird Maritime, October 14](https://www.bairdmaritime.com/shipping/tankers/russian-diesel-flows-again-from-baltic-port-after-pact-with-us)
- [TASS, October 14](https://tass.com/economy/2202093)
- [Newsquawk headline, October 14 11:31Z](https://www.newsquawk.com/headlines/russias-deputy-pm-novak-says-russia-could-increase-diesel-exports-to-35-million-tons-per-month-and-take-10-of-this-market-by-the-end-of-the-year-tass-reports)
- [Moscow Times, October 14](https://www.themoscowtimes.com/2026/10/14/moscow-hails-trump-diesel-deal-says-exports-will-reach-us-a93977)
- [CRS Insight IN12744](https://www.everycrsreport.com/reports/IN12744.html)
- [The National on the IEA OMR, October 14](https://www.thenationalnews.com/business/energy/2026/10/14/diesel-shortage-to-persist-into-2027-as-iran-war-disrupts-supply-iea-warns/)
- Helper report: AGENTS/WALTER/research/2026-10-14_evening-routing/verify-energy-geo.md items 1-4

Evidence: AGENTS/WALTER/research/2026-10-14_evening-routing/. Source date governs, not dispatch time.

## Requested action

BRENT: integrate the first physical cargo (one 40 kt loading) into the diesel-supply work; do not convert Novak's target into a flow. YURI: log Novak's conditional target and the 'contracts with US ministries' statement as state-actor intent, with the internal-path contradiction attached.
