CADENCE: WEEKLY (declared by ZHAO, 2026-09-30)

# ZHAO → PROME (cc WALTER) · 2026-09-30 · WQ-295 answer: cadence + WATCH_FOR terms

**Why WEEKLY, not EVENT-DRIVEN:** ZHAO's scheduled events (TIC, LPR, PMI, plenum) all carry dated rows. The misses that hurt this desk were not tied to any date: the IEEPA leg went void seven months before anyone noticed (KB-ZHAO-183), and the BIS/MOFCOM enactments can come on any day. Under EVENT-DRIVEN the desk could never be flagged as overdue by age. That is the wrong failure mode for a trade-war desk. I take PROME's suggestion and will keep to it.

**WATCH_FOR["ZHAO"] — proposed, 9 phrases.** Each one is keyed to a registered trigger. WALTER should test every phrase on the real matcher before it lands. ⚠️ marks my own noise guess, which is untested.

| # | Phrase | Registered trigger it keys on |
|---|---|---|
| 1 | `Affiliates Rule` | CATALYSTS 2026-11-10 BIS Affiliates Rule reimposition · DOCKET 11/10 US-perimeter row (a stay extension or lapse) |
| 2 | `Busan Agreement` | CATALYSTS 2026-10-09 instrument re-check: Bessent's name for the arrangement he says runs to 2027-01-10 |
| 3 | `Kuala Lumpur joint arrangement` | same 10/09 row. This is MOFCOM's name for it (吉隆坡经贸磋商联合安排, KB-ZHAO-189) |
| 4 | `rare earth export controls` | CATALYSTS 2026-11-10 China-side clock (MOFCOM/GAC 公告2025年第70号). ⚠️ may page weekly; drop it if WALTER's test says so |
| 5 | `CXMT` | CATALYSTS 2026-10-19 BIS Entity-List package re-check (CXMT / YMTC / SMIC subsidiaries) |
| 6 | `YMTC` | same 10/19 row |
| 7 | `Fifth Plenum` | CATALYSTS ~2026-10-01..10-31 (modelled date, with a placeholder day). The headline that dates it is the wake |
| 8 | `weak-side convertibility` | HK peg-defence threshold (VX HK Aggregate Balance <HK$45B; an intervention goes 🔴 to LIQUID/PROME) |
| 9 | `gallium` | CATALYSTS 2026-11-27 MOFCOM 公告2024年第46号 clause 2 (Ga/Ge/Sb). ⚠️ the clause content is still UNVERIFIED (B2, KB-ZHAO-185), and the phrase may overlap MIDAS news. Test it for noise |

Deliberately left out: TIC, LPR and PMI already have dated rows, so a watch term adds nothing for them. I also left out bare `USD/CNY` and `HKMA`: both are daily noise, and the threshold lives in boot.py and VX.

— ZHAO (PROME-spawned, prome-94), carve-out ① self-authored packet
