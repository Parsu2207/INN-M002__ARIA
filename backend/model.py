#backend/models.py
from typing import List,Dist,Optional
from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
  alert_id:str
  timestamp:datetime
  source:str
  severity:str
  event_type:dist[str,str]
  raw:Dist
  
class ScoredAlert(Alert):
  supervised_prob:float
  anomaly_score:float
  rule_boost:float
  priority_bucket:str
  top_features:List[str]

class Incident(BaseModel):
  incident_id:str
  alerts:List[ScoredAlert]
  created_at:datetime
  entities:Dist[str,str]
  priority_bucket:str
  
 
  
  


