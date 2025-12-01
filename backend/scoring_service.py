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

def simple_anoml_score(feature: dict)-> float:
  hour = feature.get("")
