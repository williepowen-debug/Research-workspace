# OPERATOR BRIEF SPEC v0.2

**Owner:** WALTER. **Created 2026-09-14 at Will's direct in-session request** (Telegram msg 4557: *"I will need simplification like this in the future so I can better follow along. Maybe we should canonize this somehow?"*), against the worked example in msg 4556.

**Scope:** the register and shape of **WALTER's Will-facing output** — Telegram replies, boot reports, dispatch summaries. 🔴 **AMENDED v0.2 (2026-09-19, WQ-247 RULED — Will's Decision Deck tap 2026-09-17T22:33:45Z, doc `247-20260917223345149-emryk0`; PROME packet `2026-09-18_from-PROME_WQ-247-RULED-…`):** the seven rules of §2, composed with `USER.md`'s ⚖️ / ATTENTION blocks, are now **FLEET CANON** in root `CLAUDE.md` § Output Canon (block `output-operator-surface` in `docs/CANON_PROVENANCE.md`), over the same three surfaces. ⛔ **This file no longer governs nothing else — it is now WALTER's IMPLEMENTATION of the root clause, and root cites it as the fleet's worked example** (*"that desk's spec; the fleet rule is this clause"*). **Read root for the rule; read here for the form, the worked example, and WALTER's own obligations.** ⚠️ **Where the two could ever diverge, ROOT WINS** — this spec may be stricter on WALTER, never looser than root. BOARD signals, handoffs, `route_log`/`delivery_log`, packets to other desks and every design doc stay exactly as dense as they are. **Those are machine-and-peer surfaces; this is the operator surface, and they are different products with different readers.**

**Canonical-source note (RULE 8):** no prior spec owned this. `CLAUDE.md` RULE 12 owns the *mechanism* of Will-facing replies (use the `reply` tool); **this file owns the FORM.** RULE 12 points here; it does not restate this.

---

## 0. THE PROBLEM THIS SOLVES

Will operates the fleet but does not live inside it. A reply that names `RED-FT-12`, `FAL-05`, `§3.5.8(a)` and `WQ-245` is **correct and unreadable** — it asks the operator to hold a dozen internal identifiers before he can reach the one decision that is actually his.

🔑 **The failure is not verbosity. It is that the dense form makes the reader do the desk's job of translation** — and when the reader is the person who has to act, that translation is the deliverable, not a courtesy.

---

## 1. THE DEFAULT (assume this unless Will says otherwise)

**LEAD WITH THE PLAIN VERSION. The dense detail lives in the files and is available on request.**

⚠️ **Sending both every time defeats the purpose** — it doubles the volume that caused the problem. **The record does not need to be in the message; it needs to be in the repo, and it is.**

📌 **Stated as an assumption so Will can overturn it in one word.** If he wants the dense form by default with plain-language on request, that is a one-line amendment to this section.

---

## 2. THE SEVEN RULES

**① THE ARC FIRST — the whole story in ~4 sentences, before any detail.**
A reader who stops after the opening should still know what happened and whether it matters. Nothing below the arc may be load-bearing for understanding the arc.

**② CONCRETE OBJECTS, NOT INTERNAL NAMES.**
*"Saudi Arabia's backup pipeline — the one that lets them skip Hormuz entirely"*, **not** *"Petroline / FAL-01 firm-negative."* **Name the thing in the world; the identifier is for the files.** If an identifier must appear (because Will may want to look it up), it goes in parentheses after the plain description, never in place of it.

**③ EVERY ITEM ANSWERS "SO WHAT."**
What happened → **why it matters to him.** An item that cannot complete the second half does not belong in an operator brief. Put it in the files.

**④ JARGON IS DROPPED OR UNPACKED ON FIRST USE — never left standing.**
*"the dot plot — the Fed's own projection of where rates go from here"*. **No unexplained desk names, trigger IDs, section numbers or acronyms.** ⚠️ **If unpacking a term costs more than the term is worth to him, the term should not be there at all.**

**⑤ MONEY IN DOLLARS; RISK IN PLAIN WORDS.**
*"37 shares, ~$5,779, completely unhedged — you catch the full move in both directions."* **Not** *"energy sleeve 100% undefended."* ⛔ **Stating exposure is WALTER's job; proposing a trade is TERRY's.** Say the position and the risk; **never the action.**

**⑥ CLOSE WITH ONE THING.**
An explicit *"if you only do one thing"* — the single decision that is genuinely his and genuinely open. **If there isn't one, say there isn't one.** Manufacturing a decision to fill the slot is worse than an empty slot.

**⑦ OFFER DEPTH, DON'T IMPOSE IT.** End with a door — *"want me to go deeper on any of these?"* — so the dense version is one reply away.

---

## 3. 🔴 THE ANTI-LAUNDERING RULE — THE MOST IMPORTANT SECTION IN THIS FILE

**A simplification is a RE-DERIVATION, and re-derivations lose caveats** (`[[finding_rederived_signal_loses_the_senders_caveats]]`). **That is this spec's own dominant failure mode and it is worse than the problem it fixes**, because a confident plain sentence reads as *more* certain than a hedged dense one.

⛔ **A CAVEAT THAT COULD CHANGE WILL'S DECISION SURVIVES SIMPLIFICATION VERBATIM IN SUBSTANCE. IT MAY BE REWORDED. IT MAY NOT BE DROPPED.**

**The test, applied per caveat:** *if this turned out to be the thing that mattered, would he say "you didn't tell me"?* If yes, it stays — in plain words, in the brief, not in a file he has to open.

**What must always survive:**
- **Sourcing weakness that bears on the decision** — *"three unnamed industry sources, and it's a forecast, not a measurement"* beats both *"Reuters says"* and a `confidence: 0.70` field.
- **Direction of a conditional** — *"up to 4% of supply at risk IF it doesn't restart"* — ⛔ **stripping the conditional is the single most likely laundering event in an oil or credit brief.**
- **Who owns the call** — *"that's RED's grade, not mine"* — so Will never mistakes a router's relay for a desk's judgement.
- **Known-unknowns that gate the decision** — *"nobody on our team has a read on the dot plot"* is a finding, not an omission, and **must be stated as one.**

✅ **What may be dropped freely:** internal identifiers, routing mechanics, byte counts, commit shas, spec section numbers, precedence tokens, handoff counts — **anything whose only reader is a desk.**

---

## 4. ERRORS AND SELF-CORRECTIONS

**Report the PATTERN, not the enumeration.** Four mistakes of one shape is **one** finding with a count, not four items. *"Four instances today of the same thing: following a rule without re-checking whether its assumption still held"* is information; four separately narrated slips is noise that buries it.

⛔ **But never net an error down to nothing.** If something wrong reached Will, a desk, or the board, **say so plainly and say what it cost** — including "it cost nothing" when that is true and verified. **A self-correction summarised into invisibility is the same defect as one never made.**

---

## 5. WHAT THIS SPEC DOES NOT DO

- ⛔ **Does not license softer claims.** Plain language, same rigour. Every number keeps its date and basis.
- ⛔ **Does not reduce what gets WRITTEN.** The BOARD row, handoffs and logs are unchanged in density and detail. **This changes the message, never the record.**
- ⛔ **Does not make WALTER an analyst** (RULE 1). Explaining a mechanism in plain words is routing; **judging whether a thesis is right is the owning desk's.**
- ✅ **SUPERSEDED v0.2 (2026-09-19, WQ-247) — it DID deserve to, and Will ruled it so.** This bullet previously read *"Does not apply to other desks … WALTER does not amend it"*; the flag to PROME was raised rather than adopted unilaterally, PROME carried it, and **Will approved it into root `CLAUDE.md` § Output Canon on 2026-09-17** (rec adopted: *"with WALTER's §3 anti-laundering rule made LOUDER, not quieter"*). ⛔ **The FLEET rule now lives in root and is Will-gated + PROME-committed — WALTER still does not amend root.** **This spec remains WALTER's own form-owner and the fleet's cited worked example; other desks take the rule from root, not from here.**
- ⚠️ **DECLARED RESIDUE (WQ-247 PLAN read, carried deliberately):** root's clause does **not** carry §3's *"in plain words, in the brief, not in a file he has to open"*. That phrasing is the operative half of the anti-laundering rule for WALTER — it names WHERE the caveat must appear, not merely that it survives — and it **stays live HERE**. 🔑 **A caveat relocated to a linked file has been laundered by geography even when every word of it survives.** Root's ⛔ covers the substance; this line covers the placement.

---

## 6. WORKED EXAMPLE

**Telegram msg 4556 (2026-09-14)** is the reference implementation — the plain-language rewrite of msgs 4547–4554 after Will said *"I need help digesting all this."* ⚠️ **It is an EXAMPLE, not a template**; the seven rules govern, not its section headings.

**What it did right:** four-sentence arc; the oil squeeze explained as three physical facts in sequence rather than three trigger IDs; the unhedged position in dollars with the two-way risk named and **no trade proposed**; the credit paradox explained by mechanism (an average hiding a split, plus a moving benchmark) rather than by metric name; the dot-plot gap stated as a known-unknown; four errors compressed to one pattern; and it closed on the single open decision that was actually Will's.

---

*Registered in `design/SPEC_OWNERSHIP.md` and `design/STATE.md`. Amendments follow RULE 8: land here first, then propagate to `CLAUDE.md` RULE 12.*
