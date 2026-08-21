# BOND — Boot-Document Audit · 2026-08-21 (Will-tasked)

**Scope:** every document the boot sequence reads or names — `STATUS.md` · `SCRATCH.md` · `MEMORY.md` · `thesis/PREDICTIONS.tsv` · `docket/CATALYSTS.tsv` · `workbook/SCHEMA.tsv` · `AGENTS/VOCABULARIES.tsv` · the three boot/closeout scripts · `CLAUDE.md` itself.
**Method:** read end-to-end, not grepped. Every claim below is verified at the artifact or reproduced with a probe. Two candidate findings were checked and **dismissed** — listed at the bottom, because a dismissed flag is part of the record.

---

## A · WRONG ON A LIVE SURFACE — fix these

### A1. FR2004 vintage split: the 8/12 print landed, four surfaces still say 8/05
The 8/12 as-of was pulled and written to `STATUS.md:57`, `VX-BND-04`, `DEALER_CAPACITY.md` header + table, and `NEXUS_BRIEF §`. **Still reading 8/05:**

| surface | text |
|---|---|
| `TRADE.md:74` | "✅ **FR2004 is LIVE and current through the 8/05 as-of**" |
| `STATUS.md:204` | "scoreable weekly and **current through the 8/05 as-of**" |
| `docket/CATALYSTS.tsv` row 2 | whole row's figures stop at `150.0 [8/05]` |
| `monitors/DEALER_CAPACITY.md:62–92` | body tables/prose still 8/05 **beneath a fresh 8/12 header** |

⚠️ **The DEALER_CAPACITY instance is the dangerous one — a fresh header CERTIFIES a stale body** (`finding_header_edit_is_the_edit_most_mistaken_for_maintenance`). Live figures: long-end total **149.2** (not 150.0), 11–21Y **61.2** (not 64.1).

### A2. The STATUS catalyst twin contradicts the docket on the QRA — and suppresses a load-bearing supply fact
- **`docket/CATALYSTS.tsv` row 4:** "✅ **CONTENT NOW ESTABLISHED AT PRIMARIES (2026-08-19)** … the Q3 QRA **froze coupon auction sizes** (marginal financing dollar → bills)."
- **`STATUS.md:222` (the twin):** "QRA (pattern-inferred — **still UNVERIFIED**) … **do not grade anything off it until it is.**"

**Frozen coupon sizes is a first-order supply input for this desk, and the human-facing twin instructs the reader not to use it.** 16 days stale. *(The twin is not wholly wrong — the DATE was never primary-verified and that process defect stands. But the CONTENT was established off two primaries, so the "don't grade anything" instruction is false.)*

### A3. STATUS twin carries a discharged action as still open
`STATUS.md:231` — 7/23 ECB GovC: "**still open** … the *action* is still owed: verify the ECB 2026 GovC calendar at the ECB primary and re-docket with a confirmed date."
**That action appears discharged:** `CATALYSTS.tsv` row 3 now carries a verified **2026-09-09 → 9/10 ECB Governing Council monetary-policy meeting (Berlin, press conf)**. Carried assertion nobody re-evaluated (`finding_dated_carry_item_has_no_expiry_check`).

### A4. Docket ↔ twin event-set divergence (CLAUDE.md closeout 12: "must not diverge in event SET")
| event | docket | STATUS twin |
|---|---|---|
| **8/26 2Y reopening `91282CRD5`** | ✅ row 20 | ❌ **absent** |
| 9/9–9/10 ECB GovC | ✅ row 3 | ❌ absent |
| 7/23 ECB owned-miss | ❌ absent | ✅ line 231 |

⚠️ **The 8/26 reopening is the row `docket_check.py` was built to catch.** It found it, the row was added to the docket — and it was never mirrored to the human twin. **The tool closed the gap on the machine surface and the human surface still has it.**

---

## B · THE CHECKS THAT SHOULD HAVE CAUGHT §A

### B1. `assertion_check` EXPIRED can see only 16% of the dates on the files it scans
The rule matches ISO dates only: `re.finditer(r"20\d{2}-\d{2}-\d{2}", l)`. **BOND surfaces are written in slash format.** Measured across the scanned set: **253 ISO vs 1,336 slash date tokens.**

⇒ **The catalyst twin — the one place past-dated pending items structurally accumulate — is written entirely in slash dates and is therefore invisible to the rule.** Probe found **13** clean past-date + pending-verb hits the rule cannot see, including **A2**.

### B2. Same rule: one `✅` anywhere on a line suppresses the entire line
`if guarded(l) or re.search(DONE, l, re.I): continue` — `DONE` includes `✅|resolved|graded|…`. These surfaces are **markdown table rows: one line carrying several independent claims.** One resolved clause suppresses every other claim on the row. **59 further past-date + pending instances are suppressed this way.**
*(Same bundling defect I sent VULCAN this morning — a strong half laundering a weak half in one sentence. It is now confirmed inside my own tooling.)*

### B3. `closeout_check --selftest` does not test half of what it claims
`monitors/closeout_check.py:55–59` → `return ac.selftest()`. It delegates **entirely** to `assertion_check`. **The numeric-drift checker has zero selftest coverage.**
`CLAUDE.md:43` says it "verifies the **CHECKERS**" (plural). It verifies one. `finding_verification_zero_is_ambiguous` — a check certifies its SCOPE.

### B4. Fixture counts in CLAUDE.md are stale in three places
Doc says **12** (closeout, line 43) and **10** (assertion, lines 43 + 244). Tools report **14** for both.

### B5. FR2004 is covered by no automated check at all
`boot_recompute` drift-checks the FRED set; FR2004 is the **NY Fed** API. That is why **A1** survived a clean `rc=0` on both boot and closeout this morning.

---

## C · DOCKET GAPS — what is not on the calendar

### C1. 🔴 The September FOMC is not on BOND's docket
**9/15–16** appears on **at least five other fleet surfaces**; BOND's docket has FOMC **minutes** (8/19) and no meeting. **This desk owns the curve and the Fed path, and its live T6 test grades on September-hike probability.**
⚠️ **The fleet itself carries two date variants (9/15 vs 9/16, plus the two-day form).** Verify at the Fed primary — **do not copy a sibling's date**; that is exactly the class that produced the 8/05 QRA and 8/20-vs-8/19 20Y errors.

### C2. Jackson Hole is on PROME's surfaces and not on BOND's — and it is late August, i.e. plausibly live now
Unverified here. A Powell Jackson Hole speech is a first-order long-end catalyst. **Flagging, not asserting a date.**

### C3. `docket_check.py`'s guarantee is narrower than boot step 5 implies
It diffs **TreasuryDirect coupon auctions** only. Every non-auction catalyst — FOMC, ECB, CPI, MTS, Jackson Hole — is **uncovered**. Boot step 5's framing ("a missing row is invisible") reads as general coverage; it is auction-only. **That is how C1 survived.**

---

## D · DATA HYGIENE (mechanical, low individually)

1. **KB enum violations vs `SCHEMA.tsv`** — `Conf`: `high` ×13, `med-high` ×1. `Epistemic`: `measured` ×10, `CONFIRMED` ×3. Boot step 7 mandates validating against SCHEMA; **nothing enforces it.**
2. **KB `Group` vocab** — `CREDIT`, `FED`, `FISCAL` are not in `NETWORK_GROUPS`; canonical is `CREDIT_SPREADS`. ⚠️ **I used `CREDIT` on three rows this morning** (`KB-BND-160/161/162`) — self-inflicted, today.
3. **`PREDICTIONS.tsv` Status has two tokens for one state** — `FAILED` ×4 and `FALSE` ×5. No schema documents the enum. **Any count of resolved-false predictions silently misses one group or the other** — that includes calibration.
4. **5 ACTIVE KB rows 1 day past `Stale_By`** (074, 089, 092, 093, 124); **10 ACTIVE rows with `Stale_By` empty.**
5. **Both boot-read reference files are old:** `SCHEMA.tsv` last touched **2026-03-27**, `VOCABULARIES.tsv` **2026-03-08**.
6. **`outbox/`: 19 loose packets vs 8 in `delivered/`** — SCRATCH already flags 5 unverified since May; the 8/27 content-check is docketed.

---

## E · SOFT / DURABLE-DOC DRIFT

1. **`MEMORY.md:9`** — "Held **eleven straight** benign resolutions through 2026-07-27." Date-scoped so **not false**, but the live count is **14** (THESIS, STATUS). The durable doc is 3 behind.
2. **`MEMORY.md:21`** — "calm (~275) while CCC (~970)". Illustrative, but CCC is **1035**.

---

## ✅ VERIFIED CLEAN

No missing files or broken references (33/33 paths named in `CLAUDE.md` exist) · all three boot scripts run, `rc=0` · no duplicate or gapped IDs in KB (162 rows) or PREDICTIONS (17 rows) · no future-dated or unparseable dates · all TSVs 13/13 field-count whole-file · **`CLAUDE.md` carries no live values** (correct per step 17 — only the 350/500bp thresholds, which are definitions) · THESIS header self-consistent after yesterday's fix · `BND-15` correctly the only OPEN prediction and not yet due.

## 🚫 CHECKED AND DISMISSED (not findings)

- **`NEXUS_BRIEF.md:218`** — IG OAS `80 [7/24]`, 28 days old. **Sits under `⛔ SUPERSEDED LAYER — 7/24–7/28 VINTAGE, NOT LIVE (bannered 2026-08-20)`.** Correctly-labeled history.
- **`STATUS.md:34`** — a `5.25 [8/14]` inside a labeled prior-note clause. The **live** cell reads `5.19 [8/19]` and matches `boot_recompute` exactly.

*(Both were flagged by my probe and dismissed on reading the rationale — `finding_deliberate_and_unnoticed_asymmetry_look_identical`.)*

---

# DISPOSITIONS — worked in order, same session (2026-08-21)

| # | Item | Disposition |
|---|---|---|
| **A1** | FR2004 vintage split | ✅ **FIXED on all 5 surfaces** (TRADE · STATUS ×2 · CATALYSTS row 2 · DEALER_CAPACITY body+table, 8/12 row appended). Re-pulled at the NY Fed primary first — 8/12 confirmed latest. **The 5th surface (`STATUS:26`) was found by the NEW check, not by my manual sweep.** |
| **A2** | QRA twin contradiction | ✅ **FIXED** — twin now carries the established content (Q3 QRA **froze coupon sizes**, signal did NOT fire) and keeps the *process* defect (date never primary-verified) as the surviving caveat. |
| **A3** | ECB action shown as open | ✅ **FIXED** — verified at the docket that the 9/9 row records *"DATE VERIFIED AT THE ECB PRIMARY 8/19"* and explicitly discharges the 7/23 miss. Twin replaced. |
| **A4** | Docket ↔ twin event-set divergence | ✅ **FIXED** — 8/26 reopening + 9/9 ECB mirrored; **all 12 dated docket events now verified present in the twin.** |
| **B1** | EXPIRED rule saw 16% of dates | ✅ **FIXED** — reads ISO **and** slash, resolves bare `m/d` **backward** (a forward resolution would hide expired work), 10-day floor so release-lag caveats don't fire. **+2 latent bugs found doing it: `owed` matched inside "showed", and `\bwill\b` matched the operator's NAME** (10 false positives — this desk writes "Will-ruled" constantly). |
| **B2** | Clause-scoped suppression | ⚠️ **INVESTIGATED, OVERSTATED, NOT SHIPPED AS DEFAULT.** My audit counted co-occurrence as suppression; most of the 59 rows are genuinely resolved. Measured across radii (±90→17 hits, ±250→9, whole-line→4) the tradeoff is **not monotone** — ±250 drops a *real* defect. **Default stays whole-line (quiet); `--strict` added for deliberate audit passes.** A tool that cries wolf is worse than one that misses. |
| **B3** | Selftest covered half the pass | ✅ **FIXED** — drift predicate extracted to a pure `gate_row_drift()`, `+8` numeric fixtures, `+6` lint fixtures, `+13` assertion fixtures. **`closeout_check --selftest` now runs all three: 41 fixtures, all passing** (was 14, one checker). |
| **B4** | Stale fixture counts in CLAUDE.md | ✅ **FIXED** in 4 places. |
| **B5** | FR2004 uncovered by any check | ✅ **FIXED** — `check_fr2004()` added and wired into `boot_recompute`. **Regression-tested against the exact pre-fix text: all four A1 lines fire.** Honors the sentinel; uses a NARROW guard because the shared `GUARD` list contains `✅` and would have skipped two of the four defects it exists to catch. |
| **C1** | September FOMC absent | ✅ **DOCKETED + mirrored.** **Verified at the Fed's own calendar: 9/15–16, two-day, SEP — decision lands 9/16.** The fleet's two variants (9/15 vs 9/16) were each half-right. Rest of 2026 captured: 10/27–28, 12/8–9. |
| **C2** | Jackson Hole absent | ✅ **DOCKETED with provenance stated, not glossed.** **8/27–29, Warsh's first keynote as Chair ~8/28** — on PROME's ledger since 8/18 **with BOND named as a consumer**. ⚠️ **Dates are SECONDARY**; primary unfetched by **three** independent attempts (PROME 403; BOND: WebFetch 403 + curl/browser-UA **host timeout** on deep URL *and* root). Recorded per `KB-BND-161`: **absence three-attempt strong, date single-sourced.** `re-test:` before 8/27. |
| **C3** | `docket_check` scope over-read | ✅ **FIXED** — boot step 5 now states plainly that it is **auction-only** and that a clean `rc=0` says nothing about FOMC/ECB/CPI/MTS. |
| **D1** | 14 rows outside the Conf/Epistemic enums | ✅ **NORMALIZED**, each mapped from **its own Source field**, with the original token preserved in Notes. No confidence judgment changed. |
| **D2** | 11 rows off-vocabulary `Group` | ✅ **NORMALIZED** (`CREDIT`→`CREDIT_SPREADS`, `HY_ENERGY`→`ENERGY_CREDIT`, `FED`/`FISCAL`→`RATES`). |
| **D3** | `FAILED` vs `FALSE` | ✅ **CANONICALIZED on `FALSE`**, originals preserved, **enum now declared and enforced**. ⚠️ *I first put the enum in the TSV as a `#` header line — `csv.DictReader` took it as the header, and my own new lint reported CLEAN off a wrong referent. Reverted; the lint now fails loud on a missing `Status` column.* |
| **D4** | `Stale_By` hygiene | ✅ **5 overdue rows dispositioned INDIVIDUALLY** (2 STALE · 2 CONFIRMED-atemporal · 1 extended with a stated reason). ⚠️ *My first advisory called an empty `Stale_By` a defect — the schema says "empty if the fact is static or atemporal." The advisory contradicted the schema it enforces; corrected.* |
| **D6** | 5 packets unverified 94 days | ✅ **CLOSED 6 days early. 4 of 5 verified DELIVERED by content** at each recipient (→ `outbox/delivered/`). ⛔ **1 genuine orphan: HENRY 5/19**, absent on 7 keys. **NOT re-sent** — the figures are 94 days superseded and re-sending stale marks is worse than the orphan. Bannered in place. |
| **E1/E2** | MEMORY durable drift | ✅ **FIXED** — streak pointer added (11 was date-scoped; live is 14) and the illustrative CCC level **removed rather than refreshed**, since a teaching file should carry no level at all. |
| **+** | DAEDALUS flag (`976b0b8e7`) | ✅ **FIXED, in scope** — `NEXUS_BRIEF:43` carried the retracted *"FRED series starts 2021-08"* verbatim for 3 days while §0 killed it upstream. **Upstream kill present, in-place amendment absent.** Annotated in place. |

## What the pass cost, honestly

**Four of my own audit findings were wrong or overstated, and all four were caught by testing rather than re-reading:** B2 (counted co-occurrence as suppression), the D4 advisory (contradicted its own schema), the D3 TSV header (corrupted the file and made my new lint report clean), and a future-date discriminator that killed a real fixture. **Each is in the code as a comment or a fixture, so the next pass inherits the correction and not just the conclusion.**

**Final state:** `docket_check` rc=0 · `boot_recompute` rc=0 (incl. FR2004) · `closeout_check` **rc=0 across all three checks** · `--selftest` **41/41**.

---

# STATUS.md AUDIT — read end-to-end 2026-08-21 (Will-tasked), all findings fixed same session

**18 findings. 239/250 lines after the pass (was 250/250 — a resolved section was archived, freeing 14).**

## Wrong / inaccurate

| # | Where | Finding |
|---|---|---|
| S1 | header §regime-flag | An **8/10 scoping caveat said the dashboard/composite/exits below were "the pre-forum 7/28 state, NOT re-scored."** True on 8/10, **false by 8/15** — five closeouts have since rewritten all of it. **A stale caveat telling readers to distrust rebuilt rows is worse than none: it discredits current work.** Retired, with the part that survives stated. |
| S2 | ×4 sites | **The retracted "29-day run above 5%" was still in LIVE USE in three places** (regime paragraph · configuration line · matrix evidence). The file's own header calls the figure FALSE. **Upstream correction present, in-place amendment absent** — same class as the DAEDALUS `NEXUS_BRIEF` flag, found again on the more important file. All marked; live is 32 sessions / 48 days. |
| S3 | divergence (a) | A cell **advertising "recomputed each boot"** carried **four stale values** (31/47, 10Y 4.63, DFII10 2.39). **The freshness claim is what stops the reader checking** — worse than a cell making no claim. Already twice-corrected before this. |
| S4 | IG OAS ×2 | *"flat within a ~3bp band"* (dashboard) and *"Band 79–82"* (matrix). It is **78→82, a 4bp band drifting WIDER**. **My own morning pattern-fix caught two instances of this and missed both of these because the phrasing differed** — third and fourth instances. |
| S5 | thesis pointer | *"This pointer has rotted TWICE (n=2)"* — it is **n=3**, and the third was the worst: THESIS's own header contradicted itself (H1 `v1.1.5` vs `Version: 1.1.6`). |
| S6 | catalyst prune note | *"7/2 FR2004 (still PENDING pull)"* — **false for 24 days**; the gap closed 7/28 and the series is current to 8/12. A **sixth** surface in the FR2004 stale-claim family. |
| S7 | arm falsifier | *"DEEP-LIT against: 2Y 4.33 / DFII10 2.43 / 10Y 4.69 [7/24]"* — **28 days stale on a falsifier's own live-state read.** Refreshed to 4.19 / 2.35 / 4.65; conclusion unchanged, evidence now true. |
| S8 | T7 premise drift | Said **"~2pp"** off 33.5 [8/12]; the last ORACLE pin is 28.5/30.0 [8/18] ⇒ **~5.5–7pp**, and `CATALYSTS.tsv` has carried the larger figure since 8/18. **The mirror diverged in the direction that made the premise look safer.** |
| S9 | DM cross-section | *"Latest"* column carried US legs at [8/18] while `boot_recompute` pulls both every boot. |

## 🔴 The substantive one

| # | Finding |
|---|---|
| **S10** | **The AU leg's stated limit was FALSE and its `re-test: every boot` had not been run for nine days.** The row read *"AU's ~1wk lag forced the window to end 8/12 — this instrument cannot yet speak to 8/13–8/20,"* which put the 19-yr-high 5.31 close and `sb0607` **outside** the cross-section. **RBA publishes `FCMYGBAG10D` through 2026-08-19** (pub date 8/21, n=**3,336** vs the 3,331 recorded) — so it speaks to 8/13→8/19 **including both events**, and the lag is **~2 days, not ~1 week**. ⇒ **The 9/3 deliverable's window can now extend to 8/19 on all four legs like-for-like.** ⚠️ **My first re-test hit the MONTHLY file (`f2.1-data.csv`, series `FCMYGBAG10`, no `D`) and returned "series not found" — which reads exactly like an unavailable series. The daily file is `f2-data.csv`. n=4 of this desk's claimed-unavailability-is-really-a-path-artifact class, caught only because the path was audited instead of the wall reported.** *A stated limit on your own instrument is a CLAIM, and it decays.* |

## Unnecessary / mislabeled

| # | Finding |
|---|---|
| S11 | **A 14-line section titled `★ UPCOMING` for two auctions that were both PAST and both GRADED** (20Y 8/19 → `BND-14` FALSE; 30Y TIPS 8/20 → `BND-17` TRUE), future-tense throughout, quoting `DFII10` 2.41. **Archived verbatim** (the frozen bars ARE the record) → freed 14 lines at the cap. |
| S12 | A 24-day-old meta-note about a 7/28 block rewrite — removed. |
| S13–14 | **`USD/JPY` and `Brent` rows kept BOND's OWN drifting yfinance copies of metrics SAM and BRENT own** — against root CLAUDE.md's *"don't maintain stale copies… one source of truth per metric."* Both 3 days stale; USD/JPY had drifted ~1 big figure from SAM's surface, and Brent carried an intraday bar against BRENT's settle basis. **Converted to owner-cited pointers.** |

## Self-inflicted, same day

| # | Finding |
|---|---|
| **S15** | **Mirror break: `BND-18/19/20` were registered this session and never mirrored into the STATUS scoreboard** — the exact step-17 pairing (PREDICTIONS OPEN IDs ↔ STATUS) that the closeout mirror check exists to catch, **broken by me about an hour after I ran that check.** Fixed; all four OPEN IDs now verified present. |

## Checker gap this exposed

**`assertion_check` could not have caught S11: its PENDING vocabulary had no token for "UPCOMING",** so a section header can advertise a past event as forthcoming indefinitely. Fixed with a **STRONG/SOFT split** — `upcoming|forthcoming` bypass the 10-day `MIN_AGE` floor (nothing can be upcoming about a past date at any age) while the soft vocabulary keeps the floor so release-lag caveats stay quiet. **+1 fixture; 42 total, all passing.**

**Verified clean after the pass:** `docket_check` rc=0 · `boot_recompute` rc=0 (incl. FR2004 vintage) · `closeout_check` **rc=0 across all three** · `--selftest` **42/42** · PREDICTIONS↔STATUS mirror verified · **239/250 lines**.

---

## STATUS follow-through — the three items Will approved (2026-08-21)

| # | Item | Done |
|---|---|---|
| **1** | **Catalyst table reordered chronologically** | The next event is now the **first row** (Mon 8/24, then the 8/25–27 cluster). Order was 8/11 → 9/10 → 8/5 → Watch → 8/19 → … with the imminent items buried mid-table. Standing and recently-resolved rows moved to a labelled tail. **A table whose job is "imminent catalysts + countdown" has to be readable top-down.** |
| **2** | **Two fired rows past retention pruned** | 8/05 QRA (16d) and 8/11–13 refunding (10d), per closeout step 12's ~1-week rule. ⚠️ **Pruned from the docket AND the twin in the same commit** — a one-sided prune would have re-broken the event-set parity fixed hours earlier. ⚠️ **By explicit ROW with the content read and reproduced first, never by date-key** — LABOR silently deleted rows in August doing exactly that. Both archived verbatim → `2026-08-21_STATUS_catalyst_rows_pruned.md`, including the raw TSV lines so either can be restored. |
| **3** | **August refunding block archived** | ~21 lines for a 10-day-old graded event, the largest single block on the file. Archived verbatim → `2026-08-21_STATUS_archive_august_refunding_grade.md` with the "trailing-12 spans a repricing regime" limit attached to the numbers, replaced by a 1-line pointer carrying the conclusion. |

**Net: 239 → 219 lines (31 of headroom).** Re-verified after: `docket_check` rc=0 · `boot_recompute` rc=0 · `closeout_check` rc=0 · `kb_lint` rc=0 · **composite re-sums 12/35 over 7 vectors** · **docket↔twin parity intact** · **PREDICTIONS↔STATUS mirror intact (BND-15/18/19/20)**.

**What is still NOT claimed:** that the file is *true*. Every defect SHAPE the checkers know is clear and the arithmetic and mirrors verify — but no check judges whether the analysis is still right, and my own sweeps demonstrably missed the IG wording twice and the "29-day run" once before a rescan caught them. A second reader would likely still find things.

---

# NEXUS_BRIEF.md AUDIT — read end-to-end 2026-08-21 (Will-approved)

**The file other desks consume. 245 lines. One systemic defect with several instances, not a scatter of unrelated ones.**

## The systemic finding

**`NEXUS_BRIEF` is a stack of dated editions, and supersession is declared at the TOP of each layer and NOWHERE at the point of use.** A reader who lands mid-file — by grep, by scroll, by following a "§4" reference — gets stale figures with no local signal that they are stale.

Measured: **§1 through §5 each appear 3×** across the stacked editions (§6/§7 twice). *"a reader landing on §4 cannot tell which edition they are in"* — and §4 of the top block explicitly claims to supersede "every rates/credit figure elsewhere in this file," which only helps a reader who has already found §4.

## Live-layer defects — a reader takes these as CURRENT

| # | Finding |
|---|---|
| **N1** | 🔴 **The live calendar carried `n=3` for the 30Y TIPS benchmark — a RETRACTED figure.** STATUS reconciled it to **n=7** on 8/20 (trailing-7 same-tenor same-TIPS window). **The correction never propagated from STATUS to the file other desks read.** |
| **N2** | The same calendar line described the **8/20 TIPS reopen in the future tense** — past, and graded (`BND-17` TRUE, +8.28pp). |
| **N3** | 🔴 **Jackson Hole and the September FOMC were absent from this brief entirely** — the same two events missing from my docket this morning. **NEXUS consumes this for its convergence framework**, so the gap propagated outward. Both added, Jackson Hole with its secondary-date provenance stated. |
| **N4** | **§3 and §4 of the SAME block disagreed on CCC**: §3 said "2026 max is 1034 (7/31), 18 observations at or above"; §4 said 1035 is a fresh 2026 high. §3 sits **above** §4, so first-read wins the wrong way. |
| **N5** | The block header read **"RE-PIN 2026-08-19"** while its own §4 was stamped **8/21** — a two-day-stale vintage on the block whose entire job is to say what is current. |

## Superseded content wearing live headers

| # | Finding |
|---|---|
| **N6** | **Three `##` sections below the supersession sentinel read as live instruction** — `Catalysts NEXUS should carry`, `EU rates`, `Cross-domain context`. The banner was **21+ lines above**; a reader landing on "Catalysts NEXUS should carry" saw **7/28 catalysts in future tense** and nothing telling them otherwise. |
| **N7** | The **retracted "29 CONSECUTIVE sessions"** figure, unmarked, in the 8/19 layer — a **third** file carrying that dead number after STATUS (×4) and the DAEDALUS-flagged `2021-08` line. |
| **N8** | **`Composite 13/35` in two places**; live is 12/35. |

**All eight marked or fixed at the point of use.** Verified by re-scan: every retracted/superseded figure in the file now carries a local marker within 3 lines.

## What I did NOT do, deliberately

**I did not restructure the file or collapse the editions.** The layered history is the record of how this desk's read evolved, and rewriting it would destroy exactly what makes a brief auditable by its consumers. The fix is **marking at the point of use**, not flattening.

**The section-number reuse (§1–§5 each 3×) is left standing** — renumbering would break any cross-desk reference that already cites a section by number, which is the same "stable API" argument that protects the two numbered rule-lists in root `CLAUDE.md`. The layer headers now carry explicit edition dates instead.

**Checks after:** `closeout_check` rc=0 · `boot_recompute` rc=0.

---

# thesis/THESIS.md AUDIT — read end-to-end 2026-08-21 (Will-approved) · v1.1.6 → v1.1.7

**Different lens from STATUS: a DURABLE doc. Step 17 says durable docs carry NO live values — they point to STATUS.**

## ✅ The discipline that held

**Zero date-stamped numbers in the entire document.** Both `KEY THRESHOLDS` and `POSITION VIEW` explicitly delegate live readings to STATUS, and the "State snapshot column was removed to stop cross-doc drift." Tested mechanically, not eyeballed. **This is the one rule the file kept perfectly.**

## Findings

| # | Finding |
|---|---|
| **T1** | 🔴 **A SUPERSEDED GOVERNANCE STATE — the worst, and it has no number in it.** The v1.1.4 note recorded legs (a) *indirect-sufficient-alone at the 15th per-tenor pctile* and (b) *drop dealer-as-bearish* as **HELD, "none has been base-rated."** **Will RULED implement 2026-08-20** — verbatim *"Approved on both - implement per your rec."* **A durable doc carrying a dead governance state is worse than one carrying a stale number: a reader re-checks a level; nobody re-checks whether a ruling landed.** |
| **T2** | **The body asserted flatly what this file's OWN HEADER had already qualified.** *"No Fed backstop at the coupon/long end"* stood unqualified while the v1.1.6 version note recorded `VX-BND-16` firing on 8/19. **Upstream qualification present, in-place amendment absent — the third file today carrying that shape** (after `NEXUS_BRIEF` via DAEDALUS, and STATUS's "29-day run"). |
| **T3** | **FR2004 vintage 8/05 → 8/12 in TWO places — the 7th and 8th surfaces.** ⚠️ **The 7th was missed by the guard I built that morning: `check_fr2004` scanned the live surfaces and SKIPPED THE DURABLE DOCS.** Extended coverage → it immediately found the 8th. **The derived figure was stale too** (−17.1% off peak; live −20.9%). |
| **T4** | **The thesis-kill's SOFR−IORB leg still cited `+1bp on one print`.** Fully reversed to −2bp; all three kill legs now un-met simultaneously. STATUS and TRADE were corrected 8/21 — the durable doc was not. |
| **T5** | **Scoreboard missing `BND-18/19/20`** (registered 8/21) — the same mirror break found on STATUS hours earlier, made twice in one day. Plus 5 live uses of the retired **`FAILED`** token. |

## 🔴 Open item this surfaced — flagged, not buried

**BOND pre-registered `BND-18/19/20` for the 8/25–27 cluster WITHOUT adopting the ruled MATRIX_V2 legs.** Those are BOND's own predictions and are unaffected — **but §1/§3c adoption is a separate action, ruled by Will on 8/20, still owed before 8/25, and today's pre-registration does NOT discharge it.**

## The rot class I closed instead of patching

STATUS's thesis pointer had rotted **four** times — three stale versions, once with THESIS contradicting *itself*, **and a fourth time within hours of me correcting the rot-COUNT**, because I bumped to v1.1.7 and the pointer still said v1.1.6. **Incrementing the count was treating the symptom: a version string duplicated across two files rots on every bump BY CONSTRUCTION.** The duplicate is now removed — this desk's own *one-source-of-truth-per-metric* rule, applied to a version string. STATUS carries the durable SUBSTANCE (label, conviction, posture) and points to THESIS for the number.

**Checks after:** all four rc=0 · 50/50 fixtures · THESIS header self-consistent (title and `Version:` both v1.1.7) · scoreboard mirror 20/20 · CHANGELOG v1.1.7 logged.
