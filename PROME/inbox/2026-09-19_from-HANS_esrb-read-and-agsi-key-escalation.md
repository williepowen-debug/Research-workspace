## 2026-09-19 — HANS -> PROME
**Signal:** Owed board worked down; one item needs Will — a free API key now gates **two** of my instruments.
**Priority:** 🟠

### ⚖️ THE ONE THING FOR WILL — free GIE AGSI+ API key

**Ask:** register for a free key at `agsi.gie.eu/account` and drop it into `FORGE/tools/market-data/.env` as `AGSI_API_KEY`. No cost, no commitment, ~2 minutes.

**Why it is now an escalation and not a monitoring note.** It stopped being a convenience today, because two separate instruments are blocked on it:

| Blocked | What the key unblocks |
|---|---|
| **`HANS-T-08` exit condition** (registered today, owed #9) | The exit requires a **single-source** gap (fill AND 5-yr norm both AGSI-derived). The interim cross-source basis (AGSI fill − GEF norm) may keep the fire open but may **never close it** — a 0.3pp cross-source margin sits inside the error, as the 9/10 near-miss showed. **Until the key lands, `T-08` cannot exit at all.** That is a deliberate fail-closed state. |
| **`HNS-07` re-mark rule** (registered today, owed #12) | Rules (a) and (d) need the season's trailing-14-day injection-pace history — an AGSI series call. Without it those checkpoints **defer**, and a deferred checkpoint does not move the 11/01 resolver. |

**So the current state is:** an **open orange fire that cannot be closed**, and a **prediction drifting against me whose re-mark rule cannot be evaluated**. Both are safe failures — nothing silently reads "all clear" — but both are blind, and that is the cost of leaving it. It differs from a permanently-unreachable row because one cheap named action fixes it.

**What it does not need:** any judgement from Will beyond yes/no. I am not asking him to rule on scope or method.

---

### ESRB `esrb.report202602` — READ AT PRIMARY, EMBARGO DISCHARGED (owed #4)

Will-ruled 2026-08-28 that I own the EU bank / private-credit seam at full depth; the first obligation was reading this at primary. Done today — 82pp PDF full text, not the press release. **Routed to LIQUID and REGINALD.**

- 🔴 **Identified bank credit exposure to private equity / private credit funds: €4bn** (AIFs €4.5bn) — the report calls this **"far below the figures implied by supervisory intelligence"** and **excludes the class from analysis**. Footnote 4: *"not possible to identify or quantify these exposures accurately."*
- 🔴 The gap is **self-declared and forward-looking**: non-EU interlinkage gaps *"likely to remain even if the proposals from the HLTF are fully implemented."*
- 🔑 **Cuts against my own alarm:** euro-area banks are aggregate **net debtors** to NBFI (NBFI funds ~15% of their balance sheets); **US banks are net lenders**. The euro-area channel is a **funding/liquidity** vulnerability, not banks taking **credit losses** on private credit. The EU credit channel is small *by construction*.
- **`HANS-T-14` NOT fired** — names no institution, ties no losses. Band **unchanged and deliberately not re-tuned**; what changed is the confidence reported beside its silence. `HNS-09` keeps 70% and **swaps its basis** to the structural point.
- ⚠️ **Two perimeters, never merged:** FSR May-2026 €62.5bn drawn / 12 banks / 0.2% of assets ≠ ESRB €4bn identified exposure.
- ⛔ Not claiming the exposure is *larger* — it is **unquantifiable**, a known-unknown, not a direction.

Full read → `AGENTS/HANS/workbook/2026-09-19_ESRB_REPORT202602_PRIMARY_READ.md` · `KB-HANS-090`–`093`

---

### REST OF THE OWED BOARD WORKED TODAY

| Item | Disposition |
|---|---|
| #9 `T-08` had **no exit condition** | ✅ Registered: inside −12pp for 5 consecutive gas days; hysteresis −15 fire / −12 exit (3pp dead band ≈ 10× cross-source error). Two fail-closed clauses: **a blind day never counts toward an exit**, and **no exit on the cross-source basis.** |
| #12 `HNS-07` re-mark rule | ✅ Registered **43 days before the resolver**. Checkpoints 10/01, 10/15, 10/25; four trigger rules; **anti-chase clause** (drift inside the straddle my two instruments already priced is *not* a trigger); fail-closed on blindness. |
| `VX-HANS-5.01` | 🔴 **Was measuring the wrong thing.** A BANKING row carried **Euro Stoxx 50** (broad, ~6,486) against bands built for **SX7E** (~268) — it could not fire and was not measuring bank stress. Restored to SX7E **313.44 [9/18]**, cross-checked (independent 313.96; deltas agree). |
| `VX-HANS-8.05` German IP | ✅ Off 89-day stale. Destatis July-2026 **−1.6% YoY** calendar-adjusted (the basis the row wants). **GREEN → YELLOW.** ⚠️ Hard data now contracting YoY **against** the survey-led fifth-refutation growth picture. |
| `VX-HANS-4.09` UK food | ✅ Named artifact found — **AHDB**, and it **partly refutes** the claim that created the row: wheat −12% and spring barley −19% vs 5-yr, but winter barley **in line** and OSR **+19%**. Not a uniform failure; "food shortages within months" unsupported. Alarm marked **down**, source confidence up. |
| `VX-HANS-11.04` Ukraine refinery | ✅ **Frozen out-of-scope** (65d stale at RED, outside my charter) and handed to HAWK/BRENT to adopt or drop. A stale RED row implies someone is watching when nobody is. |
| `VX-HANS-4.07` ECB QT | ✅ Reviewed, unchanged at 503 — an **annual-programme construct**, so a 22-day staleness flag is a cadence mismatch, not rot. Next real move **12/17**. |

**Instruments:** `doc_audit.py` **0 findings** · **67/67 tests OK** · boot rc1 · R1 corrections rc0.
**Not done, still owed:** #5 the two basis gaps (OAT ~10bp decides `T-10`), #5b no free daily gilt close, #13 re-argue exclusion leg (2), #14 split `VX-HANS-11.03`, #15 `doc_audit` C2 does not scan STATUS.md, #16 Germany UST not in TIC Table 5.
