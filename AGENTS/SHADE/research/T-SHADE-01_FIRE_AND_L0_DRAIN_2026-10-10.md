# T-SHADE-01 fresh read + L0 inbox drain — 2026-10-10

**Session:** `shade-1010`, PROME-spawned (`prome-ce`) Tier 1 **L0 DRAIN-ONLY** (WQ-206 aged ACTION; DOCKET L671). Model `claude-opus-5-5`, Claude Code (Agent SDK spawn). Desk dark since the 10/1 closeout (`ffd823d80`), 9 days. Written 2026-10-10 ~12:5x ET (stamped from `date`). Markets closed (Sat); last closes 10/9; latest HY obs 10/8.

**Scope:** drain the whole inbox (2 top-level + 20 WALTER), answer PROME's lane-query ask by name, consume DAEDALUS's sweeps packet, own write-back. **No new direction.** The one state change below is **forced by a letter**, named in §1.

---

## 1. `T-SHADE-01` — FIRED (owner reading, 10/9 closes · 10/8 HY obs)

**What forced the read:** `SIG-W-20261002-005` (HY **324bp** [10/1 obs, pub 10/2]) was the level leg's 5th consecutive print >280. The trigger letter (`CLAUDE.md` § REGISTERED TRIGGERS): *"Any level-leg crossing obliges a FRESH sign-leg read ON CLOSES before the trigger state is restated."* DAEDALUS's 10/8 packet (Falsification #4) asked for the same restatement. **The read was owed from 10/2 and lapsed 8 days while the desk was dark.**

### 1a. Level leg — MET (5 of 5 on the 10/1 obs; run = 10 through 10/8)

FRED `BAMLH0A0HYM2` via `fetch.py fred BAMLH0A0HYM2 --periods 15` (latest-revised), **agrees with LIQUID STATUS L8** (LIQUID owns the series):

| Obs | 9/24 | 9/25 | 9/28 | 9/29 | 9/30 | **10/1** | 10/2 | 10/5 | 10/6 | 10/7 | 10/8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bp | 280 ✗ | 293 | 302 | 308 | 312 | **324** | 310 | 312 | 303 | 309 | 315 |
| run | — | 1 | 2 | 3 | 4 | **5 ⇒ MET** | 6 | 7 | 8 | 9 | 10 |

10/9 obs not published at read time (LIQUID: not out at 10/9 15:51 ET; 10/12 Columbus Day).

### 1b. Sign leg — fresh read on CLOSES, window sweep, both bases

Script: `research/tshade01_signleg_2026-10-10.py` (committed; reproducible). RAW = split-adjusted, not dividend-adjusted (basis of prior readings). ADJ = vendor dividend-adjusted as served 10/10. End = **10/9 close**.

| Window start | RAW wrappers | RAW managers | RAW w−m | ADJ wrappers | ADJ managers | ADJ w−m | Verdict (both bases agree) |
|---|---:|---:|---:|---:|---:|---:|---|
| 8/28 (pre-episode; re-reads the window graded 10/1) | −9.67 | −14.95 | +5.28pp | −6.75 | −14.51 | +7.76pp | NOT MET — managers led |
| **9/24 (last ≤280 session = level-run start)** | **−4.67** | **−2.05** | **−2.62pp** | **−3.16** | **−2.05** | **−1.11pp** | **MET — both down, wrappers more** |
| 9/25 | −4.97 | −3.21 | −1.76pp | −3.46 | −3.21 | −0.25pp | MET (⚠️ thin on ADJ) |
| 9/28 | −4.53 | −0.62 | −3.91pp | −3.01 | −0.62 | −2.39pp | MET |
| 9/29 | −4.97 | −0.88 | −4.09pp | −3.47 | −0.88 | −2.59pp | MET |
| **9/30 (since-last-read)** | **−3.52** | **+1.57** | −5.09pp | **−2.70** | **+1.57** | −4.27pp | **MIXED — wrappers DOWN, managers UP** |
| 10/1 · 10/2 · 10/5 | −2.94 · −1.64 · −1.18 | +2.16 · +1.89 · +1.47 | | same | same | | MIXED |

Per name, **9/24 → 10/9, ADJ:** ARCC −2.98 · FSK −2.95 · OBDC −3.63 · BIZD −3.07 vs APO −1.69 · ARES −2.41 ⇒ **every wrapper fell more than every manager.** RAW closes: ARCC 19.13→18.56 · FSK 11.17→10.84 · OBDC 10.80→10.11 · BIZD 12.90→12.08 · APO 120.69→118.65 · ARES 120.11→117.22.
Per name, **9/30 → 10/9, RAW:** ARCC −2.83 · FSK −1.36 · OBDC −3.62 · BIZD −6.28 (ADJ −3.00: $0.437 ex-div 10/1 inside the window) vs **APO +2.23 · ARES +0.90**.

### 1c. Owner ruling (SHADE owns whether THIS trigger fires; LIQUID owns the series)

- **The letter registers no window for the sign leg.** The two prior readings used the since-last-read window and also reported the level-crossing window; both agreed, so the question never arose. **It arises now.**
- **No FRESH window reads NOT MET.** Every start inside the HY episode (9/24–9/29) reads **MET on the letter's own example** ("both cohorts falling with wrappers falling MORE = MET"), on both bases. Every start from 9/30 reads **wrappers down while managers rose** — a case the letter's two examples do not cover; by the leg's stated purpose (*"catch collateral re-marking, not multiple compression"*) it is the stronger form, not the weaker. **Only the pre-episode 8/28 start reads NOT MET**, and it re-reads September's manager re-rating, already graded on 10/1.
- **Ruling: SIGN LEG MET, read on the level-run window (9/24 close → 10/9 close), the window that measures both legs over the same HY episode. LEVEL LEG MET. ⇒ `T-SHADE-01` FIRES — owner reading, 2026-10-10.** First fire since registration (7/9); ends the 5-for-5 manager-led record.
- ⚠️ **Disclosed, not buried:** (1) the window was chosen **after** seeing the data — the letter is silent on it; (2) the ADJ margin from a 9/25 start is **0.25pp**; (3) part of the RAW wrapper fall is BIZD's 10/1 and OBDC's 9/30 ex-dividends — the ADJ basis is shown beside it and gives the same verdict; (4) **this is a dated reading, not a standing state** — the next session re-reads both legs before acting.
- ⛔ **Not evidence for BROCK's X1 wrapper half** (a different test with a decomposition condition) and **not LIQUID's X1 HY level leg** (WQ-363: 3 obs). Cite by name.
- **Consequence, per the letter:** *"Execute the pre-registered double-jeopardy statutory entity+fund dig (ordered a→d). Standing rule: no dig absent a trigger."* **NOT executed this session (L0 drain-only).** Routed to PROME as a Tier-1 follow-up inside the pre-registered workstream (STATUS §10 #8). **Environment bands (separate systems): HY YELLOW (315 [10/8]) · APO YELLOW ($118.65 [10/9 close]).**

### 1d. ⚠️ Self-correction — the 10/1 "RAW closes 8/28 → 9/30" row does not reproduce

Recorded 10/1: wrappers **−7.80%** vs managers **−16.99%**, **+9.19pp**; APO "$114.83 [9/30]". **Vendor closes today:** 9/30 APO **$116.06** (also `fetch.py price APO --history 12`), ARES $116.17, ARCC 19.10, FSK 10.99, OBDC 10.49, BIZD 12.89. Re-computed on those closes: **wrappers −6.33% vs managers −16.27% ⇒ +9.95pp ⇒ NOT MET — the 10/1 verdict STANDS; its figures do not.** The 10/1 endpoints implied by the recorded percentages (APO 114.85, ARES 115.42, BIZD 12.33, ARCC 19.00) match no vendor close for 9/30 or 10/1. **INFERRED cause: 10/1 intraday quotes used as the "9/30 close"** — the letter says CLOSES only. The 10/1 level-crossing row (9/24→9/30) does reproduce (adjusted basis). ⇒ Prior-reading rows on SHADE surfaces carry the corrected figures from 10/10.

### 1e. Window-sensitivity guard — its premise failed

The charter guard said the relative spread's window-sensitivity is *"immaterial to the leg itself, which turns on direction."* **10/10: the DIRECTION itself turned on the window** (8/28 start NOT MET; 9/24–9/29 MET; 9/30+ MIXED). **Proposal to PROME (not encoded — a gate-letter change goes through PROME):** register the sign-leg window as **"from the close of the last ≤280 session before the current level run to the latest close"**, with the since-last-read window reported beside it. ⚠️ Proposed after the data, and it fires on today's data — PROME/Will should weigh it as such.

---

## 2. Inbox drain — 22 items (2 top-level + 20 WALTER)

| Item | Disposition | One line |
|---|---|---|
| PROME 10/1 lane-query sizing (ACTION, 9d) | **acted** | Answered by name: 8 rows ADOPT (one in SHADE's own Egan-Jones wording), bare "Group 1001" DECLINED → `PROME/inbox/2026-10-10_from-SHADE_lane-query-adopt-decline-by-name.md`. Counts verified at WALTER's table. |
| DAEDALUS 10/8 sweeps (ACTION) | **acted** | Ask 1b DONE (§1). Ask 1a (thesis-level falsifier): **dated deferral in STATUS, by 2026-10-23** — reason: registering one is prediction-class, outside L0 drain-only authority. |
| `-20261002-005` HY 324 [10/1] | **acted** | Level leg 5th print ⇒ MET; obliged the §1 read. |
| `-20261003-010` "Guggenheim Universe" (ACTION, 7d) | **acted** | §3. ADDS · partly DUPLICATES · does not CONTRADICT. Full-doc pull requested from WALTER. |
| `-20261008-008` credit bundle; Blue Owl into insurance (ACTION) | **acted** | §4. HY 303 [10/6] read into §1a. |
| `-20261008-033` WQ-399 receipt change (ACTION) | **acted** | Two receipts filed in the WQ-399 form (§5); charter step 4b fixed (C4 own-charter). |
| `-20261002-021` / `-022` Blue Owl tenders; GATE-BRK-R2 (a) fired on OCIC | noted | `[CONF BROCK 10/2]`. **FORUM-5 W2 check: NOT FIRED — concur BROCK's 10/2 reading** (proration is a liquidity event, not forced recognition). W2 primary wording, which BROCK recorded as not located: `FORUM/2026-08-13_private-credit-recognition/04_synthesis/01_BROCK_joint-synthesis-DRAFT.md` L135 — consistent with BROCK's reconstruction. |
| `-20261009-003` PC valuation; SEC staff fair-value statement 9/28 | noted | Staff guidance (no rule) covering BDCs/interval funds — vector #5 valuation-machinery context; Kellermeyer is BROCK's. |
| `-20261010-006` Voya on SEC 7(A) FOIA log | noted | A 7(A) denial is not an investigation; Voya is not a PE-owned insurer. No SHADE letter keys. |
| `-20261002-012` Amazon chip SPV, IG debt for insurers | noted | Insurer-sink channel for IG private ABS; no SHADE letter keys. |
| `-20261007-008` / `-012` NYFed visits (+ metadata correction) | noted | Context; COR-20261007-12 receipted NO-OP. |
| `-20261007-016` Metrics Credit Partners | noted | BROCK's. |
| Isaias `-20261008-001` · `-019` · `-035` · `-046` · `-20261009-004` · `-011` | noted (bulk) | P&C / Florida / energy landfall; no PE-owned life-insurer letter keys on it. |
| `-20261008-027` ENSO · `-20261001-020` Pacific hurricanes | noted (bulk) | Climate context; no SHADE letter keys. |

## 3. "Guggenheim Universe" (`SIG-W-20261003-010`) — assessment

**Lead (third-party, MISPRICED ASSETS / Wyandanch, 8/23; WALTER read 1 page of 23):** 8 insurers in 4 control groups (Walter: Delaware Life/Clear Spring/Gainbridge · Amistad: EquiTrust/Heritage · Sammons: Midland/North American · Eldridge: Security Benefit) hold **$40.6B** of bespoke private paper across 564 securities; **$32.0B crosses control-group lines**; ~$24.5B in "Chicago-street private-credit LLCs."
- **DUPLICATES (one node):** Delaware Life is vector #1 — affiliate-contingent **$16,822M = 32.82% of GA** (Q2-26 statutory, SSAP-25 filer-defined). ⛔ Different perimeter from the lead's figures — never sum or difference them.
- **ADDS (the mechanism):** paper held **across nominally separate control groups is outside every filer's related-party test by construction** — SSAP-25 captures affiliates only. This is the allocation-discretion through-line one level up: the category boundary (control group) is set by ownership structure, and cross-group holdings of one manager's paper escape it. It also widens ladder rung (6) ("probe widens to Guggenheim AM") from a probe question to a holdings question.
- **CONTRADICTS: nothing on SHADE surfaces.** DLIC's 1.62% affiliated-reinsurance ratio (asset-side risk) is consistent with it.
- **Next (not this session):** full 23-page doc (pull requested from WALTER, $0) → verify at primary: DLIC Q2 Sch D (in hand) for the "Chicago-street" LLC family; then EquiTrust / Security Benefit statutory statements (issuer routes first — `[[finding_unfetched_is_not_unavailable]]`).

## 4. Blue Owl "big push" into insurance (`SIG-W-20261008-008` item 2)

FT 10/7 (headline; body not read), relayed by PrivateEquityWire: co-CEO Ostrover — a "big push" into insurance, **no plan to buy an insurer outright**, "balance-sheet-light." Blue Owl Insurance Solutions (from the 2024 Kuvare Asset Management purchase, $750M) — ~100 insurance clients, >$30B insurance-related assets at 6/30/26 per a **job posting** (weak source). **SHADE read:** a **mandate model** (stage 2 — assets into third-party insurer general accounts) without the affiliated-reinsurance/captive leg; same manager whose OCIC/OTIC tender queues are on the BOARD. **Watch item, no score move.** Sources: [PrivateEquityWire](https://www.privateequitywire.co.uk/blue-owl-plans-major-insurance-push/) · [Reinsurance News](https://www.reinsurancene.ws/blue-owl-capital-appoints-deva-mishra-to-lead-expansion-of-insurance-solutions-platform/) · [ai-cio (Kuvare)](https://ai-cio.com/news/blue-owl-announces-750m-kuvare-acquisition-in-latest-insurance-deal).

## 5. Corrections receipts (WQ-399 form)

`corrections_boot_check.py SHADE` → rc 1, 2 NAMED: **COR-20260921-17** (Nippon Life: two overstatements not three; balance ≠ flow) — **NO-OP**: SHADE logged `-011` on 10/1 as a "¥2tn project-finance target to FY2035", carried no dollar figure or axis count, no SHADE surface cites it. **COR-20261007-12** (NYFed metadata 0.70/"unconfirmed" → 0.80/"reports") — **NO-OP**: SHADE was INFO-only and cites `-008` nowhere.

## 6. What lapsed in the nine dark days (10/1 → 10/10)

| Owed (from 10/1) | Due | State 10/10 |
|---|---|---|
| `T-SHADE-01` fresh sign read after the 5th level print | ~10/2 | **LAPSED 8 days**; done 10/10 (§1) — **it fired** |
| `PREDICTIONS.tsv` + declared-flat TRADE surface (DAEDALUS PR6 ask 2) | 9/30 → 10/8 | **LAPSED** (now 10 days past original) |
| MEMORY.md rotation (98% of budget; STOP <22,785 B) | 10/8 | **LAPSED** — nothing appended 10/10 |
| ARI DEFM14A loan-level annex read | 10/8 | **LAPSED** |
| "Illiquid ABS" leg definition proposal → PROME | 10/8 | **LAPSED** |
| NAIC SVO override count | 10/8 | **LAPSED** |
| Guggenheim Universe assess (WALTER ACTION) | 10/3 | 7 days late; done 10/10 (§3) |
| PROME lane-query adopt/decline | next wake | 9 days; done 10/10 |
| Retirement scan | 10/1 closeout | not run 10/1; not run 10/10 (drain-only) |

**FORUM-5 W1 / DOCKET L182, one line:** all four legs were in by 10/2 (SHADE 10/1 `20261f699`; BROCK 10/2 `0f2ef30b3`); L182 is COVERED by **WQ-364** and waits only on Will's strict-vs-functional reading — **SHADE owes no enumeration on 10/16.**

**What a 10/16 SHADE session must do first:** ① re-read both `T-SHADE-01` legs on that day's closes and HY obs; if still MET, run the pre-registered dig (a) AAIA FY2025 annual Sch BA → ADS equity holding · (b) ADS facility counterparties · (c) F&G > Brighthouse > Corebridge Sch BA · (d) BROCK cross-check; ② the lapsed 10/8 items in the order above; ③ the Guggenheim primary verification once WALTER pulls the doc.
