# 🛡️ ML-Based Network Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A machine learning-based Intrusion Detection System that classifies network traffic as **normal or malicious** using multiple ML models — with a real-time web dashboard.

---

## 📸 Dashboard Preview

The web dashboard provides:
- Real-time traffic classification
- Attack type breakdown (DoS, Brute Force, Port Scan, Botnet)
- Model performance comparison
- Live alert feed

---

## 🚀 Features

- ✅ Multi-model comparison: Random Forest, Decision Tree, Logistic Regression, Neural Network
- ✅ Trained on **NSL-KDD** and **CICIDS2017** datasets
- ✅ Achieves **95–98% accuracy** on test data
- ✅ Real-time web dashboard (Flask)
- ✅ REST API for traffic classification
- ✅ Detailed evaluation: Accuracy, Precision, Recall, F1, Confusion Matrix
- ✅ Export trained models as `.pkl` files
- ✅ Jupyter notebook for full walkthrough

---

## 📁 Project Structure

```
ml-ids/
├── src/
│   ├── preprocess.py        # Data loading & preprocessing
│   ├── train.py             # Model training
│   ├── evaluate.py          # Model evaluation & metrics
│   ├── predict.py           # Prediction on new samples
│   └── utils.py             # Helper functions
├── dashboard/
│   ├── app.py               # Flask web application
│   ├── templates/
│   │   └── index.html       # Dashboard UI
│   └── static/              # CSS & JS assets
├── data/
│   └── README.md            # Dataset download instructions
├── models/                  # Saved trained models (auto-created)
├── notebooks/
│   └── IDS_Full_Analysis.ipynb
├── tests/
│   └── test_model.py
├── requirements.txt
├── train_all.py             # One-command training script
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ml-ids.git
cd ml-ids

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📦 Dataset Setup

### Option A — NSL-KDD (Recommended, free)
```bash
# Download from the official source
wget https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt -P data/
wget https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest+.txt  -P data/
```

### Option B — Use Built-in Synthetic Demo Data
```bash
python src/utils.py --generate-demo
# Creates data/demo_traffic.csv for quick testing
```

---

## 🏋️ Training

```bash
# Train all models at once
python train_all.py

# Or train individually
python src/train.py --model random_forest
python src/train.py --model decision_tree
python src/train.py --model logistic_regression
python src/train.py --model neural_network
```

Trained models are saved to `models/`.

---

## 📊 Evaluation

```bash
python src/evaluate.py
```

Example output:
```
Model              Accuracy   Precision  Recall    F1
─────────────────────────────────────────────────────
Random Forest      98.2%      97.8%      98.1%     97.9%
Neural Network     97.6%      97.2%      97.4%     97.3%
Decision Tree      95.3%      94.9%      95.1%     95.0%
Logistic Regression 91.2%    90.7%      91.0%     90.8%
```

---

## 🌐 Running the Dashboard

```bash
cd dashboard
python app.py
```

Visit: **http://localhost:5000**

---

## 🔌 REST API

### Classify a single traffic sample
```bash
POST /api/predict
Content-Type: application/json

{
  "duration": 0,
  "protocol_type": "tcp",
  "service": "http",
  "flag": "SF",
  "src_bytes": 215,
  "dst_bytes": 45076,
  "land": 0,
  "wrong_fragment": 0,
  "urgent": 0
}
```

Response:
```json
{
  "prediction": "normal",
  "confidence": 0.97,
  "model": "random_forest",
  "attack_type": null
}
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 📓 Jupyter Notebook

```bash
jupyter notebook notebooks/IDS_Full_Analysis.ipynb
```

The notebook includes:
1. Exploratory Data Analysis
2. Feature engineering
3. Model training & comparison
4. Confusion matrices & ROC curves
5. Discussion of results

---

## 🎓 Academic Information

**Dissertation Title:** Machine Learning-Based Network Intrusion Detection System for Detecting Cyber Attacks in Real-Time

**Datasets Used:**
- NSL-KDD (Tavallaee et al., 2009)
- CICIDS2017 (Sharafaldin et al., 2018)

**Attack Categories Detected:**
| Label | Attack Type |
|-------|-------------|
| 0 | Normal traffic |
| 1 | DoS (Denial of Service) |
| 2 | Probe / Port Scanning |
| 3 | R2L (Remote to Local) |
| 4 | U2R (User to Root) |

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

## 🤝 Contributing

Pull requests welcome. For major changes, please open an issue first.
