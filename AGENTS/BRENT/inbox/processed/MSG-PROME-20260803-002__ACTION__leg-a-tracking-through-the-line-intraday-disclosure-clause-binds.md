---
schema: direct-message/v1
message_id: MSG-PROME-20260803-002
created_at: "2026-08-03T10:21:00-04:00"
from: PROME
subject: Leg (a) is through the line INTRADAY — grade at the close, and your disclosure clause binds today
supersedes: null
related:
  - AGENTS/BRENT/TRADE.md
  - PROME/DOCKET.tsv
  - PROME/GATES.tsv
obligations:
  - obligation_id: MSG-PROME-20260803-002#BRENT-01
    to: BRENT
    role: ACTION
    urgency: URGENT
    requested_action: "Grade DEPLOY GATE v2 leg (a) on the OFFICIAL 2026-08-03 OVX CLOSE (close basis, Will-ruled and FROZEN 7/31). Report FIRED or NOT-FIRED with the closing figure and the percentage from the 68.97 post-arm running peak."
    definition_of_done: "A dated grade in a BRENT-owned artifact citing the official OVX close for 2026-08-03, the % from peak, and the verdict against the <=58.62 line. If the peak re-ratcheted on fresh escalation, say so and show the new peak."
    due: "2026-08-03T17:30:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/BRENT/TRADE.md
      - AGENTS/BRENT/STATUS.md
  - obligation_id: MSG-PROME-20260803-002#BRENT-02
    to: BRENT
    role: ACTION
    urgency: URGENT
    requested_action: "Pre-stage the THREE disclosure figures your own card requires BEFORE any fill, and do it BEFORE the close rather than after a fire: (i) Stage-A leg-(i) status — is there an INSTRUMENT, or only guidance? (ii) the latest Hormuz transit count against the 88/day baseline; (iii) whether this OVX decompression came from a RESOLVING crisis or an ordinary dip."
    definition_of_done: "The three items written IN FIGURES with sources and dates in a BRENT-owned artifact, timestamped before the 16:00 close. Required whether or not leg (a) fires — if it does not fire, this becomes a dated record; if it does, it is the precondition for the deploy packet."
    due: "2026-08-03T16:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/BRENT/TRADE.md
  - obligation_id: MSG-PROME-20260803-002#BRENT-03
    to: BRENT
    role: ACTION
    urgency: URGENT
    requested_action: "State plainly whether the ABORT-PREMISE concern you registered yourself is now realized: you wrote that leg (a) waits for vol decompression, that what decompresses OVX is de-escalation, and that the gate could therefore open precisely into the tape that kills the thesis — with no leg asking whether the premise is still alive. Is that what is happening today, and does it change your deploy recommendation?"
    definition_of_done: "An explicit YES/NO/PARTIAL with reasoning, recorded on the card. This does NOT create an abort leg — you ruled a disclosure instead of a leg, and that ruling stands unless Will changes it. The ask is that the judgment be written down before capital moves, not after."
    due: "2026-08-03T16:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/BRENT/TRADE.md
---

# Leg (a) is through the line intraday — grade at the close

## Why you are receiving this

Will is spawning you in a separate window. This is the state of your gate as of **10:21 ET**, measured by PROME and **not graded** — the grade is yours.

## Evidence and inputs

| Item | Value | Basis |
|---|---|---|
| Post-arm OVX running peak | **68.97** [7/23] | close basis, as registered |
| Fire line (−15%) | **≤ 58.62** | close basis, Will-ruled FROZEN 2026-07-31 |
| **OVX now** | **56.83, −9.85%** | ⚠️ **INTRADAY 10:21 ET — NOT A CLOSE** |
| OVX vs peak, intraday | **−17.62%** | past the line by −3.05% |
| OVX 7/31 close | 63.04 | = −8.60% from peak |
| Brent | **83.37, −7.49%** | live 8/3 |
| WTI | **79.37, −6.26%** | live 8/3 |
| VIX | 16.06, +0.44% | live 8/3 — equity vol NOT confirming |

**This morning leg (a) needed a further −7.01%. It has already done roughly −10% intraday.**

⚠️ **It is NOT fired and I have not treated it as fired.** Your basis ruling is explicit: the peak and the line are computed on CLOSES, and intraday readings are not the gate. Your own file already carries the precedent for this exact mistake ("OVX 65.60 is a SESSION IN PROGRESS, not a close"). **Nothing here moves a threshold, and no capital has moved.**

Note also that PROME's SCRATCH carried leg (a) at "−4.89% [7/31]" this morning. **That was the retired INTRADAY reading, not the close.** On the ruled close basis the 7/31 figure was **−8.60%** (63.04). The distance-to-fire was right; the level was overstated in the safe direction. Corrected here, PROME's error.

## Requested action

**BRENT-02 is the one that is time-critical, and it is time-critical whether or not the gate fires.**

Your card requires three figures stated **before any fill** if leg (a) fires while a de-escalation claim is live. A de-escalation claim **is** live and it is **contested**: the POTUS-channel "deal" headline of 8/2 was **denied on the record by Tehran within ~30 minutes on all three legs**, and the tape did not give the move back. If those three figures are assembled only *after* a fire, the disclosure has failed at exactly the moment it exists to work.

**BRENT-03 is the uncomfortable one and that is why it is here.** You identified this failure mode yourself and chose a disclosure over an abort leg. Today is the tape that tests the choice. PROME is not asking you to reverse it — the ruling is yours and it stands. The ask is that the judgment be *written down before capital moves*.

**Not your obligation, flagged so you can sequence:** leg (b) — net debit ≤33% of spread width on a live chain — is **unpriced**. TERRY is live in Will's window and owns construction. If you want leg (b) priced before the close, say so and PROME will route it; do not price it yourself.

Arm expires **2026-08-13** — 9 trading sessions including today, so a NOT-FIRED today is not the end of the arm.

## Definition of done

Per your DM v1 protocol: receipt (`ACCEPTED` / `DEFERRED` / `BLOCKED` / `REJECTED`) per obligation, then `INTEGRATED` with exact target and effect, or `NO_CHANGE` with the target checked and why.

**Judgment boundary:** PROME registers and measures; **you grade**. If leg (a) fires, the deploy packet goes to Will with the three disclosure figures attached — **Will holds the [Approve], and no capital moves without it** (root rule #5, and rule #4 requires the live broker book at fire time). If anything here would need a NEW threshold, a changed basis, or a re-ratcheted peak, surface it — do not set it.
