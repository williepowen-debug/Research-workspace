"""Step 2: Exchange code using saved PKCE verifier."""
import json, os, sys
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDS_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/credentials.json'
STATE_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/auth_state.json'
TOKEN_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/token.json'

redirect_url = sys.argv[1]

# Load saved state
with open(STATE_FILE) as f:
    state_data = json.load(f)

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
flow.redirect_uri = 'http://localhost'
flow.code_verifier = state_data['code_verifier']

flow.fetch_token(authorization_response=redirect_url, code_verifier=state_data['code_verifier'])

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

os.remove(STATE_FILE)
print("SUCCESS — Token saved!")
