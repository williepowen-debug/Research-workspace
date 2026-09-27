# VLY — does the property/market evidence on file transfer to its book? (WQ-311, CREED leg)

**Written:** 2026-09-27 (Sun), CREED, on PROME task **WQ-311** (Will 19:04 ET). My leg: challenge the property comparisons behind REGINALD's reading of VLY's exposures; six-dimension transfer grade per class; compare to FLG (the fleet's NYC rent-regulated reference); state whether the *property evidence* supports broader / bank-specific / neither, with the strongest contrary evidence.
**Under test:** `AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md` part (1) (`6e21a2c37`; VLY Q2-26 deck s29–32 + 10-Q, 6/30). Parts (2)–(4) not yet landed; the early part-(2) MF-DPD signal is used as flagged-preliminary.
**Reuse only** (9/26 vulnerability map, the transfer test `cd4674c5e`, the Signature file `c0461e5b5` with its §D correction). No new pulls. **No CREED band, score, threshold, tool or trade change.**
**Two anchoring cautions from PROME, applied up front:** ① VLY "clean credit" is the stale 8/20 matrix reading and is **withdrawn** — REGINALD's cross-bank report (`f2ba5de14` §A3) has VLY among the 7/14 banks whose CRE bad-loan rate *rose* 6/30/25→6/30/26; I test deterioration, not carry cleanliness. ② The Signature ~60%-of-book figure is **conditional** (on the FDIC's undefined "N/A" = unlevered) and its bias directions are hypotheses — used here only as a Dec-2023 *valuation* reference for the NYC rent-regulated slice, never a gap or a rate.

---

## §0. The answer first

1. **On composition, the property evidence does NOT support broader CRE-to-bank stress at VLY.** The channels that drive the national thesis — office CMBS maturity failure and the NYC rent-regulated rent-freeze — are **small** at VLY: office is 11% ($3.0B, Manhattan just $0.2B, DSCR 1.83×), and the ">50% rent-regulated" book is **$559M (1.1% of loans)**. The book is diversified, **low-LTV (59%)**, **high-DSCR (1.67×)**, and its concentration is **falling fast** (474%→317% in 2.5yr), with ~25pp of it low-loss co-op lending (12% LTV). This is the opposite risk shape to FLG/EGBN/OZK.
2. **But there is one real deterioration signal, and it is not yet placeable:** multifamily 30–89-day past-due jumped **$9.4M → $101.5M** in Q2 (Call Report; REGINALD's "few larger CRE loans"), plus one office loan ($25.8M) to nonaccrual and one MF loan ($6.8M) modified at the Q2 maturity wall. **Location and type are unidentified.** That single fact decides between *idiosyncratic/bank-specific* and *the leading edge of the national multifamily cash-flow deterioration* (HOMER's Freddie MF DQ 0.64%, 4th rise). **Until it is placed, the honest verdict is NEITHER-yet, leaning bank-specific/benign on the composition.**
3. **VLY is not "a small FLG."** It resembles FLG *only* in the small NYC rent-regulated slice (type + market), and even there is **better-covered** (NYC MF DSCR 1.24× vs FLG's 1.01×) and **~1/16 the size** on the narrow ">50%" book ($559M vs $8.9B; ~1/6 on the broad ≥21%-regulated ~$1.5B reading). The FLG transmission thesis does not transfer to VLY at any material scale.
4. **Most fleet realized comps DO NOT transfer to VLY** — they are CMBS trophy/gateway office and regional-mall loans; VLY's book is small-balance ($3.5M avg office), suburban-weighted, FL-heavy (28%), well-covered bank CRE.

---

## §A. OBSERVED — VLY's exposure classes (REGINALD part 1, VLY primary) and the fleet evidence that could bear on each

| VLY class (6/30/26) | $B | Wtd LTV | Wtd DSCR | Fleet market evidence on file that could transfer |
|---|---:|---:|---:|---|
| Apartment/residential (non-co-op MF) | 7.1 | 64% | 1.34× | HOMER Freddie MF DQ 0.64% (4th rise, national **cash-flow/A**); FL MF (CORAL, insurance-cost→NOI); NYC rent-reg subset below |
| — of which **NYC >50% rent-regulated** | **0.559** | — | **1.24×** (NYC MF) | FLG's NYC rent-regulated book; June-2026 rent freeze (RGB #58); **Signature 2023 ~60% implied valuation (conditional)**; BCB NJ/NY ≤79% |
| — plus 21–50%-regulated band | ~0.93 | — | — | partial rent-freeze exposure (same channel, diluted) |
| Retail | 4.2 | 61% | 1.67× | Retail SS 13.60% / DQ 7.20%; mall maturity defaults (**CMBS regional malls**) |
| Healthcare | 4.1 | 69% | 1.69× | ~none on file (not a CREED-tracked stress lane) |
| Specialty & other | 3.1 | 54% | 1.79× | ~none |
| **Office** | **3.0** | 63% | 1.83× | Office CMBS DQ 12.00%, DC/NoVA cluster, realized −61/−72% (**CMBS trophy/gateway**); Manhattan slice $0.2B @74% LTV |
| Industrial | 2.9 | 60% | 2.17× | Industrial DQ 1.14% — the **counter-signal** (clean) |
| Co-ops | 1.8 | **12%** | 1.50× | none needed — blanket mortgage on a co-op, structurally low-loss |
| Mixed use | 1.6 | 63% | 1.31× | thin (single-name SASB moves in the tape are not VLY-type) |
| Construction (separate) | 2.5 | — | — | OZK construction/life-sci stress — **wrong product** (VLY construction not life-sci disclosed) |
| **Geography:** FL/AL 28% ($7.8B, DSCR 1.81×) · other 21% · NJ 19% · NYC 25% ($6.9B) · Manhattan $2.6B (41% LTV incl co-ops) | | | | FL = CORAL lane (credit quiet in Trepp prose, but insurance-cost→NOI channel live); NYC = FLG/tape lane |

**Deterioration signal (early part-2, flagged preliminary):** MF 30–89 DPD $9.4M→$101.5M in Q2; one office $25.8M → nonaccrual; one MF $6.8M modified. **Location/type not identified.**

---

## §B. SCENARIO ASSUMPTIONS — six-dimension transfer grade, per class

Legend: ✓ match · ~ partial · ✗ no match. Dimensions: **type · market · vintage · appraisal date · lien · performing-vs-defaulted.**

| VLY class | type | mkt | vint | appr | lien | p/d | Does fleet evidence transfer? |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **NYC >50% rent-regulated ($559M)** | ✓ | ✓ | ~ | ~ | ~ | ~ | **PARTIAL — the FLG channel is real here but immaterial at scale.** Type/market match FLG and the June-2026 freeze applies. But it is **1.1% of VLY loans**, DSCR **1.24× vs FLG 1.01×** (better-covered), and **1/16 of FLG's $8.9B**. The **Signature ~60% Dec-2023 implied valuation** is available as a *valuation direction* (conditional on N/A=unlevered; both caveats), **not a loss rate**. |
| **21–50%-regulated (~$0.93B)** | ~ | ✓ | ~ | ~ | ~ | ~ | **WEAK/PARTIAL.** Diluted freeze exposure; no fleet comp is struck at this partial-regulation level. |
| **Other apartment/MF (bulk of $7.1B; FL, NJ, other)** | ✓ | ~ | ~ | — | ~ | ~ | **PARTIAL by TYPE only.** HOMER's national MF cash-flow signal (Freddie 0.64%, rising) transfers to *multifamily as a type* and is the **best match to VLY's MF-DPD jump** — but I cannot place VLY's specific loans without location/type. FL MF is CORAL's lane (insurance-cost→NOI), not on national data. |
| **Office ($3.0B; Manhattan $0.2B)** | ✗ | ~ | ✗ | ✗ | ✗ | ✓ | **DOES NOT TRANSFER.** The national office stress is **CMBS trophy/gateway** (205 W Randolph, DC/NoVA SASB) and realized comps are sale-vs-purchase, not loss rates. VLY office is **small-balance ($3.5M avg), suburban-weighted, 1.83× DSCR**. Only the $0.2B Manhattan slice (74% LTV) has any market overlap, and it is trivially small. |
| **Retail ($4.2B)** | ✗ | ~ | ✗ | ✗ | ✗ | ✓ | **DOES NOT TRANSFER.** Fleet retail evidence is **regional-mall CMBS** (Yorktown, Meadows, Sangertown). VLY retail (1.67× DSCR) is almost certainly neighborhood/strip small-balance — wrong subtype. |
| **Industrial ($2.9B)** | ✓ | ~ | — | — | ~ | ✓ | **TRANSFERS as the counter-signal.** Industrial credit is clean fleet-wide (DQ 1.14%); VLY's 2.17× DSCR confirms it. Evidence *against* stress. |
| **Healthcare / specialty ($7.2B)** | — | — | — | — | — | — | **NO FLEET COMP.** Not CREED-tracked lanes; ungraded. |
| **Co-ops ($1.8B, 12% LTV)** | ✗ | ~ | — | — | ✓ | ✓ | **NO STRESS TRANSFER.** Structurally low-loss; inflates the SR 07-1 ratio (~25pp) without carrying the risk. |

**Pools where no defensible comparable exists (named):** healthcare, specialty & other ($7.2B combined) — no fleet market evidence bears on them. Retail and office have fleet evidence but it **fails to transfer** (wrong loan type/subtype), which is different from "no comp" — I hold comps, they just don't fit VLY's book.

---

## §C. VLY vs FLG — where they resemble and where they differ

| Dimension | FLG (fleet NYC rent-reg reference) | VLY | Read |
|---|---|---|---|
| NYC >50% rent-regulated | **$8.9B** | **$559M** | VLY ~1/16 the size; the channel exists but is immaterial to VLY's bank |
| NYC MF coverage | DSCR **1.01×** | DSCR **1.24×** | VLY better-covered on its weakest MF |
| Portfolio LTV / DSCR | NYC RR 78% LTV / 1.01× | **59% LTV / 1.67×** (all CRE) | VLY far less levered, far better covered |
| Office share | mixed; NYC office a named risk | **11%, Manhattan $0.2B** | VLY minimal office/CMBS-cluster exposure |
| Geography | **NYC-centric** | **FL/AL 28%**, NYC 25%, NJ 19% | VLY is FL-weighted; different geography, different (CORAL) channel |
| Concentration trend | high, rent-freeze-driven forward risk | 317%, **falling 157pp in 2.5yr**, ~25pp co-op | VLY de-levering, not building risk |

⇒ **VLY resembles FLG only in the small NYC rent-regulated slice, and even there is smaller and better-covered. It is not a scaled-down FLG; its dominant exposures (FL, diversified low-LTV CRE, co-ops) sit outside the fleet's NYC-rent-regulated and office-CMBS stress channels entirely.**

---

## §D. UNKNOWNS

1. **Location and type of the $101.5M MF 30–89 DPD** — the decisive fact. NYC rent-regulated → the FLG channel (but small); FL → CORAL insurance-cost/cash-flow; scattered/national → HOMER's national MF cash-flow leading edge; concentrated in 1–2 names → idiosyncratic/bank-specific. **REGINALD part (2) should place it.**
2. **Whether the $559M ">50%" and ~$0.93B "21–50%" books are performing/criticized/nonaccrual** — REGINALD gives balances and DSCR, not credit tiers.
3. **VLY office by asset quality/vacancy** — only aggregate LTV/DSCR disclosed; the $0.2B Manhattan slice's building-level detail is unknown.
4. **FL/AL CRE cash-flow under the insurance-cost channel** — CORAL's lane; VLY's $7.8B FL/AL book (1.81× DSCR) is not visible in national data.
5. **Signature valuation-reference validity** — conditional on the FDIC's undefined "N/A"=unlevered (§Signature file §D); a valuation direction, not a rate.

---

## The verdict on the property evidence, and the strongest contrary evidence

**Property/composition evidence → NEITHER broad transmission NOR (yet) a confirmed bank-specific credit problem — leaning benign/bank-specific.** VLY's book is diversified, low-LTV, high-DSCR, de-levering, with the national stress channels (office CMBS, NYC rent-freeze) present only in small size. The property evidence does **not** support reading VLY as evidence of broader CRE-to-bank stress.

**Strongest contrary evidence (against the benign read — stated at full strength):**
1. **The MF 30–89 DPD jumped ~10× in one quarter** ($9.4M→$101.5M). 30–89 DPD is an **early** indicator that has not yet reached nonaccrual/loss — it could be the leading edge, not a blip.
2. **Multifamily is the one type where cash-flow stress IS rising nationally** (HOMER Freddie 0.64%, 4th rise), so a MF deterioration at VLY is *consistent with a real national signal*, not obviously idiosyncratic.
3. **NYC MF DSCR 1.24× is VLY's weakest** coverage — the thinnest cushion sits exactly in the rent-exposed book.
4. **CRE bad-loan rate rose 6/30/25→6/30/26** (REGINALD `f2ba5de14` §A3) — "clean credit" was stale; the direction is deterioration, not improvement.

**Why it still reads benign-leaning despite the above:** $101.5M of 30–89 DPD is **~0.2% of the $52.5B loan book / ~0.3% of CRE**; it is "**a few larger loans**" (concentration, not breadth); 30–89 DPD frequently cures; and the portfolio cushion (59% LTV, 1.67× DSCR) is deep. **The tie-breaker is the unidentified location/type of those loans** — which is why the verdict is "neither-yet," not "benign, closed."

**The next observation that would change the conclusion — named, with direction:** the **location and property type of the $101.5M MF 30–89 DPD loans** (REGINALD part 2 / VLY Q3). If **concentrated in 1–2 idiosyncratic credits** → bank-specific, benign for the thesis. If **spread across the NYC rent-regulated / FL MF book** → the leading edge of a broader multifamily cash-flow channel, and VLY becomes a *weak* corroborant of broader stress (still small in absolute size). Direction of the swing: identification toward **breadth** moves VLY toward "broader"; toward **concentration** moves it toward "bank-specific."

---

## Sources
- REGINALD VLY part (1): `AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md` (`6e21a2c37`) — VLY Q2-26 deck s29–32 + 10-Q, 6/30, primary; `f2ba5de14` §A3 (CRE bad-loan-rate rose).
- CREED reuse: `research/2026-09-26_CRE_VULNERABILITY_MAP.md` (§1 types, §3 holders, HOMER Freddie 0.64%); `analysis/2026-09-27_property-comparable-transfer-test.md` (`cd4674c5e`); `analysis/2026-09-27_signature-bank-2023-sale-economics.md` (`c0461e5b5`, §D conditional valuation).
- FLG reference: `AGENTS/FLG/STATUS.md` ($8.9B >50% rent-regulated).
