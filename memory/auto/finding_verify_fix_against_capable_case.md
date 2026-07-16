---
name: finding_verify_fix_against_capable_case
description: "Verifying a fix against a case that CANNOT exhibit the bug proves nothing and can manufacture a phantom failure — pick the test case by whether it's capable of demonstrating the change, and always include a control that isolates your bug from unrelated walls."
metadata: 
  node_type: memory
  type: finding
  originSessionId: bd8279ea-4bcb-44d7-a76b-0ad3a0a4cbd7
---

**The pattern (2026-07-16, DEWEY):** fixed a real silent-truncation bug in `fred_pull.py` (a `--start` range returned only the ten OLDEST rows, no error). First verification pull was `BAMLH0A0HYM2` (HY OAS) with `--start 2020-02-14` — it came back starting 2023-07-17, i.e. *still apparently broken*. But that series is **licence-truncated by FRED to a rolling ~3-year window**: it is structurally incapable of returning 2020 data whether the bug is fixed or not. Only running controls (`UNRATE` → 942 rows to 1948; `DGS10` → 9,532 to 1990) proved the fix worked and isolated the truncation as a **separate, unrelated wall**. Without the control I'd have reported a phantom fix-failure — or "fixed" a bug that was already fixed.

**Why:** a test case is only evidence if it can produce both outcomes. When the case is subject to an independent constraint (licensing, auth, rate-limit, empty-by-design), the observation is confounded and the result is uninformative in *either* direction — a pass proves nothing and a fail indicts the wrong thing. This is the sibling of picking a discriminating metric: an indicator that can't move can't inform. Two silent-failure modes stacking (my bug + their licence cap) is exactly when this bites, because the symptom looks identical.

**How to apply:** before verifying any fix/build, ask **"can this case exhibit the change?"** Pick a case known to have the property under test (long history, the disclosed field, the error path), and **pair every verification with a control that isolates your change from environmental walls** — ideally one expected to pass and one expected to fail. State the control in the write-up; "verified" without a capable case is an unsupported claim. Related: [[finding_verify_recommended_fix_not_just_finding]] (the fix itself may be wrong), [[finding_declared_data_wall_needs_fleet_memory_check]] (the wall may not be real), [[finding_verify_runtime_context_before_tool_broken]].
