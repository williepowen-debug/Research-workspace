"""Verify EGBN snapshot integrity and identify changes to original sources."""
from pathlib import Path
import hashlib
import json
import subprocess

hub = Path(__file__).resolve().parent
root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=hub, text=True).strip())
manifest = json.loads((hub / 'INVENTORY.json').read_text())
errors, changed_sources = [], []
for entry in manifest['entries']:
    destination = root / entry['destination']
    if not destination.is_file():
        errors.append('Missing copy: ' + entry['destination'])
        continue
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    if digest != entry['destination_sha256']:
        errors.append('Changed copy: ' + entry['destination'])
    source = root / entry['source']
    if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != entry['source_sha256']:
        changed_sources.append(entry['source'])
print(f"Snapshot: {manifest['captured_at_utc']}; {len(manifest['entries'])} files checked")
for error in errors:
    print(error)
for source in changed_sources:
    print('Original changed since capture; review snapshot freshness: ' + source)
if not errors and not changed_sources:
    print('PASS: every copy/extract matches its manifest; all originals match their capture hashes')
raise SystemExit(2 if errors else 1 if changed_sources else 0)
