---
signal_id: SIG-W-20260522-007
precedence: PRIORITY
timestamp: 2026-05-22T16:22:00Z
source: WALTER
origin: "Will Telegram 2026-05-22 16:09 UTC msg 1969 — X post (no attribution visible in image, data-rich) reporting March 2026 TIC data. Verify-research sub-agent agent_id aadb74c9243f5a818 — Treasury TIC primary ticdata.treasury.gov/Publish/mfhhis01.txt + Reuters coverage via US News money.usnews.com/investing/news/articles/2026-05-18/japan-china-lead-declines-in-foreign-holdings-of-treasuries-in-march-data-shows"

to: SAM (ACTION)
info: HENRY, CARL, ZHAO, RED, NEXUS, PROME

signal_type: data-release
confidence: 0.88
confidence_language: confirmed
resources: 0.04
safety_net: clear

word_count: ~350

cluster: FED_FRAMEWORK
cluster_secondary: ASIA_CHINA
signal_role: cluster_mediating
consumer_transmission: na
consumer_lens: na
event_window: closed

verify_research_verdict: CONFIRMED-WITH-CAUSALITY-FRAMING-CORRECTED 0.88. Treasury TIC March 2026 report (typically ~6wk lag, released mid-May per cycle) — numbers all check out: total foreign $9.348T (post $9.35T); Japan $1.192T -$47B (post $1.19T -$48B, close); China $652.3B -$41B (matches, lowest since Sep 2008 confirmed); UK $927B record (Reuters coverage doesn't confirm UK explicitly but TIC table 5 verifiable). **CORRECTED-FRAMING: BOJ-yen-intervention attribution is INFERRED, not primary.** Reuters attributes selling to US-Iran conflict start + oil-price-driven Asian-currency pressure, NOT specifically to BOJ funding yen intervention. BOJ-intervention mechanism plausible but Treasury TIC report doesn't assign causality.

mark_context: March 2026 TIC released mid-May (Treasury TIC reports run ~6wk lag). Dispatched ~4d after release. Numbers retrospective (March) but framing is forward-relevant in light of SIG-W-20260522-005 (Waller pivot same session) — foreign-bid weakening at same moment Fed pivots hawkish = UST term-premium pressure compounds.
---

# TIC March 2026: Foreign UST Holdings -$139B → $9.35T (Largest Monthly Decline Since Sep 2022) — Japan/China Lead Sellers, UK Counter at $927B Record (BOJ-Intervention Causality INFERRED)

**Primary release:** US Treasury TIC March 2026 report, released ~mid-May (~6wk lag). Total foreign holdings of US Treasuries declined **-$139B in March to $9.35T** — the largest monthly decline since September 2022.

## Verified Numbers (Treasury TIC Primary)

- **Total foreign:** $9.348T (post-cite $9.35T accurate)
- **Japan (#1 holder):** $1.192T, down ~$47B (post-cite $1.19T / -$48B — close)
- **China (#3 holder):** $652.3B, down -$41B — **lowest since September 2008**. China holdings now declined -$109B / -14% since start of 2025.
- **UK (#2 holder):** $927B record level, +$30B in March (Reuters coverage doesn't surface explicitly; TIC table 5 verifiable but not directly confirmed in retrieval)

## Causality Framing CORRECTED

**X-post claim:** "Bank of Japan sold US Treasuries to fund yen intervention."

**Reuters/primary read:** selling attributed to **US-Iran conflict start + oil-price-driven Asian-currency pressure**. The BOJ-intervention attribution is inferred by the post-author, not stated by Treasury TIC or Reuters coverage.

**Why this matters:** The BOJ-intervention causality is plausible (BOJ has been intervening in yen markets; selling foreign reserves is the funding mechanism) but it's a one-mechanism causal-claim layered on top of a multi-cause data print. The Iran-conflict + Asian-currency-pressure framing is broader and aligns with our existing BOARD substance:
- 5/4 Iran kinetic blockade onset (Hormuz closed, oil-price spike to ~$116)
- Asian-importer-currency pressure on JPY/KRW/INR all running through Q1
- BOJ's intervention is downstream of these conditions, not the primary causal driver

**Dispatch frames this as MULTI-CAUSE, with BOJ-intervention as ONE mechanism among several.**

## Why This Compounds With SIG-W-20260522-005 (Waller Pivot)

- Foreign bid weakening at the same moment Fed pivots hawkish = **UST term-premium pressure compounds**.
- Hawkish Fed + foreign-buyer-thinning = duration is exposed on both sides. Long-end UST yields likely face renewed upward pressure.
- HENRY positioning (vol/Fed-expectation channel) should weight this same direction.
- SAM has Japan-specific intelligence (BOJ posture, MOF intervention threshold) — action-recipient.

## Routing Discipline

- **SAM action:** owns Japan/BOJ + UST_FOREIGN composition. SAM has the institutional context to validate or refute the BOJ-intervention attribution against Japan's own MOF intervention disclosures.
- **HENRY info:** UST term-premium / vol implications.
- **CARL info:** broader Fed/rate-expectation context.
- **ZHAO info:** ASIA_CHINA cluster co-recipient (China -14% YTD-25 trend), even though ZHAO is STALE 51d (REQ-ZHAO-revival filed; CARL backup-promoted in REGISTRY).
- **RED:** counter-evidence for "structural-foreign-bid-thesis-intact" component.
- **cluster_mediating:** bridges FED_FRAMEWORK (UST plumbing) and ASIA_CHINA (Japan + China actions).

## At-Dispatch FALSIFICATION + REG-THRESHOLDS Scan

Ran 15-trigger scan. **No new fires.** No threshold-specific UST or foreign-holdings metric in current registry (potential v0.2 candidate: TIC monthly delta threshold).

— WALTER 2026-05-22 16:22 UTC
