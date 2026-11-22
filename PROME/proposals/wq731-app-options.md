# WQ-731 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "731",
  "queue_terms_sha256": "318ff3402b1385d4ec974c5f27844bf68393c7b8818ed08210b91451ab93a2ec",
  "choices": [
    {
      "id": "A",
      "label": "Log-only now; part (b) comes back later",
      "meaning": "AEOLUS's volcano-alert trigger (S-5) becomes a logged state that never counts as a fire. AEOLUS may bring back a firing version once it names a dated, measurable consequence (for example an airport closure) and its base rate.",
      "consequence": "An alert with no real-world effect stops counting toward promoting the seismic folder to a scored channel. Nothing else changes."
    },
    {
      "id": "B",
      "label": "Leave it as it is",
      "meaning": "The trigger keeps reading: USGS alert to WARNING/RED, or WATCH/ORANGE at a Very High Threat volcano.",
      "consequence": "A summit-confined eruption can count as a fire, as Kilauea's did from 9/07 to 10/17; three in about six months would promote the folder under AEOLUS's own rule."
    },
    {
      "id": "C",
      "label": "Drop the re-spec",
      "meaning": "AEOLUS removes the proposal from its owed list. The trigger stays as written.",
      "consequence": "Same trigger as B, and the open item is closed."
    }
  ],
  "recommended_choice_id": "A",
  "context": "AEOLUS, the climate and physical-risk desk, keeps a small seismic and volcano watch. On 10/29 it proposed splitting its volcano trigger into a log-only state and a firing version that needs a real consequence. The item sat as awaiting Will with no queue row until AEOLUS flagged it on 11/22.",
  "conditions": [
    "AEOLUS's draft of the firing version names no specific consequence measure yet and its base rate is not established.",
    "The trigger's wording also fuses two USGS scales; AEOLUS's draft covers that and it is not decided here.",
    "No money or position is involved; the seismic watch has no live read today.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
