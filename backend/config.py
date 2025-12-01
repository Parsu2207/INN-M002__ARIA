# backend/config.py
KAFKA_BOOTSTRAP_SERVERS = ["localhost:9092"]
KAFKA_ALERT_TOPIC = "aria_alerts"

POSTGRES_DSN = "postgresql://aria:aria@localhost:5432/aria"
ELASTICSEARCH_URL = "http://localhost:9200"

SCORING_SERVICE_URL = "http://127.0.0.1:8000"
API_BIND_HOST = "127.0.0.1"
API_BIND_PORT = 8000

PRIORITY_BUCKETS = {
    "critical": 0.9,
    "high": 0.7,
    "medium": 0.4
}

# Jira integration
JIRA_BASE_URL = "https://shindep2207.atlassian.net"
JIRA_USER_EMAIL = "shindep@gmail.com"
JIRA_API_TOKEN = "ATATT3xFfGF0eHoPWa1A-eRUg4t42bPDQjv5Nbysz3LvRUlH-vPyaOuc6_s7U8-CZxmpRbl8voGkdW_B6yFvKm6EpW0x2KPttdOiPfseB1vvo--wkUg1PrX11BHE5XD053usk3R_kLJgi9e0maGg8GoTCxqGTrCY2gYhJsqOIfbEAb2ddiQR5DY=802E95E8"
JIRA_PROJECT_KEY = "CRM"

# Email (SMTP) integration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "shindep2207@gmail.com"
SMTP_PASSWORD = "Parsu47@22"
ALERT_EMAIL_TO = "shindep2207@gmail.com"




