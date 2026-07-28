# BOND — Run Receipt

**Session:** 2026-07-28 (Tue, ~02:50 → 06:00 ET) — 5-day-dark boot → live-event override → Will-tasked 12-item mail drain → Will-tasked **file-by-file document review** → FR2004 root-cause fix. · **Overwritten at closeout.**

**Mail state at close:** general inbox **EMPTY** · WALTER lane **EMPTY** · outbox **4 new** (HENRY, NEXUS, HENRY+NEXUS+PROME, LIQUID+PROME).
**Repo:** BOND working tree clean, 0/0 with origin, ~20 commits, all pushed.

---

## Session summary

Booted 5 days dark into a live cluster (7Y today 1PM, FOMC tomorrow 2PM). Wrote the time-critical artifact first — the 7/27 auction grade plus a **frozen** 7Y pre-registration, on disk ~10h before the print — then drained all 12 mail items. Will then asked whether the stale files had *actually* been updated; they had not, and a file-by-file read of 17 files/groups found **~40 defects**. The session's largest finding came last: the FR2004 "data gap" was a **self-inflicted query bug**, and closing it **retired a leg of BOND's own bear thesis**.

## Deliverables

| # | Artifact | Note |
|---|---|---|
| 1 | `analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md` | 7/27 grade off TD primaries (n=250) + **FROZEN, tail-free, composition-keyed 7Y pre-reg**, on disk ~10h pre-print. §4b later added the pre-print challenge to itself. |
| 2 | `monitors/fr2004_fetch.py` | **NEW.** Resolves the NY Fed series break at runtime; fails loud on empty series and >28d staleness. Closes a 6-week gap. |
| 3 | `thesis/PREDICTIONS.tsv` **BND-13** | The 7Y registered at 85% — the session's most falsifiable claim, which had been living only in an analysis file. |
| 4 | 4 outbox packets | HENRY (falsifier adjudication) · NEXUS (owed grade) · HENRY+NEXUS+PROME (pre-reg challenged, then **amended after reading the backtest at source**) · LIQUID+PROME (FR2004). All verified **at the recipients' inboxes**, not at my record of sending. |

## Workbook

- **KB.tsv:** +8 rows (**KB-BND-089…096**). CRLF preserved, 13-col validated after every append.
- **VX.tsv:** 13 row-updates. **Score moves: VX-01 2→3** (5Y BTC trigger) · **VX-02 1→2** (credit widening) · **VX-04 3→2** (FR2004 gap closed, record unwound).
- **FLOW.tsv:** +2 (**FL-BND-12** oil→breakevens CONFIRMED · **FL-BND-13** basis-trade→thin-cover WATCH).
- **PREDICTIONS.tsv:** BND-13 registered; BND-01 notes refreshed (was 81 days stale) with the resolution instruction that matters — *grade the mechanism separately from the level*.
- **Composite: 12 → 14 → 13/35**, re-verified against VX.tsv.

## The four findings that changed something

1. **FR2004 was never blocked.** A stale API series break (`SBN2022`) returned **HTTP 200 with data ending 2024-07-02** — reading exactly as "the API caps pre-2026." Three re-attempts and an escalation to Will, none of which audited the path. Recovered data shows the dealer record **unwound −17.4%**, firing my own pre-registered downgrade and **removing "record dealer stock" from the demand-hole configuration.** Cuts against the standing thesis.
2. **A 323-auction backtest in `proposals/` — a directory never opened — challenges the falsifier frozen the same morning.** Then, reading the backtest *at source* rather than MATRIX_V2's summary, **I had to weaken my own challenge** (regime non-stationarity, N=11, a denominator mismatch). Both versions routed; spec not edited.
3. **THESIS was bumped to v1.1.3 claiming a re-specification that had not happened** — three tail-keyed gates still live in the body (thesis kill, TLT re-arm, KEY THRESHOLDS).
4. **TRADE's two tables disagreed on whether an add-gate had fired** — the standalone version fired 7/16, the day Will decided NO-ADD.

## Corrections issued (self, unless noted)

| Claim | Correction |
|---|---|
| HY OAS 275 `[7/2]` | **279 [7/24]** — 26 days stale; survived because it was *plausible* |
| FOMC "HOLD ~90% priced" | **~65/34** — ~25pp, and it survived in a **4th location** after I'd fixed three |
| Joint HEN-42 falsifier | **Mis-specified by me as author** — anchored on a 2Y tail a term-premium story cannot produce |
| Brent "$100.43 🔴 THROUGH $100" | **~$90.57** — STATUS contradicted its own analysis for 5 days |
| "Thu 7/31" | **Friday** — verified with `date`, not assumed |
| FR2004 "env-blocked" | **Self-inflicted query bug** |
| My own 04:45 backtest challenge | **Overstated** — corrected in place before consumption |
| HENRY: 5Y BTC "nearly five years" | **~3y10m** |
| HENRY: FedWatch leg retracted | **Over-retracted** — instrument died, claim didn't |
| NEXUS: "14th consecutive tail" | **Unverifiable by construction** — not carried |

## Git

~20 commits, all BOND-pathspec from root cwd, plus 3 carve-out ① packet deliveries and 1 carve-out ③ auto-memory. Auto-push via `safe-push.sh` throughout; final state 0/0 with origin.

## Owed / next session

- **🔴 7Y grades at 1PM ET (~8h).** Procedure in SCRATCH item 1 — grade the frozen branches, **then** report the indirect leg standalone, and **report any disagreement rather than averaging it.**
- **🔴 FOMC Wed 7/29 2PM** — ~34% hike, no forward guidance, two-sided.
- **v1.1.4** after the 7Y: adopt the 15th-percentile indirect rule + drop dealer-as-bearish + fold in the dealer downgrade. **Reconcile the denominator first** (of-offering vs of-competitive-accepted).
- **LIQUID owes a refusal-or-confirm** on the benign-distribution read of the dealer drawdown.
- **Review queue** (files still not read end-to-end) listed in SCRATCH.
