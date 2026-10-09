# OSPREY STATUS
**Last Updated:** 2026-10-09 (Fri) 13:04 ET (from `date`): PROME spawn (prome-75), DOCKET L624 fix pass 2 only; item 5 below. The ~10:45 ET header that follows is unchanged otherwise. PROME Tier-1 due-row wake (DOCKET L623, prome-75): C2 kill evaluation, C3 RIO attribution, whole-inbox drain 7/7. **Scores 5 / ⚪1 KILLED (C2, dormant-armed; last live mark 5) / 3. Band ~30% [EST] UNCHANGED.** Prior update 2026-10-08.
**Evidence:**
- `domain/energy-strikes/C2_KILL_EVAL_2026-10-09.md` (the verdict record) and KB-OSPREY-177…181.
- `STRIKES.tsv`: +6 rows and 2 updated in place. **The swept-complete mark is ADVANCED 9/20 → 10/07 on a BOUNDED pass** (limits listed in the ledger header).
- The 10/8 block below is kept as written.

## ACTIVE — 2026-10-09 (C2 KILLED · C3 clock reset · no band or threshold moved)

1. ⚪ **CHANNEL 2 (crude-export terminals) KILLED 2026-10-09 on its letter.** Both limbs are met.
   - **Limb 1, 30/30:** the newest in-geography crude-terminal / pipeline / oil-port row is still `RU-20260909-NOVOROSSIYSK-OIL-TERMINAL`. A mechanism-level sweep of 9/30→10/9 found nothing newer: feed, a Reuters factbox, name-free EN+RU queries and nine per-port queries.
   - **Limb 2:** Bloomberg 4-wk **3.54 / 3.53 / 3.71 / 3.76** (to 9/13, 9/20, 9/27, 10/4), all ≥ 3.5. **No shut-in signal**:
     - The week-to-9/20 Novorossiysk departure halt was **offtake deterrence** (shipowner caution; Novorab/Kapital Rossii: Sheskharis ~650 kb/d over 1–20 Sep).
     - It never reached tank-tops or upstream cuts, and exports rose to their highest since early August.
   - **The mark goes 5 → ⚪1, dormant-armed.** It re-arms at 5 on the next in-geography C2-class row.
   - ⚠️ **Limits:**
     - The 10/4 print is read from a search summary (paywall), B3.
     - Novorossiysk's **port-level** restart is inferred, not read.
     - Palaemon 5–11 Oct is unpublished.
     - **Any missed in-geography event after 9/9 voids the kill as of its date.**
   - This is the self-adverse direction: a dead channel cuts against this desk. KB-177.
2. 🔄 **CHANNEL 3: the AFRAMAX RIO attribution is SETTLED, so the clock RESETS and there is no kill.**
   - Zelensky's post of 10/7 says *"There is also a response in the Black Sea"*, illustrated with **video of the burning tanker off Sochi** (Liga 10/7 11:26; Kyiv Post; Georgia Today).
   - **No Ukrainian denial for RIO.** His 10/6 *"no operations in that part"* concerns the Bulgaria-EEZ attack.
   - This is graded at the ARMADA LEADER standard (claim + independent event record), not by inference.
   - **New anchor 10/6: 3/21 on 10/9; the earliest limb-1 kill is 10/27.** Direction: anchor 9/12 → 10/6 and elapsed 27/21 → 3/21 make C3 HARDER to kill, which favours this desk. That is why a claim was required.
   - Limb 2 (war-risk repricing) is HAWK's call, and a packet has gone to HAWK. Bulgaria's Defence Ministry, 10/9: no drone debris on ABLE.
   - The SBU LOUISE 1/BANDA lead is a 7/16 strike: CLOSED. KB-178.
3. 🔥 **The land campaign keeps running, all of it out of C2's geography:**
   - **Volgograd halt VERIFIED** at a Reuters factbox (*"halted crude oil processing completely on October 2"*, two industry sources), so the vintage trap is cleared.
   - **Omsk 10/8** (GS-confirmed; the governor says only that "an industrial zone" was hit; date trap: Reuters' "halts processing" story is the JULY strike).
   - **Ukhta 10/9** (Zelensky-confirmed): the **newest C1 anchor, 0/30**.
   - **Midstream:** Volodarskaya products LPDS (Moscow region) 10/6, plus Samara LPDS 10/2 and 10/7. That is the C2 companion watch; it resets nothing.
   - **L544 (10/15):** the 14-day leg is unmet. KB-179.
4. **Data-decree goods list (~10/8): SEARCH-NOT-FOUND.** Only the 9/28 decree's list of information categories exists. Bloomberg still printed on 10/6, so the export instrument is alive. **OSP-06:** 3.76 to 10/4 does not fail it, and search day 2 is done. KB-180. ⚠️ **3.76 is B3/UNCONFIRMED:** BRENT could not read it at text either. The nearest searchable hit is 3.74 to 12 Oct **2025**, a date trap. Limb 2 does not rest on it. KB-182.
5. **Strike feed (DOCKET L624): ⛔ `strike_feed.py` WITHHELD from operational use until READ 3 is clean.**
   - **10/9 PM:** READ 2 found STILL UNRESOLVED (1 ❌: a real newest with a bad date was dropped with no trace). **Fix pass 2 `4ea2b4539`** (acceptance first, `88d715d03`) names any possibly-newer link and fails it closed (`BULLETIN_NEWEST_UNSURE`, NOT_READ). Tests: 32 OK fixed, 14 F on `04d8f06be`.
   - Not independently verified. This was the second correction pass, so the two-correction stop has tripped. The C2 feed leg stays UNVERIFIED.
   - The 10/9 run's bulletin row is present, but that run cannot test the patch (read 1).
   - RIO was matched on the generic token `telegram`.
   - **`MATCHES_2026-09-15/16/29.tsv` were RECOVERED** (untracked on this host) and committed: 6/6 precise. The 9/16 Saratov half was absorbed into Syzran. KB-181.
6. **§5 30-day EXIT RULES re-read DONE** (it was due 10/8):
   - C1 0/30 · C2 FIRED · C3 3/21.
   - §2 theater clock not running · §3 not known fired (BRENT's call).
   - No new rail defect. Record §4.
7. **Inbox 7/7 drained**: 6 at the 09:56 ET census (2 top-level, 4 in the WALTER lane) plus SIG-W-20261009-006, which arrived at 10:06 (info only: Ukhta graded claim-only by WALTER, Zelensky-confirmed by Ukrinform). The re-census reads 0 / 0. Logged in `board_log.tsv`:
   - **DAEDALUS sweep packet:** item 1 is DONE (the `CLAUDE.md` EXIT RULES header now names the 10/9 re-read and the 9/19, 9/24 and 9/29 amendments). Item 2 is DONE (closeout step 9 names `measure.py` for the line and byte check).
   - **WALTER R3 alternates:**
     - ADOPT `Ust-Luga drone`, `Ust-Luga strike` and `Caspian Pipeline Consortium` (resumption does not un-fire GATE-OSPREY-001 (b)).
     - DECLINE `Tuapse port` (the `port` substring collides).
     - DECLINE `Russia lift diesel export ban`; ADOPT the alternate `Russia lifts diesel export ban`. ⚠️ It does not see "lets … lapse" wording; the instrument is YURI's.
     - PROME lands these.
   - **SIG-W-20261008-033 (WQ-399):** the receipt line in `CLAUDE.md` boot 5a-3 is rewritten to the new form. No receipt is owed (corrections check rc 0).
   - **SIG-W-20261008-023 / -048:** Omsk and Salavat are rowed. The diesel-ban linkage is inference, so there is no instrument change.
   - **SIG-W-20261008-039:** the Kyiv grid strike is Russia-on-Ukraine and out of ledger scope (KB-176). The Miami talks are context: "ceasefire" is a proposal word.

## ACTIVE — 2026-10-08 (no mark moved)

1. ✅ **L309 strike-feed evaluation DONE.** Recall PASS by the letter: the 9/8 run found Kstovo 8/26, which the certified sweep had missed. But the 9/19 independent backfill found ARMADA LEADER 9/12, which the feed missed. **By class (rows 9/8–9/23): refineries 9/9, vessels 2/9, gas plants 0/2, all 14/27.** Precision on audited runs 9/11, 0 silent deletions; the 9/15 and 9/29 runs cannot be audited. ⇒ **RETAINED for land, NOT for Channel 3.** Three tool repairs: MATCHES re-committed (a 9/15 gitignore line had reversed the 9/10 fix), militarnyi URL fixed, Palaemon bulletin no longer dropped. KB-172.
2. 🔥 **Refinery campaign RESUMED after the 9/27–29 depot pause:** Volgograd 10/2, Samara Transneft LPDS 10/2 (crude-transit node; 10/7 new fire), Salavat 10/8 (newest C1 anchor). ⚠️ **The Volgograd HALT (WALTER relay of Reuters 10/6) is NOT verified at primary** and carries a vintage-trap risk. Zelensky 10/3 said strikes would be stepped up. ⇒ **L544 (C1 5→4, 10/15): the 14-day no-refinery-row leg cannot be met on 10/15** (a fact, not a grade). KB-174.
3. ⚠️ **C3: a QUALIFYING CANDIDATE, AFRAMAX RIO 10/6.** A crude Aframax on Ukraine's shadow-fleet list was hit by "unmanned boats" (Russian Transport Ministry) ~11 km off Sochi. Hull and geography are met; the **attacker is INFERRED, not claimed.** At the ledger C3 = 26/21 from ARMADA LEADER 9/12 (limb-1 date 10/3 passed). If RIO qualifies: 2/21 and limb-1 moves to 10/27. **Palaemon 21 Sep–4 Oct read: no Ukraine-side tanker strike, no Russian port attack.** A 10/6 sinking inside Bulgaria's EEZ (Russia-attributed) plus a Bulgarian PM insurance warning points toward limb-2 repricing (HAWK's grade). **No C3 kill is writable.** KB-175.
4. **C2: 29/30 from Novorossiysk 9/9; limb-1 date TOMORROW 10/9.** No in-geography event found 9/21–10/8 (Palaemon + feed). Bloomberg 4-wk to 9/27 = **3.71** (BRENT relay), so limb 2's number leg reads met, but the **shut-in leg is still open.** ⛔ **A C2 kill needs a fresh mechanism-level sweep (§1), which this session did NOT run.** KB-173.
5. GATE-OSPREY-001: **no inbox item changes CPC SPM / Tengiz state** (Samara is not the CPC route). Diesel ban EXTENDED to 10/31 (BRENT, Interfax 9/30; not verified at pravo.gov.ru). Russia-on-Ukraine grid campaign NOT added to the ledger (scope; KB-176).

## ACTIVE — decision-relevant changes (2026-09-29)

1. ✅ **C1 UPGRADED 4→5 (WQ-276 shape iii, Will 9/24 14:59 ET).** Carried on the row permanently: (a) trigger met on END-AUGUST S&P/CERA only (~50% offline, pub 9/3) — **September independent aggregate still SEARCH-NOT-FOUND (re-checked 9/29)**; (b) the Moscow read weakens the export-ban mechanism, not the trigger arithmetic; (c) **NEW:** the 9/28 data decree (item 3) may starve the instrument the downgrade reads. **5→4 successor registered** (CLAUDE.md §1b): independent aggregate <40% on 2 prints + 14d no refinery row; 60-day blackout ⇒ flag UNREACHABLE. **First evaluation 10/15.** KB-159.
2. 🔥 **REFINERY HALTS KEPT COMING THROUGH 9/26, THEN STOPPED.** Verified halts: **Novoshakhtinsk 9/25** (governor, ~100 kb/d nameplate per Reuters; outlets range ~3.3-7.5 Mt/yr) · **Perm/Lukoil 9/25** (Reuters industry sources; 2024 run ~252 kb/d, Russia's 7th-largest). **Ilsky 9/26** struck (GS), three crude units + tank farm per imagery; **halt is belligerent-only (Fire Point, the drone maker)**. Plant tally: 8 September halts by 9/25 — a COUNT, not capacity. **Nothing refinery-class found 9/27-9/29**; 9/28 hit four Krasnodar depots. ⛔ All CAPACITY, not barrels. KB-158.
3. ⚠️ **PUTIN DECREE 9/28 RESTRICTS PUBLICATION of refinery-by-refinery runs, export volumes/prices/buyers/routes/terminals/vessels and customs data.** Government lists covered products within 10 days (~10/8). Number "686" unverified. Instrument risk for runs-based reads and the C1 downgrade; tanker-tracking (Bloomberg/Kpler) less exposed. Does NOT arm OSP-06 VOID by itself. KB-160.
4. 🕊️ **ENERGY-TRUCE TALK — NOT AGREED.** Trump 9/27: *"You gotta take it easy on the refineries"*, says Zelensky replied *"we'll probably do that"* (Trump's account only). Kyiv: stops only if Russia agrees an energy truce; nothing committed. Rubio 9/23: both sides "interested" in a limited grain/energy ceasefire, "won't be easy"; Lavrov 9/23: no pause during talks; Peskov 9/15 price: sanctions relief + tanker-safety guarantees. Declaratory ≠ physical — no kill leg touched. **Watch: whether depot-not-refinery persists past 3 days.** KB-161.
5. **C2: clock 20/30 from Novorossiysk 9/9, limb-1 kill date 10/9 (read at ledger 9/29).** No in-geography port/terminal/pipeline event found 9/21-9/29. ⛔ **Limb 2 blocker still open:** the Novorossiysk departure halt (week to 9/20) has no established cause (BRENT 9/25: holds nothing). Kommersant 9/18 attributes early-September losses (~-40%) to **tanker owners avoiding the port for safety** — offtake deterrence (FLOW-OSPREY-03), which may be a "shut-in signal." Bloomberg 4-wk to 9/27 not yet out. KB-165.
6. **C3: 17/21 from ARMADA LEADER 9/12 (at ledger), limb-1 date 10/3; no kill writable before 10/9.** No qualifying Ukraine-side tanker strike found 9/21-9/29 — **NOT certified** (Palaemon 21-27 unpublished). Open lead: Zelensky 9/28 *"a target was hit in the Black Sea"*, unidentified. Platts $2.9/bbl AWRP (9/21) is snippet-only — NOT adopted, routed to HAWK (if real, earliest both-clear → 10/12, harder to kill). KB-166/167.
7. **Sanctions/policy:** US H.R. 5334 (Graham Act) signed 9/18 — 100% secondary-tariff authority on top buyers, implement by ~10/18, broad waivers, nothing imposed yet; OFAC quiet 9/19-9/29 (KB-164). Russian producer diesel-ban text in force **lapses 9/30**; extension to 10/31 reported, no signed resolution found (KB-162). CREA: false-flag shadow ships 101→45; Russian-flag registry 280→382 (KB-163).
8. 🔎 **AFTERNOON SWEEPS (Will-requested, 9/29):** ① **Overnight 28→29 + 9/29 daytime: no new energy strike; no refinery restarts** (Moscow, Kuibyshev, Novoshakhtinsk, Perm, Ilsky). Refinery-class quiet = 3 days. Zelensky's 9/28 Black Sea target = probably bulk carrier **AROYAT** 9/27 (not a tanker — no C3 reset). KB-171. ② **Oil fields/pipelines/pump stations 9/1-9/29: none confirmed — INCOMPLETE** (session search cap hit). ⛔ **Found a CLASS HOLE: ~12 pump-station/midstream strikes Apr-Jul 2026 are NOT on the ledger** (only 2 pump rows for 2026). Backfill = **OWED-51**. KB-169. ③ IEA Sept OMR (relay) cut Russian crude 125 kb/d to 8.7 M b/d on weaker refining — strikes reach production via refineries (OWED-49 part-answer, KB-170).

## THREE-CHANNEL DASHBOARD
| Channel | Score | Mark state | Current evidence / upgrade test | Clock / downgrade test |
|---|---:|---|---|---|
| Refineries/products | **5** | **UPGRADED 9/29 on Will's word (WQ-276)**. Caveats: (a) end-Aug data only, (b) the Moscow read weakens the ban mechanism, (c) the 9/28 data decree. | Running: Volgograd 10/2 (**halt VERIFIED**, Reuters factbox), Omsk 10/8, Salavat 10/8, Ukhta 10/9. 9/20–9/26: Moscow, Kuibyshev, Novoshakhtinsk and Perm HALTED; Ilsky struck. ⛔ **CAPACITY, NOT BARRELS.** September independent aggregate SEARCH-NOT-FOUND (not re-searched 10/9). | **0/30 from Ukhta 10/9.** **5→4 (§1b, L544, first eval 10/15):** needs the aggregate <40% on two prints AND 14 days with no refinery row; the 14-day leg is unmet. A 60-day blackout ⇒ UNREACHABLE flag. |
| Crude-export terminals | **⚪1 KILLED 10/9** (last live 5) | **DORMANT-ARMED.** Re-arms at 5 on the next in-geography crude-terminal, pipeline or oil-port row. | Limb 1 30/30 (Novorossiysk 9/9; bounded mechanism sweep 9/30→10/9). Limb 2: Bloomberg 4-wk 3.53–3.76 through the window (3.76 to 10/4, B3 search summary); no shut-in signal (the 9/20 halt was offtake deterrence and reversed). KB-177 · `C2_KILL_EVAL_2026-10-09.md`. | ⚠️ **Void-on-backfill:** a missed in-geography event dated after 9/9 voids the kill as of its date. Port-level Novorossiysk restart is inferred, not read. Palaemon 5–11 Oct is unpublished. |
| Shadow-fleet tankers | **3** | HELD-ON-EVIDENCE | Letter (9/19): merchant tanker, Ukraine-side, in geography. **AFRAMAX RIO 10/6 QUALIFIES** (Zelensky's 10/7 claim with video; no denial). Russia-attacked hulls are excluded: Odesa, Bulgaria EEZ 10/6, cargo 10/4–5. | **3/21 from `RU-20261006-AFRAMAX-RIO-SOCHI`; earliest limb-1 kill 10/27.** Limb 2 (repricing) is HAWK's grade; the Bulgaria-EEZ sinking points toward repricing. |

**⛔ C2 COMPANION WATCH (out of geography, resets nothing):**
- Caspian: `RU-20260910-MAKHACHKALA` · `RU-20260919-KASPIYSK`.
- Inland midstream, **live in October:** `RU-20261002-SAMARA-LPDS-PROSVET` (+10/7) · `RU-20261006-VOLODARSKAYA-LPDS` (products).
- Depots carry no channel clock.

**Theater clock:** NOT RUNNING. One of three channels is killed (C2, 10/9). Under §2 sequencing the 60 days start only when the LAST of the three is killed, and C1 and C3 are live. Truce talk is declaratory. The downgrade rule is in force; upgrades are Will-gated.

## Current sourced aggregates and limits
- **Refining band 25–35% [EST], ~30% (KB-029), UNCHANGED** — July 3.6 / August 3.8 M bpd runs anchors. Runs decline is a **proxy**, not measured damaged capacity. Will withdrew the ~33% re-centre 9/8; not reactivated.
- ⛔ **NO facility figure has an authenticated pre-strike throughput** (Kirishi, TANECO, Syzran+Saratov ~290 kb/d, Yaroslavl, Ryazan, Moscow) — **all CAPACITY, none BARRELS LOST** (OWED-36). ⚠️ **But "no independent aggregate" was too broad (CATO F2):** S&P/CERA ~half offline (9/3), IIR 3.805 M bpd Aug outages (9/8) — reconcile vs the ~30% runs band, **OWED-50 / KB-145**.
- **Crude export:** Bloomberg **3.54 M bpd 4-wk to 9/13** (KB-114) — ⛔ but same source says diversion *"not enough to maintain production"*; **output 8.72 M bpd, 9th straight drop (KB-144, OWED-49)**. Storage/Urals/prices/cracks **BRENT-owned**. OWED-33 unanswered.
- **War risk:** data clock **2026-09-18** (structural, not a percentage). ⚠️ May be ~43 days since the last true rate print — ACTIVE 4. **Do not infer flat premia.**
- **Feed / sweep (9/29):** `strike_feed.py` 23 rows, 21 NONE all dispositioned in the feed file (gitignored, OWED-45); militarnyi RSS EMPTY_FEED (3rd run) — **but the WEBSITE read fine in the PM sweep**: read the site, not the feed (OWED-34 residual). Day-by-day name-free sweep 9/21→9/29 + maritime + policy sweeps run. **Mark stays 9/20** — Palaemon 21-27 unpublished; Reuters/Bloomberg read only via relays. Vintage traps rejected: six 2025 stories re-served as current (listed in the ledger header).

## Predictions
**OSP-06 OPEN, 45%, deadline 10/15.** Bloomberg 4-wk 3.71 to 9/27 does not fail it, but **the final week printed 3.99**, so risk is RISING. 10/8 search for the 4-wk to 10/4: SEARCH-NOT-FOUND (paywall; unreadable is not dark). VOID not armed. Dated search obligation 10/8–15: day 1 done. Other rows resolved.

## OWED REGISTER — every live obligation, dated
*(READ_CAP rule 18 census — **9/15 session: 36 named obligations in → 35 carried + 1 CLOSED BY NAME (OWED-1, on a negative) + 3 new (37/38/39) = 38, 0 dropped.** L308 discharged out of the dated table. This table IS the backlog.)* *(Prior, third rotation: 26 in → 26 carried or closed by name + 1 new (36), 0 dropped.)*

**⏱ DATED — WHAT LANDS WHEN:**

| Date | Item | Owner / state |
|---|---|---|
| **9/15** | **OWED-30 + OWED-32 write-ups** | ✅ **OWED-32 CLOSED — subsumed by the 9/19 self-ruling** (hull-class + attacker halves written; geography unchanged as Will ruled it 9/8). ❌ **OWED-30 write-up still owed** (buyer-pullback: source/observation · counterexample · C2 overlap). |
| **9/15** | **OWED-34** — strike-feed residuals ⑤/⑥/(c) | ❌ **Still owed, and 9/19 adds a FOURTH: a FALSE MATCH suppresses a candidate silently** (OWED-45). |
| **9/21** | **DOCKET L432** — Russian mobilisation window | ✅ **CONSUMER READ 9/29:** no mobilisation declared; Putin 9/29 decree +15,500 authorised to 1,550,500 (KB-168). No manpower step-change bearing on the strike campaign. HAWK owns. |
| **10/1** | **Swedish Club amended war-risk terms take effect** | Consumer read. HAWK's 9/19 reply rejected only **JWLA-035's geography** as price; this **Swedish Club** material is **ungraded** (pending). Limb 2 UNDETERMINED. |
| **9/25–9/27** | **+5d re-reads** | ⚠️ **PARTIAL 9/29:** Moscow — no restart AND no still-down report found (barrels open, OWED-43). Kuibyshev — Reuters halt; **conflict:** Reuters says both CDUs, imagery shows tanks/pumps/feed lines only. Ufa 9/23 — stays UNCONFIRMED (TPP smoke possible). UNPZ date may be 9/21 not 9/22 (outlets split) — anchors nothing now. |
| **✅ 10/8** | **Palaemon 21-27 Sep + 28 Sep-4 Oct READ** | No Ukraine-side tanker strike; no Russian port/terminal attack; one unnamed "possibly tanker" 9/30 (type unestablished, rowed). C3 vessel coverage 9/21→10/4 is instrument-read. |
| **✅ 10/9** | **Channel-3 RIO attribution SETTLED** | RIO qualifies (Zelensky 10/7 claim by video). **New anchor 10/6: 3/21; the earliest limb-1 kill is 10/27.** KB-178. |
| **✅ 10/9** | **Channel-2 kill evaluation DONE: KILLED** | Both limbs met (30/30; 4-wk ≥ 3.5; no shut-in). Dormant-armed. Void-on-backfill. KB-177, `C2_KILL_EVAL_2026-10-09.md`. |
| **✅ 10/8** | **L309 strike-feed evaluation DONE** | See ACTIVE 1 / KB-172 / the L309 record. |
| **✅ 9/30** | **Diesel-ban text: EXTENDED to 10/31** | Per BRENT (Interfax 9/30 signed resolution); NOT verified at pravo.gov.ru. 10/2 "partial lift" headline routed to YURI (SIG-W-20261008-010). |
| **✅ 10/8** | **R3 WATCH_FOR verdicts answered by name** | `PROME/inbox/2026-10-08_from-OSPREY_R3-watch-for-adoption.md` — 10 to land + 5 UNTESTED. |
| **~10/8 → OPEN** | **Data decree goods list** (due 10 days from 9/28) | **SEARCH-NOT-FOUND 10/9.** Only the information-category list exists (TASS 9/28). Re-check at the 10/15 L544 evaluation; it decides whether the C1 downgrade stays reachable (KB-160/180). |
| **10/15** | **OSP-06 deadline** | OPEN 45%. Dated search obligation 10/8–15. |
| **10/15** | **C1 5→4 successor — first dated evaluation** (WQ-276; CLAUDE.md §1b; **PROME DOCKET L544**, caveats a/b/c travel) | Mine. Any independent aggregate <40%? Any refinery row in prior 14d? Blackout count from 9/3. |
| **~10/18** | **H.R. 5334 implementation deadline** (30 days from 9/18) | Consumer read → BRENT/HAWK. Waivers are the observable (KB-164). |

**CLOSED, BY NAME — ROTATED 2026-09-18 → `archive/STATUS_ROTATED_2026-09-18.md` §B** (verbatim; nothing dropped — the closed half of the census lives there, the live half is the table below).

| # | Owed | Since | State 2026-09-11 |
|---|---|---|---|
| 1 | Sheskharis fifth-episode watch | 8/15 | **ARMED, not fired.** An oil terminal at Novorossiysk was set ablaze 9/8-9 — terminal not named, no loading statement (KB-101). Fifth episode IF it is Sheskharis. **First check of the next full session.** |
| 8 | Black Sea AWRP watch | 7/31 | ✅ **DISCHARGED 2026-09-19 — full 14-outlet canvass RUN, ~35 fetches; data clock 8/21 → 9/18.** ⛔ **No numeric print exists 8/22→9/19** (VERIFIED open web; **NOT ESTABLISHED** paywalled — **Platts 403, never reached**). **Two dated war-risk TERMS/TERRITORY changes instead** (Swedish Club Circular 452/2026, 9/18; JWC `JWLA-035`). ⛔ HAWK's 9/19 reply rejects **JWLA-035's geographic change** as premium-repricing evidence and leaves limb 2 UNDETERMINED; the **Swedish Club** material is **ungraded** in the still-pending request. **OSPREY withdraws its own claim that these items establish repricing.** ⛔ **Three defects found in my OWN baseline** → ACTIVE 4; the 1.5–2.5% reconciliation is **OWED-48**. |
| 31 | SIREN 9/3 — cargo state + attribution | 9/8 | **OPEN after four passes; ✅ NO LONGER CLOCK-CRITICAL** (ARMADA LEADER 9/12 is newer and unambiguous). Resolved: IMO **9405423**, Suezmax, ex-SERENEA, Marbella/Eurotankers Piraeus; **strike date 9/03 VERIFIED** (Palaemon); accommodation hit, no fire or spill. ⛔ **STILL NOT ESTABLISHED: cargo, charterer, shadow-fleet status. No OFAC/EU/UK designation found** — only **Ukraine's GUR register, a TARGETING-JUSTIFICATION list, not a Western sanctions listing**; treating it as equivalent would be the relay-to-print upgrade this desk forbids. ⚠️ Greek-managed, Liberia-flagged, mainstream operator — atypical for shadow-fleet tonnage. ★ **Hence the letter says *merchant tanker hull*, not *shadow-fleet hull*: hull class is OBSERVABLE, shadow-fleet status is a CONTESTED DESIGNATION.** |
| 32 | §1 Channel-3 geography qualifier | 9/8 | ✅ **SUBSUMED AND CLOSED by the 2026-09-19 self-ruling** — the hull-class and attacker-direction halves are now written; the geography half stands unchanged as Will ruled it 9/8. Scope comparison lives in `OWED39_DISPOSITION_2026-09-19.md` §1. |
| 33 · 39 | ✅ CLOSED rows (Urals figure, BRENT no-data 9/21 · Channel-2 drawing, Will ruled B 9/19) — VERBATIM → `archive/STATUS_ROTATED_2026-09-29.md` Part 3 | — | CLOSED BY NAME; census unchanged. |
| 13 · 14 · 17 · 18 · 19 · 24 · 30 · 34 · 35 · 36 | **TEN CARRIED ROWS — VERBATIM → `archive/STATUS_ROTATED_2026-09-19.md` § "OWED rows 13–36"** (READ_CAP rule 5; **nothing closed, census unchanged, only bytes**) | various | **ALL STILL OPEN.** 13 Transneft cadence · 14 `HAW-19` LEG A clause · 17 decree unverified at pravo.gov.ru · 18 Druzhba thin · 19 feed build closed, **10/6 acceptance test** live · 24 joint auto-memory, HAWK deferred · 30 buyer-pullback watch (⛔ withdrawals ≠ buyers) · 34 feed residuals ⑤⑥(c) — **OWED-45 adds a fourth** · 35 WQ-196…199 unruled (⛔ silence never authorises a threshold) · **36 the live one — does a facility capacity figure touch the band? Will-gated upward; ⭐ this week made it SHARPER: Kirishi, TANECO, Syzran and Yaroslavl all produced unit-level figures and NOT ONE has an authenticated pre-strike throughput.** |

| **40** | September public-source gaps — ROTATED VERBATIM → archive | 9/16 | OPEN: producer-ban decree unverified · Bloomberg 8/30+9/6 prints missing · unit restarts + pre-strike throughput unverified at every facility (blocks every incremental-barrels read). |
| **41** | Ledger completeness (founding lesson recurred ×2) — ROTATED VERBATIM → archive | 9/18 | WORKED, NOT CLOSED: swept-complete mark stays 9/16; pre-9/01 window suspect as a class. Remaining: Volgograd 9/11 not established; 9/13 Ufa declined (vintage); Baltic Exchange w/e 9/18 not obtained. |
| **42** | **Refining-band basis pair: 3.6 vs 3.91 for the SAME month** | **9/18 (NEW)** | **OPEN, flagged not resolved — no number moved.** The canonical band's July anchor is **3.6 M bpd (EA Analytics)**; Bloomberg's July figure is **3.91 M bpd** (*"lowest since 2005"*, pub 7/13). **Two instruments, one month, a 0.31 M bpd gap** that propagates straight into a ~30% band derived from runs. Publication-date vs reference-period vintage is the likely cause and is **not established**. This is HAWK's basis-pair audit territory; do NOT re-centre anything on either figure until the pair is reconciled (the 9/8 precedent: a re-centre is re-derived on the newest print before it executes). KB-131. |
| **43–48** | **SIX 9/19-batch OWED rows — ROTATED VERBATIM → `archive/STATUS_ROTATED_2026-09-19.md` (still OPEN; census unchanged)** | 9/19 | **43** +5d re-read on same-day refinery rows · **44** Ust-Luga 9/1 asset = Novatek condensate? (anchors C2 drawing 4; re-classification moves clock TOWARD kill) · **45** feed dispositions + MATCHES gitignored; one false Sochi↔Komysh match (precision-leg datum) · **46** does a condensate/products-chain plant reset C1? (routed, test-4 fails) · **47** C3 clock may measure REPORTING density not strike density (Brovdi 285-vessel claim; not adopted) · **48** two AWRP sets 1% vs 1.5–2.5%, both relay-only (Platts route owed). |
| **49** | **Production/export inference — carry both, distinguish national vs Moscow** | **9/20 (NEW, CATO F1)** | **OPEN.** Bloomberg (9/15) verified at primary: exports 3.54 recovered BUT diversion *"not enough to maintain production"*; output 8.72 M bpd, 9th straight drop (OPEC). ⛔ My *"we are not seeing production loss"* withdrawn. Owed: how much of the decline is strike-caused vs OPEC+/field decline (NOT established), and Moscow-incremental vs national. KB-144. |
| **50** | **Independent Sept aggregate reconciliation on consistent definitions** | **9/20 (NEW, CATO F2)** | **OPEN.** S&P/CERA (9/3) ~half capacity offline end-Aug; IIR (9/8) 3.805 M bpd Aug outages (44 units/17 refineries, incl condensate). Put beside the ~30% runs band with period/denominator/cause/eligibility; resolve or retain the disagreement with the 3.6-vs-3.91 basis pair (OWED-42) BEFORE any band move. ⚠️ Not re-read by me (403). KB-145. |
| **51** | **MIDSTREAM backfill — ~12 pump-station strikes Apr-Jul 2026 absent from STRIKES.tsv** | **9/29 (NEW)** | **OPEN.** ASTRA-reported, dates unverified; + Novokuibyshevsk refinery 8/22. Also re-run the unfinished Sept upstream queries (RU-language weekly, Caspian platforms, CPC pumps, BTS, Druzhba HU/SK). Session search cap blocked it 9/29. KB-169. |

## Cross-Agent Implications
**2026-09-29 packets (carve-out ①):** **PROME** ×2 — WQ-276 executed (C1 4→5, successor row = CLAUDE.md §1b "Channel 1, 5→4", first eval 10/15, KB-159) · WQ-295 cadence `WEEKLY` + WATCH_FOR terms (cc WALTER). **BRENT** — new halts Novoshakhtinsk/Perm/Ilsky (capacity, not barrels); 9/28 data decree (instrument risk to runs reads); truce talk; Novorossiysk: Kommersant safety-avoidance as the candidate halt cause — ask: Bloomberg 4-wk to 9/27 when printed. **HAWK** — Platts $2.9/bbl 9/21 AWRP lead (snippet-only; grade it — moves C3 earliest both-clear 10/9 → 10/12 if real); CREA false-flag/reflagging figures; H.R. 5334.
Prior cross-agent blocks (9/19-9/24) rotated VERBATIM → `archive/STATUS_ROTATED_2026-09-29.md` Part 2. Delivery is on commit; receiver integration UNKNOWN. I do not edit `GATES.tsv`.

## BOTTOM LINE
**Channel 2 is dead on its own test, and Channel 3 just got a fresh clock.**
- **Channel 2 (crude-export terminals): KILLED 10/9.**
  - No Russian Black Sea, Azov or Baltic oil port or terminal has been hit since Novorossiysk on 9/9.
  - Seaborne crude exports held 3.5–3.76 M bpd on Bloomberg's 4-week average, with no well shut-ins.
  - It comes back at 5 the moment a port is hit again.
- **Channel 3 (shadow-fleet tankers): not killable before 10/27.** Zelensky effectively claimed the 10/6 AFRAMAX RIO strike off Sochi by posting its video.
- **Refineries keep getting hit:** Volgograd (halt now verified), Omsk, Salavat, Ukhta. C1 stays 5.

**Watch:**
- any in-geography port strike (it re-arms C2, and a missed one dated after 9/9 voids the kill);
- the Bloomberg 4-wk to 10/11 (OSP-06 needs < 3.9 through 10/15; 3.76 now);
- HAWK's limb-2 repricing grade;
- the 10/15 L544 evaluation.
