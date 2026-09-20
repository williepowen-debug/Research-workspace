# OSPREY — review of the September 20 read

**Reviewer:** CATO, dedicated OSPREY session. **Assignment:** Will requested review and analysis of OSPREY's quoted boot read, with other CATO instances working on other agents. **Snapshot:** shared HEAD `26827bac08c4976fb6882e685a681f421f49a442`; latest OSPREY commit `916276bc3`. All ten captured OSPREY files matched that revision and remained unchanged at the evidence check. [Evidence and hashes](2026-09-20_1140_osprey-read-review-evidence.json).

**Disposition:** useful event discipline, but the national supply conclusion requires correction. The evidence supports withholding a new Moscow-specific lost-barrels estimate. It does not support saying refinery damage has not transmitted into production, that the only Brent transmission route is closed, or that unchanged published marks demonstrate unchanged physical impairment.

This is a context-aware review of OSPREY's work, not a blind review or certification of all its history. No owner files, shared CONTINUITY, thresholds, predictions or grades changed; no owner messages, fleet launches, operational sweep or trade action. The shared CONTINUITY was already being edited by another CATO instance; this report carries this session's separate resume point. The existing untracked CRUISE report was preserved.

## F1 — HIGH: the export source contradicts the assertion that refinery damage has not reached production

**Location:** quoted read, paragraphs beginning “The market transmission” and “The one bridge”; KB-OSPREY-114/143; `thesis/THESIS.md` §§1–2 for the broader transmission model.

The named [September 15 Bloomberg report by Julian Lee, syndicated by Transport Topics](https://www.ttnews.com/articles/russia-boosts-oil-flows) supports **3.54 million b/d for the four weeks ending September 13**. But that same report says diverted crude exports were insufficient to maintain production, and reports August output of **8.72 million b/d**, citing OPEC secondary estimates. This is direct contrary evidence to the quoted “We are not seeing that.” The underlying OPEC table was not independently downloaded: its public download endpoint looped back to the landing page.

Exports and production can move in opposite directions. Illustratively, holding stocks and other flows constant, refinery intake falling 0.3 while production falls 0.2 permits exports to rise 0.1. These are arithmetic examples, not estimated Russian flows. A recovering export series cannot, by itself, exclude production losses. Nor does a four-week average ending September 13 observe September 20's consequences.

The source does not identify a Moscow-specific production effect or quantify what portion of the national decline is strike-caused. It nevertheless requires withdrawing the categorical negative. **Correction:** retain the dated export recovery and say national production transmission has been reported; its size, attribution and new incremental effect remain unresolved.

## F2 — HIGH: the claimed aggregate evidence gap overlooks material independent estimates

**Location:** STATUS “Current sourced aggregates and limits,” C1 dashboard; KB-OSPREY-029/143; quoted next-effort choice and “more searching won't fix it.”

Two accessible publications deserve a basis reconciliation before repeating that there is no independent aggregate above 40%:

| Publication | Observation found | Important limit |
|---|---|---|
| [S&P Global, September 3](https://www.spglobal.com/energy/en/news-research/latest-news/refined-products/090326-russian-august-crude-exports-fall-on-month-amid-black-sea-attacks) | Its own CERA analysts estimate **nearly half** of Russian refining capacity offline at end-August. The same article relays Novak attributing some below-forecast production to refinery underutilisation. | End-August observation, not September 20; capacity estimate, not strike-attributable lost throughput. |
| [IIR Energy, September 8](https://www.industrialinfo.com/news/article/unplanned-outages-at-17-russian-refineries-average-38-million-bpd-offline-in-august-2026--362113) | Its ECI dataset reports **3.805 million b/d** average unplanned crude/condensate capacity outages in August, involving 44 units at 17 refineries; confirmation delays may revise the month. | Scope includes condensate; unit-level outage accounting and the denominator need inspection before comparing it with runs or the desk's band. Underlying proprietary dataset not audited. |

These are publishers reporting their own analytical estimates, not simply relaying a Ukrainian General Staff percentage. They do **not** establish the correct replacement band or automatically fire a registered rule. Source eligibility, observation period, capacity denominator, aggregation method and outage cause still matter. Existing completed predictions must not be retrospectively regraded from later publications.

**Correction:** separate the unanswered questions: current national runs; physically unavailable capacity; strike-attributable lost output; and today's incremental loss. “No measured incremental barrels for this facility” is defensible. “No useful independent aggregate exists” is too broad. Reconcile these sources with the existing July/August basis issue, rather than adopt whichever number is largest or call each number corroboration.

KB-029 itself remains ACTIVE with `Stale_By=2026-09-10`; its July source is not a new September observation. KB-143 preserves August 31 as publication date, but an old assessment and an unchanged proxy cannot establish that physical impairment remained stable throughout September. That is an unmeasured change, not a measured zero.

## F3 — MEDIUM: separately scored channels are economically connected; delayed repair can be a new loss

**Location:** quoted “three independent supply mechanisms,” “Russian problem,” “only way,” and “last night ... doesn't deepen it”; `thesis/THESIS.md` §§1–2.

Keep the separate channel accounting. But product shortfalls can affect foreign refinery demand for crude, product inventories, substitution and risk premia. Russian refinery shutdowns can also free crude for export. These opposing mechanisms require a net assessment; neither establishes an automatic bullish Brent effect. A categorical wall between products and crude is not a demonstrated economic result.

The [IEA's September 17 commentary](https://www.iea.org/commentaries/russian-refining-sector-struggles-amid-intensifying-ukrainian-attacks) connects reduced Russian diesel exports to international middle-distillate shortages. It also distinguishes short CDU repairs from secondary-unit repairs lasting months and reports Moscow offline until early 2027. This supports a sustained global products concern and OSPREY's prior-outage hypothesis, without measuring September 20's incremental damage.

A repeat strike on an idle unit can still remove **future expected output** by delaying restart. The relevant comparison is the recovery path without the new attack. For example, an additional 20 days offline at an illustrative expected 100,000 b/d means 2 million fewer barrels processed over that period, even if instantaneous throughput was zero when hit. Neither input is a Moscow estimate.

**Correction:** “No new Moscow-specific crude-supply loss is established. Persistent refinery impairment remains relevant to global products, production and the expected recovery path; net Brent impact requires BRENT's assessment.” Do not translate this review into a trade proposal or a replacement score.

## F4 — MEDIUM: the Moscow conclusion is plausible, but its sourcing and deadline need narrower claims

**Location:** RU-20260920-MOSCOW-REFINERY, KB-143, STATUS ACTIVE 2 and closing watch, quoted September 23–25 resolution.

The [August 31 Insider analysis](https://theins.org/en/economics/296530) does contain the broad impairment discussion and Moscow's expected prolonged outage. However, its Sinara link leads to a **June 24 Reuters dispatch**, not a newly dated August 31 bank estimate. Its RSPP link leads to an August 21 RBC interview whose available text does not expose the relevant passage. Thus the item is useful reported context, not two newly authenticated independent measurements.

The [June 24 Reuters dispatch, syndicated in Russian](https://ru.themoscowtimes.com/2026/06/24/eksklyuziv-moskovskiy-npz-smozhet-vozobnovit-rabotu-ne-ranshe-2027g-istochniki-a199031), attributes a minimum six-month repair outlook to two sources familiar with the plant's plans; Sinara's one-year/$1 billion estimate is explicitly a pessimistic scenario. It separately reports historical 2024 throughput. Neither historical throughput nor a repair forecast is measured September 19 operation. The Insider also links a July restart claim and disputes it; a fresh operational check remains needed.

Reusing the name **AVT-6** does not establish recycled reporting: the same unit can be struck twice. The current ledger Notes already acknowledge a September General Staff unit claim, while STATUS still calls the detail Russian-Telegram-sourced. [Contemporary reporting](https://unn.ua/en/news/the-general-staff-revealed-details-of-the-strike-on-one-of-russias-largest-oil-refineries) explicitly attributes the named units to the September 20 General Staff statement. That remains belligerent evidence, not independent damage confirmation. The original military post and imagery were not independently authenticated in this review.

**Correction:** record current belligerent claims separately from the June history; keep the damage unverified without declaring repetition proof of contamination. Treat September 23–25 as scheduled **review dates**, not a promised information release or guaranteed resolution. “Minimal incremental barrels” remains a hypothesis conditional on no restart; prolonged future outage remains possible even under that hypothesis.

## F5 — MEDIUM: the ledger supports ten September rows, not record-high tempo

**Location:** quoted opening and KB-143 Notes.

The counts reproduce: **119 data rows**, **16 columns**, **58 exact `refinery`-class rows**, and **143 KB rows**. Date range: February 23–September 20. But 58 is an event-row count, not 58 unique refineries. The ledger also contains mixed classifications and negative/unconfirmed records; total rows are not a census of confirmed successful strikes.

On the same exact refinery classification:

| Window | Rows |
|---|---:|
| August 1–20 | 13 |
| Full August | 18 |
| September 1–20 | 10 |

The quoted named list sums to **nine** events. Its tenth row is September 7's **unnamed Tatarstan facility, C4**, whose outcome is disputed. Ten ledger rows therefore cannot be rendered as ten equally confirmed named-facility strikes. The incompleteness warnings further prevent these counts establishing the true campaign peak.

**Correction:** report ten September refinery-class records with the unconfirmed case identified, or give a stricter confirmed subset. Withdraw “densest ... entire campaign” unless a consistent event series and comparable window demonstrate it. Capability, geographic reach and strike frequency are separate claims.

## F6 — MEDIUM: the feed ran, but its claimed audit trail does not travel and a known bad match recurs

**Location:** `scripts/strike_feed.py`, `.gitignore`, `domain/energy-strikes/feed/README.md`, September 20 candidate/match files; STATUS versus SCRATCH/NEXUS_BRIEF.

Local artifacts support today's run: **29 candidate rows, 22 NONE rows with owner dispositions, six match rows and one Militarnyi EMPTY_FEED**. Seven sources are configured. This establishes the saved output, not complete source coverage or full-window recall. Finding an event already entered manually is successful overlap, not another demonstration that the feed found a manual miss. The original historical recall success may stand separately; this pass did not independently backfill the window.

Both `FEED_CANDIDATES_*.tsv` **and `MATCHES_*.tsv` are ignored**. Today's files are untracked. README and code describe MATCHES as committed, so the intended precision audit is also missing from Git, beyond the already-disclosed candidate-disposition gap. The filenames are per-day and both are opened with `w`: another same-day run can overwrite the evidence and manual candidate notes. This overwrite behaviour was established by static inspection, not by running the owner's live feed.

Today's match file again associates [a September 14 Sochi residential-damage report](https://www.themoscowtimes.com/2026/09/14/ukrainian-drone-strike-in-sochi-wounds-5-a93699) with `RU-20260913-KOMYSH-UNNAMED`, carried solely by **crimea**. That article does not establish a Komysh merchant-vessel event. An isolated replay using the exact snapshot code, its ledger, the stored headline and an actual article sentence reproduces the match. It is not a reconstruction of the original RSS payload. This demonstrates a false match, **not** a newly discovered missing energy strike or a fleet-wide error rate.

The summaries disagree: STATUS says the feed did not run; SCRATCH/NEXUS say it did. STATUS ACTIVE 4 says theater-wide sweep while its coverage paragraph explicitly limits it to a targeted pass. The later KB-143 interpretation was committed only to KB/STRIKES, leaving the startup summaries behind. NEXUS also retains an older paragraph about an unidentified September 13 vessel blocking the clock despite publishing the newer ruled anchor above it.

**Correction:** apply the existing review-of-matches requirement to both absorbed and NONE candidates; preserve reviewed evidence in versioned storage; reconcile run/coverage claims. Fix the existing matcher/evidence workflow rather than add another recall-only test. No owner code repair was assigned or performed.

## Suggested bounded next step

Prioritise an **evidence-basis reconciliation**, then coverage work:

1. Correct the production/export inference using the full source already cited. Carry both observations and distinguish national transmission from Moscow's incremental effect.
2. Put the S&P/IIR estimates beside the existing runs proxy with observation period, publication date, denominator, cause and source eligibility. Resolve or explicitly retain the disagreements before proposing any band/mark change.
3. Update Moscow's pre-strike operating/restart evidence and prospective outage duration; retain an unresolved result if no reliable update appears on the review date.
4. Complete the September 17–20 pass under the existing method, preserve its receipts and review every feed match. This is useful coverage work, but does not itself resolve the aggregate measurement problem or certify older windows.

Do not wait for a complete September monthly statistic before reading already available contrary evidence. No guarantee is made that a precise, current, strike-attributable national loss can be obtained from public data.

## Checks, limits and closeout

- Independently checked selected public sources and exact local counts; traced the main Bloomberg, Insider and Reuters source chains. Web search returned the full Bloomberg syndication text, although a subsequent direct open failed. IEA/S&P/IIR pages were directly readable. RSPP's underlying passage, proprietary outage microdata, original strike imagery and OPEC's production table were not fully authenticated.
- Ran an isolated offline matching counterexample; no network fetcher main, operational boot, owner updates or full campaign census. No live price, portfolio, sanctions-law or war-risk adjudication.
- All ten initial OSPREY snapshots matched the pinned shared revision and remained unchanged at the recorded check. Only this report and its JSON evidence were authored here. Existing CATO/PROME work was preserved.
- JSON validation and whitespace checks passed; root weekday check passed on four files. The orphan advisory flagged another session's modified `memory/auto/finding_header_edit_is_the_edit_most_mistaken_for_maintenance.md`; it was preserved, not staged. No tests or controls were changed.
- **Resume:** this bounded review is delivered. Continue OSPREY discussion with Will; any assigned correction follow-up must first recheck owner revisions. Other CATO assignments and approvals remain separate. Shared CONTINUITY is intentionally untouched because it was in concurrent use.
- Exact-path commit and safe-push outcome will be delivered in-session after execution; this paragraph is not a push receipt.
