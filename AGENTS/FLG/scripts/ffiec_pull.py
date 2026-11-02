"""FLG-only FFIEC CDR Call Report facsimile pull (RSSD 694904); never prints authentication material.

Contract: argv = YYYY-MM-DD reporting periods + --out <dir under AGENTS/FLG/sources/>.
Writes 694904_<MM-DD-YYYY>_call.sdf per period (refuses to overwrite a differing file) and a retrieval_*.json
receipt (sha256, rows, bytes, last-update range). rc 0 all VERIFIED · 1 any period not verified · 2 no credentials.
Template: AGENTS/WAL/scripts/ffiec_wal_retrieve_20261014.py (curl transport, credentials via stdin).
"""
import argparse, base64, csv, hashlib, io, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

FLG = Path(__file__).resolve().parents[1]
ROOT = FLG.parents[1]
URL = 'https://ffieccdr.azure-api.us/public/RetrieveFacsimile'
RSSD = '694904'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('periods', nargs='+')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    out = (ROOT / a.out).resolve()
    assert str(out).startswith(str(FLG / 'sources')), 'out must be under AGENTS/FLG/sources/'
    env = {}
    for line in (ROOT / 'FORGE/tools/market-data/.env').read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    user, token = env.get('FFIEC_CDR_USERNAME'), env.get('FFIEC_CDR_TOKEN')
    if not user or not token:
        print('Credential fields unavailable; no request made.')
        return 2
    out.mkdir(parents=True, exist_ok=True)
    recs, bad = [], False
    for p in a.periods:
        d = datetime.strptime(p, '%Y-%m-%d')
        h = {'UserID': user, 'Authentication': 'Bearer ' + token, 'Content-Type': 'application/json',
             'dataSeries': 'Call', 'reportingPeriodEndDate': d.strftime('%m/%d/%Y'),
             'fiIDType': 'ID_RSSD', 'fiID': RSSD, 'facsimileFormat': 'SDF'}
        rec = {'period': p, 'rssd': int(RSSD), 'endpoint': URL,
               'attempted_at_UTC': datetime.now(timezone.utc).isoformat()}
        cfg = []
        for k, v in h.items():
            assert '\n' not in v and '\r' not in v
            cfg.append('header = "' + (k + ': ' + v).replace('\\', '\\\\').replace('"', '\\"') + '"')
        r = subprocess.run(['curl', '-sS', '--max-time', '40', '--config', '-', '--write-out', '\n%{http_code}', URL],
                           input='\n'.join(cfg), text=True, capture_output=True)
        try:
            if r.returncode:
                raise RuntimeError('curl rc %d' % r.returncode)
            body, status = r.stdout.rsplit('\n', 1)
            rec['http_status'] = int(status)
            if int(status) != 200:
                raise RuntimeError('HTTP %s: %s' % (status, body[:120]))
            payload = json.loads(body)
            if not isinstance(payload, str):
                raise RuntimeError('NO_VALID_FACSIMILE')
            raw = base64.b64decode(payload, validate=True)
            rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig')), delimiter=';'))
            assert rows and all(x['Bank RSSD Identifier'] == RSSD for x in rows), 'RSSD mismatch'
            assert all(x['Call Date'] == d.strftime('%Y%m%d') for x in rows), 'date mismatch'
            codes = [x['MDRM #'] for x in rows]
            assert len(codes) == len(set(codes)), 'duplicate MDRMs'
            t = out / ('%s_%s_call.sdf' % (RSSD, d.strftime('%m-%d-%Y')))
            if t.exists() and t.read_bytes() != raw:
                raise RuntimeError('EXISTING_FILE_DIFFERS_WITHHELD')
            t.write_bytes(raw)
            lu = sorted({x['Last Update'] for x in rows})
            rec.update(status='VERIFIED', path=str(t.relative_to(ROOT)), rows=len(rows), bytes=len(raw),
                       sha256=hashlib.sha256(raw).hexdigest(), last_update_min=lu[0], last_update_max=lu[-1])
        except Exception as e:
            rec.update(status='NOT_VERIFIED', error=str(e)[:200])
            bad = True
        recs.append(rec)
        print(p, rec['status'], rec.get('http_status', ''), rec.get('rows', ''), rec.get('sha256', rec.get('error', '')))
    (out / ('retrieval_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '.json')).write_text(
        json.dumps({'records': recs}, indent=2) + '\n')
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
