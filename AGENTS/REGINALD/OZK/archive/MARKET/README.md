# OZK — MARKET

**Created:** 2026-03-24

Trading, positioning, and market context for OZK. This is the action side of the thesis — THESIS.md says *what* and *why*, this folder tracks *when* and *how much*.

---

## File Instructions

### POSITIONS.md
Live position tracker. Every open put/call gets logged with:
- Ticker, strike, expiry, direction (long/short)
- Entry date, entry price, cost basis
- Thesis link (which wave/catalyst this targets)
- On close: exit date, exit price, P&L, notes

One position per entry. Keep closed positions below a `## Closed` section — don't delete them, they're the track record.

### TRADE_LOG.md
Timestamped decisions and rationale. Brief entries, not essays. Format:
- **Date** — what we did and why
- Link to the specific thesis element driving the trade
- What would make us wrong

This is how we stay honest. If we entered because of Wave 1 and Wave 1 didn't play out, the log shows it.

### CONTEXT.md
Market-moving days that affected OZK price without changing fundamentals. The "why did it move" file.
- Date, direction, magnitude
- Cause (sector rotation, relief rally, squeeze, etc.)
- Signal or noise? One sentence.

### /snapshots/
Chart images saved with descriptive filenames: `OZK_[timeframe]_[date].jpg`
Example: `OZK_1h_20260324.jpg`

Keep brief annotations in TRADE_LOG.md referencing the filename — don't write analysis in the image folder.

---

## Frameworks (Reference)

**Hamilton expiry logic:** PC single-name puts (APO, ARES, ARCC) use May/Jun/Jul for dateable catalysts. Macro/index (HYG, KRE, IWM) use Dec. OZK puts: May for Wave 1 (April 16 earnings), Aug for Wave 2-3 (maturity wall grind).

**Green day rule:** Enter or roll positions on up days with no fundamental catalyst. Relief rallies compress vol = cheaper premiums.

**Squeeze survival:** 14-15% SI, 12-18 days to cover. Size max 3-5% of account per put. Accept that green days will hurt. The thesis is trajectory, not any single print.

---

*Thesis → `../THESIS.md` | KB → `../workbook/KB.tsv` | Earnings prep → `../EARNINGS_PREP.md`*
