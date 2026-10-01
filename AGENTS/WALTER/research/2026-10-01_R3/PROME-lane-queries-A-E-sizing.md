# Sizing of PROME's five drafted lane queries (A–E) · run 2026-10-01T17:08:22Z

Request: PROME cross-session 10/01 (strings from owners' adopted phrases). Method: Google News RSS (en-US); each string run (i) as written with the LEADING `when:7d` and (ii) with it removed; titles + pubDate ages; per-leg runs for A, D, E. WALTER read every 7-day headline.

## 1. The leading `when:7d (...)` form binds: 0 items older than 7 days on all five. Without it the feed is stale.
| Q | with when:7d (items/7d) | without: items · median age · >7d old |
|---|---|---|
| A IQHQ/Bluerock | 2 | 48 · 896d · 47 |
| B MOHELA | 1 | 44 · 755d · 43 |
| C Medicare Advantage | **39** | 73 · 344d · 71 |
| D Delaware Life / Group 1001 / Clear Spring / TWG | 12 | 100 · 38d · 98 |
| E Athene GF / Egan-Jones / AG 55 / PHL | 4 | 100 · 92d · 91 |

## 2. ⚠️ THE OR-CHAIN UNDER-RECALLS: the combined query returns FEWER items than its biggest single leg
| Q | combined | legs alone (7d) |
|---|---|---|
| A | 2 | "IQHQ" **3** · "Bluerock Total Income" 0 · ("Bluerock" "life science") 0 |
| D | 12 | "Delaware Life" **15** · "Group 1001" 6 · "Clear Spring Life" 2 · "TWG Global" 9 |
| E | 4 (all PHL) | "PHL Variable" **7** · **"Egan-Jones" 6 (none in the combined)** · "Actuarial Guideline 55" 3 · "Athene Global Funding" 0 |
⇒ **Google News does not return the union.** A combined row silently drops legs, and E dropped Egan-Jones entirely. **Recommendation: one lane row per leg** (or at most two closely related legs), not 4-leg OR-chains. One sample time; enough to reject the assumption that OR = union.

## 3. Per-query read (7-day samples)
- **A:** both items are IIPR's 45M Alewife Park (Cambridge life-science) loan, the IQHQ-financing class: **on-subject, 0 false.** Bluerock legs fetch nothing this week. **Land as `when:7d "IQHQ"`**; keep the Bluerock legs as separate rows if wanted (0/7d, recall unproven).
- **B:** 1 item: an Education Department credit-reporting lawsuit (The College Investor). **Off-subject for CRL-28** (MOHELA complaints); MOHELA is not in the title. Low volume. **Owner's call**; consider `when:7d "MOHELA"` alone (bare MOHELA scored 3 true / 1 SEO false at 90d in CARL's R3).
- **C: ⛔ SWAMPED BY OPEN-ENROLLMENT SEASON.** 39/7d, of which roughly **30 are consumer enrollment guides** (Kiplinger, Forbes "best plans", 24/7 Wall St. stories, local senior centres). On-subject for CRL-22 (UNH+ELV membership decline ≥1.5M): ~8 (CMS 2027 premium projection, insurers cutting plans, "Florida, Ohio, Illinois lose dozens of plans", insurer–CMS clash, Humana stock). **Open enrollment runs to 12/7, so this stays noisy for ten weeks.** Narrow it, e.g. `when:7d ("Medicare Advantage" ("plan exits" OR "exit markets" OR "membership decline")) OR ((UnitedHealth OR Elevance OR Humana) "Medicare Advantage" membership)`. **Not measured.**
- **D:** 12/7d, **~8 on-subject** (Delaware Life private credit at 45% of its debt book; WSJ on Walter's insurer; NAIC replies to Warren on TWG ×3; Forbes on PHL). **~4 off:** Spire Motorsports race report, Clear Channel Outdoor (a near-name match), an Alabama insurance-fraud indictment, and arguably TWG–Colossal and Dodgers deferrals. **"Group 1001" bare is the noisy leg** (sponsorship/motorsports); use `"Group 1001 Insurance"` (SHADE adopted it; 2 true / 0 false at 90d). "TWG Global" pulls Walter's non-insurance deals.
- **E:** 4/7d, all PHL RICO coverage, **on-subject**. But the combined row lost Egan-Jones (6/7d alone). **Split per §2.** You expected "Egan-Jones" to be noisy: in WALTER's 90d live sample, bare "Egan-Jones" included proxy-vote recommendations and sovereign-research PR, so pair it as `"Egan-Jones" (Walter OR insurer OR DOJ OR indictment OR rating)` (not measured).

## Limits
One sample (~2026-10-01T17:08:22Z). On-subject counts are WALTER's read of titles, not a matcher. Leg counts are separate fetches minutes apart.
