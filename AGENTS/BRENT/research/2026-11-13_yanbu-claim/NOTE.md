# Yanbu / East-West Pumping Station 7 claim (SIG-W-20261112-009): BRENT read, 2026-11-13

Written 2026-11-13 ~12:45 EST (from `date`). Scope: WALTER's ask of BRENT on card SIG-W-20261112-009: does the bypass-risk read or any registered row move; read the settlement, not the vendor last. FALCON grades the claims themselves (strike, damage); this note does not.

## 1. Settlement-basis price read (not the vendor last)

CME is IP-blocked from this box (403 since 10/28), so no official settlement page. Two vendor proxies that agree to the cent:

| Read | 11/11 | 11/12 | Change |
|---|---|---|---|
| BZF27 (Jan Brent, front) 1-minute VWAP [14:28,14:30) ET, saved bars | 92.7234 | 95.8278 | +3.1044 (+3.35%) |
| BZF27 vendor daily close | 92.76 | 95.82 | +3.06 (+3.30%) |
| M1−M3 BZF27−BZH27, window VWAP | +3.8713 | +4.2394 | +0.3681 steeper |
| M1−M3, daily closes | +3.84 | +4.29 | +0.45 steeper |
| Brent−WTI, Jan vs Jan daily closes (BZF27−CLF27) | 7.33 | 8.13 | +0.80 wider |
| WTI CLZ26 (Dec) daily close | 86.53 | 88.74 | +2.21 (+2.55%) |

Sources: `research/2026-11-12_wpsr/brt33/window_c1.json` (11/12 window, saved 11/12), `research/2026-11-11_saudi-momr/window_c1.json` (11/11 window), `daily_bars.txt` here (pulled 2026-11-13 12:42 EST). All [EST vendor settlement proxy].

WALTER's card read 96.04 / +3.5%: that is the 16:15 ET vendor last, after the 14:30 ET settle; on the settlement basis the move is **+3.30%** to 95.82.

**11/13 so far (vendor, advisory, ~12:40 ET):** BZF27 95.80, flat on the settle; M1−M3 about +4.80 (BZH27 last print 12:24 ET). The premium has held, not faded.

## 2. Assessment (what the tape does and does not say)

- FACT: front Brent rose 3.3% on the settle, the front of the curve rose more than the back (M1−M3 +0.37 to +0.45), and Brent rose more than WTI (Jan-Jan spread +0.80).
- ASSESSMENT: that shape (front-led, Brent over WTI) is what an Eastern-Hemisphere supply-risk premium looks like; a pure macro risk-off day (Treasury selloff, Nvidia) would not lift Brent over WTI. It is consistent with the claim being priced, not proof: the same session had other news, and no barrels are reported lost. Attribution stays NOT ESTABLISHED, as WALTER wrote.
- It also leans against `combo:paper-physical-gap` (the paper curve pricing a surplus): on 11/12 the curve priced risk, in the same week the US printed an +11.4M build.

## 3. Registered rows

| Row | Letter needs | 11/12 claim supplies | Moves? |
|---|---|---|---|
| BRT-32 Yanbu loading halt (OPEN 20%) | Aramco, energy ministry or SPA statement that loadings stopped, or a Reuters/Bloomberg halt report, 24h+ | a Houthi claim; Saudi intercept reports; Aramco silent; no loading statement; no halt report found at secondary reach 11/13 midday (web search) | **No.** Letter not met; 20% unchanged. The registration priced repeated warnings and claims; a third claim with no confirmed damage is inside that. |
| BG-02 (laden-tanker loss) | lapsed 9/25; standing watch: a laden-tanker loss with cargo confirmed | nothing on tankers | **No.** |
| BRT-33 F-a cross (M1−M3 < +3.50) | one window under +3.50 by 11/27 | 11/12 window +4.2394, already recorded (valid 4 of 5) | **No**, and the move is away from the line (steeper). |
| THESIS F-a / KILL legs / TRACKER lines | — | price only | **No** gate, band or line moves. |
| `refinery_damage/INCIDENTS.tsv` | primary-verified facility damage | claim only | **No row** (LESSONS #1). |

## 4. Bypass-risk read (combo:yanbu-bypass)

Moves in **weight, not in state**: fourth claim or attack on the bypass system in five days (11/9 confirmed hit near Madinah, small fire, operations unaffected; 11/11 Pumping Station 11 claim; 11/12 Pumping Station 7 and Yanbu claim), and on 11/12 the settle priced it. Still no confirmed loss of flow, no loading change, no Aramco word. Logged as a member on the theme row in `docket/CATALYSTS.tsv`; review date 11/19 unchanged. A move in state needs a qualifying halt report (BRT-32) or a Saudi statement that the line or a station is out.

## 5. Tradeability

No TERRY packet from part one: no registered row moved and the event is unconfirmed. The settle-basis premium (+3.30%, front-led) is reported as tape, not a finding. If FALCON confirms damage to the line or a station, that is the material event and goes to TERRY the same session.
