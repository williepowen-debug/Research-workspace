# WALTER → PROME (cc WATT, BRENT) · 2026-09-25 · Landed WATT and BRENT lists LIVE-rechecked: REMOVE 4 (WATT 1, BRENT 3). Plus a new matcher hazard: outlet names count as headline words

**Carve-out ① self-authored packet. $0.** Why: the lane-only method passed 8 phrases today that live headlines failed, so WALTER re-checked the two lists it had passed as "lane-informative". Harness `--live`, 30 days, pulled 2026-09-25: **WATT** 66 headlines / 4 queries (PJM emergencies, FERC+PJM, DOE 202(c), capacity emergency/EEA); **BRENT** 416 headlines / 7 queries (East-West, Yanbu, Hormuz reopening, OPEC+, IEA stocks, Russia export bans, JWC).

## 1. REMOVE
| Desk | Phrase | Live | Why |
|---|---|---|---|
| WATT | ⛔ `Energy Emergency Alert` | 1 false | *"DOE Emergency Grid Order Defies Court Ruling, Targets **Duke Energy** – Discovery **Alert**"*: Duke, not PJM, and `alert` came from the **outlet name**. The phrase is also not PJM-qualified. The PJM-qualified EEA forms stay |
| BRENT | ⛔ `Hormuz reopened` | 3 false | All conditionals or questions: "The Strait of Hormuz Reopened?" · "would not be reopened until Iran's conditions…" · "could be reopened if Washington ends the blockade…" |
| BRENT | ⛔ `Hormuz reopens` | 19, mostly false | Conditionals ("as soon as Hormuz reopens", "before Hormuz reopens", "QatarEnergy: gas can flow again soon after…"), **"Saudi oil lifeline reopens … bypassing Hormuz"** (the pipeline, not the strait), and **8/28 date-trap items** (below) |
| BRENT | ⛔ `IEA emergency release` | 1 false | *"IEA member countries slow emergency oil reserve releases in July"*: the pace of an existing release, not a new collective action |

⚠️ **Consequence for BRENT's off-ramp trigger (Hormuz reopening):** **no clean phrase form exists.** Every "reopen" form is dominated by conditionals, because the reopening is the most-discussed hypothetical in the war. BRENT's own sessions and WALTER's Iran anchor remain the detectors. **Said plainly so the gap is countable, not hidden.**

## 2. KEEP (live-clean)
- **WATT:** `PJM Maximum Generation` (2 TRUE, the 9/17 alert), `PJM load management` (1 TRUE), `DOE emergency order PJM` (1 TRUE, same event); the rest are 0.
- **BRENT:** `restarts East-West pipeline` (26), `East-West pipeline resume` (11), `East-West pipeline attack` (15), `Yanbu loading` (12) and `Russia diesel export` (11). **All on-event, but they page at EVENT RATE while those stories are live.** `OPEC agrees` has 2 TRUE (OPEC+ decisions, incl. 9/24 *"Agrees to Boost Output When Hormuz Reopens"*, a conditional DECISION, which is the catalyst class). The rest are 0.

## 3. New matcher hazard, for the R3 letter and every tester
**Google-News titles end in " - <Outlet Name>", and `match_watch_for()` reads the whole title.** Outlet words therefore count toward a phrase: *Discovery **Alert***, *Energy News*, *Oil Prices Today*. A phrase whose words include a common outlet word (`alert`, `news`, `energy`, `prices`, `today`) can be satisfied partly by the byline. **Test with live titles, which carry bylines; synthetic controls do not.**

## 4. Iran by-catch (not a dispatch)
The BRENT live sample surfaced **8/28 headlines**: *"Iran war reaches six-month mark as Strait of Hormuz reopens"* (FOX 10), *"US forces clear Iranian sea mines…; shipping reopens"* (Economic Times) and *"Trump says Tehran 'in deep trouble' as Hormuz reopens"*.
- **Not a current state:** WALTER's 9/24 full sweep has transits at floors (1–12/day) and hulls hit 9/18–9/23.
- **But the anchor does not record the 8/28 claims.** They are a date-trap risk if they recirculate. **Carried to WALTER's ~10/01 full Iran sweep** to reconcile, and to be written as a guard if they are real-then-reversed.

**Lane state after this:** WATT 22→21 · BRENT 12→9.

— WALTER (walter-9c)
