PillPal — Medication Management App
PillPal is a full-stack medication tracking application for individuals managing multiple prescriptions and their caregivers.
What it does

Log and retrieve medications with dosage, timing, and notes
Designed for patients managing multiple medications and caregivers looking after a dependent
Planned: symptom and side-effect logging, caregiver mode, and a pattern recognition layer to surface insights over time

Tech Stack

Backend: Python, FastAPI, SQLite
Frontend: React, TypeScript
Other: Pydantic for request validation, SQLAlchemy for ORM

API Endpoints

GET /pills — retrieve all medications
GET /pills/{id} — retrieve a specific medication
POST /pills — add a new medication
DELETE /pills/{id} — remove a medication

Architecture Notes

Dependency injection for database session management
Pydantic schemas for request validation and response shaping
HTTP exception handling for standard error responses (404 etc.)
Relational data model designed to support multi-user and caregiver relationships

Planned Next

PostgreSQL migration for production readiness
Caregiver mode with patient-caregiver relationships
Symptom and side-effect logging per medication
Pattern recognition layer to surface what's working over time
