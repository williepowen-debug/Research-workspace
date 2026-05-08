---
signal_id: SIG-W-20260508-003
precedence: ROUTINE
timestamp: 2026-05-08T03:30:00Z
source: WALTER
origin: ["First Squawk @FirstSquawk via X.com 2026-05-07 — 'China's Central Bank Fixes Yuan at 6.8502 vs Dollar, Compared With Last Close of 6.8068' (11m before image capture, 4.4K views). Will Telegram intake 2026-05-08 03:09 UTC msg 1485 IMG 1b", "Companion First Squawk post — 'PBOC Adds 500 Million Yuan Through 7-Day Reverse Repo Operations at Steady 1.40%' (3m before, 1.9K views) — KILLED Relevance (routine OMO, no threshold)", "WALTER live tape pull 2026-05-08 ~03:25 UTC: USDCNH=X $6.80 -0.07% — offshore yuan FADED the +44 pip weaker fix back toward last-close levels"]

to: ZHAO (ACTION — Tier 2 spawn-needed; ZHAO STALE 35d revival material; UST_FOREIGN composition channel + China money-market plumbing primary)
info: SAM (info — JPY-CNY cross via JAPAN_BOJ; if PBOC drift continues, BOJ June hike calculation cross-fires), LIQUID (info — broader funding-liquidity composition signal), RED (info — China FX-fix-vs-market-fade is regime-state observation, not bifurcation), HENRY (info — risk-off cross-asset if CNY weaker drift continues into NFP Friday)
group: ASIA_CONTAGION
dispatched: 2026-05-08T03:30:00Z
dispatch_note: "Will-page Telegram 5/8 03:09 UTC msg 1485 (1/3 image batch IMG 1b sub-card). PBOC fixed onshore CNY at 6.8502 vs last close 6.8068 — +44 pip / -0.64% yuan-weaker fix. Live tape pulled this session showed USDCNH=X $6.80 (-0.07%) — **offshore market FADING the weaker fix back toward last-close** within 12-13 hours of fix. **Within-range plumbing signal**, NOT threshold-cross. Why ROUTINE not KILL: (a) ZHAO STALE 35d — UST_FOREIGN domain primary needs revival material to reset; this is appropriate substrate; (b) PBOC fix-vs-market-fade pattern is a composition signal worth tracking even when within-range — the fade itself is the data (offshore says onshore-fix is wrong); (c) cluster ASIA_CHINA only has 3 signals — at low-population thresholds, not killing routine within-range moves preserves later-pattern-detection capability. Companion post (PBOC 500M 7-day reverse repo at 1.40% steady) → KILLED Relevance: routine OMO, 500M is small in absolute terms, no threshold, no policy-shift signal. **Cluster ToC update:** ASIA_CHINA 3→4. Confidence 0.85 (golden-source PBOC fix print + golden-source live tape). No verify-research needed. **ZHAO routing**: per ROUTING_TABLE ASIA_CONTAGION → ZHAO Tier 2 spawn / SAM backup; HAWK STALE 17d so SAM-info is intact; SAM 5d-fresh on JPY-cluster. **Implications for SAM JPY-CNY watch**: USD/JPY 157.03 (5/3 SAM) + USDCNH 6.80 = both Asian funding currencies modest-but-not-extreme; CNY weaker drift into NFP Friday could pair with BOJ June hike re-rating if NFP shows soft-side surprise."

signal_type: composition-shift
confidence: 0.85
confidence_language: golden-source-print
resources: 0
safety_net: clear

word_count: 287

cluster: ASIA_CHINA
cluster_mediating: false
verify_verdict: n/a (golden-source print)
---

## Signal

**PBOC fixes onshore CNY at 6.8502 vs last close 6.8068 — +44 pip / -0.64% yuan-weaker fix. Offshore (USDCNH) faded the move back to $6.80 within 12-13 hours. Within-range plumbing signal, ZHAO revival material.**

## Body

### Mechanics

- PBOC daily fixing: 6.8502
- Last close: 6.8068
- Fix-vs-close delta: +0.0434 (+44 pip / -0.64% yuan weaker)
- Live offshore USDCNH at WALTER tape pull 03:25 UTC: $6.80 (basically flat, -0.07%)
- **Net interpretation:** offshore market FADED the PBOC fix back toward last-close territory within ~12-13 hours.

### Companion post (KILLED)

First Squawk also posted "PBOC Adds 500 Million Yuan Through 7-Day Reverse Repo Operations at Steady 1.40%." This was killed Relevance — routine OMO, 500M yuan is small in absolute terms, no threshold cross, no policy-shift signal. Documented in kill_log.

### Why ROUTINE not KILL

1. **ZHAO STALE 35d** — UST_FOREIGN + ASIA_CONTAGION domain primary needs revival material to reset. This is appropriate substrate.
2. **PBOC fix-vs-market-fade as composition signal** — the fade itself is the data point. Offshore is saying onshore-fix is wrong. Worth tracking even when within historical range.
3. **Cluster low-population guard** — ASIA_CHINA cluster only has 3 signals. Killing routine within-range moves at low cluster population would prevent later-pattern detection.

### Cross-channel implications

- **JPY-CNY cross watch (SAM):** USD/JPY 157.03 (SAM 5/3) + USDCNH 6.80 — both Asian funding currencies modest-but-not-extreme. CNY weaker drift into NFP Friday 5/8 could pair with BOJ June hike re-rating if NFP shows soft-side surprise.
- **Funding-liquidity (LIQUID):** broader composition signal; not threshold cross.

### Routing

- **ZHAO action** — Tier 2 spawn-needed; ZHAO 35d STALE revival.
- **SAM info** — JPY-CNY cross.
- **LIQUID info** — funding-liquidity composition.
- **RED info** — regime-state observation.
- **HENRY info** — risk-off cross-asset watch into NFP.

## Cross-references

- **REGISTRY ZHAO row** — Tier 2 OC, STALE since 2026-04-02 (35d), spawn pending for SIG-W-20260428-001 China FRED material
- **Sister signal SIG-W-20260508-001** (Nightingale 3-CEO consumer-stretch) — different cluster but same-batch
- **Sister signal SIG-W-20260508-002** (gurgavin 3-layoffs LABOR step-function) — different cluster but same-batch

## Caveats

- Single-print observation; PBOC fix-vs-close moves of this magnitude (+44 pip) happen multiple times per quarter and are not always policy-signaling.
- Off-shore CNH ≠ onshore CNY exactly; the 6.80 spot pull may differ slightly from the actual onshore tape.
- ZHAO Tier 2 must be spawned for proper synthesis on whether this is part of a broader pattern.
