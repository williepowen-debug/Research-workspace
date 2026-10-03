# L594 / WQ-372 Helm fold — acceptance before code

2026-10-03. Will authorized proceeding with the catch-up sequence. Original authority and supersession: `inbox/2026-10-02_from-PROME_WQ-372-fold-fleet-ops-into-the-helm.md`. PROME remains live; implementation will be an isolated, reviewable patch under DAEDALUS, not an edit to active PROME files. PROME owns integration timing, publication and CLOSEOUT rewiring. No hosted-pass claim from local output.

## Proposed implementation boundary (independent plan read before edits)

1. Extract Fleet-Ops' existing active-roster fleet-row construction into one callable in `fleet_dashboard.py`; its own build calls it, Helm imports it. Preserve classification, parking, ordering, maturity and snapshot schema. Do not call dashboard build/main from Helm, because they perform unrelated work and state writes.
2. Helm consumes Fleet-Ops `parse_gates(today)` for the transferred gate panel, keeping literal source semantics visible. Current snapshot: donor live18/resolved2, Helm live18/fired0. Preserve existing Helm position/brief parsing and fired strip; no new state token or altered gate contract.
3. Add a compact fleet table and LIVE/FIRED chips with named fired gates under Your desk. Escape source text, no new clipping of critical fields. Keep manual/three tabs/supporting docket file. Remove the Helm's prominent link to the retired Fleet-Ops page; Fleet-Ops header links to Helm with the ruled retirement notice. Keep dashboard builds/state files intact.
4. Existing donor freshness is **own-surface committed activity**, excluding inbox traffic, NOT authenticated author activity. Do not label it a proved self-authored session. Spec says last self-commit but donor currently provides only age/word/class. Resolve display to source-faithful age/class or supply an exact compatible commit reference; record this mismatch for owner disposition instead of inventing authorship. Existing UNKNOWN-versus-no-history collapse is a declared donor limit, not permission to present an all-clear.

## Required executable evidence

| ID | Acceptance |
|---|---|
| H1 | Same frozen inputs produce identical fleet row values/order/classification in donor before extraction and donor/Helm after; live/fired counts and fired names agree with donor. No new parser family |
| H2 | No-history desk visible with explicit unavailable/no-history state; never fresh zero. Parked desk retains parking, not treated as active alarm; empty table prints visible degraded message and contributes to REVIEW |
| H3 | Fired gate named and escaped with its original action/state semantics; source read failure shows unavailable, not zero/all-clear. No empty/malformed parser result silently treated as successful absence |
| H4 | Helm `--no-feed` leaves brief_snapshot/brief_changes and dashboard state/build receipts byte-identical; dashboard snapshot schema and build/closeout code contracts unchanged |
| H5 | Before/after Helm page <250,000 B on the same frozen representative snapshot; measure.py evidence; existing docket support links still resolve locally, manual content remains unchanged, no repeated split |
| H6 | Fleet-Ops only adds the retirement header and helper extraction; old build function fleet collection equivalence demonstrated; no CLOSEOUT edit/publication performed |
| H7 | Existing Helm split and desk-attention tests pass; new capable/quiet/boundary tests pass; independent result read covers final patch after remedies |
| H8 | PROME integration/Standard gate and hosted link/publication verification are owner acceptance legs. Local isolated comparison must disclose existing failures; never claim a green owner gate from unchanged code alone |

Literal L594 requirements not demonstrable while PROME is active remain explicit dependent legs, not waived. A source-hash precondition must accompany the patch; owner rebase/review required if target source changed. No broad unrelated repair campaign. Source-equivalent cosmetic labels and extraction need review because the transferred evidence affects operator attention; UPGRADE_PROTOCOL4/4a/4b applies.
