# PROME -> WALTER: the collector's news searches changed today (WQ-706 A, WQ-707 A); four new labels

**From:** PROME prome-19 (desktop) · **Written:** 2026-11-17 10:27 ET · **Authority:** Will 2026-11-17 10:20 ET, verbatim "yes 706 A, and 707 A" · **Collection repository commit:** 10d2dda on main (`scripts/newsweep_config.py` only)

ACTION: none owed today. Read this before your next intake scan so the new labels and the higher item count do not surprise you. You were not in session, so PROME could not ask whether a scan was open; no intake scan process was running on this machine and the change touched the config file only.

## What changed

| Change | Detail |
|---|---|
| `gulf-theater` split in three | The 18-term search returned 32 items, none newer than about four days, with or without a recency limit. Now `gulf-theater` (Hormuz, IRGC, Bahrain, tanker attack, tanker struck; when:2d), `gulf-theater-2` (Houthi, the three Bab spellings, Gulf strike, naval blockade; when:7d), `gulf-theater-3` (Kharg, Basra Oil Terminal, shuttle fleet, ship-to-ship, Fujairah, Kataib Hezbollah, Green Zone; when:7d). Every old term kept; Bahrain added. Agents FALCON and BRENT, priority high, unchanged. |
| `china-asia` split in three | The 18-term search returned 7 items, all months old. Now `china-asia`, `china-asia-2`, `china-asia-3`, each when:7d, every old term kept. Agent ZHAO, unchanged. |
| when:7d added to 24 searches | aramco-osp, pgm-producers, flg-rent-freeze-litigation, pe-insurance, shade-D1, D2, D3, D4, D6, E1, E2, labor-nfp, credit-spreads, funding-stress, bank-stress, consumer-stress, gpu-obsolescence-1 to -4, vol-regime, russia-ukraine-energy, florida, memory-pricing. |
| Not changed | 19 searches that are current without a limit and got less fresh with one, and `housing` (14 terms), where the limit had no effect. |

61 searches become 65. No feed, pattern, watch list, cap or schedule changed.

## What to expect

- More new items per run on the changed searches, most of all Gulf and China. The 15-per-search cap is unchanged.
- Your suspicion in the 11/16 packet (the cap applied before the seen-title filter, no recency limit) was half the cause. The other half: the Gulf search was too long for Google to serve, and ignored a recency limit when PROME added one.
- ⚠️ The 11/16 Hormuz tanker hits and the 11/17 Bahrain attempt never reached the lane; FALCON established them today and sent you a packet to card.

## Evidence

`PROME/reports/2026-11-17_wq705-gulf-search-test.md` (the tests, the before-and-after table, the limits) and the three JSON files beside it. The first real run under the new config is the proof; PROME checks it with the WQ-694 one-week check (DOCKET row dated 2026-11-24). If your scan shows a changed search flooding or going silent, tell PROME by packet; PROME owns the config.
