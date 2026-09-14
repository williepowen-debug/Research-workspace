# BOND — RUN RECEIPT (overwritten each run)

**Session:** 2026-09-14 (Mon) ~13:0x–15:4x ET · **PROME WQ-184 Tier-1 L0 spawn, DOCKET L357** · markets OPEN · desk was dark 9/10→9/14. **CLOSED OUT at Will's word (terminal shutdown), 15:4x.**

## Tasked deliverable — DISCHARGED
🔴 **`BND-22` GRADED FALSE**, breached by 5bp (`DFII10` **2.55 [2026-09-10]**, +9bp in one session). Pre-written `If_Falsified_Action` executed in full: breach protocol steps 1–5, decomposition, **no add, no proposal, `$0` moved.**

## Data provenance
All load-bearing figures pulled at BOND's **own** primaries — `boot_recompute.py` cache-busted **13:03 ET**, `fetch.fred_fetch` with explicit limits, NY Fed `/pd` API, live yfinance. PROME's relayed figures were **re-pulled, not adopted** (root rule #4); all reproduced exactly.

## Work delivered
| # | item |
|---|---|
| 1 | `BND-22` FALSE + calibration write-up (55% on the wrong side; *the row out-argued its own number*) |
| 2 | 🔴 **Spec defect escalated to Will:** the add-gate's "sustained" has **no session count** ⇒ unfireable, and it does not fail safe. **Count NOT set by me** — the level is already through. `WQ-246`. |
| 3 | **LEVEL vs SUSTAINED answered:** TERRY's card is right, mine is the underspecified one; both terminate at NO ADD today |
| 4 | **WQ-157 leg ② premises CLOSED, both favourably** — ceiling **n=244** (VERIFIED); SBN pooling **defensible** (INFERRED) ⇒ the 2022–23 stress half survives |
| 5 | **The PATH read** — the curve prices **~115–130bp more tightening**, terminal ~4.75–4.95%, no cut in 3yrs; asymmetry runs **against** a short-duration book |
| 6 | **Book RE-ARMED: 5 predictions pre-FOMC**, each base-rated *before* the confidence; one candidate **declined as padding** |
| 7 | **Two self-corrections** — the CCC leg/gap conflation, and the withdrawn buyback-cover inference |

## Checks
| check | rc | |
|---|---|---|
| `kb_lint` | **0** | ✅ |
| `closeout_check` (3/3) | **0** | ✅ — its FILE-STATE leg caught my own SCRATCH line going false mid-session |
| `docket_check` | **0** | ✅ *(was 1 — four undocketed 9/22–24 CUSIPs added)* |
| `corrections_boot_check` | **0** | ✅ *(was 1 BLOCK — `COR-20260910-02` receipted APPLIED)* |
| `read_cap_check` | **0** | ✅ *(STATUS and PREDICTIONS both rotated back under budget)* |
| `boot_recompute` | **1** | ⚠️ **DECLARED RESIDUE** — literal matches on correctly-labelled dated history. **Expected rc=1 next boot; read the SCRATCH residue note BEFORE "fixing" it.** |

## Mail
**General inbox 3 → 0** (PROME · MIDAS · RED). **WALTER lane 16 → 0 in TWO waves** — 6 at boot, **10 more arrived mid-session**. Both `action:` items handled (`SIG-014` buyback underfill; `SIG-010` GPIF capacity). **Out: 3 packets** — TERRY, WALTER, PROME.
⚠️ **With a live WALTER, an inbox count is a MOMENT property, not a session fact.**

## Position
⛔ **UNCHANGED — TLT puts HOLD, no add, `$0`. No order, no threshold set, moved or shaved.** Will's 7/16 NO-ADD · `WQ-168 ④` · root rule #5.

## Owed after this session
🔴 **WILL:** the add-gate's "sustained" session count (`WQ-246`).
🔴 **BOND next boot:** grade `BND-25`/`BND-26` off the 9/16 session · `BND-28` ceiling **9/18 17:00 ET** · **9/15 20Y-R** (`I'` 61.72, downgrade counter's 3rd chance at 2) · **9/16 FOMC + SEP** (pre-registered falsifier: terminal ≥~5.00% ⇒ my asymmetry read is wrong) · **9/18 FR2004 join — premises closed, build UNSTARTED** · reply to RED on FT-11's relative leg · CME-primary priced probability.
