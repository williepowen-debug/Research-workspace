#!/usr/bin/env python3
"""One-shot import of Will's CRE loss-sales workbook into the case ledger (Will 2026-09-30: adopt ALL rows, v3).

Source: cases/sources/2026-09-30_will_CRE_Loss_Sales_v3.xlsx (copied from Will's Downloads, unchanged).
Writes (append-only, CREED-owned):
  cases/sources/2026-09-30_will_CRE_Loss_Sales_v3_{events,workouts,methodology}.tsv   verbatim exports (cached values)
  cases/CASES.tsv        one new case per workbook Property ID not already in the ledger
  cases/CASE_EVENTS.tsv  every workbook event row (plus ACQUIRED/APPRAISAL from benchmarks, LOSS_REALIZED from losses)
  cases/CASE_NOTES.md    one section per touched case: every workbook field verbatim + the Loan Workouts record
Mapping rules (stated so a reader can audit them, not inferred per row):
  * Existing cases are ENRICHED, never duplicated (OVERLAP map below, checked by hand 2026-09-30). In CASES.tsv only
    the header vintage changes for them; the workbook's figures go to events + notes. A conflict is DISPUTED, not overwritten.
  * Grain: one case = one loan on one property (README rule 1). CRE-0094 is a component of Pool A (CRE-0080) per
    the workbook's own methodology, so it joins that case. Rows outside case grain (SUMMARY-11, SUMMARY-16 overlapping
    summaries; CRE-0091 Arbor CLO 17, a financing vehicle) are adopted VERBATIM into CASE_NOTES, not as cases.
  * trigger / originator / loan_vintage: UNKNOWN (the workbook does not carry them; not inferred).
  * source_quality: workbook 'Primary ...' -> PRIMARY-CITED (Will's research read it; CREED has not); reporting -> SECONDARY;
    'Unverified lead' / 'Probable duplicate' -> LEAD (README rule 7, tier added in the same commit).
Refuses to run if any CRE- seed id is already present. Run from anywhere: python3 AGENTS/CREED/scripts/import_cre_workbook.py
"""
import csv, datetime, io, os, pathlib, re, sys
import openpyxl

CREED = pathlib.Path(__file__).resolve().parents[1]
C = pathlib.Path(os.environ["CASES_DIR"]) if os.environ.get("CASES_DIR") else CREED / "cases"  # override = dry run on a copy
SRC = CREED / "cases" / "sources" / "2026-09-30_will_CRE_Loss_Sales_v3.xlsx"
TODAY = "2026-09-30"
TAG = "Will workbook v3"
OVERLAP = {  # workbook Property ID -> existing case (hand-checked 2026-09-30)
    "CRE-0007": "CASE-CREED-053", "CRE-0009": "CASE-CREED-052", "CRE-0011": "CASE-CREED-051",
    "CRE-0033": "CASE-CREED-048", "CRE-0063": "CASE-CREED-003", "CRE-0065": "CASE-CREED-001",
    "CRE-0067": "CASE-CREED-054", "CRE-0072": "CASE-CREED-028", "CRE-0085": "CASE-CREED-030",
}
MERGE = {"CRE-0094": "CRE-0080"}            # component of Pool A (workbook methodology)
OUTSIDE = {"SUMMARY-11", "SUMMARY-16", "CRE-0091"}
OWNER_NOTE = {  # README rule 10: other desks own these credits; not checked at import
    "MULTIFAMILY": "HOMER owns multifamily named credits (README rule 10); HOMER's record NOT checked at import -- reconcile, never fork",
    "OZK": "Bank OZK credit: the OZK desk owns it (README rule 10); AGENTS/OZK/ NOT re-checked at import -- reconcile, never fork",
}


def s(v):
    if v is None:
        return ""
    if isinstance(v, datetime.datetime):
        return v.date().isoformat()
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v).replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()


def num(v):
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def usd(m):
    return str(int(round(m * 1_000_000)))


def ptype(t):
    t = (t or "").lower()
    if "multifamily" in t:
        return "MULTIFAMILY"
    if "hotel" in t:
        return "LODGING"
    if "planned life science" in t:
        return "OFFICE"
    if "life science" in t or "lab" in t:
        return "LIFE_SCIENCE" if not t.startswith("office") or "lab" in t else "MIXED_USE"
    if "/" in t and "office" in t and "retail" in t:
        return "MIXED_USE"
    if "mixed use" in t:
        return "MIXED_USE"
    if t.startswith("office"):
        return "OFFICE"
    if t.startswith("retail"):
        return "RETAIL"
    return "UNKNOWN"


def tier(v):
    v = (v or "").lower()
    if v.startswith("primary"):
        return "PRIMARY-CITED"
    if v.startswith(("unverified", "probable duplicate")):
        return "LEAD"
    return "SECONDARY"


TIER_RANK = {"PRIMARY-READ": 0, "PRIMARY-CITED": 1, "SECONDARY": 2, "SEARCH-SUMMARY": 3, "LEAD": 4}

ETYPE = [  # first match wins
    ("cmbs liquidation", "SALE"), ("property sale", "SALE"), ("note sale", "NOTE_SALE"),
    ("deed in lieu", "REO"), ("reo acquisition", "REO"), ("reo marketed", "LISTED"),
    ("foreclosure auction scheduled", "OTHER"), ("foreclosure", "FORECLOSURE"),
    ("charge-off", "LOSS_REALIZED"), ("special servicing", "TRANSFER_SS"),
]


def etype(t):
    t = (t or "").lower()
    for k, v in ETYPE:
        if k in t:
            return v
    return "OTHER"


def status(evt_type, evt_status):
    t, st = (evt_type or "").lower(), (evt_status or "").lower()
    if "special servicing" in t:
        return "SPECIAL_SERVICING"
    if "reo" in t or "deed in lieu" in t:
        return "REO"
    if "foreclosure" in t and "scheduled" not in t:
        return "FORECLOSURE"
    if "sale" in t and ("closed" in st or "reported sale" in st or "liquidat" in st or "completed" in st):
        return "SOLD"
    if "liquidat" in st:
        return "SOLD"
    return "UNKNOWN"


MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def edate(x):
    d = x["Event Date"]
    if isinstance(d, datetime.datetime):
        return d.date().isoformat()
    prec = s(x["Date Precision"]).lower()
    ctx = s(x["Context / Date"])
    if prec.startswith("month"):
        m = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? (20\d\d)", ctx)
        if m:
            return f"{m.group(2)}-{MONTHS[m.group(1)[:3].lower()]:02}"
    y = x["Sale / Status Year"]
    return str(y) if isinstance(y, int) else "UNKNOWN"


def reported(x):
    if isinstance(x["Source Publication Date"], datetime.datetime):
        return x["Source Publication Date"].date().isoformat(), "source publication date per workbook"
    if isinstance(x["Last Source Check"], datetime.datetime):
        return x["Last Source Check"].date().isoformat(), "workbook LAST SOURCE CHECK (not a publication date)"
    return TODAY, "date the workbook reached CREED (publication date UNKNOWN)"


def tsv_rows(path):
    lines = [l for l in path.open(encoding="utf-8") if not l.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def main():
    wb = openpyxl.load_workbook(SRC, data_only=True)
    ev = list(wb["CRE Distress Sales"].iter_rows(values_only=True))
    H = ev[0]
    X = [dict(zip(H, r)) for r in ev[1:] if any(r)]
    lw = list(wb["Loan Workouts"].iter_rows(values_only=True))
    hi = next(i for i, r in enumerate(lw) if r[0] == "Workout ID")
    LH = lw[hi]
    LW = [dict(zip(LH, r)) for r in lw[hi + 1:] if r[0]]
    meth = [r for r in wb["Methodology & Notes"].iter_rows(values_only=True) if any(r)]

    cases = tsv_rows(C / "CASES.tsv")
    have = " ".join(c["seed_id"] for c in cases)
    if re.search(r"\bCRE-\d{4}\b", have):
        sys.exit("REFUSED: CRE- seed ids already in CASES.tsv -- this import has run. Nothing written.")
    if any(f"{TAG}" in l for l in (C / "CASE_EVENTS.tsv").open(encoding="utf-8")):
        sys.exit("REFUSED: workbook events already in CASE_EVENTS.tsv. Nothing written.")

    # verbatim exports
    for name, header, rows in (("events", H, [r for r in ev[1:] if any(r)]), ("workouts", LH, lw[hi + 1:]),
                               ("methodology", ("Item", "Note"), meth)):
        out = io.StringIO()
        w = csv.writer(out, delimiter="\t", lineterminator="\n")
        out.write(f"# VERBATIM export (cached cell values) of sheet from {SRC.name}, Will's research, received 2026-09-30. Not edited.\n")
        w.writerow(header)
        for r in rows:
            if any(c is not None for c in r):
                w.writerow([s(c) for c in r])
        (C / "sources" / f"{SRC.stem}_{name}.tsv").write_text(out.getvalue(), encoding="utf-8")

    by_pid = {}
    for x in X:
        pid = MERGE.get(s(x["Property ID"]), s(x["Property ID"]))
        by_pid.setdefault(pid, []).append(x)
    lw_by_pid = {}
    for r in LW:
        for pid in re.split(r";\s*", s(r["Property / Collateral IDs"])):
            lw_by_pid.setdefault(MERGE.get(pid, pid), []).append(r)

    n = max(int(c["case_id"].split("-")[-1]) for c in cases)
    case_fields = list(cases[0].keys())
    new_cases, new_events, notes = [], [], []
    outside_notes = []
    for pid, rows in by_pid.items():
        if pid in OUTSIDE:
            outside_notes.append((pid, rows, lw_by_pid.get(pid, [])))
            continue
        main_rows = [x for x in rows if "duplicate" not in s(x["Event Type"]).lower()] or rows
        lead = main_rows[0]
        if pid in OVERLAP:
            cid = OVERLAP[pid]
        else:
            n += 1
            cid = f"CASE-CREED-{n:03}"
        tiers = [tier(s(x["Verification Status"])) for x in rows]
        best = min(tiers, key=lambda t: TIER_RANK[t])
        # events
        for x in rows:
            rep, rep_basis = reported(x)
            t = tier(s(x["Verification Status"]))
            src = s(x["Source URL 1"]) or f"{TAG} {s(x['Event ID'])} (no source URL; {s(x['Source Account(s)']) or 'source account not stated'})"
            dup = "duplicate" in s(x["Event Type"]).lower()
            amt = num(x["Disposition Amount ($M)"])
            detail = (f"[{TAG} {s(x['Event ID'])}] {s(x['Event Type'])} -- {s(x['Event Status'])}"
                      + (f"; include-in-sale-analysis={s(x['Include in Sale Analysis'])}" if s(x['Include in Sale Analysis']) else "")
                      + (f"; asking/proposed ${s(x['Proposed / Asking Amount ($M)'])}M (NOT a completed price)" if num(x["Proposed / Asking Amount ($M)"]) else "")
                      + (f"; context: {s(x['Context / Date'])}" if s(x["Context / Date"]) else "")
                      + ("; PROBABLE DUPLICATE per workbook -- not a separate event" if dup else ""))
            disp = ""
            if cid == "CASE-CREED-001" and num(x["Realized Credit Loss ($M)"]):
                disp = "Workbook $64.8M aggregate trust loss (CRE News 2026-09-25) vs CREED $68.6M gross ($80M senior - $11.4M net, KB-CREED-046); UNRECONCILED until a remittance report is read"
            et = "OTHER" if dup else etype(s(x["Event Type"]))
            loss = num(x["Realized Credit Loss ($M)"])
            if et == "LOSS_REALIZED" and loss:  # the event IS the loss: carry the loss value here, no second row
                new_events.append([cid, edate(x), et, detail + f"; realized credit loss ${s(loss)}M; {s(x['Credit Loss Status'])}",
                                   usd(loss), "reported realized credit loss per workbook", rep, src, t,
                                   "DISPUTED" if disp else "UNCONTESTED", disp, rep_basis])
            else:
                new_events.append([cid, edate(x), et, detail,
                                   usd(amt) if amt and s(x["Currency"]) == "USD" else "UNKNOWN",
                                   s(x["Disposition Amount Type"]) or "UNKNOWN", rep, src, t,
                                   "UNCONTESTED", "", rep_basis])
            b, by, bt = num(x["Benchmark Amount ($M)"]), x["Benchmark Year"], s(x["Benchmark Type"])
            if b and not dup and s(x["Currency"]) == "USD":
                kind = "APPRAISAL" if ("apprais" in bt.lower() or "valuation" in bt.lower()) else "ACQUIRED"
                new_events.append([cid, str(by) if isinstance(by, int) else "UNKNOWN", kind,
                                   f"[{TAG} {s(x['Event ID'])} benchmark] {bt}" + (" -- benchmark UNVERIFIED per workbook" if "unverified" in bt.lower() else ""),
                                   usd(b), bt, rep, src, t, "UNCONTESTED", "", rep_basis])
            if loss and et != "LOSS_REALIZED":
                new_events.append([cid, edate(x), "LOSS_REALIZED",
                                   f"[{TAG} {s(x['Event ID'])}] realized credit loss ${s(loss)}M on loan ${s(x['Loan Balance ($M)'])}M; {s(x['Credit Loss Status'])}"
                                   + (f"; net principal recovery ${s(x['Net Principal Recovery ($M)'])}M" if num(x["Net Principal Recovery ($M)"]) else ""),
                                   usd(loss), "reported realized credit loss (whole loan per workbook)", rep, src, t,
                                   "DISPUTED" if disp else "UNCONTESTED", disp, rep_basis])
        # case row (new cases only)
        if pid not in OVERLAP:
            loan = next((num(x["Loan Balance ($M)"]) for x in rows if num(x["Loan Balance ($M)"])), None)
            loss = next((num(x["Realized Credit Loss ($M)"]) for x in rows if num(x["Realized Credit Loss ($M)"])), None)
            holder = "; ".join(dict.fromkeys(v for x in rows for v in (s(x["Debt Holder / Lender"]), s(x["CMBS Deal ID"])) if v))
            fin = " ".join(s(x["Financing Type"]) for x in rows).lower()
            htype = ("CMBS_SASB" if "sasb" in fin else "CRE_CLO" if "clo" in fin else
                     "BANK" if ("bank" in fin or "ozk" in holder.lower()) else "UNKNOWN")
            last = rows[-1]
            pt = ptype(s(lead["Property Type"]))
            loc = s(lead["Location"])
            m = re.match(r"(.*?)\s+([A-Z]{2})$", loc)
            city, state = (m.group(1), m.group(2)) if m else (loc or "UNKNOWN", "UNKNOWN")
            owner = OWNER_NOTE["OZK"] if "ozk" in (holder + s(lead["Property Name / Address"])).lower() else (
                OWNER_NOTE["MULTIFAMILY"] if pt == "MULTIFAMILY" else "UNKNOWN")
            st = status(s(last["Event Type"]), s(last["Event Status"]))
            row = {k: "UNKNOWN" for k in case_fields}
            row.update({
                "case_id": cid, "first_logged": TODAY, "property_name": s(lead["Property Name / Address"]),
                "address": s(lead["Property Name / Address"]), "city": city, "state": state, "property_type": pt,
                "vintage_year": "UNKNOWN (raw: " + (s(lead["Year Built / Key Notes"]) or "not stated") + ")",
                "size": s(lead["Size (SF)"]) or "UNKNOWN",
                "tenant_or_occupancy_note": s(lead["Occupancy at Event"]) or "UNKNOWN",
                "loan_amount_usd": (f"${s(loan)}M (workbook; read its basis in CASE_NOTES)" if loan else "UNKNOWN"),
                "holder_type": htype, "holder": holder or "UNKNOWN",
                "latest_status": st,
                "status_as_of": (edate(last) + f" ({s(last['Event Status'])})") if st != "UNKNOWN" else f"UNKNOWN ({s(last['Event Status'])})",
                "value_marks": "-> CASE_NOTES (read the basis there before using any mark)",
                "implied_loss_pct": (f"{round(loss / loan * 100)}% = reported realized loss / loan balance, per workbook ({s(rows[0]['Credit Loss Status'])})"
                                     if loss and loan else "UNKNOWN (a price discount vs a benchmark is NOT a loan loss)"),
                "trigger_eligibility": f"NOT ASSESSED at adoption ({TODAY})",
                "fleet_links": owner, "kb_ref": "none", "sources": "-> CASE_NOTES (workbook source URLs)",
                "source_quality": best,
                "notes": f"adopted from {TAG} Property ID {pid} (Will's research, received {TODAY}; Will: adopt all rows); full record CASE_NOTES.md § {cid}",
                "seed_id": pid if pid not in MERGE.values() else f"{pid}; CRE-0094 (component, merged per workbook)",
                "verification": f"NOT re-verified by CREED. Workbook verification: " + " | ".join(dict.fromkeys(s(x['Verification Status']) for x in rows)),
            })
            new_cases.append(row)
        # notes
        lines = [f"### {cid} — {s(lead['Property Name / Address'])} ({TAG} {pid})" if pid not in OVERLAP else
                 f"### {cid} — {TAG} {pid} enrichment ({s(lead['Property Name / Address'])})",
                 f"**Imported {TODAY} from `cases/sources/{SRC.name}` (Will's research). Fields verbatim; CREED has NOT re-verified them.**"
                 + (" This case already existed: the workbook's figures were added as events and here, and NO existing CASES.tsv cell was changed." if pid in OVERLAP else "")]
        if pid == "CRE-0072":
            lines.append("⚠️ The workbook treats Chapter Buildings I+II as ONE property (CRE-0072); the ledger splits them (028/029). Events attached to 028 ONLY; see the pointer under 029. Do not double-count.")
        if cid == "CASE-CREED-001":
            lines.append("⚠️ UNRECONCILED: workbook $64.8M aggregate trust loss (CRE News 2026-09-25) vs CREED $68.6M gross ($80M senior − $11.4M net, KB-CREED-046). Read a remittance report before citing either.")
        for x in rows:
            lines.append(f"- **{s(x['Event ID'])}:** " + " · ".join(f"*{k}:* {s(x[k])}" for k in H if s(x[k]) and k not in ("Discount to Benchmark (%)", "Discount to Alternative (%)"))
                         + (f" · *Discount to Benchmark (cached formula):* {round(x['Discount to Benchmark (%)'] * 100, 1)}% (price vs benchmark, NOT a loan loss)" if num(x["Discount to Benchmark (%)"]) is not None else ""))
        for r in lw_by_pid.get(pid, []):
            lines.append(f"- **Loan Workouts {s(r['Workout ID'])}:** " + " · ".join(f"*{k}:* {s(r[k])}" for k in LH if s(r[k])))
        notes.append("\n".join(lines))

    # outside-grain rows
    og = ["### Rows adopted OUTSIDE case grain (Will workbook v3) — verbatim, NOT cases",
          "README rule 1 defines a case as one loan on one property. These rows are adopted as records (Will: adopt all rows) but not as cases, so they never enter a case count."]
    for pid, rows, lws in outside_notes:
        why = "financing vehicle (CLO redemption / repo transfer), not a property loan; lender-capital evidence (S8b, LIQUID's lane)" if pid == "CRE-0091" else "overlapping summary row; the workbook excludes it from analysis"
        og.append(f"- **{pid}** ({why}):")
        for x in rows:
            og.append("  - " + " · ".join(f"*{k}:* {s(x[k])}" for k in H if s(x[k])))
        for r in lws:
            og.append(f"  - *Loan Workouts {s(r['Workout ID'])}:* " + " · ".join(f"*{k}:* {s(r[k])}" for k in LH if s(r[k])))

    # write CASES
    with (C / "CASES.tsv").open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        for r in new_cases:
            w.writerow([r[k] for k in case_fields])
    with (C / "CASE_EVENTS.tsv").open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        for r in new_events:
            w.writerow(r)
    with (C / "CASE_NOTES.md").open("a", encoding="utf-8") as f:
        f.write(f"\n\n## {TAG} import ({TODAY}) — Will's research, adopted whole (Will: \"adopt all the rows\")\n\n"
                f"Source `cases/sources/{SRC.name}`; verbatim TSV exports beside it. Methodology sheet: `..._methodology.tsv` "
                "(its limits apply: a selected event collection, not a market sample; discounts are price-vs-benchmark, not losses; "
                "benchmark types must not be pooled). Mapping rules: header of `scripts/import_cre_workbook.py`.\n\n"
                + "\n\n".join(notes) + "\n\n" + "\n".join(og)
                + "\n\n### CASE-CREED-029 — pointer\nThe workbook's Chapter Buildings record (CRE-0072) covers I+II as one property and is attached to CASE-CREED-028 only. Read it there; do not add it to 029.\n")
    print(f"new cases {len(new_cases)} (CASE-CREED-{n - len(new_cases) + 1:03}..{n:03}); enriched {len(OVERLAP)}; "
          f"events {len(new_events)}; outside-grain ids {len(outside_notes)}; workbook rows {len(X)}; workouts {len(LW)}")


if __name__ == "__main__":
    main()
