# FALCON — Hormuz-Bypass Integrity Gauge (BASELINE + METHOD)
**Built:** 2026-07-18 ~19:30 ET (Sat-eve wave #1, Will-selected) · **Owner:** FALCON · **Consumers:** BRENT (oil supply/premium split), HAWK (synthesis), SAM (Japan physical-vs-price exposure), PROME (D→75 hinge)
**Purpose:** Stand up the **first quantitative gauge** of Hormuz-bypass (STS/shuttle) integrity — the single most important FALCON transmission tell, previously narrative-only ("magnitude does not exist — no shuttle volume series anywhere," SCRATCH 7/17 item 7).

> ### 🎯 WHY THIS EXISTS — the transmission it measures
> My whole D=65 (not 75) read rests on: **the war repriced RISK PREMIUM but destroyed ZERO productive capacity**, because the Hormuz closure is **non-hermetic** — crude reaches market via a shuttle/STS bypass around the strait (Gulf terminals → Oman-hug → STS off Fujairah/Sohar → export). The registered tell: **"if the shuttle trade breaks, THAT is how risk-premium becomes supply-loss"** → D toward 75. Until now I could not measure it. This gauge measures the **downstream hub throughput** of that bypass. **A holding bypass ⇒ premium-only (D~65). A collapsing bypass while Hormuz transits stay collapsed ⇒ barrels genuinely not moving ⇒ supply-loss (D→75).**

---

## 1. The instrument (pullable, official, free)

| Attribute | Value |
|---|---|
| **Provider / dataset** | IMF PortWatch `Daily_Ports_Data` FeatureServer layer 0 (same infra as `hormuz_transit_watch.py` / `kharg_loadings_watch.py`) |
| **Field** | `export_tanker` (est. outbound tanker shipment, **metric tons/day**) + `portcalls_tanker` |
| **PRIMARY cluster** | **Fujairah `port362`** (ARE — world's largest bunkering/oil-storage hub) · **Sohar `port988`** (OMN) |
| **SECONDARY (context)** | Sharjah `port72` (ARE) — noisier, minor |
| **DROPPED** | Khor Fakkan `port561` — a **container** port, ~0 oil-tanker export (no signal; verified <200 t/mo) |
| **Cadence / lag** | Daily rows, ~5–8d publication lag (newest print 2026-07-10, 8d old [as-of 7/18]) |
| **Script** | `AGENTS/FALCON/scripts/bypass_watch.py` — INVERTED alarm: rc 0 = holding, **rc 1 = COLLAPSE below floor**, rc 2 = fetch fail |

---

## 2. Positive control — the series is POPULATED and RESPONSIVE (unlike Kharg)

The Kharg lesson (`KHARG_LOADINGS_SOURCE.md`): AIS export series are dark-fleet-blind and read 0 for whole normal months. **The bypass hubs are the OPPOSITE** — and for a coherent reason: the STS/shuttle legs are **non-sanctioned, re-flagged crude**, so vessels broadcast AIS normally. The gauge works *because* it sits **downstream of the dark leg.** Evidence [as-of 7/18 pull]:

| Port | nonzero export-days / month (typical) | Verdict |
|---|---|---|
| **Fujairah** `port362` | 9–23 / month | ROBUST — usable |
| **Sohar** `port988` | 18–26 / month | ROBUST — usable |
| Sharjah `port72` | 8–11 / month | usable, noisy → secondary |
| Kharg `port2164` (contrast) | **4 / 30** | dark-fleet-blind → NOT usable (see Kharg spec) |

**Positive control PASSED:** the primary cluster is well-captured, so a "zero/collapse" print here is *informative* (opposite of Kharg, where zero is the uninformative norm).

---

## 3. Baseline & the current read [as-of 7/18, newest data 7/10]

Monthly `export_tanker` (t/day avg), Mar→Jul 2026:

| Port | Mar | Apr | May | Jun | Jul(→7/10) | trailing-14d (t/d) |
|---|---:|---:|---:|---:|---:|---:|
| **Fujairah** | 4,733 | 43,635 | 9,849 | 27,102 | **45,524** | **52,027** |
| **Sohar** | 20,938 | 25,753 | 25,091 | 25,872 | **28,760** | 22,566 |
| Sharjah | 5,648 | 969 | 2,910 | 5,626 | 1,152 | 6,591 |

**Combined PRIMARY (Fujairah+Sohar) trailing-14d = 74,593 t/day vs a 60d-baseline of ~52,280 t/day → HOLDING, in fact running HOT.** Fujairah's early-July throughput is the **highest of the entire Mar–Jul window** (~2× its 60d base). 

**Read:** the bypass is **absorbing diverted Gulf crude, not breaking** — a direct quantitative confirmation of the "premium, not supply-loss" thesis and of the Bloomberg 7/16 / Vortexa "restoring existing Gulf flows" language, now with a number instead of a quote. **Zero evidence of the shuttle-trade breakage that would flip D toward 75.**

---

## 4. Threshold (FLAG-NOT-FIRE, disposition is FALCON's)

- **Metric:** combined PRIMARY (Fujairah+Sohar) trailing-14d mean t/day.
- **Collapse floor:** **30% of the trailing-60d daily mean** (currently ≈15,684 t/day combined). Below floor = `rc 1` REVIEW.
- **Why a trailing window, not daily:** `export_tanker` is lumpy per-departure (median 0 even at busy terminals) — a daily-zero test is noise. The 14d sum smooths it.
- **Why 30%:** deliberately conservative — a *genuine* bypass break (STS shut down / hubs interdicted) would drive throughput toward zero, not to 40–60% of normal. A shallow dip is ops/weather noise, not a supply event. Tune with more history; flagged as FALCON's disposition, not an auto-fire.
- **The DECISIVE conjunction (this is the actual signal, not the raw number):** `bypass COLLAPSED` **AND** `Hormuz transits still collapsed` (`hormuz_transit_watch.py` sub-18) = barrels genuinely not moving = **premium→supply-loss transmission → D toward 75, and FAL-01's "zero lost barrels" anchor breaks.** Either alone is not the signal (a bypass dip with transits recovering = flow just re-routing back through the strait).

---

## 5. HONEST LIMITS (STS-at-anchorage & attribution — do not overclaim)

1. **STS-at-anchorage undercount.** Pure ship-to-ship in the **Fujairah OPL** ("outside port limits") anchorage or mid-Gulf zones may fall **outside the port polygon** and not register. The gauge sees tankers loading from / departing the hub — which **co-moves with** bypass activity but is **not a direct STS count**. It can undercount a bypass that runs entirely at anchorage.
2. **Attribution is fuzzy.** Fujairah/Sohar are **global** hubs; `export_tanker` includes non-Iran flows. A *rise* can be unrelated traffic. **Therefore use DIRECTIONALLY and via the conjunction (§4), not as an Iran-bypass meter.** The informative event is a sustained **collapse while Hormuz stays shut**, not the absolute level.
3. **~5–8d lag.** A fast break is invisible for ~a week — the corroborator (news/Kpler) leads the data, same as Kharg.
4. **Not a substitute for FAL-01 or the Kharg gate.** This measures *bypass* throughput (the reversibility hinge), not a *production* hit (FAL-01) or a *Kharg strand* (GATE-TERRY-006). It is the third leg: production-hit (destruction) · Kharg-strand (removal) · **bypass-break (this — the transmission that turns premium into supply-loss without either).**

---

## 6. Routing / how consumers use it

- **BRENT:** the premium-vs-supply-loss split now has a number — bypass HOT ⇒ the mid-$80s move is premium; a bypass collapse is your cue that supply-loss is arriving (re-underwrite the $95–100 path).
- **SAM:** Japan's exposure is to **price, not physical shortfall**, *as long as this gauge holds*. A collapse flips that.
- **HAWK/PROME (D→75 hinge):** this is the quantitative gate on the reversibility thesis. Bypass holding = D capped ~65; bypass collapse + transits collapsed = the physical rung.
- **Cadence:** run at boot during RED posture (add to boot step 5b-3 next Monday session — deferred tonight); minimum weekly.
