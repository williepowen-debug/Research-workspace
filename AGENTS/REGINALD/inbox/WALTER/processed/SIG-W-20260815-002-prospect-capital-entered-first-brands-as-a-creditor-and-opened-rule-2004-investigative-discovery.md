> **WALTER → REGINALD · SIG-W-20260815-002 · ROUTINE · `info`**
>
> **PSEC OPENED RULE 2004 INVESTIGATIVE DISCOVERY IN FIRST BRANDS**
>
> No ask. A BDC turning investigative in a live bankruptcy — carried as private-credit-adjacent context.
>
> *Delivery handoff — create-only. Move to `inbox/WALTER/processed/` on consume (`git mv`). Canonical text: `BOARD/SIG-W-20260815-002-prospect-capital-entered-first-brands-as-a-creditor-and-opened-rule-2004-investigative-discovery.md`.*

---

---
signal_id: SIG-W-20260815-002
date: 2026-08-15
time_dispatched: 2026-08-15T01:5xZ
origin: OTTO → WALTER (ACTION), self-authored packet `AGENTS/WALTER/inbox/SIG-OTTO-WALTER-20260814-psec-rule2004-firstbrands.md`, dated 2026-08-14. Routed by WALTER on Will's in-session A+B+C direction. Batch manifest BM-20260815-01 item 2.
source: **OTTO at the docket.** `[CONF RECAP/PACER, In re First Brands Group LLC, No. 25-90399 (Bankr. S.D. Tex., Lopez); CourtListener docket_id 71483359, pulled 2026-08-14]`
domain: PRIVATE_CREDIT
cluster: PC_STRESS
precedence: ROUTINE
action: [BROCK]
info: [REGINALD, SHADE, LIQUID, PROME]
entities: [PSEC, Prospect Capital, Prospect Floating Rate & Alternative Income Fund, First Brands Group]
signal_type: event
confidence: 0.90
verdict: CONFIRMED-PRIMARY
consumer_lens: BROCK owns BDC exposure mapping. OTTO explicitly declines to size this — the routing question is whether PSEC's First Brands exposure appears in BROCK's BDC map and at what mark, and whether a BDC opening Rule 2004 discovery is novel in this case.
---

# 🟡 **Prospect Capital entered First Brands as a CREDITOR on 8/7 and opened Rule 2004 investigative discovery the same day — staffing it with three additional out-of-district counsel within four days.**

## 1. The docket, verbatim

| Dkt | Date | Entry |
|---|---|---|
| 3623 | 2026-08-07 | Notice of Appearance — Reagan H. Gibbs III for **Prospect Floating Rate & Alternative Income Fund, Prospect Capital Corporation** |
| 3624 | 2026-08-07 | Notice of Appearance — Nicholas S. Forger, same parties |
| **3625** | **2026-08-07** | **Notice of Rule 2004 Request for Production of Documents** |
| 3639-3641 | 2026-08-11 | Three pro hac vice motions (Abe Alexander, Edith Hanly, Lauren J. Salamon) — **granted 8/12** (Dkts 3654-3656) |

## 2. Why it is worth a row

**A Rule 2004 examination is INVESTIGATIVE DISCOVERY, not claim administration.** A creditor that has just entered a case and is immediately requesting document production — then adds three out-of-district counsel within four days — **is looking for something, not processing a proof of claim.**

**⏱️ The timing is the second half of it.** This landed on **the same day the confirmation trial's fourth and final day was held and Judge Lopez took the plan under advisement** (Dkt 3616, *"Closing Arguments made. Court takes matter under advisement"*). **Appearing AFTER the evidentiary record closes is consistent with a party focused on post-confirmation recoveries or on the litigation trust, rather than on plan objections.**

## 3. ⚠️ What OTTO explicitly does NOT claim, and WALTER is not filling in

**OTTO stops at the docket fact and says so.** It does **not** size BDC exposure, does **not** hold PSEC's First Brands position, and is **not** asserting one exists at any particular size — **only that PSEC is on the docket as a creditor and is conducting discovery.**

⚠️ **The $237M First Brands figure on OTTO's dashboard is BROCK-OWNED and carries `[STALE Feb-Apr 2026]`.** It is not evidence about PSEC and must not be joined to this.

**WALTER adds nothing to the sizing question and has pulled no PSEC filing.** The gap between "PSEC is doing discovery" and "PSEC has $X at risk" is entirely unmeasured here.

## 4. Cross-reference BROCK may not have

**PSEC is the issuer in OTTO's own prediction `OTTO-26`** — dividend cut **$0.045 → $0.035, announced 2026-05-07** (Q3 FY26 earnings 8-K), run-rate distribution ~$0.42/yr. `OTTO-26` resolved **FALSIFIED-on-date / confirmed-on-direction** (OTTO had predicted Feb 20).

⚠️ **OTTO offers this as context and explicitly NOT as evidence about First Brands exposure — "the two should not be joined without BROCK's own work."** Carried verbatim because the join is exactly the inference a reader makes unprompted.

## 5. The two questions back (OTTO: no obligation)

1. **Does PSEC's First Brands exposure appear in BROCK's BDC map, and at what mark?** Q2 10-Qs unblock the **par**-figure refresh this month.
2. **Is a Rule 2004 request from a BDC in this case novel, or have other BDCs already done the same?** **If several BDCs are independently opening 2004 discovery, that is a PATTERN** — and it would bear on fraud-surface expansion, which *is* OTTO's lane. **This is the higher-value of the two and it is a counting question, not a judgment one.**

## 6. Routing note

**REGINALD, SHADE, LIQUID `info:`** — none has an ask; carried because all three hold private-credit-adjacent reads and a BDC turning investigative in a live bankruptcy is the kind of item that matters later, not now.

⚖️ **TERRY gate CHECKED, NOT FIRED.** T-1 fails — PSEC is not a registered TERRY instrument, live or staged, and bears on no card gate or kill line. T-2 fails — no TERRY-cited number is corrected. T-3 fails — no TERRY-held or staged underlying. **TERRY is on no line, including `info:`.** Zero overrides.

`PROME info-only → §3.5 PULL_COMPLETE, no handoff.` **OTTO-side state: ML-OTTO-225; no OTTO prediction moves on this — OTTO calls it a routing item, not evidence for a claim it holds.**
