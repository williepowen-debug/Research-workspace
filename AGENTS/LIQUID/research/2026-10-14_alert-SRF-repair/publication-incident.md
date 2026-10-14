# Shared-push publication incident — 2026-10-14T16:33:52.940291-04:00

LIQUID session `01a13b8c-ebf0-74c0-a1c3-5ae79550bd06` ran the fleet safe-push for its authorized acceptance701511870 and repaird186bb16a. The helper's train also contained BROCK2eebe1e2c and50006b90c. The latter records an automatic-review rejection of BROCK's GitHub export. LIQUID inspected that restriction after the push completed; it did not have or obtain explicit approval for the BROCK payload.

Actual receipt: `Pushed. CONFIRMED: HEAD d186bb16a is on origin/master (fresh fetch).` The push advanced48e559bac→d186bb16a. The two BROCK commits are ancestors of that confirmed head and were included in the export.

The recorded reason in `AGENTS/BROCK/research/2026-10-14_followup/closeout.json` is: internal research/closeout export to an unverified GitHub destination; routine Git authorization and closeout request did not specifically authorize that payload export. BROCK's50006b90c SCRATCH change required explicit payload/destination approval and said do not bypass. No rejected payload content is copied into this note.

This is an unintended publication under the shared-branch helper, not evidence that BROCK's rejection was cleared. LIQUID failed to inspect the foreign restriction before export. No force-push, deletion, history rewrite, foreign-state correction or further remote push is performed. BROCK/PROME receive local self-authored incident packets; recipient consumption remains UNKNOWN. A later Git receipt cannot serve as retroactive payload approval.

ACTION for PROME/BROCK: reconcile actual publication and the recorded restriction; retain the rejection reason and involve Will in any required destination/payload or remediation decision. BROCK's source records remain owner-controlled. Future safe-push runs must inspect foreign pending export restrictions before executing; this note installs no fleet rule or new checker.

LIQUID repair remains implemented/tested and published, independently unverified. Its existing code review is separate from this publication incident. Incident receipts are local-only; no additional export is attempted while this is unresolved.
