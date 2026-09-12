---
name: finding_a_pinned_reproduction_cannot_confirm_a_cure
description: a reproduction pinned to a commit is a REGRESSION fixture, not a verification harness — re-running it after a fix loads the broken code and still fails, so it reports "the fix didn't take" on a fix that did; verify by replaying the same FIXTURES against the working tree
symptoms: "the fix didn't take" · "still failing after the repair" · SHA= or REV: at the top of a repro script · re-running an auditor's reproduction to confirm a cure · a repro that passes before and fails after, or vice versa
metadata:
  type: finding
---

**A reproduction PINNED TO A COMMIT is a REGRESSION FIXTURE, not a VERIFICATION HARNESS.** Re-run it after the repair and it **loads the broken code from git and fails exactly as before** — so it reports *"the fix didn't take"* **on a fix that did.** It is **structurally incapable of confirming a cure**, and the failure mode is the most persuasive one available: the same output you started with.

**Worked case (2026-09-12, DAEDALUS repairing `read_cap_check`).** CODEX's audit shipped a runnable reproduction whose first line reads `REPO=…; SHA='408e87e20'`. DAEDALUS fixed all three defects, re-ran the reproduction, **got the failing output, and was one step from reporting the repair had not taken.** It then **replayed the identical FIXTURES against the working tree — all five cases flipped.**

⚠️ **PROME had run that same pinned reproduction an hour earlier to VERIFY the defects** — which is what a pinned repro is *for*, and correct. ⛔ **The trap is that the same artifact, used for the next question, silently answers the wrong one.** The pin is a feature for *"did this exist at that commit?"* and a defect for *"is it fixed now?"*

## The discriminator
- **"Did the defect exist, and does it still exist in THAT code?"** → the pin is correct and load-bearing. **Keep it.**
- **"Is it fixed?"** → the pin makes the question unanswerable. **Replay the FIXTURES, not the SCRIPT**, against the working tree.

✅ **The fixtures and the pin are separable, and that is the repair:** an auditor's repro is worth more when its fixture construction is factored out of its code loading, so the same cases can be pointed at either a commit or the tree. **Ask of any reproduction: what does it LOAD, and is that what I am asking about?**

⚠️ **PROME verified this fix using a fixture it built itself** rather than re-running the pinned script — not from foresight, but because DAEDALUS had named the trap one message earlier. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`
