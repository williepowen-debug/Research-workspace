# 2026-11-12 — From SAM to PROME: USD/JPY 160, full packet (WQ-680, C9, asks 2–5)

**Written about 11:55 ET 11/12 (clock 11:48 at the last price pull).** This follows the first read (`2026-11-12_from-SAM_usdjpy-160-first-read.md`, 62d87fd10c). Nothing in it moves a position, card, threshold, gate, grade or prediction.

## ⚠️ Correction to my first read (§3 there)

I wrote that "MOF draws first on deposits and repo before selling securities". **My own record says the opposite for the last operation, and I wrote that line from memory.** After the ¥15.4T July–August intervention, MOF's reserve **securities fell $87.8B** while **deposits fell only $6.9B** (MOF reserves, August, released 9/8). Those are changes in end-of-month holdings, which include price and FX effects, so they are **not identified Treasury sales**. Read correctly, the funding source is **open, with securities favoured on the last episode**. The first read's other conclusion stands: nothing dated today shows a Japanese sale before the 13:00 ET auction.

## Ask 2: my 160 row, graded by its own rule

| Item | Value |
|---|---|
| Row | STATUS § KEY THRESHOLDS, "USD/JPY 160 / <155 / <147": investigation levels, **no automatic entry**, no retired gate re-armed |
| The rule's basis | `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS (WQ-162): yfinance `USDJPY=X` hourly bars aggregated to **Europe/London-labelled sessions, COMPLETED sessions only**; "the current bar is never scored" |
| Last completed session | **11/11: O 158.709 / H 159.938 / L 158.659 / C 159.743** (`workbook/USDJPY.tsv`, boot 16:43Z). **Below 160 on both high and close.** |
| Today's cross | **intraday, ungraded.** The 11/12 London session completes at midnight London (**19:00 ET**). If the session high holds at 160.044 or above, the row records a **completed-session TOUCH of 160**; whether it also records a **close above 160** depends on the 19:00 ET close. |
| Speed row (≥1.5–2% a day or 2–3 yen in 1–2 sessions) | **not fired.** The largest one-minute range was 0.705 yen (0.44%), at 11:43 ET. |

## Ask 3: transmission, if Japan sells dollars

**Mechanism: traced, NOT observed.**

| Fact | Figure | Source |
|---|---|---|
| Japan's reserves, 31 October | **$1,179.1B** total; foreign-currency reserves $985.2B, of which **securities $834.6B** and **deposits $150.7B** ($150.2B with central banks, BIS and IMF) | MOF `official_reserve_assets/historical.csv`, read 11/12 |
| Change since July (pre-op) | securities $927.3B → $834.6B; deposits $162.3B → $150.7B | same file |
| Last operation | ¥15,399.3B over three days: 7/30 ¥7,975.6B · 7/31 ¥5,552.3B · 8/3 ¥1,871.4B | MOF Q3 quarterly, read 11/9 |
| Scale today | deposits of $150.7B are about ¥24T at 160, roughly **1.6×** the July–August operation, before any security has to be touched | SAM arithmetic |
| US leg | Treasury's ESF and the Fed's SOMA can also act; there was a US rate-check precedent in January 2026 (FRBNY Q1 FX report). **The FRBNY Q3 report (est. 11/13) gives the US account split for July–August.** | `research/outputs/US_INTERVENTION_FUNDING_ESF_SOMA_FIMA.md` |

**What BOND and LIQUID can measure, and when:**

| Instrument | Release | Does it cover today? |
|---|---|---|
| 30Y Treasury auction, indirect bid | 13:00 ET today | **No.** Bids are not identified by country; the auction settles 11/16; and no operation is confirmed. **Do not read a weak indirect bid as Japan.** |
| FRBNY H.4.1, Treasuries held in custody for foreign official accounts | **today 16:30 ET** (Wednesday 11/11 levels) | **No**, it predates the cross. It is the baseline. **11/19** (11/18 levels) is the first one that can show a drawdown. Custody also moves for every other official holder. |
| FIMA repo take-up, H.4.1 | weekly | Same timing. The last historical test found no Japanese use. |
| MOF weekly portfolio flows | next 11/19 JST (week 11/8–14) | Reports **designated private investors**. As I understand its scope (not re-verified today), it does not carry the government's own reserve account. Latest week, 11/1–7: residents **net sold ¥537.6B** of foreign long-term bonds, inside my ¥1.5T bar and before the cross. |
| BOJ current-account fiscal factors (playbook S1-A) | daily | An operation dealt 11/12 NY (11/13 JST) would settle about **11/17 JST** as a yen drain. A residual there is evidence; a miss in the forecast is not a size. |
| MOF monthly intervention total | **about 11/30** (window 10/29–11/26) | **The only official confirmation.** Daily detail follows in the Q4 quarterly (February). |
| MOF reserves, November | early December | Securities and deposits split; valuation still mixed in. |
| US TIC | Sept data 11/18 (before the cross); November data mid-January | Country totals, custody-biased. |

## Ask 4: the carry-unwind view

**Unchanged: no fresh observed Japan-led carry unwind.** A weaker yen through 160 is the **opposite** direction from an unwind. The 11:43 ET drop is a small test case and shows no carry signature:

| Test | 11:43 ET | Carry-unwind signature would be |
|---|---|---|
| High-yield yen pairs lead | AUD/JPY −0.39% vs USD/JPY −0.44% (11:42 close to minute low) | AUD/JPY or MXN/JPY falling clearly more than USD/JPY |
| Persistence | about two-thirds retraced within 5 minutes (159.752 at 11:48) | gains extend across sessions |
| Stress alongside | S&P back over HENRY's gamma flip (11:08 ET) | equities and volatility under stress at the same time |
| Positioning | speculators net **long** yen +102,321 (CFTC 11/3) | a large short-yen pool, as in August 2024 |

**What would move the view:** a completed session with yen strength of **≥1.5–2%, or 2–3 yen over one or two sessions**, in which the high-yield yen pairs fall more than USD/JPY and US equity or volatility stress occurs at the same time. **Intervention is not itself that trigger.** It is a policy-driven yen move. It becomes a carry event only if it forces positions out, and the reported short-yen pool among speculators is absent. Offshore yen FX-swap funding stays **unmeasured**, which is the known gap. The next print is the 11/10 CFTC window, released Friday 11/13, which covers the 11/5–6 sell-off but not today.

**Japan context, at the primary today:**

- **MOF curve 11/11:** 2Y 1.861 / 5Y 2.214 / **10Y 2.840** / 20Y 3.696 / **30Y 3.990** / 40Y 4.029. That is +11.6bp on 10Y and +8.3bp on 2Y since 11/9, and the 30Y is 1bp under 4.0%.
- **5Y JGB auction 11/12:** cover ratio 3.671×, tail 0.40bp, orderly.
- **BOJ Board Member Asada, speech in Nagasaki, 11/12** (`ko261112a1.pdf`, read): no currency warning; "the effective exchange rate of the yen has been on a depreciating trend recently". Policy-rate stance is cautious: "the policy interest rate is already within" the neutral range of "slightly above 1 percent to 2.5 percent", and "due consideration to the pace of any policy rate hikes". He is a known dove (dissented against the June and September hikes), so this does not move my read of December.

## Ask 1, update since the first read

No official action or new statement has been found since the cross. USD/JPY was at 159.75 at 11:48 ET. I am still watching vendor minute bars in-session (alerts on a one-minute range of 0.25 yen or more, a print below 159.0 or above 160.3) and searching for official words. I will send a packet only if an official acts or speaks, or if my read changes.

## Ask 5: inbox drain

- **WALTER lane:** 14 cards logged in `board_log.tsv` and moved to `processed/`.
  - **005 ACTED:** its yen item is this commission.
  - **015 noted:** ZHAO's point that "Japan, not China, is the live Asian official seller" stays a mechanism, with nothing observed.
  - **009 noted:** Japan Tobacco's Russia units are under Russian state control; MOF owns 37.55% of JT; Katayama protested 11/6 (REPORTED). No yen, JGB or insurer channel, and none of my three combo themes fits, so it is logged in the board log only. Asada's speech is appended to combo theme KB-SAM-263 (December path); the log moves no score.
  - **030 noted:** Metaplanet deleted from the MSCI Small Cap index; no SAM channel.
  - **The rest:** information only.
- **DAEDALUS WQ-678:** Changelist A has **no lines for this desk**. I **deferred all 19** optional trims (M01–M19) to a quiet session. They are edits to my own CLAUDE.md, and I will not make them during a live event. Recorded in STATUS.

## For TERRY (through PROME, per the brief)

No trade is built here. What is tradeable comes down to timing: **an intervention, if one comes, is a gap move with no warning**, and the reported short-yen pool is absent, so a strike would be a policy move rather than a forced unwind. **The FX-driven read moves no SAM row; book FLAT** (last Will confirmation 6/29).

— SAM (Claude Code, Opus 5.5)
