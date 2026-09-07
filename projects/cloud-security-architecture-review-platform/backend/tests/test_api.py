from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_assessment_returns_findings_and_score():
    payload = {
        "system_name": "Synthetic Customer Portal",
        "cloud_provider": "AWS",
        "data_classification": "confidential",
        "internet_facing": True,
        "stateful_workloads": True,
        "application_uses_secrets": True,
        "privileged_mfa_enabled": True,
        "least_privilege_iam": False,
        "public_access_restricted": True,
        "network_segmentation_enabled": True,
        "encryption_at_rest_enabled": True,
        "encryption_in_transit_enabled": True,
        "secrets_managed_securely": False,
        "centralized_logging_enabled": True,
        "backups_enabled": True,
        "waf_enabled": False,
    }

    response = client.post("/api/v1/assessments/evaluate", json=payload)
    body = response.json()

    assert response.status_code == 200
    assert body["score"] == 75
    assert body["risk_rating"] == "Moderate"
    assert body["failed_controls"] == 3
    assert [finding["control_id"] for finding in body["findings"]] == [
        "IAM-02",
        "SEC-01",
        "APP-01",
    ]


def test_non_applicable_controls_are_excluded_from_scoring():
    payload = {
        "system_name": "Synthetic Internal Stateless Service",
        "cloud_provider": "AWS",
        "data_classification": "internal",
        "internet_facing": False,
        "stateful_workloads": False,
        "application_uses_secrets": False,
        "privileged_mfa_enabled": True,
        "least_privilege_iam": True,
        "public_access_restricted": True,
        "network_segmentation_enabled": True,
        "encryption_at_rest_enabled": True,
        "encryption_in_transit_enabled": True,
        "secrets_managed_securely": None,
        "centralized_logging_enabled": True,
        "backups_enabled": None,
        "waf_enabled": None,
    }

    response = client.post("/api/v1/assessments/evaluate", json=payload)
    body = response.json()

    assert response.status_code == 200
    assert body["score"] == 100
    assert body["not_applicable_controls"] == 3
    assert body["failed_controls"] == 0
