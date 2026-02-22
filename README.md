# 📡 AI-Powered ILL Root Cause Detection System

An intelligent machine learning system that predicts the root cause of Internet Leased Line (ILL) failures using structured network telemetry data.

Developed for TANFINET Hackathon – Track 5.

---

## 🚀 Problem Statement

Internet Leased Line (ILL) failures can occur due to multiple technical reasons such as fiber cuts, power outages, congestion, hardware failures, or customer-side device instability.

In traditional telecom environments, diagnosing the root cause requires manual log analysis and correlation of several network parameters. This process increases:

- Mean Time to Repair (MTTR)
- SLA breach risk
- Operational overhead
- Customer dissatisfaction

There is a need for an automated and intelligent system capable of instantly identifying the probable cause of failure using real-time telemetry data.

---

## 🧠 Proposed Solution

This project introduces an AI-driven root cause detection system that:

- Ingests structured network metrics
- Uses a trained Random Forest classifier
- Predicts the most probable failure category
- Provides interpretable outputs for engineers
- Exposes REST APIs for seamless integration

The system classifies failures into five categories:

- Fiber Cut  
- Power Failure  
- Hardware Failure  
- Congestion  
- Customer Device Issue  

---

## 📊 Model Performance

The model was trained on a balanced synthetic telecom dataset designed to simulate real-world conditions.

- **Dataset Size:** 2000 records  
- **Noise Injection:** 5% label noise for realism  
- **Train/Test Split:** 80/20  
- **Accuracy:** 95.5%  
- **Macro F1 Score:** 0.95  

The confusion matrix indicates realistic class overlap while maintaining strong predictive performance.

---

## 🔍 Explainable AI

To ensure transparency and engineer trust, the system integrates SHAP (SHapley Additive Explanations) for model interpretability.

The explainability layer:

- Highlights most influential features
- Explains individual predictions
- Aligns model reasoning with telecom domain logic
- Prevents black-box decision making

---

## 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Backend API | FastAPI |
| ML Model | Random Forest (Scikit-learn) |
| Explainability | SHAP |
| Data Handling | Pandas, NumPy |
| Deployment | Uvicorn |
| Environment | Python venv |


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/avadacodavra/ill-root-cause-detection.git
cd ill-root-cause-detection
```
Creation of venv
```bash
python -m venv venv
venv\Scripts\activate
```
Installation of Requirements
```bash
pip install -r requirements.txt
```
Run the API
```bash
uvicorn app:app --reload
```

---

Open in Browser http://127.0.0.1:8000/docs

