# MIDAS — TRADE

**NO OPEN POSITIONS.** No book yet; placeholder feeding PROME synthesis once MIDAS forms tradeable ideas.

**2026-07-12 update:** first live baseline landed (STATUS.md). M1's trigger ("divergence confirmed + quantified") is now quantified as **NOT confirmed** — trailing 90d shows real-rate-consistent gold decline, not a debasement premium. No candidate below triggers yet.

**2026-07-23 update (still NO position):** M1 **v2 was confirmed** (7/17, both catalyst tests) — the frame is now "gold re-coupled to & capped by real rates; premium in the LEVEL not the delta." The v2 tradeable trigger is a sustained (3+wk) **DIVERGE** (gold rising through rising real yields = premium reassertion) — currently a **nascent WATCH, not fired** (DFII10 hit a new high 2.37 [7/21] with gold firm, but only ~4 days). MIDAS-05 (LPR) graded NO-FIRE, so the I1 copper trigger did not arm either. **No candidate triggers; nothing to TERRY.**

*(Banner-compliant per blueprint §8 / PAT-023: a trade surface carries a FROZEN/NOT-CURRENT banner OR a live mtime alert — never the silent-rot middle. Exempts the surface until MIDAS opens its first idea; `boot.py` runs `ledger_staleness.py MIDAS --trade` regardless.)*


**2026-08-07 update — M1's tradeable trigger has FIRED (still NO MIDAS position).** The v2 tradeable trigger named in the 7/23 update — *a sustained (3+wk) DIVERGE (gold rising through rising real yields = premium reassertion)* — **fired on 8/7**: gold **$4,401.30** (+9.68% over the 3wk window 7/17->8/7) through DFII10 **+12bp** (2.31 -> 2.43) including a **2.47 cycle high [7/31]**. The magnitude test is what makes it a signal rather than a rates bid: empirical beta **-0.0513%/bp** (R^2=0.023, n=647) means the -4bp of the melt-up week explains **~2.4%** of a +8.70% move. M1 **2 -> 3 (Orange)**.

**What that does and does NOT mean for the book:**
- The M1 "long debasement" candidate row below now has its **trigger satisfied** for the first time. Per my charter I produce the signal, **not** the construction: this goes to **TERRY** for expression/sizing and **Will** for approval (root rules #5-#8). **MIDAS proposes no position and takes none.**
- ⚠️ **Timing caveat that belongs on any card built off this:** the trigger fired **after** an 8.7% four-session run. Root rule #6 (puts on green days, calls on red days) and rule #7 (roll duration, don't trim size) are TERRY's to apply, but the honest framing from the signal side is that **entry is arriving late in a fast move**, and a premium regime is the most volatile in both directions (my own precedent: the Jan-2026 blow-off peaked $5,318.40 [1/29/26] and gave back 22.7%).
- **Will already carries the exposure off-rail:** GLD 16 sh = **15.0% of the account**, largest non-cash holding [PROME/ANVIL 8/2 FORGE reconcile]. So the practical question is **not** "should we get long gold" — it is **sizing an existing 15% position in a regime my own signal just called more volatile**. That is a TERRY/Will question; my input is in the 8/7 memo (③).
- **Falsifier for anyone building on this:** gold back below **~$4,050** (7/31 pre-melt-up shelf) while DFII10 holds **>=2.40** re-instates the "re-coupled/capped" frame and takes M1 to 2. Registered as **MIDAS-06**, resolves **8/28**.

---

## Candidate expressions (thesis → instrument, not yet proposed)

| Channel | Direction | Candidate surface | Trigger to propose |
|---|---|---|---|
| M1 | long debasement | gold exposure (GLD / miners) on the real-rate divergence | ✅ **TRIGGER FIRED 8/7** (divergence confirmed + quantified: +9.68%/3wk vs +12bp; beta test isolates ~98% as unexplained by real rates). -> TERRY for construction, Will for approval. MIDAS takes no position. |
| M2 | GSR | gold/silver ratio trade | GSR extreme (>95 risk-off or <75 risk-on) |
| I1 | growth read | copper exposure (CPER) as China-growth expression | demand inflection confirmed w/ LME |
| I2 | supply tail | PGM supply-shock tail | SA/Russia disruption (HAWK) |

*All candidates route through TERRY for construction + Will approval before any position (root rules #5–#8). MIDAS produces the signal, not the execution.*
