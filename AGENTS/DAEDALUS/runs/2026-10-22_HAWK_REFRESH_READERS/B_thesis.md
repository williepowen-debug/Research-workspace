# HAWK profile refresh: Reader B (thesis, domain and research)

**Reader:** Mode-A comprehension reader for DAEDALUS. Read-only. **Written:** 2026-10-22 17:47 EDT (from `date`).
**Scope:** `AGENTS/HAWK/thesis/`, `research/`, `domain/`, `archive/`. Ledgers, scripts, STATUS and CLAUDE.md belong to the other readers. I only touched them with targeted greps, listed in §7.
**Repo state at read:** HAWK's last owner commit is `a6c11f443` (2026-10-21 21:39). Session hawk-1021 made 6 commits between 20:35 and 21:39 on 10/21. Three inbox arrivals came after that closeout and are still pending (see F14).

---

## 1. Thesis map

| Surface | Version / date | Core claim (one line) | Evidence it rests on | Last substantive update (in-content · git) |
|---|---|---|---|---|
| **FLOW-HAWK-19** (`workbook/FLOW.tsv` row 8; canonical thesis home, not a THESIS.md) | LIVE, RE-CUT #2 2026-08-20 (re-cut #1 7/25) | The binding constraint on war stress reaching oil **migrated from physical destruction to insurer/owner willingness**. Three branches: (a) damage → supply priced; (b) no damage, tolerance holds → decoupling; (c) no damage, tolerance breaks → the premium reprices with zero barrels lost | KB-228/229/233/236/237/274/275; the MRPL clause; the transit decomposition (KB-233); owner ledgers. 10/21 combined read KB-440 ("risk premium, not lost barrels"), restored to **medium** by KB-450 | In-row stamp `[2026-09-28 DATED EVIDENCE … no re-cut]`. The 9/16 review softened it: willingness "cannot be assumed to be the sole present constraint". The 10/21 read lives in KB-440/450 and FALSIFICATION:10, not in the row. Status cell still says "Forward test: HAW-19" |
| **FLOW-HAWK-20** (Gulf chokepoint → Taiwan buffer stack) | Registered 7/28 as a LOW-PROBABILITY TAIL; first test stamped 8/20 | Fires only on the full **stack** (Qatar LNG loss + 12-day LNG reserve drawn + 40-day coal + simultaneous non-Gulf disruption). First observable: a **Taipower rationing announcement** | Ras Laffan FM since 3/24; Taipower reserve CSV | FALSIFICATION §2 (8/20, plus a 9/8 reserve retrieval). The TWN-01 10/21 re-sweep (KB-451) gives reserve minimum 10.19% on 10/04; LNG/coal days UNMEASURED |
| **FLOW-HAWK-21** (ton-miles → freight index → tanker equity) | ACTIVE, registered 2026-09-11 (VECTOR-1, DOCKET L324) | The chain breaks at the index→realization joint. BWET +1034% vs FRO +27.5%; Dorian realized TCE $75.9k/day vs index peak ~$170k | KB-366/367/368; owner 10-Q TCE | Row 9/11. **Self-registered falsifier: Q3-2026 TCE prints, late Oct–early Nov.** Not a prediction |
| **Coupling account** (`KB-HAWK-252`; FALSIFICATION §5) | 8/8 understanding; CPC rung graded 8/20 | The two wars couple through **US leverage over the attacker**, not through oil price. Not transferable to the Gulf | 8/8 CPC carve-out; Skiros 8/16 (Russian cargo, inside the carve-out); the MOU expired 8/17 | §5 durability rung "~8/24" is still undisposed and points at "the September11 OSPREY review". The 9/8 artifact rung is OSPREY-observed. **Not re-read since early September** |
| **Codification ratchet** (HAW-20; VX CODIF-01) | Registered 2026-08-20, 65% | "Suspensions unwind, codified costs do not." No instrument on the axis softens through 10/31 | 4 instruments: US S301, US S338, Iran toll bill, Mecca pact | 10/21 pre-assessment in KB-451. **Grade due 2026-10-31** |
| **EURMIL** (`VX-HAWK-EURMIL-01`; `domain/europe-rearm/`) | Opened 2026-09-18, ORANGE | Europe's **military** rungs (ROE, kinetic) have stepped while its **political-legal** rungs (Art. 4/5, mobilisation, EU instrument) have not; the gap is the signal | LADDER.md rungs 1–6; INCURSIONS.tsv (19 rows, last 9/17); the 9/18 sweep (heavily corrected 9/19) | LADDER "Last real data refresh 2026-09-18" (`233dfc212`, 9/19). The mark was re-read 10/10 (KB-430) and 10/21 (KB-439, research/…PROME-asks §3) **without a ladder refresh** |
| **Dormant book** (FALSIFICATION §4 + VX.tsv) | 10 table rows + EURMIL | Per-row band ladders: VEN G · TWN Y · TWNMIL Y · IRAQ Y · TRADE-01 O · TRADE-02 O · SULPHUR R · FININFRA Y · CEASEFIRE ⬛ · CODIF O | Per-row primaries (OFAC, Taipower, MND, SOMO, FR, etc.) | Re-swept 10/21: VEN/TWN/TWNMIL/CODIF (KB-451), TRADE-02 (KB-447). IRAQ/FININFRA/SULPHUR on 9/28. TRADE-01 on 9/10 |
| `thesis/THESIS.md` v1.2 · `CHANGELOG.md` · `TIMELINE.md` | 🧊 FROZEN 2026-07-12 (live copies at FALCON) | Pre-split Iran-ceasefire thesis (4/20) | — | THESIS pointer repaired 8/10 (`694f9a4c6`). Others `699c766a5` 7/12. Bannered correctly |
| `thesis/HAW-19_CONSOLIDATION.md` | 8/20, banners 9/10 | Semantics-preserving consolidation of HAW-19 plus D1/D2/D3 defects | — | `6fd24c71e` 9/10. **Not updated for HAW-22 registration (9/26) or the DEFECTIVE encode (9/28)** |
| `thesis/2026-09-02_CANADA_9-8_PREREGISTERED_READ.md` + `2026-09-08_HAW-21_ADJUDICATION.md` | 9/2 pre-reg; 9/8 adjudication | HAW-21: Canadian counter-tariffs in force by 9/15 → **CONFIRMED 9/8** (629/629 items matched) | P.C. 2026-0785/0786, CBSA 26-23, Finance list | `548ba44e7` 9/8. The 9/9 and 9/11 follow-ups (SOR identifiers) are not evidenced in thesis/ |

**Prediction book (`thesis/PREDICTIONS.tsv` preamble lines 2–5, verified):** 6 CONFIRMED / 9 FAILED / 1 PARTIALLY / 1 VOIDED / 2 REHOMED / 1 DEFECTIVE-INSTRUMENT / **2 OPEN**:
- **HAW-20**, 65%, resolves **10/31**, IMMOVABLE.
- **HAW-22**, 65% UNCALIBRATED. Event window 10/01–10/31, observation to 12/21, resolves **12/22**.

HAW-18 FAILED 8/4. HAW-19 was encoded DEFECTIVE-INSTRUMENT 9/28 with no Brier credit (WQ-212). HAW-21 CONFIRMED 9/8 (Brier 0.1225). The file is 96,616 B. The HAW-19 row alone is 41,125 B, and its Notes cell is 18,740 B.

---

## 2. Invalidation-surface inventory (blueprint §4; PAT-077/088)

The re-derivation stamp on FALSIFICATION.md is **"Refreshed: 2026-10-21"** (line 9). It names the rows re-read that pass: §1 reading, §4 VEN/TWN/TWNMIL/IRAQ mark/TRADE-02/CODIF. It says "§6 not re-read".

| # | path:line | Kind | In-content stamp | Current vs live thesis? | Current vs today (10/22)? |
|---|---|---|---|---|---|
| 1 | `thesis/FALSIFICATION.md:30` **K1** (branch (c) fails to reproduce: a willingness step-change with no crude transmission over 5 settles) | Kill criterion (thesis) | "Untested since the 7/23-24 origin event"; 10/21 note: "K1 is not tested at settles (BRENT owns them)" | Yes | ⚠️ **About 90 days untested** through a month of willingness step-changes: Hormuz 6–9%→6–10% (~10/06), JMIC Arabian Gulf → SUBSTANTIAL 10/18, Black Sea 0.2–0.5%→0.6–1.0% (10/09). No BRENT settle read has been requested. The kill is functionally dormant (F4) |
| 2 | `FALSIFICATION.md:31` **K2** (branch (a) returns: irreversible crude capacity destroyed AND supply repricing) | Kill criterion → instrument | "LIVE AGAIN — REPAIRED 2026-09-10" | ❌ **Names HAW-19 LEG A as the instrument.** That window closed 9/30 and was encoded DEFECTIVE 9/28. The cell also says the successor "is NOT YET REGISTERED", but HAW-22 was registered 9/26 | ❌ Dead instrument, 22 days after window close (F1) |
| 3 | `FALSIFICATION.md:33-47` CPC/LEG-A stated limit + aggregation clause (D3 ≥N of M) | Stated limit | 8/20, plus a 9/10 note | Historical. D3 is still unparameterized and HAW-22 inherits it ("A.2(a) only") | Carried honestly |
| 4 | `FALSIFICATION.md:49` MRPL durability test ("does the clause survive a materially SAFER transit read") | Forward test (owed) | 8/20 | Yes | ⚠️ Owed since 8/20 with no date and no instrument. Transit has not become safer, so it is untriggerable rather than overdue |
| 5 | `FALSIFICATION.md:53-61` FLOW-20 stack + Taipower rationing observable | Fire criterion | First test 8/20; 9/8 follow-up | Yes | Endpoint quiet per TWN 10/21. Fuel-buffer legs UNMEASURED, so legs (b)/(c) cannot be read |
| 6 | `FALSIFICATION.md:65-77` transit decomposition: DENIAL vs REROUTING (= HAW-19 LEG B) | Falsifier | "Historical August15 claim, not a September16 certification" | Instrument (HAW-19 LEG B) dead after 9/30. **No successor for the denial-vs-rerouting test.** HAW-22 explicitly excludes hull losses | ❌ No live instrument (F1) |
| 7 | KB-233 transit decomposition, cheapest falsifier ("WC Saudi no-transit 0.1% — if it rises materially, risk migrated transit→origin") | Falsifier (never registered) | KB-233 dated 7/25, review-by 2026-08-25, ACTIVE | Not on FALSIFICATION (0 hits for "West Coast"/"0.1%") | ⚠️ The non-transit leg went 0.1% → **~3% Saudi-linked at Yanbu (9/24)**. FLOW-19's 9/28 stamp absorbs that as willingness evidence. KB-233 is still ACTIVE and still says "strongest quantitative evidence" (F5) |
| 8 | `FALSIFICATION.md:79-92` §3a instrument ruling (AIS transit counts refute one direction only) | Instrument rule | 8/19–8/20; 9/8 owner note | Yes, re-affirmed 10/21 via KB-450 (PortWatch = AIS lower bound) | Current |
| 9 | `FALSIFICATION.md:104` VEN-01 GREEN→ORANGE | Promotion gate | 10/21 reading | Yes. Up-only gate; §7:167 flags that the ladder cannot represent its own Jan-3 RED firing ("flagged, not patched", 63 days) | Military leg UNMEASURED |
| 10 | `:105` TWN-01 YELLOW | Promotion gate | 10/21 reading | ⚠️ The row states only the ORANGE→RED condition. **No gate from the current YELLOW mark on this surface** (VX bands carry Orange text "Reserves <10 days, amber alert") | LNG/coal days UNMEASURED, so the YELLOW→ORANGE instrument is unread |
| 11 | `:106` TWNMIL-01 YELLOW→ORANGE / →RED | Promotion gate | 10/21 reading | Yes. Up-only; no down gate | MSA notices not read at primary |
| 12 | `:107` IRAQ-01 | Gate | RED→YELLOW MET and RULED 9/28 (WQ-319) | Next gate YELLOW→GREEN only (FM lifted). **No re-escalation gate written** | Current to 9/28 |
| 13 | `:108` TRADE-01 ORANGE | Gate | Fired YELLOW→ORANGE 9/10 (WQ-211) | ⚠️ **The only gate written has fired. Nothing from ORANGE is on this surface** (VX Red: "Full decoupling, retaliation escalation") | 11/9–10 lapse clock carried in SCRATCH:53, not here |
| 14 | `:109` TRADE-02 ORANGE→RED | Gate | 10/21 FR-primary reading | ❌ "**THE RED BAND HAS NO OPERATIONAL DEFINITION — owed**". Owed since 8/20 (63 days). HAW-21 said the re-cut was owed at the 9/24 clock | One-directional and undefined (F8) |
| 15 | `:110` SULPHUR-01 RED→ORANGE (<$700/t delivered Kolwezi) | Gate | No new adjudication on this surface | ⚠️ The row says the "~$900/t build is stale March/April" and "No live matched feed". VX was re-swept 9/28 (KB-419) and holds RED on an Ivanhoe **mine-gate** ~$840/t basis. FALSIFICATION was not updated | Unfireable for lack of a feed, so the RED mark is carried indefinitely (HAW-03 class) |
| 16 | `:111` FININFRA-01 YELLOW→ORANGE (WQ-320 definition) | Gate | 9/28 | Yes, two-directional | Current to 9/28 |
| 17 | `:113` CODIF-01 | Gate | 10/21 reading | Yes. ORANGE; repeal/lapse is the down direction | Current |
| 18 | `:132-134` Coupling ladder rungs (CPC ✅ 8/20 · Durability ~8/24 · Artifact 9/8) | Falsification ladder | 8/20; 9/8 | ⚠️ The durability rung has never been disposed: "Carry to the September11 OSPREY review". No forward rung exists. GL 135 (10/09), a new US-Russia instrument spanning both wars, is not assessed against the account | Stale since ~9/11 (F10) |
| 19 | `:153-155` §6 registered rows | Prediction rail | "§6 not re-read" on 10/21 | HAW-19 row historical. HAW-22 prints are in the header (10/10, 10/21) | HAW-20 grade **in 9 days** (F3). HAW-22 event window closes the same day (F2) |
| 20 | `:163` K3 level-vs-willingness confound | Declared untestable | — | Yes | Declared, not hidden |
| 21 | `:177-186` §EURMIL E1–E6 | Kill tree (vector) | Registered 9/18 | Yes | ⚠️ E4 ("next sweep", the likeliest way the read is wrong) has not been run in 34 days. E5 needs a 2026 NATO primary. :188 "Not yet agreed" is stale (HANS AGREED 9/18, `domain/europe-rearm/README.md:88`) |
| 22 | `domain/europe-rearm/LADDER.md:13-24` rung table + `:~95` forward discriminator for Article 4 | State surface + discriminator | "Last real data refresh 2026-09-18"; self-bar **14 days per rung** | Yes | ❌ All 6 rungs are 34 days old with **no ⏳ marks**, against its own rule (`LADDER.md:4`). October RU↔NATO items (Bulgaria "considered Art. 4", Russia-attributed EEZ hull strikes 10/05, 10/06, 10/13, Belarus→Latvia 10/06) are not on the ladder or in INCURSIONS.tsv (last row 9/17) (F7) |
| 23 | `PREDICTIONS.tsv:42` HAW-20 resolution criteria | Prediction letter | Registered 8/20 | Yes | Dated-search requirement at FR/USTR/CIT/Majlis/foreign ministries. KB-451 shows an "in spirit" reading drifting off the letter (F3) |
| 24 | `PREDICTIONS.tsv:44` HAW-22 | Prediction letter | Registered 9/26 | Yes, but the scope is terminals only (F1) | 10/01–10/21 prints: no candidate (KB-432, KB-441). The 10/22 WALTER-028 Yanbu fire claim (CLAIM-ONLY) is pending disposition |
| 25 | FLOW-HAWK-21 own falsifier (FLOW.tsv row 10: "if owners' NEXT reported TCE rises toward the index … this row is wrong", Q3 prints late Oct/early Nov) | Falsifier | 9/11 | Yes | ⚠️ **Window opens now.** Not on FALSIFICATION (0 hits) or CATALYSTS. Only `STATUS.md:75` carries it (F6) |
| 26 | `research/2026-10-21_C3_limb2_GRADE.md` (HAWK grades OSPREY's C3 limb 2) | External kill-limb grade | 10/21 | Yes. NOT SATISFIED; recommends a prospective SCOPE qualifier (Will's call) | Current. Next canvass is OSPREY's |
| 27 | `workbook/EXIT_PROTOCOL.md` | Retired rail | 🧊 FROZEN 2026-08-10, blessed 8/15 | Superseded by FALSIFICATION.md (`:7`) | Correctly dead |
| 28 | `research/DEADLINE_SCENARIO_TREE_APR21.md`, `POST_DEADLINE_PLAYBOOK.md` | Retired prescriptive rails | 🧊 FROZEN 2026-08-10 | — | Correctly dead |

**Count of gates from the current mark (dormant book, 9 live rows):**
- **Live and measurable: 5** (VEN, TWNMIL, IRAQ down-only, FININFRA, CODIF).
- **Missing, undefined or unfeedable: 4.**
  - TWN-01: no gate stated on this surface.
  - TRADE-01: no gate stated on this surface.
  - TRADE-02: RED band undefined.
  - SULPHUR-01: no feed.

---

## 3. Where the richness lives, and HAWK's local vocabulary and form

**A future editor must read, in this order:**
1. `thesis/FALSIFICATION.md`, whole (39,725 B). HAWK's judgment is concentrated here: kill criteria, stated limits, instrument rulings, gate tables, and "what this surface does not cover".
2. `thesis/PREDICTIONS.tsv`: the preamble (lines 1–21) plus rows HAW-18 to HAW-22, read whole. The Notes cells carry the confidence derivations: "WHY 70% AND NOT 85%", inversion tests, the connective-counting ratchet argument, and the disclosure tests. HAW-19's 41 KB row is the record of the D1 repair and the defective disposition.
3. `thesis/HAW-19_CONSOLIDATION.md`: the model for amending a live row (equivalence map, disclosure test, put to Will rather than self-patched).
4. `thesis/2026-09-02_CANADA_9-8_PREREGISTERED_READ.md` + `2026-09-08_HAW-21_ADJUDICATION.md`: the best pre-registration exemplar. It asks "which branch happens if nobody acts" and records an inverted default.
5. `research/2026-09-19_L432_resolution_card.md` + `2026-09-21_L432_GRADE.md`: instrument-tested-before-the-date. HTTP vs HTTPS reachability, scanned-PDF limits, three-valued grade, "perimeter partial".
6. `research/2026-10-21_C3_limb2_GRADE.md` + `domain/war-risk/CROSS_THEATER_WAR_RISK.md`: grading a sibling's kill limb, separating unmeasured from negative, and naming the circular-pointer finding (9/19).
7. `domain/energy-strikes/CROSS_WAR_SUMMARY.md`: the reconciliation mechanics in practice.
8. `domain/europe-rearm/LADDER.md` + `README.md`: the dyad boundary and the forward discriminator.
9. `workbook/KB.tsv` rows 224+ and FLOW-HAWK-19's in-row stamps. These belong to the ledger reader but carry the dated evidence.

**Vocabulary and form:**
- **Grading on "the letter":** "on the letter" vs "in spirit". A **dated search attempt** is required for CONFIRMED ("I looked and found nothing", never "I did not look").
- **Outcome tokens:** **NO-VERDICT band**, **UNRESOLVED-CANDIDATE**, **DEFECTIVE-INSTRUMENT**, **UNCALIBRATED** (always travels with the number), **CANNOT-FIRE**, **UNMEASURED** vs reached-and-negative, **SEARCH-NOT-FOUND**, **PERIMETER PARTIAL**.
- **Anchor types:** **IMMOVABLE** vs **SOVEREIGN-MOVABLE**.
- **Thesis structure:** branch (a)/(b)/(c). K1/K2/K3 kills. LEG A/B with sub-limbs A.1–A.4 and B.1–B.5. "Explicit pre-registered non-fires". "Disclosure test" (does a patch move scored mass).
- **Gate form:** every gate must be stated as "moves the row from band X to band Y". Bands are unmoved; marks are corrected only by Will or PROME ("never silently re-marked", either direction).
- **Evidence tags:** `[CONF owner report]` / `[EST]`; source grades B2/B3; "owner-pending, not adopted"; "derived, not self-updating"; "capacity, not barrels"; "premium, not lost barrels"; "count it once, at the refinery".
- **Ownership language:** "Reconcile by belligerent dyad" (KB-238); "the object is OSPREY's, the reaction is HAWK's".
- **Banners:** kill-on-sight phrasings marked ⛔ in place. Corrections are kept beside the original ("kept as written on 9/19").
- **Citations:** WQ-NNN rulings, DOCKET Lnnn, KB-HAWK-nnn on every claim.
- **Runtime:** sessions span Claude (10/10 header: Opus 5.5) and Codex/Astra (the 9/16 cross-war review is authored "HAWK, Codex/Astra").

---

## 4. Cross-theater reconciliation mechanics and the dormant-book banner

**Topology** (`AGENTS/_NETWORK.md:97-101,206`): OSPREY and FALCON send their theater reads to HAWK, and HAWK sends a reconciled read to BRENT. **Acute 🔴 theater signals also go directly to BRENT, with HAWK cc'd.** So the double-count risk is structural: BRENT can receive one event twice, once directly and once through HAWK.

**How HAWK prevents double-counting (observed in artifacts):**

| Mechanism | Where |
|---|---|
| HAWK keeps no theater event ledger. Aggregates are regenerated from owner ledgers pinned **by commit hash and row count**, with "heterogeneous rows, not a census, not additive capacity" stated every pass | `CROSS_WAR_SUMMARY.md:7-13,38-44` |
| **Consumed-baseline discipline toward BRENT:** an item BRENT already consumed is labelled "corroborated baseline, not a fresh alert" and is not re-issued | `research/2026-09-16_cross-war-oil-review.md` §Provenance; `CROSS_WAR_SUMMARY.md:112` ("BRENT already consumed the correction September15; do not issue it as a new alert") |
| **No pooled lost-barrel figure across theaters.** Molecule asymmetry: Russia's damage is refining/products, the Gulf's is crude transport, hulls and an uncounted threat to processing | `CROSS_WAR_SUMMARY.md:28,66,93,105` |
| **One barrel, counted once:** a refinery-strike diesel loss and an undelivered GL 135 tranche are ONE barrel, counted at the refinery | `CROSS_WAR_SUMMARY.md:30,68` |
| Sibling events found by HAWK's own sweeps are "owner-pending, NOT adopted" into counts ("a derived surface that starts logging its sources' events has stopped being derived") | `CROSS_WAR_SUMMARY.md:88,97` |
| Prediction legs grade off FALCON's and OSPREY's ledgers: "I keep no competing copy" | HAW-19 Notes, MEASUREMENT segment |
| Price stays BRENT's: K1 reads "settles, never intraday", BRENT-owned | `FALSIFICATION.md:30`; KB-440 "[BRENT owns]" |
| Same instrument on two vectors is "one instrument, different axes": HAW-20 grades softening, TRADE-02 economic transmission, CODIF codification status | `FALSIFICATION.md:108`; HAW-20 OWNERSHIP NOTE |
| The dyad split extends the rule to Europe: RU↔UA is OSPREY's, RU↔NATO/EU is HAWK's; YURI owns the decision and HAWK the reaction | `domain/europe-rearm/README.md:16-30`; `research/…PROME-asks §3` |
| Explicit per-vintage refusal to mix legs ("mixing a 10/06 Hormuz leg with a 9/24 WC leg would mix vintages") | `CROSS_THEATER_WAR_RISK.md:10,13` |

**Gap:** no artifact records a per-session check that a HAWK-to-BRENT read did not restate an acute item BRENT already received directly. The discipline is visible (9/16, 9/15 correction), but it is applied case by case, not checked on every pass (inferred).

**Is the dormant book bannered as dormant?** Partly.
- It is named as such in FALSIFICATION §4 ("DORMANT BOOK — per-row promotion gates"), in HAW-20, and in the CLAUDE.md domain line.
- Frozen theater files are all bannered 🧊 FROZEN with successor pointers: THESIS/CHANGELOG/TIMELINE, STRIKES/SUMMARY, RUSSIA_OIL_INFRA, the DEADLINE tree, the playbook, EXIT_PROTOCOL.
- **"Dormant" is a cadence and charter label, not a state.** Of the 10 table rows, 4 are ORANGE (TRADE-01, TRADE-02, CODIF, plus EURMIL beside the table) and 1 is RED (SULPHUR).
- No Taiwan, Venezuela, sanctions or chokepoint dossier exists in `domain/`. The dormant book lives entirely in VX rows plus the FALSIFICATION §4 table.
- EURMIL sits under the dormant charter (defense spending) but calls itself a "live-thin standing surface".
- A reader should not infer "quiet" from "dormant". The old profile's DO-NOT-TOUCH #1 ("low activity there is correct by design") still holds for cadence, but 5 rows are not low-state.

---

## 5. Findings

| # | Sev | Finding | Evidence | V/I |
|---|---|---|---|---|
| F1 | 🔴 | **FLOW-HAWK-19's kill criterion K2 has no live instrument on the asset class where the Gulf threat moved.** K2's cell still names **HAW-19 LEG A** (window closed 9/30, DEFECTIVE 9/28) and says the successor "is NOT YET REGISTERED". HAW-22 was registered 9/26. The successor's letter covers only "a named **crude-export terminal**". HAW-19 A.1 covered "crude-oil **production field, stabilization/processing facility**, or crude-export terminal". In October the threat moved upstream: Abqaiq flare heat 10/08, Khurais/Shedgum/north-Ghawar 10/03–10, Shaybah intercept 10/21. HAW-19 LEG B (denial vs rerouting) also has no successor; HAW-22 excludes hulls. FLOW-19's Status cell still says "Forward test: HAW-19" | `thesis/FALSIFICATION.md:31,169`; `PREDICTIONS.tsv:44` [3] vs `:41` [3] A.1; `domain/energy-strikes/CROSS_WAR_SUMMARY.md:22,57,61`; `workbook/FLOW.tsv` row 8 [4] | V (texts); I (significance) |
| F2 | 🟠 | **Falsification horizon cliff on 10/31.** HAW-20 resolves 10/31 and HAW-22's event window closes 10/31. A grep of STATUS, SCRATCH and NEXUS found no successor or HAW-23 planned. From 11/01 the desk has no prediction with an open event window: HAW-22 stays OPEN only as a disclosure-observation row to 12/22. Will's 8/15 ruling ("a desk with no open predictions is UNGRADEABLE") is the precedent | `PREDICTIONS.tsv:7`; `:42` [5], `:44` [9]; grep of STATUS/SCRATCH/NEXUS_BRIEF | V (dates); I (consequence) |
| F3 | 🟠 | **HAW-20 grade is drifting off its letter 9 days before resolution.** The letter: "PRODUCT-LEVEL CARVE-OUTS, ANNEX CLARIFICATIONS AND EXCLUSION PROCESSES EXPLICITLY DO NOT FIRE … fixed BEFORE the evidence arrives". KB-451 and FALSIFICATION:15 now say the S338 Annex I Part B scope cut is, "in spirit, … a partial softening, which the 10/31 grade must adjudicate explicitly". This reopens what the pre-registration closed: the HAW-10 "prediction text vs threshold text" class from HAWK's own LESSONS. A MARCO packet on S338 is also pending in the inbox | `PREDICTIONS.tsv:42` [9]; `workbook/KB.tsv` KB-HAWK-451; `FALSIFICATION.md:15`; `inbox/2026-10-21_from-MARCO_s338-…` | V |
| F4 | 🟠 | **K1 has been untested for about 90 days through a month of willingness step-changes.** Examples: Hormuz 6–10% (~10/06), JMIC Arabian Gulf SUBSTANTIAL 10/18, Black Sea 0.6–1.0% (10/09), US ordered departure from Saudi Arabia 10/21. K1 needs a 5-settle BRENT read after such an event, and none was requested. The 10/21 note only says "K1 is not tested at settles (BRENT owns them)" | `FALSIFICATION.md:10,30`; `CROSS_THEATER_WAR_RISK.md:7,11`; KB-440 | V (state); I (should have fired a test) |
| F5 | 🟠 | **The transit-decomposition claim (KB-233) lost its cheapest falsifier without a record.** KB-233: West Coast Saudi calls with no chokepoint transit = 0.1% of hull, so the premium "decomposes on transit". By 9/24 Yanbu Saudi-linked was ~3%, about 30×. The falsifier was never registered on FALSIFICATION (0 hits for "West Coast" or "0.1%"). KB-233 is still ACTIVE past its 8/25 review date and still tagged "STRONGEST QUANTITATIVE EVIDENCE". FLOW-19's 9/28 stamp absorbs the rise as willingness evidence. The two can both be true (attacker/flag-linked pricing, not transit-linked), but the decomposition's status is unrecorded | `workbook/KB.tsv` KB-HAWK-232/233; `FLOW.tsv` row 8 `[2026-09-28 …]`; `CROSS_THEATER_WAR_RISK.md:10` | V (texts); I (falsified-in-substance) |
| F6 | 🟠 | **FLOW-HAWK-21's self-registered falsifier is due now and is off the falsification surface.** "If owners' NEXT reported TCE … rises toward the index … this row is wrong" at the Q3 prints (late Oct–early Nov). 0 hits in FALSIFICATION.md, not in CATALYSTS.tsv. Only `STATUS.md:75` carries it. A DEWEY "tanker-war base rates" packet (10/22) is pending in the inbox | `workbook/FLOW.tsv` row 10; `STATUS.md:75`; `inbox/2026-10-22_from-DEWEY_tanker-war-base-rates.md` | V |
| F7 | 🟠 | **The Europe ladder breaches its own staleness rule, and the native ledger stopped at 9/17.** LADDER says "Last real data refresh 2026-09-18", bar 14 days per rung, ⏳ mark required. All 6 rungs are 34 days old and unmarked. INCURSIONS.tsv's last row is EUR-2026-019 (9/17). October RU↔NATO items appear only in research and KB: Bulgaria "considered Article 4" (none requested), Russia-attributed EEZ hull strikes 10/05, 10/06, 10/13, Belarus→Latvia 10/06, Lithuania's ~100 troops. That is HAWK's own dyad. The Bulgaria case may be a candidate trial for the ladder's forward Article-4 discriminator, which needs NATO territory and manned/mass/fatality; EEZ ≠ territory. It is unrecorded either way. EURMIL's VX review cell is still 9/18 despite the 10/10 and 10/21 re-reads. E4 ("next sweep") is not run | `domain/europe-rearm/LADDER.md:3-4,13-24`, forward-discriminator block; `INCURSIONS.tsv` tail; `research/2026-10-21_PROME-asks…md` §3; `FALSIFICATION.md:182`; VX EURMIL [9] | V (dates, absence); I (trial candidacy) |
| F8 | 🟠 | **4 of 9 live dormant rows have no usable gate from the current mark.** TRADE-02 RED undefined since 8/20 (63 days; the re-cut was "owed at the 9/24 clock" per HAW-21). SULPHUR RED: "No live matched feed", so the RED mark is held indefinitely. TWN-01 and TRADE-01 rows state no transition from the current mark on this surface. The FALSIFICATION SULPHUR row is also stale against VX's 9/28 mine-gate re-sweep (KB-419) | `FALSIFICATION.md:105,108,109,110`; `PREDICTIONS.tsv:43` [3] (iv); VX SULPHUR [3],[9] | V |
| F9 | 🟡 | **Same-session supersessions were not propagated.** `CROSS_WAR_SUMMARY.md:29` and `research/…PROME-asks §4` say the read is "medium-low (KB-446)"; KB-450, committed later the same session, resolved KB-446 and **restored the read to medium**. The PROME-asks §2/§4 ("canvass has NOT been run"; "the single dated event … OSPREY's C3 canvass, Mon 10/26") were overtaken within about 40 minutes by the C3 grade (KB-449), with no addendum. Neither KB-445 nor the research file is marked superseded | `CROSS_WAR_SUMMARY.md:29`; `research/2026-10-21_PROME-asks_L433-L439-L432.md` §2, §4; KB-445/446/449/450; commit order 386402e22 → 5a159c8fc → b62f62841 → 7943b8bdb | V |
| F10 | 🟡 | **FALSIFICATION.md internal staleness.** §5 durability rung "carry to the September11 OSPREY review" (undisposed). §7:164 "Hormuz July22 is 56 days old on September16" (the current quote is ~10/06). §7:169 "the 2026-09-09 observation … is still outstanding" contradicts :12 (graded 10/21, KB-448). :188 "Not yet agreed" contradicts README:88 AGREED 9/18. Size header says "34,306 B as of 2026-09-18"; actual is **39,725 B**, 73% of the 54,250 B single-read cap. At ~160 B/day the self-set ~48,000 B decision line arrives around mid-December, and the rotation decision is still undone | `FALSIFICATION.md:3,133,164,169,188`; `wc -c` | V |
| F11 | 🟡 | `thesis/HAW-19_CONSOLIDATION.md:77` still says the successor "is NOT registered … NOT ready on data". It has no overtaken banner, unlike `research/2026-09-25_L321…md`, which carries one. The file's last edit was 9/10 | `HAW-19_CONSOLIDATION.md:77`; `git log` | V |
| F12 | 🟡 | **Unbannered stale cohort, eligible for retirement.** `research/IRAN-CROSSAGENT-2026-02-18.md` ("Status: 🔴 RED", Brent ~$67–69), `REFINERS-UKRAINE-2026-02-18.md`, `BOARD_CATCHUP_2026-04-20.md`, `HERMES_V2_DESIGN_NOTE.md` (6/19). In `domain/sources/`: `ENERGY_DOMINANCE_STRATEGY.md` ("Status: Active/Ongoing"), `LNG_DISRUPTION_MAR2.md` ("ACTIVE / ESCALATING"), `OIL_INFRASTRUCTURE_DISRUPTIONS.md`, `russia_oil_infrastructure_damage_assessment.md`, `ukrainian_energy_warfare_doctrine_thesis.md` ("FORMAL THESIS"). All are >60 days old. Each is referenced only by DAEDALUS manifests/inventories (plus one 5/22 HAWK audit for LNG), which do not count under root Data Hygiene clause ② | file heads; grep of AGENTS/ and PROME/ | V |
| F13 | 🟡 | `domain/europe-rearm/README.md:82` heading "(open — not yet agreed)" sits over a body that says "✅ Status: AGREED 2026-09-18". Same drift as F10's :188 | README:82,88 | V |
| F14 | 🟡 | **Three post-closeout arrivals are pending and bear on live rails:** MARCO 10/21 (S338 stacking; cars, light trucks and parts still unlisted → HAW-20 leg b), DEWEY 10/22 (tanker-war base rates → K1, FLOW-21), and WALTER SIG-W-20261022-028 (Houthi Yanbu fire CLAIM-ONLY → an in-window HAW-22 candidate needing a disposition). Not read beyond headers | `inbox/` listing | V (presence) |
| F15 | 🟡+ | **Positive / overtaken grade text.** The FLEET_MAP HAWK row (10/21) says "Last owner session 10/10" and "October STEO/N6 observation remains owed". Both are overtaken: session hawk-1021 ran (6 commits, 10/21 20:35–21:39), and N6 was run at the EIA primary, September DECAY and October EXTENSION (KB-448; FALSIFICATION:12). The named L5 condition's N6 leg is discharged | `AGENTS/DAEDALUS/FLEET_MAP.tsv` HAWK row; KB-448; `git log` | V |
| F16 | 🟡 | **Strengths to preserve (best-in-fleet practice, still evident).** Pre-registration with explicit non-fires and NO-VERDICT bands. Refusal to amend a live row on its own authority, putting it to Will (HAW-19 D1, the C3 limb-2 cause qualifier). The defective-instrument disposition kept separate from the repair. A three-valued grade preserved (L432, L433). Unreachable vs negative held distinct (C3, Platts 403). Fast self-correction on sibling verification (the OSPREY 8/20 figures, the HANS "no answer" claim) | as cited in §3 | V |

---

## 6. Reconciliation against the OLD profile (`profiles/HAWK.md`, body 8/7)

**§3 invalidation inventory:**

| Old §3 row | Verdict | Now |
|---|---|---|
| `workbook/EXIT_PROTOCOL.md`: 🔴 140d, unstamped, "must NOT be frozen" | **OBSOLETE** | 🧊 FROZEN 2026-08-10, blessed by Will 8/15. Successor `thesis/FALSIFICATION.md`, born 8/20 (`FALSIFICATION.md:5-7`). DO-NOT-TOUCH #6 is dead |
| FLOW-HAWK-19 🟢, re-cut 7/25, "kill only implicit" | **CHANGED** | Re-cut #2 8/20. The kill is now explicit (K1/K2/K3). Softened 9/16 ("not the sole present constraint"). The K2 instrument is stale (F1) and K1 dormant (F4) |
| FLOW-HAWK-20 🟢, untested | **CHANGED** | First test stamped 8/20 (upstream strengthened, endpoint quiet). The TWN 10/21 reserve read leaves the fuel legs UNMEASURED |
| FLOW-13/15 retired 7/28 | **STILL TRUE** | Retired-not-deleted, FLOW.tsv rows 4–5 |
| FLOW-HAWK-10 self-deferred to 8/4 (passed) | **CHANGED** | In-row "[Aug 15 RE-CHECK — DOUBLE-LAPSE CLOSED]" and "[2026-09-08 partial primary review]". Not on FALSIFICATION |
| PREDICTIONS 18 rows, sole OPEN HAW-18 | **CHANGED** | 22 rows. HAW-18 FAILED 8/4. HAW-19 DEFECTIVE 9/28. HAW-21 CONFIRMED 9/8. OPEN = HAW-20 (10/31) and HAW-22 (12/22). Cliff 10/31 (F2) |
| Dormant-book gates (9 rows), 45d clock expired 8/4 | **CHANGED** | 10 table rows + EURMIL (11 VX). Re-swept 9/28 and 10/21. Gates written per row, but 4/9 unusable (F8). Two band-scoring defects (D1 TWN, D2 FININFRA) were RULED 8/20 |
| `CROSS_THEATER_WAR_RISK.md` 🔴 5/5 legs past 10-day bar | **STILL TRUE (structurally)** | Still 5/5 past the bar on 10/21 (Black Sea freshest at 12d). The staleness is now **declared on the surface each pass**, and the matched ratio is honestly UNKNOWN. The 7/31 escalate trigger is superseded |
| `CROSS_WAR_SUMMARY.md` 🟠 sibling-understatement ×3 | **CHANGED** | Now pins owner heads by commit and states owner-state per side ("OSPREY swept-complete 10/11 … the less-swept one"), which fixes that class. New defect: a superseded same-session read (F9). The "Reconciled current read" table (:71-80) is 9/16 vintage under a "current" heading |
| NEXUS_BRIEF 🔴 | Out of my scope (root reader) | — |
| Sunset re-arm condition 🟠 | **OBSOLETE** | Conditions (successor surface + ≥1 dated row) met 8/20. The desk has been active since (sessions 9/2, 9/8, 9/10, 9/16–9/28, 10/10, 10/21) |
| LESSONS 🟢 7/28 | **CHANGED** | Rotated 10/21 (`archive/LESSONS_ROTATED_2026-10-21.md`). Content is the root reader's |

**Grade story / F4 scope / flags:**

| Old item | Verdict | Now |
|---|---|---|
| L4 holds; L5 = one blocker (F4 EXIT_PROTOCOL rewrite) | **CHANGED** | F4 discharged by FALSIFICATION.md 8/20. The current FLEET_MAP L5 condition (the N6 observation) was discharged 10/21 (F15). New blockers to weigh: F1–F3 |
| F4 content list: FLOW-19 kill · FLOW-20 fire · 3-dyad re-coupling kill · transit-decomposition falsifier (WC Saudi 0.1%) · RED steelman · per-row gates · FILES registration and closeout hook | **MOSTLY CHANGED** | Covered: FLOW-19 kill (§1), FLOW-20 (§2), RED steelman (:49 durability), per-row gates (§4), closeout re-read (:18 "Re-read at every HAWK closeout"). **NOT covered: the 3-dyad re-coupling kill (no hit) and the WC-Saudi 0.1% falsifier (F5)** |
| "HAWK has NO scenario ladder post-split" | **STILL TRUE** | THESIS.md repointed to FALCON 8/10 |
| Open Q4: does the 3-dyad finding change structure or narration? | **CHANGED** | Now encoded as rule (CLAUDE.md:29, "Reconcile by belligerent dyad"), extended to RU↔NATO (europe-rearm README §2) |
| 🔴 22 unconsumed inbound incl. FLOW-19 evidence hits | **OBSOLETE** | Drained 8/15, 10/10 (66/66), 10/21. 3 new pending (F14) |
| 🟡 March cohort banners (POLITICAL_SUSTAINABILITY, DECK_EVIDENCE, BOOT_LOG) | **PARTLY CHANGED** | The 8/10 banner sweep covered 5 surfaces. A **second unbannered cohort** remains in research/ and domain/sources/ (F12) |
| 🟡 sanctions-tracker lane unbuilt | **STILL TRUE** | `FALSIFICATION.md:165` |
| DO-NOT-TOUCH #7 "HAW-18 not amended mid-window" | **STILL TRUE (as principle)** | Applied again to HAW-19 (put to Will) and the C3 limb 2 (prospective only) |
| DO-NOT-TOUCH #5 FLOW-19 canonical home | **STILL TRUE** | — |

---

## 7. Coverage

**Read whole:**
- `thesis/FALSIFICATION.md` 1–188 (3 chunks).
- `thesis/HAW-19_CONSOLIDATION.md` 1–110.
- `thesis/PREDICTIONS.tsv`: lines 1–22, plus rows HAW-20, HAW-21 and HAW-22 (lines 42–44, every field).
- `research/2026-10-21_C3_limb2_GRADE.md` 1–31.
- `research/2026-10-21_PROME-asks_L433-L439-L432.md` 1–74.
- `domain/energy-strikes/CROSS_WAR_SUMMARY.md` 1–119.
- `domain/war-risk/CROSS_THEATER_WAR_RISK.md` 1–72.

**Read partially:**
- `PREDICTIONS.tsv` HAW-19 (line 41): fields 1–8 whole; field 3 (14,713 chars) whole; field 9 first 1,500 of 3,544; field 10 only the first 260 chars of each `||` segment.
- `PREDICTIONS.tsv` rows HAW-01 to HAW-18 (lines 23–40): every field truncated at 400 chars.
- `thesis/2026-09-02_CANADA_9-8_PREREGISTERED_READ.md`: lines 1–30 (lines cut at 700 chars) plus the heading list. **Body 31–105 not read.**
- `thesis/2026-09-08_HAW-21_ADJUDICATION.md`: 1–49, lines cut at 600 chars (a few long lines truncated).
- `thesis/THESIS.md`, `CHANGELOG.md`, `TIMELINE.md`: first 3,500 B each (banners plus the opening).
- `thesis/PREDICTIONS_ARCHIVE.md`: first 3,500 B, headings, last 2,500 B (HAW-21 section).
- `research/2026-09-19_L432_resolution_card.md`: 1–112, lines cut at 900 chars.
- `research/2026-09-25_L321_HAW19-successor_NOT-REGISTERED.md`: 1–53, lines cut at 700.
- `research/2026-09-16_cross-war-oil-review.md`: 1–25 and 75–83 plus headings.
- `research/2026-09-18_european-rearmament-evidence-sweep.md`, `2026-09-21_L432_GRADE.md`, `2026-09-25_L433_GRADE.md`, `2026-09-21_SIG-W-007…`, `2026-09-21_SIG-W-010-013…`, `2026-09-21_suwalki…`, `2026-09-22_WALTER-v047…`, `2026-09-22_covert-claim…`: first ~1,800 B each plus heading lists.
- `research/` older files (BOARD_CATCHUP, DEADLINE tree, HERMES, IRAN-CROSSAGENT, POST_DEADLINE, REFINERS, RUSSIA_OIL_INFRA): first 8 lines each.
- `domain/europe-rearm/LADDER.md`: 1–132, lines cut at 450 chars (long blockquote lines truncated).
- `domain/europe-rearm/README.md`: 1–30 plus a grep.
- `domain/europe-rearm/INCURSIONS.tsv`: lines 1–3 and last 2.
- `domain/energy-strikes/STRIKES.tsv`, `SUMMARY.md`, and all `domain/sources/*.md`: first 3 lines.
- `archive/` (8 files): first 4 lines each.

**Targeted greps and extracts outside my cluster (for currency checks only):**
- KB rows 232, 233, 440, 441, 445, 447–451 (partial cells).
- FLOW.tsv: all row heads; rows 8 and 10 extracts.
- VX.tsv: TWN-01, TRADE-01, SULPHUR-01, EURMIL-01 (partial).
- CATALYSTS.tsv grep; STATUS/SCRATCH/NEXUS_BRIEF greps; HAWK CLAUDE.md grep.
- `AGENTS/_NETWORK.md` HAWK lines; DAEDALUS FLEET_MAP HAWK row.
- `git log` for every thesis/ and research/ file and the domain synthesis docs; `git show --name-only 0d0a91709`; inbox listing.

**Not read:**
- **`domain/sources/` raw items, listed and skipped (~8.1 MB):**
  - `UNCTAD_HORMUZ_DISRUPTIONS_MAR10.pdf` (4.2 MB)
  - `2026-09-08_next-steps-1-3/aug26_base.xlsx` (1.1 MB)
  - `2026-09-08_batch2/` (navy149.pdf, navy153.pdf, qatar-*.html, canada-*.html, cbsa*.html, gazette-index.html, manifest.json, verify_draft.py)
  - `2026-09-08_canada_*` (txt, html, `source-lines.json` 206 KB)
  - `2026-09-08_verify_canada.py`
  - `next-steps-1-3/` (fr pdf, navy csv, steo_extract.py, taipower csv, usitc json, manifest)
  - three images (CRU, FORCE_MAJEURE_MAP, MAERSK)
  - STATUS archives (Feb–Jul)
  - the 9/08 "before" snapshots
- **Bodies not read:** archive/ bodies beyond line 4; the September research bodies beyond their heads; FLOW, KB and VX rows beyond the extracts above.
- **No scripts run** apart from read-only `wc`, `awk`, `grep`, `git log/show`, `date`.
