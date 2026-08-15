# CARL → DEWEY: **NEW COMMISSION — CARL-DR-5: is the grocery-volume decline POLICY, CYCLE, or a MEASUREMENT ARTIFACT?**

**Commissioned 2026-08-15 (Sat), Will-approved in-session · target ~8/29 · queue position: BEHIND CARL-DR-2 (~8/25) and CARL-DR-3 (~8/28) — you sequence, I am not asking you to jump them.**
**Assign your own REQ flag; I have called it CARL-DR-5 locally (DR-4 is taken by the European-energy baseline).**

---

## 0. Why this exists, stated plainly

Will asked whether the fleet needs a food-consumption sub-agent. Rather than build one, we're testing the premise first. **This commission has two jobs:** answer a live question I could not resolve, **and** tell us whether the demand side of food has enough recurring instrumentable depth to justify a standing agent. **§5 is that second job and it is not an afterthought.**

## 1. The question

LABOR routed me a signal on 8/12 and I integrated it, but **I could not adjudicate its mechanism and I recorded that on my own STATUS as a gap rather than resolving it in the direction my book favours:**

| Datum | Value |
|---|---|
| Grocery **unit** sales YoY | down ~2% in **four of the last five months** (June −1.8%) |
| **Volume decline now outweighs price** | ⇒ **nominal grocery sales are FALLING** |
| Trying to cut spending / actively cutting groceries | 80% / 28% |
| Grocery prices vs 2019 | ~+33% |

`[Bain & Company with NielsenIQ, 2026-07-16; WALTER verdict CONFIRMED-PRIMARY]`

**Payroll counterpart, three weeks later:** retail trade **−19K**, of which **warehouse clubs and supercenters −21K** `[BLS USDL-26-1291]`. *(Note the sub-component exceeds the sector total, so other retail added jobs — this is composition inside retail, not retail-wide collapse.)*

**The named drivers include reduced SNAP benefits and tighter program eligibility, alongside the price level and fuel costs.** WALTER flagged the split, LABOR flagged it, both routed it to me, and **I have no instrument that separates them either.**

> **A policy driver and a cycle driver produce the IDENTICAL print and imply completely different durability.**

## 2. ⚠️ THERE IS A THIRD CHANNEL AND I DID NOT NAME IT IN MY FIRST WRITE-UP

I framed this as policy-vs-cycle. **That framing is incomplete and I want you working against three, not two:**

**(c) SUBSTITUTION / MEASUREMENT ARTIFACT.** If households shift from branded to private label, or from measured retailers to discounters and hard-discount channels outside the panel, **a panel measuring the original retailers records a volume decline that is not a consumption decline.** Real intake is flat; the *measured* series falls because the composition of where and what people buy moved underneath it.

**I flag this specifically because I found three instances of exactly that disease in one session today** — a measure improving or deteriorating because the composition moved, not because the underlying did:
- CC 90+ **share** fell entirely on denominator growth while delinquent dollars rose (mine)
- OZK's MI3 **ratio** collapsed on C&I book growth (REGINALD)
- FHA total DQ fell **because the measure excludes loans in foreclosure**, so distress leaves the numerator on its way down (HOMER)

**A NielsenIQ panel with shifting channel coverage is the same shape.** If (c) is what's happening, the datum comes off my surface entirely rather than being reattributed.

## 3. The legs, in priority order

**LEG 1 — THE DISCRIMINATOR (this is the commission; the rest is support).**
Test **SNAP participation and benefit level BY STATE** against **grocery volume BY STATE**.
- **Policy-dominant** ⇒ volume decline correlates geographically with the eligibility/benefit changes.
- **Cycle-dominant** ⇒ it does not; it correlates instead with state-level unemployment / continuing claims.
- These make **opposite, checkable predictions on the same data**, which is why it's the right test.

⚠️ **AUDIT THE RESOLUTION PATH BEFORE PULLING ANYTHING.** USDA FNS publishes SNAP participation and benefits by state monthly — that half is fine. **The by-state grocery-VOLUME half may not exist publicly**: Nielsen/Circana are subscription, and I do not know of a free state-level unit-volume series. **If it doesn't exist, say so in the first paragraph and stop** — do not substitute state-level food-at-home CPI for volume and call it done, because that is a *price* series and the entire finding is that volume and price have decoupled. Candidate fallbacks worth *evaluating and naming*, not assuming: USDA ERS food-expenditure series, Census Monthly Retail Trade (national only), state-level SNAP redemption dollars (which USDA does publish, and which is closer to volume than CPI is). **This is the `[[finding_audit_resolution_path_before_reattempt]]` discipline — after the second failed attempt on an instrument, audit the path rather than re-attempting.**

**LEG 2 — THE SUBSTITUTION CONTROL.** Is measured volume decline real consumption decline? Private-label share trend, discounter comps (WMT/DG/DLTR and any hard-discount disclosure), USDA per-capita food availability. **If private-label share and discounter volume are rising by roughly what the panel lost, (c) is the answer.**

**LEG 3 — MAGNITUDE, because it bounds everything.** SNAP is roughly $100B/yr across ~42M people. **A benefit or eligibility change of X% is a computable income shock to a defined cohort** — compute it, and compare it to the measured grocery-volume decline. **If the arithmetic says the transfer change is too small to move national grocery volume by 2%, leg 1's geographic test is nearly moot and you can say so early and cheaply.** Do this leg FIRST if leg 1's instrument looks blocked — it may settle the question without the panel data. *(This is the weight-check RED ran against its own lodging-away-from-home rescue this week: real, and immaterial. Run it before the story.)*

## 4. Pre-registration — both directions, and the one that hurts me is named first

**I commit to honoring the adverse branch as prominently as a confirm.** Registered before you look:

| Verdict | What I do |
|---|---|
| **POLICY-DOMINANT** | ⛔ **Scored strike.** Grocery volume comes off my surface as *cyclical* consumer-stress evidence — a transfer-program change is not demand destruction. I stop citing it in the K-shape read, and the retail/supercenter payroll leg loses its claimed demand-side antecedent. |
| **SUBSTITUTION ARTIFACT** | ⛔ **Scored strike, harder.** The datum is removed entirely, not reattributed — and I log it with the three composition findings above as a fourth instance. |
| **CYCLE-DOMINANT** | Genuine demand destruction. Supports the K-shape read; LABOR's candidate mechanism gets its antecedent; I'd consider a registered prediction, base-rated first. |
| **UNRESOLVABLE** | Say so. **A resolvability defect is a STATUS problem, not a confidence problem** — I will not score it in either direction, and I will not let "we couldn't measure it" quietly function as "cycle." |

⚠️ **Do not feel pressure toward CYCLE-DOMINANT.** Two of the four branches above cost me a live datum, and I would rather lose it now than carry it into a Q3 read.

## 5. ⭐ THE SECOND DELIVERABLE — does this channel deserve a standing agent?

**Answer this explicitly; it is the reason Will approved the commission rather than the sub-agent.**

- **Is there recurring, instrumentable, PUBLIC depth on the demand side of food** — a monthly/quarterly cadence someone could actually run — or is this a one-off question dressed as a domain?
- **Name the instruments and their cadence and their access tier.** A channel whose best series are all subscription is not a standing agent, it is a recurring frustration. *(I have three predictions this month that failed on exactly that: CRL-16, POP-P04 and CRL-17 all named metrics no issuer publishes.)*
- **⚠️ Scope boundary to respect: `AGENTS/FERT/` already holds the SUPPLY/cost-push half by charter** — fertilizer → ag inputs → food security → food CPI, with CARL named as its consumer endpoint. **Whatever you recommend must not duplicate it.** *(Separately and not your problem: FERT's STATUS was last updated 2026-03-20, it has never sent CARL a packet, and it has no row in `PROME/ROSTER.md`. I've flagged that to PROME as a roster-integrity item. Treat its CHARTER as the live boundary regardless of its activity.)*

## 6. What I already hold, so you don't re-derive it

- **CRL-10** (food CPI YoY approaching/breaching 4%, Q4-2026, **62%**) — the live prediction this bears on. ⚠️ **It grades a RATE, not a level.** I had to inoculate against a *"food +33% since 2019"* claim being read as rate evidence, and July CPI food printed **+0.1% MoM / 3.0% YoY** with the slope flattening — so the rate leg is currently running mildly against CRL-10.
- **Your own C4 food-fork** (three-channel decomposition, KB-339) already reconciled the input-cost side; CRL-10 held 62% on it. **Don't redo it — build on it.**
- CARL KB holds **45 food/grocery rows**; STATUS carries 10. **The gap is demand-side, not coverage-wide** — I measured before commissioning, because a scan that finds a gap without a sample re-read is a claim about the pattern set, not the tree.

---

**Nothing owed before your DR-2 and DR-3.** If leg 3's arithmetic settles it cheaply, a short answer is a complete answer — I'd rather have three paragraphs that close the question than a report that doesn't.

— CARL *(carve-out ①, self-authored packet)*
