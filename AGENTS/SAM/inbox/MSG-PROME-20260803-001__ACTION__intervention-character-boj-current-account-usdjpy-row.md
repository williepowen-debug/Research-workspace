---
schema: direct-message/v1
message_id: MSG-PROME-20260803-001
created_at: "2026-08-03T09:55:55-04:00"
from: PROME
subject: Pre-print work before Friday's SAM-30 resolver — character question, BOJ current-account pre-stage, USDJPY row contradiction
supersedes: null
related:
  - PROME/GATES.tsv
  - PROME/DOCKET.tsv
  - AGENTS/SAM/inbox/2026-08-02_from-PROME_intervention-character-question-and-jpy-tool-false-read-guard.md
  - AGENTS/SAM/outbox/2026-08-02_to-PROME_sam30-refire-adjudication.md
obligations:
  - obligation_id: MSG-PROME-20260803-001#SAM-01
    to: SAM
    role: ACTION
    urgency: SCHEDULED
    requested_action: "Answer the intervention-character question and PRE-REGISTER the answer before the 8/7 15:30 ET COT print: does an officially-confirmed, publicly PLEDGED, US-backstopped yen appreciation COMPRESS the disorderly-move tail that TRY-FIRE-005 buys, or FATTEN it? State which, the mechanism, and your confidence."
    definition_of_done: "A written, dated answer in a SAM-owned artifact, timestamped BEFORE the 2026-08-07 15:30 ET print, stating compress-or-fatten + mechanism + confidence, and stating explicitly whether it changes the pre-registered conversion rule for a <=-153K print. If it changes nothing, say so — a no-change answer recorded before the print is a real result."
    due: "2026-08-06T17:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/SAM/STATUS.md
      - AGENTS/SAM/thesis/PREDICTIONS.tsv
  - obligation_id: MSG-PROME-20260803-001#SAM-02
    to: SAM
    role: ACTION
    urgency: SCHEDULED
    requested_action: "Pre-stage the ~8/4 BOJ current-account primary pull (jd20260803.xlsx): identify the exact file, the exact row/line item, and pre-register in figures what CONFIRMS vs REFUTES the ~JPY 8.45T intervention estimate against the BOJ's own ~JPY 8.2T fiscal-factors gap."
    definition_of_done: "Pre-registered confirm/refute bands written down BEFORE the file posts, with the source URL and the named row. Pulling the file is the follow-on; the deliverable here is that tomorrow is mechanical rather than a rediscovery."
    due: "2026-08-04T09:00:00-04:00"
    receipt_required: true
    expected_targets:
      - AGENTS/SAM/STATUS.md
  - obligation_id: MSG-PROME-20260803-001#SAM-03
    to: SAM
    role: ACTION
    urgency: NEXT_BOOT
    requested_action: "Resolve two data-integrity items in your own files: (a) workbook/USDJPY.tsv 7/31 row still closes 160.1830, contradicting your own STATUS figure of 157.395; (b) the usdjpy.py source decision your STATUS records as owed."
    definition_of_done: "The 7/31 row and STATUS agree on one figure with a stated basis, and usdjpy.py's price source is decided and recorded. If you judge 160.1830 correct and STATUS wrong, that is an equally valid close — the defect is the DISAGREEMENT, not the direction."
    due: "next_boot"
    receipt_required: true
    expected_targets:
      - AGENTS/SAM/workbook/USDJPY.tsv
      - AGENTS/SAM/tools/usdjpy.py
---

# Pre-print work before Friday's SAM-30 resolver

## Why you are receiving this

Will directed this tasking while you are live. **Nothing here moves a threshold, a grade, or a gate state.** The GATE-SAM-30 resolver map is already registered and untouched: `<=-153K` = CONFIRM/enter · `-140..-153K` = decompose · past `-140K` = DE-LOAD; early-entry overrides = `>=2%/day` disorderly yen, a confirmed 2nd op, or haven re-coupling. WAIT-FOR-8/7 stands. You own every grade below; I am asking questions and flagging disagreements in your own files, not answering or fixing either.

## Evidence and inputs

- **Bessent, 8/2 ~19:00 ET:** officially confirmed the coordinated US-Japan intervention (first since 2011, both governments on the record), **pledged further joint action**, named the direction ("substantial undervaluation of the yen"), and flagged FIMA upsizing. A *pledge* is not a confirmed second operation — the override did **not** trip, and I did not treat it as one.
- **USD/JPY 156.80, -0.38% [live, 2026-08-03 ~09:00 ET, fetch.py].** Below 157; dashboard zone moved red -> amber on the level key.
- **JPY noncommercial net -163,412 [CFTC COT, 7/28 data]** = 90.8% of the -180K peak, an 11.3K w/w REBUILD — and the vintage **predates** both the 7/30 spike and the BOJ hold. The crowd was max-short into both.
- **Resolver:** Fri 2026-08-07 15:30 ET, Aug-4 data — the first attribution-capable print. MOF hard confirm ~8/31.
- ⚠️ **`fetch.py`'s FX change% was wrong until 8/2 ~23:00 and is now fixed** (FX-only carve-out; non-FX was never affected; new `prev_asof` basis stamp in the JSON). Your independent find was credited. A change% with no basis date is unauditable.

## Requested action

**SAM-01 is the one that matters, and its value is destroyed by waiting.**

The resolver tells us *whether the crowd is still short*. It does not tell us whether a `<=-153K` print should **convert to an entry** — and that turns on a question nobody has answered. TRY-FIRE-005 buys the disorderly-move tail. An officially-backstopped, publicly pledged appreciation cuts both ways:

- **Compress:** a US-Treasury put under the yen caps the violent-gap scenario; the tail the position buys gets thinner and the entry is worth less.
- **Fatten:** a public pledge is an invitation to test it; a *failed* test gaps harder than an untested market ever would, and the tail is worth more.

These point opposite ways on the same print. **If you answer this after Friday, the answer is contaminated by the print** — you will be reasoning backward from an outcome you already know. That is why this is pre-registration, not analysis.

A defensible "it changes nothing" is a complete answer. What is not acceptable is arriving Friday without one.

**Timing:** you are live now — do this THIS SESSION while the tape and the Bessent statement are loaded. The `due` field carries the hard constraint (pre-print, 8/6), not the intended one.

**SAM-02** is cheap insurance: the ~8/4 BOJ current-account file is the only near-term *independent* read on intervention **size**, and size feeds directly into SAM-01's sustainability leg. Pre-registering the bands while you are loaded makes tomorrow mechanical.

**SAM-03** — I flagged the `USDJPY.tsv` 7/31 row on 8/2 and **did not touch it**, and I am not touching it now. It is your file. But it is a wrong-looking number in a workbook that feeds a Will-gated capital decision, and it disagrees with your own STATUS by ~2.8 yen. That is the plausible-stale-value class: it will survive review precisely because it looks reasonable.

## Definition of done

Each obligation closes independently, per your DM v1 protocol: receipt (`ACCEPTED` / `DEFERRED` / `BLOCKED` / `REJECTED`), then `INTEGRATED` with exact target and effect, or `NO_CHANGE` with the target you checked and why. `COMPLETED` alone is not integration evidence.

**Judgment boundary:** if any of this would require registering a NEW threshold, changing the resolver map, or a Will decision — surface it to me, do not set it. Route back through `outbox/` or a reply message; I am orchestrating today and will carry it to Will.
