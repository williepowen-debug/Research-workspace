# Panama: Gatun level vs Neopanamax draft limit (2026-11-23)

Finding: KB-AEO-312. Table: `timeline.tsv` (54 effective changes; steps that were announced then postponed or suspended are dropped).

**Inputs (not committed):** ACP index `https://pancanal.com/en/maritime-services/advisory-to-shipping/` and 97 advisory PDFs (curl default client name, HTTP 200 for all) · `gatun.csv` from `evtms-rpts.pancanal.com` (sha256 6b15595a..., to 2026-11-22) · CPC `oni.ascii.txt`. Some PDFs carry a no-extraction flag that pdfminer ignores; the text was used for figures only.

**Scripts:** `map.py` (timeline, gaps, counts) · `reg.py` (drop on DJF ONI, 11/22 level, post-2016; s 1.19 ft). Run in a directory holding the inputs; `reg.py` needs numpy.

**Limits:** seasons with the big locks in normal service n=8; the 2018 planning table is one advisory; cuts are set on PROJECTED levels with about 4 weeks of notice, so the effective-day level is a proxy; ONI 2.5 sits at the edge of the sample.
