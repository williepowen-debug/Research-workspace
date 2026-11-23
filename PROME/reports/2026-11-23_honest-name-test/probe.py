#!/usr/bin/env python3
"""WQ-735 condition (Will 2026-11-23): each distinct source ONCE under the honest name.
One request per host, client string research-bot/1.0, no retry, no second identity.
Keys come from FORGE/tools/market-data/.env and are never written to the output."""
import subprocess, pathlib, datetime, time, re
ROOT = pathlib.Path(__file__).resolve().parents[3]
UA = "research-bot/1.0"
env = {}
p = ROOT / "FORGE/tools/market-data/.env"
if p.exists():
    for l in p.read_text().splitlines():
        if "=" in l:
            k, v = l.split("=", 1); env[k.strip()] = v.strip()
ms = lambda y: int(datetime.datetime(y, 1, 1).timestamp() * 1000)
now_ms = int(time.time() * 1000)
S = [  # host, desks, url, extra headers, note
 ("agsi.gie.eu","BRENT,DEWEY,HANS","https://agsi.gie.eu/api?type=EU&size=1",["x-key: "+env.get("AGSI_API_KEY","")],"with the desk's key"),
 ("alsi.gie.eu","DEWEY","https://alsi.gie.eu/api?type=EU&size=1",["x-key: "+env.get("AGSI_API_KEY","")],"with the desk's key"),
 ("api.hkma.gov.hk","ZHAO","https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-interbank-liquidity?pagesize=5&sortby=end_of_date&sortorder=desc",[],""),
 ("api.nasdaq.com","REGINALD","https://api.nasdaq.com/api/quote/KRE/historical?assetclass=etf&fromdate=2026-10-23&todate=2026-11-23&limit=60",["Accept: application/json"],""),
 ("api.stlouisfed.org","BRENT,CARL","https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&limit=1&sort_order=desc&file_type=json&api_key="+env.get("FRED_API_KEY",""),[],"with the fleet key"),
 ("cdn.cboe.com","HENRY,RED,VIOLET","https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv",[],""),
 ("cdn.finra.org","REGINALD","https://cdn.finra.org/equity/regsho/daily/CNMSshvol20261120.txt",[],""),
 ("chartexchange.com","REGINALD","https://chartexchange.com/symbol/nyse-kre/stats/",[],""),
 ("data-api.ecb.europa.eu","HANS","https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y?lastNObservations=1&format=csvdata",[],""),
 ("data.texas.gov","LABOR","https://data.texas.gov/resource/8w53-c4f6.json",[],""),
 ("data.wa.gov","DEWEY","https://data.wa.gov/resource/sb4j-ca4h.json",[],""),
 ("dos.fl.gov","MARCO","https://dos.fl.gov/elections/data-statistics/",[],""),
 ("feeds.bbci.co.uk","HAWK","http://feeds.bbci.co.uk/news/world/rss.xml",[],""),
 ("feeds.reuters.com","HAWK","http://feeds.reuters.com/reuters/businessnews",[],""),
 ("fred.stlouisfed.org","BRENT,ZHAO","https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXCHUS&cosd=2026-11-01",[],""),
 ("gasprices.aaa.com","CARL","https://gasprices.aaa.com/",[],""),
 ("home.treasury.gov","SAM","https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv",[],""),
 ("iq.usembassy.gov","FALCON","https://iq.usembassy.gov/category/alert/feed/",[],""),
 ("markets.newyorkfed.org","LIQUID","https://markets.newyorkfed.org/api/pd/get/PDPOSCSBND-G10.json",[],""),
 ("news.google.com","HAWK,WALTER","https://news.google.com/rss/search?q=Iran+sanctions&hl=en-US&gl=US&ceid=US:en",[],""),
 ("oag.ca.gov","DEWEY","https://oag.ca.gov/privacy/databreach/list",[],""),
 ("pddata.dtcc.com","LIQUID","https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_2026_11_20.zip",[],""),
 ("rigcount.bakerhughes.com","BRENT","https://rigcount.bakerhughes.com/na-rig-count",[],"listing page; the data file sits behind it"),
 ("securitiesfilings.fdicconnect.fdic.gov","OZK,REGINALD","https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/cert/110",[],""),
 ("services.nvd.nist.gov","DEWEY","https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=1",[],""),
 ("services9.arcgis.com","FALCON","https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/?f=json",[],""),
 ("stats.bis.org","SAM","https://stats.bis.org/api/v1/data/WS_GLI/all/all?lastNObservations=1&format=csv",[],""),
 ("transtats.bts.gov","MARCO","https://transtats.bts.gov/Data_Elements.aspx?Data=1",[],""),
 ("trends.google.com","MARCO","https://trends.google.com/trends/",[],"the script's first (cookie) request"),
 ("web.archive.org","MARCO","https://web.archive.org/cdx/search/cdx?url=www.dol.gov/agencies/eta/foreign-labor/performance&output=json&filter=statuscode:200&limit=-1",[],""),
 ("www.aljazeera.com","HAWK","https://www.aljazeera.com/xml/rss/all.xml",[],""),
 ("www.atg.wa.gov","DEWEY","https://www.atg.wa.gov/data-breach-notifications",[],""),
 ("www.bankofengland.co.uk","HANS","https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Nov/2026&Dateto=23/Nov/2026&SeriesCodes=IUDSOIA&CSVF=TN&UsingCodes=Y",[],""),
 ("www.banxico.org.mx","MARCO",f"https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CE81&sector=1&locale=es&fechaInicio={ms(2025)}&fechaFin={now_ms}&formatoXLS.x=1",[],""),
 ("www.cboe.com","FORGE,VIOLET","https://www.cboe.com/us/futures/market_statistics/settlement/csv/?dt=2026-11-20",["Referer: https://www.cboe.com/"],""),
 ("www.cftc.gov","BRENT,LIQUID,SAM,VIOLET","https://www.cftc.gov/dea/newcot/deafut.txt",[],""),
 ("www.chinamoney.com.cn","ZHAO","https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/CcprHisNew?",[],""),
 ("www.cisa.gov","DEWEY","https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json",[],""),
 ("www.customs.go.jp","SAM","https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv",[],""),
 ("www.dol.gov","MARCO","https://www.dol.gov/agencies/eta/foreign-labor/performance",[],""),
 ("www.eia.gov","BRENT","https://www.eia.gov/dnav/pet/xls/PET_PRI_GND_DCUS_NUS_W.xls",[],""),
 ("www.gpif.go.jp","SAM","https://www.gpif.go.jp/en/performance/latest-results.html",[],""),
 ("www.investing.com","VIOLET","https://www.investing.com/indices/ice-bofaml-move-historical-data",[],""),
 ("www.ishares.com","DEWEY","https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf/latest-holdings.csv",[],""),
 ("www.mof.go.jp","SAM","https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv",[],""),
 ("www.newyorkfed.org","DEWEY","https://www.newyorkfed.org/microeconomics/hhdc",[],""),
 ("www.pbc.gov.cn","ZHAO","https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html",[],""),
 ("www.ssga.com","DEWEY,VULCAN","https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-jnk.xlsx",[],""),
 ("www.totan.com","SAM","https://www.totan.com/archives/15647",[],""),
 ("www.trendforce.com","VULCAN","https://www.trendforce.com/price/dram/dram_spot",[],""),
 ("www.trepp.com","CREED","https://www.trepp.com/trepptalk/",[],""),
 ("www.twc.texas.gov","LABOR","https://www.twc.texas.gov/sites/default/files/oei/docs/warn-act-listings-2026-twc.xlsx",[],""),
 ("query1.finance.yahoo.com","FORGE price tool (all desks)","https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?range=5d&interval=1d",[],"one chart call; the tool's full call set is tested separately"),
]
MARK = re.compile(rb"access denied|captcha|cf-chl|just a moment|are you a robot|request blocked|forbidden|unusual traffic|pardon our interruption", re.I)
out = ["host\tdesks\tverdict\thttp_code\tbytes\tmarker\tnote\tstamp_et"]
for host, desks, url, hdrs, note in S:
    tmp = "/tmp/claude-1000/_hn_body"
    cmd = ["curl","-s","-L","-A",UA,"--max-time","30","-o",tmp,"-w","%{http_code}"]
    for h in hdrs: cmd += ["-H", h]
    cmd.append(url)
    try:
        code = subprocess.run(cmd, capture_output=True, text=True, timeout=45).stdout.strip() or "000"
    except Exception:
        code = "000"
    try: body = pathlib.Path(tmp).read_bytes()
    except Exception: body = b""
    m = MARK.search(body[:200000]) if len(body) < 400000 else None
    mk = m.group(0).decode() if m else ""
    if code in ("401","403","429") or (mk and len(body) < 5000): v = "REFUSED"
    elif code == "200" and len(body) > 200: v = "WORKS"
    else: v = "UNCLEAR"
    stamp = subprocess.run(["date","+%H:%M:%S"],capture_output=True,text=True).stdout.strip()
    out.append("\t".join([host,desks,v,code,str(len(body)),mk,note,stamp]))
    pathlib.Path(tmp).unlink(missing_ok=True)
pathlib.Path(__file__).with_name("probe.tsv").write_text("\n".join(out)+"\n")
print("\n".join(out))
