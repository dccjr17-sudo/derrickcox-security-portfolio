from typing import Callable, Dict, List, Optional, Tuple

from .schemas import AssessmentInput, AssessmentResult, Finding, Severity


ControlEvaluator = Callable[[AssessmentInput], Optional[bool]]


CONTROLS: List[Dict] = [
    {
        "id": "IAM-01",
        "domain": "Identity & Access Management",
        "title": "Privileged accounts require MFA",
        "severity": Severity.CRITICAL,
        "weight": 15,
        "recommendation": "Require MFA for privileged identities and prefer phishing-resistant methods for administrative access.",
        "evaluate": lambda a: a.privileged_mfa_enabled,
    },
    {
        "id": "IAM-02",
        "domain": "Identity & Access Management",
        "title": "IAM follows least privilege",
        "severity": Severity.HIGH,
        "weight": 12,
        "recommendation": "Replace broad permissions with role-based, task-specific access and review unused permissions regularly.",
        "evaluate": lambda a: a.least_privilege_iam,
    },
    {
        "id": "NET-01",
        "domain": "Network Security",
        "title": "Public access is restricted",
        "severity": Severity.CRITICAL,
        "weight": 15,
        "recommendation": "Remove unnecessary public exposure and restrict inbound access using security groups, private subnets, and controlled ingress paths.",
        "evaluate": lambda a: a.public_access_restricted,
    },
    {
        "id": "NET-02",
        "domain": "Network Security",
        "title": "Workloads are segmented",
        "severity": Severity.HIGH,
        "weight": 10,
        "recommendation": "Segment workloads by trust boundary and function, and tightly control east-west traffic between tiers.",
        "evaluate": lambda a: a.network_segmentation_enabled,
    },
    {
        "id": "DATA-01",
        "domain": "Data Protection",
        "title": "Data is encrypted at rest",
        "severity": Severity.HIGH,
        "weight": 10,
        "recommendation": "Enable encryption at rest using AWS-managed or customer-managed KMS keys appropriate to the data classification.",
        "evaluate": lambda a: a.encryption_at_rest_enabled,
    },
    {
        "id": "DATA-02",
        "domain": "Data Protection",
        "title": "Data is encrypted in transit",
        "severity": Severity.HIGH,
        "weight": 10,
        "recommendation": "Require TLS for service-to-service and client communications and disable plaintext protocols.",
        "evaluate": lambda a: a.encryption_in_transit_enabled,
    },
    {
        "id": "SEC-01",
        "domain": "Secrets Management",
        "title": "Application secrets are centrally managed",
        "severity": Severity.HIGH,
        "weight": 8,
        "recommendation": "Store credentials and secrets in AWS Secrets Manager or Systems Manager Parameter Store and rotate them where supported.",
        "evaluate": lambda a: a.secrets_managed_securely if a.application_uses_secrets else None,
    },
    {
        "id": "LOG-01",
        "domain": "Logging & Monitoring",
        "title": "Centralized security logging is enabled",
        "severity": Severity.HIGH,
        "weight": 8,
        "recommendation": "Centralize CloudTrail, service, identity, and application logs in a protected logging destination with alerting and retention controls.",
        "evaluate": lambda a: a.centralized_logging_enabled,
    },
    {
        "id": "RES-01",
        "domain": "Resilience",
        "title": "Stateful workloads have backups",
        "severity": Severity.MEDIUM,
        "weight": 7,
        "recommendation": "Define backup policies, retention, restore testing, and recovery objectives for stateful workloads.",
        "evaluate": lambda a: a.backups_enabled if a.stateful_workloads else None,
    },
    {
        "id": "APP-01",
        "domain": "Application Security",
        "title": "Internet-facing applications use a WAF",
        "severity": Severity.MEDIUM,
        "weight": 5,
        "recommendation": "Place AWS WAF in front of applicable internet-facing web applications and tune managed rules to the application risk profile.",
        "evaluate": lambda a: a.waf_enabled if a.internet_facing else None,
    },
]


def _risk_rating(score: int) -> str:
    if score >= 90:
        return "Low"
    if score >= 75:
        return "Moderate"
    if score >= 60:
        return "High"
    return "Critical"


def evaluate_assessment(assessment: AssessmentInput) -> AssessmentResult:
    applicable_weight = 0
    passed_weight = 0
    passed_controls = 0
    failed_controls = 0
    not_applicable_controls = 0
    findings: List[Finding] = []

    for control in CONTROLS:
        result = control["evaluate"](assessment)

        if result is None:
            not_applicable_controls += 1
            continue

        applicable_weight += control["weight"]

        if result:
            passed_weight += control["weight"]
            passed_controls += 1
        else:
            failed_controls += 1
            findings.append(
                Finding(
                    control_id=control["id"],
                    domain=control["domain"],
                    title=control["title"],
                    severity=control["severity"],
                    weight=control["weight"],
                    recommendation=control["recommendation"],
                )
            )

    score = round((passed_weight / applicable_weight) * 100) if applicable_weight else 100
    findings.sort(key=lambda f: f.weight, reverse=True)

    return AssessmentResult(
        system_name=assessment.system_name,
        cloud_provider=assessment.cloud_provider,
        score=score,
        risk_rating=_risk_rating(score),
        passed_controls=passed_controls,
        failed_controls=failed_controls,
        not_applicable_controls=not_applicable_controls,
        findings=findings,
    )
