"""GLD on equity-stress days (SPX <= -1.0% or dVIX >= +2.0), MIDAS WQ-451, 2026-10-23."""
import sys, runpy, io, contextlib
with contextlib.redirect_stdout(io.StringIO()): g=runpy.run_path(sys.argv[0].replace("stress.py","classify.py"))
d=g["d"]
for lab,h in [("2025-01..2026-10-22",d),("2026 only",d.loc["2026"]),("last 120 pairs",d.tail(120))]:
    s=h[(h.spx<=-1.0)|(h.dvix>=2.0)]
    print(f"{lab}: stress days {len(s)}; GLD up {int((s.gld>0).sum())} ({(s.gld>0).mean():.0%}); mean GLD {s.gld.mean():+.2f}% vs mean SPX {s.spx.mean():+.2f}%; residual e>0 {(s.e>0).mean():.0%}; classes {s.cls.value_counts().to_dict()}")
