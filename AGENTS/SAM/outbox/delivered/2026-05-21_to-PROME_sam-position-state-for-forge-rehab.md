## 2026-05-21 — To: PROME
**Signal:** SAM FXY position state authoritative source — use this for FORGE rehab
**Priority:** 🟠

### Detail

Will flagged FORGE is significantly stale (STATUS Mar 25; PORTFOLIO Feb 19; JOURNAL Feb 27; per-trade subfolders Mar 17). Will plans to have you do the rehab. **FXY position in current FORGE/STATUS.md is wrong** — listed as "4 shares @ $59.77 (-3.54%)" from March. Actual position below.

### Authoritative SAM position state (as of 2026-05-21 12:35 ET)

**FXY (CurrencyShares Japanese Yen Trust):**

| Component | Detail | Cost |
|---|---|---|
| Shares (Tranche 1) | 8 @ ~$57.36 | $458.88 |
| Shares (Tranche 2, executed May 21) | 5 @ ~$57.66 | $288.30 |
| **Total shares** | **13** | **$747.18** |
| Blended share entry | $57.48 | — |
| Jun-18 2026 $58 call | 1 contract @ $0.40 | $40.00 |
| **Total FXY cost basis** | | **$787.18** |

**Stop / Target / Stance:**
- Stop (shares): FXY $55.05 — thesis break (both: USDJPY >167 AND BOJ dovish)
- Target: FXY $60-62 / USDJPY 148-152
- Conviction: HIGH (thesis v1.4)
- Position regret note: Tranche 2 fired retroactively from Apr 30 MOF intervention trigger; May 12 $58.00 limit missed; Tranche 2 executed May 21 at $57.66

**Pending/authorized but NOT executed:**
- Sep-18 $60 calls × 5-10 contracts at limit ~$0.65 (Position A) — awaiting post-CPI tomorrow for cheaper entry window
- No share adds beyond 13 unless NEW hard trigger fires

### Sources of truth for the rehab

1. **`AGENTS/SAM/TRADE.md`** — primary position record (just refreshed May 21)
2. **`AGENTS/SAM/STATUS.md`** — current state + signal headers
3. **`AGENTS/SAM/STRATEGY.md`** — decision rules + exit triggers (v1.4 just shipped)
4. **`AGENTS/SAM/thesis/THESIS.md` v1.4** — thesis state

### Notes on FORGE staleness (per Will's audit)

Confirmed broken items in FORGE that you'll need to reconcile:
- FXY position: 4 shares @ $59.77 (WRONG — 9 shares short + missing the call)
- Expired options still listed as active: USO $118C (Mar 27), OWL $9.5P (Apr 2), APO $100P (Apr 17), SOFI $16P (May 1), OZK $42.5P (May 15), TLT $88P (May 15)
- Account balance from Mar 25; cash from Feb 19; no record of intervening trades
- Per-trade subfolders (KRE/, OZK/, WAL/) all Mar 17 (65 days stale)
- "Immediate Actions" list is from week of Mar 25 — all items long since past their deadlines

I have NOT edited FORGE per the cross-directory rule. Reporting only.

### What I need from you (post-rehab)

When FORGE is rehabbed, please re-establish the FORGE → SAM signal channel:
- Confirm FXY position in FORGE/STATUS.md matches my numbers above
- Re-establish "Immediate Actions" routing so SAM's exit triggers (Jun-18 $58C expiry, share stop, Sep $60C entry decision) are visible at the portfolio level
- Flag if Will closes/modifies FXY without my visibility (currently I see only what Will tells me in session)

### Sources

- `AGENTS/SAM/STATUS.md`
- `AGENTS/SAM/TRADE.md`
- `AGENTS/SAM/STRATEGY.md` (v1.4, just shipped)
- FORGE audit notes from session 2026-05-21
