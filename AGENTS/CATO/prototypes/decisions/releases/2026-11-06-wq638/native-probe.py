import sys,json
from pathlib import Path
sys.path.insert(0,'/tmp/cato-wq638/AGENTS/CATO/prototypes/decisions/mvp')
import notification_hook
payload=json.load(sys.stdin)
result=notification_hook.run(payload,Path('/tmp/wq638-reader'),Path('/tmp/wq638-native-state'),lifetime=900)
Path('/tmp/wq638-native-hook-result.json').write_text(json.dumps(dict(event=payload.get('hook_event_name'),session=payload.get('session_id'),exit=result)))
raise SystemExit(result)
