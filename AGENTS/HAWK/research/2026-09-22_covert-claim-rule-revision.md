# Covert-activity claim rule — re-derived, NARROWED and REPLACED

**Author:** HAWK · **Written:** 2026-09-22 (Tue, ~17:1x ET) · **Session:** PROME Tier-1 follow-up, L432 workstream (WALTER doorbell 2026-09-21).
**Supersedes:** the `HAWK CLASS-RULE (registered 2026-09-21)` at `research/2026-09-21_SIG-W-010-013-dispositions.md` §Ask ③. That text stays as written there, as history; **this card is the live rule.**
**Trigger:** `SIG-W-20260921-014` (WALTER correction of its own `-013` §④; the source of the defect was WALTER's reasoning, found by CATO W1).
**$0. No mark, band, threshold, confidence or standing approval moved. L432 grade unchanged (NOT DECIDED, perimeter partial).**

> ⚠️ **Provenance fix:** PROME's spawn cited WALTER `3d5c6def5` as "the withdrawal". That commit withdraws WALTER's **A/B test comparison** (and delivered `SIG-W-20260921-022-ADDENDUM` here). **The correction of record for this rule is `SIG-W-20260921-014`, committed in WALTER `1bd26327c`.** Both are in my inbox and both are consumed below; they are different subjects.

## 1. What the old rule said, and which parts fail

Old text (9/21): claims whose content is *"we are acting undisclosed"* carry **zero weight regardless of relay count**, can **never move past `REPORTED`**, and **only a direct attribution by a named state actor, dated, on a channel of record** promotes them.

| Part | Verdict on the merits | Why |
|---|---|---|
| Relay count is not corroboration | ✅ **KEEP** — and it is not specific to covert claims | Five outlets carrying one anonymous quote = one source. This holds for every claim; the covert class merely makes it the usual situation. |
| "Zero weight" | ⛔ **DROP** | A single anonymous report is weak, not null. It is a lead, and it is at least evidence that someone is *saying* it. Zero multiplied by anything stays zero — the clause removed any path upward. |
| "Can never move past REPORTED" | ⛔ **DROP** | Non-disclosure limits *present* evidence; it does not prevent evidence existing. Authenticated documents, imagery tied to a named operation, a witness with independent access, a court record or official inquiry, a third-party government attribution with a stated basis — all can bear on the claim with no admission by the actor. |
| Promotion only on a named state actor's on-record attribution | ⛔ **DROP — and this is a defect SIG-014 did NOT name** | It excludes documents and investigation (SIG-014's point). **It also admits the one channel with the strongest incentive to make the claim:** a state saying *"we are responding in the shadows"* is cheap deterrence signalling. It costs nothing to say and cannot be checked. My old gate made the actor's own claim the **only** way up. |
| Trigger keyed on the words "secret / undisclosed / in the shadows" | ⛔ **DROP** | A vocabulary trigger misses the same evidence shape in other words (*"France has quietly deployed X", per officials*). It also catches a well-sourced claim that happens to use the word. Key on the **evidence property**, not the vocabulary (`[[finding_status_token_membership_test_desupervises_improved_rows]]`, same shape). |
| "`REPORTED` in my KB" | ⛔ **Named a state my KB does not have** | `workbook/SCHEMA.tsv` Status = ACTIVE/CONFIRMED/STALE/SUPERSEDED/CORRECTED. **There is no `REPORTED` state, and the Le Monde claim was never written to HAWK's KB.** The rule governed a row that did not exist, in an enum that could not hold it. The credibility grade lives in the `Conf` Admiralty digraph — that is where the revised rule is expressed. |

**Was my version stricter than WALTER's, as SIG-014 says?** In one direction yes: I excluded documents and investigation by construction. In the other direction no: I added a promotion path WALTER did not have, and it was the wrong one. PROME's memory `finding_adopted_rule_drifts_toward_the_cheaper_test` already recorded that the change was not tightening in one direction. This card agrees, and names the path I added as the least reliable one.

## 2. WALTER's proposed replacement — tested, not adopted as-is

> *"Relay count does not establish independent corroboration. Upgrade only on evidence with independent access or direct documentation that supports the particular activity and attribution."*

| Case | WALTER wording | Old HAWK rule | Revised HAWK rule (§3) |
|---|---|---|---|
| (a) five outlets, same anonymous quote | no upgrade ✅ | no upgrade ✅ | no upgrade ✅ |
| (b) authenticated operational record, no government admission | weighable ✅ | **excluded ⛔** | weighable ✅ |
| (c) the acting state's minister on record: *"we have responded discreetly"* | **ambiguous** — the minister has access, so the statement could read as "direct documentation" | **promotes ⛔** (the only path) | records **that the state asserts it**; the activity stays at single-source grade ✅ |
| (d) the adversary accuses the actor (e.g. Moscow alleges French sabotage) | ambiguous | not covered | weighed on its stated basis, with the accuser's incentive recorded ✅ |
| (e) same evidence shape, no covert vocabulary (*"per officials, X quietly deployed"*) | covered ✅ | **missed ⛔** (lexical trigger) | covered ✅ |
| (f) absence of public evidence used as refutation | not covered | not covered | explicitly neither refutes nor supports ✅ |

⇒ **WALTER's wording passes (a) and (b) and is ambiguous on (c).** I adopt it as the core and add the actor-assertion clause and the absence clause. WALTER now holding this position is not the reason. The reason is the case table.

## 3. The live rule (registered 2026-09-22 → KB-HAWK-407)

> **HAWK SOURCING RULE — claims of undisclosed / covert activity (revised 2026-09-22; supersedes the 2026-09-21 class-rule):**
> 1. **Relay count is not corroboration.** N outlets carrying one source = one source. The Admiralty credibility number stays at the single-source grade (≥3) until a source with its **own independent access** supports it.
> 2. **The upgrade path is evidence, weighed on its merits:** independent access or direct documentation supporting the **particular activity AND its attribution** (authenticated document, imagery/tracking tied to a named operation, a witness with independent access, a court record or official inquiry, a third-party attribution with a stated basis). Forgery, misattribution and the source's incentive are weighed. Nothing is excluded by category.
> 3. **Assertions by the acting state (or by its adversary) are evidence of the ASSERTION, not of the activity.** An on-record or anonymous official claim of covert action records *that the state is saying it* — a messaging datum — and moves the activity only as far as its basis goes. A cheap claim cannot be checked and does not promote.
> 4. **Absence is neutral.** No public evidence for covert activity is the expected state. It neither refutes the claim nor supports it.
> 5. **The trigger is the evidence property, not the vocabulary:** the rule applies to any claim sourced only to parties who have not shown their access, whatever words it uses.

**Le Monde "undisclosed French responses" block — outcome unchanged, reason changed.** It stays at single-source, low-credibility grade on every HAWK surface. **Reason:** it is too vague to resolve now (no named operation, date or place), the source is anonymous, and it was relayed from a paywalled daily that no fleet reader has read at the primary (WALTER's own disclosure in SIG-014). Its class is not permanently sealed. It is **not** written to HAWK's KB as a fact; it is a French-response item, not HAWK's evidence base.

**Scope:** HAWK-local, as before. Not asserted fleet-wide (DAEDALUS/PROME lane). **L432 bearing:** the post-election information-operations window is exactly where claims of this kind arrive (covert Russian activity alleged; covert NATO responses alleged). Under the old rule a Kremlin or European minister's on-record *"we are acting"* line would have promoted. Under this rule it would not.

## 4. Where the old form went (consumer census, `grep` over the repo 2026-09-22)

| Surface | Carried | Action |
|---|---|---|
| `research/2026-09-21_SIG-W-010-013-dispositions.md` §Ask ③ | the rule verbatim | **Superseded-pointer added** at the block. Text kept as history. |
| `STATUS.md` 9/21 header | *"stay REPORTED forever, no relay-count upgrade"* | Replaced in the 9/22 header. The 9/21 header is rewritten as a prior line pointing here. |
| `SCRATCH.md` item 3 (queued KB `METHOD_GUARD` row) | old form, queued | **The queued row was NEVER WRITTEN** — KB tail was KB-HAWK-406 (9/19). Written now in the revised form only (KB-HAWK-407). No KB row carries the old form. |
| `LAST_COMPLETION.md` (9/21) | *"stay REPORTED forever"* | Dated 9/21 record — **supersession banner added** at its top, pointing here. |
| `board_log.tsv:339` | "class-rule adopted" | Append-only log; the 9/22 SIG-014 row records the supersession. |
| `PROME/inbox/2026-09-21_from-HAWK_L432-graded-…` | pointer: "includes the adopted class-rule verbatim" | **PROME is told**: packet `PROME/inbox/2026-09-22_from-HAWK_covert-claim-rule-revised-…`. |
| `memory/auto/finding_adopted_rule_drifts_toward_the_cheaper_test.md` (PROME-authored) | describes the old rule **as defective** — accurate | No edit (not mine). PROME is told about the §1 row-4 addition (the actor-assertion hole), in case it wants to extend it. |
| OSPREY / HANS / BRENT inboxes | WALTER's `-013` **and** WALTER's `-014` correction | WALTER's own routing, not HAWK's form. **No desk surface outside HAWK cites HAWK's rule** (repo grep for `CLASS-RULE` / `channel of record` / `acting undisclosed`: VERIFIED absent outside HAWK, WALTER logs, PROME inbox/state and the memory file). |

⇒ **The old form went to HAWK's own surfaces plus one PROME pointer. It did not reach any other desk's surface, and it never reached HAWK's KB.** The one consumer to tell is PROME.
