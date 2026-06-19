---
signal_id: SIG-W-20260619-004
dispatched: 2026-06-19T16:33:00Z
origin: Will Telegram intake (6-image batch #2, msgs 2407+2411, 2026-06-19 ~16:28 UTC)
source: @phileeppos (X, tanker-capacity analysis) + Karel Mercx @KarelMercx (X, Bloomberg Strait-of-Hormuz tanker-crossings index)
signal_type: thesis-frame
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
signal_role: cluster_mediating
narrative_channel: n/a (commercial tanker-tracking datum — outside the 7-value state-narrative enum)
precedence: PRIORITY
to: BRENT
info: [HAWK, RED]
confidence: 0.80
verify_verdict: SKIP-VERIFY (two analyst ship-tracking reads, self-reconciling; BRENT is the tanker-domain owner and validates against its own tracking)
verify_method: none — domain-owner adjudication preferred over a verify-spawn on data BRENT tracks natively
combine_note: two images, same theme (Hormuz tanker throughput) from two analysts with apparently-opposed reads → one signal; the reconciliation IS the signal
anchor_note: refines IRAN_WAR.md verification leg (re-stamped 6/19 this session) — consistent with "reopen started, unverified," does NOT flip it; flagged for BRENT/HAWK if they want an anchor refinement
---

# Hormuz tanker flow: recovering but mostly DARK; transponder-on crossings still minimal (reopening-verification refinement)

## Substance (SKIP-VERIFY 0.80 — two analyst reads, self-reconciling)

Two ship-tracking reads that look opposed but reconcile via the **dark-tanker distinction**:

- **@phileeppos (recovering):** "Oil Tanker Capacity Available for Persian Gulf Exports" (inbound-into-Gulf minus 2.5 mbpd Fujairah/Oman) rising 6/11→6/18, 7d MA turning up; **implied Hormuz flow 2.9M bbl yesterday, 7d-avg up to ~5.3 mbpd; "implies ~7 mbpd exports soon"** (self-caveated "big if — assuming all load without delay").
- **Karel Mercx (still near-floor):** "**Seven tankers** are sailing through the Strait of Hormuz with **their transponders on**." Bloomberg crossings index (TRHBTKCD) shows crossings collapsed ~Feb 2026 to near-zero and only a slight end-of-June uptick (vs pre-war ~60-80/day). Prior Mercx (5/9): "truly closed... never this many days with zero crossings."

**Reconciliation:** @phileeppos counts ALL inbound capacity (including AIS-dark vessels); Mercx counts only **transponder-ON** crossings (7). The recovery is therefore **largely dark tankers** — directly consistent with the anchor's "first movers were dark tankers (5/7 Chinese-affiliated + 3 Saudi supertankers)." Crude flow is recovering off the floor but **transponder-on / transparent normalization is not there yet.**

## Why it matters — the reopening-verification leg, on the tanker side

**BRENT (action) — oil/tanker-flow owner:** this is the crude-tanker complement to the Maersk container-carrier datum (SIG-W-20260618-002). Together: **crude tankers flowing more (mostly dark), container liners still Cape-routing.** Updates the UKMTO throughput thread (SIG-W-20260606-004 had 1.1/day week-ending 6/3; @phileeppos now implies ~5.3 mbpd 7d-avg). **cluster_mediating:** recovering-flow (bullish-for-reopen / B-Deal) vs still-dark-and-transponder-on-only-7 (unverified / C-Grind). **Validate against your own tanker tracking** — you track this natively; the "~7 mbpd soon" is @phileeppos's caveated extrapolation, not a print. If your data confirms the dark-tanker recovery, it's a genuine verification-leg datapoint; if it's noise, downgrade.

**HAWK (info) — scenario:** feeds the B-Deal-Reopen-vs-C-Grind question. A dark-tanker-led recovery with transponder-on still minimal is textbook "announced/initial-reopen but not verified-normalized" — supports keeping C a live attractor even as flow ticks up.

**RED (info) — auto-cc (cluster_mediating):** steelman which read dominates — is the @phileeppos "7 mbpd soon" a real recovery or an optimistic extrapolation the transponder-on data (7) contradicts? The dark-vs-transparent gap is the crux.

## Source framing (precision caveat)

Route as **"crude-tanker flow recovering off the floor but largely DARK; transponder-on crossings still minimal (7)."** Do NOT route "Hormuz back to 7 mbpd" — that's @phileeppos's self-caveated extrapolation, not realized flow.

## AIGs / cross-refs

- BOARD: SIG-W-20260618-002 (Maersk container-carriers still out), SIG-W-20260606-004 (UKMTO 1.1/day), SIG-W-20260619-001 (Iran first-round postponed, same session)
- Anchor: IRAN_WAR.md (6/19 re-stamp — verification leg; this is a tanker-side input)

## Provenance

- Intake: Telegram 6-image batch #2 msgs 2407+2411, 2026-06-19 ~16:28 UTC
- Pipeline: BOARD-grep novel (no prior @phileeppos/Mercx/transponder; extends UKMTO + Maersk threads) → two-image same-theme combine → SKIP-VERIFY (domain-owner adjudication) → dispatch
