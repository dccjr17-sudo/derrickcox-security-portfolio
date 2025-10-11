# Scripts Powershell
Initial placeholder

# ⚡ PowerShell Scripts

Collection of PowerShell scripts for security automation and analysis.

### Examples
| Script | Purpose |
|---------|----------|
| `Collect-EventLogs.ps1` | Gathers Windows Event Logs for offline analysis |
| `Scan-OpenVAS.ps1` | Triggers OpenVAS scans and exports results to CSV |
| `Report-VulnSummary.ps1` | Summarizes scan findings and sends email report |

### Usage
```powershell
.\Collect-EventLogs.ps1 -ComputerName target01 -Days 7
