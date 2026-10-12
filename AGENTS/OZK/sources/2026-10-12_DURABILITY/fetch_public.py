"""Preserve selected public primaries and fetch receipts; no authenticated access."""
import sys, json, hashlib, datetime, io
from pathlib import Path
import requests
from pdfminer.high_level import extract_text
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

root = Path(__file__).parent
for label, url in json.loads(Path(sys.argv[1]).read_text()):
    receipt = {'label': label, 'requested_url': url,
               'fetch_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 public research'}, timeout=25)
        suffix = '.pdf' if response.content.startswith(b'%PDF') else '.html'
        path = root / (label + suffix)
        path.write_bytes(response.content)
        receipt.update(status=response.status_code, final_url=response.url, bytes=len(response.content),
                       sha256=hashlib.sha256(response.content).hexdigest(), file=path.name)
        if response.status_code == 200:
            if suffix == '.pdf': text = extract_text(io.BytesIO(response.content))
            else:
                parser = Text(); parser.feed(response.text); text = '\n'.join(parser.parts)
            (root / (label + '.txt')).write_text(text)
    except Exception as error:
        receipt['error'] = type(error).__name__ + ': ' + str(error)
    with (root / 'FETCH_RECEIPTS.jsonl').open('a') as stream:
        stream.write(json.dumps(receipt) + '\n')
    print(json.dumps({key: value for key, value in receipt.items()
                      if key in ('label', 'status', 'bytes', 'error')}), flush=True)
