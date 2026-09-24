# SCRATCH.md rotation (verbatim, crc-stamped)

Pruned from `SCRATCH.md` 2026-09-24 ~09:3x ET at closeout: the dated sections from 2026-08-27 (two), 2026-09-01 and 2026-09-02, all >2 weeks old (SCRATCH prune rule). Byte-for-byte complete lines.
Marker lines are three '<', L plus the ORIGINAL line number, three '>'. The payload is everything after the PAYLOAD-BEGIN line.
crc32 of payload: a2cf7495 · bytes: 13641 · lines rotated: 74

PAYLOAD-BEGIN
<<<L50>>>
## 2026-09-02 (Wed — boot → inbox drain → read-cap P1 → ROLL70 fill → REG-T-02 exit grade at the close)
<<<L51>>>

<<<L52>>>
- **Exit-grade arithmetic, so nobody re-derives it wrong:** 81.90 − 79.12 = $2.78 → **+3.51%** (÷ close) to leg 1. Day +$1.86 / +2.41% (÷ 77.26). ⛔ 79.12 > 78 is **NOT** an un-fire — state machine, not event counter.
<<<L53>>>
- **The intraday/close gap, measured on my own tape today:** 14:23 print **$79.51**, settled close **$79.12**. Intraday was 39¢ HIGH. This is the cheapest possible demonstration of why `value_basis: regular-session close` is not pedantry.
<<<L54>>>
- **`read_cap_check.py` reports `--agent` perimeter as a heuristic** and says so in its own header line — it scans boot-section "read" lines in CLAUDE.md. When I split the DASHBOARD out and declared it NOT-a-boot-read, it correctly dropped off the whole-read list. So the instrument DOES respond to a boot-step edit — which is also how you could launder a breach (rule 14 names exactly this). Declaring honestly is load-bearing.
<<<L55>>>
- **crc marker gotcha, cost me one rebuild:** never let a delimiter literal appear inside the verification snippet printed in the same file — `s.split('<!--A-->')` found the instruction text first and returned a 410 B fragment. Build the marker from parts in the snippet (`'<!--RB-'+tag+'-START-'+'->'`).
<<<L56>>>
- **Token-sweep gotcha, cost me three passes:** grepping the CURRENT version's tokens cannot see a superseded vintage under a `(PRIOR — …)` marker. Sweep by SHAPE (`EV \$[0-9]`, `PT \$[0-9]`), not by the value being retired.
<<<L57>>>
- **The harness memory path is a SYMLINK into the repo** — `~/.claude/projects/-home-willi-Research-workspace/memory` → `memory/auto/`. Files written there are repo files and need `git add`. `git ls-files --error-unmatch <path>` before claiming any artifact exists.
<<<L58>>>
- **Ledger nudge fired on 8 ledgers and most are false alarms** (quarterly cadence + correct two-clock headers). The one real hit is still `MI3_COHORT.tsv` — no header, and it CANNOT be hand-added: `mi3_cohort_screen.py` rewrites via `csv.DictWriter` and both readers use bare `DictReader`. Generator + 2 readers + guard re-run, ~30 min.
<<<L59>>>
- ⚠️ **A HOT/COLD SPLIT RELOCATES REFERENCES, AND A RETIREMENT CHECK KEYED ON "referenced by a live doc" WILL NOT KNOW.** My first >60d retirement grep this closeout covered STATUS/ROADMAP/MEMORY/CALENDAR/workbook and returned **refs=0** for `CRE_DQ_BY_TIER_2026-06-20.md` — retirement-eligible on the letter. It is actually referenced by **`STATUS_DASHBOARD.md`, the cold half I split out THIS MORNING**, plus two `reports/`. **I created the blind spot and then ran the check that could not see past it, in the same session.** ⇒ **after any split, the retirement grep's file list must include the cold halves** — and more generally, a structural change silently re-points every check that enumerates surfaces by hand. Same family as lesson 28 (a mechanical rule right on the letter, wrong on the object) and `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`. Only `WAL_10Q_DRILL_2026-05-21.md` was genuinely eligible (0 refs incl. cold files, reports/ and registry/; WAL-domain, and WAL has been a peer since 7/25) — archived.
<<<L60>>>
- **Noticed, not pursued:** `thesis/CHANGELOG.md` is 34,044 B and over budget — the one over-budget boot-read that got no attention today. It is history by definition, so it should rotate cleanly on the same pattern as the others.
<<<L61>>>

<<<L62>>>
---
<<<L63>>>

<<<L64>>>
*(**2026-08-23 section PRUNED 2026-09-02** — 3,930 B, 10 days old, per this file's own >~2wk promote-or-delete discipline. Its load-bearing items had already been promoted: the FHLB/PNC attribution → `STATUS.md` §THRESHOLD STATUS + `ML-REG-160`; the concentration-shape-is-not-a-cause lesson → MEMORY CARRIED LESSONS 20. Nothing unpromoted was deleted.)*
<<<L65>>>

<<<L66>>>
## 2026-08-27 (Thu) — residue from the first session after 3 dark days
<<<L67>>>

<<<L68>>>
*Task ledger is NOT here — `MEMORY.md` §NEXT SESSION, per this file's own contract.*
<<<L69>>>

<<<L70>>>
### Tooling worth keeping
<<<L71>>>
- **Recount a consecutive-session run at the series; never increment it from memory.** One `python3` pass over paired FRED pulls printed the whole run with a reset column and gave 19 sessions + the run peak + the driver decomposition in one shot. My file said 14 and I would have written 19 by adding 5 — which would have been right by luck and wrong as a method.
<<<L72>>>
- **The wide-table regex trap is real and I hit it live today.** `grep -oiE '(a|b)[^.]{0,120}(c)'` against an IR page died with *"exceeds complexity limits"*. MEMORY already carries this: **grep the bare literal and eyeball.** Cost ~1 minute because the lesson was on file.
<<<L73>>>
- **`curl` an IR host before trusting it:** `ir.westernalliancebancorporation.com` returns an Acquia *"Web Site Not Found"* page with **HTTP 200 and 970 bytes**. A byte-count check caught it; a naive grep-for-nothing would have read as "no announcement."
<<<L74>>>
- **`until [ "$(TZ=America/New_York date +%H%M)" -ge "1602" ]; do sleep 30; done`** backgrounded = a close-watcher that notifies once and exits. Better than polling `date` between edits.
<<<L75>>>

<<<L76>>>
### Arithmetic worth keeping (so I don't re-derive it)
<<<L77>>>
- **CCC/HY run, 7/31→8/26:** 19 consecutive >3.6×, peak **3.861 [8/26]**. Endpoints **CCC 1034→1031 (−3bp) / HY 285→267 (−18bp)** — the decomposition *is* the verdict.
<<<L78>>>
- **WAL cycle closes since the 6/30 exit — zero below $78.** Two nearest: **7/08 $78.31 (+0.40%)** and **8/24 $78.39 (+0.50%)**. Deepest intraday lows: **8/27 $77.13**, 7/08 $77.49, 8/25 $78.00.
<<<L79>>>
- **WAL/EGBN print sequence, both quarters:** Tue AMC → Wed AMC → Thu 10:00 call. 2025: Oct 21/22/23. 2026: Jul 21/22/23.
<<<L80>>>

<<<L81>>>
### Behavioural — parked here on purpose, not tasks
<<<L82>>>
- ★ **Two superlatives crossed my desk today from sources I trust, and both were wrong.** PROME's *"nearest approach on record"* for WAL (7/08 was 8¢ nearer) and my own file's *"2026 max 1034"* (1039 printed 8/25). **Neither was checkable without pulling the series — which is exactly why neither had been checked.** A superlative is the claim most likely to be inherited and least likely to be verified.
<<<L83>>>
- ★ **The most corrected-*looking* line in a file is a good place to hunt for stale figures.** HOMER's catch: my brief's bullet was **headed "RETRACTED"**, correctly reported a retraction, and then used the withdrawn evidence to support it — for three weeks, while my STATUS was already right.
<<<L84>>>
- ★ **Today's obvious fix would have recreated the defect it was fixing.** CREED's fix (a) — re-point `VX-CREED-4.01` at the QBP — would have named a source that does not contain the value, which *is* the original defect. It only died because CREED **executed the fix and looked at the result** rather than reasoning about it.
<<<L85>>>
- **Four of my own live surfaces were wrong in ways no threshold would have caught**: an oil-leg "FIRING" call 41 days stale, a leg cited as registered that is ungradeable, a buffer stated twice at two values, three superseded peer figures. **None of these trip an alarm. All of them travel.**
<<<L86>>>

<<<L87>>>
### Half-thought, not pursued
<<<L88>>>
- **A "publication-shape" field for registered rows.** Today produced two rows whose levels live in *episodic prose/charts* rather than standing table cells (`CREED-T-03`'s NOO series; arguably FHLB's own combined report). A row could carry *"is this level in a table cell that prints every period, or in narrative that may not?"* — cheap, and it is the property that made T-03 gradeable-by-luck. **Not proposing it; MIDAS's ask ② is adjacent and still open with Will.**
<<<L89>>>
- **Does regional CRE OREO deserve a vector?** It is the only Q2 recognition tell and it is on my surface — but n=1 quarter, and a 26% move on a $915M stock is small. **Base-rate before building.**
<<<L90>>>

<<<L91>>>
## 2026-08-27 (Thu, 2nd session) — residue from the price-correction + closeout pass
<<<L92>>>

<<<L93>>>
### Tooling worth keeping (re-derived today; next time, don't)
<<<L94>>>
- **Settled closes + the PRIOR close in one shot** — the thing that caught the inverted day-change. `market.py` gives level and a % but not the reference it used, so re-derive the % yourself:
<<<L95>>>
  `.venv/bin/python3 -c "import yfinance as yf; h=yf.Ticker('WAL').history(period='12d')[['Open','High','Low','Close']]; print(h.round(2).to_string())"`
<<<L96>>>
  Multi-ticker form: loop `yf.Ticker(t).history(period='5d')['Close']` over the cohort and zip with `str(d)[:10]`.
<<<L97>>>
- **Weekday assertion before writing any dated row** (claim_check will flag it later; cheaper now):
<<<L98>>>
  `python3 -c "import datetime; print(datetime.date(2026,8,31).strftime('%A'))"`
<<<L99>>>
- **Kernel state, checked at the artifact rather than the record:** `ls KERNEL/shadow/events/2026/08/` + `find KERNEL/audit -type f` + read each event's `actor_id`. An event id's UUID prefix is NOT a reliable owner tell — open the file.
<<<L100>>>
- **sha256 a submission against its activation pin:** load the activation JSON, walk `commands[]`, `hashlib.sha256(open(c['path'],'rb').read()).hexdigest() == c['sha256']`.
<<<L101>>>

<<<L102>>>
### Arithmetic worth keeping (so I don't re-derive it)
<<<L103>>>
- WAL 8/27: close **$78.71**, prior close **$79.60 [8/26]** ⇒ **−$0.89 / −1.12%**. Buffer to $78 = **$0.71 / 0.91%**. Intraday low **$77.13**; rally off low **$1.58**.
<<<L104>>>
- KRE 8/27: close **$74.35**, prior **$74.58 [8/26]** ⇒ **−$0.23 / −0.31%**. **+23.9%** above the $60 line.
<<<L105>>>
- ⚠️ **A buffer % and a day-change % are both "small positive numbers next to a price."** They are not interchangeable and nothing in the layout stops you swapping them. That swap is what inverted the headline.
<<<L106>>>

<<<L107>>>
### Behavioural — parked here on purpose, not tasks
<<<L108>>>
- I typed an inherited integer (precondition ⑦) from working memory **twice**, wrong both times, in the same closeout. The fix that worked was `grep -rn` for the token across the dir before commit — not resolving to be more careful.
<<<L109>>>
- The retirement rule was *correct* on `CCC_HY_TRIPWIRE` and the right answer was still "don't". Mechanical sweeps need one "what IS this object" read before executing.
<<<L110>>>

<<<L111>>>
### Half-thought, not pursued
<<<L112>>>
- `market.py` prints a % without naming the close it differenced against. If it printed the reference date, this session's defect would have been visible at a glance rather than needing a separate history pull. Possible small ask to whoever owns that script — **not raised, not verified as feasible.**
<<<L113>>>

<<<L114>>>
## 2026-09-01 (Tue — spawned post-close for the `REG-T-02` fire; inbox drain 28/28)
<<<L115>>>

<<<L116>>>
- **Fire arithmetic, both bases, so nobody re-derives it wrong:** $78.00 − $77.26 = $0.74 → 0.95% (÷78) / 0.96% (÷77.26). Exit: $81.90 − $77.26 = $4.64 → +6.01% (÷77.26). Day −$0.87 / −1.11% (÷78.13).
<<<L117>>>
- **yfinance `history()` had NO 8/28 bar for WAL/KRE (or most tickers) today** — 8/27 → 8/31. SPY/XLF had it. Not a grade defect (9/1 bar present, quote endpoint agrees). If it recurs, note it as an instrument quirk, not a missing session.
<<<L118>>>
- **Cohort-sort recipe (reused from 8/20):** `NDFI_COHORT.tsv` has a `#` comment line ABOVE the header — `csv.DictReader` silently uses the comment as the header and returns nothing usable. Strip `#` lines first. `scipy` is not in `.venv`; use `pandas.DataFrame.corr(method="spearman")`.
<<<L119>>>
- **AEOLUS 8/27 (×2):** Colorado ROD — if Lower Basin implementing agreements go unexecuted, shortage apportions by PRIORITY (Law of the River): CA senior shielded, AZ junior CAP absorbs. Apparent erratum: §10.7 drops the "not" in "shall not preclude or predetermine" (7 of 8 instances carry it). Mead consultation trigger = 1,000 ft (not 1,010). AEO-10 (no breach of 1,035 through 12/31) re-priced 30% → 65% after AEOLUS base-rated USBR's August under-projection (+2.19 ft mean, n=6). **Credit-relevant leg for me = AZ CAP-dependent munis/ag districts; CREED cc'd. No action; parked.**
<<<L120>>>
- **DEWEY CRMT playbook (8/27):** the one transferable structure — "non-recourse" ABS ring-fenced for PAYMENT but cross-defaulted for CONTROL (§8.1(p): any servicer-termination event at any trust = term-loan EOD; §8.1(b) carves that debt out of the general cross-default). → ROADMAP backlog: do the bank-syndicate credits I cover treat sponsor-serviced securitizations the same way?
<<<L121>>>
- **CREED 8/28 on WALTER-005:** the failure cohort (sub-$100M thrifts) ≠ CREED's OREO recognition cohort ($10-250B). QBP Table V-A has a `<$100M` class with a `Failed institutions` line — but pdfminer emits its columns out of order (trap #14); anchor on a known cell before quoting. Verdict 0.75 stands; low-priority backlog to run the class at primary.
<<<L122>>>
- **Cold storage (SIG-046):** first negative 1H net absorption since 2007, vacancy 7.7%, but it is a COMPOSITION story (pre-2020 stock vacated, post-2020 absorbing). No bank on my surfaces names cold-storage collateral. CREED scope call.
<<<L123>>>
- **Fifth Third has two things this week:** Delaware Life distribution pause (8/28) + the Sep 5-7 Comerica systems cutover. Different objects; do not fuse.
