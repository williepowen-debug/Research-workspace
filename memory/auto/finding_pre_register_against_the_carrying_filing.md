---
name: finding_pre_register_against_the_carrying_filing
description: "Pre-register a threshold against the FILING/SOURCE that carries the metric, not the event date — a metric living in a 10-Q graded at the 8-K print date is unreachable by construction, and the failure tempts substituting the available-but-wrong series."
metadata:
  type: feedback
---

A pre-registered threshold can be **unreachable at its own grading date by construction** when the metric lives in a filing that arrives later than the event. REGINALD 7/25: its FL small-tier watch-card keyed its PRIMARY metric (CRE 30-89 accruing) to bank print dates, but that metric is a **10-Q age-analysis table** and no Q2 10-Q is filed at the print (they land ~a month later, EDGAR-verified). Silent, quarterly-recurring, and invisible until someone tries to score it.

**Why it's dangerous rather than merely annoying:** the pressure at grade time is to substitute whatever data the 8-K *does* carry (lagging buckets) and publish a confident-looking verdict off the wrong series — the exact error class the frame existed to prevent. REGINALD refused the substitution and marked legs PENDING-10-Q; that is the correct handling.

**How to apply:** at registration, for each metric name the SOURCE that carries it and confirm that source exists at the intended grade date. Where it doesn't: re-key the grade to the carrying filing, or pre-declare the leg unscoreable-at-print. Latent in every agent running pre-registered frames — publication-lag variants include official-vs-provisional series (BOND's DGS10-governs-retroactively rider is this rule applied once), detail-vs-headline tables (TIC country transactions), and instruments blind to the measured population ([[finding_ais_port_export_darkfleet_blind]]). Cf [[finding_threshold_spec_fails_before_world]] — the spec fails before the world does; this is the specific mechanism.
