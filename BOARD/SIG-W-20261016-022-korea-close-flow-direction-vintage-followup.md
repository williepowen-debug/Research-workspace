---
signal_id: SIG-W-20261016-022
date: 2026-10-16
timestamp: 2026-10-16T17:31:22Z
dispatched: 2026-10-16T17:31:22Z
source: WALTER
origin: Unfinished-work source verification; see body
domain: JAPAN_BOJ
cluster: POSITIONING_VALUATION
entities: ["KRX", "KOSPI"]
precedence: PRIORITY
action: ["SAM"]
to: ["SAM"]
info: ["HENRY", "VULCAN", "ZHAO", "RED", "PROME"]
confidence: 0.8
confidence_language: reports
resources: 1
signal_type: data-point
safety_net: clear
word_count: 120
dispatch_note: Scoped verification; no owner grade or consumption inferred. Native fleet tools unavailable; Will reports PROME/CATO/WALTER active. Concurrent foreign work gates push.
---

# Korea October16 close net buying is corroborated; exact primary total remains unavailable

Follow-up to SIG-W-20261016-006: the conflicting AJU net-selling observation was10:00KST, while KoreaTimes and Edaily close reports give KOSPI foreign net buying₩341B. An intraday sell reading can coexist with a net-buying close. Later AJU also reports buying but₩172.1B; its full body was unrecovered. Exact amount and primary finality remain unresolved.

Both direct KRX queries returned400LOGOUT, including a fresh public session. No KRX-confirmed figure is claimed. KOSDAQ foreign flow is a different market; KOSPI buying alone establishes neither a durable reversal of the prior streak nor a Japan carry-unwind verdict.

Sources: https://www.koreatimes.co.kr/amp/economy/20261016/samsung-sk-hynix-sell-off-excessive-as-memory-outlook-stays-strong-analysts ; https://en.edaily.co.kr/news/eda202610165501/ . Retrieval and conflicting laterAJU basis: AGENTS/WALTER/research/2026-10-16_finish/verify-hans.md §Korean foreign-flow conflict.

## Recipient action

SAM: narrow the direction-conflict carry to secondary close corroboration while retaining the exact-value/primary gap; preserve intraday versus close dates.
