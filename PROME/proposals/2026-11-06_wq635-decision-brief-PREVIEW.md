# WQ-635 decision brief — PREVIEW, not installed

**Status:** preview under Will's 2026-11-06 11:08 ET instruction. No pointer is in the queue row, so the app does not read this yet. It approves nothing and changes no answer-confirmation rule.

```decisions-brief
{
  "schema_version": "decisions-brief/1",
  "wq_id": 635,
  "queue_row_sha256": "a8fffbdf85703b47a7915bfeca9ec641dc2a994166f08615c312f4669ad9fda5",
  "prepared_at": "2026-11-06 11:10 ET",
  "stale_after": "2026-11-10",
  "question": "How big a fall in Palo Alto's stock should count as a 'collapse' in CYPHER's cyber-attack test?",
  "what_changes": "CYPHER, the cyber desk, is testing whether October's attack wave badly damages a security company caught up in it. Palo Alto is the only company on its list. The test's collapse step has no number, so without one it can't be graded when its window ends at the 11/18 close. Your answer sets that number. It is a research measure, graded by HENRY, and PROME sees no position tied to it.",
  "recommendation": {
    "status": "RECOMMENDED",
    "text": "The stricter version (A): down 15% and 10 points behind the HACK cyber fund, on two straight closes. CYPHER and PROME agree. 'Collapse' should mean a large, lasting fall. Tested on history, it catches CrowdStrike 2024 and false-alarmed in 14 of 906 quiet periods (1.55%)."
  },
  "conditions": [
    "A deliberately misses a smaller slide like Progress in 2023 (down 10.7%, then recovered). B catches that one, but only on the last day, and false-alarmed 5.19% of the time.",
    "The test is thin: the periods overlap, HACK itself holds Palo Alto, and SolarWinds couldn't be tested because it delisted.",
    "No ruling by the 11/18 close means this step grades UNGRADEABLE. PROME asks for your answer by Tuesday 11/10.",
    "Not breached: down about 4.5% from its 10/20 close at about 10:05 ET 11/6. Measured from its 10/27 peak it is down 19.1%, but that is not this test, and Thursday's fall came inside a market-wide drop."
  ],
  "supporting": [
    {
      "label": "CYPHER's proposal and back-test",
      "path": "PROME/inbox/processed/2026-11-06_from-CYPHER_L973-row9-magnitude-proposal.md"
    },
    {
      "label": "CYPHER's working record",
      "path": "AGENTS/CYPHER/research/2026-11-06_L973/RECORD.md"
    }
  ]
}
```

```decisions-options
{
  "schema_version": "decisions-options/1",
  "wq_id": 635,
  "queue_row_sha256": "a8fffbdf85703b47a7915bfeca9ec641dc2a994166f08615c312f4669ad9fda5",
  "choices": [
    {
      "id": "A",
      "label": "Down 15%, stricter",
      "meaning": "Palo Alto at or below $289.24 and 10 points behind HACK since 10/20, on 2 straight closes through 11/18.",
      "consequence": "CYPHER writes this into the row and HENRY grades it after the 11/18 close."
    },
    {
      "id": "B",
      "label": "Down 10%, looser",
      "meaning": "The same test with a 10% fall.",
      "consequence": "It fires more easily and false-alarms about three times as often."
    },
    {
      "id": "C",
      "label": "Leave it without a number",
      "meaning": "No size is set.",
      "consequence": "The collapse step grades UNGRADEABLE at the 11/18 close. CYPHER's rule A would still be its measure for the next wave."
    }
  ]
}
```
