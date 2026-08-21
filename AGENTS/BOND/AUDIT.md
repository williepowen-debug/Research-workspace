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
