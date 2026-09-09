# Independent AI answer-key review

Reviewed 2026-09-08. Read scope: `corpus.json` and the scoring rules in `PROTOCOL.md` only. No model runs were performed and no corpus edits were made. This is independent AI validation of AI-authored keys; human validation remains **PENDING**.

Reviewed corpus SHA-256: `b257198bcf543b1c8ad58955c88ba642125db84aa2c10e2d07f9206b6bdc4fb1`.

**Result: all 168 initial/final field values are correct. Freeze is blocked on citation-eligibility omissions and one ambiguous field instruction.** There are 15 tasks, 84 distinct task fields, three practice tasks, twelve evaluation tasks, and exactly one designated no-change control in each evaluation family.

## Complete task inventory and value verification

Within each row, values appear in corpus field order. An arrow lists the final values when they differ; otherwise all listed values apply at both stages. These are independent evidence-based determinations, not merely key-to-key equality checks.

| Task | Initial values → final values | Reason |
|---|---|---|
| `sd_p01` | `2; sd_p01_a;sd_p01_c; 20; 8; MULTIPLE_ROOTS` (unchanged) | A and C independently collected 8/20 and 10/25; B/D are relays. |
| `sd_e01` | `1; sd_e01_a; 30; NORTH_ROOMS; SINGLE_ROOT` (unchanged) | 12/40 = 30%; B/C/E trace to A; D is a different population. |
| `sd_e02` | `1; sd_e02_a; 12; 18; UNKNOWN; SEPARATE_SESSION_COUNTS` (unchanged) | Both columns originate in one extract; overlap is not identified, so 30 distinct people is unjustified. |
| `sd_e03` | `2; sd_e03_a;sd_e03_b; 22; 100; 2031-02-09; MULTIPLE_ROOTS` → `1; sd_e03_a; 22; 100; 2031-02-09; SINGLE_ROOT` | D withdraws B's independent collection, not A's observations or date. |
| `sd_e04` | `2; sd_e04_a;sd_e04_c; 50; 80; MULTIPLE_ROOTS` (unchanged; control) | 10/50 and 16/80 each equal 20%; later summaries create no collections. |
| `su_p01` | `12; 12; 2031-02-28; MAPLE_HALL_STOOLS; PROVISIONAL` → `14; 12; 2031-02-28; MAPLE_HALL_STOOLS; FINAL` | Final release revises accepted count; original publication stays 12. |
| `su_e01` | `18; 18; 120; 2031-03-04; TEAL_ARCHIVE_JARS; PRELIMINARY` → `15; 18; 120; 2031-03-04; TEAL_ARCHIVE_JARS; FINAL` | Three incorrect crack classifications are removed; inventory scope/date stay fixed. |
| `su_e02` | `80; 52; 80; 2031-03-10; ALL_REGISTRATIONS; COMPLETED_INTRODUCTORY_SESSION` → `94; 70; 80; 2031-03-14; ALL_REGISTRATIONS; COMPLETED_INTRODUCTORY_SESSION` | Later snapshot adds registrations; 70 is the eligible subset of 94, not all registrations. |
| `su_e03` | `25; 25; 20; 80; PROVISIONAL; 2031-03-17` → `UNKNOWN; 25; 20; UNKNOWN; WITHDRAWN; 2031-03-17` | Unrecoverable denominator invalidates current rate, while distinct incidents/history remain valid. |
| `su_e04` | `42; 48; 2031-03-23; SILVER_WORKROOM_KITS; FINAL` (unchanged; control) | Later newsletter repeats history and explicitly acknowledges the accepted 42. |
| `ca_p01` | `8; 8; 40; 20; EAST_SHELF_OBJECTS` (unchanged) | 8/20 × 100 = 40; both copies of 6 are transcription errors. |
| `ca_e01` | `17; 17; 42.5; 40; BLUE_TILES; 2031-04-04` → `12; 12; 30; 40; BLUE_TILES; 2031-04-04` | 17−5 = 12 and 12/40 × 100 = 30; change propagates to both surfaces. |
| `ca_e02` | `90; 90; MINUTES; MINUTES; 6; FULL_ROUTE` (unchanged) | 5400/60 = 90 minutes; five-stop 80-minute measurement cannot replace full route. |
| `ca_e03` | `GLUE; GLUE; CONFIRMED; CONFIRMED; I-17; 24` → `UNKNOWN; UNKNOWN; UNRESOLVED; UNRESOLVED; I-17; 24` | Cause cannot be uniquely identified; uncertainty must propagate to both surfaces. |
| `ca_e04` | `24; 24; 40; 60; GARDEN_VAULT_OBJECTS; 2031-04-23` (unchanged; control) | Full inspection remains 24/60 = 40%; incomplete 23/55 draft has no superseding authority. |

The field IDs in every initial state, initial key and final key exactly equal the field specification IDs; no duplicates or extras exist. All 168 key values are strings. All source lists are nonempty, duplicate-free and refer to available stage-appropriate documents. All three controls (`sd_e04`, `su_e04`, `ca_e04`) have initial-state values equal to both stage keys, and therefore have zero required value changes. Canonical/downstream counts, durations, causes and statuses agree in every correction-task key.

## Blocker B1: citation-eligibility false negatives

A scorer that accepts only nonempty subsets of allowed IDs must allow every legitimate supporting component of an answer. For example, a correct percentage with both its observation and formula document is presently rejected in `ca_e01`, and a correct unchanged full-inspection count citing the update is rejected in `ca_e04`. A correction that invalidates one field must not invalidate an earlier source for unrelated, explicitly retained fields (`su_e03_a` still supports count 20).

The exact source-set additions below use **contributing evidence** eligibility: direct facts, arithmetic inputs/formulas, explicit provenance or authority statements, explicit preservation statements, and relays of the relevant fact may be included. They do not claim that each source alone proves the whole answer. That matches the existing allowance of `ca_e02_b` for duration 90 even though B supplies only the conversion rule and record schema. No addition restores a superseded value as current evidence.

Notation: `both` means `initial_key` and `final_key`. For each listed field, add the listed IDs to the existing `sources` array, remove duplicates, and sort lexicographically. Full task-prefixed IDs are required (for example, suffix `b` under `sd_p01` means `sd_p01_b`). Do not change any key value. Unlisted source sets remain as written.

| Task | Stage | Field(s) | Source suffix(es) to add | Supporting contribution |
|---|---|---|---|---|
| `sd_p01` | both | `root_count`, `root_ids`, `support`, `first_sample_size`, `first_chipped_count` | `b` | B explicitly traces A and repeats 40% of 20, implying 8 chipped tiles. |
| `sd_p01` | final | `root_count`, `root_ids`, `support` | `d` | D explicitly reports two teams and its relay provenance. |
| `sd_e01` | final | all five fields | `e` | E expressly relays the north-room finding via C and adds no observation. |
| `sd_e02` | final | `root_count`, `root_ids` | `b`, `c` | These still-valid explicit provenance statements were incorrectly removed from the final allowlist. |
| `sd_e02` | both | `population_scope` | `b`, `c` | Each bulletin covers its respective session column and confirms the separate-count construction. |
| `sd_e03` | both | `scratch_percent` | `c` | C explicitly repeats A's 22% rate; A's rate was not withdrawn. |
| `sd_e03` | final | `root_count`, `root_ids`, `support` | `a` | A supplies the surviving original root; a legitimate explanation may cite A together with D. |
| `sd_e04` | both | `root_count`, `root_ids`, `support` | `b`, `d` | Relays explicitly identify their respective underlying collections and absence of new observations. |
| `sd_e04` | final | all five fields | `e` | E explicitly summarizes the two earlier collections via B/D, with no additional inspection. |
| `su_p01` | initial | `release_status` | `c` | C explicitly calls the repeated count provisional. |
| `su_e01` | final | `original_published_count` | `d` | D establishes that the accepted 15 arose by removing three falsely classified cracks from A: original 18. |
| `su_e02` | initial | `current_snapshot_date` | `c` | C identifies A as its source and expressly excludes a later snapshot. |
| `su_e02` | both | `all_count_population` | `c` | C explicitly quotes total registrations; the population distinction remains valid. |
| `su_e03` | final | `missing_label_count` | `a` | Only denominator/rate are withdrawn; A's 20 incidents are affirmed by B/D. |
| `su_e04` | both | `provisional_published_count` | `b` | Final 42 plus six incomplete items in preliminary count recovers preliminary 48. |
| `su_e04` | both | `inventory_date`, `population` | `c` | C identifies B as authoritative for that inventory; B retains the inventory date/population. |
| `su_e04` | final | all five fields | `d` | D explicitly repeats original 48 and accepted final 42 and identifies the same releases/inventory. |
| `ca_p01` | both | `summary_damaged_count` | `c` | C maps the summary to the same inspected population as the canonical record. |
| `ca_p01` | both | `summary_damaged_percent` | `b`, `c` | B identifies the authoritative count; C supplies the denominator/formula. |
| `ca_p01` | final | all five fields | `d` | D directly reaffirms 8/20 and the east-shelf scope. |
| `ca_e01` | both | `canonical_defect_count`, `summary_defect_count`, `summary_defect_percent`, `sample_size`, `population` | `b` | B maps both records to the accepted inspection and explicitly gives the 40-tile denominator/formula. |
| `ca_e01` | both | `summary_defect_percent` | `c` | C confirms the denominator of 40. |
| `ca_e02` | both | `canonical_duration`, `summary_duration` | `c` | C confirms that both surfaces cover the complete six-stop route. |
| `ca_e02` | both | `population` | `b` | B explicitly specifies full-route records. |
| `ca_e02` | final | `canonical_duration`, `summary_duration`, `stop_count`, `population` | `d` | D preserves A's full-route measurement, while distinguishing five final stops from the excluded first stop. |
| `ca_e03` | both | `summary_cause`, `summary_cause_status`, `incident_id` | `b` | B explicitly maps current accepted cause/status to the summary and names I-17. |
| `ca_e04` | both | `canonical_marked_count`, `summary_marked_count`, `summary_marked_percent` | `b` | B establishes full-inspection scope, downstream equivalence and the percentage denominator/formula. |
| `ca_e04` | both | all six fields | `c` | C explicitly preserves A as the signed complete-inspection authority; it can legitimately accompany A. |
| `ca_e04` | final | all six fields | `d` | D explicitly reiterates the accepted 24/60 and preserves the signed complete-inspection result identified by C/A. |

The particularly direct, indisputable omissions are the repeated values in `ca_p01_d`, `ca_e04_d`, `su_e04_d`; the dropped provenance sources in `sd_e02`; the unaffected count in `su_e03_a`; `su_p01_c`'s explicit provisional status; `sd_e03_c`'s explicit rate; and formula/denominator documents cited together with observations. Broader provenance/preservation additions follow the contributing-evidence convention above. If a narrower convention is desired, it must be stated to workers and consistently applied across all keys before freeze; silently disallowing a valid supplemental source is not acceptable.

## Blocker B2: ambiguous session-overlap instruction

`sd_e02.population_scope` currently says: “Use DISJOINT_SESSION_COUNTS only if no attendee overlap is established.” This can mean either that zero overlap has been established or that overlap has not been established. The latter reading contradicts the intended key when overlap is unknown.

Replace the full description with this exact text:

> Exact enum: SEPARATE_SESSION_COUNTS or DISJOINT_SESSION_COUNTS. Use DISJOINT_SESSION_COUNTS only if the evidence establishes that no attendee attended both sessions; otherwise use SEPARATE_SESSION_COUNTS.

The existing key value `SEPARATE_SESSION_COUNTS` is correct under the task's intended meaning; no value edit is required.

## Advisories

1. **Citation eligibility is not evidentiary sufficiency.** Nonempty-subset scoring cannot require both an observational root and a provenance correction, or both a numerator and denominator. For example, A alone can be allowed for one component of a multi-root claim, and a formula-only source can be eligible for a derived numeric answer. The protocol already calls this predefined citation eligibility; retain that limited claim. Requiring complete proof would need a different scoring representation, such as alternative sufficient source sets, and is outside these corrections.
2. **Canonical numeric formatting could be stricter.** “Integer decimal string” does not explicitly reject leading zeroes or a leading plus sign; `ca_e01.summary_defect_percent` forbids trailing `.0` but does not unambiguously forbid `42.50`. Since exact string scoring rejects these mathematically equivalent forms, add a global worker-visible rule: “Write numbers in canonical base-10 form: no leading plus sign, no leading zeroes except for zero itself or values between zero and one, no exponent notation, and no trailing fractional zeroes; omit the decimal point for integer values.” All existing key values already satisfy this rule.
3. **Indirect support needs a declared convention.** An entire-collection relay and a document repeating only a named count are different. Do not automatically treat every linked document as reproducing every field; the table admits the relevant explicit observation, authority, preservation or schema contribution. Dates referring to a withdrawn different inspection (`sd_e03_b`) remain ineligible for A's date.
4. **Control equality concerns values.** After citation repairs, a control may appropriately gain allowed sources at the final stage while all answer values remain unchanged. Do not enforce byte equality of the two key objects as the no-change invariant.
5. **Human validation remains pending.** Independent AI validation and mechanical schema checks do not constitute human grading or a guarantee that all reasonable citation interpretations have been exhausted. Corrections should be applied and this review retained with the frozen inputs.

No arithmetic, history/current distinction, date, population, canonical/downstream equality or control-value blocker was found. No answer-key value corrections are proposed.

## Machine-readable exact source replacements

Replace only the indicated `sources` arrays. Omitted fields retain their existing arrays; every value remains unchanged. This JSON implements the additions table above.

```json
{
  "sd_p01": {
    "initial_key": {
      "root_count": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c"
      ],
      "root_ids": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c"
      ],
      "first_sample_size": [
        "sd_p01_a",
        "sd_p01_b"
      ],
      "first_chipped_count": [
        "sd_p01_a",
        "sd_p01_b"
      ],
      "support": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c"
      ]
    },
    "final_key": {
      "root_count": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c",
        "sd_p01_d"
      ],
      "root_ids": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c",
        "sd_p01_d"
      ],
      "first_sample_size": [
        "sd_p01_a",
        "sd_p01_b"
      ],
      "first_chipped_count": [
        "sd_p01_a",
        "sd_p01_b"
      ],
      "support": [
        "sd_p01_a",
        "sd_p01_b",
        "sd_p01_c",
        "sd_p01_d"
      ]
    }
  },
  "sd_e01": {
    "final_key": {
      "root_count": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "root_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "loose_latch_percent": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "population": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "support": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ]
    }
  },
  "sd_e02": {
    "final_key": {
      "root_count": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "root_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "population_scope": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ]
    },
    "initial_key": {
      "population_scope": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c"
      ]
    }
  },
  "sd_e03": {
    "initial_key": {
      "scratch_percent": [
        "sd_e03_a",
        "sd_e03_c"
      ]
    },
    "final_key": {
      "scratch_percent": [
        "sd_e03_a",
        "sd_e03_c",
        "sd_e03_d"
      ],
      "root_count": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "root_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "support": [
        "sd_e03_a",
        "sd_e03_d"
      ]
    }
  },
  "sd_e04": {
    "initial_key": {
      "root_count": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d"
      ],
      "root_ids": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d"
      ],
      "support": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d"
      ]
    },
    "final_key": {
      "root_count": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d",
        "sd_e04_e"
      ],
      "root_ids": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d",
        "sd_e04_e"
      ],
      "support": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_c",
        "sd_e04_d",
        "sd_e04_e"
      ],
      "first_sample_size": [
        "sd_e04_a",
        "sd_e04_b",
        "sd_e04_e"
      ],
      "second_sample_size": [
        "sd_e04_c",
        "sd_e04_d",
        "sd_e04_e"
      ]
    }
  },
  "su_p01": {
    "initial_key": {
      "release_status": [
        "su_p01_a",
        "su_p01_b",
        "su_p01_c"
      ]
    }
  },
  "su_e01": {
    "final_key": {
      "original_published_count": [
        "su_e01_a",
        "su_e01_c",
        "su_e01_d"
      ]
    }
  },
  "su_e02": {
    "initial_key": {
      "current_snapshot_date": [
        "su_e02_a",
        "su_e02_c"
      ],
      "all_count_population": [
        "su_e02_a",
        "su_e02_b",
        "su_e02_c"
      ]
    },
    "final_key": {
      "all_count_population": [
        "su_e02_a",
        "su_e02_b",
        "su_e02_c",
        "su_e02_d"
      ]
    }
  },
  "su_e03": {
    "final_key": {
      "missing_label_count": [
        "su_e03_a",
        "su_e03_b",
        "su_e03_d"
      ]
    }
  },
  "su_e04": {
    "initial_key": {
      "provisional_published_count": [
        "su_e04_a",
        "su_e04_b"
      ],
      "inventory_date": [
        "su_e04_a",
        "su_e04_b",
        "su_e04_c"
      ],
      "population": [
        "su_e04_a",
        "su_e04_b",
        "su_e04_c"
      ]
    },
    "final_key": {
      "provisional_published_count": [
        "su_e04_a",
        "su_e04_b",
        "su_e04_d"
      ],
      "inventory_date": [
        "su_e04_a",
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ],
      "population": [
        "su_e04_a",
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ],
      "current_completed_count": [
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ],
      "release_status": [
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ]
    }
  },
  "ca_p01": {
    "initial_key": {
      "summary_damaged_count": [
        "ca_p01_a",
        "ca_p01_b",
        "ca_p01_c"
      ],
      "summary_damaged_percent": [
        "ca_p01_a",
        "ca_p01_b",
        "ca_p01_c"
      ]
    },
    "final_key": {
      "summary_damaged_count": [
        "ca_p01_a",
        "ca_p01_b",
        "ca_p01_c",
        "ca_p01_d"
      ],
      "summary_damaged_percent": [
        "ca_p01_a",
        "ca_p01_b",
        "ca_p01_c",
        "ca_p01_d"
      ],
      "canonical_damaged_count": [
        "ca_p01_a",
        "ca_p01_b",
        "ca_p01_d"
      ],
      "sample_size": [
        "ca_p01_a",
        "ca_p01_c",
        "ca_p01_d"
      ],
      "population": [
        "ca_p01_a",
        "ca_p01_c",
        "ca_p01_d"
      ]
    }
  },
  "ca_e01": {
    "initial_key": {
      "canonical_defect_count": [
        "ca_e01_a",
        "ca_e01_b"
      ],
      "summary_defect_count": [
        "ca_e01_a",
        "ca_e01_b"
      ],
      "summary_defect_percent": [
        "ca_e01_a",
        "ca_e01_b",
        "ca_e01_c"
      ],
      "sample_size": [
        "ca_e01_a",
        "ca_e01_b",
        "ca_e01_c"
      ],
      "population": [
        "ca_e01_a",
        "ca_e01_b",
        "ca_e01_c"
      ]
    },
    "final_key": {
      "canonical_defect_count": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "summary_defect_count": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "summary_defect_percent": [
        "ca_e01_b",
        "ca_e01_c",
        "ca_e01_d"
      ],
      "sample_size": [
        "ca_e01_a",
        "ca_e01_b",
        "ca_e01_c",
        "ca_e01_d"
      ],
      "population": [
        "ca_e01_a",
        "ca_e01_b",
        "ca_e01_c",
        "ca_e01_d"
      ]
    }
  },
  "ca_e02": {
    "initial_key": {
      "canonical_duration": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c"
      ],
      "summary_duration": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c"
      ],
      "population": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c"
      ]
    },
    "final_key": {
      "canonical_duration": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c",
        "ca_e02_d"
      ],
      "summary_duration": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c",
        "ca_e02_d"
      ],
      "population": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_c",
        "ca_e02_d"
      ],
      "stop_count": [
        "ca_e02_a",
        "ca_e02_c",
        "ca_e02_d"
      ]
    }
  },
  "ca_e03": {
    "initial_key": {
      "summary_cause": [
        "ca_e03_a",
        "ca_e03_b"
      ],
      "summary_cause_status": [
        "ca_e03_a",
        "ca_e03_b"
      ],
      "incident_id": [
        "ca_e03_a",
        "ca_e03_b",
        "ca_e03_c"
      ]
    },
    "final_key": {
      "summary_cause": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "summary_cause_status": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "incident_id": [
        "ca_e03_a",
        "ca_e03_b",
        "ca_e03_c",
        "ca_e03_d"
      ]
    }
  },
  "ca_e04": {
    "initial_key": {
      "canonical_marked_count": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c"
      ],
      "summary_marked_count": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c"
      ],
      "summary_marked_percent": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c"
      ],
      "sample_size": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c"
      ],
      "population": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c"
      ],
      "inspection_date": [
        "ca_e04_a",
        "ca_e04_c"
      ]
    },
    "final_key": {
      "canonical_marked_count": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c",
        "ca_e04_d"
      ],
      "summary_marked_count": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c",
        "ca_e04_d"
      ],
      "summary_marked_percent": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c",
        "ca_e04_d"
      ],
      "sample_size": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c",
        "ca_e04_d"
      ],
      "population": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_c",
        "ca_e04_d"
      ],
      "inspection_date": [
        "ca_e04_a",
        "ca_e04_c",
        "ca_e04_d"
      ]
    }
  }
}
```
