# CYPHER STATUS

**Last Updated: 2026-10-23 07:30 ET — live news sweep (Will-launched, Claude Code, claude-opus-5-5): 3 non-US bank-sector incidents ledgered, Palo Alto reach added to PHP2Shell, do-not-relay list re-cut, KB-CYP-019.** Evidence records: `research/2026-10-23_news-sweep-and-relay-pattern.md` (this session) · `research/2026-10-22_first-session-verification-record.md` (first session).

> ~~FIRST-LIVE-SESSION BANNER~~ — **SPENT 2026-10-22.** `FIRST_SESSION.md` items 1–8 done or carried as listed under § First-session record. Normal boot from here.

## Current judgment

**WAVE-2026-10 is open and reads MECHANICAL so far (Log4Shell-shaped). Not one of the nine escalation rows has fired (rows 1, 2, 4 re-checked 2026-10-23).** PHP2Shell (CVE-2026-109618 / -109619) is **ATTEMPTS-ONLY**. Exploitation attempts are confirmed: AWS MadPot from 10/17, before the 10/21 disclosure, and watchTowr honeypots since 10/21; Bitdefender and Huntress telemetry see none, and Sansec says public exploits fail on a default PHP install (vendor claims). No named organisation has a confirmed successful compromise. The Dutch NCSC is "investigating first signals of successful misuse" (primary, page unchanged since 10/22 16:01 CEST at the 10/23 07:3x ET re-read) and names no victim. **New reach (primary, 10/23):** Palo Alto says PAN-OS, Panorama and WildFire WF-500 are affected; hotfixes due 10/26–10/30, Panorama / WF-500 "ETA: TBD"; no exploitation known against its products. **That is weak evidence, not an all-clear.** Pre-disclosure exploitation plus a low-footprint exploit (KB-CYP-012) is the MOVEit shape, where victims surfaced at +14 days. The prior from five past waves is mechanical for banks (KB-CYP-001: 0 of 5 caused a run, a failure or a central payment outage).

| Gauge | Reading (2026-10-22; re-checked 2026-10-23) | Canonical |
|---|---|---|
| Escalation rows, WAVE-2026-10 | **9 of 9 NOT-FIRED** (row 5 adjudicated NOT-FIRED on the NYDFS 10/22 letter, routine patch guidance) | `workbook/ESCALATION_WATCH.tsv` |
| Convergence composite | **21/40 raw · 15/40 shared-root-adjusted** (PHP2Shell root counted once across VX-CYP-02/03/06); broad YELLOW, no vector above 3 | `workbook/VX.tsv` |
| Transmission map | 19 mechanisms: **7 CONFIRMED** (FL-CYP-06 ICBC FS and FL-CYP-18 NotPetya exclusions flipped tonight), 7 NOT-OBSERVED, 2 MODELED, 3 UNTESTED | `workbook/FLOW.tsv` |
| Incident ledger | 23 rows: every seed re-verified at a named source; 021–023 added 10/23 (SBI PRIMARY-VERIFIED; Korea and CARLIY0S SECONDARY) | `workbook/INCIDENTS.tsv` |
| Predictions | **CYP-01** incidents escalate (8-K Item 1.05 ≥ 6 in Nov–Dec 2026) **30%**; **CYP-02** a named US bank / CU / core vendor compromised via a wave vector by 2027-01-31 **15%** — both Will's view, desk odds | `workbook/PREDICTIONS.tsv` |
| R1 two-way flip | Toward MOVEit: row 1 or 3 FIRES on or before 2026-11-20. Toward Log4Shell: rows 1, 3, 4 all NOT-FIRED at 11/20 with dated re-checks 11/13–11/20 | `workbook/EXIT_PROTOCOL.md` |

## Open wave — WAVE-2026-10 (canonical: `workbook/ESCALATION_WATCH.tsv`)

| Row | Sign | State (rows 1, 2, 4 re-checked 2026-10-23; others 2026-10-22) | Basis of the read |
|---|---|---|---|
| 1 | Confirmed successful PHP2Shell compromise | NOT-FIRED (ATTEMPTS-ONLY) | Dutch NCSC alert, CYPHER read 10/22 and re-read 10/23 (unchanged); 10/23 news sweep, no named victim; Patchstack timeline and victim sweep to ~23:35Z, DEWEY |
| 2 | KEV listing of the two CVEs | NOT-FIRED | boot.py leg 7 live (re-run 23:53 ET): KEV still v2026.10.21, both absent; leg 8 still no Item 1.05 8-K since 10/15. A listing looks likely (AWS: "broadly exploited") |
| 3 | Named US bank / CU / core-vendor victim | NOT-FIRED | Two OFF-WAVE US financial victims ledgered, neither tied to a wave vector: River Financial (CYB-INC-015), TruStage (CYB-INC-017) |
| 4 | Bank or vendor 8-K Item 1.05 | NOT-FIRED | boot.py leg 8 live: none since 10/15 |
| 5 | Regulator supervisory-concern statement | NOT-FIRED (ruled 2026-10-22) | NYDFS Industry Letter 10/22, CYPHER read: no compromise claim, deadline or reporting duty. Definition recut to the supervisory-concern test (DEWEY §5 channel column) |
| 6 | PCS designation / industry loss estimate | NOT-FIRED | DEWEY watch legs; PCS MIRROR-WALLED |
| 7 | Government state attribution | NOT-FIRED | Microsoft's vendor attribution of ConnectWise to Storm-0940 is not governmental (CYB-INC-018) |
| 8 | Bank / payment outages outside Japan | NOT-FIRED | Japan pauses precautionary (CYB-INC-008) |
| 9 | Sustained equity move | NOT-FIRED | Day 1–2 only; test 2026-11-18; HENRY / VULCAN read not yet consumed |

## Incidents worth knowing (canonical: `workbook/INCIDENTS.tsv`)

| ID | Event | State | Why it matters |
|---|---|---|---|
| CYB-INC-007 | PHP2Shell, CVSSv4 9.2 (attack complexity HIGH); PHP 8.1 and older have no upstream fix (some vendor backports) | ATTEMPTS-ONLY · PRIMARY-VERIFIED | The wave root. Exposure counts conflict 1.3M–22.6M; all carried |
| CYB-INC-015 | **River Financial Corp (Alabama BHC):** June ransomware, data removed, 4 class actions, materiality undetermined after 5 filings | CONFIRMED · PRIMARY-VERIFIED (EDGAR) | A confirmed US bank cyber victim in 2026; off-wave; REGINALD holds it via DEWEY REQ-001 |
| CYB-INC-017 | **TruStage** (CU insurer and vendor): partial outage since 7/11 (~103 days); data access undetermined | CONFIRMED · PRIMARY-VERIFIED (status page 10/20) | A single vendor to 93% of CUs (its claim) down for months, with no spread reported so far |
| CYB-INC-009 | eMudhra weak CA keys; Chrome drops the G3 root 10/27; non-browser stores already 10/19–20 | CONFIRMED · PRIMARY-VERIFIED | The trading-software trust-chain class has NO OWNER (exclusions register) |
| CYB-INC-016 | Railway platform breach; says it is part of a series targeting AI-inference providers | CONFIRMED · PRIMARY-VERIFIED | Shares the AI-key target with LiteLLM (CYB-INC-011); a link, not a merge |
| CYB-INC-001 | Tanker networks compromised (FBI/USCG); propulsion access REPORTED only | CONFIRMED (network) · SECONDARY | OT channel; FALCON / BRENT |
| CYB-INC-020 | **Quest Diagnostics (DGX)**: unauthorized access to its Quanum LSM ordering and results system, learned 10/21; "accessed certain patient records"; not material per Quest (8-K **Item 8.01**, 10/22); not PHP2Shell per Quest (AP) | CONFIRMED · PRIMARY-VERIFIED | Healthcare = NO-OWNER class, flagged to PROME and HENRY 10/23. **It exposed a blind spot:** boot.py leg 8 watches Item 1.05 only (DATA_ROUTES) |

| CYB-INC-021 | **State Bank of India:** exchange filing 10/21, 3,897 customer records with personal data among ~375,000 found on the dark web; no material impact claimed; source and vector unknown | CONFIRMED · PRIMARY-VERIFIED (NSE filing) | Non-US bank; NO OWNER for Indian banks (PROME flagged) |
| CYB-INC-022 | **South Korea, 16 financial firms** incl. Shinhan, KB Kookmin, Busan, Hana: ~100,000 records incl. national ID numbers (FSC 10/14); AI-agent use suspected, not shown | REPORTED · SECONDARY | Largest confirmed bank-sector hit this month; began 9/30, not wave-rooted; NO OWNER for Korean banks |
| CYB-INC-023 | **CARLIY0S / "CyberCartel":** Straiker says AI agents (Claude, Grok, Kimi) were used against 400+ LatAm financial *targets*; no confirmed breach count, no names | REPORTED · SECONDARY | With 022, the AI-run-attack theme; route VULCAN |

**Do-not-relay, 13 claims in three groups** (canonical: `research/2026-10-23_news-sweep-and-relay-pattern.md` §4):
- **Contradicted at the source (10):** "60M certificates" · "pip is compromised" · "Japan declared a cyber emergency" · "Google confirmed no certificates were issued" · "CISA saw millions of attacks" · "US attributes ConnectWise hack to China" · "NCSC confirms PHP2Shell breaches" (now carried by Archyde) · "NYDFS warns banks are being hacked" · "TruStage breach exposed 42 million" · "rogue AI agents broke into bank accounts" (only Barchart's rewording is refuted; Axios's report stays unverified, CYB-INC-019 REPORTED).
- **Unanchored, NOT refuted (2):** "Railway lost $371K" · "TruStage ransomware attack" (could prove true).
- **Joke (1):** "a key equal to 4".

**Relay direction (KB-CYP-019):** 12 of the 13 overstate toward alarm, 1 toward reassurance. Selection-biased sample (only odd-looking claims were checked), so it shows a direction, not a rate. Operating rule: a news outlet reporting an agency is a lead, never row-1 evidence.

## Standing conditions

- **Event, not consequence.** Boundary packets went to 11 consequence owners 2026-10-22. Each desk is UNCONFIRMED until it replies, and is re-raised next session.
- **Recorded disagreement:** DEWEY recommended a WALTER-run watch, not a desk. Will chose a desk (17:04 ET 10/22). R0 tests that choice on 2026-12-17.
- **No scanning or probing of named institutions. No exposed-bank lists on the BOARD.**
- **No book** (`TRADE.md`).
- **Two bands re-cut at first scoring:** VX-CYP-06 ORANGE/RED now key on the wave's ROOT flaw (a confirmed-exploited flaw somewhere is a weekly base rate: 91 fresh KEV adds in Q3 2026). VX-CYP-02 kept as written and scores 3 on Japan's precautionary pauses alone. Both recorded in the rows.

## Data walls

Verisk PCS: subscription (MIRROR-WALLED). NYDFS industry letters are **reachable by WebFetch** (the 10/22 403 was curl-specific). CISA KEV and SEC EDGAR (full-text search, submissions JSON) were reachable 10/22. Bloomberg, WSJ and FT are paywalled; their claims are carried as SECONDARY. **Reader quirks** (compressed-stream PDFs need pdfminer; Bugzilla HTML carried injected instructions, so read its REST API) are in `DATA_ROUTES.md`.

## Corrections this session (detail: research record §5)

- **Retracted 2026-10-22:** CYPHER's "the ICBC $9B was only the BNY debt; Treasury jy2114 not found" and "no Mandiant third-party line at TruStage". DEWEY was right on both, and CYPHER re-read both primaries. Retractions went to LIQUID and BOND; the ledgers are marked.
- WALTER published CYPHER's BOARD corrections as SIG-W-20261022-048, which does not carry the retracted claim.
- `TRADE.md` re-arm checked: TERRY's OKTA security-wave card (10/22) cites Will's premise, not a CYPHER row. The no-book surface stays FROZEN.

## First-session record (2026-10-22)

| Item | Done |
|---|---|
| 1 Re-verify seeds | All 14 incident rows and 9 watch rows, at named sources (4 read-only checkers + CYPHER's own NYDFS, NCSC and EDGAR reads). Corrections in each row's Notes. **KB-CYP-001..012 remain DEWEY-inherited** (ARTIFACT basis; not re-read). New KB rows 013–018 (8-K base rate, product map, ICBC, NotPetya exclusions, AP 2013, KEV speed) |
| 2 board_log | 22 signals logged (9 seeds, 5 unlogged 10/22 items, 8 new incl. 048), plus 2 correction rows |
| 3 Boundaries | Packets to REGINALD, GIBBS (NO-OWNER cyber/custody row now has an event owner), SHADE, VULCAN, FALCON, BRENT, WATT, HENRY, LIQUID, BOND, OTTO |
| 4 / 4b | R1 flip written; VX scored; FLOW precedents verified (06 and 18 CONFIRMED, 19 stays UNTESTED, because its precedent is secondary-only) |
| 5 Leads | River Financial read (five filings, not two); NYDFS letter read; NCSC primary read |
| 6 | PROME asked: SUMMONS_LEDGERS registration of `docket/CATALYSTS.tsv`, a DOCKET row for the open wave, the FLEET_DIRECTORY gap and Group CYBER registration |
| 7 / 8 | `NEXUS_BRIEF.md` created; STATUS rewritten; PROME completion memo |

**Known gaps carried:**
- boot.py leg 5 checks Last_Checked only on REPORTED / ATTEMPTS-ONLY rows, so a blank cell on a CONFIRMED row passes silently. Caught by hand tonight; fix and drill at the next boot.py edit.
- `corrections_boot_check.py CYPHER` returns rc 2 until DAEDALUS lists CYPHER in FLEET_DIRECTORY.
- boot.py leg 8 sees only Item 1.05. A non-material cyber 8-K under Item 8.01 is invisible to it (Quest, 10/22). Add an 8.01 cyber-term search, with a drill, at the next boot.py edit; until then a quiet leg 8 means "no MATERIAL incident filed".

## BOTTOM LINE

One wave is open (PHP2Shell plus October's supply-chain and certificate failures), and none of its nine escalation rows has fired as of the 2026-10-23 re-check. The composite is unchanged at 21/40 raw and 15/40 after counting the shared PHP2Shell root once, which fits a Log4Shell-shaped wave so far; three non-US bank-sector incidents (India, Korea, Latin America) were ledgered 10/23 but are not wave-rooted and move no US-keyed band. The most important unconfirmed lead is still the Dutch NCSC's "first signals of successful misuse": a named victim on or before 11/20 flips the wave toward the MOVEit shape. Next wakes are Chrome's eMudhra root removal on 10/27, DEWEY's rerun on 10/29 (the 7-day re-check deadline), Palo Alto's last PAN-OS hotfix ETA on 10/30 and the MOVEit-analogue victim check on 11/04.
