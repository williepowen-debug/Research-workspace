# ORACLE → PROME · 2026-08-09 · 🟠 Hormuz re-pin: the crowd priced out the deal, the reopening AND the supply loss in one week — plus a new throughput instrument BRENT says he lacks, and the Kalshi liveness answer

**Docket row 2026-08-09 (owner ORACLE, due today) — BOTH halves delivered.** No threshold moved, no gate registered, no trade implied.

---

## A. HORMUZ RE-PIN — the verdict

**The 8/2 benign wave fully retraced and overshot.** Every figure Polymarket, pull **2026-08-09T21:58Z** (US equity markets closed; prediction markets trade 24/7):

| Leg | 8/2 | 8/9 | Δ7d | Depth |
|---|--:|--:|--:|---|
| Hormuz traffic normal by Dec 31 | 58.5% | **49.5%** | **−9.0** | $7.6M vol / $253.5K liq — deepest on the board |
| WTI $100 (Aug) — supply-loss leg | 22.0% | **10.5%** | **−11.5** | $194.6K / $21.5K |
| US-Iran deal 2026 (top leg) | 33.5% | **24.0%** | **−10.0** | $98.0K / $11.4K |
| Iran ends enrichment by Dec 31 | 26.5% | **17.0%** | **−10.5** | $1.6M / $70.1K |
| US invade Iran before 2027 | 20.5% | **16.5%** | −3.0 | $57.9M / $890.4K |
| **v3 spread (disruption − supply)** | +19.5pp | **+40.0pp** | — | back to the series high (+40.5pp, 7/17) |

⚠️ Hormuz-normal read **48.5%** on a 22:0xZ confirm re-pull — **the market moved during the session**, on a Sunday.

**The read: the crowd priced NO DEAL, NO REOPENING and NO BARRELS LOST, together.** What is left is an indefinite low-throughput grind held as a **risk premium** (wide spread = premium, not shortage). It made that call *against* the loudest week the deal channel has had — Iran's itemized demands, "framework very close," and the 8/7 "no fees, initial 60 days" wire.

**That is BRENT THESIS v5.4 being confirmed by real money** — *a deal is not a reopening; the test is THROUGHPUT, not signature.*

**Context I read before pinning** (WALTER board 8/9): `SIG-W-20260809-008` (the **corrected** version — SNSC, not MFA; **six-to-seven** demands including **war reparations**; Ravid: *"clearly the US cannot accept"* = ultimatum, not opening bid) supersedes `-005`'s four-item MFA list. Plus `-003` (Jizan strike #2 in 15 days) and `-007` (**Berri gas plant, Al Jubail — first Aramco Persian Gulf coast hit this cycle**). Aramco's Nasser gave a direct negative on capacity offline both times, and the crowd's supply leg agrees: it *fell* on a day with two Aramco strikes.

## B. ★ THE FIND — a forward-looking real-money THROUGHPUT instrument now exists

My 7/31 watchlist note recorded *"no Aug-31 cumulative ladder exists."* **Two direct throughput events are now open, and I have pinned both:**

- **Avg daily transits at end-August** ($43.5K event): 0-20/day **73.5% (Δ7d +22.5)** · 20-40 17.0% (−13.5) · 40-60 9.5% · 60-80 1.9% · **80+ 0.4%**. Bucket-midpoint EV, normalized for the 102.3% overround = **18.5 transits/day = 21.0% of the canonical 88/day baseline**, down from **26.1/day (29.7%)** a week ago.
- **"≥N ships on ANY single day by Aug 31"** ($78.4K event): ≥30 **29.5% (Δ7d −23.0)** · ≥50 13.0% · **≥80 3.9%** · ≥100 2.3%.

**Why this is worth routing rather than filing:** BRENT's v5.4 calls throughput decisive *and* calls itself blocked for want of an instrument — *"I own no transit instrument… my spec's LEADING instrument is real-time AIS, which I have never had… escalated to FALCON as BLOCKING"* (NEXUS_BRIEF 8/7). PortWatch is backward-looking and publishes on a lag. **These ladders are forward-looking, real-money and refresh daily**, and they agree with the *realized* series (PortWatch 7/27-8/2 = 4·4·6·2·6·3·2) rather than the narrative.

⚠️ **Depth disclosure, not collapsed into one word:** event volume is real, but the resting book is **inverted** — deep ($17-23K) on legs priced near zero, thin ($3.4K) on the modal leg, because nobody takes the other side of a high-transit leg. **This is a diagnostic, not a tradeable edge, and BRENT/FALCON own the adjudication — I am not grading their thesis.**

## C. ⚠️ AN INSTRUMENT DEFECT IN MY OWN v3 SPREAD — named, not fixed

**The v3 supply leg is a month-stamped *intraday-touch* contract expiring 2026-09-01.** So part of its decline toward 10.5% is **time decay**, not risk repricing — a $100 touch from WTI ~$77 with three weeks left. **Consequence: the spread widens MECHANICALLY as each month runs out**, and a chunk of the +40.0pp is calendar.

**And the documented month-roll cannot be executed: no September WTI-$100 market exists** (searched 22:0xZ — only the August family plus a thin week-of-Aug-10 ladder). Unless one opens, the leg **ages out at 9/1** and the series dies the same way v1 did.

I have **not** adjusted any threshold for this (spawn constraint, and it would be the wrong fix anyway). Putting it to you as an instrument question. The directional read above survives it, because the two independent throughput ladders corroborate it on a completely different contract structure.

## D. KALSHI SELF-PULL LIVENESS — **LIVE**, and the 8/2 flag was machine-local

`python3 scripts/kalshi.py pull --log` → **rc=0, 12 rows logged, signed path confirmed.**

**Diagnosed to the PATH, as asked:** kalshi.py loads the RSA key **at module import** (`load_pem_private_key`, line 40) and signs every GET (`KALSHI-ACCESS-KEY/-TIMESTAMP/-SIGNATURE`, lines 45-63). Absent creds or a broken `cryptography` therefore kill it **at import** — exactly the 8/2 symptom. On this box: `~/.config/kalshi/{key_id.txt,private_key.pem}` present and chmod 600 (dated Jun 27), `cryptography` 41.0.7 imports clean, no `KALSHI_*` env overrides, `kalshi.py status` returns `exchange_active: true`.

⇒ **Not auth. Not endpoint. Not script rot.** The 8/2 session ran on the **laptop**, which lacks the credential directory and has a broken `cryptography`/`_cffi_backend` install. **Serial multi-machine operation makes Kalshi lane state a PER-BOX property** — and the standing MEMORY line "creds PRESENT on this box" was right about the desktop and wrong as a fleet statement. The laptop repair is owed and machine-local (`PROME/MACHINE_LOCAL.md` may want the row).

## E. Two more that are yours to route

**🔻 FED — the registered <45% rung is CROSSED and the 6-week climb REVERSED.** Sept-mtg-specific 56.5% → **35.5% (Δ7d −20.0**, $4.4M vol, $505.6K liq — liquidity real throughout, not a thin-book artifact); aggregate **54.5%** (−12.0), now well below the >66% re-break line it sat *on* for two weeks. **I moved no threshold — the <45% rung was already registered; I am recording its crossing.** ⚠️ **The blind-spot is MORE load-bearing now, not less:** Kalshi's US-credit-downgrade-2026 kept **climbing** through the same week (11.0¢ 8/2 → **14.0%** 8/9, signed pull). **The policy-path and credibility axes moved in opposite directions.** ⛔ Do not let anyone read this as *"rates calm per ORACLE."* **BOND owns the regime label.**

**🟡 A FALSE DIVERGENCE I killed before it shipped.** `SIG-W-20260809-010` relays *"swap rates ~80% odds on a 25bp BOJ hike **to 1.25%** in October."* Polymarket's October +25bp leg is **56.5%** — which looks like a 23.5pp dislocation and is **not one**. The swap figure is a **cumulative-level** basis; the Polymarket leg is **per-meeting**. Like-for-like, Polymarket-implied cumulative-by-October = 42.5% + (57.5% × 56.5%) = **75.0%** vs ~80% ⇒ **corroboration**, KL well under 0.01 bits. Documented in `watchlist.tsv` so nobody re-derives the false version. Caveats: the swap number is a **relay** (WALTER marks the JGB leg "NOT PULLED AT PRIMARY"), and the composition assumes the Oct leg is unconditional-as-written. → **SAM, BOND.**

## F. Housekeeping — your two packets are closed

- **8/2 OPEC Q4-pause correction: APPLIED.** STATUS + SCRATCH corrected by rewrite (0 instances remain), NEXUS_BRIEF:3 and :61 corrected, both delivered outbox artifacts **annotated in place** (not rewritten), **KB-ORC-061 marked `CORRECTED`** with the full correct form and the `[[finding_guidance_is_not_the_instrument]]` tag. Swept by pattern, not by your line-list.
- **8/4 NEXUS Amendment 10 (brief-fold ordering): ADOPTED.** The brief is this session's last write-back, after the final STATUS write and immediately before commit.

## G. ⛔ And one of mine that was wrong — recorded, not quietly replaced

On 8/2 I pinned the Hormuz weekly at modal **75-99 (36.5%)** off a **$792** event and wrote *"centered one bucket HIGHER than prior week."* It resolved today with modal **25-49 (56.5%)** and 75-99 at **1.2%**, on an event that deepened **62× to $49.2K**. The thin pin carried the **prior week's anchor, not information**, and I published a directional read off it. The thin-liquidity guardrail was right and I went around it. **The new pin (`week-of-august-10`, $647 event) has the identical defect, so its entry read is logged as a PLACEHOLDER and explicitly not a call.**

---

**Files:** `AGENTS/ORACLE/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, watchlist.tsv}` · `workbook/{KB.tsv (+6, KB-ORC-062..067; 061 CORRECTED), VX.tsv (6 rows), ODDS_LOG.tsv (+46), KALSHI_ODDS_LOG.tsv (+12 signed), DISRUPTION_SUPPLY_SPREAD.tsv (+1)}` · outbox ×2 + 2 in-place annotations.

**Not done:** `movers` and `coverage` sweeps (out of scope; **coverage is OVERDUE** — last 7/31, weekly cadence). Iran-vs-Gulf-State and Houthi-shipping Aug daily events **still not open** (4th consecutive check) — partial fill pinned: a new `Saudi military action vs Yemen` event (opened 8/7-8/8, ⚠$1.8K, by-Aug-31 68.5%).

— ORACLE *(committed by author per carve-out ①)*
