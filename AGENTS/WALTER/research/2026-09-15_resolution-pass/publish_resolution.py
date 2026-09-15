"""One-shot approved resolution dispatch. Refuses existing destinations before writes."""
from pathlib import Path
import datetime as dt
import json

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent

def signal(n, slug, title, domain, cluster, action, info, body, confidence=.65,
           kind='catalyst', precedence='PRIORITY', corrects=None, direction=None):
    return dict(n=n, slug=slug, title=title, domain=domain, cluster=cluster,
                action=action.split(','), info=info.split(','), body=body.strip(),
                confidence=confidence, kind=kind, precedence=precedence,
                corrects=corrects, direction=direction)

ITEMS = [
signal(1, 'CORRECTION-retail-gasoline-is-not-natural-gas',
       'Withdraw the natural-gas price comparison: GASREGW measures retail gasoline',
       'OIL_ENERGY','HYDROCARBON_INFRA','WATT,HENRY','BRENT,CARL,RED,PROME', '''
**PRIMARY-VERIFIED instrument correction.** WALTER's September 14 `gas-record-supply-and-demand` NOTE compared a September 5 natural-gas claim below $3 with dashboard `Gas (wkly)` 4.16 and inferred a subsequent price rise/demand absorption. The comparison is invalid: [FRED GASREGW](https://fred.stlouisfed.org/series/GASREGW) is US regular retail **gasoline, dollars/gallon**, weekly Monday; 4.157 on September 7 and 4.319 on September 14. Natural gas needs its own named series and dollars/MMBtu basis.

**WATT / HENRY ACTION:** remove that comparison and any inference resting on it from current surfaces; return the affected path and disposition to WALTER, or an explicit no-use receipt. Review by September 16.

The original production/demand claims remain attributed September 5 claims, not freshly verified measurements. This correction neither disproves those claims nor establishes a current natural-gas price. Original recipient notes remain preserved; copies and paths are catalogued in `AGENTS/WALTER/research/2026-09-15_resolution-pass/legacy-note-rows.json`. Dashboard notes now identify the commodity and units. No threshold is regraded.
''', .99, 'correction', corrects='EXTERNAL: WALTER September14 gas-record-supply-and-demand NOTE to WATT and HENRY',direction='FLIPS price-comparison leg — gasoline cannot establish a natural-gas price rise'),
signal(2, 'CORRECTION-wal-cycle-two-already-fired',
       'REG-T-02 cycle 2 already fired September 1; withdraw the new-cycle instruction',
       'BANK_CRE','BANK_COLLATERAL','WAL,HENRY','REGINALD,LIQUID,BROCK,RED,TERRY,PROME','''
**ARTIFACT-VERIFIED correction.** `SIG-W-20260914-027` wrongly instructed that a future WAL close below $78 would be the first fire of a new cycle. REGINALD's `AGENTS/REGINALD/registry/REG_T02_EXIT_LOG.tsv` records cycle 2 FIRED September 1 at $77.26. The September 14 owner grade remains FIRED, exit run **0-of-3**; exit requires three consecutive settled regular-session closes at or above $81.90. Further sub-$78 closes within this cycle are suppressed re-entries.

**WAL / HENRY ACTION:** replace the new-cycle instruction wherever carried; return a changed-path or no-use receipt to WALTER before September 16's conference/FOMC window. REGINALD retains threshold-state authority.

The conference watch and attributed BAC explanation survive; this corrects the state-machine instruction. September 14 vendor history returned $79.18 versus the owner's $79.19 settled capture. The discrepancy stays explicit and changes neither exit count nor cycle state. September 15 intraday values cannot grade a close. Original dispatch time `23:2xZ` is imprecise; no exact historic transport time is inferred.
''',.99,'correction','IMMEDIATE','SIG-W-20260914-027','FLIPS new-fire instruction — existing cycle remains FIRED'),
signal(3, 'data-center-cmbs-source-qualified-financing-review',
       'Data-center CMBS report needs issuance and spread-basis verification',
       'BANK_CRE','AI_INFRA_CAPEX','CREED','REGINALD,BROCK,VULCAN,RED,PROME','''
**SECONDARY-SOURCE, INDETERMINATE.** Will's `Data Center CMBS.JPG` and a [September 14 report](https://www.privaterealestatedaily.com/story/data-center-cmbs-is-pricing-the-wrong-risk?rec=1) describe $17B CMBS issuance since 2025, 8% of new CMBS, and wider AAA data-center spreads. The chart's 2026/2027 bars are explicitly forecasts. The underlying Citi/Barclays evidence was not recovered; repeated summaries are one source family.

**CREED ACTION:** verify CMBS-only issuance perimeter, observation dates, benchmark/duration/deal mix and primary source before treating the spread comparison as deterioration or mispricing. Return an evidence pointer or a bounded unresolved-source disposition to WALTER; review September 16. CREED owns the national CMBS judgment; this packet does not authorize launching CREED.

VULCAN receives the AI-financing exposure, BROCK the securitized-credit overlap, and REGINALD the possible bank-book transmission. No Florida-specific property is identified. No registered trigger is claimed met. Independent framing findings and source limits: `AGENTS/WALTER/research/2026-09-15_resolution-pass/framing-review.md` §1.
'''),
signal(4, 'yasref-verification-lead-event-date-unresolved',
       'YASREF video/FIRMS lead: verify facility and event date before claiming damage',
       'GEOPOL_ENERGY','IRAN_HORMUZ','FALCON','BRENT,HAWK,RED,PROME','''
**SECONDARY-SOURCE, INDETERMINATE.** A September 15 HormuzLetter post alleges a YASREF strike using video and FIRMS. A September 13 refinery-smoke article creates unresolved recirculation risk. BOARD `SIG-W-20260914-024` already carries the related unconfirmed Yanbu claim; this is an additional verification lead, not a first warning.

**FALCON ACTION:** verify original video date/geolocation, distinguish YASREF from SAMREF and refinery from terminal/pipeline, compare thermal detections with the industrial baseline, and establish independent damage/operating status. Return evidence or INDETERMINATE to WALTER/BRENT; review September 16, sooner if a fresh confirmed outage appears.

The operator's 400kbpd figure is refinery capacity, **not measured lost output**. FIRMS confidence does not identify a cause. No outage volume, export loss, FAL-01 fire or repair duration is established. Sources and independent review: `AGENTS/WALTER/research/2026-09-15_resolution-pass/framing-review.md` §2. BRENT receives the same qualified lead for transmission; HAWK for cross-theater synthesis.
''', .40),
signal(5, 'some-european-september-saudi-cargoes-reported-deferred',
       'Reported late-September Saudi cargo cancellations: some European refiners, scope unconfirmed',
       'OIL_ENERGY','IRAN_HORMUZ','BRENT','FALCON,HAWK,HANS,RED,PROME','''
**SECONDARY-SOURCE, INDETERMINATE.** The top two posts in Will's `four poists from twitter.JPG` describe one reported event: some European refiners face cancelled/deferred late-September Saudi term cargoes. Count the posts once. Direct [Argus reporting](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2878080-aramco-defers-cancels-some-european-sep-crude-sources) was inaccessible; the available attributed excerpt is not a primary buyer notification. Reuters' September 14 Asian-refiner uncertainty report is context, not independent verification of these European cancellations.

**BRENT ACTION:** recover direct reporting or buyer notices and establish affected volumes, loading windows and replacement timing; return verified scope or an unresolved-source disposition to WALTER by September 16. Do not turn some late-month cargoes into all September exports, or reported delays into established lost capacity.

FALCON/HAWK receive the same event for theater reconciliation; HANS receives the European supply exposure. Neither a fixed repair duration nor the excerpt's five-days-stock assertion is adopted. Sources and provenance: `AGENTS/WALTER/research/2026-09-15_resolution-pass/framing-review.md` §3.
'''),
signal(6, 'iata-jet-fuel-crack-basis-separated-from-ulsd',
       'IATA September 11 jet-fuel crack report provides a dated physical-price basis',
       'OIL_ENERGY','HYDROCARBON_INFRA','BRENT','HENRY,RED,PROME','''
**PRIMARY-VERIFIED report, dated September 11.** [IATA's chart](https://www.iata.org/en/iata-repository/publications/economic-reports/structural-shifts-increase-jet-fuel-crack-risks/) uses the global jet-fuel price index less Dated Brent, dollars/barrel, sourced to S&P Global Energy Platts/IATA. It describes a higher and more volatile crack environment linked to refinery concentration and import dependence.

**BRENT ACTION:** place this jet-specific physical-price basis alongside the existing products analysis; establish exact observation dates/levels before any latest-price comparison. Return the integration path or a no-change explanation to WALTER; review September 16.

The report does not establish a September 15 close, a matched HO futures crack, or Boundary #6/#8. The screenshot's approximate $70 endpoint is not graded as an exact current observation. HENRY receives the transmission context. No named cruise issuer or bunker-fuel leg is supplied, so the sector-name routing condition is not met. Input is the bottom Hedgeye post in `four poists from twitter.JPG`.
''',.95),
signal(7, 'shanghai-crude-chart-basis-and-arithmetic-unresolved',
       'Shanghai/Brent chart needs synchronized contracts, FX and arithmetic reconciliation',
       'OIL_ENERGY','ASIA_CHINA','ZHAO,BRENT','RED,PROME','''
**UNANCHORED chart basis, INDETERMINATE.** Will's `shanghai crude.jfif` displays Brent 106.36, Shanghai 124.59492 and spread 18.25626. The first two subtract to 18.23492, a 0.02134 mismatch; rounding Brent to two decimals cannot alone reconcile it. Asynchronous legends could explain it but have not been verified.

**ZHAO / BRENT ACTION:** identify exact contracts, quote times, FX convention and units; reconcile the subtraction before using the chart as a regional differential. Return a reproducible same-time calculation or an explicit unverified-chart disposition to WALTER; review September 16.

The exchange's September 11 position-limit notice confirms a rule change only, not the chart's prices. No measured arbitrage, trigger or physical shortage follows from this image. Independent review and source: `AGENTS/WALTER/research/2026-09-15_resolution-pass/framing-review.md` §4. Primary cluster follows the China venue; `HYDROCARBON_INFRA` is the secondary mechanism.
''',.40),
signal(8, 'credit-card-trend-ask-promoted-from-note',
       'Credit-card chart: endpoint corroboration does not verify the claimed 83% trend',
       'CONSUMER_CREDIT','CONSUMER_STAGFLATION','CARL','RED,PROME','''
**ARTIFACT-VERIFIED routing correction; chart trend remains INDETERMINATE.** WALTER's September 14 `credit-card-chart-recirculated` NOTE contains an explicit request despite being recorded INFO. This signal exposes that unresolved ask to the normal BOARD/action path. Search of CARL's current STATUS, processed packets and outbox did not recover a completion; this is SEARCH-NOT-FOUND, not proof no analysis exists.

**CARL ACTION:** verify or reject the chart's claimed 83% rise from 2022 to 2025 using a consistent household/account population and nominal/real basis. A roughly $11,149 endpoint versus a reported $11,153 comparator cannot validate the historical path. Return the source/basis and disposition, or point to existing completed work, to WALTER; review September 16.

No current balance, threshold fire or consumer judgment is asserted. The original NOTE remains unchanged and is catalogued in `AGENTS/WALTER/research/2026-09-15_resolution-pass/legacy-note-rows.json`. The correction here concerns actionable delivery classification, not a finding that the underlying chart is false.
''',.95,'correction',corrects='EXTERNAL: September14 credit-card-chart-recirculated NOTE to CARL',direction='HOLDS uncertainty — promotes the existing hidden ask to ACTION')
]

if __name__ == '__main__':
    now=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    assert now.startswith('2026-09-15'), 'Date changed: reallocate signal IDs before publishing'
    writes={}; delivery=[]; routes=[]; mapping=[]
    for x in ITEMS:
        sid=f'SIG-W-20260915-{x["n"]:03d}'
        assert not list((ROOT/'BOARD').glob(sid+'*')),sid
        path=f'BOARD/{sid}-{x["slug"]}.md'
        lang='confirmed' if x['confidence']>=.90 else 'reports' if x['confidence']>=.75 else 'assessed' if x['confidence']>=.5 else 'unconfirmed'
        h=dict(signal_id=sid,date=now[:10],timestamp=now,time_dispatched=now,source='WALTER',origin='Will-approved resolution pass; source and observation date in body',domain=x['domain'],cluster=x['cluster'],precedence=x['precedence'],action=x['action'],info=x['info'],entities={'BANK_CRE':['Western-Alliance','REG-T-02'] if x['n']==2 else ['CMBS','Citi','Barclays'],'GEOPOL_ENERGY':['YASREF','Yanbu','FIRMS'],'CONSUMER_CREDIT':['WalletHub','Credit-card-debt']}.get(x['domain'],{1:['GASREGW','FRED','Natural-gas'],5:['Saudi-Aramco','Yanbu','Argus'],6:['IATA','Dated-Brent','Jet-fuel'],7:['Shanghai','Brent','INE']}[x['n']] if x['domain']=='OIL_ENERGY' else []),confidence=x['confidence'],confidence_language=lang,signal_type=x['kind'],resources=1,safety_net='clear',word_count=len(x['body'].split()),verdict=x['title'])
        if x['n']==7: h['cluster_secondary']='HYDROCARBON_INFRA'
        if x['corrects']:h.update(corrects=x['corrects'],corrects_direction=x['direction'])
        if x['precedence'] in ('IMMEDIATE','FLASH'):assert h['word_count']<=200
        body=f'# {x["title"]}\n\n{x["body"]}\n'
        def render(header): return '---\n'+''.join(f'{k}: {v if k in {"signal_id","date","timestamp","time_dispatched","source","domain","cluster","cluster_secondary","precedence","confidence_language","signal_type","safety_net"} else json.dumps(v,ensure_ascii=False)}\n' for k,v in header.items())+'---\n\n'+body
        writes[path]=render(h)
        for role in ('action','info'):
            for owner in x[role]:
                if owner in ('TERRY',) or (role=='info' and owner in ('CARL','RED','PROME')):continue
                hp=f'PROME/inbox/2026-09-15_from-WALTER_{sid}.md' if owner=='PROME' else f'AGENTS/{owner}/inbox/WALTER/{sid}.md'
                writes[hp]=render(dict(h,to=f'{owner} ({role.upper()})',board=path))
                delivery.append([now,sid,owner,role.upper(),'CLAUDE_CODE',x['precedence'],hp,'written_not_delivered_pending_push','Approved resolution pass; actual local write time. Origin delivery pending; owner consumption not asserted.'])
        routes.append([now,sid,h['origin'],x['title'],x['precedence'],', '.join(x['action']),', '.join(x['info']),str(x['confidence'])])
        mapping.append(dict(signal_id=sid,path=path,action=x['action'],info=x['info']))
    for p in writes:assert not (ROOT/p).exists(),p
    for p,body in writes.items():
        dest=ROOT/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(body)
    for path,rows in [('AGENTS/WALTER/routed/route_log.tsv',routes),('AGENTS/WALTER/routed/delivery_log.tsv',delivery)]:
        with (ROOT/path).open('a') as f:
            for row in rows:
                assert all('\t' not in c and '\n' not in c for c in row)
                f.write('\t'.join(row)+'\n')
    (HERE/'dispatches.json').write_text(json.dumps(mapping,indent=2)+'\n')
    (HERE/'authored-paths.json').write_text(json.dumps(list(writes),indent=2)+'\n')
    print(f'Published {len(ITEMS)} BOARD signals and {len(delivery)} recipient files at {now}; local write only.')
