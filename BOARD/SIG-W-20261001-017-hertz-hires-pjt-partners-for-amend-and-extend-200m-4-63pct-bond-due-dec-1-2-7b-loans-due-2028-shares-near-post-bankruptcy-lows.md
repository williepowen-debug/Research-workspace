---
signal_id: SIG-W-20261001-017
date: 2026-10-01
timestamp: 2026-10-01T16:49:35Z
time_dispatched: 2026-10-01T16:49:35Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~16:47Z (msgs 4815-4822), batch manifest BM-20261001-03
origin: ["Will Telegram photos (msgs 4818, 4819): Bloomberg article text, Hertz Taps PJT Partners to Extend Debt as Maturities Loom (people familiar; Hertz and PJT declined comment); shares $1.68 Wednesday 9/30", "WALTER fetch.py: HTZ $1.75 (+4.5%) 10/01 intraday"]
domain: FUNDING_LIQUIDITY
cluster: CONSUMER_STAGFLATION
entities: ["Hertz Global Holdings (HTZ)", "PJT Partners", "amend-and-extend"]
confidence: 0.75
confidence_language: "Bloomberg, people familiar, read from Will's screenshot of the article text; WALTER could not retrieve the article itself. Share price cross-checked live."
signal_type: pattern-match
safety_net: clear
verdict: "Hertz is working with PJT Partners on an amend-and-extend of its debt; PJT has approached some creditors over recent weeks (Bloomberg, people familiar; both declined comment). Near-term stack: a $200M 4.63% bond due Dec 1, 2026 and $2.7B of loans due 2028. Hertz reported ~$1B liquidity in August, enough for the December bond. Shares $1.68 on 9/30, near lows since the 2021 relisting ($1.75, +4.5%, 10/01 intraday)."
precedence: PRIORITY
action: []
info: ["LIQUID", "BROCK", "CARL", "SHADE"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~16:47Z (msgs 4815-4822), batch manifest BM-20261001-03, item 5 (images 5 and 6). 'Already ours?' No Hertz signal on BOARD in September. FUNDING_LIQUIDITY HY issuer-level distress: LIQUID info (an issuer-level single-B/CCC data point inside LIQ-07's spreading window, -005), BROCK and SHADE info per row defaults, CARL info (rental-fleet disposals feed used-car prices). An A&E is a distressed-exchange precursor, not a default. No ask."
---

# Hertz has hired PJT Partners to extend its debt (Bloomberg). A $200M bond is due December 1; shares are near post-bankruptcy lows.

- **Bloomberg (people familiar):** Hertz is working with **PJT Partners** on an **amend-and-extend**; PJT has been contacting some debt investors over recent weeks. Hertz and PJT declined comment.
- **Maturities:** **$200M 4.63% bond due Dec 1, 2026** · **$2.7B loans due 2028**.
- **Liquidity:** ~$1B reported in August, enough to meet the December bond. June: a $350M convertible paired with $100M of shares designed to be shorted.
- **Stock:** $1.68 on 9/30, near its lows since the 2021 relisting; $1.75 (+4.5%) on 10/01 (WALTER pull).

**So what:** a large high-yield issuer is lining up to push out its maturities. That is the issuer-level version of what LIQUID's "stress spreading" test just picked up in single-B and CCC spreads (`-005`). **An A&E is not a default,** but it often precedes a distressed exchange.

## Caveats
- One wire, unnamed sources, read from a screenshot of the article text.
- Liquidity covers the December bond on Hertz's own August figures.

Info only.
