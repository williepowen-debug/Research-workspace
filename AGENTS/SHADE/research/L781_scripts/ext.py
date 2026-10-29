import sys, pdfplumber
pdf, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
with pdfplumber.open(pdf) as p:
    print("pages", len(p.pages), file=sys.stderr)
    with open(out, "w") as f:
        for i in range(a-1, b):
            t = p.pages[i].extract_text(layout=True) or ""
            f.write(f"\n=====PAGE {i+1}=====\n{t}")
