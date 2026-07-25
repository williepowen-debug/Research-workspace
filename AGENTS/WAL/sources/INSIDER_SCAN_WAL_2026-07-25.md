# WAL Insider Sweep — 2026-03-01 → 2026-07-25

**Run:** 2026-07-25 (WAL session #1). **Instrument:** SEC EDGAR submissions API, CIK 0001212545 — **all** Form 3/4/4A/144 filings in the window, parsed from raw ownership XML (not a screener). **Coverage: complete, not sampled** — 53 Form 4s, 3 Form 144s, 12 reporting persons, 408 transaction lines.
**Why this ran:** V4 (Leadership/insider) was scoring 3/5 **PROVISIONAL** on an unverified "zero insider buying" leg. The prior scan (`INSIDER_SCAN_WAL.md`) is dated 2026-03-25 and covers through ~Feb 2026; KB-WAL-027's `Stale_By` of 2026-04-30 had passed. The window here spans the Q1 print (4/21), the $99M 10-Q disclosure (5/11), Curley's resignation, Investor Day (5/12), and the Q2 print (7/21).

---

## ★ HEADLINE

| Question | Answer |
|---|---|
| **Any open-market purchase (code P)?** | **ZERO.** Across all 53 Form 4s and 12 filers. **KB-WAL-027 "zero buying" CONFIRMED** — now verified, no longer assumed |
| Any discretionary selling? | **Yes — two people, both June, NEITHER under a Rule 10b5-1 plan** (`aff10b5One = 0`, element present and explicitly zero on both filings) |
| Anything a Form-4-only sweep would miss? | **Yes — the departed CBO's Form 144.** See Curley below |
| What is the other ~98% of the filing traffic? | **Mechanical cash-settled RSU vesting.** Not trading. See "The mechanic" |

---

## 1. Direct common stock — every reporting person, chronological

Balance is the **Table I "Common Stock", direct-ownership** closing figure per filing. *(An earlier pass that read the trailing `sharesOwnedFollowingTransaction` without filtering on security title produced spurious −96% "liquidations" — that number is the **Table II RSU unit balance**, a different security. Corrected here.)*

| Person | Role | Mar → Jul | Net |
|---|---|---|---|
| Vecchione Kenneth | Chairman, President & CEO | 463,178 → 463,178 | **0** |
| GIBBONS DALE | Vice Chair & CBO, Deposits *(former 22-yr CFO)* | 307,093 → **267,093** | **−40,000 (−13.0%)** 🔴 |
| Boothe Timothy W | Chief Administration Officer | 65,417 → 65,417 | 0 |
| Curley Stephen Russell | Chief Banking Officer – NBL *(resigned)* | 41,531 → 41,531 *(last Form 4 5/19)* | 0 **on Form 4** — see §3 |
| Bruckner Tim R | CBO for Regional Banking | 29,068 → 29,068 | 0 |
| Nachlas Emily | Chief Risk Officer | 16,575 → 16,575 | 0 |
| Jarvi Jessica H | CLO & Secretary | 13,707 → 13,707 | 0 |
| Idnani Vishal | Chief Financial Officer | 11,468 → 11,468 | 0 |
| Kennedy Barbara | Chief HR Officer | 10,332 → 10,332 | 0 |
| Mucha Ben | Chief Accounting Officer | 9,431 → **3,485** | **−5,946 (−63.0%)** 🔴 |
| Herndon Lynne | Chief Credit Officer | 1,880 → 1,880 | 0 |
| JAMMET MARY CHRIS | Director *(new)* | 3,118 → 3,394 | +276 — **code A (grant), not a purchase** |

**Nine of eleven executives held perfectly flat.** The only new-shares event in the entire window is a director's Deferred Stock Unit *grant*.

## 2. The mechanic — what 402 of 408 transaction lines actually are

Every month, mid-month, 8-9 executives file near-identical Form 4s. Decoded from the filings' own footnotes:

> *"These units vest and are payable **solely in cash** as follows: **1/36th on the 15th day of each month** during the 36-month period... Each unit is the economic equivalent of one share of Western Alliance Bancorporation common stock."*

Per month, per tranche: **Table II** shows a Cash Settled RSU tranche vesting (code M, disposed from the RSU balance) → **Table I** shows code **M** acquiring common stock at $0 → immediately followed by code **D** disposing the identical share count **back to the issuer at the market price**. Net common stock change: **exactly zero**. No open-market transaction, no tape impact, no discretion, no S-code.

**Analytical consequence — this sharpens KB-WAL-028 from "ambiguous."** The Dec-2025 comp restructuring means ongoing executive equity compensation is **de-equitized into cash automatically every month without anyone ever selling a share.** The Form-4 open-market-sale tell that the insider thesis watches is, for the recurring-comp channel, **structurally suppressed by construction.**

⚠️ **Do not over-read intent.** Cash-settled RSUs are also chosen for dilution management and accounting reasons and are unremarkable on their own. The finding is about the **effect on signal quality** — an absence of S-codes at WAL carries less information than the same absence would at a peer paying in settled shares — **not** about motive.

## 3. ★ Stephen Curley — the exit liquidation a Form-4 sweep cannot see

Curley is the Chief Banking Officer (head of National Business Lines — the org holding the Office/CRE concentration) whose resignation the same week as the $99M disclosure **is the entire basis of V4/B3**.

| | |
|---|---|
| Last Form 4 | **2026-05-19** (period 5/15) — routine monthly RSU mechanic, common stock flat at 41,531 |
| **Form 144 filed 2026-06-15** | **10,696 shares, aggregate market value $878,114.48**, broker Merrill Lynch, approx. sale date 06/15/2026 [acc `0001628280-26-043274`] |
| Matching Form 4? | **NONE.** No Form 4 from Curley after 5/19 exists in the window |
| Why | Consistent with Section 16 reporting obligations ending on departure — a former officer generally no longer files Form 4s |
| Scale | ~10,696 of a last-reported 41,531 direct ≈ **~26% of his stake** |
| Source of shares | Form 144 lists acquisition lots from 02/22/2022 and 02/15/2023, "Employee Stock Related", compensatory payment 06/16/2026 |

⚠️ **A Form 144 is a NOTICE OF PROPOSED SALE, not proof of execution.** Treat as intent-to-sell of that size on/about 6/15, not a confirmed trade. The Gibbons and Mucha 144s each matched a Form 4 with the exact share count, which is mild evidence that WAL-affiliate 144s do get executed — but that is an inference, not confirmation for this one.

**Why it matters:** the executive at the centre of the V4 signal moved to liquidate a quarter of his position a month after leaving, and **this is invisible to the Form-4-only sweep the thesis had been relying on.** Any future insider check must include Form 144.

## 4. The two discretionary sales — full detail

Both **NOT** Rule 10b5-1 plan sales (`aff10b5One` present and `= 0` on both).

| | **Dale Gibbons** | **Ben Mucha** |
|---|---|---|
| Role | Vice Chair & CBO Deposits — the former 22-yr CFO of KB-WAL-023 | Chief Accounting Officer |
| Form 4 | acc `0001628280-26-042179`, period **2026-06-09** | acc `0001628280-26-042181`, period **2026-06-08** |
| Transactions | 33,228 @ **$82.64** (wtd avg, range $83.06–$82.50) + 6,772 @ **$81.16** | 5,946 @ **$81.00** |
| Total | **40,000 sh ≈ $3.30M** | **5,946 sh ≈ $481K** |
| Holdings | 307,093 → **267,093 (−13.0%)**; retains ~$22.2M at $83.11, plus 612 sh in 401(k) | 9,431 → **3,485 (−63.0%)**; retains ~$290K |
| Form 144 | RBC Capital Markets, 6/9, **40,000 / $3,295,612.00** — exact match | Merrill Lynch, 6/8, **5,946 / $481,259.32** — exact match |
| Prior record | — | Already flagged in the March scan: 641 sh sold Feb 2026 (KB-WAL-026). **This is a repeat seller** |

## 5. Timing read — honest, and it cuts both ways

The only discretionary sales in four months landed **June 8-9 at $81.00–$82.64**. That is:
- **AFTER** the $99M 10-Q disclosure (5/11) and Investor Day (5/12) — so not front-running that disclosure;
- **~6 weeks BEFORE** a Q2 print (7/21) that came in **benign** and popped **+3.61% to $83.41** on the call.

**Both sellers sold BELOW today's $83.11.** That cuts **against** a "they knew something bad about Q2" reading — the insiders who exercised discretion did so at worse prices than the market now offers. It says nothing about Q3, the pending $99M appraisal, or the Q3 10-Q.

The genuinely bear-supportive behavioural item in this sweep is **not** the sale prices — it is **Curley's post-departure 144** (§3) and the continued **absolute absence of any purchase** at what management itself called *"a meaningful discount to intrinsic value"* while authorizing a $150M buyback (KB-WAL-119). **The company is buying its own stock; not one insider is.**

---

## 6. Verdict on V4

| | |
|---|---|
| Prior | 3/5 **PROVISIONAL** — rested on an unverified "zero buying" leg |
| **Now** | **3/5 — RATIFIED, provisional tag removed.** The score does not move; what changed is that it now rests on a complete primary-source scan rather than a 4-month-old assumption |
| Strengthened | Zero-buying confirmed across a complete window; Curley exit-liquidation is new and on-thesis; Mucha is now a repeat seller |
| Weakened | The mass "selling" impression from filing volume is mechanical, not behavioural; the two real sellers sold below current price ahead of a benign print; Gibbons retains 87% of his stake |
| Not moved to 4/5 | because two modest discretionary sales and one unexecuted-as-far-as-we-know 144 are not a coordinated-exit pattern |
| Not cut to 2/5 | because zero buying held through a print pop, a buyback authorization, and management's own "meaningful discount" language |

**Forward discriminators (pre-registered):**
1. **Any code-P open-market purchase** by any officer/director → genuine V4 disconfirm. Cheap to check monthly.
2. **Do Gibbons/Mucha sell again in Q3?** One sale is noise; a second consecutive quarter is a pattern.
3. **Curley follow-through** — any further 144s, and whether the 6/15 notice was executed.
4. **Watch Form 144 alongside Form 4 from now on** — §3 is the proof that Form 4 alone under-covers departing officers.

---

*Sources: SEC EDGAR submissions API (CIK 0001212545) + raw ownership XML for all 56 filings, retrieved 2026-07-25. Prior scan (Feb-vintage) retained at `INSIDER_SCAN_WAL.md` as the historical record — not superseded in substance, extended in time.*
