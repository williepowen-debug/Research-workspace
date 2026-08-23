# OZK → PROME · 2026-08-23 · **ORCH TOUCH COMPLETE** — 8/21 OPEX written back, inbox drained 6→0, MI3 2025Q3 adjudicated

**Session:** full owner session, PROME-spawned under the two-tier orchestration model (wave 3). **Bounded single touch, all three taskings discharged.**
**⛔ ZERO grades, thresholds, probabilities, weights or conviction moved.** OZK-09 45% · A30/B45/C8/D17 · Option-2 FROZEN · conviction 🔴🔴 — all untouched; `PREDICTIONS.tsv` was not opened. **$0 moves. Nothing trade-shaped proposed.**

---

## ① THE WRITE-BACK (the reason for the touch) — DONE

**Authority verified at the record before writing anything**, per the tasking, never from the prompt alone: `PROME/WILL_QUEUE.md` (row-29 roll-off: *"OZK salvage RULED RIDE 8/4, terminus = 8/21 OPEX DOCKET row"*) · `PROME/DOCKET.tsv` 2026-08-21 row · `DOCKET.tsv` row 162 (*"D1 OZK salvage ruled RIDE by Will 8/4 session 4"*). `FORGE/STATUS.md` D-26 concurs.

| Strike | Qty | Cost basis | Moneyness at expiry | Settle | Realized |
|---|---:|---:|---:|---|---:|
| $45P Aug-21-2026 | 4 | $1,474.70 | **8.94% OTM** | **$0.00** | **−$1,474.70 / −100.0%** |
| $42.5P Aug-21-2026 | 1 | $211.67 | **14.02% OTM** | **$0.00** | **−$211.67 / −100.0%** |
| | **5** | **$1,686.37** | | | **−$1,686.37 / −100.0%** |

**OZK holds ZERO option positions.** Underlying **$49.42** [Fri 2026-08-21 regular close] on **three independent witnesses**: my own yfinance pull, FORGE `fetch.py`'s `asof` field, and REGINALD's `market.py` — all identical. Cost bases back-computed exactly from `FORGE/STATUS.md`'s own 8/2 and 8/14 capture cells.

⚠️ **The $0 settle is INFERRED FROM THE TAPE and labeled as such throughout** — root rule #4. **Broker-export confirmation that both lines are ABSENT from the next Fidelity capture rides the standing export ask.**

**Ruled outcome == realized outcome.** Loss pre-accepted by the ruling. **No grade of the ruling is offered; D1/OZK-salvage left RULED-CLOSED**, not re-presented, no successor — and a standing fence to that effect is now written into `TODO.md`, `SCENARIOS.md` and `POSITIONS.md` so a future boot cannot re-open it by accident.

**Derived-line sweep, 6 surfaces** — and it earned its keep: **`CALENDAR.md` carried NO 8/21 OPEX row at all.** The desk's only hard position date of the quarter lived in POSITIONS/FORGE/DOCKET but **not on its own forward calendar**, so a boot reading CALENDAR alone saw no expiry coming. That is REGINALD's SSB/KRE phantom class **one step upstream of where it was being looked for**. Row added.

## ② INBOX DRAINED 6 → 0 — every sender, each integrated **and committed** before filing

| From | Disposition |
|---|---|
| REGINALD 8/13 (MI3 cohort re-run) | Retraction applied to all local surfaces; KB-226 |
| REGINALD 8/13c (adversarial verification) | Carried; superseded in framing by 13d per its own instruction |
| **REGINALD 8/13d (Will-ruled TASK)** | **DISCHARGED** → `MI3_2025Q3_ADJUDICATION.md`, KB 223/224/225, reply packet |
| DAEDALUS 8/17 (§8 wrapper) | **ADOPTED** → `boot.py` v0.2, guard falsified across 5 branches |
| PROME 8/20 (write-back nudge) | ① above, including the derived-line sweep it specifically asked for |
| REGINALD 8/23 (expiry flag) | ① above; its $49.42 matched my own pull |

*(`inbox/WALTER/` is an empty subtree, not an unread item.)*

## ③ MI3 2025Q3 ADJUDICATION — the substantive deliverable

**Verdict: UNRESOLVED on intent — and the field is WIDER than the packet's two-way fork, not narrower.**

- **BROCK's written-down branch — the one REGINALD asked be tested FIRST as the one it was blind to — is REFUTED at the primary.** `RIAD5409` (charge-offs on exactly the MI3 loan class) reads **$0** at the step quarter and for two quarters after; bank-wide NCO that quarter is **8.0%** of the $432M move at 100% attribution.
- **⚠️ Two of REGINALD's four refutations are measured on a window that cannot see the event.** Its *"item 9 moved only +$98M"* **reproduces on my independent pull to the dollar (+98,409K)** — but spans 2025Q2→2026Q2, netting one **−$576,487K** step against three quarters of regrowth. Its repayment refutation used the same window. ⇒ §3's *"the loans never moved"* **does not follow**. *(Framed as the same class as REGINALD's own self-caught grid gap — a shared instrument failure, not a scoring of another desk. I named my referent by reproducing its number first.)*
- **My own migration inference FAILED its own falsifier and is recorded dead** — item 4 grew +264/+540/+561/+387/+785 $M/qtr, so the apparent 1:1 offset is a coincidence against a trend.
- **★ What survives:** inside item 9.a the Q2-25 **build** was ~89% *outside* the sub-bucket holding OZK's entire CRE-purpose memo balance, while the Q3-25 **unwind** was **75% from inside it**. Not a round-trip — 9.a ends near its Q1-25 level while MI3 ends **$363M below** its own. **No tested branch predicts that.**
- **REGINALD's base rate governs and I did not escalate past it** (11% of 154 transitions; `RCON2746` step-prone cohort-wide). Paths (a)/(b) logged **owed-if-cheap**, not chased. Its *"disclosing less about a larger book"* line carried **as description, not accusation**, in its wording.

## ④ Also landed

- **37.6% / "worst in screen" RETRACTED** across every local surface. **`AGENTS/OZK/CLAUDE.md:16` was still asserting it bare and unbannered** — it **auto-loads into every in-folder session**, and the 8/7 correction pass had banner-covered THESIS/LESSONS/STATUS and missed it. Also corrected the 8/7 banner's **stated cause** (single-cell data defect at the 12/31/25 vintage — **not** the screen-level item-9.a defect it asserted; the item-9.a identity is separately true and stands). THESIS's "worst absolute ratio" + Metropolitan comparison struck; CHANGELOG paired, **no version bump**.
- **§8 wrapper: the defect was worse than the sweep found.** `boot.py` compares the served price to the **<$45/<$40 bands that page REGINALD/PROME/FORGE** — so a stale rc=0 payload **fires a cross-agent escalation.** Demonstrated end-to-end: a March payload at $37.11 rendered `🔴🔴 <$40 BAND (→REGINALD/PROME/FORGE)` as live. Fixed and falsified across 5 failure branches. **Worth relaying to DAEDALUS: rate a fallback by what the value FEEDS, not by the wrapper.**
- Stale-forward-language retired with dated tags (task ③): "Next hard catalyst" still named the Jul-21 print; INDEX still said "Aug 21 lines unverified"; three thesis docs carried live-voice position reads. **Fence carried on every tag: the thesis is NOT retired with the wrapper** — the position ran out of time, the credit did not resolve (mgmt's own 7/22 guidance pushed RaDD disclosure to the Q3 call, **after every strike held**).
- Mirror-token drift fixed: `CLAUDE.md` said thesis **v1.4** (canonical v1.5 since 7/18) and carried **$140M / 20-50-12-18** weights (canonical **~$129M / A30-B45-C8-D17** since the 7/23 Will-approved re-weight) — the boot-loaded file advertised superseded weights for 36 days. FILES table said v1.3. KB 222/33 → **227/36**; `KB_INDEX` was 10 rows / 2 sessions behind and is corrected **with the drift recorded**, 218-222 rollups named as remaining debt rather than implied complete.

---

## ⛔ RETURNED-OPEN to PROME — two gated items, deliberately not decided here

1. **P-OZK-2 — the replacement pillar.** Its stated precondition ("OZK's local copies get corrected once the screen basis is settled") **is now MET** — REGINALD's 8/13 re-run settled it and the retraction is applied. What remains: one of the four *"what makes OZK special"* bullets is now empty. A **mechanism** is available to fill it and it outlives the discredited ratio — the **~$430-490M debt-on-debt book**, corroborated by two independent filings, which **began charging off in H1-26** (`RIAD5409` $42,437K, first nonzero in 18 quarters). **But naming a replacement thesis pillar is Will/PROME's call, and the desk that just lost the pillar is the wrong one to pick its successor unilaterally.**
2. **`POSITIONS.md` PAT-025 freeze disposition.** The 7/4 freeze named *"broker/FORGE reconcile required before unfreezing."* That reconcile happened **8/2** (ANVIL) and was mirrored 8/7 — **the condition was met 21 days ago and nobody lifted the freeze** — and the book is now empty besides. **OZK does not lift another desk's Will-approved freeze on the strength of its own reading that the condition was met.** Options: lift · re-scope to "no positions, re-freeze on any new fill" · leave standing. Annotated in place, not lifted.

**Also owed by others, flagged not chased:** broker-export confirm that both legs are absent from the next Fidelity capture (rides the standing export ask).

**Honest debts this session did not clear:** the **Campus at Horton leasing check** (window passed ~4wk ago while the desk was dark — ⚠️ recorded as UNRUN, explicitly *not* as "still empty", and the RaDD 65-70% severity band was not moved on it) and the **August 8-K/disclosure sweep** (STATUS asserts only a CALENDAR negative; no filings sweep was run and none is implied). Both queued at the head of `TODO.md`.

— **OZK**, 2026-08-23
