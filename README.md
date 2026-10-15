# derrickcox-security-portfolio
Security Engineer Portfolio | Cloud Detection | SIEM Automation | Vulnerability Management | Wazuh + Splunk Labs

# Derrick Cox | Security Engineer Portfolio

Welcome to my cybersecurity portfolio!  
This repository showcases hands-on projects that demonstrate my work in detection engineering, cloud security, and vulnerability management.

---

## Identity and Access Management Portfolio

Six documented projects cover workforce identity, governance, privileged access, automation, and cloud identity architecture. The collection includes live product labs, local simulations, and design work; those categories are identified below. These are personal learning projects, not claims of enterprise production ownership.

| Project | Evidence type | What I demonstrated |
| --- | --- | --- |
| [Microsoft Entra Identity Security](https://github.com/dccjr17-sudo/entra-identity-security-lab) | Live Entra lab with documented limits | Scoped Conditional Access configuration and What If analysis, contractor review/offboarding, sign-in investigation, read-only Graph auditing, and PIM eligibility/activation/post-end state. |
| [Okta Workforce Identity](https://github.com/dccjr17-sudo/okta-workforce-identity-lab) | Okta product lab plus local SCIM service | MFA, SAML/OIDC federation, manual joiner/mover/leaver exercises, and a Python SCIM service with create/update/deactivate validation. |
| [Identity Governance](https://github.com/dccjr17-sudo/identity-governance-lab) | Local Python simulation | HR-driven roles, access requests, independent approval, access certification, JML, and separation-of-duties controls. Includes 26 personally captured evidence screenshots. |
| [Privileged Access](https://github.com/dccjr17-sudo/privileged-access-lab) | Local Python simulation | Account inventory, safe design, onboarding, time-limited sessions, allowed/denied activities, emergency approval, post-use review, and fictional credential-rotation metadata. |
| [IAM Automation](https://github.com/dccjr17-sudo/iam-automation-lab) | Live Entra + Microsoft Graph lab; offline tests | Created a designated lab user, assigned and transferred group membership, disabled the user, and verified cleanup. Added role, MFA-registration, and stale-account reports; 24 offline tests and 22 live evidence screenshots. |
| [Cloud Identity Security Architecture](https://github.com/dccjr17-sudo/cloud-identity-security-architecture) | Architecture and example policies; no deployment | Entra/Azure RBAC and AWS IAM design, workload identities, exact OIDC trust, least-privilege scope, Zero Trust diagram, security design, and 28 offline checks. |

### Start here

- **Automation and troubleshooting:** [IAM Automation Lab](https://github.com/dccjr17-sudo/iam-automation-lab) — preview/apply behavior, tenant and object checks, membership reconciliation, and evidence.
- **Product identity controls:** [Entra Identity Security Lab](https://github.com/dccjr17-sudo/entra-identity-security-lab) — observed control results separated from What If analysis and unresolved limits.
- **Architecture decisions:** [Cloud Identity Security Architecture](https://github.com/dccjr17-sudo/cloud-identity-security-architecture) — human and workload identity paths, scopes, trust boundaries, and a future live validation plan.

### Evidence and working approach

I personally executed and documented the guided lab exercises. AI assistance supported planning, coding, troubleshooting, and documentation. Repository evidence distinguishes observed behavior from expected results and explains the limits of local tests.

Important distinctions: MFA registration is not proof of enforcement; group names do not grant directory roles; What If matching is not a live denial test; a disabled user does not establish complete session or entitlement revocation; local PAM credential metadata is not a real password rotation; and offline policy checks do not prove cloud enforcement. SailPoint and CyberArk concepts were simulated, rather than implemented in those commercial products.

Lab-demonstrated areas: Microsoft Entra ID, Okta, Microsoft Graph, PowerShell, Python, SAML, OIDC, SCIM, access reviews, PIM, JML, SoD, and audit evidence. Architecture-level coverage: Azure RBAC, AWS IAM, workload federation, managed identities, and Zero Trust design.


---

## Featured Projects

| Project | Description |
|----------|--------------|
| [Basic Kubernetes Cluster](./projects/kubernetes-basic-cluster) | Completed Pluralsight guided lab: initialized a single-node cluster with kubeadm, configured Flannel networking, deployed and scaled nginx, and verified Service access. |
| [Wazuh + Splunk Detection Lab](./projects/wazuh-splunk-detection-lab) | Building a home SOC integrating Wazuh and Splunk for real-time threat detection. |
| [Cloud Detection Automation](./projects/cloud-detection-automation) | Automating AWS GuardDuty alerts and compliance checks using Lambda and Config. |
| [Vulnerability Management Pipeline](./projects/vulnerability-management-pipeline) | Integrating Nexpose/OpenVAS scan data into SIEM dashboards for remediation tracking. |
| [Incident Playbooks](./projects/incident-playbooks) | Practical IR guides and workflows for common attack scenarios. |

---

## Scripts Library
Reusable automation and analysis scripts:
- [PowerShell](./projects/scripts/powershell)
- [Bash](./projects/scripts/bash)
- [Python](./projects/scripts/python)

---

## Labs & Continuous Learning
| Platform | Focus Area | Highlights |
|-----------|-------------|-------------|
| **TryHackMe** | Security Engineer, Blue Team, Threat Hunting | 25+ rooms completed — developed SIEM tuning and Linux forensics skills. |
| **Pluralsight** | Cloud Security, Kubernetes, Splunk, Detection Engineering | Completed [Building a Basic Kubernetes Cluster](./projects/kubernetes-basic-cluster): kubeadm, Flannel, nginx scaling, and NodePort access. Applied lessons to build automated AWS GuardDuty detections. |

---

## Tech Stack
AWS · Splunk · Wazuh · Nexpose · OpenVAS · Python · PowerShell · Bash · Linux · Kubernetes · kubeadm · kubectl · MITRE ATT&CK · SIEM Automation · Azure

---

### 📫 Contact
**LinkedIn**: www.linkedin.com/in/derrickcoxjr
**Email:** dccjr17@gmail.com

