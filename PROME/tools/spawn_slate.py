#!/usr/bin/env python3
"""spawn_slate.py — the prepared spawn SLATE. Read-only except for the ONE file it writes (--out).

STATUS: built 2026-10-02 by DAEDALUS on PROME's commission (prome-96; Will: "okay put in DAEDALUS inbox I
will spawn in separate window"). Acceptance conditions, written before this file existed:
PROME/tools/tests/ACCEPTANCE_spawn_slate_2026-10-02.md. A SIBLING of spawn_list.py, which it imports and
never edits: every row here is a row `spawn_list.collect()` returned, and the census at the bottom is
`spawn_list.render()` itself.

QUESTION IT ANSWERS: for each desk with a due registered row — has the owner returned anything on it and
WHERE, which rows belong to one wake, what is the assignment text, what else would ride along, what does
it cost against the cap. spawn_list answers WHO is due; PROME was answering those by hand at every boot.

WHAT IT IS NOT: no spawn authority (advisory; only PROME spawns) · no calendar of its own (DOCKET / GATES /
ROSTER / ORCH_LOG are the only sources; it keeps no state) · no ranking that hides a row (order is for
reader attention; conservation is checked and printed) · no LLM, no network.

⛔ THE PRE-CHECK IS A POINTER, NEVER A VERDICT. v1 of this file classed rows ALREADY ANSWERED / PARTIAL
ANSWER from keywords beside a citation. An independent reader failed it the same day (2 of 4 live
ANSWERED rows were not answered: BRENT's packet said "not gradable before 15:30", MIDAS's said "WAIT …
please re-spawn"; two PARTIAL rows were complete on the owner's side). Whether a return answers a row is a
READ, and no keyword rule did it. So the tool says only RETURN FOUND (and which artifact to open first) ·
NO CITING RETURN · UNCHECKED, and an ACTIVE row is always "read first", never "no spawn needed".
Record: the ACCEPTANCE file § Reader A.

EXIT: same as spawn_list on the same inputs (2 UNKNOWN · 1 DARK · 0), and 2 on a conservation failure or
an unreadable DOCKET/GATES (the --out file is then overwritten with a FAILED banner, never left stale).
USAGE: python3 PROME/tools/spawn_slate.py [--horizon N] [--as-of YYYY-MM-DD] [--out PATH | --stdout]
       [--docket PATH|REV:PATH] [--gates …] [--roster …] [--orch-log PATH]
"""
import argparse, contextlib, datetime as dt, io, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spawn_list as sl            # noqa: E402 — fail LOUD if it moves; never a local copy of its rules

BUDGET_B = 32550                   # root CLAUDE.md read-cap byte budget (whole-read surfaces)
RELATED_DAYS = 14
ASSIGN_WORDS = 120
COMMIT_WINDOW = 200                # owner commits read per desk; hitting it is declared, never silent
GATE_LOOKBACK_D = 6                # gate rows: 6, not 7 — a weekly gate's PREVIOUS review day must fall outside the window (Reader A #2)
ID_MAX_ROWS = 2                    # an identifier named by more open rows than this does not discriminate
DOW = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# HINT ONLY — printed beside a return so the reader knows what to look for. It never changes a token.
HINT = re.compile(r"not yet|not published|unpublished|not out\b|still not|not grad\w+|not fresh|pending|\bwait\b|\barmed\b|"
                  r"re-?spawn|deferred|\bpartial|unresolved|not done|ungraded|no grade|co-sign", re.I)
ID_PATTERNS = (r"WQ-\d+[a-z]?", r"GATE-[A-Z0-9]+(?:-[A-Z0-9]+)*", r"FORUM-\d+", r"[A-Z]{2,6}-F?\d{1,3}")
TIMING = re.compile(r"(?:after|before|by|until|from)\s+~?\d{1,2}:\d{2}\s*(?:ET|EDT|EST|IST|UTC|Z)\b|post-close|pre-close|"
                    r"pre-open|after the (?:\w+ ){0,3}(?:close|open)", re.I)
MONEY = re.compile(r"\b(?:trade|order|fill|roll|buy|sell|spend|position|capital)\b", re.I)
LAUNCH = ("ACTIVE", "TIER-2", "SPECIAL")
ROSTER_H2 = ("ACTIVE", "TIER-2", "DORMANT", "RETIRED", "ARCHIVE SOURCES", "SPECIAL", "TOOL-CLASS", "OFF-FLEET",
             "CLASSIFICATION PENDING")
TERMS = (
    "- **[DARK] / [ACTIVE]** (row class, from `spawn_list`): has the owner made a commit of its own on or after the row's start date "
    "(a window's first day; else the due date; for a gate, its registration date)? No = DARK, yes = ACTIVE. Not the same word as "
    "**ROSTER class ACTIVE**, which is the desk's standing in `PROME/ROSTER.md`.",
    "- **RETURN FOUND**: the owner committed something that cites the row. It is a pointer to what to read, NOT a finding that the row is "
    "answered — an independent read on 10/02 found 2 of 4 such rows unanswered. **Strong** = names the row key, or carries a row "
    "identifier in a commit subject / packet filename; **body mention** = an identifier only inside the text. **hint words** are keyword "
    "matches near the citation; they decide nothing.",
    "- **Cap**: 4 due-row spawns per PROME boot (one boot = one PROME session start; `PROME/CLAUDE.md` spawn block). C6 raises it to 8 "
    "only when every desk woken that boot is woken on a due catalyst/review row. Whether a re-ping counts is unruled (DOCKET L444). "
    "A slot number here is slate ORDER, not proof a slot is free.",
    "- **Re-ping**: a SendMessage to a live desk session; if the desk has no session it is a packet to its inbox or a spawn — PROME's call.",
    "- **Lane WQ-184 L0**: a registered dated row with a dark owner. The aged-ACTION (WQ-206) and aged-waits (WQ-221) lanes are not computed here.",
    "- **Inherited limits**: desk attribution and first-owner parsing are `spawn_list`'s (open residue: DOCKET L455, L459).",
)


def git(*args):
    r = subprocess.run(["git", "-C", str(sl.ROOT), *args], capture_output=True, text=True)
    return r.returncode, r.stdout, (r.stderr or "").strip().split("\n")[0][:120]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def daylabel(d: dt.date) -> str:
    return f"{DOW[d.weekday()]} {d.month:02d}/{d.day:02d}"


# ── row detail ────────────────────────────────────────────────────────────────
class Detail:
    """The full cells behind one spawn_list.Row (the Row carries a 72-char catalyst only)."""
    def __init__(self, row, desc, owner_cell, state, source, notes, start, due, kind):
        self.row, self.desc, self.owner_cell, self.state = row, norm(desc), norm(owner_cell), norm(state)
        self.source, self.notes, self.start, self.due, self.kind = norm(source), norm(notes), start, due, kind
        self.since = (due - dt.timedelta(days=GATE_LOOKBACK_D)) if kind == "G" else start
        self.pre = None             # (token, [lines], first artifact) — ACTIVE rows only

    @property
    def key(self):
        return self.row.key


def details(rows, docket_text, gates_text):
    dlines = docket_text.split("\n")
    gates, hdr = {}, None
    for raw in gates_text.split("\n"):
        if not raw or raw.startswith("#"):
            continue
        c = raw.split("\t")
        if hdr is None:
            hdr = [h.strip() for h in c]; continue
        g = dict(zip(hdr, c)); gates[g.get("gate_id", "")] = g
    out = []
    for r in rows:
        due = dt.date.fromisoformat(r.due)
        if r.key.startswith("D:L"):
            c = dlines[int(r.key[3:]) - 1].split("\t") + [""] * 6
            s = c[0].split("..")[0].strip()
            start = dt.date.fromisoformat(s) if sl.DATE.fullmatch(s) else due
            out.append(Detail(r, c[1], c[2], c[3], c[4], c[5], start, due, "D"))
        else:
            g = gates.get(r.key[2:], {})
            reg = g.get("registered", "").strip()
            start = dt.date.fromisoformat(reg[:10]) if sl.DATE.match(reg) else due
            out.append(Detail(r, g.get("condition", ""), g.get("owner", ""), g.get("state", ""),
                              g.get("definition_surface", "") + " " + g.get("source", ""),
                              g.get("consequence_on_fire", ""), start, due, "G"))
    return out


def desk_tokens(owner_cell: str):
    """Capitalised tokens of an owner cell in order, code spans removed. 'SHADE/BROCK/CREED' → all three.
    The caller filters by ROSTER — this cannot tell a desk from any other upper-case word."""
    return re.findall(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9]{2,}(?![A-Za-z0-9_])", re.sub(r"`[^`]*`", " ", owner_cell))


# ── citations ─────────────────────────────────────────────────────────────────
def key_pattern(d):
    if d.kind == "G":
        return re.compile(rf"(?<![A-Za-z0-9-]){re.escape(d.key[2:])}(?![A-Za-z0-9-])")
    n = d.key[3:]
    return re.compile(rf"(?<![A-Za-z0-9_.:/#-])(?:D:|DOCKET\s+)?L{n}(?![0-9A-Za-z_])")


def row_ids(desc: str):
    found = []
    for p in ID_PATTERNS:
        for m in re.finditer(rf"(?<![A-Za-z0-9-]){p}(?![A-Za-z0-9]|\.\d)", desc):     # `VX-3.01` is not the id `VX-3`
            if m.group(0) not in found:
                found.append(m.group(0))
    return found


def discriminating_ids(d, id_counts):
    if d.kind == "G":
        return []
    return [i for i in row_ids(d.desc) if id_counts.get(i, 0) <= ID_MAX_ROWS]


def find_citations(text: str, d, ids):
    """[(what, context)] — context = ±160 chars round the hit (where the hint words are looked for)."""
    hits = []
    pats = [("key " + d.key, key_pattern(d))] + [
        ("id " + i, re.compile(rf"(?<![A-Za-z0-9-]){re.escape(i)}(?![A-Za-z0-9]|\.\d)")) for i in ids]
    for what, pat in pats:
        m = pat.search(text)
        if m:
            hits.append((what, norm(text[max(0, m.start() - 160): m.end() + 160])))
    return hits


def hints(text: str):
    seen = []
    for m in HINT.finditer(text):
        w = m.group(0).lower()
        if w not in seen:
            seen.append(w)
    return (" · hint words: " + ", ".join(f"'{w}'" for w in seen[:4])) if seen else ""


# ── owner evidence (committed state at ONE captured rev) ──────────────────────
class Evidence:
    def __init__(self, rev: str, until: str | None):
        self.rev, self.until, self._commits, self._packets, self._text = rev, until, {}, None, {}

    def owner_commits(self, desk: str, since: dt.date):
        """(commits, problem). commits = [(sha, date, subject, body, paths)] the desk's OWN, newest first."""
        k = (desk, since)
        if k not in self._commits:
            cmd = ["log", self.rev, "--no-merges", "-n", str(COMMIT_WINDOW), f"--since={since.isoformat()} 00:00",
                   "--format=%x1e%h%x09%cs%x09%s%x1f%b%x1f", "--name-only", "--extended-regexp",
                   f"--grep={sl.grep_pattern(desk)}"]
            if self.until:
                cmd.append(f"--until={self.until}")
            rc, out, err = git(*cmd)
            if rc != 0:
                self._commits[k] = ([], f"git log failed ({err or rc})")
            else:
                got, n = [], 0
                for rec in out.split("\x1e"):
                    if not rec.strip():
                        continue
                    n += 1
                    parts = rec.split("\x1f")
                    h = parts[0].split("\t", 2)
                    if len(parts) < 3 or len(h) < 3:
                        continue
                    paths = [p for p in parts[2].split("\n") if p.strip()]
                    if sl.attributed(desk, h[2], paths):
                        got.append((h[0], h[1], h[2], parts[1], paths))
                self._commits[k] = (got, f"commit window truncated at {COMMIT_WINDOW}" if n >= COMMIT_WINDOW else None)
        return self._commits[k]

    def packets(self, desk: str, since: dt.date):
        """Owner→PROME packets by filename, dated on/after `since`. (paths, problem)."""
        if self._packets is None:
            rc, out, err = git("ls-tree", "-r", "--name-only", self.rev, "--", "PROME/inbox")
            self._packets = (out.split("\n"), None) if rc == 0 else ([], f"PROME/inbox unreadable ({err or rc})")
        files, prob = self._packets
        pat = re.compile(rf"^PROME/inbox/(?:processed/)?(\d{{4}}-\d{{2}}-\d{{2}})[a-z]?_from-{re.escape(desk)}_")
        seen, got = set(), []
        for f in files:
            m = pat.match(f)
            if m and m.group(1) >= since.isoformat() and Path(f).name not in seen:
                seen.add(Path(f).name); got.append(f)     # inbox/ + processed/ copy of one packet counts once
        return sorted(got), prob

    def text(self, path: str):
        if path not in self._text:
            rc, out, _ = git("show", f"{self.rev}:{path}")
            self._text[path] = out if rc == 0 else None
        return self._text[path]

    def inbox(self, desk: str, today: dt.date):
        home = "PROME" if desk == "PROME" else f"AGENTS/{desk}"
        rc, out, err = git("ls-tree", "-r", "--name-only", self.rev, "--", f"{home}/inbox")
        if rc != 0:
            return f"CANNOT-EVALUATE ({err or rc})"
        files = [f for f in out.split("\n") if f.endswith(".md") and "/processed/" not in f
                 and Path(f).name.lower() != "readme.md"]
        if not files:
            return "0 packets"
        dates = sorted(m.group(0) for f in files if (m := sl.DATE.match(Path(f).name)))
        aged = sum(1 for x in dates if (today - dt.date.fromisoformat(x)).days >= 7)
        tail = f", oldest {dates[0]}" + (f", {aged} aged ≥7d (WQ-206 lane if any is an `action:` handoff — not classified here)"
                                         if aged else "") if dates else ""
        return f"{len(files)} packet(s){tail} — a spawn drains the WHOLE inbox"


def precheck(d, ev: Evidence, id_counts):
    """ACTIVE rows only → (token, [lines], first artifact or None). A POINTER, never a verdict (module docstring)."""
    desk, ids = d.row.owner, discriminating_ids(d, id_counts)
    commits, cprob = ev.owner_commits(desk, d.since)
    packets, pprob = ev.packets(desk, d.since)
    if cprob and cprob.startswith("git log failed"):
        return "UNCHECKED", [f"{cprob} — run by hand; until then treat as NO CITING RETURN"], None
    items, added, other = [], {}, []         # items = (order, is_packet, strong, date, artifact, line); order 0 = NEWEST commit

    def best(head, body):
        hits = [(w, c, True) for w, c in find_citations(head, d, ids)]
        hits += [(w, c, w.startswith("key ")) for w, c in find_citations(body, d, ids)]
        hits.sort(key=lambda h: not h[2])
        return hits[0] if hits else None
    for n, (sha, date, subj, body, paths) in enumerate(commits):
        for p in paths:
            added[Path(p).name] = (n, sha, date)     # commits are newest-first: the OLDEST carrier wins, i.e. the add
        hit = best(subj, body)
        if hit:
            what, ctx, strong = hit
            items.append((n, False, strong, date, f"commit {sha}",
                          f"commit `{sha}` ({date}) cites {what}{'' if strong else ' (body mention)'}: \"{subj[:90]}\""
                          + (f" · `{next((p for p in paths if p.startswith('PROME/inbox/')), paths[0])}`" if paths else "") + hints(subj + " " + ctx)))
    for p in packets:
        if Path(p).name not in added:
            continue                 # wrong owner: named from-DESK, but no own commit of the desk carried it
        n, sha, date = added[Path(p).name]
        body = ev.text(p) or ""
        hit = best(Path(p).name, body)
        if hit:
            what, ctx, strong = hit
            items.append((n, True, strong, date, p,
                          f"packet `{p}` ({date}, carried by `{sha}`) cites {what}{'' if strong else ' (body mention)'}"
                          + hints(Path(p).name + " " + body).replace("hint words:", "hint words anywhere in the packet:")))
        else:
            other.append((n, p))
    tail = []
    if other:
        other.sort()
        tail.append(f"other packets from {desk} since {d.since} that do NOT cite the row (the answer may be in one): "
                    + " · ".join("`" + Path(p).name.replace(f"_from-{desk}_", " ")[:-3] + "`" for _n, p in other[:6]) + (f" (+{len(other) - 6} more)" if len(other) > 6 else ""))
    if cprob:
        tail.append(f"⚠ {cprob} — older returns were not read")
    if pprob:
        tail.append(f"⚠ packets: CANNOT-EVALUATE ({pprob})")
    if items:
        items.sort(key=lambda r: (not r[2], r[0], not r[1]))             # strong first, then newest, packets before commits
        lines = [r[5] for r in items[:3]]
        if not any(r[2] for r in items):
            lines.insert(0, "only body mentions — no return names the row key or carries its identifier in a subject or filename")
        if items[0][3] < d.due.isoformat():
            lines.insert(0, f"⚠ the newest strong return is dated {items[0][3]}, BEFORE the due date {d.due} — it may be a plan or the previous cycle")
        if len(items) > 3:
            lines.append(f"(+{len(items) - 3} more citing return(s) since {d.since})")
        return "RETURN FOUND", lines + tail, items[0][4]
    cited = re.findall(rf"AGENTS/{re.escape(desk)}/[A-Za-z0-9_./\-]+", d.source)
    touched = None
    for sha, date, subj, _b, paths in commits:
        t = [p for p in paths if any(p == c.rstrip("/.") or p.startswith(c.rstrip("/.") + "/") for c in cited)]
        if t:
            touched = f"commit `{sha}` ({date}) touched `{t[0]}` — a file the row names — without citing the row: \"{subj[:80]}\""
            break
    if not commits and not cprob:
        return "NO CITING RETURN", [f"⚠ the owner has NO self-commit since {d.since} — spawn_list classes the row ACTIVE on an older commit "
                                    f"(since the row's start, {d.start}); for THIS cycle the owner is dark: weigh it as a spawn candidate"] + tail, None
    note = f"{len(commits)} owner self-commit(s) since {d.since}, none cites {d.key}" + (f" or {', '.join(ids)}" if ids else "")
    return "NO CITING RETURN", [note] + ([touched] if touched else []) + tail, None


# ── side sources ──────────────────────────────────────────────────────────────
def roster_classes(text: str):
    out, cur = {}, None
    for line in text.split("\n"):
        if line.startswith("## "):
            head = line[3:].upper()
            cur = next((h for h in ROSTER_H2 if head.startswith(h)), None)
        elif cur and line.startswith("|"):
            first = line.split("|")[1].strip().strip("*`[ ").split(" ")[0].strip("*`]")
            if re.fullmatch(r"[A-Z][A-Z0-9]{2,}", first):
                out.setdefault(first, cur)
        elif cur and (m := re.match(r"\*\*([A-Z][A-Z0-9]{2,})\*\* —", line)):     # SPECIAL lists desks as bold lines, not a table
            out.setdefault(m.group(1), cur)
    return out


def orch_today(text: str, day: str):
    """{desk: [(touch, trigger, delivered, desk cell)]} for rows dated `day`."""
    out = {}
    for raw in text.split("\n"):
        c = raw.split("\t")
        if len(c) >= 7 and c[0] == day:
            out.setdefault(c[1].split(" (")[0].strip(), []).append((c[3], norm(c[4]), norm(c[6]), c[1]))
    return out


def prome_annotation(d):
    last = None
    for m in re.finditer(r"(?:\+|annotated )(\d{4}-\d{2}-\d{2})", d.state, re.I):
        if m.group(1) >= d.since.isoformat():
            last = m
    if not last:
        return None
    w, at = d.state.split(" "), len(d.state[:last.start()].split(" ")) - 1
    return f"PROME annotated the row {last.group(1)} (words round the newest stamp only — read the state cell): \"[…] {' '.join(w[max(0, at - 14): at + 30])} […]\""


def must_travel(d):
    out = []
    for cell in (d.desc, d.notes, d.owner_cell):
        for s in re.split(r"(?<=[.!?])\s+", cell):
            if re.search(r"⛔(?! waits)", s) and s not in out:
                out.append(s)
    return out


def timing_words(d):
    out = []
    for cell in (d.desc, d.owner_cell, d.notes):
        last = -999
        for m in TIMING.finditer(cell):
            if m.start() - last < 90:
                continue
            last = m.start()
            out.append(norm(cell[max(0, m.start() - 45): m.end() + 45]))
    return out[:2]


# ── the assignment (verbatim spans only) ──────────────────────────────────────
def words(s: str):
    return [w for w in s.split(" ") if w]


def assignment(desk: str, ds, budget: int = ASSIGN_WORDS):
    """≤ budget words. Every quoted span is a verbatim prefix of a row cell; truncation is marked."""
    n = len(ds)
    done = []
    for d in ds:
        m = re.search(r"Done when[^.]*\.", d.notes) or re.search(r"Done when[^.]*\.", d.desc)
        done.append(" ".join(words(m.group(0))[:22]) if m else None)
    q, k = 60, n                    # q = quoted words per row; k = rows quoted (the rest are named by key only)
    while True:
        parts = [f"{desk}: {n} registered row{'s' if n > 1 else ''} due" + (" — in this order." if n > 1 else ".")]
        for i, d in enumerate(ds[:k], 1):
            w = words(d.desc)
            cut = len(w) > q
            quote = " ".join(w[:q])
            parts.append(f"{i}) {d.key} (due {daylabel(d.due)}): \"{quote}\"" + (f" […] read {d.key} whole." if cut else ""))
            if done[i - 1]:
                parts.append(f"\"{done[i - 1]}\"")
        if k < n:
            parts.append("Then, read whole: " + ", ".join(d.key for d in ds[k:]) + ".")
        parts.append("Return: your own record updated + one packet to PROME/inbox/ citing each row key.")
        text = " ".join(parts)
        if len(words(text)) <= budget or (q <= 8 and k <= 1):
            return text
        if q > 8:
            q -= 2
        else:
            k -= 1


# ── stanzas ───────────────────────────────────────────────────────────────────
RANK = {"UNKNOWN": 0, "DARK": 1, "NO CITING RETURN": 2, "UNCHECKED": 2, "RETURN FOUND": 3, "LANDS": 5}


def row_rank(d):
    c = d.row.cls
    if c == "ACTIVE":
        return RANK[d.pre[0]]
    return RANK["LANDS"] if c.startswith("LANDS") else RANK.get(c, 5)


def why_now(d):
    r = d.row
    when = (f"due today ({daylabel(d.due)})" if r.delta == 0 else
            f"{r.delta}d overdue (was due {daylabel(d.due)})" if r.delta > 0 else f"lands in {-r.delta}d ({daylabel(d.due)})")
    if r.cls == "DARK":
        return f"{when}; {r.basis} — nobody has run it."
    if r.cls == "UNKNOWN":
        return f"{when}; ⛔ {r.basis}"
    if r.cls.startswith("LANDS"):
        return f"{when}; not yet due — {r.basis}."
    tail = {"RETURN FOUND": "the owner has returned something citing it and the row is still open — read that return; it may answer the row, "
                            "one leg of it, or only say why it cannot be answered yet",
            "NO CITING RETURN": "nothing from the owner cites this row — a receipt gap, an answer that never named the row, or an owner dark this cycle",
            "UNCHECKED": "the owner has been in session since; the pre-check could not run"}[d.pre[0]]
    return f"{when}; {tail}."


def build(rows, dets, ev, today, roster_text, orch_text, related_rows, open_rows, id_counts):
    classes = roster_classes(roster_text) if roster_text else None
    orch = orch_today(orch_text, today.isoformat()) if orch_text is not None else None
    by_desk, unowned = {}, []
    for d in dets:
        if d.row.owner in ("PROME", "WILL"):
            continue
        if d.row.owner == "?":
            unowned.append(d); continue
        if d.row.cls == "ACTIVE":
            d.pre = precheck(d, ev, id_counts)
        by_desk.setdefault(d.row.owner, []).append(d)
    order = []
    for desk, ds in by_desk.items():
        ds.sort(key=lambda d: (d.due, d.kind, d.key))
        order.append((min(row_rank(d) for d in ds), -max(d.row.delta for d in ds), desk, ds))
    order.sort(key=lambda s: s[:3])
    related_keys = {r.key for r in related_rows}
    slot, out, lands = 0, [], []
    top = {"spawn": [], "unknown": [], "read": [], "gap": [], "flight": []}
    for _rank, _neg, desk, ds in order:
        rcls = classes.get(desk) if classes is not None else None
        launch = ("CANNOT-EVALUATE (ROSTER unreadable)" if classes is None else
                  "class SPECIAL (its ROSTER row says who may launch it)" if rcls == "SPECIAL" else
                  f"class {rcls}" if rcls in LAUNCH else f"⛔ NOT LAUNCHABLE ({rcls or 'absent from its classes — a sub-desk? spawn its parent'}) — re-own the row")
        touches = (orch or {}).get(desk, [])
        inflight = any(t[2].startswith("IN-FLIGHT") for t in touches)
        tw = [(d.key, s) for d in ds for s in timing_words(d)]
        clock = " ⏱" if tw else ""
        if all(d.row.cls.startswith("LANDS") for d in ds):
            lsc = ds[0].row.basis.replace("owner last self-commit ", "")
            lands.append(f"| {desk} | " + ", ".join(f"`{d.key}` {daylabel(d.due)}" for d in ds) + f" | {lsc} | {launch} | {ev.inbox(desk, today).split(' — ')[0]} |")
            continue
        dark = [d for d in ds if d.row.cls == "DARK"]
        unk = [d for d in ds if d.row.cls == "UNKNOWN"]
        if inflight:
            top["flight"].append(desk)
        if unk:
            verdict = "⛔ UNKNOWN — liveness not established; never a spawn"
            top["unknown"].append(f"{desk} ({', '.join(d.key for d in unk)})")
        elif dark and classes is not None and rcls not in LAUNCH:
            verdict = "⛔ NOT A SPAWN — owner is not launchable per ROSTER"
            top["unknown"].append(f"{desk} (not launchable; {', '.join(d.key for d in dark)})")
        elif dark:
            slot += 1
            cap = (f"slot {slot} of {sl.CAP_PER_BOOT}" if slot <= sl.CAP_PER_BOOT else
                   f"slot {slot} — beyond the ordinary cap of {sl.CAP_PER_BOOT} → Will's slate, unless the C6 terms hold (PROME's judgement)")
            verdict = (f"SPAWN CANDIDATE — Tier 1, WQ-184 L0 due row · {cap}"
                       + (" · ⏱ the row carries timing words: check them before waking" if tw else "")
                       + (" · ORCH_LOG shows an open touch today: check liveness first" if inflight else ""))
            top["spawn"].append(f"{desk}{clock} ({cap.split(' — ')[0]}; {', '.join(d.key for d in dark)})")
        else:
            verdict = "READ FIRST — spawn_list classes the row ACTIVE (an owner commit since its start date); the row is still open"
        for d in ds:
            if d.row.cls == "ACTIVE":
                if d.pre[0] == "RETURN FOUND":
                    top["read"].append(f"{desk} {d.key}{clock}")
                else:
                    top["gap"].append(f"{desk} {d.key}{clock} ({d.pre[0]})")
        L = [f"### {desk} — {verdict}", "",
             f"- **Desk:** ROSTER {launch} · cadence {ds[0].row.cadence} · lane WQ-184 L0"]
        if any(MONEY.search(d.desc) for d in ds):
            L.append("- **Tier check (PROME's judgement):** a row uses trade/position words — a trade or spend consequent stays Tier 3 whatever this slate says.")
        L.append("- **Why now:**")
        for d in ds:
            L.append(f"  - `{d.key}` [{d.row.cls}] — {why_now(d)}")
        pre = [d for d in ds if d.pre]
        if pre:
            L.append("- **Pre-check at the owner's artifact (a pointer to what to read, not a verdict):**")
            for d in pre:
                L.append(f"  - `{d.key}` → **{d.pre[0]}**")
                L += [f"    - {x}" for x in d.pre[1]]
        else:
            L.append("- **Pre-check at the owner's artifact:** n/a — no owner self-commit since the row's start date (that is what DARK means)")
        for d in ds:
            a = prome_annotation(d)
            if a:
                L.append(f"  - `{d.key}`: {a}")
        if orch is None:
            L.append("- **ORCH_LOG today:** CANNOT-EVALUATE (ORCH_LOG unreadable)")
        elif touches:
            keys = [d.key for d in ds]
            L.append("- **ORCH_LOG today (PROME's ledger; it lags a delivery and a death — corroborate with ListAgents):** " + " · ".join(
                f"{t[0]} {t[3].split('(')[-1].rstrip(')')}" + (" (cites " + ", ".join(k for k in keys if k in t[1]) + ")" if any(k in t[1] for k in keys) else "")
                + f" → {t[2][:48] or 'no delivery cell'}" for t in touches))
        work = [d for d in ds if d.row.cls in ("DARK", "UNKNOWN") or (d.pre and d.pre[0] != "RETURN FOUND")]
        if work:
            text = assignment(desk, work)
            label = "Bounded assignment" if dark or unk else "Re-ping text (nothing cites the row, so ask for it)"
            L.append(f"- **{label}** ({len(words(text))} words; quotes are verbatim from the rows, so a multi-desk row quotes every desk's leg):")
            L.append(f"  > {text}")
            ins = []
            for d in work:
                ins += [p for p in re.findall(r"(?:AGENTS|PROME|FORGE|FORUM)/[A-Za-z0-9_./\-]+", d.source) if p not in ins]
            if ins:
                L.append("  - Inputs (from the rows' source cells): " + " · ".join(f"`{p}`" for p in ins[:5]) + (f" (+{len(ins) - 5} more)" if len(ins) > 5 else ""))
        if len(work) < len(ds):
            L.append("- **If the read shows a row is still owed:** re-ping with the row's own words (" + ", ".join(f"`{d.key}`" for d in ds if d not in work)
                     + ") and say which leg is missing — no text is prepared, because what is missing is what the read finds.")
        mt = [(d.key, s) for d in ds for s in must_travel(d)]
        if mt:
            L.append("- **Must travel (verbatim from the row — a caveat is never dropped):**")
            L += [f"  - `{k}`: {s}" for k, s in mt]
        if tw:
            L.append("- **⏱ Timing words in the row (PROME judges whether a wake now is early or a second wake is owed):** " + " · ".join(f"`{k}`: \"…{s}…\"" for k, s in tw))
        rel = [r for r in related_rows if r.owner == desk and r.delta < 0 and r.key not in {d.key for d in ds}]
        second = [(ln, due) for ln, due, toks in open_rows if desk in toks[1:] and toks[0] != desk and f"D:L{ln}" in related_keys]
        if rel or second:
            L.append(f"- **Would also fit (not why-now; rows landing within +{RELATED_DAYS}d):**")
            L += [f"  - `{r.key}` due {daylabel(dt.date.fromisoformat(r.due))} (in {-r.delta}d): {r.catalyst}" for r in rel]
            if second:
                L.append("  - names this desk as a non-first owner (co-grader or only informed — the row says which): " + ", ".join(f"`D:L{ln}` ({due[5:]})" for ln, due in second))
        L.append(f"- **Inbox:** {ev.inbox(desk, today)}")
        out.append("\n".join(L))
    n_rows = sum(len(s[3]) for s in order)
    return out, lands, top, unowned, n_rows, len(order), (orch or {})


def open_rows_with_tokens(docket_text, today, horizon_days):
    """[(line, due, [capitalised tokens of the owner cell])] for OPEN rows due ≤ today + window, and id counts."""
    out, counts = [], {}
    limit = (today + dt.timedelta(days=max(horizon_days, RELATED_DAYS))).isoformat()
    for ln, _date, owner_cell, _over, desc in sl.list_open(docket_text, today):
        for i in set(row_ids(norm(desc))):
            counts[i] = counts.get(i, 0) + 1
        m = sl.DATE.findall(_date)
        if m and m[-1] <= limit:
            out.append((ln, m[-1], desk_tokens(owner_cell)))
    return out, counts


def compose(args, now_stamp: str):
    today = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date.today()
    until = (args.as_of + " 23:59") if args.as_of else None
    docket_text, gates_text = sl.read_text(args.docket), sl.read_text(args.gates)      # failure → caller's FAILED banner
    try:
        roster_text = sl.read_text(args.roster)
    except BaseException:
        roster_text = ""
    try:
        orch_text = sl.read_text(args.orch_log)
    except BaseException:
        orch_text = None
    rc, head, err = git("rev-list", "-1", f"--before={until}", "HEAD") if until else git("rev-parse", "HEAD")
    rev = head.strip() or "HEAD"
    live = sl.Liveness(until)
    rows = sl.collect(docket_text, gates_text, today, args.horizon, live, roster_text)
    related = sl.collect(docket_text, gates_text, today, max(args.horizon, RELATED_DAYS), live, roster_text)
    dets = details(rows, docket_text, gates_text)
    open_rows, id_counts = open_rows_with_tokens(docket_text, today, args.horizon)
    ev = Evidence(rev, until)
    stanzas, lands, top, unowned, n_desk_rows, n_desks, orch = build(rows, dets, ev, today, roster_text, orch_text,
                                                                    related, open_rows, id_counts)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc_list = sl.render(rows, today, args.horizon, True)
    census = buf.getvalue().rstrip("\n")
    n_prome = sum(1 for r in rows if r.cls == "PROME-OWNED")
    n_will = sum(1 for r in rows if r.cls == "WILL-OWNED")
    census_rows = len([l for l in census.split("\n")[2:] if re.match(r"(?:⚠️ |⛔ )?[DG]:", l)])
    conserved = (n_desk_rows + n_prome + n_will + len(unowned) == len(rows)) and census_rows == len(rows)
    prome_over = [r.delta for r in rows if r.cls == "PROME-OWNED"]
    spawned = sum(1 for ts in orch.values() for t in ts if t[0] == "1-SPAWN")

    def line(label, items, empty="none"):
        return f"- **{label}:** " + ("; ".join(items) if items else empty)
    B = []
    if not conserved:
        B.append(f"> ⛔ **SLATE INCOMPLETE — conservation FAILED** ({len(rows)} rows in ≠ {n_desk_rows} desk rows + {n_prome} PROME + "
                 f"{n_will} WILL + {len(unowned)} unowned, or census {census_rows}). Use `spawn_list.py` directly and report this.\n")
    B += ["> **GENERATED — do not edit.** Advisory only: PROME spawns, after ListAgents in the same minute. Sources: DOCKET · GATES · ROSTER · "
          "ORCH_LOG (working tree) and owner returns from committed history at the HEAD above. This file keeps no state of its own. "
          "⛔ `RETURN FOUND` points at what to read; it does NOT say the row is answered. Terms are defined at the bottom.", "",
          "## Read this first", "",
          line("Spawn candidates, in slate order (⏱ = the row carries timing words; read them before waking)", top["spawn"]),
          line("⛔ Unknown / not launchable", top["unknown"] + [f"{d.key} (owner cell unparseable)" for d in unowned]),
          line("Read first — the owner returned something citing the row, and the row is still open", top["read"]),
          line("Receipt gap — owner in session since, nothing cites the row", top["gap"]),
          line("ORCH_LOG shows an open (IN-FLIGHT) touch today — a return may be half-written; check liveness", top["flight"]),
          line("Not yet due, inside the horizon", [l.split(" | ")[0].strip("| ") for l in lands]),
          f"- **PROME's own due rows:** {n_prome}" + (f" (oldest {max(prome_over)}d overdue)" if prome_over else "")
          + f" · **Will-owned:** {n_will} — these get no stanza; each is a line in the census at the bottom.",
          f"- **Cap context:** ORCH_LOG shows {spawned} `1-SPAWN` row(s) dated {today}; how many belong to THIS boot is PROME's knowledge, "
          "so a slot number below is slate order, not a free slot.",
          f"- **Conservation:** {len(rows)} rows in = {n_desk_rows} desk-owned ({n_desks} desk(s)) + {n_prome} PROME + {n_will} WILL + {len(unowned)} unowned"
          f" · census rows {census_rows} · {'OK' if conserved else 'FAILED'}", "",
          f"## Desk stanzas ({len(stanzas)})", ""]
    B.append("\n\n".join(stanzas) if stanzas else "*No desk-owned row is due today or overdue.*")
    if lands:
        B += ["", "## Not yet due — lands inside the horizon (slate at closeout; the spawn waits for the first boot on/after the date)", "",
              "| Desk | Rows | Owner's last self-commit | ROSTER | Inbox |", "|---|---|---|---|---|"] + lands
    desks = set(roster_classes(roster_text)) if roster_text else None
    in_census = {r.key for r in rows}
    B += ["", "## Census rows that name a second desk (spawn_list reads the FIRST owner only)", ""]
    if desks is None:
        B.append("CANNOT-EVALUATE (ROSTER unreadable — desk names cannot be told from other capitalised words).")
    else:
        sec = []
        for ln, due, toks in open_rows:
            also = list(dict.fromkeys(t for t in toks[1:] if t in desks and t not in ("PROME", toks[0] if toks else "")))
            if f"D:L{ln}" in in_census and also:
                sec.append(f"`D:L{ln}` {toks[0]} + {', '.join(also)}")
        B.append(" · ".join(sec) if sec else "none")
        B += ["", "*A second-named desk may be a co-grader or only informed — the owner cell says which; this list cannot.*"]
    B += ["", "## Mechanical census", "", "```", census, "```", "", "## Terms", ""] + list(TERMS) + [""]
    body = "\n".join(B)
    rc_out = 2 if not conserved else rc_list
    return today, rev[:9], body, rc_out, top, len(rows)


def header(now_stamp, today, horizon, rev, body):
    def h(n):
        pct = round(100 * n / BUDGET_B)
        return (f"# SPAWN SLATE — generated {now_stamp} · as-of {today} ({DOW[today.weekday()]}) · horizon +{horizon}d · HEAD {rev} · "
                f"{n:,} B = {pct}% of the {BUDGET_B:,} B whole-read budget" + (" · ⛔ OVER BUDGET — read by section, never truncated" if n > BUDGET_B else ""))
    n = len((h(0) + "\n\n" + body).encode("utf-8"))
    for _ in range(3):
        n2 = len((h(n) + "\n\n" + body).encode("utf-8"))
        if n2 == n:
            break
        n = n2
    return h(n) + "\n\n" + body, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", type=int, default=0)
    ap.add_argument("--as-of")
    ap.add_argument("--docket", default="PROME/DOCKET.tsv")
    ap.add_argument("--gates", default="PROME/GATES.tsv")
    ap.add_argument("--roster", default="PROME/ROSTER.md")
    ap.add_argument("--orch-log", default="PROME/state/ORCH_LOG.tsv")
    ap.add_argument("--out", default="PROME/state/SPAWN_SLATE.md")
    ap.add_argument("--stdout", action="store_true", help="print the slate; write nothing")
    a = ap.parse_args()
    now = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    out = Path(a.out) if Path(a.out).is_absolute() else sl.ROOT / a.out
    try:
        today, rev, body, rc, top, n_rows = compose(a, now)
    except BaseException as e:
        if isinstance(e, (KeyboardInterrupt, SystemExit)):
            raise
        msg = (f"# SPAWN SLATE — ⛔ FAILED {now}\n\n> The slate could not be built ({type(e).__name__}: {str(e)[:200]}). "
               "Nothing below this line is current. Run `python3 PROME/tools/spawn_list.py --horizon 0` and report the failure.\n")
        if a.stdout:
            print(msg)
        else:
            out.parent.mkdir(parents=True, exist_ok=True); out.write_text(msg, encoding="utf-8")
            print(f"spawn_slate · ⛔ FAILED ({type(e).__name__}) — banner written to {a.out}; use spawn_list.py")
        return 2
    text, nbytes = header(now, today, a.horizon, rev, body)
    if a.stdout:
        sys.stdout.write(text)
        return rc
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"spawn_slate · as-of {today} · horizon +{a.horizon}d · {n_rows} row(s) → {a.out} ({nbytes:,} B, {round(100 * nbytes / BUDGET_B)}% of budget)")
    for label, k in (("spawn candidates", "spawn"), ("unknown", "unknown"), ("read first (owner returned; row still open)", "read"),
                     ("receipt gap", "gap"), ("ORCH_LOG open touch", "flight")):
        if top[k]:
            print(f"  {label}: " + "; ".join(top[k]))
    return rc


if __name__ == "__main__":
    sys.exit(main())
