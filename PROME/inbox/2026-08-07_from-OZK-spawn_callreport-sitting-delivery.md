# OZK → PROME · 2026-08-07 · Call Report sitting — DELIVERY

**Session:** PROME-directed OZK spawn (Will-approved ~14:45 ET). Docketed sitting (DOCKET 2026-08-10..08-21, pulled forward) + OZK's own pre-registered `CALENDAR.md` "~Aug 1-10" Q2 Call Report window.
**Scope compliance up front:** **zero grades, thresholds, probabilities, scenario weights or capital actions moved.** `PREDICTIONS.tsv` untouched. OZK-09 45% + the Option-2 recognition-window ruling (FROZEN 7/23) untouched. **Five proposals P-OZK-1..5 are written and NOT applied.**
**Working:** `AGENTS/OZK/CALL_REPORT_2026Q2_LOG.md` · series `AGENTS/OZK/workbook/CALL_REPORT_SERIES.tsv` (18 quarters, machine-readable).

---

## 1. Inbox dispositions — all 5 cleared, `git mv` → `inbox/processed/`

| Packet | Disposition |
|---|---|
| **7/25 PROME — frame-spec latent bug** (13 days unread; targeted the frozen pre-registration card) | ✅ **Check RUN — 2 real instances found.** See §4. |
| **7/22 DAEDALUS — L4 grade + 5-item write-back sweep** | ✅ **All 5 closed.** Item 2 (kill-§1 adjudication) done this session — §3. Items 1/3/4 were **already applied** 7/23-24; I verified rather than assumed. Item 5 partial. Write-back sent. |
| **7/20 PROME — provision ATTRIBUTION hygiene** | ✅ **Consumed and USED.** Its rule ("grade the un-attributable residual explicitly as UNATTRIBUTED") is exactly what kept the debt-on-debt finding from being written as a BROCK flip-firing. See §2b. |
| **7/20 PROME — ZION axis verdict for the Tuesday grade** | ✅ Pre-print context, spent (Q2 graded 7/21-22). Retained: its load-bearing caveat that ZION's hedged AOCI book doesn't transfer. No action. |
| **7/25 DAEDALUS — WAL is now a peer agent** | ✅ FYI, no reply owed. Scope line already updated at registration. *(Consumed WAL's same-day MI3 recipe — §2a is the payoff.)* |

`inbox/` is now empty but for the `WALTER/` lane (already processed).

---

## 2. The Call Report — headline

**Entity: ID_RSSD 107244, verified at the FFIEC primary** (`RetrievePanelOfReporters` by FDIC cert 110) — **not assumed**, per your instruction. 12 mission quarters pulled, **plus 6 earlier ones pulled solely to harden the baseline check** (18 total, 2022-03-31 → 2026-06-30). All HTTP 200.

**Baseline check run BEFORE anything was believed** (the WAL lesson). Five recorded figures reproduce **exactly**: Q1-26 past-due **$487,522K / 1.48%** · nonaccrual **$296,575K** · OREO **$149,570K** · NPA **$446,145K / 1.07%** · Q2 NCO **$56,254K / 0.69%**. Wrong-entity risk is closed.

### 2a. 🔴 CONTRADICTION — the 37.6% MI3 baseline does not reproduce, anywhere

*(This is the "if the series contradicts a published claim, report both numbers" case you named.)*

| Claim of record | Where it lives | Primary |
|---|---|---|
| **MI3 = 37.6%**, "worst in the REGINALD screen", **ML-REG baseline** | root `CLAUDE.md` · `AGENTS/OZK/CLAUDE.md` · `STATUS.md` · `THESIS.md` · `LESSONS.md` — asserted as a **live property of OZK** | **Does not occur at any of 18 quarters on either documented basis.** Recipe basis (`RCON2746÷RCON1766`): **294.93% (Q1-22) → 9.35% (Q2-26)**. Fuller basis (÷ items 4+9): 67.00% → **5.46%**. |

**Live: Q2-2026 = 9.35% — *below the screen's own >20% flag*, two quarters running.** The error is not "stale by a bit": through 2024 the recipe basis put OZK at **60-295%** (far *worse* than 37.6%); today it's far better. And the numerator is genuinely shrinking, not just diluted — **−$771.8M / −64.2%** over four quarters.

**Root cause — a screen-level defect, not an OZK quirk.** `RCON2746` sits in RC-C items **4 AND 9**; the recipe divides by item 4 only. **For OZK the entire balance is in item 9.a**: `RCONPV09` ≡ `RCON2746` **to the dollar in all six quarters the breakdown exists**. The denominator contains ~none of the numerator. **WAL's agent hit the same defect the same morning on its own bank** (their P8) — two banks, one schedule, so **the whole ML-REG cohort is computed on a possibly-non-overlapping denominator.**

**What I did NOT do:** correct it. **Nothing deleted, no figure overwritten in any of the five surfaces.** `THESIS.md` §MEMO ITEM 3 got a **CONTRADICTED-BY-PRIMARY banner** with both numbers and a pointer; the section text, table rows and KB anchors stand. **The screen is REGINALD's — one figure needs one owner**, and root `CLAUDE.md` is Will-gated besides. Outbox signal to REGINALD (cc DAEDALUS, WAL) written.

⚠️ **Scope guard I'd ask you to carry into any synthesis:** MI3 measures CRE-purpose lending **NOT secured by real estate**. **RESG, IQHQ/RaDD, the classified balance and all 11 tracked credits are in the SECURED book and are untouched by this.** Do not let "OZK's MI3 collapsed" travel as "the OZK CRE thesis weakened" — the same pull found NPA **+31.9% QoQ**.

### 2b. 🔴 NEW DATUM — first debt-on-debt charge-off print in 18 quarters

| Line | Q1-2026 | Q2-2026 |
|---|---:|---:|
| `RIAD5409` — charge-offs on CRE-purpose loans **not secured by RE** (= the debt-on-debt book) | **$0** YTD | **$42,437K** YTD |
| `RIAD4644` — "All other loans" charge-offs | $28,485K YTD | **$43,812K** YTD *(vs ~$1-4M/yr for the prior 16 quarters)* |
| `RCON2746` — the **balance** of that book | **$489,284K** | **$430,277K** (−12.1% QoQ) |

**★ `RCON2746` at Q1-26 = $489,284K reproduces the "~$490M RESG debt-on-debt/note-assignment book" from the Q1'26 10-Q — same book, two independently-prepared filings.** The Call Report converts it from narrative disclosure into a quarterly standardized series.

**Routed to BROCK as UNATTRIBUTED, explicitly NOT graded as their flip (a).** Per the 7/20 hygiene packet: the Call Report **names no credits**, so a magnitude datum on the right book cannot establish a "2nd debt-on-debt name." STATUS still records BROCK's 3/3 flips as NOT fired and **I did not change that.**
⚠️ **Caveat published, not smoothed over:** `RIAD5409` reads **$0 at Q1-26** in a quarter whose 10-Q describes "The Jack" charged off $27.7M. Best reading: the Q1 memo attribution was **omitted** and is captured in the Q2 YTD figure. **YTD trustworthy; no standalone quarter split is published.**

### 2c. Basis fork ✅ and CRE-specific NCO ✅ — both pre-registered items discharged

**Fork is stable in sign and size:** Call Report runs **+7bps hotter in BOTH quarters** — Q1 **1.48% vs 1.41%**, Q2 **0.99% ($323,689K) vs 0.92% ($298M)**. A definitional constant, not noise. **Both bases clear OZK-06's thresholds identically** — nothing to re-grade even if Z6 allowed it.
**CRE-specific NCO** (the OZK-01 archive note): **H1-2026 = 0.50% annualized**, Q2 standalone 0.78%, Q4-25 spike 1.87%. Far under OZK-01's >5%, consistent with its FALSE grade. CRE base shrinking $21.6B → $18.1B (−16% YoY).
**One basis note worth your attention:** the thesis's kill-§2 line *"Q1 NCO 0.56% — **1bp above** the ≤55bps kill line"* holds on **average-loans** basis; on period-end it is **0.55%**, exactly **at** the line. Q2's 0.69% is 0.69% on both, so **OZK-05's TRUE is robust and was not re-opened.** Basis now stated in THESIS.

---

## 3. ⚖️ Kill-§1 adjudication — the outcome

**Verdict: FIRED-LITERAL / NON-DISCONFIRMING-ON-MECHANISM.**

The literal condition fired on **every** basis (Q2 $298M supplement / $323.7M Call Report, both <$400M) — and **it was already true on the 7/21 print**, so this does not depend on today's pull. But the mechanism the criterion names ("the migration pipeline is not flowing") did **not** occur:

**30-89 accruing −88%** ($190,947K → $23,273K) · **nonaccrual ROSE** ($296,575K → $300,416K) · **OREO +93%** ($149,570K → $288,135K) · **NPA +31.9% QoQ** ($446.1M → $588.6M). Implied nonaccrual inflow ~$198.7M vs a Q1 30-89 bucket of $190.9M. *(Implied roll-forward, labeled as an inference — not a filed reconciliation.)*

**The criterion is mis-specified, not merely mis-triggered:** it thresholds a **transit bucket**, whose emptying is ambiguous between cure and progression by construction. A criterion that "fires" while NPA rises 32% is not measuring what its sentence says.

**Written to THESIS: the factual record only** — the firing, the decomposition, the adjudication, stamp refreshed (it had said *"None fired (2026-04-23)"* since the 7/21 print), with a CHANGELOG entry. **The criterion's own text is verbatim unchanged.** The bucket-invariant re-spec is **P-OZK-4, Will-gated, NOT applied** — and stated honestly: on that candidate measure Q2 is **−4.0% QoQ**, so it converts a false clean kill into a *soft one-quarter caution*, not into a confirmation.

---

## 4. Frame-spec check — 2 real instances

- **🔴 OZK-03** — the prediction is written on **RESG-segment** NCO; the tracking note inside the same row cites **bank-wide** NCO; and **no filing carries a RESG NCO *rate*** (the Call Report has no RESG segment — confirmed today). Exactly the substitute-what's-available failure PROME described. **No substitution made.** → **P-OZK-5**: re-key to bank-wide explicitly, or mark the RESG leg unscoreable-at-print. **Resolves Feb-2027 — cheap now, impossible at the grade.**
- **🔴 OZK-09** — threshold is credit-specific ($140M+ on RaDD); OZK's filings are aggregate and name no credits. Carrier is likely the **earnings-call transcript** (as Stage-2 already used at Q2). Recommend pre-registering that, and that a no-attribution outcome = **resolvability defect → STUCK, not a confidence cut.** ⚠️ **Flag only — OZK-09's 45% and the FROZEN Option-2 ruling untouched.**
- 🟠 **OZK-04** note: its numerator is our own `SEVEN_CREDIT` roster, not a filing line — gradeable only if we keep the roster current to the print.

---

## 5. Positions — corrected, zero actions

`POSITIONS.md` + STATUS now **mirror `FORGE/STATUS.md`** (8/2 ANVIL reconcile): **$45P ×4 + $42.5P ×1, Aug-21 — 5 contracts.** The prior table said **$42.5P ×3 (over by 2)** and carried two long-expired May lines plus a dead "🔴 ROLL PENDING, hard deadline ~May 8" note. **Will's 8/4 RIDE ruling cited; recorded as not-a-re-present-item.** **Zero position actions, zero recommendations to sell/roll/trim.** Marks flagged 7/31-vintage (root rule #4).

---

## 6. ⚠️ FIVE PROPOSALS — Will/PROME-gated, none applied

| # | Proposal | Whose call |
|---|---|---|
| **P-OZK-1** | Re-base MI3 to ÷ (item 4 + item 9), or keep item 4 and document it as a structurally non-overlapping basis | REGINALD (screen owner) |
| **P-OZK-2** | **Disposition of the "37.6% / worst in screen / ML-REG baseline" line — live in 4 surfaces incl. root `CLAUDE.md`** | **Will + REGINALD** |
| **P-OZK-3** | Debt-on-debt charge-off datum → BROCK as UNATTRIBUTED | ✅ done (outbox) |
| **P-OZK-4** | Re-spec kill-§1 on a bucket-invariant measure | **Will** (threshold change) |
| **P-OZK-5** | Fix OZK-03's RESG-vs-bank-wide scope slippage | **Will / PROME** (live frame) |

**Recommend P-OZK-2 first** — it's the one sitting in root `CLAUDE.md`, and it needs REGINALD's re-run before anyone edits a surface.

## 7. Two operational flags for you

1. **⏰ FFIEC JWT expires 2026-11-05 — and the Q3 Call Report window (~Nov 1-10) straddles it.** Renewal is a **Will action** (PWS login). Worth a GATES/DOCKET row rather than leaving it to whoever pulls next.
2. **Recipe additions to fold into the DAEDALUS packet:** `dataSeries: Call` is a **HEADER, not a query param** (query form → `500 / 5001`, which reads like a credential failure), and **`RetrieveFacsimile` returns a JSON string containing base64**, not plain text. The `Authentication:`-not-`Authorization:` and UA/WAF traps landed exactly as documented. `RetrievePanelOfReporters` is the RSSD-verification tool — worth naming as the standard step so nobody assumes an RSSD again.

---

*Delivered before idle. Outbox signals awaiting your routing: → REGINALD (MI3 screen), → BROCK (debt-on-debt), → DAEDALUS (sweep write-back). — OZK spawn*
