"""Shared daily-log upsert for VIOLET's state-carrying canaries.

WHY THIS EXISTS (KB-VIO-160, 2026-07-30)
----------------------------------------
`jpy_vol.py`, `ovx.py` and `cheap_tail.py` each carried the same append guard:

    if any(line.startswith(asof + "\\t") for line in existing[1:]):
        return f"already has a row for {asof}"

That is *first-write-wins*. For a **state-carrying canary** it is the wrong rule,
and it fails in the silent direction:

  · boot runs at 09:08 ET, logs `CALM`
  · the event happens at 09:30 ET
  · every later run that day says "already has a row" and **skips**
  · the ledger keeps the CALMEST read of the day, forever

A wrong-but-loud row gets challenged. A **calm** row is unremarkable, so nothing
prompts anyone to look — the absence of an alert is indistinguishable from the
absence of the event. Live instance: `JPY_VOL.tsv` 2026-07-30 carried
`CALM / RV10 4.81` (written 09:08 ET) through a suspected-MOF intervention that
moved USD/JPY 5.8 yen at 09:30 ET and put the live canary at `FIRE / RV10 15.67`.
Same family as KB-VIO-139 (fill-forward), opposite corner: -139 froze the
*prior* day forward, this freezes *today* at its first read.

THE RULE THIS IMPLEMENTS
------------------------
Upsert, not append-once. On a re-run for the same date:

  · identical row      -> `skip-identical` (no churn, no rewrite)
  · differing row      -> `superseded`, and the caller is handed the diff so it
                          can print a loud line when `state` actually changed
  · `supersede=False`  -> `skip-exists` **plus the diff**, so a caller that
                          declines to write still cannot stay silent about it

NULL-PRESERVING MERGE. A later run may lose a leg an earlier one had (jpy_vol's
FXY IV leg drops out under the thin-strike guard; an off-RTH pull can serve
degraded quotes). A blind overwrite would let a *worse* read destroy a better
one — trading one silent-loss bug for another. So a new value that is null
(`None`, `""`, `"-"`) never overwrites a non-null stored value; every other
column takes the fresh value. `stamp_utc` is exempt (it is bookkeeping, not
data) and is excluded from the change diff so a pure re-stamp is not mistaken
for a data change.
"""

from __future__ import annotations

from pathlib import Path

NULLS = (None, "", "-", "nan", "None")

# Columns that are bookkeeping rather than data: always take the fresh value and
# never count toward the change diff.
STAMP_COLS = ("stamp_utc", "source_ts")


def _is_null(v) -> bool:
    return v is None or (isinstance(v, str) and v.strip() in NULLS) or str(v).strip() in NULLS


def _fmt(v) -> str:
    return "-" if v is None else str(v)


def upsert_row(
    path: Path,
    cols: list[str],
    row: list,
    *,
    date_col: str = "date",
    state_col: str | None = "state",
    supersede: bool = True,
    today: str | None = None,
    key_cols: list[str] | None = None,
) -> tuple[str, dict]:
    """Insert or update the row identified by `key_cols` (default `[date_col]`).

    `key_cols` exists because not every ledger is one-row-per-date:
    `VIX_OPTIONS.tsv` is one row per **(date, expiry)**. The identity of a row
    and the date used by the today-only guard are two different things, so they
    are two different parameters — collapsing them is how a composite-key
    ledger silently gets one row clobbered by another.

    Returns ``(status, changes)`` where status is one of ``appended`` /
    ``skip-identical`` / ``superseded`` / ``skip-exists`` / ``skip-past`` and
    ``changes`` maps ``column -> (old, new)`` for every non-stamp column whose
    value moved. ``changes`` is populated even when the write is declined, so a
    caller can never skip *silently*.

    A ``state`` transition is reported under the ``state_col`` key like any other
    column; callers should check for it explicitly and print loudly.

    ⚠️ TODAY-ONLY GUARD (added on first live run, before commit). Superseding is
    scoped to the CURRENT ET date. Some canaries date their row from the market
    data's as-of (which lags when a series has not published yet — ^SKEW prints
    ~17:00 ET) while deriving other columns from the wall clock. Without this
    guard, re-running on 7/30 while the data still reads 7/29 rewrites the
    *7/29* row with *7/30*'s clock — which is precisely the cross-date artifact
    (KB-VIO-139) this module was written to end. Caught live: `cheap_tail`
    rewrote the 7/29 row's `cat_event` from "FOMC Rate Decision" to the 7/30
    catalyst. A past-dated divergence is REPORTED (`skip-past`) and never
    written; repairing history is `backfill.py`'s job, deliberately and with the
    correct as-of, not a side effect of a boot run.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("\t".join(cols) + "\n", encoding="utf-8")

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        path.write_text("\t".join(cols) + "\n", encoding="utf-8")
        lines = ["\t".join(cols)]

    header, body = lines[0], lines[1:]
    d_idx = cols.index(date_col)
    date_key = _fmt(row[d_idx])
    new_cells = [_fmt(v) for v in row]

    k_idx = [cols.index(c) for c in (key_cols or [date_col])]
    want_key = [new_cells[i] for i in k_idx]

    hit = None
    for i, line in enumerate(body):
        cells = line.split("\t")
        if len(cells) <= max(k_idx):
            continue
        if [cells[i] for i in k_idx] == want_key:
            hit = i
            break

    if hit is None:
        with path.open("a", encoding="utf-8") as f:
            f.write("\t".join(new_cells) + "\n")
        return "appended", {}

    old_cells = body[hit].split("\t")
    # Tolerate a short/ragged stored row rather than crashing on it.
    old_cells += ["-"] * (len(cols) - len(old_cells))

    merged, changes = [], {}
    for j, col in enumerate(cols):
        old, new = old_cells[j], new_cells[j]
        if col in STAMP_COLS:
            merged.append(new)
            continue
        # A null incoming value must never destroy a stored non-null one.
        if _is_null(new) and not _is_null(old):
            merged.append(old)
            continue
        merged.append(new)
        if old != new:
            changes[col] = (old, new)

    if not changes:
        # Data is unchanged; refresh the stamp in place, report no churn.
        body[hit] = "\t".join(merged)
        path.write_text("\n".join([header] + body) + "\n", encoding="utf-8")
        return "skip-identical", {}

    # Never retro-edit a past-dated row from a live run — see the TODAY-ONLY
    # GUARD note above. Report the divergence; do not write it.
    if today is None:
        from datetime import datetime
        from zoneinfo import ZoneInfo
        today = str(datetime.now(ZoneInfo("America/New_York")).date())
    if date_key != today:
        return "skip-past", changes

    if not supersede:
        return "skip-exists", changes

    body[hit] = "\t".join(merged)
    path.write_text("\n".join([header] + body) + "\n", encoding="utf-8")
    return "superseded", changes


def describe(status: str, date_key: str, changes: dict, log_name: str,
             state_col: str | None = "state") -> str:
    """Render a one-line, honest result message for a canary's boot output.

    A state transition is 🔴-flagged: that is the whole reason this module
    exists, and it must not read like routine bookkeeping.
    """
    if status == "appended":
        return f"✓ appended {date_key} row to workbook/{log_name}"
    if status == "skip-identical":
        return f"{date_key} row already current in workbook/{log_name} (unchanged)"

    if state_col and state_col in changes:
        old, new = changes[state_col]
        head = f"🔴 STATE CHANGED {old} → {new}"
    else:
        head = "↻ values moved"

    detail = ", ".join(f"{k} {o}→{n}" for k, (o, n) in list(changes.items())[:4])
    more = f" (+{len(changes) - 4} more)" if len(changes) > 4 else ""

    if status == "superseded":
        return f"{head} — superseded {date_key} row in workbook/{log_name}: {detail}{more}"
    if status == "skip-past":
        return (f"⚠️ {head} on the PAST-DATED {date_key} row of workbook/{log_name} — NOT written "
                f"(today-only guard; the live read is a different date's clock): {detail}{more}. "
                f"If the stored row is genuinely wrong, repair it with backfill.py at the correct as-of.")
    return (f"⚠️ {head} but NOT written — workbook/{log_name} {date_key} row is STALE: "
            f"{detail}{more}. Re-run without --no-supersede to record it.")
