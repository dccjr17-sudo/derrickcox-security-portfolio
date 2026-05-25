# Microsoft Entra IAM & Zero Trust Lab

## Overview
This hands-on lab focuses on Identity and Access Management (IAM), Zero Trust security principles, Microsoft Entra ID administration, Conditional Access, Identity Protection, and Privileged Identity Management (PIM).

The lab is aligned toward:
- Microsoft SC-300
- Identity & Access Management Engineering
- Zero Trust Architecture
- Microsoft Entra Administration
- Identity Governance

---

# Objectives
- Build enterprise-style IAM controls in Microsoft Entra ID
- Implement Conditional Access policies
- Configure Identity Protection policies
- Implement Privileged Identity Management (PIM)
- Remove standing administrative privileges
- Create break-glass emergency admin accounts
- Practice least privilege and just-in-time elevation

---

# Environment
| Component | Details |
|---|---|
| Identity Platform | Microsoft Entra ID P2 |
| Tenant | SecurityEngineeringLab.onmicrosoft.com |
| Security Stack | Microsoft Defender for Cloud + Defender for Endpoint |
| Cloud Platform | Microsoft Azure |
| IAM Features | Conditional Access, Identity Protection, PIM |

---

# Completed Tasks

## Phase 1 – Foundation & Identity Security

### Microsoft Entra ID P2 Trial
- Activated Microsoft Entra ID P2 licensing
- Enabled advanced IAM security features
- Configured dedicated security lab tenant

### Conditional Access Policies
Implemented:
- Require MFA for Admin Access
- Block Legacy Authentication

Validated policies through:
- Sign-in logs
- Conditional Access reporting
- Authentication testing

### Identity Protection
Configured:
- Sign-in Risk Policy
- MFA enforcement for risky sign-ins
- Risk reporting dashboards

Reviewed:
- Risk detections
- Risky sign-ins
- Risk policy impact analysis

### Privileged Identity Management (PIM)
Implemented:
- Just-in-Time (JIT) Global Administrator elevation
- Temporary privileged role activation
- Time-bound admin sessions
- Approval justification workflow

### Break-Glass Accounts
Created:
- breakglass-globaladmin-01
- breakglass-globaladmin-02

Purpose:
- Emergency tenant recovery
- Administrative lockout prevention
- Enterprise IAM best practice implementation

### Least Privilege Improvements
Removed permanent Global Administrator assignment from primary user account.

Converted:
- Permanent privileged access

Into:
- Eligible assignment
- Time-bound activation
- Auditable elevation workflow

---

# Skills Demonstrated
- Microsoft Entra ID Administration
- Conditional Access
- Identity Protection
- Zero Trust Principles
- Privileged Identity Management (PIM)
- MFA Enforcement
- IAM Governance
- Least Privilege Implementation
- Security Architecture Thinking
- Azure Security Operations

---

# Future Roadmap
## Upcoming Phases
- Access Reviews
- Entitlement Management
- Lifecycle Workflows
- Dynamic Groups
- Role-Based Access Control (RBAC)
- Microsoft Graph API Automation
- PowerShell IAM Automation
- Sentinel Identity Detections
- SC-300 Focused Labs

---

# Career Alignment
This project supports progression toward:
- IAM Engineer
- Identity Security Engineer
- Zero Trust Engineer
- Microsoft Security Engineer
- IAM Architect
- Zero Trust Architect
