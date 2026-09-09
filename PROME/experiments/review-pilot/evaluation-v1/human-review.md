# Human-review packet

Condition labels are omitted. Human validation is PENDING. See ../HUMAN_REVIEW_GUIDE.md before grading.

## OUTPUT-001

Assess whether at least 20 percent of sampled violet storage boxes have a bent corner. Count independent collections and preserve their separate sample sizes. Later summaries may repeat either collection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- first_sample_size: Boxes examined in sd_e04_a; integer decimal string.
- second_sample_size: Boxes examined in sd_e04_c; integer decimal string.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e04_a** — 2031-02-16. Collection One: original inspection of 50 violet storage boxes, with 10 bent corners.

**sd_e04_b** — 2031-02-17. Bulletin repeats Collection One from sd_e04_a; no boxes were examined for this bulletin.

**sd_e04_c** — 2031-02-18. Collection Two: a separate team independently inspected 80 different violet storage boxes, with 16 bent corners. Its observations were not taken from Collection One.

**sd_e04_d** — 2031-02-19. Digest reproduces Collection Two from sd_e04_c; it includes no new box observations.

**sd_e04_e** — 2031-02-20. Later overview cites sd_e04_b and sd_e04_d. It uses those documents solely as summaries of the two earlier collections, with no additional inspection.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "2"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "sd_e04_a;sd_e04_c"
    },
    {
      "field": "first_sample_size",
      "source_ids": [
        "sd_e04_a"
      ],
      "value": "50"
    },
    {
      "field": "second_sample_size",
      "source_ids": [
        "sd_e04_c"
      ],
      "value": "80"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "MULTIPLE_ROOTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-002

Maintain the accepted completed-kit count for the 2031-03-23 inventory and preserve the earlier provisional publication. Determine authority by what a document says about its scope and status, not simply by its publication date.

### Required fields
- current_completed_count: Accepted completed-kit count for the inventory; integer decimal string.
- provisional_published_count: Count in provisional publication su_e04_a; integer decimal string.
- inventory_date: Date the kits were inventoried; exact YYYY-MM-DD.
- population: Exact literal SILVER_WORKROOM_KITS.
- release_status: Exact enum: PROVISIONAL or FINAL.

### Supplied documents

**su_e04_a** — 2031-03-24. Provisional Silver workroom release: 48 completed kits in the 2031-03-23 inventory.

**su_e04_b** — 2031-03-26. Final inventory release supersedes su_e04_a: 42 completed Silver workroom kits as of 2031-03-23; six items in the preliminary count were incomplete.

**su_e04_c** — 2031-03-27. Current inventory index designates su_e04_b as the final authoritative release for that inventory.

**su_e04_d** — 2031-03-30. Historical newsletter: "The provisional publication announced 48 completed kits." This passage reproduces su_e04_a as an account of the preliminary announcement. It explicitly acknowledges the final count of 42 in su_e04_b and contains no new inventory or revision.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_completed_count",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "42"
    },
    {
      "field": "provisional_published_count",
      "source_ids": [
        "su_e04_a"
      ],
      "value": "48"
    },
    {
      "field": "inventory_date",
      "source_ids": [
        "su_e04_b"
      ],
      "value": "2031-03-23"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e04_b"
      ],
      "value": "SILVER_WORKROOM_KITS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-003

Reconcile the canonical Garden vault record and its downstream summary with the accepted complete inspection. Preserve already-correct fields when later material describes a partial draft. Both surfaces must represent the full inspection.

### Required fields
- canonical_marked_count: Marked-object count on the canonical full-inspection record; integer decimal string.
- summary_marked_count: Marked-object count on the downstream full-inspection summary; integer decimal string.
- summary_marked_percent: Full-inspection marked-object percentage; integer decimal string without percent sign.
- sample_size: Full-inspection sample size; integer decimal string.
- population: Exact literal GARDEN_VAULT_OBJECTS.
- inspection_date: Full-inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e04_a** — 2031-04-24. Signed complete Garden vault inspection: 24 marked objects out of 60 inspected on 2031-04-23. This is the accepted full-inspection result.

**ca_e04_b** — 2031-04-25. Record contract: canonical and downstream marked counts cover all 60 objects in the accepted Garden vault inspection. The summary percentage is marked count divided by 60 times 100.

**ca_e04_c** — 2031-04-25. Archive note: an earlier unfinished draft omitted the final tray. It cannot replace the signed complete inspection in ca_e04_a.

**ca_e04_d** — 2031-04-28. Catalog description of the recovered unfinished draft: it lists 23 marked objects out of 55 in the trays processed before the final tray. This is the incomplete draft described by ca_e04_c; it is not a correction to the accepted full-inspection result of 24 out of 60.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_percent",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "40"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "60"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "GARDEN_VAULT_OBJECTS"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "2031-04-23"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-004

Reconcile the canonical blue-tile record and its downstream inspection summary with the currently accepted inspection. Apply any revised defect count to both surfaces and recompute the summary rate while preserving unaffected fields.

### Required fields
- canonical_defect_count: Accepted defect count on the canonical record; integer decimal string.
- summary_defect_count: Accepted defect count in the downstream summary; integer decimal string.
- summary_defect_percent: Defect percentage in the downstream summary; decimal string with no trailing .0 and no percent sign.
- sample_size: Number of inspected tiles; integer decimal string.
- population: Exact literal BLUE_TILES.
- inspection_date: Tile inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e01_a** — 2031-04-05. Inspection release: 17 defective blue tiles among 40 tiles inspected on 2031-04-04.

**ca_e01_b** — 2031-04-06. Record contract: canonical count and downstream summary count refer to the same blue-tile inspection. Summary percentage equals the accepted defect count divided by 40, multiplied by 100.

**ca_e01_c** — 2031-04-06. Population manifest: exactly 40 blue tiles were inspected on 2031-04-04; no other tile color is in this sample.

**ca_e01_d** — 2031-04-08. Signed inspection correction supersedes the defect classification in ca_e01_a: five of the 17 marks were removable dust. The accepted defect count is 12. All 40 blue tiles remain in the sample; the inspection date remains 2031-04-04.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_defect_count",
      "source_ids": [
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_count",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_percent",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "30"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "40"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "BLUE_TILES"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "2031-04-04"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-005

Maintain the cause and cause-status fields for incident I-17 on both the canonical record and downstream summary. When the evidence no longer identifies a unique cause, express uncertainty on both surfaces. Preserve the incident identifier and inspection sample size.

### Required fields
- canonical_cause: Canonical incident cause; exact enum: GLUE, HEAT, or UNKNOWN.
- summary_cause: Cause shown in downstream summary; exact enum: GLUE, HEAT, or UNKNOWN.
- canonical_cause_status: Canonical cause status; exact enum: CONFIRMED or UNRESOLVED.
- summary_cause_status: Downstream cause status; exact enum: CONFIRMED or UNRESOLVED.
- incident_id: Exact incident identifier literal I-17.
- inspection_sample_size: Objects in the incident inspection sample; integer decimal string.

### Supplied documents

**ca_e03_a** — 2031-04-18. Signed incident record I-17: a panel separation was attributed to GLUE and its cause status was CONFIRMED. The incident was found during an inspection of 24 panels.

**ca_e03_b** — 2031-04-19. Summary specification: the downstream cause and status reproduce the currently accepted cause and status for incident I-17, including unresolved status if the cause cannot be uniquely established.

**ca_e03_c** — 2031-04-19. Inspection manifest lists 24 inspected panels and incident identifier I-17. Those identifiers and the sample size are independently checked.

**ca_e03_d** — 2031-04-21. Signed correction to incident I-17: the label used to assign GLUE in ca_e03_a belonged to an ambiguously matched test. The available evidence cannot distinguish GLUE from HEAT. The earlier confirmed attribution is withdrawn, and the cause is UNRESOLVED with no uniquely identified cause. Incident I-17 and the sample of 24 panels are unchanged.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_cause",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "summary_cause",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "canonical_cause_status",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "summary_cause_status",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "incident_id",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "I-17"
    },
    {
      "field": "inspection_sample_size",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "24"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-006

Assess whether at least 20 percent of sampled violet storage boxes have a bent corner. Count independent collections and preserve their separate sample sizes. Later summaries may repeat either collection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- first_sample_size: Boxes examined in sd_e04_a; integer decimal string.
- second_sample_size: Boxes examined in sd_e04_c; integer decimal string.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e04_a** — 2031-02-16. Collection One: original inspection of 50 violet storage boxes, with 10 bent corners.

**sd_e04_b** — 2031-02-17. Bulletin repeats Collection One from sd_e04_a; no boxes were examined for this bulletin.

**sd_e04_c** — 2031-02-18. Collection Two: a separate team independently inspected 80 different violet storage boxes, with 16 bent corners. Its observations were not taken from Collection One.

**sd_e04_d** — 2031-02-19. Digest reproduces Collection Two from sd_e04_c; it includes no new box observations.

**sd_e04_e** — 2031-02-20. Later overview cites sd_e04_b and sd_e04_d. It uses those documents solely as summaries of the two earlier collections, with no additional inspection.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "2"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "sd_e04_a;sd_e04_c"
    },
    {
      "field": "first_sample_size",
      "source_ids": [
        "sd_e04_a"
      ],
      "value": "50"
    },
    {
      "field": "second_sample_size",
      "source_ids": [
        "sd_e04_c"
      ],
      "value": "80"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "MULTIPLE_ROOTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-007

Maintain the accepted completed-kit count for the 2031-03-23 inventory and preserve the earlier provisional publication. Determine authority by what a document says about its scope and status, not simply by its publication date.

### Required fields
- current_completed_count: Accepted completed-kit count for the inventory; integer decimal string.
- provisional_published_count: Count in provisional publication su_e04_a; integer decimal string.
- inventory_date: Date the kits were inventoried; exact YYYY-MM-DD.
- population: Exact literal SILVER_WORKROOM_KITS.
- release_status: Exact enum: PROVISIONAL or FINAL.

### Supplied documents

**su_e04_a** — 2031-03-24. Provisional Silver workroom release: 48 completed kits in the 2031-03-23 inventory.

**su_e04_b** — 2031-03-26. Final inventory release supersedes su_e04_a: 42 completed Silver workroom kits as of 2031-03-23; six items in the preliminary count were incomplete.

**su_e04_c** — 2031-03-27. Current inventory index designates su_e04_b as the final authoritative release for that inventory.

**su_e04_d** — 2031-03-30. Historical newsletter: "The provisional publication announced 48 completed kits." This passage reproduces su_e04_a as an account of the preliminary announcement. It explicitly acknowledges the final count of 42 in su_e04_b and contains no new inventory or revision.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_completed_count",
      "source_ids": [
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ],
      "value": "42"
    },
    {
      "field": "provisional_published_count",
      "source_ids": [
        "su_e04_a",
        "su_e04_d"
      ],
      "value": "48"
    },
    {
      "field": "inventory_date",
      "source_ids": [
        "su_e04_a",
        "su_e04_b"
      ],
      "value": "2031-03-23"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e04_a",
        "su_e04_b"
      ],
      "value": "SILVER_WORKROOM_KITS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-008

Maintain the accepted completed-kit count for the 2031-03-23 inventory and preserve the earlier provisional publication. Determine authority by what a document says about its scope and status, not simply by its publication date.

### Required fields
- current_completed_count: Accepted completed-kit count for the inventory; integer decimal string.
- provisional_published_count: Count in provisional publication su_e04_a; integer decimal string.
- inventory_date: Date the kits were inventoried; exact YYYY-MM-DD.
- population: Exact literal SILVER_WORKROOM_KITS.
- release_status: Exact enum: PROVISIONAL or FINAL.

### Supplied documents

**su_e04_a** — 2031-03-24. Provisional Silver workroom release: 48 completed kits in the 2031-03-23 inventory.

**su_e04_b** — 2031-03-26. Final inventory release supersedes su_e04_a: 42 completed Silver workroom kits as of 2031-03-23; six items in the preliminary count were incomplete.

**su_e04_c** — 2031-03-27. Current inventory index designates su_e04_b as the final authoritative release for that inventory.

**su_e04_d** — 2031-03-30. Historical newsletter: "The provisional publication announced 48 completed kits." This passage reproduces su_e04_a as an account of the preliminary announcement. It explicitly acknowledges the final count of 42 in su_e04_b and contains no new inventory or revision.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_completed_count",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "42"
    },
    {
      "field": "provisional_published_count",
      "source_ids": [
        "su_e04_a"
      ],
      "value": "48"
    },
    {
      "field": "inventory_date",
      "source_ids": [
        "su_e04_a",
        "su_e04_b"
      ],
      "value": "2031-03-23"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e04_a",
        "su_e04_b"
      ],
      "value": "SILVER_WORKROOM_KITS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-009

Repair the duration fields on a canonical route record and its downstream summary. Both requested surfaces use minutes for the full route. Preserve the six-stop scope; a later segment-only measurement is not a replacement for the full route.

### Required fields
- canonical_duration: Full-route duration on canonical record in minutes; integer decimal string.
- summary_duration: Full-route duration on downstream summary in minutes; integer decimal string.
- canonical_unit: Exact literal MINUTES.
- summary_unit: Exact literal MINUTES.
- stop_count: Number of stops on the full route; integer decimal string.
- population: Exact literal FULL_ROUTE.

### Supplied documents

**ca_e02_a** — 2031-04-11. Original timed route log: total elapsed duration 5400 seconds, covering all six stops of the full route.

**ca_e02_b** — 2031-04-12. Record schema: the canonical full-route duration and downstream full-route duration are both stored in minutes, where 60 seconds equals one minute. The task-local numeric entries were copied directly from the seconds column without conversion.

**ca_e02_c** — 2031-04-12. Route manifest confirms six stops in the full route. Both required record surfaces describe the complete six-stop route.

**ca_e02_d** — 2031-04-14. Segment timing: the final five stops took 80 minutes on a separate timing exercise. This report excludes the first stop and does not revise the full-route measurement in ca_e02_a.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "summary_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "canonical_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "summary_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "stop_count",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_c"
      ],
      "value": "6"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_c"
      ],
      "value": "FULL_ROUTE"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-010

Assess independent observational support for the claim that 22 percent of the inspected ochre panels had a surface scratch. Use explicit provenance statements in force at the relevant stage. If a claimed independent inspection is withdrawn, remove that root without discarding the surviving inspection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- scratch_percent: Scratch rate from the surviving original inspection sd_e03_a; integer decimal string without percent sign.
- sample_size: Panel count in inspection sd_e03_a; integer decimal string.
- inspection_date: Date of inspection sd_e03_a; exact YYYY-MM-DD.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e03_a** — 2031-02-10. Original ochre-panel inspection: 22 scratched panels out of 100 inspected on 2031-02-09.

**sd_e03_b** — 2031-02-11. Separate inspection report: this report declares its observations to be a new independent collection of 100 other ochre panels on 2031-02-10, with 22 scratched. It declares no use of sd_e03_a.

**sd_e03_c** — 2031-02-12. Compilation repeats the 22 percent rate from sd_e03_a and sd_e03_b; it performs no inspection of its own.

**sd_e03_d** — 2031-02-13. Signed correction by the author of sd_e03_b: the claim of a separate inspection was erroneous. No panels were inspected for sd_e03_b; its counts were copied from sd_e03_a. Its claimed 2031-02-10 inspection is withdrawn. The observations and date in sd_e03_a remain valid.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "sd_e03_a"
    },
    {
      "field": "scratch_percent",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "22"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "100"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "2031-02-09"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-011

Reconcile the current accepted cracked-jar count with the first published estimate for the same inventory. Preserve the original publication as history and keep the observation date separate from the publication date.

### Required fields
- current_cracked_count: Current accepted count of cracked jars; integer decimal string.
- original_published_count: Cracked-jar count first published in su_e01_a, without retrospectively rewriting it; integer decimal string.
- inspected_count: Jars in the inventory population; integer decimal string.
- observation_date: Inventory observation date; exact YYYY-MM-DD.
- population: Exact literal TEAL_ARCHIVE_JARS.
- release_status: Exact enum: PRELIMINARY or FINAL.

### Supplied documents

**su_e01_a** — 2031-03-05. Preliminary publication: of 120 teal archive jars inventoried on 2031-03-04, 18 were classified as cracked.

**su_e01_b** — 2031-03-06. Inventory scope sheet confirms that the 120 jars are all jars in the teal archive and that the observation date is 2031-03-04.

**su_e01_c** — 2031-03-06. Visitor summary repeats the preliminary count of 18 from su_e01_a; no new inventory was taken.

**su_e01_d** — 2031-03-08. Final correction of su_e01_a: three seam marks were incorrectly counted as cracks. The accepted cracked-jar count is 15 out of the same 120 jars observed on 2031-03-04. No jars were added or removed.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_cracked_count",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "15"
    },
    {
      "field": "original_published_count",
      "source_ids": [
        "su_e01_a"
      ],
      "value": "18"
    },
    {
      "field": "inspected_count",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "120"
    },
    {
      "field": "observation_date",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "2031-03-04"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "TEAL_ARCHIVE_JARS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-012

Reconcile two counts of volunteers who attended the west and east sessions. Identify underlying enrollment-record roots, preserve the separate session counts, and determine the number of distinct volunteers across both sessions only if identifiable. A volunteer may attend both sessions.

### Required fields
- root_count: Independent enrollment-record roots underlying the two counts; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- west_count: Volunteers attending the west session; integer decimal string.
- east_count: Volunteers attending the east session; integer decimal string.
- distinct_volunteers: Distinct volunteers across both sessions; integer decimal string if identifiable, otherwise exact literal UNKNOWN.
- population_scope: Exact enum: SEPARATE_SESSION_COUNTS or DISJOINT_SESSION_COUNTS. Use DISJOINT_SESSION_COUNTS only if the evidence establishes that no attendee attended both sessions; otherwise use SEPARATE_SESSION_COUNTS.

### Supplied documents

**sd_e02_a** — 2031-02-06. Original enrollment extract: west session attendance 12; east session attendance 18. Attendee identifiers are withheld. The same volunteer may enroll in both. The extract contains no overlap count.

**sd_e02_b** — 2031-02-07. West-session bulletin reports 12 volunteers using only the west column in sd_e02_a. It did not collect a separate roster.

**sd_e02_c** — 2031-02-07. East-session bulletin reports 18 volunteers using only the east column in sd_e02_a. It did not collect a separate roster.

**sd_e02_d** — 2031-02-08. Enrollment custodian clarification: sd_e02_a remains the only record source. Whether any volunteers attended both sessions cannot be recovered from the supplied extract; no unique-person total is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "sd_e02_a"
    },
    {
      "field": "west_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b"
      ],
      "value": "12"
    },
    {
      "field": "east_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_c"
      ],
      "value": "18"
    },
    {
      "field": "distinct_volunteers",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "population_scope",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "SEPARATE_SESSION_COUNTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-013

Assess independent observational support for the claim that exactly 30 percent of inspected north rooms had a loose latch. Count independent datasets for that population. A report that cites a later relay of an earlier inspection does not create another observational root.

### Required fields
- root_count: Independent observational roots for the north-room claim; integer decimal string.
- root_ids: Root document IDs for that claim; semicolon-separated, sorted lexicographically, no spaces.
- loose_latch_percent: Percent of inspected north rooms with a loose latch; integer decimal string without percent sign.
- population: Exact population enum: NORTH_ROOMS, SOUTH_ROOMS, or ALL_ROOMS.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e01_a** — 2031-02-01. Original north-room inspection: 12 of 40 north rooms had a loose latch. All 40 rooms were inspected that day.

**sd_e01_b** — 2031-02-02. Facilities circular reports 12 loose latches among 40 north rooms, entirely from sd_e01_a. No second inspection was performed.

**sd_e01_c** — 2031-02-03. Maintenance newsletter reports a 30 percent north-room loose-latch rate, citing sd_e01_b as its sole data source. It has no new observations.

**sd_e01_d** — 2031-02-03. Independent south-room inspection: 6 of 20 south rooms had a loose latch. No north room was included.

**sd_e01_e** — 2031-02-04. Archive abstract cites the later newsletter sd_e01_c for the north-room finding. The abstract contains no original inspection or additional sample.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "value": "sd_e01_a"
    },
    {
      "field": "loose_latch_percent",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "30"
    },
    {
      "field": "population",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "NORTH_ROOMS"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-014

Update the registration snapshot for the Cedar craft course. Report all registrations separately from registrations eligible for the advanced session. Preserve the earlier all-registration count; never substitute an eligible subset for the full population.

### Required fields
- current_all_registrations: All registrations at the latest supplied snapshot; integer decimal string.
- current_eligible_registrations: Registrations eligible for the advanced session at that same latest snapshot; integer decimal string.
- earlier_all_registrations: All registrations at the 2031-03-10 snapshot; integer decimal string.
- current_snapshot_date: Latest supplied registration snapshot date, not publication date; exact YYYY-MM-DD.
- all_count_population: Population label for current_all_registrations; exact literal ALL_REGISTRATIONS.
- eligibility_basis: Exact literal COMPLETED_INTRODUCTORY_SESSION.

### Supplied documents

**su_e02_a** — 2031-03-11. Cedar course register, snapshot 2031-03-10: 80 registrations in all; 52 of those registrations are eligible for the advanced session.

**su_e02_b** — 2031-03-11. Course definitions: eligibility for the advanced session requires completion of the introductory session. The eligible count is a subset of all registrations.

**su_e02_c** — 2031-03-12. Course bulletin quotes 80 total registrations from su_e02_a. It contains no later snapshot.

**su_e02_d** — 2031-03-15. New register, snapshot 2031-03-14: 94 registrations in all, of which 70 completed the introductory session and are eligible for the advanced session. The headline "70 eligible registrations" refers only to the subset. The previous snapshot remains historical.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_all_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "94"
    },
    {
      "field": "current_eligible_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "70"
    },
    {
      "field": "earlier_all_registrations",
      "source_ids": [
        "su_e02_a"
      ],
      "value": "80"
    },
    {
      "field": "current_snapshot_date",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "2031-03-14"
    },
    {
      "field": "all_count_population",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "ALL_REGISTRATIONS"
    },
    {
      "field": "eligibility_basis",
      "source_ids": [
        "su_e02_b",
        "su_e02_d"
      ],
      "value": "COMPLETED_INTRODUCTORY_SESSION"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-015

Reconcile the canonical Garden vault record and its downstream summary with the accepted complete inspection. Preserve already-correct fields when later material describes a partial draft. Both surfaces must represent the full inspection.

### Required fields
- canonical_marked_count: Marked-object count on the canonical full-inspection record; integer decimal string.
- summary_marked_count: Marked-object count on the downstream full-inspection summary; integer decimal string.
- summary_marked_percent: Full-inspection marked-object percentage; integer decimal string without percent sign.
- sample_size: Full-inspection sample size; integer decimal string.
- population: Exact literal GARDEN_VAULT_OBJECTS.
- inspection_date: Full-inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e04_a** — 2031-04-24. Signed complete Garden vault inspection: 24 marked objects out of 60 inspected on 2031-04-23. This is the accepted full-inspection result.

**ca_e04_b** — 2031-04-25. Record contract: canonical and downstream marked counts cover all 60 objects in the accepted Garden vault inspection. The summary percentage is marked count divided by 60 times 100.

**ca_e04_c** — 2031-04-25. Archive note: an earlier unfinished draft omitted the final tray. It cannot replace the signed complete inspection in ca_e04_a.

**ca_e04_d** — 2031-04-28. Catalog description of the recovered unfinished draft: it lists 23 marked objects out of 55 in the trays processed before the final tray. This is the incomplete draft described by ca_e04_c; it is not a correction to the accepted full-inspection result of 24 out of 60.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_percent",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "40"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "60"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "GARDEN_VAULT_OBJECTS"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "2031-04-23"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-016

Reconcile the current accepted cracked-jar count with the first published estimate for the same inventory. Preserve the original publication as history and keep the observation date separate from the publication date.

### Required fields
- current_cracked_count: Current accepted count of cracked jars; integer decimal string.
- original_published_count: Cracked-jar count first published in su_e01_a, without retrospectively rewriting it; integer decimal string.
- inspected_count: Jars in the inventory population; integer decimal string.
- observation_date: Inventory observation date; exact YYYY-MM-DD.
- population: Exact literal TEAL_ARCHIVE_JARS.
- release_status: Exact enum: PRELIMINARY or FINAL.

### Supplied documents

**su_e01_a** — 2031-03-05. Preliminary publication: of 120 teal archive jars inventoried on 2031-03-04, 18 were classified as cracked.

**su_e01_b** — 2031-03-06. Inventory scope sheet confirms that the 120 jars are all jars in the teal archive and that the observation date is 2031-03-04.

**su_e01_c** — 2031-03-06. Visitor summary repeats the preliminary count of 18 from su_e01_a; no new inventory was taken.

**su_e01_d** — 2031-03-08. Final correction of su_e01_a: three seam marks were incorrectly counted as cracks. The accepted cracked-jar count is 15 out of the same 120 jars observed on 2031-03-04. No jars were added or removed.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_cracked_count",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "15"
    },
    {
      "field": "original_published_count",
      "source_ids": [
        "su_e01_a"
      ],
      "value": "18"
    },
    {
      "field": "inspected_count",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "120"
    },
    {
      "field": "observation_date",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "2031-03-04"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e01_b"
      ],
      "value": "TEAL_ARCHIVE_JARS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-017

Reconcile the canonical blue-tile record and its downstream inspection summary with the currently accepted inspection. Apply any revised defect count to both surfaces and recompute the summary rate while preserving unaffected fields.

### Required fields
- canonical_defect_count: Accepted defect count on the canonical record; integer decimal string.
- summary_defect_count: Accepted defect count in the downstream summary; integer decimal string.
- summary_defect_percent: Defect percentage in the downstream summary; decimal string with no trailing .0 and no percent sign.
- sample_size: Number of inspected tiles; integer decimal string.
- population: Exact literal BLUE_TILES.
- inspection_date: Tile inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e01_a** — 2031-04-05. Inspection release: 17 defective blue tiles among 40 tiles inspected on 2031-04-04.

**ca_e01_b** — 2031-04-06. Record contract: canonical count and downstream summary count refer to the same blue-tile inspection. Summary percentage equals the accepted defect count divided by 40, multiplied by 100.

**ca_e01_c** — 2031-04-06. Population manifest: exactly 40 blue tiles were inspected on 2031-04-04; no other tile color is in this sample.

**ca_e01_d** — 2031-04-08. Signed inspection correction supersedes the defect classification in ca_e01_a: five of the 17 marks were removable dust. The accepted defect count is 12. All 40 blue tiles remain in the sample; the inspection date remains 2031-04-04.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_defect_count",
      "source_ids": [
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_count",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_percent",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "30"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "40"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "BLUE_TILES"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "2031-04-04"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-018

Maintain the cause and cause-status fields for incident I-17 on both the canonical record and downstream summary. When the evidence no longer identifies a unique cause, express uncertainty on both surfaces. Preserve the incident identifier and inspection sample size.

### Required fields
- canonical_cause: Canonical incident cause; exact enum: GLUE, HEAT, or UNKNOWN.
- summary_cause: Cause shown in downstream summary; exact enum: GLUE, HEAT, or UNKNOWN.
- canonical_cause_status: Canonical cause status; exact enum: CONFIRMED or UNRESOLVED.
- summary_cause_status: Downstream cause status; exact enum: CONFIRMED or UNRESOLVED.
- incident_id: Exact incident identifier literal I-17.
- inspection_sample_size: Objects in the incident inspection sample; integer decimal string.

### Supplied documents

**ca_e03_a** — 2031-04-18. Signed incident record I-17: a panel separation was attributed to GLUE and its cause status was CONFIRMED. The incident was found during an inspection of 24 panels.

**ca_e03_b** — 2031-04-19. Summary specification: the downstream cause and status reproduce the currently accepted cause and status for incident I-17, including unresolved status if the cause cannot be uniquely established.

**ca_e03_c** — 2031-04-19. Inspection manifest lists 24 inspected panels and incident identifier I-17. Those identifiers and the sample size are independently checked.

**ca_e03_d** — 2031-04-21. Signed correction to incident I-17: the label used to assign GLUE in ca_e03_a belonged to an ambiguously matched test. The available evidence cannot distinguish GLUE from HEAT. The earlier confirmed attribution is withdrawn, and the cause is UNRESOLVED with no uniquely identified cause. Incident I-17 and the sample of 24 panels are unchanged.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_cause",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "summary_cause",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "canonical_cause_status",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "summary_cause_status",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "incident_id",
      "source_ids": [
        "ca_e03_a",
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "I-17"
    },
    {
      "field": "inspection_sample_size",
      "source_ids": [
        "ca_e03_a",
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "24"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-019

Maintain the accepted missing-label rate for the copper drawer inspection. Preserve the original published percentage and any count that remains valid if the rate is withdrawn. UNKNOWN means the supplied evidence does not establish a current accepted value.

### Required fields
- current_percent: Accepted percentage of inspected drawers missing labels; integer decimal string without percent sign if established, otherwise exact literal UNKNOWN.
- original_published_percent: Percentage printed in the original publication su_e03_a; integer decimal string without percent sign.
- missing_label_count: Accepted number of drawers missing labels; integer decimal string.
- accepted_denominator: Accepted number of inspected drawers used for the rate; integer decimal string if established, otherwise exact literal UNKNOWN.
- rate_status: Exact enum: PROVISIONAL or WITHDRAWN.
- inspection_date: Date of the drawer inspection; exact YYYY-MM-DD.

### Supplied documents

**su_e03_a** — 2031-03-18. Provisional copper drawer inspection report for 2031-03-17: 20 drawers lacked labels out of 80 inspected drawers, a rate of 25 percent.

**su_e03_b** — 2031-03-18. Label incident ledger independently lists the same 20 distinct drawers missing labels on 2031-03-17. It does not enumerate all inspected drawers.

**su_e03_c** — 2031-03-19. Display card quotes the provisional 25 percent rate from su_e03_a.

**su_e03_d** — 2031-03-20. Custodian correction: the total of 80 in su_e03_a was assembled from overlapping inspection batches. The true inspected denominator cannot be reconstructed from available records. The 20 distinct missing-label incidents in su_e03_b remain verified for 2031-03-17. The 25 percent rate is withdrawn; no replacement percentage or denominator is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_percent",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "original_published_percent",
      "source_ids": [
        "su_e03_a"
      ],
      "value": "25"
    },
    {
      "field": "missing_label_count",
      "source_ids": [
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "20"
    },
    {
      "field": "accepted_denominator",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "rate_status",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "WITHDRAWN"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "su_e03_a",
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "2031-03-17"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-020

Reconcile two counts of volunteers who attended the west and east sessions. Identify underlying enrollment-record roots, preserve the separate session counts, and determine the number of distinct volunteers across both sessions only if identifiable. A volunteer may attend both sessions.

### Required fields
- root_count: Independent enrollment-record roots underlying the two counts; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- west_count: Volunteers attending the west session; integer decimal string.
- east_count: Volunteers attending the east session; integer decimal string.
- distinct_volunteers: Distinct volunteers across both sessions; integer decimal string if identifiable, otherwise exact literal UNKNOWN.
- population_scope: Exact enum: SEPARATE_SESSION_COUNTS or DISJOINT_SESSION_COUNTS. Use DISJOINT_SESSION_COUNTS only if the evidence establishes that no attendee attended both sessions; otherwise use SEPARATE_SESSION_COUNTS.

### Supplied documents

**sd_e02_a** — 2031-02-06. Original enrollment extract: west session attendance 12; east session attendance 18. Attendee identifiers are withheld. The same volunteer may enroll in both. The extract contains no overlap count.

**sd_e02_b** — 2031-02-07. West-session bulletin reports 12 volunteers using only the west column in sd_e02_a. It did not collect a separate roster.

**sd_e02_c** — 2031-02-07. East-session bulletin reports 18 volunteers using only the east column in sd_e02_a. It did not collect a separate roster.

**sd_e02_d** — 2031-02-08. Enrollment custodian clarification: sd_e02_a remains the only record source. Whether any volunteers attended both sessions cannot be recovered from the supplied extract; no unique-person total is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "sd_e02_a"
    },
    {
      "field": "west_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b"
      ],
      "value": "12"
    },
    {
      "field": "east_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_c"
      ],
      "value": "18"
    },
    {
      "field": "distinct_volunteers",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "population_scope",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "SEPARATE_SESSION_COUNTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-021

Reconcile the canonical blue-tile record and its downstream inspection summary with the currently accepted inspection. Apply any revised defect count to both surfaces and recompute the summary rate while preserving unaffected fields.

### Required fields
- canonical_defect_count: Accepted defect count on the canonical record; integer decimal string.
- summary_defect_count: Accepted defect count in the downstream summary; integer decimal string.
- summary_defect_percent: Defect percentage in the downstream summary; decimal string with no trailing .0 and no percent sign.
- sample_size: Number of inspected tiles; integer decimal string.
- population: Exact literal BLUE_TILES.
- inspection_date: Tile inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e01_a** — 2031-04-05. Inspection release: 17 defective blue tiles among 40 tiles inspected on 2031-04-04.

**ca_e01_b** — 2031-04-06. Record contract: canonical count and downstream summary count refer to the same blue-tile inspection. Summary percentage equals the accepted defect count divided by 40, multiplied by 100.

**ca_e01_c** — 2031-04-06. Population manifest: exactly 40 blue tiles were inspected on 2031-04-04; no other tile color is in this sample.

**ca_e01_d** — 2031-04-08. Signed inspection correction supersedes the defect classification in ca_e01_a: five of the 17 marks were removable dust. The accepted defect count is 12. All 40 blue tiles remain in the sample; the inspection date remains 2031-04-04.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_defect_count",
      "source_ids": [
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_count",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_percent",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "30"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "40"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "BLUE_TILES"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "2031-04-04"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-022

Update the registration snapshot for the Cedar craft course. Report all registrations separately from registrations eligible for the advanced session. Preserve the earlier all-registration count; never substitute an eligible subset for the full population.

### Required fields
- current_all_registrations: All registrations at the latest supplied snapshot; integer decimal string.
- current_eligible_registrations: Registrations eligible for the advanced session at that same latest snapshot; integer decimal string.
- earlier_all_registrations: All registrations at the 2031-03-10 snapshot; integer decimal string.
- current_snapshot_date: Latest supplied registration snapshot date, not publication date; exact YYYY-MM-DD.
- all_count_population: Population label for current_all_registrations; exact literal ALL_REGISTRATIONS.
- eligibility_basis: Exact literal COMPLETED_INTRODUCTORY_SESSION.

### Supplied documents

**su_e02_a** — 2031-03-11. Cedar course register, snapshot 2031-03-10: 80 registrations in all; 52 of those registrations are eligible for the advanced session.

**su_e02_b** — 2031-03-11. Course definitions: eligibility for the advanced session requires completion of the introductory session. The eligible count is a subset of all registrations.

**su_e02_c** — 2031-03-12. Course bulletin quotes 80 total registrations from su_e02_a. It contains no later snapshot.

**su_e02_d** — 2031-03-15. New register, snapshot 2031-03-14: 94 registrations in all, of which 70 completed the introductory session and are eligible for the advanced session. The headline "70 eligible registrations" refers only to the subset. The previous snapshot remains historical.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_all_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "94"
    },
    {
      "field": "current_eligible_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "70"
    },
    {
      "field": "earlier_all_registrations",
      "source_ids": [
        "su_e02_a"
      ],
      "value": "80"
    },
    {
      "field": "current_snapshot_date",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "2031-03-14"
    },
    {
      "field": "all_count_population",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "ALL_REGISTRATIONS"
    },
    {
      "field": "eligibility_basis",
      "source_ids": [
        "su_e02_b",
        "su_e02_d"
      ],
      "value": "COMPLETED_INTRODUCTORY_SESSION"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-023

Assess whether at least 20 percent of sampled violet storage boxes have a bent corner. Count independent collections and preserve their separate sample sizes. Later summaries may repeat either collection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- first_sample_size: Boxes examined in sd_e04_a; integer decimal string.
- second_sample_size: Boxes examined in sd_e04_c; integer decimal string.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e04_a** — 2031-02-16. Collection One: original inspection of 50 violet storage boxes, with 10 bent corners.

**sd_e04_b** — 2031-02-17. Bulletin repeats Collection One from sd_e04_a; no boxes were examined for this bulletin.

**sd_e04_c** — 2031-02-18. Collection Two: a separate team independently inspected 80 different violet storage boxes, with 16 bent corners. Its observations were not taken from Collection One.

**sd_e04_d** — 2031-02-19. Digest reproduces Collection Two from sd_e04_c; it includes no new box observations.

**sd_e04_e** — 2031-02-20. Later overview cites sd_e04_b and sd_e04_d. It uses those documents solely as summaries of the two earlier collections, with no additional inspection.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "2"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "sd_e04_a;sd_e04_c"
    },
    {
      "field": "first_sample_size",
      "source_ids": [
        "sd_e04_a"
      ],
      "value": "50"
    },
    {
      "field": "second_sample_size",
      "source_ids": [
        "sd_e04_c"
      ],
      "value": "80"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "MULTIPLE_ROOTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-024

Maintain the accepted missing-label rate for the copper drawer inspection. Preserve the original published percentage and any count that remains valid if the rate is withdrawn. UNKNOWN means the supplied evidence does not establish a current accepted value.

### Required fields
- current_percent: Accepted percentage of inspected drawers missing labels; integer decimal string without percent sign if established, otherwise exact literal UNKNOWN.
- original_published_percent: Percentage printed in the original publication su_e03_a; integer decimal string without percent sign.
- missing_label_count: Accepted number of drawers missing labels; integer decimal string.
- accepted_denominator: Accepted number of inspected drawers used for the rate; integer decimal string if established, otherwise exact literal UNKNOWN.
- rate_status: Exact enum: PROVISIONAL or WITHDRAWN.
- inspection_date: Date of the drawer inspection; exact YYYY-MM-DD.

### Supplied documents

**su_e03_a** — 2031-03-18. Provisional copper drawer inspection report for 2031-03-17: 20 drawers lacked labels out of 80 inspected drawers, a rate of 25 percent.

**su_e03_b** — 2031-03-18. Label incident ledger independently lists the same 20 distinct drawers missing labels on 2031-03-17. It does not enumerate all inspected drawers.

**su_e03_c** — 2031-03-19. Display card quotes the provisional 25 percent rate from su_e03_a.

**su_e03_d** — 2031-03-20. Custodian correction: the total of 80 in su_e03_a was assembled from overlapping inspection batches. The true inspected denominator cannot be reconstructed from available records. The 20 distinct missing-label incidents in su_e03_b remain verified for 2031-03-17. The 25 percent rate is withdrawn; no replacement percentage or denominator is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_percent",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "original_published_percent",
      "source_ids": [
        "su_e03_a"
      ],
      "value": "25"
    },
    {
      "field": "missing_label_count",
      "source_ids": [
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "20"
    },
    {
      "field": "accepted_denominator",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "rate_status",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "WITHDRAWN"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "su_e03_a",
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "2031-03-17"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-025

Assess independent observational support for the claim that 22 percent of the inspected ochre panels had a surface scratch. Use explicit provenance statements in force at the relevant stage. If a claimed independent inspection is withdrawn, remove that root without discarding the surviving inspection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- scratch_percent: Scratch rate from the surviving original inspection sd_e03_a; integer decimal string without percent sign.
- sample_size: Panel count in inspection sd_e03_a; integer decimal string.
- inspection_date: Date of inspection sd_e03_a; exact YYYY-MM-DD.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e03_a** — 2031-02-10. Original ochre-panel inspection: 22 scratched panels out of 100 inspected on 2031-02-09.

**sd_e03_b** — 2031-02-11. Separate inspection report: this report declares its observations to be a new independent collection of 100 other ochre panels on 2031-02-10, with 22 scratched. It declares no use of sd_e03_a.

**sd_e03_c** — 2031-02-12. Compilation repeats the 22 percent rate from sd_e03_a and sd_e03_b; it performs no inspection of its own.

**sd_e03_d** — 2031-02-13. Signed correction by the author of sd_e03_b: the claim of a separate inspection was erroneous. No panels were inspected for sd_e03_b; its counts were copied from sd_e03_a. Its claimed 2031-02-10 inspection is withdrawn. The observations and date in sd_e03_a remain valid.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "sd_e03_a"
    },
    {
      "field": "scratch_percent",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "22"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "100"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "2031-02-09"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-026

Assess whether at least 20 percent of sampled violet storage boxes have a bent corner. Count independent collections and preserve their separate sample sizes. Later summaries may repeat either collection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- first_sample_size: Boxes examined in sd_e04_a; integer decimal string.
- second_sample_size: Boxes examined in sd_e04_c; integer decimal string.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e04_a** — 2031-02-16. Collection One: original inspection of 50 violet storage boxes, with 10 bent corners.

**sd_e04_b** — 2031-02-17. Bulletin repeats Collection One from sd_e04_a; no boxes were examined for this bulletin.

**sd_e04_c** — 2031-02-18. Collection Two: a separate team independently inspected 80 different violet storage boxes, with 16 bent corners. Its observations were not taken from Collection One.

**sd_e04_d** — 2031-02-19. Digest reproduces Collection Two from sd_e04_c; it includes no new box observations.

**sd_e04_e** — 2031-02-20. Later overview cites sd_e04_b and sd_e04_d. It uses those documents solely as summaries of the two earlier collections, with no additional inspection.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "2"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "sd_e04_a;sd_e04_c"
    },
    {
      "field": "first_sample_size",
      "source_ids": [
        "sd_e04_a"
      ],
      "value": "50"
    },
    {
      "field": "second_sample_size",
      "source_ids": [
        "sd_e04_c"
      ],
      "value": "80"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e04_a",
        "sd_e04_c"
      ],
      "value": "MULTIPLE_ROOTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-027

Update the registration snapshot for the Cedar craft course. Report all registrations separately from registrations eligible for the advanced session. Preserve the earlier all-registration count; never substitute an eligible subset for the full population.

### Required fields
- current_all_registrations: All registrations at the latest supplied snapshot; integer decimal string.
- current_eligible_registrations: Registrations eligible for the advanced session at that same latest snapshot; integer decimal string.
- earlier_all_registrations: All registrations at the 2031-03-10 snapshot; integer decimal string.
- current_snapshot_date: Latest supplied registration snapshot date, not publication date; exact YYYY-MM-DD.
- all_count_population: Population label for current_all_registrations; exact literal ALL_REGISTRATIONS.
- eligibility_basis: Exact literal COMPLETED_INTRODUCTORY_SESSION.

### Supplied documents

**su_e02_a** — 2031-03-11. Cedar course register, snapshot 2031-03-10: 80 registrations in all; 52 of those registrations are eligible for the advanced session.

**su_e02_b** — 2031-03-11. Course definitions: eligibility for the advanced session requires completion of the introductory session. The eligible count is a subset of all registrations.

**su_e02_c** — 2031-03-12. Course bulletin quotes 80 total registrations from su_e02_a. It contains no later snapshot.

**su_e02_d** — 2031-03-15. New register, snapshot 2031-03-14: 94 registrations in all, of which 70 completed the introductory session and are eligible for the advanced session. The headline "70 eligible registrations" refers only to the subset. The previous snapshot remains historical.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_all_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "94"
    },
    {
      "field": "current_eligible_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "70"
    },
    {
      "field": "earlier_all_registrations",
      "source_ids": [
        "su_e02_a"
      ],
      "value": "80"
    },
    {
      "field": "current_snapshot_date",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "2031-03-14"
    },
    {
      "field": "all_count_population",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "ALL_REGISTRATIONS"
    },
    {
      "field": "eligibility_basis",
      "source_ids": [
        "su_e02_b",
        "su_e02_d"
      ],
      "value": "COMPLETED_INTRODUCTORY_SESSION"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-028

Reconcile the canonical Garden vault record and its downstream summary with the accepted complete inspection. Preserve already-correct fields when later material describes a partial draft. Both surfaces must represent the full inspection.

### Required fields
- canonical_marked_count: Marked-object count on the canonical full-inspection record; integer decimal string.
- summary_marked_count: Marked-object count on the downstream full-inspection summary; integer decimal string.
- summary_marked_percent: Full-inspection marked-object percentage; integer decimal string without percent sign.
- sample_size: Full-inspection sample size; integer decimal string.
- population: Exact literal GARDEN_VAULT_OBJECTS.
- inspection_date: Full-inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e04_a** — 2031-04-24. Signed complete Garden vault inspection: 24 marked objects out of 60 inspected on 2031-04-23. This is the accepted full-inspection result.

**ca_e04_b** — 2031-04-25. Record contract: canonical and downstream marked counts cover all 60 objects in the accepted Garden vault inspection. The summary percentage is marked count divided by 60 times 100.

**ca_e04_c** — 2031-04-25. Archive note: an earlier unfinished draft omitted the final tray. It cannot replace the signed complete inspection in ca_e04_a.

**ca_e04_d** — 2031-04-28. Catalog description of the recovered unfinished draft: it lists 23 marked objects out of 55 in the trays processed before the final tray. This is the incomplete draft described by ca_e04_c; it is not a correction to the accepted full-inspection result of 24 out of 60.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_percent",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "40"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "60"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "GARDEN_VAULT_OBJECTS"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "2031-04-23"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-029

Assess independent observational support for the claim that exactly 30 percent of inspected north rooms had a loose latch. Count independent datasets for that population. A report that cites a later relay of an earlier inspection does not create another observational root.

### Required fields
- root_count: Independent observational roots for the north-room claim; integer decimal string.
- root_ids: Root document IDs for that claim; semicolon-separated, sorted lexicographically, no spaces.
- loose_latch_percent: Percent of inspected north rooms with a loose latch; integer decimal string without percent sign.
- population: Exact population enum: NORTH_ROOMS, SOUTH_ROOMS, or ALL_ROOMS.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e01_a** — 2031-02-01. Original north-room inspection: 12 of 40 north rooms had a loose latch. All 40 rooms were inspected that day.

**sd_e01_b** — 2031-02-02. Facilities circular reports 12 loose latches among 40 north rooms, entirely from sd_e01_a. No second inspection was performed.

**sd_e01_c** — 2031-02-03. Maintenance newsletter reports a 30 percent north-room loose-latch rate, citing sd_e01_b as its sole data source. It has no new observations.

**sd_e01_d** — 2031-02-03. Independent south-room inspection: 6 of 20 south rooms had a loose latch. No north room was included.

**sd_e01_e** — 2031-02-04. Archive abstract cites the later newsletter sd_e01_c for the north-room finding. The abstract contains no original inspection or additional sample.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "sd_e01_a"
    },
    {
      "field": "loose_latch_percent",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "30"
    },
    {
      "field": "population",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "NORTH_ROOMS"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-030

Repair the duration fields on a canonical route record and its downstream summary. Both requested surfaces use minutes for the full route. Preserve the six-stop scope; a later segment-only measurement is not a replacement for the full route.

### Required fields
- canonical_duration: Full-route duration on canonical record in minutes; integer decimal string.
- summary_duration: Full-route duration on downstream summary in minutes; integer decimal string.
- canonical_unit: Exact literal MINUTES.
- summary_unit: Exact literal MINUTES.
- stop_count: Number of stops on the full route; integer decimal string.
- population: Exact literal FULL_ROUTE.

### Supplied documents

**ca_e02_a** — 2031-04-11. Original timed route log: total elapsed duration 5400 seconds, covering all six stops of the full route.

**ca_e02_b** — 2031-04-12. Record schema: the canonical full-route duration and downstream full-route duration are both stored in minutes, where 60 seconds equals one minute. The task-local numeric entries were copied directly from the seconds column without conversion.

**ca_e02_c** — 2031-04-12. Route manifest confirms six stops in the full route. Both required record surfaces describe the complete six-stop route.

**ca_e02_d** — 2031-04-14. Segment timing: the final five stops took 80 minutes on a separate timing exercise. This report excludes the first stop and does not revise the full-route measurement in ca_e02_a.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_d"
      ],
      "value": "90"
    },
    {
      "field": "summary_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b",
        "ca_e02_d"
      ],
      "value": "90"
    },
    {
      "field": "canonical_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "summary_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "stop_count",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_c"
      ],
      "value": "6"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e02_c",
        "ca_e02_d"
      ],
      "value": "FULL_ROUTE"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-031

Assess independent observational support for the claim that exactly 30 percent of inspected north rooms had a loose latch. Count independent datasets for that population. A report that cites a later relay of an earlier inspection does not create another observational root.

### Required fields
- root_count: Independent observational roots for the north-room claim; integer decimal string.
- root_ids: Root document IDs for that claim; semicolon-separated, sorted lexicographically, no spaces.
- loose_latch_percent: Percent of inspected north rooms with a loose latch; integer decimal string without percent sign.
- population: Exact population enum: NORTH_ROOMS, SOUTH_ROOMS, or ALL_ROOMS.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e01_a** — 2031-02-01. Original north-room inspection: 12 of 40 north rooms had a loose latch. All 40 rooms were inspected that day.

**sd_e01_b** — 2031-02-02. Facilities circular reports 12 loose latches among 40 north rooms, entirely from sd_e01_a. No second inspection was performed.

**sd_e01_c** — 2031-02-03. Maintenance newsletter reports a 30 percent north-room loose-latch rate, citing sd_e01_b as its sole data source. It has no new observations.

**sd_e01_d** — 2031-02-03. Independent south-room inspection: 6 of 20 south rooms had a loose latch. No north room was included.

**sd_e01_e** — 2031-02-04. Archive abstract cites the later newsletter sd_e01_c for the north-room finding. The abstract contains no original inspection or additional sample.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "value": "sd_e01_a"
    },
    {
      "field": "loose_latch_percent",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "30"
    },
    {
      "field": "population",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "NORTH_ROOMS"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-032

Reconcile two counts of volunteers who attended the west and east sessions. Identify underlying enrollment-record roots, preserve the separate session counts, and determine the number of distinct volunteers across both sessions only if identifiable. A volunteer may attend both sessions.

### Required fields
- root_count: Independent enrollment-record roots underlying the two counts; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- west_count: Volunteers attending the west session; integer decimal string.
- east_count: Volunteers attending the east session; integer decimal string.
- distinct_volunteers: Distinct volunteers across both sessions; integer decimal string if identifiable, otherwise exact literal UNKNOWN.
- population_scope: Exact enum: SEPARATE_SESSION_COUNTS or DISJOINT_SESSION_COUNTS. Use DISJOINT_SESSION_COUNTS only if the evidence establishes that no attendee attended both sessions; otherwise use SEPARATE_SESSION_COUNTS.

### Supplied documents

**sd_e02_a** — 2031-02-06. Original enrollment extract: west session attendance 12; east session attendance 18. Attendee identifiers are withheld. The same volunteer may enroll in both. The extract contains no overlap count.

**sd_e02_b** — 2031-02-07. West-session bulletin reports 12 volunteers using only the west column in sd_e02_a. It did not collect a separate roster.

**sd_e02_c** — 2031-02-07. East-session bulletin reports 18 volunteers using only the east column in sd_e02_a. It did not collect a separate roster.

**sd_e02_d** — 2031-02-08. Enrollment custodian clarification: sd_e02_a remains the only record source. Whether any volunteers attended both sessions cannot be recovered from the supplied extract; no unique-person total is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "sd_e02_a"
    },
    {
      "field": "west_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b"
      ],
      "value": "12"
    },
    {
      "field": "east_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_c"
      ],
      "value": "18"
    },
    {
      "field": "distinct_volunteers",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "population_scope",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "SEPARATE_SESSION_COUNTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-033

Assess independent observational support for the claim that 22 percent of the inspected ochre panels had a surface scratch. Use explicit provenance statements in force at the relevant stage. If a claimed independent inspection is withdrawn, remove that root without discarding the surviving inspection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- scratch_percent: Scratch rate from the surviving original inspection sd_e03_a; integer decimal string without percent sign.
- sample_size: Panel count in inspection sd_e03_a; integer decimal string.
- inspection_date: Date of inspection sd_e03_a; exact YYYY-MM-DD.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e03_a** — 2031-02-10. Original ochre-panel inspection: 22 scratched panels out of 100 inspected on 2031-02-09.

**sd_e03_b** — 2031-02-11. Separate inspection report: this report declares its observations to be a new independent collection of 100 other ochre panels on 2031-02-10, with 22 scratched. It declares no use of sd_e03_a.

**sd_e03_c** — 2031-02-12. Compilation repeats the 22 percent rate from sd_e03_a and sd_e03_b; it performs no inspection of its own.

**sd_e03_d** — 2031-02-13. Signed correction by the author of sd_e03_b: the claim of a separate inspection was erroneous. No panels were inspected for sd_e03_b; its counts were copied from sd_e03_a. Its claimed 2031-02-10 inspection is withdrawn. The observations and date in sd_e03_a remain valid.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "sd_e03_a"
    },
    {
      "field": "scratch_percent",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "22"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "100"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "2031-02-09"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-034

Reconcile two counts of volunteers who attended the west and east sessions. Identify underlying enrollment-record roots, preserve the separate session counts, and determine the number of distinct volunteers across both sessions only if identifiable. A volunteer may attend both sessions.

### Required fields
- root_count: Independent enrollment-record roots underlying the two counts; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- west_count: Volunteers attending the west session; integer decimal string.
- east_count: Volunteers attending the east session; integer decimal string.
- distinct_volunteers: Distinct volunteers across both sessions; integer decimal string if identifiable, otherwise exact literal UNKNOWN.
- population_scope: Exact enum: SEPARATE_SESSION_COUNTS or DISJOINT_SESSION_COUNTS. Use DISJOINT_SESSION_COUNTS only if the evidence establishes that no attendee attended both sessions; otherwise use SEPARATE_SESSION_COUNTS.

### Supplied documents

**sd_e02_a** — 2031-02-06. Original enrollment extract: west session attendance 12; east session attendance 18. Attendee identifiers are withheld. The same volunteer may enroll in both. The extract contains no overlap count.

**sd_e02_b** — 2031-02-07. West-session bulletin reports 12 volunteers using only the west column in sd_e02_a. It did not collect a separate roster.

**sd_e02_c** — 2031-02-07. East-session bulletin reports 18 volunteers using only the east column in sd_e02_a. It did not collect a separate roster.

**sd_e02_d** — 2031-02-08. Enrollment custodian clarification: sd_e02_a remains the only record source. Whether any volunteers attended both sessions cannot be recovered from the supplied extract; no unique-person total is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_b",
        "sd_e02_c",
        "sd_e02_d"
      ],
      "value": "sd_e02_a"
    },
    {
      "field": "west_count",
      "source_ids": [
        "sd_e02_a"
      ],
      "value": "12"
    },
    {
      "field": "east_count",
      "source_ids": [
        "sd_e02_a"
      ],
      "value": "18"
    },
    {
      "field": "distinct_volunteers",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "population_scope",
      "source_ids": [
        "sd_e02_a",
        "sd_e02_d"
      ],
      "value": "SEPARATE_SESSION_COUNTS"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-035

Maintain the accepted completed-kit count for the 2031-03-23 inventory and preserve the earlier provisional publication. Determine authority by what a document says about its scope and status, not simply by its publication date.

### Required fields
- current_completed_count: Accepted completed-kit count for the inventory; integer decimal string.
- provisional_published_count: Count in provisional publication su_e04_a; integer decimal string.
- inventory_date: Date the kits were inventoried; exact YYYY-MM-DD.
- population: Exact literal SILVER_WORKROOM_KITS.
- release_status: Exact enum: PROVISIONAL or FINAL.

### Supplied documents

**su_e04_a** — 2031-03-24. Provisional Silver workroom release: 48 completed kits in the 2031-03-23 inventory.

**su_e04_b** — 2031-03-26. Final inventory release supersedes su_e04_a: 42 completed Silver workroom kits as of 2031-03-23; six items in the preliminary count were incomplete.

**su_e04_c** — 2031-03-27. Current inventory index designates su_e04_b as the final authoritative release for that inventory.

**su_e04_d** — 2031-03-30. Historical newsletter: "The provisional publication announced 48 completed kits." This passage reproduces su_e04_a as an account of the preliminary announcement. It explicitly acknowledges the final count of 42 in su_e04_b and contains no new inventory or revision.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_completed_count",
      "source_ids": [
        "su_e04_b",
        "su_e04_c",
        "su_e04_d"
      ],
      "value": "42"
    },
    {
      "field": "provisional_published_count",
      "source_ids": [
        "su_e04_a",
        "su_e04_d"
      ],
      "value": "48"
    },
    {
      "field": "inventory_date",
      "source_ids": [
        "su_e04_a",
        "su_e04_b"
      ],
      "value": "2031-03-23"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e04_b"
      ],
      "value": "SILVER_WORKROOM_KITS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e04_b",
        "su_e04_c"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-036

Maintain the accepted missing-label rate for the copper drawer inspection. Preserve the original published percentage and any count that remains valid if the rate is withdrawn. UNKNOWN means the supplied evidence does not establish a current accepted value.

### Required fields
- current_percent: Accepted percentage of inspected drawers missing labels; integer decimal string without percent sign if established, otherwise exact literal UNKNOWN.
- original_published_percent: Percentage printed in the original publication su_e03_a; integer decimal string without percent sign.
- missing_label_count: Accepted number of drawers missing labels; integer decimal string.
- accepted_denominator: Accepted number of inspected drawers used for the rate; integer decimal string if established, otherwise exact literal UNKNOWN.
- rate_status: Exact enum: PROVISIONAL or WITHDRAWN.
- inspection_date: Date of the drawer inspection; exact YYYY-MM-DD.

### Supplied documents

**su_e03_a** — 2031-03-18. Provisional copper drawer inspection report for 2031-03-17: 20 drawers lacked labels out of 80 inspected drawers, a rate of 25 percent.

**su_e03_b** — 2031-03-18. Label incident ledger independently lists the same 20 distinct drawers missing labels on 2031-03-17. It does not enumerate all inspected drawers.

**su_e03_c** — 2031-03-19. Display card quotes the provisional 25 percent rate from su_e03_a.

**su_e03_d** — 2031-03-20. Custodian correction: the total of 80 in su_e03_a was assembled from overlapping inspection batches. The true inspected denominator cannot be reconstructed from available records. The 20 distinct missing-label incidents in su_e03_b remain verified for 2031-03-17. The 25 percent rate is withdrawn; no replacement percentage or denominator is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_percent",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "original_published_percent",
      "source_ids": [
        "su_e03_a"
      ],
      "value": "25"
    },
    {
      "field": "missing_label_count",
      "source_ids": [
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "20"
    },
    {
      "field": "accepted_denominator",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "rate_status",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "WITHDRAWN"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "su_e03_a",
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "2031-03-17"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-037

Repair the duration fields on a canonical route record and its downstream summary. Both requested surfaces use minutes for the full route. Preserve the six-stop scope; a later segment-only measurement is not a replacement for the full route.

### Required fields
- canonical_duration: Full-route duration on canonical record in minutes; integer decimal string.
- summary_duration: Full-route duration on downstream summary in minutes; integer decimal string.
- canonical_unit: Exact literal MINUTES.
- summary_unit: Exact literal MINUTES.
- stop_count: Number of stops on the full route; integer decimal string.
- population: Exact literal FULL_ROUTE.

### Supplied documents

**ca_e02_a** — 2031-04-11. Original timed route log: total elapsed duration 5400 seconds, covering all six stops of the full route.

**ca_e02_b** — 2031-04-12. Record schema: the canonical full-route duration and downstream full-route duration are both stored in minutes, where 60 seconds equals one minute. The task-local numeric entries were copied directly from the seconds column without conversion.

**ca_e02_c** — 2031-04-12. Route manifest confirms six stops in the full route. Both required record surfaces describe the complete six-stop route.

**ca_e02_d** — 2031-04-14. Segment timing: the final five stops took 80 minutes on a separate timing exercise. This report excludes the first stop and does not revise the full-route measurement in ca_e02_a.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "summary_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "canonical_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "summary_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "stop_count",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_c"
      ],
      "value": "6"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_c"
      ],
      "value": "FULL_ROUTE"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-038

Maintain the cause and cause-status fields for incident I-17 on both the canonical record and downstream summary. When the evidence no longer identifies a unique cause, express uncertainty on both surfaces. Preserve the incident identifier and inspection sample size.

### Required fields
- canonical_cause: Canonical incident cause; exact enum: GLUE, HEAT, or UNKNOWN.
- summary_cause: Cause shown in downstream summary; exact enum: GLUE, HEAT, or UNKNOWN.
- canonical_cause_status: Canonical cause status; exact enum: CONFIRMED or UNRESOLVED.
- summary_cause_status: Downstream cause status; exact enum: CONFIRMED or UNRESOLVED.
- incident_id: Exact incident identifier literal I-17.
- inspection_sample_size: Objects in the incident inspection sample; integer decimal string.

### Supplied documents

**ca_e03_a** — 2031-04-18. Signed incident record I-17: a panel separation was attributed to GLUE and its cause status was CONFIRMED. The incident was found during an inspection of 24 panels.

**ca_e03_b** — 2031-04-19. Summary specification: the downstream cause and status reproduce the currently accepted cause and status for incident I-17, including unresolved status if the cause cannot be uniquely established.

**ca_e03_c** — 2031-04-19. Inspection manifest lists 24 inspected panels and incident identifier I-17. Those identifiers and the sample size are independently checked.

**ca_e03_d** — 2031-04-21. Signed correction to incident I-17: the label used to assign GLUE in ca_e03_a belonged to an ambiguously matched test. The available evidence cannot distinguish GLUE from HEAT. The earlier confirmed attribution is withdrawn, and the cause is UNRESOLVED with no uniquely identified cause. Incident I-17 and the sample of 24 panels are unchanged.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_cause",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "summary_cause",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "canonical_cause_status",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "summary_cause_status",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "incident_id",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "I-17"
    },
    {
      "field": "inspection_sample_size",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "24"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-039

Repair the duration fields on a canonical route record and its downstream summary. Both requested surfaces use minutes for the full route. Preserve the six-stop scope; a later segment-only measurement is not a replacement for the full route.

### Required fields
- canonical_duration: Full-route duration on canonical record in minutes; integer decimal string.
- summary_duration: Full-route duration on downstream summary in minutes; integer decimal string.
- canonical_unit: Exact literal MINUTES.
- summary_unit: Exact literal MINUTES.
- stop_count: Number of stops on the full route; integer decimal string.
- population: Exact literal FULL_ROUTE.

### Supplied documents

**ca_e02_a** — 2031-04-11. Original timed route log: total elapsed duration 5400 seconds, covering all six stops of the full route.

**ca_e02_b** — 2031-04-12. Record schema: the canonical full-route duration and downstream full-route duration are both stored in minutes, where 60 seconds equals one minute. The task-local numeric entries were copied directly from the seconds column without conversion.

**ca_e02_c** — 2031-04-12. Route manifest confirms six stops in the full route. Both required record surfaces describe the complete six-stop route.

**ca_e02_d** — 2031-04-14. Segment timing: the final five stops took 80 minutes on a separate timing exercise. This report excludes the first stop and does not revise the full-route measurement in ca_e02_a.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "summary_duration",
      "source_ids": [
        "ca_e02_a",
        "ca_e02_b"
      ],
      "value": "90"
    },
    {
      "field": "canonical_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "summary_unit",
      "source_ids": [
        "ca_e02_b"
      ],
      "value": "MINUTES"
    },
    {
      "field": "stop_count",
      "source_ids": [
        "ca_e02_c"
      ],
      "value": "6"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e02_c"
      ],
      "value": "FULL_ROUTE"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-040

Assess independent observational support for the claim that exactly 30 percent of inspected north rooms had a loose latch. Count independent datasets for that population. A report that cites a later relay of an earlier inspection does not create another observational root.

### Required fields
- root_count: Independent observational roots for the north-room claim; integer decimal string.
- root_ids: Root document IDs for that claim; semicolon-separated, sorted lexicographically, no spaces.
- loose_latch_percent: Percent of inspected north rooms with a loose latch; integer decimal string without percent sign.
- population: Exact population enum: NORTH_ROOMS, SOUTH_ROOMS, or ALL_ROOMS.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e01_a** — 2031-02-01. Original north-room inspection: 12 of 40 north rooms had a loose latch. All 40 rooms were inspected that day.

**sd_e01_b** — 2031-02-02. Facilities circular reports 12 loose latches among 40 north rooms, entirely from sd_e01_a. No second inspection was performed.

**sd_e01_c** — 2031-02-03. Maintenance newsletter reports a 30 percent north-room loose-latch rate, citing sd_e01_b as its sole data source. It has no new observations.

**sd_e01_d** — 2031-02-03. Independent south-room inspection: 6 of 20 south rooms had a loose latch. No north room was included.

**sd_e01_e** — 2031-02-04. Archive abstract cites the later newsletter sd_e01_c for the north-room finding. The abstract contains no original inspection or additional sample.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_e"
      ],
      "value": "sd_e01_a"
    },
    {
      "field": "loose_latch_percent",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "30"
    },
    {
      "field": "population",
      "source_ids": [
        "sd_e01_a"
      ],
      "value": "NORTH_ROOMS"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e01_a",
        "sd_e01_b",
        "sd_e01_c",
        "sd_e01_d",
        "sd_e01_e"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-041

Reconcile the canonical blue-tile record and its downstream inspection summary with the currently accepted inspection. Apply any revised defect count to both surfaces and recompute the summary rate while preserving unaffected fields.

### Required fields
- canonical_defect_count: Accepted defect count on the canonical record; integer decimal string.
- summary_defect_count: Accepted defect count in the downstream summary; integer decimal string.
- summary_defect_percent: Defect percentage in the downstream summary; decimal string with no trailing .0 and no percent sign.
- sample_size: Number of inspected tiles; integer decimal string.
- population: Exact literal BLUE_TILES.
- inspection_date: Tile inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e01_a** — 2031-04-05. Inspection release: 17 defective blue tiles among 40 tiles inspected on 2031-04-04.

**ca_e01_b** — 2031-04-06. Record contract: canonical count and downstream summary count refer to the same blue-tile inspection. Summary percentage equals the accepted defect count divided by 40, multiplied by 100.

**ca_e01_c** — 2031-04-06. Population manifest: exactly 40 blue tiles were inspected on 2031-04-04; no other tile color is in this sample.

**ca_e01_d** — 2031-04-08. Signed inspection correction supersedes the defect classification in ca_e01_a: five of the 17 marks were removable dust. The accepted defect count is 12. All 40 blue tiles remain in the sample; the inspection date remains 2031-04-04.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_defect_count",
      "source_ids": [
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_count",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "12"
    },
    {
      "field": "summary_defect_percent",
      "source_ids": [
        "ca_e01_b",
        "ca_e01_d"
      ],
      "value": "30"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "40"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "BLUE_TILES"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e01_c",
        "ca_e01_d"
      ],
      "value": "2031-04-04"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-042

Reconcile the current accepted cracked-jar count with the first published estimate for the same inventory. Preserve the original publication as history and keep the observation date separate from the publication date.

### Required fields
- current_cracked_count: Current accepted count of cracked jars; integer decimal string.
- original_published_count: Cracked-jar count first published in su_e01_a, without retrospectively rewriting it; integer decimal string.
- inspected_count: Jars in the inventory population; integer decimal string.
- observation_date: Inventory observation date; exact YYYY-MM-DD.
- population: Exact literal TEAL_ARCHIVE_JARS.
- release_status: Exact enum: PRELIMINARY or FINAL.

### Supplied documents

**su_e01_a** — 2031-03-05. Preliminary publication: of 120 teal archive jars inventoried on 2031-03-04, 18 were classified as cracked.

**su_e01_b** — 2031-03-06. Inventory scope sheet confirms that the 120 jars are all jars in the teal archive and that the observation date is 2031-03-04.

**su_e01_c** — 2031-03-06. Visitor summary repeats the preliminary count of 18 from su_e01_a; no new inventory was taken.

**su_e01_d** — 2031-03-08. Final correction of su_e01_a: three seam marks were incorrectly counted as cracks. The accepted cracked-jar count is 15 out of the same 120 jars observed on 2031-03-04. No jars were added or removed.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_cracked_count",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "15"
    },
    {
      "field": "original_published_count",
      "source_ids": [
        "su_e01_a"
      ],
      "value": "18"
    },
    {
      "field": "inspected_count",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "120"
    },
    {
      "field": "observation_date",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "2031-03-04"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e01_b"
      ],
      "value": "TEAL_ARCHIVE_JARS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-043

Maintain the cause and cause-status fields for incident I-17 on both the canonical record and downstream summary. When the evidence no longer identifies a unique cause, express uncertainty on both surfaces. Preserve the incident identifier and inspection sample size.

### Required fields
- canonical_cause: Canonical incident cause; exact enum: GLUE, HEAT, or UNKNOWN.
- summary_cause: Cause shown in downstream summary; exact enum: GLUE, HEAT, or UNKNOWN.
- canonical_cause_status: Canonical cause status; exact enum: CONFIRMED or UNRESOLVED.
- summary_cause_status: Downstream cause status; exact enum: CONFIRMED or UNRESOLVED.
- incident_id: Exact incident identifier literal I-17.
- inspection_sample_size: Objects in the incident inspection sample; integer decimal string.

### Supplied documents

**ca_e03_a** — 2031-04-18. Signed incident record I-17: a panel separation was attributed to GLUE and its cause status was CONFIRMED. The incident was found during an inspection of 24 panels.

**ca_e03_b** — 2031-04-19. Summary specification: the downstream cause and status reproduce the currently accepted cause and status for incident I-17, including unresolved status if the cause cannot be uniquely established.

**ca_e03_c** — 2031-04-19. Inspection manifest lists 24 inspected panels and incident identifier I-17. Those identifiers and the sample size are independently checked.

**ca_e03_d** — 2031-04-21. Signed correction to incident I-17: the label used to assign GLUE in ca_e03_a belonged to an ambiguously matched test. The available evidence cannot distinguish GLUE from HEAT. The earlier confirmed attribution is withdrawn, and the cause is UNRESOLVED with no uniquely identified cause. Incident I-17 and the sample of 24 panels are unchanged.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_cause",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "summary_cause",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "canonical_cause_status",
      "source_ids": [
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "summary_cause_status",
      "source_ids": [
        "ca_e03_b",
        "ca_e03_d"
      ],
      "value": "UNRESOLVED"
    },
    {
      "field": "incident_id",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "I-17"
    },
    {
      "field": "inspection_sample_size",
      "source_ids": [
        "ca_e03_c",
        "ca_e03_d"
      ],
      "value": "24"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-044

Reconcile the current accepted cracked-jar count with the first published estimate for the same inventory. Preserve the original publication as history and keep the observation date separate from the publication date.

### Required fields
- current_cracked_count: Current accepted count of cracked jars; integer decimal string.
- original_published_count: Cracked-jar count first published in su_e01_a, without retrospectively rewriting it; integer decimal string.
- inspected_count: Jars in the inventory population; integer decimal string.
- observation_date: Inventory observation date; exact YYYY-MM-DD.
- population: Exact literal TEAL_ARCHIVE_JARS.
- release_status: Exact enum: PRELIMINARY or FINAL.

### Supplied documents

**su_e01_a** — 2031-03-05. Preliminary publication: of 120 teal archive jars inventoried on 2031-03-04, 18 were classified as cracked.

**su_e01_b** — 2031-03-06. Inventory scope sheet confirms that the 120 jars are all jars in the teal archive and that the observation date is 2031-03-04.

**su_e01_c** — 2031-03-06. Visitor summary repeats the preliminary count of 18 from su_e01_a; no new inventory was taken.

**su_e01_d** — 2031-03-08. Final correction of su_e01_a: three seam marks were incorrectly counted as cracks. The accepted cracked-jar count is 15 out of the same 120 jars observed on 2031-03-04. No jars were added or removed.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_cracked_count",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "15"
    },
    {
      "field": "original_published_count",
      "source_ids": [
        "su_e01_a"
      ],
      "value": "18"
    },
    {
      "field": "inspected_count",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "120"
    },
    {
      "field": "observation_date",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "2031-03-04"
    },
    {
      "field": "population",
      "source_ids": [
        "su_e01_b",
        "su_e01_d"
      ],
      "value": "TEAL_ARCHIVE_JARS"
    },
    {
      "field": "release_status",
      "source_ids": [
        "su_e01_d"
      ],
      "value": "FINAL"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-045

Assess independent observational support for the claim that 22 percent of the inspected ochre panels had a surface scratch. Use explicit provenance statements in force at the relevant stage. If a claimed independent inspection is withdrawn, remove that root without discarding the surviving inspection.

### Required fields
- root_count: Independent observational roots supporting the claim; integer decimal string.
- root_ids: Root document IDs; semicolon-separated, sorted lexicographically, no spaces.
- scratch_percent: Scratch rate from the surviving original inspection sd_e03_a; integer decimal string without percent sign.
- sample_size: Panel count in inspection sd_e03_a; integer decimal string.
- inspection_date: Date of inspection sd_e03_a; exact YYYY-MM-DD.
- support: Exact enum: SINGLE_ROOT, MULTIPLE_ROOTS, or UNSUPPORTED.

### Supplied documents

**sd_e03_a** — 2031-02-10. Original ochre-panel inspection: 22 scratched panels out of 100 inspected on 2031-02-09.

**sd_e03_b** — 2031-02-11. Separate inspection report: this report declares its observations to be a new independent collection of 100 other ochre panels on 2031-02-10, with 22 scratched. It declares no use of sd_e03_a.

**sd_e03_c** — 2031-02-12. Compilation repeats the 22 percent rate from sd_e03_a and sd_e03_b; it performs no inspection of its own.

**sd_e03_d** — 2031-02-13. Signed correction by the author of sd_e03_b: the claim of a separate inspection was erroneous. No panels were inspected for sd_e03_b; its counts were copied from sd_e03_a. Its claimed 2031-02-10 inspection is withdrawn. The observations and date in sd_e03_a remain valid.

### Final answer

```json
{
  "answers": [
    {
      "field": "root_count",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "1"
    },
    {
      "field": "root_ids",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "sd_e03_a"
    },
    {
      "field": "scratch_percent",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "22"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "100"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "sd_e03_a"
      ],
      "value": "2031-02-09"
    },
    {
      "field": "support",
      "source_ids": [
        "sd_e03_a",
        "sd_e03_d"
      ],
      "value": "SINGLE_ROOT"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-046

Update the registration snapshot for the Cedar craft course. Report all registrations separately from registrations eligible for the advanced session. Preserve the earlier all-registration count; never substitute an eligible subset for the full population.

### Required fields
- current_all_registrations: All registrations at the latest supplied snapshot; integer decimal string.
- current_eligible_registrations: Registrations eligible for the advanced session at that same latest snapshot; integer decimal string.
- earlier_all_registrations: All registrations at the 2031-03-10 snapshot; integer decimal string.
- current_snapshot_date: Latest supplied registration snapshot date, not publication date; exact YYYY-MM-DD.
- all_count_population: Population label for current_all_registrations; exact literal ALL_REGISTRATIONS.
- eligibility_basis: Exact literal COMPLETED_INTRODUCTORY_SESSION.

### Supplied documents

**su_e02_a** — 2031-03-11. Cedar course register, snapshot 2031-03-10: 80 registrations in all; 52 of those registrations are eligible for the advanced session.

**su_e02_b** — 2031-03-11. Course definitions: eligibility for the advanced session requires completion of the introductory session. The eligible count is a subset of all registrations.

**su_e02_c** — 2031-03-12. Course bulletin quotes 80 total registrations from su_e02_a. It contains no later snapshot.

**su_e02_d** — 2031-03-15. New register, snapshot 2031-03-14: 94 registrations in all, of which 70 completed the introductory session and are eligible for the advanced session. The headline "70 eligible registrations" refers only to the subset. The previous snapshot remains historical.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_all_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "94"
    },
    {
      "field": "current_eligible_registrations",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "70"
    },
    {
      "field": "earlier_all_registrations",
      "source_ids": [
        "su_e02_a"
      ],
      "value": "80"
    },
    {
      "field": "current_snapshot_date",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "2031-03-14"
    },
    {
      "field": "all_count_population",
      "source_ids": [
        "su_e02_d"
      ],
      "value": "ALL_REGISTRATIONS"
    },
    {
      "field": "eligibility_basis",
      "source_ids": [
        "su_e02_b",
        "su_e02_d"
      ],
      "value": "COMPLETED_INTRODUCTORY_SESSION"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-047

Maintain the accepted missing-label rate for the copper drawer inspection. Preserve the original published percentage and any count that remains valid if the rate is withdrawn. UNKNOWN means the supplied evidence does not establish a current accepted value.

### Required fields
- current_percent: Accepted percentage of inspected drawers missing labels; integer decimal string without percent sign if established, otherwise exact literal UNKNOWN.
- original_published_percent: Percentage printed in the original publication su_e03_a; integer decimal string without percent sign.
- missing_label_count: Accepted number of drawers missing labels; integer decimal string.
- accepted_denominator: Accepted number of inspected drawers used for the rate; integer decimal string if established, otherwise exact literal UNKNOWN.
- rate_status: Exact enum: PROVISIONAL or WITHDRAWN.
- inspection_date: Date of the drawer inspection; exact YYYY-MM-DD.

### Supplied documents

**su_e03_a** — 2031-03-18. Provisional copper drawer inspection report for 2031-03-17: 20 drawers lacked labels out of 80 inspected drawers, a rate of 25 percent.

**su_e03_b** — 2031-03-18. Label incident ledger independently lists the same 20 distinct drawers missing labels on 2031-03-17. It does not enumerate all inspected drawers.

**su_e03_c** — 2031-03-19. Display card quotes the provisional 25 percent rate from su_e03_a.

**su_e03_d** — 2031-03-20. Custodian correction: the total of 80 in su_e03_a was assembled from overlapping inspection batches. The true inspected denominator cannot be reconstructed from available records. The 20 distinct missing-label incidents in su_e03_b remain verified for 2031-03-17. The 25 percent rate is withdrawn; no replacement percentage or denominator is certified.

### Final answer

```json
{
  "answers": [
    {
      "field": "current_percent",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "original_published_percent",
      "source_ids": [
        "su_e03_a"
      ],
      "value": "25"
    },
    {
      "field": "missing_label_count",
      "source_ids": [
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "20"
    },
    {
      "field": "accepted_denominator",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "UNKNOWN"
    },
    {
      "field": "rate_status",
      "source_ids": [
        "su_e03_d"
      ],
      "value": "WITHDRAWN"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "su_e03_a",
        "su_e03_b",
        "su_e03_d"
      ],
      "value": "2031-03-17"
    }
  ]
}
```

Human grade: PENDING

## OUTPUT-048

Reconcile the canonical Garden vault record and its downstream summary with the accepted complete inspection. Preserve already-correct fields when later material describes a partial draft. Both surfaces must represent the full inspection.

### Required fields
- canonical_marked_count: Marked-object count on the canonical full-inspection record; integer decimal string.
- summary_marked_count: Marked-object count on the downstream full-inspection summary; integer decimal string.
- summary_marked_percent: Full-inspection marked-object percentage; integer decimal string without percent sign.
- sample_size: Full-inspection sample size; integer decimal string.
- population: Exact literal GARDEN_VAULT_OBJECTS.
- inspection_date: Full-inspection date; exact YYYY-MM-DD.

### Supplied documents

**ca_e04_a** — 2031-04-24. Signed complete Garden vault inspection: 24 marked objects out of 60 inspected on 2031-04-23. This is the accepted full-inspection result.

**ca_e04_b** — 2031-04-25. Record contract: canonical and downstream marked counts cover all 60 objects in the accepted Garden vault inspection. The summary percentage is marked count divided by 60 times 100.

**ca_e04_c** — 2031-04-25. Archive note: an earlier unfinished draft omitted the final tray. It cannot replace the signed complete inspection in ca_e04_a.

**ca_e04_d** — 2031-04-28. Catalog description of the recovered unfinished draft: it lists 23 marked objects out of 55 in the trays processed before the final tray. This is the incomplete draft described by ca_e04_c; it is not a correction to the accepted full-inspection result of 24 out of 60.

### Final answer

```json
{
  "answers": [
    {
      "field": "canonical_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_count",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "24"
    },
    {
      "field": "summary_marked_percent",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "40"
    },
    {
      "field": "sample_size",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b",
        "ca_e04_d"
      ],
      "value": "60"
    },
    {
      "field": "population",
      "source_ids": [
        "ca_e04_a",
        "ca_e04_b"
      ],
      "value": "GARDEN_VAULT_OBJECTS"
    },
    {
      "field": "inspection_date",
      "source_ids": [
        "ca_e04_a"
      ],
      "value": "2031-04-23"
    }
  ]
}
```

Human grade: PENDING
