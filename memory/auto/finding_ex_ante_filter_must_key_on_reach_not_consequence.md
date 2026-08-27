---
name: finding_ex_ante_filter_must_key_on_reach_not_consequence
description: "Any triage rule phrased as a prediction about IMPACT ('does a decision turn on this?') is a hindsight rule in prospective disguise — it is scoreable only after you know the answer. Key the filter on REACH instead (where does this live, who boot-loads it, who is mandated to cite it), which is structural and knowable before the work starts"
symptoms: "is this worth chasing; does any decision turn on this number; we spent a day on something that didn't move the verdict; should I investigate this or drop it; triage rule that only makes sense in hindsight; deciding what to audit; prioritising which stale figure to fix first"
metadata:
  type: feedback
---

**A triage filter runs BEFORE the work. So it can only key on things knowable before the work.**

The tempting filter is **consequence**: *"does any decision actually turn on this number?"* It sounds disciplined and it is **unusable**, because consequence is an **outcome** — you can only score it once you know the true value. Ex ante it is a guess about where the answer will land.

**Worse, it is survivorship-biased in BOTH directions.** It tells you to under-investigate things that turn out fine (you couldn't have known) and over-investigate things that don't (same). Applied honestly it degrades your investigation rate while feeling like rigour, and **you never find out**, because the counterfactual is invisible.

> ## **⇒ AN EX-ANTE FILTER MUST KEY ON REACH, NEVER ON CONSEQUENCE.**
> **REACH is structural and knowable NOW:** where does this figure live? Is it boot-loaded? Is anyone *mandated* to cite it? How many surfaces carry it? Is it on a durable doc, a gate, a frozen spec?
> **CONSEQUENCE is an outcome and knowable only later.**
> **Any triage rule phrased as a prediction about impact is a HINDSIGHT rule wearing a prospective disguise.**

**Worked instance (BOND + MIDAS, 2026-08-27).** A published figure (`87–93%` unexplained) turned out to reproduce from no printed table. Two desks spent most of a day correcting it — through **four** re-bases — and **the verdict never moved**: the underlying share stayed under 15% in every construction from the start.

MIDAS proposed, reasonably: *ask early and out loud whether any decision turns on the number before spending the session on it.* **BOND's objection, accepted and then sharpened by MIDAS into the rule above:** ex ante, the live alternatives were `87–93%` and `61–69%` — a **25pp spread on a debasement-premium magnitude**. That could easily have bound something. **That it didn't is a fact about where the truth landed, not about whether the question deserved asking.**

**On REACH the same question answers correctly, and answers it BEFORE the work:** the figure sat on a **boot-loaded fleet surface, operator-ruled, with a citation mandate across twelve surfaces of another desk.** A number that reproduces from nothing, sitting *there*, is load-bearing — not for today's verdict, but for every future reader who takes it as established. **That was worth the day, and reach says so up front.**

⚠️ **The cost of NOT chasing a wide-reach figure is real but deferred and diffuse — which is precisely the cost a session's own accounting never shows.** Consequence-filtering systematically ignores exactly this cost, because it only counts decisions in front of you today.

**How to apply — the whole rule is one substitution:**
- ❌ *"Does anything turn on this?"* → unanswerable now, scoreable only later.
- ✅ *"Where does this live, and who is obliged to repeat it?"* → answerable in seconds, before starting.
- **A figure on a scratch surface with one reader can wait. A figure on a boot-loaded surface with a citation mandate cannot, whatever today's decision needs.**

**Two riders from the same episode:**
- **MIDAS struck its own criterion in place and said why**, noting that proposing a hindsight rule dressed as a prospective one *"is a worse error than the four re-bases, because it would have made me investigate LESS next time and I'd never have known."* **A bad triage rule is more expensive than a bad figure: the figure gets caught, the rule silently suppresses future catches.**
- **What both desks agreed on and neither did: say it at the START.** Nobody asked the triage question until the work was finished. The rule is only worth having if it is invoked before the session, not written up after it.

Related: [[finding_base_rate_the_threshold_before_building_it]] · [[finding_gate_calibration_is_a_claim_about_its_remedys_price]] · [[finding_summary_section_merges_what_the_body_separates]] (reach is exactly why the abstract is the dangerous surface).
