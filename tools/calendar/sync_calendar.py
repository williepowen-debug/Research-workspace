"""Sync CALENDAR.md events to Google Calendar."""
import json, os, re
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN_FILE = '/home/moltbot/.openclaw/workspace/tools/calendar/token.json'
CALENDAR_FILE = '/home/moltbot/.openclaw/workspace/CALENDAR.md'
CALENDAR_NAME = 'Research Ops'

# Color IDs: 1=lavender, 2=sage, 3=grape, 4=flamingo, 5=banana, 6=tangerine, 7=peacock, 8=graphite, 9=blueberry, 10=basil, 11=tomato
PRIORITY_COLORS = {
    '🔴🔴': '11',  # tomato
    '🔴': '6',     # tangerine  
    '🟠': '5',     # banana
    '🟡': '8',     # graphite
}

def get_creds():
    with open(TOKEN_FILE) as f:
        token_data = json.load(f)
    creds = Credentials(
        token=token_data['token'],
        refresh_token=token_data['refresh_token'],
        token_uri=token_data['token_uri'],
        client_id=token_data['client_id'],
        client_secret=token_data['client_secret'],
        scopes=token_data['scopes'],
    )
    if creds.expired:
        creds.refresh(Request())
        token_data['token'] = creds.token
        with open(TOKEN_FILE, 'w') as f:
            json.dump(token_data, f, indent=2)
    return creds

def get_or_create_calendar(service):
    """Find or create the Research Ops calendar."""
    calendars = service.calendarList().list().execute()
    for cal in calendars.get('items', []):
        if cal['summary'] == CALENDAR_NAME:
            return cal['id']
    
    new_cal = service.calendars().insert(body={'summary': CALENDAR_NAME, 'timeZone': 'America/New_York'}).execute()
    return new_cal['id']

def parse_calendar_md():
    """Parse CALENDAR.md tables into events."""
    with open(CALENDAR_FILE) as f:
        content = f.read()
    
    events = []
    # Match table rows: | date | event | owner | priority |
    # Also match bold dates like | **3/24** | **FL Wave 1...** | ...
    row_pattern = re.compile(r'\|\s*\*{0,2}~?(\d{1,2}/\d{1,2})\*{0,2}\s*\|\s*\*{0,2}(.*?)\*{0,2}\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|')
    
    current_year = 2026
    current_section = ''
    
    for line in content.split('\n'):
        if '## MARCH' in line:
            current_section = 'mar'
        elif '## APRIL' in line:
            current_section = 'apr'
        elif '## MAY' in line or '## MAY-JUN' in line:
            current_section = 'may'
        elif '## H2' in line:
            current_section = 'h2'
            continue
        elif '## RECURRING' in line:
            break
        
        match = row_pattern.match(line)
        if match and current_section not in ('h2',):
            date_str = match.group(1).strip()
            event_name = match.group(2).strip()
            owner = match.group(3).strip()
            priority = match.group(4).strip()
            
            if not event_name or event_name == 'Event':
                continue
            
            # Parse month/day
            parts = date_str.split('/')
            month = int(parts[0])
            day = int(parts[1])
            
            # Determine color
            color_id = '8'  # default graphite
            for pri_key, color in PRIORITY_COLORS.items():
                if pri_key in priority:
                    color_id = color
                    break
            
            event_date = f'{current_year}-{month:02d}-{day:02d}'
            
            # Clean up event name
            event_name = event_name.strip('*').strip()
            if owner:
                event_name = f"[{owner.strip()}] {event_name}"
            
            events.append({
                'summary': event_name,
                'date': event_date,
                'colorId': color_id,
            })
    
    return events

def sync(dry_run=False):
    creds = get_creds()
    service = build('calendar', 'v3', credentials=creds)
    
    cal_id = get_or_create_calendar(service)
    print(f"Calendar: {CALENDAR_NAME} ({cal_id})")
    
    # Clear existing events from this calendar
    now = '2026-01-01T00:00:00Z'
    existing = service.events().list(calendarId=cal_id, timeMin=now, maxResults=250).execute()
    for event in existing.get('items', []):
        if not dry_run:
            service.events().delete(calendarId=cal_id, eventId=event['id']).execute()
        print(f"  Deleted: {event.get('summary', '?')}")
    
    # Parse and create new events
    events = parse_calendar_md()
    print(f"\nParsed {len(events)} events from CALENDAR.md")
    
    for evt in events:
        body = {
            'summary': evt['summary'],
            'start': {'date': evt['date']},
            'end': {'date': evt['date']},
            'colorId': evt['colorId'],
        }
        if not dry_run:
            service.events().insert(calendarId=cal_id, body=body).execute()
        print(f"  Created: {evt['date']} — {evt['summary']}")
    
    print(f"\nDone! {len(events)} events synced to '{CALENDAR_NAME}'")

if __name__ == '__main__':
    import sys
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("DRY RUN — no changes will be made\n")
    sync(dry_run=dry_run)
