# New oil position review — 2026-09-10 ~18:1x ET (Will asked; assessment, not a proposal)

**Read path taken before this assessment:** TRADE.md → SPECS_GATES.md (BG-01…09) → SPECS_OFFRAMP_ENTRY.md (BE-01…16) → SPECS_TRADE_RULES.md (BH-01…16) → THESIS.md v5.8 → TERRY RISK_RULES Non-Negotiables → FORGE/STATUS.md 9/10 reconcile. Live chain pulled 18:0x ET (Yahoo delayed; ICE Brent settled 18:00, NYMEX 17:00 — daily bars below are final).

## 1. Tape at the 9/10 settle [CONF Yahoo daily bars 18:07 ET]

| Instrument | Settle | Δ day | Note |
|---|---:|---:|---|
| Brent Nov `BZX26` | **108.95** | +7.65% | three sessions +11.3% (97.92 → 108.95) |
| Brent Dec / Jan / Feb | 103.85 / 99.01 / 95.07 | | **Nov–Jan +9.94** (9/8 bars +6.62); Nov–Dec +5.10 |
| WTI Oct `CLV26` / Nov `CLX26` | 103.93 / 99.56 | +8.20% / +7.20% | WTI–Brent Nov **−9.39** |
| ULSD Nov `HOX26` / RBOB Nov `RBX26` | 4.920 / 3.245 $/gal | +6.4% / +6.5% | ULSD−WTI Nov 107.08; RBOB−WTI 36.73 |
| **Brent-basis 3:2:1 (WALTER Boundary #8)** | **50.79** | | (2×136.29 + 206.64)/3 − 108.95. **CROSSED $50 at the 9/10 settle — session 1 of the 2–3 required.** 9/9 settle basis 47.80 not crossed. |
| USO | 158.38 | +5.61% | 37 shares held (Fidelity) |
| XLE | 64.93 | −0.58% | down on a +7.65% crude day, third such session |
| OVX | **60.76** | +21.9% | crisis-level vol, rising WITH price |
| STNG / FRO / DHT | 84.51 / 48.40 / 21.43 | +1.8% / +2.5% / +1.1% | liveness composite quiet; no owner grade run |

## 2. What the book already holds (FORGE 9/10 reconcile, ANVIL; BRENT TRADE)

USO 37 sh $5,860 (+29.5%, today +$311) = **14.7% of the $39,885 Fidelity book**; XLE Sep-30 65C **×1** (FORGE broker-verified 2→1, one contract sold on an unrecorded date — TRADE.md mirror corrected 9/10 evening); Robinhood USO Sep-11 159C ×1 @1.52 (Will-hand, no rule). Sep-18 150/165 spread CLOSED 9/10 +$330. **WQ-200 (a USO share harvest rule) was DECLINED by Will 9/10 11:15 — the shares are managed by hand.** Concentration flag (BH-10) stands.

## 3. Candidate structures priced against the specs — INFORMATIONAL, none fires

### 3a. Structural LONG (BG-02 vehicle/structure: USO vertical call spread, 60–90 DTE, long ~5% OTM / short ~12–15% OTM, ≤~$500, debit ≤33% of width)

Eligible monthly: **Nov-20 (71 DTE)**. Dec-18 is 99 DTE — outside the band.

| Spread | Debit (touch: ask long / bid short) | Debit (mid) | Width | Debit % width | R:R | IV | Max loss |
|---|---:|---:|---:|---:|---:|---:|---:|
| 165/180 | 12.95 − 8.15 = **4.80** | 4.05 | 15 | **32.0%** (mid 27%) | 2.1:1 (mid 2.7:1) | 54–57% | $480 |
| 165/185 | 12.95 − 7.10 = 5.85 | 5.05 | 20 | 29.3% | 2.4:1 | 54–58% | $585 — over cap |
| 170/185 | 11.10 − 7.10 = 4.00 | 3.44 | 15 | 26.7% | 2.75:1 | 55–58% | $400 |

BG-03 economics PASS on 165/180 and 170/185. **But BG-02 deploys ONLY on a confirmed destroyed-capacity event** — none exists (FALCON: zero confirmed crude-production barrels offline, 195 war-days; Riesco/New Andros/Hercules Star graded NOT MET today). A passing economics leg is not a fire (BG-07: a gate that passes carries zero thesis information).

### 3b. Off-ramp SHORT (BE-14: USO bear put spread, 21–35 DTE, long ~5–10% OTM / short ~15% OTM, ~3:1, ≤~$500)

Eligible: **Oct-2 (22 DTE)**, **Oct-9 (29 DTE)**; Oct-16 is 36 DTE — one day outside.

| Spread | Debit (touch) | Width | R:R | IV |
|---|---:|---:|---:|---:|
| Oct-9 145/135 | 4.20 − 1.49 = **2.71** | 10 | 2.7:1 | 53–54% |
| Oct-9 150/135 | 6.05 − 1.49 = 4.56 | 15 | 2.3:1 | 54% |
| Oct-2 143/135 (thin) | 3.10 − 1.11 = 1.99 | 8 | 3.0:1 | 55–56% |

**BE-01 trigger NOT fired**: no named-official signature / sovereign-action de-escalation; the alternate ">50% transit normalization" branch is UNRESOLVED (no live instrument, BE-01b). Today's kinetic direction is the opposite of the trigger. Leg T/C unrunnable without a day-0 event.

### 3c. Demand-collapse short (THESIS: Brent <$70 on confirmed demand collapse) — $108.95. Not near.

## 4. Rule gates, stated

| Gate | State | Effect |
|---|---|---|
| **WQ-192 STAND DOWN** (Will 9/7 14:42) | BINDING | No new energy capital hold; any rec returns to Will as a proposal and requires him to lift the stand-down explicitly. |
| **Root rule #6** (puts on green days, calls on red days) | Today: +7.65% Brent, +5.61% USO — a strongly GREEN day | A new long-call expression tonight is a rule-#6 break; the break test needs a direct measurement refuting the day-colour proxy written in figures before the fill. None offered. A put spread on a green day is rule-#6-consistent in colour but has no trigger (3b). |
| **BG-02 frame-breaker** | NOT MET ×3 today | Structural long does not deploy. |
| **BE-01** | NOT FIRED | Off-ramp short does not arm. |
| **BG-01 re-arm** | none registered | R1 (OVX >68.97) is a memo candidate, not live; OVX 60.76 today. |
| **Non-Negotiable #8** (no naked "because thesis") | | A long added on a +7.65% headline day at 54–58% IV is the expression the rule exists to stop. |

## 5. Assessment

**No new oil position tonight, on either side.**

- **Long:** the premium is being paid at its most expensive point — three sessions +11%, OVX 61 and rising with price, curve at +$9.94 Nov–Jan. The move is kinetic-headline driven (five hulls, Riesco sunk, Iran's 10-vessel claim, US strikes on the Hormuz shore, Israeli threat to Iranian energy infrastructure) while the US physical balance loosened at the margin today (Cushing 21.8M, distillate second build, SPR draw −1.24M) and energy equities declined for a third session. Nothing has destroyed crude capacity. The book is already long 37 USO shares with no harvest rule — it participates in a blow-off without adding vega at 55% IV. Buying calls here is the chase the frame-breaker letter exists to exclude.
- **Short:** the off-ramp fires on a de-escalation SIGNATURE plus tanker liveness plus two-day crude follow-through. The tape is the mirror image. Shorting a +7.65% escalation day on the belief it is "too far" is a view without a trigger.
- **Counter-case, stated:** if this is the start of a Phase-1 blow-off toward $120 (Goldman's raised probability, cited via WALTER), the book is underweight the tail relative to conviction. The answer is that 37 shares ≈ 15% of the Fidelity book already carry that tail, and the correct add is the pre-registered one below, on its trigger, not tonight.

## 6. What would change the answer (pre-registered so it is not decided by feel)

1. **Structural long fires** on a confirmed destroyed-capacity event under BG-02: a laden hull sunk with cargo lost in the corridor · a named-major facility with confirmed capacity loss (an Israeli strike on Iranian export infrastructure would qualify only with a confirmed loss figure) · a measurable fall in Gulf export/transit throughput. Vehicle ready: **USO Nov-20 165/180 call spread**, ~$4.05–4.80, max loss ≤$480, re-priced from a live chain at fire; Will's [Approve]; STAND DOWN lifted by Will in words; rule-#6 timing honoured or the break written in figures.
2. **Off-ramp short fires** on BE-01 (i) + T + C. Vehicle ready: **USO Oct-9 145/135 put spread**, ~$2.71, re-priced at fire; tranche rules BE-11/12; H1/H2/H3 harvest.
3. **Share management** — the only oil decision that is live tonight is how the 37 shares are managed; WQ-200 was declined this morning and that stands. A green-day scale-out is rule-#6-consistent if Will ever wants one; not proposed here.

$0 moved. No proposal issued. Boundary #8 session-1 cross recorded for tomorrow's settle grade.
