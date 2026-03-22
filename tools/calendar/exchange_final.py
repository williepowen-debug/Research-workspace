"""Exchange token using the exact same flow state."""
import json, os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDS_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/credentials.json'
TOKEN_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/token.json'

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
flow.redirect_uri = 'http://localhost'

# Generate fresh auth URL and immediately exchange — no PKCE mismatch
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

# Write the auth URL for the user
with open('/tmp/calendar_auth_url.txt', 'w') as f:
    f.write(auth_url)

print(f"AUTH_URL_WRITTEN")
print("Waiting for redirect URL file at /tmp/calendar_redirect.txt ...")

import time
while not os.path.exists('/tmp/calendar_redirect.txt'):
    time.sleep(1)

with open('/tmp/calendar_redirect.txt') as f:
    redirect_url = f.read().strip()

os.remove('/tmp/calendar_redirect.txt')

flow.fetch_token(authorization_response=redirect_url)

creds = flow.credentials
token_data = {
    'token': creds.token,
    'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri,
    'client_id': creds.client_id,
    'client_secret': creds.client_secret,
    'scopes': list(creds.scopes) if creds.scopes else [],
}
with open(TOKEN_FILE, 'w') as f:
    json.dump(token_data, f, indent=2)

print("SUCCESS — Token saved!")
