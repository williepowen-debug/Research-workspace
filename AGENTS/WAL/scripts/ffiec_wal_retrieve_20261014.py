"""Bounded WAL-only FFIEC facsimile retrieval; never prints authentication material."""
import argparse
import base64
import csv
import hashlib
import io
import json
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

WAL = Path(__file__).resolve().parents[1]
ROOT = WAL.parents[1]
OUT = WAL / 'sources/ffiec_2026-10-14'
URL = 'https://ffieccdr.azure-api.us/public/RetrieveFacsimile'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('periods', nargs='+', help='YYYY-MM-DD reporting periods')
    ap.add_argument('--curl', action='store_true', help='Use the established repository curl transport')
    args = ap.parse_args()
    env = {}
    for line in (ROOT / 'FORGE/tools/market-data/.env').read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            env[key.strip()] = value.strip().strip('\"').strip("'")
    user, token = env.get('FFIEC_CDR_USERNAME'), env.get('FFIEC_CDR_TOKEN')
    if not user or not token:
        print('Credential fields unavailable; no request made.')
        return 2
    OUT.mkdir(exist_ok=True)
    records, network_failure = [], False
    for period in args.periods:
        date = datetime.strptime(period, '%Y-%m-%d')
        headers = {'UserID': user, 'Authentication': 'Bearer ' + token,
                   'Content-Type': 'application/json', 'dataSeries': 'Call',
                   'reportingPeriodEndDate': date.strftime('%m/%d/%Y'),
                   'fiIDType': 'ID_RSSD', 'fiID': '3138146', 'facsimileFormat': 'SDF'}
        record = {'period': period, 'rssd': 3138146, 'endpoint': URL,
                  'attempted_at_UTC': datetime.now(timezone.utc).isoformat(),
                  'transport': 'curl' if args.curl else 'urllib'}
        try:
            if args.curl:
                # Authentication is supplied via stdin, not printed or persisted.
                config = []
                for key, value in headers.items():
                    assert '\n' not in value and '\r' not in value
                    escaped = (key + ': ' + value).replace('\\', '\\\\').replace('"', '\\"')
                    config.append('header = "' + escaped + '"')
                result = subprocess.run(['curl', '-sS', '--max-time', '25', '--config', '-',
                                         '--write-out', '\n%{http_code}', URL],
                                        input='\n'.join(config), text=True, capture_output=True)
                if result.returncode:
                    record.update(status='NETWORK_ERROR', curl_rc=result.returncode)
                    network_failure = True
                    records.append(record)
                    print(period, record['status'], flush=True)
                    continue
                response_body, status = result.stdout.rsplit('\n', 1)
                record['http_status'] = int(status)
                if int(status) != 200:
                    record['status'] = 'HTTP_ERROR'
                    records.append(record)
                    print(period, record['status'], status, flush=True)
                    continue
                body = response_body.encode()
            else:
                with urllib.request.urlopen(urllib.request.Request(URL, headers=headers), timeout=25) as response:
                    body = response.read()
                    record['http_status'] = response.status
            payload = json.loads(body)
            if not isinstance(payload, str):
                record['status'] = 'NO_VALID_FACSIMILE'
            else:
                raw = base64.b64decode(payload, validate=True)
                text = raw.decode('utf-8-sig')
                rows = list(csv.DictReader(io.StringIO(text), delimiter=';'))
                assert rows and all(r['Bank RSSD Identifier'] == '3138146' for r in rows)
                assert all(r['Call Date'] == date.strftime('%Y%m%d') for r in rows)
                codes = [r['MDRM #'] for r in rows]
                assert len(codes) == len(set(codes)), 'duplicate MDRMs'
                target = OUT / ('WAL_' + period + '.sdf')
                if target.exists() and target.read_bytes() != raw:
                    record['status'] = 'EXISTING_FILE_DIFFERS_WITHHELD'
                else:
                    target.write_bytes(raw)
                    record.update(status='VERIFIED', path=str(target.relative_to(ROOT)),
                                  rows=len(rows), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        except urllib.error.HTTPError as error:
            record.update(status='HTTP_ERROR', http_status=error.code)
        except urllib.error.URLError:
            record['status'] = 'NETWORK_ERROR'
            network_failure = True
        except Exception as error:
            record.update(status='INVALID_OR_UNAVAILABLE', error_type=type(error).__name__)
        records.append(record)
        print(period, record['status'], record.get('http_status', ''), record.get('rows', ''), flush=True)
    name = 'retrieval_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json'
    (OUT / name).write_text(json.dumps({'records': records}, indent=2) + '\n')
    return 3 if network_failure else 0


if __name__ == '__main__':
    raise SystemExit(main())
