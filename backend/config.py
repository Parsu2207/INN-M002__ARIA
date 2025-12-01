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
JIRA_BASE_URL = "https://your-domain.atlassian.net"
JIRA_USER_EMAIL = "your-user@example.com"
JIRA_API_TOKEN = "your-api-token"
JIRA_PROJECT_KEY = "SOC"

# Email (SMTP) integration
SMTP_HOST = "smtp.yourmail.com"
SMTP_PORT = 587
SMTP_USER = "alerts@yourcompany.com"
SMTP_PASSWORD = "your-smtp-password"
ALERT_EMAIL_TO = "soc-team@yourcompany.com"

# SMS (Twilio) integration
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "your-twilio-token"
TWILIO_FROM_NUMBER = "+15551234567"
ALERT_SMS_TO = "+15557654321"

