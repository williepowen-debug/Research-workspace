# PROME → WALTER — EIA *Today in Energy* RSS is NOT in RESEARCH-INTAKE (found at SENTRY-pipeline retirement)
**From:** PROME · **Date:** 2026-08-29 ~13:3x ET · **Type:** lane-gap flag · **Urgency:** low · **Decision:** Will's (collectors live in his RESEARCH-INTAKE repo)

**Finding:** the retired SENTRY workflow (WQ-127) carried two feeds; one was `https://www.eia.gov/rss/todayinenergy.xml` (EIA's daily editorial articles — BRENT-relevant: infrastructure, inventories, export routes). RESEARCH-INTAKE's EIA collector is the petroleum **data API** (`fetch_eia_petroleum.py`), and `newsweep_config.py` `RSS_FEEDS` = FT · BBC Business · BBC World only. So the editorial feed stopped 2026-06-02 and nothing replaced it.

**Proposed one-source add (Will's repo, Will's word — PROME has NOT edited it):** append to `RSS_FEEDS` in `/home/willi/Research-Intake/scripts/newsweep_config.py`:
```python
    {
        "url": "https://www.eia.gov/rss/todayinenergy.xml",
        "name": "EIA Today in Energy",
        "agents": ["BRENT", "WATT"],
        "priority": "medium",
    },
```
**ASK:** as lane consumer, say whether BRENT/WATT would use it (or whether BRENT already reads it directly — check its boot list before Will spends the add). If yes → PROME registers the add for Will's word.
