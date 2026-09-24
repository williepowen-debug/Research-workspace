# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** session 29 — opened **2026-09-24 ~13:15 ET** (Thu), Will-directed "boot, continue where we left off"; closed ~15:xx ET. Same-day follow-on to s28.

## CHANGES SINCE (session 28 → 29) — same day
- Nothing new published. Boot clean: WALTER lane empty, corrections rc 0, fetchers current, drift clean. Local was 1 commit ahead of origin (PROME's), nothing incoming.
- **DEWEY (live msg):** `MARCO-DR-1` (the 7/31 FL-$ commission) is **NOT RUN**, deferred at `f0abad802`. **PROME asked MARCO for a needed-by date** → **registered as PROME DOCKET L466** (`1bf42371f`, verified at artifact): wake 2026-11-02, **needed-by 2026-11-16**, core legs 1/2/3/5 (leg 4 may split). **Fallback (MARCO's own call): if nothing lands by 11/16, MARCO formally retracts the FL-$ hole.**

## WHAT I DID (session 29)

### 1. Energy re-arm → `ENR-02` (Will: "go ahead with the oil price test" / "we have an agent that handles oil — do we not have this data?")
- **Yes, we had the data.** BRENT registers the same $85 line (`AGENTS/BRENT/workbook/REGISTRY.tsv` `MKT-BZ-F-BELOW-85`, with its roll rule). MARCO's own Brent instrument was a duplicate, and the duplicate is what lapsed 8/24. **Retired. The price leg now CITES BRENT** (9/22 settles BZX26 $99.25 / BZZ26 $95.41 [single vendor]). The old re-arm stays UNGRADED and is never back-graded (TIMELINE).
- **Fare leg (MARCO-owned), live BLS API:** CPI airline fares `CUUR0000SETG01` **Aug +23.41% YoY / +27.46% 2-yr**. 2-yr ≥+20% occurs in 6.1% of months 1997–2025 (2000/2011/2022-23). `KB-MARCO-ENR-01`, `FLOW-ENR-01` re-specified.
- **Letter (pre-registered 9/24):** 2-yr stack, Sep (**Wed 10/14**) AND Oct (~Nov 12, **est.**) both ≥ +20% = SUSTAINED; either < +15% = FADED; else HOLD. **2-yr because BLS has NO Oct-2025 value (shutdown).** Said in advance: flat fares give Oct only +16.47% (HOLD). Spirit is a co-driver after May, and the series is national.
- Packet → BRENT (`f67679aae`): 8/24 closed ungraded; MARCO is now a consumer of its $85 row.

### 2. Channel 4 credit leg RUN → **thesis v3.2, Channel 4 LOW (Will-ruled: "Lower to LOW, watch Laredo")**
- Receipts (TX Comptroller, live): 11 border cities Jan–Sep **+5.70%** vs all TX +6.24%. Reproduces the carried Jan–Jul +4.75% exactly.
- Credit: 3 Opus subagents; load-bearing figures spot-verified at source. **El Paso / McAllen / Nogales STABLE. Laredo early stress** (FY26 est. GF $62.2M→$50.25M, −19%; city blames **tariffs**). **Pharr S&P A+→A Negative 4/9/26**, but its sales tax and bridge tolls grew ⇒ **threshold-met / mechanism-refuted**. **EMMA not accessed** (terms gate).
- Corrections: El Paso pension is **78–80%**, not ~60%; Pharr's outlook came with a downgrade. No fleet consumer.
- → `domain/sources/BORDER/2026-09-24_border_municipal_credit_rebuild.md`, `KB-MARCO-TX-09..12`, `VX-TX-03`, THESIS/CHANGELOG v3.2, docket **2027-03-31 Laredo FY26 ACFR** watch. Packet → REGINALD (`b1cf3c408`).

### 3. Housekeeping
- `tools/bts_airport_pull.py`: the data clock now stamps the **newest data month** (was the pull date); `--help` fixed. Tested to a temp `--out`; baseline header restamped 2026-06-30.
- Memory `finding_threshold_spec_fails_before_world` → **n=6** (ENR-02 Oct-2025 hole); a stale "false-positive rates" claim was corrected. **Promotion flag → PROME** (`af330ec19`, doorbelled) + hot `MEMORY.md` at 75% of cap flagged (not compacted).
- Local MEMORY: two lessons (don't duplicate an owner's instrument; municipal-credit data routes).

## NEXT SESSION
1. 🟠 **LVCVA August (~9/30)**: a negative dollar print again ⇒ June wasn't noise.
2. 🔴 **Banxico AUGUST (Oct 1)**: SDL-01 re-spec print 2 of 2 (count 2-yr ≤ −5% ⇒ CONFIRMS). Co-run the state-of-origin map.
3. 🟠 **Oct 1: chase CORAL on Citizens PIF.**
4. 🔴 **Wed 10/14: `ENR-02` leg 1** (CPI airline fares Sep, 2-yr vs Sep-2024). **Verify the Oct CPI release date** for leg 2 (docket says ~11/12 est.).
5. 🟠 **~Oct 15:** StatCan Sep (`ID-01` leg 1, both-months) · NTTO Sep (`VX-1.02` −24.20% vs the −25% line) · BTS July (is MCO still negative?).
6. 🟠 **~Oct 28: MIA September report** decides the MIA-2-consecutive trigger. If it fires: REGINALD + CARL, with the capacity-vs-demand caveat verbatim.
7. 🟡 **Inbox (only if Will asks):** LABOR 9/17 (FL initial claims −8%) · ZHAO 9/18 (withdrawn China PPI claim).
8. **Carried:** `VX-2.01` on an unrefreshed Jun-15 arrest rate · `VX-1.02` band doesn't name its 2019 period · USMCA preference not primary-supported · `NV-01` Canadian basis unrefreshed · `VX-1.03` "loss" undefined.
9. **Do NOT hunt a fifth Channel-1 transmission instrument** (v3.0 pre-commit).

## OPEN THREADS
| Item | Status |
|------|--------|
| ✅ **Energy re-spec** | DONE 9/24 → `ENR-02`, grades 10/14 + ~mid-Nov |
| ✅ **Channel 4** | DONE 9/24 → v3.2 LOW; Laredo watch 2027-03-31 |
| 🔴 **FL-$ hole** | DEWEY `MARCO-DR-1` = PROME **L466**, needed-by 11/16; retraction fallback |
| 🟠 **MIA Aug −5.69%: demand or capacity?** | Sep report ~10/28 |
| 🟠 **MAR-24 at 80%** | Aug MCO unobserved; resolver = BTS Q3, 2027-02 vintage |
| 🔑 **`ID-01`** | Sep print ~mid-Oct (both-months, PROME-confirmed) |
| 🟠 **SDL-01 re-spec 1 of 2** | August ~Oct 1 |
| ⏳ **Spirit seat deletion unsized** | Seats never measured |
| ⚠️ **Read budgets** | MEMORY 74% (372 B to the 75% trigger), STATUS ~74%. Next addition to either should rotate first |

## Mail state
**Inbox 2 UNPROCESSED** (LABOR 9/17 · ZHAO 9/18), not an inbox spawn. WALTER lane empty.
**Sent:** BRENT (info, $85 row consumer) · REGINALD (info, Channel 4 v3.2) · PROME (promotion flag + index-cap flag; doorbelled) · PROME live msg (DR-1 needed-by date).

## PUSH STATE
Session 29: see the closeout commit and the `safe-push.sh` receipt line.
