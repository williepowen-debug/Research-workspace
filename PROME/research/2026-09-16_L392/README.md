# L392 observation protocol — September 16

Calibration remains OPEN. The 900-second cutoff is unchanged. This collection prepares evidence, not an automatic choice of cutoff.

The instrument is `BZ=F` versus dated NYM BZ candidates, not an ICE contract relabelled as NYM. [CME contract specifications](https://www.cmegroup.com/ja/markets/energy/crude-oil/brent-crude-oil-last-day.html), checked September 16, list 18:00–17:00 Eastern trading with a daily break. The pre-close window here is 16:00–17:00 ET (session close, not the settlement marker); the overnight leg is the evening session, 20:00–21:00 ET. This Wednesday is not a listed holiday. Observe at 16:05/16:25/16:45 and 20:05/20:25/20:45 ET. These are sampling times, not proposed grading thresholds.

Run from repository root: `python3 PROME/research/2026-09-16_L392/collect.py --schedule`. The run is bounded to six samples, each with a subprocess timeout, and does not change any market-data tool, registry or grade. A missed window is printed MISSED and not backfilled. The process must remain alive; it is not a persistent installed service. Check runtime and sample files before claiming collection. `--once` is a setup test and never substitutes for a window. `--plan` prints the schedule without network.

Retain full probe JSON, stderr, return code, source-code digest, and start/end times. `candidate_age_s` is the difference from the continuous quote timestamp, not wall-clock quote age. Review both. Distinguish matched candidates (the cutoff affects identification) from nonmatched candidates (staleness is advisory). Inspect unavailable timestamps, retries, refusals and the negative control, never only successful matches. Do not assume two old synchronized quotes are live because their relative age is zero.

After both windows, tabulate candidate timestamp changes and matched-leg age/refusal behavior. A six-sample pilot does not estimate a reliable tail or false-identification rate; if observations do not discriminate cutoffs, retain 900 as UNCALIBRATED and specify the additional sample needed. Numeric calibration and independent implementation review (L394) remain separate obligations.
