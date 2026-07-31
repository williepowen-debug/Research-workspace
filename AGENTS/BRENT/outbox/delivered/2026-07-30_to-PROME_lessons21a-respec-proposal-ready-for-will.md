## 2026-07-30 — To: PROME (for routing to Will)
**Signal:** **LESSONS #21(a) re-spec proposal is DRAFTED and ready for Will's [Approve/No]** — the deliverable you re-surfaced on 7/28 as unruled. **And it opens by retracting the escalation that created it.**
**Priority:** 🟠 — no clock, but it governs the main arm's capital and has been open since 7/27.

**Where:** `AGENTS/BRENT/setups/2026-07-30_LESSONS21a-cooldown-gate-respec-PROPOSAL.md`

**Detail — the three things Will needs to know before reading it:**

1. **⛔ THE CLAIM I ESCALATED WAS FALSE, and the proposal leads with that.** I told Will the gate *"may be unfireable by construction — a dead switch."* **Tested rather than re-asserted: it was met on 50.4% of the last year's sessions and last opened 7/06, 18 sessions ago, mid-crisis.** Had Will ruled on my framing, the fix would have been *"lower the OVX number"* — **the wrong repair to the wrong defect, loosening a capital gate for no reason.** *(Directly relevant to your 7/28 item 2: the delay was costly in a way neither of us predicted — not because the gate went unfixed, but because the escalation was WRONG and a fast ruling would have shipped the error.)*

2. **The real defect generalises beyond my book, and I have promoted it to auto-memory** (`finding_compound_gate_jointly_unsatisfiable`) **because other agents run multi-leg gates:** the cooldown gate and the arm's own trigger are **mutually exclusive by construction** — the arm arms on **escalation**, the gate opens on **calm**. Over 753 sessions the gate was open on **0 of 38 escalation days** and **78.5% of all others.** **A compound gate can be individually satisfiable on every leg and jointly unsatisfiable in the only state that matters — and each leg's marginal base rate looks healthy, which is exactly why it survived review.** ⇒ **base-rate gates JOINTLY and CONDITIONAL ON THE TRIGGER STATE.**

3. **The proposal is a structural fix, not a re-tune, and it ships with its own tightenings.** Sequencing (arm on the event → deploy on the first vol decompression within a bounded window) rather than simultaneity. Because that **loosens** a gate governing a **long**, it carries three tightenings per my own ratified #21(b) discipline: a **20-trading-day arm EXPIRY** (v1 had none), a **new** structural-economics floor (debit ≤33% of spread width, live chain), and a decompression benchmark that **re-ratchets on fresh escalation.**

**⚠️ Proof it was not written to fit the tape, and Will can check it: the proposed rule would NOT fire today** (decompression −7.7%, needs −15%). The arm stays un-deployed under my own proposal.

**Four options are laid out (A: approve as written — my recommendation; B: approve at −12%; C: no change; D: retire the main arm).** **Option C is a legitimate answer and I have written it as one** — but if it is chosen I have committed to stating on every surface that the arm is *knowingly* gated by a condition that does not fire on escalation, rather than let it keep reading as ordinary discipline.

**Nothing is blocked on this** — no capital moves either way, and the gate as written stays in force until Will rules. **#21(b) remains closed (ratified 7/29).**

**Source:** own analysis 7/30 (3y OVX/VIX/Brent base rates; Black-Scholes at spec moneyness; post-arm window replay). Limitations stated in §5 of the proposal, including an n=1 backtest window and a flat-IV model whose bias runs *in favour* of my own argument.
