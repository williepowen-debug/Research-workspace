# HAWK workbook reference

Moved verbatim from CLAUDE.md on October 25 under Will's request to update the audited defects. Read on demand before a workbook write; SCHEMA.tsv and AGENTS/VOCABULARIES.tsv remain authoritative for fields and vocabulary. This reference is not a new boot whole-read.

## WORKBOOK LOGGING RULES

Your workbook is the permanent structured record. STATUS.md gets rewritten; workbook entries persist forever. **Post-split, all workbook entries are synthesis or dormant-book content only** — theater facts accrue in OSPREY's/FALCON's own workbooks.

| File | What goes in | Test |
|------|-------------|------|
| `KB.tsv` | New synthesis/dormant-book data point with a source. | "Is this a new piece of evidence outside OSPREY's/FALCON's theater scope?" |
| `VX.tsv` | When a dormant vector changes state, or the re-sweep cadence (boot 6b) surfaces a change. | "Did a dormant risk indicator move?" |
| `FLOW.tsv` | When the shared oil-decoupling thesis or another cross-war transmission channel is confirmed, changes speed, or a new pathway is identified. | "Did we learn something about HOW cross-war stress reaches markets?" |
| `thesis/PREDICTIONS.tsv` | Falsifiable synthesis/dormant-book predictions (HAW-18+), confidence, timeframe, resolution tracking. | "What do I think happens next in the cross-war or dormant-book space?" |

**When NOT to log:** Theater event tracking (that's OSPREY's/FALCON's workbook), routine status updates, unchanged metrics.

### KB.tsv — Knowledge Base Schema (13 columns)

The KB is HAWK's primary factual memory. Each row is one atomic claim with structured metadata.

**Schema:**
```
ID	Date	Group	Entity	Fact	Source	Conf	Epistemic	Status	Stale_By	DerivedFrom	Vectors	Notes
```

| Field | Format | Purpose |
|-------|--------|---------|
| **ID** | KB-HAWK-NNN | Sequential — rows ≤223 are the pre-split, both-theater historical record (frozen, incl. 2 known duplicate IDs 131/132); **rows 224+ are synthesis/dormant-book only** |
| **Date** | YYYY-MM-DD | When the claim was logged |
| **Group** | UPPER_SNAKE | From `AGENTS/VOCABULARIES.tsv` NETWORK_GROUPS (WAR, HORMUZ, TANKERS, GEOPOLITICS, etc.) |
| **Entity** | Free text (short) | From `AGENTS/VOCABULARIES.tsv` CANONICAL_ENTITIES where available |
| **Fact** | Free text | One atomic claim per row. Precise, sourced, quantified. |
| **Source** | Free text | Use SOURCE_TAGS from VOCABULARIES.tsv + date |
| **Conf** | Admiralty digraph | A1–F6 (letter = source reliability, number = info credibility). Default F6. |
| **Epistemic** | Enum | EMPIRICAL / ESTIMATE / ASSUMPTION |
| **Status** | Enum | ACTIVE / CONFIRMED / STALE / SUPERSEDED / CORRECTED |
| **Stale_By** | YYYY-MM-DD or null | Expected review/expiration date |
| **DerivedFrom** | CSV of KB IDs or null | Parent facts this was built on |
| **Vectors** | CSV of refs | VX-HAWK-xx, FLOW-HAWK-xx, →AGENT_NAME |
| **Notes** | Free text | Caveats, implications, context |

**Admiralty Code quick ref:** A=completely reliable, B=usually reliable, C=fairly reliable, D=not usually reliable, E=unreliable, F=cannot judge. 1=confirmed, 2=probably true, 3=possibly true, 4=doubtful, 5=improbable, 6=cannot judge.

**Cold-boot orientation (3 passes):**
1. **Currency pass:** Filter where Stale_By < today OR Status = STALE/SUPERSEDED. Set aside expired claims.
2. **Reliability pass:** Sort remaining by Conf. Focus on A1–C3 first. Flag F6 for verification.
3. **Synthesis pass:** Use Vectors and DerivedFrom to reconstruct thesis chains. Identify convergences and contradictions.

---

