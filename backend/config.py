# backend/config.py
KAFKA_BOOTSTRAP_SERVERS = ["localhost:9092"]
KAFKA_ALERT_TOPIC = "aria_alerts"

POSTGRES_DSN = "postgresql://aria:aria@localhost:5432/aria"
ELASTICSEARCH_URL = "http://localhost:9200"

SCORING_SERVICE_URL = "http://127.0.0.1:8000/docs"
API_BIND_HOST = "127.0.0.1"
API_BIND_PORT = 8000

PRIORITY_BUCKETS = {
    "critical": 0.9,
    "high": 0.7,
    "medium": 0.4
}
