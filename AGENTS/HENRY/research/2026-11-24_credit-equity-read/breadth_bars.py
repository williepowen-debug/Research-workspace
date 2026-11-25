import yfinance as yf, pandas as pd, sys
t="^GSPC SPY RSP QQQ ^NDX SMH SOXX NVDA AMD AVGO MSFT AAPL GOOGL IWM ^RUT DIA XLY XLP XLI XLU XLF XLE XLV XLK KRE HYG JNK LQD ^VIX ^VIX9D ^VIX3M ^VVIX IWD IWF TLT".split()
d=yf.download(t,start="2026-10-01",end="2026-11-26",auto_adjust=False,progress=False,group_by="ticker",threads=True)
cl=pd.DataFrame({x:d[x]["Close"] for x in t})
cl.to_csv(sys.argv[1])
print(cl.index[-6:].tolist())
pd.set_option("display.width",250); pd.set_option("display.max_columns",50)
r=cl.pct_change()*100
print("CLOSES last 7"); print(cl.tail(7).T.round(2))
print("PCT last 6"); print(r.tail(6).T.round(2))
