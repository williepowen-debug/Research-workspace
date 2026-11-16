# WQ-698 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "698",
  "queue_terms_sha256": "721452510e241f8afb89cb8cf2d04a04175453e2f2c2160f29b1fbc9c1895f78",
  "choices": [
    {
      "id": "A",
      "label": "HAWK keeps an unscored log of physical crude losses",
      "meaning": "From your approval date, HAWK records each physical loss of crude supply or crude-export capacity, in the Gulf and in Russia, with its source and what is confirmed and what is only claimed. It attaches no probability and makes no forecast until it has a basis for one. HAWK writes the exact terms in its own files and PROME verifies them.",
      "consequence": "A loss is on the record the session it is seen, and the fleet can see several small ones adding up. Nothing is scored, so nothing here moves a trigger or a position. Cost: a few minutes of HAWK's session when it runs."
    },
    {
      "id": "B",
      "label": "Leave the gap until HAWK has a basis for a probability",
      "meaning": "No log and no forecast. A physical loss is picked up only if WALTER's news cards carry it and a desk happens to act on it.",
      "consequence": "Nothing to build. A loss of Russian crude-export capacity would have no registered reader; a stated Gulf loss is still covered by FALCON's existing test."
    },
    {
      "id": "C",
      "label": "Have HAWK register a new probability forecast now",
      "meaning": "HAWK registers a successor to its October forecast with a stated probability.",
      "consequence": "A scored forecast exists, but HAWK says it has no basis for the number, so the probability would be a guess that later counts in the fleet's calibration record."
    }
  ],
  "recommended_choice_id": "A",
  "context": "HAWK, the desk that reads war and sanctions damage to energy supply, had a forecast on undisclosed damage that stopped accepting new events on October 31. Since then nothing records a physical loss of crude supply if one happens. FALCON's test covers only a stated loss of Gulf crude; a loss of Russian crude-export capacity has no test. HAWK raised this on November 6 and recommends an unscored log, not a new probability. Ukraine struck the Omsk and Volgograd refineries on November 11 and 13.",
  "conditions": [
    "HAWK's own recommendation is A. PROME has not read HAWK's October 25 draft of a probabilistic successor, which HAWK itself advises against.",
    "Refinery strikes are already recorded by OSPREY and stay there; this covers the crude-supply and crude-export leg.",
    "A log is not a score: nothing logged moves a threshold, a gate or a position.",
    "Whether Russia is in scope is the part HAWK said needs your word; A as written includes it.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
