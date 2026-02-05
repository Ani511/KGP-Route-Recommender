# 🚦 Smart Route Ranking System using TOPSIS  
A transportation decision-making web app built for IIT Kharagpur, ranking routes based on user-defined preferences like time, traffic, safety, cost, and distance.  

## 📌 Overview

This project implements a decision-support route recommendation system for IIT Kharagpur campus navigation.
Instead of optimizing only for shortest distance or travel time, the system models routing as a multi-criteria decision-making (MCDM) problem, incorporating safety, traffic, road quality, travel time, and distance simultaneously.

The system combines:
- Graph-based route feasibility validation
- Context-aware feature adjustment
- Multi-criteria ranking using the TOPSIS algorithm
to generate personalized, preference-aware route recommendations.
---

## 🧠 Problem Motivation

Traditional routing systems optimize a single objective (typically distance or time).
However, real-world route choice often depends on multiple competing factors such as:
- Safety (especially night-time movement)
- Road quality (affects comfort and risk)
- Traffic density
- Travel time reliability
- Physical distance
This project reframes routing as a decision-support optimization problem, where users define preference weights across criteria, and the system ranks feasible routes accordingly.
---
## 🏗 System Architecture

The system follows a hybrid pipeline:
Graph Feasibility Check (NetworkX)
↓
Candidate Route Extraction (Dataset Alternatives)
↓
Context-Aware Feature Adjustment (Night / Rain / Rush Hour)
↓
TOPSIS Multi-Criteria Decision Ranking
↓
Final Route Recommendation

----
## 🔬 Methodology
###1️⃣ Graph-Assisted Candidate Route Selection
A lightweight campus connectivity graph is modeled using NetworkX.
The graph is used to validate route feasibility and simulate path connectivity before ranking candidate routes.
- This step mimics real-world navigation pipeline stages where:
- Graph traversal ensures route viability
- Ranking modules optimize route choice

### 2️⃣ Context-Aware Feature Adjustment
The system supports simulated environmental context:
-Context	Effect
- Night Mode	Increases safety importance
- Rain Mode	Increases road quality importance
- Rush Hour	Penalizes high traffic routes
This enables dynamic route scoring based on environmental or temporal conditions.

### 3️⃣ Multi-Criteria Decision Ranking — TOPSIS

Routes are ranked using the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS).
TOPSIS works by:
- Normalizing multi-criteria feature values
- Applying user-defined weights
- Computing distance from ideal and anti-ideal solutions
- Ranking routes based on closeness to optimal decision point
This enables balanced optimization across competing routing factors.
---
## ⚙️ Core Features
#### Personalized Route Ranking
Users define importance weights across criteria:
- Safety
- Distance
- Travel Time
- Traffic
- Road Quality

#### Context-Aware Decision Support
Route recommendations adapt based on simulated environmental conditions.

#### Hybrid Graph + MCDM Architecture
Combines structural route feasibility with decision-theoretic ranking.

#### Modular ML Pipeline
Core decision logic is separated into a reusable pipeline module route_ml_pipeline.py

## 🔧 Tech Stack

### 🖥️ Frontend
- HTML5, CSS3
- JavaScript
- Google Maps JavaScript API

### ⚙️ Backend
- Python 3.x
- Flask
### ML / Decision Layer
- Pandas
- NumPy
- NetworkX
- Custom TOPSIS Implementation

---

## ⚙️ Setup Instructions

1. Clone the Repository  
2. Setup Python Environment  
3. Add Google Maps API Key  
4. Run the Flask Server  
5. Open in Browser  
---
## 📘 Project Structure
```
├── frontend/
│   └── index.html
├── app.py
├── topsis.py
├── KGP_Topsis_Dataset
├── requirements.txt
└── README.md
```

---

## 🧠 How It works
1.🧍 User selects a starting point, destination, and adjusts weights for factors like time, cost, safety, etc.
2.🖥️ Frontend sends this input to the Flask backend.
3.📊 The backend first validates route feasibility using a lightweight campus connectivity graph (NetworkX).
This simulates real-world navigation pipelines where graph traversal ensures route connectivity before optimization.
4. 📚 Candidate Route Extraction from Dataset
The backend filters feasible route alternatives from a structured dataset containing route attributes:
- Safety score
- Distance
- Travel time
- Traffic level
- Road quality
5. 🌙 Context-Aware Feature Adjustment (Optional)
If a context mode is enabled (e.g., night travel, rain conditions, rush hour), the system dynamically adjusts feature values before ranking.
Example:
- Night → safety importance increased
- Rain → road quality importance increased
- Rush hour → traffic penalty increased
6. 🧮 Multi-Criteria Ranking via TOPSIS
The filtered and context-adjusted routes are ranked using the TOPSIS multi-criteria decision algorithm.
Routes are scored based on distance from ideal and worst-case decision solutions.
7️. 🚀 Recommendation Output Generation
The backend returns ranked routes, including:
- Route name
- TOPSIS score
- Rank
8️. 🗺️ Interactive Route Visualization
The frontend uses the Google Maps JavaScript API to visualize selected routes and display ranking results interactively.
---

### 🧪 Example Use Case

Scenario:
User prioritizes safety during night travel.
Pipeline Flow:
- Graph validates route connectivity
- Candidate routes extracted
- Safety score boosted via context modifier
- TOPSIS ranks routes based on updated preferences
----

### 🎯 Learning Outcomes

This project demonstrates:
- Applied multi-criteria optimization
- Decision intelligence system design
- Hybrid graph + ranking architectures
- Context-aware feature engineering
- ML pipeline modularization
