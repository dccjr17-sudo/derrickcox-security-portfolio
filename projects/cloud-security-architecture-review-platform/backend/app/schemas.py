from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class DataClassification(str, Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


class Severity(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class AssessmentInput(BaseModel):
    system_name: str = Field(min_length=2, max_length=100)
    cloud_provider: str = Field(default="AWS", pattern="^AWS$")
    data_classification: DataClassification
    internet_facing: bool = False
    stateful_workloads: bool = True
    application_uses_secrets: bool = True

    privileged_mfa_enabled: bool
    least_privilege_iam: bool
    public_access_restricted: bool
    network_segmentation_enabled: bool
    encryption_at_rest_enabled: bool
    encryption_in_transit_enabled: bool
    secrets_managed_securely: Optional[bool] = None
    centralized_logging_enabled: bool
    backups_enabled: Optional[bool] = None
    waf_enabled: Optional[bool] = None


class Finding(BaseModel):
    control_id: str
    domain: str
    title: str
    severity: Severity
    weight: int
    recommendation: str


class AssessmentResult(BaseModel):
    system_name: str
    cloud_provider: str
    score: int = Field(ge=0, le=100)
    risk_rating: str
    passed_controls: int
    failed_controls: int
    not_applicable_controls: int
    findings: List[Finding]
