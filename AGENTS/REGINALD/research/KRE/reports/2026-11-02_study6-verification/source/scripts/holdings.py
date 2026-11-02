import xml.etree.ElementTree as ET, json, pandas as pd
from load import TK, ROOT
ns={'n':'http://www.sec.gov/edgar/nport'}
CUSIP2T={'060505104':'BAC','46625H100':'JPM','949746101':'WFC','617446448':'MS','38141G104':'GS','857477103':'STT','064058100':'BNY','14040H105':'COF','902973304':'USB','693475105':'PNC','316773100':'FITB','665859104':'NTRS','55261F104':'MTB','172967424':'C','89832Q109':'TFC','446150104':'HBAN','174610105':'CFG','7591EP100':'RF','493267108':'KEY','27579R104':'EWBC','72348N109':'PNFP','320517105':'FHN','989701107':'ZION','957638109':'WAL'}
def nport():
    r=ET.parse(ROOT+'/data/nport_0831.xml').getroot()
    u={};v={}
    for inv in r.findall('.//n:invstOrSec',ns):
        c=inv.find('n:cusip',ns).text
        if c in CUSIP2T:
            u[CUSIP2T[c]]=float(inv.find('n:balance',ns).text); v[CUSIP2T[c]]=float(inv.find('n:valUSD',ns).text)
    na=float(r.find('.//n:fundInfo/n:netAssets',ns).text)
    return pd.Series(u)[TK],pd.Series(v)[TK],na
def invesco():
    d=json.load(open(ROOT+'/data/kbwb_hold_now.json'))
    u={};v={};tot=0
    for h in d['holdings']:
        tot+=h['marketValueBase']
        if h['ticker'] in TK: u[h['ticker']]=float(h['units']); v[h['ticker']]=h['marketValueBase']
    return pd.Series(u)[TK],pd.Series(v)[TK],tot
