# Wazuh + Splunk Detection Lab
Initial placeholder.

# 🧠 Wazuh + Splunk Detection Lab

### Overview
A home-lab SOC environment integrating **Wazuh (HIDS)** with **Splunk (SIEM)** for centralized log management, correlation, and detection engineering practice.

### Objectives
- Build and secure a hybrid SIEM pipeline (Wazuh → Splunk).
- Create detections mapped to **MITRE ATT&CK** techniques.
- Automate enrichment and alert notification workflows.

### Tools & Technologies
Wazuh · Splunk · Python · PowerShell · MITRE ATT&CK · Sysmon · Windows/Linux endpoints

### Architecture Diagram
*(Insert a screenshot or draw.io diagram of your log flow here)*

### Detection Examples
| Technique | Rule Summary | MITRE ID |
|------------|--------------|----------|
| Privilege Escalation | Detects `whoami /groups` executed by non-admin users | T1068 |
| Persistence | Detects creation of suspicious autorun keys | T1547 |

### Key Takeaways
- Improved understanding of event correlation and SIEM tuning.  
- Reduced false positives through custom rule logic.  

### Next Steps
- Add dashboard screenshots  
- Write blog summary on LinkedIn/Medium
