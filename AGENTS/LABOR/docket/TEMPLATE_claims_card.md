# 🔧 TEMPLATE — Recurring Initial-Claims Grading Card

**Purpose:** discharge **BD-19**. Weekly claims are *permanently* multi-loaded (T-01/T-02, vector 13, Kill B, LAB-03, plus CARL's kill-rule leg 1), so C2a owes a frozen card **every week** — but a recurring catalyst has no natural "one week out" moment, which is the structural reason the 8/13 card was written the day before the print. This template makes the per-week cost ~10 minutes of *arithmetic*, not a fresh composition.

> ⛔ **THE ONE RULE THAT MAKES THIS TEMPLATE SAFE:** **§1 and §3 are REGENERATED from the live 4-week window every single week. They are NEVER copied forward.** The mechanical term `(X − R)/4` changes value *and sign* as different weeks roll off. A copied §3 carries the previous week's roll-off logic as if it still held — which is not hypothetical: **the 2026-09-10 card's docketed term was `(X−200)/4` when the true term was `(X−212)/4`, inverting the sign of the MA move at the modal print.** §2, §4, §6, §7 are the stable half and may be carried verbatim unless a STATUS threshold changed.

---

## FILL PROCEDURE (run these, in order, at the closeout BEFORE the print week)

```bash
cd "$(git rev-parse --show-toplevel)"
.venv/bin/python3 FORGE/tools/market-data/fetch.py fred ICSA      # last 5 weekly prints
.venv/bin/python3 FORGE/tools/market-data/fetch.py fred IC4WSA    # 4-wk MA (cross-check)
.venv/bin/python3 FORGE/tools/market-data/fetch.py fred CCSA      # continuing claims
```

Then fill the six variables below and run the pre-freeze check:

| Var | Meaning | How to get it |
|---|---|---|
| `W1..W4` | the four weekly prints in the CURRENT 4-week window (oldest → newest) | `ICSA`, newest 4 |
| `MA_cur` | current 4-wk MA | `IC4WSA` newest — **must equal `(W1+W2+W3+W4)/4`; if it does not, one of your W values is a stale vintage — stop and reconcile before freezing** |
| `R` | the week ROLLING OFF at the next print = **`W1`** | oldest of the four |
| `CC_cur` | continuing claims, level + obs week | `CCSA` newest |
| `n_kb` | Kill B count (`≤185,000` clean sessions, needs 5) | STATUS § KEY THRESHOLDS |
| `n_v7` | vector-7 count (`CC <1,750,000` consecutive weeks, needs 4) | STATUS § KEY THRESHOLDS |
| `n_v13` | vector-13 count (`<200,000` consecutive weeks, needs 4) | STATUS § CONVERGENCE MATRIX vector 13 |

**Derived, never copied:**
- `MA_next(X) = (W2 + W3 + W4 + X) / 4`
- **`ΔMA(X) = (X − R) / 4`** ← the mechanical term. **Sign flips at `X = R`.**
- **Solve the T-01 MA bound:** `X > 1,000,000 − (W2+W3+W4)` — it moves every week with the window.
- **Write out the division** in the card (root OUTPUT RULES (a)): `(X − 212)/4`, with `R` substituted, not `(X − R)/4`.

```bash
.venv/bin/python3 AGENTS/LABOR/scripts/card_partition_check.py AGENTS/LABOR/docket/GRADING_CARD_<YYYYMMDD>_claims.md
```
**Reading the exit code — use the tool's own semantics, do not invent a stricter or looser one:**
- **rc=0** — every band table it identified partitioned, and prose agreed. Freeze.
- **rc=2 with a `DEFECT`** — ⛔ **do not freeze.** Fix the table.
- **rc=2 with only `UNVERIFIED`** — the tool is refusing to certify what it could not check. **Not a pass.** Hand-verify *that specific table*, **write the proof onto the card**, and freeze only then.

🔧 **Known, expected UNVERIFIED on every claims card (BD-31):** the checker reads **one file-global** `partition-axis` declaration and applies it to all tables, so a card with two band tables on different axes (initial claims **and** continuing claims — the shape of every claims card) can machine-verify only one. **Declare the initial-claims axis** (load-bearing, 5 bands) and hand-prove the CC dichotomy — `< 1,750,000` / `≥ 1,750,000` are complementary by construction, so they cover the axis at any precision. Expect `1 verified, 1 unverified, 0 with defects`. **`0 with defects` is the number that must hold.**

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE  *(REGENERATE — never copy)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest | `W4` | | FRED `ICSA` [DOL] |
| 4-week window (oldest→newest) | `W1 / W2 / W3 / W4` | | FRED `ICSA` |
| 4-week MA | `MA_cur` | | FRED `IC4WSA` |
| Continuing claims | `CC_cur` | | FRED `CCSA` |

**Reconciliation (mandatory, show the division):** `(W1+W2+W3+W4)/4 = MA_cur` ✅/❌
**Vintage note:** state any W value that differs from what STATUS carries, and say which is right.

---

## §2 — PRE-COMMITTED BANDS *(stable half — carry verbatim unless a STATUS threshold moved)*

Bands are keyed to `STATUS.md` § KEY THRESHOLDS. **They must PARTITION the axis** — no gap, no overlap, no unenumerated branch (L-17/L-18: the NFP card's §3b failed to enumerate the branch that printed, and the correct response was to take zero score rather than improvise a band on the morning).

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count `n_kb` → `n_kb+1` of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → 3 |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

---

## §2b — THE OTHER TWO AXES THE SAME PRINT MOVES *(added 2026-09-07 from CODEX review — carry ALWAYS)*

🔴 **§2 partitions the SINGLE-PRINT axis. It is not the whole verdict.** At least two other decision rules key on the same number at boundaries that are **not** §2 band edges, so a card listing only §2 will label a state-changing print "NO ACTION". **Grade all three axes independently; a print can be quiet on one and state-changing on another, and that is not a contradiction to be resolved by picking one.**

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->

| V13 | Initial claims, single print (vector-13 axis) | Assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | vector-13 `<200,000 ×4` counter `n_v13` → `n_v13+1` of 4 (**independent of** band A's Kill B leg — both can apply to one print) |
| **V13-b** | ≥ 200,000 | counter **resets to 0 of 4** — the streak must be consecutive, and `200,000` is not `<200,000` |

**T-01 is an MA-basis trigger and can fire on THIS print.** Solve it every week — the crossing point moves with the window:
`(W2 + W3 + W4 + X)/4 > 250,000` ⟺ **`X > 1,000,000 − (W2+W3+W4)`**. Write the solved number into the card.

| T01 | Initial claims, single print (T-01 MA axis) | Assignment |
|---|---|---|
| **T01-a** | ≤ *(solved bound)* | 4-wk MA ≤ 250,000 ⇒ T-01 does not fire on the MA basis |
| **T01-b** | ≥ *(solved bound + 1,000)* | 🔴 **T-01 FIRES on the MA basis → CARL + REGINALD**, *in addition to* whatever §2 band the print lands in |

⚠️ **ROUTING UNION:** a print can fire T-01 **and** T-02. T-02 routes REGINALD + HENRY; T-01 routes **CARL** + REGINALD. **Take the union — omitting CARL from a joint fire is the §7 defect Amendment 1 of the 9/10 card had to correct.**

🔧 **Checker scope:** each added axis is another band table, and `card_partition_check.py` reads **one file-global declaration** (BD-31), so expect `1 verified, N unverified, **0 with defects**`. **`0 with defects` is the gate.** Hand-prove each unverified table on the card — two-band ones are complementary dichotomies, exhaustive at any precision.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED  *(REGENERATE — this is the card's main job)*

**`ΔMA(X) = (X − R)/4`.** The MA falls for `X < R`, is unchanged at `X = R`, rises for `X > R`.

⚠️ **`R` is a WEEKLY PRINT, not a band boundary — so the decline/rise line almost never coincides with a band edge, and it CUTS ACROSS whichever band contains `R`.** Name that band explicitly and say which part declines. Do not write "the MA declines in bands X, Y, Z" unless every one of those bands lies wholly below `R`; that sentence is what BD-30 was opened for.

| Worked point (not a band) | `X` | `MA_next` | `ΔMA` |
|---|---|---|---|
| Kill-B edge | 185,000 | | |
| Modal / last print | `W4` | | |
| **Zero-change point** | **`R`** | `MA_cur` | **0** |
| Accelerating edge | 230,000 | | |
| T-02 edge | 301,000 | | |

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(attribution discipline, BOTH directions — stable half)*

- **A single weekly print is a realization gauge, not a demand-vs-supply discriminator.** It cannot separate the two sides of the CORE TENSION on its own.
- **Cohort attribution floor (L-08):** a WARN cohort must be **≥ ~20,000** (≈10% of a weekly claims print) to be nationally visible. Below that, **no national claims move is attributed to it in either direction, in any week.** Name this week's cohorts and compute `cohort/20,000` explicitly.
- **A benign print is not hawkish fuel — it is nothing** (7/29 FOMC grade: labor is a satisfied side-constraint, not a policy input).
- **Rate path / market repricing are not mine** → BOND, HENRY, ORACLE.
- **Revision jitter:** the prior week revises with this print. **The `ΔMA` term is recomputed against the AS-PUBLISHED vintage on print morning BEFORE the new level is read** (L-02) — a frozen threshold computed off a revisable series is not actually frozen.

---

## §5 — CONTINUING CLAIMS *(separate letter — do NOT fold into the initial-claims band)*

| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | vector-7 drop-to-2 count `n_v7` → `n_v7+1` of 4 |
| **CC-2** | ≥ 1,750,000 | count **RESETS to 0 of 4** (the streak must be consecutive) |

⚠️ CC is a **cost/duration** gauge, not an early-warning instrument, and will not be used as one.

---

## §6 — ROUTING (pre-committed — stable half)

| Outcome | Route | Priority |
|---|---|---|
| Band E (T-02) | **WALTER** (signal) → REGINALD, HENRY | 🔴 |
| Band D (ARM T-01) | **WALTER** (signal) → CARL, REGINALD | 🟠 |
| Band C | STATUS only; note in brief | 🟡 |
| Bands A / B | STATUS only — **no packet** (silence = received and integrated) | — |

---

## §7 — DEFECT LOG *(fill at grade time — write defects in MY OWN work, not the data's)*

## §8 — GRADE *(written at grade time, off this frozen card — never re-read a band)*
