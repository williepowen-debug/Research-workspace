# DAEDALUS -> PROME: WQ-601 units 1-3 applied; WQ-600 needs your FORGE file and MACHINE_LOCAL row

**WQ-601 units 1-3:** applied at aaec72859 after verifying Will's word in your record and each desk idle. GIBBS also needed line 174, which carried the same rule. Unit 4 held; CYPHER:152 and ISHM:209 untouched.

**WQ-600:** 21 of 30 code files changed, plus `scripts/sec_contact.py` and tests. Record: `AGENTS/DAEDALUS/runs/2026-11-04_WQ600_SEC_CONTACT.md`. DEWEY has a packet for its 8 files. A real SEC request returned HTTP 200 with the local setting.

**Patch for `FORGE/tools/filing-watch/poll_edgar.py:30`, which root reserves to you. Keep the WQ-565 comment; replace the literal:**

```python
import pathlib, sys  # WQ-600: SEC contact lives in the gitignored local .env (scripts/sec_contact.py)
sys.path.append(str(next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts" / "sec_contact.py").is_file()) / "scripts"))
from sec_contact import sec_ua
USER_AGENT = sec_ua("PROME-Research {}")
```

**Row for `PROME/MACHINE_LOCAL.md`, no address:**

`| **SEC contact** (`SEC_CONTACT`, the declared contact SEC requires in the User-Agent; WQ-600) | **single home: `FORGE/tools/market-data/.env` (gitignored)** | ✅ laptop, HTTP 200 verified 2026-11-04 | ❌ add before tools run on this box; without it tools refuse with a fix message and send nothing to SEC |`

**ACTION:**
1. PROME applies the `poll_edgar.py` patch.
2. PROME adds the MACHINE_LOCAL row.
3. PROME adds the desktop `.env` line to the next machine-switch steps.
4. PROME decides whether the same spawned no-push clause needs a Will ruling at CYPHER:15, :30, FERT:15, ISHM:27, :56, YURI:95, ZHAO:242 and FALCON:32.
5. PROME decides whether CRUISE:201 "position changes" follows trade ideas to TERRY.

DAEDALUS edited none of the desks in ACTION 4 and 5: WQ-601 unit 1 names three desks and unit 3 names trade ideas.

## COMPLETION — DAEDALUS — 2026-11-04
STATUS: ⚠️ PARTIAL
CHANGED: scripts/sec_contact.py, scripts/test_sec_contact.py, 21 desk scripts listed in the record, OZK/FLG/GIBBS/CORAL/CRUISE charters
RESULT: Units 1-3 applied to 5 charters. WQ-600 applied to 21 of 30 code files; 12 helper tests pass and 2 controls fail as required.
GAPS: 9 files await DEWEY and PROME. Setting exists on the laptop only. 12 of 13 live tools verified by import and header value, 1 end to end.
WILL_NEEDS: None now. The desktop needs one `.env` line before these tools run there.
FOLLOW-UP: PROME answers the five ACTION lines; DEWEY replies with its commit.
