# WQ-202 — Decision Deck v1 with tap-to-rule — RULED
**Registered:** 2026-09-10 ~11:0x ET (PROME `prome-6d`, after Will's talk-through 10:5x–10:59 ET). **Ruled:** 2026-09-10 11:01 ET, Will verbatim *"Approve WQ-202 with your recs"*.

## Will's talk-through answers (10:59 ET, verbatim points)
1. Both rails (queue + decisions in general) — *"in different tabs or sections"*.
2. Plain-English block per row — *"sure"*.
3. *"Maybe the helm page or its own artifact really. It would be nice if I could quickly push approve or not on the artifact."*
4. *"everything that is still owed by me. Otherwise I will never see them. As we process through them they should be removed or archived to a process folder or something."*

## Approved spec (PROME rec, approved as written)
- **Generator:** `PROME/tools/decision_deck.py` → `PROME/artifacts/decision_deck.html`; run at every PROME closeout (and on demand). Sources: `PROME/WILL_QUEUE.md` (OPEN + RECENTLY DONE) + `PROME/archive/WILL_QUEUE_ROWS_*.md` (every DONE row since the queue began) + `PROME/ACTIVE_DECISIONS.md` live index + `PROME/DOCKET.tsv` rows whose owner cell names Will + `PROME/registry/WQ_EXPLAINERS.tsv` (sidecar, keyed by row number). A projection; never a second truth.
- **Published** as its OWN Artifact (private to Will's account), linked from the Helm. Tabs: **Owed · Decided · In-flight · Docket · Key**.
- **Card:** number · name · type · needed-by + days-left · since · plain-English block (what it is · why it is Will's · what yes / no / nothing does) · PROME rec + reason · links to the record.
- **Flow:** a ruled row leaves Owed and appears under Decided with the verbatim word; nothing is deleted (the archive files are the "processed folder").
- **Explainers:** written into `WQ_EXPLAINERS.tsv` at registration; open rows backfilled by PROME; a card without one says "explainer owed", never invents.
- **Tap-to-rule (record-only):** Approve / Decline / Later + optional note → the page's `db` store, one document per tap (`rulings/<WQ-n>-<ts>`: verdict, note, iso ts, page build id). PROME reads the store at boot (Artifact `read_db`), writes the ruling into the queue verbatim as *"tap via Decision Deck <stamp>: <verdict> <note>"*, then marks the doc `consumed`. A boot advisory (in `prome_gate.py`, script not prose) flags unconsumed taps. **Nothing executes off a tap**; trade/spend consequents still follow their own rails.
- ⚠️ **Privacy is the authentication:** no viewer-identity capability exists for this account, so a tap counts as Will's word ONLY while the artifact stays private. The deck is never shared; the page states this in its Key tab.

## Residue (declared)
- The Helm link and the boot advisory land with the build; if either slips, it is recorded here at the closeout.
