from dispatch import *
D.clear()
add('UNG-reversal-analysis-still-positive','Fresh GFS analyzed vortex winds remain positive; UNG conditions are not satisfied','AEOLUS','TERRY WATT BRENT PROME','CLIMATE_MACRO','CLIMATE_MACRO','UNG GFS WQ-573 GATE-TERRY-UNG-01',
'''NOAA GFS f000 analysis, exact10hPa/60N zonal mean over1,440 longitudes: +3.903807m/s November3 00Z; +1.791158 November4 00Z; +1.092857 November4 12Z. All sampled analyses remain above the strict<0 reversal condition. They are analyzed model fields, not direct station observations or forecast leads. Decoder cross-checks agree and reproduce November2 control; sampling cannot exclude every intervening reversal. AEOLUS canonical acceptance/logging remains owed.

UNG unadjusted November2/3 closes9.00/9.13 agree across Yahoo/Nasdaq; neither meets the≥10.40 prior-close void. November4 intraday is not a closing leg. ACTION AEOLUS: apply existing observed-reversal watch/logging; INFO TERRY/WATT/BRENT/PROME: conditional-card evidence.

WQ-573 approval remains conditional: observed reversal byNovember12, red day byNovember20, entry<10.40, debit≤0.50 and all owner guards. No order, option-price refresh, condition waiver or new approval inferred.''',
'NOAA NOMADS exact URLs/raw hashes and calculations: AGENTS/WALTER/research/2026-11-04_catchup/vortex-observations.json',confidence=.95)
# Remaining consequential headline-only leads stay explicit; do not turn unread bodies into facts or automatic kills.
items=json.loads((OUT/'intake-items.json').read_text())
groups=[
('chip-source-leads','Remaining chip and memory headlines need source-qualified owner reconciliation','VULCAN','ZHAO','AI_INFRA_CAPEX','AI_CAPEX',[124,125,126,127,128,129,130,355,357,358,361,414,416]),
('collateral-source-leads','Remaining collateral headlines retain property and source gaps','CREED HOMER CORAL','REGINALD','BANK_COLLATERAL','BANK_CRE',[35,104,108,110,111,113,171,263,400]),
('energy-source-leads','Remaining energy headlines are leads, not measured outages or settlements','BRENT','HANS','HYDROCARBON_INFRA','OIL_ENERGY',[17,59,60,62,63,163,293,296,299,402,408,433,436,464]),
('Russia-source-leads','Remaining Russia and maritime headlines require event-date matching','YURI OSPREY HAWK','BRENT FALCON','MISC','RU_STATE_ACTOR',[33,167,168,397,398,404,407,462]),
('cyber-source-leads','Binance reporting and threat claims need incident-owner reconciliation','CYPHER','LIQUID','CYBER','CYBER',[218,221,229,447,452]),
('credit-macro-source-leads','Remaining credit and macro headlines retain denominator and body gaps','BROCK HANS','GIBBS','PC_STRESS','PRIVATE_CREDIT',[36,37,40,42,47,48,253,267,431]),
('weather-source-leads','Remaining regional ENSO coverage is ungraded source context','AEOLUS','CORAL BRENT','CLIMATE_MACRO','CLIMATE_MACRO',[161,164,390,391,393,394,395]),
('power-source-leads','Remaining power-sector headlines are ungraded proposals and company leads','WATT','VULCAN HANS','AI_INFRA_CAPEX','OIL_ENERGY',[145,146,377,378])]
for slug,title,action,info,cluster,domain,nums in groups:
 refs='\n'.join(f'- Intake {i}, {items[i-1]["date"]}: {items[i-1]["title"]}. [Locator]({items[i-1]["link"]})' for i in nums)
 body=f'''These source titles survived relevance screening in the November2–3 catchup. **Bodies/primary records were not recovered in this pass; none of their numbers, mechanisms or event dates is certified by this card.** Article date may differ from event date. Overlap with owner coverage remains unresolved for these exact articles. This is an explicit residual, not a completed research grade.

ACTION {action}: reconcile only the relevant existing domain work at the next authorized review; discard duplicates, retain limitations, and obtain decisive source evidence before changing a figure/gate. No new study, monitor, paid access, or desk launch is commissioned. INFO {info}: context only. Named-property distress case tags await authenticated identity/event; no source title alone supplies one. Primary route ownership remains per the canonical carve-outs.

{refs}'''
 add(slug,title,action,info,cluster,domain,action,body,'RESEARCH-INTAKE snapshot intake-items.json; exact list positions above',confidence=.4)
write(D,56)
