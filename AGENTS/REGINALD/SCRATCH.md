# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

*(7/25 section pruned 2026-08-13 — 19d, promote-or-delete per lesson-14: the **perl EDGAR-table recipe** and the **regex-backtracking gotcha** → MEMORY §Findings; **"a stated basis is falsifiable, an unstated one isn't"** and the **control-covers-the-anticipated-case shape** → MEMORY lessons (the shape got two fresh instances today); the **EGBN two-route ACL cross-check** → MEMORY §Findings; the **small-bank-CRE-bid half-thought** → ROADMAP backlog; CCC/HY fire-#2 arithmetic DELETED as superseded by the full FRED series pulled 8/13. 7/17 section pruned 2026-08-10 — >3wk, per the lesson-14 discipline this time (same-session promote-or-delete, no unpromoted control-notes left behind): **the one live note — WALTER's BB/B sub-index gap on REG-T-03/04 — was PROMOTED to `registry/NOTES.md` §REG-T-03/04** before deletion; the other three (tripwire decomp design lesson, CFG beta-vs-substance, Brent overtaken) were already canon in ROADMAP/brief/STATUS. 7/10 section pruned 7/30 — its "two-clock header silences its own nag" note became MEMORY lesson 14 after sitting unpromoted 20 days.)*

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*

---

## 2026-08-23 (Sun) — residue from the orchestrated single touch

### Tooling worth keeping (I re-derived all of this from scratch today; next time, don't)
- **FHLBank SEC lookup that actually works.** The FHLBanks are SEC registrants. Company search by name returns the CIK in one call:
  `curl -s -H "User-Agent: <name> <email>" "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=federal+home+loan+bank+of+pittsburgh&type=10-Q&output=atom"` → **FHLBank Pittsburgh CIK `0001330399`**.
- ⚠️ **The Archives directory listing is a TRAP.** `…/Archives/edgar/data/<cik>/<acc-no-dashes>/` returned SEC nav-chrome (`brokers.htm`, `privacy.htm`, …) instead of the filing manifest, and a naive filename grep looks like the filing is missing. **Use `https://data.sec.gov/submissions/CIK##########.json` instead** — it hands back `primaryDocument` per accession directly. That is the reliable path and it is one call.
- **HTML→text for a 2.7MB 10-Q:** `re.sub(r'<[^>]+>',' ',t)` + `html.unescape` + whitespace-collapse gets ~210KB of clean prose that greps fine. Tables survive as space-separated runs — readable, and good enough to pull a Funding Sources table by eye.
- **PNC CIK `0000713676`.** Its 10-Q **Table 11 (Details of Funding Sources)** is the single highest-yield table for a wholesale-funding question: deposits by type and borrowed funds by type, both with the YE comparative and the $ / % change already computed.

### Arithmetic worth keeping (so I don't re-derive it)
- **FHLB activity-stock ratio, derived not assumed:** FHLB-Pgh B2 activity stock $1,953.3M → $3,549.0M (+$1,595.7M) against advances +$40,949M ⇒ **~3.90% blended**. That is what lets a member's *capital-stock* line stand in as a read on its *advances* when the advances themselves aren't disclosed per-member. (Cross-checked: PNC's implied ~$26.7B from stock vs its actual disclosed +$27.4B. Close enough to trust the method, and I only used it as corroboration, never as the primary claim.)
- **System denominators for FHLB share math:** H1-2026 system advance growth = $810.7B − $677B = **$133.7B**. FHLB-Pgh's own H1 growth = **$40.9B**. So PNC's +$27.4B is 67% of Pittsburgh and 20.5% of the system.

### Behavioural — parked here on purpose, not tasks
- **I nearly shipped a shape as a cause.** The FHLBank's own 10-Q gave me "top-5 = 82.1%, members falling 128→126" and that *felt* like the answer. It isn't — it is equally consistent with arbitrage and with distress. **The motive question can only be measured on the actor's own balance sheet.** Note the pull: the shape was satisfying *because it was quantitative*, not because it was responsive.
- **The pre-registration mechanism works and is nearly free.** The 8/20 block cost ~10 minutes and made the 8/21 expiry write-back a checklist tick. **It also named in advance the derived line that would go stale ("10× across 3 expiries") — which is the part I would otherwise have missed**, because it isn't the position, it's a sentence about the position.
- **Verify at the row, not at your own record of having done it.** CREED asked for two `REG-T-07` edits; my STATUS claimed they were done on 7/30. They *were* — but I checked the TSV before replying, and that check costs seconds while being wrong costs a peer's trust in the registry.

### Half-thought, not pursued
- PNC is the large-bank max on PC-NDFI (16.93% of loans, my own `NDFI_COHORT.tsv`) **and** it is the member driving the biggest single-bank FHLB draw in the system. I have **no evidence** the two are connected — the 10-Q attributes the growth to loans broadly plus the acquisition, and I did not decompose PNC's loan growth by category. **Writing it down so it is a question, not a hunch that hardens.** If it were tested: does PNC's C&I-to-NDFI line grow at a rate that needs $27B of wholesale funding, or is that mostly the FirstBank book plus resi/securities?

---

## 2026-08-27 (Thu) — residue from the first session after 3 dark days

*Task ledger is NOT here — `MEMORY.md` §NEXT SESSION, per this file's own contract.*

### Tooling worth keeping
- **Recount a consecutive-session run at the series; never increment it from memory.** One `python3` pass over paired FRED pulls printed the whole run with a reset column and gave 19 sessions + the run peak + the driver decomposition in one shot. My file said 14 and I would have written 19 by adding 5 — which would have been right by luck and wrong as a method.
- **The wide-table regex trap is real and I hit it live today.** `grep -oiE '(a|b)[^.]{0,120}(c)'` against an IR page died with *"exceeds complexity limits"*. MEMORY already carries this: **grep the bare literal and eyeball.** Cost ~1 minute because the lesson was on file.
- **`curl` an IR host before trusting it:** `ir.westernalliancebancorporation.com` returns an Acquia *"Web Site Not Found"* page with **HTTP 200 and 970 bytes**. A byte-count check caught it; a naive grep-for-nothing would have read as "no announcement."
- **`until [ "$(TZ=America/New_York date +%H%M)" -ge "1602" ]; do sleep 30; done`** backgrounded = a close-watcher that notifies once and exits. Better than polling `date` between edits.

### Arithmetic worth keeping (so I don't re-derive it)
- **CCC/HY run, 7/31→8/26:** 19 consecutive >3.6×, peak **3.861 [8/26]**. Endpoints **CCC 1034→1031 (−3bp) / HY 285→267 (−18bp)** — the decomposition *is* the verdict.
- **WAL cycle closes since the 6/30 exit — zero below $78.** Two nearest: **7/08 $78.31 (+0.40%)** and **8/24 $78.39 (+0.50%)**. Deepest intraday lows: **8/27 $77.13**, 7/08 $77.49, 8/25 $78.00.
- **WAL/EGBN print sequence, both quarters:** Tue AMC → Wed AMC → Thu 10:00 call. 2025: Oct 21/22/23. 2026: Jul 21/22/23.

### Behavioural — parked here on purpose, not tasks
- ★ **Two superlatives crossed my desk today from sources I trust, and both were wrong.** PROME's *"nearest approach on record"* for WAL (7/08 was 8¢ nearer) and my own file's *"2026 max 1034"* (1039 printed 8/25). **Neither was checkable without pulling the series — which is exactly why neither had been checked.** A superlative is the claim most likely to be inherited and least likely to be verified.
- ★ **The most corrected-*looking* line in a file is a good place to hunt for stale figures.** HOMER's catch: my brief's bullet was **headed "RETRACTED"**, correctly reported a retraction, and then used the withdrawn evidence to support it — for three weeks, while my STATUS was already right.
- ★ **Today's obvious fix would have recreated the defect it was fixing.** CREED's fix (a) — re-point `VX-CREED-4.01` at the QBP — would have named a source that does not contain the value, which *is* the original defect. It only died because CREED **executed the fix and looked at the result** rather than reasoning about it.
- **Four of my own live surfaces were wrong in ways no threshold would have caught**: an oil-leg "FIRING" call 41 days stale, a leg cited as registered that is ungradeable, a buffer stated twice at two values, three superseded peer figures. **None of these trip an alarm. All of them travel.**

### Half-thought, not pursued
- **A "publication-shape" field for registered rows.** Today produced two rows whose levels live in *episodic prose/charts* rather than standing table cells (`CREED-T-03`'s NOO series; arguably FHLB's own combined report). A row could carry *"is this level in a table cell that prints every period, or in narrative that may not?"* — cheap, and it is the property that made T-03 gradeable-by-luck. **Not proposing it; MIDAS's ask ② is adjacent and still open with Will.**
- **Does regional CRE OREO deserve a vector?** It is the only Q2 recognition tell and it is on my surface — but n=1 quarter, and a 26% move on a $915M stock is small. **Base-rate before building.**

## 2026-08-27 (Thu, 2nd session) — residue from the price-correction + closeout pass

### Tooling worth keeping (re-derived today; next time, don't)
- **Settled closes + the PRIOR close in one shot** — the thing that caught the inverted day-change. `market.py` gives level and a % but not the reference it used, so re-derive the % yourself:
  `.venv/bin/python3 -c "import yfinance as yf; h=yf.Ticker('WAL').history(period='12d')[['Open','High','Low','Close']]; print(h.round(2).to_string())"`
  Multi-ticker form: loop `yf.Ticker(t).history(period='5d')['Close']` over the cohort and zip with `str(d)[:10]`.
- **Weekday assertion before writing any dated row** (claim_check will flag it later; cheaper now):
  `python3 -c "import datetime; print(datetime.date(2026,8,31).strftime('%A'))"`
- **Kernel state, checked at the artifact rather than the record:** `ls KERNEL/shadow/events/2026/08/` + `find KERNEL/audit -type f` + read each event's `actor_id`. An event id's UUID prefix is NOT a reliable owner tell — open the file.
- **sha256 a submission against its activation pin:** load the activation JSON, walk `commands[]`, `hashlib.sha256(open(c['path'],'rb').read()).hexdigest() == c['sha256']`.

### Arithmetic worth keeping (so I don't re-derive it)
- WAL 8/27: close **$78.71**, prior close **$79.60 [8/26]** ⇒ **−$0.89 / −1.12%**. Buffer to $78 = **$0.71 / 0.91%**. Intraday low **$77.13**; rally off low **$1.58**.
- KRE 8/27: close **$74.35**, prior **$74.58 [8/26]** ⇒ **−$0.23 / −0.31%**. **+23.9%** above the $60 line.
- ⚠️ **A buffer % and a day-change % are both "small positive numbers next to a price."** They are not interchangeable and nothing in the layout stops you swapping them. That swap is what inverted the headline.

### Behavioural — parked here on purpose, not tasks
- I typed an inherited integer (precondition ⑦) from working memory **twice**, wrong both times, in the same closeout. The fix that worked was `grep -rn` for the token across the dir before commit — not resolving to be more careful.
- The retirement rule was *correct* on `CCC_HY_TRIPWIRE` and the right answer was still "don't". Mechanical sweeps need one "what IS this object" read before executing.

### Half-thought, not pursued
- `market.py` prints a % without naming the close it differenced against. If it printed the reference date, this session's defect would have been visible at a glance rather than needing a separate history pull. Possible small ask to whoever owns that script — **not raised, not verified as feasible.**

## 2026-09-01 (Tue — spawned post-close for the `REG-T-02` fire; inbox drain 28/28)

- **Fire arithmetic, both bases, so nobody re-derives it wrong:** $78.00 − $77.26 = $0.74 → 0.95% (÷78) / 0.96% (÷77.26). Exit: $81.90 − $77.26 = $4.64 → +6.01% (÷77.26). Day −$0.87 / −1.11% (÷78.13).
- **yfinance `history()` had NO 8/28 bar for WAL/KRE (or most tickers) today** — 8/27 → 8/31. SPY/XLF had it. Not a grade defect (9/1 bar present, quote endpoint agrees). If it recurs, note it as an instrument quirk, not a missing session.
- **Cohort-sort recipe (reused from 8/20):** `NDFI_COHORT.tsv` has a `#` comment line ABOVE the header — `csv.DictReader` silently uses the comment as the header and returns nothing usable. Strip `#` lines first. `scipy` is not in `.venv`; use `pandas.DataFrame.corr(method="spearman")`.
- **AEOLUS 8/27 (×2):** Colorado ROD — if Lower Basin implementing agreements go unexecuted, shortage apportions by PRIORITY (Law of the River): CA senior shielded, AZ junior CAP absorbs. Apparent erratum: §10.7 drops the "not" in "shall not preclude or predetermine" (7 of 8 instances carry it). Mead consultation trigger = 1,000 ft (not 1,010). AEO-10 (no breach of 1,035 through 12/31) re-priced 30% → 65% after AEOLUS base-rated USBR's August under-projection (+2.19 ft mean, n=6). **Credit-relevant leg for me = AZ CAP-dependent munis/ag districts; CREED cc'd. No action; parked.**
- **DEWEY CRMT playbook (8/27):** the one transferable structure — "non-recourse" ABS ring-fenced for PAYMENT but cross-defaulted for CONTROL (§8.1(p): any servicer-termination event at any trust = term-loan EOD; §8.1(b) carves that debt out of the general cross-default). → ROADMAP backlog: do the bank-syndicate credits I cover treat sponsor-serviced securitizations the same way?
- **CREED 8/28 on WALTER-005:** the failure cohort (sub-$100M thrifts) ≠ CREED's OREO recognition cohort ($10-250B). QBP Table V-A has a `<$100M` class with a `Failed institutions` line — but pdfminer emits its columns out of order (trap #14); anchor on a known cell before quoting. Verdict 0.75 stands; low-priority backlog to run the class at primary.
- **Cold storage (SIG-046):** first negative 1H net absorption since 2007, vacancy 7.7%, but it is a COMPOSITION story (pre-2020 stock vacated, post-2020 absorbing). No bank on my surfaces names cold-storage collateral. CREED scope call.
- **Fifth Third has two things this week:** Delaware Life distribution pause (8/28) + the Sep 5-7 Comerica systems cutover. Different objects; do not fuse.
