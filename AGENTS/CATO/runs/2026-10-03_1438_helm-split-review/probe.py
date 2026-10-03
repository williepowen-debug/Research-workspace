"""Independent Helm split checks; run against an isolated repository snapshot."""
import contextlib
import copy
import html
import io
import json
from pathlib import Path
import re
import sys
from unittest.mock import patch

root = Path(sys.argv[1]).resolve()
if (root / '.git').exists() or not (root / '.cato-isolated-review').is_file():
    raise SystemExit('Use a throwaway git-archive extraction with a .cato-isolated-review marker, never a live checkout.')
out = Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(root / 'PROME/tools'))
import desk_attention as da
import will_handbook as wh

rows = da.pending_work(root)
page, errors = da.render(root, docket_href='docket.html')
doc, doc_errors = da.render_docket_page(root)
page_ids = set(re.findall(r"href='docket.html#(L\d+)'", page))
doc_ids = set(re.findall(r"<details id='(L\d+)'>", doc))
assert page_ids == doc_ids == {'L' + str(r['line']) for r in rows}
for row in rows:
    record = doc.split(f"<details id='L{row['line']}'>", 1)[1].split('</details>', 1)[0]
    for key in ('title', 'owner', 'state', 'next', 'evidence'):
        assert html.escape(row[key]) in record, (row['line'], key)
print(json.dumps({'ordinary_rows': len(rows), 'row_local_cells_preserved': True,
                  'all_local_targets_present': True, 'errors': errors + doc_errors}))
(out / 'legacy-attention-current.txt').write_text(da.render(root)[0])

def render_case(name, row_results=None, force_no_file=False, real_feed=False):
    destination = out / name
    destination.mkdir(exist_ok=True)
    wh.ALERTS.clear()
    buf = io.StringIO()
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch.object(sys, 'argv', ['will_handbook', '-o', str(destination / 'handbook.html')]
                                         + ([] if real_feed else ['--no-feed'])))
        stack.enter_context(contextlib.redirect_stdout(buf))
        counter = stack.enter_context(patch.object(wh.wb, 'update_changes', wraps=wh.wb.update_changes))
        reader = None
        if row_results is not None:
            reader = stack.enter_context(patch.object(da, 'pending_work', side_effect=row_results))
        if force_no_file:
            stack.enter_context(patch.object(da, 'render_docket_page', return_value=('', ['injected supporting-file error'])))
        rc = wh.main()
    p = (destination / 'handbook.html').read_text()
    d = (destination / 'docket.html').read_text() if (destination / 'docket.html').exists() else ''
    links = set(re.findall(r"href='docket.html#(L\d+)'", p))
    ids = set(re.findall(r"<details id='(L\d+)'>", d))
    result = {'case': name, 'rc': rc, 'stdout': buf.getvalue().strip(), 'alerts': wh.ALERTS[:],
              'missing_targets': sorted(links - ids), 'pending_work_calls': reader.call_count if reader else None,
              'feed_calls': counter.call_count, 'feed_write': counter.call_args.kwargs['write']}
    print(json.dumps(result))
    return result

# A row is appended or becomes pending between the two source reads in one main() call.
extra = copy.deepcopy(rows[0])
extra.update(line=999999, title='Newly pending work — append between reads')
changed = render_case('changed-between-reads', [rows, rows + [extra]])
assert changed['rc'] == 0 and changed['missing_targets'] == ['L999999']

# Repeat with an actual source append at the write_docket/attention boundary.
docket_path = root / 'PROME/DOCKET.tsv'
original_docket = docket_path.read_bytes()
original_write = wh.write_docket
def append_after_support(out_path):
    target = original_write(out_path)
    with docket_path.open('a') as f:
        f.write('2026-10-03\tCATO synthetic concurrent row\tPROME\tPENDING\tevidence\tcompletion\n')
    return target
try:
    with patch.object(wh, 'write_docket', append_after_support):
        actual = render_case('actual-source-append')
    assert actual['rc'] == 0 and len(actual['missing_targets']) == 1
finally:
    docket_path.write_bytes(original_docket)

# A parse/read failure in the first read recovers before the second read.
transient = render_case('transient-read-error', [ValueError('injected transient DOCKET error'), rows])
assert transient['rc'] == 0 and transient['alerts'] == []

# A supporting-file-specific failure also silently returns to the large legacy page.
support = render_case('supporting-file-error', force_no_file=True)
assert support['rc'] == 0 and support['alerts'] == []

# P5: actual full render with the real feed writer, confined to this snapshot.
normal = render_case('real-feed', real_feed=True)
assert normal['rc'] == 0 and normal['feed_calls'] == 1 and normal['feed_write'] is True
