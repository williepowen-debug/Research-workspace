# HEARTBEAT commit-gate — RULED: REMOVED
**Ruled:** 2026-08-23, Will in-session, verbatim **"free it"** · **Owner:** PROME · **Status:** EXECUTED same sitting

---

## The ask
Will, unprompted: *"Is there an argument to be made for just allowing PROME to edit HEARTBEAT freely?"* — then, decisively: *"if approved - does this make the system simpler? Or does it create more work?"*

## Disclosure recorded at the top of the analysis
PROME flagged **before** presenting that it is structurally compromised on this question — it was being asked to adjudicate its own authority — and committed to measuring rather than reasoning from priors. **That disclosure is part of the record precisely because the analysis then walked PROME toward the option it benefits from most.** Any future citation of this ruling must carry the disclosure with it.

## The measurement (git, 60d window 2026-06-24 → 08-23)
| Measure | Value |
|---|---|
| HEARTBEAT commits | **117** (~2/day) |
| Carrying an explicit Will word | 82 (70%) |
| Carrying **none** | **35 (30%)** — the gate was already ~⅓ porous, on an unwritten line nobody had audited |
| Corrections/retractions of PROME's own content | **51 (44%)** |
| Will declines of a HEARTBEAT edit | **none found** |
| Artifacts existing only to service the gate | 6 DRAFT/proposal files · a named *"Will-gated residue"* spine-audit queue · batch/residue/owed language on 23/117 commits |

**The decisive instance:** the §8 gold figure Will was gated on **entered HEARTBEAT on 8/23 ~11:4x under his own verbatim "all approved"** (`9094e262f`) and was overturned ~2h later by BOND's non-author re-derivation. The gate's entire live workload was repairing something the gate had passed two hours earlier.

**Pattern, not exception:** the wrong-signed §4 base scalar, the §7 tier-inflated "PROME-verified" scope claims, and the retracted CCC "all April-2025" clause all entered through approvals and were caught downstream by BOND / HOMER / FERT / BRENT / RAV. **Measured detection rate of the gate on PROME's HEARTBEAT defects ≈ 0.**

**Base rate:** FORGE was ungated 2026-07-30 under this same argument. 20 commits since, 6 corrections, every one caught by a domain owner (BRENT, TERRY, HOMER) or PROME's own check. No incident in ~3.5 weeks.

## Counter-arguments recorded (not dismissed)
1. **`[[finding_deferral_rule_hides_its_own_cost]]`** — zero declines is equally consistent with "useless gate" and "perfectly deterrent gate." PROME has **no instrument** for edits it never proposed because it knew it had to ask. This remains unmeasured.
2. **HEARTBEAT is the one surface with no per-edit peer reader.** `PROME/BOOT.md` is explicit: PROME-facing memo, *domain agents do not read it*. PROME writes the regime memo PROME boot-reads — a closed loop whose only external observers were Will (per-edit) and the spine audit (weekly). **Ungating leaves the weekly audit alone in that role.** This is the strongest surviving objection and it is the reason the re-gate trigger below exists.
3. The gate may have been Will's own **orientation** mechanism rather than a quality check — unpriceable by PROME.

## Options and how the recommendation MOVED
| Option | Rule complexity | Machinery | Verdict |
|---|---|---|---|
| Status quo | Trivial ("ask Will") | Creates the DRAFTs, residue queue, batching, ~2 interrupts/day | Simple rule, **not** a simple system |
| **PROME's first rec** — reconciliation/assertion split, tested by *"name the owner surface + date this reconciles to"* | Highest; **self-adjudicated by PROME** | Deletes the residue queue but **adds** a per-edit classification, an audit leg, and text in an auto-injected file | **WITHDRAWN** — failed Will's simplicity test |
| **RULED: free it** | Lowest — one line struck | Deletes the DRAFTs, residue category, batching, interrupts. Adds nothing. | **ADOPTED** |

⚠️ **Honesty carried from the analysis: the withdrawn split would NOT have caught §8 either** (that was a reconciliation edit to MIDAS's named, dated self-retraction). Neither did the gate. **What caught it was commissioning a peer to re-derive as a non-author.** That is the transferable lesson, not the permission change.

## Scope of the ruling — what changed and what did NOT
**Freed (executed this sitting):**
- `PROME/CLAUDE.md` Ask-First list — `HEARTBEAT.md` struck, provenance + re-gate trigger encoded.
- `HEARTBEAT.md` footer — `**Committing = Will-gated.**` → PROME-standard. ★ **That footer's own "Approved Jun 4: Prome owns this file" line had contradicted the commit-gate for two months** — the ruling resolves an internal contradiction, it did not invent a grant.
- `PROME/AUTONOMY.md` — change-log row.

**⛔ NOT changed — do not read this ruling wider than it is:**
- **Root `CLAUDE.md` line 76** (PROME scope note naming HEARTBEAT) — root-doc lines stay **Will-gated**, FORGE precedent. Drafted for Will's word, presented same sitting so no mirror is left stale.
- **Root `CLAUDE.md` line 74** — domain agents still must **flag HEARTBEAT to PROME, never commit it.** Unaffected and still correct.
- **Every HEARTBEAT discipline survives:** re-base rule, verbatim cksum-verified archive, carried-claim re-verification, and the blind cold-reader pass before every re-base. **Ungating removed the APPROVAL step, not the DISCIPLINE.**
- **PROME still sets no thresholds.** Separately barred; untouched.
- Root `CLAUDE.md` and `AGENTS.md` core remain gated.

## Declared falsifier / re-gate trigger
**Any HEARTBEAT defect that reaches Will unrepaired past one weekly spine audit ⇒ re-gate.** One line out, one line back. Reversibility was an explicit part of the ruling's basis.

**Review:** first spine audit after 2026-08-23 checks HEARTBEAT edit provenance as a named leg.
