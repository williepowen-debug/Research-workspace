# 8/21 OPEX — PRE-REGISTERED POST-EXPIRY WRITE-BACK CHECKLIST (TERRY surfaces)

**Built:** 2026-08-20 Thu 16:5x ET, **the session BEFORE expiry**, at PROME's tasking.
**Purpose:** make Friday's write-back a **checklist item, not an act of memory.** The phantom-position class (a leg that expires and lives on in a registry) is what this closes — REGINALD pre-registered its KRE $60P write-back yesterday (`dea6d0c99`) after two phantom precedents in its own `LESSONS`.

> ⛔ **NOTHING HERE IS A TRADE, A PROPOSAL, OR A RULING.** Every 8/21 leg is **decision-free (5/5, ruled)**. This file records **what to WRITE DOWN afterward**, not what to do.

---

## 0. Every expiring leg, priced at the 8/20 close — so tomorrow is a GRADE, not a guess

**All closes are TERRY own pulls, `fetch.py`, 8/20 regular session.** Contract detail from `FORGE/STATUS.md` via `positions_from_forge.py`.

| leg | qty | strike | **8/20 close** | move needed to finish ITM | FORGE resid. | read |
|---|---|---|---|---|---|---|
| **OZK $45P** | 4 | 45.00 | **49.28** (−0.40%) | **−8.68%** | $48 | 🟢 lapse |
| **OZK $42.5P** | 1 | 42.50 | **49.28** | **−13.76%** | $5 | 🟢 lapse |
| **KRE $60P** | 3 | 60.00 | **74.71** (−0.39%) | **−19.69%** | $6 | 🟢 lapse |
| **KELYA $7.5P** | 1 | 7.50 | **16.71** (+1.09%) | **−55.12%** | $5 | 🟢 lapse |
| **🔴 VLY $14P** | **1** | **14.00** | **14.12 (−2.22%)** | **−0.92%** | ~$1 | **🔴 LIVE — see §1** |

**Four of five are unreachable by any plausible one-day move and will lapse worthless. The fifth is not.**

---

## 1. 🔴 THE VLY EbE BRANCH IS NOT A ~2% TAIL — IT BASE-RATES AT **21.1%**

PROME's tasking called this *"the known-accepted ~2% EbE branch."* **Measured against VLY's own tape, that is off by an order of magnitude, and the correction is the single most useful thing in this file.**

**VLY closed `$14.12`, `−2.22%` — `0.85%` above its own strike. Exercise-by-exception needs a close `≤ 13.99`, i.e. a `−0.92%` day.**

| measurement | value |
|---|---|
| 1-yr daily returns | n = 247 · sd **1.73%** · 20-day sd **1.35%** |
| **days with a move ≤ −0.92%** | **52 / 247 = `21.1%`** ⬅ **the base rate for finishing ITM** |
| today's move | **−2.22%** |
| last 5 sessions | −0.07% · −0.47% · −0.54% · **−2.83%** · **−2.22%** ⇒ **down 5 of 5, ≈ −6% cumulative** |

⇒ **A move of the required size happened TODAY, and one twice that size happened yesterday.** The unconditional base rate is ~1-in-5 and **the recent path is adverse to it.**

**⚠️ STATED LIMITS, so nobody over-reads this:** unconditional 1-yr base rate; **ignores the OPEX-day pin effect** (which cuts toward the strike, direction ambiguous); ignores tomorrow's tape. It is a **base rate, not a forecast** `[[finding_base_rate_the_threshold_before_building_it]]`.

### 🔑 AND THE RULING DOES NOT DISARM THIS — READ CAREFULLY BEFORE ASSUMING IT'S COVERED

`FORGE/STATUS.md` line 106: **VLY $14P — ★ RULED LAPSE 2026-08-14 (Will, afternoon batch §3): ride to expiry, no action, no re-present.**

> **"RIDE TO EXPIRY" IS NOT THE SAME CLAIM AS "EXPIRES WORTHLESS."** The ruling correctly says *take no action*; it does **not** and **cannot** disarm broker auto-exercise. **A long put that finishes `$0.01` ITM is exercised BY EXCEPTION automatically** — Will's instruction is satisfied in full (no action was taken) **and the position still converts.**

⇒ **The 8/14 ruling stays intact and is NOT being re-presented.** What is pre-registered here is only the **write-back for a branch the ruling did not contemplate**, which is precisely PROME's ask: **if it exercises, Monday's short ~100 VLY is a KNOWN outcome to RECORD, not a surprise to INVESTIGATE.**

⚠️ **And note what exercise actually delivers: SHORT 100 VLY at $14.00, with weekend gap risk into Monday's open, in exchange for ≈$1 of intrinsic.** That is an unwanted delivery, not a win. **It is Will's and PROME's call, not mine, and I am flagging it the session before — not the Monday after.**

---

## 2. ⚠️ A CONTRADICTION INSIDE `FORGE/STATUS.md` — NOT MY FILE, FLAGGED NOT EDITED

| line | says |
|---|---|
| **106** | VLY $14P — *"✅ VERIFIED 8/14 · **★ RULED LAPSE same day**… ride to expiry, no action, no re-present"* |
| **168** | Aug-21 OPEX cluster — *"**KELYA 7.5P and VLY 14P have no standing ruling**"* |

**Both are live rows in the same file and they cannot both be true of VLY.** Most likely 168 simply predates the 8/14 ruling and was never reconciled — **but "most likely" is not a reconciliation, and the tie-break is not mine to make.** `FORGE/` is **PROME's** (owner since 7/30). **Routed, not touched** — `[[finding_owner_of_record_means_authoritative_not_correct]]`.

**KELYA $7.5P genuinely has no standing ruling** per line 168 — and needs none: **−55.12% OTM, it cannot reach.** Recorded so its silence is not mistaken for an oversight.

---

## 3. ✅ THE CHECKLIST — run this Friday 8/21 after the close, or Monday 8/24 at the latest

**Step 1 — pull the settles (own pull, never a mirror):** `OZK · KRE · KELYA · VLY`.
**Step 2 — grade each leg against §0.** Expected: 4 lapse worthless.
**Step 3 — VLY branch, whichever fired:**
  - [ ] **VLY close ≥ 14.00** ⇒ **lapsed worthless.** Record: *"VLY 14P expired worthless 8/21, close $X.XX; the 21.1% EbE branch did NOT fire."* **Record the non-fire explicitly — a branch that was flagged and didn't happen must be closed out loud, or the flag rots into a permanent open question.**
  - [ ] **VLY close ≤ 13.99** ⇒ **EXERCISED BY EXCEPTION.** Record: *"VLY 14P exercised 8/21 at close $X.XX ⇒ SHORT 100 VLY delivered, settles Monday 8/24."* **This was PRE-REGISTERED — it is a known outcome, not an investigation.** Notify **PROME** (position mirror) + **Will** (it is a new equity exposure). ⚠️ **Do NOT propose a cover; that is a fresh decision on its own merits, not a write-back.**
**Step 4 — surfaces I own, updated so no phantom survives.** ⚠️ **I first wrote "no TERRY card names an 8/21 leg" and then VERIFIED it and was WRONG — there is one, and it is the whole reason this step exists:**
  - [ ] 🔴 **`TRY-RESHAPE-BC` IS THE PHANTOM-RISK CARD.** It *is* the Aug-21 bank-put dust book — `KRE 60P ×3 · OZK 45P ×4 · OZK 42.5P ×1 · KELYA 7.5P ×1` (+ WAL 77.5P Robinhood, DARK-fenced, **not** an 8/21 leg — leave it alone). Its own INDEX row already says **"card rides to its 8/21 wall; formal close + postmortem at/after OPEX — no fresh decision exists for Friday."** ⇒ **Friday it stops being CONDITIONAL and becomes CLOSED.** Update `SETUPS.tsv` row + `setups/INDEX.md` row + `TRADE_BOOK.md`, **all three, same session** — `ledger_sweep` check A compares them and will exit 1 on a partial update.
  - [ ] **`POSTMORTEMS.md`** — the card's own text pre-registers a postmortem at OPEX. **Write it** (WRITE-BACK step 4). Its pre-registered grading line is already on the card: *"ride beats salvage only if OZK <44.90 (−14.2%) by 8/21; KRE −23.1% / KELYA −50.4% additionally required"* — **§0's closes grade that directly, and the answer is going to be that RIDE lost to SALVAGE.** Grade it honestly; the salvage was ~$41.75 net and was not taken.
  - [ ] **`TRY-WILL-QQQ-VFADE`** also carried an Aug-21 expiry (QQQ 680P/670P) but is **already terminal** — VOID 8/04, formally closed 8/13. **No action; recorded so its Aug-21 date does not read as an open leg.**
  - [ ] ✅ **TERRY's INDEX row (annotated 8/19) independently says `VLY = LAPSE (ruled 8/14)`** — which **corroborates `FORGE` line 106 and makes line 168 the stale side** of the §2 contradiction. Stated as evidence for PROME's reconcile; **still PROME's call, still not my edit.**
  - [ ] `PAPER_BOOK.tsv` — **verified 8/20 by grep, and this one DID hold: no paper row references any 8/21 leg** (open rows are PB-0001, PB-0002b, PB-0004 = TLT Sep-30 ×2 + KRE **Dec-18**). ✅ **Nothing owed here — recorded so the check is not re-run from scratch.**
  - [ ] `STATUS.md` — one line, and **state the VLY branch that actually fired.**
**Step 5 — `python3 AGENTS/TERRY/scripts/ledger_sweep.py` must exit 0** (check A catches exactly the phantom class this file exists to prevent).

---

## 4. What is deliberately NOT here
- **No proposal, no roll, no cover, no sizing.** All five legs are decision-free by ruling.
- **No edit to `FORGE/STATUS.md`, `PROME/GATES.tsv`, or any REGINALD/LABOR surface** — those desks own their own write-backs (REGINALD's KRE $60P is already pre-registered `dea6d0c99`; OZK is nudged).
- **No re-presentation of the VLY lapse ruling.** It stands.

---
*TERRY proposes only; Will approves. Nothing in this file moves money.*
