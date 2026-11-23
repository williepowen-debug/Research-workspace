# WQ-735 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "735",
  "queue_terms_sha256": "5ded79d8e06c278b907d93a9e9803ca29c10cdfbea8500ac4a0edb8b3eebf5ec",
  "choices": [
    {
      "id": "A",
      "label": "Honest name first, fleet-wide, as each desk next works",
      "meaning": "Scripts that tell sites they are a Chrome browser switch to one honest name on the 28 sites that answered an honest request in PROME's 11/20 sample. A site that refuses the honest name is dropped for another source. The 16 unclear sites stay until their owner tests them. For the price tool, PROME tests an honest client on its real requests and switches only if prices still come through; otherwise it comes back to you first.",
      "consequence": "No desk is launched for this alone. Some sources will be lost where sites refuse an honest name, and those readings get a weaker source with a caveat. Live prices change nothing unless the test passes."
    },
    {
      "id": "B",
      "label": "A browser name sent first is acceptable",
      "meaning": "The rule covers only changing identity after a refusal, as LABOR's script did. Scripts and the price tool stay as they are.",
      "consequence": "Nothing changes. Sites that would refuse an honest client keep being read as if by a browser."
    },
    {
      "id": "C",
      "label": "Price tool only",
      "meaning": "PROME tests and, if it passes, switches the price tool to an honest client. Desk scripts stay as they are.",
      "consequence": "The tool every desk depends on is put right; 63 desk scripts keep their browser names."
    }
  ],
  "recommended_choice_id": "A",
  "context": "Your blocked-sites rule says never change an identity string to get past a block. On 11/20 you ruled for one script (WQ-723): one honest name, sent first, stop on a refusal. Whether a browser name sent from the very first request is inside the rule was left open. PROME recommended A on 11/20 and never registered it. On 11/23 MIDAS found that the fleet price tool does the same through its library.",
  "conditions": [
    "Sample of 11/20: 54 sites, one honest request each: 28 answered, 6 refused, 16 unclear, 4 not tried. One request per site is thin evidence.",
    "Yahoo answered one honest request from PROME on 11/23 at 12:19 ET. One request does not show the price tool's full set of calls would work.",
    "MIDAS disclosed that its gold-fund captures from about 10/20 to 11/18 used a browser-imitating client; those records stay as history and are not re-run.",
    "No money is involved. Root CLAUDE.md's text does not change under A or B; A is how the existing words are read.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
