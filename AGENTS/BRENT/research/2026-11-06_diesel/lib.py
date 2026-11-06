import xlrd,datetime as dt
from pathlib import Path
D=Path(__file__).resolve().parent/'data'  # EIA hist_xls files, not committed; re-download from eia.gov/dnav/pet/hist_xls/<name>.xls
def load(n,sheet=1,col=1):
    b=xlrd.open_workbook(D/f'{n}.xls');s=b.sheet_by_index(sheet);o={}
    for r in range(3,s.nrows):
        v=s.cell_value(r,col)
        if v=='' or s.cell_value(r,0)=='' : continue
        o[xlrd.xldate.xldate_as_datetime(s.cell_value(r,0),b.datemode).date()]=float(v)
    return o
