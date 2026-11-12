"""Build the HENRY Operating Dashboard from STATUS figures (2026-11-12 midday, Nvidia CEO wake, session henry-38).
Every rail marker, zone and gamma mark is placed by one linear scale per rail."""
import html, sys

OUT = sys.argv[1]

def pct(v, lo, hi):
    return max(0.0, min(100.0, (v - lo) / (hi - lo) * 100))

# name, src, value, display, sub, direction ('up' = higher is risk), lo, hi, (y, o, r), dist_bold, dist_text, ghost
RAILS = [
    ("VIX", "vendor 12:12 ET 11/12 · ↑ risk", 17.58, "17.58", "VIX3M 19.34 · contango", "up", 10, 35, (23, 28, 30), "5.42 below", "the &gt;23 vol-control line", (28.18, "28.18 close 11/5")),
    ("S&amp;P 500", "vendor 12:12 ET 11/12 · ↓ risk", 7631.51, "7,632", "+0.16% day · low 7,567 at 09:33", "down", 6300, 8000, (7200, 7100, 7037.04), "432 above", "the &lt;7,200 yellow line", (7818.93, "7,819 peak 10/6")),
    ("10-yr Treasury", "Treasury par 11/10 · ↑ risk", 4.98, "4.98", "% par · vendor 5.10 at 12:12 ET 11/12", "up", 4.0, 5.4, (4.5, 4.8, 5.0), "2bp under red on par", "vendor intraday is 10bp over; graded on today's par after the close", (5.10, "5.10 vendor 11/12")),
    ("2-yr Treasury", "Treasury par 11/10 · ↑ risk", 4.73, "4.73", "% · was 4.56 on 11/9", "up", 3.8, 5.0, (4.25, 4.40, 4.60), "13bp through red", "red line &gt;4.60%; HEN-62 hit on this print", None),
    ("30-yr Treasury", "Treasury par 11/10 · ↑ risk", 5.35, "5.35", "% par · vendor 5.43 at 12:12 ET 11/12", "up", 4.6, 5.8, (5.0, 5.25, 5.5), "15bp below red on par", "orange", (5.43, "5.43 vendor 11/12")),
    ("High-yield spread", "FRED 11/11 · ↑ risk", 330, "330", "bp · 2026 high 348 on 11/5", "up", 220, 560, (320, 400, 500), "10bp through yellow", "70bp under orange", (348, "348 high 11/5")),
    ("CCC spread", "FRED 11/11 · ↑ risk", 1330, "1,330", "bp · +19 on the day", "up", 700, 1400, (900, 1000, 1100), "230bp through red", "the distressed tail; 1,356 on 10/23", (1356, "1,356 10/23")),
    ("SKEW", "vendor 11/11 close · ↑ risk", 149.09, "149.1", "153.55 on 11/6 (Cboe)", "up", 125, 175, (145, 150, 160), "in yellow", "RED-FT-10 grade is the owner's", None),
    ("Regional banks", "KRE vendor 12:12 ET 11/12 · ↓ risk", 72.54, "72.54", "KRE $ · −0.56% day", "down", 55, 80, (65, 62, 60), "$7.54 above", "the &lt;$65 yellow line", None),
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
          <div class="rail-name"><span class="rail-label">USD / JPY speed</span><span class="rail-src">|daily change| · vendor 12:12 ET 11/12 · SAM's call</span></div>
          <div class="rail-val">0.05%<span class="rail-sub">159.67</span></div>
          <div class="track">
            <div class="track-bar"><div class="zone z-max" style="left:{pct(2.0,jlo,jhi):.1f}%;right:0%"></div></div>
            <div class="marker" style="left:{pct(0.05,jlo,jhi):.1f}%"></div>
          </div>
          <div class="rail-dist"><b>1.95% away</b>escalate at ±2% in a day</div>
        </div>""")

# Gamma line, scale 7,450–7,750 (12:13 ET 11/12, chain asof 11/12 = 11/11 open interest)
GLO, GHI = 7450, 7750
gp = lambda x: pct(x, GLO, GHI)
gamma_html = f"""
      <div class="gamma-line">
        <div class="gl-bar"><div class="gl-neg" style="left:0;right:{100-gp(7634):.1f}%"></div></div>
        <div class="gl-band" style="left:{gp(7632):.1f}%;width:{max(gp(7636)-gp(7632), 0.8):.1f}%"></div>
        <div class="gl-lab gl-bot al-r" style="left:{gp(7633):.1f}%">flip band<b>7,633–7,635</b></div>
        <div class="gl-mark soft" style="left:{gp(7500):.1f}%"></div>
        <div class="gl-mark soft" style="left:{gp(7600):.1f}%"></div>
        <div class="gl-lab gl-bot al-l" style="left:{gp(7500):.1f}%">put-wall band<b>7,500–7,600</b></div>
        <div class="gl-mark soft" style="left:{gp(7567.36):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7567.36):.1f}%"><b>7,567</b>open low 09:33</div>
        <div class="gl-mark" style="left:{gp(7631.51):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7631.51):.1f}%"><b>7,632</b>12:12 ET</div>
        <div class="gl-mark soft" style="left:{gp(7700):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7700):.1f}%"><b>7,700</b>call wall</div>
      </div>"""

tpl = open(sys.argv[2], encoding="utf-8").read()
page = tpl.replace("{{RAILS}}", "".join(rails_html)).replace("{{GAMMA}}", gamma_html)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page))
