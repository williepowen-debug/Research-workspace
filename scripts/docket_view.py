#!/usr/bin/env python3
"""docket_view — generated forward-catalyst view of PROME/DOCKET.tsv + drift check for prose views.

WHY (PROME commission 2026-08-16, Will-directed; built 2026-09-03 under Will's 9/2 window).
DOCKET.tsv is the canonical forward-catalyst ledger. It had two HAND-MAINTAINED prose
renderings (the SCRATCH "Live-catalyst calendar" line, HEARTBEAT's Near Gates table) and
hand-copied views of a canonical TSV drift: spine audits #7 (8/3) and #9 (8/16) were both
BLOCKED on exactly that class — a check-date promoted to an event date ("Colorado ROD
[8/25]" on both surfaces vs DOCKET's 8/30 earliest-legal date), a modal date that had
moved. A generated view kills the class; computed weekday names kill the weekday-label
class for these surfaces as a side effect.

TWO MODES
  --write        render the forward view INTO the marked block of a prose file (SCRATCH):
                   <!-- DOCKET-VIEW BEGIN --> … <!-- DOCKET-VIEW END -->
                 touches nothing outside the markers; missing/duplicated markers = rc 2,
                 no write; ragged DOCKET = rc 2, no write; write = .tmp + os.replace.
  --check FILE…  extract dated claims from any prose view, match them to DOCKET rows by
                 anchor-token overlap, flag a claim whose date NO matching row covers.
                 NEVER writes. rc 0 clean · 1 divergence(s) (advisory) · 2 error.
  --selftest     guard drills on temp fixtures (test-the-guard canon): ragged ⇒ rc 2;
                 missing marker ⇒ rc 2 + no write; duplicate marker ⇒ rc 2; past-due
                 PENDING ⇒ above the window; idempotence ⇒ zero diff; check-mode
                 positive control (Colorado ROD [8/25] flags) + negative control ([8/30]
                 clean). rc 0 all behaved · 1 a drill failed (do NOT trust the tool).

DESIGN CONSTRAINTS (commission §3 — each a paid-for lesson)
  1. DOCKET is the ONLY input to the render. The existing view is never parsed as input.
  2. The selection filter never gates the safety net: PENDING rows whose date has passed
     surface ABOVE the forward window (OVERDUE), and everything not rendered is COUNTED
     (undated rows · rows beyond the window · non-PENDING rows) — no silent caps.
  3. Field-count the whole DOCKET on read: 6 fields per data row; comment lines (#) and
     the header row are the only legal short lines. Anything else = rc 2, no write.
  4. Marker-anchored edits only. 5. Editorial layer (★, "Read") stays OUTSIDE the markers:
     the line after END is the hand-annotation line and is never touched.
  6. Idempotent: same DOCKET + same --as-of ⇒ byte-identical block (the stamp is
     content-derived: crc32 of the parsed live rows, not a clock).  7. No network.

USAGE
  python3 scripts/docket_view.py --write PROME/SCRATCH.md            # PROME closeout
  python3 scripts/docket_view.py --write PROME/SCRATCH.md --dry-run  # print block only
  python3 scripts/docket_view.py --check PROME/SCRATCH.md HEARTBEAT.md
  python3 scripts/docket_view.py --check FILE --docket <snapshot.tsv> --as-of 2026-08-16
  python3 scripts/docket_view.py --selftest
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import tempfile
import zlib

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True).stdout.strip() or "."
DOCKET_DEFAULT = os.path.join(ROOT, "PROME", "DOCKET.tsv")
BEGIN, END = "<!-- DOCKET-VIEW BEGIN -->", "<!-- DOCKET-VIEW END -->"
N_FIELDS = 6
DAYN = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
DAYMAP = {"mon": 0, "tue": 1, "tues": 1, "wed": 2, "thu": 3, "thur": 3, "thurs": 3, "fri": 4,
          "sat": 5, "sun": 6, "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
          "friday": 4, "saturday": 5, "sunday": 6}
RE_SPAN = re.compile(r"^(~)?(\d{4})-(\d{2})-(\d{2})(?:\.\.(\d{4})-(\d{2})-(\d{2}))?$")


# ----------------------------------------------------------------------------- DOCKET read
class DocketError(Exception):
    pass


def load_docket(path, skip_ragged=False):
    """Parse DOCKET.tsv. Returns list of rows (dicts, with physical line numbers).
    Raises DocketError on a ragged data row (constraint 3) or a missing file."""
    if not os.path.exists(path):
        raise DocketError(f"canonical docket missing at {path}")
    rows, ragged = [], []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#") or line.startswith("date\t"):
                continue
            parts = line.split("\t")
            if len(parts) != N_FIELDS:
                ragged.append((n, len(parts)))
                continue
            span = parts[0].strip()
            m = RE_SPAN.match(span)
            start = end = None
            if m:
                start = dt.date(int(m.group(2)), int(m.group(3)), int(m.group(4)))
                end = (dt.date(int(m.group(5)), int(m.group(6)), int(m.group(7)))
                       if m.group(5) else start)
            rows.append({"line": n, "span": span, "approx": bool(m and m.group(1)),
                         "start": start, "end": end, "catalyst": parts[1].strip(),
                         "owners": parts[2].strip(), "state": parts[3].strip(),
                         "artifacts": parts[4].strip(), "notes": parts[5].strip()})
    if ragged and skip_ragged:
        for n, k in ragged:
            print(f"DOCKET-VIEW note: SKIPPED ragged L{n} ({k} fields) under --skip-ragged (snapshot/forensic use only)")
    elif ragged:
        shown = ", ".join(f"L{n}={k} fields" for n, k in ragged[:6])
        raise DocketError(f"{len(ragged)} ragged data row(s) (expected {N_FIELDS} fields): {shown}"
                          + (" …" if len(ragged) > 6 else ""))
    if not rows:
        raise DocketError("docket parsed to ZERO rows — refusing to render an empty view")
    return rows


def state_kind(state):
    s = state.strip().upper()
    if s.startswith("PENDING") or s.startswith("★"):
        return "PENDING"
    if s.startswith("RE-DATED") or s.startswith("SLID"):
        return "PENDING"          # still forward-looking; the date cell is the live date
    return "TERMINAL"


# ----------------------------------------------------------------------------- render
def short(text, n):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def fmt_day(d):
    return f"{DAYN[d.weekday()]} {d.month}/{d.day}"


def render(rows, as_of, window=21, detail_days=7, full_chars=90, brief_chars=48, src="PROME/DOCKET.tsv"):
    """Return the generated block text (BEGIN…END inclusive) — deterministic for (rows, as_of)."""
    live = [r for r in rows if state_kind(r["state"]) == "PENDING"]
    dated = [r for r in live if r["start"]]
    undated = [r for r in live if not r["start"]]
    horizon = as_of + dt.timedelta(days=window)
    overdue = [r for r in dated if r["end"] < as_of]
    forward = [r for r in dated if r["end"] >= as_of and r["start"] <= horizon]
    beyond = [r for r in dated if r["start"] > horizon]
    vintage = zlib.crc32("\n".join(f"{r['line']}\t{r['span']}\t{r['state']}\t{r['catalyst']}"
                                   for r in live).encode())

    out = [BEGIN,
           f"*GENERATED by `scripts/docket_view.py` — source `{src}` · as-of {as_of.isoformat()} "
           f"({DAYN[as_of.weekday()]}) · window {window}d → {horizon.isoformat()} · "
           f"live rows {len(live)} = {len(forward)} in window + {len(overdue)} OVERDUE + "
           f"{len(beyond)} beyond window (not shown) + {len(undated)} undated · "
           f"docket-crc32 {vintage}. Rows cited by physical line (L#). "
           f"Do not hand-edit inside the markers; the line after END is the hand-annotation line.*"]

    if overdue:
        def tag(r):
            st = r["state"].upper()
            return ("ᶜ" if "COVERED" in st else "") + ("ᵒ" if "OVERDUE" in st else "")
        out.append(f"**⚠️ OVERDUE {len(overdue)} — PENDING rows dated before {as_of.isoformat()} with no terminal "
                   f"disposition (safety net: resolve, re-date, or tombstone; ᶜ = COVERED-annotated, ᵒ = OVERDUE-annotated):** "
                   + " · ".join(f"L{r['line']} {r['end'].month}/{r['end'].day}{tag(r)} {short(r['owners'].split('/')[0].split(' ')[0], 9)}"
                                for r in sorted(overdue, key=lambda r: (r["end"], r["line"]))))
    if undated:
        out.append(f"**UNDATED {len(undated)} (session-keyed):** "
                   + " · ".join(f"L{r['line']} `{r['span']}`" for r in undated))

    # forward window, grouped by START date (windows show their span)
    by_day = {}
    for r in sorted(forward, key=lambda r: (max(r["start"], as_of), r["line"])):
        by_day.setdefault(max(r["start"], as_of), []).append(r)
    parts = []
    for d in sorted(by_day):
        items = []
        for r in by_day[d]:
            near = (r["start"] - as_of).days <= detail_days
            txt = short(r["catalyst"], full_chars if near else brief_chars)
            span = "" if r["end"] == r["start"] else (
                f" (since {r['start'].month}/{r['start'].day} →{r['end'].month}/{r['end'].day})" if r["start"] < as_of
                else f" (→{r['end'].month}/{r['end'].day})")
            approx = "~" if r["approx"] else ""
            items.append(f"{approx}{txt}{span} [{r['owners']}] (L{r['line']})")
        head = f"**{fmt_day(d)}:**" if (d - as_of).days <= detail_days else f"**{d.month}/{d.day}:**"
        parts.append(f"{head} " + " · ".join(items))
    out.append(" — ".join(parts) if parts else f"*(no PENDING rows inside the {window}-day window)*")
    if beyond:
        nxt = min(beyond, key=lambda r: (r["start"], r["line"]))
        out.append(f"*Beyond the window: {len(beyond)} row(s); next = {nxt['span']} L{nxt['line']} "
                   f"{short(nxt['catalyst'], 50)}.*")
    out.append(END)
    return "\n".join(out)


def splice(text, block):
    """Replace the marked block in `text` with `block`. Raises on 0 or >1 markers."""
    b, e = text.count(BEGIN), text.count(END)
    if b != 1 or e != 1:
        raise DocketError(f"marker count BEGIN={b} END={e} — need exactly one of each; refusing to guess an anchor")
    i, j = text.index(BEGIN), text.index(END) + len(END)
    if j < i:
        raise DocketError("END marker precedes BEGIN marker")
    return text[:i] + block + text[j:]


def write_view(prose_path, docket_path, as_of, dry_run=False, budget=6000, **kw):
    rows = load_docket(docket_path)
    block = render(rows, as_of, src=os.path.relpath(docket_path, ROOT) if docket_path.startswith(ROOT) else docket_path, **kw)
    if dry_run:
        print(block)
        return 0, block
    with open(prose_path, encoding="utf-8") as f:
        text = f.read()
    new = splice(text, block)
    if len(block.encode()) > budget:
        print(f"DOCKET-VIEW ⚠️ block is {len(block.encode())} B > --budget {budget} B — the OVERDUE count is usually why; "
              f"resolve/tombstone rows or pass --budget (advisory, still written)")
    if new == text:
        print(f"DOCKET-VIEW ✓ unchanged — block byte-identical ({len(block.encode())} B) in {os.path.relpath(prose_path, ROOT)}")
        return 0, block
    tmp = prose_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(new)
    os.replace(tmp, prose_path)
    print(f"DOCKET-VIEW ✓ wrote {len(block.encode())} B block into {os.path.relpath(prose_path, ROOT)} "
          f"(file {len(text.encode())} → {len(new.encode())} B)")
    return 0, block


# ----------------------------------------------------------------------------- check
STOP = set("""the a an and or of to in on at for by with from vs via per not no is are was be as
this that its it their his her our your day days week weeks month months next last first second
third re re-ping ping read grade grades graded grading review reviews check checks watch window
print prints owner owners live dead pending resolved registered docket row rows line lines note notes
todo done open close closed new old date dated est approx target earliest latest eve am pm et
begins begin ends end expire expires expiry cluster time stop stops mon tue wed thu fri sat sun
monday tuesday wednesday thursday friday saturday sunday jan feb mar apr may jun jul aug sep sept oct
nov dec will prome daedalus walter hit miss own tier unchanged owed log orch record forge held sold
ruled rules rule word words item items leg legs card cards packet packets session sessions boot
closeout status gate gates level levels fire fired fires kill kills tell tells frame frames""".split())
RE_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9\-\.§#]{1,}")
RE_MD = re.compile(r"(?<![\w/\-–—])(\d{1,2})/(\d{1,2})(?![\d/])")
RE_ISO = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")
RE_LREF = re.compile(r"\bL(\d{1,4})\b")


def anchors(text):
    toks = set()
    for t in RE_TOKEN.findall(text):
        t2 = t.strip(".-#§")
        letters = re.sub(r"[^A-Za-z]", "", t2)
        if len(t2) < 2 or len(letters) < 2 or letters.lower() in STOP or t2.lower() in STOP:
            continue
        has_digit = any(c.isdigit() for c in t2)
        if "-" in t2 and not has_digit and t2 == t2.lower():
            continue                                  # "re-check", "private-credit", "in-session": prose, not IDs
        if t2.isupper() or t2[0].isupper() or has_digit or "-" in t2:
            toks.add(t2.lower())
    return toks


def norm_id(t):
    return re.sub(r"[^a-z0-9]", "", t)


def hits_between(prose_toks, row_toks):
    """Exact token hits, plus ID-containment hits ("flg-t08" ⊂ "gate-flg-t08"): returns the
    set of ROW tokens hit, so df-weighting stays keyed to the row vocabulary."""
    hit = prose_toks & row_toks
    for pt in prose_toks:
        if pt in hit or not idlike(pt):
            continue
        npt = norm_id(pt)
        if len(npt) < 5:
            continue
        for rt in row_toks:
            if rt not in hit and idlike(rt) and (npt in norm_id(rt) or norm_id(rt) in npt) and len(norm_id(rt)) >= 5:
                hit.add(rt)
    return hit


def idlike(t):
    """Ticker/ID-shaped token ('brt-26', 'gate-brent-cot-35b', 'hban', 'nfp') — strong alone."""
    return any(c.isdigit() for c in t) or "-" in t or (t.isalpha() and len(t) >= 3 and t.upper() == t)


def md_date(mo, d, as_of):
    """M/D → date in as_of's year; a month >6 behind as_of rolls to next year."""
    try:
        cand = dt.date(as_of.year, mo, d)
    except ValueError:
        return None
    if (as_of - cand).days > 183:
        try:
            cand = dt.date(as_of.year + 1, mo, d)
        except ValueError:
            return None
    return cand


def section_lines(text, section):
    """Line numbers belonging to the markdown section whose heading contains `section`
    (heading line → line before the next heading). None = whole file."""
    if not section:
        return None
    keep, inside = set(), False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            inside = section.lower() in line.lower()
        if inside:
            keep.add(n)
    if not keep:
        raise DocketError(f"--section {section!r}: no heading contains it — refusing to check zero lines as clean")
    return keep


def segments(text, as_of, only=None):
    """Yield (lineno, segment_text, [dates], context_date, weekday_claims).
    A bold header `**THU 9/3:**` / `**8/22 · 8/24-8/29**` sets the context for the
    segments that follow it on the same line (SCRATCH shape); table cells and ` · ` /
    ` — ` splits are the segment boundaries (HEARTBEAT + SCRATCH shapes)."""
    in_block = False
    for n, line in enumerate(text.splitlines(), 1):
        # Constraint 1 (2026-09-03, PROME post-flip): the GENERATED block is OUTPUT, never input —
        # its rendered catalyst text ("Will 9/2 10:57 …") was being read back as dated claims.
        if BEGIN in line:
            in_block = True
        if in_block:
            if END in line:
                in_block = False
            continue
        if only is not None and n not in only:
            continue
        if not (RE_MD.search(line) or RE_ISO.search(line)):
            continue
        ctx = None
        # split on em-dash groups first, then cells, then middots
        for grp in re.split(r"\s+[—–]\s+", line):
            for cell in grp.split("|"):
                for seg in re.split(r"\s+·\s+", cell):
                    seg = seg.strip()
                    if not seg:
                        continue
                    m = re.match(r"^\**\s*(?:~~)?\**\s*((?:[A-Z][a-z]{2}|[A-Z]{3})\s+)?(\d{1,2})/(\d{1,2})[^*]*?:?\**\s*:?", seg)
                    header = re.match(r"^\*\*([^*]{1,40})\*\*", seg)
                    if header and (RE_MD.search(header.group(1)) or RE_ISO.search(header.group(1))):
                        h = header.group(1)
                        dates = [d for d in (md_date(int(a), int(b), as_of) for a, b in RE_MD.findall(h)) if d]
                        dates += [dt.date(int(y), int(mo), int(d)) for y, mo, d in RE_ISO.findall(h)]
                        wk = [(w.lower(), dates[0]) for w in re.findall(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun|MON|TUE|WED|THU|FRI|SAT|SUN)[a-z]*\b", h)] if dates else []
                        ctx = dates
                        rest = seg[header.end():].strip(" :*")
                        yield n, rest, dates, ctx, wk
                        continue
                    body = RE_LREF.sub(" ", seg)
                    dates = [d for d in (md_date(int(a), int(b), as_of) for a, b in RE_MD.findall(body)) if d]
                    dates += [dt.date(int(y), int(mo), int(d)) for y, mo, d in RE_ISO.findall(body)]
                    yield n, seg, dates, ctx, []


def check_view(prose_path, docket_path, as_of, min_score=1.0, section=None, skip_ragged=False,
               near_days=60, verbose=False, ignore=None):
    rows = load_docket(docket_path, skip_ragged=skip_ragged)
    by_line = {r["line"]: r for r in rows}
    dated = [r for r in rows if r["start"]]
    df = {}
    for r in dated:
        r["_anchors"] = anchors(r["catalyst"] + " " + r["owners"])
        for t in r["_anchors"]:
            df[t] = df.get(t, 0) + 1
    with open(prose_path, encoding="utf-8") as f:
        text = f.read()
    only = section_lines(text, section)
    flags, unreg, claims, ignored = [], [], 0, 0
    ign = re.compile(ignore) if ignore else None
    for n, seg, dates, ctx, wk in segments(text, as_of, only):
        if ign and ign.search(seg):
            ignored += 1
            continue
        for wname, d in wk:
            want = DAYMAP.get(wname[:3])
            if want is not None and d.weekday() != want:
                flags.append((n, "WEEKDAY", f"header says {wname.upper()} but {d.isoformat()} is a {DAYN[d.weekday()]}"))
        claim_dates = dates or (ctx or [])
        if not claim_dates:
            continue
        # 1. explicit citation "(L242)" — the DOCKET citation convention — is the strongest anchor
        cited = [by_line[int(x)] for x in RE_LREF.findall(seg) if int(x) in by_line]
        if cited:
            claims += 1
            live = [r for r in cited if r["start"]]
            if not live:
                continue                       # cites an undated / terminal row — nothing to date-check
            if any(r["start"] <= d <= r["end"] for r in live for d in claim_dates):
                continue
            r = live[0]
            flags.append((n, "DATE", f"prose dates {', '.join(d.isoformat() for d in claim_dates)} for "
                          f"“{short(seg, 70)}” but the row it CITES, L{r['line']}, is dated {r['span']} "
                          f"“{short(r['catalyst'], 60)}”"))
            continue
        # 2. anchor-token match, restricted to rows within ±near_days of the claim
        toks = anchors(seg)
        if not toks:
            continue
        near = [r for r in dated if min(abs((r["start"] - d).days) for d in claim_dates) <= near_days
                or any(r["start"] <= d <= r["end"] for d in claim_dates)]
        far_hits = []

        def score_rows(cands):
            out = []
            for r in cands:
                hit = hits_between(toks, r["_anchors"])
                if not hit:
                    continue
                score = sum(1.0 / df[t] for t in hit)
                strong_single = len(hit) == 1 and df[next(iter(hit))] <= 2 and idlike(next(iter(hit)))
                if strong_single or (len(hit) >= 2 and score >= min_score) or len(hit) >= 3:
                    out.append((score, r, hit))
            return sorted(out, key=lambda x: -x[0])

        scored = score_rows(near)
        if not scored:
            far_hits = score_rows([r for r in dated if r not in near])
            if far_hits:
                unreg.append((n, claim_dates, seg, far_hits[0][1]))
            continue
        claims += 1
        top = [x for x in scored if x[0] >= scored[0][0] * 0.6]
        if any(r["start"] <= d <= r["end"] for _, r, _ in top for d in claim_dates):
            continue
        if not any(state_kind(r["state"]) == "PENDING" for _, r, _ in top):
            # every matching row is TERMINAL (a past instance already resolved): the prose names a
            # NEXT instance with no row of its own — the reverse drift direction, INFO not DIVERGENCE
            unreg.append((n, claim_dates, seg, top[0][1]))
            continue
        nearest = min(top, key=lambda x: min(abs((x[1]["start"] - d).days) for d in claim_dates))
        _, r, hit = nearest
        flags.append((n, "DATE",
                      f"prose dates {', '.join(d.isoformat() for d in claim_dates)} for “{short(seg, 70)}” — "
                      f"no matching DOCKET row covers them; nearest L{r['line']} = {r['span']} "
                      f"“{short(r['catalyst'], 60)}” (matched on: {', '.join(sorted(hit))})"))
    rel = os.path.relpath(prose_path, ROOT) if os.path.abspath(prose_path).startswith(ROOT) else prose_path
    scope = f" §{section!r}" if section else ""
    tail = (f"; {len(unreg)} dated claim(s) matched only a row >{near_days}d away — possibly UNREGISTERED "
            f"instances of a recurring event (the other drift direction; --verbose lists them)") if unreg else ""
    if ignored:
        tail += f"; {ignored} segment(s) MUTED by --ignore {ignore!r} — muted is not checked"
    if verbose:
        for n, ds, seg, r in unreg:
            print(f"  {rel}:{n} [INFO unregistered?] {', '.join(d.isoformat() for d in ds)} “{short(seg, 60)}” — "
                  f"only far row L{r['line']} {r['span']} “{short(r['catalyst'], 40)}”")
    if flags:
        print(f"DOCKET-CHECK ⚠️  {len(flags)} divergence(s) in {rel}{scope} ({claims} dated claim(s) matched to DOCKET rows{tail}):")
        for n, kind, msg in flags:
            print(f"  {rel}:{n} [{kind}] {msg}")
        return 1
    print(f"DOCKET-CHECK ✓ {rel}{scope}: {claims} dated claim(s) matched to DOCKET rows, all covered{tail}"
          + ("" if claims else " — ⚠️ ZERO claims matched: the surface may not be a DOCKET view, or the shapes differ (a clean line over zero matches proves nothing)"))
    return 0


# ----------------------------------------------------------------------------- selftest
FIXTURE_DOCKET = (
    "# LIVE ledger — fixture\n"
    "date\tcatalyst\towners\tstate\tartifacts_citing\tnotes\n"
    "2026-08-30\tPost-2026 Colorado River operating guidelines — EARLIEST legal ROD (NEPA ≥30d after the 7/31 Final EIS NOA)\tAEOLUS\tPENDING\tAGENTS/AEOLUS/CALENDAR.md\tREGISTERED 8/3\n"
    "2026-10-01\tPost-2026 Colorado River operating guidelines — Reclamation Record of Decision (Interior's stated TARGET)\tAEOLUS/WATT/CARL\tPENDING\tROUTING_TABLE.md\t~TARGET\n"
    "2026-08-10\tOLD THING that never resolved\tSAM\tPENDING\t-\told\n"
    "2026-08-17\tJapan Q2 GDP\tSAM\tRESOLVED 2026-08-17\thist\t—\n"
    "2026-08-21\tBaker Hughes rigs — BRT-26 line 457\tBRENT\tPENDING\tHEARTBEAT.md §1\tREGISTERED\n"
    "next-OZK-session\tOZK MI3 screen re-run\tOZK\tPENDING\t-\tundated\n"
    "2026-09-20\tFar future item\tRED\tPENDING\t-\t-\n"
    "2026-10-01\tNYC RENT FREEZE EFFECTIVE — FLG T-08 = GATE-FLG-T08\tFLG/PROME\tPENDING\t-\t-\n"
    "2026-08-17\tNAHB HMI + HOMER ATTOM re-check\tHOMER\tPENDING\t-\t-\n"
    "2026-08-12..2026-08-20\tFALCON leg-3 WEEKLY sweep window (in progress at as-of)\tFALCON\tPENDING\t-\t-\n"
)
FIXTURE_PROSE = "# scratch\n\nintro\n\n" + BEGIN + "\nold view\n" + END + "\n★ hand line\n\ntail\n"


def _run(cmd):
    p = subprocess.run([sys.executable, os.path.abspath(__file__)] + cmd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def selftest():
    fails = 0

    def drill(name, ok, detail=""):
        nonlocal fails
        fails += not ok
        print(f"  {'✓' if ok else '✗'} {name}{(' — ' + detail) if detail else ''}")

    with tempfile.TemporaryDirectory() as td:
        dk = os.path.join(td, "DOCKET.tsv")
        pr = os.path.join(td, "SCRATCH.md")
        open(dk, "w", encoding="utf-8").write(FIXTURE_DOCKET)
        open(pr, "w", encoding="utf-8").write(FIXTURE_PROSE)
        asof = ["--as-of", "2026-08-16"]

        # 1. write renders; overdue row above window; undated counted; far row counted
        rc, out = _run(["--write", pr, "--docket", dk] + asof)
        t = open(pr, encoding="utf-8").read()
        blk = t[t.index(BEGIN):t.index(END) + len(END)]
        drill("write: rc 0 and block written", rc == 0 and "old view" not in t and BEGIN in t, f"rc={rc}")
        drill("past-due PENDING surfaces ABOVE the window (OVERDUE section before the calendar)",
              "OVERDUE" in blk and blk.index("OVERDUE") < blk.index("**FRI 8/21") and "L5" in blk)
        drill("undated row COUNTED, not dropped", "UNDATED 1" in blk and "next-OZK-session" in blk)
        drill("beyond-window rows COUNTED (3 beyond: Colorado 10/1 + NYC 10/1 + far 9/20), next named", "3 beyond window" in blk and "Far future" in blk)
        drill("RESOLVED row excluded from the live view", "Japan Q2" not in blk)
        drill("outside-marker text untouched (hand line + tail)", "★ hand line" in t and t.endswith("tail\n") and "intro" in t)
        drill("weekday computed (2026-08-21 = FRI)", "**FRI 8/21:**" in blk)
        # 2. idempotence
        rc2, _ = _run(["--write", pr, "--docket", dk] + asof)
        t2 = open(pr, encoding="utf-8").read()
        drill("idempotence: second run zero diff, reports unchanged", rc2 == 0 and t2 == t)
        # 3. ragged docket ⇒ rc 2, no write
        bad = os.path.join(td, "BAD.tsv")
        open(bad, "w", encoding="utf-8").write(FIXTURE_DOCKET + "2026-09-01\tragged row\tX\tPENDING\n")
        before = open(pr, encoding="utf-8").read()
        rc3, out3 = _run(["--write", pr, "--docket", bad] + asof)
        drill("ragged DOCKET ⇒ rc 2 and NO write", rc3 == 2 and open(pr, encoding="utf-8").read() == before and "ragged" in out3, f"rc={rc3}")
        # 4. missing marker ⇒ rc 2, no write
        nm = os.path.join(td, "NOMARK.md")
        open(nm, "w", encoding="utf-8").write("# no markers here\n")
        rc4, out4 = _run(["--write", nm, "--docket", dk] + asof)
        drill("missing marker ⇒ rc 2 and NO write", rc4 == 2 and open(nm, encoding="utf-8").read() == "# no markers here\n", f"rc={rc4}")
        # 5. duplicate marker ⇒ rc 2
        dm = os.path.join(td, "DUP.md")
        open(dm, "w", encoding="utf-8").write(FIXTURE_PROSE + BEGIN + "\n" + END + "\n")
        rc5, _ = _run(["--write", dm, "--docket", dk] + asof)
        drill("duplicated markers ⇒ rc 2 (never guess an anchor)", rc5 == 2, f"rc={rc5}")
        # 6. empty docket ⇒ rc 2
        em = os.path.join(td, "EMPTY.tsv")
        open(em, "w", encoding="utf-8").write("# only comments\n")
        rc6, _ = _run(["--write", pr, "--docket", em] + asof)
        drill("zero-row DOCKET ⇒ rc 2 (never render an empty view as clean)", rc6 == 2, f"rc={rc6}")
        # 7. check-mode positive control: the audit-#9 shape
        v1 = os.path.join(td, "view_bad.md")
        open(v1, "w", encoding="utf-8").write("**8/22 · 8/24-8/29:** S6 pilot grades [8/22] · AEOLUS Colorado ROD [8/25] · T5 [8/26]\n")
        rc7, out7 = _run(["--check", v1, "--docket", dk] + asof)
        drill("check: 'Colorado ROD [8/25]' FLAGS against the 8/30 row (audit-#9 blocking class)",
              rc7 == 1 and "Colorado" in out7 and "2026-08-25" in out7 and "L3" in out7, f"rc={rc7}")
        # 8. check-mode negative control
        v2 = os.path.join(td, "view_ok.md")
        open(v2, "w", encoding="utf-8").write("**8/30:** AEOLUS Colorado ROD earliest-legal [8/30] · Baker Hughes rigs [8/21]\n")
        rc8, out8 = _run(["--check", v2, "--docket", dk] + asof)
        drill("check: correct dates read CLEAN (negative control)", rc8 == 0 and "all covered" in out8 and "2 dated claim" in out8, f"rc={rc8}")
        # 9. weekday-label divergence
        v3 = os.path.join(td, "view_wk.md")
        open(v3, "w", encoding="utf-8").write("**SAT 8/21:** Baker Hughes rigs\n")
        rc9, out9 = _run(["--check", v3, "--docket", dk] + asof)
        drill("check: wrong weekday label flags (8/21 is FRI)", rc9 == 1 and "WEEKDAY" in out9, f"rc={rc9}")
        # 9b. L-ref citation is the strongest anchor: cited row covers ⇒ clean; cited row does not ⇒ flag
        v5 = os.path.join(td, "view_lref.md")
        open(v5, "w", encoding="utf-8").write("**8/30:** something vague (L3)\n**8/25:** something vague (L3)\n")
        rc11, out11 = _run(["--check", v5, "--docket", dk] + asof)
        drill("check: explicit (L#) citation graded against the cited row (1 flag of 2 claims)",
              rc11 == 1 and "CITES, L3" in out11 and "2 dated claim" in out11, f"rc={rc11}")
        # 9c. "MIDAS-01/02" is an ID, not a January date; --section scopes to one heading
        v6 = os.path.join(td, "view_sec.md")
        open(v6, "w", encoding="utf-8").write("# Positions\nColorado ROD [8/25] stale prose here\n\n# Live-catalyst calendar\n**8/21:** MIDAS-01/02 · Baker Hughes rigs\n")
        rc12, out12 = _run(["--check", v6, "--docket", dk, "--section", "catalyst calendar"] + asof)
        drill("check: --section scopes to the calendar heading (stale line outside it ignored) and 'MIDAS-01/02' is not a date",
              rc12 == 0 and "1 dated claim" in out12, f"rc={rc12} {out12.strip()[:80]}")
        rc13, out13 = _run(["--check", v6, "--docket", dk, "--section", "no such heading"] + asof)
        drill("check: --section naming no heading ⇒ rc 2 (never certify zero lines)", rc13 == 2, f"rc={rc13}")
        # 9d. ID containment ("FLG-T08" ⊂ "GATE-FLG-T08") finds the right row; hyphenated prose ("re-check") is not an anchor
        v7 = os.path.join(td, "view_id.md")
        open(v7, "w", encoding="utf-8").write("**10/1:** NYC rent freeze (FLG-T08) — **10/2:** HEARTBEAT size re-check\n")
        rc14, out14 = _run(["--check", v7, "--docket", dk] + asof)
        drill("check: ID containment matches the 10/1 NYC row (clean); 're-check' alone matches nothing",
              rc14 == 0 and "1 dated claim" in out14, f"rc={rc14} {out14.strip()[:90]}")
        # 9f. a claim whose only matching row is RESOLVED = unregistered next instance → INFO, not a flag
        v8 = os.path.join(td, "view_next.md")
        open(v8, "w", encoding="utf-8").write("**8/18:** Japan Q2 GDP re-read\n")
        rc16, out16 = _run(["--check", v8, "--docket", dk] + asof)
        drill("check: terminal-only match ⇒ INFO (unregistered next instance), rc 0, counted in the tail",
              rc16 == 0 and "1 dated claim(s) matched only a row" in out16, f"rc={rc16} {out16.strip()[:100]}")
        # 9g. in-progress window renders under as-of with 'since'
        drill("write: window row opened before as-of renders under as-of as '(since 8/12 →8/20)'",
              "(since 8/12 →8/20)" in blk and blk.index("**SUN 8/16:**") < blk.index("**FRI 8/21"))
        # 9e. --ignore mutes and SAYS so
        rc15, out15 = _run(["--check", v1, "--docket", dk, "--ignore", "Colorado"] + asof)
        drill("check: --ignore mutes the segment and prints the muted count", rc15 == 0 and "MUTED by --ignore" in out15, f"rc={rc15}")
        # 9h. the generated block is skipped by --check (constraint 1: output is never input)
        v9 = os.path.join(td, "view_gen.md")
        open(v9, "w", encoding="utf-8").write(BEGIN + "\n**8/25:** AEOLUS Colorado ROD (Will ruled 8/25) (L3)\n" + END + "\nhand line: nothing dated\n")
        rc17, out17 = _run(["--check", v9, "--docket", dk] + asof)
        drill("check: dates INSIDE the generated block are skipped (constraint 1), zero claims matched", rc17 == 0 and "ZERO claims matched" in out17, f"rc={rc17}")
        # 10. zero-match surface says so
        v4 = os.path.join(td, "view_none.md")
        open(v4, "w", encoding="utf-8").write("nothing dated relevant 1/1\n")
        rc10, out10 = _run(["--check", v4, "--docket", dk] + asof)
        drill("check: zero matched claims prints its own blind-spot line", rc10 == 0 and "ZERO claims matched" in out10)
    if fails:
        print(f"DOCKET-VIEW SELFTEST ✗ {fails} drill(s) FAILED — do not trust the tool")
        return 1
    print("DOCKET-VIEW SELFTEST ✓ 24/24 drills behaved")
    return 0


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--write", metavar="PROSE", help="render into PROSE's marked block (SCRATCH)")
    ap.add_argument("--check", nargs="+", metavar="PROSE", help="diff dated claims in PROSE file(s) vs DOCKET; never writes")
    ap.add_argument("--docket", default=DOCKET_DEFAULT, help="DOCKET.tsv path (default PROME/DOCKET.tsv; use a snapshot for tests)")
    ap.add_argument("--as-of", default=dt.date.today().isoformat(), help="window anchor date (default today)")
    ap.add_argument("--window", type=int, default=21, help="forward window in days (default 21)")
    ap.add_argument("--detail", type=int, default=7, help="days shown in full detail with weekday (default 7)")
    ap.add_argument("--chars", type=int, default=90, help="catalyst text cap inside the detail window (default 90; beyond it, about half)")
    ap.add_argument("--dry-run", action="store_true", help="with --write: print the block, touch nothing")
    ap.add_argument("--section", help="with --check: only the markdown section whose heading contains this text")
    ap.add_argument("--skip-ragged", action="store_true", help="snapshot/forensic use: skip ragged rows LOUDLY instead of rc 2")
    ap.add_argument("--verbose", action="store_true", help="with --check: list claims that matched only a far-dated row")
    ap.add_argument("--ignore", metavar="REGEX", help="with --check: mute segments matching REGEX (e.g. GATES-lane 'review' items); the count of muted segments is always printed")
    ap.add_argument("--budget", type=int, default=6000, help="with --write: advisory warning if the block exceeds this many bytes (default 6000)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        as_of = dt.date.fromisoformat(a.as_of)
    except ValueError:
        print(f"ERROR: --as-of must be YYYY-MM-DD, got {a.as_of!r}", file=sys.stderr)
        return 2
    try:
        if a.write:
            rc, _ = write_view(a.write, a.docket, as_of, dry_run=a.dry_run, budget=a.budget, window=a.window, detail_days=a.detail, full_chars=a.chars, brief_chars=max(24, a.chars // 2))
            return rc
        if a.check:
            worst = 0
            for f in a.check:
                worst = max(worst, check_view(f, a.docket, as_of, section=a.section,
                                              skip_ragged=a.skip_ragged, verbose=a.verbose, ignore=a.ignore))
            return worst
    except DocketError as e:
        print(f"DOCKET-VIEW ✗ rc 2 — {e} (nothing written)", file=sys.stderr)
        return 2
    except OSError as e:
        print(f"DOCKET-VIEW ✗ rc 2 — {e} (nothing written)", file=sys.stderr)
        return 2
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
