# WIRING SWEEP #2 — JUDGMENT LEGS, part W1 — 2026-09-17 (Thu, ~09:3x ET)

**Owner:** DAEDALUS · **Sitting:** the 9/14-dated judgment sitting, run 9/17 (3d late) · **Registry row:** `sweeps/REGISTRY.tsv` "Wiring Sweep (R1 boot-leg + 8/28 input register)", `resolve_by 2026-09-14` · **Predecessor:** `runs/2026-09-04_WIRING_SWEEP_02_DETECTION_PASS.md` (§1 mechanical legs, §2 the deferral list this file discharges four items of).
**HEAD at run:** `b824b5a13` (2026-09-17). **Read-only run** — one file written (this one), no other file created, edited, moved or committed; no mutating git command issued.
**Legs run:** A (route-around LATENT/LIVE split) · B (LEDGER_GLOB census) · C (ZHAO `recheck_by` + LIQUID unattended writers) · D (BRENT grade→machine-read hop). **Legs still owed from §2:** ⑲ · ⑰ #2 · ㉓ · ⑧ · ⑩ · ㉗ · L258 SL-5 operator sweep · ㉕ · D/E/F from the detection pass.

---

## LEG A — Route-around-WALTER re-measure, split LATENT vs LIVE

### A.0 Method
```
python3 AGENTS/DAEDALUS/scripts/walter_route_check.py           # rc=1, census below
git log --diff-filter=A --name-only --format='C|%h|%cs|%s' --since=2026-08-01 -- AGENTS
  | awk -F'|' '/^C\|/{h=$2;d=$3;s=$4;next} /inbox\//{print h"\t"d"\t"$0"\t"s}'   # 3,694 inbox additions
grep -i "from-<DESK>" <that>  | grep -v "AGENTS/<DESK>/inbox"   # direct sends BY the desk
grep    "AGENTS/WALTER/inbox.*from-<DESK>" <that>               # the WALTER lane, same window
```
Then each candidate signal-class file was **opened at the artifact** (`git show <hash>:<path>`) and graded against the standard the tool itself cites: *direct PACKETS are fine; direct SIGNALS are not* (`walter_route_check.py:12-20`; root CLAUDE.md "never route signals around WALTER").

### A.1 Census re-measure — 7 → 1 ROUTE-AROUND
| | 9/2 census | 9/4 detection pass | **9/17 (this run)** |
|---|---:|---:|---:|
| ROUTE-AROUND | 14 | 7 | **1** |
| DEAD-ROUTER | 4 | 0 | **0** |
| MIXED (read, not owed) | — | 8 | **9** |
| PACKET-LANE | — | 5 | **5** |
| TWO-LANE (pass) | — | 5 | **9** |
| CORRECT | — | 170 | **163** |

The 9/4 expectation ("≤3 if LABOR/HENRY/REGINALD land") is **BEATEN**: all three landed. HENRY `CLAUDE.md:51` and REGINALD `CLAUDE.md:65,303` now read as TWO-LANE/MIXED; REGINALD's row is dated in its own text — *"re-cut 2026-09-11 per DAEDALUS route-around census 9/2"* (`AGENTS/REGINALD/CLAUDE.md:65`).

**The single surviving ROUTE-AROUND row is on a RETIRED desk.**
`AGENTS/YEYOU/CLAUDE.md:164` — *"signals via your own `outbox/` (write a copy directly to the target's `inbox/` — HERMES retired)"*. YEYOU was retired 2026-09-05 (`PROME/ROSTER.md:144`, Will *"retire yeyou"* 11:56 ET, WQ-181 ①).

### A.2 LATENT vs LIVE — the test the 9/4 pass asked for
| Desk | tool verdict | direct sends to peer inboxes since 8/1 | sends to `AGENTS/WALTER/inbox/` since 8/1 | signal-class direct send found? | **LATENT / LIVE** |
|---|---|---:|---:|---|---|
| **YEYOU** | ROUTE-AROUND | **0** (0 all-time: `git log --diff-filter=A -- AGENTS \| grep "inbox.*from-YEYOU"` returns nothing, ever) | 0 | no — desk has never sent anything | **LATENT** (and moot — retired) |
| **LABOR** *(control)* | clean (fixed `2a67bc31b`) | 48 | 4 | yes, and it was **cc'd to WALTER in the same commit** | **LATENT** |
| **LIQUID** *(control)* | clean (fixed 9/3) | 41 | 2 | no — both candidates are answers to PROME-routed asks | **LATENT** |
| **OTTO** *(control)* | clean on leg A (leg-B form, agent-judged) | 11 | **0 — all-time** | **YES** | **🔴 LIVE** |

**Headline: 0 desks LIVE of the 1 the tool marks ROUTE-AROUND; 1 LATENT. Across the ROUTE-AROUND set + the three controls: 1 LIVE (OTTO), 3 LATENT.** The 9/4 hypothesis holds — canon-census count and route-around *practice* are different headlines — but it inverts on OTTO: the desk whose canon is now CORRECT is the one whose practice is not.

### A.3 The three gradings, at the artifact

**LABOR — LATENT, and the counter-example is exemplary.** Commit `ec9018565` (2026-08-28) wrote a file whose own first body line is `**Signal:** QCEW preliminary benchmark printed −79,000 (Band E)` into `AGENTS/RED/inbox/2026-08-28_from-LABOR_qcew-printed-79K-band-E-plus-your-KB-068-staffing-answer.md`. **The same commit** wrote `AGENTS/WALTER/inbox/2026-08-28_from-LABOR_cc-routing-record-qcew-and-warsh.md`, which opens: *"To: WALTER (cc / routing record — no action requested) · **Signal:** Two LABOR items graded at primaries this morning; **routing recorded here so signal flow is not routed around you.**"* LABOR's canon defect was real and is fixed; its practice never expressed it.

**LIQUID — LATENT.** Two candidates, both opened: `15fee9a63` → BROCK 9/12 (DGS10 >4.75 consecutive-close count) is headed *"your routed ask answered … routed to me by PROME 2026-09-03"*; `eac198c83` → BROCK 9/2 declares in its own subhead *"$0 at risk. **No gate fired. No threshold moved.** No LIQUID position exists."* Neither is an originating signal. LIQUID also demonstrably uses the lane (`AGENTS/WALTER/inbox/2026-08-23_from-LIQUID_SIG-024-graded…`, and the 9/2 `ROUTE-` packet that started this census).

**OTTO — 🔴 LIVE.** OTTO's own corrected canon, `AGENTS/OTTO/CLAUDE.md:325` (corrected 2026-09-02, `16d78369b`):
> **"Route via WALTER. Always."** … *"A direct packet is legitimate only when it is an answer to that desk's own ASK, **never for a triggered signal**."*

Ten days later, `2a02ed3e0` (2026-09-12) wrote `AGENTS/BROCK/inbox/2026-09-12_from-OTTO_2A-FIRED-…md`, whose title line is:
> *"**2A FIRED.** A 9/11 8-K extends the STD to Sept 18 … ⇒ Issuer 8-K, extension, NEW DATED termination. **2A, precedence rank 3, first match. VERIFIED.**"*

That is a registered letter-condition firing, verified at a primary (SEC accession `0001171843-26-005989`). Its header claims the ASK exemption (*"Answering: your 2026-09-09 grade-staging packet"*) — but OTTO's own rule says the exemption does not reach a triggered signal. **And OTTO has never written a single file into `AGENTS/WALTER/inbox/`, all-time**, against 11 direct peer-inbox sends since 8/1. The `SIG-OTTO-WALTER-YYYYMMDD-*.md` lane specified at `AGENTS/OTTO/CLAUDE.md:185-186` has zero exercises.

### A.4 Instrument finding — the tool's perimeter includes retired desks
`walter_route_check.py` never reads `PROME/ROSTER.md` (`grep -n "ROSTER\|RETIRED\|DORMANT" AGENTS/DAEDALUS/scripts/walter_route_check.py` → no hits). Its terminal line **"DESKS OWED A PACKET (1): YEYOU"** is therefore an ask no session can ever discharge: no YEYOU session will boot again. On top of the 9/4 finding that the line "cannot see a packet already sent," the label now also cannot see a desk that no longer exists.

### A.5 Verdicts
| # | Verdict | Owner ask (one line — DAEDALUS sends the packet) |
|---|---|---|
| A-1 | **LIVE route-around at OTTO** — canon `:325` correct, practice `2a02ed3e0` contradicts it; WALTER lane 0/all-time vs 11 direct sends | **OTTO:** your 9/12 "2A FIRED" packet to BROCK is the class your own `CLAUDE.md:325` reserves for WALTER — confirm the rule or amend it, and say which. |
| A-2 | **LATENT, closable** — YEYOU `:164` is the last ROUTE-AROUND row and the desk is RETIRED | **PROME:** rule the YEYOU row NO-FIX-RETIRED so the census can close at 0, or authorise a one-line FROZEN banner on `AGENTS/YEYOU/CLAUDE.md`. |
| A-3 | **Instrument** — `walter_route_check.py` has no ROSTER screen | **DAEDALUS (self):** add a ROSTER-status column to the census output so RETIRED/DORMANT rows print as NOT-OWED rather than as an owed packet. |
| A-4 | **TRUE-STILL** — LABOR/LIQUID fixes verified at the artifact, HENRY/REGINALD canon re-cut | none. |

---

## LEG B — `workbook/LEDGER_GLOB` census (43 `AGENTS/` dirs + `PROME/`)

### B.0 Method + a correction to the leg's premise
```
find AGENTS PROME -path '*/workbook/LEDGER_GLOB*' -not -path '*/archive/*'
python3 scripts/ledger_staleness.py --all            # rc=1; 368 lines, incl. per-desk 'perimeter:' coverage lines
python3 scripts/ledger_staleness.py --nudge <DESK>   # the root closeout step 1c-bis instrument, per desk
# census script: imports ledger_staleness's own read_ledger_glob / NON_LEDGER_NAMES / is_exempt /
# unscanned_outside_glob so the perimeter is the TOOL'S, not a re-derived one, then git log -1 --format=%cs per file
```
⚠️ **The brief's premise needs narrowing, and this is the honest version.** A missing `LEDGER_GLOB` is **not** a defect on its own: the default glob is `workbook/*.tsv` (`scripts/ledger_staleness.py:59-63`), and `LEDGER_GLOB` is only required when a desk's ledgers live *outside* that default. **1c-bis nudges on nothing only where the default glob matches zero files.** Further, the nudge is **not silent** in that case — it prints `nudge: [X] no live ledgers under workbook/*.tsv — nothing to nudge (scope stated, not silent)` and returns rc 0 (verified on all 7 zero-match desks). The gap is real; it is a **coverage** gap, not a silent-failure gap.

### B.1 Headlines
- **8 of 44 surfaces declare `LEDGER_GLOB`** (AEOLUS · BRENT · CARL · CREED · DAEDALUS · ORACLE · TERRY · VIOLET). 36 do not. *(Two further copies exist and are not live declarations: `AGENTS/BRENT/research/2026-09-15_boot/before/workbook/LEDGER_GLOB` (a captured "before" tree) and `AGENTS/DAEDALUS/tests/nudge_fixture/workbook/LEDGER_GLOB` (my own test fixture).)*
- **7 surfaces get ZERO ledgers enforced while holding ≥1 TSV in-tree** — BARON (24 unscanned) · **WALTER (35)** · **PROME (10)** · DEWEY (2) · NEXUS (2) · YEYOU (2) · SHADE (1). **76 TSVs total outside every staleness instrument on those 7 alone.**
- **4 surfaces are genuinely empty** and correctly report nothing: ATHENA · CATO · RAV · SENTRY.
- **0 MISCONFIGURED** (`LEDGER_GLOB` present but matching nothing) and **0 LEDGERS-OUTSIDE-GLOB** fleet-wide — both loud classes are clean.
- **254 TSVs scanned fleet-wide, 193 NOT scanned** by the pass (sum of the table below) — the coverage half is roughly as large as the enforced half.

### B.2 The census
⛔ = zero ledgers enforced while TSVs exist in-tree (1c-bis has nothing to grade). Dates are `git log -1 --format=%cs` over the union of enforced + unscanned TSVs.

| Desk | ROSTER | LEDGER_GLOB | ledgers ENFORCED | TSVs NOT scanned | newest | oldest |
|---|---|---|---:|---:|---|---|
| **ATHENA** | ARCHIVE SOURCE | no | 0 — | 0 | - | - |
| **BARON** | DORMANT | no | 0 ⛔ | 24 | 2026-02-01 | 2026-02-01 |
| **CATO** | CLASS-PENDING | no | 0 — | 0 | - | - |
| **DEWEY** | TIER-2 | no | 0 ⛔ | 2 | 2026-09-10 | 2026-09-10 |
| **NEXUS** | ACTIVE/ORG-SERVICE | no | 0 ⛔ | 2 | 2026-09-11 | 2026-09-11 |
| **PROME** | ACTIVE/ORG-SERVICE | no | 0 ⛔ | 10 | 2026-09-17 | 2026-07-11 |
| **RAV** | SPECIAL | no | 0 — | 0 | - | - |
| **SENTRY** | DORMANT | no | 0 — | 0 | - | - |
| **SHADE** | ACTIVE/DOMAIN | no | 0 ⛔ | 1 | 2026-08-28 | 2026-08-28 |
| **WALTER** | ACTIVE/ORG-SERVICE | no | 0 ⛔ | 35 | 2026-09-15 | 2026-05-06 |
| **YEYOU** | RETIRED | no | 0 ⛔ | 2 | 2026-09-05 | 2026-09-05 |
| **AEOLUS** | ACTIVE/PROVISIONAL | YES | 15 | 0 | 2026-09-11 | 2026-08-13 |
| **BOND** | ACTIVE/DOMAIN | no | 3 | 7 | 2026-09-17 | 2026-08-20 |
| **BRENT** | ACTIVE/DOMAIN | YES | 9 | 10 | 2026-09-17 | 2026-07-01 |
| **BROCK** | ACTIVE/DOMAIN | no | 8 | 3 | 2026-09-12 | 2026-03-26 |
| **CARL** | ACTIVE/DOMAIN | YES | 45 | 10 | 2026-09-17 | 2026-06-26 |
| **CORAL** | ACTIVE/DOMAIN | no | 1 | 0 | 2026-09-13 | 2026-09-13 |
| **CREED** | TIER-2 | YES | 6 | 1 | 2026-09-02 | 2026-08-13 |
| **CRUISE** | ACTIVE/EVENT-DRIVEN | no | 4 | 0 | 2026-09-13 | 2026-09-10 |
| **DAEDALUS** | SPECIAL | YES | 4 | 3 | 2026-09-14 | 2026-09-04 |
| **FALCON** | ACTIVE/PROVISIONAL | no | 4 | 5 | 2026-09-16 | 2026-09-01 |
| **FERT** | ACTIVE/EVENT-DRIVEN | no | 5 | 0 | 2026-09-15 | 2026-09-05 |
| **FLG** | ACTIVE/EVENT-DRIVEN | no | 7 | 0 | 2026-08-28 | 2026-08-28 |
| **HANS** | TIER-2 | no | 6 | 3 | 2026-09-10 | 2026-09-05 |
| **HAWK** | ACTIVE/DOMAIN | no | 5 | 3 | 2026-09-17 | 2026-07-12 |
| **HENRY** | ACTIVE/DOMAIN | no | 6 | 1 | 2026-09-14 | 2026-07-10 |
| **HOMER** | ACTIVE/PROVISIONAL | no | 8 | 3 | 2026-09-14 | 2026-07-12 |
| **LABOR** | ACTIVE/DOMAIN | no | 6 | 3 | 2026-09-17 | 2026-06-26 |
| **LIQUID** | ACTIVE/DOMAIN | no | 5 | 1 | 2026-09-12 | 2026-07-11 |
| **MARCO** | ACTIVE/DOMAIN | no | 5 | 19 | 2026-09-17 | 2026-04-18 |
| **MIDAS** | ACTIVE/PROVISIONAL | no | 4 | 1 | 2026-09-11 | 2026-09-02 |
| **ORACLE** | ACTIVE/DOMAIN | YES | 7 | 2 | 2026-09-07 | 2026-08-27 |
| **OSPREY** | ACTIVE/PROVISIONAL | no | 4 | 6 | 2026-09-16 | 2026-09-16 |
| **OTTO** | TIER-2 | no | 9 | 2 | 2026-09-12 | 2026-07-04 |
| **OZK** | ACTIVE/EVENT-DRIVEN | no | 3 | 0 | 2026-08-28 | 2026-08-28 |
| **RED** | ACTIVE/REVIEW | no | 6 | 8 | 2026-09-14 | 2026-05-06 |
| **REGINALD** | ACTIVE/DOMAIN | no | 12 | 5 | 2026-09-14 | 2026-03-27 |
| **SAM** | ACTIVE/DOMAIN | no | 17 | 14 | 2026-09-15 | 2026-08-07 |
| **TERRY** | ACTIVE/DOMAIN | YES | 5 | 1 | 2026-09-14 | 2026-08-20 |
| **VIOLET** | ACTIVE/DOMAIN | YES | 13 | 1 | 2026-09-17 | 2026-09-11 |
| **VULCAN** | ACTIVE/PROVISIONAL | no | 10 | 2 | 2026-09-13 | 2026-08-24 |
| **WAL** | ACTIVE/EVENT-DRIVEN | no | 4 | 0 | 2026-09-02 | 2026-08-07 |
| **WATT** | ACTIVE/PROVISIONAL | no | 4 | 1 | 2026-09-11 | 2026-09-06 |
| **ZHAO** | ACTIVE/DOMAIN | no | 4 | 2 | 2026-09-17 | 2026-09-02 |

### B.3 The 7 ⛔ surfaces, named
| Surface | ROSTER | TSVs outside every staleness instrument |
|---|---|---|
| **WALTER** | ACTIVE/ORG-SERVICE | `REGISTRY.tsv` · `routed/route_log.tsv` · `routed/delivery_log.tsv` · `filtered/kill_log.tsv` · `registry/CORRECTIONS.tsv` · `registry/DOORBELL_LOG.tsv` · `registry/FALSIFICATION_FIRED_LOG.tsv` · `registry/REG_THRESHOLDS_FIRED_LOG.tsv` · `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` · 7 dated `STALENESS_SWEEP_*.tsv` · 3 `BM-*-manifest.tsv` + `BATCH_MANIFEST.tsv` · +10 research/design captures (35 total) |
| **PROME** | ACTIVE/ORG-SERVICE | `DOCKET.tsv` · `GATES.tsv` · `registry/READS.tsv` · `registry/WQ_LEDGER.tsv` · `registry/WQ_EXPLAINERS.tsv` · `registry/corrections_receipts.tsv` · `state/ORCH_LOG.tsv` · `state/AUDIT_PERIMETER.tsv` · `data/treasury_wam_series.tsv` · `tools/dashboard_parked.tsv` |
| **BARON** | DORMANT | 24 — `data/{CATALYSTS,EDGES,NODES}.tsv` + `domains/{cross-domain,crypto,defense,energy,finance,housing,media}/{catalysts,edges,nodes}.tsv`; **all last committed 2026-02-01** |
| **DEWEY** | TIER-2 | `output/INDEX.tsv` · `registry/corrections_receipts.tsv` |
| **NEXUS** | ACTIVE/ORG-SERVICE | `brief_fallback_log.tsv` · `registry/corrections_receipts.tsv` |
| **YEYOU** | RETIRED | `reviews/REVIEW_LOG.tsv` · `reviews/STATE.tsv` (frozen at the single 8/20 run) |
| **SHADE** | ACTIVE/DOMAIN | `registry/corrections_receipts.tsv` |

**The shape:** the two desks with the *largest* unenforced sets — WALTER (35) and PROME (10) — are the fleet's two ORGANIZING/SERVICE surfaces, i.e. the registries every other desk's routing and obligations depend on. `PROME/DOCKET.tsv` and `PROME/GATES.tsv` are cited by line number fleet-wide and sit outside every staleness instrument. This is `finding_guard_correctness_and_wiring_are_independent` at fleet scale: the instrument is correct, its perimeter is `AGENTS/<NAME>/workbook/`, and the load-bearing registries are not there — the same root as PAT-071/`SURFACES.tsv`.

### B.4 Verdicts
| # | Verdict | Owner ask |
|---|---|---|
| B-1 | **WALTER: 35 TSVs, 0 enforced.** `routed/route_log.tsv`, `filtered/kill_log.tsv`, `registry/REGISTRY.tsv` are live routing state with no staleness clock | **WALTER:** declare the live subset in `AGENTS/WALTER/workbook/LEDGER_GLOB` (one line) so 1c-bis grades the routing ledgers; the 7 dated `STALENESS_SWEEP_*.tsv` are archival and should be excluded or FROZEN-bannered. |
| B-2 | **PROME: DOCKET/GATES/READS/WQ_LEDGER outside every staleness instrument** | **PROME:** `PROME/workbook/LEDGER_GLOB` with `DOCKET.tsv GATES.tsv registry/*.tsv state/*.tsv`, or a ruling that these are governed elsewhere and the gap is deliberate — either closes it. |
| B-3 | **BARON: 24 TSVs frozen at 2026-02-01, desk DORMANT** | **PROME:** dormant-freeze is pre-approved (PAT-036) — a FROZEN banner on BARON's `data/`+`domains/` TSVs at the next staleness sweep; no LEDGER_GLOB needed. |
| B-4 | **Instrument, honest-scope** — the 1c-bis nudge *states* its zero-match scope (rc 0) rather than failing silently, so this is a coverage gap not a silent-rot gap | **DAEDALUS (self):** log the 44-surface census as the §12 base rate before proposing any new check; `CHECKS.tsv` row for `ledger_staleness` should record "PASS proves: only `workbook/*.tsv` (or a declared glob) is current." |
| B-5 | **0 MISCONFIGURED, 0 LEDGERS-OUTSIDE-GLOB** — both loud classes clean fleet-wide | none. |

---

## LEG C — ZHAO `recheck_by` · LIQUID unattended writers

### C.0 The leg text, located
Neither leg is in `sweeps/WIRING_SWEEP.md` or the 8/28 run dir. Both were minted in my own 9/2 dispositions packet — `AGENTS/DAEDALUS/outbox/2026-09-02_to-PROME_inbox-drained-9-items-route-around-WALTER-is-10-desks-NEXUS-ruled-L239-rendered.md:56-58`:
> **"Obligation with no dated reader / `recheck_by` (ZHAO)** — ✅ TAKEN, same sweep, same measure-first gate — **count DOCKET range rows with unknown days, and desks whose boot reader is a single file.**"
> **"① Unattended writers that cannot publish — TAKEN, census first** (LIQUID's watcher, BRENT's cloud routines, the intake lane); same family as the BRENT hop, so one census covers both."

Origin packet: `AGENTS/DAEDALUS/inbox/processed/2026-09-02_from-PROME_registry-pattern-an-obligation-with-no-dated-reader-three-shapes-in-one-day-recheck_by-proposal.md` — three shapes: ① a carried "day unannounced" that never self-evaluates · ② a vector carried 55 days in the silent-rot middle · ③ a commitment on no surface the author's boot reader travels.

### C.1 ZHAO — `recheck_by`

**Method:** `grep -rn "recheck_by" --include=*.md --include=*.tsv --include=*.py .` · `head -1 AGENTS/ZHAO/docket/CATALYSTS.tsv` · `.venv/bin/python AGENTS/ZHAO/scripts/catalyst_countdown.py` · `awk -F'\t' '$1 ~ /\.\./' PROME/DOCKET.tsv`.

| Question | Answer | Locator |
|---|---|---|
| Do any rows carry a `recheck_by` date? | **NO — zero, fleet-wide.** The token appears only in the proposal packet, my disposition, and one memory file. No column, no cell, no row. | `grep -rn "recheck_by"` → 7 hits, all prose about the proposal |
| Is there a boot step or script that reads it? | **Vacuously none** — nothing to read. | — |
| Are any past-due unread? | **N/A on `recheck_by`; YES on its substitute.** | below |
| ⑫ `date_class` (the sibling proposal) | **SHIPPED.** `AGENTS/ZHAO/docket/CATALYSTS.tsv` col 8 = `date_class`, values `confirmed` (3) · `estimated` (5) · `external` (4) · `modeled` (4) | `head -1 …/CATALYSTS.tsv` |
| Shape ③ (single-file boot reader) | **FIXED.** `boot.py:15-16` — *"[4] CATALYST COUNTDOWN — ONE reader over all three dated registries: `docket/CATALYSTS.tsv` + `PREDICTIONS.Resolve_By` + PROME DOCKET(ZHAO)"* | `AGENTS/ZHAO/scripts/boot.py:15-16`, `:202-205` |
| Shape ① (carried unknown) | **FIXED on the founding case.** DOCKET L222's Xi summit now renders `P1 🔴 2026-09-24 · 7d cal / 5d trd` in ZHAO's countdown; the DOCKET state cell reads `PENDING — DATED 2026-09-24 (ZHAO 9/2, 66ac967a4, KB-ZHAO-131)` | `PROME/DOCKET.tsv` L222 field 4; countdown output |

**Two live residues.**

**(a) ZHAO implemented `recheck_by` under a different name — as a dated CATALYSTS row — and the mechanism fired and was NOT serviced.**
`AGENTS/ZHAO/docket/CATALYSTS.tsv:8` —
> `2026-09-16 | RE-CHECK (not an event): BIS Entity-List package + MOFCOM TSMC/QCOM restriction — enactment watch | … | **ANY-DAY TRIGGER, SCHEDULED RE-CHECK — the date is when ZHAO LOOKS, not when it fires.**`

That row is exactly the proposed mechanism. The countdown surfaced it (`P2 🟠 2026-09-16 (Wed) 1d ago [CAT] RE-CHECK …` under *RECENTLY FIRED — SWEEP NOW*). And ZHAO's own STATUS records the miss verbatim:
> `AGENTS/ZHAO/STATUS.md:174` — *"🟠 **Enactment watch** (BIS package · MOFCOM TSMC/QCOM) — **CATALYSTS 9/16 re-check fired unread; re-date.**"*

**The instrument worked; the disposition did not.** As of `b824b5a13` the row still carries `2026-09-16` — past-due, logged as unread, not re-dated. This is `finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`, on the very mechanism proposed to cure the class.

**(b) `modeled` rows carry a re-check obligation with no date.** The countdown's own legend: *"('~' = modeled date: month known, DAY IS A PLACEHOLDER — **re-date when announced**)"*. 4 rows are `date_class=modeled` (e.g. `~2026-09-22` LPR fixing, `~2026-10-01..10-31` Fifth Plenum). *"Re-date when announced"* has no date, no reader and no expiry — the original shape ① defect, surviving inside the fixed reader.

**(c) The DOCKET measurement asked for.** `PROME/DOCKET.tsv`: **62 range rows** (`YYYY-MM-DD..YYYY-MM-DD` in field 1); **2 with explicit day-unknown language** — L26 (NY Fed Q2 HHDC, *"DATE UNANNOUNCED, window modeled"*, now RESOLVED) and L55 (the Xi summit). **Base rate = 2 of 62 (3.2%), 1 of which is already closed.** Against the §12 measure-first bar (≥3 desks / a recurring class), **a `recheck_by` COLUMN is NOT justified on DOCKET.** The measured class is not "range rows" — it is **dated re-check rows that fire and are not serviced**, and ZHAO's CATALYSTS row form already expresses it.

⚠️ **One row-level defect found in passing (PROME's file, not ZHAO's):** `PROME/DOCKET.tsv` L55's *Item* cell still reads *"(exact date unannounced…)"* while its *state* cell carries *"PENDING — DATED 2026-09-24"*. Two live texts in one row; the state cell is aware of it and annotates rather than replaces. `finding_correction_beside_an_instruction_leaves_two_live_instructions`.

### C.2 LIQUID — unattended writers → target → reader

**Method:** `grep -rln "AGENTS/LIQUID" --include=*.py --include=*.sh .` (outside LIQUID) · read `AGENTS/LIQUID/scripts/hy_oas_watch.py` write sites · `grep -nE "open\(|read_text|Path\(" AGENTS/LIQUID/scripts/boot.py` · `git check-ignore -v` · `ls -la AGENTS/LIQUID/alerts/`.

**The census (one unattended writer: `hy_oas_watch.py`, a systemd-timer companion, fires ~13:00 daily):**

| Writer | Target | Reader | Verdict |
|---|---|---|---|
| `AGENTS/LIQUID/scripts/hy_oas_watch.py:272` | `alerts/HY_OAS_STATE` (json) | `boot.py:541 watcher_echo()` | **READ** — but see (a)(b) |
| `hy_oas_watch.py:40,53` | `alerts/watch.log` — docstring `:19` *"append-only — one line every run (**liveness / silent-failure proof**)"* | **NONE.** No boot step, no script, no protocol doc parses it. Only self-references at `:19,:23,:40`. | **🔴 UNREAD** |
| `hy_oas_watch.py:38` | `alerts/HY_OAS_ALERTS.log` | `boot.py:554` names it inside a string, **only when `sev>=1`**; never opened or parsed | **PARTIAL** |
| `hy_oas_watch.py:197,213` | `PROME/inbox/<date>_from-LIQUID_UNATTENDED-hy-oas-*.md` | PROME boot inbox drain | **READ** |
| `hy_oas_watch.py:180,220-223` | `AGENTS/SIGNALS.md` appended row | 17 desk `CLAUDE.md`s name `SIGNALS.md`; not verified per-desk here | **NOT-ADJUDICATED** |
| `scripts/pipeline_rc_guard.py:393` | *invokes* `AGENTS/LIQUID/scripts/boot.py` — does not write into LIQUID | n/a | not an unattended writer |

**(a) The whole alerts lane is gitignored — so it is machine-local, and the fleet is serial multi-machine.**
`AGENTS/LIQUID/.gitignore:2` = `alerts/` (`git check-ignore -v AGENTS/LIQUID/alerts/watch.log` confirms). On the machine Will is *not* on, `watcher_echo()` prints `(watcher has not run yet — no HY_OAS_STATE)` (`boot.py:546`) — which reads as *no alert* but means *no data here*. Root CLAUDE.md's desktop⇄laptop model makes this a real state, not a hypothetical.

**(b) The echo prints an age and never grades it.** `boot.py:553-556` flags only on `sev>=1`; it prints `checked` as text with no comparison to today. **A dead timer therefore renders as a confidently-printed stale zone with no age flag** — `finding_plausible_stale_value_evades_review`. The one file that would prove the timer alive (`watch.log`) is the one nothing reads.

**Live state at run** (read-only, for the reader's calibration, *not* a signal — LIQUID owns this figure): the timer is **alive** — `watch.log` tail `2026-09-16 13:00 HY OAS 276bps 🟡yellow (sev 1, prev 1yellow, sub260 0, obs 2026-09-15 NEW) ok`; today's 13:00 run had not fired at 09:37 ET. `HY_OAS_ALERTS.log` last escalation `2026-09-02 13:00 🟢green→🟡yellow`. The banner in that log names `X1 >280 master` — i.e. the watched level sits 4bps under its master trigger, which is the window in which an unnoticed dead timer would cost the most.

### C.3 Verdicts
| # | Verdict | Owner ask |
|---|---|---|
| C-1 | **ZHAO `recheck_by`: NEVER IMPLEMENTED (0 rows, 0 readers) — and it does not need to be.** The CATALYSTS `RE-CHECK` row form already is the mechanism | **DAEDALUS (self):** close the `recheck_by` blueprint item as SUPERSEDED-BY-PRACTICE; cite ZHAO `docket/CATALYSTS.tsv:8` as the canonical form. |
| C-2 | **🔴 ZHAO: the re-check fired 9/16 and is logged unread + un-re-dated at `STATUS.md:174`** — instrument worked, disposition did not | **ZHAO:** re-date `docket/CATALYSTS.tsv:8` or grade it; a re-check row that fires and stays past-due converts a working reader into noise. |
| C-3 | **ZHAO: 4 `modeled` rows carry "re-date when announced" with no date/reader/expiry** — shape ① surviving inside the fixed reader | **ZHAO:** give each `date_class=modeled` row an explicit re-check date, exactly as the BIS row has one. |
| C-4 | **🔴 LIQUID: `alerts/watch.log` — the declared liveness/silent-failure proof — has NO reader**, and the echo that does read the state never grades its age | **LIQUID:** have `boot.py:watcher_echo()` compare `checked` to today and print 🔴 past a threshold; the liveness proof only proves liveness if something reads it. |
| C-5 | **LIQUID: the whole `alerts/` lane is gitignored ⇒ machine-local**; on the other box the echo's "has not run yet" is indistinguishable from "no alert" | **LIQUID (+PROME for the machine model):** make the echo distinguish *no state file on THIS machine* from *no alert*; consider a committed one-line state mirror. |

---

## LEG D — BRENT grade → machine-read hop

### D.0 The leg text, located
Same packet, `…2026-09-02_to-PROME_inbox-drained-9-items…md:56`:
> **"Grade → machine-read-block hop (BRENT)** — ✅ **TAKEN as a sweep leg, MEASURE FIRST.** Folds into Wiring Sweep #2 (~9/14) as *'count desks with a machine-read block before proposing a check'* … Sharper than STATUS-vs-ledger drift because **the reader is a machine, so the stale block certifies itself.**"

### D.1 Method
```
git log --since=2026-09-01 --format='%h %cs %s' -- AGENTS/BRENT | grep -iE "grade|adjudicat|resolv|verdict|NOT MET"
git show --stat --format='' <hash> | grep '\.tsv'
git show <hash> -- AGENTS/BRENT/thesis/PREDICTIONS.tsv        # then field-split every +/- row
.venv/bin/python AGENTS/BRENT/scripts/predictions_due.py      # the machine reader
```
Machine-readable fields in scope: `thesis/PREDICTIONS.tsv` cols **Status (6)** / **Date_Resolved (7)** / **Outcome (8)**; `workbook/REGISTRY.tsv` (levels consumed by `thresholds.py`); `docket/CATALYSTS.tsv`; `board_log.tsv`.

### D.2 The 5 most recent grades since 9/1

| # | Commit | Date | Grade (prose) | Machine cell moved in the SAME commit? |
|---|---|---|---|---|
| 1 | `114fa41ad` | 2026-09-14 | *"slope scaling moves a grade on BOTH #6 and #8 — #6 is scheduled to fire on pure roll"* | **🔴 NO — zero TSVs touched.** The commit's only file is `demand_destruction/TRACKER.md` (+6 lines, prose) |
| 2 | `5051e9061` | 2026-09-14 | *"WALTER -024/-025 graded — freight PRICES the disruption; **Boundary #5 is NO INSTRUMENT**"* | **PARTIAL** — `board_log.tsv` +2 (an inbox-consumption log, not a grade register). No boundary status cell exists to move |
| 3 | `635631fde` | 2026-09-12 | *"COT-35B #5 graded **JOINT NO-VERDICT**; **BG-02 re-graded NOT MET**; resolver defect found"* | **PARTIAL** — `board_log.tsv` +6, `docket/CATALYSTS.tsv` 3 ±; `PREDICTIONS.tsv` untouched; 13 `.md` files carry the grade |
| 4 | `1ff472552` | 2026-09-11 | *"Petroline frame-breaker **graded NOT MET** on the BG-02 letter; resolver pre-registered"* | **PARTIAL** — `board_log.tsv` +7, `docket/CATALYSTS.tsv` +1; 13 `.md` files |
| 5 | `a2daedfb8` | 2026-09-07 | *"frame-breaker **adjudicated** vs the M/T Kylo sinking — **NOT MET**, $0 moved, nothing armed"* | **🔴 NO.** `PREDICTIONS.tsv` +6 lines are **header comment lines only** — verified by field-split: no `-`/`+` data row. Its own `board_log.tsv` entry says so: *"DISPOSITION REGISTERED AS A HEADER BLOCK ON THE LEDGER (6 new # lines, **no cell edited**)"* |
| *(6, for contrast)* | `7d47bf6f2` | 2026-09-06 | *"OPEC+ Q4 **graded** at the Secretariat primary — outcome (3) DEFERRED AGAIN"* | **✅ YES** — `docket/CATALYSTS.tsv` row flipped `🔴 OPEC+ MEETING …` → `✅ OPEC+ MEETING — **FIRED 2026-09-06. GRADED SAME DAY** … OUTCOME (3) DEFERRED AGAIN`, **+ a successor row registered in the same diff** (`2026-10-04`). The clean case. |

### D.3 The two findings, kept separate

**D-a. For the class BRENT actually grades most — "Boundary #N" / frame-breaker letters — there is NO machine-readable field to lag.** Grep for a boundary register returns only prose surfaces: `NEXUS_BRIEF.md`, `TRADE.md`, `demand_destruction/TRACKER.md`, `setups/2026-09-11_petroline-frame-breaker-adjudication.md`, `setups/2026-09-12_petroline-four-quantities-and-resolver-defect.md`. `workbook/REGISTRY.tsv`'s own header says what it is: *"# BRENT TEST REGISTRY — **machine levels** consumed by `thresholds.py`, plus instrument enrollments"* — a levels table, not a grade table. `board_log.tsv` is an inbox-consumption log. **Verdict: the hop is not lagging; for this class it does not exist.** `114fa41ad` is the clean instance — a grade moved on two boundaries in a commit that touched zero machine-readable files.

**D-b. For the prediction class the hop is INTACT but UNEXERCISED in this window — so "does it lag?" is NOT-EVALUABLE, not clean.**
- `thesis/PREDICTIONS.tsv` has Status/Date_Resolved/Outcome columns and a real machine reader (`scripts/predictions_due.py`).
- **Zero Status or Date_Resolved cells moved in any commit since 2026-09-01.** Field-split of every `+`/`-` data row in the four PREDICTIONS.tsv touches (`7d47bf6f2` BRT-26, `df83fa757`/`0f71c2859`/`14d27e552` BRT-29) shows `Status=OPEN`, `Date_Resolved=` unchanged on both sides in every case — the edits are Prediction/Outcome prose.
- The newest `Date_Resolved` in the whole ledger is **2026-08-13** (BRT-16/17/21).
- And the reader agrees this is correct: `predictions_due.py` → `✅ no OPEN predictions past (or within 7d of) their timeframe`. **Nothing came due. The ledger is not stale-certifying; it has nothing to carry.**

⚠️ **Reviewer-side note against my own framing.** The 9/2 disposition's sharpener — *"the reader is a machine, so the stale block certifies itself"* — is **not demonstrated at BRENT in this window.** The machine reader returns a true clean. The defect found is the *adjacent* one: the grade-heavy class has no machine surface at all, which is invisible to any check that audits a machine block for staleness, because there is no block to audit. **A "count desks with a machine-read block" census would score BRENT as HAVING one and miss this entirely** — `finding_scan_keyed_on_naming_reads_local_form_as_absence`, inverted.

### D.4 Verdicts
| # | Verdict | Owner ask |
|---|---|---|
| D-1 | **REFUTED for the boundary/frame-breaker class** — 5 of 5 recent grades reached prose; 2 of 5 (`114fa41ad`, `a2daedfb8`) reached **no** machine-readable cell at all; no boundary grade register exists | **BRENT:** add a Status/Date_Graded column to a boundary register (or a `BOUNDARIES.tsv`) so `#5 NO INSTRUMENT`, `#6`, `#8`, `BG-02 NOT MET` are machine-readable — today they exist only in `TRACKER.md` prose. |
| D-2 | **NOT-EVALUABLE for the prediction class** — hop intact (cols + `predictions_due.py`), 0 Status transitions since 9/1, newest `Date_Resolved` 2026-08-13, reader returns a *true* clean | none; re-test at the next BRT resolution. |
| D-3 | **Clean positive control exists** — `7d47bf6f2` moved `docket/CATALYSTS.tsv` to `FIRED … GRADED SAME DAY` **and** registered the successor row in the same diff | **BRENT:** cite `7d47bf6f2` as your own house form when D-1 is built — the CATALYSTS hop already works. |
| D-4 | **Census-design correction (self)** — "count desks with a machine-read block" would score BRENT as compliant and miss D-1 | **DAEDALUS (self):** before ⑰ #2, re-spec the census to count **grade-classes without a machine surface**, not desks with a block. |

---

## SUMMARY — 4 legs, 17 verdicts, 13 owner asks

| Leg | Headline |
|---|---|
| **A** | Route-around census **7 → 1**, and the 1 is on RETIRED YEYOU. **1 desk LIVE (OTTO), 3 LATENT** across the ROUTE-AROUND set + controls. OTTO's canon was fixed 9/2 and its practice contradicted it 9/12 (`2a02ed3e0`); **0 WALTER drops all-time vs 11 direct sends.** |
| **B** | **8 of 44** surfaces declare `LEDGER_GLOB`; **7 surfaces hold 76 TSVs with 0 enforced** — the two largest are **WALTER (35)** and **PROME (10)**, the fleet's routing and obligation registries. Premise narrowed: a missing glob is only a defect where the default `workbook/*.tsv` matches zero, and 1c-bis states that scope rather than failing silently. |
| **C** | `recheck_by` **never existed** (0 rows, 0 readers) — but ZHAO built the same mechanism as a dated CATALYSTS `RE-CHECK` row, **it fired 9/16 and sits past-due, logged unread at `STATUS.md:174`.** LIQUID's watcher writes 5 targets; **`watch.log` — its own declared liveness proof — has no reader**, and the whole `alerts/` lane is gitignored (machine-local). |
| **D** | Hop **REFUTED for BRENT's boundary/frame-breaker class** (no machine surface exists; 2 of 5 grades touched zero TSVs), **NOT-EVALUABLE for the prediction class** (intact, 0 transitions since 9/1, reader returns a true clean). `7d47bf6f2` is the clean positive control. |

**Reviewer-side, on DAEDALUS's own work:** two of my own 9/2 dispositions need re-cutting — the `recheck_by` proposal is superseded by practice (C-1), and the "count desks with a machine-read block" census shape would have missed the defect it was commissioned to find (D-4). The `walter_route_check.py` perimeter omission (A-3) is mine too.

*Read-only run. No packet sent; no other desk's file touched; no threshold moved. — DAEDALUS reader, 2026-09-17*
