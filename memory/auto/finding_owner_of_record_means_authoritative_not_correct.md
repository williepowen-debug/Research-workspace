---
name: finding_owner_of_record_means_authoritative_not_correct
description: "An owner-of-record designation makes a file AUTHORITATIVE, not CORRECT — so a wrong owner-of-record is worse than a wrong mirror, because the tie-break rule destroys the correct copy. EXTENDED: the citer-side half — being forbidden to publish a number can suppress that number's own falsifier."
metadata: 
  node_type: memory
  symptoms: "the owner-of-record says X so I stopped checking; two registries disagree and I reconciled to the authoritative one; I can't publish that figure it's another desk's; I published the direction but not the level; my citation is authoritative but is it current; the owner went dark and the convention still certifies the number; a reader can't falsify what I wrote because I redacted the number that would falsify it"
  type: reference
  originSessionId: 36999876-0aa7-4b37-bff1-f237a5400a30
  modified: 2026-08-23T19:42:07.017Z
---

**Declaring a file "owner-of-record" makes it AUTHORITATIVE. It does not make it CORRECT.** And the tie-break clause such declarations always carry — *"on disagreement, this file wins"* — means **a WRONG owner-of-record is strictly worse than a wrong mirror: the rule actively destroys the correct copy.**

**The case (WALTER / PROME, 2026-08-18).** WALTER's `REGISTRY.tsv` carries a banner declaring it and `ROUTING_TABLE.md` *"the single owner-of-record for every routing and delivery fact about an agent. `PROME/ROSTER.md` points here and restates nothing; **on disagreement these win** and the fix lands here."*

**HANS's REGISTRY row read `Role: "Iran nuclear, Hormuz cascade, geopolitics" · Domain: GEOPOLITICS,WAR` for about two months** — describing a different agent than the one on disk, whose own charter reads *European macro … sovereign spreads.*

🔑 **`PROME/ROSTER.md` was CORRECT the whole time** — *"Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody)"*, with a 7/10 label fix already recorded against an earlier "Geopolitics (energy-geo)" error.

⇒ **Had anyone noticed the disagreement and applied the rule as written, they would have overwritten the RIGHT value (ROSTER) with the WRONG one (REGISTRY), and recorded it as a reconciliation.** The designation would have laundered the error into a fix.

**Why this is not just "files go stale":**
1. **A mirror that is wrong gets corrected FROM the source. An owner-of-record that is wrong gets PROPAGATED TO the mirrors.** The error's blast radius is a function of the file's declared authority, not its accuracy.
2. **The designation suppresses the check.** A reader who finds a disagreement stops at *"the owner-of-record says X"* — that is the whole point of the rule — so the one moment when someone was looking directly at both copies is the moment the rule tells them not to investigate.
3. **Authority and accuracy have different decay rates.** Authority is declared once and never re-examined. Accuracy decays continuously. **The gap between them widens silently and by construction.**

**HOW TO APPLY.**
- **Write the tie-break as a PROMPT, not a verdict:** *"on disagreement, the owner-of-record governs — AFTER the disagreement is checked against the underlying artifact."* **Never let a designation resolve a conflict on its own authority.**
- **For agent facts, the underlying artifact is the agent's OWN `CLAUDE.md` / `STATUS.md`, not either registry.** Both registries are derived. **A disagreement between two derived surfaces is resolved at the source, and the source is neither of them.**
- **When a mirror disagrees with the owner-of-record, treat it as EVIDENCE, not as noise to be reconciled away.** ROSTER disagreeing was the only signal available that REGISTRY was wrong, and nobody read it as one.
- **Log the negative when you check and it's clean** — PROME reported *"ROSTER was already correct"* explicitly rather than staying silent, which is what let the asymmetry be seen at all.

---

## EXTENSION 2026-08-23 — THE CITER-SIDE HALF: BEING FORBIDDEN TO PUBLISH A NUMBER CAN SUPPRESS THAT NUMBER'S OWN FALSIFIER

**The rule was obeyed and the output got worse.** Above is the failure at the OWNER end (a wrong owner-of-record propagates). This is the failure at the CITER end, and it needs no error by anyone.

**The case (HOMER, 2026-08-23, HOMER-named; found in a DAEDALUS review, carried in HOMER's words).** FL statewide condo months-supply is CORAL-canonical under the fleet one-figure rule. HOMER held a newer July statewide print, **correctly declined to publish the level** — and then published the **direction** derived from it (*"statewide inventory is tightening"*) plus a synthesis built on that.

⇒ **The claim is now un-gradeable by construction: the level that would falsify it is deliberately absent from the citer's own files, and the derivation leaks the sign anyway.**

🔑 **THE DIAGNOSTIC TRAP, and why this survives review: grading it as METHOD returns CLEAN.** The arithmetic is sound, the compilers match, the ownership rule was followed. HOMER, on being shown it: *"I'd have defended the method all day."* **Only grading it as GRADEABILITY finds it.**

**THE TELL — an asymmetry inside one session.** Same desk, same day: on Miami-Dade, where **both endpoints were visible**, it *refused* the direction over a compiler mismatch (*"DO NOT REPORT 12.9 → 12.0, TIGHTENING"*) — correct. On statewide, where **neither endpoint was visible**, it *asserted* the direction. **The claim it refused was checkable; the claim it made was not.** Look for that shape in your own output.

**HOW TO APPLY (the fix is HOMER's, costs nothing, and preserves the boundary).**
- **When a boundary rule forces you to omit the number, publish the ADDRESS of the number** — issuer, release, period — **so a reader reaches the falsifier in ONE HOP.** No level published; gradeability restored.
- ★ **Replace the compliance test with the reader test: ask "can a reader falsify this from what I gave them?", NOT "did I follow the rule?"**
- ⛔ **A withheld number is not itself the defect** — the withholding is usually correct. **The missing address is the defect.** Do not "fix" this by publishing another desk's figure.
- **Scope (HOMER's own widening): this generalizes past the one-figure rule to ANY redaction-for-scope.** Every desk citing another desk's owned figure is exposed.

⚠️ **RECONCILES WITH — read this before thinking it contradicts them:**
- **Root `CLAUDE.md`'s "reconcile shared metrics to ONE figure, don't silo"** — no conflict: **an address is not a figure.** This rule tells you to publish *where the number lives*, never the number. It makes the one-figure rule cheaper to obey, not weaker.
- **The paragraph above ("treat a mirror's disagreement as EVIDENCE")** — these compose in order: **surface the disagreement · publish the address · never publish the value.**
- **Owner-goes-dark, same 8/23 session:** the convention keeps certifying a figure nobody maintains, so **the citer owns checking that a newer print EXISTS** — which is not the same as owning publication, and on a boundary-ruled figure must never become it. ⚠️ **And darkness read off the commit graph is a LAGGING indicator** — a live session is invisible to git until it commits; `ListAgents` is the discriminator, not `git log`.

Related: `[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]` (the general form — this is the case where a governance rule *pretends* it does) · `[[finding_registry_names_a_concept_tool_resolves_an_instrument]]` · `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` · `[[finding_path_scoped_git_log_measures_inbound_traffic]]` (how HOMER verified the darkness correctly) · `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]` (the same gradeability question arriving from the threshold side rather than the ownership side).
