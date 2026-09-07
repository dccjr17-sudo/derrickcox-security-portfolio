# Cloud Security Architecture Review Platform

A portfolio-grade security engineering application for evaluating proposed cloud architectures against core security controls and producing prioritized remediation guidance.

## Why this project exists

Security architecture reviews are often performed through spreadsheets, tickets, and ad-hoc meetings. This project turns that process into a repeatable application workflow that can:

- collect architecture and control information from engineering teams;
- identify security gaps;
- calculate a transparent risk score;
- rank findings by severity;
- recommend remediation actions;
- preserve review history for future reporting and audit evidence.

The initial MVP is **AWS-first**. Azure support will be added after the review engine and workflow are stable.

## MVP capabilities

1. Submit an AWS architecture security questionnaire.
2. Evaluate ten foundational cloud security controls.
3. Return a score from 0-100.
4. Produce Critical / High / Medium / Low findings.
5. Provide remediation guidance for each failed control.
6. Expose the review engine through a FastAPI REST API.
7. Include safe sample data with no employer or production information.

## Security domains covered

- Identity and access management
- Network security
- Encryption
- Secrets management
- Logging and monitoring
- Data protection
- Backup and recovery
- Internet-facing application protection

## Planned architecture

- **Frontend:** Next.js / React
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Cloud:** AWS
- **Infrastructure as Code:** Terraform
- **CI/CD:** GitHub Actions
- **AI enhancement:** Amazon Bedrock or an LLM API for explanation and remediation assistance

## Repository structure

```text
cloud-security-architecture-review-platform/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── risk_engine.py
│   │   └── schemas.py
│   └── requirements.txt
├── docs/
│   └── architecture.md
├── sample-data/
│   └── aws-sample-assessment.json
└── README.md
```

## Local API quick start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the API with Swagger UI.

## Initial API endpoints

- `GET /health` — application health check
- `POST /api/v1/assessments/evaluate` — evaluate an architecture questionnaire

## Portfolio / interview story

This project demonstrates security architecture, cloud security control design, API development, risk modeling, secure software engineering, Infrastructure as Code, CI/CD, and eventually AI-assisted security analysis.

> **Important:** All included examples use synthetic data. No employer, customer, credential, internal hostname, IP address, architecture diagram, or other sensitive information should be committed to this project.
