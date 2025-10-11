# Scripts python
Initial placeholder

```markdown
# 🐍 Python Scripts

Python utilities for detection automation and data enrichment.

### Examples
| Script | Purpose |
|---------|----------|
| `aws_guardduty_alerts.py` | Pulls GuardDuty findings and sends Slack notifications |
| `wazuh_api_connector.py` | Retrieves alerts from Wazuh API for analysis |
| `vuln_trend_report.py` | Aggregates Nexpose/OpenVAS scan trends |

### Dependencies
boto3 · requests · pandas · json · logging

### Usage
```bash
python3 aws_guardduty_alerts.py
