#backend/scoring_service.py
from .model import ScoredAlert, Alert
from .config import PRIORITY_BUCKETS

def simple_supervised_prob(features: dict) -> float:
  #simple heuristic "model"
  score = 0.0
  score += 0.2 * (features.get("severity_level", 1)
  score += 0.5 * (features.get("ip_reputation", 0.0)
  score += 0.3 * (features.get("is_login_failure", 0)                  
  return max(0.0, min(1.0, score))

def simple_anomaly_score(feature: dict)-> float:
  hour = feature.get("hours_of_day",12)
  #threat lat-night as more anomalous
  if hour < 6 or hour > 22:
    return 0.8
  return 0.2

def compute_priority(supervised_prob: float, anomaly_score:float, rule_boost:float)->float:
  return max(0.0, min(1.0,6.0*supervised_prob+0.3*anamoly_score+0.1*rule_boost))

def bucket_for_score(score:float)-> str:
  if score >= PRIORITY_BUCKETS["critical"]:
    return "CRITICAL"
  if score >= PRIORITY_BUCKETS["high"]:
    return "HIGH"
  if score >= PRIORITY_BUCKETS["medium"]:
    return "MEDIUM"
  return "LOW"

def score_alert(alert_dict:dict, feature:dict)-> ScoredAlert:
  supervised_prob =  simple_supervised_prob(features)
  anamoly_score = simple_anomaly_score(feature)
  rule_boost = 0.0
  if "TA0006" in alert_dict.get("enrichment", {}).get("mitre_tactics", []):
    rule_boost += 0.2
  priority_score = compute_priority
  
  
  

