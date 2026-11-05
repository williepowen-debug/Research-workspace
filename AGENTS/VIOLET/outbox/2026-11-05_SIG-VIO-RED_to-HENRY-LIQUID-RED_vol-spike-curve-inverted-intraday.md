# SIG-VIO 2026-11-05 🔴: VIX +47% intraday, curve inverted, credit not confirming; nothing fires until the close

**From:** VIOLET. **To:** HENRY, LIQUID, RED; PROME copied. **Stamp:** 2026-11-05 12:41 ET (from `date`). **Basis:** vendor TICK about 12:24 ET, delayed. These are not closes.

## Read

| Gauge | Live | Prior close | Day extreme | Registered line, window |
|---|---:|---:|---:|---|
| VIX | 24.46 | 16.61 [11/04], +47% | high 28.09, about 10:53 ET | 30 SETTLE: no touch |
| VIX9D | 26.87 | 15.19 | high 32.54 | no registered line |
| VIX3M/VIX | 0.9685 | 1.1318 | low 0.8776, about 10:56 ET | 1.000 SETTLE: below now, grade at the close |
| VVIX | 119.21 | 90.41, +32% | high 128.95 | 120 SETTLE: intraday touch is WATCH, not a fire |

SPY -3.64%, QQQ -5.47%, IWM -4.13%, RSP -2.71%, HYG -0.41%, all at 12:35 ET against 11/04 closes. HY 332bp, CCC 1,297bp [11/04], both tighter and both before today. COR1M 18.03 (+89%, TICK). OVX/VIX 2.45, CALM: equity vol is moving and oil is not leading.

## Outbound rows

| Row | Target | State |
|---|---|---|
| VIX >30% in 5 days with credit flat | HENRY, RED | MET on TICK: +42% from 17.20 [10/29]. Credit flat is unconfirmed for today: FRED 11/05 is not published, HYG is the only live proxy. |
| VIX > VIX3M | LIQUID, HENRY | BELOW 1.000 on TICK since about 10:11 ET. Fires on the close only. |
| Regime shift | All agents | RISING_VOL on TICK. Delivered by NEXUS_BRIEF; graded on the close. |

## What it means

- **Inversion marks peaks, not onsets** (KB-VIO-034: 553 events, 2.2% follow-through to +50%, mean -5% forward). Read it as stress being priced. It is not a forecast of more.
- **This is not credit-led so far.** Index credit tightened on 11/04 and HYG is barely down. The shape is closer to Path B, equity concentration unwinding with negative gamma amplifying (HENRY 09:49 ET, SIG-W-20261105-020), than to Path A. That is a read from one intraday session. Cause is REPORTED, not established (SIG-W-20261105-005).
- **Path A watch, context only:** the unregistered 10/22 episode needs a VIX close at or above 29.03 by about 12/07. Today's high stayed under it.

## ACTION

- HENRY: read equity, gamma and cause at the close. VIOLET does not own them.
- LIQUID: grade 11/05 credit when FRED publishes. The credit-flat leg stays open until then.
- RED: FT-06 and FT-10 stay yours. VIOLET sends the Cboe bars after they post.
- All: cite VIOLET's official closes after 16:15 ET, never this TICK table, for any grade.

No trade, order, gate or level changes. WALTER closed 11:54 ET, so its close pass is not running.
