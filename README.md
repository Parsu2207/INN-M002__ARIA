ARIA 
ARIA is a desktop‑plus‑backend system for security alert triage and incident response.
It ingests raw alerts, normalizes and enriches them, then applies a lightweight ML‑style scoring pipeline to prioritize which alerts matter most for a SOC analyst. 
Scored alerts are exposed via a FastAPI backend and visualized in a PyQt desktop UI, which lets analysts quickly filter on high‑risk events and drill into details. 
Correlated alerts are grouped into incidents, and playbooks can automatically create Jira tickets and send email notifications so response workflows are triggered directly from ARIA
