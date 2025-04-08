# 🚦 Smart Route Ranking System using TOPSIS  
A transportation decision-making web app built for IIT Kharagpur, ranking routes based on user-defined preferences like time, traffic, safety, cost, and distance.  

## 📌 Features

- 🔍 **User Inputs:** Select source and destination halls/locations on campus  
- ⚖️ **Custom Weights:** Adjust importance for parameters like time, distance, cost, safety, and traffic  
- 📊 **TOPSIS Algorithm:** Ranks routes based on closeness to the ideal solution  
- 🗺️ **Google Maps API:** Real-time map rendering and route data fetching  
- 💻 **Responsive UI:** Mobile-friendly layout with animations
- 🌀 **Microinteractions:** Smooth transitions and user-friendly interface  

---

## 🔧 Tech Stack

### 🖥️ Frontend
- HTML5, CSS3
- JavaScript
- Google Maps JavaScript API

### ⚙️ Backend
- Python 3.x
- Flask
- NumPy & Pandas (for TOPSIS and data handling)

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

🧠 How It Works
🧍 User selects a starting point, destination, and adjusts weights for factors like time, cost, safety, etc.
🖥️ Frontend sends this input to the Flask backend.
📊 Backend uses a custom dataset (not real-time Maps data) containing route options and their attributes.
🧮 The TOPSIS algorithm (topsis.py) processes the data using the user's weights and ranks the routes.
🚀 Backend sends the ranked results to the frontend.
🗺️ Google Maps API is used for visualizing the selected route(s) interactively on the map.
---

## 📈 Example Use-Case
> "Rank routes from LBS Hall to Technology Market based on 40% time, 20% traffic, 20% safety, 10% cost, 10% distance."

---

## 📌 Future Enhancements
- 🧠 Machine learning for dynamic weight suggestions  
- 🌍 Expand to other halls and destinations  
- 🔄 Route refresh based on live updates  

---
