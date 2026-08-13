# Athene/Apollo Q2 2026 — M-11 DUAL-test grade card
> ✅ **EXECUTED 2026-08-04 ~10:45 ET** (PROME-directed proxy). **Verdict: FULL NO-VERDICT DAY — both legs deferred, neither orphaned.** Worksheet §5 filled from 4 primary artifacts · **no band moved** (the one pre-authorized raise was checked and correctly declined: Q4→Q1 organic drift +$1,159M < $2.0B) · **no confidence touched** · packets to CREED + NEXUS. ⚠️ **Read §5a before citing leg 1: this card's leg-1 grade DATE was mis-specified** — the FABN slide has never appeared on an earnings day. Real grade dates: **leg 2 ≈ 8/6–8/10 (ATH Q2 10-Q)**, **leg 1 ≈ 8/12–8/18 (Q2-2026 FI Investor Presentation)**.

**FROZEN 2026-08-03 ~21:50 ET — BEFORE the print.** Written by a PROME-directed proxy session (SHADE dark since 7/27); every threshold below cites SHADE's own registered files. Items marked **⚠️ DERIVED-TONIGHT** were NOT previously registered and are derived here with the derivation shown — tomorrow's grader may tighten them from primary data but must not loosen them after seeing the print.

**Event:** Apollo/Athene Q2 2026 earnings + FI materials, **Monday 2026-08-04** (registered as "T+8, confirmed date" — STATUS §0e, 7/27).
**Design goal:** tomorrow's reader fills in numbers in §5 and writes verdicts. No judgment calls should be needed that are not pre-specified here.

**Ownership + confidence discipline (hard rules):**
- **M-11 (55%) is NEXUS's board row** (`AGENTS/NEXUS/STATUS.md` M-11, root R10 "recognition-perimeter integrity"). SHADE delivers leg readings; SHADE does NOT move 55%.
- **PRED-CREED-010 (70%, opened 7/27) is CREED's ledger.** SHADE routes the reading to CREED; SHADE does NOT re-mark 70%.
- SHADE's own registered surfaces that CAN move on this print: kill-path-1 state (YELLOW), the withdrawn "widening ~+15bp" claim (retired → re-test), the §2.8 landing-entity-gap thread (theoretical → material/closed).

---

## 1. Leg 1 — FABN peer-penalty canary refresh

### Registered baseline (all pre-print, sources dated)

| Quantity | Value | Source + date |
|---|---|---|
| Athene 5Y FABN secondary level | **T+123** | Athene FI deck 5/14–15/26 (Athene's own peer set: CRBG/EQH/PFG) — STATUS §0e |
| Peer penalty, Athene's deck | **+43–48bp** | same deck, 5/14/26 observation |
| Peer penalty, SHADE-independent | **≈+40.2bp median** (within-fund paired, n=15 funds, 11/15 positive, IQR −1.0 to +52.3; pooled +55.4, per-CUSIP +58.8) | SHADE NPORT-P rebuild, marks 3/31–5/31/26; `research/FABN_PEER_CANARY_INDEPENDENT_2026-07-27.md` |
| "Penalty widening ~+15bp Feb→May" | **WITHDRAWN → unestablished** (7/27) — re-test on THIS print | STATUS §0e |
| Q1'26 FABN gross issuance | **$2.0B** (vs $13.4B FY2025; "challenging market conditions") | ATH Q1'26 10-Q MD&A, via STATUS FABN-ladder section (6/22) |
| FABN outstanding | **$34.5B** (3/31/26) | ATH Q1'26 10-Q (6/22 ladder) |
| FHLB advances outstanding | **$28.2B** (3/31/26; +$4.9B QoQ — substitution channel) | ATH Q1'26 10-Q (6/22 ladder) |
| 2026-H2/2027 maturity wall | **~$13–18B bracketed** ($3.29B registered-fund par floor; 144A, exact size unverifiable by design) | NPORT-P bottom-up, `research/ATHENE_FABN_MATURITY_LADDER_2026-06-22.md` |
| Kill-path-1 state | **YELLOW** | STATUS §0e / kill-paths |
| **Registered RED bar** | **verified large 2026-H2/27 concentration AND (FABN spread >250bp OR a pulled syndication)** | CLAUDE.md kill-path 1 + STATUS 6/22 ladder section |

⚠️ **Framing correction vs the coordination layer:** NEXUS/PROME shorthand says "FABN refresh at ≈+40bp." **There is no registered pass/fail at +40bp.** ≈+40bp is SHADE's independent *corroboration estimate* of the deck's +43–48bp; the only registered escalation threshold is the >250bp / pulled-syndication RED bar. Leg 1 is a **canary refresh with bands**, not a prediction with a confidence — no HIT/MISS vocabulary applies to leg 1 itself.

### Grade from (source, in order of preference)
1. **Athene Q2 FI/investor presentation** (the May edition was the "Fixed Income presentation," 5/14–15/26) — the FABN secondary-spread + peer-comparison slide. Look on Athene IR (ir.athene.com, presentations page) alongside the 8/4 print; Apollo IR (ir.apollo.com) Q2 earnings materials/financial supplement as fallback.
2. If no Q2 deck with the FABN slide is posted on 8/4 → **NO-VERDICT day-one** for the penalty refresh (see band N below). Do NOT substitute the earnings-call narrative for the spread table.
3. **NPORT fallback is NOT available day-one:** the rerunnable script (`research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`, ~4 min) reads holder marks, and 6/30 NPORT-P filings lag ~60 days — usable ~late Aug/Sept, not 8/4.

Compare **penalty to penalty** (deck methodology vs deck methodology), never levels — NPORT marks vs deck levels are not like-for-like (registered limit, STATUS §0e).

### Frozen verdict bands (peer penalty, 5Y/like-for-like with the deck's own prior)

| Band | Reading | Consequence |
|---|---|---|
| **≤ +48bp** (at/below the 5/14 deck band top) | **STABLE** | Canary stays YELLOW; the withdrawn "widening" claim STAYS retired; no threshold moves. |
| **+49 to +57bp** | **INCONCLUSIVE** — ⚠️ DERIVED-TONIGHT: inside the noise implied by the NPORT within-fund IQR (−1 to +52, width ~53bp) | No trend claim either way; log the number, carry to next print. |
| **≥ +58bp** (≥ +10bp above deck band top ≈ the size of the withdrawn claim) | **WIDENING RE-ESTABLISHED** — ⚠️ DERIVED-TONIGHT (band edge = deck top + the ~+15bp claim's magnitude, rounded conservatively to +10bp) | Reinstate the widening thread as LIVE (it was withdrawn as *unestablished*, not refuted); escalate watch cadence; still YELLOW unless RED bar met. |
| **>250bp OR pulled/failed syndication** (with the ~$13–18B wall verified-large) | **RED** | Kill-path-1 escalation — the registered bar. Immediate packet to PROME + LIQUID. |
| **N: no Q2 FABN spread/peer disclosure on 8/4** | **NO-VERDICT (day-one)** | Record "not disclosed day-one"; re-check IR postings daily through the ATH 10-Q; NPORT re-run ~late Aug as last resort. A missing slide is itself a datum — the May deck carried it; note if the disclosure disappears. |

### Also record (mechanism row, fill regardless of band)
- Q2 FABN **gross issuance** (vs $2.0B Q1 / $13.4B FY25) — did the ~9–10-month public-syndication gap end?
- FABN **outstanding** (vs $34.5B) and FHLB **advances** (vs $28.2B) — substitution-into-encumbered check.
- Any **tender/maturity** activity on the 2026-H2/27 cluster (Athene was actively tendering series 2022-6 / 2020-5 at 6/22) — is the ~$13–18B wall shrinking (getting refinanced) or holding?

---

## 2. Leg 2 — Athene mortgage-loan line: the ARI $9B landing (PRED-CREED-010)

### Registered spec (verbatim from SHADE's copies of CREED's ledger — board_log 7/27 rows + STATUS §6)
- **PRED-CREED-010, 70%, opened 2026-07-27.** Resolves on **Athene Holding Ltd 10-Q Q2-2026, "Mortgage loans" line (~Aug 2026)**, cross-checked vs **Apollo 10-Q Retirement Services segment**.
- **SHADE's registered expectation (STATUS §6, 7/27):** book **+~10% ($93B → ~$102B)** *if* the ARI book consolidated into the mortgage-loan line. Baseline **$93B = Athene mortgage loans at 3/31/26** — ⚠️ rounded in SHADE files; **verify the exact Q1 figure from the ATH Q1-26 10-Q before computing Δ.**
- **The transferred book:** ~$9B ARI CRE loans ($8.9B pre-sale, 7.0% wtd-avg unlevered yield, mostly floating-rate first mortgages), **closed 2026-04-24 at 99.7% of total loan commitments** (8-K acc. `0001193125-26-177686` + EX-99.1, SHADE-verified primary). Close postdates 3/31 → Q2 is the FIRST observable (registered timing guard: never add $9B to any 3/31 figure).
- **§2.8 caveat (registered, SHADE-owned):** the Purchase Agreement lets Athene designate *"Affiliates, Managed Accounts or Portfolio Companies"* to take *"all or any portion"* by **private notice**, ACRA entities named as subsidiaries. **A flat or partial line is AMBIGUOUS evidence, not clean refutation** — pre-registered as a known failure mode of the instrument (CREED's own words: classification risk, not transaction risk — why 70% and not higher).
- **Joint grading (registered):** branch verdicts are joint with **PRED-CREED-006** (MBA Q2 CM/MF, ~mid-Sept, life-insurer line ≥ **+$10.0B measured as printed**; branch 2 reads "wholly or largely outside the Fed life sector"). **On 8/4 only the Athene half is observable — record the Athene reading; the joint branch verdict WAITS for the MBA print.**

### Grade from (source, in order)
1. **Athene Holding Ltd 10-Q Q2-2026** (EDGAR; ATH remains an SEC filer via public preferreds) — **the registered resolution instrument.** May NOT be filed on 8/4 itself; historically lands early-to-mid Aug.
2. Day-one PROVISIONAL only: Apollo Q2 press release + **financial supplement** (ir.apollo.com) and/or Athene financial supplement, IF they break out net invested assets / mortgage loans. Mark any supplement-sourced number **PROVISIONAL** and re-grade FINAL from the 10-Q.
3. **Never grade 010 off earnings-call narrative.**

### Frozen verdict bands — Δ ≡ (Q2 "Mortgage loans") − (exact Q1 baseline, ~$93B)

| Band | Reading | For PRED-CREED-010 (route to CREED, do not re-mark) | For M-11 / §2.8 thread |
|---|---|---|---|
| **Δ ≥ +$7.0B** | **LANDED (wholly-or-largely)** — ⚠️ DERIVED-TONIGHT: $7.0B ≈ 78% of $9B, mirroring the "wholly or largely" branch-2 language CREED filed for 006; SHADE files registered "~+10%/~$102B" but no explicit floor | Athene leg = **HIT** (pending Apollo-10-Q RS cross-check) | Landing VISIBLE in the consolidated line → the ARI benchmark held at good disclosure; §2.8 gap NOT material for this deal; recognition-perimeter leg WEAKENS for this instance |
| **+$2.0B ≤ Δ < +$7.0B** | **PARTIAL** — consistent with §2.8 portion-designation | **PARTIAL / ambiguous** — report the number; a half-landing must NOT be written up as a clean instrument failure (CREED's filed branch-2 discipline, adopted 7/27) | §2.8 gap ACTIVE — some portion routed elsewhere; run the mandatory follow-ups below |
| **Δ < +$2.0B** | **AMBIGUOUS-NOT-MISS** — the pre-registered classification failure mode (ACRA sidecar / securitization / "investment funds" line) | Do NOT report as thesis-refuting; report as "instrument did not see the assets" pending follow-ups | If consolidated assets rose ~$9B while the mortgage line didn't → **§2.8 landing-entity gap CONFIRMED MATERIAL** — a FINDING for M-11/R10, arguably the strongest M-11 outcome |
| **NO-VERDICT (day-one)** | 8/4 disclosures don't break out the line and the 10-Q isn't filed | Record "awaiting 10-Q"; set a re-check on EDGAR daily; FINAL grade at filing | No M-11 leg-2 reading yet — say so to NEXUS explicitly rather than letting the grade orphan silently |

⚠️ **DERIVED-TONIGHT lower bound ($2.0B):** Athene's organic QoQ mortgage-book drift is **NOT registered in SHADE's files.** Before finalizing PARTIAL-vs-AMBIGUOUS, pull the Q1-26 vs Q4-25 organic Δ of the same line from the Q1 10-Q; **if organic drift exceeds ~$2B/quarter, raise this floor to (organic drift + $1B) and note the change on this card with a timestamp.** Raising the floor after seeing the ORGANIC baseline is legitimate; moving any band after seeing the Q2 PRINT is not.

### Mandatory follow-ups if Δ < +$7.0B (any non-clean band)
1. Did **consolidated total investments/assets** rise by roughly the book's size anyway?
2. Any **ACRA / Designated-Buyer allocation disclosure** in the ATH or APO 10-Q? If disclosed → **§2.8 gap CLOSES for this deal** (registered closure condition, STATUS §6).
3. Check **"Investment funds"** and consolidated-VIE lines for a matching jump.
4. Cross-check **Apollo 10-Q Retirement Services segment** (the registered cross-check) when filed.

---

## 3. M-11 outcome matrix (fill after both legs)

| | Leg 2 LANDED (visible) | Leg 2 PARTIAL/AMBIGUOUS | Leg 2 NO-VERDICT |
|---|---|---|---|
| **Leg 1 STABLE (≤+48bp)** | Governance-benchmark instance: transfer visible, funding calm. M-11 opacity leg weakens for this instance; funding leg unchanged. | **The M-11 result:** perimeter opacity confirmed on a named $9B deal while funding stays calm — recognition-integrity thesis supported without any stress print. | Report leg 1 only; flag leg 2 pending. |
| **Leg 1 WIDENING (≥+58bp)** | Funding-cost leg strengthens; opacity leg weakens. Mixed — report both, no netting. | Both legs of M-11 strengthen — the strongest composite reading. Packet PROME same-day. | Report leg 1; leg 2 pending. |
| **Leg 1 NO-VERDICT** | Leg 2 only; note the FABN slide's absence as a disclosure datum. | Note BOTH halves unmeasurable day-one — that itself feeds R10 (recognition-perimeter). | ⬅️ **THIS CELL — SELECTED 2026-08-04 ~10:45 ET.** Full NO-VERDICT day: say so loudly to NEXUS/PROME; the grade is deferred, NOT orphaned. ⚠️ **But do NOT route it to R10 as the cell's middle-column text suggests:** per §5a both absences are **schedule artifacts** (FI deck never lands on earnings day, 13-for-13; 10-Q lands ~8/6–8/10), not perimeter opacity. **Deferred, not a finding.** |

---

## 4. Tomorrow's 15-minute procedure
1. Pull Apollo Q2 press release + financial supplement (ir.apollo.com); check ir.athene.com for a Q2 FI/investor deck; check EDGAR for the ATH 10-Q.
2. Leg 1: read the FABN spread/peer slide → pick band in §1 → fill §5.
3. Leg 2: read the mortgage-loan line (supplement = PROVISIONAL, 10-Q = FINAL) → verify exact Q1 baseline → compute Δ → pick band in §2 → fill §5.
4. Fill the §3 matrix cell. Append a `board_log.tsv` row with both readings (grade even if nothing moved — an unfired pre-registration that never gets graded is worthless, per the ARCC rule 7/27).
5. Packets (carve-out ①): **CREED** (010 Athene-leg reading, numbers only, no confidence move) · **NEXUS** (M-11 dual reading vs this card) · **PROME** only if RED bar or the widening band fires.
6. If leg 2 was PROVISIONAL/NO-VERDICT: calendar the ATH 10-Q re-check; finalize on filing.

## 5. FILL-IN WORKSHEET — **EXECUTED 2026-08-04 ~10:45 ET** (PROME-directed proxy; SHADE dark since 7/27)

**Artifacts read, exhaustively, before any cell was written** (all four are the entire 8/4 disclosure set):
① APO 8-K `0001858681-26-000036` [filed 2026-08-04] · ② ATH 8-K `0001527469-26-000047` [filed 2026-08-04] — **both carry the identical earnings presentation** `agmearningsrelease2q2026.htm` · ③ APO EX-99.1 press release `erex9912q2026.htm` · ④ **`Q2'26 Financial Supplement.xlsx`** (ir.apollo.com, 8 sheets). Full-text/all-cell scans for `mortgage`, `FABN`, `ACRA`, `designat`, `peer`, `basis point`. **ATH Q2 10-Q NOT filed** (data.sec.gov submissions API, CIK 0001527469 — last 10-Q `0001527469-26-000028`, 2026-05-07).

| # | Quantity | Pre-print baseline | **Q2 print value** | Source + date | Band/verdict |
|---|---|---|---|---|---|
| 1 | 5Y FABN peer penalty | +43–48bp (Q1'26 FI deck, 5/15) / ≈+40bp (NPORT) | **NOT DISCLOSED day-one** — no FABN spread or peer-comparison table in any 8/4 artifact | 4-artifact scan, 8/4/26 | **Band N → NO-VERDICT** *(see ⚠️ §5a — by construction, not by omission)* |
| 2 | 5Y FABN absolute spread | T+123 (5/15) | **NOT DISCLOSED day-one** | same | NO-VERDICT (carry T+123) |
| 3 | Q2 FABN gross issuance | $2.0B (Q1'26, 10-Q MD&A) | **NOT DISCLOSED — FABN not broken out.** ⚠️ Nearest printed figure is the **funding-agreement aggregate**: 2Q'26 **$5,718M** (vs 1Q'26 $8,531M, −33% QoQ; 2Q'25 $11,707M, −51% YoY; 4Q'25 trough $2,800M) | Q2'26 Financial Supplement, "RS Flows and IA", printed series, 8/4/26 | ⚠️ **NOT like-for-like** — the aggregate is FABN **+ FABR + direct FA + FHLB + LT repo** (its own fn.1). **Never compare $5,718M to the $2.0B FABN-only figure.** |
| 4 | FABN outstanding | $34.5B (3/31) | **NOT DISCLOSED day-one** | — | carry baseline |
| 5 | FHLB advances | $28.2B (3/31) | **NOT DISCLOSED day-one** | — | carry baseline |
| 6 | Mortgage loans, exact Q1 baseline | ~$93B (verify) | **$93,077M (3/31/26)** ✅ VERIFIED AT PRIMARY *(12/31/25: $91,918M)*. Related-party line $1,557M; consol-VIE line $2,031M — the registered line is the **$93,077M primary line** | ATH Q1-26 10-Q `0001527469-26-000028`, condensed consol. balance sheet, filed 5/7/26 | — (SHADE's "~$93B" rounds correctly) |
| 7 | Mortgage loans, Q2 | expect ~$102B if consolidated | **NOT DISCLOSED day-one** — absent from all four artifacts; the registered instrument (ATH Q2 10-Q) is unfiled | 4-artifact scan + EDGAR submissions API, 8/4/26 | **Δ = not computable → NO-VERDICT (day-one)** |
| 8 | Consolidated total investments Δ | — | **+$19,332M QoQ** — total investments incl. related parties $357,810M (1Q'26) → **$377,142M** (2Q'26), +5.4%. Net invested assets $300,290M → $314,090M (+$13,800M) | Q2'26 Financial Supplement, "Reconciliation_NIA and Alts", **printed series** (not derived by subtraction), 8/4/26 | ⚠️ **NON-DIAGNOSTIC.** 2Q'26 gross organic inflows $22,069M / net flows +$11,928M fully account for it. Balance-sheet growth **neither confirms nor excludes** a $9B ARI landing. |
| 9 | ACRA/Designated-Buyer disclosure? | none (§2.8 gap open) | **NONE.** No allocation, designation or portion disclosure in any 8/4 artifact (only routine ADIP/ACRA NCI flow lines) | 4-artifact scan, 8/4/26 | **§2.8 landing-entity gap stays OPEN** — unchanged, neither closed nor confirmed material |
| 10 | Organic mortgage-book QoQ drift (Q4→Q1) | NOT REGISTERED — pull first | **+$1,159M** ($91,918M → $93,077M). All-three-lines basis: +$1,121M ($95,544M → $96,665M) | ATH Q1-26 10-Q `0001527469-26-000028`, filed 5/7/26 — **pre-print instrument only** | ✅ **FLOOR CHECK RESULT: $1.159B < $2.0B → the $2.0B PARTIAL floor STANDS. No band moved.** *(The card's one pre-authorized raise was conditional on drift >~$2B. It is not. Timestamped 2026-08-04 ~10:45 ET.)* |

**Verdicts:** Leg 1 = **NO-VERDICT (band N, day-one)** · Leg 2 = **NO-VERDICT (day-one)** — neither PROVISIONAL nor FINAL; nothing to provisionally grade · M-11 matrix cell = **row "Leg 1 NO-VERDICT" × col "Leg 2 NO-VERDICT"** → *"Full NO-VERDICT day: say so loudly to NEXUS/PROME; the grade is deferred, NOT orphaned."* · Packets sent: CREED **✅** / NEXUS **✅** / PROME **n/a — neither the RED bar nor the ≥+58bp widening band fired, so the card's conditional PROME packet is correctly NOT sent** (reported to PROME directly instead, this being a PROME-directed run).

**Consequences applied (card-stated only, nothing else moved):** kill-path-1 **stays YELLOW** (RED bar unmet — no spread print, no pulled syndication; the deck narrative in fact reports issuance "across FABR and FABN programs", though that is narrative and grades nothing) · the withdrawn "widening ~+15bp" claim **STAYS RETIRED** (not re-established, not refuted — untested) · §2.8 thread **stays THEORETICAL-OPEN**. **No confidence touched:** M-11 55% is NEXUS's, PRED-CREED-010 70% is CREED's.

---

### 5a. ⚠️ WHERE THIS CARD'S PRE-REGISTRATION FAILED — leg 1's grade date was wrong, and band N's consequence text is unsupportable

**The card assumed the FABN peer-penalty slide would appear on 8/4. It was never going to.** Athene publishes the FABN spread/peer table in a **standalone quarterly Fixed Income Investor Presentation**, furnished under its own Item-7.01 8-K and posted to ir.athene.com — **not** in the earnings materials, and **never on earnings day.** The May artifact this card cites is titled **"Q1 2026 Fixed Income Investor Presentation"**, furnished **2026-05-15** (8-K `0001527469-26-000032`) — i.e. **8 days after** the Q1 10-Q (5/7), not "5/14–15 alongside the print."

Cadence, EDGAR full-text search, CIK 0001527469, exact phrase *"Fixed Income Investor Presentation"* (27 hits), pulled 2026-08-04:
`2023-02-22 · 2023-05-18 · 2023-08-16 · 2023-11-09 · 2024-02-21 · 2024-05-09 · 2024-08-08 · 2024-11-14/15 · 2025-02-13 · 2025-05-12 · 2025-08-12 · 2026-02-19 · 2026-05-15` — **zero of thirteen landed on an earnings date.**

**Consequences for the grade:**
1. **Band N fires, but its consequence sentence is wrong for this instance.** "A missing slide is itself a datum — the May deck carried it; note if the disclosure disappears" reads absence as disclosure-quality evidence. **Here it carries none:** absence on earnings day is the 13-for-13 historical norm. This is **NO-VERDICT-BY-CONSTRUCTION**, and must not be routed to NEXUS/R10 as a recognition-perimeter datum. *(Recording the defect rather than smoothing it: this is the same class as SHADE's own 7/27 retraction #5 — an untested path assumption about when an artifact exists.)*
2. **Leg 1's real grade date is ~2026-08-12 to 08-18** (Q2-2025 analogue: 10-Q 8/7 → FI deck 8/12; Q1-2026: 10-Q 5/7 → FI deck 5/15). Re-check ir.athene.com and CIK 0001527469 8-Ks daily from **8/10**.
3. **Leg 2's real grade date is ~2026-08-06 to 08-10.** ATH Q2 10-Q filing dates: 2025-08-07 · 2024-08-08 · 2023-08-07 · 2022-08-09 · 2021-08-05. Athene's own financial supplement (which does carry the mortgage-loan line) was filed **with** the Q1 10-Q on 5/7 — expect the same pairing.
4. **Method note for the next freeze:** a grade card must check the **publication cadence of the instrument**, not just the event date. This card banded the numbers correctly and dated the source wrongly.

**Other errata (cosmetic, changed nothing):** the header says "**Monday** 2026-08-04" — 8/4 is a **Tuesday** (Apollo's own release: "Tuesday, August 4, 2026"); the **date** governs and was correct. Separately, at the source rather than in this card: Athene's 5/15/26 8-K body says the call took place "today, May 15, **2025**" — a typo in Athene's filing; the artifact is 2026-vintage.

### 5b. NET-NEW at a primary, not previously registered — the Q1 10-Q already named the acquirer

ATH Q1-26 10-Q `0001527469-26-000028`, related-party note: *"Apollo Commercial Real Estate Finance, Inc. (ARI) – On January 27, 2026, **we** entered into a definitive agreement to acquire an approximately $9 billion portfolio of commercial mortgage loans from ARI. The purchase price is based on **99.7%** of the total commitment amounts of the loans... **The transaction closed on April 24, 2026.**"

- **Second-primary confirmation** of the close date and the 99.7% (SHADE had these from the 8-K `0001193125-26-177686` + EX-99.1 only).
- **AHL names itself as acquirer in its own 10-Q, with no designation/portion language.** This does **not** resolve §2.8 — designation is by private notice and may occur at or after close, and a 10-Q related-party note is not an allocation disclosure — but it is the first time the **registered resolution instrument** has spoken on this deal, and it spoke in Athene's own name. Register as a **weak prior toward the LANDED branch**, not as evidence for it.

---

## 6. Discrepancy log (coordination-layer framing vs SHADE's registered files)
1. **"FABN refresh at approximately +40bp"** — not a registered threshold. Registered: deck prior +43–48bp (5/14); SHADE independent ≈+40.2bp (corroboration estimate, wide IQR); only registered escalation = >250bp / pulled syndication. Leg 1 has no confidence attached anywhere in SHADE's files.
2. **"Mortgage book grows ~+10%"** — MATCHES SHADE's registered §6 row (+~10%, $93B→~$102B). No discrepancy.
3. **"PRED-CREED-010 sits at 70%"** — matches; but it is **CREED's ledger**, resolves on the **10-Q** (which may lag 8/4), and its branch verdict is **joint with PRED-006 (mid-Sept)** — the 8/4 day-one read may legitimately be PROVISIONAL or NO-VERDICT.
4. **M-11 at 55%** is NEXUS's row and confidence, not SHADE's; SHADE reports legs, never the composite.

---

## 7. ✅ FINAL GRADES — executed 2026-08-13 ~13:00 ET by **real-SHADE** (first real session since 7/27)

> **Both legs are now GRADED against the frozen §1/§2 bands. NO BAND WAS MOVED.** The 8/4 outcome (`EXECUTED → NO-VERDICT (day-one), both legs deferred`) is hereby **CLOSED**: leg 2 FINAL from the ATH Q2 10-Q (filed 8/10), leg 1 FINAL from the Q2-2026 FI Investor Presentation (furnished **today, 8/13**). §5a's re-forecast of the grade dates — leg 2 ≈8/6–8/10, leg 1 ≈8/12–8/18 — **was right on both.**

### 7.1 Instruments (both are the registered ones, no substitutes)

| Leg | Instrument | Identifier | Filed/furnished |
|---|---|---|---|
| 2 | **Athene Holding Ltd 10-Q, q/e 6/30/26** | `0001527469-26-000056` | **2026-08-10** |
| 1 | **"Athene Fixed Income Investor Presentation August 2026"** (Item-7.01 8-K + ir.athene.com) | 8-K `0001527469-26-000063`; deck `Q2+2026+Fixed+Income+Investor+Presentation_FINAL.pdf` | **2026-08-13** (FI investor call 9:00 a.m. ET) |

✅ **§5a's method lesson is VALIDATED, not just asserted:** the FI deck landed on its own Item-7.01 cadence — **14 events, still ZERO on an earnings date.** Prior: 5/15 (Q1) → 8/13 (Q2) = 90 days; 10-Q→deck lag 5/7→5/15 = 8d, 8/10→8/13 = 3d.

### 7.2 🟢 LEG 1 — FABN peer-penalty canary: **BAND "≤ +48bp" → STABLE.** The penalty NARROWED ~12bp.

Deck slide *"Athene's Superior Financial Metrics are Not Fully Reflected in Secondary Spreads"*, row **"5-year FABN Secondary Credit Spread to US Treasury"**. ⚠️ **Spread source is stated on the slide: "J.P. Morgan data as of August 7, 2026"** — the observation date is **8/7/26**, not 8/13.

| Deck | Athene | CRBG | EQH | PFG | LNC | Peer avg | **Penalty (avg)** | Penalty (range) |
|---|---|---|---|---|---|---|---|---|
| **Q1'26** (furn. 5/15/26) | **T+123** | T+80 | T+80 | T+75 | *(not in set)* | 78.33 | **+44.7bp** | **+43 to +48** |
| **Q2'26** (furn. 8/13/26), **like-for-like** (Q1's peer set) | **T+110** | T+73 | T+82 | T+76 | — | 77.00 | **+33.0bp** | **+28 to +37** |
| **Q2'26, as published** (4 peers, LNC added) | T+110 | T+73 | T+82 | T+76 | **T+89** | 80.00 | **+30.0bp** | **+21 to +37** |

✅ **The registered baseline reproduces EXACTLY.** 123−80 = +43, 123−75 = +48 ⇒ the card's "+43–48bp" is confirmed as Athene's own arithmetic, not a paraphrase.

**VERDICT: band ≤ +48bp = STABLE — on every basis, and not marginally** (+33.0 like-for-like, +30.0 as-published, vs a +48 band top). The +49–57 INCONCLUSIVE and ≥+58 WIDENING bands are **nowhere near**.

**Card-stated consequences applied, and nothing else:**
- Kill-path-1 **stays YELLOW.** RED bar (>250bp **or** pulled syndication) **unmet** — T+110 is 140bp inside it.
- The withdrawn *"widening ~+15bp"* claim **STAYS RETIRED.** It is now not merely untested but **actively contradicted**: the penalty moved the other way by −11.7bp like-for-like.
- **No threshold, band or confidence moved.**

🔑 **Decomposition — Athene tightened; the peers barely did.** Athene **−13bp** (123→110) vs like-for-like peer avg **−1.3bp** (78.33→77.00). ⇒ **~11.7bp of the 13bp is Athene-specific outperformance**, not a beta move in FABN spreads generally. On its own terms this is a **clean negative result for SHADE's kill-path-1 funding-cost thesis, and it is recorded as such.**

⚠️ **Two guards on this slide, both mechanism-relevant:**
1. **The peer set CHANGED — Athene added LNC**, the widest peer at T+89. Adding it lifts the peer average and **cuts the reported penalty by 3.0bp** (30.0 as-published vs 33.0 like-for-like). **Immaterial to the band**, and no accusation is made — but it is the measured entity setting its own comparison set, which is SHADE's registered **allocation-discretion** through-line. **Always report the like-for-like figure alongside the published one.**
2. **The RBC row is stale in BOTH decks** — footnote 5: *"RBC ratios are as of December 31, 2025."* The values are byte-identical across the Q1 and Q2 decks (Athene 441% / CRBG 430-440% / EQH ~475% / PFG 406%). **Never read 441% as a 6/30/26 figure.**

### 7.3 🟠 LEG 2 — mortgage-loan line / ARI landing: **BAND "+$2.0B ≤ Δ < +$7.0B" → PARTIAL.** Short of LANDED by **$103M**.

| Quantity | Value | Source |
|---|---|---|
| Mortgage loans, net of allowances — **Q1 baseline (3/31/26)** | **$93,077M** | ATH Q1-26 10-Q `…-000028` (verified 8/4) |
| Mortgage loans, net of allowances — **Q2 print (6/30/26)** | **$99,974M** | **ATH Q2-26 10-Q `0001527469-26-000056`**, condensed consol. balance sheet |
| **Δ (registered primary line)** | **+$6,897M (+7.41%)** | derived from the two primaries above |
| Δ, all-three-lines basis | **+$6,916M** ($96,665M → $103,581M) | related-party $1,557→$1,549M; consol-VIE $2,031→$2,058M |

**VERDICT: PARTIAL.** Both bases land in the same band; the reading is **robust to basis choice**. Registered expectation was +~10% / ~$102B — the print is **$99,974M**, a ~$2B undershoot of that expectation.

🔴 **7.3a — THE FINDING OF THIS GRADE: the verdict turns on a $0.3B error in the card's own input, not on the print.**

The Q2 10-Q related-party note prices the deal for the first time:

> *"**Apollo Commercial Real Estate Finance, Inc. (ARI)** – On April 24, 2026, **we** completed the purchase of a commercial mortgage loan portfolio, **including accrued interest, for $8.7 billion** from ARI."*

**The transaction was $8.7B, not $9.0B.** The card's LANDED floor was derived as *"$7.0B ≈ 78% of $9B, mirroring the 'wholly or largely' branch-2 language."* Against the **actual** size:

| Basis | Arithmetic | Reads |
|---|---|---|
| **Frozen letter** (Δ ≥ $7,000M) | $6,897M < $7,000M, short by **$103M (1.5%)** | **PARTIAL** |
| **Floor's stated intent** (≥78% of the book) | 78% × $8,700M = **$6,786M**; Δ = $6,897M ⇒ **79.3%** | **LANDED** |

⚠️ **THE LETTER GOVERNS. THE BAND IS NOT MOVED — the card forbids moving any band after seeing the print, and this session did not.** But the divergence is reported at every surface, because **"PARTIAL" must not be read downstream as "the assets did not show up."** They largely did. `finding_confidence_priced_against_thesis_not_letter`, run as the inversion test: had the floor been written as a **ratio** rather than a **level**, this grades LANDED. **Method lesson for the next freeze: when a band is derived as a percentage of a quantity you have not yet verified, register the RATIO and resolve the denominator at grade time — a level silently hard-codes an unverified input.**

**7.3b — Mandatory §2 follow-ups (Δ < +$7.0B), all run:**

| # | Check | Result |
|---|---|---|
| 1 | Consolidated total investments rose ~the book's size anyway? | $321,081M (12/31/25) → **$333,842M** (6/30/26). Rose — but **NON-DIAGNOSTIC**, as on 8/4: organic inflows swamp it. |
| 2 | **ACRA / Designated-Buyer allocation disclosure?** | **NONE.** Full-text scan for `designat` returns only hedging-instrument XBRL tags. **§2.8 registered closure condition NOT met.** |
| 3 | Matching jump in "Investment funds" / consol-VIE lines? | **NO.** Consol-VIE mortgage line **FELL** $2,140M → $2,058M; related-party mortgage +$63M. **No sidecar landing is visible.** |
| 4 | Apollo 10-Q Retirement Services segment cross-check | ⚠️ **NOT RUN this session — outstanding.** |

**7.3c — Residual arithmetic, with the caveats that make it non-probative:**
$93,077M + $8,700M = $101,777M expected on a full landing with zero other change; actual **$99,974M** ⇒ residual **−$1,803M**. Applying Q4→Q1 organic drift (+$1,159M) ⇒ residual **−$2,962M**.
⚠️ **This is NOT evidence of a §2.8 diversion, and must not be cited as such.** Four unmeasured effects sit inside it: (a) the $8.7B **includes accrued interest**, so not all of it is loan principal; (b) transitional floating-rate CRE loans **amortize and prepay fast** — a quarter of runoff on a $100B book is material; (c) **CECL day-one allowance** on acquired loans reduces the net carrying value; (d) **Q2 organic drift is unobserved** and need not equal Q1's. **The instrument cannot separate these — exactly the ambiguity §2 pre-registered.**

**7.3d — §2.8 landing-entity gap: still OPEN, but the diversion branch is now WEAKLY DISFAVORED.** Athene has spoken on this deal **in its own name in three primaries** — Q1 10-Q, Q2 10-Q ("**we** completed the purchase"), and the Q2 FI deck (*"Athene's notable 2Q transaction activity included **ARI commercial mortgage loan deployment**"*) — with **zero designation or portion language in any of them**, and the consolidated mortgage line moved **+$6.9B against an $8.7B purchase**. ⚠️ **The gap does NOT close**: no affirmative allocation disclosure exists, and §2.8 designation is by private notice. But "a material portion was routed elsewhere" now requires the diverted assets to be invisible in *both* the VIE and related-party lines **while** the primary line absorbed 79% of the book. **Moved from THEORETICAL-OPEN → OPEN, diversion branch weakly disfavored.** *(SHADE's own registered thread; no other agent's confidence touched.)*

### 7.4 §3 matrix cell — FINAL

**Leg 1 STABLE (≤+48bp) × Leg 2 PARTIAL** ⇒ the cell reading: ***"THE M-11 RESULT: perimeter opacity confirmed on a named $9B deal while funding stays calm — recognition-integrity thesis supported without any stress print."***

⚠️ **SHADE qualifies its own matrix text before NEXUS uses it.** The cell was written for a materially-invisible landing. **What actually happened is a largely-VISIBLE landing (79% of the book in the registered line) with funding calm** — so *"perimeter opacity confirmed"* **overstates it.** The honest reading: **the recognition perimeter mostly HELD on this deal.** The residual opacity is real but narrow — the ~$1.8B unexplained residual is **unattributable** (7.3c), and the §2.8 allocation remains undisclosed. **Recommend NEXUS record the cell as "leg-1 STABLE × leg-2 PARTIAL, perimeter largely held, residual unattributable" rather than the cell's stock sentence.** M-11's 55% is NEXUS's to move or not; **SHADE does not move it.**

### 7.5 Confidence discipline — unchanged, stated explicitly
**M-11 (55%) NOT touched** — NEXUS's row. **PRED-CREED-010 (70%) NOT touched** — CREED's ledger; figures routed, verdict is CREED's. **No SHADE band, threshold or confidence moved by this grade.**
