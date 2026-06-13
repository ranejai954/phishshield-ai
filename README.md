# 🛡️ PhishShield AI

> AI-Powered Phishing Detection & Threat Analysis Platform

PhishShield AI is an intelligent cybersecurity platform that analyzes suspicious emails, SMS messages, and text-based communications to identify potential phishing attacks. The system leverages Large Language Models (LLMs) through the Groq API to perform threat analysis, calculate risk scores, classify threat levels, and generate detailed security reports.

---

## 🚀 Features

### 🔍 AI-Powered Phishing Detection

* Analyze suspicious emails, SMS messages, and text communications
* Detect phishing indicators using Groq AI
* Identify social engineering tactics and malicious intent

### 📊 Risk Assessment Engine

* Generate phishing risk scores (0–100)
* Classify threats into:

  * LOW
  * MEDIUM
  * HIGH
  * CRITICAL
* Explain detected risks in a human-readable format

### 📄 PDF Report Generation

* Generate downloadable PDF analysis reports
* Include:

  * Analysis ID
  * Risk Score
  * Threat Level
  * Explanation
  * Recommendations

### 🗄️ Analysis History

* Store all analyses in MySQL
* Maintain historical records
* Track previously analyzed messages

### 📈 Security Dashboard

* Total analyses performed
* Average risk score
* Threat distribution metrics
* Security monitoring overview

---

## 🏗️ System Architecture

```text
User Input
    │
    ▼
Streamlit Frontend
    │
    ▼
Groq AI Engine
    │
    ▼
Threat Analysis
    │
    ├── Risk Score
    ├── Threat Level
    ├── Indicators
    └── Recommendations
    │
    ▼
MySQL Database
    │
    ├── History Page
    ├── Dashboard
    └── PDF Reports
```

---

## 🛠️ Tech Stack

| Component       | Technology          |
| --------------- | ------------------- |
| Frontend        | Streamlit           |
| AI Engine       | Groq API            |
| Backend Logic   | Python              |
| Database        | MySQL               |
| PDF Reports     | ReportLab           |
| Deployment      | Hugging Face Spaces |
| Version Control | Git & GitHub        |

---

## 📂 Project Structure

```text
PhishShield-AI/
│
├── ai/
│   └── groq_engine.py
│
├── database/
│   └── db.py
│
├── exports/
│   └── pdfs/
│
├── pages/
│   ├── 1_Analyze.py
│   ├── 2_Dashboard.py
│   └── 3_History.py
│
├── reports/
│   └── pdf_generator.py
│
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/ranejai954/phishshield-ai.git
cd phishshield-ai
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=phishshield
```

---

## 🗄️ Database Setup

Create database:

```sql
CREATE DATABASE phishshield;
```

Create table:

```sql
CREATE TABLE analyses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    analysis_id VARCHAR(20),
    input_type VARCHAR(50),
    input_text TEXT,
    risk_score INT,
    threat_level VARCHAR(20),
    explanation TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ Running The Project

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📋 Workflow

```text
User submits message
        │
        ▼
AI Analysis
        │
        ▼
Risk Assessment
        │
        ▼
Store in MySQL
        │
        ├── Dashboard Analytics
        ├── History Records
        └── PDF Report Generation
```

---

## 🎯 Use Cases

* Cybersecurity Awareness Training
* Phishing Email Analysis
* SMS Scam Detection
* Security Education
* Threat Intelligence Demonstrations
* Student Cybersecurity Projects

---

## 🔮 Future Enhancements

* URL Reputation Checking
* Email Header Analysis
* File Attachment Scanning
* Threat Intelligence Integration
* User Authentication
* SOC Dashboard Enhancements
* Real-Time Threat Monitoring
* API Integration Support

---

## 👨‍💻 Author

**Jai Rane**

Cybersecurity | AI | Cloud Security

GitHub: https://github.com/ranejai954

---

## 📜 License

This project is developed for educational and research purposes as part of the IBM SkillsBuild AI Internship Program.
