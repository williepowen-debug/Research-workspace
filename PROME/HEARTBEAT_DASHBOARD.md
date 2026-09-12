# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Fourteenth base 2026-09-11: chain 2 — Amendment #1 (closeout write-back 12:1x) and Amendment #2 (evening closeout 19:5x, the Saudi MoE Petroline shutdown statement) projected below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "c6ebe16a080ee95b8dde186ac6011ac2d89b3ce670e49f7c96de8aec6873388e",
  "set": {
    "one": "September 11 midday: CPI printed in line (core unrounded +0.290% m/m sits on HEN-44's CONFIRM side by 1bp). TLT 77P delta −0.0354 ⇒ the book is net long duration through GLD. XLE 65C ×1 sold by Will at $1.51 (−$77.33 realized); VLO ×3 does not fire on the 9/10 read. NEXUS C#2 = C, clause exhausted, no successor (WQ-224). WATT P1 5→3, composite 14/20. STAND DOWN holds.",
    "channels": {
      "Rates": {
        "headline": "🔴 CPI in line; core unrounded +0.290% ⇒ HEN-44 CONFIRM 1bp",
        "body": "August CPI +0.4% m/m / 3.4% y/y; core +0.3% / 2.4% [BLS 9/11]. HEN-44 Leg C is keyed to numbers: unrounded core +0.290% m/m · 2.446% y/y sits on the CONFIRM side (≤0.30 / ≤2.55) by 1bp — HENRY grades. TLT 77P delta −0.0354 [TERRY 10:11] vs MIDAS's 0.0504 breakeven ⇒ net long duration through GLD. 007 owner-graded through 9/9, 0-of-5; the 9/10 cells post ~16:15."
      },
      "Energy": {
        "headline": "🔴 XLE 65C ×1 sold by Will; VLO ×3 does not fire on yesterday's read",
        "body": "Will sold the XLE 65C ×1 on 9/11 — filled $1.51 (net $150.34 vs basis $227.67 ⇒ −$77.33 realized, TERRY bcc962bbd); D-49 stays open only for the first contract's date/price. VLO ×3: the 9/10 day-colour read was a MOMENT property (RISK_RULES #14) and expired with its session; 9/11 read the inverse (refiners up, USO down); fill waits for a day the refiners are red against oil; re-arm $1,187.31. Petroline: nothing fired; resolver to 9/25."
      },
      "Credit": {
        "headline": "🔴 NEXUS C#2 = C — clause exhausted, no successor (WQ-224)",
        "body": "C#2 graded BRANCH C, NO-VERDICT, FINAL on the pinned 8/28→9/10 window; the non-renewable clause is exhausted; the admission gate admitted 0 of 4 ⇒ no successor; split 20/47/33 carried un-falsifiable. ROLL70-EXIT 0-of-3 through 9/10 (REGINALD)."
      },
      "War theaters + tariffs + housing": {
        "headline": "🟠 WATT P1 5→3 executed; composite 14/20",
        "body": "P1 stepped 5→3 at 10:37 ET on WATT's own letter; both override gates verified clear (no new §202(c) naming PJM; no emergency-class PJM posting). Panama: A-33 postpones the 47.5 ft step until further notice; Gatún 84.04 ft [9/10]. MF DQ 7.69% Aug, flat [Trepp 9/1]."
      }
    },
    "ticker": {
      "XLE": "XLE 65C ×1 SOLD by Will 9/11 at $1.51 (−$77.33 realized); line FLAT",
      "WAL": "WAL 78.50 [9/11 10:1x intraday]; ROLL70-EXIT 0-of-3 through 9/10",
      "TLT": "TLT 81.21 [9/11 10:1x intraday]; 77P delta −0.0354"
    }
  }
}
```

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "4aa5a45938eef950b02f743f9e6d29de2139785d19f2ea690c433143c632e4d0",
  "set": {
    "one": "Tell #2 FIRED: the Saudi Ministry of Energy stated the East-West (Petroline) crude line is SHUT \"as a precautionary measure\", firing FALCON's pre-committed resolver #1. ⛔ Attribution, damage location and barrels all remain unestablished. BRENT has NOT re-graded BG-02 — its packet predates the statement, and a shutdown statement is not a throughput measurement; the ≥0.7 mb/d 7-day-MA resolver runs to 9/25. Marks HOLD B 3 / C 22 / D 75; FAL-05 unfired at 55%, but route (a) force majeure is one declaration away with no duration bar. STAND DOWN holds (WQ-192); $0 moved.",
    "channels": {
      "Energy": {
        "headline": "🔴 Saudi MoE: Petroline SHUT — tell #2 FIRED; barrels unknown",
        "body": "The Saudi Ministry of Energy stated (X, Fri 9/11) that the East-West/Petroline crude line is shut \"as a precautionary measure\" after \"multiple\" attacks 9/10 in the Riyadh and Madinah regions — firing FALCON's pre-committed resolver #1, written before the event. Nothing else moved: marks HOLD B 3 / C 22 / D 75 (a pipeline is not a hull ⇒ no D→85 leg; 3rd consecutive check); GATE-FALCON-001 unchanged, review 9/14; thesis-kill 0/7. FAL-05 NOT FIRED, OPEN @55%, confidence deliberately unmoved — route (b)'s volume limb is unestablished and its ≥7-day bar unmet ⇒ earliest 9/17–18, but route (a) force majeure is one declaration away and has NO duration bar. ⚠️ BRENT has NOT re-graded BG-02 (its 9/11 afternoon packet predates the MoE statement; no published time of day for the statement is on file at any FALCON artifact — do not quote one): a shutdown STATEMENT is not a THROUGHPUT measurement, so BG-02 stands NOT MET on its own letter and the ≥0.7 mb/d 7-day-MA resolver runs to 9/25 (L329); BRENT's read is OWED. ⛔ ATTRIBUTION, DAMAGE LOCATION and BARRELS remain unestablished — net supply loss UNQUANTIFIED, the route-geometry test INCONCLUSIVE with no station named, and multiple relays of ONE statement are ONE source. FALCON shipped five wrong claims to three desks the same night and corrected them in place after an external review (one had gone to BRENT as forward guidance). Carried from midday: XLE 65C ×1 sold at $1.51 (−$77.33 realized), D-49 open for the first contract only; VLO ×3 does not fire on the 9/10 read — the fill waits for a day refiners are red against oil, re-arm $1,187.31. STAND DOWN holds (WQ-192); $0 moved."
      }
    }
  }
}
```
