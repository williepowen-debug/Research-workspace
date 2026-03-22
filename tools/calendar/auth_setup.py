"""One-time OAuth setup for Google Calendar. Generates auth URL for manual flow."""
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDS_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/credentials.json'
TOKEN_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/token.json'

flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)

# Use manual/OOB-style flow for headless server
flow.redirect_uri = 'http://localhost'

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
print(f"AUTH_URL: {auth_url}")
print("\nOpen this URL in your browser, authorize, then paste the FULL redirect URL back.")
print("(It will redirect to localhost and fail to load — that's fine. Copy the URL from the address bar.)")
