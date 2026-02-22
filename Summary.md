# CASH-CANNON: The High-Velocity Agentic Swarm - Architecture Summary

This document provides the technical blueprint and content for the 5-slide PPT required for Challenge II.

## 1. System Components
### Core Controller: CASH-CANNON
- **Role**: Main Orchestrator.
- **Function**: Manages the conversation flow, identifies user intent, and delegates tasks to specialized workers.
- **RAG Capability**: Uses `rag_tool.py` to query the `chroma_db` vector database containing product and policy data.

### Specialized Worker Agents (Tools)
1. **Sales Agent** (`worker_sales.py`): Handles loan term negotiation using custom logic.
2. **Verification Agent** (`worker_verification.py`): Simulates CRM lookup using `dummy_customers.json`.
3. **Underwriting Agent** (`worker_underwriting.py`): Implements business rules (Instant vs Conditional Approval).
4. **CASH-CANNON Agent** (`worker_sanction.py`): The high-velocity sanctioning engine.

---

## 2. End-to-End Workflow (The 5-Slide Journey)

### Slide 1: Solution Overview & Architecture
- **Title**: CASH-CANNON: The High-Velocity Agentic Swarm.
- **Concept**: A collaborative multi-agent system that combines Retrieval-Augmented Generation (RAG) with rule-based tool-calling.
- **Key Visual**: Diagram showing CASH-CANNON connecting to a Vector DB and 4 Worker Agents.

### Slide 2: Persona-Driven Engagement (Master Agent)
- **Title**: Intelligent Customer Onboarding.
- **Journey**: Customer asks "What are the current home loan rates?".
- **Action**: Master Agent retrieves precise details from the "Offer Mart" via RAG, providing persuasive, policy-accurate answers and converting interest into a lead.

### Slide 3: Negotiation & Verification
- **Title**: Seamless CRM Integration & Term Negotiation.
- **Journey**: Customer says "I want to apply".
- **Action**: 
    - **Sales Agent** offers personalized terms based on customer profile.
    - **Verification Agent** cross-references KYC details with the CRM database (`dummy_customers.json`) to confirm identity.

### Slide 4: Data-Driven Underwriting
- **Title**: Automated Eligibility & Decisioning Engine.
- **Journey**: System evaluates eligibility.
- **Action**: 
    - **Underwriting Agent** fetches Credit Score from the mock Bureau.
    - **Rule Check**: If Amount <= Pre-approved Limit -> **Instant Approval**.
    - **Rule Check**: If 1x < Amount <= 2x Limit -> **Salary Slip Request** (ensuring <50% EMI/Income ratio).

### Slide 5: Digital Fulfillment & Success
- **Title**: Closing the Loop & Sanction Generation.
- **Journey**: Final approval is granted.
- **Action**: **Sanction Letter Agent** generates a digitally signed document.
- **Impact**: Reduced turnaround time (TAT) from days to minutes, maximizing sales conversion.

---

## 3. Key Technical Highlights
- **Vector Search**: Semantic retrieval for policy accuracy.
- **Deterministic Logic**: Hardcoded business rules for underwriting to ensure compliance.
- **Simulated Environment**: Full ecosystem with dummy CRM, Bureau, and Policy Mart.
