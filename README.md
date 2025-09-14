# 🌊 Flood Prediction Project

Predicts **FloodProbability** using environmental and human-impact features. Built week-by-week (Week 1 → Week 3) as a compact learning project.

---

## 📂 Project structure
- `flood_prediction.ipynb` — main Jupyter notebook (EDA, preprocessing, modeling, saving).  
- `flood.csv` — dataset (in this repo).  
- `flood_model.pkl` — pre-trained Random Forest model (~578 MB). **Not stored in GitHub** due to file size limits — stored on Google Drive.  

---

## 📊 Notebook overview
- **Week 1** — Data loading, initial EDA (info, describe, missing values, duplicates, histograms).  
- **Week 2** — Advanced EDA (heatmap, boxplots, scatterplots), skew handling (log1p), MinMax scaling, feature importance via RandomForest, train/test split (80/20).  
- **Week 3** — Baseline (Linear Regression) + Random Forest (n_estimators=200), evaluation (MAE/RMSE/R²), save model to `.pkl`, example sample prediction printed.  

### 🔍 Example sample output

Sample Prediction: \[0.467625] | Actual: 0.455
✅ Model saved in Colab at /content/flood\_model.pkl


## 📈 Model Performance

| Model              | MAE    | RMSE   | R² Score |
|--------------------|--------|--------|----------|
| Linear Regression  | 0.0744 | 0.0919 | 0.745    |
| Random Forest      | 0.0188 | 0.0273 | 0.967    |

---

## 💾 Pre-trained model
The trained Random Forest model is **~578 MB** and exceeds GitHub’s file size limit.  
You can download it here:  

➡️ [Download flood_model.pkl from Google Drive](https://drive.google.com/file/d/1oALoppH8_TY0sDiQysiE-TV_BgYJSTYY/view?usp=sharing)  

**Load directly in Colab**:
```python
!pip install --upgrade gdown
!gdown --id 1oALoppH8_TY0sDiQysiE-TV_BgYJSTYY -O flood_model.pkl

import joblib
model = joblib.load("flood_model.pkl")
print("✅ Model loaded from Google Drive")
````

**Load locally (if you have the file)**:

```python
import joblib
model = joblib.load("flood-prediction/flood_model.pkl")
```

---

## 🚀 How to run locally

1. Clone the repo:

   ```bash
   git clone https://github.com/reneto-unstoppable/flood-prediction.git
   cd flood-prediction
   ```
2. (Optional) Create & activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install pandas matplotlib seaborn scikit-learn joblib gdown
   ```
4. Open `flood_prediction.ipynb` in Jupyter or Colab and run the notebook.

---

## 🔮 Future improvements

* Hyperparameter tuning for Random Forest.
* Try Gradient Boosting or XGBoost.
* Deploy as a web app (Flask, FastAPI, or Streamlit).

---

## ✍️ Author

**Reneto Noble**

📅 Timeline: Week 1 → Week 3

