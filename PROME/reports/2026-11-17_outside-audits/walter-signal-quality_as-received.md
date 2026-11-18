# Are WALTER's signals any good? Accuracy, speed and duplicates

**Date:** 2026-11-18. **Repo read:** `master` at `78ed22bb9d` (2026-11-17 18:44 ET). Read only; nothing in the repository was changed.
**What was measured:** all 2,229 signals on `BOARD/` (April 10 to November 17, 2026), plus a random sample of 39 checked one by one against their sources.
**Labels:** **CHECKED** = I compared it to the source myself (web page, SEC filing, or the repo file the signal cites). **COUNTED** = computed by script over all signals. **INFERRED** = my judgement.

## The short answer

WALTER's signals are accurate on the facts they report. In the sample, the core claim matched the source in 32 of 33 signals I could check (97%). The one miss was the Saudi signal, and WALTER corrected it 73 minutes later.

The weak spot is labels, not facts. When WALTER gets something wrong, it is usually the right number with the wrong label: production called supply, an intraday price called a close, a 60-day measure called 90-day, a first-half figure called a quarter. Four of the sample's 33 checkable signals carried a minor slip of this kind that nobody had corrected.

Corrections are rising. 9% of signals since July have been named in a later correction, and in November it is 15%. About 6 in 10 of those fix WALTER's own errors. The rest fix outside headlines or desk work, or record that the world moved.

Speed is mixed. Breaking news (Iran, OPEC, Reuters wires) lands within hours. Scheduled filings and articles often land one to seven days late, and the slowest case was 27 days. The typical signal lands about a day after its source.

There are almost no true duplicates. What looks like duplication is chains of same-day updates on one story, about 1 signal in 9.

## 1. Accuracy (sample, CHECKED)

**How the sample was drawn:** 39 signals picked at random, spread by month in proportion to volume (`data/sample.tsv`, seed 20261118). Correction notices were left out of the draw. For each signal I checked the headline claim and its key numbers against the source.

| Result | Signals | Share of the 33 checkable |
|---|---:|---:|
| Accurate | 28 | 85% |
| Accurate core, minor slip (label, period, or a small figure) | 4 | 12% |
| Material error | 1 (Saudi, corrected in 73 min) | 3% |
| Could not be checked (X screenshots, chart images, no factual claim) | 6 | not counted |

The per-signal grades are in `data/sample_grades.tsv`.

**The four minor slips nobody had caught:**

| Signal | What it said | What the source says |
|---|---|---|
| Foreclosures, Aug 12 (`SIG-W-20260812-003`) | "Q2 internals: foreclosure starts +18%, bank repossessions +33%" | ATTOM's +18% and +33% are **first-half, year-on-year** figures. There is no Q2-only figure. The Q2 total of 115,714 and the 563-day timeline are right. This signal's own subject was two series mislabelled as one. |
| Wells Fargo, May 11 (`SIG-W-20260511-026`) | Loans to nonbank lenders of $212.13B, 21% of loans | The Q1 call says "approximately 210 billion dollars, or 21%". The 21% and the fraud loss match. The $212B comes from an S&P call-report figure, so this is a basis mix, not an invented number. |
| Big Tech capex, Jul 27 (`SIG-W-20260727-012`) | About $787B of market value erased | The one source I could read says $797B. The other figures match. |
| Iran, Sep 1 (`SIG-W-20260901-014`) | Iranian Army claimed a drone strike on Sheikh Isa, Bahrain | Right. Tasnim's same statement also named two UAE bases (Al Dhafra, Al Minhad), which the signal left out. |

**Hedging is strong.** Most signals state what was not read and what is only a claim, such as "claim-only", "WALTER did not open the report", or "not a completed transit". That is why the Optimizely signal (Nov 17) could be partly corrected without anything it presented as fact being withdrawn. One habit stands out, though. That signal carried exact counts (178 organisations, 32 banks) from **search summaries of pages WALTER did not open**. The page I reached described a different Optimizely incident, so I could not confirm the counts.

## 2. Corrections across all signals (COUNTED)

WALTER has a formal correction format (`signal_type: correction`, with a `corrects:` field naming the target) since August 3. Some July corrections were back-filled.

| Month signal was sent | Signals | Later named in a correction | Share |
|---|---:|---:|---:|
| April–June | 415 | 0 | 0% (correction format didn't exist yet) |
| July | 232 | 10 | 4.3% |
| August | 204 | 21 | 10.3% |
| September | 261 | 33 | 12.6% |
| October | 777 | 55 | 7.1% |
| November (to 11/17) | 340 | 50 | **14.7%** |
| **All** | 2,229 | **169** | 7.6% (9.3% since July) |

**Time from signal to correction** (182 signal-and-correction pairs): the median is **2.7 hours**. 54% were fixed within 6 hours and 71% within a day. 14 took more than a week.

**What the corrections fix** (30 corrections read at random, INFERRED classification):

| Cause | Of 30 |
|---|---:|
| WALTER's own error | **17** |
| An outside headline WALTER relayed or caught (e.g. a stale "subprime auto 6.9%" headline) | 2 |
| A desk's work (e.g. OTTO retracting its own thesis) | 5 |
| Not an error: the world moved, or a newer figure arrived | 4 |
| Routing or operations | 2 |

Of WALTER's 17 own errors, **12 are label or basis errors**: wrong period, wrong session, intraday vs close, production vs supply, 60 vs 90 days, a paraphrase quoted as the filing's words, a rank or date misread. The other 5 are framing that went further than the source. None was an invented event.

**Who catches them:** mostly the receiving desks (HENRY, VULCAN, BROCK, LIQUID, BRENT) or Will. That is the system working. It also means the errors leave WALTER and are caught downstream.

**Scale, INFERRED:** about 6 in 10 corrections are WALTER's own errors. Applied to 169 corrected signals, that is roughly 100 signals, about 5% of everything WALTER sent since July. That is in line with the sample's 1 material error and 4 minor slips in 33.

## 3. Speed (sample, CHECKED where the source time is known)

I estimated hours from the source's publication to WALTER's dispatch for 34 sampled signals.

| Delay | Signals | Typical cases |
|---|---:|---|
| Under 6 hours | 10 | Iran statements, the OPEC report, Reuters wires, Trump posts, the Cboe close |
| 6 to 48 hours | 16 | Data releases, SEC filings, overnight articles, Will's screenshot batches |
| Over 48 hours | 8 | See below |

**Median: about 29 hours.** For breaking geopolitical and energy news the median is under 5 hours.

**The slow ones:**

| Signal | Delay | Why |
|---|---|---|
| Wells Fargo nonbank-lending book (`20260511-026`) | **27 days** after the April 14 call, yet sent at IMMEDIATE precedence | Found by a later extraction pass |
| Florida metros losing population (`20260626-027`) | ~17 days | Will re-sent an old post |
| Trepp Denver watchlist (`20261027-044`) | 7 days | Batch processing of saved articles |
| Alphabet and Tesla capex shock (`20260727-012`) | ~4.5 days | **WALTER flagged this itself:** a session on the day of the sell-off sent 19 signals and missed it |
| Bessent "I am the house now" (`20260914-016`) | 5 days to confirm | It was on tier-1 outlets on 9/9–9/10. WALTER held it as unverified until 9/14. Caution that cost speed. |
| Suez FE1 return (`20261005-001`) | 4 days | Article read late |

**What drives delay (INFERRED):** WALTER works in sessions, not around the clock. When Will drops a screenshot, the signal often goes out within minutes (UBS: 2 minutes after Will's message). Anything that arrives between sessions waits for the next boot. Scheduled events (earnings calls, monthly reports) are not reliably picked up the day they print.

## 4. Duplicates (COUNTED and CHECKED)

- **Pure duplicates (the same fact sent twice with nothing new): none found.** The sample had none. A scan for pairs of signals within 2 days sharing 3 or more named entities found 192 pairs. Of 25 read at random, none was a pure repeat, and about 3 restated an earlier fact alongside new material.
- **Same-day update chains are the real pattern.** About **11% of signals** (224 of 2,032 non-correction signals; a rough text match, INFERRED) are updates or companions to a signal sent the same day. Examples: three signals on one UK gilt reading on October 8; a separate signal for each day of a four-day SKEW count (2 of 4, then 3 of 4, then fired); two cards on CF Industries' results on November 5. Each carries something new, but each lands in every recipient's inbox.
- The pre-send filter is doing its job. `filtered/kill_log.tsv` holds 1,017 killed items, 162 of them with a duplicate reason.

## 5. Worst examples

1. **Saudi output, November 11 (`SIG-W-20261111-001`).** WALTER set Saudi Arabia's self-reported **production** (10.563 million barrels a day) against Bloomberg's **supply** survey (9.2) as two rival readings 1.36 apart. The two measure different things. Saudi's own supply figure was 9.203, matching the survey. WALTER had not opened the OPEC report (opec.org is blocked to its machine). **Will opened the PDF**, and the correction (`-013`) went out 73 minutes later and reached BRENT, TERRY and HAWK. The headline it misread ("Saudi output surged 26%") was itself true.
2. **Micron's earnings date, July 30–31.** Four signals named "MU 8/4" as the event that would settle the question. Micron actually reported around September 29. Corrected August 7 (`SIG-W-20260807-001`).
3. **Apartment-loan delinquency basis, May 11 to August 13.** A signal called Fannie and Freddie's serious-delinquency measure a "90+ day" series, in its title and body, and built a comparison on it. Both issuers define it as 60+ days. It stood for **3 months** (`SIG-W-20260813-010`).
4. **An inverted interest-rate comparison, August 9 to 26.** A signal said real rates were higher now than in 1999 while quoting 2.43% against 3.8%. Its conclusion, that valuations were worse than the dot-com peak, was withdrawn when HENRY caught it 17 days later (`SIG-W-20260826-005`).
5. **A source's paraphrase quoted as the filing's words, August 28 (Nvidia).** WALTER called this one "the defect is mine" (`SIG-W-20260904-001`).
6. **Uncaught today: the foreclosure period labels (`20260812-003`), above.**

## 6. Other observations

- **Readability dipped in October.** 155 of 777 October signals (20%) glued words and numbers together ("MondayOctober19", "across444 sites"), breaking the fleet's own writing rule. It was 0% before September and 3% in November (COUNTED, rough pattern match).
- **Volume tripled in October** (777 signals against 261 in September). The correction share fell that month and rose again in November. I can't say whether October's errors simply haven't been found yet (INFERRED).
- **The record is honest.** Corrections name the error, its direction (holds, weakens, flips) and who caught it, and old signals carry a correction banner. That is what made this audit possible.

## What I'd change

1. **Check the label before sending.** Every figure needs its period, its basis and its kind: production or supply, close or intraday, quarter or half-year, 60 or 90 days. That one check targets most of WALTER's own errors.
2. **When the primary source is blocked or unread, say so in the headline** and ask Will to open it when a desk will act on the number. The Saudi error happened exactly here.
3. **Don't carry exact figures from search summaries of pages that weren't opened.** Write "reported, page not read" instead.
4. **Put scheduled releases on WALTER's calendar** (earnings calls of watched names, OPEC and IEA reports, EIA, ATTOM) so they land the same day, not weeks later.
5. **Fold same-day update chains** into one card updated in place, or one end-of-day roll-up for information-only recipients.
6. **Report the correction rate by month, with causes**, as an outside measurement, not a target. A target would reward not correcting.

## Limits

- 39 signals is a small sample. The accuracy rate has wide error bars: 32 of 33 means roughly 85–99% at 95% confidence.
- I checked headline claims and key numbers, not every sentence. Several checks used news reprints rather than the primary document.
- Six sampled signals could not be checked: X screenshots and images.
- Delay estimates use the earliest source time I could find. Some are approximate to within hours.
- "Corrected" counts only formal corrections. Errors nobody noticed (like the foreclosure labels) are not in the 7.6%.

## Files

- `data/sample.tsv`, `data/sample_grades.tsv`: the sample and per-signal grades
- `data/signals.tsv`: one row per signal (dates, type, status, corrects)
- `data/corrections_pairs.tsv`: each corrected signal with its correction and the hours between
- `data/dup_entity_candidates.tsv`: possible duplicate pairs from the entity scan
- `data/corpus.py`, `data/corr.py`, `data/dup2.py`: the scripts

---

## Copy-paste for PROME

```
PROME: outside audit of WALTER signal quality, 2026-11-18, repo at 78ed22bb9d. Read-only audit; nothing in the repo was changed. Please route items 1-5 to WALTER as a packet and record item 6 on the docket. No trade or capital step follows from this.

Findings (sample of 39 signals plus counts over all 2,229 on BOARD):
- Facts: core claim matched the source in 32 of 33 checkable sampled signals. One material error (SIG-W-20261111-001, Saudi production read as supply), corrected in 73 min.
- 4 uncaught minor slips in the sample, all labels: SIG-W-20260812-003 calls ATTOM's first-half +18% starts and +33% REO "Q2"; SIG-W-20260511-026 $212.13B vs the call's ~$210B; SIG-W-20260727-012 $787B vs source $797B; SIG-W-20260901-014 omits the two UAE bases in the same Army statement.
- Corrections: 169 signals (9.3% since July) named in a later correction, rising to 14.7% in November; median 2.7 h to correct. About 6 in 10 are WALTER's own errors, and most of those are label/basis errors, not wrong events.
- Speed: median ~29 h from source to dispatch; breaking news under 5 h; slowest WFC NDFI 27 days at IMMEDIATE precedence.
- Duplicates: no pure duplicates found; ~11% of signals are same-day update chains.

Asks for WALTER (owner decides how):
1. Add a pre-dispatch label check: every figure states period, basis and kind (production/supply, close/intraday, quarter/half, 60/90 day).
2. When the primary is blocked or unopened, put that in the headline and ask Will to open it before a desk acts on the number.
3. Stop carrying exact figures from search summaries of unopened pages; write "reported, page not read".
4. Add scheduled releases for watched names and agencies to WALTER's calendar so they land the same day.
5. Fold same-day update chains into one card or an end-of-day roll-up for INFO recipients.
6. Record (DOCKET): fix the foreclosure label on SIG-W-20260812-003 through WALTER's normal correction path, and have WALTER report its correction rate by month and cause as an occasional measurement, not a target.

Full report: Claude project file signal-quality/2026-11-18_walter-signal-quality.md (outside the repo).
```
