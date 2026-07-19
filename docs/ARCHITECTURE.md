# AltCredit Nexus - System Architecture

## Overview
AltCredit Nexus is a **privacy-first AI credit scoring platform** designed for New-to-Credit (NTC) individuals and MSMEs in India. It leverages **Graph Neural Networks (GNN)**, **Account Aggregator (AA)** framework, and **Federated Learning** to deliver accurate, explainable, and privacy-preserving credit scores.

---

## High-Level Architecture
User (Mobile/Web)
↓ (Consent via AA)
Frontend (React)
↓ (REST API)
Backend (FastAPI)
↓
AI Layer (GNN + Mock Federated)
↓
Data Layer (Mock AA + GST + UPI)
text---

## Component Breakdown

### 1. Frontend (React + TypeScript)
- Modern, responsive dashboard
- Consent flow simulation
- Real-time score visualization
- Interactive GNN graph (planned)
- SHAP explanation display

### 2. Backend (FastAPI)
- RESTful API with CORS
- Pydantic models for validation
- Router-based modular design
- Easy integration with real AA APIs

### 3. AI/ML Core
- **Graph Neural Network** (SAGEConv)
  - Models user-merchant-transaction relationships
  - Captures complex behavioral patterns
- **Mock Federated Learning** ready (Flower framework)
- Explainable AI using feature importance

### 4. Data Flow
- **Input**: User features (UPI velocity, GST filings, utility, etc.)
- **Processing**: Graph construction → GNN inference → Scoring
- **Output**: Credit score + risk level + explanations

---

## Technology Stack

| Layer          | Technology                     | Reason |
|----------------|--------------------------------|--------|
| Frontend       | React 18 + MUI                 | Fast UI, great components |
| Backend        | FastAPI + Python               | High performance, auto docs |
| AI             | PyTorch Geometric (GNN)        | State-of-the-art graph ML |
| Data           | Mock AA + CSV                  | Ready for real AA integration |
| Privacy        | Federated Learning (Flower)    | No raw data sharing |

---

## Data Privacy & Compliance
- Consent-based (AA framework)
- No raw data stored centrally
- Federated learning design
- Aligned with DPDP Act & RBI guidelines

---

## Future Enhancements
1. Real Account Aggregator integration
2. Neo4j for persistent graph storage
3. Full Federated Learning with multiple banks
4. SHAP force plots in UI
5. Portfolio risk dashboard for lenders
6. Deployment on AWS/GCP with Docker

---

**This architecture is production-scalable and hackathon-demo ready.**

---
