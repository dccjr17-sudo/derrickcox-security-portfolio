# Microsoft Zero Trust Identity Security Lab

## Project Summary

This project documents a hands-on Microsoft identity security and Zero Trust lab focused on Microsoft Entra ID, Conditional Access, Identity Protection, Defender XDR, Sentinel, and security automation.

The goal is to build practical IAM engineering and architecture experience by designing, testing, and documenting identity-centric security controls in a Microsoft cloud environment.

## Career Alignment

This lab supports growth toward roles such as:

- IAM Engineer
- Identity Security Engineer
- Cloud Identity Engineer
- Zero Trust Engineer
- IAM Consultant
- Identity Security Architect

## Lab Architecture

The lab currently uses two environments:

1. **Azure Security Engineering Lab tenant/subscription**
   - Azure VM
   - Microsoft Sentinel
   - Defender for Cloud
   - Defender for Endpoint
   - Defender XDR
   - Logic Apps SOAR automation
   - Network Security Group automated containment

2. **SecurityEngineeringLab Microsoft Entra ID P2 tenant**
   - Microsoft Entra ID P2 trial
   - Conditional Access
   - Identity Protection
   - Named locations
   - Risk-based access policies
   - SC-300 aligned IAM controls

## Completed Capabilities

### SIEM / SOAR Foundation

- Built Azure VM security lab environment
- Configured Log Analytics workspace
- Enabled Microsoft Sentinel
- Created brute-force detection using Windows Security Event ID 4625
- Built analytics rule for possible RDP brute force
- Created Logic App playbook for automated SOC notification
- Added automated NSG containment action to block attacker IP on RDP port 3389
- Validated end-to-end workflow: failed RDP attempts → Sentinel alert → Logic App → NSG deny rule

### Defender XDR / EDR Foundation

- Enabled Defender for Servers Plan 2
- Onboarded VM into Microsoft Defender for Endpoint
- Verified Sense service running on the endpoint
- Generated EICAR test malware detection
- Generated suspicious PowerShell telemetry
- Validated Defender XDR device timeline and incidents

### Identity Security / Zero Trust Foundation

- Created Microsoft Entra ID P2 lab tenant: SecurityEngineeringLab.onmicrosoft.com
- Created Conditional Access policy: Require MFA for Admin Access
- Created Conditional Access policy: Block Legacy Authentication
- Created Named Location: Home Trusted Location
- Created Conditional Access policy: Require MFA Outside Trusted Locations
- Created risk-based Conditional Access policy: Require MFA for Risky Sign-ins
- Reviewed sign-in logs and Conditional Access policy evaluation results
- Explored Identity Protection: Risky users, risky sign-ins, risk detections, and policy migration to Conditional Access

## Key Skills Demonstrated

- Microsoft Entra ID
- Conditional Access
- Identity Protection
- Zero Trust policy design
- Microsoft Sentinel
- Defender XDR
- Defender for Endpoint
- Defender for Cloud
- Logic Apps automation
- Azure NSG security controls
- KQL-based detection logic
- IAM monitoring and sign-in analysis
- Risk-based access control
- Security automation and containment

## Current Project Status

The project has transitioned from a general Azure Security Engineer Lab into an identity-focused Microsoft Zero Trust Identity Security Lab.

Next phases will focus on:

- Privileged Identity Management (PIM)
- Break-glass account design
- Access reviews
- Entitlement management
- Lifecycle workflows
- Microsoft Graph PowerShell automation
- Python-based Graph API reporting
- Sentinel identity detections
- IAM-focused SOAR automation

## Notes

This project is intended for hands-on learning, portfolio documentation, and interview preparation for IAM, cloud identity, and Zero Trust security roles.
