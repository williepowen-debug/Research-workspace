import re,sys,html,urllib.request,urllib.parse,http.cookiejar,hashlib,os
U="https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx"; out=sys.argv[1]; want=sys.argv[2:]
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[("User-Agent","research-bot/1.0")]
def hid(t): return {m[0]:html.unescape(m[1]) for m in re.findall(r'<input type="hidden" name="([^"]+)"[^>]*? value="([^"]*)"',t)}
def post(t,extra):
    d=hid(t); d.update(extra); r=op.open(urllib.request.Request(U,urllib.parse.urlencode(d).encode()),timeout=300); return r
t=op.open(U,timeout=60).read().decode()
P="ctl00$MainContentHolder$"
t=post(t,{"__EVENTTARGET":P+"ListBox1","__EVENTARGUMENT":"",P+"ListBox1":"ReportingSeriesSinglePeriod",P+"FormatType":"TSVRadioButton"}).read().decode()
opts=re.findall(r'<option[^>]*value="(\d+)"[^>]*>(\d\d/\d\d/\d{4})',t); print(opts[:6])
m=dict((b,a) for a,b in opts); print(re.findall(r'Updated[^<]{0,40}<?[^>]*>?[^<]{0,40}',t)[:2])
for w in want:
    r=post(t,{"__EVENTTARGET":"","__EVENTARGUMENT":"",P+"ListBox1":"ReportingSeriesSinglePeriod",P+"DatesDropDownList":m[w],P+"FormatType":"TSVRadioButton",P+"TabStrip1$Download_0":"Download"})
    b=r.read(); d=os.path.join(out,w.replace("/","")); os.makedirs(d,exist_ok=True)
    open(d+".zip","wb").write(b); print(w,r.headers.get("Content-Disposition"),len(b),hashlib.sha256(b).hexdigest())
