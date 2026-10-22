# WQ-295 R3 WATCH_FOR live test — YURI (9/26 candidates + realized-event alternates)

**Run:** 2026-10-22T02:55–02:58Z (2026-10-21 22:55–22:58 ET), WALTER (walter session, Claude Code, Opus 5.5), on PROME's ask (prome-56 cross-session message, 2026-10-21 ~22:55 ET). Read-only to `~/Research-Intake` at HEAD `1be2d6a` (2026-10-21 22:33 ET; `git pull --ff-only` = already up to date). Nothing written to the lane.

**Source of the candidates:** `PROME/inbox/processed/2026-09-26_from-YURI_cadence-and-watch-terms.md` (7 phrases, keyed YUR-001/004/003). YURI's own sweep carries the miss as item 18 (`AGENTS/YURI/research/2026-10-21_SWEEP_owed-list.md` L61).

**Method (R3, same as `research/2026-10-01_R3/groupB.md`):** `AGENTS/WALTER/tools/watch_for_harness.py` runs the lane's real `match_watch_for()` over (a) lane history — **14,561 unique headlines, 91 lane days, 2026-06-29 → 2026-10-21** — (b) live Google-News RSS samples, 90-day window (run 1: 425 headlines / 8 queries; run 2: 354 / 7; run 3: 498 / 9; queries in each `.out` header context below), (c) synthetic positive controls. This reader classified every hit. **TRUE** = the headline reports the event the phrase is keyed to; everything else (rumour, fear, conditional "if Russia declares…", precursor request, other decree, retrospective) is **FALSE**. ⛔ REJECTED at >0 FALSE; ✅ PASS otherwise.

**Raw outputs (unedited):** `run1_candidates.out` (sha256 e64c7897b8f70c78…), `run2_alternates.out` (2a2c5bb98a414ee0…), `run3_alternates.out` (577bad01097dc4d9…).

**Lane coverage:** all 15 phrases tested score **0 lane hits**. The lane runs no mobilisation or Decree-302 query (its Russia queries are `russia-ukraine-energy` and `russia-fuel-export-ban`), so every lane 0 is **UNINFORMATIVE**. The live sample is the basis for every verdict below.

**Trigger state at test time (YURI STATUS, 2026-10-21):** YUR-001 **VOID** (superseded by YUR-004, 9/26). YUR-003 **MISS, resolved 2026-10-02**. YUR-004 OPEN (public mobilisation declaration, window 10/02→10/31). New since the candidates were written: YUR-005 (№954 diesel-exemption postponement, resolves 11/02) and **YUR-006 (fifth Decree-302 list amendment, resolves 11/15)**.

## 1. The 7 candidates of 9/26, as keyed

| Phrase | Keyed to | Live hits | TRUE / FALSE | Verdict | FALSE shape |
|---|---|---|---|---|---|
| `mobilization decree` | YUR-001/004 | 2 | 0 / 2 | ⛔ DECLINE | 15,500-troop staffing decree headlined "New Russian mobilization" |
| `partial mobilization` | YUR-001/004 | 1 | 0 / 1 | ⛔ DECLINE | Meduza retrospective ("Four years after…") |
| `Russia mobilisation` | YUR-001/004 | 29 | 0 / 29 | ⛔ DECLINE | fears, rumours, denials, Zelenskyy claims, Estonia/Armenia contingency |
| `Putin signs decree` | YUR-004 | 26 | 0 / 26 | ⛔ DECLINE | troop-size decrees, classified decrees, ambassador dismissal, seizure decrees — none a mobilisation declaration |
| `temporary management` Russia | YUR-003 | 21 | 0 / 21 as keyed | ⛔ DECLINE as keyed | YUR-003 is a SALE trigger; every hit is a custodial placement or a request. **Re-key candidate — see §2** |
| `Nestle Russia` | YUR-003 | 41 | 0 / 41 | ⛔ DECLINE | seizure/administration coverage, "pledges to continue operations"; no sale. Trigger resolved |
| `Auchan Russia` | YUR-003 | 52 | 0 / 52 | ⛔ DECLINE | as above, plus 2 off-topic (Russian strike on an Auchan warehouse in Boryspil, Ukraine). Trigger resolved |

Synthetic controls: every candidate matched its synthetic headline (recall mechanics fine). The failures are precision, not matching.

## 2. Realized-event alternates (WALTER-drafted, for the owner's choice)

**YUR-004 — public mobilisation declaration.** The live coverage is dominated by conditional and rumour headlines ("Estonia ready to close border if Russia declares/announces mobilization"; "mobilisation orders" issued to reservists). The matcher is word-AND with no negation, so it cannot exclude "if".

| Phrase | Live TRUE / FALSE | Synthetic | Verdict |
|---|---|---|---|
| `declares mobilisation` | 0 / 0 (runs 2+3) | ✓ | ✅ PASS — ⚠️ its US twin `declares mobilization` hit the Estonia conditional ×2; the same false shape is reachable, only spelling kept it out of the sample |
| `declares mobilization` | 0 / 2 | ✓ | ⛔ Estonia conditional |
| `orders mobilization` | 0 / 2 | — | ⛔ "Mobilization orders and travel bans", "Hidden mobilization … receive orders" |
| `orders mobilisation` | 0 / 1 | ✓ | ⛔ DW "hundreds of thousands of mobilisation orders" |
| `announces mobilization` | 0 / 1 | ✓ | ⛔ Estonia conditional |
| `announces mobilisation` | 0 / 1 | ✓ | ⛔ Estonia conditional |
| `mobilisation decree` | 0 / 2 | ✓ | ⛔ 15,500-troop decree (Inbox.eu, Inbox.lv) |
| `general mobilization` | 0 / 3 | — | ⛔ Estonia conditional ×2, General Staff plan |

**YUR-006 — fifth Decree-302 list amendment.** The custodial-placement phrases have high recall: they fired on every placement in the sample (Nestlé/Auchan/Lemana Pro, Metro, AptarGroup, Tarkett/Ontex). Their only FALSE class is the **precursor request** ("Russian company asks Putin to place Nestlé assets under temporary administration, Kommersant reports"; "Metro asks Kremlin to place…"; "Putin was urged to impose…").

| Phrase | Live TRUE / FALSE | Synthetic | Verdict |
|---|---|---|---|
| `temporary management Russia` (9/26 candidate, re-keyed) | 17 / 4 | ✓ | ⛔ by rule — 4 FALSE, all precursor requests |
| `temporary administration Russia` | 21 / 2 | ✓ | ⛔ by rule — 2 FALSE, both precursor requests |
| `under temporary management Russian` | 6 / 2 | ✓ | ⛔ precursor ×2 (narrower than the line above; no gain) |
| `under temporary administration Russian` | 5 / 5 | ✓ | ⛔ precursor ×5 |

"Reaction" headlines about a placement (France urges reversal; Nestlé responds) were counted TRUE: they report the keyed event.

⚠️ **Owner call, not WALTER's:** FLG's 10/21 packet set the precedent that a precursor hit can be **wanted** if the owner names it (`restraining order rent freeze`). For YUR-006 a "company asks Putin to place X" report may be a leading indicator of the next list amendment. **This is unverified:** I did not check whether the request stories preceded the Nestlé decree, and the timing of any request ahead of №661/№674/№689/№738 is unknown. Only YURI can adopt a precursor-bearing phrase, by name.

## 3. YUR-005 (diesel exemption)
No YURI phrase is needed for a lane test now. The lane already carries owner-landed diesel-ban phrases under other desks (`Russia extends diesel export ban`, `Russia lifts diesel export ban`, `Russia diesel export`; newsweep_config.py L1026–1193). Its comments note that the instrument is YURI's and that "no YURI set yet" exists. Not tested here.

## Limits
- Live samples are Google-News top-N per query over 90 days. They are not complete coverage; the sample changed between runs (the 15,500-troop headlines appeared in run 1 and run 3, not run 2).
- A 0/0 PASS proves zero noise in these samples only.
- YURI is closed out (942f5fbe3); no owner has adopted anything here. WALTER does not adjudicate YURI's triggers.
