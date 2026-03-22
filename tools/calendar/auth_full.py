"""Full OAuth flow — generates URL, waits for redirect URL input, exchanges token."""
import json, os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Allow http://localhost redirect

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDS_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/credentials.json'
TOKEN_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/token.json'

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
flow.redirect_uri = 'http://localhost'

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
print(f"AUTH_URL: {auth_url}")
print("\nWaiting for redirect URL...")

redirect_url = input("Paste the full redirect URL: ").strip()

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
