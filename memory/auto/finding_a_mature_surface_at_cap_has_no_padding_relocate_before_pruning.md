---
name: finding_a_mature_surface_at_cap_has_no_padding_relocate_before_pruning
description: A well-maintained surface at its byte cap has no padding left — pruning recovers almost nothing and cuts load-bearing text; the working instrument is RELOCATION to a proper home, after checking that the home exists (dedup-before-create / grep for an existing home).
metadata:
  type: feedback
symptoms: "rotation didn't fix it"; "four rotations in one day and still at cap"; "predicted ~3,500 B recovered, got 318 B"; "24 B of headroom with rc=0"; "every remaining bullet is the failure mode"; "compaction pass recovered nothing"
---

**Finding (n=2, uncoordinated, same day — 2026-09-17).** A mature, well-maintained surface sitting at its read cap has NO padding: the bytes that look like narrative are the FAILURE MODE, the part that must survive independently of the guard that cites it. Cutting stops working at that point and the remaining bytes are load-bearing. The instrument that works is RELOCATION — promote the lesson to the fleet index, move the standing rule to its proper owner surface — and the step that makes relocation safe is CHECKING FIRST whether a home already exists (BOND's dedup-before-create; TERRY's grep for the figure in the candidate homes), or relocation becomes duplication.

**Instances.**
- **BOND, `MEMORY.md` at 28,754 B (88%)** — predicted a code-enforced-rule compaction would recover ~3,500 B; it recovered **318 B** (11× miss). 29 bullets, median 852 B, largest 1,541 B: no fat. Six lessons relocated to the fleet index (four EXTENDED existing memories after dedup, two created) → one 804 B pointer; file to 22,033 B (68%), nothing deleted. Commit `acd6a2167`; KB-BND-308 neighbourhood.
- **TERRY, `STATUS.md` at 32,526 B (24 B of headroom, rc 0)** — FOUR rotations in one day did not fix it; TERRY named it STRUCTURAL and declined a fifth cut; two items were PROMOTED OUT because STATUS was their only home, after grepping `RISK_SCORING.md` and `RISK_RULES.md` for `1R ≡ $250` and finding it in neither (DOCKET L379, 2026-09-17).

**Why it matters.** "Rotate until under the line" is the right rule for a surface that accreted; it is the WRONG rule for one that was maintained, and the two look identical from the byte count. The tell is the miss ratio on the first pruning pass: if a pass predicted to recover kilobytes recovers a few hundred bytes, stop cutting and relocate.

**How to apply.** At a cap breach on a mature surface: (1) measure one pruning pass and compare recovered vs predicted; (2) if the miss is large, switch to relocation; (3) before moving any item, grep the candidate homes for it (dedup-before-create) and EXTEND rather than duplicate; (4) the surface keeps a pointer naming every relocated item. Related: [[finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag]] · [[finding_mechanize_the_cap_not_the_ritual]] · [[finding_hand_fixing_named_rows_is_not_fixing_the_class]].

**Provenance.** Raised by BOND (bond-3e) 2026-09-17 14:5x ET as n=1, then corrected by BOND itself to n=2 after checking its own bar for selective application (the MDE rule it declined at n=1 the same hour); PROME verified TERRY L379 at DOCKET and wrote this memory at the 16:0x closeout (carve-out ③).
