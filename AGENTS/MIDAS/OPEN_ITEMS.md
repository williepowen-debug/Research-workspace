# MIDAS — OPEN ITEMS REGISTER

> **Split out of `STATUS.md` 2026-09-02** (read-cap hot/cold split; PROME 9/2 flag ② — *"your call of shape, no ruling needed"*; CARL pilot shape, WQ-154 `d1a600bad`/`2ed23c7c0`).
> **Why here and not STATUS:** the boot protocol's STATUS read is defined as *convergence matrix · live channel reads · exit triad · BOTTOM LINE*. This register is none of those — it is the standing open-items list, and it was **7.5 KB of a 32.5 KB budget**, forcing byte-shaving on every session's edit.
> ⛔ **This file is NOT dropped from the boot — `STATUS.md` carries the live top-3 inline and points here for the rest. Read it whenever you touch an open item.**
> **Consistency rule (both files or neither):** an item that changes state must be updated **here** and, if it is in the STATUS top-3, **there too**. STATUS's pointer names this file by path.

**Last updated:** 2026-09-11 ~01:4x ET (Fri) — **item 24 CLOSED** (the contract-identity guard is built, tested and boot-wired; KB-047's 7th instance closed with it). Items 20/22/23 unchanged and still open.

---

## 23. ⛔ THE AMENDMENT RULE IS **NOT SETTLED CANON** — WQ-161 is with Will, due 2026-09-15

⚠️ **Do NOT cite the mass-moving test or my clause 3 as canon. Two desks converging is not a ruling.** PROME registered the MIDAS↔ZHAO prediction-canon exchange as **WQ-161, due 2026-09-15** (cites ZHAO `083fbc4f5` / KB-ZHAO-137 and my L-48), recommending both clauses be encoded in `FORGE/PREDICTION_DISCIPLINE.md`.

🔴 **My clause 3 POSTDATES the registration and is not in WQ-161's text** — addendum routed to `PROME/inbox/` 9/2 so it reaches Will before the decision. **Clause 3 is the operative half:** the mass-moving test is a *judgment*, and it is the judgment a desk wanting to patch resolves in its own favour; requiring **the proof written into the row at patch time** makes it a checkable claim made *before* the act.

**Until 9/15 the standing behaviour is the conservative one: prospective-only, and flag rather than patch.**

## 22. 🟠 MIDAS-01 / MIDAS-02 CARRY NO NON-RESOLUTION CASE — found 9/2 by running ZHAO's sweep on my own book (n=2 of 2)

Both OPEN, both **resolve 2026-09-30**, and **neither declares what happens if the data is unavailable.** I built the catch-all for the NEW row (MIDAS-08) and left the older two undefined — `finding_a_ruling_governs_the_next_write_not_the_existing_state`.

✅ **Under my adopted amendment rule the fix would QUALIFY** — mass-neutral (no branch masses), changes nothing in any world where data publishes, and the world it changes is one where an outage scores as a forecast MISS, which is indefensible rather than unspecified.

⛔ **NOT APPLIED: WQ-91 (Will, 9/1) rules this class "no edit to the live rows" and names MIDAS-01/02 explicitly.** A self-derived rule does not outrank an operator ruling that names the row. **Routed to PROME/Will:** *does "no edit" bar a mass-neutral non-resolution status, or only the referent re-keying it was ruled about?*

⚠️ **STANDING INSTRUCTION TO THE 9/30 GRADER, placed here because this is the surface you read (L-48 applied to itself): if the data is unavailable, record STUCK, not MISS.**

## 24. ✅ **CLOSED 2026-09-11 — the contract-identity guard is BUILT, TESTED and BOOT-WIRED (route (i)). KB-047's 7th instance is closed with it.**

**What shipped:** `check_contract_identity()` + a hand-maintained `FRONT_MONTHS` map in `metals_watch.py` — a **local** volume pull, no `fetch.py` change, per PROME's rulings of 2026-09-05 ① and 2026-09-10 ①. It grades every `=F` pointer against its explicit front month **on the PRIOR settled session** (never the newest bar — KB-112's self-heal rule, encoded as rule 1 in the source), flags **DYING** below a 5% volume share, prints the level spread, and **trips rc=1 REVIEW** in the verdict: a fetch that *succeeds and returns the wrong object* is worse than one that fails, because it prints a plausible number. **A pointer whose history cannot be pulled is UNKNOWN and is listed — an absent discriminator is not a clean bill** (L-46).

**Tested, not asserted:** `metals_watch.py` **rc=1**, zero failed legs, stderr empty; `boot.py` **rc=1 REVIEW — metals watch**, all four legs clean (ledger staleness quiet · no predictions due · COT vintage current). **9/10 result: ALL FIVE DYING** — `GC=F` vol **86** vs `GCZ26` **164,390** (0.05%) · `SI=F` 138/54,865 · `HG=F` 933/48,742 · `PL=F` 4/28,309 · `PA=F` **0**/5,105; spreads **0.22–1.22%**. **KB-112 reproduced on fresh data, and the volume-duplication shape with it (9/10 carried 9/9's volume on all five months while both ETFs printed distinct volumes) — third instance.**

⚠️ **THE RESIDUAL RISK, NAMED RATHER THAN CLAIMED AWAY: `FRONT_MONTHS` is HAND-MAINTAINED and a stale map does not fail loudly — it just stops discriminating.** That is `finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction` waiting to happen from the other end. Mitigation shipped: the guard **prints the mapped month on every run**, so a stale map is visible in the output rather than silent. **A month-roll is now a maintenance obligation on this desk.**

**Route (ii) — a `volume` field on FORGE `fetch.py` — stays PROME's** (registered on PROME's owes, 9/10 packet ②). When it lands the local pull may retire; **my call, and I would keep the local pull unless `fetch.py` also exposes the PRIOR session's row**, which is what the rule actually needs.

---

### Record of the 9/5 finding (preserved — this is what the guard was built against)

**`metals_watch.py` had no contract-identity guard and its spot block printed five dying contracts.**

Verified at the settled **9/4** bars by volume: `GC=F` **16** vs `GCZ26` **209,167** · `SI=F` 57 vs `SIZ26` 41,845 · `HG=F` **890 (= HGU26)** vs `HGZ26` 33,325 · `PL=F` 0 vs `PLV26` 19,047 · `PA=F` **11 (= PAU26)** vs `PAZ26` 4,896. **Level spreads 0.27%–1.30%.** ⛔ Standing warning ② was written as a *gold* fact; it is a property of **every** `=F` pointer this desk quotes. → **KB-112, L-50**

⛔ **DELIBERATELY NOT PATCHED 9/5, and the reason is my own precedent.** A guard needs a **volume** field; FORGE's `fetch.py` `price_fetch` returns price/prev/change only. Two routes: **(i)** a local yfinance volume pull inside `metals_watch.py` — mine to build — or **(ii)** extending `fetch.py`, which is **PROME/FORGE-gated and is the 7th instance of KB-047.** Blind-patching a 28 KB instrument at session end is exactly how the 8/23 fix ended up **certifying** a second contamination (L-45).

**Harm assessment, stated honestly:** **zero to anything graded** — MIDAS-08 is COT data, the M1 kill-rail leg has been graded on **GLD (no-roll arbiter)** since the 9/2 repair, and GSR is basis-robust across the roll (KB-067). **The exposure is the DISPLAY line** — which is the surface a mislabelled figure reached Will from on 8/20. ⇒ real, bounded, and named.

**⚠️ Interim rule until the guard exists:** quote the **explicit contract month** (`GCZ26`/`SIZ26`/`HGZ26`/`PLV26`/`PAZ26`), never the `=F` pointer, and identify a contract from the **prior session's** row — the latest futures row's volume field is stale and self-heals.

---

## 21. ✅ MIDAS-08 — GRADED TERMINAL 2026-09-05: **(b) INDETERMINATE. CLOSED.**

**Δ net/OI = −1.9163pp** (54.9437% [as-of 9/1] vs the frozen 56.8600% [as-of 8/25]) against an (a) boundary of −2.00pp ⇒ **missed by 0.0837pp**. **M1 holds 4; composite 8/20; nothing re-rated.** Graded **as first published** (WQ-162), instrument run twice with totals reconciliation passing both pulls.

⛔ **The 0.0837pp miss was stress-tested BEFORE publication, not after being challenged:** (b) on **all four** defensible boundary conventions (registered −2.0000 · p25 nearest-rank −1.9294 · p25-as-cited −1.9200 · p25 linear −1.9189, tightest miss **0.0026pp**) and on **both** baseline conventions. Every one is a published statistic of the **frozen** reference; none was invented after the print.

🔴 **The `if_falsified` conditional is keyed to (c) and (c) did NOT fire** ⇒ the public re-read of *"a meaningful part of the 8/19 residual is spec flow"* and the correction routed to **BOND** are **NOT owed**. ⚠️ **Nor is that claim re-affirmed** — the week is genuinely indeterminate about it, and its **unquantified-share** limit stands. **BOND was sent an INFO packet** saying exactly this rather than being left waiting on an open row → `AGENTS/BOND/inbox/2026-09-05_from-MIDAS_midas-08-resolved-b-indeterminate-no-correction-owed.md`.

📊 **Calibration, scored against me:** P(b)=0.40 realised; the row pre-committed *"if (b) or (c) fires that departure was wrong"* — **it fired, and the n=7 conditional base rate (14%) beat my shock-adjusted 40%.** The masses were **not** re-tuned after BND-21 (fourth honouring of the freeze); under (b) that cost nothing, and **a costless draw is not evidence the rule is cheap.**

🔑 **New standing finding (L-49):** the registered metric is a **ratio**, and its denominator co-moved — net NC long fell **−15,210 (−6.25%)** while OI fell **−2.98%**, so the ratio moved only −1.92pp. **Not re-graded on the absolute** (choosing the metric after the print is the failure pre-registration prevents); recorded as a limit and as a **prospective** rule for the successor: *register both, ratio binding.*

🔴 **CONSEQUENCE — M1 IS BACK TO SCORED-4-WITH-NO-LIVE-TEST**, the exact gap MIDAS-08 was built to close. ⛔ **A successor is deliberately NOT registered** until *NO-VERDICT vs (d) INDETERMINATE* is ruled (item 4b) and **WQ-161 lands 9/15** — registering before then repeats the defect this row already found in itself. → `analysis/2026-09-05_MIDAS-08-GRADE.md`, **KB-109**

### 21-hist. The registration record, retained (it is the calibration evidence)


⛔ **TWICE OFFERED A MID-FLIGHT IMPROVEMENT, TWICE DECLINED (see §7–§8 of the registration note).** `BND-21` resolving TRUE raised the prior on branch (a) — **P(a) not re-tuned.** ZHAO's **STUCK** design (non-resolution is a *status*, not a mass-bearing branch) is **better than my (d) and I adopted it PROSPECTIVELY only** — retrofitting it would renormalise (a)(b)(c) from sum 0.98 to 1.00 and change the scored masses. **Third honouring of the freeze in three days, in three different currencies: a score (8/31 band fence), calibration credit (BND-21), and now a known-second-best design.**

**Why it exists:** M1 sat at **4 with no live test** — MIDAS-06 graded terminal 8/31 and its own cell said any further escalation needs a NEW registered row. Everything learned about M1 since (BOND's breakeven tension, the gold-basis work, the COT crowding) was **unregistered observation** and could not move a score.

**The question, which this desk and BOND both declined to rule on 9/2:** is gold's premium **spec-funded**? Δ net/OI vs the frozen baseline **56.8600%** [as-of 2026-08-25].

⚠️ **It is a ONE-LEG forecast and the design note says so.** The first sketch was a 2×2 over {positioning × price} — **wrong, because both legs are as-of 9/1 and the price leg is ALREADY OBSERVED.** A branch set treating a known quantity as a forecast dimension manufactures a harder-looking test than it is. ⇒ the price move is a **frozen conditioning fact**: `GCZ26` **4,694.50 [8/25] → 4,396.40 [9/1] = −6.350%**, exactly the COT window. **Only the positioning response is unknown** — and that is what makes it sharp.

**Branches (MECE, half-open, boundary owner named, declared catch-all):** (a) **Δ ≤ −2.00pp** ⇒ spec was a marginal price-setter ⇒ **M1 4 → 3** · (b) **−2.00 < Δ < +1.00** ⇒ hold 4 · (c) **Δ ≥ +1.00pp** ⇒ held/added through −6.35% = conviction not hot money ⇒ hold 4 **and the COT #3 impeachment materially weakens** · (d) NO-VERDICT catch-all (unpublished by 9/8 · reconciliation fail · as-of mismatch · code 088691 absent). **P = 0.40 / 0.40 / 0.18 / 0.02.**

⛔ **Boundary provenance:** full-sample weekly Δ, **n=867** (p25 −1.92, p50 −0.03, p75 +1.78, sd 3.315). The crowded-start conditional set is **n=7 only** and is context, **deliberately not load-bearing** — this desk already published one base rate off a too-short window and had to correct it (KB-042). **P(a)=0.40 departs from the 14% conditional base rate** because of the −6.35% shock and the CHASED composition; **if (b) or (c) fires, that departure was wrong.**

**If (c) fires:** my published *"a meaningful part of the 8/19 residual is spec flow"* must be re-read **in public** as too strong, and routed to BOND, which adopted that carve-out verbatim. **A falsifier that fails to fire is information about my falsifier, not a vindication of my read.**

---

## 20. 🟠 PGM MECHANISM (n=3) — the sweep is DISCHARGED; the INSTRUMENT ask is what remains

✅ **No-news sweep RUN 2026-09-02 after three carried sessions — NO-NEWS CONFIRMED.** Five hit criteria + an explicit non-hit list **frozen to file before the first query**; seven probes; nothing dated **2026-08-25 → 2026-08-28** on supply, sanction/policy, demand, market-structure or corporate. → `analysis/2026-09-02_pgm-0828-news-sweep.md`, **KB-101**.

🔑 **Stronger than absence:** the only published cause (*dovish Fed / softer dollar*) is **refuted by the same day's tape** — gold FELL on every basis (`GCZ26` −2.875% · `GC=F` −2.855% · GLD −3.244%) while **Pd rose +6.803%**, and the statistic is a residual **vs gold**, so a monetary root is regressed out by construction. ⇒ **the 8/4 "residually unexplained" disposition survives its strongest public challenger.**

🔴 **Two negatives worth carrying:** the **Russian-palladium duty channel is CLOSED, not quiet** — USITC voted **2026-05-29** that unwrought Russian Pd does **not** injure US industry ⇒ **no AD/CVD order at all**, despite Commerce's 109.1% CVD / 132.83% AD. And the only concrete supply item found runs the **wrong way** (Nornickel guidance *"aligns with expectations"*).

⛔ **STILL OPEN — and now the ONLY route:** re-open (c)'s three instruments (**PGM lease rates · COMEX/NYMEX PGM stocks · PPLT/PALL share-count flows**), confirmed by probe 6 as **not publicly retrievable at the needed cadence**. **HAWK 5th asking (9/2)**, PROME carrying. **An explicit "no access here" closes the loop and is accepted.**

⚠️ **Limits travel or the finding is misquoted:** bounds the **public-catalyst** hypothesis only, not "no cause" · **English-language, US-centric sources only — no Russian or Afrikaans reachable**, the hole most likely to hide a supply/sanction event in a Russia/SA-concentrated market · absence of news is **weaker** than a positive instrument reading. **I2 score UNCHANGED at 2 🟡** — no registered trigger fired.

---

## OPEN ON MIDAS (next session)

> 📁 **Closed rows (9) and the superseded BOTTOM LINE stack live in `analysis/STATUS_ARCHIVE_2026-08.md`** — moved 2026-08-27, never deleted. This section carries **only what is genuinely open.**

0. **🟠 BOTH REMAINING OPEN PREDICTIONS ARE KEYED TO REFERENTS THAT HAVE MOVED — ESCALATED, NOT REPAIRED.** → `analysis/2026-08-27_registered-specs-keyed-to-moving-referents.md`; packet in `PROME/inbox/`. **MIDAS-01** grades `GC=F close vs $4,113.70 [7/10]` — a GCQ26-era anchor now graded by GCZ26; gold **+11.78%** above anchor, **19.5% clear** of the 10% kill line ⇒ **materiality LOW, stated as low.** **MIDAS-02** hardcodes the 2yr median at **239,400t** / RED leg **479,000t** vs today's **238,462t**; copper **+14.69%** above anchor, nothing at risk. 🔴 **The structural finding: the roll is a property of the TICKER, not of one row — every spec citing `GC=F`/`HG=F` was re-specified simultaneously, with no event.** ✅ **RULED (Option A, KB-070): both grade 9/30 on their frozen letters, ALL BASES PRINTED at resolution; DOCKET row 231 holds the grader-must-remember cost — do not re-carry it personally.** ⚠️ Provenance: the ledger nudge flagged this file and **I dismissed it**; Will's question forced the real check.

4. **✅ MIDAS-06 — GRADED TERMINAL 8/31: (a) DIVERGE PERSISTS. CLOSED.** DFII10 **2.42 [obs 8/28]** cleared ≥2.40 by **+2bp**; gold cleared $4,340.70 on **both** bases (**+3.165%** `GC=F` / **+4.359%** `GCZ26`, T+1 confirmed). **M1 3 → 4, composite 7/20 → 8/20.** No joint satisfaction, no adjudication owed; (a) was the modal branch (P≈0.45). ⛔ **The band that would have voided it was NOT applied** — see 4b. **Zero capital; no threshold, band or frozen letter set or moved.** → `analysis/2026-08-31_midas-06-TERMINAL-GRADE.md`, KB-092/093.

4b. **✅ ROW 66 — RULED 9/1: NARROW 2.37–2.43, prospective-only. CLOSED (compressed 9/2; see item 19).** The design draft (`analysis/2026-08-28_row66-noverdict-band-DESIGN-DRAFT.md`) stands as the record: DFII10's 1bp grid makes the band a **step function of its width**, collapsing five defensible σ windows to two (KB-082, L-39). 🔴 **Two MIDAS-06-relevant prints landed inside both candidate bands (2.40 [8/21], 2.42 [8/28]) and the fence was still not applied** — that is the honored-fence record, never a retroactive claim on row 68. ⚠️ **STILL UNRULED and it must be settled before a successor registers: NO-VERDICT vs (d) INDETERMINATE are different claims** — *the tape said no* vs *the ruler is too coarse to tell* — and a MECE branch set carrying both must say which fires.

7. **✅ RESOLVED 8/27 — magnitude-instrument revision history ARCHIVED (rotated 2026-09-02).** ⛔ **Cite 87.7–91.1% univariate · 90–93% currency-stripped (own measurement 93.0–93.8%) · 61–69% two-factor (a different question).** Verdict never moved: rates **8.9–12.3%** univariate, nothing >15% ⇒ **rates-ASSISTED**. ✅ **BOND's six-cell table DELIVERED 9/1 — the provenance owed since 8/23 is CLOSED** (see item 15). → KB-068, L-35; `analysis/STATUS_ARCHIVE_2026-08.md`.

9. **📏 N5/L-16 residue + a live proof.** Pt/Pd settlement clocks remain **PROVISIONAL**; **no settlement SOURCE exists for metals in `fetch.py`**. ⚠️ **Clause (ii-b) fired on my own desk 8/21** — a post-roll pull mislabelled the in-flight 8/21 session as an 8/20 close and I published it (see the banner). The fix is a settlement source, not more care.

13. **✅ CLOSED — inherited-window self-correction (rotated 9/2).** *"0 of 19"* → **20 of 1,103 = 1.81%**; *"P(c)=0.00%"* → **REGIME-EXTINCT** (none since 2009-01-13). ✅ **The rule-of-three 95% upper bound of 15.8% contained both the corrected rate and the realised outcome — the point estimate failed, the honest interval did not.** No MIDAS-07 change. → KB-042, L-18; `analysis/STATUS_ARCHIVE_2026-08.md`.

14. **Miner equities OUT OF SCOPE** (ruled 8/14, KB-039). Re-open trigger: miners diverging >20% from the metal over a quarter.

15. **Carryover:** China Cu imports −41.3% base-effect (ZHAO's series) · WPIC Pt-deficit PROV · sulfur/acid Platts **spot** print owed (L-14). ✅ **CLOSED 9/1 — BOND'S UNIVARIATE TABLE DELIVERED after three askings.** Six computed cells (`GC=F`/`GLD` × 2024+/5y/full), **band 87.7–91.1%**, matching my independent reproduction (87.6–91.1%) to the L-22 fork. ⚠️ **BOND logged the gap as its own failure: the packet was written 8/27 and sat undelivered in its `outbox/` for five days** — every one of my three asks was correct. *A packet written is not a packet sent.* ✅ **BOND's term-premium answer (8/27, KB-065): ~50/50 TP vs expected-path across all three horizons (40.1 / 52.3 / 50.7%) ⇒ licenses NEITHER label** — recorded plainly **because that is the direction that does NOT flatter M1**. ★ **The leg that DOES help: breakevens added only +3 to +5bp against a +26 to +56bp nominal move ⇒ ~90–95% landed in the REAL leg**, so the 7/17→8/7 kill-cond #3 fire really was gold rising through a genuine REAL-yield rise — **that strengthens the TEST it passed, not the verdict.** ⛔ **Four limits travel with it or don't cite it:** E[path] is a RESIDUAL · **this decomposes the NOMINAL yield — NEVER "the real yield splits ~50/50"** · KW deltas only, never levels vs ACM · **KW lags to 8/21.** Not a label move (C-36 stays CONTESTED); **do not stack with BOND's 8/18 rotation finding as two votes.**

16-bis. **⛔ CORRECTED 9/2 20:5x — THE GRADE WAS RIGHT AND I TOOK TOO LITTLE FROM IT (KB-107, L-48).** My **8/23 packet to ZHAO** registered the **construction sub-index against copper**, *"not just the composite"* — **KB-051 recorded only the composite**, and at grade time I read my own book. **August construction 46.9 = a NEW record low below July's 47.0, with copper firm $6.51–6.63.** ✅ **The registered condition FIRED; the structural attribution IS materially stronger and my self-deduction ① is withdrawn.** ⚠️ **Weather NOT closed** — NBS attributes to weather a **second** month; **ZHAO's settler adopted: September construction ~9/30 — rebound >47.5 retires the weather reading, a THIRD sub-47 retires weather entirely.** ⛔ **The construction→refined-copper LAG stays UNESTABLISHED** (ZHAO declined to manufacture one; a PMI is a diffusion index so any lag off it inherits unmeasurable amplitude). **Do NOT read "no lag estimate" as "no lag" — without it, 9/30 cannot settle channel-dead vs channel-not-arrived either.** ⛔ The **−41.3%** China copper-import figure is **NOT ZHAO-verified**; do not cite it as one. **I1 score UNCHANGED at 1 ⚪ UNSCOREABLE↑ — sixth demonstration of L-13(a).**

16. **✅ GRADED 9/2 — the I1 discriminator printed and it favours THIS desk's structural attribution.** NBS Aug (8/31): **composite 49.5 = second consecutive sub-50** (July 49.3), mfg **49.8** (+0.6, beat 49.7), non-mfg **49.0** (flat), while copper held **$6.51–6.63**. **The registered leg is SATISFIED on the letter** ⇒ ZHAO's 7/16 "property-only containment" frame stays marked WRONG and copper-firm-through-weak-PMI stays consistent with the structural/AI-grid read [KB-051]. ⚠️ **Two honest deductions.** ① The composite is sub-50 but **REBOUNDING** — production **50.4** and new orders **50.6** are back in expansion — so this strengthens the attribution **less than the spec's language implies**; ZHAO's typhoon caveat is now partly *retired* rather than confirmed either way. ② ⛔ **MY BRANCH SET IS NOT MECE** — "2nd sub-50 ⇒ structural" vs ">50 rebound ⇒ weather", no catch-all, no boundary owner; a rebounding sub-50 fits one on the letter and the other in spirit. **This is the first grade after Will ratified the MECE rule and it fails that rule** (see item 19). **Not a confirmed regime change.** Fleet decoy note: US-China truce expiry = **2026-11-10** (any August date is a 2025 artifact). → KB-098

19. **✅ WQ-142 + WQ-91 RULED (Will 9/1 "approve all of those with your recs") — CONFIRMED RECEIVED AND ENCODED 9/2.** *(PROME asked for a one-line confirmation at next boot; this is it.)* **WQ-142:** DFII10 NO-VERDICT band = **NARROW 2.37–2.43**, **prospective-only** (WIDE declined — its σ came from a different rate regime); MIDAS-06 unmoved. **Every successor row's branch set must be MECE** — half-open intervals with the boundary owner named (`[2.40, ∞)` vs `[2.20, 2.40)`) plus a declared catch-all; the band registers as an **admissible PRINT SET at registration** and cannot move afterwards. **WQ-91:** moving-referent class — **no edit** to live rows; **print BOTH bases at the 9/30 grades** (MIDAS-01, MIDAS-02, I1 band); forward rule = **name the contract, freeze baseline VALUE and DATE in the cell.** ⚠️ **First application found a live failure in my own registration the same day — see item 16.** ⛔ **Row 66 is therefore CLOSED as a question; NARROW is the ruling.**

17–18. **`GC=F` basis + KB-052 label — SUPERSEDED 8/28 by KB-080/087 (rotated 2026-09-02).** Retained live: **8/19 is basis-ROBUST** (GCQ26 +2.8264% / GCV26 +2.8146% / GCZ26 +2.8209%, 1.2bp spread), so the attribution write-up's core figure survives the roll untouched. Durable fix remains the `fetch.py` settlement source (KB-047, PROME/FORGE-gated). Full text → `analysis/STATUS_ARCHIVE_2026-08.md`.

---

