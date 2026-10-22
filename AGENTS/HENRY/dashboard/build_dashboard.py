"""Build the HENRY Operating Dashboard from tonight's STATUS figures (2026-10-22 close, DOCKET L787).
Every rail marker, zone and gamma mark is placed by one linear scale per rail."""
import html, sys

OUT = sys.argv[1]

def pct(v, lo, hi):
    return max(0.0, min(100.0, (v - lo) / (hi - lo) * 100))

# name, src, value, display, sub, direction ('up' = higher is risk), lo, hi, (y, o, r), dist_bold, dist_text, ghost
RAILS = [
    ("VIX", "vendor 10/22 close · ↑ risk", 19.03, "19.03", "VIX3M 20.12", "up", 10, 35, (23, 28, 30), "3.97 below", "the &gt;23 vol-control line", (22.31, "22.31 hi 10/16")),
    ("S&amp;P 500", "Cboe + vendor 10/22 close · ↓ risk", 7663.43, "7,663", "−1.21% day", "down", 6300, 8000, (7200, 7100, 6494), "463 above", "the &lt;7,200 yellow line", (7818.93, "7,819 peak 10/6")),
    ("10-yr Treasury", "Treasury par 10/22 · ↑ risk", 4.96, "4.96", "% · was 5.13", "up", 4.0, 5.4, (4.5, 4.8, 5.0), "4bp under red", "orange; red line &gt;5.00%", None),
    ("2-yr Treasury", "Treasury par 10/22 · ↑ risk", 4.65, "4.65", "% · was 4.81", "up", 3.8, 5.0, (4.25, 4.40, 4.60), "5bp through red", "red line &gt;4.60%", None),
    ("30-yr Treasury", "Treasury par 10/22 · ↑ risk", 5.29, "5.29", "% · was 5.42", "up", 4.6, 5.8, (5.0, 5.25, 5.5), "21bp below red", "orange", None),
    ("High-yield spread", "FRED 10/21 · ↑ risk", 327, "327", "bp", "up", 220, 560, (320, 400, 500), "7bp through yellow", "6 readings above 320", None),
    ("CCC spread", "FRED 10/21 · ↑ risk", 1307, "1,307", "bp", "up", 700, 1400, (900, 1000, 1100), "207bp through red", "the distressed tail", None),
    ("SKEW", "vendor 10/22 · ↑ risk", 152.39, "152.4", "150.4 on 10/21", "up", 125, 175, (145, 150, 160), "in orange", "RED-FT-10 grade is the owner's", None),
    ("Regional banks", "KRE vendor 10/22 · ↓ risk", 72.41, "72.41", "KRE $ · +2.53% day", "down", 55, 80, (65, 62, 60), "$7.41 above", "the &lt;$65 yellow line", None),
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
          <div class="rail-name"><span class="rail-label">USD / JPY speed</span><span class="rail-src">|daily change| · SAM's call</span></div>
          <div class="rail-val">1.0%<span class="rail-sub">156.64 vs 158.17</span></div>
          <div class="track">
            <div class="track-bar"><div class="zone z-max" style="left:{pct(2.0,jlo,jhi):.1f}%;right:0%"></div></div>
            <div class="marker" style="left:{pct(0.97,jlo,jhi):.1f}%"></div>
          </div>
          <div class="rail-dist"><b>1.0% away</b>escalate at ±2% in a day</div>
        </div>""")

# Gamma line, scale 7,600–7,850 (10/22 close)
GLO, GHI = 7600, 7850
gp = lambda x: pct(x, GLO, GHI)
gamma_html = f"""
      <div class="gamma-line">
        <div class="gl-bar"><div class="gl-neg" style="left:0;right:{100-gp(7745):.1f}%"></div></div>
        <div class="gl-band" style="left:{gp(7742):.1f}%;width:{gp(7748)-gp(7742):.1f}%"></div>
        <div class="gl-lab gl-bot al-r" style="left:{gp(7742):.1f}%">flip band<b>7,742–7,748</b></div>
        <div class="gl-mark soft" style="left:{gp(7650):.1f}%"></div>
        <div class="gl-lab gl-bot al-l" style="left:{gp(7650):.1f}%">put wall<b>7,650</b></div>
        <div class="gl-mark" style="left:{gp(7663.43):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7663.43):.1f}%"><b>7,663</b>close</div>
        <div class="gl-mark soft" style="left:{gp(7800):.1f}%"></div>
        <div class="gl-lab gl-top" style="left:{gp(7800):.1f}%"><b>7,800</b>14d call wall</div>
        <div class="gl-lab gl-bot al-r" style="left:100%">35d call wall<b>8,000 →</b></div>
      </div>"""

tpl = open(sys.argv[2], encoding="utf-8").read()
page = tpl.replace("{{RAILS}}", "".join(rails_html)).replace("{{GAMMA}}", gamma_html)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page))
