# YUR-006 grade (DOCKET L772) and 11/11 catch-up read

**Read by:** YURI, 2026-11-11 09:36 ET → (fetches 14:37–14:41Z, plain HTTP, browser User-Agent). PROME prome-2b catch-up wake on Will's word (09:24 ET, *"Lets make sure we get all our agents caught up to the live data and news."*). Claude Code subagent, Opus 5.5 (`claude-opus-5-5`). Saved: `sources/2026-11-11/` + `sources/2026-11-11/requests.tsv`.

## 1. What changed since the last session (2026-11-02), plainly

1. **Russia took control of Japan Tobacco's whole Russian business.** Two presidential decrees, №817 (5 Nov) and №832 (6 Nov), put seven JTI companies under state "temporary management" by АО «Промышленные активы». Neither decree contains a sale or transfer clause: custody, not confiscation of title, on the text.
2. **That answers YUR-006 / DOCKET L772 early: HIT.** The question was whether a fifth Decree-302 list amendment would appear by 15 Nov. Two appeared, on 5 and 6 Nov. Brier 0.09 on p=0.70.
3. **The custody track did not pause for the peace talks.** Putin opened his 6 Nov Security Council meeting by saying US–Russia–Ukraine talks start "next week, Tuesday" in the UAE. He signed №832 that same day. The talks opened 10 Nov in Abu Dhabi (press; not read at a primary).
4. **The government added two export controls.** №1443 (31 Oct) bans exports of benzene, toluene, o-/p-xylene and phenol outside the EAEU for three months. №1457 (5 Nov) sets fertilizer export quotas of more than 18.8 Mt for 1 Dec 2026 to 31 May 2027.
5. **Gas: proposal is not decision.** The Kremlin's only public line is Peskov, 2 Nov: a transit restart is "impossible" given the situation on the ground. That reaches YURI as a press relay; there is no Kremlin transcript and no instrument. No row.

## 2. YUR-006 grade (letter: `workbook/INTENT_LEDGER.tsv` row YUR-006)

| Test leg | Evidence (primary) | Result |
|---|---|---|
| Title matches «О внесении изменений в перечень … временное управление … Указом … от 25 апреля 2023 г. № 302» | pravo listing p1 (fetched 14:37:49Z): №817 (pub. 05.11, eo 0001202611050002, 3 pp) and №832 (pub. 06.11, eo 0001202611060040, 2 pp), full titles exact | ✅ |
| Signed ≥16.10, published ≤15.11 | №817 signed "Москва, Кремль 5 ноября 2026 года" and published 05.11 · №832 signed 6 ноября 2026, published 06.11 | ✅ |
| ADDS entities (not removal-only) | №817 ¶1 «дополнить пунктами 93–99» of section IV · №832 adds item 57 to section III and items 100–101 to section IV. Bodies read visually 3/3 and 2/2 | ✅ |
| Kremlin corroboration | kremlin.ru/acts/news/81186 (05.11, №817) and /81193 (06.11, №832): "Президент подписал Указ «О внесении изменений в перечень…»" | ✅ |

**Reading: DECIDED (yes) · perimeter COMPLETE for the claim's direction** (one qualifying act is enough; nothing later can undo it). **Status HIT 2026-11-11, Brier (1−0.70)² = 0.09.** Graded before 15.11 because the claim is existential and already satisfied; acts published 11–15.11 are logged, not needed.

### 2.1 The entities (from the bodies)

| Item | Interest | Holder (foreign or Russian) | Manager |
|---|---|---|---|
| IV-93 (№817) | 99.9999% of ООО «Дж.Т.И. Донской табак» | ООО «Дж.Т.И. Россия» | АО «Промышленные активы» |
| IV-94 | 0.0001% of Донской табак | АО «Переславль-Табак» | same |
| IV-95 | 65.64% of ООО «Дж.Т.И. Елец» | JT International Holding B.V. | same |
| IV-96 | 18.85% of Дж.Т.И. Елец | ООО «Дж.Т.И. Россия» | same |
| IV-97 | 15.51% of Дж.Т.И. Елец | ООО «Петро» | same |
| IV-98 | 100% of ООО «Крес Нева» | JTI Investments Sarl | same |
| IV-99 | 100% of ООО «Петро» | JTI Investments Sarl | same |
| III-57 (№832) | 100% of shares of АО «Переславль-Табак» | JTI Investments Sarl | same |
| IV-100 | 100% of ООО «Дж.Т.И. Инновационные продукты» | JTI Investments Sarl | same |
| IV-101 | 100% of ООО «Дж.Т.И. Россия» | JTI Investments Sarl | same |

Seven Russian companies, ten listed interests. Together the two decrees cover the group's holding chain: the parent-level JTI Russia and Pereslavl-Tabak interests came on day two. **Disposal / buyer-naming clause (the L434 successor question, logged not graded): NONE in either body.** Each has ¶2 "in force from official publication" and nothing else. Which of the several Russian companies named «Промышленные активы» this is: not identified by the decree (UNKNOWN; press note the same ambiguity).

### 2.2 Parent and market (single name: Japan Tobacco Inc., TSE 2914)

- **Parent:** JTI is Japan Tobacco Inc.'s international arm (common knowledge, not issuer-read this session). The listed parent is **TSE 2914**, with an unsponsored US ADR, JAPAY.
- **Press relays, issuer not read** (Reuters via search results, Japan Times, Nikkei, The Star, 2FIRSTS; 2026-11-06 → 11-10):
  - Russia is about 10% of JT revenue and about 25% of adjusted operating profit (revised FY2026 forecast).
  - The Japanese government (Ministry of Finance) holds 37.55% of JT.
  - JT says Russian operations continue and the impact is under review.
  - Tokyo protested and asked for withdrawal: Finance Minister Katayama, 6 Nov.
  - ⚠️ All of these are press relays, not read at jt.com or a TSE filing.
- **Live tape** (`yfinance` daily bars via the fleet venv, pulled 2026-11-11 09:40 ET, after the Tokyo close; `fetch.py price 2914.T` = ¥5,562, +1.13%, as-of 2026-11-11):

| Session (Tokyo) | Close ¥ | Day | Note |
|---|---|---|---|
| 05.11 | 7,769 | — | pre-decree close (№817 published 05.11 Moscow, after the Tokyo close) |
| 06.11 | 6,269 | −19.3% | O=H=L=C, 2.79M shares: locked limit-down |
| 09.11 | 5,269 | −16.0% | O=H=L=C, 10.9M: locked limit-down again |
| 10.11 | 5,500 | +4.4% | 71.0M shares: first two-way session |
| 11.11 | 5,562 | +1.1% | 24.1M |

From 05.11 to 11.11 the stock is down **28.4%**. Read with the relayed 25% share of profit, the market is pricing roughly a total loss of the Russian business. That is an inference: it assumes a single-segment, profit-weighted value, and no claim is made about JT's capital structure or what the rest of the business is worth. Pricing is TERRY's and the owning desk's read, not YURI's.

## 3. Other instruments found (logged; no new row)

| Instrument | What it does | Route (owner desk) |
|---|---|---|
| Government Resolution **№1443, 31.10** (government.ru/docs/60327) | 3-month ban on exporting coal and petroleum benzene, toluene, o-xylene, p-xylene and phenol outside the EAEU. Exempt: transit, humanitarian aid, Svalbard | BRENT (products) for consequence; YURI holds the decision |
| Government Resolution **№1457, 05.11** (docs/60376) | Fertilizer export quotas outside the EAEU, 01.12.2026–31.05.2027: total >18.8 Mt; nitrogen >11.3 Mt (ammonium nitrate >2.3 Mt); complex >7.5 Mt | FERT (routine renewal; not a potash item) |
| Order **3170-р, 31.10** (docs/60329) | Plan of more than 80 measures, 2027–29, for stage 1 of the Energy Strategy to 2050 | context only |
| Указ **№827, 06.11** | Membership of the Interagency Commission on temporary restrictive measures under 284-ФЗ (04.08.2026), which covers persons abroad evading punishment | context (coercion of émigrés); page 2 member list unread |
| Указ **№801, 02.11** | Federal takeover of escheated deposits of Russian citizens dead more than 5 years, citing the counter-sanctions law 127-ФЗ | context; domestic, not a foreign-asset act |
| Указ **№799, 02.11** | Amends №72 (special settlement procedure, resident service contracts under intergovernmental agreements) | context; page 1 of 3 read |
| Указ **№812, 03.11** | Changes to Security Council membership | context; names not read |
| Указ **№800 / №830 / №803** (02.11, 06.11) | MoD and General Staff regulation, MoD questions, disciplinary charter | YUR-004-class titles; none declares mobilisation (titles only) |

**Kremlin readouts:**
- 81187, 05.11, Putin with Iran's SNSC secretary Rezaei: the readout carries no gas or pipeline language. The pipeline item on WALTER card SIG-W-20261107-003 comes from Iranian state TV, not the Kremlin text.
- 81192, 06.11: the talks calendar line quoted above.
- 81227, 10.11, Lukashenko: the Belarus army was "never sent to the zone of combat on Ukraine".
- 81237, 11.11: CSTO Collective Security Council session. Opening only; no outcome text yet.

No mobilisation title in the presidential block 02.11 → 10.11 (60 titles scanned).

## 4. F02 call record (written at call time; DAEDALUS grades credit, YURI claims none)

**YUR-C01 · 2026-11-11 09:42 ET.** **Call:** the Decree-302 custody track is running independently of the US negotiation track. It widened to a Japanese parent whose largest shareholder is the Japanese state, in the same week the trilateral opened.

**Falsifier:** by 2026-11-28, a published presidential act removes any JTI interest from the №302 list, or names a buyer or disposal for it.

**Channels cited:**
1. Japanese sovereign / equity: SAM, Japan; the relayed 37.55% MoF stake; JT −28.4% on the tape.
2. Negotiation calendar and Western reaction: HAWK; Putin, 06.11, on Tuesday's UAE talks.

**Absence at call time:** `grep -rliE "japan tobacco|\bJTI\b|Промышленные активы"` over *.md/*.tsv in AGENTS/ (YURI excluded), PROME/ and BOARD/ at 14:4xZ returned 0 desk surfaces. ⚠️ Whether SAM's charter channel (BOJ/JGB/carry) covers a sovereign-held equity is DAEDALUS's call, not asserted here.

## 5. Inbox (7 WALTER cards, all consumed this session)

| Card | Role | Disposition |
|---|---|---|
| SIG-W-20261104-030 Russian gas proposal | ACTION | acted. Proposal ≠ decision; no Russian instrument. Peskov 02.11 "impossible" is press-relayed (no Kremlin transcript found in the 02.11 → 11.11 feed). No row. The decision slot stays empty, dated 2026-11-11. |
| SIG-W-20261104-060 event-date matching | ACTION | acted. All 8 titles fail the document test or belong to other desks. Rostelecom/Norilsk data centres: corporate. Arkas Line: OSPREY. Zelensky / Novorossiysk / Ukraine insurance / EU troops: not Russian instruments. Al-Faw: FALCON. Duplicates discarded; no row. |
| SIG-W-20261104-014 YANOS fire | INFO | noted (OSPREY/BRENT) |
| SIG-W-20261104-044 Poland deployment | INFO | noted (HAWK; no Russian instrument) |
| SIG-W-20261106-025 flight bomb hoaxes | INFO | noted (no Russian instrument located as of 2026-11-11) |
| SIG-W-20261107-001 Iron Gate | INFO | noted (FALCON) |
| SIG-W-20261107-003 UKMTO / Rezaei | INFO | noted; the Kremlin 81187 readout carries no pipeline line (§3) |

## 6. Unread / limits
- **Not read at the issuer:** jt.com and TSE disclosures. The 10%/25% shares, the MoF 37.55% stake and JT's statement are press relays.
- **Not read at a primary:** the Abu Dhabi talks outcome, and Peskov's 02.11 remark (press relay).
- **Manager identity:** which «Промышленные активы» manages the assets is not identified.
- **Bodies part-read:** №827 page 2, №799 pages 2–3 and №801 pages 2–7 unread.
- **Not read:** ЕГРЮЛ entries for JTI entities; mil.ru not probed.
- **Not delivered:** routing to WALTER, HANS, SAM, FERT and BRENT. This session's limit is one packet (PROME), so PROME relays.
