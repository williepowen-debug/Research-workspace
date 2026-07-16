# WALTER → PROME · NOTE — tested patch for the RESEARCH-INTAKE `fred` collector (your repo, your call)

**Date:** 2026-07-16 · **From:** WALTER · **Type:** diagnosis + tested patch, handed over for you to land
**Trigger:** Will asked "what's going on with the FRED feed? Can we fix?" — diagnosed, patched, tested. **Will directed the hand-off to you.**
**Target:** `/home/willi/Research-Intake/scripts/fetch_fred.py` — **the lane repo, which is READ-ONLY to WALTER** (boot step 7e: `pull --ff-only`, *"NEVER push to that repo"*). So I diagnose and hand over; **I have not touched it and will not.** `git status` in the lane is clean — verified after every test.

> **Not a signal:** no BOARD entry, no `route_log` / `delivery_log` row. A repo-maintenance patch, not market intelligence.

---

## TL;DR

**Nothing is broken. Don't treat it as a collector death.** The 7/15 `fred: degraded` was a **one-off transient** — FRED had a slow spell. **It self-heals on the next successful run.** But the collector has **no retry**, so a single slow response silently drops a series for the entire day — and the four it dropped included **ICSA, which feeds two registered fleet triggers**. Patch below: ~30 lines, retry-with-backoff, **10/10 unit tests + a live 16/16 end-to-end**. Your repo, your call.

## Diagnosis (not speculation — the errors are recorded)

`data/2026-07-15/fred.json`:

| Series | Recorded error |
|---|---|
| ICSA | `TimeoutError('The read operation timed out')` |
| CCSA | `TimeoutError('The read operation timed out')` |
| MORTGAGE30US | `TimeoutError('The read operation timed out')` |
| RSXFS | `<HTTPError 504: 'Gateway Time-out'>` |

**Transient upstream, full stop.** Not a bad key, not renamed series, not code rot:
- **12 of 16 series succeeded on the same run** (UMCSENT, PSAVERT, BAMLH0A0HYM2 all returned values + alerts) → the key and the code path are fine.
- **504 = FRED's server side.**
- **Run history is decisive: 13 consecutive clean runs (6/29 → 7/14), then exactly one bad run (7/15).**
- **I re-pulled all four live today: every one returned in under a second** (0.32–0.56s, against a 20s timeout) with values that cross-validate against the FORGE dashboard exactly (ICSA 208,000 [7/11], CCSA 1,805,000 [7/4]).

## The actual exposure (why it's still worth a patch)

`_fred()` makes **one attempt at `timeout=20` with no retry**. One slow response ⇒ the series is gone for the day, and it **fails silently** — a dropped series simply isn't in the output.

1. **ICSA feeds two registered fleet triggers — RED-FT-05 (claims >250k) and REG-T-05 (claims >300k).** Had claims spiked on 7/15, the lane would have been silent about it. *(The FORGE dashboard is redundancy for claims, so this was covered in practice — but the lane is the machine-independent surface, and that's the whole reason it exists.)*
2. **The 7/15 degrade didn't only drop data — it dropped a live ALERT.** My patched end-to-end run emits `MORTGAGE30US 30yr mortgage rate %=6.55 [orange]`. **That alert is absent from the 7/15 run** because the series errored. The lane silently under-reported.
3. **`liveness.json` says which feed degraded, not which series or whether any were trigger-bearing** — so "fred: degraded" reads identically whether it lost MORTGAGE30US or ICSA.

## The patch

Confined to `_fred()` + two stdlib imports. **No behaviour change on the happy path** (single call, no added latency) and **no behaviour change on permanent failure** (the caller still records the error string exactly as today).

```diff
--- a/scripts/fetch_fred.py
+++ b/scripts/fetch_fred.py
@@ -17,6 +17,8 @@
 import json
 import os
 import pathlib
+import time
+import urllib.error
 import urllib.parse
 import urllib.request
 
@@ -69,13 +71,41 @@
     return out
 
 
+# Transient upstream conditions worth a retry. 4xx (bad key / unknown series) is
+# PERMANENT — retrying it wastes the run and risks rate-limiting, so it fails fast.
+_RETRY_HTTP = {429, 500, 502, 503, 504}
+_RETRY_BACKOFF = (2, 5)  # seconds between attempts 1→2 and 2→3
+
+
 def _fred(series_id, key, limit=15):
+    """Pull a FRED series, retrying transient upstream failures.
+
+    Added 2026-07-16 after the 2026-07-15 run lost ICSA/CCSA/RSXFS/MORTGAGE30US to
+    read-timeouts + a 504 while the other 12 series succeeded — i.e. FRED had a slow
+    spell, not a broken key/series. With a single 20s attempt and no retry, one slow
+    response silently drops a series for the whole day. ICSA feeds two registered
+    fleet triggers (RED-FT-05 >250k, REG-T-05 >300k), so a silent one-day hole in it
+    is the real exposure. History: 13 consecutive clean runs before 7/15 → the
+    failure is transient and retry-shaped, not structural.
+    """
     params = {"series_id": series_id, "api_key": key, "file_type": "json",
               "sort_order": "desc", "limit": limit}
     url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
     req = urllib.request.Request(url, headers={"User-Agent": "Research-Intake/fred"})
-    with urllib.request.urlopen(req, timeout=20) as r:
-        data = json.loads(r.read())
+    attempts = len(_RETRY_BACKOFF) + 1
+    for attempt in range(attempts):
+        try:
+            with urllib.request.urlopen(req, timeout=20) as r:
+                data = json.loads(r.read())
+            break
+        except urllib.error.HTTPError as e:
+            if e.code not in _RETRY_HTTP or attempt == attempts - 1:
+                raise  # permanent (4xx) or out of attempts → caller records it as today
+            time.sleep(_RETRY_BACKOFF[attempt])
+        except (TimeoutError, urllib.error.URLError, json.JSONDecodeError) as e:
+            if attempt == attempts - 1:
+                raise
+            time.sleep(_RETRY_BACKOFF[attempt])
     return [{"date": o["date"], "value": o["value"]}
             for o in data.get("observations", []) if o["value"] != "."]
```

### Design decisions worth your review

- **Retries transient only** (`429/500/502/503/504`, `TimeoutError`, `URLError`, `JSONDecodeError`). **4xx fails FAST — deliberately.** A bad key or unknown series is permanent; retrying it wastes the run and risks rate-limiting. *(This also preserves a real diagnostic: if a series ID ever genuinely dies, you still find out on the first attempt.)*
- **`JSONDecodeError` is in the retry set** because a truncated body from a struggling server is the same transient class as a timeout. Debatable — drop it if you'd rather see a parse failure loudly.
- **3 attempts, 2s/5s backoff.** Worst case per series ≈ 67s; if all 16 failed ≈ 18 min (well inside an Actions run). On the 7/15 shape (4 failures) it'd have added **≈ 4.5 min**.
- **On exhaustion it re-raises** → `fetch()`'s existing `except` records the same error string it does today. **Failure semantics are unchanged; only the odds improve.**

## Test evidence (a patch I hand over untested is just a suggestion)

**Unit — 10/10, mocked `urlopen`, backoff shortened to keep it fast (logic unchanged):**

| Class | Case | Expected | Result |
|---|---|---|---|
| Transient | timeout ×1 → OK | retry, succeed, 2 calls | ✅ |
| Transient | 504 ×1 → OK | retry, succeed, 2 calls | ✅ |
| Transient | timeout + 504 → OK | retry twice, succeed, 3 calls | ✅ |
| Transient | URLError ×1 → OK | retry, succeed, 2 calls | ✅ |
| **Permanent** | **400 / 403 / 404** | **fail fast, 1 call, NO retry** | ✅ ×3 |
| Exhaustion | timeout ×3 / 504 ×3 | raise after 3, caller records | ✅ ×2 |
| Happy path | no failure | 1 call, unchanged | ✅ |

**Live end-to-end** (patched copy, real FRED, scratchpad — lane untouched):
```
status=ok   series=16   errored=[]   10.7s
alerts: UMCSENT 44.8 [red] · PSAVERT 3.0 [orange] · MORTGAGE30US 6.55 [orange] · BAMLH0A0HYM2 271.0 [orange]
```
All four previously-failing series return. **Note `MORTGAGE30US 6.55 [orange]` — the alert 7/15 silently lost.**

## To apply

The patch is against `scripts/fetch_fred.py` at its current HEAD (last touched 2026-07-02). The tested copy is in WALTER's scratchpad, but **it is a scratch path and will not survive** — regenerate from the diff above, or ping me and I'll re-emit it. **The lane needs `FRED_API_KEY` (GH Actions secret) — unchanged by this patch.**

## Explicitly NOT in this patch (your design call, not mine)

**The fail-loud question.** The retry fixes the *odds*; it does not fix the *semantics*. A dropped series is still silent, and `liveness.json` still can't distinguish "lost MORTGAGE30US" from "lost ICSA, which feeds two registered triggers." Options if you want it — **I'm not proposing, just naming them:**
- mark trigger-bearing series (`ICSA`, `BAMLH0A0HYM2`, …) as CRITICAL in `SERIES`, and surface a distinct alert when one errors, so a consumer can tell a cosmetic gap from a trigger-blind one;
- or leave it — WALTER's `intake_liveness` doctor check already MEDs on any degrade, and the FORGE dashboard is redundancy for claims.

I kept the patch to the bug rather than redesigning your collector. Scope is yours.

## One caveat on my own diagnosis

The "13 clean runs" history is from `data/2026-06-29` → `2026-07-15` — **the retained window, not all time**. It's enough to establish "transient, not structural," but it isn't a full base rate. If `fred: degraded` recurs within ~2 weeks **with the patch in**, the transient read is wrong and it wants a real look (rate-limiting, or an Actions-runner network issue rather than FRED).

---
*Create-only note per WALTER Routing v2 — move to `inbox/WALTER/processed/` on consume. No BOARD entry; no route/delivery/kill row (not a dispatch). WALTER did not and will not write to `/home/willi/Research-Intake` — landing this is yours.*
