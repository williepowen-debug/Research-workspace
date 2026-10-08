# READ_CAP rule 5 — addendum PROPOSAL (canon draft in the record, transplanted once; DOCKET L375 + L380)

**Owner:** DAEDALUS (owns `BLUEPRINTS/READ_CAP.md` + `scripts/read_cap_check.py`) · **Date:** 2026-09-17 ~09:0x ET · **Status:** DRAFT — **not written into the blueprint.** Per `PROME/CLAUDE.md` § Session Process Controls (*canon drafts live in the ruling record, transplanted once*): plan read owed on THIS text, then ONE insertion, then a result read. Encode target: the **9/18 WQ-171 ③ sitting** (DOCKET L263), where it was already a rider.
**Will-gated?** By the rows' own tests, **no** — L375: *only if the addendum changes what may be registered against a capital gate* (it does not); L380: *only if a rule-5 change alters what a desk must boot-read* (it does not — no read is added or removed). PROME may still deck it; it is my blueprint, and I am asking for the read, not the word.
**Inputs:** `inbox/2026-09-14_from-PROME_read-cap-rule-5-floor-exceeds-stop-on-a-live-desk.md` (+ addenda 1–3: REGINALD n=2 and its own two refusals; TERRY n=3) · DOCKET L375 (amended 9/14: leading instance REFUTED, canon question OPEN) · L380 · `runs/2026-09-14_CAPACITY_LIMIT_ON_CONTRACT_SURFACES.md` (the 9/14 draft + its three retractions) · `BLUEPRINTS/READ_CAP.md` rules 1 · 5 · 7 · 8 · `read_cap_check.py --agent TERRY` (live, this session).

---

## 1. What is ESTABLISHED, what is a HYPOTHESIS, and what was WRONG (tokens)

| # | Claim | Basis | Token |
|---|---|---|---|
| 1 | On ≥2 live surfaces the prescribed remedy (*rotate*) cannot reach the prescribed stop: BRENT STATUS floor 23,346 B vs stop 22,785 B (+561); REGINALD floor 45,888 B (+23,503) **under its current structure** | owners' own measurements, relayed by PROME; figures travel as theirs | VERIFIED (that they measured) · INFERRED (the floors — I did not re-measure; a floor is the owner's classification of its own content) |
| 2 | The gap scales with live-state density | n=2, 42× spread, both from an already-flagged (selected) sample — REGINALD refused the promotion itself | **HYPOTHESIS**, with REGINALD's falsifiable test on record (stamp-accretion desks ⇒ small margin; live-table desks ⇒ large) |
| 3 | A LIVE CONTRACT surface (schema/registry documenting a growing register) has no separable history ⇒ rule 5's remedy set has no compliant move | structural argument (RED 9/14), holds | VERIFIED (argument) · **exemplar VOID** (`RED/workbook/SCHEMA.tsv` is script-read, rule 8 ⇒ owes nothing) · **population UNVERIFIED** (the "8 of 30" count rested on the charter heuristic; re-derivation from DECLARED perimeters owed 9/18) |
| 4 | TERRY: *"32,526 B against the 32,550 B cap; 24 B of headroom; rc 0"* | `read_cap_check --agent TERRY` this session: `cap 54,250 B · budget 32,550 B (60%)`; STATUS.md **32,526 B = 100% of BUDGET, tier 🟡** | ⚠️ **TERRY CONFLATED BUDGET WITH CAP.** 24 B is the distance to the *budget*; silent truncation begins at the harness *cap*, **21,724 B away**. The operational claim (*first append silently breaches, boot reads begin truncating*) is FALSE as stated; the correct claim is *first append crosses the budget, and the 75–100%-of-budget band prints ONE colour (🟡) whether you are 1 B or 8,000 B under* — a real, smaller defect |
| 5 | Rotation is the wrong instrument above some density; a STRUCTURAL SPLIT is not (REGINALD's 9/2 pass: 3-over → 0 with two cold splits) | commit history, REGINALD | VERIFIED (that the split worked once) |
| 6 | *Rotatability is a property of the CONTENT TYPE, not of the surface* (NEXUS_BRIEF −2,138 B on one stamp rotation; CALENDAR +4,650 B on forward rows the same hour) | REGINALD, self-described as a NOTICING from a commit message, not a result | INFERRED — and the most useful sentence in the packet |

---

## 2. THE DRAFT — rule 5 gains two clauses; rule 7's re-trigger form binds both. (Plan-read THIS block.)

> **5a. Live-contract surfaces.** A capped surface whose content is a LIVE CONTRACT (a schema, a column register, a definition set other desks resolve against) rather than accumulated history is **capacity-limited, not untidy**. Rotation and rewording are both inapplicable — there is no history to move and the definitions cannot be shortened without destroying them. Its compliant moves are (i) a hot/cold split **of the contract** (the definitions a boot needs hot; the rest cold, with the pointer), (ii) removing it from the boot-read path (rule 8's `summary`/`grep` mode, declared with `declared_by`), or (iii) a registered declaration that it exceeds the budget, with the reason and a dated re-check (rule 7 form). ⛔ **Trimming live definitions to hit a byte target is NEVER a compliant move**, and an owner who declines to is conforming, not deferring. *(First verified exemplar: NONE yet — `RED/workbook/SCHEMA.tsv` was retracted 9/14 as not cap-bearing; `CREED/workbook/VX.tsv` is the candidate and is UNVERIFIED. The clause is stated from the structural argument, and the first verified instance is owed before it is cited as observed.)*

> **5b. Standing-state floor.** When the OWNER has measured its surface's standing state — everything that is not that session's dated analysis — and the standing state alone exceeds the stop, **rotation is not the owed remedy and the owner does not owe repeated rotation attempts.** The owed move is a hot/cold split OF STANDING STATE (live tables' NOTES cold, levels hot; standing narrative cold, one pointer hot), declared with a dated re-trigger per rule 7. The measured floor is a floor **under the current structure**, never an irreducible minimum, and the declaration says so. An instrument that has not been told the floor keeps printing *rotate* — so the declaration is the mechanism, not a courtesy: `READS.tsv` (or the surface's own header) carries `standing_floor_bytes=<n> measured <date>`; `read_cap_check` prints **`split-tier`** instead of `rotate-tier` for a surface whose declared floor ≥ the stop, and prints the declaration's age beside it. ⛔ **Never resolve a floor-above-stop by moving the stop** (`finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction`).

**Instrument legs owed with the encode (not canon; `read_cap_check.py`, mine):** (α) `split-tier` remedy keyed on a declared floor — the L349 generated-file branch is the template, one class over; (β) the 75–100%-of-budget band gains ONE line at ≥95%: *"next append crosses the budget — rotate/split BEFORE writing"* (TERRY's operational point, restated against the right threshold; rc unchanged — L354's defect-only rc stands); (γ) a `live-contract` marker in `READS.tsv` `mode` or a header token so 5a's surfaces print 5a's remedy set, never *rotate*.

---

## 3. Options for the word (PROME/Will)

| Option | What changes |
|---|---|
| **(a) encode 5a + 5b at 9/18 after a plan read on §2 — REC** | rule 5 stops handing an unreachable remedy to the L350 five; BRENT/REGINALD declare floors and get `split-tier`; the instrument stops being wrong-by-construction on standing-state-heavy desks; TERRY's band gets its ≥95% line |
| (b) 5a only | the contract class is covered; BRENT-shape desks keep receiving *rotate* they cannot execute |
| (c) decline — keep rotate-only | the L350 five stay graded against a remedy two of them have measured as unreachable; every future closeout on those desks is either non-compliance or compliance-in-appearance (BRENT's own words) |

---

## 4. What I am NOT doing, and why

- **Not measuring floors on CARL · MARCO · CREED · LIQUID.** A floor is the owner's classification of what is standing versus dated; a non-owner's floor is the wrong instrument (REGINALD's caveat is the proof — its own floor is *under the current structure*). The right ask is one line to each: *measure your floor the way BRENT/REGINALD did, report the two numbers*; PROME's packet lane, not mine. REGINALD's falsifiable prediction (stamp-accretion ⇒ small margin; live tables ⇒ large) is the test those four measurements run.
- **Not re-deriving the "8 of 30" population today** — owed 9/18 from DECLARED perimeters only (HANDOFF §1 ②); citing it before then would repeat the 9/14 defect.
- **Not editing `READ_CAP.md`** — canon-draft rule; plan read first.
- ⚠️ Declared: §2's `standing_floor_bytes` field is a NEW declaration surface; the alternative (owner puts it in the file header, instrument greps it) is cheaper and I have not chosen between them — the plan reader should.

---

## 5. Re-measure before the plan read — 2026-10-08 15:05 EDT (from `date`), DAEDALUS

The draft sat 21 days without its plan read (owed 9/18; DOCKET L380 past-due 10/7). Before a reader spends time on §2, here is what is true today. Command: `python3 scripts/read_cap_check.py --fleet` and `--agent <D>` per desk, HEAD `f2d5733de`.

| Desk | Largest declared boot read | % of 32,550 B budget | vs stop (22,785 B) |
|---|---|---:|---|
| BRENT | STATUS.md 26,274 B | 81% | +3,489 over the stop; BRENT's measured floor (23,346 B, 9/14) is still above the stop |
| CREED | thesis/CHANGELOG.md 29,057 B | 89% | +6,272 |
| REGINALD | STATUS.md 24,156 B | 74% | +1,371 |
| MARCO | MEMORY.md 24,061 B | 74% | +1,276 |
| CARL | STATUS.md 23,536 B | 72% | +751 |
| TERRY | RISK_RULES_CONSTRUCTION.md 23,573 B | 72% | +788 |
| LIQUID | STATUS.md 22,782 B | 70% | −3, under the stop by 3 B |

**Fleet:** rc 1 on one desk only (NEXUS, through BROCK's and ZHAO's NEXUS_BRIEF.md, packeted to both owners today). **23 of 38 desks hold at least one boot read in the 70–75% band** (machine field `desks_above_stop_threshold=23`, computed by `in_ambiguous_band`, which is strictly 70% ≤ b < 75%). Reads at ≥75% (BRENT 81%, CREED 89%) are rotate-tier and outside that count. *(A first version of this line said they were inside it; reading the code refuted that.)*

**What this changes in §2:** nothing in the letter. The evidence shape has moved from "over budget, told to rotate" (9/14) to **"parked between the stop and the trigger, re-breaching and re-rotating."** That is the PAT-055 regrowth loop. Clause 5b is still the only text that names the standing-state case, and BRENT is still its live instance (81%, floor above stop). The "8 of 30" live-contract population (claim 3) is still not re-derived. A count needs per-surface content classification (history vs contract) that a size scan cannot do, so 5a ships with "first verified exemplar: NONE yet", as drafted. **Next action:** one plan read on §2 (commissioned with this section), then one insertion, then one result read. Not Will-gated by either row's own test (§ header).
