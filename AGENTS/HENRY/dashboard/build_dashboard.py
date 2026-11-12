"""Build the HENRY Operating Dashboard from STATUS figures (2026-11-12 after the close, Nvidia CEO wake, session henry-38).
Every rail marker, zone and gamma mark is placed by one linear scale per rail."""
import html, sys

OUT = sys.argv[1]

def pct(v, lo, hi):
    return max(0.0, min(100.0, (v - lo) / (hi - lo) * 100))

# name, src, value, display, sub, direction ('up' = higher is risk), lo, hi, (y, o, r), dist_bold, dist_text, ghost
RAILS = [
    ("VIX", "vendor 16:07 ET 11/12 · ↑ risk", 18.96, "18.96", "+8.4% day · VIX3M 20.20 · contango", "up", 10, 35, (23, 28, 30), "4.04 below", "the &gt;23 vol-control line", (28.18, "28.18 close 11/5")),
    ("S&amp;P 500", "vendor close 11/12 · ↓ risk", 7592.40, "7,592", "−0.35% day · low 7,567 at 09:33", "down", 6300, 8000, (7200, 7100, 7037.04), "392 above", "the &lt;7,200 yellow line", (7818.93, "7,819 peak 10/6")),
    ("10-yr Treasury", "Treasury par 11/12 · ↑ risk", 5.10, "5.10", "% par · +12bp on the session", "up", 4.0, 5.4, (4.5, 4.8, 5.0), "10bp through red", "red line crossed; WALTER card SIG-W-20261112-008", (4.98, "4.98 par 11/10")),
    ("2-yr Treasury", "Treasury par 11/12 · ↑ risk", 4.86, "4.86", "% · 4.73 on 11/10", "up", 3.8, 5.0, (4.25, 4.40, 4.60), "26bp through red", "red line &gt;4.60%; HEN-62 hit 11/10", (4.73, "4.73 par 11/10")),
    ("30-yr Treasury", "Treasury par 11/12 · ↑ risk", 5.43, "5.43", "% par · 20-year 5.48", "up", 4.6, 5.8, (5.0, 5.25, 5.5), "7bp below red", "orange", (5.35, "5.35 par 11/10")),
    ("High-yield spread", "FRED 11/11 · ↑ risk", 330, "330", "bp · 2026 high 348 on 11/5", "up", 220, 560, (320, 400, 500), "10bp through yellow", "70bp under orange", (348, "348 high 11/5")),
    ("CCC spread", "FRED 11/11 · ↑ risk", 1330, "1,330", "bp · +19 on the day", "up", 700, 1400, (900, 1000, 1100), "230bp through red", "the distressed tail; 1,356 on 10/23", (1356, "1,356 10/23")),
    ("SKEW", "vendor 11/11 close · ↑ risk", 149.09, "149.1", "153.55 on 11/6 (Cboe)", "up", 125, 175, (145, 150, 160), "in yellow", "RED-FT-10 grade is the owner's", None),
    ("Regional banks", "KRE vendor close 11/12 · ↓ risk", 72.52, "72.52", "KRE $ · −0.59% day", "down", 55, 80, (65, 62, 60), "$7.52 above", "the &lt;$65 yellow line", None),
]

def zones(direction, lo, hi, y, o, r):
    if direction == "up":
        spans = [("z-warn", y, o), ("z-crit", o, r), ("z-max", r, hi)]
    else:
        spans = [("z-max", lo, r), ("z-crit", r, o), ("z-warn", o, y)]
    out = []
    for cls, a, b in spans:
        L, R = pct(a, lo, hi), pct(b, lo, hi)
        out.append(f'<div class="zone {cls}" style="left:{L:.1f}%;right:{100-R:.1f}%"></div>')
    return "".join(out)

rails_html = []
for name, src, v, disp, sub, d, lo, hi, (y, o, r), db, dt, ghost in RAILS:
    g = ""
    if ghost:
        g = f'<div class="ghost" style="left:{pct(ghost[0], lo, hi):.1f}%" data-tick="{ghost[1]}"></div>'
    rails_html.append(f"""
        <div class="rail">
          <div class="rail-name"><span class="rail-label">{name}</span><span class="rail-src">{src}</span></div>
          <div class="rail-val">{disp}<span class="rail-sub">{sub}</span></div>
          <div class="track">
            <div class="track-bar">{zones(d, lo, hi, y, o, r)}</div>
            {g}
            <div class="marker" style="left:{pct(v, lo, hi):.1f}%"></div>
          </div>
          <div class="rail-dist"><b>{db}</b>{dt}</div>
        </div>""")

# USD/JPY velocity rail: |daily change| vs SAM's 2% escalation line
jlo, jhi = 0.0, 3.0
rails_html.append(f"""
        <div class="rail">
          <div class="rail-name"><span class="rail-label">USD / JPY speed</span><span class="rail-src">|daily change| · vendor 16:06 ET 11/12 · SAM's call</span></div>
          <div class="rail-val">0.07%<span class="rail-sub">159.86</span></div>
          <div class="track">
            <div class="track-bar"><div class="zone z-max" style="left:{pct(2.0,jlo,jhi):.1f}%;right:0%"></div></div>
            <div class="marker" style="left:{pct(0.07,jlo,jhi):.1f}%"></div>
          </div>
          <div class="rail-dist"><b>1.93% away</b>escalate at ±2% in a day</div>
        </div>""")

# Gamma line, scale 7,450–7,750 (16:06 ET close 11/12, chain asof 11/12 = 11/11 open interest)
GLO, GHI = 7450, 7750
gp = lambda x: pct(x, GLO, GHI)
gamma_html = f"""
      <div class="gamma-line">
        <div class="gl-bar"><div class="gl-neg" style="left:0;right:{100-gp(7632):.1f}%"></div></div>
        <div class="gl-band" style="left:{gp(7630):.1f}%;width:{max(gp(7635)-gp(7630), 0.8):.1f}%"></div>
        <div class="gl-lab gl-bot al-r" style="left:{gp(7632):.1f}%">flip band<b>7,630–7,635</b></div>
        <div class="gl-mark" style="left:{gp(7500):.1f}%"></div>
        <div class="gl-lab gl-bot al-l" style="left:{gp(7500):.1f}%">put wall<b>7,500</b></div>
        <div class="gl-mark soft" style="left:{gp(7567.36):.1f}%"></div>
        <div class="gl-lab gl-bot" style="left:{gp(7567.36):.1f}%"><b>7,567</b>open low 09:33</div>
        <div class="gl-mark" style="left:{gp(7592.40):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7592.40):.1f}%"><b>7,592</b>close</div>
        <div class="gl-mark soft" style="left:{gp(7700):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7700):.1f}%"><b>7,700</b>call wall</div>
      </div>"""

tpl = open(sys.argv[2], encoding="utf-8").read()
page = tpl.replace("{{RAILS}}", "".join(rails_html)).replace("{{GAMMA}}", gamma_html)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page))
