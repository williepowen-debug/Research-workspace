"""Step 1: Generate auth URL and save PKCE verifier + state."""
import json, os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDS_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/credentials.json'
STATE_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/auth_state.json'

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
flow.redirect_uri = 'http://localhost'

auth_url, state = flow.authorization_url(prompt='consent', access_type='offline')

# Save the PKCE code_verifier and state
state_data = {
    'code_verifier': flow.code_verifier,
    'state': state,
}
with open(STATE_FILE, 'w') as f:
    json.dump(state_data, f)

print(f"AUTH_URL: {auth_url}")
