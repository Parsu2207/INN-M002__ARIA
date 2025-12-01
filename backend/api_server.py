# backend/api_server.py
from fastapi import FastAPI, HTTPException, Body, UploadFile, File
from typing import List
import json
from .models import ScoredAlert, Incident
from .correlation_service import list_alerts, list_incidents
from .playbook_engine import execute_playbook
from .correlation_service import add_scored_alert
from .normalizer import normalize_alert
from .enricher import enrich_alert
from .feature_engine import build_features
from .scoring_service import score_alert


app = FastAPI(title="ARIA Desktop Backend API")

@app.post("/api/v1/debug/ingest_raw")
def debug_ingest_raw(alerts: List[dict] = Body(...)):
    """Debug-only: ingest raw alerts, normalize + score + store."""
    injected_ids = []
    for raw in alerts:
        norm = normalize_alert(raw)
        enriched = enrich_alert(norm)
        feats = build_features(enriched)
        scored = score_alert(enriched, feats)
        add_scored_alert(scored)
        injected_ids.append(scored.alert_id)
    return {"inserted": injected_ids, "count": len(injected_ids)}

@app.get("/api/v1/alerts", response_model=List[ScoredAlert])
def get_alerts(priority: str | None = None):
    alerts = list_alerts()
    if priority:
        priority = priority.upper()
        alerts = [a for a in alerts if a.priority_bucket == priority]
    return alerts
