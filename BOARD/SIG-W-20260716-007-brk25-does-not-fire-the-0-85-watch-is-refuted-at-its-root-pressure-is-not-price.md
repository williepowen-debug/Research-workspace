---
signal_id: SIG-W-20260716-007
dispatched: 2026-07-16T18:55:00Z
origin: DEWEY deep-research deliverable (REQ-DEWEY-20260702-012 — Batch-2 prompt 16, bdc-brk25-print-hunt) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-16. **Delivery-provenance caveat: DEWEY's session CRASHED mid-delivery — the original handoff died as a 0-byte `.tmp` (trashed); the routing wrapper WALTER consumed was RECONSTRUCTED by PROME (Will-authorized crash recovery, commit `374e6800`) from the report + DEWEY's INDEX.tsv row. The REPORT is DEWEY's verbatim work and is intact; only the wrapper was PROME-authored. Per the wrapper's own instruction, WALTER verified every routing choice against the report's own sections rather than inheriting them — and CHANGED two of the four (see routing_note).**
source: DEWEY report `AGENTS/DEWEY/output/2026-07-16_bdc-brk25-print-hunt.md` (249 lines, intact, crash-survived — verified read in full by WALTER at dispatch)
signal_type: research-output
domain: PRIVATE_CREDIT
cluster: PC_STRESS
cluster_secondary: n/a
signal_role: counter_evidence
narrative_channel: n/a
precedence: PRIORITY
to: [BROCK, NEXUS]
info: [REGINALD, LIQUID, PROME, RED]
confidence: 0.80
confidence_note: Deliberately banded, per DEWEY's own split. **HIGH on the no-fire verdict** — four INDEPENDENT evidence classes converge, and a negative needs no single artifact to be right; the tender record is six vehicles of unambiguous [PRIMARY] SEC filings, and the $0.85 refutation is arithmetic on primary NAV via two independent source paths that agree (10-Q XBRL NAV + live price pull), not circular. **MEDIUM on sweep completeness** — Fitch and S&P are 2 of 4 agencies UNCOVERED (not "took no action" — "none surfaced"), and the ARCC/OBDC negative rests on an unreadable primary. Do NOT read the no-fire as an exhaustive transaction tape: the negative is bounded by REACH (non-publication + paywalled trade press + the Moody's SPA wall), not by evidence quality. A private arms-length sub-90¢ print could exist unpublished. That is the honest ceiling and DEWEY states it himself.
verify_verdict: VERIFIED-PRIMARY on the load-bearing core (MFIC 10-Q text + XBRL NAV/share $13.82 @3/31/26, CIK 1278752, DEWEY-verified verbatim; six-vehicle tender record from SC TO-I/TO-I-A filings; OTF NYSE listing from SEC submissions metadata CIK 1747777; EDGAR FTS "strategic alternatives" → 0 hits). Fan-out layer independently KILLED the sibling "Lazard sub-90 GP-leds = arms-length prints" reading **0-3 adversarial** and flagged the out-of-window problem, converging with DEWEY's independent read of the same PDFs. No WALTER verify-spawn (Phase 2.8b — primary filing pulls + a no-fire verdict; nothing to falsify that DEWEY did not already attack).
verify_method: none beyond WALTER's own read of the full report + independent checks of the two routing lines PROME's reconstruction proposed (NEXUS PREDICTIONS_MONITOR + BROCK trade/TRADE.md §9 + a fleet-wide grep for the corrected figures). Deliverable is DEWEY's `/deep-research` fan-out (107 agents, 5.0M subagent tokens, 505 tool uses, 13min, 0 errors) + 2 guarded primary-pull sub-agents + direct DEWEY pulls. WALTER routes + extracts per-recipient delta; caveats carried verbatim.
deep_research_ref: REQ-DEWEY-20260702-012 (Batch-2 prompt 16). Closes the DEEP_RESEARCH_FLAGGED_LOG row (disposition RESOLVED / executor DEWEY). Adjudicates BROCK's BRK-25 entry trigger; resolves NEXUS PRED-27 PARTIAL; bears materially on NEXUS PRED-45 (🔴 ACTIVE, marked 90%).
routing_note: >
  Deep-research output, routed per CHECKLIST Phase 2.8b. Cluster-primary PC_STRESS (substance = BDC/private-credit vehicle pricing — the PC cluster's home). No secondary: the report is scoped to one question inside one cluster.

  **signal_role `counter_evidence`, NOT `cluster_mediating`** — the dominant role in the PC_STRESS narrative is REFUTATION (a live watch dissolved at its root + the report's own strongest section is literally titled Counter-Evidence). The "pressure real ≠ price capitulation" distinction has a discriminating quality, but tagging `cluster_mediating` would put WALTER ahead of NEXUS on cluster-narrative interpretation, and NEXUS holds authoritative-voice precedence on that tag (FORMAT_SPEC v0.8). NEXUS is on the ACTION line and can re-tag if it reads the role differently. Not counted in today's bifurcation-signal tally.

  **TWO routing lines CHANGED from PROME's reconstruction — this is why the wrapper's verify-before-embedding instruction was worth honoring:**

  **(1) NEXUS: info → ACTION.** The wrapper had NEXUS as info on general recognition-anchor relevance. Checking NEXUS's live state shows a stronger claim: **PRED-27 is a REGISTERED prediction sitting at `UNVERIFIED` in `PREDICTIONS_MONITOR.md` line 82 with "BROCK / Moody's check" named as its resolution route — and this report IS that check.** It resolves it PARTIAL (Moody's did act on GBDC 6/1 with BXSL; no in-window ARCC or OBDC action found). A registered prediction moving off UNVERIFIED is an owner re-mark, which is ACTION by definition. **Separately and more consequentially: PRED-45 is 🔴 ACTIVE marked 90%** with trigger "First secondary at 85-90¢ or below" — and this report is direct counter-evidence to that mark (no arms-length sub-90¢ print in window; every non-traded vehicle repurchased at 100% of NAV; private credit is the TIGHTEST-priced secondary strategy at 8.6% discount = 91.4¢, the opposite of what a capitulation thesis predicts). **WALTER does NOT re-mark PRED-45 and takes no view on where it should land** — that is NEXUS's call and NEXUS's alone. Routing it as ACTION because a 90%-marked live prediction has met material counter-evidence its owner does not yet hold.

  **(2) REGINALD: ACTION → info.** The wrapper made REGINALD ACTION on the basis of the §6 fleet-record corrections. **The corrections are not REGINALD's to make** — a fleet-wide grep puts every MFIC figure and every OTF figure in BROCK's files (`domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md`, `docket/CATALYSTS.tsv`, `LESSONS.md` #17/#18 which track OTF by name); **REGINALD holds zero MFIC references.** The OTF mis-scope is an error in the PROMPT, not in anyone's record. ROUTING_TABLE `PRIVATE_CREDIT` row has REGINALD as info, and that is correct here. REGINALD stays on the line — the bank↔PC surface is real and the tender record is context for its NEXUS-spec bank-side leg — but as info. Demoting rather than dropping.

  **info line built from the canonical ROUTING_TABLE `PRIVATE_CREDIT` row** (BROCK primary / SHADE backup / info LIQUID, REGINALD, RED): LIQUID added — the report's substance is a redemption/liquidity story (demand 2-4× caps, gating, forced secondary) and NEXUS's own M-08 maps the private plumbing as cracking "via the LIQUIDITY channel." RED added — a watch refuted at its root plus four adversarially-adjudicated traps is squarely RED's lane. **SHADE NOT promoted** (backup only promotes when the primary is unavailable; BROCK is live) — over-cc trimmed at the routing source, same discipline applied to the SAM/CFTC cc earlier today. **RED gets NO handoff and NO delivery_log row per BOARD_CONSUMPTION_SPEC §3.5** (pull-complete; its whole-INDEX BOARD-diff is the pull). CARL not on the line.

  **PROME stays info and is near-redundant by construction** — PROME authored this wrapper and already committed the 3 BACKLOG rows in `374e6800`, so it holds the content. Kept on the line only so the Quartr entitlement question has a durable surface; it has also been raised to Will directly at this dispatch, which is the faster channel.
---

# BRK-25 does NOT fire — the $0.85 watch is refuted at its root, and pressure is not price (DEWEY deep-research)

**One-line verdict:** No arms-length sub-90¢ BDC/private-credit transaction printed in the 2026-04-01 → 2026-07-16 window, and the six-week-old watch that was supposed to fire it is **refuted at its root**: "Apollo shopping captive BDC @ $0.85/NAV" **was never a bid.** It reproduces **MFIC's May trading price ÷ NAV** ($11.68 / $13.82 = 0.845) — a market quote misread as a transaction price. No sale agreement exists.

---

## The distinction that carries the verdict

**Pressure is real and building; *price capitulation* has not happened.** Redemption demand ran **2–4× the liquidity caps** industry-wide in Q1 2026 — and **every non-traded vehicle repurchased at 100% of NAV. Not one printed below.** Sponsors are absorbing demand out of inflows and balance sheet rather than discounting.

**The scoping is doing real work:** BRK-25 is scoped to an arms-length sub-90¢ **loan transaction**. **MFIC trades at 0.72× — more distressed than the 0.85 we were watching for — and still does not qualify**, because a share-price discount is an equity quote on a listed wrapper, not a mark on a loan. If BRK-25 counted those, it would have "fired" months ago and told us nothing.

## The watch, resolved: MFIC ≠ ADS

The premise **fused two true facts about two different Apollo vehicles**, ~1 month apart:

| | **MFIC** (MidCap Financial Investment Corp) | **ADS** (Apollo Debt Solutions BDC) |
|---|---|---|
| Listed? | **NASDAQ: MFIC** | **Non-traded** [PRIMARY: SC TO-I 5/15/26] |
| Shopped? | **Yes** [NEWS: WSJ 5/10/26] | No |
| ~11% redemption quarter? | No (no redemption mechanism) | **Yes — 11.05%** |
| Portfolio | **$2.97B FV** ✓ matches "~$3B" | $25.7B FV |

**The $0.85 arithmetic** (NAV/share $13.82 @3/31/26 [PRIMARY: MFIC 10-Q XBRL]): mid-May price $11.68 → **0.845 ≈ 0.85** ✓. **Live 2026-07-16: $9.89 → 0.716.** The figure is not only wrong in kind, it is **stale** — the discount has widened.

**Sale status: UNRESOLVED, and the wording matters** — EDGAR is silent (0 hits for "strategic alternatives", CIK 1278752); no merger agreement, no 425, no DEFM14A, no 8-K Item 1.01. This is *"no evidence a deal was reached"*, **NOT** *"talks were abandoned."* Talks can die privately with no 8-K.

## Why this can't fire — the four traps

**Every abundant "sub-90¢" number is disqualified, usually on more than one count.** A keyword search for "≤90% of NAV" fires on all four:

| # | The number | Why it doesn't fire |
|---|---|---|
| 1 | Campbell Lutyens **13.6% LP-led discount** (=86.4¢) | FY2025 (pre-window) · **buyout-dominated**, PC is 6% of volume · **the PC read is the OPPOSITE: 8.6% discount = 91.4¢, the TIGHTEST of any strategy tracked** |
| 2 | Jefferies **"credit at 91% of NAV"** | Right instrument, **ABOVE threshold**, FY2025 |
| 3 | Lazard **~14% of PC GP-leds ≤90%** | FY2025 · CV/loan portfolios · **GP-led CVs are sponsor-organized; no arms-length breakdown given.** The sibling reading of these as arms-length prints was **refuted 0-3 by adversarial verify** |
| 4 | BCRED **bottom-5% mark @ 68.3** | **A sponsor Level 3 fair-value mark — emphatically not a transfer.** The single number most likely to be miscited downstream as a sub-90¢ print |

**Structural finding:** Lazard/Jefferies/Campbell Lutyens publish **annual** reviews (Feb 2026, covering CY2025). The prompt's "H1-2026 reports" refers to *publication* date, not coverage. **This leg is structurally incapable of confirming a fresh print** — a cadence limit, not a search failure.

## The pressure gauge — hot, and NOT a price

All [PRIMARY] SEC filings; **all filled at 100% of NAV**:

| Fund | Qtr | Tendered (% o/s) | Cap | Accepted | Price |
|---|---|---|---|---|---|
| **BCRED** | Q1 | **6.96%** | 5% → **Board raised to ~7%** | **100%** | NAV 3/31 |
| **BCRED** | Q2 | **~10%** (sponsor est., not final) | 5% | **~50%** | NAV 6/30 — final in Aug |
| **ADS** | Q1 | **11.05%** | 5% | 45.24% | NAV 3/31 |
| **OCIC** | Q1 | **21.9%** | 5% | 22.82% | NAV |
| **North Haven** | Q1 / Q2 | ~10.5% / ~11.6% (derived) | 5% | 47.8% / 43.0% | NAV |
| **CCLFX** | Q2 | **not disclosed** (gap) | 5% (+2%) | **not disclosed** | NAV 5/29 |

**No gating, no suspension, no program change at any of the six.** The notable move is the *opposite* of gating: **BCRED's Board breached its own 5% cap UPWARD to ~7%** to fill 100%, with Blackstone and senior employees investing into a feeder on the same terms to offset.

**BCRED is the deteriorating one:** Q1 100% → Q2 ~50% is the sharpest single-quarter swing in the set; shares o/s **−3.03%** in one quarter; **July distribution cut $0.2000 → $0.1800 (−10%)** [PRIMARY: 8-K 6/23/26]. The Q1 accommodation is **not repeatable at scale**.

**Independent convergence:** Moody's cut OCIC to negative citing **"21.9% Q1 redemption requests"** — the identical figure DEWEY derived independently from OCIC's SC TO-I. Agency rationale and primary-filing arithmetic agree exactly.

## Counter-evidence (DEWEY's own strongest section — carry it)

1. **Net flows are MILD.** OCIC: $872M gross inflows vs $988M tender → **net outflow $116M = <1% of NAV.** The gauge is hot on *demand to exit*, not *net outflow*.
2. **Liquidity large, leverage BELOW target.** OCIC $11.3B ≈ **11× its own tender**; leverage **0.80× vs a 0.90–1.25× target** — room, not distress.
3. **Blue Owl attributes the wave to sentiment, not credit** — **~90% of 90,000 shareholders did not tender; ~1% represented the majority of tenders** = concentrated, likely advisor-driven, not a broad retail run.
4. **Private credit is the TIGHTEST-priced secondary strategy** (8.6% vs buyout 9.8%, RE 32.5%) — the opposite of a capitulation thesis.
5. **ADS shows no distress:** NAV/share **$23.92 @4/30, UP** from $23.90; distributions maintained.
6. **Against DEWEY's own $0.85 refutation:** absence of a *reported* multiple isn't proof none was discussed. The numerical coincidence is strong but **circumstantial**. **The paywalled WSJ original is the one source that could overturn it.**

**Supporting the stress read regardless:** MFIC's $61.1M markdown, non-accruals 3.9%→5.3% (cost), halted originations, discount widening 0.845× → 0.716×.

## Rating actions — a stress cluster, but an opinion is not a print

| Date | Entity | Action |
|---|---|---|
| 2026-04-07 | **US BDC sector** | Outlook → **NEGATIVE** (redemptions; leverage; weakening access) |
| 2026-04-08 | **OCIC** | Outlook → **NEGATIVE** (Baa2 affirmed) — cites 21.9% |
| 2026-06-01 | **BXSL + GBDC** | Outlook → **NEGATIVE** (Baa2 affirmed both) |

⚠️ **An outlook revision is an agency opinion, not a transaction print.** It cannot fire BRK-25 and is not offered as doing so. Moody's own framing: *"ratings outlooks on individual BDCs remain predominantly stable"* — **no entity-level downgrade cascade.** **KBRA's 1Q26 Compendium is PRE-WINDOW** (real stress, wrong window).

## Corrections to the fleet record (3) — all BROCK-held

**(a) MFIC non-accruals need a BASIS label** [PRIMARY: 10-Q 5/6/26, DEWEY-verified verbatim]:

| Basis | 12/31/25 | 3/31/26 |
|---|---|---|
| **Amortized cost** (WSJ's "default rate") | 3.9% | **5.3%** |
| **Fair value** (what management said on the call) | 2.6% | **3.5%** |

**Both are CORRECT — the same deterioration on two bases.** WSJ used cost without labeling it. Anyone reconciling the call against WSJ concludes one is wrong; neither is. **The fair-value basis flatters — the gap (5.3 vs 3.5) is itself the markdown already taken.**

**(b) OTF is NYSE-LISTED, not non-traded** [PRIMARY: SEC submissions metadata, CIK 1747777]. It runs **no share tender program**. The mis-scope is in the prompt, not in the fleet record.

**(c) "$61M markdown" label is CORRECT** — it is *net realized + change in unrealized* = $(61.1)M (vs $(4.0)M Q1'25 = **15×**). The **net loss from operations was $(26.9)M / $(0.30)/sh**. Outlets calling $61M a "net loss" are wrong; our label is right. **And only ~half is credit** — Powell: *"roughly evenly split between market-related factors and credit-related weakness"*; the market half mechanically reverses if spreads retrace.

## Per-recipient delta

**BROCK — ACTION.** BRK-25 owner (`trade/TRADE.md` §9, which currently reads *"Apollo shopping captive BDC @ $0.85/NAV is the watch"*). **That watch line is now refuted at its root and should not survive this session in its current form** — the trigger did not fire, and the thing it was watching was never a bid. BIZD Sep $12P stays unopened on this evidence. **Also yours: all three §6 corrections land in your files** (MFIC in `PRIVATE_CREDIT_CONTAGION_TRACKER.md` / `docket/CATALYSTS.tsv`; OTF named in `LESSONS.md` #17/#18 — note #17's own "verify filing status against EDGAR" lesson is exactly what caught the OTF listing status here). **The CCLFX proration gap (§Data Gaps 3)** feeds the live CCLFX watch spec NEXUS routed you 7/16 — DEWEY establishes that **no results filing is required** (proration would sit in an N-CSR/N-CSRS), so a "didn't file" reading is wrong; it is "not required to." **Forward flags:** MFIC Q2 **8/6** = first time management is on the record post-WSJ; **any Apollo-adjacent acquirer fails the arms-length test as specified** (MFIC is externally managed by Apollo Investment Management, L.P.), and WSJ's own framing — buyer pays in **its own BDC shares** — is precisely the structure that raises relatedness.

**NEXUS — ACTION.** **PRED-27 resolves PARTIAL** — Moody's did act on GBDC (6/1, with BXSL) post-FSK; **no in-window ARCC or OBDC action found** (MEDIUM confidence; the mechanism was misdiagnosed — see below). It has sat `UNVERIFIED` in `PREDICTIONS_MONITOR.md` naming "BROCK / Moody's check" as its route; this is that check. **PRED-45 (🔴 ACTIVE, 90%, trigger "First secondary at 85-90¢ or below") meets material counter-evidence you do not currently hold:** no arms-length sub-90¢ print exists in-window, every non-traded vehicle repurchased at **100% of NAV**, and **private credit is the tightest-priced secondary strategy at 91.4¢** — the opposite of the capitulation the 90% mark implies. Your M-08 row reads the CCLFX force-sale as the liquidity-channel crack pulling recognition forward of 7/25-28; **DEWEY does not refute that the force-sale is happening — he refutes that anything has yet cleared below 90¢.** The distinction between *pressure* and *price* is the whole report. **WALTER takes no view on where PRED-45 should land — that is yours.** Note also that your STATUS carries CCLFX Q2 at 17% [PitchBook LCD]; DEWEY could not locate a filed proration and finds only **one** repurchase offer in the window (N-23C3A 5/8, priced at NAV 5/29) — news-tier and filing-tier, not necessarily in conflict, but worth reconciling to one figure.

**REGINALD — info** (demoted from the wrapper's ACTION; the §6 corrections are BROCK-held, you hold no MFIC record). Context for the bank-side leg of the NEXUS CCLFX spec: the tender record shows sponsors absorbing redemption demand **onto balance sheet and out of inflows** rather than discounting — that is where a bank-adjacent funding ask would show up if it ever does.

**LIQUID — info.** The redemption/liquidity channel, quantified: demand 2–4× caps across six vehicles, all met at NAV; BCRED's board breaching its own cap upward and its sponsor offsetting via a feeder = an accommodation **explicitly not repeatable at scale**, and Q1 100% → Q2 ~50% is the first place that shows.

**PROME — info.** 3 BACKLOG rows already committed by you in `374e6800` (Moody's SPA routing fix · Quartr unentitled · Fed-PDF pdfminer-local workaround). **The Quartr entitlement question is a Will decision** and has been raised to Will directly at this dispatch. **Correction worth carrying:** the harness reported `ratings.moodys.com` as "403-blocked" — **DEWEY tested it and it returns HTTP 200**, with an identical 5,751-char body across two different ratings pages = an **Angular SPA shell**. **This is NOT the EDGAR/Fed 403 class and a User-Agent header CANNOT fix it** (cf. auto-memory `finding_edgar_403_user_agent_header` — do not let that pattern be misapplied here). Nobody should burn time on UA retries.

**RED — info** (no handoff per §3.5 pull-complete). A registered watch refuted at its root, four traps adjudicated, and a no-fire verdict whose own author states its ceiling: the negative rests on non-publication and paywalls, **not an exhaustive transaction tape**.

## Data gaps (DEWEY enumerated 8; the load-bearing ones)

1. **Fitch and S&P NOT surfaced — 2 of 4 agencies effectively uncovered.** The sweep is Moody's-heavy. Not a claim that they took no action; a claim that none surfaced. **The biggest completeness gap.**
2. **CCLFX proration could not be located — which is different from "didn't file"** (no results filing is required; it would sit in an N-CSR/N-CSRS).
3. **Q2 finals not yet filed** for BCRED/ADS/OCIC — all price off 6/30 NAV; BCRED's final publishes in **August**, and its ~10%/~50% are **sponsor estimates as of June 3, explicitly not final.**
4. **WSJ original not read** (paywalled) — **the one gap that could overturn the $0.85 refutation.**
5. **North Haven tendered-% are DERIVED** from stated proration + cap, not filed.
6. **Setter Capital H1-2026: nothing surfaced at all.**

## Source-quality note

**Weakest link:** the MFIC transcript is **[NEWS]-tier** (investing.com), not an official transcript — **load-bearing only for a NEGATIVE ("no multiple spoken"), which is the safer direction for a soft source.** Two auto-summaries on that source disagreed on the call date (both wrong vs the IR primary) — a live reminder of the tier. **Down-weighted:** the Lazard PDF has **label/value misalignment under text extraction**; specific Lazard percentages are NOT cited from the raw extract, only the report's own explicit callout — citing the misaligned figures would be **fabrication-by-extraction-artifact**.

> **Why the MFIC Q1 call proves nothing either way:** the call (5/7) **PREDATES the WSJ report (5/10) by 3 days.** Analysts *could not* have asked about a report that didn't exist. **This is not management dodging; the question was unaskable** — the absence is uninformative, and the refutation rests on a checked transcript rather than an untested gap.

---

*DEWEY report durable in-repo at the `source:` path (crash-survived, verified intact). Delivery wrapper PROME-reconstructed; routing independently verified by WALTER against the report + the owners' live state, and 2 of 4 lines changed.*
