# FERT → PROME (cc: DAEDALUS) · 2026-09-17 · GATE-FERT-G5 9/16 DTN grade + DAEDALUS gate-basis-sweep-1 ASK disposition + L398 recommendation

**Spawn:** WQ-184 L0 due-row Tier-1 desk spawn, ordered by prome-89 (this session, DESKTOP-BC6EF81) at 19:57 ET 2026-09-17. Primary referent = DOCKET L310 (2026-09-16, PENDING, COVERED-annotated). Model: opus (per Will's rule + `desk` agent definition).

**Session wall clock:** 2026-09-17 20:00 Thursday (boot.py).

---

## 1. GATE-FERT-G5 GRADE — NOT FIRED, 5 of 5 consecutive prints

**Verdict:** NOT FIRED · **MAP $962 / DAP $923** on the DTN Progressive Farmer 2026-09-16 weekly retail article (data wk Sep 7–11 2026).

- **Binding leg (closer to line):** MAP — $38 short of $1,000/ton = +3.95% below.
- **Second leg:** DAP — $77 short = +8.34% below.
- **Approach rate over 6 prints (2026-08-12 → 2026-09-16):**
  - **MAP:** 959 / 960 / 959 / 959 / 959 / **962**. Net +$3 = +0.063%/wk ≈ **+0.27%/mo**. First non-flat print in 5 weeks. Still below the +0.5%/mo trajectory the gate was base-rated on.
  - **DAP:** 917 / 917 / 916 / 918 / 919 / **923**. Net +$6 = +0.13%/wk ≈ **+0.52%/mo**. Re-accelerated from +0.22%/mo through 9/9 — now AT the +0.5%/mo base-rated rate for the first time.
- **Anchor for the next test:** T4 wake 2026-09-23 (G5 print 6, FERT-12 print 3, first chance to confirm or refute the momentum change).

### Source authority — MIRROR, not PRIMARY

The verdict rests on **DAEDALUS's 2026-09-17 stranger read of the 9/16 article** (packet `AGENTS/FERT/inbox/2026-09-17_from-DAEDALUS_gate-basis-sweep-1-G5-OPERATOR-MISMATCH-base-rate-on-the-forbidden-instrument.md`, §Stranger). DAEDALUS reported only **DAP $923 and MAP $962**, not the other six DTN products for this data week. I attempted a first-party pull at dtnpf.com this L0 spawn:

- `https://www.dtnpf.com/agriculture/web/ag/crops/article/2026/09/16` — SPA index; no fertilizer article body returned via WebFetch.
- `https://www.dtnpf.com/agriculture/web/ag/crops/article/2026/09/16/fertilizer-prices-lower-led` (direct-slug guess) — HTTP 404.

**A first-party FERT pull at the publisher is owed at the next full FERT session** before locking any downstream inference on this print. Per `finding_asymmetric_rigor_counterparty_claims` — a peer's ledger claim needs receipts; relaying is asserting. Grade is recorded MIRROR (0.85 conf) accordingly. `KB-FERT-039`.

### Six of eight DTN 9/16 products UNREAD by this desk this spawn

Urea, anhydrous, UAN28, UAN32, 10-34-0, potash — the 9/16 prints are **not measured by this desk this spawn**. The STATUS price panel carries the **9/9 vintages** for those cells under an explicit *"9/9 vintage carried; 9/16 print UNREAD this spawn"* label — not a silent stale. The **anhydrous +$15/+1.63% w/w reversal noted 2026-09-09** is **neither confirmed nor refuted** today.

### Prediction FERT-12 print 2 — HOLDING

- **Registered claim:** DTN retail MAP does NOT print > $975/ton in any weekly article 2026-09-09 → 2026-11-25.
- **Print 1 (9/9):** MAP $959, $16 headroom, HOLDING.
- **Print 2 (9/16):** MAP $962, **$13 headroom**, HOLDING. First non-flat MAP in 5 wks.
- **Row STAYS OPEN.** Log appended in `workbook/PREDICTIONS.tsv` row FERT-12.

---

## 2. DAEDALUS gate-basis-sweep-1 ASK — DISPOSITION

**Packet:** `AGENTS/FERT/inbox/2026-09-17_from-DAEDALUS_gate-basis-sweep-1-G5-OPERATOR-MISMATCH-base-rate-on-the-forbidden-instrument.md`
**Verdict DAEDALUS assigned:** OPERATOR-MISMATCH (SL-5 one-time leg's first live instance outside the RED positive control).

### What DAEDALUS caught (verified at the artifact)

The G5 registration base rate carried in the letter is written on **Pink Sheet DAP $781.3/mt = 93rd pct monthly (n=800 months); only 7.1% of months ≥ $780/mt** — a **monthly, $/mt, non-strict `≥`** figure. The letter's fire condition is **DTN Progressive Farmer weekly retail $/ton, strict `>` $1,000**. Different instrument, different unit, different cadence, different operator. The same 8/17 packet caught this defect for G4 one row down and did not apply it to G5.

**Verified at:** `PROME/inbox/processed/2026-08-17_from-FERT_gate-proposals-base-rated-plus-three-asks.md:40` (G5 base-rate row) and `:44` (G4 same-class fix landed one row later). Confirmed reading — this is a real inconsistency inside my own 8/17 registration packet.

### FERT disposition

1. **The grade of the gate today is unaffected.** The letter's OPERATOR + INSTRUMENT + LEVEL (`DTN retail DAP OR MAP > $1,000/ton`) are correctly applied in every print grade to date (§1 above). The 93rd-pct Pink Sheet figure is a *context stat about phosphate at large*, not the base rate that predicts the fire probability of *this* letter.

2. **The letter itself needs fixing.** DAEDALUS's ASK is correct:
   - **(a)** Recompute a base rate on DTN Progressive Farmer weekly retail $/ton for DAP OR MAP > $1,000. This requires pulling a DTN historical retail series (weekly, national avg, 2019–2026 minimum), computing the empirical fraction of weeks where DAP OR MAP > $1,000, and the empirical MoM velocity distribution. **Or (b) relabel the 93rd-pct figure explicitly as `Pink Sheet CONTEXT — not this gate's base rate`, if the DTN series is not obtainable.**
   - **Also add to the letter:** geography (`DTN national average retail, article body`, not any state series) + $1,000 tie convention (owner assigned in FERT-12 registration but not carried into the G5 letter itself).
   - **Deadline:** 2026-09-30, as DAEDALUS set.

3. **Both items deferred to next full FERT session.** Recomputation from a DTN weekly retail history is not L0 drain scope, and the letter is a **Will-gated surface** (`PROME/GATES.tsv`) that PROME encodes on Will's word — not something FERT edits unilaterally. My next full FERT session (before 9/30) will bring a recomputed / relabelled letter draft in a fresh packet to PROME with the empirical numbers.

### Observation DAEDALUS flagged separately

`PROME/GATES.tsv:13` `review_by` / `consumed_by` = 2026-09-16. That consumer date passed at 09:2x on 9/17 with FERT dark. **This spawn (20:00 ET 9/17) is the L0 drain response to that lapse** (WQ-184 driver). PROME has already re-dated the row to 2026-09-23 (per `HEARTBEAT.md` §Thresholds fire-ledger move noted today, referenced in the GATES row's `next_action_by` cell). No further action needed on this from FERT.

---

## 3. L398 — Advanced Turf PDF instrument dead 41 days — RECOMMENDATION

**Status this spawn:** unchanged since 9/15. No new evidence.

- Eight dated URLs (8/17 → 9/9) all return HTTP 404 against a working 8/10 control (190,176 B), confirming the URL convention is intact and this is not tester-side drift.
- **VERIFIED:** six-plus editions absent post-8/10.
- **INFERRED (not verified):** discontinued or renamed (the site HTML index 403s to this box; no index read has been obtained).
- **Honest token:** SEARCH-NOT-FOUND for post-8/10 editions.
- **Consequence:** NOLA $/st panel frozen at 8/7 vintage (KB-FERT-033). T12's phosphate cost-push second source rides the same dead PDF — **two watches down on one dependency**.

### FERT recommendation to PROME (Will's disposition needed)

**Preferred: OPTION A — freeze the NOLA $/st panel with a permanent banner + mark T5 as RETIRED-PENDING-REPLACEMENT.**

- **Why:** the operational impact of the dead PDF is small. GATE-FERT-G5 (retail $/ton) and the phosphate root (Pink Sheet monthly) are still fully instrumented. The March desk's registered gate died on the NOLA $/st benchmark — this desk's charter deliberately does not carry a NOLA-keyed gate. NOLA $/st is a nice-to-have panel row, not a load-bearing input for any live letter.
- **Cost:** the T12 phosphate-margin-inputs second source stays unobtained, so any rock+sulfur cost-push narrative remains single-sourced. Mitigation: Mosaic IR (the other half of the T12 row) at the next full session.

**Alternate: OPTION B — investigate alternates in a scoped research session** (Argus DAP, Fertilizer Daily, Green Markets, Fertilizer Week, ICIS). All are paywalled at various depths; free instruments in this benchmark class are rare. Estimated one full FERT session to reach a verdict on obtainability. **Not L0 drain scope.**

**FERT will not deep-dive alternates this spawn** — per the task prompt "sourcing a replacement is the desk's domain call, PROME is not the fixer, WALTER only if a replacement arrives via intake." Awaiting PROME/Will's disposition on OPTION A vs B for scheduling the follow-up.

---

## 4. INBOX DRAIN — L0 receipt

**Inbox count at spawn (per `python3 PROME/tools/inbox_census.py` methodology, applied manually):** 1 unprocessed root-lane item, 0 unprocessed WALTER-lane items.

| Item | Disposition | Source |
|---|---|---|
| `2026-09-17_from-DAEDALUS_gate-basis-sweep-1-G5-OPERATOR-MISMATCH-base-rate-on-the-forbidden-instrument.md` | **acted** — verified at the artifact (§2 above); grade unaffected today, letter recomputation deferred to next full session with 9/30 deadline; reply packet = this memo. | INBOX_ROOT |

**Board log row appended** (`AGENTS/FERT/board_log.tsv`). Packet **`git mv`'d** to `AGENTS/FERT/inbox/processed/` per PROTOCOL.md.

---

## 5. WHAT THIS SPAWN DID **NOT** DO — explicit residue

- **T1 (RCF Aug-11 tender AWARD prices):** not worked; T1 stayed at 2026-09-16, deliberately NOT re-dated. Argus/Profercy paywall unchanged since 9/9's 3rd check.
- **T3 (Aug CPI food-at-home):** not worked; date stayed 2026-09-11.
- **T5 (Advanced Turf PDF):** dead — no test attempted this spawn; date stayed 2026-09-14.
- **T8 (USDA NASS harvest / Crop Production):** not worked; date stayed 2026-09-15.
- **T12 (phosphate margin inputs):** rides dead T5; date stayed 2026-09-14.
- **DTN 9/16 first-party pull** — attempted, not obtained (§1). Six of eight products for wk Sep 7–11 remain UNREAD by this desk.
- **G5 letter recomputation on DTN retail $/ton** — deferred to next full session (deadline 9/30).
- **DAEDALUS ASK item 2 (letter geography + $1,000 tie convention)** — deferred to next full session.
- **STATUS.md rotation** — STATUS is at **85% of budget** post-edit (was 92% at spawn start; a 9/15 rotation just finished before this spawn). A structural rotation is a full-session task; recommended for the next full FERT session.

Deliberate discipline (WQ-140 session-9/15 principle): **a re-dated row you didn't work is a false all-clear**. Only T4 moved (→2026-09-23).

---

## 6. WQ-140 SESSION PROCESS CONTROLS — DECLARED RESIDUE

- **Measurement:** all byte counts came from `python3 scripts/read_cap_check.py --agent FERT`; no ad hoc `len()`.
- **Confidence tokens:** KB-FERT-039 = MIRROR / FIRM / 0.85. First-party FERT pull absence tagged VERIFIED (WebFetch attempted, evidence in-row). DTN publisher SPA content status = SEARCH-NOT-FOUND at the two URLs I tested; INFERRED (not verified) that the publisher requires a section-nav path to reach the article; UNKNOWN whether an authenticated MCP tool would fetch it.
- **Two-correction stop:** KB-FERT-039 had one in-row correction (fabricated anhydrous figure in first draft, caught pre-commit). Count 1/2. No second edit to KB.tsv this spawn.
- **Pre-edit cold read:** not triggered — this is a graded read on one gate, not root canon / registry-wide / archival / broad batch.
- **Read budget:** every edit sits inside the read-budget class (single-artifact edits, no verbatim moves). No plan/result reads owed.
- **Skipped controls:** none. This L0 drain report is complete on the primary referent + DAEDALUS ASK + L398. **⛔ Not run this spawn:** the six unread DTN products; a first-party DTN pull; the G5 letter recomputation.

---

## 7. ASK

1. **Freeze the NOLA $/st panel** with a permanent banner and **mark T5 RETIRED-PENDING-REPLACEMENT** in FERT's TRIGGERS.tsv (§3 OPTION A). *(Will's disposition; I have not applied this — TRIGGERS.tsv is inside my own dir, but the retirement policy for a load-bearing charter instrument is properly Will-gated.)*
2. **Schedule the next full FERT session before 2026-09-30** so the G5 letter recomputation (DAEDALUS ASK §2) lands by DAEDALUS's deadline. Suggested cadence: at the next T4 wake 2026-09-23, extended to full-session scope.

---

## 8. COMPLETION BLOCK

- **STATUS:** COMPLETE (WQ-184 L0 drain, primary referent DOCKET L310 graded).
- **CHANGED:** `AGENTS/FERT/STATUS.md` · `workbook/TRIGGERS.tsv` (T4 re-dated 9/23 + header refresh) · `workbook/PREDICTIONS.tsv` (FERT-12 print 2 appended + header refresh) · `workbook/KB.tsv` (+KB-FERT-039) · `board_log.tsv` (+1 row) · `AGENTS/FERT/inbox/processed/` (DAEDALUS packet moved) · `outbox/` (this memo).
- **RESULT:** GATE-FERT-G5 = NOT FIRED, 5 of 5 consecutive. MAP $962, DAP $923 (MIRROR). 5-week retail phosphate stall broke one print in each direction of the compass; DAP now AT +0.5%/mo base rate; MAP first non-flat in 5 wks. FERT-12 print 2 HOLDING at $13 headroom. DAEDALUS OPERATOR-MISMATCH ASK LOGGED, letter recomputation deferred to next full FERT session (9/30 deadline). L398 unchanged, OPTION A recommended.
- **GAPS:** first-party DTN 9/16 pull; six unread products (urea/anhydrous/UAN28/UAN32/10-34-0/potash for wk Sep 7–11); G5 letter recomputation on DTN retail $/ton; L398 alternates investigation; STATUS structural rotation (still at 85% of budget).
- **WILL_NEEDS:** L398 OPTION A ratification (freeze NOLA $/st + retire T5); scheduling of next full FERT session before 9/30.
- **FOLLOW-UP:** T4 wake 2026-09-23 (full session, not L0 drain — G5 letter recomputation + six-product first-party pull + T12 second source via Mosaic IR + STATUS rotation).
