# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-08-21 ET (session 23 — instrument-integrity session. No primary pulled; six of my own marks moved anyway.)

## CHANGES SINCE (session 22 → 23)
Same day, hours later. Nothing external moved. **Everything this session found was already sitting in my own files**, which is the session's one-line summary.

## WHAT I DID (session 23)

### 1. 🔴 A boot warning I had been reading as housekeeping was a FALSE POSITIVE whose fix would have corrupted the file
Boot printed *"doubled quotes — CSV-quoting artifact… collapse `""` to `"`"* on four `PREDICTIONS.tsv` rows. **The quoting was correct RFC-4180**; following the advice would have broken the escaping and manufactured the exact corruption class the check exists to catch.

**Cause:** yesterday's parser fix repaired `read_tsv` to be csv-aware and left **`read_tsv_numbered`** — same module, forty lines below, *directly under the warning comment the fix had just written* — on the raw `split("\t")`. **The two readers disagreed on 5 of 6 ledgers.**

⚠️ **Why it read as benign: it MATCHED THE STORY I HAD JUST WRITTEN.** I'd spent the prior session on quote corruption, so "doubled quotes found" looked like the known problem being reported correctly.

**Shipped:** `scripts/tsvutil_selftest.py` — boot-wired, **6 ledgers × 4 invariants** (reader agreement · line-number truth · write round-trip · **stored line-endings**), with `--verify-guard` that restores the broken reader and **requires the check to fail on it**. → `4b4bd2362`

### 2. 🔴 "The unscorable-band family is n=3" was not a measurement — the census is 35 of 37
The n=3 in last session's SCRATCH was **a list of rows I happened to have noticed**, written in the grammar of a finding. Audit of all 37 live vectors: **35 defective.** The only two clean rows were the two I'd hand-fixed in the previous ten days.

**Fixed as a CONVENTION, not 35 rewrites** — five grading rules in the `VX.tsv` banner. Rule 1 changed **no** status, which is the evidence it codifies existing intent. Then **23 rows re-spec'd** individually for what convention cannot reach. Full census, one witness value per claim → `domain/sources/_archive/S23_BAND_AUDIT_2026-08-21.md`. → `9c012e213`, `b847148da`

### 3. 🔴 Six marks moved, and none was a misread of data
Each followed from **neither adopting nor refusing the row's own input** — and four times the row's own text already said the right thing. **`TX-03`** wrote *"this runs AGAINST the stress thesis and I am marking it that way"* and carried ELEVATED. **`1.02`**/**`1.04`** → UNSCORED. **`FL-02`** → CRITICAL (level band; had been de-marked on a *trend* argument, and asserted an SF mark with **no SF figure in the row**). **`EMG-01`** → NORMAL. **`2.05`** → **RETIRED** (NASS Farm Labor Survey cancelled permanently — no primary exists or is coming).

**Diagnostic, one pass:** read `Current Value` and `Status` as two independent claims, ask whether the second follows from the first. Four of six fell out that way.

### 4. ⚠️ The write-back caught two MORE of my own errors — one of them an hour old
- **`VX-1.04` UNSCORED was wrong.** I ruled its index onto BTS T-100 and marked it *"pending the pull"* — **the pull had already been run last session.** `baselines/bts_airport_pax.tsv` and `KB-APT-39` both held the stacks. Correct: **ELEVATED, index −13.15%**. *Already-fetched is not unavailable either.*
- **Checking that, I nearly retracted a KB row that was exactly right.** My throwaway script found no `pax` column and **silently fell back to positional index 3 = `domestic`**, returning FLL −20.32% vs KB's −28.09%. **KB reproduces to the cent on `total`.** `tsvutil.col()`'s own docstring warns against that fallback. ⚠️ **The band verdict was ELEVATED either way — a wrong number agreeing with the right one on the CONCLUSION is what stops you checking.**
- **`KB-APT-39` still carried the anti-correlation claim retracted the same day it was written.** Over 48 months the three FL airports are all **POSITIVELY** correlated (+0.33 to +0.76), so the 60%→35% MAR-24 cut **pointed the wrong way**. Correct replacement is the base rate: all-three-negative in **10.4% of 269 months**. → `7653b67e5`

### 5. 🔴 I rewrote a concurrent agent's commit — restored, and it is n=3 of a documented pattern
A backticked `` `total` `` in a `git commit -m "…"` was command-substituted and stored damaged. Repairing it with `--amend` **rewrote DAEDALUS's commit**, because they committed in the ~90s between my commit and my amend. **Restored to the original hash** (`git reset --hard fdf7caab8`) after verifying tree-identity, a globally clean tree, and nothing built on top. Nothing lost, nothing pushed in the window; DAEDALUS notified.

⚠️ **`finding_backtick_command_substitution_in_commit_message` already stated the rule in bold — "DO NOT AMEND… pushed or not" — and its n=2 is TERRY doing this identically on 8/18, three days ago.** The durable finding is that **documenting this has now twice failed to stop it.** Extended to n=3 with the hardened rule and the repair preconditions. → `2143107b0`

### 6. PROME desk review — one item taken, one premise corrected
Took the citation-form point (the contract-name guard lived in `notes` while the executable instruction in `what_to_check` named only `BZ=F`). **Corrected their roll premise:** Brent's Sep→Oct roll was **~8/3, before my window** — checked at the time, published in STATUS, and **confirmed in writing by BRENT**, who warned in the same packet against merging the `CL`/`HO`/`RB` 8/20 calendar with Brent's. PROME accepted in full. → `c1920883c`, `14604f108`

## NEXT SESSION
0. **🔴 Aug 22 (TOMORROW) — SECTION 338 PAUSE EXPIRES.** Deal / extension / tariff live? **Verify at a PRIMARY before any surface carries a branch.** Two of the three outcomes cut AGAINST the boycott-hardening read.
1. **🔴 Aug 24 (MONDAY) — THE ENERGY RE-ARM GRADES.** Re-pull the 8/21 settle **by contract name: `BZV26`**, and **cross-check `BZ=F` == `BZV26` before quoting either** (divergence ⇒ the continuous series has rolled). Grade off a SETTLE, never a live bar. ⚠️ **The next roll (Oct→Nov) is ~8/31 — seven days after this grade.**
2. **🟠 `VX-1.02` is UNSCORED until the NTTO PRIMARY WORKBOOK's vs-2019 column is read (~mid-Sep).** This is now also the `ES-MARCO-09` resolver. **Do not resolve either off the derived three-hop chain** — the row now formally refuses it.
3. **🟠 ~Sep 1 — Banxico July remittances.** First clean forward window for the re-spec'd SDL-01 tell (2-yr stack ≤−5%, needs 2 consecutive). **Co-run the state-of-origin map** (deferred twice). ⚠️ `VX-2.08`'s basis is now ruled to **COUNT, not dollars** — they disagree ($ +4.15% vs count +0.35%).
4. **🟡 ~Sep 11 — BLS August CPI = the `ES-MARCO-05` RESOLVER, pre-committed.** Sub-6% ⇒ DID_NOT_APPEAR. Do not push a 4th time.
5. **🟠 ~Sep 18 — FL Citizens. Ask CORAL for the refreshed PIF; do not re-derive.**
6. **🔴 CHANNEL 4 — the EMMA/MSRB credit leg is STILL UNRUN** (carried from 8/12; confirmed reachable 8/21). It **gates** a retire-or-hold ruling. `TX-03`'s BREACHED band now explicitly **cannot be tripped by receipts alone** — it requires this leg.
7. **🟠 15 residue rows closed this session, but `SDL-01`'s spec defect is NOT among them** — its problem is the instrument (bare YoY, no base guard), not band arithmetic, and the re-spec stays unscorable until #3 gives it a clean forward window.
8. **🟠 `VX-2.01` BREACHED still rests on an unrefreshed Jun-15 arrest rate.** Band is now exhaustive and `new sectors` requires NAMING the sector — but the scoring input is carried-not-confirmed. Needs an ICE/TRAC primary.
9. **Carried:** the FL-$ hole ($600M–$1.2B) still scope-mismatched and underived — **do not re-cite** · FL migration divergence vs BofA → CORAL · H-2A offer-premium pay-unit filter · `TX-01` needs a months-of-supply source (TRERC) · `H2A-02`'s consular leg unmeasured.
10. **Do NOT hunt a fifth Channel-1 transmission instrument.** v3.0 pre-commits against it; four nulls-or-against stand.

## OPEN THREADS
| Item | Status |
|------|--------|
| 🔴 **ENERGY RE-ARM — grades Mon 8/24** | 9 completed settles >$85 (8/10→8/20), accelerating; 8/21 `94.40` provisional. **Grade by contract name `BZV26`; next roll ~8/31** |
| 🔴 **Section 338 pause expires 8/22 — two-sided** | Tariff did NOT take effect. Primary-verify before any surface carries a branch |
| 🟠 **`VX-1.02` + `ES-MARCO-09` both blocked on the NTTO primary workbook** | The derived vs-2019 chain is formally refused. One read unblocks both |
| 🟠 **`VX-1.04` ELEVATED on a Spirit-dominated leg** | Index −13.15%; FLL's −28.09% is a SUPPLY shock. **Threshold reading, NOT FL demand withdrawal.** BTS runs ~3mo behind; June lands ~Sep |
| 🔴 **Channel 4 — EMMA/MSRB credit leg UNRUN** | Carried 8/12. Now *structurally* required: `TX-03` BREACHED cannot trip without it |
| 🟠 **`VX-2.01` BREACHED on an unrefreshed Jun-15 arrest rate** | Carried-not-confirmed |
| 🟠 **AEOLUS owes the PRIMARY CPC DJF read** | My read is trade-press; do not harden until the primary lands |
| 🟠 **`MAR-24` confidence was cut the WRONG WAY** | The 60%→35% cut rested on a refuted anti-correlation. Base rate is 10.4% of 269 months. **Confidence needs re-deriving from the base rate, not restored by default** |
| 🟠 **15 band-residue rows closed; 3 untrippable legs REMOVED** | `GTR-01` "searches collapsed", `ENF-01` "non-compliance surge", `2.06`/`2.05` "flat/declining while employment declining" (inverted its own scale) |
| 🟢 **El Niño → FL snowbird: sign flipped, now WITH the bearish read** | PROVISIONAL to the CPC winter outlook (Oct) |
| 🟠 **NV dollars leg inverted** · **Counter-print vs SDL-01 quantity** · **Foreign-born LF anomaly began 2025** | Carried 8/11 |
| 🔴 **FL-$ hole scope-mismatched + underived** | Carried 7/31 — **do not re-cite** |

## Mail state
**Inbox 0 · WALTER lane 0** (both drained at s22 close; nothing new arrived).
**Sent this session:** **PROME** (roll-premise correction + citation form + CRLF residue — packet `14604f108`, doorbelled; they accepted in full, no defense). **DAEDALUS** (disclosure that I rewrote and restored their commit `fdf7caab8`, plus the n=3 pattern — doorbelled, no reply owed).
⚠️ **Promotion flag owed to PROME:** I extended a COLD-tier auto-memory (`finding_backtick_command_substitution_in_commit_message`) with a new instance at **n=3** — Batch-A rule says that obligates a promotion flag carrying the n. **Not yet sent.**

## PUSH STATE
Session 23 — all work committed. ⚠️ **One history incident, fully repaired: `--amend` rewrote DAEDALUS's `fdf7caab8`; restored to the original hash after verifying tree-identity + clean global tree + nothing built on top.** Nothing was pushed during the window. **Rule adopted: do not `--amend` on this repo, at all; write commit messages via a quoted heredoc to a file.**
