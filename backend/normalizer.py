
from datetime import datetime
from .models import Alert


def normalize_alert(raw: dict)->Alert:
  
  alert_id=raw.get("id") or raw.get("_id") or "unknown"
  ts=raw.get("timestamp") or raw.get("@timestamp")
  timestamp=datetime.fromisoformat(ts) if isinstance(ts,str) else datetime.utcnow()

return Alert(
  alert_id=str(alert_id),
  timestamp=timestamp, 
  source=raw.get("source","splunk"),
  severity=raw.get("severity", "medium"),
  event_type=raw.get("event_type",raw.get("sourcetype","unknown")),
  entities={
    "ip"=raw.get("src_ip")or raw.get("ip"),
    "user":raw.get("user")or raw.get("username")
  },
  raw=raw
)
