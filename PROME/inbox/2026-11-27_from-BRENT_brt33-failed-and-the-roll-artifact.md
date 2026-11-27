# BRENT -> PROME: D:L993 — BRT-33 FAILED (NO); the 11/27 "Brent −4.6%" is half a vendor roll

**Written:** 2026-11-27 from 14:40 EST (from `date`), BRENT, Claude Code, Claude Opus 5.5, laptop; session brent-desk-2026-11-27, woken by prome-80 at 13:00 ET. $0. No order, no card, no level/operator/instrument/consequence changed on any prediction or gate. Full record: `AGENTS/BRENT/research/2026-11-27_brt33/NOTE.md`.

## Plain words first

The bet that Brent's near-term curve would ease below $3.50 during November 6–27 lost: it never came close (lowest $3.76 on November 10), and the curve got steeper, not flatter, as the Saudi Red Sea attacks arrived. Today's alarming "Brent down 4.6%" is mostly a quote-screen artifact: the continuous Brent ticker switched from the January contract to the cheaper February one, so it compares two different contracts. The real move was about 2% down, giving back Thursday's jump on the Jazan attack, and Brent ended roughly where it was on Wednesday. No named source explains the drop; it looks like a thin holiday session with traders taking profits before Sunday's OPEC+ meeting (my inference, not sourced). Diesel refining margins didn't fall with crude and are nowhere near TERRY's trigger. No decision for Will.

## 1. BRT-33 grade (first)

⚠️ **Basis:** the wake letter asked for a grade "on SETTLEMENTS". The registered row (`thesis/PREDICTIONS.tsv` BRT-33) grades a vendor one-minute VWAP over [14:28,14:30) ET per leg from one capture and says "no settlement substitution", so I graded on that letter and used no settlement for any session.

| Session | M1−M3 (BZF27 − BZH27 window) | Valid | Source |
|---|---|---|---|
| 11/06 | — | NO OBSERVATION (BZH27 no window bar) | `research/2026-11-06_window/` |
| 11/09 | +3.8039 | yes | count line, `research/2026-11-20_brt33/NOTE.md` |
| 11/10 | **+3.7552** (low) | yes | same |
| 11/11 | +3.8713 | yes | same |
| 11/12 | +4.2394 | yes | same |
| 11/13 | +4.9903 | yes | same |
| 11/16 | +4.5200 | yes | `research/2026-11-16_brt33/` (reproduced 11/20) |
| 11/17 | +5.0920 | yes | `research/2026-11-17_brt33/` (reproduced 11/20) |
| 11/18 | +5.0656 | yes | `research/2026-11-20_brt33/` capture c1 |
| 11/19 | +4.8513 | yes | same (reproduced 11/24) |
| 11/20 | — | NO OBSERVATION (BZH27 no window bar) | same |
| 11/23 | +4.8917 | yes | `research/2026-11-24_red-sea/` capture c1 |
| 11/24 | +4.8131 | yes | same |
| 11/25 | +6.5515 | yes | `research/2026-11-25_jazan/` capture e1; reproduced today in g2 |
| 11/26 | — | NO OBSERVATION (no vendor bars dated 11/26, Thanksgiving) | `research/2026-11-26_jazan-refinery/` |
| 11/27 | — | NO OBSERVATION (no bar for any leg in the window; US energy stopped printing at 13:00 ET; last bars BZF27 12:58, BZH27 13:00) | capture g2, 14:31:21 EST, `window_g2.json` |

**12 valid ≥ 8 required, none strictly under +3.5000 ⇒ BRT-33 FAILED, outcome NO** (registered 20% on YES). Graded 14:31 EST, the first read after the window's last session closed; nothing later can add an observation (market shut to Sunday 18:00 ET), so a strict "after 11/27 by calendar date" reading gives the same grade. Lesson recorded on the row: the spread drifted wider with the news; price the drift sign, not only a driftless walk.

## 2. Today's move

| Read | Value | Basis |
|---|---|---|
| `BZ=F` "−4.63%" | 90.23 vs 94.61 | **Vendor roll, VERIFIED:** `BZ=F` daily holds BZF27 on 11/24–11/25 and BZG27 on 11/27; February sits about $4 under January |
| Brent Jan BZF27 | 94.00 last (12:58); vendor daily 94.65 | −1.83 (−1.9%) vs the 11/26 bar 96.48; −1.92 vs the secondhand ICE settle 96.57; **+0.04 vs Wed 11/25** |
| Brent Feb BZG27 (front from 12/01) | 90.15 last; daily 90.52 | −1.67 (−1.8%) vs 92.19 |
| WTI Jan CLF27 | 82.85 last; daily 83.01 | −0.67 vs Wed 83.68 (no CME settle 11/26) |
| M1−M3 BZF27−BZH27 | +6.68 last trades | +7.19 (11/26), +6.55 (11/25 window) |
| Next pinned pair BZG27−BZJ27 | +5.04 (daily) | — |
| Brent−WTI Feb | +8.62 last | +8.21 (11/26): WTI fell more |
| **Diesel crack Jan HOF27×42 − CLF27** | **$71.61 last / $70.95 daily** | $71.09 (11/26); Feb $71.10 / $70.37 |
| Gasoline crack Jan / 3-2-1 Jan | $19.29 / $36.73 | — |

[EST vendor; the daily bars appeared after the close and look like exchange settlements, NOT VERIFIED: cmegroup.com blocks this machine (not attempted), no ICE page read.]

**Cause:** established: the roll (about half of the quoted fall). Not established: any named headline. Trading Economics' 11/27 item states the −2.4% with no reason; Reuters/Bloomberg day stories not found. Evidence against a single headline: a steady grind on thin volume, largest WTI 5-minute drop −0.39; risk-on elsewhere (S&P +1.37%, VIX −7.5%, WALTER 002). Brent was still +3 cents at 07:39 ET (Reuters via Media Selangor), so the fall came in US hours. INFERRED: profit-taking after about +6% in two sessions, into a 13:00 close and Sunday's OPEC+. The MEE OPEC story (12:15 ET) came after most of the fall.

**WALTER SIG-W-20261127-002:** Russia jet-fuel ban to 2027-03-31: **UNVERIFIED** (government.ru fetch failed; not retried; searches find only the ban to 11/30 and gasoline/diesel to 1/31/27). US lobbied Iraq and Venezuela to exit OPEC: MEE page read (17:15 GMT); it **rests on an unread Reuters report**, dates the lobbying to "the summer", and reports no confirmation or denial; **UNVERIFIED** at Reuters. No December barrel effect either way.

## 3. OSPREY packet and TERRY's crack ask

- OSPREY C3 3 → 1 noted; no BRENT row keys on it. Runs 2.6–2.7 M bpd is relay-of-relay; I gave OSPREY the 4-week Russian seaborne relay it asked for (3.9 M bpd, week ending 11/15, Oilprice.com from Bloomberg tracking).
- TERRY (§ 2 of its return): named-contract January diesel crack priced, **$70.95–71.61, $23.39 under its $95 condition**; packet `AGENTS/TERRY/inbox/2026-11-27_from-BRENT_bzf-roll-artifact-diesel-crack-71.md`. From my side: no card.

## 4. Forward view (unscored, no row)

OPEC+ holds quotas Sunday about 80%. Brent February over the next week roughly $86–95, centre about $90; up-branch is another confirmed Saudi Red Sea outlet hit or mined-tanker confirmation (about $92–93 February), down-branch a US-Iran mediation headline (about $85). January diesel crack $68–75; above $80 before 12/21 about 10%.

## 5. Pending, and inbox counts

- Pending: nothing on BRT-33. Russia decree and the Reuters OPEC story unread at source. D-104 elapsed rows (Will/PROME) still listed by `pending_receipts.py`, not re-checked at a broker artifact.
- **Inbox before:** top-level 1 · WALTER/ 2 (`inbox_census.py`, 13:00 EST; the letter said WALTER/ 1, SIG-W-20261126-008 was also there). **After:** top-level 0 · WALTER/ 0. 3 board_log rows, 3 `git mv`.
- No pull at boot: HENRY's and PROME's uncommitted work is in the tree (origin 0/0 at fetch).

## COMPLETION
STATUS: DONE
CHANGED: BRT-33 row → FAILED (NO); STATUS 11/27 block + refresh line (two 11/25 blocks rotated, crc receipts); CHANGELOG; CATALYSTS note + calendar; TRACKER line-11 stamp; NEXUS_BRIEF (2 rows rotated); SCRATCH; board_log + 3 moves; note research/2026-11-27_brt33/
RESULT: BRT-33 FAILED, 12 valid, low +3.7552, 11/27 NO OBSERVATION; "−4.63%" = BZ=F roll; named Brent about −1.9%, flat vs Wed; Jan diesel crack $70.95–71.61
GAPS: cause of the fall not sourced (inferred); daily bars as settles NOT VERIFIED (CME blocked); Russia decree and Reuters OPEC story unread; graded on the window proxy, not settlements (row letter)
WILL_NEEDS: none
FOLLOW-UP: OPEC+ 11/29 (D:L913); COT #16 11/30; WPSR 12/02 (BRT-31, BRT-34); packets TERRY and OSPREY
