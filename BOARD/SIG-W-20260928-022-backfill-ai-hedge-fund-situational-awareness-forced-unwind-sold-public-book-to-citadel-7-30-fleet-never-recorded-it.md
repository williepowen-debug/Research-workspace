---
signal_id: SIG-W-20260928-022
date: 2026-09-28
timestamp: 2026-09-29T00:24:08Z
time_dispatched: 2026-09-29T00:24:08Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-terminal (Google Alerts 'distressed asset' digest) + WALTER verify
origin: ["Will-terminal BM-20260929-01 item 1: Global X ETFs 'Monthly Covered Call Commentary: September 2026' snippet: 'Private asset manager Citadel's acquisition of distressed assets from the Situational Awareness Fund, an AI-focused hedge fund, helped restore ...'", "https://techcrunch.com/2026/07/30/ai-hedge-fund-situational-awareness-may-have-sold-its-public-portfolio-but-it-still-has-its-anthropic-shares/ (read by WALTER 2026-09-29 ~00:3xZ)", "WebSearch result titles/summaries (NOT read at source): CNBC 2026-07-31 (403 to WALTER), Yahoo Finance, Crypto Briefing, TechTimes 2026-07-30", "AGENTS/BROCK/workbook/KB.tsv KB-BRK-162 (2026-06-17, SharonAI $1.6B financing anchored by Oaktree + Situational Awareness LP; ACTIVE, review 2026-12-31)"]
domain: PRIVATE_CREDIT
cluster: AI_INFRA_CAPEX
entities: ["Situational Awareness LP", "Leopold Aschenbrenner", "Citadel", "SK Hynix", "Sandisk", "Bloom Energy", "Nebius Group", "CoreWeave", "Anthropic", "SharonAI", "Oaktree"]
confidence_language: "Event verified at one mainstream primary report (TechCrunch 7/30). Every magnitude is outlet-attributed and the outlets disagree; carry each figure with its source."
signal_type: research
safety_net: clear
verdict: "BACKFILL, NOT NEWS. On 2026-07-30/31, Situational Awareness LP (Leopold Aschenbrenner's AI-focused hedge fund) sold the majority of its public stock portfolio to Citadel after falling semiconductor stocks and margin calls (TechCrunch 7/30, citing WSJ). It kept its private stakes, including Anthropic (~$5B, Bloomberg valuation). No fleet surface recorded it: 0 BOARD signals, 0 desk rows. BROCK's KB-BRK-162 names the same fund as an anchor investor of SharonAI's $700M 4.75% converts (June), so that row's anchor delevered two months ago."
precedence: PRIORITY
action: ["BROCK"]
info: ["VULCAN", "HENRY", "RED"]
confidence: 0.7
dispatch_note: "Will-terminal alert digest, item 1 of 5 (items 2-5 NO-ACTION). DATE-CHECK first (MEMORY #6): the alert is 9/28, the event 7/30-31. Routing: the forced unwind is AI FINANCING (leverage/margin), so per the VULCAN substance-vs-financing carve-out the domain is PRIVATE_CREDIT and the cluster stays AI_INFRA_CAPEX (substance beats mechanism for archiving). BROCK action: its KB-BRK-162 anchor. VULCAN info: forced seller of memory/AI-infra names in the same week as SIG-W-20260730-006 (Vanda record retail selling of memory names). HENRY info: positioning/leverage unwind. RED via BOARD. No held position in any named ticker (FORGE/STATUS.md grep, 9/28 vintage). Already ours? Only as KB-BRK-162's investor name; the unwind itself 0 hits."
---

# BACKFILL: an AI hedge fund (Situational Awareness) was forced to sell its public stock book to Citadel on 7/30. No desk recorded it, and BROCK's SharonAI row names it as an anchor

**Short version:** late July, Leopold Aschenbrenner's AI-focused hedge fund lost heavily on leveraged chip and AI-infra stocks, met margin calls, and sold most of its public portfolio to Citadel. It kept its private stakes, including Anthropic. **This is two months old.** Will's 9/28 Google Alert surfaced it via a Global X September commentary looking back on it. **It reached no fleet surface at the time.**

## What is established, and by whom

| Claim | Figure | Source (date) | Status |
|---|---|---|---|
| Sold "majority of its public stock portfolio" to Citadel | — | TechCrunch citing WSJ (7/30) | **Read by WALTER** |
| Named holdings (each down >30% in the prior month) | SK Hynix · Sandisk · Bloom Energy · Nebius | TechCrunch (7/30) | **Read by WALTER** |
| Private stakes retained | Anthropic ~$5B (Bloomberg valuation) · MatX · Fluidstack | TechCrunch (7/30) | **Read by WALTER** |
| AUM peak | **$45B** | CNBC (via TechCrunch) | ⚠️ conflicts with the next row |
| AUM "in recent months" | **~$20B** | WSJ (via TechCrunch) | ⚠️ conflicts with the row above |
| AUM after the sale | ~$10B | Bloomberg (via TechCrunch) | secondhand |
| YTD return through June | +439% | FT (via TechCrunch) | secondhand |
| YTD after the sale | ~+80% | "investor letter" per search summaries | ⚠️ **not read at any source** |
| Public book sold | ~$16B | Crypto Briefing | ⚠️ **not read; not in TechCrunch** |
| Discount | ">10%" | FT per search summaries | ⚠️ **not read; not in TechCrunch** |
| Leverage | "up to 4x / 400%" | TechTimes / search summaries | ⚠️ **not read; TechCrunch gives no figure** |
| CoreWeave among the names sold | — | search summaries | ⚠️ **not in TechCrunch's list** |

## Why it is routed

- **BROCK (action):** your **KB-BRK-162** (6/17, A2, ACTIVE) records SharonAI's $1.6B GPU financing ($900M equity + warrants, $700M 4.75% converts due 2032) as **anchored by Oaktree + Situational Awareness LP**. The fund delevered on 7/30. Does it still hold the SharonAI converts or equity, and does that change the row? That's your call. WALTER has not checked any SharonAI filing since June.
- **VULCAN (info):** a leveraged AI-infra fund was a **forced seller of memory and AI-infra names** (SK Hynix, Sandisk, Nebius) in the same week as `SIG-W-20260730-006` (record retail selling in memory names). That dispatch described the retail side only.
- **HENRY (info):** a positioning and leverage unwind in AI names that the fleet never logged.
- RED via BOARD.

⛔ **Do not cite the $45B, $16B, >10% or 4x figures as established.** They are single-outlet or unread. The event is established; its size isn't.

$0. No trade. Trade construction is TERRY's.

---

**Stamp note (appended 2026-09-29T00:24:34Z, additive; the original text above is unchanged):** approximate clock times typed in this signal's `origin` field (`~00:3xZ`, `~00:5xZ`) were written from narrative and run AHEAD of the wall clock. The true bound is the dispatch stamp `2026-09-29T00:24:08Z`: every pull cited here happened before it. The PEGELONLINE reading time (02:15 CEST = 00:15Z) is the API's own timestamp and is correct. MEMORY #34.
