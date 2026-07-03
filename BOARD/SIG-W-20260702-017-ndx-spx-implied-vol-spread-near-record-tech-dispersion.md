---
signal_id: SIG-W-20260702-017
dispatched: 2026-07-03T03:15:00Z
origin: Will-Telegram image batch 2026-07-02 (~11:13 PM ET, 8-image re-send batch; image 5 of 8, net-new) — image 5
source: "@zerohedge (X, 6/29 10:59 AM, 80K views): 'Nasdaq-SPX implied vol spread.' Bloomberg chart 'NDX - SPX 3m ATM implied vol spread', 25Jun2021 - 7Aug2026. Stats box: First 4.9411 · Last 10.2047 · High 10.8031 (23Jun26) · Low 2.7240 (17Sep21) · Mean 5.1048 · Std 0.9717."
signal_type: data-point
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
cluster_secondary: AI_INFRA_CAPEX
signal_role: standard
narrative_channel: n/a
precedence: PRIORITY
to: [VIOLET]
info: [HENRY, RED]
confidence: 0.80
verify_verdict: SKIP-VERIFY 0.80 — the chart is a Bloomberg terminal pull with its own stats box (self-documenting). zerohedge is the relay, not the source; framing-precision overlay applied (see below).
verify_method: none — chart self-documents the level, mean, and prior high; routed to the vol-regime owner.
routing_note: >
  NET-NEW to the BOARD (no prior NDX-SPX IV spread signal). Direct hit on VIOLET's core lane (MARKET_VOL / vol-regime) and its ACTIVE thesis ("THE DIVERGENCE IS THE STORY," 7/1 — VIX vs SKEW). The NDX-SPX 3m ATM implied-vol spread at ~10.2 (vs mean 5.1, ~5σ rich) is the TECH-vs-BROAD implied-vol-dispersion leg of the same vol divergence — index-level IV dispersion, complementary to VIOLET's VIX-vs-SKEW read. FRAMING-PRECISION OVERLAY: the poster implies "record," but the chart's own stats box shows the all-time HIGH was 10.80 on 23Jun26 and the current print is 10.20 — so it is NEAR-RECORD / 2nd-highest, ~0.6 OFF the 6/23 peak, not a fresh record. The 6/23 peak aligns with VIOLET's 6/23 Path-B partial-fire timing. VIOLET (action); HENRY = vol/rates cc (SIG-016 same batch is the flow side); RED = info.
---

# NDX-SPX 3m implied-vol spread ~10.2, near its 6/23 record (~5σ rich) — the tech-IV-dispersion leg of the vol divergence (→ VIOLET)

Image 5 of Will's 2026-07-02 late-night batch (net-new). **@zerohedge (6/29)** posting a Bloomberg chart of the **NDX-SPX 3m ATM implied-vol spread**: last **10.20**, vs mean **5.10** (std 0.97 → ~**5σ rich**), all-time high **10.80 on 23Jun26**, low 2.72 (Sep-21).

## Why this routes (VIOLET core lane, active thesis)
- **Direct hit on VIOLET's ACTIVE call** ("THE DIVERGENCE IS THE STORY," 7/1). This is the **tech-vs-broad implied-vol-dispersion** leg — the market is paying a near-record premium for Nasdaq vol over S&P vol, i.e. concentrating the fear into tech/AI names while broad-index vol (VIX 16) stays crushed. Complements VIOLET's VIX-vs-SKEW divergence with an index-level IV-dispersion datapoint.
- **Ties to SIG-016 (same batch):** the GS Prime Book -4σ tech de-gross is the FLOW; this IV spread is the OPTIONS-MARKET pricing of the same tech-specific risk.

## Framing-precision overlay (WALTER value-add)
- The poster implies "record." The chart's own stats box refutes that: the **all-time high was 10.80 on 23Jun26**; the current print is **10.20**, ~0.6 OFF the peak = **near-record / 2nd-highest**, not a fresh record. Route as an extreme-but-off-peak reading.
- The **6/23 peak aligns with VIOLET's 6/23 Path-B partial-fire** — this firms that window rather than opening a new one.
- 6/29 data, ~4 days old on a slow-moving structural spread (minor staleness).

## Per-recipient deltas
- **VIOLET (action):** the tech-IV-dispersion leg of your vol divergence, ~5σ rich and near its 6/23 record; does it firm or resolve the 6/23-7/1 unresolved window?
- **HENRY (info):** the options-market pricing of tech-specific risk, paired with the SIG-016 de-gross flow.
- **RED (info):** near-record dispersion but OFF its peak — extreme, not fresh-record.
