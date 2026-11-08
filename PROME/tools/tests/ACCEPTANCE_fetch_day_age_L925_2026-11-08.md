# Acceptance: fetch.py `day` branch wall-clock age, DOCKET L925 (open half), written before the edit

**Defect:** `futures_bar_session` never compares the last-trade time with the clock. A futures bar dated today whose last trade was at 09:00 prints as a clean `day` row all afternoon, so a frozen vendor feed reads as live. Source: `PROME/reports/2026-11-05_L920-independent-read-2.md` finding 3 (fixture-verified; live worst age 29.1 minutes on 11/5). The 11/7 pass added only a fixed "about 10 minutes behind" note, which does not carry the row's own age, so the reader's proposed closure ("carry the age in the row") was not met.

**Conditions**
1. Every futures row that reaches a session decision carries `last_trade_age_min`: minutes from the last trade to the fetch time, one decimal, in the data and the JSON.
2. A `day` row whose bar is dated today (ET, from the clock) with a last trade more than 45 minutes old is marked in the table stamp (`⚠<N>m old`) and gets a note line saying the feed may be frozen and the row is not a live quote. The price and the change are kept (fail-safe direction as L409: the price is never nulled).
3. A `day` row with a last trade at or under 45 minutes old prints exactly as before.
4. Rows dated before today keep their `⚠stale` mark and gain no age mark; evening, non-session and unverified rows keep their current marks. Equities are untouched.
5. A negative age (vendor clock ahead of ours) is never flagged as old; the value is still carried.
6. The 45-minute limit sits above the 29.1-minute live worst case and the 10-minute median, and is named in the code as one constant.

**Neighbours:** Ordinary: a 09:00 last trade read at 13:00 on the bar date is flagged (condition 2). Overlap: a bar dated today with a prior-bar gap, where the stamp must keep both `⚠gap` and the age mark. Wrong owner: N/A, a FORGE tool owned by PROME. Missing information: no clock is injected on the CLI path, so `time.time()` is the basis; the 120-second price cache can make the carried age up to 2 minutes low (declared, below the limit's margin). Concurrent activity: N/A, no shared state added.

**Declared basis:** between 17:00 and 18:00 ET (CME daily halt), and after an exchange early close, a bar dated today can be flagged although the feed is not frozen. The mark then states a true fact (the last trade is that old), not a false one.

**State:** written before the edit, 2026-11-08 13:3x ET, prome-bf.

**After the counterexample read (one independent Opus read, 2026-11-08; ❌ 1, ⚠️ 4):**
- ❌1 fixed: condition 2 is narrowed to a clock before the 17:00 ET day-session close on the bar date. The "Declared basis" above was false by omission: without the narrowing, every futures row flagged after a Friday 17:00 close and in the daily halt. Two tests added.
- ⚠️5 fixed: the stamp rounds the age up, so a flagged 45.9 prints `⚠46m old`, never a clean-looking 45. One test added.

**Declared residue (not fixed):**
- Grains and cotton (ZC, ZW, CT) close at 14:20 ET. Their rows flag from about 15:05 to 17:00 ET on a normal day. The mark is true (the last trade is that old) but the "may be frozen" wording does not fit.
- Thin deferred contracts can pass 45 minutes without a trade during the day session and flag.
- A feed frozen since the previous evening stays `evening-next-session` and carries its age in the JSON only, with no table mark.
- `unverified` rows carry no age.
- `dashboard.py` and `snapshot --json` do not show the mark or the age.
- The gap-plus-age stamp is wider than the As-of column.
- An age carried from the 120-second cache can be up to 2 minutes low.

**State after the fix:** IMPLEMENTED and TESTED (11 new tests; the 62 existing tests pass). The ❌1 fix came after the only read, so this is not independently verified.
