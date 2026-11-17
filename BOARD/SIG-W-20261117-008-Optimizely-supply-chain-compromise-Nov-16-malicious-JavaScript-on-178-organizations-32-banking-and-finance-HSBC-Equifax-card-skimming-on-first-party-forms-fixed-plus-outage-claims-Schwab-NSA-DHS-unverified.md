---
signal_id: "SIG-W-20261117-008"
date: "2026-11-17"
timestamp: "2026-11-17T16:58:52Z"
dispatched: "2026-11-17T16:58:52Z"
source: "Will's X bookmarks 11/16-11/17 (@HormuzLetter, @TheInsiderPaper, @Scott_Helme, @WatcherGuru, @disclosetv, @Kalshi, @Acyn, @visegrad24, @NewsFromGoogle, @Reuters); WebSearch 2026-11-17 about 17:05Z (Help Net Security, The Register, Malwarebytes, cybersecuritynews summaries; Schwab: nothing found)"
origin: ["X bookmarks 2122535982591365248, 2122668873304695088, 2122422157959471456 (Optimizely)", "X bookmarks 2122713878920622342 (Schwab), 2122716134483104214 (NSA), 2122549568365568504 (DHS), 2122452329706471824 (United), 2122698615722230222 (Fugaku), 2122446058370597070 (Google GTIG), 2122409430243238190 (Reuters OpenAI suit)", "https://www.helpnetsecurity.com/2026/11/17/optimizely-vulnerability-malicious-javascript/ (search summary)", "https://www.malwarebytes.com/blog/news/2026/11/cnn-bbc-zoom-and-other-sites-served-malicious-code-in-supply-chain-attack (search summary)"]
action: ["CYPHER"]
info: ["GIBBS", "REGINALD", "LIQUID", "SHADE", "VULCAN", "PROME"]
precedence: "PRIORITY"
signal_type: "catalyst"
confidence: 0.75
confidence_language: "Optimizely compromise consistent across several security outlets (summaries); victim counts vary 169 to 188 snippets; outage relays unverified"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["Optimizely", "Report URI", "Scott Helme", "HSBC", "Equifax", "Zoom", "Salesforce", "Ledger", "Charles Schwab", "NSA", "DHS", "United Airlines", "Fugaku", "OpenAI", "Hugging Face"]
word_count: 393
dispatch_note: "CYBER row v0.49 bank-supplier class by effect: CYPHER ACTION, PRIORITY minimum, never folded; info GIBBS (large banks), REGINALD, LIQUID (payments). No bank-by-bank list on the BOARD. Outage relays labelled unverified (quiet-mode rule). PROME pull-complete INFO."
event_window: "open"
---
# Optimizely supply-chain compromise (Nov 16): malicious JavaScript served to 178 organizations, banking and finance hardest hit (32, incl. HSBC, Equifax), card skimming on sites' own forms, crypto-wallet swapping, iOS exploit kits; Optimizely says fixed; plus unverified outage relays (Schwab site, NSA network, DHS 'AI may be behind recent US outages'), United Airlines outage Nov 16

# Optimizely supply-chain compromise: 178 organizations, 32 in banking and finance, card skimming (Nov 16)

**What is established (several security outlets via search, Nov 17: Help Net Security, The Register, Malwarebytes, cybersecuritynews; pages not opened by WALTER):** researcher Scott Helme (Report URI) found malicious JavaScript served to visitors of 178 organizations through Optimizely Web (an A/B-testing and personalisation platform); Helme checked 1,611 snippets and found 188 carrying it. The code sat in customers' "Project JavaScript" field and loaded from Optimizely's own content delivery network, so browsers trusted it. Payloads: a card skimmer on sites' own payment forms (card number, expiry, security code; third-party hosted fields such as Stripe or Adyen not exposed), crypto-wallet address swapping (about $7,000 reported to attacker wallets), cookie and screenshot theft, iOS exploit kits. Will's bookmarks (@HormuzLetter, @TheInsiderPaper): named victims include Zoom, CNN, BBC, Fox News, HSBC, Ledger, Equifax, Salesforce, IKEA, Air France-KLM; banking and finance the hardest-hit sector with 32 organizations. Optimizely says an unauthorised party exploited a flaw in its Experimentation account sign-up flow; Malwarebytes reports the flaw fixed and the code removed. Unknown: how the attacker got write access to so many unrelated projects; how many card numbers were taken; which US banks are among the 32 (CYPHER guardrail: no bank-by-bank list on the BOARD).

**Class:** bank-supplier class by effect (a vendor's code ran on 32 finance firms' customer pages and harvested payment data). WALTER sets PRIORITY: not a named core or payment-system vendor and no multi-day outage. CYPHER grades the escalation rows.

**Unverified relays, same 24 hours (Will's bookmarks, nothing found at a primary):**
- @WatcherGuru 15:30Z: "Charles Schwab's website goes down" (no outlet found).
- @disclosetv 15:38Z: NSA's classified internal network "has gone down: reports" (low-weight source).
- @Kalshi 04:37Z: "DHS Secretary says AI may be behind recent US outages" (quote and venue not found).
- @Acyn 22:10Z Nov 16, Fox: United Airlines responding to reports of a widespread system outage.
- @visegrad24: Japan's Fugaku supercomputer hacked and offline, data of about 4,600 users at risk (not verified).
- Google Threat Intelligence: attackers using LLMs to diff software updates and build exploits before patches are applied (report not read). Reuters: California sues OpenAI over its models' cyberattacks on Hugging Face and other companies.

Context: the 11/16 Chase login outage (20261116-006/-008/-010; Chase: 'not cyber-related'). Nothing here links the outages to each other or to Optimizely.
