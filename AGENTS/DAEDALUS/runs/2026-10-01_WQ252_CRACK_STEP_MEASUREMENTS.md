# WQ-252 / L471 — crack contract-month step measurements (DAEDALUS, 2026-10-01)

**Instrument:** yfinance 1.2.0 named NYMEX contracts (`HO<m>.NYM`, `CL<m>.NYM`), `history(auto_adjust=False)` daily `Close`. Pulled 2026-10-01 ~12:16 ET. The script is reproduced below.
**Basis caveat ⚠️:** single vendor. The daily `Close` on these rows is the vendor's finalized row, which HENRY's 9/24 report INFERRED tracks CME settlement to ≤$0.10 (n=3). This record has **NOT checked it against CME**, which blocks this box. The live row is intraday, not a settlement. Crack = HO × 42 − CL, $/bbl, matched delivery months.

## Expiries (vendor `expireDate`, UTC date)
| Contract | Expires | | Contract | Expires |
|---|---|---|---|---|
| CLX26 | 2026-10-20 | | HOX26 | 2026-10-30 |
| CLZ26 | 2026-11-20 | | HOZ26 | 2026-11-30 |
| CLF27 | 2026-12-21 | | HOF27 | 2026-12-31 |
| HOV26 | 2026-09-30 | | (CLV26 and earlier: no longer served) | |

⚠️ **The CL leg expires ~10 days before the HO leg of the same month.** A matched November pair cannot be graded after the CLX26 last trade (10/20). That bounds every "keep November" option.

## Matched cracks by delivery month, September 2026 (daily Close)
               Nov     Dec     Jan    Cont  NovDec  DecJan
2026-09-01  101.48   95.99   92.51  106.23    5.49    3.47
2026-09-02  100.51   95.18   91.92  105.64    5.34    3.26
2026-09-03   97.82   93.29   90.38  101.63    4.53    2.90
2026-09-04   95.55   91.32   88.62   99.21    4.22    2.70
2026-09-08   95.43   91.47   89.03   98.82    3.96    2.44
2026-09-09  101.37   96.93   94.24  105.59    4.43    2.69
2026-09-10  105.13  100.41   98.09  109.93    4.72    2.32
2026-09-11  104.33  100.02   98.01  108.24    4.31    2.01
2026-09-14  102.58   98.08   96.17  106.99    4.50    1.91
2026-09-15  109.67  103.37  100.53  115.17    6.30    2.84
2026-09-16  112.50  105.26  101.27  117.92    7.24    3.99
2026-09-17  108.11  101.69   98.08  112.87    6.42    3.61
2026-09-18  107.38  100.63   96.92  112.13    6.76    3.70
2026-09-21  105.34   99.21   95.96  109.58    6.13    3.26
2026-09-22  109.49  103.07   99.13  112.98    6.41    3.94
2026-09-23  102.45  100.21   98.79  108.45    2.24    1.41
2026-09-24   95.57   94.73   94.75  104.06    0.84   -0.02
2026-09-25   95.00   95.02   94.65  104.35   -0.03    0.37
2026-09-28   96.20   94.45   93.61  107.12    1.75    0.84
2026-09-29  100.04   94.71   91.79  116.33    5.33    2.92
2026-09-30  106.48  100.87   97.24  117.77    5.61    3.62
       NovDec  DecJan
count   21.00   21.00
mean     4.60    2.58
std      1.95    1.14
min     -0.03   -0.02
25%      4.22    2.01
50%      4.72    2.84
75%      6.13    3.47
max      7.24    3.99
Nov Dec 95 straddle sessions: 7 of 21 ['2026-09-03', '2026-09-04', '2026-09-08', '2026-09-24', '2026-09-25', '2026-09-28', '2026-09-29']
Nov Dec 90.16 straddle sessions: 0 of 21 []
Dec Jan 95 straddle sessions: 4 of 21 ['2026-09-01', '2026-09-02', '2026-09-09', '2026-09-25']
Dec Jan 90.16 straddle sessions: 2 of 21 ['2026-09-04', '2026-09-08']

## Live, 2026-10-01 12:17 ET (intraday last trade, NOT settlement)
| Pair | HO $/gal | CL $/bbl | Crack $/bbl | vs $95 | vs $90.16 |
|---|---:|---:|---:|---:|---:|
| Nov (HOX26×42 − CLX26) | 4.6328 | 92.20 | **102.38** | +7.38 | +12.22 |
| Dec (HOZ26×42 − CLZ26) | 4.4819 | 90.22 | **98.02** | +3.02 | +7.86 |
| Jan (HOF27×42 − CLF27) | 4.3773 | 88.24 | **95.61** | +0.61 | +5.45 |

## Calibration-day check (the $90.16 line, 2026-07-23 close)
| Series | 7/23 close |
|---|---:|
| `HO=F × 42 − CL=F` (continuous, the registration instrument) | **90.16** (reproduces the line exactly: HO=F 4.3416, CL=F 92.19) |
| Nov matched (HOX26×42 − CLX26) | 81.41 |
| Dec matched | 76.31 |
| Jan matched | 73.07 |

⚠️ **INFERRED, not VERIFIED:** under the standard NYMEX calendar, the August CL contract stopped trading ~7/21 and August HO ~7/31. On 7/23, then, `HO=F` was most likely August heating oil and `CL=F` was September crude, which is a **mismatched** pair. HENRY's 9/14 correction says the series was "calendar-matched at every observation F1 was calibrated on". This record cannot confirm which contracts the vendor's continuous series held on 7/23, because the expired contracts are no longer served. The question goes to HENRY by packet. Either way, the line was set on the FRONT of the curve, about **$8.75 above where the November pair stood the same day**.

## Script
```python
import yfinance as yf, pandas as pd
syms={"HOX26":"HOX26.NYM","HOZ26":"HOZ26.NYM","HOF27":"HOF27.NYM","CLX26":"CLX26.NYM","CLZ26":"CLZ26.NYM","CLF27":"CLF27.NYM","HOc":"HO=F","CLc":"CL=F"}
d={}
for k,s in syms.items():
    h=yf.Ticker(s).history(start="2026-09-01",end="2026-10-01",auto_adjust=False)
    d[k]=h["Close"]
df=pd.DataFrame(d); df.index=df.index.date
df["Nov"]=df.HOX26*42-df.CLX26; df["Dec"]=df.HOZ26*42-df.CLZ26; df["Jan"]=df.HOF27*42-df.CLF27
df["Cont"]=df.HOc*42-df.CLc
df["NovDec"]=df.Nov-df.Dec; df["DecJan"]=df.Dec-df.Jan
pd.set_option("display.width",200)
print(df[["Nov","Dec","Jan","Cont","NovDec","DecJan"]].round(2).to_string())
print(df[["NovDec","DecJan"]].describe().round(2).to_string())
for k in ["HOX26","HOZ26","CLX26","CLZ26","HOF27","CLF27"]:
    i=yf.Ticker(syms[k]).info; print(k,i.get("expireDate"))
for a,b in [("Nov","Dec"),("Dec","Jan")]:
    for L in (95,90.16):
        st=df[((df[a]<L)!=(df[b]<L))]
        print(a,b,L,"straddle sessions:",len(st),"of",len(df),[str(x) for x in st.index])
```
