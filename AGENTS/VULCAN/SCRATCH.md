> # ⛔ 2026-09-13 (Sun) — READ THIS BLOCK FIRST. PROME-spawned Tier-1 session (DOCKET **L330**, dated 2026-09-11, PENDING through two PROME boots — the 9/12 sweep printed DARK owners only and I had self-committed 9/11). ~20:2x → 21:5x ET. Markets shut since the Fri 09-11 close.
>
> ## ONE LINE: **`GPU-PANEL-01` IS FROZEN** — and the reconnaissance that unblocked it returned a **NEGATIVE that is worth more than the panel**: there is no publicly quoted 12-month H100 price at ANY of the four vendors, so tier `contract` is an EMPTY SET and the on-demand-minus-contract spread the instrument was designed around is **UNGRADEABLE**. Three misses recorded, none cured off-cadence. **Nothing was read tonight, and that is correct.** No score, band, threshold or capital path moved; `GPU_SERIES.tsv` still holds ZERO rows.
>
> ## 🟢 THE FREEZE (the live deliverable — 9/18 was five days out)
> - **Criteria C1–C5 + rules R1–R5 written to disk BEFORE the first fetch** (spec §9.1). Freezing after seeing prices is composition-selection and the ONLY defence is the ordering, made auditable at the time. **R2: the observed LEVEL is never an inclusion input.**
> - **Four tiers, sealed (§9.3):** `on_demand` Lambda·CoreWeave·Nebius·Crusoe (min 3 of 4; **8-GPU/single-node scale convention** — 8×SXM is one HGX baseboard) · `marketplace` Vast.ai H100 SXM 1-GPU (min 5; **n=10 tonight**, up from the n=3 that blocked 9/6) · `contract` **EMPTY** · `index` SDH100RT (neo-cloud) + OCPI-H100, both `term_normalized`.
> - **`SCHEMA.tsv` enums WIDENED** — `tier` gained `marketplace`+`index`, `source_class` gained `vendor_primary`. The 3-token enum could not express the panel **without merging a marketplace ask into a neocloud list price**, i.e. without destroying the dispersion this instrument measures. Caught only because I checked the validator before writing a row.
> - **`tools/gpu_panel.py` built · `--selftest` 16/16.** ⚠️ **It FAILED on its first run — on MY arithmetic, not the code's** (I asserted the dispersion fixture at 9.43%; it is 9.42%). Exactly `finding_test_the_guard_not_just_the_guarded`.
> - **Marketplace tier is MECHANIZED; on_demand + index are HAND-READ** via `workbook/GPU_PANEL_INPUT_TEMPLATE.json` — HTML marketing pages change format silently, and scraping them fails in the one direction that matters.
>
> ## 🔑 WHAT THE RECONNAISSANCE ACTUALLY FOUND [KB-163/164/165]
> - **No public 12-mo H100 quote anywhere.** Lambda's clusters are *"2 weeks – 1 year"* — **a RANGE is not a duration** (fails C3) and 1yr+ is contact-sales; CoreWeave/Crusoe/Nebius fail C1. **At four vendors returning the same negative the finding is ACCESS, not data.**
> - ⇒ **WATT's tier-inverting +40% datum traces to SemiAnalysis, not to any vendor page.** That does not impeach it — it establishes **the contract leg is not independently reproducible by this desk from public sources.** Provenance question open since 9/03, now closed.
> - 🔴 **Ornn's OCPI IS LIVE and partly FREE** — `OCPI-H100` **$2.78** settled 9/13, transacted-price volume-weighted winsorized average, 3 months daily history free. **Closes the §3 rank-② SEARCH-NOT-FOUND.** **ICE settles its futures on OCPI ⇒ 10/05 is a TWO-TRACK question, not a go-live question.**
> - **The two indices disagree 9.4% day one** ($2.53 vs $2.78). **This is the panel-stability test §2 wanted, arriving from the other direction** — registered as `dispersion_index`, recorded every reading, **NO BAND** (§6: no threshold until ≥4 rows AND a stated base rate; a band tonight = a free parameter from n=1). Base rate at reading 4, **10-02**, three days before the re-decide.
> - **Neocloud mean $4.4737 vs Vast.ai median $1.8689 = ~2.4×** — WATT's 3–6× warning as a **measurement**, not a caution. NOT a series row.
>
> ## 🔴 THE THREE MISSES, RECORDED — AND WHY NOTHING WAS READ
> 1. **`semi_watch.py` slot 4 (9/11 post-close) MISSED — the FOURTH** (8/27 post-close · 8/28 · 09-04 · 09-11). Series last row 2026-08-24, **20d stale**. ✅ **The 9/30 re-arm rule survives: four slots remain (09-18·09-22·09-25·09-29) against "3+ consecutive" ⇒ margin is ONE, down from two. A fifth miss = no margin; a sixth = ungradeable.**
> 2. **`mag7.py` slot 1 (9/11 post-close) MISSED — its FIRST.** 🔑 **And STATUS's standing line *"mag7.py has NO pre-committed cadence — named as a gap"* was RETIRED tonight: it was already false when written.** The 9/11 session registered the cadence AND wrote the complaint about its absence in the same session.
> 3. **GPU reading 1 (9/11) stays MISSED** — a freeze is not a reading and Sunday is not a slot.
> **Nothing licensed an off-cadence read:** all three instruments are cadenced to Friday post-close, markets have been shut since 9/11, and the remedy for a missed reading is never an extra unscheduled one [L-21].
>
> ## ▶ START HERE NEXT SESSION
> 1. 🔴 **FRI 09-18 POST-CLOSE IS A THREE-INSTRUMENT RUN, each independently missable:** `semi_watch.py` (slot 5 — **one slot of margin left on the 9/30 rule**) · `mag7.py` (slot 2) · `gpu_panel.py --reading-date 2026-09-18 --input <filled template> --write`. **A partial run is a FAILED run [L-16].**
> 2. **Fill the GPU template AT the slot** — re-read all six URLs; **never carry the 9/13 freeze levels forward**, drop the vendor and let V5 write the sentinel.
> 3. **ORCL 10-Q by ~09-19** — `edgar_watch.py`; the $3.3B lessor guarantee's handling + the $260B off-BS book.
> 4. **STATUS is at 93% of the READ-CAP budget (30,313 B / 32,550 B).** ⚠️ **Rotate BEFORE writing next session, not after** — the 9/11 pass had to rotate mid-session for this reason. **Best candidate: the S3 matrix cell's 33-day wording-correction narrative → `CHANNEL_DETAIL.md`** (settled history; the *fact* stays). **Deferred tonight deliberately** — that cell took 33 days to get right and a rushed move at the end of an edit-heavy session is how it gets broken.
> 5. **09-15 GATE-LIQ-069** (LIQUID's; I am the seam) · **09-16 ZHAO BIS re-check** · **09-30 = a 10-01 stack.**
>
> ## ❌ STILL OPEN (carried): hyperscaler long-dated-issuance check (KB-096) · QQQ sector variant (Invesco 406s) · PROME's Q3 disinflationary-productivity falsifier (8/21) · **whether `data.ornn.com/preview` is a source of record** (a preview page is not established as one — re-check every reading) · `CLAUDE.md` auto-load cost, now ~79 KB (watch, don't rotate).

> # 2026-09-11 (Fri) — *(previous session; the 9/13 block above supersedes its ▶ START HERE)*. PROME-spawned Tier-1 session (DOCKET L323; Will *"ok approved"* 9/10 19:25), 10:37 ET → pre-close. 4 dark days before it (9/7 → 9/10).
>
> ## ONE LINE: DEWEY REQ-002 integrated into ONE instrument — **`VULCAN-17`, NVDA's guarantee-COMMITMENT level by quarter**, baseline VERIFIED at five filings by my own pulls, reading rule pre-committed (first FLAT/DOWN quarter with no successor = the signal; the fall is CLASSIFIED before it is read). Inbox **14 → 0**. TSMC August + ORCL Q1 swept. **No score, band or threshold moved.** Two misses recorded honestly: today's post-close readings (not this pre-close session's to take) and **GPU-PANEL-01 not frozen ⇒ reading 1 MISSED.**
>
> ## 🔑 THE INSTRUMENT, AND WHY IT IS THE ONE DEWEY SAID NOBODY WOULD PICK
> - Lucent/Nortel (n=2, DEWEY at the primaries): **the commitment level turning down was the only thing that LED** (Lucent peak 1999-12-31 → first warning 3 weeks later → full break ~12 mo); drawn balance unreliable BOTH signs (Nortel's fell by WRITE-OFF); provisions lagged [KB-154]. **Converges with REQ-001 (order books led 0 of 3; the marginal uncontracted unit's PRICE led)** — in both, what led was a *forward-looking supply decision*.
> - NVDA's series, **verified today at Q2 FY26 / Q3 FY26 / FY26 10-K / Q1 FY27 / Q2 FY27:** $0 → $860M (54.7% escrowed + capacity-sale + assume-lease option + warrants) → $3,530M → $3.5B → $3,529M (20.2% escrowed) **+ $105,000M Aug-2026 (0% escrowed; OpenAI indemnity)** = $108.5B max gross [KB-153]. DEWEY's §2 table holds at every point. ⇒ **BUILD phase, not break phase.**
> - **The letter:** ≥ $108,529M at the Q3 FY27 10-Q (~11/19, `publication` anchor; the August cap enters the period-end table) = HIT. **Below ⇒ classify first:** (i) transfer to a definitive third-party platform (T1, bull) · (ii) termination on an OpenAI IG rating (T5, bull) · (iii) a CALL (S5 red-band question) · (iv) WITHDRAWAL with no successor = **the Lucent signal** ⇒ level-to-Will via PROME WQ. FLAT within ±2% (the $3,530→$3,500→$3,529 rounding wobble) with no transfer = (iv). **The rule outlives the row: re-register as VULCAN-18 at grading.** [L-33]
> - **NOT done, on purpose:** no revenue-quality discount. **The share of financed revenue is NOT COMPUTABLE by disclosure asymmetry** (financing named/capped/phased; revenue attributed as *"one AI research and deployment company … a meaningful amount"*; the two named counterparties appear only in the guarantee note) [KB-155]. Direction supportable, size not — FL-VULCAN-12's disease, different note. **"AI research and deployment company" = OpenAI is INFERRED** (DEWEY's flag, carried).
> - **COR-20260910-01 → NO-OP:** the commission's *"$29B cloud agreements"* is NVDA's own-use R&D line; **KB-124 reconciled the two 10-Q tables AT THE FILING on 8/27** and NEXUS_BRIEF has carried *"use $36B for S5"* since. DEWEY's §1B is an independent second read (n=2, agreeing). Receipt written (`registry/corrections_receipts.tsv`, created today — this desk's first).
>
> ## 📥 INBOX 14 → 0, EVERY SENDER
> - **PROME 9/6 amendment (GPU ruling para. 3) ENCODED** — spec §3 and the ruling now agree; `term_normalized` + segment accepted; the cc reached WATT/DEWEY as files this time [KB-159].
> - **DEWEY ×2:** REQ-002 (above) + the Ex-99.2 confirmation — my 9/6 contested correction upheld at DEWEY's own pull; **the mechanism is transferable: `edgar_doc.py doc` without `--doc` silently returns the FIRST document of a multi-exhibit 8-K, exit 0** — never assert a filing-level absence from a bare doc-grep; enumerate exhibits first.
> - **WALTER ×11, all in `board_log.tsv` with reasons:** 4 acted (DRAM +59.5% is REVENUE not price; CXMT 16 GB package / 16 Gb die — 0 wrong carriers here; Kioxia CEO resisting NAND hikes = a stance consistent with the presold-ceiling mechanism, tested at MU 9/30; ASML–TSMC 12-inch masks 2031/2033 = horizon only; PJM IRAS docket **ER26-3515-000** now on the ~10/12 row for VULCAN-15(a); **MS $3.1T = REPACKAGING** — NVDA leg verified: the $500B is the MoU *target* in the 10-Q MD&A, the **$125B "25% RVS" is NOT filed** (0 hits) [KB-158]) · 5 noted with reasons · 1 info-only (Mistral €3B — LIQUID's mechanism).
>
> ## 📡 TWO FILINGS SWEPT (the EDGAR sweep was 8d stale; 46 rows added)
> - **TSMC August:** NT$514,806M, +10.1% MoM, +53.3% YoY, **cum Jan-Aug +39.3%** (from +37.0%) ⇒ decel NOT met, no-stress [KB-157]. Consistent with VULCAN-14 HIT at 9/30 — graded then.
> - **ORCL Q1 FY27 (8-K 9/10):** capex **$28.5B in one quarter**, FCF **−$5B**, **$20B ATM equity** completed, **$11.4B customer prepayments with a significant financing component**, RPO $664B; **0 hits on "guarantee" — the $3.3B is a 10-Q question (latest ~9/19; row registered)** [KB-156]. No band: equity is not a new-issue print. Deliberately NOT claimed for VULCAN-13 (prepayments fire on demand, not the balance sheet).
> - **NVDA 8-K 9/2:** Hugging Face ~$11.9B + $1.0B retention, close 1H27 — S1 context only [KB-160].
>
> ## 🔴 THE TWO MISSES, RECORDED
> 1. **`semi_watch.py` slot 4 + `mag7.py` slot 1 are POST-CLOSE today; this session ran 10:37 → pre-close.** Flagged to PROME for a post-close run. If none: slot 4 = 4th miss, recorded at the next boot, **never cured off-cadence** [L-21].
> 2. **`GPU-PANEL-01` NOT frozen.** Reason (spec §4 addendum): the contract tier has no vendor reconnaissance, and freezing blind mints a panel from an unspecified composition — §4's own failure. **Freeze in a dedicated pass before 09-18.**
>
> ## ✅ SELF-GRADE CHECKS 1-3 (frozen 8/21, due today): CHECK 1 YES (n=5, L-26 — correction and instruction in one cell) · CHECK 2 **7 < 11 but WEAK** (axes differ; not a cold reviewer; the strong YEYOU/RAV version has not run — UNGRADED-STRONG, not a pass) · CHECK 3 YES (2b caught the 31× cell 8/27 and the §317 supersession today; 4b caught the FILES row 9/6). Row SPENT in CATALYSTS.
>
> ## ▶ START HERE NEXT SESSION
> 1. 🔴 **If booting after 16:00 ET on 9/11: run `semi_watch.py` + `mag7.py` NOW** (slot 4 / slot 1). If booting 9/12+: record slot 4 MISSED, do not run off-cadence.
> 2. 🔴 **Freeze `GPU-PANEL-01` before Fri 09-18** (vendor probes → freeze → reading 2). Spec §3/§3b/§5 + the 9/11 addendum say what must be specified.
> 3. **ORCL 10-Q by ~09-19** — `edgar_watch.py`; read the commitments note for the $3.3B guarantee.
> 4. **`VULCAN-17` first reading ~11/19**; re-register the next quarter as VULCAN-18 at grading. A (iv) reading ⇒ PROME WQ the same session.
> 5. **9/15 GATE-LIQ-069 review (LIQUID's)** · **9/16 ZHAO BIS re-check** · **9/30 = 10/01 stack.**
>
> ## ❌ STILL OPEN (carried): hyperscaler long-dated-issuance check (KB-096) · QQQ sector variant (Invesco 406s) · PROME's Q3 disinflationary-productivity falsifier (8/21) · `CLAUDE.md` 74 KB auto-load cost (watch, don't rotate).

# VULCAN — SCRATCH (next-session pickup)

> 📖 **The 2026-09-03 closeout block was rotated to `archive/SCRATCH_ARCHIVE_2026-09.md` on 2026-09-13, verbatim** (SCRATCH had reached 82% of the READ-CAP budget and the block carried a third competing *“READ THIS BLOCK FIRST”* banner). Its durable content — the MU FQ4 date correction, the S1 yellow-band trip, the READ-CAP split — is already carried in `STATUS.md` and `LESSONS.md`; the archive is the record, not a live surface.
