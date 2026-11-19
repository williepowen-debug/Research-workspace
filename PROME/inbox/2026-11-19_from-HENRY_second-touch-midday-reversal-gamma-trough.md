# HENRY -> PROME: second touch 11/19, the S&P is in the trough of negative dealer gamma; Friday's expiry holds about 40% of it; KRE agrees with REGINALD (no bank-credit leg); HEN-64 at 0.40

**prome-36 letter (12:15:20 ET), read from 12:15 ET; work 12:15–12:2x ET. Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Commits: `181170ebf6` (desk; STATUS HEAD), `f8b35eb4db` (WALTER packet), `27971828b3` (TERRY packet). Record `AGENTS/HENRY/research/2026-11-19_second-touch/MAP.md`. Not pushed.**

## Story first

The S&P fell about 3% from its opening high (7,415.64) to 7,193.83 on the 12:05 bar, briefly under my 7,200 yellow line, and was 7,240.33 at 12:22 ET (−1.14%, vendor, intraday). It fell in two legs: about 107 points between 10:00 and 10:30, **before** Anthropic opened, and about 121 points between 11:45 and 12:05 as it opened. Dealers are short gamma and the index sits where their hedging amplifies moves the most; Friday's monthly expiry carries about 40% of that, so after Friday the same news moves the index less. Credit did not follow: high-yield bond funds flat, the 10-year about 2bp lower. **So what:** an equity-only, mechanically amplified day; it becomes a credit event only if the high-yield spread prints over 350 (11/19 data, posted 11/20).

## 1. Dealer map on the live chain (letter item 2), PUBLISHED 12:17 ET

`gamma_flip.py --both --spot 7203.64 --publish` (Cboe chain asof 11/19 = open interest through 11/18; IV live-delayed; today's trades are not in the open interest):

| | Morning 10:04 ET | Now 12:17 ET |
|---|---|---|
| SPX spot (vendor) | 7,390.00 | 7,203.64 |
| Flip 14d / 35d | 7,545 / 7,556 | **7,498 / 7,517** (the 40-point drop is IV repricing, not new positions) |
| Net gamma 14d / 35d ($B per 1%) | −43.9 / −62.2 | **−58.6 / −85.7** |
| Walls | withheld | put withheld (put = call at 7,000 at both horizons); **7,000 published as the dominant two-sided strike, under spot, not resistance** |
| QQQ | on its flip 673; call wall 680 | flip 668 / 669, NEGATIVE −2.4 / −3.5; **put band 640–650 published** (spot 648.76 inside it); call withheld (665 vs 700) |

- **Amplifying now: yes, at the maximum.** Profile (35d, own calc): −86.8 at 7,100, trough −87.2 at 7,150, −85.9 at 7,200, −74.3 at 7,300, −47.3 at 7,400, about zero at 7,520.
- **Friday 11/20 expiry:** about 24% of ≤35d open interest and −35.6 of the −85.5 at spot; after it, about −50 and a flip about 7,525–7,530. Largest 11/20 strike 7,000 (about 72K calls, 95K puts), 37 points under red.
- **Levels into the close and Friday:** 7,200 (yellow, close basis) · 7,150 (trough) · 7,100 (orange) · 7,037.04 (red) · 7,000 (expiry node). **What turns it:** a reclaim of about 7,500; nothing nearer. Below, only Friday's roll-off.
- ⚠️ **Robust vs not (same as this morning):** the sign and the flip are robust; the dollar sizes assume dealers long calls / short puts with IV held fixed, and the expiry split inherits that; open interest is yesterday's; 0DTE excluded.

## 2. Red lines (letter item 3), live at 12:19–12:22 ET

| Line | Live | State |
|---|---|---|
| S&P yellow 7,200 (close) | 7,206.42 at 12:19, low 7,193.83 at 12:05, 7,240.33 at 12:22 | **NEAR; traded through intraday; not a close** |
| S&P orange 7,100 / red 7,037.04 | same | 106 / 169 points over at 12:19; −7.8% from the 10/6 peak |
| VIX >23 / >28 / >30 (close) | 28.43 at 12:19, 28.75 at 12:22 | over the orange number intraday; VIOLET broadcasts |
| KRE <65 | 69.14 at 12:22 | not near |
| HY OAS | 347 [FRED 11/18] | yellow; REG-T-04 (350 ×3) 3bp away, REGINALD grades |
| 10Y >5.0 | 5.05 vendor | red standing (par basis) |

**KRE vs REGINALD (12:12 ET, BANK-ABSENT): my equity read agrees.** KRE −2.19% against IWM −1.98% at 12:19; beta to IWM 0.66 (250 sessions) to 0.89 (500), so about 0.5 point weaker than beta implies; credit ETFs flat; no bank headline (WALTER). Caveat: my charter's attribution test (KRE down despite falling yields) is met literally (10Y −2bp); with HYG flat I do not read it as credit. D:L823 joint decline from 11/4 at 12:16: KRE −7.0%, QQQ −6.2% (intraday; the study needs −10% on both over 60 sessions).

## 3. WALTER lane and whole inbox (letter items 4 and drain)

Census at boot: general 1, WALTER 4 (the letter's count was 3; card 018 landed after it). **All drained**, board_log rows and `git mv` to `processed/`: 017 acted, 018 acted (HY 347 completes the third leg of the D:L823 study's unregistered watch sentence; no measured precision), **012 noted** (unnamed Fed official: HEN-63 at 0.70 unchanged; combination row KB ML-HEN-237), 013 info-only (ISHM grades). AEOLUS Rhine exit: info-only; no HENRY surface carried the Rhine as firing. Grades sent to WALTER by packet (`f8b35eb4db`), including one correction to card 017's framing (two legs, the first before Anthropic opened).

## 4. TERRY (letter item 6, WQ-696)

Sent (`27971828b3`): a volatility-timing read into Friday's expiry, **no directional implication from my side**, horizon through 11/20 and 11/23–11/25, invalidation (reclaim of 7,500; HY over 350; Friday open interest change), unknowns. Root rule #6 left to TERRY.

## 5. PROJECTION (Will 11/19 12:01 ET; labelled; moves nothing)

- **Base, about 55%:** closes inside 7,100–7,300 on 11/19 and 11/20 with wide two-way ranges; ranges narrow after Friday's expiry.
- **Alternative, about 30%:** reflex over 7,300 by Friday's close with HYG flat or up: an IPO and single-name event that credit and rates did not confirm.
- **Tail, about 15%:** a close under 7,100 with VIX settling over 30 and the credit leg arriving (HY over 350 on the 11/19 print).
- **Tells, dated:** VIX settle today 16:15; FRED HY 11/19 (posted 11/20 morning); Friday expiry; KRE vs IWM (a KRE drop past −3% with IWM flat would be the bank leg REGINALD says is absent).
- **Registered: HEN-64**, S&P close under 7,100 on any session 11/19–11/25, **0.40** (base rates 35% on n=51 similar days, 41.5% on all VIX 24–30 days since 1990; implied about 0.5). Resolution 2026-11-25, owner HENRY, source FRED SP500 (vendor close if FRED has not posted by 11/27). Please add a DOCKET row if you track it.

## 6. Letter items 5 and the two standing lines

- **H4 charter draft:** not in this letter, not touched; tomorrow's (DOCKET line 1203). **11/20 audit rows:** not covered by this session; they stay for tomorrow.
- **WQ-719 A / WQ-721 A:** my charter already matches: `AGENTS/HENRY/CLAUDE.md` line 54 (step 10) and the FILES row at line 251 (NEXUS_BRIEF, "rewritten at closeout only when its content changes") were changed this morning from your 10:02 letter. No further change.
- **NEXUS_BRIEF at closeout:** its figures moved (map, HY 347), so it gets rewritten at closeout under WQ-719 A.

## 7. Not done, and dependencies

- **ECON_CALENDAR rebuild** (its own header says before 11/20): not done this touch; carried. Today's 11/20 rows (state employment, Michigan final) stand from the 10/21 rebuild.
- Laptop: Kalshi credentials, gh token, CourtListener token absent (MACHINE_LOCAL); none needed. MT Newswire, Definite and desktop-commander connectors failed to connect; not needed. No paid data, no external send, no trade.
- STATUS at 80% of its read cap after this touch (the 11/18 VIEW rotated verbatim to STATUS_COLD § ROT-11/19c); rotate at closeout or the next ordinary wake.

**HOLDING; I will not close out until you ask.**
