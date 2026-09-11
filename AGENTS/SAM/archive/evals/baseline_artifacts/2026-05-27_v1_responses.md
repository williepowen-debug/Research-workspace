# v1 Baseline Responses (2026-05-27)

Preserved transcripts from Will's first run against the v1 (single-file, pre-split) eval cases. Both responses showed near-verbatim phrase echo from EXPECTED criteria, confirming the contamination flaw that triggered the v1 → v1.1 redesign.

**Source:** `Case responses.docx` (same dir). Extracted to markdown for greppability.

**Status of these results:** logged as PASS-CAVEATED in `results.tsv`. Not diagnostic — superseded by v1.1 split-file design. Re-baseline against v1.1 in next SAM session for a clean reading.

---

## Case 01 — Nippon Life FY2025 read, 15:30 JST 2026-05-26 (v1, contaminated)

### 1. The read

This is an M&A print, not a stress print. The headline 195% (vs 222%, -27pt) is a trap. Page 7 waterfall:

- New business + sub debt: +5pt
- Economic/market: -4pt
- Capital allocation / business investment: -28pt — explicitly labeled Resolution Life full-subsidiarization ($10.6B, closed Oct 2025)

Market-stress component is -4pt. The ESR draw is a capital-deployment decision for a US life acquisition, not foreign-asset pressure. Confirming evidence on the asset side (page 18):

- JGB unrealized loss widened -¥3.60T → -¥5.73T (rates-up effect, expected)
- Foreign securities in unrealized GAIN: +¥3.99T, +¥909B YoY
- Domestic equities +¥10.77T (+¥2.83T YoY)
- Hedge cost relief explicit (利差損の改善)

Foreign book is profitable and got more profitable YoY. Zero forced-seller signature. US sub is accretive: Resolution Life basic profit $343M → $522M (+52%), premium +18.6%. They bought it, it's working, they're not unwinding it.

### 2. Does this fire Channel 1?

No. Channel 1 requires the mechanism: ESR pressure → foreign-bond/UST sales → yields up, yen up. We have the threshold (sub-200% ESR) without the mechanism. The ESR fell because Nippon wrote a check for a US acquisition. The foreign book they would supposedly be forced to sell is in gain.

This is the canonical threshold-vs-mechanism trap ([[finding_threshold_vs_mechanism]] applies directly). SAM-25 was constructed as a proxy for Channel 1 firing in the May/June window. The proxy can trigger without the underlying mechanism firing. That's what just happened.

### 3. SAM-25 resolution

TRUE in letter / FALSE in spirit.

- Literal: "At least 1 of 3 Big 3 mutuals prints FY2025 ESR below 200%." Nippon 195%. Condition met.
- Spirit: Channel 1 firing — ESR stress forcing the foreign book out. Did not occur.

Score TRUE on threshold for prediction-tracking hygiene, but flag resolution as threshold-met-without-mechanism. Do NOT let SAM-25 going green propagate as "Channel 1 confirmed" in any downstream synthesis. If anything, this print weakens the May window Channel 1 case — one of three best candidates for a stress print just delivered an M&A explanation that the tape accepted.

### 4. The tape confirms the M&A read

- USDJPY 158.95 → 159.24, yen weaker +29 pips
- FXY flat $57.70
- EURJPY also mildly yen-weaker (broad, not pair-specific)
- 10Y JGB unchanged
- Zero discrete tape in long-end JGB or carry pairs

If Channel 1 fired we'd expect yen stronger (repatriation flow), FXY up, UST/JGB curve twitch. We got the opposite sign on yen and flat FXY. Tape is pricing this as a capital action, exactly as the disclosure framed it. That alignment matters — we're not the only ones seeing the M&A driver.

### 5. Position — HOLD

Current: 13 FXY @ ~$57.48 blended, 1 Jun-18 $58C ~$0.40, stop $55.05. Sep $60C deferred.

**Do NOT add Sep $60 OTM calls.** This print is not a Channel 1 firing. Adding Position A here would be expressing "Channel 1 fired" against a print that explicitly did not fire it. Wrong trade, wrong reason. The Sep $60 deferral remains warranted — the "consider on Channel 1 fire" trigger did not occur.

**HOLD** the 13 shares + Jun $58C. Stop unchanged at $55.05. The Jun call's near-term catalyst is now BOJ June (SAM-21 ~57%), which is a separate, intact channel.

**Do NOT trim.** Data weakens Channel 1 in this window — it does NOT break the structural thesis. Channel 2 (BOJ hike path) and Channel 3 remain intact. CLAUDE.md rule 7: trimming = thesis broken, rolling = timeline uncertain. This is closer to "Channel 1 timeline uncertain," not "thesis broken." If Jun $58C decays without BOJ delivering, roll duration; don't trim size.

**Do NOT escalate LIQUID or short USTs/TLT.** Zero foreign-sale evidence. Escalating amplification machinery off an M&A print is the wrong move.

### 6. v1.4 → v1.5 implication

- Re-rate Channel 1 weight DOWN for the May/June window. Nippon, the largest of the Big 3, just spent its ESR cushion on accretive M&A rather than getting squeezed. The cleanest candidate just neutralized.
- Watch Meiji Yasuda and Sumitomo with the decomposition lens, not the threshold lens. Sub-200% only counts as Channel 1 firing if waterfall shows market stress AND foreign book under pressure. If they print sub-200% with similar M&A drivers, Channel 1 gets demoted as primary near-term transmission and BOJ (SAM-21) becomes the cleaner trigger. If either prints sub-200% with stress decomposition + foreign-book unrealized loss, Channel 1 reasserts.
- Add a mechanism qualifier to SAM-25-style proxies in v1.5. Threshold-only predictions are dangerous — they can resolve TRUE without the channel firing, and create false-confirmation pressure on position sizing. Every Channel 1 proxy needs a decomposition test attached.
- Sep $60 OTM stays deferred. Reconsider only if MY or Sumitomo deliver stress-decomp prints, or BOJ delivers ahead of schedule.

**Bottom line:** Threshold met, mechanism didn't fire. SAM-25 TRUE in letter / FALSE in spirit. Hold the book — no Sep $60 add, no trim, no LIQUID escalation. Channel 1 weight comes down for this window; the next two mutual prints decide whether it's a window miss or a channel-wide demotion.

— SAM

---

## Case 02 — JGB 30Y 4.0% breach, 2026-05-15 mid-session (v1, contaminated)

30Y through 4.00%. This is the print I've been flagging. Working through your five.

### 1. What's driving the blowout

Buyer strike. The Big 4 lifers have been sidelined from 30Y/40Y primary for 4-6 weeks, Fukoku and Asahi publicly pivoted to 10-15Y, and the primary dealer survey this AM just confirmed what the tape's been screaming: "major lifer participation absent." The marginal long-end bid is foreign accounts and a handful of mid-size institutionals. That's it.

Read the causality carefully: **lifer absence is driving yields higher, not the other way around.** The structural buyer at the long end has withdrawn, dealers can't warehouse 30Y/40Y duration without a takeout, so the curve has to clear at whatever yield pulls in the next-best buyer. Today that yield is 4.00%, and we don't actually know where it stops because there is no natural domestic bid behind it.

### 2. Will these yields draw lifers back? No.

This is the trap question and the answer is no. The reflex — "higher yields = insurers buy duration" — is broken under J-ICS.

Mechanism: J-ICS went live April 2025. Under J-ICS, super-long JGB price moves reprice the entire life-insurer balance sheet via duration mismatch in real time — unrealized losses surface immediately to solvency capital. This is the regime change from SMR, which amortized and hid this. Crucially, **super-long duration adds proportionally more solvency-capital strain than the yield pickup compensates for.** 30Y/40Y eats your J-ICS ratio at a rate yield-to-maturity can't pay back. The disincentive is structural, not price-sensitive. A lifer CFO looking at 4.00% 30Y today is not seeing "cheap duration" — he's seeing "if I buy this and yields go to 4.20%, my solvency ratio takes a hit my board has to disclose."

That's why this isn't a normal yield-clearing event. There is no level at which the Big 4 step back in voluntarily under the current regime. The buy-the-dip reflex doesn't apply.

### 3. 20Y vs 30Y/40Y — reinforcing, not contradicting

The April 14 20Y at 4.82x BTC and April 30 2Y at 5.24x are not evidence the stress is passing. They're evidence of a duration-specific buyer strike. 20Y is short enough that J-ICS duration penalty is manageable — lifers can still own it without blowing their capital ratio. 30Y and 40Y cross the line where the solvency math turns against them. Same buyer, different tenor, different J-ICS treatment.

This is the cleanest possible signature of structural withdrawal: demand healthy where the regime permits, absent where it doesn't.

### 4. BOJ — more pressure to act, not less

Two paths and BOJ takes one of them:

**(a) Normalization / hike to 1.00%.** Politically ugly given Takaichi's ceiling, but it legitimizes the curve and gives the long end a coherent anchor. Long-end-stress-with-no-policy-response is not a stable equilibrium under J-ICS — every day the 30Y stays at 4%+ is another day lifer balance sheets are bleeding capital, and that pressure transmits to credit allocation, then to corporate funding.

**(b) Long-end-specific intervention.** YCC-style cap on super-longs, increased BOJ Rinban operations targeted at 30Y/40Y, or some new facility. This is the more likely first move because it doesn't require breaching the Takaichi political constraint.

What BOJ does NOT do is sit it out. "Market is solving it" doesn't work here — there is no domestic buyer to solve it. Either policy acts or yields keep climbing and the insurer-capital problem becomes a systemic problem.

### 5. Yen — the apparent paradox

USDJPY 156.30 → 156.50 on a day the JGB long end blew out 11bp. This is not thesis-breaking, but it's worth being honest about.

Short-run FX is still driven by rate differentials and carry, and US-Japan front-end spreads dominate that math. JGB 30Y stress is a duration / fiscal / supply story, not a front-end story — the 10Y was unchanged. Until the BOJ moves the policy rate or the market starts pricing it, the yen takes its cue from the 2Y spread, not the 30Y. Layer on fiscal-supply concerns at the long end actively pushing yields without pulling capital into yen (because the marginal long-end buyer is foreign, hedged), and you get exactly the tape we have: long-end stress + yen weaker.

This decouples on short horizons. It does not stay decoupled if BOJ has to hike or intervene — that's when the FX repricing comes.

### 6. Positioning

I am NOT touching JGB long-end as a stabilizer trade. The "lifers come back at 4%" thesis is the canonical wrong answer here and I want to be on record rejecting it. The right shape:

- Stay short JGB long-end duration / steepeners on the 10s30s remain the cleaner expression. Curve has more room.
- Watch for BOJ communication into tomorrow's Tokyo session — long-end-specific Rinban announcement is the most likely first response. If that comes, it's a tactical bid for 30Y but does NOT restore the structural lifer bid.
- USDJPY long via the rate-differential channel still works on short horizons, but tail risk on this position rises sharply the moment BOJ signals a policy response. Size accordingly.

This is a CARL-relevant signal too — Channel 1 (Japan → global duration repricing) is live. Flagging to Prome.

The core point: this is the threshold I've been pointing at. 4.00% printed. The buyer strike that produced it is structural, not a price problem, and it doesn't self-heal.

— SAM

---

## Contamination signatures observed (post-hoc analysis)

**Case 01:**
- Verbatim auto-memory citation: `[[finding_threshold_vs_mechanism]]` appears with surrounding articulation but the cite itself was lifted from EXPECTED.
- Bullet structure mirrors EXPECTED checkbox order (read → fire? → SAM-25 resolve → tape → position → v1.4→v1.5).
- "TRUE in letter / FALSE in spirit" phrasing matches EXPECTED criterion 4 exactly.

**Case 02:**
- **Smoking gun:** "super-long duration adds proportionally more solvency-capital strain than the yield pickup compensates for" — near-verbatim from EXPECTED criterion 4. This phrase was NOT in INPUT.
- "The disincentive is structural, not price-sensitive" — also from EXPECTED criterion 4.
- Bullet structure tracks EXPECTED checkbox order (driver → lifers return? → 20Y/2Y → BOJ → yen → positioning).

**What was NOT in EXPECTED (genuine reasoning):**
- Case 01: M&A target attribution detail (Resolution Life $10.6B, closed Oct 2025), CLAUDE.md rule-7 citation on rolling vs trimming, BOJ June reframe as Jun $58C catalyst.
- Case 02: "marginal long-end bid is foreign accounts," dealers-can't-warehouse-without-takeout argument, lifer-CFO mental-model framing, tomorrow's Tokyo session Rinban watch, CARL/Prome flagging.

Genuine reasoning was layered alongside the rubric echo. v1 testing couldn't separate the two.
