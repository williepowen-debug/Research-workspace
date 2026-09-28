# WQ-291 grade (Will-ruled 2026-09-26): 9/23 5Y kill dealer leg = FR2004 3-6Y coupon inventory.
# MET iff as-of 2026-09-23 >= $56.586B (PRE as-of 9/16 $47.986B + $8.6B). Prints Thu 10/1 ~16:15 ET.
# Riders (travel with ANY verdict): net inventory != proof of warehousing · the funding window for the
# 9/23 fire is EXPLICITLY UNGRADED · no predictive claim · a MET = recommendation via TERRY's card + Will.
# rc: 0 = graded (MET or NOT MET, printed) · 3 = GAP (as-of 9/23 not published yet) · 2 = fetch failure / PRE mismatch.
# Dry-run 2026-09-28: expected rc=3 (GAP) with PRE reproducing $47.986B.
import sys, datetime as dt
sys.path.insert(0, "monitors"); import fr2004_fetch as F

KEY, PRE_D, POST_D = "PDPOSGSC-G3L6", dt.date(2026, 9, 16), dt.date(2026, 9, 23)
PRE_EXPECTED, BAR = 47.986, 56.586

try:
    m = {}
    for sb in ("SBN2022", "SBN2024"):
        m.update(F.fetch(KEY, sb))
except Exception as e:
    print(f"[wq291] rc=2 FETCH FAILURE — NOT a verdict: {e!r}"); sys.exit(2)
ser = {(d if isinstance(d, dt.date) else dt.date.fromisoformat(str(d))): (float(v) / 1000 if float(v) > 1e4 else float(v)) for d, v in m.items()}
if not ser:
    print("[wq291] rc=2 EMPTY SERIES — NOT a verdict"); sys.exit(2)
latest = max(ser)
print(f"[wq291] {KEY} n={len(ser)} latest as-of {latest} = ${ser[latest]:.3f}B")
pre = ser.get(PRE_D)
if pre is None or abs(pre - PRE_EXPECTED) > 0.0015:
    print(f"[wq291] rc=2 PRE MISMATCH: as-of {PRE_D} = {pre} vs registered ${PRE_EXPECTED}B — stop, reconcile before grading"); sys.exit(2)
print(f"[wq291] PRE as-of {PRE_D} = ${pre:.3f}B ✅ reproduces the registered figure")
post = ser.get(POST_D)
if post is None:
    print(f"[wq291] rc=3 GAP — as-of {POST_D} not published (latest {latest}). Report GAP, never a pass or a fail.")
    sys.exit(3)
d, margin = post - pre, post - BAR
verdict = "MET" if post >= BAR else "NOT MET"
print(f"[wq291] POST as-of {POST_D} = ${post:.3f}B · Δ vs PRE {d:+.3f}B · bar ${BAR}B · margin {margin:+.3f}B ⇒ {verdict}")
print("[wq291] riders: net inventory ≠ proof of warehousing · funding window UNGRADED by ruling · no predictive claim · "
      + ("a MET is a RECOMMENDATION via TERRY's card + Will, never a BOND action" if verdict == "MET" else "NOT MET changes no position"))
sys.exit(0)
