# 🚀 CASH-CANNON: The High-Velocity Agentic Loan Swarm

**CASH-CANNON** is a state-of-the-art, multi-agent AI system designed for **Tata Capital**. It combines **Retrieval-Augmented Generation (RAG)** with an orchestrated **Master-Worker Architecture** to automate the entire loan sales, verification, and underwriting journey.

![CASH-CANNON UI](WEB/static/css/style.css) *Note: High-end glassmorphic UI included.*

---

## 🏗️ Architecture Overview

The system uses a **Master-Worker Swarm** pattern:

1.  **CASH-CANNON Orchestrator (Master Agent)**: The intelligent entry point. It uses RAG to answer complex policy questions and manages the state of the customer journey.
2.  **RAG Knowledge Base**: Powered by **ChromaDB**. It indexes `offer_mart.md` to provide real-time, accurate data on interest rates, KYC requirements, and eligibility.
3.  **Specialized Worker Agents (Tools)**:
    *   **Sales Agent**: Dynamic loan term negotiation based on credit profiles.
    *   **Verification Agent**: Automated identity checks against digital CRM records.
    *   **Underwriting Agent**: Decision engine that applies business rules (Instant vs. Conditional Approval).
    *   **CASH-CANNON Engine**: The high-velocity sanctioning bot that "fires" the final digitized letters.

---

## ✨ Key Features

*   **Dynamic Personalization**: Sanction letters are generated in real-time using customer-entered names.
*   **Intelligent Underwriting**: Automated logic gates for pre-approved limits and credit score thresholds.
*   **Premium Web Experience**: Glassmorphism-based SPA with real-time AI status updates.
*   **Dual Interface**: Fully functional **Interactive CLI** and **Flask Web Portal**.

---

## 🛠️ Tech Stack

*   **Logic**: Python 3.x
*   **AI Orchestration**: Custom Master-Worker Framework
*   **RAG**: ChromaDB (Vector Store), Sentence Transformers (Embeddings)
*   **Backend**: Flask (Web API)
*   **Frontend**: Vanilla JS, Modern CSS (Glassmorphism)
*   **Database**: JSON-based CRM Simulation

---

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/ankushsingh003/CASH-CANNON.git
cd CASH-CANNON

# Install dependencies
pip install flask chromadb sentence-transformers langchain
```

### 2. Run the Web Portal
```bash
python WEB/app.py
```
Open your browser at **`http://127.0.0.1:5000`**.

### 3. Run the CLI Journey
```bash
python integrated_journey.py
```

---

## 📄 Documentation

*   **Presentation Content**: [ppt_content_summary.md](ppt_content_summary.md) - Contains the 5-slide technical breakdown.
*   **Knowledge Base**: [offer_mart.md](offer_mart.md) - The raw policy and product data.
*   **Customer Records**: [dummy_customers.json](dummy_customers.json) - 10 synthetic personas for testing.

---

## 🏆 Use Cases for Testing

| Goal | Customer ID | Amount | Result |
| :--- | :--- | :--- | :--- |
| **Instant Approval** | `C001` | `400,000` | Automated Sanction Letter |
| **Verification Check** | `C004` | `700,000` | Conditional Approval (Upload req) |
| **Credit Rejection** | `C005` | `200,000` | High-Velocity Rejection |

---

**Built with ❤️ for Tata Capital Agentic AI Challenge.**
*Powered by CASH-CANNON.*
