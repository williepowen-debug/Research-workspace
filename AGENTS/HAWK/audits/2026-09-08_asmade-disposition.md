# As-made audit disposition — 2026-09-08

DAEDALUS's title says five candidates; its embedded output contains **four**, across 21 predictions. Owner read the cited historical blobs and original ledger rows. No probability or scoring field was edited under this session's explicit prohibition.

| Candidate | Artifact verification | Disposition |
|---|---|---|
| HAW-06 70% vs 35% | `132abbd04` STATUS calls D-scenario 35% while referencing HAW-06's historical failure. Same commit's workbook prediction row carries 70%. | False match: scenario probability is not prediction confidence. Retain 70%. |
| HAW-09 35% vs 12% | `132abbd04` STATUS says a HAW-09 event would promote B from 12% to 20%+. Same commit's ledger records HAW-09 at 35%. | False match: consequence scenario is not event probability. Retain 35%. |
| HAW-11 20% vs 90% | `f21e2db68` STATUS's 90% describes Kharg's share of Iran exports. June 8 ledger at `132abbd04` carries HAW-11 20%. | False match: export share is not probability. Retain 20%. |
| HAW-18 55% vs 60% | `a552c04be` STATUS AND prediction ledger both register 60%. Current ledger explicitly documents a same-session July 25 correction to 55%, before resolution evidence, on a base-rate error. | Real two-vintage record. Scoring treatment remains a decision for PROME/Will; no re-mark or score edit authorized here. |

For the failed HAW-18, binary Brier contribution would be 0.3600 at first-published 60% versus 0.3025 at corrected 55%, difference +0.0575. This is a conditional calculation, not an adopted re-score or a fleet-average correction. The original published and corrected vintages are both retained. Fourteen NOT-FOUND rows were not reclassified as verified; a search miss is not a confidence finding. PROME review September 11, ahead of the September 14 sitting.
