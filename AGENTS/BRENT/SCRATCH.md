# BRENT SCRATCH — Sun Sep 6, 2026 ~11:xx ET

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⛔ READ FIRST — THE THREE THINGS THAT CHANGE HOW YOU WORK TOMORROW
>
> **① BASIS DISCIPLINE — STILL NOT SOLVED, AND TODAY IT PRODUCED A 40¢ DISAGREEMENT WITH MYSELF.** Every Brent figure NAMES **(a) the CONTRACT** and **(b) the BASIS.** ⚠️ **NEW, OPEN, DO NOT SILENTLY PICK ONE: `BZX26`'s 2026-09-02 close reads `95.23` from the 9/2 post-close pull and `95.63` from the 9/6 re-pull — same source, same named contract, same date.** Every 9/1–9/4 figure on my surfaces today is from the **single 9/6 re-pull** so the ladders are internally like-for-like; the 9/2-vintage rungs are flagged as a **BASIS BREAK, not a market move.** **Canonical `BZX26` closes ON THE 9/6 BASIS: 9/1 `94.65` · 9/2 `95.63` · 9/3 `95.52` · 9/4 `96.28`.** ⛔ `BZ=F` still banned for deltas — **and note the harder finding below: across a roll the % change may not be computable AT ALL.**
> **② THE BAKER HUGHES 403 IS SOLVED, AND IT WAS NEVER A HEADER PROBLEM.** `urllib` + browser UA returned **200** on `na-rig-count` AND on ten `/static-files/<uuid>` downloads; only after ~10 rapid fetches (~24 MB) did everything start 403-ing ⇒ **usage-triggered WAF.** **`HEAD` is 403 unconditionally, so the old HEAD-based picker could never have worked.** ✅ **Recipe: GET the page → collect uuids → GET (NEVER HEAD) → pick by the DATE in `content-disposition` → FETCH ONLY ONE FILE.** ⛔ **Year-stale decoy still in the list: uuid `e98bcf83` = `08-29-2025`.** **UNTESTED, close it next time: a `Range: bytes=0-0` GET may read `content-disposition` without spending the budget.**
> **③ THERE IS NO OPEC+ SUPPLY LEVER BEHIND Q4, IN EITHER DIRECTION.** The 9/6 statement held October at September's required production and said nothing beyond October. **At ~0.02 mb/d effective spare, the 8/2 `+188 kb/d` was ~9× the spare ⇒ ~90% paper, and not repeating it removes ~nothing physical.** ⇒ **Do not size anything off an OPEC+ supply narrative this quarter, and do not read the hold as a Q4 pause.** Next monthly meeting **4 Oct 2026** (row registered).

---

## ✅ WHAT THIS SESSION DID

**PROME-orchestrated Tier-1 due-row spawn (WQ-184 L0). Boot → OPEC+ grade → full inbox drain → two Friday grades → closeout. `$0` moved, no trade proposed, no threshold or gate created or moved.**

- **🔴 DOCKET L123 / CATALYSTS L8 GRADED, DAY ZERO, AT THE PRIMARY THE FROZEN LETTER NAMES.** `opec.org/pr-detail/1835613-6-september-2026.html` (urllib **200**; `press-releases.html` **403** — **enter via the ROOT page's link list**, that is the routing fix). **OUTCOME (3) DEFERRED AGAIN.** Statement decides **October only**, nothing beyond it, next meeting **4 Oct**. **Outcome (2) REFUTED for October** (+188 kb/d not repeated). ⛔ **NOT (1)** — a one-month hold is not an adopted Q4 pause. Full read → `setups/2026-09-06_opec-q4-grade.md`.
- **⚑ THE ROW'S OWN PREMISE WAS WRONG AND THE CORRECTION IS THE DURABLE PART.** *"THIS IS THE ACTUAL Q4 DECISION POINT"* — it was not and **could not have been**: the seven-country group decides **one month at a time**. **Never register a row as "the meeting where the quarter is decided."** Successor **10/4 row registered to the corrected shape.**
- **🔴 COT-FUEL-35B VINTAGE #4 (as-of 9/1) GRADED** — two byte-agreeing raw pulls: **111,019 / OI 1,921,085 / 5.7790% ⇒ JOINT NO-VERDICT, third consecutive.** Sizing stays BASE CASE.
- **✅✅ PROME's TWO GATE-BRENT-COT-35B LETTER DEFECTS CLOSED *BEFORE* THE GRADE, AS THE PACKET ASKED — NO LEVEL MOVED, NO RE-BASING.** ① **The base is `122,904.5`, not `122,904`** — an **8-observation median** = (122,319+123,490)/2; carry the .5 and all three levels reproduce to the contract. **Three blind readers were right, the levels were right, the truncated DISPLAY was the defect.** ② **Precedence stated: the deadband is decisive inside its range, `113,745` is its CENTRE and never a boundary** (`≤109,164 SPENT | 109,165–118,325 NO-VERDICT | ≥118,326 NOT-SPENT`). **n=0 grades affected** — falsified by re-running the grader after the fix and getting the identical verdict.
- **🔴 BRT-26 GRADED AT THE BAKER HUGHES PRIMARY (2nd time ever on this row): 449 oil rigs (+2), 457 NOT reached, 8 short, row stays OPEN, re-marked 58% → 85%** (window-shrink, **not** a print re-mark: 3 prints left, breach needs **+2.67/wk** vs a **−1.5/wk** trailing pace). ⚠️ **Horizontal FLAT at 535 a second straight print, Directional −1 ⇒ the headline +2 is MIX, not productive-rig growth; BRT-04's mechanism unchanged.** Recovered the full breakout the 9/4 routine could not reach.
- **📬 INBOX 10 → 0** (8 top-level + 2 WALTER). All logged to `board_log.tsv`, all archived; **moved-file count == ledger-row count == 10.** Packets written: **ZHAO** (vector-8), **HANS** (the joint read), **OSPREY** (THESIS:207 + the dead trigger limb), **PROME** (delivery memo incl. the WQ-176 owner text).
- **✅ TWO OWNER-FIXES DISCHARGED:** `CLAUDE.md:176` — the `~$5,131` 8/4 broker figure annotated as superseded (~$2,700 light vs the 9/2 `$7,829.95` pull); the line now carries the **leg set** only and points at `TRADE.md`. `thesis/THESIS.md:207` — the `~120M bbl` floating-storage carry annotated against this desk's own `~83M` (wk 8/23).
- **🔻 READ-CAP: NET DOWN ON BOTH SURFACES I TOUCHED.** STATUS **61,894 B → 59,037 B** (108.8% of cap) after rotating its 7,250 B nested prior-stamp chain to `archive/`, **on a session that added a full dated section.** NEXUS_BRIEF **234 → 138 lines** by rotating 8/28-and-earlier dated history; **CROSS-DOMAIN and CALIBRATION-divergence protected and untouched**, per the file's own rule.

## 🔴 THE FINDING THAT IS BIGGER THAN THIS SESSION

**A CORRECT SPEC CAN FAIL ITS OWN ARITHMETIC CHECK BECAUSE OF HOW A NUMBER IS DISPLAYED — and every reviewer will correctly conclude the spec is broken.** Three independent blind readers found `GATE-BRENT-COT-35B` off by one contract. **Nothing was wrong with the band.** The trailing-8wk base is an **even-n median** and therefore a **half-integer**, and it had been written down truncated. ⇒ **Any frozen level derived from an even-n median must carry the `.5`, and any spec that publishes a base must publish its MULTIPLIERS too, or it cannot be checked at all.** ★ **And the second defect is the sharper one: the published bar `≤113,745` was a MISSTATEMENT of the spec — the bar is the deadband's CENTRE, not a decision boundary. The code and every graded vintage already did the right thing; only the PROSE was wrong.** `[[finding_frozen_spec_and_the_surfaces_describing_it_drift_apart]]` — **the letter cannot drift, but the sentence describing it is what a grader actually reads.**

## ⏳ NEXT SESSION (dated, future-verifiable)

| when | what |
|---|---|
| **Tue 9/8** | 🔴 **DOCKET L198 ①② re-dated discriminator reads** · **Russia diesel producer-direct carve-out** — it never opened 9/1, **extended to 9/30** (OSPREY, adopted) — read the decree text · **matched Dated-Brent physical-vs-paper** (owed since 9/2; `RBRTE` blocked by `env_doctor FAIL`, no FRED credential — **4th straight cycle**) · **OSPREY's Russian seaborne 7th-week print (~9/8)** · 🟠 **XLE ⑦ leg 1: did XLE CLOSE ≥ $66.50?** From the **9/4 close $64.06** that is **+3.81% in ONE session** — expect **NO**; **TERRY/Will's call, not mine.** |
| **Wed 9/9** | 🔴 **SPR exchange-window test** + **WPSR wk-9/4 = the first instrumented read of Edouard** (pre-registered: >~1pp utilization fall ⇒ under-disclosed; flat-to-−1pp ⇒ the narrow read was right). **Lines 1–6 of the TRACKER block are UNVERIFIED until this print.** · 🟠 **XLE ⑦ leg 2 fires on the 9/9 OPEN unless 9/8 read YES.** |
| **Fri 9/11** | 🔴 **THE FRIDAY PAIR.** Baker Hughes ~13:00 (**use the corrected recipe in ⛔② above — GET not HEAD, ONE file**) · COT as-of **Tue 9/8** ~15:30. ⛔ **DO NOT LET THEM STACK.** Also the **WQ-176 7-day confirm deadline** (mine is already delivered). |
| **Fri 9/18** | 🔴 **USO Sep-18 150/165 spread EXPIRY.** |
| **Wed 9/30** | XLE 65C expiry · `BRT-12` and `BRT-29` both resolve · **BRT-26's window CLOSES** (last print inside it is 9/25). |
| **Sun 10/4** | 🟠 **OPEC+ seven-country monthly — the NOVEMBER decision.** Row registered today. ⚠️ **RE-PULL the spare-capacity figure at the primary before grading; do not carry `0.02` forward unchecked.** |

## 🔓 OPEN THREADS / DEBT

- 🟠 **READ-CAP — IMPROVED, NOT FIXED, AND THE REMEDY IS STILL WILL-GATED.** `board_log.tsv` **536%** · `TRADE.md` **320%** · **`STATUS.md` 108.8%** (was 114%). ⛔ **The structural rotation stays on PROME's Will-facing list — I did dated-history rotations inside my own dir only and did not self-approve a restructure.**
- 🟠 **`XLE Sep-30 65C ×2` — the character change is now a DATED decision, not an open question.** DOCKET **L252 (9/8 test) / L253 (9/9 exit)** are registered at Will's word. **My consumer read: the OPEC+ outcome does NOT change the oil read** — it cannot carry +3.81% in one session, XLE's Brent-capture is 12–38.6% by my own measurement, and **crude rose +1.7% 9/1→9/4 while XLE fell −1.1%** — the demotion thesis running live. `^OVX` −8.5% over the same four sessions also bleeds the extrinsic. **Disposition Will's, construction TERRY's. Nothing proposed.**
- 🔴 **`RBRTE` / GASREGW BLOCKED FOR A FOURTH CYCLE — `env_doctor FAIL`, no FRED credential on this box** (`PROME/MACHINE_LOCAL.md` FRED row). GASREGW cell now **20 days stale**. **Not this desk's to fix; re-flag it every session until it is.**
- ⚠️ **`INCIDENTS.tsv` — 12 ACTIVE rows past the 60d re-verify budget** (oldest RF-004 at **171d**) + 6 present-tense rows the budget does not cover. **The one real ledger debt; a research job, not a sweep.** Ust-Luga 9/1 still **NOT** logged (no facility damage, no throughput figure — LESSONS #1).
- ⚠️ **A pre-registered trigger lost a limb and nobody re-read it:** THESIS:207's *"export/floating-storage SATURATION"* limb is **DEAD** (storage draining, one-year low), leaving only the strike-pivot limb. **Annotated today. Sweep the OTHER pre-registered triggers for limbs that can no longer fire.**
- ⚠️ **`catalyst_countdown.py` fork still lacks OTTO's fired-row rule** (0 `fired` refs) — the two rows I graded today are now `✅ FIRED` in the title text only.
- **TERRY:** decoupling-vs-XLE falsifier slot NAMED BUT EMPTY on a filled position. **Top open item, unchanged, and 9/8–9/9 is when it matters.**
- **Energy HY OAS: PERMANENTLY UNMEASURED here;** LIQUID owns the systemic leg.

## 💼 POSITIONS

**NONE PROPOSED. `$0` moved. No trade action taken or recommended.** **USO 35 sh · USO Oct-16 135C ×2 · USO Sep-18 150/165 ×1 · XLE Sep-30 65C ×2.** `TRADE.md` canonical; **marks NOT refreshed this session — markets were closed, and a chain cannot be pulled** (last refresh 9/2 post-close). ⛔ **Position truth is off-repo.** **Two legs expire inside four weeks (9/18, 9/30) and both have DATED rules attached; the XLE pair fires 9/8–9/9.**

## 📬 MAIL

**Inbox 0** (10 consumed, 10 logged, 10 archived — reconciles). **Outbox clear.** **Packets sent this session: ZHAO ×1 · HANS ×1 · OSPREY ×1 · PROME ×1** (the delivery memo, carrying the OPEC grade, the COT-35B fixed letter + the WQ-176 owner text at exactly 500 B, the BRT-26 grade, the XLE ⑦ consumer read, and the read-cap figures).
