# ISHM — R1 successor encoded (WQ-643 A)

**Written:** 2026-11-06 20:41 ET, Claude Code, Opus 5.5. **Ruling:** PROME/proposals/2026-11-06_wq642-644-RULED.md; packet filed at inbox/processed/2026-11-06_from-PROME_WQ643-A-RULED-R1-successor.md.

## December 1 date, primary source

| Item | Result |
|---|---|
| Source | S&P Global PMI calendar, `https://www.pmi.spglobal.com/Public/Release/ReleaseDates`, the issuer's own page |
| Read | Ordinary GET, HTTP 200, November 6, 20:39 ET; copy at `sources/pmi-spglobal-calendar_2026-11-06.html`, sha256 `df30da43d12faf458173fec2c081601ee20b5b257da3fd1a85344bc2f95e9b25` |
| December 1 entry | "December 01 · 14:45 UTC · S&P Global US Manufacturing PMI" = 09:45 ET (EST, UTC−5). The page states its schedule: "Manufacturing PMI: first working day" |
| November 23 entry | "November 23 · 14:45 UTC · S&P Global Flash US PMI" = 09:45 ET, also PRIMARY now |
| Basis | PRIMARY-VERIFIED as a schedule. The page does not label the December 1 row "final"; it is the only non-flash US manufacturing row in the window, and the issuer lists the flash separately |

The caveat shown to Will, that December 1 was secondary, is cleared. PROME's DOCKET row still says "date secondary, confirm it first"; that row is PROME's to update.

## What changed in the letter

| Element | October letter | November letter |
|---|---|---|
| Reference month | October | November |
| Date | scheduled November 2 | scheduled December 1 |
| Comparison month, toward-real branch | September | October |
| Source named | dated October final issuer PDF | dated November final issuer PDF |
| Corroboration | September M3 October 27; October ISM November 2 | October advance durables November 25; November ISM December 1 |
| Date basis sentence | secondary until issuer calendar confirms | PRIMARY, issuer calendar November 6 |

Branch tests, limits, FROM state and grading rule are word-for-word unchanged. A token diff of the two tables shows only the swaps above. The October letter is kept verbatim in `workbook/EXIT_PROTOCOL.md` beside its two grades, marked NOT LIVE. No score, band, gate, threshold or other letter moved; ISM <47 is untouched.

## Caveats that travel with the letter

| Caveat | Why it matters |
|---|---|
| ⚠️ The comparison base got softer | October's final had new work at its slowest since March, so "faster than October" is an easier bar than "faster than September" was. The toward-real branch still needs output faster and the issuer saying demand broadened beyond precautionary stockbuilding, so a bounce alone does not fire it |
| ⚠️ Grade rests on issuer prose | The October release published no numeric sub-indexes (STATUS, November 2 row). If the November text does not state the composition, the branch is CANNOT-FIRE, never benign |
| ⚠️ One print only | After the December 1 grade R1 has no live print again unless a branch fires or Will rules another successor; the letter does not roll by itself |
| The date is a schedule | An issuer slip re-dates the docket row; the observation stays the November final |
