
# Room Cleanliness Validation Pipeline : Computer Vision Powered Inspection, Review & Quality Assurance System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-orange)
![ResNet50](https://img.shields.io/badge/ResNet50-FeatureExtraction-yellow)
![Computer Vision](https://img.shields.io/badge/ComputerVision-ImageAnalysis-purple)
![JWT](https://img.shields.io/badge/JWT-Authentication-black)
![Swagger](https://img.shields.io/badge/Swagger-API_Documentation-brightgreen)
![Audit Logging](https://img.shields.io/badge/Audit-Traceability-lightgrey)
![Human Review](https://img.shields.io/badge/Human--in--the--Loop-Validation-teal)




## Overview

In large hospitality operations, room readiness is one of the final control points before a guest experience begins.

A room may be cleaned, inspected, approved, and released dozens of times every day across a property. While housekeeping teams are responsible for execution, supervisors remain accountable for ensuring that rooms meet operational standards before occupancy. The challenge is not cleaning the room. The challenge is validating quality consistently, repeatedly, and at scale.

As room volumes increase, inspection processes become heavily dependent on manual review. Supervisors must evaluate large numbers of rooms within limited operational windows, often relying on subjective visual judgement and inconsistent inspection criteria. Decisions that directly affect room availability, guest satisfaction, and operational efficiency are frequently made without a structured validation framework or an auditable record of how those decisions were reached.

This creates an operational gap.

Quality verification becomes difficult to standardize, inspection outcomes become difficult to explain, and organizations lack a reliable mechanism for distinguishing between inspections that can be trusted and inspections that require additional review.

The Room Cleanliness Validation Pipeline was designed to address this problem.

The platform combines computer vision, confidence-based decision making, human review workflows, and auditability into a single operational quality assurance system. Before-cleaning and after-cleaning room images are analyzed to generate cleanliness and confidence scores that assist inspection decisions while preserving human oversight for uncertain cases.

Rather than treating machine learning as the final authority, the system treats machine learning as an operational decision-support mechanism. Confidence thresholds determine whether inspections can proceed through automated workflows or require supervisor validation. Every action performed throughout the inspection lifecycle is recorded through an auditable event trail, providing transparency across image submissions, scoring operations, reviews, and final approval decisions.

Unlike traditional computer vision projects that focus primarily on classification performance, this project focuses on integrating visual intelligence into a complete operational workflow. Inspection management, confidence-gated decision routing, supervisor review, auditability, and quality assurance are treated as first-class system capabilities.

The result is a structured inspection platform that demonstrates how computer vision can support real-world operational decision making while maintaining accountability, traceability, and human control over business-critical outcomes.

## Project Highlights

* AI-assisted room inspection workflow using before-cleaning and after-cleaning room imagery

* Computer vision-driven cleanliness assessment designed to support operational quality assurance processes

* Confidence-gated decision engine that evaluates prediction reliability before applying automated actions

* Human-in-the-loop review workflow for inspections requiring additional validation and oversight

* Structured PASS, REVIEW, and REJECT inspection routing based on cleanliness and confidence thresholds

* End-to-end inspection lifecycle management from inspection creation through final room approval

* Comprehensive audit logging framework providing complete traceability of inspection and review activities

* JWT-secured REST API architecture supporting room management, inspections, scoring, and supervisor review workflows

* Modular backend design enabling future integration of event-driven processing, analytics, search, and notification services

* Demonstrates the practical integration of computer vision, workflow automation, human oversight, and operational accountability within a real-world inspection process




## System Architecture Overview

The Room Cleanliness Validation Pipeline was designed around a fundamental operational challenge: room inspection decisions must be made quickly, consistently, and with sufficient accountability to support real-world hotel operations.

While room cleaning is performed by housekeeping staff, the responsibility for approving room readiness ultimately rests with supervisors. As inspection volumes increase, maintaining consistent quality standards becomes increasingly difficult. Visual assessments are often subjective, inspection outcomes may vary between reviewers, and operational teams frequently lack a structured mechanism to explain how approval decisions were reached.

The architecture addresses this challenge by transforming room inspections into a structured, traceable workflow that combines computer vision, confidence-based decision routing, human validation, and auditability.

Inspection requests enter the platform through the API layer, where room records, inspection workflows, authentication, and operational data management are handled by dedicated backend services. Before-cleaning and after-cleaning images submitted during the inspection process are stored and forwarded to the computer vision pipeline for analysis.

Within the machine learning layer, visual features are extracted from inspection imagery and used to generate cleanliness and confidence scores. The system is intentionally designed to evaluate both the condition of the room and the reliability of its own assessment. This distinction is a key architectural principle because operational decisions should not depend solely on prediction outputs without considering prediction certainty.

The Confidence & Decision Engine acts as the control point of the platform. Rather than allowing every machine learning prediction to directly influence room approval decisions, confidence thresholds determine the appropriate workflow path. High-confidence outcomes can proceed through automated decision routes, while uncertain inspections are escalated to supervisor review for additional validation. This ensures that machine learning functions as a decision-support capability rather than an uncontrolled decision-making mechanism.

Supervisor review workflows provide human oversight for inspections requiring additional scrutiny. Review outcomes, approval decisions, and operational actions are captured throughout the inspection lifecycle, preserving accountability for business-critical decisions while maintaining efficiency for routine inspections.

To ensure complete traceability, the Audit Service records every significant operational event, including inspection creation, image submissions, machine learning evaluations, review actions, and final approval decisions. This creates a verifiable history of how inspection outcomes were produced, enabling transparency across the entire quality assurance process.

The architecture is intentionally modular, separating workflow management, image analysis, decision routing, review operations, and audit capabilities into independent services. This allows future capabilities such as event-driven processing, notification workflows, analytics platforms, search services, model monitoring, and operational reporting to be introduced without requiring changes to the core inspection lifecycle.

### Architecture Diagram

![System Architecture](docs\Room_Cleanliness_Archi.png)

Together, these components form an operational quality assurance platform that extends beyond image classification by combining computer vision, confidence-aware automation, human oversight, and decision traceability into a unified inspection workflow.


## End-to-End Inspection Workflow

The inspection workflow is designed to ensure that every room approval decision follows a consistent, reviewable, and traceable process. Rather than relying on subjective visual checks alone, the platform introduces a structured validation lifecycle that combines visual analysis, confidence evaluation, human oversight, and auditability.

1. An inspection record is created for a room.
2. Before-cleaning and after-cleaning images are uploaded.
3. Inspection imagery is analyzed through the computer vision pipeline.
4. Cleanliness and confidence scores are generated.
5. The Decision Engine determines the appropriate workflow path.
6. High-confidence outcomes proceed through automated decision routes.
7. Uncertain inspections are escalated for supervisor review.
8. Final decisions are recorded and persisted.
9. Audit events are generated throughout the inspection lifecycle.

The result is a standardized inspection process that improves consistency while preserving accountability for room approval decisions.

---

## Machine Learning Pipeline

The machine learning pipeline provides objective inspection signals that assist room validation decisions. Its purpose is not to replace human judgement, but to support operational quality assurance through repeatable visual analysis.

Before-cleaning and after-cleaning images are processed through a ResNet50-based feature extraction pipeline that converts room imagery into high-dimensional visual representations. These representations are compared to identify meaningful differences between inspection states and generate quantitative measures of room condition.

The pipeline produces three key outputs:

* Cleanliness Score
* Confidence Score
* Machine Learning Decision

By evaluating both room condition and prediction reliability, the platform generates inspection insights that can be incorporated into a broader operational review workflow rather than functioning as isolated model predictions.

---

## Confidence-Gated Decision Engine

Not every machine learning prediction should be trusted equally.

The Confidence-Gated Decision Engine acts as the control layer between model outputs and operational actions by evaluating both cleanliness assessments and prediction confidence before determining the appropriate workflow path.

Rather than allowing every prediction to directly influence room approval decisions, the platform applies confidence-aware routing logic:

* PASS → High-confidence inspections meeting cleanliness requirements
* REVIEW → Inspections requiring supervisor validation
* REJECT → Inspections failing cleanliness standards

This approach enables the system to automate routine inspection outcomes while ensuring that uncertain evaluations remain subject to human review. By treating confidence as a first-class decision factor, the platform balances operational efficiency with quality assurance and risk control.

## Human-in-the-Loop Review Workflow

While machine learning assists inspection evaluations, final operational accountability remains with human reviewers.

The platform incorporates a Human-in-the-Loop review process to ensure that inspections with uncertain outcomes receive additional validation before approval decisions are finalized. Rather than allowing low-confidence predictions to directly influence room readiness decisions, these inspections are routed to supervisors for manual assessment.

During the review process, supervisors can examine inspection details, evaluate machine learning recommendations, and record the final inspection outcome. This approach enables the system to leverage automation for routine scenarios while preserving human judgement for cases requiring additional scrutiny.

By combining machine-assisted analysis with human oversight, the platform balances operational efficiency with quality assurance and decision accountability.

---

## Audit Logging & Traceability

Operational decisions are most valuable when they can be explained, verified, and reviewed.

To maintain transparency across the inspection lifecycle, the platform records significant system events through a centralized audit logging framework. Inspection creation, image uploads, machine learning evaluations, supervisor reviews, and final approval decisions are captured as persistent audit records.

Example audit events include:

* CREATE_INSPECTION
* BEFORE_IMAGE_UPLOADED
* AFTER_IMAGE_UPLOADED
* ML_SCORING_COMPLETED
* SUPERVISOR_REVIEW_COMPLETED

These records provide a complete history of how inspection outcomes were produced, who performed critical actions, and when those actions occurred.

By maintaining an auditable inspection trail, the platform improves operational visibility, supports quality assurance processes, and enables inspection decisions to be reviewed long after the original workflow has been completed.



## Technology Stack

| Category                | Technologies      |
| ----------------------- | ----------------- |
| Programming Language    | Python 3.13       |
| Backend Framework       | FastAPI           |
| API Documentation       | Swagger / OpenAPI |
| Database                | PostgreSQL        |
| ORM                     | SQLAlchemy        |
| Authentication          | JWT               |
| Password Security       | Passlib (bcrypt)  |
| Machine Learning        | PyTorch           |
| Computer Vision         | ResNet50          |
| Image Processing        | Pillow            |
| Data Validation         | Pydantic          |
| Web Server              | Uvicorn           |
| File Storage            | Local File System |
| Database Administration | pgAdmin           |
| Version Control         | Git               |
| Development Environment | VS Code           |



## Database Design

The platform uses PostgreSQL as its primary operational datastore. Inspection workflows, image metadata, scoring results, review decisions, audit events, and user records are persisted to support traceability throughout the inspection lifecycle.

### Core Entities

**Users**

* Authentication and role management
* Housekeeping staff and supervisors

**Rooms**

* Room metadata and operational status

**Room Inspections**

* Inspection records
* Cleanliness scores
* Confidence scores
* ML decisions
* Final review outcomes

**Inspection Images**

* Before-cleaning and after-cleaning image references

**Audit Logs**

* Inspection lifecycle events
* Review activities
* Operational traceability

The schema is designed to preserve relationships between inspections, review actions, machine learning outputs, and audit events while maintaining a complete history of operational decisions.


## API Endpoints

### Authentication

| Method | Endpoint         | Description                        |
| ------ | ---------------- | ---------------------------------- |
| POST   | `/auth/register` | Register a new user                |
| POST   | `/auth/login`    | Authenticate user and generate JWT |
| GET    | `/auth/test`     | Authentication test endpoint       |

### Room Management

| Method | Endpoint  | Description    |
| ------ | --------- | -------------- |
| POST   | `/rooms/` | Create room    |
| GET    | `/rooms/` | Retrieve rooms |

### Inspection Management

| Method | Endpoint                          | Description                  |
| ------ | --------------------------------- | ---------------------------- |
| POST   | `/inspections/`                   | Create inspection            |
| POST   | `/inspections/{id}/upload-before` | Upload before-cleaning image |
| POST   | `/inspections/{id}/upload-after`  | Upload after-cleaning image  |
| POST   | `/inspections/{id}/score`         | Execute ML scoring workflow  |

### Review Workflow

| Method | Endpoint       | Description                       |
| ------ | -------------- | --------------------------------- |
| POST   | `/review/{id}` | Submit supervisor review decision |






## Project Structure

```text
room-cleanliness-validation-pipeline/

├── app/
│   ├── auth/
│   ├── rooms/
│   ├── inspections/
│   ├── review/
│   ├── audit/
│   ├── ml/
│   └── db/
│
├── data/
│   ├── uploads/
│   └── dataset/
│
├── docs/
│   └── images/
│
├── main.py
├── requirements.txt
└── README.md
```

The project follows a modular service-oriented structure that separates authentication, room management, inspection workflows, review operations, audit services, and machine learning components into independent modules.

```
```




## Setup & Installation

### Clone Repository

```bash
git clone <>
cd room-cleanliness-validation-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Create a PostgreSQL database and update database connection settings inside the project configuration.

### Run Database Initialization

```bash
python init_db.py
```

### Start Application

```bash
uvicorn main:app --reload
```

### Access API Documentation

```text
http://127.0.0.1:8000/docs
```




## Sample Inspection Walkthrough

The following example illustrates a complete inspection lifecycle within the platform.

**Room:** 205

**Inspection Created**

* Room inspection record created by housekeeping staff.

**Images Uploaded**

* Before-cleaning image submitted.
* After-cleaning image submitted.

**Machine Learning Evaluation**

* Cleanliness Score: 71.26
* Confidence Score: 0.29
* ML Decision: REVIEW

**Supervisor Validation**

* Inspection escalated for manual review.
* Supervisor Decision: PASS

**Audit Events Generated**

* CREATE_INSPECTION
* BEFORE_IMAGE_UPLOADED
* AFTER_IMAGE_UPLOADED
* ML_SCORING_COMPLETED
* SUPERVISOR_REVIEW_COMPLETED

This workflow demonstrates how the platform combines machine-assisted evaluation, confidence-aware decision routing, human oversight, and operational traceability within a single inspection lifecycle.

---

## Engineering Concepts Demonstrated

* Computer Vision-Based Inspection Validation
* ResNet50 Feature Extraction
* Confidence-Aware Decision Making
* Human-in-the-Loop Review Systems
* Operational Quality Assurance Workflows
* REST API Design and Development
* JWT Authentication and Authorization
* Relational Database Design
* Audit Logging and Traceability
* Modular Service-Oriented Backend Architecture
* Inspection Lifecycle Management
* Production-Oriented Workflow Engineering




## Future Enhancements

The current platform establishes the foundation for AI-assisted inspection validation while providing opportunities for future expansion.

Planned enhancements include:

* Event-Driven Processing using Message Queues
* Microservice-Based Service Decomposition
* Elasticsearch-Powered Inspection Search
* Operational Analytics and Reporting Dashboard
* Real-Time Notification Workflows
* Cloud-Based Image Storage Integration
* Model Monitoring and Performance Tracking
* Multi-Property Inspection Management
* Advanced Supervisor Review Analytics
* Continuous Model Improvement Pipeline

These enhancements can be introduced without significant changes to the core inspection workflow due to the modular architecture of the platform.






