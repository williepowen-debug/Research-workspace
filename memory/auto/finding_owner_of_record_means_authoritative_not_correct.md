---
name: finding_owner_of_record_means_authoritative_not_correct
description: "An owner-of-record designation makes a file AUTHORITATIVE, not CORRECT — so a wrong owner-of-record is worse than a wrong mirror, because the tie-break rule destroys the correct copy."
metadata:
  type: reference
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

Related: `[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]` (the general form — this is the case where a governance rule *pretends* it does) · `[[finding_registry_names_a_concept_tool_resolves_an_instrument]]` · `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`.
