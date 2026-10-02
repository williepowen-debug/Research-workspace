"""Pinned, network-free check of the withheld swap-line command's entry point.

Run from the Git root with python3 -B. Prints evidence; writes no owner files.
This is not a market-data test or acceptance of the instrument's grading logic.
"""
import contextlib
import datetime
import io
import json
import subprocess
import types

PIN = "dc4c37b438a1f0ab2949be3b782ae4dbbfdd757e"
PATH = "AGENTS/LIQUID/scripts/usd_swapline.py"
module = types.ModuleType("cato_isolated_swapline")
module.__file__ = PATH
source = subprocess.check_output(["git", "show", f"{PIN}:{PATH}"], text=True)
exec(compile(source, PATH, "exec"), module.__dict__)


class FixedDate(datetime.date):
    @classmethod
    def today(cls):
        return cls(2026, 10, 1)


def blocked(*args, **kwargs):
    raise AssertionError("Unexpected network attempt")


module.dt = types.SimpleNamespace(date=FixedDate, timedelta=datetime.timedelta)
module._get = blocked
module.ops = lambda *args, **kwargs: [
    dict(trade="2026-09-30", settle="2026-10-01", mat="2026-10-08",
         cp="European Central Bank", bn=0.1, rate=4.0, term=7)
]
module.swpt = lambda *args, **kwargs: [("2026-09-30", 100.0)]
output = io.StringIO()
with contextlib.redirect_stdout(output):
    rc = module.main([])
print(json.dumps({
    "pin": PIN, "path": PATH,
    "case": "Withheld instrument entry point with synthetic healthy quiet feeds",
    "return_code": rc, "output": output.getvalue(),
    "withheld_banner": "WITHHELD" in output.getvalue(),
}, indent=2, ensure_ascii=False))
