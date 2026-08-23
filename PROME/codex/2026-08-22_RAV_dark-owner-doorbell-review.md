# RAV review — WALTER dark-owner doorbell (WILL_QUEUE row 75) · PROME disposition

**Filed:** 2026-08-22 ~23:5x ET (S7, laptop). **Provenance:** relayed by Will into the live PROME session as a paste, prefaced *"I had RAV look it over."* No RAV-authored artifact exists in the tree for this review — the content existed ONLY in the live session until this file. Filed **verbatim, before any disposition**, per `[[finding_live_claim_in_a_closed_container_is_invisible]]` n+3 (2026-08-21 RAV near-miss: operator-relayed content files to disk verbatim, same session, before disposition-pointing).

⚠️ **A relayed review is a RECOMMENDATION, not an approval** — `[[finding_relayed_recommendation_is_not_an_approval]]`. Row 75 remains REGISTERED NOT RULED; only Will's own word rules it.

**Reviewed object:** PROME's adopt-with-three-amendments recommendation on `PROME/inbox/2026-08-22_from-WALTER_dark-owner-doorbell-proposal-rule-6s-missing-branch.md` (`f80ac13da`).

---

## §1 — VERBATIM (RAV, as relayed)

> I checked the current repo around this. My read: your proposed ruling is the right shape. I would rule adopt-with-three-amendments, and I would make amendment 2 load-bearing.
>
> What checks out:
>
> • WALTER’s proposal exists at PROME/inbox/2026-08-22_from-WALTER_dark-owner-doorbell-proposal-rule-6s-missing-branch.md.
> • WALTER’s raw delivery log has 669 ACTION rows all-time. I reproduced that exactly.
> • There are 34 ACTION handoffs still sitting at their original path.
> • Using signal-date as the age basis, 26 of those are dated Aug 20 or earlier. Using WALTER doctor’s stricter age basis, it reports 22 ACTION >2d after excluding pull-complete residues. So the direction is solid; the exact age-count needs the basis named.
> • HENRY and BROCK are correctly identified as active desks with unconsumed ACTION backlog: HENRY has 7, BROCK 6.
> • HENRY has 53 top-level WALTER files and 146 processed files; BROCK has 16 top-level and 70 processed. So “still at original path” is a meaningful proxy there.
> • The spot-check on the oldest HENRY ACTION item holds: SIG-W-20260807-001 appears only in the unread handoff itself, not elsewhere in HENRY’s tree.
> • WALTER’s own current status says the same core thing: the binding constraint is owner availability/consumption at landing time, not intake.
>
> Bottom line: the argument is valid, but I would sharpen the ruling before PROME acts.
>
> I would tell PROME:
>
> Rule row 75 adopt-with-three-amendments, not adopt-as-written.
>
> 1. Leg 3 must name a registered clock. Doorbell eligibility cannot rest on vibes like “market open soon” or “feels urgent.” It needs a named DOCKET row, GATES row, dated position expiry, or equivalent registered clock tied to the recipient’s owner decision. The clock must be logged in the doorbell recommendation.
>
> 2. A spawned desk drains its whole WALTER inbox, not just the triggering item. This is the most important amendment. The measured failure is not only dark-at-dispatch latency; it is non-consumption by desks that do boot. If PROME spends a domain session, the session should clear that desk’s WALTER backlog under the normal consume/integrate/commit standard. Otherwise the system pays for a spawn and leaves the actual queue disease untouched.
>
> 3. Measure items-drained-per-spawn and misses, not doorbells-per-dispatch. Doorbell rate is only a softness warning after a base rate exists. The real metrics are: how many WALTER items got integrated per spawn, how many registered-clock ACTION items missed before consumption, and how many recommended doorbells PROME declined. Do not wire WALTER’s “tighten above one-third” rule until enough observations exist.
>
> Two implementation cautions:
>
> • Normalize role case. Current delivery_log.tsv has older ACTION/INFO and newer lowercase action/info; a case-sensitive check will undercount newest rows.
> • A doorbell spawn must be a full owner session capable of editing and committing, not a read-only receiver. WALTER’s own spec already warns that read-only reading is not consumption and can create false clearance.
>
> One wording issue: “row 75” is ambiguous in the repo. In PROME/SCRATCH.md, it means the WILL_QUEUE row for WALTER’s doorbell. In PROME/DOCKET.tsv, line 75 is a Tricolor/OTTO date. PROME should name the artifact explicitly in the ruling so future agents do not chase the wrong row.
>
> My verdict: yes, adopt the project, but only with your amendments. Amendment 2 is the one that turns this from an alerting tweak into a real backlog-reduction mechanism.

---

## §2 — PROME VERIFICATION (run before disposition; nothing below accepted on relay)

| RAV claim | PROME check | Verdict |
|---|---|---|
| 669 ACTION rows all-time | `toupper($4)=="ACTION"` on delivery_log | ✅ 669 |
| 34 ACTION handoffs still at original path | re-ran | ✅ 34 |
| 26 dated ≤Aug-20 vs doctor's 22 >2d = **basis difference** | accepted; both bases named below | ✅ resolves PROME's flagged discrepancy |
| HENRY 7 / BROCK 6 unconsumed ACTION | re-ran | ✅ |
| HENRY 53 top / **146** processed; BROCK 16 / **70** | PROME counted 145 / 69 (`*.md`) | ✅ **off-by-one = `.gitkeep`** in each dir. Immaterial; PROME's `*.md` count is the handoff count |
| SIG-W-20260807-001 appears only in the unread handoff | re-ran grep across HENRY tree | ✅ not integrated at 15d |
| WALTER's STATUS says the same core thing | grepped `AGENTS/WALTER/STATUS.md` | ✅ **verbatim:** *"binding constraint is NOT intake; it is owner availability at the moment a signal lands"* (118 unconsumed >2d, 22 ACTION) |
| **Role case must be normalized** | counted the column | ✅ **MATERIAL, upgraded caution→requirement:** 478 `action` + 191 `ACTION` = 669. A case-sensitive check sees **191 of 669 — misses 71%, biased toward the NEWER rows** (lowercase is the newer convention). PROME's own figures used `.upper()` and are unaffected |
| **"row 75" is ambiguous** | read both artifacts | ✅ **CONFIRMED:** `PROME/DOCKET.tsv` line 75 = *"2026-12-04 Goodgame sentencing — Tricolor/auto-credit criminal chain, OTTO"*; `WILL_QUEUE` row 75 = the doorbell. Second live instance of the numbering-collision class root canon documents for "rule #6" |

⚠️ **One leg NOT reconciled:** WALTER's packet reads *"118 unconsumed >2d …, 22 of them ACTION, oldest 56d."* PROME's oldest unread **ACTION** is 22d (ZHAO `SIG-W-20260730-009`). WALTER's STATUS attaches no age to the 22, so "oldest 56d" most likely modifies the **118 (INFO included)**, not the 22 — **inferred, not proven.** Do not quote "oldest 56d" of the ACTION set until someone names the basis.

## §3 — DISPOSITION

**All three amendments CONCURRED, independently reached.** Both reviewers rate amendment 2 load-bearing. Adopted additions from RAV:

1. **Amd 1 +** *the registered clock must be **logged in the doorbell recommendation***. ADOPT — this is what makes the miss counter computable after the fact; without the logged clock, leg 3 is unauditable.
2. **Amd 2 +** *drain runs **under the normal consume/integrate/commit standard***. ADOPT — welds the drain to §3.5.2 so it cannot degrade into a read-and-file pass.
   > ⚠️ **SCOPE SUPERSEDED — §1's verbatim text above says "whole WALTER inbox" and that is now NARROWER than the live rule.** Will widened it to the desk's **WHOLE INBOX** on 2026-08-23 ~00:2x (verbatim *"approve both"*) after first live application: **TERRY held 10 unconsumed items and only ONE was WALTER's.** §1 is left unedited because it is a verbatim record of what RAV said — **do not act on the narrower scope quoted there.** Live letter → `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md` and `MESSAGING/CROSS_SESSION_MESSAGING.md` rule 6b. *(This is the `finding_live_claim_in_a_closed_container_is_invisible` shape pointed the other way: a verbatim block is a closed container, so a superseded claim inside one needs a forward pointer or it keeps reading as current.)*
3. **Amd 3 + a THIRD metric PROME did not have:** ***how many recommended doorbells PROME declined***. ADOPT, and it is the sharpest of the three — it is the only counter pointed at **PROME's own half of the loop**. If WALTER doorbells correctly and PROME declines everything, every other metric still reads healthy while the mechanism is dead. Same shape as the miss counter one level up.
4. **Role-case normalization:** caution → **named spec requirement** on the doctor check (71% undercount, newer-biased).
5. **Read-only caution:** CONCUR, already carried (WALTER §4 / spec §3.5.2).
6. **Citation discipline:** ADOPT. Cite **`WILL_QUEUE row 75`** in full, never bare "row 75." *(`PROME/SCRATCH.md` already uses the explicit form and needs no fix; the exposure is prose, commit messages, and packets. Root canon's "say which list you mean" rule is the governing precedent — extending it there is Will-gated, not taken unilaterally.)*
7. **Age basis:** ADOPT "name the basis" as a spec requirement on every count the doctor check emits.

⛔ **Status unchanged: `WILL_QUEUE` row 75 is REGISTERED NOT RULED.** RAV's verdict is a concurring recommendation; a relayed review never clears a Will-gated surface.

---

# §4 — RAV SECOND REVIEW (of the correction wave) — filed verbatim 2026-08-23 ~01:0x ET

**Provenance:** relayed by Will as a paste into the live PROME session, reviewing commits `5f5bc55fc → a9cd477c3`. No RAV-authored artifact exists in the tree. Filed **verbatim, before disposition**, same rule as §1. ⚠️ A relayed review is a RECOMMENDATION, never an approval.

> Pulled and checked.
>
> Bottom line: yes, this is a real correction, and it fixes the important damage before WALTER encodes from the bad version. The mirror fast-forwarded cleanly 5f5bc55fc -> a9cd477c3, repo clean afterward. The correction wave is now on origin/master.
>
> What landed:
>
> • PROME/CLAUDE.md Ask-First now has the three-outcome spawn/doorbell triage in the boot-read surface. This is the key thing you were worried about, and it is there.
> • PROME/AUTONOMY.md got the change-log row.
> • MESSAGING/CROSS_SESSION_MESSAGING.md now has rule 6b, including the dark-recipient branch, the full-owner-session requirement, and the whole-inbox drain.
> • PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md now carries the corrected ruling record, including the two corrections: HENRY/BROCK are low-cadence, and the first leg-3 wording was unfireable.
> • WALTER got an explicit encode packet at AGENTS/WALTER/inbox/2026-08-23_from-PROME_dark-owner-doorbell-RULED-adopt-with-three-amendments-your-encode.md that leads with the correction rather than burying it.
> • The memory lesson finding_path_scoped_git_log_measures_inbound_traffic was extended to n=2 and promoted hot; finding_test_the_guard_not_just_the_guarded got the “guard can never say yes” failure direction.
>
> My read: PROME did the right correction pattern. It did not quietly overwrite the mistake; it struck or superseded the bad claims, named the instrument failure, and pushed the corrected version into the files future agents will actually read. The RAV verbatim block was left untouched, with a forward pointer explaining where RAV’s “whole WALTER inbox” wording is now narrower than live rule. That is the right treatment for a closed/verbatim artifact.
>
> Two residual concerns:
>
> 1. Rule 6b still says “PROME decides, and PROME alone spawns.” In context it means “WALTER recommends; WALTER never spawns,” but standing alone it could be read too strongly against the tiered authority model. Cleaner future wording would be: “PROME triages the recommendation; PROME launches only where the tier permits or after Will approval.” I would not block on this tonight, because PROME/CLAUDE.md has the correct tiered rule, but it is a wording edge.
>
> 2. memory/auto/INDEX_COLD.md now has a bare - where the cold row was removed. memory_index_check passes, so it is not breaking slug coverage, but it is sloppy and worth cleaning at next PROME touch.
>
> Validation I ran:
>
> • rav-refresh-repo: clean fast-forward pull.
> • Checked commit log and the key diffs.
> • memory_index_check --strict --slug ...: passed for the three touched memory slugs.
> • prome_gate.py closeout: blocked on an unrelated DOCKET FERT lands-today disposition, not this doorbell correction.
> • Grepped for the bad claims. Remaining 94 commits, registered clock fires before, and whole WALTER inbox references are in struck/superseded/verbatim contexts with warnings, not live operative text.
>
> So: the correction is meaningful and mostly healthy. The earlier thesis inversion was serious, but PROME has now put the corrected version into the right authority surfaces.
